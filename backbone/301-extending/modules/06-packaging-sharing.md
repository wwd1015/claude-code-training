---
id: 301-06
title: "Packaging & Sharing What You Build"
duration: 35 min
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

## Worked example: promoting a skill from "mine" to "ours"

You built `/regression-diagnostics` in module 2 and it's been earning its keep
in your own repo for a week. Here's the full path from personal tool to a
Contributed library entry the rates desk can rely on.

1. **Re-run the four tests on a clean clone.** Fresh-session and known-input are
   the ones that catch "works on my machine" — a skill that quietly depended on
   something in your history fails here, before a teammate ever sees it.
2. **Strip machine-specifics.** Grep the folder for absolute paths and personal
   filenames; replace them with discoverable, relative references. Confirm no
   credential or internal hostname is baked in.
3. **Add the one-line README and the discipline tags.** Say what it's for in a
   sentence, and tag it (`discipline: quant`, `use-case: model-validation`) so
   the library is searchable. This is the front-matter the promotion path
   expects.
4. **Decide the destination — and this decision *is* the exercise.** If it's
   broadly useful, open the submission per
   [CONTRIBUTING.md](../../../CONTRIBUTING.md) as a **Contributed** entry that
   keeps your name on it. If it encodes something only your desk does (a
   team-specific model spec, an internal data convention), hand it to your
   Champion for the **LOB overlay** instead — same skill, narrower home.
5. **Commit the whole toolkit, not just the skill.** If the skill leans on a
   guard hook or an `.mcp.json`, commit those too, so a clone reproduces the
   behavior with no setup.

### Best practices

- **Ship by committing to the project repo, not by sending config around.**
  `.claude/` content travels with a `git clone` — the repo *is* the install
  step. Telling teammates to copy files by hand guarantees drift.
- **Prefer project scope for anything a second person uses.** `~/.claude/`
  helps only you; `.claude/` in the repo helps everyone who clones and stays
  versioned with the code that depends on it.
- **Never commit a secret; use env expansion for `.mcp.json`.** Credentials go
  in the environment (`${VAR}`), never in a checked-in file — a leaked token in
  git history outlives the PR that added it (CC 301 module 4).
- **Gate every shared skill on the four tests plus a clean-clone check.** The
  bar for "runs in your session" is lower than "runs on a teammate's fresh
  clone." Clear the higher bar before you commit it for others.
- **Tag Contributed work with discipline and use-case.** The library grows by
  contribution; tags are what make it navigable and what let a Champion find the
  right example for a Cohort.
- **Reach for plugins only when the same toolkit must land in many unrelated
  repos.** Within one repo or team, repo-level sharing is simpler and versioned
  with your code; plugins earn their complexity across repo boundaries.

### Common pitfalls

- **"It works for me" — shipped straight from your session.** It relied on
  context or a local path a teammate doesn't have. *Fix:* clone fresh, `/clear`,
  and run the four tests before committing.
- **Personal scope for a team skill.** You put it in `~/.claude/skills/`, so
  nobody who clones the repo gets it. *Fix:* move it to `.claude/skills/` and
  commit.
- **A stale Contributed skill silently "fixed" by central.** That breaks the
  ownership model. *Fix:* stale Contributed entries are archived, not rewritten;
  the author's name stays on it (see [CONTEXT.md](../../../CONTEXT.md)).
- **Reaching for a plugin/marketplace when one committed folder would do.**
  Extra machinery for a single team. *Fix:* start with repo-level sharing; graduate
  to plugins only when the cross-repo need is real.

**For quants:** your Contributed entries are often model-validation batteries
and econometric conventions specific to a desk — frequently the right fit for
the LOB overlay rather than the general library. **For data scientists:**
they're more often reusable EDA/triage passes and feature-QA skills that
generalize across teams — good candidates for the shared Contributed library.

**Reuse (official):** [Skills docs](https://code.claude.com/docs/en/skills) ·
[anthropics/skills](https://github.com/anthropics/skills)

## Lab

Take the skill you shipped in module 2's lab and make it shareable: run the
pre-commit checklist above, add the README line, and open the submission
(internal PR or CONTRIBUTING.md flow). If it's genuinely team-specific, hand
it to your champion for the LOB overlay instead — deciding *which* is the
exercise.

**Stretch goal:** clone your repo into a fresh directory (or ask a teammate to)
and run the skill there with no other setup. Whatever breaks — a missing path, a
credential it assumed, context it relied on — is your real pre-commit checklist,
not the idealized one. Fix each break at the source and re-clone until it runs
clean from zero. That clean-clone run is the actual bar for "shareable."

## Knowledge check

1. Why does committing `.claude/` content beat telling teammates to copy your config?
2. What problem do plugins solve that repo-level sharing doesn't?
3. What's the difference between a Seed and a Contributed library entry, and who fixes a stale Contributed one?
4. You're about to commit `.mcp.json` so the team inherits a warehouse
   connection. What must you check first, and how do you share the credential?
5. **Scenario:** You built a skill that encodes your desk's proprietary curve-
   fitting convention. Does it go to the general Contributed library or the LOB
   overlay, and why does that choice matter for who maintains it later?
