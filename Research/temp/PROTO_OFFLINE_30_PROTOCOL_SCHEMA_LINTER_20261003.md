# PROTO-OFFLINE-30 — protocol schema + automatic linter

**Date:** 2026-10-03  
**Status:** **COMPLETE / POSITIVE**  
**Hypothesis:** current protocol knowledge can be expressed as a machine-readable deny-by-default schema and used to statically catch stale page shapes, invalid CRCs and selector-provenance mistakes in the current Write Beta YAML.  
**Controlled change:** offline tooling/database only; no bus TX, firmware flash, controller restart or setting write.

## Deliverables

- `Research/temp/thermia_protocol_schema_current.json`
- `Research/temp/tools/thermia_protocol_linter.py`
- `Research/temp/PROTO_OFFLINE_30_LINTER_RESULTS_20261003.txt`

## Current Write Beta audit

Result:
- **0 hard errors**
- **0 warnings**
- **39 passes**

No CRC-invalid known selector frame was found.

The seven EXP383 candidate controls remain visibly marked `TEST`; their code presence is not evidence promotion.

## Strong conclusion

Protocol knowledge is now machine-checkable rather than prose-only. Future YAML/reference-model changes can be checked against one deny-by-default schema before live use.

This is a static protocol linter, not ESPHome compile verification.

## Live status

Unchanged:
- EXP387 COMPLETE / POSITIVE
- EXP388 RUNNING / PARTIAL
