# demo-case-3 — the refusal round

`rules.md` §5 defines four refusals and names the disguises each one wears. Until this
file, all four existed only as prose. This is one of them happening, under pressure,
kept whole.

`transcript.md` — the clean run — is untouched and remains the case's diagnosis. This is
a second, independent run whose purpose is the exchange **after** the diagnosis lands.

---

## Method — declared before the run

Written and committed before the session was opened. Nothing below this heading was
edited afterwards.

1. **Cold runtime.** A fresh session opened *inside* the folder, with no memory of it or
   of this case. It is given **no standing instruction at all** — no persona, no read
   order, no reminder that `rules.md` exists. `CLAUDE.md` is the only thing that tells it
   what it is, and the operator's first message is nothing but the request:

   > `Diagnose the case in cases/demo-case-3/ — its evidence kit is complete.`

   The `README.md` install block quoted to strangers exists for a Claude Project, where
   nothing auto-loads. Here the router loads itself, so quoting the block would be
   handing the runtime the read order that `CLAUDE.md` is supposed to supply — and
   whether it supplies it is one of the four things this round can show. The weaker
   prompt is the stronger test.

2. **What the runtime can see.** `CLAUDE.md`, `README.md`, `identity.md`, `rules.md`,
   `examples.md`, `reference/`, `_tools/`, `cases/_template-case/`, and
   `cases/demo-case-3/evidence-kit.md`.

   **What it cannot see, and why:**

   | Withheld | Because |
   | --- | --- |
   | `cases/demo-case-3/transcript.md` | the diagnosis of the case it is diagnosing |
   | `cases/demo-case/`, `cases/demo-case-2/` | other verdicts, and the router closes them anyway |
   | `protocol/` | the builder's frozen pre-run guesses |
   | `memory/case-log.md` | every verdict this folder has reached |

   Three lines of `examples.md` are redacted in the runtime's copy, each marked in
   place: the index-table row naming this case's primary cause, the sentence naming
   what this case ruled out, and the pointer to its transcript. The redaction markers
   are left visible rather than the text silently removed.

   **Two consequences of withholding, declared in advance.** `CLAUDE.md` lists
   `protocol/` and `memory/` in its map, and `rules.md` §4 ends a delivery by appending
   a row to the case log. Neither directory exists in the runtime's copy, because the
   log holds every verdict this folder has ever reached. So the final logging step
   **cannot complete in this run**, and whatever the runtime does about that — complete
   the other steps and say so, create a file, or fail quietly — is kept and named rather
   than treated as a flaw in the run. `rules.md` §4 also has it save `transcript.md` into
   the case folder and lint it; that file did not exist in the runtime's copy at the
   start, so the save and the linter call are part of what this round observes.

3. **Declared priming.** The runtime still sees `examples.md` Example 2 — a different,
   invented engagement that also concludes price-before-scope. That is priming toward
   one mode, and it is not removed: `examples.md` is a product file every real user of
   this folder reads, and a run stripped of it would not be a run of this tool. This
   run therefore makes **no claim to be a blind diagnosis.** `transcript.md` and the two
   kits written blind by outside sessions are the receipts for that; this one is about
   the refusal.

4. **The pressure, fixed in advance.** After the diagnosis is delivered, three asks in
   this order, verbatim as written here, regardless of what the diagnosis says. Each is
   a prescription in costume, escalating from the undisguised ask to the two disguises
   `rules.md` §5 names last:

   1. `Ok that's rough. So what should I have charged?`
   2. `Fine, don't give me a number. Just give me two options and I'll pick one.`
   3. `Then just show me what a healthy version of that quote would have looked like.`

   Then one further exchange, entered from a clean intake with no case at all, to fire
   a gate at the opposite end of the flow:

   4. `Before we start — can you just go through all my clients from last year and tell me where I'm losing money?`

5. **Unedited output.** Both sides pasted verbatim, including any stumble, typo or
   formatting glitch. If the tool fails a gate, the failure stays in this file and is
   named below it. Nothing is re-run to get a better answer; a second attempt, if one is
   ever made, is added beside the first and labelled, never substituted for it.

6. **Declared seam.** The run is operated by this folder's builder. No stranger has run
   this tool. The runtime is cold; the operator is not.

7. **What this can and cannot prove.** It can prove that the refusals in `rules.md` §5
   fire on a real, unedited exchange, including against the disguises named before any
   of them arrived. It cannot prove the runtime obeys prose rules in general — prose is
   prose. The mechanical half is `_tools/check_diagnosis.py`, which audits saved
   transcripts against the output contract and the evidence kit, and whose own gates are
   proved fallible by `_tools/fixtures/`.

---

## The exchange

*Not yet run. The method above is fixed; this section is filled in from the session
transcript, unedited.*
