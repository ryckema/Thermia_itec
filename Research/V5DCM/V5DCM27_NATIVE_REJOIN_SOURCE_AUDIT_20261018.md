# V5DCM27-SOURCE-REJOIN-01 — V4.1-to-V5 lifecycle integration gap, exact FIX2 host regression

**Status: COMPLETE / POSITIVE for SOURCE/HOST diagnostics only**, 2026-10-18. **V5DCM27-REJOIN-BRIDGE-01: PREPARED / NOT RUN** (design, no source patch deployed). **Current XTR V5DCM23 FIX2 still RUNNING / PARTIAL** based on the user's short live 1/33 log. No device flash, native output, controller restart or Home Assistant modification during this step.

## Hypothesis / baseline / one controlled action

**Hypothesis:** the actual private V5DCM23 FIX2 has an RX-only, fail-closed but **one-way package requalification gap** following FC23, preventing the portable 33-package ledger from resuming inside the same ESP process. This is separate from the real native session/owner proof problem, and is important for planned V4.1-inspired cold/retained/recovery integration.

**Exact source baseline:**
- User's private FIX2 ZIP SHA256 `561169c31d5a7eb341055fdb37d0302b4816d661fff9cd2df9d607a9498ea9a4`; internal YAML SHA256 `04f562e2ccf5374ca890c5f107ee38e1fa108251dc80926cc3ba12c85004ed13`. **This ZIP is not independently byte-authenticated as the flashed binary.**
- Private header `v5dcm23_v5dcm19_real_ledger.hpp` SHA256 `[see private archive]`: an adapter around actual source-defined `PassivePackageLedger`, not a guessed reimplementation.
- Public original Write Beta v4.1 YAML Git blob `8e8a82689e53528a8b751a1abbd901f683b6b238` and [Write Beta recovery documentation](../../Write%20(Beta)/README.md). EXP386 cold-start recovery + EXP387 delayed service recovery are **locally positive**; EXP388 two restarts recovered, but some cancellation branches remain untested, thus **RUNNING / PARTIAL**.
- Firmware-repo `data/cm930_state_machine_transitions.csv`, `data/cm930_readiness_gates.csv` and `data/xtr_v41_tx_route_to_reference_core_matrix.csv` support a functional gap map. Original Connect 2.1.105 `cm/modbus_server15.py` and `client.py` support independent handshake, initial device-info, parameter request, operation, and current/desired-update phases. Firmware internal `HandshakeState.ACCEPTED` is not physical owner/epoch/Online proof.

**One controlled change** was to add two **host-only executable regressions** against the unmodified user's private header source. This step did not modify the ZIP, V5 C++ or YAML.

## A. Source-observed one-way ledger invalidation — reproduce against exact code

Verified call sites in the user's FIX2 YAML:
- `v5dcm23::ledger().reset_for_xtr242()` is invoked **exactly once**, during `esphome.on_boot`.
- `v5dcm23::ledger().on_native_crc_validated_bytes(f.bytes, v5dcm22_rx_clean)` is invoked once on the EXISTING completed CRC-valid V5 callback.
- The private adapter calls `invalidate()` on **any** native slave `0x0F` / function `0x17`, not only source-validated canonical FC23; `invalidate()` revokes ledger state, clears the selected profile and increments local generation.
- An invalidated ledger does **not** automatically reselect a valid source profile when additional FC16 pages arrive. No additional reselect call appears elsewhere in this YAML.
- This revocation behavior is fail-closed and **must not be 'fixed' by guessing a physical controller epoch or automatically asserting Online/owner**.

**Host test 1 (exact V5DCM1 shadow header, strict C++17): PASS**, 11 scoped invariants. An RX response-shaped event alone can seed `RESPONSE_OBSERVED`; after a qualifying FC16 the V5 observer can report `ACCEPTED_SHADOW` without verifying the modern XTR word-count for that register page and without proof that the ESP sent a native response. Test additionally covered alarm/buffer exclusions, repeat challenge, reset, foreign slave and out-of-context response. This is **intentional permissive software observation**, not a TX authority bug by itself. Private source SHA256 `43aa7c72aa5f9fcb9311d7b237e7371193bcc51ecccf7e019d286c38b1b90c06`.

**Host test 2 (exact FIX2 `NativeRxLedger` and portable decoder, strict C++17): PASS.** Profile configured once; a synthetic complete CRC-good `03E8/count14` data page is recognized 1/33. A CRC-good `0x0F FC23` boundary revokes the profile. Subsequent identical CRC-valid FC16 stays 0/unconfigured, until an explicit source `reset_for_xtr242()` call. This was executed **twice**: once with a private synthetic 0x17 CRC frame, and independently with the **unaltered first CRC-valid native 0x0F FC23** automatically extracted from the real user capture `thermia_capture_20261003_165355.log`, SHA256 `14918065297264473e2357822a8694d184e7821b8c2a3b1cb316039678a708a1`. Actual historical challenge bytes and confidential private emulation details are **not included** in this public document. Test code SHA256 `622424bf0fe2ca469e1b881d4c4f1278f031fcd63415de29b7c87073d5ad532a`. The test uses actual existing C++ decode and CRC source, with `g++ -std=c++17 -Wall -Wextra -Werror -pedantic`.

**Important provenance limitation:** the 20261003 raw frame is historical XTR/source input, not a fresh FC23 observed in currently flashed FIX2. The **latest actual FIX2 live 2m25 capture had 0 observed native FC23 boundaries**, so the new rejoin defect does **not** explain that recorded 1/33. The host evidence proves the conditional code behavior, not that this branch has happened in present live operation.

## B. Functional merge mapping — original Connect and Write Beta v4.1 versus V5 FIX2

| Lifecycle feature | Original / previous local evidence | V5 FIX2 implementation state | Required next integration change |
|---|---|---|---|
| Native FC23 response and handshake | Original firmware distinguishes response-sent from later internal accepted; EXP386 proves bounded guard-dependent cold re-entry on this XTR | V5DCM1 and V5DCM2 record **shapes**, no active responder or proof of having sent | Reuse existing user-proven guarded response-owner seam **only in private, separately armed future live implementation**; no public payload/algorithm. |
| Cold-start full settings receipt | Local EXP386 historical ordered XTR 32-page/ACK sequence | R6 Stage D 32/32 observer + 33-profile ledger, independent | Join session context and distinguish transport 32/32 versus semantic profile 33/33; never merge these into a single acceptance boolean. |
| Retained/hot rejoin | V4.1 explicitly observes service without necessarily replaying the full 32-page cold path; EXP388 shows two recoveries but incomplete cancellation branch coverage | R6-P74BC/C G shape observers remain no-owner and no-TX, Stage D can be held | Add explicit fresh/retained/recovery lifecycle *integration* sourced from existing observer, never require cold 32/32 for legitimate retained-state *classification* or bypass a HOLD for output. |
| FC23 package requalification | Controller/session transition demands a source-qualified new context | **Confirmed stuck until on_boot reselect** in current FIX2 RX ledger | Design a **separate externally qualified reselect API** with explicit profile+controller generation provenance; reject naive immediate reselect merely on FC23 or a 5s gap; preserve deny and diagnostic history. |
| Requested packages | 2.1.105 has independent W2/W3/W4 request/receipt cycle; V5DCM25 matched old XTR and Eco5 bursts | Passive ledger 1/33, boot-selected *source profile*, current native request state unknown | Join already-owned events/metadata, do not invent request, mailbox or active 33/33 receipts. |
| Mailbox and runtime | EXP387 delayed mailbox re-arm restored native Room Setpoint operation; genuine request event and fresh-page semantics distinct | Multiple V5 observers, but no joined native response authority | Leave service and TX decision gated; avoid cloning many old per-page TX blocks into new V5. |
| Semantic write and cancellation | V4.1 verified one-word/fresh-page controller re-publication; EXP388 pre-semantic / refresh cancellation scenarios still not all live | No native V5 semantic engine; public reference Core models stages | Reuse proven transaction ownership/rollback rules, but no writes before independent owner, fresh page and semantic-return evidence. |

## C. Decision and exact next controlled step

**OBSERVED FACTS (source + host):** the current FIX2 native 33-group RX ledger is deliberately one-way invalidated after any native 0x17; the sole YAML reselect is on ESP boot. The V5DCM1 `ACCEPTED_SHADOW` can be true without local response ownership, correct page geometry, or native acceptance; it must remain a diagnostic, not permission.

**STRONG CONCLUSION:** to progress to a reliable native DCM session, a single ownership/epoch-aware lifecycle integration bridge is more valuable than yet another page census, and is necessary for rejoin after initial challenge. Prior V4.1 proof can guide bounded guarded behavior, but is **not automatically transplanted** to V5.

**HYPOTHESES:** a validated source+session reselect hook will allow the V5 ledger to resume its RX-only collection safely after a genuine new session; the cause of live 1/33 may involve missing controller request activation, still unproven.

**UNKNOWNS:** exact deployed ZIP hash, electrical owner and response slot, full new session acceptance, local output authorization, whether real FIX2 ever encountered FC23 after log, true current rejoin behavior, actual old R6 first D=4 cause, 180-vs-262 HA entity mapping and metadata.

**Next: V5DCM27-REJOIN-BRIDGE-01 — PREPARED / NOT RUN.**
- **Hypothesis:** the existing V5 receive completion callback and established portable ledger can share a **one-way, externally authorized** requalification interface for cold/retained/recovery transitions without introducing a second parser, silently clearing the R6 hold or producing bytes.
- **Known-good:** exact private FIX2 archive and current user-flashed FIX2-as-observed, existing production 180 entities, 17 periodic tasks; separately preserved full v31/RX33 262-entity candidate remains NOT RUN.
- **Relevant results:** V4.1 EXP386/387 COMPLETE/POSITIVE, EXP388 RUNNING/PARTIAL, V5DCM19/20 passive positive; V5DCM23 FIX2 live partial; V5DCM25/26 offline positive; this V5DCM27 two exact-source host regressions.
- **One proposed controlled change:** add a *nontransmitting* explicit epoch/profile-reselect seam and blocked-state diagnostics to existing native lifecycle adapter, separate source-only review. It must require an **external, independently justified session/profile selection**. In the absence of that proof, remain profile-revoked and TX HARD_DENY. Keep on-boot behavior and unrelated V5 functionality byte-identical wherever possible. Avoid automatic rearm on generic FC23, old host gap, or ESP reset.
- **Target:** existing native `0x0F` FC23 boundary classification and strict 33-package RX ledger; **no write page/register, no outgoing payload, no actuator effect** in this step.
- **Positive offline:** after a host-supplied independently-qualified new session marker, ledger can resume under NEW provenance; without marker remains unconfigured; no duplicated/old pending group carry-over, no owner/TX flags; source/static HA inventory preserved.
- **Negative:** data requalification from untrusted FC23 alone, stale epoch or stale controller page, lost production source IDs, new TX path, false Online/C2.
- **Inconclusive:** no trustworthy external ownership/epoch evidence exists; candidate may remain fail-closed, must not fabricate proof.
- **Abort/rollback:** source-only branch is not deployed. On eventual device run stop on any new TX/DE high, parser fault, lost HA telemetry or unexpected controller behavior; rollback separately verified RX-only FIX2/V5 lineage. No request for compiler output without a specific need.
- **Required evidence:** strict host fixtures covering cold, retained, restart/recovery, FC23, source transition, missing/duplicate packets; later user-specific original reboot/session evidence for ownership. **Do not mark live COMPLETE without actual device results.**

Later separate V5 native-TX activation must be user-initiated and bounded, with exact private response payload, current owner/slot/epoch, precise risk, transmission window, abort and recovery specified *before* any hardware transmission. This report grants no automatic TX.

## Safe private test artifact

Two offline C++ test sources were produced in the private conversation artifacts: `v5dcm27_shadow_regression.cpp` and `v5dcm27_ledger_boundary_regression.cpp`. The second accepts an optional existing raw capture filepath at execution time. Neither includes protected native response calculations, mailbox implementations, credentials or live bus writes. The original private headers and full YAML remain user-owned and **not published**.
