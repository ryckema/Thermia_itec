# PROTO-OFFLINE-42 — Desired-page cache freshness / lifetime

**Date:** 2026-10-03  
**Status:** **COMPLETE / POSITIVE**  
**Scope:** offline evidence analysis only. No bus TX, no YAML change, no live experiment advancement.

## Hypothesis

A genuine Online/DCM gateway can answer a desired-page pull from a bus-visible authoritative same-page image that is substantially older than a few seconds; immediate page refresh is not a universal prerequisite.

## Controlled change

For each fully bracketed desired pull, measure the interval from the most recent controller FC16 publication of the same page to the controller FC03 desired-page pull, then verify that the returned desired image is either that page plus one intended word or an exact no-op.

## Results

| Source | Page | Last same-page FC16 -> desired FC03 | Delta vs cached image | Confirmation |
|---|---|---:|---|---|
| Eco5 20260926 | `03E8/14` | 67.084 s | word12 20 -> 30 | exact FC16 republish |
| Eco5 20260926 | `03E8/14` | 319.512 s | word12 30 -> 20 | exact FC16 republish |
| Eco5 20260926 | `042E/15` | **374.586 s** | word1 1 -> 0 | exact FC16 republish |
| Eco5 20260926 | `042E/15` | 87.609 s | word0 1 -> 0 | exact FC16 republish |
| ATEC/DCM03 20261003 | `0546/20` | 65.425 s | no change | no republish observed |

For every bracketed mutating Eco5 event, the desired image equals the last bus-visible same-page current image with exactly one intended word changed. The longest observed interval is **374.586 s (~6 min 14.6 s)**.

## Conclusion

Genuine Eco5 evidence proves that a same-page controller FC16 image does not have to be immediately recent for a valid desired transaction. The bus-visible cache-lifetime lower bound in the current corpus is at least **374.586 s**.

This does **not** prove that an arbitrary six-minute-old XTR cache is always safe. It proves only that a real gateway used a page with no newer same-page FC16 publication visible on the captured bus for that long. Hidden/internal refresh paths cannot be excluded from offline evidence.

## Production implication

The current emulator's `fresh authoritative page cache` rule is safety-conservative. It should not be relaxed solely from cross-model evidence, but the genuine-gateway data supports treating freshness as a policy/guard parameter rather than a protocol rule requiring a refresh immediately before every desired pull.
