# Thermia iTec Eco — Room Sensor Emulation (Write Beta v01)

This folder contains the active room sensor emulation profile for the **Thermia iTec Eco** heat pump (Danfoss DHP-AQ controller family):

📄 [`thermia_itec_eco_waveshare_room_sensor_v01.yaml`](./thermia_itec_eco_waveshare_room_sensor_v01.yaml)

---

## 1. Background & Evidence

Findings and measurements from Piotr Romanowski's [thermia-bus-sniffer](https://github.com/piotr-romanowski/thermia-bus-sniffer) project demonstrate:
- The **iTec Eco** display panel routinely polls accessory slot **`0x0A`** (Danfoss/Thermia 086U9563 Modbus room sensor) every ~4.3 seconds using FC23 (read 3 @46000, write 3 @46020):
  ```text
  display -> 0x0A: 0A 17 B3 B0 00 03 B3 C4 00 03 06 00 XX 00 10 00 00 CRC
  ```
- When answered with a standard 11-byte FC23 (FC17) response frame:
  ```text
  0A 17 06 <room temp x10> 00 00 00 00 <CRC16>
  ```
  **the display auto-detects the room sensor** and uses the supplied indoor temperature for heating curve room compensation.
- Unlike slot `0x0F` (Thermia Online), which on iTec Eco enforces a random 128-bit cryptographic challenge-response handshake that rejects replayed responses, the room sensor slot **`0x0A` requires no pairing or encryption** and operates as a direct poll-response cycle.

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
| `switch.thermia_room_sensor_emulation` | Switch | Master switch for room sensor emulation. | `OFF` (fail-closed) |
| `number.thermia_room_temp_input` | Number | Input room temperature (5.0–35.0 °C, step 0.1 °C). | `21.0 °C` |
| `number.thermia_room_temp_timeout_min` | Number | Safety watchdog timeout in minutes (0–120 min, 0 = disabled). | `30 min` |
| `sensor.thermia_room_sensor_status` | Text Sensor | Emulation status (`DISABLED`, `ACTIVE`, `TIMEOUT: Stale HA data`, `BLOCKED: External sensor on bus`). | `DISABLED` |
| `sensor.thermia_room_sensor_responses_sent` | Sensor | Total count of 0x0A responses transmitted. | `0` |
| `sensor.thermia_room_sensor_last_sent_temp` | Sensor | Last temperature value transmitted to the bus. | `—` |

---

## 4. Usage & Home Assistant Automations

### Method A: Automated Temperature Sync from Any HA Sensor
You can create a Home Assistant automation to forward readings from an existing indoor sensor (e.g., Zigbee, BLE, Ruuvi, Z-Wave) to the input number entity:

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

### Method B: Direct ESPHome Native API Service Call
Alternatively, you can call the exposed ESPHome service directly:

```yaml
action:
  - service: esphome.thermia_itec_eco_set_room_temperature
    data:
      temperature: 21.8
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

---

## 6. Credits & Attribution

Credit where credit is due:
- **Piotr Romanowski ([piotr-romanowski/thermia-bus-sniffer](https://github.com/piotr-romanowski/thermia-bus-sniffer)):**
  Pioneered the transmit-side reverse engineering and verification of the `0x0A` Modbus room sensor emulation on iTec Eco hardware, measured the controller turnaround times (~145 ms timeout), documented the 11-byte FC23 reply structure, and confirmed that the display auto-detects the sensor and adopts the temperature for room compensation.
- **ryckema ([ryckema/Thermia_itec](https://github.com/ryckema/Thermia_itec)):**
  Original register analysis, semantic definitions (`B3B0` / `B3B1` / `B3C5`), DHP-AQ controller models, and the comprehensive baseline ESPHome passive decoder upon which this build is built.

