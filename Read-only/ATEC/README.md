# Thermia ATEC — read-only ESPHome

This folder contains the **passive RX-only** Thermia ATEC variant of the ESPHome decoder.

Use:

[`thermia_atec_waveshare_readonly_v01.yaml`](./thermia_atec_waveshare_readonly_v01.yaml)

**Status:** `ATEC READ-ONLY v01 — CANDIDATE / PASSIVE`

This is intentionally separate from the active ATEC research under [`Research/Atec/`](../../Research/Atec/). Nothing in this folder is intended to emulate Thermia Online/DCM or change a heat-pump setting.

## Safety boundary

This build is strictly receive-only on the Thermia RS485 bus:

- RX is configured on GPIO18;
- GPIO21 / DE is forced LOW;
- GPIO17 / TX is **not configured**;
- there is no Modbus polling;
- there is no FC16 ACK generation;
- there is no FC03 response generation;
- there is no FC17 response/replay;
- there is no DCM/Online emulation;
- there are no Thermia write controls.

The **Log 120 Seconds** Home Assistant button only increases ESP logging for a bounded 120-second window. It does not transmit anything on RS485.

## Why this version exists

The repository already contains a passive Danfoss DHP-AQ compatibility profile. The ATEC work and supplied genuine gateway/DCM captures show substantial family overlap, so this v01 intentionally reuses that mature receive-only parser rather than rebuilding the decoder from the experimental write YAML.

The ATEC-facing identity and documentation have been separated so an ATEC installation can use a clearly named read-only baseline while the active protocol research remains isolated in `Research/Atec/`.

Internal IDs with names such as `dhpaq_...` are intentionally retained from the shared passive parser to avoid unnecessary implementation changes. They do not imply that every candidate mapping has been proven on every ATEC unit.

## Evidence level

The decoder contains a mixture of:

- shared Thermia/Danfoss mappings supported across models;
- DHP-AQ / ATEC-family candidate mappings from supplied captures;
- raw diagnostic fields whose exact physical meaning is still open.

Do not infer proof from an entity name alone.

In particular, the wider ATEC research strongly supports `0x03F4` / decimal 1012 as the room thermostat / room-setpoint field in the native page-based Online/DCM path. This read-only build only publishes that value when a genuine controller-originated `0x0F FC10 03E8/count14` page is observed. It never requests or modifies the page.

The current active ATEC research also maps `0x041D` / decimal 1053 as a DHW-start candidate from external evidence. This read-only v01 does **not** promote that field into an active control and does not add a write path for it.

## Hardware profile

The YAML targets the same Waveshare ESP32-S3 RS485 hardware used by the project:

```text
UART: 9600 baud, 8E1
RX:   GPIO18
DE:   GPIO21, LOW
TX:   not configured
```

The GPIO assignments are implementation settings for this board, not a claim that every ATEC exposes identical external wiring.

When passively attaching the Waveshare board to an already terminated Thermia bus, keep the Waveshare 120-ohm termination jumper open/off unless the actual installation requires otherwise.

## Home Assistant

The passive decoder exposes the shared Thermia monitoring entities plus the DHP-AQ/ATEC-family candidate diagnostics present in the existing compatibility parser.

Examples include:

- heating/settings values when their native pages are observed;
- room and outdoor temperature-related values;
- compressor/fan/context indicators where supported by observed traffic;
- DHP-AQ/ATEC-family refrigerant-control candidates from slave `0xA5`;
- bus-health and ESP diagnostics;
- bounded **Log 120 Seconds** capture control.

Some candidate and raw diagnostic entities are deliberately disabled by default or conservatively named.

## Important limitation without an Online/DCM module

A read-only ESP can only decode traffic that already exists on the bus.

If the native Online/DCM module is absent, some `0x0F` request/response or settings-export traffic may never occur naturally. In that case, corresponding Home Assistant entities can remain unknown even though their mapping is known from genuine gateway captures.

That is expected behaviour for a passive build. Do not add active responses to this file to "fix" missing data; active DCM emulation belongs only in the research/write branch.

## Capture workflow

For passive mapping, open the ESPHome device logs first and then press **Log 120 Seconds** under Home Assistant Configuration.

The useful block is bracketed by:

```text
ATEC-CAPTURE START
...
ATEC-CAPTURE END
```

Return the complete START-to-END block. A full CRC-valid raw capture is more useful than isolated sensor values because it allows page boundaries, request/response pairing and cross-model differences to be checked.

## Relationship to active ATEC research

Active research files live in:

- [ATEC README](../../Research/Atec/README.md)
- [ATEC AI handover](../../Research/Atec/AI_HANDOVER.md)
- [ATEC-EXP1 YAML](../../Research/Atec/thermia_atec_waveshare_atec_exp1_queued_room_setpoint.yaml)

ATEC-EXP1 is currently **PREPARED / NOT RUN**. Its transmit/emulation code is deliberately **not** included in this read-only build.

Keep the boundary explicit:

```text
Read-only/ATEC/   = passive monitoring only
Research/Atec/    = experimental protocol work
```

## Validation status

This v01 is derived from the existing passive candidate v02 with only ATEC-facing identity/documentation/log-label changes and an explicit safety note.

Static safety checks performed before publication:

- no `tx_pin:` in the YAML;
- no UART `write_array()` call;
- no DE `turn_on()` call;
- GPIO21 uses `restore_mode: ALWAYS_OFF`;
- RX remains GPIO18.

It has **not** been ESPHome compile-verified in this environment and has not yet been confirmed on the target ATEC installation.

If a live ATEC log contradicts one of the candidate mappings, preserve the raw observation and demote or relabel the candidate rather than forcing it to match the current profile.
