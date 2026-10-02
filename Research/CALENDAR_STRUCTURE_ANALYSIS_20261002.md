# Thermia iTec XTR M — Calendar Structure Analysis

**Date:** 2026-10-02  
**Scope:** passive/local XTR M calendar correlation plus comparison with existing genuine Thermia Online / iTec Eco5 captures  
**Status:** analysis note; no new ESP write target and no new active calendar write experiment

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

## 4. The calendar region has a strong 8 x 12 + 3 structure

The known native configuration pages in this range are:

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

Each group of three pages is exactly:

```text
3 x 33 = 99 words
```

The commissioning manual documents up to eight calendar slots. A structure of:

```text
8 slots x 12 words = 96 words
+ 3 group metadata words
= 99 words
```

fits the transport layout exactly.

### Candidate group layout

```text
055A..05BC   group 1 — locally anchored to a WW_GEBLOKKEERD edit
05BD..061F   group 2 — calendar-function candidate
0620..0682   group 3 — calendar-function candidate
0683..06E5   group 4 — calendar-function candidate
```

Because the commissioning manual lists four normal schedule functions before the separate concrete-drying program, the following mapping is structurally attractive:

```text
055A..05BC   WW_GEBLOKKEERD
05BD..061F   EVU / power limiting
0620..0682   Silent Mode
0683..06E5   Temperature Reduction
```

Only the first group is locally anchored by the supplied XTR M edit.

**Status of groups 2-4: HYPOTHESIS / structural candidate only.**

Do not expose these mappings as established XTR semantics until each is locally correlated.

---

## 5. Slot boundaries do not match native page boundaries

Assuming the 12-word slot model, the first group divides as:

```text
slot 0: 055A..0565
slot 1: 0566..0571
slot 2: 0572..057D
slot 3: 057E..0589
slot 4: 058A..0595
slot 5: 0596..05A1
slot 6: 05A2..05AD
slot 7: 05AE..05B9
group metadata: 05BA..05BC
```

Transport pages are instead:

```text
055A..057A
057B..059B
059C..05BC
```

Therefore calendar records can cross native page boundaries. For example, slot 2 would begin at `0572` in the first page and continue through `057D` in the second page.

This is important for any future calendar writer: a calendar slot must not be assumed to map one-to-one to a single 33-word native page.

---

## 6. Existing XTR and genuine Eco5 captures support an active-slot bitmap

An older local XTR capture contains the same three-page `055A/057B/059C` family. Its first 96 words contain multiple non-empty 12-word records, and the final three-word metadata region includes:

```text
003F 0000 0000
```

`0x003F = 0b00111111`, which is compatible with six active slots.

A genuine iTec Eco5 + Thermia Online capture contains the same page family and shows:

```text
0003 0000 0000
```

at the corresponding group tail.

`0x0003 = 0b00000011`, which is compatible with two active slots.

### Strongly supported interpretation

`05BA`, the first word of the three-word group metadata tail, is a strong candidate for an 8-bit slot-active / slot-valid bitmap:

```text
bit0 = slot 0
bit1 = slot 1
...
bit7 = slot 7
```

**Status: STRONGLY SUPPORTED**

This is supported by both local XTR structure and genuine Online/Eco5 structure, but it is not yet locally proven by observing one slot bit change during a controlled add/delete sequence.

---

## 7. Candidate recurrence / weekday metadata

Existing genuine Online/Eco5 calendar records contain structures such as:

```text
1, 0, 21, 31, 12, 0,
59, 23, 31, 12, 0, 127
```

The final value `127 = 0b1111111` is compatible with a seven-day weekday mask.

The locally added one-shot record is:

```text
0, 0, 18, 2, 10, 26,
0, 19, 2, 10, 26, 0
```

This suggests, but does not prove, that the two metadata words surrounding the two five-word timestamps may encode schedule mode/recurrence and weekday selection.

Candidate model:

```text
word 0     recurrence / date-mode metadata
words 1-5  start minute/hour/day/month/year
words 6-10 end minute/hour/day/month/year
word 11    weekday / recurrence mask metadata
```

**Status: HYPOTHESIS**, with the weekday-mask interpretation supported by the `0x007F` genuine Online examples.

A controlled recurring schedule with selected weekdays is required before promotion.

---

## 8. Deletion is still inconclusive in the supplied local capture

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

- A WW_GEBLOKKEERD calendar edit triggers the native `055A/count33` page family.
- `W0 bit1` can select `055A` on the desired/PULL side of the `0708` mechanism.
- The controller requests `055A/count33` via FC03, accepts a complete 33-word page, and republishes that identical page with FC16.
- The full-page desired-state architecture is therefore not limited to the previously proven heating/DHW/cooling/operation settings pages.

### STRONGLY SUPPORTED

- The first 12 words form one calendar record.
- The record contains two five-word date/time structures corresponding to the entered start and end.
- The likely order is minute, hour, day, month, year.
- Each normal calendar-function group occupies 99 words = eight 12-word records + three metadata words.
- `05BA` is likely the active-slot bitmap for the first calendar group.
- The four 99-word groups are likely the four ordinary calendar functions listed in the manual.

### HYPOTHESIS

- `055A` record word0 is recurrence/date-mode metadata.
- record word11 is a weekday/recurrence mask.
- groups 2-4 map, in manual order, to EVU/power limiting, Silent Mode and Temperature Reduction.
- deletion may clear only a slot-valid bit rather than zeroing the slot contents.
- the remaining `06EA/06F1/06F4` area may relate to concrete-drying or other calendar metadata; no promotion is justified yet.

### OPEN / UNKNOWN

- exact meaning of record words 0 and 11;
- exact minute-field proof using non-zero minutes;
- exact slot-bitmap location/behavior during controlled add/delete;
- whether empty/deleted slot contents are preserved;
- mapping of groups 2-4;
- concrete-drying storage layout;
- whether writes spanning a slot across two native pages require ordered multi-page desired-state transactions.

---

## Safest next experiment

A passive-only follow-up has the highest value.

Suggested controlled action:

1. create exactly one WW_GEBLOKKEERD item with non-zero minutes, for example 18:15 -> 19:30;
2. wait long enough to capture the complete `055A/057B/059C` activity;
3. delete the same item;
4. continue logging for at least 60 seconds;
5. compare:
   - `055B` and `0560` for minute values;
   - the first 12-word record before/after;
   - `05BA` for a one-bit slot validity change;
   - all three pages for any additional metadata delta.

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

The immediate durable result is structural: **the XTR M calendar participates in the same native page-owned desired-state synchronization system as the already controlled settings pages, and the first WW calendar record is directly visible in the 055A page family.**
