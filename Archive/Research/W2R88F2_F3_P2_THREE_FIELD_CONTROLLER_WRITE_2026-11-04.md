# W2R88F2 F3 Silent Mode P2: three physical writes in one Apply

**Status:** COMPLETE / POSITIVE for **three individual F3 controller-FC16-confirmed physical parameter writes in one Apply**; RUNNING / PARTIAL for the firmware's final whole CAL12 exact-match termination. Five-field target NOT RUN because only three fields were staged.

## OBSERVED FACTS
Source: user `Pasted text(20261103-230451).txt`, ~4723 lines, local ESPHome time 00:01:42–00:04:41 (date likely Nov 4 local). Actual XTR M controller2.4.2, W2R88F2 already live, native session M6=5, CURRENT4/4 epoch12167, CRC_DIFF0, RX drops0, resync0. At 00:02:30.528 native independent first CAL12 12-page read complete. Native F3 Silent Mode P2/slot18 source initially **00:00–08:00 daily** (daymask0x7F), `CAL32_SNAPSHOT_READY slot18 mode1 programmed1` at00:03:46.576.

User selected slot18 at00:03:44.029 and staged only: start minute 0→1 (field0 at00:03:48.861), stop hour8→7 (field3 at00:03:51.162), stop minute0→1 (field2, after intermediate number UI adjustments1→7→1 between00:03:56–00:03:59). **Start hour stayed 0; weekdaymask stayed 0x7F**. `CAL32_TRIAL_ARMED slot18 changed=3` at00:04:26.249, `NEW_DOMAIN_BATCH_USER_INITIATED slot18 fields=3 maxPages=5 noRetry=1` at00:04:26.257, one user activation.

Actual physical one-word OEMW23 page0x0620 S92 sends and controller-origin exact field receipts, each without retry:
1. Register `0x062B` startMinute 0→1: selector qualified00:04:27.649 `bit=0080`; `CAL32_PHYSICAL_SEND used=1/5`00:04:27.834; `CAL32_FIELD_CONFIRMED actual=1 from=controllerFC16`00:04:28.778; `CAL32_CONTROLLER_CONFIRMED step=1/3`00:04:29.230.
2. Register `0x0630` stopMinute 0→1: selector qualified00:04:32.015; physical send00:04:32.187; controller FC16 actual1 at00:04:33.289; `CAL32_CONTROLLER_CONFIRMED step=2/3`00:04:33.292.
3. Register `0x0631` stopHour 8→7: selector qualified00:04:36.368; physical send00:04:36.543; controller FC16 actual7 at00:04:37.505; `CAL32_CONTROLLER_CONFIRMED step=3/3`00:04:38.244.

Native slot sensor seen at00:04:37.405 as **00:01–08:01 daily** *before the last stop-hour FC16*; three exact field receipts together indicate intended immediate controller register state **00:01–07:01 daily**, but post-third-field full slot readback has NOT yet been captured. `CAL32_FINAL_CAL12_READ_REQUESTED noSettingTX=1`00:04:38.246. Existing read-only `APP_READ_REQUEST W2=1FFE`00:04:40.748. Log ends00:04:41 with **no** `APP_READ_OWNED_RECEIPT_COMPLETE` for this final request and **no** `CAL32_BATCH_DONE`. Do not claim terminal persistent/12-page proof.

**BUS:** M6=5, V5 CRC_DIFF0, RX drops0, parser resync0, no physical repeats or S92 aborts. Legacy diagnostic `CAL_OEMW_ALERT_SENT reg=0584` emitted but actual physically executed reg0x062B/0x0630/0x0631 accurately shown by sender and controller; label is stale F1-specific.

## STRONG CONCLUSIONS
The same sole S92 owner supports at least **three different F3 weekly record fields sequentially within one bounded Apply** and confirms each from genuine FC16. Three-field execution is **COMPLETE / POSITIVE at per-word controller level**. Proposed five-field F3 P2 batch did **not** take place: user staged exactly three values, with original start hour and day mask unchanged. Missing final CAL12 is a limited capture gap, not evidence of failure. Do not redo already proved three fields just to reproduce transport/FC16.

## OPEN / NEXT
Before any new physical write, **read exact current F3 P2 slot** using the existing shared Read button; initial source00:00–08:00 is no longer safe to assume. If actual current controller state is 00:01–07:01 daily, one true five-different-field bounded batch can be staged targeting **01:15–06:45, Monday/Wednesday/Sunday (0x45)**: startHour0→1 reg0x062C; startMinute1→15 reg0x062B; stopHour7→6 reg0x0631; stopMinute1→45 reg0x0630; weekdays0x7F→0x45 reg0x0635. Explicit user ARM45s then one Apply. Expected five genuine per-field FC16 plus fresh **postwrite** all12 CAL12 and `CAL32_BATCH_DONE exact=1 pages=5 count=5`. If current values differ, first calculate new target to keep *five actual changes* and valid intermediate times, don't blindly send. Restore original **00:00–08:00 daily** separately after fresh controller proof, if temporary test; use explicit ARM+Apply and final readback. S92 ABORT on anomaly; no blind retry.

**CURRENT MILESTONE:** one native F3 multi-field owner transaction with 3/3 controller-verified writes.
**DELIVERABLE:** W2R88F2 LIVE F3 multi-field semantic acceptance, scope three fields; original 5/5 still open.
**REAL BLOCKER:** no real blocker for controller-write per-field; 12-page terminal CAL12 after this batch not in provided capture.
**ONE NEXT ACTION:** one fresh owned F3 P2 read; if 00:01–07:01 daily, stage one five-different-field target and run bounded test with terminal 12-page log.
