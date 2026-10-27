# V5DCM45-FIX2 — first local passive RX validation (2026-10-19)

**Experiment ID:** V5DCM45-FIX2-LIVE-RX-01. **Status: COMPLETE / POSITIVE — PASSIVE LOCAL XTR RX ONLY.** Native one-shot TX remains **PREPARED / NOT RUN**; no response was sent. This result follows the FIX1 startup-order failure and FIX2 offline source changes.

## Hypothesis and controlled intervention
FIX1 erroneously entered irreversible REVOKED during initial B11D startup even when the RX stream was clean. FIX2 separates B11D-not-yet-ready from a true RX integrity failure and is expected to qualify after >=30 seconds and >=100 new valid frames, without clearing historical error records or permitting output without a fresh qualified native request. **Single change:** user's installation of FIX2 on the ESP32. Baseline: V45/FIX1 passive clean RX, FIX1 source premature REVOKED; known-good fallback V44B no-output. No requested controller reboot, Arm, unsolicited output, writable register, payload or target slave TX in this observation.

**Positive criteria:** QUALIFYING -> QUALIFIED, error counters remain clean, normal HA values continue and DE stays RX. **Negative:** recurrent REVOKED without actual faults, loss of telemetry, new RX errors or unauthorized output. **Inconclusive:** missing qualification window or truncated proof.

## Local raw evidence
User-provided ESPHome API log `Pasted text(20261019-142332).txt`, SHA256 `856d5da48c7870d54b151f022fcdc6837fb6f92ea24ef5818e2e9ad0b555a7f2`, 4,580 logical lines, 356,709 bytes, 16:20:02.423–16:23:01.218 (178.795 seconds). ESPHome 2026.9.0 client successfully connected; cache says validation skipped, so **no claim** of direct compile or flashed binary hash. Current on-device log contains FIX2-specific diagnostic.

### OBSERVED FACTS — XTR-local
- `V5DCM45 FIX2 Current RX Qualification`: first captured 16:20:05.075 `phase=QUALIFYING current=0 frames=93 elapsedMs=10762 frameAgeMs=7 P5_HISTORY=0 reason=NONE`. At 16:20:25.004 `phase=QUALIFIED current=1 frames=262 elapsedMs=30762 frameAgeMs=256 reason=NONE`. All 32 subsequent snapshots remained QUALIFIED, last 16:23:00.014 `frames=1582 elapsedMs=185763 frameAgeMs=48 P5_HISTORY=0 reason=NONE`. Earlier four snapshots QUALIFYING, zero REVOKED or WAITING in the excerpt; beginning of device boot was not captured.
- `V5 Parser Status` 98 frames/17 pages -> 1549 frames/254 known pages; `badGeom=0 unknown=0 resync=0 drops=0 TX=0` throughout reported samples. B11C PUBLIC checked 1540 frames with `crcMismatch=0` by 16:22:54.758; B11D RAW 1528 matched `rawFrames=portableFrames=comparedV5`, zero `noise/incomplete/ambiguous/overflow/nativeFault/countDiff/byteDiff`; B11D first fault NONE, sticky 0, DE_sw/DE_pin 0.
- V44B `armClicks=0 replyAttempts=0 uartAttempt=0 admitted=0 build=1 DE_RX=1 conflicts=0` constant; physical TX attempts, UART Write Calls and delivered TX all zero. No actual user Arm or on-wire answer. Existing HA operating mode, room/outdoor/compressor, DHW and water temperatures continued updating.
- Native P74E local `FC16=251 FC23=0` by 16:22:54.858; separate S8 health `fc16=255 FC23=0`. `owner=UNKNOWN epoch=UNKNOWN slot=UNKNOWN`, no native `0x0F FC23` challenge. `HA Restore 0x02 FC23` counters are other-node traffic and **not** native `0x0F` evidence. Legacy R6 P5 Session Classification remains `UNQUALIFIED / NO_TX` even when separate FIX2 fresh RX witness is QUALIFIED — they measure different conditions.

## STRONG CONCLUSION
The specific premature FIX1 REVOKED issue is corrected on the local XTR for this ~179-second passive observation. The fresh RX witness qualifies and retains current integrity with normal receive-only operation. No physical native reply, DE switching, controller acceptance, native session ownership or actual Online integration is proven.

## Remaining unknowns and next action
Native handshake trigger, controller-origin `0x0F FC23`, sender/owner, epoch, physical response slot/timing, native semantic acceptance, online state: OPEN / UNKNOWN. Do not interpret RX QUALIFIED as native session permission or write acceptance.

**Next:** preserve this as verified passive known-good FIX2; perform offline evidence analysis of why native challenge remains absent using existing firmware/captures, before any separate user-initiated live one-shot. Do not press Arm just to force traffic; it cannot create a controller request. Active experiment would require exact observed trigger, bounded reply, abort/recovery and user-run result; do not induce unsolicited bus output or reboot controller. On abort or new integrity fault, return to V44B known-good no-TX baseline.
