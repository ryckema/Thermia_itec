# Thermia iTec XTR — ESPHome & Home Assistant

**Local monitoring and control of the Thermia iTec XTR heat pump using ESP32, ESPHome and Home Assistant.**

This project provides a local, cloud-independent integration for Thermia iTec XTR heat pumps by communicating directly with the heat pump's internal RS485 bus.

The integration is developed and tested on a **Thermia iTec XTR M with Total Compact indoor unit**, using an ESP32-S3 with an RS485 interface.

## Features

The integration is organized into four firmware versions, each offering a different level of access to the heat pump.

### Firmware versions

| Version | Monitoring | Control | Access level |
|---|---|---|---|
| **Passive** | Yes | No | Read-only, passive bus monitoring |
| **DCM Read Only** | Yes | No | Read-only, using native DCM communication |
| **Write User** | Yes | Yes | User-accessible settings |
| **Write Service** | Yes | Yes | User and service-menu settings |

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

## Roadmap

**2026-10-29 — W2R29 Operating Mode D3 integrated PRIVATE firmware — SOURCE / OFFLINE TESTED; PREPARED / NOT RUN.** Starting from latest LIVE / LOCALLY VERIFIED W2R28F1 (Heating 10 descriptors 27/27, Hot Water D13+D14 4/4, Cooling six descriptors 18/18; these milestones remain closed), prepared one complete private W2R29 ZIP with exact full ESPHome YAML, manifest SHA256, compile/user-flash instructions, bounded experiment, ABORT, W2R28F1 rollback + W2R28/W2R27/W2R25F4/W2R24 reserve. Source-mapped Operating Mode descriptor **D3 register `0x0553`, word13 of `0x0546/20`**, canonical OEM `0x0708` selector **CURRENT W2 bit0 / DESIRED W0 bit0**, exact 45-byte FC03 response and one-word-pinned page added into the existing single S92 UART/RX/DE sender / OEM ledger, owner + same epoch + cache + CRC + FC16 controller-semantic receipt guards, one physical attempt per deliberate HA edit and no auto retry. Existing HA `01 Operation | 01 Mode` reuses original entity ID, only user trial targets **Auto=1 ↔ Compressor=2** allowed; other OEM-observed modes Off=0, Auxiliary Heater=3, Hot Water=4 remain HOLD in this initial bounded experimental scope. Cooling D19 and all other nonvalidated writes remain HOLD. In same integrated revision fixed ONLY native `0x044D/0x044E` Cooling hysteresis readback unit labels K→°C (raw /10 unchanged). YAML parser PASS; original HA/global/script IDs/sections retained; 225 embedded lambda delimiter check PASS; exactly one `thermia_uart.write_array`; 0546/20 source/selector and 45-byte page/semantic acceptance guards offline reviewed; ZIP manifest and CRC integrity PASS. **NOT ESPHome TARGET COMPILED / NOT FLASHED / NOT LIVE / NOT LOCALLY VERIFIED for Operating Mode.** No physical TX authority derived from this preparation, user must compile then manually flash and explicitly enable. **CURRENT MILESTONE:** Write User Operating Mode. **DELIVERABLE:** integrated private W2R29 full firmware ZIP PREPARED / NOT RUN. **REAL BLOCKER:** first actual controller-origin FC16 semantic acceptance for D3 mode 0553, and ESPHome target compilation pending. **ONE NEXT ACTION:** user compiles W2R29, user-flashes only on success, then if operationally appropriate performs ONE bounded reversible Auto→Compressor→Auto test, expecting exact `CONTROLLER_ACCEPTED d=3 actual=2/1`; ABORT immediately if unsafe, restore controller state via OEM panel if necessary, firmware rollback cannot restore controller parameters. Do not repeat the previously validated 49/49 Heating/HotWater/Cooling user writes.



**2026-10-29 — W2R28F1 XTR live Cooling closure — COMPLETE / POSITIVE, FLASHED / LIVE / LOCALLY VERIFIED for all six currently authorized Cooling descriptors (D2, D15, D16, D17, D18, D20).** User-provided W2R28F1 5,000-line local ESPHome capture from 01:51:42–01:55:32 confirms new software is running (firmware build reports MAIN04-W2R28F1). Explicit user enable at 01:53:44.164 epoch=11292. **Eight first-attempt physical S92 desired-page sends to 0x0442/13**, each 31 bytes and one selected-word change, each semantically confirmed by independent controller-origin FC16 `CONTROLLER_ACCEPTED` (8/8): D18 `0x0449` 20→22 accepted 01:54:00.170, 22→20 01:54:04.672; **D15 `0x0442` 1→0 01:54:09.078, 0→1 01:54:22.060**; **D2 low room hysteresis `0x044D` raw10→11 (1.0→1.1 °C) 01:54:48.060, raw11→10 (1.1→1.0 °C) 01:54:56.772**; D20 high room hysteresis `0x044E` raw10→33 (1.0→3.3 °C) 01:55:09.764, raw33→10 (3.3→1.0 °C) 01:55:18.468. Physical attempts=1 and receipts=1 on all eight; no SELECTOR_ABORT, UI_DESIRED_QUEUE or blind retries in this capture. D15 old EXP379 double-queue conflict **fixed and proven live**, not merely offline; D2 now live proven. Previous W2R28 D16 2/2, D17 4/4, D18 2/2, D20 2/2 remain independently proven: **18/18 controller-semantic Cooling user writes across both captures** (D2 2, D15 2, D16 2, D17 4, D18 4, D20 4). Posttest D15=ON(1), D2=1.0°C, D18=20min, D20=1.0°C; D17 previously ended at 25°C and must NOT be described as restored to 26. **D19 Room Sensor remains READ-ONLY/HOLD** pending direction-of-value evidence, a NONBLOCKING UNKNOWN for proven six-parameter Cooling scope. Earlier blocked user attempts before enabling: `SESSION_ENABLE_DENIED ... idle=0` during calendar-owned traffic, subsequent explicit enable succeeded; no unauthorized TX. The native HA readback sensors for both low/high hysteresis still display K; **UI unit defect**: true Thermia UI unit is °C; raw deciunit conversion is correct and no physical write code change needed. Sampled M6=5, CURRENT 4/4, CRC_DIFF=0, RX drops=0, parser resync=0; calendar page ACK continues. **CURRENT MILESTONE:** Write User — authorized Cooling group **COMPLETE / POSITIVE**. **DELIVERABLE:** W2R28F1 live six descriptors (18/18 group physical user writes cumulatively), verified shared S92 writer. **REAL BLOCKER:** none for currently authorized Cooling; D19 mapping direction remains NONBLOCKING UNKNOWN and held. **ONE NEXT ACTION:** move to next source-backed Write User **Operating Mode** group in the existing sole S92 engine; correct two hysteresis readback units from K to °C in that next integrated firmware, without retesting closed Heating/Hot Water/Cooling.



### 2026-10-29 W2R28 Cooling LIVE results and W2R28F1 targeted source fix
**OBSERVED FACTS / PROVEN — user XTR M controller 2.4.2 log 01:09–01:13:** With explicit `USER_WRITES_ENABLED epoch=11308`, sole S92 physical writer sent 10 exact `0x0442/13` (31-byte) changed-word desired pages, each followed by matching *controller-origin semantic* FC16 `CONTROLLER_ACCEPTED`: D16 `0x0443` 18→17→18 (2/2); D17 `0x0445` 26→25→31→26→25 (4/4); D18 `0x0449` 20→19→20 (2/2); D20 `0x044E` raw10→11→10 (2/2). **All 10/10 succeeded on first physical attempt, no blind retry**; session M6=5 CURRENT 4/4 and sampled CRC_DIFF=0, RX drops=0, parser resync=0. D17 ended at **25**, not original 26: do not assume rollback. **D15 `0x0442` 1→0 failed**: OEM ledger armed at 01:12:33 but old EXP379 `UI_DESIRED_QUEUE ... dirtyMask=0001` also armed and `SELECTOR_ABORT ... legacyIdle=0` followed; 0→1 UI reversal likewise entered EXP379. No D15 semantic acceptance, **RUNNING / PARTIAL** for overall W2R28 Cooling group; D15 **COMPLETE / NEGATIVE** for this specific attempted path, not proven incompatible with controller. **D2 `0x044D` Room Hysteresis Low** already source-mapped at page 0442/13 word11, W3/W1 mask 0010, raw5..50 (0.5..5.0 K); pre-F1 HA `04 Cooling | 06 Room Hysteresis Low` was `HA_SETTING_HELD` and did not use OEM ledger. Same page/selector and analog D20 make protocol compatibility **STRONGLY SUPPORTED**, NOT PROVEN until controller FC16.
**FIX delivered privately:** W2R28F1 complete ZIP SOURCE / OFFLINE TESTED — PREPARED / NOT RUN: route D2 through existing exact source/epoch S92 selector, one-word 13-word page, full FC16 readback and ABORT; remove competing EXP379 queue from BOTH D15 ON and OFF HA handlers. D19 remains TX HOLD. Existing W2R28 Heating/HW and D16/D17/D18/D20 paths preserved; no second UART writer. YAML parses, original 1099 unique IDs retained, 225 C++ lambdas bracket/quote smoke-check, exact D2 canonical geometry, D15 queue removal, sole owner count and ZIP SHA integrity PASS. Not ESPHome target compiled, not flashed or live validated. ZIP includes W2R28 source, W2R27, W2R25F4 and W2R24 rollback. **NEXT ACTION:** user compiles W2R28F1 and only if successful user-flashes; one bounded reversible D2 1.0→1.1→1.0 K controller-origin semantic confirmation and a D15 1→0→1 only if operationally appropriate; do **not** repeat the 10 successful Cooling writes.



**2026-10-28 W2R28 Cooling group source integration — SOURCE / OFFLINE TESTED; PREPARED / NOT RUN.** Created one complete **private** ESPHome firmware ZIP based on the actually LIVE W2R27 D13/D14 (4/4 controller-semantic writes), preserving the W2R25F4 Heating 10/10, 27/27 baseline. Five source-mapped Cooling user descriptors **D15 `0x0442` word0 Enabled 0/1; D16 `0x0443` word1 Desired Temperature 7–40°C; D17 `0x0445` word3 Active Above 10–50°C (preserved Heating Stop+3K constraint); D18 `0x0449` word7 Cooling Time 5–40min; D20 `0x044E` word12 Room Hysteresis High raw 5–50 (0.5–5.0K)** now use existing sole S92 TX and OEM ledger, exact `0x0442/13` 31-byte selected-word page and `0x0708` selector W1/W3 `0x0010`, same-epoch CURRENT/cache, physical boundary, CRC, controller-origin FC16 semantic readback, no auto-retry, ABORT. **D19 `0x044C` Room Sensor write remains ON HOLD** owing to unverified meaning of 0/1 direction. All other unvalidated settings remain HOLD; no additional UART reader/writer or bypass of session safety. Changed stale build label to W2R28 and recategorized existing D14 HA entity name as Hot Water without changing IDs. One bounded user-initiated live Cooling trial is prepared (D18, D16, D20, D17 then D15 sequentially; each reversibly), rollback W2R27, W2R25F4 and W2R24 packaged. Offline YAML structure PASS, 1099 unique IDs, 225 C++ lambda delimiter balance PASS, existing 1 UART writer and HA IDs unchanged, source geometry and selector CRC checked, ZIP integrity PASS. **NOT ESPHome TARGET COMPILED / NOT FLASHED / NOT LIVE / NOT LOCALLY VERIFIED.** Existing W2R27 D13+D14 remains COMPLETE / POSITIVE; existing Heating milestone remains closed. **CURRENT MILESTONE:** Write User Cooling group. **DELIVERABLE:** private W2R28 full source ZIP, PREPARED / NOT RUN. **REAL BLOCKER:** first real controller-origin FC16 semantic acceptance for Cooling is still unverified (and target compile pending). **ONE NEXT ACTION:** user compiles W2R28 and, only after success, user-flashes and conducts the single bounded reversible Cooling group test with ABORT/rollback.



**2026-10-28 W2R27 Hot Water user group COMPLETE / POSITIVE — FLASHED / LIVE / LOCALLY VERIFIED for both mapped descriptors, 4/4 controller-semantic physical writes across two user captures.** D13 Hot Water Mode `0x042F`, `0x042E/15` word1: 1→0 and 0→1 on 22:46:39–53, each a 35-byte S92 desired page (single changed word) followed by matching genuine controller-origin FC16 `CONTROLLER_ACCEPTED d=13 actual=0/1` (2/2). D14 Startup HT `0x0433`, same page word5: explicit HA number `02 Heating | 20 Startup HT` edited 5→6 at 22:54:41.624, one physical desired page 22:54:45.607, controller-origin `CONTROLLER_ACCEPTED d=14 actual=6` 22:54:46.262; restored 6→5 at 22:54:56.471, one physical desired page 22:54:58.605, `CONTROLLER_ACCEPTED d=14 actual=5` 22:54:59.216 (2/2). Selected word only (`deltaWords=1`), 35-byte page, sole S92 writer DE LOW, no blind retries. HA number reconciled 6 then 5. Native M6=5, CURRENT 4/4 confirmed (snapshot gen 7), sampled CRC_DIFF=0, RX drops=0, parser resync=0; calendar-owned traffic continues, no observed regression. **D14 semantic register acceptance PROVEN; physical meaning/unit of Startup HT still UNKNOWN**. Nonblocking UI/source defects: D14 HA number is miscategorized `02 Heating | 20 Startup HT` instead of Hot Water, and `Thermia Firmware Build` text still says W2R25F4 even though `[W2R27] USER_DIRECT_EDIT` and live D13/D14 TX prove updated code is running. No need to reflash solely for labels. W2R25F4 remains baseline of independently verified Heating 10/10 27/27; W2R27 now proven for Hot Water D13+D14 in same shared owner. **CURRENT MILESTONE:** Write User Hot Water D13/D14 COMPLETE / POSITIVE. **DELIVERABLE:** W2R27 live 4/4 semantic writes, restored D13 Eco and D14 5. **REAL BLOCKER:** none for these tested Hot Water descriptors; other groups still outside authorized scope. **ONE NEXT ACTION:** use roadmap order to integrate the next evidenced Write User **Cooling** descriptor group into the same S92 engine as one private integrated firmware, repair labels in that normal revision, keep physical TX user-initiated and bounded and leave service writes on hold.





**2026-10-28 W2R27 first local XTR LIVE evidence — D13 COMPLETE / POSITIVE; D14 PREPARED / NOT RUN.** User ESPHome 5000-line capture 22:43:00–22:46:59, iTec XTR M 3N controller 2.4.2. Before explicit enable: `USER_WRITE_DENIED d=13 grant=0 ... NO_TX` at 22:46:11/22:46:22 (correct guard). At 22:46:32 `USER_WRITES_ENABLED epoch=11230 HW_D13_D14_TRIAL=1`. **D13 Hot Water Mode reg 042F:** 1→0, user edit 22:46:37, descriptor page 042E/15 W3/W1 0008, physical desired page 22:46:39.883 (35 bytes, 1 changed word, S92 DE LOW), genuine controller-origin FC16 `CONTROLLER_ACCEPTED d=13 actual=0` 22:46:40.462. Reversal 0→1 user edit 22:46:52, physical page 22:46:52.885, `CONTROLLER_ACCEPTED d=13 actual=1` 22:46:53.482. **2/2 physical sends, 2/2 semantic acceptances, no blind retry.** Maintained M6=5, CURRENT 4/4 (snapshot generation 5), AUTO calendar 12/12 observed 22:46:08, sampled CRC_DIFF=0, RX buffer drops=0, parser resync=0. **D14 0433 has NO user edit/physical TX/semantic acceptance in this log; remains PREPARED / NOT RUN.** Diagnostics `Thermia Firmware Build` still prints `W2R25F4` at 22:46:37 even while active `W2R27` physical code and D13 042E/15 are explicitly logged; **stale build label is a nonblocking source defect** to fix in next firmware revision, not evidence of old runtime or write failure. W2R25F4 remains latest baseline fully validated for Heating; W2R27 is FLASHED / LIVE / LOCALLY VERIFIED for D13 only, *not* D14 or broader hot water functionality. **CURRENT MILESTONE:** Hot Water Write User. **DELIVERABLE:** W2R27 D13 COMPLETE / POSITIVE (2/2), D14 pending. **REAL BLOCKER:** no D14 live semantic result; unit uncertain. **ONE NEXT ACTION:** user-initiated bounded reversible D14 Startup HT 5→6→5 on same W2R27 session, with controller-origin FC16 confirmation and ABORT/rollback as supplied; no new compile/flash and no D13 retest.

**2026-10-28 W2R27-HW-D13-D14-S92 — SOURCE / OFFLINE TESTED; PREPARED / NOT RUN.** Integrated two source-mapped Hot Water user descriptors D13 `0x042F` (mode 0/1/2) and D14 `0x0433` (Startup HT 1–30, unit uncertain) on controller page `0x042E/15` via the *existing* sole S92 UART/RX/DE physical writer and OEM descriptor ledger, not the separate EXP378 queue. Added 0708 desired/current selector W1/W3 mask `0008` (`1801/1803`), one selected-word 35-byte desired page guarded by CRC/epoch/M6=5/CURRENT/owner, and controller-origin full 15-word FC16 acceptance/negative-release/ABORT; no blind retries. Existing explicit user enable button and all HA entity IDs preserved; Heating D1/D4–D12, CURRENT 4/4, calendar 12/12, native session behavior and rollback retained. Complete **private** firmware ZIP generated with manifest, experiment instructions and unchanged W2R25F4 and W2R24 rollbacks. Offline PyYAML parse, 1099 unique IDs, 225 C++ lambdas delimiter checks, unchanged sole UART writer, selector CRC and ZIP integrity PASS. **NOT ESPHome TARGET COMPILED; NOT FLASHED; NOT LIVE / LOCALLY VERIFIED.** W2R25F4 remains last LIVE / LOCALLY VERIFIED baseline (Heating 10/10, 27/27), and W2R26 Hot Water is COMPLETE / NEGATIVE physical TX. **REAL BLOCKER:** first true controller-origin semantic FC16 acceptance for D13/D14 remains unverified on the XTR. **ONE NEXT ACTION:** user compiles W2R27; upon successful build, user-flashes and initiates bounded reversible D13 then D14 edits with ABORT/rollback available; review actual controller readbacks for GO/FIX/NO-GO.




**2026-10-28 live W2R26 attempt: COMPLETE / NEGATIVE for actual Hot Water control; COMPLETE / POSITIVE for intent staging only.** Two overlapping user ESPHome excerpts (21:40:53–21:44:27) show genuine native M6=5 recovery, CURRENT 4/4 and calendar 12/12; requests for D13 042F Hot Water Mode 1→0 at 21:43:39 and 21:44:09, and 1→2 at 21:44:22, each log `HW_MODE_PREPARED ... NO_TX=1`. There is **zero** `GENERIC_PAGE_TX_EXECUTED`, zero `CONTROLLER_ACCEPTED` and no Hot Water controller parameter change. This is the intentional physical TX HOLD in W2R26, not controller refusal. Earlier W2R26 PREPARED / NOT RUN status superseded for staged preview but NOT for parameter TX. Heating W2R25F4 10/10 27/27 baseline remains last user-verified real write firmware. **REAL BLOCKER:** Hot Water descriptors are not integrated through one S92 guarded physical selector/desired-page and controller FC16 semantic acceptance path. **ONE NEXT ACTION:** implement consolidated supported Hot Water descriptors in same engine and deliver ONE full firmware ZIP with bounded user-triggered activation, ABORT and rollback; do not offer preview-only ZIP as physical-write test.



**2026-10-28 W2R26 integrated Hot Water Mode preparatory candidate — SOURCE / OFFLINE TESTED; PREPARED / NOT RUN.** Built one private complete ZIP on unchanged user-verified W2R25F4 Heating 10/10 baseline. Existing Home Assistant Hot Water Mode control (`0x042F` word 1 of controller-origin `0x042E/15`, descriptor 13; Comfort=0 / Eco=1 / Holiday Eco=2) now stages only one RAM-scoped intent after native M6=5, session/epoch, current 4/4, owned source/cache freshness and OEM geometry checks. It restores confirmed controller selection in HA rather than pretending to have changed controller. Preview auto-invalidates on fresh controller 042E FC16. The legacy EXP378 queue remains disabled; no new UART/RX/DE writer, no new `.write_array`, no physical parameter TX, no changes to Heating path/ABORT/rollback. Offline YAML parse and ZIP integrity pass; NOT ESPHome TARGET COMPILED / NOT FLASHED / NOT LIVE. **Real blocker:** existing shared OEM physical selector/desired-page/FC16 acceptance remains scoped to Heating 03E8. Integrating descriptor 13 atomically into that same guarded ledger is still required. **ONE NEXT ACTION:** implement descriptor 13 in existing shared selector, desired TX, semantic FC16 and ABORT chain, then deliver bounded user-initiated Hot Water experiment; avoid speculative parallel EXP378 writer. Keep HA parameter writes for Hot Water ON HOLD until proven and authorized.

**LATEST 2026-10-28: W2R25F4 Heating Write User COMPLETE / POSITIVE, LIVE / LOCALLY VERIFIED (10/10 descriptors, 27/27 physical user-write semantic acceptances).** Third XTR user log 2026-10-28 21:21:36–21:25:35: D5 Heating Maximum reg 03EA word2 user edit 40→42 at 21:25:18; one desired 03E8/14 physical page with deltaWords=1 at 21:25:28 (S92 DE=LOW); real controller-origin FC16 semantic CONTROLLER_ACCEPTED d=5 actual=42 at 21:25:29.481. M6=5; calendar AUTO_CAL_TWELVE_OWNED_ACKED 21:22:02 and 21:25:32; CURRENT 4/4 confirmed 21:22:26.991; sampled CRC_DIFF=0, RX drops=0, parser resync=0. Other d7/d8 preview attempts while busy correctly NO_TX. Combined three capture evidence: 27/27 physical Heating writes semantically accepted across all ten descriptors. **CURRENT MILESTONE:** Heating group complete. **DELIVERABLE:** unchanged W2R25F4. **REAL BLOCKER:** none for Heating; other Write User groups unvalidated. **ONE NEXT ACTION:** roadmap step 2, integrate the next OEM-supported Hot Water group in the same owner/ledger; no unvalidated physical TX without explicit bounded user initiation and ABORT/rollback. Earlier 9/10 status below is superseded, retained for history.

**Development status — 2026-10-28, updated with second live capture.** Private **W2R25F4 is FLASHED / LIVE / LOCALLY VERIFIED** on the iTec XTR M 3N, controller 2.4.2, for **NINE of TEN Heating descriptors**. First user capture (21:12:09–21:15:33) showed 19 physical Heating parameter writes with 19 controller-origin semantic FC16 confirmations across D1, D4, D7, D8, D9, D10, D11. The next independent user capture (21:16:16–21:20:05) shows **7 further physical Heating desired-page sends and 7 actual controller-origin FC16 semantic acceptances**: D6 0→1→0→1 (3), D12 22→21→22 (2), D8 0→1 (1), D7 0→1 (1). Combined observed evidence: **26/26 delivered pages accepted across NINE descriptors**, without ESP reboot between individual edits and with no arbitrary attempt/session cap. The last known alternative live rollback is W2R24; previous W2R25F4 SOURCE / NOT FLASHED statements in the historical section below are superseded by live evidence.

1. **Write User — Heating group (CURRENT MILESTONE, RUNNING / PARTIAL):** Per-descriptor **COMPLETE / POSITIVE, LIVE / LOCALLY VERIFIED** for **D1 `03E8` Heating Curve; D4 `03E9` Heating Minimum; D6 `03EB` Correction +5 (signed); D7 `03EC` Correction 0 (signed); D8 `03ED` Correction −5 (signed); D9 `03EE` Heating Stop; D10 `03EF` Reduced Temperature; D11 `03F0` Room Factor; and D12 `03F4` Room Setpoint**. **D5 `03EA` Heating Maximum is the ONE remaining PREPARED / NOT RUN descriptor**: no user-intent, delivered page or controller semantic readback for this register was observed in either capture. Every one of the seven new physical deliveries had an exact selected-register controller acceptance; D6 and D12 were changed and changed back and HA refreshed from real controller FC16. A transient D12 `PREVIEW_DENIED idle=0 / NO_TX` was followed by a successful later D12 delivery, consistent with one in-flight transaction protection. M6=5 and CURRENT `receiptPages=4/4` remained healthy, with V5 `CRC_DIFF=0`, RX drops=0, resyncs=0 in the second capture. The second capture contains a calendar read *arm* but does not independently prove 12/12 calendar *completion*; earlier proven calendar results are retained as historical evidence. Preserve single S92 UART/RX/DE owner, CRC/collision/freshness protections, explicit write enable, one physical desired page per separately user-initiated edit, controller-origin FC16 semantic acceptance, ABORT/rollback, session/CURRENT/calendar lifecycle and other register groups' TX HOLD. OEM automatic retry remains a documented unimplemented semantic difference, not a blocker for the verified edits. **REAL BLOCKER:** the missing live D5 acceptance. **ONE NEXT ACTION:** one user-initiated D5 Heating Maximum edit on **unchanged W2R25F4**, verify controller-origin 03E8/14 FC16 selected-word equality and unchanged other words, then GO/FIX/NO-GO for the full ten-descriptor Heating group; no new firmware or repeated microtests.

<details>
<summary>Historical development status before the W2R25F4 live evidence (superseded; retained for provenance)</summary>

**Development status (28 October 2026).** W2R24 is the current locally verified private XTR D1+D4 direct-HA heating-write baseline: both writes obtained genuine controller-origin FC16 semantic readback and changed only the selected heating word. W2R24 also has live logs for native M6 session, CURRENT 4/4 periodic refresh, and automatic 12/12 calendar re-reads across its normal freshness window. W2R19 remains the historical fully verified rollback, not a reason to regress the proven W2R24 D1/D4 path. Additional descriptor writes are not yet live verified; public Write User release remains incomplete.

1. **Write User — heating group (current):** **W2R24 D1 + D4 DIRECT HA WRITES LIVE / LOCALLY VERIFIED, COMPLETE / POSITIVE for each tested descriptor** (2026-10-28 XTR logs). D1 `0x03E8` word 0: `37→40`, controller-origin `0x03E8/14` FC16 with the other 13 words unchanged. D4 `0x03E9` word 1: after deliberate **ESP-only reboot**, user-initiated 17:48:01 `21→22`; 17:48:02 `DESCRIPTOR_RESOLVED id=4 page=03E8 count=14 reg=03E9 word=1` and `FAST_HIT`; one physical `DESIRED_PAGE_TX` at 17:48:03; 17:48:03.721 `CONTROLLER_ACCEPTED d=4 reg=03E9 actual=22 physicalAttempts=1 receipts=1`; genuine controller-origin 03E8 FC16 data before `[40,21,40,0,0,0,20,20,2,40,30,1,22,2]` and after `[40,22,40,0,0,0,20,20,2,40,30,1,22,2]`, exactly one word changed; Home Assistant Heating Minimum published 22. Previously blocked no-reboot D4 edit `used=1 NO_TX` remains correctly classified as one-shot guard enforcement, not controller rejection. M6 remained 5; automatic calendar owned 12/12 completed at 17:44:22 and again at 17:47:56; automatic four-page CURRENT refresh confirmed at 17:44:52 (generation 2). V5 CRC_DIFF=0 and RX drops=0 in this capture, although parser resync count 87 existed and was not seen to increment during the final write. **Preserve** existing one user-initiated desired-page physical TX per ESP boot, no parameter retry, S92 as single UART/RX/DE owner, CRC/integrity gates, ABORT/rollback, and other groups' write HOLD. **OEM comparison + integrated correction W2R25F4 (2026-10-28): SOURCE / OFFLINE TESTED; PREPARED / NOT RUN.** The original private Connect 2.1.105 `device_client/cm/modbus_server15.py` (verified identical to extracted appfs) uses a per-register pending update, sets alert/read-request bits, clears on controller-origin register-value equality, and offers retries up to three while controller still disagrees. Our F4 still requires explicit user initiation for each physical Heating desired-page TX (no autonomous retry on an ambiguous XTR bus), so automatic retry semantics are **not fully OEM-identical**; this is an intentionally disclosed bounded safety difference, not evidence of incompatibility. Critically, OEM `930/2.3.0-2.4.3/configurations.json` applicable to observed controller 2.4.2 establishes `1001` Heating Minimum **10–50 °C** (F3 incorrectly 20–40) and `1006` Heating Stop **0–30 °C** (F3 incorrectly 0–22). F4 corrects all six affected internal register validation paths and both HA sliders to OEM bounds, without changing controller interlocks. It also fixes a real remaining F3 selector-source inconsistency: `w2r8_native_source` demanded exact equality to an older owned CURRENT 4/4 snapshot even after a newer genuine same-epoch controller `03E8` FC16 had superseded that word, thus intermittently restricting the next valid manual edit to a legacy 15s fast-cache path. F4 accepts the newer genuine controller FC16 in this selector source, with existing epoch/CRC/TTL/integrity gates unchanged and diagnostic source aligned. Original physical UART owner remains single S92; CRC and 13 other unchanged word check, ABORT, explicit `Configuration | Enable Heating Writes (User Initiated)`, one physical desired page *per manual edit*, no attempt-count or global session-time cap, and hot-rejoin/CURRENT/calendar unchanged. Offline checked: YAML parse, 1,093 unique ESPHome IDs, one physical `.write_array`, 90 unchanged S92 sender callsites, OEM range extracted directly, original W2R24 and W2R19 rollback byte identical. **NOT ESPHome TARGET COMPILED, NOT FLASHED, NOT LIVE.** User F2 log 18:40–18:41 proves F2 actually FLASHED and achieved native M6=5, CURRENT 4/4, calendar 12/12; attempted D1/D4 edits were `session=0`, `grant=0`, `NO_TX` because explicit Heating session enablement had not occurred. This is NOT an observed controller rejection or evidence that the F3 cache issue caused the F2 denial. F2 status: RUNNING / PARTIAL for runtime, no parameter-write live proof; F3 SUPERSEDED / NOT RUN. W2R24 remains last D1/D4 LIVE / LOCALLY VERIFIED firmware. **ONE NEXT ACTION:** user target-compiles F4 and only on successful build initiates one user-activated multiwrite Heating acceptance; verify genuine controller-origin FC16 semantic receipts and owned CURRENT/calendar; no autonomous flashing. **REAL BLOCKER:** F4 target compile and consecutive-write live verification.

</details>

2. **Write User — additional register groups:** extend the same shared ledger to hot water, cooling, operating mode and calendar according to genuine controller evidence and user-accessible ranges. Do not create a second UART writer or parallel protocol engine.
3. **Native session reliability:** retain the verified DCM communication, CURRENT/cache freshness and calendar lifecycle. Investigate remaining restart/rejoin issues only when concrete evidence warrants it.
4. **Write Service:** later, separately scoped work. Preserve all controller interlocks and explicit authorization.

Parameter-write features that lack controller-semantic proof remain experimental; no parameter or physical transmission permission is inferred from a transport acknowledgement. Proprietary firmware source and private captures are not published.

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
