# CLAUDE.md — Claude Code Training repo

## What this repo is
A training curriculum (content, not an app) that teaches Claude Code to internal data
scientists & quants. The deliverables are: an entry website, curriculum docs, reading
lists mapped to official Anthropic material, demo scripts, templates, and starter skills.

## Audience framing
Readers are strong in Python/stats/notebooks but may be light on git, terminal habits, and
the agentic mental model. Bridge those gaps explicitly. Never assume software-engineering
background. Examples must be quant-native (EDA, research notebooks, backtests, data QA,
SQL/warehouse) — never to-do apps or CRUD.

## Core principle: reuse official material
Every module names an official Anthropic course/doc as the source of truth (see
`docs/reading-lists.md`). We author only the thin delta: a quant demo + a take-home
exercise + templates. When adding a module, find the official asset first.

## The backbone layer
`backbone/` holds the versioned course catalog (CC 101–501) — canonical modules per
course, provenance in `sources.yaml`, rendered outputs in `generated/` (never hand-edit;
regenerate via templates in `templates/formats/`). Operate it with the project skills
`/backbone-sync` (ingest + rebuild) and `/lob-overlay` (team editions). Design doc:
`BACKBONE.md`. Track-based docs in `docs/curriculum.md` remain as source material.

## Conventions
- The entry site is a single self-contained `site/index.html` — no build step, no external
  assets, inline CSS. Keep it that way so it works on GitHub Pages and via `open`.
- Demo scripts live in `demos/NN-name.md` and follow the template at the top of
  `demos/01-eda-data-dictionary.md`: Objective / Setup / Live script / Talking points /
  Take-home / Time.
- Data is never committed (see `.gitignore`). Demos default to local files/parquet so they
  run with zero infra.
- Keep official links current — they live in `docs/reading-lists.md`. Docs are hosted at
  `code.claude.com/docs/en/...`; courses at `anthropic.skilljar.com/...`.

## Voice
Direct, concrete, builder-not-consultant. Name the command, the file, the course.
