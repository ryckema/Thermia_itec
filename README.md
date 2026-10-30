# Thermia iTec XTR — ESPHome & Home Assistant

**Local monitoring and control of the Thermia iTec XTR heat pump using ESP32, ESPHome and Home Assistant.**

This project provides a local, cloud-independent integration for Thermia iTec XTR heat pumps by communicating directly with the heat pump's internal RS485 bus.

The integration is developed and tested on a **Thermia iTec XTR M with Total Compact indoor unit**, using an ESP32-S3 with an RS485 interface.
If you are looking for a ATEC version it can be found here: https://github.com/fclauson/Thermia-ATEC-ESP-emulator-of-DCOM

## Roadmap

**Development status (30 October 2026):** **W2R46** remains the last XTR **FULLY LOCALLY VERIFIED** for normal OTA startup, native M6=5, CURRENT 4/4 and automatic calendar 12/12. W2R45 and W2R44 were also locally verified for routine read/cache operation. **W2R47** is now XTR **FLASHED / LIVE / LOCALLY VERIFIED — COMPLETE / POSITIVE for ordinary read/runtime**: retained/manual-context M6=5, genuine CURRENT4/4 and automatic 12/12 controller-owned calendar receipt at 11:38:10 on 30 October. CRC_DIFF=0 across 36,499 checks, RX drops=0, parser resyncs=0, no setting writes. W2R46 remains the separate proven OTA-startup rollback; W2R47 startup/recovery and its shared legacy failure/abort guards were NOT tested. **W2R48** is now XTR **FLASHED / LIVE / LOCALLY VERIFIED — COMPLETE / POSITIVE for ordinary native read/runtime**: owner-indexed selector/desired storage migrated (714→704 globals), full automatic calendar 12/12 receipt 12:36:59 and CURRENT4/4 confirmation 12:37:34 on 30 October. CRC_DIFF0 over 21,613 checks, RX drops0 and parser resyncs0, no HA setting writes; original per-page semantic selector/commit branches remain. W2R48 initial cold start, automatic rejoin, timeout/abort negative paths and semantic setting writes were not tested. **W2R49** is XTR **FLASHED / LIVE / LOCALLY VERIFIED — COMPLETE / POSITIVE for ordinary native read/runtime**: owner-indexed six original native `0708` CURRENT/desired-selector frames and common qualification in one existing S92 RX/TX owner preserved full M6=5 retained session, CURRENT4/4 controller FC16 ACK at 13:25:40 and TWO automatic native calendar12/12 controller-owned receipts at 13:25:31 and 13:29:02 on 30 October (same session, second after ~200-second freshness). V5 CRC_DIFF0 across 11,940 checks, RX drops0/resync0, pending/dirty0; no HA setting TX. Original per-owner selector write, retry/commit/rollback semantics, cold start and automatic rejoin not tested and not declared verified. **W2R50** is a PRIVATE complete **SOURCE / OFFLINE TESTED — PREPARED / NOT RUN** firmware from XTR live-verified W2R49. A single native FC16 transaction core within sole existing S92 RX/TX owner now handles saved CURRENT snapshots, strict selected-word/full-page republish comparisons and original NOOP/CACHED/CONFIRMED/ABORT lifecycle transitions for 042E/15, 0442/13 and 0546/20, while preserving their distinct range/geometry/cooling dynamic-min/HA rollback and 0546 NOOP timing. Existing S92 guards, native session, FC03/FC16/0708, V5, HA IDs and setting-write HOLD are unchanged; 704 globals remain. NOT ESPHome target compiled, flashed or XTR live confirmed. **W2R41** remains the last independently confirmed physical calendar setting update. All calendar-setting trials and regular HA parameter setting writes remain **ON HOLD**.

1. **Consolidate native calendar reads** into one authoritative F1 data store, retaining controller-origin CRC validation, per-page freshness, and a separate owned-session receipt generation. **Implemented and first XTR OTA read-only live verified in private W2R43**; ongoing automatic freshness and independent controller-origin receipt checks remain in place.
2. **Retain one OEMW setting transaction and one S92 UART/RX/DE owner.** Source W2R43 shares one page snapshot across legacy confirmation paths without adding bus writers or changing retry/safety guards.
3. **Consolidate remaining EXP378/379/380 handlers under the existing native/OEMW/S92 owner.** W2R44/W2R45/W2R46 progressively consolidated CURRENT, desired/confirmed and lifecycle storage and were locally observed for normal read operation. W2R47 (FLASHED / LIVE / LOCALLY VERIFIED for normal read/runtime) consolidates the three owner-specific queue-expiry, active integrity/timeout watchdog and runtime-qualification decisions while preserving the original page-specific UI rollback/guards and one physical S92 owner. CURRENT4/4 and the automatic owned calendar12/12 receipt are verified. **W2R48 LIVE / LOCALLY VERIFIED** preserves genuine M6=5 and native calendar 12/12 and CURRENT 4/4 while migrating selector/desired target-word, target-value, original-value and two transaction timestamps into owner-indexed arrays; page-specific selector/commit branches and original S92 owner remain. **W2R49 LIVE / LOCALLY VERIFIED** unifies six original native `0708` CURRENT/desired selector response frames and common qualification in existing S92 owner with two completed native calendar read cycles, CURRENT4/4, CRC0, no RX drop or setting write. Individual EXP378/379/380 selector/semantic commit/requeue/rollback branches still have differences and remain source dependencies. **W2R50 SOURCE / OFFLINE TESTED — PREPARED / NOT RUN** consolidates the duplicated FC16 snapshot/strict semantic comparison/CACHED-NOOP-CONFIRMED-DISABLED transition logic in the same native owner, preserving owner-specific validation/rollback and no setting-write TX grant. **Next:** user manually builds/flashes W2R50 and supplies one ordinary natural read/runtime observation; no additional S62/S88/S92 retests, forced failure or setting-write experiments. Page-specific EXP selector/desired branches still have dependencies and are **not yet fully removed**; do not introduce a parallel TX path.
4. **Calendar setting trials ON HOLD at user request.** Both old and new calendar pilot setting TX paths are held in W2R43. Normal native FC16 sync/ACKs and FC03 read/refresh are not setting writes. New/other calendar fields and create/delete require separate XTR validation and explicit user authorization before any new physical setting TX.
5. **General Home Assistant parameter writes remain ON HOLD** pending user authorization and real controller semantic validation.

Development firmware and private OEM-derived protocol materials are not published in this public repository. The canonical detailed status and evidence remain under `Research/`; this public roadmap describes priority and availability only.

## Features

The integration is organized into four firmware versions, each offering a different level of access to the heat pump.

### Firmware versions

| Version | Monitoring | Control | Access level |
|---|---|---|---|
| **Passive** | Yes | No | Read-only, passive bus monitoring |
| **DCM Read Only** | Yes | No | Read-only, using native DCM communication |
| **Write User (soon)** | Yes | Yes | User-accessible settings |
| **Write Service (soon)** | Yes | Yes | User and service-menu settings |

### 1. Passive

**Passive monitoring without transmitting any data to the heat pump.**

This version listens to existing RS485 communication and extracts available sensor readings and controller information.

- No RS485 transmission
- Temperature and operational monitoring
- Heating settings and status where available
- Home Assistant sensor integration
- Suitable for basic monitoring

### 2. DCM Read Only

**Read-only integration using the native Thermia DCM communication protocol.**

This version is intended to provide more complete monitoring by supporting native communication and synchronization with the controller.

- All supported passive monitoring features
- Native DCM communication
- Controller synchronization
- Access to additional parameters and status information where supported
- No parameter changes

### 3. Write User 

**Beining tested at the moment and will be realeased soon**

**Monitoring and control of settings available through the heat pump's normal user interface.**

This version is intended to allow Home Assistant to change user-accessible settings documented in the Thermia operating interface.

Examples include:

- Room temperature setpoint
- Heating curve
- Minimum and maximum heating temperatures
- Heating stop temperature
- Heating curve adjustments
- Hot water settings and operating modes
- Heat pump operating mode
- Other user-accessible settings supported by the controller

These controls remain subject to protocol validation and controller support.

### 4. Write Service

**Beining tested at the moment and will be realeased soon**

**Integration of user-accessible settings and parameters available through the Thermia SERVICE menu.**

This version is intended to expose supported service-level settings in addition to the normal user controls.

Examples include:

- All supported Write User functions
- Heating system configuration
- Auxiliary heating parameters
- Hot water service settings
- Cooling configuration
- Circulation pump and Optimum settings
- Shunt group configuration
- Other available SERVICE menu parameters

Service-level access does not imply bypassing the controller's built-in safety functions. Functions requiring manual commissioning or special operating conditions retain those requirements.

**Availability:** Passive and DCM Read Only configurations are currently published. Write User and Write Service are planned versions; controller parameter writes are not yet released as validated functionality.

### Monitoring

Supported telemetry in the underlying development includes:

- Outdoor and indoor temperatures
- Room temperature setpoint
- Heating supply and return temperatures
- Domestic hot water temperature
- Heating curve and related settings
- Compressor frequency and electrical current
- Fan speed
- Condenser temperatures
- Compressor discharge temperature
- High-pressure readings
- Expansion valve information
- Operating and controller status
- Communication and bus-health diagnostics

Some values depend on the heat pump configuration, available bus messages and firmware variant.

### Local integration

- Direct RS485 communication
- ESPHome-based firmware
- Native Home Assistant API integration
- No Thermia cloud account required
- Modbus RTU-like frame decoding with CRC validation
- Passive monitoring option without bus transmission
- Local caching of selected controller settings


## Hardware requirements

You only need a few inexpensive components to get started.

### What you'll need

| Component | Description |
|---|---|
| ESP32 board | [Waveshare ESP32-S3-RS485-CAN](https://www.waveshare.com/esp32-s3-rs485-can.htm) |
| RJ45 breakout | RJ45 male to 8-pin screw-terminal adapter |
| Wires | Two short wires for RS485 A and B |
| Power supply | USB cable and compatible USB charger |
| Multimeter | Recommended for verifying the electrical connections |

The **Waveshare ESP32-S3-RS485-CAN** is the board used for this project. It combines an ESP32-S3 microcontroller, Wi-Fi connectivity and an integrated RS485 interface.

No separate RS485-to-USB converter or additional microcontroller is required.

You can use a stripped Ethernet/UTP cable instead of an RJ45 breakout adapter, but I recommend the breakout adapter. It makes the wiring cleaner and easier to verify or change.

### Wiring

The following connections are used for the Thermia iTec XTR M:

| Thermia RJ45 pin | Signal | Waveshare connection |
|---|---|---|
| Pin 1 | RS485 A (+) | A |
| Pin 3 | RS485 B (−) | B |

Only these two communication wires are required for this setup.

The ESP32 is powered separately through USB.

**Important:** The RJ45 connector also carries power. Do not connect the heat pump's power supply pins directly to the Waveshare RS485 terminals.

I strongly recommend using a multimeter to verify the electrical connections before connecting the Waveshare.

## Installation guide

### Step 1 — Prepare your hardware

You will need:

- Waveshare ESP32-S3-RS485-CAN
- RJ45 male to 8-pin breakout adapter
- Two short wires
- USB cable and USB power supply
- Multimeter (recommended)

For initial setup, leave the Waveshare disconnected from the heat pump.

### Step 2 — Install ESPHome

ESPHome is used to compile and upload the firmware to the Waveshare ESP32.

You can use ESPHome through Home Assistant or a standalone ESPHome installation.

Visit [esphome.io](https://esphome.io/) for installation instructions.

If you're already running Home Assistant, using the ESPHome Device Builder is generally the easiest option.

### Step 3 — Download the firmware

Choose one of the YAML configurations from the [Thermia iTec XTR](Thermia%20iTec%20XTR/) directory.

**Passive read-only**

[`thermia_itec_xtr_passive_1.0.yaml`](Thermia%20iTec%20XTR/thermia_itec_xtr_passive_1.0.yaml)

The receive-only version, recommended as a starting point.

**DCM read-only**

[`thermia_itec_xtr_DCM_readonly_1.0.yaml`](Thermia%20iTec%20XTR/thermia_itec_xtr_DCM_readonly_1.0.yaml)

The DCM-related development version. Review its operating requirements and supported functionality before use.

### Step 4 — Configure ESPHome

Create a new ESPHome device using the selected YAML configuration.

Configure the required secrets for:

- Wi-Fi network name and password
- Home Assistant API encryption key
- ESPHome OTA password
- Fallback access point password

The YAML uses the following secret names:

```yaml
wifi_ssid:
wifi_password:
thermia_api_encryption_key:
thermia_ota_password:
thermia_fallback_password:
```

Add the corresponding values to your ESPHome `secrets.yaml` file.

Do not publish your actual passwords or encryption keys.

The YAML already contains the ESP32 hardware configuration and Thermia communication settings.

### Step 5 — Flash the ESP32

Connect the Waveshare ESP32-S3-RS485-CAN to your computer using a USB data cable.

In ESPHome:

1. Select the device and open its configuration.
2. Compile the firmware.
3. Choose the USB installation method.
4. Flash the firmware to the ESP32.
5. Verify that the device connects to Wi-Fi.

The first upload is typically performed over USB. Subsequent updates can be installed through ESPHome OTA.

### Step 6 — Verify the Thermia RJ45 pinout and connect the gateway

Before connecting the Waveshare board to your Thermia heat pump, I strongly recommend checking the electrical pinout of the Thermia RJ45 communication port using a multimeter.

**Expected RJ45 pinout**

| RJ45 pins | Expected function |
|---|---|
| 1 + 2 | RS485 A |
| 3 + 4 | RS485 B |
| 5 + 6 | Ground / reference (GND) |
| 7 + 8 | +12 V supply |

**How to check with a multimeter**

1. Leave the Waveshare disconnected and keep the Thermia powered so the port voltages can be measured.
2. Set your multimeter to **DC voltage (V⎓)**, with a range of at least 20 V.
3. Using the RJ45 breakout adapter, place the black probe on pin 5 (expected GND).
4. Measure pin 7 with the red probe. You should expect approximately **+12 V DC**.
5. Measure pins 1 and 3 separately relative to pin 5. These are expected to carry RS485 data signals, generally measuring **around 4 V DC**.
6. Optionally measure between pins 1 and 3 to check for a differential RS485 voltage.

RS485 voltage readings depend on bus activity and biasing, so there is no single guaranteed voltage to expect on the data pins. A multimeter can help identify the power and reference connections, but cannot conclusively determine the RS485 A/B polarity.

**Do not connect the Waveshare if your measurements contradict the expected pinout.** Avoid accidentally bridging adjacent RJ45 terminals with the multimeter probes.

Once verified, connect:

- Thermia RJ45 pin 1 → Waveshare RS485 A
- Thermia RJ45 pin 3 → Waveshare RS485 B

Leave all other RJ45 pins unconnected to the Waveshare and power it separately using USB.

The ESP32 should now begin receiving communication from the heat pump.

### Step 7 — Add the device to Home Assistant

With the Waveshare connected to your Wi-Fi network, Home Assistant should be able to discover it through the ESPHome integration.

If automatic discovery doesn't work:

1. Open **Settings → Devices & services** in Home Assistant.
2. Add the ESPHome integration.
3. Enter the device's IP address or hostname.
4. Complete the connection using the configured API encryption key.

Once connected, the available Thermia sensors should appear as Home Assistant entities.

The exact number of sensors depends on the firmware variant and the data available on the bus.

## Supported hardware

### Heat pump

| Component | Tested configuration |
|---|---|
| Manufacturer | Thermia |
| Outdoor unit | iTec XTR M |
| Indoor unit | Total Compact |
| Controller generation | Pre-Genesis |
| Communication | Internal RS485 bus |

Other Thermia iTec XT/XTR models and older Danfoss-derived platforms may share parts of the protocol, but compatibility has not been established for every model.

This project should not be assumed compatible with the newer Thermia Genesis platform.

## Home Assistant integration

The ESP32 connects to Home Assistant through the native ESPHome API.

Once correctly configured and running, the gateway can expose supported heat pump sensors and diagnostic information as Home Assistant entities.

The objective is to support local dashboards, history, automations and, eventually, validated control functions without relying on Thermia Online.

The exact entity list depends on the chosen YAML configuration and the information available from the heat pump.

## Protocol research

The Thermia iTec XTR uses a proprietary communication architecture built around Modbus RTU-like messages.

Development has identified several communication addresses and their likely roles.

| Address | Observed role |
|---|---|
| `0x02` | Main controller state and communication |
| `0x06` | Expansion/accessory interface |
| `0x0A` | Room sensor communication |
| `0x0F` | Controller settings and state blocks |
| `0x1E` | Outdoor-unit communication and telemetry |

A substantial portion of the monitoring protocol has been mapped through real bus captures and controlled experiments.

The original Thermia Connect firmware is also being studied to understand native initialization, synchronization, polling, session management and recovery behaviour.

Not every observed register or message has a confirmed meaning.

## Safety and limitations

This is an independent reverse-engineering project, not an official Thermia product.

Communication with the internal bus can potentially interfere with normal heat pump operation if implemented incorrectly.

The project distinguishes passive monitoring, native protocol responses and controller parameter writes.

Parameter writes from Home Assistant are not yet enabled as a generally supported feature.

The integration is intended to preserve the heat pump's own controller logic, interlocks and safety mechanisms rather than bypass them.

Use at your own risk.

## Related projects and acknowledgements

Special thanks to [Piotr Romanowski](https://github.com/piotr-romanowski) for his independent [`thermia-bus-sniffer`](https://github.com/piotr-romanowski/thermia-bus-sniffer) project and valuable protocol research on related Thermia/Danfoss hardware.

A big thank you also goes to **everyone who contributed to this project by sharing logs, bus recordings, protocol captures, technical findings and feedback**. These contributions have been incredibly valuable in understanding the Thermia communication protocol, comparing behaviour across different heat pump models and moving the project forward.

### Related projects

- [Thermia ATEC — ESP Emulator of DCOM](https://github.com/fclauson/Thermia-ATEC-ESP-emulator-of-DCOM) by fclauson
- [Thermia Bus Sniffer](https://github.com/piotr-romanowski/thermia-bus-sniffer) by Piotr Romanowski
- [Thermia Home Assistant Integration](https://github.com/klejejs/ha-thermia-heat-pump-integration)
- [Thermia Online vs. Direct Modbus — Discussion #143](https://github.com/klejejs/ha-thermia-heat-pump-integration/discussions/143)

### Tools and platforms

- [ESPHome](https://esphome.io/)
- [Home Assistant](https://www.home-assistant.io/)

## Disclaimer

This project is not affiliated with, endorsed by or supported by Thermia, Danfoss or their related companies.

Thermia and Danfoss are trademarks of their respective owners.

---

**Development platform:** Thermia iTec XTR M / Total Compact  
**Integration:** ESP32-S3 · ESPHome · Home Assistant  
**Repository:** [ryckema/Thermia_itec](https://github.com/ryckema/Thermia_itec)
