---
id: 201-03
title: "Permissions in Depth"
duration: 30 min
objectives:
  - Read and write allow/deny permission rules in settings.json
  - Build a deliberate allowlist instead of an accidental one
  - Ship safe permission defaults to a whole team via project settings
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

## Building the allowlist deliberately

The workflow that works:

1. Run a week in default mode; notice what you approve constantly.
2. Promote the *narrowest version* of each into `allow` — `pytest *`, not `Bash(*)`.
3. Add `deny` rules for the things that must never happen in this repo:
   credentials paths, raw-data writes, destructive git.

The asymmetry to respect: a too-narrow allow costs you one extra click; a
too-broad allow costs you an incident.

## Team defaults

Because project `.claude/settings.json` is committed, a repo owner can ship
permission policy with the code: everyone who clones gets the same guardrails
and the same conveniences on day one. Personal loosening goes in
`settings.local.json` — never loosen the shared file to fix a private itch.
Permission *modes* (CC 101) still apply on top: modes set how much is asked,
rules set what's allowed at all.

**Reuse (official):** [Settings docs](https://code.claude.com/docs/en/settings) ·
[Security docs](https://code.claude.com/docs/en/security)

## Lab

For your own repo: (1) list the five approvals you grant most often and write
them as narrow allow rules in project settings; (2) add two deny rules
protecting what actually matters there (a data directory, an env file);
(3) verify both directions in a fresh session — an allowed command runs
without a prompt, a denied read is refused.

## Knowledge check

1. Allow says yes, deny says no, both match — what happens?
2. Why promote the *narrowest* pattern that covers a repeated approval?
3. Your teammate's clone should refuse to read `credentials/`. Which file does the rule go in, and why not `settings.local.json`?
