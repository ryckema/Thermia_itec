# V5DCM75 — Single-owner full native session intent model (host-only, no wire TX)

**ID:** V5DCM75-SINGLE-OWNER-FULL-SERVICE-INTENT-OFFLINE-01  
**Date:** 2026-10-20  
**Status: COMPLETE / POSITIVE — OFFLINE SOURCE-ANCHORED ARCHITECTURE ONLY. LIVE NATIVE TX / ORIGINAL CONNECT ADMISSION / CLOUD ONLINE: NOT RUN, NOT PROVEN.**

## Hypothesis, known-good baseline and prior results

**Hypothesis:** one logically exclusive native TX service actor can fail closed on absent physical context, dispatch *every* completed frame from the already-existing UART RX callback, track the historically locally confirmed **32 exact controller bootstrap FC16 request shapes** and later runtime FC16/0708, and refuse to claim session success without independently supplied delivery confirmations. We must not publish/run a protected 0x0F algorithm or unreviewed bus responder.

**Last verified local user device:** currently installed exact V49 source family `RX_ONLY/HARD_DENY` (private 69-entry ZIP SHA256 `62afe39629102a3daa06f09eab3ed159f44437d702fb8d3904c61e62e2a85630`), user-confirmed manual controller OFF/ON and software RX gap 10.351s; a V49 terminal historical cohort of 285 independently matched CRC-valid frames across 30.532s; all local native UART TX counters 0. First seven canonical slave0F FC23 requests timed just after bus return, later 63 cumulative with a long unsampled interval; no native answer or 03E8/0864/0708 service in bounded present console. Exact flashed binary SHA, physical owner, electrical EOF, exclusive physical response slot and version 0867 NOT verified. **EXP388 stays RUNNING / PARTIAL**.

**Earlier relevant local results unchanged:** EXP254/255 (63 no-responder requests), EXP256 (one bounded *real* historical answer triggers 03E8/count14 roughly +124ms but no later ACK, repeated requests and real COMM. ERR ONLINE/LINK plus DHW-side symptom), EXP257/258 (single ACKs induce sequential 03FC/count11 then 0410/count22), EXP355 and EXP386 (previously qualified full native 32-page initial sync and 085F/0708 persistent status). V47 was locally inconclusive for TX with a real old 17-byte incomplete / 250ms B11D latch, no output. V49 remains hard-locked. V74 found eight source blockers: V43 context FALSE / 1sec Arm, dual DE owners and B11D watchdog ownership mismatch, first-frame-only forwarding, and missing full service. V70–73 postgap 30s RX diagnostics are downstream and cannot authorize first cold FC23 ~+1.283s after bus return. **Do not repeat EXP256's intentionally incomplete endpoint.**

## One controlled offline implementation

Create a **nondeployable, host-only C++17 intent state machine**, `v75_session_intent.hpp`. This implements *no* native frame byte generator, modbus response, challenge transform, secret, 0708 mailbox, UART, GPIO, DE driver or native output. Every Intent `possible_hardware_output=false`; `native_tx_authorized()=false`, `physical_owner_proven()=false`, `real_online_proven()=false`, always. Compile-time `#error` for ESP_PLATFORM, ARDUINO, or either original V42 hardware/native TX build macro.

**Single logical owner and stage sequence:** Idle → explicit operator scope → independent controller return proof → exact CRC-complete challenge event → *INTENT requiring EXTERNAL confirmation* → 32 exact in-order native FC16 source pages, each with an independent *INTENT and confirmation* → observed runtime native FC16 page confirmation → observed `0708/count6` status-request response *INTENT and confirmation* → `Active` in **synthetic host model**. Any missed delivery confirmation, new peer, unexpected page/count/order, peer response, CRC failure, generation/clock change, new RX fault, DE disagreement, loss of owner/slot/exclusivity, age expiry, operator Abort or excessive batch irrevocably revokes. A generated intent is **never** proof of wire transmission and an FC16 address/count ACK is **never** proof of semantic acceptance. `Active` is only a modeled locally historically service-qualified transport stage, not Connect C2/cloud.

**Time windows are host-only POLICY proposals, not measured electrical wire deadlines:** operator pre-return scope <=60s, first new exact challenge <=5s after separately witnessed return, per-page <=5s, entire bootstrap <=90s, runtime transitions <=15s, later active service <=30s. Observed old local XTR request appeared ~1.283s after return in some cold tests; V49 user gap 10.351s. The test uses **synthetic independently witnessed owner/slot and delivered-confirmation booleans**; these are NOT satisfied by currently installed V49. Distinct early-cold qualification would still be needed on live hardware; V70–73 RX cohort not used to grant it.

The `frames(events,n, callback)` method iterates up to 128 prevalidated abstract events **in order**, including an unrelated slave first and an approval request second, fixing the *architectural omission* of V49 presenting `parsed.front()` to both existing actors. It is NOT a new UART parser. Actual integration into the existing ESPHome callback and removal of duplicate V43/V44B physical writers have NOT happened.

## Exact 32 versus original vendor 33 source reconciliation (new source comparison)

Original GitHub `Write (Beta)/thermia_itec_xtr_m_waveshare_write_beta_v4_1.yaml` blob SHA `8e8a82689e53528a8b751a1abbd901f683b6b238`, stages `write_stage=3..34`, each guard `st==0xXXXX && ct==N && bc==2N`, was reviewed directly. It gives exactly **32 native initial ACK pages**, starting `03E8/14, 03FC/11, 0410/22` and ending `06EA/7, 06F1/3, 06F4/19`. Each of the 32 pairs appears once in the host-only source model; no payload or ACK RTU bytes included.

The exact pinned original V49 `v5dcm22_v5dcm19_rx33_witness.hpp` contains a **different** source-derived Original Connect 2.1.105 2.4.2 significant *app package* profile of 33 start/count pairs. **Set comparison:** 32 controller ACK pairs vs 33 app-required pairs have **25 matches; 7 only in native bootstrap; 8 only in app-significant profile**. The app-only group includes original 0864/count4. This is SOURCE / firmware-derived profile, not proven on-device 2.1.105 parameter-map completion; controller success 32/32 cannot be substituted for OEM app 33/33 or Online.

## Actually run, reproducible tests

- **6,444 host C++ assertions PASS** in each of three runs: `g++ -std=c++17 -O2 -Wall -Wextra -Werror -pedantic`, ASan/UBSan, and `-fno-exceptions -fno-rtti`. The count includes systematic per-stage checks and pair uniqueness; it is NOT 6,444 independent device experiments.
- **4/4 NEGATIVE compile builds properly rejected:** ESP_PLATFORM, ARDUINO, V5DCM42_PRIVATE_TX_BUILD, V5DCM42_HARDWARE_PORT_REVIEWED.
- Original V49 69-entry ZIP SHA/CRC, YAML V43/V44B source, static original V49 output build lock and first-frame-only forwarding provenance verified in the host runner.
- Successful synthetic nominal 1+32+1+1 = **35 hypothetical delivery-confirmed intents** before modeled runtime active, then active service two more; every Intent has `possible_hardware_output=false`.
- Real V49 physical-owner=false / response-slot=false fixture rejects before *any* intent. No independent power-return evidence refuses stage entry. Wrong ticket, unconfirmed first reply, missing current fault history/DE low/peer exclusivity, corrupted CRC, duplicate/incorrect page, second-stage early status, later new peer, runtime unknown page, stale clocks, overdue request, operator Abort and generation changes fail closed.
- `frames` processes approval in SECOND slot when first completed event is another slave; a later unconfirmed event does NOT silently advance.
- Exact local V49 descriptor comparison verifies vendor significant33 / historic native32 = overlap25, native-only7, app-only8.
- No RAM/CPU/ESPHome compile/flash/hardware timing measured. Any true physical wire EOF/slot, controller 0x0F dynamic reply or genuine Connect Online acceptance remains UNKNOWN.

**Artifact** `V5DCM75_SINGLE_OWNER_FULL_SESSION_INTENT_HOST_ONLY.zip`, SHA256 `f43c9afe747831183968c57ccf66bb0f3271d70e88626db8df78d8ee2263b61a`. Verified six-member integrity / SHA manifest: header `dc03a7a9c2331ee145869be6a1b699f66e52db1976ff2580c0daa338d776faa6`, tests `c7237804945e0e35ef282ac1b3e8e069b617ad9011e747f3f0215e6a9308a5c3`, runner `c500e38e9a309109b9133b391b1434420bccdcaa2903ebfbde6d91ced601d0fb`. Original private V49 code is NOT bundled or published. Reproduce locally with `python3 run_v75.py '/path/to/original pinned V49 ZIP'`.

## Proven / strongly supported / hypotheses / unknowns

**PROVEN original local XTR:** 32 native page ACK sequence and runtime observations in their original historical qualified sessions; V49 no-response current state.  
**PROVEN ORIGINAL SOURCE/HOST:** a single no-output intent actor can model the exact local 32-stage sequence, require delivery confirmations and fail-closed guards; 6,444 assertions and 4 compile denials. **PROVEN source comparison:** 25/7/8 overlap difference with Connect 2.1.105 significant profile.  
**STRONGLY SUPPORTED:** one arbiter with full lifecycle is safer/more relevant than enabling a disabled V43, duplicating V44B or answering one request then abandoning FC16.  
**HYPOTHESIS:** integrating an exclusive TX actor with the *existing private dynamic* native backend and real full service, with newly measured electrical slot/owner evidence and early post-return RX checks, could let the local XTR progress. There is no new local proof of that and not every historical answer is dynamically valid for every challenge.  
**OPEN/UNKNOWN:** independent owner/exclusive timing/EOF, new physical generation proof, current version0867, original 2.1.105 selected profile + ALL 33 app receipts, actual GPIO DE-safe shared driver, complete ACK/status response delivery, semantic acceptance or Online.

## Positive / negative / inconclusive, abort / recovery, next action

**V75 OFFLINE POSITIVE** criteria met: exact original local controller stage mapping, full intent-only bootstrap/runtime and safety denial, single logical owner, correct chronological multi-frame routing, reproducible strict host tests. **NEGATIVE on future evidence:** any out-of-order native page promoted, missing confirmation treated as delivered, TX allowed by source, incorrect original page count, physical peer conflict not vetoed. **INCONCLUSIVE for hardware native acceptance**: NO live new reply attempted and physical owner/slot unknown.

**No physical live target/payload/current setting/transmission timing in V75:** host only, so abort on host test failure and discard prototype; no device recovery required. Old user V49 remains unchanged RX_ONLY/HARD_DENY, no controller reboot, no YAML/ESPHome/HA changes, no GPIO activity, no new UART frame, no cryptographic implementation published.

**NEXT (separate V76 offline TX integration preflight, NOT YET RUN):** source-validate a *single* physical UART+DE owner and the preserved private dynamic response backend **without exposing it publicly**, translate V75 INTENT flow into a bounded, fail-closed full-service transaction adapter and test with a fake port, prohibit output if owner/physical EOF/slot is still unknown; test current peer/B11D/DE watchdog arbitration, missing ACK or stage timeouts and recoverability. Decide on an operator-initiated live test only after explicit target frame, risk, slot, full-service and abort/recovery evidence. Do not simply enable TX flags or repeat EXP256's deliberately incomplete single-reply test.
