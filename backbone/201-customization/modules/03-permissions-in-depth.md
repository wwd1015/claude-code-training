---
id: 201-03
title: "Permissions in Depth"
duration: 40 min
objectives:
  - Read and write allow/deny permission rules in settings.json
  - Build a deliberate allowlist instead of an accidental one
  - Ship safe permission defaults to a whole team via project settings
  - Use deny rules and modes as guardrails, not just conveniences
---

## From reflex clicks to written policy

In CC 101 you approved actions one prompt at a time, and "don't ask again"
quietly built you an allowlist. This module makes that list deliberate.
Permissions live in settings.json (all three levels from module 2) as rules:

```json
{
  "permissions": {
    "allow": [
      "Bash(pytest *)",
      "Bash(python scripts/*)",
      "Read(~/data/reference/**)"
    ],
    "deny": [
      "Read(./secrets/**)",
      "Bash(rm -rf *)"
    ]
  }
}
```

Rules name a tool and a pattern. **Deny beats allow** when both match — so
deny rules are your guardrails and allow rules are your convenience.
<!-- verify: exact rule syntax against current settings docs before teaching -->

There is also a middle list, `ask`, that forces a prompt even for something
that would otherwise be allowed — useful for actions you want to *see* happen
every time (a deploy, a write to a shared table) without blocking them
outright. Precedence still runs deny first. <!-- verify: `ask` list behavior against current docs -->

## Building the allowlist deliberately

The workflow that works:

1. Run a week in default mode; notice what you approve constantly.
2. Promote the *narrowest version* of each into `allow` — `pytest *`, not `Bash(*)`.
3. Add `deny` rules for the things that must never happen in this repo:
   credentials paths, raw-data writes, destructive git.

The asymmetry to respect: a too-narrow allow costs you one extra click; a
too-broad allow costs you an incident.

Editing the JSON by hand isn't the only way in. `/permissions` opens the rule
lists in-session so you can review what you have accumulated and tighten it —
worth doing every few weeks, because allowlists grow by accretion and rarely
shrink on their own. <!-- verify: /permissions command name against current docs -->

## Team defaults

Because project `.claude/settings.json` is committed, a repo owner can ship
permission policy with the code: everyone who clones gets the same guardrails
and the same conveniences on day one. Personal loosening goes in
`settings.local.json` — never loosen the shared file to fix a private itch.
Permission *modes* (CC 101) still apply on top: modes set how much is asked,
rules set what's allowed at all.

## Worked example: hardening a data-QA repo before the desk clones it

You own a data-QA repo the whole desk will use. It runs read-heavy checks and
must never write raw data or touch credentials. You want new clones safe *and*
frictionless. Put policy in the committed project file:

```json
{
  "permissions": {
    "allow": [
      "Bash(pytest *)",
      "Bash(python -m qa.checks *)",
      "Read(./data/reference/**)"
    ],
    "ask": [
      "Bash(python -m qa.publish *)"
    ],
    "deny": [
      "Read(./credentials/**)",
      "Read(./.env*)",
      "Write(./data/raw/**)",
      "Bash(rm -rf *)"
    ]
  }
}
```

**What each block buys you:** the `allow` list means the routine checks run
without a prompt on a fresh clone. The `ask` list means publishing QA results
still runs, but a human sees it every time. The `deny` list is the part that
matters most — even if someone (or Claude) tries to read `.env` or overwrite
`data/raw/`, it is refused regardless of mode.

**How you verify:** in a fresh clone, ask Claude to run the QA checks — they run
with no prompt. Ask it to read `credentials/warehouse.key` — it is refused, not
prompted. Ask it to publish — you get a prompt even though nothing blocks it.
That is the shape of a deliberate allowlist: cheap things silent, dangerous
things impossible, sensitive things visible.

### Best practices

- **Deny is a guardrail; write it first.** Allow rules save clicks; deny rules
  prevent incidents. A credentials path, `data/raw/`, and destructive git
  belong in `deny` before you tune a single convenience.
- **Promote the narrowest pattern that covers the approval.** `Bash(pytest *)`,
  not `Bash(*)`. A broad allow silently green-lights things you never meant to
  approve; the narrow one costs one extra click on the rare edge case.
- **Ship policy with the repo.** Put shared guardrails in the committed project
  file so every clone is safe on day one. New teammates inherit the policy
  instead of rebuilding it click by click.
- **Loosen locally, never in the shared file.** A personal convenience goes in
  `settings.local.json`. Widening the committed allowlist to scratch your own
  itch weakens everyone's guardrails.
- **Audit the list periodically.** Allowlists grow by accretion. Every few
  weeks, open `/permissions` and delete rules you no longer recognize or need.
- **Match the mode to the moment.** Rules define what's possible; modes define
  how much is asked. Use a tighter mode on an unfamiliar or production-touching
  repo even when your rules are solid.

### Common pitfalls

**You allow `Bash(*)` to stop the prompts.** Now every shell command runs
unseen, including ones you would never have approved. Fix: allow the specific
commands you actually repeat, narrowly scoped.

**You rely on allow rules to keep data safe.** Allow only adds convenience; it
protects nothing. Fix: the thing that must never happen goes in `deny`, which
wins over allow.

**You loosen the committed file for a one-off.** The whole team inherits the
looser policy and nobody notices. Fix: personal exceptions go in
`settings.local.json`.

**You forget deny beats allow and expect an allow to "win."** You allowed a
path but also denied a subpath, and are confused when it's refused. Fix:
internalize the order — deny is checked first and always wins.

**For quants:** guard the things a re-run can't undo — writing over a published
curve, mutating a golden results file, kicking a job to a shared grid. Those
belong in `deny` or `ask`, not in the allow list, however often you do them.

**For data scientists:** guard the expensive and the irreversible — a `deny` on
paths that trigger a full retrain or a large cloud spend, an `ask` on anything
that writes to a production feature store. Cheap local reads can be allowed
freely; the blast radius is what decides the list.

**Reuse (official):** [Settings docs](https://code.claude.com/docs/en/settings) ·
[Security docs](https://code.claude.com/docs/en/security)

## Lab

For your own repo: (1) list the five approvals you grant most often and write
them as narrow allow rules in project settings; (2) add two deny rules
protecting what actually matters there (a data directory, an env file);
(3) verify both directions in a fresh session — an allowed command runs
without a prompt, a denied read is refused.

**Stretch:** pick one action you want to *keep doing but always see* — a
publish, a write to a shared table, a deploy — and move it into an `ask` rule.
Confirm it still runs but prompts every time, and explain to yourself why that's
different from both allow and deny.

## Knowledge check

1. Allow says yes, deny says no, both match — what happens?
2. Why promote the *narrowest* pattern that covers a repeated approval?
3. Your teammate's clone should refuse to read `credentials/`. Which file does the rule go in, and why not `settings.local.json`?
4. When would you use an `ask` rule instead of `allow` or `deny`?
5. A teammate says "I got sick of the prompts so I added `Bash(*)` to allow." What's the risk, and what should they do instead?
