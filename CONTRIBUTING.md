# Contributing

The Demo library grows from real work: a DSQ automates a recurring task (a Capstone) and the
good ones become **Contributed demos** for their department's niche. Seed demos (`demos/01–05`)
are program-maintained references; Contributed demos are owned by their author/department.

## Governance — how a contribution gets in

Two-tier, deliberately low bar (easy to contribute, but the library stays trustworthy):

1. **Champion vets locally and sponsors the PR.** A four-point checklist, not a code review:
   - it automates a **real recurring task**,
   - it **runs end-to-end** on seeded/sanitized data,
   - it has the **front-matter tags** (`track`, `discipline`, `department`, `use_case`, `kind: contributed`),
   - **no internal data or secrets** are committed.
2. **A central maintainer does a light merge review** — tags present, links resolve, no secrets.
   Not a quality audit. Merge fast.

**Ownership:** Contributed demos are stamped with author + department and owned by them. Central
won't polish or maintain them. **Rough and niche is fine** — the tags tell others if it's
relevant. A Contributed demo that goes stale is **archived, not fixed**.

## Add your capstone (most common)
1. Fork / branch.
2. Add a short writeup under `demos/` (follow the format in
   [`demos/01-eda-data-dictionary.md`](demos/01-eda-data-dictionary.md)): Objective · Setup ·
   Live script · Talking points · Take-home · Time.
3. If it's a skill, add the `SKILL.md` (and any scripts) under `skills/<name>/`.
4. Open a PR. Use the capstone issue template if you want feedback first.

## Add or update a demo
- Quant-native examples only (EDA, backtests, data QA, SQL/warehouse) — never to-do apps.
- Zero-infra by default: add a seeded generator to `demos/setup/` so it runs on a laptop.
- Never commit data (`.gitignore` excludes `*.parquet`, `*.csv`, `data/`).

## Add a skill
- One folder per skill: `skills/<name>/SKILL.md`.
- Write a sharp `description:` in the frontmatter — that's what makes Claude auto-trigger it.
- Keep it read-only on inputs unless the task truly needs to write.

## Keep links current
- Official docs live at `code.claude.com/docs/en/...`; courses at `anthropic.skilljar.com/...`.
- If you touch a course/doc link, update [`docs/reading-lists.md`](docs/reading-lists.md) too.

## Style
See [`CLAUDE.md`](CLAUDE.md): direct, concrete, builder-not-consultant. Name the command, the
file, the course. No to-do-app examples.

## The entry site
`site/index.html` is a single self-contained file (no build step). Keep it that way. Deep links
in the site point to GitHub blob URLs because Pages publishes only `site/`.
