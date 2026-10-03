# PROTO-OFFLINE-22 — Canonical reconciliation

**Date:** 2026-10-03  
**Status:** **COMPLETE / POSITIVE**  
**Hypothesis:** PROTO-OFFLINE-17..21 and later local evidence can be folded into canonical project state without rewriting historical observations or advancing the live experiment.  
**Controlled change:** documentation/database reconciliation only. No device TX, YAML change, restart or semantic write.

## Result

Canonical state, experiment log and durable findings now include PROTO-OFFLINE-17 through -21 plus this reconciliation. EXP387/EXP388 entries are restored at the top of the experiment log using only already-authoritative state. The semantic register map has been corrected for durable PROTO20 deltas including 0424, 04A6/04A7, the 06F4 mirror structure, 0870, sparse operating-time/defrost rows and 0884 history.

## Evidence discipline

- historical text below the new authoritative overlays is preserved;
- no missing older experiment numbers are reconstructed;
- cross-model semantics remain labelled as such;
- genuine-selector evidence is kept distinct from local XTR write-path evidence;
- EXP388 remains **RUNNING / PARTIAL**.

## Canonical files changed

- `Research/THERMIA_PROJECT_STATE.md`
- `Research/EXPERIMENT_LOG.md`
- `Research/PROTOCOL_FINDINGS.md`
- `Research/protocol reduction/thermia_protocol_semantic_register_map.csv`

## Live status

No change:
- EXP387 COMPLETE / POSITIVE
- EXP388 RUNNING / PARTIAL
- EXP383 PREPARED / NOT RUN
