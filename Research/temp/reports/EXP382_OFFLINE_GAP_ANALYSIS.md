# EXP382 — Offline gap analysis of controlled native pages

**Status:** COMPLETE / POSITIVE (offline analysis only)  
**Baseline:** EXP381B — COMPLETE / POSITIVE  
**Bus TX:** none  
**Warmtepompwijzigingen:** none  

## Hypothesis

Existing project evidence — local XTR M results, genuine Online/DCM captures, collaborator Eco/DHP-AQ captures, the Thermia iTec XT/XTR commissioning manual and the public Thermia Online/DCM register dump — can reduce the remaining unknown words inside the already controlled native pages without any new live write experiment.

## Controlled change from EXP381B

None on-device. EXP382 is analysis-only. No YAML, selector, frame, CRC, register value, timeout or state-machine behavior is changed.

## Evidence discipline

- **PROVEN / locally confirmed:** direct XTR M correlation or successful local semantic write.
- **STRONGLY SUPPORTED:** multiple independent sources align, but no direct local XTR correlation yet.
- **HYPOTHESIS:** plausible mapping from order/value/context only.
- **OPEN / UNKNOWN:** insufficient evidence.
- Cross-model values are never promoted to local XTR proof.

---

# 1. Page 0x03E8 / count14 — Heating

| Word | Register | Current project meaning | EXP382 result |
|---:|---:|---|---|
| 0 | 03E8 | Heating Curve | **PROVEN** |
| 1 | 03E9 | Heating Minimum | **PROVEN** |
| 2 | 03EA | Heating Maximum | **PROVEN** |
| 3 | 03EB | Curve Correction +5 | **PROVEN** |
| 4 | 03EC | Curve Correction 0 | **PROVEN** |
| 5 | 03ED | Curve Correction -5 | **PROVEN** |
| 6 | 03EE | Heating Stop | **PROVEN** |
| 7 | 03EF | Reduced Temperature | **PROVEN** |
| 8 | 03F0 | Room Factor | **PROVEN** |
| 9 | 03F1 | unknown | **OPEN**; specifically **DISPROVEN** as live DHW START |
| 10 | 03F2 | unknown | **OPEN** |
| 11 | 03F3 | unknown | **OPEN** |
| 12 | 03F4 | Room Setpoint | **PROVEN** |
| 13 | 03F5 | unknown | **OPEN** |

### Offline observations

A genuine Online-family capture using a 13-word `03E8..03F4` page shows the unknown triplet `03F1..03F3 = 40,30,60`. The Eco/DHP-AQ collaborator capture shows `40,30,1`. The stable `40,30` pair is interesting, but the third word diverges strongly between systems.

The old cross-model control-register documentation contains a secondary-heating-curve family after Room Factor (`Curve 2`, `Curve 2 min`, `Curve 2 max`). That is structurally suggestive, but it is **not enough** to rename `03F1..03F3` on the XTR M. The XTR commissioning manual also contains model/configuration-dependent heating items after Room Factor, so several interpretations remain possible.

**Decision:** no promotion. Keep `03F1/03F2/03F3/03F5` unknown for v1.0.

---

# 2. Page 0x042E / count15 — Hot water / service

| Word | Register | Current meaning | EXP382 result |
|---:|---:|---|---|
| 0 | 042E | Hot Water Enabled | **PROVEN** |
| 1 | 042F | Hot Water Mode | **PROVEN** |
| 2 | 0430 | unknown / Top-up candidate | **STRONGLY SUPPORTED candidate: TOP_UP**, not locally proven |
| 3 | 0431 | unknown | **OPEN** |
| 4 | 0432 | unknown | **OPEN** |
| 5 | 0433 | Startup HT | **PROVEN** |
| 6 | 0434 | Heating Time | **PROVEN** |
| 7 | 0435 | unknown | **OPEN** |
| 8 | 0436 | unknown | **OPEN** |
| 9 | 0437 | unknown | **OPEN** |
| 10 | 0438 | unknown | **OPEN** |
| 11 | 0439 | unknown | **OPEN** |
| 12 | 043A | unknown | **OPEN** |
| 13 | 043B | unknown | **OPEN** |
| 14 | 043C | unknown | **OPEN** |

### 0430 — Top-up

This is the strongest remaining gap on this page.

The XTR INFORMATION menu orders the user-facing hot-water fields as:

`WARMWATER -> MODUS -> TOP_UP`

The native page already maps:

`042E = WARMWATER`  
`042F = MODUS`  
`0430 = next word`

That exact adjacency makes `0430 = TOP_UP` substantially stronger than a generic guess.

**Classification after EXP382:** **STRONGLY SUPPORTED**, but not locally confirmed. Do not expose as a writable production entity until a local correlation exists.

### 0431 / 0432

Earlier interpretation as Heating START/STOP remains rejected. Existing page values did not match that interpretation.

**Decision:** remain OPEN / UNKNOWN.

### 0435..043C

The service manual lists additional DHW parameters (START, STOP, DHW time, anti-legionella interval/time/stop, sensor influence, Eco-mode influence). However, those menu fields cannot be assigned safely to `0435..043C` from ordering alone because:
- some confirmed DHW values live on another native page (`041D`, `041E`);
- genuine/cross-model page contents differ materially;
- no controlled local XTR correlation exists for these words.

**Decision:** no speculative register labels.

---

# 3. Page 0x0442 / count13 — Cooling

| Word | Register | Current meaning | EXP382 result |
|---:|---:|---|---|
| 0 | 0442 | Cooling Enabled | **PROVEN** |
| 1 | 0443 | Desired Cooling Temperature | **PROVEN** |
| 2 | 0444 | unknown | **STRONGLY SUPPORTED: INFORMATION Cooling Hysteresis**, likely scaled |
| 3 | 0445 | Cooling Active Above | **PROVEN** |
| 4 | 0446 | unknown | **STRONGLY SUPPORTED: SERVICE Cooling configuration/type enum** |
| 5 | 0447 | unknown | **HYPOTHESIS: Cooling START regulator threshold**, encoding unresolved |
| 6 | 0448 | unknown | **STRONGLY SUPPORTED: Cooling STOP regulator threshold** |
| 7 | 0449 | Cooling Time | **PROVEN** |
| 8 | 044A | unknown | **STRONGLY SUPPORTED: MAX_STARTTEMP** |
| 9 | 044B | unknown | **STRONGLY SUPPORTED: MIN_STOPTEMP** |
| 10 | 044C | Cooling Room Sensor | **PROVEN** |
| 11 | 044D | Room Hysteresis Low | **PROVEN**, raw/10 |
| 12 | 044E | Room Hysteresis High | **PROVEN**, raw/10 |

### Why 0444 is now a strong candidate for normal Cooling Hysteresis

The INFORMATION menu has exactly one additional field between the already identified user cooling controls: `HYSTERESIS`, factory 2 K, range 0..12 K.

A genuine Online-family `0442/count13` image contains `0444=20`, which is a perfect fit for **2.0 K if encoded x10**. This is also consistent with the nearby locally proven room-hysteresis fields using x10 encoding.

The collaborator Eco page has `0444=0`, which remains valid for a system/config where that hysteresis is zero/not used.

**Classification:** STRONGLY SUPPORTED, not local XTR proof.

### Why 0446 is likely the SERVICE cooling type

The SERVICE menu has a cooling configuration with values:
- UIT
- ACTIEVE_KOELING
- GEÏNTEGR. IN WP

A genuine Online-family page has `0446=2`; the collaborator page has `0446=0`. This fits a compact `0/1/2` enum unusually well.

**Classification:** STRONGLY SUPPORTED.

### 0447 / 0448

The SERVICE menu next lists regulator START and STOP thresholds. Their position immediately after the probable cooling-type enum and immediately before other known service cooling settings makes `0447/0448` the natural pair.

`0448` values seen cross-model are compatible with a STOP-like non-negative field. `0447` is less clean across models, so its exact signed/scaled encoding is unresolved.

**Classification:** `0447` HYPOTHESIS; `0448` STRONGLY SUPPORTED.

### 044A / 044B

Immediately after locally proven `0449 = Cooling Time`, the SERVICE menu lists:
- MAX_STARTTEMP
- MIN_STOPTEMP
- KAMERSENSOR
- KLHYS.KAMSNS.LG
- KLHYS.KAMSNS.HG

The native sequence is:

`0449 -> 044A -> 044B -> 044C -> 044D -> 044E`

This is an exceptionally clean structural match. Genuine Online-family values `044A=18`, `044B=16`, followed by room sensor `1`, low `10`, high `10`, are also numerically plausible.

**Classification after EXP382:**
- `044A = MAX_STARTTEMP` — **STRONGLY SUPPORTED**
- `044B = MIN_STOPTEMP` — **STRONGLY SUPPORTED**

These still require local XTR correlation before production write exposure.

---

# 4. Page 0x0546 / count20 — System / Operation

| Word | Register | Meaning | EXP382 result |
|---:|---:|---|---|
| 0..12 | 0546..0552 | unknown | **OPEN** |
| 13 | 0553 | Operation Mode | **PROVEN / locally write-confirmed by EXP380** |
| 14..18 | 0554..0558 | unknown | **OPEN** |
| 19 | 0559 | Link Integration | **STRONGLY SUPPORTED from public Thermia Online/DCM dump** |

### 0559 — Link Integration

The public Thermia Online/DCM dump explicitly labels register index 1369 / `0x0559` as **Link Integration** with enum:
- `0 = LIGHT`
- `1 = SYSTEM`

The register lies exactly at word 19 of the already controlled `0546/count20` page. Existing genuine/collaborator images show `0559=0`, consistent with the dump.

This is stronger than a positional guess because the public dump gives the exact numeric `registerIndex`.

**Classification:** STRONGLY SUPPORTED / firmware-cloud-side mapping, **not yet local XTR semantic correlation**.

No other `0546..0558` word receives a new label in EXP382.

---

# 5. EXP382 outcome

## Observed facts

- The controlled page architecture remains internally consistent.
- Manual menu order explains several remaining cooling words extremely well.
- `0430` sits exactly where TOP_UP would be expected after Hot Water Enabled and Mode.
- `0449..044E` matches the SERVICE cooling tail almost one-for-one.
- The public Online dump independently identifies `0559` as Link Integration.
- Cross-model/genuine page images differ enough that raw position/value matching alone is unsafe.

## Strong conclusions

EXP382 materially reduces the gap list without changing any local-proven facts.

Best new candidates:

1. `0430` = Hot Water TOP_UP — **STRONGLY SUPPORTED**
2. `0444` = Information Cooling Hysteresis — **STRONGLY SUPPORTED**
3. `0446` = Service Cooling configuration/type — **STRONGLY SUPPORTED**
4. `0448` = Service Cooling STOP threshold — **STRONGLY SUPPORTED**
5. `044A` = Cooling MAX_STARTTEMP — **STRONGLY SUPPORTED**
6. `044B` = Cooling MIN_STOPTEMP — **STRONGLY SUPPORTED**
7. `0559` = Link Integration — **STRONGLY SUPPORTED**

## Hypotheses

- `0447` is probably the SERVICE Cooling START threshold, but encoding/value evidence is not clean enough for a stronger classification.
- `03F1..03F3` may belong to an additional/secondary heating-curve or model-dependent heating family, but the evidence is ambiguous.

## Unknowns retained

- `03F1`, `03F2`, `03F3`, `03F5`
- `0431`, `0432`, `0435..043C`
- `0546..0552`, `0554..0558`
- exact encoding of `0447`
- local XTR confirmation for every newly strong candidate above

---

# 6. Production consequence

For the upcoming v1.0 production refactor:

### Safe to include as proven controls
Keep the currently locally proven EXP381B entities.

### Safe to add as read-only labels?
Only if the underlying current-page values are already captured and we clearly mark them experimental/diagnostic. For the conservative v1.0 baseline, **do not promote the new EXP382 candidates to normal production controls yet**.

### Best later targeted confirmations
After v1.0, the smallest high-value local correlations would be:
- toggle TOP_UP and watch `0430`;
- change INFORMATION Cooling Hysteresis and watch `0444`;
- inspect SERVICE Cooling type / MAX_STARTTEMP / MIN_STOPTEMP against `0446/044A/044B`.

Those are future tests, not part of EXP382.

---

**Final EXP382 status: COMPLETE / POSITIVE.**  
The offline analysis successfully narrowed several unknowns to evidence-backed candidates while preserving the distinction between local proof and cross-model/manual inference.