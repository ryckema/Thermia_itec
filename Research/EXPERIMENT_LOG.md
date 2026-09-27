## EXP263 — accelerated 12-block 33-word batch — COMPLETE / STRONG POSITIVE

## EXP264 — end-of-bulk sync tail — PREPARED / NOT RUN

Hypothesis: preserve the complete proven prefix through `06C5/33`, then ACK exact `06EA/7`, `06F1/3`, and `06F4/19` once each. After `06F4` ACK, capture the first different FC16 or FC03 and do not answer it. A `0708/6` FC03 is logged specifically but never answered in EXP264.

Negative/stop criteria: retry of the previous stage, unexpected FC16, any FC03 before tail completion, parser resync delta, RX drop delta, approval retry, peer FC17/ACK, or >5 s stage timeout.

Hypothesis: after the proven prefix through 0546/count20, ACK exact 055A, 057B, 059C, 05BD, 05DE, 05FF, 0620, 0641, 0662, 0683, 06A4 and 06C5 (all count=33), then capture only. Genuine Eco 5 predicted 06EA/count7.

Observed:
- Approval +1283 ms after controller return; R1 sent once.
- All twelve 33-word pages appeared in the expected order and were ACKed exactly once.
- First different post-06C5 frame: 06EA/count7, +475 ms after 06C5 ACK.
- Raw 06EA request: 0F1006EA00070E000A00200017001B0009001A0006F81A.
- 06EA not ACKed.
- Parser resyncs 0; RX buffer drops 0 after the run; DE LOW.
- No approval retry after R1 and no stage retry observed.

Conclusion:
Local XTR now confirms the genuine Eco 5 synchronization chain through the complete 055A..06C5 33-word run and exact 06EA/count7 next. Full Online/Link establishment remains unproven. Negative result retained: the session was intentionally stopped before 06EA ACK, so runtime/mailbox completion was not tested.

Recovery: one normal Thermia-controller reboot.

## EXP262 — accelerated 04A6..0546 ACK batch — COMPLETE / STRONG POSITIVE

Hypothesis: after the proven prefix through `0492/11`, ACK exact `04A6/13`, `04BA/22`, `04D8/27`, `04F6/14`, `050A/19`, `051E/10`, `0532/18`, and `0546/20` in order, then capture the first different FC16/FC03 without answering it.

Observed result: all eight new stages appeared in the predicted order and were ACKed exactly once. The first different frame after the `0546/20` ACK was exact `055A/count33`, +637 ms later, raw `0F10055A002142000000000000001F000C000000000000001F000C00000000000000000000001F000C000000000000001F000C00000000000000000000001F000C000000000000001FF26A`. No ACK was sent to `055A`.

Negative/clean results: no approval retry after R1; no acknowledged-stage retries observed; parser resyncs remained 0; RX buffer drops remained 0.

Conclusion: accelerated batching is confirmed workable through `0546/count20`, and the local XTR follows the genuine Eco 5 sync path through `055A/count33`. Full Online/Link remains unproven. Recovery: one normal controller reboot.

# THERMIA EXPERIMENT LOG

## EXP262 — accelerated 04A6..0546 batch — PREPARED / NOT RUN

Hypothesis: after the proven local Online/Link prefix through `0492/count11`, ACK a bounded batch of eight exact FC16 pages: `04A6/13`, `04BA/22`, `04D8/27`, `04F6/14`, `050A/19`, `051E/10`, `0532/18`, `0546/20`; then capture the first different FC16/FC03 without responding. Genuine Eco 5 predicts `055A/count33`.

Safety: all pages are exact known controller-originated FC16 export requests. EXP262 sends only standard address/count acknowledgements. Every stage is first-exact, time-bounded and parser-clean; unexpected traffic stops fail-closed. No FC03/mailbox response and no ACK after `0546`. Known incomplete-session recovery remains one normal controller reboot.


## EXP261 — bounded 046A/047E/0492 ACK batch — COMPLETE / STRONG POSITIVE

**Hypothesis:** after the proven local prefix, ACK exact `046A/count18`, then exact `047E/count19`, then exact `0492/count11`, and capture the first different FC16/FC03 stage without answering it.

**Observed facts:**
- first approval at +1245 ms after BUS_RETURN;
- R1 accepted with no approval retry;
- the proven prefix through `0456/count12` reproduced cleanly;
- `046A/count18` appeared and was ACKed once;
- `047E/count19` followed +722 ms later and was ACKed once;
- `0492/count11` followed +1480 ms later and was ACKed once;
- the first different block was exact `04A6/count13`, +576 ms after the 0492 ACK;
- raw `04A6` request: `0F1004A6000D1A0000000000000000000000000000000000000000402000000000CA9A`;
- `04A6` was not ACKed;
- no stage retries, no approval retry after R1, no unexpected peer frame, no post-return parser/RX-drop delta; DE LOW.

**Strong conclusion:** local XTR follows the genuine Eco 5 ordered synchronization path through `0492/count11`, with `04A6/count13` next in this run. The bounded-batch strategy remains valid.

**Unknown:** full Online/Link establishment and mailbox behavior remain unproven.

**Recovery:** one normal Thermia-controller reboot after the summary.


## EXP261 — bounded `046A -> 047E -> 0492` continuation — PREPARED / NOT RUN

**Hypothesis:** the local XTR continues to follow the genuine Eco 5 Online/Link FC16 sequence after EXP260. Preserve the complete proven prefix and ACK exactly three new expected stages: `046A/count18`, `047E/count19`, and `0492/count11`. Then capture the first different FC16/FC03 without answering it.

**New ACKs:** `046A/18 -> 0F10046A00126006`; `047E/19 -> 0F10047E0013E1C2`; `0492/11 -> 0F100492000B203D`.

**Primary prediction:** `04A6/count13` is the genuine Eco 5 next-page observation, but because `04A6/13` is also known as a recurrent passive family it is recorded as a prediction rather than a strict required success value.

**Safety:** same cold-boot approval guard and proven prefix as EXP260; first-exact-stage-only, <=5 s between ACKs, no retries, parser/drop counters unchanged, no unexpected peer frames. After `0492` ACK, capture only. No FC03 response. Controller reboot after summary.


## EXP260 — bounded `042E -> 0442 -> 0456` ACK batch — COMPLETE / STRONG POSITIVE

**Hypothesis:** after the locally proven prefix through `042E/count15`, ACK exactly `042E/15`, `0442/13`, and `0456/12` in order, then stop and capture the next different frame. Genuine Eco 5 predicts `046A/count18`.

**Observed facts:**
- first approval request at +1284 ms after BUS_RETURN; R1 sent once;
- `03E8/14` arrived +126 ms after R1 and was ACKed once;
- `03FC/11` arrived +694 ms after the `03E8` ACK and was ACKed once;
- `0410/22` arrived +1492 ms after the `03FC` ACK and was ACKed once;
- `042E/15` arrived +695 ms after the `0410` ACK and was ACKed once;
- `0442/13` arrived +1502 ms after the `042E` ACK and was ACKed once;
- `0456/12` arrived +566 ms after the `0442` ACK and was ACKed once;
- predicted `046A/count18` arrived +1473 ms after the `0456` ACK; it was captured and not ACKed.
- summary: approval retries after R1=0; all stage retry counters=0; peer17=0; unexpected peer ACK=0; post-return resync/drop deltas=0; DE LOW.

**UI side effect:** user reports the DHW-side literal `0` appeared again. No EXP260 `COMM. ERR ONLINE/LINK` confirmation yet. Recovery should be performed immediately after the summary rather than waiting for an alarm.

**Strong conclusion:** the bounded batching strategy is validated locally through `046A/count18` and preserves the same ordered sequence as the genuine Eco 5 reference.

Last updated: 2026-09-27

## EXP260 — bounded `042E -> 0442 -> 0456` ACK batch — PREPARED / NOT RUN

**Hypothesis:** continue the already-proven local Online/Link prefix in one bounded batch. After the proven EXP259 prefix, ACK exact `042E/count15`, then exact `0442/count13`, then exact `0456/count12`. The genuine Eco 5 reference predicts `046A/count18` next.

**New active variable family:** three exact standard FC16 ACKs: `0F10042E000FE01A`, `0F100442000DA1C6`, `0F100456000C2002`. Each is one-shot and only allowed after the preceding exact stage.

**Safety/stop rule:** any deviation, retry, FC03, unexpected peer response, parser/RX-drop delta, or >5 s missing expected stage stops the experiment immediately. After the `0456` ACK, capture the first different FC16/FC03 only; no `046A` ACK and no mailbox response.

**Known recovery:** deliberately incomplete Online/Link sessions have repeatedly produced DHW-side `0` and `COMM. ERR ONLINE/LINK`; reboot controller once after the summary.

## EXP259 — ACK `0410/count22`, capture next stage — COMPLETE / STRONG POSITIVE

**Hypothesis:** after the proven prefix `R1 -> 03E8/14 ACK -> 03FC/11 ACK -> 0410/22`, one exact FC16 ACK to `0410/count22` should advance the XTR to the next ordered sync block. Genuine Eco 5 predicted `042E/count15`.

**Observed:**
- approval at +1283 ms after BUS_RETURN;
- R1 once;
- `03E8/14` +138 ms after R1, ACKed once;
- `03FC/11` +682 ms after `03E8` ACK, ACKed once;
- `0410/22` +1498 ms after `03FC` ACK, ACKed once;
- `042E/15` +696 ms after `0410` ACK;
- `042E/15` not ACKed;
- `approval_after_r1=0`, `same03e8_after_ack=0`, `same03fc_after_ack=0`, `same0410_after_ack=0`;
- `peer17=0`, `unexpected_peer_ack=0`, `self_echo_r1=0`, `self_echo_ack=0`;
- `resync_postreturn=0`, `drop_postreturn=0`, `DE=LOW`.

**Result:** strong positive. Local XTR matches the genuine Eco 5 ordered sync prefix through `042E/count15`.

**Negative/safety result:** full Online/Link session is still not established; no `042E` ACK, no later FC16 ACK, and no FC03/mailbox response was emitted.

---

## EXP259 — UI side effect follow-up

After the successful protocol result, the user confirmed the same visible side effects seen in earlier incomplete Online/Link sessions: DHW-side literal `0` and exact `COMM. ERR ONLINE/LINK`. This is a repeated positive observation, not a new protocol stage.

Interpretation: the association between partial Online/Link servicing and the communication alarm is now reproducible across multiple active runs. The specific causal mechanism remains a hypothesis until a sufficiently complete session is shown to avoid the alarm. Recovery remains one normal controller reboot.


## EXP259 — exact `0410/count22` ACK then next-stage capture — PREPARED / NOT RUN

**Hypothesis:** after the locally proven prefix `R1 -> 03E8/14 ACK -> 03FC/11 ACK -> 0410/22`, one exact standard FC16 ACK to `0410/count22` should advance the XTR controller to a different block. The genuine Eco 5 reference predicts `042E/count15`.

**Only new active variable:** one ACK frame `0F1004100016401C` for exact slave `0x0F` FC16 `start=0410`, `count=22`, `bytecount=44`, request length `53`. The ACK carries no register-value payload.

**Safety:** R1, `03E8` ACK and `03FC` ACK retain the existing guards. The new `0410` ACK is one-shot, latch-before-DE, allowed only on the first exact post-`03FC`-ACK `0410/22` within 5 s with clean parser/drop counters and no approval/03E8/03FC retry or unexpected peer. After that, capture-only: no `042E` ACK, no later FC16 ACK, no FC03/mailbox response. Reboot controller after summary.

**Expected positive discriminator:** first post-`0410`-ACK block is `042E/count15`. Any other different FC16/FC03 is still recorded as a protocol result.

---

## EXP258 — exact `03FC/count11` ACK then next-stage capture — COMPLETE / STRONG POSITIVE

**Hypothesis:** after the locally proven `R1 -> 03E8/count14 ACK -> 03FC/count11`, one exact standard ACK to `03FC/count11` should advance the XTR to a different block. Genuine Eco 5 predicts `0410/count22`.

**Observed facts:** first approval +1243 ms after BUS_RETURN; R1 exactly once; `03E8/14` +138 ms after R1 and ACKed once; `03FC/11` +691 ms after the 03E8 ACK and ACKed once; `0410/22` appeared +1501 ms after the 03FC ACK and was not ACKed. No approval retry, no 03E8 retry, no 03FC retry, no unexpected peer frame, no post-return parser/drop delta; DE LOW at summary. User reports DHW-side `0` and the same `COMM. ERR ONLINE/LINK` alarm again.

**Exact result chain:** `R1 -> 03E8/14 -> ACK -> 03FC/11 -> ACK -> 0410/22 -> STOP`.

**Strong conclusion:** the first three ordered post-approval FC16 sync stages on the local XTR match the genuine Eco 5 sequence.

**Unknowns:** full session completion, later FC16 ordering on XTR, and mailbox behavior remain unproven. The repeated alarm is consistent with an incomplete approved session but is not yet proven to be caused specifically by the missing downstream ACK/mailbox service.

**Recovery:** one normal controller reboot before any further active test.

This file is the canonical experiment record. The compact table below indexes the early experiment series; EXP100+ are documented in the detailed chronological sections that follow. Detailed YAML and raw logs remain the primary evidence.

## EXP258 — exact `03FC/count11` ACK then next-stage capture — PREPARED / NOT RUN

**Hypothesis:** after the already-proven local prefix `R1 -> 03E8/count14 ACK -> 03FC/count11`, one exact standard FC16 ACK to `03FC/count11` should advance the XTR controller to a different block. The genuine Eco 5 reference predicts `0410/count22`.

**Only new active variable:** one ACK frame `0F1003FC000B4094` for exact slave `0x0F` FC16 `start=03FC`, `count=11`, `bytecount=22`, request length `31`. The ACK carries no register-value payload.

**Safety:** R1 and the `03E8` ACK retain the EXP257 guards. The new `03FC` ACK is one-shot, latch-before-DE, permitted only on the first exact post-`03E8`-ACK `03FC/11` within 5 s with clean parser/drop counters and no approval retry, `03E8` retry, or unexpected peer. After that, capture-only: no `0410` ACK, no later FC16 ACK, no FC03/mailbox response. Reboot controller after summary.

**Expected positive discriminator:** first post-`03FC`-ACK block is `0410/count22`. Any other different FC16/FC03 is still recorded as a protocol result.


## Post-EXP257 external Eco 5 follow-up — raw-log verified

No new local experiment was run. New external interpretation was checked against the complete public Eco 5 raw capture.

Observed facts:
- first cold-start approval request at +1.199/+1.202/+1.210 s after bus return in the three Eco 5 power-ups;
- successful genuine gateway responses at +120.153 s and +119.808 s after bus return, after 29 challenges each;
- middle no-gateway run ended by power-off at ~174 s and therefore cannot test a ~267 s natural cutoff;
- steady-state pre-power-off segment contains no approval exchange; Eco 8 steady-state absence must therefore remain open pending a cold-start capture;
- only two answered Eco 5 challenges exist, so repeated-challenge response determinism and cross-power-cycle response stability are unresolved;
- genuine endpoint continues ACKing the FC16 export stream after approval; `04A6/13` and `085F/5` are recurrent passive families whose ACK timing varies and is not a demonstrated precondition;
- first post-approval `0708/count6` mailbox polls occur at +158.393 s and +186.828 s after bus return, while the FC16 transfer is still active;
- in the first successful power-up the first mailbox poll is unanswered and the following poll is answered;
- the raw repeated idle response is six words `0000 0000 0000 0000 0001 0000` (not `...0100...` under standard Modbus word order);
- later fifth-word values include `03DC`=988 -> 984 -> 976 -> 908 -> 896 -> 768 -> 512 -> 0.

Interpretation/hypothesis:
- `COMM. ERR ONLINE/LINK` being a timeout of an approved-but-incompletely-serviced session is increasingly plausible but remains unproven;
- the fifth-word countdown may represent pending synchronization work, but no semantic mapping is established.

Decision:
- do not broaden directly to full-chain ACK + mailbox emulation;
- next candidate is **EXP258 (not prepared)**: add exactly one `03FC/count11` ACK after the already-proven EXP257 prefix and capture the first subsequent frame; genuine Eco 5 predicts `0410/count22`.


## EXP257 — One-shot R1 + single `03E8/count14` ACK + next-stage capture — COMPLETE / STRONG POSITIVE

**Hypothesis:** after EXP256's one-shot R1 transition into `03E8/count14`, acknowledge exactly the first `03E8/count14` once and capture the first different downstream FC16/FC03 request without answering it. Full genuine Eco 5 capture predicted `03FC/count11`.

**Observed facts:**
- controller cold-restart gap detected and clean `BUS_RETURN`;
- boot-only `04BA/count22` appeared at +316 ms after BUS_RETURN;
- first approval request at **+1285 ms**, `W071C=1A154568F9061AACDC1BC564001E8FD0`;
- exact R1 transmitted once; DE returned LOW;
- first post-R1 FC16 was exact `03E8/count14`, **+130 ms after R1**;
- exact standard ACK `0F1003E8000EC093` transmitted once; ACK latch closed before DE;
- first different post-ACK request arrived **+691 ms after ACK** and was exact `03FC/count11`, bytecount 22, length 31;
- raw `03FC` request: `0F1003FC000B160028000A0037000000000000000200120028001E003C369E`;
- payload words: `0028 000A 0037 0000 0000 0000 0002 0012 0028 001E 003C`;
- no ACK was sent to `03FC`;
- summary: `r1=1 ack03e8=1 approvals=1 approval_after_r1=0 post_r1_fc16=1 same03e8_after_ack=0 peer17=0 unexpected_peer_ack=0 self_echo_r1=0 self_echo_ack=0 resync_postreturn=0 drop_postreturn=0 DE=LOW`.

**Strong conclusions:**
- EXP257 satisfies its positive criterion.
- The XTR reproduces the genuine Eco 5 post-approval prefix `R -> 03E8/14 -> ACK -> 03FC/11`.
- The `03E8` ACK is sufficient to advance the local XTR one synchronization block.
- This substantially strengthens the interpretation that R1 enters the genuine Online/Link synchronization state machine rather than an unrelated failure state.
- Full Online/Link establishment remains unproven because `03FC` and all later stages were intentionally not acknowledged.

**Comparison with external reference:** the genuine Eco 5 capture proves twice that `03FC/count11` follows the acknowledged `03E8/count14`, and that acknowledged `03FC/count11` is followed by `0410/count22`. EXP257 reproduces the first of those transitions locally.

**Unknowns:**
- whether one exact ACK to local `03FC/count11` yields `0410/count22`;
- whether the remainder of the XTR synchronization ordering matches the Eco 5 chain;
- when `0708/count6` mailbox traffic starts locally;
- UI side effect for this run, pending user report.

**Safety/recovery:** no further ACKs were sent. One normal controller reboot is required after the incomplete session if not already performed.

## EXP256 — One-shot R1 + full post-R1 FC16/FC03 differential census — COMPLETE / ACTIVE STRONG POSITIVE

**Hypothesis:** the already-tested R1 changes the local XTR native FC16 distribution; leading pre-run hypothesis was selective suppression of `085F/count5` while `04A6/count13` persisted.

**Observed facts:**
- clean >=6 s controller bus gap and BUS_RETURN;
- first exact `071C/0730` approval request at **+1245 ms**; local `W071C=1A144532F9060CACDC1BC590001E8F64`, local schema check `RTC=OK`;
- exactly one R1 frame transmitted; DE returned LOW and one-shot latch stayed closed;
- approval requests **1**, retries after TX **0**;
- FC16 requests **390**, FC16 ACKs **0**;
- FC03 `0708/count6` **0**, other FC03 **0**;
- peer FC17 response **0**, self-echo **0**;
- complete FC16 census: `04BA/count22` = **1**, `03E8/count14` = **389**, `04A6/count13` = **0**, `085F/count5` = **0**;
- first `03E8/count14` at **+1369 ms after BUS_RETURN / +124 ms after R1**; last at **+419896 ms**; median `03E8` retry interval ~**1308 ms**;
- final state `A80E=0028 A80F=000A AFDC=0010`;
- post-return `resync_delta=0`, `drop_delta=0`;
- user reports the DHW/tank-side literal `0` reappeared; VERSION screen did not change; after summary the controller again raised **`COMM. ERR ONLINE/LINK`**, exactly matching EXP252.

**Strong conclusions:**
- R1 again suppresses all later approval retries.
- The pre-run H1 is falsified: R1 does **not** leave the passive `04A6/count13` stream intact while merely removing `085F/count5`. Both passive runtime families disappear.
- R1 instead advances the controller into the first known `0x0F` settings synchronization block, `03E8/count14`.
- Because EXP256 intentionally sent no FC16 ACK, the controller remained stalled retransmitting `03E8/count14` for the rest of the seven-minute observation.
- The prior EXP252 total `fc16req=386` is now best explained as likely the same unclassified `03E8` retransmission state, rather than the previously suspected passive-family remainder.

**Hypothesis / interpretation:** R1 is accepted at least far enough to cross the approval boundary and enter controller->Online/Link synchronization. This is not yet proof of a fully established Online/Link session because the expected endpoint transfer ACKs and any later FC03/mailbox phase were deliberately absent.

**Unknowns:**
- whether ACKing the exact first `03E8/count14` after R1 yields the same `0410/count22` next stage seen in earlier acknowledged-transfer experiments, or a different post-approval sequence;
- how far the synchronization chain proceeds before an additional service/mailbox response is required;
- exact semantics of the reproduced DHW-side `0`.

**Safety/recovery:** one normal controller reboot is required after the summary, matching the run plan and the known recoverable EXP252 side effect. No second active approval/sync test until normal UI recovery is confirmed.

| Experiment | Purpose | Result |
|---|---|---|
| EXP10-18 | Identify 0x06 response field responsible for controller ACK | word2/AFCA=03E8 in correct phase is decisive |
| EXP21-28 | Test trailing words/selectors/counts as setting-write encoding | Negative |
| EXP29 | Passive correlator | Diagnostic only |
| EXP30-31,33 | Outdoor-related probes | No semantic write discovered |
| EXP35-42 | Passive mapping | Useful telemetry; no write path |
| EXP43+ | Active 0x02 probes | No final semantic write path |
| EXP48-49 | Presence/multi-poll sequencing | Fast-cadence/state behaviour refined |
| EXP50 | Passive DCM audit | Recurring structure mapped |
| EXP51 | Single presence-like response | Cadence/state only |
| EXP52 | 00FF,1,03E8,1 envelope | ACK; no setting write |
| EXP53 | word2=440C | No ACK |
| EXP54 | word2=03F4 | No ACK |
| EXP55 | word2=04A6 | No ACK |
| EXP56B/C | 03E8 with word3 variants | ACK independent of simple word3 value |
| EXP57 | Bare 03E8 | ACK works |
| EXP58 | Bare 03E8 at wrong/normal-long phase | Fast cadence; no 0861 ACK |
| EXP59 | Zero stage then SHORT 03E8 | ACK; 00FF unnecessary |
| EXP60 | Same 03E8 on LONG vs SHORT | SHORT phase matters |
| EXP61 | Later valid SHORT 03E8 | ACK repeats |
| EXP62 | Selector 03E9 after established session | No ACK |
| EXP63-65 | Structured register/value layouts | Transport ACK only; no setting write |
| EXP66 | HE-like GET 440C | Handshake only; no semantic response |
| EXP67 | Post-close 03E8 on first FAST-LONG | No second ACK |
| EXP68-69B | Raw 12-word settings block variants | No setting change |
| EXP70 | Repeated zero responses | Fast cadence only |
| EXP71/71B | Apparent promotion / zero replies | Promotion later identified as natural controller behaviour |
| EXP72 | Natural AFDC/A80E state + bare 03E8 | Transport behaviour confirmed |
| EXP73/73B | Passive/manual curve correlation | Curve changes do not announce through AFDC/A80E |
| EXP74-75 | Persistent candidate register image | No write; ACK follows REQ level |
| EXP76B | Canonical four-phase handshake | PROVEN |
| EXP77-83 | HE payload/envelope/layout variants | No semantic response/write |
| EXP84 | Passive room-setpoint correlation | AFDC..AFE0 unaffected |
| EXP85 | Passive DCM source correlator | No source edge during capture |
| EXP86 | 30-minute passive first-edge capture | No A80E/A802/AFDC edge |
| EXP87 | Zero presence | Invalid/short guard stop; no semantic edge beforehand |
| EXP88 | Fixed all-zero presence 180 s | Negative |
| EXP89 | Intended persistent 00FF | Invalid due response-buffer bug |
| EXP90 | Correct persistent 00FF 90 s | Negative; 84 responses |
| EXP91 | Historical 00FF,1,REQ-low,1 envelope 90 s | Negative; 84 responses; no A80E/AFDC/settings/errors |
| **EXP92** | Completed four-phase 03E8 handshake, then historical REQ-low envelope 90 s | **VALID NEGATIVE. ACK high after 401 ms, ACK low after 1031 ms; 84 observation responses; A80E/AFDC stayed 0; no setting/error changes** |
| EXP93 | Passive A80F=50 discriminator | Armed in two captures but A80F=50 never occurred; observation window never started; NOT a negative result |
| **EXP94** | Passive cold-boot + initial-sync timeline | **COMPLETED.** Boot sequence: A80F/A810 5→10, A80E 0→8→0x28, AFDC 0→0x10; then stable for 600 s; 0861 unchanged; no settings changes |
| **EXP95** | Cold-boot zero-presence from first 0x06 poll | **VALID NEGATIVE.** 112/112 responses; cadence accelerated to 638..1503 ms, but `A80E=0x28`, `A80F/A810=10`, `AFDC=0x10`, `0861=0`; no settings changes |
| **EXP96** | Cold-boot historical envelope + canonical four-phase REQ handshake | **VALID NEGATIVE.** Handshake completed (`0861` high after 367 ms, low 1196 ms after deassert); no controller/session/settings progress |
| **EXP97** | Passive natural A80E/AFDC edge correlator | **COMPLETED.** Natural `A80E 28→20→0`, then `AFDC 10→0`; no ESP TX; 0861/outdoor/CMD1E/RSP02 unchanged at all three edges |
| **EXP98** | AFC8 single-word A/B/A influence | **COMPLETED NEGATIVE.** AFC8=00FF alone had no detectable effect; 81 polls/81 TX, no controller/0861/settings/CMD1E/outdoor changes |
| **EXP99** | Historical-field matrix, REQ low | **COMPLETED NEGATIVE.** Ten phases completed; no controller/0861/settings/CMD1E/outdoor effect; parser/drop deltas zero |

## EXP92 detailed record

Hypothesis: a completed four-phase transaction initializes hidden state needed for the old A80E/AFDC cycle.

Observed:

- baseline stable
- historical envelope preloaded
- REQ asserted on SHORT
- 0861 0->16 after 401 ms
- REQ deasserted while payload held stable
- 0861 16->0 after 1031 ms
- 90 s observation completed
- 84 observation replies
- A80E changes: 0
- AFDC changes: 0
- settings changes: 0
- parser resync delta: 0
- RX drop delta: 0

Conclusion: a single completed transport transaction is not sufficient to start the historical online-state cycle.

## External evidence before EXP93

Commit `piotr-romanowski/thermia-bus-sniffer@b4c27157402c49624917d523e016b249cdfc4e11` independently confirmed transmit-side room-setpoint control through slave 0x0A response register B3B1/46001 on iTec Eco. This matches our passive mapping and changes the highest-value next experiment.

## EXP93 — Passive A80F=50 discriminator

**Hypothesis:** the historical A80E/AFDC 0<->0x20 cycle is gated by controller state and appears while A80F=50.

**Observed:** correctly armed in two captures, but A80F remained 10 and no EXP93 trigger/summary occurred. The 180 s observation phase never began.

**Conclusion:** untriggered/inconclusive, not negative. Superseded as immediate priority by EXP94.

## EXP94 — Passive cold-boot + initial-sync timeline

**Hypothesis:** a real controller cold boot exposes a reproducible 0x06 accessory/integration startup or sync sequence that precedes semantic DCM03 operation.

**Observed facts:**

- bus silence confirmed after 5049 ms; first resumed valid frame after 11540 ms silence started capture;
- +717 ms: `A80C..A812=0040,0000,0000,0005,0005,FFFF,0000`;
- +1758 ms: `A80E 0->8`;
- +2846 ms: `A80E 8->40 (0x28)`;
- +1038 ms first 0x06 poll: `AFDC..AFE0=0000,0000,0000,0000,0019`;
- +5575 ms second 0x06 poll: `AFDC..AFE0=0010,0000,0000,0000,0014`;
- `A80F/A810` returned from 5 to 10 at about +11.3 s;
- no later DCM/integration transition occurred during the full 600 s window.

**Summary:** `frames=5185`, `06polls=140`, `06_min_ms=4086`, `06_max_ms=4537`, `ctrl_changes=3`, `rsp02_changes=1`, `0861_changes=0`, `settings_pushes=0`, `settings_changes=0`, `outdoor_state_changes=0`, `resync_delta=1`, `drop_delta=0`.

**Strong conclusion:** unanswered cold boot settles quickly into stable `A80E=0x28 / AFDC=0x10 / A80F=A810=10`; the historical A80E/AFDC 0x20 cycle is not ordinary cold-boot initialization.

**Unknowns:** exact meanings of A80E bits 0x08/0x20 and AFDC 0x10; whether a real DCM response advances this state.

## EXP95 — Cold-boot zero-presence from first 0x06 poll

**Hypothesis:** syntactic DCM presence from the first cold-boot `0x06` poll is sufficient to move the controller away from EXP94's stable waiting state.

**Observed:**

- complete `120000 ms` run;
- `frames=1133`; `06polls=112`; `tx=112`; `refused=0`;
- `06_min_ms=638`; `06_max_ms=1503`;
- boot state still followed `A80E 0->8->0x28`, `A80F/A810 5->10`, `AFDC 0->0x10`;
- `0861_final=0000`, `0861_changes=0`;
- `settings_pushes=0`, `settings_changes=0`;
- `outdoor_state_changes=0`;
- `resync_delta=1`, `drop_delta=0`.

**Strong conclusion:** zero-presence proves transport/presence and triggers fast cadence, but does not establish/advance the DCM application session. `AFDC=0x10` therefore cannot simply mean “accessory absent.”

**Negative result recorded:** syntactic presence alone does not advance the cold-boot integration state.

## EXP96 — Cold-boot historical envelope + canonical REQ/ACK handshake

**Hypothesis:** the historical envelope gains semantic meaning only in the true cold-boot EXP95 context.

**Observed:**

- canonical transaction completed;
- `0861 0->16` after 367 ms;
- REQ deasserted with payload stable;
- `0861 16->0` after 1196 ms;
- `handshake=1`; `06polls=112`; `tx=112`; `refused=0`;
- `ctrl_changes=3`; `rsp02_changes=0`;
- `settings_pushes=0`; `settings_changes=0`;
- no higher-layer application/session transition.

**Conclusion:** valid negative. Cold-boot context does not rescue the historical envelope. The missing layer remains the DCM03 semantic/init serializer.

**Additional passive observation before ARM:** `A80E 0x28->0x20->0x00`, followed by `AFDC 0x10->0x00`, occurred naturally with no EXP96 TX. This is recorded as evidence that these fields participate in broader controller-state propagation.

## EXP97 — Passive natural A80E/AFDC edge correlator

**Hypothesis:** natural A80E/AFDC transitions correlate with another controller/outdoor-unit state rather than DCM-session establishment.

**Design:** 600 s passive observation, no TX, no cold boot requirement. Every A80E or AFDC edge produces a compact multi-layer snapshot of `A80C..A812`, `A7F8..A806`, `AFDC..AFE0`, `0861`, `0x1E 0000..0008`, and outdoor-state.


## EXP97 — Passive natural A80E/AFDC edge correlator — result

**Hypothesis:** natural A80E/AFDC transitions correlate with another known controller/outdoor state rather than DCM-session establishment.

**Observed:**
- baseline `A80E=0028`, `AFDC=0010`, `0861=0000`, outdoor=`0010`;
- +71.278 s: `A80E 0028 -> 0020`;
- +72.340 s: `A80E 0020 -> 0000`;
- +74.995 s: `AFDC 0010 -> 0000`;
- all three event snapshots had identical `0861`, outdoor, `CMD1E`, and paired `RSP02`;
- experiment was passive: no 0x06 response, no REQ, no TX.

**Conclusion:** A80E/AFDC are not reliable DCM-session-success indicators. The specific monitored controller/outdoor fields did not explain the natural transition.

**Negative result recorded:** no direct edge correlation with `0861`, outdoor state, CMD1E, or paired RSP02.

## EXP98 — AFC8 single-word A/B/A influence test

**Hypothesis:** isolated `AFC8=00FF` has a measurable application-layer effect when transport presence is maintained.

**Design:** 90 s A/B/A: zero-presence 20 s; `AFC8=00FF` only for 30 s; zero-presence recovery 40 s. `AFCA=0000` throughout. No semantic write target.


### Result — EXP98
A/B/A completed cleanly. AFC8=00FF alone caused no detectable application-layer response. 81 0x06 polls and 81 TX were completed without refusals; no controller, RSP02, 0x06 write-bank, 0861, settings, CMD1E or outdoor-state changes were observed. Negative result recorded.

## EXP99 — Historical-field matrix, REQ low
Prepared as a faster structured follow-up: ten 8 s phases test AFC9=0001, AFCB=0001, pairwise combinations with AFC8=00FF, and the full historical non-REQ combination. AFCA remains 0000 throughout.


## EXP99 — Historical-field matrix, REQ low — result

**Hypothesis:** `AFC8=00FF`, `AFC9=0001`, `AFCB=0001` may have standalone or combinatorial application-layer meaning without REQ.

**Observed:** 80 s complete; `06polls=75`, `tx=75`, `refused=0`; each of the ten phases received 7–8 responses. `06_min_ms=707`, `06_max_ms=1450`. `ctrl_changes=0`, `rsp02_changes=0`, `06_changes=0`, `0861_changes=0`, `settings_pushes=0`, `settings_changes=0`, `cmd1e_changes=0`, `outdoor_changes=0`, `resync_delta=0`, `drop_delta=0`.

**Conclusion:** valid negative. None of the historically observed non-REQ fields, alone or in the tested combinations, is a standalone semantic trigger with `AFCA=0000`.

## EXP100 — Multi-transaction historical-field matrix

**Hypothesis:** those fields may only matter inside the proven canonical REQ/ACK transaction.

**Design:** six transactions in one run: AFC9 only; AFCB only; AFC8+AFC9; AFC8+AFCB; AFC9+AFCB; AFC8+AFC9+AFCB. Each uses preload -> `AFCA=03E8` -> wait `0861=16` -> `AFCA=0` with payload stable -> wait `0861=0` -> 3 s zero-presence observation. Hard stop 75 s. No semantic setting target.

## EXP100 — Multi-transaction historical-field matrix — result

**Hypothesis:** historically observed `AFC8/AFC9/AFCB` fields may only matter inside a valid canonical `AFCA=03E8` transaction.

**Observed:** six of six transactions completed. Each followed preload -> REQ high -> `0861=16` -> REQ low with stable payload -> `0861=0` -> observation. Final summary: `duration_ms=58046`, `complete=1`, `hard_stop=0`, `06polls=51`, `tx=51`, `refused=0`, `ack_hi=6`, `ack_lo=6`, `t1=1..t6=1`, `0861_changes=12`, `settings_pushes=0`, `settings_changes=0`, `ctrl_changes=0`, `rsp02_changes=0`, `06_changes=0`, `cmd1e_changes=0`, `outdoor_changes=0`, `resync_delta=0`, `drop_delta=0`.

**Result:** valid negative. Carrying the tested historical non-REQ field combinations inside a proven transport transaction still produces no semantic effect.


## EXP100 — Multi-transaction historical-field matrix — COMPLETED

Hypothesis: AFC8/AFC9/AFCB may only have application-layer meaning inside a valid AFCA=03E8 transaction.

Result: valid negative. All six transactions completed with canonical four-phase transport (`ack_hi=6`, `ack_lo=6`, `0861_changes=12`). No controller, 0x02 response, settings, 0x1E command, outdoor-state, or 0x06 controller-write change occurred. `resync_delta=0`, `drop_delta=0`.

Conclusion: historical AFC8/AFC9/AFCB values, separately and in all tested combinations, are semantically insufficient even inside valid transport transactions.

## EXP101 — AFCC..AFD3 one-word influence matrix — PREPARED

Hypothesis: one or more tail response words AFCC..AFD3 may participate in the missing DCM03 application layer.

Plan: eight transactions, one word at a time: AFCC=1, AFCD=1, AFCE=1, AFCF=1, AFD0=1, AFD1=1, AFD2=1, AFD3=1. Canonical AFCA=03E8 handshake; 3 s zero-recovery between transactions; hard stop 95 s. No known setting target.

## EXP101 — AFCC..AFD3 one-word influence matrix — COMPLETED NEGATIVE

Hypothesis: one of the still-unmapped tail words `AFCC..AFD3` may be an application-layer selector when transported with the proven canonical REQ/ACK handshake.

Observed:
- 8/8 planned transactions completed;
- `ack_hi=8`, `ack_lo=8`, `0861_changes=16`;
- T1..T8 each completed once;
- per transaction exactly one of AFCC..AFD3 was `0x0001`;
- `ctrl_changes=0`, `rsp02_changes=0`, `06_changes=0`;
- `settings_pushes=0`, `settings_changes=0`;
- `cmd1e_changes=0`, `outdoor_changes=0`;
- `resync_delta=0`, `drop_delta=0`;
- no hard stop or TX refusal.

Result: negative. No tested tail word produced a detectable application-layer effect by itself.

## Historical archive re-analysis before EXP102

Reviewed 98 archived Thermia logs. Recovered earlier coverage showed that EXP16/18 had already varied AFC9/AFC8 broadly, EXP14/15 had varied AFCB, EXP24/25 had probed words 4..11 with 0001 during the ACK window, and EXP26/28 had tested structured word4/word5 payloads. All were negative for a semantic setting change despite valid transport behavior.

This makes further isolated-word tests redundant. A new structural hypothesis is therefore promoted: one of the historical `0001` words may be a payload length/count, so previous extra tail data may have been outside the declared message length.

## EXP102 — count / structure interaction matrix — PREPARED

Hypothesis: AFC9 and/or AFCB acts as a declared payload length/count.

Plan: six canonical transactions: historical count-1 control, AFC9 lengths 2 and 3 with matching tail words, AFCB lengths 2 and 3 with matching tail words, and a both-length2 case. Small values only; no known setting IDs; 3 s zero recovery; hard stop 80 s.

## EXP102 — count / structure interaction matrix — COMPLETED NEGATIVE

Hypothesis: AFC9 and/or AFCB may be a declared payload length/count.

Observed:
- six of six transactions completed;
- `ack_hi=6`, `ack_lo=6`, `0861_changes=12`;
- T1..T6 each completed once;
- coherent AFC9 length-2/3, AFCB length-2/3, and both-length2 structures all received normal transport ACKs;
- `ctrl_changes=0`, `rsp02_changes=0`, `06_changes=0`;
- `settings_pushes=0`, `settings_changes=0`;
- `cmd1e_changes=0`, `outdoor_changes=0`;
- `resync_delta=0`, `drop_delta=0`.

Result: valid negative. Matching larger count-like values with additional tail words does not unlock semantics. The simple AFC9/AFCB length-count hypothesis is rejected.


## Post-EXP102 archive audit — 2026-09-23

No new experiment was armed. Historical archive review covered 98 logs and recovered broader prior test coverage than the condensed state showed. At least 45 unique logged experimental 0x06 response payload forms were indexed. Earlier EXP13–18, 24–28 and later EXP52–102 collectively make further isolated-word/value probing low-value. No genuine DCM03 accessory response was identified in the archive.

Decision: **EXP103 deferred pending new evidence**. Negative results are preserved; next active test should be derived from genuine DCM traffic, firmware/PCB evidence, or another independently sourced protocol trace rather than another guessed response.


## EXP103 — repeated identical canonical transaction chain — PREPARED

Hypothesis: DCM application/session state may accumulate only after multiple consecutive successfully acknowledged transactions with an unchanged historical envelope.

Plan: three identical `00FF,0001,REQ,0001,0...` canonical transactions. T2 and T3 are chained immediately after ACK-low with no 3 s zero-recovery between them. After T3, reply all zeros and observe 10 s. No new payload values or known setting IDs. Hard stop 60 s.


## EXP103 — repeated identical canonical transaction chain — COMPLETED NEGATIVE

Hypothesis: DCM application/session state may accumulate only after multiple consecutive successfully acknowledged transactions with an unchanged historical envelope.

Observed:
- T1/T2/T3 all completed with canonical `0861 0->16->0` handshakes;
- no 3 s zero-recovery was inserted between transactions;
- `ack_hi=3`, `ack_lo=3`, `t1=t2=t3=1`;
- `settings_changes=0`, `ctrl_changes=0`, `06_changes=0`;
- `cmd1e_changes=0`, `outdoor_changes=0`;
- `resync_delta=0`, `drop_delta=0`;
- final `complete=1`, `hard_stop=0`.

Result: valid negative. Three back-to-back identical historical-envelope transactions do not establish semantic DCM state.

Post-run note: after the experiment summary, a natural `A80E 0->32` followed by `AFDC 0->32` occurred, and the pattern repeated later. These transitions are not attributed to EXP103 because they occurred after the experiment ended.

Diagnostics note: this run used the pre-fix health-bookkeeping build, so `Bus Last Valid Frame Age` stayed `nan` and `Valid Frames Since Boot` stayed `0` despite continuous bus traffic. This does not invalidate the experiment result.


## EXP104 — AFC8 sequence-toggle canonical transaction chain — PREPARED

Hypothesis: AFC8 may act as transaction identity/sequence metadata only when its value changes across consecutive canonical transactions.

Plan: T1 AFC8=00FF, T2 AFC8=00FE, T3 AFC8=00FF; AFC9=1, AFCB=1, tails zero, canonical AFCA handshake for each; no zero-recovery between T1/T2/T3; 10 s zero final observation; 60 s hard stop. No known setting IDs. Corrected bus-health diagnostics from fixed EXP103 retained.


## EXP104 — AFC8 sequence-toggle canonical transaction chain — COMPLETED NEGATIVE
- Hypothesis: AFC8 may act as transaction identity/sequence metadata when changed between consecutive canonical transactions.
- Sequence: T1 `00FF`, T2 `00FE`, T3 `00FF`; AFC9/AFCB fixed at `0001`; AFCA canonical REQ handshake; no recovery gap between transactions.
- Result: all 3 transactions ACKed fully (`ack_hi=3`, `ack_lo=3`, `t1=t2=t3=1`). ACK-high: 447/441/447 ms after REQ assert. ACK-low: 1076 ms after REQ deassert for all 3.
- No semantic effect: `settings_pushes=0`, `settings_changes=0`, `cmd1e_changes=0`, `outdoor_changes=0`.
- `ctrl_changes=1` and `06_changes=1` were the natural A80E/AFDC `0->32` cycle occurring after transaction completion; the cycle later reset and repeated, so not attributed to EXP104.
- Bus-health bookkeeping fix validated: frame count increases and last-valid-frame age is live.
- Conclusion: simple AFC8 sequence-toggle hypothesis negative.


## EXP105 — State-gated canonical transaction — PREPARED

**Hypothesis:** a semantic/application transaction may only be accepted during the natural controller lifecycle window where `A80E=0x0020` and `AFDC=0x0020`.

**Change from EXP104:** no payload sequencing experiment. EXP105 remains passive until the natural gate and then sends one already-known historical canonical transaction. This isolates controller-state timing as the variable.

**Safety:** no known setting target, no new unknown payload values, no TX before the gate, fail-closed UART guard, 180 s hard stop.


## EXP105 — State-gated canonical transaction — COMPLETED NEGATIVE

Hypothesis: the known historical `00FF,0001,REQ,0001,0...` transaction may only gain semantic meaning during the natural `A80E=0x0020` / `AFDC=0x0020` lifecycle window.

Observed:
- gate triggered naturally at ~32.9 s after arm;
- preload and REQ-high both occurred while A80E and AFDC were still `0x0020`;
- ACK-high after 373 ms; ACK-low after 1151 ms;
- summary: `complete=1 hard_stop=0 gate_seen=1 gate_aborts=0 txn_complete=1 ack_hi=1 ack_lo=1 settings_pushes=0 settings_changes=0 cmd1e_changes=0 outdoor_changes=0 resync_delta=0 drop_delta=0`.

Result: valid negative. The natural `0x20/0x20` controller window does not make the known historical envelope semantically active.


## EXP106 — Passive integration-sync window correlator — PREPARED

Hypothesis: `A80F=0x0032` may identify the broader integration/synchronisation phase that older captures associated with A80E/AFDC cycling. EXP93 never triggered, so this remains untested.

Plan: strictly passive. Arm after >=15 s uptime, observe up to 30 min, trigger on A80F=50, then capture 180 s post-trigger context across A80C..A812, A7F8..A806, AFDC..AFE0/cadence, 0861, settings, 0x1E command image and outdoor state. Hard stop 1800 s if no trigger. TX=0.


## Cross-model evidence update — Piotr Romanowski / thermia-bus-sniffer — 2026-09-23

This is not a new Marten experiment; it is independent corroborating evidence from an iTec Eco 8 / DHP-AQ unit.

Observed by Piotr:
- corrected prior claim: `0x1E 0x001E..0x0033` is not frozen; it changes rarely and out of step with the live block;
- `B3B1` works as a real room-setpoint request channel in the slave response slot, encoding x1 °C;
- the controller stores the accepted setpoint and pushes it back through `B3C5`;
- `B3B1=0` means no request, not revert/clear;
- `AFDD=AFDE=AFDF=0` throughout a long passive capture;
- `AFE0` tracks displayed outdoor temperature x1;
- `AFDC` continuously pulses `0 <-> 32` with ~64 s period (~17 s high / ~47 s low);
- `A80E` follows the same pulse timing to the second;
- passive `0861` remained constantly `0` over multiple days;
- one isolated `AFDC=16` coincided with outdoor-unit-active status rise, insufficient for a semantic interpretation;
- A80E bit 3 appeared independently for ~10 minutes.

Strong conclusion:
- the recurring A80E/AFDC `0x20` state is ordinary controller lifecycle/heartbeat behaviour, not evidence of DCM login, approval, or semantic session.
- `0861` remains the cleaner transaction-level discriminator for active `AFCA=03E8` tests.

Candidate EXP107 direction after EXP106 closes:
- maintain one already-tested, harmless 0x06 accessory baseline image continuously for a stabilization interval;
- pulse only `AFCA 0 -> 03E8 -> 0` with all other words unchanged;
- observe `0861`, settings, controller state, CMD1E and outdoor state;
- do not gate the experiment on AFDC/A80E values.


## EXP106 — CLOSED (partial but sufficient negative)

The planned final post-trigger summary was not captured, so EXP106 remains technically incomplete as a full-duration run. However, the discriminating hypothesis is sufficiently rejected:

- A80E/AFDC cycling occurred at A80F 75, 80 and 50;
- A80F=50 therefore is not required for that lifecycle;
- A80F 80->50 occurred close to ordinary outdoor-unit transition to state 16/idle;
- no passive 0861 activity or settings mutation was seen;
- cross-model Eco 8 evidence shows AFDC/A80E 0<->0x20 can be a continuous heartbeat.

Decision:
Close EXP106 and do not build further A80F/AFDC-gated semantic tests.

## EXP107 — PREPARED — Persistent accessory image then isolated AFCA pulse

Hypothesis:
A known 0x06 transaction may behave differently if the accessory-side image has been continuously stable for >=60 s before AFCA is asserted.

Controlled change:
Only the preload/stabilization duration changes. The historical image and AFCA 4-phase mechanism are already-tested values.

Sequence:
1. qualify clean idle baseline;
2. transmit historical REQ-low image continuously for >=60 s;
3. change only AFCA 0000->03E8;
4. wait for 0861=16;
5. change only AFCA 03E8->0000;
6. wait for 0861=0;
7. continue the identical REQ-low image for 90 s;
8. summary.

Safety:
No new semantic write target; exact 0x06 slot only; existing-responder inhibit; compressor/outdoor idle guards; parser/drop guards; hard handshake timeouts.


## EXP107 — COMPLETE — Persistent image + isolated AFCA pulse

Result: negative for semantic initialization, positive for transport reproduction.

Timeline:
- cached settings baseline accepted
- TX_PRELOAD_REQ_LOW_01 started historical envelope
- image held continuously for 61.023 s
- TX_REQ_ASSERT: only AFCA changed to 03E8
- 0861: 0 -> 16 after 328 ms
- TX_REQ_DEASSERT: only AFCA returned to 0
- 0861: 16 -> 0 after 1122 ms
- identical REQ-low image continued for 90 s

Summary:
`handshake_complete=1 total_responses=144 observe_responses=84 A80E_peak=0 A80E_changes=0 AFDC_peak=0 AFDC_changes=0 AFDC_nonzero=0 status_peak=16 settings_changed=0 resync_delta=0 drop_delta=0`

Observed negative:
No A80E/AFDC activation, no semantic settings change, no new controller-side state beyond the known 0861 ACK.

Conclusion:
Persistent presence duration is not the missing DCM semantic bootstrap. Do not spend further experiments on longer dwell times or nearby timing variants unless new external evidence justifies them.


## Firmware analysis after EXP107

No new bus experiment was run.

New binary evidence:
- 2.1.35: generic DHPParameterCache exists, but no HPNode/SystemIntegration application layer in RegulationEngine.
- 2.7.42: HPNode/SystemIntegration application layer present.
- IntegrationMode is confirmed ParameterID 0x4414.
- SystemIntegrationInitRequest and InitSyncDone are internal booleans, not wire parameters.
- IntegrationMode update triggers full three-group resynchronization.
- system integration flips selected heat-pump parameters from GET-on-sync to SET-on-sync.

Decision:
Do not design EXP108 around a guessed "init flag". First reconstruct the three sync groups and look for a local mailbox representation of grouped synchronization.


## 2026-09-24 — EXP129–134 current run

### EXP130 — AFD1 version scaling — COMPLETE / POSITIVE MAPPING
Hypothesis: `AFD1` is the visible EXP/expansion-board version field.

Observed: with a valid 0x06 responder, VERSION display tracked the tested AFD1 values as tenths: `0→0.0`, `1→0.1`, `2→0.2`, `10→1.0`, `16→1.6`.

Conclusion: `AFD1` is a proven visible EXP version field for this XTR UI path. This is metadata/UI semantics only; it does not prove Online/DCM identity or write-session readiness.

### EXP131 — AFD0 type with valid AFD1 version — COMPLETE / NEGATIVE
Hypothesis: `AFD0` may select accessory type/identity when `AFD1` contains a valid version.

Observed: baseline `AFD0=0, AFD1=16` displayed EXP 1.6. `AFD0=1,2,10,16` produced no visible change; restore phases were also unchanged. Summary reported `tx=208`, `refused=0`, `marksSame=10`, `marksChanged=1`, `marksGone=0`, `resyncDelta=0`, `dropDelta=0`.

Conclusion: tested AFD0 values are not a simple visible type/identity selector.

### EXP132 — AFC8/AFC9/AFCB validity/header matrix with AFD1=16 — COMPLETE / NEGATIVE
Hypothesis: `AFC8/AFC9/AFCB` may form a metadata validity/header pattern whose effect only appears with a nonzero valid AFD1 version.

Observed: EXP 1.6 remained unchanged when AFC8, AFC9, AFCB were zeroed individually, pairwise and all together, with AFD1 fixed at 16. Final summary: `tx=353`, `refused=0`, `marksSame=16`, `marksChanged=1`, `marksGone=0`, `resyncDelta=0`, `dropDelta=0`.

Conclusion: AFC8/AFC9/AFCB are not required for the VERSION page to display EXP 1.6.

### Architecture review after EXP132
Uploaded Discussion #143 and supporting files from another Thermia platform were compared against our own captures. They are treated as external hints, not truth for XTR. The strongest cross-check is that our XTR itself already carries `0x0F FC10` application/settings blocks starting at `0x03E8`, while the external work independently identifies similar 0x0F block traffic. This shifts the next investigation from guessed 0x06 application payloads toward passive XTR-specific 0x0F block mapping.

### EXP133 — Passive 0x0F block-structure census — RUNNING / PARTIAL
Hypothesis: the XTR uses stable native 0x0F application/settings blocks beyond the already-known 0x03E8 block, possibly sharing structural patterns with the external ATEC/DHP-AQ material.

Design: 600 s passive-only census; no RS485 TX, no 0x06 response, no direct 0x0F write. Log every unique 0x0F FC03/FC10/FC17 shape and first payload. External block starts are flagged only as hints.

Partial observed facts:
- experiment started with `PASSIVE_ONLY DE_LOW no_tx`;
- first native FC10 shape: start `0x04A6`, count 13; payload has only word `0x04B0=0x4020` nonzero in the first observed frame;
- second native FC10 shape: start `0x085F`, count 5; first payload all zero;
- `0x0861` is inside that native five-word block;
- parser resyncs and RX drops remained zero in the supplied partial log.

Status: **OPEN**. Do not infer the final 0x0F block map until the automatic EXP133 SUMMARY and full 600 s log are captured.

### EXP134 — Passive DHW START correlation — PREPARED, NOT RUN
Hypothesis: external candidate decimal 1053 / hex `0x041D` may correspond to `SERVICE → WARMWATER → START` on this XTR.

Planned controlled variable: manually change only DHW START by -1 °C and restore it while ESP passively logs 0x0F changes. `0x041D` is a candidate marker only. No ESP write.

Safety: run only after EXP133 review; use a moment when DHW production is inactive and the actual DHW temperature is sufficiently above START so the -1 °C step cannot create a new heat demand.


### EXP134 — passive DHW START correlation — PROCEDURAL / INCIDENTAL
Only `03E8 34 -> 35` changed, tracking Heating Curve. No valid DHW mapping resulted.

### EXP135 — passive DHW START A/B/A — COMPLETE / NEGATIVE FOR 03F1
Manual `SERVICE -> WARMWATER -> START` ±1 °C produced no change in recurrent `03E8..03F5`; `03F1` remained 40. `041D` was not covered by an observed block. Downgrade `03F1 = Hot Water Start` to OPEN / locally unsupported.

### EXP136 — passive DHW COMFORT/ECO mode A/B/A — COMPLETE / NEGATIVE
Confirmed physical COMFORT<->ECO change and restore. Recurrent `03E8..03F5` remained byte-for-byte unchanged; zero word changes, zero parser/drop errors. DHW mode is not represented in that recurrent block.

### External genuine Online capture — major architecture correction
A working Thermia Online installation shows a real slave `0x0F` ACKing FC16 and serving FC03 reads. During Heat Curve 20->21->20, the two captured `03E8` read snapshots differ only at the first word, 23->22. The capture also shows recurrent controller->0x0F FC16 block families and no response to the recurring `0x06` FC17 poll. This strongly shifts the Online/DCM hypothesis from `0x06` toward a shared register interface at `0x0F`. Slave `0xA5` is also active but remains unidentified.

### EXP137 — PREPARED — 0x0F FC16 ACK-only presence probe
30 s passive collision-check baseline, then up to 90 s ACK-only responses to exact known XTR 0x0F FC16 shapes (`03E8/14`, `0442/13`, `04A6/13`, `085F/5`). No FC03 responses and no register values injected. Positive = controller starts an 0x0F FC03 read after ACK-only presence; first read stops TX immediately.


### EXP137 — 0x0F FC16 ACK-only presence probe — COMPLETE / POSITIVE TRANSPORT PROGRESSION

Hypothesis:
Simple slave-0x0F presence/acknowledgement may cause the controller to progress toward the genuine Online/DCM read phase.

Observed:
- 30 s baseline: `fc16Seen=42`, all `whitelisted=42`, `unknown=0`, no 0x0F FC03 and no responder activity.
- Active phase:
  - ACK `03E8/count14` once;
  - controller immediately introduced new `0410/count22`;
  - ACK `085F/count5` once;
  - `0410/count22` was never ACKed and repeated 83 times.
- Final summary:
  `duration_ms=120150 fc16Seen=127 whitelisted=44 unknown=83 ackTx=2 txRefused=0 fc16AckSeen=0 fc03Req=0 fc03Resp=0 resyncDelta=0 dropDelta=0 DE_LOW`

Conclusion:
The controller advanced from the normal unacknowledged XTR 0x0F pattern into a new `0410/count22` stage only after the first `03E8/count14` ACK. Continuous retransmission of `0410/count22` without ACK strongly indicates an acknowledged sequential transfer/synchronization state machine.

Negative:
No FC03 phase was reached because `0410/count22` remained unacknowledged.

Next:
EXP138 adds only `0410/count22` to the ACK whitelist.


### EXP138 — sequential 0x0F FC16 ACK probe — PREPARED
Hypothesis: after EXP137's proven progression `03E8/count14 ACK -> 0410/count22`, ACKing only `0410/count22` as the one new variable will reveal the next controller stage.

Only change versus EXP137:
- add `0410/count22` to the ACK whitelist.

Positive:
- first previously unseen FC16 shape after a successful 0410 ACK; or
- first 0x0F FC03 request after a successful 0410 ACK.

On either positive discriminator, TX stops immediately. New FC16 shapes are logged but not ACKed. FC03 is never answered. No semantic values are injected.


### Genuine Online capture follow-up — RAW FRAME CORRECTION
fclauson's follow-up interpretation claimed a direct `20 -> 21 -> 20` value path in `0x0848/0x07E4`. Independent raw parsing shows:
- first `0848/count23`: `0858=0`, `085A=20`;
- second `0848/count23`: `0858=21`, `085A=20`;
- therefore the actual delta is `0858: 0 -> 21`, not one field `20 -> 21`;
- the later `07E4` block does not prove the same field reverted to 20.

Record `0858=21` as a strong Heat-Curve-change/event candidate only. Do not label it as the persistent Heat Curve register yet.


### EXP138 — sequential 0x0F FC16 ACK probe — COMPLETE / POSITIVE TRANSPORT PROGRESSION

Observed:
- after reboot, controller was still stuck/retrying `0410/count22` throughout the passive baseline;
- baseline `fc16Seen=28`, all known, no FC03, no responder;
- first active `0410/count22` was ACKed;
- ~1.54 s later controller advanced to new `042E/count15`;
- new block was not ACKed and experiment stopped;
- final summary:
  `reason=POSITIVE_NEW_FC16_STAGE_AFTER_0410 duration_ms=31949 fc16Seen=30 whitelisted=29 unknown=1 ackTx=1 txRefused=0 fc16AckSeen=0 fc03Req=0 fc03Resp=0 existingResponder=NO resyncDelta=0 dropDelta=0 DE_LOW`.

Conclusion:
The acknowledged XTR 0x0F sequence is now locally proven as:
`03E8/14 -> ACK -> 0410/22 -> ACK -> 042E/15`.

Additional finding:
Controller sequence state persists across ESP reboot/responder disappearance; it resumes/retries the outstanding stage.

Next:
EXP139 adds only `042E/count15` to the ACK whitelist.


### EXP139 — sequential 0x0F FC16 ACK probe, stage 0x042E — PREPARED

Hypothesis:
ACKing the locally proven next-stage request `042E/count15` will advance the controller to a subsequent 0x0F transfer stage or to an FC03 read phase.

Only change versus EXP138:
- add `042E/count15` to the ACK whitelist.

Safety:
No register values are injected, FC03 is never answered, unknown next-stage FC16 shapes are logged but not ACKed, and TX stops immediately on the first positive discriminator.


### EXP139 — sequential 0x0F FC16 ACK probe, stage 0x042E — COMPLETE / POSITIVE TRANSPORT PROGRESSION

Observed:
- controller resumed/retried `042E/count15` throughout the passive baseline after ESP reboot;
- first active `042E/count15` was ACKed;
- ~0.52 s later `04A6/count13` appeared and was ACKed under the unchanged prior whitelist;
- ~1.55 s after that, new `04BA/count22` appeared;
- new block was not ACKed and test stopped;
- final summary:
  `reason=POSITIVE_NEW_FC16_STAGE_AFTER_042E duration_ms=32936 fc16Seen=31 whitelisted=30 unknown=1 ackTx=2 txRefused=0 fc16AckSeen=0 fc03Req=0 fc03Resp=0 existingResponder=NO resyncDelta=0 dropDelta=0 DE_LOW`.

Conclusion:
Locally observed sequence is now:
`03E8/14 -> ACK -> 0410/22 -> ACK -> 042E/15 -> ACK -> 04A6/13 -> ACK -> 04BA/22`.

Nuance:
`04A6/13` was already known from earlier passive XTR captures and was already whitelisted, so EXP139 does not prove it is exclusively sequence-owned. It is nevertheless an observed intermediate stage in this run.

Next:
EXP140 adds only `04BA/count22` to the ACK whitelist.


### EXP140 — sequential 0x0F FC16 ACK probe, stage 0x04BA — PREPARED

Hypothesis:
ACKing the locally proven next-stage request `04BA/count22` will advance the controller to a subsequent 0x0F transfer stage or to an FC03 read phase.

Only change versus EXP139:
- add `04BA/count22` to the ACK whitelist.

Safety:
No register values are injected, FC03 is never answered, unknown next-stage FC16 shapes are logged but not ACKed, and TX stops immediately on the first positive discriminator.


### EXP140 — sequential 0x0F FC16 ACK probe, stage 0x04BA — COMPLETE / POSITIVE TRANSPORT PROGRESSION

Observed:
- controller resumed/retried `04BA/count22` throughout the passive baseline after ESP reboot;
- first active `04BA/count22` was ACKed;
- ~0.65 s later new `05FF/count33` appeared;
- new block was not ACKed and test stopped;
- final summary:
  `reason=POSITIVE_NEW_FC16_STAGE_AFTER_04BA duration_ms=31011 fc16Seen=30 whitelisted=29 unknown=1 ackTx=1 txRefused=0 fc16AckSeen=0 fc03Req=0 fc03Resp=0 existingResponder=NO resyncDelta=0 dropDelta=0 DE_LOW`.

Conclusion:
Locally observed sequence now extends to:
`03E8/14 -> ACK -> 0410/22 -> ACK -> 042E/15 -> ACK -> 04A6/13 -> ACK -> 04BA/22 -> ACK -> 05FF/33`.

Next:
EXP141 adds only `05FF/count33` to the ACK whitelist.


### EXP141 — gated 0x0F sequence walker — PREPARED

Hypothesis:
Multiple additional controller-side 0x0F sync stages can be discovered in one run without reflashing, while retaining explicit approval for every newly observed FC16 start/count pair.

New automatic target:
- `05FF/count33` (locally proven by EXP140).

Unknown-stage gate:
1. observe exact start/count at least 3 times;
2. log full payload;
3. lock candidate;
4. operator presses `EXP141 ARM ACK Current Candidate Once`;
5. no asynchronous TX occurs;
6. next exact matching request receives one standard FC16 ACK;
7. continue to next unknown stage.

Limits/guards:
- max 8 manually approved stages;
- no FC03 response;
- no semantic value injection;
- abort on real 0x0F responder, parser resync, or RX drop.


### EXP141 — gated 0x0F sequence walker — RUNNING / PARTIAL POSITIVE

Observed:
- baseline: repeated known `05FF/count33`;
- active phase ACKed `05FF/count33`;
- new block appeared ~1.56 s later: `0662/count33`;
- exact payload repeated consistently;
- candidate locked after 3 exact start/count observations;
- no `ARM_OK` or manual-stage ACK appears in the supplied log, so the controller remained retrying `0662/count33`;
- no parser resync, RX drop, FC03, or real 0x0F responder activity in the shown run.

New proven progression:
`05FF/33 -> ACK -> 0662/33`.

Current action:
Press `EXP141 ARM ACK Current Candidate Once` while the walker remains active.


#### EXP141 continuation — 0662/33 ACKed
- `ARM_OK` accepted the locked `0662/count33` candidate.
- next exact request received one `MANUAL_GATED` FC16 ACK.
- log confirms `MANUAL_STAGE_ACKED stage=1 start=0662 count=33`.
- repeated `0662` traffic then stopped.
- no subsequent EXP141 FC16/FC03 event is present for at least ~11 s in the supplied continuation fragment.

This is different from earlier stages, where the next FC16 block followed within ~0.5–1.6 s.
Do not classify 0662 as terminal yet; continue observing until a new stage, FC03, or timeout summary appears.


### EXP142 — post-0x0662 gated sequence walker — PREPARED

Hypothesis:
Automatic ACK of the locally proven `0662/count33` stage may expose the next post-sync behavior without requiring another manual gate for that already-tested block.

Only new ACK target:
- `0662/count33`.

All later unknown FC16 stages remain human-gated after >=3 exact repetitions. FC03 is never answered.

Active observation window is 900 s to catch a delayed phase transition after 0662.


### EXP142 — post-0x0662 gated sequence walker — RUNNING / IMPORTANT NEGATIVE

Observed:
- 30 s baseline completed with `fc16Seen=0`.
- Active phase began with `fc16Seen=0 known=0 unknown=0`.
- For ~61 s of active observation in the supplied log there was no slave-0x0F FC16 or FC03 traffic.
- normal bus traffic continued; parser resyncs and RX drops remained zero.

Conclusion:
The controller does not retransmit `0662/count33` after the EXP141 ACK and reboot. The post-0662 state therefore persists on the Thermia side and the FC16 sync stream is currently quiescent.

This is an important negative result, not a walker failure.


### EXP143 — passive post-sync Heat Curve trigger probe — PREPARED

Hypothesis:
A manual +1 Heat Curve change and restore may trigger the otherwise quiescent post-0662 0x0F path.

Only variable:
Heat Curve on the Thermia UI, current -> current+1 -> original.