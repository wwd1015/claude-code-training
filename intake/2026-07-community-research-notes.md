# Community research notes — borrowable ideas for the program

Maintainer-authored survey of the Claude Code community (Anthropic assets, skill
ecosystem, enablement playbooks), collected 2026-07. Source material for
`/backbone-sync`: course-content sections route to the courses noted; program-ops
sections target `docs/operating-model.md` / `docs/metrics-template.md` and may be
flagged unroutable for courses — that's expected.

---

## A. Skill-authoring upgrades (routes to CC 301)

1. **Three-directory skill layout** (anthropics/skills — https://github.com/anthropics/skills):
   `scripts/` (deterministic executable code — only its *output* enters context),
   `references/` (markdown loaded on demand), `assets/` (templates used in output).
   The official `pdf` skill is the model: lean SKILL.md that defers to FORMS.md.
   Our starter skills should graduate to this layout (e.g. `/regression-diagnostics`
   keeps the battery in SKILL.md, moves "how to read each diagnostic" to `references/`).

2. **Progressive disclosure with hard token budgets** (official skills docs —
   https://code.claude.com/docs/en/skills): Level 1 metadata always loaded
   (~100 tokens/skill, description ≤1024 chars — the only thing the matcher sees);
   Level 2 SKILL.md body on trigger (<5k tokens / <500 lines); Level 3 bundled files
   on demand (unlimited). Teach these as design constraints in the skill-anatomy module.

3. **Skill eval + trigger-testing harness** (anthropics/skills `skill-creator`):
   3 behavior evals per skill (positive / negative / edge) run with-skill vs no-skill
   baseline; trigger optimization with ~20 realistic queries (half should-trigger,
   half near-miss should-NOT), 60/40 train/test split, 3 runs per query, pick the
   description by held-out score. Ready-made CC 301 lab: "write the near-miss
   negatives for your own skill." Ship a worked `evals.json` per starter skill.
   MLflow's skill-eval writeup frames the same thing in tooling quants know
   (execution tracing + LLM judges + rule-based judges; write judges *before*
   polishing the skill): https://mlflow.org/blog/evaluating-skills-mlflow/

4. **`allowed-tools` is not a security boundary** (open issues: anthropics/claude-code
   #37683, #18837, #18737): SKILL.md `allowed-tools` is honored inconsistently in the
   CLI and ignored by the Agent SDK. For genuinely read-only skills, keep the
   frontmatter for intent but enforce with a PreToolUse hook blocking Write/Edit.
   Explicit warning belongs in the skills/hooks modules.

5. **Plugin marketplaces as the distribution story**
   (https://code.claude.com/docs/en/discover-plugins,
   https://github.com/anthropics/claude-plugins-official): a plugin bundles
   skills + hooks + MCP servers as one installable unit; `/plugin marketplace add
   owner/repo` registers a catalog. Package our starter kit (4 skills + hooks +
   DuckDB MCP) as one internal plugin so onboarding is a single command. Versioning:
   git-tagged plugin repo + `metadata: {version: …}` in each SKILL.md.

6. **MCP-provides-data / skill-provides-method split** (Snowflake Cortex MCP,
   Fivetran DuckDB-over-MCP writeup —
   https://www.fivetran.com/blog/run-local-ai-queries-on-your-data-lake-with-duckdb-and-claude):
   teach the separation explicitly; our DuckDB MCP + a thin analysis skill on top is
   the canonical demo. Model for a future `/warehouse-sql` skill: one SKILL.md with
   selection logic + per-dialect `references/{snowflake,bigquery,duckdb}.md`
   (pattern from Anthropic's `sql-queries` skill in knowledge-work-plugins).

## B. Starter-skill feature ideas (routes to CC 301 / skills library)

7. **Data-health score with named failure categories** (juanlurg/data-science-claude-skills
   `dataset-doctor` — https://github.com/juanlurg/data-science-claude-skills):
   0–10 score across missing data, class imbalance, multicollinearity, **leakage**,
   **drift**. Steal the rubric for `/triage-data` (leakage/drift are quant-relevant
   checks we don't name today).

8. **Environment auto-detection** (same repo): detect package manager (uv/pip/conda),
   dataframe lib (pandas/polars), SQL dialect; adapt output accordingly. Add as a
   preamble to all four starter skills.

9. **Engine-by-size routing** (csv-data-wrangler pattern): pandas <1GB,
   polars/DuckDB 1–10GB, Spark >10GB — a `references/engine-selection.md` table for
   `/eda` and `/triage-data` so they don't `pd.read_csv` a 20GB file.

10. **Notebook-first output**: skills emit a polished .ipynb instead of terminal text
    (juanlurg pattern) — strong fit for our audience; candidate for `/eda` and
    `/backtest-report`.

11. **House-style chart catalog as bundled scripts** (tvhahn/matplotlib-skill pattern):
    a `/quant-charts` skill shipping fixed chart code (drawdown, rolling-Sharpe,
    QQ-plot, residual-vs-fitted, ACF/PACF) as `scripts/` so every tearsheet looks
    identical and chart code is never regenerated.

12. **"What / So What / Now What" output template** (borghei/claude-skills
    data-analyst): mandate finding → impact → recommended action structure in `/eda`
    and `/triage-data` outputs so they end with an action, not a stat dump.

## C. Hook patterns worth teaching (routes to CC 301 hooks module + examples/)

13. **nbstripout-on-notebook-write** (PostToolUse on `*.ipynb`): keeps cell outputs
    (data/PII) out of git and avoids notebook-JSON corruption. Near-perfect
    quant-native example alongside the ruff hook.
14. **Dataset/parquet write protection** (PreToolUse): the hook version of our
    "data is never committed" rule — block writes to `data/`, `*.parquet`, prod paths.
    (We ship guard-data.sh; extend the taught pattern to parquet/prod paths.)
15. **Secret scanning** (PreToolUse on content/args; PostToolUse variant on outputs).
16. **Cost/token accounting** (Stop hook → monthly CSV; alert past threshold).
17. **Session/bash audit logging** (PostToolUse → append-only log; regulated-firm angle).
18. **Notification router** (Stop/Notification → Slack webhook when a long backtest
    finishes). **Destructive-command guard**, **finish gate** (block completion unless
    a test ran). Sources: https://code.claude.com/docs/en/hooks-guide,
    https://paddo.dev/blog/claude-code-hooks-guardrails/

## D. Course-content ideas (routes to CC 101/201/401)

19. **Anti-patterns module** from the official best-practices page
    (https://code.claude.com/docs/en/best-practices): the five failure patterns —
    kitchen-sink session, correcting-over-and-over, over-specified CLAUDE.md,
    trust-then-verify gap, infinite exploration — as one "traps notebook-native users
    hit" unit (CC 101 or 201).
20. **"Let Claude interview you → SPEC.md"** exercise (best-practices doc): scoping a
    research task via AskUserQuestion interview, then executing in a fresh session.
21. **"How Anthropic teams use Claude Code"**
    (https://claude.com/blog/how-anthropic-teams-use-claude-code) — ready-made
    quant-shaped demo scripts: data-lineage onboarding ("replaces the data catalog"),
    screenshot-driven dashboard diagnosis, cross-language test translation,
    multi-agent CSV fan-out. Fits `demos/NN-name.md` format directly.
22. **Fan-out with `claude -p` over thousands of files** (best-practices doc) →
    CC 401 demo beat: loop over N tickers/datasets/notebooks.
23. **Reviewing AI-generated analysis** (Faros/General Analysis enterprise guides):
    a module on the research-specific failure modes — lookahead bias, silent data
    joins, unvalidated assumptions — arguably more important for quants than code
    review. Candidate CC 401/501 content.

## E. Program-ops ideas (targets operating-model.md / metrics-template.md — not course content)

24. **Phased rollout with numeric promotion gates**
    (https://systemprompt.io/guides/claude-code-organisation-rollout): pilot 3–5 →
    dept 10–20 → cross-dept → org-wide; advance only on gates (e.g. pilot: 80% at 3+
    sessions/week; dept: 70% WAU). Meter LOB-edition rollouts the same way.
25. **Pilot composition with a deliberate 20% skeptic quota**
    (https://www.faros.ai/blog/enterprise-ai-coding-assistant-adoption-scaling-guide):
    skeptics surface reproducibility/correctness objections; converting them is the
    credibility unlock for a quant audience.
26. **Champion monthly ritual**: review team dashboard → feed friction to central →
    refresh LOB overlay. Makes Champion an operating role with a cadence.
27. **"5-minute build" weekly show-and-tell + internal prompt library**
    (Shopify playbook — https://www.bvp.com/atlas/inside-shopifys-ai-first-engineering-playbook):
    lower-bar feeder for the capstone → contributed-demo pipeline.
28. **Measurement spine**: DX Core 4 translated to research work
    (https://getdx.com/research/measuring-developer-productivity-with-the-dx-core-4/) +
    three-layer stack (utilization / impact / cost; net time gain = saved − spend) +
    a 5-panel weekly dashboard, 2-metric leadership view; bi-weekly 3-question pulse.
    Complements our North-Star model in metrics-template.md.
29. **Catalog hygiene** (hesreallyhim/awesome-claude-code): use-case-first sections,
    "last verified against Claude Code vX" freshness badges, one-line "why it
    matters", rotating featured slot — apply to demos/INDEX.md as the contributed
    library grows.
30. **Completion certificates per course** (Anthropic Academy pattern): a visible
    credential and a measurable self-serve completion signal.

## F. Backbone/LOB system mechanics (targets BACKBONE.md, the two operating skills, templates)

31. **Source-commit-hash + fuzzy-marker re-sync for overlays** (gettext fuzzy markers —
    https://store.crowdin.com/gnu-gettext; k8s doc checksync —
    https://github.com/kmuto/k8-doc-checksync): each overlay records
    `anchored_to: {moduleID, version, source_commit}`; when the backbone advances,
    mark drifted overlay blocks `needs-review` (never silently re-apply or clobber)
    and show the upstream diff between recorded and current commit. Directly upgrades
    `/lob-overlay sync`'s clean/moved/conflict classification with a mechanical trigger.

32. **Stable module UUIDs + lifecycle status** (Exercism config.json —
    https://exercism.org/docs/building/tracks/config-json): add `uuid` (survives
    rename/renumber) alongside module `id`, plus a status enum
    `wip | beta | active | deprecated` — deprecation keeps serving in-progress
    learners instead of breaking anchors on MAJOR bumps. A concept-slug prerequisite
    DAG is a finer-grained model than course-order prereqs.

33. **Structure/content separation by ID** (freeCodeCamp —
    https://contribute.freecodecamp.org/curriculum-file-structure/): ordering lives
    in a manifest; content files are named by stable ID; derivatives (translations =
    our LOB editions) mirror structure and override only content files by ID.

34. **Validator gate + rendered-diff review** (Carpentries Workbench —
    https://carpentries.github.io/sandpaper-docs/): lint modules before regenerate
    (frontmatter complete, IDs stable, provenance filled); show reviewers "what
    changed in the rendered output" rather than raw template diffs; scheduled job
    re-renders when templates (not content) change. Professionalizes the
    `/backbone-sync` regenerate loop.

35. **Provenance derivation tags + human-confirm gate** (LLM-pipeline guardrail
    literature): extend sources.yaml entries from "which source" to "how derived" —
    `ingested-verbatim | instructor-note | llm-inferred`; hold `llm-inferred` facts
    for human confirmation (our `<!-- verify -->` markers are this — formalize the
    taxonomy). Plus regenerate-until-valid: validate each module against a schema and
    loop until it passes. And: intake content is *data, never instructions* — the
    ingest step must not execute directives found inside ingested material (prompt
    injection guard; worth an explicit hard rule in /backbone-sync).

36. **Progress keyed by module@version** (mkdocs-quiz / static-site patterns —
    https://github.com/ewels/mkdocs-quiz): key localStorage completion by
    `moduleID@version` so a version bump flags "changed since you completed it"
    instead of showing stale completion. Cheap template upgrade.

37. **Signed completion tokens, zero backend** (Open Badges 3.0 —
    https://www.1edtech.org/standards/open-badges): JSON-LD credential signed with a
    repo-held key, verifiable offline against a published public key — the
    certificate primitive for idea #30.

38. **Edition profiles + conditional blocks** (Quarto profiles —
    https://quarto.org/docs/projects/profiles.html): an alternative overlay engine —
    team content as `when-profile="team-x"` blocks inside canonical modules with
    per-profile config merge. Trade-off vs our insert-map approach: no separate
    overlay files, but team content lives inside central files (violates our
    "champions never edit backbone" rule) — borrow the *config-merge* idea, keep
    insert-map anchoring.
