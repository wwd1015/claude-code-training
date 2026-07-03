---
id: 301-04
title: "MCP I: Concepts & Connecting Servers"
duration: 30 min
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

## Knowledge check

1. What two things does an MCP server expose to Claude?
2. When do you put a server in project scope vs user scope?
3. Your team pulls from the same internal API weekly — shell or MCP, and what's the auth rule?
