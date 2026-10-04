# PROTO-OFFLINE-55 — Differential hardening simulation

**Date:** 2026-10-04  
**Status:** **COMPLETE / POSITIVE — 0870 IS THE CLEANEST HARDENING TARGET; SIMPLE 085F/CONFIG RULES OVER-BLOCK GENUINE TRAFFIC**  
**Hypothesis:** candidate stricter ACK policies can be replayed against genuine traffic to measure how much known-good gateway behavior each would preserve or incorrectly block before changing local XTR code.  
**Controlled change:** offline policy simulation only. Current Write Beta v4.1 is not modified.

## Method

For every genuine `085F`, `0870`, and configuration FC16 publication, the simulator reconstructs:

- actual ACK/no-ACK from the capture;
- age of latest answered `0708`;
- latest mailbox W0..W5;
- age of latest ACKed configuration page;
- bootstrap membership;
- recent W2/W3 configuration-work context;
- desired-page confirmation context.

Candidate policies are scored as:

- **TP** — genuine ACK preserved;
- **FP** — candidate would ACK a frame the genuine gateway left unACKed;
- **TN** — genuine withheld ACK preserved;
- **FN** — candidate would block a genuine ACK.

The goal is not to copy another profile blindly; it is to detect obviously over-simple hardening rules.

## 1. `0870`

Current shape-only behavior against the genuine corpus:

- preserves all **64** actual ACKs;
- would also ACK **31** frames genuine gateways left unACKed.

A simple requirement:

`answered 0708 within the previous 3 s`

produces:

- TP = **63**;
- FP = **0**;
- TN = **31**;
- FN = **1**.

So recent-mailbox qualification removes essentially the whole known over-ACK population, but blocks **1** genuine `0870` ACK(s).

Blocked genuine ACK source(s):

legacy_20260925_090550: 1

This is exactly why a future local-XTR rule should be:

`qualified normal runtime OR explicit recovery/rejoin branch`

rather than just `recent 0708`.

### Conclusion

`0870` remains the **best one-variable hardening target** because the genuine negative population is a coherent reconnect state and a simple runtime qualifier has high discriminatory power.

## 2. `085F`

Current known-payload-only behavior:

- genuine ACKs = **20**;
- genuine unACKed population that shape-only would also ACK = **311**.

Candidate `recent config ACK <=3 s`:

- TP = **15**;
- FP = **0**;
- TN = **311**;
- FN = **5**.

Blocked genuine ACKs are distributed across:

legacy_20260925_090209: 1, eco5_20260926: 2, eco5_20260928: 1, atec_20261003: 1

So a simple “only ACK 085F near config activity” rule is **too strict** cross-profile. This matches PROTO45: ATEC and some legacy traffic can legitimately ACK `085F` in steady runtime.

### Conclusion

Do not implement a universal `085F` config/service proximity rule from offline evidence.

## 3. Known configuration pages

Current shape-only policy would ACK all known page shapes, while genuine traffic contains large unACKed populations.

A stricter owner-style candidate:

`bootstrap OR recent W2/W3 work OR desired confirmation`

produces:

- TP = **324**;
- FP = **7**;
- TN = **821**;
- FN = **223**.

The remaining blocked genuine ACKs include profile-specific/overlap cases such as:

eco5_20260928:0683×10, eco5_20260928:06C5×9, eco5_20260928:055A×8, eco5_20260928:06EA×8, eco5_20260928:06F1×8, eco5_20260928:06F4×8, eco5_20260928:06A4×7, eco5_20260928:04A6×6, eco5_20260928:04BA×6, eco5_20260928:0456×6, eco5_20260928:0662×6, eco5_20260926:0683×5

Therefore owner-only ACK logic is also too simple as a universal Thermia rule.

PROTO45 already identified two standalone legacy `03E8` pushes and config activity overlapping approval retries; this simulation quantifies the consequence.

## Observed facts

- recent answered-mailbox context has strong discriminatory value for `0870`;
- config proximity is insufficient as a universal `085F` qualifier;
- bootstrap/W2W3/desired ownership captures much, but not all, genuine config ACK behavior;
- cross-profile differences are material enough that local XTR policy must be validated locally.

## Strong conclusions

1. **0870 should be the first ACK class considered for a bounded local hardening experiment.**
2. `085F` should not be tightened using a single generic “near config/service” predicate.
3. generic config-page hardening needs at least one additional autonomous/retained-push state if it is ever generalized.
4. Differential replay should become a gate for future ACK-policy changes: a new policy should state explicitly which genuine references it intentionally ceases to emulate.

## Safety consequence

No production policy is changed by this experiment.

A future `0870` experiment should change only the qualification predicate, preserve all semantic-write guards, leave `0834` capture-only, and have a rollback to v4.1.

## Live status

Unchanged.