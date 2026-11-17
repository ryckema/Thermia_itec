# Thermia iTec XTR — Firmware Changelog

This file records the public **Passive** firmware development from 1.0 through 1.3. The other public XTR firmware variants have separate functionality and version numbers; Passive 1.3 is **not** an upgrade to DCM Read Only or Write User.

For the latest firmware and setup instructions, see the [main README](../README.md). All entries below describe source changes and the verification available at the time, **not a guarantee of compilation or live operation on another Thermia controller**.

## Passive 1.3 — 2026-11-17

**Firmware:** [`thermia_itec_xtr_passive_1.3.yaml`](thermia_itec_xtr_passive_1.3.yaml)

### Fixed
- Removed five duplicated `disabled_by_default` YAML keys that prevented strict configuration parsing.

### Improved
- Reduced transient receive-parser allocations by reusing the frame buffer and using a fixed-size frame-length table; preserved the RX-only UART, CRC checks, bus-health tracking and existing Home Assistant identities.
- Exposed the `0x0848` heat-demand value as a **raw, freshness-checked** diagnostic. Its precise PID/integral semantics are not yet verified on the local XTR; it is not assigned a fabricated unit or interpreted setpoint.

### Added
- ESP32 memory diagnostics: minimum free heap, largest contiguous free heap block, heap fragmentation and free PSRAM, in addition to existing free-heap monitoring.

### Verification
- SOURCE / OFFLINE TESTED: strict YAML key/structure checks, alarm-formula consistency and receive-parser comparison on captured traffic (2,476 valid frames decoded identically).
- Full ESPHome target compilation and live device behaviour were **not** established by these offline checks.
- No TX pin, active reads, alarm acknowledgement or parameter writes added.

## Passive 1.2 — 2026-11-17

### Added
- Source-specific telemetry freshness so expired controller/outdoor-unit measurements become unavailable rather than silently retaining stale live values.
- Home Assistant source/data-quality diagnostics to distinguish live and partial/unavailable telemetry.
- Explicit distinction between restored/cached heating settings and fresh runtime observations.

### Refined
- Remaining internal operating-mode text translated into English and diagnostic presentation cleaned up.
- Kept existing Home Assistant entity IDs, the alarm decoder and receive-only behaviour.

## Passive 1.1 — 2026-11-17

### Added
- **30 OEM-profile-backed active-alarm predicates**: 29 based on the current alarm status registers `0x085F–0x0861`, and one outdoor-unit flag from `0x082F`. Optional/conditional predicates depend on their relevant source configuration fields.
- Per-alarm Home Assistant sensors, aggregate alarm presentation and an alarm-data availability indication.
- Passive decoding of controller-origin `0x0884/60` alarm-history pages, distinguishing legacy 10 × 6-word and newer 8 × 7-word record layouts when the received content permits. Raw history identifiers are **not** automatically mapped to current-alarm bits or UI E-codes.
- Passive controller clock decoding from controller-origin `0x06EA/7` when received.

### Corrected
- Defrost field labels from `0x087B` (count), `0x087C` (minutes since previous defrost) and `0x087D` (previous duration in minutes), with invalid values left unavailable.

### Data-availability limitation
- Current-alarm `0x085F/5` frames have been observed on the local XTR bus with an existing DCM/Online communication peer. An RX-only ESP cannot force a missing alarm page to appear. Stale or never-seen alarm source pages remain unavailable; absence of data is **not** proof of zero alarms.
- OEM alarm definitions are source-backed; individual real-fault semantics have not been validated for every alarm on the local XTR.

## Passive 1.0 — earlier public baseline

- Initial public XTR receive-only ESPHome YAML, using one RS485 receiver, Modbus RTU-style CRC validation, passive temperature/operating telemetry, selected settings caching and Home Assistant entities.
- Baseline preserved as the starting point for Passive 1.1–1.3. Release date not asserted here.

## Other currently published XTR firmware variants

- [DCM Read Only 1.0](thermia_itec_xtr_DCM_readonly_1.0.yaml) — native DCM read-only integration; unlike Passive, it can transmit protocol traffic but does not make parameter changes.
- [Write User 1.01](thermia_itec_xtr_write_user_1.01.yaml) — public native user-setting control variant. It has different controller/session requirements and should not be confused with RX-only Passive.

**Scope:** No private handshake algorithms, keys, authenticated captures or controller secrets are included in this public changelog.
