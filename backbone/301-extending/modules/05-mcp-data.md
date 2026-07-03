---
id: 301-05
title: "MCP II: Your Data over MCP"
duration: 30 min
objectives:
  - Run the schema-first querying pattern against a database over MCP
  - Apply the safety defaults: read-only credentials, scoped access, result limits
  - Scope an MCP integration for one data source your team actually uses
---

## The pattern that changes daily work

Once a database is behind an MCP server, "query the warehouse" becomes a
conversation: Claude reads the schema catalog, writes the SQL, runs it,
inspects the result, and iterates — the same agentic loop from CC 101, now
pointed at your data instead of your files.

The **schema-first pattern** (walkthrough:
[demo 04 — SQL over MCP](../../../demos/04-sql-over-mcp.md), runnable setup in
[`examples/mcp/`](../../../examples/mcp/)):

1. **Orient** — "what tables are available, and what's in `trades`?" Claude
   pulls schema before writing any SQL.
2. **Query in plain language** — "daily volume by desk, last quarter, flag
   days over 2σ". Review the SQL it shows you.
3. **Iterate on results** — "now join the reference table and re-cut by
   region". The result of one query informs the next, without you leaving the
   session.
4. **Land the artifact** — "save the final query as `volume_report.sql` and
   the output as parquet". The session's end product is a file in your repo,
   reviewable and rerunnable.

## Safety defaults (non-negotiable)

- **Read-only credentials.** The MCP server's database user should be unable
  to write, full stop. Agent mistakes then have a ceiling.
- **Scope the surface.** Expose the schemas/views the team needs, not the
  whole warehouse; views are also where row-level policy lives.
- **Limit result sizes** in the server config — a `SELECT *` on a billion-row
  table should truncate, not flood the session (context is finite; you learned
  why in CC 201).
- **Your data-handling policy still applies** (CC 101 module 4): the model
  sees returned rows. Sample or aggregate where policy requires.
  <!-- verify: link the org data-handling policy and approved warehouse endpoints via intake -->

## Lab

Using the DuckDB demo (or a sandbox your team owns): run the four-step
pattern end to end on a question you actually care about, landing a saved
query + output file. Then write a five-line scoping memo for the real thing:
which data source, which schemas/views, who issues the read-only credential,
expected first three questions.

## Knowledge check

1. Why does Claude read the schema before writing SQL, and what goes wrong if it can't?
2. Name the three server-side safety defaults.
3. What's the "landed artifact" at the end of a good data session, and why does it matter for reproducibility?

**Reuse (official):** [MCP advanced topics course](https://anthropic.skilljar.com/model-context-protocol-advanced-topics) ·
[MCP docs](https://code.claude.com/docs/en/mcp)
