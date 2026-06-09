# Data handling & safety (for quants)

Quants touch market data, positions, and sometimes PII. Claude Code is safe by default, but
you own the boundary. This is the short, practical version — adapt to your firm's policy.

## The permission model (your safety net)
- By default Claude **asks before running commands or editing files**. Read the prompt, approve
  deliberately. Don't reflexively approve.
- **Plan mode** (`shift+tab`) makes it propose first — use it for anything that writes.
- Allowlists speed up *safe, routine* commands only. Don't allowlist `rm`, network calls, or
  anything that writes to shared systems.

## Never put these in a prompt or a commit
- Credentials, API keys, tokens, connection strings → use env vars / a secrets manager.
- Raw PII (names, emails, account ids). Summarize cardinality instead of echoing values.
- Anything your data policy classifies as restricted.

The repo `.gitignore` already excludes `*.csv`, `*.parquet`, `*.duckdb`, `data/`, and `.env*`.
**Keep it that way — data and secrets are never committed.**

## Working with sensitive datasets
- Prefer **de-identified extracts** for demos and training.
- In your `CLAUDE.md`, list sensitive columns and tell Claude not to print or log them (the
  [template](../templates/CLAUDE.research-repo.md) has a slot for this).
- Keep file access **read-only** where you can.

## MCP: least privilege
- An MCP server defines exactly what Claude can reach. **Scope it read-only.**
- Never give a demo/training server write or DDL access to a real warehouse.
- Use a local DuckDB/parquet copy for demos (see [examples/mcp](../examples/mcp/)).

## Hooks as guardrails
You can *enforce* boundaries, not just hope for them:
- A **PreToolUse** hook can block writes outside a directory or block dangerous shell commands.
- A **PostToolUse** hook can run tests/lint automatically so bad edits get caught.
See runnable examples in [examples/hooks](../examples/hooks/). Related workflows: `/careful`, `/guard`, `/freeze`.

## Quick rules
1. Approve deliberately; use plan mode for writes.
2. No secrets/PII in prompts or commits.
3. Read-only on data and MCP by default.
4. De-identified data for anything shared.
5. When unsure, ask in office hours before pointing Claude at production data.
