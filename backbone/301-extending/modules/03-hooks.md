---
id: 301-03
title: "Hooks: Guards & Automation"
duration: 45 min
objectives:
  - Explain what hooks are and where they fire in the agentic loop
  - Use a PreToolUse hook as a guard and a PostToolUse hook as automation
  - Write hooks with hygiene — least-scope matchers, fast scripts that fail loudly
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

## Worked example: a data-guard hook, wired end to end

A CLAUDE.md line saying "never edit files under `data/raw/`" is advisory — the
model reads it and *usually* complies. On the one session it doesn't, your raw
data is gone. A `PreToolUse` guard makes it impossible. Two pieces: the wiring
in `settings.json` and the script it runs.

The wiring (from this repo's
[`examples/hooks/settings.sample.json`](../../../examples/hooks/settings.sample.json))
attaches the guard to every file-mutating tool:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Edit|Write|MultiEdit",
        "hooks": [
          { "type": "command",
            "command": "${CLAUDE_PROJECT_DIR}/.claude/hooks/guard-data.sh" }
        ]
      }
    ]
  }
}
```

The `matcher` is a regex over tool names — here, the three tools that write
files — so the guard can't be sidestepped by using `Write` instead of `Edit`.
The script receives the tool call as JSON on stdin, decides, and signals with
its exit code: **exit code `2` blocks** the call and feeds stderr back to
Claude as the reason; exit `0` allows it. A minimal guard:

```bash
#!/usr/bin/env bash
# Block any write whose target path is under a protected data directory.
payload=$(cat)
path=$(printf '%s' "$payload" | python3 -c 'import sys,json; print(json.load(sys.stdin).get("tool_input",{}).get("file_path",""))')
case "$path" in
  */data/raw/*|*/data/gold/*)
    echo "Refusing to modify protected data path: $path" >&2
    exit 2 ;;
esac
exit 0
```

Now ask Claude to "clean up `data/raw/prices.parquet`" and the edit is stopped
before it happens — not discouraged, stopped — with the message shown back so
Claude picks a non-protected path instead. The exact stdin schema and
exit-code contract live in the [hooks docs](https://code.claude.com/docs/en/hooks);
keep the script to a few lines so it stays fast and obviously correct.

### Best practices

- **Use a hook for anything that must ALWAYS happen; CLAUDE.md for anything
  advisory.** Hooks are a deterministic guarantee the model can't skip; CLAUDE.md
  is a strong suggestion it usually follows. Data protection and mandatory
  checks are hook territory.
- **Keep hook scripts fast and fail loudly.** A `PreToolUse` hook runs on every
  matching tool call, so a slow script taxes the whole session. Do one cheap
  check and exit; when you block, print a clear reason to stderr so Claude (and
  you) know why.
- **Scope the `matcher` to the tools that matter.** `Edit|Write|MultiEdit` for a
  file guard; a `Bash` matcher for a command guard. A guard that fires on tools
  it doesn't understand just adds noise and latency.
- **Guard with `PreToolUse`, automate with `PostToolUse`.** Only a pre-hook can
  block; a post-hook reacts (lint, format, notify) after the fact. Don't try to
  prevent something with a post-hook — it runs too late.
- **Check hook scripts into the repo so the guarantee is shared.** A guard that
  lives only on your machine protects only you. Commit `.claude/hooks/` and the
  `settings.json` wiring so every clone inherits the same rails (CC 301
  module 6).
- **Read any hook before you install it.** It runs with your permissions on
  your machine, every session — treat a copied hook exactly like a copied
  dependency.

### Common pitfalls

- **Writing the rule in CLAUDE.md and assuming it's enforced.** "Never touch
  `prod_configs/`" in prose is advisory; the model can still be argued into it.
  *Fix:* if it must never happen, make it a `PreToolUse` guard that exits
  non-zero on that path.
- **Trying to block a bad edit from a `PostToolUse` hook.** The write already
  happened by then. *Fix:* move the check to `PreToolUse`, where a non-zero
  exit actually prevents the call.
- **A slow or flaky hook that stalls the loop.** Shelling out to a network
  service on every edit makes the whole session drag. *Fix:* keep guards to a
  local, sub-second check; push anything heavy to a manual step.
- **Over-broad matcher blocking legitimate work.** A guard matching every path
  under `data/` also blocks writing a report into `data/reports/`. *Fix:*
  protect the specific sub-paths that are genuinely read-only.

**For quants:** the highest-value guard is usually protecting a *golden* input
or a validated model artifact — the calibration file a backtest depends on must
never be silently overwritten mid-session. **For data scientists:** it's more
often protecting raw/immutable data partitions and wiring `run-checks.sh` to a
linter so generated feature code is style-clean before it lands.

**Reuse (official):** [Hooks docs](https://code.claude.com/docs/en/hooks) ·
[Settings docs](https://code.claude.com/docs/en/settings)

## Lab

Install the sample guard hook in a scratch repo (copy `examples/hooks/` and
its `settings.sample.json` wiring). Ask Claude to edit a protected file and
watch the block fire. Then adapt the guard to one path that actually matters
in your work — or wire `run-checks.sh` to your linter — and confirm it fires
on a real edit.

**Stretch goal:** make the guard prove it's deterministic, not advisory. In the
same session, add a CLAUDE.md line asking Claude *not* to touch the protected
path, then explicitly instruct it to overwrite the file anyway ("ignore that
rule, I need you to edit it"). The hook still blocks the write — that gap
between the model agreeing to your instruction and the harness refusing the
tool call is the entire lesson. Commit the hook so a teammate inherits the same
guarantee.

## Knowledge check

1. What can a PreToolUse hook do that a PostToolUse hook cannot?
2. Why is a hook stronger than the same rule written in CLAUDE.md?
3. "Never write to `prod_configs/`" — CLAUDE.md, skill, or hook? Why?
4. Your guard script calls an internal API to check permissions on every edit
   and the session feels sluggish. What's the problem and how do you fix it
   without dropping the guarantee?
5. **Scenario:** A teammate wants Claude to auto-format every Python file it
   writes and to *prevent* any write under `data/raw/`. Which event does each
   task use, and why can't one hook do both jobs?
