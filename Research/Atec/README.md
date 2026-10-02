# Thermia ATEC / DHP-AQ experimental path

Last updated: **2026-10-02**

> **ATEC-EXP1 — PREPARED / NOT RUN**
>
> The active YAML has been upgraded to an integrated production-style build comparable in structure to XTR Write Beta v4.1, but the ATEC evidence boundary has **not** been widened.

Current active file:

[`thermia_atec_waveshare_atec_exp1_queued_room_setpoint.yaml`](./thermia_atec_waveshare_atec_exp1_queued_room_setpoint.yaml)

AI continuation notes:

[`AI_HANDOVER.md`](./AI_HANDOVER.md)

Strict passive file:

[`../../Read-only/ATEC/thermia_atec_waveshare_readonly_v01.yaml`](../../Read-only/ATEC/thermia_atec_waveshare_readonly_v01.yaml)

## What "v4.1-level" means here

The ATEC file now contains the full passive ATEC/DHP-AQ decoder, persistent validated settings cache, Wi-Fi/API/heap diagnostics, bus health, refrigerant/outdoor/controller telemetry, candidate ATEC settings fields, bounded 120-second raw capture, detailed write/session counters, queue visibility, a 15-minute runtime soak marker and production-style Configuration naming.

It does **not** copy unsupported XTR write functionality.

ATEC still has only one semantic write target:

`03F4` / decimal 1012 / `03E8` page word12 / room setpoint.

XTR-only R1/session recovery, multi-page semantic controls and EXP383 candidate writes are intentionally absent.

## Experiment hypothesis

With the native Online/DCM responder absent, the target ATEC/DHP-AQ controller may accept the captured page-oriented room-setpoint flow:

```text
controller -> 0x0F FC03 0708/count6
ESP        -> 0000 0001 0000 0001 0000 0000

controller -> 0x0F FC03 03E8/count14
ESP        -> fresh cached 14-word page with ONLY 03F4 changed

controller -> 0x0F FC16 03E8/count14
ESP        -> standard address/count ACK
decision   -> compare the authoritative controller republish
```

A transport ACK is never treated as semantic success.

## Important snapshot correction

The previous prepared ATEC file expected 32 ordered pages after the captured broad refresh bitmap.

Direct raw comparison shows the exact bitmap:

```text
0000 0000 FFFF 867F 03DF 0000
```

selects **26 configuration pages**, not all 32.

The raw capture sequence after that bitmap is consistent with the W2:W3 page map and skips:

```text
047E
0492
04D8
04F6
050A
051E
```

ATEC-EXP1 v0.2 therefore ACKs the exact selected 26-page sequence:

```text
03E8/14 03FC/11 0410/22 042E/15 0442/13 0456/12 046A/18
04A6/13 04BA/22 0532/18
0546/20 055A/33 057B/33 059C/33 05BD/33 05DE/33 05FF/33
0620/33 0641/33 0662/33 0683/33 06A4/33 06C5/33
06EA/7 06F1/3 06F4/19
```

Runtime pages may interleave and are handled separately.

The transmitted refresh bitmap itself has not changed.

## Active wire scope

ATEC-EXP1 may transmit only:

- the dominant captured six-zero `0708` idle response;
- the exact captured 26-page settings-refresh bitmap, manually armed;
- the exact captured `03E8` desired-page selector;
- a desired `03E8/count14` page reconstructed from the latest authoritative controller page with only word12 changed;
- standard FC16 address/count ACKs for exact whitelisted runtime/configuration page shapes.

It does **not** transmit an FC17 response.

Across the two primary gateway logs there are 163 exact `071C/0730` challenges and six exact responses, but no reusable challenge-response transform is known.

## Runtime qualification

Before a semantic write can arm, the integrated build now requires:

- active stage40 runtime;
- at least one known FC16 ACK;
- at least one `0708` reply;
- zero unknown `0x0F FC16` frames;
- zero unknown `0x0F FC03` requests;
- zero peer-responder frames;
- zero parser-resync delta;
- zero RX-buffer-drop delta;
- fresh `03E8/count14` cache <=60 s.

This is stricter than the earlier prepared file.

## Home Assistant

Experimental controls are under **Configuration**:

- **02 Heating | 00 Room Setpoint (ATEC EXP1)** — 20..30 °C, integer step;
- **ATEC | Request Settings Snapshot** — manually arms the exact captured 26-page refresh;
- **ATEC | Abort Experimental TX** — immediately disables experimental TX and returns DE LOW;
- **Log 120 Seconds** — logging only; never transmits.

The active build also exposes passive ATEC/DHP-AQ monitoring and diagnostic counters comparable to the mature XTR build.

## Safety / abort

Any external `0x0F` responder, parser/RX integrity delta, unexpected `0x0F` request/page, stale cache, timeout, or republish with an extra changed word disables or stops the semantic path.

Unknown traffic is capture-only.

FC17 is capture-only.

The current room write keeps the observed 20..30 °C guard and modifies only `03F4`.

## First live run

Do not begin by moving the room slider.

1. Boot and wait for:
   ```text
   PREFLIGHT_PASSED peer=0 busFresh=1 ENTER_STAGE40 DE=LOW
   ```
2. Confirm runtime becomes qualified with no unknown/peer/integrity counters.
3. Press **ATEC | Request Settings Snapshot**.
4. Require:
   ```text
   SETTINGS_SNAPSHOT_COMPLETE pages=26
   ```
5. Record current `03F4`.
6. Only if clean, request a **1 °C** change.
7. Wait for one terminal result.
8. If positive, restore the original room value using the same path.

ATEC-EXP1 remains **PREPARED / NOT RUN** until a live target log is supplied.

## Validation performed for this revision

Static checks performed before publication:

- every `id(...)` reference resolves to a defined ESPHome ID;
- no duplicate ESPHome IDs;
- one top-level UART/globals/sensor/binary_sensor/text_sensor/script/button/number/interval section;
- exactly one UART `write_array()` call;
- exactly one DE `turn_on()` path, inside the guarded TX helper;
- DE retains `restore_mode: ALWAYS_OFF`;
- exact captured `0708` bitmap and `03E8` selector are retained;
- no hard-coded FC17 response frame is present.

ESPHome compile verification is **not** claimed.
