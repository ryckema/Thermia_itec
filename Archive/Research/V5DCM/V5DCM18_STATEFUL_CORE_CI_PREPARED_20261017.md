# V5DCM18 — original reference-Core stateful fault-replay follow-up (2026-10-17)

**Status: RUNNING / PARTIAL; new original-Core CI execution result not independently retrieved.** This is a continuation of the original roadmap V5DCM18, not a new experiment or a claim of successful end-to-end replay.

**Hypothesis:** a complete fault replay must distinguish the original CM930 firmware's internal handshake acceptance event from host-side TX/semantic authorization and from full application readiness.

**Baseline:** original V5DCM18 offline capture replay 25,031/25,031 CRC-correct frames, 164 challenge-shaped, 7 reply-paired, one strict 32-page sequence; V5DCM17 readiness gates, V5DCM2 FIX1 production RX-only/HARD_DENY. Earlier 49/49 structural checks are not actual reference-Core stateful tests.

**Controlled offline implementation:** added source-level adverse-scenario script [test_v5dcm18_roadmap_faults.py](https://github.com/ryckema/Thermia_Connect_Firmware/blob/main/tools/test_v5dcm18_roadmap_faults.py) to the original firmware-research repository, calling original `tools/xtr_dcm_reference_core.py` directly. Wired it to the existing [reference-core-unit GitHub Actions workflow](https://github.com/ryckema/Thermia_Connect_Firmware/actions/workflows/reference-core-unit.yml). Scenarios include denied first FC16 page, handshake promotion despite denied ownership, complete 32-page bootstrap, missing 03FC, repeated ResponseSent notice, interruption/fresh reset, no semantically ready status from bootstrap tail and ineligible approval.

**Observed direct original source (not test result):** `Core.fc16()` sets `Handshake.ACCEPTED` while `RESPONSE_SENT` on most FC16 shapes, before returning `Decision`; the request may subsequently be denied by bootstrap owner. This behavior closely parallels original CM930 `_on_function16` firmware-derived acceptance, which uses a broader criterion than ownership. It therefore should NOT be called an independently proven firmware error. The emulator's external TX/security decision must not treat internal acceptance as ownership or physical slot authorization.

**Pending verification:** GitHub CI was configured, but current run/job logs were unavailable here. No assertion that the new test executed, passed or failed. CI source changes are committed but no ESPHome/YAML/physical changes were made.

**Positive:** stateful replay against unchanged original Core, reviewed output and expected transitions, then an end-to-end offline scenario matrix with actual source provenance. **Negative:** any scenario erroneously upgrades host-side TX or full Connect readiness, or breaks normal bootstrap. **Abort:** private authentication material, bus TX, source-level unintended hardware enable. **Recovery:** disable/remove added CI test; live production unchanged.

**Next:** retrieve CI result and report exact passed/failed assertions. Then resolve the original firmware versus safer host-gate separation while preserving genuine handshake semantics. Do not promote V5DCM18 to COMPLETE before review.
