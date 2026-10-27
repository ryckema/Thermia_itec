# V5DCM21 — offline delivery/provenance audit and memory-only adapter validation
Date: 2026-10-18
Status: **RUNNING / PARTIAL** for V5DCM21; **offline compilation and regression PASS** for this narrowly scoped substep. No live experiment took place.

## Hypothesis
A native response's preparation, the local platform's delivery report, independently attested controller/slot/epoch evidence, physical line observation, firmware-internal `RESPONSE_SENT / ACCEPTED`, and higher-level Connect application readiness must remain **distinct**, even when a low-level UART output call reports success. An offline read-only auditor can reject stale or inconsistent delivery records without generating native responses or granting TX.

## Known-good baseline, past results, safety
- User-flashed **V5DCM19 FIX1 RX-only** remains the **verified live baseline**. V5DCM20 **COMPLETE / POSITIVE** passive 18m33s and zero software-reported physical TX attempts. Exact installed YAML/ZIP byte identity remains **OPEN**, so neither this auditor nor a new YAML is installed.
- Earlier V5DCM21 offline: 24 Core/readiness checks, 46 RX-join checks, 30 Python firmware-like vs C++ classifier model splits, 34 public production lifecycle callsite checks, five passive geometry smoke cases and four temporal shape cases; exact embedded/portable Core parity verified.
- Original V5DCM18 full seven-corpus stateful reference-Core replay remains RUNNING / PARTIAL. V4.1 EXP386/387 locally positive, EXP388 partial. Accepted residual G01–G06 unchanged.
- NO new physical TX, no FC23 challenge-reply body or recovered security algorithm, no 0x0708 command-mailbox tooling, no device-side send timing, payload, slot assumption or speculative write.

## Source examined: actual portable adapter semantics
- `portable/xtr_platform.hpp/.cpp`: `DeliveryResult::delivered()` means `DeliveryCode::Delivered`. `PlatformPort::accept()` validates its generic guarded response record, then tries `enter_tx`, `write`, `flush`, and unconditional `enter_rx`. A successful return means these **local callback statuses**, not independently observed electrical signalling and not controller receipt.
- `portable/xtr_adapter.cpp`: response-generating processing occurs in a **candidate copy** of the pipeline. On `output_enabled=false`, candidate response state is not committed, delivery is absent, and no platform output call occurs. On local `delivery.delivered()`, staged state is copied to the live pipeline; failure sets `output_blocked`, candidate state is discarded. Non-response passive observations may be committed; the post-TX rule does not ban general passive ingestion.
- `portable/xtr_esphome_bridge.hpp`: `kLiveTxEnabled=false`, `TxDisabledHalfDuplexIo`; no physical output hook.
- No public native private-approval response class or security implementation exists in the current portable response assembler. Generic FC16 ACK responses used by host tests are **not** a native FC23 approval.

## One controlled change family: pure offline delivery audit with regression fixture
New source in `ryckema/Thermia_Connect_Firmware`:
- `portable/xtr_v5dcm21_delivery_audit.hpp`: public header, **diagnostic-only**, no I/O or mutable Core reference. Receives an existing `AdapterEvent`, read-only `State` and explicitly independently sourced `ExternalDeliveryEvidence`. Checks request CRC/geometry/native slave, dispatch/owner/class/record consistency, monotonic sequence, matching delivery sequence, platform-reported result and commit alignment. Exposes `response_prepared`, `platform_delivery_reported`, independent session-evidence conjunction and externally attested wire correlation as separate diagnostic booleans. Defaults all evidence false. **Hardcoded non-authority:** `native_response_sent_inferred=false`, `controller_accepted_inferred=false`, `application_ready_inferred=false`, `tx_authorized=false` in every code path. `revoke()` increments a *local observation generation* (NOT controller boot/epoch) and clears sequence state; its new generation still requires separate external attestation. File created `b216c8f7`, header include correction `bf2833c4`.
- `portable/test_xtr_v5dcm21_delivery_audit.cpp`: synthetic request and **generic FC16 ACK only**. Tests default host delivery without provenance, duplicate/stale sequence, no commit, mismatch delivery sequence, rejected/faulted platform, no delivery prepared-only, foreign slave, policy-open owner, broken response CRC, missing exclusive slot, source-generation revocation, stale controller epoch, unhealthy Core, no record. Positive fake external evidence is explicitly *synthetic* and never grants native acceptance. Added **real adapter integration against `MemoryHalfDuplexIo`**: one host-only normal generic FC16 ACK with local delivered report and one host-only simulated Flush failure; verifies dropped staged state, blocked output and restoration of RX. This is a **memory-only host simulation**, NOT an authorized real ESP32 transmission.
- `.github/workflows/v5dcm21-readiness.yml`: strict C++17 `-Wall -Wextra -Werror -pedantic` actual HEAD build and required test execution. Test/CI commits `3aebfbf1`, `9dae7b17`; added full adapter-memory integration commit `105735f5543dc009422c76e61d292b20145ad006`.

## Actually executed evidence
Latest mandatory GitHub Actions [39122071866](https://github.com/ryckema/Thermia_Connect_Firmware/actions/runs/39122071866), firmware commit **`105735f5543dc009422c76e61d292b20145ad006`**, **COMPLETE / SUCCESS**. Exact job logs:
```text
PASS V5DCM21 actual HEAD C++ readiness/observer 24 assertions; TX permanently denied
PASS V5DCM21 RX-only joined adapter 46 checks, full cold spine without owner or TX
PASS V5DCM21 offline delivery audit 22 assertions; no acceptance or TX authority
PASS passive-capture metadata smoke: 5 synthetic cases, no session/TX promotion
PASS embedded Core exact source parity and C++17 compile
PASS V5DCM21 FC23->FC16 metadata: 4 synthetic scenarios, response content unexamined, session and TX unproven
PASS V5DCM21 model split: 30 source/API assertions; Python internal ACCEPTED is not physical owner, response delivery or Connect application readiness
PASS V5DCM21 public production lifecycle callsite guard: 34 checks; 28 source files; no automatic session promotion
PASS: source output hard-deny invariants
```
All jobs in the dedicated workflow passed; no failed mandatory steps. Other long-running workflows have distinct semantics and are not substituted for this strict run. Physical electric waveform and genuine Online status were not tested.

## Evidence classification and limitations
**PROVEN / public source plus host CI:** `DeliveryCode::Delivered` marks a platform-level callback outcome; generic memory fake can produce this without a physical bus. Delivered, rejected, faulted, absent and mismatched completion are distinguishable; read-only ledger denies duplicate sequences. Output-disabled actual bridge still cannot call platform TX. Fully synthetic external evidence flags do **not** flip any authorization booleans.

**STRONGLY SUPPORTED:** actual native handshake transitions must not be driven by CRC-valid response shape, platform delivery success or a model-internal `ACCEPTED` without separate proof of current controller/session/owner and the actual application profile/required packages.

**OPEN / UNKNOWN:** external independently measured controller boot/session epoch; owner arbitration and collision-free exact response slot; physical DE/electrical delivery; native FC23 response delivery from a private adapter; actual XTR controller acceptance, app `OPERATION`/all-data-packages, semantic readback and Online icon; original deployed FIX1 source provenance. `ExternalDeliveryEvidence` is a **container for yet-unavailable attestations**, not a provider of them. Local `revoke()` is not a remote power-cycle witness; a restarted producer would need its own immutable identity to prevent forged/stale carryover. Static source/host assertions are not electrical certification.

## Positive/negative/inconclusive criteria, abort and next action
- **Offline source checks:** PASS: 22 new strict source-backed host assertions plus prior suites, no native approval inference or output authority, generic fake adapter Flush failure correctly discards response-dependent state.
- **Live experiment:** **NOT RUN**, so overall project remains **RUNNING / PARTIAL**, not COMPLETE for functional native integration.
- **Negative tests:** synthetic denied/rejected/failed/stale events rejected as designed; not new on-device negative results.
- **Abort:** any actual TX, unbounded retries, leak of native private response algorithm/mailbox tooling, modified production HA/YAML or faulty source-core parity. None occurred. Rollback source only: revert standalone audit header, test and workflow entries; installed known-good ESP unchanged.
- **Next most useful action:** offline provenance-source audit for real *source/slot/epoch attestations* from existing XTR data, then a private response-delivery adapter interface and app/profile/package evidence gate. Do **not** implement/generate public challenge-response bytes, claim user hardware delivery, or use synthetic witness flags to authorize new TX. Original full V5DCM18 seven-corpus stateful replay is still partial and could yield more useful existing evidence before a live experiment.
