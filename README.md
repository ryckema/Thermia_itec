## 2026-10-27 — W2R4 XTR semantic Heating Curve 36->35 PROVEN

OBSERVED LIVE: Build MAIN04-W2R4 on XTR M 3N; owner-ACKed M6=5 CURRENT 4/4 original Heating Curve36. User staged35 23:04:40.943, user ARM once 23:04:44.145. EXP444 FAST_HIT and EXP430 DESIRED_SELECTOR_TX 23:04:45.930, selector PHYSICALLY_SENT 23:04:45.949, EXP421 exactly one desired 03E8 page physical TX 23:04:46.132 (attempts1/budget1). At 23:04:46.711 genuine controller-originated FC16 03E8 reports Heating Curve35, log CONTROLLER_REGISTER_CONFIRMED original=36 target=35 otherWordsChanged=0 FC16readbacks=1 physicalAttempts=1. Production Heating Curve and HA main control published35 at 23:04:46.811, cache35 23:04:47.182. CRC_DIFF0 and RX drops0 in observed window; native M6 remains healthy. Unlike a mere transport ACK, actual controller readback proves semantic setting acceptance. Experiment STATUS COMPLETE / POSITIVE; LOCALLY VERIFIED for one user-initiated one-page Heating Curve word0 write only. Other HA parameter writes ON HOLD. No automatic retries, no further safety waiver or repeated identical test needed.

Separate source/UI defect: experimental W2 stage-only candidate republished old 4/4 original36 at 23:04:46.820, AFTER authoritative postwrite FC16=35; normal controller setting remained35. Fix candidate publisher to prefer newer controller readback and invalidate stale 4/4 candidate base, without touching validated physical TX. Legacy EXP378 automatic CURRENT_REFRESH_DEFERRED state7 runtimeAge0 persists and is a separate refresh problem.

CURRENT MILESTONE: First controller-confirmed XTR Heating Curve write ACHIEVED.
DELIVERABLE: W2R4 FLASHED/LIVE/LOCALLY VERIFIED; experiment COMPLETE / POSITIVE.
REAL BLOCKER: stale prewrite M6 snapshot overrides experimental candidate display; automatic CURRENT refresh still deferred.
ONE NEXT ACTION: smallest integrated candidate source-precedence fix from W2R4 preserving proven sole UART/S92 physical send path, no retesting successful write.

---

releasing stable version, read me TBA
