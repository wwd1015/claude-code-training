---
id: 501-03
title: "Design Doc & Architecture Review"
duration: 50 min
objectives:
  - Write a one-page design doc for an agent system
  - Choose the right building-block layer (skill / hook / subagent / MCP / SDK)
  - Run a 30-minute architecture review with the expert against the checklist
  - Name failure modes as wrong-but-plausible outputs, each with a catch
---

## One page, before any code

The design doc is one page. If it doesn't fit, the scope is too big (back to
501-02). Its job is to force the four decisions that are expensive to change
later: the acceptance check, the architecture layer, the data touched, and the
failure behavior.

## Choosing the layer

Recap of CC 301/401 as a decision guide — pick the *lowest* layer that does the job:

| If the automation is… | Build a… | Covered in |
|---|---|---|
| a repeatable procedure you'd type as instructions | **skill** (`SKILL.md`) | CC 301 |
| a guardrail or side effect on every edit/run | **hook** | CC 301 |
| a tool/data source Claude should query | **MCP** connection | CC 301 |
| a task big enough to decompose or parallelize | **subagents / workflow** | CC 401 |
| something running outside interactive sessions (CI, schedule, app) | **headless / Agent SDK** | CC 401 |

Most flagship projects are a skill plus one of the others. If your design has
four layers, cut two.

## The design doc skeleton

Copy this into your project repo as `DESIGN.md`:

```markdown
# <project name> — design

**Task automated:** <the recurring task, who does it, hours/week it costs>
**Acceptance check:** <how you'll know a run is correct — concrete and executable>

## Architecture
<layer(s) chosen and why — one short paragraph, use the table above>
<sketch: input → steps → output>

## Data touched
<sources read, outputs written, and the permission model:
 what may the system do WITHOUT asking?>

## Failure modes
<top 3 ways it produces wrong-but-plausible output, and the check that catches each>

## Out of scope
<what you are deliberately NOT building>
```

## The 30-minute review

The expert reviews against this checklist — self-review it first:

- [ ] Acceptance check is executable, not aspirational ("matches last month's report", not "is accurate")
- [ ] Layer choice is the lowest that works; each extra layer earns its place
- [ ] Every data source is accessible today; permission boundaries are written down
- [ ] Failure modes name *wrong-but-plausible* outputs, not just crashes — and each has a catch
- [ ] Week-2 increment is identified and demoable
- [ ] Out-of-scope list exists (the moonshot lives there)

The review ends with one of: **proceed**, **proceed with changes** (noted in
the doc), or **rescope** (back to 501-02 — cheaper now than in week 4).

## Worked example: a filled DESIGN.md through review

The rates-desk group from 501-01 fills the skeleton for its Monday risk report:

```markdown
# Monday risk report — design

**Task automated:** the weekly desk risk summary — one quant pulls positions, runs
DV01-by-bucket, scenario-P&L, and limit-utilization cuts, and formats a summary for the
desk head. ~3 hrs every Monday + ~1 hr/wk chasing discrepancies.
**Acceptance check:** on last Monday's positions, the generated DV01-by-bucket and
scenario-P&L tables reconcile to the hand-built report to the basis point; narrative may differ.

## Architecture
Skill (`/risk-report`) that runs the standard cuts and drafts the summary, plus a
read-only MCP to the positions warehouse. Lowest layer that works: the cuts are a
repeatable procedure (skill); the only external reach is the warehouse (MCP). No
subagents — one book at a time is fast enough.
input: as-of date → MCP pulls positions → skill runs cuts → draft markdown in working dir

## Data touched
Reads: positions warehouse (read-only), last week's report (for the check).
Writes: a draft summary to the quant's working dir only.
Without asking: may read the warehouse and write the draft. May NOT email the desk head
or write anything back to the warehouse — a human sends the report.

## Failure modes
1. Stale snapshot (wrong as-of date) → assert snapshot timestamp == report date.
2. New instrument type silently dropped from the bucket map → reconcile total notional to
   the warehouse; a mismatch fails the run.
3. Scenario P&L computed on yesterday's curve → assert curve date == report date.

## Out of scope
Intraday risk, other desks, sending the report, historical backfill.
```

In the review the expert catches one gap: the acceptance check reconciles the DV01 and
scenario tables but says nothing about the *limit-utilization* cut the task mentions.
Outcome: **proceed with changes** — limit-utilization moves to a later sprint and onto the
out-of-scope list for the week-2 increment, which is now pinned as *one book,
DV01-by-bucket, reconciled to last Monday*. Fifteen minutes of review, one rebuild
avoided.

## Reviewing well

### Best practices

- **The doc exists to catch bad architecture before it's built — not for ceremony.** Its
  payoff is a rescope in week 1 that saves a rebuild in week 4. If this doc could never
  send anyone back to 501-02, it isn't doing its job.
- **Pick the lowest layer that works and make each extra layer earn its place.** A skill
  plus one reach (a hook, or a read-only MCP) covers most Capstones. Four layers is a
  smell; cut two at review.
- **Write the acceptance check and failure modes from the humans who do the task.** Claude
  drafts the doc well, but only the person who runs the task weekly knows which
  wrong-but-plausible outputs actually occur — those are the failure modes worth catching.
- **Name failure modes as wrong-but-plausible outputs, not crashes.** A crash is loud and
  safe; a report that reconciles by luck after an instrument was silently dropped is the
  dangerous one. Each failure mode needs a mechanical catch (assert, reconcile, count).
- **Write the permission boundary as one sentence.** State what the system may do without
  asking and what always needs a human. "Reads warehouse, writes a draft, never sends" is
  what stops a research automation from mailing a wrong number to the desk head.
- **Keep it to one page.** Overflow is a scope signal, not a formatting problem — if it
  won't fit, go back to 501-02.

### Common pitfalls

- **The doc as theater.** Written once to satisfy the process, never reopened. Fix: the
  doc is what the expert reviewed and what sprints update (501-04) — when a decision
  changes, it changes *here*, not only in the log.
- **Over-engineering the architecture.** Reaching for subagents *and* an MCP *and* a hook
  when a skill would do. Fix: lowest layer that works; each layer earns its place.
- **Aspirational acceptance checks.** "The report is accurate" isn't executable. Fix: name
  the artifact you reconcile against and the tolerance ("matches last Monday to the basis
  point").
- **Failure modes that only list crashes.** "It might error out" is the safe case. Fix:
  for each output, ask "how could this be wrong but look right?" and write the catch.
- **An implicit permission model.** Fix: one line on what runs without asking; when in
  doubt, a research automation should draft, not send.

**For quants / For data scientists.** A [Quant](../../../CONTEXT.md)'s failure modes are
usually reconciliation and staleness — wrong as-of date, yesterday's curve, an instrument
outside the bucket map — and the catches are exact numeric reconciliations. A
[Data Scientist](../../../CONTEXT.md)'s are distribution and schema — silent drift, a
renamed column read as null, target leakage in a feature — and the catches are statistical
(row counts, null rates, distribution deltas against a known-good day). Same one-page doc;
the "wrong-but-plausible" list is discipline-specific.

## Lab

Write the design doc as a group — Claude Code is a good drafting partner
("draft a DESIGN.md for automating <task> following this skeleton"), but the
acceptance check and failure modes must come from the humans who do the task.
Book and run the expert review; record the outcome in the doc.

**Stretch:** self-review against the six-point checklist and fix what you can *before* the
expert sees it — a review that spends its 30 minutes on things you could have caught is
wasted. After the review, stamp the outcome (proceed / proceed-with-changes / rescope) and
the date in the doc header, so 501-04's checkpoints can tell when a later decision
contradicts what was reviewed.

## Knowledge check

1. Why pick the lowest layer that works?
2. What makes an acceptance check "executable"? Give an example from your project.
3. What are the three possible outcomes of the review?
4. A group's failure-modes section reads "the script might crash or time out." What's
   missing, and rewrite one entry as a wrong-but-plausible output with a catch.
5. The design doc says the automation "emails the desk head the finished report." What
   permission question should the review raise, and what's the safer default?
