# V4.1 to V5 S73 — passive bootstrap handoff (2026-10-21)

**ID:** V41-V5-PASSIVE-BOOTSTRAP-01. **Status:** COMPLETE / POSITIVE for source integration and generic host tests; actual native session **RUNNING / PARTIAL**, target ESPHome build and live TX **PREPARED / NOT RUN**.

**Baseline:** Previous private V49 callback-integrated RX-only source; installed V83 RX_ONLY/HARD_DENY unchanged. S62 G01/G02/G04 accepted-risk decisions remain closed in original topology.

**One bounded functional source change:** The existing `NativeEsphome23` gains `observe_passive_bootstrap(phase,pages,acks,faults)`. The original V5 R6-P30D ledger (already processed within existing UART callback) now forwards the observed phase and page/ACK counters. A fault, invalid count or failed ledger revokes the binding and aborts service/transport. A completed 32/32 ledger is **passive evidence only**: it does not create a controller epoch, qualify the owner or slot, bind, arm or send. This is not a new security gate or a replacement for V4.1 native session behavior.

**Validation:** YAML parser with ESPHome `!secret` support confirms 24 root blocks. Existing complete generic GCC C++ host runner yields **36 PASS lines**. This runner does not compile the real `ESP_PLATFORM` IDF adapter; no full ESPHome target build, flash, XTR TX or semantic readback performed. One private source HPP and RX-only candidate YAML modified; installed V83 untouched. Private 311-entry ZIP SHA256 `e679a3741793894740703182b45658608c0021400d771f25a4ac0f55b10f0be9`.

**Next:** Compile actual adapter with genuine ESPHome/IDF, check callback lifetime and target errors; independently ground next controller epoch and continue genuine startup. EXP388 remains partial; G05/G06 physical feedback and B11D initial fault remain open. Abort if unsolicited native TX occurs, DE remains high, or semantic in-flight state is reset. Rollback retains installed V83 and prior private V49 source.
