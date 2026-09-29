# Danfoss DHP-AQ / Thermia ATEC research

This folder is a **separate read-only sidetrack** for mapping older Danfoss DHP-AQ / Thermia ATEC-family bus traffic.

It does **not** replace the XTR M integration and it does **not** advance the main XTR experiment sequence.

The research YAML is derived directly from the repository root file:

`thermia_itec_xtr_m_waveshare_public_v27.yaml`

and deliberately preserves its known-good passive decoding while adding a broader mapper.

## DHP-AQ candidate compatibility profile v01

For normal passive use on the captured DHP-AQ topology, start with:

`danfoss_dhp_aq_waveshare_candidate_v01.yaml`

This file is derived directly from the repository-root
`thermia_itec_xtr_m_waveshare_public_v27.yaml` and keeps the same Waveshare
ESP32-S3, Wi-Fi/API/OTA, bus-health, heating-settings and room-sensor
functionality. It adds only passive DHP-AQ decoding.

**Status:** `DHP-AQ-PROFILE01 — CANDIDATE / PASSIVE`

**Hypothesis:** the older DHP-AQ exposes useful refrigerant/outdoor-unit data
through slave `0xA5` FC03 and slave `0x04` FC17 instead of the XTR M
`0x1E` live-telemetry layout, while the controller/settings blocks remain
partly shared.

**Controlled change from root public v27:** FC03 context/decoding is added for
the observed `0xA5` block; the 13-word DHP-AQ `0x02:A7F8` block is decoded;
candidate `0x04:ABE0/ABF4` fields and `0x02:A80C` bits are exposed. No TX,
polling, scan, emulation or write path is added.

### Candidate register table

The table deliberately uses **CANDIDATE** where the two available captures are
not enough for a service-screen proof. "Cross-model confirmed" means the
semantic bit/register has independent DHP-AQ/iTec Eco evidence but was not
independently toggled on this exact unit.

| Slave / function | Register | Candidate meaning | Scaling / values | Evidence status |
|---|---:|---|---|---|
| `0x02 FC17-R` | `A7F8` | Supply temperature | °C | shared mapping; locally plausible |
| `0x02 FC17-R` | `A7F9` | Return temperature | °C | **CANDIDATE** |
| `0x02 FC17-R` | `A7FB` | DHW upper temperature | °C | shared mapping |
| `0x02 FC17-R` | `A7FC` | DHW temperature | °C | shared mapping |
| `0x02 FC17-R` | `A802` | Outdoor temperature | °C | shared mapping |
| `0x02 FC17-W` | `A80C bit 0x40` | Compressor running | bit | cross-model confirmed; local idle/DHW consistent |
| `0x02 FC17-W` | `A80C bit 0x01` | DHW request/context | bit | cross-model confirmed; local idle/DHW consistent |
| `0x04 FC17-R` | `ABE2` | Discharge-pipe temperature | °C | **STRONG CANDIDATE**; ~17/20 → 64 during DHW |
| `0x04 FC17-W` | `ABF4` | Outdoor-unit mode/request | `4` idle, `6` DHW observed | **CANDIDATE** |
| `0x04 FC17-W` | `ABF6` | Commanded target candidate | `0` idle, `63` DHW observed | **CANDIDATE** |
| `0xA5 FC03-R` | `0000` | Evaporation pressure | ÷10 bar | **CANDIDATE** |
| `0xA5 FC03-R` | `0001` | Suction-gas temperature | ÷10 °C | **STRONG CANDIDATE** |
| `0xA5 FC03-R` | `0005` | Evaporation temperature | ÷10 °C | **STRONG CANDIDATE** |
| `0xA5 FC03-R` | `0006` | Superheat target | ÷10 K | **CANDIDATE** |
| `0xA5 FC03-R` | `0007` | Superheat | ÷10 K | **STRONG CANDIDATE**; closely tracks `0001 - 0005` |
| `0xA5 FC03-R` | `0008` | EXV opening | % | **STRONG CANDIDATE**; 0 idle, ~45–53 during DHW |
| `0xA5 FC03-R` | `000A` | EXV/control active flag | 0/1 | **CANDIDATE** |
| `0x0F FC10` | `03E8..` | Heating/settings block | existing public-v27 mapping | shared / already working |

### What remains intentionally unmapped

The two supplied captures do **not** support a reliable numeric mapping for
compressor current, fan RPM, high-side pressure or XTR-style compressor
frequency. Those existing public-v27 entities are therefore not force-filled
with guessed DHP-AQ values. Raw `ABE0`, `ABE1`, `ABE2`, `ABE4`,
`ABF4` and `ABF6` diagnostics are kept so later evidence can refine them.

The profile also keeps the original XTR `0x1E` decoder as a harmless fallback:
on the supplied DHP-AQ captures no `0x1E` live block was present, so it does
not populate those entities.

### Success / negative / abort criteria

Success means the candidate entities populate with plausible values while the
known public-v27 room/settings entities continue working and `Bus Healthy`
remains stable. A negative result is any candidate that behaves incompatibly
with its proposed physical quantity; keep the raw value and demote the label
rather than forcing the mapping. Abort and revert to the previous passive build
if repeated CRC-resync/drop warnings appear, `Bus Healthy` repeatedly falls
false while native traffic is present, or ESP stability degrades.

---

## DHP-AQ-MAP01

**Experiment:** `DHP-AQ-MAP01`  
**Status:** `COMPLETE / POSITIVE` — the supplied IDLE and DHW logs identified the DHP-AQ-specific `0xA5` FC03 and `0x04` FC17 families and supported creation of the candidate compatibility profile.

**Hypothesis:** the DHP-AQ / ATEC shares the same legacy 9600 baud, 8E1, Modbus-RTU-like bus family and part of the same settings/register namespace as the iTec XTR M, but some live operating telemetry uses a different slave/register/block layout. A passive census should reveal the differences.

This was motivated by a DHP-AQ installation where heating configuration values decode correctly while several live values remain `Unknown`, including compressor frequency/current, high pressure, fan speed, condenser temperatures, SG mode and operating state.

## File

Use:

`danfoss_dhp_aq_waveshare_research_map01.yaml`

The build is intended for the **Waveshare ESP32-S3-RS485-CAN / CAN-U** hardware used by the main project.

Default ESPHome identity:

- device name: `danfoss-dhp-aq-research`
- friendly name: `Danfoss DHP-AQ Research`

Change these through the `substitutions:` block if needed.

## Safety

This build is deliberately **receive-only**:

- RS485 RX: GPIO18
- RS485 DE/direction: GPIO21, held LOW
- GPIO17 TX is **not configured**
- no Modbus master polling
- no register scan
- no injection
- no write controls
- no room-sensor emulation

The mapper only observes traffic that the heat-pump system itself already puts on the bus.

Keep the Waveshare 120-ohm termination jumper **OFF/open** when passively attaching to an already terminated bus, as with the main project setup.

## What changed versus public v27

Only research/mapping behaviour was added:

- all existing public-v27 decoded entities remain;
- CRC-valid raw frames are logged as `dhpaq_raw`;
- FIRST and CHANGE events are logged by a generic register mapper;
- first-seen frame/block layouts are logged once;
- FC03 response mapping is added;
- passive FC06 observation is added if it exists on the bus;
- FC04, FC10 and FC17 mapping from public v27 is retained;
- the stream assembler accepts standard Modbus slave IDs `1..247`, so DHP-AQ-specific nodes such as `0x01`, `0xA5` or `0xA6` are not discarded.

No known-good production decoding was intentionally removed.

## Log convention

The useful experiment messages are deliberately warning-level so they stand out visually in ESPHome logs:

```text
[W][dhpaq_shape] DHP-AQ-MAP01 SHAPE slave=0x04 FC04 request start=0x0000 count=...
[W][dhpaq_map]   DHP-AQ-MAP01 FIRST  src=FC04-R slave=0x04 reg=0x0014 value=...
[W][dhpaq_map]   DHP-AQ-MAP01 CHANGE src=FC04-R slave=0x04 reg=0x0014 ... -> ...
```

The complete CRC-valid frames are also available at DEBUG level:

```text
[D][dhpaq_raw] DHP-AQ-MAP01 RX ... bytes: ...
```

### Mapper source labels

| Label | Meaning |
|---|---|
| `FC03-R` | holding-register read response |
| `FC04-R` | input-register read response |
| `FC06` | single-register write/echo observed on the bus |
| `FC10-W` | multiple-register write observed on the bus |
| `FC17-W` | FC17 write portion sent by the existing controller/master |
| `FC17-R` | FC17 read response |

These labels describe **observed bus direction/function**, not commands generated by the ESP.

## Suggested first capture

For the first mapping run, do not change heat-pump settings just to generate traffic.

Capture:

1. about **60–120 seconds while idle**, if practical;
2. about **60–120 seconds while the compressor is already running**;
3. optionally a normal heating-to-DHW or DHW-to-heating transition if one occurs naturally.

Save the **complete ESPHome log**, not only the `dhpaq_map` lines. The raw frames are needed to verify block boundaries and request/response pairing.

Also note, if known:

- exact DHP-AQ / ATEC model;
- controller/software version;
- whether the compressor was idle, heating or producing DHW;
- any displayed compressor/fan/current/temperature values that can be used as correlation anchors.

## Success criteria

MAP01 succeeds if the capture lets us do one or more of the following without transmitting:

- identify DHP-AQ-specific slave IDs or block shapes;
- find live values that correlate with the currently `Unknown` Home Assistant entities;
- confirm that an XTR register exists on DHP-AQ but at another address/scale;
- show that a value is not present in the observed internal traffic and should not be expected from the current parser.

A negative result is also useful: if a full operating capture contains no candidate for a particular value, record that rather than inventing a register.

## Stop criteria

Stop the capture and revert to the normal read-only build if:

- `Bus Healthy` repeatedly becomes false while the Thermia bus itself is active;
- repeated CRC-resync/drop warnings appear;
- ESP stability degrades under DEBUG logging.

MAP01 contains no active bus experiment, so there is no intended heat-pump state change.

## Existing cross-model evidence

The wider project already has evidence that DHP-AQ/iTec generations share important protocol behaviour, but mappings must still be verified on the actual unit. In particular, an independent iTec Eco / DHP-AQ capture strongly supports the outdoor-unit `0x0014` status word as a bitfield containing compressor/fan/flow information.

Treat all other XTR-specific live telemetry offsets as hypotheses until a DHP-AQ capture confirms them.
