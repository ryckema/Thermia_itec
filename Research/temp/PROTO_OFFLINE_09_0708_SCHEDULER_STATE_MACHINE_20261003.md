> **Current-status note — REFINED BY PROTO-OFFLINE-19 (2026-10-03).** The W1 and W2/W3 bit-to-page mappings remain strong. Two lifecycle interpretations are refined: `FFFF/867F` is a later 26-page mailbox refresh, not the initial Eco5 bootstrap; and W4 is better described as a runtime/service page-family state/refresh bitmap, not an exclusive immediate next-page selector. Genuine Eco5 startup first performs a separate 32-page ACK-gated autonomous bootstrap through `06F4` before the first `0708` poll.

# Thermia iTec XTR M — `0x0708/count6` scheduler state-machine reduction

**Date:** 2026-10-03  
**Track:** PROTO-OFFLINE-09  
**Status:** COMPLETE / POSITIVE — offline analysis only  
**Baseline:** EXP182 `0x0708/count6` mailbox census + PROTO-OFFLINE-05 runtime-export family + current PROTO-OFFLINE-07/08 offline work  
**Numbering note:** PROTO-OFFLINE-07 and PROTO-OFFLINE-08 are already occupied in the current project Library. This analysis therefore uses **PROTO-OFFLINE-09** even though it was originally the third item in the offline-analysis plan.  
**Controlled change:** no device change. Reanalyse all six genuine Online/DCM captures and correlate every answered `0F 03 0708 0006` poll against immediate downstream FC03 desired-state reads and FC16 page uploads.  
**Device TX:** none  
**YAML change:** none  
**Heat-pump restart:** none  
**Setting write:** none  
**GitHub change:** none  
**Live experiment status:** unchanged — EXP388 remains RUNNING / PARTIAL

---

## Hypothesis

The six response words returned to:

```text
0F 03 0708 0006
```

are not an opaque session header. They contain explicit scheduler bitmaps which select native controller/DCM page families.

Specifically:

- one bitmap requests controller **FC03 desired-state pulls** from the DCM;
- one 32-bit bitmap requests controller **FC16 configuration/state uploads** to the DCM;
- one bitmap selects/marks the **runtime/service FC16 page family**;
- the remaining word contains implementation/session metadata.

**Result: strongly supported, with major parts directly demonstrated by exact bit-to-page correspondence.**

---

# 1. Corpus

Analysed raw captures:

- `thermia_capture_20260924_210001(1).log`
- `thermia_capture_20260925_071517.log`
- `thermia_capture_20260925_090209.log`
- `thermia_capture_20260925_090550.log`
- `itec_eco5_gateway_20260926.log`
- `itec_eco5_gateway_20260928.log`

Provenance follows PROTO-OFFLINE-03:

- first four = genuine older Online/DCM reference captures;
- last two = genuine iTec Eco5 + Thermia Online captures.

Across these six files:

```text
0708 requests  = 327
answered        = 302
```

The older `090550` rejoin capture contains the already-known 16 unanswered polls while the DCM is absent. A small number of Eco5 polls also have no captured response; they are not used for bitmap decoding.

---

# 2. The native 32-page configuration/state index

The controller uses the following ordered FC16 page family below the runtime-export region:

| Index | Page |
|---:|---:|
| 0 | `03E8` |
| 1 | `03FC` |
| 2 | `0410` |
| 3 | `042E` |
| 4 | `0442` |
| 5 | `0456` |
| 6 | `046A` |
| 7 | `047E` |
| 8 | `0492` |
| 9 | `04A6` |
| 10 | `04BA` |
| 11 | `04D8` |
| 12 | `04F6` |
| 13 | `050A` |
| 14 | `051E` |
| 15 | `0532` |
| 16 | `0546` |
| 17 | `055A` |
| 18 | `057B` |
| 19 | `059C` |
| 20 | `05BD` |
| 21 | `05DE` |
| 22 | `05FF` |
| 23 | `0620` |
| 24 | `0641` |
| 25 | `0662` |
| 26 | `0683` |
| 27 | `06A4` |
| 28 | `06C5` |
| 29 | `06EA` |
| 30 | `06F1` |
| 31 | `06F4` |

This exact ordered list is the key to decoding `0708`.

---

# 3. Words 2 + 3 are the 32-bit FC16 configuration/state upload bitmap

Number the six returned words:

```text
W0 W1 W2 W3 W4 W5
```

The mapping is:

```text
W3 bit  0 -> page index  0 -> 03E8
W3 bit  1 -> page index  1 -> 03FC
...
W3 bit 15 -> page index 15 -> 0532

W2 bit  0 -> page index 16 -> 0546
W2 bit  1 -> page index 17 -> 055A
...
W2 bit 15 -> page index 31 -> 06F4
```

So:

```text
W2 = high 16 page bits
W3 = low 16 page bits
```

This is no longer merely a hypothesis.

## 3.1 Older DCM rejoin: exact 31-page match

First answered `0708` during the 2026-09-25 `090550` DCM rejoin:

```text
W2 = 7FFF
W3 = FFFF
```

Decoded:

```text
all 32 configuration pages requested
EXCEPT page index31 = 06F4
```

Before the next answered `0708`, the controller emits **exactly 31 unique FC16 configuration page starts**:

```text
03E8 03FC 0410 042E 0442 0456 046A 047E
0492 04A6 04BA 04D8 04F6 050A 051E 0532
0546 055A 057B 059C 05BD 05DE 05FF 0620
0641 0662 0683 06A4 06C5 06EA 06F1
```

`06F4` is the only member of the 32-page index not sent.

Set equality:

```text
bitmap-selected pages = 31
observed unique FC16 config pages = 31
exact equality = YES
```

This materially supersedes the old description of `7FFF/FFFF` as merely a generic “join/resync signature”.

It is a **specific full-state upload request bitmap**.

The reason it appeared only on DCM rejoin in the older corpus is that rejoin requested almost the complete controller state.

---

## 3.2 Eco5 full sync: exact 26-page match

Eco5 full-sync header:

```text
W2 = FFFF
W3 = 867F
```

`867F` has bits:

```text
0,1,2,3,4,5,6,9,10,15
```

set in the low page half.

Therefore the selected low-half pages are:

```text
03E8 03FC 0410 042E 0442 0456 046A 04A6 04BA 0532
```

and all sixteen high-half pages `0546..06F4` are selected.

Total:

```text
10 + 16 = 26 pages
```

The controller emits exactly those **26 distinct configuration pages** before the next clean `0708` state.

This exact equality is independently present in both Eco5 captures.

The six omitted low-half pages are:

```text
047E
0492
04D8
04F6
050A
051E
```

This is strong cross-model evidence that `W2/W3` encode requested page presence/state, while model/topology capability determines which page bits are set.

---

## 3.3 Small bitmap states prove individual positions

Eco5 transition:

```text
W2=4000
W3=8000
```

decodes to:

```text
W3 bit15 -> 0532
W2 bit14 -> 06F1
```

and the controller immediately emits:

```text
FC16 0532
FC16 06F1
```

A separate command event:

```text
W2=0000
W3=0001
```

causes an FC16 push of:

```text
03E8
```

Another:

```text
W2=0000
W3=0008
```

causes:

```text
042E
```

Residual examples also decode naturally:

```text
W2=FF80 -> 0620,0641,0662,0683,06A4,06C5,06EA,06F1,06F4
W2=F000 -> 06C5,06EA,06F1,06F4
W2=E000 -> 06EA,06F1,06F4
W2=C000 -> 06F1,06F4
W2=8000 -> 06F4
```

Across all 28 answered cycles with non-zero `W2/W3`, **25 clean windows have exact set equality** between the bitmap and the distinct configuration pages emitted before the next answered `0708`.

The remaining three windows span missing `0708` responses / another long resynchronization and are not clean single-state windows; they do not contradict the mapping.

**Status: PROVEN / structural in genuine Online/DCM captures.**

---

# 4. Word 1 is the low-half desired-state FC03 pull bitmap

EXP182 had already proven:

```text
W1 = 0001
```

causes immediate controller:

```text
FC03 03E8
```

The Eco5 captures add a second bit:

```text
W1 = 0008
```

causes:

```text
FC03 042E
```

Observed command-pull events in the six-file corpus:

| `W1` | Immediate FC03 | Observations | Response→FC03 delay |
|---:|---:|---:|---:|
| `0001` | `03E8` | 4 | ~39–46 ms |
| `0008` | `042E` | 2 | ~31–47 ms |

Thus:

```text
W1 bit0 -> desired-state page 03E8
W1 bit3 -> desired-state page 042E
```

Those are the same page indices used by the `W3` FC16 upload bitmap.

**Strong conclusion:** `W1` is not a scalar selector. It is a **desired-state dirty/pull bitmap for at least the low 16 configuration-page indices**.

No other `W1` bits are observed in the corpus, so their meanings must not be invented.

---

# 5. Word 0 is probably the high-half desired-state pull bitmap — but remains unobserved

The natural structural model is:

```text
W0 = desired-state pull bitmap, indices 16..31
W1 = desired-state pull bitmap, indices 0..15
```

because `W2/W3` use precisely that high-word/low-word arrangement for state uploads.

However:

```text
W0 = 0000
```

in every captured `0708` response analysed here.

Therefore:

**HYPOTHESIS / structurally strong:** `W0` is the high 16 bits of the desired-state pull bitmap.

**NOT PROVEN:** no `W0` bit has ever been observed asserted.

Do not transmit a non-zero W0 based only on symmetry.

---

# 6. Pull + publish forms a real command-confirmation transaction

Three Eco5 events give especially clean command flow.

## 6.1 `03E8`

Header:

```text
W1=0001
W3=0001
```

Sequence:

```text
0708 response
 -> FC03 03E8/count14
 -> DCM returns desired 03E8 image
 -> controller FC16 publishes 03E8/count14
```

The FC03-returned 14-word image and the following FC16-published 14-word image are **word-for-word identical**.

## 6.2 `042E`

Header:

```text
W1=0008
W3=0008
```

Sequence:

```text
0708 response
 -> FC03 042E/count15
 -> DCM returns desired 042E image
 -> controller FC16 publishes 042E/count15
```

Again, the FC03-returned image and following FC16 image are **word-for-word identical**.

Two separate `042E` events show the first word changing `1 -> 0`; both are pulled by FC03 and then republished identically by FC16.

**Strong conclusion:**

`W1` and `W3` are independent but complementary page-index bitmaps:

```text
W1 bit set -> controller pulls desired page from DCM via FC03
W3 bit set -> controller publishes current/resulting page to DCM via FC16
```

When the same bit is present in both, the observed transaction is:

```text
pull desired page
apply/accept at controller level
publish resulting page back
```

This is the clearest native Online/DCM semantic write architecture found so far.

It also explains why direct second-master FC16 writes to `0x0F` were the wrong direction for semantic command ingress.

---

# 7. Word 4 is an 11-bit runtime/service-page bitmap

The runtime/service page index is:

| W4 bit | Native page |
|---:|---:|
| 0 | `07D0` |
| 1 | `07E4` |
| 2 | `07F8` |
| 3 | `080C` |
| 4 | `0820` |
| 5 | `0834` |
| 6 | `0848` |
| 7 | `085F` |
| 8 | `0864` |
| 9 | `0870` |
| 10 | `0884` |

Bits 11..15 have not been observed asserted.

## 7.1 Older steady-state mask

Older genuine Online/DCM steady state:

```text
W4 = 077F
```

Set bits:

```text
0,1,2,3,4,5,6,8,9,10
```

The recurring service family in those captures is exactly:

```text
07D0
07E4
07F8
080C
0820
0834
0848
0864
0870
0884
```

That is an exact one-for-one match.

The missing bit is:

```text
bit7 -> 085F
```

and `085F` is likewise absent from the steady runtime ring in those particular captures.

## 7.2 Rejoin isolates bit7

First older DCM-rejoin header:

```text
W4 = 0080
```

Only bit7 is set.

During the following state resynchronization, the controller repeatedly sends:

```text
085F/count5
```

while the ordinary configuration pages are being transferred.

After rejoin, W4 becomes `077F`, bit7 clears, and the normal runtime-page family takes over.

This directly supports:

```text
W4 bit7 = 085F
```

## 7.3 Eco5 staged masks

Eco5 provides further staged evidence:

```text
03DF -> 03DC    clears bits0,1 after 07D0/07E4 service
03DC -> 03D8    clears bit2 during 07F8 service
03D8 -> 03D0    clears bit3 during 080C service
03D0 -> ...     bit4 corresponds to 0820
... bit6        corresponds to 0848
0380 -> 0300    clears bit7 around 085F
0300 -> 0200    clears bit8 around 0864
0200 -> 0000    clears bit9 around 0870
```

The Eco5 full-sync value `03DF` notably omits bit5 and bit10, and `0834`/`0884` are correspondingly not part of that forced runtime refresh set.

**Status: STRONGLY SUPPORTED / near-structural proof for the complete W4 bit0..10 map.**

### Important semantic caution

The exact *meaning of a set W4 bit* is implementation/state dependent:

- older DCM keeps `077F` asserted continuously in steady state while the corresponding runtime family repeats;
- Eco5 often uses `0000` in steady state and non-zero W4 values transiently during refresh/resync.

Therefore the safest name is:

```text
W4 = runtime/service-page request / subscription / refresh bitmap
```

The exact edge/level semantics are not yet universal across DCM generations.

---

# 8. Word 5 is not a universal 6/7 session code

Older captures:

```text
steady / normal: W5 = 0006
first DCM-rejoin response: W5 = 0007
```

This was previously interpreted as a general normal-vs-join phase code.

The Eco5 corpus changes that conclusion:

```text
Eco5 2026-09-26: W5 = 0000 in all 183 answered 0708 responses
Eco5 2026-09-28: W5 = 0000 in all 81 answered 0708 responses
```

including full synchronization states.

Therefore:

**DISPROVEN / SUPERSEDED:** `W5=6` normal and `W5=7` join is not a universal Thermia Online/DCM state enum.

**Observed older-DCM fact:** that platform changes `7 -> 6` across rejoin.

**Current safest classification:** implementation/profile/session metadata, exact meaning OPEN.

---

# 9. Revised `0708` model

The strongest current model is:

```text
0708/count6 response

W0  desired-state FC03 pull bitmap, high 16       HYPOTHESIS
W1  desired-state FC03 pull bitmap, low 16        PROVEN for bit0 + bit3

W2  controller-state FC16 upload bitmap, high 16  PROVEN
W3  controller-state FC16 upload bitmap, low 16   PROVEN

W4  runtime/service page bitmap, bits0..10         STRONGLY SUPPORTED
W5  implementation/profile/session metadata       OPEN
```

The page-index model shared by W1/W3 is particularly important:

```text
bit0 -> 03E8
bit1 -> 03FC
bit2 -> 0410
bit3 -> 042E
...
bit15 -> 0532
```

and W2 continues indices16..31.

---

# 10. Native Online/DCM command state machine

The observed state machine can now be reduced to:

```text
controller
   |
   | FC03 0708/count6
   v
DCM mailbox scheduler header
   |
   +-- W1 command bit(s) set?
   |      |
   |      +--> controller FC03 pulls desired page
   |             e.g. bit0 -> 03E8
   |                  bit3 -> 042E
   |
   +-- W2/W3 state-upload bit(s) set?
   |      |
   |      +--> controller FC16 publishes selected config/state pages
   |
   +-- W4 runtime/service bits
          |
          +--> selects/marks runtime/service page family
```

When command and state-upload bits for the same page are both present:

```text
0708
 -> desired FC03 pull
 -> desired image returned
 -> FC16 publish of same page image
 -> normal runtime scheduler continues
```

During rejoin/full resynchronization:

```text
0708
 -> broad W2/W3 bitmap
 -> controller publishes selected configuration/state page set
 -> W4 simultaneously controls/requests runtime/service refreshes
 -> scheduler eventually returns to steady runtime cycle
```

This is substantially more specific than the earlier “mailbox/session header” interpretation.

---

# 11. What this changes in the write-access project

This finding is highly relevant to the main goal.

The native semantic command path is no longer just:

```text
W1=1 -> read 03E8
```

It is better described as a **page-indexed desired-state pull architecture**.

For a future DCM emulator:

1. the controller owns the timing;
2. controller polls `0708`;
3. the emulator signals one desired page with a W1 bit;
4. controller asks for that page with FC03;
5. emulator returns the desired page image;
6. controller can republish the resulting page via FC16.

This is the architecture to emulate.

It is **not** equivalent to injecting an FC16 settings page toward slave `0x0F`.

---

# 12. Safety implications

This offline result does **not** justify a new live write yet.

Reasons:

- local XTR EXP388 work is still RUNNING / PARTIAL;
- local scheduler enablement/topology remains a separate prerequisite;
- only W1 bit0 and bit3 are directly observed desired-state command bits;
- W0 has never been non-zero;
- exact controller acceptance rules for a locally emulated 0708/FC03 transaction must remain bounded to known pages and known current values.

Do not probe unobserved W1 bits and do not set W0 based only on symmetry.

A future active semantic test should use an already-mapped low-risk page and exactly one proven W1 bit, after the controller-side scheduler path is safely available.

---

# Evidence classification

## Observed facts

- `0708/count6` occurs in all genuine scheduler-enabled Online/DCM captures.
- `W1=1` is followed by FC03 `03E8`.
- `W1=8` is followed by FC03 `042E`.
- `W2/W3=7FFF/FFFF` selects exactly 31 FC16 configuration pages in older DCM rejoin.
- `W2/W3=FFFF/867F` selects exactly 26 FC16 configuration pages in Eco5 full sync.
- `W2/W3=4000/8000` selects `0532` and `06F1`.
- isolated `W3=1` and `W3=8` select FC16 `03E8` and `042E`.
- matching W1+W3 command events pull a desired page and then republish an identical page image.
- older `W4=077F` exactly matches its ten-page recurring runtime/service family.
- older `W4=0080` coincides with repeated `085F`.
- Eco5 uses staged W4 masks that align with runtime/service page progression.
- W5 is always zero in 264 answered Eco5 responses but is 6/7 in the older DCM corpus.

## Strong conclusions

- W2/W3 form the exact 32-page controller-state FC16 upload bitmap.
- W1 is a low-half desired-state FC03 pull bitmap, not a scalar selector.
- W4 is a runtime/service-page bitmap with a stable bit-to-page ordering.
- the 0708 scheduler is the core page dispatcher for both semantic command pulls and state/runtime publication.
- the older `7FFF/FFFF` value is not opaque join magic; it is a near-full configuration-page request bitmap.

## Hypotheses

- W0 is the high-half desired-state pull bitmap corresponding to page indices16..31.
- W4 set-bit level semantics differ by DCM generation but retain the same page-index role.

## Unknowns

- any W0 bit behavior;
- W1 bits other than 0 and 3;
- exact semantic name of W5;
- W4 bits above bit10;
- exact local-XTR prerequisite that enables the full `0708` scheduler topology.

---

# Result

**PROTO-OFFLINE-09 — COMPLETE / POSITIVE**

This analysis closes a major structural unknown left by EXP182.

The `0708/count6` block is now best understood as a scheduler dispatch structure with:

- desired-state pull selection;
- 32-page state-upload selection;
- runtime/service-page selection;
- one still-unknown implementation/session word.

No live experiment status changed and no GitHub files were modified.