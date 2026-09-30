# Thermia iTec XTR M → Home Assistant via ESPHome

Local ESPHome integration and reverse-engineering project for the **Thermia iTec XTR M** internal RS485 bus, tested on an older/non-Genesis controller.

The repository now has two deliberately separated runtime builds:

| Build | Bus access | Intended use | Current status |
|---|---|---|---|
| [Read-only](Read-only/) | RX only | Monitoring, dashboards, register research | Recommended for normal monitoring |
| [Write (Beta)](Write%20%28Beta%29/) | RX + guarded TX | Native Room Setpoint control | Locally working, still Beta |

The underlying bus is **Modbus RTU, 9600 baud, 8E1**. The read-only integration decodes Thermia values into Home Assistant. The write research has additionally reconstructed enough of the native Thermia/Danfoss Online/DCM path to change one setting safely on the tested unit.

> **Current write status — EXP353:** Room Setpoint control is locally confirmed on the tested XTR M. EXP352 contains the newest archived raw-log proof of the complete refresh → desired-page write → controller-republish flow. EXP353 was explicitly confirmed successful for reusable refreshes, but its detailed raw log/YAML is not currently archived. For that reason the active build remains **Write (Beta)** rather than being presented as universally production-ready.

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

### Write (Beta) — Room Setpoint control

Use the [Write (Beta) folder](Write%20%28Beta%29/) only when you intentionally want active control.

Current file:

- `Write (Beta)/thermia_itec_xtr_m_waveshare_write_beta_v1.yaml`

The beta currently enables exactly one semantic setting:

- **Room Setpoint** — `0x03F4` inside controller page `0x03E8/count14`, whole degrees **10..30 °C**.

Changing the Home Assistant number does **not** immediately transmit a write. The transaction starts only when **Thermia Apply Room Setpoint** is pressed.

See [Write (Beta)/README.md](Write%20%28Beta%29/README.md) before installing it.

## Tested hardware

The supplied YAML files target:

- Thermia iTec XTR M with the compatible older/non-Genesis controller
- Waveshare ESP32-S3-RS485-CAN / ESP32-S3-RS485-CAN-U
- onboard isolated RS485 transceiver
- ESPHome
- Home Assistant

Other Thermia/Danfoss models are useful cross-model evidence for the research, but compatibility of the write path must **not** be assumed.

## Thermia RS485 connection

The tested Thermia RJ45 connection is:

| Thermia RJ45 | Waveshare |
|---|---|
| pin 1 — RS485 A | A+ |
| pin 3 — RS485 B | B- |
| pin 5 — bus reference | not connected in the tested isolated setup |
| pins 7/8 — +12 V | not connected |

Power the ESP32 separately over USB-C.

Leave the Waveshare **120 Ω termination jumper open/off** when passively attaching to the existing Thermia bus. Do not power the ESP32 from the Thermia +12 V pins unless that supply has been independently verified for the intended load.

### Bus parameters

```text
Modbus RTU
9600 baud
8 data bits
Even parity
1 stop bit
```

On the Waveshare build:

- GPIO18 = RS485 RX
- GPIO17 = RS485 TX in the Write (Beta) build only
- GPIO21 = RS485 DE/direction

The read-only builds intentionally do not configure TX and keep DE low.

## Home Assistant

The integration currently exposes useful values including room, outdoor, supply and DHW temperatures; heating settings; compressor and outdoor-unit telemetry; SG Ready state; operating-state information; and bus/ESP diagnostics.

The research build exposes additional raw/register diagnostics. The Write (Beta) build preserves the monitoring functionality and adds the guarded Room Setpoint controls and write-status entities.

## ESPHome secrets

The YAML files expect these entries in your ESPHome `secrets.yaml`:

```yaml
wifi_ssid: "..."
wifi_password: "..."
thermia_api_encryption_key: "..."
thermia_ota_password: "..."
thermia_fallback_password: "..."
```

Do not commit real credentials to this repository.

## Research and evidence

The reverse-engineering history is kept separately from the runtime builds:

- [THERMIA_PROJECT_STATE.md](Research/THERMIA_PROJECT_STATE.md) — authoritative current state
- [EXPERIMENT_LOG.md](Research/EXPERIMENT_LOG.md) — experiment history, including negative and inconclusive results
- [PROTOCOL_FINDINGS.md](Research/PROTOCOL_FINDINGS.md) — durable protocol findings and evidence classification

The project distinguishes local XTR M proof from genuine Online/DCM capture evidence, firmware-derived findings, cross-model Thermia/Danfoss evidence and hypotheses.

## Current write model

The locally established Room Setpoint path is:

```text
persistent DCM runtime
    ↓
fresh 03E8 page when needed
0708 W3 bit0
    ↓
controller FC16 03E8/count14
    ↓
0708 W1 bit0 + W3 bit0 selector
    ↓
controller FC03 03E8/count14
    ↓
response changes only 03F4
    ↓
controller FC16 03E8/count14 republish
    ↓
republish becomes the source for the next write
```

Important boundaries remain: only `03F4` is enabled for semantic writes; W5=`0006` is a proven working runtime value but its abstract meaning is unknown; the full W2:W3 page bitmap is not locally active-tested beyond the `03E8` case; and arbitrary fresh controller-session/power-loss recovery is less mature than retained-session operation.

## Project status

Read-only monitoring is the conservative choice and remains strictly passive.

Write support is no longer a speculative direct-register write: it follows the locally proven native Online/DCM mailbox/page mechanism. It is nevertheless intentionally isolated under **Write (Beta)** until longer-running recovery behavior is characterized.


## Disclaimer and license

This is an **independent, unofficial reverse-engineering and integration project**. It is not affiliated with, endorsed by, or supported by Thermia, Danfoss, ESPHome, Home Assistant, or Waveshare.

The software, documentation, protocol information and example configurations in this repository are provided **“as is”, without warranty of any kind**. The Read-only configurations are designed to operate passively. The Write (Beta) configuration actively transmits data on the heat pump's internal communication bus and may alter heat-pump settings. Incorrect wiring, configuration, modification, software defects or unexpected protocol behaviour may result in malfunction, loss of heating or hot water, equipment damage, or other unintended operation.

Use of this project is at your own risk. Verify the wiring, configuration, operating limits and safety behaviour for your own installation before use. The authors and contributors accept no responsibility for damage, loss, warranty issues or other consequences resulting from use or modification of this project, **to the extent permitted by applicable law**.

Protocol findings apply only to the systems on which they were actually tested unless explicitly stated otherwise. Cross-model Thermia/Danfoss findings must not be treated as proven behavior for another model.

The software in this repository is released under the [MIT License](LICENSE). The MIT License includes its own warranty and liability limitations; this project-specific disclaimer provides additional context about interaction with physical HVAC equipment.
