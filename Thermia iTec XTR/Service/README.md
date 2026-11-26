> [!WARNING]
> **EXPERT USERS ONLY.** This firmware provides access to installer-level heat pump settings. Incorrect settings or improper use can damage the heat pump and other components of the heating system, cause unsafe operating conditions, or affect warranty coverage. Use only if you understand the Thermia service parameters and the installation. Always retain a backup of your original settings and firmware. Use at your own risk.

# Thermia iTec XTR — Service PUBLIC 1.0

Service is the advanced single-file ESPHome firmware for local monitoring and control of the Thermia iTec XTR via Home Assistant. It extends Write User with installer-level configuration and additional read-only service information.

## Features

- Native local DCM communication, automatic session recovery and periodic parameter refresh.
- Heating, cooling, domestic hot water, operating mode and calendar controls.
- 36 historically validated Service settings covering heating, hot water, cooling, circulation pump (Optimum), defrost, auxiliary heating, sensor correction and logging.
- 13 additional candidate settings are read-only; installation topology writes are blocked.
- Live operating data, controller counters, alarm status and alarm history, compressor and defrost statistics.
- Streamlined Home Assistant entities and optional troubleshooting diagnostics.
- Native heat pump clock reading and automatic daily clock correction (enabled by default in Service; can be switched off).

## Compatibility

Locally tested on the iTec XTR M 3N with CM930 controller version 2.4.2. RC04.2, the release baseline, was compiled and flashed successfully on ESP32-S3 with ESPHome 2026.9.0. Retained-session recovery, parameter refresh, heating curve and heating startup time writes were demonstrated; the owner also confirmed cold start. A calendar deletion was accepted by the controller. These results do not establish compatibility with other models or controller firmware versions. The release changes the build identification only, not the operating code. The exact renamed release has not been separately flashed.

The public cold-start implementation supports only the existing known exchange; an unknown exchange is not supported. Do not operate a genuine DCM gateway and this emulation simultaneously on the same bus.

## Installation

1. Use `Service-PUBLIC-1.0.yaml` as a standalone ESPHome configuration. Keep a working firmware backup.
2. Check the device name, board, UART and RS485 pin assignments against your hardware. Preserve existing device substitutions when upgrading.
3. Supply your own `secrets.yaml` with `wifi_ssid`, `wifi_password`, `thermia_api_encryption_key` and `thermia_fallback_password`. Do not publish these secrets.
4. Compile and install with ESPHome, then connect the device to Home Assistant.
5. Check `Diagnostic | Native Session`, `Diagnostic | Bus Healthy` and `Service ⁄ Parameters Status`. Wait for a qualified session and fresh settings (17/17 Service pages) before editing.

## How to enable Service writes

Service write permission is **OFF after every ESP restart**.

1. In Home Assistant, open **Settings → Devices & services → ESPHome → your Thermia device**.
2. Confirm that the native session is qualified, the bus is healthy and the required Service parameters are fresh. If ordinary Write User control has been explicitly disabled, use `Configuration | Enable Write User (Validated Controls)` to re-enable it once the session is ready.
3. Under **Configuration**, turn on **`Configuration | Service | Enable Service Writes`**. This grants permission for the current session; switching it on does not itself write a setting.
4. Record the original value and change only the required, applicable Service setting. Wait for the controller-confirmed result in `Diagnostic | Service | Write Status` and verify the actual readback. A transmitted frame or transport ACK alone is not proof of acceptance.
5. When finished, turn off **Enable Service Writes**. If an edit fails, the session is lost or unexpected behaviour occurs, press **`Configuration | Service | ABORT Service Write`**. This revokes Service permission and stops further Service setting transmissions; it does not undo a change already accepted by the controller. Check and, if necessary, restore the original value using the Thermia panel.

Do not bypass a denied write, a range check or an installation-dependent safeguard. Not every available parameter applies to every installation. Routine Service writes should only be enabled when needed.

## Notes

- Existing Home Assistant entity registry settings may override firmware defaults. Review renamed or removed entities and disable optional diagnostics as needed.
- Pump command is a percentage, not measured speed or water flow.
- Historical alarm codes without verified names remain numeric; active alarm status is based on the qualified, mapped alarm data.
- Observation-based daily statistics cover the available observation period, not necessarily a complete day. Candidate defrost counters remain unverified.
- Private energy/COP, refrigerant and hydraulic/electrical calibration models are not included.
- See the repository's [MIT license](../../LICENSE). This release is community-developed and not an official Thermia product; the source provenance review is not exhaustive.
