# Pending canonical reconciliation — CAL-OFFLINE-01 deep reduction

**Date:** 2026-10-03  
**GitHub:** not modified  
**Reason:** current request authorized offline analysis only, not GitHub writes.

## THERMIA_PROJECT_STATE.md — proposed reconciliation

Keep:

- live experiment `EXP388 — RUNNING / PARTIAL`;
- `CAL-OFFLINE-01 — RUNNING / PARTIAL`;
- no live calendar write performed.

Add/refine:

- provenance correction: the `thermia_capture_20260924/25...` captures are genuine older Online/DCM reference captures, not local XTR captures.
- ordinary calendar transport is twelve `0x0F FC16 count33` pages from `055A` through `06C5`, covering `055A..06E5`.
- logical calendar layout is **4 × 98 words + 4-word tail**.
- each logical function is **8 × 12-word records + 2 metadata words**.
- record layout is strongly reduced to:
  `mode, start_min, start_hour, start_day, start_month, start_year, stop_min, stop_hour, stop_day, stop_month, stop_year, weekday_mask`.
- mode0 = DATE / absolute date; mode1 = DAYS/WEEK recurring.
- word11 = seven-bit weekday mask; exact bit-to-weekday order remains unknown.
- metadata0 addresses `05BA/061C/067E/06E0` are strongly supported slot-validity/configured bitmaps.
- metadata1 addresses `05BB/061D/067F/06E1` remain unknown and are zero in compared snapshots.
- genuine Eco5 natural mutation `068E:20->21` confirms F4 slot1 word2 = start hour.
- genuine Eco5 `04A6=0044/04A7=1` begins at approximately the F4 20:00 schedule boundary, strongly associating that state with F4 scheduled activity; exact semantic name remains open.
- F1 = WW_GEBLOKKEERD remains locally proven.
- F2=EVU, F3=Silent Mode, F4=Temperature Reduction remain hypotheses.
- `06E2/06E3` and derived `0870.word0` do not change across the F4 start-hour edit and are therefore not a simple calendar revision counter.
- EXP385 calendar capture attempt was inconclusive/invalid because repeated RX-buffer aborts occurred and zero calendar frames were recorded.

## EXPERIMENT_LOG.md — proposed entry/update

### CAL-OFFLINE-01 — deep reduction update — RUNNING / PARTIAL

**Controlled change:** offline-only reconstruction and cross-correlation of existing genuine Online/DCM captures and the already-recorded local WW_GEBLOKKEERD result. No TX, no YAML, no restart, no setting write.

**New observed facts:**
- complete 396-word calendar transport reassembles to 4×98 + tail4;
- 12-word field layout is strongly established;
- mode0/date and mode1/weekly distinction is strongly established;
- metadata0 behaves as slot-validity bitmap;
- F3 stale record + zero bitmap shows record contents alone do not define slot validity;
- genuine Eco5 `068E` changes 20→21 only, validating F4 slot1 start-hour location;
- `04A6=0044/04A7=1` begins almost exactly at F4's configured 20:00 boundary;
- tail `06E2/06E3` does not change across the hour edit;
- EXP385 produced zero calendar frames and repeated RX-buffer aborts, therefore no local bitmap/delete conclusion can be drawn.

**Result:** major positive refinement, but calendar track remains RUNNING / PARTIAL.

## PROTOCOL_FINDINGS.md — proposed durable findings

- **STRONGLY SUPPORTED:** calendar logical region = 4 function blocks × 98 words + 4 tail words.
- **STRONGLY SUPPORTED:** each function = 8 × 12-word records + 2 metadata words.
- **VERY STRONGLY SUPPORTED:** 12-word record layout:
  `[mode, start_min, start_hour, start_day, start_month, start_year, stop_min, stop_hour, stop_day, stop_month, stop_year, weekday_mask]`.
- **VERY STRONGLY SUPPORTED:** mode0 = absolute DATE; mode1 = recurring DAYS/WEEK.
- **VERY STRONGLY SUPPORTED:** word11 is a 7-bit weekday mask; bit ordering remains OPEN.
- **STRONGLY SUPPORTED:** metadata0 (`05BA/061C/067E/06E0`) is an 8-slot validity/configuration bitmap.
- **OPEN:** metadata1 (`05BB/061D/067F/06E1`).
- **PROVEN / genuine Eco5 structural:** `068E` is F4 slot1 start hour; natural 20→21 mutation changes only that word and persists later.
- **STRONGLY SUPPORTED / genuine Eco5:** `04A6=0044/04A7=1` is associated with F4 scheduled activity.
- **NEGATIVE / exclusion:** `06E2/06E3` and derived `0870.word0` are not a simple calendar revision counter.
- **HYPOTHESIS:** delete/inactivate can clear the validity bitmap while leaving stale record data.
- **HYPOTHESIS:** F2=EVU/power limiting, F3=Silent Mode, F4=Temperature Reduction.
- **STRONGLY SUPPORTED:** `04D8/count27` is separate concrete-drying structure, not a fifth ordinary 98-word function.

## Safety state

Do not implement a calendar writer yet.

Remaining prerequisites before any active calendar write test:
- clean local XTR bitmap add/delete correlation;
- exact weekday bit order;
- desired-page behavior for any logical record that crosses 33-word transport-page boundaries;
- rollback semantics for delete/restore.