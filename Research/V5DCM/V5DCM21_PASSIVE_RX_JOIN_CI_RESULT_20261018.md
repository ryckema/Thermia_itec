# V5DCM21 — existing RX-frame-path passive join, verified offline — 2026-10-18

**Status:** V5DCM21 overall **RUNNING / PARTIAL**; this specific nontransmitting host integration substep **COMPLETE / POSITIVE**. Native Connect/DCM application acceptance, controller icon, cloud Online, physical response-slot ownership and semantic writes remain **OPEN / UNKNOWN**.

## Hypothesis and baseline
Hypothesis: a *post-boundary, CRC-correct* frame event from the **existing** V5/portable observer can feed a native DCM diagnostic without a second UART parser, mutable handshake advancement, any fabricated epoch/owner, or TX.
- XTR live known-good remains flashed **V5DCM19 FIX1 RX-only**; **V5DCM20 COMPLETE / POSITIVE** for 18m33s, no physical TX.
- V5DCM21 previous exact-HEAD read-only readiness gate: Actions 39114268008, 22/22 host checks.
- Write Beta V4.1 **EXP386/387 local POSITIVE**, **EXP388 PARTIAL**, other untested claims unchanged.
- Original V5DCM18 Python Core full stateful capture replay remains **RUNNING / PARTIAL**. The accepted G01–G06 residual-risk decisions remain closed.

## Single controlled change family
**Source-only join and test fixture**, not a physical experiment. Added firmware-repo:
- `portable/xtr_v5dcm21_rx_join.hpp` (final amendment `203ca64e8c85311e07f834f62c89f56e3435a83f`);
- `portable/test_xtr_v5dcm21_rx_join.cpp` (`9f051025c9412e6b226a0b331fd637a1e1096323`);
- mandatory integration-compile/test jobs in `.github/workflows/v5dcm21-readiness.yml` (`1c045872c155dd0548d280cbd2be5ab494bcb054`).

The join accepts **either** (a) a completed `AdapterEvent` from the existing `EspHomeRxOnlyBridge` or (b) an already-decoded `Frame` from an existing CRC-validated RX callback. It **does not** run a new UART RX consumer or claim the private deployed callback is already wired. When given an AdapterEvent it rechecks CRC and decodes supported geometry; CRC-valid FC23 is only counted/invalidates the cold observation, and the native challenge contents are neither decoded nor answered.

It maintains only a strict 32-page **historical cold-reference observation** (interleaved runtime ignored, out-of-order settings page breaks sequence), and resets its observed sequence on bus return, native FC23 context change or integrity-fault call. A complete observed sequence never asserts real session epoch, physical owner, exclusive response slot, handshake Accepted or application readiness. Its `readiness()` passes an untrusted shadow and empty IndependentEvidence to the previously tested read-only evaluator; `live_tx_permitted` is false in all paths. No private dynamic challenge/response data or confidential 0x0708 tooling is included.

## Actual execution evidence
GitHub Actions [39115058751](https://github.com/ryckema/Thermia_Connect_Firmware/actions/runs/39115058751), firmware commit `1c045872c155dd0548d280cbd2be5ab494bcb054`:
- actual main-branch checkout and strict `g++ -std=c++17 -O0 -Wall -Wextra -Werror -pedantic` compilation of real portable Core, wire, frame, platform, adapter, ESPHome bridge and passive RX join — **PASS**;
- existing mandatory readiness regression — **22 assertions PASS**;
- new RX adapter integration regression — **43 checks PASS** including a synthetic 32/32 ordered cold reference, unowned/repeated 085F, interleaved runtime page, missing/incorrect page, bus-return, CRC-invalid event, CRC-valid FC23 presence, and absence of TX calls;
- source hard-deny invariant — **PASS**.

Logs print exactly:
```text
PASS V5DCM21 actual HEAD C++ readiness/observer 22 assertions; TX permanently denied
PASS V5DCM21 RX-only joined adapter 43 checks, full cold spine without owner or TX
PASS: source output hard-deny invariants
```
All tested frames are **synthetic unit fixtures**; this CI does not replay authentic October XTR captures or exercise the exact *flashed* V5DCM19 FIX1 ESPHome YAML. Source evidence is not physical output measurement.

## Criteria, abort and recovery
- Positive for strictly bounded offline scope: joined completed-frame interface compiles, retained RX-only bridge output policy stays hard-denied, absence of unearned ownership/session promotion under 65 tests — **MET**.
- Negative test outcomes: **none** in the executed fixture suite.
- Inconclusive for real deployment: **exact V5DCM19 FIX1 callback API and source-version parity**, independent sender/epoch/slot provenance, retained/hot runtime readiness, native firmware request-dependent response, semantic controller acceptance.
- Abort on any unintended TX, unsupported ACK, sensitive response code publication, or production regression; no physical or HA operation was initiated. Recovery not needed; existing installed firmware untouched.

## Next action / handoff
**Do not flash this offline module as a replacement.** Determine the exact *currently deployed* V5DCM19 FIX1 CRC-valid frame callback and separately correlate observed source, bounded bus-return/reset epochs, and native session context without inferring ownership. Join the new `PassiveRxJoin` at that existing callback only after exact source review and preservation of all production entities/bookkeeping. Any future active dynamic-response test needs its own guarded, precise and privately documented experiment. No new live TX authorized by this CI result.
