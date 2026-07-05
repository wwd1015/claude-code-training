---
id: 501-02
title: "Choosing a Flagship Project"
duration: 38 min
objectives:
  - Apply the five-point selection rubric to candidate projects
  - Recognize the anti-patterns that sink capstones
  - Commit the group to one project with a named owner
  - Write the acceptance check at selection, before any build
---

## The selection rubric

Score each candidate 0–2 on five points; pick the highest total, break ties
toward the most *boring* option:

1. **Recurring** — the task happens weekly or more. Time saved on a one-off is zero.
2. **Painful** — it costs real hours today. "Mildly annoying" won't sustain six weeks.
3. **Checkable** — you can state an acceptance check ("output matches last
   month's hand-built report") — the same discipline as CC 101 module 3.
4. **Data-ready** — every input the system needs is accessible *today*. Waiting
   on access requests kills more capstones than technology does.
5. **Owned** — one named person on the group does this task now and wants it automated.

Seed ideas — skills, fan-out agents, hooks, MCP integrations — are in
[capstone-ideas.md](../../../docs/capstone-ideas.md); start there rather than
from a blank page.

## Anti-patterns

- **The moonshot** — "an agent that does our whole research process." Pick the
  narrowest wedge that saves an hour a week; flagship status comes from *working*.
- **The one-off** — a migration or backfill. Real, but the time saved doesn't recur.
- **The orphan** — nobody in the group does the task. You can't verify what you
  don't do, and adoption dies at demo day.
- **The permission swamp** — needs data access nobody has. Rubric point 4 is a gate, not a score.

## Scope to the window

A good 501 project ships a working increment in week 2 (CC 401's workflow
patterns make this realistic). If your design needs everything built before
anything runs, cut scope until it doesn't.

## Worked example: scoring a pool

A fraud-team [Data Scientist](../../../CONTEXT.md) working group runs the rubric across
four candidates each member brought:

| Candidate | Recur | Pain | Check | Data | Own | Total |
|---|---|---|---|---|---|---|
| Morning data-QA triage (eyeball ~40 feature tables before models train) | 2 | 2 | 2 | 2 | 2 | **10** |
| Build a better churn model | 0 | 1 | 0 | 1 | 1 | 3 |
| Backfill 3 yrs of features into the new store | 0 | 2 | 1 | 2 | 1 | 6 |
| Auto-summarize the weekly model-review deck | 2 | 1 | 1 | 1 | 1 | 6 |

The churn model scores 0 on *Recurring* — it's a [Technique](../../../CONTEXT.md)
exercise, not a chore — and is out. The backfill is a genuine one-off: real pain, but the
hours don't recur. The deck summary is recurring but leans on a subjective acceptance
check and a deck export nobody has automated (a soft *Data-ready*). The triage wins
outright, and it happens to be the most boring option: same anomaly check fanned out over
every table, only the flagged ones bubble up (it starts from the
[`/triage-data`](../../../skills/triage-data/SKILL.md) Seed). At selection the group
writes the acceptance check into the design header: *"Replayed against last Tuesday's
known-good outputs, zero flags; replayed against the March-3 incident snapshot, it flags
`txn_features` and `merchant_agg` and nothing else."* That one sentence is what makes the
build checkable in 501-04.

## Choosing well

### Best practices

- **Pick a task you already own with a measurable baseline.** If you can't say what the
  task costs *today* in hours, you can't prove the win at demo day — and the rubric's
  *Painful* point is a guess, not a number.
- **Scope to a 2–4 week win, then extend.** Ship the narrowest slice that saves an hour a
  week; breadth is a later sprint, not the first one. Flagship status comes from
  *working*, not from ambition.
- **Write the acceptance check at selection.** If you can't state how you'll know a run is
  correct before you build, the task is either not checkable or not understood — either
  way, not ready. This is the same discipline as CC 101 module 3.
- **Treat *Data-ready* and *Owned* as gates, not scores.** A 0 on either kills the
  candidate no matter how painful or exciting it is. Access latency and the orphan
  problem sink more capstones than any technical difficulty.
- **Break ties toward the boring option.** Boring recurring chores have stable inputs and
  an obvious acceptance check; the exciting ones drift mid-build.
- **Score as a group, out loud.** One person's "this is painful" is another's "I do that
  in five minutes." Running every candidate through the same five points in front of the
  group is what surfaces that — and it stops the loudest voice's pet project from winning.

### Common pitfalls

- **The interesting research problem.** "An agent that reads our papers and proposes
  signals" is a Technique showcase: not recurring, not checkable against a known-good
  baseline. Fix: keep it on your research backlog; pick the chore.
- **Deferring the acceptance check.** "We'll figure out how to verify it later" means
  501-04 has nothing to run against. Fix: no acceptance check, no commit.
- **Scoring by total time, not recurring time.** A 20-hour one-off backfill books its
  hours once; a 1-hour weekly chore books them every week forever. Fix: *Recurring* is a
  gate (point 1), not a tiebreaker.
- **Over-scoping on day one** — "…and it should also handle X and Y." Fix: everything past
  the narrowest recurring win goes on the design's out-of-scope list (501-03).

**For quants / For data scientists.** A [Quant](../../../CONTEXT.md) group's boring
recurring wins cluster around reporting and monitoring — the Monday risk report, daily
P&L attribution, factor-refresh sanity checks — and their acceptance checks are exact
(reconcile to the hand-built number). A Data Scientist pod's cluster around data and
pipeline hygiene — QA triage, drift monitoring, feature-store checks — and are often
fan-out shaped (the same check across N tables). The rubric is identical; the shape of
the win differs. See [capstone-ideas.md](../../../docs/capstone-ideas.md) for seeds in
both shapes.

## Lab

Each member brings 2–3 candidates from their own recurring work. Score the
pool against the rubric as a group, discard anything with a 0 on points 1, 4,
or 5, and commit to one project, one owner, one written acceptance check.

**Stretch:** record the full scoring table (like the worked example) in the header of
your `DESIGN.md` so the expert review starts from your reasoning, not a blank page. Fill
the [capstone issue template](../../../.github/ISSUE_TEMPLATE/capstone.md)'s "task
(before)" for the winner, and write its acceptance check as one executable sentence. If
two candidates tie, take the more boring one and note in a line why the other was riskier.

## Knowledge check

1. Which rubric points are hard gates rather than scores, and why?
2. Why break ties toward the boring option?
3. What must be true by week 2, and what do you do if the design can't deliver it?
4. A group member pitches "an agent that reads our research papers and proposes new
   signals." Score it on the five points and say whether it's a 501 Capstone — and if not,
   what it is instead.
5. Why must the acceptance check be written at selection rather than during the build?
