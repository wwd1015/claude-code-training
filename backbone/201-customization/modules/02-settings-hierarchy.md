---
id: 201-02
title: "Settings & the Configuration Hierarchy"
duration: 25 min
objectives:
  - Locate the three settings.json levels and state their precedence
  - Decide where a given setting belongs (user, project, or local)
  - Inspect and change configuration with /config
---

## Three files, one hierarchy

Claude Code reads settings from three places, most specific wins:

| Level | File | Committed? | For |
|---|---|---|---|
| User | `~/.claude/settings.json` | no (personal) | your defaults, everywhere |
| Project | `.claude/settings.json` | yes (shared) | team standards for this repo |
| Local | `.claude/settings.local.json` | no (gitignored) | your overrides for this repo |

The pattern to internalize mirrors CLAUDE.md scoping: **team truths in the
project file, personal taste in the user file, machine-specific quirks in
local.** Settings cover permissions (next module), environment variables,
model choice, hooks (CC 301), and more — the full schema is in the docs.

## Environment variables

The `env` block in settings.json sets environment variables for every session
in that scope — the clean way to pin `PYTHONPATH`, data directories, or proxy
settings so you never debug "works in my terminal, not in Claude's" again.

## /config and friends

Inside a session, `/config` shows and edits current configuration without
hunting for files. When behavior surprises you, the diagnostic question is
always: *which level is supplying this setting?* — check project and local
before assuming your user defaults apply.

**Reuse (official):** [Settings docs](https://code.claude.com/docs/en/settings)

## Lab

In your working repo: (1) run `/config` and identify one setting at each
level; (2) add an `env` variable your analysis scripts need to the project
settings; (3) override it in `settings.local.json` and confirm which one a
fresh session sees (ask Claude to `echo` it).

## Knowledge check

1. A setting appears in all three files with different values — which wins?
2. Your team wants everyone's sessions to use the same data directory env var. Which file, and why that one?
3. Why does `settings.local.json` exist at all, given user settings are already personal?
