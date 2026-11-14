# Write User 1.01 — private development build

**Status (2026-11-14):** SOURCE / OFFLINE TESTED — `PREPARED / NOT RUN`. The 1.01 image is **not** a public firmware download, and has **not** been target-compiled, flashed, or live tested.

Write User 1.01 is a private, integrated ESPHome candidate for automatic native DCM session restoration after a physical iTec XTR M controller restart, **without a Home Assistant start button**. It is based on the owner's full FIX19 development firmware, retaining Write User controls, calendar, telemetry, CRC, single RS485/UART/DE ownership, FC16 synchronization, native FC03 refresh, ABORT, and validated parameter-write scope. The private build also retains Service diagnostic entities; it is not identical to the smaller public 1.0 YAML.

## Evidence and scope

- **FIX19 owner LIVE / LOCALLY VERIFIED for the user-armed route:** a different FC23 controller challenge was answered, followed by short/long-aware cold-start FC16 synchronization, fresh CURRENT 4/4, M6=5 transport qualification and repeated FC03 0708 native responses. This establishes the local transport/session behavior, **not** Thermia cloud connectivity.
- **1.01 change (SOURCE / OFFLINE TESTED only):** after a genuinely observed controller bus-loss/return, the existing cold-start engine arms the same one-reply native handshake automatically in the qualified cold episode. No manual trial button. The 90-second lease, same-controller-epoch checks, A80E/A80F cold guard, bus-idle/CRC, sole TX owner, no-peer and ABORT protections remain.
- **Not proven yet:** this exact automatic 1.01 build on the owner's controller. Controller-origin response after a real restart, M6=5, CURRENT 4/4 and continuing 0708 must all be observed for live completion.

## Build distribution and privacy

The verified variable handshake implementation depends on private/protected material from the owner's original Thermia Connect firmware. **The complete private 1.01 YAML/ZIP, handshake constants and implementation are intentionally not published in this public repository.** The prior public [Write User 1.0](./) remains the public firmware download and does not gain the private 1.01 capability from this document. No separate external YAML, cryptographic secret or unverified response has been substituted into the public version.

The owner's private 1.01 ZIP contains the full YAML, exact FIX19 rollback, concise build/flash/ABORT instructions and manifest. The owner flashes the firmware manually. In anomalous operation: use `Configuration | ABORT Native Session` and restore the private known-working FIX19 rollback; no autonomous flashing or expansion of parameter-write permissions.

**Milestone:** automatic DCM after controller restart.
**Real blocker:** the private 1.01 auto-trigger still awaits one owner-initiated live run.
**Next action:** owner flashes private 1.01, restarts only the Thermia controller and checks automatic M6=5 / CURRENT 4/4 / 0708 without pressing HA buttons.
