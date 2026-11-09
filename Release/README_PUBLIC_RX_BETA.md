# Thermia iTec XTR M — Public RX Monitoring Beta

**Source artifact:** [thermia_itec_xtr_public_rx_alarm_beta.yaml](thermia_itec_xtr_public_rx_alarm_beta.yaml)  
**Status:** SOURCE / OFFLINE STRUCTURE CHECKED, **NOT TARGET COMPILED OR FLASHED**.  
**Scope:** **read-only receiver**. This is **not** a public Write User firmware release.

## What this actually does

- Uses only the repository's existing public ESPHome RX-only V5/CRC parser. GPIO18 receives Thermia RS485 at 9600 8E1; GPIO21 RS485 DE is boot-off; there is no configured UART TX pin.
- Preserves existing temperature, compressor, heating, hot-water and controller telemetry **when those frames are passively present**.
- Adds `Alarms | Mapped Alarm Status`, `Alarms | Alarm Flags (Passive Raw)` and `Diagnostic | Passive Alarm Source`. If a genuine CRC-valid slave0F FC16 085F/count5 frame is seen, all five raw words are shown. Five zero words mean **only** that this mapped alarm page is clear. Nonzero flags prompt checking the OEM panel; unsupported bit descriptions are not invented.
- An alarm page older than 300s, or loss of valid bus traffic for >10s, reports STALE rather than falsely reporting clear. The logger reports the build scope as `PUBLIC RX ONLY`.
- **Does not request page 085F** and does not create a native session. On many installations the alarm page will remain UNKNOWN; this is correct for a passive receiver.

## Requirements

Waveshare ESP32-S3-RS485-CAN(-U), supported iTec XTR controller and ESPHome 2026.9.0-style configuration. Wire Thermia A/B only to verified RS485 A/B; power ESP32 over USB. Use exactly one device connected according to the wiring manual. The ESP has no transmit pin configured here.

Populate these keys in the local ESPHome `secrets.yaml` (values are created and held by the installer): `wifi_ssid`, `wifi_password`, `thermia_api_encryption_key`, `thermia_ota_password`, `thermia_fallback_password`.

## Build and install

Use a **new ESPHome device configuration** named `thermia-xtr-public-rx`; do not overwrite an existing working RC09FC configuration. Download the YAML file above and use:

```bash
esphome config thermia_itec_xtr_public_rx_alarm_beta.yaml
esphome compile thermia_itec_xtr_public_rx_alarm_beta.yaml
```

The owner may flash this receiver to a separate supported ESP board through the normal ESPHome USB/OTA workflow. This candidate has not yet been target compiled or field tested; do not call it production tested.

Expected observations: valid frames increase; passive sensors reflect received frames; `Alarms | ...` begins UNKNOWN, transitions FRESH **only when an independently initiated 085F/5 controller frame appears**, and expires after five minutes without a new frame. Never promise automatic alarm polling. Bus RX CRC error, parser or Wi-Fi status should be inspected through existing diagnostics.

## ABORT and rollback

As this build has **no configured UART TX**, there are no new physical setting commands to abort. If sensor output behaves incorrectly, disable the ESP's power or disconnect its A/B wiring, and restore the previous YAML on that ESP. Reflashing a different YAML will not undo settings changed previously by a separate gateway. The private RC09FC installation and its archived RC09FB rollback remain unchanged; they are **not bundled here**.

## Why Write User is not in this public source

The private owner-live RC09FC requires an authenticated native session and an exact single TX owner. The historical publicly available **R1** implementation is one recorded full-challenge/full-response replay, **not** a universal key or independent authentication. Republishing those captured bytes, private session emulation or a guessed response is not a valid public Write User implementation. Native read-only transport alone also does not prove controller acceptance of parameter writes.

Until a separately licensed, independently implementable owner/session engine exists and can be compiled and live validated under the same controls, **public Write User remains NO-GO**. See [WRITE_USER_PUBLIC_BETA_GATE.md](WRITE_USER_PUBLIC_BETA_GATE.md).

## Provenance and scope

Derived from already public RX-only file `Thermia iTec XTR/thermia_itec_xtr_passive_1.0.yaml` (blob `6a16eae17ea5e4dc8e82d1dc013e8c91b41fb22b`), with one new passive 085F/5 decoding branch, two non-persistent alarm globals, four textual diagnostics and stale-cache checks. Existing RX/CRC, HA entity IDs, UART and hardware controls were retained. The candidate is independently **source/offline checked** for one UART, zero UART send calls, absent TX pin and no captured private challenge pair.

This beta is not an OEM product; do not generalize private owner-live write test results to this RX-only public build.
