---
id: 401-01
title: "Subagents: Delegation & Decomposition"
duration: 35 min
objectives:
  - Explain what a subagent is and what it does (and doesn't) share with your session
  - Define a reusable subagent in .claude/agents/ with a scoped prompt and toolset
  - Decide when to delegate to a subagent vs. do the work inline
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

**Reuse (official):** [Subagents docs](https://code.claude.com/docs/en/sub-agents) ·
[Introduction to Subagents course](https://anthropic.skilljar.com/introduction-to-subagents)

## Lab

In a repo you know: (1) ask Claude to use a subagent to audit every data-loading
path and report file names + formats + assumptions — watch your context stay
clean; (2) define `.claude/agents/reviewer.md`, a read-only reviewer whose
prompt forbids edits and demands findings as a numbered list; (3) invoke it on
your latest change. Keep the reviewer — you'll wire it into a workflow next
module.

## Knowledge check

1. What does a subagent share with your session, and what is it blind to?
2. Name two signals that a task should be delegated rather than done inline.
3. Why might you restrict a subagent's tools, and where is that configured?
