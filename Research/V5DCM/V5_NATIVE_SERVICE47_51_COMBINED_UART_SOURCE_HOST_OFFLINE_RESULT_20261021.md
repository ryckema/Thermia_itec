# Service-47–51 combined — borrowed ESPHome UART / one guarded native V5 transport

**Date:** 2026-10-21. **Experiment:** V5-NATIVE-SERVICE47-51-COMBINED-UART-01. **Status: COMPLETE / POSITIVE — OFFLINE SOURCE/HOST ONLY.** Actual ESPHome/ESP-IDF codegen or firmware compilation, flash, live RS485 native TX, electrical EOF/slot, Connect C2/Online and semantic setting acceptance **PREPARED / NOT RUN**.

## Baseline, provenance and ONE controlled functional change
Last user-confirmed installed iTec XTR M: V83-family RX_ONLY/HARD_DENY, V49 fallback. EXP388 remains RUNNING / PARTIAL, B11D first startup cause remains OPEN. Prior G01–G06 bounded user-accepted research risks are acknowledged, without treating them as a fresh electrical owner, slot or controller epoch proof.

User-private S46 archive SHA256 `9b4745c5f161ade47772b9c0f4c3f8ac5545deed663c3291099e904a94f6e2ba` is the immutable source baseline. **307/307 original ZIP members CRC-valid and byte-identically rechecked**. All protected original native response backend and authentication material are preserved PRIVATE and unchanged.

**One source change:** replace only the *candidate copy* of original `EspHomePhysicalIo` optimistic void-`write_array` / ignored `flush` result with a single typed borrowed ESP-IDF UART/FIFO/drain adapter, while leaving the original `ScopedTransport23 -> GuardedPort -> PhysicalOwner` one-owner service and B11D/1s watchdog safety callbacks in place. Update the candidate native runtime's UART type to the exact existing `IDFUARTComponent`, and fix YAML pointer-to-reference calls for that instance. No new UART driver, RX reader, protected response generator, authentication algorithm, slave profile or ATEC takeover behavior.

Five engineering work packages share this **same** functional change rather than being counted as five separate physical experiments:

- **S47:** separate, source-only adapter for borrowed ESPHome's existing UART object; exact original V5 service and private native backend unchanged.
- **S48:** bounded `uart_tx_chars` FIFO admission and typed `uart_wait_tx_done` drain with negative/status paths. An unexpected negative FIFO return is treated as possibly uncertain admission. On unresolved drain the candidate latches `UnresolvedInFlight` and may leave DE HIGH; it **must not be flashed/deployed until a separate safe hardware-abort/DE recovery procedure is reviewed**.
- **S49:** the same original GuardedPort/PhysicalOwner is consulted by native B11D 50ms and watchdog 1s. Host tests cover source-defined owned-DE-high decision; real ESP scheduling/interleaving is not proven.
- **S50:** entire original YAML retained with **24/24 production top-level blocks and 403/403 ID occurrences**. 9600 8E1, GPIO17 TX/GPIO18 RX/GPIO21 DE, original UART-debug RX ingress, valid-frame counters, stale watchdog, B11D sticky fault logic, Home Assistant entities and Configuration controls preserved. One brown diagnostic added. All `esphome_service23(id(thermia_uart),...)` calls are corrected to a typed UART reference `*id(thermia_uart)` in candidate YAML. It is named **SOURCE_NOT_FLASHABLE**.
- **S51:** source/identity check **356/356 PASS** (including 307 file-hash checks), new real-original-GuardedPort C++ fixture **4/4 PASS** (GCC strict, noexceptions/noRTTI, UBSan and Clang, against locally mocked ESP-IDF UART/GPIO), **4/4 native/legacy TX macro compile-negative tests correctly rejected**, previous V5 **35/35** host executables PASS, original S46 **32/32** and S45 **28/28** source audit PASS, independently pinned standalone S44 **24/24**, S43 **26/26**, S42 **25/25** source audits PASS.

A full ZIP was independently extracted into a **clean directory** and `run_offline_suite.sh` returned **exit 0** with all included current tests passing. Older S44/S43/S42 ancestry verifiers applied to a newer descendant would reject source difference by design; they were instead rerun correctly on their immutable pinned versions. No such failed descendant run is promoted to a pass.

## Physical/build boundary and source safety
- The **existing Service36 RX-only compiler gate is byte-identical** and still refuses both native/legacy TX macros. Candidate `EspHomePhysicalIo` initializes reviewed FIFO/drain budgets to **ZERO**, so even source construction cannot assert DE with the current runtime. No user ARM or physical reply was executed.
- **NOT COMPILED under ESPHome/ESP-IDF**: `esphome` and `pio` are not installed in this runtime. C++ host stubs compile real checked project classes but are not equivalent to a complete ESPHome translation unit, source-generated IDFs, timing measurements or native session proof.
- Public ESPHome 2026.9.0 and ESP-IDF v5.3.x API source signatures for existing UART, `uart_tx_chars` and `uart_wait_tx_done` were previously reviewed in S44–S46. They do not establish device-specific TX timing/driver behavior without an actual embedded compile and live electrical validation.
- `uart_tx_chars` accepts bytes into UART FIFO; a subsequent successful `uart_wait_tx_done` is a driver-side drain report, not proof of remote receipt, collision-free physical reply slot, complete Online/C2 handshake or semantic setpoint acceptance.
- An unresolved in-flight DE-HIGH condition is **a known deployment blocker**, not a recoverable/approved live policy. Retain the previous negative/inconclusive experiment history, B11D sticky fault and EXP388 incomplete branches.

## OBSERVED FACTS / STRONG CONCLUSION / HYPOTHESIS / UNKNOWN
**OBSERVED (offline):** exact parent source and YAML preserved apart from the two intentional source-header edits and scoped YAML pointer/reference and diagnostics change. Same GuardedPort host test exercises successful simulated FIFO/drain and faults for partial, negative or zero-progress admission, driver loss, invalid port, drain failure, DE-release disagreement and unresolved bytes.

**STRONG CONCLUSION:** it is technically feasible at source/host level to integrate typed UART completion handling within the original one-owner V5 route while retaining RX-only gates. This is not a newly proven hardware-native Connect endpoint.

**HYPOTHESIS:** an independently source-pinned, manually user-scoped future TX target may deliver the historical locally tested V4.1 full-session lifecycle after embedded build, physical safety/owner/slot proof and separately initiated test.

**UNKNOWN:** real ESPHome translation and linking, actual pin/defer/wire timing and safe abort with partial frames, present XTR responder/epoch/slot, B11D first-fault root cause, the remaining EXP388 cancellations, genuine Connect/Online C2 and new semantic writing/readback. Historical ACK / 32-of-32 and FakeIO receipts do not prove any of these.

## Artifact, abort and next action
User-private ZIP `V5_NATIVE_SERVICE47_51_COMBINED_OFFLINE_PRIVATE_20261021.zip`: **324 ZIP entries**, SHA256 `36a0b37dcac6210161f495f76bc007022d61b780c67b64d91688212998df3dcf`, **323/323 independent SHA manifest entries checked** and CRC clean. Includes exact original S46 ZIP, full private source-only candidate YAML/headers, real GuardedPort host fixtures, runner, test logs, source patch, report and reproducible manifests. Contains unlicensed firmware-derived private source; **do not publish or redistribute** protected material. This public research report carries no keys, private handshake logic, 0x0F response implementation or 0x0708 mailbox tooling.

**Abort:** source hash mismatch, B11D fault, DE disagreement, incomplete FIFO/drain, unknown owner/session/slot or any unintended output. **Rollback:** none necessary offline; user-installed V83 RX_ONLY/HARD_DENY untouched, V49 fallback retained.

**NEXT:** complete a **real ESPHome 2026.9.x compile** using the private included source (request compiler output only for diagnosis), independently design/review unresolved-DE hardware abort and actual timing/slot safety; then prepare a separate user-initiated scoped full native TX test with exact private source/payload/CRC, known controller current value, timing, bounds, abort and rollback. Do not auto-enable ATEC V3 or use a lone incomplete response that historically caused COMM ERR.
