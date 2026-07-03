---
id: 201-01
title: "CLAUDE.md & Memory"
duration: 30 min
objectives:
  - Explain what CLAUDE.md is and when Claude Code reads it
  - Choose the right scope (user vs project) for a given instruction
  - Write and iterate on a CLAUDE.md that actually changes behavior
---

## The file Claude reads before you say anything

`CLAUDE.md` is standing instructions: a markdown file Claude Code loads at the
start of every session in that directory. Everything you find yourself
repeating — "we use pandas not polars", "run `make test` before declaring
done", "never touch `data/raw/`" — belongs there, said once.

Two scopes, one rule of thumb:

- **Project memory** — `CLAUDE.md` at the repo root (committed, shared with
  the team): conventions, key commands, layout, gotchas *of this repo*.
- **User memory** — `~/.claude/CLAUDE.md` (private, follows you everywhere):
  *your* preferences, like "explain stats notation, skip Python basics".

Claude reads both; the more specific scope wins when they disagree.

## What belongs in it (and what doesn't)

Good CLAUDE.md content is what a sharp new collaborator would need on day one:

- **Commands** — how to run tests, rebuild data, launch the notebook server.
- **Conventions** — naming, preferred libraries, style choices linters can't see.
- **Gotchas** — "the dates in `prices.parquet` are trade dates, not settlement".
- **Boundaries** — directories or files never to modify.

What doesn't belong: anything derivable from the code itself (Claude can read),
long prose, or session-specific context. Short and true beats long and stale.

A worked starting point for research repos lives in this repo:
[templates/CLAUDE.research-repo.md](../../../templates/CLAUDE.research-repo.md).

## Iterating on it

Treat CLAUDE.md as tuned, not written. When Claude does something you had to
correct, ask: "add an instruction to CLAUDE.md so this doesn't happen again"
— it will phrase the rule itself. Use `#` at the start of a message as a
shortcut to add a memory mid-session. Prune on the same trigger: instructions
that never fire are noise. <!-- verify: `#` memory shortcut against current docs -->

**Reuse (official):** [Memory docs](https://code.claude.com/docs/en/memory) ·
[Best practices](https://code.claude.com/docs/en/best-practices)

## Lab

Pick the repo or notebook folder you touched most in CC 101. Ask Claude to
draft a `CLAUDE.md` for it, starting from the research-repo template. Cut the
draft to the ten lines a new collaborator would actually need. Start a fresh
session and verify the behavior changed (e.g., it runs your test command
without being told).

## Knowledge check

1. Which scope — user or project — for "always show me effect sizes, not just p-values"? For "raw data is read-only"?
2. Name two things that do NOT belong in CLAUDE.md, and why.
3. What's the fastest way to capture a correction as a permanent instruction?
