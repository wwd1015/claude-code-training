---
id: 101-03
title: "Your First Real Session: Explore, Plan, Edit, Run"
duration: 35 min
objectives:
  - Use Claude Code to navigate and explain an unfamiliar repo
  - Use plan mode to review an approach before any file changes
  - Complete an edit → run → verify cycle end to end
---

## Explore before you change

Agents are excellent at building maps. Openers that work on any repo:

- "Give me a tour of this repo — what are the entry points and the data flow?"
- "Where is <metric/model/report> computed? Walk me through it."
- "What would break if I changed <function>? Find the callers."

Ask follow-ups; it's a conversation, not a query language. Reference files
naturally ("the loader in `data/io.py`") — or use `@` to attach a file path
precisely.

## Plan mode: look before it leaps

For anything non-trivial, use **plan mode** (Shift+Tab cycles modes): Claude
researches and proposes a plan but changes nothing until you approve. This is
the single best habit for building trust early — you see the intended edits
as a reviewable plan, not as a surprise diff.

## The edit → run → verify cycle

Effective instructions share three parts (remember your lab from module 1):

1. **Goal** — "add a docstring and type hints to every function in `analysis.py`"
2. **Constraints** — "don't change behavior; keep the existing naming style"
3. **Verification** — "run the tests / rerun the script and confirm identical output"

Always give the third part. An agent that knows how to check its work will
check its work; one that doesn't will declare victory.

## Iterating

- Interrupt any time (`Esc`) to redirect; you don't have to let a wrong plan finish.
- "Show me what you changed" → it summarizes the diff.
- Wrong direction? Ask it to revert: git checkpoints (module 2) make this cheap.

**Reuse (official):** [Common workflows](https://code.claude.com/docs/en/common-workflows) ·
[Claude Code in Action](https://anthropic.skilljar.com/claude-code-in-action)

## Lab

On one of your own notebooks or scripts: (1) ask for a tour of what it does;
(2) in plan mode, request a cleanup (docstrings, dead-code removal, or
extracting a function) and read the plan critically before approving;
(3) have it run the result and confirm the output is unchanged. Time yourself
against doing it by hand.

## Knowledge check

1. What does plan mode change about the agentic loop?
2. What are the three parts of an effective instruction?
3. You approved a change and regret it — what are two ways to recover?
