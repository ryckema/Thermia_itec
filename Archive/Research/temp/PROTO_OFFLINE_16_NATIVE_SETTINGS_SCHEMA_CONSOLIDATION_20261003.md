> **Current-status note — HISTORICAL SNAPSHOT / PARTIALLY SUPERSEDED (2026-10-03).** The profile-drift architecture remains durable, but several local-XTR evidence tiers in this report were later upgraded by live EXP results. PROTO-OFFLINE-20 is the current reconciliation overlay: e.g. `03E9/03EA/03EC/03ED/03EE/03EF/03F0`, local `042E/042F`, several cooling controls, and `0553` have stronger local write/semantic evidence than recorded here. Preserve this report as the offline cross-profile snapshot; use PROTO-OFFLINE-20 for current evidence status.

# Thermia iTec XTR M — Native settings/register schema consolidation

**Date:** 2026-10-03  
**Track:** PROTO-OFFLINE-16  
**Status:** COMPLETE / POSITIVE — offline evidence-consolidation scope closed  
**Roadmap item:** #7 — complete the native settings/register database  
**Baseline:** local XTR UI-correlation experiments + genuine Online/DCM desired-state captures + PROTO-OFFLINE-09/10 scheduler/write reconstruction + public Thermia Online ATEC/iTec profile dumps + firmware/manual semantic evidence  
**Controlled change:** no device change. Reconcile all known native register semantics into one profile-aware database and explicitly resolve contradictions instead of copying one cross-model register table wholesale.  
**Device TX:** none  
**YAML change:** none  
**Heat-pump restart:** none  
**Setting write introduced by this analysis:** none  
**GitHub change:** none  
**Live experiment status:** unchanged — EXP388 remains RUNNING / PARTIAL

---

## Hypothesis

The Thermia Online `registerIndex` namespace substantially overlaps the native `0x0F` numeric register namespace, but the **semantic assignment is installation-profile/model dependent**.

A useful XTR database must therefore store:

```text
numeric address
+ page family
+ semantic label
+ source profile
+ local-XTR confirmation state
+ writable/read-only evidence
+ value domain
```

rather than one universal:

```text
address -> meaning
```

table.

**Result: proven at architecture level.**

The same numeric address can have different semantics in different Thermia profiles.

---

# 1. Major correction: there is no universal Thermia `registerIndex` map

Public Online profile data gives several direct contradictions.

## `042E` / decimal 1070

ATEC / DHP-AQ profile:

```text
042E = REG_SER_HEATING_INTEGRALA1
writable
range -250 .. -5
```

iTec profile:

```text
042E = REG_HOT_WATER_STATUS
writable
0 = OFF
1 = ON
```

These cannot be the same semantic parameter.

## Operation Mode

ATEC / iTec:

```text
0553 / decimal 1363 = REG_OPERATIONMODE
```

older Diplomat:

```text
decimal 51 = REG_OPERATIONMODE
```

NCP fixtures:

```text
decimal 151 = REG_OPERATIONMODE
```

## Hot Water Status

iTec:

```text
042E / decimal 1070
```

NCP:

```text
decimal 1059
```

## Runtime examples

ATEC:

```text
return temperature = 07D1
outdoor temperature = 07E7
0848 = Integral LSD
```

iTec:

```text
return temperature = 07D2
outdoor temperature = 07DA
0848 = PID
```

### Strong conclusion

The numeric namespace is **profile-indexed**.

A register name from one public DCM profile may be an excellent hypothesis for another closely related profile, but it is not automatically a Thermia-wide fact.

This supersedes the earlier working shortcut:

> “public Online registerIndex is a universal native address-to-semantic map.”

The better statement is:

> **for a given controller/profile family, Online registerIndex often equals the native `0x0F` numeric register address; the semantic schema attached to that index is profile-dependent.**

---

# 2. XTR settings core — current evidence-ranked map

## `03E8..03F0` heating-curve family

Both public ATEC and iTec profiles independently use:

```text
03E8 Heat Curve
03E9 Heating Minimum
03EA Heating Maximum
03EB Curve +5
03EC Curve 0
03ED Curve -5
03EE Heating Stop
03F0 Room Factor
```

with identical value-domain shapes.

Public profile ranges:

```text
03E8 Heat Curve       22..56, step 1
03E9 Heating Minimum  10..50, step 1
03EA Heating Maximum  40..85, step 1
03EB Curve +5         -5..5, step 1
03EC Curve 0          -5..5, step 1
03ED Curve -5         -5..5, step 1
03EE Heating Stop      0..40, step 1
03F0 Room Factor       0..4, step 1
```

### Local XTR classification

```text
03E8 Heat Curve       PROVEN / locally confirmed
03E9 Heating Min      STRONGLY SUPPORTED
03EA Heating Max      STRONGLY SUPPORTED
03EB Curve +5         PROVEN / locally confirmed
03EC Curve 0          STRONGLY SUPPORTED
03ED Curve -5         STRONGLY SUPPORTED
03EE Heating Stop     STRONGLY SUPPORTED
03F0 Room Factor      STRONGLY SUPPORTED
```

Why the intermediate entries are not all called locally proven:

- their profile semantics agree across ATEC and iTec;
- they sit in the locally observed contiguous heating page;
- they align with the firmware-derived semantic ordering;
- but a dedicated reversible XTR UI-causality test has not been recovered for every individual word.

That distinction is retained deliberately.

---

# 3. `03F4` room setpoint is stronger than the public profile tables suggest

`03F4` is not exposed as a normal writable item in the two public profile snippets used for the table above.

But protocol evidence is stronger.

## Genuine Online/DCM

PROTO-OFFLINE-10 contains two reversible semantic commands:

```text
03F4: 20 -> 30
03F4: 30 -> 20
```

In both cases:

1. scheduler requests desired page `03E8`;
2. DCM returns the complete page image with only `03F4` changed;
3. controller republishes the page byte-for-byte;
4. the independent room-setpoint path `B3C5` changes to the same value.

This is genuine Online/DCM semantic proof.

## Local XTR writer track

The later local XTR write track also records confirmed desired-state transactions:

```text
target 03F4 = 21
WRITE_CONFIRMED exact 03E8 republish
Room Setpoint Mirror = 21 °C

then

target 03F4 = 20
WRITE_CONFIRMED exact 03E8 republish
Room Setpoint Mirror = 20 °C
```

### Classification

**PROVEN / locally confirmed native semantic target:** `03F4 = room setpoint`.

This is currently the strongest semantically written local XTR setting.

---

# 4. Old `03F1 = HotWaterStart` hypothesis is retired for XTR

An early register map labelled:

```text
03F1 = likely Hot Water START
```

mainly from value similarity and firmware semantic ordering.

Later physical XTR tests changing DHW START and related hot-water settings did **not** produce the expected corresponding mutation in the recurrent `03E8..03F5` page.

Therefore:

```text
03F1 = HotWaterStart on XTR
```

is **DISPROVEN / SUPERSEDED** as a working mapping.

`03F1` itself remains a native field, but its exact XTR semantic label is OPEN.

This is an important example of why semantic-order matching alone is not enough.

---

# 5. `042E` is the clearest profile-drift discriminator

Earlier project notes inherited:

```text
042E = Integral A1
```

from the ATEC/DHP-AQ Online profile.

That is not universal.

The iTec Online profile instead states:

```text
042E = Hot Water Status
0 = OFF
1 = ON
```

This is especially important because genuine Eco5 + Online command event E4 does:

```text
042E: 1 -> 0
```

and the controller accepts and republishes the changed page.

### Value-domain test

ATEC Integral A1 profile domain:

```text
-250 .. -5
```

Observed genuine Eco5 values:

```text
1 -> 0
```

Those values do **not** fit Integral A1.

They fit the iTec Hot Water Status enum exactly.

### Revised classification

For the **genuine Eco5 Online command**:

```text
042E = Hot Water Status
```

is now **STRONGLY SUPPORTED** by:

- modern/iTec profile semantics;
- exact observed `1 -> 0` value domain;
- genuine desired-state command acceptance.

For the **local XTR M**:

```text
042E semantic = OPEN / not locally confirmed
```

until a local XTR UI/capture correlation is available.

### Correction

The PROTO-OFFLINE-10 wording that cited ATEC's `Integral A1` label for E4 should be read as historical cross-model context, **not** the current best semantic interpretation.

---

# 6. `042F` remains open

Genuine Eco5 command E3 changes:

```text
042F: 1 -> 0
```

through the same proven desired-state mechanism.

No sufficiently reliable public or local semantic label has been recovered for `042F`.

### Classification

```text
042F
structure: PROVEN desired-state target
meaning: OPEN
```

Do not assign a hot-water/boost/integral label by adjacency alone.

---

# 7. Cooling settings

Local XTR physical UI testing established:

```text
0442 = Activate Cooling
0 = OFF
1 = ON
```

The public ATEC DCM profile independently exposes the same:

```text
registerIndex 1090 / 0442
REG_ACTIVATE_COOLING
0 OFF
1 ON
```

### Classification

**PROVEN / locally confirmed on XTR:** `0442 = Activate Cooling`.

Associated recurrent page:

```text
0442/count13
```

Other cooling-page words may have strong candidates from earlier experiments, but they remain below the confidence threshold for inclusion as proven settings in this consolidated database.

---

# 8. Operation mode and Link Integration

## `0553` Operation Mode

Local XTR EXP218 physically changed:

```text
AUTO -> COMPRESSOR -> AUTO
```

and observed:

```text
0553: 1 -> 2 -> 1
```

Therefore locally:

```text
0553 = Operation Mode
1 = AUTO
2 = COMPRESSOR
```

is **PROVEN**.

ATEC and iTec public profiles additionally define:

```text
0 = OFF
1 = AUTO
2 = COMPRESSOR
3 = AUXILIARY
4 = HOT_WATER
```

For XTR only `1` and `2` have direct local causality evidence in the current archive.

So:

```text
0 / 3 / 4
```

remain **STRONGLY SUPPORTED cross-model enum values**, not locally proven XTR values.

## `0559` Link Integration

ATEC, iTec and older Diplomat Online profiles all expose a Link Integration semantic concept, commonly:

```text
0 = LIGHT
1 = SYSTEM
```

Local XTR and genuine reference pages have been observed at:

```text
0559 = 0
```

but no direct local XTR semantic change has been performed.

### Classification

```text
0559 = Link Integration
STRONGLY SUPPORTED / cross-profile Online evidence

local XTR current value 0:
OBSERVED

local XTR writable meaning:
NOT PROVEN
```

Also, scheduler-enabled genuine traffic has been observed while `0559=0`, so `0559=1` is **not** a prerequisite for the native Online scheduler.

---

# 9. Runtime/service database — major correction to `0870`

Previous offline work had correctly established:

```text
0870.word0 = (06E3 << 8) | 06E2
```

but left its human meaning open and tentatively treated it as a generic context word.

Public ATEC and iTec Online profiles independently identify:

```text
0870 = REG_OPER_TIME_COMPRESSOR
```

This substantially changes the interpretation.

### Current classification

```text
0870 = Compressor Operating Time
STRONGLY SUPPORTED cross-profile semantic
```

The existing raw bridge:

```text
0870 = (06E3 << 8) | 06E2
```

is still valid.

It now means that `06E2/06E3` feed the packed compressor-runtime value, rather than an unnamed generic context value.

Do not discard the historical raw observation; update its semantic interpretation.

---

# 10. Operating-time registers are not a contiguous `0872..0878` seven-word block

An earlier structural hypothesis tried to map the manual's seven BEDRIJFS TIJD entries onto the contiguous range `0872..0878`.

Public Online profiles show a better mapping.

Both ATEC and iTec agree on:

```text
0870  Compressor operating time
0872  Heating operating time
0873  Cooling operating time
0876  Hot-water operating time
0877  Immersion / auxiliary heater stage 1
0878  Immersion / auxiliary heater stage 2
```

ATEC additionally exposes:

```text
0879  Immersion / auxiliary heater stage 3
```

The XTR commissioning manual independently lists:

```text
COMPRESSOR
VERWARMING
KOELING
WARMWATER
BIJVERW_1
BIJVERW_2
BIJVERW_3
```

### Revised interpretation

The seven logical operating-time counters are **not required to occupy seven consecutive addresses**.

Best current map:

```text
0870  COMPRESSOR
0872  VERWARMING
0873  KOELING
0876  WARMWATER
0877  BIJVERW_1
0878  BIJVERW_2
0879  BIJVERW_3
```

### Evidence classification

- address/semantic agreement across public ATEC+iTec:
  **STRONGLY SUPPORTED**
- `0879` stage 3:
  **STRONGLY SUPPORTED for ATEC and semantically aligned with XTR manual; local XTR not confirmed**
- exact units/scaling on raw bus:
  **not fully reduced for every counter**

### Superseded hypothesis

```text
0872..0878 = seven consecutive operating-time counters
```

is **DISPROVEN / SUPERSEDED**.

The nonzero `0874/0875` raw fields remain semantically OPEN.

---

# 11. Defrost counters are now much stronger

Both public ATEC and iTec profiles independently assign:

```text
087B = REG_DEFROSTS_MA_SA
087C = REG_DEFROSTS_BETW2DEFR_MA_SA
087D = REG_DEFROST_TIME_LAST_DEFROST_MA_SA
```

This aligns directly with the official XTR commissioning menu:

```text
ONTD_PERIODES
TUSSEN. 2 ONTD.
LAATSTE ONTD.P.
```

Therefore the previous broad `087B..087D` hypothesis can be upgraded substantially.

Best current semantic map:

```text
087B = completed defrost periods / defrost count
087C = compressor/runtime interval between the last two defrosts
087D = compressor/runtime since the last defrost
```

### Classification

**STRONGLY SUPPORTED / cross-profile Online + official XTR semantic alignment.**

Not yet labelled **PROVEN locally** because the project has not captured a local XTR display-value cross-check against these exact addresses at the same moment.

This also corrects the earlier uncertainty around `087D`: it should no longer be described merely as a generic cumulative compressor-runtime-like counter.

---

# 12. Public iTec profile is a better semantic donor for modern Eco5/XTR than ATEC when the profiles disagree

The public ATEC profile is valuable because it is DHP-AQ lineage and contains many labels.

But when ATEC and iTec disagree at the same numeric address, modern iTec evidence must take priority for modern iTec-like behavior.

The `042E` command is the strongest example:

```text
ATEC:
042E = Integral A1

iTec:
042E = Hot Water Status

genuine modern Eco5 command:
042E 1 -> 0
```

The observed values select the iTec interpretation.

### Working rule

For XTR hypothesis generation:

```text
local XTR causality
  >
genuine modern Eco5 native behavior
  >
public iTec Online profile
  >
public ATEC/DHP-AQ Online profile
  >
older Diplomat/NCP profile
```

This hierarchy is only for **semantic donor selection within the external register maps**.

It does not replace the project's general source-of-truth hierarchy.

---

# 13. Current settings/write candidate tiers

This consolidation does **not** automatically authorize writes.

## Tier A — locally proven semantics / strongest candidates

```text
03E8  Heat Curve
03EB  Curve +5
03F4  Room Setpoint
0442  Activate Cooling
0553  Operation Mode (local values 1=AUTO, 2=COMPRESSOR)
```

Of these, only `03F4` is already proven through the reconstructed native Online desired-state path on the local XTR writer track.

For the other settings, a semantic address being locally proven does **not** mean the correct desired-state page/bit/write transaction has been proven locally.

## Tier B — strongly supported XTR semantics

```text
03E9  Heating Minimum
03EA  Heating Maximum
03EC  Curve 0
03ED  Curve -5
03EE  Heating Stop
03F0  Room Factor
0559  Link Integration
```

These need dedicated local causality before promotion.

## Tier C — genuine modern desired targets, local XTR semantics not confirmed

```text
042E  strongly supported modern Hot Water Status
042F  semantic OPEN
```

## Explicitly excluded from active write planning

```text
03F1
```

because the old `HotWaterStart` interpretation was not supported by later XTR correlation.

---

# 14. Desired-state page architecture in database form

Current proven/observed page relationships:

```text
03E8 page
  W1 desired bit0
  genuine Online desired FC03 proven
  local XTR 03F4 desired write proven
  contains heating/setpoint family

042E page
  W1 desired bit3
  genuine Eco5 desired FC03 proven
  command targets 042E and 042F
  local XTR page semantics not yet causally mapped

0442 page
  controller FC16 export page
  0442 Activate Cooling locally proven
  desired scheduler bit for this page has not been observed in the genuine corpus

0546 page
  controller FC16 export page
  0553 Operation Mode locally proven
  0559 Link Integration strongly supported
  desired scheduler bit for this page has not been observed in the genuine corpus
```

This distinction is critical:

> **knowing a setting's register address is not the same as knowing its native desired-state command path.**

---

# 15. Database invariants

The consolidated database now records four separate questions per register:

```text
1. Does this numeric address exist locally?
2. Is its semantic label locally proven?
3. Is it writable in some Online profile?
4. Is the native desired-state mechanism for this page proven?
```

Example:

```text
0553:
exists locally                         YES
Operation Mode locally proven          YES
public Online profile says writable    YES
native desired W0/W1 bit observed      NO
safe local semantic write path proven  NO
```

Versus:

```text
03F4:
exists locally                         YES
Room Setpoint semantic proven          YES
genuine desired page path observed     YES
local native semantic write confirmed  YES
```

This prevents a major class of unsafe inference.

---

# 16. Observed facts

- local XTR `0553` changes reversibly `1 -> 2 -> 1` with physical AUTO → COMPRESSOR → AUTO.
- local XTR `0442` changes with physical Activate Cooling and is 0/1.
- local XTR heating page contains `03E8` and locally proven curve-related fields.
- local XTR desired-state writer has confirmed `03F4` setpoint writes with exact controller `03E8` republish.
- genuine Eco5 Online desired commands mutate `03F4`, `042E`, and `042F`.
- public ATEC and iTec Online profiles agree on the core `03E8..03F0` heating semantics.
- public ATEC and iTec profiles disagree on `042E`.
- public older profiles place common semantics at other numeric indices.
- public ATEC+iTec profiles independently agree on `0870`, `0872`, `0873`, `0876`, `0877`, `0878`, `087B`, `087C`, `087D`.
- ATEC additionally exposes `0879` as immersion-heater stage-3 operating time.
- XTR manual's operation-time and defrost menu labels align with those public profile semantics.

---

# 17. Strong conclusions

1. **Thermia Online registerIndex is profile/model scoped, not universal.**
2. The core heating family `03E8..03F0` is unusually stable across ATEC and iTec and is therefore a strong XTR donor family.
3. `042E` must not be universally called Integral A1.
4. For the genuine modern Eco5 `042E:1->0` command, Hot Water Status is now the strongest semantic interpretation.
5. `0870` is strongly identified as compressor operating time.
6. The seven XTR operating-time counters use a sparse address layout; the previous contiguous `0872..0878` hypothesis is superseded.
7. `087B..087D` now have strong defrost-counter semantics aligned across two public profiles and the XTR manual.
8. A semantic address map and a native write-path map must remain separate databases/layers.

---

# 18. Hypotheses

- the local XTR follows the public iTec `042E = Hot Water Status` mapping.
- the local XTR uses `0879` for BIJVERW_3.
- `0559` retains the LIGHT/SYSTEM semantics on XTR, though its local effect has not been causally exercised.
- the unobserved desired bitmap half W0 ultimately provides desired-state pulls for settings pages in the high half such as `0546`, but no genuine W0 event has yet been captured.

---

# 19. Unknowns

- local XTR semantic meaning of `042E` and `042F`.
- exact XTR semantics of `03F1`, `03F2`, `03F3`, `03F5`.
- exact semantics of `0874` and `0875`.
- exact raw-bus scaling for every operating-time/defrost field.
- desired scheduler bit for `0442` cooling page.
- desired scheduler bit for `0546` Operation Mode page.
- whether `0559` is accepted as a remotely desired setting on XTR.
- which additional settings pages are remotely writable versus export-only.
- full XTR-specific profile table / Connect protocol package.

---

# Result

**PROTO-OFFLINE-16 — COMPLETE / POSITIVE — offline scope**

The native settings database is now substantially safer and more useful because it is no longer treated as a universal cross-model register table.

The project should use:

```text
XTR-local semantic truth
        +
genuine Online desired-state behavior
        +
profile-aware external register metadata
```

and never:

```text
one public DHP-AQ register dump
        =
universal XTR register map
```

The most important concrete corrections are:

```text
042E:
  not universally Integral A1;
  modern iTec/Eco5 evidence strongly favors Hot Water Status.

0870:
  compressor operating time.

operating-time group:
  sparse addresses, not 0872..0878 contiguous.

087B / 087C / 087D:
  defrost count / between-two-defrosts / since-last-defrost
  strongly supported.
```

No new live bus action, YAML change, restart or setting mutation was performed.