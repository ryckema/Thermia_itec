# Service-52–58 combined: owner reset must prove DE LOW (offline)

**Date:** 2026-10-21. **ID:** V5-NATIVE-SERVICE52-58-COMBINED-SAFE-RESET-01. **Status:** COMPLETE / POSITIVE **OFFLINE SOURCE/HOST ONLY**. Embedded compile/flash, physical DE safety proof, current XTR online C2/session and semantic readback **PREPARED / NOT RUN**.

## Baseline and single source delta
Installed user-confirmed V83-family RX_ONLY/HARD_DENY, rollback V49; EXP388 RUNNING/PARTIAL, first B11D fault OPEN. User accepted historic installation-scoped G01–G06 experimental risks but has NOT initiated active S52–58 TX.

Source pinned S47–51 ZIP `36a0b37dcac6210161f495f76bc007022d61b780c67b64d91688212998df3dcf` verified CRC and hash. This round makes **ONE source change** in a separate candidate: `GuardedPort::reset_rx_only()` previously discarded `PhysicalIo::leave_de_rx()` result and cleared `PhysicalOwner` sticky fault even when DE did not become LOW; new implementation returns bool and requires both release success and observed RX/DE LOW to clear the fault, else keeps fault latched. Existing parent candidate headers except this header are byte-identical and a separate SOURCE_NOT_FLASHABLE YAML copy is byte-identical to prior S47–51 YAML. No UART driver/reader/writer addition, parser/room-sensor/HA edit or physical send.

## S52–S58 outcomes
- **S52** no `esphome` or `pio` binaries installed. Real ESPHome 2026.9.x/IDF schema, codegen, compile/link NOT RUN, and no claim that C++ mocks constitute embedded compilation.
- **S53** actual inherited `GuardedPort` host fixture (mocked IDF I/O) in 4 modes strict GCC, noexceptions/noRTTI, UBSan and Clang PASS. Negative mock: drain cannot finish, DE stuck HIGH, reset returns false, existing fault stays sticky and new grant denied. Positive mock: DE genuinely LOW and safe release returns true, reset succeeds. This prevents unsafe software rearming, not physical repair of DE.
- **S54** B11D 50ms + DE-watchdog 1s original callback service ownership preserved; prior host regressions PASS; physical scheduling NOT TESTED.
- **S55** offline original native startup/session source unchanged; no freshly verified original Connect C2 success or genuine XTR application acceptance. ATEC external source and cross-model claims are not promoted to local truth.
- **S56** FC16 transport ACK and FC03 host-model readback remain distinct from semantic acceptance; no active semantic readback done.
- **S57** separate RX-only source YAML byte-identical to S47–51; 24 production top-level blocks, 403 `id` field occurrences, original UART 9600 8E1 pins 17/18/DE21, valid-frame counters, stale watchdog, B11D and HA Configuration preserved. 4/4 prohibited native/legacy TX switches still compile-fail.
- **S58** independent verifier **316/316** source/lineage checks PASS, new 4/4 C++ host modes PASS, original pinned S47–51 full `run_offline_suite.sh` exit 0, inherited V5 **35/35** and S46 verifier **32/32** PASS. Two preliminary validator false positives (YAML AST object identity and mistaking existing conditional TX macros for actual defines) were corrected and retained in private report, not hidden.
- NO physical bus TX, GPIO activity, ESP32 flash, original C2, physical EOF slot or confirmed heater setting acceptance.

## Safety assessment
**OBSERVED FACT / source:** prior `reset_rx_only()` was able to clear the fault without verified DE release; source-only fix now refuses reset while output is physically unconfirmed. **STRONG CONCLUSION:** this is a necessary fail-closed property before considering an active native TX target. **OPEN / UNKNOWN:** real UART shifter completion, physically safe recovery from unresolved in-flight bytes/DE-HIGH, B11D first cause, exclusive native response slot/controller epoch, current Online/Connect session and true semantic controller readback. In particular, S47–51's unresolved in-flight branch may keep DE HIGH and block RS485; this is still a physical **NO-GO** for deployment. No unsupported timing or ATEC V3 auto-TX defaults have been added.

## Artifact, rollback, next
Full user-private ZIP `V5_NATIVE_SERVICE52_58_COMBINED_SAFETY_OFFLINE_PRIVATE_20261021.zip`, 317 entries, SHA256 `5e45798f3ea7bf7375920b1c73fdf20e926a4f0522f027d4f22c182786b01c3e`; pinned original private S47–51 ZIP included, along with source-only safety delta, replay verifier, tests and report. Protected firmware-derived code must remain private. This public report contains no protected handshake logic/key/native responder or 0x0708 mailbox source.

**NEXT:** acquire actual ESPHome 2026.9.x compiler and verify source-only YAML; independently review hardware-safe DE recovery and actual owner/slot before constructing a separately user-initiated bounded TX experiment. Abort on unowned output, DE disagreement, unknown slot/epoch or fault. User-installed V83 RX_ONLY/HARD_DENY remains; V49 rollback unchanged.