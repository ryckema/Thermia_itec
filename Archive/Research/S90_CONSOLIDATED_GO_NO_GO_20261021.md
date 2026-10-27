# S90 — Consolidated V4.1 ↔ V5 TX readiness decision (2026-10-21)

**Milestone status: RUNNING / PARTIAL. Decision for live native TX now: NO-GO.**
This review consolidates S90-A/B/B2–B9 and FIX1 without treating auxiliary checks as additional milestones. No firmware modification, flash, or physical TX performed as part of this review.

## OBSERVED FACTS / provenance
- **Local user test evidence:** V4.1 EXP386/387 showed historical native writes on user's XTR M; EXP388 remains PARTIAL. This does not prove V5 native session.
- **User live S88 P5:** native FC16 observer recognized 84 in its window (28 085F/5, 56 04A6/13), RX parsing stable, zero physical TX attempts, HARD_DENY. S89 formal closure still to review separately.
- **Exact S88 P5 source:** V5 NativeEsphome23, scoped transport and guarded UART adapter present. IDF-specific adapter uses uart_tx_chars, uart_wait_tx_done and MCU-pad-level DE readback; fail-closed zero-budget defaults. Source/host checks positive, embedded behavior not physically established.
- **Original Service43 source/host report:** B11D and watchdog callback join with existing GuardedPort owner was host-positive. Service43 archive itself is a different private source parent and must not be silently identified as S88 P5.
- **S62 local TTL timing:** G01/G02/G04 operationally closed by user-accepted risk for unchanged topology, not physical role/slot proof; do not reopen mechanically. G05/G06 electrical drain/DE behavior still unverified.
- **ESP32-S3 compiler evidence:** user provided successful ESPHome 2026.9.0 / ESP-IDF 5.5.5 app+bootloader build, factory/OTA/ELF generated. Log reads thermia-itec-xtr-m.yaml, not explicitly named S90B9_FIX1 diagnostic YAML. Thus target build is proven; compiler inclusion/execution path of named diagnostic adapter is not proved from the log alone.
- **S82 regression:** original brittle exact-text release-gate test still FAIL, while additional structure and host tests passed. Do not silently treat source-text replacement as runtime semantic proof.
- **No genuine Connect/DCM hardware** available; ATEC V3 external source/claimed function is not XTR proof and its protected material remains private.

## STRONG CONCLUSIONS
Existing RX-only production installation is not a suitable live TX candidate. Merely compiling a diagnostic include cannot establish native session binding, physical hardware completion or a scoped send authorization. S90 does not need another independent mock/protocol experiment: one exact integrated private-source implementation review plus target-aware guard tests is needed.

## GO/NO-GO checklist for a future **prepared** S91
1. **Exact artifact lineage:** one pinned private V5 source tree, matching complete YAML, with preservation of current V5 parser, HA, B11C/B11D, valid-frame counters, stale watchdog, existing controller/peer/slot accepted-risk scope. No secret/protected logic publicly committed.
2. **Real lifecycle:** source-backed evidence feeds the actual existing NativeEsphome23/session state machine, with no forged epoch or supervisor flags; passive 32/32 alone never binds or arms. Correct guarded single-response transaction with staged FC16 cache and delivery/readback semantics; fault/timeout reset and restart.
3. **Target-aware transport:** actual ESP32-S3/IDF compilation of the same implementation (not header-only diagnostic), bounded FIFO admission + drain, unresolved-inflight latch, DE returned LOW within reviewed guard, no second UART/DE owner; B11D/watchdog supervision preserved. GPIO readback is MCU-pad proof, not independent transceiver electrical proof. Any unreviewed difference: fail closed.
4. **Test and rollback:** negative behavior cases (stale/replayed epoch; invalid slot/peer; B11D fault; UART FIFO/drain error; DE disagreement; disconnect/restart; repeated requests) and no automatically enabled TX. A complete first S91 proposed experiment must specify controller-origin trigger, single exact payload/CRC derived from observed source, reply window, timeout, stop criteria and recovery to verified S88 P5; actual TX only user-initiated.
5. **User-facing handoff:** one complete private ZIP for build/flash when ready, with source manifest, full YAML, README, only Configuration controls, red/brown test logs, and exact evidence request. No standalone mock ZIPs as a substitute.

## HYPOTHESES / OPEN
Whether the integrated private V5 lifecycle and IDF physical owner on the actual ESP32-S3 are equivalent to historical V4.1 positive behavior; real physical DE-low and last-stopbit safety; actual XTR acceptance of full Connect/Online session and semantic setting changes.

## NEXT ACTION
Do **one bounded integrated offline source/target review** on the exact newest PRIVATE V5 parent and produce a single S91-ready or NO-GO verdict. Do not run new passive XTR recordings, repeat S62 ownership tests, flash the diagnostic build, or start bus TX under this document. S91/S92/S93 remain PREPARED / NOT RUN.
