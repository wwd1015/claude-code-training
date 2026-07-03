---
id: 101-04
title: "The Permission & Safety Model"
duration: 20 min
objectives:
  - Explain when Claude Code asks before acting and why
  - Choose an appropriate permission mode for a given task
  - Apply your organization's data-handling rules inside sessions
---

## Asking before acting

By default, Claude Code asks before doing anything with side effects: editing
files, running most shell commands, fetching from the web. Reading files and
searching the repo generally don't require approval. Each prompt offers
"yes once" / "yes, don't ask again for this" — approvals accumulate into an
allowlist you'll manage deliberately in CC 201.

## Permission modes

Cycle modes with Shift+Tab; pick per task, not per personality:

| Mode | Behavior | Use when |
|---|---|---|
| default | asks for anything with side effects | unfamiliar repo, high-stakes files |
| plan | research only, proposes a plan, changes nothing | design/review before acting |
| accept edits | file edits auto-approved; commands still ask | you trust the direction, tight loop |
| bypass / auto | no prompts | sandboxes and throwaway dirs only |

The habit that scales: **start conservative, loosen as trust accrues** — the
reverse is how accidents happen.

## Data handling

The permission model governs *actions*; you still govern *data*. Two rules
that apply everywhere:

- Know your organization's policy on what data may enter a session (the model
  sees file contents it reads). Point Claude at schemas and samples rather
  than full sensitive extracts when policy requires.
- Anything the agent is allowed to run, it may run — don't grant blanket shell
  approval in a directory containing credentials or production configs.

Your org's specific policy belongs in your team's LOB edition of this course.
<!-- verify: link the central data-handling policy here via intake when available -->

**Reuse (official):** [Settings/permissions docs](https://code.claude.com/docs/en/settings) ·
[Security](https://code.claude.com/docs/en/security)

## Lab

In a scratch repo: run the same small refactor once in default mode and once
in accept-edits mode, and note the difference in prompts. Then try plan mode
on a bigger ask and reject the plan — confirm nothing changed.

## Knowledge check

1. Which actions require approval by default, and which don't?
2. When is bypass/auto mode appropriate?
3. Approving a command "don't ask again" does what, exactly?
