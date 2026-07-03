---
id: 501-04
title: "Build Sprints: Cadence, Checkpoints, Demos"
duration: 25 min
objectives:
  - Run 2–4 one-week sprints that each end in a working increment
  - Keep a decisions log that makes the writeup and handoff cheap
  - Know when to call the expert (and when not to)
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

## Lab

Run sprint 1. Hold the increment demo, answer the three checkpoint questions,
and make your first three `LOG.md` entries. If the end-to-end slice didn't
run live, the sprint isn't done — narrow it until it runs.

## Knowledge check

1. What qualifies as a sprint "increment"?
2. What goes in the log vs. back into the design doc?
3. Name two good reasons to call the expert and two bad ones.
