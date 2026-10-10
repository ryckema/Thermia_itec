# PROTO-OFFLINE-72 — Dead-code / state liveness proof

**Date:** 2026-10-04  
**Status:** **COMPLETE / POSITIVE — DEAD AND TRANSITIVELY UNREACHABLE WRITER STATE IDENTIFIED**  
**Hypothesis:** static read/write and enabling-state analysis can distinguish safety-critical live state from obsolete experiment scaffolding in Write Beta v4.1.  
**Controlled change:** source analysis only. No YAML modification, compile/flash, or bus TX.

## Baseline

Audited source blob:

`8e8a82689e53528a8b751a1abbd901f683b6b238`

Current `globals:` section contains **342 globals**.

A complete lexical read/write scan classifies:

- **239** globals with at least one control-flow-style read;
- **91** additional active-data globals;
- **12** globals with writes but **zero reads**.

The control/data split is conservative because syntax alone cannot perfectly distinguish HA presentation logic from protocol control. The **zero-read and constant-assignment findings below are exact source facts**.

## Definite write-only globals

Twelve globals are assigned but never read anywhere in v4.1:

1. `write_extra_delta_words`
2. `write_request_word_index`
3. `write_request_register`
4. `write_request_target`
5. `write_request_generation`
6. `write_pending_generation`
7. `write_last_confirm_ms`
8. `write_hot_rejoin_armed`
9. `write_hot_rejoin_tx_ms`
10. `write_hot_rejoin_challenge_baseline`
11. `write_boot_observation_15s_noted`
12. `write_boot_observation_complete`

These variables cannot influence a current TX decision because no read exists.

Important nuance: for `write_extra_delta_words`, the **global copy** is dead; the local `extra` calculation used to detect confirmation deltas must remain.

## Constant-state findings

### Pending queue surface

`write_pending_valid`

- initial value: false
- source assignments: false only
- assignment to true: **none**
- reads: diagnostic sensors / status context

Therefore the old `Thermia Write Queue Pending / Queued Register / Queued Word / Queued Raw Value` surface can never represent a live pending transaction in current v4.1.

Associated values remain constant defaults:

- `write_pending_word_index = 0`
- `write_pending_register = 03E8`
- `write_pending_target = 0`

This is obsolete queue telemetry, not live transaction state.

### Stalled-export resume experiment

`write_resume_armed`

- initial false
- all source assignments false
- no assignment true

The only branch that can set `write_resume_started=true` is:

`if (write_resume_armed && !write_resume_started)`

Therefore it is statically unreachable in current v4.1.

Consequence: the physical `04A6` resume ACK TX site inventoried by PROTO61 **exists in source but cannot be reached from current source state**.

The downstream resume state (`started`, `done`, `start_ms`, `expected_index`, `pages_acked`, runtime-interleave handling) is therefore historical experiment scaffolding in the production core.

This refines, but does not erase, PROTO61: PROTO61 counted physical TX sites; PROTO72 adds reachability.

### Historical hot-rejoin branch

`write_hot_rejoin_in_progress`

- initialized false
- all assignments false
- no assignment true

`write_hot_rejoin_sent` is likewise source-constant false.

The branch after `06F1` that would set:

- `write_hot_rejoin_export_complete=true`
- `write_hot_rejoin_wait_runtime=true`
- hot-rejoin completion timestamp/state

is guarded by `if (write_hot_rejoin_in_progress)` and is therefore unreachable.

The later hot-rejoin runtime qualification branch is transitively unreachable as well.

This is separate from the **current EXP388 controller-restart recovery**, which uses `write_recovery_in_progress` / `write_recovery_attempted` and remains live/safety-critical.

## Safety-critical state confirmed live

Do **not** remove or merge away semantics of:

- `write_write_state`
- `exp378_state`
- `exp379_state`
- `exp380_state`
- `write_delayed_refresh_pending`
- `write_recovery_in_progress`
- `write_recovery_attempted`
- parser resync/drop baselines and counters
- peer FC17 / peer FC16-ACK counters
- authoritative page cache validity/timestamps
- semantic response counters

These state variables participate in actual authorization/recovery decisions.

## Cleanup classes

### Safe source-dead candidates

The 12 zero-read globals are the strongest removal candidates.

### Safe obsolete telemetry candidates

The `write_pending_*` queue surface is source-constant/inert and can be removed together with its HA diagnostic sensors.

### Historical experiment code to move, not silently delete from history

- stalled-export `write_resume_*` machinery;
- dead `write_hot_rejoin_*` branch.

Their historical purpose should remain in experiment records, but they do not need to remain in a future production core.

### Must stay until separate live/refactor validation

- EXP388 recovery engine;
- semantic page engines;
- integrity guards;
- current ACK policy.

## Strong conclusion

PROTO64's cleanup hypothesis is now strengthened by source liveness evidence:

> substantial parts of v4.1 are not merely “old-looking”; they are statically unable to influence current protocol behavior.

A future clean core can remove/archive this state without needing to preserve impossible runtime paths, provided the structural refactor still passes PROTO54/60/61/62/63/67/68 and an actual ESPHome compile.

## Limitations

This is static source-level reasoning. It assumes no external mechanism mutates ESPHome globals behind the YAML-generated code. For ordinary ESPHome globals that is a sound project assumption, but generated-code inspection would be the next layer if absolute binary proof were required.

## Live status

Unchanged: EXP387 COMPLETE / POSITIVE; EXP388 RUNNING / PARTIAL; EXP383 PREPARED / NOT RUN.