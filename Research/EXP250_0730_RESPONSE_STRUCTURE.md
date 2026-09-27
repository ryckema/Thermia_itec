# EXP250 — Offline 0730..0737 response-structure classification

**Status:** COMPLETE / OFFLINE / NO TX

## Hypothesis

The two externally reported genuine Eco 5 `0730..0737` blocks behave more like one opaque 128-bit approval/authenticator response than eight independent status/control words.

## Source responses

```text
R1 1691 A5F3 F8E8 D587 3892 4416 E8E6 A3D5
R2 FD63 6CCD 0F92 1D83 FF23 2A1A 2413 B372
```

## Observed facts

- all 8/8 response word positions change;
- no response word position is fixed;
- no common small Thermia status/control constants occur;
- C1→R1 Hamming distance = 65/128;
- C2→R2 Hamming distance = 62/128;
- R1→R2 Hamming distance = 68/128.

## Strong conclusion

For emulator design, `0730..0737` should currently be treated as one **opaque 16-byte response blob**.

There is no evidence-backed per-word semantic map.

## Hypotheses

A keyed/nonlinear authenticator remains compatible with the data. A tightly packed or obfuscated structured message cannot be excluded.

## Unknowns

- exact algorithm/key/state;
- installation- or gateway-specific material;
- repeated-challenge determinism;
- whether XTR M uses the same response function as the reported Eco 5.

## Safety

This experiment was offline only. No TX occurred.

The result does not make arbitrary replay safe and does not approve an active XTR `0730` response.
