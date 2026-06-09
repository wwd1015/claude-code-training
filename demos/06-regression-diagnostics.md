---
title: Build a /regression-diagnostics skill
track: 3a-skills
discipline: quant
department: reference
use_case: econometric-modeling
kind: seed
---

# Demo 06 — Build a `/regression-diagnostics` skill, live (Quant seed)

**Track:** 3a (Skill creation) · **Discipline:** quant · **Time:** ~20 min live
**Pre-work:** [Introduction to Agent Skills](https://anthropic.skilljar.com/introduction-to-agent-skills) · [Skills docs](https://code.claude.com/docs/en/skills)

> The Quant counterpart to [Demo 02](02-backtest-report-skill.md)/[the `/eda` skill](../skills/eda/SKILL.md):
> same SKILL.md mechanics, an econometric use case. Use this anchor with a regression/econometrics
> cohort; use the ML-flavored seeds with a data-science cohort.

## Objective
Turn the standard regression sanity-check a quant runs on every model into a reusable Skill —
coefficients vs. expectation, multicollinearity, heteroskedasticity, residual/normality, and a
stationarity check. Teaches skill authoring on a *traditional-modeling* example.

## Setup (zero infra)
- **Generate the data:** `cd demos/setup && pip install -r requirements.txt && python gen_regression_data.py`
  → writes `data/econ_panel.parquet` with known coefficients and *injected* multicollinearity,
  heteroskedasticity, and a unit-root column (so the diagnostics have something to find).
- `statsmodels` for the stats (`pip install statsmodels`).

## Live script
1. `I run the same diagnostics on every regression. Let's make it a skill: create .claude/skills/regression-diagnostics/SKILL.md.`
2. Dictate the spec, have Claude write it: *given a data file + a formula (y ~ x1 + x2 + x3),
   fit OLS; report coefficients with CIs, R²/adj-R², VIF per regressor, Breusch-Pagan for
   heteroskedasticity, Jarque-Bera on residuals, Durbin-Watson, and an ADF test on any flagged
   non-stationary series.*
3. `Run it on data/econ_panel.parquet with y ~ x1 + x2 + x3.`
4. Verify against the generator's printout: recovered coefficients ≈ true ones; **VIF flags
   x1/x3**; **Breusch-Pagan rejects** (heteroskedastic); **ADF does not reject** on `rw_unit_root`.
5. Iterate live: `Add robust (HC3) standard errors and a residual-vs-fitted plot.`

## Talking points
- A Skill is the diagnostic checklist you stopped re-pasting — versioned and shareable across the desk.
- The `description:` frontmatter is what makes Claude auto-trigger it; write it well.
- Same building block (skill creation) as the DS demos — only the **technique** differs. This is
  the "one Spine, swappable anchor demo" idea in practice.

## Take-home exercise
Pick a model family you run weekly (a factor regression, a VAR, a cointegration test). Author its
standard diagnostics as a Skill and ship it as a **Contributed demo** for your department.

## Time
20 min live + 30–45 min take-home.
