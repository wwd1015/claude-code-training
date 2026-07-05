# Workshop C — Agents + integrations (CC 401 subagents + CC 301 MCP)

**Length:** 90 min · **Format:** live
**Pre-work:** [Introduction to Subagents](https://anthropic.skilljar.com/introduction-to-subagents) +
[Introduction to MCP](https://anthropic.skilljar.com/introduction-to-model-context-protocol).

## Slide 1 — From one prompt to many agents (5 min)
- When a task is "do the same check across 200 things," fan-out beats one big prompt.
- Cheaper, parallel, and each checker has clean context.

## Slide 2 — Subagents (10 min)
- Orchestrator + workers; isolation; when to use. Reference: [Sub-agents](https://code.claude.com/docs/en/sub-agents).
- The mental model: a research team, not a single researcher.

## Slide 3 — LIVE DEMO: anomaly-triage agent (20 min)
- Run [Demo 03](../../demos/03-anomaly-triage-agent.md) over `data/series/`.
- Verify against `data/series_truth.csv` — did it find the 12 injected anomalies?
- Land it: this is the multi-agent research pattern applied to data QA. Ties to LENS `/triage-data`.

## Slide 4 — Headless / batch (10 min)
- `claude -p` and the [Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview) for unattended jobs.
- "Re-run this nightly and alert me" — the path from interactive to scheduled.

## Slide 5 — MCP: plug Claude into your data (10 min)
- MCP = a typed plug between Claude and your tools/data. The *server* defines access, not the prompt.
- Start read-only. Least privilege. Reference: [MCP](https://code.claude.com/docs/en/mcp).

## Slide 6 — LIVE DEMO: SQL over MCP (20 min)
- Run [Demo 04](../../demos/04-sql-over-mcp.md) against `data/warehouse.duckdb`.
- NL → SQL → result → chart. Then wrap it as a `/daily-volume` command.
- Discuss the trust boundary explicitly: never hand a demo server write/DDL.

## Slide 7 — Capstone kickoff + take-home (15 min)
- Assign the capstone: automate one real recurring task (skill/agent/hook/MCP) and demo it.
- Take-home: scope a subagent OR an MCP server for one of your own workflows.

## Facilitator prep
- `cd demos/setup && python gen_series.py && pip install duckdb && python gen_warehouse.py`.
- Pre-install a DuckDB MCP server and confirm `claude mcp add` works before the room is watching.
- Teach from the [CC 401 instructor deck](../../site/courses/401-deck.html); assign
  [CC 401](../../site/courses/401.html) as follow-up and point builders at the capstone course
  ([CC 501](../../site/courses/501.html)).
