# V5DCM71 — Continuously rolling RAW/V5 independent read-only witness in existing UART callback

**Experiment ID:** V5DCM71-SINGLE-CALLBACK-ROLLING-RAW-V5-RX-ONLY-HOST-01  
**Date:** 2026-10-20  
**Status: COMPLETE / POSITIVE (40/40 strict original-source-linked C++17 HOST TESTS, 40/40 ASan/UBSan, 4/4 compile-denial tests).** **NOT RUN** on XTR hardware; controller epoch, physical owner, electric wire EOF/slot and OEM Connect/Online remain OPEN / UNKNOWN.

## Hypothesis, known-good baseline, previous outcomes, one controlled change

**Hypothesis:** after the original V49 `RX_SHADOW_RECORDED` frozen *historical* CRC/byte-agreement witness, a separate observer attached to the SAME existing `uart.debug.lambda` callback can continually independently reframe future RAW UART bytes, compare complete CRC-valid ADUs byte-for-byte to *existing* V5 output, preserve original B11D/P5/FIX2 immutable first-fault history, and qualify **RX DIAGNOSTICS ONLY** after a new clean period. An old interrupted frame near a power transition should not automatically imply persistent *current* UART corruption; a NEW post-anchor incomplete frame must still fail closed.

**Last user-verified XTR baseline (UNCHANGED):** V49 RX_ONLY/HARD_DENY, manual controller OFF/ON acknowledged; software callback gap 10,351 ms; V49 recorded 285 matched CRC frames /128 batches/30.532 s; no new B11C/B11D parser errors in that sample, native UART TX0. Native FC23 63 cumulative unanswered, strict 03E8/0864/0708 absent in bounded sampled log, current owner/epoch/physical EOF/slot and flashed binary hash unknown. Original older V47 cold-return one-shot had 17-byte pre-gap partial + 250ms B11D timeout +17 parser resync and FIX2 revoked, **0 actual output**; this is plausible power-off truncation, not proven electrical causation. Historical EXP388 remains RUNNING / PARTIAL.

**Relevant evidence (do not repeat):** V45/FIX2 healthy passive before new fault, V47 inconclusive one-shot no TX, V48 exact 17-byte partial-parser recovery reproduced host-only, V49 independent 30s/50-frame post-gap success, V66 V49 single-parser/ledger source, V69 build lock, V70 40/40 conceptual host model without live independent counterpart, and completed EXP255/256/257/258/355/386 native session experiments. Prior incomplete responder COMM ERR is preserved; no native responder built here.

**ONE controlled source-only change:** create and test `v71_rolling_raw_v5.hpp` as **non-deployable** host research observer. It receives raw bytes **before** V5 `parser.feed` and completed frame bytes **after** it from the existing ONE callback, plus an idle tick, without opening UART or touching the original parser/latches. The unchanged V49 ZIP is SHA256 `62afe39629102a3daa06f09eab3ed159f44437d702fb8d3904c61e62e2a85630`, same exact original source used in V66–70.

## Exact V49 seam source check

A checksum-pinned automatic host runner extracts exact original V49 headers and `components/thermia_portable_bridge/` translation units into a temporary directory. Source search confirms the **existing** single UART callback already invokes:
1. original V49 `witness().ingress(bytes,...)` from copied callback bytes BEFORE original `c.parser.feed(bytes.data(),bytes.size())`;
2. original V49 `witness().parsed(v49_frames,...)` AFTER parser has emitted completed frames and CRC counters updated;
3. `v5dcm49::witness().idle(...)` from the existing periodic tick.

No new hardware channel, UART RX consumer or parser subscription is necessary; **this is source feasibility, not integration**. Original V49 `Recorded` freezes, B11D original processing stops on sticky fault, and FIX2's revoked state remains sticky. Therefore **the new rolling comparator is NOT running on the current XTR firmware**. The host test synthesizes callback copies and expected original V5 frame vectors but links unmodified original portable `known_rtu_slave`, `candidate_lengths`, `wire::valid_crc` and CRC-aware frame functions. It does NOT directly run the production inline V5 StreamParser or measure physical bus EOF.

## Model acceptance, abort and provenance constraints

Entry requires original V49 `Recorded` from >=5 s software gap and >=30s/50 matched frames, no expected parser pending, source old-fault-preserved flag, absence of asserted epoch/TX, explicitly scoped nonzero software generation/gap count, plus nonoutput/DE-low runtime input. If B11D sticky is present, evidence that the FIRST fault happened BEFORE the gap must be independently supplied; this host model does NOT derive a physical controller epoch from callback silence.

For the new independent RX period, source-bound thresholds: >=100 NEW matching CRC-valid ADUs, >=30,000 ms and fresh input age <=3,000 ms before returning `QualifiedRxOnly`. Thresholds are conservative diagnostics, NOT response-slot deadlines. The raw fragment hold is bounded at 4,096 bytes and 128 expected frames and a 250ms incomplete-fragment timeout (software), with 25ms quiet before independent scan.

**Immediate irrevocable RX diagnostic revocation** on a new CRC/RAW/V5 byte mismatch, unknown/invalid RTU geometry, new resync/drop/unknown or B11C disagreement, first-fault history altered or cleared, unexpected TX/DE, second software gap/generation change, counter rollback, clock regression, buffer overflow or new fragment exceeding 250ms. After 3–5s no traffic the current RX qualifier becomes false; >5s causes irrevocable diagnostic revoke. No automatic rearm/second scope.

**Safety architecture:** `native_tx_authorized()=false`, `controller_owner_proven=false`, `controller_epoch_proven=false`, `original_online_proven=false`. The V71 host header explicitly rejects ESP_PLATFORM/ARDUINO and either original V42 native TX macro at compile-time. It has NO UART/GPIO/DE output API, secure native FC23 response, 0708 mailbox or FC16 ACK implementation. Original sticky B11D/P5/FIX2 and HA red/brown logs untouched.

**User's interruption/context:** An incomplete frame coincident with controller restart is PLAUSIBLE/EXPECTED as a possible consequence of power removal during an ADU; not intrinsically an ongoing fault. The timing of V47's 17-byte residual, ~9s callback gap and +17 resync strongly fits the scenario but is NOT synchronized electrical switch/EOF proof. V71 accepts *prior* truncation as immutable history only after a new clean anchor and independently reconciled new frames; it does NOT excuse new partial frames afterward.

## Actually performed local offline evidence

- Final strict g++ C++17 with `-O0 -Wall -Wextra -Werror -pedantic` and ORIGINAL V49 portable C++ `xtr_adapter.cpp/xtr_frame.cpp/xtr_core.cpp/xtr_wire.cpp/xtr_platform.cpp`: **40/40 PASS**.
- Final ASan/UBSan original-source-linked C++17 host replay: **40/40 PASS**, no sanitizers reported.
- **4/4 fail-closed compile tests:** separately `V5DCM42_PRIVATE_TX_BUILD`, `V5DCM42_HARDWARE_PORT_REVIEWED`, `ESP_PLATFORM`, `ARDUINO` builds rejected as intended.
- Tests include: reject unrecorded V49/pending/current safety/history mismatch; exact CRC full ADU; two distinct ADUs in one callback; split 3-byte fragment completed within timeout; unresolved 250ms fragment revoked; V5 absent/raw absent mismatch; corrupted CRC, unknown slave; bounded 4096-byte and 128-frame queues; resync/CRC/drop-counter change; second gap/generation; original B11D first-fault field clearing refused; unsafe DE output; 99 frames not sufficient; 101 matched frames spanning 30s qualify; no TX/Online/owner; live freshness withhold at 3001ms and revoke at 5001ms; continued RX matching after first 30s; old history never reset; clock rollback; irreversible revoke/no auto rearm.
- Program inputs AFTER V49 `Recorded` are **synthetic**, not new local XTR source capture. This does not prove on-device CPU/heap impact, firmware build, live independent frame completion under load, original future line timing or native connection.
- Standalone host package: `V5DCM71_ROLLING_RAW_V5_RX_ONLY_HOST_TESTS.zip` SHA256 `d0e1fd748e32a89912bd692fb8d38f5c2ac38677be70a6a04d29e5f1a2af6ed9` includes `v71_rolling_raw_v5.hpp` (SHA256 `c99c3810a963565b11d9a718fce4474beb3fd5e9ce40d68f898b33cc7593f117`), `v71_host_test.cpp` (SHA256 `c8e9796f58d07b27c3d706102a75283e6b82b5e520cb0402353a340b72fb4e5f`), runner, README, SHA256 manifest. Does not contain user-private V49 files, secrets or a native response engine. Reproduce: `python3 run_v71_offline.py '/path/to/V5DCM49_RX_ONLY_POST_GAP_COHORT_PREPARED_NOT_FLASHED(3).zip'`. Sanitizer run with `V71_SANITIZE=1`.

## Classification and next

**PROVEN OFFLINE/SOURCE:** one original RX callback can supply both copies needed for a separate, nondeployed, independently CRC-framing/byte-matching rolling read-only observer; fixed V49 (frozen) cannot. Existing original first-fault histories can be preserved; host test fails on attempted clearing and on any new incomplete frame fault. 40+40/4 denials hold.

**STRONGLY SUPPORTED:** it is meaningful to distinguish past restart truncation from current communication health, but only with a new independently verified time-bounded cohort, not by suppressing B11D/P5. A newly observed incomplete message after clean anchor is not automatically normalized.

**HYPOTHESIS:** a future ESPHome integration of a *separate RX-only* rolling witness could diagnose recovery on XTR after past B11D sticky faults, provided the missing continuously updating independent input, CPU/heap budget and provenance are established. No original controller-main-board admission rule is proven by this study.

**OPEN/UNKNOWN:** performance of duplicate independent raw parsing on ESP32-S3 under bus load, physical UART owner/EOF/slot, exact live B11D first-fault pre-gap provenance, current 0867 version, acceptance of any future native endpoint and original 2.1.105 app cloud readiness.

**NEXT:** either an offline-only embedded performance/memory/counter-wrap feasibility study before preparing any real RX-only diagnostic build, OR stop and focus on genuinely missing native Connect service preflight. **DO NOT change the deployed V49, merely enable TX flags, auto-clear historic faults, flash the HOST-only header, run incomplete response experiments, or declare controller Online.** A future RX-only ESPHome experiment must be separately prepared (PREPARED / NOT RUN) and validated before the user initiates execution; maintain HA controls and red/brown logs. No live intervention occurred in V71.

**Abort/rollback:** only host compile/test; stop on unexpected compile success with TX macro, source hash mismatch, failed CRC assertion or sanitizer alert and discard research fixture. Device remains on original V49, so no physical recovery or register rollback is needed.
