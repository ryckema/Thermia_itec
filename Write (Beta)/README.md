# Thermia iTec XTR M — Write (Beta)

> [!WARNING]
> **Active control software.** This build transmits on the Thermia internal RS485 bus and can change heat-pump settings. It has been locally tested only on the documented Thermia iTec XTR M configuration. Verify wiring and safeguards and do not assume cross-model compatibility.

This folder contains the active native-control build for the tested XTR M. Read-only remains the conservative choice when control is not required.

## Current file

`thermia_itec_xtr_m_waveshare_write_beta_v4_0.yaml`

Write Beta v4.0 is based on the **EXP381B COMPLETE / POSITIVE** runtime baseline and the EXP382 offline gap analysis. It also contains the seven **EXP383 TEST controls** requested for staged validation.

Important distinction:

- the established controls listed as **PROVEN** below have local XTR M write evidence;
- entities containing **TEST** are only **STRONGLY SUPPORTED** mappings;
- publishing them in v4.0 does **not** promote them to proven protocol behavior;
- EXP383 itself is **PREPARED / NOT RUN** until individual results are supplied.

The previous v3.0 build remains useful as a rollback point before the EXP383 candidate controls were added.

## Proven write scope

The following controls are locally confirmed writable through the native controller-owned page mechanism.

### Heating — `03E8/count14`

| Home Assistant control | Register | Range used in v4.0 | Evidence |
|---|---:|---:|---|
| 02 Heating \| 00 Room Setpoint | `0x03F4` | 10..30 °C | PROVEN |
| 02 Heating \| 01 Heating Curve | `0x03E8` | 22..56 | PROVEN |
| 02 Heating \| 02 Minimum | `0x03E9` | 20..40 °C | PROVEN |
| 02 Heating \| 03 Maximum | `0x03EA` | 40..85 °C | PROVEN |
| 02 Heating \| 04 Curve Correction +5 | `0x03EB` | -5..+5 | PROVEN |
| 02 Heating \| 05 Curve Correction 0 | `0x03EC` | -5..+5 | PROVEN |
| 02 Heating \| 06 Curve Correction -5 | `0x03ED` | -5..+5 | PROVEN |
| 02 Heating \| 07 Heating Stop | `0x03EE` | implementation bound 0..22 °C | PROVEN |
| 02 Heating \| 08 Reduced Temperature | `0x03EF` | 10..30 °C | PROVEN |
| 02 Heating \| 09 Room Factor | `0x03F0` | 0..4 | PROVEN |

### Hot water / Heating service — `042E/count15`

| Home Assistant control | Register | Evidence |
|---|---:|---|
| 03 Hot Water \| 01 Enabled | `0x042E` | PROVEN |
| 03 Hot Water \| 02 Mode | `0x042F` | write path PROVEN; not every enum individually exercised |
| 02 Heating \| 20 Startup HT | `0x0433` | PROVEN |
| 02 Heating \| 21 Heating Time | `0x0434` | PROVEN |

### Cooling — `0442/count13`

| Home Assistant control | Register | Evidence |
|---|---:|---|
| 04 Cooling \| 01 Enabled | `0x0442` | PROVEN |
| 04 Cooling \| 02 Desired Temperature | `0x0443` | PROVEN |
| 04 Cooling \| 03 Active Above | `0x0445` | PROVEN; dynamic minimum `max(10 °C, Heating Stop + 3 K)` |
| 04 Cooling \| 04 Cooling Time | `0x0449` | PROVEN |
| 04 Cooling \| 05 Room Sensor | `0x044C` | PROVEN |
| 04 Cooling \| 06 Room Hysteresis Low | `0x044D` | PROVEN; raw/10; 0.5..5.0 |
| 04 Cooling \| 07 Room Hysteresis High | `0x044E` | PROVEN; raw/10; 0.5..5.0 |

### Operation — `0546/count20`

| Home Assistant control | Register | Evidence |
|---|---:|---|
| 01 Operation \| 01 Mode | `0x0553` | PROVEN by EXP380; not every enum value individually exercised |

## EXP383 TEST controls

These seven controls are fully wired into the existing native semantic-write engines but remain **STRONGLY SUPPORTED / TEST** until local XTR M validation.

| Home Assistant control | Register | Current interpretation | Current implementation |
|---|---:|---|---|
| 03 Hot Water \| 03 **TEST** Top-up | `0x0430` | Hot Water TOP_UP | switch 0/1 |
| 04 Cooling \| 08 **TEST** Hysteresis | `0x0444` | INFORMATION Cooling Hysteresis | 0.0..12.0 K, step 0.1, tentative raw×10 |
| 04 Cooling \| 09 **TEST** Configuration | `0x0446` | SERVICE Cooling type | Uit / Actieve koeling / Geïntegreerd in WP |
| 04 Cooling \| 10 **TEST** Stop Threshold | `0x0448` | SERVICE Cooling STOP threshold | raw 0..100 |
| 04 Cooling \| 11 **TEST** Max Start Temperature | `0x044A` | MAX_STARTTEMP | 5..55 °C; guarded against current Min Stop |
| 04 Cooling \| 12 **TEST** Min Stop Temperature | `0x044B` | MIN_STOPTEMP | 5..55 °C; guarded against current Max Start |
| 01 Operation \| 02 **TEST** Link Integration | `0x0559` | Link Integration | Light / System |

### Test order

Test one new candidate at a time, use the smallest reversible change, confirm the Thermia-side semantic effect, then roll it back before moving to the next candidate.

Recommended order:

`0430 → 0444 → 0446 → 0448 → 044A → 044B → 0559`

`0559 Link Integration` is intentionally last. Changing the integration mode may plausibly affect the Online/DCM-style session itself. If the session or normal bus behavior changes unexpectedly after this test, stop and do not retry automatically.

## Native write model

The implementation does not behave like an arbitrary second Modbus master writing controller registers directly. It emulates the native page-owned Online/DCM path.

For each controlled page:

```text
fresh authoritative controller FC16 page
    ↓
current-page selector if refresh is needed
    ↓
desired-page selector
    ↓
controller FC03 reads that exact page from the emulated 0x0F side
    ↓
ESP returns the full fresh page with exactly one selected word changed
    ↓
controller FC16 republishes the page
    ↓
success only when target matches and extraDeltaWords = 0
```

The mechanism is locally proven on:
- `03E8/count14`
- `042E/count15`
- `0442/count13`
- `0546/count20`

A standard ACK or a transmitted desired page by itself is not considered semantic success.

## Home Assistant behavior

Configuration controls are grouped in the Thermia-manual order:

1. Operation
2. Heating
3. Hot Water
4. Cooling

The normal read sensors remain controller-authoritative.

During an active or queued semantic write, Configuration controls may temporarily retain the user's desired value while the controller catches up. A successful controller republish makes it authoritative. A failed transaction rolls the control back to the last confirmed value where possible.

The exact entity catalogue is maintained in:

[Research/HOME_ASSISTANT_ENTITIES.md](../Research/HOME_ASSISTANT_ENTITIES.md)

## Safety model

The v4.0 build retains the existing fail-closed guards:

- authoritative current page required before semantic TX;
- one selected word changed per semantic transaction;
- exact expected page/count only;
- exact controller republish required;
- `extraDeltaWords=0` required for success;
- one active semantic transaction at a time;
- queued desired-state handling is serialized;
- parser/RX integrity changes fail closed;
- unexpected peer responder/session traffic fails closed;
- no automatic semantic retry after failure;
- driver-enable remains LOW outside guarded TX;
- controller-session recovery remains separately guarded;
- the fixed challenge replay is only locally validated behavior, not the recovered native challenge-response algorithm.

For the EXP383 candidate controls, add this rule:

> **Do not use simultaneous candidate changes as the first validation. Test one TEST entity at a time and correlate the physical/front-panel effect.**

## EXP383 result classification

A candidate becomes locally PROVEN only when both are true:

1. the controller republishes the exact target with no unrelated page changes; and
2. the observed Thermia behavior/menu value matches the expected semantic field.

Possible classifications:

- **COMPLETE / POSITIVE** — exact republish and correct semantic effect;
- **COMPLETE / NEGATIVE** — controller keeps/rejects the original selected value without unrelated changes;
- **COMPLETE / INCONCLUSIVE** — exact transport behavior is seen but the semantic effect is ambiguous, or unexpected session/page behavior occurs.

Do not promote a candidate solely because the FC16 republish accepted the raw word.

## Tested hardware and wiring

The YAML targets the Waveshare ESP32-S3-RS485-CAN / ESP32-S3-RS485-CAN-U used during the research.

For the tested isolated setup:

| Thermia RJ45 | Waveshare |
|---|---|
| pin 1 — RS485 A | A+ |
| pin 3 — RS485 B | B- |
| pin 5 — bus reference | not connected |
| pins 7/8 — +12 V | not connected |

Power the Waveshare separately over USB-C.

Write build GPIO:
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

1. Start from a healthy Thermia bus and a known working EXP381B/v4-compatible configuration.
2. Copy `thermia_itec_xtr_m_waveshare_write_beta_v4_0.yaml` into ESPHome.
3. Add the required secrets.
4. Validate and compile against your installed ESPHome version.
5. Flash the firmware.
6. Confirm that normal read entities update and the persistent runtime qualifies before changing any setting.
7. First verify one already-PROVEN control.
8. Only then test the TEST controls, one at a time.

Required secrets:

```yaml
wifi_ssid: "..."
wifi_password: "..."
thermia_api_encryption_key: "..."
thermia_ota_password: "..."
thermia_fallback_password: "..."
```

The EXP383/v4.0 YAML was statically checked during preparation for YAML parsing, duplicate ESPHome IDs and missing `id(...)` references. The existing page selector frames were deliberately retained. **No ESPHome compile was run during preparation**, so compile/validate it locally before flashing.

## Recovery / stop criteria

Stop active testing if:
- normal bus updates become abnormal;
- parser resync/RX-drop counters change unexpectedly;
- another responder appears;
- the controller requests an unexpected page/count;
- exact republish does not occur;
- `extraDeltaWords` is non-zero;
- the semantic effect does not match the candidate;
- Link/Online session behavior changes unexpectedly.

For conservative rollback, install one of the [Read-only](../Read-only/) builds or the previous known-good write baseline.

Do not use controller power cycling merely to force a failed write transaction.

## Evidence trail

Canonical project state and experiment evidence:

- [THERMIA_PROJECT_STATE.md](../Research/THERMIA_PROJECT_STATE.md)
- [EXPERIMENT_LOG.md](../Research/EXPERIMENT_LOG.md)
- [PROTOCOL_FINDINGS.md](../Research/PROTOCOL_FINDINGS.md)
- [HOME_ASSISTANT_ENTITIES.md](../Research/HOME_ASSISTANT_ENTITIES.md)
- [EXP382_OFFLINE_GAP_ANALYSIS.md](../Research/EXP382_OFFLINE_GAP_ANALYSIS.md)

## Scope discipline

This folder remains **Beta**, even though the established controls are locally functional. STRONGLY SUPPORTED mappings remain explicitly named **TEST** until local validation is recorded.

The long-term goal remains a stable local integration that follows the native Thermia/Danfoss Online/DCM architecture rather than relying on speculative direct-register writes.
