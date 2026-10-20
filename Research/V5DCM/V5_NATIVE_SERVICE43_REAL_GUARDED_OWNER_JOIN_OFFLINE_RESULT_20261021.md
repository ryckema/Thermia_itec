# Service-43 — exact existing GuardedPort ownership exposed to both native safety callbacks

**Date:** 2026-10-21. **Experiment:** V5-NATIVE-SERVICE43-REAL-GUARDED-OWNER-JOIN-OFFLINE-01. **Status: COMPLETE / POSITIVE — OFFLINE SOURCE/HOST ONLY**. Actual ESPHome/ESP-IDF compilation, flash, live XTR and bus TX: **PREPARED / NOT RUN**.

## Baseline, hypothesis and one scoped source change

The last user-confirmed installed unit remains V83-family **RX_ONLY / HARD_DENY**; the original B11D first-fault mechanism remains **OPEN**, EXP388 remains **RUNNING / PARTIAL**, and V49 RX-only is fallback. The exact private Service42 ZIP SHA256 **61652c9f14d561c60c21471ae42b370f494f1cc90249f673f536019b7ffed739** is pinned unchanged.

**Hypothesis:** the existing actual V5 `ScopedTransport23 -> GuardedPort -> PhysicalOwner` can be observed by both actual original B11D 50ms and DE watchdog 1s callback sites through one read-only integration without a second UART/DE owner or modification of the active V83 safety gate. A host fixture should classify a held guarded DE-high interval and fail closed on stale or mismatched provenance. This is **source integration**, not independent physical owner/slot proof.

**One controlled development addition:** a private S43 source-only `SharedOwnerCallbackJoin` and separate TX-disabled YAML with read-only getters in exactly two existing headers (`v5_native_service23_scoped_transport.hpp`, `v5_native_service23_esphome_runtime.hpp`); S43 is called from the two actual YAML callback code sites. All other 250/252 parent members are byte-identical. Existing S40 and S42 witnesses, V83 observer, UART writer, DE watchdog, V5 parser, B11D sticky faults and Home Assistant entities remain unchanged. No separate UART reader or output actuator added.

## OBSERVED FACTS — actual offline execution

- Original S42 archive SHA/CRC checked and fully retained as separate user-private parent.
- **26/26** Service43 source, YAML and ancestry checks PASS; exact 24 production YAML top-level blocks and 403 existing `id` fields preserved; only two inherited header members differ, exposing the already existing physical-owner instance **read-only**.
- **4/4** S43 C++17 host configurations PASS (strict, noexceptions/noRTTI, UBSan, simulated ESP_PLATFORM/ARDUINO host macros). Existing S42 **4/4**, S40 **4/4**, merged V5 **35/35** host test executables PASS. **4/4** intentionally forbidden TX macro builds correctly FAIL; unchanged S42 independent source audit **25/25 PASS** when rerun on its exact pinned parent.
- The host FakeIO callback occurs **inside original unchanged `GuardedPort::send`** after its existing `PhysicalOwner::confirm_de_high` decision; both simulated B11D/watchdog observations obtain source `PauseOwned`, then return `ContinueRaw` once DE is released. A synthetic fixture is NOT a real electrical lease.
- Negative host controls reject unowned DE-high, missing/mismatched service pointer, DE switch/GPIO disagreement, legacy output, previous B11D sticky fault, stale callback, same-boot and zero reset attempts, and failed drain. S43 always reports `kTxAuthorized=false` and `may_transmit()=false`.
- User-private packaged ZIP **85486e352c831e1f3849f9c1bd9097d8869c32956132ea63e71e483853b493bb**, 263 ZIP members, CRC and 262 content manifest checks validated. Private inherited firmware-derived code and challenge-response material are **NOT** committed to GitHub.

**NOT RUN:** ESPHome schema/IDF compilation, physical callback interleaving, ESP32 flash, bus TX, electrical DE or FIFO completion, current physical controller epoch/slot/peer, Connect C2/Online and semantic setting acceptance/readback.

## STRONG CONCLUSIONS

- **PROVEN OFFLINE SOURCE/HOST:** the exact existing GuardedPort owner is accessible through both original callback sites, and the bounded classification can be exercised using the real original C++ ownership decision, rather than fabricated duplicate state.
- **NOT PROVEN PHYSICALLY:** a `PauseOwned` host classification, original V4.1 success, FC16 ACK, callback timestamps or synthetic true booleans cannot establish current electrical sender, exact reply slot, or native Connect session.
- **TX SAFETY BLOCKER:** inherited `EspHomePhysicalIo::write` reports `n` after calling `UARTComponent::write_array` without per-call evidence of hardware acceptance/last-stopbit completion. `flush` alone has not been independently verified to provide the needed electrical DE release deadline. The existing embedded RX-only compiler denial must stay in place; no direct macro bypass.
- G01–G06 user-accepted bounded installation research risks remain acknowledged without relabeling technical unknowns as physical proof. No ATEC V3 automatic TX defaults, protected source, keys, mailbox implementation or speculative standalone responder are transferred.

## NEXT — Service44

Privately review one borrowed, complete ESPHome/ESP-IDF UART write/drain authority on the already owned hardware peripheral, the original exact V45 owner and the two callback supervisors; preserve production RX-only and test fail-closed interrupted/fault/retry cases offline. Verify compile against actual ESPHome 2026.9.x headers before any user-proposed scoped TX experiment. Do not add a second UART driver/reader, never auto-TX and do not ask for a DCM module, room-sensor disconnection or repetitive G01/G02 test. Any eventual physical TX requires a separate user-initiated test with exact source-confirmed payload/CRC, bounded time/slot/abort and rollback.

**Abort/rollback:** stop source promotion on provenance mismatch, any output-capable regression, B11D fault, DE disagreement or unreviewed wire slot. S43 is offline only; installed V83 and V49 fallback unchanged.
