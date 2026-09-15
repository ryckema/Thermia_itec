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
- DHW temperature
- DHW upper temperature
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
- Target temperature
- Outdoor fan speed
- Expansion valve steps
- SG Ready mode
- Bus health

Additional refrigerant/compressor values and raw registers are also exposed as **diagnostic entities** and are **disabled by default** in Home Assistant. They can be enabled from the device's entity list when needed for testing.


## Register map

Certainty levels used below:

- **Confirmed** — matched against a known value or controlled test.
- **High** — behaviour and scaling strongly match the proposed meaning, but it has not yet been independently verified in every operating state.
- **Tentative** — plausible based on behaviour, naming context or correlation, but still needs a targeted test.
- **Unknown** — register is observed on the bus, but its meaning has not yet been identified.
## Slave `0x02`

### FC17 read block — `0xA7F8`

| Register | Meaning | Scale / values | Certainty |
|---|---|---|---|
| `0xA7F8` | Supply temperature | °C | **Confirmed** |
| `0xA7F9` | Unknown / often unavailable | often `-1000` | **Unknown** |
| `0xA7FA` | Unknown / often unavailable | often `-1000` | **Unknown** |
| `0xA7FB` | DHW upper temperature | °C | **Confirmed** |
| `0xA7FC` | DHW main / lower / control temperature | °C | **Confirmed** |
| `0xA7FD` | SG Ready discriminator 1 | usually `-1000` / `+1000` | **Confirmed** |
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
| `0xA80E` | Controller bitfield | observed `0`, `8`, `32`, `40` | **Tentative** |
| `0xA80F` | Control Request Level Raw | observed `5`, `10`, `50`, `80`, `100` | **High** |
| `0xA810` | Unknown | often `10` | **Unknown** |
| `0xA811` | Unknown | often `-1` | **Unknown** |
| `0xA812` | Unknown | often `0` | **Unknown** |

Observed `A80C` contexts:

| Raw value | Interpretation | Certainty |
|---:|---|---|
| `64` | Normal / baseline controller context | **High** |
| `65` | DHW / high-temperature context | **High** |
| `66` | Cooling requested / cooling context | **High** |
| `112` | Transition state | **Tentative** |
| `193` | Compound / unknown state | **Tentative** |

> `A80F` should not be interpreted as a percentage. It is a raw controller request level.

### SG Ready mapping

Observed real combinations:

| SG state | `A7FD` | `A803` |
|---|---:|---:|
| Normal | `-1000` | `224` |
| Blocked | `-1000` | `232` |
| Enhanced | `+1000` | `224` |
| Peak | `+1000` | `232` |

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
| `0xB3C4` | Propagated outdoor temperature | °C | **High** |
| `0xB3C5` | Room setpoint | °C | **Confirmed** |
| `0xB3C6` | Room-sensor boost / enhanced request | observed `0` / `2` | **High** |

External researcher note: the display pushes `[outdoor, room setpoint, 0]` to the room-sensor accessory, while a genuine sensor returns its own payload rather than echoing the push.

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

Another researcher reports a DHW settings block at decimal registers `1053–1059`.

| Decimal range | Hex range | Meaning | Certainty |
|---|---|---|---|
| `1053–1059` | `0x041D–0x0423` | DHW start temperature, run time, top-up interval / stop / time, sensor influence, ECO influence | **External** |

These values should be verified against the physical display before being promoted to confirmed mappings.

### Cooling settings block — reported externally

Another researcher reports the cooling settings block at decimal registers `1090–1102`.

| Decimal range | Hex range | Meaning | Certainty |
|---|---|---|---|
| `1090–1102` | `0x0442–0x044E` | Cooling enabled, desired cooling temperature, hysteresis / room-sensor related cooling settings | **External** |

On the tested XTR M, the physical display currently shows cooling parameters including:

- Cooling: ON
- Desired cooling temperature: 18 °C
- Cooling active threshold: 25 °C
- START: 50
- STOP: -30
- Cooling time: 20 min
- Room sensor: ON
- Low room deviation: 1.0 °C
- High room deviation: 1.0 °C

The exact register-to-setting mapping within `1090–1102` still needs a targeted capture.

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
| `0x0014` | Outdoor-unit operating state | enum | **Confirmed / High** |
| `0x0015` | Outdoor-unit status / mode bitfield | bitfield | **High** |

External report:
- `0x0014` decimal register `20` / `0x0014`
- `0x0015` decimal register `21` / `0x0015`
- another researcher also reports reg20/21 as superheat/subcooling on a related interpretation; this conflicts with the state/status behaviour observed on the tested XTR M and should therefore **not** be applied without model-specific verification.

### `0x0014` operating-state values

| Raw value | Meaning | Certainty |
|---:|---|---|
| `16` | Idle | **Confirmed** |
| `24` | Preparing / transition | **Confirmed** |
| `26` | Cooling shutdown / post-run stage | **High** |
| `27` | Cooling shutdown / post-run stage | **High** |
| `28` | Heating / DHW pre-run | **High** |
| `29` | Heating / DHW compressor running | **Confirmed** |
| `30` | Cooling pre-run | **Confirmed** |
| `31` | Cooling compressor running | **Confirmed** |

Observed cooling shutdown sequence:

`31 → 27 → 26 → 24 → 16`

### `0x0015` status bitfield

Observed values include:

- `33` = `0x021`
- `65` = `0x041`
- `129` = `0x081`
- `545` = `0x221`
- `577` = `0x241`
- `641` = `0x281`

Current bit interpretation:

| Bit | Meaning | Certainty |
|---|---|---|
| `0x0001` | Common / base flag | **Tentative** |
| `0x0020` | Heating context | **High** |
| `0x0040` | DHW / high-temperature context | **Confirmed** |
| `0x0080` | Cooling context | **Confirmed** |
| `0x0200` | Outdoor-unit run / request active | **Confirmed** |

> `0x0200` is not the same as physical compressor running. Physical compressor running is best derived from `0x000B > 0 Hz`.

---

## Slave `0x1E` — FC16 / command block from controller to outdoor unit

The controller writes a command block to the outdoor unit. The ESPHome implementation remains passive and only observes these writes.

| Register | Meaning | Scale / values | Certainty |
|---|---|---|---|
| `0x0000` | Unknown / possible demand-related field | — | **Unknown** |
| `0x0001` | Commanded target temperature | ×0.1 °C | **Confirmed — display matched** |
| `0x0002` | Unknown | — | **Unknown** |
| `0x0003` | Unknown | — | **Unknown** |
| `0x0004` | Mode request | `1=Heating`, `2=DHW/high-temp`, `3=Cooling` | **Confirmed / High** |
| `0x0005` | Unknown | — | **Unknown** |
| `0x0006` | Unknown | — | **Unknown** |
| `0x0007` | Outdoor-unit cycle / flow request | `0/1` | **High** |
| `0x0008` | Outdoor-unit run enable | `0/1` | **Confirmed** |

Important model-specific observation:

On the tested XTR M, FC16 register `0x0008` behaves as a **run-enable** signal. During cooling it changes `0 → 1` before the outside unit enters its running state and before compressor frequency rises above zero. This does **not** match an external mapping that labelled the same word as an electric-heater state.

### Confirmed cooling start sequence

Observed sequence:

1. Controller context changes to cooling (`A80C = 66`)
2. `A80F` request level rises
3. FC16 `0x0001` target changes toward cooling target
4. FC16 `0x0004 = 3`
5. FC16 `0x0007 = 1`
6. FC04 `0x000A` mirrors the target
7. FC04 `0x0015`: DHW/previous context → cooling context (`129`)
8. FC04 `0x0014`: `16 → 24`
9. FC16 `0x0008 = 1`
10. FC04 `0x0015`: `129 → 641`
11. FC04 `0x0014`: `24 → 30`
12. Compressor frequency rises above `0 Hz`
13. FC04 `0x0014`: `30 → 31`

---

## Slave `0x06` — Online / Connect / DCM slot

Observed polling:

- FC17 read around `0xAFC8`, count 12
- FC17 write around `0xAFDC`, count 5

| Register | Meaning | Scale / values | Certainty |
|---|---|---|---|
| `0xAFDC` | Status / control-related word | — | **Tentative** |
| `0xAFDD` | Prep / status-related word | — | **Tentative** |
| `0xAFE0` | Propagated outdoor temperature | °C | **High** |

External researcher observation:

An accessory responds with its own data rather than echoing the display's write payload. Therefore the 12-register response from a Thermia Online / Connect / Danfoss DCM accessory should be treated as the module's own payload, not as a mirror of the controller push.

The accessory protocol appears stable across display firmware 2.3.0 and 2.4.2 according to external testing.

---

## Slave `0x14`

Observed FC04 block at `0x0000`, count 12.

Meaning is still unknown; likely an optional module / accessory block.

**Certainty: Unknown**

---

## Derived values

| Derived value | Source | Certainty |
|---|---|---|
| Compressor running | `0x1E:0x000B > 0 Hz` | **Confirmed** |
| Heating active | heating context bit + compressor running | **High** |
| DHW active | DHW context bit + compressor running | **High** |
| Cooling active | cooling context bit + compressor running | **Confirmed** |
| Condenser delta-T | `0x0001 - 0x0000` | **Confirmed** |
| DHW delta-T | `0xA7FB - 0xA7FC` | **Confirmed** |
| SG Ready mode | combination of `0xA7FD` + `0xA803` | **Confirmed** |

---

## Display-correlated values

A physical-display snapshot taken while the bus was being logged provided direct cross-checks for the following telemetry:

| Display value | Bus register |
|---|---|
| Setpoint / target temperature | `0x1E FC04 0x000A` |
| Commanded setpoint | `0x1E FC16 0x0001` |
| Compressor frequency | `0x1E FC04 0x000B` |
| Compressor current | `0x1E FC04 0x000D` |
| High pressure | `0x1E FC04 0x0008` |
| Outdoor fan speed | `0x1E FC04 0x000E` |
| Expansion valve steps | `0x1E FC04 0x0010` |

During the display capture, the outdoor-unit target was 19.0 °C, compressor frequency was about 16–17 Hz, compressor current about 0.8–0.9 A, and high pressure about 13.2–13.5 bar. These values matched the live bus decode.

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

The mapping is still being expanded, with return temperature, operating states/status bits and additional internal temperatures among the remaining targets.

Write support will also be investigated further, but the public YAML will remain read-only until bus arbitration and safe write behaviour are understood.
