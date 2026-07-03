---
id: 401-05
title: "Best Practices: Context, Cost & Evaluation"
duration: 35 min
objectives:
  - Manage what enters an agent's context window, and why it decides output quality
  - Identify the cost drivers of agent systems and apply the standard controls
  - Set up a lightweight evaluation loop: spot-checks, golden tasks, regression prompts
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

**Reuse (official):** [Claude Code best practices (engineering)](https://www.anthropic.com/engineering/claude-code-best-practices) ·
[Best practices docs](https://code.claude.com/docs/en/best-practices)

## Lab

For the automation you built in 401-03: (1) write three golden tasks with
expected outputs; (2) run them and record results in `evals.md`; (3) change
the prompt in a way you suspect is an improvement, rerun, and let the golden
tasks arbitrate. Separately, estimate its monthly token cost and note the
single biggest driver.

## Knowledge check

1. Why does context engineering dominate prompt wording at the system level?
2. Name three cost drivers and one control for each.
3. What turns a production failure into lasting protection?
