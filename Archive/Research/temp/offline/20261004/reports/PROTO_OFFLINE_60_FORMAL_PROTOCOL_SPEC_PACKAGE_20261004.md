# PROTO-OFFLINE-60 — Formal protocol/spec package

**Date:** 2026-10-04  
**Status:** **COMPLETE / POSITIVE**  
**Hypothesis:** the accumulated protocol findings can be represented as one machine-readable deny-by-default model with executable consistency checks, so future implementation work depends on explicit evidence/status rather than scattered assumptions.  
**Controlled change:** documentation/model tooling only. No device TX, no YAML change, no compile/flash.

## Package produced

### Machine-readable model

`THERMIA_PROTOCOL_MODEL_V1_20261004.json`

It formalizes:

- slave `0x0F` transport and FC17 approval gate;
- complete 32-page XTR bootstrap geometry and ACK CRCs;
- runtime page family;
- 0708 W0..W5 model;
- locally/genuinely proven selector provenance;
- desired-state transaction rules;
- state axes and sole-owner invariant;
- ACK-policy evidence for `085F`, `0870`, config pages and `0834`;
- calendar safety boundary;
- profile ABI warning;
- explicit invariants and open questions;
- current live EXP388 partial status.

### Structural schema

`THERMIA_PROTOCOL_MODEL_V1_SCHEMA_20261004.json`

This is intentionally lightweight: it validates package structure, while protocol-specific safety rules live in the executable validator.

### Executable validator

`validate_thermia_protocol_model_v1.py`

Validation result:

```text
THERMIA PROTOCOL MODEL V1: PASS (57 checks)
```

The validator checks:

- exactly 32 unique bootstrap pages indexed 0..31;
- every hard-coded bootstrap ACK CRC;
- desired-selector page-index/word/bit geometry;
- selector uniqueness;
- calendar `055A` not production-authorized;
- local `0834` remains capture-only;
- `0870` recovery qualifier remains explicitly OPEN;
- EXP388 remains RUNNING / PARTIAL;
- PROTO54 golden trace regression still passes;
- PROTO57 has zero reachable multi-owner states;
- PROTO58 `0870` shadow policy still reproduces TP=64, FP=0, TN=31, FN=0.

### Human decision table

`THERMIA_PROTOCOL_MODEL_V1_DECISION_TABLE_20261004.csv`

This gives a compact deny-by-default implementation view without replacing the detailed semantic register map.

## Important model decisions

### Evidence and implementation remain separate

A selector may be locally proven but still not be production-authorized for generalized use.

The clearest example is `W0 bit1 -> 055A`: local calendar work proves the selector on this unit, but the formal model keeps generalized calendar production writing disabled because cross-page atomicity and genuine Online desired behavior remain unresolved.

### Profile-specific behavior remains explicit

The model does not treat same address as same semantic across Thermia generations.

The ATEC/Eco5/XTR ABI split and the `042E` semantic conflict remain first-class warnings.

### ACK permission is contextual

The model no longer equates page recognition with ACK permission.

For `0870`, normal-runtime ownership and recovery/rejoin are separate branches.

For `085F`, both known payload forms remain locally proven, while the universal context predicate remains OPEN.

### State7 is explicitly split

PROTO57 showed that `write_state=7` cannot be modeled as a single re-armable state.

The formal model records that only the EXP387 delayed-refresh substate can re-enter current-page refresh; timeout/runtime-only state7 cannot.

## Evidence classification

**Observed / machine-validated**
- 32-page bootstrap CRC table is internally valid;
- golden trace suite passes;
- reachable state graph has no multi-owner state;
- shadow `0870` architecture reproduces the current genuine reference corpus.

**Strong conclusions**
- the project now has a machine-readable protocol contract suitable for future regression;
- a future writer revision can be checked against explicit safety invariants before live use.

**Still OPEN**
- exact approval challenge algorithm;
- exact local recovery/rejoin `0870` qualifier;
- universal/local `085F` context predicate;
- `0834` local ACK;
- alarm IDs and calendar write atomicity.

## Result

**COMPLETE / POSITIVE.**

This closes the planned offline 57→60 sequence. Further offline work without new captures/binaries is now mostly maintenance/regression rather than high-probability protocol discovery.

## Live status

Unchanged:

- EXP387 — COMPLETE / POSITIVE
- EXP388 — RUNNING / PARTIAL
- EXP383 — PREPARED / NOT RUN