# Thermia Protocol Reduction — Offline Step 3

**Date:** 2026-10-02  
**Status:** COMPLETE / POSITIVE — offline reduction only  
**Device change:** none  
**GitHub write:** none

## Purpose

Turn the current project knowledge into a machine-readable protocol database rather than leaving the information distributed over experiment notes, YAML and captures.

This reduction preserves evidence classes and does not promote hypotheses to local XTR proof.

## Corpus

Parsed **22,344** raw Modbus-RTU frames from six attached captures.

- local XTR captures: 4
- genuine iTec Eco5 + Thermia Online captures: 2
- CRC failures: **0**

The raw capture inventory is in `thermia_protocol_capture_inventory.csv`.

## Generated database

- `thermia_protocol_database.json` — combined machine-readable source
- `thermia_protocol_page_census.csv` — one row per native 0x0F page
- `thermia_protocol_register_observations.csv` — per-word raw variability by source class
- `thermia_protocol_semantic_register_map.csv` — known/proposed semantics with evidence status
- `thermia_protocol_selector_map.csv` — complete 32-page 0708 current/PUSH and desired/PULL bitmap map

## 1. Current 32-page selector model

The current page order is:

```text
W3/W1 low half:
03E8 03FC 0410 042E 0442 0456 046A 047E
0492 04A6 04BA 04D8 04F6 050A 051E 0532

W2/W0 high half:
0546 055A 057B 059C 05BD 05DE 05FF 0620
0641 0662 0683 06A4 06C5 06EA 06F1 06F4
```

`W3/W2` are the current/PUSH side and the mirrored `W1/W0` words are the desired/PULL side.

The database deliberately labels the overall map **STRONGLY SUPPORTED** while retaining local proof only for the page paths actually exercised on this XTR.

## 2. Important historical/current page-shape difference

The attached historical local XTR captures contain shorter page shapes for four pages:

| Page | historical local raw | current v4.1 | genuine Eco5 |
|---|---:|---:|---:|
| 03E8 | 13 | 14 | 14 |
| 0410 | 21 | 22 | 22 |
| 0492 | 9 | 11 | 11 |
| 051E | 9 | 10 | 10 |

This is intentionally **not normalized away**.

The current write engine and later project state use the extended shapes, while the older raw local captures directly prove that shorter forms existed in the historical local context.

### Interpretation

**Observed fact:** the shape difference is real in the source corpus.

**Strong conclusion:** the database must support page-shape history/version/session context instead of assuming one eternal count per page.

**Hypothesis:** the extended shapes may be Online/DCM-session dependent or may reflect later controller/session behavior. The attached early raw logs alone cannot decide why.

**Unknown:** the exact transition condition.

## 3. Highest-value raw unknown: 04A6/count13

Across the two genuine Eco5 + Online captures, `04A6/count13` occurs **583 times**, much more often than ordinary one-pass configuration pages.

Only three words vary in that corpus:

- `04A6`: `0000 ↔ 0044`
- `04A7`: `0000 ↔ 0001`
- `04B0`: `4A00 ↔ 4A20`

The attached local XTR snapshots have stable but different values.

This page is therefore now a top offline mapping candidate. It behaves more like a live native state/configuration page than an inert setup block.

## 4. Clean one-word delta at 0410:0424

In the attached genuine Eco5 captures, page `0410/count22` varies only at offset 20:

```text
0424: 0039 ↔ 003C
```

The surrounding page is otherwise identical in the available observations.

`041D` and `041E` are already locally mapped to Hot Water Start Temperature and Warm Water Time. `0424` is therefore an unusually clean unresolved field in a partially understood service page.

## 5. 06F4 final-sync page has three live fields

In genuine Eco5 Online traffic, the final initial-sync page `06F4/count19` varies at:

```text
06F6: 0008 ↔ 0028
06F7: 000A ↔ 003C
0701: 0000 / 0010 / 0020
```

Semantics remain open. Because `06F4` closes the current initial-sync family, these fields deserve correlation against session/runtime state before speculative register labels are assigned.

## 6. Calendar reduction integrated into the database

The corrected model is preserved:

```text
F1 055A..05BB  WW_GEBLOKKEERD locally anchored
F2 05BC..061D  EVU candidate
F3 061E..067F  Silent Mode candidate
F4 0680..06E1  Temperature Reduction candidate
```

Each block is `8 × 12-word records + 2 metadata words = 98 words`.

Candidate slot-validity bitmaps:

```text
05BA 061C 067E 06E0
```

The register CSV expands all 384 logical calendar record words so future captures can be diffed directly by function/slot/field.

## 7. Concrete drying separated from ordinary calendar storage

`04D8/count27` is represented as:

```text
7-word header
+ 10 × (day/index, supply temperature)
```

The candidate hysteresis and point-count positions are retained as **STRONGLY SUPPORTED**, while header words 0..4 remain **OPEN / UNKNOWN**.

## 8. Exact 06E2/06E3 ↔ 0870 relationship

The database records the repeated equality:

```text
(06E3 << 8) | 06E2 == 0870.word0
```

Observed across the local XTR and both genuine Eco5 datasets.

It is stored as a repeated structural relation, **not** labeled as a checksum/pointer/ID.

## 9. Evidence separation

The semantic map contains separate status fields for:

- PROVEN / locally confirmed
- STRONGLY SUPPORTED
- HYPOTHESIS
- OPEN / UNKNOWN
- cross-model-only evidence
- TEST-only candidates

No candidate becomes proven simply because it has an address or a Home Assistant control.

## 10. Priority queue for further offline work

| priority | target | evidence | next_action |
| --- | --- | --- | --- |
| 1 | Historical/current page-shape drift | Attached historical local raw captures show 03E8/13, 0410/21, 0492/9 and 051E/9, while current v4.1 recognizes 03E8/14, 0410/22, 0492/11 and 051E/10 and genuine Eco5 uses the extended shapes. | Locate/reduce the later local EXP logs that established the extended XTR shapes; do not overwrite either historical observation. |
| 2 | 04A6/count13 | 583 FC16 frames in the two genuine Eco5 logs; dynamic offsets 0,1,10 (04A6,04A7,04B0). | Correlate 04A6/04A7/04B0 against runtime state transitions and local XTR captures. |
| 3 | 0410 register 0424 | Genuine Eco5 0410/count22 varies only at offset20 (0424: 0x0039↔0x003C) in attached captures. | Timeline-correlate 0424 with DHW/service state and known UI changes. |
| 4 | 06F4 final-sync dynamic words | Eco5 varies at 06F6, 06F7 and 0701; 0701 observed 0/16/32. | Correlate these words around genuine Online approval and later runtime windows. |
| 5 | Calendar F2/F3/F4 semantics | 98-word structure strong; only F1 is locally anchored. | Future passive one-variable UI correlations when physically back at the XTR. |
| 6 | 06E2..06E5 / 0870 relationship | (06E3<<8)\|06E2 equals 0870 word0 across local XTR and both Eco5 datasets. | Correlate 0870 word0 changes with the same-session 06E2/06E3 timeline. |

## Result

**Offline Step 3: COMPLETE / POSITIVE.**

The project now has a normalized protocol dataset suitable for:

- automatic diffing of future captures;
- checking whether a new frame matches a known page shape;
- selecting unknown words by actual variability rather than guesswork;
- separating local XTR evidence from genuine Eco5/Online evidence;
- generating future read-only entities from proven fields;
- preventing older observations from being silently overwritten by newer interpretations.

The most important new research issue surfaced by this reduction is the **historical/current page-count drift** on `03E8`, `0410`, `0492` and `051E`.