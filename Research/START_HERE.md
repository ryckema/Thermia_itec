## 2026-10-25 — HANDOFF C5AQ: boot auto-START confirmed BUG; correct complete source prepared

**Attention: do NOT flash older prepared C5AP.** User actual log from C5AO at 18:22 after OTA showed stage40/RETAINED_CONTEXT_MANUAL even though user did NOT press S92; 0 FC16 ACK and 0 physical TX; after 60s automatically expired RX ONLY / DE LOW. The full C5AP source inherited a 5s ESPHome on_boot button.press on the MANUAL S92 control and conditional 07E4 autoarm. This incorrectly grants user-only authority at boot, not an OEM native session. **C5AP SUPERSEDED / NOT RUN**. Private **C5AQ** now removes the boot callback and leaves original DE LOW/RX-only initialization, changes build/status label. Retains all other C5AP native first 0864, 0870, 0708, config/085F, C5AK cold-start, C3 FC03/CURRENT, existing HA and collision/CRC/TX guards. Full source offline YAML checks PASS; target build/flash/LIVE NOT DONE. ZIP has ONE YAML, README, manifest; no old YAML.

**ONE NEXT ACTION:** User flash C5AQ, confirm RX ONLY/DE LOW and stage inactive *before* pressing Configuration → S92 Native DCM | Start Session Manually. Then user-initiated ONE bounded native session with controller/room sensor connected; abort or rollback if needed. No HA parameter writes. Only true RUNTIME+SYNCED+fresh CURRENT H/D/C/M 4/4 is success.

---

## 2026-10-25 — HANDOFF: C5AP private SOURCE prepared; C5AO remains last user LIVE

**Milestone C5 native rejoin on iTec XTR M controller 2.4.2.** Genuine OEM Connect 2018/2.1.105 is a Modbus slave, no established outbound rejoin initiator. Local original DCM 2026-10-03 XTR capture ACKs FIRST `0864/count4`, then FIRST `0870/count17`, then FC03/0708. The old C5AL branch in latest LIVE C5AO would reject that genuine 0864 payload and wait for a second 0864, prearm button and earlier 0708. **One integrated full private C5AP fix** now handles the FIRST controller-offered CRC-valid 0864 in one explicitly manually started S92 session with existing sole UART/DE owner, no invented second-offer/payload/prearm/12-15s constraints, then existing 0870/0708/CURRENT follow-up. Removes obsolete extra C5AL HA arm button, preserves all other production controls, V5/CRC/de/collision safeguards, C5AK FC23 cold-start, first config/085F responder, C3 refresh and HA writes HOLD. One compact ZIP: only complete latest C5AP YAML + README + manifest. SOURCE/OFFLINE TESTED, **NOT** TARGET COMPILED/FLASHED/LIVE. No device TX and no private code on GitHub. C5AO last XTR live native join COMPLETE / NEGATIVE.

**One next action:** user-initiated ONE bounded full C5AP manual S92 rejoin with complete log captured BEFORE pressing start; 0864 may be absent and that's still a real blocker, not trigger failure. Observe only actual native RUNTIME/SYNCED+CURRENT fresh H/D/C/M 4/4 as positive. S92 ABORT/DE LOW and saved C5AO rollback; keep room sensor and controller running, HA settings writes ON HOLD. Then GO/FIX/NO-GO.

---

## 2026-10-25 — C5AO FLASHED / LIVE, native DCM still not accepted; focus OEM entry

**Controller:** user Thermia iTec XTR M 2.4.2. Private C5AO first config-ACK firmware (user flashed) now has one bounded S92 session with `initFC16=059C`, `runtimeFC16ACK=1`, physical TX 1, `OEM_INTERNAL=ACCEPTED` *only internal*, no 04A6, 085F, further config, FC03/0708 or fresh H/D/C/M 4/4. First request/ACK occurred before log started 17:42:28; exact first-offer timing not proven. At 17:43:25.806 unqualified 60.031s expiry, RX-only/DE LOW, CRC/resync/drop 0. Complete end-to-end native join **COMPLETE / NEGATIVE**, fail-safe **COMPLETE / POSITIVE**. Genuine OEM XTR full export had 04A6 BEFORE 059C; therefore C5AO's corrected first normal FC16 ACK by itself does not create a native attach.

**NO-GO further ACK-gate microtests. ONE NEXT ACTION:** find and integrate the specific legitimate OEM native session-entry/re-entry behavior from original Connect (2018/2.1.105) vs C5AK locally verified cold-start, or explicit NO-GO if no supporting XTR evidence. Preserve sole UART/DE, room sensor, all production HA; controller restart NOT requested, HA parameter writes ON HOLD. Do not publish private OEM firmware/YAML.

---

## 2026-10-25 — LATEST HANDOFF MAIN03-C5AO prepared for XTR 2.4.2

**Current milestone C5.** User controller **2.4.2** (iTec XTR M, older/non-Genesis); Connect firmware **2.1.105** is gateway image, not controller version. C5AN user-flashed first-join attempt on still-running controller offered 059C twice, ACK sent on duplicate, no FC03/0708/CURRENT, owner not qualified and 60s RX-only rollback (COMPLETE / NEGATIVE full DCM; first-085F branch untriggered). Genuine OEM XTR 2026-10-03 answered first 059C immediately. **Private C5AO complete single-YAML ZIP SOURCE / OFFLINE TESTED / PREPARED / NOT RUN:** one integrated first-offer FC16 fix covers 04A6/count13 and existing 22 C5AC config geometries via same S92 UART/DE TX owner, preserves 2.4.2 profile fields, C5AN 085F, previous cold-start, hot-rejoin, native FC03/CURRENT, HA and real bus protection; no semantic session acceptance from mere ACK and HA writes HOLD. Full target compile/flash/live NOT done. GitHub docs only, never publish protected firmware code.

**ONE NEXT ACTION:** user compiles/flashes private C5AO and runs one bounded manual S92 stage40 full cold-join on running controller (room sensor connected, no heat-pump restart), full log; assess real native RUNTIME + FRESH H/D/C/M 4/4 and safety/ABORT. Rollback to user's saved C5AN (not included in ZIP). Continue GO/FIX/NO-GO rather than extra speculative experiments.

---

## 2026-10-25 — C5AN live result and next source FIX

C5AN user-flashed and live. One S92 stage40 session on running controller captured CRC-valid 059C/count33 twice at 17:15:58.285/59.072 and one C5AD ACK at 17:15:59.088. No 04A6/085F/further export/0708/FC03 or 4/4; after 60s RX-only/DE LOW, zero CRC/resync/drops. Full native cold join COMPLETE / NEGATIVE; specific new first-085F path NOT TRIGGERED, retained as RUNNING / PARTIAL validation. New SOURCE discrepancy: existing C5AD needs duplicate 059C before first ACK; genuine local OEM Connect XTR 2026-10-03 ACKed its first 059C within ~14ms. Next FIX one integrated OEM first-config-offer responder through existing manually armed S92 UART/DE path and real guards, no old YAMLs in ZIP. Do not confuse ACK with owner; no WP restart, room sensor removal or HA setting writes. See latest top canonical Research entries.

## 2026-10-25 — CURRENT HANDOFF: MAIN03-C5AN prepared, not yet live

**Milestone C5.** The exact complete private C5AM source ZIP is now supplied and its YAML hash matches previously recorded source. The source-availability blocker is therefore closed. Original Connect 2018/2.1.105 + genuine XTR DCM capture justify removing C5AM's extra PREARM/two-offer/POST0662 restriction for alarm FC16 transport. A complete private C5AN YAML ZIP has been prepared (SOURCE / OFFLINE TESTED, not target compiled/flashed/live). First exact known 085F response after a single user-initiated S92 stage40 start is bounded to one new unvalidated physical ACK; no session ACCEPTED/owner/write privilege inferred. Existing native/HA features, UART/DE safeguards, parser and rollback preserved. Early transport-only alarm ACK excluded from C5AB/C5AD/C5AL initial-entry config ACK counting. Prior C5AM-COLD-JOIN-01 is still RUNNING / PARTIAL (its specific gated branch never triggered); C5AN-OEM-085F-01 is PREPARED / NOT RUN. **ONE NEXT ACTION:** one complete user-initiated C5AN cold join test on running controller, with room sensor connected, no controller restart, no setting writes, S92 ABORT/rollback available. Only actual RUNTIME/SYNCED/FRESH CURRENT 4/4 counts positive.

---

## 2026-10-25 — OFFLINE: OEM 085F first-offer ACK vs C5AM two-offer gate — SOURCE / OFFLINE TESTED

**Evidence review (no live test, no new firmware, no TX):** Original Connect 2.1.105 appfs (`device_client/cm/modbus_server15.py`, version 0.2.8) exposes Modbus RTU server at the existing DCM slave address and receives FC16 through normal slave handler. `CM_Client_Constants.ALARM_START_ADDRESS=2143 (0x085F)`; `_on_function16` publishes every received register event, but *excludes ALARM_START_ADDRESS* from setting internal `HandshakeState.ACCEPTED`. Thus ordinary alarm FC16 transport response and acceptance are independent. Do not infer session/owner/semantic acceptance from ACK.

**Verified exact XTR genuine DCM capture (2026-10-03, local file `thermia_capture_20261003_165355.log`):** controller FC16 04A6/13 at 38.419s, ACK 38.433s; 0662/33 at 55.187s, ACK 55.202s; 0683/33 at 56.599s, ACK 56.611s; final export 06F4/19 at 61.461s, ACK 61.475s; FIRST 085F/5 at 61.529s, OEM ACK at 61.542s (13ms). NEXT 085F not until 84.572s (ACK 84.586s). All 12 cited request/ACK frames individually passed Modbus CRC16 offline. There is NO requirement of two 085F requests before first ACK in this successful genuine XTR DCM trace.

**Implementation discrepancy:** Current C5AM source description in Research state requires special POST0662_PREARM and TWO new zero-085F offers before one response; that is more restrictive than original normal FC16 server / this live DCM reference. It may explain controller repeatedly offering zero 085F and withholding further export after C5AL's five ACKs, but CAUSALITY is a HYPOTHESIS, not PROVEN: in successful genuine trace the 085F occurs AFTER completion 06F4, whereas C5AL encountered retries early after 0662. Neither C5AL nor C5AM has established semantically accepted rejoin. The 2026-10-25 C5AM live logs show missing prearm/offer prerequisites, so the NEW C5AM condition was **NOT EXERCISED**, not failed. C5AM-COLD-JOIN-01 retains **RUNNING / PARTIAL** status.

**Integrated engineering decision (offline FIX identified, source blocked):** On receipt of FIRST full CRC-valid, exact 085F/count5 request in one explicitly authorized native session, service it through existing single S92 Modbus ACK implementation with existing bus/DE/collision, source address/shape, ABORT and rollback guards, without a second M7/POST0662 button or two-duplicate requirement. Its receipt/ACK MUST NOT set ownership, handshake ACCEPTED, FC03 read permissions or HA parameter-write permission. Keep normal FC16 export/FC03 chain qualified independently. Scope as one bounded user-initiated future full cold-session validation, not a 085F microtest or autonomous TX.

**Real source blocker:** latest user-flashed C5AM *full private YAML/dependencies* are absent from currently available mounted/conversation files and not committed to GitHub; last byte-verified available private YAML is older C5AK. NEVER fabricate a C5AM-based ZIP from C5AK or erase C5AL/C5AM features. This offline review establishes a specific integration change but cannot honestly claim SOURCE FIXED / TARGET COMPILED / FLASHED / LIVE. No reason to ask user to act while away.

**ONE NEXT ACTION:** Apply this single OEM-equivalent 085F first-offer responder correction into the actual C5AM complete YAML when accessible, preserving all native and HA functionality; then one end-to-end user-started validation at home and GO/FIX/NO-GO. No independent test of a lone 085F frame.

---

**2026-10-25 C5AM LIVE LOG REVIEW:** Two uploaded logs are overlapping (short is exact prefix of long). Device confirms C5AM flashed; initial S92 session began before log and sent one FC16 ACK (085F counter=1, no C5AM proof), timed out 13:12:35. Second explicit S92 START at 13:13:21 stage40 sent 0 TX and timed out 13:14:21. No `POST0662_PREARMED`, `POST0662_ARM_BOUND`, 04A6→0662 pages, 0708 or current 4/4; clean CRC/RX and DE LOW. **C5AM-COLD-JOIN-01 RUNNING / PARTIAL**, its post-0662 085F fix NOT TRIGGERED, not proven negative. Next: confirm real controller first-attach offers before one correctly prearmed run; avoid unarmed repeated START. See Research/EXPERIMENT_LOG.md.

**2026-10-25 CURRENT C5 COLD-JOIN FIX: MAIN03-C5AM SOURCE PREPARED / NOT RUN.** Live C5AL 04A6→04BA→059C→05FF→0662 sent five ACKs on continuously running controller; no 0683/0708/runtime. Exact source review found existing OEM-consistent one-shot alarm response reachable on C5AD path but missing from C5AB 04A6 path. Private C5AM enables ONLY one manually prearmed, post-0662 two-offer one-shot existing reply via sole S92 TX owner, preserving no-acceptance until qualified runtime and fresh H/D/C/M. Offline YAML, patch and source tests done; target compile/flash/live NOT done. No private YAML committed; no WP reboot. Next: ONE user-initiated C5AM-COLD-JOIN-01 with ABORT and rollback. See Research/EXPERIMENT_LOG.md.

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
