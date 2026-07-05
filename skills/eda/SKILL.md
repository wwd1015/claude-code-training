---
name: eda
description: Run a standard exploratory data analysis pass on a dataset file (CSV/parquet) — shape, dtypes, null counts, per-column profiling, and a draft data dictionary. Use when the user says "eda", "profile this data", "explore this dataset", or points at a data file and asks what's in it.
---

# /eda — Exploratory data analysis pass

A starter skill for data scientists & quants. Install by copying this folder to
`.claude/skills/eda/` in any repo (or `~/.claude/skills/eda/` for all repos).

## What it does
Given a path to a CSV or parquet file, produce a consistent first-look profile and a draft
data dictionary — the same pass you'd otherwise retype every time.

## Steps
1. **Load** the file with pandas (use `pyarrow` for parquet). Report `shape`, `dtypes`, memory.
2. **Null/dup audit:** per-column null counts and %, duplicate-row count, constant columns.
3. **Profile each column:**
   - numeric → count, mean, std, min/max, quartiles, skew, and outliers (values beyond 3·IQR).
   - categorical/object → cardinality, top 10 values + frequencies, suspected IDs.
   - datetime-like → min/max range, gaps, monotonicity.
4. **Flag risks:** likely identifiers, leaked targets, mixed-type columns, high-cardinality
   categoricals, columns that are ~all null.
5. **Write `data_dictionary.md`** — one row per column: name, dtype, inferred description,
   example value, data-quality note. Tell the user these descriptions are drafts to review.
6. **Offer** to save a reusable `profile.py` that reproduces the pass on future extracts.

## Rules
- Actually run the code and report real numbers — never guess from the filename.
- Do not modify or move the data file. Read-only.
- Do not print values from columns that look like PII (names, emails, account IDs); summarize
  cardinality instead.
- Keep output skimmable: a short summary first, the full per-column table second.

## Example
```
/eda data/sample.parquet
```

See it taught live: [Demo 01 — EDA + data dictionary](../../demos/01-eda-data-dictionary.md).
Quant counterpart: [/regression-diagnostics](../regression-diagnostics/SKILL.md).
