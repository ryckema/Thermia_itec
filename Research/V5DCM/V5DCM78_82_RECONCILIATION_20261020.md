# V5DCM78–82 reconciliation — 2026-10-20

**Status: SOURCE/RESULT RECONCILIATION (not a separate live experiment).** No new hardware TX, no ESPHome flash, no controller restart. Newest tested milestone V5DCM82 **COMPLETE / POSITIVE, offline host/source only**.

| ID | Actually executed | Valid conclusion | Must NOT conclude |
|---|---|---|---|
| V78 | Original protected V49 V43 dynamic initial native backend **ACTUALLY ran**, original V42 OneShot behind nonphysical FakePort; 6/6 default, 10/10 isolated host, 53/53 negatives | Genuine private computation + abstract transport can operate with synthetic context; default build locks output | Not real UART, owner, electrical response window, complete 32 ACK chain or Online |
| V79 | Metadata-only 35-stage single owner host model, 2729/2729×3, 15/15 source audits | Host ordering and owner guard for initial +32 native controller ACK intentions + runtime metadata | Mock confirmations are NOT real FC16 ACK delivery; no true native responder |
| V80 | Original V49 StreamParser physically unmodified and host-replayed 2687 existing capture ADUs; synthetic split/coalesced, 8696/8696×3, 20/20 source checks | Original V49 V43/V44B one-frame callback gate can miss **synthetically coalesced** ADUs, unlike general per-ADU RX loop | 448 synthetic coalesced groups were NOT observed as such in actual ESPHome callback timing |
| V81 | Original V45 predicate used unmodified in single-owner *synthetic* lease, 2236/2236×3, 24/24 source audits | Exact source exposes V44B-only owner decisions in B11D/watchdog, and preguard-vs-high difference; guarded host mock can be consistent | NOT actual physical owner, DE slot, native payload generator or RTOS scheduling |
| V82 | Original source 30/30; new **NONDEPLOYABLE HARD-DENY interface** tested 38081/38081×3; 4 embedded/TX compile guards | RX-only one-owner interface and B11D/watchdog fail-closed scheduling simulated; source profile discriminators 03E8 13/14 etc confirmed | NOT an embedded driver or safe live native TX; no native private computation in V82 |

## Evidence hierarchy and current real state

- **LOCAL HISTORIC XTR PROOF:** EXP256 one native reply triggered 03E8 within ~124ms, but without a complete service produced real COMM ERR ONLINE/LINK; EXP257/258 progressed page ACKs; EXP355/386 earlier qualified historical 32/32 ACK and runtime under those particular contexts. These old experiments are NOT current V49 acceptance proof.
- **CURRENT USER VERIFIED V49:** RX_ONLY/HARD_DENY, physical UART TX0, manual controller callback silence 10.351s, post-gap 285 CRC/byte matched frames over30.532s, cumulative63 unanswered native 0x0F FC23, EXP388 RUNNING/PARTIAL. Exact binary installed, present controller 0x0867, real electrical peer/owner/EOF/slot are UNKNOWN.
- **V49 SOURCE PROVEN:** V43 + V44B are two physical borrowers of same UART and GPIO21 direction switch; B11D (50ms) and periodic RX watchdog (1s) both recognize V44B exclusively; 1s watchdog can defer already during PreGuard while B11D owns DE HIGH only in active bounded window; native actor path only sees one parsed ADU if no pending fragment. Source profile shape1 vs shape2 distinguished by registers (03E8=13/14, 0410=21/22, 0492=9/11, 051E=9/10).
- **ORIGINAL VENDOR APPLICATION:** Connect 2.1.105 APP33 significance/profile logic is not the local historical 32-stage controller ACK chain; source interpretation does not imply APP C2, genuine Connect identity, or Online.

## Safe next handoff

**V83 (NOT RUN):** prepare an exact-source RX-only integration diff/consolidated observer interface preserving known-good V49 YAML, all entities, colored logs, substitutions, DE fail-safe, sticky B11D/P5/FIX2 and per-ADU framing. Offline review/validate before any user-initiated flash. Nothing in V78–82 justifies unlocking native TX. A *future distinct* native TX experiment needs ONE actual UART/DE owner integrated with **both** supervisors, independently measured electrical wire EOF/peer/slot and timing, current controller geometry/version, **complete private** request-dependent first response + 32 native ACK/runtime service, bounded abort/recovery, and verified rollback. Do not rerun EXP256 standalone first reply.

**Canonical refs:** [V78](V5DCM78_PRIVATE_BACKEND_V42_FAKEPORT_SOURCE_RESULT_20261020.md), [V79](V5DCM79_SINGLE_OWNER_FULL_SERVICE_BOUNDARY_HOST_RESULT_20261020.md), [V80](V5DCM80_EXACT_V49_MULTIFRAME_RX_MIGRATION_SOURCE_HOST_RESULT_20261020.md), [V81](V5DCM81_SINGLE_OWNER_B11D_WATCHDOG_SOURCE_HOST_RESULT_20261020.md), [V82](V5DCM82_SINGLE_OWNER_HARD_DENY_SCHEDULER_SOURCE_HOST_RESULT_20261020.md).
