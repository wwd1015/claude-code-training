---
id: 401-04
title: "The Agent SDK: Building Custom Agents"
duration: 40 min
objectives:
  - Explain what the Agent SDK provides and how it relates to Claude Code
  - Treat system prompt, tools, and permissions as the three design surfaces
  - Choose the right layer: prompt, skill, subagent, headless CLI, or SDK
  - Recognize when custom tools and a programmatic permission policy make the SDK the right layer — and when they don't
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
up to own deployment, monitoring, and upgrades for no added capability. (The
SDK ships for Python and TypeScript; the [overview](https://code.claude.com/docs/en/agent-sdk/overview)
has the install and the current API.)

## Worked example: an "ask the warehouse" service

Analysts keep asking the data team the same shape of question — *"what's the
30-day null rate on the positions feed?"* — and waiting hours for a hand-written
query. You want a self-serve agent inside an internal web app. That's squarely
SDK territory, because it needs things a cron'd `claude -p` can't give you.
Design it on the three surfaces:

- **System prompt** — role ("you answer warehouse questions for analysts"),
  rules (read-only, cite the query you ran, refuse anything not answerable from
  the allowed schemas), and an output contract (a short answer + the SQL + a
  table or chart).
- **Tools** — not raw bash. You define two custom tools your application owns:
  `run_sql(query)` bound to a read-only service account, and `plot(spec)` that
  returns an image your UI can render. The tool list *is* the capability
  boundary — the agent literally cannot do anything else.
- **Permissions** — a policy in your code auto-approves `run_sql` against the
  allowlisted schemas, and forbids everything else without a prompt. There's no
  human in the terminal to confirm, so the policy has to be exhaustive.

Your application is the harness: it takes the analyst's question from the web
form, runs the agent, and renders the answer in the UI. Contrast this with the
CI diff-reviewer from module 3 — that one needs only a prompt on a schedule, so
a headless `claude -p` step is the right (lower) layer. The tell that pushed
*this* one up the ladder: **custom tools** and a **programmatic permission
policy**, living **inside a product**.

### Best practices

- **Exhaust the lower rungs first.** Prompt → skill → subagent → headless CLI →
  SDK. Each rung you climb, you take on more to own (deployment, monitoring,
  upgrades). Only climb when the rung below genuinely can't do the job.
- **A single agent with good tools beats a premature multi-agent system.** Reach
  for orchestration when one agent measurably can't cope, not on spec. Most
  "agent platform" ideas are one well-scoped agent with two custom tools.
- **Prefer narrow custom tools over raw bash.** `run_sql(read_only)` is safer,
  more legible, and easier to audit than handing the agent a shell and hoping.
  The tool boundary is your strongest guardrail — design it deliberately.
- **Make the permission policy exhaustive, because nobody's watching.** In a
  service there's no interactive confirm. Every action is auto-approved,
  auto-denied, or escalated to a human queue — decide which for each, and
  default-deny the unknown.
- **Treat prompt, tools, and policy as versioned code.** They belong in the repo
  under review like any other source; a prompt change is a behavior change and
  deserves the same scrutiny as a code change (module 6 makes this auditable).
- **Own the observability from day one.** Claude Code gave you a transcript for
  free; in the SDK you build the logging. Capture inputs, tool calls, and
  verdicts so a bad answer in production is diagnosable.

### Common pitfalls

- **Reaching for the SDK when a skill + cron'd `claude -p` would do.** You inherit
  deployment, monitoring, and upgrades for zero added capability. Fix: write the
  one-line "why not the layer below?" justification before you build; if it's
  weak, drop a rung.
- **Handing the SDK agent unbounded tools "to be flexible."** A read-only Q&A
  agent with shell and network access is a liability. Fix: expose the minimum
  set of narrow tools the job needs and nothing more.
- **No permission callback — the agent acts freely in a service.** Fix: make the
  policy a required part of the design; default-deny anything not explicitly
  allowed.
- **Rebuilding Claude Code.** If your "custom agent" is just a terminal
  assistant with the standard tools, you're reimplementing what you already
  have. Fix: the SDK earns its keep only where Claude Code can't reach — custom
  tools, your own UI, embedded in a service.

**For quants / For data scientists:** a **Quant** might wrap the SDK around a
pricing library as a custom tool so an agent can answer "reprice the book under
this shock" from a risk dashboard; a **Data Scientist** might expose a
feature-store lookup and a model-scoring tool behind an internal endpoint. Same
three surfaces — the custom tools are where your **Technique** becomes something
the agent can safely call.

**Reuse (official):** [Agent SDK overview](https://code.claude.com/docs/en/agent-sdk/overview) ·
[Building effective agents (engineering)](https://www.anthropic.com/engineering/building-effective-agents)

## Lab

No code required: pick one agent idea from your team's backlog and write a
one-page SDK design — system prompt (rules + output contract), exact tool
list, permission policy (auto / confirm / forbid), and the harness (what
invokes it, where results land). Then justify in three sentences why it needs
the SDK rather than a skill + headless CLI. Bring it to office hours or your
501 working group — this doubles as a capstone proposal.

**Stretch:** deliberately try to knock your idea *down* a rung. Rewrite it as a
skill plus a cron'd `claude -p` and see how far you get; the design earns the
SDK only where that rewrite visibly fails (needs custom tools, its own UI, or
lives inside a service). List the two narrowest custom tools it would expose and
the default-deny rule for everything else.

## Knowledge check

1. What does the SDK provide that calling the raw API doesn't?
2. Name the three design surfaces and one decision you'd make on each.
3. Give one signal that a project genuinely needs the SDK layer — and one that it doesn't.
4. Why prefer a narrow custom tool (e.g. `run_sql` bound to a read-only account) over giving the agent bash?
5. **Scenario:** a colleague wants to build an "SDK agent" that reviews every PR
   diff against a checklist and comments pass/fail. Which layer does that
   actually need, and what would have to be true to justify the SDK instead?
