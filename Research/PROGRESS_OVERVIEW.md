# Progress Overview — Thermia iTec XTR M

**Status date:** 2026-10-16 · **Latest user-tested build:** GAP-46C RX-only shadow · **Native V5 transmission:** HARD_DENY.

> Percentages below are **qualitative project estimates**, not measured completion rates. They should not be read as evidence of a working native Thermia Online/DCM session. The figures reflect the current research assessment after GAP-46B/C, not automatic proof of each subtask.

| # | Workstream | Estimated progress | Evidence and remaining gap |
|---|---|---:|---|
| 1 | RS485 communication | **95%** | Stable physical bus reception on XTR M; independent physical TX/DE behavior not yet validated. |
| 2 | Parser and CRC | **96%** | Local raw/portable frame agreement, zero resync/drop faults in recent tests; advanced edge cases remain. |
| 3 | Native protocol understanding | **88%** | FC16 page families, traces and Connect firmware analyzed; owner/epoch and semantic authorization unresolved. |
| 4 | Parameter map | **80%** | Production values and selected words confirmed; extended native pages and type/scale mapping incomplete. |
| 5 | Handshake and session ownership | **55%** | Historical V4.1 challenge path and GAP-46C exact-frame shadow design; no qualified V5 challenge/event or slot ownership locally observed. |
| 6 | Bootstrap / page synchronization | **78%** | Historical 32-page sequence and offline ordering models; current retained XTR traffic is not a newly proven full 32/32 boot session. |
| 7 | Native runtime reading | **65%** | Live baseline operational measurements and retained frames; native extended runtime/accepted-session feed incomplete. |
| 8 | Native data to Home Assistant | **50%** | Working production entities plus RX diagnostics; complete native Online/DCM dataset is unavailable. |
| 9 | Writing settings and readback | **25%** | Historical V4.1 test successes under specific conditions; GAP-46B/C performed **no TX** and prove neither semantic write acceptance nor readback. |
| 10 | Error handling and recovery | **60%** | Live NO-TX timeout/revoke and fail-closed logging confirmed; qualified transaction abort/rejoin recovery untested. |

## Latest live results

- **GAP-46B — COMPLETE / POSITIVE** for manual arm, automatic expiry and post-expiry revoke; **INCONCLUSIVE** for revocation of a pending native transaction.
- **GAP-46C — COMPLETE / POSITIVE** for manual arm, automatic expiry and exact-frame shadow snapshot under an unqualified session; **INCONCLUSIVE** for a genuine qualified FC23 event and active native response. User log: `Pasted text(20261016-184950).txt`. Snapshot: `exact=0 eligible=0 refused=0 reservedState=0 TX=HARD_DENY`.
- **Current bus model:** routine native `0x0F` FC16 `03E8/14` plus `085F/5`; no locally observed qualifying `0x0F` FC23 challenge in the GAP-46B/C windows.
- **Current technical boundary:** A working historical V4.1 response mechanism is not proof that the present V5 stack owns a safe response slot. Native V5 UART writes remain denied.

## Next work

**GAP-46D — PREPARED / NOT RUN (proposed):** Offline correlate genuine existing captures, historical V4.1 handler and exact-frame timing/ownership evidence before any separate authorized active test. No controller restart, genuine DCM module, or HA button is required for that offline analysis.

**Safety:** Keep the known-good GAP-36 RX-only fallback. A future active test requires explicit response address/function/guard, precise slot evidence, one-shot TX budget, abort criteria, and recovery plan.

See [project state](THERMIA_PROJECT_STATE.md), [experiment log](EXPERIMENT_LOG.md), and [protocol findings](PROTOCOL_FINDINGS.md) for evidence classification. Do not distribute private native response bytes or security tooling.
