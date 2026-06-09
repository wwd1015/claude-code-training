# Curriculum

**Audience:** internal data scientists & quants (strong Python/stats/notebooks; not engineers)
**Delivery:** hybrid — self-paced official pre-work + live demo/workshop + office hours
**Principle:** official Anthropic material carries the conceptual load; we build only a thin
custom layer (quant demos + exercises + templates). See [reading-lists.md](reading-lists.md).

---

## Design principles

1. **Reuse first.** Each module names an official Anthropic course/doc as pre-work. We build only the delta.
2. **Quant-native examples.** EDA, research-notebook refactors, backtests, data-QA/anomaly triage, SQL/warehouse — never to-do apps.
3. **Bridge, don't assume.** Cover git, terminal hygiene, and the agentic mental model explicitly and fast.
4. **Apply to real work.** Every module ends with "do this to one of your own notebooks/tasks." The capstone automates a recurring task.
5. **Tiered, not linear-only.** Beginners finish Track 1; power users jump to Track 3.

---

## The 5 tracks

| Track | Title | Level | Format | Time |
|------|-------|-------|--------|------|
| 0 | Orientation & mental model | All | Self-paced | ~30 min |
| 1 | Daily-driver fundamentals | Onboarding | Self-paced + live workshop | ~2 hrs |
| 2 | Make it yours: configuration | Intermediate | Hybrid | ~2 hrs |
| 3 | Advanced builder (skills · hooks · agents · MCP) | Advanced | Live + office hours | ~3–4 hrs |
| 4 | Capstone: automate your own work | All | Project + office hours | self-directed |

### Track 0 — Orientation & mental model (~30 min)
The agentic loop (ask → plan → act → verify), install & auth, the permission/safety model.
- **Quant framing:** "a pair-researcher in your terminal that can read your whole repo and run your code — not autocomplete."
- **Reuse:** [Overview](https://code.claude.com/docs/en/overview) · [Quickstart](https://code.claude.com/docs/en/quickstart) · [Claude Code 101](https://anthropic.skilljar.com/claude-code-101)
- **Outcome:** installed, authenticated, ran first prompt against a sample repo.

### Track 1 — Daily-driver fundamentals (~2 hrs)
Navigate/search an unfamiliar repo, read & explain code, edit files, run scripts/notebooks,
plan mode, basic git, iterating with the model.
- **Reuse:** [Common workflows](https://code.claude.com/docs/en/common-workflows) · [Claude Code in Action](https://anthropic.skilljar.com/claude-code-in-action)
- **Demo:** [01 — EDA + data dictionary](../demos/01-eda-data-dictionary.md)
- **Apply:** point Claude at your own notebook → explain the flow + add a docstring/README.

### Track 2 — Make it yours: configuration (~2 hrs)
`CLAUDE.md` memory, user vs project settings, custom slash commands, output styles,
permissions/allowlists, first taste of MCP.
- **Reuse:** [Memory](https://code.claude.com/docs/en/memory) · [Settings](https://code.claude.com/docs/en/settings) · [Best practices](https://code.claude.com/docs/en/best-practices)
- **Demo:** author a research-repo `CLAUDE.md` ([template](../templates/CLAUDE.research-repo.md)) + an `/eda` command ([skill](../skills/eda/SKILL.md)).
- **Apply:** write your own `CLAUDE.md` + one personal slash command.

### Track 3 — Advanced builder
The four priority topics. Each: official course pre-work → live demo → take-home build.

| Module | Reuse (official) | Demo | Apply |
|--------|------------------|------|-------|
| 3a Skill creation | [Intro to Agent Skills](https://anthropic.skilljar.com/introduction-to-agent-skills) · [Skills docs](https://code.claude.com/docs/en/skills) | [02 — /backtest-report skill](../demos/02-backtest-report-skill.md) | ship one skill for a recurring task |
| 3b Hooks & settings | [Hooks docs](https://code.claude.com/docs/en/hooks) · [Settings](https://code.claude.com/docs/en/settings) | [05 — hooks automation](../demos/05-hooks-automation.md) · [examples/hooks](../examples/hooks/) | add one hook to your repo |
| 3c Building agents | [Intro to Subagents](https://anthropic.skilljar.com/introduction-to-subagents) · [Subagents docs](https://code.claude.com/docs/en/sub-agents) · [Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview) | [03 — anomaly-triage agent](../demos/03-anomaly-triage-agent.md) | design a subagent for your workflow |
| 3d MCP & integrations | [Intro to MCP](https://anthropic.skilljar.com/introduction-to-model-context-protocol) · [MCP advanced](https://anthropic.skilljar.com/model-context-protocol-advanced-topics) · [MCP docs](https://code.claude.com/docs/en/mcp) | [04 — SQL/data over MCP](../demos/04-sql-over-mcp.md) · [examples/mcp](../examples/mcp/) | scope an MCP server for one data source |

### Track 4 — Capstone: automate your own work
Each participant automates a real recurring task (skill / agent / hook / MCP) and demos it.
Doubles as proof of time saved + the demo bank for the next cohort.

---

## Build roadmap (creating the curriculum)

| Phase | Goal | Output | Est. |
|-------|------|--------|------|
| 1. Inventory & map | Confirm official assets; finalize reuse map | [reading-lists.md](reading-lists.md) ✅ | done |
| 2. Define thin layer | Decide minimum custom content | demo/exercise/template list | 1 day |
| 3. Build pilot | Reading lists + decks + demo scripts + starter repo | this repo | in progress |
| 4. Pilot & measure | Run one small cohort; collect time-saved data | iterated v1 + metrics | 2–3 wks |
| 5. Scale | Record demos, internal portal, recurring cohorts | self-serve | ongoing |

## Supporting material
- **Learner reference:** [cheatsheet](cheatsheet.md) · [glossary](glossary.md) · [FAQ](faq.md) · [data handling & safety](data-handling.md)
- **Facilitator:** [facilitator guide + comms templates](facilitator-guide.md) · [session decks](sessions/) · [metrics template](metrics-template.md) · [capstone ideas](capstone-ideas.md)
- **Templates & examples:** [research-repo CLAUDE.md](../templates/CLAUDE.research-repo.md) · [hooks](../examples/hooks/) · [MCP](../examples/mcp/) · starter skills ([eda](../skills/eda/SKILL.md), [backtest-report](../skills/backtest-report/SKILL.md), [triage-data](../skills/triage-data/SKILL.md))
- **Contributing:** [how to add demos/skills/capstones](../CONTRIBUTING.md)

## Open questions
- Cohort size & number of cohorts (self-paced vs live ratio)?
- Which internal data sources are fair game for the MCP demo?
- Standard sandbox repo/dataset for demos?
- Co-delivery + publishing channel (this repo's Pages site, or internal wiki)?
