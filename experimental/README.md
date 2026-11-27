# Thermia CM930 Universal — experimental beta

**Planned version: 0.1.0-beta.1. Status: firmware candidate prepared; public firmware not yet available.**

Community ESPHome integration for local monitoring and supported user-level control of Thermia/Danfoss CM930 heat pumps through Home Assistant. Not an official Thermia product. The Universal track is separate from the existing supported XTR release and the separate iTec Eco beta.

For an installable existing XTR release, see [Write User 1.1](../Thermia%20iTec%20XTR/thermia_itec_xtr_write_user_1.1.yaml). For the existing Eco experiment, see [iTec Eco](../Write%20(Beta)/iTec%20Eco/).

## Compatibility and evidence

| Controller / family | Profile recognition and decoding | Native session / control |
|---|---|---|
| iTec XTR M 3N, CM930 2.4.2 | Locally observed | Automatic retained-session recovery and current configuration synchronization locally verified on dev011 |
| Other XTR, XT, Eco / E and Split models | Implemented version-aware mappings; coverage varies | Experimental; not locally verified |
| Atec / Danfoss DHP-AQ | Implemented version-aware mappings; coverage varies | Experimental; not locally verified |
| Older iTec | Discovery and mapped read-only observations where available | No validated native session support |
| Unknown controller | Passive discovery | No native transmission by default |

The owner tested dev011 on 27 November 2026 using ESPHome 2026.9.0. The OTA recovery restored a previously authorized XTR installation, confirmed the observed controller identity, synchronized four current configuration pages and restored existing user-control readiness automatically. Alarm refresh and an automatic hot-water configuration read also completed. No setting change was performed in this test. The complete service refresh had been demonstrated on the earlier dev010; the dev011 capture ended before all service pages were received.

The dev012 candidate changes entity presentation, logging and build identification. It is offline-tested only, not target-compiled or live-validated. The owner has elected not to repeat the existing live recovery experiment.

## Intended beta behaviour

- One-time installation selection, persisted across ESP reboot and OTA, on the validated XTR profile.
- Automatic retained-session recovery, configuration synchronization and read refresh without routine session-start buttons.
- No automatic parameter writes by default. Deliberately initiated user-level controls remain subject to fresh controller feedback.
- Unknown models remain in discovery. Other models are not automatically granted experimental native control.
- Preserve the existing abort, disable and rollback controls.
- Model-specific entity presentation and duplicate-sensor defaults are build-time choices; existing Home Assistant entity registry settings may override them.

A controller power cycle is different from an ESP reboot. The demonstrated recovery does not guarantee a fresh native session after a controller restart. Transport qualification is not proof of cloud connectivity or a successful setting change. Optional or unsupported values may be unavailable.

## Distribution status

The public release is not yet installable from this directory. The private candidate contains protected protocol material and OEM-derived mappings whose redistribution has not been cleared. No firmware, private authentication material, OEM archives or raw captures are included here. The repository MIT license covers original project contributions, not automatically third-party materials.

Public firmware distribution requires a cleared source candidate. Until then, keep using the existing firmware appropriate to your installation.

See [development history](CHANGELOG.md) and [beta feedback guidance](BETA_FEEDBACK.md).
