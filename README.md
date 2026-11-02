# Thermia iTec XTR — ESPHome & Home Assistant

**2026-11-02 W2R68FAST SOURCE / OFFLINE TESTED — PREPARED / NOT RUN:** Original private OEM CM930 driver updates holding register and per-page alert/read bits immediately, then waits for controller FC03/FC16, without fixed per-setting sleep. Source supports single F1 page containing multiple staged registers; not yet XTR LIVE proof. W2R68 integrates a disabled-by-default 45s, same-program explicit fast arm plus user Apply for 2–5 weekly F1 edits on ONE 33-word page, one physical S92 sender/CRC, all-field controller-origin FC16 and fresh F1 3/3 verification, no retry, no new UART owner. Normal W2R67 one-field writes unchanged, cross-page edits stay normal, EVU/Silent/TempReduction still NO_TX. OFFLINE YAML 1120 unique IDs, 286 lambdas, 8x5 F1 page maps, no additional TX callsites, ZIP CRC/SHA PASS. NOT ESPHome target compiled, flashed or live. CURRENT MILESTONE: OEM faster calendar writing; DELIVERABLE: full PRIVATE W2R68FAST ZIP and W2R67/W2R66/W2R64 rollbacks; REAL BLOCKER: single-page multiword semantic acceptance and normal post-W2R66 calendar refresh not yet LIVE; ONE NEXT ACTION: user manually flash and observe normal CAL12/12 before one explicitly user-armed reversible P5 dual-minute field trial.



**2026-11-02 W2R65 LIVE, W2R66 PRIVATE source fix — PREPARED / NOT RUN:** Real XTR W2R65 logs show M6=5, CURRENT4/4, automatic calendar12/12 completed 00:23:21.932, CRC_DIFF0 RXdrops0, genuine 0870/17 OEM lifetime counters and controller-confirmed D13 HolidayEco→Eco. User-initiated TOP-UP D25 (0x0430) sent exactly once at00:25:38, genuine FC16 returned0 with unchanged other words at00:25:39, and user saw DHW start (strong functional trigger evidence; exact OEM boost flag still open). Generic EXP444 marked persistent-target mismatch and left exp430_state=6, while OEMW lease revoked at00:26:33; native calendar/CURRENT read scheduler requires exp430_state=0 and therefore cannot schedule another refresh. W2R66 is a scoped existing-owner D25 one-shot terminal fix: after exact physical send and genuine same-epoch controller FC16 returning0, all other 14 words unchanged, clear logical exp430/OEMW leases and mark one-shot semantic status INCONCLUSIVE, no retry, no reset TX. Other persistent writes and single UART RX/TX/DE untouched; full PRIVATE ZIP W2R65+W2R64 rollback, YAML/1111 IDs/285 lambdas/ZIP CRC+SHA offline PASS. W2R66 NOT TARGET COMPILED/FLASHED/LIVE. New Operation modes still PREPARED / NOT RUN (user attempts NO_TX while owner busy). **CURRENT MILESTONE:** post-TOP-UP calendar recovery. **DELIVERABLE:** complete W2R66 private ZIP. **REAL BLOCKER:** actual post-fix calendar refresh not yet observed. **ONE NEXT ACTION:** user manually flashes W2R66, observes CAL12/12 and periodic read without repeating TOP-UP.



**2026-11-01 MAIN04-W2R65 integrated PRIVATE firmware — SOURCE / OFFLINE TESTED, PREPARED / NOT RUN:** Delivered ONE complete ZIP, W2R64HW latest XTR LIVE/LOCALLY VERIFIED YAML exact rollback. OEM Connect version matched 930/2.3.0-2.4.3 metadata identifies operation_mode register1363 (0x0553/current0546 word13, enum0..4), hot_tapwater_boost operation1072 (0x0430/current042E word2; 0→1 one-shot), operation/defrost lifetime registers2160,2162,2163,2166..2173 (0870/17), operation status2149 bits incl. TOP-UP/defrost, and additional live telemetry. W2R65 adds D25 to SAME sole S92/OEMW descriptor table, explicit user-armed 45s ONE edit for D25 TOP-UP and novel Operation Off/Aux/HotWater modes, no immediate TX, no retry/guessed reset, same 4/4 native and controller-origin FC16 acceptance guards. Existing verified Operation Auto↔Compressor, DHW D13/D24, Cooling six, Heating ten, calendar P4, all entities preserved. 42 passive OEM data+time HA sensors, missing 0870 page→NaN, age>300s→NaN, 2 provenance text sensors. NO expansion to Distribution Circuits 1/2 or Pool/Buffer. **Cooling standalone user Hysteresis remains OPEN / NO_TX** because no proven 2.4.2 register; six other Cooling writes already verified. Genuine 0870/17 was in local 2026-09-25 capture, not in W2R64 2026-11-01 log; runtime delivery OPEN. OFFLINE: YAML parsed, 1,111 unique IDs preserving 1,051 prior, 285 C++ lambda delimiter checks, same sole S92 sender, ZIP CRC/SHA PASS; **NOT ESPHome TARGET COMPILED/FLASHED/LIVE**. First novel Operation and TOP-UP controller-semantic acceptance **PREPARED / NOT RUN**; do not mark verified based on source metadata or transport ACK. **CURRENT MILESTONE:** integrated Write User+OEM data/time candidate. **DELIVERABLE:** private W2R65 full firmware ZIP. **REAL BLOCKERS:** first user-initiated XTR semantic proof of TOP-UP/novel modes; standalone Cooling Hysteresis register; genuine native 0870 freshness under current runtime. **ONE NEXT ACTION:** user manually compiles/flashes W2R65, verifies M6=5/CURRENT4/4/CRC and passive 0870 status before initiating ONE explicitly armed physical Operation/TOP-UP trial.



**2026-11-01 MAIN04-W2R64HW — COMPLETE / POSITIVE, FLASHED / LIVE / LOCALLY VERIFIED on Thermia XTR M 3N controller 2.4.2:** User-provided ESPHome 23:37–23:40 capture confirms native M6=5, CURRENT 4/4, calendar 12/12, V5 CRC_DIFF=0, zero RX drops/resync. Four intentional physical one-page S92/OEMW writes each with actual controller-origin FC16 semantic acceptance, no retry: **D24 Hot Water Enabled ON(1)→OFF(0)** at 23:38:48; **D24 OFF(0)→ON(1)** at 23:39:39; **D13 Eco(1)→Comfort(0)** at 23:39:52; **D13 Comfort(0)→Holiday Eco/AWAY(2)** at 23:40:01. Prior W2R63 ABORT_RANGE source defect is resolved; no new UART owner. A premature attempt to restore ON and an early AWAY attempt without separate trial were correctly denied NO_TX. **Current controller-confirmed final state at capture end: DHW ENABLED ON, mode Holiday Eco (2), NOT restored to prior Eco (1)**; user may restore Eco through the existing validated D13 Comfort/Eco path. **Hot Water ON/OFF and AWAY milestones CLOSED with 4/4 positive writes; do not retest without contradictory live evidence.** TOP-UP remains ONE-SHOT NO_TX and OPEN: OEM trigger semantics absent. **CURRENT MILESTONE:** Hot Water Write User ON/OFF and MODE complete; TOP-UP outstanding. **DELIVERABLE:** W2R64HW live verified firmware (private source). **REAL BLOCKER:** exact controller-semantic one-shot TOP-UP command only, not basic DHW writes. **ONE NEXT ACTION:** source-map OEM TOP-UP one-shot command and integrate a single bounded user-initiated S92 transaction, preserving W2R64HW production baseline.


**2026-11-01 MAIN04-W2R64HW — SOURCE / OFFLINE TESTED; PREPARED / NOT RUN:** Live user log on W2R63HW proves M6=5, CURRENT 4/4, calendar 12/12, clean V5 CRC/RX; Write User enabled 23:29:14, Hot Water one-edit trial armed 23:29:23, D24 Hot Water Enabled requested 1→0 23:29:32. Existing single S92/OEMW path sent genuine CURRENT selector, then older `EXP444` FC03 validation incorrectly classified D24 target 0 as out of range: `ABORT_RANGE`, no desired-page TX, no semantic acceptance. **W2R63HW test COMPLETE / NEGATIVE** for D24 value delivery, not a controller refusal. W2R64HW fixes only the legacy 042E range decision (D24 0/1; D13 0/1/2 including AWAY; D14 1–30) and updates build label; no new TX path, changed session safeguards, Heating controls or TOP-UP. Complete PRIVATE ZIP contains full YAML, previous exact W2R63 rollback, manifest, diff and concise test instructions. YAML parsed, unique IDs and lambda delimiters checked, ZIP SHA/CRC passed; **NOT TARGET COMPILED / FLASHED / LIVE** for W2R64HW. **CURRENT MILESTONE:** Hot Water Write User. **DELIVERABLE:** W2R64HW integrated source fix. **REAL BLOCKER:** first controller-origin D24 semantic FC16 after a real desired page; TOP-UP one-shot still unknown. **ONE NEXT ACTION:** user-compile/flash W2R64HW, one bounded D24 ON→OFF trial, assess controller-origin FC16 and restore with separate explicit edit.


**2026-11-01 MAIN04-W2R63HW — SOURCE / OFFLINE TESTED; PREPARED / NOT RUN:** Private full W2R62HW-derived YAML now integrates Hot Water ON/OFF `0x042E/15 word0` as new OEMW descriptor D24 in the **existing sole S92/FC03/FC16 writer**, plus an explicitly user-armed, one-edit/45-second trial for ON/OFF and the existing D13 Holiday Eco/AWAY (target/source value 2). No new UART/TX/DE owner; one physical desired page per selected edit, controller-origin exact FC16 acceptance required, ABORT and source-file rollback retained. Existing LIVE-verified Comfort/Eco remains unchanged. TOP-UP stays visible as a one-shot NO_TX because its exact controller command is not established; do not claim full Hot Water completion. PyYAML and C++ lambda delimiter offline checks pass; **NOT TARGET COMPILED / FLASHED / LIVE**. **CURRENT MILESTONE:** Hot Water Write User. **DELIVERABLE:** private complete W2R63HW trial ZIP (user-supplied W2R62HW baseline). **REAL BLOCKER:** no physical XTR semantic acceptance of D24/AWAY; TOP-UP OEM one-shot encoding still OPEN. **ONE NEXT ACTION:** user compiles/flashes W2R63HW and initiates ONE reversible ON/OFF trial, then supplies controller-origin FC16 outcome.


**Local monitoring and control of the Thermia iTec XTR heat pump using ESP32, ESPHome and Home Assistant.**

This project provides a local, cloud-independent integration for Thermia iTec XTR heat pumps by communicating directly with the heat pump's internal RS485 bus.

The integration is developed and tested on a **Thermia iTec XTR M with Total Compact indoor unit**, using an ESP32-S3 with an RS485 interface.
If you are looking for a ATEC version it can be found here: https://github.com/fclauson/Thermia-ATEC-ESP-emulator-of-DCOM

## Roadmap

**2026-11-02 W2R76N parameter status consolidation, SOURCE / OFFLINE TESTED (PREPARED / NOT RUN):** One standalone YAML migrates EXP430 semantic state, OEMW physical page phase and W2R73 Heating fast batch state into one authoritative RAM `native_transaction_state` array. An additional fail-closed same-owner combined-phase guard prevents inconsistent D4+D5 physical TX. All original S92/V5/FC03/FC16/ABORT/HA/calendar paths and send sites maintained, no new TX scope. Full offline normalized YAML comparison PASS; target compile/LIVE missing. **Important:** this is state **storage** consolidation, NOT full transition FSM merger; legacy/write/calendar submachines still active and require dedicated transition-reducer implementation after baseline validation. W2R75D and W2R68FAST rollbacks bundled. **NEXT:** user compiles the single YAML, verifies normal M6/CURRENT/CAL/CRC without triggering new parameter-write tests; then implement reducer.

**2026-11-02 Source consolidation W2R74M — SOURCE / OFFLINE TESTED, PREPARED / NOT RUN:** Production-facing W2R73B-C1 module refactor to 191-line `thermia-itec-xtr-m.yaml` and 11 literal `!include` modules. S92/V5 CRC/RX/TX/DE sole physical owner, FC03/FC16, M6 session, native refresh/calendar, 291 C++ lambdas (290 text-identical and one build-label-only text change) and all HA entities unchanged; removed six unreferenced globals after reference check. ZIP includes modular complete source, exact C1 and W2R68FAST LIVE rollback. Source assembled and compared to baseline, ZIP CRC/SHA PASS; NOT ESPHome target compiled or live verified. Further deduplication of legacy state machines remains an implementation task, not claimed completed. **NEXT:** target compile modular build and confirm same M6/CURRENT4/4/CAL12/12 before any new physical TX experiment.

**2026-11-01 W2R62HW SOURCE candidate — PREPARED / NOT RUN:** Private integrated full YAML ZIP `Thermia_MAIN04_W2R62HW_TopUp_Button_Source_ONLY_PRIVATE.zip` starts from W2R61HW and adds a user-facing ESPHome **one-shot TOP-UP button**, leaving old EXP383 switch internal for RX compatibility. The button explicitly does **NO_TX** because controller semantics for 042E word2 are not demonstrated. Build label adjusted; existing S92 TX/FC03/FC16, verified COMFORT/ECO, controls and rollback preserved. YAML parsed and archive CRC/SHA passed; NOT TARGET COMPILED/FLASHED/LIVE. This is **NOT** the requested working HOT WATER release and not a reason to reflash. **REAL BLOCKER:** new ON/OFF descriptor not yet integrated in single S92 OEMW owner; TOP-UP OEM one-shot command unknown. **ONE NEXT ACTION:** implement the native bounded ON/OFF descriptor in existing S92 owner rather than more preflight/JS changes.

**2026-11-01 MAIN04-W2R61HW HOT WATER source-preflight candidate — SOURCE / OFFLINE TESTED, PREPARED / NOT RUN on physical XTR.** Private ZIP `Thermia_MAIN04_W2R61HW_S92_Source_Preflight_PRIVATE.zip` contains full W2R60-derived YAML, byte-identical W2R60 rollback, diff (~174 lines), SHA256, Dutch build/ABORT/rollback instructions. **Implemented:** one controller-source-only `03 Hot Water | Native Write Preflight` text sensor requiring existing qualified M6/S92 same epoch owner, fresh current 042E native owned snapshot and genuine FC16 cache, word 0/1/2 agreement, V5/collision/ledger idle checks; reports `SOURCE QUALIFIED ... NEW WRITES NOT AUTHORIZED` or explicit `NO-GO`. Simplified existing HOT WATER ON/OFF and internal EXP383 TOP-UP switch actions to preserve controller state and report NO_TX, removed their dead legacy queue code. Preserved real D13 COMFORT↔ECO validated OEMW route, all previous W2R60 S92 TX logic, UART/DE/CRC/ABORT/FC03, calendar, native runtime. **Not implemented:** novel HOT WATER ON/OFF or TOP-UP physical writes or AWAY; legacy `0x0430` word2 remains unproven one-shot. No new physical TX and no existing TX grant expansion. **OFFLINE TESTED:** PyYAML with ESPHome secrets handler loaded complete 15 switches/86 text sensors/4 scripts, exact source/rollback comparison, ZIP CRC and SHA manifest. **NOT TARGET COMPILED, NOT FLASHED, NOT LIVE / LOCALLY VERIFIED.** This is partial delivery of requested functional write integration and should not be described as working ON/OFF/TOP-UP; W2R60 remains last live verified. **CURRENT MILESTONE:** integrated HOT WATER functions in sole native S92 engine, partial preparatory implementation. **DELIVERABLE:** complete private source-preflight YAML ZIP with exact original rollback. **REAL BLOCKER:** controller-semantic geometry/dispatch evidence for novel ON/OFF and single-shot TOP-UP beyond current D13/D14 whitelist, plus qualified one bounded live trial. **ONE NEXT ACTION:** implement source-backed 042E word0 ON/OFF as single bounded user-initiated S92/OEMW descriptor, with ABORT and no retry; do not turn on speculative TOP-UP.


**2026-11-01 HOT WATER TOP-UP OEM semantics and source gate — COMPLETE / POSITIVE for source review; UI correction SOURCE / OFFLINE TESTED, PREPARED / NOT RUN on HA.** Official XT/XTR user guide §5.4 specifies TOP-UP is a **one-time** immediate DHW full-tank heating request with compressor + electric auxiliary heater, must be reactivated each time; not a persistent ON/OFF switch. HOT WATER ON/OFF controls production enable; COMFORT/ECO validated on XTR W2R27 D13 2/2; AWAY not controller-write-verified. Exact W2R60 private source has `exp378_sww_enabled_control` on known DHW 042E word0 and `exp383_topup_control` candidate 0430 word2, BOTH early `NO_TX` and old EXP378/EXP383 queues; **no validated S92/OEMW semantic write/one-shot trigger/reset for these two**. Never turn on obsolete queue or infer TOP-UP one-shot from register candidate. UI private zip `Thermia_Hot_Water_TOP_UP_OneShot_UI_Scope_PRIVATE.zip` includes SAME filename `thermia-display-menu-v5.js`, unchanged custom type/resource, exact W2R60 full firmware byte-identical, rollback and scope mapping. New disabled `Start TOP-UP` momentary button and accurate OEM explanation, live DHW-boost observation separately shown, no UI calls/new physical TX, JS `node --check` and ZIP SHA/CRC PASS. **Not W2R61 firmware, no new parameter writes, NOT live verified on user HA.** **CURRENT MILESTONE:** Hot Water missing user scope. **DELIVERABLE:** source-backed one-shot TOP-UP semantics and same-name HA correction. **REAL BLOCKER:** safe controller-origin semantic transaction for ON/OFF and one-shot TOP-UP through single S92/OEMW sender, not merely FC16 transport or old queue. **ONE NEXT ACTION:** integrate a bounded user-initiated Hot Water group in the same native S92/OEMW owner, with exact source-state/epoch, abort/rollback, and one novel physical XTR validation when user chooses to run it. Existing 51/51 writes remain closed.


**2026-11-01 integrated display-menu flattening after user GO — SOURCE / OFFLINE TESTED; PREPARED / NOT RUN on real HA.** Starting from actual W2R60 XTR LIVE / LOCALLY VERIFIED full firmware (M6=5, CURRENT4/4, CAL12/12, clean V5 and D1 40→37 controller-origin FC16), made one PRIVATE deliverable `Thermia_Integrated_User_Display_Menu_Flat_UI_PRIVATE.zip`. The ESPHome W2R60 YAML is **byte-identical**, so NO new firmware/OTA or TX role. The `ha/www/thermia-display-menu-v5.js` retains **exact same installed filename, resource and `custom:thermia-display-menu-v5` type**, unchanged existing validated control service paths and schematic curve manual single-write button. Removed separate nested dropdowns in all other official user sections too (DISTRIBUTION CIRCUIT 1/2, HOT WATER, COOLING HYSTERESIS, calendar domains/per-program/time function/weekday, alarm/readback options): existing `_branch` creates visible heading/indented flat grouping; `_item` with live value renders inline without its own dropdown. Only top-level menu chapters and existing curve preview group remain collapsible. All authored UI text English, Startup HT not displayed, 17 existing proven display control options retained; P4 remains existing limited editor. `node --check` PASS, no new HA service method or new physical writer, ZIP CRC + SHA manifest PASS; HA browser/live not run. **Scope decision: PARTIAL integrated larger step**, not fake 1:1 physical Write User: HOT WATER ON/OFF source-only `0x042E` word0, TOP-UP old test queue `0x0430`, AWAY, other OPERAT modes, circuit controls and 31 additional calendar slots still lack controller-origin semantic validation in the one S92 owner; old test queues stay OFF and no new unvalidated TX occurs. Prior 51/51 controller-confirmed writes remain CLOSED. **CURRENT MILESTONE:** display-faithful HA user controls and major gap implementation planning. **DELIVERABLE:** complete same-identity UI/rollback ZIP + exact W2R60 source reference; new hardware write scope not implemented. **REAL BLOCKER:** source-qualified user functions outside 19 proven controls lack integrated guarded OEMW/S92 controller semantic acceptance; cannot claim full menu write functionality. **ONE NEXT ACTION:** source-integrate a consolidated, user-initiated bounded HOT WATER user write group into existing sole S92/OEMW engine as next firmware milestone, with ABORT and original W2R60 rollback; no retesting already verified controls.


**2026-11-01 display-menu missing parameter coverage update (same v5 JavaScript file/card) — SOURCE / OFFLINE TESTED; PREPARED / NOT RUN on actual HA.** User's ordered request: FIRST fill remaining user-guide display parameter coverage, NEXT remove remaining nested dropdowns outside HEATING. Exactly same installed `thermia-display-menu-v5.js`, resource `/local/thermia-display-menu-v5.js?v=5`, custom `custom:thermia-display-menu-v5`; firmware unchanged W2R60 live verified. One private UI ZIP `Thermia_Display_Menu_Missing_Parameters_Same_JS_PRIVATE.zip` and direct replacement JS plus rollback/diff/guide-gap matrix. Added official HEATING DURING COOLING (AUTO/OPEN/CLOSED), CONSTANT TEMP, POWER LIMITATION as correctly unavailable (no guessed register); both distribution circuits' seven genuine readbacks each (CURVE/MIN/MAX/+5/0/-5/CONSTANT TEMP) plus target/configuration and explicit unverified equivalents; TOP-UP shows OEM DHW boost indication as partial correlation NOT validated toggle; OP.DATA TANK links existing DHW temperature with uncertain label, SYSTEM SUPPLY links controller **target**, explicitly NOT measured supply; OPERAT.TIME compressor only observed since ESP boot, NOT lifetime counter; 8 existing raw XTR alarm records shown without invented event names. All UI strings English, Startup HT hidden, 17 proven display controls + prior one-change chart Write unchanged; **no additional physical TX scope**, no source YAML or S92/CRC/FC16/ABORT/DE change. Browser PASS: valid JS, 11 sections, 1 flat HEATING nine-control list, SVG visible, source-backed additional option labels, Write blocked without grant, one explicit validated number.set_value and no duplicate, 0 service calls from plot sliders, no JS errors. **NOT yet verified on user's HA**. Scope of missing physical functionality remains: HOT WATER ON/OFF source known read 0x042E word0 but legacy switch intentionally NO_TX; TOP-UP old EXP383 NO_TX, AWAY, Off/Aux/Hot Water operating modes, individual circuits, other calendar slots, accumulated OEM hours and alarm names all HOLD. Do not re-enable obsolete experimental queues or invent registers. **CURRENT MILESTONE:** user-display parameter coverage menu UI COMPLETE / POSITIVE offline only; real controller write parity not complete. **DELIVERABLE:** same-name JavaScript patch and full private rollback ZIP/mapping. **REAL BLOCKER:** controller-origin semantic acceptance and same-owner S92 integration missing for unvalidated user options. **ONE NEXT ACTION:** existing W2R60-based source engineering of HOT WATER ON/OFF in canonical S92 as one guarded, user-initiated bounded function, then one authorized physical validation with ABORT/rollback; meanwhile existing HA file may be copy-pasted and refreshed, flatten other dropdowns in next UI revision.


**2026-11-01 UI-only Thermia HEATING flat list + monochrome curve + manual single-setting Write button (same v5 JavaScript identity) — SOURCE / OFFLINE TESTED; PREPARED / NOT RUN on user HA.** User requested flatter HEATING and Thermia manual-style graph, then explicitly requested a write button next to curve, but required NO JS filename/resource/custom-card name changes. One private archive `Thermia_XTR_Display_Menu_Heating_Curve_UI_Update_PRIVATE.zip` and direct copy-ready `thermia-display-menu-v5.js` replace **exact same** installed `/homeassistant/www/thermia-display-menu-v5.js`; resource `/local/thermia-display-menu-v5.js?v=5`, `type: custom:thermia-display-menu-v5` unchanged; hard browser reload required as registered JS custom element won't hot-reload in same tab. W2R60 XTR LIVE / LOCALLY VERIFIED native M6/CURRENT/auto CAL and one deliberate D1 40→37 write remains unchanged; **NO ESPHome firmware changes and no new UART owner or RS485 path**. Original display menu hierarchy and 17 proven display controls, English-only UI, no Startup HT preserved. HEATING contains ONE native HA `entities` list of 9 validated user numbers instead of 9 nested field dropdowns (ROOM separate on main screen). The always-visible plot is monochrome with original Thermia-style supply/outdoor axes (+20 to −20), one solid current curve, gray dashed preview when staged, labeled MIN/MAX and HEAT STOP, 8 local-only preview sliders. New **Write selected change** user button sends **only ONE last-touched outstanding staged value** using existing user-validated `number.set_value` entity; multiple preview changes require separate explicit click per setting; no batch, blind retries or reauthorizing TX. UI requires explicit Write User grant, exact unique HA entity and current baseline, HA min/max/step, blocks in-flight duplicate; observes native readiness BUSY→ENABLED and numeric controller-reflected value before displaying a qualified completion indication and directs user to native controller-origin FC16 for conclusive semantic proof; HA service completion is not semantic acceptance. Firmware alone retains original S92/DE/CRC/session guards and ABORT. Browser offline PASS `node --check`; 11 sections, 1 flat 9-entity HEATING list, visible SVG, zero HA calls on preview, denied without grant, exactly 1 HA `number.set_value` call on deliberate authorized Write, second click while pending zero, optimistic numeric state alone doesn't count as controller result, readiness BUSY→ENABLED+readback state required. ZIP manifest SHA/CRC and byte-exact rollback of previously delivered v5 JS PASS. Card UI change **not yet HA live verified**; no physical write experiment repeated. **CURRENT MILESTONE:** user display-equivalent English HA menu and heating-curve interaction. **DELIVERABLE:** same-name v5 JavaScript replacement with manual write button, full private ZIP/rollback, W2R60 untouched. **REAL BLOCKER:** none for source/UI preparation; user browser reload and real card confirmation pending. **ONE NEXT ACTION:** user pastes exact replacement JS into existing same-name HA file, hard-refreshes; checks flat HEATING and diagram and, only when a normal desired change is needed, manually enables Write User and clicks Write for one setting while observing controller result. No retesting the historical 51 accepted writes.


**2026-11-01 English UI / curve visibility v5 — SOURCE / OFFLINE TESTED; PREPARED / NOT RUN on actual HA.** User reported the schematic curve invisible in previous v4 card and explicitly mandated **all UI text in English**. Created one complete PRIVATE UI-only ZIP `Thermia_XTR_Display_Menu_v5_English_CurveFix_PRIVATE.zip`. Exact W2R60 XTR live-verified private firmware reference retained byte-identical, no OTA flash or RS485 source changes. New unique JavaScript filename `thermia-display-menu-v5.js` and distinct custom element **`custom:thermia-display-menu-v5`** avoid conflicts with previously loaded `thermia-write-user-card` class; prominent always-visible SVG curve appears above ALL collapsed menu details, renders illustrative fallback immediately even without HA states and updates to genuine HA values once available. Eight preview sliders change only the orange path; the original blue live-HA path and all real W2R60 Write User controls remain separate. **EVERY authored UI heading, legend, tooltip, menu description, button, status, and HA entity display alias is English**; original Dutch ESPHome friendly-name strings used ONLY for internal exact entity discovery, without renaming HA entities. Display-faithful official USER-menu, 17 historically validated display controls, no Startup HT control, nonvalidated options read-only/HOLD, P4 same separate authorization. Headless Chromium simulated HA `PASS`: SVG visible 1126×370, two long path data strings, 8 sliders, 11 menu sections, no page errors, early fallback graph with no HA state, slider moves preview path but `window.calls=0`; label overrides for 86 mock entities and JS `node --check` PASS. ZIP CRC/SHA validated. **Actual user's HA card v5 installation NOT RUN**, suspected previous v4 class/cache collision is hypothesis, not proven. **CURRENT MILESTONE:** display-equivalent English HA UI and heating curve visibility repair v5 PREPARED / NOT RUN on actual HA. **DELIVERABLE:** private complete v5 ZIP with original v4 JS rollback and unchanged W2R60 firmware reference. **REAL BLOCKER:** only actual HA resource/card configuration and real display remain unconfirmed; no firmware/protocol blocker for the UI. **ONE NEXT ACTION:** user copies `ha/www/thermia-display-menu-v5.js` to `/homeassistant/www/thermia-display-menu-v5.js`, adds `/local/thermia-display-menu-v5.js?v=5` JavaScript resource, changes card type to `custom:thermia-display-menu-v5`, hard reloads, confirms always-visible curve and English wording. Do not re-run validated physical write experiments.


**2026-11-01 display-faithful Thermia XT/XTR user menu + interactive schematic HEATING curve v4 — SOURCE / OFFLINE TESTED; PREPARED / NOT RUN on actual HA.** In response to explicit user direction, removed *all non-display controller parameters* from the custom menu (including the unit-unknown D14 control; the actual W2R60 firmware entity is unchanged). Menu faithfully follows the original user-guide tree: HOOFDSCHERM ROOM + INFORMATION §§5.1–5.9, original OPERAT./HEATING/DISTRIBUTION CIRCUIT 1&2/HOT WATER/COOLING/OP.DATA/OPERAT.TIME/CALENDAR/ALARM HISTORY and their suboptions. **17 display-aligned previously validated writes are presented; original 19 XTR descriptor/51-write evidence remains closed and unchanged**, two non-display descriptors intentionally hidden. New HEATING section shows interactive blue current-HA versus orange preview SVG with eight preview sliders CURVE/ROOM/MIN/MAX/HEAT STOP/+5/0/-5, pointer-read outdoor/indicative supply, restore-to-HA, and official manual curve sample +20→24,0→40,-20→56 for CURVE40. The graph is explicitly **illustrative**, not OEM's exact curve algorithm: 3°C curve translation per 1°C ROOM is official manual p20; correction interpolation is approximate; graph sliders generate **ZERO HA writes**. Actual edits only via unchanged existing W2R60 native number controls and original S92 single owner/FC16 semantics/ABORT. Full PRIVATE archive **`Thermia_XTR_Display_Exact_Menu_Interactive_Curve_v4_PRIVATE.zip`** includes `ha/www/thermia-write-user-cards.js` matching user's plural installed filename, dashboard example, README, manual tree-to-support mapping, offline check, previous v2 card rollback, SHA manifest, exact existing W2R60 live full YAML for reference/rollback and offline screenshot. One consolidated PASS: `node --check`, Playwright Chromium renders 10 sections + 8 responsive curve sliders, live-vs-preview paths, slider changes SVG with 0 calls, reset works, valid manually clicked mode single HA service call, unsupported mode source disabled, no automatic calls; ZIP CRC/SHA PASS, exact baseline W2R60 YAML byte-identical to prior original ZIP. **No ESPHome compile/flash and no new RS485 TX; actual v4 card UI NOT YET LIVE VERIFIED**. Startup/experimental controller settings not displayed in card, but no firmware entity deletion claimed. **CURRENT MILESTONE:** Display-faithful Write User HA menu plus interactive heating curve v4 PREPARED / NOT RUN. **DELIVERABLE:** full private HA-only v4 ZIP, original W2R60 untouched. **REAL BLOCKER:** actual Home Assistant v4 load/display pending; broader display-menu functions (HOT WATER ON/OFF, TOP-UP, AWAY, other operating modes/calendars etc) lack controller-semantic write validation and remain READ/HOLD. **ONE NEXT ACTION:** user replaces `/homeassistant/www/thermia-write-user-cards.js`, sets resource `/local/thermia-write-user-cards.js?v=4` as JavaScript module, hard-refreshes, verifies display menu and heating curve live; then prioritize first unvalidated display-user function without retesting the 51 already-proven writes.


**2026-11-01 W2R60 integrated Write User + HA operator panel — SOURCE / OFFLINE TESTED; PREPARED / NOT RUN.** On actual XTR, W2R58 remains latest LOCALLY VERIFIED OTA native M6=5/CURRENT4/4/CAL12/12/RX-clean baseline; the 19 ordinary user controls had prior W2R25F4/W2R27/W2R28F1/W2R29F1 total **51/51 genuine controller-origin FC16 semantic acceptances**, not to be retested. Starting from byte-identical W2R59F1 corrected private candidate, prepared ONE complete private ZIP `Thermia_MAIN04_W2R60_WriteUser_HA_Control_Bundle_PRIVATE.zip` with full YAML, optional `ha/www/thermia-write-user-card.js` and HA dashboard example, previous full rollback YAMLs, exact source diff and SHA manifest. Integrated one evidence-based scope correction: D3 Operating Mode transitions only when source and target in Auto(1)/Compressor(2); D13 DHW Mode only when source and target in Comfort(0)/Eco(1), preventing untested transitions out of Off/Aux/HotWater or Holiday Eco, before any OEMW ledger/TX intent. Other 17 proven descriptors and S92 UART/DE/CRC/owner/FC16/ABORT/native CURRENT/automatic calendar/P4 engine unchanged. Optional dashboard groups EXACT 19 source-declared enabled HA controls, permission buttons, readiness, controller-result, M6/CURRENT/CRC; optional separate P4 section. Dashboard resolves HA entity IDs only by unique exact friendly-name suffix and matching domain (optionally prefix); no guessed IDs, autonomous writes, extra TX owners or service actions. Offline PyYAML `!secret` parse, **1042/1042 existing IDs**, all 19 mapped enabled controls, source diff35 lines, `node --check`, safe lookup smoke, one writer and ZIP CRC/SHA PASS. W2R59 original invalid binary-sensor `update_interval` remains fixed from W2R59F1. **W2R60 NOT ESPHome TARGET COMPILED/FLASHED/LIVE; optional HA card NOT HA runtime verified; no new XTR physical write experiment or blanket new user manual permission.** Nonvalidated D19, D13 Holiday Eco, Operating other modes, hot water Top-up/enable and other calendar/service writes remain HOLD. **CURRENT MILESTONE:** Write User daily-use production interface W2R60 package prepared. **DELIVERABLE:** integrated private full W2R60 firmware + dynamic HA card ZIP. **REAL BLOCKER:** W2R60 ESPHome target compilation and OTA normal native regression, optional dashboard live HA check pending; no need to rerun the 51 historical physical tests. **ONE NEXT ACTION:** user manually compiles/OTA installs W2R60, observes exact build/M6=5/CURRENT4/4/calendar12/12/CRC and optionally installs card; report only compiler failure if any.


**2026-11-01 MAIN04-W2R59 validated Write User production-facing release candidate — SOURCE / OFFLINE TESTED; PREPARED / NOT RUN.** Exact source: user's genuinely XTR-FLASHED/LIVE/LOCALLY VERIFIED W2R58 full private YAML (native M6=5, CURRENT4/4, calendar12/12, clean V5 RX). Historical separately independently verified XTR writes remain CLOSED: Heating 10 descriptors 27/27, Hot Water D13/D14 4/4, Cooling six 18/18, Operation Auto↔Compressor 2/2 = **19 controls and 51/51 controller-origin FC16 semantic acceptances** on earlier W2R25F4/W2R27/W2R28F1/W2R29F1. No repeat physical tests. ONE integrated private **`Thermia_MAIN04_W2R59_Write_User_Production_PRIVATE.zip`** prepared: keep original `w2r25_start_heating_acceptance` HA button ID and session/owner/Fresh CURRENT/CRC/peer/one-S92-TX/no-retry/ABORT, rename its visible HA label to `Enable Write User (Validated Controls)` with truthful no-TX/19-control result, add an idle-only `Disable Write User` control (refuses during in-flight OEMW; emergency S92 ABORT remains separate), add binary and text grant/readiness status. Preserve all existing 19 HA controls and unchanged P4 per-Apply 5-field engine. One scoped XTR evidence alignment: D13 `Holiday Eco=2` remains readable but is now denied for writing, because physical D13 evidence covered only Comfort0↔Eco1; Cooling D19 and Operating Off/Aux/Hot Water, other domain/service TX remain HOLD. Correct historical misleading `HA_WRITES_HOLD` and bounded-trial message text only for the verified scope. Diff 209 lines; PyYAML with `!secret` PASS; 1040 old unique YAML IDs retained plus 3 new=1043; exact `uart`, `globals`, `interval`, all other scripts, `esphome`, `api`, logger and sensor preserved; same ONE UART `.write_array`, unchanged DE-low/ABORT, no new TX role; ZIP CRC and SHA manifest PASS. Historical exact W2R29F1 source artifact not accessible in current container: byte-identical source parity to W2R29F1 NOT claimed; verified closed evidence + preserved W2R58 shared ledger used. **NOT ESPHome target compiled, NOT flashed, NOT live, no W2R59 physical setting writes.** W2R58 original live-verified normal read remains exact rollback. **CURRENT MILESTONE:** Write User 19 validated controls W2R59 release candidate prepared. **DELIVERABLE:** complete private W2R59 integrated firmware/rollback ZIP. **REAL BLOCKER:** first W2R59 ESPHome target compilation and ordinary OTA M6/CURRENT/calendar regression; *no new protocol validation blocker for previously verified 19 descriptors*. **ONE NEXT ACTION:** user manually compiles/flashes W2R59, checks exact W2R59 firmware build, normal M6=5/CURRENT4/4/CAL12/12/CRC/HA and read-only grant state; existing 51 physical parameter tests must NOT be repeated.


**2026-11-01 WRITE USER EVIDENCE CORRECTION / GO FOR SOURCE-SCOPE RELEASE PREPARATION (NO NEW TX).** Earlier statement that all ordinary HA parameter writes still require initial XTR semantic validation was incorrect. On real XTR M 3N/controller 2.4.2, W2R25F4 Heating 10 descriptors 27/27, W2R27 DHW D13+D14 4/4, W2R28F1 Cooling six descriptors D2/D15/D16/D17/D18/D20 18/18, and W2R29F1 Operating Auto(1)↔Compressor(2) D3 2/2 completed with independent controller-origin FC16 per physical send: cumulative **51/51, FLASHED / LIVE / LOCALLY VERIFIED, COMPLETE / POSITIVE**; do NOT repeat. Exact W2R58 private YAML source retains `w2r20_heating_group_enabled: "true"`, the HA Configuration user-enable button, the existing OEMW ledger across these four pages, same-owner guarded one-word desired-page send/FC16 confirmation, and S92 ABORT, even though inherited general `HA_WRITES_HOLD` comments remain. Distinguish **historically verified physical user scope** from **W2R58 live regression**, which only confirmed native read/runtime, NOT parameter writes or current user-enabled production use. Release decision needs one targeted source parity/reconciliation against the proven W2R29F1 user scope, removal of misleading HOLD/status/UI text only where justified, continued explicit user enablement, CRC/owner/epoch/FC16/freshness/ABORT and one S92 writer; NO new physical TX experiment. D19 Cooling room-sensor write, Operating Off/Aux Heater/Hot Water, additional/user/service and unverified calendar modes remain HOLD. **CURRENT MILESTONE:** Write User validated scope productisation as next functional milestone. **DELIVERABLE:** 51/51 historical XTR proof and current W2R58 source presence reconciled. **REAL BLOCKER:** no new controller protocol proof missing for the 19 established descriptors; current W2R58 production activation/parity not independently confirmed. **ONE NEXT ACTION:** perform one minimal W2R29F1→W2R58 source parity and integrate a single validated-scope Write User release fix if needed, without reopening the 51 previously closed physical tests.

**2026-11-01 W2R58 actual XTR OTA/live baseline — COMPLETE / POSITIVE for ordinary native read/session ONLY.** User log `Pasted text(20261101-161744).txt` 17:13:57–17:17:08 (3m11s API capture) shows actual `Thermia MAIN04-W2R58 | P4 per-Apply grant` firmware build at 17:14:49, 17:15:49, 17:16:49; ESP reset reason OTA. Existing S92 retained-runtime native session progressed M6=2→4→5, independently controller-origin `CURRENT_4PAGE_CONFIRMED` mask=0F at 17:14:19.648, `CURRENT_SYNCED page=FRESH` continuing through 17:17:05 with FC03 count42. Owned controller calendar read reported complete 12/12 at 17:14:41.170, `AUTO_CAL_TWELVE_OWNED_ACKED` at 17:14:49.364. Controller P4 physical Sunday18:20–18:26 unchanged, shown at 17:14:36.935 and 17:14:51.866. V5 CRC_DIFF=0/1577 checks 17:17:06.981, parser resyncs0 and RX buffer drops0 through 17:16:49; queue and dirty0, no P4 Apply or parameter-setting TX. One passive spontaneous F1 metadata change 05BB 0000→0008 at 17:15:49 was observed, NOT a setting write and local semantics unproven. 200s periodic refresh threshold NOT reached during capture; controller-only restart/loss, visual HA cleanup, W2R58 per-Apply reauthorization/write and ABORT not exercised. Distinguish W2R58 **FLASHED / LIVE / LOCALLY VERIFIED normal runtime** from W2R58 per-Apply **PREPARED / NOT RUN** for physical edit; W2R56 remains proven five-field physical semantic write+restore. General HA parameter writes ON HOLD. **CURRENT MILESTONE:** W2R58 normal-runtime OTA regression confirmed. **DELIVERABLE:** W2R58 private integrated firmware runs on XTR M. **REAL BLOCKER:** none for ordinary session/read and previously validated W2R56 P4 fields; W2R58 per-Apply new interaction has no live physical evidence, and controller-only automatic hot-rejoin unresolved. **ONE NEXT ACTION:** proceed with next real roadmap engineering gap (native controller-only loss/recovery in same S92/M6 owner), using W2R58 as locally verified normal-runtime baseline; do not require repeating proven P4 controller writes.


**2026-11-01 W2R58 P4 PER-APPLY GRANT — SOURCE / OFFLINE TESTED; PREPARED / NOT RUN.** Starting from actual XTR W2R57 FLASHED / LIVE / LOCALLY VERIFIED for OTA M6=5, CURRENT4/4, calendar12/12 and clean RX, prepared ONE complete PRIVATE W2R58 ZIP. Explicit HA Apply P4 now starts a fresh bounded authorization per click, removing previous expired boot-once 30min/10-page grant and ESP-restart friction. Maximum five DISTINCT existing configured P4 weekly-field physical pages per click, max 30min transaction, original scoped small value/day-bit steps preserved, same sole S92/OEMW sender, CRC/RX/session ownership/collision guards, no automatic resend, controller-origin FC16 each field and independently fresh owned F1 3/3 for final persistence. A second Apply requires a new owned P4 F1 3/3 snapshot AFTER the preceding Apply, including on partial failure; this prevents blind retry and allows deliberate later use without ESP reboot. Stop subsequent fields and existing S92 ABORT/rollback unchanged. No new program/domain, general HA parameter TX or service-write authority. Full YAML parse, ID/dependency/diff/UART-one-writer, ZIP CRC and SHA manifest pass; **W2R58 NOT target compiled, NOT flashed, NOT live**. Original proven P4 controller state remains Sunday18:20–18:26; W2R56 physical semantic proof must not be repeated. **CURRENT MILESTONE:** W2R58 per-Apply P4 usability prepared. **DELIVERABLE:** private complete W2R58 integrated ZIP, exact W2R57 live rollback and older rollback YAMLs. **REAL BLOCKER:** W2R58 first user ESPHome compilation and normal OTA validation are outstanding; broader value/calendar scopes and general HA writes remain HOLD. **ONE NEXT ACTION:** user manually compiles/OTA-flashes W2R58 and checks actual build label, native M6=5/CURRENT4/4/CAL12/12 and unchanged HA entities; no repeat of verified physical P4 write tests.


**2026-11-01 W2R57 OTA LIVE / LOCALLY VERIFIED — COMPLETE / POSITIVE for ordinary native read + UI-only release startup scope.** User log 10:38:54–10:40:47 proves actual W2R57 firmware OTA boot, M6=5, CURRENT FC16 4/4, automatic owned 12/12 calendar read, P4 Sunday18:20–18:26, CRC_DIFF0 over 854 checked frames with zero resync/drops, and no setting writes. Visual HA control cleanup, W2R57 physical calendar writes, repeated 200s calendar refresh and controller-only recovery NOT tested; these are not claimed. W2R56 retains scoped five-field real physical setting proof. **Next:** improve existing validated P4 one-click editor trial-only UX in one existing S92 owner without widening authorization; HA parameter writes ON HOLD. More details in Research state and log.


**2026-11-01 NEWEST XTR MILESTONE — W2R56 ALL FIVE P4 WEEKLY FIELDS COMPLETE / POSITIVE; W2R57 PRIVATE UI CLEANUP PREPARED / NOT RUN.** 2026-11-01 real XTR W2R56 second Stop Hour log `Pasted text(20261101-092609).txt` 10:21:59–10:26:01: same ESP boot/session native M6=5, CURRENT4/4, prior auto CAL12/12. Controller P4 previously Sunday18:20–19:26 from positive forward write. At 10:25:32 user staged ONLY Stop Hour=18, explicit W2R56 `BATCH_USER_INITIATED` 10:25:34.133, `BATCH_FIELD_ARMED step=1/1 reg=0585 old=19 new=18` 10:25:34.140. Exactly one original S92/OEMW23 physical page `057B/33` TX 10:25:38.343, W2R54 send-budget used=2/10 across the two directions, no automatic retry. Independent genuine controller-origin FC16 `CONTROLLER_ACCEPTED d=23 reg=0585 actual=18 physicalAttempts=1 receipts=1` 10:25:39.306, associated passive changed word `0x0013→0x0012`. Fresh owned selected F1 3/3 `REFRESH_COMPLETE program=4 mode=1 start=18:20 stop=18:26 days=40` 10:25:44.730, `BATCH_DONE f1Exact=1 pages=2 count=1` at10:25:44.900 (pages=2 cumulative forwards + return; count=1 fields in this batch). Follow-up HA physical P4 Sunday18:20–18:26. CRC_DIFF0 through >2600 checks, parser resync0, RX drops0; no collisions evidenced. **Stop Hour reversible experiment COMPLETE / POSITIVE, FLASHED/LIVE/LOCALLY VERIFIED on W2R56; physical P4 original Sunday18:20–18:26 restored and independently verified.** Together with earlier four fields, five original P4 weekly fields have positive scoped live semantic evidence. Other programs, date calendars, create/delete, general HA writes remain HOLD/UNKNOWN.

After closing that live milestone, prepared one complete PRIVATE `Thermia MAIN04-W2R57` source ZIP from byte-exact W2R56 verified YAML. One dependency-checked UI-only change: removed 5 obsolete per-field/Preview/Arm/Stop-Minute HA controls and unused selector global; updated stale Read-blocked help text and firmware-build diagnostic. Verified old Preview's sole caller was removed old per-field Apply; retained exact existing Read Selected, Discard, Apply Staged P4, Stop P4 Batch, S92 ABORT, all other HA entities and same one S92 UART/RX/DE writer. Existing P4-only 30min/10 sends/boot, CRC/V5, native M6/FC03/FC16/CURRENT4/4/CAL12/12/recovery, no auto-retry and other-write HOLD unchanged. Full PyYAML and dependency/diff checks, complete ZIP 11 entries including exact W2R56/W2R55/... rollbacks, manifest hashes and ZIP CRC pass. **W2R57 SOURCE / OFFLINE TESTED; PREPARED / NOT RUN; NOT TARGET COMPILED, NOT FLASHED, NOT LIVE.** Source PRIVATE: no firmware YAML, secret, protected handshake or OEM mailbox tooling pushed. **CURRENT MILESTONE:** W2R56 P4 five-field editor closed; UI cleanup W2R57 prepared. **DELIVERABLE:** complete private W2R57 ZIP; W2R56 remains locally verified operational baseline. **REAL BLOCKER:** none for validated P4; W2R57 target compile/user flash still pending. **ONE NEXT ACTION:** user manually compiles/OTA-flashes W2R57 and verifies build identity plus original M6/CURRENT/CAL and cleaned HA controls; do NOT retest closed physical P4 settings.

**2026-11-01 NEW XTR W2R56 P4 STOP HOUR REG0585: FORWARD COMPLETE / POSITIVE, FINAL RESTORE RUNNING / PARTIAL.** 2026-11-01 W2R56 real XTR Stop Hour `0x0585` forward trial: uploaded `Pasted text(20261101-092204).txt` covers 10:20:28–10:21:59. ESP-only OTA reboot shown by reset reason; W2R56 actual build, native M6=5 CURRENT4/4 10:20:52.979 and auto CAL12/12 10:21:13.572; clean sampled V5 CRC_DIFF0 through 732 checks, RX drops0, parser resync0. Genuine owned selected P4 F1 3/3 10:21:39.712/715: Sunday 18:20–18:26 mask 0x40. User only staged Stop Hour18→19 at10:21:43.910. Explicit `BATCH_USER_INITIATED` 10:21:46.220, `BATCH_FIELD_ARMED step=1/1 reg=0585 old=18 new=19`; original S92/OEMW23 single physical 057B/33 page `GENERIC_PAGE_TX_EXECUTED` 10:21:50.601, W2R54 counter used=1/10, NO_AUTORETRY. Genuine controller-origin FC16 semantic `CONTROLLER_ACCEPTED d=23 reg=0585 actual=19 physicalAttempts=1 receipts=1` at10:21:51.535; changed word confirmed by passive CAL_F1_WORD_CHANGE. Distinct fresh owned selected F1 3/3 completes10:21:57.016 with P4 Sunday 18:20–19:26 and `BATCH_DONE f1Exact=1 pages=1 count=1` 10:21:57.366. **Stop Hour forward 18→19 COMPLETE / POSITIVE, FLASHED/LIVE/LOCALLY VERIFIED in scoped test.** Full reversible Stop Hour trial is **RUNNING / PARTIAL** because log ends 10:21:59 and contains **NO 19→18 controller restoration**. This is a real physical controller schedule change: P4 currently Sunday18:20–19:26 in latest evidence. Keep other HA settings writes ON HOLD. No new firmware/flash or retests of four previously verified P4 fields. **ONE NEXT ACTION:** on same W2R56 boot within its preexisting 30min/10 physical-send grant (if still valid), select P4, obtain fresh selected F1 3/3 BEFORE editing, stage Stop Hour19→18 ONLY, explicitly press ONE existing Apply Staged P4, require genuine reg0585 controller FC16 actual18 plus independent F1 3/3 Sunday18:20–18:26. No blind retry; expired grant => use original Thermia panel for recovery rather than broaden TX rights; S92 ABORT at first error. After physical restore verified, dependency-check and implement separately the UI-only obsolete P4 trial button cleanup; review trial-lease UX without lifting safety budget.

**2026-11-01 W2R56 STOP HOUR REG0585 ATTEMPT — PREPARED / NOT RUN, ZERO SETTING TX.** The new user log10:08–10:15 confirms build W2R56 retained native M6=5/CURRENT4/4/auto CAL12/12, clean CRC / RX and original P4 Sunday18:20–18:26. User staged only `Stop Hour=19` at10:14:45, then tried **Read Selected after editing** at10:14:51 -> `W2R53 READ_BLOCKED_UNSAVED` to protect staging; Apply10:15:09 correctly `BATCH_DENIED owner=1 clean=1 idle=1 snapshot=0 grant=0 NO_TX=1`. Two independent blockers: no fresh owned selected F1 3/3 less than5min, and same ESP boot has an **expired prior W2R56 trial grant (the successful01:18 four-field batch, >8h ago)**, whose existing 30-minute boot-local one-shot scope cannot be restarted on same boot. **No controller field test/rejection** and no rollback needed; reg0585 still NOT RUN. **ONE NEXT ACTION:** user reboots **ESP only**, waits for existing native M6=5, Discard staging if required, select P4 then Read Selected Program BEFORE editing until genuine F1 3/3, stage only Stop Hour18→19, press ONE W2R56 Apply Staged P4; verify exact reg0585 controller FC16 and new selected F1 P4 Sunday18:20–19:26, then new user-initiated restore19→18 within existing 30min/10 physical-send grant and final F1 Sunday18:20–18:26. Do not blindly retry, maintain S92 ABORT and original Thermia panel for recovery. Existing W2R56 four-field complete positive remains latest locally verified, other HA writes remain HOLD. **After physical Stop Hour positive and restored:** separate dependency-checked UI-only old-button cleanup, and evaluate reboot-only trial expiration UX without broadening physical TX rights. No firmware change needed now.

**2026-11-01 NEXT ACTION AFTER W2R56 LIVE COMPLETE / POSITIVE: validate only missing P4 Stop Hour, then clean obsolete buttons.** Keep **W2R56** active as latest real XTR verified one-click P4 batch baseline (four fields/controller FC16 plus fresh F1 and original P4 Sun18:20–18:26 restored). Existing W2R56 source already permits exactly one bounded Stop Hour reg0585 ±1 through original single S92/OEMW23, preserves start<end and independent final owned F1; no new firmware needed to test it. **PREPARED / NOT RUN:** with actual P4 Sun18:20–18:26, stage ONLY Stop Hour18→19 and deliberately user press existing `Apply Staged P4 (One Click - Physical TX)` once; confirm genuine reg0585 FC16 + new F1 Sunday18:20–19:26; then one new intentional batch to restore19→18 with independent F1 Sunday18:20–18:26. Existing max10 physical sends in30min/ESP boot, no blind retries, S92 ABORT and OEM-panel restoration if any mismatch. No new general parameter or calendar write permission. **Only once physical Stop Hour and rollback are confirmed**, next version will hide/remove obsolete manual trial UI (`Field to Apply`, `Preview OEM Field Plan`, `Apply Selected Field (Prepare / Commit)`, `Arm P4 Weekly Fields`, old Stop Minute trial) after exact dependency analysis, keeping selected read, RAM discard, one-click apply, stop batch and S92 ABORT. No two changes in the same unverified physical experiment. **CURRENT MILESTONE:** validate fifth P4 field; **DELIVERABLE:** W2R56 working, no new ZIP; **REAL BLOCKER:** reg0585 Stop Hour semantic write not yet evidenced; **ONE NEXT ACTION:** bounded Stop Hour 18→19 and 19→18 on active W2R56 with genuine F1.

**2026-11-01 CURRENT XTR LIVE MILESTONE — W2R56 ONE-CLICK P4 BATCH COMPLETE / POSITIVE (LOCALLY VERIFIED).** User's complete real W2R56 ESPHome log (01:14:38–01:18:38) confirms explicit `BATCH_USER_INITIATED`01:18:07, **four** user-scoped physical existing original S92/OEMW d23 one-field-at-a-time TX without retry, four **genuine controller-origin FC16 semantic acceptances** (start minute21→20 reg057F at01:18:10, start hour17→18 reg0580 at01:18:14, stop minute27→26 reg0584 at01:18:19, weekday mask Mon+Sun 0x41→Sun0x40 reg0589 at01:18:23), each before arming next distinct field. New independently owned **final P4 F1 3/3** 01:18:28 confirms exact **Sunday18:20–18:26**, followed by `BATCH_DONE f1Exact=1 pages=4 count=4` and `W2R56 COMPLETE`01:18:29. Real HA slot4 also shows Sun18:20–18:26. Thus earlier W2R54 P4 experimental physical calendar settings **ARE NOW PHYSICALLY RESTORED**, as independently verified; no more tests/flash needed for those four fields. Same M6=5/CURRENT4/4/CAL12/12, V5 CRC_DIFF0, RX drops0/resync0; existing single owner/guards and HA-parameter-write HOLD remain. This is **NOT** blanket validation of other calendars/P4 Stop Hour (reg0585 was not physically tested)/create-delete/date operations or general parameter writes. **CURRENT MILESTONE:** one-click P4 four-field editing and controller persistence verified. **DELIVERABLE:** working private W2R56 ZIP and real four-field restore. **REAL BLOCKER for 5-field scope:** physical Stop Hour remains unverified. **ONE NEXT ACTION:** retain W2R56 as locally verified baseline and decide the single missing Stop Hour validation before any broad editor or HA-write expansion; only separately bounded user-initiated physical TX if authorized. Keep all previous roadmap history intact.

**2026-11-01 W2R56 XTR OTA LIVE / LOCALLY VERIFIED normal session; batch still PREPARED / NOT RUN.** Live build W2R56 at 01:13:41, M6=5, CURRENT4/4, CAL12/12, V5 CRC_DIFF0/resync0/drops0, owned selected F1 3/3 P4 controller 17:21–18:27 Mon+Sun. User staged desired Sun18:20–18:26 (4 fields) but pressed OLD per-field Apply, which only PREPARED reg0584 (NO TX). NEW one-click P4 Apply config entity exists but `disabled_by_default: true`; one-time enable from HA entity settings. No physical calendar write or rollback yet; no firmware fix justified. **ONE NEXT ACTION:** user enables NEW `Apply Staged P4 (One Click - Physical TX)` and presses it exactly once with current genuine read/staged P4, then check true per-field controller receipts and final fresh F1. ABORT/physical UI fallback unchanged; all other parameter writes HOLD.

**2026-11-01: W2R56 NOT YET FLASHED — PREPARED / NOT RUN.** Uploaded ESPHome 01:06–01:09 capture proves a real OTA reboot but repeatedly announces **`Thermia Firmware Build = Thermia MAIN04-W2R55`** at01:07:14/01:08:14. Thus native M6=5/CURRENT4/4/auto calendar12/12 recovery and V5 CRC_DIFF0/RX drops0 are again live-proven **on W2R55**; W2R56 one-click batch has **no target-compile, flash or XTR evidence**. Original P4 remains **17:21–18:27 Monday+Sunday** on controller-origin F1 3/3 at01:07:52. At01:08:22 user only staged W2R55 stopminute27→26 in RAM (NO SETTING TX). Not a W2R56 failure and physical schedule not restored. **ONE NEXT ACTION:** manually replace the *actual* ESPHome device config `thermia-itec-xtr-m.yaml` with `firmware/Thermia_MAIN04_W2R56_OneClickP4Batch_HOLD_PRIVATE.yaml` from already delivered private ZIP, install OTA, confirm diagnostic **`Thermia MAIN04-W2R56`** before using the new one-click P4 button. Keep HA parameter writes HOLD and existing ABORT/physical panel rollback unchanged. No new source change needed.

**2026-10-31 W2R56 PRIVATE ONE-CLICK P4 CALENDAR BATCH — SOURCE / OFFLINE TESTED; PREPARED / NOT RUN.** Responding to user feedback: W2R55 per-field trials require too many HA presses. Exact latest XTR LIVE/LOCALLY VERIFIED W2R55 (M6=5, CURRENT4/4, auto CAL12/12, clean V5 and original W2R54 4 individual controller-accepted P4 writes) is unchanged baseline; actual P4 **17:21–18:27 Monday+Sunday** awaits physical restoration to original **Sunday18:20–18:26**. W2R56 adds one default-disabled Configuration HA **`05 Calendar | Warm Water | Apply Staged P4 (One Click - Physical TX)`** button: user first selects P4, loads genuine owned F1 3/3, stages all desired calendar fields, presses this button ONCE. The press itself grants ONE original P4-only 30-minute / ten actual physical-send budget (no separate ARM/Field/Preview/double Apply). Tiny sequential coordinator plans up to five individually bounded one-word changes in safe nonovernight intermediate order, arms exclusively the already proven original OEMW d23 / S92 one UART/RX/DE sender, requires genuine exact controller FC16 acceptance for each before automatically issuing the NEXT *distinct* field (never retransmit), then requests fresh owned F1 3/3 for final exact whole-program persistence; failures stop with no further fields. Preserves original CRC/V5/B11C/B11D/DE/collision, native FC16/FC03/CURRENT/CAL recovery/ABORT; all other HA/calendar setting writes stay on HOLD. Separate disabled-by-default Stop P4 Batch stops subsequent fields (current OEMW may finish); immediate native abort still S92 ABORT. 10-entry complete private ZIP with full YAML, Dutch README, diff, manifest/CRC/SHA and byte-exact W2R55/W2R54/W2R53/W2R52/W2R51 rollback sources; all 1031 W2R55 IDs retained, new coordination 14 IDs. Offline actual P4 rollback four-field scheduling checked. **NOT TARGET COMPILED / NOT FLASHED / NOT LIVE**, does NOT prove controller semantics of automated sequence. Physical controller writes cannot be rolled back by firmware or HA Discard; original Thermia UI fallback. **ONE NEXT ACTION:** user manually compiles/flashes private W2R56, reads real P4, stages original Sun18:20–18:26, presses ONE explicit batch Apply and checks per-field real controller FC16 + final independent owned F1; ABORT and restore via original panel at first failure. Keep W2R54 expanded trial RUNNING / PARTIAL until physical P4 restoration is actually demonstrated.

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
