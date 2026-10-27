# PROTO-OFFLINE-69 — RTU timing / callback feasibility audit

**Date:** 2026-10-04  
**Status:** **COMPLETE / POSITIVE — PROTO63 SPLIT-PREFIX PATH IS PHYSICALLY UNLIKELY UNDER THE CURRENT 5 ms IDLE CALLBACK MODEL**  
**Hypothesis:** with the actual v4.1 serial settings (`9600 8E1`) and UART-debug callback timeout (`5 ms`), a valid 9/10-byte FC03 response should normally finish before the debug layer can emit an 8-byte prefix as a separate idle-delimited callback.  
**Controlled change:** offline timing analysis only. No YAML change, TX, compile or flash.

## Source configuration

Current Write Beta v4.1 declares:

- baud: **9600**
- data bits: **8**
- parity: **EVEN**
- stop bits: **1**
- `rx_full_threshold: 120`
- `rx_timeout: 2`
- UART debug callback: `after: timeout: 5ms`

The parser then retains callback bytes in a `pending` buffer and searches function-specific CRC-valid candidate lengths.

## Wire timing

For 8E1, each UART character occupies:

`1 start + 8 data + 1 parity + 1 stop = 11 bits`

At 9600 baud:

- one character = **1.145833 ms**
- Modbus 1.5-character interval = **1.718750 ms**
- Modbus 3.5-character frame interval = **4.010417 ms**
- configured 5 ms debug idle timeout = **4.364 character times**

Frame wire times:

- 8 bytes = **9.167 ms**
- 9 bytes = **10.312 ms**
- 10 bytes = **11.458 ms**

For the PROTO63 ambiguity, after an 8-byte CRC-valid prefix the legitimate longer response tail arrives, if contiguous:

- 9-byte frame: final 1 byte after **1.146 ms**
- 10-byte frame: final 2 bytes complete after **2.292 ms**

Both are substantially shorter than the configured **5 ms inactivity timeout**.

## Feasibility result

If `after: timeout: 5ms` is applied to actual RX inactivity as configured, a physically contiguous 9/10-byte response should not be handed to the lambda as an isolated 8-byte prefix. The remaining byte(s) arrive roughly 1.15–2.29 ms later, before 5 ms of silence can occur.

A 5 ms silence after byte 8 is also longer than the nominal Modbus RTU 3.5-character frame separation (4.010 ms). At the wire-protocol level that silence would already indicate a frame boundary rather than continuation of the same RTU frame.

Therefore the exact PROTO67 adversarial case:

`valid 8-byte semantic prefix -> callback/parse -> later tail bytes of same response`

is **not the expected behavior for a normal contiguous RTU frame under the current 5 ms idle-delimited debug callback**.

## Important qualification

This does **not** prove impossibility in the deployed ESPHome/ESP-IDF stack.

The YAML also configures `rx_full_threshold: 120` and `rx_timeout: 2`; without executing the actual ESPHome UART/debug implementation we should not claim that every callback boundary is guaranteed to correspond exactly to a 5 ms physical idle interval.

The source comment says these settings are intended to prevent ESP-IDF splitting frames into ~7-byte chunks, but that is implementation intent, not an offline runtime proof.

## Relationship to PROTO63–67

- PROTO63: parser ambiguity is mathematically real.
- PROTO65: **0 / 25,031** genuine CRC-valid Online/DCM frames exhibit a double-valid ambiguity.
- PROTO66: sort-order-only fixes are insufficient if arbitrary chunking can expose the 8-byte prefix early.
- PROTO67: such early prefix delivery can cross the semantic TX boundary in an adversarial model.
- **PROTO69:** current physical/configured timing makes that early-prefix callback path **substantially less plausible** for normal contiguous 9/10-byte RTU responses.

## Strong conclusion

The parser issue should remain classified as:

**defensive hardening requirement, not demonstrated live defect.**

For a future refactor, RTU-gap-aware framing is still cleaner architecture, but there is no offline evidence that EXP388/v4.1 requires an urgent parser change.

## Unknowns

- exact callback behavior of this ESPHome/ESP-IDF build under DMA/UART driver edge cases;
- whether UART driver buffering can invoke the debug lambda despite less than 5 ms physical inter-byte silence;
- behavior under electrical corruption severe enough to create abnormal intra-frame gaps.

Those require compiled/runtime instrumentation, not further capture algebra.

## Live status

Unchanged: EXP387 COMPLETE / POSITIVE; EXP388 RUNNING / PARTIAL; EXP383 PREPARED / NOT RUN.