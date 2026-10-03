> **Current-status note — HISTORICAL / SUPERSEDED (2026-10-03).** This report correctly records the earlier `RUNNING / PARTIAL` state at the time it was written. The offline calendar reduction is now closed by `CAL_OFFLINE_01_FINAL_CLOSURE_20261003.md` as COMPLETE for the current evidence scope. Preserve this document as the intermediate analysis; use the final closure for current structure/status. Active calendar write semantics remain unproven where the final closure says OPEN.

# Thermia iTec XTR M — Calendar Structure Analysis

**Date:** 2026-10-02  
**Scope:** passive/local XTR M calendar correlation plus comparison with existing genuine Thermia Online / iTec Eco5 captures  
**Track:** CAL-OFFLINE-01  
**Status:** RUNNING / PARTIAL — offline evidence reduction only; no new ESP calendar write target

> **Revision:** the earlier 99-word-per-function interpretation is superseded. Re-aligning the complete 12-page region supports four logical **98-word** calendar blocks (8 × 12-word records + 2 metadata words), followed by a separate 4-word tail.

## Capture context

A local XTR M capture was taken while changing only one calendar function on the heat-pump UI:

- log start: approximately 13:09:30
- calendar function: **Hot Water Blocked / WW_GEBLOKKEERD**
- entry added at approximately 13:11:00
- interval: **02-10-2026 18:00 -> 19:00**
- the same entry was deleted at approximately 13:11:30

The commissioning manual lists the normal calendar functions as:

- WW_GEBLOKKEERD
- EVU / power limiting
- silent mode
- temperature reduction
- concrete-drying program

and documents a maximum of eight calendar slots.

This note records only what the supplied capture and existing project evidence support. It does not promote the untested calendar groups or unknown record fields beyond their evidence level.

---

## 1. Exact native transaction caused by adding the WW block

At approximately t=94.46 s, immediately after the UI change, the controller performs the following sequence:

```text
94.459  0F 03 0708 0006
94.506  0F 03 0C 0002 0000 0002 0000 0000 0000

94.552  0F 03 055A 0021
94.648  0F 03 42 <33 words>

95.454  0F 10 055A 0021 <same 33 words>
95.500  0F 10 055A 0021 ACK
```

The exact frames are:

```text
0F03070800064450
0F030C000200000002000000000000350C

0F03055A0021A423

0F03420000000000120002000A001A000000130002000A001A0000000100000015001F000C0000003B0017001F000C0000007F000000000000001F000C000000000000001F5E4D

0F10055A0021420000000000120002000A001A000000130002000A001A0000000100000015001F000C0000003B0017001F000C0000007F000000000000001F000C000000000000001FCB70

0F10055A002121E0
```

All six frames have valid Modbus RTU CRCs.

### Observed facts

- The `0708/count6` response is `W0..W5 = 0002,0000,0002,0000,0000,0000`.
- The controller then requests `055A/count33` with FC03.
- The returned 33-word page is subsequently republished by the controller with FC16.
- The FC03 page response and the controller FC16 republish are word-for-word identical.
- Therefore this transaction has no unrelated page delta.

### Strong conclusion

The local XTR M now directly confirms that `055A/count33` participates in the native desired-page mechanism during a calendar edit.

The existing 32-page selector model assigns `W2 bit1` to the current/PUSH side of page `055A`. This capture also locally demonstrates the corresponding desired/PULL selection with `W0 bit1`, because that bit is set immediately before the controller requests `055A/count33`.

**Status: PROVEN / locally confirmed**

- `W0 bit1 -> desired/PULL page 055A`
- `055A/count33` is writable through the same controller-owned full-page synchronization architecture used by the previously proven settings pages.

This does **not** yet prove that the complete `055A..05BC` region is exclusively Hot Water Blocked data.

---

## 2. First 12 words contain the newly entered interval

The first twelve words returned for page `055A` are:

```text
0000 0000 0012 0002 000A 001A
0000 0013 0002 000A 001A 0000
```

Decimal:

```text
0, 0, 18, 2, 10, 26,
0, 19, 2, 10, 26, 0
```

This matches the entered interval exactly:

```text
02-10-2026 18:00
02-10-2026 19:00
```

Register-level view:

| Register | Raw | Current interpretation | Evidence |
|---|---:|---|---|
| 055A | 0 | record metadata A | OPEN / UNKNOWN |
| 055B | 0 | start minute | STRONGLY SUPPORTED |
| 055C | 18 | start hour | STRONGLY SUPPORTED / locally correlated |
| 055D | 2 | start day | STRONGLY SUPPORTED / locally correlated |
| 055E | 10 | start month | STRONGLY SUPPORTED / locally correlated |
| 055F | 26 | start year, apparently 2026 -> 26 | STRONGLY SUPPORTED / locally correlated |
| 0560 | 0 | end minute | STRONGLY SUPPORTED |
| 0561 | 19 | end hour | STRONGLY SUPPORTED / locally correlated |
| 0562 | 2 | end day | STRONGLY SUPPORTED / locally correlated |
| 0563 | 10 | end month | STRONGLY SUPPORTED / locally correlated |
| 0564 | 26 | end year, apparently 2026 -> 26 | STRONGLY SUPPORTED / locally correlated |
| 0565 | 0 | record metadata B | OPEN / UNKNOWN |

The hour/day/month/year fields are not yet promoted to PROVEN because only one controlled calendar interval has been varied. The correspondence is nevertheless direct and highly specific.

---

## 3. Independent clock-format cross-check from page 0848

The same local capture contains the controller clock/date page at `0848/count23`.

Examples from its final seven words include:

```text
0017 000F 000D 0002 000A 001A 0004
```

and later:

```text
000E 0011 000D 0002 000A 001A 0004
```

These are consistent with:

```text
second, minute, hour, day, month, year, weekday
```

For the calendar record, removing seconds gives the same internal ordering expected for the candidate timestamp fields:

```text
minute, hour, day, month, year
```

This is supporting evidence for `055B..055F` and `0560..0564`, not independent proof of every field.

The heat-pump internal clock in this capture appears to be several minutes ahead of the external log-start annotation. This is useful for event correlation but should not be treated as a calibrated clock-offset measurement from this single sample.

---

## 4. Corrected calendar region: four 98-word logical function blocks

The native transport pages are:

```text
055A/33  057B/33  059C/33
05BD/33  05DE/33  05FF/33
0620/33  0641/33  0662/33
0683/33  06A4/33  06C5/33
```

Together these pages cover **396 contiguous registers** from `055A` through `06E5`.

Re-aligning the full region gives a substantially better fit than the earlier three-pages-per-function model:

```text
4 × 98 words = 392 words
+ 4 trailing words = 396 words
```

Each 98-word logical calendar-function block is:

```text
8 slots × 12 words = 96
+ 2 metadata words
= 98 words
```

Corrected logical boundaries:

| Logical block | Range | Record area | Metadata |
|---|---|---|---|
| F1 | `055A..05BB` | `055A..05B9` | `05BA..05BB` |
| F2 | `05BC..061D` | `05BC..061B` | `061C..061D` |
| F3 | `061E..067F` | `061E..067D` | `067E..067F` |
| F4 | `0680..06E1` | `0680..06DF` | `06E0..06E1` |
| trailing | `06E2..06E5` | — | separate four-word region |

### Strong conclusion

The previous 99-word grouping followed transport-page boundaries rather than the logical calendar structure.

Native 33-word page boundaries cut **through** logical functions and records. For example, F2 begins at `05BC`, the last word of native page `059C/count33`, and continues in page `05BD/count33`.

**Status: STRONGLY SUPPORTED** by exact structural alignment in the local XTR and genuine Eco5 captures.

---

## 5. Slot occupancy / validity bitmap candidates

The first metadata word of each 98-word block correlates strongly with populated slot count:

```text
F1 -> 05BA
F2 -> 061C
F3 -> 067E
F4 -> 06E0
```

Observed historical local XTR snapshot:

```text
05BA = 003F   -> bits 0..5 set; six populated F1 records
06E0 = 000F   -> bits 0..3 set; four populated F4 records
```

Observed genuine Eco5 + Online snapshot:

```text
05BA = 0003   -> bits 0..1 set; two populated F1 records
06E0 = 0003   -> bits 0..1 set; two populated F4 records
```

F2/F3 candidate bitmaps are zero in the compared Eco5 snapshot. Importantly, F3 still contains a record-shaped residual pattern while `067E=0`. That is consistent with slot contents remaining in memory after a slot is inactive and with the bitmap carrying the configured/valid state.

### Classification

`05BA`, `061C`, `067E`, `06E0` as eight-bit slot-validity/occupancy bitmaps:

**STRONGLY SUPPORTED**, not yet locally PROVEN by a controlled one-bit add/delete transition.

The second metadata word of every logical block (`05BB`, `061D`, `067F`, `06E1`) is zero in the compared snapshots. Its semantics remain **OPEN / UNKNOWN**.

---

## 6. Record-mode and weekday fields

The current best 12-word record model is:

```text
word 0      schedule-mode metadata
word 1      start minute
word 2      start hour
word 3      start day
word 4      start month
word 5      start year
word 6      stop minute
word 7      stop hour
word 8      stop day
word 9      stop month
word 10     stop year
word 11     weekday / recurrence mask
```

The local DATE entry uses:

```text
0, 0,18,2,10,26, 0,19,2,10,26, 0
```

Genuine Eco5 + Online contains weekly-looking records such as:

```text
1, 0,21,31,12,0, 59,23,31,12,0, 127
```

`127 = 0b1111111`, exactly compatible with seven selected weekdays.

The repeated empty-record form:

```text
0,0,0,31,12,0,0,0,31,12,0,0
```

supports `31/12/00` as an unset/sentinel date.

Current classification:
- minute/hour/day/month/year ordering: **STRONGLY SUPPORTED**;
- word0 as DATE versus DAYS/WEEK mode: **STRONGLY SUPPORTED**, not locally proven;
- word11 as weekday mask: **STRONGLY SUPPORTED by genuine Online/Eco5 evidence**, not locally proven;
- exact weekday bit ordering: **OPEN / UNKNOWN**.

---

## 7. Probable function mapping

The commissioning manual lists four ordinary schedule functions plus a separate concrete-drying program:

```text
WW_GEBLOKKEERD
EVU / power limiting
Silent Mode
Temperature Reduction
Concrete Drying Program
```

F1 is locally anchored by the supplied edit:

```text
F1 055A..05BB = WW_GEBLOKKEERD
```

The remaining order is structurally attractive:

```text
F2 05BC..061D = EVU / power limiting
F3 061E..067F = Silent Mode
F4 0680..06E1 = Temperature Reduction
```

**F2-F4 remain HYPOTHESIS only** until each is locally correlated.

---

## 8. Concrete Drying is strongly indicated at 04D8/count27

The separate native `04D8/count27` block matches the documented concrete-drying structure closely.

Local XTR example:

```text
1,1,12,0,0,2,2,
1,25, 2,20, 3,20, 4,20, 5,20,
6,20, 7,20, 8,20, 9,20, 10,20
```

Genuine Eco5 + Online example:

```text
6,2,25,0,12,2,10,
1,20, 2,25, 3,30, 4,35, 5,40,
6,40, 7,35, 8,30, 9,25, 10,20
```

The last 20 words are exactly ten `(day/point index, supply temperature)` pairs.

The commissioning manual independently specifies:
- maximum 10 points;
- day value 1..40;
- supply temperature 15..55 °C;
- hysteresis factory 2, range 1..5.

Current classification:
- `04D8/count27` = concrete-drying configuration: **STRONGLY SUPPORTED**;
- words7..26 = ten day/temperature pairs: **STRONGLY SUPPORTED**;
- header word5 = hysteresis and word6 = configured-point count: **STRONGLY SUPPORTED**, not locally correlated;
- header words0..4: **OPEN / UNKNOWN**.

Do not label header words0..4 as a start date/time without a controlled correlation.

---

## 9. 06EA/count7 is clock/date, not concrete-drying storage

Observed examples fit:

```text
second, minute, hour, day, month, year, weekday
```

including local XTR:

```text
14,11,8,25,9,26,4
```

and genuine Eco5 examples on their respective capture dates.

**Status: STRONGLY SUPPORTED.**

Therefore the earlier idea that `06EA/06F1/06F4` might simply be the continuation of the ordinary calendar-function store is not supported for `06EA`.

---

## 10. Separate trailing region 06E2..06E5 and exact 0870 relationship

The corrected four-block model leaves four words:

```text
06E2 06E3 06E4 06E5
```

Across three compared datasets:

```text
Local XTR:
06E2=00CE, 06E3=0055 -> 0x55CE
0870 word0 = 0x55CE

Eco5 20260926:
06E2=006B, 06E3=0004 -> 0x046B
0870 word0 = 0x046B

Eco5 20260928:
06E2=006C, 06E3=0004 -> 0x046C
0870 word0 = 0x046C
```

`06E4` and `06E5` are zero in these snapshots.

The byte-pair reconstruction `(06E3 << 8) | 06E2` therefore equals `0870 word0` in every compared dataset.

**Observed relationship: STRONGLY SUPPORTED / repeatedly observed.**  
**Semantic meaning: OPEN / UNKNOWN.**

Do not call it a checksum, pointer or calendar identifier without further evidence.

---

## 11. Deletion is still inconclusive in the supplied local capture

The user deleted the same calendar entry around t=120 s.

At:

```text
120.310  0F 03 0708 0006
120.356  0F 03 0C 0000 0000 0000 0000 0000 0000
```

the selector is already idle again.

No later `055A`, `057B`, or `059C` calendar transaction is visible in the supplied remainder of the capture.

Therefore:

- the **add** correlation is positive;
- the **delete** encoding is not captured here;
- absence of a second `055A` transaction does not prove that deletion failed or uses a different protocol.

If `05BA` is indeed the slot-active bitmap, a delete may only require clearing the relevant slot bit while leaving old 12-word record contents intact. This is a hypothesis to test, not a proven behavior.

---

## Evidence classification

### PROVEN / locally confirmed on this XTR M

- a WW_GEBLOKKEERD edit triggers the native `055A/count33` desired-page path;
- `W0 bit1` participates in desired/PULL selection for page `055A`;
- the controller requests a 33-word desired page and republishes the accepted image through FC16.

### STRONGLY SUPPORTED

- one logical calendar record is 12 words;
- words1..10 hold start/stop date-time fields in minute/hour/day/month/year order;
- word0 is schedule-mode metadata and word11 is recurrence/weekday metadata;
- the ordinary calendar store is four logical 98-word blocks = eight 12-word records + two metadata words;
- `05BA/061C/067E/06E0` are slot-validity/occupancy bitmap candidates;
- `04D8/count27` is the separate concrete-drying configuration structure;
- `06EA/count7` is a clock/date block;
- `06E2/06E3` reconstruct `0870 word0` across the compared datasets.

### HYPOTHESIS

- F2 = EVU / power limiting;
- F3 = Silent Mode;
- F4 = Temperature Reduction;
- schedule-mode 0 = DATE and 1 = DAYS/WEEK;
- deletion may clear a slot-validity bit while leaving stale record data.

### OPEN / UNKNOWN

- exact meaning of the second metadata word in each function block;
- exact weekday-bit order;
- live local bitmap transition on add/delete;
- exact meaning of concrete-drying header words0..4;
- semantics of `06E2..06E5`;
- transaction ordering when one logical record crosses two native 33-word pages.

---

## Safest next experiment

A passive-only follow-up has the highest value.

Suggested controlled action:

1. create one WW_GEBLOKKEERD DATE item while changing only one previously-zero minute field, e.g. start 18:15 with the remaining date/time values controlled;
2. note the exact UI slot used;
3. wait until relevant calendar-page traffic has settled;
4. delete that same item;
5. continue logging for 60–90 seconds;
6. compare the predicted minute word, the corresponding slot record and the candidate bitmap at `05BA`.

### Positive evidence

- non-zero minute values appear only in the predicted minute words;
- adding one slot sets exactly one candidate bitmap bit;
- deleting the same slot clears exactly that bit;
- no unrelated calendar-record words change.

### Negative / alternative evidence

- minute values appear at different positions;
- add/delete changes multiple record fields or a different metadata word;
- the slot-active model does not match the observed occupancy.

### Abort

No active ESP protocol action is required. Unexpected bus traffic remains capture-only. Do not introduce calendar writes until the passive record and bitmap layout is locally confirmed.

---

## Practical consequence

The calendar path is now a realistic future extension of the native Thermia Online/DCM emulation architecture, but it should not yet be implemented as a production Home Assistant writer.

The immediate durable result is structural: **the XTR M calendar participates in the same native page-owned desired-state synchronization system as the already controlled settings pages, while its logical 12-word records and 98-word function blocks cross the native 33-word transport-page boundaries.**
