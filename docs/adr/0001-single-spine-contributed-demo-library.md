# Single Spine with a contributed demo library, organized by competency

The audience (DSQ) spans two disciplines — **Quants** (econometric/economic modeling,
regression) and **Data Scientists** (ML, big data) — across many departments with varied use
cases and skill levels.

We teach **one discipline-agnostic Spine** (the five Tracks + the Claude Code building blocks:
skill creation, hooks, subagents, MCP) rather than forking per-discipline programs. The in-repo
demos are **Seed** examples only; the real **Demo library** is **contributed by DSQ for their own
niches**, promoted from **Capstones**. Demos use **competency/track as the only structural (folder)
axis**, with **discipline / department / use-case / kind** as front-matter tags.

## Considered options

- **Fork per discipline** (a Quant track + a DS track) — rejected: doubles maintenance,
  contradicts reuse-first, and the Capstone already personalizes to each person's real work.
- **Folder-per-department** as the structure — rejected: org reorgs age the taxonomy, and it
  hides cross-department reuse (a fraud-team anomaly demo can help another team).

## Consequences

- The repo owes at least one **Quant** seed demo (econometric/regression), to balance the
  ML-leaning seeds.
- Demos need a front-matter tag scheme (`track`, `discipline`, `department`, `use_case`, `kind`)
  plus an index, and eventually tag filters on the site's demo bank.
- Governance must keep a light line between program-maintained **Seed** demos and community
  **Contributed** demos.
