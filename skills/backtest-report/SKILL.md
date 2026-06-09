---
name: backtest-report
description: Produce a standard performance report from a backtest result file (date + returns/pnl, optional position) — CAGR, Sharpe, Sortino, max drawdown, hit rate, turnover, plus equity-curve, drawdown, and monthly-returns-heatmap charts written to a report. Use when the user says "backtest report", "performance summary", "tearsheet", or points at a results file of strategy returns.
---

# /backtest-report — strategy performance report

Install by copying this folder to `.claude/skills/backtest-report/`. Pairs with
[Demo 02](../../demos/02-backtest-report-skill.md).

## Input
A CSV or parquet with at least `date` and `returns` (or `pnl`); optional `position` for turnover.
Returns are assumed daily and arithmetic unless the user says otherwise — ask if ambiguous.

## What it produces (`report.md` + `figs/`)
1. **Headline metrics:** CAGR, annualized vol, Sharpe, Sortino, Calmar, max drawdown (+ dates),
   hit rate, average win/loss, best/worst day.
2. **Turnover** (if `position` present): mean daily turnover, holding period.
3. **Charts:** equity curve (log option), drawdown underwater plot, monthly-returns heatmap,
   rolling 60-day Sharpe.
4. **report.md** that embeds the figures and a one-paragraph plain-English summary.

## Rules
- Annualize with 252 trading days unless told otherwise; state the assumption in the report.
- Compute, don't estimate — run the numbers on the actual file.
- Be explicit about return convention (arithmetic vs log) and any NaN handling.
- Do not invent a benchmark; only compute relative metrics if a benchmark column is provided.
- Read-only on the input file.

## Example
```
/backtest-report data/results.parquet
```
