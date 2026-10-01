# Thermia iTec XTR M → Home Assistant via ESPHome

Local ESPHome integration and reverse-engineering project for the **Thermia iTec XTR M** internal RS485 bus, tested on an older/non-Genesis controller.

The repository has two deliberately separated runtime builds:

| Build | Bus access | Intended use | Current status |
|---|---|---|---|
| [Read-only](Read-only/) | RX only | Monitoring, dashboards, register research | Recommended for normal monitoring |
| [Write (Beta)](Write%20%28Beta%29/) | RX + guarded TX | Native multi-setting control | Locally working, still Beta |

The underlying bus is **Modbus RTU-like, 9600 baud, 8E1 with Modbus CRC**.

> **Current write status — Write Beta v4.0:** native page-owned semantic writes are locally confirmed on `03E8/count14`, `042E/count15`, `0442/count13` and `0546/count20`. EXP381B is the current COMPLETE / POSITIVE runtime baseline. v4.0 also contains seven clearly named **TEST** controls from EXP382/EXP383; those mappings are STRONGLY SUPPORTED but not yet locally proven.

## Choose a build

### Read-only — recommended for monitoring

Use the [Read-only folder](Read-only/) when you only need Home Assistant monitoring or want to inspect the Thermia bus without transmitting anything.

Two variants are maintained:

- **Public / optimized** — quiet, lower-overhead build for normal Home Assistant use.
- **Research / register mapping** — still RX-only, but includes raw logging, register mapping and additional diagnostics.

Current XTR files:

- `Read-only/Thermia itec XTR/thermia_itec_xtr_m_waveshare_public_v28.yaml`
- `Read-only/Thermia itec XTR/thermia_itec_xtr_m_waveshare_research_v28.yaml`

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

Useful read-only entities including expansion-valve steps, refrigerant temperatures, discharge-gas temperature, compressor temperature and Room Setpoint Mirror are enabled by default in the current write baseline.

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

## Current experiment status

- **EXP380 — COMPLETE / POSITIVE:** Operation Mode `0553` native write path locally confirmed.
- **EXP381B — COMPLETE / POSITIVE:** production/UI consolidation ran successfully and is the current proven runtime baseline.
- **EXP382 — COMPLETE / POSITIVE, offline:** narrowed remaining controlled-page gaps without bus TX.
- **EXP383 — PREPARED / NOT RUN:** seven STRONGLY SUPPORTED mappings are exposed as TEST controls in Write Beta v4.0 for one-at-a-time validation.

## Roadmap

The current roadmap after EXP383 validation is:

1. **Kalenderfunctionaliteit**
2. **Missende entiteiten toevoegen**
3. **Storingen/alarmen uitlezen**
4. **Volledige native settings-map afronden**
5. **Generieke DCM/Online-emulator maken**
6. **Challenge-response oplossen**
7. **Defrost + volledig operating-state model**
8. **Cross-model vergelijking**

The cross-model step is intended as a **supported-types compatibility effort**: establish which Thermia/Danfoss models share the required bus architecture, pages, mappings and safe control behavior rather than assuming compatibility from platform similarity.

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

## Project status

Read-only monitoring remains the conservative choice and is strictly passive.

Write support now follows a locally proven native Online/DCM-style page mechanism across multiple setting pages. The active build remains intentionally isolated under **Write (Beta)** because it transmits on the heat-pump bus, controller-session recovery is model/context-specific, the native challenge-response transform is not yet reconstructed, and v4.0 includes clearly marked TEST mappings awaiting local validation.

## Disclaimer and license

This is an **independent, unofficial reverse-engineering and integration project**. It is not affiliated with, endorsed by, or supported by Thermia, Danfoss, ESPHome, Home Assistant, or Waveshare.

The software, documentation, protocol information and example configurations in this repository are provided **“as is”, without warranty of any kind**. The Read-only configurations are designed to operate passively. The Write (Beta) configuration actively transmits data on the heat pump's internal communication bus and may alter heat-pump settings. Incorrect wiring, configuration, modification, software defects or unexpected protocol behaviour may result in malfunction, loss of heating or hot water, equipment damage, or other unintended operation.

Use of this project is at your own risk. Verify the wiring, configuration, operating limits and safety behaviour for your own installation before use. The authors and contributors accept no responsibility for damage, loss, warranty issues or other consequences resulting from use or modification of this project, **to the extent permitted by applicable law**.

Protocol findings apply only to the systems on which they were actually tested unless explicitly stated otherwise. Cross-model Thermia/Danfoss findings must not be treated as proven behavior for another model.

The software in this repository is released under the [MIT License](LICENSE). The MIT License includes its own warranty and liability limitations; this project-specific disclaimer provides additional context about interaction with physical HVAC equipment.
