# V5DCM22-RX33-01 — FIX1: Home Assistant statistics metadata

**Date:** 2026-10-18  
**Status:** PREPARED / NOT RUN (source-only correction; new YAML not compiled, flashed or evaluated in HA).

## User evidence
Home Assistant reported: `sensor.zolder_thermia_itec_xtr_m_heating_minimum` previously had long-term statistics but currently no supported `state_class`, and offered **permanent deletion of past statistics**. User reports additional errors of the same general kind; no exact additional messages yet supplied.

**Immediate data-preservation instruction:** **Do NOT delete existing long-term statistics**. A future validated ESPHome OTA carrying `state_class: measurement` may restore new statistics generation without discarding historical records; HA may take subsequent recording/statistics intervals to refresh.

## Root cause verified from exact YAML
`Heating Minimum` has existing ID `thermia_heating_min`, `unit_of_measurement: "°C"`, `device_class: temperature`, but lacks `state_class` in **both**:
- production source `Read-only/Thermia itec XTR/thermia_itec_xtr_m_read_only.yaml` blob `f4b90fcd3d96cb728ba4726409bacd9d5c23b5f3` (user-confirmed FIX4 flash), and
- first RX33 candidate `Research/V5DCM/V5DCM22_RX33_ONLY_PREPARED_20261018.yaml` blob `9c906e116a22fe9800093b7d5c3be80bfad4dc7c`.

Therefore absence predates the RX33 monitoring experiment; this is **sensor metadata**, not a native bus/page or physical control issue. Source cannot conclusively establish which firmware is presently running or what previously supplied the entity's statistics class.

## One controlled correction
New separate full YAML `Research/V5DCM/V5DCM22_RX33_STATCLASS_FIX1_PREPARED_20261018.yaml` — **do not overwrite the user-flashed production FIX4 yet**.

In the `sensor:` definitions, added exactly **40** `state_class: measurement` fields for numeric HA sensors already exposing appropriate physical units `°C`, `min`, `h` or `d` and missing a state class. Includes all **21 missing `device_class: temperature` sensors** such as Heating Minimum, Heating Maximum, Room Setpoint, Heating Stop and native cooling/heating setpoints, plus **19** similarly missing typed-unit temperature-correction/time/hysteresis sensors.

No existing device class, unit, ID, name, availability, lambda, UART, global, bus-health bookkeeping, direct 0x1E telemetry, 33-page monitor, entity count, experimental TX or native handshake changed.

**Precisely verified offline:** removing only the added YAML header and the 40 `state_class: measurement` lines from FIX1 produces byte-identical original RX33 candidate (5708 previous source lines), IDs in original order unchanged, and all 40 inserted lines directly follow pre-existing `device_class` or `unit_of_measurement`. 34 pre-existing state classes preserved; candidate now 74 `measurement` declarations. Explicit TX pin still absent and DE remains `ALWAYS_OFF`. Source diff is exactly those 40 metadata lines.

## Controlled live test criteria (not yet executed)
- **Target/address/register/payload:** HA/ESPHome metadata only; no Thermia slave, native register, TX frame or outgoing payload. TX ceiling 0; no requests or responses.
- **Known-good baseline:** user-flashed v31 FIX4 RX-only; earlier V5 passive build as historical recovery baseline if necessary.
- **Positive:** after user-chosen ESPHome validation and OTA, HA entity ID remains `sensor.zolder_thermia_itec_xtr_m_heating_minimum`, HA Developer Tools States reports `state_class: measurement`, unit °C and temperature device class unchanged; existing historical statistics retained, stats warning resolves after HA processing; same other affected entities behave consistently; original bus/HA entities remain healthy.
- **Negative:** ID or unit changes, type incompatibility, entity unavailable, unintended TX, temperature/bus regression, HA metadata issue persists despite a confirmed OTA and stable observation.
- **Inconclusive:** candidate not flashed, HA has not refreshed attributes or stats scheduler, other warnings refer to distinct unsupported types.
- **Abort/rollback:** stop on any bus/HA regression or observed TX; restore previously user-tested v31 FIX4, do not erase historical HA statistics or Home Assistant database.
- **Smallest follow-up evidence:** one HA entity's **Developer Tools → States** attributes (`state_class`, `device_class`, `unit_of_measurement`) after optional new flash and one remaining actual statistics warning, if any.

This correction does not advance or complete native Online/DCM emulation by itself. RX33-01 remains PREPARED / NOT RUN until the user confirms execution.
