# Claude Code Training — for Data Scientists & Quants

Internal enablement program that teaches Claude Code to a **data science / quant** audience
(strong Python, stats, notebooks — not software engineers), from first install through
building skills, agents, hooks, and MCP integrations.

**Design principle:** reuse the official public Anthropic training as the backbone, and
build only a thin custom layer — quant-flavored demos, exercises, and templates. Every
module points to an official course or doc as the source of truth.

## The backbone system

The curriculum is maintained as five numbered **backbone courses** (CC 101 → CC 501)
in [`backbone/`](backbone/) — a centralized, versioned single source of truth with
three delivery formats (self-paced site, instructor decks, capstone working groups)
and per-team **LOB editions** layered on top. Two skills operate it:

- **`/backbone-sync`** — drop source material into [`intake/`](intake/), and it
  classifies, diffs, merges (with provenance), versions, and regenerates course outputs.
- **`/lob-overlay`** — lets a team champion layer their own demos/use cases onto the
  backbone and re-sync when the central version advances.

**How to use it:** [`docs/backbone-user-guide.md`](docs/backbone-user-guide.md) —
role-based walkthroughs for learners, instructors, LOB champions, and maintainers.
**How it's designed:** [`BACKBONE.md`](BACKBONE.md).

## What's here

| Path | What it is |
|------|------------|
| [`BACKBONE.md`](BACKBONE.md) · [`backbone/`](backbone/) | The versioned course catalog CC 101–501: canonical modules + generated outputs. |
| [`docs/backbone-user-guide.md`](docs/backbone-user-guide.md) | **User guide** — how to take, teach, customize, and maintain the courses, by role. |
| [`templates/formats/`](templates/formats/) | HTML templates (self-paced + deck) and the [template contract](templates/formats/TEMPLATE-CONTRACT.md). |
| [`intake/`](intake/) | Drop folder for new source material → `/backbone-sync`. |
| [`lob/`](lob/) | Line-of-business editions (backbone + team overlays) → `/lob-overlay`. |
| [`.claude/skills/`](.claude/skills/) | The two operating skills: `backbone-sync`, `lob-overlay`. |
| [`site/index.html`](site/index.html) | The **entry site** — the single access point for all courses (locally and on GitHub Pages). |
| [`site/courses/`](site/courses/) | Published copies of the generated course pages (build artifacts — never hand-edit). |
| [`docs/curriculum.md`](docs/curriculum.md) | Full curriculum: 5 tracks, structure, build roadmap, links to everything. |
| [`docs/reading-lists.md`](docs/reading-lists.md) | The official Anthropic asset map (verified links) per module. |
| [`docs/sessions/`](docs/sessions/) | Facilitator slide outlines: 3 workshops + capstone demo day. |
| [`docs/facilitator-guide.md`](docs/facilitator-guide.md) | Cohort runbook + comms templates. |
| [`docs/cheatsheet.md`](docs/cheatsheet.md) · [`glossary.md`](docs/glossary.md) · [`faq.md`](docs/faq.md) · [`data-handling.md`](docs/data-handling.md) | Learner reference. |
| [`docs/operating-model.md`](docs/operating-model.md) · [`metrics-template.md`](docs/metrics-template.md) · [`capstone-ideas.md`](docs/capstone-ideas.md) | Program ops, ROI tracking, project ideas. |
| [`demos/`](demos/) | 6 facilitator-ready demo scripts + [`demos/setup/`](demos/setup/) runnable seeded data generators. |
| [`examples/`](examples/) | Copy-paste [hooks](examples/hooks/) and [MCP](examples/mcp/) configs. |
| [`templates/`](templates/) | Drop-in `CLAUDE.md` template for research repos. |
| [`skills/`](skills/) | Starter skills to install today: `/eda`, `/backtest-report`, `/regression-diagnostics`, `/triage-data` ([guide](skills/README.md)). |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | How to add demos, skills, and capstones. |

## Start here (as a learner)

1. Open the [entry site](site/index.html) (`open site/index.html`, or the hosted
   GitHub Pages URL) — every course is one click away.
2. Install Claude Code and authenticate — [Quickstart](https://code.claude.com/docs/en/quickstart).
3. Take [CC 101 — Foundations](site/courses/101.html), then follow the catalog
   101 → 201 → 301 → 401 → 501.

## Viewing / hosting the site

The entry site plus all course pages are self-contained HTML under `site/`
(no build step, no dependencies).

- **Locally:** `open site/index.html`
- **GitHub Pages:** push to GitHub, then enable Pages → Source: **GitHub Actions**.
  The included workflow ([`.github/workflows/pages.yml`](.github/workflows/pages.yml))
  publishes the `site/` folder on every push to `main`.
- The course pages in `site/courses/` are published copies of
  `backbone/*/generated/*.html`, refreshed by `/backbone-sync` — edit modules,
  not these files.

## Contributing

Capstone projects (a real recurring task automated with Claude Code) become the demo bank
for the next cohort. Add yours under `demos/` and link it from the site. See
[`CLAUDE.md`](CLAUDE.md) for conventions.
