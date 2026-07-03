---
id: 301-02
title: "Skill Creation II: Design Patterns & Testing"
duration: 30 min
objectives:
  - Structure a skill as phases with hard rules so results don't drift
  - Make a skill self-contained enough to survive being shared
  - Test a skill the same way you'd test code — known input, expected output
---

## Workflow-shaped skills

The skills that hold up in daily use read like runbooks, not essays:

- **Phases in order** — "1. Inventory the inputs. 2. Validate. 3. Produce X.
  4. Report." Claude follows numbered phases far more reliably than prose.
- **Hard rules, stated as rules** — a short "never do X / always do Y" list
  ("never modify raw data files", "always report row counts before and
  after"). These are the lines that stop drift.
- **Output contracts** — show the exact table/file format the skill must
  produce. An example beats a description.
- **Escape hatches** — tell the skill what to do when inputs are missing or
  ambiguous ("ask one question, then proceed"), or it will guess.

Study the worked examples in this repo:
[`skills/eda/SKILL.md`](../../../skills/eda/SKILL.md) (phased profiling with
an output contract) and
[`skills/backtest-report/SKILL.md`](../../../skills/backtest-report/SKILL.md)
(a `/backtest-report` command with hard rules about what may not be recomputed).

## Self-contained or it breaks

A shared skill runs on machines that aren't yours. Keep every instruction the
skill needs inside SKILL.md or files in the same folder; refer to paths the
skill can discover ("look for a `data/` directory") rather than paths only you
have. If the skill depends on a tool being installed, say so at the top and
tell Claude how to check.

## Testing a skill

Treat SKILL.md like code: it isn't done until it passes.

1. **Known input → expected output.** Run the skill on a small fixture where
   you know the right answer; diff what you get.
2. **Trigger test.** Ask for the task in your natural words (not the skill's
   name) — does it load? If not, the description is missing your phrasing.
3. **Fresh-session test.** `/clear`, then run it again: skills must not rely
   on anything you said earlier in a conversation.
4. **Break it once.** Feed a missing/odd input and check the escape hatch
   fires instead of a confident wrong answer.

Iterate on the wording exactly as you would on failing code — the skill file
is the program.

**Reuse (official):** [Skills docs](https://code.claude.com/docs/en/skills) ·
[Intro to Agent Skills course](https://anthropic.skilljar.com/introduction-to-agent-skills)

## Lab

Finish the skill you stubbed in module 1: add phases, at least two hard
rules, and an output contract. Then run the four tests above against a small
known input. Ship it to `.claude/skills/` in one of your real repos.

## Knowledge check

1. Name the four structural patterns of a durable skill.
2. Why must a shared skill avoid machine-specific paths?
3. Your skill works when you type its name but never triggers naturally — which test failed, and what do you fix?
