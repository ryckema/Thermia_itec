# Thermia iTec XTR M — Write (Beta)

This folder contains the **active write-capable beta** for the tested Thermia iTec XTR M / older non-Genesis controller.

The read-only builds remain the recommended choice when control is not required. This write build actively participates in the native Thermia/Danfoss Online/DCM path and therefore transmits on the RS485 bus.

## Current write scope

Only one semantic setting is enabled:

- **Room Setpoint** — controller page `0x03E8`, register `0x03F4`, whole degrees `10..30 °C`.

No other Thermia setting is writable in this build.

The write path is based on the locally proven EXP352 flow and the user-confirmed successful EXP353 reusable-refresh test. The raw EXP352 log is archived in the research project; a detailed raw EXP353 log/YAML is not currently archived, so exact EXP353 counts/timings are not claimed here.

## Home Assistant control

Changing **Thermia Desired Room Setpoint** does not transmit anything by itself. A write is only armed when **Thermia Apply Room Setpoint** is pressed.

Useful status entities include:

- `Thermia DCM Write Status`
- `Thermia DCM Write Last Event`
- `Thermia DCM Runtime Active`
- `Thermia Last Setpoint Write Confirmed`
- `Thermia Confirmed Setpoint Writes`
- `Thermia 03E8 Refresh Requests`
- `Thermia 03E8 Refresh Confirmed`

Additional protocol diagnostics remain available but are disabled by default.

## Safety model

Before a semantic write, the firmware requires a clean retained DCM runtime. It never seeds a historical `03E8` page as write-eligible at boot. A missing or older-than-300-second page is refreshed from the controller first. The requested and current setpoints must both be whole degrees inside `10..30 °C`.

The desired-page response is constructed from the latest controller-originated `03E8/count14` page and changes only `03F4`. The controller must then republish the expected `03E8/count14` page with no extra changed words. Transactions are serialized and unknown/session-conflicting traffic is handled fail-closed.

## Known limitation

Retained-session operation is much better validated than arbitrary fresh controller power-loss/session recovery. Treat this as **Beta**, not as a universal Thermia/Danfoss implementation. If an abnormal Online/Link state appears, stop semantic testing and return to the read-only build or the last known-good research build.

## File

`thermia_itec_xtr_m_waveshare_write_beta_v1.yaml`

The file uses the same ESPHome secrets as the read-only XTR builds.