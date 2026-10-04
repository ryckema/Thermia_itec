## Follow-up offline reductions — PROTO-OFFLINE-69..72

Added on 2026-10-04:

- PROTO69: RTU timing / UART callback feasibility audit
- PROTO70: standalone compiled C++ parser harness + output
- PROTO71: targeted safety-regression mutation testing
- PROTO72: dead-code / state-liveness proof
- `tools/thermia_v41_cpp_parser_harness.cpp`: source-faithful standalone parser harness
- `CANONICAL_UPDATE_PENDING_PROTO69_72_20261004.md`: pending canonical reconciliation notes

Key results:
- PROTO69: at 9600 8E1 the remaining 1–2 bytes of a contiguous 9/10-byte frame arrive within ~1.15–2.29 ms, shorter than the configured 5 ms UART-debug idle timeout; the split-prefix ambiguity is therefore physically unlikely for normal contiguous short RTU frames.
- PROTO70: standalone C++17 parser replayed 25,031 genuine frames exactly across 50 randomized-chunk full runs and reproduced all deliberate 042E/0442/0546 shortest-prefix ambiguities.
- PROTO71: 19/19 targeted safety mutants killed (100% for the tested invariant set).
- PROTO72: 12 definite write-only globals identified; old `write_resume_*` / 04A6 resume and historical hot-rejoin branches are source-unreachable in current v4.1. Current EXP388 recovery remains separate and live.

These are offline results only. No Write Beta behavior changed and EXP388 remains **RUNNING / PARTIAL**.

---

## Follow-up offline reductions — PROTO-OFFLINE-65..68

Added on 2026-10-04:

- PROTO65: exhaustive genuine-corpus parser ambiguity scan + per-capture summary/details/type distribution
- PROTO66: parser-fix shadow tournament against genuine and adversarial double-valid frames
- PROTO67: parser + semantic-state end-to-end adversarial replay + gap-aware genuine replay
- PROTO68: clean-core structural equivalence dry-run + equivalence matrix
- `tools/thermia_clean_core_v0_reference.py`: architecture/reference note for the PROTO68 clean-core design
- `CANONICAL_UPDATE_PENDING_PROTO65_68_20261004.md`: pending canonical reconciliation notes

Key results:
- PROTO65 scanned **25,031 genuine CRC-valid Online/DCM frames** and found **0 double-valid parser candidates** and **0 genuine semantic-prefix collisions**.
- PROTO66 refined the parser fix: merely preferring shortest/longest or rejecting only already-complete ambiguities is insufficient under arbitrary chunk splitting; robust handling needs frame-gap/context-aware deferral.
- PROTO67 demonstrates the synthetic risk end-to-end: in 50,000 adversarial parser+semantic cases, the current shortest-prefix strategy can cross the setting-bearing TX boundary in matching-owner split-prefix states, while frame-gap finalization reduced tested ambiguous-prefix setting TX decisions to **0** and preserved **140/140** genuine replay runs plus **4/4** legitimate semantic request controls.
- PROTO68 proves structural cleanup can preserve current behavior offline: **13,358,496** current-v4.1 vs schema/table-driven decision comparisons, **0 differences**; PROTO54 and PROTO60 gates remain PASS.

These remain offline results. No Write Beta YAML behavior was changed and EXP388 remains **RUNNING / PARTIAL**.

---

## Follow-up offline reductions — PROTO-OFFLINE-61..64

Added/reconciled on 2026-10-04:

- PROTO61: model-to-code TX conformance audit + route matrix
- PROTO62: source-transcribed host decision-engine regression + 4630-check matrix
- PROTO63: stream-parser/resynchronization fuzzing + fuzz summary + parser ambiguity matrix
- PROTO64: production-core reduction/cleanup map

Key new durable finding from this block: the current shortest-first parser can accept an 8-byte CRC-valid FC03 request prefix from a longer CRC-valid FC03 response in synthetic double-valid cases. Targeted non-semantic fuzz produced 0 accidental semantic requests, and no genuine Thermia frame is currently known to trigger the ambiguity. Treat this as defensive parser hardening debt, not a proven live write defect.

Canonical Research files are reconciled through **PROTO-OFFLINE-64**. Live status remains **EXP387 COMPLETE / POSITIVE**, **EXP388 RUNNING / PARTIAL**, **EXP383 PREPARED / NOT RUN**. Write Beta v4.1 is unchanged.

---

## Follow-up offline reductions — PROTO-OFFLINE-45..60

Added/reconciled on 2026-10-04:

- PROTO45: executable trace/state-machine verifier, replay matrix and verifier output
- PROTO46: synthetic valid-CRC fail-closed replay, fault matrix and replay output
- PROTO47: cross-profile ABI alignment + matrix
- PROTO48: unresolved-register edge correlation + matrix
- PROTO49: selector-candidate ranking + matrix
- PROTO50: 0884 history lifecycle forensics + matrix
- PROTO51: calendar cross-capture forensics + matrix
- PROTO52: Connect/DCM03 artifact-hunt second pass + acquisition matrix
- PROTO53: exhaustive state/permission model-check + conflicting-state matrix
- PROTO54: golden-trace regression suite + assertion matrix
- PROTO55: differential ACK-hardening simulation + policy matrix
- PROTO56: XTR-only ACK-context reduction + matrix
- PROTO57: semantic-state reachability + reachable-state/conflict matrices
- PROTO58: shadow-patch regression + 0870/policy matrices
- PROTO59: local-XTR 0870 context classifier + rule/context matrices
- PROTO60: formal protocol/spec package, model JSON, schema, decision table and validation output

Added tooling under `Research/temp/tools/` includes the trace-state verifier, fail-closed replay harness, golden-trace regression runner and protocol-model validator.

Canonical Research files are reconciled through **PROTO-OFFLINE-60**. The live state remains **EXP387 COMPLETE / POSITIVE**, **EXP388 RUNNING / PARTIAL**, **EXP383 PREPARED / NOT RUN**. None of the offline work completes EXP388 or changes Write Beta v4.1.

The formal model is also mirrored durably under `Research/protocol reduction/` as:
- `thermia_protocol_model_v1.json`
- `thermia_protocol_model_v1_schema.json`
- `thermia_protocol_model_v1_decision_table.csv`

---

# Offline research snapshot — TEMP

Created: 2026-10-03
Updated: 2026-10-03

This folder is a **temporary snapshot/copy** of the offline-analysis material accumulated during the current Thermia iTec XTR M research pass.

The original/canonical files remain in their existing Research locations where applicable. This TEMP folder does **not** replace:
- `Research/THERMIA_PROJECT_STATE.md`
- `Research/EXPERIMENT_LOG.md`
- `Research/PROTOCOL_FINDINGS.md`

## Included baseline reports

- `CALENDAR_STRUCTURE_ANALYSIS_20261002.md`
- `EXP382_OFFLINE_GAP_ANALYSIS.md`
- `THERMIA_0708_OFFLINE_REDUCTION_20260930.md`
- `EXTERNAL_ITEC_ECO5_FULL_CAPTURE_ANALYSIS.md`
- `PROTO_OFFLINE_01_UNKNOWN_PAGE_CORRELATION_20261002.md`
- `PROTO_OFFLINE_02_071C_0730_GATE_ANALYSIS_20261002.md`
- `THERMIA_PROTOCOL_REDUCTION_20261002.md`

## 2026-10-03 offline reductions

Already present:
- `PROTO_OFFLINE_08_UNRESOLVED_RUNTIME_FIELD_REDUCTION_20261003.md`
- `PROTO_OFFLINE_08_CANONICAL_UPDATE_PENDING_20261003.md`
- `PROTO_OFFLINE_09_0708_SCHEDULER_STATE_MACHINE_20261003.md`
- `PROTO_OFFLINE_09_0708_PAGE_BIT_MAP_20261003.csv`
- `PROTO_OFFLINE_09_CANONICAL_UPDATE_PENDING_20261003.md`

Added in this update:
- `CAL_OFFLINE_01_DEEP_REDUCTION_20261003.md`
- `CAL_OFFLINE_01_FINAL_CLOSURE_20261003.md`
- `CAL_OFFLINE_01_LOGICAL_REGISTER_MAP_20261003.csv`
- `CAL_OFFLINE_01_CANONICAL_UPDATE_PENDING_20261003.md`
- `PROTO_OFFLINE_10_DESIRED_STATE_COMMAND_RECONSTRUCTION_20261003.md`
- `PROTO_OFFLINE_10_COMMAND_EVENT_MATRIX_20261003.csv`
- `PROTO_OFFLINE_10_CANONICAL_UPDATE_PENDING_20261003.md`
- `PROTO_OFFLINE_13_CROSS_TOPOLOGY_NORMALISATION_20261003.md`
- `PROTO_OFFLINE_13_CROSS_TOPOLOGY_MAPPING_20261003.csv`
- `PROTO_OFFLINE_13_CANONICAL_UPDATE_PENDING_20261003.md`
- `PROTO_OFFLINE_14_ALARM_STATUS_SERVICE_MAPPING_20261003.md`
- `PROTO_OFFLINE_14_HISTORY_DECODE_20261003.csv`
- `PROTO_OFFLINE_14_CANONICAL_UPDATE_PENDING_20261003.md`
- `PROTO_OFFLINE_15_DCM03_CONNECT_FIRMWARE_ARCHAEOLOGY_20261003.md`
- `PROTO_OFFLINE_15_FIRMWARE_ACQUISITION_TARGETS_20261003.csv`
- `PROTO_OFFLINE_15_CANONICAL_UPDATE_PENDING_20261003.md`
- `PROTO_OFFLINE_16_NATIVE_SETTINGS_SCHEMA_CONSOLIDATION_20261003.md`
- `PROTO_OFFLINE_16_NATIVE_REGISTER_DATABASE_20261003.csv`
- `PROTO_OFFLINE_16_PROFILE_DRIFT_MATRIX_20261003.csv`
- `PROTO_OFFLINE_16_CANONICAL_UPDATE_PENDING_20261003.md`

Numbers 11 and 12 are intentionally absent here: no completed PROTO-OFFLINE-11/12 report is being invented or backfilled.

## Included protocol-reduction data

The current protocol-reduction database, page census, semantic register map, selector map and capture inventory are copied under `protocol reduction/`.

## Included offline tooling

The current helper/reference-model scripts are copied under `tools/` because they support the offline reductions and replay/reference-model work.

## Important evidence-state notes

- TEMP contains working/offline analysis and pending canonical reconciliation notes; it is not itself the canonical source of truth.
- No live experiment is promoted merely by placing material in TEMP.
- CAL-OFFLINE-01 is complete for the current offline evidence scope; calendar write semantics remain unproven where explicitly marked OPEN.
- PROTO-OFFLINE-09/10 reduce the native scheduler and desired-state read/modify/return architecture.
- PROTO-OFFLINE-13 distinguishes logical Online/DCM runtime ABI from topology-specific source adapters.
- PROTO-OFFLINE-14 maps the XTR modern timestamped service/alarm-history structure without inventing alarm-name translations.
- PROTO-OFFLINE-15 narrows old serializer archaeology toward DCM03 and modern XTR archaeology toward Thermia Connect/protocol packages.
- PROTO-OFFLINE-16 treats public Online register semantics as profile-specific and keeps semantic proof separate from write-path proof.

## Follow-up offline reductions — PROTO-OFFLINE-17..21

- `PROTO_OFFLINE_17_APPROVAL_SYNC_READINESS_REDUCTION_20261003.md`
- `PROTO_OFFLINE_17_SESSION_TIMING_MATRIX_20261003.csv`
- `PROTO_OFFLINE_17_CANONICAL_UPDATE_PENDING_20261003.md`
- `PROTO_OFFLINE_18_SYNC_READINESS_DISCRIMINATOR_20261003.md`
- `PROTO_OFFLINE_18_CANDIDATE_FIELD_MATRIX_20261003.csv`
- `PROTO_OFFLINE_18_CANONICAL_UPDATE_PENDING_20261003.md`
- `PROTO_OFFLINE_19_MAILBOX_SYNC_SEQUENCE_COMPLETION_20261003.md`
- `PROTO_OFFLINE_19_ECO5_BOOTSTRAP_PAGE_MATRIX_20261003.csv`
- `PROTO_OFFLINE_19_CANONICAL_UPDATE_PENDING_20261003.md`
- `PROTO_OFFLINE_20_REGISTER_DATABASE_HISTORY_AUDIT_20261003.md`
- `PROTO_OFFLINE_20_REGISTER_DATABASE_DELTA_20261003.csv`
- `PROTO_OFFLINE_20_SUPERSESSION_MATRIX_20261003.csv`
- `PROTO_OFFLINE_20_CANONICAL_UPDATE_PENDING_20261003.md`
- `PROTO_OFFLINE_21_CONNECT_APP_ARTIFACT_HUNT_20261003.md`
- `PROTO_OFFLINE_21_ARTIFACT_ACQUISITION_MATRIX_20261003.csv`
- `PROTO_OFFLINE_21_CANONICAL_UPDATE_PENDING_20261003.md`

These files extend the TEMP working/offline snapshot only. They do not by themselves change live experiment status or replace the canonical Research files.

## Protocol-reduction mirror verification

Verified on 2026-10-03: the five core files under `Research/temp/protocol reduction/` are byte-for-byte identical to their counterparts under `Research/protocol reduction/` by Git blob SHA:

- `thermia_protocol_capture_inventory.csv`
- `thermia_protocol_database.json`
- `thermia_protocol_page_census.csv`
- `thermia_protocol_selector_map.csv`
- `thermia_protocol_semantic_register_map.csv`

This is a mirror-status check only; the TEMP copies remain non-canonical.


## Follow-up offline reductions — PROTO-OFFLINE-22..27

- `PROTO_OFFLINE_22_CANONICAL_RECONCILIATION_20261003.md`
- `PROTO_OFFLINE_23_REFERENCE_MODEL_REGRESSION_20261003.md`
- `PROTO_OFFLINE_23_REGRESSION_OUTPUT_20261003.txt`
- `PROTO_OFFLINE_24_085F_CURRENT_ALARM_BRIDGE_20261003.md`
- `PROTO_OFFLINE_24_085F_HISTORY_MATRIX_20261003.csv`
- `PROTO_OFFLINE_25_UNRESOLVED_REGISTER_SWEEP_20261003.md`
- `PROTO_OFFLINE_25_UNRESOLVED_REGISTER_MATRIX_20261003.csv`
- `PROTO_OFFLINE_26_SESSION_CHALLENGE_METADATA_DEEP_PASS_20261003.md`
- `PROTO_OFFLINE_26_BOOT_CONTEXT_MATRIX_20261003.csv`
- `PROTO_OFFLINE_27_CONNECT_ONSITE_STATIC_ANALYSIS_20261003.md`
- `PROTO_OFFLINE_27_APP_ARTIFACT_MATRIX_20261003.csv`

## Follow-up offline reductions — PROTO-OFFLINE-28..33

- `PROTO_OFFLINE_28_SELECTOR_PROVENANCE_RECONCILIATION_20261003.md`
- `PROTO_OFFLINE_28_SELECTOR_PROVENANCE_MATRIX_20261003.csv`
- `PROTO_OFFLINE_29_RUNTIME_SCHEDULER_GRAMMAR_20261003.md`
- `PROTO_OFFLINE_29_RUNTIME_PAGE_GRAMMAR_MATRIX_20261003.csv`
- `PROTO_OFFLINE_30_PROTOCOL_SCHEMA_LINTER_20261003.md`
- `PROTO_OFFLINE_30_LINTER_RESULTS_20261003.txt`
- `thermia_protocol_schema_current.json`
- `PROTO_OFFLINE_31_0884_EVENT_ID_ARCHAEOLOGY_20261003.md`
- `PROTO_OFFLINE_31_EVENT_ID_CANDIDATE_MATRIX_20261003.csv`
- `PROTO_OFFLINE_32_CHALLENGE_GENERATOR_DEEP_REDUCTION_20261003.md`
- `PROTO_OFFLINE_32_CHALLENGE_BYTE_STATS_20261003.csv`
- `PROTO_OFFLINE_33_CONNECT_HARDWARE_OEM_FINGERPRINT_20261003.md`
- `PROTO_OFFLINE_33_HARDWARE_FINGERPRINT_MATRIX_20261003.csv`

Canonical Research state is reconciled through PROTO-OFFLINE-33. TEMP remains a working/archive surface rather than the source of truth.

## Follow-up offline reductions — PROTO-OFFLINE-34..39

- `PROTO_OFFLINE_34_0708_W5_SEMANTIC_AUDIT_20261003.md`
- `PROTO_OFFLINE_34_W5_EVIDENCE_MATRIX_20261003.csv`
- `PROTO_OFFLINE_35_RUNTIME_COUNTER_SCALING_20261003.md`
- `PROTO_OFFLINE_35_RUNTIME_COUNTER_SCALING_MATRIX_20261003.csv`
- `PROTO_OFFLINE_36_RUNTIME_FIELD_CORRELATION_20261003.md`
- `PROTO_OFFLINE_36_RUNTIME_CORRELATION_MATRIX_20261003.csv`
- `PROTO_OFFLINE_37_WRITE_BETA_SAFETY_PROVENANCE_AUDIT_20261003.md`
- `PROTO_OFFLINE_37_TX_ROUTE_AUDIT_MATRIX_20261003.csv`
- `PROTO_OFFLINE_38_ABI_PROFILE_FINGERPRINT_CLASSIFIER_20261003.md`
- `PROTO_OFFLINE_38_PROFILE_CLASSIFICATION_MATRIX_20261003.csv`
- `PROTO_OFFLINE_38_CLASSIFIER_OUTPUT_20261003.txt`
- `tools/thermia_profile_classifier.py`
- `PROTO_OFFLINE_39_EXPERIMENT_EVIDENCE_COVERAGE_AUDIT_20261003.md`
- `PROTO_OFFLINE_39_EXPERIMENT_COVERAGE_LEDGER_20261003.csv`

Canonical Research state is reconciled through PROTO-OFFLINE-39. TEMP remains a working/archive surface rather than the source of truth.

## Follow-up offline reductions — PROTO-OFFLINE-40..44

- `PROTO_OFFLINE_40_CHALLENGE_RESPONSE_PAIR_REDUCTION_20261003.md`
- `PROTO_OFFLINE_41_NOOP_VS_DELTA_REPUBLISH_20261003.md`
- `PROTO_OFFLINE_42_PAGE_CACHE_FRESHNESS_20261003.md`
- `PROTO_OFFLINE_43_RUNTIME_ACK_CONTEXT_RECONSTRUCTION_20261003.md`
- `PROTO_OFFLINE_43_ACK_CONTEXT_MATRIX_20261003.csv`
- `PROTO_OFFLINE_44_FULL_PROTOCOL_STATE_MACHINE_REGRESSION_20261003.md`
- `PROTO_OFFLINE_44_STATE_REGRESSION_MATRIX_20261003.csv`

Canonical Research state is reconciled through PROTO-OFFLINE-44. These offline results do not advance EXP388 and do not modify Write Beta behavior.
