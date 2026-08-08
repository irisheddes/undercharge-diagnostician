# Case log — the folder that learns

One line per diagnosed engagement, appended after every diagnosis. This is the
diagnostician's accumulated experience: over time, the frequency column becomes its own
finding about how solo underpricing actually distributes.

**Append rule:** after each completed diagnosis, add a row. A registered case that has
not yet run may hold a placeholder row marked *pending run* — that is a declared
intention, not a diagnosis. Never edit or delete a diagnosed row — if a diagnosis is
later revised, add a new row referencing the old one.

**Integrity rule:** every row names its folder in `cases/`, and every case folder with a
transcript has a row here. A row without a folder, or a folder without a row, is a defect.

**Privacy rule:** this log is public even when its cases are not. A row for a private
case carries the cause and its family only — never client figures, amounts, dates of
the engagement, or details that could identify anyone. The full verdict lives in the
private transcript.

| Date | Case folder | Domain | Primary cause | Contributing | Matched pre-run guess? |
| --- | --- | --- | --- | --- | --- |
| — | `cases/case-a/` (private) | AI consulting (design/build) | *pending run* | | |
| — | `cases/case-b/` (private) | AI consulting (discovery phase) | *pending run* | | |
| 2026-08-08 | `cases/demo-case/` | Brand design (fictional demo) | F9 — the unpriced offer | F1, F2, F8, F6, F11 | — (no pre-run guess for demo) |
| 2026-08-08 | `cases/demo-case-2/` | Video editing (fictional demo) | F1 — necessity acceptance | F9, F8, F4, F3, F5 | — (no pre-run guess for demo) |
| 2026-08-08 | `cases/demo-case-3/` | WordPress development (fictional demo) | F2 — price before scope (fixed price accepted sight-unseen; own written condition never enforced) | F8, F4, F5 | — (no pre-run guess for demo) |
| 2026-08-08 | `cases/case-c/` (private) | AI consulting (team build) | F10 — the pricer was not the builder (no effort estimate from the builders existed; AI-drafted figure as F4 special case) | F1, F9, F11, F8, F6-adjacent | sharpened — see private protocol; revision pending |

## Pattern notes

*(written only when three or more rows share a cause — the log speaks first, the pattern
after)*
