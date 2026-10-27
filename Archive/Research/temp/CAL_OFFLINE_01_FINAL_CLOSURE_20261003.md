# Thermia iTec XTR M — CAL-OFFLINE-01 final offline closure

**Date:** 2026-10-03  
**Track:** CAL-OFFLINE-01  
**Final status:** **COMPLETE / POSITIVE — offline scope closed**  
**Previous status:** RUNNING / PARTIAL  
**Baseline:** `CAL_OFFLINE_01_DEEP_REDUCTION_20261003.md` + `PROTO_OFFLINE_09_0708_SCHEDULER_STATE_MACHINE_20261003.md` + `PROTO-OFFLINE-10` desired-state reconstruction  
**Controlled change:** no device change. Re-check the remaining calendar unknowns against the complete existing offline corpus, with special attention to whether the newly reconstructed `0708` desired-state scheduler exposes any calendar-page FC03 pulls.  
**Device TX:** none  
**YAML change:** none  
**Heat-pump restart:** none  
**Setting write:** none  
**GitHub change:** none  
**Live experiment state:** unchanged — EXP388 remains RUNNING / PARTIAL

> Scope note: `COMPLETE / POSITIVE` means the **offline reconstruction track is complete** and has reached the evidence ceiling of the existing captures. It does **not** mean every calendar semantic or the live calendar write path is proven. Remaining gaps are explicitly retained as OPEN and require new discriminating evidence.

---

## Hypothesis of the final closure pass

The previous deep reduction had already established the logical calendar record structure, but kept the parent track RUNNING / PARTIAL because five important issues remained:

1. exact weekday-bit ordering;
2. F2/F3/F4 user-facing identities;
3. metadata1 meaning;
4. delete/inactivate transaction details;
5. native desired-state/write behavior for the calendar pages.

The final offline pass tests whether the existing six genuine Online/DCM captures, interpreted with the newly reconstructed `0708` scheduler and desired-state architecture, contain enough hidden evidence to resolve any of those remaining issues without a new live test.

### Result

The structural calendar model remains strongly supported and internally consistent.

The remaining five issues **cannot be resolved further from the existing offline corpus without inventing semantics**.

The most important new negative/closure result is that the genuine captures contain **no observed calendar desired-state pull at all**.

---

# 1. Durable calendar structure

The ordinary calendar transport is twelve contiguous native slave-`0x0F` FC16 pages:

```text
055A/33
057B/33
059C/33
05BD/33
05DE/33
05FF/33
0620/33
0641/33
0662/33
0683/33
06A4/33
06C5/33
```

Together:

```text
055A .. 06E5 = 396 words
```

Logical re-alignment:

```text
F1 = 055A .. 05BB = 98 words
F2 = 05BC .. 061D = 98 words
F3 = 061E .. 067F = 98 words
F4 = 0680 .. 06E1 = 98 words
tail = 06E2 .. 06E5 = 4 words
```

Each function is:

```text
8 × 12-word slot records
+ 2 metadata words
= 98 words
```

This is the final supported ordinary-calendar structural model and supersedes the earlier 99-word interpretation.

---

# 2. Final 12-word slot format

The best-supported slot layout remains:

| Offset | Meaning | Status |
|---:|---|---|
| 0 | schedule mode | VERY STRONGLY SUPPORTED |
| 1 | start minute | VERY STRONGLY SUPPORTED |
| 2 | start hour | VERY STRONGLY SUPPORTED; structurally proven in genuine Eco5 edit |
| 3 | start day | VERY STRONGLY SUPPORTED |
| 4 | start month | VERY STRONGLY SUPPORTED |
| 5 | start year | VERY STRONGLY SUPPORTED |
| 6 | stop minute | VERY STRONGLY SUPPORTED |
| 7 | stop hour | VERY STRONGLY SUPPORTED |
| 8 | stop day | VERY STRONGLY SUPPORTED |
| 9 | stop month | VERY STRONGLY SUPPORTED |
| 10 | stop year | VERY STRONGLY SUPPORTED |
| 11 | weekday / recurrence mask | VERY STRONGLY SUPPORTED |

There is no spare per-slot action/type word. The scheduled action is most plausibly selected by the enclosing function block.

### Mode 0

Controlled local XTR WW_GEBLOKKEERD example:

```text
02-10-2026 18:00 -> 19:00

0000 0000 0012 0002 000A 001A
0000 0013 0002 000A 001A 0000
```

So mode `0` is strongly supported as absolute DATE mode.

### Mode 1

Genuine Eco5 weekly record:

```text
0001 0000 0015 001F 000C 0000
003B 0017 001F 000C 0000 007F
```

Interpretation:

```text
mode = 1
21:00 -> 23:59
31/12/0 date sentinel
weekday mask = 0x007F
```

So mode `1` is strongly supported as recurring DAYS/WEEK mode.

---

# 3. Validity bitmap versus record contents

Metadata word0:

```text
F1 05BA
F2 061C
F3 067E
F4 06E0
```

continues to fit:

```text
bit0 -> slot0 configured
...
bit7 -> slot7 configured
```

The strongest negative-control observation remains F3: the function contains record-looking residual data while its candidate validity bitmap is zero.

Therefore:

**STRONGLY SUPPORTED**

```text
slot validity is determined by metadata0,
not by whether the 12-word body happens to contain non-zero data.
```

This also makes stale record contents after delete/inactivation plausible.

However, the corpus contains no clean locally controlled XTR bitmap edge, so the exact delete operation remains OPEN.

Metadata word1 (`05BB`, `061D`, `067F`, `06E1`) is zero in every complete snapshot and remains OPEN / UNKNOWN.

---

# 4. Function identities — final evidence classification

| Function | Range | Interpretation | Final status |
|---|---|---|---|
| F1 | `055A..05BB` | WW_GEBLOKKEERD | **PROVEN / locally correlated** |
| F2 | `05BC..061D` | EVU / vermogensbegrenzing | **HYPOTHESIS** |
| F3 | `061E..067F` | Stille modus | **HYPOTHESIS** |
| F4 | `0680..06E1` | Temperatuurverlaging | **HYPOTHESIS**, with strong proof that F4 has a real scheduled operational effect |

The commissioning manual lists four ordinary calendar functions before the separate concrete-drying program in the same plausible order, but the manual does not expose protocol addresses. Therefore ordering alone is not sufficient to promote F2/F3/F4 to PROVEN.

No existing capture contains a controlled semantic edit that distinguishes F2, F3 and F4 by user-facing label.

This is a real evidence boundary, not unfinished parsing.

---

# 5. Weekday mask — exact bit order cannot be recovered offline

The corpus contains:

```text
weekday mask = 0000
weekday mask = 007F
```

but no independently labelled subset such as Monday-only, weekday-only, weekend-only, etc.

`0x007F` proves only that the low seven bits participate and that all seven set means all days.

There is no information in the current captures that can distinguish, for example:

```text
bit0 = Monday
```

from:

```text
bit0 = Sunday
```

or any other permutation.

Therefore:

- `word11` as a 7-bit weekday mask: **VERY STRONGLY SUPPORTED**
- exact bit-to-weekday order: **OPEN / NOT IDENTIFIABLE FROM CURRENT CORPUS**

No further offline computation can solve an unlabelled 7-bit permutation from only `0x00` and `0x7F`.

---

# 6. New closure result — no calendar desired-state pull exists in the captured Online traffic

PROTO-OFFLINE-09 established:

```text
W1 = desired-state pull bitmap, low page indices
W0 = structurally likely desired-state pull bitmap, high page indices
```

but only W1 bit0 and W1 bit3 are ever observed asserted.

The twelve ordinary calendar transport pages are native page indices 17 through 28:

```text
index17 = 055A
index18 = 057B
index19 = 059C
index20 = 05BD
index21 = 05DE
index22 = 05FF
index23 = 0620
index24 = 0641
index25 = 0662
index26 = 0683
index27 = 06A4
index28 = 06C5
```

Those are in the **high half** of the 32-page configuration index.

Across all six genuine Online/DCM captures:

```text
0708 requests  = 327
answered        = 302
W0 non-zero     = 0
```

An independent raw-corpus scan for controller FC03 reads of all twelve calendar transport-page starts found:

```text
FC03 055A = 0
FC03 057B = 0
FC03 059C = 0
FC03 05BD = 0
FC03 05DE = 0
FC03 05FF = 0
FC03 0620 = 0
FC03 0641 = 0
FC03 0662 = 0
FC03 0683 = 0
FC03 06A4 = 0
FC03 06C5 = 0
```

### Strong conclusion

The existing genuine captures show calendar pages being **published by controller FC16**, but never being **pulled as desired-state pages by controller FC03**.

Therefore PROTO-OFFLINE-10's proven read-modify-return command primitive for `03E8` and `042E` must **not** be silently generalized to calendar writes.

The natural symmetry:

```text
W0 = high-half desired-state bitmap
```

remains a structural hypothesis only.

A calendar writer must not assert W0 or invent a calendar desired-page response from symmetry.

This is the main reason no further offline work can safely finish the write side of the calendar protocol.

---

# 7. Transport-page versus logical-record boundary

Logical records and native transport pages are different layers.

Examples:

```text
F1 slot2 = 0572..057D   crosses 055A-page -> 057B-page
F1 slot5 = 0596..05A1   crosses 057B-page -> 059C-page
F2 slot0 = 05BC..05C7   crosses 059C-page -> 05BD-page
F3 slot0 = 061E..0629   crosses 05FF-page -> 0620-page
F4 slot0 = 0680..068B   crosses 0662-page -> 0683-page
F4 slot5 = 06BC..06C7   crosses 06A4-page -> 06C5-page
```

This matters materially for any future write implementation.

A single logical slot edit can require coordinated desired-state handling for **two physical native pages**.

Because no calendar desired-state pull has been captured, the required ordering/atomicity/confirmation behavior for such a cross-page edit remains unknown.

---

# 8. F4 natural edit and activation evidence remains valid

Genuine Eco5 traffic naturally changes:

```text
068E: 20 -> 21
```

with every other relevant slot word unchanged.

Alignment:

```text
F4 starts 0680
slot1 starts 068C
068E = slot1 word2 = start hour
```

This independently validates word2 as start hour.

The same capture associates the F4 20:00 boundary with an operational `04A6=0044 / 04A7=1` state, providing strong evidence that F4 is a real scheduled function.

This still does not prove the user-facing label "Temperature Reduction"; that label remains a hypothesis.

---

# 9. Four-word tail remains outside the editable slot model

Tail:

```text
06E2 06E3 06E4 06E5
```

remains outside the four 98-word function blocks.

Known relationship:

```text
0870.word0 = (06E3 << 8) | 06E2
```

The value does not change across the observed F4 start-hour edit, excluding a simple "calendar edit generation counter" interpretation.

Exact semantics remain OPEN.

---

# 10. Concrete drying remains separate

`04D8/count27` continues to fit:

```text
7-word header
+ 10 × (day, supply-temperature) pairs
```

which matches the commissioning manual's maximum of ten concrete-drying points.

Therefore BETONDROOG_PROG is not part of F1..F4.

Header words 0..4 remain unresolved.

---

# 11. Final evidence classification

## Observed facts

- Ordinary calendar transport spans twelve contiguous count33 FC16 pages, 396 words total.
- Logical re-alignment gives 4 × 98-word function blocks + 4-word tail.
- Every function fits 8 × 12-word slots + 2 metadata words.
- Controlled local F1 record matches absolute date/time encoding.
- Genuine Eco5 weekly records match recurring mode with `0x007F` all-days mask.
- F4 word2 naturally changes `20 -> 21` as a start-hour edit.
- Metadata0 matches slot occupancy across independent snapshots.
- Stale-looking F3 record data exists while F3 metadata0 is zero.
- Across 302 answered genuine `0708` cycles, W0 is never non-zero.
- No FC03 desired-page request for any of the twelve calendar transport pages occurs in the six genuine captures.

## Strong conclusions

1. The **read/export structure** of the ordinary calendar is sufficiently reconstructed for implementation of a passive decoder.
2. Mode0 = absolute date; mode1 = recurring week/day form.
3. Word11 is a seven-bit recurrence mask; `0x7F` = all seven days.
4. Metadata0 is the slot-validity/configuration bitmap.
5. Function/action semantics live at function-block level rather than in a spare per-slot type word.
6. F1 = WW_GEBLOKKEERD is locally confirmed.
7. F4 has a real scheduled operational effect.
8. No current genuine capture demonstrates the **calendar desired-state write path**.
9. PROTO-OFFLINE-10's full-page desired-state primitive cannot yet be applied to calendar pages as a proven behavior.

## Hypotheses retained

- F2 = EVU / vermogensbegrenzing.
- F3 = Stille modus.
- F4 = Temperatuurverlaging.
- W0 is the high-half desired-state bitmap for page indices16..31.
- Delete/inactivate may primarily clear the slot-validity bit while leaving stale body data.

## Open / requires new discriminating evidence

- weekday bit order;
- F2/F3/F4 label confirmation;
- metadata1 semantics;
- local XTR add/delete bitmap edge;
- delete transaction/body rewrite behavior;
- calendar desired-state W0 behavior;
- cross-page calendar write ordering/atomicity;
- tail `06E2..06E5`;
- concrete-drying header words0..4.

---

# 12. Final status and next evidence

## CAL-OFFLINE-01

**COMPLETE / POSITIVE — offline scope closed**

Reason:

- the ordinary calendar structure has been reconstructed to a useful decoder-level model;
- every unresolved item was explicitly checked against the available offline evidence;
- the remaining gaps are not hidden parsing work: the necessary discriminating events simply do not exist in the current corpus.

The next step is therefore **not another broad offline pass**.

The smallest high-value new evidence is passive-only local XTR capture of either:

1. one weekly entry using a known subset of weekdays, to decode bit order; or
2. one add/delete cycle, to prove metadata0 transition and body-retention behavior.

A live calendar writer is **not justified yet**, because no calendar desired-state FC03 pull/W0 activation has ever been observed.

No active experiment is started by this closure.