# V5DCM44-A user device follow-up — 2026-10-19

**Status: RUNNING / PARTIAL**, linked to [PREPARED](V5DCM44A_ARM_ABORT_DENIAL_LIVE_PREPARED_20261019.md). Device logs provided as two user text files.

**OBSERVED:** two Arm presses (~12:14:59 and ~12:16:56) were refused; an Abort callback executed at ~12:17:00. GPIO21 was reported low; physical UART TX=0; RX, parser and B11C/B11D remained healthy. Last post-event status retains step=7, deny=1, armPressed=1, build=0, UARTattempt=0. The log extends only about four seconds after Abort, not the requested 20 seconds.

**SOURCE-DERIVED:** original OneShot Step::Revoked has value 7; abort intentionally latches that result and V43 retains the button-pressed diagnostic. It is not by itself evidence of active TX or a broken cancellation. No local native handshake or real response seen.

**NEXT:** retain partial because the scoped post-Abort evidence interval is missing; do not repeat Arm to advance unrelated offline work. Existing V43 device remains untouched.
