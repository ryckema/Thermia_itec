# W2R88F2 F3 P1 — user-confirmed restoration resolves apparent persistence discrepancy

**Experiment: COMPLETE / POSITIVE for locally verified one-field F3 controller write.** Full postwrite `CAL32_BATCH_DONE` still **OPEN / not captured** (it is not necessary to repeat the proved one-field write). **Follow-up read-only CAL12: COMPLETE / POSITIVE for current restored controller state**, not proof that original target persisted through a full separate CAL12 transaction.

## OBSERVED FACTS
User's first log `Pasted text(20261103-224922).txt`: at 23:49:00 W2R88F2 native sole S92 owner executed one physical OEMW23 F3 P1/slot17 start-minute reg0x061F 0→1; at 23:49:01 genuine controller-origin FC16 exact value1, passive controller page diff 0000→0001, at23:49:08 native Silent Mode P1 source read 22:01–23:59 daily. M6=5, CRC_DIFF=0, RX drops0, no retry. This proves target reached real controller (not just host UI or transport ACK). At23:49:02 owner requested final complete CAL12; first log ended23:49:13 before terminal event.

User's second log `Pasted text(20261103-225440).txt` starts23:51:09 (gap from first log), shows repeatedly Silent P1 22:00–23:59 daily; 23:53:31 auto CAL12 read was independently requested, and at23:53:47.305 `APP_READ_OWNED_RECEIPT_COMPLETE requested=12 pages epoch=8262`, followed by `CAL32_SNAPSHOT_READY slot17` 23:53:47.382 with 22:00–23:59, daymask0x7F. No `CAL32_BATCH_DONE` for original trial in this file.

**Decisive user clarification:** `ik had het al weer veranderd naar 22:00` — user intentionally restored Silent Mode P1 back to 22:00 between captures. Thus the later state at 22:00 is **EXPECTED**, not autonomous controller reversion or disproved persistence. The exact time/route of user restoration was not logged, so DO NOT claim a second independently recorded TX/FC16 trace or full terminal CAL12 for original trial. A previous assistant NO-GO inference (spontaneous revert) is **SUPERSEDED by explicit user evidence**.

## STRONG CONCLUSION
The bounded first F3 P1 semantic write is **COMPLETE / POSITIVE** at field/controller-origin level. Full original postwrite 12-page batch terminal remains unobserved, but is a nonblocking diagnostic gap, not an observed rejection. No need to repeat 00→01. Based on clean bus and exact controller page evidence, **GO** for the originally planned F3 P2 five-field combined test. One user-initiated ARM45s + one Apply after fresh genuine source. F2/F4 create/delete are separate future work.

## NEXT TEST — PREPARED / NOT RUN
Silent Mode P2 shared slot18 source historically `00:00–08:00 days=0x7F` daily, verify actual `SLOT READY` before staging. ONE combined five-field target `01:15–07:45 days=0x45` Monday+Wednesday+Sunday. Fields changed: startH0→1, startM0→15, stopH8→7, stopM0→45, days0x7F→0x45. Explicit `Arm New-Domain Write (45s)` and one `Apply Selected Slot` while source and M6 qualify; retain existing F3/owner guards; expect five exact controller FC16 receipts and **fresh independently owned CAL12 full 12 pages** with F3 P2 exactly target, ending `CAL32_BATCH_DONE exact=1 pages=5 count=5`. Abort/stop if guard fails; no blind repeat. After confirmed completion, restore original `00:00–08:00 daily` using a **separate explicit user-initiated** ARM and Apply, verifying controller final state (firmware rollback cannot restore schedule). If any partial change, first read actual controller state before deciding inverse. Note real Silent Mode scheduling may change temporarily during test.

**CURRENT MILESTONE:** cross-class F3 single-field semantic write proven; multi-field remains next.
**DELIVERABLE:** corrected experiment conclusion and bounded five-field plan.
**REAL BLOCKER:** no real blocker for bounded F3 P2 trial, though full terminal CAL12 behavior must be examined in trial.
**ONE NEXT ACTION:** user explicitly runs one F3 P2 five-field batch and supplies ARM→FC16→CAL12 end log.
