# V5DCM42-BOUNDED-TX-BOUNDARY-OFFLINE-01 — PREPARED contract (2026-10-19)

**Initial status: PREPARED / NOT RUN**, followed by the separately documented [offline RESULT](V5DCM42_BOUNDED_TX_BOUNDARY_OFFLINE_RESULT_20261019.md). This is **NOT** a live user TX experiment.

## Hypothesis
The original private FIX-B2 has exactly one existing ESPHome UART/RX owner and a bounded *host/isolated-bench* native executor, but production native TX remains hard-disabled. A separate private response transport actor can implement finite one-use **DE→FIFO→drain→DE-low** transitions after fresh request/session qualification and still fail closed by default. Its hypothetical physical port must borrow, not replace, ESPHome's installed ESP-IDF UART. Source tests cannot prove current XTR owner/slot/epoch, a native correct dynamic ESP32 backend, or live acceptance.

## Known-good baseline and earlier results
- User-flashed source-family **V5DCM33-FIX-B2**, latest previously supplied on-device 204 s good RX/HA, 393/393 TX HARD_DENY, UART writes=0, exact flashed OTA image digest unknown. Source parent ZIP SHA256 `fdc09c5927b5a351163db95db96dc467abd43cb27e1e7fc8068782bea4a677c7`; YAML SHA256 `32e1b7c3ea4f7411fb94d6d769370b9ae10874403961403002250b96e4365d46`. Rollback **V5DCM23 FIX2 RX-only**.
- Historical **V4.1 EXP386/387 locally positive**, EXP388 RUNNING / PARTIAL; V5DCM32 first manual controller-rejoin attempt COMPLETE / NEGATIVE from earlier B11D integrity.
- V35–V39 source/host guards only; V40 **7/7 genuine historic cross-model DCM cryptographic responses**; V41 dynamic host reference backend, cross-model positive but local XTR acceptance unknown. Oct03 file is genuine **collaborator ATEC/DCM03**, not local XTR; Sep25 old file model unresolved.
- FIX-B2 original `xtr_adapter.hpp` locks production `output_enabled_(false)`; `r6p74b_bounded_driver.hpp` locks `kLiveNativeTxAllowed=false` and limits existing physical egress to an isolated bench. `r6p74e` reports no independent physical response-slot authority. Do not silently graft public firmware HEAD's different Core/adapter.

## Exactly ONE controlled change
Build a **separate private, NONFLASHABLE C++17 TX-capable boundary source** plus source-pinned tests; do not modify/copy production YAML, firmware, HA entities, original Core, existing UART driver, TX block or sticky history. New actor requires both separate compile switches, user-initiated arm, fresh boot/generation, exact already CRC/complete `0x0F` FC23 request metadata, current independently supplied owner/epoch/slot-scoped inputs, unchanged installation under accepted G01–G06 research risks, active B11D/P5 integrity and no competing responder, as well as an injected **confidentially reviewed** dynamic-backend reply. It revalidates session/fault/slot on every TX tick and aborts to RX on failure. Generic ESP-IDF port is **source-only**, uses already-installed UART; compile only against fake IDF stubs.

## Target, bounded effects, risks
**Native incoming classification:** known slave `0x0F`, FC23, firmware-defined approval read `0x0730/count8`, write `0x071C/count8`. **Prospective outgoing frame:** native FC23 *slave response*, generic `0F 17 10 [16 request-dependent private bytes] [CRC16]`; **exact reply bytes and outgoing CRC cannot be supplied before a future specific received challenge** and MUST be verified privately at the later user-initiated trial. There is **no arbitrary FC16 settings write** or user-settable current register value in this source test. Current device values/physical answer slot/owner/epoch are still UNKNOWN.

Host fixture has synthetic arm/deadline/pre/post guard durations only, **not measured or safe current-XTR transmit limits**. Historical genuine gateway response latencies 29–63 ms are cross-model observations, **not** our PHY timing authorization. Risks include bus contention/duplicate responder, incorrect private reply with valid CRC, DE/driver ownership failures, RX loss, heating/controller communication interruption, insufficient physical EOF/brownout recovery.

## Positive, negative, inconclusive, abort
**Offline POSITIVE:** exact B2 ZIP/YAML output-disabled source hash verified, six strict g++ variants including two-key opt-in fake-port path; source-native exact request validation matches original V39; error/peer/generation/slot dropout during transfer aborts and releases RX; borrowed ESP-IDF class compiles/runs under fake-IDF four-way source fixtures; no UART reinstall, input flush or second reader; private ZIP manifest + clean-extract rerun exit0. No ESPHome compilation or physical transmission claim.

**Offline NEGATIVE:** missing gate can arm, repeated output permitted, malformed/foreign RX permitted, active session/slot fault ignored, physical output enabled by a single macro, source baseline changed, simulated release fails without fault, or dependency/suite errors.

**INCONCLUSIVE:** source/parent missing, unexpected compilation/binding or untested real ESP-IDF function semantics. Any physical controller/Online outcome **remains OPEN** regardless of host results.

**Abort/recovery:** stop host research on failed invariant and discard new module. No physical rollback needed since no ESP changed. For later live work, preserve sticky B11D/P5; make fail-closed DE-low and give user FIX-B2/FIX2 rollback. No autonomous controller restart, no scan, no live bus TX.

**Required evidence for future live experiment:** exact signed/pinned private ESP32 backend/source, real full reply bytes+CRC scoped to actual challenge, existing UART binding, measured DE and shifter-empty timing and slot policy, at most one response attempt, user Configuration ARM/CANCEL in existing red/brown logging, current RX/B11C/B11D/P5 checks, stop/recovery log. **These are not yet completed in V42.**
