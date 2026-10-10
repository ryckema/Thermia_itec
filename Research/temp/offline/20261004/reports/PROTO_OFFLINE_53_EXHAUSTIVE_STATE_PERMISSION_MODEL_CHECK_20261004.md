# PROTO-OFFLINE-53 — Exhaustive state/permission model-check

**Date:** 2026-10-04  
**Status:** **COMPLETE / POSITIVE WITH DEFENSIVE-INVARIANT DEBT IDENTIFIED**  
**Hypothesis:** exhaustive enumeration of the runtime semantic-engine state space will show whether Write Beta v4.1 can emit semantic TX from an unexpected state combination, and whether its fail-closed behavior depends on implicit cross-engine invariants.  
**Controlled change:** offline-only Cartesian state enumeration. No bus TX, no YAML change, no compile/flash.

## Baseline

Current Write Beta v4.1 runtime logic, GitHub blob:

`8e8a82689e53528a8b751a1abbd901f683b6b238`

The model covers the stage40 decision surfaces for:

- production `03E8` write engine;
- EXP378 / `042E`;
- EXP379 / `0442`;
- EXP380/383 / `0546`;
- controller FC03 desired pulls;
- controller `0708` mailbox polls;
- >=5 s controller-loss recovery predicate;
- generic FC16 ACK permission classes.

It is a **source-faithful abstract shadow model**, not compiled ESPHome execution.

## Exhaustive space

Enumerated:

- `write_write_state = 0..8`;
- `exp378_state = 0..7`;
- `exp379_state = 0..7`;
- `exp380_state = 0..7`.

Total runtime state tuples:

**4,608**

Each tuple was tested against:

- four known desired-page FC03 shapes + one unexpected FC03 class;
- one `0708` arbitration event;
- controller-loss recovery;
- seven runtime FC16 permission classes.

Total decision rows:

**64,512**

## Result 1 — selector arbitration also relies on cross-engine state invariants

Healthy-guard `0708` arbitration produces:

- **148** semantic-selector decisions with no other semantic engine already in an in-flight state;
- **276** Cartesian state combinations where a semantic selector would still be emitted while another engine is already marked semantically in-flight.

The largest conflict class is the production `03E8` selector falling through while EXP378/379/380 are already in an in-flight state. Smaller asymmetric cases also exist for EXP378 and EXP379.

These combinations are **not known reachable through the normal state transitions**. They expose the same architectural pattern as the FC03 response analysis below: arbitration relies partly on upstream invariants instead of one global `sole semantic owner` guard.

This is defensive hardening debt, not evidence that the current live writer has actually entered such a state.

## Result 2 — desired-page response branches rely partly on cross-engine state invariants

FC03 desired-page handling produces:

- **268** semantic responses with no conflicting semantic-inflight engine;
- **328** Cartesian state combinations where the local page branch would still authorize a semantic response while another semantic engine is already marked in-flight.

These conflict combinations are not known reachable through the normal UI/state transitions. They appear because some FC03 page handlers validate their own engine plus selected peer guards, rather than asserting a single global rule such as:

`exactly one semantic owner may be in-flight`.

The asymmetric guard pattern is:

- `0546` is strongest: it requires main engine idle and both earlier experimental engines idle/disabled;
- `0442` guards main + EXP378, but not EXP380;
- `042E` guards main, but not EXP379/EXP380;
- production `03E8` validates its own state/cache/budget but does not explicitly assert EXP378/379/380 semantic-idle.

### Interpretation

This is **defensive-invariant debt**, not evidence of a demonstrated live bug.

Normal transition guards appear to prevent these mixed semantic states from being created. But if state became inconsistent because of a future code change, recovery edge, or latent bug, the desired-page handlers do not all independently fail closed.

A future refactor could cheaply harden this with one global semantic-owner invariant before any full-page desired response.

## Result 3 — controller-loss recovery remains conservative

Across all 4,608 combinations:

- **1,296** are classified recoverable: intent/cache cancellation + cold-start re-entry;
- **3,312** refuse recovery because at least one semantic engine is beyond the safe boundary.

No semantic-inflight state is classified recoverable by the modeled predicate.

This independently supports the EXP388 recovery design, but does **not** complete EXP388 without live logs.

## Result 4 — broad FC16 ACK classes are orthogonal to semantic-engine state

In current stage40 code, the generic ACK decision for:

- known `085F`,
- `0870/count17`,
- known `local_config` page,

does not depend on the four semantic-engine states.

Therefore each of those ACK classes remains permitted throughout the Cartesian semantic state space, subject to its special page-specific branches.

This does **not** inject setting values, but it confirms that ACK authorization and semantic ownership are currently separate mechanisms.

PROTO45/46 already showed why changing those policies requires profile-specific care.

## Observed facts

- the current `0708` selector arbitration does not create double-semantic-selector combinations in the modeled healthy-guard path;
- semantic FC03 response guards are asymmetric across the four engines;
- the recovery predicate refuses all modeled semantic-inflight states;
- generic `085F`, `0870`, and known-config ACK permission is independent of semantic-engine ownership.

## Strong conclusions

1. The highest-value new hardening idea is **not another page-specific rule**, but a global invariant:
   `before any semantic selector OR full-page desired response, assert that this engine is the sole semantic owner`.
2. Both the `0708` selector dispatcher and several FC03 desired-page handlers rely partly on upstream cross-engine invariants.
3. The conflicting Cartesian combinations are not known reachable through current normal transitions, so this is **defensive-invariant debt**, not a proven live defect.
4. EXP388's recovery-state partition remains internally coherent.
5. ACK-policy debt remains separate from semantic-value TX safety.

## Unknowns / limitations

- Cartesian states include combinations that may be impossible to reach through normal code.
- This is not compiler/runtime verification.
- The abstract model intentionally does not reproduce millisecond timing/race behavior.
- It does not prove memory corruption resilience.

## Live state

Unchanged:

- EXP387 — COMPLETE / POSITIVE
- EXP388 — RUNNING / PARTIAL
- EXP383 — PREPARED / NOT RUN