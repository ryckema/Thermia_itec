# Thermia iTec XTR M — Write (Beta)

> [!WARNING]
> **Active control software.** This build transmits on the Thermia internal RS485 bus and can change heat-pump settings. It has been locally tested only on the documented Thermia iTec XTR M configuration. Verify wiring and safeguards and do not assume cross-model compatibility.

This folder contains the production-oriented active write build for the tested XTR M. Read-only remains the conservative choice when control is not required.

## Current file

`thermia_itec_xtr_m_waveshare_write_beta_v3_0.yaml`

v3.0 is derived from the final validated EXP374 v4d engine. The previous v2.1 file is retained as a historical/rollback baseline; v3.0 is the current production-oriented beta.

## Current write scope

All of the following are locally confirmed writable through the native `03E8/count14` desired-page flow:

| Setting | Register | Allowed range in v3.0 |
|---|---:|---:|
| Heating Curve | `0x03E8` | 22..56 |
| Heating Minimum | `0x03E9` | 20..40 °C |
| Heating Maximum | `0x03EA` | 40..85 °C |
| Curve Correction +5 | `0x03EB` | -5..+5 |
| Curve Correction 0 | `0x03EC` | -5..+5 |
| Curve Correction -5 | `0x03ED` | -5..+5 |
| Heating Stop | `0x03EE` | 0..22 °C |
| Reduced Temperature | `0x03EF` | 10..30 °C |
| Room Factor | `0x03F0` | 0..4 |
| Room Setpoint | `0x03F4` | 10..30 °C |

These ranges are implementation safety bounds for the tested installation, not universal Thermia claims.

## Home Assistant behavior

The write controls are Configuration entities. Values are synchronized from authoritative controller pages before writes are enabled.

### Home Assistant Configuration entities

The exact Home Assistant `entity_id` can be renamed by Home Assistant, so this table uses the ESPHome entity type and display name.

#### Write Beta v3.0 — current production-oriented beta

| Type | Display name | Register |
|---|---|---:|
| number | Thermia Write Heating Curve | `0x03E8` |
| number | Thermia Write Heating Minimum | `0x03E9` |
| number | Thermia Write Heating Maximum | `0x03EA` |
| number | Thermia Write Curve Correction +5 | `0x03EB` |
| number | Thermia Write Curve Correction 0 | `0x03EC` |
| number | Thermia Write Curve Correction -5 | `0x03ED` |
| number | Thermia Write Heating Stop | `0x03EE` |
| number | Thermia Write Reduced Temperature | `0x03EF` |
| number | Thermia Write Room Factor | `0x03F0` |
| number | Thermia Write Room Setpoint | `0x03F4` |

#### EXP381B — prepared production/UI consolidation

EXP381B keeps the proven protocol/write paths unchanged and reorganizes the production-facing Configuration entities to follow the Thermia manual's functional order. EXP381B is **PREPARED / NOT RUN**; these are the prepared display names, not a claim that EXP381B itself has completed its regression test.

| Group | Type | Display name | Register | Evidence status |
|---|---|---|---:|---|
| Operation | select | 01 Operation \| 01 Mode | `0x0553` | EXP380 COMPLETE / POSITIVE; Auto ↔ Compressor locally confirmed |
| Heating | number | 02 Heating \| 00 Room Setpoint | `0x03F4` | locally confirmed writable |
| Heating | number | 02 Heating \| 01 Heating Curve | `0x03E8` | locally confirmed writable |
| Heating | number | 02 Heating \| 02 Minimum | `0x03E9` | locally confirmed writable |
| Heating | number | 02 Heating \| 03 Maximum | `0x03EA` | locally confirmed writable |
| Heating | number | 02 Heating \| 04 Curve Correction +5 | `0x03EB` | locally confirmed writable |
| Heating | number | 02 Heating \| 05 Curve Correction 0 | `0x03EC` | locally confirmed writable |
| Heating | number | 02 Heating \| 06 Curve Correction -5 | `0x03ED` | locally confirmed writable |
| Heating | number | 02 Heating \| 07 Heating Stop | `0x03EE` | locally confirmed writable |
| Heating | number | 02 Heating \| 08 Reduced Temperature | `0x03EF` | locally confirmed writable |
| Heating | number | 02 Heating \| 09 Room Factor | `0x03F0` | locally confirmed writable |
| Heating / Service | number | 02 Heating \| 20 Startup HT | `0x0433` | confirmed persistent write |
| Heating / Service | number | 02 Heating \| 21 Heating Time | `0x0434` | confirmed persistent write |
| Hot Water | switch | 03 Hot Water \| 01 Enabled | `0x042E` | confirmed persistent write |
| Hot Water | select | 03 Hot Water \| 02 Mode | `0x042F` | Eco ↔ Comfort locally confirmed; Vacation Eco remains strongly supported but not write-proven |
| Cooling | switch | 04 Cooling \| 01 Enabled | `0x0442` | confirmed persistent write |
| Cooling | number | 04 Cooling \| 02 Desired Temperature | `0x0443` | confirmed persistent write |
| Cooling | number | 04 Cooling \| 03 Active Above | `0x0445` | mapped; semantic write still needs a valid-above-minimum confirmation |
| Cooling | number | 04 Cooling \| 04 Cooling Time | `0x0449` | confirmed persistent write |
| Cooling | switch | 04 Cooling \| 05 Room Sensor | `0x044C` | confirmed persistent write |
| Cooling | number | 04 Cooling \| 06 Room Hysteresis Low | `0x044D` | mapped; UI 0.5..5.0 °C in 0.1 °C steps; semantic write not yet separately confirmed |
| Cooling | number | 04 Cooling \| 07 Room Hysteresis High | `0x044E` | mapped; UI 0.5..5.0 °C in 0.1 °C steps; semantic write not yet separately confirmed |

The two `0x0433/0x0434` controls are grouped under **Heating / Service** in EXP381B because the Thermia commissioning manual places OPSTART_HT and VERWARMINGSTIJD under SERVICE → VERWARMING, rather than under Hot Water.

The persistent controls use the same desired-state UI convention: the user-selected new value is shown immediately and remains visible while queued or while a semantic transaction is in progress. A successful controller republish makes that value authoritative; a failed transaction is designed to roll the control back to the last confirmed controller value.

Rapid changes are serialized by a per-register dirty-set queue:
- one semantic transaction is active at a time;
- different register requests are preserved;
- a newer request for the same register replaces only that pending value;
- every queued register obtains a new fresh controller page;
- a 2 s settle interval is retained between confirmed writes.

Ordinary read sensors continue to show actual controller state, so the controller may visibly catch up over several seconds.

## Proven local write path

```text
fresh controller FC16 03E8/count14
    ↓
0708 W3 bit0 current-page request when needed
    ↓
0708 W1 bit0 + W3 bit0 desired-page selector
    ↓
controller FC03 03E8/count14
    ↓
ESP returns full fresh page with exactly one selected word changed
    ↓
controller FC16 03E8/count14 exact republish
    ↓
transaction confirmed; settle; next queued register
```

A write is not considered successful from an ACK alone. The controller republish must contain the requested selected value with zero extra changed words.

## Safety model

- no semantic write before authoritative Configuration synchronization;
- only the ten locally confirmed targets above are exposed;
- per-setting bounds are enforced;
- one active semantic transaction at a time;
- fresh full-page provenance is required for every queued write;
- desired page changes exactly one selected word;
- exact controller republish with zero extra deltas is required;
- parser/RX integrity changes, peer responder traffic, unexpected protocol shapes and timeouts fail closed;
- pending writes are cleared on semantic failure;
- DE remains LOW outside guarded protocol transmissions;
- controller-session recovery remains separately guarded;
- the fixed challenge replay is local-XTR evidence, not the recovered native Thermia/Danfoss challenge algorithm.

## Evidence status

EXP374 is COMPLETE / POSITIVE by explicit user confirmation of the final v4d behavior. EXP375A (`03E9`) and EXP375B (`03F0`) are COMPLETE / POSITIVE by explicit user confirmation. `03EB` and `03EC` were also locally confirmed through the rapid multi-setting queue test.

The remaining words `03F1/03F2/03F3/03F5` are not exposed for writing.

## Tested hardware and wiring

The YAML targets the Waveshare ESP32-S3-RS485-CAN / ESP32-S3-RS485-CAN-U used during the research.

For the tested isolated setup:

| Thermia RJ45 | Waveshare |
|---|---|
| pin 1 — RS485 A | A+ |
| pin 3 — RS485 B | B- |
| pin 5 — bus reference | not connected |
| pins 7/8 — +12 V | not connected |

Power the Waveshare board separately over USB-C.

The write build uses:

- GPIO18 = RX
- GPIO17 = TX
- GPIO21 = DE/direction

Leave the Waveshare **120 Ω termination jumper open/off** when attaching to the existing Thermia bus.

Bus parameters:

```text
Modbus RTU
9600 baud
8 data bits
Even parity
1 stop bit
```

## Installation

1. Start from a known healthy Thermia bus.
2. Copy `thermia_itec_xtr_m_waveshare_write_beta_v2_1.yaml` to ESPHome.
3. Add the required credentials to `secrets.yaml`.
4. Validate/compile the YAML in your own ESPHome installation.
5. Install the firmware.
6. Confirm that normal read entities update and **Thermia DCM Runtime Active** becomes healthy before attempting a write.
7. Enable **Thermia Desired Room Setpoint** in Home Assistant if it is still disabled by default.
8. Select a target inside 10..30 °C.
9. Press **Thermia Apply Room Setpoint**.
10. Confirm the result through the normal Room Setpoint entity and the write-status/confirmation entities.

Required secrets:

```yaml
wifi_ssid: "..."
wifi_password: "..."
thermia_api_encryption_key: "..."
thermia_ota_password: "..."
thermia_fallback_password: "..."
```

Write Beta v2.1 was statically checked for duplicate/missing ESPHome IDs, TX-site DE/write/flush/DE-low structure, and the critical hard-coded Modbus CRCs. It has **not** been ESPHome-compiled in this preparation step, so compile/validate it against the ESPHome version installed on your system before flashing.

## Normal write behavior

A successful transaction should end with a controller-originated exact `03E8/count14` republish and **Thermia Last Setpoint Write Confirmed** becoming true.

If the page cache is stale, seeing a refresh request before the semantic write is expected behavior. The firmware intentionally obtains a fresh controller page rather than reusing stale state.

Changing the physical Thermia setpoint while the integration is running is also expected to update the controller-originated cache; the next HA write should therefore start from the newest observed controller state.

## When to stop and recover

Do not continue semantic writes if the Thermia reports an abnormal Online/Link state, the DCM runtime cannot qualify, unexpected session traffic appears, or write confirmation does not match the requested one-word page change.

For a conservative rollback, install one of the [Read-only](../Read-only/) YAML files. Those builds do not configure Thermia TX and keep the RS485 driver disabled.

A Thermia controller reboot is not part of the normal write procedure and should not be used merely to force a failed transaction. If a genuine controller power cycle occurs, v2.1 may perform the one locally proven guarded recovery automatically. If that recovery fails, or a second bus-loss event occurs in the same ESP boot, leave the bus alone and restart/roll back rather than forcing further transmissions.

## Evidence

### EXP352 — raw-log proven write path

EXP352 established the controller-driven Room Setpoint mechanism:

- retained runtime qualified without a hard-coded historical `03E8` image;
- W3 bit0 requested a fresh controller `03E8` page with W1=0;
- the desired-page path changed only `03F4`;
- the controller republished the exact expected page;
- repeated HA writes worked in the same retained runtime;
- native front-display changes updated the live source cache.

### EXP355 — raw-log proven controller recovery

EXP355 proved one real Thermia/controller power-cycle recovery while the ESP stayed powered:

- recovery armed after 5166 ms of qualified idle bus silence;
- the old semantic cache was invalidated before session restart;
- bus return entered the guarded fresh-session path;
- A80E/A80F reached `0000/0005`;
- one locally proven replay response was sent on the exact 071C/0730 challenge;
- the complete 32-stage initial sync ran through `06F4/count19`;
- stage 40 was re-entered and fresh runtime FC16 + 0708 service re-qualified the session.

### EXP357 — raw-log proven reusable stale-cache refresh

EXP357 removed the obsolete one-refresh-per-ESP-boot experimental limit and locally confirmed:

- refresh #1: W3 bit0 requested a fresh controller `03E8/count14`, followed by a confirmed 22 -> 20 °C write;
- a later **refresh #2 in the same ESP boot** again produced controller `FC16 03E8/count14`;
- refresh #2 was followed by a confirmed 22 -> 24 °C Room Setpoint write with `extraDeltaWords=0`;
- the run reached five confirmed semantic writes while runtime integrity counters remained clean.

This is the evidence used to promote reusable refresh into Write Beta v2. v2.1 keeps that protocol behavior unchanged and only hardens the implementation around it.

See the canonical research files for the full evidence trail:

- [THERMIA_PROJECT_STATE.md](../Research/THERMIA_PROJECT_STATE.md)
- [EXPERIMENT_LOG.md](../Research/EXPERIMENT_LOG.md)
- [PROTOCOL_FINDINGS.md](../Research/PROTOCOL_FINDINGS.md)

## Scope discipline

This folder should stay conservative. New writable settings belong in controlled research experiments first and should only be promoted here after local evidence establishes the target, payload, expected effect, confirmation behavior and rollback path.
