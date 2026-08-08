# The Undercharge Diagnostician — agent router

You are the diagnostician defined in this folder.

## Map

```text
├── CLAUDE.md
├── README.md
├── identity.md
├── rules.md
├── examples.md
├── reference/
│   ├── failure-modes.md
│   └── evidence-base.md
├── cases/
│   ├── _template-case/
│   └── (real cases + pre-run protocol: private, kept out of the public repo)
└── memory/
    └── case-log.md
```

What each file is for: `README.md`, "The folder" section — the one annotated list.

## Read order

1. `identity.md`
2. `rules.md`
3. `reference/failure-modes.md` + `reference/evidence-base.md`

Then wait for an evidence kit (defined in `rules.md` §1). Read `examples.md` before your
first diagnosis, not every time.

## Load rules

- Load a folder in `cases/` only when diagnosing or citing that case. Never load another
  case's transcript into a live diagnosis.
- After a completed diagnosis, append one row to `memory/case-log.md`. The row must name
  its case folder.
- `README.md` is for the human user. Do not restate it, and do not load it to diagnose.
