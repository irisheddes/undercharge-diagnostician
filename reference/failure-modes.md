# The eleven failure modes

The ways a solo engagement ends up underpriced, ordered roughly by how early in the chain
they strike. These are hypotheses to test against the artifacts, not a checklist — a real
diagnosis names one of these (or something these miss) and proves it from the evidence.

Distilled from lived engagements and from pricing method studied in consulting communities.
No client figures or third-party private material appear here.

## The four families

The modes group into families by where they strike on the chain. Diagnosis walks the
families first — which region of the chain broke earliest? — then lands on a mode inside
it. A case that fits a family but no listed mode is still diagnosable: name the family,
describe the new mode, and it becomes a candidate for this file.

| Family | Chain question | Modes |
| --- | --- | --- |
| **A — Taking the job** | Should this engagement have existed on these terms at all? | F1 |
| **B — The pricing moment** | When the number was fixed, what was it missing? | F2 F3 F4 F5 F6 F7 F10 |
| **C — Execution** | The price was set; what ate it afterward? | F8 F11 |
| **D — Standing conditions** | What was broken before any client appeared? | F9 |

The families interact, and the interplay is itself diagnostic knowledge: F1 frequently
enables F2, which later produces F8. F10 and F11 travel together — an estimate made
without the builder's reality leaves no budget for the learning curve, and uncertainty
about whether the work is good enough (the same uncertainty behind F4 and F7: no outside
comparison to check against) is what drives polishing past the priced standard.

---

## Family A — Taking the job

### F1 — Necessity acceptance

The job was taken because money was needed, so the walk-away price never existed. Every
number downstream was negotiated by someone who could not afford to lose the deal — and the
client could feel it. **Chain position: the decision to take the job.**
*Evidence signature:* fast agreement to the first number mentioned; no counter; pricing
conversation shorter than the scope conversation.

## Family B — The pricing moment

### F2 — Price before scope

The number was agreed before either party could list what the work contained. Whatever was
discovered afterward was, by construction, free. **Chain position: scope at pricing time.**
*Evidence signature:* the pricing message predates any written scope; delivered-scope list
is several times longer than anything discussed at pricing time.
**Ranking against F8:** apply the soundness test written under F8 before choosing between
them. Remedial work required to deliver the priced items counts here, not as growth.

### F3 — Free discovery

The diagnostic work — audits, mapping the client's process, figuring out what they actually
need — was given away to prove worth, then the priced work was quoted small because "most
of the thinking is already done." Discovery is a product: it produces the very number the
build should be priced against. Giving it away removes the anchor and the revenue at once.
**Chain position: the anchor.**
*Evidence signature:* substantial unbilled work before any agreement; proposal references
findings the client never paid for.

### F4 — No anchor

The price was derived from the freelancer's own hours and comfort, not from any external
number — what a vendor would charge, what hiring for it would cost, what the outcome is
worth per year to the client. Without an anchor, the price defaults to the freelancer's
self-assessment, which for most solo workers runs low. **Chain position: the anchor.**
*Evidence signature:* price justified internally ("that felt like about two weeks") with no
reference to any client-side number anywhere in the artifacts. A special case: the proposal
was drafted by AI and the number came with it. An AI-generated price is not an anchor — the
model predicts a plausible-sounding figure; it does not know the local market, the client's
alternatives, or the builder's speed. Common where the freelancer is new to the field and
has no rate history of their own to check against.

### F5 — Effort-priced outcome work

The work produced a durable asset or recurring saving, but was priced as hours. The client
keeps the yearly value; the freelancer was paid once for the typing. **Chain position: the
agreed price.**
*Evidence signature:* deliverable is a system, asset, or automation with ongoing value;
price is rate × time with no relation to that value.

### F6 — The relationship discount

Friend, warm referral, long-standing client — the price carried a tax paid to the
relationship, usually without either side naming it. Distinct from a *chosen* strategic
discount — a portfolio piece taken knowingly cheap, a foot in a door, is a strategy, not a
failure mode, and diagnosing it as one is a misdiagnosis. The relationship discount is
different in kind: unexamined, recurring, and resented. **Chain position: the agreed
price.**
*Evidence signature:* apologetic pricing language ("for you...", "since we know each
other"); this client priced below identical work for strangers.

### F7 — Self-worth pricing

The number measured the freelancer's confidence, not the client's outcome. Common where the
work is genuinely rare — the fewer people who can do it, the fewer prices exist to compare
against, and the more the number defaults to what feels defensible to say out loud.
**Chain position: the agreed price.**
*Evidence signature:* price far below any anchor that the artifacts themselves make
available; downplaying language around the freelancer's own expertise in the thread.

### F10 — The pricer was not the builder

The person (or AI) who set the price was not the person doing the work — a partner drafted
the proposal, a tool estimated the hours — so the estimate never contained the builder's
reality: their actual speed at *this* task, the skills they would have to learn on the job,
the parts they had never done before. Learning time became unbilled time by construction.
This is not the pricer's error alone: an estimate made without interviewing the builder is
a guess, and a builder who accepts an estimate without checking it against their own
history has co-signed the guess. **Chain position: the agreed price.**
*Evidence signature:* proposal authored by someone other than the person logging the hours;
estimate contains no reference to the builder's past actuals; hour log shows early tasks
taking multiples of their estimated time (the learning curve, paid by nobody).

## Family C — Execution

### F8 — Silent scope growth

The price was sound when set; the work grew and the price did not. No change-order moment
existed — each addition was absorbed because renegotiating felt harder than working.
**Chain position: scope shifts.**
*Evidence signature:* delivered-scope list materially exceeds priced scope; the scope-shift
record shows requests acknowledged but never re-priced.

**Ranking against F2 — the soundness test.** Both fit almost every engagement that grew,
because an underpriced job that also grew shows both signatures. F8's first clause is the
discriminator and it is a question about arithmetic, not judgment:

> **Deliver only the priced items, on the artifact as it actually was. Does the price
> still hold?**

Count *every* hour that delivering those items required, including remedial work nobody
requested and nobody could see at pricing time — a broken plugin, a dead mail path, an
old migration's debris. That work is not growth: the client did not ask for it (which is
F8) and the freelancer did not choose it (which is F11). It is what was already there, and
F2's signature names it — *whatever was discovered afterward was, by construction, free.*

- **The priced items alone overrun the price → F2.** The price was never sound, so the
  break is at the pricing moment however much the work later grew. Growth is contributing.
- **The priced items fit the price → F8.** The price was sound and only the additions sank
  it. The sight-unseen pricing, if any, is contributing.

Ask it in hours before ranking either. Two cold runs of this folder split on exactly this
arithmetic and neither stated the test it was applying — see
`cases/demo-case-3/refusal-round.md`.

### F11 — Gold-plating

The scope never moved and the client never asked — the *standard* moved, from the inside.
The engagement was priced for good; the freelancer delivered toward excellent; and the
extra hours turned a sound price into an underpriced one. "Good was good, and excellent
became bad": past the point the client would have accepted, every hour of polish lowers the
effective rate without raising the fee or, usually, the client's perceived value. Distinct
from F8: in F8 the client grows the work; in F11 the freelancer does. **Chain position:
between the agreed price and the invoice — the execution itself.**
*Evidence signature:* hour log shows a long tail after the deliverable was functionally
complete; revisions nobody requested; the delivered quality visibly exceeds anything
discussed at pricing time; perfectionism named in the freelancer's own account.

## Family D — Standing conditions

### F9 — The unpriced offer

No published or stated prices exist anywhere, so every engagement begins from zero and is
negotiated from whatever the client first suggests or the freelancer first dares. The
undercharge is decided before any specific client appears. **Chain position: before the
chain — a standing condition.**
*Evidence signature:* no rate card, no price on the website or proposal template; pricing
moment opens with the client's number, not the freelancer's.

---
