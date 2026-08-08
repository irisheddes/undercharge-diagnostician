# Case log — the folder that learns

One line per diagnosed engagement, appended after every diagnosis. This is the
diagnostician's accumulated experience: over time, the frequency column becomes its own
finding about how solo underpricing actually distributes.

**Append rule:** after each completed diagnosis, add a row. Never edit or delete a row —
if a diagnosis is later revised, add a new row referencing the old one.

**Integrity rule:** every row names its folder in `cases/`, and every case folder with a
transcript has a row here. A row without a folder, or a folder without a row, is a defect.

| Date | Case folder | Domain | Primary cause | Contributing | Matched pre-run guess? |
| --- | --- | --- | --- | --- | --- |
| — | `cases/case-a/` (private) | AI consulting (design/build) | *pending run* | | |
| — | `cases/case-b/` (private) | AI consulting (discovery phase) | *pending run* | | |
| 2026-08-08 | `cases/demo-case/` | Brand design (fictional demo) | F9 — the unpriced offer | F1, F2, F8, F6, F11 | — (no pre-run guess for demo) |
| 2026-08-08 | `cases/demo-case-2/` | Video editing (fictional demo) | F1 — necessity acceptance | F9, F8, F4, F3, F5 | — (no pre-run guess for demo) |
| 2026-08-08 | `cases/demo-case-3/` | WordPress development (fictional demo) | F2 — price before scope (fixed price accepted sight-unseen; own written condition never enforced) | F8, F4, F5 | — (no pre-run guess for demo) |

## Pattern notes

*(written only when three or more rows share a cause — the log speaks first, the pattern
after)*
