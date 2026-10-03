> **Current-status note — PARTIALLY SUPERSEDED (2026-10-03).** The cross-topology geometry and source-normalisation findings remain useful. The old group-level `0872..0878` operating-time interpretation is superseded by the profile-backed sparse mapping consolidated in PROTO-OFFLINE-16 and audited in PROTO-OFFLINE-20. Do not infer consecutive counter semantics from geometry alone.

# Thermia iTec XTR M — Cross-topology runtime normalisation

**Date:** 2026-10-03  
**Track:** PROTO-OFFLINE-13  
**Status:** COMPLETE / POSITIVE — offline analysis only  
**Original plan item:** #4 — cross-topology normalisation  
**Baseline:** PROTO-OFFLINE-05 runtime export family + PROTO-OFFLINE-06 automated source correlation + PROTO-OFFLINE-08 unresolved runtime reduction  
**Controlled change:** no new device traffic. Compare the same `0x0F` logical runtime pages across two genuine Online/DCM topology families and reduce which fields are topology-independent logical semantics versus topology-specific backend details.  
**Device TX:** none  
**YAML change:** none  
**Heat-pump restart:** none  
**Setting write:** none  
**GitHub change:** none  
**Live experiment status:** unchanged — EXP388 remains RUNNING / PARTIAL

## Topologies compared

### Legacy genuine Online/DCM reference

Observed backend domains:

```text
0x02 controller
0x04 legacy gateway/outdoor path
A5 legacy outdoor/service endpoint
0x06 accessory path
0x0F Online/DCM-facing export
```

Corpus:

- `thermia_capture_20260924_210001(1).log`
- `thermia_capture_20260925_071517.log`
- `thermia_capture_20260925_090209.log`
- `thermia_capture_20260925_090550.log`

### Modern genuine Eco5 + Online

Observed backend domains:

```text
0x02 controller
0x1E outdoor unit
0x06 accessory path
0x0F Online/DCM-facing export
```

Corpus:

- `itec_eco5_gateway_20260926.log`
- `itec_eco5_gateway_20260928.log`

The current XTR M local bus also uses the modern `0x1E` outdoor-unit topology, but the conclusions below remain cross-model evidence unless separately locally confirmed.

---

# Hypothesis

Thermia Online/DCM does not expose the physical bus topology directly.

Instead, the `0x0F` runtime family acts as a logical serialization layer:

```text
legacy physical sources ─┐
                         ├─> logical Online/DCM runtime schema
modern physical sources ─┘
```

If true, some `0x0F` fields should preserve logical meaning while changing physical source, while other fields should expose generation-specific capabilities or metadata.

**Result: strongly supported.**

---

# 1. Page-shape stability

The principal runtime pages retain the same start/count shape in both compared topology families:

```text
07D0 / 19
07E4 / 17
07F8 / 17
080C / 18
0820 / 18
0834 / 18
0848 / 23
085F / 5
0864 / 4
0870 / 17
```

Raw frame counts in this six-capture corpus:

| Page | Legacy frames | Eco5 frames |
|---|---:|---:|
| `07D0/19` | 8 | 101 |
| `07E4/17` | 8 | 96 |
| `07F8/17` | 7 | 70 |
| `080C/18` | 6 | 65 |
| `0820/18` | 6 | 47 |
| `0834/18` | 7 | 44 |
| `0848/23` | 7 | 47 |
| `085F/5` | 10 | 319 |
| `0864/4` | 7 | 48 |
| `0870/17` | 39 | 44 |

`0884/count60` exists in both families too, but only one Eco5 payload instance is available, so this pass does not assign cross-topology semantics to that page.

**Strong conclusion:** stable page addresses/counts survive a major physical-topology change.

---

# 2. Normalisation class A — stable controller-backed logical fields

Several fields keep both their logical role and source family across topologies.

Durable examples:

```text
07D0 <- A7F8             Supply Temperature
07D3 <- A7FB             DHW upper temperature
07D4 <- A7FC             DHW main temperature
07DA <- A802             instantaneous Outdoor Temperature
07DD <- A80C
07DE <- A80D
07DF <- A80E
07E0 <- A80F
07E1 <- A810
07E2 <- normalized A811

081A <- AFDC
```

These fields do not care whether the outdoor backend is legacy `0x04/A5` or modern `0x1E`.

This establishes the first normalisation class:

> **controller/accessory state can pass through the Online serializer unchanged while the outdoor-unit implementation changes underneath it.**

---

# 3. Normalisation class B — same logical field, different physical source

Two fields are now exceptionally clear examples of topology substitution.

## `07D1` — Return Line Temperature

Legacy:

```text
07D1 = A7F9
```

in 8/8 source-qualified legacy samples.

Modern Eco5:

```text
07D1 = signed(1E:0000) / 10
```

in 101/101 source-qualified samples.

The modern source is independently decoded as condenser inlet, ×0.1 °C.

Therefore the Online-facing logical field survives while the physical backend and scale change.

## `07E4` — Average Outdoor Temperature

Legacy:

```text
07E4 = 0x04:ABE0
```

in 8/8 source-qualified samples.

Modern Eco5:

```text
07E4 = signed(1E:0005) / 10
```

in 96/96 source-qualified samples.

`1E:0005` is independently decoded as Average Outdoor Temperature ×0.1 °C.

The same page separately carries:

```text
07E7 = A802 = instantaneous Outdoor Temperature
```

So the logical distinction between **average** and **instantaneous** outdoor temperature survives the topology change.

**PROVEN / structural cross-topology normalisation.**

---

# 4. New finding — the Eco5 `07E4` signature is directly sourced from the `0x1E` identity/capability block

PROTO-OFFLINE-05 had identified this stable Eco5 signature:

```text
0906 0709 0967 0579
```

inside `07E4/count17`, but its source was open.

This pass reconstructs contemporaneous `0x1E FC04 0016/count8` state and finds exact source identity:

```text
07E8 = 1E:001C = 0906
07E9 = 1E:001D = 0709
07EA = 1E:0016 = 0967
07EB = 1E:0017 = 0579
```

Each relation is exact in **83/83 source-qualified `07E4` frames**.

The source request is:

```text
1E 04 0016 0008
```

so registers `0016..001D` form one eight-word modern outdoor-unit metadata block.

The serializer deliberately selects four words from that block and reorders them:

```text
001C, 001D, 0016, 0017
```

into:

```text
07E8..07EB
```

### Important semantic classification

This proves source identity, **not** the human-readable meaning of the four values.

Safest label:

```text
modern outdoor-unit identity/capability metadata
```

Do not name the values as ProductID, firmware version, model number, etc. without further evidence.

---

# 5. `0820/count18` is the clearest topology abstraction boundary

## Modern `0x1E` backend

The already-established Eco5 mapping is:

```text
0820 <- 1E:0000   condenser inlet
0821 <- 1E:0001   condenser outlet
0822 <- 1E:0002   refrigerant temp 1
0823 <- 1E:0003   discharge gas
0824 <- 1E:0004   refrigerant temp 2
0825 <- 1E:0005   average outdoor temperature
0826 <- 1E:0006   compressor temperature
0827 <- 1E:000A   requested/target temperature
0828 <- 1E:000B   compressor frequency
0829 <- reserved zero
082A <- 1E:000D   compressor current
082B <- 1E:000E   outdoor fan rpm
082C <- reserved zero
082D <- 1E:0010   expansion valve
082E <- 1E:0014   outdoor operating state
082F <- 1E:0015   outdoor status flags
0830 <- 1E:0016
0831 <- 1E:0017
```

The live telemetry portion was already exact in 47/47 paired Eco5 observations.

This pass adds exact source confirmation for the tail:

```text
0830 = 1E:0016 = 0967
0831 = 1E:0017 = 0579
```

in **33/33 source-qualified `0820` frames**.

The same pair therefore appears in both:

```text
07EA/07EB
0830/0831
```

This duplication strongly supports the interpretation that `0967/0579` are modern topology/capability metadata rather than ordinary sensor values.

## Legacy A5 backend

Reconstructing the latest A5 FC03 state before every legacy `0820` frame gives:

```text
0820 <- A5:0000             6/6 exact
0821 <- A5:0001             6/6 exact
0822 <- byte-swap(A5:0002)  6/6 exact
0825 <- A5:0005             6/6 exact
0826 <- A5:0006             6/6 exact
0827 <- A5:0007             6/6 exact

082C <- A5:0032             6/6 exact
082D <- A5:0033             6/6 exact
082E <- A5:0034             6/6 exact
082F <- A5:0035             6/6 exact
0830 <- A5:0036             6/6 exact
0831 <- A5:0037             6/6 exact
```

Legacy slots `0823/0824/0828/082A/082B` are zero in the available frames while modern `0x1E` populates several of them.

### Cross-topology interpretation

The front of `0820` is strongly homologous:

```text
logical slot 0820:
legacy A5:0000 -> modern 1E:0000

logical slot 0821:
legacy A5:0001 -> modern 1E:0001

logical slot 0825:
legacy A5:0005 -> modern 1E:0005

logical slot 0826:
legacy A5:0006 -> modern 1E:0006
```

At `0827`, the physical address changes more substantially:

```text
legacy A5:0007
modern 1E:000A
```

while the Online-facing slot remains fixed.

That is exactly what a normalising serializer would do.

The back half should be treated more cautiously: the same **positions** are used, but generation-specific values/scales/features differ enough that positional equality alone cannot prove identical semantics for every field.

---

# 6. `07F8` is a legacy-compatibility / optional-extension page

Observed:

```text
Eco5:
07F8/count17 = all zero
70/70 frames

Legacy:
almost all zero
0807 carries instantaneous outdoor temperature
```

The page address/count survives both topologies, but useful content can disappear completely.

This is characteristic of a stable interface that preserves reserved/legacy slots for compatibility.

**STRONGLY SUPPORTED:** do not interpret zero-filled modern pages as absence of the runtime family itself.

---

# 7. `080C` contains both portable state and topology-specific capability data

Two especially clean fields:

```text
080C = 00C8
```

in all compared frames.

```text
081A = AFDC
```

in all 71 previously source-qualified observations.

A new cross-topology discriminator is also apparent:

```text
0819:
legacy = 0000  in all 6 frames
Eco5   = 0014  in all 65 frames
```

The semantic meaning of `0819=20` is OPEN.

The field should currently be classified as:

```text
topology/profile constant or capability field
```

not runtime telemetry.

---

# 8. `0834/count18` is not byte-portable across generations

Legacy payload is extremely sparse.

Six of seven legacy samples have:

```text
0834 = 001E
0840 = 0046
all other words = 0
```

and one sample has:

```text
0834 = 001E
all other words = 0
```

Modern Eco5 instead contains the already-reduced dynamic structure:

```text
0834 = 0000 or 0100
083B = controller-cycle runtime remainder
083C = 0000/0080 pre-run state code
0841 = 015E
0842 = 015E
0845 = 0000/0300 command-state export
```

There is no defensible one-to-one field correspondence between these page bodies.

### Strong conclusion

`0834/count18` is a **stable logical page envelope with generation-specific implementation content**.

It must not be copied byte-for-byte from an Eco5 reference to another topology.

For the XTR project, modern Eco5 `0834` is useful because the local XTR also has a `0x1E` topology, but its exact constants still require local confirmation.

---

# 9. `0848/count23` contains a genuinely portable clock/date ABI

The final seven words:

```text
0858 second
0859 minute
085A hour
085B day
085C month
085D year (two digits)
085E weekday
```

were checked against the calendar date in every available runtime frame:

```text
legacy: 7/7 valid
Eco5:  47/47 valid
total: 54/54
```

The weekday field also exactly matches the conventional:

```text
Monday = 0
Tuesday = 1
...
Sunday = 6
```

in **54/54** frames.

Examples:

```text
24-09-2026 Thursday -> 085E = 3
25-09-2026 Friday   -> 085E = 4
26-09-2026 Saturday -> 085E = 5
28-09-2026 Monday   -> 085E = 0
```

### Classification

**PROVEN / cross-topology logical ABI:**

`0858..085E` is a stable Online/DCM clock/date tuple with Monday-zero weekday enumeration.

The earlier `0848` words vary substantially between topology families and remain mostly OPEN.

---

# 10. `0864/count4` cleanly separates dynamic runtime bits from a topology fingerprint

Observed:

```text
legacy:
0000 0000 0000 0016

Eco5 normally:
0000 0000 0000 00E8

Eco5 transitions:
0000 0001 0000 00E8
0000 0000 0001 00E8
```

Modern reduction already supports:

```text
0865 = compressor running
0866 = commanded/start-pending state
```

The legacy samples do not provide enough dynamic coverage to determine whether the same booleans are implemented there or simply remained false.

But the final word is decisive:

```text
0867 legacy = 0016
0867 Eco5   = 00E8
```

for every captured sample in each family.

### Classification

- `0865/0866`: modern dynamic runtime semantics; cross-topology portability **not proven**.
- `0867`: **STRONGLY SUPPORTED topology/platform fingerprint**, semantic identity OPEN.

---

# 11. `0870/count17` preserves service-counter geometry across topologies

All 83 `0870` frames — 39 legacy and 44 Eco5 — share exact zero separators:

```text
0871 = 0
0879 = 0
087A = 0
087E = 0
087F = 0
0880 = 0
```

This creates the same structural layout on both topology families:

```text
0870        context word
0871        separator/reserved

0872..0878  seven-word value group

0879..087A  separator/reserved

087B..087D  three-word value group

087E..0880  separator/reserved
```

Legacy has all seven words `0872..0878` populated.

Eco5 has:

```text
0872..0876 populated
0877..0878 = 0
```

That fits a fixed logical counter schema where unsupported/not-used functions may serialize as zero.

The manual-derived interpretation remains:

```text
0872..0878  candidate BEDRIJFS TIJD group
087B..087D  candidate ONTDOOIEN statistics group
```

### Evidence refinement

Cross-topology geometry **strengthens the group-level service-counter interpretation**.

It does **not** independently prove the exact individual labels/order.

In particular, the previous defrost mapping remains a hypothesis pending a direct XTR UI value cross-check.

---

# 12. `0870` word0 remains a portable cross-page context bridge

Across compared systems:

```text
0870.word0 = (06E3 << 8) | 06E2
```

Examples:

```text
legacy = 55CE
Eco5 2026-09-26 = 046B
Eco5 2026-09-28 = 046C
```

The numerical value is topology/system-specific, but the packing relationship survives.

This is another form of logical ABI stability:

```text
same transformation
different underlying system value
```

---

# 13. Five portability classes

The runtime family should no longer be documented as simply "portable" or "not portable".

It contains at least five distinct classes.

## A. Portable direct logical fields

Examples:

```text
07D0 supply
07D3 DHW upper
07D4 DHW main
07DA outdoor current
07DD..07E1 controller context
081A AFDC
0858..085E clock/date
```

## B. Portable logical fields with topology-specific source substitution

Examples:

```text
07D1 return line
  old A7F9
  modern 1E:0000 / 10

07E4 average outdoor
  old 04:ABE0
  modern 1E:0005 / 10

0820-family outdoor telemetry
  old A5
  modern 1E
```

## C. Capability/identity fields

Examples:

```text
07E8..07EB modern 1E metadata
0830/0831 modern 1E identity/capability pair
0819 legacy 0 vs Eco5 20
0867 legacy 22 vs Eco5 232
```

## D. Generation-specific derived runtime fields

Examples:

```text
07F4 operating-state summary
083B/083C
0845
0865/0866
```

These can have stable logical purpose but their encoding must not be assumed portable without evidence.

## E. Reserved / legacy compatibility fields

Examples:

```text
07F8 page
zero/unavailable 0820 extension slots
various sparse 0834 fields
```

---

# 14. Revised architecture for an Online/DCM emulator

The best model is now:

```text
                  LOGICAL DCM RUNTIME MODEL
                           |
        +------------------+------------------+
        |                                     |
   legacy adapter                         modern adapter
        |                                     |
0x02 + 0x04 + A5 + 0x06               0x02 + 0x1E + 0x06
        |                                     |
        +------------------+------------------+
                           |
                 0x0F runtime serializer
                           |
      07D0 / 07E4 / ... / 0870 / service pages
```

For the current XTR M project this matters in two ways:

1. **The DCM-facing `0x0F` page namespace is more portable than the underlying physical bus.**
2. **The payload bytes are not universally portable.**

So a future emulator should implement:

```text
logical field semantics
+ topology-specific source adapter
+ topology-specific capability/constants
```

rather than replaying a complete Eco5 or legacy payload template.

---

# 15. Local XTR relevance

The local XTR M is already known to use the modern `0x1E` outdoor-unit family rather than legacy `0x04/A5`.

Therefore the modern adapter is the appropriate starting model for:

```text
07D1
07E4
0820
0834
0864
```

But evidence discipline remains:

- Eco5 source relationships = genuine cross-model Online/DCM evidence;
- local XTR `0x1E` register semantics that were separately measured remain locally confirmed;
- the final XTR `0x0F` serializer equality for each field must not be assumed until observed locally.

The cross-topology result increases confidence in **architecture**, not permission to replay foreign payloads.

---

# Evidence classification

## Observed facts

- principal runtime page shapes are the same across both topology families.
- `07D1` changes physical source while retaining its logical temperature role.
- `07E4` changes physical source while retaining average-outdoor semantics.
- `07E8..07EB` exactly source from modern `1E:001C,001D,0016,0017` in 83/83 source-qualified frames.
- `0830/0831` exactly source from `1E:0016/0017` in 33/33 source-qualified frames.
- legacy `0820` front/tail slots source from A5; modern `0820` sources from `0x1E`.
- `0819` is 0 in all 6 legacy `080C` frames and 20 in all 65 Eco5 frames.
- the full `0858..085E` clock/date tuple is valid in 54/54 frames and weekday is Monday-zero in 54/54.
- `0867` is stable at `0016` legacy and `00E8` Eco5.
- all 83 `0870` frames share the same separator geometry.

## Strong conclusions

1. `0x0F` is a logical serializer/normalizer layer across Thermia/Danfoss topology generations.
2. Page address/count is more stable than physical source address.
3. Some fields are true logical ABI fields; others are topology capabilities, optional extensions or generation-specific encodings.
4. `0820` is a concrete adapter boundary between legacy A5 and modern `0x1E`.
5. the modern `07E4` signature is not arbitrary: it is selected/reordered metadata from `0x1E:0016..001D`.
6. replaying a complete cross-model runtime payload is unsafe even where the page address/count matches.
7. emulator design should separate logical model from backend adapter.

## Hypotheses

- `1E:0016/0017/001C/001D` are product/capability/identity metadata; exact labels OPEN.
- legacy and modern `082D..082F` may preserve some logical semantics despite different scales/encodings.
- the seven- and three-word `0870` groups are stable operation-time and defrost-service schemas.

## Unknowns

- exact identity of the modern 1E metadata words.
- exact legacy semantics of A5 tail fields `0032..0037`.
- whether legacy `0865/0866` implement the same running/start flags.
- cross-topology semantic identity of every `0834` field.
- exact labels/order/scaling of `0872..0878`.
- direct local-XTR confirmation of the complete normalized runtime serializer.

---

# Result

**PROTO-OFFLINE-13 — COMPLETE / POSITIVE**

The cross-topology model is now much clearer:

> Thermia Online/DCM presents a relatively stable logical `0x0F` runtime ABI while sourcing and synthesizing that ABI from generation-specific physical endpoints.

The correct implementation target is therefore not "copy Eco5 packets" or "copy legacy packets", but:

```text
logical Online/DCM schema
        +
XTR-specific source adapter
        +
locally confirmed capability/constants
```

No live bus action, write, YAML change, restart or experiment-status change was performed.