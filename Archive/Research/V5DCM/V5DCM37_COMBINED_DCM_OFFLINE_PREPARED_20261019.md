# V5DCM37-COMBINED-DCM-OFFLINE-01 — experiment contract
**Status: PREPARED / NOT RUN.** Initiated 2026-10-19 by user request to combine as many *offline* native-DCM research tracks as feasible while preserving independent negative tests.

## Baseline and past observations
- **Verified on-device baseline** V5DCM33-FIX-B2-LIVE-PASSIVE-01 COMPLETE / POSITIVE: 204 s stable B11D 2342/B11C 2345 parser parity, HA temperatures, software HARD_DENY 393/393, UART writes=0, software DE=0. User-attested B2 flash, runtime B2 tag; exact flashed binary hash unverified. Fallback V5DCM23 FIX2 RX-only.
- Exact user-private FIX-B2 ZIP SHA256 `fdc09c5927b5a351163db95db96dc467abd43cb27e1e7fc8068782bea4a677c7`. Private Core ticketed/mutable, byte/API divergent from firmware repository HEAD; never graft public HEAD adapter defaults into B2.
- V5DCM34 source map COMPLETE/POSITIVE offline; V5DCM35 model-only approval/mock-delivery 192+18 host checks COMPLETE/POSITIVE offline; V5DCM36 private pinned B2 Core/output disable source+host 53/53 etc COMPLETE/POSITIVE offline.
- Historical V4.1 EXP386 and EXP387 COMPLETE/POSITIVE local, EXP388 RUNNING/PARTIAL. Original V5DCM32 actual restart RX-rejoin COMPLETE/NEGATIVE due B11D `RAW_INCOMPLETE_AT_IDLE` before 12.923s gap. FIX-B post-gap RX cohort COMPLETE/POSITIVE, fixed historical retention B2 source offline but B2 new live post-gap >90s NOT RUN.
- Connect 2.1.105 AppFS native 0x0F internal handshake states, cold-32 vs 33-profile-significant group readiness, mailbox/semantic/Online are separate. No new genuine DCM module for captures.

## Hypothesis
One **standalone, physically nontransmitting** evidence coordinator can reconcile *five separately asserted axes*, without introducing a second UART parser or treating mock success as real DCM acceptance:
A) FC23 observed → mock delivery → FC16 first-page *internal shadow* (modern 03E8/count14);
B) fresh vs retained vs recovery as **different observations**, no universal 32/32 cold requirement and no false retained 085F-as-handshake;
C) fail-closed original B11D/P5 historical faults, CRC/boundary, generation, source, responder conflict, stale request and budget/expiry;
D) actual current profile 33 significant W2/W3/W4 group geometry matched from the exact B2 V5DCM22 static source, separate from 32 bootstrap/owner;
E) pinned exact private B2 Core decision copy and disabled output sink, with old V35/36 host regressions.

## Exactly one controlled change
Implement a separate **host-only** C++17 coordinator plus tests and reproducible source/archive pinning. It may include *multiple separately tested modules* within the **same offline-only addition**, never live interdependent unknowns. The parent FIX-B2 YAML and all 72+ previous source members remain unchanged; no Arduino/ESPHome include, no UART/GPIO/DE/physical send, no actual response bytes or recovered approval algorithm, no 0x0708 mailbox commands, no semantic register-write logic and no changes to HA Configuration controls. Host mock delivery is an explicit test event; no fake controller acceptance/owner/epoch/ticket leaves that seam. No real writer/driver provided.

## Target and safety envelope
- Read-only classified native `0x0F` canonical FC23 and subsequent CRC-validated `0x0F` FC16 first-page + selected 33 profile-page shapes from actual B2 source. Recognize 03E8/count13 as a historical **negative for modern 03E8/count14**, even if chronologically close.
- **No active slave/page/register target**, no outgoing frame/payload/CRC, no transmission timing or retry; all outputs DENY. Input mock time limits if used are host test bounds, never vendor timing or real bus slot proof. No physical controller/ESP actions. B11D/P5 sticky faults must never be cleared.
- Abort/recover: on host test/source pin violation, leaked private algorithm or an output-capable code path, discard this offline addition and retain user-flashed FIX-B2 and original files. No bus recovery needed because no bus activity.

## Required evidence and criteria
- **POSITIVE (offline only)**: exact source SHA pinned; strict C++17 host tests independently exercise A-E, including success + stale/foreign/CRC-corrupt/fragment/generation/conflict/legacy-fault/duplicate/partial/expiry/recovery negative controls; no group reached via arbitrary caller index, source descriptors checked geometrically; no false full C2 for empty/mismatched/unowned group; old V35 192/V36 53 and B2 65 etc rerun; altered parent ZIP rejected; archive integrity/hash verified; no live TX/provider symbols in new code.
- **NEGATIVE**: wrong page or old count13 passes modern group, observed CRC alone creates owner/Online/TX permission, 085F creates retained or recovery acceptance, stale or foreign event survives generation change, missing/duplicate pages auto-complete, old B11D/P5 cleared, new UART or actual output path possible, or test failure.
- **INCONCLUSIVE**: exact source/fixtures missing, test suite not runnable, original reference-Core seven-fixture parity still unresolved. Not all external assumptions can be proven by synthetic tests.

## Report and follow-up
Create a private downloadable nonflashable archive and a **sanitized public result**. Update all 3 canonical Research files with PREPARED then actual RESULT status; never call source creation a completed hardware experiment. Following successful offline results, identify smallest remaining proof for **real native response delivery and controller continuation**; *do not* automatically flash or start a live test. User has authorized controlled TX preparation but every new live test still needs exact privately reviewed frame payload, current controller state, bounded timing/retry, stop/recovery, before physical transmission.
