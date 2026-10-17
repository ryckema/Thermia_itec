# V5DCM18 — extended user-ZIP portable C++ stateful regression (2026-10-17)

**Experiment:** V5DCM18 original roadmap offline replay. **Status: RUNNING / PARTIAL for the complete experiment**, COMPLETE / POSITIVE only for this bounded C++ test batch.

**Baseline:** User-supplied `V5DCM2_CM930_CHALLENGE_INTEGRATION_RX_ONLY_PREPARED_20261017(2).zip` portable source, previous 11/11 host-C++ checks; historical CRC 25,031 frames and 49/49 passive structural fault observations. **Controlled change:** test-only six new C++17 assertions, no change to source Core, production YAML, hardware or UART.

**Actually compiled and executed:** `g++ -std=c++17 -Wall -Wextra -pedantic`, portable Core from ZIP, `test_extended.cpp`. **17 PASS / 0 FAIL**. Six additional checks: controller-epoch change rejects stale decision; separate Core instance rejects another instance's decision; changed frame payload after decision is rejected; deliberately qualified runtime can report ready; `revoke_authority` removes readiness; recovery transition removes runtime readiness. Earlier 11 positive/negative tests still pass.

**Critical limit:** ZIP source has provenance/ticket API absent from current `Thermia_Connect_Firmware/main` portable Core. Therefore these 17 results are **NOT** validation of GitHub HEAD. Existing original Python reference Core CI results and end-to-end merged corpus/fault replay are NOT verified. Do not mark roadmap experiment COMPLETE merely for synthetic host-C++ success.

**Positive criteria for this subtest:** all 17 compile/run successful, no unsafe state promotion in named checks. **Negative:** zero observed in these checks. **Abort:** any live TX, production changes, unexpected model-authority elevation. **Recovery:** none, no deployment. **Next:** execute original reference-Core tests against all seven existing capture fixtures and compare error semantics with original CM930 firmware; reconcile ZIP/Core version difference before V5DCM19.
