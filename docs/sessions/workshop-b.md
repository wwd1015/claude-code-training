# Workshop B — Configuration + first builds (Track 2, 3a, 3b)

**Length:** 90 min · **Format:** live
**Pre-work:** [Memory](https://code.claude.com/docs/en/memory) +
[Introduction to Agent Skills](https://anthropic.skilljar.com/introduction-to-agent-skills).

## Slide 1 — Recap + today's goal (5 min)
- You can drive it. Now make it *yours* and teach it your repeated tasks.
- By the end: a `CLAUDE.md`, a slash command, and your first skill.

## Slide 2 — CLAUDE.md: project memory (10 min)
- What it is, why it matters: persistent context so you stop re-explaining your repo.
- Walk the [research-repo template](../../templates/CLAUDE.research-repo.md).
- DO: each attendee drafts a CLAUDE.md for one of their repos (5 min, live).

## Slide 3 — Settings & permissions (10 min)
- User vs project settings; allowlists to cut approval prompts; output styles.
- Reference: [Settings](https://code.claude.com/docs/en/settings),
  [Best practices](https://code.claude.com/docs/en/best-practices).

## Slide 4 — Slash commands (10 min)
- A slash command is the prompt you stopped retyping.
- Build `/eda` together; show the [eda skill](../../skills/eda/SKILL.md) as the reference.

## Slide 5 — LIVE DEMO: author a skill (20 min)
- Run [Demo 02](../../demos/02-backtest-report-skill.md): build `/backtest-report` live.
- Land it: the `description:` frontmatter is what makes it auto-trigger — write it well.
- Skill vs slash command vs subagent: when to reach for each.

## Slide 6 — Hooks (15 min)
- Lifecycle (PreToolUse/PostToolUse/Stop). Auto-run pytest/ruff after edits; guard writes.
- DEMO: add a PostToolUse hook that runs `ruff` after edits. Reference: [Hooks](https://code.claude.com/docs/en/hooks).

## Slide 7 — Hands-on + take-home (15 min)
- Hands-on: finish your CLAUDE.md + one personal slash command.
- Take-home: author one skill for a task you do weekly; ship it to the shared repo.

## Facilitator prep
- `cd demos/setup && python gen_backtest_results.py`.
- Have the `skills/eda` and `skills/backtest-report` folders open to show real SKILL.md files.
