# Thermia iTec XTR M — RX-only monitoring (v31 FIX4)

**Status: RUNNING / PARTIAL (user-confirmed first FIX4 live observation, 2026-10-18).** User confirms FIX4 is flashed: `Thermia ESP Reset Reason = Reboot request from esphome.ota`, ESP uptime 151 s, `Native Settings Pages Seen = 03E8:Y` with all other 12 families N, and `Cooling Settings Page Source = 0442 NOT received since ESP boot`. The heating curve and direct outdoor-unit sensors report plausible running/idle values while 34 native dependent settings are Unknown. This validates the on-device presence of the diagnostic, **not** that all passive data or native service pages are available, nor electrical TX inactivity. The previous V5DCM19 FIX1 remains the better independently evidenced long-soak fallback.

This directory deliberately contains **exactly two files**:
- [`thermia_itec_xtr_m_read_only.yaml`](thermia_itec_xtr_m_read_only.yaml) — the single consolidated v31 candidate, 258 named ESPHome/HA entities.
- This `README.md` — usage, scope, safety and limitations.

## Model and safety

Target Thermia iTec XTR M (legacy Danfoss DHP-AQ), Waveshare ESP32-S3-RS485-CAN / CAN-U, ESPHome + Home Assistant. Native bus: Modbus RTU **9600 8E1**, receiver GPIO18, driver-enable GPIO21 always LOW (`restore_mode: ALWAYS_OFF`); **no UART TX pin or unsolicited bus transmission**. The RS485 transceiver's TX function is deliberately not configured.

Existing production YAML, entities, bus CRC/frame bookkeeping and fixed v29 temperature/status interpretation were retained as far as the source-only audit permits. Core native 0x0F pages are passively decoded from *controller-originated* traffic; their presence and exact cadence on this individual device are not guaranteed by firmware extraction.

ESPHome secrets must be supplied locally: `wifi_ssid`, `wifi_password`, `thermia_api_encryption_key`, `thermia_ota_password`, `thermia_fallback_password`. **Never commit actual secrets.**

## Other Unknowns: native page coverage (FIX4)

FIX4 adds **one** compact, default-enabled source-diagnostic entity: `Native Settings Pages Seen`. It reports which of thirteen relevant full controller-originated `0x0F FC16` pages were **received since the current ESP boot**. Example before any pages arrive:

```text
03E8:N 03FC:N 0410:N 042E:N 0442:N 0532:N 0546:N 07D0:N 080C:N 0820:N 0848:N 0864:N 0870:N
```

`Y` = full page reached the existing valid decoder geometry; `N` = not seen **since this ESP boot**. N is *not proof of a decoding bug*, and Y is *not proof that every field's scaling/semantics are correct*. The flags do not report page age, do not trigger polling and do not retain previous boots.

| Page | Representative HA values requiring that native page |
|---|---|
| `03E8` | Heating curve, heating min/max, room-setpoint mirror |
| `03FC` | Additional heating circuit 1 settings (when installed) |
| `0410` | DHW start and max production time, anti-legionella service values |
| `042E` | Hot Water Enabled/Mode, Startup HT, Heating Time |
| `0442` | Cooling Enabled, cooling targets and room hysteresis |
| `0532` | Installed flags: Pool, Distribution Circuit 1/2, Buffer Tank |
| `0546` | Controller Operation Mode |
| `07D0` | Hydraulics, auxiliary output states and tank runtime |
| `080C` | Native room / cooling / pool / circuit 2 raw temperatures |
| `0820` | Native outdoor status bits and Defrost Active |
| `0848` | Supply Temperature Wanted, Weighted DHW Temperature |
| `0864` | DHW Top-up Active, defrost-source statuses and Outdoor Stop Active |
| `0870` | Defrost Count, Previous Defrost Interval, Time Since Last Defrost |

In the earlier October 18 Home Assistant PDF, **33 visible values** show `Unknown`; the newer full-name list establishes **34 distinct Unknown entities** while direct outdoor measurements are populated. This is not proof that every Unknown is caused by missing native pages. `Unknown` can also be an unrecognized enum, filtered out-of-range/sentinel raw value, a missing direct source, or a newly restarted ESP which has not observed its next controller settings page.

**Live result RUNNING / PARTIAL:** User explicitly confirms FIX4 flash and supplies its 151 s HA observation. Only `03E8` is Y; all other 12 monitored native pages are N, meaning no matching CRC-validated full-page decoder branch has been seen **in this ESP boot window**. N does not prove the controller never transmits the page, nor that a differently shaped frame would not exist. No independent ESPHome build logs, raw bus frame audit, or electrical TX measurements were reviewed; do not mark COMPLETE yet. The earlier PDF predated FIX4.

## Koeling: missing-page diagnostics (FIX3)

The cooling settings are read from a **complete controller-originated 0x0F FC16 0442/count13** page, which is *not* guaranteed to be broadcast again after an ESP restart when no genuine Online/DCM module is present. For example, `Cooling Enabled` might be `Unknown` even while `Cooling Active` reports correctly `Off` during heating: these describe configuration and real-time operation from **different physical data sources**.

FIX3 adds exactly **seven** HA entities, without changing any existing names:
- `Cooling Settings Page Source` (diagnostic, enabled): `0442 NOT received since ESP boot` until a full native page is captured, then `0442 received since ESP boot`. This witness records *receipt only*, not value correctness or page freshness.
- Six **RAW signed word** diagnostic sensors, **disabled by default**: `Cooling Hysteresis Raw 0444`, `Cooling Configuration Raw 0446`, `Cooling Start Threshold Raw 0447`, `Cooling Stop Threshold Raw 0448`, `Cooling Maximum Start Temperature Raw 044A` and `Cooling Minimum Stop Temperature Raw 044B`. They publish only when that same full page arrives; no invented scale, engineering unit, profile interpretation or polling. Earlier XTR EXP382 supports all named meanings other than 0447, which remains *hypothesis only*.

If the page source says **NOT received**, the solution is **not** to fabricate values or to assume cooling is disabled; it needs a passive full-frame capture and analysis of why the controller did not publish the page. RX-only firmware intentionally cannot request native settings on demand. When the page source says **received** but a setting stays Unknown, inspect the register word/range filter in the decoder using a short CRC-valid capture. The initial full cooling-page source status does not require any external DCM.

**FIX3 source-only audit status was PREPARED / NOT RUN when written.** Subsequently the user explicitly flashed FIX4 and reported `0442 NOT received since ESP boot` with 151 s uptime. The cooling raw-word labels remain unproven and the known-good V5 historical reference is unchanged.

## Optional hardware: conditional states (v31 FIX4)

The passive native capability page `0x0F FC16 0532/count18` contains firmware-derived bits:

| Feature in Thermia UI | Native candidate | HA capability entity | Other HA entities |
|---|---|---|---|
| Zwembad / pool | 0x0533 | `Pool Installed` | Pool Start/Stop Raw, Pool Temperature Raw, Pool Heating Active, Pool Demand Queued |
| Shuntgroep 1 / 2nd heating circuit | 0x0534 | `Distribution Circuit 1 Installed` | Circuit 1 curve, min/max/corrections, hydraulic temperature, target |
| Shuntgroep 2 / 3rd heating circuit | 0x0535 | `Distribution Circuit 2 Installed` | Circuit 2 curve, min/max/corrections, raw temperature, target |
| Buffertank / buffer tank | 0x0536 | `Buffer Tank Installed` | Buffer Tank Temperature, Tank Temperature and wanted tank temperatures |

**Policy:**
- At boot, absence of a 0532 page means **unknown**, not `OFF`.
- Only a correctly received native page with the relevant flag exactly `1` permits interpreted optional measurements and states to publish. Flag `0`, invalid values, or page age beyond **6 hours** suppress those values. The 6-hour age threshold is a **provisional safety policy**, not locally measured 0532 broadcast frequency; verify with passive capture before production adoption.
- Optional numeric entities become invalid/unavailable (`NAN`) when gated; optional pool activity/demand binaries invalidate their state rather than inventing `OFF`.
- Raw diagnostic register readings (041B/041C/080D/080F, etc.) remain *deliberately independent* as source evidence, but are **disabled by default in HA**. They are not confirmed physical temperatures or status readings.
- Capability flags themselves remain HA enabled and lose valid state on expiry. **No live hardware validation of this gating has been performed.**

### Home Assistant visibility limitation

ESPHome's `disabled_by_default: true` is a **static first-registration default**, not a dynamic enable/disable based on the native capability flag. It cannot automatically turn a disabled HA entity on when a pool/shunt/buffer is later installed. Where you **do** have optional hardware, manually enable the desired related disabled entities in HA once (Settings → Devices & Services → ESPHome → Thermia → Entities).

Use conditional Lovelace cards to show them only while the installed flag reports ON; replace example IDs with **actual** IDs assigned by HA:

```yaml
type: conditional
conditions:
  - condition: state
    entity: binary_sensor.thermia_itec_pool_installed  # Replace with actual entity ID
    state: "on"
card:
  type: entities
  title: Zwembad
  entities:
    - binary_sensor.thermia_itec_pool_heating_active   # Enable manually if HA-disabled
    - binary_sensor.thermia_itec_pool_demand_queued     # Enable manually if HA-disabled
```

Repeat the same pattern for `Distribution Circuit 1 Installed`, `Distribution Circuit 2 Installed`, and `Buffer Tank Installed`. The dashboard visibility hides groups automatically when the flag is OFF or unavailable; it **does not edit the HA entity registry**. Before a 0532 page has ever arrived, no optional card should appear.

## What is included / excluded

- **258 source-defined entities:** 187 numeric sensors, 60 binary sensors and 11 text sensors. They are NOT 258 different on-device-proven native registers.
- Regular heating, hot water, cooling, compressor and outdoor-unit data; added native runtime registers; defrost counters and passive bus diagnostics.
- Optional pool/circuit/buffer measurements and features, fail-closed as above; raw register diagnostics disabled by default.
- **Excluded:** calendar/schedules, alarms and fault entity publishing, speculative model-inapplicable interpretations, live parameter writes, service test controls, DCM handshake/response emulation.
- Firmware registry list: 524 `xtr_m_cm_2_4_2=YES` rows in `Thermia_Connect_Firmware/parameters/ALL_PARAMETERS_ACCESS_MATRIX.csv`, **not all confirmed available on passive XTR frames**. Expanding and proving full parameter coverage remains outstanding.

## Validation / installation order

1. Keep working V5DCM19 FIX1 or validated v29 production firmware available as rollback.
2. The user has flashed FIX4, showing a working device and ESPHome OTA reboot; no independent YAML parse/compiler output or reproducible build signature was audited here. Run `esphome config` / compile **locally** only if diagnosing a concrete issue, using local secrets. Do not infer full compilation test coverage from the OTA alone.
3. **Current FIX4 passive test is RUNNING / PARTIAL** on the basis of the user's first 151 s HA snapshot. Next check the same diagnostic after a longer uninterrupted interval (no OTA restart) and, only if available, narrow CRC-valid native RX evidence. No device TX request is necessary for diagnosis; electrical DE/TX has not been independently measured. Mark the overall test COMPLETE only after reviewing the final user results and relevant abort criteria.
4. If bus health or baseline measurements regress, recover the previously tested version.

## Provenance and archives

The exact **pre-consolidation directory tree**, including old v26–v29 YAML builds, previous v31 YAML and six documentation files, is preserved at
[`Research/Archive/Read-only_XTR_before_FIX2`](../../Research/Archive/Read-only_XTR_before_FIX2).
This is a move by Git subtree object: no prior content or old version is destroyed. Earlier SHA histories remain available.

Detailed research and source audit now live in `Research`, including `THERMIA_PROJECT_STATE.md`, `EXPERIMENT_LOG.md` and `PROTOCOL_FINDINGS.md`. Native Online/DCM emulation research is separate and **not deployed by this read-only build**.
