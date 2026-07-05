---
id: 401-02
title: "Designing Multi-Agent Workflows"
duration: 45 min
objectives:
  - Recognize the four core workflow shapes and what each is for
  - Decide which parts of a task fan out and which must stay sequential
  - Design for failure — agents that return nothing, or the wrong thing
  - Compose the shapes into one workflow and place the verification stage where it earns its cost
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

## Worked example: the nightly data-QA workflow

A realistic system uses more than one shape. Say every night you validate a data
drop of ~30 tables before the morning models consume it. Compose:

1. **Fan-out** over the 30 tables — one subagent profiles each (row counts,
   null rates, type drift, range checks) against last week's baseline and
   returns `TABLE_OK` or a structured list of deviations. Independent work, so
   it maps.
2. **Pipeline** inside each worker — profile → threshold → classify severity —
   because those stages chain for one table but never block another table.
3. **Generate-then-verify** on the merged result — a second agent takes *only*
   the flagged deviations plus the acceptance rules ("a null-rate jump >5pp on a
   key column is a blocker") and rules each one blocker / warning / false alarm.
   It does **not** see the profiler's reasoning, so it can't rubber-stamp it.
4. **Orchestrator** synthesizes: a ranked blocker list, the warnings below it,
   and — critically — *"profiled 28 of 30 tables; `fx_rates` and `positions`
   timed out, not yet checked."*

Notice what stayed sequential: the baseline for step 1 is loaded *once, first*,
because it reshapes what every worker checks. That discovery step belongs before
the fan-out, never inside it. And the verify stage sits exactly where a wrong
answer is expensive — the gate between "data looks fine" and "models run on it."

### Best practices

- **Start with the simplest shape that works.** A single agent with a good tool
  and a clear contract beats a premature multi-agent system you have to debug.
  Reach for fan-out when the wall-clock or the context math forces it — not
  because parallel looks sophisticated.
- **Parallelize only genuinely independent work.** The dependency arrows are the
  design. If item B needs item A's output, they are pipeline stages, not a
  fan-out — running them in parallel just races.
- **Make verification a first-class stage, not a footnote.** Decide up front
  what gets checked, by whom, and against which acceptance criteria. Match the
  rigor to the blast radius: a full adversarial verify before data feeds
  production, a cheap spot-check for a throwaway summary.
- **Give the verifier only the artifact and the criteria.** Feed it the
  generator's reasoning and it inherits the same blind spots — it will confirm
  what it was told rather than test it. "Try to refute this" beats "check this."
- **Bound every fan-out and loop in the design.** "At most N workers", "one
  retry, then surface." An unbounded fan-out over an unbounded input is a cost
  and latency incident waiting for a big input.
- **Make the synthesis step name what's missing.** The dangerous report is the
  one that covers 7 of 10 items and reads as complete. Require the coverage line
  as part of the output contract.

### Common pitfalls

- **Fanning out work that actually chains.** Two workers edit the same file, or
  worker B needs worker A's output that isn't there yet. Fix: draw the "needs
  the output of" arrows first; only arrow-free groups may fan out.
- **The verifier sees the generator's chain of thought.** It agrees with the
  reasoning instead of testing the artifact. Fix: pass the artifact and the
  acceptance criteria only — nothing about how it was produced.
- **No sentinel for "nothing found."** Silence is ambiguous: did the worker find
  no issues, or did it fail? Fix: require an explicit `NONE` (or `TABLE_OK`) so
  empty is a stated answer, not a missing one.
- **Orchestrator context bloat.** Workers hand back full transcripts and the
  coordinator's window fills with raw material it was supposed to avoid. Fix:
  tighten each worker's report contract so it returns conclusions, then
  synthesize from those.

**For quants / For data scientists:** a **Quant** validating a rates data drop
cares that the verify stage encodes *economic* acceptance rules (a negative
overnight rate is a blocker, not a warning); a **Data Scientist** guarding a
training table cares about distributional drift and leakage. Same four shapes —
the acceptance criteria you hand the verifier are where your **Technique** lives.

**Reuse (official):** [Building effective agents (engineering)](https://www.anthropic.com/engineering/building-effective-agents) ·
[Subagents docs](https://code.claude.com/docs/en/sub-agents)

## Lab

Take a real recurring deliverable of yours with 3+ separable parts (a periodic
report, a multi-dataset QA pass). On paper: list the pieces, draw the
dependency arrows, choose shapes. Then run the fan-out part with subagents
from your session, using your module-1 reviewer as a verify stage on the
merged result. Compare against doing it in one linear session.

**Stretch:** find the discovery step in your deliverable — the one whose output
reshapes every later piece (loading a baseline, picking the reporting period) —
and prove it belongs *before* the fan-out by trying to push it inside and
watching the workers disagree on scope. Then write the acceptance criteria your
verify stage checks, as if handing them to someone who never saw the data.

## Knowledge check

1. Which shape fits: "summarize each of 12 experiment logs, then rank the findings"?
2. Why should a verifier not see the generator's reasoning?
3. Your fan-out returns 9 of 10 reports. What does a well-designed synthesis step do?
4. Where does a discovery step that reshapes the plan belong relative to the fan-out, and why?
5. **Scenario:** a teammate proposes ten parallel workers where worker 4 needs
   worker 3's cleaned output. What breaks, and what's the correct shape?
