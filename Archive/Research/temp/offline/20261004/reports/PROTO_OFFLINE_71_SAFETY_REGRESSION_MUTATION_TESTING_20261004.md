# PROTO-OFFLINE-71 — Safety regression mutation testing

**Date:** 2026-10-04  
**Status:** **COMPLETE / POSITIVE — 19/19 TARGETED SAFETY MUTANTS KILLED**  
**Hypothesis:** the accumulated offline regression contract should detect deliberate mutations that weaken proven safety invariants or contradict locally proven behavior.  
**Controlled change:** mutation testing of an offline policy/decision contract only. No production YAML edit, no firmware compile/flash, no bus TX.

## Baseline gates

Before mutation testing:

- PROTO54 golden trace regression: **PASS**
- PROTO60 formal model validator: **PASS (57 checks)**
- compact mutation-test baseline: **20/20 assertions PASS**

## Mutants

**19** deliberate single-variable mutants were injected one at a time.

Mutation classes included:

- ACKing `0834`;
- ACKing unknown runtime or unknown `085F`;
- removing either locally proven `085F` payload;
- authorizing unproven 03E8 word indices;
- relaxing page-cache freshness;
- allowing a second semantic response;
- allowing recovery after semantic-boundary states;
- collapsing the state7 delayed-rearm substate;
- removing sole semantic ownership;
- requiring `0864` before all `0870`;
- promoting calendar `055A` to production;
- allowing multi-word semantic deltas;
- allowing a second bus-loss recovery;
- permitting semantic interpretation before complete-frame finalization;
- dropping bootstrap ACK CRC enforcement;
- permitting an unproven desired selector.

## Result

- mutants: **19**
- killed: **19**
- survived: **0**
- mutation score: **100.0%**

Survivors: **none**

## What this proves

For these explicitly targeted failure classes, the current **offline safety specification** contains at least one assertion that would fail if the rule were weakened.

That materially reduces the chance that a future cleanup silently:

- broadens ACK behavior;
- loses semantic freshness/budget guards;
- crosses recovery boundaries;
- collapses state7 semantics;
- breaks direct local 0870 behavior;
- promotes calendar writes;
- reintroduces prefix-before-frame semantic interpretation.

## What this does not prove

This is **not source-code mutation of the generated ESPHome binary**.

The mutant harness modifies a compact policy model representing the known invariants. Therefore:

- it tests the strength of the regression **specification**;
- it does not prove every equivalent C++ coding mistake would be caught;
- it does not replace compile-time/static analysis or live regression.

A later source-level mutation framework would require generating/compiling many modified C++/YAML variants, which is unnecessary before the core is actually rewritten.

## Strong conclusion

The current offline regression package is strong enough to act as a **refactor gate for the safety properties we explicitly know about**.

The major remaining blind spot is no longer an obvious missing invariant; it is implementation integration: whether future generated C++ faithfully enforces those invariants.

## Live status

Unchanged.