# THERMIA EXPERIMENT LOG



## W2R27 Hot Water D13 local semantic acceptance (first live run)

**2026-10-28 W2R27 first local XTR LIVE evidence — D13 COMPLETE / POSITIVE; D14 PREPARED / NOT RUN.** User ESPHome 5000-line capture 22:43:00–22:46:59, iTec XTR M 3N controller 2.4.2. Before explicit enable: `USER_WRITE_DENIED d=13 grant=0 ... NO_TX` at 22:46:11/22:46:22 (correct guard). At 22:46:32 `USER_WRITES_ENABLED epoch=11230 HW_D13_D14_TRIAL=1`. **D13 Hot Water Mode reg 042F:** 1→0, user edit 22:46:37, descriptor page 042E/15 W3/W1 0008, physical desired page 22:46:39.883 (35 bytes, 1 changed word, S92 DE LOW), genuine controller-origin FC16 `CONTROLLER_ACCEPTED d=13 actual=0` 22:46:40.462. Reversal 0→1 user edit 22:46:52, physical page 22:46:52.885, `CONTROLLER_ACCEPTED d=13 actual=1` 22:46:53.482. **2/2 physical sends, 2/2 semantic acceptances, no blind retry.** Maintained M6=5, CURRENT 4/4 (snapshot generation 5), AUTO calendar 12/12 observed 22:46:08, sampled CRC_DIFF=0, RX buffer drops=0, parser resync=0. **D14 0433 has NO user edit/physical TX/semantic acceptance in this log; remains PREPARED / NOT RUN.** Diagnostics `Thermia Firmware Build` still prints `W2R25F4` at 22:46:37 even while active `W2R27` physical code and D13 042E/15 are explicitly logged; **stale build label is a nonblocking source defect** to fix in next firmware revision, not evidence of old runtime or write failure. W2R25F4 remains latest baseline fully validated for Heating; W2R27 is FLASHED / LIVE / LOCALLY VERIFIED for D13 only, *not* D14 or broader hot water functionality. **CURRENT MILESTONE:** Hot Water Write User. **DELIVERABLE:** W2R27 D13 COMPLETE / POSITIVE (2/2), D14 pending. **REAL BLOCKER:** no D14 live semantic result; unit uncertain. **ONE NEXT ACTION:** user-initiated bounded reversible D14 Startup HT 5→6→5 on same W2R27 session, with controller-origin FC16 confirmation and ABORT/rollback as supplied; no new compile/flash and no D13 retest.



**2026-10-28 W2R27-HW-D13-D14-S92 — SOURCE / OFFLINE TESTED; PREPARED / NOT RUN.** Integrated two source-mapped Hot Water user descriptors D13 `0x042F` (mode 0/1/2) and D14 `0x0433` (Startup HT 1–30, unit uncertain) on controller page `0x042E/15` via the *existing* sole S92 UART/RX/DE physical writer and OEM descriptor ledger, not the separate EXP378 queue. Added 0708 desired/current selector W1/W3 mask `0008` (`1801/1803`), one selected-word 35-byte desired page guarded by CRC/epoch/M6=5/CURRENT/owner, and controller-origin full 15-word FC16 acceptance/negative-release/ABORT; no blind retries. Existing explicit user enable button and all HA entity IDs preserved; Heating D1/D4–D12, CURRENT 4/4, calendar 12/12, native session behavior and rollback retained. Complete **private** firmware ZIP generated with manifest, experiment instructions and unchanged W2R25F4 and W2R24 rollbacks. Offline PyYAML parse, 1099 unique IDs, 225 C++ lambdas delimiter checks, unchanged sole UART writer, selector CRC and ZIP integrity PASS. **NOT ESPHome TARGET COMPILED; NOT FLASHED; NOT LIVE / LOCALLY VERIFIED.** W2R25F4 remains last LIVE / LOCALLY VERIFIED baseline (Heating 10/10, 27/27), and W2R26 Hot Water is COMPLETE / NEGATIVE physical TX. **REAL BLOCKER:** first true controller-origin semantic FC16 acceptance for D13/D14 remains unverified on the XTR. **ONE NEXT ACTION:** user compiles W2R27; upon successful build, user-flashes and initiates bounded reversible D13 then D14 edits with ABORT/rollback available; review actual controller readbacks for GO/FIX/NO-GO.



**2026-10-28 live W2R26 attempt: COMPLETE / NEGATIVE for actual Hot Water control; COMPLETE / POSITIVE for intent staging only.** Two overlapping user ESPHome excerpts (21:40:53–21:44:27) show genuine native M6=5 recovery, CURRENT 4/4 and calendar 12/12; requests for D13 042F Hot Water Mode 1→0 at 21:43:39 and 21:44:09, and 1→2 at 21:44:22, each log `HW_MODE_PREPARED ... NO_TX=1`. There is **zero** `GENERIC_PAGE_TX_EXECUTED`, zero `CONTROLLER_ACCEPTED` and no Hot Water controller parameter change. This is the intentional physical TX HOLD in W2R26, not controller refusal. Earlier W2R26 PREPARED / NOT RUN status superseded for staged preview but NOT for parameter TX. Heating W2R25F4 10/10 27/27 baseline remains last user-verified real write firmware. **REAL BLOCKER:** Hot Water descriptors are not integrated through one S92 guarded physical selector/desired-page and controller FC16 semantic acceptance path. **ONE NEXT ACTION:** implement consolidated supported Hot Water descriptors in same engine and deliver ONE full firmware ZIP with bounded user-triggered activation, ABORT and rollback; do not offer preview-only ZIP as physical-write test.

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
