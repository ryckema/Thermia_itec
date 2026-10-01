# Thermia ATEC / DHP-AQ experimental ESPHome path

> **Status: PREPARED / NOT RUN**
>
> This folder is an experimental ATEC/DHP-AQ side branch of the main Thermia iTec XTR M research. It is **not a production integration** and it has not yet been confirmed on the target ATEC installation.

The goal of this version is to reproduce only the parts of the native Thermia Online/DCM exchange that are supported by captured bus traffic, then test one tightly bounded semantic write: the room setpoint at `0x03F4`.

Current implementation:

[`thermia_atec_waveshare_atec_exp1_queued_room_setpoint.yaml`](./thermia_atec_waveshare_atec_exp1_queued_room_setpoint.yaml)

## Evidence basis

ATEC-EXP1 was built by comparing the available ATEC/DHP-AQ / iTec Eco gateway captures with the write path developed in the XTR research. The ATEC version does **not** simply reuse XTR wire behaviour.

The strongest capture-backed sequence used here is:

```text
controller -> 0x0F FC03 0708/count6
gateway    -> 0708 mailbox response

controller -> 0x0F FC03 03E8/count14
gateway    -> 14-word desired 03E8 page

controller -> 0x0F FC16 03E8/count14
gateway    -> FC16 ACK
```

In the supplied capture, word 12 of the `03E8/count14` page — address `0x03F4`, decimal 1012 — changes between 20 and 30 and is then republished by the controller. Discussion #143 independently identifies decimal 1012 as the room thermostat / room setpoint field.

The same captures also show the larger settings-export family beginning at `03E8`, followed by pages such as `03FC`, `0410`, and later pages through `06F4`, plus recurring runtime pages in the `07D0..` / `08xx` area.

Supporting analysis:

- [External iTec Eco 5 full capture analysis](../EXTERNAL_ITEC_ECO5_FULL_CAPTURE_ANALYSIS.md)
- [Original Discussion #143](https://github.com/klejejs/ha-thermia-heat-pump-integration/discussions/143)

## What ATEC-EXP1 changes compared with the XTR write branch

The ATEC build keeps the conservative queued-write safety design from XTR EXP374, but removes XTR-specific session assumptions.

| Area | ATEC-EXP1 behaviour |
| --- | --- |
| Startup | 10 s passive-only peer-responder check |
| Active slave path | `0x0F` only |
| Mailbox poll | `0708/count6` |
| Normal idle reply | six zero words |
| Room-page selector | `0000,0001,0000,0001,0000,0000` |
| Semantic page | `03E8/count14` |
| Writable field | only word 12 = `0x03F4` |
| Write range | 20–30 °C, integer steps only |
| Queue | one pending request, last user intent wins |
| Post-write settle | at least 2 s |
| Unknown `0x0F` traffic | capture-only |
| `0x0F FC17` | capture-only; no ATEC response is synthesized |
| `0x041D` DHW start | diagnostic/read mapping only; not writable |

The XTR-specific cold-boot/R1 replay, A80E/A80F guard, hot-rejoin logic and other semantic write targets are deliberately absent.

## Hardware/config assumptions

The YAML is currently written for the same ESP32-S3/Waveshare-style RS485 setup used during the research:

```text
UART baud: 9600
Data bits: 8
Parity: EVEN
Stop bits: 1

TX: GPIO17
RX: GPIO18
RS485 direction / DE: GPIO21
```

These GPIO numbers are **implementation settings in this YAML**, not a claimed universal Thermia ATEC pinout. Verify them against the actual ESP32/RS485 hardware before flashing.

Required ESPHome secrets are:

```text
wifi_ssid
wifi_password
thermia_api_encryption_key
thermia_ota_password
thermia_fallback_password
```

The YAML has been structurally checked, but this ATEC version has **not yet been ESPHome compile-verified or run on the target heat pump**.

## Safety model

ATEC-EXP1 is intentionally fail-closed.

During the first 10 seconds after boot, DE remains LOW and the ESP transmits nothing. If another device already answers as slave `0x0F`, the experiment stops rather than competing on the bus.

After activation, the firmware only responds to frame shapes that were explicitly included from the capture analysis. Unknown `0x0F` traffic remains capture-only.

A semantic room-setpoint transaction additionally requires a fresh `03E8/count14` page cached within the previous 60 seconds. The outgoing desired page is reconstructed from that exact cache and only word 12 may differ.

The semantic write path is disabled if the controller republish does not exactly match the requested page, if another word changes unexpectedly, if a peer responder appears, if parser resync/RX-drop counters change, or if the transaction times out.

The Home Assistant **ATEC Abort Experiment** button immediately disables experiment TX and returns DE LOW.

## Home Assistant controls

Experimental controls are placed under **Configuration**.

| Entity | Purpose |
| --- | --- |
| `ATEC-EXP1 Room Setpoint` | Experimental 20–30 °C room-setpoint target |
| `ATEC Request Settings Snapshot` | Manually requests the captured broad settings export |
| `ATEC Abort Experiment` | Stops the experiment and disables TX |

Important diagnostics include `ATEC-EXP1 Status`, `ATEC-EXP1 Stage`, `ATEC-EXP1 Last Event`, the current cached room setpoint, cache age, peer-response count, parser/resync counters and confirmed-write count.

`ATEC DHW Start (0x041D mapped)` is deliberately diagnostic only. No DHW write is implemented in EXP1.

## First test procedure

1. Boot the ESP and do not touch any control during the passive preflight.
2. Confirm a clean log marker:
   ```text
   PREFLIGHT_PASSED peer=0 busFresh=1 ENTER_STAGE40 DE=LOW
   ```
3. Press **ATEC Request Settings Snapshot**.
4. Wait for:
   ```text
   SETTINGS_SNAPSHOT_COMPLETE
   ```
   The status should report a fresh `03E8` cache and expose the current room value.
5. Before any write, record the current `ATEC Room Setpoint Current`.
6. Change the experimental setpoint by only **1 °C**, staying inside the 20–30 °C guard.
7. A positive result requires:
   ```text
   WRITE_CONFIRMED reg=03F4 ... extraDeltaWords=0
   ```
   together with zero parser resyncs, zero RX drops and zero peer responses.
8. Restore the original room setpoint using the same control after a confirmed test.

Do not stress-test the queue on the first run. First establish that passive preflight, runtime servicing, the manual settings snapshot and one single-step room-setpoint transaction behave exactly as expected.

## Result classification

**COMPLETE / POSITIVE** means the controller republishes `03E8/count14` with exactly the requested `0x03F4` value and no other changed words.

**COMPLETE / NEGATIVE** means the controller republishes the original `0x03F4` value unchanged while the transaction otherwise remains clean.

**COMPLETE / INCONCLUSIVE** is used for a timeout, unexpected page sequence, stale cache, parser/RX integrity problem or any result that does not cleanly establish acceptance or rejection.

A peer responder, unexpected semantic delta or integrity fault is an abort condition, not a reason to widen the experiment.

## What to capture after the first run

Return the log from:

```text
PREFLIGHT_PASSED
```

through the end of the settings snapshot and, if a write was attempted, through the first `WRITE_CONFIRMED`, negative result, timeout or abort marker.

For the first ATEC run, the most useful sequence is therefore:

```text
PREFLIGHT_PASSED
-> SETTINGS_SNAPSHOT_ARMED
-> settings page ACK sequence
-> SETTINGS_SNAPSHOT_COMPLETE
-> ROOM_WRITE_ARM
-> 0708_SELECTOR_TX
-> desired 03E8 page
-> controller 03E8 republish
-> final result
```

## Evidence status

### Observed in supplied external captures

- `0x0F` carries mailbox/settings traffic.
- `0708/count6` participates in selecting desired pages.
- `03E8/count14` is fetched and later republished by the controller.
- `0x03F4` changes in captured room-setpoint round trips.
- broad settings-export and recurring runtime page families are present.

### Strongly supported

- `0x03F4` is the room thermostat / room setpoint field for this ATEC/DHP-AQ-family path.
- a desired-page pull is a more faithful write mechanism than a speculative direct register write.

### Still a hypothesis until ATEC-EXP1 is run

- this ESPHome implementation can replace the absent native responder safely on the target ATEC installation;
- the captured selector and desired-page sequence will be accepted unchanged by that target;
- the controller will adopt the requested `0x03F4` value and republish it exactly.

### Not implemented / not proven

- arbitrary register writes;
- DHW writes;
- calendar functions;
- emulation of the full Thermia Online service;
- ATEC `0x0F FC17` session-response generation;
- portability to every ATEC/iTec/DHP-AQ firmware revision.

---

This branch should remain separate from the XTR canonical experiment history. Cross-model agreement is useful evidence, but ATEC results must not be promoted to locally proven XTR behaviour without an independent XTR confirmation.
