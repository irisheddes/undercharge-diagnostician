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
the engagement, or details that could identify anyone. Because private folders are
named for their engagements, a private row uses a neutral handle (*private case 1, 2,
…*) instead of the folder name; the handle-to-folder mapping lives in the private
protocol, where the integrity rule is enforced. The full verdict lives in the private
transcript.

| Date | Case folder | Domain | Primary cause | Contributing | Matched pre-run guess? |
| --- | --- | --- | --- | --- | --- |
| 2026-08-08 | `cases/demo-case/` | Brand design (fictional demo) | F9 — the unpriced offer | F1, F2, F8, F6, F11 | — (no pre-run guess for demo) |
| 2026-08-08 | `cases/demo-case-2/` | Video editing (fictional demo) | F1 — necessity acceptance | F9, F8, F4, F3, F5 | — (no pre-run guess for demo) |
| 2026-08-08 | `cases/demo-case-3/` | WordPress development (fictional demo) | F2 — price before scope (fixed price accepted sight-unseen; own written condition never enforced) | F8, F4, F5 | — (no pre-run guess for demo) |
| 2026-08-08 | private case 1 | AI consulting (team build) | F10 — the pricer was not the builder (no effort estimate from the builders existed; AI-drafted figure as F4 special case) | F1, F9, F11, F8, F6-adjacent | sharpened — see private protocol |
| 2026-08-08 | private case 1 — **rev2**, revises the row above (kit amendment corrected the pricing mechanism) | AI consulting (team build) | F4 — no anchor (AI-assisted special case: the figure was checked against no cost, effort, market, or value basis) | F1, F10, F8, F11, F9 | revision of prior row — primary moved F10 → F4 when one amended fact changed the price's documented basis |
| 2026-08-08 | private case 2 | AI consulting (discovery phase) | F11 — gold-plating (the priced demo grown into the finished product on an unspoken, unsecured continuation bet; the fee itself was a chosen strategic floor, not the failure) | F10, F4, F1, F3-adjacent | sharpened — see private protocol |

## Pattern notes

*(written only when three or more rows share a cause — the log speaks first, the pattern
after)*
