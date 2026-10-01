# Thermia iTec XTR M — Write (Beta)

> [!WARNING]
> **Active control software.** This build transmits on the Thermia internal RS485 bus and can change heat-pump settings. It has been locally tested only on the documented Thermia iTec XTR M configuration. Verify your wiring and configuration, keep the documented safeguards intact, and do not assume compatibility with other Thermia/Danfoss models. Use at your own risk; see the repository's [Disclaimer and license](../README.md#disclaimer-and-license).

This folder contains the **active write-capable beta** for the tested Thermia iTec XTR M with the older/non-Genesis controller.

Unlike the [Read-only](../Read-only/) builds, this firmware configures RS485 TX and actively participates in the native Thermia/Danfoss Online/DCM path. It preserves the normal monitoring entities while adding a guarded Room Setpoint write flow.

> **Beta means active protocol participation.** Room Setpoint writes, reusable stale-cache refresh and one controller cold-reboot recovery per ESP boot are locally proven on the tested XTR M. Do not assume this behavior is compatible with every Thermia/Danfoss controller or firmware.

## Current file

`thermia_itec_xtr_m_waveshare_write_beta_v2_1.yaml`

Write Beta v2.1 is a **hardening revision** of v2. It adds no new writable register/page and no new protocol payload. It tightens runtime ACK eligibility and runtime qualification before the next regression test.

Older write builds are archived under `old versions/`:

- `old versions/thermia_itec_xtr_m_waveshare_write_beta_v2.yaml` — pre-hardening v2 baseline;
- `old versions/thermia_itec_xtr_m_waveshare_write_beta_v1.yaml` — older pre-recovery baseline.

Only the current v2.1 build remains at the top level of the Write (Beta) folder.

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

Additional protocol diagnostics are present but mostly disabled by default. v2.1 also exposes **Thermia DCM Recovery Count**, **Thermia DCM Session State**, and **Thermia DCM Last Recovery Result** for recovery/qualification visibility.

## Proven local write path

The production-beta implementation is derived from the raw-log-proven EXP352 write flow, the locally proven EXP355 controller-session recovery, and the raw-log-proven EXP357 reusable stale-cache refresh/write test.

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

### Controller reboot recovery

Write Beta v2.1 retains the locally proven EXP355 recovery path for a Thermia/controller power cycle while the ESP remains powered:

```text
qualified stage-40 runtime
    ↓
>=5 s complete valid-bus silence while semantic write state is idle
    ↓
invalidate pre-reboot 03E8 cache and reset session-local state
    ↓
controller bus returns
    ↓
A80E=0000 / A80F=0005 guarded 071C/0730 challenge
    ↓
send one locally proven replay response
    ↓
ordered 32-stage initial sync through 06F4/count19
    ↓
return to stage 40
    ↓
fresh runtime FC16 ACK + 0708 W5=0006
    ↓
recovered runtime qualified
```

The fixed 16-byte response is **not** documented as the native Thermia challenge-response algorithm. Genuine gateway captures show different responses for different challenges/sessions. On this XTR M, EXP355 proved that the previously captured response can be replayed successfully under the guarded cold-boot state.

For safety, v2.1 permits only **one automatic controller recovery attempt per ESP boot**. A second >=5 s controller bus-loss event fails closed and requires an ESP restart. Repeated controller recoveries per ESP boot have not yet been locally proven.

## Safety model

The write build keeps the following guards:

- only `03F4` is semantically writable;
- requested and current values must both be whole degrees from 10 through 30 °C;
- no historical `03E8` page is seeded as write-eligible at boot;
- a missing or >300-second-old source page is refreshed from the controller before writing;
- stale-cache refresh is reusable in the same ESP boot; EXP357 locally confirmed a second W3-bit0 refresh followed by a confirmed write;
- only one semantic transaction can be active at a time;
- the desired page is copied from the latest controller-originated/confirmed `03E8/count14` page;
- exactly one word, `03F4`, may differ in that desired page;
- the controller must republish the expected page with zero extra changed words before the write is considered confirmed;
- unexpected/session-conflicting traffic fails closed rather than broadening the write behavior;
- RS485 DE is kept low except during guarded protocol transmission;
- controller-reboot recovery is armed only from a clean, qualified, semantically idle stage-40 runtime;
- recovery invalidates the old semantic cache before re-entering the fresh-session bootstrap;
- the recovered session must re-qualify with fresh runtime FC16 service plus a 0708 exchange before writes are allowed again.
- **Thermia DCM Runtime Active** stays false until that FC16 + `0708` qualification is actually complete;
- runtime `04A6/count13` is capture-only / NO ACK; this matches the canonical finding that it can be parallel/state-dependent traffic;
- `0834/count18` is locally unsupported and is never ACKed; if encountered it fails closed;
- runtime `085F/count5` is ACKed only for the two locally proven payload forms: all-zero or `0861=0x0800`; any other payload fails closed.

The build also services the proven runtime/ACK traffic required by the emulated DCM session. Those protocol frames are part of the active integration even when no Room Setpoint write is pending.

### v2.1 hardening scope

The v2.1 changes come from a static production-code audit against the canonical protocol findings. They deliberately **remove permissive behavior rather than add new protocol capability**:

- remove stage-40 ACK behavior for runtime `04A6/count13`;
- remove `0834/count18` from the ACK whitelist;
- qualify `085F/count5` by exact locally proven payload rather than address/count alone;
- use one runtime-qualified latch for both FC16-first and `0708`-first event ordering;
- publish **Runtime Active** only after qualification, not merely on stage-40 entry;
- re-arm the 15-minute soak diagnostic after controller recovery;
- correct the firmware-build label and the disabled-by-default Room Setpoint number entity.

These changes are **PREPARED / NOT YET LIVE-REGRESSION-TESTED**. EXP358 is the planned regression run. v2.1 therefore remains beta until that result is supplied.

## Known limitations

The best-tested operating cases are retained stage-40 operation, reusable Room Setpoint writes, reusable stale-cache refresh, and one controller cold-reboot recovery while the ESP remains powered.

The current implementation should **not** be interpreted as proof that:

- repeated controller cold-reboot recoveries in one ESP boot are solved;
- full simultaneous ESP + Thermia mains-loss/cold-start behavior is solved;
- recovery from arbitrary interruption points inside the initial-sync chain is solved;
- the fixed 16-byte replay value is the native Thermia/Danfoss challenge-response algorithm;
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
