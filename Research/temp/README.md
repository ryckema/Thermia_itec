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
