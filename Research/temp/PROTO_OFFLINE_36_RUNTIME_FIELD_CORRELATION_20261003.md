# PROTO-OFFLINE-36 — unresolved runtime-field correlation sweep

**Date:** 2026-10-03  
**Status:** **COMPLETE / POSITIVE**  
**Hypothesis:** change-point and source-state correlation across the genuine Eco5 runtime ring can still reduce unresolved dynamic words without guessing register meanings.  
**Controlled change:** offline analysis only. No bus TX, YAML change, reboot or setting write.

## Method

For every dynamic word in the genuine Eco5 `07D0..0870` runtime family:

1. align each controller `0x0F FC16` page with the most recent valid `0x1E FC04 0000/count22` outdoor-unit image;
2. rank exact equality/derived-state relationships before loose numerical correlations;
3. compare against known anchors such as compressor frequency, outdoor operating state/status flags, compressor-running and pre-run state;
4. refuse semantic promotion where the corpus lacks an independently labelled heating/cooling/DHW/defrost/SG transition.

## 1. `07F4` operating-state summary is now exactly reduced

Across **96/96** source-qualified Eco5 samples:

```
if 1E:0015 != 0x0221:
    07F4 = 0

if 1E:0015 == 0x0221 and compressor_frequency == 0:
    07F4 = 4

if 1E:0015 == 0x0221 and compressor_frequency > 0:
    07F4 = 6
```

Observed counts:

- `07F4=0`: 79
- `07F4=4`: 1
- `07F4=6`: 16

### Conclusion

`07F4` is **PROVEN / structural in genuine Eco5** as a normalized outdoor-unit operating-state summary:

- 0 = inactive/not in the `0x0221` active-status family;
- 4 = active/start phase with zero compressor frequency;
- 6 = active/running phase with non-zero compressor frequency.

These numeric labels are protocol-state codes, not claimed Thermia UI enum names.

## 2. `0845` is an exact coded active-status export

Across **43/43** source-qualified `0834/count18` samples:

```
0845 = 0x0300  iff  1E:0015 == 0x0221
0845 = 0x0000  otherwise
```

This means `0845` does not distinguish pre-run from running. It marks the broader outdoor-unit active/status family that `07F4` then subdivides using compressor frequency.

### Strong conclusion

`0845` is **PROVEN structural / genuine Eco5** as a coded active-state export derived from the modern outdoor-unit status field.

Human-readable firmware name remains OPEN.

## 3. Existing transition reductions survive the automatic sweep

The sweep independently leaves the earlier high-confidence relations intact:

- `0865 = compressor running` from compressor frequency;
- `0866` = commanded/start-pending candidate;
- `083B` = mod-60 active controller-cycle accumulator;
- `083C` = coded inverse pre-run transition;
- `0867` = topology/platform fingerprint.

No contradictory source-state relationship was found.

## 4. Negative results are important

The corpus does **not** contain enough independently labelled transitions to assign new fields to:

- heating active;
- cooling active;
- DHW active;
- defrost active;
- SG mode.

For SG, the already-local `04A6/04A7` correlation remains stronger than any new runtime-ring correlation.

For defrost, `087C/087D` service counters are now scaled, but no actual defrost onset/clear event exists in these captures.

### Conclusion

Do not manufacture heating/cooling/DHW/defrost state labels from correlation with outdoor activity alone.

## 5. Ranked result

Highest-value new reductions:

1. **07F4** — exact three-state normalized outdoor operating summary.
2. **0845** — exact coded active-status export.
3. no additional field reaches semantic-proof threshold beyond already-known `0865/0866/083B/083C`.

This is a useful stopping point: remaining runtime unknowns need either labelled physical-mode transitions or firmware/serializer evidence.

## Live status

Unchanged:
- EXP387 COMPLETE / POSITIVE
- EXP388 RUNNING / PARTIAL
