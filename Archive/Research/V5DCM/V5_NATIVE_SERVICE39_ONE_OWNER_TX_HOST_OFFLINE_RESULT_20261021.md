# Service-39 — Single native TX owner and shared B11D/watchdog lease (host-only)

**Date:** 2026-10-21. **Experiment ID:** V5-NATIVE-SERVICE39-ONE-OWNER-LEASE-TX-HOST-01. **Status: COMPLETE / POSITIVE — OFFLINE SOURCE/HOST ONLY**. Physical XTR test and ESPHome TX build: **PREPARED / NOT RUN**.

## Verified baseline and one controlled change

The last user-confirmed running device is V83-family RX_ONLY/HARD_DENY, not Service38. The FAS1 add-on lacks independent flash confirmation. EXP388 remains RUNNING / PARTIAL and B11D's startup first-fault cause remains OPEN. The original V49 source is fallback. Service38 private source archive SHA256 `f1f5c14c205c91ede175ea165f8fc07b18b01b510d1779556fa9c95709725cf6`.

**One source addition only:** a private, host-only shared-owner lease around the *existing* V5 `ScopedTransport23` and `UnifiedNative23`. Both modeled B11D and 1s watchdog callbacks must reference the **same transport object** and use the already existing V45 DE-ownership decisions. Current request geometry/CRC, epoch, token, peer and measured physical slot remain separate required evidence. The adapter latches failure and permanently disarms within the host session on owner conflict, old-actor activity, replayed token, elapsed slot hint, CRC fault, DE switch/GPIO disagreement or transport-drain failure. It adds no new protocol responder, UART consumer, GPIO/DE writer or authentication handling.

The new header **intentionally refuses compilation on ESP_PLATFORM and ARDUINO**. It is a separated TX-capable desktop test target, **not** a TX-enabled ESPHome YAML or flashable firmware. The original RX_ONLY YAML SHA256 `55c6b1aaa8e17ea8d4ccc51d59fb7f6bc6673554cb5a2cacc841fd80574cc6ca` remains byte-identical.

## Four distinct evidence classes

- **LOCAL XTR V4.1 (earlier completed user live experiments):** 32/32 native bootstrap page ACK progression, bounded runtime, W1 desired and W3 current-selector behavior, prior 03F4 setpoint application and controller republish/readback in specifically qualified historical sessions. These results **do not** prove current V83 electrical slot or a working Service39 device session.
- **CURRENT V5 source + Service38 host:** one guarded physical-IO abstraction, transactional FC16 page cache, runtime service and XTR version page physical `0864/count4` corrected offline. S39 reuses these components; no proprietary responder copied.
- **ORIGINAL Thermia Connect 2.0.18 and 2.1.105 firmware:** W0/W1 desired selectors, W2/W3 current selectors, W4 operations, independent version/profile/receipt/Online application states. The original firmware architecture and nominal selector ranges are NOT proof of current XTR physical timing or Connect C2 readiness.
- **ATEC V3: EXTERNAL SOURCE / EXTERNAL CLAIM:** structurally comparable native 0x0F gateway, startup, FC16/FC03, refresh and readback. Different controller/display topology, externally claimed working writes, missing underlying claimed historical raw captures and no redistribution license. No secret, authentication algorithm, challenge/reply bytes, private gateway or mailbox code included in public report.

## Observed offline results

- 223/223 original Service38 archive members verified byte-identical. S39 adds only separate host-owner adapter, tests, runner, source verifier and private documentation.
- Separate Service39 C++17 host build matrix **6/6 PASS**: default no-TX flags, each lone scoped-build flag, both flags, no-exceptions/no-RTTI and UBSan. The first three generate zero FakeIO writes; only dual flags plus synthetic explicitly supplied qualifying evidence permit simulated delivery.
- FakeIO rehearses **36** responses through the existing engine: one synthetic startup, 32 V4.1-derived config page acknowledgments, runtime service entry, local-XTR-shaped 0864/count4 and cached FC03. During each simulated DE-high lease, **both** B11D and watchdog see the same qualified owner; when RX/DE low, neither defers.
- Negative host tests pass for wrong owner instance, no manual arm, missing slot, token replay, synthetic expired slot hint, mismatch between DE switch/pin, legacy actor interference, incomplete drain and same-scope no-rearm after fault. **Synthetic booleans and timing values are not actual XTR measurement**.
- Compile-negative guard rejected both ESP_PLATFORM and ARDUINO modes, **2/2 PASS**. Inherited Service38 synthetic host matrix + UBSan PASS; existing 35/35 merged C++ executable tests PASS, 40/40 strict RX-only build/source checks PASS, 14/14 Service38 parent audit PASS, 12/12 S39 source/provenance checks PASS.
- **NOT RUN:** actual ESPHome compilation/link, native TX firmware target, flash, active RS485 TX, independent electrical EOF/slot/peer/epoch measurement, original Connect C2/Online or newly verified semantic write/readback.

## Strong conclusions, hypotheses and open points

**PROVEN OFFLINE SOURCE/HOST:** the existing complete V5 native service can be wrapped by a *single* B11D/watchdog owner contract and exercised through full scripted FakeIO progression while preserving the RX-only source and hard-deny build. This is necessary for a future native TX build, **not proof that the actual V83 50ms and 1s callbacks are wired to this same owner**.

**HYPOTHESIS:** a distinct reviewed TX-aware ESPHome target may ultimately support the known V4.1 session service. The current host gate does NOT independently verify electrical owner/slot; manually supplied true flags never suffice as production provenance.

**OPEN / NEXT:** review a separate embedded TX target that leaves the verified RX-only YAML untouched; replace RX-only V83 safety supervisor only with a properly integrated TX-aware lease covering both actual callbacks; establish actual current XTR source/epoch/physical slot/peer and B11D fault resolution. An embedded compile pass and an individually scoped **user-initiated** TX test are mandatory prerequisites for real delivery. Never auto-enable ATEC defaults or a speculative incomplete first response, never disconnect the room sensor, and abort on CRC, DE mismatch, B11D latch or COMM ERR. Historical FC16 ACK is not semantic acceptance.

Private user Service39 archive SHA256 `9ecae2f2063c81b595e77da4781f8e70c4575a92a56c5a5b5db133164ff9e1e7` (230 CRC-valid entries); contains inherited firmware-derived private code, **not for public redistribution**.
