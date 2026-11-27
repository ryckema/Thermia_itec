# W2R88F2 — first genuine F3 Silent Mode P1 controller-accepted write

**Status:** COMPLETE / POSITIVE for **single-field physical F3 write and controller-origin readback**; RUNNING / PARTIAL for full batch terminal **CAL32 12-page completion** (not captured). Distinguish validated scope precisely.

## OBSERVED FACTS (LIVE / LOCALLY VERIFIED for one physical field)
User supplied 3,065-line ESPHome log `Pasted text(20261103-224922).txt`, 2026-11-03 23:47:17–23:49:13, Thermia XTR M 3N/controller 2.4.2, firmware `MAIN04-W2R88F2` actually TARGET COMPILED / FLASHED / LIVE. ESP restarted by OTA, requalified native M6=5 with authoritative CURRENT 4/4 at 23:48:03.146. Source F3 Silent Mode program1 slot17 was read mode1, programmed1 22:00–23:59 days0x7F at 23:48:44.436. User staged start minute 00→01, `CAL32_TRIAL_ARMED slot=17 changed=1` at 23:48:53.078 and one `NEW_DOMAIN_BATCH_USER_INITIATED slot=17 fields=1 noRetry=1` at 23:48:59.583.

- 23:49:00.103 exact `CAL32_FIELD_ARMED` reg0x061F old0 new1 page0x05FF.
- 23:49:00.426 **`CAL32_SELECTOR_QUALIFIED` slot17 page05FF bit0040 reg061F**, proving W2R88F2 fixes previous W2R88F1 selector denial.
- 23:49:00.596–00.604 **`GENERIC_PAGE_TX_EXECUTED page=05FF count=33`**, **`CAL32_PHYSICAL_SEND used=1/5 reg061F NO_RETRY`** and `CAL_OEMW_ONE_WORD_TX_EXECUTED d=23 reg061F`: exactly ONE physical desired parameter page.
- 23:49:01.580 **controller-origin** `CAL32_FIELD_CONFIRMED reg=061F actual=1 from=controllerFC16`, `OEMW CONTROLLER_ACCEPTED d=23 reg061F actual=1 physicalAttempts=1 receipts=1`.
- 23:49:01.581 independent passive page diff `CAL_OTHER_WORD_CHANGE reg=061F page=05FF word=32 old=0000 new=0001`. 23:49:02.105 `CAL32_CONTROLLER_CONFIRMED step=1/1 actual=1`.
- 23:49:08.457 the native calendar slot entity `14 Calendar | Silent Mode Slot 1` shows **`Programmed; 22:01 to 23:59; Repeats: Every day`**, matching controller FC16.
- Native M6=5, `CRC_DIFF=0`, RX drops=0, parser resync baseline 56 **unchanged** throughout, loop stack minfree ≈12,798B. A single 94ms UART operation emitted the existing ESPHome >50ms runtime-duration warning; no observed bus CRC/RX damage.

**NOT OBSERVED:** at 23:49:02.111 `CAL32_FINAL_CAL12_READ_REQUESTED`, but log ends 23:49:13.135 with **no** `APP_READ_OWNED_RECEIPT_COMPLETE` after request and **no** `CAL32_BATCH_DONE exact=1 pages=1 count=1`. Do not claim full terminal batch success, even though field write, changed authoritative page and HA display update are proven. `CAL_OEMW_ALERT_SENT reg=0584` in legacy log at 23:49:00.528 is an outdated F1-labelled diagnostic; physical intent/sends/actual write are all register061F. Not itself evidence of a wrong physical value send.

## STRONG CONCLUSION
**PROVEN:** existing weekly Silent Mode F3 P1 start-minute offset 0x061F is physically writable using one native OEMW descriptor23 and the sole S92 owner; genuine controller FC16 reports exact desired and page image reflects it. Previous W2R88F1 NO_TX selector denial is resolved. No need to repeat the +1 test. **OPEN:** W2R88F2 full terminal CAL12 after user batch still awaiting evidence; no proof yet for larger five-field F3 batches, F2/F4, create or delete. Do not interpret generic FC16 transport ACK alone as setting acceptance.

## ONE NEXT ACTION
**Read-only observation of existing W2R88F2**: obtain the few minutes immediately after 23:49:13, filtered to `CAL32_BATCH_DONE`, `CAL32_FINAL`, `APP_READ_OWNED_RECEIPT_COMPLETE`, `CAL32_`, and `14 Calendar | Silent Mode Slot 1`. Expected terminal independently owned CAL12 with `22:01–23:59 days=0x7F`; if absent or timeout, fix final-read state machine before another physical experiment. Do **not** repeat 00→01. After terminal GO, separate user-initated return to 22:00 (ARM+Apply) may be combined with a later five-field F3 test only if exact controller state and rollback are preserved. **ABORT:** existing S92 stop/ABORT on anomaly; firmware W2R86 rollback cannot revert already persisted Silent Mode schedule.

**CURRENT MILESTONE:** cross-domain F3 one-word controller-accepted write established.
**DELIVERABLE:** W2R88F2 LIVE proof for register061F; formal batch closure pending.
**REAL BLOCKER:** none for physical one-word F3 setting; terminal owned CAL12 receipt evidence missing.
**ONE NEXT ACTION:** capture terminal CAL32 owned CAL12 (no TX) or diagnose its failure.
