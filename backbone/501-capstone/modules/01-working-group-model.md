---
id: 501-01
title: "The Working-Group Model"
duration: 28 min
objectives:
  - Describe the working-group format and how it differs from a cohort
  - Name the three roles (group, Champion, expert) and who does what
  - Set up a group's cadence from kickoff to demo day
  - Keep the expert in a support role and the weekly slot demo-driven
---

## What a working group is

CC 501 is not a class. It's a **working group**: 3–6 people from one team who
already finished CC 401, delivering one real project together over ~4–6 weeks.
The group operates itself — the program supplies structure, review, and expert
help, not instruction. The output is a working agent system and a measured
time-saved number; the program's goal is that the best of these become
**flagship projects** that recruit the next wave.

## The three roles

- **The group** (Learners) — owns the project end to end: picks it, designs it,
  builds it, demos it. Everyone builds; nobody audits.
- **The Champion** — your department's standing lead
  ([operating model](../../../docs/operating-model.md)): convenes the group,
  keeps the cadence, clears local blockers, sponsors the final contribution.
- **The expert** — an experienced builder (central program owner or senior
  Champion) who **supports, not runs**: one architecture review, on-call for
  unblocking, and a demo-day reviewer. If the expert is writing your code, the
  scope is wrong.

## The cadence

| Week | What | Module |
|---|---|---|
| 0 | Kickoff: pick the project | 501-02 |
| 1 | Design doc + architecture review with the expert | 501-03 |
| 2–4 | Build sprints, weekly increment demos within the group | 501-04 |
| 5 | Measure, write up, contribute | 501-05 |
| 6 | Demo day | 501-05 |

Compress or stretch a week either way; never skip the review or the measurement.

## Why a group, not a cohort

A [Cohort](../../../CONTEXT.md) teaches the Spine to a room of Learners; a working
group *ships one thing*. The difference is the deliverable. A cohort's output is trained
people; a working group's output is a running agent system, a measured time-saved number,
and — if it's good — a [Contributed demo](../../../CONTEXT.md) the next group starts from.
That's why the format is small (3–6), single-team, and time-boxed: you're not covering
material, you're converging on a shipped [Capstone](../../../CONTEXT.md). If your group
finds itself re-teaching CC 301/401 content, that's a signal someone should have finished
the prerequisite first — the working group assumes the Spine is already in hand.

## A working group, week 0 to demo day

A rates-desk team of four finishes CC 401 and convenes. One of them — the person who
hand-builds the Monday risk summary every week — owns the Capstone. The desk
[Champion](../../../CONTEXT.md) books the six slots and starts a read-only warehouse
credential request on day one. A senior Champion from another department agrees to one
30-minute design review and to sit in the demo-day audience; that is the entire expert
commitment. Week 0 the group picks the task (501-02). Week 1 they write the one-page
design doc and run the review (501-03). Weeks 2–4 are three one-week sprints, each ending
in a live run demoed to the four of them (501-04). Week 5 the owner measures before/after
on a real Monday; week 6 they demo to two adjacent desks (501-05). Total expert time:
roughly 90 minutes across six weeks. That ratio — the group builds, the expert reviews —
*is* the model. If it inverts, the scope was wrong.

## Running the group well

### Best practices

- **One team, one room.** Draw the group from a single Department so the schedule, the
  data access, and the task itself are already shared. A group stitched across desks
  spends its cadence reconciling calendars instead of shipping.
- **Cadence is the mechanism, not the meeting.** Six dated slots on calendars beat any
  amount of enthusiasm. Keep the meetings short, regular, and demo-driven — the live run
  *is* the agenda. Groups that "meet when we can" stall by week 2.
- **Everyone builds; nobody only reviews.** The group owns the code end to end. Give the
  Capstone to the one person who does the task today, and have the rest build alongside —
  you cannot verify, or later adopt, a task nobody in the room performs.
- **Protect the expert-supports-not-runs line.** Use the expert for one architecture
  review, on-call unblocking, and the demo-day read. The moment the expert is typing your
  code, rescope (501-02) rather than borrow their hands.
- **Clear access on day one.** Whatever credential or grant the Capstone needs, the
  Champion starts the request in week 0. Access latency, not code, is what slips working
  groups (501-02, rubric point 4).
- **Fix demo day before you start.** Working backward from a named date keeps scope
  honest; "we'll demo when it's ready" never converges.

### Common pitfalls

- **The status meeting.** The slot becomes verbal updates ("still working on the parser")
  with nothing running. Fix: no demo, no meeting — the checkpoint is a live run, however
  narrow (501-04).
- **The expert becomes the builder.** The group hands the hard parts over and turns into
  spectators. Fix: the expert diagnoses and points; the group types. If a piece genuinely
  needs the expert's hands, it's out of scope for a 501 Capstone.
- **The cross-department all-star team.** Six strong people from five desks who never find
  a common hour. Fix: one Department, one shared task.
- **Skipping the review or the measurement.** These are the two non-negotiable steps: skip
  the review and you build the wrong architecture; skip the measurement and you have no
  story at demo day and nothing for the program roll-up (501-05).

**For quants / For data scientists.** "One team" is the desk or pod that shares a task
*and* a data source. A [Quant](../../../CONTEXT.md) group tends to form around a shared
report or model-monitoring chore; a [Data Scientist](../../../CONTEXT.md) pod around a
shared feature-pipeline or data-QA chore. Either way the test is identical: do all 3–6
people touch this task and this data today? If not, it's a cross-team project, not a
working group.

## Lab

Convene the group: agree on members, confirm your Champion, and get an expert
committed for one review slot and demo day. Book the six calendar slots now —
the cadence is the mechanism; a group without dates on calendars is a mailing list.

**Stretch:** write a one-paragraph charter — members, the named owner, the Champion, the
committed expert, and the six dates — and paste it where the group can see it. Open the
[capstone issue template](../../../.github/ISSUE_TEMPLATE/capstone.md) and stub the
"task (before)" section now; you'll finish it at demo day.

## Knowledge check

1. What does the expert do — and what must the expert *not* do?
2. What two things does the program get out of a working group besides trained people?
3. Which two cadence steps are non-negotiable?
4. Your strongest candidate task is done on the fixed-income desk, but half your proposed
   group sits on the equities desk and has never touched it. What's wrong with the group,
   and how do you fix it?
5. Three weeks in, the weekly slot has become verbal status updates with nothing running
   live. Which rule of the format restores it, and why is that rule there?
