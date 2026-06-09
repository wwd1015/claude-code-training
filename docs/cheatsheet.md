# Cheatsheet — prompting Claude Code for quant/DS work

One page. Print it. Official depth: [Common workflows](https://code.claude.com/docs/en/common-workflows)
· [Best practices](https://code.claude.com/docs/en/best-practices).

## The loop
**ask → plan → act → verify.** Use **plan mode** (`shift+tab`) for anything that writes more
than one file. Read the diff. Then let it run.

## Prompt patterns that work for research code
- **Be specific about the artifact:** "Write a reusable `profile.py`," not "look at this data."
- **Ask it to run and report real numbers**, not describe: "Load it and tell me the actual null counts."
- **State assumptions you want enforced:** "Returns are daily arithmetic; annualize with 252."
- **Give it the acceptance test:** "It's done when `pytest -q` passes and the equity curve renders."
- **Constrain scope:** "Only touch `src/features.py`. Don't refactor anything else. Don't change data."
- **Make it think first on hard things:** "Before coding, outline 2 approaches and pick one."

## High-leverage recipes
| You want… | Say something like |
|-----------|--------------------|
| Understand an unfamiliar repo | "Map this repo: entry points, data flow, where the model is trained." |
| Profile a dataset | "`/eda data/x.parquet` — shape, nulls, outliers, draft data dictionary." |
| Refactor a notebook | "Promote the reusable logic from `nb.ipynb` into `src/`, add a smoke test, keep behavior identical." |
| Add tests | "Add pytest cases for `backtest.py` covering empty input, NaNs, and a known fixture." |
| Explain a failure | "This traceback — find the root cause before proposing a fix." |
| Standardize a report | "`/backtest-report data/results.parquet`." |
| Batch a check | "Fan out subagents to run `check_one.py` over `data/series/`; return only anomalies." |
| Query data | "(over MCP) top 10 days by volume in Q4, then plot the daily series." |

## Anti-patterns
- Vague asks ("make this better") → vague results. Name the file and the goal.
- Letting it write 10 files unreviewed → use plan mode.
- Pasting sensitive data into prompts → see [data handling](data-handling.md).
- Treating inferred descriptions/labels as truth → you're the domain expert; review them.

## Handy
- `shift+tab` plan mode · `claude -p "..."` headless/batch · `/` to see commands & skills
- `CLAUDE.md` for persistent context · allowlists to stop repeated approval prompts
