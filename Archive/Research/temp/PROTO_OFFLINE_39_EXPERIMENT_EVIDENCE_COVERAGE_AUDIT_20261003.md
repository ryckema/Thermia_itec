# PROTO-OFFLINE-39 — experiment evidence / coverage audit

**Date:** 2026-10-03  
**Status:** **COMPLETE / POSITIVE**  
**Hypothesis:** the experiment history can be audited without reconstructing missing history, producing a reliable distinction between prepared, partial, result-summary, raw-detail and user-confirmed evidence and a short list of genuinely valuable future live work.  
**Controlled change:** documentation/evidence audit only. No bus TX, YAML change, compile/flash, reboot or setting write.

## Global coverage

Current canonical EXPERIMENT_LOG contains:

- **139 unique numbered experiment IDs**
- earliest documented numbered ID: **EXP92**
- latest: **EXP388**
- **249 numbers absent from the numeric range 1..388**

The absent numbers are **not interpreted as lost experiments**. Numbering may have been unused, documented elsewhere, or predate the current canonical log.

Current unique-status classification:

- HISTORICAL / LEGACY STATUS WORDING: **17**
- COMPLETE / POSITIVE: **80**
- COMPLETE / NEGATIVE: **11**
- RUNNING / PARTIAL: **7**
- PREPARED / NOT RUN: **2**
- COMPLETE / INCONCLUSIVE: **20**
- SUPERSEDED / NOT RUN: **2**

Evidence markers:
- **63** unique IDs have complete-result blocks with raw frame/protocol detail detectable in the canonical log;
- **10** unique IDs explicitly contain user-confirmation wording;
- historical EXP92..107 and EXP134 use older status wording and are preserved rather than rewritten to modern labels.

## Repository-file coverage caution

The repository contains multiple YAML/research files, but experiment number is rarely embedded in the filename. Only a very small subset of experiment IDs can be matched reliably by filename alone.

Therefore:

> absence of `EXP###` in a filename is **not** evidence that the YAML/log did not exist.

The canonical log remains the experiment-history source of truth unless a raw capture/YAML is directly available.

## Highest-value unresolved live work

### Priority 1 — finish EXP388, not a new semantic target

EXP388 remains **RUNNING / PARTIAL**.

Already confirmed:
- repeated controller-restart recovery succeeded twice without ESP reboot.

Still not independently exercised:
- pre-semantic controller-loss cancellation;
- refresh-only controller-loss cancellation.

These are the cleanest remaining live gaps because they test fail-closed recovery behavior rather than a new heat-pump setting.

### Priority 2 — runtime ACK-context hardening evidence

PROTO37 identified a specific production safety debt:

- `085F` known payload is currently enough to permit ACK;
- `0870` is also ACKed by page shape;
- known config pages can be ACKed broadly in runtime.

Before changing those rules, the most useful live evidence is passive/contextual:

- capture W4 + `085F` + `0870` ordering around naturally occurring service/runtime events;
- do not inject a new fault;
- unexpected traffic capture-only.

A future hardened beta can then be regression-tested with the same already-proven semantic target.

### Priority 3 — EXP383 only after protocol-stability work

EXP383 remains **PREPARED / NOT RUN** for seven TEST candidates.

Those controls are not the main protocol-architecture gap and should not be used merely to generate activity.

If resumed later:
- one candidate at a time;
- smallest reversible change;
- fresh authoritative page;
- exact one-word desired page;
- exact controller republish;
- immediate rollback where meaningful.

`0559 Link Integration` remains highest risk and should remain last.

## Evidence-quality conclusion

The project is no longer primarily limited by “unknown registers”.

The important remaining gaps are now:

1. fail-closed recovery branch coverage;
2. runtime ACK permission/context;
3. Connect/DCM serializer artifacts;
4. labelled alarm/current-alarm edges;
5. a small number of unproven semantic settings.

That is a materially better position than simply continuing numeric register exploration.

## Full matrix

`Research/temp/PROTO_OFFLINE_39_EXPERIMENT_COVERAGE_MATRIX_20261003.csv`

contains one row per documented unique experiment ID with:
- normalized status class;
- evidence class;
- raw-detail marker;
- explicit user-confirmation marker;
- directly named repository artifact when discoverable.

## Live status

Unchanged:
- EXP387 COMPLETE / POSITIVE
- EXP388 RUNNING / PARTIAL
- EXP383 PREPARED / NOT RUN
