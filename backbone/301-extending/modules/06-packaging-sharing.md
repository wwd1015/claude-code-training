---
id: 301-06
title: "Packaging & Sharing What You Build"
duration: 25 min
objectives:
  - Share skills, commands, and hooks with your team through the project repo
  - Describe what plugins add on top of repo-level sharing
  - Use the contributed-library path to give your work a life beyond your team
---

## The repo is the distribution channel

Everything you built in this course ships by committing it:

- `.claude/skills/<name>/SKILL.md` — skills, picked up by everyone who clones
- `.claude/commands/*.md` — slash commands (CC 201)
- `settings.json` + hook scripts — guards and automation
- `.mcp.json` — team data sources (credentials via env, never committed)

A teammate clones the repo and has the whole toolkit — no install step. This
is why project scope beats personal scope for anything a second person will
use: **the repo is the training material.**

Checklist before you commit a skill for others: passes the four tests from
module 2 (known-input, trigger, fresh-session, break-it); no
machine-specific paths; secrets via environment, never in the file; one
`README` line saying what it's for.

## Plugins, briefly

For distribution *across* repos and teams, Claude Code supports **plugins** —
installable bundles of skills, commands, hooks, and MCP config, distributed
through marketplaces. Know they exist; reach for them when the same toolkit
must land in many unrelated repos. Until then, repo-level sharing is simpler
and versioned with your code.
<!-- verify: confirm current plugin/marketplace mechanism against https://code.claude.com/docs/en/skills before teaching this section -->

## The contributed library

Program-wide, the demo/skill library grows by contribution, not by central
authorship (see [CONTRIBUTING.md](../../../CONTRIBUTING.md)):

- **Seed** examples are program-maintained references — like this repo's
  `skills/` and `demos/`.
- **Contributed** entries are team-authored, author-owned, promoted from real
  work (often capstones — see CC 501). Stale entries get archived, not
  silently fixed; the author's name stays on it.

The promotion path for the skill you built in this course: prove it in your
own repo → tag it with discipline/use-case front-matter → submit per
CONTRIBUTING.md. Your LOB's champion can also fold it into your team's
edition of this curriculum (`lob/` + `/lob-overlay`).

**Reuse (official):** [Skills docs](https://code.claude.com/docs/en/skills) ·
[anthropics/skills](https://github.com/anthropics/skills)

## Lab

Take the skill you shipped in module 2's lab and make it shareable: run the
pre-commit checklist above, add the README line, and open the submission
(internal PR or CONTRIBUTING.md flow). If it's genuinely team-specific, hand
it to your champion for the LOB overlay instead — deciding *which* is the
exercise.

## Knowledge check

1. Why does committing `.claude/` content beat telling teammates to copy your config?
2. What problem do plugins solve that repo-level sharing doesn't?
3. What's the difference between a Seed and a Contributed library entry, and who fixes a stale Contributed one?
