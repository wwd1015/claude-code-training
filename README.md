# Claude Code Training — for Data Scientists & Quants

Internal enablement program that teaches Claude Code to a **data science / quant** audience
(strong Python, stats, notebooks — not software engineers), from first install through
building skills, agents, hooks, and MCP integrations.

**Design principle:** reuse the official public Anthropic training as the backbone, and
build only a thin custom layer — quant-flavored demos, exercises, and templates. Every
module points to an official course or doc as the source of truth.

## What's here

| Path | What it is |
|------|------------|
| [`site/index.html`](site/index.html) | The **entry site** — the training portal (GitHub Pages). Open it locally or host it. |
| [`docs/curriculum.md`](docs/curriculum.md) | Full curriculum: 5 tracks, structure, build roadmap. |
| [`docs/reading-lists.md`](docs/reading-lists.md) | The official Anthropic asset map (verified links) per module. |
| [`docs/operating-model.md`](docs/operating-model.md) | How we run cohorts: cadence, office hours, metrics. |
| [`demos/`](demos/) | Facilitator-ready demo scripts (the reusable core). |
| [`templates/`](templates/) | Drop-in `CLAUDE.md` templates for research repos. |
| [`skills/`](skills/) | Starter skills learners can install today (e.g. `/eda`). |

## Start here (as a learner)

1. Install Claude Code and authenticate — [Quickstart](https://code.claude.com/docs/en/quickstart).
2. Take [Claude Code 101](https://anthropic.skilljar.com/claude-code-101) (self-paced).
3. Do your first real task: open one of your own notebooks and ask Claude Code to explain it.

Then follow the tracks on the [entry site](site/index.html).

## Viewing / hosting the entry site

The site is a single self-contained `site/index.html` (no build step, no dependencies).

- **Locally:** `open site/index.html`
- **GitHub Pages:** push to GitHub, then enable Pages → Source: **GitHub Actions**.
  The included workflow ([`.github/workflows/pages.yml`](.github/workflows/pages.yml))
  publishes the `site/` folder on every push to `main`.

## Contributing

Capstone projects (a real recurring task automated with Claude Code) become the demo bank
for the next cohort. Add yours under `demos/` and link it from the site. See
[`CLAUDE.md`](CLAUDE.md) for conventions.
