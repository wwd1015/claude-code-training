---
name: lob-overlay
description: >
  Help a line-of-business (LOB) champion build and maintain their team-specific edition
  of the backbone training curriculum. Scaffolds an LOB workspace, anchors team demos,
  use cases, and policies onto backbone course modules, generates the team's edition of
  the self-paced and deck outputs, and re-syncs the edition when the central backbone
  version advances. Use when asked to "create an LOB version", "customize the training
  for <team>", "add our team's demos to the course", "sync our LOB material with the
  backbone", or "is our edition up to date".
---

# lob-overlay

You help an LOB champion maintain a **team edition** of the backbone curriculum.
The invariant that makes the whole system work: **LOB editions never modify
backbone files.** All team content lives in overlay files anchored to backbone
module IDs, so central updates flow in cleanly and team content survives them.

## Layout

- `backbone/` — central courses (read-only for this skill)
- `lob/_template/` — scaffold for a new LOB workspace
- `lob/<team>/lob.yaml` — team metadata + **pinned backbone versions** it was built against
- `lob/<team>/overlays/<course>/insert-map.yaml` — where each overlay slots in
- `lob/<team>/overlays/<course>/*.md` — the team content (demos, use cases, policies)
- `lob/<team>/generated/` — the team edition outputs; never hand-edit

`insert-map.yaml` entries anchor content to module IDs, not line numbers:

```yaml
inserts:
  - module: 301-02          # backbone module id (front-matter `id`)
    position: after-section "Design patterns"   # or: end-of-module | before-lab | replace-lab
    file: demos/backtest-report-walkthrough.md
    note: "team demo replacing the generic example"
```

Valid positions: `end-of-module`, `before-lab`, `after-section "<heading>"`,
`replace-lab` (the only *replace* allowed — labs are the sanctioned
customization point; backbone prose is never replaced, only supplemented).

## Modes

Infer from the request; default to **status** if unclear.

### init — create a new LOB workspace
1. Ask for (or take from the request): team name, champion, which courses they
   deliver, any known team use cases.
2. Copy `lob/_template/` → `lob/<team-slug>/`, fill `lob.yaml`, and pin each
   delivered course's `base_version` (under `courses:`) from the current
   `backbone/MANIFEST.yaml`.
3. Suggest 2–3 concrete overlay ideas based on what they told you about the
   team (e.g. their data sources → a 301 MCP demo; their recurring reports → a
   skill-creation lab).

### add — bring in team content
1. Read the material the champion provides (folder or files — demos, decks,
   notes, use-case writeups).
2. Propose anchor points: which backbone module each piece belongs to and at
   what position. Show the proposed `insert-map.yaml` additions before writing.
3. Write the content into `overlays/<course>/`, formatted to match backbone
   module voice, and update `insert-map.yaml`.
4. Team content that is actually **universally applicable** (nothing
   team-specific about it): recommend promoting it to the backbone via
   `/backbone-sync` instead of burying it in the overlay — put it in `intake/`
   if the champion agrees.

### generate — render the team edition
1. For each course in `lob.yaml`, produce the merged content: backbone modules
   + overlays applied at their anchors.
2. Render outputs per `templates/formats/TEMPLATE-CONTRACT.md` into
   `lob/<team>/generated/<course>/` — same formats as the backbone, with the
   team name in the title block ("CC 301 — <Team> Edition").
3. If a team template exists (`lob/<team>/templates/`), it wins over the
   central one; verify it declares the contract markers.
4. LOB editions are **not** published to `site/courses/` — that folder carries
   backbone outputs only. Point the team at `lob/<team>/generated/` directly
   (or the team hosts its own copy).

### sync — catch up with a backbone update
1. Compare each course's `base_version` in `lob.yaml` against the current
   `backbone/MANIFEST.yaml` versions. Nothing changed → report "up to date", stop.
2. For each drifted course, read the backbone `CHANGELOG.md` entries between
   the pinned and current versions and classify the impact on each overlay:
   - **clean** — anchors intact (MINOR/PATCH bumps usually) → re-apply.
   - **moved** — anchor module renumbered/renamed (MAJOR) → propose new anchor.
   - **conflict** — backbone now covers what the overlay adds, or contradicts
     it → show both side by side; champion decides keep / drop / rewrite.
3. Apply resolutions, update each `base_version` to current, regenerate the
   edition, and write a short entry to `lob/<team>/SYNC-LOG.md` (date, versions
   crossed, resolutions).

### status — report
Pinned vs current versions per course, overlay count per course, last sync,
last generate, and whether generated outputs are older than the overlays.

## Hard rules

1. Never write into `backbone/` — flag promotion candidates for `/backbone-sync` instead.
2. Never hand-edit `generated/` — regenerate.
3. Overlays supplement; only labs may be replaced.
4. Every sync decision that drops or rewrites champion content must be
   confirmed by the champion, not decided silently.
