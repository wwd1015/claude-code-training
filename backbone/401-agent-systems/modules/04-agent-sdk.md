---
id: 401-04
title: "The Agent SDK: Building Custom Agents"
duration: 30 min
objectives:
  - Explain what the Agent SDK provides and how it relates to Claude Code
  - Treat system prompt, tools, and permissions as the three design surfaces
  - Choose the right layer: prompt, skill, subagent, headless CLI, or SDK
---

## The same engine, programmable

The **Agent SDK** exposes the agent engine that powers Claude Code — the
agentic loop, tool execution, permission handling, context management — as a
library you call from your own code. Instead of a person in a terminal, *your
application* is the harness: it decides what the agent works on, which tools
exist, and what happens with the results.

Read the [Agent SDK overview](https://code.claude.com/docs/en/agent-sdk/overview)
first; the [Claude with the Anthropic API course](https://anthropic.skilljar.com/claude-with-the-anthropic-api)
covers the underlying API concepts (tool use, streaming) the SDK builds on.

## Three design surfaces

Every custom agent is designed on the same three surfaces you've been using
all curriculum — now programmatically:

- **System prompt** — the agent's role, rules, and output contract. Everything
  you learned writing skills (CC 301) applies verbatim.
- **Tools** — you choose the set: built-ins (file ops, bash), MCP servers, or
  custom tools your application defines. The tool list *is* the capability
  boundary.
- **Permissions** — programmatic hooks decide what runs without asking, what
  requires confirmation, and what is forbidden — your CC 201 allowlist
  thinking, expressed in code.

## Picking the right layer

Work up this ladder; stop at the first rung that fits:

| Need | Layer |
|---|---|
| do a task once | prompt in a session |
| repeat a procedure reliably | skill (CC 301) |
| a scoped role with isolation | subagent (401-01) |
| run it on a schedule / in CI | headless CLI (401-03) |
| an agent inside your product or service, custom tools, own UI | **Agent SDK** |

The SDK is the right layer when the agent must live where Claude Code isn't:
inside an internal web app, a service endpoint, a data platform. It's the
wrong layer when a skill plus a cron'd `claude -p` would do — you'd be signing
up to own deployment, monitoring, and upgrades for no added capability.

**Reuse (official):** [Agent SDK overview](https://code.claude.com/docs/en/agent-sdk/overview) ·
[Building effective agents (engineering)](https://www.anthropic.com/engineering/building-effective-agents)

## Lab

No code required: pick one agent idea from your team's backlog and write a
one-page SDK design — system prompt (rules + output contract), exact tool
list, permission policy (auto / confirm / forbid), and the harness (what
invokes it, where results land). Then justify in three sentences why it needs
the SDK rather than a skill + headless CLI. Bring it to office hours or your
501 working group — this doubles as a capstone proposal.

## Knowledge check

1. What does the SDK provide that calling the raw API doesn't?
2. Name the three design surfaces and one decision you'd make on each.
3. Give one signal that a project genuinely needs the SDK layer — and one that it doesn't.
