# Thermia iTec XTR — Firmware Changelog

This file records the public iTec XTR firmware release history. Passive, DCM Read Only, Write User and Service have separate functionality and version numbers; Passive 1.1 is **not** an upgrade to either active variant.

For the current firmware and installation instructions, see the [main README](../README.md). Entries describe source changes and the verification available at the time; they are **not** a guarantee of full ESPHome compilation or live behaviour on another Thermia controller.
# Write version
## Write User 1.1 — 2026-11-27

**Firmware:** [`thermia_itec_xtr_write_user_1.1.yaml`](thermia_itec_xtr_write_user_1.1.yaml)

Major feature, reliability and usability update following Write User 1.03 and 1.04. Based on the locally validated Service 1.0 architecture, with installer-level parameter writes removed and the existing User controls retained. Single standalone ESPHome YAML, published as the exact FINAL firmware derived from the locally tested RC06.

### Performance monitoring

Added 11 performance monitoring entities, providing:

- Observed compressor starts today.
- Observed compressor running time today.
- Compressor duty cycle today.
- Mean running compressor frequency today.
- Total observation time today.
- Current compressor off time.
- Last completed compressor off time.
- Direct defrost cycle count since boot.
- Last completed defrost duration.
- Mean completed defrost duration since boot.
- Supply temperature deviation based on paired OEM measured and target temperatures.

Daily statistics follow the local calendar date and exclude unobserved periods. They are calculated from available observations and are not persistent lifetime counters.

### Circulation pump and defrost monitoring

- Added circulation pump command percentage, with separate primary and secondary source diagnostics.
- Added direct outdoor-unit defrost detection, with qualified OEM data as fallback.
- Added source selection and freshness diagnostics.
- Improved defrost cycle and duration tracking.
- Revised the interpretation and presentation of native defrost-related counters. Unconfirmed counter semantics remain explicitly labelled as candidates.
- Pump command percentage is not presented as measured flow or actual pump speed.

### Central operating state

Added a unified `Operation | Operating State` entity for Home Assistant dashboards.

Supported states include Heating, Hot Water, Cooling, Starting, Defrosting, Standby, Alarm and qualified running or compressor-off states.

- Separates actual production from controller operating context.
- Provides an independent operating activity entity without the alarm overlay.
- Includes operating-state source and data-quality diagnostics.
- Reports unknown or incomplete states instead of inferring unsupported activity.
- Does not assume that standby means all auxiliary equipment is switched off.

### Extended read-only Service monitoring

- Extended native Service synchronization to 17 configuration pages and 303 words.
- Added 49 read-only Service register views.
- Expanded automatic parameter refresh through the existing native communication engine.
- Added additional heating, hot-water, cooling, auxiliary-heater, Optimum, sensor-calibration and installation parameters.
- Added outdoor-unit flow detection, four-way valve status, confirmed setpoint and frequency-limitation observations.
- Added Service source, refresh and synchronization diagnostics.
- Unverified register interpretations remain labelled as candidates.
- Installer-level setting changes are not supported by Write User.

### Calendar management

- Extended the shared 32-slot calendar editor.
- Added native Home Assistant start and end time fields.
- Added start and end date fields and weekly/date-range schedule selection.
- Added creation and clearing of calendar records.
- Improved calendar transaction handling, input validation and controller readback.
- Preserved the existing native TX owner and bounded transaction safeguards.
- Clarified EVU or power-limitation calendar labels.

The four legacy hour/minute controls have been replaced by native time entities. Existing dashboards and automations referencing those controls may require updates.

### Native controller clock

Includes the native clock functionality introduced in 1.04:

- Live heat-pump clock display.
- Home Assistant time and controller clock-difference diagnostics.
- Manual clock synchronization.
- Optional automatic daily synchronization.
- Automatic correction only when the time difference exceeds 60 seconds.
- Controller-confirmed readback and bounded correction attempts.
- Independent RTC refresh, even when extended Service parameter refresh is disabled.

Automatic clock correction remains disabled by default.

### Alarm monitoring and fault reporting

- Added an independent passive receive cache for current alarms, alarm history and outdoor-unit fault information.
- Alarm presentation no longer requires a fully established local DCM session when valid controller-origin frames are received.
- Added the outdoor compressor-down indication to the active alarm summary.
- Added outdoor-unit and communication-kit fault presentation.
- Extended alarm-history presentation to ten records where supported by the detected record layout.
- Separated passive alarm availability from active alarm-refresh status.
- Fixed active alarm-refresh completion so that a received page is not considered complete until its physical acknowledgement has been sent.
- Missing, stale or invalid alarm sources remain unknown rather than being reported as alarm-free.

Historical event identifiers are not automatically interpreted as Thermia UI error codes.

Passive reception does not guarantee that the controller exports every alarm page without an active DCM peer.

### Native communication and recovery

- Improved retained-session recovery and INFO synchronization.
- Added bounded INFO synchronization continuation through the existing native communication engine, enabled in the released configuration.
- Improved recovery after ESP restart and incomplete synchronization.
- Improved serialization of native reads, refreshes and user-setting transactions.
- Preserved the existing single UART/RX/TX/DE owner, CRC checks, frame validation, session freshness, collision safeguards and ABORT functionality.
- Retained controller-confirmed User parameter writes.

The additional INFO clear-response recovery branch has not yet been directly observed in a live capture.

### Data quality and Home Assistant improvements

- Improved source-specific freshness handling and invalid-value presentation.
- Improved synchronization of measured and target supply temperatures.
- Separated direct measurements, OEM-reported values and candidate mappings.
- Improved English labels, units, icons and diagnostic categorization.
- Corrected the OEM outdoor-temperature label to Outdoor Average.
- Reduced overlapping and redundant default-visible entities.
- Expanded optional technical diagnostics without unnecessarily cluttering normal Home Assistant dashboards.

### Internal architecture and cleanup

- Rebased Write User on the shared Service 1.0 firmware architecture.
- Removed the dedicated installer-level Service setting-write engine from Write User.
- Retained the read-only Service register views and 17 supported User-write descriptors.
- Removed obsolete state, redundant internal code and unused diagnostic paths.
- Preserved the established native transaction owner and controller readback requirements.
- No private authentication material, dynamic handshake implementation or experimental energy, COP, refrigerant or flow models are included.

### Upgrade and compatibility notes

- The locally validated platform is the Thermia iTec XTR M 3N / Total Compact with CM930 software 2.4.2 and ESP32-S3.
- Several native session and write gates in 1.1 explicitly require CM930 2.4.2. The broader 2.4.0–2.4.3 access policy of Write User 1.03 should not be assumed to carry over.
- Preserve the existing device name and hardware configuration when upgrading.
- Review dashboards and automations referencing renamed or replaced entities.
- Home Assistant may retain previous entity visibility settings.
- Automatic parameter writes and automatic clock correction remain disabled by default.
- Installer-level parameter writes require the separate Service firmware.

### Local validation

The release candidates and final firmware were tested on the local XTR M installation. The following observations are from the release validation sequence and do not imply that every feature was independently retested in the exact FINAL build.

- Native session recovery and CURRENT synchronization: 4/4.
- INFO synchronization: 5/5 on RC06.
- Calendar synchronization: 12/12 pages.
- Service synchronization: 17/17 pages, 303 words.
- Successful active alarm refresh and acknowledgement.
- Passive alarm-related publication before full native session qualification.
- Controller-confirmed heating curve changes from 38 to 39 and back to 38 on RC05.
- Successful cold start confirmed by the owner on RC05.
- Zero CRC disagreements in the observed validation windows.

Remaining research includes historical alarm identifiers, fully session-free alarm-page availability, the additional INFO recovery branch and compatibility with other CM930 controller profiles.

Superseded firmware versions remain available through Git history.

## Write User 1.04 — 2026-11-24

**Firmware (historical):** [`thermia_itec_xtr_write_user_1.04.yaml`](https://github.com/ryckema/Thermia_itec/blob/ffbbd711a7df428ba54380c0c9cfdfeb0d031e23/Thermia%20iTec%20XTR/thermia_itec_xtr_write_user_1.04.yaml)

### RTC independence update (2026-11-24)

- Native RTC reads remain scheduled even when Extended Automatic Parameter Refresh is OFF. Automatic Time Sync alone controls automatic correction, with its existing 60-second tolerance, daily attempt limit, same-session ownership, exact readback, ABORT and single TX owner retained. Disabling Service refresh cancels only its unsent parameter requests; the RTC request and correction are not cancelled. An incomplete RTC read is held until a new qualified session or explicit Time Sync OFF/ON.
- Improved recognition of valid short/long FC16 page geometries (`0492/9 or 11`, `051E/9 or 10`) and retained-session qualification. Existing public known-challenge cold start, single native TX owner, CRC/parser, epoch/freshness guards, ABORT and established user controls are retained.
- Persistent automatic extended read-only refresh, enabled by default, without the RC trial expiry. The locally qualified XTR M 3N / CM930 2.4.2 profile retrieves 17 configuration pages / 278 words, with independently scheduled native RTC reads. Requests use the existing native owner. Other CM930 2.4.0–2.4.3 profiles retain their previous access range; expanded reads are not field-qualified there.
- Periodic alarm read becomes due at 240 seconds rather than waiting until the 300-second cache expiry.
- Native clock display, Home Assistant time and clock-difference diagnostics. 
- Clock sync: added `Configuration | Automatic Time Sync` switch, persistent OFF by default. Explicit opt-in enables comparison on activation and daily thereafter; only drift above 60 seconds can trigger one correction attempt per 24 hours, with native readback and no automatic retry on failure. 
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
- [Write User 1.1](thermia_itec_xtr_write_user_1.1.yaml) — current public native user-setting-control variant; previous releases available in Git history.
- [Service 1.0](Service/) — separate expert-only installer-level firmware; read its own README before use. The 1.1 alarm/recovery updates are not yet integrated into Service 1.0.

**Scope:** This public changelog contains no proprietary handshake algorithms, keys, authenticated captures or controller secrets.
