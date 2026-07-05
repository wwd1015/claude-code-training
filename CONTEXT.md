# Claude Code Training (for DSQ)

Internal enablement program teaching Claude Code to the firm's data scientists and quants
across departments. This glossary fixes the language used to describe the audience and the
program, so the docs, demos, and entry site stay consistent.

## Language

### Audience

**DSQ**:
Umbrella term for the program's audience — the firm's **Data Scientists** and **Quants**. Use
it only when a statement applies to both. Not a homogeneous group; see the two roles below.
_Avoid_: "engineers", "users", "students" (technical, but not software engineers).

**Quant**:
A modeler who builds **economic / econometric models** with traditional techniques —
regression, time-series, statistical inference. Python is common but not universal (also R,
MATLAB, SAS).
_Avoid_: conflating with Data Scientist; "analyst".

**Data Scientist**:
A practitioner working primarily with **machine learning and big-data techniques** — feature
engineering, large datasets, distributed compute, ML/DL frameworks.
_Avoid_: conflating with Quant.

**Department**:
The org unit a DSQ sits in. Use cases and experience levels vary by **department**,
independently of role — segmentation is two-axis (discipline × department), not one.

### Program & demos

**Spine**:
The single, discipline-agnostic core the program teaches — the Claude Code competencies
(skill creation, hooks, subagents, MCP) and the path through them. Every DSQ applies the same
Spine to their own niche; the program does **not** fork per discipline. The user also calls
this "the framework". The Spine is maintained as the five Courses of the Backbone.
_Avoid_: "framework" in the software-library sense; "platform".

**Backbone**:
The versioned, centrally-maintained curriculum implementation of the Spine: five **Courses**
(CC 101–501) under `backbone/`, each with canonical modules, provenance, a changelog, and
generated outputs. Operated with `/backbone-sync`. Design: `BACKBONE.md`.
_Avoid_: using "backbone" for the official Anthropic material (that's the *source of truth*
the modules link out to).

**Course**:
One of the five numbered catalog entries (CC 101 Foundations, CC 201 Make It Yours, CC 301
Skills·Hooks·MCP, CC 401 Agent Systems, CC 501 Capstone Studio). The unit of versioning and
delivery. The track-based design in `docs/curriculum.md` is source material for the Courses
(T0+1→101, T2→201, T3→301+401, T4→501).
_Avoid_: Track numbering in learner-facing material; speak in course codes.

**LOB edition**:
A team's derivative of the backbone — backbone modules plus the team's overlays (demos, use
cases, policies) anchored to module IDs, generated under `lob/<team>/`. Never edits backbone
files; re-syncs when the backbone version advances. Operated with `/lob-overlay` by a
**Champion**.
_Avoid_: "fork" — an edition tracks the backbone, a fork abandons it.

**Demo**:
A facilitator-ready, DSQ-native worked example pairing one Claude Code competency with a
discipline use case (e.g. skill-creation × regression-diagnostics). Two kinds:

**Seed demo**:
A reference Demo authored in this repo to illustrate the Spine (the current `demos/01–06`). Not
canonical curriculum — an example to reference, expected to be supplemented and outnumbered by
Contributed demos. **Program-maintained:** central keeps Seeds current.
_Avoid_: treating Seed demos as "the curriculum".

**Contributed demo**:
A Demo authored by a DSQ for their department's niche use case. The steady-state **Demo library**
grows from these, typically promoted from a **Capstone**. **Author-/department-owned:** central
does not maintain it; a stale Contributed demo is archived, not fixed.

**Capstone**:
The real recurring task a DSQ automates with Claude Code during the program. The primary engine
that turns learners into contributors: a successful Capstone becomes a Contributed demo.

### Building blocks & artifacts

**Skill**:
A Claude Code `SKILL.md` artifact — a packaged capability Claude auto-invokes (`/eda`,
`/backtest-report`). The word "Skill" is reserved for this and nothing else.
_Avoid_: using "skill" for a learner's ability or for a thing the program teaches.

**Building block**:
One of the four things Track 3 teaches: **skill creation, hooks, subagents, MCP**. The
skill-creation building block is the one that produces **Skills**.
_Avoid_: "competency", "module" when you specifically mean these four.

**Technique**:
A DSQ's own professional modeling ability — regression, cointegration, gradient boosting, etc.
Belongs to the learner, not to Claude Code.
_Avoid_: "skill" for these.

### Delivery

**Learner**:
A DSQ going through the program, whether Self-serve or in a Cohort.
_Avoid_: "student", "user", "attendee", "participant" — standardize on **Learner**.

**Self-serve**:
The baseline delivery mode available to all ~1000 DSQ — the entry site, the progress checklist,
and the self-paced official courses. No instructor required. Reaches the long tail of small
departments that never get a formal Cohort.

**Champion**:
A DSQ appointed to lead Claude Code adoption within their **Department** — runs office hours,
shepherds **Contributed demos**, and usually leads that department's **Cohorts**. The standing,
ongoing role; the linchpin of the federated model.
_Avoid_: equating with "Facilitator" — a Champion often *acts as* Facilitator, but the role is
broader and permanent.

**Facilitator**:
Whoever delivers a given **Cohort** — a central instructor (mostly in big departments) or a
**Champion** / department volunteer. A function performed for one Cohort, not a standing title.
_Avoid_: assuming the Facilitator is central staff; most are department volunteers.

**Cohort**:
A time-boxed group that works through the **Spine** together. Instructor-led in big departments;
**Champion- or volunteer-led** elsewhere. One delivery mode among several, not the default.

## Flagged ambiguities

- **Seed-demo balance:** most Seed demos are discipline-neutral or **Data Scientist**-leaning;
  Demo 06 (`demos/06-regression-diagnostics.md` — VIF, heteroskedasticity, stationarity)
  anchors the **Quant** side. Keep both disciplines represented as the library grows.

## Example dialogue

> **Facilitator:** Is this cohort quants or data scientists?
> **Lead:** Mixed. The rates desk quants do econometric work — regressions, cointegration.
> The fraud team are data scientists — gradient-boosted trees on huge tables.
> **Facilitator:** Then one anchor demo won't land for both. The quants need a
> regression-diagnostics example; the data scientists need a big-data/ML one.
> **Lead:** Right — same Claude Code skills, different example data and modeling.
