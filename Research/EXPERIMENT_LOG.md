# THERMIA EXPERIMENT LOG

Last updated: 2026-10-28. This restored public status file records non-sensitive outcomes only. Historical user-provided September 2026 snapshots remain separate private source material; their detailed experiment history is not reconstructed or silently overwritten here. See Git commit history and private project captures for earlier raw evidence.

## W2R25F4 — Heating group consolidated live multiwrite acceptance

- **Experiment ID:** W2R25F4 Heating multiwrite acceptance (one consolidated user-run milestone).
- **Date / evidence:** 2026-10-28, XTR ESPHome supplied log excerpt 21:12:09–21:15:33, 5,000 lines; real iTec XTR M 3N, controller 2.4.2.
- **Status:** Overall **RUNNING / PARTIAL**. D1, D4, D7, D8, D9, D10, D11 **COMPLETE / POSITIVE**. D5, D6, D12 **PREPARED / NOT RUN** from this log.
- **Hypothesis:** Multiple sequential, independently user-initiated Heating edits can reuse the single native-owned 03E8/14 write engine and be semantically accepted by XTR without ESP reboot or global session cap.
- **Baseline:** Locally verified W2R24 D1/D4 one-shot; W2R25F4 prepared integrated source with OEM min/stop ranges, controller-FC16 cache provenance fix and explicit enablement.
- **ONE change under test:** W2R25F4 integrated repeated Heating descriptor writes and fixed cache provenance/OEM limits; preserve S92 sole owner and safeguards.
- **Expected:** One desired 03E8/14 page per deliberate edit, exactly selected register changed, genuine controller-origin FC16 actual equals target; no concurrent writes, CRC issues, or session loss.
- **Actual:** 19 HEATING_DIRECT_USER_EDIT, 19 GENERIC_PAGE_TX_EXECUTED, 19 CONTROLLER_ACCEPTED; each actual selected value equals target, and D1 explicit otherWordsChanged=0. D1 4x; D4 3x; D7 2x signed; D8 2x signed; D9 5x; D10 2x; D11 1x. Total 19. Latest matching controller FC16 page synced HA controls. One d10 PREVIEW_DENIED due to idle=0 generated NO_TX; later D10 successful.
- **Native/session side evidence:** M6=5 throughout sampled writes; controller CURRENT 4/4 and calendar 12/12 completed in capture. CRC_DIFF=0, RX drops=0, parser resyncs=0 in sampled statuses.
- **ABORT / rollback:** Existing S92 ABORT; last verified rollback W2R24 (D1/D4), historical W2R19. No emergency abort required in this captured run.
- **Scope boundary:** Do not assert full Heating group until D5, D6, D12 receive their own controller-origin semantic proof. Do not extend to DHW/cooling/operating-mode writes without separate scope.

## Historical baseline (not superseded as evidence)

2026-10-28 W2R24 LIVE / LOCALLY VERIFIED D1 37→40 and D4 21→22 using a one-shot-per-boot guard; controller-origin 03E8/14 FC16 and unchanged remaining words. W2R25F2 was flashed but D1/D4 edit attempts were denied by session=0, with no Heating physical TX; not controller rejection. F3 remained unflashed and was superseded by F4. OEM Connect baseline recognizes per-register update, alert/read and controller readback; automatic retries differ in our experimental XTR engine.

**ONE NEXT ACTION:** Complete D5/D6/D12 together on the current W2R25F4 (explicit user-initiated bounded acceptance); evaluate GO/FIX/NO-GO based on genuine controller-origin semantic readbacks.
