# V5DCM78 — Actual private V49 backend + original V42 policy behind FakePort (no physical TX)

**Experiment ID:** V5DCM78-PRIVATE-BACKEND-V42-FAKEPORT-HOST-01  
**Date:** 2026-10-20  
**Status: COMPLETE / POSITIVE — original private code was ACTUALLY EXECUTED OFFLINE, NO WIRE / ESPHOME / XTR TX.**

## Controlled question and known-good baseline

**Hypothesis:** the actual original, protected V49 native backend can be linked to the unmodified V42 OneShot Port abstraction in a host-only test, with a strict build lock in ordinary mode and simulated UART progression only when independent safety evidence is *synthetically* supplied. This is an integration/source milestone beyond the abstract V75–77 intent/DE models, not a claim of genuine XTR native admission.

**Last user-verified XTR baseline:** V49 RX_ONLY/HARD_DENY with local user-attested controller OFF/ON, 10.351s callback gap, 285 independently CRC/byte-matched RAW/V5 frames over 30.532s, native UART TX attempts0; initial 0x0F FC23 requests timed after return, cumulative 63 unanswered over noncontinuous console. Actual physical reply owner/EOF/slot, controller profile 0867, flashed firmware binary hash UNKNOWN. EXP388 remains RUNNING / PARTIAL.

**Previously relevant:** EXP255 63 no-response / no native status; EXP256 one real old controlled native response → first 03E8/count14 ~124ms later but no follow-on ACK → repeated page and real COMM. ERR ONLINE/LINK; EXP257/258 first sequential FC16 ACK stage progression; EXP355/386 historical previously qualified 32/32 controller ACK + runtime 085F/0708; V47 original sticky B11D fault denied new TX; V74 exact-source independent TX gates, V75 full 32-stage *intent*, V76 dry ticket owner, V77 original V45 DE decision with FakePort. No historic live experiments repeated.

**ONE controlled OFFLINE CHANGE:** the actual original V49 `v5dcm43_private_native_backend.hpp` is **compiled and invoked** with the exact original `v5dcm42_one_shot_tx_policy.hpp` behind a local FakePort that does not connect to ESP32, UART or GPIO. No YAML, physical port, power change, settings or register writes. Unlike V76/V77, the original private computation runs — but private response bytes and security algorithm are never logged, stored as user artifacts, or committed.

**Pins:** original private V49 69-file ZIP SHA256 `62afe39629102a3daa06f09eab3ed159f44437d702fb8d3904c61e62e2a85630`. Exact original backend and V42 headers copied solely to temporary local private build directory. The original V42 class's response CRC/geometry guards, compile-time kBuildMaySend and `physically_confirmed=false` / `real_online_confirmed=false` are preserved. Original V43 `user_arm()` and actual ESP-IDF UART/DE runtime were NOT compiled or exercised as on-device integration.

## Executed results (test fixture inputs are synthetic; not physical XTR captures)

1. **Ordinary source build (no native TX macros): 6/6 assertions PASS.** Genuine backend computes a bounded structurally CRC-valid reply locally, but V42 `arm` refuses `BuildLocked`. Fake UART writes=0; DE never high.
2. **Host-only build with BOTH original V42 macros: 10/10 assertions PASS.** With *synthetic* boot/generation/owner/slot/healthy-RX/accepted-risk evidence, original V42 `OneShot` moves through guarded FIFO/drain/postguard to `Complete`; FakePort writes=2 and 21 bytes admitted, then DE LOW. This is not an electrical UART transmission and explicitly **does not validate real response timing, bus ownership or master acceptance**. No reply content retained or published.
3. **13 negative scenarios, 53/53 assertions PASS.** Missing peer exclusivity, slot, owner, generation, new B11D/P5/RX fault, DE low, pinned reference, backend dynamic indication, plus fake DE-entry and UART drain faults. Ordinary safety negatives fail before a fake write; driver-failure paths revoke and end RX.
4. **ASan/UBSan PASS** for the 10/10 host both-flags integration and 53/53 negative suite, no sanitizer diagnostics. Initial disposable test source lacked a standard header for `std::abort`, fixed before final run; not a production bug.
5. No real physical UART/DE writes, no ESP-IDF/ESPHome compilation, no protected source publication, no full XTR boot/service ACK chain, no controller/runtime 0708, no vendor-app readiness.

**CRITICAL implementation boundary:** V42 `OneShot` is exactly *one* approval reply and then terminal `Complete` (or `Revoked`); its 70ms response budget is an old software bound, **not a measured wire-EOF-to-reply slot**. For full native DCM emulation, keep the actual private per-request backend behind an exclusive physical owner *and* implement the downstream 32 historic native controller FC16 ACK + runtime FC16/0708 responder safely. No session progression can be inferred from FakePort completion; no native master semantic acceptance is proven. Current V49 V43`user_arm` still passes generation 0, unqualified timing and owner/slot FALSE, and V43/V44B shared UART/DE still must be consolidated with original B11D/watchdog coherency.

## Evidence levels and readiness decision

**PROVEN ORIGINAL SOURCE + HOST:** actual private backend and actual V42 abstract transport compose and can complete solely on fake hardware under synthesized all-true evidence; original default build prevents output; 13 fault scenarios fail closed.  
**STRONGLY SUPPORTED:** technical source integration of first private response is feasible without reverse-engineering the answer anew, but it is *not* the XTR's full native DCM integration.  
**HYPOTHESIS:** a future single physical UART/DE owner plus complete native controller service can be brought up safely after independent electrical verification and separate user-scoped experiment.  
**OPEN / UNKNOWN:** physical owner, wire EOF/slot, timing, current controller version, actual acceptance of current challenge-dependent answer, DE watchdog, 32/32 real ACK, vendor app 33 significant groups, original Connect C2/cloud Online.

**Safety / abort / rollback:** All executed calls use nonphysical FakePort. Abort host test immediately if source SHA, CRC, sanitizer or positive/negative guard fails. No physical actions, register values, response payloads, device rollback or restart. V49 installed baseline unchanged, TX=HARD_DENY; no user-run active experiment was initiated.

**NEXT V79 — offline only, not registered/run:** integrate a private single-owner *session-level* Port interface around original V42 + 32 native ACK/runtime policy, and replay historical page-shape metadata with FakePort (no protected source/publication). Verify same actual DE owner is recognized by B11D *and* periodic watchdog and that future TX cannot be armed without externally measured electrical slot/owner/EOF. If source feasibility passes, prepare a **separate** bounded user-run experiment; avoid standalone EXP256-style first reply because of prior COMM ERR.
