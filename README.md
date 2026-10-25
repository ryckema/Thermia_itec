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
