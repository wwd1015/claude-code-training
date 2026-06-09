---
title: Anomaly-triage subagent
track: 3c-agents
discipline: ds
department: reference
use_case: data-qa
kind: seed
---

# Demo 03 — Anomaly-triage subagent that fans out over many series

**Track:** 3c (Building agents) · **Time:** ~20 min live
**Pre-work:** [Introduction to Subagents](https://anthropic.skilljar.com/introduction-to-subagents) · [Subagents docs](https://code.claude.com/docs/en/sub-agents)

## Objective
Show the multi-agent pattern: one orchestrator fans out over many time series, each checked
independently, only anomalies bubble up. Teach subagents, when fan-out beats one big prompt,
and headless/batch use for unattended jobs.

## Setup (zero infra)
- **Generate the data:** `cd demos/setup && python gen_series.py` → writes `data/series/*.csv` (200 series, 12 with injected level-shifts/spikes) and `data/series_truth.csv` (ground truth, so you can confirm the agent found them).
- A simple anomaly check the audience trusts (z-score / rolling-IQR is fine; or reference the
  LENS `/triage-data` TabPFN-TS approach if that's the internal standard).

## Live script
1. `We have ~200 series in series/. I want to flag anomalous ones. First write check_one.py that takes a path and returns a verdict + score.`
2. `Now use subagents: fan out one checker per series, collect verdicts, and give me only the anomalous ones ranked by score.`
3. Watch the orchestrator spawn parallel checkers; show the consolidated report.
4. `Re-run as a headless batch I could cron nightly` → show `claude -p` / Agent SDK framing.
5. Discuss: each checker is blind to the others — that's the point (isolation + parallelism).

## Talking points
- **Fan-out vs one prompt:** independent checks are cheaper, parallel, and don't pollute context.
- This is exactly the multi-agent research pattern, applied to data QA.
- Ties to existing LENS `/triage-data` work — natural growth path from one skill to an agent.
- For production: headless mode + a schedule, output to a dashboard/alert.

## Take-home exercise
Sketch (and stub) a subagent for a fan-out task you have: many tickers, many files, many
configs. Bring the design to office hours.

## Time
20 min live + design exercise.
