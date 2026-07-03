---
id: 101-05
title: "Everyday Workflows & Getting Unstuck"
duration: 30 min
objectives:
  - Apply the core daily patterns: explain, search, refactor, test, commit
  - Manage a session: context, /clear, interrupting, resuming
  - Know where to get help and what to try when results disappoint
---

## The daily patterns

Five workflows cover most days; all are elaborations of module 3's cycle:

1. **Explain** — "walk me through how X works" on any unfamiliar code or notebook.
2. **Search** — "find every place we compute Y" beats grep because it follows meaning, not strings.
3. **Refactor** — goal + constraints + verification; plan mode for big ones.
4. **Test & document** — "write tests for the edge cases in Z", "add a README for this folder".
5. **Git chores** — "commit this with a sensible message", "what changed since yesterday?", "make a branch for this experiment".

## Session hygiene

- A session's **context** fills up as it reads files and talks. Long sessions
  drift; `/clear` starts fresh (new task = new context is a good default).
- One task per session beats one mega-session; resume with `--continue` when
  it really is the same task.
- Interrupt early (`Esc`) when you see it going sideways — steering beats redoing.

## When results disappoint

Work the checklist before blaming the model:

1. Did you give a verification step? (No check → no self-correction.)
2. Was the goal one sentence or one essay? Split compound asks.
3. Did it have the context — right directory, right files mentioned?
4. Ask *it* to diagnose: "you missed X — why, and what would have helped?"

## Where to get help

`/help` in a session · [docs](https://code.claude.com/docs/en/overview) ·
[Common workflows](https://code.claude.com/docs/en/common-workflows) ·
your department's champion · office hours.
<!-- verify: add internal support channel link via intake -->

## Lab (course capstone)

Take the recurring task you wrote down in module 1 and do it end-to-end with
Claude Code: explore → plan-mode proposal → execute with a verification step →
commit the result. Record minutes saved vs. by hand; bring the number (and the
pain points) to your next cohort session or office hours.

## Knowledge check

1. When should you `/clear` vs `--continue`?
2. Give the four-item checklist for disappointing results.
3. Which daily pattern will save you the most time this month — and what's the verification step for it?
