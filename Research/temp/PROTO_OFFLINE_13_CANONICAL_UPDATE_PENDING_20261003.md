> **Reconciliation status: APPLIED / HISTORICAL (2026-10-03).** The canonical Research state was reconciled through PROTO-OFFLINE-16 in commit `b4edd42cd17354845ec75111fb0aa30e5a0bda38`. This file is retained as the historical proposal that informed that reconciliation; do not apply it again blindly.

# Pending canonical reconciliation — PROTO-OFFLINE-13

**Date:** 2026-10-03  
**GitHub:** not modified  
**Status:** PROTO-OFFLINE-13 COMPLETE / POSITIVE  
**Live experiment:** EXP388 remains RUNNING / PARTIAL

## THERMIA_PROJECT_STATE.md — proposed additions

- Add `PROTO-OFFLINE-13 — COMPLETE / POSITIVE — cross-topology runtime normalisation`.
- Strong architecture conclusion:
  `0x0F` runtime pages form a logical Online/DCM ABI above topology-specific physical backends.
- Define portability classes:
  1. portable direct fields;
  2. portable logical fields with source substitution;
  3. topology/capability identity fields;
  4. generation-specific derived runtime fields;
  5. reserved/legacy compatibility fields.
- Key source substitutions:
  - `07D1`: legacy `A7F9`; Eco5 `1E:0000/10`.
  - `07E4`: legacy `04:ABE0`; Eco5 `1E:0005/10`.
  - `0820` family: legacy A5; modern `0x1E`.
- New modern metadata source mapping:
  - `07E8 <- 1E:001C`
  - `07E9 <- 1E:001D`
  - `07EA <- 1E:0016`
  - `07EB <- 1E:0017`
  - `0830 <- 1E:0016`
  - `0831 <- 1E:0017`
- `0858..085E` is a cross-topology clock/date ABI; weekday enumeration is Monday=0.
- `0819` is a strong topology/profile discriminator: old=0, Eco5=20.
- `0867` remains topology fingerprint: old=`0016`, Eco5=`00E8`.
- `0870` retains the same 7+3 service-counter geometry across both topology families; group-level interpretation strengthened, individual labels remain unproven.
- Safety: never replay an entire foreign-model payload merely because page start/count is identical.

## EXPERIMENT_LOG.md — proposed entry

### PROTO-OFFLINE-13 — COMPLETE / POSITIVE — cross-topology normalisation

**Hypothesis:** the Online/DCM runtime layer preserves a logical ABI while changing physical source endpoints between legacy `0x04/A5` and modern `0x1E` topologies.

**Controlled change:** offline-only comparison of six genuine captures; no TX/YAML/restart/write.

**Key results:**
- stable runtime page shapes across topologies;
- proven source substitution for `07D1` and `07E4`;
- `0820` confirmed as legacy-A5 versus modern-1E abstraction boundary;
- modern `07E8..07EB` mapped to `1E:001C,001D,0016,0017`;
- modern `0830/0831` mapped to `1E:0016/0017`;
- `0858..085E` clock/date tuple valid cross-topology with Monday=0 weekday;
- `0819` and `0867` are topology/profile discriminators;
- same service-counter geometry retained at `0870`.

**Result:** COMPLETE / POSITIVE.

## PROTOCOL_FINDINGS.md — proposed durable updates

### PROVEN / structural cross-topology

- `07D1` is source-substituted:
  - legacy `<- A7F9`;
  - modern `<- signed(1E:0000)/10`.
- `07E4` is source-substituted:
  - legacy `<- 04:ABE0`;
  - modern `<- signed(1E:0005)/10`.
- modern identity/capability source relationships:
  - `07E8=1E:001C`
  - `07E9=1E:001D`
  - `07EA=1E:0016`
  - `07EB=1E:0017`
  - `0830=1E:0016`
  - `0831=1E:0017`
- `0858..085E` = second/minute/hour/day/month/year/weekday in both topologies.
- weekday enumeration in that runtime tuple is Monday=0.

### STRONGLY SUPPORTED

- `0820` is a topology abstraction page:
  - legacy backend A5;
  - modern backend `0x1E`.
- `0819` is topology/profile metadata (`0` legacy, `20` Eco5).
- `0867` is topology/platform metadata (`0x16` legacy, `0xE8` Eco5).
- `0870` group separators and 7+3 geometry are topology-stable.

### HYPOTHESIS / OPEN

- exact semantic names of `1E:0016/0017/001C/001D`.
- exact equivalence/scaling of legacy A5 tail fields versus modern `082D..0831`.
- individual `0872..0878` and `087B..087D` labels remain to be locally cross-checked.

### Safety rule

Equal `0x0F` page address/count does not imply byte-identical payload semantics across models. Implement logical-field adapters; do not replay whole foreign-model page images.