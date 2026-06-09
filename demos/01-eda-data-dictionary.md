# Demo 01 — EDA + data dictionary on an unfamiliar dataset

> **Demo script template** (all demos follow this): Objective · Setup · Live script ·
> Talking points · Take-home · Time.

**Track:** 1 (Daily-driver fundamentals) · **Time:** ~15 min live

## Objective
Show that Claude Code reads a whole dataset/repo and runs your code — it's a pair-researcher,
not autocomplete. Turn a messy unfamiliar CSV/parquet into a documented, profiled dataset.

## Setup (zero infra)
- **Generate the data:** `cd demos/setup && pip install -r requirements.txt && python gen_sample_dataset.py` → writes `data/sample.parquet` (a messy dataset with seeded nulls, outliers, a high-cardinality column, and a leaked target). Or bring a real de-identified extract.
- Open Claude Code in a fresh empty folder containing only that file.
- A Python env with `pandas` (and `pyarrow` for parquet). That's it.

## Live script (what to type)
1. `What's in data/sample.parquet? Load it and give me shape, dtypes, null counts, and 5 sample rows.`
2. `Profile every column: for numerics give distribution summary + outliers; for categoricals give cardinality and top values; flag anything that looks like an ID, date, or leaked target.`
3. `Write a data_dictionary.md: one row per column with name, dtype, description (infer it), example, and a data-quality note.`
4. `Now write profile.py that reproduces all of this so I can rerun it on next month's extract.`
5. (If time) `Plot the 3 most interesting distributions and save them to figs/.`

## Talking points
- It **ran the code** to get real null counts — not guesses.
- Plan mode (`shift+tab`) before step 4 to review what it'll write.
- The output (`data_dictionary.md` + `profile.py`) is reusable real work, not a toy.
- Note it inferred descriptions — review them; this is a draft, you're the domain expert.

## Take-home exercise
Point Claude Code at one of *your own* datasets/notebooks. Ask it to generate a data
dictionary and a reusable `profile.py`. Bring the diff to office hours.

## Time
15 min live + 20 min take-home.
