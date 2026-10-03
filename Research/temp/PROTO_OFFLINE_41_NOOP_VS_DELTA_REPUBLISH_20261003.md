# PROTO-OFFLINE-41 — Desired-page no-op versus semantic delta republish

**Date:** 2026-10-03  
**Status:** **COMPLETE / POSITIVE**  
**Scope:** offline evidence analysis only. No bus TX, no YAML change, no live experiment advancement.

## Hypothesis

A controller FC16 republish after a desired-page FC03 pull occurs when the returned desired image differs from the controller's current image; an exact no-op desired image may be accepted without a same-page FC16 republish.

## Controlled change

Baseline: PROTO-OFFLINE-10's four fully bracketed genuine Eco5 desired transactions.  
New evidence: genuine ATEC/DCM03 `W0 bit0 -> FC03 0546/count20` no-op desired pull from the 2026-10-03 cold-start capture.

## Observed mutating Eco5 transactions

1. `03E8/count14`: word12 (`03F4`) 20 -> 30; controller republished exact desired image 0.524 s after DCM response.
2. `03E8/count14`: word12 (`03F4`) 30 -> 20; exact republish after 0.571 s.
3. `042E/count15`: word1 (`042F`) 1 -> 0; exact republish after 0.491 s.
4. `042E/count15`: word0 (`042E`) 1 -> 0; exact republish after 0.491 s.

All four change exactly one word relative to the last same-page controller FC16 image, and all four following controller FC16 images exactly equal the desired image returned by the gateway.

## Genuine ATEC no-op

- Mailbox: `W0=0001 W1=0000 W2=0000 W3=0000 W4=077F W5=0006`.
- Controller pulls `0546/count20` at 111.366 s.
- DCM03 returns exactly the same 20-word image as the controller previously published at 45.941 s.
- `0553=0004` is identical in current and desired images.
- No later controller `FC16 0546/count20` occurs through capture end at 338.043 s: at least 226.677 s of post-pull observation.

## Conclusion

Within the currently bracketed genuine corpus:

- 4/4 semantic-delta desired pulls are followed by exact controller FC16 confirmation/republish;
- 1/1 exact no-op desired pull is not followed by a same-page FC16 republish during >226 s of observation.

This strongly supports treating an absent same-page republish after an exact no-op as normal behavior rather than automatic failure.

This is cross-profile evidence (Eco5 deltas, ATEC no-op), not yet a universal Thermia rule. For a real requested value change, exact FC16 republish remains the strongest confirmation criterion.

## Side observation

Two legacy `03E8/count13` desired pulls exist in `thermia_capture_20260924_210001(1).log`, but they are not bracketed by a same-page controller current image/confirmation in that capture, so they are excluded from the causal comparison.
