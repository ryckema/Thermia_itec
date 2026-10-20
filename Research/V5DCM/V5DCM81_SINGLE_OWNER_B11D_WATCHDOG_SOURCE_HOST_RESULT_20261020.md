# V5DCM81 — Single logical owner for V49 B11D + watchdog: original V45/source-linked HOST result

**Experiment ID:** V5DCM81-SINGLE-SUPERVISOR-V45-SOURCE-HOST-01  
**Date:** 2026-10-20  
**Status: COMPLETE / POSITIVE — EXACT V49 SOURCE + HOST-ONLY safety consistency, NOT physical UART/DE or native XTR TX.**

## Controlled question and last verified baseline

**Hypothesis:** A single nondeployable logical native-session owner can provide identical scoped DE-ownership decisions to both original V49 supervisors — the 50ms B11D/V45 observer and 1s periodic DE-low watchdog — through an initial session intent, 32 ordered historical local controller FC16-page-shape intents and two runtime intents, rejecting wrong owner, context loss and DE pin/switch mismatch without any native bytes/output.

**Last user-verified physical state:** installed V49 RX_ONLY/HARD_DENY TX0, user manual controller restart callback gap 10.351s, V49 shadow matched 285 post-gap frames over 30.532s, cumulative 63 unanswered native challenges. Controller 0x0867 version, electrical owner/EOF/slot, current XTR acceptance, installed binary SHA UNKNOWN; EXP388 remains RUNNING / PARTIAL. No new on-device result.

**Prior relevant:** local EXP255 unanswered; EXP256 one guarded reply led to first settings page but without complete follow-on caused COMM ERR ONLINE/LINK; EXP257/258 partial ACK progression; EXP355/386 historical 32 native page ACK + runtime. V74–80 exact-source and host-only steps: V78 private initial backend actually ran behind FakePort, V80 original V49 StreamParser verified multi-ADU fan-out. V81 does NOT execute V78 backend or re-run hardware.

**One controlled OFFLINE change:** new nondeployable `v81_owner_boundary.hpp` shares one logical owner and an artificial stage lease between two read-only supervisor calls; links byte-identical original `v5dcm45_de_ownership.hpp`, permits no physical Port, GPIO, UART or protected native response code. The host fixture injects *synthetic* all-true physical predicates, GPIO/switch levels and 35 mock confirmations. Never treat these as measurements.

## Exact-source evidence

- Pinned original user-provided **69-entry V49** ZIP SHA256 `62afe39629102a3daa06f09eab3ed159f44437d702fb8d3904c61e62e2a85630`. **24/24 source audit PASS**, including byte-identical original V45 logic, exact V49 B11D+watchdog callsites, original V43 and V44B double borrow of same UART+DE, native actors' `parsed.size()==1u` branch, original V42 build lock, and all 32 original R6P30D page start/count metadata against V49 long-history profile.
- Original V49 B11D every 50ms reads `v5dcm44b::runtime().b11d_tx_window_owned(...)` and original V45 `observe(switchHigh,pinHigh,legacy,owned)`. Any switch/GPIO disagreement or old TX activity is an original V45 sticky-unsafe condition.
- Original V49 1s periodic DE watchdog reads `v5dcm44b::runtime().defer_periodic_rx_watchdog()` or unconditionally sets tracked direction switch low.
- Original V44B allows watchdog defer in **PreGuard**, even before actual DE-high, while B11D's true ownership qualification requires active FIFO ownership. V81 deliberately narrows mock watchdog defer to the *currently observed* matching DE-high lease. This is **new modeled safety policy**, NOT original behavior nor tested on ESP32; physical race/interrupt interactions remain OPEN.
- V49's 32 historic native controller ACK metadata uses LONG/capture geometry, while other source-supported actual XTR profile shapes exist (e.g. `03E8/13` vs `03E8/14`). Profile 2, 32/32 native ACK and genuine Connect 2.1.105 APP33/C2 are different readiness claims.

## Actually run / measured scope

- **2,236/2,236** strict C++17 g++ host assertions PASS.
- **2,236/2,236** ASan/UBSan PASS.
- **2,236/2,236** noexceptions/noRTTI PASS.
- **4/4 deliberate embedded/private TX macro builds correctly DENIED**.
- Positive synthetic path: 35 stage metadata events with explicit mock confirmations (first native request intent; 32 source-derived historic long-profile FC16 ACK intents; runtime 085F FC16 + 0708 FC03 intents). Identical owner ID at each stage and both supervisor queries. Host fault tests: 12 absent preconditions; 12 scoped DE/owner/clock/fault variants; 35 out-of-order/wrong-shape attempts; 32 premature native pages; context mutations observed independently by B11D/watchdog; duplicate-owner veto; 256 repeated default output impossible checks.
- **0 real UART writes; 0 physical GPIO/DE writes; no runtime Port method exists.** No actual native `0x0F` reply or `0x0708` command-mailbox implementation, protected source, keys, or captured challenge bytes published. No ESPHome source/YAML change, full ESPHome compile, flash, reboot, warm-water setting change, register write or real controller ACK.

**PROVEN SOURCE/HOST:** old V49 split-borrower and V44B-only supervisor ownership; original V45 ownership truth table, and an independent non-emitting shared-owner host model that passes negative guard tests for both readings.  
**STRONGLY SUPPORTED:** unify one *real* physical DE driver and make both B11D and watchdog read a single bounded authoritative owner state before any private full-native service can ever operate.  
**OPEN / UNKNOWN:** real physical owner/peer, wire EOF and slot, source watchdog PreGuard vs DE-HIGH race under scheduling, current controller version/profile0867, complete real XTR native 32 ACK/runtime acceptance, Connect APP33/C2/Online.

## Abort/recovery and next

This was an offline test, **no register/payload/current register applies**. Positive criteria: exact source pins, consistent host B11D/watchdog decisions, full mock stage ordering, hard compiler deny and impossible hardware output. Negative: mismatched source or unsafe owner/watchdog grant; neither seen in tested host scenarios. Controller acceptance untested and remains unknown, not a negative result. Abort is to discard host program on failing assertion/source pin; physical rollback N/A. Installed V49 remains unchanged RX-only/HARD_DENY, all original historical B11D/P5/FIX2 faults preserved.

**NEXT V82 (NOT RUN):** exact-source unified physical Port/DE *design with TX permanently disabled*; host interleaving stress for 50ms B11D versus 1s watchdog, geometry/version qualification and full private response chain separately. Before a live trial independently measure wire EOF, peer/slot and document exact bounded user-triggered payload/rollback; never repeat single-response EXP256 COMM ERR.

**Reproducible nonsecret conversation-only ZIP:** `V5DCM81_SINGLE_SUPERVISOR_V45_SOURCE_HOST_ONLY.zip`, SHA256 `a6e2590e86b460337e476f40c463968481a72a2e26a3e4444d81fe5d05e54907`; contains source audit, host-only owner header, unchanged original V45 and fixture, migration map, report and checksums. No private native backend in public GitHub.