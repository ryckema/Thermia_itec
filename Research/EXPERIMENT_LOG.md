# THERMIA EXPERIMENT LOG

## W2R26 — Hot Water Mode source integration (not live)

**2026-10-28 W2R26 integrated Hot Water Mode preparatory candidate — SOURCE / OFFLINE TESTED; PREPARED / NOT RUN.** Built one private complete ZIP on unchanged user-verified W2R25F4 Heating 10/10 baseline. Existing Home Assistant Hot Water Mode control (`0x042F` word 1 of controller-origin `0x042E/15`, descriptor 13; Comfort=0 / Eco=1 / Holiday Eco=2) now stages only one RAM-scoped intent after native M6=5, session/epoch, current 4/4, owned source/cache freshness and OEM geometry checks. It restores confirmed controller selection in HA rather than pretending to have changed controller. Preview auto-invalidates on fresh controller 042E FC16. The legacy EXP378 queue remains disabled; no new UART/RX/DE writer, no new `.write_array`, no physical parameter TX, no changes to Heating path/ABORT/rollback. Offline YAML parse and ZIP integrity pass; NOT ESPHome TARGET COMPILED / NOT FLASHED / NOT LIVE. **Real blocker:** existing shared OEM physical selector/desired-page/FC16 acceptance remains scoped to Heating 03E8. Integrating descriptor 13 atomically into that same guarded ledger is still required. **ONE NEXT ACTION:** implement descriptor 13 in existing shared selector, desired TX, semantic FC16 and ABORT chain, then deliver bounded user-initiated Hot Water experiment; avoid speculative parallel EXP378 writer. Keep HA parameter writes for Hot Water ON HOLD until proven and authorized.


Last updated: 2026-10-28. This restored public status file records non-sensitive outcomes only. Historical user-provided September 2026 snapshots remain separate private source material; their detailed experiment history is not reconstructed or silently overwritten here. See Git commit history and private project captures for earlier raw evidence.

## W2R25F4 — Heating consolidated milestone closure

- **Experiment ID:** W2R25F4 Heating multiwrite acceptance, continuation, no firmware change.
- **Hypothesis:** D5 Heating Maximum works through the existing user-initiated desired-page path.
- **Baseline:** prior 26/26 acceptances spanning nine Heating descriptors.
- **ONE change:** user edited D5 40→42 on unchanged W2R25F4.
- **Expected:** one changed word, one physical page, genuine controller FC16 acceptance, M6/CURRENT/calendar stable.
- **Actual:** Third XTR user log 2026-10-28 21:21:36–21:25:35: D5 Heating Maximum reg 03EA word2 user edit 40→42 at 21:25:18; one desired 03E8/14 physical page with deltaWords=1 at 21:25:28 (S92 DE=LOW); real controller-origin FC16 semantic CONTROLLER_ACCEPTED d=5 actual=42 at 21:25:29.481. M6=5; calendar AUTO_CAL_TWELVE_OWNED_ACKED 21:22:02 and 21:25:32; CURRENT 4/4 confirmed 21:22:26.991; sampled CRC_DIFF=0, RX drops=0, parser resync=0. Other d7/d8 preview attempts while busy correctly NO_TX. Combined three capture evidence: 27/27 physical Heating writes semantically accepted across all ten descriptors.
- **Status:** **COMPLETE / POSITIVE**, 10/10 descriptors and 27/27 physical user writes with semantic readback.
- **ABORT/rollback:** no ABORT required; existing S92 abort and verified W2R24 fallback retained.
- **ONE NEXT ACTION:** roadmap step 2, integrate supported Hot Water writes in the same engine, without expanding physical TX before user-initiated bounded experiment.

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
