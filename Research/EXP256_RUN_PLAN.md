# EXP256 — One-shot R1 + full post-R1 FC16/FC03 differential census

**Status:** PREPARED / NOT RUN

## Hypothesis

The already-tested one-shot R1 response changes the local XTR's native FC16 distribution. The
leading EXP255-derived hypothesis is selective suppression of `085F/count5`, while
`04A6/count13` continues.

## Known active value

Exactly the same one-shot response used in EXP252:

```text
R1 = 1691 A5F3 F8E8 D587 3892 4416 E8E6 A3D5
frame = 0F 17 10 1691A5F3F8E8D58738924416E8E6A3D5 E227
```

No new write target or value is introduced.

## Procedure

1. Flash `thermia_itec_xtr_m_waveshare_exp256.yaml`.
2. Wait >=15 s with healthy normal bus traffic.
3. HA -> Configuration -> **EXP256 Arm One-shot R1 + FC Census**.
4. Within 60 s power-cycle only the Thermia controller.
5. Do not change Thermia settings.
6. Wait for `SUMMARY COMPLETE` (~7 min after BUS_RETURN).
7. **After the summary**, reboot the Thermia controller once. The previous R1 run showed a
   recoverable DHW-side `0` / `COMM. ERR ONLINE/LINK`; this experiment does not need to wait for the
   alarm.
8. Return the full log from ARM through SUMMARY and note whether the DHW-side `0` reappeared.

## What changes from EXP252

Instrumentation only:
- every `0x0F FC16` request now logs start/count/timing;
- every `0x0F FC03` request now logs start/count/timing.

The one-shot value, exact first-approval trigger, RTC/service checks, controller-state guard,
parser/drop guards, peer-response guard and TX latch behavior are unchanged.

## What is NOT sent

- no FC16 ACK;
- no FC03 response;
- no second FC17 response;
- no mailbox response;
- no desired-state page response.

## Primary discriminator

EXP255 baseline:

```text
04BA/count22 = 4
04A6/count13 = 383
085F/count5  = 195
total FC16    = 582
FC03          = 0
```

EXP252 one-shot-R1 total was 386 FC16 requests.

If EXP256 shows `085F/count5` disappearing after R1 while `04A6/count13` remains, the count
differential is explained and the next experiment can target the meaning of that transition rather
than guessing a DCM reference sequence.