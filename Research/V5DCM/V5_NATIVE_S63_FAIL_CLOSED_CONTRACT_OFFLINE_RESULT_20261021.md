# Service-63 — Native V5 TX safety contract (offline-only)

**Experiment:** V5-NATIVE-S63-FAIL_CLOSED-CONTRACT-01
**Status:** COMPLETE / POSITIVE — stand-alone OFFLINE reference-model tests (11/11); actual V5 source integration PREPARED / NOT RUN.
**Date:** 2026-10-21

## Baseline and source access
Last user-confirmed installed V83-family RX_ONLY/HARD_DENY and V49 rollback; EXP388 RUNNING/PARTIAL, B11D initial fault OPEN. GitHub S60 and S62 reports verified. S62 explicitly closes G01/G02/G04 as accepted operational risks for unchanged installation, not universal electrical proof. The private S60 source ZIP was searched for in current container and Library, but its raw bytes were not accessible; no false source patch claimed.

## Single offline change
Added a separate, minimal Python state-machine reference model and 11 unit tests for native TX fail-closed recovery. **This is neither private native responder code nor firmware.** No modifications to ESPHome YAML, V5 C++, UART, thermia bus or controller. No secret Connect authentication logic, V3 derivative source, or frames published.

## Tested cases
11/11 PASS: physical TX permanently refused in model; no epoch/no runtime qualification; risk acceptance not fabricated as epoch/peer/slot evidence; owner revoked on epoch change; DE HIGH and unresolved FIFO retain sticky fault; release failure, pad HIGH or nonempty FIFO deny reset; only all-safe reset clears latch but drops ownership; sticky fault and mismatched epoch block requalification.

## Proven / strong / hypotheses / unknown
**OBSERVED FACT (OFFLINE):** Stand-alone reference model passed 11 deterministic Python tests. **STRONG CONCLUSION:** The modeled reset rules can encode conservative fail-closed conditions and highlight integration requirements. **NOT PROVEN:** C++/S60 correspondence, GPIO pad to physical transceiver, UART drain success in ESPHome, actual native Connect session/C2/semantic acceptance. **OPEN:** G05/G06 physical fail-high recovery, target ESPHome compile, B11D first fault, EXP388. No live test, compile or TX happened.

## Acceptance criteria and rollback
Do not treat Python test pass as native V5 source completion. Real candidate must enforce verified typed UART drain and DE-LOW fail-closed, propagate false reset through GuardedPort -> ScopedTransport23 -> NativeEsphome23, keep all guards and HA, keep TX HARD_DENY until separate user-scoped live authorization. Rollback not required because hardware/YAML untouched.

## Next
Obtain readable, exact pinned private S60 (SHA256 e0c7fa49b58d9ef1c68cb90f7226ce42cc6bb2ce886c0c83e296f52299933561); only then implement/analyze code-level S63 integration and test original host regressions and actual embedded compile when available. Don't reopen G01/G02/G04 absent changed system or contradictory evidence.
