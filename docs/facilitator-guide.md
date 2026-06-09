# Facilitator guide — running a Cohort

Runbook for whoever runs a **Cohort** — usually a department **Champion** or volunteer, sometimes
central staff in a big department. A Cohort is **one** delivery mode; most Learners adopt via
**self-serve** (the [entry site](../site/index.html)) plus a Champion's office hours. See the
[operating model](operating-model.md). Pairs with the [session decks](sessions/).

## Cohort at a glance (2–3 weeks)
| When | What | Owner |
|------|------|-------|
| T-1 week | Send invite + pre-work; everyone installs | Facilitator |
| Week 1 | Workshop A (fundamentals) | Facilitator |
| Week 1–2 | Office hours (drop-in) | Champion |
| Week 2 | Workshop B (config + first builds) | Facilitator |
| Week 2 | Workshop C (agents + MCP) | Facilitator |
| Week 2–3 | Capstone build + office hours | Champion |
| Week 3 | Capstone demo day | Facilitator |
| T+30 days | Active-use check + metrics roll-up | Central owner |

## Prep checklist (before Workshop A)
- [ ] Cohort list finalized (8–15 is a good size for one facilitator).
- [ ] Pre-work email sent (template below).
- [ ] Demo data generated: `cd demos/setup && pip install -r requirements.txt && python gen_sample_dataset.py && python gen_backtest_results.py && python gen_series.py`.
- [ ] For a **quant** cohort: `pip install statsmodels && python gen_regression_data.py` (for the `/regression-diagnostics` anchor).
- [ ] For Workshop C: `pip install duckdb && python gen_warehouse.py`, and a DuckDB MCP server installed + tested ([examples/mcp](../examples/mcp/)).
- [ ] A throwaway sandbox repo ready for anyone without their own.
- [ ] Metrics sheet ready ([metrics template](metrics-template.md)).

## Running the live sessions
- Keep it hands-on: Learners typing into Claude Code by ~minute 20.
- Demo from the [scripts](../demos/INDEX.md), don't improvise — they're timed and de-risked. Pick the quant or DS anchor to match the cohort.
- Float during hands-on; collect 2–3 real stumbles to address in office hours.
- End every session with a take-home tied to the Learner's *own* work.

## Comms templates

**Invite / pre-work (T-1 week)**
> Subject: Claude Code training — start here before <date>
> You're in the next Claude Code cohort. ~30 min of pre-work before our first session:
> 1) Install + sign in: https://code.claude.com/docs/en/quickstart
> 2) Take Claude Code 101 (self-paced): https://anthropic.skilljar.com/claude-code-101
> 3) Pick one of your own notebooks/repos to bring.
> Portal with everything: <Pages URL>. See you <date/time>.

**Capstone kickoff (after Workshop C)**
> Your capstone: automate one real recurring task with Claude Code (a skill, agent, hook, or
> MCP connection). 5-min live demo on <demo day>. Stuck? Office hours <times>. Ideas:
> docs/capstone-ideas.md.

**Post-cohort (T+30)**
> Quick check-in: what have you automated since the cohort, and roughly how much time/week is it
> saving? (one line is fine) — feeds our impact roll-up.

## Common failure modes
- People arrive un-installed → pre-work email + a 5-min unblock buffer in Workshop A.
- MCP demo flakes live → test `claude mcp add` on the room's network the day before.
- Capstones too ambitious → steer toward something they do *weekly*, not a moonshot.
