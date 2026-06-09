# Hooks examples

Runnable hooks for a research repo. Hooks fire automatically at lifecycle points — here, after
and before edits. Official schema: [Hooks reference](https://code.claude.com/docs/en/hooks).

## What's here
| File | Event | Does |
|------|-------|------|
| `guard-data.sh` | **PreToolUse** (Edit/Write) | Blocks any write to a `data/` path (exit 2 = block). Keeps the agent off your datasets. |
| `run-checks.sh` | **PostToolUse** (Edit/Write) | Runs `ruff format` + `ruff check --fix` after edits; exit 2 surfaces lint errors back to Claude to fix. |
| `settings.sample.json` | — | The `hooks` config block to drop into settings.json. |

## Install
```bash
# from your repo root
mkdir -p .claude/hooks
cp path/to/examples/hooks/guard-data.sh .claude/hooks/
cp path/to/examples/hooks/run-checks.sh .claude/hooks/
chmod +x .claude/hooks/*.sh
# then merge the "hooks" block from settings.sample.json into .claude/settings.json
```
Restart Claude Code (or run `/hooks`) so it picks up the config.

## How it works (the loop)
1. You ask Claude to edit a file.
2. **PreToolUse** fires → `guard-data.sh` checks the target path. If it's under `data/`, exit 2
   blocks the edit and tells Claude why.
3. The edit runs.
4. **PostToolUse** fires → `run-checks.sh` formats + lints. If lint fails, exit 2 hands the
   errors back to Claude, which fixes them — no manual nagging.

## Notes
- `${CLAUDE_PROJECT_DIR}` resolves to your repo root.
- The matcher `Edit|Write|MultiEdit` is an exact tool-name list (not regex).
- For an async version that runs slow tests without blocking, see the "run tests after file
  changes" example in the [hooks docs](https://code.claude.com/docs/en/hooks).
- Verify behavior with a throwaway file before trusting a guard hook on a real repo.
