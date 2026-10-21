# S75 — repeatable callback-gap session invalidation (2026-10-21)

Experiment `V41-V5-S75-REPEAT-GAP-REVOCATION-01`: **COMPLETE / POSITIVE OFFLINE** for limited source modification and generic host suite; ESPHome target build and physical run **PREPARED / NOT RUN**.

Verified baseline: exact S73 private archive SHA256 `e679a3741793894740703182b45658608c0021400d771f25a4ac0f55b10f0be9`; last installed V83 RX_ONLY/HARD_DENY unchanged. V49 original witness is intentionally one-shot; initial S73 integration used a static revocation latch and could miss second return.

**One scoped change:** The existing V5 UART callback now detects each increment in the existing `R6-P24` >=5000 ms **inter-callback** gap counter and calls the pre-existing `NativeEsphome23::observe_unqualified_bus_return()`. New tiny private `GapRevoker75` header supports repeatable edge detection; original V49 witness, R6-P24 counting, B11D and other RX/HA entities remain intact. This is passive invalidation only and is **not** controller-reboot attestation, new epoch, ownership, authorization, TX or restart. It deliberately does not invoke verified recovery nor re-bind.

**Validation:** 38/38 strict GCC C++17 host test executables PASS, including new two-gap repeatability test. YAML parses with `!secret` support and maintains 24 root blocks; includes new header. Host runner does NOT compile actual ESPHome UART lambda or IDF adapter; embedded target compile NOT RUN, no flash/TX. ZIP integrity test PASS for 315 private items, SHA256 `ad5c8831da0706989ae949520f99e6529afb0a11337ea559bbd59fb83a42a5b1` (PRIVATE, not on GitHub).

Abort and rollback: on any unexpected TX, stale binding, lost watchdog/valid-frame bookkeeping or DE anomaly, discard candidate; installed V83 remains untouched, exact S73 ZIP is source rollback. S62 G01/G02/G04 scoped accepted-risk decisions unchanged; physical G05/G06, B11D first fault, EXP388 remain open/partial. Next run an **actual RX-only ESPHome/IDF compile** of S75, not a live test; separately implement source-backed startup/next-epoch qualification. No physical acceptance claim.
