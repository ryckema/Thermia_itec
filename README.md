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
