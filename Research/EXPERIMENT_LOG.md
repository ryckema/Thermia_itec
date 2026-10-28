# THERMIA EXPERIMENT LOG

Last updated: 2026-10-28. This restored public status file records non-sensitive outcomes only. Historical user-provided September 2026 snapshots remain separate private source material; their detailed experiment history is not reconstructed or silently overwritten here. See Git commit history and private project captures for earlier raw evidence.

## W2R25F4 — second live capture, added to existing consolidated acceptance

- **Experiment ID:** Same W2R25F4 Heating multiwrite acceptance, continued user-run; not a new firmware experiment.
- **Evidence/time:** 2026-10-28 21:16:16–21:20:05, real controller 2.4.2, new 5,000-line ESPHome user log.
- **Status:** D6 and D12 move **PREPARED / NOT RUN → COMPLETE / POSITIVE (LIVE / LOCALLY VERIFIED)**. D8/D7 reconfirmed under the same session without reboot. D5 remains **PREPARED / NOT RUN**; overall consolidated group **RUNNING / PARTIAL**.
- **Baseline / change:** SAME W2R25F4 firmware and native session; continued independently user-initiated HA edits, not a code change.
- **Expected:** One physical 03E8/14 desired page per explicit edit; new genuine controller FC16 matching selected word and only selected word intentionally changed; no session or transport regression.
- **Actual:** Exactly **7** direct edit intents, **7** actual physical desired-page sends, **7** `CONTROLLER_ACCEPTED` semantic readbacks. D6 `03EB` original 0→1→0→1 (three confirmed edits), D12 `03F4` 22→21→22 (two), D8 `03ED` 0→1, D7 `03EC` 0→1. `deltaWords=1` on all seven constructed pages. The final 7 confirmations are semantic readbacks of the actual controller response; not transport ACK alone. Count across first and second captured logs: **26/26** accepted physical pages, **9/10** distinct descriptors.
- **Busy/ABORT:** One D12 preview denied with `idle=0 NO_TX`; no physical send on denial, subsequent D12 edit accepted. No emergency ABORT used; S92 manual abort and W2R24 rollback preserved.
- **Native integrity:** M6=5 and CURRENT 4/4 remain confirmed, CRC_DIFF=0, RX drops=0, parser resync=0 in sampled statuses. This log records a calendar `12/12` read ARM but **does not itself demonstrate the completed 12/12 read cycle**.
- **Remaining real blocker / ONE next action:** User-initiated single D5 `03EA` Heating Maximum edit on unchanged W2R25F4, confirm controller `03E8/14` FC16 semantic acceptance and other-words integrity, then GO/FIX/NO-GO for complete Heating group.

## W2R25F4 — Heating group consolidated live multiwrite acceptance

- **Experiment ID:** W2R25F4 Heating multiwrite acceptance (one consolidated user-run milestone).
- **Date / evidence:** 2026-10-28, XTR ESPHome supplied log excerpt 21:12:09–21:15:33, 5,000 lines; real iTec XTR M 3N, controller 2.4.2.
- **Status at first capture:** Overall **RUNNING / PARTIAL**. D1, D4, D7, D8, D9, D10, D11 **COMPLETE / POSITIVE**; D5, D6, D12 **PREPARED / NOT RUN** in this first log. The second live capture update above supersedes current per-descriptor status.
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

**ONE NEXT ACTION (updated after second capture):** Complete only D5 with one user-initiated edit and semantic controller-origin readback on unchanged W2R25F4; then GO/FIX/NO-GO.
