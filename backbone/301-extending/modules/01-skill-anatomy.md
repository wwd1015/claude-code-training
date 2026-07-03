---
id: 301-01
title: "Skill Creation I: Anatomy of a Skill"
duration: 30 min
objectives:
  - Explain what a skill is and when Claude Code loads one
  - Read and write the SKILL.md structure — frontmatter plus instructions
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

**Reuse (official):** [Skills docs](https://code.claude.com/docs/en/skills) ·
[Intro to Agent Skills course](https://anthropic.skilljar.com/introduction-to-agent-skills) ·
[anthropics/skills examples](https://github.com/anthropics/skills)

## Lab

Read this repo's [`skills/eda/SKILL.md`](../../../skills/eda/SKILL.md).
Identify: the trigger phrases in its description, the steps that would drift
without it, and one thing you'd change for your own data. Then stub your own:
pick the recurring task from CC 101 module 1 and write just the frontmatter —
name plus a description with your real trigger phrases.

## Knowledge check

1. What are the only two things Claude sees before deciding to load a skill?
2. Why is "progressive disclosure" the reason skill bodies can be long?
3. A teammate keeps getting different report formats from the same prompt — skill or slash command, and why?
