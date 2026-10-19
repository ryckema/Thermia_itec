# V5DCM47 — FIX2 cold-return one-shot preflight (2026-10-19)

**Offline V5DCM47-RX-GAP-HOST-01: COMPLETE / POSITIVE — 19/19 actual exact-header C++17 assertions.**
**Separate V5DCM47-LIVE-ONE-SHOT-01: PREPARED / NOT RUN.** No Arm, controller intervention, flash, physical TX or settings write.

## Hypothesis and baseline

FIX2 is locally proven for 178.8s receive-only: 0 resync/drop/B11D fault, stable QUALIFIED, live HA, 0 native FC23 and 0 TX. Original FIX1 startup bug corrected. Historical local XTR G01-09 had one documented controller power intervention, a ~11.944s callback gap and 24 native 0x0F FC23 retries; it is historical evidence, not the current state. Known-good output-disabled rollback V44B.

**Exactly one controlled offline change:** execute source-pinned FIX2 FreshRx witness with a 12-second gap and first resumed CRC-valid frame. No changes to ESPHome YAML, private response backend, UART, physical controller, HA entities or experiments. PIN ZIP SHA256 9a709b5e4a53d05ced25e59310bc0b87f6c794a685a32ed18fa9ccdc432ca3ef, exact header SHA256 e052c9181c0dca79fc0fdab4ab8202a73e494aa9c238a637815355959493513c, user FIX2 log SHA256 856d5da48c7870d54b151f022fcdc6837fb6f92ea24ef5818e2e9ad0b555a7f2.

## OBSERVED OFFLINE RESULTS

Strict g++ C++17 -Wall -Wextra -Werror -pedantic tests PASS: 19/19 assertions. Waiting B11D startup stays WAITING; after 30s and at least 100 new complete frames, QUALIFIED and current=1; after 12s with no RX callback, current=0 but phase remains QUALIFIED; one new valid frame, if B11D-ready and otherwise healthy, restores current=1. Stale frame >3s prevents current approval. New drops, true integrity error or B11D readiness loss irrevocably REVOKE. This is tested original FIX2 FreshRx code, not an invented model. Does not test physical gap effect on B11D original RAW supervisor.

Source review of the existing one-shot actor: once successfully armed, the wait window is 30s; while Armed, 2ms tick times out on expiry but does not transmit during temporary RX staleness; current RX is rechecked with new CRC request; max one successful Arm per ESP boot, one reply, 70ms callback-relative response budget. Do not mistake 70ms since callback for independently measured wire EOF. Real B11D RAW idle fault may latch across a controller gap and then forbid a reply. This is OPEN until actually tested, NOT guaranteed by 19 host assertions.

## Bounded first native LIVE experiment — PREPARED / NOT RUN

**Hypothesis:** during a single separately user-initiated and documented controller cold-return, exact native slave 0x0F FC23 request may be answered once by the existing guarded private dynamic backend without damaging RX/HA, possibly resulting in controller-owned FC16/0708 continuation. This does not itself prove genuine Online/C2 or semantic acceptance.

**One change:** only a single native one-shot manual Arm plus one normal controlled controller return in a reviewed scope, no extra YAML edit or independent bus write. Historical G01-09 already demonstrated a cold request; no need to repeat a standalone RX-only restart.

**Target and response:** ONLY slave 0x0F controller-origin FC23 canonical geometry, read 0x0730/count8 and write 0x071C/count8. Controller challenge bytes/current values are unknown until newly received; no separate controller register is being written by ESP. Only the validated private request-dependent 21-byte RTU response geometry (FC23, 16 dynamic data bytes and CRC) may be emitted; no static guessed payload and no publishing security implementation. If live dynamic payload cannot be proven from exact current CRC-good request, deny output.

**Limits:** Arm after local FIX2 current QUALIFIED, one 30s window; one reply only, no automatic retry; 70ms completion budget relative to completed parser callback. Historical ~12s gap plus ~1s until first request makes the window plausible but does not prove timing.

**Risks and abort:** heat/DHW briefly interrupted during normal controller power transition; incomplete RAW frame/B11D sticky fault; competing responder/unknown electrical slot, DE high/collision, stale epoch or response rejected. Abort at first fresh parser resync/drop, B11D sticky or B11C CRC issue, unexpected DE high / peer response / production HA loss, controller alarms or operator concern; use Configuration Abort Native TX and verify DE LOW, fall back to known-good V44B NO TX as needed and normal recovery.

**Positive:** one actual current native FC23, permitted single response, DE returns RX, parser remains healthy and controller later issues new stage-specific FC16/0708; separately classify whether semantic acceptance occurred. **Negative:** full verified response sent but no expected advancement. **Inconclusive:** no challenge, timeout, early veto/fault or incomplete attribution. No live state transitions before user runs and supplies evidence. Minimum log: FIX2 phase, user Arm status, V44B actor attempts/UART, V45 B11D owned/unsafe, P74E 0x0F FC23, parser/faults, post-response FC16/0708, and short controller-switch timestamp. One user-initiated test only. Do not repeat without evidence review.

## NEXT
Leave current FIX2 unchanged. Review this prepared scope before any live Arm; a fresh current XTR challenge plus bounded one-shot reply is now the most discriminating new physical evidence. Never interpret RX QUALIFIED or firmware-internal ACCEPTED as native ownership or Online. Full ESPHome compile and actual physical TX not executed in V47.
