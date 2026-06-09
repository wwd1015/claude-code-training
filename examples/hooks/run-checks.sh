#!/usr/bin/env bash
# PostToolUse hook — auto-format + lint after every edit. If lint fails, exit 2 surfaces the
# problems back to Claude so it fixes them. Skips silently if ruff isn't installed.
# See https://code.claude.com/docs/en/hooks
set -uo pipefail

cd "${CLAUDE_PROJECT_DIR:-.}" || exit 0
command -v ruff >/dev/null 2>&1 || exit 0   # no ruff -> no-op

ruff format . >/dev/null 2>&1 || true

if ! out="$(ruff check --fix . 2>&1)"; then
  echo "ruff found issues after the edit:" >&2
  echo "$out" >&2
  exit 2
fi
exit 0
