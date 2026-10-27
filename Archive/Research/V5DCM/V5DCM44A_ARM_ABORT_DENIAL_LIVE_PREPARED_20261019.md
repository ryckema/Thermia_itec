# V5DCM44-A — Arm/Abort denial-only device test

**Status: PREPARED / NOT RUN (2026-10-19).** Only the user performs HA button presses. **No native reply TX authorized by this test.**

## Hypothesis and verified baseline
V5DCM43 FIX1 running on local XTR ESP32 can accept HA Arm/Abort button events while preserving compile-time HARD_DENY, actual DE=LOW, UART writes=0 and normal B11C/B11D RX. The user-provided 12:00–12:02 log was analyzed in [first passive result](V5DCM43_FIX1_FIRST_USER_LIVE_PASSIVE_RESULT_20261019.md): parser 1150 frames, 0 resync/drop, B11C/B11D integrity healthy, 0 TX; V43 status `step=0 deny=0 armPressed=0 build=0 UARTattempt=0 owner=? epoch=? slot=? timing=? TX=HARD_DENY`. Exact installed binary SHA UNKNOWN; V43 source original B2 pin retained. Existing fallback is FIX-B2 known-good source and V5DCM23 FIX2 RX-only. Prior V40 7/7 DCM cross-model reference only; V41/V42 source/host; V43 on-device passive positive. Prior local V4.1 EXP386/387 guarded positive, EXP388 partial, V5DCM32 negative.

## Exactly one controlled intervention
Test the already installed, fail-closed V43 HA **button event handling**. No new flash, configuration, bus scan, HP restart, forced challenge, or manually transmitted frame. Record one pre-button snapshot of V43 status + DE + UART Write Calls + parser/ B11C/B11D faults, then click **V5DCM43 Arm One-Shot Native DCM** ONCE in HA Configuration. Wait ~5 seconds, click **V5DCM43 Abort Native DCM TX** ONCE. Observe next 10–20 seconds and retain the smallest native logs/status lines.

**Target:** HA Arm/Abort event handler and no-output 0x0F FC23 response actor; canonical native slave/page request remain observational, **no outgoing payload, CRC, FC16 register/current value, scheduled TX slot or reply latency**. This test is not a native bus transmission. Potential issue is unexpected DE high/software output or RX/HA loss from a handler bug.

## Criteria and abort/recovery
**COMPLETE / POSITIVE only after actual user log:** Arm click visibly processed or explicit denied reason logged, Abort processed/returns idle, V43 `TX=HARD_DENY`, `UARTattempt=0`, original `V5 S3 UART Write Calls=0`, `V5 S2 Physical TX Attempts=0`, GPIO21 DE LOW, RX B11C/B11D fault/resync/drops remain 0, HA sensors still live. The exact `deny` counter may depend on implementation; do not insist it increases without verifying code.

**COMPLETE / NEGATIVE:** any new physical UART write, DE high, RX/HA disruption, parser/B11D/P5 fault, repeated output, or unbounded arm; stop immediately. **COMPLETE / INCONCLUSIVE:** buttons not visible/updates unclear or evidence insufficient to confirm no output.

**Abort:** press Abort once if unexpected output, then stop interaction and use verified FIX-B2/FIX2 RX-only rollback if bus or HA fails; do not force a warmtepomp restart. Existing B11D/P5 sticky diagnostic history must remain unmodified.

**Evidence:** copied timestamped log excerpt around pre-Arm, Arm, Abort, post-20s of `V5DCM43`, `UART Write Calls`, `Physical TX Attempts`, `TX-02`, `DE`, `B11C`, `B11D`, `P5`, parser; note whether HA remained responsive. No result may be labeled COMPLETE before user confirms and supplies observations.
