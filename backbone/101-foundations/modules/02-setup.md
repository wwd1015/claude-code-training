---
id: 101-02
title: "Install, Authenticate & Set Up Your Environment"
duration: 25 min
objectives:
  - Install Claude Code and authenticate with your organization's method
  - Start and exit a session; know where you are (directory = context)
  - Use enough terminal and git to work confidently
---

## Install and authenticate

Follow the official [Quickstart](https://code.claude.com/docs/en/quickstart)
and [Setup docs](https://code.claude.com/docs/en/setup) for your platform.
The short version: install the CLI, run `claude` in a terminal, complete the
login flow. <!-- verify: confirm your org's approved install channel and auth method (console vs SSO) and note it here via intake -->

Verify it works:

```bash
cd path/to/any/repo
claude
> what does this repository do?
```

## The terminal bridge (for notebook-first people)

You need very little:

- `cd`, `ls`, `pwd` — move around; **the directory you launch `claude` from is
  its world**, so start it at the root of the project you care about.
- `Ctrl+C` interrupts; `/exit` or `Ctrl+D` leaves a session; `claude` resumes fresh,
  `claude --continue` picks up the last conversation.
- Your shell profile, Python env, and credentials are the ones Claude Code
  inherits — if `python` works for you in that terminal, it works for Claude.

## The git bridge

You don't need to be a git expert — Claude Code handles the mechanics if you
understand three ideas: a **commit** is a checkpoint, a **branch** is a
parallel line of checkpoints, and **nothing committed is ever lost**. Practical
habit: work in a repo (ask Claude to `git init` if needed) and let checkpoints
make the agent's edits fearless — you can always ask it to show or undo what changed.

**Reuse (official):** [Quickstart](https://code.claude.com/docs/en/quickstart) ·
[Common workflows](https://code.claude.com/docs/en/common-workflows)

## Lab

Install and authenticate. Then, in a terminal: clone or pick any repo you know,
launch `claude` at its root, and ask three questions about the codebase. Exit,
relaunch with `--continue`, and confirm it remembers the conversation.

## Knowledge check

1. Why does the directory you launch from matter?
2. How do you resume your previous conversation?
3. What's the practical reason to work inside a git repo with an agent?
