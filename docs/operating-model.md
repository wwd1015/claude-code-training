# Operating model

How the program runs at ~1000 DSQ across 15–20 departments. Delivery is **federated**: a central
program supplies the Spine, the self-serve site, the official-course reading lists, the Demo
library, and Champion enablement — and **delivery is decentralized**. See
[ADR 0002](adr/0002-federated-delivery-champions-and-self-serve.md).

## Three delivery modes

1. **Self-serve (baseline, everyone).** The [entry site](../site/index.html), the progress
   checklist, and the self-paced official courses. No instructor. This is how the long tail of
   small departments adopts.
2. **Champion-led (per department).** A [Champion](../CONTEXT.md) runs office hours, shepherds
   Contributed demos, and sustains adoption locally. The engine of the federated model.
3. **Cohort (one mode, not the default).** A time-boxed group through the Spine — instructor-led
   in big departments, Champion-/volunteer-led elsewhere.

## Cohort shape (when a department runs one, 2–3 weeks)
- **Week 0 (self-paced):** CC 101 pre-work (Claude Code 101, Quickstart).
- **Live Workshop A:** CC 101 recap + an anchor demo (pick the quant or DS variant for the cohort).
- **Live Workshop B:** CC 201 (CLAUDE.md, slash commands, settings) + CC 301 skills & hooks.
- **Live Workshop C:** CC 401 subagents + CC 301 MCP.
- **Capstone demo day (CC 501):** each Learner demos a real task they automated — the best become Contributed demos.

## Office hours
Weekly drop-in to unblock real work, run by the department **Champion**. This is where adoption
actually converts — the sessions teach, office hours make it stick.

## Shared assets & the contribution loop
This repo is the shared asset: `CLAUDE.md` templates, starter Skills, hook samples, the
[Demo library](../demos/INDEX.md). Capstones flow back as **Contributed demos** (governance in
[CONTRIBUTING](../CONTRIBUTING.md)), so the library compounds across departments.

## Metrics
Steer by **one North Star**, not a basket — see [metrics-template](metrics-template.md). North
Star is active-use rate (if usage data exists) or federation health (if not); leading indicators
are champion coverage and Contributed-demos-per-quarter; time-saved is the executive headline.

## Roles
- **Champion** — standing per-department lead: runs office hours, curates Contributed demos, often
  acts as Facilitator. The linchpin.
- **Facilitator** — whoever runs a given Cohort (a Champion, a department volunteer, or central
  staff in big departments). A per-cohort function, not a title.
- **Central program owner** — maintains the Spine + Seed demos, keeps `reading-lists.md` current,
  enables Champions, does the light merge review on Contributed demos.
