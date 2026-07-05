# Starter skills

Four installable skills that turn recurring DSQ chores into one-line commands.
They double as worked examples for the skill-creation module in
[CC 301](../backbone/301-extending/modules/01-skill-anatomy.md).

| Skill | What it does | Taught in |
|---|---|---|
| [`/eda`](eda/SKILL.md) | First-look profile + draft data dictionary for a CSV/parquet | [Demo 01](../demos/01-eda-data-dictionary.md) |
| [`/backtest-report`](backtest-report/SKILL.md) | Tearsheet from a backtest results file — CAGR, Sharpe, drawdown, charts | [Demo 02](../demos/02-backtest-report-skill.md) |
| [`/regression-diagnostics`](regression-diagnostics/SKILL.md) | OLS diagnostic battery — VIF, Breusch-Pagan, Jarque-Bera, ADF (the quant counterpart to `/eda`) | [Demo 06](../demos/06-regression-diagnostics.md) |
| [`/triage-data`](triage-data/SKILL.md) | Scan many time series, surface only the anomalies, ranked | [Demo 03](../demos/03-anomaly-triage-agent.md) |

## Install

Copy a skill folder into a repo (project-scoped) or your home directory
(everywhere):

```bash
# one repo
mkdir -p .claude/skills && cp -r path/to/skills/eda .claude/skills/

# all repos
mkdir -p ~/.claude/skills && cp -r path/to/skills/eda ~/.claude/skills/
```

Restart Claude Code (or start a new session) and type `/` — the skill appears
in the list. The `description:` frontmatter is what makes Claude auto-invoke
it, so if you adapt a skill, keep the trigger phrases ("profile this data",
"backtest report", …) accurate to how your team actually asks.

## Adapting them

These are seeds, not gospel — swap in your team's conventions (annualization
factor, anomaly thresholds, report format). If your adaptation is genuinely
team-specific, keep it in your team's repo or LOB overlay; if it's universally
useful, contribute it back (see [CONTRIBUTING.md](../CONTRIBUTING.md)).
