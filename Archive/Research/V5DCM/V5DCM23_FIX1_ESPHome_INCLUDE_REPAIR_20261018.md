# V5DCM23-FIX1 — Missing ESPHome header copy (offline repair)

Date 2026-10-18. **PREPARED / NOT RUN** for full ESPHome firmware and physical device. Offline C++ source validation **COMPLETE / POSITIVE**.

## User-provided actual compiler result
ESPHome 2026.9.0 / ESP-IDF 5.5.5 / ESP32-S3 failed in generated `src/main.cpp` at include of `v5dcm23_v5dcm19_real_ledger.hpp`, with `fatal error: xtr_v5dcm21_packages.hpp: No such file or directory`.

This is a **build-time missing copied header**, not a native bus error. The separate `ota.password` resource warning is **not the build failure** and OTA credentials/security should not be changed as part of this controlled fix.

## Reproduction and exact cause
Original private source archive `V5DCM23_V5DCM19_REAL_LEDGER_PRIVATE_PREPARED_NOT_FLASHED.zip` SHA256 `127d781089134569299f4e01faa8c380d2176dcd0794e06a7fd971240e6c179d`. Its root contained `xtr_v5dcm21_packages.hpp` and `xtr_v5dcm21_readiness.hpp`, but neither was in YAML `esphome.includes:`, hence absent from generated ESPHome `src` copy even though present alongside original YAML in ZIP. The new private ledger depends transitively on both, with package header itself including readiness.

Audited **all 38 original YAML include entries**, all present in the archive. Investigated quoted includes of bundled sources and verified the local portable `components/thermia_portable_bridge/xtr_core.hpp`, `xtr_frame.hpp`, `xtr_wire.hpp` dependencies are included in archive.

## Single controlled fix
Private artifact **not published**: `V5DCM23_V5DCM19_REAL_LEDGER_FIX1_INCLUDES_PREPARED_NOT_FLASHED.zip` SHA256 `ee6814b29a3412069ec33c7015c9a3ad2f5913e236b8cb4e529d59f83bd3d5e0`. New YAML includes **exactly** two additional lines **before** `v5dcm23_v5dcm19_real_ledger.hpp`:

```yaml
    - xtr_v5dcm21_readiness.hpp
    - xtr_v5dcm21_packages.hpp
```

Other ZIP members unchanged; one new `V5DCM23_FIX1_INCLUDE_AUDIT.json` documents hashes, 40 unique include entries. No component, HA entity, sensor, `state_class`, native frame code, boot stage, UART, pin/DE or TX path changed.

## Offline tests actually executed
- Static ZIP+YAML source audit: **PASS**; 40 distinct declared includes, all present in private ZIP, exact two-line YAML patch and every previous YAML byte preserved.
- `g++ -std=c++17 -Wall -Wextra -Werror -pedantic` host `test_v5dcm23_ledger.cpp` linking original private portable `xtr_core.cpp/xtr_wire.cpp/xtr_frame.cpp`: **PASS**.
- Same strict compiler on `replay_v5dcm23_private.cpp`, replay real historical 20261003 capture: 2687 CRC-valid frames, 162 0x0F FC16, two 0x0F FC23, no C2/Online or TX: **PASS**.

**Not verified:** user's full ESPHome ESP-IDF compilation after repair, OTA flashed/new boot slot, HA/runtime parity, any physical bus TX. All prior known-good runtime baselines intact. Abort if unexpected TX, missing production HA data, or new device crash. User-provided compile log is specific diagnostic evidence; do not request routine compiler output unless further errors occur.

Next: user can try building with FIX1 private source; wait for confirmed compile before flashing. If a new compilation issue occurs, investigate the first actual `error:` without unrelated changes.
