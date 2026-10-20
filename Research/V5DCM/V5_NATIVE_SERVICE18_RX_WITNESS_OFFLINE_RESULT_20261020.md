> **ERRATUM / SUPERSEDED CLAIMS (2026-10-20):** This original Service18 report incorrectly labels `thermia_capture_20261003_165355.log` as LOCAL XTR; it is a genuine collaborator ATEC+DCM03 cold-start capture (Research/Atec/ATEC_DCM03_COLD_START_20261003.md). September capture exact model identity is also unresolved. The Service18 FC23 classifier swapped read/write fields, and the mirrored host fixture hid this defect. Correct 29-byte FC23 request reads 0730/8 and writes 071C/8. Corrected FIX1 sees ONE genuine ATEC FC23 request rather than zero; this is not XTR acceptance. All original results below are preserved as historical erroneous statements and must not be cited as local XTR startup evidence. See V5_NATIVE_SERVICE_11_TO_18_FIRMWARE_REAUDIT_AND_S18_FIX1_20261020.md.

# V5-NATIVE-SERVICE-18 — passive V5 RX integration (2026-10-20)

**Experiment status: PREPARED / NOT RUN** (offline development and historic replay; no new XTR runtime execution).

## OBSERVED FACTS
- Source base: previously user-verified V83 FAS1 RX-only YAML SHA256 `b4aaedf27f8dd3d58fcc7c09316cfe03d9c8f41d40fcd827a31bf1f104d389fa`.
- Prepared additive RX-only YAML, SHA256 `e1a4158a49761f8b45b286b3048ac43a108240117efef17cd00e2b564ffbbd12`. Source integrates one new pure C++17 passive witness into the original single CRC-validated V5 RX callback and adds one Configuration/diagnostic Home Assistant text entity; no new reader or TX code path.
- Strict YAML parser/substitution and structural source-diff checks PASS: all original top-level blocks, existing entities, B11D/watchdog, frame counters, original UART TX calls and DE enable calls preserved. No ESPHome compile performed.
- 18/18 C++17 isolated host tests PASS (17 previous plus new passive witness). Archive is private, SHA256 `11f32a99e70e4504cd8d81a016d13abc96379b47b64117fdbcd346e50e1e7590`; private sources are not published here.
- Local XTR historical capture `thermia_capture_20261003_165355.log`: 2687 CRC-valid frames; 162 0x0F FC16 requests, 162 8-byte ACK-shaped frames of unattributed origin, 65 FC03 0x0708/count6 requests, two FC16 0x085F/count5 requests, **no complete cold-start challenge**. This does not show an active V5 session.
- Another local XTR capture `thermia_capture_20260925_071517.log`: 674 CRC-valid frames, 40 FC16 requests, 40 unattributed ACK shapes, 18 0708/count6 polls. External Eco5 replay remains cross-model evidence only.

## STRONG CONCLUSIONS
- Existing V5 RX callback is an appropriate *passive diagnostic* seam, without asserting electrical owner/response slot/epoch.
- A passively observed FC16 ACK cannot be attributed to any specific physical sender. Ten-page and twenty-two-page counters are *source-shaped observations*, not controller acceptance or proof that the V4.1 legacy resume path can execute.

## HYPOTHESES / UNKNOWNS
- Physical 0x0F owner/slot/peer absence, real startup response provider, current B11D first-start anomaly, full session and semantic controller acceptance remain **OPEN**.
- The S14–S17 engine is still source-only, not bound to UART/DE, with readiness false and TX HARD_DENY. No protected ATEC V3 handshake/authentication code or secret was reused.

## NEXT ACTION
Review B11D startup anomaly and ownership evidence before wiring physical native TX. Independently prove startup-provider/session and exact response timing; continue using the unchanged V83 FAS1 as rollback. No flash and no user-initiated live TX performed for Service-18.
