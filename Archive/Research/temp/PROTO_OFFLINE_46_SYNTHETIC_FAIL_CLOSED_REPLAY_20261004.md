# PROTO-OFFLINE-46 — Synthetic fail-closed fault replay

**Date:** 2026-10-04  
**Status:** **COMPLETE / POSITIVE WITH THREE BROAD ACK SURFACES CONFIRMED**  
**Scope:** offline reference-model + source-predicate regression only. **No bus TX, no YAML change, no compile/flash, no reboot and no setting write.**

## Hypothesis

Write Beta v4.1 should fail closed when a protocol-valid but semantically/state-invalid frame is injected at the major native state boundaries. Previously identified broad ACK permissions should appear explicitly rather than being hidden by aggregate capture statistics.

## Baseline

- Canonical project state on GitHub: through PROTO-OFFLINE-44, blob `73ca337d276d50416fa3110c65c82bff6a9b254e`.
- PROTO-OFFLINE-45 local result: executable trace replay found the core native model reproducible but refined it into overlapping dimensions rather than one strict enum.
- Write Beta v4.1 blob: `8e8a82689e53528a8b751a1abbd901f683b6b238`.
- No baseline file was modified.

## Exact controlled change

A synthetic fault suite was constructed from **real genuine capture frames** and state predicates copied from the current v4.1 branches.

Each raw frame mutation remains **Modbus-CRC valid** so the test targets application/state authorization rather than merely exercising the CRC parser.

Fault classes:

- unknown/wrong-count runtime FC16;
- unknown and duplicate `085F`;
- unqualified `0870`;
- standalone configuration page;
- `04A6`, `0834`, resume-order and post-export `06F4`;
- unexpected/wrong/stale/repeated FC03 desired pulls;
- repeated `0708` during semantic wait;
- no-op, exact republish, original-value republish and extra-delta republish;
- controller loss before/after the semantic boundary and second-loss handling.

The replay is a **branch-faithful shadow model**, not ESPHome binary execution. Therefore this is stronger than prose review but is **not compile/runtime verification**.

## Results

**29 deterministic scenarios** were executed.

- **21** -> `STOP/NO_ACK`, `STOP/NO_RESPONSE`, capture-only or equivalent fail-closed behavior.
- **2** -> recoverable controller-loss branches cancel intent and re-enter cold-start without immediate semantic value TX.
- **1** -> exact republish closes without another TX.
- **1** -> expected/authorized positive-control transmission.
- **4** -> the current v4.1 intentionally/broadly ACKs the injected frame.

## Fail-closed paths confirmed

The shadow replay confirms:

1. unknown FC16 page -> **NO ACK + stop**;
2. correct address with wrong count -> **NO ACK + stop**;
3. `085F/count5` with unrecognized payload -> **NO ACK + stop**;
4. unarmed runtime `04A6/count13` -> **capture-only, no ACK**;
5. `0834/count18` -> **NO ACK + stop**;
6. out-of-order page during export resume -> **NO ACK + stop**;
7. unrequested `06F4/count19` in the post-export discriminator window -> **NO ACK + stop**;
8. unexpected external FC16 ACK -> abort, no new TX;
9. unexpected FC03 page or wrong FC03 count -> **no response + stop**;
10. desired FC03 with cache age `300001 ms` -> **no response + stop**;
11. second semantic response attempt -> **no response + stop**;
12. desired pull for unauthorized 03E8 word index -> **no response + stop**;
13. FC03 desired-page pull during refresh-only state -> page response withheld and semantic TX disabled;
14. new `0708` while waiting inside the semantic transaction -> **no response + stop**;
15. controller republish of original selected value -> **NEGATIVE / disabled / no retry**;
16. republish with unrelated extra delta -> **INCONCLUSIVE / disabled / no retry**;
17. bus loss after semantic-selector boundary -> recovery refused, **TX=0**;
18. second bus loss after a recovery attempt -> stop, no second recovery.

## Positive controls

- exact expected `03E8/count14` FC03 pull with valid cache/word/budget -> exactly one desired-page response is authorized;
- exact target republish with zero extra deltas -> transaction closes positive;
- fresh current page already equal to target -> **NO semantic TX**.

These controls matter because the suite is not a blanket “everything must stop” test.

## Three broad ACK surfaces confirmed

### 1. Known `085F` payload is ACKed without an additional service qualifier

A valid all-zero `085F/count5` in stage40 reaches generic `local_runtime_ack_proven` and is ACKed.

A duplicate of the same known frame is ACKed again; there is no duplicate one-shot suppression at this branch.

**Classification:** broad ACK surface / hardening candidate, **not proven XTR defect**.

PROTO45 matters here: genuine ATEC/DCM03 also ACKs a steady-state `085F`, so a universal “service-only” rule would itself be wrong cross-profile.

### 2. `0870/count17` is ACKed from shape alone inside stage40

The FC16 handler does not require a preceding answered mailbox before the generic `0870` ACK.

**Classification:** broad ACK surface / strongest remaining hardening candidate.

The genuine legacy reconnect evidence remains asymmetric: 31 repeated `0870` frames are deliberately unACKed before one transition ACK. This gives the strongest reason to investigate local XTR qualification.

### 3. Known configuration page `03E8/count14` is ACKed in stage40 without an owning refresh/confirmation state

Generic `local_config` is sufficient unless a special resume guard is active.

**Classification:** broad ACK surface / profile-ambiguous hardening candidate.

PROTO45 showed genuine legacy Online performing standalone ACKed `03E8` pushes with `W2/W3=0`, so “always require W2/W3 ownership” cannot be promoted to a universal protocol rule.

## EXP388 static branch result

Two still-unfinished EXP388 branches were exercised **only in the shadow model**:

- pre-selector main state `ws=1` + controller loss -> queued intent is cancelled and cold-start recovery is entered with no immediate semantic value TX;
- current-refresh-only `ws=6` + controller loss -> intent/cache is cancelled and cold-start recovery is entered with no immediate semantic value TX.

The source predicates therefore look internally fail-closed.

**This does not complete EXP388.** The project rule still requires an actual live result/log for those branches.

## Observed facts

- All protocol-frame mutations used in the suite have valid Modbus CRC.
- No malformed unknown page/count reaches a semantic response branch in the shadow model.
- No stale/duplicate/unexpected FC03 desired pull reaches a semantic value response.
- Semantic-confirmation mismatch paths disable retry.
- Semantic-boundary controller loss refuses recovery.
- The only deliberately broad runtime ACK results are the already-known `085F`, `0870`, and generic known-config allowlists.

## Strong conclusions

1. v4.1's **semantic write machinery is strongly fail-closed** against the tested single-fault mutations.
2. The safety debt is concentrated in ACK authorization rather than value injection.
3. `0870` is the cleanest candidate for a one-variable future hardening experiment.
4. `085F` and generic config-page hardening require more care because PROTO45 proves genuine cross-profile behavior is broader than strict predicates.
5. The remaining EXP388 cancellation code passes offline source-model regression but remains **RUNNING / PARTIAL** until live-tested.

## Hypotheses / not proven

- A locally correct `0870` qualification predicate is still unknown.
- Duplicate `085F` ACK may be harmless/required on XTR; current evidence cannot decide.
- Standalone XTR config-page ACK may be legitimate in some controller-originated update context.
- The shadow model does not prove compiler/runtime behavior, race behavior or parser scheduling under real ESP32 timing.

## Safety consequence

Do **not** change all three ACK surfaces together.

If a hardening live experiment is prepared later, the safest sequence is:

1. finish EXP388's two remaining live cancellation branches;
2. test one ACK policy at a time;
3. keep `0834` capture-only;
4. keep unknown payload/page/count fail-closed;
5. do not relax semantic cache/value guards based on this experiment.

## Live state

Unchanged:

- **EXP387 — COMPLETE / POSITIVE**
- **EXP388 — RUNNING / PARTIAL**
- **EXP383 — PREPARED / NOT RUN**