# Write User Stable / Write Service Development — Split decision (2026-11-04)

**Decision:** maintain two independent development/release tracks for Thermia iTec XTR M. Current **User Stable** is exact W2R92 privately distributed YAML, confirmed working by the owner; Service is a separate evolving line starting at W2R93-derived **Service DEV S0**. Public GitHub carries only non-sensitive status and instructions; private OEM/TX firmware must not be committed.

| Track | GitHub branch | Private YAML snapshot | Proof |
|---|---|---|---|
| Write User Stable | [xtr-write-user-stable](https://github.com/ryckema/Thermia_itec/tree/xtr-write-user-stable) | W2R92 SHA256 `b20d145018d0ac0de36410f8738054e0841a1bd8563d3bbdf7ba39a7b37d289f` | user confirmed FLASHED/LIVE normal; no new quantified frame capture |
| Write Service Development | [xtr-write-service-dev](https://github.com/ryckema/Thermia_itec/tree/xtr-write-service-dev) | W2R93-derived DEV S0 SHA256 `765b9adb6ea0099bfaaab18e47452ebfdb9dabeee739f09d189a4d0a3394160b` | SOURCE/OFFLINE TESTED only, no new service TX |

**Deliverable:** ONE complete PRIVATE `Thermia_XTR_WRITE_USER_SERVICE_SPLIT_PRIVATE_20261104.zip` with two independently installable standalone YAMLs, installation/ABORT/rollback, track descriptions, audit and SHA manifests. Both keep the original ESPHome name, HA IDs, **exactly one sole S92 UART/RX/TX/DE owner**, V5 CRC, controller-origin FC16, native FC03/calendar, and ABORT. One version at a time on the same physical ESP32/RS485 bus. No service writes activated or silently tested.

**Release policy:**
- USER: frozen functional baseline; only necessary and proven fixes or explicit reviewed backports. No service feature creep.
- SERVICE: starts with full User features but isolated service-menu implementation. New/unproven physical TX remains disabled until explicit bounded user experiment with source, target, genuine FC16/controller-readback, ABORT, rollback and no collisions.
- Keep OEM/private code, protected handshakes and privileged tools in **private files**, not the repository. Do not modify `README.md` or `Write (Beta)/iTec Eco`.
- Source/offline success != ESPHome target compiled or XTR live proof. User W2R92 live confirmation remains accepted; Service DEV S0 is not yet target-compiled/flashed/live.

**CURRENT MILESTONE:** separate stable Write User from new Service development. **DELIVERABLE:** branches + private two-track ZIP. **REAL BLOCKER:** none for track separation; public redistribution requires privacy/license review. **ONE NEXT ACTION:** develop the first genuine SERVICE-menu feature within the one existing S92 engine, leaving User Stable unchanged.
