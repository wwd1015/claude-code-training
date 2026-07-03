# Template contract

How `/backbone-sync` and `/lob-overlay` turn course modules into `generated/`
outputs. Any template (central or user-supplied) must follow this contract.
Generation is done by Claude following these rules — templates are patterns to
instantiate, not code that executes.

## Tokens

Simple `{{TOKEN}}` string replacements, allowed anywhere in a template:

| Token | Value |
|---|---|
| `{{COURSE_ID}}` | e.g. `CC 301` |
| `{{COURSE_TITLE}}` | full title from `course.yaml` |
| `{{COURSE_VERSION}}` | e.g. `1.2.0` |
| `{{EDITION}}` | `Backbone` or the LOB team name |
| `{{GENERATED_DATE}}` | ISO date of generation |
| `{{MODULE_COUNT}}` | number of modules |
| `{{TOTAL_DURATION}}` | sum of module durations |

## Repeating blocks

A template marks each repeating region with paired comments containing ONE
example instance. The generator replaces the whole region with N instances —
one per module (or per slide) — following the example's exact markup:

```html
<!-- BB:MODULE:BEGIN -->
  ...one fully-worked example module section...
<!-- BB:MODULE:END -->
```

Block types a template may declare:

- `BB:NAV` — one entry per module (table of contents / progress list)
- `BB:MODULE` — one section per module (self-paced format)
- `BB:SLIDE` — one slide per unit (deck format; see slide mapping below)

Inside a block, per-item tokens are available: `{{MODULE_ID}}`,
`{{MODULE_NUM}}`, `{{MODULE_TITLE}}`, `{{MODULE_DURATION}}`,
`{{MODULE_OBJECTIVES}}` (render as list items), `{{MODULE_BODY}}` (module
markdown rendered to HTML), `{{MODULE_ANCHOR}}` (slug for ids/links).

## Content mapping rules

**Self-paced** (`self-paced.html`): every module in `course.yaml` order, full
body. Preserve the module's own headings one level down from the module title.
Labs and knowledge checks stay inside their module section, visually distinct
(the template shows how). Keep all links; external links open in a new tab.

**Deck** (`deck.html`): decks are teaching aids, not documents. Per module:
1. one section-title slide (module title + objectives),
2. 2–5 content slides — distill the body to talking points (≤ 6 bullets or one
   diagram/code block per slide; split rather than shrink),
3. one lab slide if the module has a Lab.
Course-level: one title slide first, one "agenda" slide (from BB:NAV data),
one closing slide (next course + where to get help). Speaker notes: put the
distilled-away detail into the template's notes mechanism if it has one.

**Working group** (CC 501): no rendered artifact is defined yet — the course's
self-paced output serves as the group's handbook. If a kickoff one-pager format
is added later, it gets its own block type here first.

**LOB editions**: identical rules on the merged (backbone + overlay) content;
`{{EDITION}}` = team name; overlay-sourced sections get the template's
`edition-badge` treatment if it defines one.

## Rules for generators

1. Do not restyle, add, or remove template CSS/JS — only instantiate tokens and blocks.
2. Do not summarize module content in self-paced output — it is the full text.
3. Escape user content properly; module markdown → semantic HTML (h3/h4, p, ul, pre>code, table).
4. Output is a single self-contained file — no external requests (fonts, CDNs, images); inline everything.
5. Write to `generated/` only, and stamp `{{GENERATED_DATE}}` honestly.

## Validating a user-supplied template

Before first use, check: at least one of `BB:MODULE`/`BB:SLIDE` declared, the
example instance parses, tokens spelled as above. If markers are missing, map
the template's evident structure onto this contract, state the assumptions you
made, and proceed — do not silently guess twice on the same template; ask.
