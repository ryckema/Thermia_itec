# Thermia 0708 offline reduction — 2026-09-30

Status: **offline analysis COMPLETE**

Scope: six available genuine gateway/DCM captures, including the two iTec Eco5 gateway logs and four older genuine ATEC/DCM-family captures. This document records cross-model evidence separately from local XTR confirmation.

## Corpus reduction

- exact FC03 0708/count6 requests: 327
- requests with a paired six-word response suitable for reduction: 302

Response layout:

    W0 W1 W2 W3 W4 W5

## Evidence classification

### STRONGLY SUPPORTED — W2:W3 controller->gateway page refresh bitmap

W2:W3 forms a 32-bit page-selection mask for configuration pages. Set bits correlate with controller-originated FC16 pages as follows:

| bit | page | bit | page |
|---:|---:|---:|---:|
| 0 | 03E8 | 16 | 0546 |
| 1 | 03FC | 17 | 055A |
| 2 | 0410 | 18 | 057B |
| 3 | 042E | 19 | 059C |
| 4 | 0442 | 20 | 05BD |
| 5 | 0456 | 21 | 05DE |
| 6 | 046A | 22 | 05FF |
| 7 | 047E | 23 | 0620 |
| 8 | 0492 | 24 | 0641 |
| 9 | 04A6 | 25 | 0662 |
| 10 | 04BA | 26 | 0683 |
| 11 | 04D8 | 27 | 06A4 |
| 12 | 04F6 | 28 | 06C5 |
| 13 | 050A | 29 | 06EA |
| 14 | 051E | 30 | 06F1 |
| 15 | 0532 | 31 | 06F4 |

Representative genuine observations:

- Eco5 W2:W3 = 4000:8000 is followed by 0532 and 06F1 refresh pages.
- Eco5 W2:W3 = FFFF:867F is followed by the corresponding multi-page configuration refresh.
- ATEC W2:W3 = 7FFF:FFFF is followed by the first 31 pages of the same ordered family, through 06F1 and excluding 06F4.

Page counts are model/firmware dependent in some captures. The page-index bit ordering is the durable finding; do not assume every cross-model count is identical.

### STRONGLY SUPPORTED — W1 gateway->controller desired-page PULL bitmap

Observed selectors:

| W1 | bit | controller FC03 pull |
|---:|---:|---:|
| 0001 | 0 | 03E8 |
| 0008 | 3 | 042E |

ATEC includes W1=0001 while W3=0000 followed by FC03 03E8, separating PULL from PUSH/refresh behavior.

### Genuine Eco5 desired-page roundtrip: 03E8

Observed sequence:

    0708 response with W1 bit0
    -> controller FC03 03E8/count14
    -> gateway returns 14-word desired page
    -> controller FC16 republishes 03E8/count14

One captured desired page differs from the prior/current page only at 03F4:

    03F4: 0014 -> 001E

A later transaction restores:

    03F4: 001E -> 0014

The controller's following FC16 page matches the gateway-supplied desired image in each case.

Local-XTR note: 03F4 is already independently confirmed as the room-setpoint mirror. That local mapping does not by itself prove the Eco5 write event has identical semantics on XTR.

### Genuine Eco5 desired-page roundtrips: 042E

Observed sequence:

    0708 response with W1 bit3
    -> controller FC03 042E/count15
    -> gateway returns desired page
    -> controller FC16 republishes 042E/count15

Captured one-field changes include:

    042F: 0001 -> 0000
    later 042E: 0001 -> 0000

Public DCM material labels 042E as Integral A1, but this semantic label is not imported as proven XTR behavior.

## HYPOTHESIS — W0

W0 is structurally positioned to be the high 16 bits of a 32-bit PULL bitmap, but it remained zero in all 302 paired responses in this reduction. No positive high-bit PULL example exists in the current corpus.

## OPEN / UNKNOWN — W4 and W5

Observed Eco5 W4 values include 0100, 010B, 03DF, 03DC, 03D8, 03D0, 03CF, 038C, 0380, 0300 and 0200. Older ATEC/DCM captures include substantially different values such as 077F and 0080, with W5 values including 0006/0007.

These fields may encode lifecycle/status/capability/session state. Their semantics are unresolved and literal values must not be transplanted between models without a matching capture context.

## Runtime export relationship

Genuine runtime repeatedly interleaves FC16 export pages and 0708 polls. A common runtime pattern is:

    07D0 -> 07E4 -> 0708
    07F8 -> 080C -> 0708
    0820 -> 0834 -> 0708
    0848 -> 0864 -> 0708
    0870 -> 0884 -> 0708

All-zero six-word responses occur often in normal runtime. Exact order/interleaving is state-dependent and must not be assumed universal.

## Architectural conclusion

Best current genuine Online/DCM model:

    controller current state
        -> FC16 page export
        -> gateway page cache

    gateway desired state
        -> 0708 W1 pending-page bit
        -> controller initiates FC03 page read
        -> gateway returns desired page
        -> controller accepts and republishes page via FC16

This is materially different from injecting a direct Modbus register write as a competing master and is the preferred route for XTR emulation.

## Local validation target

Proposed EXP341, **NOT YET PREPARED / NOT RUN**:

1. Obtain a fresh controller-originated local 03E8/count14 page and cache all 14 words.
2. At a valid local 0708 mailbox point, advertise only the authentic 03E8 desired-page PULL selector with all other fields constrained by evidence.
3. Require exact controller FC03 03E8/count14.
4. Return the exact cached 14-word page unchanged.
5. Capture whether the controller accepts/republishes 03E8.
6. Stop; do not modify any semantic value.

Success would prove the native gateway->controller page-pull transport locally on the XTR without changing a setting. A semantic write remains a later experiment and requires a known current value, one reversible target, explicit rollback and independent confirmation.
