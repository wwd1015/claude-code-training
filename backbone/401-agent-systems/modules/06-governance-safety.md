---
id: 401-06
title: "Governance & Safety for Agent Systems"
duration: 25 min
objectives:
  - Apply least-privilege thinking to agent permissions and credentials
  - Make agent actions observable and auditable after the fact
  - Place human review gates before irreversible actions
---

## Least privilege, at scale

CC 101's rule — start conservative, loosen as trust accrues — becomes policy
when agents multiply:

- **Permissions per role, not per person.** A reviewer subagent gets read-only
  tools; a doc generator gets write access to `docs/` and nothing else
  (tool allowlists + settings from CC 201/301 are the mechanism).
- **Credentials scoped to the job.** An agent querying the warehouse gets a
  read-only service account for the schemas it needs — never a human's
  personal credentials, which grant everything the human can do and audit as
  the human. <!-- verify: name the internal process for provisioning service accounts for agent use -->
- **Blast radius by placement.** Run automation in checkouts and sandboxes
  that physically cannot reach production paths; the strongest permission
  rule is a directory that doesn't contain the dangerous thing.

## Observability & audit

"What did the agent do, and why?" must be answerable after the fact:

- Keep the artifacts: headless runs write their reports, diffs, and
  verification evidence to files (401-03) — retain them like build logs.
- Prefer changes through git: a commit trail of agent edits is a free audit
  log with rollback included.
- Log the inputs too — which prompt/skill version ran. When output quality
  shifts, the first question is "what changed?"; version your prompts like
  code because they are.

## Review gates

Decide, in the design, which actions require a human between the agent and the
world. The test is **reversibility**: editing a branch is reversible (gate:
none needed); merging to main, sending external messages, writing to shared
databases, deleting data are not (gate: human approval, or the agent's output
is a *proposal* — a PR, a draft — that a human executes).

The pattern that scales: agents produce **artifacts**, humans (or gated
pipelines) **promote** them. It keeps agent speed on the safe side of the line
and human judgment exactly where it pays.

**Reuse (official):** [Security](https://code.claude.com/docs/en/security) ·
[Settings/permissions docs](https://code.claude.com/docs/en/settings)

## Lab

Audit the automation you built in 401-03 against the three sections: write
its permission set and credential scope (tightening at least one thing),
confirm you can reconstruct its last run from artifacts alone, and mark each
action it takes as reversible or gate-required. Fix the gaps.

## Knowledge check

1. Why must an unattended agent never run on personal credentials?
2. What makes git the cheapest audit mechanism for agent systems?
3. State the reversibility test and give one example on each side of the line.
