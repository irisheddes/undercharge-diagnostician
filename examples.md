# Example diagnoses

Each example shows the full reasoning: artifacts in, chain walked, one cause out.

> **Status while the entry is being built:** Example 1 is synthetic, written to demonstrate
> the output contract. It will be replaced by real diagnoses from the three pre-registered
> cases (see `cases/method-preregistration.md`) once those runs are complete. Real
> receipts beat clean fabrications; a labeled fabrication beats a fake receipt.

---

## Example 1 — the automation that priced itself as a design job *(synthetic)*

**Artifacts supplied.** A WhatsApp thread agreeing "€480 for the client-intake form and the
follow-up emails, yes?"; a delivered-scope list of eleven items including a Make scenario
that routes enquiries, drafts replies, and updates a tracking sheet; an hour log totalling
41 hours; a scope-shift record showing four "could it also…" requests, each answered
"sure, easy to add."

**The diagnosis as delivered:**

```text
DIAGNOSIS
Primary cause: the price was agreed for a two-item deliverable before the client's process
had been mapped, so the eleven-item system that mapping revealed was built for free (F2,
price before scope).

HOW I KNOW
Walking the chain backward from the invoice:
- The invoice covers 41 hours against a price set in the message "€480 for the client-intake
  form and the follow-up emails, yes?" — sent on day 2, before any process mapping.
- The four scope additions ("could it also update the sheet?") were absorbed without
  re-pricing — but silent growth (F8) is downstream here: there was no priced scope for the
  additions to be measured against, because the priced scope was two lines long.
- The delivered system replaces a recurring manual task — outcome work priced as effort
  (F5) is present — but the rate is not the broken link: at double the rate this engagement
  still loses, because 9 of the 11 delivered items were never in the priced scope at all.
The earliest broken link is the pricing moment itself: the number was fixed when the work
was two items, and every discovery after it was, by construction, unpaid.

CONTRIBUTING (not primary)
- F8 silent scope growth — real, but only possible because no priced scope existed to
  defend.
- F5 effort-priced outcome work — would cap the upside even with correct scoping; did not
  cause this loss.

WHAT THIS DIAGNOSIS CANNOT TELL YOU
Whether the client would have accepted a scoped price — the thread contains no signal of
their budget. And whether taking it anyway was strategically right; that depends on facts
outside these artifacts.
```

**Why this is a diagnosis and not something else.** It does not list all three failure
modes as findings — it ranks them and names one. It does not say what to charge. It quotes
the artifact the conclusion rests on. And it ends.

---

## Example 2 — *(reserved: pre-registered Case A, real engagement, redacted)*

## Example 3 — *(reserved: pre-registered Case B, real engagement, redacted)*
