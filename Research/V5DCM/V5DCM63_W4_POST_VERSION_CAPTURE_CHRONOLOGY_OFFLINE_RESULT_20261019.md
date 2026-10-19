# V5DCM63 — Genuine archive W4-group chronology against original Connect 2.1.105 tracker

**ID:** V5DCM63-W4-POST-VERSION-CHRONOLOGY-OFFLINE-01
**Date:** 2026-10-19
**Status: COMPLETE / POSITIVE (independent archival CRC/shape/chronology ONLY); original on-device application C2, Online, and current XTR acceptance remain OPEN / INCONCLUSIVE.**
No live bus transmission, ESPHome compile/flash, controller restart, sensor disconnection, native FC23 response or 0708 command tooling.

## Hypothesis, baseline, one change and evidence rules

**Hypothesis:** Archived genuine/collaborator DCM FC16 transfer recordings contain enough **post-0864** page chronology to distinguish visible repeated receipt opportunities for the 33 **original Connect 2.1.105, selected 2.4.2-profile significant groups** from mere historic 32-page native bootstrap. An FC16 request shape plus short ACK envelope is not proof of internal application tracker completion.

**User's last verified on-device baseline:** V49 RX_ONLY/HARD_DENY after user manual controller OFF/ON, 10,351ms UART callback gap, 285 clean matched post-gap frames/30.532s; UART TX=0, original HA entities and parser/fault latches intact; sampled 03E8/0864/0708=0, 04A6/085F recurring; first 7 FC23 challenges unanswered and later cumulative 63 after a >13-min console observation gap. V47 remains COMPLETE/INCONCLUSIVE. Previous local EXP254/255 no-responder full 63-challenge sequences and EXP355/386 historic 32/32 positive unchanged.

**Earlier completed work checked (NOT repeated as new discovery):** V54 original-source 2.1.105 internal app gates; V55 25,031-frame first-event and version chronology; V57 first-version same-callback credit and 8-byte ACK correction; V59 seven historical cross-model response-shaped episodes; V62 25/33 overlap and eight missing W4 groups; R6-P74DI-B10/B12 and V40 file-provenance errata. This experiment adds a **new narrowly scoped post-first-version group/ACK census**; no new firmware method execution and no new experiment on hardware.

**One controlled offline change:** parse the *same seven original user-supplied time-plus-RTU-hex files* independently for CRC-good FC16 request **start/count**, matching 8-byte FC16 ACK **envelopes** (same start/count, forward <=300ms host-clock analysis filter), and FC23 request/reply shapes; for each FC23 reply-shaped event, bound a documentary segment at the **next native FC23 challenge shape or file end**. Inside each such segment, find first FC16 **0864/count>=4** and list distinct members of the V62 **33 original profile-dependent group starts** at or after that event (strict log row order, not just coarse equal timestamps); also count how many of these distinct group requests have any host-near matching FC16 ACK shape. Compare earlier group types BEFORE the same 0864. Segments are NOT measured controller physical epochs or proven ownership intervals.

**Passive targets, not TX authority:** 0x0F FC16 W4 page starts 07D0/07E4/07F8/080C/0820/0848/0864/0870, the 25 firmware-selected W2/W3 settings-page starts, FC23 29-byte challenge/21-byte reply-shaped envelopes; no register-value writes, outgoing payload, delay budget or physical effect. Positive: all original CRCs valid, coherent documentary before/after version groups, appropriate counterexamples. Negative: bad raw source or incompatible chronology; inconclusive: model identity, physical receiver, software WAIT/C2 or Online. Abort offline work on CRC/source mismatch or any accidentally included protected bytes; no device rollback.

## Evidence provenance and raw integrity

The seven files in the existing attached project corpus total **25,031 / 25,031 valid CRC rows; zero invalid**. Names and validated geometry:

| Source | Rows | Firmware-selected 33 group types ANYWHERE in file | W4 among them | First visible FC16 0864 | Provenance |
|---|---:|---:|---:|---|---|
| thermia_capture_20260924_210001(1).log | 394 | 8/33 | 8/8 | +14.176s | historically listed local; model/owner not newly physically authenticated |
| thermia_capture_20260925_071517.log | 674 | 9/33 | 8/8 | +5.244s | September identity uncertain; do not treat as independently local-XTR proof |
| thermia_capture_20260925_090209.log | 491 | 30/33 | 8/8 | +50.828s | September identity uncertain; do not treat as independently local-XTR proof |
| thermia_capture_20260925_090550.log | 892 | 26/33 | 2/8 | none | September identity uncertain; do not treat as independently local-XTR proof |
| thermia_capture_20261003_165355.log | 2,687 | 33/33 | 8/8 | t=86.672s | **ATEC + classic DCM03 COLLABORATOR**, NOT XTR |
| itec_eco5_gateway_20260926.log | 10,719 | 33/33 | 8/8 | t=7.961s | **Eco5 COLLABORATOR** |
| itec_eco5_gateway_20260928.log | 9,174 | 33/33 | 8/8 | t=4.574s | **Eco5 COLLABORATOR** |

**Critical provenance guard:** R6-P74DI-B10/B12 (2026-10-13) explicitly classified September thermia_capture device model as **UNKNOWN** (legacy/ATEC-like geometry), despite some earlier V55/V60 shorthand labeling them local XTR. V40 corrected the Oct03 ATEC capture. This report does not silently upgrade the September files into independent XTR evidence. The *separately user-confirmed active XTR EXP254/255/256–258/355/386 results* remain locally grounded via their own experiment histories. Original cross-model firmware value metadata per V55: September/ATEC 0867 raw22, Eco5 raw232; neither attests the **currently installed V49** firmware version or actual gateway client software.

## Seven reply-shaped, analytically bounded episodes: what reappears AFTER first 0864?

In ALL SEVEN segments the recorded sequence BEFORE first post-reply 0864 contains **31/33 distinct selected group-start types: all 25 W2/W3, plus six W4 (07D0,07E4,07F8,080C,0820,0848)**. The next two W4 in the observed first-order pattern are version-bearing **0864** itself and **0870**. This is a *visible order of FC16 REQUEST envelopes*, not proof of when genuine 2.1.105 software set WAIT or credited 0864.

| Episode anchored on FC23 reply-shaped event (host seconds) | First later 0864 | Distinct required group requests AT/AFTER 0864 | Groups with matching short FC16 ACK shape (<=300ms host filter) | W4 group types absent AFTER 0864 |
|---|---:|---:|---:|---|
| ATEC Oct03, t27.429 | 86.672 | **8/33** | 8/33 | none; all eight W4 present |
| Eco5 Sep26 #1, t303.615 | 357.491 | **2/33** | 1/33 | 07D0,07E4,07F8,080C,0820,0848,0870 |
| Eco5 Sep26 #2, t723.286 | 805.663 | **33/33** | **33/33** | none |
| Eco5 Sep28 #1, t313.728 | 363.291 | **31/33** | 31/33 | 0820,0848 |
| Eco5 Sep28 #2, t447.825 | 607.887 | **33/33** | **33/33** | none |
| Eco5 Sep28 #3, t744.353 | 908.579 | **30/33** | 30/33 | 080C,0820,0848 |
| Eco5 Sep28 #4, t1094.717 | 1144.278 | **31/33** | 31/33 | 0820,0848 |

For the two 33/33 shape-and-ACK-census episodes, earliest *all distinct group-start types have become observable at least once after 0864* is **+79.947 seconds (Eco5 Sep26 #2)** and **+81.025 seconds (Eco5 Sep28 #2)** after first in-segment version page. These are host-log chronology intervals, not a firmware timeout. The actual original host method's state transition, internal group receipt ledger, application information serial/version readiness and parameter-map publication were **not recorded**.

**Careful definitions:** 'ACK paired' means an 8-byte Modbus FC16 address/count ACK-shaped frame appears after one same-geometry controller request within an **analyst-chosen 300ms log-time window**. It does not prove physical sender, original Connect process participation, receipt into a configured CM930 instance, settings semantics or cloud Online. Some requests are unACKed, and 300ms must NEVER be treated as safe TX deadline.

## Findings, confidence and limits

**PROVEN archived raw (source provenance as above):**
- All 25,031 frames were CRC checked independently. This is a new *post-0864 group* reduction of existing data, not a new capture.
- In seven cross-model reply-shaped segments, 25 selected W2/W3 plus six W4 group REQUEST shapes appear BEFORE first following 0864. First visible version-bearing 0864 is **not equivalent** to all original application settings being ready.
- Counterexamples: ATEC segment has all 33 distinct types anywhere yet ONLY eight post-0864 and no post-version settings groups; Eco5 two segments have 33 post-version ACK-paired *types*, while others have 2,30,31. Full-file 33/33 is therefore a misleading substitute for temporal application completeness.
- Four September archives cannot all be called proven local XTR when historic origin remains unresolved. This is a documentary evidence-strength clarification, not a reinterpretation of their valid RTU bytes.

**STRONGLY SUPPORTED original-firmware INTERPRETATION (not a proven actual running process):** 2.1.105 starts its 33-group tracker when it recognizes version/profile, ignores pre-WAIT receipts, and may credit the first version group in the same callback (V54/V57/V62). Thus a hypothetical newly started tracker would see different possible progress depending on whether post-version settings/runtime pages are resent. The two 33/33 post-version Eco5 windows are **consistent with** a complete compatible receipt stream; the other five windows do not provide same-window **post-first-version** 33-group evidence. Actual firmware/version/profile loaded by collaborators and whether prior cached state persisted are unmeasured; do NOT label actual '2.1.105 C2' successes/failures.

**HYPOTHESIS:** A full DCM application may require post-profile refreshes/republication of otherwise already bootstrap-ACKed settings pages. Exact triggering request flags, original async queue outcomes, gateway cache persistence and on-wire sender remain open; this report cannot derive a universal startup sequence from callback or host times.

**OPEN / UNKNOWN:** Current local V49 processor version at 0867, independent XTR 33/33/actual W4 receipt after fresh version, exact 2.1.105 application map-publish/onboarding/cloud status, physical owner/electrical EOF/response slot/current dynamic acceptance. The old XTR EXP355 32/32 native success is still real but is NOT original 2.1.105 application C2 proof.

## Result, abort/recovery and NEXT

**COMPLETE / POSITIVE only for offline raw shape and chronology audit**; physical/native application status remains OPEN. All before/after counts are row-order preserving, frame CRC/FC16 length and bytecount validated, and segments terminate before next later FC23 *challenge shape* or EOF. No physical action, TX, compilation, YAML/HA edits, register write, controller reset, fault-latch clearing, firmware modification or secrets publication; no hardware rollback.

**Next useful offline direction:** correlate the original 2.1.105 CM930 info/version/profile and startup request-event schedule with *repeated post-first-version selected W2/W3 pages* in the TWO Eco5 windows that have 33 ACK-paired groups, while keeping explicit the unknown actual collaborator software and no proven C2. If that cannot distinguish code-level request generation from controller periodic refresh, mark the source-only ceiling; do not re-run passive cold boot or protected active handshake/0708 tests on V49.
