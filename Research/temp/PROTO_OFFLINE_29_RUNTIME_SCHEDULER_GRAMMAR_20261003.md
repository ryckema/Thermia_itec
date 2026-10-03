# PROTO-OFFLINE-29 — runtime scheduler grammar

**Date:** 2026-10-03  
**Status:** **COMPLETE / POSITIVE**  
**Hypothesis:** runtime traffic can be reduced to a small grammar separating ordinary cyclic publication, service-refresh state and recurrent overlays, rather than treating W4 as a literal one-shot page command.  
**Controlled change:** offline capture analysis only. No bus TX, YAML change, reboot or setting write.

## Corpus

All six genuine Online/DCM reference captures were analysed. The runtime-family page map remains:

`07D0, 07E4, 07F8, 080C, 0820, 0834, 0848, 085F, 0864, 0870, 0884`.

## Normal Eco5 runtime grammar

During ordinary runtime with no configuration work in W2/W3, the controller publishes a highly regular ring.

Most answered `0708` polls are separated by about **4.24 s median**.

The dominant inter-poll publication groups are:

```
A: 07D0 -> 07E4
B: 07F8 -> 080C
C: 0820 -> 0834
D: 0848 -> 0864
E: 0870
```

and then the sequence repeats.

`0884` appears only occasionally as a history/service publication rather than once per normal ring.

This ring continues while Eco5 W4 is either `0000` or the common `0100` state. Therefore W4 cannot be interpreted as “the only page(s) that may be sent before the next poll”.

## W4 refinement

During broad service/configuration refresh episodes W4 takes staged values such as:

`03DF -> 03DC -> 03D8 -> 03D0 -> ... -> 038C -> 0380 -> 0300 -> 0200`

and bits clear in correspondence with ACKed runtime/service page families.

This supports W4 as a **remaining runtime/service work/state bitmap during refresh**.

However ordinary cyclic runtime pages continue around that work, so the safe model is:

```
normal publication ring
+ optional W4 service work
+ configuration W2/W3 work
+ recurrent overlays
```

rather than one exclusive W4-driven scheduler.

## ACK behavior

Across the six genuine captures:

- ordinary runtime pages are normally ACKed at very high rates;
- `07D0/07E4/07F8/080C/0820/0834/0848/0864` are ~97–100% ACKed in the examined corpus;
- `0884` is 9/9 ACKed where present;
- `085F` is only 18/329 ACKed;
- `0870` is 52/83 overall because one older reconnect capture contains 31 repeated unACKed `0870` publications; in the normal Eco5 captures `0870` is consistently ACKed.

### Strong conclusion

Known page shape alone is not enough to decide whether to ACK.

`085F` is the clearest recurrent overlay: it can be published repeatedly without ACK and later be ACKed in an explicit service/synchronization context.

`0870` has a similar context-sensitive exception in one older reconnect window.

## Emulator grammar

A safe reference implementation should model at least three runtime classes:

### 1. NORMAL_RING
Expect cyclic controller publications in the A→B→C→D→E family. ACK only page shapes already proven safe in the current qualified runtime context.

### 2. SERVICE_REFRESH
W4 may hold a remaining-work bitmap while W2/W3 configuration work is also active. ACKing mapped service pages may clear W4 bits, but ordinary ring traffic may interleave.

### 3. RECURRENT_OVERLAY
Pages such as `085F` can recur outside strict work state. Presence alone is not permission to ACK.

Unexpected page/order combinations remain capture-only.

## Strong conclusions

1. Eco5 runtime has a stable cyclic publication ring independent of literal W4 exclusivity.
2. W4 is best described as runtime/service state or remaining-work metadata.
3. W2/W3 configuration work and W4 service work can coexist.
4. `085F` is demonstrably context-sensitive and mostly unACKed.
5. A future emulator should separate **page recognition** from **permission to ACK**.

## Live status

Unchanged:
- EXP387 COMPLETE / POSITIVE
- EXP388 RUNNING / PARTIAL
