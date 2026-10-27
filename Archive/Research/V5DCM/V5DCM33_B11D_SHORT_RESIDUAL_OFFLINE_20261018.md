# V5DCM33 — B11D short-residual integrity audit (2026-10-18)

Status: **COMPLETE / POSITIVE** for finding a source-level deferral asymmetry; **no recovery implementation or live validation**. Follow-up V5DCM33-FIX-A **PREPARED / NOT RUN**.

## Inputs / provenance
- User-supplied `V5DCM32_RX_REJOIN_INTEGRATION_OFFLINE_NOT_FLASHED(1).zip`: examined source in `waveshare-thermia_V5DCM23_REAL_LEDGER_PREPARED_NOT_FLASHED.yaml` and `v5dcm31_accepted_risk_session_policy.hpp`.
- Canonical V5DCM32 live result: user confirmed manual power cycle; 22:02:23 ARM, 22:02:30 first B11D `RAW_INCOMPLETE_AT_IDLE`, 22:02:43 12923 ms callback gap, 22:02:45 FC23; later denial verdict 5 BadIntegrity, localGen 0, native package ledger revoked 0/0.
- No new raw log, controller experiment, flashed binary, compile, or physical bus operation in this step.

## Observed source facts
1. The B11D 50 ms scheduling lambda returns immediately on `b11d_fault` (YAML source line ~4000): the error is intentionally sticky.
2. Once the RAW FIFO is nonempty and 25 ms quiet has elapsed, the independent splitter checks the remaining bytes; when fewer than five remain it calls `first_fault("RAW_INCOMPLETE_AT_IDLE")` **immediately** (~4091–4095).
3. The separate, already-existing maximum 250 ms incomplete-fragment deferral applies only to a *later* path, when the residual is at least five bytes, CRC candidate length exceeds available bytes, and V5 pending metadata exists (~4111–4131). It does **not** cover 1–4-byte residuals.
4. `first_fault` latches `b11d_fault=true`; its diagnostic snapshot preserves aggregate lengths and never reveals payload bytes (~4025–4087). Once latched, the scheduler cannot observe later clean raw windows as evidence for requalification.
5. V5DCM31 source revokes the active accepted-risk scope on `!crc_valid || !rx_integrity_healthy` (~122–123). V5DCM32 properly forwards `integrity_healthy`; the denial is expected.

## Strong conclusion
The source has an **asymmetric treatment of incomplete RAW residuals**: short fragments are immediately fatal after a 25 ms quiet observation, whereas longer recognisable incomplete fragments may be deferred up to 250 ms. This is a source-level candidate explanation for a nonrecoverable rejoin after an interrupted UART frame. The exact runtime bytes and V5 pending context that triggered 22:02:30 were not reproduced in this audit; the root cause of that specific physical event remains **UNKNOWN**.

## V5DCM33-FIX-A — PREPARED / NOT RUN
Hypothesis: bounded pre-fault deferral and explicit post-intervention RAW integrity qualification can distinguish a transient 1–4-byte truncation from persistent receiver corruption, without treating bad CRC or malformed frames as valid.

- Baseline: actually flashed V5DCM32 RX-only; retain FIX2 known-good rollback; keep all production entities, B11C/B11D diagnostics, physical DE LOW and TX HARD_DENY.
- One controlled code family: **RX-only short-residual/epoch qualification**. Avoid clearing the sticky fault by time alone. Prefer defer-only for 1–4 bytes *only where an unfinished V5 fragment is independently visible*, capped by the existing 250 ms deferral budget; if no verified progress/expiration occurs, hold remains. Any subsequent fresh-scope reset/requalification needs an independently testable clean post-gap window and explicit policy, not a unilateral counter clear.
- Offline positive: exact original source host fixtures for fragmented 1–4 bytes and valid CRC completion do not prematurely fault; truly orphaned 1–4 bytes, timeout, CRC mismatch, cross-stream mismatch, duplicate/stale FC23 and TX/DE violations fail closed; baseline clean captures unchanged.
- Negative: any unqualified fragment or repeated corrupt window reaches an accepted rejoin, or a diagnostic hold is silently cleared.
- Inconclusive: only compiler or synthetic tests pass but no original observed fault-context replay is available.
- Abort/recovery: offline only initially. If later user-initiated live testing is approved within a defined experiment, on bus-health/HA regression or nonzero TX/DE restore verified known-good RX-only FIX2; don't automatically request another controller restart.
- Protected scope: no `0x0F` emulation, `0x0708` mailbox implementation, credential/security material, or TX code.

## Next
Reconstruct original first-fault metadata (`FIRST_FAULT_DIAG`, `FIRST_FAULT_META`, pending V5 length/candidate data) from the supplied 22:02 log if available. Implement and host-test the minimal short-residual deferral, separately from any runtime fault-clearing design. No live retest yet.
