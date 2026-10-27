# V5 NATIVE-SERVICE-19..21 — CM930 lifecycle parity, provenance-pinned replay, passive V5 coupling

**Date:** 2026-10-20. **Status:** PREPARED / NOT RUN as a new XTR device experiment. Offline source audits and C++17 replay checks executed; no ESPHome compiler, flash, live TX, or new local semantic write.

## Baseline, hypothesis, and change
- Last user-verified V83 FAS1 RX-only source SHA256 `b4aaedf27f8dd3d58fcc7c09316cfe03d9c8f41d40fcd827a31bf1f104d389fa`, kept byte-identical.
- EXP388 RUNNING / PARTIAL; prior B11D first-start anomaly remains OPEN; TX=HARD_DENY.
- Hypothesis: firmware-parity observation must not promote raw frame shapes into authenticated ACCEPTED, C2 completeness, cloud OPERATION, XTR owner, or physical response-slot evidence.
- One combined offline change: S19 independent passive firmware-axis witness, S20 strict source-provenance historical replays, S21 additive V5 single-callback RX-only integration. No new UART reader, write, DE enable or change to installed YAML.

## OBSERVED FACTS — genuine firmware source
- Independently accessed user-extracted Connect **2.0.18** `appfs_2018.zip` and **2.1.105** `2.1.105 extracted_appfs.zip`. Both original 930 `modbus-flags.json` byte-identical SHA256 `bb0b335eaf4e3a98e5d71d1cd1551e0772fedcfcd3f7d17f3c78e04c21844b9e`.
- Original `cm/modbus_server15.py` in both versions contains separate startup-response and FC16 acceptance transitions. Both exclude FC16 start 0x085F and 0x04BA from the ordinary acceptance qualifier (older version numeric, newer version named constant).
- `cm/client.py` in 2.1.105 separates version-profile loading, significant-package wait, onboarding/OPERATION and parameter-map publication. These internal states are **not** derivable from CRC-valid 0x0F ADUs alone.
- The original firmware cryptographic key/algorithm, protected private 0x0F response logic and challenge/response bodies are NOT republished. ATEC V3 remains EXTERNAL SOURCE/CLAIM, not XTR proof.

## OBSERVED FACTS — bounded offline tests
- Source-only S19 witness differentiates exact FC23 0730/8-read,071C/8-write request geometry from an **unattributed** FC23 response shape, then a **candidate** post-response FC16. Includes software correlation windows (not wire-EOF timing) and rejects swapped geometry, CRC fault, stale cross-window pairings and excluded FC16 start addresses.
- S20 strict SHA256-pinned genuine **collaborator ATEC + DCM03** 2026-10-03 replay: 2687 CRC-valid frames, 1 exact FC23 request, 1 unattributed response shape, 1 candidate qualifying FC16, 32/32 **start-address geometry** sequence, 162 FC16 requests, 65 FC03 0708 polls. This is NOT local XTR acceptance; ATEC 03E8/count13 differs from historical XTR 03E8/count14.
- Second strict hash-pinned 2026-09-25 replay has **model UNKNOWN**: 674 CRC-valid frames, 0 exact FC23 request/reply, 40 FC16 requests, 18 mailbox polls, 1/32 start-address progress. Do not label it locally verified XTR.
- Prior 17 S14–17 C++17 tests independently rerun PASS; S18 FIX1 host test PASS; new S19 C++17 host test PASS: **19/19 host executables PASS**. Two raw-capture replay/source-hash assertions PASS. Firmware 2.0.18/2.1.105 static source/map checks PASS (source presence is not runtime reachability).
- S21 YAML parser + substitution + IDs + existing top-level and HA + V5 parser/B11D/watchdog + UART TX / DE call invariants PASS. One native-`0x0F` only RX callback observer and one diagnostic HA text sensor added; no second UART reader. The S19 witness is always TX-disabled, even on observed challenge/response/32 group shapes.
- Private candidate YAML SHA256 `1901b21c6efebaccbb1cb8a8a42e6c24d0a877b978b0d7135035da93b37721e4`; private reproducible overlay ZIP SHA256 `5fa62c1c5616669ad8dd18e949dab6bb30c47854027cea0a3325d80b9e56f132`. Private archive not published to GitHub.

## STRONG CONCLUSIONS
- Source parity requires **separate** approval observation, authenticated state (unknown), settings bootstrap shape, profile/required data-group completeness, cloud OPERATION, semantic readback and physical ownership.
- A full **ATEC** 32/32 source-shaped bootstrap and observed post-FC23 FC16 do not prove local XTR receipt or an XTR native session. The historical source/mislabeled S18 claims remain DISPROVEN/SUPERSEDED.
- The passive V5 diagnostic seam is source-valid under offline static checks, but compilation and on-device performance remain NOT RUN.

## HYPOTHESES / UNKNOWNS / ABORT
- OPEN: exact current local XTR controller epoch, peer/response slot/electrical timing, independent B11D first-start resolution, native response provider, local accepted profile, C2 significant-group state, semantic write/readback in V5. The V4.1 22-page resume is unreachable legacy source, not live proven.
- Abort any future live TX on unknown slot, peer, original controller epoch, missing CRC/source shape, stale/brownout or B11D fault. Rollback unchanged user-verified V83 FAS1 RX-only. No actual bus TX or flash authorized/executed by these steps.

## NEXT ACTION
Use only properly provenance-tagged **local XTR** user captures/logs to isolate the existing B11D start anomaly and TX-response ownership. Continue the source-verified private approval provider + physical single-owner audit separately. A narrowly scoped live test needs user initiation, exact frame/value/CRC/slot/effect, abort and rollback. Do not flash this offline prepared candidate as proven. 
