# PROTO-OFFLINE-62 — Source-transcribed host decision-engine regression

**Date:** 2026-10-04  
**Status:** **COMPLETE / POSITIVE**  
**Hypothesis:** the relevant runtime authorization/state logic from Write Beta v4.1 can be transcribed into a host-side executable decision engine and reproduce the current golden/fault/reachability expectations without executing ESPHome firmware.  
**Controlled change:** offline host model only. No YAML change, bus TX, compile/flash.

## Scope

The host engine transcribes current v4.1 branch ordering and guards for:

- runtime FC16 ACK permission;
- special `04A6`, `0834`, `085F`, hot-rejoin `06F4`;
- `0708` arbitration for 03E8 / 042E / 0442 / 0546;
- current-refresh and delayed-rearm behavior;
- all four semantic FC03 page-response guards;
- EXP388 recovery-safe partition.

It deliberately does **not** claim to execute the ESPHome binary.

## Regression result

Total host checks executed:

**4630 / 4630 PASS**

This includes:

- PROTO54 golden capture suite: PASS;
- PROTO46 representative runtime/fault decisions;
- 03E8 stale-cache, response-budget, word-index and refresh-only fail-closed guards;
- all four selector paths;
- explicit state7 delayed-rearm vs runtime-only distinction;
- exhaustive EXP388 recovery classification across all 4,608 engine-state tuples;
- PROTO57 reachable-state sole-owner invariant.

Recovery partition totals:

- modeled recoverable tuples: **1296**
- modeled refused tuples: **3312**

## Observed facts

- the source-transcribed engine reproduces every tested current decision vector;
- no tested fail-closed branch becomes permissive;
- delayed-refresh state7 remains distinct from runtime-only state7;
- all reachable PROTO57 states remain sole-owner safe;
- the generic source behavior still reproduces known broad `0870` and `085F` ACK permissions rather than silently applying future hardening.

## Strong conclusion

The gap between the prose/formal model and current source logic is now reduced one step further: the important authorization predicates exist as executable host regression logic and agree with the existing golden/fault/reachability assets.

## Limitation

This remains a **manual source transcription**. It is not compiled ESPHome/C++ and therefore cannot prove compiler behavior, C++ object lifetime, UART scheduling, timing races or exact lambda integration.

## Live status

Unchanged.