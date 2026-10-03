# PROTO-OFFLINE-44 — Full protocol state-machine regression

**Date:** 2026-10-03  
**Status:** **COMPLETE / POSITIVE WITH HARDENING REQUIREMENTS**  
**Scope:** offline capture/model regression only. No bus TX, YAML modification, compile, flash, reboot, or setting write.

## Hypothesis

The current native Online/DCM model can be expressed as a small set of protocol states, and the current Write Beta v4.1 can be checked against that state graph to identify over-broad permissions, deliberately conservative gaps, and unsupported transitions.

## Controlled change

Baseline:

- PROTO-OFFLINE-19 — bootstrap vs later mailbox refresh;
- PROTO-OFFLINE-29 — runtime grammar;
- PROTO-OFFLINE-37 — static TX provenance audit;
- PROTO-OFFLINE-40..43;
- ATEC-COLDSTART-01.

New variable: regress the current v4.1 protocol actions against the combined genuine seven-capture transition model.

## Reconstructed protocol state graph

### S0 — APPROVAL / SESSION OPEN

`0F FC17 read 0730/8 + write 071C/8 -> DCM response`

Eco5 and ATEC both exhibit this gate. ATEC proves classic DCM03 can answer it directly.

### S1 — APPROVED / WAITING_FOR_PAGE_SERVICE

Genuine Eco5 proves approval acceptance and page-service readiness can be separated by about 108 s. During that interval the controller can repeatedly publish `03E8` without receiving an ACK.

ATEC demonstrates this wait is not universal: page service begins 1.833 s after its DCM03 response.

### S2 — ORDERED BOOTSTRAP / EXPORT

The controller performs the 32-page configuration export through terminal `06F4`, with profile-specific page counts.

### S3 — POST-BOOT SERVICE HANDOFF

`085F` can appear immediately after export completion and can be ACKed as part of the transition into mailbox/runtime service.

### S4 — NORMAL MAILBOX / RUNTIME

Normal runtime consists of answered `0708` polls plus the recurrent runtime ring:

`07D0/07E4 -> 07F8/080C -> 0820/0834 -> 0848/0864 -> 0870`

with `0884` as an occasional history/service publication.

Possible branches:

- `S4 -> S5` configuration/current refresh;
- `S4 -> S6` service refresh / overlay;
- `S4 -> S7` desired-state transaction;
- retained/reconnect paths may enter `S8`.

### S5 — CONFIGURATION / CURRENT-PAGE REFRESH

`W2/W3` carries outstanding current-page work. Controller FC16 configuration pages are ACK-gated in the active work context.

### S6 — SERVICE REFRESH / RECURRENT OVERLAY

W4 carries service/runtime work metadata, while ordinary runtime traffic can continue. `085F` is the clearest overlay.

### S7 — DESIRED-PAGE TRANSACTION

`0708 desired selector -> controller FC03 page pull -> DCM returns full page`

For a semantic delta, genuine Eco5 performs exact FC16 republish/confirmation.

For the genuine ATEC `0546` no-op, no same-page FC16 republish follows.

### S8 — RETAINED / RECONNECT / RECOVERY

Legacy genuine evidence shows repeated unACKed `0870` can persist until a single ACK causes entry into `0708` rejoin/export state.

Local XTR EXP3xx work independently proves retained-controller recovery must be branch-aware rather than treated as fresh boot.

## Runtime ACK regression against genuine corpus

| Runtime page | Publications | ACKed | UnACKed | Current v4.1 generic policy |
|---|---:|---:|---:|---|
| `07D0` | 123 | 122 | 1 | ACK |
| `07E4` | 118 | 117 | 1 | ACK |
| `07F8` | 90 | 90 | 0 | ACK |
| `080C` | 84 | 82 | 2 | ACK |
| `0820` | 66 | 65 | 1 | ACK |
| `0834` | 64 | 63 | 1 | **NO ACK / stop** |
| `0848` | 66 | 66 | 0 | ACK |
| `085F` | 331 | 20 | **311** | ACK known payload |
| `0864` | 67 | 67 | 0 | ACK |
| `0870` | 95 | 64 | **31** | ACK |
| `0884` | 21 | 21 | 0 | ACK |

## Write Beta v4.1 regression

### PASS — guarded approval / R1 route

The current XTR code keeps the approval response behind exact shape, controller-state and one-shot guards.

### PASS — ordered bootstrap

Exact page/count/order guards match the reconstructed S2 model.

### PASS — `04A6` runtime exception

Runtime `04A6` is capture-only except in the explicitly proven resume context.

### HARDEN — `085F`

Current v4.1 treats a locally known `085F` payload as generic runtime ACK permission.

**Required future hardening:** make `085F` ACK contingent on explicit local service/recovery state.

### HARDEN — `0870`

Current v4.1 allows generic runtime ACK by page shape.

**Required future hardening:** permit ACK in qualified normal runtime or an explicit recovery branch.

### HARDEN — runtime configuration pages

Current v4.1's `local_config` class can ACK known configuration page shapes outside the ordered resume branch.

**Required future hardening:** unexpected standalone configuration FC16 must default to capture-only unless bootstrap/refresh/confirmation/resume owns it.

### CONSERVATIVE GAP — `0834`

Genuine references ACK **63/64** observed `0834/count18` publications, but v4.1 intentionally refuses it because local XTR ACK safety has not been established.

This is a coverage gap, not a safety defect.

### PASS — desired-state transaction

The current full-page clone + one-word mutation + exact FC16 republish rule matches all bracketed genuine semantic-delta transactions.

PROTO41 adds that an exact no-op need not republish; v4.1 already resolves freshly synchronized same-value targets as NO-TX.

### PASS / CONSERVATIVE — cache freshness

PROTO42 shows a genuine gateway can reuse a bus-visible page image at least 374.586 s old. v4.1's fresher-cache rule is stricter than genuine behavior but safety-conservative.

## Result

**COMPLETE / POSITIVE WITH HARDENING REQUIREMENTS.**

The full genuine-capture state graph is coherent enough to drive a state-qualified ACK policy. It does not justify new semantic targets or cross-model payload replay.

## Recommended next implementation step

Do not change production behavior solely from this offline analysis. Harden one ACK authorization class at a time and regress each change separately.

## Live state

Unchanged:

- EXP387 — COMPLETE / POSITIVE
- EXP388 — RUNNING / PARTIAL
- EXP383 — PREPARED / NOT RUN
