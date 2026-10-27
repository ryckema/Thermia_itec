# V5DCM74 — Native TX full-service gate audit: first response versus complete DCM session

**ID:** V5DCM74-NATIVE-TX-SOURCE-BLOCKERS-HOST-01  
**Date:** 2026-10-20  
**RESULT: COMPLETE / POSITIVE — exact-source OFFLINE code audit and no-output host tests only.** Actual XTR native output, controller acceptance, Online/C2 and ESPHome build all **NOT RUN / OPEN**.

## Goal, hypothesis, prior results, baseline, one controlled action

**User goal:** solve **native TX emulation**, rather than continue unrelated RX-only optimizations. **Hypothesis:** the existing V49 source's native TX cannot be made functional merely by enabling its two build flags: there are independent clock/session/owner arbitration constraints and missing later application service. Identify all major upstream source gates and an implementable single-owner path without publishing the confidential 0x0F response algorithm or transmitting.

**Last USER-verified XTR baseline:** installed private V49 RX_ONLY/HARD_DENY; user-attested manual controller OFF/ON, 10,351ms RX callback silence followed by frozen clean V49 post-gap witness (285 CRC/RAW/V5-matched frames over 30.532 s, zero new original B11C/B11D faults and UART TX0 by on-device counters). Seven timed CRC-valid 0x0F FC23 requests began after return, later cumulative 63 with a >13-minute unsampled console interval, **zero actual native response**. Source strict 03E8/0864 and FC03 0708 not observed in bounded consoles; peer responder/owner/electrical EOF/slot, flashed machine-code hash, controller version 0867 UNKNOWN. EXP388 RUNNING / PARTIAL is unchanged.

**Past locally executed experiments preserved:**
- EXP254/255 COMPLETE/POSITIVE no responder → 63 approval requests, no native 0708.
- EXP256 COMPLETE/POSITIVE one bounded historic reply → first FC16 03E8/count14 approximately 124ms later; missing subsequent ACK causes repeats and **real COMM. ERR ONLINE/LINK / DHW-side 0**.
- EXP257/258 COMPLETE/POSITIVE one exact first-page ACK each → sequential 03FC/count11 and 0410/count22.
- EXP355/386 COMPLETE/POSITIVE full previously qualified native runtime/restart chain → ordered historical 32/32 native settings ACK and later 085F service + 0708 status; different session, not proof the present controller would accept an arbitrary reply.
- V47 COMPLETE/INCONCLUSIVE (manual restart, old B11D 17-byte partial, +17 parser resync; one-shot Arm but **zero UART TX**), V48 original-source proof, V49 positive RX-only, V69 source build-lock confirmation, V70–73 separate host RX **diagnostic only**, NOT an authority to send in the first cold 1.3s.

**Sole controlled V74 intervention:** pin and inspect *unchanged* original V49 ZIP and original V42/V43/V44B/V45 source, compare with archived V4.1 historical native service outcome, then compile **original V42 OneShot and original V45 DE-owner decision source** against a non-hardware FakePort, with and without both V42 build macros (HOST ONLY). Also test source assertions, initial-vs-late frame fan-out using anonymous booleans and time-stage relationships. No private computation, no native request/reply frames, no 0x0708 mailbox, no new YAML, no controller/pump power action, no TX.

## Exact source pins and reproducibility

- Original pinned private V49 ZIP SHA256 `62afe39629102a3daa06f09eab3ed159f44437d702fb8d3904c61e62e2a85630`, YAML SHA256 `fe02f0b0a503f8f896442165e57397afeacd22cf951efa46ea87885f98d71c22`, 69 source entries.
- Original header SHA256:
  - V42 OneShot `2ca917afea80ba4cfa8b25748a75bc31b53b74ab11a5436254cebaf67a236c00`
  - V43 ESPHome runtime `9652ae34b413c640085bfefe5926976cd7d86ce010b51e5ebeb5a98fd4abfe41`
  - V44B live runtime `542ef764413edd4db51cac8a5403356695dc989d6dfd108dbbe80994b0242fda`
  - V45 DE owner `649c820ba45fbbbbbcdbdcdab2f849956f6c587acacf0540fb413b4e170e4922`.
- Historical TX-enabled repository source `Write (Beta)/thermia_itec_xtr_m_waveshare_write_beta_v4_1.yaml` SHA `8e8a82689e53528a8b751a1abbd901f683b6b238` (GitHub blob SHA, not user-flashed binary digest). Contains a historic native initial bootstrap and runtime service implementation, but a *different* lifecycle and earlier response strategy; **DO NOT blindly paste hard-coded historic response** into current private V43.
- User-only **safe host audit package** `V5DCM74_NATIVE_TX_SOURCE_GATES_OFFLINE.zip` SHA256 `7a9e4ff2de51e5218ff1e5a103df546dd476e4d24c282a4e4bd19f76bbf4c8f6`. It contains *only* non-hardware FakePort test, source scanner, README, results and SHA256 manifest; requires user-supplied pinned V49 original to run, does NOT bundle original private source, response algorithm, keys, protected frames or bus tooling.
- Reproduce with `python3 run_v74.py /path/to/original-V49.zip`. Runner refuses hash mismatches.

## Actual V74 test results

**27/27 independent source/static checks PASS** (13 exact private-header invariants, eight live V49 YAML integrations including only-first `parsed.front()`, six negative/no-other-owner/no-legacy-stage constraints).
**23/23 host assertions PASS** with ordinary default V42 build = `kBuildMaySend=false`.
**23/23 PASS** with both V42 enabling macros defined in a C++ host-only build and a fake Port; the exact original V43 arm inputs still fail and `FakePort.tx_count=0`.
**23/23 + 23/23 PASS** rerun with AddressSanitizer and UndefinedBehaviorSanitizer in both builds. The host tests do **not** exercise a request-response native computation or actual electrical timing.
Original V42 `physically_confirmed()` and `real_online_confirmed()` remain false by design.

## Observed source blockers in order

1. **HARD BUILD GATE — PROVEN:** V49 omits both `V5DCM42_PRIVATE_TX_BUILD` and `V5DCM42_HARDWARE_PORT_REVIEWED`; YAML contains `static_assert(!v5dcm42::kBuildMaySend)`. Existing V49 could never send. But that is only **the first gate**.
2. **V43 ARM IS DELIBERATELY UNQUALIFIED — PROVEN:** source `user_arm()` passes **controller generation=0**, `timing_independently_qualified=false` and does not set explicit `one_shot_timing_risk_explicitly_accepted`; original V42 `arm` rejects such inputs as `MissingContext` EVEN in a fake test with both native build flags defined. Simply flipping flags is insufficient.
3. **WRONG COLD-RESTART ARM WINDOW — PROVEN source + LOCAL contrast:** V43 sets **1,000,000μs (1 s)** to wait for the entire new request. Actual V49 user restart had 10.351s callback gap and earlier first native FC23 appears ~1.3s after bus return; arming V43 before the power interruption cannot cover the restart. Existing separately tested V44B actor instead has a **30-second** accepted-risk one-shot Arm. This is only an arm scope, **not** a measured electrical response-slot deadline.
4. **V43 PEER / OWNER / EPOCH / SLOT GATES ALWAYS FALSE — PROVEN:** its `fresh_unqualified_` supplies `no_competing_peer=false`, `owner_scoped=false`, `current_epoch_scoped=false`, `response_slot_scoped=false`. Nothing in a CRC-valid parser callback alone can certify those physical/electrical facts.
5. **TWO ACTORS, ONE PHYSICAL PORT — PROVEN SOURCE INTEGRATION HAZARD:** V43 and V44B both bind the same ESPHome UART and RS485 DE GPIO switch. Original V45 B11D watchdog recognizes a legitimate DE HIGH **only** if `v5dcm44b::runtime().b11d_tx_window_owned`; periodic 1s force-RX watchdog defers **only** for `v5dcm44b::runtime().defer_periodic_rx_watchdog()`. A hypothetical V43 TX DE assertion is **not** recognized as owned, so at the B11D periodic check it could permanently latch unsafe DE; another actor/watchdog can force RX. This is a source-inferred risk, **not a newly measured collision or V43 actual TX**. One jointly arbitrated actor is necessary before any TX candidate.
6. **INCOMPLETE CALLBACK FAN-OUT — PROVEN SOURCE:** at V49 callback the only forwarded frame to both V43/V44B is `parsed.front()`. The remaining completed frames are processed by other observers but **not** offered to these TX actors; a native request in second position can be missed. Host abstract two-token test confirms the trivial counterexample without creating any confidential challenge bytes.
7. **V49 HAS NO FULL SERVICE CHAIN — PROVEN CODE DIFFERENCE:** exact current V49 YAML lacks V4.1 `id(write_stage)` logic or the proven full ordered FC16 ACK and 0708 status responder. Therefore merely unlocking first native 0x0F FC23 reply would recreate the real incomplete-service/COMM ERR risk from EXP256.
8. **30-SECOND REQUALIFICATION COMES TOO LATE FOR FIRST COLD REPLY:** historical first cold FC23 appears ~1.283s after bus return; V70–73 need >=30s additional independent clean frames and V49 freezes 30.532s after clean anchor. These are valuable RX-only diagnostics, but impossible to demand BEFORE first cold approval response. A separate safe **early-cold-RX policy** is required that preserves first-fault provenance, excludes pre-gap orphan bytes and immediately rejects new CRC or peer/output faults; it cannot just clear B11D or claim physical owner.

## Provenance distinction, unknowns and decision

**PROVEN local XTR:** historical no-response vs one-response vs sequential ACK vs full-service *particular session* progress (EXP255–258/355/386), plus user V49 no-TX baseline and clean passive gap cohort.

**PROVEN original source/host:** the eight gate findings above (some risks conditional on unperformed V43 TX); 27 source invariants + four sets of 23 host checks. Original Connect 2.1.105 2.4.2 application significant-group tracker = **33 groups after version/WAIT** (V62–68), distinct from the **historical 32/32 native controller ACK chain**; don't treat a source model as local acceptance proof. Original Connect internal H2 after FC16 is not controller master approval.

**STRONGLY SUPPORTED:** next implementation must be a **single bounded native TX transport owner with a complete service lifecycle**, not V49 with `#error` removed, not a standalone V43/44B single reply, and not unverified v4.1 replay of a historic static response.

**OPEN:** exact active physical sender, wire EOF, response slot, competing peer, current 0867/profile, acceptance of dynamically computed native approval, whether current controller would progress, OEM 33-group app C2 and actual Online/HA connectivity. No new DCM hardware exists for new OEM capture; use existing genuine/peer captures and firmware. Existing one-response live run harmed communication state, so do NOT replay an incomplete endpoint.

## Safety and concrete next action — V75 source-only TX architecture

**V74 negative criterion:** any original-source hash change, test failure, demonstrated current V49 native TX, or evidence that first-answer-only is a safe complete session. **Positive achieved:** multiple independent upstream blockers reproducibly confirmed. **Unanswered controller master acceptance is INCONCLUSIVE** by absence of new TX. **Abort/rollback:** offline-only, discard host candidate on failure. No on-device target/slave/register/wire payload/expected plant effect in V74, because **nothing was sent**. Current V49 remains RX_ONLY/HARD_DENY, no flash, no need for device recovery.

**Prepare NEXT as a separate V75 OFFLINE implementation (not yet run):**
- One and only one native TX actor and DE/GPIO arbiter, with permanent default HARD_DENY and no second UART reader.
- The **existing** CRC-valid callback supplies **every** complete frame in order; no `parsed.front()` limitation. Scope to the controller-origin exact native FC23 request for slave0x0F, public geometry 0730/count8 and 071C/count8; do not publish/generate private response bytes here.
- Controller-gap/return observations (software epoch **candidate only**), pre-gap B11D fault attribution plus new per-frame independently checked RX, no concurrent owner, both GPIO and software DE low, bounded one user acceptance and no unsolicited send. First response window must be early enough for observed +1.3s post-return request but physical wire EOF/slot remains unverified, so **do not mark TX-ready** without separate reviewed evidence.
- Offline fake-Port full-session state-machine progression with ORIGINAL historic XTR first pages 03E8/count14, 03FC/count11, 0410/count22, remaining 32-stage local ACK service, followed by exact runtime FC16/0708 handling. Original Connect significant-app-33 profile tracking is **independently monitored**, not a guessed extra wire ACK stage. Every unexpected frame, new parser fault, lost owner, timeout, DE mismatch, incomplete app service or operator Abort → force RX/stop/no retry; test all before contemplating private on-device TX build.
- Future live controlled test, if ever prepared, must pin current versions and full transaction/rollback, declare exact permitted slave/addresses/response class with physical no-conflict/slot evidence, and require user to initiate it. Do NOT flash the V74 host tools, port a legacy static response as universal security, enable compile flags alone, clear original faults or publish private 0x0F response code.
