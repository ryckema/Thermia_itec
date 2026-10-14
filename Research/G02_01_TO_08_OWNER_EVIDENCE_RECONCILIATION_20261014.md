# G02 native responder/work-owner — source-bounded offline reconciliation (2026-10-14)

**Overall gate: G02 OPEN / UNKNOWN — NO-GO FOR NATIVE TX.** This is a documentation and strictly OFFLINE audit of evidence already collected and of the user's new G01-09 RX-only log. No ESPHome compilation, OTA flash, new controller power-cycle, write, native reply, or electrical proof is claimed. Historic G01-09 user performed/recorded power operation is separately reported in [G01-07R/08/09](G01_07R_08_09_CONTROLLER_RESTART_20261014.md).

**Evidence provenance:** original local-XTR logs and user results are distinct from genuine Eco5/ATEC collaborator captures and firmware 2.0.18/2.1.105. Video and user raw log are not published in this repository. Original source SHA-256 for the 4,660-line XTR G01-09 log: `a66541b2c8d91661863c6a315003ef26eb4ca3d8960e324479ff2a43cd8acb2e`.

## Mandatory three-way separation
1. **PHYSICAL_SENDER**: electrically transmitting device. Neither Modbus slave address, CRC-valid frame, short ACK shape, nor software-only TX=0 uniquely identifies the physical sender; an external electrical observer would be required for that claim.
2. **CONTROLLER_WORK_OWNER**: a controller-issued work item genuinely assigned to the current native endpoint in the same controller/session epoch. Controller-owned W0–W4 mailbox request selectors and FC16 geometries identify *request families*, not a proven bus lease.
3. **TX_AUTHORITY**: independent safety decision additionally requiring epoch, ownership, physical EOF, exclusive response slot, FIFO/DE drain and reset fail-low evidence. G02 observer output cannot authorize a reply.

## Previously performed G02-01..07: source-scoped status and new 2026-10-14 recheck

| Work | Current historical result | Limitations and new verification |
|---|---|---|
| **G02-01** | RUNNING/PARTIAL for complete original-XTR evidence replay; bounded typed ledger prepared (POSITIVE within ledger-only scope) | Full original EXP355/386/S11F and EXP419–426 raw streams not independently replayed in this audit; local facts documentary where marked. No physical owner proof. |
| **G02-02** | COMPLETE/POSITIVE for inspected 2.1.105 CM930 handler paths; direct independently repeated 2.0.18-vs-2.1.105 code diff PARTIAL | Slave 0x0F handles controller-driven FC23/FC16 and mailbox work with internal NOT_ACCEPTED/RESPONSE_SENT/ACCEPTED tracking; **NO_EXPLICIT_ON_WIRE_OWNER_LEASE_IDENTIFIED_IN_INSPECTED_PATHS**, not global proof of nonexistence. Comparison source from Thermia_Connect_Firmware reviewed. |
| **G02-03** | COMPLETE/POSITIVE OFFLINE raw genuine cross-model replay | Seven original cross-model capture hashes revalidated 7/7 (prior report). 25,031 CRC-valid frames, 164 FC23 request shapes, 7 response shapes; a bounded Eco5 window contained 41 FC23 requests with NO matching response shape while other bus traffic continued. Cannot identify physical sender or establish permanent absence of responder. |
| **G02-04** | COMPLETE/POSITIVE DOCUMENTARY_ONLY context matrix; complete original local-XTR raw replay INCONCLUSIVE | EXP419 target absent INCONCLUSIVE; EXP420 bounded POSITIVE; EXP423 orphan 0662/33 INCONCLUSIVE; EXP425 COMPLETE/NEGATIVE for required ordered 0683 tail following a one-shot 0662 ACK; EXP426 INCONCLUSIVE. No inference of enduring owner. |
| **G02-05** | COMPLETE/POSITIVE HOST-ONLY passive owner reducer, **not deployed** | Original bundle rerun on 2026-10-14: 38/38 unit tests; 25,031 genuine CRC-good cross-model frames; 4,096 synthetic streams / 131,072 synthetic events / 655,360 DENY invariant checks; no TX permission. Adversarial synthetic tests are not physical experiments. |
| **G02-06** | COMPLETE/POSITIVE OFFLINE diagnostic preflight; optional new live observer SUPERSEDED/NOT RUN | 2026-10-14 source/preflight rerun **16/16 PASS**, only with existing local handover and host reducer. CO, CN, P74L and B6 have sufficient software-observer counters; another flash not warranted. Current as-built binary provenance and electrically measured ESP DE absent. |
| **G02-07** | COMPLETE/POSITIVE OFFLINE formal **G02_OPEN_NO_GO** decision; physical G02 remains OPEN | 2026-10-14 decision script reexecuted **26/26 PASS** using the original documentary snapshots and host test results. This decision cannot authorize an on-device native response. A new video-anchored G01-09 changes manual G01 documentation but not absent G02 ownership. |
| **G02-08** | COMPLETE/POSITIVE OFFLINE analysis of new LOCAL XTR G01-09 RX-only capture; actual physical owner INCONCLUSIVE | User live power-cycle captured on RX-only B6: 11,944-ms callback gap, CRC-valid `0x1E` return, `A80E=0000 A80F=0005`, 24 FC23 requests, reported `peerRspShape=0`, `P=0/32 A=0/32`, software TX=0, no sampled RX parser resync/drop. NO peer response shape in this bounded window; **not proof of an empty slave/address, physical sender identity or exclusive reply authority**. |

All 38/38, 16/16, 26/26 tests and the cross-model parser/fuzz replay were rerun in this conversation on 2026-10-14 after restoring Python fixture dependencies from the existing local evidence bundles. The initial attempt without unpacked dependencies failed at import/data lookup and was fixed by restoring the original immutable test inputs; those setup errors are not protocol-negative observations. Code/results are host-only and not deployed. Original cross-model capture 7/7 hash confirmation is sourced from prior recorded revalidation, not independently redone in this new step.

## G02-08 experiment discipline
**Number/hypothesis:** G02-08 — a newly documented physical switch intervention combined with passive FC23 request retries can reveal whether response-shaped traffic occurs in the bounded RX-only window, without silently creating an owner claim.

**Baseline:** G02-01..07 local/other-model source-typed findings; fresh G01-09 user-video-anchored power episode on R6-P74DI-B6 RX-only. The user supplied identical 4,660-line logs.

**Exact controlled change:** offline read of existing G01-09 log; Python read-only assertions of capture SHA, causal chronology, FC23 counter, peer response counter, TX and parser health. No new instrumentation, ESP flash, register transaction or on-wire action.

**Relevant fields:** native slave 0x0F FC23 requests (handshake family), `peerRspShape` observation, `03E8` bootstrap count, 0x1E first CRC-valid return, `A80E/A80F`, B11D CRC/fault and TX software metadata. Generic native FC16/FC03 only as context; no controller-controlled register was changed.

**Observed:** callback gap at source line 1826, first CRC return line 1828, cold status line 1860, 24th request/zero peer response at line 4570. RX parser reported resync=0/drops=0, software TX=0 and DE reported 0. The last B11D record around 15:42:32 had `rawFrames=93280 comparedV5=93280 countDiff=0 byteDiff=0 nativeFault=0/0/0 ioTx=0`; it is a **sample** not a final electrical proof.

**Positive criteria reached:** correct source hash, chronology, bounded 24 requests, reported 0 matching replies, HOLD and no TX approval. **Negative/abort:** any inference `no peer reply => permanent exclusive physical responder`, any false local/cross-model identity, missed parser fault, or native TX implied from video or ACK. **Recovery:** no hardware/config changes; if source mismatch or corrupt diagnostics invalidate the offline result, mark G02-08 INCONCLUSIVE and leave TX HARD DENY.

## Interpretation
**OBSERVED LOCALLY XTR:** the same video-anchored episode shows repeated unanswered native FC23 while a software RX-only observer remains alive. The absence of a reported peer response is a bounded negative observation, not proof that none can ever exist. Firmware's own internal handshake state and mailbox mapping are not uniquely identifying electrical owner.

**STRONG CONCLUSION:** some native responses in genuine cross-model contexts clearly depend on a functioning responder, and unanswered retry windows exist. The XTR now adds a specifically anchored RX-only local example. Metadata can classify requests and preserve unknown ownership, but **no physical exclusive lease/sender or response authority is established**.

**HYPOTHESIS:** the native Connect service may rely on a single assumed physical slave for 0x0F and controller-master scheduling rather than an explicit on-wire ownership token in the reviewed code. It remains a hypothesis, not a safety guarantee.

**UNKNOWN:** current exclusive native owner, any other potential responder under a different boot/session, hardware stopbit/EOF, physical reply slot, DE circuit electrical fail-low and actual TX line exclusivity. Direct full original XTR raw replays and independent electrical attribution are limited.

## Next research (G02-09 PREPARED / NOT RUN — offline only)
**Hypothesis:** a finite set of same-epoch controller request families can be partitioned into `REQUEST_WITHOUT_RESPONSE_OBSERVED`, `RESPONSE_SHAPE_PRESENT_SENDER_UNKNOWN`, `ASSIGNED_WORK_CANDIDATE`, and `UNKNOWN/HOLD`, but cannot establish permanent physical responder exclusivity without independent evidence.

**Baseline:** G02-01..08, fresh G01-09 FC23 retries and genuine ATEC/Eco5 present/absent windows. **Exact intended change:** host-only comparison of cross-model role/ack response pairs against bounded current XTR request/response families; no code deployment. **Positive:** all source provenance and epochs stay distinct, physical sender and TX authority remain UNKNOWN/DENY. **Negative:** contradictory sender attribution, missed response, or false auto-go. **Abort:** any active bus action, private handshake material, unmatched provenance. **Recovery:** remove/revise host model; keep installed RX-only unchanged.

**Decision:** do not perform a new on-device ACK/handshake test; G02-09 is prepared research, not an authorized TX experiment. Native TX HARD DENY until independent physical ownership and separately required G03–G06 conditions are proven and a particular new active action is explicitly approved.

Existing source reports are dated 2026-10-13 and local evidence bundles; this file consolidates them without rewriting history or reproducing private challenge transformations, recovered secrets or writable emulation code.
