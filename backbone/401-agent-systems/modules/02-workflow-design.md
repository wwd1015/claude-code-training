---
id: 401-02
title: "Designing Multi-Agent Workflows"
duration: 35 min
objectives:
  - Recognize the four core workflow shapes and what each is for
  - Decide which parts of a task fan out and which must stay sequential
  - Design for failure — agents that return nothing, or the wrong thing
---

## The four shapes

Most multi-agent designs are compositions of four shapes:

1. **Fan-out / map** — the same task over many independent items (review every
   notebook, profile every table). Wall-clock ≈ the slowest item, not the sum.
2. **Pipeline** — each item flows through stages (extract → validate →
   summarize) with no barrier between items; item A can be in stage 3 while
   item B is in stage 1.
3. **Generate-then-verify** — one agent produces, a second independently
   checks. The verifier gets *only* the artifact and the acceptance criteria —
   never the generator's reasoning — or it inherits the same blind spots.
   Make it adversarial: "try to refute this" outperforms "check this".
4. **Orchestrator + workers** — a coordinator decomposes, dispatches, and
   synthesizes. Your main Claude Code session is already this; the design work
   is deciding what the workers are.

## What fans out, what stays sequential

Fan out when items are **independent** (no item needs another's output) and
**self-contained to brief** (the prompt fits in a paragraph). Keep sequential
when outputs chain, when a shared resource would conflict (two agents editing
one file), or when early results should change later work — a discovery step
that reshapes the plan belongs before the fan-out, not inside it.

The practical method: write the work as a list. Draw arrows for "needs the
output of." Arrow-free groups fan out; chains become pipeline stages.

## Designing for failure

At N agents, someone returns nothing useful. Decide *in the design*:

- **Empty result** — is it "no findings" (fine) or "task failed" (retry once,
  then surface)? Force the distinction: require a structured answer
  ("return `NONE` if no issues") so silence is never ambiguous.
- **Wrong result** — verification (shape 3) is the systematic answer;
  spot-checking a sample is the cheap one. Match rigor to blast radius.
- **Partial completion** — synthesize what arrived and *name what's missing*;
  a report that silently covers 7 of 10 items reads as complete and isn't.

**Reuse (official):** [Building effective agents (engineering)](https://www.anthropic.com/engineering/building-effective-agents) ·
[Subagents docs](https://code.claude.com/docs/en/sub-agents)

## Lab

Take a real recurring deliverable of yours with 3+ separable parts (a periodic
report, a multi-dataset QA pass). On paper: list the pieces, draw the
dependency arrows, choose shapes. Then run the fan-out part with subagents
from your session, using your module-1 reviewer as a verify stage on the
merged result. Compare against doing it in one linear session.

## Knowledge check

1. Which shape fits: "summarize each of 12 experiment logs, then rank the findings"?
2. Why should a verifier not see the generator's reasoning?
3. Your fan-out returns 9 of 10 reports. What does a well-designed synthesis step do?
