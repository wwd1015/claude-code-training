# intake/ — source material drop folder

Drop any training material here (markdown, PDFs, exported decks, notes,
meeting transcripts, link lists), then run **`/backbone-sync`**. The skill will:

1. inventory what's new or changed (by content hash),
2. classify each section against the course routing rubric in `backbone/MANIFEST.yaml`,
3. merge only genuinely new/updated information into the backbone courses,
4. record provenance in each course's `sources.yaml`,
5. bump versions + changelogs and regenerate the course outputs.

Nothing here is ever silently dropped:

- `_unrouted/` — material the skill couldn't map to a course (with `NOTES.md` explaining why)
- `_lob-flagged/<team>/` — team-specific material that doesn't belong in the
  backbone; hand it to that team's champion for `/lob-overlay add`

Ingested files can be deleted from `intake/` afterwards — their hash and
disposition live in `sources.yaml`, so re-dropping the same file is a no-op.
