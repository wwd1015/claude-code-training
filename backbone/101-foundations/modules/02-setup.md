---
id: 101-02
title: "Install, Authenticate & Set Up Your Environment"
duration: 30 min
objectives:
  - Install Claude Code and authenticate with your organization's method
  - Start and exit a session; know where you are (directory = context)
  - Use enough terminal and git to work confidently
  - Recover from the two most common first-session snags (wrong directory, wrong Python env)
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

## Worked example: prove the environment is really yours

The most common "it doesn't work" is an environment mismatch — Claude Code
inherits the shell you launched it from, nothing more. Prove it in ten seconds
before you trust a session:

> Run `python -c "import sys; print(sys.executable)"` and
> `git rev-parse --show-toplevel`, then tell me which Python and which repo root
> you're operating in.

If the Python path isn't your project's env, or the repo root isn't the project
you meant, stop and fix it in the terminal — not inside the session. Activate the
env (`conda activate research` / `source .venv/bin/activate`), `cd` to the right
root, and relaunch `claude`. Everything downstream — which `pandas`, which
credentials, which files — follows from those two facts.

### Best practices

- **Launch from the project root, every time.** The directory is the agent's
  whole world: the files it can read, the git repo it checkpoints against.
  Starting one level too high or too low is the difference between "give me a
  tour" working and it seeing nothing useful.
- **Make your first commit before your first prompt.** A clean `git status` at
  the start means every later "what did you change?" has an honest baseline. If
  the repo isn't initialized, ask Claude to `git init` and commit the current
  state first.
- **Set the env in the terminal, verify it in the session.** Claude can't switch
  conda envs for you retroactively; it uses whatever `python` resolved to when
  you launched. Confirm with the check above rather than assuming.
- **Learn `--continue` vs `--resume`.** `claude --continue` reopens your most
  recent conversation; `claude --resume` lets you pick an older one from a list.
  Both beat re-explaining context from scratch. <!-- verify: confirm --resume picker behavior on your installed version -->
- **Keep one terminal tab per project.** Since directory = context, juggling two
  projects in one tab invites launching Claude in the wrong root. One tab, one repo.

### Common pitfalls

- **Launching in your home directory "to look around."** Now the agent's world is
  your entire home folder — slow, noisy, and it may read things you didn't intend.
  Always `cd` into the specific repo first.
- **Assuming Claude sees your Jupyter kernel's environment.** It sees the
  terminal's environment. If your notebook runs in `research` but your terminal
  is on `base`, imports fail in ways that look like Claude's fault. Activate the
  env first.
- **Worrying you'll "lose work" to the agent.** Nothing committed is ever lost,
  and you can always ask "show me what you changed" or revert. The fear that keeps
  notebook people from delegating is exactly the one git removes — that's the
  point of working in a repo.
- **Editing dotfiles to force auth before checking your org's method.** Don't.
  Your organization has an approved install and login path; guessing can put
  credentials in the wrong place.

### For quants / For data scientists

**Quants** on R/MATLAB/SAS: Claude Code is language-agnostic at the shell — if
`Rscript` runs in your terminal, it runs for Claude. The git and terminal habits
here matter more than the Python specifics. **Data scientists** juggling conda
envs and remote kernels: make the environment-proof check above a reflex; most
"broken" sessions are just the wrong interpreter.

**Reuse (official):** [Quickstart](https://code.claude.com/docs/en/quickstart) ·
[Common workflows](https://code.claude.com/docs/en/common-workflows)

## Lab

Install and authenticate. Then, in a terminal: clone or pick any repo you know,
launch `claude` at its root, and ask three questions about the codebase. Exit,
relaunch with `--continue`, and confirm it remembers the conversation.

**Stretch:** Before your three questions, run the two-line environment check from
above and paste the result into your notes. If either line surprises you, you
just found the snag that would otherwise have cost you an hour later.

## Knowledge check

1. Why does the directory you launch from matter?
2. How do you resume your previous conversation?
3. What's the practical reason to work inside a git repo with an agent?
4. `--continue` and `--resume` — what's the difference?
5. A teammate says "Claude keeps using the wrong pandas version." Which two commands do you have them run first, and why?
