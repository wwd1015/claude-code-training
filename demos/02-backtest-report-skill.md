# Demo 02 — Build a `/backtest-report` skill, live

**Track:** 3a (Skill creation) · **Time:** ~20 min live
**Pre-work:** [Introduction to Agent Skills](https://anthropic.skilljar.com/introduction-to-agent-skills) · [Skills docs](https://code.claude.com/docs/en/skills)

## Objective
Turn a recurring task ("produce a standard report from a backtest result") into a reusable
skill. Teach skill authoring (`SKILL.md`), when a skill beats a one-off prompt, and progressive
disclosure.

## Setup (zero infra)
- **Generate the data:** `cd demos/setup && python gen_backtest_results.py` → writes `data/results.parquet` (`date`, `returns`, `position`, `pnl`) with a seeded drawdown so the report has signal.
- Claude Code open in a repo where `.claude/skills/` can live.

## Live script
1. `I run the same report on every backtest. Let's make it a skill. Create .claude/skills/backtest-report/SKILL.md.`
2. Dictate the spec out loud and have Claude write it: *given a results file, compute CAGR, Sharpe, Sortino, max drawdown, hit rate, turnover; render an equity curve + drawdown chart; write report.md.*
3. `Now run the skill on results.parquet.` → invoke `/backtest-report results.parquet`.
4. Iterate live: `Add a rolling 60-day Sharpe panel and a monthly returns heatmap.`
5. Show the `SKILL.md` — point out the description line (how Claude decides to use it) and the scripts it calls.

## Talking points
- **Skill vs prompt:** a skill is the prompt you stopped retyping — versioned, shareable, discoverable.
- The `description` in `SKILL.md` frontmatter is what makes it auto-trigger. Write it well.
- Commit the skill to a shared repo → the whole desk gets it.
- Compare with `skills/eda/SKILL.md` in this repo as a reference.

## Take-home exercise
Pick a report/transform you run weekly. Author it as a skill. Ship it to the shared repo.

## Time
20 min live + 30–45 min take-home.
