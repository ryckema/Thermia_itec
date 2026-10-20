# V5DCM83 — first on-device RX-only result (partial, 2026-10-20)

**Experiment:** V5DCM83 RX-only shared supervisor.  
**Current status: RUNNING / PARTIAL.** User supplied a real ESPHome API log; this is NOT merely an offline or host execution. Device observation is positive for RX-only owner supervision and normal receive telemetry, while startup RX/B11D fault provenance remains unresolved.

## Evidence and original controlled change

Evidence: user-uploaded `Pasted text(20261020-080704).txt`, SHA256 `bac4ceb1385d003af5dce52653fc6e5c7b000d92eee9cfb7af66f54fac7a46f6`, **2435 lines**, captured **10:05:21.076–10:06:54.920** (93.844 seconds) on ESPHome 2026.9.0 via successful API handshake. The log's distinctive `V5DCM83 Shared RX-Only Owner` entity confirms V83-specific running code; it does **not** independently establish the flashed binary checksum, exact ESPHome compilation process, firmware identity, physical electrical timing or that the entire user-produced firmware equals the original candidate SHA.

Original last user-verified baseline was V49 RX_ONLY/HARD_DENY. V83 controlled delta: unbind both legacy native physical port borrowers, place a shared RX-only software observer under B11D 50ms and DE watchdog 1s, retain original RX parser/HA controls and sticky fault logic; no new transmit service. The previously **PREPARED / NOT RUN** source-review report remains valid as the preparation record, but the new uploaded log establishes execution. No controlled bus TX, register write or controller restart requested or evidenced. EXP388 remains **RUNNING / PARTIAL**.

## Positive local observations

- Shared observer first `owner=RX_ONLY locked=1 samples=14 unsafe=0 sticky=0 sw=0 pin=0 TX=HARD_DENY`; final `samples=104 unsafe=0 sticky=0 sw=0 pin=0`. 19 snapshots, approximately 90 additional supervisor samples; **no V83 unsafe or DE-high fault during the observed window**.
- Original V45/B11D DE status across 19 samples: `DE_sw=0 DE_pin=0 replyAttempts=0 admitted=0`; `build=0`, no owned/unsafe TX window. Native V43 and V44B status remain build-locked and unarmed.
- V5 TX-02 native executor progresses from `candidates=18 denied=18 physical_attempts=0` to `candidates=128 denied=128 physical_attempts=0`. Source-reported V5 S2 physical TX, S3 UART write calls, S3 physical delivered, B11C portable IO attempts and S8R3 TX attempts remain **0**. Thus **NO TX OBSERVED IN SOFTWARE DIAGNOSTICS**, not an independent oscilloscope proof of zero wire activity.
- V5 parser `frames=103 pages=16 known=16 badGeom=0 unknown=0 resync=22 drops=0 TX=0` → `frames=868 pages=141 known=141 badGeom=0 unknown=0 resync=22 drops=0 TX=0`: **765 additional valid frames, 125 additional known pages, no additional reported resync/drop, no reported geometry mismatch** in this interval.
- B11C original portable mirror `frames=88→856`; source summary at 10:06:46: 798 V5, 798 portable, count/byte difference 0, boundary errors 0, new resync/drop 0. UART API and heating telemetry remained accessible: room 21.2°C, DHW 49°C, supply 34→35°C, compressor 38→39 Hz; heating mode observed. Some other temperature/config entities remain `nan`; without a comparable pretest or longer interval, do not declare all production values restored.
- Controller metadata: FC16 page count 15→140, repeated 085F/5 service and 04A6/13 settings-pattern observations; no FC23 initial challenge during this capture, `0708` polls 0, configuration page/ACK semantic qualification 0. Neither controller owner, native admission nor Connect APP33/C2/Online proven.

## Existing-at-first-snapshot startup RX issue: not explained

The original B11D first-fault reports `RAW_V5_FRAME_COUNT_MISMATCH` and **countDiff=1** with `B11D_sticky=1`. Independent raw scanner summary: `batches=1 rawFrames=2 portableFrames=0 comparedV5=0 countDiff=1`; no later increments. V5 parser resync counter already **22** at first visible reading, and bridge RX-integrity faults already **2**, all stable through capture. No matching first-fault emission or early boot raw-framing lines were included in this log.

**Critical source distinction:** the exact V83 candidate declares `b11d_fault` and `b11d_first_fault` with `restore_value: no` and initial false/`NONE`. Therefore they could NOT simply be restored unchanged from a prior V49 firmware across a genuine ESP reboot. The V83 boot appears to precede the first user log line: an ESP uptime reading is 33 seconds at 10:05:45, then 93 seconds at 10:06:45. The mismatch was thus likely latched **during the initial seconds of this V83 boot**, before API logging began. This is compatible with startup framing or a real pre-log mismatch; the root cause and whether it already happened at V49 startup are UNKNOWN. Do not clear the fault or claim current independent RX-qualification is positive merely because the counters stopped increasing.
- FIX2 remains `REVOKED`; V49 post-gap cohort remains `WAIT_GAP` with no witnessed new gap; the old/current fault gate still blocks native qualification. Several red diagnostics `ABORT_NO_TX` and `MONITOR_HOLD` are explicitly fail-closed model decisions, not evidence of actual device TX or malfunction of the heat pump.

## Criteria, safety and next action

**Positive criteria achieved in this limited live window:** unique V83 diagnostic is running, supervisory pin/switch consistent low, no software TX attempts, stable passively read production metrics and continuing CRC-complete reception without new observed resync/drop.

**Unresolved/partial:** source of boot-time independent B11D `RAW_V5_FRAME_COUNT_MISMATCH` and 22 pre-log resyncs; incomplete duration and no boot-start log; independent physical DE/owner/EOF/slot unknown; no source-to-binary/hash verification or controller admission. Because of these unknowns, retain **RUNNING / PARTIAL**, not COMPLETE/POSITIVE for the *whole* V83 validation. V83's original preparation remains distinct from this user-performed run.

**Minimum missing evidence:** if available, request ONLY the earliest ESP32 boot log covering first 10–15 seconds **from the same V83 start**, particularly the first red `[B11D-RX] FIRST_FAULT` and initial parser resync messages. Do **not** ask user to reboot the heat pump or enable TX; a fresh ESP restart should not be initiated merely to retrieve this evidence without separate plan. A further passive interval may establish continuing healthy telemetry but cannot reconstruct initial mismatch cause. Abort on any new DE-high, TX counters, ongoing growth in CRC/resync/drop, HA telemetry regression or new controller COMM ERR; recover original verified V49 if V83 introduces an issue. No independent hardware-scope TX test is implied.

**NEXT:** analyze the earliest boot mismatch against unchanged original B11D scanner/25ms coalescing and original parser alignment before generating further YAML or advancing to new active experiments. No standalone initial native TX (historic EXP256 caused COMM ERR).