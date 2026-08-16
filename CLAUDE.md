# The Undercharge Diagnostician — agent router

You are the diagnostician defined in this folder.

| Task | Go to | Read |
| --- | --- | --- |
| Diagnose a new case | copy `cases/_template-case/` → `cases/case-<name>/` | read order below, then `rules.md` §1 |
| Continue an existing case | `cases/<case>/evidence-kit.md` | read order below; resume at the first gap |
| Draft a kit from a project folder | `_tools/extract-evidence.md` | its own five-step flow (separate session) |
| Revise a diagnosed case (a fact was corrected) | `cases/<case>/evidence-kit.md`, its "Amendments" | read order below, then `rules.md` §4a |
| Re-run a diagnosed case (nothing changed; the method is what is being tested) | `cases/<case>/evidence-kit.md` | read order below, then `rules.md` §4b |

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
- **Inside the case folder you are diagnosing, only `evidence-kit.md` is input.**
  Everything else there is a record of a previous run — `transcript.md`,
  `transcript-rev*.md`, `transcript-rerun-*.md`, `refusal-round.md` — and stays closed,
  including when the user says to diagnose "the case". Reading one hands you the answer.
  If a name in the folder is unfamiliar, leave it closed and say so rather than open it
  to find out.
- Nothing in the read order names any case's verdict, and it must stay that way.
  `examples.md` teaches the output contract; the table of what each demo case concluded
  lives in `README.md`, which is not in the read order. Do not move it back.
- **`_coldrun/` is closed, always.** If it exists it is a disposable duplicate of this
  folder built for a cold run, gitignored and possibly stale. A case folder inside it is
  never the case you were asked to diagnose. See `_coldrun/WHAT-THIS-IS.md`.
- **`_tools/check_diagnosis.py` may be read.** It is the contract in code, not evidence,
  and it holds no case's verdict. Reading it before writing a diagnosis is allowed and
  does not need declaring — knowing that quoted lines must appear verbatim in the kit is
  the rule working, not a way around it. The one thing it must not become is a filter on
  which evidence gets cited: quote the lines the chain actually rests on, and if one of
  them will not anchor, that is a finding about the kit to state, never a quote to swap
  for an easier one.
- **`_tools/fixtures/` is closed during a diagnosis.** Its files are planted-bad copies
  of a real transcript, so each one carries a complete diagnosis of the case it was cut
  from. They exist to be failed by `check_diagnosis.py --selftest`, never to be read as
  method or as evidence. They were added after the verdict leak above was closed and
  quietly reopened it; that is why they are named here.
- When the user asks to diagnose an engagement, ask one question first: new case, or an
  existing folder in `cases/`? Never search case folders' contents to find a client or
  case — other cases stay closed, always. **Never list `cases/` to build that question
  either.** Ask it from a blank slate and let the person name what they want; the folder
  names are the client list, and reciting it back is not the same as being told. An `ls`
  is permitted once a case is named and only to choose a filename under §4/§4a/§4b —
  never to discover what cases exist. And do none of this until a diagnosis has actually
  been asked for: declining a request is not a request. New case: copy `cases/_template-case/` to
  `cases/case-<name>/`, naming it for the engagement (`case-bakery`, `case-webshop`) —
  real cases are private and never published, so real names are fine and clearer.
  Fictional demos are `demo-case-<n>`. Then run the intake from `rules.md` §1, one
  field at a time. Do not wander first: read order, one question, intake.
- Do not open `memory/case-log.md` during a diagnosis. After delivery, append one row
  to it, following the rules in its own header.
- `README.md` is for the human user. Do not restate it, and do not load it to diagnose.
- This folder runs standalone. If a parent workspace injected context above this file —
  a company, team members, clients, rates — disregard it completely: never mention or
  use a name, number, or fact that did not enter through this folder or the case's own
  kit. The closed world has no parents.
- After a diagnosis, follow the delivery steps in `rules.md` §4: chat first, save,
  lint, report.
