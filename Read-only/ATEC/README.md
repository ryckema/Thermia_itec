# Thermia ATEC — read-only ESPHome

Last updated: **2026-10-02**

Use:

[`thermia_atec_waveshare_readonly_v01.yaml`](./thermia_atec_waveshare_readonly_v01.yaml)

**Status:** `ATEC READ-ONLY v01 — CANDIDATE / PASSIVE`

This build is strictly RX-only and is separate from active DCM/mailbox research in [`Research/Atec/`](../../Research/Atec/).

## Safety boundary

- RX: GPIO18
- DE: GPIO21 forced LOW
- TX: not configured
- bus: 9600 baud, 8E1
- no polling
- no FC16 ACK
- no FC03 response
- no FC17 response/replay
- no DCM emulation
- no Thermia write controls

The **Log 120 Seconds** button changes logging only and never transmits.

## 2026-10-02 passive map refresh

The two supplied gateway logs were reparsed directly. Exact controller-originated page shapes repeatedly present include:

- `03E8/count14`
- `0410/count22`
- `042E/count15`
- `0442/count13`
- `0546/count20`

Selected fields are now passively exposed where direct ATEC page evidence and stronger cross-model semantics agree. They are explicitly named **Candidate** until locally correlated on the target ATEC.

New passive candidates:

- `041D` DHW Start
- `042E` Hot Water Enabled
- `042F` Hot Water Mode
- `0433` Startup HT
- `0434` Heating Time
- `0442` Cooling Enabled
- `0443` Cooling Desired Temperature
- `0445` Cooling Active Above
- `0449` Cooling Time
- `044C` Cooling Room Sensor
- `044D/044E` Cooling Room Hysteresis
- `0553` Operation Mode
- `0559` Link Integration

The supplied ATEC/Eco `0546/count20` page repeatedly contains `0553=2` and `0559=0`. Those values are consistent with public Online/DCM semantics and later XTR findings, but remain candidates on ATEC.

## Strongest mapping

`0x03F4` / decimal 1012 remains the strongest ATEC/DHP-AQ-family semantic mapping. Genuine gateway captures show a `03E8/count14` desired-page round trip where only `03F4` changes 20→30 followed by controller republish.

This passive build only publishes a page when it actually appears. It never requests or modifies it.

## Without Online/DCM

If the native gateway is absent, some `0x0F` pages may never occur. Corresponding entities can remain unknown. That is expected for a passive build.

Do not add active replies to this file to make data appear; active emulation belongs in `Research/Atec/`.

## Capture workflow

Open ESPHome logs and press **Log 120 Seconds**. Return the complete:

```text
ATEC-CAPTURE START
...
ATEC-CAPTURE END
```

## Active ATEC research

- [ATEC README](../../Research/Atec/README.md)
- [ATEC AI handover](../../Research/Atec/AI_HANDOVER.md)
- [ATEC-EXP1 YAML](../../Research/Atec/thermia_atec_waveshare_atec_exp1_queued_room_setpoint.yaml)

ATEC-EXP1 remains **PREPARED / NOT RUN**.

## Validation

Static RX-only checks performed for this update:

- no configured `tx_pin:`
- no UART `write_array()`
- no DE `turn_on()`
- DE `restore_mode: ALWAYS_OFF`
- RX remains GPIO18

No ESPHome compile verification is claimed.
