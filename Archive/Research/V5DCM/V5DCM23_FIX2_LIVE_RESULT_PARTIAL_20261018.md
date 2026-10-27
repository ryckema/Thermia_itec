# V5DCM23-FIX2 — user-reported live RX-only observation

**Experiment status: RUNNING / PARTIAL** (first user-supplied live evidence; not extended soak or native C2 proof). 2026-10-18.

## Evidence and provenance
Source: user-provided raw ESPHome console `Pasted text(20261018-162608).txt`, 3,536 lines, approximately 18:23:35–18:26, with active source explicitly reporting `[V5DCM22]` and `[V5DCM23] PORTABLE_LEDGER`. The currently running firmware therefore contains the V5DCM23 observer. Compile succeeded sufficiently to flash and boot; exact binary hash and private ZIP source-byte identity are not independently authenticated.

User has flashed FIX2 candidate. Prior FIX1 compilation failures were missing include-copy headers and misplaced ESP_LOGW code. The earlier private source is not published.

## Observed live facts
- **Five** V5DCM23 snapshots: `profile=1 received=1/33 completeShapes=0`, `W2pending=BFFF W3pending=867E W4pending=035F` at 18:23:58, 18:24:28, 18:24:58, 18:25:28, 18:25:58. No C2/Online/controller owner/epoch proof and TX=HARD_DENY.
- Five simultaneous V5DCM22 snapshots: `sinceBoot=1/33 sessionCandidate=1/33 W2=0000 W3=0001 W4=0000`; exact occurrences 28,56,84,112,140; wrongGeom=0, fc23=0, integrity=0, revoked=0. Strong cross-check of a **single observed native significant 0x03E8/count14** shape, not 33 groups.
- Four B11C checkpoints grow V5=portable=276/276 → 1046/1046, countDiff=byteDiff=boundaryFaults=resync=drops=ioTxAttempts=0. Four B11D checkpoints grow rawFrames=portableFrames=comparedV5 287→1053 with zero differences, raw fault, overflow, noise and ioTx.
- Four S8 HEALTH checkpoints valid 276→1046 and fc16 45→170, no resync/drop, DE=0, software TX counters 0/0/0. Periodic `HARD_DENY` execution reports at end `candidates=208 denied=208 physical_attempts=0`. **Software-observed only; not independent electrical verification.**
- Uptime grows 34→124 seconds within logs, no visible reset after log start. No OTA rollback line in this capture, which does not negate earlier rollback history.
- Existing HA heating, DHW, compressor, condenser, outdoor sensors report values.
- Other pre-existing gate `[R6-P30EC]` continues to report `first=STAGE_D_LEDGER_FAULT reason=INTEGRITY_HOLD_NO_TX`, `D=4`, `NO_APPROVAL`, whereas B11C/B11D live parser integrity is clean. **Do not interpret this as a new RX CRC failure or as native accept; separately audit gate-D stale/latched provenance semantics offline.** Also some A80E/A80F snapshots are NaN; do not infer a new regression without comparative evidence.

## Conclusion and safety
**Positive partial**: source-compiled FIX2 firmware operates on device; actual portable V5DCM23 ledger receives native strict 03E8/14 and agrees with interim RX33 observation; RX/HA and software hard deny stable for ~2m25s observed.

**Open:** sustained runtime, source hash/OTA partition, physical DE/TX electrical measurement, actual controller epoch/owner, native C2/Online, explanation of D=4 integrity-held independent session gate. A ledger `profile=1` is a caller-selected profile, not firmware/controller authentication.

**No further live test authorized or performed.** Continue OFFLINE audit of gate-D `INTEGRITY_HOLD_NO_TX` semantics and reconciliation of full HA entity inventory. Abort/recover to prior known-good RX-only version on crashes, HA loss, growing parser faults, or actual unsolicited TX. No request for repeated compiler output.
