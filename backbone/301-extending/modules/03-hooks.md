---
id: 301-03
title: "Hooks: Guards & Automation"
duration: 30 min
objectives:
  - Explain what hooks are and where they fire in the agentic loop
  - Use a PreToolUse hook as a guard and a PostToolUse hook as automation
  - Choose hooks over instructions when a rule must hold every time
---

## Deterministic enforcement

Everything so far — CLAUDE.md, skills — is *asking nicely*: instructions the
model reads and almost always follows. A **hook** is different: it's a shell
command the harness itself runs at fixed points in the loop. The model can't
skip it, forget it, or talk its way around it. When a rule genuinely must hold
— data protection, mandatory checks — you want a hook, not a sentence.

## Where hooks fire

Hooks attach to lifecycle events in `settings.json`. The two you'll use first:

- **PreToolUse** — runs *before* a tool call executes; can inspect the call
  and **block it**. This is your guard rail.
- **PostToolUse** — runs *after* a tool call succeeds; can't block, but can
  react. This is your automation.

Others exist (session start, prompt submit, on-stop) — see the docs when you
need them.

## The two canonical patterns

**Guard (PreToolUse):** block edits that would touch sensitive data. This
repo's [`examples/hooks/guard-data.sh`](../../../examples/hooks/guard-data.sh)
refuses writes into protected data paths — the edit is stopped before it
happens, every time, regardless of what the conversation said.

**Automation (PostToolUse):** run checks after every edit. This repo's
[`examples/hooks/run-checks.sh`](../../../examples/hooks/run-checks.sh) lints
Python files after Claude writes them, so style feedback arrives immediately
and Claude fixes its own output in the same session.

Wiring lives in
[`examples/hooks/settings.sample.json`](../../../examples/hooks/settings.sample.json)
and the walkthrough in [demo 05](../../../demos/05-hooks-automation.md) — copy,
adapt the paths, done.

## Instructions vs hooks — the decision rule

| The rule is... | Use |
|---|---|
| a preference ("prefer pandas idioms") | CLAUDE.md |
| a workflow ("this is how we build reports") | skill |
| a *must-never* / *must-always* | hook |

Hooks run with your permissions on your machine — read a hook script before
installing it, exactly as you would any code you didn't write.

**Reuse (official):** [Hooks docs](https://code.claude.com/docs/en/hooks) ·
[Settings docs](https://code.claude.com/docs/en/settings)

## Lab

Install the sample guard hook in a scratch repo (copy `examples/hooks/` and
its `settings.sample.json` wiring). Ask Claude to edit a protected file and
watch the block fire. Then adapt the guard to one path that actually matters
in your work — or wire `run-checks.sh` to your linter — and confirm it fires
on a real edit.

## Knowledge check

1. What can a PreToolUse hook do that a PostToolUse hook cannot?
2. Why is a hook stronger than the same rule written in CLAUDE.md?
3. "Never write to `prod_configs/`" — CLAUDE.md, skill, or hook? Why?
