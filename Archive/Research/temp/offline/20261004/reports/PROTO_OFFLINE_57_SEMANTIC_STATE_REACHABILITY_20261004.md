# PROTO-OFFLINE-57 — Reachability analysis of PROTO53 semantic conflicts

**Date:** 2026-10-04  
**Status:** **COMPLETE / POSITIVE — PROTO53 CONFLICT STATES ARE UNREACHABLE IN THE MODELED CURRENT SEMANTIC TRANSITION GRAPH**  
**Hypothesis:** PROTO53's Cartesian mixed-semantic combinations are defensive-invariant debt rather than states reachable through current v4.1 semantic dispatch/progression/recovery transitions.  
**Controlled change:** forward reachability replaces Cartesian enumeration. No TX, no YAML change, no compile/flash.

## Baseline

Write Beta v4.1 blob `8e8a82689e53528a8b751a1abbd901f683b6b238`.

The model follows current source guards for main `03E8`, EXP378/`042E`, EXP379/`0442`, EXP380/`0546`, dirty dispatch, current refresh, selectors, desired responses, confirmation exits, timeouts, EXP387 delayed re-arm, and EXP388 cancellation/recovery.

A required refinement versus the first rough model is explicit tracking of `write_delayed_refresh_pending`: **state7 is not one state semantically**. Only EXP387's parked states may re-arm current-page refresh; state7 reached through refresh/autosync failure is runtime-only and cannot transition back to semantic work.

Dedicated Configuration autosync (`write_state=8`) is outside this semantic-capable graph because it never enters selected-word logic. Its controller-page response returns directly to state0, while its timeout produces state7 with delayed re-arm false.

## Roots

- normal semantic-capable runtime: `(0,0,0,0)`;
- post-controller-restart re-synchronization: `(0,7,7,7)`.

## Result

Forward exploration reaches **115 distinct semantic-capable state variants** (including the delayed-rearm flag).

- reachable nodes with more than one semantic owner in-flight: **0**
- PROTO53 Cartesian conflict tuples reachable after projection to the four engine states: **0**
- reachable pre-event states that could emit a selector or desired response while another semantic owner is already in-flight: **0**

## Why

All four dirty dispatchers require peer engines to be idle/disabled before latching an active transaction. Once one engine is active, peers may retain UI intent in dirty flags but cannot latch their own semantic state.

The experimental current-refresh branches also only advance from startup/queued states when their `refresh_ok` guards succeed. A failed guard leaves the engine waiting and emits only an idle response; it does not advance to selector state.

EXP388 recovery cancels every safe pre-semantic intent and resets all experimental engines to state7 before re-synchronization.

## Refinement of PROTO53

PROTO53 remains useful: individual selector/FC03 handlers do not all restate a universal peer-owner assertion.

PROTO57 now shows that the risky Cartesian combinations are **not reachable through the modeled current transition graph**.

Classification:

**STRONGLY SUPPORTED defensive-invariant debt; no demonstrated double-semantic-TX bug.**

A global `sole semantic owner` assertion remains attractive future hardening because it centralizes a safety property that is currently distributed over multiple dispatch guards.

## Limitations

This is an abstract source model, not compiled ESPHome execution. It does not test memory corruption, ISR scheduling, compiler behavior or future refactors. It also intentionally excludes the non-semantic Configuration-autosync subgraph from semantic-owner reachability.

## Live status

Unchanged: EXP387 COMPLETE / POSITIVE; EXP388 RUNNING / PARTIAL; EXP383 PREPARED / NOT RUN.