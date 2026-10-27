# V5DCM73 — Fixed-capacity rolling RAW/V5, wrap-safe RX-only offline result

**ID:** V5DCM73-FIXED-BUFFER-ROLLING-RX-WRAP-SAFE-HOST-01  
**Date:** 2026-10-20  
**Status: COMPLETE / POSITIVE — SOURCE-PINNED OFFLINE ONLY.** **NOT RUN** on XTR/ESP32; no embedded readiness, native TX admission or Online claim.

## Hypothesis, baseline, prior work, controlled change

**Hypothesis:** the two V72 host-identified blockers in the *new V71 rolling RAW/V5 observer* (dynamic STL allocation inside `noexcept` UART callback functions, and rejecting natural uint32 millis() wrap after ~49.71d uptime) can be fixed by one bounded, observer-only offline source replacement without weakening any current RX error veto or clearing past B11D/P5/FIX2 historical faults.

**Last VERIFIED live baseline:** current installed V49 RX_ONLY/HARD_DENY, after user-confirmed manual Thermia controller OFF/ON with 10,351ms callback gap; terminal V49 frozen `RX_SHADOW_RECORDED`, 285 independently CRC/byte-matched frames in 128 batches /30.532s, UART TX0 reported. Current cumulative native FC23 requests=63 unanswered in discontinuous console; strict 03E8/0864/0708 absent in bounded sampled logs. Exact flashed binary, physical owner/electrical wire EOF/response slot and present 0867 controller version unknown. EXP388 still RUNNING / PARTIAL. These device facts were not newly measured or reproduced here.

**Relevant prior history:** V47 COMPLETE/INCONCLUSIVE native one-shot due to 17-byte pre-restart orphan/B11D 250ms timeout, +17 parser resync, no native TX; V48 offline original parser proof; V49 on-device passive cohort; V69 native response never attempted because intentionally hard build-locked; V70 historical-vs-current diagnostic conceptual host-only; V71 40/40 original-source-linked rolling observer; V72 6/6 host memory/uint32 rollover audit and EMBEDDED NO-GO. Earlier EXP255–258/355/386 complete native stage evidence preserved; partial one-response EXP256 yielded COMM ERR and MUST NOT be repeated by default.

**One controlled change:** new NONDEPLOYABLE `v73_fixed_rolling_rx.hpp` replaces only the proposed extra V71 observer's dynamic RAW and expected-frame vectors, nested frame allocations and copied diagnostic string with fixed arrays/descriptors and an independent allocation-free CRC/frame-candidate implementation. A 32-bit unsigned modular elapsed check replaces the signed/order-sensitive `now<last_time` comparison. No modifications to existing V49 YAML, original V5 parser, V49 frozen witness, B11D/P5/FIX2 latches, HA Configuration, bus behavior or GPIO; no live TX/reboot/flash.

## Exact source pins, reproducible artifact

- Original private V49 ZIP SHA256 `62afe39629102a3daa06f09eab3ed159f44437d702fb8d3904c61e62e2a85630`, unchanged 69-member original source and existing single RX UART callback (`witness().ingress(bytes)` BEFORE original `c.parser.feed`, `witness().parsed(v49_frames)` AFTER, periodic `idle`). No second UART reader added.
- Original V71 host ZIP SHA256 `d0e1fd748e32a89912bd692fb8d38f5c2ac38677be70a6a04d29e5f1a2af6ed9`.
- V73 HOST-ONLY package `V5DCM73_FIXED_RX_WRAP_SAFE_OFFLINE.zip` SHA256 `f511c2be0a16e4af6cb84b244dd6785827ac22b77b42f9a38280b159e5ac6b50`. This exact 16,976-byte ZIP is a conversation artifact, not firmware and not published on public GitHub.
- `v73_fixed_rolling_rx.hpp` SHA256 `c12ad6ce9d590cf09a12855c118a948117bc825077783f56d0cc35f9f70c6f24`, test `v73_host_test.cpp` SHA256 `a7b4992bfe9955b72616cb094cfb5efe28edb77b95b6293bed1334643073d39f`, runner `run_v73_offline.py` SHA256 `e7476ff9e460ae268023e7a4b91ddbfb114eb90d55d10ed2379aa72c5e8ba358`.
- Reproduce: `python3 run_v73_offline.py '<V49 original ZIP>' '<V71 original ZIP>'`. Runner SHA-pins both source archives, extracts the unchanged V49 portable `xtr_adapter.cpp/xtr_frame.cpp/xtr_core.cpp/xtr_wire.cpp/xtr_platform.cpp` and literal original in-YAML V5 `StreamParser` into a disposable host wrapper, tests safety invariants, compile-guards and original V71 regression. The original V49 ZIP/YAML, exact production V5 source and private native response algorithms are **not redistributed** in V73 ZIP.

## Actually executed results

- **56/56 PASS** C++17 g++ `-O2 -Wall -Wextra -Werror -pedantic` against original V49 portable C++.
- **56/56 PASS** ASan/UBSan; **56/56 PASS** separate `-fno-exceptions -fno-rtti` host run.
- **4/4 expected compile denials**: private V42 native TX build, V42 hardware-reviewed TX, `ESP_PLATFORM`, `ARDUINO`; deliberately NOT a deployable ESPHome component.
- **40/40 PASS** original unchanged V71 host regression in runner.
- **12,288 exact candidate geometry comparisons** = 256 function bytes ×16 partial-frame sizes ×3 fields, against unmodified `thermia::xtr::candidate_lengths`, plus all 256 slave/function values and CRC16 mutations against unchanged `xtr_wire`.
- **5 exact original production inline V5 StreamParser-host links**: one frame, split frame, two frames same callback, corrupt/incomplete input (hold briefly then revoke >250ms), long FC16-shaped frame. No claim of full ESPHome build.
- No new `operator new` calls measured inside the V73 RX+idle functions for modeled bursts of **128 × 8-byte frames** (1024 RAW bytes) and **128 × 31-byte frames** (3968 RAW bytes). Other pre-existing V49 and original V5 parser paths still allocate; this is *not* zero allocations for the full ESP callback.
- Fixed host x86-64 object `sizeof(FixedRollingRx)=8896` bytes: two 4096-byte flat buffers, 128 bounded frame descriptors and 96-byte first-fault identifier. ESP32 ABI, internal/PSRAM placement, stack and workload unmeasured.
- Normal 32-bit `millis()` wrap accepts a legitimate short forward step around `0xFFFFFF00`; backwards step appears as a huge modulo delta and revokes. Absent new good RX >5s revokes. A gap/clock discontinuity >10s revokes rather than inferring physical time/epoch.
- RX qualification remains **DIAGNOSTIC ONLY** after original V49 recorded frozen witness + demonstrably pre-gap first fault + >=30s/100 **NEW independently matched CRC and exact RAW/V5 frame bytes**. New CRC/resync/byte error, newly incomplete frame >250ms, mismatch, altered first fault, second software gap, counters rollback, DE/TX activity and ambiguous time all fail closed, no auto-rearm. Original historic B11D/P5/FIX2 faults are NEVER cleared and always remain authoritative for existing hardware TX guards.

## Findings by evidence/provenance

**PROVEN OFFLINE SOURCE/HOST:** new independently bounded *additional observer* does not allocate in tested callback/idle operations, maintains fixed storage and CRC parity with V49 portable code, handles uint32 rollover correctly and never offers TX/owner/Online authority; literal original V49 StreamParser outputs also agree on tested callback shapes. A partial frame from a controller power cut is a **plausible** historic phenomenon, not electrical switch timing proof. Its historical record can be retained while a separate RX-ONLY diagnostic reports new clean reception.

**STRONGLY SUPPORTED:** allocation-free shadow with bounded frames is a more defensible embedded candidate than V71 and its timer bug is removed without relaxing post-anchor error checks.

**OPEN/NOT VERIFIED:** **the original V49 / inline V5 parser / B11D still allocate**, so all ESPHome processing is not proven allocation-free; ESP32-S3 heap/PSRAM/CPU, 9600-baud callback scheduling with Wi-Fi/HA, physical response owner/slot/EOF, old-first-fault pre-gap timestamp proof, actual controller version 0867, genuine DCM C2 and Online service are unknown. No embedded compile/flash/hardware results, and **the V73 header intentionally #error rejects embedded builds**. The XTR controller has NOT accepted a V73 native reply (none exists).

## Criteria, safety, abort and next

**OFFLINE POSITIVE:** exact source pins, fixed storage, zero new allocations in tested V73 RX member path, correct 32-bit wrap, CRC/RAW/V5 parity, all TX/first-fault invariants and safety mutations pass. **NEGATIVE:** any new CRC or present RX fault admitted, original fault overwritten, unauthorized TX, memory overrun, unsound normal clock wrap, source checksum conflict. **INCONCLUSIVE for actual hardware** until future user-run RX-only observations.

**No physical target/slave/register payload, TX timing, current register value or recovery:** this experiment is HOST-ONLY; abort/rollback is discard prototype on failed source/checks. Current known-good live V49 RX_ONLY/HARD_DENY remains untouched.

**NEXT:** separately scope a V74 offline *whole-callback* memory/stack/runtime feasibility study (including the original still-allocating V5 parser, V49 witness, B11C/B11D, Wi-Fi and HA), and only then prepare a different user-initiated RX-only ESPHome build if supported. Do NOT simply remove `#error` guards, flip V42 TX switches, clear original first fault or mistake recovered RX for native Connect session acceptance.
