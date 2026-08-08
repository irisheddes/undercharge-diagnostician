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
│   ├── demo-case/ · demo-case-2/ · demo-case-3/   (fictional, public, with transcripts)
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

- During a diagnosis, open only the one case folder being diagnosed. Everything else in
  `cases/` stays closed: other case folders, their transcripts, and
  `method-preregistration.md` (it holds the builder's pre-run guesses; reading it would
  contaminate the diagnosis). This holds without the user having to say it.
- Do not open `memory/case-log.md` during a diagnosis. After the diagnosis is delivered,
  append one row to it; the row must name its case folder.
- `README.md` is for the human user. Do not restate it, and do not load it to diagnose.
