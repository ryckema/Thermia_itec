# V5DCM21 offline compilation and passive seam — 2026-10-18
Status: **RUNNING / PARTIAL** overall. Positive narrow smoke compilation, not full HEAD integration.

## Baseline and controlled change
Production baseline unchanged: V5DCM19 FIX1 RX-only; V5DCM20 local 18m33s stability confirmed. Preserve G01–G06 accepted risks. Read GitHub firmware source portable/xtr_core.hpp/.cpp, xtr_adapter.hpp/.cpp and xtr_esphome_bridge.hpp/.cpp. Earlier readiness evaluator and test existed at firmware commit 8dc5918d63967dc53f500fb637f92d7cda1902b2. Controlled change adds *only* passive observer seam portable/xtr_v5dcm21_observer.hpp at 947200841159e0caced6d5930aa4f6386778554a. No changes to Core's mutating decisions, adapter, native response algorithm, ESPHome YAML or platform TX.

## What was actually executed
Local container could not clone GitHub (DNS unavailable). Manually reconstructed matching relevant current xtr_core.hpp declarations, copied the evaluator logic from the earlier retrieved GitHub content and recreated the previously committed regression-test assertions into temporary local C++ files; compiled with:
`g++ -std=c++17 -Wall -Wextra -Werror -pedantic test.cpp -o test`
Then executed: `PASS offline assertions` (exit 0).
**Scope limitation:** this is an actual compiler/test execution against locally recreated header/fixture content, NOT a byte-verified GitHub checkout and NOT a compile of new GitHub observer.hpp or original test_xtr_v5dcm21_readiness.cpp. Claiming full GitHub HEAD regression PASS would be incorrect. No physical XTR experiments.

## Source-reviewed behavior
- Core::fc16_decision has firmware-like internal ResponseSent→Accepted promotion on an eligible FC16 before owner qualification. This state is not physical TX authority.
- recompute_write_ready does not independently attest to profile/required-package readiness or exclusive response-slot ownership.
- Existing EspHomeRxOnlyBridge is constructed with output_enabled=false and TxDisabledHalfDuplexIo, kLiveTxEnabled=false.
- New observer accepts a const Core&, ApplicationPath and *externally proven* IndependentEvidence, invokes only the pure readiness evaluator and has no response API. The header includes bridge static assertion. Not wired into current ESPHome production.
- Readiness evaluator's cold 32/32 predicate is explicitly one cold reference; no retained/hot positive path is currently implemented. Application-data flags are *descriptive candidate axes*, not a claim that local XTR is application ready.

## Criteria and limits
Positive, scoped: prior evaluator compiles/executes on recreated test fixture; source files authored and acknowledged by GitHub, observer design never produces TX.
Open/partial: full GitHub HEAD checkout/build/test, compile observer against actual current headers, valid retained/hot evidence, real native owner/epoch/slot, joined runtime parser, firmware-derived challenge responder and local acceptance.
Negative: no failure identified in scoped smoke test. Inconclusive: full-source integration / physical behavior.
Abort: unexpected TX/side-effect or private disclosure; none performed. Rollback: omit newly added offline headers; deployed FIX1 unchanged. No active payload, address write, timing or retry authorized.

## Next action
Run full HEAD regression (including new observer include), test external evidence revocation and epoch resets, join passive observer strictly behind existing parser; keep all native output hard-denied. Do not repeat V5DCM20 RX-only endurance test to satisfy offline integration scope.
