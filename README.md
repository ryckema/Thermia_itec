# Thermia iTec XTR M → Home Assistant via ESPHome

A **local, read-only ESPHome integration** for a Thermia iTec XTR M heat pump using its internal RS485 communication bus.

This project is based on reverse engineering of a real Thermia iTec XTR M with the older/non-Genesis controller. The bus traffic has been identified as **Modbus RTU** and a number of useful values are decoded into native Home Assistant entities.

> **Current status:** read-only monitoring is working reliably on the tested system. Writing/control is intentionally disabled. Direct writes to several known mirror/broadcast registers did not change the controller's master state, and the Online/DCM command protocol is not yet understood well enough for safe control.

## What you need

- Thermia iTec (XTR)  with the compatible older/non-Genesis controller
- [Waveshare ESP32-S3-RS485-CAN-U](https://www.waveshare.com/esp32-s3-rs485-can.htm) or equivalent ESP32 + isolated RS485 interface
- USB-C power supply for the ESP32
- RJ45 breakout / cable for connecting to the Thermia communication port
- ESPHome + Home Assistant

The provided YAML variants are written for the **Waveshare ESP32-S3-RS485-CAN-U**.

## Thermia RJ45 bus

On the tested controller the two RJ45 connectors are similar to the 122 / 123 connectors found on older Thermia boards.

Pin groups reported for this Thermia/iTec bus family (only pins 1=A and 3=B are required and were used in the tested read-only setup):

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
- RX is **not inverted** in the current Waveshare ESPHome configuration

Relevant ESPHome configuration:

```yaml
uart:
  id: thermia_uart

  rx_pin:
    number: GPIO18
    inverted: false

  baud_rate: 9600
  data_bits: 8
  parity: EVEN
  stop_bits: 1
```

TX is intentionally not configured in either shared YAML, so the ESP32 remains passive/read-only.

## Which YAML should I use?

Two read-only variants are maintained:

### Public / optimized

Use this for normal Home Assistant operation and for sharing with other users.

- Passive **RX-only** operation
- Quiet production logging
- Only the useful decoded entities and a small set of diagnostics
- Generic reverse-engineering register database removed
- Raw register entities removed
- Lower log/API/heap overhead
- Device name can be changed through `substitutions`

Current file:

`thermia_itec_xtr_m_waveshare_public_v27.yaml`

### Research / register mapping

Use this when capturing the bus to identify or verify additional registers.

- Still passive **RX-only** — no Thermia writes are performed
- Raw Modbus frame logging
- Generic change-only register mapper
- Raw diagnostic register entities retained
- More verbose and uses more resources than the public build
- Intended for controlled captures and reverse engineering rather than minimum-overhead 24/7 use

Current file:

`thermia_itec_xtr_m_waveshare_research_v27.yaml`

Both variants use the same confirmed bus parameters and decoded register logic. New discoveries should first be verified in the research build and only then promoted to the public build.

### v27 changes

v27 keeps both shared YAMLs strictly **passive RX-only**. The functional production decoder remains conservative; this release mainly updates the protocol model and removes interpretations disproved by later controlled experiments.

- `0x06` is now described as the **Online/DCM-facing accessory transport slot** rather than as a proven physical DCM identity.
- `0x0F` is described as **native controller settings/state**.
- A valid `0x06` response is explicitly only **transport presence**; it causes the fast ~0.7 / ~1.4 s polling cadence but does not establish a semantic Online/DCM session.
- The `AFCA 0000 -> 03E8 -> 0000` / `0x0F:0861 0000 -> 0010 -> 0000` cycle is documented as a **proven transport REQ/ACK transaction**, not semantic write success.
- EXP135 showed that changing `SERVICE -> WARMWATER -> START` by 1 °C did **not** change the recurrent `03E8..03F5` block.
- EXP136 showed that changing DHW mode `COMFORT <-> ECO` did **not** change any word in the recurrent `03E8..03F5` block.
- Therefore `03F1`, `03F2`, `03F3`, and `03F5` remain **unknown** on the tested XTR M; the old `03F1 = Hot Water Start` interpretation is not retained.
- v26 remains in the repository as a historical/reference snapshot.

### v26 changes

Compared with v25, v26 does **not** add Thermia TX or write controls. It is a register-interpretation/documentation update:

- `0x0A:B3B1` is documented as the pending room-sensor setpoint request path.
- `0x0A:B3C5` is explicitly treated as the controller-propagated/confirmed room setpoint, not the master write input.
- `0x0A:B3C6` is returned to a neutral unknown control/status label; the old boost/enhanced interpretation was too strong.
- `0x02:A80F` is refined as a controller sequence/control value and explicitly not a percentage.
- `0x1E` FC16 `0x0006` is documented as a repeating `0/1/2` periodic state/counter with roughly two-hour steps; purpose remains unknown.
- FC16 `0x0007` versus `0x0008` is clarified using captured heating↔DHW handovers.
- The strong delayed correlation between `0x02:A80E` and `0x06:AFDC` is documented without treating either as a DCM-present flag.
- The `0x06` Online/DCM command-mailbox hypothesis is documented as **Tentative/External**, not implemented.

## Installation

1. Choose either `thermia_itec_xtr_m_waveshare_public_v27.yaml` or `thermia_itec_xtr_m_waveshare_research_v27.yaml` and copy it into your ESPHome configuration directory.
2. Copy the entries from `secrets.example.yaml` into your ESPHome `secrets.yaml`.
3. Replace the placeholder values with your Wi-Fi, API encryption key, OTA password and fallback-AP password.
4. Connect the RS485 bus as shown above.
5. Power the Waveshare board over USB-C.
6. Validate and install the YAML from ESPHome.
7. Add the ESPHome device to Home Assistant if it is not discovered automatically.

Example `secrets.yaml`:

```yaml
wifi_ssid: "MyWiFi"
wifi_password: "MyWiFiPassword"

thermia_api_encryption_key: "GENERATED_BASE64_KEY"
thermia_ota_password: "MyOTAPassword"
thermia_fallback_password: "MyFallbackAPPassword"
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

Additional controller, refrigerant/compressor and DCM values are exposed as **diagnostic entities** where useful. The **research** build additionally exposes raw-register diagnostic entities and the generic register mapper; these are intentionally removed from the **public/optimized** build.

For high-level Home Assistant status, do **not** treat outdoor-unit state `0x0014` as a compressor-running flag. Physical compressor operation is derived from compressor frequency (`0x1E FC04 0x000B > 0 Hz`).


## Register map

The map below contains the mappings that are most useful for the shared integration. A separate detailed register-map document can be used for the full reverse-engineering notes and unresolved observations.

Certainty levels:

- **Confirmed** — matched against a known value, controlled test, repeated operating behaviour or the physical Thermia display.
- **High** — behaviour and scaling strongly match the proposed meaning, but have not yet been independently verified in every operating state.
- **Tentative** — plausible and correlated, but still needs a targeted test.
- **External** — reported for a related Thermia / Danfoss implementation but not yet verified on this XTR M.
- **Unknown** — observed on the bus, but meaning not identified.

For the **public/optimized** YAML, only mappings considered sufficiently stable for normal use should be exposed by default. Tentative, External and Unknown values belong in diagnostics or the research build until verified.

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
| `0xA80C` | Controller output/context bitfield | bitfield; see mapping below | **High locally; individual output bits partly External** |
| `0xA80D` | Additional controller output bitfield | Eco 8: bit `0x10` = immersion heater stage 2 | **External** |
| `0xA80E` | Controller / accessory status bitfield | observed `0`, `8`, `32`, `40` | **High correlation / semantic Tentative** |
| `0xA80F` | Condenser / circulation pump speed candidate | observed `5`, `10`, `50`, `75–100`; Eco 8 manual test tracked 30→40→50→40→30 exactly | **External controlled test; XTR correlation strong** |
| `0xA810` | Unknown | often `10` | **Unknown** |
| `0xA811` | Unknown | often `-1` | **Unknown** |
| `0xA812` | Unknown | often `0` | **Unknown** |

Observed / cross-model `A80C` bit mapping:

| Bit | Meaning | Evidence / certainty |
|---:|---|---|
| `0x01` | DHW reversing valve / DHW request context | **High locally; External manual-test confirmation** |
| `0x02` | Bypass cooling output | **External controlled manual test** |
| `0x04` | Potential-free output | **External controlled manual test** |
| `0x08` | External auxiliary heater output | **External controlled manual test** |
| `0x20` | Unresolved manual-test/context bit | **External / Unknown** |
| `0x40` | Controller active context | **High correlation; External manual-test confirmation** |
| `0x80` | Immersion heater stage 1 | **External controlled manual test** |

This explains compound values such as `65 = 64 + 1` and `193 = 128 + 64 + 1`. Treat the individual output-bit meanings as cross-model evidence until reproduced on the XTR M.

`A80E` is a controller/accessory status path, not a heating/DHW/cooling mode and not a DCM-present flag. The apparent delay from `A80E 0x20` to `0x06:AFDC 0x20` is cadence-dependent: external frame-timed captures show AFDC following on the next 0x06 push, typically `0.0–0.2 s` in fast cadence and up to about `3.7 s` in slow cadence.

`A80F` now has a strong cross-model candidate meaning: on an Eco 8 / DHP-AQ, `SERVICE → MANUAL TEST → CONDENSER PUMP (%)` made A80F follow `30 → 40 → 50 → 40 → 30` exactly, while values below 30% fell to `5`. The XTR M values `5`, `10`, `50`, `75–100` are consistent with a condenser/circulation-pump speed signal, but local XTR manual-test confirmation is still required before calling it Confirmed.

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
| `0xB3B1` | Pending room-sensor setpoint request | integer °C while a local change is pending, otherwise `0` | **Confirmed / High** |
| `0xB3B2` | Unknown room-sensor response word | observed `0` in current captures | **Unknown** |

### FC17 write part

| Register | Meaning | Scale / values | Certainty |
|---|---|---|---|
| `0xB3C4` | Propagated outdoor temperature | °C | **Confirmed / High** |
| `0xB3C5` | Controller-propagated / confirmed room setpoint | °C | **Confirmed** |
| `0xB3C6` | Unknown room-sensor control/status word | observed `0` / `2` | **Tentative** |

Repeated logging shows the central outdoor temperature propagating from `0x02:A802` to `0x0A:B3C4` and then to `0x06:AFE0`.

Setpoint direction is important: a genuine room-sensor adjustment appears in the sensor's FC17 **response** at `B3B1`; the controller then propagates the resulting confirmed setpoint through `B3C5`, while `0x0F:03F4` follows later as a mirror. A direct write to `B3C5` did not change the controller's master setpoint.

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

`0x03F4` is a **room-setpoint mirror**, not a proven writable master input. During a main-display change, `B3C5` changed first and `03F4` followed roughly 6.5 seconds later. Direct writes to the mirror did not produce a persistent controller change.

### Additional native / Online-index findings

| Register / block | Decimal | Meaning | Certainty |
|---|---:|---|---|
| `0x041D` | `1053` | DHW START candidate from external ATEC/DHP-AQ material | **External only; still OPEN on XTR M** |
| `0x042E` | `1070` | Integral A1 | **External Online dump** |
| `0x0442` | `1090` | Activate Cooling | **Confirmed on XTR M by display A/B test** |
| `0x0553` | `1363` | Operation Mode | **External Online dump** |
| `0x0559` | `1369` | Link Integration | **External Online dump** |
| `0x04A6..0x04B2` | `1190..1202` | Native runtime FC10 block; `0x04B0=0x4020` seen in first EXP133 sample | **Observed locally / semantics Unknown** |
| `0x085F..0x0863` | `2143..2147` | Native five-word FC10 block containing transaction field `0x0861` | **Observed locally** |
| `0x0861` | `2145` | Transport ACK field: `0 → 16 → 0` follows the proven AFCA REQ cycle | **Confirmed transport semantics** |

A related ATEC/DHP-AQ map reports a DHW settings family around decimal `1053–1059` (`0x041D–0x0423`). On the XTR M, `0x041D` is currently only a candidate for `SERVICE → WARMWATER → START` and is being treated as a passive-correlation target rather than as an assumed mapping.

The low Online indices appear substantially more portable across this Thermia/Danfoss platform than the higher telemetry ranges: `0x0442 Activate Cooling` has already been independently verified on the XTR M, while some 2xxx Online indices differ between ATEC and iTec models.

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
| `0x0014` | Outdoor-unit actuator / sequence-status bitfield | bitfield; common combinations listed below | **High locally; bit meanings externally controlled/correlated** |
| `0x0015` | Outdoor-unit status / context bitfield | bitfield | **High** |
| `0x001F` | Unknown, observed during state-20 recovery sequence | observed `0 → 911` | **Unknown / correlated** |
| `0x0023` | Unknown, observed during state-20 recovery sequence | observed `0 → 4` | **Unknown / correlated** |

### `0x0014` status-bit combinations

Cross-model correlation now shows that `0x0014` behaves as a **bitfield**, not a simple enum. On an Eco 8 / DHP-AQ, seven days of 30 s samples gave the following bit meanings with 100% correlation in that dataset:

| Bit | Meaning | Certainty |
|---:|---|---|
| `0x01` | Compressor running | **External strong correlation** |
| `0x04` | Outdoor fan turning | **External strong correlation** |
| `0x08` | Water flow / circulation pump | **External strong correlation** |
| `0x10` | Base / controller-active bit | **External strong correlation; exact semantics unresolved** |

This decodes common raw values naturally:

| Raw value | Bit interpretation | XTR observation |
|---:|---|---|
| `16` | base only | Idle |
| `20` | base + fan | Autonomous/recovery sequence observed locally |
| `24` | base + circulation pump | Preparation / transition |
| `25` | base + pump + compressor | Seen in heating/DHW shutdown |
| `28` | base + pump + fan | Heating/DHW startup / ramp |
| `29` | base + pump + fan + compressor | Established heating/DHW sequence |

Cooling combinations `26`, `27`, `30`, and `31` remain useful observed XTR states, but their exact additional-bit semantics should stay provisional until locally correlated. Physical compressor operation in the shared integration should continue to use compressor frequency as the local source of truth until the `0x0014 bit 0` mapping is independently reproduced on the XTR M.

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
| `0x0006` | Periodic state/counter; purpose unknown | repeating `0/1/2`; ~2 h steps observed | **High for periodic behaviour / semantic Unknown** |
| `0x0007` | Outdoor-unit cycle / sequence request | `0/1`; can stay active across heating↔DHW handovers | **Confirmed** |
| `0x0008` | Immediate outdoor-unit run enable | `0/1`; can toggle off/on within an ongoing cycle | **Confirmed** |

Repeated cycles show `A80F 50 → 80` immediately before `0x0007` turns on. A captured heating → DHW handover is especially useful: mode changed `1 → 2` and `0x0008` temporarily changed `1 → 0`, while `0x0007` remained active. This makes `0x0007` a reliable **overall cycle/sequence request** and `0x0008` the more immediate run-enable command. `0x0015 bit 0x0200` follows `0x0008` as an acknowledgement/context flag with a short delay. Physical compressor operation should still be derived from compressor frequency.

---

## Slave `0x06` — accessory / expansion slot (Online/DCM relationship unresolved)

Observed polling:

- FC17 read around `0xAFC8`, count 12
- FC17 write around `0xAFDC`, count 5

| Register | Meaning | Scale / values | Certainty |
|---|---|---|---|
| `0xAFD1` | Accessory EXP version metadata | displayed as value / 10 (e.g. `16 → 1.6`) | **Confirmed** |
| `0xAFDC` | Accessory/controller context word | observed `0`, `16`, `32` and compound states | **High correlation / semantic Tentative** |
| `0xAFDD` | Accessory housekeeping / preparation word | observed `0`, `16` | **Tentative** |
| `0xAFE0` | Propagated outdoor temperature | °C | **High** |

`AFDC` should not be interpreted as a heating/DHW/cooling mode or as proof that a DCM is present. In long captures `AFDC 0x20` repeatedly follows `A80E 0x20` after a short delay, while startup/housekeeping values such as `0x10` can occur without a DCM connected. The exact semantics remain unresolved.

The FC17 direction is now proven at transport level: the controller writes `AFDC..AFE0` **to** the accessory slot while reading `AFC8..AFD3` **from** the accessory response. A valid responder establishes the fast accessory cadence, and `AFCA=0x03E8` drives the `0x0F:0861` ACK `0→16`; clearing AFCA returns it to `0`.

However, EXP129–132 show that `0x06` should **not** currently be labelled as a proven DCM/Online device identity. A valid responder makes the controller expose an `EXP / expansion board` version entry, and `AFD1` is rendered as that version number in tenths. This proves an accessory/expansion presence + metadata path; whether the genuine Online/Connect/DCM hardware owns this slot directly or uses it as part of a larger session remains unresolved.

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
- that RX remains configured with `inverted: false`
- that the ESP is connected to the correct Thermia communication port

If necessary, try swapping A and B. RS485 naming conventions are unfortunately not consistent between manufacturers.

### Home Assistant shows lots of unavailable diagnostic entities

That is expected for some raw registers. The controller uses sentinel values such as `-1000` for unavailable sensors/fields, and not every register is populated on every installation.

### Can this control the heat pump?

Not yet in this shared version.

Some frames contain fields that look writable, but direct writes to the known room-setpoint and settings mirrors have **not** changed the controller's master state. The room sensor uses an FC17 response field (`B3B1`) to report a pending local setpoint change back to the controller, so simply writing `B3C5` or `03F4` is the wrong direction.

The controller additionally polls an Online/DCM-facing accessory slot (`0x06`) with FC23/0x17. The controller reads `AFC8..AFD3` (12 words) from the accessory while writing `AFDC..AFE0` (5 words) toward it. A valid response proves accessory presence and changes the poll cadence, but does not establish a semantic session. The `AFCA 0 -> 03E8 -> 0` / `0x0F:0861 0 -> 16 -> 0` exchange is a proven transport transaction. The still-missing layer is the genuine DCM/Connect identity, binding, integration/initial-sync and semantic serializer. TX is therefore intentionally disabled in both shared v27 versions.

## Safety / compatibility

This is an unofficial reverse-engineered integration and is **not affiliated with or supported by Thermia**.

The register map is based on one Thermia iTec XTR M installation. Other Thermia iTec revisions or related models may use different boards, bus wiring, slave addresses or register layouts.

Start with read-only operation and verify the RJ45 pinout on your own hardware before connecting anything.

## Development status

Read-only monitoring is stable on the tested installation and the register map is still being expanded. Several controller and outdoor-unit sequence states have now been decoded, including normal heating/cooling startup and shutdown paths, SG Ready state, run-enable signalling and a special autonomous recovery sequence.

Write support is intentionally not included. Presence on `0x06` and the AFCA/0861 transport transaction are now understood, but neither is sufficient for semantic control. Later experiments also showed that manual DHW START and COMFORT/ECO changes do not alter the recurrent `03E8..03F5` block, so earlier DHW labels in that block are not retained. The central unresolved problem is the DCM/Connect identity/binding/IntegrationMode/initial-sync serializer inside the 12-word accessory interface. A genuine Thermia Online/Connect cold-boot capture with one safe official setting change is the highest-value next artifact. The shared integrations remain passive/read-only.
