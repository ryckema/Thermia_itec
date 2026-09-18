# Thermia iTec XTR M → Home Assistant via ESPHome

A **local, read-only ESPHome integration** for a Thermia iTec XTR M heat pump using its internal RS485 communication bus.

This project is based on reverse engineering of a real Thermia iTec XTR M with the older/non-Genesis controller. The bus traffic has been identified as **Modbus RTU** and a number of useful values are decoded into native Home Assistant entities.

> **Current status:** reading is working reliably on the tested system. Writing/control is intentionally disabled for now while bus timing and arbitration are still being investigated.

## What you need

- Thermia iTec (XTR)  with the compatible older/non-Genesis controller
- [Waveshare ESP32-S3-RS485-CAN-U](https://www.waveshare.com/esp32-s3-rs485-can.htm) or equivalent ESP32 + isolated RS485 interface
- USB-C power supply for the ESP32
- RJ45 breakout / cable for connecting to the Thermia communication port
- ESPHome + Home Assistant

The provided YAML is written for the **Waveshare ESP32-S3-RS485-CAN-U**.

## Thermia RJ45 bus

On the tested controller the two RJ45 connectors are similar to the 122 / 123 connectors found on older Thermia boards.

Measured pin groups:

| RJ45 pins | Function |
|---|---|
| 1 + 2 | Data A |
| 3 + 4 | Data B |
| 5 + 6 | Bus ground / reference |
| 7 + 8 | +12 V |

### Recommended test wiring

For the Waveshare board, the tested read-only setup is:

| Thermia | Waveshare |
|---|---|
| RJ45 pin 1 | RS485 A+ |
| RJ45 pin 3 | RS485 B- |
| RJ45 pin 5 | **Not connected** |
| RJ45 pins 7/8 | **Not connected** |

Power the ESP32 separately through **USB-C**.

The Waveshare RS485 side is isolated, so do not connect the ESP logic/power ground to the Thermia bus reference when using this setup.

> **Do not power the ESP from the Thermia +12 V pins unless you have independently verified that the port can safely supply the required current.**

## Bus settings

The bus parameters found on the tested system are:

- Modbus RTU
- 9600 baud
- 8 data bits
- Even parity
- 1 stop bit
- RX inverted in ESPHome

Relevant ESPHome configuration:

```yaml
uart:
  id: thermia_uart

  rx_pin:
    number: GPIO18
    inverted: true

  baud_rate: 9600
  data_bits: 8
  parity: EVEN
  stop_bits: 1
```

TX is intentionally not configured in the shared YAML, so the ESP32 remains passive/read-only.

## Installation

1. Copy `thermia_itEC_xtr_m_readonly.yaml` into your ESPHome configuration directory.
2. Copy the entries from `secrets.example.yaml` into your ESPHome `secrets.yaml`.
3. Replace the placeholder values with your Wi-Fi, API encryption key and OTA password.
4. Connect the RS485 bus as shown above.
5. Power the Waveshare board over USB-C.
6. Validate and install the YAML from ESPHome.
7. Add the ESPHome device to Home Assistant if it is not discovered automatically.

Example `secrets.yaml`:

```yaml
wifi_ssid: "MyWiFi"
wifi_password: "MyWiFiPassword"
api_encryption_key: "GENERATED_BASE64_KEY"
ota_password: "MyOTAPassword"
```

## Home Assistant entities

The currently decoded values include:

- Supply temperature
- Outdoor temperature
- Propagated outdoor temperature on the room-sensor / DCM buses
- DHW temperature
- DHW upper temperature
- DHW delta-T
- Room temperature
- Room setpoint
- Heating curve
- Heating minimum / maximum
- Heating stop temperature
- Reduced temperature
- Room factor
- Condenser inlet temperature
- Condenser outlet temperature
- Condenser delta-T
- Compressor frequency
- Compressor current
- Compressor running
- High pressure
- Outdoor-unit target temperature
- Commanded target temperature
- Outdoor fan speed
- Expansion valve steps
- Controller context
- Outdoor-unit operating state
- Outdoor-unit cycle request / run enable
- SG Ready mode
- Heating / DHW / cooling active state
- Bus health

Additional controller, refrigerant/compressor, DCM and raw-register values are exposed as **diagnostic entities**. Many are disabled by default in Home Assistant and can be enabled from the device entity list when needed for reverse engineering or troubleshooting.

For high-level Home Assistant status, do **not** treat outdoor-unit state `0x0014` as a compressor-running flag. Physical compressor operation is derived from compressor frequency (`0x1E FC04 0x000B > 0 Hz`).


## Register map

The map below contains the mappings that are most useful for the shared integration. A separate detailed register-map document can be used for the full reverse-engineering notes and unresolved observations.

Certainty levels:

- **Confirmed** — matched against a known value, controlled test, repeated operating behaviour or the physical Thermia display.
- **High** — behaviour and scaling strongly match the proposed meaning, but have not yet been independently verified in every operating state.
- **Tentative** — plausible and correlated, but still needs a targeted test.
- **External** — reported for a related Thermia / Danfoss implementation but not yet verified on this XTR M.
- **Unknown** — observed on the bus, but meaning not identified.

### Protocol overview

- Modbus RTU
- 9600 baud
- 8 data bits
- Even parity
- 1 stop bit
- Observed slave IDs: `0x02`, `0x06`, `0x0A`, `0x0F`, `0x14`, `0x1E`
- Observed functions: FC04, FC16 (`0x10`), FC17

---

## Slave `0x02`

### FC17 read block — `0xA7F8`

| Register | Meaning | Scale / values | Certainty |
|---|---|---|---|
| `0xA7F8` | Supply temperature | °C | **Confirmed** |
| `0xA7F9` | Unknown / often unavailable | often `-1000` | **Unknown** |
| `0xA7FA` | Unknown / often unavailable | often `-1000` | **Unknown** |
| `0xA7FB` | DHW upper temperature | °C | **Confirmed** |
| `0xA7FC` | DHW main / lower / control temperature | °C | **Confirmed** |
| `0xA7FD` | SG Ready discriminator 1 | stable values `-1000` / `+1000` | **Confirmed** |
| `0xA7FE` | Unknown | often `-1000` | **Unknown** |
| `0xA7FF` | Unknown | often `-1000` | **Unknown** |
| `0xA800` | Unknown | often `-1000` | **Unknown** |
| `0xA801` | Unknown | often `-1000` | **Unknown** |
| `0xA802` | Outdoor temperature | °C | **Confirmed** |
| `0xA803` | SG Ready discriminator 2 | `224` / `232` | **Confirmed** |
| `0xA804` | Unknown | often `30` | **Unknown** |
| `0xA805` | Unknown | often `-1000` | **Unknown** |
| `0xA806` | Unknown | often `-1000` | **Unknown** |

### FC17 write part — `0xA80C`

| Register | Meaning | Scale / values | Certainty |
|---|---|---|---|
| `0xA80C` | Controller context / state | observed `64`, `65`, `66`, `112`, `193` | **High** |
| `0xA80D` | Unknown | often `0` | **Unknown** |
| `0xA80E` | Controller / accessory status bitfield | observed `0`, `8`, `32`, `40` | **Tentative** |
| `0xA80F` | Controller Sequence Value Raw | observed `5`, `10`, `50`, `75–80`, `81–100` | **High** |
| `0xA810` | Unknown | often `10` | **Unknown** |
| `0xA811` | Unknown | often `-1` | **Unknown** |
| `0xA812` | Unknown | often `0` | **Unknown** |

Observed `A80C` contexts:

| Raw value | Interpretation | Certainty |
|---:|---|---|
| `64` | Normal / baseline controller context | **High** |
| `65` | DHW / high-temperature context | **High** |
| `66` | Cooling context | **High** |
| `112` | Controller housekeeping / transition | **Tentative** |
| `193` | Compound / unknown state | **Tentative** |

`A80F` should **not** be interpreted as a percentage. Repeated heating cycles show the pattern `50 → 80` before cycle start, followed later by `80 → 79 → 78 → 77 → 76 → 75`. During shutdown it returns via `75 → 80 → 50`. The exact internal meaning is still unknown, but it behaves like a controller sequence/control value rather than a simple demand percentage.

### SG Ready mapping

| SG state | `A7FD` | `A803` | Certainty |
|---|---:|---:|---|
| Normal | `-1000` | `224` | **Confirmed** |
| Blocked | `-1000` | `232` | **Confirmed** |
| Enhanced | `+1000` | `224` | **Confirmed** |
| Peak | `+1000` | `232` | **Confirmed** |

Short-lived intermediate values such as `A7FD = 85` have been observed while switching and should be treated as transient/invalid rather than as an additional SG mode.

---

## Slave `0x0A` — room sensor

### FC17 read

| Register | Meaning | Scale / values | Certainty |
|---|---|---|---|
| `0xB3B0` | Room temperature | ×0.1 °C | **Confirmed** |
| `0xB3B1` | Genuine room-sensor payload word 1 | genuine sensor reported `0` | **External / High** |
| `0xB3B2` | Genuine room-sensor payload word 2 | genuine sensor reported `0` | **External / High** |

### FC17 write part

| Register | Meaning | Scale / values | Certainty |
|---|---|---|---|
| `0xB3C4` | Propagated outdoor temperature | °C | **Confirmed** |
| `0xB3C5` | Room setpoint | °C | **Confirmed** |
| `0xB3C6` | Room-sensor boost / enhanced request | observed `0` / `2` | **High** |

Repeated logging shows the central outdoor temperature propagating from `0x02:A802` to `0x0A:B3C4` and then to `0x06:AFE0`.

---

## Slave `0x0F` — settings

### Heating block

| Register | Decimal | Meaning | Scale / values | Certainty |
|---|---:|---|---|---|
| `0x03E8` | `1000` | Heating curve | integer | **Confirmed** |
| `0x03E9` | `1001` | Heating minimum | °C | **Confirmed** |
| `0x03EA` | `1002` | Heating maximum | °C | **Confirmed** |
| `0x03EB` | `1003` | Curve correction +5 | temperature correction | **Confirmed** |
| `0x03EC` | `1004` | Curve correction 0 | temperature correction | **Confirmed** |
| `0x03ED` | `1005` | Curve correction -5 | temperature correction | **Confirmed** |
| `0x03EE` | `1006` | Heating stop | °C | **Confirmed** |
| `0x03EF` | `1007` | Reduced temperature | °C | **Confirmed** |
| `0x03F0` | `1008` | Room factor | integer | **Confirmed** |
| `0x03F1` | `1009` | Unknown | often `40` | **Unknown** |
| `0x03F2` | `1010` | Unknown | often `30` | **Unknown** |
| `0x03F3` | `1011` | Unknown | often `1` | **Unknown** |
| `0x03F4` | `1012` | Room setpoint mirror | °C | **High** |
| `0x03F5` | `1013` | Unknown | often `2` | **Unknown** |

### DHW settings block — reported externally

Another researcher reports a DHW settings block at decimal registers `1053–1059` (`0x041D–0x0423`). The exact mapping has not yet been verified on this XTR M and remains **External**.

### Cooling settings block — reported externally

Another researcher reports cooling-related settings at decimal registers `1090–1102` (`0x0442–0x044E`). The exact register-to-setting mapping still needs controlled captures while changing one display setting at a time.

---

## Slave `0x1E` — outdoor unit

### FC04 telemetry

| Register | Meaning | Scale / values | Certainty |
|---|---|---|---|
| `0x0000` | Condenser inlet temperature | ×0.1 °C | **Confirmed** |
| `0x0001` | Condenser outlet temperature | ×0.1 °C | **Confirmed** |
| `0x0002` | Refrigerant temperature 1 | ×0.1 °C | **High** |
| `0x0003` | Discharge gas temperature | ×0.1 °C | **High** |
| `0x0004` | Refrigerant temperature 2 | ×0.1 °C | **High** |
| `0x0005` | Average outdoor temperature | ×0.1 °C | **High** |
| `0x0006` | Compressor temperature | ×0.1 °C | **High** |
| `0x0007` | Unknown | — | **Unknown** |
| `0x0008` | High pressure | ×0.1 bar | **Confirmed — display matched** |
| `0x0009` | Unknown | — | **Unknown** |
| `0x000A` | Outdoor-unit target temperature | ×0.1 °C | **Confirmed — display matched** |
| `0x000B` | Compressor frequency | Hz | **Confirmed — display matched** |
| `0x000C` | Unknown | — | **Unknown** |
| `0x000D` | Compressor current | ×0.1 A | **Confirmed — display matched** |
| `0x000E` | Outdoor fan speed | rpm | **Confirmed — display matched** |
| `0x000F` | Unknown | — | **Unknown** |
| `0x0010` | Expansion valve position | steps | **Confirmed — display matched** |
| `0x0011` | Unknown | — | **Unknown** |
| `0x0012` | Unknown on tested unit; externally reported max-frequency ratio | % | **External** |
| `0x0013` | Unknown | — | **Unknown** |
| `0x0014` | Outdoor-unit operating / sequence state | enum | **Confirmed / High** |
| `0x0015` | Outdoor-unit status / context bitfield | bitfield | **High** |
| `0x001F` | Unknown, observed during state-20 recovery sequence | observed `0 → 911` | **Unknown / correlated** |
| `0x0023` | Unknown, observed during state-20 recovery sequence | observed `0 → 4` | **Unknown / correlated** |

### `0x0014` operating-state values

| Raw value | Meaning | Certainty |
|---:|---|---|
| `16` | Idle | **Confirmed** |
| `18` | Late shutdown / final transition | **Tentative** |
| `20` | Recovery / autonomous outdoor-unit sequence | **Tentative** |
| `24` | Preparation / transition / shared finalisation | **Confirmed / High** |
| `25` | Heating/DHW shutdown / fan-stop stage | **High** |
| `26` | Cooling shutdown transition | **High** |
| `27` | Cooling shutdown / likely earlier fan-stop stage | **High** |
| `28` | Heating/DHW startup / ramp; also seen in shutdown | **High** |
| `29` | Heating/DHW established sequence | **Confirmed as sequence-state** |
| `30` | Cooling startup / ramp | **High** |
| `31` | Cooling established sequence | **High** |

`0x0014` is a **sequence state**, not a compressor-running flag. The compressor may already be running in state `28` / `30`, and state `29` may persist after compressor frequency reaches zero.

### Observed state-machine paths

Heating / DHW startup:

`16 → 24 → 28 → 29`

Common Heating / DHW shutdown:

`29 → 25 → 24 → 16`

Alternative Heating / DHW shutdown:

`29 → 28 → 24 → 16`

Cooling startup:

`16 → 24 → 30 → 31`

Cooling shutdown:

`31 → 27 → 26 → 24 → 16`

### State `20` — recovery / autonomous sequence

State `20` was observed after an SG-triggered DHW start was aborted. The normal controller request had already been removed (`FC16 0x0007 = 0`, `0x0008 = 0`) before the outside unit entered `16 → 20` on its own.

During that sequence the outdoor fan started and ramped, the expansion valve moved, `0x001F` changed to `911`, `0x0023` changed to `4`, and the compressor briefly ran up to about 20 Hz even though the normal controller cycle request was already off.

The safest current label is therefore **Recovery / autonomous outdoor-unit sequence**. It should not yet be called defrost.

### `0x0015` status / context bitfield

Observed values include:

- `33` = `0x021`
- `65` = `0x041`
- `129` = `0x081`
- `545` = `0x221`
- `577` = `0x241`
- `641` = `0x281`

| Bit | Meaning | Certainty |
|---|---|---|
| `0x0001` | Common / base flag | **Tentative** |
| `0x0020` | Heating context | **High** |
| `0x0040` | DHW / high-temperature context | **Confirmed** |
| `0x0080` | Cooling context | **Confirmed** |
| `0x0200` | Controller run-enable acknowledged / active | **Confirmed** |

`0x0200` is **not** physical compressor-running state and is not a universal prerequisite for compressor operation; the state-20 recovery sequence demonstrated a brief compressor run after this bit had cleared.

---

## Slave `0x1E` — FC16 command block from controller to outdoor unit

| Register | Meaning | Scale / values | Certainty |
|---|---|---|---|
| `0x0000` | Unknown / possible demand-related field | — | **Unknown** |
| `0x0001` | Commanded target temperature | ×0.1 °C | **Confirmed — display matched** |
| `0x0002` | Unknown | — | **Unknown** |
| `0x0003` | Unknown | — | **Unknown** |
| `0x0004` | Mode request | `1=Heating`, `2=DHW/high-temp`, `3=Cooling` | **Confirmed / High** |
| `0x0005` | Unknown | — | **Unknown** |
| `0x0006` | Unknown; possible periodic counter/state | observed `0→1→2`, ~2 h spacing in one capture | **Tentative** |
| `0x0007` | Outdoor-unit cycle / sequence request | `0/1` | **Confirmed** |
| `0x0008` | Outdoor-unit run enable | `0/1` | **Confirmed** |

Repeated heating cycles show `A80F 50 → 80` immediately before `0x0007` turns on, and `A80F 80 → 50` immediately before `0x0007` turns off. This makes `0x0007` a reliable overall cycle/sequence request.

`0x0008` is a separate run-enable command. This does **not** match an external mapping that labelled the same register as an electric-heater state.

---

## Slave `0x06` — Online / Connect / DCM slot

Observed polling:

- FC17 read around `0xAFC8`, count 12
- FC17 write around `0xAFDC`, count 5

| Register | Meaning | Scale / values | Certainty |
|---|---|---|---|
| `0xAFDC` | DCM / accessory status word | observed `0`, `16`, `32` and compound states | **High correlation / semantic Tentative** |
| `0xAFDD` | DCM / accessory housekeeping / preparation word | observed `0`, `16` | **Tentative** |
| `0xAFE0` | Propagated outdoor temperature | °C | **Confirmed** |

`AFDC` should not be interpreted as a heating/DHW/cooling mode. `AFDC 0x20` repeatedly correlates with `A80E 0x20`, while `AFDC 0x10` and `AFDD 0x10` have been seen during controller/accessory housekeeping and propagation events.

---

## Slave `0x14`

Observed FC04 block at `0x0000`, count 12.

Meaning is still unknown; likely an optional module / accessory block.

**Certainty: Unknown**

---

## Derived values

| Derived value | Source | Certainty |
|---|---|---|
| Compressor running | `0x1E FC04 0x000B > 0 Hz` | **Confirmed** |
| Heating active | heating context + compressor running + FC16 `0x0007 = 1` | **High** |
| DHW active | DHW context + compressor running + FC16 `0x0007 = 1` | **High** |
| Cooling active | cooling context + compressor running + FC16 `0x0007 = 1` | **High** |
| Condenser delta-T | `0x0001 - 0x0000` | **Confirmed** |
| DHW delta-T | `0xA7FB - 0xA7FC` | **Confirmed** |
| SG Ready mode | stable combination of `0xA7FD` + `0xA803` | **Confirmed** |

The extra `0x0007 = 1` condition prevents an autonomous state-20 compressor run from being incorrectly labelled as Heating, DHW or Cooling active.

---

## Display-correlated values

A physical-display snapshot provided direct cross-checks for:

| Display value | Bus register |
|---|---|
| Setpoint / target temperature | `0x1E FC04 0x000A` |
| Commanded setpoint | `0x1E FC16 0x0001` |
| Compressor frequency | `0x1E FC04 0x000B` |
| Compressor current | `0x1E FC04 0x000D` |
| High pressure | `0x1E FC04 0x0008` |
| Outdoor fan speed | `0x1E FC04 0x000E` |
| Expansion valve steps | `0x1E FC04 0x0010` |

---

## Recommended Home Assistant interpretation

For a single user-facing heat-pump state, the safest current order is:

1. ESP unavailable → `Offline`
2. bus unhealthy → `Bus fault`
3. compressor running + cooling context + `0x0007 = 1` → `Cooling`
4. compressor running + DHW context + `0x0007 = 1` → `DHW`
5. compressor running + heating context + `0x0007 = 1` → `Heating`
6. `0x0014 = 20` → `Recovery / autonomous sequence`
7. startup sequence (`24`, `28`, `30`) before compressor operation → `Starting / transition`
8. compressor off while `0x0014 != 16` → `Post-run / transition`
9. `0x0014 = 16` → `Idle`

This deliberately keeps raw controller / sequence values separate from the normal user-facing status.

## Troubleshooting

### No data / Bus Healthy is off

Check:

- A/B wiring
- 9600 8E1 settings
- that `GPIO18` is used as RS485 RX on the Waveshare board
- that RX remains configured with `inverted: true`
- that the ESP is connected to the correct Thermia communication port

If necessary, try swapping A and B. RS485 naming conventions are unfortunately not consistent between manufacturers.

### Home Assistant shows lots of unavailable diagnostic entities

That is expected for some raw registers. The controller uses sentinel values such as `-1000` for unavailable sensors/fields, and not every register is populated on every installation.

### Can this control the heat pump?

Not yet in this shared version.

The bus contains writable parameters, including the room setpoint, but adding another transmitter to a bus with an existing master requires proper timing/arbitration. TX is therefore intentionally disabled until this can be done safely and reliably.

## Safety / compatibility

This is an unofficial reverse-engineered integration and is **not affiliated with or supported by Thermia**.

The register map is based on one Thermia iTec XTR M installation. Other Thermia iTec revisions or related models may use different boards, bus wiring, slave addresses or register layouts.

Start with read-only operation and verify the RJ45 pinout on your own hardware before connecting anything.

## Development status

Read-only monitoring is stable on the tested installation and the register map is still being expanded. Several controller and outdoor-unit sequence states have now been decoded, including normal heating/cooling startup and shutdown paths, SG Ready state, run-enable signalling and a special autonomous recovery sequence.

Write support is intentionally not included. Initial tests involving writable values were not reliable enough, and adding another transmitter to the existing bus requires correct timing and arbitration. The shared integration therefore remains passive/read-only.
