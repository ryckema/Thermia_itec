# V5DCM18 — direct original Core test assertion correction (2026-10-17)

**Experiment:** V5DCM18 original-roadmap end-to-end replay / adverse cases. **Status:** RUNNING / PARTIAL — verification of executed original reference-Core test results remains open.

**Baseline:** earlier capture-replay result (25,031 CRC valid / 164 FC23 candidate challenges / 7 temporal pairs), V5DCM17 11 firmware readiness gates; original `tools/xtr_dcm_reference_core.py`, `tools/test_v5dcm18_roadmap_faults.py`, existing GitHub Actions reference-core-unit workflow. Live V5DCM2 FIX1 RX-only/HARD_DENY.

**Controlled change:** repair an incorrectly strict synthetic assertion. The earlier test treated any denied owner decision with an internal handshake transition to ACCEPTED as a firmware inconsistency. Direct original CM930 `_on_function16` source-derived rules explicitly permit internal acceptance for a later qualifying FC16, even when the emulator's ACK owner remains unqualified. Updated the test to assert that the internal acceptance **does not** grant owner/TX by itself. Added `sys.exit(1)` when any check fails, so CI cannot falsely pass while printing failed assertions.

**Changes:** firmware repo [test_v5dcm18_roadmap_faults.py](https://github.com/ryckema/Thermia_Connect_Firmware/blob/main/tools/test_v5dcm18_roadmap_faults.py), commit `1cec88606379d9aedb505017fcb49b8ba63fb13f`; existing [reference-core-unit workflow](https://github.com/ryckema/Thermia_Connect_Firmware/actions/workflows/reference-core-unit.yml) references it.

**Observed / verified:** source diff was successfully written. The original reference core code sets H2 during `Core.fc16` on suitable post-response FC16 frame *before* ownership decisions, matching the original firmware-derived acceptance criterion. This is not evidence of physical response ownership. The test suite has 13 named checks, including a valid 32-page bootstrap, missing-page negative, repeated response notice, controller reset and a deliberately denied first page.

**UNKNOWN:** no actual GitHub Actions job result or host Python test execution was retrievable in this session. Do not state 13/13 PASS or COMPLETE. This script does not replay the seven captures itself; historical capture replay is separately covered by the existing `test_xtr_dcm_reference_core.py --fixture-root ...` and previously reported partial replay.

**Next:** run/check the CI workflow, capture exact per-case results and existing reference-Core corpus tests. If a failure, classify expectation mismatch versus genuine emulator authorization defect. Only after stateful original-Core replay and failure-case matrix are verified should original-roadmap V5DCM18 be COMPLETE and V5DCM19 RX-only integration begin.

**Positive:** a complete original Core test run and captured adversarial outcomes, no unauthorized action. **Negative:** assertions fail or hidden owner/TX readiness elevation. **Abort:** unbounded bus output, private approval code disclosure, production changes. **Recovery:** revert only test assertion addition; production unchanged. No new TX, YAML, or hardware.
