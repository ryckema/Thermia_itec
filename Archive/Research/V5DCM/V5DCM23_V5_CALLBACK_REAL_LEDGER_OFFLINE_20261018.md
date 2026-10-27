# CI VERIFICATION UPDATE — 2026-10-18

GitHub Actions [39140420159](https://github.com/ryckema/Thermia_Connect_Firmware/actions/runs/39140420159) completed **SUCCESS** on source commit `755cfd28929bb82a6a3caf0b28265f85278b58b8`, including strict V5DCM23 real-ledger V5 callback compile/execution and existing Core/portable parity/output-hard-deny regressions. The scoped OFFLINE SOURCE+TEST substep is now **COMPLETE / POSITIVE**. Actual private ESPHome integration, source provenance and deployment remain **PREPARED / NOT RUN**; no new device operation occurred.

---

# V5DCM23 — actual portable package ledger at V5 completed-frame boundary

**Date:** 2026-10-18
**Status:** RUNNING / PARTIAL — source and mandatory CI test committed; execution result pending. No firmware flash or active bus TX.

## Evidence and known-good baseline
User confirmed the private V5DCM22-on-V5DCM19 RX-only candidate is running and supplied `Pasted text(20261018-151745).txt` (17:14:29–17:17:26, approximately 3 minutes, uptime 33→183 s). 6 live `[V5DCM22] RX33` samples: exact geometry `0x03E8/14` only; W2=0/W3=1/W4=0, `sinceBoot=1/33`, exact occurrences 28→168, wrongGeom=0, fc23=0 and revoked=0. B11C and B11D each report six consecutive zero-difference RX checks (last B11C 1568/1568, B11D 1564/1564), resync/drops/IO TX=0. Existing production temperature/DHW readings update. The software native executor reports HARD_DENY and physical_attempts=0. Independent electrical TX proof not supplied. Native C2/Online/owner and actual controller epoch remain unproven.

**Important warning:** ESPHome at 17:14:32 reports `OTA rollback detected! Rolled back from partition 'app1'` with prior reset before boot marked successful. The currently running image emits V5DCM22 logs, but neither binary/source hash nor reason for previous rollback is proven; do not infer actual partition solely from cached configuration filename `waveshare-thermia_GAP51D_CLEAN_RX_ONLY_PREPARED_NOT_FLASHED.yaml`. Avoid unnecessary new OTA until boot provenance is understood.

## Hypothesis and one scoped change
The interim private V5DCM22 shape witness duplicates data already represented by the repository's tested `PassivePackageIntegration`. Before further deployment, prove an adapter can feed that **actual C++ portable ledger** using only bytes passed from an existing complete V5 RX frame callback. No duplicate UART parser, external serial reader, ACK, FC23 response or TX.

In `ryckema/Thermia_Connect_Firmware`:
- `portable/xtr_v5dcm23_v5_callback_gate.hpp`: `V5CompletedFramePackageGate` owns the existing `PassivePackageIntegration`, accepts the original full wire byte vector from an existing callback, selects 33 source-derived CM930 XTR 2.4.2 profiles only with explicit caller validation, and revokes evidence on CRC/integrity fault, source transition, bus return or epoch label transition. No TX or claims of real epoch/owner.
- `portable/test_xtr_v5dcm23_v5_callback_gate.cpp`: checks unvalidated-profile denial, repeated valid 03E8/14 counting once, rejection of 0410/21, acceptance of 0410/22, session/source revoke, corrupted CRC revoke, epoch reselection and no physical authorization.
- Strict GitHub CI added compile and actual-host execution at source commit `755cfd28929bb82a6a3caf0b28265f85278b58b8` and workflow run [39140420159](https://github.com/ryckema/Thermia_Connect_Firmware/actions/runs/39140420159). **At documentation time CI was IN PROGRESS**, so not a claimed PASS.

## Verification boundary and next action
**Source committed only**, CI status pending. Critically this adds an interface in the public firmware repository; it **has NOT replaced** the interim observer in the user's private flashed ZIP or run on the real ESP. The private ZIP's exact flashed bytes/OTA partition remain unproven. Source-only change has no outgoing payload, target register or transmission slots; no hardware recovery needed. Do not mark the overall native integration complete.

Next offline: confirm CI, reconcile exact original V5 callback signature/private ZIP source, embed the portable headers into the candidate without duplicating the observer or triggering extra UART allocation, and do exact HA/entity/state_class inventory comparison. A new candidate must preserve production and remain strictly RX-only. Only then plan controlled user-initiated live testing.
