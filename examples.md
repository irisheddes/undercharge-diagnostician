# Example diagnoses

Two examples, different in kind and labeled honestly. The first is a real cold run on a
fictional engagement, with the full evidence and unedited transcript in this repo. The
second is a written illustration of the output contract. My own real engagements have
also been run; those cases and transcripts stay private out of respect for the people
in them.

One note on reading the transcripts: early runs used the internal F-codes as cause
names. After running the tool, the rules gained a plain language rule — causes are named
in words a stranger understands, codes demoted to optional pointers. Old transcripts
stay as they were run; the commits date the change.

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
different evidence, different answers. `demo-case-3/transcript.md` shows the current
rules — plain language, spoken to the person — and is the best single thing to read.

---

## Example 1 — the €900 rebrand (real run, fictional engagement)

Maya, a freelance brand designer, rebranded a yoga studio for a flat €900 the client
proposed in the first message. Nine weeks and roughly 120 hours later everything was
delivered, loved, and in daily use. Effective rate: at most €7.50 an hour.

Five failure modes were visibly present in the kit — the client spoke the first number,
the scope was written after the price, four scope additions were absorbed silently, the
client was a warm referral, and the last three weeks were polish nobody asked for. The
test of a diagnostician is which one it ranks first.

The run named none of the obvious ones. Primary cause, from the transcript:

> Maya began this engagement with no price of her own anywhere — no rate card, no
> published prices, no idea what studio rebrands cost — so the only number that could
> exist was the client's, and €900 became the price the moment it was said (F9, the
> unpriced offer).

Every other broken link was then shown as downstream of that standing condition — for
example:

> F8 silent scope growth — four unpriced additions, but there was no priced scope or
> rate in existence for a change-order to invoke.

The full run is public: the invented artifacts in `cases/demo-case/evidence-kit.md`,
the complete first-output transcript in `cases/demo-case/transcript.md` — including the
chain walk, the chosen-discount check, and what the artifacts could not show.

---

## Example 2 — the automation that priced itself as a design job (written illustration)

A shorter, invented illustration of the output shape, kept because it shows the
contract at a glance.

**Artifacts supplied.** A WhatsApp thread agreeing "€480 for the client-intake form and
the follow-up emails, yes?"; a delivered-scope list of eleven items including a Make
scenario that routes enquiries, drafts replies, and updates a tracking sheet; an hour
log totalling 41 hours; a scope-shift record showing four "could it also…" requests,
each answered "sure, easy to add."

**The diagnosis, in the contract's shape:**

```text
DIAGNOSIS
Primary cause: the price was agreed before anyone knew what the work contained — the
number was fixed for a two-item deliverable before the client's process had been
mapped, so the eleven-item system that mapping revealed was built for free (price
before scope, F2 in the reference).

HOW I KNOW
- The invoice covers 41 hours against a price set in the message "€480 for the
  client-intake form and the follow-up emails, yes?" — sent on day 2, before any
  process mapping.
- The four scope additions were absorbed without re-pricing — but silent growth is
  downstream here: the priced scope was two lines long, so there was nothing for the
  additions to be measured against.
- At double the rate this engagement still loses: 9 of the 11 delivered items were
  never in the priced scope at all. The rate is not the broken link.

CONTRIBUTING (not primary)
- Silent scope growth (F8) — real, but only possible because no priced scope existed.
- Outcome work priced as hours (F5) — would cap the upside even with correct scoping;
  did not cause this loss.

WHAT THIS DIAGNOSIS CANNOT TELL YOU
Whether the client would have accepted a scoped price — the thread contains no signal
of their budget. And whether taking it anyway was strategically right; that depends on
facts outside these artifacts.
```

**Why these are diagnoses and not something else.** Neither lists every present failure
mode as a finding: each ranks them and names one. Neither says what to charge. Both
quote the artifact each conclusion rests on. And both end.
