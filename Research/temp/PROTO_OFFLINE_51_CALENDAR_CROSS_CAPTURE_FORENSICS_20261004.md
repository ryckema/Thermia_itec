# PROTO-OFFLINE-51 — Calendar cross-capture forensic pass including new ATEC/DCM03 capture

**Date:** 2026-10-04  
**Status:** **COMPLETE / POSITIVE STRUCTURAL RECONFIRMATION; NO NEW WRITE SEMANTICS**  
**Hypothesis:** the new ATEC/DCM03 cold-start capture may provide calendar variation not present when CAL-OFFLINE-01 was closed.  
**Controlled change:** add the ATEC 12-page calendar snapshot to the existing legacy/Eco5 structural comparison. No TX.

## ATEC result

The ATEC capture contains the complete twelve-page ordinary calendar transport:

`055A/33 ... 06C5/33`.

After logical re-alignment to `4 × 98 words + 4-word tail`, the ATEC calendar is **word-for-word identical to the legacy 20260925_090550 calendar for the first 392 words**.

There is exactly **1 difference out of 396 words**:

- absolute `06E2`: legacy `206` -> ATEC `214`.

`06E3`, `06E4`, `06E5` remain unchanged.

### Strong conclusion

The new ATEC capture independently reinforces the existing logical calendar model:

- F1..F4 boundaries;
- 8×12-word records;
- metadata0/metadata1 positions;
- legacy profile slot content.

It also strengthens the conclusion that the four-word `06E2..06E5` tail is **not part of editable calendar slot state**.

`06E2` can vary while the entire 392-word calendar-function payload remains identical.

## Eco5 cross-capture difference

Between the first full Eco5 snapshots from 20260926 and 20260928 there are exactly **2 differences**:

1. logical offset 308 / absolute `068E`: `20 -> 21` — the already-known F4 slot1 start-hour change;
2. logical offset 392 / absolute `06E2`: `107 -> 108`.

Because `06E2` is already linked structurally to the `0870` operating-time bridge, its +1 change must not be attributed to the F4 calendar edit.

## Metadata / weekday result

The ATEC snapshot adds no discriminating weekday subset:

- legacy/ATEC records use mode0 with weekday masks `0000`;
- Eco5 weekly records use `007F`;
- no Monday-only/weekend/weekday subset appears.

Metadata1 remains zero in every complete compared snapshot.

Therefore the exact weekday bit order and metadata1 meaning remain offline-unresolvable.

## Desired-state/write result

The new ATEC capture adds only the genuine `W0 bit0 -> 0546` desired pull.

It contains **no calendar desired-page FC03 pull**.

Therefore CAL-OFFLINE-01's safety conclusion remains unchanged:

- no calendar W0 selector may be inferred merely from page-index symmetry;
- no cross-page calendar writer is justified.

## Result

The new ATEC capture does improve confidence in the passive decoder structure and tail separation, but it does not reopen the calendar write path.

## Live status

Unchanged.