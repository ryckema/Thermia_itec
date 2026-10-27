> **Reconciliation status: APPLIED / HISTORICAL (2026-10-03).** The canonical Research state was reconciled through PROTO-OFFLINE-16 in commit `b4edd42cd17354845ec75111fb0aa30e5a0bda38`. This file is retained as the historical proposal that informed that reconciliation; do not apply it again blindly.

# Pending canonical reconciliation — PROTO-OFFLINE-09

**Date:** 2026-10-03  
**GitHub:** not modified  
**Reason:** current request authorizes offline analysis, not GitHub writes.

## THERMIA_PROJECT_STATE.md — proposed update

Keep:

- current live experiment: `EXP388 — RUNNING / PARTIAL`;
- no calendar/live write implied by this offline result;
- existing PROTO-OFFLINE-07 and PROTO-OFFLINE-08 history unchanged.

Add:

- `PROTO-OFFLINE-09 — COMPLETE / POSITIVE`.
- `0x0F FC03 0708/count6` is now strongly reduced from a generic mailbox header to a page scheduler/disptacher.
- Six-word structure:
  - `W1` = low-half desired-state FC03 pull bitmap; bit0->`03E8`, bit3->`042E` directly proven.
  - `W0` = hypothesized high-half desired-state pull bitmap; never observed non-zero.
  - `W3` = low-half FC16 configuration/state upload bitmap, page indices0..15.
  - `W2` = high-half FC16 configuration/state upload bitmap, page indices16..31.
  - `W4` = runtime/service-page bitmap, mapped bits0..10 to `07D0,07E4,07F8,080C,0820,0834,0848,085F,0864,0870,0884`.
  - `W5` = implementation/profile/session metadata; exact semantics open.
- The 32-page configuration index is:
  `03E8,03FC,0410,042E,0442,0456,046A,047E,0492,04A6,04BA,04D8,04F6,050A,051E,0532,0546,055A,057B,059C,05BD,05DE,05FF,0620,0641,0662,0683,06A4,06C5,06EA,06F1,06F4`.
- Older rejoin `W2/W3=7FFF/FFFF` maps exactly to 31 pages and excludes only `06F4`.
- Eco5 full sync `FFFF/867F` maps exactly to 26 pages; omitted low-half bits are `047E,0492,04D8,04F6,050A,051E`.
- Command + confirmation flow is directly observed:
  `W1 bit -> FC03 desired page -> desired image -> matching W3 bit -> FC16 republish`, with exact payload equality for `03E8` and `042E` events.
- Refine old EXP182 interpretation:
  - `W2/W3` are not merely generic join markers; they are the page-upload bitmap.
  - `W4` is not generic state metadata; it is a runtime/service-page bitmap.
  - `W5=6/7` is not universal; Eco5 keeps W5=0 even during sync.

## EXPERIMENT_LOG.md — proposed entry

### PROTO-OFFLINE-09 — COMPLETE / POSITIVE — `0708` scheduler state machine

**Hypothesis:** the six `0708/count6` words encode explicit page-scheduler bitmaps rather than an opaque session header.

**Controlled change:** offline-only exhaustive correlation of all six genuine Online/DCM captures. No TX/YAML/restart/write.

**Observed:**
- 327 `0708` requests, 302 answered.
- W1 bit0 -> FC03 `03E8`; W1 bit3 -> FC03 `042E`.
- W2/W3 decode as a 32-page FC16 configuration/state bitmap.
- older `7FFF/FFFF` -> exact 31-page set;
- Eco5 `FFFF/867F` -> exact 26-page set;
- small masks (`4000/8000`, `0000/0001`, `0000/0008`) independently confirm bit positions.
- matching W1/W3 events pull desired page and republish an identical FC16 image.
- W4 bits0..10 align to the ordered runtime/service pages `07D0..0884`.
- W5 varies by platform; 6/7 old DCM, always 0 in Eco5.

**Result:** COMPLETE / POSITIVE.

No live experiment state change.

## PROTOCOL_FINDINGS.md — durable updates

### PROVEN / genuine Online/DCM structural

`W2/W3` of `0708/count6` form a 32-page FC16 upload bitmap:

```text
W3 bit0..15 -> page indices 0..15:
03E8 03FC 0410 042E 0442 0456 046A 047E
0492 04A6 04BA 04D8 04F6 050A 051E 0532

W2 bit0..15 -> page indices 16..31:
0546 055A 057B 059C 05BD 05DE 05FF 0620
0641 0662 0683 06A4 06C5 06EA 06F1 06F4
```

### PROVEN / observed desired pulls

- `W1 bit0 -> FC03 03E8`.
- `W1 bit3 -> FC03 042E`.
- When the corresponding W3 bit is also set, the controller republishes the desired FC03-returned page via FC16 with exact payload equality.

### STRONGLY SUPPORTED

`W4` is a runtime/service-page bitmap:

```text
bit0  07D0
bit1  07E4
bit2  07F8
bit3  080C
bit4  0820
bit5  0834
bit6  0848
bit7  085F
bit8  0864
bit9  0870
bit10 0884
```

Exact request/subscription/refresh level semantics can differ by DCM implementation.

### HYPOTHESIS

- `W0` is the high-half desired-state pull bitmap for page indices16..31.

### OPEN / UNKNOWN

- W1 bits other than bit0 and bit3.
- W0 behavior.
- W4 bits11..15.
- exact meaning of W5.

### DISPROVEN / SUPERSEDED

- `W2/W3=7FFF/FFFF` as merely opaque join/session magic.
  It is the concrete 31-page upload mask in that older DCM rejoin.
- W4 as generic state/capability metadata.
  It has a clear page-index role.
- universal interpretation `W5=6 normal / 7 join`.
  Eco5 uses W5=0 across steady state and full sync.

## Safety

Do not use unobserved W1 bits or any W0 bit in a live test.

A future active semantic test must:
- use a controller-originated genuine `0708` poll;
- set only one already-proven command bit;
- use a locally mapped low-risk desired-state page;
- know the current value before the test;
- preserve a deterministic rollback;
- abort on any scheduler/frame-shape deviation.