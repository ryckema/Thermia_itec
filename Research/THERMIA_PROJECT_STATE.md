# 2026-10-19 — LATEST HANDOFF: V5DCM47-RX-GAP-HOST-01 COMPLETE / POSITIVE OFFLINE ONLY (strict C++17 exact FIX2 FreshRx header 19/19 assertions; 12s quiet period invalidates current but leaves phase QUALIFIED, first new valid frame restores current if B11D/other health still good; genuine errors permanently REVOKE). Source audit: one-shot Arm=30s, max one successful Arm per ESP boot, 70ms callback-relative response budget, no output while RX stale. Original B11D sticky response to actual power gap remains UNKNOWN. V5DCM47-LIVE-ONE-SHOT-01 PREPARED / NOT RUN: user-initiated one cold return, one canonical new 0x0F FC23 challenge and at most one private request-dependent guarded reply. Never solicit unsolicited TX, never invent payload, no currently performed live/flash/Arm. Prior current XTR FIX2 178.8s RX QUALIFIED positive, native 0x0F FC23=0, TX=0. Historical G01-09 restart had 24 FC23 retries (different past event). Current next decision: review V47 prepared live scope; preserve FIX2 unchanged and V44B no-TX rollback. [V47 report](V5DCM/V5DCM47_COLD_REJOIN_ONE_SHOT_PREFLIGHT_20261019.md).

# 2026-10-19 — NEWEST: V5DCM46-TRIGGER-H0-H2-OFFLINE-01 **COMPLETE / POSITIVE (original firmware FC16 isolated host tests 7/7 and FIX2 log invariants; NO NEW TX/FLASH)**. Source-original 2.1.105 `modbus_server15.py` byte-equal AppFS/device_client SHA256 `9afc455fb50472012ae31d0767a0c39878647643ea9c37d7155142e097621d4f`: internal H0 NOT_ACCEPTED + ordinary FC16 03E8 or 04A6 can go straight to H2 ACCEPTED WITHOUT H1/FC23; 085F and 04BA excluded. Public reference Core only promotes H1->H2, deliberate TX-safe model difference; do not translate vendor internal H2 to physical acceptance. Current user FIX2 178.8s passive log remains QUALIFIED, all 18 P74E sampled FC23=0, 36 actor snapshots Arm/TX=0; no witnessed new current cold epoch. Historical G01-09 controller user-power intervention produced 24 FC23 retries after gap; older XTR post-return evidence supports lifecycle association, NOT proof of universal trigger/owner. FIX2 live PASSIVE baseline preserved; native TX PREPARED / NOT RUN; owner/epoch/physical slot/Online OPEN. Next offline discrimination or separately user-initiated scope only, no redundant restart/Arm. [V46 result](V5DCM/V5DCM46_CONTROLLER_TRIGGER_AND_CM930_H0_H2_OFFLINE_RESULT_20261019.md).

# 2026-10-19 — CURRENT HANDOFF: V5DCM45-FIX2-LIVE-RX-01 **COMPLETE / POSITIVE PASSIVE LOCAL XTR**; first native TX still **PREPARED / NOT RUN**. New local 178.8-second FIX2 log (user file Pasted text(20261019-142332).txt SHA256 856d5da48c7870d54b151f022fcdc6837fb6f92ea24ef5818e2e9ad0b555a7f2) shows FIX2 `QUALIFYING` then `QUALIFIED` at witness elapsedMs=30762 with 262 fresh frames; remained `QUALIFIED current=1 reason=NONE` through last sampled elapsedMs=185763 / frames=1582. V5 parser frames98->1549, no resync/drops/geometry/unknown; B11C CRC0 and B11D first fault NONE and raw/portable counters match. V44B armClicks0/replyAttempts0/uartAttempt0, physical TX0, DE=RX. Local native 0x0F FC23 remains 0 (P74E FC16=251, FC23=0), owner/epoch/slot unknown. Separate legacy R6 P5 session class UNQUALIFIED does not contradict FIX2 CURRENT RX qualification; they measure different evidence. FIX1 premature startup REVOKED blocker corrected on local XTR during this passive window. Current preferred RX baseline FIX2; no physical reply acceptance claim. Next: existing capture/firmware offline study of missing native challenge, then only a distinct user-initiated bounded TX experiment with strict controls. [Result](V5DCM/V5DCM45_FIX2_FIRST_LIVE_PASSIVE_RX_RESULT_20261019.md). No confidential source published.

---

# 2026-10-19 — NEWEST: V5DCM45-FIX1 first user passive boot log RUNNING / PARTIAL; native TX PREPARED / NOT RUN. FIX1 permanently REVOKED immediately despite clean RX (687 frames by ~16:04:42; resync/drops/badGeom/unknown=0, B11D first fault NONE, DE=0, Arm=0, native FC23=0). Source shows candidate startup ordering bug: FreshRx::observe() requires b11d_started=true before raw B11D initialized, and irrevocably revokes on initial false. No TX attempted; HA data present. Source-only FIX2 should defer initial qualification until B11D readiness, without weakening any subsequent fail-closed fault. [New local result](V5DCM/V5DCM45_FIX1_FIRST_PASSIVE_STARTUP_REVOKE_20261019.md).

# 2026-10-19 — PRIVATE FIX1 INDEPENDENT RECOVERY **COMPLETE / POSITIVE OFFLINE ONLY; COMPILE/FLASH/TX PREPARED / NOT RUN.** [distinct recovery result](V5DCM/V5DCM45_FIX1_INDEPENDENT_RECOVERY_RESULT_20261019.md). Exact user V45 base; new independent private ZIP SHA256 `fd004cf1aa0edf2adbe6569a56cf453e1401bf0010378e4e5107aa40c894f067`, sole YAML SHA256 `88632deb095ab940ee47a4e8bd88d896478f43b6270e20a08d3aced556e7760e`; 57/57 new guard C++17 checks, 66-member ZIP/hash + YAML/HA-entity validations PASS. Not identical to earlier offline FIX1 ZIP; original proprietary backend unchanged. User device still V45 passive, P5_history preserved, current native FC23 zero. Do not infer native session/TX; first physical reply remains PREPARED / NOT RUN. No other status changed.

---

# 2026-10-19 — LATEST: **V5DCM45-FIX1-FRESH-RX-SOURCE-01 COMPLETE / POSITIVE OFFLINE ONLY; REAL ESPHOME COMPILE/FLASH AND NATIVE TX PREPARED / NOT RUN.** [PREPARED](V5DCM/V5DCM45_FIX1_FRESH_RX_PREPARED_20261019.md) → [OFFLINE RESULT](V5DCM/V5DCM45_FIX1_FRESH_RX_OFFLINE_RESULT_20261019.md). Current actual user device remains previously flashed V45 (first passive log 195.6s), where 7 pre-existing parser resyncs did not increase, B11C/B11D no new fault, old P5_history=1, TX build=1, DE0, 0 output/Arm and **0 native challenge**. FIX1 source isolates current RX witness after >=30s and >=100 new good complete frames, disallows stale validated frame (>3s), resets qualification window for a new pre-qualification resync and permanently revokes a newly observed error after qualification; original P5/B11D sticky histories unchanged. Rejected Arm during failed qualification no longer consumes the only accepted single-use Arm. One additional HA diagnostic `V5DCM45 FIX1 Current RX Qualification`; original V43 denial, GPIO21/UART/OTA/API, 117 sensors, 13 binaries, 11 HA buttons and 51 original text sensors intact (now 52 text). Single private ZIP sha256 `7f130635c5b8ef59f3cba9b17afd229b7afd5ee67856d1281300331ec5496791`, one YAML sha256 `37f295903aa92e2efa9b57a2a08d44acabb2572020aa81d35bcba795290df4fc`; 66 ZIP entries, 65 individual source member pins, CRC/shas/cold extraction confirmed. Native backend byte-for-byte same original V45. **56/56 FIX1 + 40/40 V45 DE + 32/32 V44B fake-IDF tests PASS = 128/128 strict offline cases**. Real ESPHome compile and FIX1 flash **NOT RUN**. User can compile single YAML and report status; do not treat host PASS as device acceptance or live TX. Current native FC23 request still zero and sender/epoch/slot unknown, no guaranteed output even after user Arm. Preserve V44B no-TX and FIX-B2/FIX2 rollback, original user V45 logs and previous V45 RUNNING/PARTIAL historical record. Never publish confidential native backend or keys.

---

# 2026-10-19 — LATEST HANDOFF: **FIRST USER LIVE V5DCM45 PASSIVE LOG = RUNNING / PARTIAL, FIRST NATIVE TX PREPARED / NOT RUN.** [Raw-log source findings](V5DCM/V5DCM45_FIRST_LIVE_PASSIVE_P5_ARM_GATE_20261019.md). User supplied `Pasted text(20261019-123601).txt` 5,000 lines, 14:32:31–14:35:46 (195.6 s), SHA256 `768825d91e8f35b37d8fd3a6e0fdacc3b8fecac1ef344b9cb1b9afca0e288eea`. Confirms user V45 TX-capable source on ESP: new status `build=1`, 39 snapshots step0/deny0/armClicks0/replyAttempts0/uartAttempt0/admitted0/DE_RX1, B11D `ownedSamples=0 unsafeSamples=0 sticky=0 DE_sw=0 DE_pin=0`. Parser frames798→2416, drops0, resync **7 unchanged through excerpt**, B11C/B11D 0 new CRC/byte/fault, HA updates. **CRITICAL NEW FUNCTIONAL BLOCKER:** existing R6-P5 historical latch `P5_history=1`, R6-P5 `FAULT_LATCHED`, first 7 parser resync predate log. Current V45 Arm source explicitly requires `!id(r6p5_meta)[4]` and increments one-use `arm_presses_` before evaluating that predicate, so a user clicking V44B Arm now **will be denied and consumes only click this ESP boot**. P5 latch is sticky since any parser resync>0 under old R6-P5 source; do NOT reset faults, reboot to bypass, or tell user to Arm immediately. Independent native trigger still **not observed**: P74E `FC16=390 FC23=0` for 0x0F controller-native request; V45 cannot send unsolicited reply. **Next source action**: explicitly differentiate historical startup P5 vs fresh session-integrity for V44B Arm/on_crc/tick/B11D owner, preserving sticky P5 evidence and fresh-error fail-close, and investigate missing 0x0F challenge offline. User wants practical one ZIP/one YAML, no script combining and no generic G01–G06 replay. Current healthy device V45 passive; verified prior fallback V44B no-TX and FIX-B2/FIX2. No Arm/no UART/DE driven in user V45 log, no live semantic native approval, owner/epoch/electrical timing unknown; no OTA digest verification. V45 prior 40/40 + V44B 32/32 offline still positive; live TX separate experiment remains PREPARED / NOT RUN.

---

# 2026-10-19 — LATEST HANDOFF: **V5DCM45-B11D-TX-OVERLAP-SOURCE-01 COMPLETE / POSITIVE OFFLINE ONLY; REAL V45 COMPILATION/FLASH AND PHYSICAL NATIVE REPLY PREPARED / NOT RUN.** [Prepared](V5DCM/V5DCM45_TX_AWARE_B11D_ONE_SHOT_PREPARED_20261019.md) → [source result](V5DCM/V5DCM45_TX_AWARE_B11D_ONE_SHOT_OFFLINE_RESULT_20261019.md). Based on **locally verified user-running V44B compile-only source** (real 200.41s RX/HA positive, B11C/B11D 0 fault, V44B build=0, TX0). Newly prepared **PRIVATE one ZIP/one YAML** V45 TX-capable source: archive SHA256 `b77e4f20b64aa8503f2c5889f6e308678af4d4dd04e4a0e52391f1cf36363df5`; candidate YAML SHA256 `428cb1e087d7e35d7bc806afca57ca36e8425ba6c7ed1dd2980587b5034d5941`, 65 ZIP entries, 64 member manifest SHA checks, clean extract host regressions PASS. **Both V42 compile TX enables ON in V45**, unlike currently flashed V44B build=0. No auto-initiation: only manual Configuration Arm once/boot valid 30s, then only genuine fresh CRC-good native `0x0F FC23` read `0x0730/8` write `0x071C/8` bytecount16; private current-request-dependent 21-byte reply including CRC, MAX ONE TX reply, 70ms response cutoff from parser callback, Abort returns DE to RX. Actual physical owner/epoch/slot/wire EOF XTR unproven, accepted risks G01–G06 retained but NOT relitigated. **One bounded B11D change:** original 50ms sentinel now requires actor actually in TX Fill/Drain/PostGuard, same boot/one attempt/same GPIO+switch DE=high/no fault/no competing peer/current callback within 70ms, to pause only that scanner tick; all unowned DE, switch/GPIO mismatch, old legacy output or stale slot still cause original sticky B11D first fault + Abort. Original independent B11D raw parser and P5 history NEVER reset; old B11C/B11D status and red/brown logs preserved, plus one new diagnostic text. Production 117 sensor/13 binary/11 button/50 old text IDs retained, 51 text total, new globals2, no extra UART reader. **Validated:** V45 source/fake-IDF 40/40 scenarios, original V44B fake-IDF 32/32, genuine historical Eco5 and collaborator ATEC+DCM03 seven exact replies, 256 independent Python oracle matches, 32 bad CRC denies. Native backend byte-exact unchanged. **Current local XTR canonical native 0x0F FC23=0** in prior V44B running log: Thermia Connect firmware is passive 0x0F RTU slave, does not initiate handshake; reason controller has not sent challenge remains OPEN, do not invent scans/unsolicited writes or a DCM capture unavailable to user. **V45 NOT compiled on actual ESPHome/ESP-IDF, NOT FLASHED, NOT ARMED, NOT on-wire tested.** Current device stays V44B known good build0. **NEXT:** user compile only single V45 YAML on ESPHome 2026.9.0; review compiler result and exact user-initiated max-one native reply experiment/abort/recovery before any flash. Recovery V44B no-TX and verified FIX-B2/FIX2 RX-only. Never publish confidential native backend/key/cipher or command-mailbox tooling. V44-A earlier Arm denial/Abort RUNNING/PARTIAL remains recorded.

---

# 2026-10-19 — LATEST HANDOFF: **V5DCM44-B COMPILE-ONLY ON-DEVICE PASSIVE RUNTIME COMPLETE / POSITIVE**. [User-flashed compilation report](V5DCM/V5DCM44B_COMPILE_ONLY_USER_COMPILE_FLASH_PARTIAL_20261019.md) followed by [actual RX/HA runtime RESULT](V5DCM/V5DCM44B_COMPILE_ONLY_POSTFLASH_RX_RESULT_20261019.md). Source-based compile-only V44B (physical TX flags ABSENT) user compiled and flashed. New raw user log `Pasted text(20261019-115204).txt` SHA256 `6e0e80c33d2bdef3614a039bedb5a351a6016ea04f1a3888de911637fad63626`, exactly **5,000 lines from 13:48:18.926–13:51:39.336**, 200.41 s; uptime 271→421s in sampled interval. V5 parser **2130→3753 valid frames (+1623), pages 348→611 (+263), badGeom=unknown=resync=drops=TX=0**. B11C CRC checked 2306→3579 with mismatch=0; B11C portable V5/portable=3589/3589, all differentials/faults=0. B11D raw/portable compared 3589/3589, count/byteDiff/nativeFault=0, DE=0, no historical sticky P5 change, First Fault NONE. V44B new status **40 snapshots consistently `step=0 deny=0 armClicks=0 replyAttempts=0 uartAttempt=0 admitted=0 build=0 DE_RX=1 conflicts=0`**; old UART Write Calls=0, physical attempts=0, delivered=0, Core remains HARD_DENY. HA sensor updates continue (room/outdoor/supply/DHW); some unproven semantic entities still nan. **Still zero actual LOCAL native `0x0F FC23`**; R6 P74E `FC16=614 FC23=0`, owner/epoch/response-slot/wire EOF UNKNOWN, C2/Online unproven. Last actual flashed OTA binary digest not measured; hardware GPIO not probed on oscilloscope; do NOT upgrade to live TX. No additional passive 3-min test needed. **NEXT OFFLINE:** fix/reconcile the known source conflict where old B11D 50ms RX-only supervisor treats intentionally HIGH DE as sticky fault; preserve all original B11D/P5 history and flag unexpected DE as before, allow only exact bounded native user-armed TX interval with automatic RX restoration. Also investigate why XTR has not initiated native challenge using existing firmware/historical evidence, without scans/unsolicited TX. The next TX-enabled image is NOT YET PREPARED/FLASH-READY; separately user-initiated first native reply remains PREPARED / NOT RUN, with private reply/CRC and one-shot abort/recovery review. Working current device = V44B safe no-TX; rollback V43-FIX1/FIX-B2/FIX2 RX-only. Prior V44-A manual denial + Abort recorded separately RUNNING / PARTIAL for its missing 20s post-Abort evidence; V44B runtime success does not erase that result.

---

# 2026-10-19 — LATEST: **V5DCM44-B COMPILE-ONLY user reported COMPILE + FLASH succeeded; RUNNING / PARTIAL pending post-flash logs.** [Record](V5DCM/V5DCM44B_COMPILE_ONLY_USER_COMPILE_FLASH_PARTIAL_20261019.md). User says “gelukt en geflashed” after receiving **one complete ZIP with one YAML**. Assistant verified given ZIP SHA256 `c504934004331f3b3e44b1163a24a4c052d208e7a4aa0555a0158b1f9b1b1295`, ZIP CRC valid, YAML inside SHA256 `2b54ef5211bf0bbafe167803cf1401a9a7127177ae4c305263775c21aef40d9b`; exact ESP32 flashed OTA binary digest NOT available, compiler output NOT requested/collected. **Build flag gate still OFF:** V42 header requires BOTH `V5DCM42_PRIVATE_TX_BUILD` and `V5DCM42_HARDWARE_PORT_REVIEWED`; neither is present in this compile-only YAML, so `kBuildMaySend=false`, manual Arm cannot enable TX. **NOTE:** V44B code includes misleading unconditional log text `PRIVATE TX-ELIGIBLE BUILD` even when no build flags; use actual runtime `build=0` and UART/DE logs, not text. Installed device source family V44B by user report; no new post-flash RX/HA confirmation yet, no actual native 0x0F FC23 handshake or response sent/observed. Existing B11D 50ms DE-high sticky fault with future TX remains unresolved. Old V43 FIX1 good RX, V44-A two denied Arms+Abort with zero UART, RUNNING / PARTIAL post-Abort log, original FIX-B2/FIX2 fallback. **NEXT:** collect ONE passive 2–3 minute V44B ESPHome log only, without Arm, confirm `build=0`, parser/RX/HA B11C/B11D stability, DE=0, old/new TX counts zero; then analyze dedicated B11D/TX overlap offline and prepare later TX-enabled source separately. No live TX now.

---

# 2026-10-19 — LATEST HANDOFF: **V5DCM44-B source/host COMPLETE / POSITIVE; source-verified COMPILE-ONLY preflight COMPLETE / POSITIVE; actual ESPHome V44-B compilation and real XTR native TX PREPARED / NOT RUN.** [V44B contract](V5DCM/V5DCM44B_SINGLE_RESPONSE_SOURCE_PREPARED_20261019.md) → [source result](V5DCM/V5DCM44B_SINGLE_RESPONSE_SOURCE_RESULT_20261019.md) → [compile preflight](V5DCM/V5DCM44B_COMPILE_PREFLIGHT_HOLD_20261019.md). V43-FIX1 (user running, last live on-device V44-A buttons) unchanged. V44-A linked [RESULT](V5DCM/V5DCM44A_ARM_ABORT_RESULT_20261019.md): RUNNING / PARTIAL because Arm DENIED and Abort executed safely, step7 after Abort intentionally latched by source, only four seconds post-Abort. V44-B private overlay derives from exact V43 FIX1 ZIP SHA256 `2bda32cc2efa92678ca9f9a6f615134e430884552ecabdcec667ba57f830ba47`, old original FIX-B2/FIX2 RX-only recovery available. Original V44-B fake-IDF 4x8=32/32 runs PASS, prior V42 six host variants, V43 reference historical 7/7 cross-model exact (Eco5+collaborator ATEC, NOT local XTR). Compiler-only separate generated YAML SHA256 `2b54ef5211bf0bbafe167803cf1401a9a7127177ae4c305263775c21aef40d9b` keeps 117 sensors, 13 binary, 50 text sensors and 11 buttons; both physical TX build flags deliberately ABSENT. Private-script-only no-key/no-algorithm compiler-preflight ZIP SHA256 `a6c399f097f67fb0cebddc8a4612e92c2eaf8bdb14fe19986fecd4c3582aaf56` manifest and clean regenerate verified. **IMPORTANT NEW BLOCKER:** original FIX-B2 B11D 50ms RX-only sentinel treats any DE HIGH as STICKY ERROR. The V44-B previous 1s DE watchdog exception does NOT prevent this; REAL TX-ENABLED V44-B MUST NOT BE FLASHED until its overlap is reconciled without clearing/replacing sticky B11D/P5 evidence. New Mac-side next action is `esphome config` and `esphome compile` on no-TX compiler-only YAML, no flash. Real device native FC23 seen=0 in last user logs, so responder trigger not yet locally observed; app C2/Online UNKNOWN. No actual V44-B ESPHome compiler, flash, direct UART/DE or physical controller test occurred. NEXT investigate appropriately scoped TX-aware B11D accounting separately, then only user-initiated bounded first genuine native trial after exact current-frame/CRC and recovery review. No private algorithm/keys/public emulator code pushed to GitHub.

---

# 2026-10-19 — V5DCM44-A **PREPARED / NOT RUN**: user-initiated denial-only HA Arm→5s→Abort test on verified running V43 FIX1; no new flash or native TX. [Contract](V5DCM/V5DCM44A_ARM_ABORT_DENIAL_LIVE_PREPARED_20261019.md). V43 last user log 1150 frames, RX/B11C/B11D fault 0, TX UART0, GPIO21 DE LOW, status build=0/TX=HARD_DENY with owner/epoch/slot/timing unknown. User must press HA buttons and supply pre/after relevant log; **do not claim executed/positive before evidence**. If DE high or UART write >0 stop, Abort and fallback FIX-B2/FIX2. Previous V43 and V41/V42 evidence unchanged.

---

# 2026-10-19 — LATEST HANDOFF: **V5DCM43-PRIVATE-ESPHOME-INTEGRATION-OFFLINE-01 COMPLETE / POSITIVE (SOURCE/YAML/HOST/FAKE-IDF ONLY); REAL DEVICE TX PREPARED / NOT RUN, NOT FLASH-READY**. [PREPARED](V5DCM/V5DCM43_PRIVATE_ESPHOME_INTEGRATION_PREPARED_20261019.md) → [RESULT](V5DCM/V5DCM43_PRIVATE_ESPHOME_INTEGRATION_RESULT_20261019.md). User-requested joining of V41 reference-derived native dynamic answer, V42 bounded one-shot TX state machine, and exact ORIGINAL V5DCM33-FIX-B2 ESPHome single-parser/UART/DE/HA now done as **private source candidate** `waveshare-thermia_V5DCM43_PRIVATE_NATIVE_INTEGRATION_OFFLINE_NOT_FLASHED.yaml` SHA256 `959bc5cee094715e3475263207736146bc146ff48760619df4d8020f9939991c`. Exact source B2 ZIP `fdc09c5927b5a351163db95db96dc467abd43cb27e1e7fc8068782bea4a677c7` and original YAML `32e1b7c3ea4f7411fb94d6d769370b9ae10874403961403002250b96e4365d46` verified. **All 117 sensors/13 binary sensors/48 original text sensors and 7 old HA buttons preserved**; new 2 manual HA buttons in Configuration (Arm One-Shot Native DCM/Abort Native DCM TX), new diagnostic text. Existing ESP32-S3 ESP-IDF 9600 8E1, GPIO17/18, ESPHome-managed DE switch GPIO21, original RX callback and red/brown logs unchanged except **one** CRC-complete hook after existing parser; driver borrowed post-hardware startup, no secondary UART reader/install or RX flush. Private C++ native backend validated against **7/7 independent genuine HISTORICAL cross-model DCM responses**, plus **256 C++ versus existing independent Python synthetic reference matches** and **32 bad-CRC denies**. Exact original V42 C++ policy **6/6** compiled/run variants and V43 borrowed ESPHome switch/UART fake IDF **4/4** compiled/run PASS. Confidential 75-file private NONFLASHABLE archive SHA256 `c74f9105d66d21b2a37b5204434953375a7036431f2997b8aeb3df8df223e745` SHA manifest verified and full runner fresh-extract EXIT0; source/private cryptographic implementation NOT COMMITTED to public repo. **Current XTR physical owner/epoch/slot/deadline not independently known**; source hard-denies ARM by holding them false, timing not qualified, double TX macros absent; no actual native TX. Real ESPHome compiler NOT INSTALLED/NOT EXECUTED, no flash, ARM, controller restart, GPIO/physical UART test, new user logs, profile C2/Online, or live XTR acceptance. **User running device UNCHANGED V5DCM33-FIX-B2** latest 204s RX/HA positive 393/393 HARD_DENY UART writes=0, flashed image hash unknown, safe rollback V5DCM23 FIX2 RX-only; V4.1 EXP386/387 local positive, EXP388 partial, V5DCM32 B11D live negative preserved; Oct03 genuine capture belongs to collaborator ATEC/DCM03 NOT local XTR. **NEXT:** separately qualify actual ESPHome compilation and physical borrowed UART/DE plus current accepted-risk owner/epoch/slot/timing policy and exact protected current reply CRC, then a distinct user-initiated one-response live experiment with immediate abort/FIX-B2-FIX2 rollback; never claim live because host tests passed.

---

# 2026-10-19 — LATEST HANDOFF V5DCM42: **BOUNDED TX SOURCE/HOST/FAKE-IDF COMPLETE / POSITIVE; physical native TX PREPARED / NOT RUN (NOT READY TO FLASH).** [PREPARED](V5DCM/V5DCM42_BOUNDED_TX_BOUNDARY_OFFLINE_PREPARED_20261019.md) → [RESULT](V5DCM/V5DCM42_BOUNDED_TX_BOUNDARY_OFFLINE_RESULT_20261019.md). Fresh exact source audit of user FIX-B2 ZIP SHA256 `fdc09c5927b5a351163db95db96dc467abd43cb27e1e7fc8068782bea4a677c7` and source YAML SHA256 `32e1b7c3ea4f7411fb94d6d769370b9ae10874403961403002250b96e4365d46`: original ESP32-S3 ESP-IDF 9600 8E1 / UART GPIO17/18 and existing DE GPIO21, original private adapter forced output false, bounded B2 driver production native TX false. Separate new private TX-capable source `OneShot` has two explicit build switches, user one-shot scope, current exact CRC-qualified native 0x0F FC23, ongoing fresh boot/generation/B11D/P5/collision/slot/owner/epoch checks, injected opaque reply backend, finite preguard→FIFO→drain→DE-low state machine with abort and buffer wipe. **Strict 6-build C++17 fake-port suite PASS** (3 deny builds 449 each, 3 opt-in fake builds 460 each); **4096 original V39 frame-geometry comparisons PASS**, **4 fake ESP-IDF borrow-port stub builds PASS**, ASan/UBSan fake 460 PASS, parent source audit PASS. Private NONFLASHABLE 15-file archive SHA256 `a6906c78887e6a8e376fecbb7209a2bc72cf7ad2b47798e4b52dedfa67ebb53b`, 14 SHA manifest files and archive CRC verified, clean-extract complete runner exit0. **No working native ESP32 confidential backend, NO ESPHome RX callback binding/Configuration buttons, NO real ESP-IDF compile/flash, NO physical UART/DE testing, NO actual TX or controller acceptance.** Current user device STILL **V5DCM33-FIX-B2** last 204 s live RX/HA positive, TX executor 393/393 HARD_DENY, UART=0; binary hash unverified, rollback V5DCM23 FIX2 RX-only. Historical V4.1 EXP386/387 local positive, EXP388 partial; V5DCM32 rejoin negative preserved; Oct03 genuine ATEC/DCM03 not local XTR. G01–G06 user accepted research risks remain accepted, not falsely promoted to independently measured physical slot/owner/epoch. **NEXT** source-review and add confidential native C++ response backend, exact original ESPHome UART/DE and B2 CRC RX callback integration, finite Configuration ARM/CANCEL, calibrated physical slot/EOF, private exact current-request response bytes+CRC and abort+FIX2 fallback. No live test until separately user-initiated and scoped. V42 source ZIP private, GitHub sanitized docs only.

---

# 2026-10-19 — LATEST VERIFIED HANDOFF **V5DCM41-PRIVATE-DYNAMIC-REFERENCE-BACKEND-OFFLINE-01 COMPLETE / POSITIVE SOURCE/HOST ONLY**. [PREPARED](V5DCM/V5DCM41_PRIVATE_DYNAMIC_REFERENCE_BACKEND_PREPARED_20261019.md) → [RESULT](V5DCM/V5DCM41_PRIVATE_DYNAMIC_REFERENCE_BACKEND_RESULT_20261019.md). New genuine **dynamic per-request source-pinned external reference callback** bound to byte-identical original V39/V38 BoundProvider; NOT a recorded-answer lookup, NOT a flashable real DCM responder. Exact external firmware reference Git blob `2aeb56f3afb60414f0527acd6960996219a0b0fb` and parent V39 SHA `35195716ec530ee512776e9bd6aba3a3780bcf0635edc0554d6745f6e11ebada`, B2 source/YAML pins verified. **7/7 genuine historical DCM cross-model responses byte-exact** (Eco5 Sep26 two, Sep28 four, collaborator ATEC+DCM03 Oct03 one; Oct03 NOT local XTR), **256 newly generated nonhistorical requests** reference-consistent (not independent cipher oracle), **427 negative/control assertions**. Critical V39 risk: 8 incorrect cipher outputs with valid Modbus CRC pass structural host mock, detected only by independent oracle comparison; they are NOT V39 rejection victories. Ordinary host default and `ARDUINO`/`ESP_PLATFORM` even with test macros deny before oracle call, missing live sender compiler negative, sticky/session/CRC/geometry/source guards host tested. **Private 9-file NONFLASHABLE no-key/no-algorithm ZIP SHA256 `8596434e26d90172d5d4eb930b49981e86020910dfe6d21e57ac16dc385382cb`**, 8 manifest member SHA + CRC verified, fresh extract complete runner exit 0. **Actual user ESP32 UNCHANGED V5DCM33-FIX-B2** last 204s proven RX/HA and HARD_DENY 393/393 UART=0, flashed binary digest unknown, fallback V5DCM23 FIX2 RX-only, B2 new >90s post-gap live NOT RUN. V4.1 EXP386/387 local positive, EXP388 PARTIAL, V5DCM32 integrity-denied rejoin NEGATIVE preserved. **Still OPEN:** current XTR physical owner/epoch/slot, real native response/controller acceptance, hardware TX, app C2 33/33 and Online. No ESPHome compile, ARM, restart, flash or TX. **NEXT** new private V42 bounded live-readiness contract and exact FIX-B2 output/slot/owner evidence review, then separately user-initiated real trial only after private exact response+CRC/current state/timing/abort/rollback. Public GitHub only sanitized report, never security algorithm/key/private native implementation. 

---

# 2026-10-19 — LATEST HANDOFF: **V5DCM40-GENUINE-DCM-HISTORICAL-PARITY-01 COMPLETE / POSITIVE OFFLINE; current XTR physical DCM acceptance OPEN/UNKNOWN.** [PREPARED](V5DCM/V5DCM40_HISTORICAL_CRYPTO_PARITY_PREPARED_20261019.md) → [RESULT](V5DCM/V5DCM40_HISTORICAL_CRYPTO_PARITY_RESULT_20261019.md). Critical V39 correction: pre-existing 2026-10-05 firmware repo already had **7/7 genuine reference handshake matches**. V40 independently reran exact Git-blob-pinned external reference `2aeb56f3afb60414f0527acd6960996219a0b0fb` against original Eco5 Sep26 (2), Sep28 (4), ATEC+DCM03 Oct03 (1) raw captures; **7/7 exact CRC-valid responses**, 21/21 corrupt/modified/geometry negative controls, historical 29–63ms observed only. Original source-pinned V39 BoundProvider processed 7 recorded-pair-only host mock fixtures **184/184** C++17 assertions PASS and denied unknown changed challenges. Original V39 2926/2926, V38 318/318, handler 256 stubbed fixtures and default/ESP_PLATFORM/ARDUINO DENY rerun PASS. New private **8-file NONFLASHABLE no-key/no-algorithm ZIP SHA256 `dbe134f3a11826c7beb3177d16bfa44d90f925711c78bba373845fab78a06be7`** CRC/SHA checked and freshly extracted full runner exit 0 with external source+captures. **CRITICAL PROVENANCE ERRATUM:** `thermia_capture_20261003_165355.log` is genuine collaborator **ATEC + DCM03**, NOT local XTR despite mistaken V35–V39 labels; Sep25 old thermia_capture hardware model UNKNOWN. Historic CRC/page counts are preserved but no October 3 old 31/33 counts qualify local XTR current model. No new native XTR acceptance, owner/slot/epoch, physical response, C2, Online or dynamic V39 self-contained backend proven. **Current ESP32 unchanged V5DCM33-FIX-B2**, last 204s user passive healthy HA and HARD_DENY 393/393, UART=0, flashed binary SHA unverified, fallback V5DCM23 FIX2 RX-only; B2 >90s postgap NOT RUN. Historical V4.1 EXP386/387 positive, EXP388 PARTIAL and V5DCM32 rejoin negative preserved. **NEXT** separately private V41 dynamic backend integration/reference and held-out proofs, then only user-initiated strictly bounded hardware trial with explicit private exact reply/CRC, controller state, owner/slot/epoch, one response, abort and rollback. No firmware/YAML edits/ARM/restart/TX now.

---

# 2026-10-19 — LATEST HANDOFF: **V5DCM39-REQUEST-BOUND-REFERENCE-01 COMPLETE / POSITIVE OFFLINE SOURCE/HOST ONLY; NATIVE CRYPTOGRAPHIC BACKEND / REAL DCM ACCEPTANCE OPEN/UNKNOWN**. [PREPARED](V5DCM/V5DCM39_REQUEST_BOUND_BACKEND_PREPARED_20261019.md) → [RESULT](V5DCM/V5DCM39_REQUEST_BOUND_BACKEND_RESULT_20261019.md). Corrected concrete V38 gap: V38 `Request` only metadata, not original CRC-qualified native request bytes needed by firmware's request-dependent backend. New separate original-B2-source-pin, NONFLASHABLE host-only `BoundProvider` holds exact verified incoming FC23 frame for **one** abstract backend call, then wipes it; external profile + existing B11D/P5 and one-scope checks remain fail closed. **2,926/2,926** new strict C++17 host checks PASS, original V38 **318/318** PASS. Actual pinned original Connect 2.1.105 Python handler dynamically source-loaded and executed with **stubbed** cryptography / fake in-memory register bank for **256** synthetic examples PASS for input extraction, quantity guards, register placement and software RESPONSE_SENT. **NO genuine cryptographic output was computed/compared; parity not proven** (original xxtea library ARM-only), no native physical reply/owner/slot/controller epoch/C2/Online. V39 strengthens V38 simulated-output guard: ordinary host DENY unless explicit OFFLINE_HOST_TEST; `ESP_PLATFORM` and `ARDUINO` always DENY even with macro; absence of live sender compiler negative. User-installed XTR still V5DCM33-FIX-B2 last 204s passive clean/HA, 393/393 HARD_DENY, UART writes=0, compiled image hash unknown, fallback V5DCM23 FIX2 RX-only. No device ARM/flash/controller restart/TX/YAML change. Private 11-file ZIP SHA256 `35195716ec530ee512776e9bd6aba3a3780bcf0635edc0554d6745f6e11ebada` created, member-checks and fresh extraction full runner exit 0, shared only privately. Original V4.1 EXP386/387 local positives, EXP388 PARTIAL, V5DCM32 negative and V35–V38 offline history preserved. **NEXT:** private original cryptographic dependency/reference parity research, then a new separately scoped user-initiated controlled live test only with exact reviewed private output CRC, current owner/epoch/slot/state, one attempt, abort/recovery. Never conflate source-stub or mock with real controller acceptance.

---

# 2026-10-19 — LATEST HANDOFF V5DCM38-PRIVATE-RESPONSE-PROVIDER-OFFLINE-01 **COMPLETE / POSITIVE (HOST/SOURCE ONLY)**. [Contract](V5DCM/V5DCM38_PRIVATE_RESPONSE_PROVIDER_PREPARED_20261019.md) / [Result](V5DCM/V5DCM38_PRIVATE_RESPONSE_PROVIDER_RESULT_20261019.md). New private NONFLASHABLE 8-file V38 provider interface ZIP SHA256 `9e28f3ed2ae3bf95f79b69c2b72eebf5d228bd306147285aa906a73400be6767` created/manifest-checked/extracted/fully rerun **318/318 C++17 host assertions PASS**, embedded ESP_PLATFORM simulated-send forced DENY, nonexistent live sender compile rejected, exact FIX-B2 ZIP/YAML/Core and source-output pin PASS. This is **only an interface** for a separate future confidential request-dependent backend, not the actual native vendor approval algorithm or usable DCM responder. No device change, no live TX; current user ESP32 still FIX-B2 last 204s good RX, HA, 393/393 HARD_DENY, UART=0, rollback FIX2 RX-only. No current physical owner/epoch/slot, real native controller acceptance, profile C2, Online or semantic write proven; all remain OPEN. Preserve original V4.1 EXP386/387 positive, EXP388 partial, V5DCM32 live rejoin negative and V37 results. **NEXT:** separately scope V5DCM39 private backend/reference parity offline, then user-initiated bounded physical experiment only after independent current slot/epoch/owner and exact private payload review. V38 private archive kept in chat only; public GitHub documentation sanitized. 

---

# 2026-10-19 — LATEST HANDOFF: V5DCM37 offline COMPLETE / POSITIVE; independent recovered artifact also COMPLETE / POSITIVE OFFLINE.

Continuity fixed: previous GitHub V37 result reports 1017 host cases but its original ZIP was unavailable; do not claim its bytes were reverified. A DIFFERENT reconstructed V37 19-file NONFLASHABLE ZIP is newly provided to user: V5DCM37_REPRODUCED_OFFLINE_NOT_FLASHABLE.zip, SHA256 f94b6cccf9982df79b3eecf21693f1a4e1b82a9e6429c82effa5987dc6eafc19. Reconstructed 11507/11507 C++17 assertions PASS; V35 192+18, V36 53, B2 65+70 local historical CRC fixtures, FIX-A 52+32, V31 61 and V32 34 all PASS; four original/collaborator captures 23472 CRC-valid, 0 bad. Three compiler-negative and one tampered-source tests PASS. New archive SHA manifest 18/18 + CRC verified; full runner fresh-extracted EXIT 0. [Separate evidence](V5DCM/V5DCM37_REPRODUCED_ARCHIVE_VERIFICATION_20261019.md).

Five offline axes: synthetic FC23/mock-delivery/fresh FC16 internal shadow, retained/recovery candidates, strict provenance and original B11D/P5 fault protection, exact 33 source profile shapes 15+10+8 (not C2), pinned user-private B2 Core and DENY-only output. These are not physical owner/slot/epoch, real native response, controller acceptance or Online.

CURRENT USER DEVICE UNCHANGED: V5DCM33-FIX-B2, last 204s passive user log locally positive, HA working, UART writes 0, software TX attempts 0 and HARD_DENY. V4.1 EXP386/387 historical positive, EXP388 partial, V5DCM32 restart negative preserved; B2 post-gap retention live still untested. No ESPHome compile, ARM, controller restart, flash or new device TX in V37. Next plan a separately scoped, private, bounded native response experiment only after independently qualified slot/owner and exact private payload review.

---

# 2026-10-19 — CURRENT V5DCM37 handoff verified: V5DCM37 combined offline COMPLETE / POSITIVE; separate new spot check COMPLETE / POSITIVE (source/host/history ONLY). Original V37 1,017 checks and independent 2,848 checks remain historical validated reports, NOT re-run under this new audit. This turn freshly compiled the exact private B2 passive 33-profile witness **113/113 PASS**, verified pinned source ZIP/YAML/header, validated **23,472/23,472 CRC good** in four historical XTR/Eco5 logs and current-modern geometric coverage 31/33 Oct03 XTR, 24/33 Sep25 XTR, 33/33 each Eco5 collaborator (entire recordings, not same-session C2). Separate **six-file NONFLASHABLE** ZIP SHA256 `050b98fe4b1dbd25d8a613ae2cf84ce74b80acb102fc68d06958aa48ecd3d55e` built/re-extracted/rerun PASS, private chat only. [New evidence report](V5DCM/V5DCM37_SOURCE_CAPTURE_SPOTCHECK_RESULT_20261019.md). User device still V5DCM33-FIX-B2 last 204s passive, 393/393 HARD_DENY, UART=0; no user live actions, no actual vendor DCM controller acceptance/physical responder/epoch/slot/Online/C2, no flash/ARM/restart/TX. **NEXT:** separately scoped private dynamic response-provider preflight after source/slot/owner/epoch and guarded current payload/CRC evidence, not another unbounded RX shadow test.

---

# 2026-10-19 — CONTINUITY CORRECTION: **V5DCM37-COMBINED-DCM-OFFLINE-01 COMPLETE / POSITIVE (SOURCE/HOST/HISTORICAL CAPTURE ONLY), NOT LIVE.** This result was already recorded in [V5DCM37 RESULT](V5DCM/V5DCM37_COMBINED_DCM_OFFLINE_RESULT_20261019.md) and EXPERIMENT_LOG/PROTOCOL_FINDINGS, while this canonical STATE header had incorrectly remained on V5DCM36. Existing V37 report records five independently tested offline axes, 1017/1017 C++17 host checks, pinned B2 source, 33 profile-group shape analysis and preceding V35/V36 regressions. **The historic V37 nonflashable ZIP SHA256 f656c09082f6077b84db216570666a96a097ad85e676a9d693efee2e47f8974f and runner results are documented but this archive is currently absent from the mounted workspace; their exact bytes cannot be independently reverified solely from the GitHub report.** Any newly generated reconstruction must have distinct hash/provenance, not masquerade as the archived original. User's latest proven ON-DEVICE image family remains **V5DCM33-FIX-B2** with the 204s stable passive baseline and HARD_DENY, no new flash/ARM/restart/TX, no proven native DCM physical response, owner/epoch/slot, 33/33 current C2 or Online. Next: recreate/retest a clearly separately identified offline V37 reproduction artifact and keep V37 physical acceptance UNKNOWN; no device action. Exact historical V37 Prepared: [PREPARED](V5DCM/V5DCM37_COMBINED_DCM_OFFLINE_PREPARED_20261019.md), Result: [RESULT](V5DCM/V5DCM37_COMBINED_DCM_OFFLINE_RESULT_20261019.md).

---

# 2026-10-19 — **CURRENT HANDOFF: V5DCM37-COMBINED-DCM-OFFLINE-01 COMPLETE / POSITIVE (SOURCE/HOST/CAPTURE ONLY), independently REPRODUCED with a separate source-only suite COMPLETE / POSITIVE.** Earlier canonical sync was inconsistent: EXPERIMENT_LOG and PROTOCOL_FINDINGS already had the first V37 1,017-host-test result while STATE incorrectly pointed at V36. **Corrected here without overwriting past results.** New independent C++17 harness **2,848/2,848 PASS**, prior V36 source-pinned Core+output **53/53 PASS**, V35 mock **192/192+18/18 PASS**, 3 forbidden compiler access attempts denied, altered B2 parent rejected, B2 ZIP/YAML hash verified, all **23,472 historical captured frames CRC good/0 bad**, original local Oct03 modern 31/33 (15/8/8; legacy 03E8/count13), local Sep25 24/33 (14/8/2), Eco5 collaborator Sep26/Sep28 33/33 each **across whole captures only**. Original earlier V37 1,017-test result and original private ZIP SHA f656c090... remain in [first V37 report](V5DCM/V5DCM37_COMBINED_DCM_OFFLINE_RESULT_20261019.md), but original archive bytes NOT mounted/independently rechecked in this recovery. The **new** separately reproducible private **23-file nonflashable ZIP SHA256 879ffcd03a7b4fe0198ef09077fbb0356f3222603a63d7c882a62e70e78d886c** passed fresh-extract complete default runner twice. Optional old B2/FIX-A/31/32 recompilation hit resource/time limit (first old B2 65/65 PASS); **NOT promoted to newly completed here**, earlier results stay historically preserved. NO new live device TX, YAML, ESPHome compile, flash, ARM, controller restart or actual DCM ACCEPTED/owner/slot/physical epoch/C2/Online. **Installed user XTR remains FIX-B2** (204sec last proven live unarmed RX/HA healthy B11D 2342/B11C 2345, executor 393/393 HARD_DENY, UART writes=0, compiled machine hash unverified); fallback RX-only V5DCM23 FIX2. V4.1 EXP386/387 local POSITIVE, EXP388 PARTIAL; V5DCM32 integrity-failed rejoin NEGATIVE; original B2 post-gap >90sec physical status still NOT RUN. **NEXT ACTION:** no more unscoped observer changes; prepare separately reviewed PRIVATE native response-provider experiment contract, pin exact currently verified B2 Core/source, prove independent current slot/owner/epoch or fail closed; exact confidential payload/CRC, bounded single response, abort+rollback before any user-initiated active test. NEVER equate mock delivery, static 33/33, 0x085F or historical RX_SHADOW_ONLY with physical authority. Full new independent report [here](V5DCM/V5DCM37_INDEPENDENT_REPRODUCTION_RESULT_20261019.md).

---

# 2026-10-19 — **CURRENT HANDOFF: V5DCM36-PINNED-CORE-OUTPUT-PROVIDER-OFFLINE-01 COMPLETE / POSITIVE (source/host ONLY).** [Detailed result](V5DCM/V5DCM36_PINNED_CORE_OUTPUT_PROVIDER_OFFLINE_RESULT_20261019.md); [prior V5DCM35](V5DCM/V5DCM35_NATIVE_APPROVAL_BOUNDARY_OFFLINE_RESULT_20261019.md). **USER ESP32: still V5DCM33-FIX-B2**, historically named main YAML, user-confirmed flash and runtime B2 marker (compiled machine image hash NOT verified). Most recent actual XTR live FIX-B2 passivity **204sec COMPLETE/POSITIVE**: independent B11D 2342 and B11C 2345 matched frames, parser no CRC/resync/drop fault, production HA telemetry live, executor 393/393 candidates HARD_DENY, UART writes/physical attempts=0, software DE low; physical wire level/owner/epoch/Online still UNKNOWN. Known-good rollback V5DCM23 FIX2 RX-only. Historical Write Beta V4.1 EXP386/387 COMPLETE/POSITIVE but fixed cold approval not universal; EXP388 RUNNING/PARTIAL. Prior original V5DCM32 live fresh rejoin COMPLETE/NEGATIVE with B11D fault before callback gap; FIX-B post-gap RX shadow positive, FIX-B2 >90sec post-qualified LIVE NOT RUN. **New controlled OFFLINE finding:** exact original private FIX-B2 source ZIP SHA256 `fdc09c5927b5a351163db95db96dc467abd43cb27e1e7fc8068782bea4a677c7` and YAML SHA `32e1b7c3ea4f7411fb94d6d769370b9ae10874403961403002250b96e4365d46` unchanged. Compiled pinned old B2 Core+adapter+platform strict C++17: **53/53 assertions PASS**, original B2 source/package pins **15/15 PASS**, **3/3 deliberately forbidden compile attempts rejected** (raw PlatformPort accept, upstream const vs B2 mutable Core, GAP15 host test access in Arduino device), **1/1 deliberately modified ZIP rejected**; V5DCM35 **192/192 +18/18 PASS**, original FIX-B2/FIX-A/V5DCM31/32 **65+70 fixture CRC+52+32+61+34+34 PASS**. **CRITICAL PROVEN SOURCE DIVERGENCE:** installed-family B2 ticketed/mutable Core decision can say STRUCTURAL owner while its own handshake NotAccepted but its adapter normal build ALWAYS sets `output_enabled_=false` even if caller true; raw platform output private except test macro. Firmware repo HEAD `xtr_core.hpp` git blob 3d172fe134f127e9d19c5ad48d863da9a87741bc uses const `fc16_decision`, HEAD adapter blob d3f1a75d551accef2576cb86c77fb2c3080c3c50 defaults output_enabled=true; public PlatformPort accept in HEAD platform blob 95014011a004d8c3165a4619ed61cdf75aac55d3. **Do not graft upstream HEAD automatically.** V5DCM36 standalone copied-Core structural inspection returns NO usable ticket and explicit `DeniedNoOutputProvider`; no actual/native security reply, UART/DE, code/YAML flash or controller action. New private NONFLASHABLE 16-file ZIP sha256 `9eefe9e7452f01267277b742d83e1a9b9b54dfb1e2b42d1bdbf93d83a48d948a`, independently archive/hash checked and rerun with only original B2 ZIP. Source package remains private; sanitized research result committed. **NEXT:** prepare V5DCM37 offline version-compatible private fail-closed output-provider design with slot/epoch/revocation negatives, not an active physical send. Native DCM/Online acceptance, C2 33/33 and local physical TX still OPEN/UNKNOWN. Do not new ARM/restart/flash/transmit or clear sticky B11D/P5. 

---

# 2026-10-19 — **CURRENT HANDOFF: V5DCM35-NATIVE-APPROVAL-BOUNDARY-OFFLINE-01 COMPLETE / POSITIVE (host-only).** V5DCM34 exact firmware↔V4.1↔FIX-B2 source comparison COMPLETE/POSITIVE offline. **ACTUAL USER ESP32:** still V5DCM33-FIX-B2 (historical YAML basename V5DCM23); last live FIX-B2-LIVE-PASSIVE-01 COMPLETE/POSITIVE 204s: B11D 2342 equal, B11C 2345 equal, parser 2417 no CRC/resync/drop faults, HA readings present, TX executor 393/393 HARD_DENY, UART Write Calls=0, software DE=0, owner/physical epoch/Online UNPROVEN, 0x0F FC23=0 in that live log. Compiled firmware hash unknown. Known-good rollback remains V5DCM23 FIX2 RX-only. **NEW OFFLINE result:** exact original unchanged FIX-B2 source ZIP sha256 fdc09c5927b5a351163db95db96dc467abd43cb27e1e7fc8068782bea4a677c7, YAML sha256 32e1b7c3ea4f7411fb94d6d769370b9ae10874403961403002250b96e4365d46. Private standalone NONFLASHABLE mock native request→synthetic delivery→first modern XTR FC16/03E8-count14 INTERNAL_ACCEPTED_SHADOW; **192/192** strict C++17 state/negative tests + **18/18** against actual FIX-B2 private portable Core, **4/4** source/output guard groups PASS, original FIX-B2 regression suites **65+70 frame-validity+52+32+61+34+34 PASS**. Four historical raw/collaborator captures independently **23,472 CRC-valid/0 CRC-bad**; original XTR Oct03 one canonical FC23 then reply-shaped record 29ms later then **03E8/count13 (legacy)** 1.862s later, **NOT** modern count14. XTR Sep25 no canonical FC23 (negative); Eco5 modern count14 only CROSS-MODEL. **PROVEN SOURCE:** exact private B2 Core can issue STRUCTURAL bootstrap `Decision.authorized=true` while own handshake is NotAccepted, so NEVER equate Core owner decision, model internal accepted or observed reply shape with electrical bus owner/current slot/TX permission. Current private B2 Core API differs from firmware-repo HEAD; no blind mixing. **No ESPHome compilation, YAML change, device flash/ARM/restart/TX; no real native approval delivery or C2/Online.** V5DCM35 ZIP private 12-file NONFLASHABLE SHA256 e672cbcb8fe630011982579687cbe33cd6652c732f0b9e13c14f7406b017c70b, not published on GH. **Next: offline version-pinned pure decision/delivery API reconciliation and private gated output provider planning; no additional power-cycle or active TX yet.** V4.1 EXP386/387 historical POSITIVE, EXP388 PARTIAL, B2 post-gap >90s live not run, old V5DCM32 rejoin negative B11D sticky retained. [V5DCM35 result](V5DCM/V5DCM35_NATIVE_APPROVAL_BOUNDARY_OFFLINE_RESULT_20261019.md) · [V5DCM35 contract](V5DCM/V5DCM35_NATIVE_APPROVAL_BOUNDARY_OFFLINE_PREPARED_20261019.md).

---

# 2026-10-19 — **V5DCM34-CM930-V41-FIXB2-NATIVE-GAP-AUDIT-01 COMPLETE / POSITIVE (OFFLINE SOURCE-ONLY); V5DCM35-NATIVE-APPROVAL-BOUNDARY-OFFLINE-01 PREPARED / NOT RUN.** Latest user-flashed running candidate remains **V5DCM33-FIX-B2**, proven passive in 204s local log: runtime marker seven times, B11D 2342 matched, B11C 2345 matched, parser 2417, no CRC/byte/resync/drop errors, 393/393 native executor candidates HARD_DENY, UART writes=0/software physical attempts=0, HA normal; compiled binary hash unverified. **NO NEW FLASH, ARM, RESTART OR TX in this source audit.** Original Connect 2.1.105 AppFS modules `cm/modbus_server15.py`, `cm/cm_client_type.py`, `cm/client.py` byte-identical (3/3) to supplied device_client.zip, CM930 native 0x0F, independent firmware handshake/FC16, controller config, app W2/W3/W4 profile and mailbox. Historical Write Beta v4.1 actual YAML blob `8e8a82689e53528a8b751a1abbd901f683b6b238` read: EXP386 controller cold recovery COMPLETE/POSITIVE; EXP387 delayed mailbox re-arm COMPLETE/POSITIVE; EXP388 2 recoveries RUNNING/PARTIAL, NOT full general emulation. New direct exact private FIX-B2 YAML/header audit + fresh log: **21/21** deterministic read-only checks PASS. RX shadow declares `kMayQualifySession=false`, `kTxAllowed=false`; it does not feed V5DCM32 or ledger reselect; V5DCM32 is separately manually armed and cannot TX, current step=0/localGen=0; V5DCM23 observed 1/33 after retained-only traffic, current 0x0F FC23 absent. **PRIMARY COLD FUNCTIONAL BREAK**: native 0x0F FC23 eligibility/response delivery/current session state bridge; existing V5 parser is good, but physical native response HARD_DENY and internal Accepted/ACK/owner/epoch/profile/Online distinct. **SECONDARY RECOVERY BREAK**: qualified historical RX shadow not current/owned epoch and intentionally not joined to manually scoped fresh/retained RX profile reselect. **LATER** C2 full profile 33 groups and semantic/service/Online. **Critical version divergence:** private user-flashed-family `xtr_core.hpp/.cpp` git blobs `63874043.../1ddb6cce...` vs firmware-repo HEAD `3d172fe.../5c345d76...`; private ticketed mutable classifier vs HEAD pure const `fc16_decision`; do not graft HEAD blindly. Keep G01–G06 previously accepted risks accepted but not newly proven, and original V5DCM18 complete reference-core seven-fixture replay remains PARTIAL. **NEXT V5DCM35 PREPARED / NOT RUN OFFLINE**: one nontransmitting decision→mock delivery→controller FC16 state join, version-pinned Core, negative tests, no private algorithms published; no new on-device actions. [Exact source audit](V5DCM/V5DCM34_CM930_V41_FIXB2_NATIVE_GAP_AUDIT_20261019.md) · [Next contract](V5DCM/V5DCM35_NATIVE_APPROVAL_BOUNDARY_OFFLINE_PREPARED_20261019.md).

---

# 2026-10-19 — **V5DCM33-FIX-B2-LIVE-PASSIVE-01 COMPLETE / POSITIVE (user-flashed source-family; 204s live RX + software TX hard deny).** User-confirmed flash of candidate ZIP source, with historical YAML filename; **actual runtime `[V5DCM33-FIX-B2]` observed seven times** in new full unfiltered 5000-line ESPHome log 00:17:40.478–00:21:04.536, 371306 bytes SHA256 `f00ceb663f17138b2efb57f7bc424ae3187991cc26b138e45aad6aefa136b9e7`; exact compiled/flashed machine-code hash remains unverified. FIX-B2 passive witness **DORMANT reason=NONE gap=0 frames=0 batches=0 B11D_OLD_FAULT=0 P5_HISTORY=0**, no ARM or new controller callback gap. Independently original B11D RAW=portable=V5 **2342/2342/2342** zero count/byte/CRC/framing faults, First Fault NONE; B11C portable=V5 **2345/2345** zero boundary/resync/drop/fault, independent public CRC checked 2316 mismatch 0. Main parser **800→2417 frames**, pages **129→392**, resync=0 drops=0. Existing HA room 21.2°C, DHW 51°C, supply 24°C and heating mode published; some other HA entities NaN (not all mapping validated). TX executor **393 candidates=393 denied**, software physical attempts=0, UART Write Calls=0, software DE=0/HARD_DENY; hardware DE level unmeasured. Native 0x0F FC16 130→393, 0x0F FC23=0, only 1/33 passive significant package, V5DCM32 step=0 scope=0 localGen=0, owner/epoch/C2/Online UNKNOWN, P5 UNQUALIFIED. **Only initial passivity proven for B2, NOT post-success >=90s terminal retention after new gap**, nor native DCM acceptance. Prior FIX-B live POST-GAP-01 COMPLETE/POSITIVE transient and old FIX-B timeout bug COMPLETE/NEGATIVE preserved; B2 offline fix COMPLETE/POSITIVE. Next prioritize offline identification of native rejoin/session integration missing proof from historical V4.1 + CM930 + existing V5, and/or **separately PREPARE** (not run) B2 post-gap qualified-hold verification only when useful and safely initiated; no further ARM/restart/TX now. [Verified live result](V5DCM/V5DCM33_FIX_B2_FIRST_LIVE_PASSIVE_RESULT_20261019.md).

---

# 2026-10-19 — **V5DCM33-FIX-B2 user reports FLASHED; live passive verification PREPARED / NOT RUN.** User explicitly confirmed the installed `waveshare-thermia_V5DCM23_REAL_LEDGER_PREPARED_NOT_FLASHED.yaml` came from the **latest FIX-B2 ZIP** `V5DCM33_FIX_B2_QUALIFIED_EVIDENCE_HOLD_OFFLINE_NOT_FLASHED.zip`. That historical YAML basename is NOT the actual code revision. Source candidate ZIP SHA256 `fdc09c5927b5a351163db95db96dc467abd43cb27e1e7fc8068782bea4a677c7`; exact compiled/flashed image hash **UNVERIFIED**. This confirmation changes deployment provenance only: **no runtime `[V5DCM33-FIX-B2]` marker, B11C/B11D RX, HA health, TX HARD_DENY, post-gap observer output, or electrical DE has yet been observed for B2**. The preceding B2 offline source/host tests remain COMPLETE / POSITIVE; the earlier FIX-B live POST-GAP-01 RX-only qualification remains COMPLETE / POSITIVE and its post-success timeout bug COMPLETE / NEGATIVE. **Next: FIX-B2-LIVE-PASSIVE-01 PREPARED / NOT RUN** pending ~60–90 s unarmed ESPHome API log on normal bus: require `[V5DCM33-FIX-B2]` boot/periodic marker, observer DORMANT, baseline B11C/B11D/parsers clean, production HA values updating, executor HARD_DENY, UART writes=0, TX physical attempts=0, software DE=0. No ARM, no controller restart or native TX; abort/recover if real RX/HA/TX regression. After reviewing user-supplied log, update all three canonical docs and only then design any new gap trial. NOTE: YAML filename contains PREPARED_NOT_FLASHED historically despite user's confirmed flashing.

---

# 2026-10-19 — **V5DCM33-FIX-B2-QUALIFIED-HOLD-OFFLINE-01 COMPLETE / POSITIVE (source/C++17 host/static ZIP only); FIX-B2-LIVE-PASSIVE-01 PREPARED / NOT RUN.** Canonical installed image remains user-reported **FIX-B**, exact firmware hash UNVERIFIED. Post-gap user XTR test FIX-B-POST-GAP-01 **COMPLETE / POSITIVE** transient independent RX: 11,888ms callback gap, qualified RX_SHADOW_ONLY 23:45:58 with 348 frames; but FIX-B-QUALIFIED-TIMEOUT-RETENTION separately **COMPLETE / NEGATIVE**, 23:46:38.439 FAULT_NO_RELEASE/WINDOW_EXPIRED due to applying ARM+90s after success, although B11D/B11C/parser and software TX stayed healthy. **B2 single source fix:** terminal/frozen QualifiedReadOnly historical milestone, freezes counters and age-at-qualification, stops independent post-qualification RAW/V5 sampling, Cancel cannot erase completion; WAIT_GAP/OBSERVING safety, 90s timeout, original B11D/P5 latches, V5DCM32 session/ledger and UART native HARD_DENY unchanged. Red regression on FIX-B reproduced; green FIX-B2 65/65 host, 70/70 actual 20261003 local captured XTR fixtures independently validated with synthetic clock/gap (61 frames consumed until qualification), old FIX-A 52+32, V5DCM31 61, V5DCM32 34 synthetic +34 genuine historical FC23 all PASS. Exact FIX-B parent SHA256 1753e92590237e9685f74d8c9d80ca64064cb73e5151d56dcdfc38cbc0769cde. Private 75-member B2 ZIP **fdc09c5927b5a351163db95db96dc467abd43cb27e1e7fc8068782bea4a677c7**; YAML SHA 32e1b7c3ea4f7411fb94d6d769370b9ae10874403961403002250b96e4365d46. YAML preserves 24 top blocks, 44 includes, 117/13/48 original HA entities, 7 original buttons and switch; only two passive log markers changed to FIX-B2. **NOT performed** full ESPHome compile, user flash, active controller ARM or reboot, live B2 run, native TX. **NO new TX**; frozen shadow is historical, not current bus integrity/owner/epoch/Online acceptance. NEXT if user flashes: FIX-B2-LIVE-PASSIVE-01 unarmed 60–90s RX/HA/HARD_DENY log; do not ARM/restart before reviewing results; abort for telemetry, CRC, UART TX/DE regressions, rollback verified V5DCM23 FIX2. [Full offline result](V5DCM/V5DCM33_FIX_B2_QUALIFIED_HOLD_OFFLINE_RESULT_20261019.md).

---

# 2026-10-18 — **V5DCM33-FIX-B-POST-GAP-01 COMPLETE / POSITIVE (scoped RX-only cohort), with independently PROVEN post-success observer lifecycle bug.** User continuation `Pasted text(20261018-214726).txt` 4999 lines/402566 bytes SHA256 8903b3707a91fdb63a56b29faa96badf8798b0fb96449670b21877a065a03753, 23:44:01–23:47:15. Same prior ARM accepted **23:45:04.356**; R6-P24 gap **11888ms 23:45:20.888**, CRC return 0x1E and cold-pattern event with epoch still UNKNOWN. FIX-B independent RX witness progressed CLEAN_WINDOW then **RX_SHADOW_ONLY 23:45:58.453 (348 frames/168 batches gap=1, NONE)**, 23:46:01 source marker ageMs=40376 frames=374, stayed qualified through **23:46:31.266** 638/291. This meets original >=30s/>=50 CRC+V5-parity frame within 90s contract; original B11D still fault/hold 0, first NONE, B11D 17574/17574 parity 0 diff at 23:46:56, B11C 17594/17594 zero fault, V5 parser resync/drops=0, HA live. Native FC23 **27 requests**, NO native acceptance: V5DCM32 scope=0 step=0 localGen=0, R6-P5 UNQUALIFIED, unknown owner/epoch/C2/Online. Executor 2897/2897 HARD_DENY, 0 software physical attempts, UART writes=0, software DE=0; physical pin unmeasured. **IMPORTANT CRITICAL BUG**: despite clean TX/RX, at **23:46:38.439** witness becomes `FAULT_NO_RELEASE reason=WINDOW_EXPIRED` (668/303) due to `check()` checking ARM+90s even AFTER Phase::QualifiedReadOnly; original host suite missed post-qualified expiry. This does NOT negate earlier positive *transient* RX proof, but **durable success evidence is not retained**. Separate FIX-B-QUALIFIED-TIMEOUT-RETENTION **COMPLETE / NEGATIVE**; next FIX-B2 offline source-only immutable-qualified-evidence policy **PREPARED / NOT RUN**, test retention after 90s without TX/no legacy fault clear; do not flash, re-ARM or restart for current issue. Physical controller switch times/alarms not separately user confirmed; do not assert electrical epoch. [Full final report](V5DCM/V5DCM33_FIX_B_POST_GAP_01_COMPLETE_RESULT_20261018.md).

---

# 2026-10-18 — **V5DCM33-FIX-B-POST-GAP-01 RUNNING / PARTIAL (LIVE)**. New user API log 5000 lines, SHA256 5eb5bd6f1c9c82ffc9fc0d721a3defdabe1633e6d638492fbd4677b0f81862ac, 23:42:14–23:45:36. FIX-B HA ARM **ACCEPTED 23:45:04.356**, WAIT_GAP, fresh R6-P24 callback gap **11888ms 23:45:20.888** and FIRST_CRC_RETURN slave 0x1E, fresh 0x02 A80E=0000 A80F=0005 coldPattern event; controller power switch edge/user exact timing still UNCONFIRMED, epoch UNKNOWN. FIX-B CLEAN_WINDOW **23:45:28** 64 frames/34 batches, **23:45:31** 98 frames/47 batches ageMs=10376, gap=1, reason NONE, B11D_OLD_FAULT=0 P5_HISTORY=0, software TX HARD_DENY. Original B11D 16764/16764 RAW/portable/V5 zero parity/CRC mismatch fault=hold=0 through 23:45:26; B11C 16785/16785 no fault; main parser resync/drops 0, HA continues. Native 0x0F **four FC23 requests** after return but session still UNQUALIFIED/no owner; V5DCM32 step=0 localGen=0, old portable profile 1/33 context revoked, reset 0/0; no native rejoin claim. Executor 2736/2736 candidates denied, physical attempts=0 software, DE_LOW, UART writes=0. Log ENDS **23:45:36**, BEFORE 30sec post-gap minimum around 23:45:51; NO RX_SHADOW_ONLY or failure yet. Need ONLY continuation ~23:45:45–23:46:40 (or later FIX-B status) plus confirmation physical restart/alarm; **NO re-ARM/restart/flash**. Prior V5DCM32 failed rejoin COMPLETE/NEGATIVE remains. [Partial report](V5DCM/V5DCM33_FIX_B_POST_GAP_01_PARTIAL_RESULT_20261018.md).

---

# 2026-10-18 — V5DCM33-FIX-B-POST-GAP-01 **PREPARED / NOT RUN** (one live passive controller-gap witness; NOT a native TX/session experiment). After successful user-flashed FIX-B PASSIVE COMPLETE/POSITIVE baseline, independently audited actual source: only HA Configuration `V5DCM33-FIX-B Arm Passive Gap Witness (NO TX)` followed by one manually user-initiated manufacturer-safe controller restart when compressor is NOT running; last log 23:23:49 compressor 25Hz, therefore **do not arbitrarily power-cycle now**. Button must yield PASSIVE_ARM_ACCEPTED / WAIT_GAP; 90s hard scope STARTS at ARM, new R6-P24 >=5000ms callback gap detected in existing UART callback, >=30s and >=50 verified RAW/CRC/V5 frames after gap to RX_SHADOW_ONLY. No ESP reboot, old V5DCM32 Arm, TX, registration writes or wiring change. Source exact 90s,30s,50 frames, one-shot, cancellation/failure requires separate experiment after ESP reboot. Historical B11D/P5 sticky unchanged; new RX shadow does NOT grant V5DCM32 acceptance/Online owner/C2/TX. Abort on real heat-pump alarm or production telemetry issue, DE/TX write or parser/CRC runaway; preserve continuous 10–20s pre-ARM through >=90s post-ARM API log and ARM/restart timings. Original B11D fault may recur independently; record both. Full preparation [POST-GAP-01](V5DCM/V5DCM33_FIX_B_POST_GAP_01_PREPARED_20261018.md); no device execution/ARM user confirmation yet.

---

# 2026-10-18 — V5DCM33-FIX-B-LIVE-PASSIVE-01 **COMPLETE / POSITIVE (user-flashed RX-only passive baseline, NO ARM/NO CONTROLLER RESTART)**. 4999-line user ESPHome API log SHA256 0f86352fd9c6cf2c70c7b3d1ef004c3d2280ef73ca42a3b188993bd566e4a87f, 23:20:28.816–23:23:50.942. Actual [V5DCM33-FIX-B] runtime marker and new HA witness text prove FIX-B code family executing; exact flashed YAML/firmware hash remains unverified. FIX-B phase DORMANT, gap=0 frames=0 throughout (correct while unarmed). Latest independent B11D console 5617/5617 original RAW/portable/V5 parity, fault=0 hold=0 count/byte differences=0; B11C 5637/5637, zero boundary/CRC/drops; V5 main parser 4124→5829 frames and 672→950 page observations, resync=0 drops=0; HA heating temperatures and room sensor still update. P5 history=0, R6 P5 UNQUALIFIED / NO_TX (ESP_BOOT_UNQUALIFIED), native V5DCM32 scope=0 step=0 localGen=0, portable 1/33, native 0x0F FC23=0, P24 NO_CALLBACK_GAP_SEEN; NEVER confuse HA 0x02/0x0A FC23 with native 0x0F. Software TX HARD_DENY 944/944 candidates denied physical_attempts=0, UART WriteCalls=0, DE=0 software; physical DE voltage not measured. This fulfills PASSIVE baseline only; separate V5DCM33-FIX-B-POST-GAP-01 PREPARED / NOT RUN, needs reviewed one-shot 90s ARM / >5s gap / 30s+50 clean RX test, no session latch reset, no TX. Prior failed V5DCM32 power cycle remains COMPLETE / NEGATIVE; no automatic new restart. [Detailed live log report](V5DCM/V5DCM33_FIX_B_FIRST_LIVE_PASSIVE_RESULT_20261018.md).

---

# 2026-10-18 — **V5DCM33-FIX-B COMPLETE / POSITIVE OFFLINE SOURCE/HOST/STATIC ONLY; LIVE PREPARED / NOT RUN**. From FIX-A source ZIP ec26b859..., prepared private complete FIX-B ZIP SHA256 **1753e92590237e9685f74d8c9d80ca64064cb73e5151d56dcdfc38cbc0769cde**, YAML SHA256 8610cabc3198ccb7061e9b8e905efeb6ea31b342d6f32e63b19a283ebb817477. One additive RX-only manually armed post-gap independent RAW witness: existing one UART callback, fresh R6-P24 >=5s callback gap, bounded 90s arm, minimum 30s+50 independently CRC-valid exact V5-parity frames; finite error/timeout guards; no second UART, no TX. New C++17 54/54 synthetic host assertions and 70/70 local historical XTR raw captured-frame replay (synthetic clock/gap), old FIX-A 52+32, V5DCM31 61, V5DCM32 34+34 PASS; YAML 44/44 includes, original 117/13/47 HA entities plus 5 buttons/1 switch intact, added 1 diagnostic text+2 Configuration buttons. **Original B11D sticky fault, R6 P5 historical latch, R6 P24, V5DCM32 rejoin gate and HARD_DENY all untouched.** RX_SHADOW_ONLY is observational; does NOT resolve prior V5DCM32 22:02 BadIntegrity rejoin, attest controller power/owner/epoch/C2/Online, or authorize TX. No full ESPHome compile, flash, device test, new ARM/controller restart. Actual installed source still user-attested FIX-A; image hash not proven. NEXT FIX-B-LIVE-PASSIVE-01 PREPARED/NOT RUN: unarmed RX regression log only if user separately flashes; no automatic ARM or controller reboot. [Research report](V5DCM/V5DCM33_FIX_B_POST_GAP_RAW_WITNESS_OFFLINE_20261018.md).

---

# 2026-10-18 — V5DCM33-FIX-A first USER-FLASHED **LIVE PASSIVE OBSERVATION RUNNING / PARTIAL** (no ARM, no controller restart, no live-rejoin execution). User supplied 2,050-line ESPHome API log SHA256 96f4f25dc5ee551f21a7d3c5173eece70ec62f85bef585f44d4d65207a9e46ed. B11D 529/529 original RAW/portable/V5 frames parity, countDiff=0 byteDiff=0 fault=0 hold=0, First Fault NONE; B11C 548/548, resync=0 drops=0 CRC integrity healthy; live readings maintained; TX executor HARD_DENY 126/126 candidates, physicalAttempts=0, DE=0 software. Parser resync **8 already at first recorded snapshot and stays 8**, Bridge04-1 separately had one historical fault then passive recovered (resync+8), R6 P5_HISTORY=1 and RX Integrity Faults=1 persist **despite current clean B11D**: keep these separate. V5DCM32 step=0 scope=0 localGen=0, portable 1/33, 0 native 0x0F FC23, controller R6-P24 no callback gap. User's flash report accepted as attestation; exact machine image hash UNVERIFIED (CLI config-cache labels GAP51D; no V5DCM33 image marker). DOES NOT exercise short-fragment fix or prove prior 22:02 recovery. Offline FIX-A source result remains COMPLETE/POSITIVE; prior V5DCM32 failed reboot remains COMPLETE/NEGATIVE. NEXT V5DCM33-FIX-B OFFLINE PREPARED / NOT RUN; no new ARM/controller reboot recommended. [Live passive report](V5DCM/V5DCM33_FIX_A_FIRST_LIVE_PASSIVE_LOG_20261018.md).

---

# 2026-10-18 — V5DCM33-FIX-A **COMPLETE / POSITIVE OFFLINE SOURCE/HOST/STATIC ONLY**, **NOT COMPILED, NOT FLASHED, NOT RUN LIVE**. Private full V5DCM32-derived ZIP SHA256 ec26b85929a760be04b03031b02d10a432fc1765c9e699428bec51aa23cf7bd0, YAML e02073a54ea22963de1671fba99fa6c426282b02364a5405ef3a049dbe4797ae. Single B11D RAW 1–4-byte residual behavior modified: delay <=250ms ONLY with fresh existing V5 parser pending evidence, original CRC/portable/V5 parity unchanged, sticky holds remain fail-closed. Strict C++17 tests 52+32 NEW, 34+34 V5DCM32, 61 V5DCM31 PASS; YAML syntax/top-level/entity parity PASS, 43 includes, original 117+13+47 entities and 5 buttons+1 switch intact, no TX/DE callsite added. IMPORTANT: no recovery of old integrity latch; user-confirmed V5DCM32 22:02 live power-cycle -> B11D BadIntegrity remains COMPLETE / NEGATIVE, and a 13s gap would time out even under FIX-A. Actual installed V5DCM32 unchanged. NEXT V5DCM33-FIX-B post-gap integrity qualification PREPARED / NOT RUN OFFLINE FIRST; extract first-fault metadata, never silently clear sticky fault. Do not re-power-cycle to test yet. [FIX-A report](V5DCM/V5DCM33_FIX_A_SHORT_RESIDUAL_SOURCE_RESULT_20261018.md).

---

# 2026-10-18 — V5DCM33 B11D short-residual audit COMPLETE / POSITIVE **OFFLINE SOURCE ONLY**. Exact uploaded V5DCM32 YAML has immediate sticky `RAW_INCOMPLETE_AT_IDLE` fault on <5 byte RAW residual after 25ms quiet; existing 250ms bounded defer only applies later to >=5-byte candidate fragments with V5 pending. This asymmetry is a plausible source-level contributor to 22:02:30 BadIntegrity, NOT a proven cause of actual bytes. User-confirmed controller power cycle and V5DCM32 COMPLETE / NEGATIVE fresh rejoin stay unchanged. No live changes, build, flash, TX or fault-clear. NEXT V5DCM33-FIX-A PREPARED / NOT RUN: minimal fail-closed host-tested short fragment deferral first, followed by separately justified post-gap integrity qualification; no new restart yet. [Report](V5DCM/V5DCM33_B11D_SHORT_RESIDUAL_OFFLINE_20261018.md).

---

# 2026-10-18 USER FOLLOW-UP — Physical manual Thermia controller power cycle **CONFIRMED BY USER** for the V5DCM32 armed live test. Preserve original measured chronology: 22:02:23 arm, 22:02:30 B11D first RAW_INCOMPLETE_AT_IDLE, 22:02:43 callback gap 12923ms, 22:02:45 first logged FC23, then BadIntegrity denied rejoin, localGen=0; ledger revoked to 0/0. User confirmation establishes manual intervention provenance, but exact switching instants and independent physical epoch/owner remain unknown. NEXT V5DCM33 offline examine whether interrupted serial frame causes sticky observer and how to require clean post-gap RX before qualified rejoin. Do not restart again before offline review.

---

# V5DCM32 live armed attempt COMPLETE / NEGATIVE: 22:02:23 arm, 22:02:30 B11D RAW_INCOMPLETE_AT_IDLE fault, 22:02:43 R6 P24 12923ms gap, 22:02:45 onward 14 observed FC23, 22:02:49 V5DCM32 step=2 Denied verdict=5 BadIntegrity, localGen=0, V5DCM23 correctly revoked to 0/0. Software TX HARD_DENY and DE=0. Physical restart not directly proven. Original log SHA256 94c3121d56ff70c2bef30e621f82eac97fb80f7b1d7ab2d4e006f1fef6842c11. Next V5DCM33 integrity recovery OFFLINE PREPARED / NOT RUN; no further live re-arm until reviewed. Full provenance: V5DCM/V5DCM32_LIVE_REJOIN_INTEGRITY_DENIAL_20261018.md.

---

# 2026-10-18 — V5DCM32-LIVE-OBS-01 **RUNNING / PARTIAL**. **USER CONFIRMED FLASHED V5DCM32** and provided 1,514-line user ESPHome API log SHA256 2d4bf22ca79bd9047de749efb07241886a5064a86ad1ee5082e7e9e7b99c786a spanning 21:36:53.998–21:37:57.072 (~63s). Runtime confirms [V5DCM32] at 21:37:18/48: `step=0 scope=0 localGen=0 verdict=0 epoch=UNKNOWN owner=UNKNOWN C2=UNPROVEN TX=HARD_DENY`, **NO ARM AND NO FRESH REJOIN TEST YET**. Actual V5DCM22 RX33 1/33 W3 bit0, exact30→58, wrongGeom=0, FC23=0; V5DCM23 portable 1/33 stable. Healthy RX [B11C] 522/522 diff=0, [B11D] 533/533 diff=0, parser resync=0 drops=0, current HA temperatures/heating update, software DE=0 and native hard deny 88/88 candidates denied physical_attempts=0. Legacy R6 D=4 still present, first fault trigger unobserved. ESPHome CLI validated cache references GAP51D filename, NOT verified exact flashed source hash; runtime V5DCM32 logger is present. **Installed V5DCM32 now current; FIX2 prior baseline is fallback**, not silently still deployed. Full fresh arm→manual controller intervention→native FC23→ledger reselect NOT RUN. Next user-initiated test only if intended, with 30s/8192 event scope under Configuration, abort on parser/HA/TX regression; G01–G06 accepted research risks not reopened. [LIVE partial report](V5DCM/V5DCM32_LIVE_OBS_PARTIAL_20261018.md). Offline source V5DCM32 remains COMPLETE / POSITIVE.

---

# 2026-10-18 — V5DCM32-RX-REJOIN-INTEGRATION-01 **COMPLETE / POSITIVE OFFLINE SOURCE+HOST+STATIC ONLY**. Made source-only FULL private V5DCM23 FIX2 candidate with V5DCM31 bounded accepted-risk fresh-scope policy physically joined to ORIGINAL one-consumer V5 CRC callback after existing R6-P24 SAME-frame context and friend-only native portable package ledger `reselect_rx_only_after_accepted_risk` path. Prior FC23 boundary REQUIRED; standalone FC23 never reselects; Configuration fresh arm and revoke, 30s/8192 frame upper budgets, require post-arm callback gap+return, cold status and current canonical native FC23, clean RX and unchanged accepted installation scope; unknown physical epoch stays 0 and no owner/C2/Online/ACK/TX. Retained/recovery paths NOT wired. EXACT original portable C++ source strict host 34/34 twice PASS (synthetic and unchanged historical local CRC-valid FC23), V5DCM31 61/61 PASS. Offline YAML syntax PASS, 42/42 includes, all 55 original ZIP entries preserved with ONLY original ledger header+YAML modified; all 117/13/47 sensor entities + original 3 buttons unchanged, 2 Config buttons added. 45 YAML lines added, zero removed, no new UART, DE or TX callsite. PRIVATE ZIP `V5DCM32_RX_REJOIN_INTEGRATION_OFFLINE_NOT_FLASHED.zip` SHA256 `346966b47cad7a184936a905e40e46fa19bb6fbe8e7140eeee505cbbc1dc9374`, modified YAML SHA256 d1f904d12ef33a47811693a9ff8acfd49564f510874fa08196c2b9bd0188f968; **ESPHome compile NOT RUN, NOT FLASHED**. Live user V5DCM23 FIX2 still RUNNING/PARTIAL RX-only 1/33, TX HARD_DENY. Original V5DCM22 witness since-boundary remains separately revoked; reset only portable 33-group ledger, no claim complete C2. Next V5DCM32-LIVE-OBS-01 PREPARED/NOT RUN and requires source review + user-initiated RX-only live action/results. G01–G06 accepted research risks remain accepted, not re-opened. [Full report](V5DCM/V5DCM32_RX_REJOIN_SOURCE_INTEGRATION_OFFLINE_20261018.md).

---

# 2026-10-18 — V5DCM31-MANUAL-SESSION-SCOPE-01 COMPLETE / POSITIVE **OFFLINE C++ SOURCE/HOST ONLY**. User-accepted G01–G06 residual risks are NOT reopened. Actual Write Beta v4.1 guarded cold/retained/recovery source reviewed; added one distinct nontransmitting experiment-scoped `v5dcm31_accepted_risk_session_policy.hpp` admitting only `RxCandidateUnderAcceptedRisk` metadata after current boot, user-initiated short-lived bounded scope and required fresh/retained/recovery context. It DOES NOT forge V5DCM29 `IndependentProof`, controller epoch, owner, native acceptance, ACK, TX or Online. Strict g++17 61/61 checks PASS and unchanged GAP24A/B join test PASS, including duplicate-frame negative, CRC, foreign epoch, expired scope and peer collision; private ZIP SHA256 cc576fed268426107536223f790349e0dd3d723918c913f136f64c411fde47e7 NONFLASHABLE. No production callback, ledger, UART, YAML or HA changes. Current **V5DCM23 FIX2 RX-only RUNNING / PARTIAL 1/33**, TX HARD_DENY unchanged, exact flash hash/physical C2 still OPEN. **Next V5DCM32-RX-REJOIN-INTEGRATION-01 PREPARED / NOT RUN**: one source-only strict local-generation RX reselect seam into exact FIX2, preserve all 180 entities; no TX. Older V5DCM26-LIVE-OBS-01 remains PREPARED / NOT RUN. [Evidence](V5DCM/V5DCM31_ACCEPTED_RISK_SESSION_POLICY_OFFLINE_20261018.md).

---

# 2026-10-18 — USER RECONFIRMED G01–G06 AS ACCEPTED RESEARCH RISKS (authorization-policy correction, NOT experiment). Reconfirm existing NATIVE_AUTONOMOUS_TX_AUTHORIZATION_20261018.md: do NOT reopen or demand completion of G01, G02, G03, G04, G05, G06 as new prerequisites for continued native DCM emulation/rejoin development or a properly scoped user-initiated live test. Historical G01-09 video-intervention positive, conditional installed-topology G02 accepted, other electrical proof OPEN/PARTIAL remain truthful technical evidence labels. V5DCM30 COMPLETE/INCONCLUSIVE refers solely to missing independent CURRENT controller-epoch witness and DOES NOT mean a global TX-research NO-GO. NEXT: prioritize V5DCM31 implementation-facing bounded fresh/retained/recovery policy from proven V4.1 rather than another G01–G06 proof loop; distinguish **verified independent proof** from **user-accepted experimental risk policy** without fabricating epoch/owner evidence. Specific known response-slot policy/targets, CRC, fail-closed conditions, timing, abort/recovery still required for an armed user-initiated live test. Current device FIX2 RUNNING/PARTIAL RX-only, HARD_DENY, no changes/physical TX.

---

# 2026-10-18 — V5DCM30-INDEPENDENT-WITNESS-AUDIT-01 COMPLETE / INCONCLUSIVE for current physical controller-epoch/continuity source. OFFLINE audit only: FOUND existing G01-09 2026-10-14 VIDEO/INTERVENTION_ANCHORED user physical switch/display restart (11,944ms bus gap, first CRC return, cold status and 24 FC23 requests); this is historically POSITIVE, but no main-controller power-rail measurement and not a current FIX2 witness. FOUND 2026-10-14 user-approved G02 COMPLETE / POSITIVE (CONDITIONAL) single known DCM port/no installed DCM + bounded historical controller-owned work; preserve accepted scope, no automatic electrical exclusivity/new-epoch response lease. Old V4.1 EXP386/387 locally POSITIVE, EXP388 PARTIAL, not a present V5 owner. Available 20261003 raw 2687 frames and 2 native FC23, 20260925 raw 892 and zero FC23; video/G01 original raw bytes unavailable for fresh replay. Current V5DCM23 FIX2 RUNNING / PARTIAL only ~2m25 1/33, no observed FC23, no independent physical restart, exact flash SHA unknown; no production V5DCM29 proof issuer. Therefore no automatic native owner/slot/C2/TX claim. G03/G04/G05/G06 remain technically open under accepted research risk. No hardware action. Next V5DCM31-MANUAL-SESSION-SCOPE-01 PREPARED / NOT RUN, source-only distinction between bounded user-intervention and autonomous physical proof; not new live TX. [Report](V5DCM/V5DCM30_INDEPENDENT_WITNESS_AUDIT_20261018.md).

---

# 2026-10-18 — V5DCM29-SESSION-PROVENANCE-CONTRACT-01 COMPLETE / POSITIVE OFFLINE SOURCE/HOST ONLY. One new private RX-only contract separates physical controller epoch from monotonic local rejoin generation (V5DCM28 had conflated them). Fresh requires independently evidenced restart/new physical epoch; retained may keep SAME physical epoch with a NEW local generation if physical continuity independently attested; recovery needs verified continuity OR restart, never both assumed. Three strict C++17 host tests PASS including real original 20261003 native FC23 into exact V5DCM28 ledger: 1/33→revoked, then historic/passive evidence cannot reselect; no actual independent physical proof issuer exists, so no production rejoin/TX/Online authority. Private ZIP SHA256 2b044617411de452870ce70210c02fa0b3fd71e31815454248212881f23c2320 is NOT FLASHABLE. Live installed V5DCM23 FIX2 remains RUNNING / PARTIAL RX-only 1/33, TX HARD_DENY, R6 D=4 cause and exact flashed hash UNKNOWN; 262 extended RX33 vs 180 private HA inventory unresolved. V5DCM30-INDEPENDENT-WITNESS-AUDIT-01 PREPARED / NOT RUN (offline), V5DCM26-LIVE-OBS-01 PREPARED / NOT RUN. [Full report](V5DCM/V5DCM29_SESSION_PROVENANCE_CONTRACT_OFFLINE_20261018.md).

---

# 2026-10-18 — V5DCM28-EPOCH-GUARD-01 COMPLETE / POSITIVE (OFFLINE ONLY): current V5DCM23 FIX2 remains live RX-only RUNNING / PARTIAL, 1/33 observed with no FC23 in its short log. Exact private V5DCM27 source replay exposed stale/reused epoch-label acceptance after revocation; one-line guard now requires strictly newer external label. Two g++17 host regressions PASS, including a real historical native FC23 and fresh/retained/recovery source observer checks. No source today independently proves controller owner, physical epoch, or response slot. The V5DCM28 ZIP is nonflashable; no ESPHome compile, flash, TX or HA changes. Previous V5DCM27 inert rejoin prototype source-only tests also passed. V5DCM29 independently sourced epoch/owner contract PREPARED / NOT RUN. Earlier V5DCM26 15–20 minute unchanged-FIX2 passive run also PREPARED / NOT RUN. [V5DCM28 report](V5DCM/V5DCM28_EPOCH_GUARD_AND_LIFECYCLE_PROVENANCE_OFFLINE_20261018.md).

---

# 2026-10-18 — V5DCM26-PASSIVE-CENSUS-01 COMPLETE / POSITIVE (OFFLINE only). PRIVATE FIX2 ZIP SHA256 561169c3... verified in mounted files; identity-level comparison to public RX33 STATCLASS PREPARED/not-flashed source: 262 public named (187/60/15), 180 FIX2 (117/13/47/3 buttons), 44 same exact name, 218 public-only and 136 FIX2-only; all shared explicit IDs equal, registry unique_id parity and missing producers NOT VERIFIED. DO NOT blindly merge or delete HA statistics. Standalone no-TX Python strict CRC/FC16 33-profile shape/window census tested with mutation fixture, 7 existing local/cross-model files: XTR 20260925_090550 24/33 distinct with 2 historic short-shape mismatches; XTR 20261003 31/33 with 2 FC23 boundaries; Eco5 reference 20260926 and 0928 descriptively 33/33 but NOT continuous session C2 or genuine DCM. This is geometry inventory only; old R6 D=4 and live current FIX2 1/33 unresolved, TX HARD_DENY unchanged. **V5DCM26-LIVE-OBS-01 PREPARED / NOT RUN:** same already flashed RX-only FIX2, 15–20 min sustained passive logs (V5DCM19/22/23 B11C/B11D S8 R6-P30D) only; no new YAML, reboot, TX, other change. [Census report](Research/V5DCM/V5DCM26_PASSIVE_CENSUS_OFFLINE_20261018.md), [HA parity](Research/V5DCM/V5DCM26_HA_IDENTITY_PARITY_AUDIT_20261018.md).

---

# 2026-10-18 — V5DCM25-REQUEST-CYCLE-01 COMPLETE / POSITIVE (OFFLINE ONLY). ORIGINAL Connect 2.1.105 AppFS cm/modbus_server15.py, cm_client_type.py and client.py verified byte-identical to device_client.zip. Native CM930 source uses slave=0x0F and separate internal handshake, profile request bitmaps (three groups), info/onboarding/operation, and 33 significant-package readiness. Internal HandshakeState.ACCEPTED can follow first qualifying FC16: old R6 Stage-D 32/32 is NOT a vendor firmware acceptance prerequisite; neither proves controller owner/C2/Online. Offline CRC-checked historic local 20260925_090550: first 68.23s 0 upper/0 lower settings FC16, then after request transition 15 upper +16 lower distinct FC16 within 33.69s (39 FC16 ACKs); earlier physical 03E8/13 vs modern local 03E8/14! Cross-model Eco5 20260926/28 repeated expanded request -> distinct FC16 bursts -> request decrease, not local XTR or genuine DCM proof. STRICT distinction between 33 profile-significant, broad requested, and 32 ordered R6. Current live FIX2 remains RUNNING / PARTIAL 1/33, D=4 unresolved, software TX HARD_DENY; no fresh request-transition evidence. V5DCM26 passive-only request-count/receipt observer PREPARED / NOT RUN, subject to HA entity identity reconciliation (180 private vs 262 full) BEFORE new YAML; no flash or TX. No private mailbox tooling published. [Full report](Research/V5DCM/V5DCM25_REQUEST_CYCLE_SOURCE_CAPTURE_AUDIT_20261018.md).

---

# 2026-10-18 — V5DCM24-SOURCE-GATE-01 COMPLETE / POSITIVE (OFFLINE ONLY). Verified private FIX2 Stage-D source: R6 D=4 is a sticky, fail-closed 32-page/ACK transport ledger, separate from portable V5DCM23 33 significant-groups RX accounting. Source-extracted strict C++17 host replay of historical cross-model 20261003 2687 CRC-valid frames reached 32/32 state3; two synthetics correctly held for repeat page and ACK timeout. Original Connect 2.1.105 device_client confirms request-bit + package-receipt readiness lifecycle: 33 significant groups are not guaranteed unsolicited broadcasts. Private FIX2 YAML 180 named HA entities vs full RX33 STATCLASS baseline 262, state_class 31 vs74; DO NOT substitute without identity parity. Live FIX2 first-fault D=4 trigger still UNKNOWN; do not conflate source proof with live diagnosis, C2, owner, epoch or TX. No device change, no TX, live V5DCM23 FIX2 stays RUNNING / PARTIAL 1/33. Next: source-only reconcile request lifecycle and HA identity loss; if essential ask user ONLY first R6-P30D HANDOFF_ABORT line. [Offline report](Research/V5DCM/V5DCM24_SOURCE_GATE_REQUEST_AUDIT_20261018.md).

---

# 2026-10-18 — V5DCM23 FIX2 RUNNING / PARTIAL: user flashed corrected private build, first live log 20261018-162608 shows five [V5DCM23] actual portable package ledger snapshots profile=1 received=1/33, matching five [V5DCM22] RX33 snapshots W3 bit0 03E8/14 strict, 28→140 frame occurrences, no geom/FC23/integrity in RX33. B11C V5=portable 1046/1046 no diff/drop/resync; B11D 1053/1053 no diff/fault; S8 DE=0 and native TX HARD_DENY candidates=208 denied=208 physical_attempts=0 (software counters only). HA heating/DHW sensors updating, uptime 34→124s no restart in capture. CAUTION older R6-P30EC independent gate still D=4 STAGE_D_LEDGER_FAULT INTEGRITY_HOLD_NO_TX while RX parser clean; preserve as separate provenance unknown, don't assume native C2. Running actual ZIP hash/partition not authenticated. No further live TX. Next offline investigate latched gate-D and HA inventory; report Research/V5DCM/V5DCM23_FIX2_LIVE_RESULT_PARTIAL_20261018.md.

---

# 2026-10-18 — V5DCM23-FIX1 PREPARED / NOT RUN full ESPHome/on-device. User's real ESPHome 2026.9.0 ESP-IDF 5.5.5 build failed at v5dcm23_v5dcm19_real_ledger.hpp missing xtr_v5dcm21_packages.hpp in generated src. Root cause: both packages and transitive readiness headers present in private ZIP but absent YAML esphome.includes. New private FIX1 ZIP sha256 ee6814b29a3412069ec33c7015c9a3ad2f5913e236b8cb4e529d59f83bd3d5e0 inserts exactly two YAML include entries (readiness and packages), all 38 original includes/HA/bus/TX code unchanged. Offline strict C++ ledger test and real historical 2687-frame replay PASS; full ESPHome compile/flashing still UNVERIFIED. OTA password warning is unrelated and untouched. User can retry build, do NOT assume full build PASS. Report: Research/V5DCM/V5DCM23_FIX1_ESPHome_INCLUDE_REPAIR_20261018.md.

---

# 2026-10-18 — V5DCM23-EMBED-OFFLINE-01 COMPLETE / POSITIVE: new **PRIVATE not-flashed** V5DCM19-derived candidate using adapted real portable PassivePackageLedger on existing completed V5 callback, host g++17 tests PASS and original 20261003 2687-frame byte replay PASS (162 native FC16, 2 FC23, no stale qualification). Single controlled four-insertion YAML diff reconstructs previous private candidate byte-exactly; 117 numeric+13 binary+47 text+3 buttons unchanged. New private ZIP SHA256 127d781089134569299f4e01faa8c380d2176dcd0794e06a7fd971240e6c179d, NOT published. **ESPHome compilation, flash, physical TX and live integration NOT RUN**. Original live V5DCM22 RX33 experiment remains RUNNING / PARTIAL (1/33; clean parity), prior OTA app1 rollback unresolved. Warning: private branch has materially fewer HA entities than v31/RX33 full-monitoring; DO NOT deploy over functioning production until exact source/HA parity and OTA provenance verified. [Status report](V5DCM/V5DCM23_OFFLINE_INTEGRATION_STATUS_20261018.md).

---

# 2026-10-18 — V5DCM22-V5BASE-RX33-01 RUNNING / PARTIAL based on first uploaded live XTR log (~17:14:29–17:17:26; uptime 33–183s). Six [V5DCM22] RX33 checkpoints prove native 03E8/14 single significant page observed (W2 0000/W3 0001/W4 0000, 1/33 since boot, exact occurrences 28→168), zero wrong geometry/FC23/observer-integrity faults. B11C last 1568/1568 and B11D 1564/1564, no diff/drop/resync; existing HA measurements present and HARD_DENY software physical_attempts=0. OTA WARNING: rollback from app1 after earlier unconfirmed boot, current active binary exact hash/source/partition unknown despite V5DCM22 log; do not assume cached GAP51D filename represents running binary. No native C2/Online. Offline V5DCM23 actual portable ledger V5 callback adapter and 11-case guard committed to Thermia_Connect_Firmware (2d40e6b, fd5de2e, CI 755cfd2), exact-head [Actions 39140420159](https://github.com/ryckema/Thermia_Connect_Firmware/actions/runs/39140420159) SUCCESS. Status V5DCM23-OFFLINE COMPLETE / POSITIVE; private ESPHome embedding PREPARED / NOT RUN. Live device still uses interim witness; no new flash/TX. Next: source-provenance and HA parity, then private embedding and compile. [Report](V5DCM/V5DCM23_V5_CALLBACK_REAL_LEDGER_OFFLINE_20261018.md).

---

# 2026-10-18 — V5DCM22-V5BASE-OFFLINE-01 COMPLETE / POSITIVE (host C++17 and original historical byte-replay); V5DCM22-V5BASE-RX33-01 PREPARED / NOT RUN (device); overall native DCM RUNNING / PARTIAL. A private V5DCM19 lineage candidate ZIP was created from user exact 66-file source ZIP (SHA256 ca1dd27231ff12d587c8931fda81d7f61fab9da84603fe11eee78c41b5ec75b5); candidate ZIP SHA256 ba1bfb9a922f29f3c3fa1af5bf54a66484c9d1a36a6247befac8acb07add36ab. Four controlled insertions: one metadata-only RX33 header include, boot reset, one validated existing V5 frame callback and a 30s diagnostic in the existing interval list. Static strict YAML passes and old YAML is byte-identical when insertions removed; 180 old named HA entities and all 16 old periodic entries preserved; original UART GPIO17 TX pin, DE GPIO21 ALWAYS_OFF and software HARD_DENY unchanged. Strict host C++17 PASS; historical capture byte-replay via actual new C++ witness: 2687 CRC-valid,162 FC16,2 FC23,31/33 exact XTR geometries,126 matching occurrences,2 wrong counts,zero C2/Online/TX authority. The source ZIP is not byte-proven as flashed; candidate is NOT production replacement of wider v31/RX33 HA and HAS NOT been ESPHome compiled/flashed/live-tested. Actual portable PassivePackageLedger still not bound into the private V5 callback; current observer is an interim RX-only shape witness. Next: integrate actual portable ledger, reconcile full HA entity inventory and stats metadata, then compile offline. Detail: Research/V5DCM/V5DCM22_V5DCM19_PRIVATE_RX33_OFFLINE_20261018.md.

---

# 2026-10-18 — **Baseline decision: V5DCM19 FIX1 is preferred for native DCM development, but ZIP is NOT byte-proven flashed; preserve current v31/RX33 HA baseline.** User supplied `V5DCM19_RX_ONLY_FIX1_20261018(2).zip` SHA256 `ca1dd27231ff12d587c8931fda81d7f61fab9da84603fe11eee78c41b5ec75b5`, internal main YAML SHA256 `44a9d82154aac71d1b17adf62ed0a9901a1c1bd334cb1a943d5b8eae15ad6612`. Main YAML parses with strict duplicate keys, one 16-entry interval, 180 named entities, existing state_class for Heating Minimum; native CM930 shadow, V5/portable bridge and HARD_DENY. **Physically user-confirmed V5DCM19 FIX1 189 s and V5DCM20 18m33 RX/passive parity COMPLETE/POSITIVE** from separate live logs, but uploaded ZIP itself labels PREPARED and is NOT proven same bytes as flashed. Its UART config has `tx_pin GPIO17` (DE GPIO21 ALWAYS_OFF), unlike v31 FIX4 no TX pin. Archive checksum manifest incomplete/stale. v31/RX33 candidates retain broader HA entity coverage and resolved metadata, so no wholesale YAML regression. Offline decision: reconcile exact source, then integrate only V5DCM22 passive 33-package ledger into one proven V5 callback, while keeping all production HA and TX fail-closed. No new physical TX, no YAML changes. [Comparative audit](V5DCM/V5DCM19_FIX1_VS_V5DCM22_BASELINE_AUDIT_20261018.md).

---

# 2026-10-18 — **V5DCM22-RX33-01 STATCLASS FIX1 PREPARED / NOT RUN — Home Assistant LTS warning diagnosed.** User reports `sensor.zolder_thermia_itec_xtr_m_heating_minimum` had historical long-term statistics but has no current `state_class`. **DO NOT ACCEPT DELETE STATISTICS.** Confirmed original deployed-source v31 FIX4 and first RX33 YAML both omit `state_class` for `thermia_heating_min`, plus 39 other numeric physical-unit sensor definitions (21 temperature device class, 19 corrections/timing). New separate [FIX1 candidate](V5DCM/V5DCM22_RX33_STATCLASS_FIX1_PREPARED_20261018.yaml) adds exactly 40 `state_class: measurement` declarations. Removing new metadata recovers previous RX33 candidate byte-identically; all original IDs/units/names/bus parsing/health/DE LOW/TX-disabled unchanged. **Not ESPHome compiled, not flashed, not executed; original user-flashed FIX4 remains as was.** Next: user-controlled validation/OTA when desired; check HA Developer Tools entity state_class and warning, without deleting historical statistics; V5DCM22 native offline work remains separate. [Documentation](V5DCM/V5DCM22_RX33_STATCLASS_FIX1_PREPARED_20261018.md).

---

# 2026-10-18 — V5DCM22-RX33-01 **PREPARED / NOT RUN** — Next controlled user-facing XTR observation: source derived from user-flashed v31 FIX4 exact GitHub blob `f4b90fc...`; new *separate* full YAML [RX33 candidate](V5DCM/V5DCM22_RX33_ONLY_PREPARED_20261018.yaml) adds **4 diagnostic HA text sensors** (W2 15, W3 10, W4 8 strict geometry and aggregate), **7 internal globals**, no TX path, no changes to production original. Four insertions removed recover source byte-identical (static PASS), 33 exact verified descriptors, 11 new IDs all references resolve. Physical `0x0F FC16` start/count receive-only; `03E8/13` and `0410/21` intentionally do not satisfy XTR 14/22. Candidate summary explicitly says **C2 unverified**, no owner/epoch assumption. **YAML ESPHome compilation NOT VERIFIED, flashing and live execution NOT RUN.** Current user-deployed v31 FIX4 unchanged, remains RX-only RUNNING / PARTIAL. V5DCM22 offline CI from earlier commit `9c14bb3` SUCCESS is not a test of this new YAML. NEXT: user-controlled RX-only flash/15–30 min observation when ready, then results before proceeding. Abort/recover on any TX, bus regression or HA loss. [Experiment specification](V5DCM/V5DCM22_RX33_01_PREPARED_20261018.md).

---

# 2026-10-18 — **V5DCM22 source/CI validation verified PASS; overall RUNNING / PARTIAL awaiting native XTR device evidence.** GitHub Actions [39130592175](https://github.com/ryckema/Thermia_Connect_Firmware/actions/runs/39130592175) on firmware source `9c14bb3976985051d6a053664c828f0e59cb1525` is **SUCCESS**: exact-HEAD C++17 Core + RX package join, lifecycle safety, actual byte-replay executable compile, safe synthetic Python/C++-ledger replay, existing regressions, embedded parity and physical-TX hard deny all PASS. Separately executed local standalone C++ and Python on private original 20261003 capture: all 16 counters and 2 geometry lists agree (2687 CRC-valid, 162 native FC16, 33 selected starts, 31 exact local XTR geometries, 2 FC23, 0 qualified receipts / no C2). Negative CRC mutation fixture PASS both languages. **Do not conflate** actual GitHub CI's synthetic replay with exact-HEAD C++ execution on original raw capture; that latter combination is still not executed. No ESP32 flash/new local TX; current known-good v31 FIX4 remains RX-only. Next: determine whether any additional source-only tests needed, then plan a scoped RX-only 33-group provenance run preserving current known-good YAML. [Report](V5DCM/V5DCM22_CPP_PYTHON_PARITY_OFFLINE_20261018.md).

---

# 2026-10-18 — V5DCM22-REPLAY-02 **COMPLETE / POSITIVE (offline standalone C++17/Python parity)**; **V5DCM22 overall RUNNING / PARTIAL**. Strict standalone C++17 (-Wall -Wextra -Werror -pedantic) compiled and executed on *unchanged original* 20261003 capture SHA256 14918065297264473e2357822a8694d184e7821b8c2a3b1cb316039678a708a1; fresh Python replay agrees on **all 16 summary fields** and exact missing/mismatched geometry lists. 2687 CRC-good frames, 162 native 0x0F FC16, 33 required starts but 31 exact XTR geometries, 2 FC23 boundary invalidations, 0 qualified receipts/no C2, zero physical TX. CRC-mutation negative fixture PASS both languages. **Important limitation:** this C++ binary is an independent standalone comparator, NOT compiled from GitHub portable Core/actual PassivePackageIntegration. Current exact-HEAD GitHub C++ harness CI remains unverified because repo could not be cloned in offline container and CI status inaccessible. v31 FIX4 unchanged. Next: verify actual GitHub C++ class replay using repository source archive or verified CI; no automatic active TX. [Detailed report](V5DCM/V5DCM22_CPP_PYTHON_PARITY_OFFLINE_20261018.md).

---

# 2026-10-18 — V5DCM22-REPLAY-01 **COMPLETE / POSITIVE (offline byte-exact raw capture discriminator)**; V5DCM22 integration remains **RUNNING / PARTIAL**. Historical `thermia_capture_20261003_165355.log` SHA256 `14918065297264473e2357822a8694d184e7821b8c2a3b1cb316039678a708a1`: 2,687/2,687 valid CRC; 162 exact-length slave 0x0F FC16 requests; 33 selected starts, **31/33** local-XTR start/count shapes, mismatches `03E8/13` vs XTR14 and `0410/21` vs XTR22. Two valid 0x0F FC23 events at 27.400,27.429 **before** first FC16 at 29.262 force fail-closed provenance revocation; without explicit independently validated reselect: **0 qualified receipts**, no C2. Source-only C++ byte-replay harness, Python verifier and synthetic CI added to Thermia_Connect_Firmware; GitHub C++ execution **not yet verified**. User ESP32 v31 FIX4 RX-only unchanged; no physical TX. Next verify exact-HEAD C++ build, offline original capture run and qualify actual local XTR capture provenance. [Report](V5DCM/V5DCM22_RAW_CAPTURE_REPLAY_RESULT_20261018.md).

---

# 2026-10-18 — V5DCM22 RUNNING / PARTIAL update: historical 20261003 raw capture has 162 CRC-valid 0x0F FC16 requests, all 33 source-selected starts; only 31 match exact local XTR physical start/count. 03E8 count13 (XTR 14) and 0410 count21 (XTR 22) mismatch. Never count reference geometry as local C2. Strict synthetic 33-package test added to CI, actual CI success not verified. No deployed TX.

---

# 2026-10-18 — V5DCM22 RUNNING / PARTIAL: source-only 33-group W2/W3/W4 ExpectedPackage mapping and full synthetic receive-only frame replay checks committed to Thermia_Connect_Firmware. Source-selector bit and XTR counts checked; no real capture replay or successful fresh CI confirmed yet. Firmware production v31 FIX4 unchanged, TX off. Next verify CI and analyze actual passive XTR capture.

[Implementation update](V5DCM/V5DCM22_PACKAGE_INTEGRATION_PARTIAL_20261018.md)

---

# 2026-10-18 — V5DCM22 RUNNING / PARTIAL: new offline RX-only join combines existing validated AdapterEvent, PassiveRxJoin and PassivePackageLedger; source and strict CI test added to firmware repo. Source check performed, full compile/CI result not yet verified. No v31 FIX4 deployment, physical TX, native C2 or Online proof. Next: verify CI, add verified 33-group source mapping and passive replay.

[Implementation note](V5DCM/V5DCM22_PACKAGE_INTEGRATION_PARTIAL_20261018.md)

---

# 2026-10-18 — V5DCM21-PACKAGES-03 RUNNING / PARTIAL. ORIGINAL 2.1.105 appfs 2.3.0–2.4.3 JSON independently yields 570 objects, 541 numeric dependencies and EXACT same 33 W2/W3/W4 selected starts (15/10/8) as prior normalized index; 0 unmapped/ambiguous. Full field-by-field derived CSV equality OPEN (large GitHub CSV not retrievable in this runtime), but original-source package selection now POSITIVE offline. Current v31 FIX4 RX-only, no live native C2 or TX. Next: portable source-audit reproducibility and passive package-receipt chronology.

---

# 2026-10-18 — Original extracted 2.1.105 appfs profile 2.3.0–2.4.3 now directly available. Direct JSON count 99 sensors + 471 configs (570) and numeric formula/condition/min/max/default dependency union 541; both match normalized index aggregate. Original sensors/config/info-2.4.2 SHA256 documented in PACKAGES-03. Still not verified: object-by-object normalized CSV equality, and original JSON => W2/W3/W4 33-group mapping. V5DCM21-PACKAGES-03 RUNNING / PARTIAL, no live TX/YAML.

[Detailed original-JSON audit](V5DCM/V5DCM21_PACKAGES_03_RAUC_PROVENANCE_PARTIAL_20261018.md)

---

# 2026-10-18 — V5DCM21-PACKAGES-03 RUNNING / PARTIAL: source-equivalence gate: user original 2.1.105 RAUC present, SquashFS v4 zlib, not extracted (extractor absent); device_client.zip contains parser but not target JSON, appfs_2018.zip has only 2.3.0–2.4.1. Therefore 570 objects/541 dependencies/33 groups are normalized-derived, NOT proven exact original RAUC equality. No new TX/YAML/live run. Next: original read-only extraction and row/token comparison.

[Audit details](V5DCM/V5DCM21_PACKAGES_03_RAUC_PROVENANCE_PARTIAL_20261018.md)

---

# 2026-10-18 — **V5DCM21-PACKAGES-02 RUNNING / PARTIAL — SOURCE-DRIVEN PROFILE 2.4.2 SIGNIFICANT PACKAGE CENSUS CI PASS.** Inspected user `device_client.zip` original 2.1.105 `_get_all_data_package_to_request()`: union ONLY sensors+configs `significant_registers`, direct expressions/conditions/min/max/default token refs, integers deduplicated to W2/W3/W4 request-selector ranges; NOT operation/alarms/info parser in this C1 method, not write-formula targets. Existing normalized 2.1.105 `cm930_semantic_objects.csv` profile `2.3.0-2.4.3` with independent XTR `xtr_portable_profile_xtr_2_4_2.json` contains **99 sensor + 471 config definitions = 570**, **541 numeric dependencies**, **33 selected descriptor groups: W2=15, W3=10, W4=8**. This is computed from *normalized derived profile data*; direct byte-equivalence to full original RAUC profile not freshly reverified. Current user-flashed **v31 FIX4 read-only** 13-bit page Y/N observes only **13 of 33**, leaving **20 outside that diagnostic**; first 151s only `03E8:Y`, others N, later “nog steeds op N” without timestamp. Important exception: profile expects `0864` despite general read-all excluding it. All selector ranges are firmware-derived, physical FC16 counts from separate XTR evidence (not spans); never publish protected native responder or claim C2/Online. **Strict CI [39126103885](https://github.com/ryckema/Thermia_Connect_Firmware/actions/runs/39126103885) PASS**, firmware `cfafd2cd`, 10 new source-profile regression assertions, existing 26 package C++ + 24 Core + 46 RX + 22 delivery + 5+4+30+35, embedded parity/hard deny. No new live V5DCM21 test/flash/TX, autonomous TX standing permission and accepted G01–G06 risks retained. Historical EXP325–329 locally prove guarded ACK progression; V5DCM18 original 7-corpus Core replay still PARTIAL. Next verify normalized 2.1.105 profile against RAUC original, then 33-group chronology/presence analysis and scoped native response test design. [Full report](V5DCM/V5DCM21_PROFILE_242_SIGNIFICANT_PACKAGES_20261018.md).

---

# 2026-10-18 — READ-V31-UNKNOWN-01 / COOL-01 **RUNNING / PARTIAL — PERSISTENT N AFTER USER FOLLOW-UP**. User reports after the suggested additional wait that the missing pages are “nog steeds op N”. Exact new mask/ESP uptime and no-restart condition **not independently supplied**, so no exact long-duration claim. Earlier confirmed FIX4 151s boot window: only `03E8:Y`, other 12 `N`, 34 HA Unknowns sourced from ten absent qualified native page decoder branches; direct 0x1E bus healthy. **Offline new reconciliation** of supplied local XTR `thermia_capture_20261003_165355.log` and `thermia_capture_20260925_090550.log`: historical active native sessions transferred 03E8→03FC→0410→042E→0442 etc with per-page FC16 ACK (~14ms adjacency); controller runtime 07D0 etc followed. Canonical **EXP325–329 COMPLETE/POSITIVE local causal tests** prove qualified fresh-session response then exact owned ACKs (03E8/count14→03FC, 03FC→0410/count22, 0410→042E, through 0442) advance configuration sync. **FIX8H local 5min TX=0** observed 130 repeating 07D0 runtime pages *after* service chain had previously been established; does not prove fresh RX-only session. Older historical captures use 03E8/count13 vs newer tested XTR/count14, so never assume universal ACK geometry or owner. **STRONGLY SUPPORTED:** native config synchronization is ACK/session-dependent in locally tested contexts; strict physical RX-only FIX4 cannot promise all firmware-profile settings by simply waiting. **UNKNOWN:** exact current controller transport/owner and why current 03E8 still seen. **No new YAML/physical TX/test**, one-YAML+README unchanged. Next: offline session/provenance analysis and *separate* TX-assisted read-only-semantics profile only as a controlled user-initiated future test (NOT physically RX-only). Preserve FIX4 and V5 verified fallback. [FIX4 persistent-N follow-up and historical ACK-gated XTR evidence](V31_NATIVE_PAGES_N_FOLLOWUP_20261018.md).

---

# 2026-10-18 — V5DCM21-PACKAGES-01 newest DCM integration result: **RUNNING / PARTIAL** (strict firmware-repo source CI PASS; no V5DCM21 live experiment). Original Thermia Connect **2.1.105** device_client package tracker has three distinct W2/W3/W4 significant-data masks and separate C0 INITIAL -> C1 WAIT -> C2 ALL_RECEIVED; it is **not** handshake H2, cold B2/32-32, service M/R or full app OPERATION. Added private-safe/public RX-only `portable/xtr_v5dcm21_packages.hpp` + 26 guarded C++ tests and required CI. [Actions 39124813711](https://github.com/ryckema/Thermia_Connect_Firmware/actions/runs/39124813711) firmware commit `6a96c3a8cd517f689f4d420d0b8789bbd40abb4f` **SUCCESS**, 26 new assertions, previous 24 Core/46 RX/22 delivery/30 model/35 static callsite + 5+4 synthetic and hard-deny all PASS. Existing firmware-derived W2/W3/W4 **bit-to-range selector map is PROVEN**; **XTR 2.4.2 profile significant-register *subset* and actual per-profile expected package masks remain OPEN**, not invented. User's latest separate **v31 FIX4 live read-only** run is confirmed at 151s, only `03E8:Y`; keep distinct from V5DCM19/V5DCM20 former verified fallback and native V5DCM21 emulator. User's standing autonomous TX authorization continues, G01–G06 risks remain accepted, no physical TX/flash/public private responder occurred in this substep. V5DCM18 full original 7-corpus Core replay PARTIAL. **Next:** derive significant subset from verified 2.1.105 profile JSON then join to native page reports; do not substitute all 43 selectors as significant or infer Online from C2. [Evidence](V5DCM/V5DCM21_2105_PACKAGE_COMPLETENESS_OFFLINE_20261018.md).

---

# 2026-10-18 — **READ-V31-UNKNOWN-01 / READ-V31-COOL-01 RUNNING / PARTIAL — FIRST USER-CONFIRMED FIX4 LIVE EXECUTION.** The user explicitly confirmed FIX4 is flashed; ESPHome HA snapshot shows OTA-request reset, ESP uptime **151 s**, `Native Settings Pages Seen = 03E8:Y 03FC:N 0410:N 042E:N 0442:N 0532:N 0546:N 07D0:N 080C:N 0820:N 0848:N 0864:N 0870:N` and `Cooling Settings Page Source = 0442 NOT received since ESP boot`. **OBSERVED HA result:** the 13-bit passive source witness runs; one native `0x0F FC16 03E8` branch recognized and corresponding heating settings populated (curve 36°C, min/max 20/40°C, setpoint 22°C). All **10** native source families required by exact **34 Unknown** HA entities are N during this 151s run; native `0x0F` page reception problem is now **STRONGLY SUPPORTED for this short boot window**, not independently proven physical non-transmission. Direct outdoor `0x1E` functions still update (Idle, compressor 0Hz/0A, fan 0rpm, ambient 13°C), `Bus Healthy=Connected`. Source read-only TX pin absent, but **no physical DE/TX measurement, raw frame audit or independently witnessed ESPHome compile**. Keep **RUNNING / PARTIAL**, NOT overall COMPLETE/POSITIVE: 151s insufficient for source cadence, 12 pages could appear later, or frame geometry/decoder may exclude other shapes. **No YAML changes**; FIX4 unchanged at blob `f4b90fcd3d96cb728ba4726409bacd9d5c23b5f3`. One-YAML/README structure maintained. Next passive-only action: allow 15–30 minutes with **no ESP/controller reboot**, then obtain just Native Settings Pages Seen, Cooling Settings Page Source and ESP Uptime. Review before proposing TX or new YAML. User confirms FIX4 active, supersedes prior PREPARED/not-flashed speculation. Verified V5 RX baseline remains available for recovery; firmware 524-row catalog unchanged. [Live FIX4 151s Unknown/page-receipt audit](V31_ALL_UNKNOWNS_HA_AUDIT_20261018.md).

---

# 2026-10-18 — USER AUTHORIZATION UPDATE: **GENERAL AUTONOMOUS NATIVE TX NOW ALLOWED IN PRINCIPLE**. User explicitly states “Algemene, autonome TX-bevoegdheid: nu toegestaan.” This supersedes prior prohibitions on *general permission* and repeated per-response approval; allows development and, within a documented user-initiated, armed live deployment/test, autonomous controller-driven responses/handshakes/owned native protocol TX. **NOT a physical experiment, no flash, no TX occurred from this decision**. G01–G06 accepted research risks remain accepted, *not technically proven* or automatically six blockers. Fail-closed context/CRC/owner/known response slots, bounded retry, abort/rollback and confidential native responder protection remain; no uncontrolled scans/unknown ACKs/unsolicited speculative writes. Installed user-confirmed V5DCM19 FIX1 and V5DCM20 18m33s baseline still RX-only HARD_DENY until verified deployment of new code. V5DCM21 RUNNING / PARTIAL; private native response and app Online still unproven. [Authoritative dated authorization decision](NATIVE_AUTONOMOUS_TX_AUTHORIZATION_20261018.md).

---

# 2026-10-18 — Full-name HA Unknown source refinement (**OBSERVED user HA snapshot / SOURCE AUDIT, no new experiment**): user supplied exact current 34 `Unknown` entities, superseding the earlier PDF's 33 visually printed/truncated Unknown tally; **15 normal + 19 diagnostic**. All 34 map uniquely by current FIX4 YAML decoder to **10** controller-native 0x0F FC16 source families: `0442=7, 0410=4, 042E=4, 0532=4, 07D0=4, 0864=4, 0870=3, 0848=2, 0546=1, 0820=1`. User simultaneously reports 0x1E-linked live compressor 22 Hz, 0.8 A, heating mode, fan 380 rpm and bus Connected; healthy direct reception does not prove native source pages were emitted. **Root cause OPEN:** absent full pages since ESP boot (plausible), blocked invalid/sentinel values, intentional option fail-closed, or actual enum literal Unknown. Neither FIX4 `Native Settings Pages Seen` nor FIX3 `Cooling Settings Page Source` appears in user's posted list, so exact installed firmware/registry is not independently established. No YAML edits, flash or TX; latest FIX4 remains PREPARED / NOT RUN, known-good V5 passive baseline intact. Next: user-confirmed FIX4 binary and the one 13-page Y/N string, not sweeping log requests. [Exact 34-name Unknown source matrix](V31_ALL_UNKNOWNS_HA_AUDIT_20261018.md).

---

# 2026-10-18 — READ-V31-UNKNOWN-01 FIX4 **PREPARED / NOT RUN**, no live device experiment. Reviewed user's Oct18 12:43 7-page HA PDF: **33 rendered Unknown rows** (p1–p7 counts 4/4/5/4/9/5/2) alongside working 0x1E compressor 20 Hz and mode Heating; all entity labels are truncated, no exact flashed blob or controller 0x0F native page receipt supplied. Audit identifies at least 13 relevant controller-native page families whose absence may explain settings Unknowns (03E8/03FC/0410/042E/0442/0532/0546/07D0/080C/0820/0848/0864/0870); also possible invalid sentinels, intentional optional fail-closed and literal 'Unknown' enum strings. Controlled source-only observability change committed to **the sole** `Read-only/Thermia itec XTR/thermia_itec_xtr_m_read_only.yaml`: FIX4 new `Native Settings Pages Seen` diagnostic, one nonpersisted bitmask, Y/N since ESP boot set only in existing valid full-page decoder branches; no TX or extra polling. Commit `6c24cffffbaf091c88fd68961e1abb5d872dcaa6`; **257 prior HA names preserved, 258 total (187 numeric, 60 binary, 11 text)**; static unique ID/reference/substitution/no TX/DE-off checks pass. **Not compiled, flashed or live checked**; v31 FIX4 remains PREPARED / NOT RUN, verified deployed V5DCM19 FIX1 and V5DCM20 passive positive untouched. XTR folder still **one YAML + README**. [Full 33 Unknown HA audit and FIX4 source mapping](V31_ALL_UNKNOWNS_HA_AUDIT_20261018.md). Next user-initiated passive test: two diagnostic text states and a full-name Unknown, then only a narrow RX frame if needed. XTR native Online/DCM main research and 524 firmware profile completion unaffected.

---

# 2026-10-18 — V5DCM21 latest: **RUNNING / PARTIAL** overall; new offline delivery/provenance audit **STRICT HOST CI PASS**, no user-confirmed on-device experiment. Current firmware `105735f5543dc009422c76e61d292b20145ad006`: added `portable/xtr_v5dcm21_delivery_audit.hpp`, host adapter regression and required CI. True `PlatformPort::DeliveryCode::Delivered` means successful *local callback* write/flush/enter_rx, NOT physical RS485/remote XTR acceptance. Nontransmitting read-only auditor distinguishes prepared/host-delivered/faulted/stale/duplicate and separately externally attested owner/slot/epoch/wire. **Always native_response_sent_inferred=false, controller_accepted_inferred=false, application_ready_inferred=false, tx_authorized=false**. Mandatory [Actions 39122071866](https://github.com/ryckema/Thermia_Connect_Firmware/actions/runs/39122071866) PASS strict actual HEAD **24 Core, 46 RX join, 22 delivery/adapter-memory fake, 5 capture, 4 temporal, 30 model split, 34 callsite** + embedded/Core parity and TX deny. Host-only MemoryHalfDuplexIo delivered and Flush-failed path tested; no electrical bus operations. **Exact installed FIX1 YAML/ZIP still not byte-proven**, user-flashed RX-only baseline V5DCM19 FIX1 and V5DCM20 live 18m33s POSITIVE unchanged. Controller epoch/real owner/physical slot/native response/app profile+packages/Online **OPEN**; V5DCM18 full 7-corpus stateful replay PARTIAL, G01–G06 accepted. Next offline independent provenance/evidence-provider audit before any private guarded response interface; no YAML/flash/TX. [Result](V5DCM/V5DCM21_DELIVERY_PROVENANCE_AUDIT_RESULT_20261018.md).

---

# 2026-10-18 — **V5DCM21 latest RUNNING / PARTIAL**; new MODEL-SPLIT and genuine FC23-followup **offline validations PASS**, not new/user-confirmed live experiment. Original firmware-derived Python reference deliberately auto-promotes internal RESPONSE_SENT→ACCEPTED on most FC16 requests **before owner classification**, including a synthetic out-of-order 03FC/count11 with Owner.NO; it also does not validate foreign slave in its direct Core API. C++ public/embedded `fc16_decision(... ) const` remains pure/fail-closed, not a rewrite of proven Thermia firmware semantics. Mandatory current source CI [39121165286](https://github.com/ryckema/Thermia_Connect_Firmware/actions/runs/39121165286), firmware `83b4fc789dccc1c40a9f8e787d2d6587bd586491`, SUCCESS: 30 original-model boundary assertions + 4 temporal synthetic scenarios + existing 24 Core/46 RX/33 callsite/5 capture, exact embedded parity/TX deny. Independently checked user-provided genuine/collaborator captures: Eco5 Sep26/28 **99/2 and 64/4 FC23 request/reply shapes**, ATEC Oct03 **1/1**, seven reply-shaped CRC-valid frames followed by first 0x0F FC16 **03E8**, six modern count14 and one legacy count13, in **92–1833 ms**. Shape/time does not validate protected response contents, native ACCEPTED, physical owner/epoch/slot, Connect profile/package OPERATION or Online. Exact deployed V5DCM19 FIX1 source still not byte-proven; user-flashed RX-only baseline and V5DCM20 positive unchanged. V5DCM18 full original seven-corpus stateful replay remains PARTIAL; G01–G06 accepted. **Next** offline response-delivery/provenance witness design, not an active TX test. [Full evidence](V5DCM/V5DCM21_MODEL_SPLIT_AND_GENUINE_FC23_FOLLOWUP_RESULT_20261018.md).

---

# 2026-10-18 — READ-V31-COOL-01 source FIX3 **PREPARED / NOT RUN**: User's 7-page HA PDF showed many Unknowns while outdoor heating/20 Hz compressor were populated; the PDF truncates entity IDs and does not confirm complete `0x0F FC16 0442/count13` since latest ESP boot. Source review found v31 FIX2 only covered seven of 13 cooling settings word positions; EXP382 had STRONGLY SUPPORTED candidate semantics for 0444/0446/0448/044A/044B, with 0447 HYPOTHESIS; EXP379 local cooling hysteresis 044D PROVEN. **Controlled source change only:** v31 FIX3 at `Read-only/Thermia itec XTR/thermia_itec_xtr_m_read_only.yaml`, commit `a3be92f113f0e06a53ec619f63aec930139f9ce4`. Added six disabled-by-default **RAW** diagnostic fields 0444/0446/0447/0448/044A/044B and enabled `Cooling Settings Page Source` (observed/not observed since ESP boot); total **257** named HA entities = 187 sensors + 60 binary + 10 text; 250 prior names retained; existing interpreted seven untouched. No extra requests, stale cache, fabricated cooling values, TX pin or DE activity; all existing IDs/substitutions resolve and no duplicate IDs in static source. **Not performed:** full YAML parser, ESPHome compile, flash, passive live test, physical TX instrument, HA registry confirmation. Do not claim fix for Unknown until 0442 receipt/values or exact flashed source verified; absence of native Online/DCM may mean settings page not republished after OTA. XTR folder remains EXACTLY one YAML + one README. Separate verified deployed V5 RX-only baseline untouched. [FIX3 cooling gap and Unknown audit](V31_COOLING_UNKNOWN_AUDIT_20261018.md). Next passive 0442 RX evidence, then only meaningful semantic promotion.

---

# 2026-10-18 — READ-V31-COOL-01 analysis **PREPARED / NOT RUN**, no YAML/flash/bus changes: user supplied seven-page Home Assistant device PDF dated 2026-10-18 12:43. Populated compressor 20 Hz, fan 380 rpm and heating mode coexist with many HA `Unknown` entries; PDF truncates entity names and does not provide any native 0x0F 0442/count13 receipt or exact flashed YAML fingerprint. Audited current public v31 FIX2: cooling 0442/count13 publishes only **7/13** words (0442,0443,0445,0449,044C,044D,044E); six not exposed: 0444 cooling hysteresis, 0446 service config, 0447 uncertain START, 0448 STOP, 044A max STARTTEMP, 044B min STOPTEMP. Earlier XTR EXP379 locally proved 044D hysteresis; EXP382 strongly supports 0444,0446,0448,044A,044B and keeps 0447 hypothesis only. Runtime `Cooling Active` from 0x1E is distinct from settings `Cooling Enabled` on 0x0F:0442. No 0442 in current capture is **HYPOTHESIS**, not proven; lack of genuine DCM may inhibit complete native-page republication. Next prioritize passive page-seen/age diagnostics over blind semantic filling. READ-V31-COOL-01 proposed scoped RX-only source observability **PREPARED / NOT RUN**; no generated YAML or new live data. [v31 cooling/Unknown source audit](V31_COOLING_UNKNOWN_AUDIT_20261018.md). Existing V5 known-good and one-YAML/one-README XTR folder untouched.

---

# 2026-10-18 — Cross-model RX-only expansion feasibility documented, **DESIGN / SOURCE AUDIT ONLY**; all proposed CM-RO-01…05 future builds **PREPARED / NOT RUN**. Firmware `ALL_PARAMETERS_ACCESS_MATRIX.csv` has 564 rows split across semantic CM930 ranges: 516 (1.1.1–2.1.0), 526 (2.2.0–2.2.1), 524 (2.3.0–2.4.3), 526 (3.0.0–3.1.1), with 492 shared across all. These are firmware register mentions, NOT physical passive accessibility or matching commercial models. Public RX-only sources already exist: XTR v31 FIX2 (250 HA names), iTec Eco v01 (90), ATEC v01 (112), DHP-AQ v02 (96); all four had no TX pin and DE restore OFF in source review. Firmware profile geometry differs (ATEC 03E8/count13 vs Eco5/XTR/count14; 0410 21 vs22; historical 0884 legacy records). Legacy 0867 raw values 0/0x16 do NOT safely identify a modern CM930 profile. Recommended shared passive decoder and evidence-gated per-model self-contained YAML, preserving exactly one YAML plus README in XTR folder. **No YAML changed, compiled, flashed or tested; no new bus/firmware-local proof or active TX.** Existing v31/XTR known-good V5 state unaffected. [Cross-model RX-only profile roadmap](CROSS_MODEL_READONLY_PROFILE_ROADMAP_20261018.md); next offline matrix join, then candidate Eco/ATEC/DHP-AQ profiles only where captured evidence supports.

---

# 2026-10-18 — V5DCM21 latest: **RUNNING / PARTIAL** overall; bounded **V5DCM21-CALLSITE-GUARD offline COMPLETE / POSITIVE**. In current public firmware portable/embedded source, legacy `Core::qualify_handshake()`, `set_mailbox()`, `set_runtime_normal()` remain test-fixture setters, but no direct production callsites in 27 audited files. Mandatory fail-closed static source guard now scans them and self-tests unsafe injected setter calls. New joined RX fixture verifies **full synthetic cold 32/32 does not promote live Core handshake/bootstrap/mailbox/write readiness**. GitHub Actions [39119204399](https://github.com/ryckema/Thermia_Connect_Firmware/actions/runs/39119204399), firmware `0f5b358235cca8f31db7d45bf5a313d2d4675652`, **SUCCESS**: 24 Core readiness/FC16, 46 adapter RX-only, 5 synthetic capture, 33 production callsite assertions, embedded/portable Core parity + strict embedded compilation, TX hard-deny. Source reviewed: `BoundaryFedAdapter` stages response-dependent state until delivery; passive no-record processing may commit observations. **This is NOT electrical or native acceptance proof.** Production user-flashed V5DCM19 FIX1/YAML unchanged; V5DCM20 live 18m33s POSITIVE. Exact deployed FIX1 YAML/ZIP still not byte-proven: do NOT wire/flash speculative replacement. V5DCM18 original full 7-corpus Core replay PARTIAL, accepted G01–G06 unchanged, physical owner/slot/epoch, native application required packages, icon and Online OPEN. [Full handoff](V5DCM/V5DCM21_CALLSITE_GUARD_AND_RX_NONPROMOTION_RESULT_20261018.md).

---

# 2026-10-18 — READ-V31-OPTIONAL-FIX2 & XTR folder consolidation, **PREPARED / NOT RUN** (user-authorized source work complete; no on-device experiment): New canonical `Read-only/Thermia itec XTR/thermia_itec_xtr_m_read_only.yaml` (250 unchanged entity names) and sole sibling `README.md`; target directory verified to have **exactly two files**. Old complete directory including 6 old versions, v29 and earlier v31 and six v31 research documents archived byte-for-byte at `Research/Archive/Read-only_XTR_before_FIX2` via original Git tree. Branch commit `4b83915d7899a2ee3ef4218b1a70689c4fa38fa8`; new YAML blob `9b3c7427db82c23753076d7787d49b8acc03884c`. Root `Read-only/README.md` updated. Conditionals: passive 0x0F FC16 0532/count18 candidate `0533 pool`, `0534 shunt1/second circuit`, `0535 shunt2/third circuit`, `0536 buffer`; accepted only with flag == 1 and fresh page; unknown/OFF/invalid/older than **6h** fails closed. Six hours is an unvalidated provisional timeout. Numeric optional entities cleared via NAN, pool active/queued binaries invalidated, 5s expiry callback; native raw register diagnostics retained (HA default-disabled). Capability flags lose validity on stale page. Source-only checks PASS: 250-to-250 unchanged entity names, no undefined/duplicate IDs, CRC bookkeeping preserved, no configured UART TX pin, DE always LOW. **Not performed:** full YAML parser, ESPHome compile, flashing, any native TX/live testing or HA registry check. ESPHome disabled_by_default is *static*: user must manually enable optional HA entities once, and use conditional Lovelace cards (example in new README) for automatic dashboard visibility. **Separate v31 524-firmware-register full-coverage work remains OPEN**. Existing live-deployed V5DCM19 FIX1/V5DCM20 result and native V5DCM21 roadmap unchanged. Definitive [source audit](V31_OPTIONAL_CONSOLIDATION_RESULT_20261018.md). Rollback to verified deployed build; archived pre-FIX2 v31 blob `debedae0c22a6d20d29cadbbb46ef0426cf70c06` is source only.

---

# 2026-10-18 — V5DCM21 latest: **RUNNING / PARTIAL** overall; **embedded Core parity offline substep COMPLETE / POSITIVE**. Direct source diff found `components/thermia_portable_bridge/xtr_core.hpp/.cpp` still had pre-authorization FC16 handshake mutation after portable Core was fixed. Mirrored only the pure `fc16_decision(const Frame&) const` change into embedded HPP/CPP; both pairs now **byte-identical**. Mandatory CI [39118302777](https://github.com/ryckema/Thermia_Connect_Firmware/actions/runs/39118302777), firmware HEAD `a1595e69`, PASS strict separate embedded Core C++17 compile + exact `cmp` parity + 24 readiness/FC16, 45 RX join, 5 Python synthetic checks, TX hard-deny. Original reference Core CI also PASS [39117997136](https://github.com/ryckema/Thermia_Connect_Firmware/actions/runs/39117997136) after separate C004 validator drift fix. **No production FIX1 YAML/flash/TX changed**; actual flashed FIX1 source still absent/not byte-verified, so embedded repo parity does NOT prove deployed change. `Core::qualify_handshake()` explicit setter and real owner/slot/epoch/service/app readiness OPEN; private native responder/Online unproven. Keep V5DCM20 local 18m33s positive, V5DCM18 full Core replay partial, G01–G06 accepted. [Embedded parity report](V5DCM/V5DCM21_EMBEDDED_CORE_PARITY_RESULT_20261018.md).

---

# 2026-10-18 latest — V5DCM21 overall **RUNNING / PARTIAL**; offline C004 validator reconciliation **COMPLETE / POSITIVE**, separate from completed pure-FC16 + generation CI substep. Firmware platform contract has 3 existing C004 interface names / 7 rules; stale validator assumed 2 / 4. Validator-only commit `1067f49b84bd92a8675435c1a205a66d1e747437`; mandatory original [Reference core unit validation 39117997136](https://github.com/ryckema/Thermia_Connect_Firmware/actions/runs/39117997136) **SUCCESS**, including 18/18 contract checks and portable C++ reference tests. Earlier identical C004 failure verified on 2026-10-17; not caused by latest Core change. Separate [V5DCM21 strict 39117672490](https://github.com/ryckema/Thermia_Connect_Firmware/actions/runs/39117672490) PASS 24 FC16/readiness + 45 RX join + 5 Python synthetic, TX hard-deny. **No YAML/flash/live TX, exact deployed FIX1 source still unresolved**, so no direct V5 callback integration or native Online claim. V5DCM20 last live 18m33s POSITIVE and known-good FIX1 untouched. Original V5DCM18 7-corpus full Core stateful replay PARTIAL, G01–G06 accepted. Next direct `qualify_handshake()` call-site/provenance and delivery-commit audit, exact installed FIX1 fingerprint. [C004 result](V5DCM/V5DCM21_C004_REFERENCE_WORKFLOW_RECONCILIATION_20261018.md).

---

# 2026-10-18 — V5DCM21 **RUNNING / PARTIAL** overall; new offline core-purity + passive-source generation substep **COMPLETE / POSITIVE**. Firmware portable Core `fc16_decision` is now `const` and no longer promotes ResponseSent to Accepted simply on frame classification; `PassiveRxJoin` increments **local observation generation (NOT controller epoch)** and records bus-return/CRC/FC23/input-source change invalidation. Strict actual HEAD GitHub Actions [39117672490](https://github.com/ryckema/Thermia_Connect_Firmware/actions/runs/39117672490) at firmware `a2042fc2` PASS **24 C++ readiness+classification, 45 C++ RX join, 5 Python metadata smoke and static TX deny**. No production YAML/flash/TX; known-good live XTR V5DCM19 FIX1 / V5DCM20 18m33s positive unchanged. **Critical blockers:** exact deployed FIX1 ZIP/YAML source and callback still not byte-verified; independent physical slot/owner/epoch and real Online unknown. The legacy `qualify_handshake()` setter is still independently callable; it is NOT an owner gate. Existing separate Reference-core CI red since Oct17 at stale `C004_INTERFACE_NAMES` public contract-validator drift; not fixed in this substep. Full V5DCM18 original session replay PARTIAL and G01–G06 accepted. [Report](V5DCM/V5DCM21_OBSERVATION_GENERATION_AND_PURE_FC16_RESULT_20261018.md).

---

# 2026-10-18 — READ-V31 optional feature audit: **SOURCE REVIEW ONLY; v31 PREPARED / NOT RUN**. Actual v31-alpha01 FIX1 has native 0533 pool/0534 circuit1/0535 circuit2/0536 buffer capability decoding and HA disabled_by_default on pool measurements, but **does not fully satisfy conditional visibility**. Pool start/stop raw, pool temp raw and Pool Heating Active / Pool Demand Queued publishing lack consistent known-ON gating; capability data has no confirmed stale-expiry contract. Optional shunt/buffer numeric measurements have partial guards with NAN on known OFF, not dynamic HA enablement. ESPHome disabled_by_default is static registration-time. No YAML changes, flashing or physical TX; existing V5DCM19 FIX1 deployed baseline unaffected. Next source candidate: consistent fail-closed per-feature availability on valid/fresh flags; HA dashboard conditional cards for automatic presentation, preserving all raw data and unique registers. [Audit](../Read-only/Thermia%20itec%20XTR/V31_OPTIONAL_CAPABILITY_AUDIT_20261018.md).

---

# 2026-10-18 — V5DCM21 latest: **RUNNING / PARTIAL** overall; new offline provenance/capture replay substep **COMPLETE / POSITIVE**. Actual user-provided Eco5 collaborator RTU logs Sep26/Sep28 replayed with CRC validation: 10,719/10,719 and 9,174/9,174 CRC valid; native 0x0F FC16 1058/1105; strict cold maxima **28/32, 24/32**, no full. Uploaded Oct03 2687-row *fragment* begins after 03E8/14 (0/32); does NOT overturn earlier full Oct03 corpus 1×32/32. Source-only firmware `tools/validate_v5dcm21_passive_capture.py` and synthetic tests added; actual HEAD Actions **39116725303 PASS** 22 C++ readiness + 43 C++ adapter join + 5 Python smoke, TX denied. Crucial **BLOCKER: exact deployed V5DCM19 FIX1 YAML/ZIP absent from both current GitHub trees, source byte-equivalence NOT VERIFIED**. Do not wire into assumed YAML, flash, or claim controller acceptance. Installed RX-only FIX1 and V5DCM20 live positive unchanged; V5DCM18 complete original stateful replay still PARTIAL, G01–G06 accepted. Next exact deployed source provenance and same-callback nontransmitting integration only when source verified. [Source and capture report](V5DCM/V5DCM21_CAPTURE_PROVENANCE_AND_RX_REPLAY_20261018.md).

---

# 2026-10-18 — v31 R1–R11 USER-APPROVED CLEANUP: PREPARED / NOT RUN, **offline source edits finished, no live experiment**. Updated public v31-alpha01 FIX1 at `Read-only/Thermia itec XTR/thermia_itec_xtr_m_waveshare_v31_full_monitoring_alpha01.yaml`: 300→250 HA named entities, 50 removed (R1–R6, R9–R11) plus R7/R8 three diagnostics newly disabled-by-default. Current 181 sensor / 60 binary_sensor / 9 text_sensor, 86 default enabled / 164 disabled / zero internal. Generic RX parser/CRC and optional 0533–0536 gates, 0539 RAW, native measurement sources, bus-health bookkeeping, DE LOW and absent UART TX pin preserved. Static source checks passed: 265 unique IDs, 263 distinct valid id() refs, no missing substitutions, no duplicate top-level keys, no UART write, post-write GitHub readback. **NOT verified:** strict YAML parse with YAML engine, ESPHome compile, flashed run, HA registry, bus TX counter/CRC health on device. Existing deployed V5DCM19 FIX1 and V5DCM20 live positive remain unaffected; V5DCM21 native readiness track unchanged. Next: full ESPHome config/compile validation, then only user-initiated passive v31 on-device comparison; 524 XTR firmware schema coverage remains open. [Audit](../Read-only/Thermia%20itec%20XTR/V31_R1_R11_CLEANUP_AUDIT_20261018.md) · [250-entity inventory](../Read-only/Thermia%20itec%20XTR/V31_ENTITY_INVENTORY_20261018.md). Source commits `1ba0a5a0`, `2f876fed`, inventory `1866221b`. Rollback pre-cleanup blob `d81bd7673ae33d4e51460e81e18fb0e425c86c4d`.

---

# 2026-10-18 — V5DCM21 newest: RUNNING / PARTIAL overall, but original portable RX-path passive join CI **COMPLETE / POSITIVE**. Firmware commit `1c045872c155dd0548d280cbd2be5ab494bcb054`, Actions run 39115058751 PASS strict actual-HEAD Core/wire/frame/adapter/bridge compile and synthetic **22 readiness + 43 RX-join** checks; output policy stays hard-denied and no TX call in fixtures. `portable/xtr_v5dcm21_rx_join.hpp` consumes existing complete-frame AdapterEvent or validated Frame; no second UART parser, mutable Core approval or response. Strict cold 32/32 is observation ONLY; unknown epoch, owner, native approval, application readiness and Online remain unclaimed. **Deployed live V5DCM19 FIX1 RX-only/YAML unchanged**; last on-device V5DCM20 positive. Actual FIX1 frame callback not independently audited/wired into this source yet; next exact source review, external reset/epoch provenance and integration as observer only. V5DCM18 original Core replay PARTIAL; G01–G06 accepted. [Verified report](V5DCM/V5DCM21_PASSIVE_RX_JOIN_CI_RESULT_20261018.md).

---

# 2026-10-18 — v31 entity inventory extracted directly from public v31-alpha01 YAML (blob `d81bd7673ae33d4e51460e81e18fb0e425c86c4d`): 300 named entities = 192 sensor + 92 binary_sensor + 16 text_sensor; 92 HA default enabled, 178 HA disabled-by-default, 30 internally hidden. `Active Mapped Faults` text sensor remains HA-visible despite intended alarm/fault exclusion: unresolved UI defect, no YAML modifications. [Full row-by-row YAML inventory](../Read-only/Thermia%20itec%20XTR/V31_ENTITY_INVENTORY_20261018.md). v31 still PREPARED / NOT RUN, not complete 524-profile coverage; existing live V5 and native DCM roadmap unchanged.

---

# 2026-10-18 — V5DCM21 latest: RUNNING / PARTIAL overall; **exact HEAD CI C++17 readiness/observer regression COMPLETE / POSITIVE**. Firmware commit `1ca3cf60158ecdc8b8d83450c359673a84b7f273`; GitHub Actions run 39114268008 PASS mandatory checkout/compile/run/deny, **22/22 source-backed offline assertions**. New read-only gate explicitly requires path match, current controller epoch and independent fresh-session attestation; cold 32/32 only cold; retained/recovery need independent config evidence; stale session, unhealthy controller and invalid epoch deny descriptive readiness. `live_tx_permitted=false` remains invariant. Production V5DCM19 FIX1 RX-only, no YAML/flash/TX; V5DCM20 18m33s POSITIVE. **Open:** exact physical owner/slot, provenance reset (retained epoch can stay unchanged), V5 observer-to-deployed callback join, general firmware-dependent response and app Online. V5DCM18 original full Core replay still PARTIAL; G01–G06 remain accepted. [Actual result](V5DCM/V5DCM21_HEAD_REGRESSION_RESULT_20261018.md).

---

# 2026-10-18 — READ-V31 full coverage source inventory audit, PREPARED / NOT RUN. Direct review of `Thermia_Connect_Firmware/parameters/ALL_PARAMETERS_ACCESS_MATRIX.csv` shows 564 firmware register rows, 524 with XTR 2.4.2 profile=YES (468 firmware write-capable, 56 runtime read-only) and 40 other-profile-only; these are schema entries, NOT 524 local XTR bus-proven readings. v31 is to inventory ALL 524, not only 46 INFO / 24 SERVICE name matches; the 494 UNCONFIRMED entries need classification, not exclusion. Every observed XTR register should be decoded or exposed RAW as read-only diagnostic unless calendar/alarm excluded, with option guards, freshness and no fabricated semantic values. No new YAML/flash/TX. [Coverage contract](../Read-only/Thermia%20itec%20XTR/V31_ALL_PARAMETERS_COVERAGE_CONTRACT_20261018.md).

---

# 2026-10-18 — READ-V31 manual taxonomy documented, PREPARED / NOT RUN: additional user-supplied AWIXT01CG0210 commissioning manual photos confirm INFO (§7) and SERVICE (§8) grouping. New documentation-only [Manual hierarchy](../Read-only/Thermia%20itec%20XTR/V31_MANUAL_MENU_STRUCTURE_20261018.md); no YAML, native protocol, flash or live state changes. v31-alpha01 is still a candidate lacking complete per-parameter native-source/HA coverage audit; optional shunt groups 1/2 represent 2nd/3rd heating circuits, pool/buffer optional. Exclude calendar, alarms, actuator/test/reset controls. Earlier verified V5DCM20 and V5DCM21 states unchanged.

---

# 2026-10-18 V5DCM21 RUNNING / PARTIAL — offline compiler smoke PASS on locally recreated current Core declarations and evaluator/test assertions; NOT a verified GitHub HEAD checkout (network clone unavailable), NOT observer compile or live XTR proof. New firmware passive observer source `portable/xtr_v5dcm21_observer.hpp` commit `947200841159e0caced6d5930aa4f6386778554a`; returns read-only gate snapshot from const Core and externally independently qualified evidence, with TX-disabled bridge assertion. No Core, production YAML, native TX or firmware challenge adapter changes. V5DCM20 deployed RX-only good; G01–G06 accepted unchanged; V5DCM18 original full replay PARTIAL. Next actual HEAD compiler/regression and source-to-observer integration, retained/rejoin evidence gates. [Report](V5DCM/V5DCM21_OFFLINE_COMPILE_AND_OBSERVER_PARTIAL_20261018.md).

---

# 2026-10-18 — v31 Full Monitoring read-only track: PREPARED / NOT RUN. A new public RX-only `Read-only/Thermia itec XTR/thermia_itec_xtr_m_waveshare_v31_full_monitoring_alpha01.yaml` was created from firmware repo v30-alpha12, without replacing known-good v29 or live V5DCM19 FIX1. Alarm/fault/calendar HA entities are internal, eight optional-circuit settings newly HA-disabled-by-default; installed capability flags preserved. Static ID/substitution and absent UART TX pin checks passed. No full ESPHome compile, flash, live HA validation, or claim of exhaustive parameter coverage. HA `disabled_by_default` cannot dynamically re-enable existing registry entries; optional runtime availability must be separately audited. Native Online/DCM V5DCM21 remains PREPARED / NOT RUN and unaffected. [Scope](../Read-only/Thermia%20itec%20XTR/V31_FULL_MONITORING_SCOPE.md).

---

# 2026-10-18 — V5DCM21 RUNNING / PARTIAL: nontransmitting readiness-gate source added to Thermia_Connect_Firmware. New `portable/xtr_v5dcm21_readiness.hpp` and `portable/test_xtr_v5dcm21_readiness.cpp`, firmware commit `8dc5918d63967dc53f500fb637f92d7cda1902b2`. Pure read-only State+independent evidence evaluation; internal handshake, physical ownership, cold reference config, app data, service and semantic receipt separate; always returns live_tx_permitted=false. No Core/adapter/ESPHome/YAML modifications, flash or TX. **Test file added, compilation/execution NOT VERIFIED; partial, NOT complete**. Later work: test against current HEAD, model retained/recovery positive evidence rather than treating unknown as complete, integrate under observer with no output, compare original reference and G01-G06 constraints. V5DCM20 positive baseline and V5DCM18 full roadmap partial unchanged. [Contract](V5DCM/V5DCM21_TX_READINESS_CONTRACT_PREPARED_20261018.md).

---

# 2026-10-18 — V5DCM21 PREPARED / NOT RUN: native DCM integration contract. Preserve proven 0x0F exact framing/CRC, FC16 pages and owner guards; replace fixed R1 only via private firmware-derived request-dependent adapter; separate firmware handshake, physical owner/TX, config and application readiness. No generic ACK, no universal V4.1 timing. **No TX, YAML change, flash or experiment execution**. Live baseline remains V5DCM19 FIX1 with V5DCM20 COMPLETE / POSITIVE 18m33s RX-only, zero physical TX. V5DCM18 original full Python replay remains PARTIAL; G01-G06 accepted. [Contract](V5DCM/V5DCM21_TX_READINESS_CONTRACT_PREPARED_20261018.md).

---

# 2026-10-18 latest: V5DCM20 COMPLETE / POSITIVE for live passive RX-only duration 18m33s, superseding the earlier PREPARED row below. V5DCM19 FIX1 retained; 37 V5DCM19 diagnostic cycles, parser V5 6590->16050, B11C V5=portable 15885, B11D raw=portable=V5 15880 with zero byte/count divergence. Resync 11->11, integrity 1->1, drops 0, TX candidates 2619 denied 2619 physically sent 0. Natural fan stop/start and compressor ON occurred; selected HA values NaN during part of transition (semantic question). No native challenge/acceptance, owner, slot or Online icon proof. Next V5DCM21 offline TX-readiness audit based on V4.1 + original CM930 reference; G01-G06 accepted risks stay closed; no active TX without explicit separate test. Full V5DCM18 original reference Python replay still separately open.

[Full result](V5DCM/V5DCM20_LIVE_RX_ONLY_RESULT_20261018.md).

---

# V5DCM20 PREPARED / NOT RUN (2026-10-18): original roadmap live passive XTR validation, no new YAML/flash or TX. Deployed V5DCM19 FIX1 positive 189s baseline. Controlled change 10-minute continued passive duration checking B11C/B11D count and byte parity, resync/integrity/drop trends, HA sensors and physical TX attempts zero. Earlier V5DCM20 host-only synthetic 24/24 separate and not live completion. Accepted G01–G06 unchanged. Report: V5DCM/V5DCM20_LIVE_RX_ONLY_PREPARED_20261018.md

---

# 2026-10-18 V5DCM19 FIX1 live RX-only integration COMPLETE / POSITIVE. User confirmed flashed and supplied 4643-line ~189s ESPHome log. Six sets of joined V5DCM19 diagnostics; raw versus portable parser parity B11D 1564/1564 and B11C 1566/1566, zero differences, no new observed errors; historical 11 resyncs and 1 integrity incident stable. HA readings healthy (Heating Curve 36). Executor 266/266 candidates denied with zero physical TX. No FC23 native challenge or DCM mailbox; owner/epoch/icon/acceptance unknown. Next experiment V5DCM20 passive; original V5DCM18 Python replay remains separately partial. G01–G06 accepted residual risks unchanged.

[Result](V5DCM/V5DCM19_FIX1_LIVE_RESULT_20261018.md).

---

# 2026-10-18 — V5DCM19 FIX1 prepared: duplicate interval fixed

V5DCM19 remains PREPARED / NOT RUN. Original candidate contained two top-level interval keys, invalidating its claimed 8/8 syntax validation. New FIX1 moves diagnostic into existing production interval list; strict duplicate-key parse PASS, 16 total periodic entries including new diagnostic. No ESPHome compile/flash or live result; deployed FIX1 parity still unverified. G01–G06 accepted risks not reopened. [Report](V5DCM/V5DCM19_FIX1_DUPLICATE_INTERVAL_20261018.md).

---

# 2026-10-18 — V5DCM19 PREPARED / NOT RUN (latest)

RX-only diagnostic candidate generated from archived V5DCM2 ZIP, not yet verified byte-equal to deployed FIX1. Logging-only change; three [V5DCM19] lines. 8/8 syntax/source checks; no ESPHome compile, flash or live test. TX HARD_DENY. V5DCM18 original full reference-Core replay remains PARTIAL. G01–G06 accepted risks unchanged. [Report](V5DCM/V5DCM19_PREPARED_RX_DIAGNOSTIC_20261018.md).

---

# 2026-10-18 — V5DCM18 functional V4.1→V5 gap handoff COMPLETE (scoped), roadmap experiment PARTIAL

**Current V5DCM18 RUNNING / PARTIAL** until original Python CM930 reference-Core fixture test / full stateful replay is actually executed; **functional gap inventory and V5DCM19 handoff COMPLETE / POSITIVE** from direct sources (prior chat Markdown, Write Beta V4.1 YAML/README, firmware evidence matrices and current V5 components). Priority gaps: existing V5 observer lacks proven *joined* session pipeline; separate firmware handshake state from owner/TX authorization; fixed guarded R1 V4.1 differs from original computed challenge response; cold-start 32 pages must not be imposed on retained/hot rejoin; mailbox, profile-dependent package completeness and runtime are separate. Historical V4.1 EXP386/387 positive, EXP388 partial. Existing 17/17 ZIP Core and seven-capture replay keep their narrower scopes. G01–G06 accepted residual risks NOT reopened. User production V5DCM2 FIX1 RX-only TX HARD_DENY unchanged. [Functional handoff](V5DCM/V5DCM18_FUNCTIONAL_GAP_HANDOFF_20261018.md).

---
# 2026-10-18 — V5DCM18 verified strict replay + 17/17 real ZIP-Core C++ tests (LATEST)

**Current original-roadmap V5DCM18: RUNNING / PARTIAL** (full original Python CM930/Core corpus-state parity unexecuted). **Verified directly today:** g++ -std=c++17 -Wall -Wextra -pedantic original user ZIP portable Core 17/17 PASS; strict offline seven-capture re-run: one Oct-03 32/32 bootstrap, Eco5 28/32 and 24/32, CRC-corrupt and missing 03FC/mid-session interruption reject false completion. Write V4.1 EXP386/387 locally positive and EXP388 partial must be preserved as independent native cold-start/retained/hot-rejoin baseline; NOT live rerun. **Remaining:** run original Python reference-Core tests against 7 fixtures; current repo HEAD C++ differs from ZIP provenance-enabled Core. **G01–G06 already accepted; do not reopen.** Production V5DCM2 FIX1 RX-only TX HARD_DENY unchanged. [Verified report](V5DCM/V5DCM18_VERIFIED_OFFLINE_RESULT_20261018.md).

---
# 2026-10-18 — V5DCM18 integrated existing observers: verified bounded offline replay (LATEST)

**Current experiment:** V5DCM18 RUNNING / PARTIAL (original roadmap). Deployed V5DCM2 FIX1 RX-only / TX HARD_DENY, unchanged. Already accepted G01–G06 residual-risk decisions must NOT be reopened without new evidence. Direct C++17 replay using user ZIP V5DCM1/V5DCM2 observer + portable parser over all seven historical logs, 25,031 CRC-valid frames, 164 exact FC23 request geometries, 7 reply-shaped events. A naïve counter produced **seven invalid full sessions** and was discarded. Corrected bounded profile/page/count/continuity replay: exactly one 32/32 Oct-03, Eco5 max 28/32 and 24/32, no full there. Missing page and mid-bootstrap interruption remove full series; duplicate challenge does not falsely create new series. Existing 17/17 ZIP C++ Core tests remain valid only for ZIP variant. **Still open:** actually execute Github Python original reference-Core corpus+stateful tests and reconcile ZIP with HEAD before full original-roadmap COMPLETE. [Report](V5DCM/V5DCM18_INTEGRATED_OBSERVER_REPLAY_20261018.md).

---
# 2026-10-17 — V5DCM18 offline CPP 7-capture replay completed (bounded); roadmap PARTIAL

**Deployed unchanged:** V5DCM2 FIX1 RX-only TX HARD_DENY. **G01–G06 accepted residual risks: DO NOT REOPEN absent genuinely new evidence.** Executed C++17 parser/owner-decision traversal on user-supplied ZIP Core and all seven captures: 25,031 frames, 2,500 slave-0x0F FC16 requests, 1,365 ACK shapes, 171 slave-0x0F FC23 records (164 challenge requests + 7 response shapes from separate earlier classifier). Owner decision probe without commit: 216 hypothetical authorized candidates, 2,284 denied; not physical TX authorization. ZIP core does not decode FC23—existing V5DCM2 observer handles it. **Status V5DCM18 RUNNING/PARTIAL:** original Python reference Core end-to-end fixture tests + integrated stateful fault replay remain unverified. No new bus TX or production changes. [Evidence](V5DCM/V5DCM18_CPP_CORPUS_BRIDGE_20261017.md).

---
# 2026-10-17 — V5DCM18 ZIP C++ extended suite 17/17 verified; ROADMAP PARTIAL

Original roadmap V5DCM18 remains **RUNNING / PARTIAL**. Actual host C++17 compile/run of supplied V5DCM2 ZIP Core: 17/17 stateful assertions pass (previous 11 plus epoch, cross-Core origin, mutated-frame, readiness/revoke/recovery tests). Original Python reference-Core corpus+fault execution and Github HEAD parity still unverified. ZIP Core provenance ticket APIs differ from canonical Thermia_Connect_Firmware/main. No ESPHome changes, no native TX, current V5DCM2 FIX1 RX-only/HARD_DENY preserved. [Report](V5DCM/V5DCM18_EXTENDED_CPP_17_PASS_20261017.md).

---
# 2026-10-17 — V5DCM18 CURRENT: RUNNING / PARTIAL (11/11 ZIP C++ stateful tests)

Original-roadmap V5DCM18: locally compiled user-supplied V5DCM2 ZIP portable C++ Core, 11/11 stateful checks passed (denial, one-shot ticket, revocation, full bootstrap, reset). But ZIP Core includes stamped tickets/provenance and **DIFFERS** from `Thermia_Connect_Firmware/main` portable Core; GitHub CI Python Core outcome and integrated corpus/stateful replay not independently verified. Therefore **NOT COMPLETE**. Existing 25,031-frame passive replay remains separate. Next reconcile source versions and run actual original Core fault tests before roadmap V5DCM19; current production V5DCM2 FIX1 RX-only HARD_DENY unchanged. [Evidence](V5DCM/V5DCM18_CPP_ZIP_SOURCE_DIVERGENCE_20261017.md).

---

# 2026-10-17 — V5DCM18 RUNNING / PARTIAL — corrected original firmware test assertions

Original-roadmap V5DCM18 stateful original-reference-Core replay remains open. Direct CM930-derived handshake may internally accept a qualifying FC16 before emulator owner qualification. The prior test incorrectly treated this as failure. Test assertion now checks internal acceptance WITHOUT corresponding unauthorized owner/TX; script also exits nonzero on failed checks. Source committed to firmware repo `tools/test_v5dcm18_roadmap_faults.py` (`1cec88606379d9aedb505017fcb49b8ba63fb13f`). CI/corpus execution results NOT VERIFIED. No live TX, YAML, or change to V5DCM2 FIX1 RX-only/HARD_DENY. [Report](V5DCM/V5DCM18_ROADMAP_CI_ASSERTION_FIX_20261017.md).

---

# 2026-10-17 — V5DCM18 ROADMAP RUNNING / PARTIAL; original Core CI verification pending

**Current:** V5DCM18, original-roadmap end-to-end offline replay. Capture-only structural replay 25,031 CRC valid, 164 challenge shapes, 7 pairs, 1 strict 32-page run, 49/49 limited observational checks remains valid. Added direct-original-Core offline error-injection script and GitHub Actions integration to Thermia_Connect_Firmware (source committed). GitHub workflow run logs/results NOT verified; **do not claim stateful tests passed or full V5DCM18 complete**. Original CM930 acceptance can occur before emulator owner decision, so distinguish internal H2 state from TX authorization. Next retrieve CI results, reconcile acceptance/owner gate, finish stateful replay. **Production V5DCM2 FIX1 RX-only/TX HARD_DENY unchanged.** [Source test progress](V5DCM/V5DCM18_STATEFUL_CORE_CI_PREPARED_20261017.md).

---

# 2026-10-17 — ROADMAP RECONCILIATION: V5DCM18 RUNNING / PARTIAL (latest)

**Roadmap authoritative:** V5DCM18 requires end-to-end offline replay and fault scenarios, NOT only source/API audit. Previous V5DCM18 source audit is retained separately. **Current:** capture-only replay completed, 25,031 CRC-valid historical frames, 164 FC23 request shapes, 7 paired reply shapes, 1 full strict 32-page sequence; 49/49 limited structural fixtures passed. Original CM930/Core stateful error-injection validation is NOT RUN; full V5DCM18 success criterion NOT MET. **Next:** run existing original reference-Core tests and adverse transitions, then V5DCM19 RX-only YAML integration and V5DCM20 passive XTR validation per roadmap. **Production unchanged:** V5DCM2 FIX1 RX-only, native TX HARD_DENY. [Roadmap partial report](V5DCM/V5DCM18_ROADMAP_REPLAY_PARTIAL_20261017.md).

---

# 2026-10-17 — V5DCM19 isolated observe/authorize/commit contract (latest)

**Deployed live:** V5DCM2 FIX1 RX-only, native TX HARD_DENY, HA unchanged. **Last completed experiment:** V5DCM19 COMPLETE / POSITIVE for 15/15 standalone synthetic Python tests of a fail-closed observation → authorization → commit contract; COMPLETE / INCONCLUSIVE for compiled C++ parity, local XTR accepted session, physical owner/slot, icon and Online. Controlled offline test-only Python model; no native response implementation, original V5 C++ edits, ESPHome YAML, flash or live TX. Denied FC16 shape with absent source/epoch/session evidence does not promote the model handshake; isolated mailbox and full Connect-readiness gates are explicit. The V5DCM18 C++ classification-side-effect is *not fixed* by this Python experiment. **Next:** V5DCM20 PREPARED / NOT RUN — isolated C++ source/API refactor and negative regression tests with original Core call-site audit; never allow live TX before independently qualified physical provenance and separate approval. Positive C++ negative fixtures and preserved runtime paths, negative API/call-site failure, abort any unsafe TX/private code, recovery revert isolated patch. [Report](V5DCM/V5DCM19_OBSERVE_AUTHORIZE_COMMIT_OFFLINE_20261017.md).

---

# 2026-10-17 — V5DCM18 source/API parity audit completed (latest)

**Deployed:** V5DCM2 FIX1 RX-only, native TX HARD_DENY, HA unchanged. **Last completed:** V5DCM18 COMPLETE / POSITIVE for bounded source-level V5 Core versus original CM930 firmware-derived lifecycle audit; COMPLETE / INCONCLUSIVE for real local XTR approval/Online/physical ownership. Inspected portable xtr_core.cpp/.hpp, adapter, frame pipeline, platform and original CM930 source-derived state tables. Notable implementation discrepancy: Core::fc16_decision mutates ResponseSent→Accepted before owner authorization; explicit qualify_handshake and set_mailbox public APIs have no built-in provenance token; write_ready does not itself prove firmware profile, package completion or bus ownership. Offline source observation only, NOT a proven defect in user-flashed FIX1, and no actual transmit. **Next:** V5DCM19 PREPARED / NOT RUN, offline pure observation-versus-authorized-transition contract/test; positive denied frames never promote acceptance, negative missing evidence guards, abort any unsafe TX/private payload, rollback discard offline tests. [Report](V5DCM/V5DCM18_SOURCE_API_PARITY_20261017.md).

---

# 2026-10-17 — V5DCM17 completed offline lifecycle-gate reconciliation (latest)

**Deployed baseline:** V5DCM2 FIX1 RX-only; native TX=HARD_DENY; production HA unchanged. **Last completed:** V5DCM17 COMPLETE / POSITIVE for bounded firmware source/readiness reconciliation (9/9 applicable static checks), COMPLETE / INCONCLUSIVE for real local XTR approval, sender/epoch/profile, exclusive response slot, display icon and cloud Online. Previous GAP51–53 frame observer and V4.1/V5 comparison do not resolve independent acceptance or physical ownership. Oct-03 candidate FC23 shape + 32 reference starts is compatible with native firmware *ordering*, not proof of semantic acceptance. The 43 flag ranges are not a universal required set. **Next:** V5DCM18 PREPARED / NOT RUN, offline source/API transition-parity audit between genuine CM930 firmware, V5 Core, and historical V4.1; no new observer, YAML, hardware or TX. Positive verified missing implementation interface, negative no actionable parity gap, abort unsourced slot/epoch or protected code exposure, recovery unchanged FIX1.

[Detailed V5DCM17 result](V5DCM/V5DCM17_LIFECYCLE_GATES_OFFLINE_20261017.md).

---

# 2026-10-17 — V5DCM16 completed offline historical session replay (latest)

**Deployed live baseline:** V5DCM2 FIX1, RX-only, working HA production; native TX=HARD_DENY. No new ESPHome YAML/build/flash or live test in V5DCM16.

**Last completed:** V5DCM16 COMPLETE / POSITIVE for bounded CRC-valid seven-capture replay, challenge/reply-shape correlation and strict config reference sequence, 14 offline assertions PASS; COMPLETE / INCONCLUSIVE for actual XTR DCM approval, controller icon/cloud Online and sender/epoch/slot. 25,031/25,031 original text-record CRC-valid, 164 exact FC23 native 0x0F challenge shapes, 7 temporally paired shaped replies within 200 ms, 157 unpaired *within these records*. Oct-03 27.400s challenge → 27.429s reply-shaped (29ms) → first configuration 29.262s (1.833s later) → 32 consecutive reference page starts through 61.461s (32.199s). Eco5 Sep26 99/2 challenge/pair; Eco5 Sep28 64/4; no strict 32-page runs in Eco5 (heuristic only). Profile remains UNKNOWN despite common original 43-bit flag map verified V5DCM15A. No proven sender, physical wire EOF, response slot, epoch, native accepted, icon or Online.

**Next:** V5DCM17 PREPARED / NOT RUN: offline reconcile candidate lifecycle with original CM930 firmware state gates and existing GAP51–53 evidence, avoiding redundant work. Baseline V5DCM16, change passive offline replay/classification only; positive justified state witnesses, negative count/parity discrepancy; abort any unsourced owner/acceptance/TX claim; recovery retain unchanged V5DCM2 FIX1. Never infer genuine DCM device availability.

[Full V5DCM16 report](V5DCM/V5DCM16_HISTORICAL_SESSION_REPLAY_20261017.md).

---

# 2026-10-17 V5DCM15A — RAUC 2.1.105 original config complete

**V5DCM15A:** COMPLETE / POSITIVE (16/16 offline extraction and equality checks), INCONCLUSIVE for actual XTR profile and DCM acceptance. Extracted original RAUC 2.1.105 appfs `/etc/device-client.d/930/modbus-flags.json`: 3333 bytes and SHA256 bb0b335eaf4e3a98e5d71d1cd1551e0772fedcfcd3f7d17f3c78e04c21844b9e, exact byte match with original Connect 2.0.18 flags JSON. Request ranges 0x070A:16; 0x070B:16; 0x070C:11. The V5DCM13 2.1.105 original-JSON gap is closed. CM930 config profiles differ: 33 old and 35 new JSON; 25 shared paths, 17 changed, 8 unchanged; 2.3.0–2.4.1 extended to 2.3.0–2.4.3. Original app selects version-specific profile using observed CM firmware version; local XTR selected profile unknown. Do not equate 43 available ranges with 43 required subscriptions or accepted Online.

**Live:** V5DCM2 FIX1 RX-only/HARD_DENY unchanged, no new flash or TX.

**Next:** V5DCM16 PREPARED / NOT RUN, historical FC23/session replay only, conservatively preserve sender/epoch/profile UNKNOWN; no active TX.

[Report](V5DCM/V5DCM15A_RAUC_21105_CONFIG_AUDIT_20261017.md).

---

# 2026-10-17 — V5DCM13–15 consecutive offline audit (latest)

**Production:** user-tested V5DCM2 FIX1 RX-only/HARD_DENY; no new ESPHome firmware, TX or controller actions.

**Latest:** V5DCM13 COMPLETE/POSITIVE strictly for original 2.0.18 flags JSON: 43/43 request spans exactly match derived V5DCM12 map (0x070A=16, 070B=16, 070C=11). 2.1.105 original appfs config remains RUNNING/PARTIAL/INCONCLUSIVE (not extracted here). V5DCM14 COMPLETE/POSITIVE for firmware-source subscription-based package selection path; INCONCLUSIVE actual XTR selected mask. V5DCM15 COMPLETE/POSITIVE for 18/18 offline synthetic assertions of fail-closed witness bookkeeping; INCONCLUSIVE vendor-runtime parity, native XTR acceptance, Online and display. Verified RAUC 2.1.105 Python source used; selected profile unresolved. Live TX remains HARD_DENY.

**Strongest conclusion:** 43 bits describe available flag ranges, not a universal required data set. An observed FC16 frame is not the firmware receive callback; an FC23-shaped event is not vendor acceptance. Required bitset, received bitset, session owner/epoch, controller icon and cloud status must be treated independently.

**Next:** V5DCM16 PREPARED/NOT RUN: offline historical session timing/provenance replay with explicit UNKNOWN sender/wire EOF. In parallel unresolved narrow V5DCM13 follow-up: independently read new RAUC 2.1.105 original config JSON; do not assume unchanged flags map. Positive genuine evidence-backed classification, negative failed parity, abort overclaim/secrets/TX; recovery none, retain FIX1.

[Reports: V5DCM13](V5DCM/V5DCM13_ORIGINAL_FLAGS_AUDIT_20261017.md) · [14](V5DCM/V5DCM14_REQUIRED_PACKAGE_SELECTION_AUDIT_20261017.md) · [15](V5DCM/V5DCM15_FAIL_CLOSED_SESSION_MODEL_20261017.md).

---

# 2026-10-17 — V5DCM12 offline request-package mapping (latest)

**Live production baseline:** user-tested V5DCM2 FIX1, RX-only; no hardware modifications or ESPHome flash during V5DCM3–12.

**Last completed:** V5DCM12 COMPLETE / POSITIVE for offline 14/14 source-map and historical event replay assertions; COMPLETE / INCONCLUSIVE for firmware-recognized package receipt/accepted XTR DCM/Online. Connect 2.1.105 original Python source selects request words 0x070A, 0x070B, 0x070C via profile-configured flags JSON; the existing firmware repo's derived flags map describes 16+16+11 address/bit candidate ranges. Seven existing historical/collaborator files (3,063 normalized native event rows) match 10–43 unique bits each (Oct-03 43/43, Eco5 Sep-26 43/43, Eco5 Sep-28 42/43). These are request-SHAPED observations and cannot be treated as application callbacks, owner/epoch confirmation, approval or Online. Original flags JSON/profile selection not independently reverified in this experiment.

**Current model:** handshake, source/epoch, received selected packages, publication-readiness, display and cloud connection are independent. Highest unknown: selected XTR profile and ability to associate actual original firmware receive events to same-session captures.

**Next:** V5DCM13 PREPARED / NOT RUN, offline direct original RAUC appfs flags JSON profile provenance and comparison to repository map. Positive exact JSON/range match and justified profile selection; negative missing/mismatch; abort protected material leak or hardware TX; recovery none, retain RX-only FIX1.

[Evidence](V5DCM/V5DCM12_REQUEST_PACKAGE_MAP_OFFLINE_20261017.md).

---

# 2026-10-17 — V5DCM11 offline firmware readiness audit (latest)

**Deployed live baseline:** user-tested V5DCM2 FIX1, RX-only with stable production HA telemetry; physical TX HARD_DENY. No firmware built/flashed from V5DCM3–11.

**Last completed:** V5DCM11 — COMPLETE / POSITIVE for direct RAUC-proven firmware source AST examination and 10/10 synthetic fail-closed guard tests; COMPLETE / INCONCLUSIVE for native XTR acceptance and vendor-runtime parity. Verified RAUC 2.1.105 embedded device_client 0.2.8 adds `CMClientParameterUpdateState` INITIAL / WAIT_FOR_ALL_DATA_PACKAGE / ALL_DATA_PACKAGE_RECEIVED, seeding from needed subscription package bits after version-aware config load, clearing on register package receipt, and delaying parameter-map publication until ALL received. RAUC 2.0.18 embedded app 0.1.45 has no equivalent specific class/gate in compared code. Both have separate FC23 reply vs FC16-driven software handshake state. This is firmware-derived, NOT XTR bus handshake or DCM icon proof. A zero-package wait is not auto-complete in original newer class.

**Strongest interpretation:** handshake status, application runtime, data-package readiness, cloud publication and display Online must be separate evidence axes. Current XTR owner/epoch, actual response slot and native accepted state remain unknown.

**Next:** V5DCM12 PREPARED / NOT RUN: offline source-table package-bit mapping and historical capture replay with fail-closed UNKNOWN on missing mapping; baseline V5DCM8–11 and live FIX1, controlled change offline only. Positive source-derived package identity without false acceptance; negative incomplete mapping or counters; abort unpublished secrets or physical TX; recovery none, FIX1 remains.

[Detailed V5DCM11](V5DCM/V5DCM11_CM930_READINESS_OFFLINE_20261017.md).

---

# 2026-10-17 — V5DCM10 RAUC provenance verified (current)

**Current live baseline:** V5DCM2 FIX1, native 0x0F TX=HARD_DENY; production Home Assistant data continued in last user-supplied run. No new ESPHome firmware compiled or flashed by V5DCM3–10.

**Last completed offline experiment:** V5DCM10 — COMPLETE / POSITIVE for direct RAUC content provenance and source identity. Original `Thermia_Connect-2.0.18-s1.raucb` contains manifest version 2.0.18 and appfs `device_client 0.1.45`, 21/21 extracted Python modules byte-identical to `appfs_2018.zip`. Original `Thermia_Connect-2.1.105-s1.raucb` contains manifest version 2.1.105 and appfs `device_client 0.2.8`, 25/25 modules identical to `device_client.zip`. Both RAUC bundles directly read as SquashFS, manifest/appfs/rootfs extracted; 4/4 SHA256 and image-size checks match embedded manifests. V5DCM9's unverified source-to-RAUC mapping is now **RESOLVED**. Cryptographic RAUC signature CA chain has NOT been validated.

**Protocol/evidence scope:** version-scoped CM930 application source differences (21 shared modules; 16 changed; 4 added) may guide session and parameter-readiness modeling but are NOT proof of XTR native acceptance, DCM icon, cloud Online, physical owner or response slot. Never infer changed native cryptographic handshake output solely from file diffs.

**Next experiment:** V5DCM11 — PREPARED / NOT RUN: offline version-scoped CM930 application state/packet-readiness witness mapping from authenticated provenance chain; baseline V5DCM9/10; controlled change offline AST/code-evidence mapping only. Positive: source-backed differences and reproducible fixture criteria; negative: unsupported state/display inferences; abort private source publication or physical TX; recovery no hardware changes, retain FIX1.

**GitHub:** user authorized updates per experiment, excluding working private 0x0F authentication/security logic and command-mailbox tooling. Full sanitized details: [V5DCM10](V5DCM/V5DCM10_RAUC_PROVENANCE_VERIFIED_20261017.md).

---

# 2026-10-17 — V5DCM9 offline firmware-source comparison (latest)

**Current live baseline:** user-flashed V5DCM2 FIX1 RX-only, HA production preserved, native TX HARD_DENY; no later firmware flashed.

**Last completed:** V5DCM9 COMPLETE / POSITIVE (static comparison of original recovered device_client source snapshots 0.1.45 and 0.2.8, 21 vs 25 Python files, 16 changed shared modules, 4 new modules; AST checks PASS). COMPLETE / INCONCLUSIVE for independent one-to-one mapping of source archives to RAUC 2.0.18 vs 2.1.105, which has NOT been verified here; never conflate Python package and RAUC release numbers. CM930 packet-readiness, conditional request selection and service-level publication differ; these are firmware-derived and NOT XTR local bus/display proof. Native FC23 cryptographic/response changes not established.

**Next:** V5DCM10 PREPARED / NOT RUN — offline establish verifiable RAUC image→application package provenance, and separate wire-observable state differences. Baseline V5DCM9; no hardware TX. Positive verified chain of custody/hashes, negative missing/ambiguous extraction, abort private disclosure or production changes, recovery no action as offline.

[Detailed report](V5DCM/V5DCM9_FIRMWARE_VERSION_AUDIT_20261017.md).

---

# 2026-10-17 — V5DCM8 offline provenance model completed

**Live baseline unchanged:** V5DCM2 FIX1, RX-only with functioning HA production entities, software TX HARD_DENY.

**Last completed:** V5DCM8 COMPLETE / POSITIVE for offline passive replay of seven historical/collaborator CRC-validated text capture files, 164 native FC23 exact challenge shapes, 7 time-correlated reply shapes <=200ms, one strict 32-reference-page run. A fail-closed model never upgrades those observations to owner, epoch, native acceptance, DCM icon, cloud Online or TX permission. COMPLETE / INCONCLUSIVE for actual XTR-native session/Online. No new YAML compiled or flashed.

**Protocol position:** V5DCM4–8 confirm the need to separate frame shape, time correlation, provenance, software acceptance, controller display and cloud status. Existing CM930 firmware semantics remain firmware-derived, not observed locally as XTR acceptance.

**Next:** V5DCM9 PREPARED / NOT RUN, offline firmware-version comparison of original Connect 2.0.18 and 2.1.105 session lifecycle and application state. Positive verifiable version differences; negative equivalent code/no new evidence; abort confidential security publication or any live TX; recovery leave FIX1 unchanged.

[V5DCM8 evidence](V5DCM/V5DCM8_PROVENANCE_OFFLINE_20261017.md).

---

# 2026-10-17 — V5DCM4–7 offline genuine/collaborator capture audit (latest)

**Current live deployment:** user-tested V5DCM2 FIX1, RX-only; parser healthy, TX=HARD_DENY, no observed local native 0x0F FC23 during last live sample. No additional firmware flashed.

**Latest completed offline experiments:** V5DCM4 real-record replay (25,031/25,031 text-record CRC correct, 7/7 normalized V5DCM3 counter parity), V5DCM5 historical FC23 timing (Oct-03 29ms request/reply-shaped pair; Eco5 99+64 requests and 2+4 response-shaped matches; no sender or slot proven), V5DCM6 strict 32-reference-run comparison (Oct-03 32 ordered, Sep-25 09:05 31 captured, Eco5 profile count differences), V5DCM7 false-positive guards (0708 mailbox request seen without FC23 in the same capture window; permissive aggregate 32-page cursor can overclaim one epoch). All COMPLETE/POSITIVE for narrow offline evidence, INCONCLUSIVE for live XTR authentication/Online. No active writes, YAML changes, or compile.

**Protocol model:** Separate frame-shape and timing observations, correlated candidate, single-epoch source-qualified session, vendor acceptance, DCM icon and cloud Online state. A text capture containing a reply shape does not establish sender or physical slot; a mailbox poll or completed reference cursor does not establish acceptance. Firmware-derived semantics remain marked as such.

**Next:** V5DCM8 PREPARED / NOT RUN: build and test a provenance-aware offline model with explicit UNKNOWN flags. Baseline V5DCM4–7 and live FIX1; controlled change offline-only model. Positive no false acceptance and matching observation counts; negative mismatch/overclaim; abort on secret disclosure or physical TX; recovery discard offline model and retain V5DCM2 FIX1.

[Detailed evidence](V5DCM/V5DCM4_TO_7_OFFLINE_REPLAY_20261017.md).

---

# 2026-10-17 — V5DCM3 offline completed (current)

**Current live baseline:** V5DCM2 FIX1 RX-only, live-positive diagnostic and preserved HA telemetry; native FC23 and mailbox not observed; TX=HARD_DENY.

**Last completed:** V5DCM3 COMPLETE / POSITIVE for 5/5 synthetic offline C++ host fixtures; COMPLETE / INCONCLUSIVE for genuine-capture replay and local XTR handshake/Online. No YAML flashed/changed. Separate handshake, reference config order, mailbox direction and runtime witnesses. Source: original Connect firmware, firmware-derived semantics NOT locally confirmed.

**Next:** V5DCM4 PREPARED / NOT RUN: replay existing genuine captures offline against model, no TX. Abort on contradictory provenance, unsafe inference or any hardware operation. Recovery: preserve tested V5DCM2 FIX1.

Details: [V5DCM3](V5DCM/V5DCM3_OFFLINE_SESSION_AUDIT_20261017.md).

---

# 2026-10-17 — V5DCM rebuild: current experiment V5DCM2 PREPARED / NOT RUN

**Current installed/reported:** V5DCM1 passive CM930 observer (user explicitly confirmed it was flashed); RUNNING / PARTIAL. RX-only XTR monitoring, preserved production HA data, zero reported parser faults and software TX. The new internal observer has no individually visible diagnostics, so its state transitions are not independently demonstrated. Logs: Pasted text(20261017-004017).txt, Pasted text(20261017-004733).txt, Pasted text(20261017-004803).txt. No fresh native 0x0F FC23 or 0708 in these windows.

**Last locally tested:** V5DCM1 partial positive for preserved RX-only functionality; no DCM acceptance evidence. **Current prepared:** V5DCM2 RX-only challenge correlation and 30-second [V5DCM2] diagnostics, NOT FLASHED/NOT RUN according to current evidence. Its private-provider interface does NOT contain the actual firmware-derived cryptographic responder.

**Protocol model:** Native Connect CM930 as Modbus slave 0x0F. FC23 approval response is challenge-dependent according to recovered Thermia Connect 2.0.18/2.1.105 firmware; software states NOT_ACCEPTED -> RESPONSE_SENT -> ACCEPTED are distinct from controller recognition, config completeness, runtime/mailbox, cloud connectivity, and display indications. Historical V4.1 fixed response/replay and ordered configuration ACKs only partly match firmware implementation. Known local passive FC16 03E8/14 and 085F/5 do not prove fresh session ownership.

**Highest-priority goal:** firmware-faithful V5 DCM session, DCM icon then online status *as separately observed outcomes*. Do not claim icon/online mapping proved. Preserve GAP-51E RX-only baseline and rollback. TX=HARD_DENY until separately approved and bounded. Controller epoch, bus slot, wire EOF and physical DE remain unproven.

**Next action:** install and collect compact [V5DCM2] and S8-health diagnostics; classify result before advancing. Subsequent implementation must include real dynamic handshake computation in a private environment, tested against genuine captures, not just an interface.

**GitHub policy:** user authorized updating GitHub with each experiment from 2026-10-17. Keep Research canonical files reconciled, preserve historical sections, and exclude confidential 0x0F responder/security/key and mailbox command tooling. Detail: [V5DCM handover](V5DCM/V5DCM1_V5DCM2_HANDOVER_20261017.md).

---

# 2026-10-16 — GAP-46C live reconciliation (current project status)

**Current deployed/observed baseline:** User-installed GAP-46C exact-frame shadow ESPHome candidate on XTR M, built after live GAP-46B. Native V5 TX remains **HARD_DENY / NO TX**; production Home Assistant telemetry continued in the supplied log. Software counters show no UART writes, no TX attempts, no DE activation; physical DE line not independently measured. This section supersedes older “current” labels below, without changing their historical observations.

**Last completed experiment:** **GAP-46C — COMPLETE / POSITIVE** for manual arm, automatic 15 s timeout and NO-TX snapshot in an ordinary unqualified session. **COMPLETE / INCONCLUSIVE** for qualified FC23 challenge recognition and active native response (no qualifying native challenge occurred). User log: `Pasted text(20261016-184950).txt`, ~20:48–20:49: arm 20:49:07.926, expiry 20:49:24.887, snapshot 20:49:37.733; snapshot `exact=0 eligible=0 refused=0 reservedState=0 TX=HARD_DENY`. No native FC23 for 0x0F. GAP-46B preceding live test confirmed manual revoke after expiry and the fail-closed RX-only transaction boundary; it did **not** exercise revocation of a live reserved transaction. GAP-45B/45C confirmed arm and timeout under unqualified traffic.

**Protocol model:** XTR M on present RX-only run repeatedly exposes native `0x0F` FC16 `03E8/count14` and `085F/count5`, not an accepted Online/DCM startup. Historical V4.1 contains a guarded single-shot FC23 `071C/0730` response followed by ordered configuration/runtime exchanges (historically positive under its exact test conditions). This must not be equated with a locally qualified V5 session or generic permission to transmit.

**Locally proven (scope-limited):** V5 parser/CRC and production sensor continuity in supplied GAP-46B/C captures; stable RX/no resync or drops in the evaluated samples; arm, timeout, revoke (after expiry), NO-TX snapshot. No physical DE verification. Firmware-derived acceptance transitions remain distinct from proof of actual XTR bus acceptance.

**Strong hypotheses:** Frame-bound V4.1 challenge logic may be reusable after a verified fresh cold session, verified exact matching frame and safe response slot. Offline model and documentary replay do not prove slot timing or semantic acceptance.

**Important unknowns:** Fresh 0x0F FC23 challenge within an armed window; controller epoch/owner; wire-end and response-slot ownership; qualified event-route success; native V5 TX and subsequent readback; active recovery/rejoin. Existing `STAGE_D_LEDGER_FAULT` in retained traffic is not a newly demonstrated parser failure.

**Next experiment:** **GAP-46D — PREPARED / NOT RUN (proposal only)**: offline timing/event-chain comparison of existing genuine captures and V4.1 code, no physical TX. Baseline GAP-46C no-TX positive; controlled change is offline replay/correlation only. Positive criterion: uniquely linked exact challenge and bounded response-slot evidence in existing raw capture; negative: missing/ambiguous direction/epoch/timing; abort: unverifiable provenance or need for unsolicited live TX. Recovery none (offline). Do not require a genuine DCM or controller restart. Do not enable active TX without a separately described authorized test and rollback to known-good GAP-36 RX-only.

**GitHub confidentiality:** No private 0x0F response bytes, mailbox payload/tooling, keys, or recovered security methods in this update.

---

# 2026-10-16 — GAP-25E/F and GAP-26–32 reconciliation (newest evidence)

**Current deployed/observed baseline:** User-reported GAP-25E RX-only ESPHome/HA integration, preserving working production sensors; native 0x0F TX HARD_DENY and software TX attempts 0 in the supplied logs. Native XTR M traffic remained FC16 `03E8/count14` and `085F/count5`; no local native FC23 or extended candidate pages in the reported captures. Compressor current/frequency and outdoor-fan speed being Unknown while the outdoor unit is off is **expected behaviour per user confirmation**. The 30 visible GAP25D raw candidates are Unknown; HA also lists 19 disabled entities of **unverified identity**, not assumed to be GAP25D. YAML `disabled_by_default` does not retroactively disable HA-registered entities.

**Most recent intervention:** GAP-25F Eco → Comfort water mode change by the user; corresponding capture showed no new native page family and no RX parser errors or software native TX. **COMPLETE / NEGATIVE** narrowly for appearance of new native page types during that capture; **COMPLETE / INCONCLUSIVE** for byte-level change inside existing `03E8` page (no timestamped pre/post payload comparison). Do not extrapolate to all controller states. Eco restoration was recommended, **not confirmed**.

**Last completed experiment:** GAP-32 — **COMPLETE / POSITIVE (offline firmware observability audit); INCONCLUSIVE (actual XTR session acceptance/trigger)**. GAP-26–32 were offline-only and did not change the installed YAML, wiring, HA or native TX policy. Full local reports: `GAP26_OFFLINE_REPORT.md`, `GAP27_OFFLINE_REPORT.md`, `GAP28_RESULT.md` through `GAP32_RESULT.md` (analysis artifacts, not necessarily present in this repository). Do not mark these as deployed/live tests.

**Protocol model and evidence:** Original Connect 2.0.18/2.1.105 RAUC appfs contents were extracted and compared; 2.1.105 firmware has distinct NOT_ACCEPTED → RESPONSE_SENT → ACCEPTED state logic and conditionally requests further information/operation packages. Firmware-derived; **not locally proven bus semantics**. Seven historical captures contain 4,809 CRC-valid recognized native `0x0F` records; extended FC16 pages occur both in recordings with FC23 and in recordings without FC23 (possibly started mid-session). October 3 historical FC23 request/response-shaped frames precede `03E8/count13` and extended configuration pages, but direction/owner/epoch/acceptance not proven. Do not equate historical `03E8/count13` with locally observed XTR `03E8/count14`. Capture provenance must remain qualified, including Eco5 cross-model evidence.

**Strongest hypothesis:** Expanded Online/DCM pages may depend on qualified session state and firmware-initiated package requests; exact XTR prerequisite unknown. **Unknowns:** sender/direction, controller epoch, true first handshake, firmware ACCEPTED witness, physical EOF/response slot, page trigger, and active TX safety. No native write or handshake is authorized or warranted by these offline findings.

**Recommended next step:** Refrain from replaying the same partial capture chronology or adding 76 more HA sensors. Seek genuinely independent existing firmware/capture provenance or a bounded new passive witness with a discriminator; otherwise document the evidence ceiling. Preserve production, RX-only and HARD_DENY. Reconcile canonical files again after material new evidence.

---

# 2026-10-16 — GAP-23E through GAP-24I offline/live handoff

**Scope:** additive summary; earlier experiment records remain historical. Full account: [GAP23_GAP24_HANDOFF_20261016.md](GAP23_GAP24_HANDOFF_20261016.md).

- **Current user-confirmed device:** GAP-23E RX-only, HA production preserved, native `0x0F` TX HARD_DENY. Live observed `03E8/count14` = 69 and `085F/count5` = 34 in sample; HA Heating Curve=36; no software UART writes/TX, but no authenticated native session/owner/epoch.
- **GAP-23F/G/H:** offline contextual/fingerprint/source audits. Eco5 byte-identical page repetition is **cross-model only**; locally observed XTR repeats have no full byte-fingerprint trace. GAP-23H **COMPLETE/NEGATIVE for obtaining verifiable local frame pairs**, not negative protocol evidence.
- **GAP-24A/B/C:** COMPLETE/POSITIVE in bounded offline fail-closed candidate classification, evidence adapter and RX projection; live V4.1 session parity remains INCONCLUSIVE.
- **GAP-24D:** COMPLETE/POSITIVE limited negative host regression; **INCONCLUSIVE** for exact EXP355/386 positive raw frame replay (source completeness/provenance not established).
- **GAP-24F:** COMPLETE/POSITIVE ten-stage offline parity map and passive projection; full active native parity INCONCLUSIVE.
- **GAP-24G/H/I:** COMPLETE/POSITIVE offline lifecycle observational guard, synthetic 32-page shape ledger and nine-source-gap inventory. `67,613/67,613` synthetic C++ assertions pass; shapes never imply semantic acceptance or TX permit. The fixture pages are artificial, not bus evidence.
- **G01–G06 research-risk decisions:** G01 accepted bounded intervention-anchored restart risk; G02 **COMPLETE/POSITIVE CONDITIONAL** only on unchanged installed topology; G03 EOF unknown/accepted research risk; G04 exclusive slot unknown/accepted research risk; G05 hardware DE/FIFO PARTIAL/HOST-ONLY, residual research risk accepted; G06 reset/brownout DE-low unproved/accepted research risk. Acceptance is distinct from technical proof and from permission to send.
- **Unchanged history:** EXP388 RUNNING/PARTIAL; EXP425 NEGATIVE; GAP-18 DEFERRED/NOT RUN; GAP-19 STOPPED/PARTIAL. Do not merge their epochs.
- **Next:** bounded actual portable Core lifecycle-method source equivalence versus V4.1 branch decisions (not another generic observer); offline only, no live TX, no new DCM hardware assumption. No ESPHome compile or deployed GAP-24 firmware claimed.

---

## Current reconciled state

- **Current user-confirmed device:** GAP-23E RX-only, HA production preserved, native `0x0F` TX HARD_DENY. Live observed `03E8/count14` = 69 and `085F/count5` = 34 in sample; HA Heating Curve=36; no software UART writes/TX, but no authenticated native session/owner/epoch.
- **GAP-23F/G/H:** offline contextual/fingerprint/source audits. Eco5 byte-identical page repetition is **cross-model only**; locally observed XTR repeats have no full byte-fingerprint trace. GAP-23H **COMPLETE/NEGATIVE for obtaining verifiable local frame pairs**, not negative protocol evidence.
- **GAP-24A/B/C:** COMPLETE/POSITIVE in bounded offline fail-closed candidate classification, evidence adapter and RX projection; live V4.1 session parity remains INCONCLUSIVE.
- **GAP-24D:** COMPLETE/POSITIVE limited negative host regression; **INCONCLUSIVE** for exact EXP355/386 positive raw frame replay (source completeness/provenance not established).
- **GAP-24F:** COMPLETE/POSITIVE ten-stage offline parity map and passive projection; full active native parity INCONCLUSIVE.
- **GAP-24G/H/I:** COMPLETE/POSITIVE offline lifecycle observational guard, synthetic 32-page shape ledger and nine-source-gap inventory. `67,613/67,613` synthetic C++ assertions pass; shapes never imply semantic acceptance or TX permit. The fixture pages are artificial, not bus evidence.
- **G01–G06 research-risk decisions:** G01 accepted bounded intervention-anchored restart risk; G02 **COMPLETE/POSITIVE CONDITIONAL** only on unchanged installed topology; G03 EOF unknown/accepted research risk; G04 exclusive slot unknown/accepted research risk; G05 hardware DE/FIFO PARTIAL/HOST-ONLY, residual research risk accepted; G06 reset/brownout DE-low unproved/accepted research risk. Acceptance is distinct from technical proof and from permission to send.
- **Unchanged history:** EXP388 RUNNING/PARTIAL; EXP425 NEGATIVE; GAP-18 DEFERRED/NOT RUN; GAP-19 STOPPED/PARTIAL. Do not merge their epochs.
- **Next:** bounded actual portable Core lifecycle-method source equivalence versus V4.1 branch decisions (not another generic observer); offline only, no live TX, no new DCM hardware assumption. No ESPHome compile or deployed GAP-24 firmware claimed.


---

# 2026-10-15 — GAP-11..17 reconciled; GAP-18 DEFERRED; GAP-19 STOPPED

> Newest additive project status; detailed per-experiment record: [GAP-11–19 reconciliation](V41V5_GAP11_TO_19_STATUS_RECONCILIATION_20261015.md). Earlier GAP-11 PREPARED / NOT RUN text below is historical/superseded. Prior observations and negative results are preserved unmodified.

**Latest completed experiment:** **V41V5-GAP-17 COMPLETE / POSITIVE** for offline provenance audit and 47/47 controlled checks; **COMPLETE / NEGATIVE** for assuming repeated framebytes establish a clock link; **OVERALL COMPLETE / INCONCLUSIVE** for G03 physical EOF→ESPHome callback latency and G04 physical response slot. GAP-16 complete 25,031/25,031 CRC-good seven-capture source audit and 35/35 checks, but native TX readiness inconclusive.

**Current:** no running experiment. **GAP-18 DEFERRED / NOT RUN** by user (GPIO18 physically inaccessible; no physical synchronization recording). **GAP-19 STOPPED BY USER / PARTIAL**, no final result accepted; do not revive or call complete based on working drafts. User requested this documentation update after stopping.

**Offline software:** GAP-11 host revocation patch 326/326; GAP-12 adapter revocation 79/79 (full earlier stale-decision model was negative); GAP-13 Decision provenance 361/361; GAP-14 synchronous staged-snapshot 175/175; GAP-15 single-event-loop deferred lease/API guard 188/188; later regression matrix historical 541/541 with explicit updated obsolete expectations. These are **isolated host candidates**, not flashed into ESPHome; no new active native reply permission.

**Running device:** user-confirmed **GAP-08 RX-only** installed; GAP-09 live passive parity observed, TX attempts 0, `HARD_DENY`. All GAP-11..19 work was offline/planning, with GAP-19 interrupted. Production YAML, live ESPHome core and HA entities untouched.

**Protocol safety:** native Online/DCM still primary target; controller-driven slave `0x0F` model is firmware-derived and supported by distinct captured cases. XTR vs genuine cross-model captures remain separated. G01 independent current controller epoch OPEN; G02 installation owner CONDITIONAL; G03 physical wire EOF OPEN; G04 exclusive slot OPEN; G05 DE/FIFO electrical behavior PARTIAL/HOST-ONLY; G06 reset/brownout fail-low OPEN. No local genuine DCM. **NATIVE TX HARD DENY.**

**Next:** no automatic experiment. Await user request; do not suggest probing inaccessible GPIO18 or require genuine DCM hardware. If later authorized, prefer existing offline evidence and a separate feasibility review.

---

# 2026-10-15 — V41V5-GAP-10 latest; GAP-11 PREPARED / NOT RUN

> Newest additive canonical state. [GAP-08B–10 detailed audit](V41V5_GAP08B_TO_10_AUDIT_20261015.md). Earlier GAP-08B PREPARED overlay below is historical and superseded, not the current experiment. Preserve older entries intact.

**Current experiment:** GAP-10 **COMPLETE / NEGATIVE (offline revocation-policy invariant)**; 23/23 host checks executed, including intentionally demonstrated stale authorization upon toggle restoration. **Last completed live test:** GAP-09 **COMPLETE / POSITIVE in bounded RX-only parity/TX-deny scope**, with lifecycle-transition verification **COMPLETE / INCONCLUSIVE** and complete HA-production inventory check still open. GAP-08B **COMPLETE / POSITIVE**, user-confirmed full ESPHome compile (build transcript/image SHA not independently inspected); user confirmed GAP-08 candidate flashed.

**Locally observed XTR M:** live GAP-08 RX-only log >15k paired portable/V5 frames, zero frame/byte differences, resync, drops, physical TX or UART write attempts, DE=0; HARD_DENY. Repeated 085F/5 all-zero and 04A6/13, no fresh FC23/0708, current epoch/owner unknown. H021 alias NaN is expected without the required pages; fail closed.

**Offline core findings:** GAP-07 fresh/retained/recovery paths revoke page `write_base`; GAP-10 proves that mailbox/runtime toggles only block readiness temporarily, and re-enabling can reuse cached authority without a newly sourced qualified page. Separate synthetic inconsistent-Decision `commit_fc16()` trust-boundary gap; not demonstrated from the normal frame path or on real bus. Fix is required **before considering** native active TX.

**Protocol model:** native Thermia Online/DCM remains primary target; historical S11F/X/Y are separate bounded episodes, not a consolidated epoch. GAP-06 twelve historical fixtures are report-derived. Zero FC23 on present bus is not proof native handshake is impossible.

**Next:** **GAP-11 PREPARED / NOT RUN** — offline-only revocation-policy patch proposal plus contradiction/retoggle regression; no production YAML changes, no flash, no native TX. Baseline current installed GAP-08 RX-only; controlled change host-copy policy only; positive fresh-page requalification required; negative stale authority on retoggle; abort any widened TX or production regression; recovery leave current RX-only firmware unchanged.

**Safety:** native TX HARD DENY. Controller epoch/owner, G03 physical wire EOF, G04 reply slot, G05 electrical DE/FIFO and G06 reset/brownout fail-low remain OPEN or PARTIAL as previously documented. This update records test results, not new electrical permission.

---

# 2026-10-15 — V41V5-GAP-06..08 offline integrated; GAP-08B PREPARED / NOT RUN

> Newest additive status. [GAP-06..08 source-scoped report](V41V5_GAP06_TO_08_OFFLINE_20261015.md); [GAP-01..05 earlier report](V41V5_GAP01_TO_05_OFFLINE_20261015.md). Earlier GAP-06 proposed-status below is **historical and superseded**, not a still-open next experiment. All older project history is preserved.

**Latest completed offline experiment:** **V41V5-GAP-08 COMPLETE/POSITIVE, limited to source packaging/basic YAML parse/host regression**, full ESPHome config/compile, OTA and on-device integration **PREPARED / NOT RUN**. Prepared baseline is the *packaged* V5-TX-04B FIX1 RX-only YAML with local portable core and GAP-07 write-base invalidation. Existing YAML source fields/known-good HA scope preserved in offline delta audit (111 sensors, 71 text sensors); actual installed firmware hash **not verified**; full ESPHome compiler not available in the executed GAP-08 session.

**GAP-07 COMPLETE/POSITIVE host-only:** cached `write_base` revoked at `begin_retained()` and `begin_recovery()`; 530/530 assertions across six compiled host suites. **GAP-06:** report-derived 12 local-XTR event fixtures and host candidate requalification check COMPLETE/POSITIVE (bounded); original portable retained-session stale write-base property **COMPLETE/NEGATIVE**; patched-host candidate positive; full raw-XTR byte-parity **COMPLETE/INCONCLUSIVE** (original S11 raw logs unavailable here). A green 108/108 characterization of the original code does not negate its demonstrated stale-base vulnerability.

**Native evidence:** historical local XTR S9–S11 approved handshake/bootstrap/runtime and individual full-page semantic writes/readback are context-bounded. GAP-01..08 host tests do **not** demonstrate current on-device native response/active read-write functionality. No new register/page mapping, live experiment result, new firmware image or real native TX is claimed.

**Risks/safety:** user accepts G01–G06 uncertainty as research risk, not a claim of closure or general active TX permission; G02 conditional installation decision unchanged. G03 physical EOF OPEN, G04 exclusive reply slot OPEN, G05 electrical DE/FIFO PARTIAL/HOST-ONLY, G06 reset/brownout fail-low OPEN; new controller epoch OPEN. **Native TX HARD DENY**. Current V5 production configuration stays untouched. No GitHub production code changes.

**Next:** **V41V5-GAP-08B PREPARED / NOT RUN**: verify exact installed baseline, run actual ESPHome `config`/`compile` using the local component candidate, review entity/ID preservation and UART single owner, retain hard TX disabled. Positive full build+source inventory clean; negative compiler/entity mismatch; inconclusive missing ESPHome/secrets/original firmware identity. Abort any TX/DE path expansion; recovery use existing RX-only image. No live flash/active response without separately scoped approval.

---

# 2026-10-15 — V41V5-GAP-01..05 offline migration progress; GAP-06 PROPOSED / NOT RUN

> Newest additive status. Detailed source-scoped report: [V41V5 GAP-01..05 offline](V41V5_GAP01_TO_05_OFFLINE_20261015.md). All previous G01–G06 overlays and historical results below are retained; their electrical unknowns are NOT silently closed.

**Current experiment:** V41V5-GAP-05 **COMPLETE/POSITIVE (bounded metadata-only dispatcher tests 31/31)** and **PARTIAL/INCONCLUSIVE (full V4.1 branch/W0–W5 byte equivalence and actual positive local-XTR raw replay NOT RUN)**. GAP-04: **COMPLETE/POSITIVE offline mailbox policy 136/136**, full behavioral parity INCONCLUSIVE. GAP-03: **COMPLETE/POSITIVE offline synthetic/documentary session tests 114/114**, exact original-XTR byte replay INCONCLUSIVE. GAP-02: **COMPLETE/POSITIVE offline portable C++ adapter/replay**, semantic 69/69 and revocation 46/46; **18,507/18,507** decisions safely denied without authority in real *cross-model* replay. GAP-01: **COMPLETE/POSITIVE offline route inventory 58/58** (five owners plus an explicitly rejected legacy path). **None of GAP-01..05 installed as production firmware, and no native TX performed.**

**Live software baseline:** User-provided V5-TX-04B FIX1 log shows `[TX04B-FIX1] CALLBACK_ONLY` and the `V5 TX04B FIX1 Callback Timing (NO TX)` entity; software callback instrumentation is **COMPLETE/POSITIVE for bounded function**, no observed RX regressions or TX attempts in evaluated log. **G03 physical wire EOF→callback remains OPEN**: largest software callback gap is not wire-end latency. Current as-built firmware hash / full compile log not independently verified.

**Canonical protocol model:** V4.1's 58 distinct TX call sites map to approval 2; ordered 32-page bootstrap; generic runtime 1; mailbox 18; desired full-page responses 4; one legacy 04A6 recovery site explicitly denied. Consolidated development direction: one native session/ownership core with separate logical owner families, one fail-closed eventual output boundary. `085F` and `0884` cannot be ACK-authorized from page shape alone. GAP-03 detected a broad `0884` host-only RuntimeOverlay candidate; supplemental policy keeps unqualified `0884` capture-only. GAP-05 synthetic conflicting workfamilies default DENY, intentionally not full first-match V4.1 parity.

**Risk decision:** User accepts unresolved G01–G06 as **engineering research risks**, not automatic blockers for **offline development**. G02 remains **COMPLETE/POSITIVE CONDITIONAL** for unchanged installation only. G01 new controller epoch autonomous proof OPEN; G03 physical EOF OPEN; G04 exclusive response slot OPEN; G05 physical drain/DE PARTIAL HOST-ONLY; G06 reset/brownout DE fail-low OPEN. This acceptance does **not** make unknown predicates observed or authorize an unrequested active bus test. **Native V5 TX HARD DENY.**

**Next experiment:** V41V5-GAP-06 **PROPOSED / NOT RUN**, offline positive *local-XTR* event-fixture differential replay including mailbox owner/priorities, `085F/0884` source-qualified context, page freshness, cancellation and recovery. Positive: exact per-fixture state/owner parity; negative: false owner, unqualified ACK or stale page mutation; inconclusive: missing complete capture. Abort at any payload/TX/public private-implementation exposure; recovery keep existing RX-only YAML. No wiring, flash or GitHub sourcecode implementation change required.

---

# 2026-10-14 — G03-02R correlation audit COMPLETE/INCONCLUSIVE; G03 current physical EOF OPEN

> Newest additive status after user-approved G02 conditional closure. [G03-01R source revalidation](G03_01R_OFFLINE_REVALIDATION_20261014.md) and [G03-02R Saleae/ESPHome correlation](G03_02R_SALEAE_ESPHOME_CORRELATION_20261014.md). Prior dated current-state blocks preserved as historical. No new physical action or native TX.

**Last completed offline:** G03-01R COMPLETE/POSITIVE source scope; G03-02R COMPLETE/INCONCLUSIVE physical EOF→current B6 callback correlation, POSITIVE provenance audit. Original Saleae 2026-09-04 three sessions contain 55+156+1047=1258 CRC-good local XTR D2 ADUs; 22 available ESPHome logs inspected, none reliably simultaneous, byte matches with later logs recurrent/non-unique. No common synchronized clock anchor. Do not claim electrical callback latency or infer a safe G04 slot from host timestamps. Existing historical G03-03..05 wire edge decoding remains bounded positive. **G03 current B6 physical EOF OPEN**. G04 OPEN, G05 PARTIAL/HOST-ONLY, G06 OPEN. G01 manual intervention positive, autonomous epoch OPEN. **G02 remains COMPLETE/POSITIVE CONDITIONAL for unchanged installation only**, with invalidation triggers unchanged. **NATIVE TX HARD DENY**.

**Next:** locate a truly same-session Sep 4 ESPHome log if already existing (historical only); otherwise separately plan ONE passive synchronized D2 + current B6 RX-only measurement if justified and user-approved. G04-07 UART driver patch remains DEFERRED/NOT RUN; no new firmware or YAML changes.

---

# 2026-10-14 — G02 conditional closure approved; G03 next; native TX HARD DENY

> Latest additive canonical overlay. User explicitly accepts `G02 COMPLETE/POSITIVE (CONDITIONAL)` for the **unchanged, documented XTR M installation**, not for universal electrical exclusivity or current TX authorization. Full basis and experiment limitations: [G02-09..11B conditional closure](G02_09_TO_11B_CONDITIONAL_CLOSURE_20261014.md). Earlier dated G02 OPEN/NO-GO passages below are historical snapshots superseded for *scoped research acceptance only*; their negative and unknown observations remain valid.

**Current project status:** G01-09 `COMPLETE/POSITIVE INTERVENTION_ANCHORED` video+RX observed, autonomously electrically proven new controller epoch OPEN. G02-09 `COMPLETE/POSITIVE OFFLINE` finite capture role classification; G02-10 `COMPLETE/POSITIVE OFFLINE INVENTORY`, physical exclusivity INCONCLUSIVE; G02-11A `COMPLETE/POSITIVE BOUNDED HISTORICAL PROTOCOL WORK OWNER`; G02-11B `COMPLETE/INCONCLUSIVE ELECTRICAL EXCLUSIVITY`, `CONDITIONAL POSITIVE` one known external DCM interface/no DCM installed. **G02 overall: COMPLETE/POSITIVE (CONDITIONAL), installation-scoped decision made by user**. This does NOT prove all physical transmitters absent or grant live native reply rights.

**Known installation:** XTR hub two RJ45: `122 Display` with display; `123 Ext.` intended accessory path / ESP32 connection. ATEC p7 is cross-model; local PCB markings, photos and user installation statement corroborate roles, not exact copper or hypothetical other transceivers. No separate Online/Connect/DCM installed per user. User-video-anchored RX-only G01-09 24 FC23 requests and 0 observed peer response shapes in bounded window. Historical native XTR controller-work sessions exist; unknown concurrent physical responder not universally excluded.

**Invalidate conditional G02 immediately:** any additional Online/DCM, splitter/new wiring/board/profile, peer `0x0F` response/conflict, unknown current epoch or session owner, CRC/RX integrity failure. Then `G02=UNKNOWN/HOLD` for current context. The previous strict `G02_OPEN_NO_GO` electrical rule is NOT disproven: conditional acceptance is a changed scoped research policy.

**Installed baseline:** user-confirmed B6 RX-only, actual image hash not independently checked; no change to production HA. **Separate G03 physical EOF OPEN; G04 exclusive reply slot OPEN (G04-07 deferred); G05 electrical FIFO/DE PARTIAL/HOST-ONLY; G06 DE reset/brownout fail-low OPEN. Native 0x0F TX HARD DENY.** Do not unlock a TX interlock simply because G02 scope accepted. Last live user experiment G01-09; latest G02-09..11B work offline/documentary only.

**Next:** G03 offline investigation with existing UART owner/driver and captures; preserve no TX and no flash until independently approved.

---

# 2026-10-14 — G02-01..08 historical offline results reconciled; G02-09 PREPARED/NOT RUN

> Newest additive G02 overlay. Source-linked [G02 full offline evidence synthesis](G02_01_TO_08_OWNER_EVIDENCE_RECONCILIATION_20261014.md); preceding G01-09 video-anchored event remains POSITIVE within manual intervention scope. All dated material below remains historical; no hardware, firmware or HA changes were made for this reconciliation.

**G02 overall:** `OPEN / UNKNOWN` physical exclusive responder/work-owner; **`G02_OPEN_NO_GO` for native TX**, despite completed bounded offline analyses. `G02-01 RUNNING/PARTIAL` for full original local-XTR raw audit (ledger complete within typed source scope); `G02-02 COMPLETE/POSITIVE` inspected CM930 2.1.105 paths with 2.0.18 independent re-diff PARTIAL; `G02-03 COMPLETE/POSITIVE OFFLINE` seven genuine cross-model captures; `G02-04 COMPLETE/POSITIVE DOCUMENTARY_ONLY` historic local XTR work context; `G02-05 COMPLETE/POSITIVE HOST-ONLY` reducer; `G02-06 COMPLETE/POSITIVE OFFLINE PREFLIGHT`, optional on-device live SUPERSEDED/NOT RUN; `G02-07 COMPLETE/POSITIVE OFFLINE DECISION` = NO-GO; `G02-08 COMPLETE/POSITIVE OFFLINE` new locally supplied G01-09 FC23/owner-zero-response audit. None establishes physical exclusive owner or electrical TX authority.

**Reproduced 2026-10-14:** G02-05 38/38 units, 25,031 genuine cross-model CRC-valid records, 4,096 synthetic streams / 655,360 invariant checks; G02-06 16/16; G02-07 26/26. New locally witnessed RX-only G01-09 after video intervention: 11,944ms gap, 24 cumulative FC23 requests, zero matching peer response shapes in logged window, no ordered bootstrap, software TX=0. This supports bounded `NO_RESPONSE_OBSERVED`, **not** permanent address freedom, physical sender or owner exclusivity.

**NEXT:** `G02-09 PREPARED / NOT RUN` for source-typed same-epoch offline comparison only, positive/negative/abort/recovery per linked synthesis. No on-device response test now. G01 manual video event POSITIVE, strict measured controller-rail/future autonomous epoch OPEN; G03/G04/G06 OPEN, G05 electrical partial. **Native 0x0F TX HARD DENY** remains unchanged.

---

# 2026-10-14 — G01 video-anchored controller restart reconciled; G02 next (NO NATIVE TX)

> Newest additive state. Primary source: [G01-07R/08/09 video + RX evidence](G01_07R_08_09_CONTROLLER_RESTART_20261014.md). The user-provided original video and 4,660-line ESPHome log were reviewed. No firmware flash or new transmitted response was performed in this reconciliation; older dated G01/G04 states below remain historical as originally recorded.

**Current experiment:** G01-09 **COMPLETE / POSITIVE — VIDEO / INTERVENTION_ANCHORED**, physical main-controller voltage **not measured**; G01-08 COMPLETE/POSITIVE **OFFLINE** candidate replay, independent automatic boot proof INCONCLUSIVE; G01-07R historical chronology six XTR candidates (five clean and EXP296 HOLD). **Last completed live experiment:** G01-09, performed by user with one filmed switching operation and uninterrupted RX-only log. User considers G01's manual-start research objective successful. Strict `EXTERNAL_BOOT_WITNESSED` independent controller-rail/validated boot-ID claim remains **OPEN**; future current-epoch TX may not inherit this video's proof automatically.

**G01-09 local results:** video switch clicks, display dark and restarted; ESPHome XTR log gap 11,944 ms at 15:41:15.736; first valid `0x1E` return 15:41:15.749; `A80E=0000 A80F=0005` at 15:41:16.460; first FC23 counted by 15:41:17.021 and 24 cumulative FC23 by 15:42:55.315; no 32/32 configuration bootstrap and no native TX. ESP observer counters/API stayed continuous with no reported software TX, RX corruption or ESP reboot; separate contemporaneous ESP Uptime samples absent. Two reuploads are byte-identical, SHA-256 `a66541b2c8d91661863c6a315003ef26eb4ca3d8960e324479ff2a43cd8acb2e`. User associates video and log; video alone is not controller-rail measurement.

**Installed baseline:** user-confirmed `R6-P74DI-B6` RX-only, exact flashed binary hash not independently verified. Production HA entities preserved. **No newly approved active TX test. G02 physical responder/work owner OPEN; G03 EOF OPEN; G04 reply slot OPEN; G05 FIFO/DE PARTIAL/HOST-ONLY; G06 DE reset fail-low OPEN. Native 0x0F TX HARD DENY.**

**Next investigation:** G02 existing [owner research plan](G02_EXCLUSIVE_OWNER_PLAN_20261013.md), G02-01 and G02-02 first with source/provenance and current G01-09 evidence; prefer offline work. No repeat power cycling or fabricated ownership inference.

---

# 2026-10-14 — G04 evidence reconciled; B6 installed; G04-07 deferred

> Latest additive canonical overlay. Full details: [G04-01..07 evidence](G04_RESPONSE_SLOT_G04_01_TO_G04_07_20261014.md). Preserve all history below; no new native TX, no OTA flash, no controller restart.

**Current installed firmware:** user explicitly confirms R6-P74DI-B6 RX-only is running. The uploaded filename's PREPARED_NOT_FLASHED label is historical; installed binary/hash not independently checked. ESPHome 2026.9.0, Dashboard 1.15.0 user-confirmed. UART 9600 8E1, RX GPIO18, TX GPIO17, DE GPIO21; software debug timeout 5ms.

**Most recent G04 result:** G04-05 COMPLETE/PARTIAL bounded user-live software latency/RX integrity audit (88 B4 and 88 B3 events in 5000-line log; early callback-to-decision median 1545us, early decision median 6us; later B3 median 4169us). Zero parser resync/drop/geometry errors, zero software TX counters in reported live window. One API buffer-full warning. Original one-shot B5/B6 event missing from excerpt. G04-01..04 and G04-06 COMPLETE/POSITIVE within explicitly offline evidence/feasibility scopes; G04-07 **PREPARED / NOT RUN, user deferred**. Driver metadata prototype NOT compiled, NOT integrated, NOT flashed; do not treat as OTA-ready.

**Safety/protocol:** G04 exclusive physical reply slot OPEN; G01/G02/G03/G06 OPEN; G05 electrical FIFO/DE PARTIAL/HOST-ONLY. RX software timestamps and cross-model FC23 adjacency do not demonstrate electrical EOF, exclusive owner or permissible native TX. **Native 0x0F TX HARD DENY**. Historical local V4.1 EXP355/386/S11F/387 functionality retained as scoped positive reference; EXP388 PARTIAL, EXP419/423 INCONCLUSIVE, EXP425 NEGATIVE, EXP383 NOT RUN remain unchanged.

**Next step:** no immediate test: user postponed G04-07 due to complexity. When resumed verify full compile against ESPHome 2026.9.0 of single-owner UART metadata patch before separately approving any RX-only OTA. Do not use new physical wiring or a genuine DCM requirement.

---

# 2026-10-13 — G01 offline results reconciled, G02 research planned, native TX HARD DENY

> Additive newest overlay, preserving all earlier negative, partial and prepared observations below as historical snapshots. See [G01 synthesis](G01_CONTROLLER_EPOCH_20261013_SYNTHESIS.md), [G02 plan](G02_EXCLUSIVE_OWNER_PLAN_20261013.md) and [DI-B12 provenance erratum](R6_P74DI_B10_B12_PROVENANCE_RECONCILIATION_20261013.md).

**G01:** G01-01 source-check POSITIVE (21/21 includes; as-built PARTIAL), G01-02 offline 38/38, G01-03 offline 48/48, G01-04 old-projector robustness NEGATIVE (seven false epoch promotions), hardened host-only gate POSITIVE 2087/2087, G01-05 offline preflight POSITIVE 11/11 with new user-live NOT RUN, G01-06 offline evidence review POSITIVE 15/15 and independent physical boot witness NOT RUN. User confirms no Shelly/HA supply-power measurement for Thermia indoor unit. **Independent current controller epoch G01 OPEN.**

**G02:** physical sender, controller-work owner and actual reply permission are separate predicates. G02-01..06 PREPARED/NOT RUN; G02-07 PROPOSED/NOT RUN. Exclusive current responder/work owner OPEN. Next: G02-01 and G02-02 OFFLINE only.

**DD-DH updated offline scopes:** R6-P74DD PARTIAL exact as-built binary/dependency provenance, source audit bounded positive; DE COMPLETE/POSITIVE offline session projection (27 host checks); DF COMPLETE/POSITIVE bounded historical documentary replay, full original local raw XTR replay INCONCLUSIVE; DG COMPLETE/POSITIVE offline fail-closed host checks; DH COMPLETE/POSITIVE OFFLINE PREFLIGHT, new user-live measurement PREPARED/NOT RUN. None licenses native TX.

**DI-B10/11 provenance SUPERSEDED:** twelve all-zero 085F/5 + ACK-shape pairs were genuine collaborator/cross-model, not twelve locally proven XTR. October 3 confirmed ATEC DCM03; September 25 legacy-like profile with physical model UNKNOWN, conflicting historic Eco5 labels below retained. DI-B12 firmware bit7 085F vs bit10 0884, legacy 10x6 vs modern 8x7+4 history, no universal 085F-ACK to 0884. Raw observations retained; false provenance withdrawn.

**On-device:** CO historically last canonically confirmed RX-only, later separate DI-B6 user-run bounded log exists; exact CURRENT flashed firmware not independently checked. No G01/G02 research caused a flash, bus TX or controller restart.

**Safety:** G01/G02/G03/G04/G06 OPEN, G05 physical FIFO/DE only PARTIAL/HOST-ONLY; native FC23/FC16 ACK/0708/semantic writes HARD DENY. EXP388 RUNNING/PARTIAL; EXP419 and EXP423 INCONCLUSIVE; EXP425 COMPLETE/NEGATIVE unchanged.

---

# 2026-10-13 — CURRENT PROJECT STATE: R6-P74DC last completed OFFLINE; DD–DH PREPARED / NOT RUN; native TX HARD DENY

> **Newest additive overlay:** full scoped evidence and controls in [CX–DC results + DD–DH plan](R6_P74CX_TO_DC_20261013_RESULTS_AND_DD_DH_PLAN.md). Prior CW/BW–CD status sections remain below as historical snapshots, not the latest active-status claim. Preserve all negative and partial experiments.

**Last user-confirmed installed XTR M firmware:** **R6-P74CO RX-only** (bounded live log only; present-day uptime not newly checked). At HA Configuration dump: `CN_SHAPES accepted=214 rejected=0 FC16_REQ=214 FC16_ACK_SHAPE=0 FC23_REQ=0 FC23_RSP_SHAPE=0 source_latched=0 ... TX=DENY`. Early single V5 parser resync and historical P5 fault latch remain, cause INCONCLUSIVE; don't erase. CO/CN known-good production functionality and HA entities untouched by CX–DC.

**Most recent completed experiments — OFFLINE ONLY:** **CX** COMPLETE/POSITIVE syntactic classification of 13 `OTHER` frame families, no hidden 0x0F frame there, handshake cause INCONCLUSIVE; **CY** COMPLETE/POSITIVE unchanged 102 first-page requests (101 retries) in each of two genuine Eco5 slow contexts, timeout cause INCONCLUSIVE; **CZ** COMPLETE/POSITIVE genuine Eco5 first `03E8` ACK-shape timing ~118.478–120.296 host seconds after post-restart-related log-gap first frame, physical causal timer INCONCLUSIVE; **DA** COMPLETE/POSITIVE XTR historical versus Eco5 chronology, NEGATIVE universal 118–120-second **bus-return-to-ACK** wait on XTR (historical EXP355 all 32 ACKs finished within 33.595 s after logged return; original local raw log not independently re-parsed in DA); **DB** COMPLETE/POSITIVE Eco5 status timing with NEGATIVE `A80E/A80F` status alone proves native readiness (four Sep28 contexts same progression; later status around +66 s, ACK around +118–120 s); **DC** COMPLETE/POSITIVE ten-stage **offline** V4.1↔V5/CM930 gap audit (512 synthetic negative metadata cases), current actual XTR work-owner/active readiness still INCONCLUSIVE. Cross-model Eco5 and firmware-derived results **are not local XTR proof**.

**Most important model:** native Thermia Connect reference separates firmware approval (`NOT_ACCEPTED → RESPONSE_SENT → ACCEPTED`), application onboarding/runtime, and controller-owned native bus work. Wire ACK-shape != internal acceptance; 32/32 ACK shapes != semantic write acceptance. Old V4.1 XTR **EXP355/EXP386/S11F** scoped fresh restart→full 32/32→runtime success remains positive and was not reexecuted; **EXP387** qualified delayed semantic write success remains historical bounded only. **EXP388 RUNNING/PARTIAL** (cancellation not completed). **EXP425 COMPLETE/NEGATIVE** (predicted `0683` ordered tail after orphan `0662` ACK failed). Do not promote any historical active evidence to contemporary V5 TX authorization.

**Safety gates:** G01 independent current controller epoch OPEN, G02 exclusive current owner OPEN, G03 physical EOF OPEN, G04 response slot OPEN, G05 FIFO/drain/DE hardware PARTIAL/HOST-ONLY, G06 DE fail-low at reset OPEN. Owner/sender/epoch/slot/semantics UNKNOWN; **native FC23/FC16 ACK/0708/write TX HARD DENY**, no unsolicited transmissions.

**Next experiments (all PREPARED / NOT RUN; no YAML/test run):** **DD** exact V4.1-vs-CO source-map (source-linked owner/epoch/recovery/retained/cancellation gap), **DE** read-only session-candidate projection, **DF** raw-versus-documentary XTR historical replay (EXP355/386/S11F/W/X/388/423/425), **DG** deterministic fail-closed and HA production regression, **DH** *conditional* user-live RX-only observation **only after DD–DG justify it**. Decide after DD/DE, again after DF/DG; otherwise mark inconclusive, do not fake absent original logs. No controller restart, real DCM module or room-sensor disconnection.

**GitHub scope of this update:** additive evidence docs only, no production YAML, firmware code, private response security algorithm/payload, keys or mailbox tooling modified.

---

# 2026-10-13 — CURRENT STATE: R6-P74CT–CW completed OFFLINE; user-live CO RX-only; native TX HARD DENY

> This additive overlay supersedes only older **current-status** wording. It preserves every original negative/inconclusive/historical experiment below. Details: [R6-P74CH–CS handoff](R6_P74CH_TO_CS_20261013_HANDOFF.md), [R6-P74CT–CW report](R6_P74CT_TO_CW_20261013.md). Earlier R6-P74BW–CD results remain valid **for their bounded offline scope**.

**Installed and user-confirmed last:** **R6-P74CO** (XTR M ESPHome RX-only). CO on-demand user log at 12:45:02–12:47:39 shows `CN_SHAPES accepted=214 rejected=0 FC16_REQ=214 FC16_ACK_SHAPE=0 FC23_REQ=0 FC23_RSP_SHAPE=0 source_latched=0 ... TX=DENY`. An early single V5 resync, before the diagnostic button, produced one historical P5 fault latch and five safety `ABORT_NO_TX` messages; parser continued, observer recovered, 0 sample software UART TX. The exact fault cause remains **INCONCLUSIVE** and is **not** established as a CO regression. **CN** was explicitly compiled/flashed and its >15-min logged RX-only run positive for existing reception; had four API buffer warnings, no seen fresh session. **CH** retained RX-only logged positive for 17m51.752s; these are bounded software/log observations, not proof of physical DE fail-low.

**Most recent experiments:** R6-P74CT **COMPLETE / POSITIVE offline**: two genuine Eco5 slow contexts each have 102 first-page `03E8/count14` FC16 request shapes, i.e. 101 repeats, then a first short ACK shape after 108.653 or 108.507 host seconds; four fast response-bearing cases first ACK at 0.122–0.137 seconds. R6-P74CU **COMPLETE / NEGATIVE** for a new decoded STATUS-pair/FC23/FC03 request shape at that ACK boundary (each slow interval 102 STATUS and 102 first-page requests, 0 extra FC23/FC03 requests; status pair before/after `(40,10)` already repeated). R6-P74CV **COMPLETE / POSITIVE for descriptive fast/slow contrast, INCONCLUSIVE for predictive handshake/owner**. R6-P74CW **COMPLETE / POSITIVE host-only fail-closed model**: six broad 32/32 ACK-shape windows and one no-response context, 7/7 replay, 256/256 deterministic negative metadata cases with all authority bits false. Original seven verified cross-model captures 25,031 CRC-good pre-delimited frames. **No new local XTR fresh handshake proven.**

**Prior recent progress now reconciled:** CH user-live; CI–CM offline validation; CN user-live duration (frame-kind feature coverage partial); CO user-live button; CP offline chronology positive, resync-cause inconclusive; CQ time-window replay positive (120s 10/32,12/32 versus broad 32/32; NOT original P74AR boundary equivalence); CR retained-predictor NEGATIVE; CS dump-after-resync chronology positive with causal resync UNKNOWN. Cross-model Eco5/ATEC evidence is **not** local XTR M semantics. A short FC16 ACK *shape* does NOT imply controller acceptance, sender authentication or right to reply.

**Persistent historical outcomes:** EXP355/386/387 historical guarded V4.1 bounded successes; EXP388 **RUNNING/PARTIAL**; EXP425 **COMPLETE/NEGATIVE** for ordered `0683` tail after one ACK; no reversal. G01 unique current controller epoch **OPEN**, G02 exclusive owner **OPEN**, G03 physical EOF **OPEN**, G04 response slot **OPEN**, G05 FIFO/drain/DE physical validation **HOST ONLY/PARTIAL**, G06 DE fail-low **OPEN**. Native TX **HARD DENY**; no unsolicited response, emulation, `0708` command or speculative write.

**Next recommended, NOT RUN:** classify presently `OTHER` original genuine cross-model frames offline against source provenance and firmware-derived meanings, seeking a discriminator that is not a host-timing artifact. No new ESPHome flashing, restart, DCM attachment or room-sensor disconnection justified by CT–CW. Maintain CO RX-only; CN remains a fallback. Do not advance experiments on prepared YAML alone.

---

# 2026-10-13 — CURRENT STATE: R6-P74BW–CD completed OFFLINE; native TX HARD DENY

> Newest overlay, preserving every prior dated experimental observation. Detailed public-safe offline report: [R6_P74BW_TO_CD_OFFLINE_20261013.md](R6_P74BW_TO_CD_OFFLINE_20261013.md). Historical 2026-10-12 P74AQ/P74AR state below remains authentic for its date but is superseded for the current offline research progress.

**Most recently completed:** **R6-P74CD COMPLETE / POSITIVE (bounded integrated host-only offline regression)**. Sequential R6-P74BW, BX, BY, BZ, CA, CB, CC, CD are each COMPLETE / POSITIVE for explicitly documented **offline scope only**. Seven genuine **cross-model** archives 25,031 CRC-good pre-delimited frames, 4,809 native metadata events host-executed through unchanged BM/P74AT C++, 8,192 synthetic V4.1 cancellation-state combinations, and 210 deliberate CRC-corruption checks; all native output **HARD DENY**. No live ESPHome compile/flash, controller restart, direct XTR TX or new current owner/epoch proof. Public scripts/results are a separate local artifact, not published private emulation tooling.

**Prior recent progression (not erased):** BM RX-only staged and bounded user XTR logs strongly match its source and show no new sampled parser/resync/drop/B11D-parity or software TX issues. The exact flashed BM binary identity has not been independently established. BO and BQ were explicitly administratively closed as **COMPLETE / INCONCLUSIVE**, despite positive measured RX slices; BP and BR/BS offline positives, BT/BU/BV offline positives for bounded research, physical-epoch proof inconclusive. Do not call a prepared firmware compiled or user-flashed without direct evidence. Existing RX-only fallback is the user-known-good P74BC/P74AV family.

**Most material new result:** The original `Thermia_Connect_Firmware` research README attributes the Eco5 September 26 sequence to collaborator-reported controller restarts and **gateway present/absent/present** conditions. The 41 FC23 polls without recorded response in BW were in the **gateway-absent** segment according to that external intervention note. This is provenance, not independently sampled controller power rails or a new XTR current-session owner. BW 6/7 contexts have recorded response shapes. BX finds **6 broad context-to-context** 32/32 ACK-**shape** chains; earlier P74AR phases 4/5 documented **four full plus two partial 10/32,12/32** in more narrowly bounded episodes. **This is an OPEN SCOPING DIFFERENCE**, not license to rewrite P74AR observations or promote semantic ACK success. BY host-timing threshold classification is sensitive to ~100 ms adversarial synthetic shifts, so never use it for a live reply slot.

**Historical XTR:** EXP355/386/387 bounded V4.1 successes remain; EXP388 still **RUNNING / PARTIAL** with untested cancellation; EXP419 INCONCLUSIVE; EXP420 contextually POSITIVE; EXP423 INCONCLUSIVE orphan 0662; EXP425 **COMPLETE / NEGATIVE for expected 0683 ordered tail after ACK**; EXP426 INCONCLUSIVE trigger absent. Old successes cannot authorize new V5 TX. Cross-model source provenance never equals local XTR proof.

**Native Online/DCM protocol state:** main differences are fresh start, retained service `085F/5`, orphan `0662/33`, session cancellation and controller provenance. Present XTR BM retained RX-only `0x0F` FC16 usual `04A6/13`, `085F/5`, no fresh `FC23`, `0708` or current owner. All output stays HARD DENY: no unsolicited ACK, mailbox or semantic write.

**Safety gates:** G01 independent controller epoch OPEN; G02 exclusive owner OPEN; G03 physical frame EOF OPEN; G04 reply slot OPEN; G05 hardware FIFO/drain/DE-release HOST ONLY / PARTIAL; G06 DE fail-low physical OPEN. Sender authentication and controller outcome of incomplete bootstrap UNKNOWN.

**Next proposed / NOT RUN:** reconcile original P74AR narrow episode boundaries with P74BX broad context-to-context windows at exact original source lines; then reassess whether any genuinely new offline evidence remains. Do not propose a new physical DCM module, disconnect the room sensor or initiate TX based on the host successes. Production ESPHome/HA unchanged.

---

# 2026-10-12 — CURRENT STATE ADDENDUM: P74AQ user-live; P74AR phases 1–8 offline

> **Newest project-state overlay.** Supersedes only the *current-status* statements in older overlays (which had P74AB installed). Original observations below remain unchanged. Full dated, public-safe handoff: [R6_P74AQ_P74AR_20261012_HANDOFF.md](R6_P74AQ_P74AR_20261012_HANDOFF.md).

**Current installed / user-tested:** **R6-P74AQ COMPLETE / POSITIVE (bounded live RX-only shadow gate)** from user log `Pasted text(20261012-151054).txt` 17:04:50–17:08:10 (200.261s). Seven AQ snapshots EV 715→964, SEQ aligned, HOLD=0, TX=DENY. P74AL observed concurrently; zero new sampled parser bad geometry/unknown/resync/drop, sampled software TX and UART calls=0, no API buffer warnings. This closes only the *observed smoke-test scope*; the originally targeted 5 minutes and independent full HA production regression are **not documented**. Software DE LOW is not independent physical fail-low proof. Keep installed AQ unchanged; P74AL remains the last explicitly documented fallback.

**Current parent experiment:** **R6-P74AR RUNNING / PARTIAL (native Online/DCM session evidence reconstruction).** Phases 1–5: offline FC23→page→FC16 short ACK shape reconstruction, phase 5 32/32 tests. Six Eco5 episodes: four complete 32/32 ACK-shape chains, two partial 10/32 and 12/32 with long `03E8/14` retries; one ATEC episode has different geometry. These are **genuine cross-model** captures, not new XTR M V5 sessions or electrically authenticated owners. Phase 6: **COMPLETE / INCONCLUSIVE** for unique controller epoch/owner (30/30 offline tests pass); phase 7: **COMPLETE / INCONCLUSIVE** for epoch identification (20/20 offline tests pass; existing clock/defrost/register candidates rejected as unique boot markers); phase 8: **COMPLETE / POSITIVE offline software audit** (26/26 C++ sanitizer tests + 20/20 static source checks), but **ACTIVE-TX READINESS NO-GO**. No phase 1–8 performed new XTR controller, ESP or physical TX action.

**Current safety gates:** G01 unique controller epoch OPEN; G02 exclusive current-work owner OPEN; G03 physical wire frame end OPEN; G04 reply slot OPEN; G05 FIFO/drain/DE-release PARTIAL HOST ONLY; G06 electrical DE fail-low OPEN; native output `HARD DENY` throughout. P74AR phase 9 passive electrical measurement is **PREPARED / NOT RUN**, explicitly **deprioritized**, not silently executed. User prefers leveraging historical active experience before demanding more scope tests.

**Historical baseline to reuse without overgeneralizing:** EXP355/386 locally guarded V4.1 controlled restart→32/32→runtime **COMPLETE/POSITIVE**; EXP388 remains **RUNNING/PARTIAL** (untested cancellation branches). EXP419 085F branch INCONCLUSIVE; EXP420 explicit owner positive in tested retained context; EXP423 repeated `0662/count33` unowned sync-block INCONCLUSIVE; EXP425 ACK stopped loop but expected ordered tail did not follow (**NEGATIVE** for ordered-tail hypothesis); EXP426 isolated trigger absent (**INCONCLUSIVE**). No original EXP355/386 raw trace was re-parsed in P74AR; do not infer verified electrical timing, general owner or current V5 active permission. The wider EXP355–455 series must be audited from actual records, not characterized as universally positive.

**Next:** **V4.1 ↔ current V5/P74AQ implementation gap audit, PROPOSED / NOT PREPARED / NOT RUN**, with source-to-source owner/state evidence and explicit focus on EXP355–455, retained `085F`, orphan/repeated `0662`, cancellation and negative tests. Offline/read-only first; no room-sensor disconnection, no genuine DCM required, no new active response/ACK/writes. Preserve production HA entities and bus-health metrics. Reconcile these canonical files when a material new experiment result is received.

---

# 2026-10-12 — CURRENT STATE: R6-P74AI closed; R6-P74AB installed RX-only

> **Newest dated reconciliation.** This section supersedes *status statements* in older P74B–P74L overlays, not their historical observations. Older content remains below unchanged. Do not interpret delivery of a YAML as a live test.

**Current installed / locally observed:** **R6-P74AB COMPLETE / POSITIVE — bounded live RX-only normal runtime**, from user-supplied `Pasted text(20261012-095002).txt` (2026-10-12 11:46:13–11:49:33). P74AB EVENT 823→1101 (21 snapshots); P74W streaming and P74L journal consistent at their separately sampled times. Ordinary native `0x0F FC16 04A6/13` and `085F/5`; no new FC23, 32-page bootstrap or response ownership. V5 parser resync/drops, bridge byte/count differences and software TX indicators remain zero in observed window; P74D reports DENY_LOCKED and software DE LOW. **Not** an electrical DE/brownout/FIFO proof, complete production-HA regression, or live controller session approval. Configuration dump button not exercised.

**Latest completed experiment:** **R6-P74AI COMPLETE / POSITIVE (OFFLINE, bounded direct original-Core parity)**. The *entire original* `Thermia_Connect_Firmware/tools/xtr_dcm_reference_core.py` was SHA-verified to Git blob `671af7b27d2fbc2df988f4f080d13c7f06e6c496`, imported and directly executed against the unchanged C++ P74AF metadata projector: 4488/4488 default-unqualified owner decisions match; 4394 line-linked genuine Eco5/ATEC raw ADUs, 94 collaborator shape-only metadata; 16 local XTR journal metadata and seven explicitly synthetic qualified cases checked. In the raw-enriched fixture, 164 canonical FC23 shapes become `POLICY_OPEN / tx=False` (not `NO`); 334 prior OTHER are decoded FC03 responses. Prior P74AI RUNNING/PARTIAL is **superseded for the direct-execution blocker only**, not erased; this is not full stateful equivalence or live TX approval.

**Other recent results (preserving exact scope):**
- P74W COMPLETE/POSITIVE live RX-only; P74X COMPLETE/POSITIVE offline post-prefix classification; P74Y COMPLETE/POSITIVE offline cross-model episode provenance; P74Z COMPLETE/INCONCLUSIVE for genuine controller cancellation; P74AA COMPLETE/POSITIVE offline; P74AB COMPLETE/POSITIVE live (normal RX only).
- P74AC COMPLETE/POSITIVE source audit; P74AD COMPLETE/POSITIVE source-only checks; P74AE COMPLETE/NEGATIVE *for current active-TX readiness* (architecture NO-GO, no failed physical TX trial).
- P74AF, P74AG, P74AH COMPLETE/POSITIVE OFFLINE (metadata-only response intent, sticky DENY/HOLD, replay/regression); **not deployed**. P74AJ COMPLETE/INCONCLUSIVE for independently identified controller epoch; P74AK COMPLETE/POSITIVE OFFLINE deny-review contract; **active NO-GO**.
- Historical XTR V4.1 EXP355/386 COMPLETE/POSITIVE constrained controller-restart 32/32 bootstrap; EXP387 COMPLETE/POSITIVE active-path historical; **EXP388 RUNNING/PARTIAL** (pre-semantic and refresh-only cancellation branches untested).

**Protocol model and safety:** geometry/payload recognition, host-policy `POLICY_OPEN`, ordered synthetic 32/32 and FC16 address/count ACK are not exclusive response-slot ownership, semantic acceptance or authority to transmit. `0x085F`, recovery/retained service and `0x0708` require evidence-bound authorization not present in installed P74AB. Native TX **HARD DENY**; no autonomous FC23 response, ACK, mailbox service or semantic write. Never infer controller reboot from ESP reboot, constant A80F or A80E fluctuations (observed 0000↔0020 with no independent reset marker).

**Next:** preserve P74AB; offline/source work only until an independently verified same-controller-epoch/work owner, physical frame-end/response slot and DE/FIFO fail-low safety contract can be established. No new active experiment is prepared or authorized. User has no genuine DCM and cannot record one locally; room sensor is not the target and must remain connected.

**Detailed additive evidence record:** [R6-P74W_TO_P74AI_RECONCILIATION_20261012.md](R6_P74W_TO_P74AI_RECONCILIATION_20261012.md). Public artifacts deliberately omit private emulation payloads/implementation.

---

# 2026-10-12 — CURRENT STATUS OVERLAY: R6-P74B through R6-P74L (latest user evidence)

> **Current superseding status only; older observations and experiments below remain intact.** This overlay reconciles results supplied in the project conversation after the 2026-10-11 P41–P59 overlay. The repository had not yet reflected these newer live tests. No additional experiment was run by this documentation update.

**Current installed on XTR M:** user-tested **R6-P74E RX-only / HARD DENY** on the existing Waveshare ESP32-S3, as last confirmed by P74E live logs. **R6-P74L is PREPARED / NOT RUN**: YAML and six headers delivered, not yet compiled/flashed by user. The separate isolated P74D bench proposal is **SUPERSEDED / NOT RUN**, as the user requires no rewiring, second ESP, or bench hardware.

**Latest live results:** **P74B FIX1 COMPLETE / POSITIVE (borrowed-UART RX-only)**, user compiled/flashed; 2 logs show stable RX and no UART TX. **P74D alternative COMPLETE / POSITIVE (live DENY executor)**, user-supplied log confirms real device status `UART=1 DE_LOW_SW=1 EXEC=DENY_LOCKED RX_NOW=CLEAN P5_HISTORY=1 NEW_HOLD=0`, no new resync/drop, TX counters zero, software DE LOW; this is not a physical FIFO/drain/DE-release verification. **P74E COMPLETE / POSITIVE (live slot-evidence monitor RX-only)**, two overlapping logs (~43 status snapshots) show CRC/parser stability, zero new resync and drop, P5_HISTORY=0 in that boot, observed FC16 only, FC23=0, mailbox=0, physical output counters=0 and slot/owner/epoch/sender/wire-end UNKNOWN. The latest live evidence supersedes the older top-level claim that P37 is currently installed, while preserving the original historical P37 trial.

**Offline results:** **P74C COMPLETE / POSITIVE** source/readiness audit: P5 historical fault is sticky per ESP boot because absolute resync increments trigger P5 while later P74A/B compare baseline deltas; no automatic fault clearing. 14 active TX gates remain NO. **P74F COMPLETE / POSITIVE OFFLINE:** original V4.1 and historical EXP355/386 native 32/32 startup reconstruction, not new raw XTR timing proof. **P74G COMPLETE / POSITIVE OFFLINE:** seven genuine FC23 request/response episodes across Eco5 and ATEC captures; host-log intervals only. **P74H COMPLETE / POSITIVE OFFLINE:** logger timestamps not proven physical byte boundaries; ATEC `03E8/count13` vs Eco5/XTR modern `03E8/count14`. **P74I COMPLETE / POSITIVE OFFLINE:** the 2026-10-03 capture is attributed to ATEC in firmware research; a referenced sniffer script timestamps host receive chunks using `time.time()`, rounded to milliseconds, not wire-end. Script-version equivalence for every file is not independently proven. **P74J COMPLETE / POSITIVE OFFLINE:** event-driven synthetic bootstrap model; 10/10 tests, TX always DENY; capture replay recognizes first-page milestones, not full live 32/32. **P74K COMPLETE / POSITIVE OFFLINE:** P74E cumulative status-to-P74J non-promoting adapter, 10/10 tests; counters cannot reconstruct individually ordered FC23/ACK events. **P74L PREPARED / NOT RUN:** passive bounded 32-event `0x0F` journal designed at V5/P60 receive callback, exposing sequence, function/address/count and provenance; YAML and host tests prepared but no reported ESPHome build, flash or on-device result. No source-only/host validation should be described as physical bus proof.

**Protocol state:** local historical EXP355/386 COMPLETE / POSITIVE proved guarded original V4.1 controller-restart recovery, full 32/32 initial page export and fresh runtime in that controlled context; EXP387 last historically fully completed active trial. **EXP388 RUNNING / PARTIAL:** two restart subtests positive, pre-semantic and refresh-only cancellation not exercised. Modern RX-only P74E sees repeated `04A6/count13` and `085F/count5`, config 1/32, runtime 1/11, no fresh FC23 bootstrap, owner/epoch/slot UNKNOWN. Genuine Eco5 captures cannot authorize XTR output; ATEC count13 is model-dependent, not an XTR page template. P74J host session events and P74K cumulative adapter do not invent missing native ACKs or TX permissions.

**Safety / remaining blockers:** native TX HARD DENY; no private 0x0F response payload, command-mailbox/0708 machinery or recovered security data in public Research. Still unknown: physical GPIO21 DE reset/brownout behavior; physical UART FIFO/drain/DE-release; independently established controller epoch, sender/owner, wire-end and exclusive response slot; recovery after incomplete bootstrap; outstanding EXP388 cancellation branches. A normal FC16 ACK is not semantic acceptance. No new hardware/wiring or genuine DCM is to be required.

**Next:** execute existing **P74L RX-only** YAML on current ESP only after user compiles/flashes and returns 2-minute event-journal and parser/health logs; then review P74L as a live experiment. Until that evidence arrives, keep **PREPARED / NOT RUN**. Follow-on P74M P74J event adapter is only a proposal. No automated approval or active response from matching CRC or frame shape.

---

# 2026-10-11 — CURRENT STATUS OVERLAY: R6-P41 through R6-P59 (OFFLINE)

> This is the newest status overlay. It supersedes earlier “current/latest/next” status lines below, **not** their historical observations or experiment results. All steps R6-P41–P59 were offline only and did not run a new controller/native TX experiment. Reports and reproducible host-only packages were delivered separately in the project conversation; they are not ESPHome or physical-bus validation.

**Current installed XTR M firmware:** user-compiled/flashed **R6-P37 DENY-only RX-only** on existing Waveshare ESP32-S3. Last independently discussed bounded live P37 interval: 3,510 valid frames, 573/573 recognized FC16, no parser resync/drop, no B11C/B11D parity fault, UART attempts/writes=0, DE *reported* LOW, FC23=0, native mailbox=0, initial bootstrap=0/32. No new live observations during P41–P59. Hardware DE fail-low at reset/brownout remains **UNKNOWN**.

**Latest completed research:** **R6-P56–P59 COMPLETE / POSITIVE for integrated offline host-only TX review model** (735,721 test assertions with ASan/UBSan, 60,000 seeded fault cases, 25,031 already-framed genuine cross-model records, 9,968 FC16/FC23 request-shaped records, P59 static 15/15 and host-only build fences 4/4). Action scopes review first response, each of 32 bootstrap page ACK proposals, runtime, mailbox, and semantic writes separately. No UART/GPIO executor exists in the host model; every physical TX action is DENY. **Active V5: NO-GO / NOT RUN.** This is software-contract evidence only; individual assertions/cases are not independent physical trials.

**Intermediate offline results, all dated 2026-10-11:**
- **R6-P41–P43:** seven genuine paired first-response episodes all proceeded to first 03E8 request and ACK. Two Eco5 episodes exhibited ~108-second first-page retry spans with 102 requests in the focused window; **zero** deliberately isolated first-response-without-following-ACK episodes. P42 10/10 tests and 529 event pairs, P43 11/11 evidence checks. Controller pending/abort/autonomous timeout after incomplete bootstrap remains **OPEN / UNKNOWN**.
- **R6-P44:** historical working Write Beta V4.1 vs current P37 readiness audit, 7/7 static checks; missing active gates enumerated.
- **R6-P45–P47:** host-only C++ session authority/event adapter; 32-step synthetic fixture, no native output; P45 3,920,085 assertions, P46 14/14 static checks, P47 8,000,146 assertions. Fixture-supplied epoch/owner is not an actual controller identity.
- **R6-P48–P50:** seven raw reference files yield 25,031/25,031 CRC-valid **pre-delimited** frames; P48 125,167 policy assertions; P49 75,093 chunked frame replays and 1,171,252 assertions. P50 15/15 source checks. P37 V5 and B11D CRC framing remain *observational*, not independently proven electrical wire boundaries. B11D 25 ms measures UART callback idle, not measured wire silence; CRC-valid ambiguous prefixes require DENY.
- **R6-P51–P55:** integrated host RX/event/session pipeline: 1,828,923 assertions, 50,000 seeded adversarial cases, seven genuine cross-model sources × 3 chunk patterns, P55 23/23 static checks. P37 production top-level blocks/entities preserved against FIX4 in source audit; no new device-side ESPHome build.
- **R6-P56–P59:** V4.1 TX inventory (58 textual write_array and flush occurrences, **not** 58 distinct executed transfers), one-shot scope review and sticky abort, 32 staged synthetic proposals, capture replay and active NO-GO.

**Historical local XTR native proof unchanged:** **EXP355 COMPLETE / POSITIVE** and **EXP386 COMPLETE / POSITIVE** showed guarded fresh full bootstrap (32/32) and qualified runtime after real controller restart using the older active V4.1 family, ESP remaining powered. **EXP387** is the last fully completed historical active experiment. **EXP388 RUNNING / PARTIAL**: two controller-restart subtests succeeded; pre-semantic and refresh-only cancellation branches remain untested. Historical successful full recovery does **not** prove safe cancellation of a partial bootstrap, ESP hot-rejoin, or V5 physical driver correctness.

**Protocol/roles:** observed native challenge context uses 0x0F FC23 071C/count8 -> 0730/count8 and initial controller FC16 pages from 03E8/count14 through 06F4/count19, followed by fresh runtime evidence including 085F/count5 and 0708; use historical/local attribution only where actually exercised. No recovered private handshake response, private 0x0F code, or 0708 command-mailbox implementation is published in this overlay. Cross-model framing, timing and records are not current-XTR owner proof.

**Current safety gates / OPEN:** independent physical GPIO21/DE fail-low through reset/brownout; bounded UART TX+flush and DE release; independently qualified controller-origin reply slot; physical session epoch/owner; ambiguous frame boundaries; safe controller recovery after incomplete initial export; both outstanding EXP388 cancellation branches. Repeating host fuzz cases cannot close these hardware/controller questions. An FC16 address/count ACK is not evidence of semantic acceptance.

**Next proposed step (NOT RUN):** **R6-P60 RX-only ESPHome integration readiness / passive design**, first compare and preserve deployed P37 entities and bus-health bookkeeping and verify non-transmitting adapter under a new separately reviewed RX-only experiment. No flashable YAML, live trial, active 0x0F reply, auto ACK, mailbox or write is authorized by R6-P41–P59. To prepare active TX later, require separate explicit permission, known current slave/page/register/value, provenance, plausible effects, abort and recovery. No new wiring/DCM hardware requested.

---
# 2026-10-11 — CURRENT STATUS OVERLAY: R6-P37 to R6-P40

**Current installed firmware:** R6-P37 DENY-only RX-only on the existing Waveshare ESP32-S3 (user compiled/flashed). Last examined local XTR log at ~20:33:15–20:36:42: 3510 valid frames, FC16 573/573 recognized, no geometry mismatch/resync/drop, no B11C/B11D count or byte differences, UART TX attempts/writes=0, DE reported LOW. FC23=0, 0708 mailbox=0, bootstrap=0/32, H021 NaN because target pages absent. This is limited live RX-only proof, not a fresh native Online session or evidence of electrical fail-low at reset.

**Latest completed experimental step:** R6-P40 COMPLETE/POSITIVE for isolated offline host-only single-slot review model (7/7 methods; 2048 guard combinations; 500 repeat attempts). All actual TX/FC16 ACK/mailbox/semantic actions DENY; it did not run on the bus. R6-P39 COMPLETE/POSITIVE as offline readiness review, immediate active V5 NO-GO/NOT RUN. R6-P38 assistant full ESPHome build INCONCLUSIVE (dependencies unavailable), but user subsequently successfully compiled/flashed P37; do not conflate these. R6-P37 COMPLETE/POSITIVE for bounded live RX-only regression. Earlier P31–P36 are offline audits and models, not active XTR trials.

**Locally proven historical native operation:** EXP355 and EXP386 show guarded controller cold-restart fresh-session recovery with ESP remaining on and 32/32 initial page synchronization followed by runtime qualification; EXP388 restarted successfully twice in selected subtrials, but remains RUNNING/PARTIAL because pre-semantic and refresh-only cancellation cases have not been separately tested. Last historically fully completed active V4.1 experiment EXP387. The current live P37 has no active UART-write or DE-on code and cannot be treated as an active responder.

**Protocol model:** genuine cross-model DCM captures support complete 32/32 fresh session, 31/31 selective refresh, and >100s retries on initial 03E8. Cross-model results are not XTR authorization. Controller physical epoch UNKNOWN; native work owner UNPROVEN; hot-rejoin after ESP restart NOT PROVEN; native TX DENY. First FC23 response, each FC16 ACK, 0708 mailbox and semantic write require separately bounded permissions. An FC16 ACK alone is not semantic acceptance.

**Safety and next experiment:** user does not want additional hardware/wiring, and immediately compiles+flashes any supplied YAML. No active YAML should be supplied without separate explicit approval of a live active experiment. R6-P41 proposed OFFLINE/NOT RUN: analyze controller pending state after an initial native response without subsequent page ACKs using existing captures and historical records; define abort/recovery and open unknowns. No reboot/TX planned. P39/P40 did not alter installed firmware, warm pump or GitHub. Raw original EXP355/386/388 logs were not independently reparsed in P39/P40.

---
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