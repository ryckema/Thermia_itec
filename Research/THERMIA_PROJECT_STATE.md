# CURRENT — 2026-10-11 R6-P30 Stage C offline complete; Stage B actually LIVE RX-only

> Supersedes prior **current-status** headings lower in this file, including the preceding R6-P24 / R6-P29 update. Historical experiment observations below are retained unmodified. Do not infer a new native owner or bus action from Stage C host tests.

**LIVE XTR M baseline now:** R6-P30 **Stage B** is actually deployed and running as the passively extended R6-P24/Bridge15C image, not just a prepared YAML. Original user-supplied log "Pasted text(20261011-000121).txt", ESPHome 2026.9.0 API, 01:59:17.735–02:01:14.407. Stage B **COMPLETE / POSITIVE within the bounded live observation**: new "R6 P30 Native Page Census" and "R6 P30 H021 ReadOnly Eligibility" publish. Across twelve sensor snapshots the census progressed from 21 to 174 observed FC16 frames, all 174 with matching known page geometry; unique setting/runtime families remained 1/32 and 1/11 (04A6/13 and 085F/5). Four targeted H021 source pages **03E8/14, 042E/15, 0442/13, 0546/20** were not observed; H021 eligibility remains 0/4 pages and 0/22 values, **COMPLETE / NEGATIVE for target-page reception in this window only**. No genuine live HA H021 engineering values. User deployment confirms device runtime but **not a documented full ESPHome compile**, as the client reused a validated-config cache.

**Live transport and safety:** physical TX attempts=0, S3 UART write calls=0, delivered=0, DE LOW; no new ACK/FC03 response/native writes. V5 parser had **four already-present resync steps** and Bridge02 **one historical integrity fault** at first log sample, stable through the supplied window; observer's local hold=0 does NOT clear those historical counts. Bridge04 passively recovered after healthy frames; B13-SHADOW ABORT_NO_TX logs are correct fail-closed refusals, not transmissions. Bridge11C/11D frame/byte differences and new portable faults/drops remained 0 in-window; historical extended-duration B11D framing risk remains OPEN. R6-P24 start witness continued NO_CALLBACK_GAP_SEEN / EPOCH_UNKNOWN / NO_TX; no controller power cycle or cold-start branch observed. Owner UNKNOWN, physical controller epoch UNKNOWN. Continue RX_ONLY.

**Last completed investigation: R6-P30 Stage C — COMPLETE / POSITIVE for OFFLINE handoff contract and guards; INCONCLUSIVE for actual live qualified native page/HA delivery.** Exact controlled change: new host-only receipt/generation/ack/health gate connecting a *synthetically* 32/32 XTR page+matching-ACK timeline to the 22 H021 aliases using read-only typed interpretation; no code deployed to ESPHome in Stage C. 31 prior Stage A + 42 Stage C tests = **73/73 PASS**. Synthetic fixture decodes 22/22 data fields including signed curve offsets and /10 scaling; never publishes them as real XTR values or grants output. A 32/32 timeline, even with matching ACKs, does **not** itself prove a unique controller power epoch or work owner. Evidence gate defaults to NO_LIVE_VALUE, NO_TX, NO_SEMANTIC_WRITE. Stage B live regression audit rechecked 12/12 census samples (cfg=1/32 rt=1/11), H021=0/22, TX=0.

**R6-P30 Stage A — COMPLETE / POSITIVE offline ONLY:** passive Python shadow/model adapter, **31/31 unit tests**, 43/43 XTR page geometries matched to R6-P24 source, 22/22 H021 metadata from exact GitHub catalog (blob a233e9543e9881801c5f53a3ff8b98d9662ed389), 22,580 CRC-good *genuine cross-model* ADUs of which 2,321 have geometry compatible with XTR; no cross-model data promoted to local XTR values. No HA connection, TX or YAML change.

**R6-P30 Stage B preparation (historical):** 2,800-line R6-P24 baseline -> 2,925-line candidate, +125 lines, 0 existing lines changed, full YAML candidate SHA256 a2b68265650b14826fff104d7d559e1d1344b001f87cd0095adad88cf937d152; literal new C++17 lambdas **36/36 host tests**, YAML parsed, full ESPHome compile **not independently captured**. Previous PREPARED/NOT FLASHED status was correct **before** the user's actual Stage B live log but is SUPERSEDED as current device state.

**Current experiment / next:** Stage C COMPLETE/POSITIVE offline. R6-P30 **Stage D PROPOSED / NOT PREPARED / NOT RUN**: safely port read-only page/session validity to existing live Stage B without new responses; first review exact deployed YAML, IDs, cold-/process-epoch evidence and hardware health. Do not automatically flash or reboot. Native autonomous owner, hot-rejoin, valid live H021, 32/32 fresh session in current run and semantic write+readback remain unproven.

**Production/safety:** Preserve existing HA functionality and parser/Bridge11C/11D counters. No autonomous slave-0x0F FC23 answer, FC16 ACK, 0708 response, semantic write, unsolicited UART TX or speculative tests. Current project retains primary goal native Thermia Online/Connect/DCM path, not room-sensor emulation. Source packages/reports R6_P30_OFFLINE_RX_ONLY_INTEGRATION_20261011.zip, R6_P30_STAGE_B_RX_ONLY_PREPARED_20261011.zip, R6_P30_STAGE_B_FIRST_LIVE_RESULT_20261011.md and R6_P30_STAGE_C_OFFLINE_HANDOFF_20261011.zip originate from the user conversation; companion private firmware repo stores a research synopsis. No new device action from this documentation commit.

---

# CURRENT 2026-10-11 — R6-P24 LIVE / PARTIAL; R6-P25 to R6-P29 offline results

**Current-state override:** all historical LATEST / NEXT / R6-P24 PREPARED headings below reflect their original dates. Their observations remain preserved, but this top section governs current interpretation.

**Live XTR M:** R6-P24 passive RX-only controller-start witness actually flashed and user-logged. Two normal-traffic excerpts ~00:42:52–00:43:18 and ~00:46:32–00:50:27 showed NO_CALLBACK_GAP_SEEN / EPOCH_UNKNOWN / NO_TX; qualifying gaps=0 and cold-start events=0. Later V5-valid rose 1997 to 3870 without a new resync. One older initial parser resync persisted as count 1 in the first excerpt, observer recovered; 11C/11D bounded counters stable, physical TX=0 and DE LOW. New independent A80E/A80F observation works while older Bridge02 qualifying snapshots may stay NAN. Four Bridge15C target configuration pages still absent. **R6-P24 RUNNING / PARTIAL:** passive no-gap function positive; controller-start branch NOT EXERCISED, long-run B11D issue not disproven. No controller restart.

**Newest completed offline R6-P29 step 1:** documented three ESP-OTA evidence gaps: S11F last 0884 to S11G first 085F/0708 = 45m05.715s; S11W 07D0 (signature 8721F668) to S11X original 07D0 (D7EC8823) = 6m02.749s; S11X original to FIX1 stable 07D0 signature D7EC8823 = 7m29.287s. These are elapsed intervals between documented events, NOT recorded wire silence or exact OTA duration. Historically S11X FIX1 manually ACKed retained 07D0 then 07E4 followed ~2.041s later. Step 1 **COMPLETE / POSITIVE for documentary coverage audit (32/32 checks), INCONCLUSIVE for independent continuous controller epoch/identical work-item**. Original local XTR full logs were not newly re-CRC-parsed. R6-P29 step 2 secondary hardware sniffer/software package **PREPARED / NOT RUN** (16/16 offline checks); no second device installed, no independent OTA capture. Existing Bridge11C/D are different software observers on the same ESP, not independent OTA recorders. Hardware repetition currently not prioritized without a qualified new live owner.

**Recent offline studies, no new bus actions:**
- **R6-P25 COMPLETE/POSITIVE offline:** six genuine cross-model Online/DCM captures, 22,344 CRC-good frames, 327 FC03 0708 polls and 302 paired replies; legacy hot-rejoin involved 16 unanswered polls, then answered W2:W3=7FFF:FFFF and exact 31-page settings sync (excluding 06F4) with matching FC16 ACKs. W4=0080 or W5=0007 as universal rejoin-owner indicator NEGATIVE; local XTR generalization INCONCLUSIVE; 40/40 host assertions.
- **R6-P26 COMPLETE/POSITIVE offline:** three-class comparison unanswered mailbox / local retained service / genuine 31-page rejoin, 55/55 checks. Poll, generic answer or W4 alone cannot automatically authorize TX.
- **R6-P27 COMPLETE/POSITIVE offline:** local historical S10C service release yielded 07D0 but analogous S11H yielded 0884; already completed local S11I and S11W bounded ACK0884 then yielded 07D0 at ~2.042s and ~2.039s. Historical local log descriptions compared, not newly raw CRC replayed; 54/54 host checks. Universal successor rule NEGATIVE, owner still unknown.
- **R6-P28 COMPLETE/POSITIVE offline:** Connect source + seven genuine captures, 25,031 valid ADUs, 392 mailbox polls / 367 paired replies, 62/62 checks. W2/W3 and W4 represent gateway-side settings/runtime refresh/request bookkeeping, not a unique controller pending-work ID. W4=0000 can precede differing runtime pages; exclusive W4/W5 next-owner claim NEGATIVE. No independent controller epoch ID found in examined sources.

**Historically locally proven:** manually qualified fresh native handshake, 32/32 bootstrap (S9J–S10A, S11F), retained service context S10C/S11H, 0884→07D0 S11I/S11W, retained 07D0→07E4 S11X FIX1. None of these automatically establishes an owner after ESP OTA. Genuine Online/DCM captures remain cross-model. An FC16 address/count ACK is not semantic write acceptance.

**Native authority CURRENT:** physical controller epoch UNKNOWN, outstanding work owner UNPROVEN, auto FC23 response / FC16 ACK / 0708 answer / semantic write DENY. Preserve RX-only ESPHome and production HA entities. No new live YAML, TX or heat-pump restart performed by R6-P25–P29. Prioritize useful read-only HA mapping in parallel with evidence-driven native Online integration. Historical documentation retained verbatim below.

---

# 2026-10-11 R6-P24 — PREPARED / NOT RUN / NOT FLASHED (latest status)

R6-P24 passive controller-start witness was now prepared against live Bridge15C, preserving all existing production/bus-health and all TX locks. Two metadata-only globals, two diagnostic text sensors and two additive RX observation hooks; **125 added, 0 existing lines changed**. Source SHA256 c08b8fa6afc437b59730e457703d50bf9c2957593a80c12a9e9ace60999df8bb (baseline Bridge15C SHA256 9d2be8d2d8411ae7a1394cc93d086658d1d1f93f2db87e1d920fe3d8adace76b). YAML parsed offline; extracted actual C++17 gap/observer/sensor lambdas compiled and passed **37/37** host checks. **No full ESPHome compile, no OTA, no live execution.** Physical controller epoch UNKNOWN, owner UNPROVEN, auto TX/ACK/write DENY. No heat-pump restart requested. Prepared private report: Thermia_Connect_Firmware/findings/R6_P24_PASSIVE_CONTROLLER_START_WITNESS_PREPARED_20261011.md. Existing historical experiment details below unchanged.

---

# 2026-10-11 NEWEST — R6-P18–P23 offline reconciled; R6-P24 next (NOT RUN)

**Live baseline:** Bridge15C RX-only on XTR M (two 10 Oct logs totalling approximately 7m38s). Native 04A6/13 and 085F/5 received. Four targeted H021 pages 03E8/14, 042E/15, 0442/13, 0546/20 each rx=0 even while heat pump was actively heating. Latest V5 3943 valid; observed CRC/resync/drops/geometry and B11C/B11D differences zero; physical TX=0, DE LOW. Bridge15C is RUNNING/PARTIAL: absent-page diagnosis positive, positive four-page reception and expiry NOT RUN. Previous longer-term B11D raw framing failures remain open.

**R6-P18:** COMPLETE/POSITIVE offline for partial order in 6 genuine cross-model starts from 19,893 CRC-valid frames. 085F ACK and 06F4 ACK precede 07D0 in all six, but relative ordering varies. COMPLETE/NEGATIVE universal instant linear sequence; INCONCLUSIVE causality, owner, semantic acceptance.
**R6-P19:** COMPLETE/POSITIVE offline for 3 early 085F-before-handshake paths and 3 later 085F-after-06F4 plus answered-0708 paths; 28/28 host checks. In genuine traces ACK07D0→07E4 was approximately 2.130–2.256s, consistent with local EXP271 2.159s. Universal strict order NEGATIVE, owner unknown.
**R6-P20:** COMPLETE/POSITIVE offline frame-based route observer: 3 early/3 late/3 unknown genuine segments and documentary local 2 late/8 unknown cases. 65/65 host tests. Routes only classified by/after first 07D0, never transmission authority.
**R6-P21:** COMPLETE/POSITIVE offline prefix analysis (28/28 checks). ACK-history gives a pre-07D0 route prefix in the six in-sample starts; repeated identical controller-origin 085F zero requests cannot discriminate route (NEGATIVE). No out-of-sample proof.
**R6-P22:** COMPLETE/POSITIVE offline controller-origin pre-first-gateway-reply audit (30/30 checks): first 04BA and 085F patterns in seven genuine powercycle segments, including gateway-absent control, do not identify an owner; 192 first 0x0F request shapes matched in one present/absent contrast. FC23 words can change within one start; no proven boot-ID.
**R6-P23:** COMPLETE/POSITIVE offline rediscovery of *historically executed local* EXP355 controlled controller restart with ESP powered: sustained bus silence, controller 0x02 A80E=0000/A80F=0005 after return, 32/32 bootstrap, recovered runtime. Original EXP355 raw log NOT newly re-parsed; 28/28 host tests. NEGATIVE for ESP boot-id, bus silence or A80F=0005 alone being unique controller epoch/work-item-ID. Autonomous hot-rejoin and unique device-generation ID remain INCONCLUSIVE. EXP94/95 separately corroborate boot-status progression.

**NEXT R6-P24 PREPARED / NOT RUN:** prepare a strictly passive ESPHome controller-start witness against Bridge15C, retaining production entities, all existing counters and RX-only lock. Observation only: ESP boot, inter-callback silence/return, controller A80E/A80F, first native startup frames, health/gap provenance. Never promote physical epoch/owner or authorize FC23 response/FC16 ACK/write from passive evidence. No controller reboot or flash approved in this reconciliation.

**Current authority:** controller physical epoch UNKNOWN; native owner UNPROVEN; auto TX/ACK/write DENY. Existing R6-P10 FIX1 first-fault positive trigger untested. Source details in private Thermia_Connect_Firmware findings/R6_P18_P23_OFFLINE_NATIVE_SESSION_SYNTHESIS_20261011.md. Historical records preserved below.

---

# 2026-10-10 LATEST — R6-P17 completed offline; R6-P18 NEXT (NOT RUN)

**R6-P17 COMPLETE / POSITIVE** offline for cross-model FC23-response/FC16-ACK/runtime sequencing; **COMPLETE / NEGATIVE** for fixed immediate FC23-to-085F-to-runtime linear handshake; **COMPLETE / INCONCLUSIVE** for semantic acceptance or XTR applicability. Sep26+Sep28 genuine Eco5 traces rechecked: 19,893/19,893 CRC-valid. Six post-restart phases with captured FC23 response later show 0x03E8 requests/ACKs and 0x07D0 runtime, and all six show an 0x085F FC16 geometry ACK before first 0x07D0. Three 085F ACKs precede FC23 response and three follow it; first 03E8 ACK in four phases after ~0.12–0.14s and two phases after >108s. Gateway-absent Sep26 phase: 41 FC23 requests, 0 responses, 82 085F requests, no 0x0F FC16 ACK, no 03E8 or 07D0. Gateway presence confounds attribution; FC16 ACK alone is not semantic acceptance.

**R6-P16 COMPLETE / POSITIVE:** revises/supersedes causal INTERPRETATION of R6-P14/P15 apparent long FC23 pauses: original collaborator documents Sep26 A/B/A power cycles (gateway on/off/on) and Sep28 four power cycles with gateway present. Three and four >5s all-address capture gaps respectively. All five >5.1s FC23 gaps cross those boundaries; 156/156 within-restart-segment FC23 intervals lie 3.8–4.7s. Six response-bearing startup segments stop observed FC23 requests after first reply; response-free Sep26 segment continues 41 requests. Sniffer records CRC-valid frames with software receive timestamps, not independent proof of wire silence or loss-free logging. Power cycle boundary ≠ proven capture loss. Preserve R6-P14/P15 raw observations but their suggestion of continuous-session FC23 cessation is SUPERSEDED.

**R6-P14:** COMPLETE / POSITIVE offline for detecting five >5.1s cross-boundary FC23 gaps; original interpretation of in-session heartbeat pauses SUPERSEDED. **R6-P15:** COMPLETE / POSITIVE for all-address gap assessment, INCONCLUSIVE standalone cause; refined by R6-P16 documented deliberate restarts.

**R6-P10 FIX1 RUNNING / PARTIAL:** on-device HA snapshot entity present but NONE in three user logs; independent B11D frames >6000 and fault=0 while V5/B11C advance; early one V5 resync followed by observer recovery, no further drops/resync, TX/DE=0. First real sticky B11D fault after FIX1 NOT captured, so latch behavior untested. Native controller power epoch and owner UNKNOWN, native automatic TX/ACK/write DENY.

**NEXT R6-P18 OFFLINE / NOT RUN:** analyze page 0x06F4, 0x085F ACK ordering and 0x07D0 first runtime across six cross-model startup phases, with gateway absent control explicitly confounded. No YAML, TX or controller action.

---

# 2026-10-10 LATEST — R6-P11/P12/P13 OFFLINE, R6-P10 FIX1 LIVE
R6-P13 COMPLETE / POSITIVE offline repeated cadence; COMPLETE / NEGATIVE universal mandatory 085F->FC23->04A6 triplet; COMPLETE / INCONCLUSIVE actual scheduler/semantic acceptance/XTR applicability. On genuine Eco5 Sep26/Sep28 DCM captures: 0x0F FC23 requests 99/64, FC16 085F count 197/122, FC16 04A6 count 357/226. Median recurrence periods respectively FC23 4.2335/4.241s; 085F 2.1245/2.131s; 04A6 1.383/1.411s. FC23 had preceding 085F and later 04A6 within 10s in 96/99 and 58/64 cases, but independent 085F-to-next-04A6 matched control medians 1.451/1.4555s, close to FC23-containing combined medians 1.473/1.4915s. Periodic overlapping work likely; causal handshake unproven.
R6-P12 COMPLETE / POSITIVE offline: 164 genuine cross-model FC23 0x0F requests and 7 recorded immediate responses. Fixed geometry read 0x0730 count8, write 0x071C count8; seven 21-byte responses, recorded gaps 29–63ms; 157 requests have no observed paired response, NOT proof of rejection. FC23 recurs ~4.2s on two long captures. THESE ARE NOT LOCAL XTR WRITE TARGETS OR TX AUTHORITY.
R6-P11 COMPLETE / POSITIVE offline: seven cross-model captures, 25,031 CRC-valid ADUs in prior replay; recording-window start does not establish controller boot, and visible configuration/runtime order differs.
R6-P10 FIX1 RUNNING / PARTIAL (actual live): user logs ~19:16 to 19:28 show First Fault Snapshot sensor active but NONE; B11D >6000 independent frames without new raw fault, V5/B11C progressing, no TX/DE. V5 had one early resync (+1) with passive observer recovery, later no additional resync/drops; session UNQUALIFIED/FAULT_LATCHED/NO_TX. First-fault snapshot capture not exercised; remain partial. Native owner/physical epoch UNKNOWN, TX/ACK/write DENY.
Next R6-P14 possible offline phase-gap analysis; no new live experiment needed.
---
2026-10-10 CURRENT UPDATE: R6-P10 live COMPLETE / POSITIVE for recurring independent B11D sticky RAW_NO_VALID_CRC_CANDIDATE_AT_IDLE; COMPLETE / NEGATIVE for long-run independent raw framing; COMPLETE / INCONCLUSIVE for actual first-fault V5.has_pending/cause. At 18:57 B11D frozen at 4269 frames and 1746 batches, incomplete=1/fault=1; V5 and B11C continue past 16000 frames, resync/drops=0, TX/DE=0. First-fault onset occurred outside provided log. R6-P7/P8/P9 OFFLINE analyses concluded: R6-P1 32 raw minus 25 processed = 7 residual (12/12 tests); synthetic 25ms split framing reproduces premature sticky failure (12/12 tests); one candidate length180 with 7 remainder bytes is FC23-shaped under source implementation (13/13 tests), NOT proven real FC23. R6-P10 static post-fault audit COMPLETE / POSITIVE: first fault diagnostic only written once to logger, not HA. NEXT R6-P10 FIX1 PREPARED / NOT RUN: one latched bounded first-fault snapshot in HA; YAML parsed, IDs/diff checked; no ESPHome compile/flash/live test. Native owner and epoch UNKNOWN; TX denied.

---

# 2026-10-10 — CURRENT STATE: R6-P6 FIX1 PREPARED / NOT RUN (newer than historical R6 concept note)

**Latest live XTR M experiment:** R6-P5 COMPLETE / POSITIVE for bounded RX-only classifier integration; COMPLETE / INCONCLUSIVE for native runtime-node exercise. User log 16:31:00–16:34:03: V5 1,626 valid frames and 266 known 0x0F FC16 pages; geometry/unknown/resync/drops 0; Bridge11C differences 0; B11D raw frames 1,621 with no fault during this brief run; physical TX 0, DE LOW. Classifier remained UNQUALIFIED / NO_TX, reason ESP_BOOT_UNQUALIFIED, observed node NONE because only 085F/5 service and 04A6/13 configuration appeared. Controller epoch UNKNOWN, owner UNQUALIFIED, TX/ACK/write DENY.

**R6-P1 long-run observation:** COMPLETE / POSITIVE for actual first-fault metadata, COMPLETE / NEGATIVE for independent B11D long-run continuity. At 16:26:44.824, RAW_NO_VALID_CRC_CANDIDATE_AT_IDLE: batch=6406, raw=32 bytes, cursor=25, 7 remaining, calculated candidate length 180, 1 needs-more candidate and 0 valid remainder CRC. V5 and V5-delimited Bridge11C continued safely while independent B11D froze; root cause unknown. Do NOT rely on stale zero-difference counters after B11D fault. Supersedes old note stating first-fault onset unavailable for a DIFFERENT, earlier log only.

**Offline R6 milestones:** P2 historical retained-runtime comparison COMPLETE / POSITIVE for reconstruction but inconclusive for independent epoch/owner. P3 reconstructed event classifier 10/10 offline scenarios. P4 seven genuine Eco5/ATEC cross-model captures: 25,031 CRC-valid raw frames, 794 runtime-shaped requests rejected as local XTR authority, zero TX. P6 offline audit 15 scenario tests and 25,031 cross-model replay: latched fault reason could be overwritten on FC23; STALE reason could diverge. Cross-model replay and Python behavioral simulations are not locally proven XTR runtime.

**NEXT: R6-P6 FIX1 PREPARED / NOT RUN.** Exactly two passive classifier diagnostic fixes (preserve latched fault reason on FC23; align STALE reason with state) in full production-preserving ESPHome YAML. Offline YAML parse and 8 behavior tests reported PASS; no user-confirmed compile, flash or live result. Preserve known-good R6-P5 and TX-deny. Abort if unexpected TX/DE, V5 resync/drops/geometry or production sensor regressions; rollback R6-P5 firmware, no controller reboot. Last completed LIVE experiment is R6-P5, not R5 FIX2.

---

# 2026-10-10 — CURRENT STATE: B11D independent raw RX fault / original-C++ offline integration reconciled

**Newest supplied local XTR M evidence:** [LIVE_B11D_RX_VALIDATION_20261010.md](LIVE_B11D_RX_VALIDATION_20261010.md) — supplied passive ESPHome log 15:04:31–15:08:43. **LIVE-B11D-RX-VALIDATION-01 RUNNING / PARTIAL** for planned duration and first-fault-onset investigation; **bounded COMPLETE / NEGATIVE** for independent B11D raw stream continuation. No new firmware, RX/TX hardware action or controller reboot during this documentation reconciliation.

**Current physical controller epoch: UNKNOWN. Pending native work owner: UNQUALIFIED. TX/ACK/write: DENY.** No new automatic takeover or semantic write acceptance is proven.

**Latest bounded local findings:**
- V5 Valid Frame Count **151,615 → 153,659** (+2,044), V5 geometry/resync/drops zero. B11C original portable using V5-delimited frames **151,818 → 153,604** (+1,786), count/byte differences zero and zero recorded TX; **NOT independent raw framing**.
- Independent B11D rawFrames=portableFrames=comparedV5 **56,714, frozen** while callbacks +5,377, received bytes +38,429; sticky fault=1/incomplete=1 and first-fault class **RAW_NO_VALID_CRC_CANDIDATE_AT_IDLE**, already present at the beginning of the supplied log. No valid new independent raw frames, no fresh parity after this fault; displayed countDiff/byteDiff=0 are stale snapshots.
- B11D physical output counters ioTx=0, DE=0, native owner UNKNOWN. The fault onset and raw bytes preceding it are **NOT CAPTURED**; no causal claim about UART/25-ms timing may be made.
- The supplied observation is **~4m12s**, not the requested 20–30 min; do not mark the duration experiment complete.

**Offline original-source host evidence now reconciled (NOT hardware proof):**
- Metadata-only NATIVE-OBSERVER-06: 4,809 native cross-model events, correlations 374 FC03 / 1,324 FC16 / 7 FC23.
- Bridge07: original pinned C++ host + 4,809 synthetically rebuilt CRC-valid frames, no TX; full real original source replay not run yet at that stage.
- Bridge08: **25,031 genuine cross-model raw ADUs through original pinned C++ RX bridge and observer**, GCC/Clang/sanitizers PASS; [private CI 38051370371](https://github.com/ryckema/Thermia_Connect_Firmware/actions/runs/38051370371).
- Bridge09: **25,031 genuine frames × 3 synthetically timed UART callback fragmentation/coalescing models** through raw framer → original C++ → observer; 75,093 frame-occurrences per compiler build, GCC/Clang/sanitizers PASS, no host TX; [private CI 38053859261](https://github.com/ryckema/Thermia_Connect_Firmware/actions/runs/38053859261).
- These host tests **do not establish** on-device ESP32 scheduler behaviour, true Modbus t3.5, native controller power epoch, ownership or write authority.

**Last completed locally controlled active experiment remains R5 FIX2**, as documented below; the planned third phase was NOT RUN. **R6 remains CONCEPT / NOT PREPARED / NOT RUN.** The older S11 and native rebuild branches stay separate. Do not reinterpret the new passive log as a fresh handshake or completed active experiment.

**Next:** seek log covering the FIRST B11D fault transition (about 20–30 s before), including scheduling/heap/loop details if available; otherwise separately prepare an **ESP-only, RX-only startup observation** preserving known-good production configuration, with no Thermia controller power-cycle, no active bus responses, and fail-closed handling. Not performed yet. Abort further live testing on V5 health regressions or any unexpected TX/DE.

---

# 2026-10-10 — Native session/epoch offline reconciliation + EPOCH-WITNESS-02 (NO LIVE CHANGE)

**Historical evidence reconciliation (2026-10-10):** de genuine cross-model RTC-cluster `0858–085E` was **al gedocumenteerd op 2026-10-05** in `Thermia_Connect_Firmware/findings/CM930_UNMAPPED_PATTERN_CLASSIFICATION.md`. De nieuwe bijdrage van OFFLINE-EPOCH-WITNESS-02 is de onafhankelijke woord-/tijdcontrole tegen de firmware-klok `06EA–06F0` plus de classificatie als **ongeschikt zelfstandig controller-epoch-bewijs**. De bestaande firmwarefinding blijft prioritaire eerdere ontdekking; lokaal XTR-bewijs ontbreekt.

**Current physical controller epoch/owner: UNKNOWN / UNQUALIFIED. Auto-TX/ACK: DENY.** This is an **offline research update**, not a new bus experiment or a claim that a controller reset was witnessed. The deployed Bridge 11C Public RX-shadow is unchanged; its observed bounded CRC subtest was positive (1,546/1,546 checked V5-delimited frames, zero CRC mismatches, no observed TX/DE), but it does **not** establish independent portable RTU framing or native session ownership. Do not extrapolate from the last submitted log to the device's present physical state.

**Last completed local live branch:** R5 FIX2 — COMPLETE / POSITIVE for the bounded 0870/17 word-capture objective, COMPLETE / INCONCLUSIVE for the planned three-stage 0864 gate (P3 NOT RUN; controller epoch unknown). Keep S11Y-AL FIX1, FIX8K and the separate formal native rebuild branch distinct. **R6: CONCEPT / NOT PREPARED / NOT RUN.** No subsequent active experiment is authorized by this update.

**Offline studies closed 2026-10-10 (do not count as controller experiments):**
- NATIVE-SESSION-MVP matrix and timestamp reconciliation — COMPLETE / POSITIVE for source/time-order reconstruction; COMPLETE / INCONCLUSIVE for a universal, unattended runtime owner or ACK policy. S11F's later runtime page followed an ACK **and** another service reply: ACK-alone sufficiency is unresolved. S11W→S11X showed recurring 07D0/19 through ESP firmware changes, but content changed across the first boundary; S11X original→FIX1 retained matching content, followed by a manually qualified one-ACK progression. ESP OTA is not proof of controller power-epoch continuity.
- NATIVE-SESSION-EPOCH-CONTINUITY audit — COMPLETE / POSITIVE for classifying observed ESP restart boundaries and excluding inadequate witnesses; COMPLETE / INCONCLUSIVE for controller boot identity. No independent controller uptime/resetcounter or synchronized power-event marker was established.
- OFFLINE-EPOCH-WITNESS-02 — COMPLETE / POSITIVE for a seven-file, **cross-model reference** audit (2,500 complete slave-0x0F FC16 frames with valid CRC) and for identifying a **calendar-clock mirror** at 0858–085E in genuine reference captures; COMPLETE / INCONCLUSIVE for a unique, locally proven XTR M controller-epoch witness. Connect firmware semantically labels 06EA–06F0 as date/time; the 0858–085E mirror mapping is derived from reference words and **NOT locally proven on this XTR M**. RTC values, defrost counters, compressor hours and monotone short windows cannot authorize TX or prove reset identity.

**Strongest remaining blocker:** differentiate the ESP restart from an independently verified controller-epoch change, then prove pending runtime work ownership inside that epoch. Address/count, successful CRC, payload repetition, a valid RTC, and a standard FC16 ACK are individually insufficient.

**Next action (offline, read-only):** search existing **local XTR** captures for complete 0848/count23 words W16–W22 (0858–085E) and 06EA/count7 time data, especially near any already documented controller reset. If unavailable, prepare a separately reviewed RX-only observer without changing known-good production entities; **do not flash or run it without a new request**. Do not propose a new write, mailbox response or active ACK stage from these results.

**Provenance:** local S11F/G/H/W/X experiment logs and canonical R5 FIX2 record versus genuine cross-model Online/DCM reference captures and Connect firmware 2.0.18/2.1.105 profile semantics. Detailed private evidence: `ryckema/Thermia_Connect_Firmware/findings/NATIVE_SESSION_MVP_TIMESTAMP_RECONSTRUCTION_20261010.md`, `NATIVE_SESSION_EPOCH_CONTINUITY_AUDIT_20261010.md`, and `OFFLINE_EPOCH_WITNESS_02_RESULT_20261010.md`. Keep cross-model and firmware-derived interpretation separate from PROVEN/local XTR evidence.

---

# 2026-10-09 — Native Online/DCM MVP focus and CM930 source-diff reconciliation (OFFLINE ONLY)

**Primary goal:** reproduce a safe native Thermia Online/Connect/DCM ESP32/ESPHome session on local XTR M for stable HA reads and eventually validated desired-value writes. Stop diverting into W4 minutiae unless needed for a specific blocker.

**Most recent locally completed live branch:** V5-S8-R5 FIX2 COMPLETE / POSITIVE for full passive 0870/17 words, COMPLETE / INCONCLUSIVE for the intended three-stage 085F→0864→0870 continuation (P3 never ran). One bounded P1 mailbox response plus one bounded P2 ACK085F were delivered; first 0870 arrived after 2.089s without a newly observed 0864. Controller epoch UNKNOWN; READY=0; reported aggregate HEALTH TX 1/1/1 conflicts with separately evidenced two transmissions. S11F qualified 32/32 bootstrap and 0884 progression is a separate controller epoch confounded by additional mailbox traffic. **R6 CONCEPT / NOT PREPARED / NOT RUN.**

**Separate status:** S11Y-AL FIX1 latest local S11Y passive observer COMPLETE / POSITIVE only for clean zero-TX observation, INCONCLUSIVE for owner/session transition and heating correlation. FIX8K semantic correlation RUNNING / PARTIAL. Formal native rebuild S8 NOT RUN. Do not merge experiment lines or infer current physical owner from prior captures.

**2026-10-09 source audit — COMPLETE / POSITIVE OFFLINE only:** original Connect 2.0.18 appfs device_client sources (user supplied) were compared with recovered 2.1.105 device_client. Five CM930 handlers examined: on_registers_request_event, _request_operation_data, on_handshake_state_changed_event, _on_successfull_onboarding, on_registers_received_event. The reviewed handlers are functionally unchanged (four textually equal and one formatting-only difference in earlier comparison). Both releases clear W2/W3/W4 on application processing of corresponding FC16; 2.1.105 adds CMClientParameterUpdateState completeness notification. Read-all seeds W4=06FF (bit8 excluded). Internal _request_info_data and _request_operation_data produce targeted register sets; no autonomous periodic read-all/W4 refresh producer found in either examined device_client tree. This disproves the narrow theory that Connect 2.0.18 lacked self-clearing selectors, but does NOT determine legacy genuine DCM03 application behavior. Genuine ATEC W4=07FF once, then 077F 64 times remains CROSS-MODEL CAPTURE evidence, not a timer/ACK permission rule. See Thermia_Connect_Firmware findings/CONNECT_2.0.18_VS_2.1.105_PROTOCOL_DIFF.md and findings/CM930_SOFTWARE_ARCHITECTURE.md. Do not publish confidential emulation or security implementation.

**Five integration gaps:**
- HANDSHAKE: locally reproduced in qualified sessions; automatic fresh/rejoin ownership and restart recovery unproven.
- BOOTSTRAP: 32/32 reached in S11F; unattended repeatable acquisition across arbitrary epochs unproven.
- RUNTIME: bounded locally proven context-specific edges; no globally qualified automatic owner/ACK policy (especially 085F H011 and 0864/0870/0884 branches). FC16 ACK is not semantic acceptance.
- READS: preserve known-good ESPHome/HA production entities and bus-health counters; native feed not yet a validated unattended production source.
- WRITES: firmware-derived desired/read-back route exists but no validated production-safe semantic XTR setting change follows from a transport ACK.

**Next: NATIVE-SESSION-MVP — OFFLINE / PROPOSED / NOT RUN.** Reconcile existing S11F/S11W/S11X/R5 and genuine captures into a compact evidence-linked state-transition/authorization matrix: locally proven same-epoch edges; manually demonstrated non-generalizable edges; and CAPTURE-ONLY unknowns. Positive: independently justified exact owner/epoch/health guards; negative: captured counterexample rules out a proposed generalization; inconclusive: missing raw/epoch/ACK provenance. No TX/YAML/controller recovery in this offline task. Only then select the first actual blocker; any later active bus action needs separate authorization and fail-closed manual boundaries.

**Safety:** preserve production functions and health bookkeeping; unexpected traffic capture-only, zero unsolicited TX; no unqualified ACK, unknown writes, controller reset, room-sensor disconnection or tests needing a genuine DCM. No experiment is advanced by document edits.

---
# 2026-10-09 — V5-S8-R5 FIX2 closeout (separate retained/rejoin branch; latest supplied local log)

**Current evidence:** **V5-S8-R5 FIX2 COMPLETE / POSITIVE** for the *passive full 17-word 0870/17 capture objective*, and **COMPLETE / INCONCLUSIVE** for reproducing the originally planned three-stage 085F→0864→0870 path (P3 was never run). Source: user-supplied ESPHome log `Pasted text(20261009-095219).txt`, boot `D7726116`, 11:50:31–11:51:58 on 2026-10-09. This is **not** S11Y-AL or a new qualified fresh-session epoch; the software reports `UNKNOWN_CONTROLLER_EPOCH` / `MANUAL_ZERO_085F_REJOIN_EPOCH_UNKNOWN`; session label `BASE_RING_OBSERVED_ONLY`; READY=0.

**Last locally completed test in this branch:** R5 FIX2. P1 manually armed 11:50:59.405 and delivered one bounded reply by 11:50:59.628; P2 armed 11:51:05.420 and delivered one FC16 address/count ACK for exact 085F/5 at 11:51:06.663. **First 0870/17 arrived 11:51:08.752, 2.089 s after P2**, without 0864 publication or P3 ACK during this run. At least 24 full 0870/17 receptions logged through 11:51:58; captured payload baseline (W00–W16): `0519 0000 021D 0291 0000 0000 005E 0000 0000 0000 0000 0000 0000 FD20 0000 0000 0000`. At reception #12, words at 0871,0874,0875,087E,087F,0880 briefly changed `0000→0100`, returning on next reception. **Meaning OPEN / UNKNOWN**; no raw standalone wire+CRC copy for this occurrence.

**Bus health:** parser geometry/unknown/resync/drops/boundary all zero in sampled log; DE low; P3 0864 captures=0, P3 TX=0; P1 and P2 each show one delivered transmission. One `[S8] HEALTH` aggregate TX triplet shows `1/1/1` while independent UART write / delivered counters show **2** after P2; treat this as a bookkeeping discrepancy, NOT proof of only one physical TX. No unsolicited additional TX evidenced in this record.

**Protocol model update:** In this *retained/rejoin unknown-controller-epoch* context, `0870/17` appeared directly after bounded P1/P2; 0864 is **not a universal immediate predecessor** for 0870. Do not transfer this result to the qualified fresh S11D/S11F path, where 0864 was observed. S11F reached 0884 after qualified ACK0870 **plus** a further mailbox response (causal confounder); ACK0870-alone sufficiency remains unproven.

**Next action:** R6 **CONCEPT / NOT PREPARED / NOT RUN**. Offline check R5 FIX2 0870 words and variant against genuine gateway and firmware evidence; qualify active session ownership/same-epoch gates before any new ACK0870/17. Prefer passive evidence; no TX or new controller action authorized by this closeout. Abort any proposed active test on unknown owner, unexpected frame/payload, parser fault, DE fault, or extra TX. Preserve existing production ESPHome behavior. Historical S11Y-AL remains the most recent result in its **separate S11Y experiment line**; no result superseded by this addendum.

---

## 2026-10-09 — Heating-context clarification after S11Y-AL FIX1 (no new experiment)

**User observation:** heat pump was heating when asked *after* the S11Y-AL FIX1 passive capture; user cannot confirm whether heating was already active during 01:38–01:47. Existing `0662/33` observed with stable signature `EEEA4167` and `085F/5` W2=`0800` does **not** itself date or prove heating onset. Full `0662` words were not dumped, and currently available operation/heating anchors are `NaN` (unavailable, not false). Do **not** infer a heating-state bit or causality from this signature. Next **OFFLINE / NOT RUN** action: check existing timestamp-aligned production telemetry or documented register mapping against the capture interval; if none, declare heating-at-capture UNKNOWN and request the smallest synchronized evidence. No new TX, ACK, control action, controller reset or assumed controller epoch. S11Y-AL FIX1 remains COMPLETE/POSITIVE for healthy passive logging and COMPLETE/INCONCLUSIVE for heating correlation, owner or transition. No new live experiment was performed.

---

# 2026-10-09 — Canonical update: S11Y-AI–AL FIX1 (latest)

**Latest live result:** **S11Y-AL FIX1 COMPLETE / POSITIVE** for a passive, healthy zero-transmission observation on the local Thermia iTec XTR M; **COMPLETE / INCONCLUSIVE** for any native session transition, ACK-owner predicate or runtime-controller causality. Two overlapping ESPHome logs `Pasted text(20261008-233905).txt` and `thermia-exp86-20261009-013844.log` carry one ESP boot `F59E0699`, segment 0; log continued until **01:47:16** (t_ms ~532530, ~8m53 from boot). The second filename does **not** make this a new EXP86: the experiment is S11Y-AL FIX1. Last full HEALTH at **01:46:54.738**: `valid=4441 seen085F=242 polls=0 observed_responses=0 peerACK=0 resync=0 drops=0 mismatch=0 boundary=0 unknown=0 tx=0/0/0 de=0 invalid=0 controller_epoch=UNKNOWN CAPTURE_ONLY boot=F59E0699`. At the end, `NSH J 085F Captures=253`. Observed repeated FC16 `0662/33` signature `EEEA4167` (~1.06 s average interval) and `085F/5` `0000 0000 0800 0000 0000` signature `7EAE5A0A` (~2.1 s), no `0708` polls, no observed answers, no native runtime continuation and no new FC23 in this sample. The full 0662 payload was **not** logged; signature stability does not establish heating semantics.

**Heating:** user reported that the heat pump **was heating when asked after the log**, but whether it was heating during **01:38–01:47** is **UNKNOWN**. Do not reinterpret `NaN` operation/heating anchors as absence of heating; the needed semantic page data were unavailable. Do not infer that 0662 caused/indicated heating without a synchronized operational source.

**Most recent offline source work:** S11Y-AI COMPLETE/POSITIVE original S7, S11V FIX1 and S11Y-M FIX1 ESPHome logs recovered and event order compared (no independent local raw RS485 frames); S11Y-AJ COMPLETE/POSITIVE offline source-profile audit; S11Y-AK COMPLETE/POSITIVE source recovery and comparison: original S7 and S11V FIX1 YAML both declare FC03 `0708/count6` response W0–W4=`0000`, W5=`0006`, while S11Y-M FIX1 declares all six words `0000`. S7 `0708 response → ACK085F → 0870/17` and S11V `0708 response → guarded all-zero ACK085F → 0884/60` occur in separate controller epochs; W5 alone cannot select branch. S7 did not log exact pre-ACK five 085F words. S11V guarded five-zero state but independent pre-ACK word dump remains absent. S11Y-M: `0708 response → 085F W2 0800→0000` without ACK and no new owner in window. S11Y-AL observation specification COMPLETE/POSITIVE offline; FIX1 YAML prepared and **now actually executed as passive observation**, not as active responder. Offline analysis does not authorize ACK.

**Current safety/state:** actual current controller epoch UNKNOWN; locally transmitted responses remain **CAPTURE_ONLY/NOT AUTHORIZED**. S11Y-AA active experiment PREPARED / NOT RUN; FIX8K RUNNING / PARTIAL; formal native rebuild S8 NOT RUN (S7 last formally completed). Preserve working HA production entities/health bookkeeping. No semantic writes, broad scans, speculative ACKs or DCM hardware. **Next:** correlate operational heating status only from independent synchronized telemetry or existing captures, and assess already captured 0662/085F vs historical 0708/085F offline; consider a strictly passive follow-up only if a specific missing observable is identified. 

---

# 2026-10-09 — Current offline research through S11Y-AH (supersedes earlier next-action headings)

**Last completed work:** **S11Y-AH COMPLETE / POSITIVE for OFFLINE classifier fusion (65/65 checks)**; **INCONCLUSIVE for unique current XTR controller-owner / automatic ACK permission.** Prior sequential offline results: **AE 20/20**, **AF 44/44**, **AG 86/86** (all COMPLETE/POSITIVE *only for offline research*; precise controller priority remains unknown). **No new live ESP bus TX, compile, controller reset or semantic write.**

**Last *observed* local XTR epoch (S11Y-AA, Oct 8 ~23:09–23:15):** FC16 `085F/count5` with W2=`0800` and repeated FC03 `0708/count6` **polls**; `0662=0`, ESP TX=0. AA ARM was refused at 23:15:21.637. **S11Y-AA active test PREPARED / NOT RUN; ARM attempt COMPLETE / INCONCLUSIVE.** Actual current physical controller state after these logs **UNKNOWN**, never infer it from historic epochs. FIX8K semantic correlation **RUNNING / PARTIAL**. Separate formal rebuild: last S7 COMPLETE/POSITIVE, **S8 NOT RUN**.

**Updated protocol model:** three genuine Eco5/ATEC Online/DCM captures: 111 acknowledged `07D0`-anchored candidate intervals; **47** strict complete cycles on `07D0 → 07E4 → 07F8 → 080C → 0820 → 0834 → 0848 → 0864 → 0870`, **64** unqualified. Overlay: `085F` and `0884` optional/context-dependent; 321 genuine `085F` requests/10 ACK (314 after `04BA`, 4 after `06F4`, 3 after `0848`); 13 `0884` requests after `0870`. These are **CROSS-MODEL capture observations, not locally proven XTR scheduler priorities**. Actually answered W4=`0100` can precede `07D0` rather than `0864`; W4 is not an exclusive FIFO or TX token.

**Current diagnostic result for AA:** `BASE_RING=UNKNOWN_REJOIN`; `SERVICE_PENDING=RETAINED_085F0800_WITH_POLL_ONLY_W4_UNKNOWN`; `PROVENANCE=UNKNOWN`; `last answered 0708 W4=UNAVAILABLE`. An unanswered *poll* cannot establish W4. **CAPTURE_ONLY; no ACK/mailbox/write authorisation**. Cross-ESP-OTA owner provenance is never inherited.

**Next candidate: S11Y-AI OFFLINE / NOT RUN.** Reconcile original local S7, S11V and S11Y-M same-run raw event order where available. Positive = timestamped predecessor/actually answered `0708`/subsequent `085F` relation; negative = counterexample to proposed stable ordering; inconclusive = missing raw files or epochs; abort = contradictory timestamps/CRC. No physical recovery required. No active experiment suggested from AH alone. Maintain production HA, health counters, fail-closed capture; no speculative TX, forced controller reset, DCM hardware, room-sensor disconnection or unverified semantic writes.

Full redacted offline dossier: [S11Y-AE–AH scheduler and rejoin evidence](protocol%20reduction/S11Y_AE_AH_OFFLINE_SCHEDULER_RECONCILIATION_20261009.md). Historical project state below remains intact.

---

## 2026-10-08 (additional independent evidence) — H012 five-second ACK feature is NOT an owner rule

Independent **H012 OFFLINE** analysis, committed separately in the firmware research repository, reconstructed the known genuine 321 all-zero `085F/5` requests (10 ACK/311 without matched ACK) with a CRC-validated seven-file replay. A **previous FC16 ACK within a retrospective five-second window** was seen before **9/10** acknowledged `085F` requests and **0/311** unanswered requests; **one genuine Eco5 2026-09-28 ACK is a counterexample**, so the feature is not necessary, nor proven sufficient for XTR owner authorization. Five seconds is **an analyst-defined window, not a vendor deadline**. First following FC16 pages in those 10 genuine examples were `07D0/19` (4), `03E8/14` (3), `0864/4` (2), and repeated `085F/5` (1), *temporal* successors, not causally proved ACK effects. H012: **COMPLETE / POSITIVE OFFLINE census and falsification; COMPLETE / INCONCLUSIVE for a transferable live ACK predicate**; 14/14 offline checks. This does not change S11Y-AA **PREPARED / NOT RUN**, AD's 9/9 limited offline classification, or the **CAPTURE_ONLY** policy.

# 2026-10-08 (late) — Native S11Y-AA/AB/AC/AD reconciliation (newest supplement)

**This section supersedes older "current experiment" headings below, without altering historical results.** Last locally observed state, supplied logs ~23:09–23:15: repeating slave `0x0F FC16 085F/count5` words `0000 0000 0800 0000 0000`, signature `7EAE5A0A`, plus `FC03 0708/count6`; `0662/count33` and `0864/count4` absent. This is not a claim about any later controller state.

## Current experiment / last results
- **S11Y-AA — PREPARED / NOT RUN as an active two-ACK experiment.** Actual ARM attempt at **23:15:21.637** was **COMPLETE / INCONCLUSIVE**: `NSH AA ARM REFUSED ... state=2 0662=0 085F=161 0708=80 tx=0/0/0 NO_TX`. It did not test an ACK to newly all-zero `085F` or an `0864` successor.
- **S11Y-Y FIX2 — COMPLETE / INCONCLUSIVE for intended two-ACK endpoint.** ACK1 of `0662/33` was delivered (`1/1/1`), following `085F` had all-zero signature `9BFE9A42`, later `0708` appeared. TX2 was refused by the obsolete `0800` signature guard; no `0864` appeared in the observed window. The first-stage transition is positive local evidence.
- **S11Y-AB — COMPLETE / POSITIVE OFFLINE comparison**, not a new bus test. Existing S11T/S11U/S10C evidence plus Connect 2.1.105 timeout review do not establish a controller timer forcing `0662` after ESP restart.
- **S11Y-AC — COMPLETE / POSITIVE OFFLINE genuine-corpus analysis**, not a live test. Across genuine Eco5/ATEC Online/DCM captures: 321 all-zero `085F/5` requests, only 10 ACKs. First subsequent work pages include both `0864` and `07D0` in differing cross-model contexts.
- **S11Y-AD — COMPLETE / POSITIVE OFFLINE classifier checks**, **9/9** (four existing XTR log fixtures, two observation-equivalent distinct predecessor histories, three fail-closed health cases). Implemented classifier covers selected documentary labels only; no on-device compile/CRC validation; **all classifications CAPTURE_ONLY**.
- Older **FIX8K — RUNNING / PARTIAL** semantic correlation remains uncompleted; no natural operation-mode markers were added. **Formal rebuild S8 remains NOT RUN** in the separate firmware-rebuild track.

## Protocol model, strongest conclusions and unknowns
- Locally established, *context-specific* edges: S11T `ACK0662 -> 0708`; S11U FIX1 `0708 reply -> all-zero 085F`; S11V FIX1 `ACK fresh zero 085F -> 0884`; S11W `ACK0884 -> 07D0`; S11X FIX1 `ACK07D0 -> 07E4`. S11B observed two ACKs (`0662`, `085F`) and later `0708`, `0864`.
- **S11B payload-attribution correction:** its all-zero `085F` log is emitted after TX2 in the same receive-event handling order; TX2 to **already all-zero** `085F` is STRONGLY SUPPORTED but not independently pre-TX word-proven. Older shorthand “S11B ACKed `085F(0800)`” is SUPERSEDED AS AN INTERPRETATION ONLY; preserve the original ACKs and follow-on observations.
- `085F(0800)+0708` occurs after multiple earlier work phases across ESP restarts, **not** proof of identical controller-internal owner/session state. Payload geometry, selector flags, or a prior different session are never sufficient TX authorization.
- Firmware-derived: `0861.bit11=0800` carries Online/gateway communication-error labels in applicable Connect profiles. **Not XTR UI-confirmed** and not proven to trigger the scheduler. Connect serial/application timeouts are not evidence of controller `0662` regeneration.
- UNKNOWN: exact retained H011 owner authorization; current internal epoch; why `085F` branches to `0884`, `07D0` or `0864`; generic hot-rejoin; semantic write acceptance.

## Next step / safety
**S11Y-AE candidate — OFFLINE / NOT RUN.** Compare existing raw XTR and genuine DCM predecessor timestamps, selector images, last observed mailbox answer and ESP restart boundaries; test for counterexamples before inferring pending-work priority. Positive: a reproducible context discriminator for differing next work pages; negative: counterexample disproves proposed rule; inconclusive: missing predecessor history. No bus recovery needed. No AA re-ARM without fresh `0662` baseline, no speculative ACKs, no new writes/resets, no room-sensor disconnection or DCM-dependent captures. Preserve production HA and fail-closed UART health accounting.

Redacted detailed report: [S11Y-AA..AD passive reconciliation](protocol%20reduction/S11Y_AA_AD_PASSIVE_SESSION_RECONCILIATION_20261008.md).

---

# 2026-10-08 — Passive FIX8H–FIX8K evidence and native-path roadmap (supplement to S11X FIX1)

## Current experiment / status
- **FIX8K — RUNNING / PARTIAL (semantic correlation deferred)**. Installed and locally run 2026-10-08; passive log `thermia-exp86-20261008-120937.log` shows repeated `0x0F FC16 07D0/count19` plus `FC03 0708/count6`; final observed summary `07D0=280 0708=140 changes=19 marks=0 tx=0/0/0 integrity=0 mismatch=0 unknown=0 resync=0 drops=0`. The 19 signature changes are attributable to `07DF` edge changes in this capture; no changes to `07D0`, `07D1` or `07E0` recorded. No heating/DHW/idle markers, because there was no naturally occurring demand. Do **not** mark the intended semantic correlation complete; resume only when such operation naturally occurs, without forcing heating/DHW.
- **FIX8J — COMPLETE / POSITIVE (passive timing)**. Eight full `07DF` cycles in the analysed recording, steady-state rise-to-rise ~64.66–64.78 s, on ~17.21–17.29 s, off ~47.44–47.55 s; passive UART TX=0 and clean parser. Later longer FIX8J recording confirmed continued periodic edges and clean parser. This proves periodicity, not meaning.
- **FIX8I — COMPLETE / POSITIVE (passive time correlation)**. `07D0/count19` dynamic words `07D0,07D1,07DF`, and cross-run change `07E0` observed; semantics remain unknown.
- **FIX8H — COMPLETE / POSITIVE (passive full-page capture)**. 130 `07D0/count19` frames and 65 `0708` polls in five minutes; 12 signatures including first, 11 recorded word deltas, no `085F/0884/0662`, no ESP TX, parser faults=0.
- **S11X FIX1 remains the most recent completed *active native-path experiment* — COMPLETE / POSITIVE**. The locally proven retained `07D0/count19` ACK -> `07E4/count17` edge (~2041 ms) is unaffected by the passive FIX8 observations.
- **S11Y (active ACK07E4) — NOT PREPARED / NOT RUN**. Latest passive FIX8K runtime is `07D0/count19`, **not** the required retained `07E4/count17` start state. Never assume an earlier post-test owner survives later sessions/OTAs.

## Current protocol model and evidence boundary
The context-dependent native service/work-owner route remains locally supported as:
`0708 response -> exact all-zero 085F -> ACK085F -> 0884 -> ACK0884 -> 07D0 -> ACK07D0 -> 07E4`.
S11W proves the service route up to `07D0` in one continuous run; S11X original/FIX1 proves retained `07D0` ownership and direct continuation to `07E4` in their specific controller epoch. This does **not** establish a universal fixed ring or a complete Online session. The new FIX8K run started in repeating `07D0 + 0708` without TX, and **does not contradict** S11X: owner state is contextual and can change across sessions.

## Next action — passive S11Y-A (candidate, not yet prepared)
**Hypothesis:** passive capture of the current controller epoch and comparison with earlier S11X plus genuine Online/DCM captures can discriminate the present `07D0` owner from a retained `07E4` owner without transmitting.

**Baseline:** locally verified FIX8K-style capture with repeating `07D0/count19` and `0708/count6`, clean parser and zero ESP TX.

**Controlled change:** offline trace/firmware comparison plus, if needed, read-only owner-geometry/timestamp recording; no new ACK or other TX. Preserve production HA entities and bus-health counters.

**Relevant fields:** `0x0F FC16 07D0/count19`, `07E4/count17` when actually seen, `FC03 0708/count6`, signature and session context; distinguish `07DF` periodic content from owner transition.

**Positive:** independently grounded owner classification and/or naturally observed next owner with clean timing. **Negative:** no `07E4` emergence while only `07D0` continues. **Inconclusive/abort:** log gap, parser integrity fault, unintended ESP TX, FC23/new session, unexpected geometry. **Recovery:** stay capture-only; restore previous proven passive firmware if logging destabilises; controller reboot only for persistent abnormal behaviour.

Only after an actual repeated, qualified `07E4/count17` baseline is observed may a separate, explicitly authorised S11Y-B single-ACK experiment be prepared. A standard FC16 ACK is scheduler/work acknowledgement, **not** proof of semantic acceptance or a write capability.

## Research roadmap
1. Preserve/reconcile evidence: compare raw XTR captures, genuine collaborator Online/DCM captures, Thermia Connect firmware and exact experiment YAML; classify observed/proven vs hypotheses.
2. Reconstruct contextual scheduler one proven owner edge at a time, without speculative or unsolicited TX. Document branches `0834`, `0864` and alternate post-`0884` routes.
3. Qualify restart/session recovery and fail-closed behaviour before any automated owner draining.
4. Validate read-only native values against independent measurements; resume FIX8K only on naturally occurring heating/DHW.
5. Assess controlled, reversible settings changes only with confirmed target/current value, documented risks, abort and rollback; never conflate ACK with semantic write acceptance.
6. Produce a compact production ESPHome/Home Assistant integration after independent stability validation.

## Safety and repository discipline
No DCM hardware available locally; do not propose capturing with a genuine module attached. Keep passive investigation preferred, do not disturb the room sensor, retain production entities/health telemetry. Retain private emulation/security/mailbox tooling outside this repository's public research docs. No new experiment is complete merely because YAML is generated.

---

# 2026-10-07 — Current state through S11X FIX1

## Current experiment / status

- **S11X FIX1 — COMPLETE / POSITIVE** — from a retained local XTR state with recurring `0708/count6` plus recurring `07D0/count19` (sig `D7EC8823`), exactly one standard ACK07D0 released the runtime owner. `07E4/count17` appeared 2041 ms later. Exactly one physical TX; accounting `tx=1 delivered=1 writes=1`; no FC23, mismatch, unknown page, drops, or boundary faults.
- **S11X original — COMPLETE / INCONCLUSIVE** — after S11W, ESP OTA/restart did not restore the earlier `085F` baseline. The controller remained retained at recurring `07D0/count19` plus `0708/count6`; original S11X correctly failed closed as an unexpected pre-TX runtime owner and transmitted nothing.
- **S11W — COMPLETE / POSITIVE** — in one uninterrupted run: one source-faithful `0708` response -> exact all-zero `085F/5` -> ACK085F -> `0884/60` -> ACK0884 -> `07D0/19`. Timings: ~576 ms to all-zero 085F, ~2347 ms ACK085F->0884, ~2039 ms ACK0884->07D0. Exactly three TX with clean accounting.
- **S11V FIX1 — COMPLETE / POSITIVE** — one uninterrupted service chain: `0708` response -> exact all-zero `085F/5` after ~576 ms -> ACK085F -> `0884/count60` after ~2355 ms. Exactly two TX; clean accounting.
- **S11V — COMPLETE / INCONCLUSIVE** — the transient all-zero `085F` state produced by S11U FIX1 did not persist across the next ESP OTA/restart; controller returned to `0708 + 085F(W2=0800)`. Zero TX.
- **S11U FIX1 — COMPLETE / POSITIVE** — one source-faithful response to the retained `0708/count6` poll caused exact all-zero `085F/count5` to appear about 566 ms later. Exactly one TX.
- **S11U — COMPLETE / INCONCLUSIVE** — after OTA, controller had already retained the post-S11T `0708 + 085F(W2=0800)` state; no active TX.

No new live experiment is currently prepared after S11X FIX1. The next candidate is a retained-`07E4/count17` one-ACK continuation (S11Y), but it is not yet generated or run.

## Last completed experiment

The latest completed experiment is **S11X FIX1 — COMPLETE / POSITIVE**.

Locally confirmed transition:

`retained 07D0/count19 + 0708 -> one ACK07D0 -> 07E4/count17 after 2041 ms`.

The controller then continued publishing `07E4/count17` while ESP TX remained fixed at one.

## Current protocol model

The strongest local model is now a contextual pending-work scheduler with persistent owner state across ESP restarts/OTAs.

A locally reconstructed service/runtime route has now been exercised end-to-end far beyond a single isolated edge:

`0708 response -> all-zero 085F -> ACK085F -> 0884 -> ACK0884 -> 07D0 -> ACK07D0 -> 07E4`.

Important evidence boundary:
- S11W proves the route through `07D0` in one uninterrupted run.
- S11X original then proves that the resulting `07D0` owner can persist across ESP OTA/restart.
- S11X FIX1 proves that one ACK to that retained `07D0` advances to `07E4`.

This does not make the entire scheduler globally rigid. Earlier local runs still show context-dependent branches such as `0834`, `0864`, and alternate post-`0884` ownership.

## PROVEN / locally confirmed

- One source-faithful `0708/count6` response can move the retained `085F(W2=0800)` service state to exact all-zero `085F/count5`.
- The exact all-zero `085F` state is transient; it should not be assumed to survive an ESP OTA/restart.
- In the exercised service context, ACK of exact all-zero `085F/count5` releases `0884/count60`.
- In S11W, ACK `0884/count60` released `07D0/count19` after ~2039 ms.
- The resulting `07D0/count19` owner persisted across ESP OTA/restart.
- In S11X FIX1, one ACK to retained `07D0/count19` released `07E4/count17` after 2041 ms.
- Runtime owner persistence is controller-side, not transient ESP state.
- The exercised actions remained bounded and accounting-clean.

## STRONGLY SUPPORTED

- Native Online/DCM-style service is best represented as a contextual scheduler/work-drain plus mailbox boundary, not a globally fixed page sequence.
- Already-proven owner edges can be resumed directly from a retained owner after ESP restart rather than replaying the entire earlier chain.
- Geometry + explicit state/session context is a stronger owner discriminator than frozen payload signatures.
- The known runtime ring remains consistent with `07D0 -> 07E4 -> 07F8 -> 080C -> 0820 -> 0848`, but each retained continuation still needs local qualification before production auto-drain.

## OPEN / UNKNOWN

- Whether the current retained `07E4/count17` can be advanced directly by one standard ACK after another ESP OTA/restart.
- Whether the next owner is again `07F8/count17` in this exact retained epoch.
- Generic rules for safely auto-adopting retained runtime owners without replaying earlier service steps.
- Semantic meanings of the words in `07D0`, `07E4`, `085F`, `0884`, and other scheduler/runtime pages unless separately mapped.
- Whether every native session follows the same service-to-runtime route; earlier branch evidence says not universally.

## Recommended next experiment — S11Y candidate, not yet prepared

**Hypothesis:** the current retained `07E4/count17` owner can be completed directly with one standard address/count ACK and should expose `07F8/count17`.

**Baseline:** repeated `07E4/count17` plus continuing `0708/count6`; no `07D0` owner return; no FC23/new session; zero TX in the new harness; stable geometry; clean parser/UART/accounting.

**Controlled change:** after manual ARM, ACK exactly one new qualified retained `07E4/count17`; then hard capture-only.

**Positive:** `07F8/count17` appears within the observation window. A different new 0x0F FC16 family is secondary positive scheduler advancement.

**Negative:** bus remains live but only `07E4` and/or `0708` continue.

**Abort / inconclusive:** baseline owner changes before TX, FC23/session reset, unexpected family before TX, parser/UART/accounting fault, no new `07E4` after ARM, or any second TX attempt.

**Recovery:** one ACK maximum, then capture-only; controller reboot only for persistent abnormal state.

---

# 2026-10-07 — Current state through S11U FIX1

## Current experiment / status

- **S11U FIX1 — PREPARED / NOT RUN** — current controller state after S11T/S11U is repeated `0708/count6` plus stable `085F/count5 = 0000 0000 0800 0000 0000` (sig `7EAE5A0A`), with `0662/count33` absent. Controlled action: one previously locally exercised source-faithful response to the next post-ARM `0708/count6`; then hard capture-only. Hard TX ceiling 1.
- **S11U — COMPLETE / INCONCLUSIVE** — after OTA, the controller had already retained the post-S11T state: `0708` was present before any TX, `085F(W2=0800)` remained stable, `0662` was absent, and the fail-closed harness transmitted nothing.
- **S11T — COMPLETE / POSITIVE** — from stable retained `0662/33 + 085F(W2=0800)`, one standard ACK to `0662/count33` caused `0662` to stop and `0708/count6` to appear about 1.422 s later. Exactly one physical TX occurred.
- **S11S FIX2 — COMPLETE / INCONCLUSIVE** — corrected the false abort on normal `0662/33` background. The controller remained in `0662/33 + 085F(W2=0800)` with no `0708`; no TX occurred.
- **S11S FIX1 — SUPERSEDED / NOT RUN** — never reached its active sequence because normal repeated `0662/33` traffic was incorrectly classified as an unexpected FC16 family; zero TX.
- **S11S — COMPLETE / INCONCLUSIVE** — expected retained post-ACK `085F` signature `9BFE9A42`, but after the next ESP run the controller had returned to stable `085F(W2=0800)`; zero TX.
- **S11R FIX3 — COMPLETE / NEGATIVE** for its narrow endpoint criterion — one ACK to stable retained `085F(W2=0800)` changed the same `085F/5` geometry to signature `9BFE9A42` but did not expose a different FC16 family within 10 s.
- **S11R FIX2 — COMPLETE / INCONCLUSIVE** — ARM was refused because the strict pre-click `0708` recency guard was stale; zero TX.

## Last completed experiment

The latest completed experiment is **S11U — COMPLETE / INCONCLUSIVE**. It transmitted nothing because the controller had remained in the post-S11T scheduler state across the ESP OTA/restart.

The latest positive protocol discriminator is **S11T — COMPLETE / POSITIVE**:

`retained 0662/33 + 085F(W2=0800) -> one ACK0662 -> 0662 stops -> first 0708/count6 ~1.422 s later`.

This is locally confirmed on the XTR M and materially narrows the service/scheduler path.

## Current protocol model

The current strongest local model is a contextual pending-work scheduler with an ordered service boundary, not a rigid global page chain.

Newly confirmed local edge:

`0662/count33 pending -> ACK0662 -> 0708 mailbox phase`.

Combined with earlier local evidence, the working service model is now:

`0662 ACK -> 0708 response -> changed 085F -> ACK085F -> next pending runtime/history owner`.

Only the first edge above is newly proven by S11T. The complete combined chain remains a hypothesis until exercised in one uninterrupted run.

S11R FIX3 additionally showed that ACKing stable `085F(W2=0800)` alone is not sufficient to expose a different FC16 family within 10 s. It changes the same `085F/5` payload state instead.

## PROVEN / locally confirmed

- Stable retained `085F/count5 = 0000 0000 0800 0000 0000` is a real XTR state.
- One standard ACK to that stable `085F` causes a reproducible same-geometry payload/signature transition, but did not release a different FC16 family within the S11R FIX3 10 s window.
- Stable `0662/count33` can be a pending controller work item in parallel with `085F(W2=0800)`.
- One standard ACK to retained `0662/count33` locally releases that owner: `0662` stops and `0708/count6` begins about 1.422 s later.
- The post-S11T `0708 + 085F(W2=0800)` state persisted across an ESP OTA/restart; the ESP restart did not restore `0662`.
- S11T used exactly one physical TX and remained parser/accounting clean.

## STRONGLY SUPPORTED

- `0662` is part of scheduler/work-drain ordering rather than harmless unrelated traffic in every context.
- `0708` availability depends on prior pending work completion in at least the S11T retained context.
- ESP restart/OTA does not necessarily reset the Thermia controller scheduler state.
- The `085F` signature `9BFE9A42` is consistent with an all-zero five-word payload for this exact FC16 geometry, but exact all-zero words were not directly logged in S11R FIX3 and therefore remain signature-derived there.

## OPEN / UNKNOWN

- Whether one source-faithful `0708` response from the current post-S11T state causes the expected `085F` transition or exposes another pending FC16 owner. **S11U FIX1 tests exactly this.**
- Whether the locally successful broader service sequence requires strict ordering `0708 response -> changed 085F -> ACK085F`, or whether equivalent contextual orderings exist.
- Generic production rules for automatically recognizing and draining all retained scheduler states without over-acknowledging unrelated traffic.
- Semantic meaning of the individual words in `085F`, `0662`, `0834`, and other runtime/history pages beyond locally established transport/scheduler behavior.

## Next experiment — S11U FIX1

**Hypothesis:** in the current retained post-S11T state, one source-faithful response to the next `0708/count6` poll is the missing service step and will change `085F` or expose another controller-owned FC16 family.

**Baseline:** repeated `0708/count6`; at least three exact `085F/count5 = 0000 0000 0800 0000 0000`; no `0662/count33`; no FC23/new session; zero TX; clean parser/UART/accounting.

**Controlled change:** after manual ARM, respond exactly once to the next `0708/count6` using the already locally exercised source-faithful idle mailbox response. No ACK085F or other TX is allowed.

**Positive:** within 10 s, `085F` changes away from `7EAE5A0A/W2=0800`, especially toward the previously seen transition state, or another different 0x0F FC16 family appears.

**Negative:** bus remains live for >=10 s with only unchanged `085F` and repeated `0708`.

**Abort / inconclusive:** `0662` returns before TX, baseline `085F` changes before TX, unexpected FC16/FC03 family appears, FC23/session restart, parser/UART/accounting fault, no post-ARM `0708` within 15 s, any second TX attempt, or post-TX silence.

**Recovery:** hard capture-only immediately after the single response; controller reboot only if a persistent abnormal state is observed.

---

# 2026-10-07 — Current state through S11R FIX2

## Current experiment / status

- **S11R FIX2 — PREPARED / NOT RUN** — clean one-action retained-`085F/5` probe using the locally observed stable baseline `0000 0000 0800 0000 0000` plus recent `0708/6`. One standard ACK to the next exact matching `085F/count5`; all later traffic capture-only; hard TX ceiling 1.
- **S11R FIX1 — SUPERSEDED / NOT RUN** — prepared against an all-zero `085F` baseline, then superseded before live use when the earlier S11R passive run showed the stable retained baseline is actually W2=`0800`.
- **S11R original — COMPLETE / INCONCLUSIVE** — passive baseline after OTA repeatedly showed `085F/5 = 0000 0000 0800 0000 0000`, not all-zero; experiment locked before ARM; `physicalTX=delivered=writes=0`.
- **S11Q FIX2 — COMPLETE / POSITIVE** — one locally executed ACK to retained `0834/count18` released that owner. Follow-on was `0708/6` then all-zero `085F/5` about 2.02 s after ACK0834. The harness later misclassified the run because inherited pre-sequence code saw the post-ACK 085F; protocol result is positive.
- **S11Q FIX1 — SUPERSEDED / NOT RUN** — fixed-signature qualifier locked when a valid `0834/18` payload variant changed signature; no TX.
- **S11Q original — SUPERSEDED / NOT RUN** — expected the earlier `085F(0800)+0708` entry state, but the controller had already retained `0834/18`; no TX.
- **S11P — COMPLETE / INCONCLUSIVE** — branch-A path reached ACK0884, then the first runtime owner was `0834/18`; no ACK0834 was sent because local safety was still OPEN at that point.
- **S11O — COMPLETE / INCONCLUSIVE** — direct-0884 branch and the full `07D0 -> 07E4 -> 07F8 -> 080C -> 0820 -> 0848` runtime ring completed; post-0848 `0708` was followed by `0864/4`, not the rigidly expected final zero-085F.
- **S11J — COMPLETE / POSITIVE** — retained runtime ring `07D0 -> 07E4 -> 07F8 -> 080C -> 0820 -> 0848` was ACKed cleanly in one run; follow-on included `0708` and a later `085F` publication.

## Last completed experiment

The latest attempted experiment is **S11R original — COMPLETE / INCONCLUSIVE** because its intended all-zero prerequisite was absent and it transmitted nothing.

The latest positive protocol discriminator is **S11Q FIX2 — COMPLETE / POSITIVE**:
`retained 0834/18 -> one ACK0834 -> 0708 -> all-zero 085F/5`.

Subsequent passive S11R evidence shows the all-zero 085F was not a stable retained baseline: the controller later repeatedly published
`085F/5 = 0000 0000 0800 0000 0000` with `0708/6`, while ESP TX stayed zero.

## Current protocol model

Locally confirmed controller-owned work is not a single fixed linear sequence. The controller can expose pending work in different orders depending on retained/session context.

Current locally exercised work-owner set includes:
`07D0`, `07E4`, `07F8`, `080C`, `0820`, `0834`, `0848`, `0864`, qualified `0870`, `0884`, and context-qualified `085F`.

The strongest current scheduler model is therefore a **contextual pending-work drain**, not a rigid page chain. In particular:
- ACK0848 can be followed by another pending work family such as 0864;
- ACK0884 can expose either runtime work or, in another retained context, 0834;
- ACK0834 is now locally proven to release its pending owner slot;
- the immediate post-ACK0834 all-zero 085F can later settle back to the familiar retained `085F(0800) <-> 0708` service boundary.

## PROVEN / locally confirmed

- Standard address/count ACK of retained `0834/count18` is locally accepted as work completion in the exercised XTR context: the repeated 0834 owner stopped and a different controller-owned FC16 family appeared.
- The post-ACK0834 follow-on in S11Q FIX2 was `0708` then all-zero `085F/5` about 2.02 s after ACK0834.
- The stable retained S11R baseline observed later is `085F/5 = 0000 0000 0800 0000 0000` plus repeated `0708/6`; no all-zero 085F was seen in that supplied passive run and ESP TX remained zero.
- The complete runtime ring `07D0 -> 07E4 -> 07F8 -> 080C -> 0820 -> 0848` is locally exercised with clean ACK accounting.
- `0834` payload content can vary while start/count geometry remains `0834/18`; fixed payload signature is not a valid owner identity.

## STRONGLY SUPPORTED

- Runtime ownership is geometry + session/context driven rather than tied to a frozen payload signature.
- The controller retains pending work across ESP restarts/OTAs, while the visible owner can change as the internal scheduler/session advances.
- The old production engine's whitelist-like treatment of known runtime pages matches the newer observation that known pages can be interleaved rather than appearing in one fixed order.

## OPEN / UNKNOWN

- Whether one isolated ACK to the stable retained `085F(0800)` owner is sufficient to release the next controller-owned family without first sending a `0708` mailbox response. S11R FIX2 tests exactly this.
- Which family will follow that isolated ACK085F in the current retained epoch.
- Generic ownership rules for contextual `085F` and qualified `0870` outside already exercised states.
- Active local ACK behaviour for any not-yet-exercised context remains OPEN even when firmware/genuine captures suggest it.

## Next experiment — S11R FIX2

**Hypothesis:** the stable retained `085F/count5 = 0000 0000 0800 0000 0000` owner can be released by one standard FC16 address/count ACK without any `0708` response.

**Baseline:** at least three exact matching 085F publications + at least two `0708/6` polls; both last observations <=4 s old; zero TX; no other 0x0F FC16/FC03 family; no FC23; clean parser/accounting.

**Controlled change:** after manual ARM, ACK exactly the next matching `085F/count5` once. No other response or ACK is allowed.

**Positive:** first different 0x0F FC16 within 10 s after ACK085F.

**Negative:** bus remains live for >=10 s with only repeated 085F and/or 0708.

**Abort / inconclusive:** baseline payload changes, qualification becomes stale, another family appears before ACK, FC23/session reset, parser/UART/accounting fault, or any second TX attempt.

**Recovery:** capture-only immediately after the one ACK; controller reboot only if an abnormal persistent state is observed.

---
# 2026-10-07 — S11I COMPLETE / POSITIVE — retained 0884 ACK releases to 07D0

## Current experiment / status

- **S11I — COMPLETE / POSITIVE** — in one uninterrupted no-controller-reboot retained run, the locally proven two-step `085F/0708` service release exposed `0884/60`; exactly one ACK0884 then released the controller to `07D0/19` after 2042 ms.
- **S11H — COMPLETE / NEGATIVE** for the narrower direct-`07D0` endpoint hypothesis; its service-release action itself remained effective and exposed `0884/60`.
- **S11G FIX1 — COMPLETE / INCONCLUSIVE** — retained `0884` was absent after ESP restart, so ACK0884 was not exercised there.

## S11I observed sequence

Directly qualified retained baseline:
`085F/5 = 0000 0000 0800 0000 0000` + repeated `0708/6`, zero TX, no FC23, clean integrity.

Controlled actions:
1. TX1: one proven `0708/6` response with W0..W4=0000, W5=0006;
2. controller published exact all-zero `085F/5`;
3. TX2: one standard ACK to `085F/count5`;
4. controller published `0884/60`;
5. TX3: one standard ACK to `0884/count60`;
6. all later ESP TX disabled;
7. `07D0/19` appeared 2042 ms after TX3.

Final status:
`result=1`, `tx1=1`, `tx2=1`, `tx3=1`, `seen0884=1`, `seen07D0>=1`, `physicalTX=delivered=writes=3`, `mismatch=0`, `unknown=0`, `drops=0`, `boundary=0`. One parser resync step was present but stable in the supplied slice.

## Evidence classification

**PROVEN / locally confirmed**
- current retained `085F(0800) <-> 0708` service gate can be released with the proven S10C two-step sequence;
- that release can expose pending `0884/60` work in this retained controller epoch;
- exactly one standard ACK to that exposed `0884/60` is locally sufficient to release into `07D0/19` in the same uninterrupted ESP/controller epoch;
- after ACK0884, the first `07D0/19` followed after 2042 ms, closely matching genuine gateway cadence;
- the complete retained path required exactly three ESP transmissions and no Thermia/controller reboot.

**STRONGLY SUPPORTED**
- retained work ownership survives ESP process restarts but may be hidden behind a phase-local `085F/0708` service gate;
- `0884` is a real pending history/runtime work item whose ACK can complete the retained work and return scheduling to the runtime ring.

**OPEN / UNKNOWN**
- whether every retained `0884` context can use the same ACK-only release without first restoring the phase-local service gate;
- whether the generic production emulator should auto-chain this exact retained path or require stronger owner/session classification;
- whether post-`07D0` runtime can now be resumed directly without replaying earlier service steps in the current controller epoch.

## Recommended next step

Do not spend another controller reboot. The highest-value next live test is a retained runtime continuation from the now-visible `07D0/19`, reusing the already locally proven S10D-fix1 chain (`07D0 -> 07E4 -> 07F8 -> 080C -> 0820 -> 0848`) with exact one-shot ownership guards. This should be treated as a separate experiment; do not silently auto-advance beyond 0848 because the later service boundary is context-sensitive.

---
# 2026-10-07 — S11H COMPLETE / NEGATIVE for 07D0 endpoint; positive retained release to 0884

## Current experiment / status

- **S11I — PREPARED / NOT RUN** — no-controller-reboot continuation in one uninterrupted ESP process: replay the proven S11H two-step retained release, then ACK exactly one resulting `0884/60`; capture-only afterwards; endpoint `07D0/19`.
- **S11H — COMPLETE / NEGATIVE** for the narrow hypothesis that the proven S10C release sequence reproduces `07D0/19` in the current controller epoch. The exact two-step action executed cleanly but exposed repeated `0884/60` instead of `07D0/19`.
- **S11G FIX1 — COMPLETE / INCONCLUSIVE** — retained `0884` prerequisite absent after ESP restart; zero TX.

## S11H observed result

Baseline qualification directly confirmed repeated `085F/5 = 0000 0000 0800 0000 0000`, repeated `0708/6`, no FC23/new session, zero TX and clean integrity.

At ARM, S11H executed the locally proven S10C sequence: TX1 one 0708/6 response with W0..W4=0000 and W5=0006; controller 085F then changed to exact all-zero; TX2 one standard FC16 ACK to 085F/count5; all later ESP TX disabled.

Both TX were delivered. The controller did not publish `07D0/19` within the 10 s endpoint window. Instead, about 2.33 s after TX2, it began publishing `0884/60`, which then repeated interleaved with `0708/6` while ESP TX remained fixed at 2.

Integrity remained clean: mismatch=0, unknown=0, resync=0, drops=0, boundary=0.

### Interpretation

**PROVEN / locally confirmed**
- the current retained `085F(0800) <-> 0708` boundary is real and directly word-confirmed;
- the S10C mailbox step again clears 085F word2 from `0800` to `0000`;
- one ACK to that exact changed all-zero `085F/5` again releases the service boundary;
- in this controller epoch, the released next work is `0884/60`, not `07D0/19`.

**DISPROVEN / superseded for this context**
- the stronger assumption that the same two-step retained release always returns directly to `07D0/19`.

**STRONGLY SUPPORTED**
- controller/session work ownership survives ESP process restarts and determines which pending runtime family is exposed after the `085F` service gate;
- the `0884` work seen after S11H is consistent with unfinished S11F/S11G history-overlay work surviving behind the `085F/0708` boundary.

## S11I prepared discriminator

Keep S11H behavior unchanged through the first resulting `0884/60`. The only new active action is one standard FC16 ACK to that exact `0884/60`, in the same uninterrupted ESP/controller epoch. No mailbox response or other ACK after that point.

Positive: `07D0/19` within 10 s after ACK0884 with total physical TX exactly 3.

Negative: controller remains live for >=10 s after ACK0884 but no `07D0/19` appears.

Abort/inconclusive: baseline word mismatch, changed 085F not all-zero, missing 0884 after the proven two-step release, fresh FC23, unexpected family, parser/UART/accounting fault, or TX >3.

No Thermia/controller reboot is part of S11I.

---
# 2026-10-07 — S11H PREPARED / NOT RUN — replay locally proven S10C retained release

## Current experiment / status

- **S11H — PREPARED / NOT RUN** — no-controller-reboot replay of the locally proven S10C retained release from the currently observed `085F(7EAE5A0A) <-> 0708` boundary.
- **S11G FIX1 — COMPLETE / INCONCLUSIVE** — retained 0884 prerequisite absent; zero TX.

## S11H hypothesis and baseline

Current S11G FIX1 bus evidence shows repeated `085F/5` signature `7EAE5A0A` plus repeated `0708/6` with zero ESP TX. S10C previously proved that this signature corresponded to `0000 0000 0800 0000 0000` and that the exact two-action sequence below released to `07D0/19`.

S11H does not trust the signature alone: it directly logs and requires the five baseline words before ARM.

## Exact controlled action

```text
qualified baseline 085F = 0000 0000 0800 0000 0000
+ >=3 baseline 085F and >=3 0708 polls
-> TX1: one FC03 0708/6 response W=0000,0000,0000,0000,0000,0006
-> require controller publication exact 085F = 0000,0000,0000,0000,0000
-> TX2: one standard FC16 address/count ACK to 085F/count5
-> all later traffic capture-only
-> positive endpoint 07D0/19
```

Hard TX ceiling: 2. No setting value is changed. Any payload mismatch, fresh FC23, unexpected family, integrity fault or accounting mismatch fails closed. Thermia/controller reboot is not part of the experiment.

---

# 2026-10-07 — S11G FIX1 COMPLETE / INCONCLUSIVE — retained 0884 absent after ESP-only restart

## Current experiment / status

- **S11G FIX1 — COMPLETE / INCONCLUSIVE** — prerequisite retained `0884/count60` was absent after ESP-only OTA/restart; no ACK0884 was sent and the active hypothesis was not exercised.
- **S11F — COMPLETE / POSITIVE** — fresh source-faithful session reached `0884/60` and stopped all TX at first 0884.

## S11G FIX1 observed result

The post-OTA controller state was not the expected retained 0884 boundary. Instead the live bus showed a stable repeated pair:

```text
085F/count5  sig=7EAE5A0A
0708/count6  polls
```

S11G counters in the supplied log reached `q0708=27` while `q0884=0`. The first unexpected pre-arm `085F/5` set `otherPre=1`, `locked=1`, and `result=3` (inconclusive), exactly as the fail-closed design intended. `physicalTX=delivered=writes=0`; ACK0884 remained 0; no `07D0` appeared. Parser geometry/unknown/drop/boundary counters remained clean. The nonzero resync counter was already stable at 16 in the visible slice and did not increase there.

### Conclusion

S11G did **not** test whether ACK0884 alone releases to 07D0, because the required retained 0884 state no longer existed when FIX1 observed the bus. Do not classify this as a negative result for ACK0884.

The useful new observation is that, without a Thermia/controller reboot and with zero ESP TX, the controller is now back at the familiar retained `085F(7EAE5A0A) <-> 0708` boundary.

### Recommended next direction

Do not broaden S11G to ACK arbitrary pre-arm traffic. Preserve S11G as inconclusive. If avoiding a controller reboot remains the priority, the next experiment should be a separately scoped retained `085F/0708` continuation using prior S10/S11 evidence; do not reinterpret the missing 0884 as an authorization for ACK0884.

---

# 2026-10-07 — S11F COMPLETE / POSITIVE; S11G PREPARED / NOT RUN

## Current experiment / status

- **S11G FIX1 — PREPARED / NOT RUN** — corrected compile/scoping defect in the first generated S11G YAML; protocol hypothesis and one-shot `0884/count60` ACK design are unchanged. The first S11G YAML did not compile and therefore never ran.\n- **S11G original YAML — SUPERSEDED / NOT RUN** — ESPHome C++ generation reached compile, then failed because helper/frame-handler code was accidentally spliced inside `candidates_for`; no firmware was flashed and no bus action occurred.\n- **S11G — PREPARED / NOT RUN** — no-controller-reboot retained `0884/count60` release probe. After an ESP-only OTA/restart, require repeated exact `0884/60` plus live `0708/6` polling with zero TX, then permit exactly one standard FC16 address/count ACK to `0x0F:0884/60`; all later traffic is capture-only.
- **S11F — COMPLETE / POSITIVE** — fresh source-faithful session reached `0884/60` after one qualified ACK to `0870/17`; first `0884` disabled all further TX.
- **S11E — SUPERSEDED / NOT RUN** — the planned “withhold ACK0864” causality test is retained as an optional scientific discriminator but is no longer the shortest route toward production parity.
- **S11D — COMPLETE / POSITIVE** — full fresh native session reached capture-only `0870/17` through approval, exact 32-page bootstrap, bounded mailbox/runtime service and qualified `0864/4` completion.

## S11F observed result

Local XTR M, one uninterrupted fresh controller session:

```text
canonical FC23 qualification
-> approval response
-> exact settings bootstrap 32/32
-> bounded 0708/6 mailbox service
-> runtime progression
-> 0864/4 ACK
-> 0870/17
-> one qualified standard ACK0870
-> one further bounded 0708/6 response
-> 0884/60
```

Key counters at the positive endpoint:

```text
result=1
boot=32/32
mailbox responses=5
runtime ACKs=9
ack0870=1
physicalTX=delivered=writes=47
mismatch=0 unknown=0 resync=0 drops=0 boundary=0
```

First `0884/60` arrived about 2.04 s after the qualified ACK0870. Repeated `0884` publications continued after completion while TX stayed fixed at 47.

### Evidence classification

**PROVEN / locally confirmed**

- a fresh XTR session can be driven through approval -> full 32-page bootstrap -> runtime -> `0864` -> `0870` -> `0884` using bounded source-faithful service;
- one qualified standard FC16 ACK to `0870/17` is locally safe in the exact exercised fresh-session context;
- the first `0884/60` can be used as a fail-closed capture-only endpoint;
- after that endpoint, repeated `0884/60` plus `0708/6` continue while ESP TX remains disabled.

**STRONGLY SUPPORTED**

- qualified `0870` completion participates in the normal transition to the `0884` history/runtime overlay;
- S11F follows the same broad cadence/order as genuine Online/DCM captures.

**CAUSAL LIMITATION / OPEN**

S11F does not prove that ACK0870 alone is sufficient for 0884 because one exact `0708/6` mailbox response occurred between ACK0870 and first 0884. The proven statement is the combined qualified-session path above.

## Offline 0884 correlation used for S11G

Across the currently available raw captures with explicit controller `0884/60` requests and matching gateway ACKs, 21/21 observed requests were ACKed. Nineteen qualified normal-cycle cases then showed:

```text
ACK0884 -> 0708 poll -> 07D0/19
```

Timing over those 19 cases:

```text
0884 request -> next 0708: min 1.253 s, median 1.277 s, max 3.534 s
0884 request -> next 07D0: min 1.979 s, median 2.010 s, max 4.578 s
```

Two remaining ACKed 0884 observations do not form a normal-cycle discriminator: one transitions into a settings/bootstrap context and one ends before useful follow-on traffic is visible.

This is genuine/cross-model evidence, not by itself proof of local retained-XTR ACK authorization.

## S11G — retained 0884 release probe

**Hypothesis:** in the exact retained post-S11F state, one standard ACK to repeated `0884/60` is sufficient to release the history-overlay retry loop into the next runtime cycle without a Thermia/controller reboot and without a mailbox response from the ESP.

**Baseline:** S11F COMPLETE / POSITIVE; controller repeatedly publishes `0884/60` and polls `0708/6`; ESP TX is disabled.

**Controlled change:** ESP-only OTA/restart, passive qualification of at least 3 exact `0884/60` publications with at least 2 exact `0708/6` polls and clean integrity, then exactly one standard FC16 address/count ACK to the next `0884/60`. No `0708` response and no other FC16 ACK is allowed after the split.

**Positive:** `07D0/19` appears within 10 s after the one ACK0884 with no second ESP TX. This demonstrates retained release into the normal runtime ring under the isolated action.

**Negative:** controller remains live for >=10 s with repeated `0884/60` and `0708/6`, but no `07D0/19` appears. This is negative only for “ACK0884 alone is sufficient”; it does not reject a source-faithful ACK0884 + mailbox-service path.

**Inconclusive / abort:** retained 0884 is absent after ESP OTA, a canonical FC23/new controller session appears, another runtime/config family arrives before the active split, unexpected geometry appears, or parser/integrity/UART accounting becomes non-clean.

**Safety / recovery:** the only active action is a standard metadata ACK to slave `0x0F`, page `0884`, count 60. The 60-word controller-owned history payload is not modified or replayed. Hard active-TX maximum is 1. After the ACK all traffic is capture-only. A Thermia reboot is not part of S11G and is reserved only for recovery if the controller enters an unexpected persistent state.

---

# 2026-10-05 — EXP426 COMPLETE / INCONCLUSIVE — trigger absent; baseline/runtime healthy

## Current experiment / status

- **EXP426 — COMPLETE / INCONCLUSIVE** — the narrow isolated `0662/count33` release-ACK path was not exercised because no `0662/count33` appeared in the supplied ~147 s run.
- **EXP425 — COMPLETE / NEGATIVE** — one ACK stopped the prior repeated 0662 loop, but the predicted ordered tail did not follow.
- **EXP424 — SUPERSEDED / NOT RUN**.
- **EXP423 — COMPLETE / INCONCLUSIVE**.
- **EXP422 — COMPLETE / POSITIVE**.
- **EXP421 — COMPLETE / POSITIVE**.

## EXP426 observed result

The ESP entered retained `stage=40` cleanly after OTA. EXP426 diagnostics remained:
- `repeat=0`;
- `released=0`;
- `releaseACK=0`;
- `resumeStarted=0`.

No `0662/count33` frame appeared anywhere in the supplied log, so the EXP426 active path never transmitted.

Normal startup/runtime synchronization completed without any special 0662 handling:
- `042E/count15` synchronized;
- `0442/count13` synchronized;
- `0546/count20` synchronized;
- `03E8/count14` Configuration autosync confirmed and writes became READY at ~24 s.

At the final visible heartbeat (~146 s):
- `stage=40`;
- `cacheValid=1`, `cache03F4=22`;
- `refreshReq=1`, `refreshOK=1`;
- `runtimeFC16ACK=65`, `idle0708=34`;
- `semanticResponses=0`, `confirmedWrites=0`;
- `unknown16=0 unknown03=0 peer17=0 peer16ack=0 resync=0 drops=0`.

EXP418 remained balanced (7 tokens set / 7 consumed) and EXP420 showed `ownedACK=4 noOwner=0`.

## Conclusion

**EXP426 is COMPLETE / INCONCLUSIVE for its 0662-release hypothesis.**

This run does NOT show that the isolated release ACK is unnecessary or sufficient; the required repeated-0662 condition simply did not recur.

It does positively confirm that the presentation-only HA cleanup and the retained baseline do not disrupt normal startup synchronization in this run.

## Recommended next action

Keep the EXP426 logic available for a repeat occurrence of the exact 0662 condition. Do not manufacture a 0662 condition with speculative traffic.

Because normal startup is currently healthy, return to the previously interrupted generic-page geometry program: prepare a fresh `0442/count13` validation derived from this cleaned baseline, while leaving the EXP426 0662 safety path dormant/fail-closed.

---

# 2026-10-05 — EXP426 PREPARED / NOT RUN — isolated 0662 release ACK + HA entity cleanup

## Current experiment / status

- **EXP426 — PREPARED / NOT RUN** — test a narrowly-qualified one-shot ACK for repeated `0662/count33` without assuming an ordered export tail.
- **EXP425 — COMPLETE / NEGATIVE** — the one-shot 0662 ACK stopped the retry loop, but the predicted `0683 -> ... -> 06F4` ordered tail never appeared. After the 60 s timeout, normal retained-runtime synchronization recovered and Configuration reached READY.
- **EXP424 — SUPERSEDED / NOT RUN**.
- **EXP423 — COMPLETE / INCONCLUSIVE**.
- **EXP422 — COMPLETE / POSITIVE**.
- **EXP421 — COMPLETE / POSITIVE**.

## EXP425 result that motivates EXP426

Observed locally:
- exact repeated `0662/count33` was recognized and ACKed once;
- repeated 0662 stopped;
- no `0683/count33` followed;
- ordered-resume timed out cleanly after 60 s;
- normal runtime then resumed;
- `042E/count15`, `0442/count13`, and `0546/count20` startup syncs completed;
- `03E8/count14` Configuration autosync completed and writes became READY;
- parser/peer/resync/drop integrity stayed clean.

Conclusion:
The EXP425 ordered-tail hypothesis is negative. The narrower interpretation — that this exact 0662 retry condition may need a standalone release ACK — remains viable and is now the EXP426 hypothesis.

## EXP426 controlled change

Only one new active authorization versus the EXP423 baseline:
- exact `0x0F FC16 0662/count33`;
- pre-first-0708;
- unsynchronized Configuration;
- no semantic write/pending/dirty state;
- EXP378/379/380 states exactly 7/7/7;
- EXP410 idle;
- no recovery/hot-rejoin/resume;
- clean integrity counters;
- same receive-frame CRC repeated >=3 times within 5 s gaps.

On the third qualifying repeat:
- send the standard `0662/count33` FC16 ACK exactly once;
- do **not** seed ordered resume;
- do **not** suppress/hold 0708;
- allow the existing normal runtime/autosync logic to continue.

No setting value is transmitted.

## EXP426 expected positive result

- exactly one isolated 0662 ACK;
- no further 0662 retry;
- normal 0708 resumes;
- 042E, 0442, 0546 startup syncs complete;
- 03E8 Configuration autosync reaches READY;
- integrity counters stay clean.

## EXP426 HA entity cleanup

Presentation-only cleanup:
- removed EXP417 Parser Status text entity; numeric suppression counter retained;
- removed EXP421 Generic Page Core status text entity; generic counters retained;
- removed EXP414 Arm / Cancel Natural 0532 buttons;
- EXP414 dormant status object kept internal because old dormant capture code still references it;
- active EXP418/419/420 diagnostics retained;
- added one compact EXP426 status entity.

No protocol/state-machine behavior is intentionally removed by this cleanup.

## User action

Flash EXP426, change no HA setting, leave the system untouched for at least 2 minutes and up to 3 minutes if Configuration is not READY, then return the full log from OTA/boot through either complete synchronization or the failure/timeout point.

---

# 2026-10-05 — EXP425 PREPARED / NOT RUN — repeated 0662 orphan-resume adoption

## Current experiment / status

- **EXP425 — PREPARED / NOT RUN** — tightly-qualified one-shot adoption of the repeated pre-first-0708 `0662/count33` observed in EXP423, followed only by the already-existing exact ordered-resume tail.
- **EXP424 — SUPERSEDED / NOT RUN** — do not run until the 0662 ownership/recovery gap is resolved.
- **EXP423 — COMPLETE / INCONCLUSIVE** — aborted before the `044D` geometry write because repeated `0662/count33` was withheld by EXP420.
- **EXP422 — COMPLETE / POSITIVE**.
- **EXP421 — COMPLETE / POSITIVE**.

## Hypothesis

The repeated byte-identical `0662/count33` is a retained/orphaned ordered-export page whose predecessor ACK happened before the ESP OTA/reconnect. A one-shot ACK only after repeated exact evidence should release the controller into the already-known tail:

`0662 -> 0683 -> 06A4 -> 06C5 -> 06EA -> 06F1 -> 06F4`.

## Exact controlled change

New authorization exists only for exact `0x0F / FC16 / 0662/count33` when all of the following hold:

- stage40;
- byteCount 66 / frame length 75;
- no 0708 answered yet;
- `configSynced=0`;
- write state idle, no pending/dirty semantic transaction;
- EXP378/379/380 states exactly `7/7/7`;
- EXP410 idle;
- no recovery, hot-rejoin, or existing resume active;
- no approval TX in this ESP session;
- unknown/peer/resync/drop integrity clean;
- same received frame CRC observed on at least 3 retries with <=5 s gaps.

On the third qualifying repeat EXP425 sends the already-existing standard `0662/count33` ACK once and seeds the existing ordered-resume engine at expected index 16 = `0683/count33`.

During the adopted tail, any 0708 interleave receives only the existing idle W5=0006 response; Configuration autosync and semantic selectors are suppressed until the ordered tail finishes.

No semantic setting value is transmitted by EXP425.

## Evidence behind the discriminator

Replay of the supplied EXP423 failure log found 165 captured `0662/count33` frames; the first three carried the same received CRC field `BB60`, consistent with repeated byte-identical retry behavior.

## Positive criteria

- exactly one EXP425 0662 adoption ACK;
- next config page is exact `0683/count33`;
- exact ordered continuation through `06F4/count19`;
- `EXP425 ORPHAN_TAIL_RESUME_POSITIVE`;
- no out-of-order page, ACKed-page retry, unknown/peer/resync/drop fault;
- normal 0708/config synchronization can resume afterwards.

## Negative / abort

No TX if the exact qualifier is not met. Abort/fail-closed on repeated 0662 after the adoption ACK, out-of-order config page, timeout, parser/peer/integrity fault, semantic activity, or session degradation.

## Recovery

If partial adoption leaves the controller retained on a later config page, reverting ESP firmware alone may not clear controller transfer state. Stop TX, revert to the last proven firmware, and use the known controller restart recovery if the retained transfer remains.

## Offline validation

- YAML parse PASS;
- undefined `id()` references: 0;
- UART `write_array` sites `63 -> 65`;
- all original TX expressions preserved in order;
- exactly two new TX call sites: the one-shot 0662 ACK and idle 0708 response during the adopted tail;
- no new semantic desired-page TX site;
- hard-coded 0662 ACK CRC independently recalculated as wire bytes `A0 69`;
- braces/parentheses balanced;
- ESPHome compile not run in assistant environment.

---

# 2026-10-05 — EXP423 COMPLETE / INCONCLUSIVE — aborted by pre-target 0662 ACK-ownership regression

## Current experiment / status

- **EXP423 — COMPLETE / INCONCLUSIVE** — target `0442/count13` semantic validation was not run because the baseline entered a persistent `0662/count33` retry loop before configuration synchronization.
- **EXP424 — SUPERSEDED / NOT RUN** — its prerequisite (EXP423 COMPLETE / POSITIVE) was not met; do not run the prepared EXP424 YAML.
- **EXP422 — COMPLETE / POSITIVE** — generic helper live-confirmed on `042E/count15`.
- **EXP421 — COMPLETE / POSITIVE** — generic helper live-confirmed on `03E8/count14`.
- **EXP420 — COMPLETE / POSITIVE for the observed long retained-runtime slice, but its ownership predicate is now known to be incomplete outside that exercised context.**

## EXP423 observed failure before active write

After OTA/reconnect the controller remained at `stage=40`, `A80E=0000`, `A80F=000A`, but repeatedly published `FC16 0662/count33`.

The EXP420 ownership rule classified each publication as:
`EXP420_CONFIG_NO_OWNER ... NO_ACK`.

Key state during the loop:
- `write_state=0`;
- `exp378_state=7`, `exp379_state=7`, `exp380_state=7` (startup-unsynchronized states);
- `configSynced=0`;
- `resume=0`;
- no generic semantic TX;
- no parser/resync/drop fault.

The retry persisted for the full supplied ~180 s slice. The no-owner counter reached 166 and `idle0708` remained 0. The generic transaction counter remained 0 and no setting write was attempted.

## Interpretation

This is not evidence against the EXP421 generic page builder and not an `0442/count13` semantic-write result.

It is new local evidence that the EXP420 config-ACK ownership model is too narrow for at least one pre-first-0708 / unsynchronized context involving `0662/count33`.

The previous EXP420 positive result remains valid for the long retained-runtime context actually observed there, but must not be generalized to all reconnect/startup/export contexts.

## Safety decision

Do not attempt the EXP423 044D write and do not run EXP424.

Do not simply restore unconditional page-shape ACK for 0662. The next experiment should isolate the legitimate owner/context for this 0662 transfer and authorize only that context.

## Recommended next experiment

**EXP425 — 0662 pre-first-0708 ownership discrimination / recovery hardening.**

Goal: reproduce the observed unsynchronized retained-session condition and determine a narrow owner predicate for `0662/count33`, while preserving EXP420 fail-closed behavior for unrelated config pages.

---

# 2026-10-05 — EXP424 PREPARED / NOT RUN — queued behind EXP423

## Current experiment / status

- **EXP423 — PREPARED / NOT RUN** — third generic page-geometry validation on `0442/count13`; this remains the current live experiment.
- **EXP424 — PREPARED / NOT RUN** — fourth generic page-geometry validation on `0546/count20`, staged in advance and **must not be run until EXP423 is reviewed COMPLETE / POSITIVE**.
- **EXP422 — COMPLETE / POSITIVE** — generic helper live-confirmed on `042E/count15`.
- **EXP421 — COMPLETE / POSITIVE** — generic helper live-confirmed on `03E8/count14`.

## EXP424 hypothesis

The unchanged EXP421 generic desired-page builder/TX primitive also preserves the already-proven `0546/count20` semantic write flow.

## Target

- slave `0x0F`;
- page `0546/count20`;
- register `0553`;
- word 13;
- local meaning Operation Mode;
- local writeability source: EXP380;
- EXP424 restricts the live validation to the two locally panel-confirmed modes:
  - raw 1 = Auto;
  - raw 2 = Compressor.

No Off / Auxiliary Heater / Hot Water value is part of EXP424.

## Controlled live action

After EXP423 has passed:
1. read the fresh authoritative Operation Mode;
2. if Auto, request Compressor;
3. if Compressor, request Auto;
4. if any other mode, **do not run** EXP424;
5. require exact `0546/count20` FC16 confirmation with `extraDeltaWords=0`;
6. restore the exact original mode immediately;
7. require exact rollback confirmation.

## Safety / abort

Expected temporary semantic effect: Auto <-> Compressor can change whether auxiliary heat is permitted and may briefly affect heating/hot-water behavior.

Abort on generic build failure, wrong page/count, missing exact confirmation, extra changed words, unexpected mode value, EXP420 no-owner, parser/resync/drop/peer fault or session degradation.

EXP424 introduces **no protocol/TX behavior change** versus EXP423; only experiment labels/status/build identification differ.

## Offline validation

- YAML parse PASS;
- undefined `id()` references: 0;
- UART write sites `63 -> 63`;
- ordered UART TX expressions identical to EXP423;
- hard-coded protocol literal sequence identical;
- generic `0546/count20` call preserved;
- `0553` word13 Operation Mode control preserved;
- Auto/raw1 and Compressor/raw2 mappings preserved;
- exact `0546` confirmation path and EXP420 owner preserved;
- ESPHome compile not run in assistant environment.

---

# 2026-10-05 — EXP423 PREPARED / NOT RUN — third generic page geometry validation

## Current experiment / status

- **EXP423 — PREPARED / NOT RUN** — live validation of the unchanged EXP421 generic desired-page TX core on `0442/count13`.
- **EXP422 — COMPLETE / POSITIVE** — generic helper live-confirmed on `042E/count15`.
- **EXP421 — COMPLETE / POSITIVE** — generic helper live-confirmed on `03E8/count14`.
- **EXP420 — COMPLETE / POSITIVE** — explicit config ACK ownership baseline.
- **EXP419 — COMPLETE / INCONCLUSIVE**.
- **EXP418 — COMPLETE / POSITIVE**.
- **EXP417 — COMPLETE / POSITIVE**.

## Hypothesis

The unchanged generic byte-level desired-page builder/TX primitive also preserves the already-proven `0442/count13` semantic write behavior.

## Baseline / target

- slave: `0x0F`;
- page: `0442/count13`;
- register: `044D`;
- page word: 11;
- local mapping: Cooling Room Hysteresis Low;
- source: EXP379 local XTR result;
- locally proven historical write: raw `10 -> 18 -> 10` = `1.0 -> 1.8 -> 1.0 °C`;
- latest known value before preparation: raw 10 / 1.0 °C, but EXP423 must use the fresh authoritative value after flash.

## Exact controlled change

Protocol/YAML behavior versus EXP422 is intentionally unchanged. EXP423 changes only experiment labelling, build identification and the Configuration validation-status entity.

The live action uses `04 Cooling | 06 Room Hysteresis Low`:
1. read authoritative current value `N`;
2. request `N+0.1 °C` if `N<5.0`, otherwise `N-0.1 °C`;
3. require exact `0442/count13` FC16 confirmation with `extraDeltaWords=0`;
4. restore exactly `N`;
5. require exact restoration confirmation.

## Safety / abort

Expected effect: cooling room-hysteresis-low shifts by 0.1 °C until rollback.

Plausible unintended effect: if the system is exactly at a cooling-control threshold, cooling behavior can differ slightly during the short test.

Abort on generic build failure, wrong page/count, missing exact confirmation, extra changed words, controller-retained original after semantic TX, EXP420 no-owner, parser/resync/drop/peer fault or session degradation.

If the forward write was confirmed, rollback only through the same proven `044D` path while the session is healthy.

## Offline validation

- YAML parse PASS;
- undefined `id()` references: 0;
- UART write sites remain `63 -> 63`;
- ordered UART write expressions identical to EXP422;
- hard-coded long protocol literal sequence identical;
- generic `0442/13` call site preserved;
- `044D` word11 scaling/range and exact confirmation path preserved;
- EXP420 `0442_EXP379` ownership preserved;
- obsolete EXP422 target-status entity removed;
- ESPHome compile not run in assistant environment.

---

# 2026-10-05 — EXP422 COMPLETE / POSITIVE — second generic page geometry live-confirmed on 042E/count15

## Current experiment / status

- **EXP422 — COMPLETE / POSITIVE** — the unchanged EXP421 generic desired-page builder/TX primitive is now live-confirmed on a second page geometry, `042E/count15`.
- **EXP421 — COMPLETE / POSITIVE** — generic helper live-confirmed on `03E8/count14`.
- **EXP420 — COMPLETE / POSITIVE** — explicit config ACK ownership baseline.
- **EXP419 — COMPLETE / INCONCLUSIVE**.
- **EXP418 — COMPLETE / POSITIVE**.
- **EXP417 — COMPLETE / POSITIVE**.

## Hypothesis

The same generic desired-page byte builder/TX primitive proven on `03E8/count14` preserves the already-proven `042E/count15` semantic write behavior.

## Controlled live action

Existing locally proven target:
- slave `0x0F`;
- page `042E/count15`;
- register `0433`;
- word 5;
- local mapping Startup HT / Opstart HT.

Authoritative starting value was 5. The controlled test changed `5 -> 6`, required exact controller confirmation, then restored `6 -> 5` and required exact rollback confirmation.

## Observed live result

### Forward 5 -> 6
- desired selector executed for `042E/count15`, `0433` word 5;
- controller pulled `FC03 042E/count15`;
- EXP421 generic helper emitted `GENERIC_PAGE_TX_EXECUTED page=042E count=15 frameLen=35 txCount=1`;
- controller republished `FC16 042E/count15` with word 5 = 6;
- `WRITE_CONFIRMED reg=0433 word=5 original=5 target=6 observed=6 extraDeltaWords=0`;
- EXP420 ownership identified the confirmation page as `042E_EXP378`.

### Rollback 6 -> 5
- the same generic helper emitted `GENERIC_PAGE_TX_EXECUTED page=042E count=15 frameLen=35 txCount=2`;
- controller republished `FC16 042E/count15` with word 5 restored to 5;
- `WRITE_CONFIRMED reg=0433 word=5 original=6 target=5 observed=5 extraDeltaWords=0`;
- HA authoritative Startup HT returned to 5.

## Integrity / safety result

After rollback:
- `genericTX=2`;
- `buildFail=0`;
- `lastPage=042E`;
- EXP420 `noOwner=0`;
- final visible heartbeat at ~175 s: `stage=40 unknown16=0 unknown03=0 peer17=0 peer16ack=0 resync=0 drops=0`;
- EXP418 remained balanced through 9/9 token set/consume;
- EXP417 suppressions remained 0;
- no EXP419 085F event.

## Conclusion

**EXP422 COMPLETE / POSITIVE.**

The shared EXP421 desired-page byte builder/TX primitive is now locally live-proven on two distinct page geometries:
- `03E8/count14`;
- `042E/count15`.

This materially strengthens the generic-core architecture. The remaining generic call-site geometries `0442/count13` and `0546/count20` are still only offline-equivalence checked under the shared helper, although both page-specific write paths were proven before the consolidation.

## Recommended next action

Prepare EXP423 as one more live geometry check on either `0442/count13` or `0546/count20`, using an already locally proven reversible setting and changing no parser/ACK/W4/session logic.

---

# 2026-10-05 — EXP422 PREPARED / NOT RUN — second generic page geometry validation

## Current experiment / status

- **EXP422 — PREPARED / NOT RUN** — live validation of the unchanged EXP421 generic desired-page TX core on a second page geometry, `042E/count15`.
- **EXP421 — COMPLETE / POSITIVE** — generic helper live-confirmed on `03E8/count14` with reversible `03F4 22 -> 23 -> 22`.
- **EXP420 — COMPLETE / POSITIVE** — explicit config ACK ownership baseline.
- **EXP419 — COMPLETE / INCONCLUSIVE**.
- **EXP418 — COMPLETE / POSITIVE**.
- **EXP417 — COMPLETE / POSITIVE**.

## Hypothesis

The unchanged generic byte-level desired-page builder/TX primitive from EXP421 also preserves the already-proven `042E/count15` semantic write behavior.

## Baseline / target

- slave: `0x0F`;
- page: `042E/count15`;
- register: `0433`;
- page word: 5;
- local mapping: Startup HT / Opstart HT;
- mapping/writeability source: EXP378 local XTR result;
- historical reversible example: `5 -> 7 -> 5`;
- EXP422 does not assume the current live value is still 5.

## Exact controlled change

Protocol/YAML behavior versus EXP421 is intentionally unchanged. EXP422 changes only experiment labelling, build identification and one Configuration diagnostic text sensor.

The live controlled action uses the existing `02 Heating | 20 Startup HT` control:
1. read authoritative displayed current value `N`;
2. request `N+1` if `N<30`, otherwise `N-1`;
3. require exact `042E/count15` FC16 confirmation with `extraDeltaWords=0`;
4. restore exactly `N`;
5. require exact restoration confirmation.

## Safety / abort

Expected effect: Startup HT timing changes by one minute until rollback.

Plausible unintended effect: timing behavior associated with Startup HT can differ briefly during the test.

Abort on generic build failure, wrong page/count, missing exact confirmation, extra changed words, controller-retained original after semantic TX, EXP420 no-owner, parser/resync/drop/peer fault or session degradation.

If forward change was confirmed, rollback only through the same proven `0433` path while the session is healthy.

## Offline validation

- YAML parse PASS;
- undefined `id()` references: 0;
- UART write sites remain `63 -> 63`;
- ordered UART write expressions are identical to EXP421;
- hard-coded long protocol literal sequence is identical;
- generic `042E/15` call site preserved;
- existing `0433` word5 control/range and exact confirmation path preserved;
- ESPHome compile not run in assistant environment.

---

# 2026-10-05 — EXP421 COMPLETE / POSITIVE — generic desired-page TX core live-confirmed on 03E8

## Current experiment / status

- **EXP421 — COMPLETE / POSITIVE** — shared desired-page builder/TX primitive is live-confirmed on the proven `03E8/count14` room-setpoint writer in both directions.
- **EXP420 — COMPLETE / POSITIVE** — explicit config ACK ownership baseline.
- **EXP419 — COMPLETE / INCONCLUSIVE**.
- **EXP418 — COMPLETE / POSITIVE**.
- **EXP417 — COMPLETE / POSITIVE**.

## Hypothesis

The existing production semantic writers can share one byte-level desired-page construction/TX primitive without changing page-specific guards, selectors, state transitions, confirmation or ACK ownership.

## Controlled change

No additional code change was made for this result. The previously prepared EXP421 build was exercised using the already-proven room-setpoint target `03F4` on `03E8/count14`:

- forward write: `22 -> 23`;
- exact controller confirmation required;
- rollback write: `23 -> 22`;
- exact controller confirmation required.

No other setting was intentionally changed.

## Observed live result

### Forward write 22 -> 23

- fresh authoritative `03E8/count14` page confirmed current room setpoint `22`;
- desired selector issued for `03F4`, word 12;
- controller pulled desired `03E8/count14`;
- EXP421 shared helper emitted `GENERIC_PAGE_TX_EXECUTED page=03E8 count=14 frameLen=33 txCount=1`;
- controller republished `03E8/count14` with room setpoint `23`;
- `WRITE_CONFIRMED writeNo=1 ... original=22 target=23 observed=23 extraDeltaWords=0`.

### Rollback 23 -> 22

- same generic path was exercised again;
- EXP421 emitted `GENERIC_PAGE_TX_EXECUTED page=03E8 count=14 frameLen=33 txCount=2`;
- controller republished `03E8/count14` with room setpoint `22`;
- `WRITE_CONFIRMED writeNo=2 ... original=23 target=22 observed=22 extraDeltaWords=0`.

## Integrity / safety result

After rollback:
- `genericTX=2`;
- `buildFail=0`;
- `lastPage=03E8`;
- `confirmedWrites=2`;
- cache restored to `03F4=22`;
- EXP420 remained `noOwner=0`;
- parser/peer integrity remained clean: `unknown16=0 unknown03=0 peer17=0 peer16ack=0 resync=0 drops=0`;
- EXP418 remained balanced `23/23`;
- EXP417 suppressions remained 0.

## Conclusion

**EXP421 COMPLETE / POSITIVE.**

The shared desired-page byte builder/TX primitive is now **locally live-proven on `03E8/count14`**, including a semantic write and exact rollback. This proves the refactor did not alter the observed `03E8` write semantics.

It does **not** yet independently live-prove the shared helper on the other three geometries `042E/15`, `0442/13`, and `0546/20`; their call sites were offline-equivalence checked and their ordinary current-sync paths remain healthy.

## Recommended next action

Prepare **EXP422** as a second-geometry live validation of the same generic helper using one already-proven reversible write on a non-`03E8` page. Change only that page/value, require exact FC16 confirmation and exact rollback, and keep parser/ACK/W4/approval logic unchanged.

---

# 2026-10-05 — EXP421 RUNNING / PARTIAL — smoke/non-regression passed, semantic TX branch unexercised

## Current experiment / status

- **EXP421 — RUNNING / PARTIAL** — generic desired-page transaction core is live and stable in retained runtime, but the generic semantic TX helper has not yet been exercised.
- **EXP420 — COMPLETE / POSITIVE** — explicit config ACK ownership baseline.
- **EXP419 — COMPLETE / INCONCLUSIVE**.
- **EXP418 — COMPLETE / POSITIVE**.
- **EXP417 — COMPLETE / POSITIVE**.

## Supplied live result

The supplied EXP421 log covers about 200 s after OTA.

Observed:
- successful API reconnect and immediate retained-runtime qualification;
- `stage=40`, `A80E=0000`, `A80F=000A`;
- startup/current synchronization completed normally for `042E/count15`, `0442/count13`, `0546/count20`, and `03E8/count14`;
- EXP420 recorded the expected four explicitly owned config ACKs;
- Configuration synchronized with local room setpoint `03F4=22` and writes were enabled;
- normal 0708 idle operation continued;
- EXP418 remained balanced at 9 token sets / 9 consumes with zero tokenless events;
- EXP417 double-valid suppression remained 0;
- EXP419 remained unexercised;
- no EXP420 no-owner event;
- no parser/peer/resync/drop regression;
- final visible heartbeat around 196 s remained clean with `runtimeFC16ACK=87 idle0708=46 unknown16=0 unknown03=0 peer17=0 peer16ack=0 resync=0 drops=0`.

EXP421-specific counters remained:
- `genericTX=0`;
- `buildFail=0`;
- `lastPage=0000`;
- `semanticResponses=0`;
- `confirmedWrites=0`.

Therefore the generic desired-page builder/TX path was **not exercised** in this run.

## Result interpretation

This is a **positive live smoke/non-regression result**, not completion of EXP421.

The experiment remains **RUNNING / PARTIAL** because its key positive criterion still requires one already-proven reversible `03E8` write to traverse `GENERIC_PAGE_TX_EXECUTED page=03E8 count=14` and receive exact controller FC16 confirmation, followed by the reverse write and confirmation.

## Next action

Using the already-proven room-setpoint control:
1. change `03F4` / room setpoint `22 -> 23`;
2. wait for exact controller confirmation;
3. change `23 -> 22`;
4. wait for exact controller confirmation;
5. return the log covering both directions.

Abort on generic build failure, config no-owner event, missing exact FC16 confirmation, parser/resync/drop regression or session degradation.

---

# 2026-10-05 — EXP421 PREPARED / NOT RUN — generic desired-page transaction core

## Current experiment / status

- **EXP421 — PREPARED / NOT RUN** — structural consolidation of the four existing production semantic desired-page transmitters into one generic FC03 page builder/TX primitive.
- **EXP420 — COMPLETE / POSITIVE** — explicit config ACK ownership baseline.
- **EXP419 — COMPLETE / INCONCLUSIVE**.
- **EXP418 — COMPLETE / POSITIVE**.
- **EXP417 — COMPLETE / POSITIVE**.

## Hypothesis

The existing `03E8/count14`, `042E/count15`, `0442/count13`, and `0546/count20` semantic writers can share the byte-level desired-page construction/TX core without changing page-specific guards, state transitions, confirmation rules, selectors or ACK ownership.

## Exact controlled change

EXP421 centralizes only:
- FC03 response byte-count construction;
- full cached-page serialization;
- exactly one selected-word substitution;
- Modbus CRC16 calculation;
- response hex rendering;
- the existing DE-on / 1000 us / UART TX / flush / 1000 us / DE-off sequence.

The individual page engines still own validation, cache freshness, semantic response budget, selector state, state transitions, confirmation, extra-delta checks, HA/UI rollback and ACK ownership.

No new register, selector, desired value, ACK rule, parser rule, recovery/approval behavior or semantic write target is introduced.

## Offline validation

- YAML parse PASS;
- undefined `id()` references: 0;
- UART `write_array()` call sites reduce **66 -> 63** exactly because four duplicated desired-page TX sites collapse into one shared TX helper;
- the four generic call sites are exactly `042E/15`, `0442/13`, `0546/20`, and `03E8/14`;
- all 58 existing named static `uint8_t` protocol arrays are byte-for-byte unchanged;
- 2000 randomized desired-page constructions across the four page geometries were byte-identical to the EXP420 construction algorithm;
- no ESPHome compile is claimed; the ESPHome CLI is unavailable in the working environment.

## Live positive criteria

1. retained `stage=40` and production startup/current sync remain healthy;
2. no EXP420 no-owner event or parser/peer/resync/drop regression;
3. one already-proven `03E8` write and reverse write produces an EXP421 `GENERIC_PAGE_TX_EXECUTED page=03E8 count=14` log and exact controller FC16 confirmation both directions;
4. `EXP421 Generic Build Failures` remains zero.

## Abort / recovery

Any generic-build failure, semantic write mismatch, session degradation or parser/integrity regression -> revert to EXP420. EXP421 adds no new write target.

---

# 2026-10-05 — EXP420 COMPLETE / POSITIVE — generic config ACK ownership hardening

## Current experiment / status

- **EXP420 — COMPLETE / POSITIVE** — broad known-config page-shape ACK authorization was replaced by explicit ownership without observed regression.
- **EXP419 — COMPLETE / INCONCLUSIVE** — 085F target branch remained unexercised.
- **EXP418 — COMPLETE / POSITIVE** — 0870 one-shot ownership-token hardening.
- **EXP417 — COMPLETE / POSITIVE** — FC03 double-valid-prefix parser hardening.

## EXP420 hypothesis

A known stage40 config-page address/count shape must not by itself authorize an FC16 ACK. Production/config ACKs should require an explicit owner captured before page handlers mutate state.

## Controlled change

Explicit owners were preserved for:
- production `03E8/count14`, `042E/count15`, `0442/count13`, `0546/count20` flows;
- evidence-backed autonomous idle `03E8/count14`;
- exact EXP410 calendar ownership states/pages;
- ordered export-resume with the existing exact-order checker.

Other known config-family pages in normal retained runtime are capture-only / NO_ACK.

No new TX frame, selector, CRC, timing, W4 behavior, semantic writer, approval path, parser rule, EXP418 ownership rule or EXP419 rule was introduced.

## Live result

The supplied log is a late retained-runtime slice from the same EXP420 boot, spanning about 6483 s to 6770 s runtime age.

Observed:
- `stage=40` remained qualified throughout;
- EXP420 status was already `ownedACK=4 noOwner=0 autonomous03E8=0` at the start of the supplied slice and remained unchanged to the end;
- no `EXP420_CONFIG_NO_OWNER` event occurred;
- the supplied 5-minute slice contained 122 stage40 FC16 publications, all runtime-service pages and no config-family page;
- final retained-runtime counters remained clean: `unknown16=0 unknown03=0 peer17=0 peer16ack=0 resync=0 drops=0`;
- final runtime heartbeat was approximately 6767 s with `runtimeFC16ACK=2844`, `idle0708=1578`, `rt085F=0`;
- EXP418 remained clean and advanced to `set=316 consumed=316 noToken=0 bypass=0`;
- EXP417 suppression remained 0;
- EXP419 remained unexercised (`085F` seen/ACK/no-context counters all zero);
- no semantic write was performed in this observation slice.

The four EXP420 owned-ACK counts occurred earlier in the same boot and are consistent with the four production startup/current sync pages. The supplied slice does not contain those earlier per-page owner log lines, so the exact four owner labels are not independently re-read from this attachment.

**Result:** **COMPLETE / POSITIVE** for the stated ACK-hardening hypothesis and retained-runtime non-regression.

## Strong conclusion

On this local XTR M, broad page-shape-only authorization is no longer needed for the currently exercised config path. Explicit config ownership can remain as the production baseline without disturbing long-running retained runtime.

## Remaining limits

- autonomous idle `03E8` ownership was not exercised in this supplied slice;
- no unowned config page occurred, so the NO_ACK discrimination branch remains unexercised;
- EXP419 085F context remains open;
- recovery/rejoin and cold native approval remain separate validation tracks.

## Recommended next action

Stop broadening ACK hardening for now. The next higher-value step is to consolidate the proven per-page read/write transactions into a generic page transaction engine while keeping the current fail-closed ownership rules intact.

---

# 2026-10-05 — EXP420 PREPARED / NOT RUN — generic config ACK ownership hardening

## Current experiment / status

- **EXP420 — PREPARED / NOT RUN** — stage40 known-config FC16 ACKs are changed from broad page-shape authorization to explicit ownership captured at frame arrival.
- **EXP419 — COMPLETE / INCONCLUSIVE** — no 085F target page appeared; ordinary retained-runtime non-regression passed.
- **EXP418 — COMPLETE / POSITIVE**.
- **EXP417 — COMPLETE / POSITIVE**.

## EXP420 hypothesis

A known config page shape must not by itself authorize a runtime FC16 ACK. ACK permission should come from an explicit active owner.

## Controlled change

Explicit owners are retained for:
- production `03E8/count14` current/autosync and semantic-confirm flows;
- evidence-backed autonomous idle `03E8/count14`;
- production `042E/count15`, `0442/count13`, and `0546/count20` current/confirm flows;
- the exact existing EXP410 calendar states and pages;
- ordered export-resume, with the existing exact-order checker unchanged.

Any other known config-family page in normal retained runtime is capture-only / NO_ACK and increments an EXP420 diagnostic counter.

No new TX frame, selector, CRC, timing, W4 behavior, semantic write, approval path, parser rule, EXP418 ownership rule, EXP419 rule, 04A6 policy, or 0834 policy is introduced.

## Offline validation

- YAML parse PASS;
- undefined `id()` references: 0;
- UART `write_array()` sites remain 66 -> 66;
- ordered UART write expressions are identical to EXP419;
- existing hard-coded long-hex protocol literals are identical;
- replay of the supplied EXP419 run found exactly four config publications (`042E`, `0442`, `0546`, `03E8`), all four with their explicit owner markers present.

## Safety / abort

If an unowned config page appears, EXP420 logs `EXP420_CONFIG_NO_OWNER ... NO_ACK` and does not auto-broaden the rule. Repeated retries, failed production sync, session degradation or parser/write regression require reverting to EXP419.

---

# 2026-10-05 — EXP419 COMPLETE / INCONCLUSIVE — retained-runtime 085F context hardening

## Current experiment / status

- **EXP419 — COMPLETE / INCONCLUSIVE** — target 085F branch was not exercised; ordinary retained-runtime non-regression passed.
- **EXP418 — COMPLETE / POSITIVE** — 0870 one-shot ownership-token hardening.
- **EXP417 — COMPLETE / POSITIVE** — FC03 double-valid-prefix parser hardening.

## EXP419 hypothesis

In stable retained runtime, a known `085F/count5` payload should not by itself authorize an ACK. Only explicit fresh-approval/recovery/hot-rejoin/resume contexts retain ACK permission.

## Live result

The supplied EXP419 run covered about 180 s after OTA.

Observed:
- successful ESP/API reconnect and immediate retained-runtime qualification;
- `stage=40`, `A80E=0000`, `A80F=000A`;
- production startup/current synchronization remained healthy;
- `03E8/count14` configuration autosync completed and writes were enabled;
- normal `0708` idle responses continued;
- EXP418 ownership remained healthy, reaching 9 token sets / 9 token consumes, with 0 tokenless 0870 and 0 bypasses;
- EXP417 double-valid suppression remained 0;
- final heartbeat remained clean:
  `stage=40 runtimeFC16ACK=80 idle0708=42 rt085F=0 unknown16=0 unknown03=0 peer17=0 peer16ack=0 resync=0 drops=0`;
- **no `085F/count5` appeared at all**;
- EXP419 counters therefore remained:
  `zeroSeen=0 0800Seen=0 contextACK=0 noContext=0`.

**Result:** **COMPLETE / INCONCLUSIVE** for the 085F-context hypothesis.

**Positive side result:** no regression is visible in ordinary retained runtime, production synchronization, EXP417 parser hardening or EXP418 0870 ownership.

**Limitation:** because the target page never appeared, this run gives no live evidence about whether withholding a known but contextless 085F ACK is correct.

## Next step

Do not broaden or promote the EXP419 085F predicate. Either wait for a naturally occurring 085F/recovery context, or move to the separate generic known-config ACK ownership hardening track while preserving EXP419 as an unexercised fail-closed rule.

---

# 2026-10-05 — EXP419 PREPARED / NOT RUN — retained-runtime 085F ACK-context hardening

## Current experiment / status

- **EXP419 — PREPARED / NOT RUN** — known `085F/count5` payload is no longer sufficient by itself for ACK permission in stable retained runtime.
- **EXP418 — COMPLETE / POSITIVE** — `0870/count17` one-shot ownership-token hardening.
- **EXP417 — COMPLETE / POSITIVE** — FC03 double-valid-prefix parser hardening.

## EXP419 hypothesis

In stable retained runtime, known `085F/count5` payload shape alone is not sufficient ACK authorization.

The two locally known payload forms remain recognized:
- `0000 0000 0000 0000 0000`;
- `0000 0000 0800 0000 0000`.

EXP419 ACKs them only when an already-explicit session context is active:
- a fresh native approval was transmitted in this ESP session;
- controller recovery is in progress;
- hot-rejoin is in progress / waiting for runtime qualification;
- ordered export-resume is active.

In ordinary retained runtime with none of those owners, a known 085F is capture-only / NO_ACK.

## Baseline evidence

- EXP302 locally proved that ACK of repeated `085F(0861=0800)` can change retained controller state.
- EXP307 locally proved that a qualified all-zero 085F ACK can advance into known runtime.
- EXP305 showed 085F can occur downstream of an ACK-gated retained transfer.
- Genuine/offline evidence shows 085F is context-sensitive and often present without ACK; page recognition and ACK permission must remain separate.
- EXP418 supplied run contained zero stage40 085F publications, so replay predicts no behavior change on that ordinary retained-runtime trace.

## Exact controlled change

- remove `local_085f_known` from unconditional runtime ACK permission;
- replace it with explicit context-owned 085F authorization;
- known 085F with no context -> log `EXP419_085F_NO_CONTEXT`, capture-only / NO_ACK;
- unknown 085F payload -> existing fail-closed STOP remains unchanged;
- EXP418 0870 token creation from all-zero 085F remains possible only after an actual 085F ACK.

No TX frame/CRC/timing, parser, 0870 ownership, 0708/W4, config ACK, semantic writer, approval implementation, recovery state machine or 0834 policy is intentionally changed.

## Offline validation

- YAML parse PASS;
- zero undefined `id()` references;
- UART `write_array()` sites unchanged: 66 -> 66;
- ordered UART TX expressions identical to EXP418;
- existing hard-coded long protocol literals unchanged;
- EXP418 supplied trace contains zero stage40 `085F/count5`, so the new target branch is not exercised by replay.

## Result criteria

**Positive:** ordinary retained runtime remains healthy and any 085F ACK that occurs is explicitly context-owned.

**Negative/discrimination:** a known 085F appears in stable retained runtime and is withheld. If it repeats or session health degrades, record that result and revert to EXP418 rather than broadening the rule.

**Inconclusive:** no 085F appears during an otherwise healthy run; this proves only non-regression of ordinary runtime, not the 085F target branch.

**Recovery:** revert to EXP418. EXP419 changes no Thermia setting.

---

# 2026-10-05 — EXP418 COMPLETE / POSITIVE — 0870 ownership hardening

## Current experiment / status

- **EXP418 — COMPLETE / POSITIVE** — normal-runtime `0870/count17` ACK ownership hardened from page-shape-only to one-shot session-token authorization.
- **EXP417 — COMPLETE / POSITIVE** — FC03 double-valid-prefix parser hardening, including live bidirectional `03F4` write regression.

## EXP418 hypothesis

Normal-runtime `0870/count17` should be ACKed only when owned by a one-shot session token created after an actually executed ACK of either:
- qualified all-zero `085F/count5`; or
- qualified `0864/count4`.

Ordinary `0708` preserves the token. The first normal-runtime `0870` ACK consumes it. Existing explicit recovery/rejoin contexts remain separate passthrough authorization branches.

## Controlled change

- removed `0870/count17` from the unconditional runtime ACK whitelist;
- added one-shot ownership token and diagnostics;
- tokenless normal-runtime `0870` is capture-only / NO_ACK;
- no parser, 085F payload recognition, W4, 0708 words, generic config ACK policy, semantic writer, approval/bootstrap/recovery state-machine, frame, CRC, timing or DE behavior was intentionally changed.

## Live result

The supplied EXP418 log is a late retained-runtime slice beginning after approximately 2069 s uptime and ending near 2378 s.

Observed in that slice:
- retained runtime stayed at `stage=40`;
- 15 `0864/count4` publications were ACKed and each set one EXP418 token;
- 15 `0870/count17` publications followed and each consumed exactly one token;
- token counters advanced from 96/96 at the start of the supplied slice to 111/111;
- **0 tokenless 0870 captures**;
- **0 recovery/rejoin bypasses**;
- `rt085F=0` in this slice, so all observed token creation here came from `0864`;
- EXP417 double-valid suppression remained 0;
- no semantic write was performed in this EXP418 observation slice;
- final heartbeat remained clean:
  `stage=40 unknown16=0 unknown03=0 peer17=0 peer16ack=0 resync=0 drops=0`.

**Result:** **COMPLETE / POSITIVE** for the normal-runtime ownership-hardening hypothesis.

## Interpretation

Locally on this XTR M, the hardened rule is now live-compatible over the observed retained-runtime sequence: every observed normal-runtime `0870/count17` had an unconsumed prior token and the one-shot token was consumed exactly once when its ACK was sent.

This does **not** prove that the token is universally necessary for every possible 0870 context. EXP309/310 still prove that 0864 specifically is not mandatory because qualified all-zero 085F can also precede a valid 0870. Recovery/rejoin authorization remains a separate open context.

## Next engineering step

Keep ACK hardening isolated. The next candidate is the remaining **085F / generic config ACK context authorization debt**, not additional 0870 broadening.

---

# 2026-10-05 — EXP418 PREPARED / NOT RUN — 0870 ACK ownership hardening

## Current experiment / status

- **EXP418 — PREPARED / NOT RUN** — normal-runtime `0870/count17` ACK ownership hardening.
- **EXP417 — COMPLETE / POSITIVE** — FC03 double-valid-prefix parser hardening, including live bidirectional `03F4` write regression.

## EXP418 hypothesis

Normal-runtime `0870/count17` should be ACKed only when owned by a one-shot session token created after an actually executed ACK of either:
- qualified all-zero `085F/count5`; or
- qualified `0864/count4`.

Ordinary `0708` traffic preserves the token. The first normal-runtime `0870` ACK consumes it.

Existing explicit recovery/rejoin contexts are intentionally passed through unchanged:
- controller recovery in progress;
- hot-rejoin waiting for runtime;
- ordered export-resume runtime interleave.

## Controlled change

- remove `0870/count17` from the unconditional runtime ACK whitelist;
- add the one-shot ownership token and diagnostics;
- tokenless normal-runtime `0870` becomes capture-only / NO_ACK and is logged as EXP418 negative evidence;
- do not alter parser logic, 085F payload recognition, W4, 0708 words, generic config ACK policy, semantic writers, approval/bootstrap/recovery state machines or TX frame construction.

## Offline validation

- YAML parse PASS;
- undefined `id()` references: 0;
- UART `write_array()` sites unchanged: 66 -> 66;
- ordered UART write expressions unchanged;
- existing long hexadecimal protocol literals unchanged;
- replay of the supplied EXP417 long run: 137 stage40 FC16 publications, 15 token-source `0864` events, 15 `0870/count17` publications, **15/15 authorized, 0 withheld** under the EXP418 rule.

## Positive / negative / abort

**Positive:** retained runtime remains healthy and ordinary `0870` ACKs are preceded by a valid token source and consume exactly one token.

**Negative / discrimination:** a normal-runtime `0870` appears with no token. It must be captured with NO_ACK; do not broaden the rule in the same experiment.

**Abort:** repeated tokenless 0870 retries, session degradation/loss, parser resync/drop, or production write regression. Revert to EXP417; no Thermia setting rollback is required.

---

# 2026-10-05 — EXP417 strengthened by live semantic-write regression

EXP417 remains **COMPLETE / POSITIVE**.

Additional local XTR runtime evidence now confirms that the FC03 double-valid-prefix hardening does not break the existing proven semantic write path:

- retained runtime stayed at `stage=40`;
- room setpoint `03F4` was changed `22 -> 23` through the normal selector / desired-page / FC16-confirm flow;
- the controller republished `03E8/count14` with the requested value and the transaction closed READY with exactly one semantic page response and zero extra delta words;
- the setting was then changed back `23 -> 22` through the same path and again controller-confirmed;
- the later heartbeat remained clean with `unknown16=0`, `unknown03=0`, `peer17=0`, `peer16ack=0`, `resync=0`, `drops=0`;
- the EXP417 double-valid suppression counter remained zero throughout the supplied ~10 minute retained-runtime observation.

**Conclusion:** EXP417 is now live-regression-tested not only against normal read/runtime traffic but also against a complete proven one-word semantic write and reverse write. This still does not prove that a naturally occurring double-valid frame exists on the bus; the ambiguity itself remains a defensive parser hardening case demonstrated offline.

---

# 2026-10-05 — CANONICAL RECONCILIATION — EXP411–416

**Authoritative status:** this section supersedes older current-state summaries below where they conflict.

## Current experiment / status

- **EXP416 — COMPLETE / POSITIVE** — structural cleanup pass 2 live-smoke-tested successfully.
- **EXP415 — COMPLETE / POSITIVE** — structural cleanup pass 1 live-smoke-tested successfully.
- **EXP414 — RUNNING / PARTIAL historically** — capture-only natural `0532/count18` observer; no natural page observed in the supplied retained-runtime logs.
- **EXP413 — COMPLETE / INCONCLUSIVE** — bounded current-only identity-page request did not produce `0532/count18` within the discrimination window.
- **EXP412 — PREPARED / NOT RUN** — manual UI correlation requires physical heat-pump access.
- **EXP411 — COMPLETE / INCONCLUSIVE** — a firmware-derived native approval implementation was prepared, but retained runtime produced no fresh controller challenge.

## Confidential native approval finding

Thermia Connect firmware analysis established the native approval mechanism and genuine capture evidence independently verified it.

**Security-sensitive approval parameters, capture fixtures and working implementation details are confidential and are intentionally not stored in this repository.**

Evidence status:
- **PROVEN / firmware-derived:** native approval mechanism recovered.
- **PROVEN / genuine Online/DCM capture:** recovered mechanism verified against genuine traffic.
- **OPEN / local XTR live:** acceptance during a fresh local controller challenge has not yet been exercised.

## Local XTR identity / firmware findings

- **PROVEN / locally observed:** `0867=242`, decoded by the vendor firmware formula as CM firmware **2.4.2**.
- Additional repeatedly observed local raw values: `07DC=30`, `07E8=2410`, `07E9=2201`, `07EA=2501`, `07EB=1301`, `0816=0`.
- `0539` configured product code remains **OPEN / UNKNOWN** locally.
- Firmware-derived XTR M codes are 22 for 1N and 23 for 3N; this has not yet been locally read from `0539`.

## EXP415 / EXP416 cleanup result

Both cleanup passes were designed as zero-bus-behaviour changes and preserved the existing production/session paths.

Live validation showed:
- retained `stage=40`;
- `A80E=0000`, `A80F=000A`;
- normal runtime FC16 page flow and ACKs;
- successful startup/current synchronization for `042E/count15`, `0442/count13`, `0546/count20`;
- successful automatic `03E8/count14` configuration refresh;
- minimal zero-W4 `0708` idle replies continued;
- clean integrity counters with no parser resync/drop or peer responder activity in the supplied windows;
- no semantic setting write was triggered by either cleanup experiment.

## Current strongest hypotheses / unknowns

1. `0532/count18` appears context-sensitive rather than a normal retained-runtime publication.
2. W4 remains service/work metadata whose exact local lifecycle is not yet proven.
3. Fresh local native-approval acceptance remains open because no fresh challenge has been seen.
4. Parser ambiguity hardening from PROTO-OFFLINE-63 is now a higher-value next engineering step than another small cleanup.

## Safety constraints

- Do not broaden fresh-session eligibility based only on retained runtime.
- Do not infer new desired selectors from W4 or current-selector symmetry.
- Keep `0834` capture-only.
- Do not combine W4 emulation, approval testing, parser hardening and semantic writes in one experiment.
- Confidential native-approval implementation details must not be committed to a public repository.

---

# 2026-10-04 — CANONICAL RECONCILIATION — calendar writer through EXP404

**Authoritative status:** this section supersedes older live/calendar summaries below where they conflict. Historical sections remain unchanged.

## Current live XTR status

- **EXP404 — COMPLETE / POSITIVE** — F1 slot0 validity metadata write proven locally on `05BA bit0`; controller confirmed `0000 -> 0001` with exactly one changed word and automatic rollback restored the exact original `059C/count33` page.
- **EXP405 — PREPARED / NOT RUN** — bounded inactive-slot two-word content test: `055B` start minute +1 and `0560` stop minute +1 in one `055A/count33` desired-page response, only while `05BA bit0=0`, followed by exact rollback.
- **EXP403 — COMPLETE / POSITIVE** — `W0 bit3 + W2 bit3` locally proven as desired selector for `059C/count33`; exact no-op 059C response accepted with no FC03 retry.
- **EXP402 — COMPLETE / POSITIVE** — `W2 bit3` alone locally proven as CURRENT selector for `059C/count33`.
- **EXP401 — COMPLETE / POSITIVE** — first locally proven semantic calendar-content write: `055B` start minute `0 -> 1`, exact FC16 confirmation, exact rollback.
- **EXP400 — COMPLETE / POSITIVE** — exact no-op desired response on `055A/count33` accepted; no FC03 retry; exact same-page FC16 observed.
- **EXP399 — COMPLETE / POSITIVE** — `W0 bit1 + W2 bit1` locally proven as desired selector for `055A/count33`. Its operational side effect/session loss was later recovered after controller restart; challenge-response itself remains unsolved.

## Current protocol model — calendar writer

The local XTR M now proves both content-page and metadata-page native desired transactions.

### F1 content page

Current selector:
`W2 bit1 -> FC16 055A/count33` — PROVEN.

Desired selector:
`W0 bit1 + W2 bit1 -> FC03 055A/count33` — PROVEN.

Accepted desired-page transaction:
`0708 selector -> FC03 055A/33 -> full 33-word response -> FC16 055A/33 confirmation`.

Locally proven semantic mutation:
- `055B` / slot0 word1 / start minute — writable and rollbackable.

### F1 metadata page

Current selector:
`W2 bit3 -> FC16 059C/count33` — PROVEN.

Desired selector:
`W0 bit3 + W2 bit3 -> FC03 059C/count33` — PROVEN.

Locally proven semantic mutation:
- `05BA bit0` — F1 slot0 validity; writable `0 -> 1` and rollbackable `1 -> 0`.

### Full F1 current refresh

`W2=000E` produces `055A/33 + 057B/33 + 059C/33`, yielding 98 F1 words as 33+33+32 logical words. The final word of the physical 059C page belongs to the next logical region and is excluded from F1.

## Locally proven calendar findings

- F1 corresponds to **WW_GEBLOKKEERD / Hot Water Blocked**.
- F1 contains eight 12-word slot records plus two metadata words.
- `05BA bit0` controls validity of F1 slot0.
- slot0 word1 is start minute.
- slot0 word3 is start day.
- slot0 word8 is stop day.
- slot0 word11 is weekday/recurrence mask; exact day-bit identity is not fully resolved.
- A full desired-page response may contain an intended semantic delta; controller republishes the accepted page via FC16.
- Exact no-op desired responses are accepted locally on both 055A and 059C.

## Strong conclusions

1. Calendar write access is no longer hypothetical on this XTR M.
2. The native Online/DCM path is a page-image synchronization mechanism, not direct register writes.
3. Both schedule content and slot-validity metadata are locally writable through controller-owned FC03 pulls.
4. Safe writer design should keep a fresh authoritative page image, mutate only intended words, require exact FC16 confirmation, and use exact rollback when experimenting.
5. No generalized writer for all F1 slots or F2/F3/F4 is proven yet.

## Strongest remaining calendar unknowns

- whether coherent multi-word slot content is accepted in one 055A desired response;
- whether complete slot preparation plus later validity activation behaves atomically enough for production use;
- exact weekday bit order;
- mode field semantics and recurrence/date interaction;
- desired selectors for 057B and the remaining calendar pages;
- F2/F3/F4 local semantic confirmation;
- persistence semantics across restart and UI edits;
- cross-model compatibility of the XTR selector/write behavior.

## Next experiment

**EXP405 — PREPARED / NOT RUN**

Hypothesis: while slot0 remains invalid, a coherent two-word time-window mutation is accepted in one 055A desired transaction.

Controlled mutation:
- `055B` start minute: +1
- `0560` stop minute: +1
- no wrap; both originals must be <=58
- `05BA bit0` must remain clear
- exact rollback required

Success requires exactly two expected deltas, zero unexpected deltas, and exact original-page restoration.

## Safety constraints

- Do not mark EXP405 complete until its live result is supplied.
- Keep slot validity clear during EXP405.
- If a semantic write is confirmed but rollback is not confirmed, stop further calendar experiments.
- Unexpected FC03/config traffic remains capture-only.
- Do not extrapolate untested W0 bits or desired selectors by symmetry alone.
- Challenge-response remains OPEN.
- `0834` remains capture-only.
- Production settings functionality and known-good ACK paths must remain unchanged.

---

# 2026-10-04 — CANONICAL RECONCILIATION — offline tracks through PROTO-OFFLINE-64

**Authoritative status:** this section supersedes older offline/current-state summaries below where they conflict. Historical sections remain unchanged.

## Current live XTR status — unchanged

- **EXP387 — COMPLETE / POSITIVE**
- **EXP388 — RUNNING / PARTIAL** — repeated controller-restart recovery succeeded twice without ESP reboot; pre-semantic cancellation and refresh-only cancellation remain not independently live-exercised.
- **EXP383 — PREPARED / NOT RUN**
- **PROTO-OFFLINE-61..64 do not advance live experiment state.**

## New offline results

- **PROTO-OFFLINE-61 — COMPLETE / POSITIVE WITH THREE KNOWN ACK-POLICY DEVIATIONS** — 58/58 explicit v4.1 UART TX sites are accounted for by six known route classes. No unmodeled semantic TX route exists. Remaining source/model gaps are the already-known broader ACK permissions for 085F, 0870, and generic known-config pages.
- **PROTO-OFFLINE-62 — COMPLETE / POSITIVE** — source-transcribed host decision logic passes **4630/4630 checks**, including golden evidence, representative fault cases, selector/page guards, all 4,608 EXP388 recovery-state combinations, and PROTO57 sole-owner reachability.
- **PROTO-OFFLINE-63 — COMPLETE / POSITIVE FOR RESYNC ROBUSTNESS WITH PARSER AMBIGUITY** — 60,000 broad fuzz cases plus 100,000 non-semantic targeted controls; targeted controls produced **0 accidental semantic-request outputs**. Deterministic constructions nevertheless prove that a longer valid FC03 response can contain an 8-byte CRC-valid prefix that the current shortest-first assembler accepts as an exact semantic FC03 request. Constructions were found for 0546, 042E, and 0442.
- **PROTO-OFFLINE-64 — COMPLETE / POSITIVE** — a cleanup/rebuild map classifies 28 current components into KEEP / MERGE / MOVE-TO-TEST-HARNESS / REMOVE-OR-REVIEW.

## Current protocol/safety additions

1. Every explicit v4.1 UART TX site maps to a known protocol route class; no hidden semantic TX path was found.
2. The host-side decision transcription reproduces current regression expectations, but is not compiled ESPHome proof.
3. CRC validity plus shortest-candidate selection is not a unique request/response discriminator. Future parser hardening should use transaction/session context or fail closed on double-valid candidates.
4. No genuine Thermia frame is currently known to trigger the PROTO63 ambiguity; treat it as defensive parser hardening, not an observed live write.
5. Do not combine EXP388 recovery restructuring with 0870, 085F, generic-config ACK hardening, or parser replacement in the same live experiment.
6. Any rewrite must preserve delayed-refresh state, integrity counters, autonomous 03E8 handling, both locally proven 085F payload forms, and direct 0870 behavior without mandatory 0864.

## Recommended next sequence

1. Keep v4.1 behavior unchanged until an explicitly prepared live experiment.
2. Rebuild EXP388 only around recovery/state instrumentation and deterministic cancellation testing.
3. Carry parser ambiguity as a separate hardening item.
4. After EXP388, test 0870 context hardening separately.
5. Run PROTO54/60/61/62/63 offline gates before future live refactors.

## Safety constraints retained

- No new desired selector is authorized.
- 0834 remains capture-only.
- Do not require 0864 before every 0870.
- Do not reduce config ACK ownership to W2/W3 only.
- Do not remove either locally proven 085F payload form.
- **EXP388 remains RUNNING / PARTIAL.**
- Write Beta v4.1 is unchanged by PROTO61..64.

---

# 2026-10-04 — CANONICAL RECONCILIATION — offline tracks through PROTO-OFFLINE-60

**Authoritative status:** this section supersedes older offline/current-state summaries below where they conflict. Historical sections remain unchanged.

## Current live XTR status — unchanged

- **EXP387 — COMPLETE / POSITIVE** — last fully completed local XTR experiment.
- **EXP388 — RUNNING / PARTIAL** — repeated controller-restart recovery succeeded twice without ESP reboot. The pre-semantic cancellation and refresh-only cancellation branches remain not independently live-exercised.
- **EXP383 — PREPARED / NOT RUN** — historical TEST-candidate bundle remains unpromoted except where later experiments separately established a target.
- **PROTO-OFFLINE-45..60 do not advance live experiment state.**

## Offline state through PROTO-OFFLINE-60

- **PROTO-OFFLINE-45 — COMPLETE / POSITIVE WITH MODEL REFINEMENTS** — executable replay across seven genuine Online/DCM captures plus one local passive XTR trace reproduces approval, ordered bootstrap, runtime grammar, desired pulls and recovery/rejoin. Approval and retained service/config traffic can overlap; genuine legacy standalone config pushes and genuine ATEC steady-state 085F ACK show that one strictly linear protocol enum is too coarse.
- **PROTO-OFFLINE-46 — COMPLETE / POSITIVE WITH THREE BROAD ACK SURFACES CONFIRMED** — 29 valid-CRC synthetic faults show semantic write paths fail closed. Remaining broad authorization surfaces are known 085F, 0870 and generic known-config ACKs.
- **PROTO-OFFLINE-47 — COMPLETE / POSITIVE** — local XTR page geometry aligns with modern Eco5 at the known count-drift pages 03E8/0410/0492/051E. Local XTR 03F3=1 and 03F5=2 align structurally with the modern family; semantics remain OPEN.
- **PROTO-OFFLINE-48 — COMPLETE / NEGATIVE FOR NEW SEMANTIC PROMOTIONS** — unresolved settings fields lack useful edges in the current corpus. 087D +1 edges are reconfirmed only while compressor-running is active; no new user-facing register labels are promoted.
- **PROTO-OFFLINE-49 — COMPLETE / POSITIVE AS PRIORITIZATION ARTIFACT** — no new W0/W1 selector is proven. Unproven selectors remain DENY-BY-DEFAULT; ranking is planning guidance only.
- **PROTO-OFFLINE-50 — COMPLETE / POSITIVE FOR HISTORY LIFECYCLE** — 0884/count60 is a periodically republished newest-first history snapshot, not merely a one-shot new-alarm event. Raw event-ID semantics remain OPEN.
- **PROTO-OFFLINE-51 — COMPLETE / POSITIVE STRUCTURAL RECONFIRMATION** — ATEC calendar words 0..391 match the legacy reference; only tail register 06E2 differs. The 06E2..06E5 tail is further separated from F1..F4 calendar state. No new calendar desired-pull evidence.
- **PROTO-OFFLINE-52 — COMPLETE / INCONCLUSIVE FOR BINARY RECOVERY; POSITIVE FOR TARGET REFINEMENT** — current app target is MyThermia while Android package identity remains `se.thermia.online2`; OnSite remains `com.thermia.onsite`. No APK/XAPK, Connect firmware, protocol package or DCM03 binary was recovered.
- **PROTO-OFFLINE-53 — COMPLETE / POSITIVE WITH DEFENSIVE-INVARIANT DEBT IDENTIFIED** — exhaustive Cartesian state/permission analysis exposes mixed semantic-owner combinations only when impossible states are injected.
- **PROTO-OFFLINE-54 — COMPLETE / POSITIVE** — eight captures are now a deterministic golden-trace regression suite; **72/72 assertions pass**.
- **PROTO-OFFLINE-55 — COMPLETE / POSITIVE** — differential ACK-policy replay shows 0870 is the cleanest hardening target. A recent-mailbox-only 3 s candidate yields TP=63, FP=0, TN=31, FN=1; simple 085F/config ownership rules over-block genuine traffic.
- **PROTO-OFFLINE-56 — COMPLETE / POSITIVE** — XTR-only reduction proves both accepted 085F payload forms are locally ACKable in qualified contexts, proves direct local 0870 can occur without 0864, and confirms qualified local 0870 ACK advances runtime.
- **PROTO-OFFLINE-57 — COMPLETE / POSITIVE** — corrected forward reachability with the EXP387 delayed-rearm substate reaches **115 semantic-capable variants, 0 multi-owner states, 0 reachable PROTO53 conflict projections and 0 unsafe semantic pre-events**.
- **PROTO-OFFLINE-58 — COMPLETE / POSITIVE** — a global sole-owner guard blocks all **604** PROTO53 synthetic conflict cases and 0 modeled reachable normal paths. A two-branch 0870 architecture reproduces the genuine corpus **TP=64, FP=0, TN=31, FN=0**.
- **PROTO-OFFLINE-59 — COMPLETE / POSITIVE** — best-supported local normal-runtime 0870 qualifier is a session-scoped one-shot ownership token created by qualified all-zero 085F ACK OR qualified 0864 ACK; known optional 0708 may intervene. Exact local recovery/rejoin qualification remains OPEN.
- **PROTO-OFFLINE-60 — COMPLETE / POSITIVE** — formal machine-readable protocol model v1 created and validated. **57/57 model checks pass**.

## Current protocol model

1. FC17 `071C/0730` is the genuine Online/DCM approval gate; exact response algorithm remains OPEN.
2. Session qualification and current work class are orthogonal axes. Work may be bootstrap, runtime, config refresh, service overlay, desired transaction or recovery/rejoin.
3. Only one semantic owner is reachable at a time in the modeled v4.1 transition graph. A global sole-owner assertion remains recommended defensive hardening.
4. Bootstrap is a fixed 32-page XTR sequence `03E8..06F4`, ACK-gated and profile-specific in page counts.
5. Desired primitive remains: proven selector -> controller FC03 full-page pull -> coherent authoritative page response with at most intended mutation -> exact FC16 confirmation for an actual delta. Exact no-op may not republish.
6. **0870:** normal-runtime ACK is locally proven, but shape alone is wider than local proof. Strongest normal-runtime candidate is the PROTO59 ownership token. A separate recovery/rejoin authorization branch remains locally unresolved.
7. **085F:** both currently accepted local payload forms are genuinely ACK-proven; the open problem is contextual authorization.
8. **Config FC16:** bootstrap, explicit refresh and desired confirmation are locally owned contexts; autonomous controller-originated 03E8 also exists locally. A universal W2/W3-only rule is too strict.
9. **0834:** remains capture-only because local XTR ACK safety is not proven.
10. **0884:** rolling newest-first history snapshot; raw event IDs remain unresolved.
11. **Calendar:** F1..F4 structure remains passive/read-oriented; no generalized writer or new selector inference is authorized.

## Strongest remaining unknowns

- exact 071C/0730 challenge-response algorithm/key/session dependence;
- exact local recovery/rejoin qualifier for an 0870 ACK outside the PROTO59 normal-runtime token path;
- universal/local context predicate for 085F;
- autonomous config-push ownership beyond the locally observed 03E8 case;
- local ACK safety for 0834;
- raw 0884 event-ID meanings;
- calendar weekday bit order and native cross-page write atomicity;
- missing Connect/OnSite/DCM03 firmware or application binary.

## Recommended next sequence

1. Finish EXP388 live: pre-semantic controller-loss cancellation and refresh-only controller-loss cancellation, one branch at a time.
2. Only after EXP388 closes, prepare a single-variable 0870 context-hardening experiment based on the PROTO59 normal-runtime ownership-token model.
3. Keep the recovery/rejoin exception explicitly instrumented; do not guess its local qualifier from cross-model traffic.
4. Run the PROTO54 golden regression and PROTO60 model validator before/after any future writer refactor.

## Safety constraints retained

- Unexpected traffic remains capture-only unless explicitly part of a bounded test.
- No new desired selector is authorized by symmetry or ranking.
- Do not require 0864 before every 0870; EXP309/310 locally disprove that.
- Do not remove either known 085F payload from the local allowlist solely from cross-model statistics.
- Do not convert generic config ACKs to W2/W3-only ownership without preserving autonomous-current-state behavior.
- Keep 0834 capture-only until local evidence changes.
- **EXP388 remains RUNNING / PARTIAL.**
- Write Beta v4.1 itself is unchanged by PROTO45..60.

---

# 2026-10-03 — CANONICAL RECONCILIATION — offline tracks through PROTO-OFFLINE-44

**Authoritative status:** this section supersedes older offline/current-state summaries below where they conflict. Historical text remains unchanged below.

## Current live XTR status — unchanged

- **EXP387 — COMPLETE / POSITIVE** — last fully completed local XTR experiment.
- **EXP388 — RUNNING / PARTIAL** — repeated controller-restart recovery succeeded twice without ESP reboot; remaining pre-semantic and refresh-only cancellation branches are still not independently live-exercised.
- **EXP383 — PREPARED / NOT RUN** — TEST-candidate bundle remains unpromoted except where later experiments separately established a target.
- No PROTO-OFFLINE-40..44 result advances the live experiment state.

## Newly reconciled offline tracks

- **PROTO-OFFLINE-40 — COMPLETE / NEGATIVE for tested simple-transform families** — seven CRC-valid challenge/response pairs (six Eco5, one ATEC/DCM03) reject fixed XOR/add masks, fixed byte/word permutation+mask families, rotations and simple unkeyed MD5/SHA candidates. Exact challenge-response algorithm remains OPEN.
- **PROTO-OFFLINE-41 — COMPLETE / POSITIVE** — four bracketed genuine Eco5 one-word desired deltas all receive exact controller FC16 republish in 0.491..0.571 s; one genuine ATEC exact no-op `0546` desired pull receives no same-page FC16 republish over 226.677 s. Missing republish after an exact no-op is therefore not automatic failure.
- **PROTO-OFFLINE-42 — COMPLETE / POSITIVE** — genuine desired transactions reuse bus-visible same-page current images aged 67.084, 319.512, 374.586 and 87.609 s on Eco5; ATEC no-op age 65.425 s. The current corpus establishes a >=374.586 s lower bound for bus-visible same-page cache reuse in genuine Eco5, without authorizing relaxation of local XTR safety guards.
- **PROTO-OFFLINE-43 — COMPLETE / POSITIVE** — ACK permission is state-qualified rather than shape/payload-qualified. `085F/count5`: 331 publications, 20 ACKed, 311 unACKed. `0870/count17`: 95 publications, 64 ACKed, 31 unACKed; all 31 belong to one reconnect retry window. Known config-page shape likewise does not imply ACK permission.
- **PROTO-OFFLINE-44 — COMPLETE / POSITIVE WITH HARDENING REQUIREMENTS** — the seven-capture state graph is coherent as APPROVAL -> optional WAIT_PAGE_SERVICE -> BOOTSTRAP -> POST_BOOT_SERVICE -> NORMAL_RUNTIME with CONFIG_REFRESH, SERVICE_REFRESH, DESIRED_PULL and RECOVERY_REJOIN branches. Write Beta v4.1 is structurally aligned, but ACK authorization remains broader than the newest evidence model for `085F`, `0870` and generic runtime config pages.

## Protocol-model consequences

1. The challenge-response mechanism is no longer a useful target for simple request->response algebra from the current corpus; keyed/stateful/proprietary mechanisms remain OPEN.
2. Desired-state confirmation is delta-sensitive in the current genuine corpus: semantic deltas republish exactly; an exact no-op may not.
3. Immediate same-page refresh is not a universal gateway prerequisite. Local freshness guards remain a safety policy and must not be relaxed from cross-model evidence alone.
4. Page recognition and permission to ACK are separate concepts. ACK authority belongs to an owning protocol state.
5. Runtime state model now explicitly separates approval, page-service wait, bootstrap, post-bootstrap handoff, normal runtime, config refresh, service refresh/overlay, desired pull and retained/reconnect recovery.
6. `0834/count18` remains a deliberate conservative local gap: genuine references ACK 63/64, but local XTR ACK safety is not proven.

## Future hardening requirements — not yet implemented

1. gate `085F` ACK by explicit locally proven service/recovery context;
2. gate `0870` ACK by qualified normal runtime or explicit recovery state;
3. remove generic runtime config-page ACK-by-shape fallback and require bootstrap/refresh/confirmation/resume ownership;
4. keep `0834` capture-only until separately locally tested.

## Safety constraints retained

- No Write Beta YAML behavior changed by PROTO40..44.
- Do not relax local page-cache freshness solely because genuine Eco5 reused a bus-visible image for >=374.586 s.
- Do not infer a universal no-op rule beyond the current cross-profile evidence.
- Do not broaden `0834` ACK permission from cross-model evidence alone.
- Any future ACK hardening should change one permission class at a time and be live-regressed separately.
- EXP388 remains **RUNNING / PARTIAL**.

---

# 2026-10-03 — ATEC/DCM03 cold-start reconciliation

**Authoritative status:** this section supersedes older ATEC/DCM03 assumptions below where they conflict. Historical text remains unchanged below.

## Current live XTR status — unchanged

- **EXP387 — COMPLETE / POSITIVE** — last fully completed local XTR experiment.
- **EXP388 — RUNNING / PARTIAL** — repeated controller-restart recovery succeeded twice without ESP reboot; remaining cancellation branches are still not independently live-exercised.
- **EXP383 — PREPARED / NOT RUN** — historical TEST-candidate bundle remains unpromoted except where later experiments individually established a target.
- The ATEC/DCM03 evidence below does **not** advance the local XTR live experiment.

## ATEC side branch

- **ATEC-COLDSTART-01 — COMPLETE / POSITIVE** — genuine collaborator ATEC + classic DCM03 cold start captured from the first bus traffic, with DCM03 already powered/listening before HP power-up.
- **ATEC-EXP1 — SUPERSEDED / NOT RUN** — v0.2 was never run. Its 26-page Eco5-derived snapshot geometry and no-FC17 session assumption are incompatible with the complete ATEC ground truth. Keep it as historical code only; do not run it.
- **ATEC-EXP2 — PREPARED / NOT RUN** — isolated DCM03 cross-controller challenge-compatibility bench test. The heat-pump/controller must be absent from the bench bus. This is active FC17 DCM-only traffic, not read-only.

## ATEC-COLDSTART-01 observed facts

- First captured bus frame: **26.480 s**.
- Exact ATEC approval challenge at **27.400 s**: `0F 17 0730/0008 071C/0008 10 2EE156572B8B84A0BC7A65C72D56185D`.
- Classic DCM03 response at **27.429 s**, **29 ms** later: `0F 17 10 20B8F28A236F28FA0339669E2C6F600D`.
- First controller page `03E8/count13` starts at **29.262 s**, **1.833 s after the DCM03 response**. The Eco5 ~120 s page-service delay is therefore not an ATEC/DCM03 requirement.
- ATEC then performs a complete **32-page ACK-gated bootstrap** `03E8..06F4`; every observed page receives the ordinary address/count ACK.
- ATEC page geometry is profile-specific. Concrete differences from modern Eco5 include `03E8/count13`, `0410/count21`, `0492/count9`, and `051E/count9`.
- After `06F4`, `085F/count5` is published/ACKed and the first `0708/count6` response is `0000 0000 0000 0000 07FF 0006`. Steady state then uses `W4=077F, W5=0006`.
- Exactly one non-zero genuine high-half desired selector is present: `W0=0001` at 111.327 s. The controller immediately pulls `0546/count20`.
- The DCM03's returned `0546` desired image is byte-for-byte equal to the earlier controller `0546` image and contains `0553=0004`. This proves **genuine ATEC/DCM03 `W0 bit0 -> FC03 0546`**, but it is a no-op desired pull and does **not** prove an Operation Mode change.
- No later `FC16 0546` republish occurs after that no-op pull.
- This known ATEC uses `0867=0000`; the older-reference `0867=0016` value must not be universalized to every legacy ATEC/DCM03 system.

## Protocol-model consequences

1. A classic DCM03 is directly observed as the slave-`0x0F` device answering the native `071C/0730` approval challenge. DCM03 is therefore a first-class challenge-response firmware/hardware target, not merely an architectural inference.
2. Approval-to-page-service timing is profile/gateway dependent.
3. ATEC and modern Eco5 share the 32-page index and runtime-family architecture but **not all page counts/payload ABIs**.
4. `W0 bit0 -> 0546` is now proven in both local XTR emulation and a genuine ATEC/DCM03 native session. No other new W0 bit is promoted by symmetry.
5. ATEC-EXP1's heat-pump TX assumptions are superseded. No replacement HP-write YAML is promoted until the ATEC approval gate is solved or a native DCM03-assisted path is demonstrated.
6. Immediate controlled next test: ATEC-EXP2 on an isolated DCM03 bench, using the captured ATEC challenge as a positive control before interpreting any Eco8 foreign challenge.

## Strongest ATEC/DCM03 unknowns

- whether standalone DCM03 answers a challenge captured from another controller generation;
- whether response depends only on request + DCM credential or also prior bus/session/pairing state;
- response algorithm/key material;
- remaining genuine W0/high-half desired selectors;
- whether a future non-no-op `0546` desired pull is followed by controller FC16 republish.

## Safety constraints added

- Do **not** run historical ATEC-EXP1 v0.2.
- ATEC-EXP2 must run with heat-pump/controller physically absent from the test bus.
- FC17 writes eight words at `071C` while reading eight at `0730`; classify it as active DCM TX.
- If the captured ATEC positive-control challenge does not produce a valid DCM response on the isolated bench, stop and record **COMPLETE / INCONCLUSIVE** rather than interpreting foreign-challenge silence as pairing proof.

---

# 2026-10-03 — CANONICAL RECONCILIATION — offline tracks through PROTO-OFFLINE-39

**Authoritative status:** this section supersedes older current-state headers below where they conflict. Historical text remains unchanged below.

## Current live XTR status

- **EXP387 — COMPLETE / POSITIVE** — last fully completed live experiment; delayed `0708` semantic re-arm with Room Setpoint write locally confirmed.
- **EXP388 — RUNNING / PARTIAL** — controller-restart recovery succeeded twice without ESP reboot; pre-semantic and refresh-only controller-loss cancellation branches remain not independently live-exercised.
- **EXP383 — PREPARED / NOT RUN** — TEST-candidate bundle remains unpromoted except where later experiments individually established a target.
- No offline result below advances EXP388.

## Newly reconciled offline tracks

- **PROTO-OFFLINE-17 — COMPLETE / POSITIVE** — genuine Eco5 approval acceptance and native page-service readiness are separate bus-visible gates. Across six successful sessions first accepted `03E8/count14` ACK occurs at 118.478..120.296 s after bus return. Two challenge-#3 approvals occur near 10 s and are followed by 102 unACKed `03E8` retries before page service becomes ready.
- **PROTO-OFFLINE-18 — COMPLETE / NEGATIVE** — no independent recurrent captured RS485 field predicts the genuine Eco5 page-service transition before the first `03E8` ACK. The first ACK remains the first direct bus-visible readiness marker.
- **PROTO-OFFLINE-19 — COMPLETE / POSITIVE** — genuine Eco5 startup performs a fixed **32-page ACK-gated controller-autonomous bootstrap** from `03E8` through terminal `06F4` before the first `0708` poll. Later `W2/W3=FFFF/867F` is a separate **26-page mailbox refresh**. `047E,0492,04D8,04F6,050A,051E` are bootstrap-only in the current Eco5 corpus. W4 is runtime/service state/refresh metadata rather than an exclusive next-page selector.
- **PROTO-OFFLINE-20 — COMPLETE / POSITIVE** — register/history audit identifies stale evidence levels and historical interpretations. Local XTR `042E=Hot Water Enabled` and `042F=Hot Water Mode` are no longer open; several heating/cooling settings have later local write proof; runtime/service rows require sparse/profile-scoped semantics.
- **PROTO-OFFLINE-21 — COMPLETE / POSITIVE** — Thermia Connect/OnSite artifact hunt narrows the modern serializer acquisition path. Official Connect commissioning links local AP use, heat-pump serial input and “pairing and protocol packages”; exact Connect identifiers are kit `206495`, gateway `355202`, PSU `357577`. No Connect/DCM firmware, protocol-package archive or APK binary was recovered.
- **PROTO-OFFLINE-22 — COMPLETE / POSITIVE** — this canonical reconciliation folds PROTO17..21 and the PROTO20 evidence corrections into the durable project state without rewriting historical experiment observations.

- **PROTO-OFFLINE-23 — COMPLETE / POSITIVE** — six genuine reference captures pass the current reference-model capture regression: 6/6 exact Eco5 32-page bootstraps, 7/7 exact FFFF/867F 26-page refresh windows, 4/4 clean full-page one-word desired transactions, and no non-zero genuine W0.

- **PROTO-OFFLINE-24 — COMPLETE / NEGATIVE** — 339/339 observed `085F/count5` payloads are all-zero while non-empty `0884` history exists. `085F` is not a mirror of the newest history entry; no current-alarm bridge is identifiable without an actual labelled alarm edge.

- **PROTO-OFFLINE-25 — COMPLETE / POSITIVE** — unresolved-register sweep narrows profile drift: 03F3/0431/0432/0447 are clearly non-universal; 03F5 is a modern count14 extension; 0875 equals 0873 in 83/83 reference frames; 087D shows +1 running-time edges while compressor-running is active. Exact unresolved semantics/scaling remain conservatively OPEN.

- **PROTO-OFFLINE-26 — COMPLETE / POSITIVE** — 163 Eco5 approval challenges contain 162 unique bodies; one exact body repeats on consecutive polls, disproving uniqueness-per-poll. Challenge #3/#29 map tightly to ~10/~120 s timing; simple body features and recent prior gateway activity do not explain early/late/failed approval.

- **PROTO-OFFLINE-27 — COMPLETE / INCONCLUSIVE** — current OnSite/Online public metadata and package acquisition surfaces were rechecked. OnSite Android permissions fit local Wi-Fi commissioning; Thermia Online exposes a concrete XAPK download surface, but no app binary could be retrieved into the analysis environment, so endpoint/manifest/static-code analysis remains untested.

- **PROTO-OFFLINE-28 — COMPLETE / POSITIVE** — selector provenance is now split explicitly: genuine desired proof exists for 03E8/W1b0 and 042E/W1b3; local XTR additionally proves 0442/W1b4, 0546/W0b0 and 055A/W0b1. All remaining desired bits are geometry/symmetry only.

- **PROTO-OFFLINE-29 — COMPLETE / POSITIVE** — runtime grammar reduced to a normal A→B→C→D→E publication ring plus W4 service-refresh state and recurrent overlays. W4 is not exclusive scheduling; 085F is mostly unACKed and requires context-specific permission.

- **PROTO-OFFLINE-30 — COMPLETE / POSITIVE** — current page geometry, selector provenance and runtime ACK rules are now encoded in a deny-by-default machine-readable schema with a static YAML linter. Current Write Beta v4.1 produced no hard protocol-schema errors; TEST candidates remain explicitly marked.

- **PROTO-OFFLINE-31 — COMPLETE / NEGATIVE** — raw 0884 event-ID archaeology found no safe public decoder. Numeric collisions with Genesis alarm addresses exist, but larger modern IDs and profile mismatch disprove a universal direct-address mapping.

- **PROTO-OFFLINE-32 — COMPLETE / NEGATIVE** — 163 genuine Eco5 challenge bodies show high diffusion, balanced bits and no stable counter/timestamp byte field. The one exact consecutive duplicate disproves nonce uniqueness; local-XTR structured request bytes must not be universalized to Eco5.

- **PROTO-OFFLINE-33 — COMPLETE / POSITIVE** — Thermia Connect hardware fingerprint narrowed to exact part IDs 206495/355202/357577, 12 V gateway, USB/Ethernet/two communication ports, 2.4 GHz Wi-Fi/WPA-PSK and regulatory radio-standard set. No OEM/SoC/module identity was recovered; cellular certification must not be interpreted as proof of a built-in active modem because Thermia documents external 3G/4G modem use for no-broadband installations.

- **PROTO-OFFLINE-34 — COMPLETE / POSITIVE** — W5 is narrowed to profile/session metadata with local XTR liveness/UI significance: EXP344→345 proves W5=0006 sufficient for persistent DCM icon while W5=0000 remains transport-valid; genuine Eco5 uses W5=0000 in 264/264 answered polls, so W5 is not a universal connected enum.

- **PROTO-OFFLINE-35 — COMPLETE / POSITIVE** — operational-time scaling is reduced: 0870/0872/0873/0876/0877/0878 are strongly supported as raw integer hours; 087B is count; 087C/087D are compressor-runtime minutes, matching the XTR manual and observed minute-scale 087D increments.

- **PROTO-OFFLINE-36 — COMPLETE / POSITIVE** — automated runtime correlation exactly reduces 07F4 as a 0/4/6 normalized outdoor-unit state summary and 0845 as 0x0300 iff modern 1E:0015=0x0221. No new heating/cooling/DHW/defrost/SG label is promoted without a labelled transition.

- **PROTO-OFFLINE-37 — COMPLETE / POSITIVE with hardening candidate** — Write Beta v4.1 TX provenance audited. No uncontrolled/unknown semantic TX found; stale EXP379/EXP352/EXP380 evidence labels were corrected without behavior changes. Generic runtime config-page ACK-by-shape remains a future hardening candidate because recognition is broader than scheduler-qualified permission.

- **PROTO-OFFLINE-38 — COMPLETE / POSITIVE** — deterministic ABI/topology classifier separates all six genuine references: 4/4 legacy A5 Online/DCM and 2/2 modern 0x1E Online, with no ambiguous capture. It classifies topology/ABI, not exact Thermia model identity.

- **PROTO-OFFLINE-39 — COMPLETE / POSITIVE** — canonical experiment coverage audit records 139 present numeric EXP IDs and preserves 249 missing IDs as explicit gaps. Newest-record provenance is inventoried without reconstructing history. The only current active live experiment remains EXP388; EXP383 remains PREPARED / NOT RUN.

- **PROTO-OFFLINE-37 — COMPLETE / POSITIVE WITH SAFETY DEBT IDENTIFIED** — Write Beta v4.1 TX provenance audit found semantic write machinery strongly fail-closed, but three runtime ACK rules are broader than the newer context-driven model: 085F payload-only ACK permission (highest priority), context-blind 0870 ACK, and generic runtime ACK of known configuration page shapes. No YAML behavior changed.\n\n## Current protocol model additions

1. Treat **APPROVAL**, **WAITING_FOR_PAGE_SERVICE**, **BOOTSTRAP**, and **RUNTIME/MAILBOX** as separate protocol states.
2. Do not encode the genuine Eco5 ~120 s page-service boundary as a universal Thermia controller requirement.
3. Initial genuine Eco5 configuration synchronization is the 32-page autonomous ACK-gated bootstrap; later `0708 W2/W3` configuration refresh is a separate mechanism.
4. `W4` retains its page-family mapping but is not an exclusive immediate scheduler.
5. Genuine desired-selector evidence remains narrow: `W1 bit0 -> 03E8` and `W1 bit3 -> 042E`. High-half/W0 genuine behavior remains unobserved; local XTR selector/write evidence must be tracked separately by experiment and not generalized cross-model.
6. Local XTR semantic identity is now established for `042E=Hot Water Enabled` and `042F=Hot Water Mode`; the same numeric address remains profile-dependent across ATEC/iTec families.

## Strongest remaining unknowns

1. Exact gateway-internal/sideband condition behind the genuine Eco5 page-service readiness boundary.
2. Unobserved desired-state selector coverage, especially genuine W0/high-half behavior.
3. Thermia Connect / DCM03 serializer and protocol-package contents.
4. `085F/count5` per-word semantics and the current-alarm bridge to `0884` history.
5. Remaining unresolved registers including `03F1/03F2/03F3/03F5`, `0431/0432`, `0447`, `0874/0875`, plus exact runtime-counter scaling.
6. Alarm-history raw-code translation and calendar active-write atomicity/weekday-bit behavior.

## Safety constraints retained

- EXP388 remains **RUNNING / PARTIAL**.
- Unexpected traffic remains capture-only unless explicitly part of a bounded experiment.
- Do not infer a desired selector from bitmap symmetry alone.
- Desired responses use a fresh authoritative page cache and mutate one intended known target only.
- Foreign-model page equality does not authorize payload replay.
- Calendar/alarm/history remain passive unless separately defined.

---

# 2026-10-03 — CANONICAL RECONCILIATION — offline tracks through PROTO-OFFLINE-16

**Authoritative status:** this section supersedes older current-state headers below where they conflict. Historical experiment text is retained unchanged.

## Current live XTR status

- **EXP387 — COMPLETE / POSITIVE** — last fully completed live experiment.
- **EXP388 — RUNNING / PARTIAL** — repeated controller-restart recovery has succeeded twice without ESP reboot; pre-semantic and refresh-only controller-loss cancellation branches are not yet independently live-exercised.
- **EXP383 — PREPARED / NOT RUN** — historical TEST-candidate bundle remains recorded as prepared/not-run; later local proof must be tracked per target, not inferred from publication alone.
- **CAL-OFFLINE-01 — COMPLETE / POSITIVE (offline scope closed)** — ordinary calendar structure is reduced to decoder level; calendar write semantics remain unproven.
- No live experiment is advanced by the offline analyses below.

Current published write baseline remains the existing Write (Beta) branch/file; this reconciliation changes documentation only.

## Newly reconciled offline tracks

- **PROTO-OFFLINE-02 — COMPLETE / POSITIVE** — `071C/0730` response is a strong session-opening gate in genuine Online captures; local XTR evidence shows a fixed known-good response can be accepted against different request payloads, so per-request cryptographic derivation is not required for that locally proven step.
- **PROTO-OFFLINE-03 — COMPLETE / POSITIVE** — corrected provenance: the four `thermia_capture_20260924/25...` files are genuine Online/DCM reference captures, not historical local-XTR captures. Page-size differences are therefore cross-system/profile differences, not proven temporal XTR drift.
- **PROTO-OFFLINE-04 — COMPLETE / POSITIVE** — `06F4..06F8 = A80C..A810` and `0701 = AFDC` are structurally proven mirrors; `06F4/count19` is an integration/context bridge, not a simple static settings page.
- **PROTO-OFFLINE-05 — COMPLETE / POSITIVE** — recurring runtime family reduced: `07D0/19, 07E4/17, 07F8/17, 080C/18, 0820/18, 0834/18, 0848/23, 0864/4, 0870/17`.
- **PROTO-OFFLINE-06 — COMPLETE / POSITIVE** — automated source correlation proves topology-normalized runtime fields including `07D1` return-line temperature and `07E4` average outdoor temperature.
- **PROTO-OFFLINE-07 — COMPLETE / POSITIVE** — Link CC 2.7.42 contains HE identity/binding and a rich semantic heat-pump model but not the final Thermia-native `0x0F` serializer; exact HE heat-pump identity is firmware-derived only and must not be injected into native traffic.
- **PROTO-OFFLINE-08 — COMPLETE / POSITIVE** — unresolved runtime-field reduction materially narrows `0834`, `0864`, and `0870`; later PROTO-OFFLINE-16 supersedes the earlier contiguous operating-time-counter hypothesis.
- **PROTO-OFFLINE-09 — COMPLETE / POSITIVE** — `0708/count6` is a page scheduler/dispatcher. `W2/W3` are proven 32-page FC16 state-upload bitmaps; `W1` is proven as a desired-state FC03 pull bitmap for observed low-half bits; `W4` is strongly supported as the runtime/service-page bitmap; `W0` remains only a high-half desired-state hypothesis; `W5` remains open metadata.
- **PROTO-OFFLINE-10 — COMPLETE / POSITIVE** — native Online semantic writes are controller-pulled full-page read/modify/return transactions. In all four fully bracketed Eco5 examples exactly one word differs from the last controller page and the following FC16 page exactly equals the desired image. `03F4` setpoint adoption is independently confirmed and later locally confirmed on XTR.
- **CAL-OFFLINE-01 — COMPLETE / POSITIVE (offline scope closed)** — four logical calendar blocks `F1..F4`, each `8 × 12-word records + 2 metadata words`, plus four-word tail. F1 is locally WW_GEBLOKKEERD. No calendar desired-state pull or nonzero W0 exists in the current genuine capture corpus; live calendar writing is therefore not inferred.
- **PROTO-OFFLINE-13 — COMPLETE / POSITIVE** — `0x0F` runtime pages form a logical Online/DCM ABI above topology-specific physical backends. Stable page envelopes do not imply byte-identical payload semantics across models.
- **PROTO-OFFLINE-14 — COMPLETE / POSITIVE** — local XTR `0884/count60` is a rolling timestamped history page using the modern `8 × 7-word records + 4-word trailer` ABI; genuine legacy Online uses `10 × 6`. It is very strongly supported as alarm/service history, but raw IDs are not mapped to displayed XTR E-codes.
- **PROTO-OFFLINE-15 — COMPLETE / POSITIVE** — firmware archaeology narrows the old AQ/Atec/iTec serializer target to DCM03 and the modern XTR target to Thermia Connect / protocol packages. No DCM03/Connect firmware binary or protocol package was recovered.
- **PROTO-OFFLINE-16 — COMPLETE / POSITIVE** — register semantics are profile/model scoped, not universal. Core heating semantics are stable across ATEC+iTec; `042E` is a concrete profile-drift example. `0870` is strongly supported as compressor operating time; operating-time counters are sparse, and `087B/087C/087D` are strongly supported as the three defrost statistics.
- **PROTO-OFFLINE-11 / -12:** no completed canonical experiment is recorded; do not backfill or infer completion from roadmap numbering.

## Current protocol model

### Native session and scheduler

1. Controller/session transport, application approval, initial state synchronization, runtime qualification and semantic desired-state writes are separate layers.
2. `071C/0730` is a session-opening gate in genuine Online traffic; XTR replay success does not prove a universal challenge algorithm.
3. `0708/count6` is the dispatcher:
   - `W1`: observed low-half desired-state FC03 pull bits;
   - `W0`: hypothesized high-half desired-state pull bits, never observed nonzero in the current genuine corpus;
   - `W2/W3`: proven 32-page FC16 state-upload bitmap;
   - `W4`: runtime/service-page bitmap;
   - `W5`: implementation/profile/session metadata, exact meaning open.
4. Proven semantic write primitive:
   `0708 desired-page bit -> controller FC03 desired page -> emulator returns coherent full page with one intended change -> controller applies -> controller FC16 republishes result`.
5. Do not generalize this primitive to a page whose desired-state selector has never been observed or locally proven.

### Register/schema discipline

- Native numeric addresses can share the public Online `registerIndex` namespace, but semantics are **profile-specific**.
- Keep four evidence dimensions separate: address exists; semantic label proven; an external profile says writable; native desired-state path proven.
- Strong local/protocol anchors include `03E8` Heat Curve, `03EB` Curve +5, `03F4` Room Setpoint, `0442` Activate Cooling, and `0553` Operation Mode. Evidence level for each write path remains target-specific.
- `03F1 = HotWaterStart` is superseded for XTR.
- `042E` is profile-dependent: ATEC metadata says Integral A1; iTec metadata says Hot Water Status. Genuine modern Eco5 `1 -> 0` behavior strongly favors Hot Water Status for that profile; local XTR semantic identity remains separately tracked.
- `0870` = compressor operating time is strongly supported; the seven operating-time counters are not a simple contiguous `0872..0878` block.
- `087B/087C/087D` align strongly with defrost count / interval between last two defrosts / time since last defrost.

### Runtime and service model

- `0x0F` acts as a logical serializer/normalizer across legacy and modern topology families.
- `0820` is a concrete adapter boundary: legacy sources from A5; modern sources from `0x1E`.
- `0858..085E` is a stable clock/date tuple; weekday is Monday=0 through Sunday=6.
- `0884/count60` is locally confirmed XTR rolling timestamped history; raw event identifiers remain unmapped.
- Current alarm/error state and timestamped history are separate concepts; `085F/count5` remains semantically OPEN.

### Calendar

- Ordinary calendar = four 98-word logical functions + four-word tail.
- Each function = eight 12-word records + two metadata words.
- Metadata0 is strongly supported as slot-validity bitmap.
- F1 = WW_GEBLOKKEERD locally; F2/F3/F4 labels remain hypotheses.
- No W0/calendar desired-state transaction is observed; no active calendar writer should be inferred.

## Strongest remaining unknowns

1. Exact local-XTR prerequisite/state transition that activates or reactivates the full Online/DCM scheduler after loss/restart.
2. Unobserved desired-state selector coverage, especially W0/high-half pages.
3. Thermia Connect / DCM03 native serializer and protocol-package contents.
4. Exact local XTR semantics for remaining profile-dependent fields such as `042E/042F`.
5. Alarm-history raw-code translation and current-alarm native bridge.
6. Calendar weekday bit order and calendar write/atomicity behavior.

## Safety constraints

- Preserve EXP388 as RUNNING / PARTIAL until its remaining branches are actually exercised.
- Never transmit an unobserved W0 bit or invent W1 selectors from symmetry.
- Build any desired page from a fresh locally authoritative full-page cache; mutate one known target only.
- Equal page address/count across models does not authorize foreign payload replay.
- External profile writability does not authorize an XTR write.
- Calendar and alarm/history pages remain read/capture-only unless a separate active experiment explicitly defines otherwise.
- Fail closed on parser/RX/session/page-shape mismatch and keep DE LOW outside guarded TX.

## Reconciled working artifacts

Current detailed working reports are retained under `Research/temp/`, including PROTO-OFFLINE-09/10/13/14/15/16 and CAL-OFFLINE-01 closure. Canonical files summarize durable conclusions; temp reports preserve the full derivations and intermediate evidence.

---

# 2026-10-02 — PROTO-OFFLINE-01 — unknown-page correlation — COMPLETE / POSITIVE

**Track:** offline evidence analysis only. No heat-pump TX, no new native write target and no live experiment advancement.

## Authoritative current live XTR status

This entry reconciles the canonical state with the current published Write Beta v4.1 header:

- **EXP386 — COMPLETE / POSITIVE** — guarded controller-restart recovery locally confirmed end-to-end.
- **EXP387 — COMPLETE / POSITIVE** — delayed `0708` semantic re-arm locally confirmed with Room Setpoint write.
- **EXP388 — RUNNING / PARTIAL** — repeated controller-restart recovery locally confirmed twice without ESP reboot; pre-semantic and refresh-only controller-loss cancellation branches are not independently live-exercised.
- **EXP383 — PREPARED / NOT RUN** — the seven TEST candidate controls remain unpromoted.
- **CAL-OFFLINE-01 — RUNNING / PARTIAL** — passive calendar reduction remains open.

Current published active write baseline:
`Write (Beta)/thermia_itec_xtr_m_waveshare_write_beta_v4_1.yaml`

Older state sections below are retained as historical snapshots and must not override this newer status.

## PROTO-OFFLINE-01 durable results

### STRONGLY SUPPORTED / locally correlated — 04A6/04A7 and SG operating state

In the later local XTR DCM-style runtime:
- SG Normal `(0-0)` -> `04A6=0000, 04A7=0000`
- SG Enhanced `(0-1)` -> `04A6=0041, 04A7=0001`
- SG Blocked `(1-0)` -> `04A6=0042, 04A7=0001`
- returning to Normal returns the pair to `0000/0000`.

`04A6/04A7` are therefore strongly linked to SG/operational state in that runtime context. Genuine Eco5 approval events occur with both zero and non-zero `04A6`, so this is not an Online/DCM approval flag.

An older local XTR capture contains a radically different `04A6/count13` payload, so the whole page must not be treated as one fixed SG-only schema across all historical/session contexts.

### STRONGLY SUPPORTED — 0424 Returnline Temperature Max Limit

The cross-model DHP/AQ contiguous register sequence is locally anchored by the already-confirmed `041D` Hot Water Start Temperature and `041E` Hot Water Operating Time. Continuing that sequence places `0424` at **Returnline Temperature Max Limit**. No one-variable XTR UI correlation has yet promoted it to local proof.

### PROVEN / directly observed structural relation — 06F4 context mirror

Across local XTR evidence and all compared genuine Eco5 `06F4/count19` frames:
- `06F4 = A80C`
- `06F5 = A80D`
- `06F6 = A80E`
- `06F7 = A80F`
- `06F8 = A810`
- `0701 = AFDC`

This proves the mirror relationship only; it does not promote the underlying semantic meanings of A80C/A80E/A80F/AFDC beyond their existing evidence levels.

**Strong conclusion:** `06F4/count19` is at least partly a controller/integration-context snapshot inside the native `0x0F` page family rather than a purely static configuration page.

## Current strongest offline unknown

Why `04A6/count13` has a radically different historical local payload regime remains OPEN. Investigate this together with the already-observed historical/current page-shape drift rather than forcing one fixed schema across all captures.

Full report:
`Research/protocol reduction/PROTO_OFFLINE_01_UNKNOWN_PAGE_CORRELATION_20261002.md`

---

# 2026-10-02 — CAL-OFFLINE-01 — calendar structure refinement — RUNNING / PARTIAL

**Track:** offline evidence analysis only. No new ESP calendar TX or semantic write is introduced, and this note does not advance or close any live XTR experiment.

## Current calendar protocol model

New local XTR evidence directly anchors a **WW_GEBLOKKEERD** edit to the native `055A/count33` desired-page path. The complete historical XTR + genuine Eco5 page family has now been re-aligned.

**STRONGLY SUPPORTED structural model:**
- one calendar record = 12 words;
- four ordinary logical calendar-function blocks occupy `055A..06E1`;
- each block = 8 × 12-word records + 2 metadata words = **98 words**;
- corrected block boundaries are:
  - F1 `055A..05BB`
  - F2 `05BC..061D`
  - F3 `061E..067F`
  - F4 `0680..06E1`
- the earlier 99-word-per-function interpretation is **DISPROVEN / SUPERSEDED**;
- candidate slot-validity/occupancy bitmaps are `05BA`, `061C`, `067E`, `06E0`;
- `04D8/count27` is **STRONGLY SUPPORTED** as the separate concrete-drying configuration block;
- `06EA/count7` is **STRONGLY SUPPORTED** as the clock/date block;
- the separate tail `06E2/06E3` reconstructs `0870 word0` exactly across the compared local XTR and two genuine Eco5 datasets; semantics remain OPEN.

**Locally PROVEN calendar anchor:** F1 participates in WW_GEBLOKKEERD editing through `055A/count33`.  
**HYPOTHESIS only:** F2=EVU/power limiting, F3=Silent Mode, F4=Temperature Reduction.

## Important calendar unknowns

Exact weekday-bit ordering, live bitmap transition during add/delete, second metadata-word semantics, concrete-drying header words0..4, `06E2..06E5` semantics and multi-page transaction ordering for a record crossing native 33-word boundaries remain open.

## Next calendar experiment

Passive-only local correlation: one WW_GEBLOKKEERD DATE slot with one controlled non-zero minute field, followed by deletion and 60–90 s continued capture. No calendar write from the ESP until record and bitmap behavior are locally confirmed.

Full reduction: `Research/CALENDAR_STRUCTURE_ANALYSIS_20261002.md`.

---

# 2026-10-02 — iTec Eco replay experiment refined from genuine gateway logs; no Eco active result yet

**Cross-model status:** `ECO-WRITE-01` remains **PREPARED / NOT RUN** in `Research/iTec Eco/`. The prepared definition was refined before its first run after combined reduction of both genuine Eco5 + Thermia Online captures. This does not change the authoritative XTR M experiment/result status below.

## iTec Eco active-write baseline

Passive baseline:

`Read-only/iTec Eco/thermia_itec_eco_waveshare_public_v01.yaml`

Prepared active artifact:

`Research/iTec Eco/thermia_itec_eco_waveshare_write_exp01.yaml`

Raw-capture evidence note:

`Research/iTec Eco/ECO5_GATEWAY_CAPTURE_EVIDENCE.md`

## Current genuine Eco5 protocol model

**Observed directly in genuine Eco5 Online captures:**

- six successful exact `071C/0730` challenge -> gateway-response events across the two available Eco5 gateway logs;
- every successful response is followed by controller `FC16 03E8/count14`;
- successful responses occur at challenge #29 four times and challenge #3 twice;
- all six response bodies differ;
- when `03E8/count14` is immediately ACKed, synchronization advances to `03FC/11` and onward;
- in two no-immediate-ACK challenge-#3 windows, `03E8/count14` is repeatedly retransmitted and does not progress to `03FC` during the next 10 s.

**Strong conclusion:** the native Eco5 Online approval/synchronization architecture and first page-ACK progression are established by genuine capture evidence. They do not need to be rediscovered by ECO-WRITE-01.

**OPEN / UNKNOWN for the target Eco controller:** whether a previously captured known-good response is accepted against a different live challenge.

## ECO-WRITE-01 hypothesis

The target iTec Eco controller accepts a known-good Eco5 response replayed against a non-matching current challenge.

## Exact new variable

After manual arm + >=5 s controller-bus silence + boot return:

- exact challenge #1: capture-only;
- exact challenge #2: capture-only;
- exact challenge #3: replay once:

`0F17101691A5F3F8E8D58738924416E8E6A3D5E227`

Challenge #3 is evidence-based: a genuine Eco5 gateway successfully responds at that ordinal in two captured sessions. The replay body came from another captured challenge/session, making this a deliberate mismatched-replay test.

No FC16 page ACK, no `0708` reply, no desired-page selector and no semantic setting write are enabled.

## Information criterion

**Positive:** after the single challenge-#3 replay, the controller sends `0x0F FC16 03E8/count14`.

The ESP deliberately leaves that page unACKed because the downstream Eco5 ACK/sync architecture is already genuine-capture evidence.

## Safety

One R1 maximum per ESP boot; manual arm required; DE LOW otherwise; challenge #1/#2 NO TX; peer responder or parser CRC/resync/RX-drop integrity change aborts; unexpected traffic is capture-only. If a partial Online/DCM state or alarm persists, return to the passive Eco build and use only the normal controller restart procedure if needed.

**Do not advance to Eco initial-sync ACKs or semantic writes until an ECO-WRITE-01 result/log is supplied.**

---

# 2026-10-02 — EXP386 complete; native DCM session recovery locally confirmed

**Authoritative current state:** EXP386 is **COMPLETE / POSITIVE** from the supplied local Thermia iTec XTR M runtime log. There is no newly promoted live experiment. EXP383 remains **PREPARED / NOT RUN** for the seven semantic candidate controls; the DCM/session-recovery work did not validate those mappings.

## Current DCM/session baseline

Current published write file:

`Write (Beta)/thermia_itec_xtr_m_waveshare_write_beta_v4_0.yaml`

The v4.0 session state machine is now locally confirmed to recover a native DCM-style session after a real controller power-cycle while the ESP remains running.

Locally confirmed EXP386 flow:
- repeated exact `071C/0730` challenges outside the proven cold-start guard are **NO TX / capture-only** and no longer stop unqualified stage40;
- >=5 s complete bus silence transitions unqualified semantic-idle stage40 into the existing stage-1 cold-start recovery path;
- first valid frame after silence produces `BOOT_RETURN` and stage 2;
- R1 is allowed only when the controller state is known as `A80E=0000 / A80F=0005`;
- one already-proven R1 is transmitted on the exact challenge;
- the first post-R1 FC16 is `03E8/count14`;
- the complete ordered initial FC16 sync runs through `06F4/count19`;
- persistent stage40 runtime then qualifies with a fresh known runtime FC16 ACK plus a `0708` idle reply;
- the successful run ended with `COMPLETE / POSITIVE / fresh controller session recovered`;
- parser integrity remained clean in that run: `resync=0`, `drops=0`.

No hard-coded R1, page-ACK or selector payload was changed by EXP386. The controlled changes were session-state transitions only.

## Current protocol model additions

1. An exact `071C/0730` challenge by itself is not permission to transmit.
2. On this XTR M, the locally proven R1 replay permission remains the known `A80E=0000 / A80F=0005` cold-start state.
3. Challenges observed outside that guard, including `A80E=0008 / A80F=0032`, are capture-only.
4. A real controller restart can be detected by >=5 s complete bus silence followed by boot return.
5. Initial settings synchronization and persistent runtime qualification are separate phases; the session is only considered recovered after fresh runtime service evidence.

## Current experiment status

- **EXP386 — COMPLETE / POSITIVE**
- **EXP383 — PREPARED / NOT RUN**
- Calendar track remains parked unless explicitly reopened.

## Safety

Keep semantic writes separate from session activation. Do not relax the R1 guard, do not invent challenge responses, do not broad-scan or write unknown registers, and do not use the EXP383 TEST controls as if they were proven mappings.

---

# 2026-10-01 — EXP381B complete; EXP382 offline complete; EXP383 prepared

**Authoritative current state:** EXP381B is **COMPLETE / POSITIVE** by explicit user confirmation after running the production/UI consolidation build. EXP382 is **COMPLETE / POSITIVE** as an offline evidence-analysis experiment. EXP383 is **PREPARED / NOT RUN**. The current published active write build is **Write (Beta) v4.0**, derived from EXP383; its seven entities containing `TEST` are intentionally not yet promoted to locally proven mappings.

## Current experiment

### EXP383 — PREPARED / NOT RUN — STRONGLY SUPPORTED candidate controls

**Baseline:** EXP381B **COMPLETE / POSITIVE**. EXP382 **COMPLETE / POSITIVE** offline gap analysis.

**Hypothesis:** seven EXP382 mappings classified **STRONGLY SUPPORTED** can reuse the already proven page-owned native semantic-write mechanisms without changing the established selector/session model.

**Exact controlled change from EXP381B:** add seven user-visible Configuration controls, each explicitly marked `TEST` in its Home Assistant name:
- `0430` / 042E word2 — **TEST Top-up**
- `0444` / 0442 word2 — **TEST Cooling Hysteresis**
- `0446` / 0442 word4 — **TEST Cooling Configuration**
- `0448` / 0442 word6 — **TEST Stop Threshold**
- `044A` / 0442 word8 — **TEST Max Start Temperature**
- `044B` / 0442 word9 — **TEST Min Stop Temperature**
- `0559` / 0546 word19 — **TEST Link Integration**

No candidate is considered proven merely because it is present in Write Beta v4.0.

**Existing proven page paths reused:**
- `042E/count15` current/desired selector path
- `0442/count13` current/desired selector path
- `0546/count20` current/desired selector path

Each semantic transaction still requires a fresh authoritative controller page, changes one selected word only, and accepts success only after an exact controller FC16 republish with `extraDeltaWords=0`.

**Safety:** test one new candidate at a time and use the smallest reversible change possible. `0559 Link Integration` is the highest-risk candidate because changing integration mode may affect the Online/DCM-style session; test it last. Stop on parser/RX/peer/session fault, timeout, unexpected page/count, unexpected extra delta, or controller behavior inconsistent with the candidate field. No automatic retry after failure.

**Status:** PREPARED / NOT RUN.

## Last completed live experiment

### EXP381B — COMPLETE / POSITIVE — production/UI consolidation

The user explicitly confirmed EXP381B ran successfully. Its behavior-preserving cleanup therefore becomes the current locally proven runtime baseline.

Confirmed scope:
- manual-aligned Configuration ordering: Operation → Heating → Hot Water → Cooling;
- Startup HT / Heating Time grouped under Heating / Service;
- useful read-only entities enabled by default;
- no change to the proven protocol/write machinery;
- existing persistent controls retained their working behavior.

EXP381A was superseded by the consolidated EXP381B build and was not separately run.

## Last completed offline experiment

### EXP382 — COMPLETE / POSITIVE — offline controlled-page gap analysis

EXP382 performed no bus TX and made no device change. It compared local XTR results with the commissioning manual, genuine Online/DCM evidence, collaborator captures and public register-index evidence.

New classifications:
- `0430` Hot Water TOP_UP — **STRONGLY SUPPORTED**
- `0444` Cooling Hysteresis — **STRONGLY SUPPORTED**
- `0446` Service Cooling Configuration/Type — **STRONGLY SUPPORTED**
- `0448` Cooling STOP threshold — **STRONGLY SUPPORTED**
- `044A` MAX_STARTTEMP — **STRONGLY SUPPORTED**
- `044B` MIN_STOPTEMP — **STRONGLY SUPPORTED**
- `0559` Link Integration — **STRONGLY SUPPORTED**
- `0447` Cooling START threshold — **HYPOTHESIS** only; not included in EXP383.

The full offline analysis is retained in `Research/EXP382_OFFLINE_GAP_ANALYSIS.md`.

## Current proven writable scope

### 03E8/count14 — heating
Locally proven writable:
`03E8`, `03E9`, `03EA`, `03EB`, `03EC`, `03ED`, `03EE`, `03EF`, `03F0`, `03F4`.

### 042E/count15 — hot water / service
Locally proven writable:
- `042E` Hot Water Enabled
- `042F` Hot Water Mode
- `0433` Startup HT
- `0434` Heating Time

`0430` is STRONGLY SUPPORTED as TOP_UP but remains unproven until EXP383 testing.

### 0442/count13 — cooling
Locally proven writable:
- `0442` Cooling Enabled
- `0443` Desired Cooling Temperature
- `0445` Cooling Active Above
- `0449` Cooling Time
- `044C` Cooling Room Sensor
- `044D` Cooling Room Hysteresis Low
- `044E` Cooling Room Hysteresis High

EXP382 candidate mappings `0444/0446/0448/044A/044B` remain STRONGLY SUPPORTED, not locally proven.

### 0546/count20 — system
- `0553` Operation Mode — **PROVEN / locally confirmed writable** by EXP380 user-confirmed success.
- `0559` Link Integration — **STRONGLY SUPPORTED**, TEST only in EXP383/v4.0.

## Published Write Beta

Current file:
`Write (Beta)/thermia_itec_xtr_m_waveshare_write_beta_v4_0.yaml`

v4.0 contains the EXP381B proven baseline plus the seven clearly marked EXP383 TEST controls. Publication does not change their evidence status.

## Read-only baseline

Current passive build:
- `Read-only/Thermia itec XTR/thermia_itec_xtr_m_waveshare_public_v29.yaml`
- `Read-only/Thermia itec XTR/thermia_itec_xtr_m_waveshare_research_v29.yaml`

v29 remains strictly RX-only: no Thermia TX pin, no `write_array()` calls, DE forced LOW. It passively decodes the locally proven settings on `042E/count15`, `0442/count13` and `0546/count20`, and enables the useful service/read-only entities aligned with EXP381B. EXP382/EXP383 STRONGLY SUPPORTED candidates remain excluded from normal read-only semantics until locally confirmed.

## Next roadmap

After EXP383 candidate validation:
1. Calendar functionality
2. Missing entities
3. Faults/alarms readout
4. Complete native settings map
5. Generic DCM/Online emulator
6. Solve challenge-response
7. Defrost + full operating-state model
8. Cross-model compatibility / supported types

## Safety constraints

Continue one-target-at-a-time writes from fresh controller pages, exact page/count validation, one-word deltas, exact controller republish verification, bounded UI values, no automatic retries, parser/RX/peer fail-close, and DE LOW outside guarded TX. STRONGLY SUPPORTED candidates remain TEST-only until individually confirmed on this XTR M.

---

# 2026-10-01 — EXP379 complete; EXP380 prepared

**Authoritative current state:** EXP379 is **COMPLETE / POSITIVE** from the supplied local XTR M runtime log. EXP380 is **PREPARED / NOT RUN**. The last completed experiment is therefore EXP379.

## Current experiment

### EXP380 — PREPARED / NOT RUN — persistent Operation Mode control on 0546/count20

**Hypothesis:** the native desired-page mechanism can be extended to page `0546/count20` and used to change only `0553` / word 13, the Operation Mode field.

**Accepted working enum for this experiment:**
- `0 = Uit`
- `1 = Auto`
- `2 = Compressor`
- `3 = Bijverwarmer`
- `4 = Warmwater`

Local XTR evidence before EXP380 confirms `1 = Auto` and `2 = Compressor` by panel-driven change `0553: 1 -> 2 -> 1`. Values 0/3/4 are accepted as genuine/cross-model evidence for active testing by explicit user instruction, but are not rewritten as historical local proof.

**Exact controlled change from EXP379:** add one persistent Home Assistant `select` under Configuration for `0553`, using the same desired-intent queue/UI model as EXP378/379. No other new target is introduced.

**Planned semantic flow:** fresh controller `FC16 0546/count20` -> desired selector -> controller `FC03 0546/count20` -> emulator returns full page with only word 13 changed -> controller republishes `FC16 0546/count20`.

**Success:** republished word 13 equals target and `extraDeltaWords=0`; transaction closes READY.

**Negative/abort:** wrong page/count, enum outside 0..4, stale source page, parser/RX/peer fault, timeout, target not adopted, or any extra changed word. No automatic retry after failure.

**Status:** PREPARED / NOT RUN. Generated YAML does not count as experiment completion.

## Last completed experiment

### EXP379 — COMPLETE / POSITIVE — persistent cooling controls on 0442/count13

EXP379 v2 locally confirmed persistent semantic writes for every exposed cooling field in the experiment:
- `0442` Cooling Enabled — PROVEN
- `0443` Desired Cooling Temperature — PROVEN
- `0445` Cooling Active Above — PROVEN and reversible
- `0449` Cooling Time — PROVEN
- `044C` Cooling Room Sensor — PROVEN and reversible
- `044D` Cooling Room Hysteresis Low — PROVEN, raw/10 °C, reversible
- `044E` Cooling Room Hysteresis High — PROVEN, raw/10 °C, reversible

Representative exact confirmations from the supplied runtime log include:
- 0442: `0 -> 1`, `extraDeltaWords=0`
- 044C: `0 -> 1`, `extraDeltaWords=0`
- 044D: raw `10 -> 18 -> 10`, `extraDeltaWords=0`
- 044E: raw `10 -> 17 -> 10`, `extraDeltaWords=0`
- 0449: `21 -> 20`, `extraDeltaWords=0`
- 0443: `17 -> 18`, `extraDeltaWords=0`
- 0445: `25 -> 27 -> 25`, exact one-word republish, `extraDeltaWords=0`

The dynamic guard for 0445 is also locally confirmed: with Heating Stop 22 °C, the minimum accepted UI target is 25 °C. Requests below `Heating Stop + 3 K` were blocked locally with NO_TX and the authoritative value restored.

**Cooling hysteresis UI bounds:** both Low and High are `0.5..5.0 °C`, step `0.1 °C`, raw `5..50`.

## Recent completed experiments

### EXP378 — COMPLETE / POSITIVE — 042E current refresh + unified desired-state queue UI

- W3-only bit3 current selector was locally confirmed for page `042E/count15`.
- Current-refresh frame observed/used: `0F030C0000000000000008000000067CB7`.
- Desired selector for 042E: `0F030C0000000800000008000000061B77`.
- Rapid desired-state queue behavior worked as intended: UI retains newest desired intent while queued/in-flight and returns to controller authority after success/failure.
- 0433 was also confirmed reversible `5 -> 7 -> 5`.

### EXP377 — COMPLETE / POSITIVE — first semantic write on 042E/count15

- `042F` SWW Mode was changed `1 -> 0` through the full native desired-page flow.
- Controller republished the exact target with `extraDeltaWords=0`.
- This locally proves semantic writeability of page 042E and the selector path.

### EXP376 — RUNNING / PARTIAL — broader native-page mapping

Locally established mappings retained from this mapper:
- `041D` SWW Start Temperature, controlled `48 -> 47`
- `041E` Warm Water Time, controlled `30 -> 31`
- `042E` SWW Enabled
- `042F` SWW Mode
- `0433` Opstart HT
- `0434` Verwarmingstijd

Do not promote `0431` or `0432`: they remain **UNKNOWN**. A prior interpretation as Heating START/STOP was explicitly rejected after checking the actual 042E page values.

## Current locally proven writable settings

### 03E8/count14 heating page
- `03E8` Heating Curve
- `03E9` Heating Minimum
- `03EA` Heating Maximum
- `03EB` Curve Correction +5
- `03EC` Curve Correction 0
- `03ED` Curve Correction -5
- `03EE` Heating Stop
- `03EF` Reduced Temperature
- `03F0` Room Factor
- `03F4` Room Setpoint

Unknown on this page: `03F1`, `03F2`, `03F3`, `03F5`. `03F1` is specifically not the live DHW START mapping on this XTR M.

### 042E/count15 DHW/runtime-service page
Proven locally writable:
- `042E` SWW Enabled
- `042F` SWW Mode
- `0433` Opstart HT
- `0434` Verwarmingstijd

`0430` is a **HYPOTHESIS** for Extra Hot Water / Top-up because it is the still-unmapped word adjacent to SWW Enabled/Mode and normally sits at 0 in known pages. It is not yet locally confirmed. `0431` and `0432` remain UNKNOWN.

### 0442/count13 cooling page
Proven locally writable:
- `0442` Cooling Enabled
- `0443` Desired Cooling Temperature
- `0445` Cooling Active Above
- `0449` Cooling Time
- `044C` Cooling Room Sensor
- `044D` Cooling Room Hysteresis Low
- `044E` Cooling Room Hysteresis High

Unknown: `0444`, `0446`, `0447`, `0448`, `044A`, `044B`.

### 0546/count20 mode page
- `0553` Operation Mode: local read-side/panel evidence confirms Auto=1 and Compressor=2.
- Active semantic write is **not yet proven**; that is EXP380.

## Current protocol model

1. Native settings control is page-based and controller-owned, not arbitrary second-master register writing.
2. Each semantic write requires a fresh authoritative controller page.
3. The desired-page selector causes a controller FC03 pull of that exact page.
4. The emulator returns the complete page with exactly one intended word changed.
5. Success is only accepted after an exact controller FC16 republish with the target value and `extraDeltaWords=0`.
6. The same mechanism is now locally proven on pages `03E8`, `042E` and `0442`.
7. The W2:W3 32-page current/PUSH bitmap is strongly supported by genuine DCM/Eco5 captures. For page 0546, W2 bit0 is the current/PUSH bit; the mirrored W0 bit0 desired/PULL interpretation is accepted from genuine/cross-model evidence for EXP380 but is not yet a local semantic-write result.
8. Runtime stage 40 and the serialized desired-state queue remain the known-good experimental foundation.

## Important remaining work

Most everyday XTR M parameters are now mapped. Remaining high-value work is:
- run EXP380 for persistent Operation Mode;
- confirm or reject `0430` as Extra Hot Water / Top-up;
- remaining DHW service settings;
- remaining heating/cooling service settings;
- calendar;
- auxiliary heater;
- shunt groups;
- pool;
- optional buffer-tank/accessory settings where relevant.

## Safety constraints

Continue one-target-at-a-time writes from fresh controller pages, exact page/count validation, one-word deltas, exact controller republish verification, bounded UI values, no automatic retries, parser/RX/peer fail-close, and DE LOW on every abort. Do not promote 0430/0431/0432 or untested Operation Mode values beyond their stated evidence level.

---

# 2026-10-01 — EXP374/375 complete; Write Beta v3.0 production baseline

**Authoritative current state:** EXP374 is **COMPLETE / POSITIVE** by explicit user confirmation of the final v4d behavior. EXP375A and EXP375B are **COMPLETE / POSITIVE** by explicit user confirmation. The production-oriented write baseline is now **Write (Beta) v3.0**, derived from the validated EXP374 v4d engine.

## Last completed experiments

### EXP374 — COMPLETE / POSITIVE — serialized per-register queue + Configuration intent preservation

**Hypothesis:** rapid Home Assistant changes across multiple writable settings can be serialized without overlap, stale-page reuse or loss of distinct register intents.

**Final implementation:** one active semantic transaction plus a bounded per-register dirty-set; same-register latest value wins; different-register intents are preserved. Each dispatched item requires a fresh controller-originated `03E8/count14` page and exact one-word controller republish. Configuration controls show active/queued desired values while ordinary read sensors remain controller-authoritative.

**Result:** user confirmed the final v4d build behaves correctly. In the representative rapid three-control case, requested curve-correction values remained visually stable in Configuration while the controller applied them sequentially. Earlier v4/v4b/v4c implementation defects remain part of the history and are not erased.

**Evidence note:** final v4d success is user-confirmed in chat; no separate raw runtime log for that final run was supplied.

### EXP375A — COMPLETE / POSITIVE — Heating Minimum `03E9`

User explicitly confirmed the planned Heating Minimum write/rollback test succeeded. `03E9` is therefore promoted to **PROVEN / locally confirmed writable** on this XTR M.

### EXP375B — COMPLETE / POSITIVE — Room Factor `03F0`

User explicitly confirmed the planned Room Factor write/rollback test succeeded. `03F0` is therefore promoted to **PROVEN / locally confirmed writable** on this XTR M.

## Current locally proven writable 03E8/count14 fields

- `03E8` Heating Curve
- `03E9` Heating Minimum
- `03EA` Heating Maximum
- `03EB` Curve Correction +5
- `03EC` Curve Correction 0
- `03ED` Curve Correction -5
- `03EE` Heating Stop
- `03EF` Reduced Temperature
- `03F0` Room Factor
- `03F4` Room Setpoint

`03EB` and `03EC` are promoted from the successful rapid multi-setting queue test confirmed by the user. The unknown page words `03F1`, `03F2`, `03F3` and `03F5` remain unknown; prior work specifically disproved `03F1` as live DHW START on this tested XTR M.

## Production write baseline

Current file:

`Write (Beta)/thermia_itec_xtr_m_waveshare_write_beta_v3_0.yaml`

The production baseline retains the validated native desired-page mechanism, fresh-page provenance for every semantic write, per-register dirty queue, exact republish verification, Configuration autosync, desired-intent UI presentation, bounded values and fail-closed parser/RX/peer guards.

## Current protocol model

1. The native `0x0F` settings exchange is page/state based, not an arbitrary second-master register-write scheme.
2. A semantic write begins from an authoritative controller `FC16 03E8/count14`.
3. W3 bit0 obtains the fresh current page; W1 bit0 + W3 bit0 advertises the desired `03E8` page.
4. The controller pulls `FC03 03E8/count14`; the emulator returns the full page with exactly one selected word changed.
5. Success requires the controller to republish `FC16 03E8/count14` with that selected value and zero extra changed words.
6. Multiple user intents are serialized; each queued register gets its own fresh page.
7. Read sensors remain controller-authoritative even while Configuration shows queued desired intent.
8. Controller-session recovery remains separately guarded; the genuine challenge-response transform remains unknown.

## Next research direction

Do not broaden writes blindly. The next research step should first identify the remaining unknown words in the current page (`03F1/03F2/03F3/03F5`) passively, or choose one already mapped setting on another native page and establish its exact controller-originated page/ownership before any write test.

---

# 2026-10-01 — EXP374 PREPARED / NOT RUN; EXP373 RUNNING / PARTIAL

**Authoritative current state:** EXP374 is **PREPARED / NOT RUN**. EXP373 is **RUNNING / PARTIAL** from the supplied local XTR M log and contains multiple independently confirmed semantic-write sub-results. EXP371 and EXP372 are **SUPERSEDED / NOT RUN** as distinct experiments. The last fully completed numbered experiment is EXP370 (**COMPLETE / POSITIVE**).

## Current experiment

### EXP374 — PREPARED / NOT RUN — queued serialized write safety layer

**Baseline:** EXP370 established a reusable serialized semantic-write engine for the native `03E8/count14` settings page. EXP373 then confirmed additional writable settings while keeping the same fresh-page -> selector -> FC03 desired-page -> exact FC16 republish mechanism.

**Hypothesis:** rapid Home Assistant slider changes can be made safer by serializing user intent in a bounded one-slot pending queue without changing any proven Thermia wire frame, register mapping, selector or ACK behavior.

**Exact controlled change from EXP373:** scheduling/safety logic only:
- one active semantic transaction at a time;
- at most one pending user request;
- last user intent wins in the pending slot;
- no TX when merely storing/replacing a pending request;
- after exact controller republish, enforce a settle delay before dispatching a queued request;
- every queued request must obtain a fresh controller-originated `03E8/count14` page before semantic TX;
- clear pending state on negative/inconclusive result, parser/RX fault, peer traffic, timeout or manual abort;
- no automatic retry after a failed semantic write.

No new write address or payload is introduced. First planned queue test uses only locally confirmed targets (Heating Stop and Reduced Temperature).

**Positive criterion:** first write closes with exact controller republish and `extraDeltaWords=0`; queued request then starts only after the safety delay, obtains a new fresh page, and independently closes with exact republish. Parser resync/RX drop/peer counters remain clean and DE returns LOW.

**Negative/abort:** any overlap between semantic transactions, queued TX before the first transaction closes, stale-page reuse, wrong page/count/order, extra changed words, peer responder/ACK, parser resync/RX drop delta, timeout or manual abort.

**Status:** PREPARED / NOT RUN. Do not advance on the basis of generated YAML alone.

## Latest experimental evidence

### EXP373 — RUNNING / PARTIAL — extended heating settings sliders

EXP373 reused the established serialized `03E8/count14` semantic-write path and added settings in `03EB..03F0`. The supplied log proves the following local XTR M writes:

- `03ED` Heating Curve Correction -5: `0 -> -5 -> 0`, represented on the wire as signed int16 (`-5 = 0xFFFB`), exact controller republish, `extraDeltaWords=0`.
- `03EE` Heating Stop: `20 -> 22`, later `22 -> 18 -> 22`, each exact controller republish with `extraDeltaWords=0`.
- `03EF` Reduced Temperature: `20 -> 22 -> 20`, both directions exact controller republish with `extraDeltaWords=0`.
- a no-op `03EF` request where current already equaled target correctly returned READY without semantic page TX.
- in the inspected run, no abort was observed and parser resync/RX drop/challenge/peer-FC17/peer-FC16-ACK counters remained zero.

**Current classification:** the experiment as a whole remains RUNNING / PARTIAL because the complete added target set was not systematically closed in the supplied evidence. The confirmed sub-results above are locally proven.

### EXP370 — COMPLETE / POSITIVE — reusable multi-setting semantic writes

Final conversation-21 interpretation:
- Heating Curve reusable writes included `35 -> 40 -> 30`, exact one-word controller republish, `extraDeltaWords=0`.
- Heating Maximum writes included `40 -> 41 -> 58 -> 40`, exact controller republish, `extraDeltaWords=0`.
- Room Setpoint `20 -> 22` was also confirmed in the reusable engine.
- Heating Minimum was not semantically tested at the attempted `40` value because a local implementation guard required Minimum < Maximum while Maximum was 40. That guard is not Thermia protocol evidence.

This is the last fully completed numbered experiment before the EXP371/372 superseded preparations and the partial EXP373 run.

## Conversation-21 reconciliation (EXP358–EXP372)

The tests from conversation 21 are retained in the experiment log. Key status chain:

- EXP358 — COMPLETE / POSITIVE: Write Beta v2.1 regression; retained runtime qualification, stale-page refresh and exact Room Setpoint write survived hardening; bus counters clean. Conditional fail-closed branches not all exercised.
- EXP359 — COMPLETE / POSITIVE: controller cold-reboot recovery repeated successfully after >5 s silence, full ordered initial sync through `06F4/count19`, stage-40 requalification, clean runtime.
- EXP360 — COMPLETE / INCONCLUSIVE: broad `0708` bitmap `7FFF/FFFF/0000/0006`; intended discriminator not cleanly resolved.
- EXP361 — COMPLETE / NEGATIVE: expected `0708` event did not occur.
- EXP362 — COMPLETE / INCONCLUSIVE: intended bitmap was never transmitted.
- EXP363 — COMPLETE / NEGATIVE for the specific `04A6 -> 0708` hypothesis; however, ACKing exact `04A6/count13` resumed the interleaved export sequence.
- EXP364 — COMPLETE / INCONCLUSIVE: no `04A6` discriminator occurred; a fresh-boot/hot-rejoin-style runtime without new R1/bitmap remained stable for >5.5 min, but native hot-rejoin semantics were not proven.
- EXP365 — COMPLETE / POSITIVE: Heating Curve `30 -> 31`, exact republish, one-word delta.
- EXP366 — COMPLETE / POSITIVE: Heating Curve `31 -> 30`, exact inverse republish.
- EXP367 — COMPLETE / POSITIVE: Heating Curve `30 -> 35`; one-shot guard blocked a second semantic write.
- EXP368 — COMPLETE / INCONCLUSIVE: Curve `35 -> 32` itself succeeded, but a verifier-latch bug allowed a later Apply to overwrite the selected register/word before verification.
- EXP369 — COMPLETE / POSITIVE for the latch-fix objective: Curve `32 -> 35` confirmed; a later Room Setpoint Apply was refused before it could overwrite the active selection. One-shot behavior still prevented a second semantic transaction.
- EXP370 — COMPLETE / POSITIVE: one-shot restriction removed for the proven serialized engine; reusable Curve, Heating Maximum and Room Setpoint writes confirmed.
- EXP371 — SUPERSEDED / NOT RUN as a distinct experiment. Its planned unrestricted Min/Max test was absorbed into the later audited build; Maximum results discussed at that point belong to EXP370.
- EXP372 — SUPERSEDED / NOT RUN. Its added `03EB..03F0` slider design was replaced by EXP373 before a distinct run.

## Current protocol model

1. The controller-to-DCM configuration export and DCM desired-page path are stateful and page-based rather than arbitrary direct register writes.
2. A semantic write uses a fresh controller-originated `03E8/count14` page as provenance.
3. The desired-page selector causes the controller FC03 pull; the emulator returns the full page with exactly one intended word changed.
4. Success requires the controller to republish `FC16 03E8/count14` with exactly the requested word changed and no extra deltas.
5. This mechanism is reusable within a healthy stage-40 runtime; it is no longer limited to Room Setpoint or to a single semantic write.
6. Controller cold-reboot recovery and retained-runtime qualification remain separately guarded lifecycle paths.
7. Queueing/scheduling safety is not yet proven; that is the sole objective of EXP374.

## Locally proven writable settings in the 03E8 page

- `03E8` Heating Curve — PROVEN writable.
- `03EA` Heating Maximum — PROVEN writable.
- `03ED` Heating Curve Correction -5 — PROVEN writable, signed int16.
- `03EE` Heating Stop — PROVEN writable.
- `03EF` Reduced Temperature — PROVEN writable.
- `03F4` Room Setpoint mirror/desired value — PROVEN writable through the native desired-page flow.

Read-side mappings for `03E9`, `03EB`, `03EC`, `03F0` remain useful, but writeability is not promoted here without a clean local confirmation.

## Important unknowns

- `03E9` Heating Minimum writeability is still unproven; the only recent attempt was blocked locally before semantic TX.
- `03EB` Curve Correction +5, `03EC` Curve Correction 0 and `03F0` Room Factor are not yet locally write-confirmed in the supplied EXP373 evidence.
- Native hot-rejoin/rejoin bitmap behavior remains incompletely understood; EXP360–364 did not prove a general no-R1 shortcut.
- The native challenge-response transform remains unknown; the fixed R1 is still only a locally proven replay for this XTR M/context.
- Queue behavior under rapid UI changes remains unproven until EXP374 is run.

## Safety constraints

Continue to use fresh full-page provenance, one-word semantic deltas, exact republish verification, one active transaction, DE-low fail-closed behavior, bounded values, clean parser/RX/peer counters and explicit abort handling. Do not infer Thermia-level ordering constraints such as Minimum < Maximum from a local UI/software guard unless the controller itself demonstrates them.

---

# 2026-10-01 — Write Beta v2.1 hardened; EXP358 PREPARED / NOT RUN

**Authoritative current state:** EXP357 remains the last completed experiment and is **COMPLETE / POSITIVE**. Write Beta v2.1 has been prepared from the v2 production code audit but has **not yet been live-regression-tested**. EXP358 is the next experiment and is **PREPARED / NOT RUN**.

## Production hardening — Write Beta v2.1

Current production-beta candidate:

`Write (Beta)/thermia_itec_xtr_m_waveshare_write_beta_v2_1.yaml`

This revision adds **no new writable register, page, bitmap bit, R1 payload or ACK shape**. It only narrows behavior to the current canonical evidence and fixes production-state reporting.

Controlled implementation changes from v2:

- runtime `04A6/count13` is now explicit **capture-only / NO ACK** in stage 40;
- runtime `0834/count18` is removed from the ACK whitelist and fails closed with no TX;
- runtime `085F/count5` is ACKed only for the two locally proven payload forms: all-zero or third word/register `0861=0x0800`;
- `080C/0820/0848/0864/0870/0884` are documented in code as locally ACK-proven rather than genuine-capture-only where canonical experiments already established them;
- runtime qualification is centralized so FC16-first and `0708`-first ordering both converge on the same qualification latch;
- **Thermia DCM Runtime Active** is false until qualification is actually complete;
- write arming now requires that explicit runtime-qualified latch in addition to the existing clean-counter guards;
- controller-recovery arming also requires the explicit qualified latch;
- the 15-minute soak milestone is re-armed after controller recovery;
- firmware build label is corrected to `Write Beta v2.1`;
- the Room Setpoint number entity is genuinely disabled by default;
- recovery/session diagnostics were added without changing protocol TX behavior.

Static checks after hardening:
- no duplicate ESPHome IDs;
- no missing `id(...)` references;
- every DE-high TX site still contains write + flush + DE-low in the same local path;
- critical hard-coded CRCs remain unchanged/correct from the proven v2 paths.

**No ESPHome compile was performed in this preparation step.**

## Current experiment

### EXP358 — PREPARED / NOT RUN — v2.1 production regression

**Baseline:** EXP357 COMPLETE / POSITIVE for reusable stale-cache refresh + semantic write; EXP355 COMPLETE / POSITIVE for controller cold-reboot recovery.

**Hypothesis:** the v2.1 safety hardening preserves the already-proven retained runtime, reusable stale-cache refresh and guarded `03F4` write path while removing unsupported/permissive runtime ACK behavior.

**Exact controlled change:** firmware implementation only. No new Thermia semantic target or wire payload is introduced.

**Planned positive criteria:**
- retained stage 40 qualifies through at least one locally ACK-proven runtime FC16 plus exact `0708/count6`;
- `Thermia DCM Runtime Active` becomes true only after that qualification;
- ordinary runtime continues with parser resync/RX drop/peer-responder counters clean;
- if runtime `04A6/count13` appears, it is logged capture-only with **NO ACK** and runtime continues;
- `0834/count18`, if encountered, receives **NO ACK** and fails closed;
- unknown `085F/count5` payload receives **NO ACK** and fails closed; locally proven all-zero / `0861=0800` forms remain serviceable;
- one stale-cache refresh can again obtain fresh controller `FC16 03E8/count14`;
- one Room Setpoint write completes through W1 selector -> controller FC03 -> one-word `03F4` desired page -> exact controller republish with zero extra delta words.

**Negative criteria:** any regression in qualification, refresh, selector/pull, exact republish or known runtime service; any TX to runtime `04A6` or `0834`; or any acceptance of an unknown `085F` payload.

**Abort criteria:** parser resync/RX drop delta, external responder, unexpected runtime FC03/FC16 outside explicit handlers, wrong page/count/order during active semantic transaction, or DE not returning low.

**Status:** PREPARED / NOT RUN. Do not promote v2.1 beyond beta until the user supplies the EXP358 result/log or explicitly confirms the run.

# 2026-10-01 — EXP357 COMPLETE / POSITIVE; Write Beta v2 promoted

**Authoritative current state:** EXP357 is **COMPLETE / POSITIVE** from the supplied local XTR M raw log. EXP356 is **SUPERSEDED / NOT RUN** because the user chose to install the next targeted write test instead. EXP355 remains **COMPLETE / POSITIVE** for controller cold-reboot recovery.

## Last completed experiment

### EXP357 — COMPLETE / POSITIVE — reusable stale-cache refresh in one ESP boot

**Hypothesis:** after the `03E8` semantic cache becomes stale again later in the same ESP boot, the proven W3-bit0 refresh-only flow can be reused and followed by the existing safe Room Setpoint semantic write.

**Controlled change from EXP355:** remove only the experimental one-refresh-per-ESP-boot budget. Keep the 300 s stale threshold, W3-bit0 refresh frame, controller-originated `FC16 03E8/count14` freshness requirement, W1-bit0 selector, `03F4`-only delta and exact controller republish confirmation.

### Observed facts

- Refresh #1 produced controller `FC16 03E8/count14` in about 120 ms and was followed by a confirmed 22 -> 20 °C write.
- Later in the same ESP boot, refresh #2 was transmitted with the same W3-bit0 frame and produced controller `FC16 03E8/count14` in about 119 ms.
- Refresh #2 was followed by the normal selector -> controller FC03 -> one-word-delta desired page -> exact controller republish path.
- The resulting 22 -> 24 °C write was confirmed with `extraDeltaWords=0`.
- The supplied run reached five confirmed semantic writes.
- Runtime remained clean in the inspected log: unknown FC16/FC03, peer responder, parser resync and RX drop counters remained zero; DE returned low.

### Strong conclusion

**PROVEN / locally confirmed:** stale-cache refresh via `0708` W3 bit0 is reusable in the same retained ESP session. The old one-refresh-per-ESP-boot safety budget is obsolete for this XTR M and has been removed from Write Beta v2.

## Production status

`Write (Beta)/thermia_itec_xtr_m_waveshare_write_beta_v2.yaml` was the production-beta baseline promoted after EXP357; it is now superseded by the hardened v2.1 candidate pending EXP358.

It combines:
- the locally proven retained runtime and Room Setpoint write path;
- reusable stale-cache refresh proven by EXP357;
- one controller cold-reboot recovery attempt per ESP boot using the EXP355-proven guarded fresh-session path.

The previous v1 file remains as the pre-recovery production-beta baseline.

# 2026-09-30 — EXP356 PREPARED / NOT RUN; EXP355 COMPLETE / POSITIVE

**Authoritative current state:** EXP355 is **COMPLETE / POSITIVE** from the supplied local XTR M log. EXP356 is **PREPARED / NOT RUN** as the next post-recovery soak. EXP354 was not run. EXP353 remains **COMPLETE / POSITIVE** by user confirmation; EXP352 remains the latest earlier experiment with full raw-log proof of the complete refresh -> write -> republish path.

## Offline capture re-analysis — 2026-10-01

No new bus experiment was run. Existing genuine DCM/Online and collaborator Eco5 gateway captures were re-analysed against the now-locally-proven EXP352/355 model.

### New durable cross-capture evidence

- **STRONGLY SUPPORTED / genuine DCM + Eco5 capture evidence:** `0708` W2:W3 is a 32-page current/PUSH bitmap covering the ordered config pages from `03E8` through `06F4`. The externally observed bitmap is consistent with W3 bits 0..15 mapping `03E8..0532` and W2 bits 0..15 mapping `0546..06F4`.
- **Direct cross-capture checks:** W3 bit15 + W2 bit14 is followed by controller pages `0532` and `06F1`; W2 bit15 is followed by `06F4/count19`. This materially strengthens the full bitmap model, while only W3 bit0 -> `03E8` remains locally active-tested on this XTR M.
- **STRONGLY SUPPORTED desired-page indexing:** genuine Online/DCM capture evidence shows W1 bit0 followed by controller `FC03 03E8`; genuine Eco5 gateway evidence shows W1 bit3 followed by controller `FC03 042E/count15`. This supports W1 using the same page-index family for desired/PULL selection.
- **PROVEN / genuine Eco5 gateway capture:** the 16-byte response to the exact `071C/0730` challenge is not constant across sessions. Different challenges receive different response payloads.
- **PROVEN / locally confirmed XTR M:** despite that native variability, EXP355 successfully replayed the previously captured fixed response `1691A5F3F8E8D58738924416E8E6A3D5` under the known cold-boot guard and completed the full initial sync. Therefore the fixed payload is a locally proven replay for this unit/context, not a universal Thermia/Danfoss challenge-response value.
- **STRONGLY SUPPORTED lifecycle interpretation:** existing genuine capture evidence is consistent with at least two native integration paths: controller cold boot with challenge/response + initial sync, and accessory/gateway rejoin to an already-running controller via a `0708` page bitmap followed by controller page export. The latter is not yet locally emulated.

### Consequence for production recovery

The production-recovery design remains valid for this XTR M, but documentation/code comments must describe the fixed R1 as a **locally proven replay** rather than the native universal response algorithm. Do not generalize the replay to other Thermia models/firmware. The native challenge-response transform remains unknown.

## Historical prepared experiment

### EXP356 — SUPERSEDED / NOT RUN — post-recovery runtime soak

EXP356 had been prepared after EXP355 but was never run. The user chose the targeted EXP357 reusable-refresh test instead. No EXP356 result is inferred.

## Last completed experiment

### EXP355 — COMPLETE / POSITIVE — controller cold-reboot recovery without ESP reboot

**Baseline:** EXP353 COMPLETE / POSITIVE, using the EXP352-derived fresh-session/retained-runtime state machine.

**Hypothesis:** a running ESP/DCM emulator already in a healthy qualified retained stage-40 runtime can recover after a real Thermia-controller power cycle without rebooting the ESP by reusing the established fresh-session bootstrap.

**Controlled protocol change:** no new writable register/page or semantic payload. EXP355 only made the existing fresh-session stages reachable again from qualified stage 40 after a clearly detected controller outage.

### Observed facts

- Before the controller power cycle, retained stage 40 was healthy and repeatedly qualified with known runtime FC16 ACK service and exact `0708/count6` idle replies.
- Normal pre-reboot state observations repeatedly showed `A80E=0000 / A80F=000A`.
- EXP355 detected `5166 ms` bus silence while runtime was qualified and `writeState=0`, armed one recovery attempt, invalidated the semantic cache and kept DE low.
- Bus traffic returned about `10.072 s` after recovery was armed.
- The first valid returned frame promoted the state machine to fresh-boot stage 2.
- The cold-boot guard became `A80E=0000 / A80F=0005`.
- The first exact `071C/0730` challenge passed that guard and triggered exactly one known R1:
  `0F17101691A5F3F8E8D58738924416E8E6A3D5E227`.
- The first post-R1 settings publication was exact `FC16 03E8/count14`; it contained `03F4=22` and became the new same-session semantic cache.
- The existing 32-stage ordered initial-sync sequence completed through `06F4/count19`.
- Final `06F4/count19` was ACKed about `32.252 s` after R1 and returned the emulator to stage 40.
- Immediately after stage-40 re-entry, controller `FC16 085F/count5` was serviced and ACKed.
- A fresh `0708/count6` exchange then completed post-recovery qualification.
- EXP355 logged `RECOVERY_POSITIVE success=1 runtimeFC16ACK=1 idle0708=1 r1Used=1 cacheValid=1 writeState=0 DE=LOW`.
- Recovery arm -> positive post-recovery qualification took about `45.297 s`.
- A later heartbeat remained clean with `runtimeFC16ACK=22`, `idle0708=12`, `unknown16=0`, `unknown03=0`, `peer17=0`, `peer16ack=0`, `resync=0`, `drops=0`, `DE=LOW`, and `cache03F4=22`.
- No STOP, ABORT or INCONCLUSIVE event was observed after recovery armed in the supplied log.

### Additional state progression observed

During the recovered fresh session:

`A80E/A80F = 0000/0005 -> 0008/0005 -> 0028/0005 -> 0028/000A`

This is an observation only. The abstract semantics of A80E/A80F remain open.

## Strong conclusions

**PROVEN / locally confirmed:** an already-running ESP/DCM emulator can recover from a real Thermia-controller power cycle without an ESP reboot.

**PROVEN / locally confirmed:** in the tested setup, sustained >=5 s observed bus silence from a healthy qualified stage 40 can safely gate re-entry into the already established fresh-session bootstrap.

**PROVEN / locally confirmed:** the recovered controller session reproduces the guarded chain:
`bus return -> A80E=0000/A80F=0005 -> exact 071C/0730 challenge -> one R1 -> ordered initial-sync -> stage 40 -> fresh runtime FC16 + 0708 qualification`.

**PROVEN / locally confirmed:** the new-session controller `FC16 03E8/count14` publication re-establishes semantic cache provenance; EXP355 observed `03F4=22`.

## Current protocol/lifecycle model

1. retained Online/DCM stage-40 runtime may survive ESP OTA/reboot;
2. retained runtime qualification uses known FC16 service plus exact idle `0708/count6` with W5=`0006`;
3. stale/missing `03E8` may be refreshed by W3 bit0 and controller `FC16 03E8/count14`;
4. desired `03F4` uses W1-bit0 selector -> controller FC03 -> one-word-delta page -> exact controller republish;
5. if the Thermia/controller cold-reboots while the ESP remains powered, a qualified stage-40 emulator can detect sustained bus silence and re-enter the fresh-session bootstrap;
6. fresh-session recovery uses the guarded exact `071C/0730` challenge, one known R1, and the established ordered initial-sync ACK chain;
7. completion of `06F4/count19` re-enters stage 40;
8. new runtime FC16 + `0708` service requalifies the recovered session.

## Important unknowns / limits

- EXP355 proves one controller power-cycle recovery in the supplied run; repeated controller cold-reboot recoveries in one ESP boot are not yet locally proven.
- EXP355 intentionally did not perform a semantic room-setpoint write after recovery; the user explicitly chose to skip that combination test.
- The exact abstract meanings of A80E and A80F remain unknown.
- The official 16-byte challenge-response transform is unknown; genuine gateway responses vary per challenge/session. The fixed `1691...A3D5` payload is only a locally proven replay on this XTR M.
- Native hot-rejoin via `0708` page-bitmap advertisement is strongly supported by genuine captures but has not been locally emulated.
- The >=5 s silence threshold is a locally proven implementation discriminator, not a universal Thermia protocol requirement.
- Recovery from arbitrary interruption points within the initial-sync chain is untested.
- Full W2:W3 behavior beyond W3 bit0 / `03E8` remains unproven locally.
- Other writable settings/registers remain unproven; active semantic writes stay limited to `03F4`.
- W0, W4 and the abstract meaning of W5 remain open.
- The separate native/controller-originated 22 °C event from EXP352 remains unattributed; the 19 °C event is explicitly correlated to the Thermia front display.

## Safety constraints

No broad writes, scans or unknown-value injection. Semantic control remains limited to locally mapped `03F4` inside `03E8/count14`, using only a fresh controller-originated/confirmed full page and changing one word. Keep 10..30 °C whole-degree guards, one outstanding transaction, exact republish verification and fail-closed handling. Recovery remains gated on a previously healthy qualified runtime and the known guarded fresh-session path.

---

# 2026-09-30 — EXP352 COMPLETE / POSITIVE; retained runtime, fresh-page refresh and native coexistence proven

**Authoritative current state:** EXP352 is **COMPLETE / POSITIVE** from the supplied local XTR M log plus the user's direct confirmation that there was **no alarm** and the DCM icon remained visible. EXP351 is **COMPLETE / INCONCLUSIVE** because its intended refresh hypothesis was never reached due to an implementation gate. EXP350 is **COMPLETE / INCONCLUSIVE** for the full soak-write hypothesis, with positive automatic-retained-runtime sub-results.

## Current experiment/result

### EXP352 — COMPLETE / POSITIVE

**Hypothesis:** retained stage-40 Online/DCM runtime does not require a hard-coded boot-time `03E8/count14` page image. Runtime service and semantic-write page provenance can be separated: start/qualify the retained runtime with no write-eligible `03E8` cache, obtain a fresh controller-originated `03E8` page only when needed via the 0708 current-page/PUSH path, then use the already-proven guarded semantic write flow.

**Controlled change from EXP351:** remove the hard-coded historical `03E8` handover equality gate that prevented stage-40 entry when the real setpoint no longer matched the old page; seed no valid/write-eligible `03E8` page at boot; preserve the known-good retained runtime service and the bounded W3-bit0 refresh-only path.

### Observed facts

- After ESP OTA/reboot, retained stage 40 qualified automatically with no Thermia-controller reboot and no new R1/bootstrap.
- Runtime service remained clean: known controller FC16 pages were ACKed, exact idle `0708/count6` service continued with W5=`0006`, and relevant challenge/unknown/peer/resync/drop counters remained zero in the observed run.
- The boot-time semantic page cache was intentionally invalid.
- On the first Apply with target 25 °C and no valid cache, EXP352 armed refresh only; no semantic page was transmitted.
- On the next exact `FC03 0708/count6`, EXP352 sent:
  `W0..W5 = 0000 0000 0000 0001 0000 0006`
  frame `0F030C000000000000000100000006A0B6`.
- About 120 ms later, the controller itself published `FC16 03E8/count14` with current `03F4=23`; the log reported `REFRESH_CONFIRMED ... W1=0000 W3bit0=1 NO_DESIRED_PULL=1 CACHE_FRESH=1`.
- The proven desired-page flow then wrote 23 -> 25 °C and the controller confirmed the exact page with `extraDeltaWords=0`.
- Six ESP-originated semantic writes were confirmed in the same retained runtime:
  `23 -> 25 -> 17 -> 23 -> 21`, then after a native/controller-originated update `22 -> 21`, then after another native update `19 -> 21`.
- While no ESP semantic write was pending, the controller independently published a new `03E8/count14` with `03F4=22`; EXP352 promoted that controller page to the live cache.
- Later the controller independently published `03F4=19`; the user explicitly confirmed that **19 °C was set on the Thermia front display**. EXP352 again promoted that page to the live cache.
- The following ESP write used the newly observed native value as its source (`19 -> 21`), showing that a physical Thermia change is not overwritten from stale cached state.
- User confirmed **no alarm** and **DCM icon still visible** after the run.

## Strong conclusions

**PROVEN / locally confirmed:** retained Online/DCM runtime qualification on this XTR M does not require a hard-coded historical `03E8` page image. Semantic page provenance can be kept separate from runtime/session liveness.

**PROVEN / locally confirmed:** in the tested stage-40 context, `0708` **W3 bit0** with W1=0 requests a fresh current `03E8` page. The controller responded with its own `FC16 03E8/count14` publication and no desired-page FC03 pull occurred first. This upgrades W3 bit0 / page 03E8 from genuine-capture evidence to local XTR proof.

**PROVEN / locally confirmed:** controller-originated `03E8` publications during normal runtime can safely refresh the source cache for later guarded room-setpoint writes. A Thermia-front-display change to 19 °C was observed as controller `FC16 03E8/count14` with `03F4=19`.

**PROVEN / locally confirmed:** the combined flow
`fresh-page refresh -> guarded semantic write -> exact controller republish -> continued runtime`
works while the DCM icon remains present and no Online/Link alarm is observed.

## Current protocol model

The locally proven bidirectional cache model now includes:

1. retained controller-side Online/DCM session surviving ESP OTA/reboot;
2. automatic retained stage-40 qualification without manual Arm, Thermia reboot or new R1;
3. persistent runtime FC16 service;
4. idle `0708` service with W5=`0006`;
5. W3 bit0 current-page/PUSH request for `03E8`;
6. controller-originated `FC16 03E8/count14` refresh;
7. W1 bit0 desired-page/PULL selector for `03E8`;
8. controller `FC03 03E8/count14` desired-page read;
9. desired page changing only locally mapped `03F4`;
10. exact controller FC16 republish confirming semantic application;
11. promotion of any new controller-originated/confirmed `03E8` page to the next-write source;
12. coexistence with native Thermia-front-display changes during the same persistent DCM runtime.

The **full** W2:W3 32-bit page map remains strongly supported by genuine DCM/Eco5/ATEC captures; only W3 bit0 -> `03E8` is now locally active-tested. W0, W4 and the abstract meaning of W5 remain open.

## Immediately preceding results

### EXP351 — COMPLETE / INCONCLUSIVE
The planned W3-only stale-cache refresh test was **not reached**. Automatic stage-40 entry was incorrectly gated on persisted settings matching a hard-coded historical `03E8` handover image, including an old 22 °C setpoint. With live state changed, the experiment returned before activating the emulator. User observed alarm/no retained runtime. No valid protocol conclusion about W3 refresh is drawn from EXP351 itself; EXP352 removed the faulty gate and tested the intended hypothesis.

### EXP350 — COMPLETE / INCONCLUSIVE
Automatic retained-session qualification without a manual Arm control worked and the DCM presentation remained healthy; user confirmed no error and icon still visible. The later setpoint write was correctly refused because `cacheValid=1` but the `03E8` source cache was about 715 s old, beyond the 300 s freshness guard. This exposed the need for an explicit fresh-page request before long-interval writes rather than weakening the freshness guard.

## Important unknowns / limits

- EXP352 actively exercised **one** W3-bit0 refresh-only request per ESP boot. Repeated stale-cache refresh cycles in one long-lived boot are not yet locally proven.
- Full W2:W3 page-refresh bitmap behavior beyond bit0/page 03E8 remains genuine-capture-supported rather than locally proven.
- The source of the separate native/controller-originated 22 °C event is unresolved because both room-sensor and Thermia controls were used during the run. Do not label that event specifically as a room-sensor change.
- Other writable settings/registers remain unproven; active writes stay limited to `03F4`.
- W0, W4 and W5 field semantics remain open; W5=`0006` is a proven working runtime value, not a proven “connected flag.”

## Next experiment

**EXP353 — NOT YET PREPARED / NOT RUN.**

Preferred controlled change: keep the complete EXP352 protocol path unchanged, but replace the **one-refresh-per-ESP-boot experimental budget** with a still-bounded reusable refresh mechanism (for example, several rate-limited refreshes in one boot). Validate at least three stale-cache cycles separated by >300 s, with each cycle:
`Apply -> W3-bit0 refresh -> controller FC16 03E8 -> guarded W1-bit0 write -> exact republish -> READY`.
Include at least one native Thermia/display change between cycles and verify that it becomes the next source cache. Do not introduce a second writable setting in the same experiment.

## Safety constraints

No broad writes, scans or unknown-value injection. Semantic control remains limited to locally mapped `03F4` inside `03E8/count14`, using only a fresh controller-originated/confirmed full page and changing one word. Keep 10..30 °C whole-degree guards, one outstanding transaction, exact republish verification and fail-closed handling. Unexpected session challenges, unknown FC16/FC03, peer responders, parser resyncs or RX drops remain abort conditions. Preserve the known-good W5=`0006` persistent runtime. Thermia-controller reboot is recovery only if an abnormal Online/Link state actually occurs.

---

# 2026-09-30 — EXP349 COMPLETE / POSITIVE; reusable HA-selected room-setpoint writes proven in one retained DCM session

**Authoritative current state:** EXP349 is **COMPLETE / POSITIVE** from the supplied local XTR M log plus the user's direct confirmation that it worked perfectly. EXP348 and EXP347 are also **COMPLETE / POSITIVE**. EXP350 is **NOT YET PREPARED / NOT RUN**.

## Current experiment/result

### EXP349 — COMPLETE / POSITIVE

**Hypothesis:** the locally proven HA-selected `03F4` desired-page write can be reused repeatedly in one retained stage-40 Online/DCM session, with each new transaction built from the latest exact controller-republished `03E8/count14` page.

**Controlled change from EXP348:** remove the one-write-plus-rollback limitation and allow repeated guarded writes. After every exact controller republish, promote that page to the source cache for the next write and return to READY. The experimental budget remained bounded to eight semantic responses per ESP boot. No new page, register, selector encoding or runtime ACK shape was introduced.

### Observed facts

- EXP349 was entered from the retained EXP348 controller session after ESP OTA; no Thermia-controller reboot and no new R1/bootstrap were used.
- Retained runtime qualification was repeatedly observed from known FC16 service plus exact `0708/count6` idle service with:
  `W0..W5 = 0000 0000 0000 0000 0000 0006`.
- Before semantic writes, runtime health remained clean: no new challenge, unknown FC16/FC03, peer responder, parser resync or RX drop.
- First reusable write:
  - current `03F4=22`, requested `16`;
  - selector `0000 0001 0000 0001 0000 0006`;
  - desired page changed only `03F4: 22 -> 16`;
  - controller republished exact `03E8/count14`;
  - `WRITE_CONFIRMED writeNo=1 ... extraDeltaWords=0 ... NEXT_SOURCE=CONTROLLER_REPUBLISH ... READY_AGAIN=1`;
  - Home Assistant `Room Setpoint Mirror` and normal `Room Setpoint` reached 16 °C.
- Second reusable write:
  - current `03F4=16`, requested `24`;
  - exact same native selector/pull path;
  - controller republished exact page with `03F4=24`;
  - `WRITE_CONFIRMED writeNo=2 ... extraDeltaWords=0 ... READY_AGAIN=1`;
  - Home Assistant reflected 24 °C.
- Third reusable write:
  - current `03F4=24`, requested `22`;
  - controller republished exact page with `03F4=22`;
  - `WRITE_CONFIRMED writeNo=3 ... extraDeltaWords=0 ... READY_AGAIN=1`;
  - EXP349 status became `COMPLETE / POSITIVE / 3+ reusable writes confirmed / runtime continues`;
  - Home Assistant returned to 22 °C.
- User directly confirmed the sequence worked perfectly.
- The 10..30 °C protection is implemented both in the HA number limits and in the write lambda; out-of-range current or requested values are fail-closed. This limit is a locally observed native indoor-sensor/UI range, not a claimed universal protocol range.

## Strong conclusions

**PROVEN / locally confirmed:** on this XTR M, the native Online/DCM mailbox + desired-page path for mapped register `03F4` is reusable for multiple semantic setpoint writes inside one continuously retained stage-40 session. The exact controller republish from one successful write can be promoted to the source page for the next write.

**PROVEN / locally confirmed:** a single retained session successfully carried the tested chain `22 -> 16 -> 24 -> 22 °C`, with `extraDeltaWords=0` on all three controller confirmations and continued stage-40 runtime.

**PROVEN / locally confirmed:** changing the HA number alone does not transmit a semantic write; the explicit Apply action is required. Requested/current values outside 10..30 °C are refused by local implementation guards.

## Current protocol model

Locally proven integration chain now includes:
1. retained controller-side Online/DCM session surviving ESP OTA/reboot;
2. requalification without Thermia reboot or new R1;
3. persistent stage-40 runtime FC16 service;
4. idle `0708` mailbox with W5=0006 preserving DCM-connected presentation in the tested context;
5. W1 bit0 desired-page selector for `03E8`;
6. controller FC03 `03E8/count14` pull;
7. same-session desired page changing only mapped `03F4`;
8. exact controller FC16 republish confirming the requested setpoint;
9. promotion of that republish to the next-write source cache;
10. repeated semantic writes in the same session without rebootstrap.

W1 as low desired-page/PULL bitmap and W2:W3 as current-page/PUSH bitmap remain strongly supported. W0, W4 and the exact semantic meaning of W5 remain open. W5=0006 is proven only as sufficient for persistent DCM indication in the tested local context.

## Immediately preceding results

### EXP348 — COMPLETE / POSITIVE
HA-selected generic target was locally proven with `22 -> 24 -> 22 °C`. The controller confirmed both the write and explicit rollback with `extraDeltaWords=0`; Room Setpoint followed; retained runtime stayed clean. EXP348 remained intentionally one write plus one rollback.

### EXP347 — COMPLETE / POSITIVE
After ESP OTA/reboot, the existing controller-side stage-40 session was rejoined **without Thermia-controller reboot and without new R1/bootstrap**. Retained runtime qualification succeeded, then the guarded `03F4` write/rollback worked while the user confirmed the DCM icon stayed visible, no error appeared and the temperature changed/restored correctly.

## Next experiment

**EXP350 — NOT YET PREPARED / NOT RUN.**

Preferred controlled change: remove the manual experiment Arm button. After ESP boot/OTA, automatically enter passive retained-session qualification. Do not permit semantic writes until the same EXP349 clean-runtime requirements are satisfied. Keep only the explicit HA desired-setpoint control + Apply trigger for active semantic writes. Preserve all existing 10..30 guards, cache freshness, exact republish verification, fail-closed behavior and bounded write budget unless EXP350 explicitly tests a different one.

## Safety constraints

No broad writes, scans or unknown-value injection. Semantic control remains limited to locally mapped `03F4` inside `03E8/count14`, using the latest controller-originated/confirmed full page and changing one word only. Exact stage/function/start/count/session and runtime-health guards remain mandatory. Unexpected traffic is capture-only/fail-closed. An abnormal Online/Link state remains a stop condition; Thermia-controller reboot is recovery only if such an abnormal state actually occurs.

---

# 2026-09-30 — EXP346 COMPLETE / POSITIVE; guarded semantic write + rollback inside persistent DCM runtime

**Authoritative current state:** EXP346 is **COMPLETE / POSITIVE** from supplied local XTR M logs plus the user's direct Thermia-screen observation. EXP345 remains the proven persistent-connected baseline. EXP347 is **NOT YET PREPARED / NOT RUN**.

## Current experiment/result

### EXP346 — COMPLETE / POSITIVE

**Hypothesis:** the native desired-page write path proven in EXP343 can be executed inside the persistent EXP345 Online/DCM runtime without dropping the DCM-connected presentation.

**Controlled change from EXP345:** preserve the entire EXP345 fresh-session bootstrap, ordered initial sync, stage-40 runtime FC16 whitelist/ACK scheduler and idle 0708 W5=0006 behavior; add exactly one guarded 03E8/count14 desired-page write plus one explicit rollback using a same-session controller-originated page cache. No other settings words are intentionally changed.

### Observed facts

- Fresh session entered stage 40 normally and continued serving persistent runtime with idle mailbox:
  `W0..W5 = 0000 0000 0000 0000 0000 0006`.
- Initial same-session controller FC16 `03E8/count14` cached `03F4=22`.
- User armed one guarded write:
  `current03F4=22 -> target03F4=21`.
- On the next exact `0708/count6` request, emulator returned selector:
  `W0..W5 = 0000 0001 0000 0001 0000 0006`
  with frame `0F030C000000010000000100000006AD26`.
- Controller then issued exact `FC03 03E8/count14`.
- Emulator answered with the same-session 14-word page, changing only `03F4: 0016 -> 0015`:
  `0F031C0024001400280000000000000014001400020028001E000100150002C29F`.
- Controller republished exact `FC16 03E8/count14` with `03F4=0015`.
- EXP346 verification reported:
  `WRITE_CONFIRMED original03F4=22 target03F4=21 observed03F4=21 extraDeltaWords=0 semanticResponses=1 KEEP_W5_0006=1 CONTINUE_RUNTIME=1`.
- Home Assistant `Room Setpoint Mirror` and then normal `Room Setpoint` both reached 21 °C.
- User confirmed the DCM icon remained visible and no Online/Link error appeared.
- Explicit rollback was then armed while cached `03F4=21`.
- Emulator repeated the same native selector/pull flow and returned the same-session page with only `03F4: 0015 -> 0016`:
  `0F031C0024001400280000000000000014001400020028001E000100160002329F`.
- Controller republished exact `FC16 03E8/count14` with `03F4=0016`.
- EXP346 verification reported:
  `ROLLBACK_CONFIRMED original03F4=22 observed03F4=22 extraDeltaWords=0 semanticResponses=2 KEEP_W5_0006=1 CONTINUE_RUNTIME=1`.
- Home Assistant `Room Setpoint Mirror` and normal `Room Setpoint` returned to 22 °C.
- User again confirmed DCM icon still visible and no Online/Link error.

## Strong conclusion

**PROVEN / locally confirmed:** on this XTR M, a guarded native 03E8 desired-page semantic change can be applied and rolled back inside the long-lived stage-40 Online/DCM-emulation runtime while W5=0006 preserves the DCM-connected presentation. The controller itself republishes the changed page, and in EXP346 the only page-word delta on both write and rollback was 03F4.

This upgrades the local model from “semantic write works” (EXP343) plus “persistent connected runtime works” (EXP345) to **both functions working together in the same session**.

## Current protocol model

Locally proven integration chain now includes:
1. fresh challenge / accepted fixed-R1 entry;
2. ordered full initial FC16 sync;
3. persistent stage-40 runtime FC16 service;
4. idle 0708 mailbox with W5=0006 retaining DCM indication;
5. authentic W1 bit0 desired-page selector for 03E8;
6. controller-initiated FC03 03E8/count14 pull;
7. same-session cloned desired page with exactly one 03F4 delta;
8. controller FC16 republish confirming semantic application;
9. continued persistent runtime after the write;
10. second native transaction restoring the original 03F4 value;
11. continued DCM indication and no observed Online/Link error through write and rollback.

W1 as low desired-page/PULL bitmap and W2:W3 as current-page/PUSH bitmap remain strongly supported. W0, W4 and the exact semantic meaning of W5 remain open. W5=0006 is proven only as sufficient for DCM-indication persistence in the tested local context.

## Next experiment

**EXP347 — NOT YET PREPARED / NOT RUN.** Preferred target: test **reusability of the proven semantic path within one already-established persistent session** without a new controller reboot: one additional bounded user-requested 03F4 setpoint change, using the latest controller-originated same-session page as source, followed by exact controller republish verification and rollback. Exact target, freshness bound, write budget and abort criteria must be fixed before YAML generation.

## Safety constraints

No broad writes/scans or unknown-value injection. Semantic writes remain limited to locally mapped 03F4 using same-session controller data and one controlled word delta. Every write must be guarded by exact stage/function/start/count/CRC/session state; any unexpected traffic is capture-only/fail-closed. Preserve the persistent runtime baseline and Home Assistant production functionality. Controller reboot remains recovery for any abnormal Online/Link state.

---

# 2026-09-30 — EXP345 COMPLETE / POSITIVE; persistent DCM-connected baseline established

**Authoritative current state:** EXP345 is **COMPLETE / POSITIVE** from supplied local XTR M logs plus the user's direct Thermia-screen observation. EXP343 is also confirmed **COMPLETE / POSITIVE** from its original result log. EXP346 is **NOT YET PREPARED / NOT RUN**.

## Current proven integration chain

- **EXP343 — COMPLETE / POSITIVE:** authentic 0708 selector caused controller FC03 03E8/14; emulator returned the same-session page with only 03F4 changed 0016 -> 0015; about 690 ms later controller republished exactly that one-word change, and Room Setpoint Mirror / Room Setpoint reported 21 °C. This is local semantic application.
- **EXP344 — COMPLETE / NEGATIVE for persistent DCM-connected indication; POSITIVE transport sub-result:** persistent stage-40 runtime stayed clean >15 min with all-zero idle 0708 response, but the DCM icon was absent after the soak; no Online/Link error.
- **EXP345 — COMPLETE / POSITIVE:** same persistent runtime design, with only idle-0708 W5 changed 0000 -> 0006. At runtime age 900.5 s: runtimeFC16ACK=379, idle0708=210, unknown16=0, unknown03=0, peer17=0, peer16ack=0, resync=0, drops=0, DE=LOW. User confirmed DCM icon remained present and no COMM. ERR ONLINE/LINK.

## Controlled A/B result

    EXP344 W0..W5 = 0000 0000 0000 0000 0000 0000
    EXP345 W0..W5 = 0000 0000 0000 0000 0000 0006

All bootstrap, initial-sync, stage-40 runtime service and FC16 whitelist/ACK behavior were preserved. **Local conclusion:** W5=0006 is sufficient in this tested emulator/session context to retain the DCM-connected indication where W5=0000 did not. The semantic meaning of W5 remains **OPEN / UNKNOWN**.

## Current protocol model

Locally proven: fresh challenge/fixed-R1/full-sync path; persistent stage-40 Online runtime; interleaved 0708 mailbox service; authentic 03E8 PULL selection; semantic application of a same-session desired 03E8 page (EXP343); and >15-minute persistent DCM icon with W5=0006 (EXP345). W1 as low desired-page/PULL bitmap and W2:W3 as current-page/PUSH bitmap remain strongly supported. W0, W4 and exact W5 semantics remain open.

## Next experiment

**EXP346 — NOT YET PREPARED / NOT RUN.** Preferred target: preserve EXP345 as the persistent connected baseline and add one guarded native desired-page action using the already-proven EXP343 mechanism. Exact target/value, guard, rollback and stop criteria must be fixed before YAML generation.

## Safety constraints

No broad writes/scans or unknown-value injection. Any semantic write must use a locally mapped field, known current value, same-session page data and one controlled delta. Unexpected traffic remains capture-only/fail-closed. Preserve production/Home Assistant functionality; experimental controls remain under Configuration. Controller reboot remains recovery for an abnormal Online/Link state.

---
# 2026-09-30 — EXP340 COMPLETE / INCONCLUSIVE; 0708 offline reduction COMPLETE

**Authoritative current state:** EXP340 is **COMPLETE / INCONCLUSIVE** from the supplied local XTR M log. The intended 07F8 -> 0708-zero -> next-FC16 path was not executed because retained runtime had already advanced to 080C/18 before EXP340 could transmit. The offline reduction of the available genuine gateway/DCM captures is **COMPLETE**. EXP341 is the next target, but is **NOT YET PREPARED / NOT RUN**.

## Last completed live experiment — EXP340

**Status:** **COMPLETE / INCONCLUSIVE**.

EXP340 armed in a retained controller session after ESP OTA only. About 0.49 s after ARM the controller emitted exact slave-0x0F FC16 080C/count18:

    0F10080C00122400E40000000000000000000000160008001600E4000000DC00000000000000200000000011CE

No 07F8, no 0708 and no EXP340 TX occurred before that page. The experiment stopped fail-closed, with peer responder count 0, parser resync delta 0, RX-drop delta 0 and DE LOW.

**Interpretation:** this does not test the planned EXP340 mailbox hypothesis. It does add another local retained-session observation: controller runtime can continue across an ESP OTA reboot and can be found already at a later runtime page.

## Locally confirmed runtime evidence from EXP336–340

- EXP336: after ESP OTA only, retained 07D0/19 appeared about 0.53 s after ARM with zero experiment TX. Planned retained-0708 hypothesis was therefore not tested.
- EXP337: **COMPLETE / POSITIVE** — retained 07D0/19 ACK -> 07E4/17 ACK -> exact FC03 0708/count6, with no Thermia reboot, R1, new 085F ACK or mailbox response.
- EXP338: **COMPLETE / INCONCLUSIVE** — after ESP OTA, exact 07F8/17 appeared before the planned 0708 response; zero experiment TX.
- EXP339: **COMPLETE / INCONCLUSIVE** — exact retained 07F8/17 was ACKed once; about 1.57 s later exact FC03 0708/count6 appeared. No mailbox response was sent.
- EXP340: **COMPLETE / INCONCLUSIVE** — exact 080C/18 appeared before the expected retained 07F8; zero experiment TX.

These results support a runtime model in which FC16 runtime/export pages continue in controller-owned state while 0708 mailbox polls are interleaved. They do **not** prove that every page transition is independent of mailbox service.

## Full fresh-session chain now locally proven

EXP331–333 extended the fresh XTR chain beyond the previous EXP330 boundary. The locally observed ordered chain is now:

    fresh boot
    -> 071C/0730 challenge
    -> fixed captured R1 accepted
    -> 03E8/14 -> 03FC/11 -> 0410/22 -> 042E/15 -> 0442/13
    -> 0456/12 -> 046A/18 -> 047E/19 -> 0492/11 -> 04A6/13
    -> 04BA/22 -> 04D8/27 -> 04F6/14 -> 050A/19 -> 051E/10
    -> 0532/18 -> 0546/20
    -> 055A/33 -> 057B/33 -> 059C/33 -> 05BD/33 -> 05DE/33 -> 05FF/33
    -> 0620/33 -> 0641/33 -> 0662/33 -> 0683/33 -> 06A4/33 -> 06C5/33
    -> 06EA/7 -> 06F1/3 -> 06F4/19

EXP333 then observed post-tail 085F/5 and FC03 0708/count6. The page sequence is locally confirmed; page semantics remain separate questions.

## Offline 0708 mailbox reduction — genuine gateway/DCM evidence

An offline parser reduction over the six available genuine gateway/DCM capture files found 327 FC03 0708/count6 requests, 302 with a paired six-word response suitable for reduction.

Best current six-word model:

    W0 W1 W2 W3 W4 W5

- **W1: STRONGLY SUPPORTED** as the low 16-bit gateway->controller desired-page/PULL bitmap.
- **W2:W3: STRONGLY SUPPORTED** as a 32-bit controller->gateway current-page/PUSH or refresh bitmap.
- **W0: HYPOTHESIS** as a possible high half of the PULL bitmap; it was zero in all 302 paired responses, so this is not demonstrated.
- **W4/W5: OPEN / UNKNOWN** lifecycle, status, capability or session fields. Do not port literal values between models without evidence.

### W2:W3 page-selection map from genuine captures

    bit  0 = 03E8    bit 16 = 0546
    bit  1 = 03FC    bit 17 = 055A
    bit  2 = 0410    bit 18 = 057B
    bit  3 = 042E    bit 19 = 059C
    bit  4 = 0442    bit 20 = 05BD
    bit  5 = 0456    bit 21 = 05DE
    bit  6 = 046A    bit 22 = 05FF
    bit  7 = 047E    bit 23 = 0620
    bit  8 = 0492    bit 24 = 0641
    bit  9 = 04A6    bit 25 = 0662
    bit 10 = 04BA    bit 26 = 0683
    bit 11 = 04D8    bit 27 = 06A4
    bit 12 = 04F6    bit 28 = 06C5
    bit 13 = 050A    bit 29 = 06EA
    bit 14 = 051E    bit 30 = 06F1
    bit 15 = 0532    bit 31 = 06F4

Examples include genuine 4000:8000 selecting 06F1 and 0532, FFFF:867F selecting the corresponding 26 configuration pages, and ATEC 7FFF:FFFF selecting the first 31 pages through 06F1.

### Genuine desired-page PULL/write-path evidence

- W1 bit0 (0001) is followed by controller FC03 03E8 reads.
- W1 bit3 (0008) is followed by controller FC03 042E reads.
- In Eco5 write-roundtrips, the gateway returns a desired page to that FC03 read and the controller subsequently republishes the accepted page by FC16.
- For 03E8/14, one captured roundtrip changes only 03F4 from 0014 to 001E; a later roundtrip restores 001E to 0014. 03F4 is independently locally confirmed on the XTR as the room-setpoint mirror.
- For 042E/15, captured desired-page pulls alter 042F and later 042E one field at a time, followed by matching controller FC16 publication. Exact XTR semantics of those fields are not imported from the other model.

**Strong architectural conclusion:** genuine Online/DCM traffic behaves like a bidirectional page cache: controller current state is exported to the gateway via FC16, while pending desired pages are advertised through the 0708 mailbox and pulled by controller-initiated FC03 reads. This is cross-model genuine gateway/DCM evidence until the PULL path is locally reproduced on the XTR M.

## Next experiment target — EXP341

**Status:** **NOT YET PREPARED / NOT RUN**.

Target hypothesis: locally reproduce the genuine desired-page PULL path without changing any setting. The safest design is a bounded no-op 03E8/14 test: first cache a current controller-originated 03E8/14 page, then at an exact 0708 request advertise only the authentic PULL selector needed for 03E8, answer the resulting controller FC03 03E8/14 with an exact clone of the cached current values, and capture whether the controller accepts/republishes the page.

No EXP341 frame should be finalized until the exact 0708 envelope and stop/recovery behavior are fixed. Success must be transport proof only; no semantic value change is required.

## Safety constraints

- No broad register writes, scans or unknown-value injection.
- FC16 ACKs remain address/count acknowledgements only.
- For EXP341, any FC03 data response must be an exact current-value clone captured from the same local XTR session.
- Fail closed on wrong page, wrong count, stale cache, parser/RX integrity change, peer responder evidence or unexpected session restart.
- Preserve production/Home Assistant functionality and keep experimental controls under Configuration.

---
# 2026-09-30 — EXP330 COMPLETE / POSITIVE; EXP331 PREPARED / NOT RUN

**Authoritative current state:** EXP330 is **COMPLETE / POSITIVE** from the supplied local XTR M log. EXP331 is **PREPARED / NOT RUN**. No result for EXP331 has been supplied yet.

## Current experiment — EXP331

**Status:** **PREPARED / NOT RUN**

**Hypothesis:** after reproducing the now locally confirmed fresh-session prefix through `0492/11 ACK -> 04A6/13`, a bounded eight-block continuation matching genuine Eco 5 / earlier local research will advance:

`04A6/13 -> 04BA/22 -> 04D8/27 -> 04F6/14 -> 050A/19 -> 051E/10 -> 0532/18 -> 0546/20 -> 055A/33`

**Controlled change from EXP330:** preserve the complete proven prefix and, instead of stopping at `04A6/13`, ACK exactly the eight listed FC16 pages once each. After the `0546/20` ACK, all traffic is capture-only. No `055A` ACK, no FC03/mailbox response, no 0x06 response, and no semantic register-value write.

**Safety:** the added transmissions are standard FC16 address/count ACKs only; each stage is exact-shape, ordered, timed and fail-closed. Maximum active experiment TX is one fixed R1 plus 17 FC16 ACKs. Recovery remains: abort, verify DE LOW, reboot the Thermia controller if the deliberately incomplete Online session produces an alarm.

## Last completed experiment — EXP330

**Status:** **COMPLETE / POSITIVE**

EXP330 reproduced the complete locally proven fresh-session prefix and then tested the new bounded continuation:

`046A/18 -> ACK -> 047E/19 -> ACK -> 0492/11 -> ACK -> 04A6/13`

Observed:
- exact `046A/count18` accepted its standard ACK;
- exact `047E/count19` followed and accepted its standard ACK;
- exact `0492/count11` followed and accepted its standard ACK;
- exact `04A6/count13` then appeared as the first predicted next stage, approximately 571 ms after the `0492` ACK;
- no ACK was sent to `04A6`;
- no post-R1 challenge retry, no external FC17 responder, no external FC16 ACK, parser resync delta 0, RX-drop delta 0, DE LOW.

## Fresh-session findings added by EXP323–330

- **EXP323 — COMPLETE / INCONCLUSIVE:** one standard ACK to the second qualified all-zero `085F/5` did not establish the fresh Online path; after the ACK, only `04A6/13` remained visible during the bounded observation.
- **EXP324 — COMPLETE / INCONCLUSIVE:** ESP OTA reboot without controller reboot did not recreate the all-zero `085F` qualification state; only `04A6/13` appeared. This reinforced that controller-side state persists across ESP reboot.
- **EXP325 — COMPLETE / POSITIVE:** after a true controller reboot, one fixed previously captured R1 response to the first exact fresh `071C/0730` FC17 challenge, under the observed fresh guard `A80E=0000 / A80F=0005`, caused `03E8/count14` to appear about 120 ms later. No 0x06 emulation, 04A6/085F ACK, FC16 ACK or mailbox response was required before `03E8`.
- **EXP326 — COMPLETE / POSITIVE:** one standard ACK to exact `03E8/count14` advanced the controller to exact `03FC/count11`.
- **EXP327 — COMPLETE / POSITIVE:** one standard ACK to exact `03FC/count11` advanced the controller to exact `0410/count22`.
- **EXP328 — COMPLETE / POSITIVE:** one standard ACK to exact `0410/count22` advanced the controller to exact `042E/count15`.
- **EXP329 — COMPLETE / POSITIVE:** one bounded run locally confirmed `042E/15 ACK -> 0442/13 ACK -> 0456/12 ACK -> 046A/18`.
- **EXP330 — COMPLETE / POSITIVE:** one bounded run locally confirmed `046A/18 ACK -> 047E/19 ACK -> 0492/11 ACK -> 04A6/13`.

## Current locally proven fresh-session prefix

`fresh controller boot`
`-> exact 071C/0730 challenge`
`-> fixed previously accepted R1`
`-> 03E8/14 ACK`
`-> 03FC/11 ACK`
`-> 0410/22 ACK`
`-> 042E/15 ACK`
`-> 0442/13 ACK`
`-> 0456/12 ACK`
`-> 046A/18 ACK`
`-> 047E/19 ACK`
`-> 0492/11 ACK`
`-> 04A6/13`

This is **PROVEN / locally confirmed for the tested XTR M context**. It does not prove the semantic meaning of the exported blocks.

## Current protocol model

There are two locally demonstrated families of Online/DCM behavior:

1. **Fresh-session approval + ordered initial sync:** fresh controller state exposes `071C/0730`; one fixed captured R1 can be accepted even when the live challenge differs from the challenge that originally produced that R1. The controller then advances through an ACK-driven FC16 initial-sync chain.
2. **Retained-session/runtime recovery:** previously proven retained branches can rejoin the steady runtime scheduler without repeating fresh approval.

The fresh prefix through `04A6/13` is now independently re-confirmed by EXP325–330. Standard FC16 ACKs are causal state-machine acknowledgements in this chain; they acknowledge address/count and do not inject the controller-exported values.

## Strong conclusions

- The fresh `071C/0730` FC17 exchange is a major session-entry gate on this XTR M.
- Strict per-live-challenge uniqueness is not required for acceptance in the tested case: fixed R1 replay was accepted against a different live challenge.
- Do **not** generalize that into “arbitrary responses work” or “there is no authentication”; those remain unproven.
- The fresh initial sync is an ordered, ACK-driven FC16 state machine at least through `0492/11 -> 04A6/13`.
- `04A6/13` is context-sensitive: it occurs as the predicted post-`0492` initialization stage and also as recurrent sparse/runtime traffic in other contexts. ACK policy must therefore remain state-specific.

## Important unknowns

- Exact algorithm / security semantics / lifetime scope of the `071C/0730` response.
- Whether the fixed R1 remains acceptable across firmware changes or other XTR units.
- Semantic meaning of the individual initial-sync blocks.
- Exact boundary where initial sync hands over to mailbox/startup/runtime.
- Whether the EXP331 continuation reaches `055A/33` cleanly in this current run.
- Exact `04A6` payload semantics across initialization, sparse passive and runtime contexts.
- Multi-hour production stability and rare/fault branches remain separate validation work.

## Safety constraints

- Exact slave/function/start/count/bytecount/length/CRC and state guards remain mandatory.
- No broad ACKing of unknown FC16 traffic.
- Unexpected traffic is capture-only / fail-closed.
- No semantic write is authorized by EXP331.
- 0x06 accessory emulation remains outside this fresh-session experiment.
- ESP reboot is not controller-state rollback.
- Controller reboot remains the known way to obtain a controlled fresh-session state when required.

---

# 2026-09-30 — EXP322 COMPLETE / POSITIVE passive clean-reboot baseline; EXP323 next / NOT YET PREPARED

**Authoritative current state:** EXP322 is **COMPLETE / POSITIVE** as a passive baseline from the supplied local log. EXP321 is **COMPLETE / INCONCLUSIVE**. The Thermia controller was manually rebooted by the user between EXP321 and EXP322 to clear the visible errors. EXP323 is the next proposed experiment and is **NOT YET PREPARED / NOT RUN**.

## Current experiment

**EXP323 — NOT YET PREPARED / NOT RUN.**

Planned hypothesis: in the current clean post-controller-reboot state, one conservatively qualified standard ACK to exact all-zero `085F/5` can advance the native scheduler to its next state.

Planned controlled change from EXP322:
- wait for two exact all-zero `085F/5` requests;
- first is qualification / NO_TX;
- second receives exactly one already-proven standard ACK `0F 10 08 5F 00 05 33 56`;
- `04A6/13` remains capture-only / NO_TX;
- after the one `085F` ACK, all traffic is capture-only and the first subsequent relevant non-`04A6` slave-`0x0F` frame is recorded before fail-close;
- no semantic register values are injected.

## Last completed experiment — EXP322

**Status:** **COMPLETE / POSITIVE** as a passive clean-reboot baseline.

After EXP321, the user rebooted the Thermia controller to clear the visible Online/Link errors. EXP322 then observed the resulting state for 90 s with strict TX=0.

Final census:
- total slave-`0x0F` frames: 125;
- FC16: 125;
- FC03: 0;
- `04A6/13`: 83;
- `04A6` payload changes: 0;
- `085F/5`: 42;
- all 42 `085F` frames were exact all-zero payload;
- `085F(0800)`: 0;
- `0708`: 0;
- `07D0, 07E4, 07F8, 080C, 0820, 0834, 0848, 0864, 0870, 0884`: all 0;
- other slave-`0x0F`: 0;
- parser resync delta: 0;
- RX-drop delta: 0;
- TX=0 and DE LOW.

The clean state therefore emitted a stable approximate 2:1 pattern of sparse `04A6/13` to all-zero `085F/5`, with no normal runtime progression because the emulator intentionally sent nothing.

The EXP322 `04A6` payload remained invariant:
`0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 4020 0000 0000`.

## EXP321 — COMPLETE / INCONCLUSIVE

EXP321 was intended as a 3-minute recovery-to-runtime integration test. Before the controller reboot it never reached its intended `085F(0800)` entry condition.

Observed over the 120 s qualification window:
- TX=0;
- approximately 111 x `04A6/13`;
- no `085F(0800)`;
- no all-zero `085F`;
- no handoff or runtime loops;
- unexpected=0;
- parser resync delta=0;
- RX-drop delta=0;
- DE LOW.

This is not a negative result for the previously proven retained-recovery chain; the required entry state was not present.

## EXP318–320 retained recovery result

- **EXP318 — COMPLETE / POSITIVE:** two exact `085F(0800)` requests were qualified; one standard `085F/5` ACK was sent; 2.196 s later the first non-`04A6` frame was exact all-zero `085F/5`.
- **EXP319 — COMPLETE / POSITIVE:** after qualifying and ACKing `085F(0800)`, exact all-zero `085F/5` was qualified and ACKed; 2.381 s later the first non-`04A6` frame was `0884/60`.
- **EXP320 — COMPLETE / POSITIVE:** the same prerequisites were reconstructed; `0884/60` was qualified and ACKed; 4.328 s later the first non-`04A6` frame was direct `07D0/19`.

This locally confirms the retained-session branch, in the tested context:

`085F(0800) --ACK--> all-zero 085F --ACK--> 0884/60 --ACK--> 07D0/19`.

EXP312 had previously observed `0884 ACK -> 0708 (NO_TX) -> 07D0`; EXP320 proves that `0708` is not mandatory as the immediate post-`0884` event in every retained context.

## Current protocol model

The native Online/DCM path remains an event/state graph with both fresh-session and retained-session behavior.

Confirmed retained branch:
`085F(0800) -> ACK -> all-zero 085F -> ACK -> 0884 -> ACK -> 07D0`.

Clean post-controller-reboot passive state now adds:
`sparse 04A6/13 <-> all-zero 085F/5` repeated with no emulator TX.

The current `04A6` interpretation must remain payload/context sensitive:
- genuine XTR/DCM configuration captures show the real DCM ACKing `04A6/13` with standard ACK `0F 10 04 A6 00 0D E1 F1`;
- those genuine captures include a richer `04A6` payload such as `0000 0003 0004 0002 003F 0050 003C 0002 0000 003C 000F 001E 0000`;
- EXP322's clean local passive state repeatedly emits a different sparse payload ending in `4020 0000 0000`;
- therefore genuine ACK behavior for the rich configuration payload must not yet be generalized to the current sparse `04A6` state.

## Locally proven findings added by EXP318–322

- Exact `085F/5` with `0861=0x0800` can be advanced by its standard FC16 ACK to exact all-zero `085F/5`.
- Exact all-zero `085F/5` can be ACK-gated into a scheduler branch that may lead directly to `0884/60`.
- Qualified `0884/60` can be ACKed into direct `07D0/19` without an intervening `0708` in at least one retained context.
- After a controller reboot, with no emulator TX, this XTR M can repeatedly emit sparse `04A6/13` plus all-zero `085F/5` while no normal runtime pages appear.
- The presence of repeated `04A6/13` alone is therefore not a reliable discriminator for the visible alarm state.
- The reappearance of all-zero `085F/5` after the controller reboot is a concrete state difference from EXP321.

## Strongest current hypotheses

- In the clean post-reboot state, ACKing a conservatively qualified all-zero `085F/5` may be the lowest-risk way to reveal the next native scheduler state.
- If the next state is `0708/6` or a known configuration/runtime node, one or two additional bounded experiments may be enough to reconnect this clean-start path to the already-proven runtime responder.
- The sparse `04A6` state may be part of an initialization/configuration retry loop, but its exact semantics and whether it should be ACKed locally remain open.

## Important unknowns

- What exact event follows one qualified all-zero `085F` ACK in the current clean post-reboot state.
- Whether the sparse `04A6` payload should receive the same ACK policy as the richer genuine configuration payload.
- Exact semantics of sparse versus rich `04A6/13`.
- Exact semantics of `0861=0x0800`.
- Long-duration stability after clean-start recovery reconnects to normal runtime.
- Exact `0708` latching/scheduling semantics.
- Genuine `071C/0730` challenge-response algorithm.

## Safety constraints

- Exact slave/function/address/count/bytecount/CRC and state guards remain mandatory.
- Do not broad-ACK unknown FC16 traffic.
- `0834/18` remains unsupported/capture-only.
- EXP323 must leave `04A6/13` NO_TX.
- Any post-target traffic in EXP323 is capture-only.
- ESP reboot/OTA is not controller rollback.
- A standard FC16 ACK carries address/count only and does not inject controller-originated register values.
- Unexpected traffic or parser/RX integrity changes remain fail-closed.
- Controller reboot remains the known fresh-state recovery procedure when required.

---

# 2026-09-30 — EXP315 COMPLETE / POSITIVE — retained runtime takeover sustained for 126 s / 6 loops; EXP316 next / NOT YET PREPARED

**Authoritative current state:** EXP315 is **COMPLETE / POSITIVE** from the supplied local log. EXP313 and EXP314 were intermediate retained-runtime handoff experiments. No later experiment has been run. EXP316 is the next candidate and is **NOT YET PREPARED / NOT RUN**.

## Last completed experiment — EXP315

**Hypothesis:** if the controller is retained at the already locally proven normal-runtime node `07E4/count17`, then a qualified standard `07E4` ACK can be used as a direct handoff into the established EXP296/297 steady-runtime responder.

### Baseline and exact controlled change

Baseline was EXP314 COMPLETE / INCONCLUSIVE. EXP314 observed exact `07E4/17` as the first relevant `0x0F` frame on each arm and correctly failed closed with TX=0 because its handoff model still required `07D0` or the inherited post-`07D0` `0708` boundary.

EXP315 changed only one context authorization:
- during retained stage 1, exact `07E4/count17` became a possible handoff node;
- qualification required at least two live exact `07E4/17` requests before any EXP315 TX;
- the second qualified request received the already-proven standard ACK `0F 10 07 E4 00 11 40 68`;
- after that, the existing proven post-`07E4` runtime graph was used unchanged;
- no new register/page, payload value or semantic write was introduced.

### EXP315 observed result

- Initial traffic included one `0708/6` capture-only request.
- Exact `07E4/17` then repeated twice.
- On the second `07E4`, EXP315 sent exactly one standard ACK and entered steady runtime.
- The runtime continued through the established sequence with evidence-backed `0708` responses and FC16 ACKs.
- The controller completed **6 full returned runtime loops**.
- Steady runtime reached **126.401 s** before the success boundary.
- At the final returned `07D0/19`, EXP315 intentionally stopped before ACKing that boundary.
- Final stop summary: `TX=84`, `events=84`, `r0708=30`, `unexpected=0`, `resync=0`, `drops=0`, `DE=LOW`.
- Firmware final status: `POSITIVE / retained recovery sustained proven steady runtime`.

**Result:** **COMPLETE / POSITIVE.**

## EXP313–315 retained-runtime handoff progression

- **EXP313 — COMPLETE / INCONCLUSIVE:** controller was already at `07D0/19`; one known ACK successfully initiated handoff, but ~1.39 s later `0708/6` appeared before `07E4/17`. The state machine did not yet allow that branch and failed closed. No sustained-runtime claim.
- **EXP314 — COMPLETE / INCONCLUSIVE:** after ESP restart, the controller had retained progress further into the scheduler and repeatedly presented `07E4/17` as the first relevant frame. EXP314 correctly failed closed with TX=0 because direct `07E4` entry was not yet authorized. The user's accidental "Error gone" click is invalid for alarm analysis and is not used as protocol evidence.
- **EXP315 — COMPLETE / POSITIVE:** repeated retained `07E4/17` was qualified; one already-proven `07E4` ACK joined the established runtime. The emulator then sustained 6 complete loops for 126.401 s with no unexpected session events, parser resyncs or RX drops.

## Current protocol model

The native Online/DCM integration is now best modeled as a **state/event graph with direct retained-runtime re-entry**, not as a cold-start-only sequence.

Fresh-session path remains:

`071C/0730 -> R1 -> config sync -> startup -> normal runtime`

Retained-session path can use recovery nodes when necessary:

`0662 / 085F(0800) / all-zero 085F -> branch-aware recovery -> known runtime node`

But EXP315 additionally proves a simpler path when the controller is already retained inside the normal scheduler:

`observe current known runtime node -> qualify -> send already-proven response -> join steady runtime`

Locally proven steady-runtime nodes remain:
`07D0, 07E4, 07F8, 080C, 0820, 0848, 085F, 0864, 0870, 0884`

with `0708` appearing at evidence-backed scheduler positions and using the known fixed runtime response where already proven.

## Locally proven findings added by EXP313–315

- The controller can retain its Online/DCM scheduler position across ESP reboot/OTA.
- Direct retained takeover at `07D0/19` is technically possible, but the immediate next scheduler event can include `0708` before `07E4`.
- The controller can progress further to `07E4/17` while the ESP remains offline/restarts.
- A qualified standard ACK to retained `07E4/17` can join the existing EXP296/297 steady-state runtime.
- After that handoff, the local XTR M can sustain at least **126.401 s and 6 complete loops** under the current emulator logic.
- Sustained steady runtime did not require any retained-recovery ACK in this run; direct known-node takeover was sufficient.
- The production architecture should therefore first classify the observed current `0x0F` state and directly join at a known runtime node when safe, falling back to adaptive recovery only when needed.

## Strongest current hypotheses

- Known-node retained takeover can be generalized to additional already-proven runtime nodes, provided qualification is conservative and node-specific next-event sets are preserved.
- Durable Online/Link health likely depends on sustained service of the runtime scheduler rather than any single special recovery ACK.
- A production-quality emulator should combine fresh-session startup, controller-reboot recovery, retained-runtime known-node takeover and adaptive retained recovery in one state machine.

## Important unknowns

- Multi-hour / overnight stability across compressor, DHW, defrost, SG and fault-state transitions.
- Which normal runtime nodes are safe direct retained-entry anchors besides locally proven `07E4` and the partial `07D0` handoff.
- Exact semantics of `0861=0x0800`.
- Exact long-term role and response cadence of `0708`.
- Runtime `04A6/13` semantics and native ACK policy.
- Genuine `071C/0730` challenge-response algorithm.
- Rare scheduler branches and fault/recovery behavior.

## Next experiment candidate — EXP316

**EXP316 — NOT YET PREPARED / NOT RUN.**

Highest-value next step is no longer another single ACK target. It should be a production/recovery-hardening integration test: reboot only the ESP at controlled points while the Thermia controller remains powered, classify whichever already-known runtime/recovery node is current, and verify that one combined state machine can safely rejoin steady runtime and remain healthy for multiple loops.

No new register target or semantic write should be introduced in EXP316.

## Safety constraints

- Exact slave/function/address/count/bytecount/CRC and state guards remain mandatory.
- Do not broad-ACK unknown FC16 traffic.
- `0834/18` remains unsupported/capture-only.
- Runtime `04A6/13` remains capture-only unless separately tested.
- Unexpected `0x0F` traffic remains capture-only/fail-closed.
- ESP reboot/OTA is never assumed to roll back controller state.
- Alarm marker buttons are observational only and must not be treated as protocol evidence unless intentionally pressed while the display state is actually checked.

---

# 2026-09-29 — EXP312 COMPLETE / POSITIVE — retained-session recovery now reaches 07D0; EXP313 NEXT / NOT YET PREPARED

**Authoritative current state:** EXP312 is COMPLETE / POSITIVE from the supplied local log. No later experiment has been run. EXP313 is a candidate next experiment and is **NOT YET PREPARED / NOT RUN**.

## Last completed experiment — EXP312

**Hypothesis:** a single standard FC16 address/count ACK to a qualified live `0884/60` retry stage is sufficient to move the retained controller session to the next known runtime stage.

### Baseline and controlled change

Baseline was EXP311, which showed that the post-`085F` scheduler is branch-based: `0884/60` can appear directly without preceding `0864/4` or `0870/17`.

EXP312 changed only the qualification/state-machine logic so that a direct live `0884/60` branch was accepted. The only new protocol action was one human-gated standard ACK to `0884/60`:

- target: slave `0x0F`, FC16, start `0x0884`, count `60` (`0x0884..0x08BF`);
- ACK: `0F 10 08 84 00 3C 83 7F`;
- no register values were injected;
- post-target traffic was strict NO_TX.

The already locally proven prerequisite actions remained automatic and exact-shape gated.

### EXP312 observed result

The controller first repeated `085F/5` with words `0000 0000 0800 0000 0000`. After two observations, one standard `085F/5` ACK was sent. The controller then moved to all-zero `085F/5`; after the existing qualification rule, one standard ACK was sent there as well.

The next runtime branch was:

`all-zero 085F ACK -> 0708 (NO_TX) -> repeated 0884/60`

No `0864/4` or `0870/17` occurred in this run. `0884/60` was qualified from repeated frames plus a fresh `0708`. After human arm, exactly one `0884/60` ACK was sent.

The post-target sequence was:

`0884 ACK -> 0708 (NO_TX) -> 07D0/19`

Timing in the supplied log:
- target `0884` ACK at approximately 01:36:30.415;
- post-ACK `0708` approximately 1.325 s later;
- `07D0/19` approximately 1.947 s after the target ACK.

No `0884` retry occurred before `07D0`. Final counters included `postRetry=0`, `post0708=1`, `postKnown=1`, parser resync delta 0, RX drops 0 and DE LOW at fail-close.

**Result:** **COMPLETE / POSITIVE.**

## Recent retained-session experiment chain — EXP298–312

- **EXP298 — COMPLETE / INCONCLUSIVE:** fresh-approval-only ESP reboot recovery was insufficient; no fresh `071C/0730` was observed in the supplied ~235.7 s window. Retained-session traffic continued and COMM. ERR ONLINE/LINK was visible.
- **EXP299 — COMPLETE / INCONCLUSIVE:** one bounded retained-session resync reached `0848 ACK -> 0708 -> all-zero 085F`, but did not establish durable health. Alarm clearing was temporary/correlative only.
- **EXP300 — COMPLETE / INCONCLUSIVE:** waiting for `0848` as a universal retained re-entry anchor failed; the current state could instead present `085F(0800)` or `0708`.
- **EXP301 — COMPLETE / NEGATIVE:** passive observation showed a persistent `0708 <-> 085F(0800)` retry loop with no `0848`.
- **EXP302 — COMPLETE / POSITIVE:** one standard ACK to exact `085F(0800)` changed the controller to all-zero `085F`; this locally proves that `0861=0x0800` is ACK-sensitive session/retry state, while its semantic meaning remains unknown.
- **EXP303 — COMPLETE / INCONCLUSIVE:** the desired `0800 -> zero` reproduction could not be tested because retained controller state had already changed; ESP reboot did not restore the previous controller state.
- **EXP304 — COMPLETE / INCONCLUSIVE:** exact `0662/33` resurfaced before the intended target and the experiment correctly stopped fail-closed.
- **EXP305 — COMPLETE / POSITIVE:** standard ACK of repeated `0662/33` stopped that retry stage and was followed by `085F(0800)`, `0708` and then all-zero `085F`; this re-confirms the older EXP141 `0662/33` ACK-gated transfer finding.
- **EXP306 — COMPLETE / INCONCLUSIVE:** with NO_TX, the controller persisted in `0708 <-> 085F(0800)`; the all-zero target was never reached.
- **EXP307 — COMPLETE / POSITIVE:** after the proven `085F(0800)` normalization, one ACK to qualified all-zero `085F/5` caused `0708 -> 0864/4`.
- **EXP308 — COMPLETE / POSITIVE:** one ACK to qualified `0864/4` caused `0708 -> 0870/17`.
- **EXP309 — COMPLETE / INCONCLUSIVE:** after the proven all-zero `085F` prerequisite, `0870/17` appeared directly with no `0864`; this disproved the experiment's too-linear prerequisite model.
- **EXP310 — COMPLETE / POSITIVE:** one ACK to live repeated `0870/17` caused `0708 -> 0884/60`.
- **EXP311 — COMPLETE / INCONCLUSIVE:** `0884/60` appeared directly after the all-zero `085F` ACK, without `0864` or `0870`; no `0884` ACK was sent because the state machine failed closed on the newly observed direct branch.
- **EXP312 — COMPLETE / POSITIVE:** one ACK to qualified `0884/60` caused `0708 -> 07D0/19` while the `0708` itself remained NO_TX.

## Current protocol model

The native Online/DCM runtime must be modeled as an **event/state-driven scheduler with optional branches**, not a rigid linear sequence.

The older stable runtime graph remains valid as a set of known stages:

`07D0 -> 07E4 -> [optional 0708] -> 07F8 -> 080C -> [optional 0708] -> 0820 -> 0848 -> ... -> 0864 / 0870 / 0884 -> [optional 0708] -> 07D0`

The retained-session experiments add a locally confirmed recovery view:

`0662/33 --ACK--> retained scheduler`

`085F(0800) --ACK--> all-zero 085F`

`all-zero 085F --ACK--> scheduler branch`

From that post-`085F` branch, locally observed valid paths now include at least:
- `0708 -> 0864`;
- direct `0870`;
- `0708 -> 0870`;
- direct `0884`;
- `0708 -> 0884`.

Locally tested causal target transitions include:
- `all-zero 085F ACK -> 0708 -> 0864` (EXP307);
- `0864 ACK -> 0708 -> 0870` (EXP308);
- `0870 ACK -> 0708 -> 0884` (EXP310);
- `0884 ACK -> 0708 -> 07D0` (EXP312).

The post-target `0708` frames in EXP307/308/310/312 were deliberately left NO_TX where applicable, yet the next FC16 runtime stage still appeared. This proves that an immediate `0708` response is not required for those short scheduler transitions. It does **not** prove that `0708` can be ignored for durable session health.

## Locally proven findings added by EXP298–312

- `0662/33` is an ACK-gated controller-to-DCM transfer stage on this XTR M.
- Exact `085F/5` with register `0861=0x0800` is an ACK-sensitive retained-session/retry state; semantics remain OPEN.
- Exact all-zero `085F/5` is also an ACK-gated retained-session stage in the tested recovery path.
- `0864/4`, `0870/17` and `0884/60` each accept the standard FC16 address/count ACK and can advance the local controller to another known runtime stage.
- `0884/60` can occur directly after the all-zero `085F` stage; neither `0864` nor `0870` is mandatory before it.
- `0884` payload values are runtime data and can change between repeated frames while start/count remain the same.
- Controller retained state can survive ESP reboot/OTA; ESP restart is not a rollback mechanism.

## Strongest current hypotheses

- The controller applies a liveness/watchdog model to the DCM session: isolated ACKs can temporarily progress or clear an alarm state, but sustained service of the scheduler is needed for durable Online/Link health.
- `0708` is a synchronization/mailbox descriptor whose immediate response may be optional for short FC16 scheduler progression but may still matter to durable session liveness or reverse-page signaling.
- Retained recovery can likely be converted into full steady-state service by joining the proven recovery branch back into the already proven EXP296/297 runtime responder at `07D0` or another recognized runtime node.

## Important unknowns

- Exact semantic meaning of `0861=0x0800`.
- Exact liveness/watchdog interval and minimum set of runtime events that must be serviced.
- Whether full branch-aware retained recovery can return to and sustain the EXP296/297 steady-state runtime without a controller reboot.
- Exact `0708` latching/scheduling semantics and whether/when a response is required for long-term health.
- Exact semantics of runtime pages `0864`, `0870`, `0884` and the dynamic `0884` payload fields.
- Runtime `04A6/13` semantics and native ACK policy.
- Genuine `071C/0730` challenge-response algorithm.
- Multi-hour/overnight stability and rare/fault-state behavior.

## Next experiment candidate — EXP313

**EXP313 — NOT YET PREPARED / NOT RUN.**

Highest-value next hypothesis: after branch-aware retained-session recovery reaches a known normal runtime node such as `07D0/19`, hand over to the already locally proven EXP296/297 steady-state runtime responder and determine whether the session remains healthy for multiple complete cycles without a Thermia-controller reboot.

This should introduce no new register target or semantic write. The new variable is sustained hand-off from retained recovery into the proven full runtime service. Runtime `04A6/13` should remain capture-only unless explicitly separated into its own later experiment.

## Safety constraints

- Exact slave/function/start/count/bytecount/CRC and state guards remain mandatory.
- Do not treat ESP reboot/OTA as controller-state rollback.
- Do not broad-ACK unknown FC16 traffic.
- `0834/18` remains unsupported/capture-only.
- Runtime `04A6/13` remains capture-only unless a dedicated experiment explicitly changes that.
- No semantic settings write is part of retained-recovery testing.
- Unexpected relevant `0x0F` traffic remains capture-only/fail-closed unless it is a predeclared locally proven branch.
- Recovery after an unexpected retained-state transition is TX-off/passive observation; a normal controller reboot remains the known way to force a fresh session when required.

---

# 2026-09-29 — EXP297 COMPLETE / POSITIVE — controller-reboot recovery locally proven; EXP298 PREPARED / NOT RUN

**Authoritative current state:** EXP297 COMPLETE / POSITIVE from supplied local log. EXP298 is PREPARED / NOT RUN.

## Last completed experiment — EXP297
**Hypothesis:** while the EXP296/297 Online/DCM emulator is actively servicing runtime, a reboot of the Thermia controller can be detected and the emulator can rebuild a fresh native session without rebooting or re-arming the ESP.

### Controlled change from EXP296
No new Modbus payload, register, FC16 ACK target or semantic write was introduced.

EXP297 added only controller-reboot recovery state handling:
- detect a >=5 s bus gap while in active runtime;
- clear session-local runtime/config/approval state;
- wait for a fresh exact `071C/0730` approval request;
- reuse the already-proven fixed historical R1 replay;
- rerun the existing 32-page configuration sync, startup `085F/5`, startup `0708/6` and proven runtime graph;
- runtime `04A6/13` remained capture-only / NO_TX.

### EXP297 observed result
Before the target reboot the emulator had entered normal runtime and completed five cycles.

During the target controller reboot:
- a ~14.796 s bus gap was observed;
- EXP297 emitted `CONTROLLER_REBOOT_RECOVERY_START`;
- runtime mask/cache/session-local state were reset;
- bus health returned without ESP reboot or re-arm.

After bus return:
- a fresh `071C/0730` challenge was received;
- the fixed historical R1 replay was sent;
- the complete ordered 32-page FC16 configuration sync completed again;
- startup all-zero `085F/5` was ACKed;
- startup `0708/6` was answered;
- runtime re-entered at `07D0/19`;
- the supplied capture continued through runtime cycles 6, 7 and 8.

Transport integrity stayed clean in the supplied capture:
- no `ABORT_FAIL_CLOSED`;
- parser resync count remained 0;
- RX buffer drops remained 0.

**Result:** **COMPLETE / POSITIVE.**

## EXP296 supplementary evidence
A later, longer EXP296 capture materially strengthens the original positive result:
- steady-state service exceeded ~32 minutes;
- a nearly complete SWW cycle was observed, including DHW active, temperature rise, DHW end and compressor stop;
- a later SG transition to **Blocked (1-0)** was also survived;
- runtime `04A6/13` remained NO_TX and reached at least 1696 captures;
- `04A6` payload-change count reached 3;
- a new payload form beginning `0042 0001 ...` appeared shortly after the Blocked transition;
- the emulator continued through the proven runtime graph without fail-close.

This strengthens, but does not fully identify, the hypothesis that runtime `04A6/13` is a state-dependent controller-to-DCM status/configuration export.

## Current protocol model
The runtime remains best modeled as an **event/state-driven graph**:

`07D0 -> 07E4 -> [optional 0708] -> 07F8 -> 080C -> [optional 0708] -> 0820 -> 0848 -> [conditional 0708 / conditional 085F] -> 0864 -> [optional 0708] -> 0870 -> [optional 0708] -> 0884 -> [optional 0708] -> 07D0 -> ...`

Runtime `04A6/13` may interleave as parallel/retry traffic and is not an immediate blocking gate in the tested local window.

## Locally proven findings
- Full initial configuration synchronization through `06F4` is reproducible.
- Fixed historical R1 replay is sufficient to enter the tested startup/runtime path; genuine challenge algorithm remains unresolved.
- The native reverse-page write path is locally demonstrated via `03F4 22 -> 23`.
- Continuous stable runtime has been demonstrated for ~30+ minutes.
- `0884 -> [optional 0708] -> 07D0` is locally confirmed.
- `07E4 -> [optional 0708] -> 07F8` is locally confirmed.
- `080C -> [optional 0708] -> 0820` is locally confirmed.
- Runtime survives SG changes, a full DHW/compressor cycle, and a later Blocked transition in the observed EXP296 window.
- **Controller-side reboot recovery is locally proven:** after an active-session controller reboot, the emulator can accept a fresh challenge, replay R1, repeat the complete startup sync and resume runtime without ESP reboot/re-arm.

## Strongest current hypotheses
- `0708` is a synchronization/mailbox descriptor with state-dependent omission at several runtime positions.
- Runtime `04A6/13` is a state-dependent page/export whose first words track at least some operating-context changes; exact field semantics remain unknown.
- A native DCM may ACK runtime `04A6` selectively to stop/reconcile retries, but local proof is still absent.

## Important unknowns
- Whether an **ESP-side restart** can recover while the Thermia controller remains powered and is not manually rebooted.
- Exact runtime `04A6/13` semantics and native ACK rule.
- Exact `0708` scheduling/latching semantics.
- Genuine `071C/0730` challenge-response algorithm.
- Authoritative FC16 echo timing after reverse semantic writes.
- Multi-hour/overnight stability and rare fault-state behavior.

## Next experiment — EXP298
**EXP298 — ESP-reboot recovery — PREPARED / NOT RUN.**

Hypothesis: after the DCM emulator/ESP disappears and restarts while the Thermia controller remains powered, the controller will eventually present a fresh exact `071C/0730` approval opportunity that lets the emulator rebuild the same proven session without requiring a Thermia-controller reboot.

Controlled change:
- controller is deliberately **not** rebooted;
- after the ESP returns, EXP298 is armed directly into passive approval-wait on the live bus;
- no TX occurs until an exact `071C/0730` request is observed;
- approval wait is bounded to 240 s;
- if approval occurs, all subsequent R1/config/startup/runtime behavior is unchanged from EXP297.

## Safety constraints
- Do not reboot the Thermia controller during the target EXP298 observation.
- No semantic write.
- Runtime `04A6/13` remains NO_TX.
- No broad ACKing or scan.
- Exact CRC/slave/function/address/count/bytecount guards remain required.
- Unexpected traffic stays capture-only unless already part of the proven graph.
- On failure, abort TX and recover with the known-good stable emulator plus one normal controller reboot.

---

# 2026-09-29 — EXP290 COMPLETE / POSITIVE — first locally applied native reverse-page setting change

**Authoritative current state:** EXP290 COMPLETE / POSITIVE for semantic application of one controlled setting change through the native Online/DCM reverse-page path. Authoritative FC16 echo confirmation is still OPEN. No EXP291 result exists; EXP291 is not yet prepared/run in canonical state.

## Last completed experiment — EXP290
**Hypothesis:** after EXP289 proved that the local XTR accepts an unchanged reverse `03E8/14` page, change exactly one known word in that same current-session page — `03F4`, locally mapped as the Room Setpoint mirror — from the cached value `22` to `23`, then observe whether the controller applies it.

### Controlled change from EXP289
All EXP289 transport behavior was preserved:
`0708 w1=0001 -> controller FC03 03E8/14 -> gateway page response`.

Only one payload word changed:
- `03F4: 22 -> 23`
- all other `03E8/14` words were copied unchanged from the current-session FC16 cache;
- compressor had to be stopped and the original value had to be within the bounded 15..24 guard.

No other setting/register was modified.

## EXP290 observed result
The local controller requested `FC03 03E8/14` 98 ms after the `0708 w1=0001` response. The emulator returned the current-session `03E8/14` page with only `03F4 22->23`.

The first subsequent 0x0F transfer was the normal runtime `FC16 07F8/17` 680 ms later, so the bounded experiment itself did not capture an authoritative `FC16 03E8/14` echo.

However, roughly two seconds later the live ESPHome/Home Assistant `Room Setpoint` sensor changed to `23 °C`, exactly matching the injected target. No RX buffer drops occurred. One parser resync was logged at controller bus return before the active sequence; the write path itself completed and normal bus traffic continued.

### Status interpretation
- **COMPLETE / POSITIVE** for controller-visible semantic application of the reverse-page `03F4` change.
- **OPEN** for authoritative controller `FC16 03E8/14` echo of the changed value.
- The `Room Setpoint = 23 °C` observation is not yet an independent room-sensor-path confirmation; EXP291 should explicitly observe the slave-0x0A/B3C5 room-sensor path as a second confirmation channel.

## Immediately preceding experiments
### EXP289 — COMPLETE / POSITIVE
After `0708 w1=0001` triggered local `FC03 03E8/14`, the emulator returned the exact current-session cached `03E8/14` payload unchanged. The controller accepted it and continued normally with `FC16 07F8/17` 680 ms later. This locally proved reverse-page transport acceptance.

### EXP288 — COMPLETE / POSITIVE
Changing only `0708 w1` from `0000` to `0001` caused the local XTR to issue `FC03 03E8/count14` about 98–99 ms later. This locally proved that `0708 w1 bit0` can advertise/request the reverse pull of page `03E8`.

### EXP287 — COMPLETE / INCONCLUSIVE
The second runtime cycle accepted the evidence-backed branch through direct `0864/4`, but then the controller emitted direct `0870/17` instead of the experiment's mandatory post-`0864` `0708`. The experiment stopped fail-closed. This proved that post-`0864` `0708` is also conditional/state-dependent.

## Current protocol model
### Reverse/native settings path — now locally demonstrated
`0708 response advertises desired page -> controller FC03 pulls page -> emulator returns page -> controller applies at least one known changed setting`.

Locally demonstrated chain:
`FC03 0708/6 -> response w1=0001 -> FC03 03E8/14 -> reverse 03E8 page response -> controller-visible Room Setpoint changes 22->23`.

Transport and semantic application are now locally demonstrated on this XTR M. The remaining confirmation gap is an authoritative controller-originated FC16 echo of the modified `03E8/14` page.

### Runtime scheduler model
Genuine XTR captures and local experiments show at least two valid branch shapes around `085F/0864/0870`:
- `0848 -> 0864 -> 0708 -> 0870`
- `0848 -> 085F -> 0708 -> 0864 -> 0870`

Local EXP287 additionally observed direct `0864 -> 0870`. Therefore `085F` and placement of `0708` are state-dependent; 0708 must not be treated as a fixed mandatory separator.

### 0708 words
- `w1 bit0`: **PROVEN / locally confirmed** to trigger reverse `03E8/14` pull.
- `w2/w3`: **STRONGLY SUPPORTED** configuration-page request/selection bitmap.
- `w4`: **STRONGLY SUPPORTED** runtime-page bitmap/scheduler field, exact semantics still open.
- `w0`, `w5`: OPEN.

## Locally proven findings
- Full initial configuration synchronization through `06F4` is reproducible.
- Fixed historical R1 replay remains sufficient to enter the tested runtime/reverse-page path, though the genuine challenge algorithm is unresolved.
- `085F` is conditional/state-dependent in steady-state runtime.
- `0708 w1=0001` locally causes `FC03 03E8/14`.
- The XTR accepts a same-session unchanged reverse `03E8/14` page.
- A reverse `03E8/14` page with exactly one controlled change `03F4 22->23` changes the controller-visible Room Setpoint to `23 °C`.

## Important unknowns
- Authoritative controller FC16 echo timing/conditions after a reverse semantic write.
- Whether slave `0x0A:B3C5` independently confirms the same changed room setpoint on this XTR after the native reverse-page write.
- Exact semantics of 0708 `w0`, `w4`, `w5`.
- Exact scheduling/latching rules for runtime page bits and conditional `085F`.
- Genuine `071C/0730` challenge-response algorithm.
- Long-running production stability of continuous DCM emulation across operating-state changes.

## Next experiment
**EXP291 — NOT YET PREPARED / NOT RUN.**

Highest-value next test:
repeat the exact bounded EXP290 `03F4 +1` semantic write path, but remain RX-only long enough to seek **two confirmation channels**:
1. authoritative controller-originated `FC16 03E8/14` with target value at `03F4`;
2. independent room-sensor-side confirmation through the locally observed slave-`0x0A` setpoint propagation path, specifically `B3C5` if present in the expected frame.

No second semantic value should be changed. No automatic rollback write should be added unless explicitly made a separate controlled action.

## Safety constraints
- Exact stage/order/count/CRC checks remain mandatory.
- Reverse page must be based on the current-session `03E8/14` image.
- Only one already mapped word may change per semantic experiment.
- Keep bounded value guards and compressor-stop guard.
- After the semantic response, prefer RX-only observation.
- Unexpected FC03/FC16 ordering/shape remains capture-only/fail-closed.
- No broad register writes/scans or speculative unknown targets.

---

# 2026-09-29 — EXP286 COMPLETE / INCONCLUSIVE — steady-state runtime loop confirmed with conditional 085F branch

**Authoritative current state:** EXP286 COMPLETE / INCONCLUSIVE. No next live experiment is currently prepared.

## Last completed experiment — EXP286
**Hypothesis:** after EXP285 proved that the runtime sequence loops back through `07D0 -> 07E4 -> 0708 -> 07F8` without a new approval/R1 exchange, continue the entire second runtime cycle using only already locally proven ACKs and 0708 responses, then capture the next returned `07D0/19` without ACK.

### Controlled change from EXP285
All first-cycle behaviour and the EXP285-proven start of cycle 2 were retained. The new active scope was only the continuation of cycle 2 using already locally proven actions:
`07F8 ACK -> 080C ACK -> 0708 response -> 0820 ACK -> 0848 ACK -> 0708 response -> [expected 085F ACK] -> 0864 ACK -> 0708 response -> 0870 ACK -> 0884 ACK -> 0708 response -> returned 07D0 capture-only`.

No new address, payload, or semantic write was introduced.

## EXP286 observed result
Cycle 2 reproduced cleanly through:
`07F8 -> 080C -> 0708 -> 0820 -> 0848 -> 0708`.

At that point the local controller did **not** emit `085F/5`; it emitted `0864/4` directly. The experiment had intentionally made `085F` a mandatory gate, so it stopped fail-closed with `LOOP2_085F_GATE_FAILED` and did not ACK the unexpected direct `0864`.

Bus health remained clean: no RX-buffer drops and no parser resyncs during the relevant sequence.

## Strong current protocol model
The Online/DCM-style runtime loop is now locally established on the XTR M as:

`07D0 -> 07E4 -> 0708 -> 07F8 -> 080C -> 0708 -> 0820 -> 0848 -> 0708 -> [085F optional/state-dependent] -> 0864 -> 0708 -> 0870 -> 0884 -> 0708 -> 07D0 -> ...`

Key evidence:
- EXP284 closed the first full loop: after `0884 ACK -> 0708 response`, `07D0/19` returned 571 ms later.
- EXP285 proved steady-state continuation without a new approval/R1 exchange: returned `07D0` was ACKed, followed by `07E4`, `0708`, then `07F8`.
- EXP286 showed that `085F` is not mandatory in every cycle: after cycle-2 `0848 -> 0708`, the controller went directly to `0864/4`.

## Important correction to earlier interpretation
EXP281 historically stopped as COMPLETE / INCONCLUSIVE because its hypothesis expected `0864 ACK -> 0870` directly, but it observed `FC03 0708/6` first. Later genuine-capture reanalysis showed that `0864 ACK -> 0708 -> 0870` is a valid native ordering. Preserve EXP281's historical result, but do not treat that 0708 as a protocol divergence.

## Locally proven findings
- Full initial configuration synchronization through `06F4` remains reproducible.
- The fixed historical R1 replay is sufficient to reach the runtime family on this XTR, though genuine challenge-response semantics remain unresolved.
- Standard FC16 ACKs for the observed runtime pages advance the controller without injecting controller payload values.
- The local runtime cycle can close from `0884` back to `07D0`.
- A second runtime cycle begins without another approval/R1 exchange.
- `085F` can appear as an ordered gate, but is now proven **conditional/state-dependent**, not universally mandatory per cycle.

## Important unknowns
- Exact condition controlling presence/absence and payload role of `085F`.
- Exact semantics of runtime pages `07D0..0884`.
- Exact semantics of 0708 words 0, 4 and 5; word4 remains a runtime-bitmap hypothesis.
- Exact native/genuine response-selection logic for different 0708 runtime states.
- Genuine `071C/0730` challenge-response algorithm.
- Whether long-running continuous emulation remains stable across controller state changes, heating/DHW transitions, alarms, and later re-synchronization events.
- Reverse desired-state page application is still not locally proven and no semantic settings write has been authorized by these experiments.

## Next experiment
**Not assigned / NOT PREPARED.**

Highest-value next live test, when work resumes, is to make the steady-state runtime handler explicitly accept the two locally/genuinely supported post-`0848 -> 0708` branches:
1. `085F/5 -> ACK -> 0864/4`
2. direct `0864/4`

Then continue the already proven tail and verify another loop closure. This should remain a separate bounded experiment; do not silently promote it into production continuous emulation.

## Safety constraints
- Continue exact stage/order, count, bytecount, CRC and parser-health checks.
- Treat unexpected traffic as capture-only unless explicitly included in the experiment hypothesis.
- One-shot latches close before DE is raised; DE returns LOW immediately after permitted TX.
- No broad register writes/scans and no speculative semantic values.
- Standard FC16 address/count ACKs are acknowledgements, not value injection, but each new ACK stage remains an explicit active action.
- Keep semantic desired-state/page-read tests separate from runtime-session continuity tests.

---

# 2026-09-29 — EXP272 COMPLETE / POSITIVE — runtime path proven through post-07E4 0708

**Authoritative current state:** EXP272 COMPLETE / POSITIVE. EXP273 is NEXT / NOT YET PREPARED.

## Last completed experiment — EXP272
**Hypothesis:** after the EXP271-proven transition `07D0/count19 -> ACK -> 07E4/count17`, ACKing the first exact `07E4/count17` once should advance the local XTR M to the next native mailbox poll `FC03 0708/count6`.

### Controlled change from EXP271
All previously proven behavior was retained unchanged:
- fixed historical `0730`/R1 replay;
- exact ordered FC16 synchronization through `06F4/19`;
- one exact ACK of the first all-zero `085F/count5`;
- the same one-shot early mailbox response `0000 0000 0000 0000 0080 0006`;
- one exact ACK of first `07D0/count19`.

The only new active variable was:
- ACK the first exact `07E4/count17` once with `0F1007E400114068`.

The following `0708/count6` was capture-only and received no response.

## EXP272 observed result
The local XTR reproduced the full controlled chain cleanly:

`BUS_RETURN -> 071C -> fixed R1 -> 03E8 ... 06F4 -> 085F/5 ACK -> early 0708/6 -> 0080/0006 response -> 07D0/19 ACK -> 07E4/17 ACK -> post-07E4 FC03 0708/6`.

Key timing:
- `07D0/19` ACK executed at 09:37:56.434.
- `07E4/17` arrived ~2.08 s later and was ACKed once; TX execution logged at 09:37:58.534.
- exact post-`07E4` `FC03 0708/count6` arrived ~1.46 s after the `07E4` ACK.
- firmware terminated on `SUCCESS_0708_AFTER_07E4_ACK`.
- the post-`07E4` 0708 request was not answered.
- parser resync and RX-buffer-drop counters remained zero.

## EXP271 result retained
EXP271 is COMPLETE / POSITIVE. It changed only one active variable relative to EXP270: one exact standard ACK of first `07D0/count19` with `0F1007D000138067`. Exact `07E4/count17` appeared 2159 ms later and was captured without ACK. This locally proved `07D0` as the next ordered runtime gate.

## Locally proven protocol progression
The XTR M now locally confirms these ordered session/runtime gates:

`... -> 06F4/19 ACK -> 085F/5 all-zero ACK -> early 0708/6 service -> 07D0/19 ACK -> 07E4/17 ACK -> post-07E4 FC03 0708/6`.

This proves:
1. exact all-zero `085F/count5` is an ordered gate in this phase;
2. `07D0/count19` requires a standard ACK to progress to `07E4/count17`;
3. `07E4/count17` requires a standard ACK to progress to the next `0708/count6` mailbox poll.

It does **not** yet prove the correct response payload for that post-`07E4` mailbox poll, nor the local transition to `07F8/count17`.

## Strongly supported cross-capture model
New genuine-capture comparison strongly supports `0708` as a bidirectional synchronization descriptor rather than a simple idle mailbox:
- `word1=0001` is followed ~39–41 ms later by controller `FC03 03E8/count13`, after which the gateway serves the heating/settings page.
- `word2` and `word3` behave as a 32-bit request bitmap for controller->gateway FC16 page export. Multiple sparse and dense bitmap values predict the exact subsequent page families.
- `word4` is a strong candidate runtime-page bitmap, but this remains a hypothesis rather than a locally proven semantic mapping.

## Important unknowns
- Exact semantics and correct local response value for the post-`07E4` `0708/count6`.
- Whether the genuine matching response `0000 0000 0000 0000 0000 0006` is sufficient locally to advance to `07F8/count17`.
- Exact semantics of 0708 word0, word4 and word5.
- Whether fixed historical `0730` replay remains sufficient through full steady-state operation and reverse-direction desired-state reads.
- Genuine `071C/0730` challenge-response algorithm remains unresolved.

## Next experiment — EXP273
**Status: NEXT / NOT YET PREPARED.**

**Hypothesis:** after the now-proven `07E4 ACK -> post-07E4 FC03 0708/count6` transition, answer only that post-`07E4` 0708 once with the phase-matched genuine-capture response `0000 0000 0000 0000 0000 0006` (raw frame `0F030C0000000000000000000000069D76`), then capture the first exact `07F8/count17`.

Only that one post-`07E4` 0708 response may be the new active variable. `07F8` must remain capture-only. No later runtime ACKs, no semantic settings writes, no broad mailbox service and no scans.

## Safety constraints
- Exact stage/order matching remains mandatory.
- One-shot ACK/response latches close before DE is raised.
- DE returns LOW immediately after every permitted frame.
- Unexpected FC03/FC16 families, duplicate completed-stage requests, parser resync/drop deltas or peer-response anomalies remain fail-closed stops.
- No semantic register values are injected by standard FC16 address/count ACKs.
- Any future desired-state/page-read experiment must remain separate from runtime-session completion experiments.

---

## 2026-09-28 — bidirectional 0x0F page-cache model / EXP270 PREPARED

New cross-capture analysis materially refines the likely Online write architecture.

### Observed 0708 -> FC03 read-side trigger
In `thermia_capture_20260924_210001`, two `FC03 0708/count6` responses have word1=`0001`. Both are followed within ~39–41 ms by a controller-originated `FC03 03E8/count13` read from slave 0x0F. The returned 13-word page differs between the two events only at `03E8` (`0017 -> 0016`). Other 0708 responses in the same capture with word1=0 are not immediately followed by that 03E8 read.

The `03E8` page is the known heating-settings family. A separate genuine DCM capture shows the controller sending the same 13-word image in the opposite direction with `FC16 03E8/count13`.

**Strong architectural conclusion:** slave 0x0F behaves like a bidirectional page cache/interface. Controller -> gateway data moves by FC16 writes; gateway -> controller desired/config data can move by controller-initiated FC03 reads. This is a much better fit than a second-master write model.

**Current write-path hypothesis:** a gateway advertises pending desired/config data through the 0708 control/status words (word1 is the leading candidate for the 03E8 page), after which the controller reads the page from 0x0F and decides whether/how to apply it. This is not yet proven on the XTR M and must not be treated as an authorized semantic write path until a bounded local test confirms application and authoritative echo.

### EXP270 — PREPARED / NOT RUN

**Hypothesis:** the local XTR stalls after `06F4/19` because the pending exact all-zero `085F/count5` transaction is ordered session traffic and must be ACKed. EXP268/269 both saw it after 06F4 and deliberately ignored it; successful Eco5 sessions ACK it before first 07D0 whenever it is still pending.

**Only new active variable versus EXP269:** ACK the first exact controller-originated all-zero `085F/count5` once with standard FC16 response `0F10085F00053356`.

The proven R1 + FC16 chain through 06F4 remains unchanged. If `0708/6` occurs after the 085F ACK before 07D0, preserve the same single EXP269 phase-matched response `0000 0000 0000 0000 0080 0006`; no second mailbox response is allowed. Primary success is controller-originated `07D0/count19`, which is capture-only and never ACKed in EXP270.

Safety remains fail-closed: exact all-zero 085F shape only, one 085F ACK maximum, no broad writes/scans, parser/drop and peer-response guards retained. Experimental controls remain under Configuration with red/brown trace markers.

**Historical state at that point: EXP270 PREPARED / NOT RUN.**

## 2026-09-28 — community HMAC-SHA256 serial-number hypothesis

A community post proposed that the 16-byte 071C/0730 response may be the first 128 bits of HMAC-SHA256(challenge, serial-number-string). The example claimed:

challenge `01bd6eba71bff920128ab44bae2537eb`
key `******24190327`
expected response `826ed2acbc1b3db93adec93c53087a53`.

Independent calculation of HMAC-SHA256 using the literal ASCII key `******24190327` does **not** reproduce that response; it yields a different prefix. Therefore the example as written is not yet verified and must not be treated as a confirmed algorithm.

The hypothesis remains worth testing once the real Eco5 serial number/key encoding is known, because six genuine challenge/response pairs are available. Test variants should be limited and evidence-driven: exact serial string, possible model prefixes/suffixes, zero-padding, ASCII vs BCD/binary, and full-vs-truncated HMAC comparison. Do not perform broad brute-force key search.

## 2026-09-28 — deeper analysis of itec_eco5_gateway_20260928.log

Direct full-log parsing confirms four power-cycle sessions beginning after bus gaps at approximately 193.555, 438.000, 734.310 and 974.803 s. All four ultimately establish a working gateway session.

### Approval timing
Successful 071C/0730 replies occur on challenge request #29 in sessions 1 and 4 (~120 s after bus return), and on challenge request #3 in sessions 2 and 3 (~10 s after bus return). Reply latency is 30–47 ms.

First ACK of FC16 03E8, however, is tightly clustered at +120.296, +118.478, +118.550 and +120.038 s after bus return. In sessions 2 and 3 the controller therefore repeats 03E8 102 times over ~108 s before the gateway begins ACKing it. This strongly separates challenge-answer capability from later FC16/session-service readiness.

### 085F ordering
The exact all-zero 085F/5 request receives exactly one ACK in each power-cycle session:
- S1: ACK at 312.360 s, before successful challenge response at 313.728 s.
- S2: 06F4 ACK at 590.919 s -> 085F request+ACK at 590.996 s -> 0708 idle reply at 592.311 s -> 07D0 at 592.930 s.
- S3: 06F4 ACK at 888.765 s -> 085F request+ACK at 889.309 s -> 0708 idle reply at 892.978 s -> 07D0 at 893.603 s.
- S4: 085F ACK at 1093.398 s, before successful challenge response; later 06F4 ACK at 1129.287 s -> 07D0 at 1129.365 s.

This is a very close match to local EXP268/269, where 085F appeared after 06F4 but was deliberately ignored. The strongest next local hypothesis is therefore that missing 085F ACK, not mailbox payload selection, is the direct blocker to first 07D0.

Important nuance: in S2/S3 one normal 0708 idle transaction occurs after 085F ACK and before 07D0. Therefore the phase-matched expected local path is likely 06F4 -> ACK exact 085F/5 -> optionally answer the next exact 0708/6 with the normal idle frame -> capture 07D0.

### Mailbox script
Raw wire words after the first sync are deterministic:
- normal idle frame is **0000 0000 0000 0000 0100 0000** on the wire (not 0001 in Modbus big-endian word notation);
- then **0000 0000 4000 8000 010B 0000**;
- then **0000 0000 FFFF 867F 03DF 0000**.

Across all four new sessions the 03DF trigger is followed by a new 03E8 within 62–94 ms. This second synchronization immediately interleaves the normal configuration pages with 07D0/07E4 runtime pages.

Project implication: correct prior documentation that described the raw idle fifth word as 0001; the raw Modbus word is 0100. Continue to preserve exact raw frame bytes when replaying.

**Next experiment candidate (not yet prepared): EXP270 — exact 085F ACK gate.** Build from the known-good EXP268 path, changing only handling of the exact all-zero 085F/5 from ignore to one ACK. Preserve the known idle 0708 response and stop/capture on first 07D0. No new mailbox values.

## 2026-09-28 — piotrek_r second-capture interpretation materially refines next step

New peer analysis of `itec_eco5_gateway_20260928.log` adds two important corrections:

1. `085F/5` must no longer be treated as harmless background during session establishment. Across the cited Eco5/ATEC transitions it is ACKed before first `07D0`; when pending after `06F4`, the controller sends `085F`, waits for its ACK, then proceeds to `07D0`. This suggests queue/ordering semantics.

2. The post-first-sync mailbox script is highly repeatable across complete Eco5 sessions. Sequence reported:
   - several idle responses `0000 0000 0000 0000 0100 0000`;
   - then `0000 0000 4000 8000 010B 0000`;
   - then `0000 0000 FFFF 867F 03DF 0000`.
   The last pattern is followed by a second full synchronization within ~0.06–0.11 s in all observed complete sessions.

Timing evidence further separates challenge approval from session service: challenge response may occur ~10 s or ~120 s after bus return, yet first FC16 ACK clusters around ~118 s after bus return. Long unacked repetition of `03E8/14` can persist for nearly two minutes without breaking the session.

Challenge/response remains unresolved. Six observed responses are all different and no simple XOR/difference relation was found. Reply latency (~30–60 ms) strongly favors local computation or a non-challenge-dependent lookup/token mechanism. Fixed replay working locally therefore remains relevant but does not prove equivalence with a genuine session.

**Implication for next local experiment:** before inventing new mailbox values, test the newly recognized queue prerequisite by ACKing the exact pending `085F/5` after `06F4` if it appears, while keeping all other post-`06F4` traffic capture-only. This is a narrower and better-supported hypothesis than further mailbox variation.

## 2026-09-28 external Eco5 capture — major correction to post-06F4 interpretation

New raw capture `itec_eco5_gateway_20260928.log` materially changes the interpretation of EXP269.

Observed in a fully successful genuine Eco5 session:
- `071C/0730` challenge at 313.682 s received a distinct 16-byte response at 313.728 s.
- The controller immediately started the normal FC16 export at `03E8`.
- After the proven chain reached `06F4/19`, `07D0/19` followed only ~78 ms later, **before any subsequent 0708 mailbox poll**.
- `07E4/17` followed; only afterwards did `0708/6` occur, answered with the familiar `0000 0000 0000 0000 0001 0000` idle frame, then `07F8/17`, etc.

This disproves the working assumption used for EXP269 that the first post-`06F4` mailbox reply must unlock `07D0`. In a genuine successful session, `07D0` can be part of the FC16 continuation itself.

The same capture contains four genuine `071C/0730` challenge-response pairs with different challenges and different 16-byte responses. This is strong evidence that the response is challenge-dependent rather than a fixed session token. Our fixed captured response can still trigger the early XTR sync, but may establish only a partial/insufficient session state, explaining why local progression stops after `06F4`.

**Current direction:** do not vary 0708 payloads further as the primary next step. Highest-value work is now understanding/reproducing the genuine `071C/0730` response mechanism or identifying which session state the dynamic response establishes before `03E8`.

## EXP269 UI follow-up

User supplied a photo of the Thermia main display after EXP269. The screen shows `KAMER 22.2°C (22.0)`, `EVU-STOP`, `BEDRIJF AUTO`, and the lower-right heat-pump/tank status graphic. The user reports that the previously hollow-looking `0`/status glyph now has its center filled, while an alarm is still present.

Interpretation remains deliberately limited: this is evidence of a visible UI/state change after the `0080/0006` mailbox test, but it does **not** show that the Online session completed or that the alarm condition cleared. Exact semantics of the glyph remain unknown until the alarm/detail screen is identified.

# EXP269 — COMPLETE / NEGATIVE FOR SINGLE 0080/0006 PHASE-MATCH RESPONSE

**Hypothesis:** the first post-`06F4` `FC03 0708/count6` on the XTR would progress to `FC16 07D0/19` if answered once with the exact Eco5 phase-matched response `0000 0000 0000 0000 0080 0006`.

**Observed facts**
- Full proven approval/sync prefix reproduced through `06F4/19`.
- First exact `0708/6` arrived +1.566 s after the `06F4` ACK.
- Exactly one response was transmitted: `0F030C0000000000000000008000069C9E`.
- No `07D0/19` appeared.
- `0708/6` repeated after ~4.43 s and continued repeatedly during the 30 s RX-only window.
- Final summary: `responses_sent=1 mailbox_requests=8 ignored_bg=15 resync_postreturn=0 drop_postreturn=0 DE=LOW`.
- Recurrent `085F/5` remained the only observed post-`06F4` FC16 family.
- A80E again changed `0008 -> 0028`, and AFDC later reported `32`.
- User observed a visible display/UI change described as “the middle of the 0 is now filled”; exact UI element/semantic meaning is not yet identified.

**Strong conclusions**
- The Eco5 `0080/0006` mailbox response is **not sufficient by itself** on the XTR to trigger `07D0/19`.
- The mailbox path remains electrically/protocol-valid and stable; the negative result is not explained by parser or RX-drop faults.
- The missing condition lies before or alongside the mailbox payload itself: likely controller/session state, model-specific mailbox semantics, or an additional prerequisite from the Eco5 trace.

**Hypotheses**
- The visible UI change may indicate that `0080/0006` changed an internal state despite not triggering `07D0`; this requires direct UI identification before assigning meaning.
- The Eco5 first-mailbox payload may only be effective when another state established earlier in the genuine Online session is present.
- `071C/0730` replay may unlock only a subset of the genuine Online state machine.

**Unknowns**
- Exact meaning of the newly observed filled-center display symbol.
- Which pre-`0708` Eco5 state differs from the XTR replayed session.
- Whether `07D0` is gated by a second mailbox transaction, an FC17/DCM state, or another controller-side condition.

**Current experiment state:** EXP269 COMPLETE / NEGATIVE. Next experiment not yet assigned.

---
# EXP269 — PREPARED / NOT RUN — phase-matched post-06F4 mailbox response

**Hypothesis:** the XTR failed to progress after EXP268 because the reused `0001/0000` mailbox payload was not the correct payload for the first post-`06F4` phase. In the matching Eco5 raw capture the first exact `FC03 0708/count6` after `06F4/19` is answered with `0F030C0000000000000000008000069C9E` (words `0000 0000 0000 0000 0080 0006`), followed about 0.7 s later by `FC16 07D0/count19`.

**Only experimental changes from EXP268:** replace the mailbox payload with the exact phase-matched Eco5 `0080/0006` response and send it exactly once. The proven R1/prefix/tail chain through `06F4/19`, safety gates, parser/drop checks and background handling remain unchanged.

**Expected success signal:** after the one exact mailbox response, capture local `07D0/19`. Do not ACK it. Any first different non-background FC16/FC03 is capture-only and terminates. Repeated `0708/6` is logged RX-only and not answered. Observation timeout is 30 s after the single mailbox response.

**Safety:** one new phase-matched mailbox TX only; no second mailbox response, no post-mailbox FC16 ACK, no invented payload values, no broad register writes/scans. Experimental controls remain under Configuration and logs retain red/brown markers.

**Current experiment state:** EXP269 PREPARED / NOT RUN. The previous 10x-idle EXP269 design is superseded and must not be run.

---
# EXP269 — PREPARED / NOT RUN — extended bounded mailbox service

# ECO5 LOG REVIEW — materially revises post-06F4 mailbox interpretation

Direct review of the Eco5 raw captures shows that the first post-`06F4/19` mailbox response is **not always** the previously reused idle frame `0000 0000 0000 0000 0001 0000`.

In `thermia_capture_20260925_090209.log` the sequence is:
`06F4/19 -> 0708/6 -> response 0000 0000 0000 0000 0080 0006 -> 07D0/19 -> 07E4/17 -> 0708/6 -> response ...0000 0006 -> 07F8/17 -> 080C/18 -> ...`.
Thus the mailbox poll and later FC16 pages are interleaved, and the first response payload is phase-specific.

EXP268 local timing closely matches the Eco5 first post-06F4 poll (~3.6 s), but our response payload differed (`0001 0000` vs Eco5 `0080 0006`) and no `07D0` followed. This is stronger evidence that **payload content/state matters more than response count**.

A second Eco5 capture (`thermia_capture_20260925_090550.log`) shows unanswered `0708/6` polls coexisting with repeated `0870/17`, and a later response `0000 0000 7FFF FFFF 0080 0007` immediately triggers a new FC16 sync beginning at `03E8/13`. This confirms that mailbox payload values are active commands/state selectors and must not be generalized across phases.

**Project decision:** do not run the previously prepared “10 identical idle replies” EXP269 as-is. It is superseded before execution. Any revised EXP269 must be built from the exact Eco5 post-`06F4` sequence and keep the first new payload tightly bounded/capture-only afterwards.


**Hypothesis:** EXP268 showed that after three genuine Eco5 idle responses followed by 30 s RX-only, `FC03 0708/count6` continued at the same ~4.2 s cadence and only recurrent `085F/5` FC16 background traffic appeared. If genuine Online keeps the idle mailbox serviced continuously, stopping after response #3 may itself prevent or delay later parallel runtime/synchronization traffic. EXP269 therefore changes only one active variable: increase the maximum exact idle mailbox responses from 3 to 10. The response payload, proven prefix, timing gates and fail-closed checks remain unchanged. After response #10, remain RX-only for 30 s.

Special-interest capture-only families remain `07D0/19, 07E4/17, 07F8/17, 080C/18, 0820/18, 0834/18, 0848/23, 0864/4`. Any first different non-background FC16 or different FC03 ends the experiment without ACK/response. Recurrent `085F/5` and `04A6/13` remain background.

**Safety:** same known-good exact mailbox response `0F030C0000000000000000010000001C88`; maximum 10 responses; no eleventh response; no new payload values; no post-mailbox FC16 ACK; no broad writes/scans. Parser/RX-drop delta after BUS_RETURN, approval retry or unexpected peer response stops TX. Recovery remains one normal Thermia-controller reboot.

# EXP268 RESULT — COMPLETE / NEGATIVE FOR 30 S RX-ONLY PARALLEL-RUNTIME OBSERVATION

**Hypothesis:** after three bounded genuine Eco5 idle responses, later Online/Link FC16/runtime traffic may still appear while repeated `0708/6` mailbox polling continues unanswered.

**Observed facts**
- Full proven approval/synchronization prefix reproduced through `06F4/19`.
- One CRC resync occurred at controller BUS_RETURN; the experiment then established that value as its baseline. Final summary reported `resync_postreturn=0` and `drop_postreturn=0`.
- First `0708/6` arrived +3.621 s after the `06F4` ACK.
- Three exact genuine Eco5 idle responses were transmitted.
- After response #3, the ESP remained RX-only for 30 s.
- During that RX-only window, exact `0708/6` continued repeatedly; total mailbox requests for the run reached 10, so 7 post-response-#3 polls were observed without response.
- Recurrent `085F/5` continued throughout; 21 post-`06F4` background FC16 frames were counted.
- No different non-background FC16 and no different FC03 appeared during the 30 s RX-only window.
- No `07D0..0864` special-interest family was observed.
- A80E later changed `0008 -> 0028` and AFDC changed to 32 during the observation window, but the semantics of those state changes remain unknown.
- DE was LOW at summary.

**Strong conclusions**
- Unanswered `0708/6` remains a persistent periodic mailbox poll for at least 30 s after three valid idle responses.
- Stopping mailbox replies after response #3 does not cause any immediate later FC16/runtime family to appear within the next 30 s.
- EXP268 does **not** prove that later runtime traffic is absent during correctly continued mailbox servicing.

**Hypotheses**
- A genuine Online endpoint may need to keep returning the idle mailbox response continuously while other synchronization/runtime traffic progresses in parallel.
- The absence of later FC16 pages in EXP268 may be caused by the bounded mailbox service ending after only three responses, or simply by a longer timing/state dependency.

**Unknowns**
- Whether continued exact idle service for a longer bounded interval causes or permits `07D0..0864` traffic.
- Whether A80E `0x28` / AFDC `32` are related to an active-but-incomplete Online state.
- Whether later mailbox non-idle fifth-word values are required for application writes only, rather than session progression.

**Current experiment state:** EXP268 COMPLETE / NEGATIVE. EXP269 PREPARED / NOT RUN.

---

# EXP267 RESULT# EXP267 RESULT# EXP267 RESULT — COMPLETE / NEGATIVE FOR <=3-IDLE-RESPONSES PROGRESSION

**Hypothesis:** up to three consecutive exact `FC03 0708/count6` polls may require the same genuine Eco5 idle response before the controller progresses.

**Observed facts**
- The full proven Online/Link prefix through `06F4/19` reproduced cleanly.
- Recurrent `085F/5` traffic was correctly treated as background after `06F4`.
- First local `0708/6` arrived +1.561 s after the `06F4` ACK.
- Three exact mailbox responses were transmitted, all identical: `0F030C0000000000000000010000001C88`.
- The controller requested `0708/6` again after each response.
- Approximate request/response-to-next-request spacings were ~4.4 s, ~4.1 s and ~4.18 s.
- A fourth `0708/6` was captured after response #3 and deliberately received no response.
- No different meaningful FC03/FC16 appeared before that fourth poll.
- Parser resyncs remained 0 and RX buffer drops remained 0 during the active run.

**Strong conclusions**
- Repeating the genuine Eco5 idle mailbox response three times is not sufficient to make the local XTR leave the observed `0708/6` polling phase.
- The ~4.2 s `0708/6` repetition is stable enough to look like normal mailbox servicing cadence rather than a one-shot retry caused by malformed transport.
- EXP267 is therefore a valid negative result for the specific hypothesis “<=3 identical idle responses cause immediate progression”.

**Hypotheses**
- `0708/6` may be a persistent runtime mailbox poll that is expected to continue indefinitely while idle.
- Later non-idle fifth-word values seen in the genuine Eco5 capture may be state/content, not a simple completion countdown we should invent.
- Later Online/Link FC16 traffic may be independent of continued idle mailbox responses and may appear on a longer timescale.

**Unknowns**
- Whether the XTR ever emits the later `07D0..0864` sync/runtime families after this point.
- Whether a different mailbox content/state is required to progress.
- Whether persistent mailbox servicing changes the DHW/COMM. ERR ONLINE/LINK side effect.

**Current experiment state:** EXP267 COMPLETE / NEGATIVE. EXP268 PREPARED / NOT RUN.

---

# EXP267 — PREPARED / NOT RUN — bounded repeated 0708 mailbox responses

**Hypothesis:** EXP266 proved that one genuine Eco5 idle response to local `FC03 0708/count6` is accepted without destabilising the bus, but the controller repeats the same request about 4.18 s later. EXP267 changes only one experimental variable: answer at most the first **three** exact post-`06F4` `0708/6` polls with the same genuine Eco5 idle response `0F030C0000000000000000010000001C88`. If repeated polling is normal mailbox servicing, the controller may transition to another FC03/FC16/runtime phase after repeated valid responses.

Safety: proven prefix unchanged; only exact `0F 03 0708 0006` requests are answered. Response #1 must arrive within 30 s after `06F4`; responses #2/#3 must each arrive within 10 s of the previous response. Parser/RX-drop deltas, approval retry or unexpected peer FC17/ACK stop TX. The response counter advances before DE. Maximum 3 mailbox responses; no fourth response; no post-mailbox FC16 ACK. Known response words are `0000 0000 0000 0000 0001 0000`; effect observed in EXP266 was continued healthy traffic plus another `0708/6` poll, not session completion.

Expected decisive outcomes: (a) a different FC03/FC16 after <=3 responses, supporting progression; (b) a fourth `0708/6`, showing repeated idle polling continues; or (c) timeout/integrity stop. Negative outcomes are recorded.

# EXP266 RESULT — COMPLETE / PARTIAL POSITIVE

**Hypothesis:** After the proven prefix through `06F4/19`, respond exactly once to local `FC03 0708/count6` with the genuine Eco5 idle mailbox response `0F030C0000000000000000010000001C88`, then remain RX-only.

**Observed facts**
- Full proven prefix repeated cleanly through `06F4/19`.
- `085F/5` appeared +95 ms after the `06F4` ACK and was correctly ignored as recurrent background traffic.
- Local `FC03 0708/count6` arrived +1.561 s after the `06F4` ACK.
- Exactly one mailbox response was transmitted: `0F030C0000000000000000010000001C88`; DE returned LOW and the one-shot latch remained closed.
- The controller issued the same `FC03 0708/count6` again +4.180 s after the mailbox response. No second response was sent.
- Parser resyncs remained 0 and RX buffer drops remained 0.

**Strong conclusion**
- The genuine Eco5 idle mailbox response does not by itself complete the local XTR mailbox exchange; the controller requests `0708/6` again about 4.18 s later.
- This is a real local protocol result, not a parser artefact.

**Hypotheses**
- The `0001` idle response may need to be returned repeatedly while idle, as in the genuine Eco5 capture.
- Alternatively, a later mailbox-state value or cadence may be required before runtime sync proceeds.

**Unknowns**
- Whether repeated identical idle responses will advance the session.
- Whether the later fifth-word countdown seen in the genuine capture is controller-driven, gateway-driven, or dependent on repeated polls.
- Whether completing mailbox servicing removes DHW `0` / `COMM. ERR ONLINE/LINK`.

**Current experiment state:** EXP266 COMPLETE / PARTIAL POSITIVE. No EXP267 prepared yet.

---

# EXP266 — PREPARED / NOT RUN — ONE-SHOT 0708 MAILBOX RESPONSE

**Hypothesis:** after the locally proven sync tail `06EA/7 -> 06F1/3 -> 06F4/19`, the first exact `FC03 0708/count6` mailbox request can be answered once with the genuine Eco5 idle response `0F030C0000000000000000010000001C88` (words `0000 0000 0000 0000 0001 0000`), causing the XTR M to advance into the next Online/Link runtime phase.

**Only new active variable:** one exact response to first post-06F4 `FC03 0708/count6`. No other FC03 is answered; no second 0708 response; no post-mailbox FC16 ACK.

**Safety gate:** phase 24 after exact 06F4 ACK; first exact 0708/6; <=30 s; parser/drop clean; no approval retry; no unexpected peer FC17/FC16 ACK; latch closed before DE. After the one response the test is RX-only and captures the first non-background FC16 or any FC03. Known recurrent `085F/5` and `04A6/13` are logged and ignored.

**Known possible effect:** may advance Online/Link runtime synchronization. **Unknowns:** local acceptance, next runtime frame, controller/UI state, whether DHW `0` / `COMM. ERR ONLINE/LINK` disappear.

**Prepared YAML:** `thermia_itec_xtr_m_waveshare_exp266.yaml`.

---

## Current experiment status — EXP265 COMPLETE / STRONG POSITIVE — LOCAL 0708/6 MAILBOX REQUEST CONFIRMED

Hypothesis: continue the proven Online/Link synchronization tail by ACKing exact `06EA/7 -> 06F1/3 -> 06F4/19`, then stop transmitting and capture the first later frame.

Observed:
- `06EA/7` appeared and was ACKed once.
- `06F1/3` appeared next and was ACKed once.
- `06F4/19` appeared next and was ACKed once.
- The first later FC16 was `085F/5`, only 107 ms after the `06F4` ACK.
- `085F/5` is already known as recurrent passive/background traffic, so this does **not** establish `085F/5` as the next synchronization stage.
- No mailbox response was sent.
- Parser resync count incremented once at controller return (`CRC resync at 0x06 0x17`) before the post-return experimental chain; RX drops remained 0.
- No stage retry or approval retry occurred in the serviced chain.

Strong conclusion:
- The local XTR accepts the exact tail `06EA/7 -> ACK -> 06F1/3 -> ACK -> 06F4/19 -> ACK`.
- EXP264's capture rule was too broad to identify the next meaningful sync stage because a known recurrent `085F/5` background frame arrived first.

Next-test requirement:
- Preserve the proven chain.
- After `06F4/19`, ignore known recurrent/background FC16 families for discovery purposes (at minimum `085F/5`; `04A6/13` remains context-sensitive), while still logging them.
- Capture the first non-background FC16 or FC03, especially any `0708/count6` mailbox poll, without answering it.

Recovery: one normal Thermia-controller reboot after the incomplete session.

## Authoritative current state — 2026-09-27 — EXP263 COMPLETE / STRONG POSITIVE

## EXP264 — PREPARED / NOT RUN

**Hypothesis:** after the locally proven Online/Link synchronization prefix through `06C5/count33`, the XTR will continue with the genuine Eco 5 tail `06EA/count7 -> 06F1/count3 -> 06F4/count19`. EXP264 ACKs only those three exact frames, in order, with <=5 s timing and clean parser/drop state, then becomes capture-only. Any FC03 is never answered; if `0708/count6` appears after the `06F4` ACK it is captured as mailbox evidence only.

**New TX frames:**
- `06EA/7` ACK: `0F1006EA0007A199`
- `06F1/3` ACK: `0F1006F10003D05D`
- `06F4/19` ACK: `0F1006F40013C190`

**Safety:** complete proven prefix unchanged; no broad ACKing, no FC03 response, no mailbox response, no TX after `06F4`; any retry/unexpected frame/parser-drop delta stops fail-closed. Known incomplete-session DHW `0` / `COMM. ERR ONLINE/LINK` side effect remains recoverable by one normal controller reboot.

### EXP263 — accelerated 12-block 33-word batch — COMPLETE / STRONG POSITIVE

Hypothesis:
After the proven local prefix through 0546/count20, ACK the exact genuine Eco 5 33-word sequence
055A, 057B, 059C, 05BD, 05DE, 05FF, 0620, 0641, 0662, 0683, 06A4, 06C5
(all count=33), then stop TX and capture the first different FC16/FC03. Genuine Eco 5 predicts 06EA/count7.

Observed:
- Approval request arrived +1283 ms after controller return.
- R1 sent exactly once.
- Proven prefix through 0546/count20 reproduced cleanly.
- Exact 33-word sequence observed and ACKed once each, in order:
  055A -> 057B -> 059C -> 05BD -> 05DE -> 05FF -> 0620 -> 0641 -> 0662 -> 0683 -> 06A4 -> 06C5.
- First different post-06C5 frame was exact 06EA/count7, +475 ms after the 06C5 ACK:
  RAW=0F1006EA00070E000A00200017001B0009001A0006F81A
- 06EA was deliberately NOT ACKed.
- Parser resyncs since boot remained 0 after the run and RX buffer drops remained 0.
- No approval retry after R1 and no stage retry was observed in the captured chain.
- DE returned LOW after each TX.

Strong conclusions:
- Local XTR follows the genuine Eco 5 Online/Link synchronization chain through the full 055A..06C5 sequence of twelve 33-register FC16 blocks.
- Genuine Eco 5 prediction 06EA/count7 is now locally confirmed immediately after 06C5.
- Accelerated multi-page batching remains valid for this already-known sync sequence.
- Full Online/Link establishment is still NOT proven.

Hypotheses:
- The recurring DHW-side literal 0 / COMM. ERR ONLINE/LINK remains consistent with an approved but incompletely serviced Online/Link session timing out.
- Completing the remaining 06EA/06F1/06F4 phase may move the session closer to runtime/mailbox behavior, but this is not yet proven locally.

Unknowns:
- Local behavior after ACKing 06EA/count7.
- Whether 06F1/count3 and 06F4/count19 follow locally exactly as in the Eco 5 capture.
- Where the first local 0708/count6 mailbox poll appears relative to later sync pages.
- Whether a sufficiently complete session prevents the DHW-side 0 and COMM. ERR ONLINE/LINK side effects.

Safety / recovery:
- One normal Thermia-controller reboot after the incomplete EXP263 session.
- No next experiment prepared yet.
- EXP239 remains OPEN. EXP238 remains PARKED / NOT RUN.

## Authoritative current state — 2026-09-27 — EXP262 COMPLETE / STRONG POSITIVE

### EXP262 result
Hypothesis: accelerate the proven Online/Link synchronization by ACKing eight additional genuine Eco 5 FC16 pages in exact order after the locally proven prefix, then stop and capture the next different frame.

Observed: EXP262 reproduced the full ordered chain through `0546/count20` and then captured exact `055A/count33` +637 ms later. The new accelerated block was `04A6/13 -> ACK -> 04BA/22 -> ACK -> 04D8/27 -> ACK -> 04F6/14 -> ACK -> 050A/19 -> ACK -> 051E/10 -> ACK -> 0532/18 -> ACK -> 0546/20 -> ACK -> 055A/33`. `055A` was deliberately not ACKed.

Integrity: one approval, no approval retry after R1, no stage retry in the acknowledged chain, parser resync count remained 0 and RX buffer drops remained 0. Existing production functionality was not intentionally changed.

Strong conclusion: the accelerated multi-page strategy is valid at least through `0546/count20`; the local XTR matches the genuine Eco 5 synchronization order through `055A/count33`. Full Online/Link establishment remains unproven.

Unknowns: the behavior after ACKing `055A/count33`, the exact point at which the `0708/count6` mailbox appears locally, and whether completing enough of the session prevents the known DHW-side `0` / `COMM. ERR ONLINE/LINK` failure state.

Safety/recovery: current session remains deliberately incomplete; perform one normal Thermia-controller reboot before another active experiment. No next experiment prepared yet. EXP239 OPEN. EXP238 PARKED / NOT RUN.

# THERMIA PROJECT STATE

## Authoritative current state — 2026-09-27 — EXP261 COMPLETE / EXP262 PREPARED

### EXP262 — accelerated 8-block sync batch — PREPARED / NOT RUN

**Hypothesis**
After the locally proven prefix through `0492/count11` and the locally captured next `04A6/count13`, acknowledge a bounded batch of eight exact controller-originated FC16 pages:
`04A6/13 -> 04BA/22 -> 04D8/27 -> 04F6/14 -> 050A/19 -> 051E/10 -> 0532/18 -> 0546/20`.
Then capture the first different FC16 or FC03 without answering it. Genuine Eco 5 predicts `055A/count33`.

**New active targets and known basis**
- `04A6/13`: locally observed immediately after the `0492` ACK in EXP261; also a recurrent genuine Eco 5 family, so context matters. A genuine gateway has ACKed this family in captured sessions.
- `04BA/22`, `04D8/27`, `04F6/14`, `050A/19`, `051E/10`, `0532/18`, `0546/20`: all observed in the genuine Eco 5 successful synchronization traffic.
- These are controller-originated FC16 export pages; the experiment sends only standard FC16 acknowledgements, not new register payload values. The known protocol effect is progression of the Online/Link session; direct application-setting effects are not established.
- Known incomplete-session side effect remains DHW-side literal `0` and `COMM. ERR ONLINE/LINK`; recovery is one normal Thermia-controller reboot.

**Fail-closed**
- Existing proven prefix remains unchanged.
- Each new page must be the first exact expected page, with exact count/bytecount/full length, within 5 s of the preceding ACK.
- Any retry, unexpected FC16/FC03, peer FC17/ACK, or post-return parser/drop delta stops further TX.
- After `0546/20` ACK: capture-only; no `055A` ACK and no mailbox response.
- Maximum active TX: one R1 plus seventeen exact FC16 ACKs.


## Authoritative current state — 2026-09-27 — EXP261 COMPLETE / STRONG POSITIVE

- Last completed experiment: **EXP261 — COMPLETE / STRONG POSITIVE**.
- No next experiment is prepared yet.
- **EXP239 remains OPEN.**
- **EXP238 remains PARKED / NOT RUN.**

### EXP261 hypothesis

Continue the proven local Online/Link prefix using a bounded three-block batch:
`046A/count18 -> ACK -> 047E/count19 -> ACK -> 0492/count11 -> ACK`,
then capture the first different FC16/FC03 stage without answering it.

The genuine Eco 5 reference commonly predicts `04A6/count13` next. Because `04A6/13` is also a recurrent passive family, this was treated as a prediction rather than a strict success requirement.

### EXP261 observed result

The complete observed sequence was:

`R1 -> 03E8/14 ACK -> 03FC/11 ACK -> 0410/22 ACK -> 042E/15 ACK -> 0442/13 ACK -> 0456/12 ACK -> 046A/18 ACK -> 047E/19 ACK -> 0492/11 ACK -> 04A6/13`

Key timings:
- first approval: +1245 ms after BUS_RETURN;
- 046A/18: +1433 ms after 0456 ACK;
- 047E/19: +722 ms after 046A ACK;
- 0492/11: +1480 ms after 047E ACK;
- first post-0492 frame: `04A6/count13`, +576 ms after the 0492 ACK.

Exact captured post-0492 request:
`0F1004A6000D1A0000000000000000000000000000000000000000402000000000CA9A`

It was not acknowledged.

Integrity:
- all planned one-shot ACKs through 0492 were used exactly once;
- no stage retries;
- no approval retry after R1;
- no unexpected peer FC17 / FC16 ACK;
- no post-return parser-resync or RX-drop delta in the experiment summary;
- DE returned LOW.

### Strong conclusion

EXP261 extends the local XTR match with the genuine Eco 5 Online/Link synchronization chain through `0492/count11`, and the first next block is exactly `04A6/count13`.

The bounded-batch method remains valid and materially reduces required controller restarts while preserving a clear fail-closed boundary.

Full Online/Link establishment remains unproven because `04A6` and all downstream pages/mailbox traffic remain unanswered.

### Side effects / recovery

Front-panel side effects for this specific EXP261 run have not yet been reported. Prior incomplete sessions repeatedly produced DHW-side `0` and `COMM. ERR ONLINE/LINK`. Continue to recover with one normal Thermia-controller reboot after summary.

---


## Authoritative current state — 2026-09-27 — EXP260 COMPLETE / EXP261 PREPARED / NOT RUN

- Last completed experiment: **EXP260 — COMPLETE / STRONG POSITIVE**.
- Current prepared experiment: **EXP261 — bounded three-block continuation `046A/18 -> 047E/19 -> 0492/11`, then capture-only — PREPARED / NOT RUN**.
- **EXP239 remains OPEN.**
- **EXP238 remains PARKED / NOT RUN.**

### EXP261 hypothesis

EXP260 proved the bounded-batch method works and extended the local XTR Online/Link sequence through exact `046A/count18`. EXP261 keeps all previously proven behavior unchanged and adds only three further one-shot FC16 ACKs, in the genuine Eco 5 order:

`046A/count18 -> ACK -> 047E/count19 -> ACK -> 0492/count11 -> ACK -> capture first different FC16/FC03`

The genuine Eco 5 capture commonly has `04A6/count13` after `0492/count11`, but `04A6/13` is also a recurrent passive family. EXP261 therefore treats `04A6/13` as the primary prediction, not as a required success condition. The first different post-0492 frame is captured and never answered.

### Exact new active targets

- `046A/count18` ACK: `0F 10 04 6A 00 12 60 06`
- `047E/count19` ACK: `0F 10 04 7E 00 13 E1 C2`
- `0492/count11` ACK: `0F 10 04 92 00 0B 20 3D`

All three are standard FC16 ACKs carrying no register-value payload.

### EXP261 fail-closed boundary

Each new ACK is permitted only for the first exact expected FC16 block, within 5 s of the immediately preceding ACK, with no prior stage retry, no unexpected peer response, and unchanged post-BUS_RETURN parser/RX-drop counters. All one-shot latches close before DE is enabled.

After the single `0492` ACK:
- no `04A6` ACK;
- no later FC16 ACK;
- no FC03/mailbox response;
- first different FC16 or any FC03 is captured and the experiment stops;
- 15 s capture timeout if no different stage appears.

Known side effect remains the reproducible DHW-side literal `0`, often followed by `COMM. ERR ONLINE/LINK`, after deliberately incomplete sessions. Recovery is one normal Thermia-controller reboot after summary.

### Build validation

- YAML syntax parsed successfully with ESPHome custom tags tolerated.
- `${device_name}` and `${friendly_name}` are the only substitutions referenced and both are defined.
- All YAML IDs are unique and all `id(...)` references resolve.
- Exactly ten DE-enable/UART TX paths exist: R1 plus nine exact FC16 ACKs through `0492`.
- All nine FC16 ACK CRCs validate.
- CRC-valid-frame bus-health bookkeeping remains present.
- ESPHome compile was **not run** because the ESPHome CLI is unavailable.

---


## Authoritative current state — 2026-09-27 — EXP260 COMPLETE / STRONG POSITIVE

- Last completed experiment: **EXP260 — COMPLETE / STRONG POSITIVE**.
- Hypothesis: continue the proven local Online/Link prefix with a bounded three-block ACK batch `042E/15 -> 0442/13 -> 0456/12`, then capture only. Genuine Eco 5 predicts `046A/count18` next.
- Observed local sequence: `R1 -> 03E8/14 ACK -> 03FC/11 ACK -> 0410/22 ACK -> 042E/15 ACK -> 0442/13 ACK -> 0456/12 ACK -> 046A/18`.
- Timing after previous ACK: `042E` +695 ms after `0410` ACK; `0442` +1502 ms after `042E` ACK; `0456` +566 ms after `0442` ACK; `046A` +1473 ms after `0456` ACK.
- `046A/count18` was captured and **not acknowledged**.
- Integrity: approval retries after R1=0; all same-block retry counters=0; no unexpected peer FC17/FC16 ACK; post-return parser-resync delta=0; RX-drop delta=0; DE LOW at summary.
- User reports the DHW-side literal **`0` appeared again** during/after EXP260. `COMM. ERR ONLINE/LINK` has not yet been reported for this run. Do not wait for the alarm; recovery remains one normal controller reboot after the summary.
- Strong conclusion: the local XTR now matches the genuine Eco 5 ordered Online/Link sync through `046A/count18`. The bounded batch method worked without losing causal order.
- Full Online/Link session establishment remains unproven.
- No next experiment is prepared yet.
- **EXP239 remains OPEN. EXP238 remains PARKED / NOT RUN.**

## Authoritative current state — 2026-09-27 — EXP259 COMPLETE / EXP260 PREPARED / NOT RUN

- Last completed experiment: **EXP259 — COMPLETE / STRONG POSITIVE**.
- EXP259 reproduced the genuine Eco 5 ordered prefix through `042E/count15`; user confirmed DHW-side `0` and `COMM. ERR ONLINE/LINK` again after the deliberately incomplete session.
- Current prepared experiment: **EXP260 — bounded three-block sync batch — PREPARED / NOT RUN**.
- **Hypothesis:** after the proven local prefix `R1 -> 03E8/14 ACK -> 03FC/11 ACK -> 0410/22 ACK -> 042E/15`, acknowledging the next three exact genuine-Eco5 blocks `042E/15`, `0442/13`, and `0456/12` in order will advance the XTR to `046A/count18`.
- **Only new experimental variable family:** a bounded batch of three exact standard FC16 ACKs for those already-observed reference stages.
- Maximum experimental TX: **7 frames** total: R1 + proven ACKs `03E8`, `03FC`, `0410` + new batch ACKs `042E`, `0442`, `0456`.
- Fail-closed: every stage must be the first exact expected block, within 5 s, parser/drop clean, with no approval retry, previous-page retry, FC03, unexpected peer FC17, or unexpected peer FC16 ACK.
- After the one `0456/count12` ACK, capture only. Genuine Eco 5 predicts `046A/count18`; **do not ACK `046A`**.
- No FC03/mailbox response and no downstream full-chain emulation in EXP260.
- Known side effect remains DHW-side `0` + `COMM. ERR ONLINE/LINK`; one normal controller reboot is required after summary.
- Run only after the prior alarm and DHW-side `0` have cleared following recovery reboot.
- **EXP239 remains OPEN. EXP238 remains PARKED / NOT RUN.**

### EXP260 exact new ACK frames

- `042E/count15`: `0F 10 04 2E 00 0F E0 1A` (CRC `0x1AE0`, wire `E0 1A`)
- `0442/count13`: `0F 10 04 42 00 0D A1 C6` (CRC `0xC6A1`, wire `A1 C6`)
- `0456/count12`: `0F 10 04 56 00 0C 20 02` (CRC `0x0220`, wire `20 02`)

### Build validation

- YAML syntax parsed successfully with ESPHome custom tags tolerated.
- Only `${device_name}` and `${friendly_name}` are referenced and both are defined.
- All YAML IDs are unique and every `id(...)` reference resolves.
- Exactly seven UART TX / DE-enable paths exist.
- CRC-valid-frame bus-health bookkeeping remains present.
- ESPHome compile was **not run** because the ESPHome CLI is unavailable in this environment.

---

## EXP259 UI side-effect confirmation — 2026-09-27

- EXP259 is **COMPLETE / STRONG POSITIVE**.
- User confirmed the same front-panel side effects again after the incomplete active Online/Link session:
  - DHW-side literal `0`;
  - exact alarm `COMM. ERR ONLINE/LINK`.
- This repeats the EXP252/EXP256 failure mode while the controller is progressively serviced farther into the genuine Online/Link FC16 sync chain.
- Strong conclusion: the visible side effect is reproducibly associated with entering the Online/Link session and then leaving it incompletely serviced.
- Hypothesis, still not formally proven: the alarm is the controller timing out an approved but incompletely serviced Online/Link session.
- Recovery remains one normal Thermia-controller reboot before any further active test.
- To keep the remaining reboot count practical, future experiments may acknowledge small, pre-verified batches of the genuine Eco 5 FC16 sequence, with fail-closed stop on the first unexpected block. Do not jump directly to full-chain/mailbox emulation.

## Authoritative current state — 2026-09-27 — EXP259 COMPLETE / STRONG POSITIVE

- Last completed experiment: **EXP259 — COMPLETE / STRONG POSITIVE**.
- **EXP239 remains OPEN.**
- **EXP238 remains PARKED / NOT RUN.**
- No next experiment is prepared yet.

### EXP259 hypothesis

After the locally proven chain `R1 -> 03E8/count14 ACK -> 03FC/count11 ACK -> 0410/count22`, send exactly one standard FC16 ACK for the first exact `0410/count22` block, then capture the first different FC16/FC03 stage without answering it. The genuine Eco 5 reference predicted `042E/count15`.

### EXP259 observed result

Observed sequence:
- BUS_RETURN
- first approval at +1283 ms
- R1 sent once
- `03E8/count14` at +138 ms after R1; ACKed once
- `03FC/count11` at +682 ms after 03E8 ACK; ACKed once
- `0410/count22` at +1498 ms after 03FC ACK; ACKed once
- `042E/count15` at +696 ms after 0410 ACK
- `042E` was **not** acknowledged

Exact first different request:
`0F10042E000F1E000100010000000AFFF60005001E0000002D0000000000000000000000003A99`

Decoded header:
- slave `0x0F`
- FC16
- start `0x042E`
- count `15`
- bytecount `30`

Payload words:
`0001 0001 0000 000A FFF6 0005 001E 0000 002D 0000 0000 0000 0000 0000 0000`

Safety/integrity summary:
- R1 used: 1
- 03E8 ACK: 1
- 03FC ACK: 1
- 0410 ACK: 1
- approval retries after R1: 0
- 03E8 retries after ACK: 0
- 03FC retries after ACK: 0
- 0410 retries after ACK: 0
- unexpected peer frames: 0
- post-return parser resync delta: 0
- post-return RX-drop delta: 0
- DE LOW
- no FC03/mailbox response
- no ACK beyond `0410`

### Strong conclusion

The local XTR now reproduces the genuine Eco 5 ordered Online/Link synchronization prefix through four consecutive FC16 pages:

`approval response -> 03E8/14 -> ACK -> 03FC/11 -> ACK -> 0410/22 -> ACK -> 042E/15`

This is the third consecutive bounded positive progression after EXP256–258 and strongly supports that the replayed R1 enters the native Online/Link synchronization state machine.

Full Online/Link establishment remains unproven because `042E` and all later blocks/mailbox traffic were deliberately left unanswered.

### UI / recovery

The EXP259 log itself does not report the front-panel UI. As with EXP252/256/258, an incomplete approved session may again lead to DHW-side `0` and/or `COMM. ERR ONLINE/LINK`; exact EXP259 UI outcome awaits user confirmation. Perform one normal Thermia-controller reboot after this run.

---

## Authoritative current state — 2026-09-27 — EXP258 COMPLETE / EXP259 PREPARED / NOT RUN

- Last completed experiment: **EXP258 — COMPLETE / STRONG POSITIVE**.
- Current prepared experiment: **EXP259 — R1 + exact `03E8/count14` ACK + exact `03FC/count11` ACK + exact `0410/count22` ACK + next-stage capture — PREPARED / NOT RUN**.
- **EXP239 remains OPEN.**
- **EXP238 remains PARKED / NOT RUN.**

### EXP259 hypothesis

EXP258 locally proved the ordered prefix `R1 -> 03E8/14 ACK -> 03FC/11 ACK -> 0410/22`. EXP259 changes one active variable only: acknowledge that already-proven exact `0410/count22` request once, then capture the first different FC16/FC03 stage without answering it. The genuine Eco 5 reference predicts `042E/count15` next.

### Exact new active target

- Required request: slave `0x0F`, FC16, start `0x0410`, count `22` (`0x0016`), bytecount `44` (`0x2C`), full request length `53` bytes.
- Exact standard FC16 ACK: `0F 10 04 10 00 16 40 1C`.
- CRC16 over `0F1004100016` is `0x1C40`, transmitted little-endian `40 1C`.
- The ACK carries no register-value payload; it echoes only start/count.

### EXP259 fail-closed boundary

Maximum experimental TX is four frames: one R1, one exact `03E8/14` ACK, one exact `03FC/11` ACK and one exact `0410/22` ACK. The new `0410` ACK is allowed only after the proven prefix, only when the first post-`03FC`-ACK FC16 is exact `0410/22`, within 5 s, with unchanged parser/drop counters, no approval/03E8/03FC retry, and no unexpected peer frame. All one-shot latches close before DE is enabled.

After the one `0410` ACK:
- no second `0410` ACK;
- no ACK of `042E` or any later FC16;
- no FC03/mailbox response;
- first different FC16 or any FC03 is captured and the experiment stops;
- 15 s timeout if only `0410` retries continue.

Known reproducible side effect remains the DHW-side `0` plus `COMM. ERR ONLINE/LINK` after an incomplete approved Online/Link session. **Do not run EXP259 until one normal controller reboot has cleared both after EXP258.** After EXP259 summary, reboot the Thermia controller once again.

### Build validation

- YAML syntax parsed successfully with ESPHome custom tags tolerated.
- `${device_name}` and `${friendly_name}` are the only substitutions referenced and both are defined.
- All 138 YAML IDs are unique and all `id(...)` references resolve.
- Exactly four DE-enable / UART TX call sites exist: R1, `03E8` ACK, `03FC` ACK, `0410` ACK.
- CRC-valid-frame bus-health bookkeeping is unchanged.
- ESPHome compile was **not run** because the ESPHome CLI is not installed in the available environment.

---


## Authoritative current state — 2026-09-27 — EXP258 COMPLETE / STRONG POSITIVE

- Last completed experiment: **EXP258 — COMPLETE / STRONG POSITIVE**.
- No next experiment is yet prepared.
- **EXP239 remains OPEN.**
- **EXP238 remains PARKED / NOT RUN.**

### EXP258 hypothesis

After the already-proven local prefix `R1 -> 03E8/count14 -> ACK -> 03FC/count11`, acknowledge exactly the first `03FC/count11` FC16 request once and capture the first different FC16/FC03 stage without answering it. Genuine Eco 5 reference predicts `0410/count22`.

### EXP258 observed facts

- BUS_RETURN occurred after the controller power-cycle; two parser resync events happened exactly at the return edge, while the experiment summary recorded `resync_postreturn=0` and `drop_postreturn=0`.
- First approval request: **+1243 ms after BUS_RETURN**.
- R1 sent exactly once; no approval retry after R1.
- First post-R1 `03E8/count14`: **+138 ms after R1**.
- Exact `03E8/count14` ACK sent once: `0F 10 03 E8 00 0E C0 93`.
- First post-03E8-ACK block: exact `03FC/count11` at **+691 ms**.
- Exact `03FC/count11` ACK sent once: `0F 10 03 FC 00 0B 40 94`.
- First post-03FC-ACK different block: exact **`0410/count22` at +1501 ms**.
- `0410/count22` was captured and **not acknowledged**.
- Summary: `r1=1 ack03e8=1 ack03fc=1 approvals=1 approval_after_r1=0 post_r1_fc16=1 post_03e8_fc16=1 same03e8_after_ack=0 same03fc_after_ack=0 peer17=0 unexpected_peer_ack=0 self_echo_r1=0 self_echo_ack=0 resync_postreturn=0 drop_postreturn=0 DE=LOW`.
- User reports the DHW/tank-side literal **`0` reappeared** and the same **`COMM. ERR ONLINE/LINK`** alarm appeared again.

Exact captured `0410/count22` request:

`0F10041000162C0028000A0037000000000000000200120028001E003C00120014002F001E00070000003C000D00060037000088E3`

### Strong conclusions

- EXP258 locally reproduces the genuine Eco 5 synchronization prefix one step further: `R1 -> 03E8/14 -> ACK -> 03FC/11 -> ACK -> 0410/22`.
- The Eco 5 prediction for the third ordered sync block is therefore confirmed on the XTR.
- The replayed R1 is sufficient to move the XTR through at least the first three native Online/Link synchronization stages when the expected FC16 ACKs are supplied.
- The repeated DHW-side `0` + exact `COMM. ERR ONLINE/LINK` after EXP252/256/258 remains consistent with an approved but incompletely serviced Online/Link session timing out; this causal explanation is now stronger but still not proven.

### Unknowns / safety

- Full Online/Link establishment is still unproven.
- `0410/count22` and all later FC16 pages remain unacknowledged locally.
- No local `0708/count6` mailbox response has been provided.
- Do not broaden directly to full-chain ACK + mailbox emulation in one step.
- Recovery after EXP258 remains one normal controller reboot; confirm the `0` and alarm clear before another active test.

---

## Authoritative current state — 2026-09-27 — EXP257 COMPLETE / EXP258 PREPARED / NOT RUN

- Last completed experiment: **EXP257 — COMPLETE / STRONG POSITIVE**.
- Current prepared experiment: **EXP258 — R1 + exact `03E8/count14` ACK + exact `03FC/count11` ACK + next-stage capture — PREPARED / NOT RUN**.
- **EXP239 remains OPEN.**
- **EXP238 remains PARKED / NOT RUN.**

### EXP258 hypothesis

EXP257 locally proved `R1 -> 03E8/count14 -> ACK -> 03FC/count11`. EXP258 changes one active variable only: acknowledge that already-proven exact `03FC/count11` request once, then capture the first different FC16/FC03 stage without answering it. The genuine Eco 5 reference predicts `0410/count22` next.

### Exact new active target

- Required request: slave `0x0F`, FC16, start `0x03FC`, count `11` (`0x000B`), bytecount `22` (`0x16`), full request length `31` bytes.
- Exact standard FC16 ACK: `0F 10 03 FC 00 0B 40 94`.
- CRC16 over `0F1003FC000B` is `0x9440`, transmitted little-endian `40 94`.
- The ACK carries no register-value payload; it echoes only start/count.
- The same ACK frame is present in the genuine Eco 5 raw capture.

### EXP258 fail-closed boundary

Maximum experimental TX is three frames: one R1, one exact `03E8/count14` ACK, one exact `03FC/count11` ACK. The new `03FC` ACK is allowed only after the proven prefix, only when the first post-`03E8`-ACK FC16 is exact `03FC/11`, within 5 s, with unchanged parser/drop counters, no approval retry, no `03E8` retry, and no unexpected peer frame. All one-shot latches close before DE is enabled.

After the one `03FC` ACK:
- no second `03FC` ACK;
- no ACK of `0410` or any later FC16;
- no FC03/mailbox response;
- first different FC16 or any FC03 is captured and the experiment stops;
- 15 s timeout if only `03FC` retries continue.

Known possible side effect remains an incomplete Online/Link session with DHW-side `0` and/or `COMM. ERR ONLINE/LINK`; recovery is one normal Thermia-controller reboot after the summary.

### Build validation

- YAML syntax parsed successfully with ESPHome custom tags tolerated.
- `${device_name}` and `${friendly_name}` are the only substitutions referenced and both are defined.
- All `id(...)` references resolve to defined YAML IDs; no duplicate IDs found.
- Exactly three DE-enable / UART TX call sites exist: R1, `03E8` ACK, `03FC` ACK.
- CRC-valid-frame bus-health bookkeeping remains present and unchanged.
- ESPHome compile was **not run** because the ESPHome CLI is not installed in the available environment.

---

## External Eco 5 follow-up after EXP257 — 2026-09-27

The new public-comment analysis has been cross-checked against the full raw Eco 5 capture. It materially refines the reference behavior but does not change the EXP257 result.

Observed from the raw capture:
- three cold-start approval windows begin with the first `071C/0730` request at **+1.199 s, +1.202 s, and +1.210 s** after bus return; this matches the local XTR EXP248/249/256/257 ~+1.28 s startup phase closely;
- with the genuine gateway attached, the two successful approval responses occur at **+120.153 s** and **+119.808 s** after bus return, after 29 challenge requests each;
- the no-gateway middle run was power-cycled after only ~174 s, with 41 unanswered challenges through +171.230 s, so it cannot test the local ~267 s / 63-request natural stop;
- the already-running steady-state segment before the first power-off contains no `071C/0730` traffic, so absence in steady-state captures does not prove a model lacks the cold-start approval stream;
- only two answered challenges exist, so challenge-repeat determinism and response stability across power cycles remain **unknown**; the one duplicated challenge in the capture was unanswered.

### Gateway behavior after approval

The genuine Eco 5 endpoint ACKs the controller's FC16 transfer blocks and the stable prefix is:

`03E8/14 -> ACK -> 03FC/11 -> ACK -> 0410/22 -> ACK -> 042E/15 -> ...`

The broad controller-export sequence then continues through the known 0x03E8..0x0864 range. `04A6/13` and `085F/5` are recurrent passive families overlaid on that transfer; their ACK timing differs between power-ups and they are **not supported as approval preconditions**. Do not treat their interleaving position as a required ordered sync step.

The first `0708/count6` mailbox poll occurs while the FC16 transfer is still in progress:
- first successful power-up: **+158.393 s** after bus return; the first poll is unanswered, the next poll is answered;
- second successful power-up: **+186.828 s** after bus return and is answered immediately.

**Raw-frame correction:** the repeated post-approval idle mailbox response in the public capture is `0F 03 0C 0000 0000 0000 0000 0001 0000 ...`, i.e. six Modbus words `0000 0000 0000 0000 0001 0000`. A comment transcribed the fifth word as `0100`; the raw bytes support `0001` in standard Modbus register order.

Later in the second successful session the fifth mailbox word is observed at `03DC` (988), then 984, 976, 908, 896, 768, 512, and finally 0. This is an **observed countdown-like sequence**. Interpreting it as pending sync-item count remains a hypothesis.

### Next bounded candidate

**EXP258 — candidate / NOT PREPARED.** Hypothesis: after the already-proven `R1 -> 03E8/14 ACK -> 03FC/11`, one exact standard ACK to the first local `03FC/count11` should advance the XTR to `0410/count22`, matching both successful genuine Eco 5 sessions. Stop on the first different block and do not ACK `0410`.

Do **not** jump directly to ACKing the entire chain or answering `0708`; that would change multiple active variables at once and would lose the clean discriminator established by EXP256-257.


## Authoritative current state — 2026-09-27 — EXP257 COMPLETE / STRONG POSITIVE

- Last completed experiment: **EXP257 — COMPLETE / STRONG POSITIVE**.
- **EXP239 remains OPEN.**
- **EXP238 remains PARKED / NOT RUN.**
- No next experiment is yet authorized/prepared.

### EXP257 hypothesis

After the same guarded one-shot R1 used in EXP256, acknowledge exactly the **first** post-R1 `0x0F FC16 03E8/count14` request once. Then observe the first different `0x0F` FC16/FC03 stage without answering it.

The full genuine Eco 5 gateway capture predicted `03FC/count11` as the immediate next stage.

### EXP257 observed result

The complete experiment sequence was:

```text
BUS_RETURN
  -> +1285 ms approval request 071C/0730
  -> R1 sent once
  -> +130 ms first post-R1 FC16 03E8/count14
  -> one exact FC16 ACK 0F1003E8000EC093
  -> +691 ms first different post-ACK block FC16 03FC/count11
  -> NO ACK
  -> SUMMARY NEXT_STAGE_FC16
```

Exact first different request:

`0F1003FC000B160028000A0037000000000000000200120028001E003C369E`

Decoded FC16 header:
- slave `0x0F`
- function `0x10`
- start `0x03FC`
- count `11`
- bytecount `22`

Payload words:
`0028 000A 0037 0000 0000 0000 0002 0012 0028 001E 003C`

Safety/integrity summary:
- R1 used: `1`
- one `03E8` ACK used: `1`
- approvals: `1`
- approval retries after R1: `0`
- same-`03E8` retries after ACK: `0`
- unexpected peer FC17: `0`
- unexpected peer FC16 ACK: `0`
- self echo R1/ACK: `0/0`
- post-return parser resync delta: `0`
- post-return RX-drop delta: `0`
- DE returned LOW
- `03FC/count11` was **not acknowledged**

### Strong conclusion

EXP257 reproduces the same post-approval synchronization prefix as the genuine Eco 5 reference:

`approval response -> 03E8/count14 -> ACK -> 03FC/count11`

This is a second independent XTR-to-Eco5 architecture match after EXP256 first established `approval response -> 03E8/count14`.

The result strongly supports that the replayed R1 is sufficient to advance the local XTR through at least the first two native controller->Online/Link synchronization stages. It still does **not** prove full Online/Link session establishment, because `03FC` and all downstream stages/mailbox traffic were deliberately left unanswered.

### Comparison with genuine Eco 5

The full Eco 5 capture shows the same prefix twice, then continues:

`03E8/14 -> ACK -> 03FC/11 -> ACK -> 0410/22 -> ...`

EXP257 stopped exactly at `03FC/11`, as intended. Therefore the next protocol question is whether acknowledging this exact `03FC/count11` on the XTR yields `0410/count22`, but no such next experiment has yet been run or authorized.

### UI / recovery status

The protocol objective is complete from the supplied log. Front-panel side effects for this run have not yet been reported. Because EXP252/EXP256 showed the recoverable DHW-side `0` / `COMM. ERR ONLINE/LINK` failure mode after incomplete Online/Link participation, perform one normal controller reboot after this EXP257 capture if not already done.

## Authoritative current state — 2026-09-27 — EXP256 COMPLETE / EXP257 PREPARED / NOT RUN

- Last completed experiment: **EXP256 — COMPLETE / ACTIVE STRONG POSITIVE**.
- Current prepared experiment: **EXP257 — ONE-SHOT R1 + SINGLE `03E8/count14` ACK + NEXT-STAGE CAPTURE — PREPARED / NOT RUN**.
- **EXP239 remains OPEN.**
- **EXP238 remains PARKED / NOT RUN.**

### EXP257 hypothesis

EXP256 proved the sequence `071C/0730 approval -> one R1 -> approval retries stop -> FC16 03E8/count14 repeats`. EXP257 changes one variable only: after the same guarded one-shot R1, send **one standard FC16 ACK** to the first exact post-R1 `03E8/count14` request, then observe the first different FC16/FC03 stage without answering it.

The complete genuine Eco 5 capture now makes `03FC/count11` the external-reference prediction for the immediate next stage after the `03E8/count14` ACK. Prior local EXP137 evidence still shows `0410/count22` later in progression; EXP257 does not require or ACK either block.

### New active target and known effects

- Required request: slave `0x0F`, FC16, start `0x03E8`, count `14`, bytecount `28`, length `37`.
- Single ACK frame: `0F 10 03 E8 00 0E C0 93`.
- The ACK echoes only address/count and contains **no register-value payload**.
- CRC16 over `0F1003E8000E` is `0x93C0`, transmitted little-endian `C0 93`.
- Genuine Eco 5 full capture shows `03E8/14 ACK -> 03FC/11 -> 0410/22` in two independent successful approval cycles.
- EXP137 previously showed locally that ACKing exact `03E8/count14` reaches `0410/count22`, but did not prove there was no intervening `03FC/11`.
- Possible side effect remains an incomplete Online/Link session with DHW-side `0` and later `COMM. ERR ONLINE/LINK`; recovery is one normal controller reboot.

### EXP257 fail-closed boundary

The `03E8` ACK is permitted only when R1 has already been sent once, there was no approval retry, the **first** post-R1 FC16 is exact `03E8/14/bytecount28/len37`, it arrives within 5 s of R1, parser/drop counters remain unchanged since BUS_RETURN, and no unexpected peer FC17/FC16 ACK was observed. The ACK latch closes before DE is enabled.

After that one ACK:
- no second `03E8` ACK;
- no ACK for `03FC`, `0410`, or any other FC16;
- no FC03/mailbox/desired-state response;
- first different FC16 or any FC03 is captured and the experiment stops;
- otherwise a 15 s post-ACK timeout records a negative result.

### Run prerequisite and recovery

Do not run EXP257 until the controller has recovered from EXP256: `COMM. ERR ONLINE/LINK` absent, DHW-side `0` cleared, then healthy normal traffic for at least 15 s. After EXP257 capture/summary, perform one normal controller reboot immediately.

### Build validation

- YAML syntax parsed successfully with ESPHome custom tags tolerated.
- `${device_name}` and `${friendly_name}` are the only substitutions referenced and both are defined.
- All 124 `id(...)` references have matching YAML `id:` definitions.
- Only two DE-enable TX call sites exist: one R1 script and one exact `03E8` ACK script.
- CRC-valid-frame bus-health bookkeeping is unchanged.
- ESPHome compile was **not run** because the ESPHome CLI is not installed in the available environment.

## External Eco 5 full-capture refinement — 2026-09-27 — BEFORE EXP257

The complete genuine iTec Eco 5 gateway capture materially sharpens the expected post-approval state machine without changing the bounded EXP257 TX plan.

Observed across the 1482.480 s capture:
- 99 exact `0x0F FC17 read 0730/count8 + write 071C/count8` approval requests occurred in three retry windows: 29 requests (`184.661..303.554 s`), 41 requests (`394.976..565.004 s`), and 29 requests (`604.688..723.223 s`).
- Median retry cadence in those windows is approximately 4.24 s / 4.26 s / 4.21 s.
- 98/99 16-byte `071C` payloads are unique; one payload repeats once. Therefore the genuine Eco 5 challenge value is normally regenerated between retries rather than held constant.
- Successful pair 1 is directly present in the raw capture: `C1=63CEFB32C6F41382087992370CACEEBA` -> `R1=1691A5F3F8E8D58738924416E8E6A3D5`.
- Successful pair 2 is also directly present: `C2=31FB59FC8FB1175CD89F904D06D92EA4` -> `R2=FD636CCD0F921D83FF232A1A2413B372`.

Both successful responses are followed by the same acknowledged sync prefix:

```text
FC17 response
  -> +92 ms  FC16 03E8/count14
  -> ACK 03E8/count14
  -> FC16 03FC/count11
  -> ACK 03FC/count11
  -> FC16 0410/count22
  -> ACK 0410/count22
  -> ... broader ordered sync ...
```

Timing is highly reproducible:
- R1 cycle: `03E8` at +92 ms, ACK at +137 ms, `03FC` at +510 ms, `0410` at +1.950 s.
- R2 cycle: `03E8` at +92 ms, ACK at +122 ms, `03FC` at +536 ms, `0410` at +2.189 s.

The first successful cycle then progresses through the ordered controller-export chain:

`03E8/14 -> 03FC/11 -> 0410/22 -> 042E/15 -> 0442/13 -> 0456/12 -> 046A/18 -> 047E/19 -> 0492/11 -> 04A6/13 -> 04BA/22 -> 04D8/27 -> 04F6/14 -> 050A/19 -> 051E/10 -> 0532/18 -> 0546/20 -> 055A/33 -> 057B/33 -> 059C/33 -> 05BD/33 -> 05DE/33 -> 05FF/33 -> 0620/33 -> 0641/33 -> 0662/33 -> 0683/33 -> 06A4/33 -> 06C5/33 -> 06EA/7 -> 06F1/3 -> 06F4/19`, followed by `07D0/19` and the `0708/count6` mailbox/runtime phase.

**EXP257 consequence:** the external Eco 5 reference now predicts `03FC/count11` as the immediate next block after the single `03E8/count14` ACK. Prior local EXP137 evidence still records that `0410/count22` appears after a `03E8` ACK, but did not establish that it is the first intervening block. EXP257 remains necessary to determine the local XTR ordering. Its active behavior does not need to broaden: ACK only `03E8` once, capture the first different block, and stop.

## Authoritative current state — 2026-09-27 — EXP256 COMPLETE / ACTIVE STRONG POSITIVE

- Last completed experiment: **EXP256 — COMPLETE / ACTIVE STRONG POSITIVE**.
- Hypothesis tested: repeat the already-tested one-shot Eco 5 R1 response and enumerate the complete local post-R1 `0x0F FC16/FC03` distribution.
- One exact R1 response was transmitted at the first local approval request, **+1245 ms after BUS_RETURN**.
- Approval requests: **1 total; 0 retries after TX**.
- User-reported front-panel effect: the DHW/tank-side literal **`0` reappeared**; the VERSION screen showed **no change**.
- After `SUMMARY COMPLETE`, the front panel again raised the exact same alarm as EXP252: **`COMM. ERR ONLINE/LINK`**. This makes the incomplete Online/Link-session side effect reproducible across both R1 runs.
- No downstream emulation was provided: **0 FC16 ACKs, 0 FC03 responses, 0 second FC17 response**.

### EXP256 definitive post-R1 census

- `FC16 requests = 390`
- `FC16 ACKs = 0`
- `FC03 0708/count6 = 0`
- other `FC03 = 0`
- `peer17 = 0`
- `self_echo = 0`
- `s06 = 102`
- final state: `A80E=0028 A80F=000A AFDC=0010`
- post-BUS_RETURN parser resync delta: **0**
- post-BUS_RETURN RX drop delta: **0**
- DE returned LOW.

Complete FC16 family census in the EXP256 run:
- `04BA/count22`: **1** request, boot-only, before R1;
- `03E8/count14`: **389** requests, first **+1369 ms after BUS_RETURN / +124 ms after R1**, last **+419896 ms**, median inter-request interval about **1308 ms**;
- `04A6/count13`: **0**;
- `085F/count5`: **0**;
- no other FC16 family observed.

### Material protocol conclusion from EXP256

The EXP255-derived numerical hypothesis that R1 might merely suppress `085F/count5` while leaving `04A6/count13` intact is **rejected**. The earlier 582-vs-386 count coincidence was misleading.

R1 instead causes a much stronger state transition: immediately after the one-shot response, the controller enters the native `03E8/count14` FC16 synchronization stage and retransmits that first settings block continuously because EXP256 deliberately supplies no FC16 ACK. This reproduces the beginning of the acknowledged `0x0F` transfer state machine previously mapped in EXP137+, but now specifically **after the approval response**.

Therefore the strongest current interpretation is:
1. the R1 response is accepted far enough to terminate the `071C/0730` approval retry loop;
2. it advances the local XTR into a controller->Online/Link synchronization phase beginning at `03E8/count14`;
3. without the expected endpoint FC16 ACK, the controller stalls on that first synchronization block;
4. full Online/Link session establishment is still not proven; no FC03/mailbox phase was reached in EXP256.

The lack of VERSION-screen change is expected and not a negative discriminator: VERSION `EXP` metadata is the separate `0x06/AFD1` expansion-board path, while EXP256 acts only on the `0x0F` approval path.

### Safety / recovery after EXP256

The known R1 side effect is reproducible at least at the UI level (`0` at the DHW/tank icon). As planned, perform **one normal Thermia controller reboot after the EXP256 summary**. Do not run another active approval/sync experiment until the UI has returned to its normal state.

**EXP239 remains OPEN.**  
**EXP238 remains PARKED / NOT RUN.**

Next active candidate is not yet prepared. The highest-value controlled discriminator is likely a bounded post-R1 ACK of the already-proven exact `03E8/count14` FC16 request, with no ACK of any newly appearing block, to determine the first post-approval progression. This must be prepared as a separate experiment with explicit fail-closed guards.

## Authoritative current state — 2026-09-27 — EXP255 COMPLETE / EXP256 PREPARED

- Last completed experiment: **EXP255 — COMPLETE / VALID PASSIVE BASELINE**.
- Current prepared experiment: **EXP256 — ONE-SHOT R1 + FULL POST-R1 FC16/FC03 DIFFERENTIAL CENSUS — PREPARED / NOT RUN**.

### EXP255 definitive passive baseline

- approval requests: **63**
- first approval: **+1284 ms**
- last approval: **+265513 ms**
- median approval cadence: **4241 ms**
- FC16 requests: **582**
- FC16 ACKs: **0**
- FC03 requests: **0**
- FC03 responses: **0**
- parser resync delta: **0**
- RX drop delta: **0**
- TX disabled

Complete local passive FC16 families:
- `04BA/count22`: **4**, boot-only (+316..+3641 ms)
- `04A6/count13`: **383**, persistent (+4337..+419417 ms)
- `085F/count5`: **195**, persistent (+2265..+419542 ms)

No other 0x0F FC16 family and no FC03 request appears in the full seven-minute run.

The FC16 streams continue after the 63rd/final approval request: 219 FC16 requests occur after
+265513 ms, proving that normal FC16 runtime traffic is separate from the approval retry budget.

### New EXP252 / EXP255 differential hypothesis

EXP252 one-shot R1 had `fc16req=386` over the same seven-minute observation window.
EXP255 passive baseline has 582, a difference of **196**.

EXP255's `085F/count5` family alone contributes **195** requests. The remaining passive families
contribute **387**, almost exactly EXP252's 386 total.

This supports, but does not yet prove, the hypothesis that R1 selectively suppresses the normal
`085F/count5` family while leaving `04A6/count13` largely intact.

### EXP256 hypothesis

Repeat the already-tested EXP252 one-shot R1 response with the same fail-closed guards while logging
every FC16 and FC03 address/count. No downstream ACK or response is added.

Primary discriminator:
- disappearance/reduction of `085F/count5`;
- persistence of `04A6/count13`;
- or appearance of any new FC16/FC03 family.

Known recoverable side effect:
- previous R1 produced DHW-side `0` and `COMM. ERR ONLINE/LINK`;
- one normal controller reboot cleared both.
- EXP256 should be followed by one controller reboot immediately after its summary; do not wait for
  the communication alarm.

**EXP239 remains OPEN.**
**EXP238 remains PARKED / NOT RUN.**



## Authoritative current state — 2026-09-27 — EXP255 PREPARED / NOT RUN

- Last completed experiment: **EXP254 — COMPLETE / VALID PASSIVE POSITIVE**.
- Recovery confirmation from the user:
  - after the manual controller restart following EXP252,
  - `COMM. ERR ONLINE/LINK` cleared,
  - the DHW/tank-side `0` also cleared.
- Therefore EXP252 side effects were **recoverable by one normal controller reboot with no active
  responder**. Spontaneous self-clear without reboot remains untested.
- Current prepared experiment: **EXP255 — PASSIVE FULL 0x0F FC16/FC03 BASELINE CENSUS**.
- Reason for inserting EXP255 before another active R1 test:
  - EXP254 counted only exact `0870/count17` and `0708/count6`;
  - it did not map all local `0x0F FC16` and `FC03` start/count pairs;
  - without this baseline, an active post-R1 address census would be ambiguous.
- EXP255 is fully RX-only and records every `0x0F FC16` request and every `0x0F FC03` request after
  BUS_RETURN.
- Candidate after EXP255, if baseline is clean:
  **EXP256 — one-shot R1 + identical post-R1 FC16/FC03 census, no downstream ACKs/responses.**
- **EXP239 remains OPEN.**
- **EXP238 remains PARKED / NOT RUN.**


## EXP252/254 recovery clarification — 2026-09-27

The heat pump/controller was manually restarted after the `COMM. ERR ONLINE/LINK` alarm from EXP252.

Therefore EXP254 demonstrates **post-reboot recovery to the normal local XTR protocol baseline**.
It does **not** demonstrate that the alarm/session state would have cleared spontaneously without a
controller restart.

The following remain valid:
- EXP252 R1 suppressed all later approval retries in that boot;
- a DHW-side `0` appeared;
- `COMM. ERR ONLINE/LINK` appeared;
- after a subsequent controller restart with no active responder, EXP254 returned to the familiar
  63-request passive approval lifecycle with no `0870/count17` and no `0708/count6`.

UI recovery of the alarm and DHW-side `0` still requires explicit visual confirmation if it was not
recorded at the time.


## Authoritative current state — 2026-09-27 — EXP254 COMPLETE / VALID PASSIVE POSITIVE

- Last completed experiment: **EXP254 — COMPLETE / VALID PASSIVE POSITIVE**.
- EXP254 clean passive recovery summary:
  - approval requests: **63**
  - first request: **+1.283 s**
  - median cadence: **4.241 s**
  - last request: **+265.086 s**
  - exact `FC16 0870/count17`: **0**
  - peer FC16 ACK: **0**
  - exact `FC03 0708/count6`: **0**
  - `s06=107`
  - final state `A80E=0028 A80F=000A AFDC=0010`
  - `resync_delta=0`
  - `drop_delta=0`
  - TX disabled
- All complete passive retry runs (EXP248, 249, 251, 254) stop at exactly **63 requests**, despite
  differing cadence and elapsed duration. The fixed 63-attempt budget remains the leading model.
- With EXP254 median cadence, a nominal 64th request would fall around +269.327 s, before +270 s,
  but does not appear.
- **Material refinement of EXP252 interpretation:** the late A80E/AFDC fall-back is not R1-specific.
  EXP254 reproduces it passively at almost the same boot age:
  - A80E `0x28 -> 0x20` at ~+642.650 s in EXP254 vs ~+647.433 s in EXP252
  - AFDC `0x10 -> 0x00` at ~+646.459 s in EXP254 vs ~+651.106 s in EXP252
- Therefore the R1-specific evidence from EXP252 is now narrowed to:
  1. immediate suppression of all later approval retries;
  2. front-panel DHW-side `0`;
  3. `COMM. ERR ONLINE/LINK`.
- Exact `0870/count17` and `0708/count6` do not occur in the 7-minute local passive XTR baseline.
  Do not copy the reference ATEC/DHP-AQ `0870 -> 0708 -> sync` sequence onto XTR without direct
  local evidence.
- Next candidate: **EXP255 — one-shot R1 + post-R1 FC16/FC03 address census, no downstream ACKs**.
- Safety prerequisite before EXP255: user confirms that `COMM. ERR ONLINE/LINK` and the DHW-side `0`
  cleared after the EXP254 passive recovery reboot.
- **EXP239 remains OPEN.**
- **EXP238 remains PARKED / NOT RUN.**


## EXP254 provisional live result — 2026-09-27 — RUNNING

- EXP254 is behaving as intended: fully passive / RX-only.
- A genuine controller-off bus gap and BUS_RETURN were observed.
- After BUS_RETURN the local XTR returned to the known unanswered approval lifecycle:
  - first `071C/0730` request at +1.283 s;
  - 23 requests observed so far through +94.787 s;
  - recent cadence ~4.240 s.
- Controller state progression returned to the familiar pattern:
  - A80E `0x28 -> 0x00 -> 0x08 -> 0x28`;
  - A80F `0x0A -> 0x05 -> 0x0A`;
  - AFDC `0x10 -> 0x00 -> 0x10`.
- So far:
  - exact `0x0F FC16 0870/count17` requests: **0**;
  - exact `0x0F FC03 0708/count6` polls: **0**;
  - peer FC16 ACKs: **0**.
- This already supports clean recovery toward the local XTR baseline and shows that the reference
  ATEC/DHP-AQ `0870/0708` service cycle is not ordinary early local XTR baseline traffic.
- EXP254 remains **RUNNING** until `SUMMARY PASSIVE_RECOVERY_COMPLETE`.


## Authoritative current state — 2026-09-27 — EXP253 COMPLETE / EXP254 PREPARED

- Last completed experiment: **EXP253 — COMPLETE / OFFLINE POST-APPROVAL SESSION RECONSTRUCTION**.
- Last completed live-bus experiment: **EXP252 — COMPLETE / ACTIVE POSITIVE / COMM. ERR ONLINE/LINK SIDE EFFECT**.
- Current prepared experiment: **EXP254 — PASSIVE RECOVERY + 0870 BASELINE CENSUS — PREPARED / NOT RUN**.

### EXP253 material finding

Reference established Online/DCM captures show a concrete endpoint-coming-online transition:

1. controller repeatedly sends `0x0F FC16 0870/count17` with no reply;
2. controller repeatedly polls `0x0F FC03 0708/count6` with no reply;
3. endpoint first ACKs `0870/count17`;
4. endpoint then answers `0708` with `0000 0000 7FFF FFFF 0080 0007`;
5. controller immediately begins a broad FC16 synchronization burst (`03E8`, `03FC`, `0884`, ...),
   with each block ACKed by the endpoint.

In capture 090550 there are 31 unanswered `0870/count17` requests and 16 unanswered `0708` polls
before this transition.

Established idle/service captures show recurring `0708` responses ending in `...0006`, including
`0000 0000 0000 0000 077F 0006` and all-zero-like variants.

### EXP252 interpretation refined

EXP252's R1 is not simply ignored: it suppresses the local approval retries. However the ESP supplied
none of the downstream endpoint duties seen in the reference topology: no FC16 ACKs and no read-side
service/mailbox responses. The later `COMM. ERR ONLINE/LINK` is therefore consistent with an
**incomplete Online/Link endpoint/session**.

This does not prove that local XTR uses the same post-approval sequence as the reference ATEC/DHP-AQ
topology.

### Safety / next step

No further active response is approved until clean passive recovery is documented.

EXP254 is fully RX-only and will establish:
- whether the alarm and DHW-side `0` clear on a normal no-responder boot;
- whether local `0870/count17` is baseline traffic;
- whether any local `0708/count6` poll occurs without active endpoint behavior;
- whether the normal 63-attempt approval lifecycle returns.

**EXP239 remains OPEN.**
**EXP238 remains PARKED / NOT RUN.**


## Authoritative current state — 2026-09-27 — EXP252 COMPLETE / ACTIVE POSITIVE / ALARM SIDE EFFECT

- Last completed experiment: **EXP252 — COMPLETE / ACTIVE POSITIVE / SAFETY SIDE EFFECT OBSERVED**.
- One mismatched externally reported Eco 5 R1 response was transmitted exactly once at the first
  local XTR `071C/0730` approval request.
- Result:
  - approval requests: **1**;
  - retries after TX: **0**;
  - no second approval request for the complete 7-minute observation;
  - `peer17=0`;
  - controller FC16 requests: **386**;
  - peer FC16 ACKs: **0**;