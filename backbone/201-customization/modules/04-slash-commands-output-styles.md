---
id: 201-04
title: "Custom Slash Commands & Output Styles"
duration: 30 min
objectives:
  - Create a custom slash command from a prompt you keep retyping
  - Parameterize commands with arguments
  - Adjust how Claude communicates with output styles
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

## Output styles

Output styles change how Claude communicates — more explanation, less
narration, different formats — without touching what it can do. They're
useful when the default register is wrong for the audience: terse for
yourself, tutorial-mode when onboarding someone. The statusline is similarly
configurable if you want session state (model, cost, directory) visible at a
glance. <!-- verify: output-styles and statusline configuration against current docs -->

**Reuse (official):** [Common workflows](https://code.claude.com/docs/en/common-workflows) ·
[Best practices](https://code.claude.com/docs/en/best-practices)

## Lab

Find the prompt you've retyped most this month (check your history). Turn it
into a project slash command with one `$ARGUMENTS` slot. Run it on two
different targets and refine the wording until both outputs are right without
follow-up instructions.

## Knowledge check

1. Where does a slash command live if the whole team should get it on clone?
2. What does `$ARGUMENTS` do?
3. What's the signal that a slash command should graduate into a skill?
