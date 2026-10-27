# Thermia iTec XTR M — mailbox + synchronization-sequence completion

**Date:** 2026-10-03  
**Track:** PROTO-OFFLINE-19  
**Status:** **COMPLETE / POSITIVE** — offline evidence analysis only  
**Baseline:** PROTO-OFFLINE-09 scheduler reduction, PROTO-OFFLINE-10 desired-state reconstruction, PROTO-OFFLINE-17/18 startup readiness work, both genuine Eco5 + Thermia Online captures, plus the four older genuine Online/DCM reference captures for `0708` word inventory  
**Controlled change:** no device change. Separate the genuine Eco5 controller-driven initial configuration export from later `0708`-driven refresh traffic, classify bootstrap-only versus mailbox-refreshable pages, test ACK-gating/order, and re-check unresolved `W0/W4/W5` plus desired selectors for `0442` and `0546`.  
**Device TX:** none  
**YAML change:** none  
**Heat-pump reboot:** none  
**Setting write:** none  
**Live XTR experiment status:** unchanged — EXP388 remains RUNNING / PARTIAL  
**GitHub modification:** none

---

## Hypothesis

The startup traffic previously grouped broadly as “sync” actually contains two different mechanisms:

1. a controller-autonomous bootstrap export that starts immediately after the first accepted `03E8` ACK;
2. a later DCM/mailbox-driven refresh mechanism selected by `0708 W2/W3`.

If true, the corpus should show a stable bootstrap spine before the first `0708`, while later mailbox refreshes should select only the bitmapped subset.

**Result: positive.**

---

# 1. Major result: genuine Eco5 has a fixed 32-page bootstrap before `0708`

All six successful genuine Eco5/Online sessions contain the same ordered configuration spine:

```text
03E8 03FC 0410 042E 0442 0456 046A 047E
0492 04A6 04BA 04D8 04F6 050A 051E 0532
0546 055A 057B 059C 05BD 05DE 05FF 0620
0641 0662 0683 06A4 06C5 06EA 06F1 06F4
```

Properties:

- all **32/32** page indices occur in every successful startup;
- the first accepted occurrence follows the same ascending page-index order in **6/6** sessions;
- `06F4/count19` is the terminal member of the strict configuration spine;
- the first `0708/count6` poll occurs only **after** this 32-page sequence has completed.

Session summary:

| Session | Bootstrap pages | Order match | unACKed config retries | first `03E8` ACK -> accepted `06F4` ACK | first `0708` after first `03E8` ACK |
|---|---:|---|---:|---:|---:|
| E26-A | 32/32 | exact | 4 | 36.722 s | 38.103 s |
| E26-B | 32/32 | exact | 1 | 62.790 s | 66.898 s |
| E28-A | 32/32 | exact | 2 | 34.453 s | 38.063 s |
| E28-B | 32/32 | exact | 2 | 34.441 s | 35.802 s |
| E28-C | 32/32 | exact | 3 | 35.905 s | 40.118 s |
| E28-D | 32/32 | exact | 2 | 34.446 s | 38.094 s |

The long E26-B duration is not a different page order: the same spine pauses after `06A4` while recurrent/overlay traffic occurs, then resumes with `06C5 -> 06EA -> 06F1 -> 06F4`.

### Strong conclusion

The genuine Eco5 initial configuration export is **not initiated by a preceding `0708 W2/W3` selector**.

It is a separate controller-autonomous startup phase.

This refines the older shorthand “full sync” used for later `FFFF/867F` mailbox states.

---

# 2. The bootstrap is ACK-gated

Across the six sessions there are:

```text
31 page-to-next-page transitions × 6 sessions = 186 transitions
```

For all **186/186**, the current spine page receives its matching FC16 address/count ACK before the controller first emits the next spine page.

When an ACK is missed, the same page is retried before progression.

Examples include retries of:

```text
03E8
03FC
042E
04D8
055A
057B
059C
05BD
0620
0662
0683
06A4
06C5
```

depending on the session.

### Strong conclusion

For the genuine Eco5 bootstrap:

```text
send current configuration page
        ↓
wait for matching ACK
        ↓
retry same page if required
        ↓
advance to next page
```

is the correct state-machine model.

The recurrent overlays discussed below can interleave, but they do not change the first-accepted spine order.

---

# 3. `06F4` is the bootstrap/running-plane boundary

In all six successful sessions:

1. the ordered configuration spine ends at `06F4/count19`;
2. only after that point does the first `0708` mailbox poll occur;
3. runtime/service traffic can begin in the small gap between `06F4` and the first `0708`.

Observed immediate post-`06F4` behavior differs:

- some sessions show `07D0` / `07E4`;
- some show an ACKed `085F`;
- one first `07D0` is unACKed.

Therefore there is **no single mandatory first runtime page** after `06F4`.

What is stable is the boundary:

```text
03E8 ... 06F4   = strict bootstrap configuration spine
after 06F4      = runtime/service/mailbox plane may begin
```

This is consistent with the later local XTR work that uses `06F4` as an important initial-sync completion marker, but the result here is genuine Eco5 evidence and must not be promoted to universal XTR behavior solely from this cross-model capture.

---

# 4. Later `FFFF/867F` is a 26-page mailbox refresh, not the bootstrap itself

PROTO-OFFLINE-09 correctly decoded:

```text
W2 = FFFF
W3 = 867F
```

as selecting 26 configuration pages.

PROTO-OFFLINE-19 adds the missing lifecycle distinction:

- the initial bootstrap sends **all 32 pages** before any `0708`;
- later `FFFF/867F` responses request only **26 pages**;
- in six clean `FFFF/867F` refresh windows, the 26 selected pages appear in exact ascending selector/page-index order;
- one additional `FFFF/867F` window crosses a later controller power gap and is therefore not a clean single-window ordering test.

The six pages omitted from the later 26-page refresh are:

```text
047E
0492
04D8
04F6
050A
051E
```

---

# 5. Six pages are bootstrap-only in the current Eco5 corpus

The two Eco5 captures contain six successful session openings.

Raw FC16 request counts for five of the omitted pages are exactly:

```text
047E = 6
0492 = 6
04F6 = 6
050A = 6
051E = 6
```

`04D8` occurs seven times because one bootstrap transmission is retried after a missing ACK.

Thus every occurrence of these six page families is accounted for by the six initial bootstraps.

They do **not** appear in the later `FFFF/867F` mailbox refresh set.

### Classification

For the examined genuine Eco5/Online corpus:

```text
047E
0492
04D8
04F6
050A
051E
```

are **bootstrap-only configuration pages**.

This does not prove that another Thermia profile can never request them at runtime.

---

# 6. The remaining 26 configuration pages are mailbox-refreshable

The later `FFFF/867F` scheduler state selects:

```text
03E8 03FC 0410 042E 0442 0456 046A
04A6 04BA 0532
0546 055A 057B 059C 05BD 05DE 05FF 0620
0641 0662 0683 06A4 06C5 06EA 06F1 06F4
```

The controller services them in page-index order, while runtime/service pages can be interleaved.

Subsequent `0708` responses often contain residual masks such as:

```text
FF80/0000
F000/0000
E000/0000
C000/0000
8000/0000
0000/0000
```

after earlier selected pages have already been serviced.

### Strong conclusion

`W2/W3` is not merely a static capability mask.

During a refresh it behaves as a **remaining configuration-work bitmap**: bits disappear as the selected page work progresses.

This is consistent with the exact bit-to-page mapping established in PROTO-OFFLINE-09.

---

# 7. Recurrent overlays are separate from strict configuration progression

Two page families are especially clear:

```text
04A6/count13
085F/count5
```

Across the two Eco5 captures:

```text
04A6 requests = 583
085F requests = 319
```

Most are not ACKed by the genuine gateway:

```text
04A6: only a small minority receive FC16 ACKs
085F: only a small minority receive FC16 ACKs
```

Yet when `04A6` appears at its fixed position in the 32-page bootstrap, it **is** ACKed and progression continues.

`085F` can likewise be ACKed during the relevant service/synchronization state while being ignored during recurrent background traffic.

### Strong conclusion

The presence of a page on the wire is not by itself evidence that it belongs to the active strict sync worklist.

For these recurrent families the gateway can selectively ACK based on session/scheduler context.

This reinforces the project's capture-only rule for unexpected traffic.

`04BA` also occurs outside the minimal expected bootstrap/refresh count and is therefore a hybrid/recurrent candidate, but its exact extra role is not reduced enough here to promote it to the same status as `04A6`/`085F`.

---

# 8. `W4` refinement: page-family state, not an exclusive “next page” selector

PROTO-OFFLINE-09 mapped W4 bits 0..10 to:

```text
07D0 07E4 07F8 080C 0820 0834 0848 085F 0864 0870 0884
```

That mapping remains supported.

However, PROTO-OFFLINE-19 sharpens the semantics.

During early post-bootstrap runtime, genuine Eco5 repeatedly returns:

```text
W4 = 0100
```

while the controller emits a normal sequence containing pages such as:

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
```

not only `0864`.

During staged refresh states, W4 bits do clear in correlation with their mapped page families.

### Revised wording

W4 should be treated as:

> **runtime/service page state / refresh-work bitmap**

and **not** as:

> “send exactly the pages whose W4 bits are currently set, and no others.”

The exact level/edge semantics remain profile- and state-dependent.

This retains the structural bit-to-page map while avoiding an overly literal scheduler interpretation.

---

# 9. `W0` remains completely unobserved

Across all six genuine Online/DCM reference captures:

```text
0708 requests  = 327
answered        = 302
W0 != 0000      = 0
```

The symmetry hypothesis remains attractive:

```text
W0 = desired-state pull bitmap for page indices16..31
W1 = desired-state pull bitmap for page indices0..15
```

but there is still **zero direct genuine evidence** for any W0 bit.

Therefore:

```text
W0 bit0 -> 0546
```

must remain **HYPOTHESIS ONLY**.

It is not a proven Operation Mode desired-state selector.

---

# 10. No genuine desired selector for `0442` or `0546` exists in the corpus

Across the 302 answered genuine `0708` responses:

```text
W1 non-zero:
  0001  four times  -> 03E8
  0008  two times   -> 042E

W1 bit4 / 0010:
  never observed

W0:
  always 0000
```

Therefore:

```text
0442 desired pull:
candidate by structural symmetry = W1 bit4 / 0010
direct genuine observation        = NONE

0546 desired pull:
candidate by structural symmetry = W0 bit0 / 0001
direct genuine observation       = NONE
```

### Result

The search for existing-capture proof of desired selectors for Cooling (`0442`) and Operation Mode/System (`0546`) is **negative**.

Do not promote either selector to proven and do not use them for a live experiment merely from bitmap symmetry.

---

# 11. `W5` remains profile/session metadata, not progress state

Across the same 302 answered genuine responses:

```text
Eco5:
W5 = 0000 in 264/264 answered responses

older Online/DCM:
W5 = 0006 in 37 responses
W5 = 0007 in one rejoin response
```

Within Eco5, W5 remains zero through:

- idle runtime;
- broad configuration refresh;
- staged W4 service refresh;
- desired-state commands.

### Strong conclusion

W5 is not a universal page-progress counter, desired selector, or generic “sync active” field.

The exact older-platform meaning of `0006/0007` remains OPEN.

---

# 12. Refined native session architecture

Best current model:

```text
APPROVAL ACCEPTED
      |
      v
WAITING FOR PAGE SERVICE
      |
      v
first accepted 03E8 ACK
      |
      v
CONTROLLER-AUTONOMOUS BOOTSTRAP
  32 config pages
  fixed ascending order
  ACK-gated
  terminal page = 06F4
      |
      v
RUNTIME / MAILBOX PLANE
      |
      +--> ordinary runtime/service publication
      |
      +--> 0708 W2/W3 configuration refresh worklists
      |       e.g. FFFF/867F = 26 refreshable pages
      |
      +--> 0708 W1 desired-state pulls
      |       proven only bit0 -> 03E8
      |                   bit3 -> 042E
      |
      +--> W4 runtime/service state/refresh bitmap
      |
      +--> recurrent overlays such as 04A6 / 085F
```

This is more precise than treating every configuration transfer as one mailbox-driven mechanism.

---

# 13. Evidence classification

## Observed facts

- six successful genuine Eco5 session openings contain all 32 configuration pages in the same first-accepted order.
- no `0708` poll occurs before completion of that 32-page spine.
- all 186 page-to-next-page transitions are preceded by an ACK of the current spine page.
- `06F4` is last in the strict bootstrap spine in all six sessions.
- later `FFFF/867F` selects 26 pages, not 32.
- six pages omitted by that mask occur only in the startup bootstrap within the current Eco5 corpus.
- six clean broad-refresh windows service the selected 26 pages in exact ascending page-index order.
- `04A6` and `085F` are recurrent and mostly unACKed outside synchronization contexts.
- W0 is zero in all 302 answered genuine `0708` responses.
- W1 is nonzero only as `0001` (4×) and `0008` (2×).
- W5 distribution is Eco5 `0000` versus older DCM `0006/0007`.

## Strong conclusions

1. Genuine Eco5 initial bootstrap and later mailbox refresh are distinct synchronization mechanisms.
2. The bootstrap is a fixed 32-page, ACK-gated controller-autonomous export.
3. Later mailbox refresh uses a 26-page refreshable subset and residual W2/W3 work masks.
4. The six omitted pages are bootstrap-only in the current Eco5 corpus.
5. `06F4` is the terminal strict-bootstrap page in all six successful genuine Eco5 sessions.
6. W4 maps to runtime/service page families but is not an exclusive immediate next-page selector.
7. Existing genuine captures do not prove desired selectors for `0442` or `0546`.

## Hypotheses

- W1 bit4 would be the `0442` desired-page selector by index symmetry.
- W0 bit0 would be the `0546` desired-page selector if W0 is the high-half desired bitmap.
- W5 carries implementation/profile/session metadata.
- `04BA` has an additional recurrent/startup role beyond ordinary configuration refresh.

## Unknowns

- any real non-zero W0 behavior;
- desired semantics for W1 bits other than 0 and 3;
- exact W4 level/edge semantics in each DCM generation;
- exact meaning of W5 values 6/7 on older DCM;
- why these six Eco5 pages are bootstrap-only rather than runtime-refreshable;
- exact extra role of `04BA`;
- whether modern Thermia Connect preserves the same split.

---

# Result

**PROTO-OFFLINE-19 — COMPLETE / POSITIVE**

The principal new result is the separation:

```text
32-page ACK-gated autonomous bootstrap
               !=
26-page 0708-driven configuration refresh
```

and the identification, in the current genuine Eco5 corpus, of six bootstrap-only page families:

```text
047E 0492 04D8 04F6 050A 051E
```

No live experiment was advanced, no new write target was introduced, and EXP388 remains RUNNING / PARTIAL.