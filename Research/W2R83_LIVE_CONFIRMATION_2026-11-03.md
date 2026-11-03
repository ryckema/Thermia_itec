# W2R83 XTR M automatic calendar selection and Apply — 2026-11-03

**Experiment status: COMPLETE / POSITIVE**, scoped to demonstrated selection-driven F1 reads (Programs 3, 4, 5) and one guarded single-field Program 4 Apply. **LIVE / LOCALLY VERIFIED on iTec XTR M, controller 2.4.2**. Source W2R83 built and flashed by the user; logger firmware build reports `Thermia MAIN04-W2R83` at 13:36:56, 13:37:56, 13:38:56. Preserve distinction from tests not run: other individual program write combinations and large multi-field batches are not established by this log.

## OBSERVED FACTS
- Auto-read upon selector change, without clicking Read: `[W2R83] AUTO_F1_READ_ARMED p=3` at 13:37:45; p=4 at 13:38:01; p=5 at 13:38:21; p=4 again at 13:38:31.
- Genuine selected F1 pages `055A`, `057B`, `059C` all return `ACK_OWNED=1`, `seenMask=07`; `REFRESHED` for each selected program. Readback for P4 before edit: `18:20–18:26 days=40` (Sunday).
- Guard worked: an attempted selection while a calendar read was active returned `BLOCKED / calendar transaction active / program selection restored` 13:37:49, no unexpected write.
- User staged P4 start minute `20->21`; preview `STAGING VALID` 13:38:39.
- User explicitly pressed Apply: `BATCH_USER_INITIATED p=4 fields=1` at 13:38:41; `BATCH_FIELD_ARMED step=1/1 reg=057F old=20 new=21`.
- **Physical** one-word writer `CAL_OEMW_ONE_WORD_TX_EXECUTED d=23 reg=057F` at 13:38:43, one attempt without retry.
- Controller-authoritative confirmation: `CAL_EDITOR_FIELD_CONFIRMED p=4 reg=057F actual=21`, `OEMW CONTROLLER_ACCEPTED`, `BATCH_CONTROLLER_CONFIRMED` at 13:38:44–45, controller FC16 page `057B` contains changed word `0014 -> 0015`.
- Post-Apply fresh owned F1 three-page read completes 13:38:50: P4 `18:21–18:26 days=40`, `BATCH_DONE f1Exact=1 pages=1 count=1`, `W2R56 COMPLETE / all fields genuine FC16 + fresh owned F1 3/3 match / F1 selected weekly program saved`. Preview resets to `NO STAGED CHANGES`.
- Integrity at log end: `CRC_CHECK=1926 CRC_DIFF=0 SHAPE_OTHER=0`, RX buffer drops 0; M6/CURRENT4/4 remains operational. No crash seen in this sample. Previously reported W2R79F stack overflow remains a separate open issue; absence from this short W2R83 capture does not close it.

## STRONG CONCLUSIONS
Auto select -> native F1 read -> stage -> one Apply physical TX -> controller FC16 value match -> exact selected-F1 fresh readback **PROVEN** for Program 4 start minute 20 to 21. Read-only source for P3/4/5 **PROVEN**. No reason to change sole S92 UART/TX/DE engine. Transport ACK alone is not the proof; persistence F1 readback is.

## OPEN / NEXT ACTION
A future firmware iteration should diagnose the independent FreeRTOS stack-overflow report without perturbing this locally verified W2R83 path. No further W2R83 write-test required to close this bounded experiment. If reverting user's test minute is desired, use the now locally proven inverse path 18:21 -> 18:20 with explicit Apply; not automatic.

**CURRENT MILESTONE:** automatic native calendar editor.
**DELIVERABLE:** W2R83 LIVE / LOCALLY VERIFIED for above test, private firmware ZIP previously provided.
**REAL BLOCKER:** no blocker for demonstrated calendar workflow; separate stack overflow root cause OPEN.
**ONE NEXT ACTION:** preserve W2R83 production baseline and tackle stack-overflow root cause in next integrated firmware iteration.
