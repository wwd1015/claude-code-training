# Glossary — Claude Code terms for data scientists & quants

The vocabulary, with a quant translation where it helps. Official reference:
[Claude Code glossary](https://code.claude.com/docs/en/glossary).

| Term | What it means | Quant translation |
|------|---------------|-------------------|
| **Agent / agentic** | A model that takes actions in a loop (reads files, runs code, edits) toward a goal — not just answering a question. | A research assistant who can actually open your repo and run your scripts, not just chat. |
| **Turn** | One round of you prompting and Claude responding (possibly with many tool calls inside). | One "ask." |
| **Plan mode** | A mode where Claude proposes what it will do and waits for approval before touching anything. Toggle with `shift+tab`. | "Show me the diff before you run it." |
| **Permission mode** | How much Claude can do without asking (ask each time / accept edits / etc.). | The blast radius you've authorized. |
| **Tool** | A capability Claude can call: read, edit, run a command, search, etc. | The verbs available to the assistant. |
| **CLAUDE.md (memory)** | A file Claude reads every session for persistent project context. | The repo's onboarding note, so you stop re-explaining your stack. |
| **Slash command** | A reusable prompt you invoke with `/name`. | A saved macro for a task you repeat. |
| **Skill** | A packaged capability (a `SKILL.md` + optional scripts) Claude auto-uses when relevant. | A versioned, shareable "recipe" — `/eda`, `/backtest-report`. |
| **Subagent** | A separate Claude instance the main one spawns for a focused job, with its own clean context. | Delegating one task to a teammate so your own desk stays uncluttered. |
| **Fan-out** | Running many subagents in parallel over many items. | `joblib.Parallel`, but each worker is a reasoning agent. |
| **Hook** | A script that fires automatically at a lifecycle point (after an edit, before a command). | A pre/post-commit hook, but for the whole agent loop. |
| **MCP (Model Context Protocol)** | An open standard for plugging Claude into external tools/data via a server. | A typed connector to your warehouse / API. |
| **MCP server** | The process that exposes a tool or data source to Claude over MCP. | The adapter that decides what Claude can touch (scope it read-only). |
| **Headless mode** | Running Claude non-interactively (`claude -p "..."`) for scripts/CI/cron. | A batch job instead of a REPL session. |
| **Context window** | How much text Claude can consider at once (your repo, files, history). | RAM for the conversation. |
| **Allowlist** | Commands/tools pre-approved so Claude won't stop to ask. | Whitelisting your safe, routine commands. |
| **Output style** | A preset that shapes how Claude formats responses. | House style for the assistant. |
| **Checkpoint** | A saved point you can rewind to. | Git stash for the session. |
| **Agent SDK** | Libraries to build your own agents on the same engine. | The programmatic API behind Claude Code. |

See also: [cheatsheet](cheatsheet.md) · [FAQ](faq.md) · [data handling](data-handling.md).
