# V5DCM22 — Native Package Integration (offline)
Date: 2026-10-18
Status: **RUNNING / PARTIAL** (source committed; CI execution not independently verified; no live experiment).

## Hypothesis / baseline
Existing source-verified 2.1.105 XTR 2.4.2 significant set consists of 33 groups (15 W2, 10 W3, 8 W4). An independent RX-only observation join can associate completed CRC-valid 0x0F FC16 input with the already existing PassivePackageLedger while preserving local observation generation and invalidating stale evidence on source/epoch/bus boundaries. Baseline is v31 FIX4 RX-only production; existing V5DCM21 Portable Core, PassiveRxJoin and generic ledger retained unchanged.

## One controlled change
In firmware repo:
- `portable/xtr_v5dcm22_package_integration.hpp`: encapsulates existing PassiveRxJoin + PassivePackageLedger. Consumes existing `AdapterEvent` from already completed receive callback; never independently reads UART or calls CompleteFramePipeline::process; requires caller-provided independently validated `ExpectedPackage` map and controller epoch label. Integrity faults, native 0x0F FC23 observation, bus return, input source change or epoch change revoke C2 and require explicit profile reselection. Never claims owner, physical controller epoch, Online, TX or semantic write acceptance.
- `portable/test_xtr_v5dcm22_package_integration.cpp`: 13 synthetic scenario checks including unvalidated profile denial, good/duplicate package, malformed CRC, partial, completed-without-TX, bus/epoch/source invalidation.
- CI workflow adds strict C++17 compile and runtime test at current GitHub HEAD.

**No real 33-group bit mapping embedded in new code.** It must be supplied from separately verified source. The test mapping is purely synthetic and is not native response logic.

## Outcome / evidence
Files and workflow committed and source review complete. **Full compile and GitHub Actions outcome pending independent confirmation**. No production firmware build, user flash, ESPHome YAML update or physical bus test. Therefore no locally confirmed package delivery, C2 or native DCM OPERATION.

## Criteria / risks / recovery
Positive offline: strict current HEAD CI PASS, all existing regressions PASS and no TX authorization. Negative: any build failure, accidental source/epoch continuity retention or authority escalation. Inconclusive live: no user-run device test. Abort on TX path, private 0x0F security logic, unexpected ACK, uncontrolled response or production regression. Recovery: existing v31 FIX4 remains flashed; new source addition is independent and can be reverted without touching production.

## Next
1. Verify actual GitHub CI run of newly committed source, fix issues if any.
2. Wire real source-verified expected package map through a separate read-only configuration adapter, with no mailbox actuation or response serialization.
3. Offline replay existing local XTR capture against single-callback integration; only then prepare optional scoped RX-only device diagnostic.
