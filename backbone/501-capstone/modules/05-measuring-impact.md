---
id: 501-05
title: "Measuring Impact & Promotion to Flagship"
duration: 34 min
objectives:
  - Measure time saved honestly, before/after, on the real task
  - Contribute the project to the shared demo library
  - Run a demo day that recruits the next working group
  - Set and hand off a T+30 active-use check
---

## Measure honestly

The number that matters: **hours per week saved on the real task**, measured
before/after by the person who owns it — the same discipline as the
[metrics template](../../../docs/metrics-template.md). Rules:

- **Before** is what the task actually cost (the owner knows; write it down
  before the after-measurement biases it).
- **After** includes the new costs: kicking off runs, reviewing output,
  fixing the occasional miss. Net, not gross.
- Rough is fine; inflated is fatal — one audited, deflated claim costs the
  program more credibility than ten modest true ones earn.
- Also record: does the acceptance check still pass a month later? (That's the
  T+30 active-use check the program tracks.)

## Write it up and contribute

Promote the project to the **contributed demo library** — the mechanism that
compounds capstones across departments ([CONTRIBUTING](../../../CONTRIBUTING.md)):

1. Short writeup in the demo format: objective · setup · live script · time saved.
2. Front-matter tags (`discipline`, `department`, `use_case`, `kind: contributed`)
   so others can judge relevance.
3. No internal data or secrets committed — sanitize or seed.
4. Champion sponsors the PR (their four-point check); central does a light merge review.

Contributed demos are **author-owned**: rough and niche is fine, and if it
goes stale it's archived, not fixed. Your `DESIGN.md` + `LOG.md` from 501-03/04
are most of the writeup already.

## Demo day: the recruiting engine

Demo day is how flagship projects recruit the next groups. The framing that
works ([capstone-ideas.md](../../../docs/capstone-ideas.md)):

1. The task **before** — how long, how manual (30 seconds of pain everyone recognizes).
2. What you built — 10 seconds on the building block, not an architecture lecture.
3. A **live run**.
4. The honest time-saved number and the T+30 plan.

Invite adjacent teams and their Champions. The question you want from the
audience is "could this work for our version of that task?" — that question is
the next working group forming.

## Worked example: measuring and promoting the risk report

The rates-desk group closes out the Monday risk report from 501-01/03.

- **Before** (written down at selection, so it can't drift): 3 hrs every Monday building
  the report + ~1 hr/wk chasing discrepancies = **~4 hrs/wk**.
- **After** (measured on a real Monday a month in): ~15 min kicking off and reviewing the
  draft + ~10 min the odd week fixing a flagged reconciliation ≈ **~35 min/wk**.
- **Net:** ~3.25 hrs/wk saved, reported as **3 hrs/wk** — rounded down on purpose.
- **T+30:** the acceptance check still passes on this Monday's positions and the owner is
  still using it. Active at T+30 = yes.

Then they promote it. The [Capstone](../../../CONTEXT.md) becomes a
[Contributed demo](../../../CONTEXT.md): `DESIGN.md` + `LOG.md` are most of the writeup;
they add the demo-format sections and front-matter tags:

```yaml
discipline: quant
department: <!-- verify -->   # the actual desk/department code is org-specific
use_case: risk-reporting
kind: contributed
```

They seed the positions (no real book committed), the Champion sponsors the PR with the
four-point check, and central does a light merge review. Now `/risk-report` is where the
*next* rates group starts — that is how the [Demo library](../../../demos/INDEX.md)
compounds. At demo day: 30 seconds of Monday pain every desk recognizes, 10 seconds ("it's
a skill plus a read-only warehouse MCP"), a **live run**, then "was ~4 hrs/wk, now ~35 min,
net 3 hrs — still passing at T+30." An adjacent desk asks whether it could do their weekly
P&L attribution. That question is the next working group forming.

## Measuring and promoting well

### Best practices

- **Measure against a written-down before, not a guess.** The owner records what the task
  cost *before* the after-measurement biases it. A remembered "it took forever" is not a
  baseline — see the [metrics template](../../../docs/metrics-template.md).
- **Count net, not gross.** "After" includes the new costs — kicking off runs, reviewing
  output, fixing the occasional miss. The honest number is time saved minus that overhead.
- **Deflate rather than inflate.** One audited, inflated claim costs the program more
  credibility than ten modest true ones earn. Round down; when unsure, claim the smaller
  number.
- **Record the T+30 check.** Does the acceptance check still pass a month later, and is the
  owner still using it? That yes/no is the program's truest signal (the active-use rate),
  worth more than any satisfaction score.
- **Promote every finished Capstone to a Contributed demo.** A Capstone that stays in the
  group's repo doesn't compound; promoted, it's where the next group starts. This is the
  mechanism that turns Learners into contributors and grows the library.
- **Frame demo day to recruit, not to lecture.** Before (30 sec of shared pain), built
  (10 sec on the building block), a live run, the honest number and T+30 plan. The live
  run and the honest number convince skeptics; an architecture walkthrough convinces no one.

### Common pitfalls

- **Measuring vibes instead of hours.** "It feels way faster." Fix: a before number and an
  after number on the real task, from the owner.
- **The inflated claim.** Reporting gross time, or the best-case week. Fix: net, a typical
  week, rounded down.
- **The Capstone that never becomes a Contributed demo.** It works, saves hours, and dies
  in a private repo. Fix: the promotion PR is part of *this* course (the lab below);
  `DESIGN.md` + `LOG.md` are most of the writeup already.
- **Committing internal data or secrets.** Fix: sanitize or seed before the PR; the
  Champion's four-point check ([CONTRIBUTING](../../../CONTRIBUTING.md)) is there to catch it.
- **Demo day as an architecture lecture.** Ten minutes on subagents, no live run. Fix: 10
  seconds on the building block, then run the thing.
- **No T+30 plan.** A number at demo day with no follow-up. Fix: name the T+30 date and who
  checks it, and report both to your Champion for the roll-up.

**For quants / For data scientists.** A [Quant](../../../CONTEXT.md)'s before is often
exact — "the report ran 8:00 to 11:00 every Monday" — and the after reconciles cleanly. A
[Data Scientist](../../../CONTEXT.md)'s before is usually diffuse — "about an hour every
morning, plus fire drills" — so log a week of it *before* you start automating, or the
after-comparison has nothing solid to sit against. Same rule (a written-down before); the
DS baseline usually needs that week of logging first.

## Lab (course capstone)

Close out: run the before/after measurement with the task owner; submit the
contribution PR with your Champion; hold demo day with at least one adjacent
team in the room. Report the time-saved number and T+30 date to your Champion
for the program roll-up.

**Stretch:** add the front-matter tags and a one-line "how to run it" so a teammate could
try it tomorrow, and pre-fill the [demo-day scoring sheet](../../../docs/sessions/capstone-demo-day.md)
(real / works / reusable / saved) for your own project as a dry run before you present.
Book the T+30 check-in as a calendar event now, owned by the task owner — an unbooked T+30
is a T+30 that doesn't happen.

## Knowledge check

1. What must "after" include for the time-saved number to be honest?
2. Who owns a contributed demo, and what happens when it goes stale?
3. What are the four parts of the demo-day framing, and which one convinces skeptics?
4. A group reports "saved about 10 hours a week" but has no before number and measured
   only its best week. What's wrong, and what's the honest way to report it?
5. Why is promoting the Capstone to a Contributed demo part of the course, not an optional
   extra?
