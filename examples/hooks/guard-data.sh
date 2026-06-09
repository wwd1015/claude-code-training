#!/usr/bin/env bash
# PreToolUse hook — block edits/writes to a data/ path so the agent never touches datasets.
# Claude Code sends the tool call as JSON on stdin. Exit code 2 BLOCKS the tool call and
# shows stderr to Claude. See https://code.claude.com/docs/en/hooks
set -euo pipefail

input="$(cat)"
path="$(printf '%s' "$input" | python3 -c \
  "import sys,json; d=json.load(sys.stdin); print((d.get('tool_input') or {}).get('file_path',''))" \
  2>/dev/null || true)"

case "$path" in
  */data/*|data/*)
    echo "Blocked by data-guard hook: writing to '$path' is not allowed. Data files are off-limits." >&2
    exit 2
    ;;
esac
exit 0
