# Thermia iTec XTR — Firmware Changelog

This file records the public iTec XTR firmware release history. Passive, DCM Read Only and Write User have separate functionality and version numbers; Passive 1.1 is **not** an upgrade to either active variant.

For the current firmware and installation instructions, see the [main README](../README.md). Entries describe source changes and the verification available at the time; they are **not** a guarantee of full ESPHome compilation or live behaviour on another Thermia controller.
# Write version
## Write User 1.04 — 2026-11-24

**Firmware:** [`thermia_itec_xtr_write_user_1.04.yaml`](thermia_itec_xtr_write_user_1.04.yaml)

### Added and improved

- Improved recognition of valid short/long FC16 page geometries (`0492/9 or 11`, `051E/9 or 10`) and retained-session qualification. Existing public known-challenge cold start, single native TX owner, CRC/parser, epoch/freshness guards, ABORT and established user controls are retained.
- Persistent automatic extended read-only refresh, enabled by default, without the RC trial expiry. The locally qualified XTR M 3N / CM930 2.4.2 profile retrieves 17 configuration pages / 278 words plus the native RTC. Requests use the existing native owner. Other CM930 2.4.0–2.4.3 profiles retain their previous access range; expanded reads are not field-qualified there.
- Periodic alarm read becomes due at 240 seconds rather than waiting until the 300-second cache expiry.
- Native clock display, Home Assistant time and clock-difference diagnostics. Separate `Configuration | Automatic Time Sync` switch, persistent OFF by default. Explicit opt-in enables comparison on activation and daily thereafter; only drift above 60 seconds can trigger one correction attempt per 24 hours, with native readback and no automatic retry on failure. Requires extended refresh and qualified fresh controller data. Effective automatic correction is not yet live confirmed in this public build.
- Native weekly calendar start/end time fields connected to the established FAMILY03 write route; old hour/minute controls remain. No new date-range/create/delete write semantics claimed.
- Additional read-only numeric Service parameters and English names/status texts. Advanced Optimum, calibration and installation diagnostics are disabled by default where appropriate; uncertain mappings retain candidate labels. The 24 existing raw register diagnostics remain available but disabled by default; 14 new page dumps are internal. Normal user controls and their names are unchanged. Existing Home Assistant registry settings may override default visibility; renamed read-only entities may need dashboard updates.
- No new service-level writes, private dynamic handshake or proprietary authentication material included.


The superseded 1.03 YAML is removed from the current tree; the original remains in [Git history](https://github.com/ryckema/Thermia_itec/blob/7048dc7d8086c077c96214ad626ed03953d8e233/Thermia%20iTec%20XTR/thermia_itec_xtr_write_user_1.03.yaml) for rollback.

## Write User 1.03 — 2026-11-22

**Firmware (historical):** [`thermia_itec_xtr_write_user_1.03.yaml`](https://github.com/ryckema/Thermia_itec/blob/7048dc7d8086c077c96214ad626ed03953d8e233/Thermia%20iTec%20XTR/thermia_itec_xtr_write_user_1.03.yaml)

- Built from the public Write User 1.02 source through FAMILY02/FAMILY03, preserving the existing S92 sole UART/RX/TX/DE owner, V5 CRC parser, native FC16/FC03, session epoch and freshness guards, controller-confirmed user writes, ABORT and rollback behavior.
- **CM930 software 2.4.0, 2.4.1, 2.4.2 and 2.4.3:** allow the existing native session/refresh/write-gate paths for this controller family. **Only local XTR M 3N / CM930 2.4.2 is live-confirmed**; the other versions are enabled by user decision, not separately field-validated. An unmatched recorded authentication challenge remains a compatibility limit.
- **Automatic native session recovery:** no Home Assistant enable toggle required after ESP reboot; retained W2R33 and native M3/CURRENT recovery reuse existing bounded S92 owner paths, with existing bus/epoch/ABORT checks.
- **Calendar F1 Apply repaired:** reconnect the common calendar editor to existing guarded W2R56 → OEMW23 → S92; bounded explicit edits require fresh source and controller FC16 acceptance, followed by exact native F1 readback. No separate TX writer.
- Removed two unreferenced RAM variables; retained dependent internal legacy/test functions and established protections.
- **XT model identification (2026-11-22):** decode OEM CM930 `0x0539` product codes 15–20 as iTec XT 10/14/16, 1N/3N, in both Home Assistant identity and controller-profile diagnostics; keep XTR M 22/23 restricted to 2.4.2+ profile maps. Display-only change: handshake, session engine, register access and physical TX unchanged. **SOURCE / not separately target compiled or XT LIVE-tested**.

**LIVE evidence — 2026-11-22, local XTR M 3N, CM930 2.4.2:** ESP OTA reboot followed by retained native session rejoin, M6=5 and controller-confirmed CURRENT 4/4; Write User automatically ENABLED. On one explicit calendar apply, slot 4 stop minute **38→30** at register `0x0584` and weekday mask **0x71→0x31** at `0x0589` each received genuine `CONTROLLER_ACCEPTED` with one physical attempt. Final F1 readback reported `BATCH_DONE f1Exact=1 pages=2 count=2`, slot 4 **20:23–20:30**, Monday/Friday/Saturday. RX CRC discrepancy **0**, parser resync **0**, observed through the captured window. **COMPLETE / POSITIVE** for that bounded calendar edit and resumed operation; not proof of every calendar operation or of other CM930 versions.

**Validation:** ESPHome 2026.9.0 running on the user ESP32-S3 and LIVE log as above. No independent fresh build was executed here. The superseded `1.02` source file was removed from the current repository tree on 2026-11-22; its history remains available through Git commits. Superseded versions remain available in Git history rather than accumulating in the current firmware directory.

## Write User 1.02 — 2026-11-17
- Controller 0x02 loss >=5s with living room-sensor 0x0A: automatic one-episode transition into the EXISTING S92 cold-start state machine.
- Automatic recovery rearm moved from FC16+0708 transport ACK to same-epoch M6=5, native accepted ownership and CURRENT 4/4.

# Passive Version
## Passive 1.1 — 2026-11-17

**Firmware:** [`thermia_itec_xtr_passive_1.1.yaml`](thermia_itec_xtr_passive_1.1.yaml)

This release combines the alarm decoding, data-freshness improvements, Home Assistant presentation fixes and memory optimizations into **one RX-only version**.

### Added

- **30 OEM-profile-backed active-alarm predicates:** 29 from the current-alarm registers `0x085F–0x0861` and one outdoor-unit flag from `0x082F`. Conditional alarm predicates use their relevant configuration fields.
- Individual Home Assistant alarm entities, an aggregate current-alarm summary and alarm-source availability diagnostics.
- Passive decoding of controller-origin `0x0884/60` alarm-history pages. Supports legacy 10 × 6-word and newer 8 × 7-word layouts when the received record content permits; raw record identifiers are **not** equated with current-alarm bits or UI E-codes.
- Passive decoding of the controller clock from `0x06EA/7`, when received.
- Source-specific telemetry freshness and Home Assistant data-quality/source status indicators. Expired live controller, outside-unit and other source-based measurements become unavailable instead of silently showing stale values.
- Explicit distinction between restored/cached heating settings and fresh controller observations.
- ESP32-S3 memory diagnostics: minimum free heap, largest contiguous free heap block, heap fragmentation and free PSRAM, alongside existing free heap.
- Freshness-checked raw heat-demand register `0x0848` as a diagnostic, without assigning unverified PID/integral semantics, units or a controller setpoint interpretation.

### Fixed and improved

- Removed five duplicated `disabled_by_default` YAML keys, correcting strict YAML parsing.
- Reduced receive-parser temporary allocations by reusing the frame buffer and using a fixed-size frame-length table.
- Corrected defrost labels: `0x087B` is the counter, `0x087C` is minutes since the previous defrost, and `0x087D` is the previous duration in minutes. Invalid values remain unavailable.
- Finished English translations of internal operating-mode values and cleaned up Home Assistant diagnostic visibility.
- Preserved existing Home Assistant IDs, the validated RX parser/CRC checks, bus health/watchdog and **no-TX** UART architecture.

### Availability and verification

- Current-alarm `0x085F/5` frames have been observed on the local XTR bus when a DCM/Online communication peer was active. A passive ESP does not request those pages; stale or never-seen alarm sources stay unavailable. **No data is not the same as no active alarm.**
- The OEM definitions are source-backed; real-fault behaviour for all 30 predicates has not been tested on the local XTR.
- **SOURCE / OFFLINE TESTED:** strict YAML structure/duplicate-key checks, alarm-formula comparison and receive-parser equivalence on captured bus data (2,476 valid frames decoded identically).
- These offline checks are **not** a full ESPHome target compile or an independent LIVE firmware test. No physical TX, active reads, alarm acknowledgements or parameter writes were added.

## Passive 1.0 — original public baseline

- Initial public XTR receive-only ESPHome YAML with one RS485 receiver, Modbus RTU-like CRC checking, passive temperature and operating telemetry, selected heating-settings cache and Home Assistant integration.
- Serves as the baseline for the consolidated Passive 1.1 release. Original release date is not asserted here.

## Other published iTec XTR firmware variants

- [DCM Read Only 1.0](thermia_itec_xtr_DCM_readonly_1.0.yaml) — native DCM read-only integration. Unlike Passive, it can transmit protocol traffic but does not change controller parameters.
- [Write User 1.04](thermia_itec_xtr_write_user_1.04.yaml) — current public native user-setting-control variant; previous releases available in Git history.

**Scope:** This public changelog contains no proprietary handshake algorithms, keys, authenticated captures or controller secrets.
