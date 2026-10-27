# PROTO-OFFLINE-35 — runtime-counter scaling

**Date:** 2026-10-03  
**Status:** **COMPLETE / POSITIVE**  
**Hypothesis:** the sparse `0870` operational-time/defrost family can be assigned usable raw scaling from existing genuine captures, the XTR commissioning manual and public iTec profile metadata.  
**Controlled change:** offline evidence analysis only. No bus TX, YAML change, reboot or setting write.

## 1. Operating-time family `0870/0872/0873/0876..`

### Structural arithmetic

Legacy genuine Online/DCM values:

```
0870 compressor = 21966
0872 heating    =  9763
0873 cooling    =    10
0876 hot water  = 12091
sum modes       = 21864
gap             =   102
```

Genuine Eco5:

```
0870 compressor = 1131
0872 heating    =  501
0873 cooling    =  423
0876 hot water  =  201
sum modes       = 1125
gap             =    6
```

The mode counters therefore nearly partition total compressor operating time in both topology families.

Between the two Eco5 captures:

```
0870 compressor 1131 -> 1132
0876 hot water   201 -> 202
0872 heating     501 -> 501
0873 cooling     423 -> 423
```

This is exactly the pattern expected when roughly one additional whole hour of compressor operation belongs to hot-water production.

### External profile support

The public iTec Online profile exposes:
- `REG_OPER_TIME_COMPRESSOR`
- `REG_OPER_TIME_HEATING`
- `REG_OPER_TIME_COOLING`
- `REG_OPER_TIME_HOT_WATER`
- auxiliary-heater operational-time registers

as integer operational-time values with step 1.

### Scaling conclusion

For the `0870/0872/0873/0876/0877/0878` family:

> **raw integer value = operating hours** is **STRONGLY SUPPORTED**.

This is not promoted to locally causal XTR proof because the current local XTR project has not independently changed a runtime counter by a known one-hour interval under controlled conditions.

`0879` inherits the family scaling if its Aux/Immersion Heater 3 semantic is correct; that semantic remains slightly weaker.

## 2. Defrost family

The digitized XTR commissioning manual explicitly defines:

- `TUSSEN. 2 ONTD.` = **compressor runtime in minutes between last two defrosts**
- `LAATSTE ONTD.P.` = **compressor runtime in minutes since last defrost**

The public iTec profile maps these to:
- `2172 / 087C` — between last two defrosts, with step `0.0167`, compatible with 1 minute = 1/60 hour when displayed as hours;
- `2173 / 087D` — time since last defrost.

### Capture dynamics

In the 2026-09-26 Eco5 capture:

`087D: 30729 -> 30730 -> 30731 -> 30732 -> 30733 -> 30734`

The observed +1 edges after runtime publication resumes occur while the most recent compressor-running state is active and at roughly minute-scale intervals.

Between 2026-09-26 and 2026-09-28:

`087D: 30734 -> 30811`

That is compatible with additional **compressor-runtime minutes**, not wall-clock minutes.

### Scaling conclusion

- `087B` = raw completed-defrost **count**.
- `087C` = raw **compressor-runtime minutes** between last two defrosts — STRONGLY SUPPORTED.
- `087D` = raw **compressor-runtime minutes** since last defrost — STRONGLY SUPPORTED.

## 3. Remaining gaps

- `0874` remains OPEN.
- `0875` remains semantically OPEN despite the proven `0875==0873` relation.
- exact rollover width/persistence behavior has not been tested;
- `0879` semantic identity is not locally confirmed even though the operational-time family scaling is clear.

## Strong conclusions

1. The main operational-time counters can now be interpreted in **hours** instead of opaque raw units.
2. The defrost interval/since-last counters are **compressor-runtime minutes**, not generic wall-clock time.
3. This makes the current `0870` family useful for Home Assistant read-only entities without introducing any write path.

## Live status

Unchanged:
- EXP387 COMPLETE / POSITIVE
- EXP388 RUNNING / PARTIAL
