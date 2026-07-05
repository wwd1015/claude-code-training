---
id: 201-05
title: "Models, Context & Cost"
duration: 35 min
objectives:
  - Match model choice to task difficulty
  - Manage the context window: /compact, /clear, and session scope
  - Build cost-awareness habits without becoming a token accountant
  - Recognize when a session has degraded and reset it deliberately
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

The point isn't to minimize spend on every turn — it's to spend where judgment
matters. A hard debugging session on the capable model that lands in twenty
minutes is cheaper, in your time and in tokens, than an hour of a cheaper model
circling the problem.

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

Two refinements worth knowing. `/compact` can take a focus instruction —
`/compact keep the feature-engineering decisions, drop the debugging` — so the
summary keeps what you still need. And when context runs low, Claude Code will
auto-compact rather than fail; that is a safety net, not a plan, and an
auto-compact mid-thought is a sign the session should have been scoped tighter.
`/context` shows what is currently filling the window when you want to look.
<!-- verify: /context command and auto-compact behavior against current docs -->

## Cost habits

You don't need per-token bookkeeping; you need three habits: know roughly
what a normal session costs for your usage (`/cost` shows the session's
spend), notice outliers and ask why (usually a runaway loop or a giant file
read), and prefer scoped sessions — the same habit that improves quality
cuts cost. <!-- verify: /cost availability under your org's billing/subscription setup -->

## Worked example: a long research session that started to drift

You're refactoring a feature pipeline. Two hours in, Claude starts
re-suggesting a change it already made and forgets a decision from early on.
That's the context window telling you something, and the fix depends on the
cause.

**Diagnose first.** Run `/context` (or just notice the symptoms: slower
replies, repeated suggestions, vagueness about early details). The window is
full of a long back-and-forth, most of it now irrelevant.

**Then pick the right reset:**

- The new task is *unrelated* to the refactor (you're moving on to a data-QA
  bug)? `/clear`. Carrying the refactor's context into a QA task only adds fog.
- You're *still on the refactor* and need continuity? `/compact keep the final
  pipeline design and the decisions we made; drop the dead ends`. The session
  continues from a clean summary that preserves what matters.

**How you verify it worked:** after the reset, ask Claude to restate the current
plan. On a good compact it reproduces the decisions you told it to keep; if it
lost one, that decision belonged in a file (a CLAUDE.md line, a design note),
not just in the chat. The durable fix for "it forgot" is usually to write the
decision down, not to compact more carefully.

### Best practices

- **Reach for the model that fits the task, not the cheapest by reflex.** Spend
  capability where judgment matters; save it on mechanical work. The expensive
  mistake is a cheap model looping on a hard problem.
- **Escalate, then de-escalate.** Start capable on an unfamiliar or hard task,
  and drop to a faster model for the repetitive tail once the pattern is set.
- **`/clear` between unrelated tasks.** A fresh window is faster, cheaper, and
  sharper than one carrying a previous task's residue. Make it a reflex on
  every context switch.
- **`/compact` at natural breakpoints, with a focus.** Compact when you finish a
  phase and want to continue, and tell it what to keep. Don't wait for an
  auto-compact to interrupt you mid-thought.
- **Write durable facts to files, not chat.** Anything you'd hate to lose to a
  compact — a design decision, a gotcha — belongs in CLAUDE.md or a note, where
  it survives every reset for a few lines of cost.
- **Check `/cost` occasionally to calibrate, not to obsess.** Learn your normal
  and investigate outliers; a spike is usually a runaway loop or a giant read,
  which is a bug to fix, not a number to fret over.

### Common pitfalls

**You run the whole day in one session to "keep context."** The window fills
with stale detail, quality drops, and cost climbs. Fix: one task, one session;
`/clear` between them.

**You keep the most capable model on for trivial edits.** You pay top rate to
reformat a file. Fix: drop to a faster model for mechanical work once the hard
thinking is done.

**You compact and lose the one decision you needed.** A blind `/compact` summary
dropped it. Fix: pass a focus instruction, and write load-bearing decisions to
a file so no reset can lose them.

**You treat auto-compact as normal.** Hitting it every session means your
sessions are scoped too wide. Fix: scope tighter and compact deliberately at
breakpoints instead of waiting to be interrupted.

**For quants:** your hard, capable-model tasks are usually reasoning-dense —
deriving a model, debugging why a cointegration test disagrees with intuition,
a tricky refactor of shared pricing code. Mechanical R/MATLAB-to-Python
translation or docstring passes are fine on a faster model.

**For data scientists:** your context fills fast because artifacts are large —
don't paste a 400 MB dataframe or a giant log into the session; point Claude at
the file and let it sample. Reserve the capable model for pipeline architecture
and thorny training bugs, not for regenerating boilerplate configs.

**Reuse (official):** [Best practices](https://code.claude.com/docs/en/best-practices) ·
[How Claude Code works](https://code.claude.com/docs/en/how-claude-code-works)

## Lab (course capstone)

Put the whole course together on your primary repo: (1) write or finish its
`CLAUDE.md` (module 1 draft, now battle-tested); (2) commit project settings
with your allowlist and one env var; (3) ship one custom slash command for a
recurring task. Fresh session, run the command — the goal is a session that
needs zero re-explaining. That configured repo is your entry ticket to CC 301.

**Stretch:** run one deliberately long task on that repo and practice the
context controls — check `/context`, `/compact` at a breakpoint with a focus
instruction, and confirm afterward that Claude still holds the decisions you
told it to keep. Note any decision it lost and move that one into CLAUDE.md or a
design note so the next session can't lose it.

## Knowledge check

1. Which tasks justify the most capable model, and which don't?
2. `/compact` vs `/clear` — when is each the right call?
3. Name the three cost habits that don't require counting tokens.
4. Why pass a focus instruction to `/compact` instead of a bare `/compact`?
5. A teammate says Claude "keeps forgetting a decision we made two hours ago" in a long session. Give them two fixes — one for right now, one so it doesn't recur.
