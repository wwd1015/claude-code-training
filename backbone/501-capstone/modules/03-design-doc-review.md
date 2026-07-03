---
id: 501-03
title: "Design Doc & Architecture Review"
duration: 40 min
objectives:
  - Write a one-page design doc for an agent system
  - Choose the right building-block layer (skill / hook / subagent / MCP / SDK)
  - Run a 30-minute architecture review with the expert against the checklist
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

## Lab

Write the design doc as a group — Claude Code is a good drafting partner
("draft a DESIGN.md for automating <task> following this skeleton"), but the
acceptance check and failure modes must come from the humans who do the task.
Book and run the expert review; record the outcome in the doc.

## Knowledge check

1. Why pick the lowest layer that works?
2. What makes an acceptance check "executable"? Give an example from your project.
3. What are the three possible outcomes of the review?
