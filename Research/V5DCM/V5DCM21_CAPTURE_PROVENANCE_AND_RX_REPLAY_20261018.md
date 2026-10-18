# V5DCM21 — provenance audit + genuine capture passive geometry replay (2026-10-18)

**Overall V5DCM21: RUNNING / PARTIAL.** This bounded offline capture-replay substep is **COMPLETE / POSITIVE** for repeatable parser/cold-reference diagnostics, **not** for live Connect/DCM functionality.

## Hypothesis and source basis
A passive, source-traceable capture validator can independently confirm the portable observer's strict cold sequence behavior on available RTU captures without a new UART listener, approving a native handshake or touching the bus.

Known-good local baseline remains **flashed V5DCM19 FIX1 RX-only**, **V5DCM20 COMPLETE / POSITIVE** 18m33s parity/no physical TX. Existing source-level RX integration CI 22 readiness + 43 joined adapter checks passed. Accepted G01–G06 residual risks unchanged; full original V5DCM18 Python reference-Core seven-session stateful replay remains PARTIAL.

## Deployed production source provenance limit
Direct recursive GitHub-tree inspection (2026-10-18) of `ryckema/Thermia_itec` (356 tracked paths) and `ryckema/Thermia_Connect_Firmware` (678 tracked paths) **did not locate an exact deployed `V5DCM19_RX_ONLY_FIX1_20261018.yaml` or its ZIP**. Relevant [V5DCM19 FIX1 report](V5DCM19_FIX1_DUPLICATE_INTERVAL_20261018.md) says earlier prepared ZIP was based on an archived V5DCM2 source and **was not byte-verified against the flashed FIX1**. The live user-supplied V5DCM20 logs do prove RX-only operation but not the exact YAML bytes/source branch. Therefore **production callback equivalence is unresolved**. This is not permission to substitute the simplified public `V5/thermia_v5_session_bridge02_rx_only.yaml` or a rebuild YAML as the actual installed baseline. No production YAML, source callback or HA entities changed.

## Controlled offline change
New `Thermia_Connect_Firmware/tools/validate_v5dcm21_passive_capture.py` implements **metadata-only** chronological replay of exactly 32 public FC16 cold-page geometry pairs, plus 0x0F FC23 presence and CRC validation. It outputs only bounded observation counters, always `native_session_accepted=false` and `physical_tx_authorized=false`. Its input is existing **already saved local capture files**: no device contact, TX, ACKs, native response bytes, mailbox payload interpretation or security transform. `tools/test_v5dcm21_passive_capture.py` adds five synthetic assertions: cold 32/32, omitted page, interleaved nonsettings 085F, FC23 reset, CRC failure. Workflow `.github/workflows/v5dcm21-readiness.yml` runs these mandatory tests. No genuine/raw capture uploaded or published.

## Observed replay results (actual local capture files, not synthetic)
All input lines were checked as whole-frame RTU records and CRC validated:

| Provided source (SHA-256 prefix) | Parsed CRC-valid rows | 0x0F FC23 observed | Valid 0x0F FC16 full requests | Maximum strict cold run | Full cold run |
| --- | ---: | ---: | ---: | ---: | ---: |
| `itec_eco5_gateway_20260926.log` (`3836b7885dfe`) | 10,719 | 101 | 1,058 | **28/32** | 0 |
| `itec_eco5_gateway_20260928.log` (`55583e2ec2cd`) | 9,174 | 68 | 1,105 | **24/32** | 0 |
| `thermia_capture_20261003_165355.log` (`149180652972`) | 2,687 | 2 | 162 | **0/32** | 0 |

Every parsed record in these three provided files passed CRC (0 invalid). The Sep26/Sep28 material is **cross-model Eco5 collaborator data**, not local XTR proof. This result agrees with the previously documented strict max 28/32 and max 24/32 in [V5DCM18 replay](V5DCM18_INTEGRATED_OBSERVER_REPLAY_20261018.md). The available 2026-10-03 file is **only a 26.480–338.043 second fragment** containing no initial FC16 `0x03E8/count14`; consequently this replay cannot see a full cold run there. **Its 0/32 does not disprove the previous 1×32/32 result from a different/full historical October corpus**.

Important limit: this script independently mirrors the portable join's *observation* logic and checks raw-file CRC, but does **not** execute the actual C++ observer on these three capture files. Exact original Core stateful replay and physical semantics remain outside this substep.

## Executed build and regressions
Local Python syntax/behavior executed against the three uploaded files, and five synthetic regressions ran PASS. Independently GitHub Actions [39116725303](https://github.com/ryckema/Thermia_Connect_Firmware/actions/runs/39116725303) at firmware commit `e39b81107fb492ee7498b2771e6920a71be82920` confirmed:
- original strict C++17 Core + observer build PASS and **22 checks PASS**;
- existing portable adapter+RX join build PASS and **43 checks PASS**;
- new Python capture-validator synthetic smoke **5 cases PASS**;
- source TX hard-deny invariants PASS.
All mandatory workflow steps concluded success. This CI **did not have access to the private uploaded real captures**; only the local execution above uses them.

## Decision, safety and next action
- **PROVEN / source-and-capture offline:** exact SHA-256 identified files, CRC soundness, max strict geometry progress, no session authorization in implemented diagnostic; actual C++/Python regression jobs passed.
- **STRONGLY SUPPORTED:** present Eco5 partial cold-reference behavior; existing observer must not treat incomplete/retained sequences as universal disqualification.
- **OPEN / UNKNOWN:** byte-verified flashed FIX1 YAML and exact CRC-valid callback, independently sourced physical epoch/owner/slot, genuine native acceptance, private firmware-dependent challenge response, Connect Online icon/cloud, HA runtime semantics.
- **Negative/abort:** zero live actions performed, hence no device abort triggered. No new TX payload, target register or timing authorized; rollback is leave flashed FIX1 alone.
- **NEXT:** source-provenance gate: obtain/locate exact deployed FIX1 YAML/ZIP or its immutable hash and wire only into its existing completed-frame callback after preserving top-level production entities, diagnostics and TX hard-deny. If exact source unavailable, do **not** claim installed integration or prepare flashing; offline source/capture research can continue.
