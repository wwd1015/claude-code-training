# lob/ — line-of-business editions

One directory per team, created and maintained with **`/lob-overlay`**.
LOB editions layer team-specific demos, use cases, and policies **on top of**
the backbone — they never modify `backbone/` files, so central updates flow in
cleanly via `/lob-overlay sync`.

```
lob/<team>/
  lob.yaml                  # team, champion, courses delivered, PINNED backbone versions
  overlays/<course>/
    insert-map.yaml         # anchors: which module, which position, which file
    *.md                    # the team content
  templates/                # optional team template override (must follow TEMPLATE-CONTRACT.md)
  generated/                # rendered team edition — never hand-edit
  SYNC-LOG.md               # history of backbone syncs and conflict resolutions
```

Start a new team with `/lob-overlay init` — it copies `_template/` and pins the
current backbone versions. See `.claude/skills/lob-overlay/SKILL.md` for the
full workflow (init / add / generate / sync / status).
