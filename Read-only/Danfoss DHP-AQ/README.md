# Danfoss DHP-AQ / Thermia ATEC research

This folder is a **separate read-only sidetrack** for mapping older Danfoss DHP-AQ / Thermia ATEC-family bus traffic.

It does **not** replace the XTR M integration and it does **not** advance the main XTR experiment sequence.

The research YAML is derived directly from the repository root file:

`thermia_itec_xtr_m_waveshare_public_v27.yaml`

and deliberately preserves its known-good passive decoding while adding a broader mapper.

## DHP-AQ candidate compatibility profile v02

For normal passive use on the captured DHP-AQ topology, use:

`danfoss_dhp_aq_waveshare_candidate_v02.yaml`

This **replaces v01**. It is still derived from the repository-root
`thermia_itec_xtr_m_waveshare_public_v27.yaml`, but incorporates the
offline MAP02/MAP03 analysis of the supplied IDLE and DHW captures.

**Status:** `DHP-AQ-PROFILE02 — CANDIDATE / PASSIVE`

No active Thermia-bus functionality is added: GPIO17 TX remains unconfigured,
GPIO21/DE remains forced LOW, and there is no Modbus polling, scanning,
injection, emulation or heat-pump write control.

### What changed from candidate v01

- `A5:0000` is no longer published as bar; it remains a pressure-like raw candidate because the physical unit/scaling is not proven.
- `A5:0007` is strengthened: across the available captures it closely follows `0001 - 0005`, supporting the superheat interpretation.
- `A5:0006` is retained as a target-like candidate for that control relationship.
- `A5:0008` is now a raw refrigerant-control output / EXV candidate, not a proven percentage.
- passive FC06 parsing is added so the observed `A5:0023` clear/echo sequence is preserved.
- `A5:0023` is exposed as an event/latch/handshake candidate.
- `ABF4` is treated as a context/status word; its `0x02` bit is exposed separately.
- `ABF6` is kept raw and is **not** published as a commanded temperature.
- `A80E -> AFDC` is documented as periodic sync/housekeeping correlation, not operating mode.
- `A812`, `ABF7`, `AC29` and `AFE0` are retained as raw packed-word candidates; `0x050D = 1293` is no longer interpreted as 12.93 °C.
- `A7F8/A7F9` remain water-side supply/return candidates pending a third operating state or service-screen cross-check.
- a Home Assistant **Log 120 Seconds** Configuration button enables a bounded raw-capture window.

### Candidate register table after MAP03

| Slave / function | Register | Current interpretation | Scaling / values | Evidence status |
|---|---:|---|---|---|
| `0x02 FC17-R` | `A7F8` | Supply / water-side temperature candidate | °C | **CANDIDATE+** |
| `0x02 FC17-R` | `A7F9` | Return / water-side temperature candidate | °C | **CANDIDATE+** |
| `0x02 FC17-R` | `A7FB` | DHW upper temperature | °C | shared mapping |
| `0x02 FC17-R` | `A7FC` | DHW temperature | °C | shared mapping |
| `0x02 FC17-R` | `A802` | Outdoor temperature | °C | shared mapping |
| `0x02 FC17-W` | `A80C bit 0x40` | Compressor running | bit | cross-model confirmed; local IDLE/DHW consistent |
| `0x02 FC17-W` | `A80C bit 0x01` | DHW request/context | bit | cross-model confirmed; local IDLE/DHW consistent |
| `0x02 FC17-W` | `A80E bit 0x20` | Periodic controller/accessory sync/housekeeping | bit | **PROVEN correlation** to delayed AFDC |
| `0x02 FC17-W` | `A812` | packed/base context candidate | raw, observed `0x0500` | **HYPOTHESIS** |
| `0x04 FC17-R` | `ABE2` | Discharge-pipe temperature | °C | **STRONG CANDIDATE** |
| `0x04 FC17-W` | `ABF4` | Context/status word | `4 -> 6`; bit `0x02` becomes active | **STRONG CANDIDATE** |
| `0x04 FC17-W` | `ABF6` | Outdoor command/limit/target-like word | `0 -> 63` during DHW | **CANDIDATE / RAW** |
| `0x04 FC17-W` | `ABF7` | packed context candidate | raw, observed `0x050D` | **HYPOTHESIS** |
| `0x05 FC17-W` | `AC29` | packed context candidate | raw, observed `0x050D` | **HYPOTHESIS** |
| `0x06 FC17-W` | `AFDC bit 0x20` | delayed sync/housekeeping propagation | ~1.5 s after A80E in supplied logs | **PROVEN correlation** |
| `0x06 FC17-W` | `AFE0` | packed context candidate | raw, observed `0x050D` | **HYPOTHESIS** |
| `0x0A FC17-W` | `B3C6` | context/status word; `0 -> 2` in DHW | raw/bit-like | **CANDIDATE** |
| `0xA5 FC03-R` | `0000` | pressure-like process value | **RAW; unit/scale unknown** | **CANDIDATE+** |
| `0xA5 FC03-R` | `0001` | Suction-gas temperature candidate | ÷10 °C | **STRONG CANDIDATE** |
| `0xA5 FC03-R` | `0004` | refrigerant-controller context/state | `0`, startup `4`, active `2` observed | **CANDIDATE+** |
| `0xA5 FC03-R` | `0005` | Evaporation/saturation temperature candidate | ÷10 °C | **STRONG CANDIDATE** |
| `0xA5 FC03-R` | `0006` | Superheat/control target candidate | ÷10 K | **STRONG CANDIDATE** |
| `0xA5 FC03-R` | `0007` | Superheat candidate | ÷10 K; closely matches `0001 - 0005` | **VERY STRONG CANDIDATE** |
| `0xA5 FC03-R` | `0008` | Refrigerant control output / EXV candidate | raw; 0 idle, ~45–53 DHW | **CANDIDATE+** |
| `0xA5 FC03-R` | `000A` | refrigerant-control active flag | 0/1 | **STRONG CANDIDATE** |
| `0xA5 FC03/FC06` | `0023` | event/latch/handshake candidate | read 1, then clear/echo 0 observed | **STRONGLY SUPPORTED** |
| `0x0F FC10` | `03E8..` | Heating/settings block | existing public-v27 mapping | shared / already working |

### 120-second log button

The v02 device exposes **Log 120 Seconds** under the Home Assistant device
**Configuration** section. Pressing it does **not** send anything to the heat
pump. It only makes the ESP emit every complete CRC-valid frame at WARN level
for 120 seconds using the tag `dhpaq_capture`.

The output is bracketed by:

```text
[W][dhpaq_capture] DHP-AQ-CAPTURE START duration=120s ...
[W][dhpaq_capture] DHP-AQ-CAPTURE RAW t=... frame=... len=...: ...
...
[W][dhpaq_capture] DHP-AQ-CAPTURE END duration=120s frames=...
```

**Important:** the ESP does not archive this log window. Open the ESPHome device
log stream (ESPHome Device Builder / device logs, or `esphome logs`) **before**
pressing the Home Assistant button. Wait for the END marker, then save/copy the
complete START-to-END block.

Pressing the button again while a capture is running restarts the 120-second
window and resets its frame counter.

For future mapping, the most valuable next capture is about 120 seconds of
**stable space heating**. Also record, if available, the service-screen values
for supply, return, outdoor temperature, DHW temperature, evaporation
pressure/temperature, superheat or EXV around the same time.

### What remains intentionally unmapped

The available IDLE + DHW data does not support a reliable numeric mapping for
compressor current, fan RPM, high-side pressure or XTR-style compressor
frequency. These are not force-filled with guesses.

The exact physical semantics of `A5:0000`, `A5:0008`, `ABF6`,
`ABE0/ABE1/ABE4`, the packed `A812/ABF7/AC29/AFE0` words and the exact
A7F8/A7F9 supply/return ordering remain open.

### Success / negative / abort criteria

Success means the candidate entities remain plausible, known settings/room
entities continue working, the 120-second capture produces complete CRC-valid
frames, and `Bus Healthy` remains stable.

A negative result is any candidate that behaves incompatibly with its proposed
quantity. Keep the raw value and demote the semantic label rather than forcing
the map.

Abort the logging run if repeated CRC-resync/drop warnings appear,
`Bus Healthy` repeatedly falls false while native traffic is present, or ESP
stability degrades. The button itself is receive-only and has no intended
heat-pump state effect.

---

## DHP-AQ-MAP02

**Status:** `COMPLETE / POSITIVE`

**Hypothesis:** IDLE-versus-DHW statistical comparison of the two existing
captures can reduce the unknown register set without a new live experiment.

**Controlled change:** none on the heat pump or bus; offline analysis only.

MAP02 established the coherent `0xA5` operating block, strengthened the
`0001/0005/0007` temperature-difference relationship, identified
`A5:0023` as a controller-cleared latch/handshake candidate and separated
several active-state candidates from housekeeping traffic.

---

## DHP-AQ-MAP03

**Status:** `COMPLETE / POSITIVE`

**Hypothesis:** causal timing, arithmetic relationships and propagation delays
within the same two captures can distinguish measurement, target, control
output and protocol housekeeping more reliably than simple state correlation.

**Controlled change:** none on the heat pump or bus; offline analysis only.

Key MAP03 refinements:

- `A5:0007 ≈ A5:0001 - A5:0005` is highly repeatable across the available data.
- `A5:0006` behaves target-like relative to that derived value.
- `A5:0000` is pressure-like, but bar scaling is **not proven**.
- `A5:0008` is clearly an active control/load-like output, but EXV % is **not proven**.
- `ABF6=63` is not sufficient evidence for a 63 °C commanded target and is kept raw.
- `A80E bit 0x20 -> AFDC bit 0x20` is a periodic delayed sync/housekeeping path.
- `0x050D = 1293` at ABF7/AC29/AFE0 is treated as a packed-word candidate, not 12.93 °C.
- the shared `0x02` context visible in A5 state / B3C6 / ABF4 is retained as a candidate until a third operating state can separate DHW-specific from generic-active meaning.

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

MAP01 already produced the initial IDLE/DHW evidence. For new collaborator captures, prefer the bounded `Log 120 Seconds` workflow in candidate v02 rather than leaving DEBUG raw logging enabled continuously.

Do not change heat-pump settings just to generate traffic.

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
