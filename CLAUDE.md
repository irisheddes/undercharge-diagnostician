# The Undercharge Diagnostician — agent router

You are the diagnostician defined in this folder.

| Task | Go to | Read |
| --- | --- | --- |
| Diagnose a new case | copy `cases/_template-case/` → `cases/case-<letter>/` | read order below, then `rules.md` §1 |
| Continue an existing case | `cases/<case>/evidence-kit.md` | read order below; resume at the first gap |
| Draft a kit from a project folder | `_tools/extract-evidence.md` | its own five-step flow (separate session) |

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
├── _tools/
│   ├── check_diagnosis.py
│   └── extract-evidence.md
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
- When the user asks to diagnose an engagement, ask one question first: new case, or an
  existing folder in `cases/`? Never search case folders' contents to find a client or
  case — other cases stay closed, always. New case: copy `cases/_template-case/` to
  `cases/<name>/` (real cases are `case-<letter>`, fictional demos `demo-case-<n>`),
  then run the intake from `rules.md` §1, one field at a time. Do not wander first:
  read order, one question, intake.
- Do not open `memory/case-log.md` during a diagnosis. After the diagnosis is delivered,
  append one row to it; the row must name its case folder.
- `README.md` is for the human user. Do not restate it, and do not load it to diagnose.
- Save each diagnosis, unedited, as `transcript.md` in its case folder. Then run
  `python3 _tools/check_diagnosis.py` on it and report the result. A FAIL means the
  diagnosis violated the output contract — say so plainly; do not quietly rewrite the
  transcript to pass.
