---
id: 401-01
title: "Subagents: Delegation & Decomposition"
duration: 45 min
objectives:
  - Explain what a subagent is and what it does (and doesn't) share with your session
  - Define a reusable subagent in .claude/agents/ with a scoped prompt and toolset
  - Decide when to delegate to a subagent vs. do the work inline
  - Brief a subagent with an explicit report contract so its output is trustworthy without re-checking its work
---

## What a subagent is

A **subagent** is a separate Claude instance your main session launches to do a
scoped task and report back. It gets its own context window, its own system
prompt, and (optionally) its own restricted toolset. It does *not* see your
conversation — only the task prompt it's given — and you see only its final
report, not its tool-by-tool work.

That isolation is the point. Two consequences to internalize:

- **Context isolation** — a subagent can read fifty files without polluting
  your session's context. You keep the conclusion, not the file dumps.
- **Blind spots** — it doesn't know what you and Claude discussed. Everything
  it needs must be in its task prompt or on disk.

## Defining one

Ad-hoc delegation happens automatically ("search the codebase for…" often
spawns one). For repeatable roles, define a named subagent in
`.claude/agents/<name>.md`: front-matter for name, description (when the main
agent should pick it), and allowed tools; body is its system prompt. Project
agents live in the repo and are shared with the team; personal ones live in
`~/.claude/agents/`.

A worked example lives in this repo:
[demo 03 — anomaly-triage agent](../../../demos/03-anomaly-triage-agent.md) —
a read-only subagent that investigates data anomalies and returns a structured
triage report.

## Delegate or do it inline?

| Delegate to subagents | Keep inline |
|---|---|
| independent pieces that can run in parallel | steps that each depend on the last |
| bulk reading/search where you need the conclusion | judgment calls needing conversation context |
| a role with different rules (read-only reviewer) | quick single-file edits |
| work that would flood your context window | anything faster to do than to explain |

The cost of delegation is the briefing: a subagent is only as good as its task
prompt. If writing the prompt takes longer than the task, do it inline.

## Worked example: fan-out anomaly triage over 200 series

You have `data/series/` with ~200 daily series and need the handful that broke
overnight. Done in one session, this means reading 200 files into one context
window — the answer drowns in the raw material, and every follow-up turn
re-reads the pile. Delegate instead:

1. Ask your session to write `check_one.py` (a path in → verdict + score out) —
   a deterministic detector you and the desk already trust (z-score, rolling
   IQR, or your team's standard).
2. Brief the orchestrator: *"Fan out one subagent per file in `data/series/`.
   Each runs `check_one.py` on its file and returns exactly one line:
   `series_id | verdict | score | reason | location`. Return `NONE` if the
   series is clean."*
3. The subagents run in parallel. Each reads its own file, keeps its own scratch
   work in its own context, and hands back a single line. Your session sees ~200
   one-line verdicts — not 200 files.
4. The orchestrator ranks the flagged series and drops the rest into the report.

Isolation is doing three jobs here at once: **parallelism** (wall-clock ≈ the
slowest checker, not the sum), **context hygiene** (the file dumps stay in the
workers and never reach your window), and a **uniform contract** (every worker
answers in the same shape, so merging is a sort, not a negotiation). This is the
[demo 03](../../../demos/03-anomaly-triage-agent.md) pattern and the
`/triage-data` skill — the same decomposition you'll reuse for many tickers,
many configs, many backtests.

### Best practices

- **One subagent, one job.** A worker with a single, stateable objective returns
  a crisp result; a worker asked to "profile the data and also fix what's wrong
  and also write it up" returns mush. Split multi-part work into multiple
  workers (or a pipeline, module 2), not one overloaded prompt.
- **Hand it an explicit report contract.** State the exact shape you want back
  (a table, a `verdict | score | reason` line, "≤5 bullets"). The contract is
  what lets you trust the output without re-doing the work — and what makes N
  results mergeable.
- **Return conclusions, not transcripts.** The whole point is that fifty files
  become one summary. If a worker hands back its tool-by-tool log, tighten the
  prompt: "report only the finding and its location, not your steps."
- **Restrict the toolset to the job.** A reviewer gets read-only tools; a
  profiler gets read + bash but not Write/Edit. Set `tools:` in the agent's
  front-matter — a narrow toolset is a guardrail *and* a hint that steers the
  worker toward the intended work.
- **Brief it like a colleague who just walked in.** It has none of your
  conversation. Name the files, the definition of done, and any assumption you'd
  otherwise leave implicit. Everything it needs is in the prompt or on disk —
  nowhere else.
- **Delegate for isolation, not just for offloading.** Even a task you *could*
  do inline is worth a subagent when its raw material would pollute your context
  for the rest of the session (a large log, a sprawling schema dump).

### Common pitfalls

- **"Fix the bug we discussed" — but the subagent never saw the discussion.** It
  guesses, and returns something unrelated. Fix: restate the actual change in
  the task prompt, or point it at the file/commit where the context lives. Blind
  spots are structural, not laziness.
- **The worker returns three paragraphs of reasoning per item and your context
  fills up anyway.** Fix: demand a fixed, terse output shape in the prompt
  ("one line per series, `NONE` if clean") — the contract is the context
  control.
- **Over-delegation: spinning up a subagent for a two-line edit.** The briefing
  costs more than the task, and you wait on a round-trip. Fix: if you can do it
  faster than you can explain it, do it inline.
- **Giving a read-only reviewer write access "just in case."** Now a review can
  silently mutate your tree. Fix: scope `tools:` to exactly what the role needs;
  a reviewer that *can't* edit is a reviewer you can run unwatched.

**For quants / For data scientists:** the fan-out is the same; the unit of
independence differs. A **Quant** fans out over many tickers or many model
specifications — one worker per cointegration test or regression diagnostic. A
**Data Scientist** fans out over shards, feature groups, or experiment logs —
one worker per slice. Pick the axis along which items don't need each other's
output; that axis is your map.

**Reuse (official):** [Subagents docs](https://code.claude.com/docs/en/sub-agents) ·
[Introduction to Subagents course](https://anthropic.skilljar.com/introduction-to-subagents)

## Lab

In a repo you know: (1) ask Claude to use a subagent to audit every data-loading
path and report file names + formats + assumptions — watch your context stay
clean; (2) define `.claude/agents/reviewer.md`, a read-only reviewer whose
prompt forbids edits and demands findings as a numbered list; (3) invoke it on
your latest change. Keep the reviewer — you'll wire it into a workflow next
module.

**Stretch:** check the reviewer into the repo as a project agent, and give its
front-matter a `tools:` list that excludes `Write` and `Edit`. Then ask it to
"fix" something and confirm the session refuses on its behalf — you've turned a
convention ("please don't edit") into a guardrail (it *can't*). Write a
one-sentence report contract at the top of its prompt and re-run; note how much
less you have to re-read the second time.

## Knowledge check

1. What does a subagent share with your session, and what is it blind to?
2. Name two signals that a task should be delegated rather than done inline.
3. Why might you restrict a subagent's tools, and where is that configured?
4. **Scenario:** you tell a subagent "apply the fix we agreed on" and it returns
   an unrelated change. What went wrong, and how do you re-brief it in one line?
5. **Scenario:** your fan-out of 200 checkers each returns three paragraphs of
   reasoning, and your context fills up. What single instruction in the worker
   prompt would have kept it clean?
