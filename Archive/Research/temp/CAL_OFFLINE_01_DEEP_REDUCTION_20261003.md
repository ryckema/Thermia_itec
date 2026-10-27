# Thermia iTec XTR M — Calendar deep reduction

**Date:** 2026-10-03  
**Track:** CAL-OFFLINE-01 — refinement pass  
**Refinement result:** COMPLETE / POSITIVE — offline analysis only  
**Parent track status:** RUNNING / PARTIAL  
**Live experiment status:** unchanged — EXP388 remains RUNNING / PARTIAL  
**Device TX:** none  
**YAML change:** none  
**Heat-pump restart:** none  
**Setting write:** none  
**GitHub change:** none

## Hypothesis

The existing calendar corpus contains enough independent structure and natural variation to reduce the ordinary Thermia calendar format further without a new live write test.

Specifically, this pass tests whether:

1. the 396-word native calendar region can be reconstructed as four logical function blocks;
2. the 12-word slot format can be assigned field-by-field;
3. the two trailing words per function can be distinguished from slot data;
4. natural changes in genuine Online/DCM captures validate the proposed field alignment;
5. the runtime/operational pages provide independent evidence that a scheduled function is becoming active.

The hypothesis is **supported**, but the parent calendar track is **not complete** because several semantic labels and delete/weekday details still lack direct XTR confirmation.

---

# 1. Evidence and provenance

Corpus used:

- `thermia_capture_20260925_090209.log`
- `thermia_capture_20260925_090550.log`
- `itec_eco5_gateway_20260926.log`
- `itec_eco5_gateway_20260928.log`
- existing controlled local XTR WW_GEBLOKKEERD result already recorded in the canonical experiment log
- Thermia iTec XT/XTR commissioning manual transcription

Important provenance correction carried forward from PROTO-OFFLINE-03:

- the `thermia_capture_20260924/25...` captures are **genuine older Online/DCM reference captures**, not historical local-XTR captures;
- the two `itec_eco5_gateway_*` captures are genuine Eco5 + Thermia Online captures;
- only the explicitly controlled WW_GEBLOKKEERD observation is treated as local-XTR semantic evidence here.

The previous EXP385 passive UI-edit attempt is **not usable as calendar evidence**: it repeatedly hit RX-buffer aborts and recorded zero calendar frames. It is therefore an inconclusive/invalid capture, not evidence against the calendar model.

---

# 2. Native transport census

The ordinary calendar transport consists of twelve contiguous native slave-`0x0F` FC16 pages:

```text
055A / count33
057B / count33
059C / count33
05BD / count33
05DE / count33
05FF / count33
0620 / count33
0641 / count33
0662 / count33
0683 / count33
06A4 / count33
06C5 / count33
```

Together they cover:

```text
055A .. 06E5
```

which is exactly:

```text
12 × 33 = 396 words
```

Observed frame census:

| Capture | Calendar FC16 frames | Dynamic pages |
|---|---:|---|
| older Online/DCM `090209` | 12 | none inside capture |
| older Online/DCM `090550` | 12 | none inside capture |
| Eco5 + Online `20260926` | 64 | `0683` only |
| Eco5 + Online `20260928` | 150 | none inside capture |

In the 2026-09-26 Eco5 capture, every calendar page is byte-stable except `0683`, which has exactly two payload variants.

---

# 3. Correct logical alignment: 4 × 98 words + 4-word tail

Concatenating the twelve 33-word transport pages and re-aligning by record structure gives:

```text
F1 = 055A .. 05BB = 98 words
F2 = 05BC .. 061D = 98 words
F3 = 061E .. 067F = 98 words
F4 = 0680 .. 06E1 = 98 words
tail = 06E2 .. 06E5 = 4 words
```

Each 98-word function block decomposes exactly as:

```text
8 slots × 12 words = 96 words
+ 2 metadata words = 98 words
```

This supersedes the older 99-word-per-function interpretation.

The manual independently states that the ordinary calendar supports up to **8 calendar slots**, which matches this structure exactly.

**STRONGLY SUPPORTED:** the ordinary native calendar is four logical functions, each with eight 12-word records plus two metadata words.

---

# 4. The 12-word record format

The combined local controlled record, older genuine Online/DCM records and Eco5 weekly records support the following field map:

| Word | Proposed field | Evidence level |
|---:|---|---|
| 0 | schedule mode | VERY STRONGLY SUPPORTED |
| 1 | start minute | VERY STRONGLY SUPPORTED |
| 2 | start hour | VERY STRONGLY SUPPORTED |
| 3 | start day | VERY STRONGLY SUPPORTED |
| 4 | start month | VERY STRONGLY SUPPORTED |
| 5 | start year | VERY STRONGLY SUPPORTED |
| 6 | stop minute | VERY STRONGLY SUPPORTED |
| 7 | stop hour | VERY STRONGLY SUPPORTED |
| 8 | stop day | VERY STRONGLY SUPPORTED |
| 9 | stop month | VERY STRONGLY SUPPORTED |
| 10 | stop year | VERY STRONGLY SUPPORTED |
| 11 | weekday / recurrence mask | VERY STRONGLY SUPPORTED |

There is **no spare per-record action/type word**. The action is therefore most plausibly implied by the enclosing function block F1/F2/F3/F4.

## Mode 0 — absolute DATE entry

The controlled local XTR WW_GEBLOKKEERD record for:

```text
02-10-2026 18:00 -> 19:00
```

was encoded as:

```text
0000 0000 0012 0002 000A 001A
0000 0013 0002 000A 001A 0000
```

Interpretation:

```text
mode = 0
start = 18:00 02-10-2026
stop  = 19:00 02-10-2026
weekday mask = 0
```

**VERY STRONGLY SUPPORTED:** mode `0` is the absolute-date mode.

## Mode 1 — DAYS/WEEK recurring entry

Genuine Eco5 records use forms such as:

```text
0001 0000 0015 001F 000C 0000
003B 0017 001F 000C 0000 007F
```

Interpretation:

```text
mode = 1
start = 21:00
stop  = 23:59
date fields = 31/12/0 sentinel
weekday mask = 0x007F
```

`0x007F` has all seven low bits set, matching an all-days recurring entry.

**VERY STRONGLY SUPPORTED:**

```text
mode 1 = DAYS/WEEK recurring mode
word11 = 7-bit weekday mask
```

The **exact bit-to-weekday order remains OPEN**, because the current corpus contains only the all-seven-days mask and no independently labelled subset-day record.

---

# 5. Metadata word 0 is the slot-validity bitmap

The first metadata word of each 98-word function is:

```text
F1: 05BA
F2: 061C
F3: 067E
F4: 06E0
```

The evidence lines up exactly with `bit N -> slot N active/configured`.

## Older genuine Online/DCM

```text
F1 metadata0 = 0x003F
```

Slots 0..5 contain records; slots 6..7 are empty.

```text
F4 metadata0 = 0x000F
```

Slots 0..3 contain records; slots 4..7 are empty.

## Genuine Eco5

```text
F1 metadata0 = 0x0003
F4 metadata0 = 0x0003
```

Slots 0 and 1 are the active records.

Most importantly:

```text
F3 metadata0 = 0x0000
```

while F3 slot0 still contains a record-looking residual image.

That stale record with a zero bitmap is strong evidence that the bitmap, not record contents alone, determines whether a slot is configured/active.

**STRONGLY SUPPORTED:**

```text
metadata0 = 8-bit slot-validity/configured bitmap
bit0 -> slot0
...
bit7 -> slot7
```

This is still not labelled **PROVEN / local XTR** until a controlled XTR add/delete capture directly shows the relevant bitmap edge.

---

# 6. Metadata word 1 remains unknown

The second metadata word is:

```text
F1: 05BB
F2: 061D
F3: 067F
F4: 06E1
```

It is zero in every compared complete snapshot.

No existing capture provides a discriminating value.

**Status: OPEN / UNKNOWN.**

Do not assign checksum, generation, mode, enable or count semantics to it yet.

---

# 7. Natural Eco5 mutation directly confirms `word2 = start hour`

The strongest new field-level evidence comes from the genuine Eco5 2026-09-26 capture.

Page:

```text
0683 / count33
```

has eight observed instances and exactly two payload variants.

The only changing logical word is:

```text
register 068E
```

Timeline:

```text
t=333.998 s  068E = 20
t=750.384 s  068E = 20

t=780.568 s  068E = 21
t=836.562 s  068E = 21
t=837.114 s  068E = 21
t=849.700 s  068E = 21
t=851.117 s  068E = 21
t=905.957 s  068E = 21
```

Logical alignment:

```text
F4 starts at 0680
F4 slot1 starts at 068C
068E = F4 slot1 word2
```

Under the proposed record map, word2 is the **start hour**.

The full slot changes from:

```text
mode1, 20:00 -> 23:59, all days
```

to:

```text
mode1, 21:00 -> 23:59, all days
```

with every other slot field unchanged.

The Eco5 2026-09-28 capture retains `068E=21`.

**PROVEN / structural in genuine Eco5 Online traffic:** F4 slot1 word2 is the start-hour field.

This natural one-field edit independently validates both the 12-word alignment and the start-time interpretation.

---

# 8. F4 schedule activation correlates with Eco5 `04A6=0044`

A second independent clue appears in the same genuine Eco5 2026-09-26 capture.

Before the scheduled F4 slot1 start:

```text
04A6 = 0000
04A7 = 0000
```

The first transition to:

```text
04A6 = 0044
04A7 = 0001
```

occurs at capture time `482.626 s`.

The nearest preceding controller clock export is:

```text
19:57:55
```

at `355.263 s`.

Adding the elapsed ~127.36 s places the `0044/0001` onset at approximately:

```text
20:00:02
```

At that moment:

- F4 slot1 is configured for `20:00 -> 23:59`;
- F1's comparable weekly slot starts only at `21:00`;
- F2 has no active bitmap;
- F3 has no active bitmap.

The `0044/1` state therefore starts essentially on the F4 scheduled boundary.

Later, the F4 start hour is changed from 20 to 21 at `068E`, and `04A6/04A7` has returned to `0000/0` shortly beforehand.

There are several brief zero excursions while the interval is otherwise active, so the evidence does **not** justify calling `04A6=0044` a simple Boolean F4-active flag.

**STRONGLY SUPPORTED:**

> On the genuine Eco5 system, `04A6=0044 / 04A7=1` is associated with the active operational state produced by the scheduled F4 function.

**OPEN:** exact semantic name of the state and why short zero excursions occur.

This adds strong behavioral evidence that F4 is a real scheduled function, but it does **not** by itself prove which user-facing calendar function F4 represents.

---

# 9. Function identities

Current evidence classification:

| Function | Current interpretation | Status |
|---|---|---|
| F1 `055A..05BB` | WW_GEBLOKKEERD | **PROVEN / locally correlated** |
| F2 `05BC..061D` | EVU / vermogensbegrenzing | **HYPOTHESIS** |
| F3 `061E..067F` | Stille modus | **HYPOTHESIS** |
| F4 `0680..06E1` | Temperatuurverlaging | **HYPOTHESIS**, now with strong evidence of actual scheduled activation |

The F2/F3/F4 naming remains based on structure/manual ordering and plausibility rather than a controlled semantic edit.

Do not promote those names to locally proven mappings yet.

---

# 10. The four-word tail is not a simple calendar revision counter

The four words after F4 are:

```text
06E2 06E3 06E4 06E5
```

Eco5 2026-09-26 remains:

```text
006B 0004 0000 0000
```

across the observed F4 slot1 hour edit `20 -> 21`.

The previously established relation remains:

```text
0870.word0 = (06E3 << 8) | 06E2
```

which gives:

```text
0x046B
```

and this likewise does not change as a result of the schedule-hour edit.

**NEGATIVE / useful exclusion:**

> `06E2/06E3` and the derived `0870.word0` are not a simple calendar-edit generation/revision counter.

Their actual semantics remain OPEN.

---

# 11. Physical page boundaries versus logical slots

The 33-word native transport pages cut across logical slot boundaries. This is important for any future emulator/writer.

| Function | Logical item | Register range |
|---|---|---|
| F1 | slot0 | `055A..0565` |
| F1 | slot1 | `0566..0571` |
| F1 | slot2 | `0572..057D` — crosses `055A -> 057B` |
| F1 | slot3 | `057E..0589` |
| F1 | slot4 | `058A..0595` |
| F1 | slot5 | `0596..05A1` — crosses `057B -> 059C` |
| F1 | slot6 | `05A2..05AD` |
| F1 | slot7 | `05AE..05B9` |
| F1 | metadata | `05BA..05BB` |
| F2 | slot0 | `05BC..05C7` — crosses `059C -> 05BD` |
| F2 | slot1 | `05C8..05D3` |
| F2 | slot2 | `05D4..05DF` — crosses `05BD -> 05DE` |
| F2 | slot3 | `05E0..05EB` |
| F2 | slot4 | `05EC..05F7` |
| F2 | slot5 | `05F8..0603` — crosses `05DE -> 05FF` |
| F2 | slot6 | `0604..060F` |
| F2 | slot7 | `0610..061B` |
| F2 | metadata | `061C..061D` |
| F3 | slot0 | `061E..0629` — crosses `05FF -> 0620` |
| F3 | slot1 | `062A..0635` |
| F3 | slot2 | `0636..0641` — crosses `0620 -> 0641` |
| F3 | slot3 | `0642..064D` |
| F3 | slot4 | `064E..0659` |
| F3 | slot5 | `065A..0665` — crosses `0641 -> 0662` |
| F3 | slot6 | `0666..0671` |
| F3 | slot7 | `0672..067D` |
| F3 | metadata | `067E..067F` |
| F4 | slot0 | `0680..068B` — crosses `0662 -> 0683` |
| F4 | slot1 | `068C..0697` |
| F4 | slot2 | `0698..06A3` |
| F4 | slot3 | `06A4..06AF` |
| F4 | slot4 | `06B0..06BB` |
| F4 | slot5 | `06BC..06C7` — crosses `06A4 -> 06C5` |
| F4 | slot6 | `06C8..06D3` |
| F4 | slot7 | `06D4..06DF` |
| F4 | metadata | `06E0..06E1` |
| tail | — | `06E2..06E5` |

**Architectural implication:** the logical record model and the native FC16 transport-page model are different layers. A future DCM emulator cannot safely assume “one schedule slot = one native page”.

No calendar writer should be implemented until the desired-page behavior for all affected transport pages is understood.

---

# 12. Concrete drying remains a separate structure

The manual lists concrete drying as a calendar-area feature, but its data structure is distinct.

The native:

```text
04D8 / count27
```

fits:

```text
7-word header
+ 10 × (day, supply-temperature) pairs
```

which matches the manual's maximum of ten concrete-drying points.

Therefore BETONDROOG_PROG should **not** be forced into the four ordinary 98-word calendar functions.

**STRONGLY SUPPORTED:** `04D8/count27` is the concrete-drying configuration structure or a directly related structure.

Header words 0..4 remain unresolved.

---

# 13. Clock/date block

`06EA/count7` retains the strongly supported layout:

```text
second
minute
hour
day
month
year (2 digit)
weekday
```

It provides an independent time reference for the natural F4 schedule activation described above.

The runtime page `0858..085E` exposes the same logical clock/date tuple.

---

# 14. EXP385 disposition

EXP385 was designed as a passive controlled add/delete capture, but the supplied run cannot be used for protocol conclusions.

Observed:

```text
Calendar Frames = 0
Calendar Changes = 0
repeated ABORT_RX_BUFFER
pending buffer approximately 8.2 kB
NO_TX = 1
```

Classification:

**COMPLETE / INCONCLUSIVE as a capture attempt**, not a negative result for the calendar hypothesis.

It does not provide the missing local bitmap add/delete edge.

---

# Evidence classification

## Observed facts

- Twelve count33 FC16 pages cover `055A..06E5`, exactly 396 words.
- Re-alignment yields four 98-word blocks plus four tail words.
- Each 98-word block fits exactly eight 12-word records plus two metadata words.
- The local controlled F1 record encodes a real absolute start/stop date and time.
- Genuine Eco5 mode1 records use `31/12/0` date sentinels and `0x007F`.
- F1/F4 metadata bitmaps match occupied slot positions across independent captures.
- F3 contains stale record-looking data while its candidate bitmap is zero.
- Genuine Eco5 `068E` changes naturally `20 -> 21` and is the only changed word in the page variant.
- `068E` is F4 slot1 word2.
- `04A6=0044/04A7=1` begins approximately at the F4 20:00 scheduled boundary in the genuine Eco5 capture.
- `06E2/06E3` do not change across the F4 start-hour edit.
- EXP385 captured no calendar frames due repeated RX-buffer aborts.

## Strong conclusions

1. The ordinary calendar is a four-function logical record layer serialized across twelve native 33-word transport pages.
2. A slot is a 12-word schedule record with mode, start date/time, stop date/time and weekday mask.
3. Mode0 is absolute DATE; mode1 is recurring DAYS/WEEK.
4. Metadata0 is the slot-validity/configuration bitmap.
5. Deletion/inactivation can plausibly leave stale record memory behind while clearing the bitmap; this is strongly suggested but not locally proven.
6. `068E` independently confirms word2 as start hour.
7. F4 has a real scheduled operational effect visible in Eco5 runtime state.
8. The `06E2/06E3 -> 0870.word0` value is not a simple calendar revision counter.

## Hypotheses

- F2 = EVU / power limiting.
- F3 = Silent Mode.
- F4 = Temperature Reduction.
- Delete/inactivate primarily clears the corresponding validity bit while record contents may remain stale.
- `04A6=0044` is an F4-induced operational state on Eco5; exact semantic label is open.

## Unknowns

- exact weekday bit ordering;
- exact F2/F3/F4 user-facing identities;
- semantic meaning of metadata1;
- locally confirmed bitmap transition on XTR;
- exact delete encoding/transaction;
- whether a record body is rewritten on delete or merely left stale;
- desired-page/write behavior for records crossing native page boundaries;
- semantics of `06E2..06E5`;
- concrete-drying header words 0..4.

---

# Result

**CAL-OFFLINE-01 refinement pass — COMPLETE / POSITIVE**

**Parent CAL-OFFLINE-01 remains RUNNING / PARTIAL.**

The offline corpus now supports a substantially stronger calendar model, including the full 12-word record layout, recurring-versus-date mode distinction, validity bitmap semantics, and a natural one-field start-hour change.

The remaining unknowns are now narrow enough that another broad offline reconstruction is unlikely to resolve them. The highest-value next evidence is a **clean passive XTR UI edit capture** with:

- one weekly entry using a subset of weekdays, and/or
- one add/delete cycle while calendar pages are captured without RX overflow.

No live calendar writer is justified yet.