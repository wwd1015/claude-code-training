# Demo library index

The reusable core of the program. **Seed** demos (below) are program-maintained references;
the library grows with **Contributed** demos from DSQ across departments (see
[CONTRIBUTING](../CONTRIBUTING.md)). Organized by competency/track; everything else is a tag.

## Tag scheme (front-matter on every demo)

```yaml
---
title: <short title>
track: 1-fundamentals | 2-config | 3a-skills | 3b-hooks | 3c-agents | 3d-mcp
discipline: quant | ds | both
department: reference        # "reference" for Seeds; the owning dept for Contributed
use_case: <short-slug>       # e.g. econometric-modeling, data-qa, strategy-evaluation
kind: seed | contributed
---
```

Filter by `discipline` to assemble a cohort: **quant** cohorts get the quant + both demos,
**ds** cohorts get the ds + both demos. Same Spine, swappable anchors (see
[ADR 0001](../docs/adr/0001-single-spine-contributed-demo-library.md)).

## Seed demos

| # | Title | Track | Discipline | Use case |
|---|-------|-------|------------|----------|
| [01](01-eda-data-dictionary.md) | EDA + data dictionary | 1-fundamentals | both | data-profiling |
| [02](02-backtest-report-skill.md) | Build a `/backtest-report` skill | 3a-skills | both | strategy-evaluation |
| [03](03-anomaly-triage-agent.md) | Anomaly-triage subagent | 3c-agents | ds | data-qa |
| [04](04-sql-over-mcp.md) | Answer a data question over MCP | 3d-mcp | both | data-access |
| [05](05-hooks-automation.md) | Hooks: auto-lint + guard data | 3b-hooks | both | automation |
| [06](06-regression-diagnostics.md) | Build a `/regression-diagnostics` skill | 3a-skills | quant | econometric-modeling |

## Contributed demos

_None yet._ Yours goes here — automate a real recurring task (a **Capstone**), tag it
`kind: contributed` with your `department`, and open a PR. A **Champion** sponsors it; a central
maintainer does a light merge review. Rough and niche is fine.

## Data

Generators for the Seed demos live in [`setup/`](setup/) and write to `data/` (git-ignored).
Run `python setup/<gen>.py`; each prints the "right answers" so a facilitator can confirm the
demo lands.
