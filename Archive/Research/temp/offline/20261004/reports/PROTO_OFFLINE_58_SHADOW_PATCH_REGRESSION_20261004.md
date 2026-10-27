# PROTO-OFFLINE-58 — Shadow-patch regression

**Date:** 2026-10-04  
**Status:** **COMPLETE / POSITIVE — BOTH HARDENING CONCEPTS REGRESS CLEANLY IN THE OFFLINE MODEL**  
**Hypothesis:** two defensive changes can be modeled without modifying v4.1: (A) a global sole-semantic-owner assertion before selector/desired-page TX, and (B) `0870` ACK permission split into qualified normal runtime OR an explicit recovery/rejoin branch.  
**Controlled change:** shadow-policy only. No YAML modification, no device TX, no compile/flash.

## Shadow patch A — sole semantic owner

Policy:

`before any semantic selector or desired-page response, require that the requesting engine is the only semantic owner in-flight`

Regression:

- PROTO57 reachable semantic graph: **0** reachable multi-owner states;
- therefore the guard blocks **0 known reachable normal transitions**;
- PROTO53 Cartesian conflict cases blocked: **604/604**.

### Conclusion

This hardening is behavior-neutral for the modeled reachable graph and converts the distributed serialization assumption into an explicit local invariant.

It is therefore a low-risk defensive refactor candidate.

## Shadow patch B — `0870` state-qualified ACK architecture

The shadow policy is intentionally architectural, not yet a final implementation predicate:

`ACK 0870 if qualified normal runtime OR explicit recovery/rejoin state owns the transition`

For the genuine reference corpus, normal runtime is approximated by:

`answered 0708 age <= 3 s`

The one already-established legacy reconnect transition ACK is tagged as the explicit recovery/rejoin exception.

Result across **95** genuine `0870/count17` publications:

- genuine ACK preserved (TP): **64**
- genuine unACKed incorrectly ACKed (FP): **0**
- genuine unACKed preserved (TN): **31**
- genuine ACK incorrectly blocked (FN): **0**

So the two-branch architecture exactly reproduces the current 95-event genuine corpus:

**64 ACK / 31 withhold, zero classification errors.**

This does **not** solve how the XTR should detect the recovery branch. It proves only that a runtime+recovery architecture is sufficient to represent all current evidence.

## Local XTR compatibility

The shadow architecture also represents the local evidence from PROTO56:

- EXP310 qualified direct `0870` -> ACK;
- EXP292 sustained runtime `0870` -> ACK;
- EXP309 deliberately unqualified/fail-closed observation -> no automatic ACK.

No `0864` prerequisite is introduced.

## Golden and fault regression

PROTO54 golden suite:

**PASS**

All **72/72** golden assertions remain intact because the shadow patch does not reinterpret capture facts.

PROTO46 synthetic-fault matrix:

- no previously fail-closed scenario becomes more permissive;
- the unqualified `0870` case R06 becomes stricter: generic ACK -> withhold pending qualification;
- semantic stale/wrong/duplicate guards remain unchanged.

## Observed facts

- sole-owner guard rejects all PROTO53 synthetic mixed-owner cases and zero PROTO57 reachable paths;
- runtime+explicit-recovery `0870` architecture can reproduce 64/64 genuine ACKs and 31/31 genuine withholds;
- current local positive `0870` evidence fits the normal-runtime branch;
- no other semantic guard needs weakening.

## Strong conclusions

1. A **global sole-owner assertion** is a safe-looking future defensive refactor in the offline model.
2. `0870` should be represented by at least two ownership modes: **normal runtime** and **recovery/rejoin**.
3. A simple recent-mailbox predicate alone remains insufficient because it misses the genuine reconnect transition ACK.
4. The next unresolved problem is not architecture but the **exact local XTR recovery/rejoin qualifier**.

## Limitations

- the legacy recovery exception is fixture-labelled from genuine capture evidence; the exact online detection predicate is not yet derived;
- this is shadow-model regression, not ESPHome execution;
- no production code changed.

## Live status

Unchanged.