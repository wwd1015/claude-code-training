---
id: 401-03
title: "Headless & Automation"
duration: 40 min
objectives:
  - Run Claude Code non-interactively with claude -p and capture its output
  - Sketch where an agent fits in CI or a scheduled job
  - Apply the unwatched-agent discipline: explicit verification, bounded permissions
  - Turn an agent's self-assessment into an exit code so an unwatched run fails loudly
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

## Worked example: a nightly QA run that fails loudly

The pattern that separates a real automation from a toy is that its verdict
becomes an **exit code** the scheduler can act on. Wrap the agent so its
self-assessment can't be ignored:

```bash
#!/usr/bin/env bash
set -euo pipefail
REPORT="reports/qa-$(date +%F).md"

claude -p "Profile today's drop in data/drop/ against baselines/ and write a
dated QA report to $REPORT. Run check_drop.py and paste its output as your
verification evidence. End the report with exactly one line:
'STATUS: PASS' or 'STATUS: FAIL'." \
  --max-turns 40                      # <!-- verify: confirm --max-turns spelling against the current CLI reference -->

grep -qx "STATUS: PASS" "$REPORT" \
  || { echo "QA gate failed — see $REPORT" >&2; exit 1; }
```

Five design decisions are visible in ten lines: the agent runs `check_drop.py`
and must **paste its output** (verification evidence, not a claim); it emits a
**machine-readable verdict** the wrapper turns into an exit code; `--max-turns`
**bounds the run** so a confused agent can't loop forever; the report lands in a
**dated file** a human (and tomorrow's audit) can find; and a non-`PASS` verdict
makes the job **exit nonzero**, so cron or CI raises the alarm instead of the
failure passing silently. Give this run write access to `reports/` and read
access to the data — nothing near production.

### Best practices

- **Make the acceptance check something the job can assert on.** A grep-able
  `STATUS:` line, a nonzero exit, a JSON field — not prose a human has to read.
  If the automation can't tell pass from fail by itself, it isn't unattended.
- **Fail loudly, never silently.** Wire the verdict to an exit code and route
  failures to a channel someone watches. A green run nobody looks at and a red
  run nobody hears about are the same broken system.
- **Budget every run.** Cap turns (and, where your runner supports it, wall
  time) so a stuck agent is a bounded cost, not a surprise bill. Unbounded
  headless loops are the classic overnight incident.
- **Pin permissions to the narrowest set that works.** Explicit tool allowlist,
  least-privilege permission mode, and a working directory that can't reach
  production. Never blanket-bypass permissions in a checkout wired to prod.
- **Keep the run idempotent and observable.** Same input should yield the same
  verdict; write the report, the command's inputs, and the verification evidence
  to files so a failure two weeks later is diagnosable, not a mystery.
- **Log what ran, not just what happened.** Stamp the prompt/skill version into
  the report. When output quality shifts, the first question is "what changed?"
  — and you want the answer on disk.

### Common pitfalls

- **No verification step — the agent "declares victory."** It writes a
  confident report and exits 0 having checked nothing. Fix: require it to run a
  real check and surface the check's result; gate the exit code on that result,
  not on the agent's self-satisfaction.
- **Output goes to stdout and nobody captures it.** The nightly run "works" and
  its findings evaporate. Fix: redirect to a dated file or a channel, decided in
  the design.
- **Blanket-bypassing permissions to "just make it run."** Convenient today, a
  production incident the night the prompt drifts. Fix: allowlist the exact
  tools; place the run where the dangerous paths don't exist.
- **Unbounded run with no turn cap.** One malformed input and the agent loops
  until morning. Fix: set a turn budget and treat hitting it as a failure to
  investigate.

**For quants / For data scientists:** a **Quant** runs the nightly curve/rates
QA before the desk opens — the acceptance rule is *economic* (a negative
overnight rate, a stale fixing = `FAIL`). A **Data Scientist** runs a freshness
and drift check before the morning retrain — the rule is *statistical*
(row-count collapse, feature drift beyond threshold). Different checks, identical
discipline: the verdict must be assertable by the machine, never eyeballed.

**Reuse (official):** [CLI reference](https://code.claude.com/docs/en/cli-reference) ·
[Common workflows](https://code.claude.com/docs/en/common-workflows) ·
[Claude Code best practices (engineering)](https://www.anthropic.com/engineering/claude-code-best-practices)

## Lab

Automate one chore end to end: write a `claude -p` one-liner that inspects
something you check manually (data freshness, failing tests, stale TODOs) and
writes a dated markdown report including its own verification evidence. Run it
twice; confirm the second run's report is trustworthy without you watching it
work. Bonus: put it in cron or your scheduler of choice.

**Stretch:** wrap it in the exit-code pattern above — have the agent end with a
`STATUS: PASS`/`FAIL` line and make the script exit nonzero on failure. Then
break the input on purpose (feed it a truncated file) and confirm the job goes
red instead of quietly reporting success. Add a turn budget and note what
happens when you set it deliberately too low.

## Knowledge check

1. What does `-p` change about how Claude Code runs?
2. Name the three disciplines that become mandatory when no human watches.
3. Why is "declares victory" the failure mode to design against in automation?
4. How do you turn an agent's self-assessment into something a scheduler or CI can act on?
5. **Scenario:** your nightly run has been green for a month, but you later learn
   it never actually checked anything. Which one design decision would have
   caught this, and how?
