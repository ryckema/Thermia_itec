# V5DCM20 — live passive XTR M integration validation (2026-10-18)

**Roadmap experiment V5DCM20: PREPARED / NOT RUN.** Source of roadmap: prior-conversation Markdown, Phase 3: V5DCM19 offline model integration; V5DCM20 live passive validate against current XTR bus, no parser regression, no TX. The previously-created file V5DCM20_ISOLATED_CPP_PARTIAL_20261017.md reports a different host-only synthetic 24/24 experiment; **do not treat it as completing the roadmap live experiment**.

**Hypothesis:** V5DCM19 FIX1 continuously and correctly receives, classifies and observes existing XTR traffic without degradation of original production ESPHome functionality, and always maintains native TX HARD_DENY.

**Baseline:** user-confirmed flashed V5DCM19 FIX1 LIVE 2026-10-18 01:19:09–01:22:18, about 189 s, six 30 s joined diagnostic cycles; B11C V5/portable parity 1566/1566, B11D 1564/1564; countDiff=byteDiff=0; one historical RX integrity fault, initial 11 parser resyncs, not rising through baseline; hard-denied 266/266 candidates, physical_attempts=0; HA heating curve=36 and other sensors working. Existing firmware RX-only unchanged.

**Exactly one controlled change:** observational duration, run **10 min passive** on the *already-flashed* FIX1. No new YAML, flash, bus TX, controller reboot, button or equipment disconnect. Capture start and end snapshots of same counters, plus first new fault context if any. 30 s `[V5DCM19]` diagnostics continue to run.

**Relevant fields:** B11C and B11D frames/countDiff/byteDiff/boundary/CRC/drop/incomplete/ambiguous/overflow/fault, V5 parser resyncs/drops/geometry, bridge 11C/11D TX attempts, native executor candidates/denied/physical_attempts, RX health and telemetry, CM930 challenge, 0708/mailbox, epoch/owner/provenance (all passive). FC16 service 085F/5 and configuration page 03E8/14 are observation only; no ACK semantic proof.

**Positive**: sustained incoming frame counters and HA sensor values; countDiff=0, byteDiff=0, no fresh RX drop/resync/integrity incident, zero physical TX, recurrent joined diagnostics. **Negative**: any regression/unexpected native TX/integrity progression; if isolated fault, mark partial/inconclusive with evidence before causal attribution. **Abort**: unexpectedly nonzero physical TX, loss of critical production measurements, rapidly increasing RX errors. **Recovery**: cease logging experiment, ensure native TX remains HARD_DENY, return to previously installed confirmed V5DCM19 FIX1 (or prior known-good V5DCM2 FIX1 if needed). No new controlled write targets or payloads.

**What user should return:** 10 min ESPHome log or two timestamped snippets at start/end containing `[V5DCM19]`, `[B11C-PORTABLE]`, `[B11D-RX]`, `V5 Parser Status`, `V5 TX-02 Native Executor`, `V5 Bridge02 RX Integrity Faults`, `V5 RX Buffer Drops` plus one live heating/temperature sensor. If any errors, include first nearby ~20 lines.

**Unknowns not part of this test:** native controller acceptance, actual DCM icon/Online activation, physical response owner/slot, original V5DCM18 full Core parity. G01–G06 accepted residual risks are not reopened. Experiment is NOT COMPLETE until user supplies duration result or explicitly confirms it.
