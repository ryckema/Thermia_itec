# Thermia iTec XTR M — Offline Unknown-Page Correlation

**Date:** 2026-10-02  
**Track:** PROTO-OFFLINE-01  
**Status:** COMPLETE / POSITIVE — offline evidence analysis only  
**Device TX:** none  
**Live experiment status:** unchanged

## Hypothesis

The three highest-value unresolved native `0x0F` targets from the protocol reduction (`04A6/count13`, `0424` inside `0410/count22`, and `06F4/count19`) can be narrowed by time-correlating existing local XTR traffic with genuine iTec Eco5 + Thermia Online captures and the existing cross-model register map.

## Controlled change

None. Existing captures/logs only.

---

## 1. `04A6/count13`

### Local XTR EXP296 correlation

In the later local XTR runtime log, `04A6/count13` is emitted very frequently.

Observed runtime correlations:

| UI / controller condition | `04A6` word0 | `04A7` word1 | `04B0` word10 |
|---|---:|---:|---:|
| SG Normal `(0-0)` | `0000` | `0000` | `4020` |
| SG Enhanced `(0-1)` | `0041` | `0001` | `4020` |
| SG Normal `(0-0)` after Enhanced | `0000` | `0000` | `4020` |
| SG Blocked `(1-0)` | `0042` | `0001` | `4020` |

Timing is tight:
- SG Enhanced is published at 21:55:52.192; `04A6=0041 / 04A7=1` appears at 21:55:53.768.
- SG returns Normal at 21:56:36.902; the page returns to `0000/0000` at 21:56:37.369.
- SG Blocked is published at 22:24:15.180; `04A6=0042 / 04A7=1` appears at 22:24:16.925.

The Enhanced transition also coincides with controller context `A80C=0041`, but the Blocked transition does not require a matching `A80C=0042`, so `04A6 word0` is not simply a copy of `A80C`.

### Genuine Eco5 + Online

In the genuine 2026-09-26 capture, the active runtime page uses:
- `04A6=0000 / 04A7=0`, or
- `04A6=0044 / 04A7=1`.

The 2026-09-28 genuine capture stays at `0000/0000`.

Successful Online challenge/approval events occur while `04A6` is both zero and non-zero. Therefore `04A6` is **not** an Online/DCM approval flag.

`04B0` is normally:
- local XTR: `4020`;
- Eco5: `4A20`;
with one genuine Eco5 transient `4A00`.

### Historical local conflict

An older local XTR capture contains a completely different `04A6/count13` payload:

`0000,0003,0004,0002,003F,0050,003C,0002,0000,003C,000F,001E,0000`

This must be preserved. It means the complete page cannot yet be treated as a fixed SG-only schema across all historical/session contexts.

### Classification

**Observed facts**
- In current local EXP296 runtime, SG mode transitions and `04A6/04A7` transitions are tightly correlated.
- `04A7=1` in the locally observed non-Normal SG states and `0` in Normal.
- `04A6` is not required for genuine Online approval.
- `04B0` is model/context dependent and mostly stable.

**Strong conclusion**
- In the current XTR DCM-style runtime context, the first two words of `04A6/count13` carry SG/operational-state information rather than Online login/approval state.

**Strongly supported mapping**
- `04A6=0000, 04A7=0` -> SG Normal
- `04A6=0041, 04A7=1` -> SG Enhanced
- `04A6=0042, 04A7=1` -> SG Blocked

**Hypothesis**
- the low two bits of non-zero `04A6` may encode the two SG inputs, with `0x0043` as a possible `(1-1)` state. This is not observed and must not be promoted.

**Open**
- why the older local capture has a completely different payload regime;
- exact semantics of `04B0` and its `0x20` bit;
- the genuine Eco5 `04A6=0044` meaning.

---

## 2. `0424` inside `0410/count22`

The attached cross-model DHP/AQ register table has the contiguous sequence:

- register 68: Hotwater start temperature
- 69: Hotwater operating time
- 70: Heatpump operating time
- 71: Legionella interval
- 72: Legionella stop temperature
- 73: Integral limit A1
- 74: Heatpump hysteresis
- 75: Returnline temperature, max limit
- 76: Minimum starting interval

Two anchors in this sequence are already locally mapped on the XTR:

- native `041D` = Hot Water Start Temperature
- native `041E` = Hot Water Operating Time

Those correspond to cross-model entries 68 and 69. Continuing the same one-register sequence gives:

| Native | Cross-model semantic candidate |
|---|---|
| `041D` | Hot Water Start Temperature — locally confirmed anchor |
| `041E` | Hot Water Operating Time — locally confirmed anchor |
| `041F` | Heatpump Operating Time |
| `0420` | Legionella Interval |
| `0421` | Legionella Stop Temperature |
| `0422` | Integral Limit A1 |
| `0423` | Heatpump Hysteresis |
| `0424` | **Returnline Temperature Max Limit** |
| `0425` | Minimum Starting Interval |

The actual page values are also plausible:

Local XTR later `0410/count22`:
`... 041D=47, 041E=30, 041F=7, 0420=0, 0421=60, 0422=13, 0423=6, 0424=55, 0425=0`

Genuine Eco5 2026-09-26:
`... 041D=39, 041E=40, 041F=7, 0420=1, 0421=62, 0422=13, 0423=6, 0424=57, 0425=0`

Genuine Eco5 2026-09-28:
same except `0424=60`.

### Classification

`0424 = Returnline Temperature Max Limit`:

**STRONGLY SUPPORTED**, but not locally PROVEN by a controlled XTR UI change.

The confidence is higher than a simple value guess because two adjacent registers (`041D` and `041E`) independently provide local sequence anchors.

---

## 3. `06F4/count19`

This page is substantially more decoded than previously thought.

Across **all 25** `06F4/count19` frames in the two genuine Eco5 + Online captures:

`06F4..06F8` exactly equal the first five controller context words `A80C..A810` from the immediately preceding slave `0x02` FC17 transaction.

Observed forms:

Eco5 2026-09-26:
- `06F4..06F8 = 0040,0000,0008,003C,000A`
- or `0040,0000,0028,003C,000A`

Eco5 2026-09-28:
- `0040,0000,0028,000A,000A`

These exactly match:
- `A80C`
- `A80D`
- `A80E`
- `A80F`
- `A810`

for every compared frame.

Also, `0701` (offset 13 in the `06F4` page) exactly equals slave `0x06` controller-written `AFDC` in **all 25** genuine frames:

Eco5 2026-09-26:
- `A80E=0008` / `AFDC=0000` -> `06F6=0008` / `0701=0000`
- `A80E=0028` / `AFDC=0020` -> `06F6=0028` / `0701=0020`

Eco5 2026-09-28:
- `A80E=0028` / `AFDC=0010` -> `06F6=0028` / `0701=0010`

The relation also appears locally.

Historical local XTR:
- controller context immediately before `06F4`: `0040,0000,0028,000A,000A,...`
- `AFDC=0010`
- `06F4` begins `0040,0000,0028,000A,000A`
- `0701=0010`

Later local EXP296:
- controller context: `A80C=0040, A80D=0000, A80E=0028, A80F=000A, A810=000A`
- local `AFDC=16`
- `06F4` again begins `0040,0000,0028,000A,000A`
- `0701=0010`.

### Classification

**PROVEN / directly observed relation**
- `06F4 = A80C`
- `06F5 = A80D`
- `06F6 = A80E`
- `06F7 = A80F`
- `06F8 = A810`
- `0701 = AFDC`

The semantic meanings of `A80C/A80E/A80F/AFDC` themselves remain governed by their existing evidence levels; this finding is about the exact mirroring relationship.

### Strong conclusion

`06F4/count19` is not merely an unknown final configuration page. At least part of it is a **controller/integration context snapshot** that copies state from the controller (`0x02`) and accessory-facing (`0x06`) domains into the native `0x0F` page family.

The other `06F4` words remain unresolved. Older local traffic contains additional non-zero words not present in the later EXP296 page, so the full page schema still needs contextual reduction.

---

## Result

**PROTO-OFFLINE-01 — COMPLETE / POSITIVE**

No device action was performed.

Most valuable durable outcomes:

1. `04A6/04A7` are strongly linked to local SG operating mode in the current DCM-style runtime and are not Online approval flags.
2. `0424` is strongly supported as **Returnline Temperature Max Limit** through a contiguous cross-model map anchored by two locally confirmed XTR registers.
3. `06F4/count19` contains exact mirrors of `A80C..A810`, and `0701` mirrors `AFDC`; this is now a directly observed structural relationship rather than an unknown-page guess.

## Next offline question

The strongest unresolved issue exposed here is why `04A6/count13` has a radically different historical local payload regime. This should be treated together with the already-observed historical/current page-shape drift, rather than forcing one fixed schema across all captures.