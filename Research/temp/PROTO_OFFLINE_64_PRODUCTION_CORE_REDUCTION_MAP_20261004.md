# PROTO-OFFLINE-64 — Production-core reduction / cleanup map

**Date:** 2026-10-04  
**Status:** **COMPLETE / POSITIVE — SAFE REBUILD BOUNDARY DEFINED**  
**Hypothesis:** current v4.1 can be decomposed into proven production core, reusable generic machinery, historical experiment scaffolding and dead state without changing behavior today.  
**Controlled change:** source inventory/classification only. No YAML edit, no TX, no compile/flash.

## Source evidence used

Current v4.1 contains:

- 58 explicit TX sites, all accounted for by PROTO61;
- three highly duplicated semantic engines (`exp378_*`, `exp379_*`, `exp380_*`) plus production 03E8;
- **37** `write_resume_*` references while the source explicitly states normal Thermia Write does not arm that old resume probe;
- dead-looking `write_boot_observation_*` fields with declarations/initialization only;
- `write_request_*` fields with initialization/reset only;
- `write_pending_*` telemetry that is repeatedly cleared/read but has no source assignment making `write_pending_valid=true`;
- several `write_hot_rejoin_*` fields, of which only a subset remains operational;
- large per-page bootstrap one-shot/timestamp duplication;
- parser, passive decoder, writer/session logic and HA presentation inside one very large lambda.

## Recommended target architecture

A future rebuild should have five layers:

1. **RTU stream assembler** — passive framing/CRC only; ambiguity-aware after PROTO63.
2. **Frame decoder + evidence cache** — no TX decisions.
3. **Session/work-state engine** — approval, bootstrap, runtime, recovery/rejoin.
4. **One generic semantic transaction engine** — page schema + current selector + desired selector + allowed words + freshness + exact confirmation.
5. **HA presentation/test packages** — proven controls separated from PREPARED experimental candidates.

## Keep unchanged in the next recovery experiment

For EXP388-R2 specifically, retain behavior for:

- approval/R1;
- full ordered bootstrap;
- current 085F policy;
- current 0870 policy;
- current config ACK policy;
- 0834 capture-only;
- known-good 03E8/042E/0442/0546 production functionality.

This keeps EXP388 a **recovery-only controlled change**.

## Strong cleanup candidates

### Clearly dead / obsolete in current source

- `write_boot_observation_15s_noted`
- `write_boot_observation_complete`
- `write_hot_rejoin_armed`
- `write_hot_rejoin_tx_ms`
- `write_hot_rejoin_challenge_baseline`
- `write_request_*`
- current `write_pending_*` legacy telemetry/state

These should still be removed only with static/compile validation, not by assumption during a live experiment.

### Historical experiment scaffolding

`write_resume_*` / stalled-export `04A6` resume machinery should move out of the production core. The normal writer never arms the branch.

`EXP383` TEST controls remain historically important but **PREPARED / NOT RUN** and belong in a separate experimental package rather than the production semantic core.

### Merge, do not delete

- 32 page-specific bootstrap ACK blocks -> table-driven ordered bootstrap engine;
- per-page ACK booleans/timestamps -> compact index/bitmap + common telemetry;
- four semantic engines -> one schema-driven transaction engine;
- repeated TX direction/write/flush blocks -> one guarded TX primitive;
- repeated numeric state predicates -> enums/helper predicates;
- runtime integrity counters -> one immutable/session integrity snapshot for guard decisions.

## Important non-cleanup

Some apparent complexity is evidence-backed and must not be simplified away:

- `write_delayed_refresh_pending` is semantically meaningful; PROTO57 proves two different forms of state7.
- autonomous runtime 03E8 means config traffic cannot be reduced to W2/W3 ownership alone.
- direct 0870 without 0864 is locally valid.
- both accepted 085F payload forms have local positive evidence.
- `0834` must remain capture-only.

## Interaction with PROTO63

The future parser split should include an ambiguity rule before production cleanup is considered complete.

A valid longer FC03 frame can have an 8-byte CRC-valid prefix interpreted as a semantic request. The present semantic-state guards make this difficult to exploit accidentally, but the parser should ultimately reject/context-disambiguate double-valid candidates rather than selecting the shortest CRC-valid prefix blindly.

## Proposed cleanup order

1. **No cleanup in current EXP388 live test.**
2. Build EXP388-R2 on current behavior, applying only recovery-state restructuring and extra deterministic test instrumentation.
3. After EXP388 completes, create a non-live refactor branch/package:
   - remove verified dead fields;
   - move EXP383/resume experiments out of core;
   - table-drive bootstrap;
   - genericize semantic transactions;
   - split parser/decoder/state/TX layers.
4. Run PROTO54 golden, PROTO60 validator, PROTO61 TX conformance, PROTO62 host decisions and PROTO63 parser tests.
5. Only then consider dedicated 0870 hardening.

## Result

The cleanup target is now explicit enough that a future rewrite does not need to start from a blank sheet and does not need to preserve historical experiment scaffolding accidentally.

No current production functionality was changed.

## Live status

Unchanged: EXP387 COMPLETE / POSITIVE; EXP388 RUNNING / PARTIAL; EXP383 PREPARED / NOT RUN.