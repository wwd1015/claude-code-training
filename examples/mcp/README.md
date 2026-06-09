# MCP example — query a local DuckDB warehouse

Backs [Demo 04](../../demos/04-sql-over-mcp.md). Zero infra, no credentials: a local DuckDB file
exposed to Claude over MCP so you can go natural-language → SQL → result → chart.
Official docs: [Connect Claude Code to tools via MCP](https://code.claude.com/docs/en/mcp).

## 1. Build the demo warehouse
```bash
cd demos/setup
pip install duckdb
python gen_warehouse.py        # -> data/warehouse.duckdb (table: trades, view: daily_volume)
```

## 2. Add the MCP server
Two equivalent ways. **Project scope** writes a shared `.mcp.json` (see the sample here).

**CLI (stdio server):**
```bash
claude mcp add --scope project --transport stdio duckdb \
  -- uvx mcp-server-motherduck --db-path "$PWD/data/warehouse.duckdb"
```
Everything after `--` is the command Claude runs. `claude mcp list` to confirm; project-scoped
servers show as `⏸ Pending approval` until you approve them in an interactive session.

**Or copy `.mcp.json`** from this folder to your repo root.

> ⚠️ This example uses the MotherDuck MCP server (`mcp-server-motherduck`), which can serve a
> local DuckDB file. **Verify the package name and flags against its current README**, or swap in
> any DuckDB/SQL MCP server from `modelcontextprotocol/servers`. Requires `uv`/`uvx`
> (https://docs.astral.sh/uv/).

## 3. Ask it things
```
What tables and views are available?
Top 10 days by total volume in Q4, and plot the daily series.
Turn that into a /daily-volume slash command.
```

## Safety
- **Read-only intent.** Never point a demo/training MCP server at a real warehouse with write or
  DDL access. Least privilege always. See [data handling](../../docs/data-handling.md).
- The server — not the prompt — defines what Claude can reach. Scope it deliberately.
