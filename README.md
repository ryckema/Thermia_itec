## 2026-10-26 — C5BE targeted retained hot-rejoin lifecycle fix — PREPARED / NOT RUN

C5BD user LIVE after ESPHome OTA reboot (controller did not restart) manually S92-armed at 01:20:16. Controller offered genuine FC16 0864/4 at 01:20:17, 0870/17 at 01:20:19 and subsequently 0884/60, 07D0/19, 07E4/17, 07F8/17, 080C/18, 0820/18 by 01:20:34. All eight were physically ACKed; no owner/profile, zero FC03 replies, H/D/C/M 0/4. The old C5AL 15s expiry since 0870 fired at 01:20:34 even as controller offered new pages: real EARLY STOP lifecycle defect. OEM 0870 was genuinely ACKed; misleading got0870=0 came from m6_revoke_stop() clearing c5al_followup_0870_ms before logging. C5BD result COMPLETE / INCONCLUSIVE for actual hot-rejoin, but exposed two SOURCE-corroborated defects.

C5BE PRIVATE full firmware starts from exact user-LIVE C5BD complete YAML and makes one integrated lifecycle repair: if real subsequent FC16 ACK occurred AFTER genuine 0870 ACK within same manually started S92 run, suppress only the narrow C5AL 15s idle-candidate stop; retain original FIX18 60s total retained-session cap, all runtime owner/epoch/profile, CRC/parser/DE/peer/dirty, ABORT and one UART owner. When no real continuation, existing 12s/15s idle expiry unchanged. Snapshot got0870/ack count before reset for truthful logging. This is NOT automatic owner promotion, more TX budget, or guaranteed hot-rejoin. C5BD CURRENT refresh arming fix and LEGACY_03E8 diagnostic distinction preserved; HA writes ON HOLD. Complete private ZIP THERMIA_MAIN03_C5BE_HOT_REJOIN_PROGRESS_LIFECYCLE_PRIVATE_20261026.zip, ZIP SHA256 7c0fb424af755f871fb14399ad243e916c460b9cbcc3901044273441a3166d0e, YAML SHA256 f8f091086e896230c8550ba809942cb7595dc4e5f39057e9fabe0fe3c1324f2a. YAML parse, standalone IDs uniqueness, sole UART writer, ZIP CRC PASS. SOURCE / OFFLINE TESTED, PREPARED / NOT RUN; NOT TARGET COMPILED/FLASHED/LIVE. C5AR last earlier fully LOCALLY VERIFIED cold-start rollback; C5BC cold-start user-LIVE full 4/4. No new controller-reset test needed.

CURRENT MILESTONE: C5 native hot-rejoin recovery after full cold-start preservation. DELIVERABLE: C5BE full private integrated source ZIP. REAL BLOCKER: acceptance/0708/FC03 and fresh H/D/C/M after ESP-only rejoin remains OPEN; C5BD stopped prematurely during valid real FC16 continuation. ONE NEXT ACTION: user initiates ONE bounded C5BE S92 live experiment on running controller, no controller reset, ABORT and rollback C5AR if needed; assess true continuation/ownership by physical frames not ACK alone.

---

## 2026-10-26 — C5BD native four-CURRENT refresh owner parity: PREPARED / NOT RUN

User requested consolidating the already user-LIVE C5BC controller-cold-start success and fixing FC03-refresh/cache freshness, then returning to hot-rejoin. C5BC live after real controller restart showed native FC23, full 32-page FC16 config, XTR 2.4.2 profile, RUNTIME/SYNCED H/D/C/M 4/4 through end of observed log. Optional diagnostic 03E8 cache was separately stale/missing. Last prior fully locally verified C5AR rollback.

Concrete source defect in the full C5BC YAML: manual 'MAIN01 | Arm One-Shot Four-Page CURRENT Refresh' button required rejoin approval or a recovery runtime token EVEN when the same-epoch native controller cold-start was fully qualified, while the existing sole S92 TX dispatcher already required valid native owner, profile 242, correct epoch, runtime FC16 and FC03 and CRC/collision/dirty guards. In C5BD PRIVATE exact-C5BC full YAML only the redundant hot-rejoin-specific gate on the CURRENT refresh button was removed, not the genuine owner/profile/runtime/integrity gates. The user button itself has no TX. The existing future real controller 0708, existing 60s arm, 12-cycle budget, cooldown and FC16 four-page receipt gates remain. No HA setting writes or synthetic cache freshness. Diagnostic string now truthfully identifies optional legacy 03E8 freshness as LEGACY_03E8_FRESH/MISSING, separately from authoritative H/D/C/M snapshot; this is a reporting clarification, not a received diagnostic refresh.

Complete PRIVATE ZIP THERMIA_MAIN03_C5BD_FC03_REFRESH_OWNER_PARITY_PRIVATE_20261026.zip, YAML SHA256 fb12123fdf5c286e17e1b1eff601d0483ed0d6e7d9c3d8b0b15ab0af3950568b, ZIP SHA256 40ddcb043f031568b61613c5ed3018fb891b5cafadf88b8654923e41c0ebcf5c. YAML !secret-aware offline parse PASS, declared IDs unique, one physical UART write_array, ZIP integrity PASS. SOURCE / OFFLINE TESTED, PREPARED / NOT RUN; no target compile, flash, user LIVE or hardware TX. C5BC code's normal alarm-only and controller cold-start routes otherwise retained; C5AR rollback. Existing explicit user S92 START and ABORT; room sensor retained; HA parameter writes HOLD.

No extra cold-start is claimed or required for offline preparation. A valid controller-native session is prerequisite before future user-initiated refresh validation; ESP flash itself may lose previous session ownership. Never arm refresh on an unqualified retained/ownerless attach. After one relevant live refresh validation return to parked hot-rejoin engineering (C5AU/C5AZ observations), NOT repeat the C5BC alarm-idle loop.

CURRENT MILESTONE: C5 native session/FC03 cache freshness before hot-rejoin. DELIVERABLE: C5BD full firmware source zip, PREPARED / NOT RUN. REAL BLOCKER: user-LIVE validation of future real 0708 read request and resulting four new FC16 receipts; optional 03E8 diagnostic remains nonessential, not fabricated. ONE NEXT ACTION: verify C5BD in one bounded user-initiated already-qualified native session, then proceed to hot-rejoin using OEM/local evidence.

---
## 2026-10-26 — C5 controller-offered configuration versus alarm-only entry: NO-GO further idle TX

C5AZ user LIVE received normal controller-offered config pages and then a real information response (2/5); C5BC user LIVE served 12 real idle reads in an alarm-only session and received no new config/info pages: COMPLETE / NEGATIVE for blank-read progression. Genuine XTR DCM capture 2026-10-03 begins with controller-offered ordinary config pages before alarm and later read polling. The private original Connect CM slave separates alarm-only receipt from internal handshake qualification; its source does not establish a safe unsolicited recovery-start message. STRONGLY SUPPORTED: the normal controller-generated configuration-entry phase is absent from these alarm-only runs. No evidence warrants additional repeated replies, forced accepted-owner, or fabricated controller epoch. Decision NO-GO for further alarm-only idle reply variants. Preserve last LOCALLY VERIFIED C5AR native controller-cold-start and C5AZ scoped running-controller continuation evidence. HA parameter writes HOLD; one UART/DE owner and ABORT remain.

CURRENT MILESTONE: C5 reliable native session attach/recovery on running XTR. DELIVERABLE: OEM/local source comparison and explicit NO-GO for repeated blank-read approach, no new firmware. REAL BLOCKER: no genuine controller configuration-entry/identity offer in alarm-only retained context. ONE NEXT ACTION: implement only if additional real XTR controller event or OEM evidence demonstrates supported native rejoin entry; otherwise retain RX-only and previously verified cold-start path, not another duplicate live experiment.

---

## 2026-10-26 — C5BC live repeated empty reads: COMPLETE / NEGATIVE for session advancement

USER FLASHED/LIVE C5BC on running XTR. S92 manual START 00:59:30.096; real 085F/5 ACK 00:59:32.063; initial alarm-only empty FC03 reply 00:59:35.755; 11 genuine repeated controller 0708 polls received and empty responses sent 00:59:40.037–01:00:22.956. Controller offered 14 total 0708 requests, 12 served, two withheld (one early before 085F response provenance and one later). 28 observed 085F FC16 packets, first ACKed and subsequent zeros left unanswered. Exactly 13 physical TX (one FC16 ACK + 12 FC03 responses), no normal qualifying 042E/0442/0546/0662 pages, no identity INFO receipts, no native owner/profile/accepted session and H/D/C/M 0/4, CONFIG NOT_SYNCED. Existing safe timeout 01:00:30.228 age60064ms RX_ONLY and DE LOW. CRC_DIFF0, resync0, drops0. `C5BC repeated-empty-read advances alarm-first controller session` is COMPLETE / NEGATIVE; bounded real-FC03 physical response and safe expiry COMPLETE / POSITIVE. Do not continue microtests for identical idle responses. C5AZ previous first config→info 2/5 remains strongest running-controller LIVE. C5AR last fully LOCALLY VERIFIED cold-start; no HA setting writes.

CONCLUSION: normal OEM repeated empty FC03 servicing alone does not progress current XTR alarm-first state. This is not proof of failed bus transport or disproval of normal 0708 read response. Need one evidence-backed consolidated source correction for distinguishing controller's accepted protocol/normal config-first versus alarm-only state, or explicit NO-GO if OEM and genuine captures do not support trigger. Do not invent owner, handshake, controller epoch, unsolicited startup or stricter hypothetical lockouts.

CURRENT MILESTONE: C5 running-controller native first join. DELIVERABLE: C5BC live result COMPLETE / NEGATIVE for empty-poll progression, SOURCE now user LIVE. REAL BLOCKER: controller stays alarm-only despite 12 genuine 0708 responses; no qualifying native config or INFO. ONE NEXT ACTION: revisit original OEM/controller DCM sequencing vs known successful C5AZ route to choose one integrated change or NO-GO. C5AU/C5AS parked; HA parameter writes HOLD.

---

## 2026-10-26 — C5BB alarm-first OEM idle FC03 user LIVE — COMPLETE / INCONCLUSIVE (full native join)

OBSERVED FACTS: complete user C5BB log 00:46:00.702 manual S92 start; first actual controller 085F/5 ACK at 00:46:02.542; first genuinely offered FC03 0708/6 served by C5BB one-shot OEM empty read at 00:46:04.115. Subsequent controller behavior remained alarm-only: 28 total FC16 085F/5 (one first ACK and 27 zero-valued repeats no ACK), 14 genuine 0708 polls total, first answered and 13 blocked by FIX21. There was no 042E/0442 config prefix, no requested native INFO pages or H/D/C/M refresh. Exactly two physical TX, expiry after 60064ms at 00:47:00.775, SESSION_LOST / RX ONLY / DE LOW; CRC_DIFF=0, in-run resync=0 and RX drops=0. Native OEM_INTERNAL NOT_ACCEPTED, profile/owner UNPROVEN, H/D/C/M 0/4, HA parameter writes HOLD. C5BB scoped FC03 idle-read send and safe expiry COMPLETE / POSITIVE, session progression after empty read COMPLETE / INCONCLUSIVE (no continuation).

STRONG CONCLUSION: ordinary alarm-first controller FC03 can be physically serviced with OEM-aligned blank response, but first blank response alone does not lead to normal configuration flow. Original OEM slave read being available without handshake does not prove 2.4.2 owner qualification from such a read. Unlike C5AZ (real first normal config prefix, OEM info request, 2/5 info receipts), C5BB produces no information progress and FIX21 blocks remaining read polls. A single 085F packet must NOT grant owner or justify unbounded TX. The user's confirmed DCM-missing communication alarm is not treated as an independent blocker; still retain real bus protections. Full prior verified native cold-start rollback = C5AR.

DECISION: do NOT repeat isolated ACK/blank poll microtest; investigate this exact interrupted/alarm-only controller state against locally captured genuine DCM and OEM request-cycle sequencing, then one integrated evidence-backed normal protocol/lifecycle fix or explicit NO-GO. Do not invent controller epoch, authentication, unsolicited master TX or parameter writes.

CURRENT MILESTONE: C5 running-controller first native join. DELIVERABLE: C5BB LIVE result assessed, no new firmware yet. REAL BLOCKER: alarm-only poll sequence cannot reach qualifying real configuration/identity data. ONE NEXT ACTION: reconcile OEM recurring idle FC03 handling with genuine XTR running-controller captures and route in one native engine; implement only evidenced single integrated correction, with ABORT/rollback.

---

## 2026-10-26 — C5BB OEM alarm-first FC03 read correction — PREPARED / NOT RUN

OBSERVED FACTS (XTR C5BA user LIVE): controller offered alarm FC16 085F/5 and genuine FC03 0708/6 after first 085F ACK; no qualifying ordinary 042E/0442 config-prefix and existing FIX21 withheld the 0708 response. C5BA INFO_PENDING branch was never entered. C5AZ previously yielded qualified normal FC16 prefix, 0708 and two received INFO pages (2/5). User states display communication warning derives from missing DCM, not a separate heating failure; user wishes project to continue. C5AR remains last locally verified full controller-cold-start native baseline.

OEM SOURCE 2018/2.1.105 review: original Connect Modbus RTU slave allows ordinary FC03 reads independently of internal handshake flag. Alarm page 085F alone is excluded from normal handshake acceptance and cannot source missing-INFO request flags. Native read register initialization is empty; normal qualification requires later controller evidence. OEM source does NOT prove XTR accepts a zero read at this specific ownerless entry point.

ONE integrated PRIVATE C5BB SOURCE fix from exact C5BA: after user-started stage40 S92 session and physically ACKed single known 085F, if controller really offers an exact CRC-good 0708/6 without normal config prefix, issue at most ONE OEM-aligned six-word empty FC03 response; no pending request flags, no invented handshake, no assumed owner. The same sole S92 UART/DE writer, CRC, peer/collision, dirty, epoch, 55s window, 60s failback, abort/rollback and HA parameter-write HOLD remain. The TX success path explicitly excludes this alarm-only transport response from native M6 session promotion or H/D/C/M freshness. Existing C5AZ normal prefix and C5BA information followup are preserved. PRIVATE ZIP `THERMIA_MAIN03_C5BB_OEM_ALARM_FIRST_PRIVATE_20261026.zip` (SHA256 37683314163db7902d9cf7db4805ffe1ec8df1455bcd32788ca82943473d3934), full YAML SHA256 ec373ba040573e8ab3b804c8fe8bb1b06341b2bcf7a188dcfc9352d3c8f7830a; README, manifest, source. YAML syntax parsed, ID uniqueness and sole UART write_array checked, archive integrity verified. SOURCE / OFFLINE TESTED, **PREPARED / NOT RUN**: not target compiled, user flashed or LIVE.

CURRENT MILESTONE: C5 native first join on already-running XTR. DELIVERABLE: OEM/XTR compared and one C5BB private full firmware ZIP prepared. REAL BLOCKER: no verified semantic native owner/profile/4/4 on running XTR; alarm-only 0708 read response is not XTR live validated. ONE NEXT ACTION: user executes one bounded manual S92 C5BB trial with complete log and ABORT/rollback C5AR; classify GO/FIX/NO-GO from controller continuation. C5AU/C5AS parked.

---

## 2026-10-26 — C5BA first manual live after DCM absence: COMPLETE / INCONCLUSIVE

User confirmed the controller-display communication warning concerns loss of expected DCM responses. Treat as expected communication-context feedback, not an unrelated heat-pump fault or reason to invent new TX authorization. User explicitly requested continuation without treating this display error as an independent blocker; retain electrical, collision, protocol guards and HA writes HOLD.

User C5BA LIVE at 00:31:10 manual S92 stage40: first received 085F/5 (one physical ACK) then genuine controller FC03 0708/6 at 00:31:13.765, explicitly FIX21 0708_UNQUALIFIED_NO_REPLY; zero qualifying normal FC16 042E/0442 prefix, no C5AZ INFO_FIRST read or C5BA INFO_PENDING continuation. Source C5BA follow-up requires previous genuinely served first read, c5ax_info_acked_mask nonzero and different from last mask, exact same-epoch c5az normal prefix anchor, and all original S92 guards. This run did not reach that branch, so C5BA new capability **COMPLETE / INCONCLUSIVE**, not protocol negative. Native owner unverified, H/D/C/M 0/4. Last fully LOCALLY VERIFIED session startup C5AR; C5AZ prior observed normal first prefix→0708→2/5 information pages, scoped COMPLETE / POSITIVE.

**Decision:** do not remove FIX21, synthesize session owner, or turn a lone 085F alarm page into protocol authority. No extra ACK-only experiment. Next action: source-level identify original OEM handling of first FC03 after an alarm-only attach, compare with XTR controller offered actual frames, then IMPLEMENT smallest warranted normal protocol response in same S92 engine if evidence supports; otherwise explicit NO-GO and retain C5BA source. Existing controls keep user-initiated, bounded and parameter writes HOLD.

CURRENT MILESTONE: C5 first native running-controller join. DELIVERABLE: C5BA live diagnosis with untriggered pending-info logic. REAL BLOCKER: controller gave no qualified config prefix before 0708; ownerless initial FC03 response rule not established. ONE NEXT ACTION: assess OEM alarm-first FC03 path against genuine XTR trace, then FIX or NO-GO; do not repeat untouched C5BA.

---

## 2026-10-26 C5AZ live result — scoped native INFO continuation COMPLETE / POSITIVE; full join COMPLETE / INCONCLUSIVE

User FLASHED/LIVE full C5AZ on running XTR M 2.4.2. Manual S92 START 00:13:39.795, bounded expiry 00:14:40.019 after 60216ms. Real 0442/13 physically ACKed 00:13:41.511; alarm 085F/5 once ACKed; genuine controller 0546/20 and 0662/33 offered and ACKed. Genuine controller FC03 0708/6 then served with OEM INFO_FIRST request 00:13:45.366; controller replied with requested 0532/18 and 06F1/3, both physically ACKed: info receipt mask 03/1F = 2/5. Total 7 physical TX: 0442, 085F, 0546, 0662, 0708 response, two INFO ACKs. Total observed controller FC03 0708: 13, one response, twelve explicitly withheld by FIX21 0708_UNQUALIFIED_NO_REPLY because qualified owner/profile remained absent. No remaining three INFO groups or full native session, no H/D/C/M freshness (0/4), CONFIG NOT_SYNCED. Safe RX ONLY/DE LOW expiry, CRC_DIFF 0, parser resync 0, RX drops 0, HA parameter writes still HOLD. C5AZ flexible-first-page code path and associated real controller continuation COMPLETE / POSITIVE, full semantic cold join COMPLETE / INCONCLUSIVE. C5AR remains last locally verified full native cold-start. Real blocker is subsequent 0708 handling with outstanding OEM missing-info flags while session remains unqualified. ONE NEXT ACTION: one integrated private correction to the existing sole S92 FC03 engine for bounded genuine later 0708 polls and remaining INFO requests, derived from exact C5AZ and OEM source, preserving UART/DE, collision, peer, CRC, epoch, ABORT, rollback and no acceptedOwner promotion. No isolated ACK microtests or autonomous TX. C5AU/C5AS parked.

---

**2026-10-26 — C5AY XTR live result, C5AZ private source prepared.** Manual first attach started 2026-10-25 23:57:48: 56 controller 0442/13 packets, 28 alarm 085F/5 packets, no 042E or 0708. Exactly one first 085F ACK; C5AY continuation was not reached because its first-page anchor required 042E. Safe expiry after 60.084s, RX-only DE LOW, clean CRC/resync/drop, no native owner or fresh H/D/C/M (0/4). C5AY new route **COMPLETE / INCONCLUSIVE**, not triggered. One integrated private C5AZ candidate now prepared based on full user-live C5AY: normal bounded first page may be either locally verified 042E or 0442; subsequent actual controller-offered pages use same single S92 engine. No controller restart instruction, no new UART owner, no artificial session status, no HA parameter writes. Full private ZIP SOURCE/OFFLINE TESTED, **PREPARED / NOT RUN**; not ESPHome-target compiled, flashed or live. Last locally verified full native cold start remains C5AR. **CURRENT MILESTONE:** C5 running-controller cold join. **DELIVERABLE:** C5AY diagnosis and integrated C5AZ offline package. **REAL BLOCKER:** complete native profile/session and H/D/C/M 4/4 still unproven without controller reset. **ONE NEXT ACTION:** one bounded user-initiated manual C5AZ live test with ABORT and C5AR rollback.

**2026-10-25 23:25 — C5AX user FLASHED/LIVE first-attach info-first attempt: COMPLETE / INCONCLUSIVE (INFO branch NEVER TRIGGERED); bounded transport and expiry positive.** Actual 23:25:14.209 manual stage40 after ESP-only OTA; CRC-good FC16 042E/15 twice, physically ACKed once at 23:25:15.683 via C5AA; 085F/5 first nonzero packet ACK at 23:25:15.729 C5AN, then 54 identical 0442/13 offers **NO_ACK**, plus 27 more 085F (zero) NO_ACK. 84 captured controller FC16 total: 2x042E, 28x085F, 54x0442. NO 0848/23 and NO 0708/6 offered; C5AX INFO_FIRST_READ_SENT and INFO_PAGE_ACK_SENT never fired, FC03SERVED=0, two TX total, owner/profile=UNPROVEN, cache NOT_SYNCED H/D/C/M 0/4. At 23:26:14.414 manual 60.202s expiry: SESSION_LOST, RX_ONLY/DE LOW, CRC_DIFF0 and no incremental session parser resync/drops. Not a failed INFO request—request never sent.

**Concrete SOURCE gap (single S92 owner):** native 0442/13 is accepted and decoded as known controller settings/current page, but the C5AO first-attach list of 22 configuration export geometries starts at 04BA and excludes 0442. Existing EXP420 only ACKs 0442 with qualified runtime/selector owner, so during manual unqualified C5AX first attach it logs CONFIG_NO_OWNER and controller repeats endlessly. Historic local XTR EXP329 proves 042E ACK → 0442 ACK → 0456, and EXP426 qualified retained startup 042E → 0442 → 0546 → 03E8; that evidence does NOT prove success in current ownerless epoch but identifies specific missing native sequence handling. Do NOT retest isolated 0442 ACK, promote owner or invent controller startup. Need one integrated guarded first-attach FC16 prefix/continuation fix using existing S92 TX only when controller actually offers known frame after physically ACKed 042E in same manually approved epoch, plus real later 0708 OEM info handling. HA writes HOLD, preserve C5AR controller-cold-start. Last full locally PROVEN native baseline C5AR, last first-attach user LIVE C5AX; C5AU/C5AS parked.

CURRENT MILESTONE: C5 first native join on running XTR 2.4.2. DELIVERABLE: full C5AX log analysed and ownerless 0442 routing defect localized; C5AX experiment COMPLETE / INCONCLUSIVE, not false negative for untriggered INFO. REAL BLOCKER: repeated 0442/13 has no guarded first-attach owner; no controller 0848 or 0708 while stalled, no native identity/current acceptance. ONE NEXT ACTION: implement ONE integrated C5AY normal-FC16 prefix continuation from actual 042E ACK (0442 and OEM/local validated successor geometries) within existing bounded single-engine manual scope; keep C5AX info request conditional on genuine subsequent 0708, no HA writes/auto flash, then one user-initiated full live experiment.

**2026-10-25 — MAIN03-C5AX OEM INFO-FIRST integrated PRIVATE source prepared, PREPARED / NOT RUN.** Built from full last user-LIVE C5AW YAML; locally PROVEN controller cold-return remains C5AR. OEM 2.1.105 CM930 2.4.2 info/significant-register and flags source maps first information request to five exact locally observed XTR packet groups, rather than the C5AW erroneously labeled CURRENT-only request that actually selected SETTINGS. C5AX changes only the ONE manual first-attach 0708 response's request class and includes one-shot ACK of each real controller-offered exact information-page FC16 through existing sole S92 UART/RX/DE owner, maximum seven TX in new scope (one 0848, one 0708, five data ACKs). Existing CRC/framing/peer/collision/epoch/55s window/60s stop, ABORT and room-sensor topology remain; no unsolicited TX, no new owner, no fabricated XTR profile acceptance, no HA setting writes. Info receipt mask is transport accounting only, not actual native owner or H/D/C/M 4/4. Private full firmware ZIP `THERMIA_MAIN03_C5AX_OEM_INFO_FIRST_PRIVATE_20261025.zip`; YAML SHA256 `351fbba664d662447cf934fe12d2b51a890edddc71032148d408ed83dae8700f`, ZIP SHA256 `dbd7710aa78d7f44a7d7070fde46772260c0158e86f6630c01bf88f1a08ed67c`; complete YAML, README, manifest; offline YAML parsed, 620 unique globals, one UART write_array, ZIP CRC valid. ESPHome TARGET COMPILE NOT DONE, NOT FLASHED/LIVE; no new user experiment. **CURRENT MILESTONE:** C5 native cold join on running controller. **DELIVERABLE:** one complete private C5AX integrated source ZIP. **REAL BLOCKER:** no proven complete native session/owner and fresh H/D/C/M 4/4 after running-controller first-attach. **ONE NEXT ACTION:** user compiles/flashes C5AX and conducts exactly ONE guarded manual S92 info-first session with complete log, ABORT and C5AR rollback; decide GO/FIX/NO-GO. Hot rejoin C5AU and refresh C5AS remain parked.

**2026-10-25 — OEM CM930 reinit investigation: no sourced unsolicited controller restart; C5AW request-class defect (SOURCE + LIVE).** Two genuine original Connect gateway branches (2018 and 2.1.105) implement the controller bus as a passive Modbus RTU SLAVE. A genuine controller FC23 triggers its handshake response; an ordinary qualifying incoming FC16 can set OEM LOCAL handshake acceptance even without fresh FC23, then in WAITING_FOR_DEVICE_INFO causes missing-INFO request flags at a subsequent controller FC03 poll. Operation-page requests are a DIFFERENT class after onboarding. Actual received pages clear corresponding request bits. Service manager diagnoses missing controller messages and may reboot GATEWAY; no controller-running reinitialize command was found in examined device-client/service-manager paths. This is a scoped negative finding, not universal nonexistence or proof of XTR native ownership.

C5AW USER LIVE 22:47:36–22:48:36: 0848/23 ACK, one offered 0708/6 served, 03E8/14 received twice (second ACK), repeated 042E/15 and 085F/5 withheld, three total bus TX, 60.227s safe expiry with native profile UNVERIFIED and H/D/C/M 0/4. Native first join COMPLETE / NEGATIVE; bounded transport continuation COMPLETE / POSITIVE. Important SOURCE FIX: the C5AW branch described in its comment/log as CURRENT-only in fact selects OEM SETTINGS request flags (the observed 03E8 is consistent), not operation CURRENT. The earlier statement that a true CURRENT-only request was tested is DISPROVEN. Correct this classification before protocol conclusions. No additional firmware or physical TX in this review; OEM private mask values, protected source and handshake omitted from public docs; HA setting writes ON HOLD.

CURRENT MILESTONE: C5 running-controller first native join. DELIVERABLE: two-version OEM code-path investigation and exact C5AW request-class mismatch; no new physical experiment. REAL BLOCKER: no proven way to compel controller restart/export or qualify native owner/profile/current 4/4 on running XTR. ONE NEXT ACTION: prepare ONE private integrated info-first request/receipt and truthful read-classification fix on C5AW/C5AR single-engine baseline, grounded in actual offered 0708 and genuine OEM schema, with CRC/DE/peer/ABORT unchanged, no automatic TX and no fabricated acceptance.

**2026-10-25 — PRIORITY RETURNED: FIRST cold join from zero, not hot rejoin; C5AV SOURCE/OFFLINE TESTED PREPARED/NOT RUN.** 2026-10-25 — User resumed previously PARKED FIRST native cold join on a RUNNING XTR M controller 2.4.2, with NO preceding DCM and NO controller restart. This is NOT C5AU retained hot rejoin, nor C5AR controller-cold-start (proven LIVE), nor C5AS 042E refresh (parked). Previous actual C5AB/C5AD/C5AF first-attach experiments already demonstrated physical ACK on 04BA and later 059C, ACKs for qualifying 059C/05FF/0662, and a standalone 085F ACK that stopped retries, but NEVER a fully qualified first DCM session. Do NOT repeat individual-page ACK microtests.

OEM Connect 2.1.105 SOURCE: slave internally recognizes a qualifying incoming FC16 and may request missing data on later controller FC03 polls. C5AR sparse cold-join code already produces a guarded first config ACK but both RX and sole-TX FC03 runtime read gates required complete 22-page export to permit even a single CURRENT read request. One integrated candidate MAIN03-C5AV built from exact LIVE C5AR: only in ONE explicitly user-started S92 session, after actual CRC-good known config FC16 and PHYSICALLY successful first ACK, in same manually authorized sparse first-attach epoch, when controller itself later offers genuine native controller read within existing 120s export window, send ONE existing read-only CURRENT request with read-only request words (PRIVATE) through SAME physical S92 UART/DE owner and unchanged CRC/peer/collision/dirty/ABORT guards. No invented start or auth frames, no new UART writer, no HA setting/parameter writes; do not mark acceptedOwner, config SYNCED, or H/D/C/M 4/4 until real controller export independently proves it. If controller offers only 085F or no FC03 runtime read, the gateway slave cannot initiate and experiment would be inconclusive; no retry loops. OEM guide describes gateway reboot during pairing without prescribing controller reboot; this is NOT local XTR first-attach proof.

Full PRIVATE C5AV ZIP: THERMIA_MAIN03_C5AV_FIRST_ATTACH_NO_RESTART_XTR_242_PRIVATE_20261025.zip; exactly ONE complete full YAML + README + manifest; YAML SHA256 72f980d71b6026207ab89094f3500247c440845404795bb83fb31847d6c196d4; ZIP SHA256 f81b257dab4ee1069ff3fb1111e0c0a18ef6736a34abc91266d962fc687c809c. PyYAML, 852 unique IDs, 800 resolved ID refs, no new physical write_array/DE HIGH, unchanged production HA section counts, ZIP integrity PASS. SOURCE / OFFLINE TESTED, PREPARED / NOT RUN; not ESPHome target compiled, not FLASHED/LIVE. OEM private source and C5AV private YAML NOT published. C5AR remains last user LIVE and locally verified; C5AU hot rejoin + C5AS refresh parked.

CURRENT MILESTONE: first native DCM cold join from zero on already-running controller. DELIVERABLE: single integrated C5AV private source prepared. REAL BLOCKER: actual first qualifying FC16 -> following FC03 runtime read -> controller full native export/accepted owner/FRESH 4/4 unverified; no evidence for unsolicited slave TX. ONE NEXT ACTION: user compiles/flashes C5AV in one explicitly authorized bounded S92 first-attach experiment with continuous logs, no pump restart/room sensor disconnect, ABORT for real fault, rollback C5AR, HA writes ON HOLD.

**2026-10-25 — C5AU RETAINED HOT-REJOIN FIX PREPARED / NOT RUN; C5AS FC03/042E refresh PARKED.** User wants code now but test only on next real native DCM. C5AR last local LIVE, controller cold-return proven. C5AT ESP-only test partial: one 042E ACK + 0662 ACK, controller offers 0848 and 0708, no 0864/0870, owner not qualified, log ends before 120s; no reason to invent newer test results. OEM Connect is a Modbus slave that handles ordinary controller FC16 without fresh startup every time; source supports bounded 0848 retained candidate, NOT full XTR Online proof. Complete private MAIN03-C5AU built from exact C5AR, same UART/DE owner, user S92 manual approval, CRC/peer/dirty guards, after real ACKed 0662 and later controller-offered 0708 permits one 0848 ACK; only actual later served 0708 can qualify transport, no fake config SYNCED/fresh H/D/C/M/Online, 120s unsynced failback. Full source ZIP only (one YAML, README, manifest), SHA256 `a3f260d6a1ab7b4b95325d19866a81aac88c0c9ebc53a6867ca944fcbb55614a`; source/offline validated 852 unique IDs/800 refs, no target compile/flash/live. **CURRENT MILESTONE:** hot rejoin before refresh. **DELIVERABLE:** private C5AU PREPARED/NOT RUN; C5AR last live. **REAL BLOCKER:** true hot transport+config+fresh current after ESP-only restart not yet proven. **ONE NEXT ACTION:** wait for genuine running DCM, then user flash C5AU, one explicit S92 bounded experiment with full log and ABORT/rollback; no autonomous flashing and HA writes HOLD. Full notes in Research.

**2026-10-25 21:27 — C5AT ESP-only hot rejoin USER LIVE RUNNING / PARTIAL; C5AS stays PARKED.** Last user FLASHED C5AR iTec XTR M controller 2.4.2 was ESP-only rebooted; manual S92 started 21:25:55.782. Controller offered CRC-good FC16 042E/15 (ACK once), 0662/33 (ACK once), ongoing FC16 0848/23 (NO_ACK without new owner) and at least 14 FC03 0708/6 (WITHHELD), two total guarded bus TX, CRC/resync/drops0 and DE LOW. No 0864/0870 or full config export, M6 owner0, NOT_SYNCED/H-D-C-M 0/4. First 0662 ACK starts a source-verified 120s tail; uploaded log ends 21:27:04 ~66s later BEFORE final timeout. Hot rejoin NOT qualified during window, experiment RUNNING/PARTIAL, do NOT claim final expire. Prior C5AR controller-cold-start still COMPLETE/POSITIVE. C5AS 042E refresh fix PREPARED/NOT RUN and deliberately PARKED. **CURRENT MILESTONE** retained-session hot rejoin. **REAL BLOCKER** OEM-consistent current controller session adoption without invented owner: 0848+0708 existing runtime offered but fresh ESP epoch unqualified. **ONE NEXT ACTION** examine later logs from same attempt until ~21:27:59 if available, then GO/FIX/NO-GO and grounded integrated source correction, no repeat idle S92 or HA writes. See Research canonical files.

**2026-10-25 21:02 — PRIORITY: HOT REJOIN (C5AT) PREPARED / NOT RUN, C5AS PARKED.** User-running C5AR native DCM; ESP-only restart + one explicit S92 session, real risk current DCM lost until future controller restart. Do not flash C5AS. See Research/THERMIA_PROJECT_STATE.md for verified C5AT plan, expected 0864→0870→0708+fresh 4/4 and guards; no HA writes.

**2026-10-25 — MAIN03-C5AS private SOURCE/OFFLINE TESTED, PREPARED / NOT RUN: native 042E current refresh and ACK owner FIX.** The last XTR M 2.4.2 locally verified controller cold-return is MAIN03-C5AR: user-opted native FC23→full FC16 config→FC03/0708 replies 4, accepted runtime owner and FIRST H/D/C/M 4/4 FRESH; OEM Online/cloud and sustained refresh unproven. Critical live/source detail: at 19:44:55, EXP378 read-only 042E current refresh immediately aborted state6 after 28ms on **historical resyncDelta=11** (new read-selector failed to snapshot counters), then repeated controller 042E/15 FC16 got NO_ACK from EXP420 because experiment already state5. One integrated **C5AS** corrects BOTH parts: snapshot live counters at start of a new EXP378 selector, retaining guards on NEW faults; ACK subsequent CRC-good normal controller 042E/15 via the **existing** same-epoch S92 native runtime owner when synced and no write pending, rather than requiring transient EXP378 state6. No new TX owner/callsite/frames/HA setting writes. C5AR cold-start, UART/DE/CRC/B11 guards, FC16/03/CURRENT, HA, ABORT and recovery opt-in default OFF are kept. Compact private ZIP has exactly ONE full C5AS YAML+README+manifest (no prior YAMLs); YAML SHA256 `3e5c092d83b83f375657879cbbccc5536c38bf5678787f5dac121f38361cd7b3`, ZIP SHA256 `1e6272c447d5f47a72b9ddfc0d71fce76d8515704866f269080033d3073241c8`, source/offline YAML + IDs/refs + XTR 042E CRC PASS, **not target-compiled, not flashed, not LIVE**. **CURRENT MILESTONE:** native FC03/current refresh/long-lived freshness. **REAL BLOCKER:** end-to-end CURRENT periodic refresh remains unverified after correction. **ONE NEXT ACTION:** user compile/flash C5AS and evaluate ONE qualified controller-originated runtime/042E refresh opportunity; boot stays passive after ESP-only reboot, no repeated empty S92 or unnecessary controller power cycle. HA parameter writes HOLD. See canonical Research files.

**2026-10-25 19:45 — BREAKTHROUGH: MAIN03-C5AR LIVE achieved locally owned DCM native cold-start and first full CURRENT 4/4.** With user opt-in recovery ON, user restarted XTR M controller 2.4.2; true RS485 bus silence 5235ms at 19:43:59 consumed switch OFF, recovery stage1; genuine controller FC23 accepted and guarded response 19:44:08, full native config FC16 export incl 04A6/059C, native FC03/0708 (4), 0864/0870/0884 replies, runtime config SYNCED + H/D/C/M all fresh (4/4) 19:44:58, M6 acceptedOwner/integrity/profile/fresh at 19:45:00. Later CM930 APP 33/33 observed, status **NOT_ONLINE manualReadOnly**; local owned DCM transport PROVEN, OEM full Online/cloud/longevity still OPEN. UART CRC_DIFF0, RX drops0, DE LOW, HA settings writes ON HOLD. **C5AR cold-return experiment COMPLETE / POSITIVE**, latest LIVE baseline C5AR. **New confirmed source/live blocker:** existing EXP378 read-only `042E/count15` selector led to repeated controller 042E FC16 but `EXP420_CONFIG_NO_OWNER` because exp378 state5 excludes source's allowed4/6; EXP378 refresh inconclusive. **CURRENT MILESTONE** C5 cold-start proven, complete FC03 refresh/cache freshness. **DELIVERABLE** integrated proven cold return and fresh 4/4, next concrete TX-owner correction identified. **REAL BLOCKER** normal qualified owner ACK of recurring 042E and sustained fresh/current, not cold-start. **ONE NEXT ACTION** targeted single-engine 042E FC16/EXP378-420 refresh ownership fix starting at complete locally flashed C5AR; preserve DE/CRC/collision, ABORT and all production HA, no HA setting writes, no more forced controller restarts. Canonical research updated.

**2026-10-25 19:34 — MAIN03-C5AR now user FLASHED/LIVE, C5AI opt-in recovery waiting (RUNNING / PARTIAL).** Target XTR M controller 2.4.2. New user log `Pasted text(20261025-183448).txt` shows passive BOOT_RX_ONLY after ESP OTA with normal bus frames. Explicit C5AI one-shot Cold Recovery ON 19:32:28, OFF 19:32:59, ON again 19:34:30 (**last observed ON**). No >=5s bus outage, no controller native FC23/config FC16/FC03 0708, zero physical TX, no owner, no fresh H/D/C/M 4/4. V5 CRC_DIFF=0 through 1103, RX drops=0, parser resyncs 11 **stable** in log. Boot and manual opt-in **COMPLETE / POSITIVE**; actual cold-return **RUNNING / PARTIAL**, untriggered and not a failed handler. No new firmware or speculative TX justified. **CURRENT MILESTONE:** C5 controller-originated cold return. **REAL BLOCKER:** no genuine observed outage/controller re-export. **ONE NEXT ACTION:** user leaves one-shot ON only if intending a future bounded recovery (otherwise OFF); examine full controller-originated sequence when real outage occurs, without forced pump restart, room-sensor disconnect or HA parameter writes. Read Research canonical files for handoff.

**2026-10-25 — MAIN03-C5AR SOURCE/OFFLINE TESTED (PREPARED / NOT RUN):** XTR M controller 2.4.2. Latest user-FLASHED/LIVE **C5AQ** proved manual-only boot/RX-only and safe S92 expiry, but 0 native DCM offers on still-running controller. Original Connect is Modbus slave; no justified unsolicited attach TX, avoid another empty S92 run. **Concrete next engineering FIX integrated privately:** preexisting explicit opt-in one-shot C5AI controller cold-recovery wrongly required a prior failed 60s manual retained session (origin5/M6=7), excluding normal passive ESP boot (origin0/M6=0). **C5AR** accepts both exact passive states when user switch ON (ALWAYS_OFF after reboot), real >=5s bus silence, no competing/pending writes, valid guards and one-shot latch. Retains original one UART/DE owner and verified C5AK/C5Y exact controller FC23+actual A80E/A80F guards, FC16 sync, 0864/0870 rejoin, FC03/CURRENT, all production HA, ABORT, no parameter writes. ONE private complete C5AR firmware YAML ZIP with README+manifest ONLY (no old YAML), YAML SHA256 `ef50a552c1a737f88286fc9313a79d772cf891d8176a46349533985e5492e45b`; YAML parsed/850 unique IDs/798 refs/unchanged TX code validated offline, no target compile/flash/LIVE. **CURRENT MILESTONE:** C5 native cold-return/hot rejoin. **REAL BLOCKER:** controller must genuinely offer DCM during actual controller return; running-controller passive session offers none. **ONE NEXT ACTION:** user compile/flash C5AR, observe manual-only boot/switch OFF, explicitly opt in to one future naturally occurring controller cold return; full logs/GO-FIX-NO-GO. Do not request controller restart or disconnect room sensor. HA setting writes ON HOLD. Canonical Research files updated.

**2026-10-25 — MAIN03-C5AQ FLASHED/LIVE on iTec XTR M controller 2.4.2: BOOT FIX POSITIVE, manual S92 running-controller native rejoin has NO OFFER.** User log `Pasted text(20261025-181012).txt`: after ESP OTA 19:08:03–19:08:46 BOOT_RX_ONLY, no automatic START; one **USER-initiated** S92 at 19:08:46.695, stage40 for 60.247s; no controller known FC16 04A6/059C/085F/0864/0870 or FC03/0708, ZERO ACK/TX, no fresh H/D/C/M 4/4, owner NOT QUALIFIED. 19:09:46.956 safe RX-only/DE LOW, V5 CRC_DIFF/resync/drops zero and regular bus 02/0A/1E healthy. C5AQ boot fix **COMPLETE / POSITIVE**, actual retained attach **COMPLETE / NEGATIVE**, new 0864/0870 responder **COMPLETE / INCONCLUSIVE** (never offered), not a protocol-handler failure. C5AQ is newest locally user FLASHED/LIVE baseline; C5AP SUPERSEDED/NOT RUN. **C5 milestone / REAL BLOCKER:** running controller not initiating an OEM DCM exchange on an ESP-only rejoin, while original Connect is controller-driven Modbus slave; don't invent initiating TX. **ONE NEXT ACTION:** integrate/qualify existing C5AK verified controller-originated startup path within C5AQ, preserving S92 guarded response, native runtime FC03/current, room sensor, collision/CRC/DE and HA parameter writes HOLD. **NO-GO** more empty repeat 60s S92 probes or new FC16 gates on unchanged running controller; no new YAML until a real fix is justified. Read Research files.

**2026-10-25 — C5AQ: FIX unintended S92 automatic START on ESP OTA, PREPARED / NOT RUN.** User's actual C5AO log `Pasted text(20261025-172350).txt` showed S92 stage40/RETAINED_CONTEXT_MANUAL 5s after OTA **without manual button press**; no controller DCM request, no FC16 ACK or physical TX (DE LOW), 60s expiry RX ONLY. Source-proven cause in both C5AO and previously prepared C5AP was obsolete C5Y `on_boot` unconditional `button.press: s92_manual_dcm_start` and conditional legacy 07E4 autoarm. Physical TX did not occur this time, but unauthorized manual-scope arming was a REAL defect. **C5AP SUPERSEDED / NOT RUN; do not flash.** Complete PRIVATE **MAIN03-C5AQ** now removes the entire auto-START/auto-07E4 on_boot action and preserves boot RX_ONLY/DE LOW, sole UART/DE/CRC/collision safeguards, manual S92/ABORT, native first 0864→0870/0708 plus first 04A6/059C/085F, locally verified C5AK cold start, FC03/CURRENT and all production HA. Source and YAML offline PASS (850 unique IDs, 798 resolved refs), ZIP one latest full YAML+README+manifest, no old YAML. Not target compiled or flashed/live. **CURRENT MILESTONE C5 XTR 2.4.2 native rejoin; REAL BLOCKER** genuine controller re-offer/acceptance and fresh H/D/C/M 4/4. **ONE NEXT ACTION:** user compile/flash C5AQ, confirm NO auto session and DE LOW during boot, then ONE explicit user-started full bounded S92 session, log before start and decide GO/FIX/NO-GO. No heat-pump reboot/room sensor removal; HA setting writes HOLD. See canonical Research files.

**2026-10-25 C5AP — OEM native 0864→0870 rejoin SOURCE FIX PREPARED / NOT RUN:** Target iTec XTR M controller 2.4.2. Genuine Connect 2018/2.1.105 runs as Modbus slave, not a proven unsolicited master for rejoining a running controller. Genuine XTR OEM DCM trace ACKed FIRST controller FC16 `0864/count4`, then `0870/count17`, then controller FC03/0708. Existing C5AL branch inside latest user-LIVE C5AO incorrectly demanded a fixed 0864 payload **not matching the original XTR**, two identical 0864 offers, separate manual PREARM and earlier FC03, plus unproven timing requirements. **PRIVATE complete C5AP ZIP** integrates normal first-offer 0864 ACK via existing one USER-STARTED bounded S92 session and sole UART/RX/DE owner, then already existing genuine 0870/0708 follow-up; removes obsolete 0864 prearm button. All native, production HA and CRC/collision/ABORT safety preserved; HA parameter writes HOLD. Exactly one latest full YAML + manifest + instructions; no older YAMLs, no public private firmware. SOURCE / OFFLINE TESTED only; ESPHome target compile/flash/live NOT done. C5AO remains last user-FLASHED/LIVE (native attach NEGATIVE). **REAL BLOCKER:** no guaranteed controller-offered rejoin if it offers only isolated 059C; no proof of legal Connect-initiated session-start TX. **ONE NEXT ACTION:** one user-initiated full C5AP S92 end-to-end session with log captured before start, success only owner/RUNTIME/SYNCED+fresh CURRENT H/D/C/M 4/4, ABORT/rollback available, no heat pump reboot or room sensor removal. See Research canonical files.

**2026-10-25 17:45 — C5AO XTR 2.4.2 LIVE / NO DCM — C5 FIX decision:** User flashed C5AO and user-started one S92 stage40 session on running controller. Full provided log starts ~3 seconds AFTER native start/first request, so exact first 059C request/ACK timing is NOT observable. Sensor/counters confirm first config `059C`, native ACK 1, physical TX 1, `04A6_SEEN=0`, `0708/FC03=0`, fresh H/D/C/M 0/4, owner NOT ACCEPTED; `OEM_INTERNAL=ACCEPTED` is internal firmware imitation only. At 17:43:25.806 60.031s unqualified timeout returned RX ONLY/DE LOW, zero CRC/resync/drops; no HA writes. Native cold join COMPLETE / NEGATIVE, safe expiry COMPLETE / POSITIVE. In genuine OEM successful XTR capture, 059C occurs AFTER 04A6 during full controller-driven export, not as isolated re-entry. **NO-GO** further duplicate-gate ACK microtests; **ONE NEXT ACTION** find/implement actually evidenced OEM running-controller native attach/session entry from genuine Connect vs verified C5AK controller-start path, in existing sole UART/DE engine; if not substantiated, explicit NO-GO (no fabricated physical TX). Room sensor remains connected; HA parameter writes HOLD. See Research/THERMIA_PROJECT_STATE.md and Research/DCM_SESSION_ROADMAP.md.

**2026-10-25 — MAIN03-C5AO OEM first-FC16 FIX PREPARED / NOT RUN (current):** Target is user's iTec XTR M **controller version 2.4.2** (do not confuse with OEM Thermia Connect **gateway** firmware version 2.1.105). Actual C5AN 17:15 user live attempt ACKed a duplicate 059C/33 but had no native FC03/0708 or CURRENT; full cold join COMPLETE / NEGATIVE, new C5AN first-085F subroute NOT TRIGGERED. Genuine XTR OEM DCM capture responds to the very first 059C, with a ~14ms ACK. Complete PRIVATE C5AO one-YAML ZIP now integrates OEM first-offer FC16 for 04A6/13 plus all 22 **already known** config export geometries using the *existing* S92 sole UART/DE owner and common page table; preserves C5AN 085F response, FC23 cold start, C5AL hot rejoin, FC03/CURRENT and all production HA. Real CRC/collision/DE guards and ABORT kept; ACK does not imply controller acceptance; HA writes ON HOLD. YAML SHA256 `0c81e396b05706ed0281a0e60fedf0b61410fd3cb7eaee94d944347f014c50a2`; SOURCE/OFFLINE TESTED only, not target compiled/flashed/live; private code NOT published. **ONE NEXT ACTION:** user-initiated bounded full C5AO cold join on running controller with room sensor connected; log to assess runtime + fresh H/D/C/M 4/4 and decide GO/FIX/NO-GO. See current Research files.

**2026-10-25 C5AN LIVE / NO DCM:** User flashed C5AN and ran one manual S92 stage40 attempt on a running controller. Controller offered CRC-good FC16 059C/count33 twice (17:15:58.285/59.072); existing C5AD answered the second once (17:15:59.088), then no further native export/0708/FC03/CURRENT (0/4); 60s guard safely returned RX ONLY/DE LOW, RX error counters zero. Full cold join COMPLETE / NEGATIVE; new C5AN 085F responder NOT TRIGGERED (no 085F offer), not a negative test of that branch. Source comparison shows C5AD requires two identical 059C offers unlike genuine local XTR OEM Connect (one at 48.893s, ACK at 48.907s). **DECISION FIX:** align first known config FC16 ACK to OEM in one integrated private successor within existing single S92 owner, while not claiming session acceptance from ACK. HA writes HOLD; no controller restart, room sensor disconnect or blind retest. See Research/DCM_SESSION_ROADMAP.md.

**2026-10-25 C5AN SOURCE PREPARED / NOT RUN (current next action):** Original Connect 2018/2.1.105 and genuine local XTR DCM trace show that FIRST controller-offered 085F/count5 alarm FC16 is normally ACKed without C5AM's additional PREARM/double-offer/post-0662 protocol gates; such transport ACK is explicitly NOT handshake acceptance. The missing exact C5AM private source ZIP is now available and SHA-256 verified. Complete **private** MAIN03-C5AN YAML and rollback ZIP has been prepared and offline syntax, IDs, XTR CRC and packaging checked; no embedded target compile, no flash, no live TX. One user-started S92 session remains mandatory for this new unvalidated physical first-offer ACK (max one), with existing CRC/DE/peer guards, ABORT and HA writes ON HOLD. Early alarm transport ACK does not block later native config cold/hot entry accounting. **C5AM-COLD-JOIN-01 remains RUNNING / PARTIAL** (special gated reply NOT TRIGGERED); **C5AN-OEM-085F-01 PREPARED / NOT RUN**. Next: ONE bounded full C5AN user-initiated running-controller native cold join, no heat-pump restart or room sensor disconnect, successful only on RUNTIME+SYNCED+FRESH H/D/C/M 4/4. Private YAML is NOT public. See Research/DCM_SESSION_ROADMAP.md and canonical Research files.

**2026-10-25 C5AM LIVE LOG REVIEW:** Two uploaded logs are overlapping (short is exact prefix of long). Device confirms C5AM flashed; initial S92 session began before log and sent one FC16 ACK (085F counter=1, no C5AM proof), timed out 13:12:35. Second explicit S92 START at 13:13:21 stage40 sent 0 TX and timed out 13:14:21. No `POST0662_PREARMED`, `POST0662_ARM_BOUND`, 04A6→0662 pages, 0708 or current 4/4; clean CRC/RX and DE LOW. **C5AM-COLD-JOIN-01 RUNNING / PARTIAL**, its post-0662 085F fix NOT TRIGGERED, not proven negative. Next: confirm real controller first-attach offers before one correctly prearmed run; avoid unarmed repeated START. See Research/EXPERIMENT_LOG.md.

**2026-10-25 CURRENT C5 COLD-JOIN FIX: MAIN03-C5AM SOURCE PREPARED / NOT RUN.** Live C5AL 04A6→04BA→059C→05FF→0662 sent five ACKs on continuously running controller; no 0683/0708/runtime. Exact source review found existing OEM-consistent one-shot alarm response reachable on C5AD path but missing from C5AB 04A6 path. Private C5AM enables ONLY one manually prearmed, post-0662 two-offer one-shot existing reply via sole S92 TX owner, preserving no-acceptance until qualified runtime and fresh H/D/C/M. Offline YAML, patch and source tests done; target compile/flash/live NOT done. No private YAML committed; no WP reboot. Next: ONE user-initiated C5AM-COLD-JOIN-01 with ABORT and rollback. See Research/EXPERIMENT_LOG.md.

**2026-10-25 C5AL cold-join LIVE:** User actually runs MAIN03-C5AL (not presumed C5AK). One S92 START on already-running controller at 12:41:57 (stage40); controller offers 04A6→04BA→059C→05FF→0662 and five guarded ACKs are physically sent. Controller then only repeats zero-context 085F, with no 0683/FC03/0708 and 0/4 CURRENT; 60s timeout -> RX ONLY DE LOW. **COMPLETE / NEGATIVE** full cold join; safe expiry positive. C5AL hot-0864 ARM NOT used, hot rejoin still PREPARED / NOT RUN. NO-GO speculative 085F reply; one next action: reconcile OEM 085F/0662 continuation against XTR evidence for a real implementation fix. See Research/EXPERIMENT_LOG.md. HA parameter writes HOLD.

**2026-10-25 — CURRENT USER PRIORITY: COLD JOIN, NO HEAT-PUMP RESTART.** Previous C5AK controller cold-start restoration plan is SUPERSEDED / NOT RUN by user preference. Current warmtepomp works without DCM; next: one bounded, user-initiated **C5AK stage40 native cold join on live controller bus** with complete log, existing sole UART/DE and ABORT. C5AL is retained hot rejoin only, PREPARED / NOT RUN, not the right present entry. HA parameter writes remain ON HOLD. See Research/EXPERIMENT_LOG.md.

**2026-10-25 NEXT MILESTONE ACTION — C5AK-DCM-RESTORE-01 (PREPARED / NOT RUN):** After the locally observed C5AK ESP-only hot-rejoin failure, user confirmed expected Online-module communications alarm, manually restarted the heat pump and reports normal heat-pump operation **without DCM**. The user explicitly requests to restore DCM first using the **locally verified C5AK guarded controller cold-start path**. No C5AL hot-rejoin experiment until the user reports healthy owned RUNTIME and fresh H/D/C/M 4/4. No new firmware or HA parameter write; no autonomous flash or power cycle. Details: Research/EXPERIMENT_LOG.md.

**2026-10-25 C5AL prepared:** Exact C5AK hot-rejoin blocker addressed by PRIVATE integrated C5AL source (offline YAML and patch checked; NOT compiled/flashed/live). One user-armed, guarded controller-offered 0864→0870→0708 candidate in the existing single S92 engine, followed by one proven CURRENT 4/4 request; HA parameter writes ON HOLD. No private firmware code published. NEXT: one bounded, user-initiated C5AL-HOT-ENTRY-01 with ABORT/rollback. See Research/EXPERIMENT_LOG.md.

**2026-10-25 C5AK hot-rejoin verdict:** From confirmed RUNTIME/FRESH/4-of-4, ESP-only OTA reset received 27 controller FC16 0864/4 and 14 FC03 0708/6, all withheld due current-epoch owner gate; 60s timeout -> RX ONLY, clean V5. **LIVE COMPLETE / NEGATIVE** for automatic hot rejoin, safe rollback positive. Next: one integrated user-initiated bounded guarded retained-entry fix; cold start positive, HA writes HOLD. See Research/EXPERIMENT_LOG.md.

**25 October 2026 — current C5AK source-gate decision:** The full *manually armed controller-restart* C5AK native cold-start chain is **LIVE COMPLETE / POSITIVE** (FC23→FC16 through 06F4→FC03/0708→fresh H/D/C/M 4/4). Exact C5AK source review against genuine prior C5AB/C5AC/C5AD/C5AJ offers and original Connect (2018/2.1.105) found **no new demonstrable missed authorized controller request in the deployed ESP-boot gate**. Earlier sparse `04BA→059C` and direct `059C` entry fixes are present; `0662` ACK alone did not prove `0683` acceptance. **NO-GO speculative firmware fix.** Cold join with already-running controller and ESP-only retained hot rejoin remain OPEN. ONE NEXT ACTION: one user-initiated bounded complete first-attach cold join on unchanged C5AK, not another isolated ACK test; preserve abort/rollback and HA writes ON HOLD.

> **25 October 2026 — C5AK continuity update (supersedes older C5AF/current-stage summaries below):** C5Y controller-initiated cold-start recovery is **LIVE COMPLETE / POSITIVE within its tested scope** (guarded FC23, ordered FC16 export through 06F4, FC03/0708 runtime). The manually requested C3 CURRENT H/D/C/M refresh is **LIVE COMPLETE / POSITIVE (4/4, snapGen 1→2)**. C5AJ retained-stage 0662/count33 ACK was physically transmitted with clean DE LOW, but the controller did not offer 0683 or progress to runtime in the observed window; transport ACK is not semantic session acceptance. C5AK fixed competing retained/export timers and has been **FLASHED / LIVE observed only for retained no-DCM-offer / zero-TX expiration**; a complete C5AK controller-led cold-start has **NOT** been locally verified. C5Y success cannot be automatically transferred to the C5AK binary. **CURRENT MILESTONE: C5 — durable session, recovery and integrity. REAL BLOCKER: full C5AK controller-offered cold-start chain and ESP-only retained rejoin remain unproven. ONE NEXT ACTION:** one USER-INITIATED, bounded end-to-end actual controller cold-start observation on C5AK using the established C5Y sequence as reference (controller boot recognition → guarded FC23 → controller FC16 configuration export/ACK → native FC03/0708 runtime → complete fresh H/D/C/M and healthy RX/HA). Do not reduce this to a standalone 0662 ACK test, invent 0683 requests or relax owner/CRC/DE/collision guards. Abort on communication alarm or bus-integrity problems; preserve rollback and HA writes **ON HOLD**. Private firmware-derived details stay private.

# Thermia iTec XTR M → Home Assistant via ESPHome

Local ESPHome integration and reverse-engineering project for the **Thermia iTec XTR M** internal RS485 bus, tested on an older/non-Genesis controller.

The repository has two deliberately separated runtime builds:

| Build | Bus access | Intended use | Current status |
|---|---|---|---|
| [Read-only](Read-only/) | RX only | Monitoring, dashboards, register research | Recommended for normal monitoring |
| [Write (Beta)](Write%20%28Beta%29/) | RX + guarded TX | Native multi-setting control | Locally working, still Beta |

The underlying bus is **Modbus RTU-like, 9600 baud, 8E1 with Modbus CRC**.

> **Published Write (Beta) status — v4.0:** native page-owned semantic writes have been locally demonstrated on `03E8/count14`, `042E/count15`, `0442/count13` and `0546/count20`. Seven clearly labeled **TEST** controls are not yet locally proven. This TX-capable public build is separate from the currently deployed **RX-only / TX HARD_DENY** V5 research baseline.

## Continue research across ChatGPT chats

Start with **[Research/START_HERE.md](Research/START_HERE.md)** for the short, date-stamped research handoff, then **[Research/CONTINUITY_WORKFLOW.md](Research/CONTINUITY_WORKFLOW.md)** for the documentation/update workflow. Always verify against the newest canonical experiment evidence; the handoff is not a replacement for source logs.

## Choose a build

### Read-only — recommended for monitoring

Use the [Read-only folder](Read-only/) when you only need Home Assistant monitoring or want to inspect the Thermia bus without transmitting anything.

Two variants are maintained:

- **Public / optimized** — quiet, lower-overhead build for normal Home Assistant use.
- **Research / register mapping** — still RX-only, but includes raw logging, register mapping and additional diagnostics.

Current XTR files:

- `Read-only/Thermia itec XTR/thermia_itec_xtr_m_waveshare_public_v29.yaml`
- `Read-only/Thermia itec XTR/thermia_itec_xtr_m_waveshare_research_v29.yaml`

See [Read-only/README.md](Read-only/README.md) for installation, wiring and the difference between both variants.

### Write (Beta) — guarded native multi-page control

Current file:

- `Write (Beta)/thermia_itec_xtr_m_waveshare_write_beta_v4_0.yaml`

The build follows the native Thermia/Danfoss Online/DCM-style page mechanism rather than issuing speculative direct register writes.

Locally proven write scope currently includes:

- Heating settings on `03E8/count14`
- Hot Water / service settings on `042E/count15`
- Cooling settings on `0442/count13`
- Operation Mode on `0546/count20`

Each write starts from a fresh authoritative controller page. The ESP answers the controller's desired-page pull with a full page containing exactly one intended word change, and success is accepted only after the controller republishes that page with the requested target and `extraDeltaWords=0`.

Write Beta v4.0 also contains seven candidate controls that are **fully implemented but explicitly marked TEST** in Home Assistant:

- `0430` — Hot Water **TEST Top-up**
- `0444` — Cooling **TEST Hysteresis**
- `0446` — Cooling **TEST Configuration**
- `0448` — Cooling **TEST Stop Threshold**
- `044A` — Cooling **TEST Max Start Temperature**
- `044B` — Cooling **TEST Min Stop Temperature**
- `0559` — **TEST Link Integration**

These are STRONGLY SUPPORTED mappings from EXP382. They are not locally proven until their individual EXP383 results are supplied. `0559 Link Integration` should be tested last because it may affect the integration/session itself.

See [Write (Beta)/README.md](Write%20%28Beta%29/README.md) before installing it.

## Tested hardware

The supplied XTR YAML files target:

- Thermia iTec XTR M with the compatible older/non-Genesis controller
- Waveshare ESP32-S3-RS485-CAN / ESP32-S3-RS485-CAN-U
- onboard isolated RS485 transceiver
- ESPHome
- Home Assistant

Other Thermia/Danfoss models are useful cross-model evidence, but compatibility must **not** be assumed until validated on the specific supported type.

## Thermia RS485 connection

The tested Thermia RJ45 connection is:

| Thermia RJ45 | Waveshare |
|---|---|
| pin 1 — RS485 A | A+ |
| pin 3 — RS485 B | B- |
| pin 5 — bus reference | not connected in the tested isolated setup |
| pins 7/8 — +12 V | not connected |

Power the ESP32 separately over USB-C.

Leave the Waveshare **120 Ω termination jumper open/off** when attaching to the existing Thermia bus. Do not power the ESP32 from the Thermia +12 V pins unless that supply has been independently verified for the intended load.

### Bus parameters

```text
Modbus RTU-like
9600 baud
8 data bits
Even parity
1 stop bit
Modbus CRC
```

On the Waveshare build:

- GPIO18 = RS485 RX
- GPIO17 = RS485 TX in the Write (Beta) build
- GPIO21 = RS485 DE/direction

The read-only builds intentionally do not configure Thermia TX and keep DE low.

## Home Assistant

The integration exposes operational values including room, outdoor, supply and DHW temperatures; compressor/outdoor-unit telemetry; heating/cooling state; SG Ready state; settings and diagnostics.

Write Beta v4.0 Configuration controls are ordered to follow the Thermia manual:

1. Operation
2. Heating
3. Hot Water
4. Cooling

The exact entity catalogue, including TEST status and ESPHome IDs, is maintained in:

[Research/HOME_ASSISTANT_ENTITIES.md](Research/HOME_ASSISTANT_ENTITIES.md)

Useful read-only entities including expansion-valve steps, refrigerant temperatures, discharge-gas temperature, compressor temperature and Room Setpoint Mirror are enabled by default in both the current Write Beta and Read-only v29 builds. Read-only v29 also passively exposes the locally proven Hot Water, Cooling and Operation settings pages without configuring TX.

`Return Temperature` remains deliberately absent because no sufficiently reliable local XTR M mapping has been proven.

## Current native write model

The current model is controller-owned and page based:

```text
persistent qualified runtime
    ↓
fresh authoritative controller FC16 page
    ↓
current-page selector if refresh is required
    ↓
desired-page selector
    ↓
controller FC03 reads that page
    ↓
ESP returns the complete page with exactly one selected word changed
    ↓
controller FC16 republishes the page
    ↓
target match + extraDeltaWords=0 → transaction confirmed
```

This mechanism is locally proven on four page families:

- `03E8/count14`
- `042E/count15`
- `0442/count13`
- `0546/count20`

The project does **not** treat a normal Modbus ACK as proof of a semantic setting change.

## Research and evidence

The reverse-engineering history is maintained separately from the runtime builds:

- [THERMIA_PROJECT_STATE.md](Research/THERMIA_PROJECT_STATE.md) — authoritative current state
- [EXPERIMENT_LOG.md](Research/EXPERIMENT_LOG.md) — complete experiment history, including negative and inconclusive results
- [PROTOCOL_FINDINGS.md](Research/PROTOCOL_FINDINGS.md) — durable protocol findings and confidence classification
- [HOME_ASSISTANT_ENTITIES.md](Research/HOME_ASSISTANT_ENTITIES.md) — canonical Home Assistant entity catalogue
- [EXP382_OFFLINE_GAP_ANALYSIS.md](Research/EXP382_OFFLINE_GAP_ANALYSIS.md) — latest offline controlled-page gap analysis

Evidence is separated into locally confirmed XTR M behavior, genuine Online/DCM capture evidence, firmware-derived evidence, cross-model evidence and hypotheses.

> **25 October 2026 native MAIN03 update:** Live XTR evidence now confirms C5Y **autonomous controller cold-restart recovery** (guarded FC23 → FC16 export through 06F4 → runtime 0708) and C1C3 **user-requested runtime CURRENT H/D/C/M refresh 4/4**. ESP-only retained hot-rejoin remains a **REAL BLOCKER**: C5Z failed in its bounded 60-second test without TX; C5AE observed repeating zero 085F with no TX; C5AF is **PREPARED / NOT RUN** for one guarded 085F response, not target compiled/flashed/live verified. Parser-resync-induced secondary refresh abort also remains open. These private source candidates are separate from the public Write Beta and RX-only builds. **HA parameter writes remain ON HOLD for MAIN03.** Refer to the newest top entries of [project state](Research/THERMIA_PROJECT_STATE.md) and [experiment log](Research/EXPERIMENT_LOG.md); historical 18 October snapshot below is not the current live milestone.

## Current project status

_Snapshot: 18 October 2026. This is a project-level overview, not a per-experiment status log. For the current evidence and verified baseline, consult [Research/THERMIA_PROJECT_STATE.md](Research/THERMIA_PROJECT_STATE.md), [Research/EXPERIMENT_LOG.md](Research/EXPERIMENT_LOG.md), and [Research/PROTOCOL_FINDINGS.md](Research/PROTOCOL_FINDINGS.md)._

| Workstream | Current status | What is verified / still missing |
|---|---|---|
| **Read-only monitoring** | **Working locally** | Existing XTR RX-only monitoring is usable. The expanded v31 full-monitoring YAML is a **PREPARED / NOT RUN** source candidate, not a compiled, flashed or locally validated release. |
| **Native settings control — Write (Beta)** | **Locally demonstrated, limited scope** | Controller-owned page writes have been confirmed on heating (`03E8/14`), hot water/service (`042E/15`), cooling (`0442/13`), and operation (`0546/20`) pages. Candidate **TEST** settings and general recovery are not universally proven. |
| **Native Online / Connect / DCM integration** | **In progress; application acceptance unproven** | A deployed RX-only V5 diagnostic build was observed for **18 min 33 sec** with parser parity and **zero physical TX attempts reported by software**. This is passive reliability evidence, **not** proof of an accepted DCM session, exclusive response ownership, an Online icon or cloud connectivity. |
| **Firmware and protocol research** | **Offline evidence and tests advancing** | Actual Connect firmware, genuine historical/collaborator captures, and source-backed host tests inform the lifecycle model. Full original-reference replay, exact deployed V5 source identity, and current controller epoch/owner/slot remain unresolved. Firmware behaviour is not automatically XTR bus proof. |
| **Home Assistant coverage** | **Expansion in preparation** | The v31 source candidate has **250 named entities** after cleanup. The **524 XTR-profile firmware schema entries** are an inventory to classify, **not** 524 locally verified bus mappings. Optional-feature availability, freshness, compilation and live HA presentation still need validation. |

**Safety and deployment boundary:** the currently deployed V5 research path remains **RX-only / TX HARD_DENY**. Published Write (Beta) is a separate, guarded TX-capable build and must not be confused with that V5 deployment. No new native transmission is authorized by offline test success; any future live TX must have independently checked ownership, a bounded response slot, abort conditions and a recovery plan.

## Roadmap

**Primary objective:** reproduce the native **Thermia/Danfoss Online / Connect / DCM** integration on the iTec XTR M with ESP32/ESPHome and Home Assistant. Preserve proven monitoring and existing safe control while moving from passive protocol evidence to a controller-recognized, recoverable implementation. Progress is evidence-gated rather than tied to a fixed date or experiment number.

### Critical path — native Online / Connect / DCM

1. **Re-establish the exact deployed baseline and provenance.** Obtain a byte-verifiable copy/hash of the currently flashed V5 RX-only YAML/component set; confirm the single existing UART/CRC frame callback and preserve the known-good image and rollback. Do not substitute a newer draft or the simplified public research bridge for the flashed baseline.
2. **Complete the passive native session/lifecycle model.** Correlate genuine XTR bus evidence, historical DCM/collaborator captures and Connect firmware. Separate cold startup, retained session, reconnection and controller restart. Establish independent evidence for current controller epoch, physical response owner and legal response slot; a CRC-valid frame, page sequence, ACK or internal firmware acceptance is insufficient by itself.
3. **Close the Connect protocol and application gaps offline first.** Reconcile the original firmware-derived reference Core, native request/response lifecycle, parameter/profile/package readiness and existing V5 observer. Build repeatable private source tests without publishing sensitive security, `0x0F` responder or `0x0708` mailbox implementations. Keep RX-only TX denial while evidence gates remain open.
4. **Integrate a guarded, generic native emulator.** Only after source and ownership gates are satisfied, prepare a separate bounded, user-initiated live test in known controller response slots. Require measured controller-side acceptance and explicit abort/recovery evidence before enabling any broader behavior. Verify native settings readback and semantic application independently of transport ACKs. Do not assume Online icon or cloud readiness follows automatically.
5. **Consolidate proven control into the native implementation.** Reuse the locally confirmed controller-owned page mechanism; qualify each additional register and Home Assistant control separately, with fresh-page matching, one intended change, controller republish confirmation, and reversible recovery. Keep unverified **TEST** controls quarantined.

### Parallel track — monitoring and Home Assistant

6. **Finish the XTR read-only monitoring release.** Audit and classify all **524 firmware-profile entries** against actual XTR evidence; expose only appropriately sourced values or clearly labeled RAW diagnostics. Resolve v31 optional pool/shunt/buffer availability and stale-value behavior, check entity/ID coverage and existing diagnostics, then separately validate ESPHome config, compilation, passive flash and Home Assistant behavior. Firmware schema support alone does not prove live registers.
7. **Improve everyday features after their native sources are proven.** Complete fault/warning monitoring, operating-state and defrost interpretation, heating/cooling and DHW presentation, optional circuits and settings. Add calendar/scheduling only after its native semantics and safe control path are independently established.

### Release and compatibility

8. **Make the work reproducible and model-specific.** Maintain a versioned known-good baseline, capture/firmware provenance, regression fixtures, safety/rollback instructions, compatibility matrix and clear installation paths. Validate ATEC, iTec Eco and other Danfoss/Thermia variants as **cross-model evidence**, never automatic XTR proof.

**Release gates:** source reviewed → offline tests passed → ESPHome config/compile passed → user-confirmed flash and RX/bus health → controller-confirmed native semantics. Each gate is recorded separately; passing one never implies the next. The [research handoff](Research/START_HERE.md) points to the latest work, and the [canonical state](Research/THERMIA_PROJECT_STATE.md) determines what is ready next.

**Definition of success:** stable Home Assistant monitoring plus a locally verified native Connect/DCM-compatible controller session with narrowly authorized, semantically confirmed settings changes and safe reconnect/rollback behavior. Cloud Online connectivity, universal model compatibility and unmapped features remain separate goals, not assumed outcomes.

## ESPHome secrets

The YAML files expect these entries in `secrets.yaml`:

```yaml
wifi_ssid: "..."
wifi_password: "..."
thermia_api_encryption_key: "..."
thermia_ota_password: "..."
thermia_fallback_password: "..."
```

Do not commit real credentials to this repository.

## Deployment caution

For normal monitoring, use the established **Read-only** configuration. **Write (Beta)** is a separate TX-capable implementation with proven but bounded controller-owned setting paths; candidate TEST controls are not general release-ready features. The V5 native Connect/DCM research deployment is presently **RX-only / TX HARD_DENY**, not a finished Online emulator. Always follow the [current research state](Research/THERMIA_PROJECT_STATE.md) before changing a running installation.

## Disclaimer and license

This is an **independent, unofficial reverse-engineering and integration project**. It is not affiliated with, endorsed by, or supported by Thermia, Danfoss, ESPHome, Home Assistant, or Waveshare.

The software, documentation, protocol information and example configurations in this repository are provided **“as is”, without warranty of any kind**. The Read-only configurations are designed to operate passively. The Write (Beta) configuration actively transmits data on the heat pump's internal communication bus and may alter heat-pump settings. Incorrect wiring, configuration, modification, software defects or unexpected protocol behaviour may result in malfunction, loss of heating or hot water, equipment damage, or other unintended operation.

Use of this project is at your own risk. Verify the wiring, configuration, operating limits and safety behaviour for your own installation before use. The authors and contributors accept no responsibility for damage, loss, warranty issues or other consequences resulting from use or modification of this project, **to the extent permitted by applicable law**.

Protocol findings apply only to the systems on which they were actually tested unless explicitly stated otherwise. Cross-model Thermia/Danfoss findings must not be treated as proven behavior for another model.

The software in this repository is released under the [MIT License](LICENSE). The MIT License includes its own warranty and liability limitations; this project-specific disclaimer provides additional context about interaction with physical HVAC equipment.
