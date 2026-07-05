---
id: 501-04
title: "Build Sprints: Cadence, Checkpoints, Demos"
duration: 32 min
objectives:
  - Run 2–4 one-week sprints that each end in a working increment
  - Keep a decisions log that makes the writeup and handoff cheap
  - Know when to call the expert (and when not to)
  - Wire the acceptance check in early so every run self-verifies
---

## One-week sprints, working increments

Structure the build as 2–4 sprints of one week. The rule that keeps groups
honest: **every sprint ends with a live run of something real**, demoed inside
the group — not slides, not "it almost works." Sprint 1's increment is the
week-2 demoable slice from your design doc; later sprints widen it toward the
acceptance check.

A useful default split:

- **Sprint 1** — thinnest end-to-end path: real input → automated step → real output, however narrow.
- **Sprint 2** — widen coverage; wire in the acceptance check so every run self-verifies.
- **Sprint 3–4** — failure-mode catches from the design doc; polish for someone-else-can-run-it.

## The decisions log

Keep a `LOG.md` next to `DESIGN.md`: date, decision, why, what you tried that
failed. Two minutes per entry. It becomes the writeup in 501-05, the handoff
when a group member rotates, and the honest record of what the acceptance
check caught. (Your CC 201 `CLAUDE.md` should tell Claude to append to it.)

## Checkpoints with the group

The weekly demo is the checkpoint. Three questions after each one:

1. Did the increment run live against the acceptance check?
2. What did the log record this week — any design-doc decision now wrong?
3. Is next week's increment still the right next slice?

If the design doc changed, note it in the doc, not just the log — the doc is
what the expert reviewed.

## When to call the expert

**Call** when: blocked > half a day on a Claude Code mechanism (permissions,
MCP auth, hook not firing); an architecture decision is being reversed; the
acceptance check keeps failing for reasons the group can't diagnose.
**Don't call** for: code review of working increments, scope debates (that's
the group's call), or anything the docs answer in ten minutes.

## Worked example: three sprints on data-QA triage

The fraud-team pod from 501-02 builds its morning triage across three one-week sprints:

- **Sprint 1 — thinnest path.** Run the existing single-table anomaly check on *one*
  table, live, from a `/triage-data` invocation, printing one line: `txn_features: OK`.
  Ugly, but it ran against last night's real data and demoed to the pod in three minutes.
- **Sprint 2 — widen + wire the check.** Fan the check out across all ~40 tables as
  subagents; only flagged tables bubble up. Then wire the acceptance check from the design
  doc: replay last Tuesday (known-good) → zero flags; replay the March-3 incident snapshot
  → flags `txn_features` and `merchant_agg`, nothing else. From here every run
  self-verifies green/red instead of being eyeballed.
- **Sprint 3 — catches + polish.** Add the design-doc failure-mode catches (a renamed
  column that read as all-null had slipped through → assert schema; a table that failed to
  load looked falsely "clean" → assert freshness and row-count > 0). Polish so the pod's
  on-call can run it: one command, a short README.

Two `LOG.md` entries from that build:

```
2026-05-04  Chose subagent fan-out over a sequential loop. Why: 40 tables in parallel
            keeps the morning run under 2 min; the loop version took ~9 min. (501-03 layer
            choice held.)
2026-05-11  Added a freshness assert. Why: a table that failed to load showed zero
            anomalies — falsely clean. The known-incident replay caught it, not us.
```

## Running the sprints well

### Best practices

- **Demo early and ugly.** A three-minute live run of one table in sprint 1 beats a
  polished thing in week 4 that nobody watched evolve. Ugly-but-real surfaces wrong
  assumptions while they're still cheap to fix.
- **Every sprint ends in a live run against real data.** Not slides, not "it almost
  works." If the end-to-end slice didn't run, the sprint isn't done — narrow it until it
  does.
- **Wire the acceptance check in by sprint 2, so every run self-verifies.** Once the
  replays are wired you stop eyeballing correctness and start trusting green/red — that's
  what lets you widen coverage without fear of silently breaking what worked.
- **Thin end-to-end before wide.** Real input → automated step → real output on one slice,
  *then* fan out. A wide-but-broken pipeline can't be demoed; a narrow-but-working one can.
- **Keep the decisions log at two minutes an entry.** Date, decision, why, what failed.
  It's the writeup in 501-05, the handoff when someone rotates, and the honest record of
  what the acceptance check caught. Have your CC 201 `CLAUDE.md` tell Claude to append to it.
- **Call the expert for mechanisms, not scope or code review.** Blocked half a day on MCP
  auth or a hook not firing → call. Scope debates and reviewing working increments are the
  group's job.

### Common pitfalls

- **Building everything before running anything.** The pipeline that only runs once it's
  "complete" is the one still not running at demo day. Fix: thin end-to-end path, live, in
  sprint 1.
- **The "it almost works" demo.** A screenshot, or a run that erred "but here's what it
  would show." Fix: no live run, no checkpoint — narrow the increment until it runs.
- **Sprints that slip without narrowing.** "We just need another week," repeated. Fix:
  hold the date, cut the increment; a smaller thing that runs beats a bigger thing that
  doesn't.
- **Neglecting the log until the writeup.** Reconstructing six weeks of decisions the
  night before demo day. Fix: two minutes per decision, in the moment.
- **Gold-plating before the acceptance check passes.** Prettifying output while the core
  still miscounts. Fix: green check first, polish last (sprint 3).

**For quants / For data scientists.** For a [Quant](../../../CONTEXT.md) the thin
end-to-end slice is usually one book or one report section reconciled to the hand-built
number, and "widen" means more books and more cuts. For a
[Data Scientist](../../../CONTEXT.md) the thin slice is one table or one check, and
"widen" means the fan-out across the universe. The sprint rule doesn't change — each
sprint ends in a live run against real data — only what "wider" points at.

## Lab

Run sprint 1. Hold the increment demo, answer the three checkpoint questions,
and make your first three `LOG.md` entries. If the end-to-end slice didn't
run live, the sprint isn't done — narrow it until it runs.

**Stretch:** before sprint 2, wire your acceptance check into the run so it self-verifies
green/red, and add a `CLAUDE.md` line telling Claude to append every decision to `LOG.md`.
At the sprint-2 demo, run against the check live in front of the group — the demo *is* the
check passing, not you asserting that it does.

## Knowledge check

1. What qualifies as a sprint "increment"?
2. What goes in the log vs. back into the design doc?
3. Name two good reasons to call the expert and two bad ones.
4. It's the sprint-2 demo and the group shows a screenshot of last week's successful run
   because "today's data isn't loaded yet." Is the sprint done? What should they do?
5. Why wire the acceptance check in by sprint 2 rather than saving verification for the end?
