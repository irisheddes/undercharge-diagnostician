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
│   └── (real cases: private, kept out of the public repo)
├── protocol/   (private: the pre-run test protocol and frozen guesses)
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

- During a diagnosis, open only the one case folder being diagnosed. Every other case
  folder and transcript stays closed, as does `protocol/` (it holds the builder's
  pre-run guesses; reading it would contaminate a diagnosis). This holds without the
  user having to say it.
- Starting a new case: copy `cases/_template-case/` to `cases/<name>/`. Real cases are
  named `case-<letter>`; fictional demos are `demo-case-<n>`.
- Do not open `memory/case-log.md` during a diagnosis. After the diagnosis is delivered,
  append one row to it; the row must name its case folder.
- `README.md` is for the human user. Do not restate it, and do not load it to diagnose.
- After saving a transcript, run `python3 _tools/check_diagnosis.py <transcript path>`
  and report the result. A FAIL means the diagnosis violated the output contract — say
  so plainly; do not quietly rewrite the transcript to pass.
