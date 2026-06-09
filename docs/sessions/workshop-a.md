# Workshop A — Fundamentals (Tracks 0–1)

**Audience:** data scientists & quants, first real session · **Length:** 90 min · **Format:** live
**Pre-work (sent before):** [Claude Code 101](https://anthropic.skilljar.com/claude-code-101) +
[Quickstart](https://code.claude.com/docs/en/quickstart) — everyone arrives installed.

> Slide outline. Each slide = talking points + a demo/do cue + timing. Keep it hands-on:
> attendees should be typing into Claude Code by minute 20.

## Slide 1 — Why we're here (5 min)
- The pitch: a pair-researcher in your terminal that reads your whole repo and runs your code.
- Not autocomplete, not a chatbot. It edits files and executes.
- Today's promise: by the end you'll have used it on your own notebook.

## Slide 2 — The agentic loop (5 min)
- ask → plan → act → verify. You stay in the loop; it does the typing.
- Plan mode (`shift+tab`) before anything that writes. Review before it acts.
- The permission model: it asks before running/editing. You're always in control.

## Slide 3 — Confirm everyone's running (5 min)
- Quick poll: who got it installed? Unblock stragglers (point to Quickstart).
- `claude` in any repo → first prompt.

## Slide 4 — LIVE DEMO: EDA + data dictionary (20 min)
- Run [Demo 01](../../demos/01-eda-data-dictionary.md) on `data/sample.parquet`.
- Land the points: it *ran the code* for real null counts; plan mode before writing files;
  the output (`data_dictionary.md` + `profile.py`) is reusable real work.
- Show it inferred column descriptions — "review these, you're the domain expert."

## Slide 5 — HANDS-ON: your own notebook (25 min)
- Everyone opens one of their own notebooks/repos.
- Prompt: "Explain what this notebook does, then add a docstring/README."
- Facilitators float and unblock. Collect good/bad moments for office hours.

## Slide 6 — Core moves cheat sheet (10 min)
- Navigate/search a repo, explain code, edit, run, iterate.
- Basic git: branch, diff, commit — let Claude write the commit message.
- Reference: [Common workflows](https://code.claude.com/docs/en/common-workflows).

## Slide 7 — Take-home + what's next (5 min)
- Take-home: run the EDA pass on one real dataset, bring the diff to office hours.
- Next: Workshop B — make Claude Code *yours* (CLAUDE.md, slash commands, your first skill).

## Facilitator prep
- Pre-generate demo data: `cd demos/setup && pip install -r requirements.txt && python gen_sample_dataset.py`.
- Have a throwaway repo ready in case someone has nothing of their own to open.
