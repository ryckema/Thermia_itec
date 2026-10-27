# G03-01R and G03-02R — Offline source and Saleae-to-ESPHome correlation audit (2026-10-14)

**Current status:** G03-01R `COMPLETE / POSITIVE` for source-baseline verification; G03-02R `COMPLETE / POSITIVE` for source provenance/nonunique matching audit and `COMPLETE / INCONCLUSIVE` for *same-session physical EOF→current B6 callback timing*. G03 physical EOF current-B6 correlation **OPEN**; G04 exclusive reply slot **OPEN**; native `0x0F` TX **HARD DENY**.

**Scope of this commit:** documentation-only reconciliation of the user's completed local offline audits, not a fresh Saleae re-decode, ESPHome compilation, on-device capture, electrical measurement or TX. Source artifacts were previously generated locally; this public note excludes sensitive native emulation payloads and recovered security details.

## G03-01R — COMPLETE/POSITIVE OFFLINE
- **Hypothesis:** existing B6 UART debug batching cannot be treated as last electrical stopbit EOF; previous G03-01 and G04-06 findings remain applicable to user-confirmed B6.
- **Baseline:** G03-01 original source audit, G03-03..05 historical XTR Saleae edge reconstructions, G04-04/06/07 driver audit, user-confirmed installed B6 RX-only. Installed binary/include hash independently unverified.
- **Controlled change:** offline reread of B6 source and historical reports, hash/line checks only; no firmware or bus action.
- **Observed source:** B6 4,442 lines, SHA256 `6139bd73b26967e4c7beaa02f2a370c889d89731c7c4eafbd1d227d81f4dfca9`; UART 9600 8E1, RX GPIO18, TX GPIO17, DE GPIO21, debug RX timeout 5ms, callback `micros()`. ESPHome 2026.9.0 driver prior audit: UART event queue not provided to YAML callback; timeout/debug task scheduling not hardware last-stopbit timestamp. Earlier D2 1 MHz reconstruction 1,047 CRC-good ADUs; two additional recordings 55+156 CRC-good ADUs.
- **Relevant:** physical UART last stopbit, 3.5 char RTU idle; `0x0F` native FC23/FC16 only passive observation. 9600 8E1 char=1.145833ms; 3.5 chars=4.010417ms **calculated**, not observed callback latency.
- **Positive criterion:** prove software callback ≠ physical EOF and identify single-owner metadata feasibility; met within source-audit scope. **Negative:** no exact current-B6 EOF timing from callback; unresolved. **Abort:** extra UART byte consumer, inferred physical timing from 5ms timeout, TX/DE change. **Recovery:** none, offline-only; retain B6 RX-only.

## G03-02R — COMPLETE/POSITIVE provenance audit; COMPLETE/INCONCLUSIVE cross-clock EOF correlation
- **Hypothesis:** existing Saleae original D2 recordings and local ESPHome raw frame logs can be aligned uniquely, same session, to measure `t_callback - t_last_stopbit` without a new test.
- **Baseline:** G03-01R, G03-03/05 local XTR D2 reconstructions, G04-05 B6 software callback timings, existing local .log files.
- **Controlled change:** read original `.sal` embedded start metadata; compare exact complete CRC-good frame byte strings against existing ESPHome `RAW=/HEX=/FRAME=/DATA=` records; no live bus/device modification.
- **Original Saleae capture UTC metadata:** `Session 3.sal` 2026-09-04 11:22:16.306041, 55 CRC-good frames, 16 unique full frame payloads, max same payload repeated 6 times; `Session 3--1degree.sal` 2026-09-04 11:22:46.732742, 156 frames, 18 unique, max repeated 18; `Session 5.sal` 2026-09-04 11:31:55.810217, 1,047 frames, 50 unique, max repeated 115. Total 1,258 complete CRC-good reconstructed D2 frames. These acquisition metadata timestamps do **not** synchronize ESP clock and Saleae host clock.
- **Available ESPHome files:** 22 local `.log` files inspected in earlier offline execution; no corresponding Sept 4 raw ESPHome log available. Some later Sept 29/30 logs contain exact bytes (e.g. recurrent `085F/5` all-zero native publications), but repeated bytes across **different dates** cannot establish a simultaneous shared event or clock offset. G01-09/current B6 October windows do not coincide with Sept 4 Saleae sessions.
- **Relevant:** passive native `0x0F` FC16 `03E8/14`, `085F/5` and other `0x02/0x1E` frame chronology. No ACK or native TX assumed.
- **Positive criterion:** multiple uniquely ordered same-session CRC-valid frames **and** independently defensible common clock/marker permitting bounded EOF-to-callback latency. **NOT MET**.
- **Negative/inconclusive criterion:** mismatched dates, repeated frame payloads, no same-session clock. **MET**; no absolute offset, jitter percentile or worst-case current-B6 lag can be claimed.
- **Abort:** invented time alignment, host millisecond timestamp treated as wire EOF, cross-model inference treated as local, EOF used to authorize G04/TX. **Recovery:** none, offline-only; B6 unchanged.
- **Next minimum evidence:** first seek existing 2026-09-04 raw ESPHome log from exact Saleae session (would only characterize historical firmware). To characterize *current* B6, a **separately authorized** passive simultaneous D2+current B6 RX-only trace with independently verifiable common timing marker would be needed. No second UART consumer, DCM, room-sensor disconnect, controller reboot, or active response required.

## Evidence classification and gate disposition

**PROVEN local historical:** reconstructed digital D2 UART edges and complete CRC-good ADUs from three 2026-09-04 Saleae recordings; existing B6 source/debug batching characteristics. **STRONGLY SUPPORTED:** callback-entry software timestamps cannot substitute for last physical stopbit or independent slot availability. **HYPOTHESIS:** an approved simultaneous passive capture could bound EOF→callback delay, subject to clock synchronization and uncertainty. **OPEN/UNKNOWN:** current B6 physical EOF correlation, independent physical UART driver/DE timing, G04 reply slot, G05 drain/release, G06 fail-low. G02 remains installation-scoped CONDITIONAL POSITIVE and G01 manual video scope unchanged.

**Safety:** G03 overall OPEN; G04 OPEN; native TX HARD DENY. Historical negative/inconclusive experiments remain unchanged.
