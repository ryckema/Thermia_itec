# PROTO-OFFLINE-26 — session/challenge metadata deep pass

**Date:** 2026-10-03  
**Status:** **COMPLETE / POSITIVE** — one new structural challenge property found; several candidate readiness predictors rejected.  
**Hypothesis:** challenge content, challenge cadence or immediately preceding gateway activity may explain why genuine Eco5 approval occurs at challenge #3, challenge #29, or not at all.  
**Controlled change:** offline analysis only; no device TX, YAML change, reboot or setting write.

## Corpus

Both genuine Eco5 + Thermia Online captures:
- 163 exact `071C/0730` challenge requests;
- six successful gateway responses;
- one no-response boot used as negative control.

## Challenge cadence

Across every analysed boot:

- first challenge occurs about +1.0..1.2 s after bus return;
- challenge #3 occurs about +9.79..10.01 s;
- challenge #29 occurs about +119.75..120.13 s;
- normal challenge cadence is ~4.1..4.6 s.

### Strong conclusion

Challenge ordinal is largely a proxy for **elapsed startup time** in this corpus:
- #3 ≈ 10 s;
- #29 ≈ 120 s.

The ordinal itself should not be treated as a semantic controller state.

## New structural finding: challenge bodies are not guaranteed unique

Across 163 challenge requests:

- 162 unique 16-byte bodies;
- one exact duplicate occurs twice consecutively in the final 2026-09-26 boot.

Exact repeated body:

`f6632ebf14c6bc50b33f692485150ed9`

Observed at:

- 710.497 s;
- 714.559 s;

corresponding to challenge ordinals #26 and #27 of that boot.

No gateway response follows either duplicate request.

### Strong conclusion

The 16-byte request field is **not guaranteed to be a fresh unique nonce on every poll**. A cryptographic challenge/nonce interpretation may still be possible, but uniqueness-per-poll is disproven.

This is important for future firmware archaeology: code should be searched for approval/session-token handling without assuming a strict “new random nonce every challenge” design.

## Challenge-content statistics

The challenge bodies otherwise show high diffusion:

- 2026-09-26 consecutive challenge Hamming distance: mean ~64.45 bits, range 0..80 (0 is the exact duplicate);
- 2026-09-28 mean ~64.03 bits, range 49..76;
- successful challenge Hamming weights are 61..67 bits, entirely ordinary for the corpus;
- successful bodies contain no common prefix, fixed byte, zero-byte rule or simple weight class.

### Negative conclusion

No simple challenge-content property distinguishes successful #3/#29 approvals from unanswered challenges.

This agrees with earlier rejection of fixed XOR/hash-like challenge-response transforms.

## Previous gateway activity is not the discriminator

The 2026-09-28 boots are especially useful:

- all four have a last observed gateway `0x0F` response only ~15.6..17.1 s before controller bus return;
- outcomes nevertheless split:
  - #29,
  - #3,
  - #3,
  - #29.

Therefore “gateway was recently active” does not explain early versus late approval.

The 2026-09-26 first successful boot and failed boot are another negative control:

- success #29: previous gateway response gap 35.514 s;
- failed boot: previous gateway response gap 36.283 s.

Those are nearly identical despite opposite outcome.

### Strong conclusion

Recent bus-visible gateway activity before controller reboot is **not sufficient** to predict:
- #3 vs #29 response;
- response vs no response.

## Current best model

The captured bus now supports:

`controller challenge cadence / request body`
does not expose the missing discriminator.

The unknown is still most consistent with a gateway-internal or sideband condition such as:
- internal service readiness;
- registration/cloud state;
- retained binding/session state;
- protocol-package/service initialization;
- another private timer/state not serialized onto the observed RS485 fields.

These remain hypotheses.

## Evidence classification

### Observed
- 163 challenge requests, 162 unique bodies;
- one exact request body repeated on consecutive polls;
- challenge cadence tightly maps #3 to ~10 s and #29 to ~120 s;
- previous gateway-response recency does not separate early/late/failed boots.

### Strong conclusions
1. challenge ordinal is mainly a timing landmark;
2. challenge-body uniqueness per poll is disproven;
3. simple request-content features do not explain approval timing;
4. recent prior gateway activity is not the missing discriminator.

### Unknown
- actual response-generation algorithm;
- actual internal condition selecting #3/#29/no-response;
- whether repeated challenge values reflect cached state, RNG behavior, controller state retention or another mechanism.

## Live status

No change:
- EXP387 COMPLETE / POSITIVE
- EXP388 RUNNING / PARTIAL
