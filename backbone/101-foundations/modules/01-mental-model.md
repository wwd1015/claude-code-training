---
id: 101-01
title: "What Claude Code Is (and Isn't): the Agentic Mental Model"
duration: 20 min
objectives:
  - Explain the agentic loop (ask → plan → act → verify) in your own words
  - Distinguish Claude Code from chat assistants and autocomplete tools
  - Predict what Claude Code can see and do in your project
---

## A pair-researcher in your terminal

Claude Code is an **agent**: you describe an outcome, and it plans, reads your
files, runs commands, edits code, and checks its own work — in a loop — until
the outcome is met or it needs your input. That's the difference from a chat
window (which only talks) and from autocomplete (which only continues the line
you're typing).

The loop to internalize:

1. **Ask** — you state a goal ("profile this dataset and write a data dictionary").
2. **Plan** — it decides which files to read, what to run, what to change.
3. **Act** — it uses tools: read/edit files, run shell commands, search the repo.
4. **Verify** — it checks results (runs the tests, reruns the script, rereads output) and iterates.

You stay in control at the **act** step: tool use goes through a permission
model you configure (covered in module 4).

## What it can see and do

- Your **working directory** and anything reachable from it: code, notebooks,
  data files, git history.
- Your **shell**: it can run the same commands you can — `python`, `pytest`,
  `git`, `jupyter nbconvert`.
- Not your screen, other apps, or anything outside the directory/permissions
  you give it.

## What it's for (and not)

Good fits: understanding an unfamiliar repo, refactoring a messy notebook,
writing tests and docs, automating recurring analysis chores, git mechanics.
Poor fits: tasks you can't describe an acceptance check for, and judgment calls
that are yours to make — it's a collaborator, not an oracle.

**Reuse (official):** [Overview](https://code.claude.com/docs/en/overview) ·
[Quickstart](https://code.claude.com/docs/en/quickstart) ·
[Claude Code 101 course](https://anthropic.skilljar.com/claude-code-101)

## Lab

No install needed yet. Pick one recurring task from your own work (a report,
a data pull, a cleanup script). Write, in three sentences: the goal, what
"done" looks like, and what you'd need to check to trust the result. Keep it —
it becomes your working example for the rest of the curriculum.

## Knowledge check

1. Name the four steps of the agentic loop and where you retain control.
2. True/false: Claude Code can read files outside the directory you started it in without asking.
3. What makes a task a poor fit for delegation to an agent?
