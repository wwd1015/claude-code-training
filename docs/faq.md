# FAQ & troubleshooting

For DS/quants getting started. Deeper: [Troubleshooting](https://code.claude.com/docs/en/troubleshooting)
· [Quickstart](https://code.claude.com/docs/en/quickstart).

## Getting started
**Do I need to be good at git or the terminal?**
No. You need to be comfortable running a Python script. Claude handles most git for you —
ask it to "create a branch and commit this with a sensible message." CC 101 covers the basics.

**Where do I run it?** In a terminal, inside the repo/folder you want to work on: `claude`.

**It asked me to approve something — is that normal?**
Yes. By default Claude asks before running commands or editing files. Read it, approve if it's
what you wanted. Repeated prompts for safe commands? Add an allowlist (CC 201 /
[Settings](https://code.claude.com/docs/en/settings)).

## Working with it
**It changed something I didn't want.**
Use **plan mode** (`shift+tab`) next time so you approve before it writes. To undo: `git diff`
to see what changed, then `git checkout -- <file>` (or ask Claude to revert it).

**It made up a column / metric.**
It can infer wrong. Always ask it to *run the code and show real numbers*, and review any
inferred descriptions or labels — you're the domain expert.

**It edited the wrong file.**
Scope your ask: "only touch `src/features.py`." For a hard boundary, the `/freeze` workflow or
a PreToolUse [hook](../examples/hooks/) can block edits outside a directory.

**How do I make it stop re-explaining my repo every session?**
Add a `CLAUDE.md` (CC 201). Use the [research-repo template](../templates/CLAUDE.research-repo.md).

**My notebook is huge — will it fit?**
Big notebooks can blow the context window. Point it at the relevant cells/files, or have it
promote logic into `src/` first.

## Data & safety
**Can it see our internal data?**
Only what you give it (files in the repo) or what an MCP server exposes. Scope MCP servers
read-only. Never paste secrets/PII into a prompt. See [data handling](data-handling.md).

**Where does my data go?** Files stay local unless you connect a remote tool. Don't commit
data — the repo `.gitignore` already excludes `*.parquet`, `*.csv`, `data/`.

## Building
**Skill vs slash command vs subagent — which do I make?**
Slash command = a saved prompt. Skill = a packaged, auto-triggering capability you share.
Subagent = delegating a focused job (often fanned out). Start with a slash command; promote to
a skill when the desk wants it. See the [glossary](glossary.md).

**How do I run something nightly/unattended?** Headless mode: `claude -p "..."`, or the Agent SDK.

## Still stuck
Bring it to **office hours** — that's what they're for. Or open an issue in this repo.
