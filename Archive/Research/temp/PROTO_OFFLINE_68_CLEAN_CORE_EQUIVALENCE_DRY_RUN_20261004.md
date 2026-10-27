# PROTO-OFFLINE-68 — Production-core cleanup equivalence dry-run

**Date:** 2026-10-04  
**Status:** **COMPLETE / POSITIVE — SCHEMA/TABLE-DRIVEN CORE CAN PRESERVE CURRENT BEHAVIOR OFFLINE**  
**Hypothesis:** the structural cleanup proposed by PROTO64 can be represented as a smaller table/schema-driven host architecture without changing current v4.1 protocol decisions.  
**Controlled change:** offline reference architecture only. No YAML edit, no bus TX, no compile/flash.

## Candidate clean-core architecture

The dry-run replaces repeated logic conceptually with:

1. one table for the 32 bootstrap/config page shapes;
2. one semantic-page schema for `03E8`, `042E`, `0442`, and `0546`;
3. one generic desired-page authorization function;
4. one ordered mailbox/0708 engine table for 042E -> 0442 -> 0546 followed by production 03E8;
5. named recovery-safe state sets instead of repeated magic-number predicates;
6. one ACK table with the **current** special-case ordering retained.

No `0870`, `085F`, config-ACK, or parser hardening is mixed into this equivalence test.

## Exhaustive equivalence result

Current source-transcribed v4.1 behavior and the clean-core candidate were compared across:

- all 4,608 combinations of the four semantic engine states;
- desired-page cache-valid/freshness boundary classes;
- semantic response-budget boundaries;
- authorized and unauthorized word-index classes;
- production dirty-state guards;
- runtime qualification and age boundaries;
- delayed-refresh and config-autosync conditions;
- all EXP388 recovery-state combinations;
- all known config/runtime ACK shapes plus special 04A6/0834/085F/hot-rejoin contexts.

Decision comparisons executed:

**13358496**

Differences:

**0**

## Bootstrap / formal-model gate

- bootstrap page/count entries: **32/32 match**
- hard-coded bootstrap ACK CRCs: **32/32 valid**
- PROTO54 golden regression: **PASS**
- PROTO60 formal model validator: **PASS**

## What can safely be merged conceptually

Offline equivalence now supports later refactoring of:

- 32 page-specific bootstrap ACK branches -> one ordered table-driven bootstrap;
- four duplicated semantic page handlers -> one schema-driven semantic transaction engine;
- repeated recovery state-set predicates -> named helpers/enums;
- repeated ACK page recognition -> table lookup with existing special-case ordering.

## What must remain separate

### Parser hardening

PROTO63/66/67 changes framing semantics. It is **not** part of this cleanup-equivalence proof.

A future parser revision should be a separate controlled change using frame-gap finalization.

### ACK hardening

The clean-core candidate deliberately preserves today's broader v4.1 behavior for:

- known `085F`;
- `0870/count17`;
- generic known config pages.

Those are separate future protocol experiments, not cleanup.

### EXP388

Recovery semantics are preserved exactly in this host equivalence pass. EXP388-R2 can use this architecture later, but its live cancellation branches still need their own result.

## Cleanup significance

PROTO64 identified dead/historical fields that can eventually be removed. PROTO68 now shows that the **active protocol decision core does not require the current copy/paste structure**.

That makes a future v4.2-style rewrite substantially lower risk:

`same decisions first -> live regression -> only then separate hardening changes`.

## Strong conclusion

A clean, schema-driven production core is feasible without changing current protocol behavior.

The safe ordering for future development is therefore:

1. structural equivalence refactor;
2. offline regression;
3. live equivalence confirmation;
4. only afterward parser and ACK hardening as separate experiments.

## Live status

Unchanged: EXP387 COMPLETE / POSITIVE; EXP388 RUNNING / PARTIAL; EXP383 PREPARED / NOT RUN.
