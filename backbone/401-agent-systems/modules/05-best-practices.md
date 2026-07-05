---
id: 401-05
title: "Best Practices: Context, Cost & Evaluation"
duration: 45 min
objectives:
  - Manage what enters an agent's context window, and why it decides output quality
  - Identify the cost drivers of agent systems and apply the standard controls
  - Set up a lightweight evaluation loop: spot-checks, golden tasks, regression prompts
  - Turn a production failure into a regression golden task so the same failure can't return silently
---

## Context engineering

An agent's output quality is a function of what's in its context window —
not just the prompt you typed, but every file it read, every command output,
every earlier turn. Engineering that, deliberately, is the highest-leverage
skill at this level:

- **Feed conclusions, not raw material.** Subagents exist so fifty files
  become one summary (401-01). The same applies to what *you* paste in.
- **CLAUDE.md is standing context** (CC 201) — keep it current and short;
  every stale line is noise the agent must overcome on every task.
- **New task, new context.** Long sessions accumulate irrelevant history;
  `/clear` beats coaxing a drifted session back on course.
- **Put contracts in writing.** Output format, definition of done, and
  verification steps in the prompt outperform iterating on vibes.

## Cost

Agent systems spend tokens the way pipelines spend compute. The drivers:
context size (re-read on every turn), number of agents, iteration loops, and
model choice. The standard controls:

- Match the model to the step — cheap/fast models for mechanical work
  (formatting, extraction), the strongest model for judgment steps
  (design, verification). Model per subagent is a design decision.
- Cap fan-outs and loops in the design ("at most N items", "two retries");
  unbounded loops are cost incidents waiting to happen.
- Watch for the re-reading pattern: an agent that keeps re-opening the same
  large files needs a summary artifact, not a bigger budget.

## Evaluation

You can't improve — or trust — what you don't measure. Three tiers, adopt in
order:

1. **Spot-check protocol** — a fixed sample rule ("review 2 of every 10
   outputs, always including one edge case"), not ad-hoc glancing.
2. **Golden tasks** — a small suite of representative tasks with known-good
   answers. Run it when you change prompts, skills, or models; it's the unit
   test suite of your agent system.
3. **Regression prompts** — every production failure becomes a golden task, so
   the same failure can't return silently.

Track one adoption metric from day one, even if crude: minutes saved per run,
or reviewer-accepted rate. It's what justifies (or kills) the system later.

## Worked example: making the triage automation trustworthy and cheap

Take the nightly fan-out triage from modules 1 and 3 and turn it from "seems to
work" into "measured and tuned." The demo-03 data ships with
`data/series_truth.csv` — you know exactly which 12 of the 200 series carry
injected anomalies. That's a **golden set for free**:

1. **Golden tasks.** The agent should flag those 12 and leave the other 188
   alone. Score precision and recall against the truth file. Now "improve the
   prompt" has an arbiter that isn't your gut.
2. **Regression prompts.** The night it misses a subtle variance break, add that
   exact series (or a synthetic twin) to the golden set. The suite only grows,
   and that specific miss can never return silently.
3. **Cost, by the drivers.** The fan-out's spend is `~200 × per-series context`.
   Two controls apply directly: run the mechanical per-series check on a
   cheap/fast model and reserve the strongest model for the synthesis/ranking
   step (model-per-subagent is a design decision); and cap the fan-out ("at most
   200 workers, one retry each") so a malformed input directory can't multiply
   the bill.
4. **The re-reading tell.** If the orchestrator keeps re-opening the same big
   baseline file every turn, that's the silent burn — build a one-time summary
   artifact and pass *that* to the workers, not a bigger budget.
5. **One adoption metric.** "Analyst-confirmed flags per run" or "minutes saved
   vs. the manual sweep" — crude is fine; it's what the system is judged on at
   review time.

The loop is the point: golden tasks let you change the prompt, the detector, or
the model and *know* whether you improved it. Several "obvious" improvements will
fail the golden set — that surprise is exactly the value.

### Best practices

- **Feed conclusions, not raw material.** The single highest-leverage habit:
  fifty files become one summary (that's what subagents are for), and the same
  restraint applies to what *you* paste in. Output quality tracks what's in the
  window, not what you meant.
- **Design for the smallest context that does the job.** Cost scales with
  tokens, and tokens are re-read every turn. A tight window is cheaper *and*
  sharper — clutter is something the model has to overcome on every task.
- **Match the model to the step.** Cheap/fast for mechanical work (extraction,
  formatting, per-item checks), the strongest model for judgment (design,
  verification, synthesis). Paying top price for formatting is waste; using a
  cheap model on the judgment step is false economy.
- **Cap every fan-out and loop in the design.** "At most N", "two retries."
  Unbounded loops are cost incidents waiting for a big input.
- **Make golden tasks your unit tests.** A small suite of representative tasks
  with known-good answers, run on every prompt/skill/model change. Where you have
  ground truth (a truth file, a labeled holdout), the metric writes itself.
- **Every production failure becomes a golden task.** Otherwise you fix it today
  and it regresses next quarter with nobody noticing. The suite is how a fix
  stays fixed.
- **Track one adoption metric from day one.** Minutes saved, reviewer-accepted
  rate — crude but honest. It's what justifies or kills the system later.

### Common pitfalls

- **Pasting raw files into context instead of conclusions.** The window fills
  with material the agent must wade through, and quality drops. Fix: summarize
  first (a subagent, a pre-computed artifact), then hand over the summary.
- **Never clearing a drifted session.** A 200-turn session carries 190 turns of
  irrelevant history into every new answer. Fix: new task, new context —
  `/clear` beats coaxing.
- **Tuning on vibes with no golden task to arbitrate.** Every change "feels
  better" and some quietly regress. Fix: write the golden set first; let it
  settle disputes.
- **One expensive model for every step.** You overpay for formatting and
  extraction. Fix: model-per-step; reserve the strong model for judgment.
- **No budget on the loop.** One malformed input and an iteration loop or
  fan-out balloons. Fix: bound it in the design and treat hitting the bound as a
  signal to investigate.

**For quants / For data scientists:** a **Quant**'s golden tasks are historical
episodes with known outcomes — "flag the 2020 vol spike, don't flag the quiet
week after." A **Data Scientist**'s are a labeled holdout with known drift or
leakage. In both, ground truth is what converts "the new prompt seems better"
into "recall went from 0.8 to 0.95" — the same rigor you already apply to a
model, pointed at your agent system.

**Reuse (official):** [Claude Code best practices (engineering)](https://www.anthropic.com/engineering/claude-code-best-practices) ·
[Best practices docs](https://code.claude.com/docs/en/best-practices)

## Lab

For the automation you built in 401-03: (1) write three golden tasks with
expected outputs; (2) run them and record results in `evals.md`; (3) change
the prompt in a way you suspect is an improvement, rerun, and let the golden
tasks arbitrate. Separately, estimate its monthly token cost and note the
single biggest driver.

**Stretch:** apply the biggest cost control your driver analysis points to —
usually model-per-step (cheap model on the mechanical part, strong model on the
judgment part) or a summary artifact to kill a re-reading loop — then rerun the
golden tasks to confirm you cut cost *without* losing quality. Convert one real
miss into a regression golden task and watch the suite grow.

## Knowledge check

1. Why does context engineering dominate prompt wording at the system level?
2. Name three cost drivers and one control for each.
3. What turns a production failure into lasting protection?
4. Why is "the smallest context that does the job" both a cost control and a quality control?
5. **Scenario:** you tweak a prompt and it "feels sharper," but two weeks later
   quality has quietly dropped. Which practice would have caught the regression
   at change time, and how?
