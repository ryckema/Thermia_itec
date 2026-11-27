# Thermia CM930 Universal – Experimental Beta

**Version:** 0.1.0-beta.1 (release candidate)

A universal ESPHome integration for local monitoring and control of Thermia and Danfoss heat pumps using the CM930 controller. The goal is to support multiple heat pump models and controller firmware versions through a single YAML configuration, without relying on Thermia Online.

This is a community project and is not an official Thermia product. Feedback from owners of different models is welcome.

> **Availability:** The dev012 firmware candidate is prepared but the public YAML has not yet been released. The installation instructions below apply once it becomes available. For an existing installable XTR version, use [Write User 1.1](../Thermia%20iTec%20XTR/thermia_itec_xtr_write_user_1.1.yaml).

## Compatibility

The following table describes targeted compatibility, not a list of fully supported installations. Controller firmware versions are the versions shown on the heat pump panel, not the Thermia Connect or ESPHome firmware versions.

| Heat pump family | Model variants | Explicit controller firmware mappings | Passive/profile readout | Native DCM session | Calendar / writes | Live confirmation |
| --- | --- | --- | --- | --- | --- | --- |
| iTec (legacy) | 5 kW 1N; 9 and 16 kW 1N/3N | 1.1.1, 1.2.0, 1.2.2, 2.0.0, 2.1.0 | Mapped | Not implemented | Not available | No |
| iTec | 5 kW 1N; 9 and 16 kW 1N/3N | 2.3.0, 2.3.2, 2.4.0, 2.4.1, 2.4.2, 2.4.3 | Mapped | Experimental | Not validated / not released | No |
| iTec Eco / E (legacy) | 5 kW 1N; 8, 12 and 16 kW 1N/3N | 2.0.0, 2.1.0 | Mapped | Not implemented | Not available | No |
| iTec Eco / E | 5 kW 1N; 8, 12 and 16 kW 1N/3N | 2.3.0, 2.3.2, 2.4.0, 2.4.1, 2.4.2, 2.4.3 | Mapped; Eco 5 kW 1N / 2.3.2 capture replay tested | Experimental; partial offline evidence | Not validated / not released | No |
| iTec Split | 6 kW 1N; 9 kW 1N/3N | 2.3.0, 2.3.2, 2.4.0, 2.4.1, 2.4.2, 2.4.3 | Mapped | Experimental | Not validated / not released | No |
| iTec XT | 10, 14 and 16 kW 1N/3N | 2.4.0, 2.4.1, 2.4.2, 2.4.3 | Mapped | Experimental | Not validated / not released | No |
| **iTec XTR M 3N** | **M, three-phase** | **2.4.2** | **Confirmed** | **Confirmed** | **Confirmed in development baseline** | **Yes** |
| Other iTec XTR combinations | S 1N; M 1N/3N; L and XL 1N/3N (excluding the confirmed combination above) | 2.4.2, 2.4.3 | Mapped | Experimental | Not validated / not released | No |
| Atec / Danfoss DHP-AQ | 6, 9, 11, 13, 16 and 18 kW Atec mappings | 2.2.0, 2.2.1, 3.0.0, 3.0.2, 3.0.3, 3.1.0, 3.1.1 | Mapped; capture replay tested | Experimental; offline cold-start/rejoin evidence, not live qualified | Calendar not validated; limited private write trial only | No |

**How to read the table:**

- **Mapped:** model recognition and version-aware register decoding are implemented; this does not establish that all data are available or correct on a live installation.
- **Offline tested:** tested against recorded bus traffic or host tests; not a physical validation of this firmware on that model.
- **Confirmed:** demonstrated on a live heat pump with the stated model, firmware and development build.
- The 18 explicitly mapped versions are listed above. Other versions may use a nearby mapping within the same controller family, but are not independently validated. 1N and 3N designate single-phase and three-phase model variants.
- Atec-family mappings must not be interpreted as confirmation of every Danfoss-branded variant.
- Passive readout depends on what the controller actually sends. Some information is only available after a qualified DCM session.

### Confirmed XTR reference installation

On 27 November 2026, dev011 was compiled and flashed using ESPHome 2026.9.0 on an iTec XTR M 3N / CM930 2.4.2. The saved installation choice was retained after OTA; the native session recovered automatically, controller identity was confirmed, and all four current configuration pages were synchronized. Calendar reception, alarm refresh and automatic hot-water configuration readout were observed, and existing Write User controls became ready. Actual setting changes and full calendar functionality were validated in earlier XTR development builds, not repeated in this dev011 OTA test.

Dev012 is the beta cleanup candidate: entity visibility, duplicate-sensor defaults, logging and firmware identification have been adjusted. These changes are offline-tested, not target-compiled or live-validated. A fresh controller cold-start is not guaranteed by the retained-session recovery result.

## Installation

### 1. Hardware and wiring

The reference hardware is the **Waveshare ESP32-S3-RS485-CAN**, with a separately powered USB connection and an RJ45 breakout adapter for the heat pump communication port.

Follow the [hardware, wiring and electrical checks in the main README](../README.md#hardware). The reference XTR connection uses RJ45 pin 1 (RS485 A) and pin 3 (RS485 B). Verify the pinout of your specific controller before connecting: do not assume that every model uses the same connector or pinout. The RJ45 also carries power; do not connect its power pins to the RS485 terminals. Keep the existing room sensor connected. Do not operate two native DCM responders on the same slot.

### 2. Prepare ESPHome

Once the public Universal YAML is available in this directory:

1. Back up your existing ESPHome YAML and relevant heat pump settings.
2. Copy the complete Universal YAML into ESPHome. ESPHome 2026.9.0 is the version used for the dev011 reference test.
3. Review the hardware configuration and device name. When upgrading an existing installation, retain the device name and existing network/API credentials to preserve the Home Assistant device association.
4. Add your own values to ESPHome's local `secrets.yaml`. The current candidate uses the following ordinary ESPHome secrets:

```yaml
wifi_ssid: "YOUR_WIFI_SSID"
wifi_password: "YOUR_WIFI_PASSWORD"
thermia_api_encryption_key: "YOUR_EXISTING_OR_GENERATED_API_KEY"
thermia_fallback_password: "YOUR_FALLBACK_AP_PASSWORD"
```

Use a valid ESPHome API encryption key (32 bytes encoded as Base64). Keep all credentials local. Leave any optional private provider disabled in the distributed configuration; no private authentication material is included.

### 3. Select the entity presentation

The default presentation is intended for XTR. Optional substitutions affect visibility only, not native session permissions:

| Substitution | XTR (default) | Other iTec / Eco / XT / Split | Atec |
| --- | --- | --- | --- |
| `cm930_hide_legacy_controls` | `"false"` | `"true"` | `"true"` |
| `cm930_view_hide_atec` | `"true"` | `"true"` | `"false"` |
| `cm930_view_hide_itec` | `"false"` | `"false"` | `"true"` |
| `cm930_view_disable_duplicates` | `"true"` | `"false"` | `"false"` |

These are build-time choices. Existing Home Assistant entity registry settings may override default visibility. Keep private diagnostics off for normal use.

### 4. Compile and install

Validate the YAML in ESPHome, then compile it. For a first installation, flash via USB with the RS485 connection disconnected; for an existing compatible device, use OTA. Verify the wiring before connecting the RS485 bus. Add or reconnect the device using the ESPHome integration in Home Assistant.

A fresh installation starts in passive discovery with native transmission disabled. An upgrade from a previously authorized XTR installation may restore its saved choice automatically.

## Testing

Please follow this sequence and report which steps work on your model. Passive-only results are valuable too.

| Step | What to check | Expected result |
| --- | --- | --- |
| 1. Passive readout | Compare available temperatures, compressor frequency and operating status with the panel. Check `Diagnostic \| RX Integrity`. | Valid bus traffic; plausible readings; no increasing parser resync or RX-drop counts. |
| 2. Identification | Check `Diagnostic \| CM930 Universal Identity` and compare against your model and firmware on the panel. | Correct identification when the controller has supplied the necessary information. Identity may initially be unavailable. |
| 3. Native DCM | On the confirmed XTR M 3N / 2.4.2 only, select `XTR M 3N 2.4.2 (automatic)` in `Configuration \| CM930 Native Installation` if not already selected. | Automatic session recovery; `Diagnostic \| Native Session` reports transport qualified and CURRENT fresh. |
| 4. Configuration and calendar | Check `Native DCM \| Cache Freshness` for CURRENT 4/4; check the calendar summaries and compare with the panel. | Current settings and calendar entries are received automatically on the validated profile. Calendar refresh may take longer than initial session recovery. |
| 5. Write readiness | Check `Diagnostic \| Write Readiness`. | ENABLED only after the current configuration has been confirmed on the validated profile. |
| 6. Optional write | On the validated XTR profile only, record an existing user setting, make one small supported change (e.g. heating curve by 1 °C within the permitted range), check the panel/controller feedback, then restore the original value and verify it again. | Controller-confirmed new value and restoration. A transport ACK alone is not confirmation. |

For a different or unknown model, leave native TX trial options disabled by default. Report passive readout and identity first. Native trials on additional models require a separately defined, user-initiated test with the correct model/firmware, bounded scope and rollback; do not select the XTR installation profile for another model. Do not test unsupported Service writes.

Normal session recovery does not require pressing a start button. A heat pump controller restart is different from an ESP restart and may require a new authorized session; do not deliberately power-cycle the controller just to test the beta.

## Troubleshooting

| Symptom | What to check |
| --- | --- |
| No passive values | Verify wiring, power, board configuration and whether valid frames are received. |
| Wrong or missing model | Compare the panel version and model with the compatibility table; report the discrepancy rather than forcing an unrelated profile. |
| Session not established | Check the installation choice, native session status and whether another DCM responder is present. Allow the initial recovery and synchronization to complete. |
| Calendar or settings unavailable | Check CURRENT freshness and calendar refresh status. Not all models have validated native support. |
| Missing or duplicate entities | Check the presentation substitutions and Home Assistant entity registry. |
| Unexpected bus behaviour or controller faults | Use `Configuration \| ABORT Native Session`, select `Disabled (RX only)` and restore the previous working YAML if necessary. |

## Feedback

Please post successful and unsuccessful results in [GitHub Discussions](https://github.com/ryckema/Thermia_itec/discussions), using the [beta feedback template](BETA_FEEDBACK.md).

Include the exact heat pump model, controller firmware, passive readout results, DCM session status, calendar readout, write results (if tested) and other observations. Do not share full raw captures, credentials or sensitive protocol data publicly.

## Release status and limitations

- [Changelog](CHANGELOG.md)
- [Existing XTR Write User release](../Thermia%20iTec%20XTR/thermia_itec_xtr_write_user_1.1.yaml)
- [Separate iTec Eco room-sensor beta](../Write%20(Beta)/iTec%20Eco/)

The public Universal YAML remains pending clearance of protected protocol material and OEM-derived mappings. No private authentication material, OEM archives or raw captures are distributed here. The repository MIT license does not automatically grant redistribution rights for third-party material. This documentation does not imply a public firmware release or full cross-model compatibility.
