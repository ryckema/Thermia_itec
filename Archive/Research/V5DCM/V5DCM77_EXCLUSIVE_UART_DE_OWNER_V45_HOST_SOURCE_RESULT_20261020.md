# V5DCM77 — Exclusive UART/DE ownership and exact original V45 B11D guard: source/host preflight

**Experiment ID:** V5DCM77-EXCLUSIVE-DE-OWNER-V45-SOURCE-HOST-01  
**Date:** 2026-10-20  
**Status: COMPLETE / POSITIVE — OFFLINE source-constrained FakePort safety checks only.** Not native XTR TX, not a complete responder, not compiled/flashed into ESPHome and not Online.

## Hypothesis, known-good baseline, relevant past, one controlled change

**Hypothesis:** one exclusive nontransmitting owner for native DE activity can enforce the *original V49 V45* B11D switch-vs-GPIO decision, preserve old error history, and fail closed on unverified electrical bus owner/wire EOF/slot, watch-dog disagreement, invalid generation or inability to return to RX. It should be possible to test this as a bounded C++17 host class before privately integrating the existing native dynamic backend or allowing any on-device UART output.

**Last verified XTR baseline:** User-installed V49 RX_ONLY/HARD_DENY, user-confirmed controller manual OFF/ON and 10,351ms UART callback gap; original V49 `RX_SHADOW_RECORDED` 285 RAW/V5 matched frames over 30.532s, output attempts0; first exact native 0x0F FC23 ~1.3s after return, cumulative 63 native requests unanswered in noncontinuous log. Current electrical line EOF, exclusive reply slot/owner, exact flashed binary and controller 0867 version NOT MEASURED. EXP388 RUNNING / PARTIAL unchanged.

**Earlier findings:** EXP255 no-reply requests; EXP256 one real historical guarded native reply triggered first FC16 03E8/count14 ~124ms later but incomplete service caused COMM ERR and DHW-side problem; EXP257/258 sequential page ACKs advanced to 03FC and 0410; EXP355/386 older, previously qualified full 32/32 page ACK + runtime status. V47 17-byte restart orphan B11D 250ms fault, TX0; V69 intentional V49 hard build lock; V74 V43/V44B both bound to same physical UART and DE, original B11D owner and periodic watchdog only recognize V44B; V75 source-pinned 32 stage intent-only model; V76 exclusive ticket *dry* model with 0 physical writes. None of these represent a newly qualified physical reply slot.

**ONE NEW controlled offline change:** source-pin the *exact original* `v5dcm45_de_ownership.hpp` from V49 and implement a small, separate, **nondeployable** `v77_exclusive_arbiter.hpp` with one claimant, conservative external evidence predicates, bounded 70,000us synthetic DE interval, original V45 `observe` decision and fake DE switch. It has **no real Port or UART output API**, and hard-rejects ESP/Arduino or either V42 private native build macro. It is an additional guard/source feasibility probe, NOT a private V43 backend integration or live native responder.

## Source provenance

- Pinned original 69-member user V49 ZIP SHA256 `62afe39629102a3daa06f09eab3ed159f44437d702fb8d3904c61e62e2a85630` verified locally. Private `v5dcm43_private_native_backend.hpp` and physical `v5dcm43_esphome_runtime.hpp` and `v5dcm44b_live_reply_runtime.hpp` exist inside that ZIP; private response algorithm was not invoked or published.
- Original V45 `v5dcm45_de_ownership.hpp` original behavior: `observe(switchHigh,pinHigh,oldTxActivity,qualifiedOwnedWindow)`. Any switch/pin mismatch or old TX activity ⇒ `LatchUnsafe`; exact both-HIGH with a qualified owner ⇒ `PauseOwned`; both LOW without owner ⇒ `ContinueRaw`; both LOW with alleged owner ⇒ `LatchUnsafe`. This method only decides monitoring; it NEVER grants TX.
- Source-linked original V43 `EsphomeBorrowedPort` uses GPIO21 with shared ESPHome direction switch and already-installed ESP-IDF UART; original V44B uses this borrowed Port and alone implements B11D owned-response and periodic-watchdog defer windows. The V43 actor itself lacks independently verified controller/slot timing, and current V49 build remains HARD_DENY.
- Artifact `V5DCM77_EXCLUSIVE_DE_OWNER_OFFLINE.zip` SHA256 `b7e4fdb6a10688414998eda3b7e814def19c270752525ef5b98379bb9644fd25` (verified ZIP CRC and file checksums). Standalone nonsecret host guard `v77_exclusive_arbiter.hpp` SHA256 `0e23af9d0579848e797d1b5538c90ea0fc9983175c8f539b30946d870887956e`, host tester `v77_test.cpp` SHA256 `931f8506b68115d18438275972db2d8adbd3bd6a2ea6cdd17d5ebe3d79273a51`; ZIP bundles only those, original public V45 guard, README and manifest (NOT private backend).

## Actually run host tests

- **3,245 / 3,245 strict C++17 g++ -O2 -Wall -Wextra -Werror -pedantic assertions PASS**.
- **3,245 / 3,245 ASan/UBSan PASS**.
- **3,245 / 3,245 -fno-exceptions -fno-rtti PASS**.
- **4/4 deliberate compiler denials**: ESP_PLATFORM, ARDUINO, V5DCM42_PRIVATE_TX_BUILD, V5DCM42_HARDWARE_PORT_REVIEWED.
- Fake fixture tests 200 unknown-owner/slot cases fail before claim, 200 fully **synthetic externally true** owner/slot/EOF episodes claim → DE-high bool → original V45 `PauseOwned` → DE-low bool → release; 14 fault variants for missing physical evidence, missing full-service readiness, altered historical error, new RX error, peer, owner/generation, synthetic DE enter failure, mismatch, 70ms expiry and Abort; four exact original V45 decision table assertions. 0 FakePort data writes and 0 native response/ACK/status bytes. All `can_send_real()`, `authenticated()` and `online()` return false.
- The synthetic DE boolean going HIGH in a **FakePort** is NOT physical GPIO21/actual UART/DE timing. No true electrical line measurement, flash, Home Assistant edit, controller restart, or bus TX occurred. The 70ms budget is a conservative historic software policy, NOT an independently measured XTR response slot.

## Findings / safety decision

**PROVEN source/host:** original V45 B11D ownership rule is compatible with a *single* host arbiter that denies on absent evidence and monitors DE agreement; no output is possible. Independently source-verified existing V43/V44B dual physical runtime and shared borrowed Port would require consolidation before physical testing. **STRONGLY SUPPORTED:** exclusive UART/DE must be owned and checked by the *same* actor recognized by raw B11D + periodic watchdog; never grant a runtime send just because a CRC-valid FC23 arrived.

**NOT PROVEN:** electrical owner/EOF/exclusive response window; real GPIO21 timing, genuine 0x0F dynamic answer, complete UART 32-page FC16 ACK/runtime service, actual physical peer-free state, original Connect 2.1.105 C2 or Online. The private dynamic backend is present but **NOT** executed in this V77 experiment. A host FakePort test cannot qualify native TX.

**Positive criteria:** source-pinned original monitor, single owner, explicit unknown-context veto, original B11D agreement, abort/clock/fault fail-closed, no real transmitter. **Negative:** any physical output, ownerless DE grant, lost first-fault preservation, mismatched GPIO falsely accepted, forbidden embedded compile passes. **INCONCLUSIVE for controller acceptance**, no new on-wire tests.

**Abort/rollback:** offline only, discard guard on failed tests. No TX target/payload/current register values involved and no device recovery because current V49 remains RX_ONLY/HARD_DENY.

## NEXT V78 scope (not run)

Offline **private** integration boundary needs real V49 V43 dynamic backend and the one owner that both original B11D and 1s watchdog recognize, plus V75/V76 32 native controller FC16 ACK+runtime service. Before any user-run live experiment independently inspect physical wire EOF/DE/no-other-peer/slot and source timing; prove fail-closed with fake hardware under missing context; current V49 will not permit it. **Do not** simply enable V42 compile flags, copy a static historic response into public GitHub, clear V47-style B11D first faults, flash this host guard or repeat EXP256 one-reply alarm.
