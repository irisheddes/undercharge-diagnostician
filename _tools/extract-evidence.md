# Optional: draft the evidence kit from your project folder

If the engagement has a big paper trail, you do not have to assemble the kit by hand.
Open a **separate** Claude session in the folder where the project's material lives
(your client folder, your archive — not this diagnostician folder), paste the prompt
below, and it will draft the kit for you. Then read the draft, correct it by hand —
you are the authority on what actually happened — and set the Frozen on date.

The separation matters: the diagnosis session never enters your project folder, and
the extraction session never diagnoses. One mines, the other judges.

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

Start the file with: "DRAFT — extracted <date>. Correct by hand and set the Frozen on
date before any run."

Write the draft to: <full path to this diagnostician folder>/cases/<case-name>/evidence-kit.md
```
