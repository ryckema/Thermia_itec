# Thermia iTec Eco — Room Sensor Emulation, Setpoint Control & DHW Top-Up (Write Beta v01)

This folder contains the active room sensor emulation and control profiles for the **Thermia iTec Eco** heat pump (Danfoss DHP-AQ controller family):

- 📄 [`thermia_itec_eco_waveshare_room_sensor_v01.yaml`](./thermia_itec_eco_waveshare_room_sensor_v01.yaml) — **Standard profile:** `0x0A` Room Sensor emulation, native Home Assistant `Room Thermostat` (`climate`), bidirectional setpoint control, hot-water top-up trigger, and flash-persisted `0x03E8` / `0x042E` settings cache.
- 📄 [`thermia_itec_eco_waveshare_room_sensor_0f_ack_v01.yaml`](./thermia_itec_eco_waveshare_room_sensor_0f_ack_v01.yaml) — **Extended `0x0F` ACK profile:** Identical to `v01`, plus optional **`0x0F` Online/DCM ACK emulation** (`FC10` write ACKs + `FC03 0x0708` idle replies with automatic peer collision guard) so a heat pump without a physical Thermia Online module immediately publishes all `0x0F` settings blocks (`0x03E8..0x03F5` heating curve and `0x042E..0x0434` hot-water settings) without retry timeouts.

---

## 1. Background & Protocol Architecture

Findings and measurements from Piotr Romanowski's [thermia-bus-sniffer](https://github.com/piotr-romanowski/thermia-bus-sniffer) project demonstrate:
- The **iTec Eco** display panel routinely polls accessory slot **`0x0A`** (Danfoss/Thermia 086U9563 Modbus room sensor) every ~4.3 seconds using FC23 (read 3 @46000, write 3 @46020):
  ```text
  display -> 0x0A: 0A 17 B3 B0 00 03 B3 C4 00 03 06 00 XX 00 YY 00 ZZ CRC
  ```
  Where the controller writes 3 registers:
  - `@46020` (`0xB3C4`): Displayed outdoor temperature (°C).
  - `@46021` (`0xB3C5`): Controller-propagated / confirmed room setpoint (`YY`, e.g. `0x14` = 20 °C).
  - `@46022` (`0xB3C6`): Hot-water top-up status (`ZZ`: `0` = idle, `2` = top-up active).

- The emulated sensor responds with an 11-byte FC23 (FC17) response carrying **3 control registers**:
  ```text
  0A 17 06 <temp*10> <setpoint_req> <topup_req> <CRC16>
  ```
  1. **Word 0 (`@46000` / `0xB3B0`): Indoor Temperature (°C × 10)**
     - e.g. `215` = 21.5 °C. The heat pump auto-detects the sensor and adopts this temperature for heating curve room compensation.
  2. **Word 1 (`@46001` / `0xB3B1`): Room Setpoint Request (°C × 1)**
     - Acting like the dial on a physical sensor: sending a value (e.g. `21`) requests the controller to adopt 21 °C as its new setpoint.
     - When idle or no change is requested, it transmits `0`.
     - Once the heat pump adopts the value, it confirms the change by echoing it back in `@46021`.
  3. **Word 2 (`@46002` / `0xB3B2`): Hot-Water Top-Up Trigger (One-shot command)**
     - Writing `1` into this register triggers the heat pump to immediately start domestic hot-water top-up (using the immersion heater, bypassing compressor limits).
     - The trigger is one-shot: ESPHome transmits `1` for a single cycle and returns to `0`.
     - When active, the controller updates `@46022` to `2`.

- **Why this path works when Thermia Online does not:**
  Unlike slot `0x0F` (Thermia Online), which on iTec Eco enforces a random 128-bit cryptographic challenge-response handshake that rejects replayed responses, the room sensor slot **`0x0A` requires no pairing or encryption** and operates entirely locally on a simple poll-response loop.

---

## 2. Hardware & Wiring

**Waveshare ESP32-S3-RS485-CAN / ESP32-S3-RS485-CAN-U:**
- **RX:** GPIO18
- **TX:** GPIO17
- **DE/RE direction:** GPIO21 (HIGH = transmit, LOW = receive)
- **Bus connection to Thermia indoor unit RJ45 port (ports 122/123):**
  - Pin 1 or 2 (RS485 A) -> Waveshare A+
  - Pin 3 or 4 (RS485 B) -> Waveshare B-
  - Pin 5 or 6 (GND) -> Waveshare GND
  - *(Warning: Do not connect pins 7/8; they supply +12 V).*

---

## 3. Home Assistant Entities

When flashed to an ESP32, this configuration exposes the following control and diagnostic entities to Home Assistant:

| Entity | Type | Description | Default |
|---|---|---|---|
| `climate.thermia_room_thermostat` | Climate (Thermostat) | Native Home Assistant thermostat card (`10–30 °C` target step `1 °C`, `0.1 °C` measured room temperature, and real `Heating` / `Cooling` / `Idle` action from the heat pump). | `Heat` / `20 °C` |
| `switch.thermia_room_sensor_emulation` | Switch | Master toggle for room sensor emulation (must be ON to answer polls). | `OFF` (fail-closed) |
| `switch.thermia_0f_ack_emulation` | Switch | *(Only in `0f_ack_v01`)* Master toggle for `0x0F` Online/DCM ACK emulation (auto-disables if an external `0x0F` module is detected). | `ON` |
| `number.thermia_room_temp_input` | Number | Input indoor temperature fed from Home Assistant (5.0–35.0 °C, step 0.1 °C). | `21.0 °C` |
| `number.thermia_target_room_setpoint` | Number | Target room setpoint (10.0–30.0 °C, step 1.0 °C). Synchronized bidirectionally with both the heat pump panel and `climate.thermia_room_thermostat`. | `20.0 °C` |
| `button.thermia_trigger_dhw_topup` | Button | One-shot trigger to start hot-water top-up (pikalämmitys). | — |
| `binary_sensor.thermia_dhw_topup_active` | Binary Sensor | Status of hot-water top-up (`true` when active, mirrors `@46022 == 2`). | `false` |
| `number.thermia_room_temp_timeout_min` | Number | Safety watchdog timeout in minutes (0–120 min, 0 = disabled). | `30 min` |
| `sensor.thermia_room_sensor_status` | Text Sensor | Emulation status (`DISABLED`, `ACTIVE`, `TIMEOUT: Stale HA data`, `BLOCKED: External sensor on bus`). | `DISABLED` |
| `sensor.thermia_room_sensor_responses_sent` | Sensor | Total count of 0x0A responses transmitted. | `0` |
| `sensor.thermia_room_sensor_last_sent_temp` | Sensor | Last temperature value transmitted to the bus. | `—` |

---

## 4. Usage & Home Assistant Automations

### A. Sync Room Temperature from HA Sensor (Zigbee, BLE, Ruuvi, etc.)
Forward real-time readings from an existing indoor sensor to the heat pump:

```yaml
alias: "Thermia - Sync Room Temperature"
trigger:
  - platform: state
    entity_id: sensor.living_room_temperature
condition:
  - condition: template
    value_template: "{{ states('sensor.living_room_temperature') not in ['unavailable', 'unknown'] }}"
action:
  - service: number.set_value
    target:
      entity_id: number.thermia_room_temp_input
    data:
      value: "{{ states('sensor.living_room_temperature') | float }}"
```

### B. Adjust Room Setpoint from Home Assistant
Change the heat pump's room temperature setpoint dynamically (e.g., night setback or away mode):

```yaml
alias: "Thermia - Night Temperature Setback"
trigger:
  - platform: time
    at: "23:00:00"
action:
  - service: number.set_value
    target:
      entity_id: number.thermia_target_room_setpoint
    data:
      value: 19
```
*Note: If someone manually turns the dial on the heat pump's physical display, `number.thermia_target_room_setpoint` in Home Assistant automatically updates to match.*

### C. Cheap Electricity Hot-Water Top-Up (Nordpool / Spot Price)
Heat up domestic hot water when electricity is cheap or negative:

```yaml
alias: "Thermia - Spot Price Cheap DHW Top-Up"
trigger:
  - platform: numeric_state
    entity_id: sensor.nordpool_kwh_fi_eur
    below: 0.02
condition:
  - condition: state
    entity_id: binary_sensor.thermia_dhw_topup_active
    state: "off"
action:
  - service: button.press
    target:
      entity_id: button.thermia_trigger_dhw_topup
```

### D. Direct ESPHome Native API Service Calls
You can also call the exposed ESPHome services directly without using entity helpers:

```yaml
# Set indoor temperature
service: esphome.thermia_itec_eco_set_room_temperature
data:
  temperature: 21.8

# Set room setpoint
service: esphome.thermia_itec_eco_set_target_room_setpoint
data:
  setpoint: 21

# Trigger hot water top-up
service: esphome.thermia_itec_eco_trigger_hot_water_topup
```

---

## 5. Safety & Safeguards (Fail-Closed)

1. **Passive by Default:**
   - The device always boots with `switch.thermia_room_sensor_emulation` **`OFF`**.
   - DE (`GPIO21`) is held `LOW` permanently when disabled, keeping the ESP strictly in receive mode.
   - When enabled, DE is asserted `HIGH` only during the ~12 ms frame transmission every ~4.3 seconds.

2. **Safety Watchdog Timeout:**
   - If Home Assistant or the sensor goes offline (e.g., dead battery or HA restart), the watchdog timer halts responses after the configured duration (default: 30 minutes).
   - The heat pump gracefully reverts to its outdoor weather curve without room compensation, preventing the system from running indefinitely on stale temperature data.

3. **Physical Sensor Collision Guard:**
   - If a genuine physical Danfoss/Thermia room sensor (086U9563) is detected answering on `0x0A`, the ESP immediately disables emulation, drops DE to `LOW`, and reports `BLOCKED: External sensor on bus` to prevent bus collisions.

4. **Setpoint Request Handshaking:**
   - Setpoint changes are sent as requests and automatically cleared back to `0` as soon as the heat pump acknowledges the change in `@46021`. If the heat pump does not acknowledge within 5 cycles, the request times out and clears to avoid flooding the bus.

---

## 6. Credits & Attribution

Credit where credit is due:
- **Piotr Romanowski ([piotr-romanowski/thermia-bus-sniffer](https://github.com/piotr-romanowski/thermia-bus-sniffer)):**
  Pioneered the transmit-side reverse engineering and verification of the `0x0A` Modbus room sensor emulation on iTec Eco hardware: measured turnaround timing (~145 ms timeout), verified indoor temperature adoption (`@46000`), discovered the room setpoint request mechanism (`@46001`), and experimentally confirmed the hot-water top-up trigger (`@46002`) and status word (`@46022`).
- **ryckema ([ryckema/Thermia_itec](https://github.com/ryckema/Thermia_itec)):**
  Original register analysis, semantic definitions (`B3B0` / `B3B1` / `B3C5`), DHP-AQ controller models, and the comprehensive baseline ESPHome passive decoder upon which this build is built.
