# THERMIA — START HERE

Updated 2026-10-28. For the current roadmap, read README.md / Roadmap first, then THERMIA_PROJECT_STATE.md, EXPERIMENT_LOG.md and PROTOCOL_FINDINGS.md here. These restored public Research files contain only non-sensitive status and recent verified evidence; older comprehensive private September snapshots are not reproduced in the public repository.

**Latest flashed / LIVE / LOCALLY VERIFIED firmware:** private W2R25F4 user-run on XTR M 3N controller 2.4.2, nine Heating descriptors D1, D4, D6–D12 (except D5) with 26 genuine controller-origin FC16 accepted parameter writes across two 2026-10-28 user captures. Preserve M6, CURRENT 4/4, calendar 12/12, V5/CRC, S92 sole UART owner, ABORT, W2R24 rollback and all functioning HA entities. Only D5 Heating Maximum `03EA` lacks verified user evidence; the new log confirms D6 and D12. Other write groups remain ON HOLD.

**CURRENT MILESTONE:** Heating Write User. **DELIVERABLE:** W2R25F4 multiwrite proof for nine descriptors (26 confirmed parameter writes). **REAL BLOCKER:** only D5 lacks controller-semantic live proof. **ONE NEXT ACTION:** One user-initiated D5 write on unchanged W2R25F4; confirm genuine controller FC16 readback and decide GO/FIX/NO-GO. No autonomous flashing or speculative microtest loop.
