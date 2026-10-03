# Thermia iTec XTR M — unresolved runtime-field reduction

**Date:** 2026-10-03  
**Track:** PROTO-OFFLINE-08  
**Status:** COMPLETE / POSITIVE — offline analysis only  
**Baseline:** PROTO-OFFLINE-06 automated runtime-source correlation, with PROTO-OFFLINE-05 runtime-family model  
**Numbering note:** `PROTO-OFFLINE-07` is already occupied in the project Library by `PROTO_OFFLINE_07_FIRMWARE_SEMANTIC_IDENTITY_MINING_20261003.md`; this run therefore uses `PROTO-OFFLINE-08`.  
**Controlled change:** no new traffic or corpus; specifically reduce unresolved words in `0834/count18`, `0864/count4`, and `0870/count17` by correlating them against native `0x02` controller cycles, modern `0x1E` command/telemetry state, cross-platform runtime pages, and the XTR commissioning-manual menu structure.  
**Device TX:** none  
**YAML change:** none  
**Heat-pump restart:** none  
**GitHub change:** none  
**Live experiment status:** unchanged — `EXP388` remains RUNNING / PARTIAL

## Hypothesis

Remaining unresolved fields in the `07D0..0870` Online/DCM runtime ring are not arbitrary values. At least some are expected to be:

- direct or normalized mirrors of already-observed controller/outdoor state;
- derived booleans for compressor transition states;
- controller-cycle based runtime accumulators;
- service counters exposed by the XTR information menus.

**Result:** supported.

---

## Corpus

Raw captures analysed:

- `thermia_capture_20260924_210001(1).log`
- `thermia_capture_20260925_071517.log`
- `thermia_capture_20260925_090209.log`
- `thermia_capture_20260925_090550.log`
- `itec_eco5_gateway_20260926.log`
- `itec_eco5_gateway_20260928.log`

The first four are genuine older Online/DCM reference captures. The two `itec_eco5_gateway_*` files are genuine Eco5 + Online captures using the modern `0x1E` outdoor-unit topology.

The commissioning-manual AI transcription was used only as a semantic anchor for the names and ordering of `BEDRIJFS TIJD` and `ONTDOOIEN` counters; it was not used to invent register addresses.

---

# 1. `0865` — compressor-running boolean reconfirmed

Across all modern Eco5 `0864/count4` samples with a valid current `0x1E` live image:

```text
0865 = 1  <=>  1E:000B compressor frequency > 0
0865 = 0  <=>  1E:000B compressor frequency = 0
```

Result:

- Eco5 2026-09-26: 32/32
- Eco5 2026-09-28: 16/16
- combined: **48/48 exact**

This independently reconfirms the PROTO-OFFLINE-06 result.

**Status: PROVEN / structural in genuine Eco5 + Online traffic.**

The semantic label `compressor running` is strongly supported by the independently decoded `0x1E:000B` frequency field.

---

# 2. `0866` — compressor start / pre-run transition

A second boolean in the same page now has a clean derived-state relationship.

Across the same 48 modern samples:

```text
0866 = 1
    <=> command word7 = 1
        AND command word8 = 1
        AND compressor frequency = 0

0866 = 0 otherwise
```

Result: **48/48 exact**.

Only one positive `0866=1` sample exists, so the semantic name must remain slightly cautious.

Observed transition:

```text
1113.177 s:
0864/count4 = 0000 0000 0001 00E8
cmd7=1, cmd8=1
compressor frequency=0
outdoor status=0x0221

1138.374 s:
0864/count4 = 0000 0001 0000 00E8
cmd7=1, cmd8=1
compressor frequency=16 Hz
```

**STRONGLY SUPPORTED:** `0866` is a start-pending / commanded-but-not-yet-running indicator.

It is not yet locally proven on the XTR M itself.

---

# 3. `083C` — inverse start-transition code

`083C` on the `0834/count18` page is also explained by the same transition.

For all 43 modern `0834` samples with complete current `0x1E` state:

```text
083C = 0000
    <=> cmd7=1 AND cmd8=1 AND compressor frequency=0

083C = 0080 otherwise
```

Result: **43/43 exact**.

So `083C` is not a generic constant. It flips only during the commanded-start / pre-run state seen simultaneously in `0866`.

**PROVEN / structural correlation in the Eco5 corpus.**  
**Semantic name:** OPEN; safest description is `inverse pre-run/start-transition code`.

---

# 4. `083B` — active-runtime controller-cycle remainder

This is the strongest new reduction in the `0834` page.

During the long Eco5 compressor-active segment, `083B` evolves as:

```text
19 -> 43 -> 7 -> 27 -> 51 -> 11 -> 31 -> 51 -> 11 -> 35 -> 55 -> 15 -> 35 -> 55 -> 15
```

For every one of the **14 adjacent intervals** tested, the modulo-60 increase of `083B` equals exactly the number of `0x02 FC17` controller polling cycles in that interval.

Examples:

```text
25.221 s: 19 -> 43 = +24 ticks ; 24 controller polls
25.209 s: 43 ->  7 = +24 mod 60 ; 24 controller polls
20.967 s:  7 -> 27 = +20 ticks ; 20 controller polls
25.203 s: 27 -> 51 = +24 ticks ; 24 controller polls
```

This continues exactly across all 14 checked intervals.

Important negative discriminator:

- it is **not literal RTC seconds**;
- the actual `0858` RTC-second field tracks wall time normally;
- `083B` instead follows the approximately 1.05 s controller-poll cadence.

In the Eco5 2026-09-28 idle capture, `083B` initially remains latched at `35` while the compressor is off and later becomes `0`, so the precise reset/latch rule is still open.

**Strong conclusion:** `083B` is a modulo-60 controller-cycle accumulator associated with compressor-active runtime, not a generic status bitfield and not literal seconds.

Safest current name:

```text
083B = compressor-active controller-cycle remainder / sub-minute runtime ticks
```

Exact firmware variable name remains unknown.

---

# 5. `087B..087D` — defrost-counter group identified

The XTR commissioning manual exposes exactly three consecutive values under `INFORMATIE -> ONTDOOIEN`:

1. `ONTD.PERIODES` — total completed defrost cycles;
2. `TUSSEN. 2 ONTD.` — compressor runtime in minutes between the last two defrosts;
3. `LAATSTE ONTD.P.` — compressor runtime in minutes since the last defrost.

The `0870/count17` runtime page contains a highly suggestive three-word group at exactly `087B..087D`, bounded by zero/reserved words.

Observed values:

| Corpus | `087B` | `087C` | `087D` |
|---|---:|---:|---:|
| older genuine Online/DCM | 3122 | 422 | 15462 |
| Eco5 2026-09-26 | 298 | 1475 | 30729 -> 30734 |
| Eco5 2026-09-28 | 298 | 1475 | 30811 |

The behavior of the third word is especially diagnostic:

- five `087D` increments were observed during the Eco5 compressor-running interval;
- every observed increment occurred while `1E:000B` compressor frequency was non-zero;
- no `087D` changes occurred in the Eco5 2026-09-28 idle sample set;
- the increment rate is compatible with a minute-level accumulator driven by the same ~1.05 s controller-cycle clock.

This materially refines the previous generic description of `087D` as a cumulative compressor-runtime counter.

### Current mapping

```text
087B  STRONGLY SUPPORTED -> ONTD.PERIODES
087C  STRONGLY SUPPORTED -> TUSSEN. 2 ONTD.
087D  VERY STRONGLY SUPPORTED -> LAATSTE ONTD.P.
                              compressor runtime since last defrost
```

`087D` has the strongest behavioral evidence. `087B` and `087C` currently rely on group structure, order, plausible cross-system values, and the exact three-counter manual match; no defrost event was captured in this corpus to produce a live edge.

These are **not yet PROVEN / locally confirmed on the XTR UI**, because no user-supplied `INFORMATIE -> ONTDOOIEN` readout is available for a direct value cross-check.

---

# 6. `0872..0878` — seven-word operating-time candidate group

Immediately before the identified defrost triple, the same page contains seven populated positions:

```text
0872 0873 0874 0875 0876 0877 0878
```

The XTR manual independently lists exactly seven `INFORMATIE -> BEDRIJFS TIJD` counters:

```text
COMPRESSOR
VERWARMING
KOELING
WARMWATER
BIJVERW_1
BIJVERW_2
BIJVERW_3
```

Observed page values:

```text
older genuine reference:
9763, 10, 10, 10, 12091, 124, 170

Eco5 2026-09-26:
501, 423, 437, 423, 201, 0, 0

Eco5 2026-09-28:
501, 423, 437, 423, 202, 0, 0
```

The `7 values + padding + 3 defrost values + padding` layout is structurally striking.

However, the current corpus does **not** justify assigning the seven labels one-to-one in register order. The values cannot yet be reconciled safely with known elapsed operating times across the different platforms, and only `0876` changes between the two Eco5 capture dates.

**HYPOTHESIS:** `0872..0878` is the normalized `BEDRIJFS TIJD` seven-counter group.  
**OPEN:** exact field order, unit/scaling, and whether all platforms use identical semantics.

A single XTR UI snapshot of all seven `BEDRIJFS TIJD` values would be enough to test this without any bus write.

---

# 7. `0867` — static platform/topology fingerprint

`0867` remains completely static inside each platform corpus:

```text
older genuine Online/DCM: 0016
Eco5 + Online:            00E8
```

It does not change across idle, commanded-start, or running states and no direct contemporary mirror was found in the tested native source fields.

**STRONGLY SUPPORTED:** this is a platform/model/software/capability constant or limit, not ordinary runtime telemetry.

**OPEN:** exact semantic identity.

Do not name it as a model ID or software version without new evidence.

---

# 8. `0834` itself — still open

`0834` is usually zero and occasionally `0100`.

Later in the Eco5 active-run segment, two `0100` observations are separated by about 63 seconds / 60 controller cycles and occur at the same controller-poll phase. This is compatible with a short periodic/accounting pulse, but earlier `0100` observations do not yet allow a unique rule.

No single current `0x02`, `0x06` or `0x1E` source field explains it exactly.

**Status: OPEN / HYPOTHESIS ONLY.**

Do not assign a semantic name yet.

---

# 9. Revised interpretation of `0870/count17`

`0870/count17` should no longer be treated as one homogeneous counter array.

Current best model:

```text
0870           calendar/runtime context bridge
0871           zero/reserved in corpus
0872..0878     seven-value operating-time candidate group  [HYPOTHESIS]
0879..087A     zero/reserved in corpus
087B..087D     defrost counter group                        [STRONGLY SUPPORTED]
087E..0880     zero/reserved in corpus
```

`0870` word0 retains the already-established relation:

```text
0870 = (06E3 << 8) | 06E2
```

Therefore the page is a **mixed normalized service/runtime export**, not a raw physical register bank and not a pure operating-time page.

---

# Evidence classification

## Observed facts

- `0865 == (compressor frequency > 0)` in 48/48 modern samples.
- `0866 == (cmd7 && cmd8 && frequency == 0)` in 48/48 modern samples; only one positive event exists.
- `083C` is `0000` exactly in the same pre-run condition and `0080` otherwise in 43/43 usable modern samples.
- modulo-60 `083B` changes equal the `0x02 FC17` poll count in all 14 consecutive active-run intervals tested.
- `087D` changes five times in the Eco5 active segment and zero times in the compared Eco5 idle sample set.
- `087B/087C` stay fixed while `087D` advances.
- the XTR manual contains exactly three defrost counters and exactly seven operating-time counters.
- `0867` is `0016` on the older genuine platform and `00E8` on Eco5 throughout the available runtime states.

## Strong conclusions

1. `083B` is a controller-cycle runtime accumulator/remainder, not literal RTC seconds.
2. `0865/0866` represent mutually exclusive running versus commanded-start/pre-run phases in the genuine Eco5 runtime export.
3. `083C` carries the same pre-run transition in inverted/coded form.
4. `087B..087D` is very likely the three-value defrost statistics group; `087D` is especially strongly supported as compressor-runtime-since-last-defrost.
5. `0867` is a static platform/topology-dependent constant, not normal changing telemetry.

## Hypotheses

- `087B = ONTD.PERIODES`, `087C = TUSSEN. 2 ONTD.`, `087D = LAATSTE ONTD.P.` in manual order.
- `0872..0878` is the seven-value `BEDRIJFS TIJD` group.
- `0834=0100` is a short periodic/accounting pulse.

## Unknowns

- exact firmware identity/name of `083B`;
- reset/latch rule for `083B` after compressor stop;
- exact semantic name of `083C` and `0866`;
- exact identity of `0867` (`0016` versus `00E8`);
- exact label/order/scaling of `0872..0878`;
- direct XTR UI confirmation of `087B..087D`;
- semantic cause of `0834=0100`.

---

# Result

**PROTO-OFFLINE-08 — COMPLETE / POSITIVE**

The unresolved runtime family is materially reduced without any heat-pump interaction.

The most important new result is the likely identification of the `087B..087D` defrost-statistics group, together with a strong correction/refinement of `087D`: it is better modeled as the compressor-runtime-since-last-defrost counter than as an unspecified lifetime compressor-runtime counter.

The `0834` page is also substantially clearer: `083B` is a modulo-60 active-runtime controller-cycle accumulator, `083C` marks the inverse pre-run state, and the `0864` page exposes separate pre-run and running booleans.

No live experiment status changed. `EXP388` remains **RUNNING / PARTIAL**.
