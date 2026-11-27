# W2R86 XTR P5 five-field Apply — COMPLETE / POSITIVE

**LIVE / LOCALLY VERIFIED**, controller 2.4.2, log `Pasted text(20261103-210207).txt`, 2026-11-03 22:00–22:02.

Selected Hot Water Program 5: owned F1 3/3 read `18:31–18:36 days=0x20` (Saturday) at 22:00:53.024. User presses one Apply, `BATCH_USER_INITIATED p=5 fields=5 extendedTrial=0` at 22:01:14.021. Five S92/OEMW23 one-word physical sends followed by genuine exact controller FC16 receipts: reg 0x058B 31→30 at 22:01:17.833; reg 0x058C 18→17 at 22:01:22.181; reg 0x0590 36→35 at 22:01:26.551; reg 0x0591 18→17 at 22:01:30.896; reg 0x0595 0x20→0x21 at 22:01:35.248. Each time field delta is ±1, one weekday bit; no extended ARM required. Final fresh owned F1 3/3 at 22:01:40.620 shows `17:30–17:35 days=0x21` (Monday and Saturday), followed by `BATCH_DONE f1Exact=1 pages=5 count=5` at 22:01:40.953. CRC_DIFF 0, RX drops 0, parser resync 0; main-loop stack min free 12718B.

**GO:** existing configured F1 five-field editor validated on two different XTR programs, P4 and P5. No repeated P6–8 microtests absent contradiction. **Separate usability bug:** selected F1 age >300s shows auto read pending but reader does not restart until user changes program; safe NO_TX, fix in next firmware. **Other function writing and deletion are NOT yet proven.** Preserve current S92 UART/DE sole owner and require controller readback.

**Rollback:** currently observed P5 `17:30–17:35 Monday+Saturday`, previously `18:31–18:36 Saturday`; P4 also had temporary test values `20:23–20:38 Monday+Friday+Saturday+Sunday`. Firmware rollback does not undo controller schedule values; user uses deliberate separate Apply and verifies.

**CURRENT MILESTONE:** F1 cross-program five fields — COMPLETE / POSITIVE.
**DELIVERABLE:** W2R86 validated in P5.
**REAL BLOCKER:** none for F1 editor; F3/F2/F4 semantic writes and true deletion still OPEN.
**ONE NEXT ACTION:** implement and bound F3 Silent Mode editor plus expired-F1 refresh fix in next integrated firmware.
