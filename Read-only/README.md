# Thermia legacy iTec — Read-only

This folder contains **passive RX-only** ESPHome builds for the legacy/non-Genesis Thermia iTec family through its internal RS485 bus. The main production profile targets the iTec XTR M; a separate iTec Eco compatibility profile is included and keeps unconfirmed cross-model mappings conservative.

These builds do **not** transmit Thermia Modbus frames. GPIO17/TX is intentionally not configured and the RS485 driver-enable line is held low. Use this folder when monitoring is sufficient or when you want the lowest-risk starting point.

## Which file should I use?

### Public / optimized

`Thermia itec XTR/thermia_itec_xtr_m_waveshare_public_v29.yaml`

Recommended for normal Home Assistant use.

It keeps the useful decoded entities and a small set of diagnostics while removing most reverse-engineering overhead. Logging is intentionally quiet and the generic raw-register mapper is not included.

### iTec Eco compatibility profile

`iTec Eco/thermia_itec_eco_waveshare_public_v01.yaml`

Use this for a **Thermia iTec Eco** on the legacy Danfoss DHP-AQ controller family.

It is derived from the XTR public v29 decoder, but adapts the parts that are independently confirmed on iTec Eco hardware/captures: the Eco outdoor-unit `0014` bitfield, `A80F` condenser-pump speed, `03F3` High Power, the shared `03E8` heating/settings page, and the Eco-confirmed compressor/fan/current/EEV fields. XTR-derived fields that are not independently Eco-confirmed are labelled **candidate** and disabled by default where practical.

The Eco profile is also strictly RX-only: GPIO17/TX is not configured and GPIO21/DE is held LOW.

### Research / register mapping

`Thermia itec XTR/thermia_itec_xtr_m_waveshare_research_v29.yaml`

Use this when collecting captures or validating additional registers.

It is still completely RX-only and retains the research instrumentation:

- raw Modbus frame logging;
- generic change-only register mapping;
- additional raw diagnostic entities;
- detailed protocol logging hooks.

**v29 defaults to WARN-only logging**, just like the public build. The DEBUG/VERBOSE research instrumentation is therefore suppressed during normal operation. Temporarily raise only the specific logger categories you need when making a controlled capture, then return them to WARN.

New mappings should be verified here before being promoted to the public build.

## v29 changes

v29 remains **strictly RX-only**. It does not import the DCM TX/write engine from Write (Beta).

Changes from v28:

- passively decodes the now locally proven `042E/count15`, `0442/count13` and `0546/count20` settings fields;
- adds read-only entities for Hot Water Enabled/Mode, Startup HT, Heating Time, Cooling Enabled/Desired Temperature/Active Above/Time/Room Sensor/Room Hysteresis Low/High, and Operation Mode;
- enables by default the useful service/read-only entities Expansion Valve Steps, Refrigerant Temperature 1/2, Discharge Gas Temperature, Compressor Temperature and Room Setpoint Mirror;
- updates protocol comments through EXP380–EXP383 while keeping STRONGLY SUPPORTED TEST mappings out of the normal read-only entity set;
- keeps the research build's generic mapper and raw capture tooling;
- keeps WARN-only default logging;
- retains the v28 files as rollback/history.

No read-only TX pin, DCM emulation, write control or semantic response has been added.

## Tested hardware

The current XTR YAML files target:

- Thermia iTec XTR M with the older/non-Genesis controller used for this research;
- Waveshare ESP32-S3-RS485-CAN / ESP32-S3-RS485-CAN-U;
- ESPHome and Home Assistant.

The bus settings confirmed on the tested installation are:

```text
Modbus RTU
9600 baud
8 data bits
Even parity
1 stop bit
RX not inverted
```

## Wiring

For the tested isolated Waveshare setup:

| Thermia RJ45 | Waveshare |
|---|---|
| pin 1 — RS485 A | A+ |
| pin 3 — RS485 B | B- |
| pin 5 — bus reference | not connected |
| pins 7/8 — +12 V | not connected |

Power the Waveshare board separately over USB-C.

The YAML uses:

- GPIO18 = RX
- GPIO21 = DE/direction, forced LOW
- GPIO17/TX = **not configured**

Leave the Waveshare **120 Ω termination jumper open/off** when attaching passively to the existing Thermia bus.

## Installation

1. Choose the public or research YAML.
2. Copy it to your ESPHome configuration directory.
3. Add the required values to your ESPHome `secrets.yaml`.
4. Optionally change `device_name` and `friendly_name` under `substitutions`.
5. Validate the YAML in ESPHome.
6. Connect RS485 A/B as shown above.
7. Power the ESP32 over USB-C and install the firmware.
8. Add the ESPHome device to Home Assistant.

Required secrets:

```yaml
wifi_ssid: "..."
wifi_password: "..."
thermia_api_encryption_key: "..."
thermia_ota_password: "..."
thermia_fallback_password: "..."
```

## What is currently decoded?

The shared v29 read-only decoder exposes useful values in these groups:

- room temperature and room setpoint;
- outdoor and supply temperature;
- DHW temperatures and delta-T;
- heating curve, minimum, maximum, corrections, heating stop, reduced temperature and room factor;
- passive Hot Water settings: Enabled, Mode, Startup HT and Heating Time;
- passive Cooling settings: Enabled, Desired Temperature, Active Above, Cooling Time, Room Sensor and both room hysteresis values;
- passive Operation Mode from the proven `0553` field;
- condenser inlet/outlet temperatures and delta-T;
- compressor frequency, current and running state;
- high pressure;
- outdoor-unit target temperature, fan speed and expansion-valve information;
- controller / operating context;
- SG Ready mode;
- heating, DHW and cooling activity;
- bus and ESP diagnostics.

Some additional values are intentionally diagnostic or disabled by default because their exact semantics are not sufficiently established.

The **research** build exposes substantially more raw protocol information than the public build.

## Persisted heating-settings cache

The XTR builds persist the validated `0x0F:03E8..03F5` heating/settings block locally.

This avoids Home Assistant showing `Unknown` after an ESP reboot while waiting for the Thermia controller to broadcast that relatively infrequent page again. Persisted values are only refreshed from a genuine live controller `FC16 03E8..03F5` frame.

Persistence does not make the read-only build active: it is local ESP flash storage only.

## Important interpretation notes

The decoder intentionally keeps uncertain fields conservative.

In particular:

- `0x0F:03F4` is the room-setpoint mirror used by the monitoring build.
- `0x0A:B3C5` is the controller-propagated/confirmed room setpoint, not treated as a direct master-write input.
- `0x02:A80E` is not treated as a DCM-present flag.
- `0x02:A80F` has strong cross-model evidence for a condenser/circulation-pump-speed meaning, but is not promoted to locally confirmed XTR semantics without a matching local test.
- unknown or cross-model-only fields remain diagnostic instead of being presented as confirmed XTR behavior.

For the evidence level behind a mapping, use the canonical research documents rather than inferring meaning from an entity name alone.

## Public versus research logging

The public build is designed for 24/7 use and normally logs warnings only.

The research build is deliberately more verbose. It is useful for captures but creates more log/API/heap activity and is not intended as the minimum-overhead daily configuration.

## No write support in this folder

Nothing under this Read-only XTR runtime is intended to emulate the DCM or change a Thermia setting.

All active control is isolated in the repository's [Write (Beta)](../Write%20%28Beta%29/) folder. Do not add experimental TX to the read-only files; keeping the passive and active builds separate is an intentional safety boundary.

## Research documentation

The protocol model and experiment history live in [../Research/](../Research/):

- [THERMIA_PROJECT_STATE.md](../Research/THERMIA_PROJECT_STATE.md)
- [EXPERIMENT_LOG.md](../Research/EXPERIMENT_LOG.md)
- [PROTOCOL_FINDINGS.md](../Research/PROTOCOL_FINDINGS.md)

The read-only decoder should only promote mappings that have enough evidence for normal Home Assistant use.
