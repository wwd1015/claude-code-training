---
id: 301-01
title: "Skill Creation I: Anatomy of a Skill"
duration: 40 min
objectives:
  - Explain what a skill is and when Claude Code loads one
  - Read and write the SKILL.md structure — frontmatter plus instructions
  - Write a skill description the matcher fires on — trigger phrases, not marketing
  - Decide when a task deserves a skill versus a one-off prompt
---

## What a skill is

A **skill** is a folder containing a `SKILL.md` file: reusable instructions
that teach Claude Code a workflow you'd otherwise re-explain every session.
Skills live at `.claude/skills/<name>/SKILL.md` in a project (shared with the
repo) or `~/.claude/skills/<name>/SKILL.md` for just you. When your request
matches a skill's description, Claude loads the instructions and follows them.

Think of it as the difference between telling a new teammate how to run the
weekly report every single week, and writing the runbook once.

## The anatomy

```markdown
---
name: data-dictionary
description: >
  Profile a dataset and produce a standardized data dictionary.
  Use when asked to "profile this data", "document this dataset",
  or "make a data dictionary".
---

# data-dictionary

## Steps
1. Load the data; infer types, ranges, null rates per column.
2. Flag columns needing human description; never invent meanings.
3. Write dictionary.md using the table format below.
...
```

Two parts matter most:

- **Frontmatter drives discovery.** `name` and `description` are all Claude
  sees before deciding to load the skill — the description must say *what it
  does* and *when to use it*, including the phrases people actually say.
- **The body is loaded only when triggered.** This is *progressive
  disclosure*: a hundred installed skills cost almost nothing until one is
  needed. Detail belongs in the body (or in extra files alongside SKILL.md),
  never crammed into the description.

## Skill, or just a prompt?

Make it a skill when: you've typed the same instructions twice; the workflow
has steps or rules that must not drift; teammates should get identical
behavior. Keep it a prompt when it's genuinely one-off. Slash commands (CC
201) are lightweight text shortcuts you invoke by name; skills carry full
workflows and can be picked up by Claude automatically when relevant.

## Worked example: the description is a trigger, not a tagline

The description is the single highest-leverage line in the file, because it's
the *only* thing the matcher reads when deciding whether to load your skill.
Write it for the matcher, not for a human browsing a catalog. Watch the same
skill fail and then succeed on wording alone.

A first draft that reads like marketing copy:

```yaml
description: A powerful helper for regression work.
```

Nothing here tells Claude *when* to reach for it. Ask "check whether my rates
model is sound" and the skill never loads — "powerful helper" doesn't match
anything you'd actually say. Now the version that names the job and the phrases
a Quant really types (this is the real opening of this repo's
[`skills/regression-diagnostics/SKILL.md`](../../../skills/regression-diagnostics/SKILL.md)):

```yaml
description: >
  Run a standard diagnostic battery on a linear/OLS regression — coefficients
  with confidence intervals, R²/adjusted-R², multicollinearity (VIF),
  heteroskedasticity (Breusch-Pagan), residual normality, autocorrelation, and
  a stationarity check. Use when the user says "regression diagnostics", "check
  this model", "is my regression sound", "VIF/heteroskedasticity/stationarity",
  or fits an econometric model and wants it validated.
```

Two things changed: it says *what it produces* in concrete nouns, and it lists
the *trigger phrases* verbatim. Now "is my regression sound?" lands on the
skill without anyone typing its name. The body underneath — the actual battery
of tests — never loaded during matching; it only arrives once the description
wins.

### Best practices

- **Write the description for the matcher.** Lead with the task in plain nouns,
  then a "Use when the user says …" clause listing the phrases people actually
  type. The matcher only ever sees `name` + `description`; if your phrasing
  isn't in there, the skill is invisible no matter how good the body is.
- **Keep SKILL.md lean; push heavy material to linked files.** Progressive
  disclosure means the body loads only on a match, and extra files load only
  when the body points at them. A long lookup table or a policy doc belongs in
  a sibling file the skill references, not inline — see CC 301 module 2.
- **Name the skill after the job, not the tool.** `regression-diagnostics`
  and `eda` describe what the Learner wants done; `run-statsmodels` describes
  your implementation and ages badly.
- **One skill, one workflow.** A skill that "profiles data *and* trains a model
  *and* writes the deck" matches ambiguously and drifts. Split it; small skills
  compose.
- **Prefer project scope for anything a teammate will reuse.** A skill in
  `.claude/skills/` ships with the repo (CC 301 module 6); `~/.claude/skills/`
  is for personal tooling only you need.

### Common pitfalls

- **The description sells instead of triggering.** "A best-in-class data tool"
  matches nothing. *Fix:* rewrite it as "Use when asked to profile a dataset,
  document columns, or make a data dictionary" — the words a Learner says.
- **Detail crammed into the description to make the skill "smarter."** It
  bloats every match decision and still doesn't run until loaded. *Fix:* the
  description says *when*; the body says *how*.
- **Building a skill for a genuinely one-off task.** If you'll run it once,
  a prompt is faster. *Fix:* wait for the second time you type the same
  instructions — that's the signal it should be a skill.

**For quants:** your first skill is often a model-validation battery like
`/regression-diagnostics` — deterministic tests (VIF, Breusch-Pagan, ADF) whose
steps must never drift. **For data scientists:** it's often a profiling or
triage pass over a large table like `/eda` — the value is a consistent,
repeatable first look, not a one-off notebook cell.

**Reuse (official):** [Skills docs](https://code.claude.com/docs/en/skills) ·
[Intro to Agent Skills course](https://anthropic.skilljar.com/introduction-to-agent-skills) ·
[anthropics/skills examples](https://github.com/anthropics/skills)

## Lab

Read this repo's [`skills/eda/SKILL.md`](../../../skills/eda/SKILL.md).
Identify: the trigger phrases in its description, the steps that would drift
without it, and one thing you'd change for your own data. Then stub your own:
pick the recurring task from CC 101 module 1 and write just the frontmatter —
name plus a description with your real trigger phrases.

**Stretch goal:** take the frontmatter you just wrote and run the trigger test
by hand — say your task three different ways you'd naturally phrase it (none
using the skill's name) and check each phrasing appears, in spirit, in your
description. Every phrasing that doesn't match is a line you add to the "Use
when …" clause. This is the same trigger test you'll automate in module 2.

## Knowledge check

1. What are the only two things Claude sees before deciding to load a skill?
2. Why is "progressive disclosure" the reason skill bodies can be long?
3. A teammate keeps getting different report formats from the same prompt — skill or slash command, and why?
4. Rewrite this description so the matcher can fire on it: "A comprehensive
   toolkit for time-series analysis." What's missing, and what would you add?
5. **Scenario:** You wrote a `/backtest-report` skill, but when you ask
   "summarize how the strategy did last quarter" it never loads — yet typing
   `/backtest-report` works fine. Which part of the file is at fault, and what's
   the one-line fix?
