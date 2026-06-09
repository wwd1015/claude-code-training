---
name: triage-data
description: Scan a set of time series for anomalies (level shifts, spikes, variance breaks, stale/flat segments) and return only the anomalous ones, ranked by severity, with a short reason for each. Use when the user says "triage", "check these series for anomalies", "data QA", or points at a folder of series and asks what looks wrong.
---

# /triage-data — anomaly triage across many series

Install by copying this folder to `.claude/skills/triage-data/`. Pairs with
[Demo 03](../../demos/03-anomaly-triage-agent.md). For a large set, fan out with subagents
(one checker per series) and consolidate — see the demo.

## Input
A folder of series (CSV/parquet, each with a value column, optionally a date column), or a
single wide table where each column is a series.

## Method (default — swap in your team's standard)
For each series, compute and threshold:
- **Level shift:** rolling-mean change beyond N·(rolling std).
- **Spike:** point beyond N·IQR of its neighborhood.
- **Variance break:** rolling-std ratio across a changepoint.
- **Stale/flat:** runs of (near-)constant values.
Score = max normalized exceedance. Return only series above the score threshold.

> If your org standardizes on a model-based detector (e.g. TabPFN-TS, the LENS approach),
> call that instead of the heuristics above and keep this skill's I/O contract.

## Output
A ranked table: `series_id | verdict | score | reason | where (index/date)`. Only anomalies.
Offer to plot the top K flagged series.

## Rules
- Report only anomalies, ranked — don't dump every series.
- Give a concrete reason and location for each flag (a quant will want to eyeball it).
- State the detection method and thresholds used so results are reproducible.
- Read-only on inputs.

## Example
```
/triage-data data/series/
```
