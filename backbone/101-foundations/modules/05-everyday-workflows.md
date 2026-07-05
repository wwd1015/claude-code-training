---
id: 101-05
title: "Everyday Workflows & Getting Unstuck"
duration: 40 min
objectives:
  - Apply the core daily patterns: explain, search, refactor, test, commit
  - Manage a session: context, /clear, interrupting, resuming
  - Know where to get help and what to try when results disappoint
  - Diagnose and recover from a disappointing result without starting over
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

## Worked example: search that follows meaning, and a recovery

You're chasing a number that looks wrong in a report. Grep for "sharpe" gives 40
hits across the repo; instead:

> Find every place we compute an annualized Sharpe ratio — including where the
> annualization factor is applied — and list them with file and line. Some may
> not use the word "sharpe".

It follows the *computation*, not the string: it finds the helper named
`risk_adjusted_return`, the notebook cell that multiplies by `sqrt(252)`, and the
one place someone hard-coded `sqrt(250)`. That last one is your bug — grep would
never have connected it.

Now suppose the first answer disappoints — it lists two spots and misses the
notebook. Don't start over; work the checklist. It didn't have the notebook in
context (you launched in `src/`, the notebook lives in `research/`). You relaunch
at the repo root, or `@`-attach the notebook, and re-ask. Nine times out of ten
"the model missed it" is really "the model couldn't see it."

### Best practices

- **Reach for semantic search before grep for anything conceptual.** "Where do we
  compute X" beats a string match because renames, helpers, and synonyms don't
  break it. Save grep for exact tokens.
- **One task per session; `/clear` between unrelated ones.** Context is finite and
  long sessions drift. Starting the plotting task in the same session that just
  finished a data-QA pass drags in irrelevant context. New task, fresh context.
- **`/compact` at a natural breakpoint in a long *single* task.** When one
  legitimate task runs long, `/compact` summarizes the history to reclaim room
  without losing the thread — different from `/clear`, which drops it entirely.
- **When results disappoint, diagnose before you retry.** Run the four-item
  checklist above; blind re-prompting repeats the same miss. Often the fix is
  context (right directory, right file), not a better sentence.
- **Ask the agent to diagnose itself.** "You missed the notebook — why, and what
  would have helped?" surfaces the gap (usually missing context) faster than you
  guessing.
- **Commit the good outputs as you go.** The daily patterns produce real artifacts
  (a `profile.py`, a `metrics.py`, a README). A checkpoint after each keeps a clean
  history and makes the next experiment reversible.

### Common pitfalls

- **Re-prompting a disappointing result without changing anything.** Same context,
  same miss. Change one variable — the directory, the file you attach, the
  acceptance check — then retry.
- **Never running `/clear`.** The session that's been open since Monday is carrying
  Monday's context into Thursday's task. Stale context is the quiet cause of "it's
  gotten worse today."
- **Confusing `/clear` and `/compact`.** `/clear` = new task, drop everything.
  `/compact` = same task, keep the thread but shrink it. Using `/clear` mid-task
  throws away context you still needed.
- **Blaming the model for a context problem.** "It can't find our Sharpe calc"
  usually means the calc lives in a directory the session can't see. Check what's
  reachable before concluding it's wrong.

### For quants / For data scientists

**Quants:** the highest-value daily pattern is usually *explain + search* on
inherited econometric code — tracing where an estimator or an annualization factor
really lives. **Data scientists:** it's usually *refactor + test* on pipeline code
at scale, where "write tests for the edge cases in this feature" pays off across
every downstream retrain.

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

**Stretch:** While you do it, keep a two-column log — where Claude saved you time,
and every point where you had to steer (interrupt, re-context, add a check). The
steer column is your personal best-practices list; bring both columns to office hours.

## Knowledge check

1. When should you `/clear` vs `--continue`?
2. Give the four-item checklist for disappointing results.
3. Which daily pattern will save you the most time this month — and what's the verification step for it?
4. What's the difference between `/clear` and `/compact`, and when do you use each?
5. A teammate says "Claude can't find where we compute exposure — it's useless for our repo." What two things do you check before agreeing?
