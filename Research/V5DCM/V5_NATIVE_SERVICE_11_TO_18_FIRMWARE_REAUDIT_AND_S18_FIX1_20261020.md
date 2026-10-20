# V5 Native Service 11–18 — genuine Connect firmware re-audit and S18 FIX1

**Date:** 2026-10-20. **Audit ID:** V5-NATIVE-FIRMWARE-REVIEW-01. **Status: COMPLETE / POSITIVE (OFFLINE SOURCE AUDIT AND PASSIVE REPLAY ONLY).** Service-11–18 remain PREPARED / NOT RUN as XTR live experiments.

## Evidence and provenance
- Genuine original Connect **2.1.105** source inspected from user-uploaded `2.1.105 extracted_appfs.zip` and `device_client.zip`. Nine code modules checked byte-for-byte identical: `cm/modbus_server15.py`, `cm/client.py`, `cm/genesis.py`, `data/info.py`, `data/param.py`, `data/service.py`, `data/parsers.py`, `state.py`, `events.py`.
- Original Connect `etc/device-client.d/930/modbus-flags.json`, `info-2.4.2.json`, `info-2.4.3.json` and `configurations.json` also inspected from genuine AppFS. The **2.0.18** parity is previously documented in `Thermia_Connect_Firmware/findings/CONNECT_2.0.18_VS_2.1.105_PROTOCOL_DIFF.md`, but its original RAUC image was NOT independently re-extracted in this audit.
- Original Write Beta V4.1 GitHub source and private S11/S12/S13/S14–17/S18 code reviewed. ATEC V3 stays EXTERNAL SOURCE, not XTR proof.
- **CRITICAL PROVENANCE:** `thermia_capture_20261003_165355.log` is genuine COLLABORATOR ATEC + classic DCM03, **NOT local XTR**; per `Research/Atec/ATEC_DCM03_COLD_START_20261003.md` and `Research/V5DCM/V5DCM40_HISTORICAL_CRYPTO_PARITY_RESULT_20261019.md`. The 2026-09-25 captures have unresolved exact model identity, per `Research/R6_P74DI_B10_B12_PROVENANCE_RECONCILIATION_20261013.md`. Previous S18 text incorrectly attributed Oct03 and Sept25 results to local XTR: **DISPROVEN / SUPERSEDED**.

## Firmware-derived facts (not local XTR proof)
- `modbus_server15.py`: native CM930 is slave `0x0F`. FC23 approval callback precedes a later FC16 handler; firmware handshake state RESPONSE_SENT and ACCEPTED and application OPERATION are separate. Production FC16 acceptance predicate is permissive, while our safe V5 candidate intentionally requires stronger observed sequence.
- Firmware marks work with `modbus-flags.json`: W0/W1 desired advertisement, W2/W3 requested-current groups, W4 operation request groups. It tracks significant data-package reception separately from a 32-group controller settings bootstrap. `client.py` gates parser publication and cloud onboarding independently.
- Original client supports desired value plus request bits, controller FC03 pull, FC16 controller readback and bounded retry; semantic acceptance is not an FC16 ACK.
- Genuine ATEC+DCM03 32-page bootstrap is model/profile-specific; e.g. starting `0x03E8/count13`, not locally mapped XTR `0x03E8/count14`. Header equality, page-order counters and 32/32 cannot be transferred mechanically.

## Service-11 through Service-18 implementation review
| Service | Actual present code | Firmware-parity gap |
|---|---|---|
| 11 | Ten XTR/V4.1-derived initial FC16 pages, host tested | Not complete 32-page profile, startup, native session or current XTR acceptance |
| 12 | Partial FC16/FC03 router | No genuine startup or complete application service, no UART/B11D |
| 13 | Fail-closed startup/0708 classifier | Recognition only, not original firmware approval/messaging |
| 14 | Host-attested startup phases + ten-page tracking | Original authenticated provider and independent accepted session not wired; true full 32-page bootstrap unavailable |
| 15 | Constrained 0708 six-word responses | Partial fixed/intended mailbox values, not profile-complete flags, lifecycle and significant-group handling |
| 16 | One-word 03E8 change and exact republish host model | Not general original update event/state/retry model; no local V5 semantic proof |
| 17 | Single offline actor and hard-denied coordinator | UART/DE/B11D/peer/slot not physically bound, readiness deliberately false |
| 18 | Passive RX witness | Initial FC23 detector had endpoints reversed and test fixture mirrored this error; no hardware owner/acceptance evidence |

## S18 FIX1: verified root cause and corrected replay
- Original S18 witness matched FC23 read `071C`, write `0730` and test created the same **wrong** order. Original genuine protocol reads `0730/count8` and writes `071C/count8`. **29 bytes is the correct complete RTU frame length, unchanged from S18**.
- Private FIX1 changes only passive FC23 classifier and its regression test; proper read/write fields, eight-word counts and 16-byte payload length required; no response handling or secret copied.
- Direct genuine ATEC+DCM03 Oct03 replay now returns **1 exact FC23** (previous S18 reported zero), 2687 CRC-valid frames, 162 FC16 request shapes, 162 unattributed ACKs, 65 mailbox0708, two 085F. This is **EXTERNAL/CROSS-MODEL genuine DCM**, not local XTR.
- Sep25 071517 replay: 674 CRC-valid, zero exact FC23, 40 FC16, 40 ACK-shaped, 18 mailbox polls; model identity UNKNOWN, not local-XTR-proven.
- Corrected unit test checks the CRC-valid real FC23 request and rejects a CRC-valid swapped-address negative. S18 corrected test PASS; existing S14–17 C++17 host suite PASS (17 tests), aggregate 18/18 host-only PASS. The corrected archive is PRIVATE; no protected firmware key/algorithm/handshake response is published.

## STRONG CONCLUSIONS
- Prior S18 reports wrongly claimed local XTR capture and missed an actual genuine approval request. Both are now superseded in the research state while retaining the original report for traceability.
- The observed progression gap is **not** solved by another simulated response/ACK count. A firmware-parity lifecycle adapter and verified physical single-owner boundary remain required.
- S14–S17 'working' means host contracts exercised; **not** a complete firmware-compatible local native session.

## HYPOTHESES / UNKNOWNS
- XTR-specific model/profile, real current authenticated response acceptance, response-slot electrical timing/peer absence and B11D first-start anomaly remain OPEN.
- Legacy 22-page V4.1 resume path has no proven live trigger; do not treat it as the second half of a locally verified modern startup.
- Remaining firmware/2.0.18 original raw parity can be revisited if relevant; prior source-report comparison is not independent re-extraction this turn.

## NEXT ACTION
Use genuine original firmware state axes and **locally authenticated XTR** captures to make a source-to-V5 lifecycle parity matrix first, with acceptance/session/data-package readiness/writes in separate stages. Correct offline RX observer only; don't flash it as if newly verified. Resolve B11D startup and current physical ownership before any user-initiated scoped TX. Keep unchanged V83 FAS1 RX-only as user-verified baseline, `TX=HARD_DENY`, EXP388 `RUNNING / PARTIAL`.

## No-device-action evidence
No ESPHome compilation, no flash, no on-bus TX. No new local XTR session/write confirmed. Private artifact: `V5_NATIVE_SERVICE18_FIX1_FIRMWARE_REAUDIT_PRIVATE_20261020.zip`, SHA-256 `d7bed78d38a82cb8753581563f7dcf3f6fa5be64d30d21b79f355874284b430e`.