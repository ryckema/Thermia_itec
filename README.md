# Thermia iTec XTR — ESPHome & Home Assistant

**Local monitoring and control of the Thermia iTec XTR heat pump using ESP32, ESPHome and Home Assistant.**

This project provides a local, cloud-independent integration for Thermia iTec XTR heat pumps by communicating directly with the heat pump's internal RS485 bus.

The integration is developed and tested on a **Thermia iTec XTR M with Total Compact indoor unit**, using an ESP32-S3 with an RS485 interface.
If you are looking for a ATEC version it can be found here: https://github.com/fclauson/Thermia-ATEC-ESP-emulator-of-DCOM

## Roadmap

**2026-10-31 XTR W2R55 P4 attempted controller-value rollback NOT SENT — W2R54 experiment still RUNNING / PARTIAL.** Real uploaded W2R55 01:32–01:36 log: native owner M6=5, CURRENT4/4, auto CAL12/12, CRC_CHECK104580 DIFF0, parser resync0 and RX buffer drops0. At01:34:25 valid native P4 F1 3/3 confirms controller **17:21–18:27 Monday+Sunday** (0x41), so previous four physical W2R54 trial settings still persist. User staged three HA-only corrections **startHour 17->18, startMinute21->20, stopMinute27->26**, preview at01:35:26 `changedRegisters=3 / NOT SAVED / NO TX`. First selected Start Hour Apply01:35:28 prepared only; second01:35:30 properly denied `CAL_EDITOR_WRITE_ON_HOLD` because explicit dedicated **Configuration | Calendar Trial | Arm P4 Weekly Fields (10 Sends / 30min)** was never pressed; generic heating-write enable is distinct. Another Apply01:35:57 only PREPARED. **ZERO new physical calendar setting TX; W2R55 P4 multi-staged guard not tested** (it deliberately checks >1 fields only with dedicated P4 trial ARMed). Do not call this a native bus or controller Stop Hour failure. **ONE NEXT ACTION:** user restores actual P4 to Sunday18:20–18:26, preferably via OEM panel; alternatively within existing user-approved bounded P4 trial, discard unsaved HA staging, fresh controller-owned P4 Read Selected, explicit dedicated P4 ARM and send each separate user-selected one-field revert with Preview changedRegisters=1 and double Apply, independent genuine controller readback before next (startHour17->18; startMinute21->20; stopMinute27->26; Monday0x41->Sunday0x40). S92 ABORT immediately on any defect; firmware rollback/Discard alone cannot undo controller schedule. Other HA parameter and calendar writes remain HOLD; do not repeat four validated forward writes or make broader scope.

**2026-10-31 W2R55 XTR LIVE normal-runtime + new editor BUSY guard — COMPLETE / POSITIVE (scoped), P4 rollback NOT DONE.** User log 01:15:34–01:19:32 proves actual MAIN04-W2R55 build (three reports), retained M6=5 stage40 long runtime (~12125s, not boot evidence), original CURRENT FC16 4/4, two automatic owned calendar12/12, CRC_CHECK96788 DIFF0, resync/drop0, queue0. Real calendar shows **Program4 STILL 17:21–18:27 Monday+Sunday**, original Sunday18:20–18:26 not restored. User selected **Program5**, controller-owned F1 3/3 Saturday18:30–18:35. Staged P5 time edits, user Apply attempts got intended `WRITE ON HOLD` for all P5 physical writes (only P4 trial authorized) and an order denial where selected start hour19 would violate original P5 end hour18. **W2R55 new `EDITOR BUSY / retry Apply when idle / NO TX` actually verified** twice during automatic calendar transaction at01:19:08/15. **W2R55 new multi-staged field HOLD specifically while P4 trial ARMed is still PREPARED / NOT RUN** (user never armed P4 during log), so don't claim fully editor-live validated. No new physical calendar write and no new semantic stop-hour. At01:18:39 user also separately pressed `Configuration | Enable Heating Writes (User Initiated)` and enabled a distinct existing heating/hotwater/cooling setting edit lease; no immediate TX and no parameter setting physical write observed. This button is NOT P4 calendar trial ARM; avoid any additional parameter edits, HA parameter writes remain project ON HOLD. Full W2R54 write trial stays RUNNING / PARTIAL pending physical P4 rollback confirmation. **ONE NEXT ACTION:** manually restore actual controller Program4 using Thermia original panel to Sunday18:20–18:26 and obtain fresh owned native readback; only then decide whether to test Stop Hour and P4 multistaged editor path with explicit bounded user scope. W2R55 is latest XTR LOCALLY VERIFIED normal-runtime code, no reflash or repeated passive tests needed.

**2026-10-30 latest W2R54 XTR physical P4 calendar trial — RUNNING / PARTIAL; W2R55 private editor fix PREPARED / NOT RUN.** Four real OEMW/S92 one-word P4 controller-semantic accepted values: Stop Minute 26->27 reg0584 at17:40:04, Start Minute20->21 reg057F at17:41:26, Start Hour18->17 reg0580 at17:42:21, Weekdays Sunday0x40->Sun+Mon0x41 reg0589 at17:45:09. Physical 4/10 sends, no retries; normal M6=5/CRC_DIFF0/RX drops0. Stop Hour18->17 had **NO physical TX**: shared native automatic calendar refresh caused busy idle=0 at17:43:30, later only PREPARED at17:43:34, never second Apply. W2R53 staging guard correctly blocked Read Selected. Weekdays was then separately applied while Stop Hour remained staged, leading Preview changedRegisters=2 but the original sender correctly wrote ONLY weekdays. W2R55 SOURCE/OFFLINE TESTED (NOT target compiled or live) adjusts only original HA Apply handler: precise BUSY retry-Apply status for idle=0, and if trial explicitly ARM-ed rejects >1 pending staged field before PREPARE/TX with Discard-one-field guidance. One original UART/RX/DE S92 owner, original guarded writer, 30-min/10-send P4 scope, CRC, V5 and native FC16/FC03 read/auto-refresh/ABORT unchanged; complete private firmware ZIP with exact W2R54/W2R53/W2R52/W2R51 YAML rollbacks. **CRITICAL:** latest confirmed controller P4 in logs is **17:21–18:27 Sunday+Monday**; original Sunday18:20–18:26 is NOT proven restored before supplied log ended 17:45:19. Firmware flash, Discard or ABORT cannot reverse physical P4 setting writes. **NEXT ACTION:** user check/restore actual P4 via the Thermia original panel and confirm native controller readback. Only then consider optional manual W2R55 target compilation/flash. Do not repeat proven four field writes or treat Stop Hour as controller failure. Experimental physical HA/calendar setting permissions remain otherwise ON HOLD; no create/delete/date or extra TX architecture.

**2026-10-30 W2R54 PRIVATE BROADER CALENDAR TX TRIAL — SOURCE / OFFLINE TESTED, PREPARED / NOT RUN.** User permits a larger **bounded, user-initiated** physical trial. Latest actual XTR locally verified basis **W2R53**: native M6=5, CURRENT4/4, automatic CAL12/12, P4 RAM staging20→21, re-read correctly blocked, deliberate Discard→20 (both editor functions COMPLETE / POSITIVE), V5 CRC_DIFF0/drop0/resync0. W2R54 integrated full private YAML (not pushed): new disabled-by-default HA Configuration ARM, one boot-local/session-qualified 30-minute lease for max **ten manually confirmed physical one-word calendar page sends** to **already configured weekly DHW Program4 only**. Covers start/end minute/hour and weekday mask, one field per explicit user double-press, time ±1, weekday one-bit toggle, nonzero days and nonovernight program; five forward changes and five deliberate controller-value reversals, with genuine controller-origin FC16 semantic receipt and independent fresh selected F1 readback after EACH. Global other calendar and all HA parameter setting HOLD stays enabled; only this scoped OEMW descriptor23 inside existing sole S92 UART/RX/DE owner is temporarily authorised, never autonomous TX, no extra frame/reader/retry. Normal live W2R53 functionality, V5/CRC/B11C/B11D/DE/ABORT preserved; existing S92 manual ABORT immediately revokes test permission. One complete private 8-entry source+instructions+checks+diff+manifest+exact W2R53/W2R52/W2R51 rollback ZIP locally verified for YAML entity IDs/ZIP checksums, **NOT target compiled, flashed or XTR tested**. Firmware rollback **does not** undo physical controller calendar value changes: user must verify/restore the actual Thermia controller settings via its native UI on failure. No create/delete/date/overnight or other calendar program writes authorised, no room sensor removal. W2R41 was a real one-minute controller write, but does not prove the broader d23 fields. **ONE NEXT ACTION:** user manually compiles and optionally flashes W2R54, initiates explicit HA ARM and each bounded field transaction/readback/physical restoration, with ABORT on first fault; do not repeat verified passive/OTA/editor tests.

**Latest XTR live milestone — 2026-10-30 W2R53 calendar editor COMPLETE / POSITIVE (LOCALLY VERIFIED).** W2R53 already proved native M6=5, FC16 CURRENT4/4, automatic 12/12 calendar refresh and clean V5/RX in a real continuous run. A subsequent user-initiated, RAM-only HA test now also proves the editor fix: Program4 genuine owned F1 3/3 read at16:35:28–30 (Sunday18:20–18:26), stage start minute20→21 at16:35:56 NO_TX, accidental Read Selected blocked at16:35:57 with READ_BLOCKED_UNSAVED/noReadTX, and deliberate Discard at16:36:44 restored HA start minute20 from the same owned snapshot, NO TX. 0 CRC differences out of >=12887 checks, resync0/RX drops0, dirty/pending0. **Calendar HA editor staging/overwrite prevention and Discard are complete; don't repeat tests or refactor them.** HA/calendar physical parameter writes remain **HARD ON HOLD**, and neither this RAM-only test nor existing controller transport ACK confirms full calendar setting-write permission. Earlier W2R41 independently proved only one P4 stop-minute25→26 XTR setting change; other fields/create/delete/date/overnight remain unproven. **ONE NEXT ACTION:** use existing W2R41 XTR evidence to define a *single* bounded semantic calendar setting GO/FIX/NO-GO via the sole S92 owner, with explicit separate user permission and ABORT/rollback before ANY new physical setting TX. Controller-only outage recovery still separate/not physically proven; no power-cycle or room sensor removal.

**Development status (30 October 2026):** **W2R46** remains the last XTR **FULLY LOCALLY VERIFIED** for normal OTA startup, native M6=5, CURRENT 4/4 and automatic calendar 12/12. W2R45 and W2R44 were also locally verified for routine read/cache operation. **W2R47** is now XTR **FLASHED / LIVE / LOCALLY VERIFIED — COMPLETE / POSITIVE for ordinary read/runtime**: retained/manual-context M6=5, genuine CURRENT4/4 and automatic 12/12 controller-owned calendar receipt at 11:38:10 on 30 October. CRC_DIFF=0 across 36,499 checks, RX drops=0, parser resyncs=0, no setting writes. W2R46 remains the separate proven OTA-startup rollback; W2R47 startup/recovery and its shared legacy failure/abort guards were NOT tested. **W2R48** is now XTR **FLASHED / LIVE / LOCALLY VERIFIED — COMPLETE / POSITIVE for ordinary native read/runtime**: owner-indexed selector/desired storage migrated (714→704 globals), full automatic calendar 12/12 receipt 12:36:59 and CURRENT4/4 confirmation 12:37:34 on 30 October. CRC_DIFF0 over 21,613 checks, RX drops0 and parser resyncs0, no HA setting writes; original per-page semantic selector/commit branches remain. W2R48 initial cold start, automatic rejoin, timeout/abort negative paths and semantic setting writes were not tested. **W2R49** is XTR **FLASHED / LIVE / LOCALLY VERIFIED — COMPLETE / POSITIVE for ordinary native read/runtime**: owner-indexed six original native `0708` CURRENT/desired-selector frames and common qualification in one existing S92 RX/TX owner preserved full M6=5 retained session, CURRENT4/4 controller FC16 ACK at 13:25:40 and TWO automatic native calendar12/12 controller-owned receipts at 13:25:31 and 13:29:02 on 30 October (same session, second after ~200-second freshness). V5 CRC_DIFF0 across 11,940 checks, RX drops0/resync0, pending/dirty0; no HA setting TX. Original per-owner selector write, retry/commit/rollback semantics, cold start and automatic rejoin not tested and not declared verified. **W2R50** is **FLASHED / LIVE / LOCALLY VERIFIED — COMPLETE / POSITIVE for OTA retained-session restoration and normal native read/runtime**: after actual ESPHome OTA reboot the system did not inherit ownership, requalified existing native transport by real controller FC16/0708, reached CURRENT4/4 mask0F (14:17:25) and controller-owned auto calendar12/12 (14:17:47). One-shot runtime check at14:18:57 reports POSITIVE_RUNTIME_SYNC; CRC_DIFF0 across1681 V5 checks, RX drops/resync0, FC16 ACKs1→107, no HA parameter writes. Its common 042E/0442/0546 FC16 semantic snapshot/strict comparator/phase core preserves the sole S92 owner, page-specific guards and rollback. Strict republish/semantic setting-write branches were not exercised; cold controller startup, forced session-loss rejoin and OEM Online equivalence not proven. **W2R51** is XTR **FLASHED / LIVE / LOCALLY VERIFIED — COMPLETE / POSITIVE for normal native read, OTA retained-session recovery and automatic refresh**. After actual OTA, M6=5 and CURRENT4/4 at14:36:50, controller calendar12/12 at14:37:07; subsequent SAME epoch11490 native calendar12/12 at14:40:37 and14:44:08, plus a fresh controller CURRENT4/4 at14:41:07. V5 CRC_CHECK3809 DIFF0, RX drops0, ambiguous0, no parameter writes; FC16 ACKs117→245 and 0708 replies50→102 in the 14:40–14:44 continuation. **Explicit nonblocking startup unknown:** V5 parser resync counter reached100 by14:36:42 but remained precisely100 through14:44:12; W2R51 parser code counts increments without 100 cap and is unchanged from W2R50. No evidence of ongoing RX corruption or loss; do not label the reboot perfectly RX-clean or infer cause. W2R50 remains separately zero-resync OTA rollback. W2R51 consolidates common EXP378 042E/15, EXP379 0442/13 and EXP380/383 0546/20 FC03 selector/desired eligibility, phases and saved CURRENT-to-EXP421 builder in the same S92 owner and shares exact six original idle replies, while preserving per-page cooling requeue, 0546 word19-only rule, allowlists and HA rollback. Page-specific semantic parameter writes/requeue/rollback and controller cold-start/forced hot-rejoin were NOT tested; original S92/V5/CRC/DE/ABORT protections and setting-write HOLD remain. **W2R52 is now FLASHED / LIVE / LOCALLY VERIFIED — COMPLETE / POSITIVE for ordinary XTR OTA retained native entry and first CURRENT/calendar read**, not for controller-only physical recovery. User OTA log15:43:02–15:46:00 shows RX_ONLY initial, qualified 0884/transport M6=4 at15:43:22, native FC16 CURRENT4/4 mask0F M6=5 epoch12302 at15:43:29, native controller-owned calendar12/12 at15:43:46 and CAL5 ack15:43:51, C5BT observational POSITIVE_RUNTIME_SYNC at15:44:57 (NO_TEST_TX). CRC_CHECK1422 DIFF0, parser resync0 and RX drops0 across samples, 92 FC16 ACKs, 35 0708 replies, dirty/pending0. This capture ends before the next original ~200s automatic CAL refresh. The newly added 0x02-only loss/revoke/guarded cold retry while room sensor0x0A continues is still PREPARED / NOT RUN for actual XTR outage; experimental controller-only 120s one-shot defaults OFF, no new setting-write permission. W2R51 remains proven for recurring CAL; W2R50 zero-resync OTA rollback. **W2R53 is now XTR FLASHED / LIVE / LOCALLY VERIFIED — COMPLETE / POSITIVE for native normal-runtime CURRENT4/4 and recurring automatic CAL12/12 only.** User 16:21:18–16:25:27 continuous runtime log confirms actual MAIN04-W2R53 build (device already uptime725s, NOT OTA start), same owner M6=5 stage40, genuine FC16 CURRENT4/4 epoch11551 at16:22:59, original automatic calendar 12 controller-owned page receipts at16:24:21 / CAL5 16:24:27 following refresh arm and real native 0708. CRC_CHECK7449 DIFF0 SHAPE_OTHER0, RX drops0/ambiguous0/parser resync0, FC16 ACK355→475, idle 0708 replies153→207, dirty/pending/queued0. Specific W2R53 HA staging-protection and Discard buttons were NOT pressed in this log and remain PREPARED / NOT RUN for editor proof. No HA/calendar semantic write; HOLD unchanged. W2R52 remains separately user-live OTA retained restart baseline. **W2R53** private complete firmware is SOURCE / OFFLINE TESTED — PREPARED / NOT RUN for the calendar editor. A prior W2R42F1 local XTR observation proved unsaved P4 start-minute RAM staging was overwritten by Read Selected. W2R53 protects same-epoch owned F1 selected-program staging from silent re-read overwrite and adds one explicit RAM/HA-only Discard Staged Changes button. EXACT W2R52 latest XTR locally verified ordinary OTA/CURRENT4/4/CAL12/12 baseline and its single S92/V5/CRC/DE/ABORT/recovery guards remain; no new setting TX, all prior HA IDs retained, W2R52/W2R51/W2R50 rollbacks bundled. W2R53 is NOT target compiled, flashed or live. **Calendar editor and scoped XTR setting validation now take priority over any forced controller-loss recovery trial.** **W2R41** remains the last independently confirmed physical calendar setting update. All calendar-setting trials and regular HA parameter setting writes remain **ON HOLD**.

1. **Consolidate native calendar reads** into one authoritative F1 data store, retaining controller-origin CRC validation, per-page freshness, and a separate owned-session receipt generation. **Implemented and first XTR OTA read-only live verified in private W2R43**; ongoing automatic freshness and independent controller-origin receipt checks remain in place.
2. **Retain one OEMW setting transaction and one S92 UART/RX/DE owner.** Source W2R43 shares one page snapshot across legacy confirmation paths without adding bus writers or changing retry/safety guards.
3. **Consolidate remaining EXP378/379/380 handlers under the existing native/OEMW/S92 owner.** W2R44/W2R45/W2R46 progressively consolidated CURRENT, desired/confirmed and lifecycle storage and were locally observed for normal read operation. W2R47 (FLASHED / LIVE / LOCALLY VERIFIED for normal read/runtime) consolidates the three owner-specific queue-expiry, active integrity/timeout watchdog and runtime-qualification decisions while preserving the original page-specific UI rollback/guards and one physical S92 owner. CURRENT4/4 and the automatic owned calendar12/12 receipt are verified. **W2R48 LIVE / LOCALLY VERIFIED** preserves genuine M6=5 and native calendar 12/12 and CURRENT 4/4 while migrating selector/desired target-word, target-value, original-value and two transaction timestamps into owner-indexed arrays; page-specific selector/commit branches and original S92 owner remain. **W2R49 LIVE / LOCALLY VERIFIED** unifies six original native `0708` CURRENT/desired selector response frames and common qualification in existing S92 owner with two completed native calendar read cycles, CURRENT4/4, CRC0, no RX drop or setting write. Individual EXP378/379/380 selector/semantic commit/requeue/rollback branches still have differences and remain source dependencies. **W2R50 LIVE / LOCALLY VERIFIED** consolidates native FC16 snapshot/strict semantic comparison and shared CACHED/NOOP/CONFIRMED/DISABLED transitions in the same sole S92 owner, and its OTA retained-runtime restoration and native CURRENT4/4+calendar12/12 are now directly observed. All semantic setting writes and forced fault paths are still untested, still ON HOLD. **W2R51 development phase (now XTR LOCALLY VERIFIED for normal native reads):** same sole native owner now also centralizes the original three FC03 selector/desired preflight, state transitions and saved CURRENT-to-EXP421 desired frame construction; original 0442 requeue vs 042E/0546 disable and page-specific HA rollback remain distinct on purpose. Six identical idle responses now share one guarded emitter, no new physical TX role. **W2R51 LIVE / LOCALLY VERIFIED — COMPLETE / POSITIVE for native reads and recurring refresh**: same OTA session automatically repeated controller CURRENT4/4 and calendar12/12 across minutes with CRC_DIFF0, drops0, and unchanged early resync counter100 for over7 minutes. **Initial100 parser resyncs are a NONBLOCKING UNKNOWN**, not erased or reclassified as zero; W2R50 is clean-zero-resync OTA fallback. **Source decision COMPLETE / POSITIVE, NO-GO further general branch refactoring:** exact W2R51 FC16/FC03 shared transaction paths already centralize identical work. Remaining 042E hot-water UI, 0442 cooling EXP390 requeue/dynamic limits, 0546 enum/word19 TEST-link and HA rollback are genuine page-specific distinctions. **Next engineering milestone:** integrate actual controller-restart/session-loss detection and validated native automatic hot-rejoin/cold-start fallback in ONE existing S92/M6 owner, distinguishing these from ESP OTA reboot and FC03/current refresh failure, preserving FC16 CURRENT 4/4/calendar 12/12, original DE/CRC/ABORT guards and HA functionality. Existing native entry and controller-loss recovery handlers exist but actual XTR controller restart/forced rejoin are NOT user-live verified; do not autonomously enable any new unvalidated physical TX. HA/calendar setting writes remain ON HOLD. No repeat proven read tests. Page-specific EXP selector/desired branches still have dependencies and are **not yet fully removed**; do not introduce a parallel TX path.
4. **Calendar setting trials ON HOLD at user request.** Both old and new calendar pilot setting TX paths are held in W2R43. Normal native FC16 sync/ACKs and FC03 read/refresh are not setting writes. New/other calendar fields and create/delete require separate XTR validation and explicit user authorization before any new physical setting TX.
5. **General Home Assistant parameter writes remain ON HOLD** pending user authorization and real controller semantic validation.
7. **Finish calendar editor and controller semantics, without speculative TX.** All 12 controller-owned calendar read pages, four calendar-domain HA readbacks and separate selected DHW F1 3/3 staging are present. Last independently confirmed real XTR calendar value update is W2R41 P4 stopminute25→26, not a blanket write authorization; W2R42F1 showed the concrete manual Read Selected staged-edit overwrite. W2R53 PRIVATE source fixes only that editor bug (READ BLOCKED on unsaved five weekly fields; user Discard clears stage to F1; NO TX). It remains PREPARED/NOT RUN; W2R52 is user-LIVE for normal native reads. **Next:** optional user compile/flash W2R53, preserve hard calendar setting HOLD; proposed physical controller write/create/delete/date/night-mode extensions must each depend on genuine XTR evidence and explicit separately bounded user-initiated scope. No new TX architecture, no mandatory room sensor disconnect, no repeated read validation. Controller-only outage auto-rejoin work deferred without forcing a controller restart.
6. **One native S92/M6 controller-only outage recovery (W2R52 private, SOURCE / OFFLINE TESTED — PREPARED / NOT RUN).** Source-confirmed integration defect in locally verified W2R51: an active native session can retain old controller authority when controller 0x02 and native DCM traffic disappear but a room sensor 0x0A keeps the valid RS485 bus active; existing cold stage1 also accepted a live 0x0A as boot return. W2R52 integrates a source-qualified 5s 0x02/native absence into the same existing S92/M6 owner. Without explicit user experimental enablement (default OFF), it only revokes stale ownership/caches to RX-only and DE LOW; with a separately user-enabled, 120s one-shot Configuration control, that exact controller-only episode can re-enter the previously existing guarded cold path, where only a fresh valid 0x02 can qualify boot return. This does not add a new UART/TX owner, Modbus frame, register, challenge, or setting-write authority. **XTR W2R52 has now been actually OTA-flashed and live verified for M6=5/CURRENT4/4/CAL12/12 normal read with CRC_DIFF0/resync0/drops0 (15:43–15:46 on 2026-10-30).** Genuine 0x02-only loss and newly scoped recovery were NOT physically tested; their experiment remains PREPARED / NOT RUN. W2R51 remains XTR locally verified for ordinary native read/OTA refresh; W2R50 is the zero-resync OTA rollback. Existing full-bus-loss recovery, FC16/FC03/current/calendar, CRC/DE/ABORT guards and setting write HOLD remain. **Next:** keep W2R52 in ordinary native read operation and the new 120s recovery one-shot OFF. Do not repeat already positive OTA/current/calendar tests or force power loss; act only on actual naturally observed controller-only outage evidence. No room sensor disconnection or HA/calendar parameter setting writes.

Development firmware and private OEM-derived protocol materials are not published in this public repository. The canonical detailed status and evidence remain under `Research/`; this public roadmap describes priority and availability only.

## Features

The integration is organized into four firmware versions, each offering a different level of access to the heat pump.

### Firmware versions

| Version | Monitoring | Control | Access level |
|---|---|---|---|
| **Passive** | Yes | No | Read-only, passive bus monitoring |
| **DCM Read Only** | Yes | No | Read-only, using native DCM communication |
| **Write User (soon)** | Yes | Yes | User-accessible settings |
| **Write Service (soon)** | Yes | Yes | User and service-menu settings |

### 1. Passive

**Passive monitoring without transmitting any data to the heat pump.**

This version listens to existing RS485 communication and extracts available sensor readings and controller information.

- No RS485 transmission
- Temperature and operational monitoring
- Heating settings and status where available
- Home Assistant sensor integration
- Suitable for basic monitoring

### 2. DCM Read Only

**Read-only integration using the native Thermia DCM communication protocol.**

This version is intended to provide more complete monitoring by supporting native communication and synchronization with the controller.

- All supported passive monitoring features
- Native DCM communication
- Controller synchronization
- Access to additional parameters and status information where supported
- No parameter changes

### 3. Write User 

**Beining tested at the moment and will be realeased soon**

**Monitoring and control of settings available through the heat pump's normal user interface.**

This version is intended to allow Home Assistant to change user-accessible settings documented in the Thermia operating interface.

Examples include:

- Room temperature setpoint
- Heating curve
- Minimum and maximum heating temperatures
- Heating stop temperature
- Heating curve adjustments
- Hot water settings and operating modes
- Heat pump operating mode
- Other user-accessible settings supported by the controller

These controls remain subject to protocol validation and controller support.

### 4. Write Service

**Beining tested at the moment and will be realeased soon**

**Integration of user-accessible settings and parameters available through the Thermia SERVICE menu.**

This version is intended to expose supported service-level settings in addition to the normal user controls.

Examples include:

- All supported Write User functions
- Heating system configuration
- Auxiliary heating parameters
- Hot water service settings
- Cooling configuration
- Circulation pump and Optimum settings
- Shunt group configuration
- Other available SERVICE menu parameters

Service-level access does not imply bypassing the controller's built-in safety functions. Functions requiring manual commissioning or special operating conditions retain those requirements.

**Availability:** Passive and DCM Read Only configurations are currently published. Write User and Write Service are planned versions; controller parameter writes are not yet released as validated functionality.

### Monitoring

Supported telemetry in the underlying development includes:

- Outdoor and indoor temperatures
- Room temperature setpoint
- Heating supply and return temperatures
- Domestic hot water temperature
- Heating curve and related settings
- Compressor frequency and electrical current
- Fan speed
- Condenser temperatures
- Compressor discharge temperature
- High-pressure readings
- Expansion valve information
- Operating and controller status
- Communication and bus-health diagnostics

Some values depend on the heat pump configuration, available bus messages and firmware variant.

### Local integration

- Direct RS485 communication
- ESPHome-based firmware
- Native Home Assistant API integration
- No Thermia cloud account required
- Modbus RTU-like frame decoding with CRC validation
- Passive monitoring option without bus transmission
- Local caching of selected controller settings


## Hardware requirements

You only need a few inexpensive components to get started.

### What you'll need

| Component | Description |
|---|---|
| ESP32 board | [Waveshare ESP32-S3-RS485-CAN](https://www.waveshare.com/esp32-s3-rs485-can.htm) |
| RJ45 breakout | RJ45 male to 8-pin screw-terminal adapter |
| Wires | Two short wires for RS485 A and B |
| Power supply | USB cable and compatible USB charger |
| Multimeter | Recommended for verifying the electrical connections |

The **Waveshare ESP32-S3-RS485-CAN** is the board used for this project. It combines an ESP32-S3 microcontroller, Wi-Fi connectivity and an integrated RS485 interface.

No separate RS485-to-USB converter or additional microcontroller is required.

You can use a stripped Ethernet/UTP cable instead of an RJ45 breakout adapter, but I recommend the breakout adapter. It makes the wiring cleaner and easier to verify or change.

### Wiring

The following connections are used for the Thermia iTec XTR M:

| Thermia RJ45 pin | Signal | Waveshare connection |
|---|---|---|
| Pin 1 | RS485 A (+) | A |
| Pin 3 | RS485 B (−) | B |

Only these two communication wires are required for this setup.

The ESP32 is powered separately through USB.

**Important:** The RJ45 connector also carries power. Do not connect the heat pump's power supply pins directly to the Waveshare RS485 terminals.

I strongly recommend using a multimeter to verify the electrical connections before connecting the Waveshare.

## Installation guide

### Step 1 — Prepare your hardware

You will need:

- Waveshare ESP32-S3-RS485-CAN
- RJ45 male to 8-pin breakout adapter
- Two short wires
- USB cable and USB power supply
- Multimeter (recommended)

For initial setup, leave the Waveshare disconnected from the heat pump.

### Step 2 — Install ESPHome

ESPHome is used to compile and upload the firmware to the Waveshare ESP32.

You can use ESPHome through Home Assistant or a standalone ESPHome installation.

Visit [esphome.io](https://esphome.io/) for installation instructions.

If you're already running Home Assistant, using the ESPHome Device Builder is generally the easiest option.

### Step 3 — Download the firmware

Choose one of the YAML configurations from the [Thermia iTec XTR](Thermia%20iTec%20XTR/) directory.

**Passive read-only**

[`thermia_itec_xtr_passive_1.0.yaml`](Thermia%20iTec%20XTR/thermia_itec_xtr_passive_1.0.yaml)

The receive-only version, recommended as a starting point.

**DCM read-only**

[`thermia_itec_xtr_DCM_readonly_1.0.yaml`](Thermia%20iTec%20XTR/thermia_itec_xtr_DCM_readonly_1.0.yaml)

The DCM-related development version. Review its operating requirements and supported functionality before use.

### Step 4 — Configure ESPHome

Create a new ESPHome device using the selected YAML configuration.

Configure the required secrets for:

- Wi-Fi network name and password
- Home Assistant API encryption key
- ESPHome OTA password
- Fallback access point password

The YAML uses the following secret names:

```yaml
wifi_ssid:
wifi_password:
thermia_api_encryption_key:
thermia_ota_password:
thermia_fallback_password:
```

Add the corresponding values to your ESPHome `secrets.yaml` file.

Do not publish your actual passwords or encryption keys.

The YAML already contains the ESP32 hardware configuration and Thermia communication settings.

### Step 5 — Flash the ESP32

Connect the Waveshare ESP32-S3-RS485-CAN to your computer using a USB data cable.

In ESPHome:

1. Select the device and open its configuration.
2. Compile the firmware.
3. Choose the USB installation method.
4. Flash the firmware to the ESP32.
5. Verify that the device connects to Wi-Fi.

The first upload is typically performed over USB. Subsequent updates can be installed through ESPHome OTA.

### Step 6 — Verify the Thermia RJ45 pinout and connect the gateway

Before connecting the Waveshare board to your Thermia heat pump, I strongly recommend checking the electrical pinout of the Thermia RJ45 communication port using a multimeter.

**Expected RJ45 pinout**

| RJ45 pins | Expected function |
|---|---|
| 1 + 2 | RS485 A |
| 3 + 4 | RS485 B |
| 5 + 6 | Ground / reference (GND) |
| 7 + 8 | +12 V supply |

**How to check with a multimeter**

1. Leave the Waveshare disconnected and keep the Thermia powered so the port voltages can be measured.
2. Set your multimeter to **DC voltage (V⎓)**, with a range of at least 20 V.
3. Using the RJ45 breakout adapter, place the black probe on pin 5 (expected GND).
4. Measure pin 7 with the red probe. You should expect approximately **+12 V DC**.
5. Measure pins 1 and 3 separately relative to pin 5. These are expected to carry RS485 data signals, generally measuring **around 4 V DC**.
6. Optionally measure between pins 1 and 3 to check for a differential RS485 voltage.

RS485 voltage readings depend on bus activity and biasing, so there is no single guaranteed voltage to expect on the data pins. A multimeter can help identify the power and reference connections, but cannot conclusively determine the RS485 A/B polarity.

**Do not connect the Waveshare if your measurements contradict the expected pinout.** Avoid accidentally bridging adjacent RJ45 terminals with the multimeter probes.

Once verified, connect:

- Thermia RJ45 pin 1 → Waveshare RS485 A
- Thermia RJ45 pin 3 → Waveshare RS485 B

Leave all other RJ45 pins unconnected to the Waveshare and power it separately using USB.

The ESP32 should now begin receiving communication from the heat pump.

### Step 7 — Add the device to Home Assistant

With the Waveshare connected to your Wi-Fi network, Home Assistant should be able to discover it through the ESPHome integration.

If automatic discovery doesn't work:

1. Open **Settings → Devices & services** in Home Assistant.
2. Add the ESPHome integration.
3. Enter the device's IP address or hostname.
4. Complete the connection using the configured API encryption key.

Once connected, the available Thermia sensors should appear as Home Assistant entities.

The exact number of sensors depends on the firmware variant and the data available on the bus.

## Supported hardware

### Heat pump

| Component | Tested configuration |
|---|---|
| Manufacturer | Thermia |
| Outdoor unit | iTec XTR M |
| Indoor unit | Total Compact |
| Controller generation | Pre-Genesis |
| Communication | Internal RS485 bus |

Other Thermia iTec XT/XTR models and older Danfoss-derived platforms may share parts of the protocol, but compatibility has not been established for every model.

This project should not be assumed compatible with the newer Thermia Genesis platform.

## Home Assistant integration

The ESP32 connects to Home Assistant through the native ESPHome API.

Once correctly configured and running, the gateway can expose supported heat pump sensors and diagnostic information as Home Assistant entities.

The objective is to support local dashboards, history, automations and, eventually, validated control functions without relying on Thermia Online.

The exact entity list depends on the chosen YAML configuration and the information available from the heat pump.

## Protocol research

The Thermia iTec XTR uses a proprietary communication architecture built around Modbus RTU-like messages.

Development has identified several communication addresses and their likely roles.

| Address | Observed role |
|---|---|
| `0x02` | Main controller state and communication |
| `0x06` | Expansion/accessory interface |
| `0x0A` | Room sensor communication |
| `0x0F` | Controller settings and state blocks |
| `0x1E` | Outdoor-unit communication and telemetry |

A substantial portion of the monitoring protocol has been mapped through real bus captures and controlled experiments.

The original Thermia Connect firmware is also being studied to understand native initialization, synchronization, polling, session management and recovery behaviour.

Not every observed register or message has a confirmed meaning.

## Safety and limitations

This is an independent reverse-engineering project, not an official Thermia product.

Communication with the internal bus can potentially interfere with normal heat pump operation if implemented incorrectly.

The project distinguishes passive monitoring, native protocol responses and controller parameter writes.

Parameter writes from Home Assistant are not yet enabled as a generally supported feature.

The integration is intended to preserve the heat pump's own controller logic, interlocks and safety mechanisms rather than bypass them.

Use at your own risk.

## Related projects and acknowledgements

Special thanks to [Piotr Romanowski](https://github.com/piotr-romanowski) for his independent [`thermia-bus-sniffer`](https://github.com/piotr-romanowski/thermia-bus-sniffer) project and valuable protocol research on related Thermia/Danfoss hardware.

A big thank you also goes to **everyone who contributed to this project by sharing logs, bus recordings, protocol captures, technical findings and feedback**. These contributions have been incredibly valuable in understanding the Thermia communication protocol, comparing behaviour across different heat pump models and moving the project forward.

### Related projects

- [Thermia ATEC — ESP Emulator of DCOM](https://github.com/fclauson/Thermia-ATEC-ESP-emulator-of-DCOM) by fclauson
- [Thermia Bus Sniffer](https://github.com/piotr-romanowski/thermia-bus-sniffer) by Piotr Romanowski
- [Thermia Home Assistant Integration](https://github.com/klejejs/ha-thermia-heat-pump-integration)
- [Thermia Online vs. Direct Modbus — Discussion #143](https://github.com/klejejs/ha-thermia-heat-pump-integration/discussions/143)

### Tools and platforms

- [ESPHome](https://esphome.io/)
- [Home Assistant](https://www.home-assistant.io/)

## Disclaimer

This project is not affiliated with, endorsed by or supported by Thermia, Danfoss or their related companies.

Thermia and Danfoss are trademarks of their respective owners.

---

**Development platform:** Thermia iTec XTR M / Total Compact  
**Integration:** ESP32-S3 · ESPHome · Home Assistant  
**Repository:** [ryckema/Thermia_itec](https://github.com/ryckema/Thermia_itec)
