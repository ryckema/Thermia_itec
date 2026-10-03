> **Reconciliation status: APPLIED / HISTORICAL (2026-10-03).** The canonical Research state was reconciled through PROTO-OFFLINE-16 in commit `b4edd42cd17354845ec75111fb0aa30e5a0bda38`. This file is retained as the historical proposal that informed that reconciliation; do not apply it again blindly.

# Pending canonical reconciliation — PROTO-OFFLINE-14

**Date:** 2026-10-03  
**GitHub:** not modified  
**Status:** PROTO-OFFLINE-14 COMPLETE / POSITIVE  
**Live experiment:** EXP388 remains RUNNING / PARTIAL

## THERMIA_PROJECT_STATE.md — proposed additions

- Add `PROTO-OFFLINE-14 — COMPLETE / POSITIVE — alarm/status/service-data mapping`.
- Local XTR confirms native `0x0F:0884/count60` as a rolling timestamped history page.
- Legacy genuine Online/DCM ABI:
  `10 × [raw_id, minute, hour, day, month, year]`.
- Modern Eco5 and local XTR ABI:
  `8 × [raw_A, raw_B, minute, hour, day, month, year] + 4-word trailer`.
- `0884` is VERY STRONGLY SUPPORTED as the Online/DCM alarm/service-history export, but exact identity with the complete XTR UI ALARM list is not yet proven.
- Official XTR UI semantic anchor:
  ALARM history depth 10, fields alarm_name/time/date.
- Raw `0884` IDs must not be interpreted directly as displayed XTR E-codes.
- Modern trailer:
  `08BC..08BF`; last word changes with history progression in selected local captures, exact semantics OPEN.
- Firmware-derived current alarm layer remains distinct:
  DHP/HE `0x03F0 ErrorCode`, `0x0400..0x0404 AlarmField1..5`.
  Their native `0x0F` bridge is OPEN.
- `085F/count5` remains a runtime/service page but is semantically OPEN; sampled local XTR payload is all zero.
- Maintain separation:
  live operational status (`07F4/083C/0845/0865/0866`) vs current alarms vs history.

## EXPERIMENT_LOG.md — proposed entry

### PROTO-OFFLINE-14 — COMPLETE / POSITIVE — alarm/status/service history

**Hypothesis:** native runtime/service pages expose timestamped history separately from current status/alarm state.

**Controlled change:** offline-only comparison of existing genuine legacy/Eco5 Online captures, local XTR stage-40 payloads, commissioning manual and firmware semantics. No new TX/YAML/reboot/write.

**Observed:**
- legacy `0884/count60`: exact 10×6 timestamped record ABI.
- Eco5 `0884/count60`: exact 8×7 + trailer4 ABI.
- local XTR `0884/count60`: same modern 8×7 + trailer4 ABI.
- local history moves newest-first in later snapshots.
- firmware exposes separate abstract ErrorCode + AlarmField1..5.
- sampled local `085F/count5` remains all-zero.

**Result:** COMPLETE / POSITIVE.

No live experiment status changed.

## PROTOCOL_FINDINGS.md — proposed durable updates

### PROVEN / locally confirmed

Modern XTR `0884/count60` layout:

```text
8 × 7-word timestamped records
+ 4-word trailer

record:
raw_A
raw_B
minute
hour
day
month
year2
```

### PROVEN / genuine legacy Online/DCM structural

Legacy `0884/count60` layout:

```text
10 × 6-word records

record:
raw_id
minute
hour
day
month
year2
```

### VERY STRONGLY SUPPORTED

`0884/count60` is the Online/DCM alarm/service-history export.

### FIRMWARE-DERIVED / separate semantic layer

DHP/HE:
- `0x03F0 ErrorCode`
- `0x0400 AlarmField1`
- `0x0401 AlarmField2`
- `0x0402 AlarmField3`
- `0x0403 AlarmField4`
- `0x0404 AlarmField5`

No native `0x0F` serializer mapping for these is yet proven.

### OPEN / UNKNOWN

- raw history IDs -> XTR alarm names / E-codes.
- modern raw_B meaning.
- trailer `08BC..08BF`.
- exact relation between modern 8-entry wire history and 10-entry UI history.
- `085F/count5` semantics.
- whether `0884` is strictly alarm-only or broader service/event history.

### DISPROVEN / SUPERSEDED shortcut

Do not treat raw `0884` word0 as a direct displayed XTR `E###` number.

### Safety

This track is read-only. Do not synthesize or write history/alarm pages. Any future mapping should use passive UI/capture correlation or naturally occurring alarm events.