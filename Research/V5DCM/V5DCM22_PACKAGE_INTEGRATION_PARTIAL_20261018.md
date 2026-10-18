# Offline raw-capture cross-check (2026-10-18)
Inspected attached `thermia_capture_20261003_165355.log` with a CRC16 Modbus gate and FC16 exact request-length check. **162 CRC-valid 0x0F FC16 requests**, containing **all 33 selected package starts**, but **NOT all matching the local XTR physical geometry**: the captured `03E8/count13` differs from local `03E8/count14`; `0410/count21` differs from `0410/count22`. Thus **31 of 33 selected starts match the XTR expected start/count shapes** in this particular external/reference-style capture. Non-selected `0492/count9` and `051E/count9` also differ from local-profile counts 11 and 10. No local XTR C2 or session delivery conclusion is justified. These frames are historical source captures, not a newly executed XTR/ESP experiment. Replaying all these frames into the strict package ledger MUST leave C2 false without locally correct shapes for the two mismatches.

This refines the next test: add a true byte-for-byte existing-capture regression fixture, explicitly distinguish reference captures versus locally proven XTR geometry; never broaden accepted counts to match reference traffic.
---
# V5DCM22 continuation — source-derived 33-package mapping and replay fixtures

Date: 2026-10-18. **RUNNING / PARTIAL**. Source changes committed, no executed new CI/build confirmed and no on-device run.

From original Connect 2.1.105 CM930 2.3.0–2.4.3 source-derived 33 selected groups, W2=15/W3=10/W4=8, selector bit positions checked against `data/cm930_modbus_flags_map.csv` and physical counts from `data/xtr_portable_profile_xtr_2_4_2.json`. Added `portable/xtr_v5dcm22_profile_242.hpp` as **receive-only** 33-element `ExpectedPackage` mapping. No firmware response commands, mailbox writes or credential/security logic.

Enhanced `portable/test_xtr_v5dcm22_package_integration.cpp` to construct CRC-valid synthetic FC16 frames for all 33 source-derived geometries: before last package C2 remains false, after last C2 can become observed true but owner, TX and native Online remain false; bus-return invalidates it. The fixture is NOT a real XTR capture replay and does not prove real bus delivery. Added profile header to required GitHub workflow path filters. Current GitHub workflow status was **not verified PASS** (connector only returned no PR-associated run for earlier commit; that is not evidence of failure).

Next: confirm strict HEAD build and execution, replay available original local bus captures without assuming 33 pages appear under RX-only conditions, and only after evidence-driven lifecycle review consider adding a deployment RX diagnostic to the known-good YAML. Abort on any physical TX or code that treats package C2 as accepted session. Existing user-flashed v31 FIX4 unchanged.

---
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
