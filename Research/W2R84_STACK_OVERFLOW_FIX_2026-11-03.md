# W2R84 — bounded ESPHome loopTask stack overflow correction

**Experiment status:** PREPARED / NOT RUN
**Evidence grade:** SOURCE / OFFLINE TESTED, **not target compiled / flashed / live**.
**Baseline:** user's XTR M controller 2.4.2, MAIN04-W2R83 live confirmed for select->automatic owned F1 3/3->one user Apply->genuine FC16 + exact post-F1 persistence (2026-11-03). Existing W2R83 remains full rollback and only known locally verified calendar baseline.

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