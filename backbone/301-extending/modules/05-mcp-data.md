---
id: 301-05
title: "MCP II: Your Data over MCP"
duration: 40 min
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

## Worked example: scoping a warehouse before you connect it

Least privilege here isn't a setting in Claude Code — it's how you provision the
database user the MCP server logs in as. The server can only ever do what that
user can do, so the safest integration is decided in the warehouse, before the
first query. A concrete scoping for a rates desk:

```sql
-- 1. A role that can read, and only read, the curated views.
CREATE ROLE claude_ro NOLOGIN;
GRANT USAGE   ON SCHEMA analytics_curated TO claude_ro;
GRANT SELECT  ON ALL TABLES IN SCHEMA analytics_curated TO claude_ro;
-- No INSERT/UPDATE/DELETE, and no grant on the raw schema at all.

-- 2. A login user the MCP server uses, holding only that role.
CREATE USER claude_mcp LOGIN PASSWORD :'from_secret_manager';
GRANT claude_ro TO claude_mcp;
```

Now point the `warehouse` server's DSN at `claude_mcp`, expose only
`analytics_curated` (not the raw tables), and set a result cap in the server
config so a stray `SELECT *` truncates instead of dumping a billion rows into
context. The four defaults above are now enforced by the *credential*, not by
anyone remembering them. The schema-first pattern then runs against exactly the
surface you meant to expose — Claude orients on `analytics_curated`, and the
tables it never should have seen simply aren't there.

### Best practices

- **Provision least privilege in the database, not in the prompt.** A read-only
  role on curated views is a guarantee; "please don't write" is a hope. The
  credential is the smallest, most durable place to enforce safety.
- **Expose views, not base tables.** Views are where row-level policy, column
  masking, and desk scoping live. Point the server at the view layer and the
  policy travels with every query the agent writes.
- **Cap result size at the server, and prefer aggregates.** Context is finite
  (CC 201). Ask for "daily volume by desk", not "all trades", and let the
  server truncate anything that slips through — a flooded session is a failed
  session.
- **Land a reviewable artifact every time.** The end product of a good data
  session is a saved `.sql` plus its output file, committed — reproducible and
  auditable, not a number that scrolled past in chat.
- **Let Claude read schema first; never paste it in by hand.** The orient step
  is what keeps the SQL correct as tables change. If schema access is missing,
  the model guesses column names — fix the access, don't work around it.

### Common pitfalls

- **Connecting with your own read-write warehouse account "just to test."** The
  agent now inherits your write access, and one bad query can mutate data.
  *Fix:* create the dedicated read-only user first; it's ten minutes that caps
  the blast radius permanently.
- **Pointing the server at raw schemas.** The agent sees ungoverned, un-masked
  data and can exfiltrate PII into the transcript. *Fix:* expose only curated
  views; keep raw out of the grant entirely.
- **No result cap, then a `SELECT *` on a fact table.** The session's context
  fills with rows and everything downstream degrades. *Fix:* set a row limit in
  the server config and steer questions toward aggregates.
- **Treating the chat answer as the deliverable.** Nothing is reproducible if
  the query only ever lived in the conversation. *Fix:* always land the query
  and output as files.

**For quants:** the curated views are usually reference/market data and desk
P&L — scope by desk and date, and land the query next to the model that
consumes it so the pull is reproducible in a backtest. **For data scientists:**
the tables are large and wide, so the result cap and "aggregate, don't dump"
discipline matter most — pull features and counts, not raw event logs, into the
session.

**Reuse (official):** [MCP advanced topics course](https://anthropic.skilljar.com/model-context-protocol-advanced-topics) ·
[MCP docs](https://code.claude.com/docs/en/mcp)

## Lab

Using the DuckDB demo (or a sandbox your team owns): run the four-step
pattern end to end on a question you actually care about, landing a saved
query + output file. Then write a five-line scoping memo for the real thing:
which data source, which schemas/views, who issues the read-only credential,
expected first three questions.

**Stretch goal:** turn the scoping memo into the actual grant. Write the
`CREATE ROLE` / `GRANT SELECT` statements for the read-only user (as in the
worked example), list exactly which views you'd expose, and name the result cap
you'd set. Hand that block to whoever owns the warehouse — a reviewable request
for a scoped, read-only integration is the deliverable your data-platform team
can actually say yes to.

## Knowledge check

1. Why does Claude read the schema before writing SQL, and what goes wrong if it can't?
2. Name the three server-side safety defaults.
3. What's the "landed artifact" at the end of a good data session, and why does it matter for reproducibility?
4. Why enforce read-only in the database credential rather than by instructing
   the agent not to write?
5. **Scenario:** A `SELECT *` on a 2-billion-row fact table returns before you
   can stop it and the session becomes sluggish and confused. Name the two
   server-side defaults that would have prevented this, and the one change to
   how you *phrase* the question that also helps.
