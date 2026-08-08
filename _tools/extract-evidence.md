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
4. **Close the extraction window and return to your diagnosis session** — the same
   window if it is still open (it stayed clean; the mining happened elsewhere), or any
   fresh session later, saying: *"continue my case — cases/<case-name>."*
5. **Correct the draft together.** Tell it the extraction landed. It walks you through
   the draft's "For me to verify" list one item at a time — you answer, it fixes the
   kit — and sets the frozen date when you confirm the kit is complete. You are the
   authority on what actually happened; the extractor only found what was written
   down. (Prefer to edit the file by hand? Also fine — set the "Frozen on" date
   yourself, then tell the session you're ready.) Either way, the intake then resumes
   from whatever the corrected kit still leaves unanswered.

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

End your final summary with a single clear next step for me, in this spirit: "Draft
saved. Go back to your diagnosis session and tell it the extraction landed — it will
walk you through correcting the draft one item at a time and freeze it when you
confirm." Do not tell me to edit the file by hand; that is the fallback, not the path.
```
