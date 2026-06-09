# CLAUDE.md — <research repo name>

> Drop-in template for a data-science / quant research repo. Copy to your repo root as
> `CLAUDE.md`, fill the angle-bracket bits, delete what doesn't apply. This is the project
> memory Claude Code reads on every session.

## What this repo is
<One paragraph: the research question / strategy / model this repo serves.>

## Environment
- Python <3.x>, env via <uv | conda | venv>. Activate: `<command>`.
- Key libs: <pandas/polars, numpy, scikit-learn, statsmodels, ...>.
- Run tests: `<pytest -q>`. Lint/format: `<ruff check . && ruff format .>`.
- Notebooks: <jupyter | marimo>; keep heavy notebooks out of git (see `.gitignore`).

## Data
- Source: <warehouse table / vendor / local extract>. **Never commit data.**
- Local cache: `<data/>`. Schema / data dictionary: `<docs/data_dictionary.md>`.
- Sensitive columns: <list any PII / restricted fields Claude must not echo or log>.

## Conventions
- Research notebooks live in `<notebooks/>`; reusable code in `<src/>`. Promote code out of
  notebooks once it's used twice.
- Every analysis must be reproducible: a script + a fixed seed, not just a notebook.
- Prefer `<polars | pandas>`; vectorize, no Python loops over rows.

## How to help me
- When I ask for an analysis, write a reusable script (not just inline), add a quick test, and
  show me the numbers you actually computed.
- Use plan mode for anything that writes more than one file.
- Don't refactor unrelated code. Don't change data files.

## Guardrails
- Read-only on `<data/>` and any DB connection unless I say otherwise.
- Never print or commit values from the sensitive columns above.
