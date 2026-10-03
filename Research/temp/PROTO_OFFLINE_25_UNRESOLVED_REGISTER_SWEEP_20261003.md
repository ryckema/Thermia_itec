# PROTO-OFFLINE-25 — unresolved-register sweep

**Date:** 2026-10-03  
**Status:** **COMPLETE / POSITIVE** — several unknowns are narrowed structurally, but no unsafe semantic promotion is made.  
**Hypothesis:** the remaining unresolved settings/runtime fields can be narrowed by cross-topology value-domain comparison, page-shape drift and exact runtime relations without another broad register scan.  
**Controlled change:** offline analysis only; no device TX, YAML change, reboot or setting write.

## Settings-page results

### 03F1 / 03F2

Where present in both legacy and Eco5 reference pages:

- `03F1 = 40`
- `03F2 = 30`

They are stable across the compared topology families and behave like persistent configuration/context values.

However:
- EXP135 already disproves `03F1 = Hot Water Start` on the local XTR;
- no controlled semantic edge exists for either field.

**Classification:** OPEN / UNKNOWN. Cross-topology stability is structural evidence only.

### 03F3

- legacy genuine reference: `60`
- Eco5: `1`

This is a strong profile/generation discriminator.

**Conclusion:** do not attach a universal Thermia semantic label to `03F3`.

### 03F5

The legacy desired/config page is `03E8/count13` and does not contain `03F5`.
Modern Eco5 uses `03E8/count14` and carries:

`03F5 = 2`

**Conclusion:** `03F5` is a concrete modern page-extension field; exact semantics remain OPEN.

### 0431 / 0432

Observed:

- legacy: `0431=12`, `0432=60`
- Eco5: `0431=20`, `0432=-10` (signed `FFF6`)

This strengthens the existing EXP376 correction: the earlier generic Heating START/STOP interpretation is not portable and should remain rejected.

### 0447

Observed:

- legacy reference: `35`
- Eco5: `-8` (signed `FFF8`)

The value-domain difference is too large to strengthen the current Cooling START hypothesis cross-model.

**Classification remains HYPOTHESIS.** Exact semantic and signed/scaled encoding remain OPEN.

## Runtime results

### 0875 has an exact relation to 0873

Across every `0870/count17` page in the six reference captures:

`0875 == 0873`

holds in **83/83 frames**.

Examples:
- legacy: `0873=10, 0875=10`
- Eco5: `0873=423, 0875=423`

Since `0873` is strongly supported as Cooling Operating Time from public iTec/ATEC profiles, `0875` may be a duplicate/alias/context copy of that counter. The capture relation itself is proven; the semantic reason is not.

**Classification:**
- equality relation: **PROVEN structural**
- `0875 = Cooling Operating Time`: **HYPOTHESIS only**
- keep `0875` OPEN in the semantic map, with the equality noted.

### 0874

Observed:
- legacy: `10`
- Eco5: `437`

No stable relation to a proven counter survives both topology families.

**Classification:** OPEN / UNKNOWN.

### 087D dynamic behavior

In the 2026-09-26 Eco5 capture `087D` changes:

`30729 -> 30730 -> 30731 -> 30732 -> 30733 -> 30734`

Every observed +1 edge after the long idle interval occurs while the most recent `0865` compressor-running Boolean is `1`.

Observed publication intervals for those edges are roughly minute-scale.

This materially strengthens `087D` as a **running-time accumulator associated with compressor/defrost runtime**, consistent with the external iTec defrost register identity.

The public iTec profile also exposes registerIndex 2172 with step `0.0167`, numerically close to 1/60, which is compatible with minute-resolution timing for the defrost interval family. Modifier/scaling rules are not sufficiently decoded to turn that into a universal raw conversion.

**Safe classification:** time-accumulator behavior strongly supported; exact raw unit/scaling remains OPEN.

## Negative results

The sweep does **not** recover safe names for:
- `03F1/03F2/03F3/03F5`
- `0431/0432`
- `0447`
- `0874/0875`

except for the proven `0875==0873` relation.

## Strong conclusions

1. Several unresolved settings fields are demonstrably profile/generation dependent.
2. `03F5` is part of the modern 14-word heating page extension and absent from the legacy 13-word page.
3. `0875==0873` is a real cross-topology invariant in the current reference corpus.
4. `087D` behaves as a running-time accumulator during compressor-running state, but exact unit/scaling should not yet be hard-coded.

## Live status

No change:
- EXP387 COMPLETE / POSITIVE
- EXP388 RUNNING / PARTIAL
