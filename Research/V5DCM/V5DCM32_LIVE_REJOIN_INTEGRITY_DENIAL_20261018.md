## Follow-up provenance correction (2026-10-18)

The user subsequently explicitly confirmed **YES, the Thermia controller was manually powered off and back on** around the V5DCM32 live-test interruption. This supersedes this report's earlier *'physical restart not confirmed'* uncertainty at the level of **user testimony**, while exact power transition times, electrical measurements, epoch identity and owner continue **UNKNOWN**. The observed 22:02:30 B11D partial-frame latch, 22:02:43 callback gap, 22:02:45 native FC23 and later `BadIntegrity` denied rejoin remain unchanged. Reset-associated partial framing is a hypothesis needing source/host review, not permission to suppress fault. Live rejoin outcome remains **COMPLETE / NEGATIVE**. Next V5DCM33 offline, no repeat hardware action proposed.


---

# V5DCM32-LIVE-OBS-01 — armed real session transition; integrity-gated RX rejoin denied

**2026-10-18 — status COMPLETE / NEGATIVE for this specific armed live rejoin attempt** (not proof native integration impossible). Retain V5DCM32 overall firmware-soak follow-up as RUNNING / PARTIAL only if tracked separately. Source-only V5DCM32-RX-REJOIN-INTEGRATION-01 remains COMPLETE / POSITIVE offline. Do not conflate source and live results.

## Evidence and baseline
Original user ESPHome log `Pasted text(20261018-200358).txt`, SHA256 `94c3121d56ff70c2bef30e621f82eac97fb80f7b1d7ab2d4e006f1fef6842c11`, 5000 lines 22:00:23.875–22:03:44.723. User-deployed V5DCM32 source-derived RX-only (flashed binary hash not independently verified), earlier fallback user-known FIX2. Prior live logs proved initial operation and manual Configuration arm; no current prior current-session FC23. Single controlled active observation intended: Configuration fresh RX rejoin arm, followed by an apparent controller communication interruption and controller-like native FC23 activity. User has **not explicitly confirmed** physical restart; do not equate observed 12.923s callback gap with physically proven reboot. G01–G06 research risks remain user-accepted.

## OBSERVED FACTS (local current XTR log)
- **22:02:23.181** `[V5DCM32] FRESH_RX_REJOIN_ARMED userArmed=1 NO_TX`.
- **22:02:30.830** `[B11D-RX] FIRST_FAULT RAW_INCOMPLETE_AT_IDLE batch=1307 raw=63 cursor=62 expected=2 NO_TX`. Subsequent B11D snapshots show `incomplete=1 fault=1` persist. This observer fault occurred **before** the R6-P24 callback-gap log.
- **22:02:43.700** R6-P24 detects `CALLBACK_GAP ms=12923 boot=184B7C12 controllerEpoch=UNKNOWN NO_TX`, followed by `GAP_UNQUALIFIED firstSlave=1E health=0 NO_TX`.
- **22:02:45.016** first `[S8] FC23 epoch=1 PageStore_invalidated=1 owner=UNKNOWN NO_NEW_TX`; up to **FC23 epoch=14** at 22:03:40.517. These are **local S8 counter labels**, not independent physical controller-epoch proof. 0x0F shape should be verified in relevant original callback metadata if a further experiment is prepared.
- At **22:02:49.587** and **22:03:19.537** `[V5DCM32] RX_ONLY step=2 scope=1 localGen=0 verdict=5 ... TX=HARD_DENY`. Exact unchanged V5DCM31 `Verdict` enum maps **5=BadIntegrity** and V5DCM32 `Step=2` to **Denied**. Scope did NOT reselect. The original ledger changed from `V5DCM23 profile=1 received=1/33` (22:02:19) to `profile=0 received=0/0` (22:02:49), consistent with FC23 invalidation. V5DCM22 `sinceBoot=3/33`, `sessionCandidate=0/33`, `fc23=2`, `integrity=1`, `revoked=1` at 22:02:49; 9 FC23 by 22:03:19. This is actual RX source-level fail-closed behavior.
- In prior baseline, B11C portable and B11D batch comparisons are 0 frame/byte diffs. At 22:03:19 B11C `V5=3511 portable=3511 countDiff=0 byteDiff=0 boundaryFaults=0 resync=0 drops=0 ioTxAttempts=0 DE=0`; B11D `rawFrames=3177 portableFrames=3177 comparedV5=3177 countDiff=0 byteDiff=0` BUT `incomplete=1 fault=1`. This means parser parity is good for completed frames, **not** that integrity is clean. The B11D raw pipeline stopped committing after the fault and remains latched. RX health cannot be declared clean.
- Software diagnostics show `HARD_DENY` on native executor, `ioTxAttempts=0`, `DE=0` throughout checked event. Electrical line not independently probed.
- Old R6 `D=4 first=STAGE_D_LEDGER_FAULT` existed before this test and continues; separate from the new observed B11D first fault.

## Interpretation
**PROVEN locally:** arm callback works; a >12s frame gap, subsequent native FC23 events and correct one-way RX-ledger invalidation happened on the current device. Integrity guard detected partial raw frame and correctly prevented fresh rejoin, preserving TX denial. This is useful negative test evidence of the complete rejoin hypothesis **under this specific event**.

**STRONGLY SUPPORTED:** partial frame at interruption/recovery might be an expected artifact of controller communication disruption, but without raw bytes and timing proof we cannot decide whether the guard is overly strict, the B11D parser handling needs recovery, or the sequence was genuinely unsafe. A gap preceded by B11D integrity latch is precisely why the policy denies. Do **not** simply suppress or reset the latch to force qualification.

**UNKNOWN:** user physical restart timing (ask one question); whether native FC23 is canonical fresh challenge and from which actual sender; whether B11D idle incomplete is transient/legitimate physical break; recovery health contract; current-source to flashed binary hash; later bus health beyond excerpt; native C2/Online/ownership.

## Criteria and abort/recovery
Positive live would require armed fresh scope, current controlled gap+return+cold+canonical 0x0F FC23, clean required RX evidence and portable reselect to 0/33 with subsequent strict 1/33; **not achieved**. Negative live observed: `BadIntegrity` denies and ledger remains invalidated despite observed FC23. Do not retry physical restart or re-arm as automatic next step. Preserve deployed RX-only, monitor standard HA sensor health; if telemetry freezes/CRC/drops persist, restore previously verified FIX2. The RX-only bridge has no outgoing payload or native slot, no extra TX. No evidence of actual harmful write.

## NEXT ACTION
**V5DCM33-INTEGRITY-RECOVERY-OFFLINE-01 PREPARED / NOT RUN**: first analyze ORIGINAL FIX2/V5DCM32 B11D code and the exact `RAW_INCOMPLETE_AT_IDLE` state transition/latched observer, under a synthetic 12.923s callback gap and 0x0F FC23 burst, preserving original B11C/11D and fail-closed no-TX. Separate canonical post-intervention full CRC boundary and raw-idle fault from physical controller reset. Propose a one-change, host-tested recovery evidence contract, not unconditional integrity reset. Require existing raw capture or smallest future passive log only if source analysis insufficient. **No new physical restart yet.**
