**2026-10-25 C5AL cold-join LIVE:** User actually runs MAIN03-C5AL (not presumed C5AK). One S92 START on already-running controller at 12:41:57 (stage40); controller offers 04A6→04BA→059C→05FF→0662 and five guarded ACKs are physically sent. Controller then only repeats zero-context 085F, with no 0683/FC03/0708 and 0/4 CURRENT; 60s timeout -> RX ONLY DE LOW. **COMPLETE / NEGATIVE** full cold join; safe expiry positive. C5AL hot-0864 ARM NOT used, hot rejoin still PREPARED / NOT RUN. NO-GO speculative 085F reply; one next action: reconcile OEM 085F/0662 continuation against XTR evidence for a real implementation fix. See Research/EXPERIMENT_LOG.md. HA parameter writes HOLD.

**2026-10-25 — CURRENT USER PRIORITY: COLD JOIN, NO HEAT-PUMP RESTART.** Previous C5AK controller cold-start restoration plan is SUPERSEDED / NOT RUN by user preference. Current warmtepomp works without DCM; next: one bounded, user-initiated **C5AK stage40 native cold join on live controller bus** with complete log, existing sole UART/DE and ABORT. C5AL is retained hot rejoin only, PREPARED / NOT RUN, not the right present entry. HA parameter writes remain ON HOLD. See Research/EXPERIMENT_LOG.md.

**2026-10-25 NEXT MILESTONE ACTION — C5AK-DCM-RESTORE-01 (PREPARED / NOT RUN):** After the locally observed C5AK ESP-only hot-rejoin failure, user confirmed expected Online-module communications alarm, manually restarted the heat pump and reports normal heat-pump operation **without DCM**. The user explicitly requests to restore DCM first using the **locally verified C5AK guarded controller cold-start path**. No C5AL hot-rejoin experiment until the user reports healthy owned RUNTIME and fresh H/D/C/M 4/4. No new firmware or HA parameter write; no autonomous flash or power cycle. Details: Research/EXPERIMENT_LOG.md.

**2026-10-25 C5AL prepared:** Exact C5AK hot-rejoin blocker addressed by PRIVATE integrated C5AL source (offline YAML and patch checked; NOT compiled/flashed/live). One user-armed, guarded controller-offered 0864→0870→0708 candidate in the existing single S92 engine, followed by one proven CURRENT 4/4 request; HA parameter writes ON HOLD. No private firmware code published. NEXT: one bounded, user-initiated C5AL-HOT-ENTRY-01 with ABORT/rollback. See Research/EXPERIMENT_LOG.md.

**25 October 2026 — current C5AK source-gate decision:** The full *manually armed controller-restart* C5AK native cold-start chain is **LIVE COMPLETE / POSITIVE** (FC23→FC16 through 06F4→FC03/0708→fresh H/D/C/M 4/4). Exact C5AK source review against genuine prior C5AB/C5AC/C5AD/C5AJ offers and original Connect (2018/2.1.105) found **no new demonstrable missed authorized controller request in the deployed ESP-boot gate**. Earlier sparse `04BA→059C` and direct `059C` entry fixes are present; `0662` ACK alone did not prove `0683` acceptance. **NO-GO speculative firmware fix.** Cold join with already-running controller and ESP-only retained hot rejoin remain OPEN. ONE NEXT ACTION: one user-initiated bounded complete first-attach cold join on unchanged C5AK, not another isolated ACK test; preserve abort/rollback and HA writes ON HOLD.

> **LATEST HANDOFF — 2026-10-25 / MAIN03 C5AK:** The active roadmap priority is **C5 native session continuity**, superseding the older V5DCM and C3S "next steps" preserved below. **Locally proven:** C5Y recovered from a genuine controller cold restart using existing guarded FC23 → ordered FC16 export through 06F4 → runtime FC03/0708; C3 manual CURRENT one-shot returned four H/D/C/M pages (snapGen 1→2). **Not proven:** C5AK complete controller-cold-start chain or safe ESP-only automatic retained hot-rejoin. C5AJ's 0662/count33 physical ACK with no later 0683 was transport-only. C5AK repaired a competing timer; its subsequent retained OTA log recorded no controller DCM offer, no TX, bounded expiry. C5AK is not a newly fully verified runtime release. **Current next action:** one user-initiated, bounded full controller-offered cold-start observation on existing C5AK using C5Y as reference, evaluating complete FC23/FC16/FC03, fresh H/D/C/M 4/4, RX/DE and HA parity; not another isolated ACK experiment. Do not infer controller acceptance from an ACK, send invented requests, perform autonomous flashing or HA parameter writes. ABORT/rollback for alarm, collision or corruption. The three canonical Research files record the detailed evidence and unchanged ON HOLD write policy.

---

> **S62 FINAL DECISION — 2026-10-21 (overrides older open/prerequisite wording below for this unchanged XTR installation).** On user's explicit instruction, **G01 controller epoch, G02 conditional external native peer/owner and G04 native response-slot risk are COMPLETE / POSITIVE — USER-ACCEPTED OPERATIONAL RISK CLOSURE**. This is a documented risk acceptance, **not** false claims of independently probed controller rail, universal absent peer or measured FC23 acceptance window. New user TTL waveform recordings showed 2,280/2,280 9600-8E1 CRC-valid frames in 267.387s with 2,280 matching GPIO1-like marker edges (EOF-to-marker median 19.268ms) and 373 native 0x0F FC16 requests each followed by at least 102.311ms of observed no-next-frame time. Earlier user-performed G01-09 intervention/video, preaccepted conditional G02 installation inventory and bounded XTR V4.1 success retained. **Do not routinely reopen these THREE gates, request inaccessible GPIO18, or insist on new power/peer/slot probes in future work;** reconsider only changed hardware/wiring/profile, observed competing 0x0F output, a concrete contradicting fault or explicit user reopening. Historical uncertainty stays archived and is not converted to physical `true` booleans or auto-arm. Separate UART/DE safe drain/reset and full ESPHome embedded build remain independent safety work. Reference: `Research/V5DCM/V5_NATIVE_S62_TIMED_TTL_RISK_CLOSEOUT_20261021.md`. No new flash/TX.

---

# 2026-10-18 HANDOFF UPDATE: User YES: MANUAL THERMIA CONTROLLER POWER CYCLE CONFIRMED for V5DCM32-LIVE-OBS-01. Previously noted 'unconfirmed restart' in older entries is superseded by the user's follow-up, not retroactively established as independent hardware measurement. Arm 22:02:23, B11D incomplete 22:02:30, 12923ms gap 22:02:43, FC23 22:02:45, BadIntegrity verdict5 Denied, 0/0 ledger, localGen0, TX HARD_DENY. Status COMPLETE / NEGATIVE rejoin. V5DCM33-INTEGRITY-RECOVERY-OFFLINE-01 PREPARED / NOT RUN. Next OFFLINE study exact incomplete-frame latch; no repeated physical restart until reviewed.

---

# LATEST 2026-10-18 V5DCM32 LIVE ARMED ATTEMPT COMPLETE / NEGATIVE FOR REJOIN. Real user log 22:00:23–22:03:44 SHA256 94c3121d56ff70c2bef30e621f82eac97fb80f7b1d7ab2d4e006f1fef6842c11. Arm at 22:02:23, B11D FIRST_FAULT incomplete 22:02:30, R6-P24 12923ms gap 22:02:43, 14 FC23 afterward, Bridge step=2 verdict=5 BadIntegrity (confirmed exact policy enum) and localGen=0; V5DCM23 1/33→0/0 fail-closed. Software TX HARD_DENY/DE LOW. No native Online or epoch ownership proved; user physical restart not separately confirmed. NEXT V5DCM33-INTEGRITY-RECOVERY-OFFLINE-01 PREPARED / NOT RUN; read exact B11D parser before any repeat live restart. Full provenance: V5DCM/V5DCM32_LIVE_REJOIN_INTEGRITY_DENIAL_20261018.md.

---

# LATEST 2026-10-18 HANDOFF — V5DCM32 FIRST LIVE ARM CONFIRMED (REJOIN STILL UNKNOWN)

V5DCM32-LIVE-OBS-01 stays **RUNNING / PARTIAL** after second user API log (5,000 lines; 21:42:09–21:45:31; SHA256 1187ff2b...). **21:45:09.681** user pressed `V5DCM32 Arm Fresh RX Rejoin (NO TX)` and `FRESH_RX_REJOIN_ARMED userArmed=1` executed on-device. At **21:45:18.308** status `step=1 scope=1 localGen=0 verdict=8` = **WAITING / MissingContext** (verified against exact private V5DCM31 header). No current native FC23, new R6 gap/return or cold controller event in supplied excerpt; portable V5DCM23 & V5DCM22 remain **1/33**, software TX HARD_DENY, healthy B11C/B11D parity/no fault, DE=0. The log ends **22 seconds** after arm, before 30s limit; **not a failed/expired scope conclusion**. Ask user only if manual controller restart was performed after 21:45:09, and for smallest continuation log ~21:45:30 to 21:45:50 if yes; no need for arbitrary new experiments or a second arm yet. G01–G06 residual risk acceptance stands. Current device V5DCM32 RX-only, FIX2 baseline fallback. [Detailed finding](V5DCM/V5DCM32_LIVE_ARM_PARTIAL_20261018.md).


---

# NEWEST HANDOFF — V5DCM32 IS NOW USER-FLASHED AND RUNNING (2026-10-18)

User explicitly confirmed V5DCM32 OTA on their XTR ESP32 and supplied 1514-line 63s live API log. **V5DCM32-LIVE-OBS-01 RUNNING / PARTIAL** (NOT previously PREPARED/NOT RUN; NOT COMPLETE). Two [V5DCM32] lines: RX_ONLY step=0 scope=0 localGen=0 verdict=0 TX=HARD_DENY: first-stage live parser integration works, but **fresh arm/rejoin has not been attempted**. Strict V5DCM22+portable V5DCM23 both 1/33, FC23=0, no controller gap/cold transition in log; B11C/B11D parity zero mismatches, no parser faults, normal HA readings, 88/88 software output attempts blocked/physical=0, DE=0. Legacy R6 D=4 sticky unrelated, unknown first fault. First V5DCM32 code log hash unverified as flashed binary and ESPHome CLI cache names GAP51D, but actual V5DCM32 logger runs. Prior FIX2 is **fallback**, not active image. [LIVE evidence report](V5DCM/V5DCM32_LIVE_OBS_PARTIAL_20261018.md); offline source result remains COMPLETE/POSITIVE [here](V5DCM/V5DCM32_RX_REJOIN_SOURCE_INTEGRATION_OFFLINE_20261018.md). If user intentionally starts fresh test, press `V5DCM32 Arm Fresh RX Rejoin (NO TX)` in Configuration immediately before controlled manual restart; 30-second/8192-observation scope, new gap/return + cold pattern + canonical current 0x0F FC23 required, and all TX remains HARD_DENY; no spontaneous hardware action. Require minimal log of V5DCM32/23/22 R6-P24 B11C/B11D S8 and first fault, rollback FIX2 on regression. G01–G06 remain accepted residual engineering risks.


---

# LATEST HANDOFF — V5DCM32 (2026-10-18)

**NEW V5DCM32-RX-REJOIN-INTEGRATION-01 COMPLETE / POSITIVE, OFFLINE SOURCE/HOST/STATIC ONLY**: full private FIX2-derived RX-only candidate ZIP `V5DCM32_RX_REJOIN_INTEGRATION_OFFLINE_NOT_FLASHED.zip` SHA256 346966b47cad7a184936a905e40e46fa19bb6fbe8e7140eeee505cbbc1dc9374, source reference [V5DCM32 detailed report](V5DCM/V5DCM32_RX_REJOIN_SOURCE_INTEGRATION_OFFLINE_20261018.md). V5DCM31 bounded accepted-risk Fresh policy now connected to ORIGINAL V5DCM23 33-group collector in same single native CRC callback, after original R6-P24 observer; prior FC23 revocation + manual Configuration arm + **new post-arm gap/return, cold status and same-frame canonical FC23** required to locally reselect portable 0/33. Retained/recovery and other V5 readiness layers NOT connected. Host exact portable C++ 34/34 PASS with synthetic and genuine historical FC23, V5DCM31 policy 61/61 PASS, YAML parser+includes+HA identity source checks PASS. No full ESPHome compile, no flash, no device TX. **LIVE current user-flashed V5DCM23 FIX2 remains RUNNING / PARTIAL RX-only 1/33, HARD_DENY**; exact flash digest unknown. Candidate has 2 new HA Configuration experiment buttons, preserve 117 sensors/13 binary/47 text. Next **V5DCM32-LIVE-OBS-01 PREPARED / NOT RUN** must be separately user-initiated after reviewing candidate + rollback; don't claim user ran it. G01–G06 residual research risks already accepted; don't re-open as gate. v5dcm22 since-boundary witness still independently revoked, no native DCM C2/Online acceptance evidence. Older V5DCM26 15–20-minute unchanged-FIX2 observation remains PREPARED / NOT RUN.


---

# LATEST HANDOFF — 2026-10-18 V5DCM31 COMPLETE / POSITIVE OFFLINE

A new **nontransmitting accepted-risk, user-armed, finite native-session policy** has been compiled and host tested (61 strict assertions + original GAP24A/B join PASS). **G01–G06 risk acceptance is standing; do NOT restart those proof projects.** This new policy emits **RX-only `RxCandidateUnderAcceptedRisk`** for explicit fresh/retained/recovery experiment context, NOT an independent physical epoch witness, native Online acceptance, owner/slot or TX approval; never fake V5DCM29 `IndependentProof`. Private V5DCM31 archive SHA256 cc576fed... NONFLASHABLE and **not integrated into current YAML**. [V5DCM31 report](V5DCM/V5DCM31_ACCEPTED_RISK_SESSION_POLICY_OFFLINE_20261018.md). Next **V5DCM32-RX-REJOIN-INTEGRATION-01 PREPARED / NOT RUN**: modify only strict RX-collector reselect using monotonic LOCAL generation and exact FIX2 callback; preserve HA identities and TX HARD_DENY; keep live user-flashed **V5DCM23 FIX2 RX-only RUNNING / PARTIAL 1/33**. Distinct V5DCM26 long passive observation still PREPARED / NOT RUN. No physical flash or output performed in V5DCM31.


---

# LATEST USER DECISION — 2026-10-18: G01–G06 ACCEPTED RISKS

User explicitly reconfirmed **all G01–G06 residual research risks are accepted** for the documented unchanged XTR installation. This was ALREADY reflected in standing [native autonomous TX authorization](NATIVE_AUTONOMOUS_TX_AUTHORIZATION_20261018.md): do NOT repeatedly reopen six proof projects or present their missing strict electrical evidence as mandatory blockers to development and a properly bounded user-initiated native test. Technical states remain as originally evidenced; G01-09 intervention-video POSITIVE, G02 scoped installed-topology CONDITIONAL acceptance, G03/G04/G06 OPEN and G05 PARTIAL. V5DCM30 `COMPLETE / INCONCLUSIVE` concerns unavailable **verified current epoch witness only**, not a general veto. Next V5DCM31 should design actual bounded V4.1-derived session integration with a distinct **accepted-research-risk experiment policy** instead of pretending a `V5DCM29 IndependentProof` exists. Do not change the installed FIX2 RX-only/HARD_DENY or transmit until a specified user-initiated live test has known slot, timing, limited response policy, abort/rollback. No new experiment run in recording this reaffirmation.

---

# CURRENT HANDOFF — 2026-10-18 V5DCM30

Latest **V5DCM30-INDEPENDENT-WITNESS-AUDIT-01 COMPLETE / INCONCLUSIVE** for usable CURRENT independently witnessed controller epoch. Report: [G01/G02 provenance audit](V5DCM/V5DCM30_INDEPENDENT_WITNESS_AUDIT_20261018.md). Historical **G01-09 video+user switch/display off/on was positively documented**, not main-controller rail measured or current FIX2 restart proof. Earlier **G02 is already user-approved COMPLETE / POSITIVE (CONDITIONAL)** for unchanged no-DCM external port and bounded historical work; don't reopen this acceptance, but don't claim electrical exclusive slot/owner. V4.1 EXP386/387 locally proven guarded native recovery, EXP388 PARTIAL; no current V5 permission. The original G01-09 raw video/log not mounted for this audit; earlier report used with explicit provenance. Installed XTR remains **V5DCM23 FIX2 RX-only RUNNING / PARTIAL 1/33 in short live log, 0 captured FC23, TX HARD_DENY**, exact flashed SHA/slot and D=4 fault origin unknown. No actual runtime V5DCM29 independent proof issuer. **V5DCM31-MANUAL-SESSION-SCOPE-01 PREPARED / NOT RUN** is next offline source/policy action to distinguish manual bounded proof from autonomous proof. Previously V5DCM26 15–20min passive live obs remains PREPARED / NOT RUN. No new code/ESPHome/flash, controller restart or native TX.


---

# CURRENT HANDOFF — 2026-10-18 V5DCM29

**Latest:** V5DCM29 source-only physical-epoch versus local session generation contract COMPLETE / POSITIVE on three strict C++ host tests. Original historic FC23 drives real unchanged V5DCM28 ledger to revoked; there is NO genuine current physical witness/owner/slot/Online proof and no production wiring. Private ZIP is nonflashable. **Deployed user device remains V5DCM23 FIX2 RX-only, RUNNING / PARTIAL (1/33 short first log), TX HARD_DENY.** V5DCM26 15–20-minute passive observation still PREPARED / NOT RUN; **V5DCM30 INDEPENDENT WITNESS AUDIT PREPARED / NOT RUN** is next offline action. V5DCM28 numeric `proven_controller_epoch` MUST NOT be used as both physical epoch and monotonically increasing local generation; source contract separates them. No new firmware, ESPHome compilation, flashing or TX. [Result](V5DCM/V5DCM29_SESSION_PROVENANCE_CONTRACT_OFFLINE_20261018.md). Canonical project state above older summaries remains authoritative.

---

# CURRENT HANDOFF — V5DCM28 2026-10-18

Live user-flashed **V5DCM23 FIX2: RUNNING / PARTIAL RX-only**, first short log 1/33 strict page groups and clean RX, no FC23 captured, native TX HARD_DENY. Latest **V5DCM28-EPOCH-GUARD-01 COMPLETE / POSITIVE for OFFLINE host tests only**: one inert V5DCM27 source reselect guard now refuses repeated/older controller generation *labels*, cross-tested with the real historical 20261003 FC23 and gap24a/b Fresh/Retained/Recovery metadata. No current independent actual owner/physical epoch/slot proof; proof flag in host test synthetic only; 1/33 unresolved. New ZIP is **NOT FLASHABLE**, no ESPHome/HA changes. V5DCM29 trustworthy independent-session contract PREPARED / NOT RUN; V5DCM26 15–20-minute same-FIX2 passive run also PREPARED / NOT RUN. [Source/host result](V5DCM/V5DCM28_EPOCH_GUARD_AND_LIFECYCLE_PROVENANCE_OFFLINE_20261018.md). Verify newest canonical file headings below, not older snapshots.

---



---

# CURRENT VERIFIED HANDOFF — 2026-10-18 V5DCM27

Latest user-flashed device is **V5DCM23 FIX2 RX-only, RUNNING / PARTIAL** (first ~2m25 log, actual portable ledger 1/33, clean B11C/B11D and TX HARD_DENY). Previous V5DCM20 18m33 RX-only positive is a different device build. Latest OFFLINE step **V5DCM27-SOURCE-REJOIN-01 COMPLETE / POSITIVE**: strict original-private-C++ host tests confirm native 0x0F FC23 revokes V5DCM23 package ledger and the only reselect call is on ESP boot. Further FC16 alone cannot restore the package ledger, but this has NOT happened in the current short live FIX2 log (no observed FC23). Internal CM930 handshake shadow is NOT physical owner or TX authorization. Next **V5DCM27-REJOIN-BRIDGE-01 PREPARED / NOT RUN**: source-only externally qualified profile/epoch reselect, preserve all 180 current private HA entities, TX hard deny, no extra UART, no automatic FC23 rearm. Report: [V5DCM27 source and regression](V5DCM/V5DCM27_NATIVE_REJOIN_SOURCE_AUDIT_20261018.md). Prior V5DCM26 passive 15-20min live observation also PREPARED / NOT RUN. Verify exact flashed bytes before any code change. This block supersedes older dated snapshots below only for current state.

---

# START HERE — Thermia iTec XTR M
> Compact, evidence-bound entry point for a NEW ChatGPT session. Updated 2026-10-18. This is a navigation and handoff document, NOT a replacement for the canonical evidence. Verify the latest dated canonical entries before acting.

## Standing autonomous native TX authorization (2026-10-18)
User explicitly authorizes **general, autonomous native TX** for Online/Connect/DCM development and controlled deployment: no repeated general consent per handshake or response in an already scoped and armed user-initiated experiment. This is **permission, not evidence** of protocol acceptance or electrical ownership. G01–G06 previously accepted research risks remain technically scoped; do not demand repeating them simply to continue research. The verified installed V5DCM19 FIX1/V5DCM20 device remains **RX-only/TX HARD_DENY** until a separately documented live activation; no live TX/flash occurred by changing this note. Preserve fail-closed session/CRC/owner/slot/retry and abort/rollback, confidentiality, and no uncontrolled scans/unknown ACKs/speculative writes. [Authoritative user decision](NATIVE_AUTONOMOUS_TX_AUTHORIZATION_20261018.md).

## Latest cross-project handoff — 2026-10-18
- **V5DCM21 source-derived package coverage update (2026-10-18):** 2.1.105 modern profile sensor/config 570 definitions -> 541 numeric dependencies -> **33 candidate significant groups** (W2=15, W3=10, W4=8); v31 FIX4 only tracks 13/33, so `Native Settings Pages Seen` is not C2 evidence. [Source audit, limits and CI](V5DCM/V5DCM21_PROFILE_242_SIGNIFICANT_PACKAGES_20261018.md).
- **Actual latest user-run firmware:** v31 FIX4 **read-only**, with `03E8:Y` and the other 12 native settings pages `N` at 151s; user subsequently says missing pages **still N**, without a new exact uptime or no-reboot confirmation. This is READ-V31-UNKNOWN-01 **RUNNING / PARTIAL**, NOT an active V5DCM21 trial.
- **Historical native XTR proof:** EXP325–329 owned ACKs in a qualified native session advanced `03E8→03FC→0410→042E→0442`. This supports the hypothesis that missing current-service pages can require native synchronization; it is not permission or evidence of a complete new session.
- **V5DCM21 latest:** **RUNNING / PARTIAL**; actual firmware-repo HEAD CI [39124813711](https://github.com/ryckema/Thermia_Connect_Firmware/actions/runs/39124813711) PASS, including **26 new** 2.1.105 three-mask package-readiness checks plus prior source/RX/delivery cases. W2/W3/W4 bit-to-range mapping is firmware-derived and verified; *exact significant subset* for XTR profile 2.4.2 remains unknown. [Result](V5DCM/V5DCM21_2105_PACKAGE_COMPLETENESS_OFFLINE_20261018.md).
- **Autonomous native TX** authorized by user as standing permission; accepted G01–G06 risks must not be reopened by default. No new active TX or code flash was performed by this V5DCM21 offline substep; any first autonomous deployment requires an explicitly scoped/armed test.

## First five minutes
1. Read **this file** and [CONTINUITY_WORKFLOW.md](CONTINUITY_WORKFLOW.md).
2. Read the **TOP/current sections** of [THERMIA_PROJECT_STATE.md](THERMIA_PROJECT_STATE.md), [EXPERIMENT_LOG.md](EXPERIMENT_LOG.md), and [PROTOCOL_FINDINGS.md](PROTOCOL_FINDINGS.md). These large files contain historical entries: do NOT treat every older 'LATEST' heading as current.
3. For the active experiment, read the linked experiment-specific PREPARED/RESULT report and the exact code/YAML provenance.
4. Inspect relevant [Thermia Connect firmware research](https://github.com/ryckema/Thermia_Connect_Firmware) and actual firmware files when firmware claims matter.
5. Check for newer commits/experiments than this handoff. If found, update this file; never override newer evidence with this snapshot.

## Verified handoff snapshot — 2026-10-18
- **Most recent locally confirmed live test:** **V5DCM20 COMPLETE / POSITIVE** for passive RX-only stability. User-provided log covered **18 min 33 sec**; B11C/B11D raw-vs-portable parity with zero observed count/byte differences, drops 0, **2,619 TX candidates denied and physical TX attempts 0**. Some HA values briefly NaN through natural fan/compressor transitions: semantics unresolved.
- **Deployed baseline in the latest result:** V5DCM19 FIX1, RX-only, TX HARD_DENY. Do NOT infer it has since changed without current source/log verification.
- **Next planned step:** **V5DCM21 PREPARED / NOT RUN** — *offline* TX-readiness/source/evidence audit from V4.1 plus original CM930 reference. Not approval to transmit.
- **Independent unresolved task:** V5DCM18 original Python reference-Core full fixture/stateful replay remains **RUNNING / PARTIAL**; separately bounded ZIP C++ tests/replays passed but do not close it.
- **Accepted constraints:** G01–G06 residual risks remain accepted/closed pending genuinely new evidence. Physical owner, response slot, native challenge acceptance, Online icon/cloud readiness remain unproven locally. User has **now authorized general autonomous native TX in principle** for documented/armed controller-driven integration; **authorization is not evidence of safe electrical or protocol readiness**.
- **Firmware distinction:** user ZIP portable Core and firmware-repo HEAD have differed; never transfer test validity between them without checking provenance.
- **Important evidence:** [V5DCM20 live result](V5DCM/V5DCM20_LIVE_RX_ONLY_RESULT_20261018.md), [V5DCM19 FIX1 live result](V5DCM/V5DCM19_FIX1_LIVE_RESULT_20261018.md), [V5DCM18 functional gap handoff](V5DCM/V5DCM18_FUNCTIONAL_GAP_HANDOFF_20261018.md).

## Do next
1. Check whether V5DCM21 has subsequently been prepared/performed.
2. Review V4.1, original firmware reference, current deployed code and **accepted G01–G06 research risks**; prepare qualified autonomous TX behavior without reopening these gates reflexively.
3. Keep the **currently installed** RX-only TX hard-deny unchanged until a bounded user-initiated, explicitly armed deployment/test; standing general authorization does not itself execute code.
4. After any material result, update canonical files, then refresh this handoff in the **same documentation change**. Verify commit and report SHA.

## What NOT to do
- Do not ask for a DCM module, disconnect room sensor or silently repeat rejected tests.
- Do not confuse synthetic/offline acceptance with native local confirmation.
- Do not mark PREPARED as COMPLETE; do not invent compilation, flashing or TX.
- Do not expose confidential response algorithms/private 0x0F or 0x0708 material.
