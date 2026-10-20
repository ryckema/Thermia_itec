# Service-42 — One-owner B11D/watchdog TX-aware contract (offline only)

**Date:** 2026-10-21. **Experiment:** V5-NATIVE-SERVICE42-TX-SUPERVISOR-SOURCE-01. **Status: COMPLETE / POSITIVE — OFFLINE SOURCE/HOST ONLY.** Embedded ESPHome compilation, OTA, live XTR and physical TX: **PREPARED / NOT RUN**.

## Baseline / one controlled change
Last user-confirmed XTR-installed image is V83-family RX_ONLY/HARD_DENY, with first B11D start-alignment fault still OPEN, EXP388 RUNNING / PARTIAL, V49 fallback. Pinned user-supplied Service40 private archive SHA256 `47af7ec68e369a7b4e862295c3ed6772cc3c21663e65f5ab8371313c7aba0a34` (240 members, CRC valid) and all 240 original members were retained byte-identically in a **private** continuation bundle.

**Single offline integration change:** a separate S42 source-only candidate adds a pure callback/ownership-contract observer to the existing real 50ms B11D and 1s DE-watchdog callback sites. The candidate changes neither original V5 parser nor UART input, DE writer, B11D first-fault latches, Home Assistant identity fields, or the existing TX-denying compile header. The older S40 observer and the original Service23/V45 decisions remain unchanged. S42 records RX callback provenance and host-models a distinct prospective guarded DE-high ownership classification; it never grants TX. There is no additional UART reader/writer, no switch command, no automatic authorization, no protected handshake implementation, no 0x0708 tooling or ATEC-derived TX code.

## OBSERVED FACTS — actual offline tests
- Exact S40 parent archive CRC/sha verified; 240/240 inherited source members byte identical.
- **25/25** new source/YAML checks PASS. PyYAML compose accepted source and distinct candidate (not ESPHome schema/codegen). Original **24/24** production top-level blocks and **403/403** YAML ID fields preserved, including existing Home Assistant identities and sensor/supervisor paths. Original RX-only build guard retained.
- New metadata-only C++17 host tests **4/4 configurations PASS** (strict, noexceptions/noRTTI, UBSan, simulated ESP_PLATFORM+ARDUINO macros). Existing S40 callback-witness tests **4/4 PASS** in corresponding host modes. Existing merged V5 C++ host suite **35/35 PASS**. The original S36 guard rejects **4/4 intentionally forbidden TX-macro builds**.
- Host negative cases exercise boot/pointer mismatch, absent/stale callbacks, mismatched DE switch/GPIO, prior sticky B11D, old output path, incomplete owner/slot/epoch/peer flags, incorrect guarded-port verdict and expired deadline (also across timer wrap). A synthetic positive *classifies* the future bounded owner state but always returns TX permission FALSE; simulated flags are NOT physical provenance.
- **NOT RUN:** actual ESPHome/ESP-IDF target compilation, embedded runtime callbacks, physical RS485 TX/DE lease/turnaround, independent physical EOF/slot/peer/epoch observation, current native Connect session/C2/Online or semantic settings readback.
- User-private complete source artifact SHA256 `61652c9f14d561c60c21471ae42b370f494f1cc90249f673f536019b7ffed739`, **252 members CRC/manifest checked**. TX-disabled candidate YAML SHA256 `d3eb41ea9e84d7a702f1fe8efa4f633abfe96166640d6866b1ee97c5d77f94ad`. **Neither private code nor firmware-derived material was uploaded to public GitHub.**

## STRONG CONCLUSION
The RX-only original S40 pointer/freshness witness cannot be promoted to a TX-aware DE-high exception. To defer one B11D/watchdog tick legally, a separate embedded TX owner must prove its actual guarded DE-high section and consult the same V45/ScopedTransport physical lease from **both** callbacks. Merely supplying TRUE booleans for boot, profile or slot does not establish this. The present S42 source and candidate remain TX HARD_DENY.

## HYPOTHESES / OPEN
A separately configured TX-capable V5 target using the proven historical local V4.1 session and a *real* single owner/lease may eventually be testable under bounded manual user initiation and the already accepted installation-scoped G01–G06 research risks. Technical OPEN: current XTR session/peer/slot/epoch, embedded DE-write completion proof (ESPHome write_array queues bytes), B11D first fault, trusted production attestation and genuine application/semantic acceptance. Prior 32/32 local V4.1 successes are not equivalent to current V83/V5 TX readiness. External ATEC V3 author claims, cross-model captures and original Connect source remain separate evidence classes.

## NEXT
Service43: privately design/test the single actual embedded DE/UART write authority and B11D/watchdog shared lease, with an explicit manual accepted-risk policy, full native service rather than an incomplete one-shot gateway and independent abort/rollback. Keep the currently installed RX-only YAML and V49 fallback unchanged. Never auto-enable ATEC timings/TX, do not disconnect the room sensor, and do not treat FC16 ACK or host FakeIO readback as semantic acceptance.

**Abort:** unexpected output or unknown owner/slot/peer, B11D latch, parser fault, DE mismatch or COMM ERR. **Rollback:** last user-verified RX-only image; S42 offline work itself requires no device rollback.
