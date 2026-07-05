---
id: 301-02
title: "Skill Creation II: Design Patterns & Testing"
duration: 40 min
objectives:
  - Structure a skill as phases with hard rules so results don't drift
  - Make a skill self-contained enough to survive being shared
  - Test a skill the same way you'd test code — known input, expected output
---

## Workflow-shaped skills

The skills that hold up in daily use read like runbooks, not essays:

- **Phases in order** — "1. Inventory the inputs. 2. Validate. 3. Produce X.
  4. Report." Claude follows numbered phases far more reliably than prose.
- **Hard rules, stated as rules** — a short "never do X / always do Y" list
  ("never modify raw data files", "always report row counts before and
  after"). These are the lines that stop drift.
- **Output contracts** — show the exact table/file format the skill must
  produce. An example beats a description.
- **Escape hatches** — tell the skill what to do when inputs are missing or
  ambiguous ("ask one question, then proceed"), or it will guess.

Study the worked examples in this repo:
[`skills/eda/SKILL.md`](../../../skills/eda/SKILL.md) (phased profiling with
an output contract) and
[`skills/backtest-report/SKILL.md`](../../../skills/backtest-report/SKILL.md)
(a `/backtest-report` command with hard rules about what may not be recomputed).

## Self-contained or it breaks

A shared skill runs on machines that aren't yours. Keep every instruction the
skill needs inside SKILL.md or files in the same folder; refer to paths the
skill can discover ("look for a `data/` directory") rather than paths only you
have. If the skill depends on a tool being installed, say so at the top and
tell Claude how to check.

## Testing a skill

Treat SKILL.md like code: it isn't done until it passes.

1. **Known input → expected output.** Run the skill on a small fixture where
   you know the right answer; diff what you get.
2. **Trigger test.** Ask for the task in your natural words (not the skill's
   name) — does it load? If not, the description is missing your phrasing.
3. **Fresh-session test.** `/clear`, then run it again: skills must not rely
   on anything you said earlier in a conversation.
4. **Break it once.** Feed a missing/odd input and check the escape hatch
   fires instead of a confident wrong answer.

Iterate on the wording exactly as you would on failing code — the skill file
is the program.

## Worked example: the four patterns in one skill

This repo's [`skills/regression-diagnostics/SKILL.md`](../../../skills/regression-diagnostics/SKILL.md)
shows all four patterns doing their job. Read it alongside this dissection:

- **Phases in order.** The body is a numbered battery — Fit → Multicollinearity
  (VIF) → Heteroskedasticity (Breusch-Pagan) → Residuals (Jarque-Bera,
  Durbin-Watson) → Stationarity (ADF) → plain-English verdict. Claude runs them
  in that order every time instead of picking a favorite subset.
- **Hard rules, stated as rules.** "Use `statsmodels`. Run the tests and report
  the actual statistics + p-values — never guess." and "Read-only on the input
  file." are the lines that stop the model from hand-waving a number or
  mutating your data.
- **Output contract.** It names the artifact (`regression_report.md`) and
  itemizes exactly what each section contains, down to "flag VIF > 5 (and > 10
  as serious)." A reviewer knows what a correct run looks like before it runs.
- **Escape hatch.** "Assumes cross-sectional OLS unless the user says
  time-series/panel — ask if ambiguous." One question when the input is unclear,
  rather than silently assuming and producing a confidently wrong report.

Now put it through the four tests. **Known input:** run it on a fixture where
you already computed the VIFs by hand and diff. **Trigger:** ask "is my rates
model sound?" without naming the skill — it should load. **Fresh session:**
`/clear` and rerun; it must not depend on anything said earlier. **Break it:**
hand it a single-column file with no regressors and confirm the escape hatch
asks a question instead of crashing. When all four pass, it's shippable.

### Best practices

- **Test on real inputs before you share.** A skill that works on your toy
  fixture but breaks on a wide, null-riddled production table isn't done. Run it
  against a genuine slice of your data — the messy one — before committing it
  for teammates.
- **State hard rules as imperatives, not preferences.** "Never modify raw data
  files", "always report row counts before and after" are load-bearing. Bury
  them in prose and they drift; list them as rules and they hold.
- **Show the output contract, don't describe it.** Paste the exact table or the
  exact filename and section list the skill must produce. An example the model
  can pattern-match beats a paragraph explaining the format.
- **Give every skill an escape hatch.** Missing column, ambiguous spec, empty
  file — say what to do ("ask one question, then proceed"). Without it, the
  model guesses, and a confident wrong answer is worse than a question.
- **Push heavy reference material to a sibling file.** A long code-style guide
  or a lookup table lives in `reference.md` next to `SKILL.md`, referenced by
  path — progressive disclosure keeps the skill lean and loads the detail only
  when the workflow reaches it (CC 301 module 1).
- **Keep the skill self-contained and path-agnostic.** Discover paths ("look for
  a `data/` directory") rather than hard-coding `/Users/you/...`; a shared skill
  runs on machines that aren't yours.

### Common pitfalls

- **The skill works only because of context you gave earlier in the session.**
  It passes for you and fails for a teammate on a fresh clone. *Fix:* the
  fresh-session test — `/clear` and rerun; move anything it relied on into the
  file.
- **Hard-coded absolute paths.** `read_csv("/Users/you/data/x.parquet")` breaks
  the moment someone else runs it. *Fix:* refer to discoverable, relative
  locations the skill can find.
- **No escape hatch, so the model invents inputs.** Feed it an ambiguous spec
  and it picks one silently. *Fix:* add the "ask one question, then proceed"
  rule and re-run the break-it test.
- **Never tested on messy real data.** It handles the clean fixture and falls
  over on production nulls and mixed types. *Fix:* test on a real, ugly slice
  before you ship.

**For quants:** your hard rules tend to be statistical integrity — "report the
actual test statistic, never a guessed p-value", "state the significance level
and whether it's cross-section or time-series". **For data scientists:** they
tend to be data hygiene and scale — "never mutate the raw partition", "sample
before profiling a billion-row table", "report null rates per column".

**Reuse (official):** [Skills docs](https://code.claude.com/docs/en/skills) ·
[Intro to Agent Skills course](https://anthropic.skilljar.com/introduction-to-agent-skills)

## Lab

Finish the skill you stubbed in module 1: add phases, at least two hard
rules, and an output contract. Then run the four tests above against a small
known input. Ship it to `.claude/skills/` in one of your real repos.

**Stretch goal:** deliberately fail the break-it test first. Before you add an
escape hatch, feed the skill a malformed input (missing column, empty file) and
watch it produce a confident wrong answer. Then add the "ask one question, then
proceed" rule and rerun until it asks instead of guesses. Seeing the failure
mode once is what makes you write escape hatches for every skill afterward.

## Knowledge check

1. Name the four structural patterns of a durable skill.
2. Why must a shared skill avoid machine-specific paths?
3. Your skill works when you type its name but never triggers naturally — which test failed, and what do you fix?
4. A skill runs perfectly for you but a teammate gets a "column not found"
   error on a fresh clone of the same repo. Which of the four tests would have
   caught this, and what's the likely cause?
5. **Scenario:** Your `/eda`-style skill gives a clean profile on your 500-row
   fixture but times out and floods the session on a real 400-million-row table.
   Which best practice did you skip, and which two hard rules would you add?
