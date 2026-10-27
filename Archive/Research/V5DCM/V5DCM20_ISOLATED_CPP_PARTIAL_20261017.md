# V5DCM20 — partial offline C++ contract test (2026-10-17)

Status: RUNNING / PARTIAL. Standalone non-transmitting C++17 contract compiled and passed 24/24 synthetic assertions. Original portable Core refactor was NOT applied: a safety control blocked the source modification. No integrated Core build/test, ESPHome compile, flash or physical TX occurred.

Hypothesis: pure observation followed by independently qualified authorization and explicit commit prevents a denied event from changing the handshake state. Baseline: V5DCM18 code audit, V5DCM19 15/15 isolated Python assertions, deployed V5DCM2 FIX1 RX-only/HARD_DENY. Controlled change: isolated host-only test fixture, with no serial, native responder, authentication implementation or command mailbox.

Observed: all 24 synthetic checks passed with g++ C++17, strict warnings; invalid geometry, absent source/epoch/session flags and other denied observations do not promote an isolated state. Artificial test authority is NOT real physical bus/source/slot proof.

Positive: standalone 24/24 — MET. Integration positive: original portable Core changed and regressions passing — NOT MET. Negative: no standalone test failure. Abort: original source mutation blocked by safety review; do not bypass. Recovery: original repository implementation and live RX-only production remain unchanged.

Next: finish integration only through an approved review path; do not mark experiment complete until source changes and original-call-site tests are actually verified.
