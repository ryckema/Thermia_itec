# V5 native S65–S70 combined offline verification (2026-10-21)

ID: V5-NATIVE-S65_S70-INTEGRATION-AUDIT-01. Main test and audit result **COMPLETE / POSITIVE OFFLINE**. Native session binding S67/S68 **RUNNING / PARTIAL** (host/source only). Embedded ESPHome target build and flash **PREPARED / NOT RUN**.

## Baseline
Exact private S64 archive SHA256 `28588fd60919f68e86d4b6655d75fa687b7056c4af5bb42be698a4e39a947f36`. Last installed user-confirmed V83-family RX_ONLY/HARD_DENY, V49 rollback; EXP388 partial and B11D first fault open. S62 G01/G02/G04 operational risk accepted/closed under unchanged setup and not reopened.

## Observed S65–S70 work and evidence
Initial original S64 full runner FAILED on an old host test assertion: a negative `uart_tx_chars` result was incorrectly expected to drain and release DE. Current S64 deliberately preserves unresolved state and DE HIGH for uncertain FIFO admission. The false-positive test expectation was repaired **in the test code only**; two explicit host tests were added: known-admission drain later succeeds and explicit reset reverts safely to RX without automatic TX; unknown FIFO admission remains latched across reset. This initial failure is retained, not erased.

**Source comparison:** zero differences to non-generated private S64 production source. Changes are to `TESTS/test_safe_reset.cpp`, plus verifier harness packaging/report only. RX-only production YAML SHA256 `d30f7d3c43672f34aa2efbc19144e6ee255f89132a782b82afc77efd4b881e16` exactly unchanged: 24 root blocks, 403 IDs. 28/28 source predicates PASS; compile-deny guard retained. Full corrected runner PASS: 8 C++ variants of safe reset and reset propagation using GCC strict/GCC no-exceptions/GCC UBSan/Clang; existing host suite 34 test names passed, totaling 42 explicit PASS lines. Stubbed ESP_PLATFORM adapter branch built, not real IDF firmware. No device, flash, physical electrical measurement or TX.

## Per-stage status
- S65 COMPLETE / POSITIVE OFFLINE: adapter in hardware-oriented mocked ESP_PLATFORM host fixture.
- S66 COMPLETE / POSITIVE OFFLINE: regression cases covering unknown FIFO admission, deferred drain, sticky higher owner faults and explicit safe reset. G05/G06 physical DE remains OPEN.
- S67 RUNNING / PARTIAL SOURCE: existing NativeEsphome23 binding/profile/arm APIs reviewed, but production YAML does not call them; it keeps `set_same_owner_supervisor_wiring(false)`, controller epoch zero, peer false, slot false, source profile false. There is **no qualified native session binding** and no safe basis to auto-enable it.
- S68 RUNNING / PARTIAL HOST: existing FC16/FC23/FC03/C2 host tests are not locally verified XTR native full-session/semantic readback.
- S69 COMPLETE / POSITIVE OFFLINE HOST: tests and YAML audit pass, genuine ESPHome/PlatformIO target compile NOT RUN (toolchain absent); no invented compile result.
- S70 COMPLETE / POSITIVE PACKAGING: standalone private 319-entry ZIP SHA256 `12967fa652c572ba2b0e032cf527e1cfa5321e69f5d1af62c6846d97d8278928` containing original S64 source, corrected host test, script, audit, manifest, log and result. Protected source stays PRIVATE.

## Classification and next action
PROVEN offline: exact source preservation; regression test correction and pass; guarded typed FIFO/DE C++ stub behavior; negative TX builds. STRONGLY SUPPORTED: source-level unknown admission must remain fail-closed, even if generic drain later succeeds. UNKNOWN/OPEN: actual physical DE feedback/recovery, real embedded build, runtime native session/C2, semantic XTR acceptance, B11D first fault, EXP388. No physical/semantic claims upgraded. Next: obtain actual ESPHome/IDF build and independently review source-backed native binding/profile evidence; no repeated G01/G02/G04 study absent changed configuration. Actual bus TX only separate user-initiated bounded experiment.