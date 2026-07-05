# CLAUDE.md — Claude Code Training repo

## What this repo is
A training curriculum (content, not an app) that teaches Claude Code to internal data
scientists & quants. The canonical curriculum is the **backbone**: five versioned courses
(CC 101–501) under `backbone/`, delivered through one entry site. Everything else —
demos, starter skills, reference docs, facilitator kit — is the supporting layer.

## Audience framing
Readers are strong in Python/stats/notebooks but may be light on git, terminal habits, and
the agentic mental model. Bridge those gaps explicitly. Never assume software-engineering
background. Examples must be quant-native (EDA, research notebooks, backtests, data QA,
SQL/warehouse) — never to-do apps or CRUD. Controlled vocabulary (DSQ, Quant vs Data
Scientist, Learner, Champion, Capstone…) is defined in `CONTEXT.md` — use it.

## Core principle: reuse official material
Every module names an official Anthropic course/doc as the source of truth (see
`docs/reading-lists.md`). We author only the delta: quant-native worked examples, best
practices and pitfalls, labs on the learner's own work, and templates. When adding a
module, find the official asset first.

## The backbone (canonical curriculum)
`backbone/` holds the versioned course catalog — per course: `course.yaml` (metadata +
version), `modules/NN-slug.md` (canonical content), `sources.yaml` (provenance),
`CHANGELOG.md`, and `generated/` (rendered HTML — **never hand-edit**). Versions are
mirrored in `backbone/MANIFEST.yaml`. Operate it with the project skills
`/backbone-sync` (ingest, rebuild, publish) and `/lob-overlay` (team editions).
Design doc: `BACKBONE.md`. How-to by role: `docs/backbone-user-guide.md`.

**Module anatomy** (keep this shape when editing content): YAML front-matter
(`id`, `title`, `duration`, `objectives`) → body sections including a worked example,
`### Best practices`, and `### Common pitfalls` → a `**Reuse (official):**` links line →
`## Lab` (always on the learner's own work) → `## Knowledge check` (4–5 questions).
Content depth lives in the modules, not the templates.

**The edit loop** (what "continue working on the curriculum" means):
1. Edit `backbone/<course>/modules/*.md` (or ingest new material via `intake/` +
   `/backbone-sync`).
2. Bump `version` in that course's `course.yaml` **and** mirror it in
   `backbone/MANIFEST.yaml` (PATCH = fixes, MINOR = new info/module, MAJOR = restructure —
   breaks LOB anchors). Add a `CHANGELOG.md` entry; record provenance in `sources.yaml`.
3. Regenerate `generated/` from `templates/formats/` per
   `templates/formats/TEMPLATE-CONTRACT.md`.
4. Republish: copy each regenerated file to `site/courses/` (`101.html`,
   `301-deck.html`, …). `/backbone-sync` does steps 2–4 for you.

## The one-site rule
All self-paced courses are accessed through the entry site: `site/index.html` links
`site/courses/<id>.html`, which are byte-identical published copies of
`backbone/*/generated/*.html`. GitHub Pages publishes the `site/` folder only
(`.github/workflows/pages.yml`), and `open site/index.html` must work locally — so
course pages live *inside* `site/`. Both `generated/` and `site/courses/` are build
artifacts: fix modules or templates, then regenerate and republish; never hand-edit
either. LOB editions (`lob/<team>/generated/`) are never published to the central site.

## Source-material layer
`docs/curriculum.md` (track-based, Tracks 0–4) is **source material**, not the curriculum —
tracks map to courses (T0+1→101, T2→201, T3→301+401, T4→501). Don't extend the
track docs; route new content into backbone modules. Learner-facing material (entry site,
README, session outlines) speaks in course codes (CC 101…), not track numbers.

## Conventions
- The entry site is a single self-contained `site/index.html` — no build step, no external
  assets, inline CSS. Keep it that way so it works on GitHub Pages and via `open`. Same
  rule for every generated course page (the templates already comply).
- Demo scripts live in `demos/NN-name.md` and follow the template at the top of
  `demos/01-eda-data-dictionary.md`: Objective / Setup / Live script / Talking points /
  Take-home / Time. Index in `demos/INDEX.md`.
- Starter skills live in `skills/<name>/SKILL.md` (see `skills/README.md`); the two
  operating skills live in `.claude/skills/`.
- Data is never committed (see `.gitignore`). Demos default to local files/parquet so they
  run with zero infra (generators in `demos/setup/`).
- Keep official links current — they live in `docs/reading-lists.md`. Docs are hosted at
  `code.claude.com/docs/en/...`; courses at `anthropic.skilljar.com/...`. Facts about
  Claude Code stated from memory (not from a source) are marked `<!-- verify -->` in
  modules — resolve these when you can confirm them.

## Voice
Direct, concrete, builder-not-consultant. Name the command, the file, the course.
