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

1. Drop this folder into a Claude project, or open Claude Code inside it.
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
   rules.md, section 1.
2. **Then one round of questions** to complete the picture — only the ones your
   evidence does not already answer. Plain answers beat polished ones.
3. **Then the diagnosis**, in a fixed shape: one primary cause in a single sentence,
   the reasoning with quotes from your own evidence, the contributing factors ranked
   underneath it, and a plain statement of what your evidence cannot show. Then it
   stops.

## What it refuses

Ask "so what should I have charged?" and it declines. That is a consultant's job, not a
diagnostician's. Same answer for "write the renegotiation email" and "check my whole
pricing model." A diagnostician that drifts into fixing has stopped diagnosing. The
refusal rules, including the disguised versions of these asks, are in rules.md,
section 5.

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
