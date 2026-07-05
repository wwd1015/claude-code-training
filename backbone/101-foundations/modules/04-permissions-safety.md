---
id: 101-04
title: "The Permission & Safety Model"
duration: 30 min
objectives:
  - Explain when Claude Code asks before acting and why
  - Choose an appropriate permission mode for a given task
  - Apply your organization's data-handling rules inside sessions
  - Keep sensitive data out of a session while still getting useful help
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

## Worked example: getting help without exposing the data

You want Claude Code to help write a query that de-duplicates a customer-level
table, but the table holds PII and your policy says raw rows don't leave approved
systems. You can still get real help — you feed it *shape*, not *contents*:

> Here's the schema (columns and dtypes) and a 5-row **synthetic** sample I made
> up. Write a dedup query keyed on `account_id` that keeps the most recent
> `updated_at`, and explain the tie-breaking. Don't query the real table.

The agent works from the schema, writes the SQL, explains the window function. You
run it yourself against the real warehouse. The model saw column names and fake
rows — never protected data. Contrast the anti-pattern: pasting a real extract
into the prompt "so it has context." Once real rows are in the session, they're in
the session.

If Claude proposes running the query itself against a live connection, that's a
side-effecting command — it asks first (default mode), and that prompt is exactly
the one to read carefully before approving.

### Best practices

- **Start conservative, loosen as trust accrues.** Default mode on unfamiliar or
  high-stakes repos; step up to accept-edits only once you trust the direction.
  The reverse order — broad permissions first — is how accidents happen.
- **Read the command in the prompt, not just the verb.** Approve `pytest`, sure —
  but the prompt shows the *actual* command. "Yes, don't ask again" on a broad
  pattern is a standing grant; give it deliberately, never in a directory with
  credentials or prod configs.
- **Scope by directory.** The agent's reach is the launch directory. Keep secrets,
  `.env` files, and production configs out of the tree you run sessions in, so
  "allowed to run" can never quietly mean "allowed to run *against prod*."
- **Feed shape, not sensitive contents.** Schemas, dtypes, synthetic samples, and
  column statistics are usually enough for the agent to be useful. Point it at
  those instead of raw sensitive extracts whenever policy allows.
- **Keep plan mode in your pocket for the risky ask.** When you're unsure what a
  task will touch, plan mode shows the intended actions with zero side effects — a
  free dry run.

### Common pitfalls

- **Reflexively clicking "yes, don't ask again."** It feels efficient and quietly
  builds a broad allowlist you never reviewed. Prefer "yes once" until a command is
  genuinely routine; you'll manage the allowlist deliberately in CC 201.
- **Running bypass/auto mode in a real repo "to go faster."** Bypass
  (`claude --dangerously-skip-permissions`) belongs in throwaway sandboxes only. In
  a repo that matters, one wrong command runs with no brakes. <!-- verify: confirm the bypass flag name on your installed version -->
- **Pasting a sensitive extract for "context."** The model reads what enters the
  session. Use schema + synthetic rows; let the real query run on your side.
- **Assuming read-only is risk-free.** Reading is low-risk for *actions*, but the
  model still sees whatever it reads. A directory full of PII is a data-exposure
  question even when nothing is edited.

### For quants / For data scientists

**Quants:** your sensitive surface is often positions, P&L, and counterparty data
— keep those out of the launch tree and work from anonymized or synthetic series.
**Data scientists:** your sensitive surface is usually large PII tables in the
warehouse — the schema-plus-synthetic-sample pattern lets Claude write the
transform without ever seeing a real row.

**Reuse (official):** [Settings/permissions docs](https://code.claude.com/docs/en/settings) ·
[Security](https://code.claude.com/docs/en/security)

## Lab

In a scratch repo: run the same small refactor once in default mode and once
in accept-edits mode, and note the difference in prompts. Then try plan mode
on a bigger ask and reject the plan — confirm nothing changed.

**Stretch:** For your own real work, write down one directory you would never
launch a session in, and why (what's in it). That sentence is the start of your
team's data-handling note.

## Knowledge check

1. Which actions require approval by default, and which don't?
2. When is bypass/auto mode appropriate?
3. Approving a command "don't ask again" does what, exactly?
4. You need help writing a query against a table full of PII. How do you get the help without the data entering the session?
5. A teammate turns on bypass mode in the team's production analytics repo to "stop the prompts." What do you tell them?
