## 2026-10-25 — C5AK OEM / XTR continuation decision — COMPLETE / INCONCLUSIVE (retained active session)

Source review: original 2018 CM930 modbus_server15.py dispatches FC16 through Modbus slave callback `_on_function16`, posts register receipt and tracks internal HandshakeState.ACCEPTED separately; it does not generate unsolicited `0683` next-page request. Genuine XTR DCM trace 2026-10-03 at 55.187s FC16 0662/count33, ACK 55.202s, next controller FC16 0683/count33 at 56.599s, ACK 56.611s, proves expected progression under that controller context. User C5AJ live: exact 0662 reply physicalTX=1 and clean DE LOW, no controller-follow-up in 120s; controller-side acceptance is NOT demonstrated. User C5AK live: OTA retained manual stage40, zero DCM requests, zero TX, proper RETAINED_NO_DCM_OFFER after 60024ms; cold rearm enabled before expiry but no later observed >=5s bus outage. Source C5AK includes `exp420_resume_owner = exp420_config_shape && write_resume_started && !write_resume_done`, and local resume-page ACK path ordered to 0683, so no demonstrated firmware refusal of an actually offered 0683 in these logs. Controller-context causality remains OPEN. Do not fabricate a follow-up handshake or modify timeout again. Decision: FIX/NO-GO for further speculative TX; retain C5AK and C5Y proven cold recovery, no new firmware on these logs. Next action: only a supported end-to-end meaningful controller-offered cold startup observation or verified source bug; not another single-frame microtest. HA writes remain ON HOLD.

## 2026-10-25 — C5AJ LIVE → C5AK competing timer fix — PREPARED / NOT RUN

**Observed XTR:** C5AJ user flash and manual retained S92 START led to one normal 0662/count33 response, M6 2→3 RESPONSE_SENT, physicalTX=1, DE LOW and no CRC/resync/drop fault. In the log no subsequent ordered FC16 0683..06F4, FC03 or 0708 appeared, no fresh cache/accepted owner; at 60s old 04A6 timer printed EXPORT_RESUME_NEGATIVE despite 04A6_SEEN=0; retained scope terminated at 121254ms. Transport ACK positive, full session outcome negative within this window.

**Concrete integrated fix C5AK:** full private ZIP `THERMIA_MAIN03_C5AK_RET_EXPIRE_FIX_PRIVATE_20261025.zip` based strictly on user-live C5AJ. The legacy 04A6 export-resume 60s timer no longer executes on manually triggered 0662 tail; existing 120s bounded S92 retained expiry becomes sole result owner and explicitly describes no 0683..06F4 continuation. No new TX, frame, UART/RX/DE owner, session qualification, or HA parameter-write authorization; all genuine bus, CRC and collision guards preserved, C5Y unchanged. YAML SHA256 `2dcf4254219461d009f82bd7c8b25c7d581f82d2aeb2fe5fdf8fe9fcc788d77f`. Offline generic YAML parse/ZIP integrity PASS; target compile/flash/live NOT RUN. The fix avoids a deceptive 60s negative status but does not imply controller will continue after single 0662 ACK.

**Decision:** FIX source timer overlap; NO-GO speculative unsolicited hot-rejoin frames or a new single-page TX microtest. ONE NEXT ACTION: reconcile XTR/OEM controller-offered continuation against implemented S92 sequence, then integrate only a concrete evidence-backed fix if found; otherwise NO-GO hot rejoin.

---

## 2026-10-25 — C5AJ unified bounded 0662→tail S92 responder — PREPARED / NOT RUN

**OBSERVED (XTR LIVE C5AI baseline):** 56 repeated CRC-valid 0F FC16 0662/count33 in 60s; OEM internal ACCEPTED is not physical owner; zero TX/FC03, CRC_DIFF=0, resync=0, drops=0 and stage40 session expired. Source confirms additional M7 12s arm + three-retry condition withheld a known native request. Genuine C5Y controller restart cold join separately live-positive. The C5AI optional bus-loss one-shot path was not activated by a real controller interruption in the supplied live log.

**INTEGRATED C5AJ deliverable:** private complete firmware ZIP `THERMIA_MAIN03_C5AJ_INTEGRATED_FC16_CONTINUATION_PRIVATE_20261025.zip`, YAML SHA256 `3e2b6420c14200c3328e487af6184e7c937f08424aad2da6395b6193f2b7526a`. Starts with full user-live C5AI YAML. During a single explicit S92 manual START in retained stage40, exact CRC-validated 0662/count33 may be answered ONCE without a second M7 button or 3 duplicates, if all other existing semantic-idle, peer, RX baseline, CRC/shape, single S92 TX/DE owner and collision guards hold. It then uses the existing guarded ordered 0683..06F4 continuation, with up to 120s bounded tail instead of interrupting it at absolute 60s. No new frame, UART writer, HA parameter-write permission or owner promotion by transport ACK; original C5Y and C5AI cold-return retained. The legacy M7 button remains as backwards-compatible entity but is not needed for the new single manual native session.

**Validation:** SOURCE / OFFLINE TESTED: YAML parse PASS with custom ESPHome !secret tag treatment, identical HA names, one S92 owner and unchanged call-site count (79), 0662 ACK bytes unchanged, ZIP CRC PASS. ESPHome target compiler, flashing and XTR LIVE are NOT RUN. Explicit bounded physical experiment, ABORT and bundled C1C3 rollback included. This is ONE integrated iteration, not multiple single-frame mini-tests. C5AJ may advance only on controller-observed native continuation plus FC03/cache semantics; ACK alone insufficient.

**REAL BLOCKER:** C5AJ response-to-native-controller offer requires live end-to-end observation; silent ESP-only hot-rejoin without any controller DCM requests remains unsupported.

**ONE NEXT ACTION:** user-controlled single C5AJ end-to-end FC16 0662→tail→FC03 test and GO/FIX/NO-GO, without new diagnostic-only microtests.

---

## 2026-10-25 — C5AI XTR live, repeated 0662 withheld — RUNNING / PARTIAL

**User evidence:** logged MAIN03-C5AI after OTA; retained manual stage40 sees 56 identical native slave 0x0F FC16 0662/count33 requests during initial 60-second window, CRC A0AB stable; OEM_INTERNAL=ACCEPTED on 0662; CRC_DIFF=0, parser resync=0, drops=0, no FC16 ACK/FC03/0708/physical TX, DE LOW. M6 event6 retained-unproven expires at 60007ms (M6=7, stage99). C5AI Enable One Retained-Idle Cold Recovery was enabled only after expiry (~08:52:36); no actual controller bus loss/restart is observed, so this part is NOT RUN, not a negative cold recovery result.

**Implementation interpretation:** source S92 permits 0662 native ACK in qualified ordered export, and M7 optionally after separate short manual one-shot arm/3 repeated frames; EXP426 default is capture-only. Existing retained manual session does not itself exercise M7. The extra M7 button and hard 60s session timeout despite ongoing requests are candidate unjustified restrictions for normal OEM-style Modbus servicing. Do not infer device owner or semantic acceptance from OEM_INTERNAL=ACCEPTED or repeated packets. Preserve full electrical, parser, collision and HA write guards. Do not run a new single-page test; next change must consolidate native FC16 response + continuation and run one end-to-end user-initiated bounded trial.

**Outcome:** live RX observation COMPLETE / POSITIVE for repeatable 0662 stimulus and guard diagnosis; C5AI retained-idle C5Y recovery remains RUNNING / PARTIAL (no qualifying controller outage yet). No new TX, no unverified compatibility claim.

---

## 2026-10-25 — C5AI integrated retained-idle C5Y rearm — PREPARED / NOT RUN

**Hypothesis:** Following C5AH passive retained-idle expiry, an independently observed later >=5s full valid-frame bus outage can safely enter the ALREADY proven C5Y controller cold-start engine, instead of remaining stuck at stage99. It cannot create an OEM ESP-only hot-rejoin when the controller offers no DCM frame.

**Baseline:** user-live C5AH (02:52:32–02:53:32, M6=7 RETAINED_NO_DCM_OFFER, 0 FC16, 0 FC03, 0 TX, DE LOW; 18 parser resync, 0 CRC diff/drop) + separately live-verified C5Y full cold recovery. OEM Connect serves controller-driven requests and does not prove spontaneous DCM initiation on XTR.

**ONE integrated change:** private C5AI complete YAML reuses the exact S92 Manual START session reset from the existing 250ms watchdog only with explicit volatile one-shot Configuration opt-in, retained idle M6=7 and a later >=5s bus silence; follows the SAME M6 event3 and C5Y cold return; new wait expires after 120s with no returned valid frame. Owner and TX guards unchanged, no new frames, no HA parameter writes. Explicit ABORT disarms opt-in and drives DE LOW. Existing HA entities preserved (255 named). YAML SHA256 `230ac3deec69ed1a1d63cffd0aa598f661afad34c596c4a7b2c545a8a9de8fdc`.

**Expected:** when enabled by user and a genuine later controller restart occurs, one log `C5AI RETAINED_IDLE_TO_C5Y_COLD_WAIT`, then existing BOOT_RETURN and exact validated challenge/FC16/FC03 path. Normal ESP-only reboot/085F/idle must not trigger. Successful ACK is not semantic acceptance; full native runtime evidence required.

**Actual:** SOURCE / OFFLINE TESTED: YAML parse PASS, patch retained, all existing 255 HA names preserved, unchanged S92 TX call-site count and ZIP CRC PASS. Target compile, flash, physical TX and XTR live: NOT RUN. No live experiment concluded from offline results.

**ABORT/rollback:** HA S92 Native DCM | ABORT Session, verify DE LOW; rollback bundled locally proven C1C3 YAML. No room sensor unplug. Do not activate physical test autonomously.

**Decision:** GO for prepared integrated cold recovery only; NO-GO for ungrounded ESP-only silent hot rejoin; next one full end-to-end user-controlled experiment if elected.

---

## 2026-10-25 C5AH XTR LIVE — COMPLETE / POSITIVE (retained-idle classification)

User log 02:52:32–02:53:32 reports ESP OTA restart, retained manual M6=2 and zero DCM FC16 requests, zero FC16 ACK, zero FC03/0708, zero physical TX, DE LOW. At 02:53:29 age=60004ms C5AH emits `RETAINED_NO_DCM_OFFER 60s RX_ONLY no fake controller reset DE=LOW`, closes stage 99, and M6 subsequently reports `RETAINED_IDLE / NO DCM OFFER / RX ONLY / DE LOW`; provenance updates to `RETAINED_NO_DCM_OFFER / M6=7`. This confirms C5AH's bounded classification but does NOT prove successful hot rejoin or full DCM session. At least 18 parser resyncs were observed by ~02:52:54 versus CRC_DIFF=0 and drops=0; their cause and impact remain OPEN; no ungrounded parser fix. Existing C5Y controller cold-start remains last separately live-positive recovery. Next engineering action: integrate event-based transition from retained idle to a genuinely controller-offered native initiation via existing S92, without invented controller reset, new TX owner, or HA writes. Status: C5AH classification COMPLETE / POSITIVE, native hot-rejoin COMPLETE / INCONCLUSIVE.

## 2026-10-25 — C5AH retained idle event classification — PREPARED / NOT RUN

C5AG user LIVE: ESP OTA reboot, M6 stage40 retained context, zero DCM FC16/FC03 received for full 60s, physicalTX=0, DE LOW, zero CRC/resync/drops; existing generic SESSION_LOST misdescribed eventless ESP-only retained idle. C5AH private ZIP `THERMIA_MAIN03_C5AH_LIFECYCLE_EVENT_ENGINE_PRIVATE_20261025.zip`, based exactly on C5AG, adjusts only existing M6 60-second expiry: with retained manual provenance, zero observed DCM FC16, zero FC16 ACK/0708, no physical TX and no unknown DCM requests, classify `RETAINED_NO_DCM_OFFER` and bounded RX-only completion, rather than generic session loss. No invented controller reset or owner. Genuine observed bus-loss still follows unchanged live-verified C5Y event route. All TX call-sites, single S92 UART/DE owner, HA entity set, cache and write HOLD preserved. YAML parsed and ZIP CRC verified offline; no target compilation or flash/live validation. YAML SHA256 `8fd00707705a648e57f4175579816aeadce0aa37fd6efd10411709ab0726a1d5`. Next: optionally user flash to validate M6 classification; no physical TX experiment required, abort and C1C3 rollback included.

## 2026-10-25 C5AG lifecycle provenance — PREPARED / NOT RUN

C5AF LIVE: exactly one guarded 085F ACK; no follow-up FC16/FC23/FC03, no session acceptance; clean RX and DE LOW. C5AG private integrated ZIP is based on flashed C5AF and adds source-only provenance classification in the one existing M6 lifecycle: ESP unknown; manual retained context; observed controller loss/restart C5Y; first ACKed 059C offered initialization; standalone successfully sent 085F ACK. Neither OEM internal acceptance nor transport ACK grants session ownership. No new TX sites, existing C5Y and HA entities preserved. Generic YAML parse and ZIP CRC PASS, target compile and live flash NOT RUN. HA writes ON HOLD. SHA256 f65d6d37e805ce58e31631175df8ac2236e2275ccca0d68978a0b5850e3869c7.

## 2026-10-25 C5AF — PREPARED / NOT RUN

C5AE LIVE: only zero-payload FC16 085F/5 repeated, zero TX, zero parser-resync and CRC errors, no config first ACK. C5AF private complete ZIP prepared from C5AE with one guarded first 085F ACK after two matching frames <=5 s during existing stage40 initial 55s, through sole S92 owner, one attempt; no owner acceptance, cache or FC03 advancement and HA parameter writes ON HOLD. C5Y cold-start untouched. Offline YAML parser and ZIP CRC pass, not compiled/flashed/live. YAML SHA256 ce1dedafff7fd31b7c64cf13d9fa0d0a8cd91632418161a60d70320657ce7f15. ONE next action: user-initiated bounded C5AF first 085F test; ABORT and baseline C1C3 rollback included.


## 2026-10-25 — C5AD first 059C cold join — PREPARED / NOT RUN

Complete private source ZIP: THERMIA_MAIN03_C5AD_FIRST_059C_COLD_JOIN_PRIVATE_20261025.zip. Based on C5AC. A repeated exact 059C/count33 can now initiate the one-shot guarded cold-join ACK within the existing stage40 window without waiting for 04A6. The sparse follow-up remains separate from the previously live-positive C5Y ordered cold-start. Same UART/DE owner and all RX/peer/collision guards. No session acceptance from ACK alone; no HA parameter writes. Generic YAML parse and ZIP CRC checked; ESPHome compile and live test not performed. User initiation, abort and rollback documented. SHA256 YAML c742240b21b4b334c4c5ada0a619c52a5aeb5f33711e0af728265653a0a8efc8.

## 2026-10-25 — C5AB first cold-join R4 candidate — PREPARED / NOT RUN

Integrated private firmware ZIP `THERMIA_MAIN03_C5AB_COLD_JOIN_R4_PRIVATE_20261025.zip` derived directly from C5AA (original C5Y live-positive automatic controller cold recovery unchanged). In the existing S92 single UART/DE owner, the automatic 04A6/count13 R4 arm no longer requires a *previous* FC16 ACK to attempt the first response: one-time attempt only if stage40, active fresh ESP-start epoch, at least two exact 04A6 frames, no prior session TX/FC03, within 55s of arm, no competing peer/unknown frames, no parser resync/drop delta, zero HA pending writes, all unchanged S92 TX guards; existing 12s R4 armed TTL and exact `04BA..06F4` export continuation required. ACK is NOT semantic acceptance. FC23 cold challenge state guard unchanged, 042E/080C path unchanged, HA parameter writes ON HOLD. Offline YAML parser/ZIP CRC PASS, central TX-owner call count unchanged, target compilation and live flash NOT RUN. SHA256 YAML 6bf0407b922b6e27b748e22e757f975095c80f992058df2581611befb97f0401. Critical distinction: earlier C5AA first trial did not verify that a DCM session existed before OTA reboot, so it cannot establish hot-rejoin failure from a healthy session; new R4 cold join is hypothesis pending one bounded user initiated test, not proven OEM parity.

---

## 2026-10-25 — C5AA bounded first retained FC16 response — PREPARED / NOT RUN

Private complete ZIP `THERMIA_MAIN03_C5AA_RETAINED_FIRST_ACK_PRIVATE_20261025.zip` based on C5Z: in the existing sole S92 RX/TX/DE engine, after two matching CRC-valid exact `042E/count15` (39-byte request) or `080C/count18` (45-byte request) FC16 frames within 5s during existing 60-second stage40 boot retained window, permit ONE standard FC16 address/count ACK per ESP boot via the existing central sender. Prechecks: active/current session arm epoch, no queued setting write, no recovery/resume, no peer presence/unknown frames, no RX resync/drop delta; physical writer retains CRC/framing/DE/collision restrictions. No controller authority or FC03 permission is promoted by the experimental ACK; following native traffic and semantics must qualify any runtime. C5Y automatic WP cold-start path untouched. HA settings/parameter writes ON HOLD. Offline YAML syntax parsing (secrets tags normalized for generic parser) and ZIP CRC PASS; target compilation NOT RUN, physical flash NOT RUN, live verification NOT RUN. Experiment bounded and user-initiated by manual flash only; ABORT/rollback included. Need to evaluate whether one ACK changes controller continuation; do NOT claim full OEM-equivalent hot-rejoin. Prior C5Z complete negative had only 042E/080C repeated, 0 TX, no 07E4. YAML SHA256 c874e8951ff8fa2e6bae235a1f360691ed89f1196c68948cf21d256a3019eb49.

---

## 2026-10-25 — C5Z targeted ESP retained hot-rejoin opportunity — PREPARED / NOT RUN

Private complete source ZIP `THERMIA_MAIN03_C5Z_LATE_EXP315_HOT_REJOIN_PRIVATE_20261025.zip` is based on C5Y. One functional correction: existing automatic EXP315 first-request passive opportunity extends from 12 to 60 seconds to allow delayed exact 07E4/count17 requests. Existing requirement for two exact frames within 5s and one bounded guarded ACK remains unchanged. No new TX frames or physical TX owner; S92 UART/DE/CRC/collision guards preserved; original C5Y automatic controller cold-start unchanged (locally COMPLETE / POSITIVE). Firmware build text updated from stale C5 to C5Z. Offline YAML parser PASS, ZIP integrity PASS, 75 owner TX send sites unchanged. SHA256 YAML `42cd496266d0d2d31988510f7fbcd91c3892d7971c6746e8ea4399be58ff8507`. No compilation or flash of C5Z. IMPORTANT: alarm-state user trace showed only repeated 085F/0800 and FC03 polls, not 07E4: C5Z cannot restore that state, so full ESP hot-rejoin remains OPEN, not live validated. Must not repeat a trial while controller is in Online alarm; rollback C1C3. The existing C5Y parser resync/refresh issue also remains open. HA parameter writes ON HOLD. Next action one user-initiated bounded C5Z trial only on healthy alarm-free session, or pursue OEM-equivalent 085F lifecycle classification if no 07E4 appears.

---

## 2026-10-25 — C5Y controller-reboot autonomous recovery LIVE COMPLETE / POSITIVE (bounded scope)

User confirms C5Y actually flashed (build label still says C5; stale metadata), and WP reboot was deliberately done after existing Online alarm. User log 02:44:55 bus silence 5147ms -> recovery armed with TX=0, 02:44:58 first controller frame -> verified cold return, A80E=0000/A80F=0005, 02:44:59 FC23 dynamic guarded response executed, controller 03E8 export and ordered ACKs continued to 06F4/count19 at 02:45:32. 02:45:33 log `RECOVERY_POSITIVE success=1 runtimeFC16ACK=1 idle0708=1` followed by continuing native stage40 FC16 including 07E4. Physical session response evidenced, with no HA parameter writes. Thus AUTO WP/controller cold recovery of C5Y is LIVE COMPLETE / POSITIVE, but ESP-only hot-rejoin not proven: earlier alarm-state ESP reboot log showed 085F(0800) repeats and FC03 withheld. Caveat parser resync counter climbed to 6 during ensuing runtime; EXP378 secondary refresh aborted on resync delta, so full OEM-parity/refresh and error-free runtime are NOT validated. Do not label whole C5Y production ready. Build string stale and several diagnostic states still wrongly display MANUAL SESSION despite autonomous recovery; correct metadata/status in next integrated source change. No new experiments needed to re-prove cold route; next action targeted fix for ESP-only retained session rejoin without extra handshake or invented owner, based on verified EXP315/R4 context, keep collision/CRC guards, HA parameter writes ON HOLD.

---

## 2026-10-25 — C5Y bounded automatic boot start and retained recovery — PREPARED / NOT RUN

Private integrated firmware ZIP `THERMIA_MAIN03_C5Y_AUTO_RECOVERY_PRIVATE_20261025.zip` built from C5X retaining locally LIVE C1C3 baseline. C5Y removes the need to click native START on initial ESP boot: one delayed `button.press` invokes the existing S92 start code (not a second state engine). One automatic bounded 12-second EXP315 `07E4/17` two-observation arm is set on healthy retained stage40; one R4 `04A6/count13` arm is set only after existing clean context (>=1 runtime FC16 ACK, >=2 exact 04A6, no prior 0708, no pending semantic/peer/integrity fault). Both use existing central UART/DE TX writer and no new frame; HA parameter writes stay ON HOLD. Controller power-loss/cold-start path in existing S92 remains as before. YAML parsed and ZIP CRC tested offline; existing central sender reference count 75 unchanged. SHA256 `6d509810167292d52bb59139cd09bf9ab4e58225b77128df41e038291456bf1c`. Not compiled, not flashed, not live validated; explicit bounded user-initiated physical trial via manually flashing this private build is required. This is not full always-successful buttonless OEM rejoin, nor production release. Unknown/no qualifying frame stays NO_TX; after controller online alarm ABORT/rollback to C1C3. Next action one bounded C5Y live validation only after user review and manual flashing; do not declare semantically accepted on ACK alone.

---

## 2026-10-25 — C5X OEM parity guarded owner cleanup — PREPARED / NOT RUN

Private integrated source-only ZIP `THERMIA_MAIN03_C5X_OEM_PARITY_CLEANUP_PRIVATE_20261025.zip`, based on C5V source-only via latest locally LIVE C1C3 baseline. Concrete cross-guard consistency correction: when EXP315 handoff has actually sent a guarded 07E4 ACK it records `c5v_07e4_handoff_epoch`. RX-side FC03 export provenance already recognized that physical handoff, but the sole UART/DE writer FC03 owner and RX FC03 owner conditions depended on temporary `s92_rejoin_approved`; C5X also recognizes the existing current-session epoch at those checks. No way to create the epoch was added, no new physical TX, no frame changes, no bypass of CRC/peer/stage40/received FC16/collision precautions. Existing R4 and cold-start remain untouched. YAML parsed offline; ZIP CRC pass; 77 central TX owner references unchanged. SHA256 YAML 7c48ae3e91cd79fd3888c174544ee28e8e81948a2ce7c13acae07d763782dbe6. Not target compiled, not flashed, not live verified. This is a targeted correction, NOT a full firmware dead-code removal or automatic buttonless recovery release. Removing historical EXP handlers globally requires verified dependency analysis and target build to preserve production HA entities. Keep HA parameter writes ON HOLD. Next action: implement OEM-equivalent automatic two-route controller/ESP restart qualification under defined bounded user-initiated TX validation; no autonomous unvalidated TX.

---

## 2026-10-25 — C5 two fully automatic recovery paths: user requirement / PREPARED / NOT RUN

Explicit product requirement: (1) after WP/controller restart with ESP continuously powered, automatically detect cold boot and start/restore DCM without a HA button; (2) after ESP flash/reboot with WP continuously powered, automatically detect retained controller phase and resume DCM without a HA button. Both must use ONE existing UART/RX/DE/TX owner and locally proven existing protocol frames, preserve cold-start, FC16/FC03, V5 CRC, B11C/B11D, ABORT and controller interlocks, and keep HA parameter writes ON HOLD. Evidence: EXP355 controller cold return; EXP315 direct 07E4/17 retained node (second exact request, 6 loops); S92-R4 contextual 04A6 with 085F followup; EXP363 one-shot 04A6 ACK followed by config export; EXP364 full export remains PREPARED/NOT RUN. Current C1C3/C5U still manual-arm TX; existing EXP315/R4 route presence is not automatic recovery proof. Engineering scope is to consolidate automatic *classification* and grounded authorization with bounded retries and cold fallback, without assuming FC16 observation alone gives TX ownership. New/unvalidated physical auto TX must be introduced only after appropriately bounded user-initiated live authorization, not quietly in source. No new firmware flashed, compiled or live tested by this requirement update.

---

## 2026-10-25 C5 native requalification integration decision — NO-GO without controller authorization evidence

Concrete source-to-LIVE cross-check on C5T against single C5 ESP-only restart capture: post-reboot at 01:10:11 `BOOT_RX_ONLY / OWNER NOT INHERITED / TX LOCKED`, then `FC03=0 RX0708=0 physicalTXthisSession=0` through the pre-alarm window (sample at 01:11:06); user-reported Online alarm at 01:11:30-35. Passive recognized native FC16 arises around 01:11:33, after reported alarm boundary, not as prior authorized rejoin. C5T OEM_INTERNAL_ACCEPTED is a logical software state, but guarded native owner/epoch (`write_arm_ms`, `main01_native_accepted_epoch`, `s92_rejoin_approved`) remains unqualified; no controller-issued, qualified 0708 response/re-acceptance path has been verified in that window. Engineering decision: NO-GO for bridging passive FC16 to owner authorization or adding automatic physical TX; preserve last locally LIVE C1C3 and source-only C5T. Do not falsely label C5T a hot-rejoin fix. One next engineering action is isolate evidence of OEM mid-session controller-authorized response opportunity, preferably from existing original Connect traces; without that, bounded user-initiated test plan rather than automatic takeover. No flash or live retest. HA parameter writes still ON HOLD.

---

## 2026-10-25 — MAIN03-C5R OEM internal lifecycle reset — PREPARED / NOT RUN

One complete private firmware ZIP `THERMIA_MAIN03_C5R_OEM_LIFECYCLE_PRIVATE_20261025.zip` built from original user-LIVE C1C3 and source-only C5. Corrected one actual C5 state-coherence defect: internal OEM ACCEPTED/FC16 source is invalidated on native session authority revocation, manual START/ABORT and boot. Original valid FC16 OEM acceptance exceptions 085F/04BA and successful-FC23 RESPONSE_SENT unchanged. Single UART/DE owner, TX guards and 75 send occurrences preserved. YAML parsed offline with ESPHome secret-tag handling; no target compilation, flash, live testing, no HA parameter writes. SHA256 YAML `f0bad49ac29d36b8f9b0852d7ab3fb240d2b3e38d7daf9772b5749acb956f8f5`. Status PREPARED / NOT RUN. This is NOT physical hot-rejoin restoration: owner remains UNKNOWN after ESP reboot and alarm is known; no new TX permission inferred from internal acceptance. C5 remains REAL BLOCKER; do not flash merely to repeat failed restart.

---

## 2026-10-25 — MAIN03-C5 OEM internal acceptance parity — PREPARED / NOT RUN

Produced private complete ZIP `THERMIA_MAIN03_C5_OEM_INTERNAL_ACCEPTANCE_PRIVATE_20261025.zip` from locally LIVE-proven MAIN03-C1C3 (not source-only C3A). OEM Connect 2.1.105 `_on_function16` equivalent internal state: NOT_ACCEPTED at ESP boot; RESPONSE_SENT after already-guarded FC23 physical response success; ACCEPTED upon valid controller FC16 excluding 0x085F and 0x04BA. Internal state is NOT native owner/TX permission; no sender, UART/DE or safety-guard changes. One read-only diagnostic entity. YAML parsed offline, existing native send call count 75 unchanged. Full target compile, flash and XTR live verification NOT performed. This is an internal parity correction, NOT an autonomous hot-rejoin fix; online alarm/hot-rejoin remain REAL BLOCKER. No flash into current alarm/qualified session, HA writes on hold. Status PREPARED / NOT RUN.

---

## 2026-10-25 C5 post-restart timing clarification — LIVE evidence

Single ESP-only restart on MAIN03-C1C3: pre-reboot last qualified traffic approximately 01:09:38; post-reboot `BOOT_RX_ONLY / OWNER NOT INHERITED / TX LOCKED` by 01:10:11. User observed Online communication alarm approximately 01:11:30–35. Passive `NATIVE FC16 OBSERVED / SESSION OWNER UNKNOWN / TX LOCKED` first reported 01:11:33.281, after the reported alarm boundary; known FC16 shapes reached 25 by 01:12:20. No accepted new handshake is evidenced in this log. Native frame reception after alarm is NOT warm-session ownership. ~112-117 s to reported alarm supports an approximately two-minute monitoring timeout as a hypothesis, not an OEM-confirmed timing contract. C5 remains COMPLETE / NEGATIVE; do not promote FC16 observation to TX authority. OEM source initializes NOT_ACCEPTED and requires subsequent handshake acceptance evidence but does not prove warm takeover. Engineering NO-GO for unqualified physical auto-TX; retain last locally verified C1C3 and guarded cold-start. No new flash or test performed.

---

## 2026-10-25 — C5 ESP-only hot-rejoin LIVE NEGATIVE / alarm

Baseline: user-live MAIN03-C1C3, qualified stage40, alarm-free before ESP restart. One user-initiated ESP restart while controller stayed powered. Subsequent uploaded log showed M6 BOOT_RX_ONLY / OWNER NOT INHERITED / TX LOCKED; passive native FC16 candidate remained OWNER UNKNOWN. No native owner promotion or verified resumed FC03/FC16 service. User directly observed controller Online-module communication alarm around 01:11:30–01:11:35. Classification COMPLETE / NEGATIVE for unattended ESP-only hot-rejoin on this exact firmware. Distinguish direct alarm report from bus log. Prior FRESH_BOOT_RUNTIME_QUALIFIED entries were from pre-restart retained runtime, not this ESP restart. Fail-closed TX is correct but operational alarm is a REAL BLOCKER. Do not try repeated ESP/controller restarts, START, refresh, or unqualified TX; settings writes remain on hold. No new firmware flashed or experimentally validated. Next engineering decision: retain single UART/DE owner and cold-start baseline; require evidence-based, controller-approved mid-session session handover/rejoin mechanism, with hard stop, before enabling physical TX. Existing C3A is source-only and NOT a C5 repair.

---

## 2026-10-25 — MAIN03-C3S — PREPARED / NOT RUN (no live experiment) (SOURCE / OFFLINE TESTED, PREPARED / NOT RUN)

From complete original C1C3 baseline plus source-only C3 atomic staging, produced ONE private firmware ZIP `THERMIA_MAIN03_C3S_REFRESH_SCHEDULER_PRIVATE_20261025.zip` (YAML SHA256 `4f7eada4eaa8cae068553ab74fe48a4c31ae9a5c005e353b6a540fd95e773b81`). Adds a single 30s passive scheduler tick that declares the *accepted* atomic CURRENT snapshot due at 240s, only with existing qualified S92 session/2.4.2 profile/integrity/idle guards; logs once per generation. 240s is a local planning threshold, NOT OEM cadence evidence. Scheduler cannot arm the read button or TX, and creates no second UART owner or new frame. Physical autonomous TX remains NOT AUTHORIZED. Existing user-initiated C3 native refresh stays the only enabled path, previous 300s TTL unchanged; exact 9 Configuration buttons, one UART writer and 75 native send calls preserved. Offline YAML/substitutions/entity parity tests passed; no target compile, flash, new XTR LIVE observation. **Do not flash over an active qualified DCM session**: ESP-only hot-rejoin remains unproven. The next functional step is a separately authorized bounded automatic physical read experiment, not an autonomous flash or parameter writes.

---

## MAIN03-C3-ONE-SHOT-01 — COMPLETE / POSITIVE (2026-10-25)

- **Hypothesis:** One explicit native read-only four-page request during an already qualified S92 runtime will re-export and owner-ACK H/D/C/M and advance local atomic snapshot generation.
- **Baseline:** User-FLASHED/LIVE MAIN03-C1C3, manual cold-return session, stage40, ~45min runtime, `snapGen=1`, last CURRENT stale, normal FC03/0708 and runtime FC16 acknowledgements; no evidence of spontaneous second four-page cycle.
- **ONE change:** User presses `MAIN01 | Arm One-Shot Four-Page CURRENT Refresh`. Physical TX only as previously guarded response to subsequent controller poll, no independent master TX.
- **Expected:** W2/W3 read-only demand, controller H/D/C/M FC16, owner ACK, `snapGen=2` within existing 60s timeout; abort on safety alarm/session loss.
- **Actual:** 00:52:50.691 PRESS_RECEIVED count=1; 00:52:53.925 `FOUR_PAGE_CURRENT_REQUEST_TX W2=0001 W3=0019`; H/03E8 00:52:54.068, D/042E 00:52:54.592, C/0442 00:52:56.170, M/0546 00:52:56.877, all native ACK; `CURRENT_4PAGE_CONFIRMED` 00:52:56.884; 00:53:01.439 `snapGen=2`, `FRESH`, `receiptPages=4/4`, `ackMask=0F`, `confirmed=1`, `button=1`, `denied=0`. CRC_DIFF/resync/drops 0; no parameter writes or restart.
- **Conclusion:** COMPLETE / POSITIVE for user-initiated native C3 fresh four-page re-export. Autonomous scheduler remains source-design only, not authorized for physical auto-TX or claimed LIVE.
- **Abort/rollback:** Existing S92 STOP/RX ONLY and fail-closed guards; no abort triggered; preserve currently qualified firmware/session; no unsolicited OTA/controller restart.

---

