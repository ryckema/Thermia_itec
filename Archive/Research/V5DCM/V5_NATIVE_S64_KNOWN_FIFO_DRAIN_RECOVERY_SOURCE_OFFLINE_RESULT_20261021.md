# Service-64 — bounded native UART/DE physical adapter source integration (2026-10-21)

**ID:** V5-NATIVE-S64-KNOWN_FIFO_DRAIN_RECOVERY-01. **Status:** COMPLETE / POSITIVE — source integration and three generic C++ host tests; ESPHome/IDF adapter build and physical TX PREPARED / NOT RUN.

**Verified baseline:** Exact uploaded private S60 zip SHA256 `e0c7fa49b58d9ef1c68cb90f7226ce42cc6bb2ce886c0c83e296f52299933561`. Installed V83 RX_ONLY/HARD_DENY, V49 rollback; EXP388 RUNNING/PARTIAL and B11D initial fault OPEN. S62 G01/G02/G04 scope-bound accepted-risk closures remain intact.

**One source change:** Modified private `CORRECTED_SOURCE_ONLY/v5_native_tx_esphome_io.hpp` only, in `EspHomePhysicalIo::leave_de_rx()`. Existing implementation latched `unresolved_` after drain failure but could not clear it even if all **known FIFO-admitted** bytes later successfully drained and MCU DE observed LOW. New logic refuses resolution for `admission_uncertain_`, but after successful bounded `uart_wait_tx_done`, `de_.turn_off`, both ESPHome switch and sampled GPIO LOW, clears IO `unresolved_` only when `admitted_>0 && drained_`. Higher GuardedPort/ScopedTransport owner fault remains sticky until explicit `reset_rx_only`. No automatic rearm, no invented firmware-native session qualification.

**Validation:** ZIP original SHA verified, 3 original GCC C++17 generic tests passed (`fix2_guard_test.cpp`, `tests/test_guarded_port.cpp`, `tests/test_service23_scoped_transport.cpp`). Rebuilt private 306-entry archive, CRC-clean and fresh contents manifest, SHA256 `28588fd60919f68e86d4b6655d75fa687b7056c4af5bb42be698a4e39a947f36`. One-HPP unified diff included. No full existing test suite or ESPHome/IDF adapter compile, no flash, no actual XTR TX.

**Limits:** generic host tests do not compile active ESP_PLATFORM IDF branch, so adapter behavior and physical reset remain UNVERIFIED. MCU GPIO21 LOW is not independent RS485 differential DE feedback. A generic drain success cannot resolve uncertain FIFO admission. This remains a private SOURCE_NOT_FLASHABLE candidate. Keep production YAML, Home Assistant, B11D watchdog, bus-health, stale timer and hard TX denial untouched.

**Abort/rollback:** Never install as TX firmware or infer electrical/semantic acceptance from a host pass. Discard candidate and retain last user-verified V83 RX-only or private S60 parent if further checks fail. Next focus a hardware-faithful IDF adapter host stub and actual ESPHome compile before a separately user-scoped live test. Do not re-open G01/G02/G04 absent setup change/contradictory evidence.
