# V5DCM39-REQUEST-BOUND-REFERENCE-01 — PREPARED experiment contract (2026-10-19)

**Status at preparation: PREPARED / NOT RUN.** Later results are separately documented in [RESULT](V5DCM39_REQUEST_BOUND_BACKEND_RESULT_20261019.md). User-initiated offline development; NOT a user-initiated hardware test.

## Hypothesis
The V5DCM38 private output-provider abstraction is missing the immutable complete incoming native request from its `Request` metadata. A separately source-pinned host-only request-bound extension can preserve the exact CRC-verified FC23 frame from the existing B2 parser, feed a *separate confidential backend interface* once, and independently execute the genuine Connect 2.1.105 FC23 **handler** with stubbed cryptography to qualify shape/input/response-placement semantics. These tests must never manufacture physical responder ownership, acceptance, Online or a functional cryptographic answer.

## Known-good baseline and past results
- User-flashed **V5DCM33-FIX-B2**, last XTR on-device 204 s passive RX/HA healthy; 393/393 HARD_DENY, UART writes 0; flashed image SHA unknown. Source parent ZIP SHA256 `fdc09c5927b5a351163db95db96dc467abd43cb27e1e7fc8068782bea4a677c7`, YAML SHA256 `32e1b7c3ea4f7411fb94d6d769370b9ae10874403961403002250b96e4365d46`; rollback **V5DCM23 FIX2 RX-only**.
- Original V4.1 local EXP386/387 COMPLETE / POSITIVE with bounded guarded recovery/semantic path; EXP388 RUNNING / PARTIAL. Original V5DCM32 live RX-rejoin COMPLETE / NEGATIVE after B11D pre-gap integrity fault. New B2 post-gap >90 s live NOT RUN.
- V5DCM34 original Connect source map, V35/V36/V37 host/mocks and V38 interface 318/318. V38 private ZIP SHA256 `9e28f3ed2ae3bf95f79b69c2b72eebf5d228bd306147285aa906a73400be6767`.
- Genuine original Thermia Connect 2.1.105 firmware-derived `modbus_server15.py` source SHA256 `9afc455fb50472012ae31d0767a0c39878647643ea9c37d7155142e097621d4f`; ARM-only cryptographic dependency is not native-executable in this host environment.

## Exactly one controlled source-only change
Add **one new nonflashable request-binding extension with independent tests** on top of the unchanged V38 provider. It accepts a completed original-parser-sourced CRC-validated native FC23 frame, checks a separately pinned private expected request profile, keeps bytes bounded and private, calls an *abstract backend once*, wipes request bytes after preparation, and denies mock output by default (including host, ESP_PLATFORM and ARDUINO). Tests use only synthetic profile addresses and synthetic reply data. The vendor handler source is imported from the user's original external archive **at runtime** and exercised with **fake cryptography and fake register bank**. No vendor algorithm or secrets copied to this work; no production YAML, UART/DE, HA or device change.

## Targets, risks, positive/negative/inconclusive
**Passive input classification only:** native `0x0F` FC23 from the existing CRC/full-frame original B2 callback. Synthetic target fields in fixtures are **not** actual live slave page/write values. **No outgoing native frame, CRC, current register write value, physical reply slot, real retry or transmission timing exists in this offline work**. Main risk is falsely promoting synthetic/source results; all physical authority flags remain false.

**Positive offline:** exact parent sources pass SHA pins; C++ request+CRC/quantity+origin binding and 1-use zeroization tests pass; original vendor handler isolated from pinned original bytecode accepts synthetic valid inputs and rejects invalid/missing bank; output DENY host/ESP_PLATFORM/ARDUINO even when mock-only flag is erroneously combined; absent live sender compile rejects; archive manifest and fresh extract rerun pass.

**Negative:** wrong shape/CRC/foreign/expired/replayed/sticky B11D/P5 can prepare, simulator can reach embedded transport, physical/session/Online flags can become true, source divergence is ignored, or source oracle check fails. **Inconclusive for broader cryptographic parity:** actual vendor binary response cannot run on host and no verified live dynamic reply supplied. No claim of vendor-algorithm parity may be made.

**Abort and rollback:** fail host test/source pin → discard offline extension, no device intervention necessary, retain deployed B2 and unchanged sticky faults. Separate hardware test requires independently current controller state/owner/epoch/slot, protected exact payload+CRC evidence, one explicit response attempt, timing, failure/abort, and FIX2 rollback; not authorized by this source-only test.
