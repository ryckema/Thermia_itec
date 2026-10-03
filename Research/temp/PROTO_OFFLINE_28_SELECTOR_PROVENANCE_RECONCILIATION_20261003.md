> **Current-status refinement — ATEC-COLDSTART-01 (2026-10-03).** A later genuine ATEC + classic DCM03 cold-start capture proves `W0 bit0 -> FC03 0546/count20`. Therefore the historical statement below that genuine W0 had never been observed non-zero is corpus-scoped to the earlier six reference captures. Current provenance is: `0546/W0b0` = genuine ATEC/DCM03 + local XTR proven; genuine Eco5 W0 remains unobserved. Other W0 bits remain unproven unless separately evidenced.

# PROTO-OFFLINE-28 — desired-selector provenance reconciliation

**Date:** 2026-10-03  
**Status:** **COMPLETE / POSITIVE**  
**Hypothesis:** the selector database currently over-compresses three different evidence types — genuine Online/Eco5 selector observations, locally proven XTR selector behavior, and symmetry-only extrapolation — and can be made safer by separating them explicitly.  
**Controlled change:** offline provenance/database reconciliation only. No bus TX, YAML change, reboot or setting write.

## Result

The page-index geometry remains valid, but **desired-state selector proof is not uniform across all 32 pages**.

### Genuine Online/Eco5 desired selectors actually observed

Only:

- `W1 bit0 -> 03E8`
- `W1 bit3 -> 042E`

have genuine-capture desired-pull evidence in the current corpus.

Across the genuine reference corpus, `W0` has never been observed non-zero.

### Locally proven XTR selectors beyond the genuine desired corpus

The local XTR experiments independently prove additional selector paths:

- `03E8`: current `W3 bit0`, desired `W1 bit0`
- `042E`: current `W3 bit3`, desired `W1 bit3`
- `0442`: current `W3 bit4`, desired `W1 bit4` — EXP379 successful cooling writes
- `0546`: current `W2 bit0`, desired `W0 bit0` — EXP380 successful Operation Mode write
- `055A`: local calendar edit produced `W0=0002/W2=0002`, controller `FC03 055A/count33`, then exact FC16 republish

This means **W0 is locally proven on this XTR M**, but **not proven in genuine Eco5 Online captures**. These two provenance statements are compatible and must remain separate.

## Important correction

The earlier selector CSV used the same evidence wording for all 32 rows and could be read as if every desired bit was already established. That is unsafe.

The revised database now keeps:
- current/PUSH bitmap evidence;
- desired/PULL evidence;
- local XTR experiment provenance;

as separate columns.

## Safe selector classes

### Class A — genuine + local desired proof
- `03E8 / W1 bit0`
- `042E / W1 bit3`

### Class B — local XTR desired proof, not genuine-Eco desired proof
- `0442 / W1 bit4`
- `0546 / W0 bit0`
- `055A / W0 bit1`

### Class C — geometry only
All remaining desired bits.

Do not transmit Class C desired selectors merely because the 32-page current bitmap is symmetric.

## Strong conclusion

The 32-page page-index geometry is a strong structural model, but **current-state bitmap proof and desired-state selector proof are different evidence dimensions**.

The selector matrix has been corrected accordingly.

## Live status

No change:
- EXP387 COMPLETE / POSITIVE
- EXP388 RUNNING / PARTIAL
