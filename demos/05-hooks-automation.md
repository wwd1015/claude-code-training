# Demo 05 — Hooks: auto-lint on edit + guard your data

**Track:** 3b (Hooks & settings) · **Time:** ~15 min live
**Pre-work:** [Hooks reference](https://code.claude.com/docs/en/hooks) · [Settings](https://code.claude.com/docs/en/settings)

## Objective
Show that hooks turn "please remember to lint / don't touch the data" into something the agent
loop *enforces automatically*. Teach the lifecycle (PreToolUse / PostToolUse), the matcher, and
exit-code-2 blocking.

## Setup (zero infra)
- Any small Python repo with `ruff` installed (`pip install ruff`).
- The two example hooks: [`examples/hooks/`](../examples/hooks/). Install them:
  ```bash
  mkdir -p .claude/hooks
  cp examples/hooks/{guard-data.sh,run-checks.sh} .claude/hooks/ && chmod +x .claude/hooks/*.sh
  # merge the "hooks" block from examples/hooks/settings.sample.json into .claude/settings.json
  ```
- Restart Claude Code (or `/hooks`) so it loads them.

## Live script
1. Show the config: `cat .claude/settings.json` — point out the `PostToolUse` and `PreToolUse`
   groups and the `Edit|Write|MultiEdit` matcher.
2. **Auto-lint:** ask Claude to "add a deliberately badly-formatted function to `util.py`."
   After it writes, the PostToolUse hook runs `ruff` — show the file came out formatted, and if
   there were lint errors, watch Claude fix them because exit 2 handed them back.
3. **Data guard:** ask Claude to "write a quick csv to `data/scratch.csv`." The PreToolUse hook
   blocks it (exit 2) and Claude reports it can't. Show the stderr message.
4. Discuss: the matcher narrows which tools fire the hook; exit code 2 is the block signal;
   `${CLAUDE_PROJECT_DIR}` resolves to repo root.

## Talking points
- Hooks make guardrails *enforced*, not hoped-for. A quant's data stays untouched by policy.
- PostToolUse + tests/lint = the agent self-corrects without you nagging.
- For slow tests, use an **async** hook so it doesn't block the loop (see hooks docs).

## Take-home exercise
Add one hook to your own repo: either auto-`pytest` on edits to `src/`, or a guard blocking
writes outside `src/`. Bring it to office hours.

## Time
15 min live + 20 min take-home.
