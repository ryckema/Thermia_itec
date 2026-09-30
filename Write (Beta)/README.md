# Thermia iTec XTR M — Write (Beta)

This folder contains the **active write-capable beta** for the tested Thermia iTec XTR M with the older/non-Genesis controller.

Unlike the [Read-only](../Read-only/) builds, this firmware configures RS485 TX and actively participates in the native Thermia/Danfoss Online/DCM path. It preserves the normal monitoring entities while adding a guarded Room Setpoint write flow.

> **Beta means active protocol participation.** The write mechanism is locally proven on the tested XTR M, but arbitrary fresh controller-session/power-loss recovery is less mature than retained-session operation. Do not assume this build is compatible with every Thermia/Danfoss controller.

## Current file

`thermia_itec_xtr_m_waveshare_write_beta_v1.yaml`

## Current write scope

Exactly one semantic setting is enabled:

| Setting | Page | Register | Allowed values |
|---|---:|---:|---:|
| Room Setpoint | `0x03E8/count14` | `0x03F4` | whole degrees `10..30 °C` |

No other Thermia setting is writable in this build.

The 10..30 °C limit reflects the locally observed native control range on the tested installation. It is an implementation guard, not a claim about every Thermia model.

## Home Assistant controls

The two user-facing controls are:

- **Thermia Desired Room Setpoint**
- **Thermia Apply Room Setpoint**

The number entity is deliberately **disabled by default** and belongs to Home Assistant's Configuration category.

Changing **Thermia Desired Room Setpoint** only selects the requested value. It does **not** transmit a semantic write. Pressing **Thermia Apply Room Setpoint** explicitly arms the transaction.

Useful status entities include:

- **Thermia DCM Write Status**
- **Thermia DCM Write Last Event**
- **Thermia DCM Runtime Active**
- **Thermia Last Setpoint Write Confirmed**
- **Thermia Confirmed Setpoint Writes**
- **Thermia 03E8 Refresh Requests**
- **Thermia 03E8 Refresh Confirmed**

Additional protocol diagnostics are present but mostly disabled by default.

## Proven local write path

The production-beta implementation is derived from the raw-log-proven EXP352 flow and adopts the reusable-refresh behavior associated with the user-confirmed successful EXP353 follow-up.

The active sequence is:

```text
persistent / retained DCM runtime
    ↓
if 03E8 source cache is missing or older than 300 s:
    0708 W3 bit0 current-page request
    ↓
controller FC16 03E8/count14
    ↓
fresh controller page becomes source cache
    ↓
0708 W1 bit0 + W3 bit0 desired-page selector
    ↓
controller FC03 03E8/count14
    ↓
ESP returns the source page with only 03F4 changed
    ↓
controller FC16 03E8/count14 exact republish
    ↓
write confirmed; republish becomes next source cache
```

Native Thermia front-display setpoint changes can also refresh that source cache. EXP352 locally demonstrated this with a front-display change to 19 °C followed by a later HA write starting from the new 19 °C controller state rather than stale data.

## Safety model

The write build keeps the following guards:

- only `03F4` is semantically writable;
- requested and current values must both be whole degrees from 10 through 30 °C;
- no historical `03E8` page is seeded as write-eligible at boot;
- a missing or >300-second-old source page is refreshed from the controller before writing;
- only one semantic transaction can be active at a time;
- the desired page is copied from the latest controller-originated/confirmed `03E8/count14` page;
- exactly one word, `03F4`, may differ in that desired page;
- the controller must republish the expected page with zero extra changed words before the write is considered confirmed;
- unexpected/session-conflicting traffic fails closed rather than broadening the write behavior;
- RS485 DE is kept low except during guarded protocol transmission.

The build also services the proven runtime/ACK traffic required by the emulated DCM session. Those protocol frames are part of the active integration even when no Room Setpoint write is pending.

## Known limitations

The best-tested operating case is a retained controller-side DCM session across ESP OTA/reboot.

The current implementation should **not** be interpreted as proof that:

- every cold controller boot or arbitrary power-loss/session-recovery path is solved;
- W5=`0006` is semantically a generic “connected” flag;
- all W2:W3 bitmap pages behave like the locally tested `03E8` case;
- any register other than `03F4` is safe to write;
- this protocol behavior is universal across Thermia/Danfoss models.

If the DCM runtime does not qualify, a write is refused. Do not weaken the guards to force a transaction.

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
2. Copy `thermia_itec_xtr_m_waveshare_write_beta_v1.yaml` to ESPHome.
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

The repository release was structurally/YAML checked during preparation, but that check is not a substitute for compiling against the ESPHome version installed on your system.

## Normal write behavior

A successful transaction should end with a controller-originated exact `03E8/count14` republish and **Thermia Last Setpoint Write Confirmed** becoming true.

If the page cache is stale, seeing a refresh request before the semantic write is expected behavior. The firmware intentionally obtains a fresh controller page rather than reusing stale state.

Changing the physical Thermia setpoint while the integration is running is also expected to update the controller-originated cache; the next HA write should therefore start from the newest observed controller state.

## When to stop and recover

Do not continue semantic writes if the Thermia reports an abnormal Online/Link state, the DCM runtime cannot qualify, unexpected session traffic appears, or write confirmation does not match the requested one-word page change.

For a conservative rollback, install one of the [Read-only](../Read-only/) YAML files. Those builds do not configure Thermia TX and keep the RS485 driver disabled.

A Thermia controller reboot is not part of the normal write procedure and should not be used merely to force a failed transaction.

## Evidence

The strongest archived local evidence is EXP352:

- retained runtime qualified without a hard-coded historical `03E8` image;
- W3 bit0 requested a fresh controller `03E8` page with W1=0;
- the desired-page path changed only `03F4`;
- the controller republished the exact expected page;
- repeated HA writes worked in the same retained runtime;
- native front-display changes updated the live source cache;
- the user confirmed no alarm and the DCM icon remained visible.

EXP353 is **COMPLETE / POSITIVE by explicit user confirmation** for the reusable-refresh follow-up. Its detailed raw log/YAML is not currently archived, so this README deliberately does not invent exact EXP353 counts or timings.

See the canonical research files for the full evidence trail:

- [THERMIA_PROJECT_STATE.md](../Research/THERMIA_PROJECT_STATE.md)
- [EXPERIMENT_LOG.md](../Research/EXPERIMENT_LOG.md)
- [PROTOCOL_FINDINGS.md](../Research/PROTOCOL_FINDINGS.md)

## Scope discipline

This folder should stay conservative. New writable settings belong in controlled research experiments first and should only be promoted here after local evidence establishes the target, payload, expected effect, confirmation behavior and rollback path.
