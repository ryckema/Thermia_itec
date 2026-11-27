# W2R84 — bounded ESPHome loopTask stack overflow correction

**Experiment status:** COMPLETE / POSITIVE for bounded live stack-headroom/no-regression test; historical overflow root cause still OPEN
**Evidence grade:** SOURCE / OFFLINE TESTED and **user target compiled / FLASHED / LIVE / LOCALLY VERIFIED (bounded W2R84 test)**.
**Baseline:** user's XTR M controller 2.4.2, MAIN04-W2R83 live confirmed for select->automatic owned F1 3/3->one user Apply->genuine FC16 + exact post-F1 persistence (2026-11-03). Existing W2R83 remains full rollback and only known locally verified calendar baseline.

## 2026-11-03 14:12–14:13 XTR live result — COMPLETE / POSITIVE (bounded stack-headroom and no-regression test)

**LIVE / LOCALLY VERIFIED** from user log `Pasted text(20261103-131404).txt` (2396 lines, ~97 s of ESPHome API logs). ESPHome 2026.9.0 on ESP32-S3 ESP-IDF 5.5.5; reset reason `Reboot request from esphome.ota`, not a panic. `Thermia Firmware Build` reports `MAIN04-W2R84` at 14:13:14.79.

- New `Thermia ESP Loop Stack Min Free` reads 13038 B at 14:12:30 and 14:12:45, drops once to 12894 B by 14:13:00, remains 12894 B at 14:13:15, 14:13:30, 14:13:45. With allocated 16384 B, maximum observed loopTask stack use is **3490 B**. Above provisional 2048 B headroom threshold throughout.
- Native M6 CURRENT4/4 receipt `mask=0F` on pages 03E8, 042E, 0442, 0546 at 14:12:49–52; no semantic setting TX during sync.
- W2R83 auto F1 Program 4 reader armed 14:12:53.945; owned FC16 pages 055A/057B/059C `seenMask=07` received 14:12:54–56, fresh P4 readback `18:21–18:26 days=40`, matching prior locally validated W2R83 calendar write. No Apply/write test requested or performed in this W2R84 run.
- RX parser latest `CRC_CHECK=740 CRC_DIFF=0 SHAPE_OTHER=0` at 14:13:46; `RX Buffer Drops Since Boot=0`, `Parser Resyncs Since Boot=0`.
- Automatic broader CAL12/12 refresh armed 14:13:04; this log doesn't contain an unambiguous CAL12/12 completed marker. Do not call global calendar12/12 complete from this alone.
- No panic, abort or unexpected reboot observed during capture (device uptime increments to 90s).

**Strong conclusion:** W2R84 is live and preserved the tested native M6, F1 and RX functionality with generous **measured** loopTask stack headroom. **Crucial qualification:** 3490 B measured peak stack use would have fitted within W2R83's former 8192 B allocation, so this observation *does not establish* that the historical W2R79F FreeRTOS overflow arose in the ESPHome loopTask. It could have occurred on another task or rare execution path. Retain classification of historical crash root cause **OPEN**, not fixed/proven.

**Experiment result:** COMPLETE / POSITIVE for the bounded W2R84 loopTask margin and no-regression observation. **No additional microtest needed**; retain this live baseline and diagnose any new crash from a full panic with overflowing task identity rather than blindly raising stack again. **CURRENT MILESTONE:** W2R84 stable loopTask after OTA. **DELIVERABLE:** working locally observed W2R84 plus existing full private ZIP/rollback. **REAL BLOCKER:** none for measured stack headroom; historical crash task identity UNKNOWN. **ONE NEXT ACTION:** keep W2R84 running normally and capture the complete panic/overflowing task only if a recurrence occurs.

## OBSERVED FACTS
- W2R79F prior panic on CPU 1: vApplicationStackOverflowHook invoked by FreeRTOS vTaskSwitchContext; the crash report does not provide the overrun task name. Do not infer the specific task from the core number alone.
- Existing W2R83 ESPHome UART RX parser executes in main loop callback; it contains serially executed scratch char buffers 360, 300 and 160 bytes, nested frame processing and repeated string formatting. ESPHome's esp-idf loopTask (core 1) defaults to 8192 bytes; documented configurable `esp32.framework.advanced.loop_task_stack_size`.
- W2R83 live user log confirmed no RX CRC errors, no drops, and successful native F1 3/3 and selected P4 one-field write; a short clean log does not eliminate intermittent stack exhaustion.

## ONE CODE CHANGE / HYPOTHESIS
**HYPOTHESIS:** ESPHome main loop task suffers transient high stack pressure during nested native RX/HA callbacks, contributing to the FreeRTOS overflow. To reduce measured stack pressure without changing protocol state:
1. Increase the *correct* ESPHome loopTask stack from 8192 to 16384 bytes, not the unrelated ESP-IDF app_main stack.
2. Move three non-reentrant, main-loop-only RX/status scratch arrays (360+300+160 B) into static BSS with unchanged formatting/reading.
3. Add one diagnostic `Thermia ESP Loop Stack Min Free`, the loopTask's lifetime minimum free bytes via `uxTaskGetStackHighWaterMark(nullptr)`; ESP-IDF returns bytes.

**Unchanged:** sole S92 RX/TX/DE/UART owner, parser shape/CRC and frame counters, cold start, M6, FC03/FC16, F1 auto read, W2R83 Apply, authorization/ABORT/rollback, all existing HA entities and controls. No expansion of physical TX scope.

## OFFLINE
Complete standalone W2R84 ESPHome YAML parses with !secret resolution stub; 1147 unique IDs. Parsed original framework/uart/globals/interval/buttons/selects/switches/scripts retained; only framework advanced option, three C++ stack-to-static qualifiers, one diagnostic sensor and firmware build string change. Source diff 85 lines. ZIP CRC and SHA256 content PASS. No available ESPHome target compiler in environment.

## LIVE / ABORT / ROLLBACK
User compiles and flashes W2R84 manually. Confirm build W2R84, M6/current4/4/CAL12/12/V5 CRC0/drop0; select programs 3,4,5 to exercise auto F1 reads **without setting writes**. Inspect new HA diagnostic after native activity; ≥2048 B is provisional sufficient margin for this bounded run, not proof against all future states or other task overflows. If crash recurs, capture UART serial panic including task name, change hypothesis rather than increasing stack again. On bus/collision anomalies, use existing S92 ABORT and roll back to exact W2R83 YAML in private ZIP.

**CURRENT MILESTONE:** stabilize W2R83 without regression.
**DELIVERABLE:** W2R84 full YAML + single private ZIP.
**REAL BLOCKER:** no source blocker; task identity of historic crash still UNKNOWN and target live evidence needed.
**ONE NEXT ACTION:** user compiles/flashes W2R84 and observes stack headroom under routine native F1 reads.