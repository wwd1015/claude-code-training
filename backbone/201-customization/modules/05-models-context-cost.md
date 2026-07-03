---
id: 201-05
title: "Models, Context & Cost"
duration: 25 min
objectives:
  - Match model choice to task difficulty
  - Manage the context window: /compact, /clear, and session scope
  - Build cost-awareness habits without becoming a token accountant
---

## Choosing a model

Claude Code can run different Claude models; switch with `/model` or set a
default in settings. The working heuristic:

- **Most capable model** — architecture, tricky debugging, multi-step
  refactors, anything you'd give your strongest colleague.
- **Faster/cheaper model** — mechanical edits, formatting, boilerplate,
  first-draft docstrings.

When unsure, start capable and downgrade the repetitive parts once the
pattern is established — the reverse (cheap model digs a hole, capable model
excavates it) costs more. <!-- verify: current model lineup and default before teaching -->

## Context is a budget

Everything the session reads and says occupies the **context window**. As it
fills, sessions get slower, costlier, and vaguer about early details. Three
controls, in order of preference:

1. **Scope sessions tightly** (CC 101 habit): one task, one session.
2. **`/clear`** when switching tasks — a fresh start beats a fog of leftovers.
3. **`/compact`** mid-task when context is large but you need continuity — it
   summarizes the conversation so far and continues on the summary.

The CLAUDE.md connection from module 1: standing instructions in CLAUDE.md
cost a few lines once per session; re-explaining them costs paragraphs every
session. Configuration *is* context management.

## Cost habits

You don't need per-token bookkeeping; you need three habits: know roughly
what a normal session costs for your usage (`/cost` shows the session's
spend), notice outliers and ask why (usually a runaway loop or a giant file
read), and prefer scoped sessions — the same habit that improves quality
cuts cost. <!-- verify: /cost availability under your org's billing/subscription setup -->

**Reuse (official):** [Best practices](https://code.claude.com/docs/en/best-practices) ·
[How Claude Code works](https://code.claude.com/docs/en/how-claude-code-works)

## Lab (course capstone)

Put the whole course together on your primary repo: (1) write or finish its
`CLAUDE.md` (module 1 draft, now battle-tested); (2) commit project settings
with your allowlist and one env var; (3) ship one custom slash command for a
recurring task. Fresh session, run the command — the goal is a session that
needs zero re-explaining. That configured repo is your entry ticket to CC 301.

## Knowledge check

1. Which tasks justify the most capable model, and which don't?
2. `/compact` vs `/clear` — when is each the right call?
3. Name the three cost habits that don't require counting tokens.
