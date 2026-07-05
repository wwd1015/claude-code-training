---
id: 201-02
title: "Settings & the Configuration Hierarchy"
duration: 35 min
objectives:
  - Locate the three settings.json levels and state their precedence
  - Decide where a given setting belongs (user, project, or local)
  - Inspect and change configuration with /config
  - Check the right settings file into git and keep the rest out
---

## Three files, one hierarchy

Claude Code reads settings from three places, most specific wins:

| Level | File | Committed? | For |
|---|---|---|---|
| User | `~/.claude/settings.json` | no (personal) | your defaults, everywhere |
| Project | `.claude/settings.json` | yes (shared) | team standards for this repo |
| Local | `.claude/settings.local.json` | no (gitignored) | your overrides for this repo |

The pattern to internalize mirrors CLAUDE.md scoping: **team truths in the
project file, personal taste in the user file, machine-specific quirks in
local.** Settings cover permissions (next module), environment variables,
model choice, hooks (CC 301), and more — the full schema is in the docs.

Precedence runs local → project → user: `settings.local.json` overrides
`.claude/settings.json`, which overrides `~/.claude/settings.json`. Managed
environments can add an enterprise policy layer that sits *above* all three and
cannot be overridden locally — if a setting refuses to budge, that is the usual
reason. <!-- verify: enterprise managed settings path/precedence for your org -->

## Environment variables

The `env` block in settings.json sets environment variables for every session
in that scope — the clean way to pin `PYTHONPATH`, data directories, or proxy
settings so you never debug "works in my terminal, not in Claude's" again.

Scope it the way you scope everything else. A `DATA_DIR` the whole desk shares
goes in the project file so every clone agrees. A path that only exists on your
machine (a scratch SSD, a personal cache) goes in `settings.local.json` so you
don't break anyone else by committing it.

## /config and friends

Inside a session, `/config` shows and edits current configuration without
hunting for files. When behavior surprises you, the diagnostic question is
always: *which level is supplying this setting?* — check project and local
before assuming your user defaults apply.

## Worked example: pinning a warehouse connection so every session agrees

Your team's SQL and feature scripts read `WAREHOUSE_DSN` from the environment.
Half the desk has it in their shell profile, half don't, and Claude sessions
fail intermittently with "env var not set." Fix it in the shared scope.

**Project `.claude/settings.json`:**

```json
{
  "env": {
    "WAREHOUSE_DSN": "warehouse.internal:5439/analytics",
    "PYTHONPATH": "src"
  }
}
```

Commit it. Now every clone runs analysis scripts against the same warehouse
without anyone editing a dotfile. One quant works off a read-replica for heavy
scans; that path is personal, so it goes in *their* `settings.local.json`,
which the hierarchy lets win locally:

```json
{
  "env": { "WAREHOUSE_DSN": "replica.internal:5439/analytics" }
}
```

**How you verify:** in a fresh session, ask Claude to `echo $WAREHOUSE_DSN`. On
a plain clone it prints the shared DSN; on the replica user's machine it prints
the override. If it prints nothing, the setting is in a scope that session
isn't reading — check that the file is where you think it is and valid JSON.

### Best practices

- **Check the project file into git; keep the rest out.** `.claude/settings.json`
  is a team artifact — review it in PRs like any config. `.claude/settings.local.json`
  belongs in `.gitignore` (Claude Code adds it for you) so personal overrides
  never travel.
- **Push a setting to the narrowest scope that needs it.** A value only you need
  does not belong in the shared file, and a team standard does not belong buried
  in your user settings where nobody else gets it.
- **Pin environment through `env`, not dotfiles.** A `.zshrc` export works on
  your box and nowhere else. The `env` block makes the dependency explicit and
  reproducible for everyone who reads the repo.
- **Keep JSON valid — a syntax error drops the whole file.** One trailing comma
  and none of that scope's settings load. When config "isn't taking," validate
  the JSON first.
- **Diagnose by scope, not by guessing.** Surprising behavior is almost always a
  more-specific file overriding a less-specific one. Read local, then project,
  then user, in that order.

### Common pitfalls

**You edit `~/.claude/settings.json` to fix a repo problem.** It works for you
and no one else, and now the repo behaves differently on your machine. Fix: put
repo behavior in the repo's `.claude/settings.json`.

**You commit `settings.local.json`.** Your machine-specific paths and personal
overrides land in everyone's clone. Fix: confirm it is gitignored; move anything
truly shared up to the project file.

**You expect a shell export to reach Claude's sessions.** Environment you set in
your terminal isn't guaranteed to be what a session runs with. Fix: declare it
in the `env` block at the right scope.

**You assume your user defaults are in effect.** A committed project setting is
silently overriding them, and you burn twenty minutes confused. Fix: `/config`,
and read the hierarchy top-down.

**For quants:** your dependencies are often licensed engines and data paths (a
solver seat, a Bloomberg/tick path, an R/MATLAB runtime). Pin those in the
right scope so a session doesn't silently fall back to a different install.

**For data scientists:** yours are often compute and framework knobs
(`CUDA_VISIBLE_DEVICES`, a cache dir, a cluster endpoint). Keep the shared ones
in the project file so a teammate's session doesn't grab the wrong GPU or
re-download a 20 GB dataset to the wrong disk.

**Reuse (official):** [Settings docs](https://code.claude.com/docs/en/settings)

## Lab

In your working repo: (1) run `/config` and identify one setting at each
level; (2) add an `env` variable your analysis scripts need to the project
settings; (3) override it in `settings.local.json` and confirm which one a
fresh session sees (ask Claude to `echo` it).

**Stretch:** open the committed `.claude/settings.json` and read it as a
teammate cloning fresh would. Is there anything in it that is actually personal
(a local path, your model preference)? Move it to the right scope and leave the
shared file as clean team policy.

## Knowledge check

1. A setting appears in all three files with different values — which wins?
2. Your team wants everyone's sessions to use the same data directory env var. Which file, and why that one?
3. Why does `settings.local.json` exist at all, given user settings are already personal?
4. A setting won't change no matter what you edit. What are the first two things you check?
5. A teammate says "I set `PYTHONPATH` in my `.zshrc` but Claude still can't import our package." What do you tell them to do instead?
