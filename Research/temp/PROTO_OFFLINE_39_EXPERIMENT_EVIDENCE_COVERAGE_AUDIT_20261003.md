# PROTO-OFFLINE-39 — experiment evidence / coverage audit

**Date:** 2026-10-03  
**Status:** **COMPLETE / POSITIVE** — the experiment ledger is now auditable without reconstructing missing history.  
**Hypothesis:** the canonical experiment log can be reduced into a provenance/coverage ledger that separates present records, missing numbering, embedded raw evidence, user confirmation and current live gaps.  
**Controlled change:** documentation/evidence audit only. No bus TX, YAML behavior change, reboot or setting write.

## Scope

The audit uses the **newest record for each numeric EXP identifier** in the current canonical `Research/EXPERIMENT_LOG.md`.

Important limitation:

> “summary-only in canonical log” does **not** mean no raw log ever existed in chat or an earlier upload. It means the current canonical experiment block itself does not embed a raw frame/timestamp excerpt or explicit user-confirmation marker.

No missing experiment is reconstructed from memory.

## Ledger coverage

Current canonical log contains:

- **139 unique numeric EXP IDs**
- earliest recorded numeric ID: **EXP92**
- latest recorded numeric ID: **EXP388**
- **249 numeric IDs from 1..388 have no canonical experiment header**

Missing ranges:

`1-91, 108-129, 142-255, 265, 271-286, 341-342, 354, 384-385`

These gaps are preserved as gaps. They must not be backfilled merely to make numbering continuous.

## Current-header status normalization

Newest-record classification:

```
COMPLETE / POSITIVE          66
COMPLETE / NEGATIVE          11
COMPLETE / INCONCLUSIVE      31
RUNNING / PARTIAL            4
PREPARED / NOT RUN           3
SUPERSEDED / NOT RUN         3
PREPARED / LEGACY WORDING    12
LEGACY / UNCLASSIFIED        9
```

The noncanonical legacy wording is retained rather than silently rewritten.

## Evidence retained directly in the canonical log

Automated conservative markers find:

- **27/139** newest experiment blocks with raw-frame or timestamp excerpts;
- **15/139** with explicit user-confirmation/report markers;
- **8/139** containing both a controlled-change marker and an exact-republish/byte-exact causal marker;
- only **2** current numeric experiments have an experiment-specific repository artifact discoverable by filename/path in the present tree: EXP296, EXP382.

This last figure is deliberately narrow. The production Write Beta YAML contains many later experiment implementations internally, but it is not counted as a separate per-experiment source file.

## Historical duplicate headers

Many experiment numbers intentionally have both PREPARED and RESULT-era headers in the append-only history.

That is not treated as corruption. The audit chooses the newest occurrence for the ledger while preserving all older text.

Examples include EXP137–141, EXP258–264, EXP331, EXP356, EXP358, EXP374 and EXP380.

## Current live/open interpretation

The top canonical state remains authoritative:

- **EXP387 — COMPLETE / POSITIVE**
- **EXP388 — RUNNING / PARTIAL**
- **EXP383 — PREPARED / NOT RUN**

Older entries such as EXP373 and EXP376 still have historical `RUNNING / PARTIAL` headers, but substantial downstream experiments subsequently exercised/promoted many of their subtargets. They are **historical partial records**, not additional active live-experiment slots competing with EXP388.

## Highest-value future live gaps identified by the audit

### 1. Finish EXP388
Still missing independent live exercise of:
- pre-semantic controller-loss cancellation;
- refresh-only controller-loss cancellation.

This is the only current active live experiment.

### 2. Scheduler-qualified runtime ACK hardening
PROTO-OFFLINE-37 found a bounded production hardening candidate:

known config-page shape can contribute to runtime ACK permission outside explicit export-resume state.

A future live regression could tighten this to scheduler/session-qualified permission while preserving the known-good production path.

This is **not yet an experiment number** and is not promoted ahead of EXP388.

### 3. EXP383 candidate semantics
The seven TEST controls remain explicitly PREPARED / NOT RUN. Their page transport/selector machinery may now be better understood, but that does not prove the individual semantics.

They should remain one-at-a-time only if the user later chooses to resume live semantic mapping.

## Strong conclusions

1. The canonical experiment history is intentionally incomplete as a numeric sequence; continuity must not be manufactured.
2. Current state must be read from the top canonical overlay, not from old partial/prepared headers deeper in the history.
3. The main remaining live-protocol gap is EXP388 branch coverage, not another broad register scan.
4. The next production-hardening question is ACK permission qualification, but changing it requires live regression.
5. EXP383 remains a semantic-candidate queue, not proven functionality.

## Deliverable

`Research/temp/PROTO_OFFLINE_39_EXPERIMENT_COVERAGE_LEDGER_20261003.csv`

contains one row per present numeric experiment using the newest canonical record.

## Live status

Unchanged:
- EXP387 COMPLETE / POSITIVE
- EXP388 RUNNING / PARTIAL
- EXP383 PREPARED / NOT RUN
