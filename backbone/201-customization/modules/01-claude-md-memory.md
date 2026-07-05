---
id: 201-01
title: "CLAUDE.md & Memory"
duration: 40 min
objectives:
  - Explain what CLAUDE.md is and when Claude Code reads it
  - Choose the right scope (user vs project) for a given instruction
  - Write and iterate on a CLAUDE.md that actually changes behavior
  - Import shared standards into CLAUDE.md instead of copy-pasting them
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

## Memory that layers instead of duplicating

You rarely want one giant file. Three moves keep memory DRY:

- **Bootstrap, then cut.** In a repo with no CLAUDE.md, run `/init` — Claude
  reads the README, layout, and test config and drafts a first file. It is a
  fast skeleton and almost always too long; keep the ten lines a new hire
  needs and delete the rest.
- **Import shared standards.** A line like `@../shared/house-style.md` inside
  CLAUDE.md pulls that file's contents in, so a firm-wide convention lives in
  one place and every repo references it instead of copying it.
  <!-- verify: @import path syntax against current memory docs -->
- **Edit deliberately with `/memory`.** `/memory` opens your memory files in
  your editor when you want to prune or reorganize, not just append.

Subdirectory `CLAUDE.md` files also exist: a `research/alpha/CLAUDE.md` is
picked up when Claude works inside that subtree, which keeps desk-specific
rules out of the repo-root file. <!-- verify: subdirectory CLAUDE.md load behavior -->

## Worked example: a backtest repo that stops re-explaining itself

You keep telling Claude the same three things in a returns-research repo. Turn
them into memory once.

**Prompt (fresh session in the repo):** `/init`

**What happens:** Claude scans the repo and writes a CLAUDE.md describing the
package layout, the test command, and the data folders. Useful, but it has
fifteen lines of structure Claude could have read itself, and none of your real
gotchas. You cut it down and add what actually bites:

```markdown
## Commands
- Tests: `uv run pytest -q`. Run before declaring a task done.
- Rebuild features: `python -m alpha.features --asof <date>`.

## Conventions
- Returns are **log** returns unless a column says `_simple`.
- pandas, not polars. Vectorize; no row-wise `.apply` on price frames.

## Gotchas
- `prices.parquet` dates are **trade** dates, not settlement.
- Never refit a model past the embargo date in `config/embargo.yaml`.

## Boundaries
- `data/raw/` is read-only. Write derived data to `data/derived/`.
```

**How you verify:** start a fresh session and say "run the tests" — it should
use `uv run pytest -q` unprompted. Ask it to compute a Sharpe from
`prices.parquet` and check it treats the column as log returns and doesn't
touch `data/raw/`. If it slips, that's a missing or badly-worded line — fix the
line, don't just correct the turn.

### Best practices

- **Treat it like a prompt, not a wiki.** Every line competes for the model's
  attention; a bloated CLAUDE.md dilutes the rules that matter. Add a line only
  after you have seen the behavior it fixes.
- **Write imperatively and specifically.** "Run `uv run pytest -q` before
  saying a task is done" beats "we care about testing." Vague guidance produces
  vague adherence.
- **One fact, one place.** Team truths in project memory, personal taste in
  user memory. Duplicating a rule across scopes guarantees they drift.
- **Emphasize sparingly.** Reserve bold or "IMPORTANT" for the two or three
  rules that actually get violated. If everything is important, nothing is.
- **Prune on the same trigger you add.** When you delete a rule the linter or
  CI now enforces, the file gets sharper. Standing instructions that never fire
  cost context every session for no behavior change.
- **Keep it under review like code.** The project CLAUDE.md is committed —
  changes to it belong in PRs, so the team sees when the house rules move.

### Common pitfalls

**You paste your whole style guide into the project file.** It reads like
documentation, and Claude skims documentation the way you do. Fix: keep only
the rules Claude actually breaks, and `@import` the long-form guide if you need
it linked at all.

**You put a personal preference in the committed CLAUDE.md.** "Explain stats
notation to me" then lands in every teammate's session. Fix: personal register
and preferences go in `~/.claude/CLAUDE.md`.

**You write aspirations instead of facts.** "We write clean, well-tested code"
changes nothing. Fix: name the command, the path, the convention.

**You write it once and never touch it again.** The repo moves; the memory goes
stale and starts actively misleading. Fix: edit a line the moment you correct
Claude, with `#` or `/memory`.

**For quants:** your gotchas are usually economic, not mechanical — "curve is
quoted act/360", "returns are log", "don't refit past the embargo". Those are
exactly what a new collaborator gets wrong, so they earn their place in
CLAUDE.md over anything the code already states.

**For data scientists:** yours are usually about scale and pipelines — "the
feature table is 400M rows, sample before `.describe()`", "training runs go
through the scheduler, never on the login node." Encode the operational
guardrails so Claude doesn't cheerfully melt a node to answer a question.

**Reuse (official):** [Memory docs](https://code.claude.com/docs/en/memory) ·
[Best practices](https://code.claude.com/docs/en/best-practices)

## Lab

Pick the repo or notebook folder you touched most in CC 101. Ask Claude to
draft a `CLAUDE.md` for it, starting from the research-repo template. Cut the
draft to the ten lines a new collaborator would actually need. Start a fresh
session and verify the behavior changed (e.g., it runs your test command
without being told).

**Stretch:** find one convention you would repeat across several repos (a house
style, a shared data dictionary). Move it into a single file and `@import` it
from two different repos' CLAUDE.md. Change the shared file once and confirm
both repos pick up the change.

## Knowledge check

1. Which scope — user or project — for "always show me effect sizes, not just p-values"? For "raw data is read-only"?
2. Name two things that do NOT belong in CLAUDE.md, and why.
3. What's the fastest way to capture a correction as a permanent instruction?
4. Why keep CLAUDE.md short instead of documenting everything about the repo?
5. A teammate pastes their entire 200-line lab wiki into the project `CLAUDE.md` and says Claude now "ignores half of it." What do you tell them?
