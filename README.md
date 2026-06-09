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
| [`docs/curriculum.md`](docs/curriculum.md) | Full curriculum: 5 tracks, structure, build roadmap, links to everything. |
| [`docs/reading-lists.md`](docs/reading-lists.md) | The official Anthropic asset map (verified links) per module. |
| [`docs/sessions/`](docs/sessions/) | Facilitator slide outlines: 3 workshops + capstone demo day. |
| [`docs/facilitator-guide.md`](docs/facilitator-guide.md) | Cohort runbook + comms templates. |
| [`docs/cheatsheet.md`](docs/cheatsheet.md) · [`glossary.md`](docs/glossary.md) · [`faq.md`](docs/faq.md) · [`data-handling.md`](docs/data-handling.md) | Learner reference. |
| [`docs/operating-model.md`](docs/operating-model.md) · [`metrics-template.md`](docs/metrics-template.md) · [`capstone-ideas.md`](docs/capstone-ideas.md) | Program ops, ROI tracking, project ideas. |
| [`demos/`](demos/) | 5 facilitator-ready demo scripts + [`demos/setup/`](demos/setup/) runnable seeded data generators. |
| [`examples/`](examples/) | Copy-paste [hooks](examples/hooks/) and [MCP](examples/mcp/) configs. |
| [`templates/`](templates/) | Drop-in `CLAUDE.md` template for research repos. |
| [`skills/`](skills/) | Starter skills to install today: `/eda`, `/backtest-report`, `/triage-data`. |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | How to add demos, skills, and capstones. |

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
