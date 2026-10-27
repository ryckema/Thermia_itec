# V5DCM72 — V71 rolling RAW/V5 ESP32 integration-readiness, memory, latency and clock-wrap audit

**Experiment ID:** V5DCM72-V71-EMBEDDED-INTEGRATION-READINESS-OFFLINE-01  
**Date:** 2026-10-20  
**Status: COMPLETE / POSITIVE for exact-source OFFLINE AUDIT; EMBEDDED INTEGRATION = NOT READY / NO-GO.** No change to installed ESPHome firmware, no new live XTR proof, no TX, no reboot, no motor/DHW/register action.

## Controlled question, verified baseline and existing results

**Hypothesis:** V71's unmodified host-tested independent rolling RAW/V5 witness has a safe and practical implementation path into the existing ESP32-S3 V49 receive callback, or the source/host audit reveals concrete integration blockers before a live RX-only experiment is prepared.

**Last verified on-device baseline:** V49 RX_ONLY/HARD_DENY, user-attested manual controller OFF/ON with a 10,351 ms RX callback gap; 285 clean RAW/V5 matched frames over 30.532 s in frozen historical `RX_SHADOW_RECORDED`; original history and production HA unchanged, native UART TX0 by device diagnostics. Unanswered native FC23 cumulative 63 across interrupted console; sampled strict current `0x03E8`, `0x0864`, `0x0708` absent. Exact deployed binary SHA, controller version, response owner/slot/electrical EOF remain UNKNOWN. Existing EXP388 stays RUNNING / PARTIAL.

**Relevant completed work:** V47 (17-byte pre-power-cycle residue, B11D timeout, +17 resync and safe deny; actual TX0); V48 original parser replay; V49 healthy frozen 30 s RX cohort; V69 first native reply still unexercised in V49; V70 historical-vs-current diagnostic conceptual model 40/40; V71 original portable source + rolling observer 40/40, with future V5 completion inputs synthesized. No existing experiment is rerun on the physical pump.

**ONE controlled change:** source/host **integration readiness audit** only, retaining V49 and original V71 untouched. V72 measures existing unmodified V71 allocations and CPU on x86-64 with synthetic CRC-valid inputs, runs the original V71 source tests again, checks 32-bit uptime rollover, and reviews original V49 ESP-IDF/PSRAM/UART callback geometry and compiled source dependencies. No rewritten native response, NO extra UART reader, no new ESPHome entities/YAML or TX.

## Source pins / exact hardware-configuration facts (source only)

- Original user V49 ZIP SHA256 `62afe39629102a3daa06f09eab3ed159f44437d702fb8d3904c61e62e2a85630`; 69 entries, one 4,728-line YAML; native V49 main YAML previously SHA256 `fe02f0b0a503f8f896442165e57397afeacd22cf951efa46ea87885f98d71c22`.
- Original V71 host package SHA256 `d0e1fd748e32a89912bd692fb8d38f5c2ac38677be70a6a04d29e5f1a2af6ed9`. Unchanged `v71_rolling_raw_v5.hpp` SHA256 `c99c3810a963565b11d9a718fce4474beb3fd5e9ce40d68f898b33cc7593f117`.
- Exact V49 source declares **ESP32-S3, ESP-IDF, octal PSRAM 80 MHz**, native UART **9600 baud/8E1**, `rx_buffer_size: 4096`, UART debugger **RX only** with `after.timeout: 5ms`. This is **configuration**, not current hardware CPU speed, heap size or proof PSRAM is used by `std::vector`.
- Source callback already orders `v5dcm49::witness().ingress(bytes,...)` before `c.parser.feed(bytes.data(),bytes.size())`, then `v5dcm49::witness().parsed(v49_frames,...)` after, plus existing periodic `witness().idle(...)`. Reusing this callback is architecturally feasible, but V71 remains deliberately `#error`-blocked for `ESP_PLATFORM` and `ARDUINO`.
- V71 source and original portable `candidate_lengths` use `std::vector` and other allocating STL containers repeatedly, including `raw_.insert`, `v5_.push_back`, per-iteration copied `tail`, candidate `std::set`/vector, CRC-frame body copies, and temporary independently decoded frames, all from functions declared `noexcept`.

## Executed tests and measurements (x86-64 HOST ONLY)

Reproduction: `python3 run_v72_offline.py '<V49.zip>' '<V71.zip>' --sanitize`. SHA pins refuse changed archives. Host compiler **g++ 14.2.0, C++17 -O2 -Wall -Wextra -Werror -pedantic**, linked against original V49 portable `xtr_adapter.cpp`, `xtr_frame.cpp`, `xtr_core.cpp`, `xtr_wire.cpp`, `xtr_platform.cpp`, **not an ESPHome/ESP-IDF compile**.

**Original V71 regression rerun:** `40/40` host assertions PASS; `40/40` ASan/UBSan PASS; the four prohibited compile configurations (`V5DCM42_PRIVATE_TX_BUILD`, `V5DCM42_HARDWARE_PORT_REVIEWED`, `ESP_PLATFORM`, `ARDUINO`) continue to FAIL COMPILE correctly.

**New V72 scoped probes: 6/6 PASS**:
1. Source-linked C++ object/layout metrics: `sizeof(RollingRawV5)=152` bytes on this x86-64 C++ ABI; `sizeof(std::vector<uint8_t>)=24`, `sizeof(std::string)=32`. **Object size is not dynamic heap need or ESP32 ABI layout.**
2. 2,000 independently matched synthetic eight-byte CRC-valid ADUs at 100ms *modeled timestamps* successfully remain `QualifiedRxOnly` and `TX=false`; modeled timestamps are not physical UART timing or actual sleep.
3. 200 trials with 128 CRC-valid 8-byte frames in one 1,024-byte RAW callback: mean **236.61µs**, max **497.24µs** on x86-64; approximately **301,000 dynamic allocations over 200 trials = 1,505 per trial**; allocator-tracked peak concurrently live requested payloads **15,892 bytes** for this trial class.
4. 200 trials of 128 synthetic 31-byte CRC-valid FC16-shaped ADUs per callback (3,968 RAW bytes, within 4,096 limit): mean **113.17µs**, max **209.30µs** on x86-64; approximately **311,000 dynamic allocations /200 = 1,555 per trial**; peak live requested payload bytes across tests **30,693 bytes**. This 3,968-byte burst would take multiple seconds on a 9,600-baud line; it is an artificial buffer stressor, **not a 5ms real RX callback prediction**.
5. Force a correctly increasing modulo-32-bit clock from `0xFFFFFF00` to `0x00000010`: original V71 compares `now < last_time_`, incorrectly classifies normal **millis() wrap (~49.71 days)** as `ClockRollback` and irreversibly REVOKES RX diagnosis. It stays TX-fail-closed, but long-lived diagnostic coverage ends unexpectedly.
6. Force a change to the baseline CRC error counter: V71 correctly REVOKES `ChangedCounters`, not an accidental acceptance.

Allocation telemetry comes from a host-only overridden `operator new/delete` that tracks requested bytes, **not full peak RSS**, allocator metadata, fragmentation, original ESPHome memory or PSRAM usage. The standalone fixture/test overhead contributes. Timing is native host `steady_clock` and is **NOT extrapolatable** to ESP32. Repeat runs vary. No real-world performance guarantee is implied.

## Positive findings versus blockers

**PROVEN SOURCE/TEST:** original V49 has a single suitable callback seam; V71 host functional suite retains RX-only fail-closed behavior; 6/6 additional measured tests execute deterministically; original V49/ V71 files remain unchanged.

**SOURCE-LEVEL BLOCKER A — heap failure mode:** the V71 callback/idle hot path performs numerous potentially throwing heap allocations inside `noexcept` methods. Under allocation failure, C++ requires termination rather than a clean catch/revoke. Even with optional PSRAM, the current architecture does **NOT** give an acceptable deterministic bounded-memory embedded safety or availability guarantee. This is an engineering integration NO-GO; high allocation churn might perturb timing and fragment the heap over long uptime. None of the host benchmarks quantifies that embedded risk.

**SOURCE-LEVEL BLOCKER B — uint32 clock rollover:** `if(now<last_time_)` incorrectly treats the natural 49.71-day `millis()` wrap as rollback. At minimum this requires wrap-safe bounded elapsed-time arithmetic and boundary tests without allowing actual backward time to become false-positive authorization.

**ADDITIONAL SOURCE/TEST BOUNDARY:** V71 accepted future V5 complete-frame vectors as fixture inputs; it did **NOT** link the complete actual inline production V5 parser in the receiver callback, nor demonstrate CPU/heap/stack budgets while Wi-Fi, Home Assistant, full B11C/B11D/P5, PSRAM and all other V49 observers are active. Continuous independent RAW/V5 is NOT running on the user's XTR. Host source says nothing about electrical wire-end/owner/native TX slot or original Connect cloud/application state.

**SAFE interpretation of user's partial-frame concern:** an RTU frame interrupted by a controller power cycle is plausible (V47 +17 residue); historical first-fault evidence should stay immutable, while a **separate RX-only** observer may one day report current good frames. V72 does not normalize any NEW incomplete frame after qualification and does not change the original sticky B11D/FIX2.

## Acceptance criteria, abort and recovery

**Offline POSITIVE:** independently identify source-backed integration seam and real host allocation/clock behavior; show regression of existing guards; record a bounded NO-GO decision if the unmodified V71 prototype is unsafe for deployment. All met.

**Embedded-ready POSITIVE was NOT achieved:** it would require deterministic preallocated/fixed-buffer hot paths, corrected timer rollover handling, exact original parser-linked replay, controlled resources and a **separate** RX-only ESPHome build and eventually user-supplied performance readings.

**NEGATIVE (would invalidate research):** source hash mismatch, reproducer regression, a change that authorizes native TX, or a contradiction between source and host behavior. **INCONCLUSIVE for actual ESP32 CPU/PSRAM use**, because no ESP32 build/measurement was performed.

**Abort/rollback:** offline only: stop at any source/hash/guard/test mismatch; no physical action and thus no rollback. The original V49 remains last user-verified RX_ONLY/HARD_DENY; no device experiment was started.

## NEXT ACTION: V5DCM73 (PREPARATION NOT RUN)

A separate **offline host engineering iteration** should replace the allocation-heavy V71 hot path with a fixed-capacity flat byte buffer and bounded frame descriptors, avoid throw/terminate inside `noexcept`, fix uptime elapsed math with conservative ambiguity handling, preserve first-fault history and all absolute TX-locked guardrails, then test existing 40 regression cases plus burst/partial/overflow/clock-wrap boundary cases. This is **not** an authorization for source publishing protected native 0x0F responses or on-device TX. Only if that offline source result passes and an ESPHome source integration is validated should a dedicated **RX-only** test build be separately prepared for user flashing.

**Package (conversation-only, no private original sources):** `V5DCM72_ESP32_INTEGRATION_READINESS_OFFLINE.zip`, SHA256 `ea0abfe4401350cb86637673964b04d282fdb417ae121b389ce735e966c19c49`, containing host C++ probe SHA256 `a7c43520ce9a50595d4228acded4398b43e1cda0c840176210df56119f88a94e`, reproducible strict runner SHA256 `7a5d17d9ba0f91ec727e9522fdbf112c9be9474c78bed6c801b3d31ca5d4e220`, README, source manifest and test output. ZIP is NOT firmware and should not be flashed.
