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

| Slave | FC | Register | Meaning | Scale / values | Certainty |
|---|---:|---|---|---|---|
| `0x02` | `0x17` | `0xA7F8` | Supply temperature | °C | **High** |
| `0x02` | `0x17` | `0xA7F9` | Unknown / often unavailable | often `-1000` | **Unknown** |
| `0x02` | `0x17` | `0xA7FA` | Unknown / often unavailable | often `-1000` | **Unknown** |
| `0x02` | `0x17` | `0xA7FB` | DHW upper temperature | °C | **Confirmed** |
| `0x02` | `0x17` | `0xA7FC` | DHW temperature | °C | **Confirmed** |
| `0x02` | `0x17` | `0xA7FD` | SG Ready discriminator 1 | usually `-1000` / `1000`, transition values possible | **Confirmed** |
| `0x02` | `0x17` | `0xA7FE` | Unknown | often `-1000` | **Unknown** |
| `0x02` | `0x17` | `0xA7FF` | Unknown | often `-1000` | **Unknown** |
| `0x02` | `0x17` | `0xA800` | Unknown | often `-1000` | **Unknown** |
| `0x02` | `0x17` | `0xA801` | Unknown | often `-1000` | **Unknown** |
| `0x02` | `0x17` | `0xA802` | Outdoor temperature | °C | **Confirmed** |
| `0x02` | `0x17` | `0xA803` | SG Ready discriminator 2 | `224` / `232` | **Confirmed** |
| `0x02` | `0x17` | `0xA804` | Unknown | often `30` | **Unknown** |
| `0x02` | `0x17` | `0xA805` | Unknown | often `-1000` | **Unknown** |
| `0x02` | `0x17` | `0xA806` | Unknown | often `-1000` | **Unknown** |
| `0x02` | `0x17` write part | `0xA80C` | Control / status bitfield | observed `0`, `64`, `65`, `193` | **Tentative** |
| `0x02` | `0x17` write part | `0xA80D` | Unknown | often `0` | **Unknown** |
| `0x02` | `0x17` write part | `0xA80E` | Unknown | often `0` | **Unknown** |
| `0x02` | `0x17` write part | `0xA80F` | Control / demand level | observed `10`, `50`, `80` | **High** |
| `0x02` | `0x17` write part | `0xA810` | Unknown | often `10` | **Unknown** |
| `0x02` | `0x17` write part | `0xA811` | Unknown | often `-1` | **Unknown** |
| `0x02` | `0x17` write part | `0xA812` | Unknown | often `0` | **Unknown** |
| `0x0A` | `0x17` | `0xB3B0` | Room temperature | ×0.1 °C | **Confirmed** |
| `0x0A` | `0x17` | `0xB3B1` | Unknown | — | **Unknown** |
| `0x0A` | `0x17` | `0xB3B2` | Unknown | — | **Unknown** |
| `0x0A` | `0x17` write part | `0xB3C4` | Propagated outdoor temperature | °C | **High** |
| `0x0A` | `0x17` write part | `0xB3C5` | Room setpoint | °C | **Confirmed** |
| `0x0A` | `0x17` write part | `0xB3C6` | Boost / enhanced request | observed `0` / `2` | **High** |
| `0x0F` | `0x10` | `0x03E8` | Heating curve | integer | **Confirmed** |
| `0x0F` | `0x10` | `0x03E9` | Heating minimum | °C | **Confirmed** |
| `0x0F` | `0x10` | `0x03EA` | Heating maximum | °C | **Confirmed** |
| `0x0F` | `0x10` | `0x03EB` | Curve correction +5 | temperature correction | **Confirmed** |
| `0x0F` | `0x10` | `0x03EC` | Curve correction 0 | temperature correction | **Confirmed** |
| `0x0F` | `0x10` | `0x03ED` | Curve correction -5 | temperature correction | **Confirmed** |
| `0x0F` | `0x10` | `0x03EE` | Heating stop | °C | **Confirmed** |
| `0x0F` | `0x10` | `0x03EF` | Reduced temperature | °C | **Confirmed** |
| `0x0F` | `0x10` | `0x03F0` | Room factor | integer | **Confirmed** |
| `0x0F` | `0x10` | `0x03F1` | Unknown | often `40` | **Unknown** |
| `0x0F` | `0x10` | `0x03F2` | Unknown | often `30` | **Unknown** |
| `0x0F` | `0x10` | `0x03F3` | Unknown | often `1` | **Unknown** |
| `0x0F` | `0x10` | `0x03F4` | Room setpoint mirror | °C | **High** |
| `0x0F` | `0x10` | `0x03F5` | Unknown | often `2` | **Unknown** |
| `0x1E` | `0x04` | `0x0000` | Condenser inlet temperature | ×0.1 °C | **Confirmed** |
| `0x1E` | `0x04` | `0x0001` | Condenser outlet temperature | ×0.1 °C | **Confirmed** |
| `0x1E` | `0x04` | `0x0002` | Refrigerant temperature 1 | ×0.1 °C | **High** |
| `0x1E` | `0x04` | `0x0003` | Discharge gas temperature | ×0.1 °C | **High** |
| `0x1E` | `0x04` | `0x0004` | Refrigerant temperature 2 | ×0.1 °C | **High** |
| `0x1E` | `0x04` | `0x0005` | Average outdoor temperature | ×0.1 °C | **High** |
| `0x1E` | `0x04` | `0x0006` | Compressor temperature | ×0.1 °C | **High** |
| `0x1E` | `0x04` | `0x0007` | Unknown | — | **Unknown** |
| `0x1E` | `0x04` | `0x0008` | High pressure | ×0.1 bar | **Confirmed** |
| `0x1E` | `0x04` | `0x0009` | Unknown | — | **Unknown** |
| `0x1E` | `0x04` | `0x000A` | Requested / target temperature | ×0.1 °C | **Confirmed** |
| `0x1E` | `0x04` | `0x000B` | Compressor frequency | Hz | **Confirmed** |
| `0x1E` | `0x04` | `0x000C` | Unknown | — | **Unknown** |
| `0x1E` | `0x04` | `0x000D` | Compressor current | ×0.1 A | **Confirmed** |
| `0x1E` | `0x04` | `0x000E` | Outdoor fan speed | rpm | **Confirmed** |
| `0x1E` | `0x04` | `0x000F` | Unknown | — | **Unknown** |
| `0x1E` | `0x04` | `0x0010` | Expansion valve steps | steps | **Confirmed** |
| `0x1E` | `0x04` | `0x0011` | Unknown | — | **Unknown** |
| `0x1E` | `0x04` | `0x0012` | Unknown | — | **Unknown** |
| `0x1E` | `0x04` | `0x0013` | Unknown | — | **Unknown** |
| `0x1E` | `0x04` | `0x0014` | Status bitfield | observed `16`, `24`, `25`, `28`, `29` | **Tentative** |
| `0x1E` | `0x04` | `0x0015` | Status bitfield | observed e.g. `65`, `577` | **Tentative** |

### Derived values

| Home Assistant value | Source | Certainty |
|---|---|---|
| Compressor running | `0x1E:0x000B > 0 Hz` | **Confirmed** |
| Condenser delta-T | `0x0001 - 0x0000` | **Confirmed** |
| DHW delta-T | `0xA7FB - 0xA7FC` | **Confirmed** |
| SG Ready mode | combination of `0xA7FD` + `0xA803` | **Confirmed** |


## SG Ready mapping

The physical SG inputs were tested and the following state mapping was observed:

| SG1 | SG2 | A7FD | A803 | Home Assistant state |
|---:|---:|---:|---:|---|
| 0 | 0 | -1000 | 224 | Normal |
| 1 | 0 | -1000 | 232 | Blocked |
| 0 | 1 | 1000 | 224 | Enhanced |
| 1 | 1 | 1000 | 232 | Peak |

Temporary values can appear while the SG state is changing; the YAML keeps the last valid state during those transitions.

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
