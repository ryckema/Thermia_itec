# PROTO-OFFLINE-45 — Trace-replay / state-machine verifier

**Date:** 2026-10-03  
**Status:** **COMPLETE / POSITIVE WITH MODEL REFINEMENTS**  
**Scope:** offline only. No heat-pump TX, no YAML behavior change, no compile/flash, no reboot and no setting write.

## Hypothesis

The protocol model from PROTO-OFFLINE-44 can be converted into an executable trace verifier and replayed against all currently available genuine Online/DCM captures plus a local passive XTR trace. The replay should either validate the current state model or expose specific places where the model is too coarse.

## Baseline

- PROTO-OFFLINE-19: autonomous bootstrap vs later mailbox refresh.
- PROTO-OFFLINE-29: runtime publication grammar.
- PROTO-OFFLINE-40..44: approval, desired-state, cache-age and ACK-context reductions.
- Current Write Beta v4.1 is used only as a comparison target; it is **not modified**.

## Exact controlled change

A new offline verifier (`thermia_trace_state_verifier.py`) parses raw RS485 frames, validates CRC, pairs FC16/FC03/FC17 request-response exchanges, recognizes the 32 configuration pages, decodes answered `0708/count6` mailboxes, tracks desired pulls and detects the repeated-`0870` reconnect pattern.

No live variable changes.

## Corpus

### Genuine Online/DCM captures

Seven reference captures were replayed:

1. four legacy A5/Online captures from 2026-09-24/25;
2. two modern Eco5/0x1E Online captures from 2026-09-26/28;
3. the 2026-10-03 ATEC + classic DCM03 cold-start capture.

Together they contain **4809 slave-0x0F frames; CRC failures: 0**.

### Local XTR trace

`thermia-logs.txt` was also replayed as a **local passive XTR trace**. It is not identified as EXP387/EXP388 and is therefore not used to advance either experiment.

## Observed facts

### 1. Approval/bootstrap path is machine-reproducible

The verifier finds **7 complete 32-page bootstraps** in the genuine corpus:

- six Eco5 bootstraps;
- one ATEC/DCM03 bootstrap.

It also recognizes one legacy capture that starts part-way through an ordered bootstrap: `042E -> ... -> 06F4`, **29 ACKed pages**.

No complete bootstrap violates the 32-page page-index order.

### 2. Desired-state path is machine-reproducible

The verifier finds **7 selector-owned desired-page pulls**:

- two legacy `03E8` pulls whose same-page current/confirmation bracket is incomplete in those captures;
- four Eco5 semantic deltas, all four followed by exact same-page FC16 confirmation;
- one ATEC `0546` no-op pull, with no same-page confirmation required by the observed genuine behavior.

This independently reproduces PROTO41.

### 3. Reconnect path is machine-reproducible

The legacy 20260925_090550 capture is recognized as one recovery/rejoin window:

- 31 repeated unACKed `0870/count17` publications;
- then one ACKed `0870`;
- then `0708` rejoin/config-export state.

The verifier therefore does not interpret those 31 missing ACKs as packet loss.

### 4. Runtime grammar survives executable replay

Across steady answered-mailbox windows the verifier finds **286/298 = 96.0%** exact canonical A/B/C/D/E publication-group intervals.

The remaining 12 intervals are boundary-spanning, merged or capture-end partial groups; none requires a new runtime page family.

### 5. Local XTR passive trace stays fail-closed

The local passive trace lasts **73.842 s** and contains:

- **70** unACKed `03E8/count14` publications;
- **35** unACKed `085F/count5` publications;
- no answered `0708`;
- no captured `071C/0730` approval exchange.

The replay therefore never promotes that trace into qualified mailbox/runtime service. It remains an unqualified retry/capture-only state.

## Model refinements discovered by the verifier

### A. Approval and service/config traffic are not strictly exclusive states

Three **ACKed configuration pages occur while Eco5 is still emitting unanswered approval challenges**, before the eventual accepted challenge response:

- 20260926: `04A6/count13`;
- 20260928: `04A6/count13`, then `04BA/count22`.

This is direct evidence that `APPROVAL_RETRY` and retained/service traffic can overlap. The PROTO44 diagram remains useful as a workflow, but should not be implemented as one mutually exclusive enum.

**Better model:** keep at least two orthogonal axes:

1. session/approval qualification;
2. current work class (bootstrap, runtime, refresh, service, desired, recovery).

### B. Legacy configuration can be pushed and ACKed outside W2/W3 mailbox work

`thermia_capture_20260925_071517.log` contains two genuine ACKed standalone `03E8/count13` publications at approximately 22.185 s and 61.676 s while the last answered mailbox is steady:

`W0=0000 W1=0000 W2=0000 W3=0000 W4=077F W5=0006`.

Between those two pages word 0 changes `0x0017 -> 0x0016`.

Therefore a universal rule of **“configuration FC16 is valid only when W2/W3 explicitly owns it”** is too strong across Thermia profiles. A controller-originated autonomous configuration/state push exists in genuine legacy traffic.

This does **not** prove that every standalone XTR configuration page should be ACKed.

### C. `085F` ACK policy is profile-specific

The ATEC/DCM03 capture contains two `085F/count5` publications and both are ACKed. One is the post-bootstrap handoff; the other occurs in steady runtime with mailbox:

`0000 0000 0000 0000 077F 0006`.

Therefore **“085F may only be ACKed in an explicit service-refresh state” is not a universal Thermia rule**.

This refines PROTO43/44 rather than invalidating their local-safety point:

- modern Eco5 mostly leaves `085F` unACKed;
- ATEC/DCM03 ACKs the observed steady `085F`;
- local XTR permission must therefore remain locally proven and profile-specific.

## Strong conclusions

1. The core native architecture is now reproducible by code, not only by manual interpretation: approval, bootstrap, mailbox/runtime, desired-page pull and recovery/rejoin are all detected from raw frames.
2. PROTO44's states should be treated as **overlapping protocol dimensions**, not a single strictly linear finite-state enum.
3. Two earlier hardening ideas must stay **candidates**, not universal rules:
   - requiring W2/W3 ownership for every runtime configuration ACK;
   - forbidding steady-state `085F` ACK outside a service-refresh state.
4. The `0870` recovery exception remains strongly supported: normal traffic ACKs it, while a real reconnect window deliberately withholds it until a transition point.
5. The local passive XTR trace behaves safely under the new verifier: it never acquires a qualified state from page shape alone.

## Write Beta v4.1 consequence

PROTO45 does **not** justify broadening v4.1, but it changes the interpretation of the PROTO44 hardening backlog:

- `085F` context hardening: **still worth local XTR testing**, but no universal cross-profile predicate should be encoded.
- `0870` context hardening: **still strongly supported**.
- generic runtime configuration ACK hardening: **must be tested locally one class at a time**; genuine legacy traffic proves standalone configuration pushes can be legitimate.
- `0834/count18`: unchanged — genuine ACK evidence is strong, local XTR ACK safety remains unproven.

## Hypotheses

- The two standalone legacy `03E8` pushes are likely controller-originated change notifications/current-state exports, but the capture alone does not prove what caused the underlying setting change.
- The three approval/config overlap pages may be retained work from the prior session while a new approval attempt is underway; exact controller/gateway ownership of that overlap remains open.

## Unknowns

- whether local XTR ever emits a legitimate standalone configuration push during qualified runtime;
- local XTR steady-state `085F` ACK requirement;
- whether a local XTR `0870` retry window behaves exactly like the legacy reconnect capture;
- exact rules by which session qualification and retained work overlap across generations.

## Safety / abort criteria

Offline only: no transmitted frame exists, so no device abort action is required. Any future live experiment derived from this result must change only one ACK-permission class at a time, leave unexpected traffic capture-only, and preserve EXP388 as RUNNING / PARTIAL until its own remaining branches are actually exercised.

## Live status

Unchanged:

- **EXP387 — COMPLETE / POSITIVE**
- **EXP388 — RUNNING / PARTIAL**
- **EXP383 — PREPARED / NOT RUN**
