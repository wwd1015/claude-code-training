# Demo 04 — Answer a data question end-to-end over MCP

**Track:** 3d (MCP & integrations) · **Time:** ~20 min live
**Pre-work:** [Introduction to MCP](https://anthropic.skilljar.com/introduction-to-model-context-protocol) · [MCP docs](https://code.claude.com/docs/en/mcp)

## Objective
Connect Claude Code to a data source over MCP and go natural-language → query → result →
chart, without leaving the terminal. Teach what MCP is, how to add a server, and how to scope
one for an internal source.

## Setup — source-agnostic, pick one
**Default (zero infra):** a local DuckDB/SQLite file or a folder of parquet, exposed via a
local MCP server (e.g. a DuckDB MCP server from `modelcontextprotocol/servers` or community).
Runs on a laptop, no credentials.

**Internal (decide later):** the real warehouse (Snowflake/BigQuery/Postgres) or a market-data
API via its MCP server. Requires read-only creds + sign-off. Keep this for a follow-up once the
data source is chosen — see the open question in `docs/curriculum.md`.

## Live script
1. `Add the DuckDB MCP server pointing at data/warehouse.duckdb.` (show `claude mcp add` / config)
2. `What tables are available and what's in them?` → Claude lists schema via MCP.
3. `What were the top 10 days by volume last quarter, and plot the daily series?` → NL → SQL → result → chart.
4. `Now turn that into a /daily-volume slash command I can rerun.`
5. Discuss trust boundary: the MCP server controls what Claude can touch — scope it read-only.

## Talking points
- MCP = a typed plug between Claude and your tools/data. The server, not the prompt, defines access.
- Start read-only. Least privilege. Never hand it write/DDL for a demo.
- Once it works locally, the same pattern points at the real warehouse — only the server config changes.

## Take-home exercise
Scope an MCP server for one data source you query daily: which tables, read-only, what
questions it should answer. Bring the scoping note to office hours.

## Time
20 min live + scoping note.
