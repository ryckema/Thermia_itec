# PROTO-OFFLINE-17 — canonical update pending

**Date:** 2026-10-03  
**Reason pending:** no GitHub write permission was granted in the current request.

## THERMIA_PROJECT_STATE.md — proposed addition

- **PROTO-OFFLINE-17 — COMPLETE / POSITIVE** — genuine Eco5 approval and native sync readiness are separate bus-visible gates.
- Across six successful genuine sessions, first accepted `03E8/count14` ACK occurs at `118.478..120.296 s` after bus return.
- Two challenge-#3 approvals occur at about `10 s`, but the gateway then leaves `102` identical `03E8` requests unACKed until about `118.5 s`.
- Four challenge-#29 approvals occur at about `120 s` and `03E8` is ACKed immediately.
- First `03FC/count11` follows accepted `03E8` ACK within `0.373..0.481 s`.
- A no-response boot continues challenge polling beyond 120 s with no gateway FC16 ACK/FC03 service, proving elapsed time alone is insufficient.
- Treat `approval/session open` and `configuration service ready` as separate states in emulator/reference-model work.
- EXP388 remains RUNNING / PARTIAL; no live experiment status changes.

## EXPERIMENT_LOG.md — proposed entry

`PROTO-OFFLINE-17 | Offline approval-vs-sync-readiness reduction | COMPLETE / POSITIVE. Six genuine Eco5 sessions show approval response and native page-service readiness are distinct. Early #3 approvals at ~10 s trigger immediate 03E8 retries, but first 03E8 ACK is delayed to ~118.5 s after boot; late #29 approvals at ~120 s receive immediate 03E8 ACK. All six first ACKs occur 118.478..120.296 s after bus return; 03FC follows within 0.373..0.481 s.`

## PROTOCOL_FINDINGS.md — proposed durable finding

**STRONGLY SUPPORTED / genuine Online/DCM capture evidence**

The `071C/0730` approval response and the `0x0F` native configuration-service readiness state are distinct. In two genuine Eco5 boots, approval at challenge #3 (~10 s) is accepted immediately and causes the controller to start `03E8/count14`, but 102 identical requests are left unACKed until ~118.5 s after bus return. In four other boots approval occurs at challenge #29 (~120 s) and `03E8` is ACKed immediately. Across all six successful sessions the first accepted `03E8` ACK occurs at 118.478..120.296 s after bus return, after which `03FC/count11` follows in 0.373..0.481 s.

Do not encode the ~120 s boundary as a universal Thermia controller requirement. Local XTR session work can progress without reproducing that delay. Treat it as genuine Eco5 gateway/session behavior unless cross-model evidence proves otherwise.