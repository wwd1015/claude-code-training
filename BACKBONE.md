# The Backbone System

The **backbone** is the centralized, versioned copy of the Claude Code training
curriculum, organized as numbered courses (101 → 501) like a college catalog.
It is the single source of truth that every delivery format and every
line-of-business (LOB) edition derives from.

> **Looking for how to *use* the system** (take a course, teach a session,
> build a team edition, ingest material)? That's the
> [user guide](docs/backbone-user-guide.md). This document is the design.

This layer sits on top of the existing track-based curriculum in
[docs/curriculum.md](docs/curriculum.md) — the tracks map 1:1 onto courses
(Track 0+1 → 101, Track 2 → 201, Track 3 → 301+401, Track 4 → 501). The
existing `docs/`, `demos/`, and `skills/` content is **source material** that
feeds the backbone through the ingest pipeline.

---

## Operating model

```
                       ┌─────────────────────────────┐
   source material     │        BACKBONE (this)      │      delivery formats
                       │                             │
  Anthropic docs ───►  │  101 Foundations            │  ──► self-paced site (all)
  Academy courses ──►  │  201 Customization          │  ──► instructor decks (301/401)
  eng blog / repos ─►  │  301 Skills · Hooks · MCP   │  ──► working groups   (501)
  internal decks ───►  │  401 Agent Systems          │
  intake/ drop-folder  │  501 Capstone Studio        │
                       └──────────────┬──────────────┘
        /backbone-sync ▲              │ /lob-overlay
        (ingest+build) │              ▼
                       │        LOB editions
                       │   backbone + team demos,
                       │   use cases, data policies
```

**Universally applicable core, locally compensated.** The backbone contains
only material that works for every team. Each LOB champion layers their own
demos, use cases, and policies on top via `/lob-overlay` — they never edit
backbone files, so central updates flow cleanly.

## The three delivery formats

| Format | Courses | Output | Operated by |
|---|---|---|---|
| **Self-paced site** | 101–501 (all) | `generated/self-paced.html` per course, with progress tracking | Central; baseline for everyone |
| **Instructor-led training** | 301, 401 (primarily) | `generated/deck.html` per course | Champions / central experts |
| **Working groups** | 501 | Capstone briefs + review cadence | Teams themselves, expert support; goal is recruiting flagship projects |

## Directory layout

```
backbone/
  MANIFEST.yaml            # course registry: versions, routing rubric, format targets
  101-foundations/
    course.yaml            # metadata: title, audience, prereqs, formats, module list
    modules/NN-slug.md     # canonical content, one file per module
    sources.yaml           # provenance: every ingested source file, hash, disposition
    CHANGELOG.md           # human-readable version history
    generated/             # rendered outputs (self-paced.html, deck.html) — never hand-edit
  201-customization/ … 501-capstone/   # same shape
templates/formats/         # HTML templates + TEMPLATE-CONTRACT.md
intake/                    # drop folder for new source material to ingest
lob/                       # LOB editions (one dir per team) + _template scaffold
.claude/skills/
  backbone-sync/           # ingest → classify → diff → merge → regenerate
  lob-overlay/             # LOB init / add / generate / sync
```

## The two skills

### `/backbone-sync` — build and maintain the backbone
Drop any material into `intake/` (decks, docs, notes, transcripts, links) and run it.
It classifies content against the routing rubric in `MANIFEST.yaml`, diffs against
what each course already says, merges only **new or updated** information into the
canonical modules (with provenance in `sources.yaml`), bumps course versions,
writes changelogs, and regenerates the self-paced + deck outputs from the
templates. Also handles pure rebuilds (`regenerate`) when only templates change.

### `/lob-overlay` — LOB champion editions
Scaffolds an LOB workspace under `lob/<team>/`, anchors team-specific overlays
(demos, use cases, policies) to backbone module IDs via `insert-map.yaml`,
generates the team's edition of the outputs, and — when the backbone version
advances — re-syncs the edition, re-applying overlays and flagging conflicts.

## Versioning rules

- Each course carries `version: MAJOR.MINOR.PATCH` in `course.yaml`.
  - **PATCH** — corrections, link fixes, wording.
  - **MINOR** — new information merged into existing modules, or a new module.
  - **MAJOR** — module restructure, renumbering, or removal (breaks LOB anchors).
- Every version bump gets a `CHANGELOG.md` entry saying *what changed and from which source*.
- `backbone/MANIFEST.yaml` mirrors the current version of every course — LOB
  editions pin the versions they were built against and diff against this file.

## Ground rules

1. **Generated files are never hand-edited.** Fix the module or the template, regenerate.
2. **Backbone content must be universally applicable.** Team-specific material belongs in an LOB overlay.
3. **Every merged fact keeps provenance** (`sources.yaml`) so internal material can be audited or pulled later.
4. **Reuse first** (unchanged from the curriculum): official Anthropic material carries the conceptual load; modules link out rather than paraphrase at length.
