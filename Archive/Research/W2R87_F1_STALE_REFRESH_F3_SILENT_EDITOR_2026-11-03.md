# W2R87 — stale F1 re-read and F3 Silent Mode source editor

**Status: PREPARED / NOT RUN; SOURCE / OFFLINE TESTED only.**

**Baseline:** W2R86 is FLASHED / LIVE / LOCALLY VERIFIED on XTR M 3N controller 2.4.2 for F1 P4 and P5 five-field transactions, exact controller FC16 per word, independent owned F1 3/3 and zero CRC errors / RX drops.

## ONE implementation change in full W2R86 firmware

- Fix reproduced stale selected F1 snapshot: original snapshot expires after 300s but old firmware did not re-trigger a native read until program selection. W2R87 re-arms the existing W2R37 reader once per successfully expired snapshot and controller epoch, provided no staged edits and no busy transaction. Unsaved edits are preserved; no uncontrolled reread/parameter TX.
- Original genuine Thermia Connect 930/2.4.2 config independently maps F3 Silent Mode records 1566–1661 (hex 061E–067D), 12 words each; P1 first 2 words cross page 05FF, and further source pages 0620,0641,0662. Programmed bitmap at 1662 (067E), active at 1663 (067F). Original alert/read flags are 1800/1802 with page specific masks. Do not apply F1 physical guard blindly to F3.
- Added F3 program 1–8 selector, four time numbers and seven weekday switches under Configuration (all disabled by default), plus source-checked four-page auto-hydration, Discard, status and a Prepare F3 Write (NO TX) source-plan button. Only already configured weekly programs are eligible. Preparation validates source unchanged and logs exact reg/page/word old/new for each stage; NO physical F3 setting write. Existing CAL12 reader is reused, not a second UART owner.
- New F3 setting physical TX is NOT IMPLEMENTED: future change needs exact S92 owner extension, user-initiated guarded trial, per-field authoritative FC16 and fresh F3 page readback, bounded abort/rollback. Neither other calendar domains nor create/delete is authorized by this release.
- All existing W2R86 FC03/FC16/RX/CRC/S92 native writers, verified Apply, manual hot-rejoin/ABORT, and W2R84 stack diagnostics retained.

## Offline / deliverable
Complete source YAML parsed with secret stub, 1182 unique IDs, all unchanged existing HA components verified, 31 modified/new C++ callbacks GCC C++17 syntax-only passed using stub symbol declarations, no actual ESPHome target compile. ZIP CRC and SHA256 content passed. One private complete artifact: Thermia_MAIN04_W2R87_F3_EDITOR_AUTO_REFRESH_PRIVATE.zip with real single-file YAML, exact W2R86 rollback, diff, manifest, concise user procedure.

**Expected LIVE after user flash:** M6=5 CURRENT4/4 and CRC0; F3 Program1 or Program2 hydrated from native four-source-page data, stage one minute -> Prepare prints F3_WOULD_WRITE NO_TX -> Discard restores without controller write. For F1, after selected source >300s and no staged edits: STALE_F1_REARM, existing AUTO_F1_READ_ARMED, owned REFRESH_COMPLETE; with edits, hold preserves staging. Any novel physical TX: use existing S92 ABORT and restore W2R86 YAML. Firmware rollback does not restore controller schedules.

**CURRENT MILESTONE:** F1 stale native auto reread plus F3 source-qualified HA staging.
**DELIVERABLE:** W2R87 full private YAML ZIP, SOURCE / OFFLINE TESTED; PREPARED / NOT RUN.
**REAL BLOCKER:** none for reads/staging; genuine F3 physical setting writes still lack scoped central S92 owner integration and semantic XTR evidence.
**ONE NEXT ACTION:** user compiles/flashes W2R87 and checks F3 source hydration/NO_TX plan and F1 stale reread before F3 user-armed physical write integration.
