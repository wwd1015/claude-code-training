---
id: 201-04
title: "Custom Slash Commands & Output Styles"
duration: 40 min
objectives:
  - Create a custom slash command from a prompt you keep retyping
  - Parameterize commands with arguments
  - Adjust how Claude communicates with output styles
  - Know when a command has outgrown itself and should become a skill
---

## Prompts you keep retyping are programs

A custom slash command is a markdown file whose body is a prompt. Drop it in
`.claude/commands/` (project, shared) or `~/.claude/commands/` (user,
personal) and its filename becomes the command:

```markdown
<!-- .claude/commands/eda.md -->
Profile the dataset at $ARGUMENTS: shape, dtypes, missingness, outliers,
and a five-line summary of what would surprise a new analyst.
Save the report as markdown next to the data file.
```

Now `/eda data/prices.parquet` runs your best prompt every time —
`$ARGUMENTS` receives whatever follows the command. Anything you've typed
twice with small variations is a candidate: a regression-diagnostics
checklist, a notebook-cleanup pass, a "summarize what changed since main".

This is the gateway to CC 301: when your command needs supporting files,
scripts, or multi-step logic, it graduates into a **skill**. Same instinct,
bigger container.

## Arguments, frontmatter, and namespaces

`$ARGUMENTS` takes everything after the command as one blob. When you need
distinct inputs, positional placeholders `$1`, `$2` split them:

```markdown
<!-- .claude/commands/compare-runs.md -->
Compare backtest run $1 against run $2. Report the change in Sharpe, max
drawdown, and turnover, and flag any metric that moved more than 10%.
```

`/compare-runs 2024Q1 2024Q2` fills each slot. <!-- verify: $1/$2 positional argument syntax against current docs -->

A YAML frontmatter block at the top of the file tunes the command — a
`description` for the `/help` listing and an `argument-hint` so the UI shows
what to pass. You can also restrict which tools the command may use. Two power
features worth knowing: a line beginning `!` runs a shell command and injects
its output into the prompt, and `@path/to/file` pulls a file's contents in — so
a command can gather live context before Claude reasons. <!-- verify: frontmatter keys, ! bash, and @file syntax against current docs -->

Subdirectories namespace commands: `.claude/commands/qa/nulls.md` becomes
`/qa:nulls`, which keeps a growing library legible.

## Output styles

Output styles change how Claude communicates — more explanation, less
narration, different formats — without touching what it can do. They're
useful when the default register is wrong for the audience: terse for
yourself, tutorial-mode when onboarding someone. The statusline is similarly
configurable if you want session state (model, cost, directory) visible at a
glance. <!-- verify: output-styles and statusline configuration against current docs -->

## Worked example: a regression-diagnostics command the desk shares

Every time a quant fits a linear model, the same review happens by hand:
residual plots, multicollinearity, stability. Encode it once so it runs
identically for everyone.

```markdown
<!-- .claude/commands/reg-diag.md -->
---
description: Standard regression-diagnostics review for a fitted model
argument-hint: <path-to-notebook-or-script>
---
Review the regression in $ARGUMENTS as if signing off for production:
1. Residuals: normality, heteroskedasticity (name the test), autocorrelation.
2. Multicollinearity: VIF per regressor; flag anything above 10.
3. Stability: coefficient signs and magnitudes vs. economic priors.
4. Leakage: any feature that could not be known at prediction time.
Return a short verdict — ship / fix / investigate — with the reasons.
```

**What happens:** `/reg-diag notebooks/rates_model.ipynb` runs the full
checklist and returns a verdict instead of a wall of plots. Because the prompt
is fixed, two quants get the *same* review, and a new hire inherits the desk's
standard without reading a wiki.

**How you verify:** run it on a model you have already reviewed by hand and
check it catches what you caught. Run it on a deliberately broken model (add a
collinear feature) and confirm it flags the VIF. When it misses something,
you fix the *command*, and everyone's next review improves.

### Best practices

- **Harvest, don't invent.** The best commands come from prompts you have
  already typed several times. Check your history; the repetition is the signal
  that it's worth encoding.
- **Make the output self-sufficient.** Write the prompt so a good run needs no
  follow-up. If you always ask "now summarize the verdict," bake the verdict
  into the command.
- **Share the ones the team should standardize on.** A review checklist or QA
  pass belongs in `.claude/commands/` in the repo so the whole desk runs the
  identical prompt. Keep personal shortcuts in `~/.claude/commands/`.
- **Add a `description` and `argument-hint`.** They cost one line each and make
  the command discoverable in `/help` and usable by someone who didn't write it.
- **Name and namespace clearly.** `/qa:nulls` reads better than `/checknulls`.
  Subdirectories keep a growing library legible.
- **Match the output style to the audience, not your mood.** Terse for your own
  fast work, explanatory when onboarding — set it deliberately rather than
  fighting the default register turn by turn.

### Common pitfalls

**You over-parameterize a command nobody else runs the same way.** Ten
placeholders and a paragraph of options is a worse experience than typing the
prompt. Fix: start with `$ARGUMENTS`, add positional slots only when a second
distinct input actually recurs.

**You keep a genuinely multi-step, file-touching workflow as a slash command.**
It gets brittle and hard to reuse. Fix: when it needs helper scripts or several
coordinated steps, promote it to a skill (CC 301).

**You put a team-standard command in your user directory.** You get the
benefit; the desk re-invents it. Fix: commit shared commands to the project
`.claude/commands/`.

**You reach for an output style to change *what* Claude can do.** Styles change
tone and format, not capability or permissions. Fix: capability lives in tools
and permissions; register lives in output styles.

**For quants:** your best commands are sign-off checklists — regression
diagnostics, cointegration checks, a "does this respect the embargo" review.
Encoding the checklist makes model review reproducible and audit-friendly.

**For data scientists:** yours are often pipeline and data-hygiene passes — a
missingness/leakage audit, a "profile this feature table" command, a
train/serve skew check. The same prompt across every dataset is worth more than
a cleverer one-off.

**Reuse (official):** [Common workflows](https://code.claude.com/docs/en/common-workflows) ·
[Best practices](https://code.claude.com/docs/en/best-practices)

## Lab

Find the prompt you've retyped most this month (check your history). Turn it
into a project slash command with one `$ARGUMENTS` slot. Run it on two
different targets and refine the wording until both outputs are right without
follow-up instructions.

**Stretch:** add a `description` and `argument-hint` in frontmatter, then give
the command a second positional argument (`$1`/`$2`) so it takes two distinct
inputs — for example a "compare these two runs/datasets" command. Confirm both
slots fill correctly, and decide honestly whether it is still a command or has
become a skill.

## Knowledge check

1. Where does a slash command live if the whole team should get it on clone?
2. What does `$ARGUMENTS` do, and how do `$1`/`$2` differ from it?
3. What's the signal that a slash command should graduate into a skill?
4. What do output styles change, and what do they *not* change?
5. A teammate has a 60-line command that shells out to three scripts and writes files, and complains it's flaky. What do you tell them?
