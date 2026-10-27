# PROTO-OFFLINE-20 — canonical reconciliation pending

**Date:** 2026-10-03  
**Reason pending:** GitHub write permission was not granted in the current request.

This file proposes reconciliation only. Historical experiment text should not be deleted or rewritten.

## 1. THERMIA_PROJECT_STATE.md

Add completed offline tracks:

- PROTO-OFFLINE-17 — COMPLETE / POSITIVE — approval accepted and configuration-service ready are separate states; first genuine Eco5 03E8 ACK across six successes at 118.478..120.296 s after bus return.
- PROTO-OFFLINE-18 — COMPLETE / NEGATIVE — no independent captured recurrent bus field predicts page-service readiness before first 03E8 ACK.
- PROTO-OFFLINE-19 — COMPLETE / POSITIVE — six genuine Eco5 sessions show a fixed 32-page ACK-gated autonomous bootstrap through 06F4 before first 0708; later FFFF/867F is a separate 26-page refresh.
- PROTO-OFFLINE-20 — COMPLETE / POSITIVE — register/history audit; stale database/canonical-summary rows identified.

Correct strongest-unknown wording:
- REMOVE `local XTR semantic identity of 042E/042F` from current unknowns.
- RETAIN cross-profile 042E drift as a profile-specific caution.
- Add/retain true unknowns: 03F1/2/3/5, 0431/0432, 0447, EXP383 candidates, 0874/0875, W0/unobserved selectors, 085F semantics/current-alarm bridge, raw 0884 translation, Connect packages, calendar write atomicity.

Current live state remains:
- EXP387 COMPLETE / POSITIVE.
- EXP388 RUNNING / PARTIAL.
- EXP383 PREPARED / NOT RUN.

## 2. EXPERIMENT_LOG.md

Add concise entries for EXP387/388 from already-authoritative PROJECT_STATE + Write Beta v4.1 only:

### EXP387 — delayed 0708 semantic re-arm — COMPLETE / POSITIVE
- delayed 0708 semantic re-arm locally confirmed;
- Room Setpoint semantic write succeeded;
- no further detail should be invented beyond the existing authoritative sources.

### EXP388 — repeated controller-restart recovery hardening — RUNNING / PARTIAL
- repeated controller-restart recovery succeeded twice without ESP reboot;
- pre-semantic and refresh-only controller-loss cancellation branches remain not independently live-exercised;
- do not mark complete.

Then add PROTO-OFFLINE-17/18/19/20 entries without advancing live experiment state.

## 3. PROTOCOL_FINDINGS.md

Correct current top-level OPEN list:
- local 042E/042F semantics are not open.
- local XTR: 042E Hot Water Enabled; 042F Hot Water Mode.
- retain profile drift: the same numeric address 042E has different semantics in ATEC/iTec/public profiles.

Add durable PROTO17–19 findings:
- approval != page-service-ready;
- no observed pre-readiness discriminator;
- 32-page autonomous bootstrap != 26-page mailbox refresh;
- 06F4 is terminal strict-bootstrap page in six genuine Eco5 sessions;
- 047E/0492/04D8/04F6/050A/051E are bootstrap-only in current Eco5 corpus;
- W0 remains unobserved; no genuine desired-selector proof for 0442 or 0546.

## 4. thermia_protocol_semantic_register_map.csv

Apply the rows/deltas in:
`PROTO_OFFLINE_20_REGISTER_DATABASE_DELTA_20261003.csv`

Highest-priority corrections:
- 0424 -> Returnline Temperature Max Limit / STRONGLY SUPPORTED.
- 04A6/04A7 -> SG/operational-state correlation / STRONGLY SUPPORTED, context-qualified.
- 06F4..06F8 + 0701 -> PROVEN mirror relations.
- 0870 -> Compressor Operating Time / STRONGLY SUPPORTED.
- add sparse 0872/73/76/77/78/79 and 087B/C/D runtime semantics.
- add 0884 page-level modern XTR history ABI.
- preserve 03F1/2/3/5 and 0874/0875 as OPEN.

## 5. PROTO-OFFLINE-16 working database

Do not delete it.

Mark it as a historical offline snapshot where its evidence status conflicts with later local live proof. Later experiment evidence upgrades include:
03E9,03EA,03EC,03ED,03EE,03EF,03F0,042E,042F,0442-family proven controls, and 0553.

## 6. History-preservation rule

Do not rewrite old EXP text to make later interpretations appear known earlier.

Add current-status annotations instead:
`DISPROVEN / SUPERSEDED`, `REFINED`, `UPGRADED`, `OPEN`, or `PROVEN`.

Use `PROTO_OFFLINE_20_SUPERSESSION_MATRIX_20261003.csv` as the reconciliation checklist.