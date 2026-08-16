# The Undercharge Diagnostician

One question: why did this engagement end up underpriced?

I built this because I kept underpricing my own work and could never say exactly where
it went wrong. The tool reads the paper trail of one finished job and names the single
decision that made the low price inevitable. It will not tell you what to charge next
time, it will not write the awkward email to the client, and it will not hand you a list
of twelve mistakes. One engagement in, one cause out, reasoning shown.

It is built for solo AI and creative consultants: people who sell custom builds,
automations, design and content, set their own prices, and have no sales team to blame.
The method works for most self employed work, but it was built and tested on real AI
consulting engagements first. That includes a failure native to this field: the AI
drafted proposal whose price nobody checked against anything.

## How to use it

1. Drop this folder into a Claude project, or open Claude Code inside it. Both work for
   diagnosing. One difference worth knowing up front: the contract checker
   (`_tools/check_diagnosis.py`) is a Python script, so it can only run where there is a
   shell — Claude Code, or your own terminal. In a Claude Project the diagnosis is
   delivered and saved as normal and the check simply reports that it could not run.
   Nothing else changes.
2. Pick one finished job that still bothers you. A website you built, a rebrand, a
   video edit, a launch campaign, a discovery phase that went nowhere — any client work
   where the invoice is paid or written off and you know, from the hours or the
   resentment, that the price was wrong. Finished matters: the diagnosis works backward
   from how things ended. Not a live project, not a hypothetical.
3. Start with one line: **"I want to diagnose a finished engagement."** What happens
   next is below.

## What to expect

1. **You will be asked for four pieces of evidence** — all from the money trail, never
   from the project files: the pricing moment (the thread or proposal where the number
   was set), the scope as actually delivered, the time actually spent (rough is fine),
   and what was said each time the work grew. Redact names freely; keep the numbers,
   the dates and the order of events, because the diagnosis lives in the sequence. Gaps
   are allowed: if something was never written down, say so — what is missing from a
   paper trail is information too. Full definitions and the intake questions are in
   rules.md, section 1. Two ways to provide the evidence, both fine: paste it yourself
   as you are asked for it, or — for a big project — run the ready extraction prompt in
   `_tools/extract-evidence.md` in a separate session inside your own project folder,
   and it drafts the kit for you to correct.
2. **Then one round of questions** to complete the picture — only the ones your
   evidence does not already answer. Plain answers beat polished ones.
3. **Then the diagnosis**, in a fixed shape: one primary cause in a single sentence,
   the reasoning with quotes from your own evidence, the contributing factors ranked
   underneath it, and a plain statement of what your evidence cannot show. Then it
   stops.

## If the diagnosis rests on a wrong fact

You are the authority on what happened, and evidence can be corrected. Tell it which
fact is wrong — "the price wasn't built from the monthly cap; it was set first and
then split into payments" — and the correction goes into the kit as a dated amendment,
a fresh session re-runs the case cold, and the new verdict is saved beside the old
one. Both stay: seeing what changed when one fact changed is part of the diagnosis.

What this is not: a way to re-roll a verdict you dislike. Corrections change facts;
they don't appeal conclusions. A diagnosis you disagree with, built on facts you
confirm, stands.

## What it refuses

Ask "so what should I have charged?" and it declines. That is a consultant's job, not a
diagnostician's. Same answer for "write the renegotiation email" and "check my whole
pricing model." A diagnostician that drifts into fixing has stopped diagnosing. The
refusal rules, including the disguised versions of these asks, are in rules.md,
section 5.

### The refusals on disk, including the one that failed

Designing a refusal is easy. `cases/demo-case-3/refusal-round.md` is three sessions of
one happening, run against a method written and committed before any of them opened, and
kept unedited.

- **The bulk ask, refused at the front door.** "Go through all my clients and tell me
  where I'm losing money" — declined in the first sentence, before a case existed and
  before the method loaded.
- **Three disguises after a real diagnosis.** "What should I have charged", then "just
  give me two options", then "show me what a healthy version would look like". The second
  and third held. **The first did not** — it declined correctly and then priced the
  engagement at a hypothetical figure anyway, closing with "that is as close to a number
  as the evidence goes". That turn is still in the file.
- **The clause, then the re-run.** `rules.md` §5 gained a paragraph forbidding exactly
  that, naming both forms. The same ask, sent again to a cold session, declined and
  stopped. What counted as holding was written down before the answer existed.

The commits are in that order on purpose: the failure is committed before the rule that
closes it, so which came first is checkable rather than claimed.

### Two cold runs on the same evidence disagreed

`demo-case-3` has been diagnosed twice from the identical frozen kit, months apart, the
second time by a session that never opened the first transcript. They reached **different
primary causes** — price-before-scope, then silent-scope-growth — and each examined the
other's answer and ranked it second. Both pass the contract check.

Neither is superseded. `rules.md` §4b, written before the second run, says a differing
verdict is a finding about the folder and not a correction to the case, so the pair is
kept as the result. It locates the method's weakest joint precisely: §2 asks which link
broke *earliest*, and the two runs disagree about whether a condition you wrote and never
enforced breaks on the day it is written or the day it is first ignored.

That is the honest limit of this tool, found by its own rule, and it is on the front page
rather than in a footnote.

## Three demonstration runs, three different verdicts

All three cases are fictional and labeled so; all three runs were cold — fresh session,
method files and one case only, first output kept unedited. Two of the kits were written
blind, by sessions (one from a different AI entirely) that had never seen this method.

| Case | The engagement | Primary cause found | Transcript |
| --- | --- | --- | --- |
| `demo-case/` | €900 studio rebrand, client named the price first | The unpriced offer — no price of her own existed anywhere | `cases/demo-case/transcript.md` |
| `demo-case-2/` | €850 launch video, quoted at 00:14 with rent due | Necessity — no walk-away price could exist | `cases/demo-case-2/transcript.md` |
| `demo-case-3/` | €750 site refresh, quoted before opening the backend | Price before scope — own written condition never enforced | `cases/demo-case-3/transcript.md` |

Each run also argued explicitly *against* the causes the other cases concluded — the
third case ruled out necessity (the developer had savings and booked work) and the
unpriced offer (he owned a day rate) before landing on the pricing moment. Same method,
different evidence, different answers. The verdicts column shows each case as first
diagnosed; `memory/case-log.md` is the authoritative record if a diagnosis is ever
revised. For a human reader, `demo-case-3/transcript.md` — the run under the current
rules, plain language, spoken to the person — is the best single thing to read. (An agent running a diagnosis learns the
contract from the worked example in `examples.md`; case transcripts and this table stay
closed to it, per the router — see that file's note on why the verdicts are not there.)

The table sits here, not in `examples.md`, because that file is required reading before a
first diagnosis: anything in it is read *before* the evidence kit is opened. It used to be
there, and a re-run of `demo-case-3` read its own answer on the way in and said so
unprompted — see `cases/demo-case-3/refusal-round.md`.

---

## The folder

- `CLAUDE.md` — read order for the agent running this folder
- `identity.md` — who the diagnostician is and what it diagnoses
- `rules.md` — the method: intake gate, the pricing chain, cause vs symptom, output
  contract, refusals
- `examples.md` — worked diagnoses showing the reasoning
- `reference/failure-modes.md` — the eleven ways solo engagements end up underpriced,
  in four families
- `reference/evidence-base.md` — the research behind the failure modes, tiered by how
  solid the source is, gaps stated
- `cases/` — the diagnosed engagements. Public here: `_template-case/` (copy it to start
  a case) and three fictional demo cases, each with its evidence kit and unedited run
  transcript. Private, on my machine only: the real case files, out of respect for the
  clients and people inside them, and a `protocol/` folder holding the pre-run test
  protocol with my frozen guesses.
- `memory/case-log.md` — one row per diagnosed case. It ships with cases in it, not
  promises.
- `_tools/check_diagnosis.py` — the output contract, enforced in code: checks any
  transcript for exactly one primary cause, all four sections in order, reasons under
  every contributing factor, plain-language naming, and zero prescription language.
  Run on the three demo transcripts it passes `demo-case-3` and fails the two older
  runs on exactly the rule that postdates them — the method's improvement, verifiable
  mechanically.

  It also opens the case's `evidence-kit.md` and checks the rule the rest of the
  contract rests on — `rules.md` §3, **no quote, no claim**: every quoted span in a
  diagnosis must appear in the evidence. Formatting is flattened first (line wrapping,
  markdown, quote-mark style, elisions marked with `...`), so a quote that was re-marked
  or re-wrapped still matches — but wording is not, so **a paraphrase does not match**.
  A quote directly behind a negation is read as a named absence and exempted; that
  exemption, and its limit, is written above the code. If no kit sits beside the
  transcript the check fails rather than skips: a gate that passes when it cannot look
  is not a gate.

  Until this existed the checker enforced the *shape* of a diagnosis and never opened
  the evidence, so an invented quote scored a clean pass. It found one real defect on
  first run against the full case set — a private transcript that rendered the kit's
  "not evidenced as ever communicated to Gabi" as the direct quote
  "never communicated to Gabi", turning an absence of evidence into an asserted fact.
  That first catch is the argument for the check.

- `_tools/fixtures/` — three planted-bad transcripts, each a copy of `demo-case-3`
  carrying exactly one defect: a fabricated quote, a smuggled prescription, two primary
  causes. `python3 _tools/check_diagnosis.py --selftest` fails unless **every one of
  them fails**. A checker that cannot fail is a rubber stamp, and a green run against
  only good files cannot tell a working gate from a broken one.
