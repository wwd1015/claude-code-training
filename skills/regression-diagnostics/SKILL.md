---
name: regression-diagnostics
description: Run a standard diagnostic battery on a linear/OLS regression — coefficients with confidence intervals, R²/adjusted-R², multicollinearity (VIF), heteroskedasticity (Breusch-Pagan), residual normality (Jarque-Bera), autocorrelation (Durbin-Watson), and an ADF stationarity check on flagged series. Use when the user says "regression diagnostics", "check this model", "is my regression sound", "VIF/heteroskedasticity/stationarity", or fits an econometric model and wants it validated.
---

# /regression-diagnostics — econometric model sanity battery

The Quant counterpart to [`/eda`](../eda/SKILL.md). Install by copying this folder to
`.claude/skills/regression-diagnostics/`. Pairs with
[Demo 06](../../demos/06-regression-diagnostics.md).

## Input
A CSV/parquet plus a model spec (a formula like `y ~ x1 + x2 + x3`, or a dependent column and a
list of regressors). Assumes cross-sectional OLS unless the user says time-series/panel — ask if
ambiguous.

## What it produces (`regression_report.md`)
1. **Fit:** OLS coefficients with std errors + 95% CIs, R², adjusted-R², F-test. Offer robust
   (HC3) standard errors.
2. **Multicollinearity:** VIF per regressor; flag VIF > 5 (and > 10 as serious).
3. **Heteroskedasticity:** Breusch-Pagan (and/or White) test; state the verdict.
4. **Residuals:** Jarque-Bera normality, Durbin-Watson autocorrelation, a residual-vs-fitted plot.
5. **Stationarity:** ADF test on the dependent and any regressor that looks non-stationary;
   warn on likely spurious regression if levels are I(1).
6. A one-paragraph plain-English read of whether the model is sound and what to fix.

## Rules
- Use `statsmodels`. Run the tests and report the actual statistics + p-values — never guess.
- State assumptions explicitly (OLS, cross-section vs time-series, significance level).
- Call out the standard pitfalls when present: multicollinearity inflating SEs, heteroskedasticity
  invalidating default SEs (recommend robust), non-stationarity risking spurious regression.
- Read-only on the input file.

## Example
```
/regression-diagnostics data/econ_panel.parquet  y ~ x1 + x2 + x3
```
