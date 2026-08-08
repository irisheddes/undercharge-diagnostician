# Optional: draft the evidence kit from your project folder

If the engagement has a big paper trail, you do not have to assemble the kit by hand.
A separate session can draft it from your own project folder. Here is the whole flow:

1. **Open a new window in your project folder** — the client folder or archive where
   the engagement's material lives. Not this diagnostician folder. Start Claude there.
2. **Paste the prompt below**, filling in the engagement name and the output path (the
   full path to this folder's `cases/<case-name>/evidence-kit.md`).
3. **Approve one permission.** The session reads its own folder freely; at the end it
   asks to write a single file outside it — the draft kit, into this folder. Say yes to
   that one write and nothing else.
4. **Stay in that window and finish the kit there.** After writing the draft, the
   session walks you through its "For me to verify" list and declared gaps one item at
   a time — and because the source files are right there, it can re-check documents as
   you answer. You are the authority on what actually happened; genuine unknowns stay
   as declared gaps. When you confirm the kit is complete, it sets the frozen date.
5. **Then return to your diagnosis session** — the same window if still open, or any
   fresh one — and say: *"my kit is frozen — continue cases/<case-name>."* The intake
   resumes with only its own remaining questions, then the diagnosis.

Why the separate window matters: the mining session must never judge, and the judging
session must never mine. A diagnosis made by a session that has wandered your whole
project folder is not made from the frozen kit, and stops being reproducible.

---

Copy from here, fill the two paths:

```text
You are doing an evidence-extraction pass for a pricing post-mortem. Read-only on this
folder, plus one file written elsewhere. Do not analyze, do not diagnose, do not offer
opinions about pricing — extract and quote.

From the material in this folder, draft the four pieces of evidence about the
engagement: <name the engagement / client>

1. THE PRICING MOMENT — the proposal, thread, or notes where the price was set. Quote
   verbatim, with dates. Who proposed the number, and what was it based on, if visible.
2. THE SCOPE AS DELIVERED — a plain list of delivered things (not files), with roughly
   when each was added, cross-checked against the priced scope where possible.
3. THE TIME SPENT — reconstructed as ranges from what exists: file dates, logs,
   calendars, message timestamps. State the basis for every block. Never invent hours.
4. THE SCOPE-SHIFT RECORD — the moments the work grew past the agreement. Quote
   verbatim, with dates, including what was said about money (usually: nothing).

Rules: never fabricate quotes, numbers, or dates; preserve the order of events; where
something cannot be found, write it into a "Declared gaps" section instead of filling
it. Under each artifact add a "Sources:" line with the file paths used. End with a
"For me to verify" list of every number and claim I should confirm.

Start the file with: "DRAFT — extracted <date>. To be corrected and frozen before any
run."

Write the draft to: <full path to this diagnostician folder>/cases/<case-name>/evidence-kit.md

After writing the draft, do not finish there. Walk me through, one item at a time:
every entry in "For me to verify" and every declared gap — ask, wait for my answer,
re-check the source files here where that settles it, and correct the saved kit as we
go. One item per message, short. Keep genuine unknowns as declared gaps. When I confirm
the kit is complete, set the "Frozen on" date and change the first line to "CORRECTED
AND FROZEN — <date>". Then end with exactly one next step: "Kit frozen. Go back to
your diagnosis session and say: my kit is frozen — continue my case."
```
