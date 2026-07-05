---
id: 101-03
title: "Your First Real Session: Explore, Plan, Edit, Run"
duration: 45 min
objectives:
  - Use Claude Code to navigate and explain an unfamiliar repo
  - Use plan mode to review an approach before any file changes
  - Complete an edit → run → verify cycle end to end
  - Write instructions with a built-in acceptance check so the agent can correct itself
---

## Explore before you change

Agents are excellent at building maps. Openers that work on any repo:

- "Give me a tour of this repo — what are the entry points and the data flow?"
- "Where is <metric/model/report> computed? Walk me through it."
- "What would break if I changed <function>? Find the callers."

Ask follow-ups; it's a conversation, not a query language. Reference files
naturally ("the loader in `data/io.py`") — or use `@` to attach a file path
precisely.

## Plan mode: look before it leaps

For anything non-trivial, use **plan mode** (Shift+Tab cycles modes): Claude
researches and proposes a plan but changes nothing until you approve. This is
the single best habit for building trust early — you see the intended edits
as a reviewable plan, not as a surprise diff.

## The edit → run → verify cycle

Effective instructions share three parts (remember your lab from module 1):

1. **Goal** — "add a docstring and type hints to every function in `analysis.py`"
2. **Constraints** — "don't change behavior; keep the existing naming style"
3. **Verification** — "run the tests / rerun the script and confirm identical output"

Always give the third part. An agent that knows how to check its work will
check its work; one that doesn't will declare victory.

## Iterating

- Interrupt any time (`Esc`) to redirect; you don't have to let a wrong plan finish.
- "Show me what you changed" → it summarizes the diff.
- Wrong direction? Ask it to revert: git checkpoints (module 2) make this cheap.

## Worked example: a full cycle on a messy notebook

You've inherited `signal_backtest.ipynb` — 400 cells, no functions, and you need
to reuse its Sharpe calculation elsewhere. Run the whole loop:

1. **Explore.** "Give me a tour of `signal_backtest.ipynb` — what does it compute,
   and where is the Sharpe ratio calculated?" It reads the notebook and points
   you at the three cells that matter.
2. **Plan (plan mode).** Shift+Tab into plan mode: "Extract the Sharpe calculation
   into a `metrics.py` function with type hints and a docstring, and have the
   notebook import it. Don't change any numbers." It returns a plan — which cells
   it will touch, the function signature, that it leaves the notebook's outputs
   intact. You read it before a single file changes.
3. **Act.** Approve. It writes `metrics.py`, edits the notebook to import it, and stops.
4. **Run + verify.** Because you asked it not to change numbers, give it the check:
   "Re-run the notebook and confirm the Sharpe value in cell 212 is identical to
   before — 1.83." It executes `jupyter nbconvert --execute` (or runs the cell)
   and compares. If it drifted to 1.79, it investigates *before* telling you it's done.

The verification sentence is what separates this from a hopeful refactor. Without
"confirm 1.83," the agent has no way to know it broke something — and neither do
you until it's in production.

### Best practices

- **Explore before you edit — always.** The official pattern is *explore → plan →
  code → verify*. Jumping straight to "refactor this" on an unfamiliar file is how
  agents make confident, wrong changes. Spend the first prompt building a map.
- **Use plan mode for anything you'd want to review as a diff.** Plan mode
  (Shift+Tab) turns "surprise me" into "here's what I intend" — the highest-leverage
  trust-building habit in the course. Reject freely; a rejected plan changes nothing.
- **Always supply the third part: verification.** Goal + constraints + *how to
  check*. "Run the tests," "rerun the script and diff the output," "confirm the
  row count is unchanged." An agent given a check will use it; one without will
  declare victory.
- **Course-correct early — press `Esc`.** The moment a plan or an edit heads
  somewhere wrong, interrupt and redirect. Letting a bad path run to completion
  and then fixing it costs more than steering at step two.
- **Checkpoint with git so edits are reversible.** Commit before a big change;
  then "show me what you changed" and, if needed, revert cost you nothing. Fearless
  editing is a git habit, not a bravery habit.
- **Keep the ask to one job.** "Add type hints" and "also fix the timezone bug"
  and "rename the columns" in one breath produces a tangled diff you can't review.
  Split them; run the loop three times.

### Common pitfalls

- **Approving a plan you skimmed.** Plan mode only helps if you actually read the
  plan. The failure mode is treating the approval prompt as a speed bump. Read
  which files it names and what it says it won't touch.
- **Omitting the acceptance check, then blaming the model.** "It broke my numbers"
  almost always means the instruction never said which number to preserve. Name
  the value, the test, or the expected output.
- **Letting one session sprawl across three unrelated tasks.** Context from the
  refactor bleeds into the plotting task and confuses both. New task, `/clear`
  (module 5).
- **Refactoring a notebook without a way to re-run it.** If the notebook can't be
  executed headless (missing data, secrets), the agent can't verify identical
  output — decide up front how "unchanged" will be checked.

### For quants / For data scientists

**Quants:** "don't change the numbers" is your most important constraint —
econometric code refactors easily into subtly different results (a shifted lag, a
changed `ddof`). Pin the check to a known value. **Data scientists:** for large
pipelines, explore to scope before editing ("which modules import this feature?")
so a rename doesn't silently break three downstream jobs.

**Reuse (official):** [Common workflows](https://code.claude.com/docs/en/common-workflows) ·
[Claude Code in Action](https://anthropic.skilljar.com/claude-code-in-action)

## Lab

On one of your own notebooks or scripts: (1) ask for a tour of what it does;
(2) in plan mode, request a cleanup (docstrings, dead-code removal, or
extracting a function) and read the plan critically before approving;
(3) have it run the result and confirm the output is unchanged. Time yourself
against doing it by hand.

**Stretch:** Do the same loop once *without* the verification sentence, and watch
how the agent reports "done." Then add the check back and compare. The contrast is
the lesson — keep it for module 5's capstone.

## Knowledge check

1. What does plan mode change about the agentic loop?
2. What are the three parts of an effective instruction?
3. You approved a change and regret it — what are two ways to recover?
4. A teammate refactored a backtest with Claude and the Sharpe changed from 1.83 to 1.79. What one habit would have caught it, and when?
5. When would you press `Esc` mid-task instead of waiting to see the final result?
