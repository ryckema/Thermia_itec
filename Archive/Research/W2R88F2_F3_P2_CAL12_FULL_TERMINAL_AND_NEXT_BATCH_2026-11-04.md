# W2R88F2 F3 Silent P2 — native terminal confirmation, another 3-field batch and 1-field rollback

**LIVE / LOCALLY VERIFIED, COMPLETE / POSITIVE** for the original previous three-field F3 P2 transaction **and** two more distinct new-domain batches including independent native CAL12 final exact. **NOT RUN** for proposed FIVE-field combined test.

## OBSERVED FACTS — user file
Source: `Pasted text(20261103-230802).txt`, 4,999 lines, Nov 4 local time 00:04:50–00:07:56, W2R88F2 XTR M controller2.4.2 M6=5 CURRENT4/4, native sole S92 owner, CRC_DIFF0 RX drops0 parser resync0, no retries.

### A. Closure of preceding three-field batch
User prior file `Pasted text(20261103-230451).txt` showed user-ARM+Apply `fields=3` at 00:04:26, physical reg0x062B 0→1 (start minute), 0x0630 0→1 (stop minute), 0x0631 8→7 (stop hour), three exact genuine controller FC16 and final native CAL12 request at00:04:38. **New log begins** at00:04:50.364 HA shared status `COMPLETE / POSITIVE / controller FC16 all fields + fresh CAL12 exact`. At00:04:52.131 `APP_READ_OWNED_RECEIPT_COMPLETE requested=12 pages epoch=12167`, at00:04:52.310 native 14 Calendar Silent P2 `00:01–07:01 Every day`; at00:04:52.603 `CAL32_SNAPSHOT_READY slot18`, shared status `00:01-07:01 days=0x7F`. Thus original three-field transaction now **COMPLETE / POSITIVE including semantic terminal fresh CAL12**; its literal `CAL32_BATCH_DONE` event occurred before this new log began or is not separately present, but exact completion status and fresh CAL12 are explicit. Do not invent its timestamp.

### B. New explicit 3-field batch — COMPLETE / POSITIVE
User selected F3 Silent P2 slot18 and staged three, NOT five, changes from actual `00:01–07:01 days0x7F` to `00:01–08:00 days0x7E` (Tuesday–Sunday): stopMinute1→0; stopHour7→8; weekdayMask127→126 (Monday off). `CAL32_TRIAL_ARMED slot18 changed3` at00:05:41.081; single `NEW_DOMAIN_BATCH_USER_INITIATED slot18 fields3` at00:06:00.521. Sole S92 OEMW physical 1-word page0x0620 sends and exact controller-origin FC16 receipts:
- reg0x0630 stopMinute1→0, `CAL32_FIELD_CONFIRMED actual0`00:06:03.439, `CAL32_CONTROLLER_CONFIRMED step1/3`00:06:04.244.
- reg0x0631 stopHour7→8, actual8 at00:06:07.804, step2/3 at00:06:08.247.
- reg0x0635 weekdayMask0x7F→0x7E, actual126 at00:06:12.099, step3/3 at00:06:12.283.
Native fresh full CAL12 requested00:06:12; `CAL32_BATCH_DONE exact=1 pages=3 count=3`00:06:24.348; `APP_READ_OWNED_RECEIPT_COMPLETE requested=12 pages epoch12167`00:06:26.978, source `00:01–08:00 Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday`, shared source rebase. New register 0x0635 1-bit weekday write is now verified live in F3.

### C. Next explicit 1-field Monday restore — COMPLETE / POSITIVE
From fresh `00:01–08:00 days0x7E`, user staged Monday ON (daymask0x7F), ARM00:07:26.388, Apply00:07:31.464 `fields1`, reg0x0635 126→127 physical send00:07:32.839 and true controller FC16 actual127 at00:07:33.816, step1/1 confirmed00:07:34.252. Fresh all-calendar reread requested00:07:34; `CAL32_BATCH_DONE exact=1 pages=1 count=1`00:07:46.244; actual `APP_READ_OWNED_RECEIPT_COMPLETE requested=12 pages`00:07:48.561; 14 Calendar P2 `00:01–08:00 Every day`, shared `SLOT READY ... days0x7F`. No setting retries.

### STRONG CONCLUSIONS
- Two distinct fully terminal **F3** batches (3-word and 1-word) plus independent CAL12 validate current new-domain S92 selector, send, field receipt, multi-step sequencing and semantic terminal controller persistence **LIVE / LOCALLY VERIFIED**.
- Last confirmed controller F3 P2 state **00:01–08:00 daily, daymask0x7F** (not original00:00–08:00; start minute still +1).
- F3 weekday mask reg0x0635 semantic write both directions is now PROVEN. F3 multi-field per-batch 3/3 PROVEN; five-field combined batch **NOT RUN**, do not claim.
- Preserved runtime M6=5 CRC_DIFF0 RX drops0 resync0; sole S92 owner and V5 parser intact.
- User explicitly intends a larger five-field test. No firmware change needed to attempt it; no need for additional one-word or three-word microtests.

## ONE NEXT TEST — PREPARED / NOT RUN
Read current live selected F3 P2 slot18; if `00:01–08:00 days0x7F` is still exact, stage exactly FIVE changed fields in one user-initiated batch to `01:15–07:45 days0x45` (Monday,Wednesday,Sunday). Registers 0x062B startMinute1→15, 0x062C startHour0→1, 0x0630 stopMinute0→45, 0x0631 stopHour8→7, 0x0635 weekdayMask0x7F→0x45. One `Arm New-Domain Write (45s)` plus one Apply; expect `fields=5`, five controller FC16 actual target values, and `CAL32_BATCH_DONE exact=1 pages=5 count=5` with fresh independently owned 12-page CAL12 and actual weekly P2 source exactly target. If baseline differs, recalculate changes before ARM; do not blindly apply old values. ABORT on session/bus anomaly, no blind retry or writes past bound. Restore the originally real-world setting `00:00–08:00 daily` via separate user-initiated ARM+Apply and exact controller fresh readback after experimental success, if wanted (firmware rollback alone does not restore controller calendar).

**CURRENT MILESTONE:** F3 calendar multi-field controller acceptance plus full owned terminal readback — COMPLETE / POSITIVE.
**DELIVERABLE:** W2R88F2 LIVE verified native F3 multi-field engine.
**REAL BLOCKER:** none for 5-field scoped test; F2/F4 create/delete semantics still require separate new implementation.
**ONE NEXT ACTION:** one bounded full five-changed-field F3 P2 batch from fresh `00:01–08:00 daily` to `01:15–07:45 Mon/Wed/Sun`.
