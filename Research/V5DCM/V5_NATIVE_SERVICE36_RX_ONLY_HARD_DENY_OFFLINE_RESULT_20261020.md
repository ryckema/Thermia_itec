# V5 Native Service-36 — RX-only compiler denial and completed-ADU routing

**Date:** 2026-10-20. Private user source, offline only. Two separately controlled experiments: **V5-NATIVE-SERVICE-36A-RX-ONLY-BUILD-GATE-OFFLINE-01 — COMPLETE / POSITIVE OFFLINE** and **V5-NATIVE-SERVICE-36B-COMPLETED-ADU-RX-FANOUT-OFFLINE-01 — COMPLETE / POSITIVE OFFLINE**. Actual physical XTR validation for both: **PREPARED / NOT RUN**.

## User-verified baseline, source and provenance
- Last user-confirmed running device is V83-family **RX_ONLY/HARD_DENY**, with V49 fallback. The FAS1 supplement has no independent user-confirmed flash here. **EXP388 RUNNING / PARTIAL**, early **B11D** independent receive-alignment fault unresolved. Controller owner/electrical slot/current original Connect application acceptance unknown.
- Exact private original Service-35 ZIP SHA256 `c89287f3a565a0718beb5dd2244a68791d93c62779a48683249daba3e40cb5f5`. Authentic recovered original V83 supervisor remains byte-identical; original FAS1/V45 safety files unchanged. New Service-36 private ZIP SHA256 `39f3901dc3fc33a4874721465be6c9ca61fedd842e1976b6c764b8e5e37be7bd`, 209 CRC-clean entries, **not for public redistribution**. Staged YAML SHA256 `55c6b1aaa8e17ea8d4ccc51d59fb7f6bc6673554cb5a2cacc841fd80574cc6ca`.
- The earlier V80 and Service30/33 had **already documented** V43/V44B callback suppression on coalesced frames and trailing partial data. The S36 finding is an **offline implementation/test of that known RX-only integration issue**, not a newly discovered physical fault cause.

## Experiment 36A — one source change
**Hypothesis:** Original V83 safety header denied older V42 hardware TX compile flags but not newer Service23 scoped TX flags, so the S35 source lacked a universal hard stop for the intended RX-only build.

**Change:** Add one strictly receive-only build gate, included both in the staged ESPHome header list and at the top of its existing private native service runtime. It denies compilation if **any** one of four known legacy/newer TX-owner compile flags is defined. No additional UART or DE/GPIO calls, profile selection, controller session binding or physical output. Future active TX would need a separately reviewed build target; it cannot be silently enabled by these flags in this RX-only target.

**Positive:** default RX-only host header syntax passes; **15/15 nonempty flag combinations** produce the expected compiler rejection. **Negative:** even a single forbidden mode compiles, or original source safety changes. **Inconclusive:** embedded ESPHome compilation NOT RUN. **Abort/rollback:** reject/discard private source candidate on any failure; installed V83 unchanged.

## Experiment 36B — one RX-only source change after 36A
**Hypothesis:** The pre-existing V43/V44B native observation hook could skip already completed CRC-valid ADUs because it required the parser to have **no trailing incomplete frame**. Main V5 frame processing was already complete-ADU-based.

**Change:** Use a tiny, pure RX-only completed-ADU dispatch helper to present **each** completed frame from the original single V5 parser to the existing **unbound** V43 and V44B observers. Preserve their original RX/B11D/P5/DE health checks, main V5/HA processing, independent B11D raw scanner/fault latch and passive Service34 version witness. No second reader or response privilege. The 36A compiler guard prevents this altered routing from being built as a TX-enabled actor in this target.

**Positive:** an earlier source-extracted **original V5 parser** with synthetic generic non-native Modbus read frames passes **46/46 assertions in each of three C++17 modes** (strict, no-exceptions/no-RTTI, ASan+UBSan). Cases: one complete frame, two coalesced, completed frame + trailing partial, two completed + trailing partial, later split completion, and CRC-invalid frame not forwarded. **Negative:** valid finished ADU omitted/duplicated, unfinished ADU delivered, RX safety removed or physical TX permitted. **Inconclusive:** actual ESP32 callback batching frequency, B11D real first fault and any controller acceptance. **Abort/rollback:** discard private source if parser, CRC, safety or source-integrity tests fail; no device change.

## Combined validation actually performed
- Existing full Service35 + S36 test runner: **35/35 host executable invocations PASS**. This includes inherited synthetic FakeIo test executables; it does **not** mean physical TX was tested.
- Exact source/YAML/compiler verifier: **40/40 PASS**, including the 15 compiler-denial combinations.
- Staged YAML retains **24/24 original top-level blocks**, all **198** existing HA ID/name identities (197 original + one Service34 diagnostic), unchanged physical UART settings, substitutions, original globals/HA controls/B11D and watchdog blocks. All referenced project-local source headers present.
- S35-to-S36 YAML change is reconstructed and checked byte-for-byte. Existing private native runtime header is identical to S35 after removing the single added compiler-guard include; authentic recovered V83/FAS1/V45 safety headers unchanged.
- **NOT RUN:** full ESPHome/PlatformIO compile or link, firmware flashing, actual UART/RS485 TX, device reboot, new local XTR measurement, native Thermia Connect C2/Online or semantic writes.

## Conclusions, remaining unknowns, next
**PROVEN OFFLINE SOURCE/HOST:** the intended RX-only target now compiler-denies all known V42/S23 TX build flags, and complete ADU delivery to the retained unbound native observation hooks no longer depends on an empty trailing parser buffer. These changes do **not** independently prove runtime correct behavior on the ESP32.

**STRONG CONCLUSION:** this is a safety-hardened source candidate, **not** an automatic native Online/Connect session or working write gateway. **HYPOTHESIS:** the new RX dispatch might prevent a future callback-level omission if coalesced/partial callbacks occur on-device; their actual occurrence and role in B11D are unknown.

**OPEN:** early real B11D first-fault cause, current XTR session/version/physical slot/owner, callback behavior on device, exact original Connect profile/session acceptance and full embedded compile. **NEXT:** validate the RX-only candidate with an offline ESPHome/PlatformIO compile using a reproducible toolchain (no routine request to user for compiler output), then independently review whether a **user-initiated receive-only** observation is warranted. No controller restart or bus TX is part of S36. Do not clear existing sticky faults.