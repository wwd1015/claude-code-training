---
id: 101-01
title: "What Claude Code Is (and Isn't): the Agentic Mental Model"
duration: 25 min
objectives:
  - Explain the agentic loop (ask → plan → act → verify) in your own words
  - Distinguish Claude Code from chat assistants and autocomplete tools
  - Predict what Claude Code can see and do in your project
  - Recognize which of your tasks are strong fits for an agent — and which aren't
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

## The loop on a real task

Watch what actually happens when you type one sentence. You open Claude Code in
a research repo and ask:

> Fit an OLS of `daily_return` on the three factor columns in `factors.parquet`,
> then check the residuals for heteroskedasticity and tell me whether the
> standard errors are trustworthy.

- **Ask** — that sentence is the goal. Notice it already carries a check ("tell
  me whether the standard errors are trustworthy"), which is what lets the loop
  close.
- **Plan** — it reads `factors.parquet` to learn the column names and dtypes,
  sees there's no fitting script yet, and decides to write a short one rather
  than guess.
- **Act** — it writes and runs the regression (statsmodels), prints the summary,
  then runs a Breusch–Pagan test on the residuals.
- **Verify** — the p-value comes back small, so it doesn't stop at "here's your
  R²"; it reports the heteroskedasticity, re-runs with robust (HC3) standard
  errors, and shows you both side by side.

You never said "Breusch–Pagan" or "HC3". A chat window would have handed you code
to paste and run yourself; autocomplete would have finished a line. The agent ran
the analysis, read the result, and adjusted — that is the loop.

How you verify *it*: the numbers live in your files now, so re-run the script
yourself, or ask "show me the exact commands you ran." Never accept a statistic
just because it was phrased confidently.

### Best practices

- **State the outcome, not the keystrokes.** "Profile this dataset and flag
  data-quality issues" gives the agent room to plan; "open pandas, call
  `.describe()`, then…" turns it back into autocomplete. This is the official
  *explore → plan → act → verify* pattern — you own the outcome, it owns the steps.
- **Put the acceptance check in the ask.** The loop can only close if there's
  something to check against ("…and confirm the row count matches the source
  table"). No check, no self-correction — the mechanics are in module 3.
- **Match the tool to the task.** Reach for Claude Code when the work touches
  files, the shell, or a repo. For a pure "explain this concept" question with
  no code, a chat window is lighter.
- **Treat every result as a draft you own.** It infers, runs, and reports; you're
  the domain expert who decides whether the inference is right. The agent is a
  collaborator, not an oracle.

### Common pitfalls

- **Expecting it to read your mind about "the data."** It only knows what's
  reachable from the directory you launched in (next module). Say "the returns
  file" when three exist and it will guess. Name the path, or use `@` to point
  at it.
- **Treating a confident answer as a verified one.** Fluent prose is not evidence.
  If it says "the join is clean," ask it to show the null count after the join.
- **Handing it a judgment call.** "Should we trade this signal?" is yours to make.
  "Backtest this signal and show me the drawdown and turnover" is the agent's.
  Keep the decision; delegate the legwork.

### For quants / For data scientists

**Quants:** the win is usually breadth of mechanics — econometric boilerplate
(lag construction, HAC standard errors, rolling regressions) it scaffolds in
seconds while you keep the modeling judgment. **Data scientists:** the win is
usually navigating scale — feature pipelines, large tables, framework glue —
where "find every place we compute this feature" across a big codebase beats grep.

**Reuse (official):** [Overview](https://code.claude.com/docs/en/overview) ·
[Quickstart](https://code.claude.com/docs/en/quickstart) ·
[Claude Code 101 course](https://anthropic.skilljar.com/claude-code-101)

## Lab

No install needed yet. Pick one recurring task from your own work (a report,
a data pull, a cleanup script). Write, in three sentences: the goal, what
"done" looks like, and what you'd need to check to trust the result. Keep it —
it becomes your working example for the rest of the curriculum.

**Stretch:** For that same task, write the one sentence you would *not* delegate —
the judgment call inside it that stays yours. Naming the boundary now saves you
from over-trusting later.

## Knowledge check

1. Name the four steps of the agentic loop and where you retain control.
2. True/false: Claude Code can read files outside the directory you started it in without asking.
3. What makes a task a poor fit for delegation to an agent?
4. A teammate says "Claude Code is just autocomplete for a whole file." What's the one distinction you'd correct them on?
5. You ask for a Sharpe ratio and get a confident number back. What do you do before putting it in a deck?
