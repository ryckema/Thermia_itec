# V5DCM85 — CM930 vendor state architecture vs historical local XTR session chronology

**Experiment:** V5DCM85-CM930-OFFLINE-SESSION-ORDER-01  
**Date:** 2026-10-20  
**Status: COMPLETE / POSITIVE — OFFLINE source and archived-frame chronology ONLY; NO native XTR TX.**

## Baseline, hypothesis and controlled change

The user-run V5DCM83-FAS1 RX-only snapshot was COMPLETE / POSITIVE for its passive observation scope: first RAW=2 vs V5 expected=2, 1028 independently compared frames with no differences, 1194 parser frames without resync/drops, current FIX2 RX QUALIFIED, software TX0. The prior *separate* V83 startup B11D mismatch is still unexplained; EXP388 remains RUNNING / PARTIAL. Installed FAS1 stays RX_ONLY/HARD_DENY and original V49 remains verified earlier source rollback.

**Hypothesis:** Original Thermia Connect 2.1.105 CM930 source defines discrete nonsecret runtime/handshake/parameter-group states consistent at the abstract level with the real historical October 3 native register event order. **Single offline change:** parse public class/state labels and metadata from exact archived vendor source, re-parse timestamps and Modbus CRC/shape information from the five existing XTR captures, verify stage ordering, never transmit.

Firmware source provenance verified byte-identical between user `device_client.zip` and `2.1.105 extracted_appfs.zip` for `cm_client_type.py`, `modbus_server15.py`, `client.py`, `state.py`. Existing V84 SHA pins of first two source files verified.

## Independent vendor firmware findings — not automatically proven XTR semantics

Firmware separates **HandshakeState** (NOT_ACCEPTED, RESPONSE_SENT, ACCEPTED), **CMClientRuntimeState** (NOT_STARTED, WAITING_FOR_DEVICE_INFO, WAITING_FOR_SET_DEVICE_INFO, SERIAL_NUMBER_UPDATE, OPERATION) and a separate requested-data-package bitmask lifecycle (INITIAL, WAIT_FOR_ALL_DATA_PACKAGE, ALL_DATA_PACKAGE_RECEIVED). Version-dependent profile loading, gathering device information, onboarding/cloud readiness and completeness before parameter-map publication are distinct. State-label presence in real firmware does NOT prove that our passive ESP has completed these stages. The protected native reply/security algorithm, exact private gates and command-mailbox tooling are intentionally NOT included.

## Local historically observed stages — 2026-10-03 capture (capture clock, not electrical wire timing)

Across five Sept24/25–Oct03 captures, **873 CRC-valid frames addressed to 0x0F** (per file 68,116,94,137,458). The Oct03 capture contains 458 0x0F frames: 162 FC16 request-shapes, 162 adjacent FC16 ACK-shapes, 66 FC03 read-shapes, 66 reply-shapes, 2 FC23-shapes.

| Historical event | Timestamp and shape | Confidence |
|---|---|---|
| Two FC23-shaped frames | **27.400 and 27.429 s**; separation 29 ms | PROVEN historical ADU shape/order, not controller cold-start or authenticated peer |
| Config page group | **29.262–61.461 s**, 32 distinct ascending starts `0x03E8` through `0x06F4`; **32/32** requests immediately followed by FC16 ACK shapes in 12–15 ms | PROVEN historical ordering; ACK semantic acceptance not proven |
| First alarm/status page | **61.529 s**, `0x085F`/5, ACK shape | PROVEN |
| First polling | **64.923 s**, FC03 `0x0708`/6, FC03 reply shape | PROVEN |
| First operation page | **65.664 s**, `0x07D0` FC16 request and ACK shape | PROVEN |
| Ongoing polls | 65 requests of `0x0708`/6; neighboring request intervals **4.071–4.332 s** | PROVEN for archived capture-clock timing |

First configuration request follows the second FC23 frame by 1.833 s. Across all Oct03 FC16 traffic 162 request-shaped frames are immediately followed by 162 ACK-shaped frames separated by 12–16 ms. These are capture-logger timestamps, **not measured physical UART EOF/drain, slave ownership, semantic application, or safe TX slots**. The beginning of a logging file does not establish a controller reboot/epoch. Historical first `0x03E8`/13 is one profile geometry only; current XTR profile remains UNKNOWN. Historical 0x0867 raw22 (V84) is not a confirmed present-day controller software string.

## Conclusions and evidence classification

**PROVEN / LOCALLY CONFIRMED:** ordering in historical XTR capture and CRC/ACK-shaped adjacency, distinct from vendor source facts. **PROVEN / FIRMWARE SOURCE ONLY:** multiple distinct CM930 app state/bitmask levels. **STRONGLY SUPPORTED:** source state architecture is structurally compatible with local historical FC23→settings→alarm→data read→operation stage families. **HYPOTHESIS:** captured FC23 pair belongs to the beginning of a native initial session and historical subsequent stages imply some internal acceptance; no independent physical epoch or genuine Online app is proven. **OPEN:** sender/owner, wire EOF/response slot, present firmware/profile 0x0867, complete live controller ACK/runtime behavior, genuine DCM/Online/APP33/C2/onboarding.

## Reproduction and next action

Read-only package `V5DCM85_CM930_SESSION_CHRONOLOGY_OFFLINE.zip`, SHA256 **4ab764ccc286412f743ae1262549b600c638914134d028730f970a20639a726e**. Contains `audit.py`, `test_audit.py`, source/hash-checked sanitized `evidence.json`, README, detailed RESULT and SHA256 manifest. **19/19 host Python tests PASS**, including intentionally missing/reordered pages, wrong ACK, missing status/poll/operation, CRC corruption and no-sensitive-output assertions. ZIP integrity/manifests verified. No ESPHome compile/flash, controlled device run, controller power-cycle or physical TX. No complete raw ADUs, private response/0x0708 implementations or secrets included.

**Abort:** any source SHA drift, invalid CRC, failed ordered-event assertion or accidental private content; discard offline audit. Physical rollback N/A; running FAS1 untouched. **NEXT V86, NOT RUN:** offline vendor profile-selection and requested-data-group completeness vs 32 native controller pages, carefully distinguishing vendor APP33/C2 from controller ACK progression. Prefer original firmware/captures over new active tests; no isolated live FC23 reply (historical EXP256 resulted in COMM ERR).

See V84, FAS1 user live report, and the three canonical Research files for ongoing reproducibility.
