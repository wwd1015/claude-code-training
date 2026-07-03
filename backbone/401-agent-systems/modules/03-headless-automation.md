---
id: 401-03
title: "Headless & Automation"
duration: 30 min
objectives:
  - Run Claude Code non-interactively with claude -p and capture its output
  - Sketch where an agent fits in CI or a scheduled job
  - Apply the unwatched-agent discipline: explicit verification, bounded permissions
---

## Print mode: the building block

`claude -p "your task"` runs one task with no interactive session and prints
the result to stdout — which makes Claude Code scriptable like any Unix tool:

```bash
claude -p "summarize what changed in this repo since yesterday and flag anything touching the pricing model" > daily-brief.md
```

Structured output (`--output-format json`) and piped input make it composable:
cron jobs, Makefiles, shell scripts, notebook pre-flight checks. See the
[CLI reference](https://code.claude.com/docs/en/cli-reference) for flags
(permission mode, allowed tools, model, output format).

## Where automation fits

Common placements, in increasing ambition:

- **Scheduled chores** — a nightly `claude -p` that QAs yesterday's data drop
  and writes a triage note.
- **CI steps** — on every pull request, an agent reviews the diff against a
  checklist, or regenerates docs the change invalidated. GitHub Actions can
  run Claude Code as a workflow step. <!-- verify: link the official GitHub Actions integration doc for our platform/runner setup -->
- **Event-driven** — a failed pipeline triggers an agent that gathers logs and
  drafts the incident summary before a human arrives.

## The unwatched-agent discipline

Everything from CC 101–301 assumed a human watching. Remove the human and
three practices stop being optional:

1. **Verification is part of the task.** The prompt must say how the agent
   checks its work (run the tests, re-run the query, diff the output), and the
   job must fail loudly when the check fails — an unwatched agent that
   "declares victory" is worse than no agent.
2. **Permissions are pinned down.** Headless runs use explicit tool allowlists
   and the narrowest permission mode that works; never blanket bypass in a
   directory that can reach production.
3. **Output goes somewhere a human looks.** A report nobody reads is a system
   nobody notices failing. Decide the landing place (PR comment, dashboard
   file, alert channel) as part of the design.

**Reuse (official):** [CLI reference](https://code.claude.com/docs/en/cli-reference) ·
[Common workflows](https://code.claude.com/docs/en/common-workflows) ·
[Claude Code best practices (engineering)](https://www.anthropic.com/engineering/claude-code-best-practices)

## Lab

Automate one chore end to end: write a `claude -p` one-liner that inspects
something you check manually (data freshness, failing tests, stale TODOs) and
writes a dated markdown report including its own verification evidence. Run it
twice; confirm the second run's report is trustworthy without you watching it
work. Bonus: put it in cron or your scheduler of choice.

## Knowledge check

1. What does `-p` change about how Claude Code runs?
2. Name the three disciplines that become mandatory when no human watches.
3. Why is "declares victory" the failure mode to design against in automation?
