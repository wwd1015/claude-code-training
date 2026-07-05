# Backbone System — User Guide

How to *use* the backbone training system, by role. For how it's *designed*,
see [BACKBONE.md](../BACKBONE.md).

**Find your role:**

| You are… | You want to… | Go to |
|---|---|---|
| A **learner** | take the training | [§1](#1-learners-taking-the-training) |
| An **instructor / facilitator** | teach 301 or 401 with the decks | [§2](#2-instructors-teaching-with-the-decks) |
| An **LOB champion** | build your team's edition | [§3](#3-lob-champions-your-teams-edition) |
| A **backbone maintainer** | add/update central material | [§4](#4-maintainers-feeding-and-updating-the-backbone) |

The two skills (`/backbone-sync`, `/lob-overlay`) are project skills: they are
available whenever you run `claude` from the root of this repo. You talk to
them in plain English — the phrasings below are examples, not exact syntax.

---

## 1. Learners: taking the training

### Where the courses are

**One place: the entry site.** Open `site/index.html` (locally with
`open site/index.html`, or the GitHub Pages URL if the repo is hosted) and
every course is one click away — the site links the published copies in
`site/courses/`:

```
site/index.html            ← start here
site/courses/101.html      CC 101 — Foundations
site/courses/201.html      CC 201 — Make It Yours
site/courses/301.html      CC 301 — Skills, Hooks & MCP   (+ 301-deck.html)
site/courses/401.html      CC 401 — Agent Systems         (+ 401-deck.html)
site/courses/501.html      CC 501 — Capstone Studio
```

Each course is a single self-contained HTML page — any browser, no server or
install needed. (The canonical rendered outputs live in
`backbone/<course>/generated/`; the `site/courses/` files are identical
published copies.)

If your team has its own edition, use `lob/<your-team>/generated/` instead —
same courses, plus your team's demos and use cases.

### How to work through a course

1. Take courses **in order** (each lists its prerequisite at the top).
   101 → 201 are for everyone; 301 → 401 make you a builder; 501 is a team
   project, not a solo read.
2. Read a module, **do its Lab** (the green box — always on your own real
   work, that's the point), answer the knowledge check, then click
   **"Mark module complete."** The progress bar at the top tracks you.
3. Module 1 of CC 101 asks you to write down one recurring task from your own
   work. Keep it — the labs reuse it all the way to the 501 capstone.

**Progress tracking caveat:** progress is stored in your browser
(localStorage) — it survives restarts but doesn't follow you across browsers
or machines, and clearing site data erases it. Nothing is reported anywhere.

### Getting help

`/help` inside Claude Code · the [cheatsheet](cheatsheet.md) ·
[FAQ](faq.md) · your department's champion · office hours.

---

## 2. Instructors: teaching with the decks

CC 301 and CC 401 ship an instructor deck alongside the self-paced page:

```
backbone/301-extending/generated/deck.html
backbone/401-agent-systems/generated/deck.html
```

Open in a browser. Controls: **← / → / space** to navigate · **N** toggles
speaker notes (the distilled detail lives there — read them when preparing) ·
**F** fullscreen · click right/left half of the screen also advances/goes back.

How the pieces fit: the **deck** carries the talking points; the **self-paced
page** is the full text — assign it as pre-work or follow-up; the **labs** in
the deck are the same labs as in the self-paced page, so learners can catch up
if they miss a session. For cohort logistics (comms templates, session
runbook), see the [facilitator guide](facilitator-guide.md).

If a deck looks stale (a module changed but the deck didn't), tell the
maintainer or run: `claude` → *"/backbone-sync regenerate 301"*.

---

## 3. LOB champions: your team's edition

Your team's edition = the backbone + your overlays (demos, use cases,
policies). You **never edit backbone files** — that's what makes central
updates painless. Everything below happens by running `claude` at the repo
root and talking to `/lob-overlay`.

### 3.1 Create your workspace (once)

> "Use /lob-overlay to set up an edition for the **Rates Research** team.
> Champion is me (Alan). We deliver 101–301. Our recurring pain points:
> weekly risk report, model validation memos."

You get `lob/rates-research/` with `lob.yaml` pinned to today's backbone
versions, plus 2–3 suggested overlay ideas based on what you told it.

### 3.2 Add your team's content

Put your material anywhere (a folder of demo writeups, an existing deck,
rough notes) and:

> "/lob-overlay add — here's our folder `~/rates-demos/`. Attach the
> backtest walkthrough to the skill-creation module and make our weekly
> report the lab."

The skill proposes **anchor points** (which backbone module, what position)
before writing anything. Positions you can ask for:

- `end-of-module` — append your example after the backbone content
- `before-lab` — slot in just before the lab
- `after-section "<heading>"` — insert below a specific heading
- `replace-lab` — swap the generic lab for your team-native one
  (**labs are the only thing you may replace**; backbone prose is only ever
  supplemented)

If something you add is actually universal (nothing team-specific about it),
the skill will suggest promoting it to the backbone instead — say yes and it
goes to `intake/` for the maintainer.

### 3.3 Generate your edition

> "/lob-overlay generate"

Renders `lob/<team>/generated/<course>/…` — same formats as the backbone,
titled "*CC 301 — Rates Research Edition*". Point your team at these instead
of the central files. Optional: drop a team-branded template into
`lob/<team>/templates/` (it must follow the
[template contract](../templates/formats/TEMPLATE-CONTRACT.md)) and it wins
over the central one.

### 3.4 When the backbone updates

You'll hear "backbone 301 is now v1.2.0" (or notice it in
`backbone/MANIFEST.yaml`). Run:

> "/lob-overlay sync"

It reads the changelogs between your pinned version and current, re-applies
your overlays, and walks you through anything that needs a decision:
**clean** (re-applied automatically) · **moved** (a module was renumbered —
it proposes the new anchor) · **conflict** (backbone now covers or
contradicts your overlay — you choose keep / drop / rewrite; it never decides
silently). Then it re-pins your versions, regenerates, and logs the sync in
`SYNC-LOG.md`.

**Check where you stand any time:** "/lob-overlay status".

---

## 4. Maintainers: feeding and updating the backbone

You own the central material. The workflow is: **drop → sync → review → done**.

### 4.1 Ingest new material

1. Drop anything into `intake/` — markdown, PDFs, exported decks, meeting
   notes, link lists. (Internal training material, new Anthropic docs, a
   good conference talk writeup — all fine.)
2. Run `claude` at the repo root:

   > "/backbone-sync — ingest what's in intake/"

3. What it does, in order (you see each step):
   - **Inventory** — lists what's new/changed (by content hash; re-dropping
     an already-ingested file is a no-op).
   - **Classify** — routes each *section* to a course using the rubric in
     `backbone/MANIFEST.yaml`. One deck can feed three courses.
   - **Diff** — for each routed section: NEW (backbone doesn't cover it),
     UPDATED (supersedes what's there), or DUPLICATE (already covered).
   - **Merge plan** — anything touching more than ~3 modules, or replacing
     content, is shown to you as a table **before** it's applied.
   - **Merge + provenance** — edits the modules, records every source in
     the course's `sources.yaml`.
   - **Version + changelog** — PATCH (fixes) / MINOR (new info or module) /
     MAJOR (restructure — breaks LOB anchors, called out loudly).
   - **Regenerate** — re-renders `generated/` for every course that changed.
4. Read the final report. Two folders to check afterwards:
   - `intake/_unrouted/` — material it couldn't place (with notes). Either
     tell it where it goes or discard.
   - `intake/_lob-flagged/<team>/` — team-specific material that doesn't
     belong in the backbone. Forward it to that team's champion.
5. If any course got a **MAJOR** bump, tell the champions to run
   "/lob-overlay sync" (the report reminds you who's affected).

You can delete ingested files from `intake/` afterwards — their hashes live
in `sources.yaml`.

### 4.2 Other maintainer moves

- **Rebuild outputs only** (after a template tweak, no new content):
  > "/backbone-sync regenerate all"

  This also refreshes the published copies in `site/courses/` so the entry
  site serves the new version.
- **Health check** (versions, pending intake, stale outputs):
  > "/backbone-sync status"
- **Use a different output template**: replace or add a template under
  `templates/formats/` following the
  [template contract](../templates/formats/TEMPLATE-CONTRACT.md) — tokens
  like `{{COURSE_TITLE}}` plus `BB:MODULE`/`BB:SLIDE` example blocks — then
  regenerate. This is how you'll swap in the company deck format later.
- **Fix a typo**: edit the module in `backbone/<course>/modules/`, bump PATCH
  in `course.yaml` **and** `MANIFEST.yaml`, add a changelog line, regenerate.
  (Or just ask `/backbone-sync` to do exactly that.)

### 4.3 Rules that keep the system healthy

1. **Never hand-edit `generated/` or `site/courses/`** — both get overwritten.
   Fix the module or the template, then regenerate (which republishes).
2. **Backbone = universal only.** If it names a team, a department, or an
   internal system, it belongs in an LOB overlay (or gets an anonymized,
   generalized version in the backbone).
3. **Watch the `<!-- verify -->` markers** — they mark org-specific gaps
   (install channel, data policy links, support channels) and facts added
   from model memory rather than a source. Filling them via `intake/` drops
   is the highest-value early maintenance.

---

## 5. FAQ / troubleshooting

**The skills don't show up when I type `/`.**
You must run `claude` from the repo root (the skills are project-scoped,
in `.claude/skills/`). To use them from anywhere, symlink each skill dir to
`~/.claude/skills/` — flat, one level: `~/.claude/skills/backbone-sync/`.

**My course progress disappeared.**
Progress is per-browser localStorage. Different browser/machine or cleared
site data = fresh progress. It's a checklist, not a transcript of record.

**I edited `generated/self-paced.html` and my change vanished.**
Expected — generated files are overwritten on every regenerate. Put the
change in the module (content) or the template (styling) instead.

**A learner found an error in a course.**
Tell the maintainer, or fix it yourself: edit the module, PATCH-bump, ask
`/backbone-sync` to regenerate. LOB copies pick it up on next sync.

**How do I add our internal/company training material?**
Drop it in `intake/` and run `/backbone-sync`. Universal parts merge into the
backbone (with provenance); team-specific parts get flagged to the right LOB.
⚠️ If this repo is public, keep genuinely internal material out of it —
host a private fork/mirror first.

**Where do working groups (CC 501) get their materials?**
The 501 self-paced page is the working-group handbook: the operating model,
the project-selection rubric, the design-doc skeleton, and the review
checklist are all in its modules.

**Who updates what?**

| Content | Owner | Tool |
|---|---|---|
| Backbone modules & versions | maintainer | `/backbone-sync` |
| Format templates | maintainer | edit + `regenerate` |
| Team overlays & editions | LOB champion | `/lob-overlay` |
| `generated/` + `site/courses/` | nobody | always regenerated |
| Entry site (`site/index.html`) | maintainer | edit by hand (it's not generated) |
