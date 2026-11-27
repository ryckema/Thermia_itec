# W2R88F3 — EVU2 programmed weekly restoration

**Status:** W2R88F2 previous EVU2 five-field setting COMPLETE / POSITIVE; subsequent restoration attempt COMPLETE / NEGATIVE (blocked before physical TX). W2R88F3 SOURCE / OFFLINE TESTED, PREPARED / NOT RUN.

**LIVE source:** User log `Pasted text(20261103-231420).txt`. Existing weekly EVU2 slot10, mode1/programmed1, started 17:00–19:00 with daymask 0. One explicit user-initiated five-field batch changed it to 18:01–20:01 Monday, with five exact controller-origin FC16 responses and complete fresh owned CAL12 (`CAL32_BATCH_DONE exact=1 pages=5 count=5`). Later staging tried 20:00–20:01/no days, only three changed fields: `NEW-DOMAIN ARM DENIED` and `NONF1_APPLY_DENIED arm=0 fresh=1 exact=1 idle=1 fields=3 NO_TX`. Last authoritative controller EVU2 state 18:01–20:01 Monday; no reverse write was sent.

**Root cause:** W2R88F2 independently forbade zero weekday mask at ARM, Apply, intermediate-order planner, page dispatch, and central S92 source-qualified physical guard. Existing EVU2 was originally programmed weekly with zero weekdays, distinct from an unprogrammed/deleted slot. No reason to repeat already validated 5-field forward write.

**Integrated fix:** W2R88F3 retains exact W2R88F2 production YAML, V5 RX, one UART/S92 TX owner, source/epoch/session/CRC/collision checks, per-field controller FC16 and final owned CAL12. Narrow permission only for existing EVU2 slot10 with fresh exact controller baseline 18:01–20:01 Monday, changed=5 and exact frozen target 17:00–19:00 daymask0. Weekday mask 1→0 must be the final individual word. No new UART path, no automatic parameter TX, no date-mode EVU1 grant, no actual create/delete. Offline strict YAML/1230 unique IDs/32-slot selector, C++ callback/owner syntax, five-step planning, ZIP and unchanged W2R88F2/W2R86 rollbacks all passed. Not target compiled, flashed or live.

**Next user-initiated experiment:** compile/flash W2R88F3. Choose EVU2 slot10, wait actual `SLOT READY` exactly 18:01–20:01 Monday, set Start17:00, Stop19:00, all weekdays OFF; require preview `changed=5`. Explicit 45-second ARM, one Apply. Expect five exact controller FC16, last weekdays register0x05D3 actual0, and new full CAL12 readback 17:00–19:00/no weekdays with `CAL32_BATCH_DONE exact=1 pages=5 count=5`. ABORT on anomaly, inspect real controller, no blind retry. Firmware rollback cannot restore controller schedules. Firmware ZIP `Thermia_MAIN04_W2R88F3_EVU2_ZERO_WEEKDAY_RESTORE_PRIVATE.zip` remains private.

**CURRENT MILESTONE:** full EVU weekly control and restoration to zero selected weekdays.
**DELIVERABLE:** W2R88F3 integrated complete private firmware package, OFFLINE TESTED.
**REAL BLOCKER:** none offline; controller semantic acceptance of last mask0 write still OPEN.
**ONE NEXT ACTION:** user target builds/flashes and initiates one exact EVU2 restoration, then reports final controller CAL12 evidence.
