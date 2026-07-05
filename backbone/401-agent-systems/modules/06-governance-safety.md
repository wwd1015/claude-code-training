---
id: 401-06
title: "Governance & Safety for Agent Systems"
duration: 35 min
objectives:
  - Apply least-privilege thinking to agent permissions and credentials
  - Make agent actions observable and auditable after the fact
  - Place human review gates before irreversible actions
  - Design an agent so its last run can be reconstructed and rolled back from artifacts alone
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

## Worked example: governing the nightly warehouse-QA agent

Take the same nightly QA automation from modules 3 and 5 and put it through the
three sections — this is what makes the previous five modules acceptable to risk
and compliance:

- **Least privilege.** It runs under a **read-only service account** scoped to
  the QA schemas — never your personal warehouse login, which would let an
  unattended job do everything *you* can and log every action as *you*. Its only
  write is to `reports/`.
- **Blast radius by placement.** It runs in a checkout that has no path to the
  production tables or the model registry. The strongest permission rule is a
  working directory where the dangerous thing simply isn't reachable.
- **Observability.** Every run commits its dated report, the check output, and
  the prompt/skill version to git. Ask "what did it do, and why, on the 3rd?"
  and the answer is a commit — with rollback included for free.
- **Review gate by reversibility.** Writing a report is reversible: no gate.
  *Quarantining a table* or *blocking the morning load* is not — so the agent
  never does it directly. It emits a `STATUS: FAIL` artifact and a human (or a
  gated pipeline) promotes that into the actual quarantine. Agent speed on the
  safe side of the line; human judgment exactly at the irreversible step.

The whole design is one sentence: the agent **proposes**, a gated step
**disposes**, and git remembers both.

### Best practices

- **Permissions per role, not per person.** A reviewer subagent gets read-only
  tools; a report writer gets `reports/` and nothing else. Encode it in tool
  allowlists and settings, so the grant survives whoever's running it.
- **Scope credentials to the job.** Read-only service accounts for exactly the
  schemas needed. Personal credentials on an unattended agent are the one
  non-negotiable "never" — they grant everything you can do and destroy the
  audit trail.
- **Set blast radius by placement.** Sandboxes and checkouts that physically
  can't reach production beat any permission rule you could write, because
  there's nothing dangerous within reach to permit.
- **Route changes through git.** A commit trail of agent edits is a free audit
  log with rollback built in — the cheapest observability you'll ever get.
- **Version prompts and skills like code.** When output quality shifts, the first
  question is "what changed?" Stamp the prompt/skill version into the run so the
  answer is on disk, not in memory.
- **Gate by reversibility, and default to proposals.** Reversible actions (branch
  edits) need no gate; irreversible ones (merge, external message, shared-DB
  write, delete) get a human — or the agent's output is a PR/draft/report a
  human executes.

### Common pitfalls

- **Running the agent on personal credentials.** It acts as you and audits as
  you; a mistake is indistinguishable from your own work. Fix: a scoped service
  account, provisioned for agent use.
- **Blanket-approving actions to reduce friction.** A bypass-everything mode in a
  checkout that can reach production is one prompt drift from an incident. Fix:
  narrow allowlists plus placement that removes the dangerous path.
- **Output and evidence landing nowhere durable.** A week later you can't
  reconstruct what the agent did. Fix: persist reports, diffs, and verification
  evidence; prefer git so history and rollback come along.
- **Letting the agent take the irreversible action directly.** A merge, a
  warehouse write, a delete with no human in between. Fix: make the agent emit a
  proposal artifact and gate the promotion step.

**For quants / For data scientists:** a **Quant**'s agent anywhere near the
position or PnL store must be read-only and gated — a bad write is irreversible
money, and the reversibility test puts a human on it. A **Data Scientist**'s
agent touching the feature store or model registry is the same call — a
silently poisoned feature reaches every downstream model. Different asset,
identical test: reversible → no gate; irreversible → proposal plus a human.

**Reuse (official):** [Security](https://code.claude.com/docs/en/security) ·
[Settings/permissions docs](https://code.claude.com/docs/en/settings)

## Lab

Audit the automation you built in 401-03 against the three sections: write
its permission set and credential scope (tightening at least one thing),
confirm you can reconstruct its last run from artifacts alone, and mark each
action it takes as reversible or gate-required. Fix the gaps.

**Stretch:** take the single most dangerous action your automation could take
and redesign it as a **proposal** — the agent produces the artifact (a PR, a
`STATUS: FAIL` report, a draft), and a human or a gated pipeline promotes it.
Then, from artifacts alone, reconstruct exactly what the last run did and which
prompt version produced it; if you can't, you've found the gap to close.

## Knowledge check

1. Why must an unattended agent never run on personal credentials?
2. What makes git the cheapest audit mechanism for agent systems?
3. State the reversibility test and give one example on each side of the line.
4. Why is placement (where the agent runs) a stronger control than any permission rule you could write?
5. **Scenario:** a nightly agent is about to be given write access to the model
   registry so it can auto-retire underperforming models. How should you
   restructure that action, and why?
