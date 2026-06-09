# Capstone ideas

The capstone = automate one **real, recurring** task. Pick something you do weekly, not a
moonshot. Each idea notes the building block it exercises. Ship it to the shared library when done.

## Good capstones are…
- Something you actually repeat (so the time saved is real).
- Runnable end-to-end without hand-holding.
- Small enough to finish in the capstone window.

## Skill ideas (`/command`)
- **`/eod-report`** — standard end-of-day P&L / risk summary from your results file.
- **`/data-dictionary`** — generate + refresh a data dictionary for a dataset you maintain.
- **`/factor-check`** — run your standard sanity checks on a new factor (coverage, decay, IC).
- **`/notebook-to-script`** — promote a research notebook into a reproducible `src/` module + smoke test.
- **`/regime-plot`** — your usual set of diagnostic plots for a price/return series.

## Agent / fan-out ideas
- **Data QA sweep** — fan out an anomaly check over every series/ticker you track; only flags bubble up. (Start from [`/triage-data`](../skills/triage-data/SKILL.md).)
- **Universe screen** — run the same screen across N instruments in parallel, rank results.
- **Backtest matrix** — run a strategy across parameter sets as parallel subagents, collect a leaderboard.

## Hook ideas
- **Auto-QA** — PostToolUse hook running `pytest`/`ruff` after every edit in a research repo.
- **Data guard** — PreToolUse hook blocking writes to `data/` or to anything outside `src/`.
- **Reproducibility check** — Stop hook that warns if a notebook was changed without rerunning.

## MCP / integration ideas
- **Warehouse Q&A** — read-only MCP to your SQL warehouse; a `/ask-data` command for NL queries.
- **Reference-data lookups** — MCP to an internal reference/market-data API for enrichment.
- **Ticket/notes sync** — MCP to your notes/issue system to log research decisions.

## Demo-day framing (what to show)
1. The task *before* (how long, how manual).
2. What you built (10 sec on the building block).
3. A live run.
4. Time saved per week.

> Submit your capstone as a PR (see [CONTRIBUTING](../CONTRIBUTING.md)) so the next cohort starts ahead.
