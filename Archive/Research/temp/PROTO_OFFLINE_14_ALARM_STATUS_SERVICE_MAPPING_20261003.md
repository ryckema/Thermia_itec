# Thermia iTec XTR M — Alarm / status / service-data mapping

**Date:** 2026-10-03  
**Track:** PROTO-OFFLINE-14  
**Status:** COMPLETE / POSITIVE — offline analysis only  
**Original plan item:** #5 — alarms/status/service-data mapping  
**Baseline:** PROTO-OFFLINE-09 scheduler map + PROTO-OFFLINE-13 cross-topology runtime normalisation + firmware-derived DHP/HE alarm layer  
**Controlled change:** no device change. Correlate the native `0x0F` service pages, local XTR stage-40 captures, genuine legacy Online/DCM captures, genuine Eco5 + Online captures, the XTR commissioning-manual ALARM menu, and firmware-derived DHP/HE alarm/status semantics.  
**Device TX introduced by this analysis:** none  
**YAML change:** none  
**Heat-pump restart:** none  
**Setting write:** none  
**GitHub change:** none  
**Live experiment status:** unchanged — EXP388 remains RUNNING / PARTIAL

> Important provenance note: local XTR `0884/count60` examples below were captured while the ESP was already servicing/ACKing the emulated Online/DCM runtime. The `0884` payload itself is nevertheless controller-originated local-XTR data. This analysis does not call those captures passive.

---

## Hypothesis

The native Online/DCM runtime/service family contains separate layers for:

1. timestamped historical alarm/service events;
2. current operating/status state;
3. current alarm/error state at the abstract DHP/HE integration layer.

The primary candidate for timestamped history is:

```text
0x0F FC16 0884/count60
```

The analysis tests whether its payload has a stable record structure across topology generations and whether that structure matches the official XTR ALARM menu closely enough to call it an alarm-history export without inventing individual code meanings.

**Result:** strongly supported. `0884/count60` is proven to be a timestamped rolling service-history page and very strongly supported as the Online/DCM alarm-history export. Its internal record ABI changes by generation.

---

# 1. Scheduler role of `0884`

PROTO-OFFLINE-09 mapped:

```text
0708 W4 bit10 -> 0884
```

So `0884` belongs to the runtime/service-page scheduler.

The older Online/DCM steady-state mask includes bit10, while the Eco5 forced-refresh mask can omit bit10; this explains why the page is not equally frequent in all captures.

`0884` therefore belongs to the same integration-facing service namespace as:

```text
07D0 ... 0870
```

but its payload is much more history-like than live telemetry.

---

# 2. Official XTR semantic anchor

The normalized 2024 iTec XT/XTR commissioning manual describes:

```text
INFORMATIE -> ALARM

history_depth: 10
fields:
- alarm_name
- time
- date
```

This is used only as a semantic anchor.

It does **not** provide a Modbus register address and must not be treated as proof that `0884` is the exact menu backing store.

---

# 3. Legacy genuine Online/DCM `0884` ABI — exact 10 × 6-word history

Across the four older genuine Online/DCM reference captures, all complete `0884/count60` payloads are byte-identical.

The 60 words split exactly as:

```text
10 records × 6 words
```

with record format:

```text
word0  raw event/alarm identifier
word1  minute
word2  hour
word3  day
word4  month
word5  year (two digits)
```

Representative decode:

| # | Raw ID | Time | Date |
|---:|---:|---:|---:|
| 0 | `0x0002` | 10:47 | 27-08-2026 |
| 1 | `0x0029` | 10:28 | 27-08-2026 |
| 2 | `0x002A` | 10:28 | 27-08-2026 |
| 3 | `0x0002` | 10:05 | 27-08-2026 |
| 4 | `0x0029` | 10:05 | 27-08-2026 |
| 5 | `0x002A` | 10:05 | 27-08-2026 |
| 6 | `0x002C` | 10:04 | 27-08-2026 |
| 7 | `0x002C` | 09:43 | 27-08-2026 |
| 8 | `0x002A` | 09:43 | 27-08-2026 |
| 9 | `0x0002` | 09:41 | 27-08-2026 |

The order is newest first.

### Classification

**PROVEN / genuine legacy Online/DCM structural:**

```text
0884/count60 = ten timestamped history records
```

**VERY STRONGLY SUPPORTED semantic interpretation:**

```text
alarm-history export
```

because the native structure is exactly:

```text
10 entries × [identifier + time + date]
```

which independently matches the official XTR ALARM menu shape.

The raw identifiers `2`, `41`, `42`, `44` are **not** assigned alarm names here.

---

# 4. Modern Eco5 `0884` ABI — 8 × 7 words + 4-word trailer

The genuine Eco5 + Online capture contains one complete data-bearing `0884/count60` payload.

It does **not** use the legacy 10×6 ABI.

Instead the 60 words split cleanly as:

```text
8 records × 7 words
+ 4-word trailer
= 60 words
```

Record format:

```text
word0  raw event/alarm field A
word1  raw event/alarm field B
word2  minute
word3  hour
word4  day
word5  month
word6  year (two digits)
```

Decoded records:

| # | Raw A | Raw B | Time | Date |
|---:|---:|---:|---:|---:|
| 0 | `0x002C` | `0x0000` | 14:45 | 26-09-2026 |
| 1 | `0x002C` | `0x0000` | 09:32 | 23-09-2026 |
| 2 | `0x002C` | `0x0000` | 10:00 | 11-09-2026 |
| 3 | `0x002C` | `0x0000` | 11:00 | 04-09-2026 |
| 4 | `0x002C` | `0x0000` | 07:00 | 29-08-2026 |
| 5 | `0x1400` | `0x0000` | 16:44 | 15-08-2026 |
| 6 | `0x0172` | `0x0000` | 09:00 | 14-08-2026 |
| 7 | `0x0019` | `0x0000` | 12:00 | 27-06-2026 |

Trailer:

```text
0000 0000 0000 000F
```

### Classification

**PROVEN / genuine Eco5 + Online structural:**

```text
0884/count60 = 8 timestamped records + 4-word metadata trailer
```

**OPEN:** the distinction between raw field A and raw field B.

Safest current interpretation:

```text
A/B = composite event/alarm identity and/or flags
```

but this is only a hypothesis.

---

# 5. Local XTR M confirmation — same modern 8 × 7 + 4 ABI

A local XTR stage-40 capture contains:

```text
0F 10 0884 003C ...
```

with exactly the same modern geometry as Eco5:

```text
8 × 7-word records
+ 4-word trailer
```

Representative local decode:

| # | Raw A | Raw B | Time | Date |
|---:|---:|---:|---:|---:|
| 0 | `0x002C` | `0x0000` | 12:05 | 01-10-2026 |
| 1 | `0x002C` | `0x0000` | 11:28 | 01-10-2026 |
| 2 | `0x002C` | `0x0000` | 22:00 | 30-09-2026 |
| 3 | `0x002C` | `0x0000` | 20:00 | 30-09-2026 |
| 4 | `0x002C` | `0x0000` | 19:00 | 30-09-2026 |
| 5 | `0x2D00` | `0x0000` | 18:00 | 30-09-2026 |
| 6 | `0x0000` | `0x0000` | 17:00 | 30-09-2026 |
| 7 | `0x001E` | `0x0000` | 17:00 | 30-09-2026 |

Trailer:

```text
0000 0000 0000 0010
```

Later local XTR snapshots show the list rolling forward during 2026-10-01 and 2026-10-02.

Examples of the final trailer word observed in selected local snapshots:

```text
0010
0011
0013
0014
```

while newer timestamped records appear at the front.

### Classification

**PROVEN / locally confirmed on this XTR M:**

- native `0x0F:0884/count60` exists;
- it is a rolling timestamped history structure;
- XTR uses the same 8×7 + 4 modern ABI observed on Eco5;
- newest records occupy the front of the page.

This is the strongest local result in PROTO-OFFLINE-14.

---

# 6. Why `0884` is best called "alarm/service history", not blindly "alarm code table"

The structural match with the manual is very strong:

```text
manual: alarm name + time + date
native: raw identifier(s) + minute + hour + day + month + year
```

But there is one important generation mismatch:

```text
manual UI depth: 10
legacy native ABI: 10 records
modern XTR/Eco5 ABI: 8 records + trailer
```

Possible explanations include:

- modern DCM exports an Online-specific subset of the controller's ten-entry UI history;
- two UI entries are represented through metadata/trailer state;
- modern firmware changed internal history ABI while UI depth remained ten;
- `0884` is a closely related service/event history rather than a byte-for-byte backing store of the UI ALARM list.

The existing corpus cannot distinguish these.

Therefore:

**VERY STRONGLY SUPPORTED:** `0884` is the Online/DCM alarm/service history export.

**NOT YET PROVEN:** `0884` is exactly the complete backing storage for `INFORMATIE -> ALARM`.

A single XTR UI transcription/photo showing the ten alarm-history entries at the same moment as a captured `0884` page would resolve this directly without a write.

---

# 7. Raw history identifiers are not direct XTR `E###` fault numbers

The official XTR manual uses fault names/codes such as:

```text
E111
...
```

while the native history contains values such as:

```text
legacy:
0002
0029
002A
002C

modern:
002C
0019
0172
1400
2D00
```

There is no safe direct numeric conversion from these raw words to the displayed XTR `E###` namespace.

For example, neither:

```text
raw 0x002C -> "E44"
```

nor:

```text
raw 0x002C -> alarm #44
```

is justified by the evidence.

### Classification

**DISPROVEN / SUPERSEDED as a working shortcut:**

> "The first 0884 word is directly the displayed XTR E-number."

The history words are internal/native identifiers or encoded event descriptors whose lookup/translation remains unknown.

Do not expose them in Home Assistant under named alarms until mapped.

---

# 8. Current alarm state exists as a separate firmware-level semantic layer

Recovered Danfoss Link 2.7.42 firmware defines abstract DHP/HE parameters:

```text
0x03F0 ErrorCode     WORD

0x0400 AlarmField1   WORD
0x0401 AlarmField2   WORD
0x0402 AlarmField3   WORD
0x0403 AlarmField4   WORD
0x0404 AlarmField5   WORD
```

These are **abstract DHP/HE ParameterIDs**, not local slave-`0x0F` register addresses.

The HPAQ implementation also contains alarm aggregation logic over these fields.

The project has not recovered the final DCM03 serializer mapping from:

```text
ErrorCode / AlarmField1..5
```

to a specific native `0x0F` page.

### Architectural conclusion

There are at least two distinct concepts:

```text
CURRENT alarm/error state
  -> DHP/HE ErrorCode + AlarmField1..5
  -> native serializer mapping still open

HISTORICAL timestamped events
  -> native 0884/count60
  -> local XTR structure now confirmed
```

Do not conflate them.

---

# 9. Cross-model community evidence supports the current-vs-history split

An older Thermia/Danfoss Modbus map from independent community work exposes:

```text
Operating status 1
Operating status 2
Alarm flag
Alarm group 1
Alarm group 2
```

as live bitfields.

Examples in that older map include live bits for:

```text
compressor
hot-water production
active cooling
passive cooling
alarm
high-pressure pressostat
low-pressure pressostat
sensor faults
```

This is useful **cross-model architecture evidence only**.

It supports the idea that live status/alarm bitfields are distinct from a timestamped history page, but those 400xx addresses and bits are not promoted to XTR `0x0F` mappings.

---

# 10. Current operational-status layer already partially reduced

The native runtime serializer contains several live status representations that are not alarm history.

Examples already established in genuine Eco5 traffic:

```text
07F4 = normalized operating-state summary
  0 -> inactive/idle class
  4 -> one captured startup/ramp class
  6 -> compressor-running class

083C = startup/pre-run transition code

0845 = combined outdoor command-state export

0865 = compressor-running Boolean

0866 = start-pending / commanded-but-not-yet-running indicator
```

These should be modelled as **live operating status**, not alarms.

This gives the Online/DCM runtime model at least three semantic layers:

```text
LIVE OPERATING STATUS
    07F4 / 083C / 0845 / 0865 / 0866 / ...

CURRENT ALARM STATE
    DHP/HE ErrorCode + AlarmField1..5
    native 0x0F bridge not yet recovered

HISTORICAL SERVICE/ALARM EVENTS
    0884/count60
```

---

# 11. `085F/count5` is not identified as an alarm page

`085F/count5` is a confirmed runtime/service scheduler page and is important to the session lifecycle.

However, in many local XTR stage-40 captures its payload is:

```text
0000 0000 0000 0000 0000
```

and the same all-zero shape is common in genuine reference traffic.

That makes it tempting to call it "current alarm fields", but there is no edge evidence to justify that.

### Classification

**PROVEN / structural:**
- `085F/count5` is a native runtime/service page;
- it participates in scheduler/service progression.

**OBSERVED locally:**
- all five words are zero in the sampled normal XTR runtime.

**OPEN:**
- semantic meaning of each word;
- whether any field becomes nonzero under alarm, service or another state.

Do not map the five firmware AlarmFields directly onto `085F` merely because the count also happens to be five.

That numerical coincidence alone is insufficient.

---

# 12. Modern `0884` trailer

Modern XTR/Eco5 layout:

```text
08BC
08BD
08BE
08BF
```

is outside the eight 7-word records.

Observed:

```text
Eco5 representative trailer:
0000 0000 0000 000F

local XTR selected snapshots:
0000 0000 0000 0010
0000 0000 0000 0011
...
0000 0000 0000 0013
0000 0000 0000 0014
```

The changing last word correlates qualitatively with the history list advancing.

### HYPOTHESIS

`08BF` may be:

- a history generation counter;
- ring-buffer sequence/index;
- event serial/revision.

But the evidence does not distinguish these.

Do not call it "entry count" because the page always contains eight record slots while `08BF` exceeds eight.

`08BC..08BE` remain zero in the inspected examples and their semantics are OPEN.

---

# 13. Record-address map

## Legacy ABI

```text
record0  0884..0889
record1  088A..088F
record2  0890..0895
record3  0896..089B
record4  089C..08A1
record5  08A2..08A7
record6  08A8..08AD
record7  08AE..08B3
record8  08B4..08B9
record9  08BA..08BF
```

No trailer.

## Modern XTR/Eco5 ABI

```text
record0  0884..088A
record1  088B..0891
record2  0892..0898
record3  0899..089F
record4  08A0..08A6
record5  08A7..08AD
record6  08AE..08B4
record7  08B5..08BB

trailer  08BC..08BF
```

This is a concrete generation-specific ABI change hidden behind the **same**:

```text
0884/count60
```

page envelope.

That reinforces PROTO-OFFLINE-13's central lesson:

> page start/count can be portable while internal payload ABI changes by generation.

---

# 14. Implications for Home Assistant

A safe read-only implementation can already expose:

```text
Thermia Service History Raw Event 1..8
Thermia Service History Time 1..8
Thermia Service History Date 1..8
Thermia Service History Sequence Raw
```

for the local modern XTR ABI.

But until raw identifiers are mapped, user-facing entity names such as:

```text
High pressure alarm
Low pressure alarm
E111
```

would be unjustified.

A better initial HA representation is:

```text
timestamp + raw code A + raw code B
```

with evidence metadata/documentation explaining that the text meaning is unresolved.

No write access is involved.

---

# 15. Evidence classification

## Observed facts

- legacy genuine Online/DCM `0884/count60` splits exactly into 10×6 timestamped records.
- all complete legacy `0884` payloads in the examined four-reference corpus are identical.
- genuine Eco5 `0884/count60` splits exactly into 8×7 timestamped records + 4-word trailer.
- local XTR `0884/count60` uses the same 8×7+4 modern ABI.
- local XTR history records advance newest-first across later stage-40 captures.
- the modern trailer's final word changes across selected local snapshots as the history evolves.
- official XTR documentation exposes an ALARM history with alarm name, time and date and UI depth 10.
- Danfoss Link firmware defines a separate `ErrorCode` plus five `AlarmField` parameters.
- local XTR `085F/count5` is repeatedly all-zero in normal sampled runtime.
- live status semantics exist independently in `07F4`, `083C`, `0845`, `0865`, `0866`.

## Strong conclusions

1. `0884/count60` is a **timestamped rolling service-history page**.
2. It is **very strongly supported** as the Online/DCM alarm-history export.
3. The history ABI changed from legacy `10×6` to modern `8×7 + 4 metadata`.
4. The local XTR M belongs to the modern `8×7 + 4` family.
5. Raw history IDs are not safely interpretable as direct displayed XTR `E###` numbers.
6. Current alarm/error state and timestamped history are separate concepts in the integration architecture.
7. `085F` must remain semantically OPEN despite its five-word size.

## Hypotheses

- modern raw A/raw B form a widened/composite alarm/event identifier or identifier+flags.
- `08BF` is a ring-buffer/history generation or sequence value.
- `0884` is exactly the DCM export of the UI's ALARM history, possibly with a modern subset/packing change.

## Unknowns

- raw legacy code -> alarm name mapping.
- raw modern A/B -> XTR E-code/alarm-name mapping.
- modern raw B semantics.
- exact `08BC..08BF` trailer semantics.
- why manual UI depth 10 coexists with modern 8-record wire ABI.
- native `0x0F` bridge for DHP/HE `ErrorCode` and `AlarmField1..5`.
- semantics of `085F/count5`.
- whether `0884` contains alarm-only events or a wider service/event history class.

---

# Result

**PROTO-OFFLINE-14 — COMPLETE / POSITIVE**

The major durable result is:

```text
0x0F:0884/count60
```

is locally confirmed on the XTR M as a modern timestamped rolling history ABI and is very strongly supported as the Online/DCM alarm-history/service-history export.

At the same time, the analysis establishes a strict separation between:

```text
live operating status
current alarm/error state
historical timestamped events
```

and avoids the unsafe shortcut of assigning raw history words directly to XTR `E###` fault names.

No live bus action, setting write, YAML change or experiment-status change was introduced by this offline analysis.