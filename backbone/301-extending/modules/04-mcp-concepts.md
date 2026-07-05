---
id: 301-04
title: "MCP I: Concepts & Connecting Servers"
duration: 40 min
objectives:
  - Explain what MCP is and what a server provides (tools, resources)
  - Connect a server via .mcp.json and choose the right scope
  - Decide when MCP beats a shell command for reaching a system
---

## What MCP is

The **Model Context Protocol (MCP)** is an open standard for plugging external
systems into Claude Code. An **MCP server** is a small program that exposes a
system — a database, an API, an internal service — as typed **tools** Claude
can call and **resources** it can read. Claude Code is the client; you decide
which servers it may talk to.

Without MCP, Claude reaches other systems by running shell commands. With
MCP, it gets a purpose-built, permission-scoped interface: a warehouse server
exposes `run_query` and the schema catalog, not a general-purpose shell.

## Connecting a server

Servers are declared in `.mcp.json` (or via `claude mcp add`). A minimal
project-level example:

```json
{
  "mcpServers": {
    "warehouse": {
      "command": "npx",
      "args": ["-y", "some-sql-mcp-server", "--db", "analytics.duckdb"]
    }
  }
}
```

**Scope matters:**

- **Project scope** (`.mcp.json` in the repo) — shared with everyone who
  clones; right for team data sources.
- **User scope** (your own config) — follows you across projects; right for
  personal tooling.

On first use, Claude Code asks before trusting a project's servers; MCP tool
calls then flow through the same permission model as everything else (CC 101
module 4). Auth for remote servers is typically an OAuth flow or a token in
an environment variable — never hard-code credentials into `.mcp.json`.
<!-- verify: list org-approved MCP servers and the credential process here via intake -->

## Worked example: a warehouse server the team can share

The whole point of project scope is that the `.mcp.json` is checked in, so the
next person who clones the repo inherits the connection with no setup. But a
checked-in file must not carry a secret. The pattern is **env expansion**: the
config names the variable, each person's shell provides the value.

```json
{
  "mcpServers": {
    "warehouse": {
      "command": "npx",
      "args": ["-y", "some-sql-mcp-server", "--dsn", "${WAREHOUSE_DSN}"],
      "env": { "WAREHOUSE_TOKEN": "${WAREHOUSE_TOKEN}" }
    }
  }
}
```

`${WAREHOUSE_DSN}` and `${WAREHOUSE_TOKEN}` are read from the environment when
Claude Code launches the server — the repo commits the *shape* of the
connection, never the credential. A teammate exports the two variables (from
your secret manager, not a chat message) and the same file just works. The DSN
should point the server at a **read-only** database user; least privilege is
covered in depth in CC 301 module 5.

### Best practices

- **Check `.mcp.json` into the repo, secrets via env expansion — never
  inline.** The config is team infrastructure and should be reviewed and
  versioned like code; the credential is per-person and belongs in the
  environment (`${VAR}`), so a `git log` never leaks a token.
- **Least privilege for the server's credentials.** For a data source, hand
  the MCP server a read-only user. The server defines the whole surface Claude
  can reach, so a narrow credential is your cheapest, strongest guardrail.
- **Prefer a scoped MCP tool over a raw shell for anything recurring.** A
  `run_query` tool that only the warehouse can answer is safer and more legible
  in the transcript than `psql …` in a Bash call — you can see exactly which
  tool ran and approve it by name.
- **Keep the server list short and named for the system.** One server per real
  system (`warehouse`, `tickets`, `metrics`), not a grab-bag. Fewer, clearer
  servers make the permission prompts meaningful.
- **Read a third-party server before you connect it.** An MCP server is code
  that runs on your machine with your environment. Pin the version and skim the
  source or docs, exactly as you would any dependency.

### Common pitfalls

- **A token pasted straight into `.mcp.json`, then committed.** Now it's in the
  git history for everyone with clone access. *Fix:* replace it with
  `${VAR}` expansion and rotate the leaked token immediately.
- **Reaching for MCP when a file is already on disk.** Standing up a server to
  answer "how many rows in this CSV" is pure overhead. *Fix:* if it's a local
  file you'd read once, use the shell; save MCP for the recurring, authed,
  structured system.
- **Assuming a project server is trusted automatically.** Claude Code prompts
  before it will talk to a repo's servers the first time. *Fix:* expect the
  approval prompt on a fresh clone; it's the feature, not a bug.

**For quants:** MCP most often fronts a market/reference database or a pricing
service — a `run_query` tool over curated views. **For data scientists:** it's
more often a warehouse or feature store with very large tables, which makes the
result-limit and scoping defaults in module 5 non-optional rather than nice to
have.

## MCP or a shell command?

| Situation | Reach it via |
|---|---|
| one-off: "how many rows in this CSV" | shell (it's already a file) |
| recurring, structured: "query the warehouse" | MCP server |
| needs auth / scoping / an API | MCP server |
| local script you already trust | shell |

Rule of thumb: if you'd write a wrapper library for it, wrap it as MCP; if
you'd type it once, shell is fine.

**Reuse (official):** [MCP docs](https://code.claude.com/docs/en/mcp) ·
[MCP quickstart](https://code.claude.com/docs/en/mcp-quickstart) ·
[Intro to MCP course](https://anthropic.skilljar.com/introduction-to-model-context-protocol) ·
[Reference servers](https://github.com/modelcontextprotocol/servers)

## Lab

Connect one MCP server in a scratch repo — the DuckDB demo in
[`examples/mcp/`](../../../examples/mcp/) works out of the box. Confirm:
(1) Claude Code lists the server's tools, (2) a natural-language question
routes through an MCP tool call (watch the permission prompt name the tool),
(3) removing the `.mcp.json` entry removes the capability.

**Stretch goal:** convert the demo's config to the env-expansion pattern above.
Move any connection string into a `${VAR}`, export it in your shell, and
confirm the server still starts. Then `unset` the variable and watch the server
fail to launch — that failure is the proof your secret was never in the file.

## Knowledge check

1. What two things does an MCP server expose to Claude?
2. When do you put a server in project scope vs user scope?
3. Your team pulls from the same internal API weekly — shell or MCP, and what's the auth rule?
4. Why is a scoped `run_query` MCP tool safer to approve than the equivalent
   `psql …` shell command, even though both hit the same database?
5. **Scenario:** A teammate commits `.mcp.json` with a live warehouse token
   inline "just to get it working." Name the two things you do, in order, and
   what the corrected config looks like.
