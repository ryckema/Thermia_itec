# PROTO-OFFLINE-18 — canonical update pending

**Date:** 2026-10-03  
**Reason pending:** GitHub write permission was not granted in the current request.

## THERMIA_PROJECT_STATE.md — proposed addition

- **PROTO-OFFLINE-18 — COMPLETE / NEGATIVE** — exhaustive offline search found no independent captured RS485 field that predicts genuine Eco5 configuration-service readiness before the first `03E8/count14` ACK.
- Seven genuine Eco5 boot windows were compared: six successful, one no-response/no-sync negative control.
- 25 data-bearing frame families were scanned for value transitions.
- No family changes within the final 10 s before first `03E8` ACK in all six successful sessions.
- Same-day successful and failed 20260926 boots have byte-identical key state near +120 s for `A80C..A812`, slave-0x02 FC17 response, `AFDC..AFE0`, `04A6`, `085F`, and 0x1E control requests.
- `04A6` and `085F` are not readiness flags.
- `0708` begins only later in runtime and is not a pre-readiness signal.
- No `0xA5` traffic exists in the two genuine Eco5 captures, so that candidate cannot be evaluated from this corpus.
- Best current model: approval accepted + ~120 s gateway/session age fits all successful boots, while neither condition alone is sufficient.
- First `03E8` ACK is the first direct bus-visible marker of native configuration-service readiness.
- Missing discriminator is likely gateway-internal or not present in the captured RS485 state; this remains an inference, not proven implementation detail.
- EXP388 remains RUNNING / PARTIAL.

## EXPERIMENT_LOG.md — proposed entry

`PROTO-OFFLINE-18 | Sync-readiness discriminator search | COMPLETE / NEGATIVE. Six successful + one failed genuine Eco5 boot windows were aligned. No independent data-bearing RS485 family shows a common transition within 10 s before first 03E8 ACK. Same-day success/failure controls share identical A80C..A812, AFDC..AFE0, 04A6, 085F and other recurrent state near ~120 s. Current corpus supports approval-accepted + ~120 s session age as a joint model; first 03E8 ACK remains the first direct readiness marker.`

## PROTOCOL_FINDINGS.md — proposed durable finding

**DISPROVEN / SUPERSEDED:** the working idea that an already-observed recurrent controller/peripheral field announces native Online/DCM configuration-service readiness before the first `03E8` ACK.

**STRONGLY SUPPORTED / genuine Eco5 capture evidence:** approval/session state and page-service readiness are separate. Within the currently captured fields, no independent readiness bit/state was found. `A80C..A812`, `AFDC..AFE0`, `04A6`, `085F` and observed `0x1E` traffic do not discriminate successful from failed readiness at the ~120 s boundary. The first accepted `03E8` ACK is the earliest direct bus-visible service-ready marker.

**HYPOTHESIS:** the missing state is gateway-internal or sideband and may be timer-, registration-, cloud-, retained-state- or protocol-service-related.