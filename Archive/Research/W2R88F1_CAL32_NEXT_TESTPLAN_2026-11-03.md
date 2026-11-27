# W2R88F1 CAL32 — next user-initiated tests

**PREPARED / NOT RUN** for first F3 parameter change. F1 P4/P5 five-field writes are already COMPLETE / POSITIVE; the W2R88F1 shared F1/F3 editor is LIVE for source read only.

**Source from actual Nov 3 user log:** F3 Silent P1 22:00–23:59 daily and P2 00:00–08:00 daily, both configured. EVU F2 P1 is date-based, F2 P2 is configured 17:00–19:00 but has zero weekdays; F4 Temperature Reduction configured=0/8. Genuine creation and deletion are not implemented in W2R88F1. Do not attempt unsupported records.

**T1 — new-domain F3 P1:** select slot17, require live ready mode1 programmed1 22:00–23:59 daymask0x7F, stage startMinute 00 to 01, press Arm New-Domain Write (45s), then one Apply. Require matching actual controller-origin FC16 for register0x061F and a fresh full owned CAL12 confirming 22:01–23:59 daily plus CAL32_BATCH_DONE exact1 pages1 count1. ABORT on anomaly; do not blindly retry. Restore 01 to 00 using a separate user-arm and independently confirm.

**T2 — only after T1 positive:** F3 P2 five-field combined test under a fresh exact 00:00–08:00 daily source: target 01:15–07:45 Monday/Wednesday/Sunday (daymask0x45), exactly five field changes in one ARM/Apply; require five individual controller FC16 and fresh CAL12 exact count5; separately restore after success. If T1 fails, FIX first.

**Next implementation:** true create/delete via genuine controller mode/metadata and sole S92 owner, then test a disposable new record's round-trip creation and deletion. Not daymask0 as assumed deletion. F2 dates/zero weekdays and F4 empty state are concrete scope blockers for normal edits, not arbitrary uncertainty.

**CURRENT MILESTONE:** cross-domain calendar writing. **DELIVERABLE:** W2R88F1 test plan. **REAL BLOCKER:** no for T1; create/delete not implemented. **ONE NEXT ACTION:** one F3 P1 startMinute 00 to 01 user-initiated trial.
