# THERMIA EXPERIMENT LOG

Last updated: 2026-09-27

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

ESP behavior:
strictly passive; no ACK, no FC03 response, no Modbus write.

Controls:
- START
- MARK +1 applied
- MARK restored
- STOP

Positive:
0x0F FC16 or FC03 activity temporally associated with the manual change or restore.


### EXP143 — passive post-sync Heat Curve trigger probe — COMPLETE / STRONG POSITIVE

Observed:
- passive baseline: no 0x0F FC16/FC03;
- after manual Heat Curve +1, `0x0F FC16 03E8/count14` started immediately;
- controller repeated it continuously because no ACK was sent;
- first payload word was `0x0024` while HA showed Heating Curve 36;
- after restoring Heat Curve, first payload word became `0x0023` while HA showed Heating Curve 35;
- remaining 13 words stayed unchanged in the shown frames;
- final summary:
  `fc16=103 fc03Req=0 fc03Resp=0 fc16Ack=0 resyncDelta=0 dropDelta=0 DE_LOW`.

Conclusion:
A Heat Curve UI change re-triggers the 0x0F FC16 sync path at `03E8/count14`, and the first word of that FC16 payload directly tracks the Heat Curve value in this run.

Negative:
No FC03 was reached because `03E8/count14` was deliberately not ACKed.

Next:
EXP144 = same manual Heat Curve trigger, then ACK only already-proven sequence shapes and stop on the first unknown FC16 or FC03 discriminator.


### EXP144 — Heat Curve-triggered known-sequence progression — PREPARED

Hypothesis:
The event-triggered sync discovered in EXP143 can be walked through the already-proven FC16 stages and may reveal either a new FC16 stage or FC03 read phase.

Single protocol-method change:
Known shapes are ACKed after the manual +1 Heat Curve trigger.

Stop conditions:
- first unknown FC16: log, no ACK, stop;
- first FC03 request: log, no response, stop.

Heat Curve must be restored to its original value after the run.


### EXP144 — Heat Curve-triggered known-sequence progression — ABORTED / PROCEDURAL

Observed:
- baseline immediately contained repeated `03E8/count14`;
- payload first word remained `0x0023` (35);
- 29 FC16 requests seen in 30 s;
- no FC03, no real 0x0F ACK/response;
- parser/drop clean;
- automatic abort:
  `ABORT_BASELINE_0F_ACTIVITY fc16=29 fc03Req=0 fc03Resp=0 fc16Ack=0 DE_LOW`.

Interpretation:
The outstanding `03E8/count14` request from EXP143 persisted over reboot. Therefore EXP144's quiet-baseline prerequisite was invalid for the actual controller state and the intended hypothesis was not tested.

Next:
EXP145 resumes the pending event-triggered sequence directly; no new Heat Curve UI change.


#### EXP144 attempts 2 and 3 — reproduced procedural abort
Both additional attempts again saw only repeated `03E8/count14` with first word `0x0023` during baseline and both aborted after 29 FC16 requests / 30 s. No FC03 or real 0x0F responder appeared.

This strengthens the conclusion that the outstanding event-triggered 03E8 retry state is persistent and must be ACKed before progression can resume.


### EXP145 — pending 0x03E8 sync to FC03 transition probe — PREPARED

Hypothesis:
Complete the persistent event-triggered controller->0x0F sync using only proven ACKs, then test specifically for the transition to `0x0F FC03` or another post-sync stage.

No new Thermia UI change.

Baseline:
10 s, only repeated `03E8/count14`, minimum 3 requests.

After ACKing known sequence:
- first unknown FC16 => stop/no ACK;
- first FC03 => stop/no response;
- after ACK of `0662/count33`, all experiment TX stops and 120 s passive post-sync observation begins.

A5/A4 FC03 requests are logged passively for comparison with the genuine Online capture.


### EXP145 — pending 0x03E8 sync to FC03 transition probe — COMPLETE / IMPORTANT NEGATIVE

Observed:
- baseline: 10 exact `03E8/count14` retries, first word `0x0023`;
- baseline accepted;
- one ACK sent to the next `03E8/count14`;
- retries stopped immediately;
- for at least ~69 s afterward: no further 0x0F FC16, no 0x0F FC03, no A5/A4 FC03;
- parser/drop clean.

Conclusion:
The event-triggered Heat Curve update is a one-block ACK-gated update, not a replay of the long startup/snapshot chain.

Negative result:
ACKing the event-triggered 03E8 block does not itself trigger FC03 read-side behavior.

Next:
Investigate the missing Online-side trigger around the first genuine Online FC03 request instead of continuing FC16 chain-walking.


### EXP146 — direct Online-style 0x0F FC03 0708 read probe — PREPARED

Hypothesis:
The genuine Online module itself may be the source of `0x0F FC03` reads.

Test:
After a clean 10 s baseline, transmit exactly once:
`0F 03 07 08 00 06 44 50`.

This exact request is present in the genuine Online capture and receives a 12-byte FC03 response there.

No semantic write is performed. Positive = local 0x0F responds; negative = no response within 2 s.


### EXP146 — direct Online-style 0x0F FC03 0708 read probe — INVALID / PROCEDURAL

Two attempts transmitted the intended exact request:
`0F 03 07 08 00 06 44 50`.

However both runs logged `NO_RESPONSE_2S` approximately 8–10 ms after `FC03_TX`.

Root cause:
`phase_ms` was calculated while still in phase 1. The code then transmitted, changed to phase 2, and continued in the same interval invocation; the stale phase-1 elapsed time (~10 s) immediately satisfied the phase-2 `>=2 s` timeout.

Therefore:
- no real 2 s response window was observed;
- "no response" is not a valid protocol result;
- the Online-side-master hypothesis remains open.

Second run additionally showed two CRC-resync warnings shortly after TX, but because the experiment had already terminated incorrectly these are not yet interpretable.

Next: EXP147 = exact same read request with corrected response-window timing only.


### EXP147 — corrected Online-style 0x0F FC03 0708 read probe — PREPARED

EXP146 was invalid because its nominal 2 s response window collapsed to ~10 ms.

EXP147 changes only the timing implementation:
- dedicated TX timestamp;
- immediate return after TX;
- true timeout based on `now - tx_ms`.

Protocol stimulus is unchanged:
`0F 03 07 08 00 06 44 50`

Positive = byte-count-12 FC03 response from 0x0F.
Negative = no response during a genuine 2 s observation window.


### EXP147 — corrected Online-style 0x0F FC03 0708 read probe — COMPLETE / NEGATIVE

Observed:
- exact request transmitted at 23:38:38.137:
  `0F 03 07 08 00 06 44 50`;
- experiment ended at 23:38:40.375, giving ~2.238 s actual post-TX observation;
- no matching 0x0F FC03 response;
- no other 0x0F activity in that window;
- normal bus traffic continued.

Logging bug:
The summary format string has 8 `%u` fields but only 7 numeric arguments after `reason`, so `responseWindowMs`, `tx`, and later printed fields are shifted/corrupt. This does not invalidate the protocol observation because TX and timing are independently visible in timestamped log lines.

Conclusion:
A bare exact Online-style FC03 read is not sufficient to obtain a local 0x0F response in the current state.

Next:
reconstruct the genuine Online topology/session prerequisite, with A5/A4 as the leading discriminator.


#### EXP147 repeat run — same negative reproduced
Second run:
- TX 23:39:13.389;
- summary 23:39:15.632;
- actual response window ~2.243 s;
- no 0x0F response and no other 0x0F activity.

This reproduces the first negative result. The summary printf-field defect remains and must not be used for counter interpretation.


### EXP148 — passive Online topology and timing profiler — PREPARED

Hypothesis:
Missing A5/A4/session topology may be the reason local direct 0x0F FC03 reads do not answer.

Run:
300 s passive only.

Logs and counts:
A5/A4 FC03, 0x0F FC03/FC16, 0x06 FC17, plus inter-event timing buckets.

No experiment TX is generated.


### EXP148 — passive Online topology and timing profiler — COMPLETE / STRONG TOPOLOGY NEGATIVE

Final 300 s summary:
`A5req=0 A5resp=0 A4req=0 A4resp=0 0F03req=0 0F03resp=0 0F16write=280 0F16ack=0 06req=69 06resp=0 gaps_101_500=69 gaps_gt500=279 resyncDelta=0 dropDelta=0 DE_LOW`

Interpretation:
- A5/A4 absent for the full clean run.
- No 0x0F FC03 activity despite heavy 0x0F FC16 activity.
- 69/69 0x06 poll-related short gaps landed in 101–500 ms, consistent with the repeatedly observed ~254 ms 0x06 -> 0x0F 04A6 schedule.

Conclusion:
The no-Online local topology is missing an active logical/session layer present in the genuine Online capture. Continue with ownership/presence discrimination rather than more arbitrary FC03 register reads.


### EXP149 — A5 0x0000 ownership probe — PREPARED

Hypothesis:
A5 may be an endpoint owned by the genuine Online/DCM hardware.

Exact read-only stimulus copied from genuine Online:
`A5 03 00 00 00 12 DC E3`
(start 0x0000, count 18).

Expected genuine response shape:
A5 FC03 with byte count 0x24 (36 data bytes; 41-byte total frame).

Run:
5 s passive baseline, >=20 ms idle gap, one TX, true 2 s response window.

No semantic write is performed.


### EXP149 — A5 0x0000 ownership probe — COMPLETE / NEGATIVE

Exact request:
`A5 03 00 00 00 12 DC E3`

Result:
- one TX;
- true response window = 2016 ms;
- no A5 response;
- no other A5 activity;
- no 0x0F FC03;
- resyncDelta=0;
- dropDelta=0;
- DE_LOW.

Conclusion:
The exact genuine-Online A5 read is not answered in the local no-Online topology.

Combined with EXP148, A5 is strongly indicated to belong to or depend on the missing genuine Online/DCM topology rather than the heat-pump controller itself.


### EXP150 — staged Online/DCM bootstrap role-emulation harness — PREPARED

Single hypothesis:
sustained known `0x0F` slave-side ACK presence may bootstrap the missing Online/DCM read/discovery layer.

Efficiency:
one gated run combines:
- passive baseline;
- known-shape `0x0F FC16` ACK-only presence;
- exact captured A5 discovery responses if requested;
- one exact `0x0F 0708/count6` read-only probe;
- conditional exact `0x0F 03E8/count13` probe if the first succeeds.

Known caveat:
ACKing 0x0F FC16 deliberately advances the proven controller transfer state machine.

No semantic payload values are invented.


### EXP150 — staged Online/DCM bootstrap role-emulation harness — COMPLETE / NEGATIVE

Observed:
- phase 1 passive baseline showed pending `04A6/count13`;
- phase 2 ACKed `04A6/count13`, then `0662/count33`;
- phase 3 armed exact A5 responder, but no A5 request appeared;
- no A4 activity;
- no spontaneous `0x0F FC03`;
- phase 4 sent exact genuine `0F 03 0708 0006 4450`;
- no response in 2015 ms;
- `ack=2`, `ackRefused=0`, `A5req=0`, `A5resp=0`, `A4=0`, `0F03req=0`, `0F03resp=0`, `resyncDelta=0`, `dropDelta=0`.

Conclusion:
ACK-capable `0x0F` presence alone is not the missing Online/DCM bootstrap.

Next:
test simultaneous known-good `0x06` accessory presence plus `0x0F` ACK/mailbox presence in one controlled harness.


### EXP151 — combined 0x06 + 0x0F role-emulation harness — PREPARED

Hypothesis:
simultaneous known 0x06 accessory presence plus known 0x0F ACK/mailbox presence may enable the missing Online/DCM read/discovery layer.

Run:
- 10 s passive baseline;
- 60 s combined 0x06 REQ-low responder + known 0x0F ACK service + exact A5 responder if polled;
- then exact read-only 0x0F 0708/count6 probe;
- conditional 03E8/count13 probe only after a valid 0708 response.

No semantic setting write or AFCA REQ transaction is introduced.


### EXP151 — combined 0x06 + 0x0F role-emulation harness — COMPLETE / NEGATIVE

Observed:
- 2 passive baseline 0x06 polls;
- phase 2 enabled the known REQ-low 0x06 responder;
- final counts: `06req=60`, `06resp=58`, `06refused=0`;
- fast accessory-presence cadence restored;
- no 0x0F FC16 occurred during the active combined-role window, so `ack=0`;
- no A5/A4 traffic;
- no spontaneous 0x0F FC03;
- exact genuine `0F 03 0708 0006 4450` sent after 60 s of 0x06 presence;
- no response in 2010 ms;
- `resyncDelta=0`, `dropDelta=0`.

Conclusion:
Valid 0x06 transport presence does not make the local 0x0F FC03 read side appear and does not trigger A5/A4 discovery.

The intended simultaneous 0x0F ACK role was armed but not exercised in this run because the controller produced no FC16 transaction during the phase.

Architectural implication:
A5/A4 and the 0x0F FC03 responder increasingly look like endpoints/functions hosted by the missing external Online/DCM participant itself.


### EXP152 — genuine Online ownership reconstruction — COMPLETE / OFFLINE

No bus TX.

Main result:
The genuine Online capture behaves like a coordinated polling schedule:
A5 service reads, 0x04/0x06 polling, 0x0F read service, and 0x0F write/ACK traffic coexist in a topology not present locally.

A5 provides three repeated read blocks and later falls back to equivalent A4 reads when A5 disappears. 0x0F provides both FC16 ACK and FC03 data service.

Strongest current ownership hypothesis:
the heat-pump controller remains the common master and enables extra A5/A4 + 0x0F FC03 polling only after recognizing genuine external Online/DCM hardware.

This is not electrically proven from the two-wire capture.

Untested quadrant identified:
cold boot with BOTH 0x06 accessory presence and 0x0F slave ACK/service presence from the beginning.

Decision:
EXP153 = cold-boot combined-role presence test.


### EXP153 — cold-boot combined 0x06 + 0x0F role presence — PREPARED

Hypothesis:
recognition of the genuine Online/DCM topology may be boot-latched and require both external roles present from first relevant controller traffic.

Arm while bus is healthy, then restart the heat-pump/controller while ESP remains powered. The firmware waits for >=3 s bus-down, detects the first returned valid frame, and only then enables:
- known 0x06 REQ-low responder;
- strict known 0x0F FC16 ACK;
- exact A5 responses if A5 is spontaneously polled.

A4 and spontaneous 0x0F FC03 are observation-only.

Positive = any spontaneous A5/A4/0x0F FC03 after boot return.
Negative = 300 s clean post-return with none.


### EXP153 — cold-boot combined 0x06 + 0x0F role presence — COMPLETE / NEGATIVE

Observed:
- real bus-down confirmed;
- ~18.547 s controller outage;
- first returned valid frame: `0x1E FC04`;
- combined emulation active immediately on return;
- boot-time 0x0F ACK sequence:
  `04BA/22 -> 05FF/33 -> 04A6/13 -> 085F/5 -> 0662/33 -> 04A6/13`;
- continuous valid 0x06 REQ-low responses;
- final after 300 s:
  `06req=297 06resp=283 06refused=0 ack=6 ackRefused=0 unknown0F16=0 A5req=0 A5resp=0 A4=0 0F03req=0 0F03resp=0 resyncDelta=0 dropDelta=0`.

Conclusion:
Cold-boot presence of both known transport roles is not sufficient to activate A5/A4 or 0x0F FC03. The missing prerequisite is now strongly likely to be semantic identity/application state rather than presence/timing.

Next:
return to firmware-led identity/integration reconstruction and choose one evidence-backed semantic discriminator for EXP154.


### EXP154 — semantic firmware→wire reconstruction — COMPLETE / OFFLINE

Main finding:
Recovered HE `0x4414 IntegrationMode` and public Online `0x0559 Link Integration` match semantically and enum-for-enum:
- 0 = LIGHT
- 1 = SYSTEM.

Firmware shows IntegrationMode triggers SystemIntegrationInit and a full three-group sync. The public Online dump identifies `0x0559` as writable Link Integration.

Confidence is strengthened because the same Online registerIndex namespace is locally validated on the XTR at `0x0442 Activate Cooling` and strongly matches the local `03E8..03EE` heating family.

Limitation:
`0x0559` has not yet been observed natively on this XTR; EXP119 saw no 0559 boot broadcast. Therefore the mapping is STRONGLY INDICATED, not PROVEN.

Decision:
No blind write. EXP155 should determine the local ownership/direction/block shape for `0x0559`.


### EXP154 refinement — documentary DCM03 integration-mode / approval evidence

External Danfoss HP-kit manual adds two high-value facts:
1. DCM03 has an explicit selectable Danfoss Link vs Danfoss Online integration mode, changed/reported by triple button press.
2. Gateway-based HP-kit diagnostics explicitly include `DCM-HP approval`, approval failure, and `sending settings to DCM` states.

This provides independent documentary support for the missing semantic approval layer inferred from EXP147–153.

It also narrows the role of public `0x0559 Link Integration`: it remains a strong candidate, but may represent DCM-side integration state rather than a simple controller-local boot register.

Decision:
EXP155 should use a genuine DCM03 mode toggle as the controlled variable and compare the exact bus delta. Do not spend another local experiment on passive 0559 observation already covered by EXP119/153.


### EXP155 — genuine DCM03 Link ↔ Online mode-transition capture — PREPARED

Passive-only. Controls under Configuration:
START, MARK Switch to LINK, MARK Switch to ONLINE, STOP.

Run sequence:
Online baseline 30–60 s -> MARK LINK + immediate physical DCM triple-press -> ~60 s -> MARK ONLINE + immediate triple-press -> ~60 s -> STOP.

No RS485 TX is generated by EXP155.


### EXP155 — correction before execution

The previously prepared genuine-DCM mode-transition YAML is not runnable on the local installation because no DCM03 hardware is available.

This is not a failed experiment; it was a planning mismatch.

EXP155 is re-scoped to offline serializer/ownership reconstruction using existing genuine capture + firmware + Online dump + documentation. No bus TX.

### EXP155 — Discussion #143 / genuine capture re-analysis — OFFLINE

Key correction: the external AI commentary claiming Heat Curve 20->21->20 in FC16 block 0x0848 is not supported by direct word parsing. At 12.116 `0x0858=0, 0x085A=20`; at 33.107 `0x0858=21, 0x085A=20`. The 43.705 frame is a different block (`0x07E4/count17`).

Most valuable new lead: obtain the actual `0F_register_value_map.xlsx`, `modbus_slave.py`, and `config.yaml` referenced by fclauson. These are likely to contain more actionable ownership/block information than another local speculative write.


### EXP155 — fclauson 0F artifacts — COMPLETE / OFFLINE

Analysed `0F_register_value_map.xlsx`, `modbus_slave.py`, and add-on manifests.

Key result:
- passive logger tracks Unit 0x0F FC03 read blocks;
- spreadsheet maps 1000..1012 (position 12 = 1012 room target) and 1040..1060 (position 13 = 1053 DHW start);
- FC16 map includes 1350..1369 with 1363=4 and 1369=0;- public semantics identify those as Operation Mode and Link Integration.

Conclusion:
`0x0559 Link Integration` is observed in the FC16 controller->0x0F state/snapshot direction, so it should not be used as a guessed DCM->controller activation write.

The stronger model is:
controller writes state/snapshots to 0x0F via FC16; controller reads desired-state/command mailbox areas from 0x0F via FC03.

Next:
anchor on the proven 03E8/count13 FC03 command mailbox and reconstruct genuine command semantics / scheduler activation.

### EXP156 — genuine Online connected + local display Heating Curve change — COMPLETE / POSITIVE

Hypothesis: a local-display setting change should update controller->0x0F FC16 state without requiring the remote command-mailbox FC03 03E8/count13 path.

Capture: `thermia_capture_20260925_071517.log`, ~79.4 s / 674 frames.

Observed:
- 0x0F FC03 only at 0708/count6 (18x); **no FC03 03E8/count13**.
- FC16 03E8/count13 at 22.185 s: 03E8=23.
- FC16 03E8/count13 at 61.676 s: 03E8=22.
- Remaining 12 words unchanged.
- 0848-family changes were unrelated dynamic fields, not a clean 23->22 mirror.

Conclusion:
Local Heating Curve change is propagated in the FC16 state/snapshot direction and does not itself cause an FC03 03E8/count13 read. This strongly supports FC03 03E8/count13 as an externally supplied desired-state/command path rather than a generic settings mirror.

Also observed:
A4 is transiently probed and A5 resumes shortly after; treat A4 as alternate/discovery/fallback-like, not as proof of permanent A5 failure.

### EXP157 — genuine DCM + HP power-up captures — COMPLETE / POSITIVE

Hypothesis: boot captures can separate Online discovery from 0x0F mailbox readiness and expose the trigger for the initial state sync.

Observed:
- DCM power-up: early repeated valid `C8 FC03 2328/count2`; 0x0F already ACKing by 0.389 s; A5 responsive by 1.236 s; long ACKed FC16 sync sweep `042E..06F4`; one valid `A4 FC06 0032=0046` later.
- HP power-up: A5 already responsive, but 0x0F FC03 `0708/count6` unanswered and FC16 `0870/count17` unACKed for ~66 s.
- First 0x0F ACK at 66.860 s; next 0708 read gets a response; then broad ACKed FC16 initial sync begins at `03E8`, followed by `03FC`, `0410`, `042E`, etc.
- A4 discovery trio + 0x05 FC17 occurs before 0x0F readiness.

Strong conclusion: A5 discovery/status availability and 0x0F mailbox readiness are separate stages. First successful 0x0F ACK is a strong gate for the controller's full state/configuration upload to the DCM.

Safety/result: offline/passive analysis only; no local TX.

## EXP158 — Cross-capture structural analysis — COMPLETE / POSITIVE

**Hypothesis:** the two new genuine boot captures can expose stable address/service pairing and separate deterministic initial-sync fields from dynamic data.

**Observed facts:**
- Nine unanswered `C8 FC03 2328/count2` probes occur only in the DCM-power-up capture, with alternating ~1.28/~0.81 s gaps.
- A4 and A5 are queried with the same three FC03 shapes. In HP boot, the A4 triplet is immediately followed by 0x05 FC17; normal Online runtime pairs A5 activity with 0x06 FC17.
- `A4-05 = A5-06 = 0x9F`, strongly supporting paired logical slots/services `A4<->05` and `A5<->06`.
- The one-off `A4 FC06 0032=0046` writes a register/value that exactly matches A5 register 0032 inside its `002E/count10` response.
- Across the two boot captures, 27/28 overlapping FC16 initial-sync blocks in `042E..06F1` are byte-identical. Only `06EA/count7` changes.
- `06EA/count7` is RTC/date-time. The same fields are mirrored later at runtime `0858..085E`; elapsed seconds line up exactly with capture time.
- `085F/count5` periodically interleaves with the HP initial-sync upload, so it is not part of the linear bulk config sequence.
- `0708/count6` responses change form across mailbox-ready / sync / post-sync phases, so that block carries session/state information.

**Strong conclusions:**
- A4/05 and A5/06 are structurally paired address families, not a simple primary/fallback pair.
- A4/A5 share register semantics/layout.
- Genuine initial-sync content is highly deterministic across DCM-only and HP boots.
- `06EA..06F0` is an initial-sync RTC block and `0858..085E` its runtime mirror.

**Negative/open results:**
- C8 remains unanswered and semantically unknown.
- A4 FC06 ownership/effect remains unknown; do not reproduce it yet.
- HP boot omits visible 06F4 before runtime; reason unknown.

## EXP159 — Passive wildcard no-DCM cold-boot differential — PREPARED

**Hypothesis:** the newly discovered DCM-era boot addresses/functions (`0xC8`, `0xA4/0xA5`, `0x05/0x06`, FC06 and `0x0F` mailbox traffic) can be classified against a clean local no-DCM cold boot only if the parser is widened beyond the address/function whitelist used in older EXP94-era tooling.

**Why this is not a repeat of EXP94:** EXP94 established the no-DCM controller/accessory state machine (`A80E 0->8->0x28`, `AFDC 0->0x10`) but its parser/logging was designed before `C8`, `A4/A5`, `0x05` and A4 FC06 were known as relevant boot/discovery traffic. EXP159 changes only observability: wildcard legal-slave parsing plus FC06 recognition.

**Only controlled variable:** power-cycle the heat-pump/controller with no DCM present. ESP32/Waveshare remains externally powered and already listening. No setting is changed.

**Instrumentation:**
- accept CRC-valid Modbus frames for legal slave IDs `0x01..0xF7`;
- recognize FC03/FC04/FC06/FC16/FC17 and exception frames;
- focused red/brown logs for `C8`, `A4/A5`, `05/06`, `0x0F`, first 15 s of `0x02`, and first-seen unexpected slave IDs;
- auto-detect >=3 s complete bus silence, set first returning valid frame to t=0, capture 180 s;
- summary counts include `C8`, A4, A5, 05, 06, 0F FC03 req/rsp, 0F FC16 req/ACK, unexpected addresses, parser resyncs and RX drops.

**Safety:** strictly passive RX-only; GPIO17 TX not configured; DE forced LOW; no replies/ACKs, no 05/06 response, no scan, no register write, no room-sensor emulation. Known-good production parsing/entities remain intact.

**Success criteria:** determine with current observability whether `C8`, A4/A5, 05/06 pairing, FC06, 0x0F FC03 or ACKed 0x0F FC16 appear during a no-DCM cold boot and align their timing against EXP157 genuine DCM/Online boot.

**Negative result:** none of the newly discovered discovery/mailbox frames appears despite a valid complete boot capture with zero parser/RX errors. This would materially strengthen the conclusion that the missing layer is DCM-dependent rather than ordinary controller startup.

**Prepared YAML:** `thermia_exp159_passive_wildcard_cold_boot_profiler.yaml`.

**Current experiment:** **EXP159 PREPARED / PASSIVE WILDCARD NO-DCM COLD-BOOT DIFFERENTIAL.**

## EXP159 — Passive wildcard no-DCM cold-boot differential — COMPLETE / POSITIVE

**Hypothesis:** C8/A4/A5/05/06/0F boot traffic may distinguish genuine DCM startup from ordinary no-DCM controller startup when observed with a widened passive parser.

**Observed:**
- passive RX-only; no TX/ACK/response/scan/write;
- bus-down confirmed after 3005 ms quiet; first returned frame set t=0;
- exact `C8 FC03 2328/count2` occurred with no DCM: 20 requests from +0.565 s to +20.775 s, no response;
- controller state reproduced known boot path A80E 0->8->0x28 and sequence 5->10;
- 0x06 FC17 appeared from +0.789 s; AFDC settled to 0x0010;
- 0x0F FC16 requests: 04BA/count22 twice, then repeated 04A6/count13 and periodic 085F/count5; zero ACKs observed;
- no A4, A5, 0x05, FC06 or 0x0F FC03 observed in the available ~90 s post-boot capture;
- capture ended before planned 180 s summary.

**Strong conclusion:** C8 probing is generic native cold-boot discovery, not a DCM-specific signature. The higher-value DCM discriminator remains the transition into A5/A4/05 and responsive 0x0F FC03/FC16 mailbox behaviour.

**Negative result recorded:** absence of DCM does NOT suppress C8 probing. Reject the previous hypothesis that C8 itself is DCM-originated/DCM-specific.

**Current experiment:** EXP159 COMPLETE / POSITIVE GENERIC-DISCOVERY DIFFERENTIAL.

## EXP160 — isolated genuine A5 responder — COMPLETE / NEGATIVE

**Hypothesis:** exact genuine A5 service responses may be sufficient to advance controller discovery beyond the generic no-DCM boot state seen in EXP159.

**Observed:** clean no-DCM cold boot completed for 180 s. No A5 request occurred, therefore the exact A5 responder was never invoked (`A5=0`, `A5tx=0`). No A4/05 activity and no `0x0F FC03` occurred. The controller continued native C8 discovery and unACKed 0x0F FC16 startup traffic. Final summary: `frames=1596 s02=336 s05=0 s06=42 s0F=290 A4=0 A5=0 A5tx=0 C8=20 0F03req=0 0F03rsp=0 0F16req=248 0F16ack=0 resyncDelta=0 dropDelta=0`.

**Strong conclusion:** an isolated passive A5 responder cannot advance the local no-DCM boot because the controller never addresses A5.

**Negative result recorded:** the captured A5 payloads were not disproven; they were never requested.

## EXP161 — offline cross-capture discovery analysis — COMPLETE / POSITIVE

**Hypothesis:** genuine DCM captures may reveal the ordering/prerequisite missing before A5 activation without another active bus intervention.

**Observed:** in the DCM-power-up capture, a successful 0x0F FC16 ACK is visible before the first A5 request, while C8 probes continue in parallel. A5 therefore does not require the C8 retry sequence to finish. Genuine DCM startup enters an ordered ACKed 0x0F initial-sync sequence. A4 can occur later while A5 is already established, so A4 is not a simple A5 precursor. Normal genuine runtime repeatedly shows the A5 triplet followed by 0x06 and responsive `0x0F FC03 0708/6` service.

**Strong conclusions:** C8 completion/success is not a necessary gate for A5/0x0F functionality; A4 is not a simple precursor to A5; genuine 0x0F service is operational before the first visible A5 transaction in the DCM-power-up capture.

**Hypothesis:** the missing local prerequisite is closer to a combined DCM service/mailbox presence or binding state than to C8 alone or A5 payload contents.

**Unknown:** the exact event that makes the controller begin A5 polling.

## EXP162 — combined known 0x0F FC16 ACK + genuine A5 responder — COMPLETE / NEGATIVE

**Hypothesis:** a working known 0x0F FC16 ACK role combined with the exact A5 responder may activate or advance DCM-like service state on a no-DCM cold boot.

**Observed:** 180 s run completed. The ESP transmitted six valid whitelisted 0x0F FC16 ACKs (`0FtxACK=6`), demonstrating that the active ACK path was exercised. Nevertheless no A5 request occurred (`A5=0`, `A5tx=0`), no A4/05 appeared, and no `0x0F FC03` request/response appeared. C8 remained at 20 probes. Final summary: `frames=1388 s02=344 s05=0 s06=43 s0F=49 A4=0 A5=0 A5tx=0 0FtxACK=6 C8=20 unexpectedSlaves=0 0F03req=0 0F03rsp=0 0F16req=6 0F16ack=0 resyncDelta=1 dropDelta=0`.

**Strong conclusions:** known 0x0F FC16 ACKs successfully advance/terminate the visible FC16 retry path, but 0x0F ACK + a waiting A5 responder is insufficient to activate A5 polling or `0x0F FC03` service.

**Negative result recorded:** do not repeat the hypothesis that merely acknowledging the visible 0x0F FC16 startup writes causes the controller to start A5 polling.

**Unknown:** the earlier discovery/binding/service-state prerequisite that enables A5 scheduling.

## EXP163 — 0x0F ACK then exact A5 master read-only probe — PROPOSED / NOT YET RUN

**Hypothesis:** A5 may be an endpoint that the genuine DCM actively reads rather than a service the DCM provides. After the known 0x0F ACK phase, issuing the exact captured A5 FC03 read triplet may reveal whether an A5 endpoint responds locally or whether this action changes subsequent controller scheduling.

**Only new experimental variable relative to EXP162:** remove the A5 slave responder and, after the known 0x0F ACK phase, send one bounded read-only A5 FC03 sequence: `0000/count18`, `0023/count1`, `002E/count10`. No A5 writes. C8/0x06/A4/0x05 remain otherwise passive; no room-sensor emulation.

**Success evidence:** a CRC-valid A5 response, newly autonomous A5 traffic, new `0x0F FC03`, A4/05 activation, or another repeatable state transition after the probe.

**Stop/negative criterion:** one bounded probe sequence completes without A5 response or higher-layer transition; do not escalate to guessed writes or broad scans.

Status: **PROPOSED / NOT YET RUN**.


---

## EXP163 — 0x0F ACK then exact A5 master probe — COMPLETE / NEGATIVE

**Hypothesis:** after the known `0x0F` ACK phase, the exact genuine A5 FC03 triplet may reveal or activate the missing service endpoint.

**Result:** valid 180020 ms no-DCM cold-boot run. Six known-shape `0x0F FC16` requests were ACKed. The ESP then transmitted exactly three read-only A5 FC03 requests (`0000/18`, `0023/1`, `002E/10`). No A5 response or higher-layer transition followed.

**Final summary:** `frames=1363 s02=338 s05=0 s06=42 s0F=48 A4=0 A5=0 A5probeTX=3 A5rsp=0 0FtxACK=6 C8=20 unexpectedSlaves=0 0F03req=0 0F03rsp=0 0F16req=6 0F16ack=0 resyncDelta=5 dropDelta=0`.

**Observed facts:** A5 response count remained zero; A4/0x05 remained absent; no `0x0F FC03` request appeared; C8 repeated 20 times; 0x06 continued normally. Five parser resyncs occurred at the end of the A5 injection sequence, with zero RX buffer drops and no continuing resync growth.

**Strong conclusion:** post-ACK exact A5 master polling does not establish A5 or the genuine DCM service state.

**Negative result:** do not repeat A5 read probing without a newly identified prerequisite.

## EXP164 — passive early-boot discriminator census — PROPOSED / NOT YET RUN

**Hypothesis:** a still-unmodelled early ordering/state discriminator can be isolated by a clean passive no-DCM cold boot and direct timing comparison with the genuine DCM power-up capture.

**Only change:** remove EXP163 active ACK/probe behaviour; add passive event timestamps/counters. No bus transmission.

**Success criterion:** identify at least one reproducible event/order/state difference that exists before genuine A5 activation and is absent/different in no-DCM boot.

**Stop criterion:** if the passive trace adds no new discriminator, close negative and return to offline differential analysis rather than escalating to guessed writes.

## EXP164 — COMPLETE / POSITIVE PASSIVE DISCRIMINATION
Hypothesis: passive early-boot ordering may reveal a missing pre-A5 DCM-binding discriminator.

Result: clean 180 s no-DCM cold boot, fully passive. Summary: `frames=1601 s05=0 s06=42 s0F=291 A4=0 A5=0 C8=20 0F03req=0 0F03rsp=0 0F16req=249 0F16ack=0 resyncDelta=0 dropDelta=0 PASSIVE_ONLY_DE_LOW`.

Observed: C8, 0x06, A80E `0->8->0x28`, AFDC=0x0010 and sustained unACKed 0x0F FC16 all occur without A5/A4/0x05/0x0F-FC03.

Conclusion: those visible states are not sufficient DCM recognition/binding discriminators. EXP164 reproduces EXP159 and closes the planned cold-boot series unless a future hypothesis uniquely requires another reboot.

## EXP165 — PREPARED — runtime DCM-surface hot-plug test
Hypothesis: simultaneous known 0x06 accessory presence plus exercised 0x0F ACK service at runtime may trigger the same dynamic service transition seen when a genuine DCM is powered while the controller is already running.

Basis: genuine DCM power-up capture 090209 shows 0x0F ACK at ~0.389 s and working A5 from ~1.179 s without controller restart. EXP151 did not actually exercise a 0x0F FC16 ACK during its combined runtime phase; EXP153 tested the same broad roles only at cold boot.

Controlled runtime surface: exact 0x06 REQ-low response, strict known 0x0F FC16 ACKs, and exact A5 responses only if A5 is autonomously requested. No AFCA strobe, semantic write, master probe, scan or reboot. 180 s automatic stop.

Status: **PREPARED / NOT YET RUN**.

## 2026-09-25 — EXP165 — runtime DCM-surface hot-plug — COMPLETE / PARTIAL NEGATIVE

Hypothesis:
Known 0x06 accessory presence plus known 0x0F ACK service, introduced while the controller remains running, may reproduce the genuine DCM hot-plug transition and activate A5 / 0x0F FC03.

Observed facts:
- No controller reboot.
- Final summary: `duration_ms=180020 frames=1330 s05=0 s06=43 s0F=5 A4=0 A5=0 06tx=0 0FtxACK=5 A5tx=0 0F03req=0 0F03rsp=0 0F16req=5 resyncDelta=0 dropDelta=0`.
- ACKed 0x0F FC16 blocks: 04A6/13, 085F/5, 04BA/22, 05FF/33, 0662/33.
- No A5, A4/05 or 0x0F FC03.
- No parser resync or RX drop.
- 43 0x06 frames were observed but zero 0x06 responses were transmitted.

Negative result:
Runtime 0x0F ACK service alone is insufficient to activate the DCM-like A5 / 0x0F FC03 service state.

Implementation defect:
The intended 0x06 role was not exercised because EXP165 required a 27-byte FC17 request; the native AFC8/12 + AFDC/5 request is 23 bytes. Thus EXP165 cannot be used as a negative result for simultaneous 0x06 + 0x0F presence.

Classification:
**COMPLETE / NEGATIVE for 0x0F-only runtime activation; INVALID for the intended combined-role hypothesis.**

## 2026-09-25 — EXP166 — corrected runtime 0x06 + 0x0F hot-plug — PREPARED

Hypothesis:
Actually exercising the proven 0x06 REQ-low responder at runtime together with the known 0x0F FC16 ACK role may activate native A5 and/or 0x0F FC03 without a controller reboot.

Single correction relative to EXP165:
- 0x06 exact FC17 request-length discriminator: 27 -> 23 bytes.

Controls and safety:
- HA Configuration: `EXP166 ARM Runtime DCM Surface`, `EXP166 STOP Runtime DCM Surface`.
- 180 s runtime window, no heat-pump/controller reboot.
- No AFCA strobe, setting write, master probe, scan or room-sensor emulation.
- Exact known 0x06 response only; strict known 0x0F ACK whitelist; exact A5 response only if natively requested.

Validity / success criteria:
- First verify `06tx > 0`; `EXP 0.0` on VERSION is corroborating evidence of the known 0x06 metadata path.
- Combined role is fully exercised only if both `06tx > 0` and `0FtxACK > 0` occur in the run.
- Primary positive result is spontaneous A5 and/or 0x0F FC03.

## 2026-09-25 — EXP166 — corrected runtime 0x06 + 0x0F hot-plug — COMPLETE / PARTIAL NEGATIVE, POSITIVE 0x06→EXP RESULT

**Hypothesis:** actually exercising the proven 0x06 REQ-low responder at runtime while the known 0x0F FC16 ACK role is available may activate native A5 and/or 0x0F FC03 without a controller reboot.

**Observed facts:** runtime-only, no controller reboot. The first 0x06 TX occurred ~3.3 s after ARM and the user observed `EXP 0.0` appear almost immediately. Final summary: `duration_ms=180018 frames=1444 s05=0 s06=169 s0F=0 A4=0 A5=0 06tx=169 0FtxACK=0 A5tx=0 0F03req=0 0F03rsp=0 0F16req=0 resyncDelta=0 dropDelta=0`. All 169 observed 0x06 transactions were answered. No 0x0F request occurred, so the 0x0F ACK role was not exercised. No A5, A4/05 or 0x0F FC03 appeared. Bus remained clean.

**Strong conclusions:** runtime 0x06 presence is sufficient for the UI `EXP 0.0` metadata to appear, but insufficient for DCM-like A5/0x0F service activation. `EXP 0.0` is therefore an accessory/version metadata indication, not proof of DCM binding. The intended simultaneous exercised 0x06+0x0F hypothesis remains technically uncompleted because no 0x0F traffic occurred during this run.

**Comparison with EXP165:** EXP165 exercised five 0x0F ACKs but accidentally sent zero 0x06 responses; EXP166 exercised 169 0x06 responses but saw zero 0x0F requests. Each surface alone is insufficient. Do not simply repeat either role or reboot the controller.

**Next:** offline differential analysis of the earliest genuine DCM-power-up sequence before defining EXP167. Do not emulate the unresolved A4 FC06 write or invent a new register write.

Classification: **COMPLETE / POSITIVE for 0x06→EXP UI mapping; NEGATIVE for 0x06-only DCM activation; INCOMPLETE for simultaneous exercised 0x06+0x0F activation.**


---

## EXP167 — Runtime 0x06 then native 0x0F ACK wait — COMPLETE / INCONCLUSIVE COMBINED TEST; STRONG NEGATIVE FOR 0x06-DRIVEN ACTIVATION

**Hypothesis:** after the proven `0x06` accessory-presence response is active, a naturally occurring controller-originated known `0x0F FC16` request that is ACKed may reproduce the missing runtime service transition and cause native A5 and/or `0x0F FC03`.

**Only experimental change from EXP166:**
- keep the proven exact 23-byte `0x06 FC17` responder active;
- do not ACK `0x0F` until `06tx > 0`;
- wait up to 600 s for a native known `0x0F FC16`;
- if it occurs, first ACK becomes T0 and observe 120 s;
- no controller/heat-pump reboot.

**Safety:** no AFCA strobe, semantic setting write, ESP-generated FC16, A5 master probe, broad scan, room-sensor emulation, A4/05 response or C8 response. DE LOW outside exact response windows.

**Observed facts:**
- ARM at 14:12:45; first successful `0x06` response at 14:12:46;
- terminal summary at 14:22:45.530;
- `duration_ms=600009`;
- `frames=4715`;
- `s05=0`;
- `s06=559`;
- `s0F=0`;
- `A4=0`;
- `A5=0`;
- `06tx=559`;
- `0FtxACK=0`;
- `A5tx=0`;
- `0F03req=0`;
- `0F03rsp=0`;
- `0F16req=0`;
- `resyncDelta=0`;
- `dropDelta=0`;
- firmware reason: `NO_NATIVE_0F_WITHIN_600S`;
- firmware classification: `INCONCLUSIVE_COMBINED_ROLE_NOT_EXERCISED_DE_LOW_IDLE`.

**Strong conclusions:**
1. Valid `0x06` accessory/version presence can be sustained for 600 s without inducing any native `0x0F` traffic.
2. It also does not induce A5, A4 or 0x05 scheduling.
3. EXP167 is technically inconclusive for the exact combined condition because `0F16req=0`, so no `0x0F` ACK was actually exercised.
4. EXP167 is nevertheless a strong negative result for the hypothesis that `0x06` presence itself causes or eventually unlocks native `0x0F`/A5 service.
5. Combined with EXP165 and EXP166, neither runtime `0x0F` ACK alone nor runtime `0x06` presence alone reproduces the genuine DCM service state.

**Comparison with genuine DCM power-up:** in `thermia_capture_20260925_090209.log`, `0x0F` is already ACK-capable at ~0.389 s and A5 starts at ~1.179 s while C8 continues in parallel. The no-DCM runtime emulation therefore lacks a prerequisite that exists essentially immediately in the real DCM topology.

**Negative result retained:** do not repeat longer 0x06-only dwell tests or treat `EXP 0.0` as evidence of DCM recognition.

**Next:** offline transmitter/ownership analysis of the first seconds of genuine DCM power-up before defining EXP168.


## EXP168 — Runtime 0x06 presence + manually triggered 03E8/count14 ACK — PREPARED

**Hypothesis:** a proven active `0x06` accessory-presence role plus an actually exercised runtime `0x0F FC16 0x03E8/count14` ACK may activate native A5 and/or `0x0F FC03`.

**Design:** arm at runtime; after >=10 valid `0x06` responses log READY; manually change only Heat Curve +1; ACK only exact `03E8/count14`; define that ACK as T0; observe 120 s. A5/A4/0x05 are passive. No controller reboot.

**Classification:** positive if spontaneous A5 and/or `0x0F FC03` appears after T0; valid negative if the exact ACK is exercised and neither appears during 120 s; inconclusive if no exact `03E8/count14` event is captured.


## EXP168 — Runtime 0x06 presence + manually triggered 03E8/count14 ACK — COMPLETE / VALID NEGATIVE

**Hypothesis:** a proven active `0x06` accessory-presence role plus an actually exercised runtime `0x0F FC16 0x03E8/count14` ACK may activate native A5 and/or `0x0F FC03`.

**Observed facts:**
- READY after 10 valid `0x06` responses.
- Manual Heat Curve +1 caused exact `0x0F FC16 03E8/count14`.
- First payload word: `36 (0x0024)`.
- One exact FC16 ACK was transmitted and defined T0.
- 120 s post-T0 observation completed.
- Final summary: `duration_ms=163187 frames=1308 s05=0 s06=155 s0F=1 A4=0 A5=0 06tx=155 0FtxACK=1 A5tx=0 0F03req=0 0F03rsp=0 0F16req=1 firstAckRelMs=43163 resyncDelta=0 dropDelta=0 COMBINED_06_PLUS_03E8_ACK_EXERCISED_DE_LOW_IDLE`.

**Result:** VALID NEGATIVE.

**Strong conclusion:** simultaneous proven runtime `0x06` presence and a deliberately exercised known controller-originated `0x0F FC16` ACK do not activate A5, A4/0x05, or `0x0F FC03`. This closes the exact combined-role gap left open by EXP167.

**Comparison:**
- EXP165: runtime `0x0F` ACK role alone -> no A5/0F03.
- EXP166/167: valid runtime `0x06` presence -> no A5/0F03; EXP167 sustained 600 s with zero native 0x0F.
- EXP168: valid `0x06` + exercised `0x0F 03E8/14` ACK -> still no A5/0F03.

**Negative result retained:** stop repeating simple `0x06` + `0x0F` transport-role combinations.

**Next:** offline analysis of genuine DCM transmitter ownership / service activation before EXP169. No controller reboot required.


### EXP170 — Heat Curve sync to 042E ACK -> A5 watch — COMPLETE / INCONCLUSIVE

Hypothesis:
Advance the proven native 0x0F synchronization path `03E8/14 -> 0410/22 -> 042E/15`, then observe whether ACK of `042E/15` activates A5.

Observed:
- runtime/no-reboot ARM successful;
- controller was already repeatedly sending `0x04A6/count13` before the manual Heat Curve change; these were intentionally not ACKed;
- Heat Curve +1 produced `0x03E8/count14`, first word `37 / 0x0025`;
- ESP ACKed `03E8/14` once;
- expected `0410/22` never appeared;
- controller continued repeating the pre-existing `04A6/13`;
- phase-1 timeout after 15 s; final: `ackTx=1 ack03E8=1 ack0410=0 ack042E=0 0F16req=48 resyncDelta=0 dropDelta=0`.

Result: INCONCLUSIVE — intended chain not reached.

Strong conclusion:
A new `03E8/14` parameter-change event does not necessarily restart/override an already-pending 0x0F block. The controller's native 0x0F synchronization is stateful and current pending-block context matters.

Negative result retained:
Do not repeat EXP170 unchanged from arbitrary runtime state. First understand/clear the pending `04A6/13` state offline or via a specifically justified experiment.


### EXP172 — passive controller scheduler fingerprint — COMPLETE

Hypothesis:
A controller-side scheduler-enable state may be visible in ordinary `0x02` / `0x04` FC17 traffic.

Observed:
- 180002 ms passive-only;
- frames=1456;
- s02=336, s04=0, s05=0, s06=42, s0F=168, A4=0, A5=0, C8=0;
- 0F03req=0, 0F03rsp=0, 0F16req=168;
- resyncDelta=0, dropDelta=0;
- all visible FC16 traffic was repeated `04A6/count13`;
- local controller request fingerprint repeated as `0217A7F8000FA80C00070E004000000000000A000AFFFF0000...`, i.e. read count 15 and `A80C..A812 = 64,0,0,10,10,65535,0`.

Comparison with scheduler-enabled pre-DCM `090550`:
- `A7F8` read count is 13;
- `A80C..A812 = 64,0,0,10,10,12,0x0500`;
- A5 and `0x0F FC03 0708/6` already run before DCM response.

Conclusion:
There is a stable controller-side structural/state difference. `A811/A812` (`FFFF/0000` local versus `000C/0500` scheduler-enabled) and the read-span difference (15 versus 13) are now the highest-value correlation markers. They are not yet proven controls and must not be written blindly.

Status: COMPLETE.


### EXP173 — 0x06 presence vs A811/A812 — COMPLETE / VALID NEGATIVE

Hypothesis:
The local-vs-reference difference in `A811/A812` and A7F8 read-count may be caused by current accessory presence.

Result:
- baseline: read-count 15, A811=FFFF, A812=0000;
- 56 exact known `0x06` REQ-low responses during 60 s active phase;
- no change in read-count, A811, or A812;
- 180 s passive recovery also unchanged;
- A5=0, A4=0, 0x05=0, 0F03req=0;
- parser and RX-drop deltas both 0.

Conclusion:
Simple `0x06` accessory presence does not explain or activate the scheduler-enabled controller state. The discriminator now points more strongly to persistent controller configuration / firmware / commissioning state.

Status: COMPLETE / VALID NEGATIVE.


### EXP174 — COMPLETE / VALID NEGATIVE

Across a real Heat Curve `36 -> 37 -> 36` cycle, A7F8 read-count stayed 15 and A811/A812 stayed FFFF/0000. No A5/A4/0x05/0x0F FC03 appeared. Record as negative for ordinary fingerprint mutability, not as proof of scheduler causality.

### EXP175 — passive topology fingerprint — COMPLETE

Hypothesis:
Scheduler-enabled external captures may reflect a different/broader bus topology rather than a directly reproducible scheduler state on the local XTR M.

Result:
`duration_ms=180009 frames=1457 s02=336 s04=0 s1E=670 s05=0 s06=42 s0F=168 A4=0 A5=0 C8=0 0F03req=0 0F03rsp=0 0F16req=168 lastReadCount=15 lastA811=FFFF lastA812=0000 resyncDelta=0 dropDelta=0`

Observed:
- local slave 0x1E was highly active with repeated FC16 and FC04 request/response cycles;
- no slave 0x04 frame occurred in the full 180 s;
- no A5, A4, 0x05, C8 or 0x0F FC03 scheduler traffic occurred;
- controller fingerprint remained FFFF/0000, read-count 15;
- passive capture was clean with zero parser resync/drop delta.

Conclusion:
Valid passive topology discriminator. The local XTR M bus topology differs materially from the scheduler-enabled reference captures. Do not assume the external 0x04/A5/0x0F FC03 scheduler can be transplanted one-for-one to local XTR M.

Negative result:
No evidence that a hidden local 0x04 or scheduler family spontaneously appears under ordinary runtime conditions.


### EXP176 — offline reconstruction around 0x0559 — COMPLETE / NEGATIVE

Hypothesis:
The scheduler-enabled reference may carry `0x0559 Link Integration = 1`, explaining scheduler activation.

Observed:
- external FC16 block `0x0546/count20` spans `0x0546..0x0559`;
- its last word, address `0x0559`, is `0x0000`;
- next FC16 block starts at `0x055A`;
- identical structure is present in both scheduler-enabled external captures.

Conclusion:
Scheduler-enabled operation is observed while 0x0559 is zero. `0x0559=1` is not a required scheduler-enable condition in the reference topology. Do not proceed to a 0x0559 write test from this hypothesis.

## 2026-09-26 — EXP218 COMPLETE / MAJOR POSITIVE — local 0x0553 Operation Mode validation

Hypothesis:
Local XTR M uses the same `0x0F FC16 0546/count20` system-page family as the genuine DCM reference, with `0x0553` carrying Operation Mode.

Observed:
- Controlled physical `AUTO -> COMPRESSOR -> AUTO` produced local `0x0553: 1 -> 2 -> 1`.
- `0x0559` remained `0`.
- Repeated controller-originated `0546/count20` frames updated in-flight when the physical mode was restored.

Conclusion:
`0x0553` is project-proven Operation Mode on this XTR for at least `1=AUTO`, `2=COMPRESSOR`.


## 2026-09-26 — EXP219 COMPLETE / MAJOR POSITIVE — local full 0546/count20 page

Hypothesis:
Capture the complete local `0546/count20` page and compare it with the genuine DCM reference.

Observed:
- 12/12 local pages were byte-for-byte identical:
  `[1,1,2,0,2,0,0,0,0,3,0,0,0,1,0,0,0,0,0,0]`.
- Stable local/reference differences exist at `0546`, `0547`, `054A`, `054F`, and the expected operational difference at `0553`.
- `0559=0` in both local and genuine reference.

Conclusion:
`0546`, `0547`, `054A`, and `054F` are stable structural/configuration/topology candidates; semantics remain unknown.


## 2026-09-26 — EXP220 COMPLETE / POSITIVE — Operation Mode independence of 0546/0547/054A/054F

Hypothesis:
During physical `AUTO -> COMPRESSOR -> AUTO`, the four EXP219 candidates remain stable while `0553` changes `1 -> 2 -> 1`.

Observed:
- `0546=1`, `0547=1`, `054A=2`, `054F=3`, `0559=0` remained unchanged.
- Only `0553` changed reversibly `1 -> 2 -> 1`.
- End counts: total 195 full pages; baseline 41, compressor 49, restored 105.

Conclusion:
The four EXP219 candidates are not simple Operation Mode mirrors and remain stronger structural/configuration/topology candidates.


## 2026-09-26 — EXP221 COMPLETE / STRONG NEGATIVE — local cold-boot scheduler activation

Hypothesis:
A true local cold boot without DCM might spontaneously create the extended Online/DCM scheduler.

Observed:
- ~200 s post-power-on capture.
- End summary: `A5=0`, `A4=0`, `S04=0`, `S05=0`, `0F03=0`, `0708=0`, `S06=61`, parser resync delta 1, RX drops 0.
- Native local `0x0F` traffic resumed rapidly after boot, including `04BA/count22`, `04A6/count13`, `085F/count5`, and FC17 `0730/count8`.
- EXP221's original `runtime/topology hit` counter incorrectly counted `085F`; this is corrected conceptually: lone `085F` does not prove the genuine scheduler.

Conclusion:
The local no-DCM controller does not spontaneously create A5/A4/0x04/0x05 + FC03/0708 scheduler topology during a normal cold boot, despite native `0x0F` serializer/runtime traffic being present.


## 2026-09-26 — EXP222 PREPARED — bounded cold-boot FC16 ACK completion test

Hypothesis:
The genuine DCM scheduler may start only after the controller completes its long initial slave-0x0F FC16 state/snapshot synchronization with valid FC16 ACKs.

Evidence motivating test:
- Genuine startup capture shows a long ACKed FC16 initialization sequence through `06F4/count19` and `085F/count5`.
- First observed `0x0F FC03 0708/count6` follows a few seconds later; cyclic runtime exporter starts at `07D0/count19`.
- Earlier local ACK experiments advanced individual FC16 stages but did not reproduce the entire genuine startup synchronization in one cold-boot run.
- A4/0x05 burst observed in another genuine capture occurs after 0708 is already active, so that burst is not the primary scheduler-start trigger.

Experimental variable:
During one controlled cold boot only, ACK CRC-valid slave-0x0F FC16 requests whose exact start/count shape is in the fixed local/genuine allow-list.

Safety:
- FC16 echo ACK only.
- No desired-state payloads.
- No FC03 responses.
- First FC03 or 07D0 runtime-start frame disables TX immediately.
- Unknown FC16 shape, parser resync, or RX-buffer fault disables TX immediately.
- No room-sensor emulation.

Status:
**PREPARED / NOT YET RUN.**



---
## EXP222 — Cold-boot 0x0F FC16 ACK completion probe — COMPLETE / IMPORTANT NEGATIVE

**Hypothesis**
ACKing only known controller-originated `0x0F FC16` state writes from before/through a controlled Thermia cold boot may be enough to create the Online/DCM read-side scheduler (`0x0F FC03 0708/count6`) and runtime exporter.

**Observed facts**
- Thermia power OFF was marked; ESP stayed powered. ACK mode was enabled before Thermia power ON.
- First acknowledged request after boot: `04BA/count22` at ~9.37 s post-on.
- ACK sequence actually observed: `04BA/22`, `05FF/33`, `04A6/13`, `085F/5`, `0662/33`, `04A6/13`. Total ACKs: 6.
- Total `0x0F FC16` requests counted: 72 (includes pre-test/pending repeats); no unknown target was seen.
- After the six ACKs, no further FC16 progression toward FC03 occurred.
- `FC03=0`, `0708=0`, `07D0=0`, `A5=0`, `A4=0`, `S04=0`, `S05=0` at END.
- Normal `0x06` polls and `0x0F FC17 0730/count8` remained present.
- Clean transport: `resyncDelta=0`, `dropDelta=0`.

**Strong conclusions**
- The tested ACK-only `0x0F` responder does not activate the extended scheduler.
- Local FC16 completion and extended A5/FC03 topology are separate conditions.
- This reproduces the earlier post-`0662` quiet behavior in a controlled cold-boot context.

**Hypotheses**
- Extended topology probably depends on persistent accessory/service binding, commissioning/configuration state, firmware/model capability, or an earlier non-0x0F service-discovery path.
- A5 is more likely a prerequisite/parallel service context than a consequence of FC16 ACK completion.

**Unknowns / limits**
- The local boot did not emit the genuine module's whole FC16 startup dump, so EXP222 does not test ACKing every genuine page.
- Exact trigger that enables A5 remains unknown.

**Negative result recorded**
ACKing the locally offered known FC16 boot/state pages is not sufficient to start `0x0F FC03 0708` or the runtime exporter.


---
## EXP223 — Offline XTR-native 0x0F FC17 071C/0730 discriminator — COMPLETE / POSITIVE

**Hypothesis**
The recurring local slave-0x0F FC17 transaction may be an XTR-native Online/DCM keepalive/session/mailbox surface that is distinct from the ATEC/DCM FC03/FC16+A5 scheduler family.

**Observed facts**
- Exact local request contract: read `0x0730/count8`, write `0x071C/count8`, bytecount 16.
- EXP221 contained 47 exact requests; EXP222 contained 25, for 72 analysed local frames.
- No response was present locally, consistent with no DCM/Online endpoint attached.
- In all 72 frames:
  - 071C=`1A16`, 071E=`F906`, 0720=`DC1A`, 0722=`001E` stayed fixed;
  - 0723=`2*071D+0500` modulo 16 bits;
  - low byte of 071F=`AC`, and high byte of 071F=`floor(low_byte(071D)/4)`.
- 0721 changes much more slowly, approximately once per minute-scale interval.
- None of the three available genuine ATEC/DCM captures (`071517`, `090209`, `090550`) contains slave-0x0F FC17 traffic. Those captures instead show the ATEC `0x04`+A5+`0x0F FC03/FC16` topology.
- Local XTR passive topology already established in EXP175 is the inverse at this layer: active slave `0x1E`, no slave `0x04`, no A5.

**Strong conclusions**
1. The ATEC/DCM scheduler topology must not be assumed to be a one-for-one transport template for XTR.
2. The local `071C/0730` FC17 exchange is a higher-value XTR-specific target for passive characterization than another A5/FC03 injection.
3. The deterministic write-side relations argue against interpreting the 071C block as eight independent ordinary setting values.

**Hypotheses**
- `071C..0723` may be a heartbeat/challenge/session image supplied by the XTR controller to an external slave-0x0F service.
- `0730..0737` may be the corresponding external response/status/command image.
- A genuine XTR/iTec/DHP-AQ Online module capture is still required to know the correct response semantics.

**Unknowns**
- Exact meaning of all sixteen request bytes.
- Whether a genuine DCM answers this FC17 request on XTR-family systems.
- Whether any controller semantic state changes the 071C write image beyond its deterministic timing/counter evolution.
- Meaning and safety of the 0730 read-side values.

**Negative result recorded**
No response value is inferred or guessed from the request structure. Do not emulate `0730` yet.

---
## EXP224 — Passive 071C/0730 Heat Curve A/B/A correlation — COMPLETE / INCONCLUSIVE TARGET NOT EXERCISED

**Hypothesis**
If the XTR FC17 071C write image includes semantic controller state, a known Heat Curve `baseline -> +1 -> baseline` change should produce a phase-correlated reversible change beyond the already observed deterministic counter/timer relations.

**Observed facts**
- ESP was RX-only; no experimental TX, ACK, FC17 response, scan or semantic write.
- The experiment ran from the explicit START marker to END with clean parser/resource diagnostics.
- Native `03E8/count14` ground-truth frames clearly exercised the semantic change: Heat Curve was observed at 37 during the +1 phase and 36 after restore.
- 96 `03E8` ground-truth frames were logged.
- Exact target FC17 count at END: `total=0 baseline=0 plus=0 restored=0`.
- RX buffer drops remained 0 and parser resyncs remained 0.

**Strong conclusions**
1. EXP224 is not a valid negative for Heat-Curve influence on the 071C write image because the target FC17 transaction never occurred.
2. The 071C/0730 FC17 family is not continuously present in ordinary steady runtime.
3. Combined with EXP221, where it appeared from ~2.9 s after controller power-on and continued throughout the ~200 s cold-boot observation, the FC17 family is strongly gated by controller boot/recovery/service-session state.

**Hypotheses**
- `071C/0730` may be a cold-boot/recovery session establishment or challenge exchange toward the absent slave-0x0F endpoint.
- It may be more relevant to XTR Online/DCM startup than the ATEC-specific A5/FC03 topology.

**Unknowns**
- Whether Heat Curve or any semantic setting modifies the 071C image while the cold-boot FC17 stream is active.
- Exact semantics of `071C..0723` and `0730..0737`.
- Whether a genuine XTR-family DCM responds to this FC17 request and what response transformation is required.

**Negative result recorded**
Do not treat EXP224 as evidence that Heat Curve has no effect on 071C; the target was absent.

---
## EXP225 — Passive cold-boot-gated 071C/0730 Heat Curve A/B/A correlation — PREPARED

**Hypothesis**
The local XTR 071C/0730 FC17 stream is a controller-cold-boot/recovery exchange. Once that stream is re-established, a Heat Curve `baseline -> +1 -> baseline` A/B/A can determine whether the controller-written 071C image carries semantic state or only session/timing/challenge data.

**Required setup condition**
ESP stays independently powered and armed while the Thermia/controller is power-cycled normally. No setting is changed until at least three exact target FC17 frames have been observed.

**Only experimental variable after FC17 READY**
Physical Heat Curve on the Thermia display: baseline -> baseline+1 -> exact baseline. No other setting changes.
**Instrumentation**
- exact target FC17 matcher: slave0F FC17 read `0730/count8`, write `071C/count8`;
- logs all eight write words and validates the known deterministic 0723/071F relations;
- records first/last post-power-on FC17 timing and per-phase counts;
- native `03E8/count14` Heat Curve frame remains the semantic ground truth;
- Home Assistant controls remain Configuration-category markers only.

**Safety**
Strict RX-only. No `tx_pin`, FC17 reply, FC16 ACK, probe, scan, semantic write, or room-sensor emulation.

**Status**
PREPARED / NOT YET RUN.

---
## EXP225 — Passive cold-boot-gated 071C/0730 Heat Curve A/B/A — COMPLETE / PROCEDURAL-INCONCLUSIVE

**Hypothesis**
The local XTR 071C/0730 FC17 stream is a controller-cold-boot/recovery exchange. Once active, a Heat Curve `baseline -> +1 -> baseline` A/B/A can test whether the controller-written `071C..0723` image carries semantic setting state or only session/timing/challenge data.

**Observed facts**
- ESP remained RX-only; no FC17 response, ACK, probe, scan or semantic write.
- A real Thermia/controller power-off interval was observed: valid bus traffic stopped and `Bus Healthy` went OFF, then bus traffic recovered.
- The exact target FC17 stream reappeared after bus recovery and 32 exact frames were captured.
- The first 13 target frames occurred before the manually pressed Power ON marker; consequently their `post_on` field remained 0.
- The Power ON marker was pressed late and reset `exp225_phase` to 1 after the target stream was already active.
- Native `03E8` ground truth shows Heat Curve `36 -> 37` at 23:52:38.785 and `37 -> 36` at 23:53:17.395.
- No valid `Mark Heat Curve +1` phase was recorded; final counters were `total=32 baseline=32 plus=0 restored=0`.
- The restore marker was explicitly refused because the firmware had not recorded a +1 phase.
- All 32 captured FC17 images satisfy `rel0723=YES` and `rel071F=YES`.
- The static words remained `071C=1A17`, `071E=F906`, `0720=DC1A`, `0722=001E`; the other words progressed in the same deterministic counter/timing pattern.
- Parser resyncs and RX buffer drops remained 0.

**Strong conclusions**
1. EXP225 successfully reproduces the cold-boot-gated 071C/0730 stream, independently confirming EXP221/224's cold-boot/recovery association.
2. EXP225 is **not** a valid negative for Heat-Curve influence because the user phase markers were not executed in the required order and the late Power ON marker reset the phase state.
3. The write image continues to look strongly structured/counter-like; no obvious Heat-Curve-correlated discontinuity is visible in the raw sequence, but that observation is only supportive, not conclusive.

**Hypotheses**
- `071C..0723` is primarily a timed/session/challenge structure rather than a direct scalar settings block.
- Any semantic input, if present, may be encoded in a response at `0730..0737`, in a subtler transformation, or in another session layer.

**Unknowns**
- Whether a correctly phased Heat Curve A/B/A causes any reproducible change in `071C..0723`.
- Exact semantics of `071C..0723` and all `0730..0737` response words.
- Whether a genuine XTR-family Online/DCM device responds to this FC17 transaction.

**Recorded result**
Procedural/inconclusive for semantic correlation; positive reproduction of the cold-boot FC17 stream. Do not infer response values and do not proceed to a responder test yet.

---
## EXP226 — Offline 071C..0723 generator/calendar analysis — COMPLETE / POSITIVE

**Hypothesis**
The dynamic words in the XTR-native `0x0F FC17 read 0730/count8 + write 071C/count8` image are primarily derived from time/counter/session state rather than ordinary heat-pump settings.

**Method**
Offline only. No ESP/heat-pump action, no restart, no TX and no setting change.
Analysed 129 already-recorded exact target requests:
- EXP221: 47
- EXP222: 25
- EXP225: 32
- older 2026-09-22 EXP71/EXP71B captures: 25

The older September 22 frames were deliberately included as out-of-sample date/time validation rather than deriving the mapping only from the September 26 experiments.

**Observed facts**
Across all 129 frames:
- `071E=F906` in 129/129;
- `0722=001E` in 129/129;
- high byte of `071D=45` in 129/129;
- high byte of `0720=DC` in 129/129;
- high byte of `0721=C5` in 129/129;
- high byte of `0723=8F` in 129/129;
- low byte of `071D` was always even;
- low byte of `0721` and `0723` was always divisible by 4;
- the earlier `071F` and `0723` algebraic relations held in 129/129.

Cross-date/time decoding:
- `071C high byte = year-2000`; all frames carry `1A` = 26.
- `071C low byte = hour`: Sep22 14h -> `0E`; Sep26 22h -> `16`; Sep26 23h -> `17`.
- `0720 low byte = day-of-month`: Sep22 -> `16` hex (=22); Sep26 -> `1A` hex (=26).
- `071D low byte = 2*second`.
- `071F high byte = floor(second/2)`, low byte fixed `AC`.
- `0721 low byte = 4*minute`.
- `0723 low byte = 4*second`.

Reconstructed controller time from `071C/0721/071D` is consistently ahead of the ESP/log clock:
- Sep22 EXP71: mean +200.94 s;
- Sep22 EXP71B: mean +200.99 s;
- Sep26 EXP221: mean +206.37 s;
- Sep26 EXP222: mean +206.32 s;
- Sep26 EXP225: mean +206.37 s.
Within-run scatter is roughly sub-second, strongly supporting the RTC interpretation rather than a coincidental counter fit.

**Strong conclusions**
1. EXP226 materially refines EXP223: `071C..0723` is not merely "counter/timing-like"; most of its changing content is a transformed calendar/clock image.
2. The previous fixed/dynamic observations now have concrete explanations:
   - `071C 1A16 -> 1A17` = hour 22 -> 23;
   - `0721` slow changes = minute * 4;
   - `071D`, `071F`, `0723` are redundant second representations.
3. The observed dynamic write image is not a direct Heat Curve/settings image. This substantially lowers the value of another Heat-Curve correlation run against 071C..0723.
4. The return bank `0730..0737` remains unknown; nothing in this analysis justifies responding with zeros, echoes or a guessed inverse transform.

**Hypotheses**
- `0722=001E` may encode calendar metadata such as days-in-month (September has 30 days), but this is unproven because every available validating raw capture is from September.
- `071E=F906` and the fixed high/magic bytes may encode month/calendar format/check metadata.
- The FC17 transaction may be a time/date synchronization, validation or challenge surface toward an external service endpoint, but the purpose and response semantics are still unknown.

**Unknowns**
- Exact semantics of `071E`, `0722`, and the fixed high bytes.
- Where/how month is encoded.
- Meaning and required values of `0730..0737`.
- Whether a genuine XTR Online/DCM endpoint transforms, validates or simply consumes this time image.

**Safety / negative result**
No response is inferred. No active responder test is justified from EXP226 alone. Heat-pump restarts are explicitly paused for subsequent work.

**Next**
EXP227 should remain offline and compare local XTR transport/block topology with the genuine ATEC/DCM captures, using this newly identified RTC image to avoid misclassifying time-derived traffic as semantic settings.



---
## EXP227 — Offline XTR vs genuine ATEC/DCM architecture comparison — COMPLETE / POSITIVE HOMOLOGY

**Hypothesis**
The local XTR and genuine ATEC/DCM systems may differ mainly in outer scheduler/topology while retaining a homologous native slave-`0x0F` page/register serializer. If so, locally proven XTR sync pages should align by start address/order with genuine ATEC/DCM full-sync pages even when page selection/counts and service scheduling differ.

**Method**
Offline only. No restart, no ESP TX, no setting change.

Compared:
- genuine DCM/Online captures `210001`, `071517`, `090209`, `090550`;
- local XTR raw EXP221/222 traffic;
- locally proven XTR ACK-walk sequence from EXP137–142;
- EXP175/182 topology and scheduler findings;
- EXP226 RTC decode to exclude time-derived `071C/0730` from semantic-setting comparisons.

**Observed facts**

Local proven ACK-walk:
`03E8/14 -> 0410/22 -> 042E/15 -> 04A6/13 -> 04BA/22 -> 05FF/33 -> 0662/33`

Genuine ATEC/DCM full sync contains the same seven start addresses in the same relative order:
- `03E8/13` — same start, XTR has one extra word;
- `0410/21` — same start, XTR has one extra word;
- `042E/15` — exact shape match;
- `04A6/13` — exact;
- `04BA/22` — exact;
- `05FF/33` — exact;
- `0662/33` — exact.

Additional recurrent common shapes:
- `0546/20` exact;
- `085F/5` exact.

Selected payload comparison using exact shared shapes:
- `04BA/22`: 20 of 22 words equal between compared XTR and ATEC frames; differences only at word0 (`0014` vs `0013`) and word6 (`0028` vs `001E`);
- `05FF/33`: 31/33 words equal;
- `0662/33`: 31/33 equal;
- `085F/5`: 5/5 equal (all zero);
- `0546/20`: 15/20 equal in the compared states;
- `04A6/13`: same shape but strongly different payload, consistent with state/model-specific page content.

Genuine ATEC/DCM full sync includes many intermediate pages absent from the local XTR ACK-walk, including `03FC`, `0442`, `0456`, `046A`, `047E`, `0492`, `04D8`, `04F6`, `050A`, `051E`, `0532`, `055A` and multiple `33`-word pages through the `06xx` range.

The outer topology remains different:
- local XTR: active slave `0x1E`; no `0x04`, A5, or local `0x0F FC03/0708` service scheduler;
- genuine ATEC/DCM: active slave `0x04`, A5 service traffic, `0x0F FC03 0708/count6`, and cyclic runtime `07D0..0884`.
- reference 0x04 recurrent wire contract is FC17 `ABE0/12 -> ABF4/4`;
- local 0x1E recurrent wire contract is FC16 `0000/9`, `0014/3` plus FC04 `0000/22`, `001E/6`.

Across all four genuine DCM captures:
- exact `0x06 FC17 read AFC8/count12, write AFDC/count5` polls: 69;
- slave-0x06 responses: 0.
The Online/DCM service is nevertheless active through A5/`0x0F`.

DCM-rejoin capture `090550`:
- A5 active from ~0.526 s;
- first `0708/count6` poll at ~0.987 s;
- first successful `0x0F FC16` ACK only at 66.860 s;
- first `0708` DCM response at 68.235 s;
- 16 earlier `0708` polls were unanswered.
Thus controller-side extended scheduling exists before the DCM `0x0F` endpoint is ready.

**Strong conclusions**
1. EXP175 is refined: XTR and ATEC/DCM are not the same *outer bus topology*, but they are not unrelated protocol families. Their native `0x0F` page/register serialization is substantially homologous.
2. All seven locally proven XTR ACK-walk stage addresses map into the genuine ATEC/DCM full-sync sequence in the same relative order. Five match exact start/count; the first two use the same start with XTR count = ATEC count + 1.
3. The high word-for-word similarity in several exact shared pages strongly supports common page schemas with model/state-specific values.
4. The main missing local feature is the extended Online/DCM runtime service subsystem (`A5 + 0708 + 07D0..0884`), not basic `0x0F` register serialization.
5. `0x06` should not be pursued as the Online/DCM endpoint on the basis of the genuine ATEC captures; it remains a parallel expansion/accessory path.
6. Reference slave `0x04` and local slave `0x1E` are not wire-compatible renumberings; any functional equivalence would be at a higher architectural level.
7. EXP226's `071C/0730` RTC exchange is not the XTR equivalent of the ATEC `0708` mailbox merely by address proximity.

**Hypotheses**
- The shared `0x0F` serializer has model/firmware/capability-dependent page selection, explaining the sparse XTR sync path versus broad ATEC full sync.
- Extended scheduler activation may depend on commissioning/binding/platform capability or another service-discovery state outside the ordinary `0x0F` page ACK chain.
- Some fixed differences inside homologous shared pages may expose model/service capability fields and are suitable for the next offline discriminator study.

**Unknowns**
- Whether this XTR firmware can ever enable the A5/0708/07D0 service subsystem without genuine Online/DCM commissioning.
- Which exact field(s), if any, encode that capability/binding.
- Whether slave 0x04 and local 0x1E are functionally analogous at a higher layer.
- Semantics of the XTR `0730..0737` return bank.
- Exact reason for the +1 page-length differences at `03E8` and `0410`.

**Negative/safety result**
No active write or responder follows from EXP227. No guessed `0708`, `0730`, A811/A812, or runtime-page injection is justified. Heat-pump restarts remain paused.

**Next**
Prefer EXP228 offline: build a field-level homology/difference map for shared pages (`04BA`, `0546`, `05FF`, `0662`, `085F`, plus the near-matching `03E8`/`0410`) and rank only persistent cross-system discriminator fields for further passive validation.


---
## EXP228 — Offline shared-page field discriminator map — COMPLETE / POSITIVE

**Hypothesis**
Persistent word-level differences inside the homologous native `0x0F` pages shared by local XTR and genuine ATEC/DCM systems may expose model/platform/capability fields. Values that vary within one platform should be rejected as fixed capability discriminators.

**Method**
Offline only: no restart, no ESP TX and no Thermia setting change. Exact FC16 payloads were parsed and compared from local XTR EXP221/222/141 and genuine ATEC/DCM `090209`/`090550`. Prior local Operation-Mode evidence was used to exclude the already-semantic `0553` field.

Page-level replication used for the discriminator test:
- `04BA/count22`: XTR 5 identical frames; ATEC 2 identical full-sync frames.
- `0546/count20`: XTR 55 identical EXP221 frames; ATEC 2 identical full-sync frames; earlier local A/B/A proves only `0553` changes with Operation Mode.
- `05FF/count33`: XTR 30 identical EXP141 frames plus one identical EXP222 frame; ATEC 2 identical frames.
- `0662/count33`: XTR 267 identical EXP141 frames plus one identical EXP222 frame; ATEC 2 identical frames.
- `085F/count5`: XTR 115 compared frames from EXP221/222 and ATEC 10 frames from `090209/090550`; all payloads all-zero.
- `04A6/count13`: 223 local XTR frames showed multiple payload variants, so it was treated as state-dependent rather than a fixed discriminator.

**Observed facts**
Stable differences in exact shared pages:

| Register | XTR | genuine ATEC/DCM | status |
|---|---:|---:|---|
| `04BA` | `0014` | `0013` | persistent candidate |
| `04C0` | `0028` | `001E` | persistent candidate |
| `0546` | `0001` | `0002` | persistent candidate |
| `0547` | `0001` | `0000` | persistent candidate |
| `054A` | `0002` | `0000` | persistent candidate |
| `054F` | `0003` | `0000` | persistent candidate |
| `0553` | `0001` in compared local frame | `0004` | excluded: known Operation Mode |
| `061C` | `0003` | `0000` | persistent candidate |
| `061E` | `0001` | `0000` | persistent candidate |
| `067E` | `0003` | `0000` | persistent candidate |
| `067F` | `0001` | `0000` | persistent candidate |

Exact page-difference counts:
- `04BA/22`: only 2 of 22 words differ (`04BA`, `04C0`).
- `05FF/33`: only 2 of 33 differ (`061C`, `061E`).
- `0662/33`: only 2 of 33 differ (`067E`, `067F`).
- `0546/20`: 5 of 20 differ in the compared frames; one of those is known runtime-semantic `0553`, leaving four stronger structural candidates.
- `085F/5`: 0 of 5 differ; explicit negative result.

`04A6/13` is not stable locally. EXP221 uses an image dominated by zeros with `04B0=4020`; EXP222 additionally shows `04A6=0042`, `04A7=0001`, and one observed `04B0=4000`. The genuine ATEC image is stable but very different. Therefore this page is unsuitable as a fixed scheduler/capability fingerprint without semantic decomposition.

Structural differences retained from EXP227:
- XTR `03E8/count14` versus ATEC `03E8/count13`;
- XTR `0410/count22` versus ATEC `0410/count21`.
These are schema/page-length discriminators only.

**Strong conclusions**
1. The cross-platform homology from EXP227 can now be narrowed to a small, reproducible set of word-level differences rather than broad page mismatch.
2. `0546`, `0547`, `054A`, `054F`, `04BA`, `04C0`, `061C`, `061E`, `067E`, and `067F` are the best current passive discriminator candidates.
3. `0553` must be excluded from that list because it is already proven to encode Operation Mode locally.
4. `04A6` is state-dependent locally and should not be used as a fixed model/Online fingerprint.
5. `085F` is shared all-zero state in the compared systems and provides no platform discrimination.
6. No field is proven to *cause* the Online/DCM scheduler. Cross-system persistence supports model/config/capability association only.

**Hypotheses**
- The `0546/0547/054A/054F` group may be system/model/hardware configuration metadata.
- The XTR-specific `061C/061E` and `067E/067F` values may belong to a repeated table/capability structure in the 33-word `05xx/06xx` family.
- Their location near points where XTR skips ATEC pages (`0620`, `0641`, then post-`0662` pages) makes a page-selection/capability relationship worth testing offline, but this is not yet causal evidence.
- The +1 page lengths at `03E8` and `0410` may represent XTR schema extensions.

**Unknowns**
- Semantic names for the new discriminator registers.
- Whether any candidate is configurable or firmware-fixed.
- Whether any candidate participates directly in scheduler/binding enablement.
- Whether the 33-word family encodes repeated hardware/module tables, feature groups or another structure.

**Negative / safety result**
No active write target emerges from EXP228. Do not write the discriminator candidates to reference ATEC values. Heat-pump restarts remain paused.

**Next**
EXP229 should remain offline and analyse the entire 33-word page family `055A..06C5`, including the pages present on ATEC but skipped by XTR, to test whether the candidate tail words form a coherent table/capability/page-selection structure.

---
## EXP229 — Offline 33-word family / 12-word structure analysis — COMPLETE / POSITIVE

**Hypothesis**
The contiguous `055A..06C5` count-33 family is a coherent table/descriptor structure. The XTR-only values `061C/061E` and `067E/067F` may be structural fields associated with model-dependent page selection rather than ordinary runtime state.

**Method**
Offline only. Parsed existing genuine ATEC/DCM full-sync captures `090209` and `090550`, plus local XTR EXP141 and EXP222 payloads. No heat-pump restart, no ESP TX and no setting change.

The ATEC full-sync contains twelve consecutive FC16 `count33` pages:
`055A, 057B, 059C, 05BD, 05DE, 05FF, 0620, 0641, 0662, 0683, 06A4, 06C5`.

**Observed facts**
1. Every page start advances by exactly `0x21` (=33) words. The twelve pages therefore form one contiguous 396-word image covering `055A..06E5`.
2. `090209` and `090550` are bit-for-bit identical across all 396 words in this family.
3. The concatenated image has strong periodicity at 12 words:
   - `315/384 = 82.0%` of values equal the value 12 words later;
   - 396 words = `33 * 12`, allowing a natural candidate decomposition into 33 records of 12 words.
4. Exact 12-word template repetitions include:
   - records `9..15`: seven identical records;
   - records `17..23`: seven identical records;
   - records `29..31`: three identical records;
   - records `6..7`: two identical records.
5. Local XTR `05FF/count33`:
   - 31 observed frames across EXP141+EXP222;
   - one unique payload;
   - differs from ATEC only at `061C=0003` (ATEC `0000`) and `061E=0001` (ATEC `0000`).
   - In the 12-word decomposition these are record 16 fields 2 and 4, directly after the seven-record repeated run `9..15`.
6. Local XTR `0662/count33`:
   - 268 observed frames across EXP141+EXP222;
   - one unique payload;
   - differs from ATEC only at `067E=0003` (ATEC `0000`) and `067F=0001` (ATEC `0000`).
   - These fall in record 24 fields 4 and 5, directly after the seven-record repeated run `17..23`.
7. The ATEC reference image contains zero occurrences of value `0003` across all 396 words. It contains multiple `0001` values. Therefore the XTR `0003` values are the more distinctive cross-platform markers.
8. Local transport page selection differs:
   - ATEC: `05FF -> 0620 -> 0641 -> 0662`;
   - XTR acknowledged sequence: `05FF -> 0662`.
   The XTR jump is three page strides (`3 * 0x21`), numerically matching `061C=3`.
9. A second numerical correlation exists: `0662 + 3 * 0x21 = 06C5`, while XTR `067E=3`. However, after the local `0662` ACK the XTR becomes quiescent and does not emit `06C5`; therefore a literal "next-page stride" interpretation is not supported.

**Strong conclusions**
1. The `055A..06E5` data is a coherent structured family rather than twelve unrelated 33-word blocks.
2. The FC16 `count33` boundaries are transport chunk boundaries superimposed on a stronger 12-word internal periodicity.
3. The four XTR-vs-ATEC differences inside `05FF` and `0662` occur in transition records between repeated 12-word regions. This is substantially more specific than EXP228's page-level discriminator result.
4. The family behaves like static/configuration/descriptor data in the two genuine ATEC captures; it does not look like ordinary fast runtime telemetry.
5. No causal Online/DCM scheduler-enable field is identified.

**Hypotheses**
- `061C/061E` and `067E/067F` may encode model/configuration metadata controlling which substructures are relevant or serialized.
- `061C=3` may be related to the three-page-stride jump from `05FF` to `0662`; this remains correlation only.
- Repeated numerical constants (`31`, `12`, `59`, `23`) also fit a calendar/range/constraint-descriptor interpretation, which competes with a page-selection/capability interpretation.
- The family begins immediately after the previously identified `0559 Link Integration` register, but adjacency alone is insufficient to call the family integration-specific.

**Unknowns**
- Formal record width/schema; 12 words is strongly supported statistically but undocumented.
- Semantic meaning of records 16 and 24.
- Whether XTR's skipped pages are absent, unsupported, unchanged, or merely omitted from the particular sync path.
- Whether the XTR-only `0003` values are counts, enum values, pointers, feature identifiers, or unrelated metadata.

**Negative / safety result**
The attractive `value 3 == three page strides` observation is not sufficient for a pointer interpretation because the second `3` does not cause an observed `0662 -> 06C5` transition. No write target follows from EXP229.

**Next**
EXP230 should stay offline and classify the 12-word records semantically, explicitly testing calendar/range-descriptor versus model/capability/page-selection hypotheses against the public Online map, recovered firmware semantics and all available cross-model evidence.

### EXP229 refinement — calendar interpretation strongly upgraded

A documentary cross-check after the initial EXP229 analysis materially changes the semantic ranking of the 396-word family. Thermia iTec/iTec XTR documentation confirms four calendar-controlled function groups (hot-water block, EVU/power limitation, silent mode, temperature reduction), with up to 8 calendar settings per function. The Thermia Online guide independently describes 8 occasions for 4 categories with start/end dates. That yields 32 user schedule slots.

EXP229 independently found 396 words = 33 candidate 12-word records. The family also contains strong calendar/time-domain constants and tuples (`59`, `23`, `31`, `12`; values compatible with 23:59, 22:30, 16:00, 05:30 and Dec-31 boundaries).

**Revised strong conclusion:** `055A..06E5` is now strongly indicated to encode calendar/schedule data. Exact field order, slot-to-function ordering, recurring-vs-date representation, weekday masks, and the role of the 33rd record remain unknown. The 32+1 relationship is compelling but is still a hypothesis, not proof.

**Next confirmation path:** passive/manual A/B/A on one unused calendar slot using a harmless future period, observing the native `0x0F` delta and restoring immediately. No heat-pump restart or ESP TX is required.


---
## EXP230 — Offline write-mailbox reconstruction — COMPLETE / POSITIVE

**Hypothesis**

The genuine Online/DCM `0x0F FC03 0708/count6` poll exposes a command-pending indicator which causes the controller to read a desired-state settings block at `0x03E8/count13`.

**Method**

Offline only. Parsed the four existing genuine Online/DCM captures:
- `thermia_capture_20260924_210001`
- `thermia_capture_20260925_071517`
- `thermia_capture_20260925_090209`
- `thermia_capture_20260925_090550`

No heat-pump restart, ESP TX, semantic write, configuration change or YAML change.

**Observed facts**

1. The corpus contains 54 exact `0F 03 0708 0006` requests.
2. 38 receive valid six-word responses; 16 are unanswered, all in the early `090550` rejoin interval before `0x0F` becomes responsive.
3. Exactly two valid responses have:
   `0708..070D = 0000 0001 0000 0000 077F 0006`.
   The remaining 36 valid responses have `0709=0000`.
4. Both `0709=0001` responses are immediately followed by `0F 03 03E8 000D`. No `0709=0000` response is followed by that read.
5. Across the entire four-capture corpus there are exactly two FC03 `03E8/count13` requests, so the association is 2/2 positive and 36/36 negative among valid `0708` responses.
6. Event 1 timing:
   - `11.383`: `0708/count6` request
   - `11.406`: `0709=0001` response
   - `11.447`: `03E8/count13` request
   - `11.486`: desired-state response
7. Event 2 timing:
   - `23.962`: `0708/count6` request
   - `23.986`: `0709=0001` response
   - `24.025`: `03E8/count13` request
   - `24.067`: desired-state response
8. The desired-state blocks are:
   - event 1: `0017 0014 0028 0000 0001 0001 0012 0012 0002 0028 001E 003C 0014`
   - event 2: `0016 0014 0028 0000 0001 0001 0012 0012 0002 0028 001E 003C 0014`
   Only `03E8` changes (`23 -> 22`); the remaining 12 words are identical.
9. On the next `0708` poll after each event, `0709` is back to zero.
10. `070C/070D` do not identify command-pending state: `077F/0006` occurs in both idle and command responses, while startup/rejoin captures show other values in these positions.
11. A later `090550` FC16 `03E8/count13` authoritative snapshot matches the second desired-state image exactly. This is supportive cross-capture evidence only, not a same-transaction apply ACK.

**Strong conclusions**

- `0709` is the strongest available command-pending / command-count field candidate in the six-word `0708` mailbox response.
- In the observed working Online/DCM system, `0709=1` is a sufficient discriminator for the controller to immediately fetch the `03E8/count13` desired-state image.
- The desired-state command is not a single-register write: the DCM returns a complete 13-word image, preserving non-target values while changing the requested register.
- This materially narrows the native write serializer.

**Hypotheses**

- `0709` may be a boolean dirty flag or a pending-command count. Only `0` and `1` are observed, so the distinction is unresolved.
- Clearing `0709` on the next poll may be DCM-side consumption after serving the desired block, controller acknowledgement semantics, or both.
- `070C/070D` likely belong to session/readiness metadata rather than the write trigger.

**Unknowns**

- How the local XTR controller is made to schedule `0708/count6` reads at all.
- Whether a desired-state read alone guarantees controller acceptance/application.
- Exact semantics of the remaining `0708` words.
- Whether all writable setting families use the same pending flag and full-image response pattern.

**Negative result / safety**

EXP230 does not justify direct second-master FC03 or FC16 writes to the heat pump. The local controller must first expose the genuine read-side scheduler/device-recognition path. No new active write target is approved.

**Next**

EXP231 should remain offline and reconstruct the scheduler activation prerequisite from genuine Online/DCM startup/rejoin ordering, with special attention to A5 activity versus first `0708` polling and first successful `0x0F` response.


---
## EXP231 — Offline scheduler-origin and XTR service-slot comparison — COMPLETE / POSITIVE

**Hypothesis**
The genuine ATEC/DCM `0x0F FC03 0708/count6` poll belongs to a controller-side service scheduler that exists before `0x0F` endpoint readiness. Comparing its recurrent cycle with local XTR cold-boot traffic may reveal a homologous XTR-native mailbox/service slot relevant to write access.

**Method**
Offline only. Parsed all four genuine Online/DCM captures (`210001`, `071517`, `090209`, `090550`) and local XTR EXP221/EXP222 raw logs. No heat-pump restart, no ESP TX, no setting change.

**Observed facts**
1. Genuine corpus contains 54 exact `0F 03 0708 0006` requests.
2. Every one of the 54 follows the A5 `002E/count10` response by 0.262..0.394 s.
3. Every one also follows the recurrent `0x06 FC17 AFC8/12 -> AFDC/5` poll by 0.110..0.236 s.
4. Inter-`0708` cadence is normally ~4.2 s in all four captures.
5. In rejoin capture `090550`: first `0708` request = 0.987 s; first successful `0x0F FC16` ACK = 66.860 s; 16 prior `0708` polls are unanswered; first `0708` response = 68.235 s. Thus scheduler activity predates DCM `0x0F` readiness by ~66 s.
6. The trace begins with the scheduler already enabled; no visible event in these captures can be identified as the original enable transition.
7. Local XTR EXP221+EXP222 contain 72 exact `0x0F FC17 read 0730/count8 + write 071C/count8` requests. Their median cadence is ~4.25 s.
8. Every local XTR FC17 request follows a local `0x06` poll; median delay is ~0.247 s. Local topology has no A5/0x04/`0708` service family.
9. EXP226 already decoded the XTR FC17 write image `071C..0723` as predominantly controller RTC/date-time. `0730..0737` is still entirely unknown because no valid response has been captured.

**Strong conclusions**
1. Successful `0x0F` FC16 ACK completion is not the trigger that creates the genuine ATEC/DCM `0708` scheduler. The scheduler is controller-side and can run while the DCM `0x0F` endpoint is silent.
2. `0708` is not an isolated poll; it is one slot in a stable ~4.2 s service cycle coupled to A5/0x04/0x06 scheduling.
3. For the local XTR, the recurrent post-`0x06` `0x0F FC17 071C/0730` transaction occupies a strongly analogous scheduler position and cadence. This is functional/scheduling homology, not wire-protocol equivalence.
4. For native XTR write access, `0730..0737` is now a higher-value target than trying to force the ATEC-specific `0708` scheduler into existence.

**Hypotheses**
- `0730..0737` may be an XTR-generation desired-state/status/command mailbox returned by the external service endpoint while the controller simultaneously publishes RTC state in `071C..0723`.
- A valid `0730..0737` response may keep the XTR service session alive or cause further desired-state reads. This is unproven.
- The scheduler-enabled controller fingerprint (`A811/A812=000C/0500`, shorter A7F8 span) may reflect persistent commissioning/firmware/platform state, but causality is still unknown.

**Unknowns**
- Exact semantics and safe idle/default values for `0730..0737`.
- Whether an XTR FC17 response alone is sufficient to extend the service session.
- Whether the XTR ever supports the ATEC `0708` family, or whether FC17 is its generation-specific replacement.
- The original event/configuration that enables the ATEC extended scheduler.

**Negative / safety result**
Do not continue FC16 ACK-chain expansion as a scheduler-enablement strategy, and do not guess an eight-word `0730` response. No active write target is established by EXP231. Heat-pump restarts remain paused.

**Next**
EXP232 should remain offline and search all available firmware/artifacts/maps/source discussions for `0730..0737`, FC17 read/write-multiple semantics, or an eight-word XTR/Connect response image. If no evidence-backed neutral response can be recovered, stop before an active responder rather than synthesize zeros.


---
## EXP232 — Offline `0730..0737` response reconstruction — COMPLETE / STRUCTURAL POSITIVE + IMPORTANT NEGATIVE

**Hypothesis**

The local XTR `0x0F FC17 read 0730/count8 + write 071C/count8` exchange may contain an external-to-controller service/command return bank whose safe response can be reconstructed or at least constrained from existing captures, related Thermia FC17 role interfaces, archived artifacts and external reference work.

**Method**

Offline/read-only only. No heat-pump restart, ESP TX, setting change or YAML change. Searched:
- local EXP221, EXP222 and EXP225 logs and older EXP71/71B evidence for an FC17 count-8 slave response;
- all indexed project/library material for `0730`, `0737`, `071C`, decimal register `1840`, and exact FC17 response signatures;
- fclauson's `0F_register_value_map.xlsx`, `modbus_slave.py`, `Config.yaml` and Discussion #143;
- read-only repository searches in `piotr-romanowski/thermia-bus-sniffer`, `klejejs/ha-thermia-heat-pump-integration`, and `ryckema/Thermia_itec`.

**Observed facts**

1. Local XTR requests have exact shape `0F 17 0730 0008 071C 0008 10 <16-byte controller write image> CRC`. EXP226 already establishes that the write image is predominantly transformed controller RTC/calendar data.
2. A valid FC17 response for eight requested words would have byte count `0x10`, total length 21 bytes, and begin `0F 17 10`. No such genuine response was found in the relevant local/archived logs. Searches for both decoded shape (`slave=0x0F function=0x17 length=21`) and raw prefix (`0F 17 10`) were negative.
3. No `0730..0737` values are present in fclauson's spreadsheet or Python slave logger. His reference work covers the ATEC/DHP-AQ `0x0F` FC03 read blocks and FC16 state blocks, not this XTR FC17 bank.
4. Discussion #143 similarly documents two FC03 read areas plus FC16 write areas on the reference Online/DCM topology and supplies no XTR `0730` response.
5. Read-only repository searches for `0730`, `071C`, `0x0730`, decimal `1840`, and FC17 produced no usable source mapping in the three available repositories.
6. A platform-wide FC17 address convention emerges from independently established interfaces:
   - `0x0A`: read base `B3B0`, write base `B3C4`, delta `0x14`;
   - `0x06`: read base `AFC8`, write base `AFDC`, delta `0x14`;
   - reference `0x04`: read base `ABE0`, write base `ABF4`, delta `0x14`;
   - reference `0x05`: read base `AC12`, write base `AC26`, delta `0x14`;
   - local XTR `0x0F`: write base `071C`, read base `0730`, delta `0x14`.
7. The nearby service addresses also form exact `0x14` steps: `0708 + 0x14 = 071C` and `071C + 0x14 = 0730`. ATEC/DCM uses `0708/count6` as a command/session header, whereas XTR uses `071C` as the write side and `0730` as the read side of FC17.
8. The room-sensor path provides architectural proof that an FC17 **read-bank response can be semantic controller ingress**: a device-owned pending setpoint word returned in the read bank is adopted by the controller. This is architectural analogy only; room-sensor emulation is not a project direction and no field position is transferred to `0730`.

**Strong conclusions**

1. `0730..0737` is best classified as an **external/service-owned return bank** in the XTR slave-0x0F FC17 role transaction. The controller explicitly reads it, so it is a real ingress surface even though its fields are unknown.
2. The exact `+0x14` separation is not accidental-looking: it is a repeated Thermia FC17 register-bank convention across at least five role interfaces.
3. EXP231's scheduler/cadence homology remains useful, but the stronger EXP226+EXP232 evidence argues against calling XTR `071C/0730` a direct equivalent of the ATEC `0708` mailbox. They are structurally related service families, not proven wire-semantic equivalents.
4. Current artifacts are insufficient to reconstruct a safe `0730..0737` response.

**Hypotheses**

- `071C..0723` may be controller-owned service/RTC state, while `0730..0737` is the paired external service/device state or request bank.
- Because other FC17 read banks can carry controller-ingress requests, one or more `0730` words could eventually carry command/session semantics. No current evidence identifies which word/value.
- The exact `0708 -> 071C -> 0730` spacing may reflect a common service-register namespace inherited across controller generations, even though ATEC and XTR use different Modbus function shapes.

**Unknowns**

- Any genuine value for `0730..0737`.
- Whether the neutral image is zero, nonzero metadata, clock acknowledgement, capability data, command selectors, or another structure.
- Whether a genuine XTR Online/Connect endpoint answers this FC17 transaction and whether that response changes after commissioning.
- Whether command writes on XTR ultimately use this bank or a separate service path.

**Negative / safety result**

No genuine response image was recovered. Therefore no active FC17 responder is justified. Do not return zeros, echo `071C..0723`, synthesize an RTC mirror/inverse, or copy another slave's read-bank layout. Those would be uncontrolled semantic guesses.

**Next**

EXP233 should remain offline and build a formal cross-role FC17 bank-schema map (`0x0A`, `0x04`, `0x05`, `0x06`, `0x0F`), comparing read/write counts, offsets, known request/feedback fields and lifecycle timing. The goal is to determine whether response field-position homology can narrow `0730..0737` enough to justify a bounded active test.
---

## EXP233 — Offline cross-role FC17 bank-schema analysis — COMPLETE / STRUCTURAL REFINEMENT + NEGATIVE FOR FIELD-POSITION HOMOLOGY

**Hypothesis**

The repeated Thermia FC17 `+0x14` paired-bank structure may preserve more than address spacing. If request/feedback fields occupy homologous relative positions across roles, one or more XTR `0730..0737` words might be constrained without guessing.

**Method**

Offline/read-only only. No heat-pump restart, ESP TX, setting change or YAML change. Parsed all FC17 request shapes in the four genuine Online/DCM captures and cross-referenced the established local/XTR semantics for `0x02`, `0x06`, `0x0A` and the cold-boot `0x0F` FC17 family.

**Observed facts**

1. In the four genuine reference captures, the recurrent FC17 request schemas are:
   - `0x02`: read `A7F8=43000/count13`, write `A80C=43020/count7` — 274 requests;
   - `0x04`: read `ABE0=44000/count12`, write `ABF4=44020/count4` — 275 requests;
   - `0x05`: read `AC12=44050/count12`, write `AC26=44070/count4` — 2 requests;
   - `0x06`: read `AFC8=45000/count12`, write `AFDC=45020/count5` — 69 requests;
   - `0x0A`: read `B3B0=46000/count3`, write `B3C4=46020/count3` — 31 requests.
2. Every pair above is separated by exactly **20 decimal registers**, i.e. `0x14`.
3. The local XTR `0x02` uses the same `43000 -> 43020` pair but read-count 15 instead of 13. Thus bank spacing is fixed independently of used payload length.
4. Local XTR `0x0F FC17` uses write `071C=1820/count8` and read `0730=1840/count8`. This is again a +20-register page pair, but the direction is reversed relative to the common lower-read/upper-write pattern.
5. The adjacent service addresses normalize to exact decimal pages: `0708=1800`, `071C=1820`, `0730=1840`.
6. The `0x02` and `0x04` genuine read-bank payloads are clearly state/telemetry-style multiword images; therefore an FC17 read bank is not inherently a command bank.
7. Known semantic ingress/control-like fields do not share one relative position:
   - `0x0A` read word1 (`B3B1`) is a pending room-setpoint request; accepted value is reflected later at paired write word1 (`B3C5`);
   - `0x06` read word2 (`AFCA`) is a transport REQ/data-valid strobe; its ACK is not the paired write word2 but native `0x0F:0861`;
   - `0x06` read word9 (`AFD1`) is version metadata.
8. A role can have a zero command field without the whole response bank being semantically neutral:
   - `0x0A B3B1=0` means no setpoint request, but an all-zero `0x0A` bank would also report a false room temperature of 0 °C;
   - a valid all-zero `0x06` response changes controller polling/presence behavior and exposes `EXP 0.0`.
9. The XTR `071C/0730` stream is lifecycle-gated rather than ordinary steady runtime: EXP224 saw zero exact target frames during a clean runtime Heat Curve A/B/A, whereas EXP221/225 reproduced the family after controller cold boot.

**Strong conclusions**

1. `+0x14` is best interpreted as a **generic 20-register Thermia FC17 bank/page stride**, not as evidence that adjacent banks share command semantics.
2. `0708=1800`, `071C=1820`, `0730=1840` are three consecutive 20-register service pages. This is strong namespace structure, but it does not prove ATEC `0708` and XTR `0730` use the same mailbox schema.
3. There is no cross-role field-position homology strong enough to assign a pending/request word in `0730..0737`.
4. Direction alone proves that `0730..0737` is controller-ingress data, but other roles show such ingress may carry telemetry, metadata, transport state or semantic requests depending on role.
5. Because the XTR FC17 family is boot/recovery gated, it may be a startup/service/RTC-session exchange rather than a general runtime desired-state interface.

**Hypotheses**

- The 1800/1820/1840 sequence may be a three-page service namespace: a header/control page plus controller-owned and external-owned service pages.
- The reversed direction of the XTR 1820/1840 pair may reflect a symmetric service synchronization role rather than a normal accessory sensor role.
- One or more `0730` words may still carry command/session data, but positional analogy cannot identify them.

**Unknowns**

- Any genuine value or field meaning in `0730..0737`.
- Whether `0730` is used only during startup or can remain active after a successful external-service handshake.
- Whether a genuine response would cause the FC17 stream to persist into runtime.
- Whether the preceding 1800 page is used by XTR at all or is only an older/reference-generation service page.

**Negative / safety result**

EXP233 does not justify an active FC17 response. Do not map room-sensor word1 to `0731`, accessory word2 to `0732`, or transmit eight zero words. The generic page structure is now better understood, but role semantics remain insufficiently constrained.

**Next**

EXP234 should remain offline and search firmware/register maps/source artifacts using the normalized decimal page bases `1800`, `1820` and `1840`, plus neighboring 20-register pages, looking for a role name, field labels or a genuine XTR service response image.




---

## EXP234 — Offline decimal/service-page archaeology — COMPLETE / NEGATIVE IN ACCESSIBLE INDEXED CORPUS, RAW-BINARY GAP REMAINS

**Hypothesis**

The normalized service-page bases `1800`, `1820`, `1840` (hex `0708`, `071C`, `0730`) may appear in recovered firmware, source artifacts, register maps, or repository code with names/field metadata sufficient to identify the XTR service interface or a genuine `0730` response.

**Method**

Offline/read-only only. Searched the available indexed Project/Library corpus and relevant Thermia repositories using decimal, hex and FC17-shape variants. Attempted to materialize the archived `THERMIA_PART9_BUNDLE.zip` for byte-level inspection, but the Project file currently has no authorized raw-byte materialization path in this runtime. No heat-pump access or TX.

**Observed facts**

1. No accessible indexed source exposed a named schema for page 1800, 1820 or 1840.
2. No genuine `0x0F FC17` response for `0730/count8` was recovered.
3. No repository hit tied `0730`, `071C`, decimal 1840/1820, or the exact XTR FC17 pair to a field/struct name.
4. The Part9 archive could not be exhaustively byte-scanned because raw materialization was unavailable.

**Strong conclusions**

- The accessible indexed corpus does not currently contain the missing `0730` schema or response image.
- This is not an exhaustive firmware/binary negative because one relevant archive remains inaccessible at raw-byte level.

**Hypotheses**

- The missing serializer/service schema may exist only in a DCM/Connect binary not present in the indexed corpus, or in an unindexed binary region of the archived bundle.

**Unknowns**

- Whether the inaccessible Part9 raw bytes contain the page constants or response builder.

**Negative result**

No new safe `0730` response value was obtained.

---

## EXP235 — Offline DCM-to-XTR topology-transferability audit — COMPLETE / STRONG DOWNGRADE OF DIRECT TRANSFERABILITY

**Hypothesis**

The genuine ATEC/DHP-AQ DCM command architecture may be sufficiently wire-homologous to the local XTR that `0708 -> 03E8` should remain the primary local write-access target.

**Method**
Offline comparison of the established reference and local topology fingerprints. No new bus activity.

**Observed facts**

1. Reference scheduler-enabled captures continuously use slave `0x04`, A5 and controller-originated `0x0F FC03`.
2. Local XTR runtime instead uses slave `0x1E` and shows no normal A5/A4/0x05/`0x0F FC03` scheduler family.
3. Reference controller fingerprint: `A7F8/count13`, `A811=000C`, `A812=0500`.
4. Local XTR fingerprint: `A7F8/count15`, `A811=FFFF`, `A812=0000`.
5. Local XTR `071C/0730` appears in a boot/recovery service window and uses FC17, not the reference runtime FC03 mailbox transaction.

**Strong conclusions**

- The two systems are protocol relatives but not the same observed bus topology.
- The genuine `0708 -> 03E8` path remains strong evidence for Thermia's desired-state design, but should no longer be treated as the most likely one-for-one local XTR write path.
- A future genuine XTR/Connect capture would still be valuable, but emulating the old DCM scheduler is now a secondary route rather than the primary route.

**Hypotheses**

- XTR may implement equivalent application semantics through a different internal panel/controller path or generation-specific serializer.

**Unknowns**

- Whether a commissioned XTR Connect module activates an otherwise dormant path not visible in the no-module local topology.

**Negative result**

No evidence justifies forcing the reference scheduler onto the XTR.

---

## EXP236 — Offline local-UI write-causality audit — COMPLETE / POSITIVE DIRECTIONAL RESULT

**Hypothesis**

The known XTR `0x0F FC16 03E8/count14` Heat Curve frame is an outbound consequence of a successful local UI mutation, not the semantic command ingress itself.

**Method**

Offline causal comparison of EXP143 and EXP177. No new TX or UI action.

**Observed facts**

1. EXP143: after a physical Heat Curve change on the Thermia UI, the controller begins transmitting `0x0F FC16 03E8/count14`; word0 follows the actual Heat Curve value, and the controller retransmits until the block is ACKed.
2. EXP177: an ESP-originated native-looking `03E8/count14` frame with only Heat Curve word0 changed was transmitted cleanly, followed by a restore, but no semantic Heat Curve change was observed.
3. Therefore the same block is sufficient to export/announce the already-changed state but is not sufficient, in the reverse second-master direction tested, to create that state change.

**Strong conclusions**

- The semantic local UI mutation occurs **before** the outbound `03E8` synchronization event.
- `03E8` is best classified locally as a controller-owned state/config synchronization block, not the user-input ingress path.
- The best next write-access experiment is to capture the full bus around a physical UI A/B/A change and identify any reversible pre-`03E8` event.

**Hypotheses**

- The true ingress may be a panel-to-main-controller transaction on a slave/function family that previous 0x0F-focused experiments did not preserve with enough timing context.
- A local panel event may occur on `0x01` or another role, but no XTR-specific address is assigned without capture evidence.

**Unknowns**

- Exact slave, function code, payload and timing of the local panel input.
- Whether the panel shares this same observed RS485 segment for the semantic input or communicates internally before the main controller mirrors state onto the bus.

**Negative / safety result**

Do not repeat direct `0x0F FC16 03E8` writes or invent `0730` responses.

**Next**

EXP237 should be a strictly passive full-bus Heat Curve A/B/A trace with exact user-event markers and pre/post windows.


---

## EXP236A — Offline cross-setting outbound-sync audit — COMPLETE / POSITIVE GENERALIZATION

**Hypothesis**

The Heat Curve result from EXP143/177 is not a one-off. If physical UI changes for other settings also appear afterward as controller-originated `0x0F FC16` page updates, then the `0x0F` write-side pages are best treated as a generic controller-owned configuration/state export layer rather than the semantic ingress.

**Method**

Offline comparison only. Existing proven local results were compared for:
- Heat Curve;
- Activate Cooling;
- Operation Mode.

No new bus transmission, UI action, restart, YAML change or setting mutation was performed.

**Observed facts**

1. Heat Curve:
   - physical UI change reactivates `0x0F FC16 03E8/count14`;
   - `03E8` follows the actual curve value;
   - EXP177 showed that replaying the same native-looking page toward `0x0F` did not create the semantic Heat Curve change.
2. Activate Cooling:
   - the local XTR physical UI toggle is proven to change native `0x0F:0442`;
   - `0442 = 0/1` tracks OFF/ON in the `0442..044E` cooling page.
3. Operation Mode:
   - physical `AUTO -> COMPRESSOR -> AUTO` changes local `0x0553: 1 -> 2 -> 1`;
   - the surrounding `0546/count20` page remains stable for the previously tested structural words.

**Strong conclusions**

- Controller-originated `0x0F FC16` is a general configuration/state serialization path spanning at least heating, cooling and system-operation settings.
- The presence of a changed value in one of these pages should not be interpreted as the command ingress.
- EXP236's upstream-mutation model is strengthened beyond Heat Curve alone.

**Hypotheses**

- A common panel/controller mutation mechanism may feed multiple page serializers.
- The page selected for export is setting-family specific, while the ingress mechanism may be shared.

**Unknowns**

- Whether the physical panel input itself is visible on the monitored RS485 segment.
- Which slave/function family, if any, carries the pre-export panel event.

**Negative result / safety**

No new direct write target emerges. Do not replay `0442` or `0553` FC16 pages as commands based on this result.

---

## EXP236B — Offline page-family and pre-export discriminator audit — COMPLETE / POSITIVE DESIGN REFINEMENT

**Hypothesis**

If unrelated UI settings are serialized into different `0x0F` page families, then the highest-value write-ingress evidence is any reversible event that precedes those page-specific exports, not the exports themselves.

**Method**

Offline comparison of:
- Heat Curve -> `03E8/count14`;
- Activate Cooling -> `0442..044E`;
- Operation Mode -> `0546/count20` / `0553`;
- prior DHW START and COMFORT/ECO negatives in the recurrent `03E8..03F5` page.

**Observed facts**

- Three proven UI-controlled settings live in three distinct native `0x0F` page families.
- DHW START A/B/A did not change recurrent `03E8..03F5`; `03F1` stayed unchanged.
- DHW COMFORT/ECO A/B/A likewise left `03E8..03F5` byte-for-byte unchanged.
- Therefore the recurrent heating page is not a universal container for all settings changes.

**Strong conclusions**

- Native `0x0F FC16` serialization is page-family specific after the semantic state has already changed.
- Tomorrow's full-bus trace should prioritize a narrow time window **before the first changed FC16 page**, across every slave and function code.
- A repeated pre-export pattern across Heat Curve and Operation Mode would be much stronger ingress evidence than another page mapping.

**Hypotheses**

- If the panel is a separately addressed bus role, a short request/write/response may appear immediately before the changed `0x0F` page.
- If no such pre-export bus event exists, the display/controller interaction may be internal to the same controller assembly and inaccessible on this observed segment.

**Unknowns**

- Exact latency from button/confirm action to controller-state mutation.
- Whether navigation traffic and commit traffic are distinguishable.
- Whether a second setting family will share the same pre-export event shape.

**Decision**

Keep **EXP237** reserved for tomorrow as the strictly passive local-UI ingress trace. Start with Heat Curve A/B/A; if successful, repeat with Operation Mode for cross-setting confirmation.


## EXP237 — Passive local-UI ingress trace — PREPARED

**Hypothesis**

A physical Heat Curve change is semantically accepted before the known controller-originated `0x0F FC16 03E8/count14` state export. If that ingress traverses the observed RS485 bus, at least one reversible frame/field should precede the first `03E8` export on both the `baseline -> +1` and `+1 -> baseline` transitions.

**Controlled variable**

Only physical Heat Curve: `baseline -> baseline+1 -> baseline`. No other Thermia setting changes.

**Design**

- fully passive / RX-only;
- exact EXP225 RX-only source used as base; obsolete EXP225 experiment code removed;
- 10 s untouched baseline trace;
- 20 s trace opened by a marker pressed **before** Heat Curve +1;
- 20 s trace opened by a marker pressed **before** exact restore;
- every recognised CRC-valid frame in each window is logged as raw hex with phase and marker-relative timestamp;
- first `0x0F FC16 03E8` frame is highlighted with elapsed time and number of preceding frames;
- passive parser additionally recognises slave `0x01`, `0x03`, `0x05`, `0xC8` and common Modbus FC01/02/05/06/08/0F/16 to avoid discarding a possible panel/service ingress frame.

**Safety**

No TX pin, DE LOW, no restart, no ACK, no response, no scan, no room-sensor path, no synthetic register image. Experimental controls remain under Configuration.

**Success**

A pre-`03E8` frame/field that changes with `+1` and reverses on restore.

**Stop / negative criterion**

If both transitions contain no reversible pre-`03E8` event, record that as evidence that the local UI mutation may occur internally before the controller exports state onto this RS485 segment.

Status: **PREPARED / NOT YET RUN**.

## EXP237 — Passive Heat Curve local-UI ingress trace — COMPLETE / VALID NEGATIVE

**Hypothesis:** a physical Heat Curve mutation traverses the observed RS485 segment before the known controller-owned `0x0F FC16 03E8/count14` state export, producing a reversible frame/event before the changed export in both directions.

**Only experimental variable:** physical Heat Curve `36 -> 37 -> 36`. ESP TX remained disabled.

**Observed facts:**
- baseline showed `03E8=36`;
- after the +1 marker, the first `03E8` carrying the target value `37` appeared at +2418 ms;
- the 17 frames strictly before that target export were all ordinary known traffic (`0x02`, `0x1E`, `0x14`, `0x0A`, `0x0F:085F`); no new slave or function code appeared within the recognised parser set;
- after the restore marker, a stale cyclic `03E8=37` appeared at +114 ms, so the firmware's `FIRST_03E8` marker did not identify the semantic restore;
- the first `03E8` carrying the restored value `36` appeared at +4821 ms;
- the intervening restore-window traffic again contained only normal known frames and no reversible candidate preceding the target export;
- final summary: `total=420 baseline=86 plus=166 restore=168 S01=0 unusualFC=0 03E8=42 resync=0 drops=0`.

**Strong conclusion:** no distinct reversible Heat-Curve ingress frame/event was observed within EXP237's recognised parser coverage before the authoritative controller-owned `03E8` export.

**Important negative result:** the experiment did not reveal a panel-command frame, new slave, unusual function code, or pre-export field that follows `36 -> 37 -> 36`.

**Logger correction:** future UI-ingress experiments must detect the first export carrying the expected target value; "first page after marker" can be stale and is not a valid semantic boundary.

**Hypothesis remaining:** panel semantic ingress may be internal to the controller/display path or on another bus segment.

## EXP238 — Passive Operation Mode local-UI ingress trace — PREPARED

**Hypothesis:** if physical-panel semantic ingress is visible on this RS485 segment for a different setting family, `AUTO -> COMPRESSOR -> AUTO` should produce a reversible pre-export frame/event before the first target-valued `0x0F FC16 0546/count20` exports (`0553=2`, then `0553=1`).

**Only experimental variable:** physical Operation Mode `AUTO -> COMPRESSOR -> AUTO`.

**Design:** same bounded passive trace as EXP237, but target-value-aware. Stale `0546` pages do not stop the pre-export counter. The passive stream parser accepts standard Modbus unit IDs `0x00..0xF7` for the already-supported common functions, closing EXP237's residual unknown-address blind spot.

**Safety:** RX-only; no Thermia bus TX, ACK, response, scan, write, restart or room-sensor emulation. Controls remain under Home Assistant Configuration.



---
## 2026-09-27 — Inter-experiment offline DCM mailbox re-audit (before EXP238)

**Status:** analysis only; no new experiment number, no ESP TX, no heat-pump setting change. EXP238 remains PREPARED / NOT RUN.

**Observed facts**
- Re-analysed all four genuine external Online/DCM logs.
- Confirmed the two `0709=1` command events and their immediate `03E8/count13` desired-state reads.
- Found a distinct first-rejoin `0708` response in `090550`: `[0000,0000,7FFF,FFFF,0080,0007]`. It follows 16 unanswered mailbox polls and is followed 69 ms later by the start of a large FC16 full-state snapshot.
- Regular `0708` polling pauses during the large snapshot and resumes after `06F1/count3` with idle `[0000,0000,0000,0000,077F,0006]`.
- `090209` shows `070C=0080 -> 0000` while later snapshot pages continue; `070D=7` is unique to the first successful rejoin response in the available corpus.
- The second known command desired image from `210001` is byte-identical to the `03E8/count13` image at the start of the successful `090550` rejoin snapshot.

**Strong conclusion**
`0708/count6` is a multi-purpose mailbox/lifecycle page. `0709` is the proven one-shot command-pending discriminator; other words participate in endpoint rejoin/synchronization. The reference command path is controller-pull/full-image based.

**Hypothesis**
The XTR-specific `0730/count8` return bank may likewise be a status/dirty/session selector rather than a direct setting-value block. No field mapping or safe response value is established.

**Safety / next**
Do not answer `0730` yet. Finish the offline `0708` state-machine correlation before executing EXP238.


---
## EXP234B — Raw-binary completion of `0730` archaeology — COMPLETE / NEGATIVE FOR SERIALIZER IN LINK CC HOST

**Hypothesis**

The raw Link CC 2.7.42 firmware may contain named/local constants or code sufficient to reconstruct the XTR `0x0F FC17 read 0730/count8` response.

**Observed facts**

- Offline only; no heat-pump TX or setting change.
- Original 2.7.42 `ccimage.bin` was materialized and parsed as a Windows CE B000FF image.
- Managed `ParameterCache.dll` contains the expected DHP Set/Get/binding implementation and real parameter IDs (`030A`, `4402`, `4414`).
- No managed `ldc.i4 071C` or `ldc.i4 0730` was found in the heat-pump/regulation assemblies.
- The three `0708` immediates in `RegulationEngine.dll` map to node constructors and are decimal-1800 timing/configuration values, not service-page references.
- Full-ROM exact-constant mapping puts all exact `071C`/`0730` hits in unrelated Windows/UI/framework files.
- Native `HECTArch.dll` is the HE/Z-Wave transport layer and exposes `HESetGetReqRsp`/ServiceBind/ServiceSetGet; it contains no exact 32-bit `0708/071C/0730` constants.
- The available 4.2.1724 image uses a different opaque packaging and yielded no additional searchable DHP/local-page evidence.

**Strong conclusion**

The missing DCM03/Connect -> Thermia RS485/service-page serializer is not present in the audited Link CC host-side DHP/HE stack. EXP234's desired `0730..0737` idle image cannot be reconstructed from this firmware.

**Negative result recorded**

Do not construct a `0730` response from Link CC parameter IDs, zeros, echoes, or page-position analogy.

**Unknowns**

Exact `0730..0737` idle/session image, challenge/approval relation, pending selector and post-acceptance scheduler behavior remain unknown.

**Next**

Search for Thermia Connect/DCM03 firmware or heat-pump Gateway/controller firmware that implements the missing local serializer. Keep EXP238 PREPARED / NOT RUN.


---
## EXP239 — Offline 071C/0730 challenge-response analysis — IN PROGRESS

**Hypothesis:** the controller's eight-word `071C..0723` image is a 16-byte challenge/session token and the gateway's eight-word `0730..0737` return is a reproducible non-trivial response that unlocks the iTec Online state machine.

**Only experimental variable:** none on the heat pump. EXP239 is offline/read-only analysis of published challenge/response evidence. EXP238 is parked and was not run.

**Available input:** two complete challenge/response pairs from the new genuine iTec Eco 5 Online capture. The full 10,719-frame raw log and timeline script are not yet locally available.

**Observed facts:**
- Pair 1 Hamming distance challenge→response: `65/128` bits.
- Pair 2 Hamming distance challenge→response: `62/128` bits.
- Input differential has 55 changed bits; output differential has 68 changed bits.
- Fixed-XOR model fails because the inferred masks differ.
- Fixed 128-bit modular addition/subtraction fails in both byte orders.
- Fixed per-byte addition fails.
- No fixed 128-bit rotation followed by a fixed XOR mask fits.
- The more general `byte_permutation(input) XOR fixed_mask` model also fails because the input and output XOR differentials do not have the same byte multiset.
- MD5, truncated SHA-1/SHA-256/SHA-512 and 128-bit BLAKE2 variants do not reproduce the responses.

**Strong conclusions:**
1. The available pairs rule out several trivial linear/static response functions.
2. A non-linear keyed/authenticated transform is now a substantially stronger hypothesis, but AES/CMAC or any named primitive remains unproven.
3. No arbitrary new `0730` response can be calculated from the present evidence.

**Hypotheses:**
- `071C` carries a challenge/session nonce.
- `0730` is an authenticator/response under gateway, installation or pairing secret material.
- The response may also depend on persistent pairing history or session state.

**Unknowns / completion criteria:** repeated-challenge determinism, cross-power-cycle stability, exact response-delay distribution, first-success→FC16 synchronization timing, first-success→0708 mailbox timing, and whether the same challenge is held until acceptance. These require the raw Eco 5 log.

**Tooling:** created `exp239_extract_071c_0730.py`, a read-only log analyzer. A parser self-test against the older genuine ATEC/DCM 090550 capture correctly finds zero 071C/0730 attempts and its known 0708 mailbox responses.

**Status:** EXP239 remains open; Phase A complete. No active TX approved.


---

## EXP239 — Phase B: DCM-HP approval model + crypto triage — COMPLETE WITHIN OPEN EXP239

**Hypothesis**

The 16-byte `071C` controller block and 16-byte `0730` gateway return form the DCM-HP approval gate; successful approval is followed by the controller's settings/state synchronisation and then operational mailbox polling.

**Changed variables**

None on the heat pump. Offline documentation, firmware-string inspection, limited cryptographic candidate testing and public artifact search only.

**Observed facts**

- Official Danfoss HP-kit documentation explicitly lists GateWay states: startup -> `DCM-HP approval` -> distinct approval-failed state -> `sending settings to DCM` -> all OK.
- This order aligns with the external Eco 5 report: repeated `071C/0730` -> first valid response -> FC16/full state sync -> `0708` mailbox.
- Link CC 2.7.42 contains `OML_AES`, `OML_RSA`, `OML_SHA256` and encrypted-file-system strings in `OMService.dll`.
- No obvious AES/Rijndael/CMAC/HMAC/SHA256 strings were found in the audited `RegulationEngine.dll`, `ParameterCache.dll` or `HECTArch.dll` scans.
- AES-128 ECB encrypt/decrypt and AES-CMAC using only zero, FF, and obvious padded ASCII keys (`Danfoss`, `Thermia`, `DanfossLink`, `LinkCC`, `DCM03`) match neither of the two known pairs.
- Exhaustive direct-key scan: all contiguous 16-byte and 32-byte windows of the available Link CC 2.7.42 and 4.2.1724 images were tested as literal AES-128/AES-256 keys for direct ECB encrypt/decrypt and one-block CMAC of C1; zero matches.
- Official instructions show DCM03 can be used in Danfoss Link integration or Danfoss Online mode, making Link-mode DCM03 firmware/hardware relevant to the same HP-facing approval layer.
- Targeted public DCM03/Connect firmware searches did not recover the missing firmware/serializer.
- The vendor install/replacement workflow does not document manual provisioning of a heat-pump/DCM shared secret.

**Strong conclusions**

1. Best current functional interpretation: `071C/0730` is the **DCM-HP approval handshake**.
2. The post-approval bulk FC16 sequence is strongly consistent with the vendor-documented `sending settings to DCM` phase.
3. AES code elsewhere in Link CC cannot be used as evidence for the handshake algorithm.
4. EXP239 still lacks enough challenge/response samples to compute a valid arbitrary response.

**Hypotheses**

- Approval uses a keyed/non-linear transform.
- A manually configured pump-specific secret is less likely, while fixed/vendor, factory, identity-derived or automatically negotiated secrets remain possible.

**Unknowns**

- exact primitive/key;
- deterministic response behavior on repeated challenge;
- cross-boot stability;
- Eco 5 vs XTR key/algorithm compatibility;
- exact first-valid-response -> FC16 sync -> 0708 timings from the raw source capture.

**Negative results**

- obvious AES key candidates negative;
- public firmware search negative;
- no active response candidate approved.

**Status**

EXP239 remains **IN PROGRESS**. Phase B is complete; full-corpus analysis remains blocked on the Eco 5 raw capture/timeline or a DCM03/Connect firmware dump.


---

## EXP240 — Offline DCM03 implementation-locus and firmware-lineage archaeology — COMPLETE

**Hypothesis**

The `071C -> 0730` DCM-HP approval function is implemented in the DCM03 / HP-facing integration layer rather than in the Link CC host, and public product topology can identify the correct recovery target.

**Only experimental variable**

None on the heat pump. Offline documentation/public-artifact analysis only. No YAML change and no bus TX.

**Observed facts**

- DHP-AQ HP-kit `086L2382` contains DCM03, power supply and direct DHP-AQ↔DCM03 cable; the manual connects DCM03 `RS 485` directly to a free relay-board RJ45. No separate GateWay card is part of the AQ kit.
- DHP-H/L/A instead uses a separate internal GateWay card plus DCM03. The documented `DCM-HP approval` and subsequent `sending settings to DCM` state are shown on the GateWay card in this topology.
- Danfoss identifies `086L1602` as the DCM03 gateway module; product catalogues identify kits `086L2381` (DCM) and `086L2382` (DCM AQ).
- Official instructions support switching the DCM03 family between Danfoss Link integration and Danfoss Online mode.
- Historical field reports describe DCM02 incompatibility with a newer Link generation, replacement with DCM03, and same-looking DCM03 devices with differing firmware revisions. Treat this as corroborating field evidence only.
- Public Thermia debug reports expose `dcmVersion=2.0.17` independently from heat-pump program/firmware versions.
- Targeted public searches did not recover a DCM03 firmware image, update package, service loader, or reliable MCU/debug-pad identification.

**Strong conclusions**

1. The DCM03 itself is now the primary firmware-recovery target for the `071C/0730` approval function on DHP-AQ/iTec-like topology.
2. DHP-H/L/A GateWay+DCM03 topology and DHP-AQ direct-DCM03 topology must remain distinct in the model.
3. Link-mode DCM03 firmware remains valuable because the same DCM03 family supports Link and Online modes while preserving the HP-facing interface.
4. `2.0.17` is the best concrete DCM firmware-version search token currently known.

**Hypotheses**

- DCM03 firmware contains the challenge-response primitive/key derivation.
- Approval code may be shared between Link and Online modes.
- Firmware generation may change compatibility/approval details while hardware remains visually similar.

**Unknowns**

MCU, flash layout, update mechanism, key storage/derivation, exact Eco 5 DCM firmware version, and XTR-vs-Eco key-domain compatibility.

**Negative result**

No public firmware binary or actionable hardware-debug identification recovered.

**Next**

Keep EXP239 open. Highest-value artifacts: DCM03 `2.0.17` firmware/service package, DCM03 PCB photos/MCU markings, or the complete Eco 5 raw capture. No active 0730 response approved.


---

## EXP241 — DCM03 version/profile census — COMPLETE / OFFLINE

**Hypothesis**

If the approval routine is a reusable DCM03 function, the same DCM firmware generation should appear across different classic Thermia heat-pump profiles rather than one DCM build per model.

**Observed facts**

Public Thermia Online API fixtures report `dcmVersion=2.0.17` on:

- Diplomat/Diplomat Duo, profile 1001, HP program 1.42;
- ATEC/DHP-AQ, profile 1002, HP program 3.1.1;
- iTec/IQ, profile 1005, HP program 2.4.1.

Newer Calibra NCP profiles 1024/1028 expose null/empty DCM version and do not present the same classic DCM connection metadata. Additional public issues also show DCM 2.0.17 with ATEC program 3.1.0 and an older classic HP program 1.2.0.

**Strong conclusions**

DCM03 2.0.17 is a generic multi-profile firmware generation and is directly relevant to iTec-family installations. A 2.0.17 dump from any classic supported DCM03 is high-value for approval-function recovery.

**Hypotheses**

A reusable approval/crypto routine may be shared across profiles while profile-specific register/state logic is dispatched separately.

**Unknowns**

Eco 5/XTR DCM version, exact key domain, and whether profile dispatch changes the 071C/0730 function.

**Negative result**

No alternative Thermia DCM version or public DCM03 firmware binary was recovered in the targeted corpus.

**Safety**

Offline only; no Thermia TX. EXP239 stays open; EXP238 stays parked.

---

## EXP242 — DCM03 update-path / package archaeology — COMPLETE / OFFLINE

**Hypothesis:** the missing DCM03 `071C -> 0730` approval implementation may be recoverable from a firmware/update package distributed through the Danfoss Link ecosystem.

**Observed facts:**
- Link CC 2.7.42 manifest contains only `ccimage.bin`, CC bootloader/splash, `extern_eep.hex`, `zensys_firmware.hex` and `attiny2313.hex`; no DCM payload.
- Link CC 4.2.1724 manifest contains only `ccimage.bin`, `extern_eep.hex` and `zensys_firmware.hex`; no DCM payload.
- Companion files contain no meaningful `DCM03`, `2.0.17`, `086L1602`, `086L2381/2/3` identifier.
- Official update documentation describes CC update paths and HP-controller minimum versions but no DCM03 flash/update workflow.
- Danfoss release history changes HP-integration behavior in CC software independently of the HP-kit hardware.
- 2014 field reports describe same-looking DCM03 modules with different firmware and replacement/compatibility concerns rather than a user DCM reflash.
- Targeted public search recovered no DCM03 firmware, updater or service-loader package.

**Strong conclusions:** public Link CC firmware packages are not an obvious carrier for DCM03 firmware; a normal consumer DCM03 update path is unsupported by current evidence. Direct DCM03 hardware dump or service/factory tooling is now a higher-value route.

**Hypotheses:** DCM03 firmware may be factory/service programmed; any OTA/service update, if it existed, may use a separate non-public payload/channel.

**Unknowns:** DCM MCU/flash, bootloader/update support, service programmer, key storage, and whether `2.0.17` is fully internal flash.

**Negative result:** no standalone DCM03 `2.0.17` package or loader recovered.

**Next:** EXP243 offline DCM03 hardware/MCU/debug-interface archaeology. EXP239 stays open; EXP238 stays parked. No bus TX.

## EXP243 — DCM03 hardware / MCU / debug-interface archaeology — COMPLETE / OFFLINE

**Hypothesis:** public hardware evidence for DCM03 can identify the MCU/NVM/debug boundary likely to contain the `071C -> 0730` approval transform.

**Observed facts:** Danfoss identifies `086L1602` as DCM03 Gateway; HP-kit docs expose DCM03 `RS 485` and direct AQ RJ45 connection and show the enclosure is mechanically openable. Field evidence independently reports Ethernet/Online behavior and triple-press Z-Wave pairing. Thermia spare-part article **086L2973** is a new useful identifier. Historical same-model/different-firmware DCM03 reports exist, but their original hardware photos are unavailable.

**Strong conclusions:** DCM03 is a multi-interface gateway and remains the primary firmware-recovery locus. A high-resolution internal board image or retired DCM03 is more valuable than further Link CC package archaeology. `086L1602` and `086L2973` should both be used as search keys.

**Hypotheses:** host MCU + RS485 + network + radio subsystem; approval code on host side; identity/key material in internal/external persistent NVM.

**Unknowns:** exact MCU, radio IC, flash/EEPROM, RS485 transceiver, debug/programming interface, readout protection and key storage.

**Negative result:** no readable PCB photo, MCU marking, schematic, JTAG/SWD/UART/ISP pad identification, firmware dump or service programmer recovered.

**Next:** EXP244 archived DCM03 hardware-photo/label recovery. EXP239 stays open; EXP238 stays parked. No bus TX.

---
## EXP244 — Offline XTR 071C structure and recurrence analysis — COMPLETE / POSITIVE

**Hypothesis**

The local XTR `0x0F FC17 read 0x0730/count8 + write 0x071C/count8` payload has enough recurrence and internal structure to determine whether it behaves like a random challenge/nonce, a retry token, a counter/PRNG stream, or a deterministic service/RTC image.

**Method**

Offline only. No Thermia restart, no RS485 TX, no ACK, no FC17 response, no scan, no Home Assistant/YAML change, and no room-sensor emulation.

Directly re-parsed:
- EXP221: 47 exact target frames;
- EXP222: 25 exact target frames;
- EXP225: 32 exact target frames;
- total: 104 local XTR frames.

Older EXP71/EXP71B evidence from EXP226 remains supporting cross-date validation but was not required for the new recurrence statistics.

**Observed facts**

- 104/104 local XTR `071C..0723` payloads are unique; zero exact repeats.
- Median target cadence:
  - EXP221: ~4.277 s;
  - EXP222: ~4.246 s;
  - EXP225: ~4.220 s;
  - combined: ~4.261 s.
- 72 target requests available as complete raw Modbus frames in EXP221+222 are 72/72 CRC-valid.
- The EXP226 RTC encoder reproduces 104/104 locally re-parsed payloads exactly:
  - `071C=(year_since_2000<<8)|hour`
  - `071D=0x4500|(2*second)`
  - `071E=0xF906`
  - `071F=(floor(second/2)<<8)|0xAC`
  - `0720=0xDC00|day_of_month`
  - `0721=0xC500|(4*minute)`
  - `0722=0x001E`
  - `0723=0x8F00|(4*second)`
- On the same-day Sep-26 corpus only 5/16 payload bytes vary; 11/16 remain constant.
- Consecutive local 128-bit images differ by median 6 bits, mean ~6.68 bits, range 2..18.
- Decoded controller time remains ahead of logger time by about +206.3 s across EXP221/222/225.
- The externally reported Eco 5 controller values:
  - `63cefb32c6f41382087992370caceeba`
  - `31fb59fc8fb1175cd89f904d06d92ea4`
  differ from each other by 55/128 bits and match none of the 11 byte positions constant in all 104 local Sep-26 XTR images.
- The external report describes an exact 16-byte retry after roughly one poll when unanswered. No exact retry exists in the local XTR corpus; its RTC-derived image advances every poll.

**Strong conclusions**

1. In the observed local XTR no-Online-endpoint state, `071C..0723` is not a fresh high-entropy 128-bit challenge/nonce. It is a deterministic RTC-derived service image.
2. EXP226 remains valid for the local XTR corpus.
3. The external Eco 5 evidence means the RTC interpretation must not be generalized to all iTec/DCM states or models.
4. The same FC17 bank contract can apparently carry materially different payload regimes.
5. The neutral role description is now:
   - `071C..0723` = controller-owned DCM/service approval input bank;
   - `0730..0737` = external/service-owned return bank.
6. The published Eco 5 responses must not be replayed against the locally observed XTR RTC image.

**Hypotheses**

- The XTR may have a state-dependent encoder: RTC/service bootstrap first, challenge-like approval later.
- Eco 5 and XTR M may use model/firmware-specific payload schemas on the same bank addresses.
- The serializer may be selected by integration/profile/capability state.

**Unknowns**

- Whether this XTR ever enters the high-entropy/retryable 071C mode.
- What `0730..0737` means in the local RTC/service regime.
- Whether the RTC image is itself a validation/MAC input, time-sync bootstrap, or pre-approval service record.
- Whether the externally reported Eco 5 challenge behaviour is confirmed byte-for-byte when the raw log arrives.

**Negative results recorded**

- No local exact 16-byte retry.
- No evidence of a PRNG/high-entropy local 071C generator.
- No basis to replay an Eco 5 response on XTR.
- No active `0730` response approved.

**Next**

EXP245 — offline existing-capture `071C/0730` mode/precondition census.

---
## EXP245 — Existing-capture 071C/0730 mode/precondition census — COMPLETE / STRONG NEGATIVE FOR LOCAL MODE TRANSITION

**Hypothesis**

If the local XTR can enter the externally reported Eco-5-like high-entropy `071C` challenge regime, an existing historical capture may contain either a `071C..0723` payload that violates the RTC encoder or a controller/accessory state transition that changes the payload regime.

**Method / safety**

Offline re-analysis only. No new restart, RS485 TX, ACK, FC17 response, scan, setting change, HA/YAML change or room-sensor emulation.

Directly re-parsed exact local XTR target frames:
- EXP71: 6
- EXP71B: 19
- EXP221: 47
- EXP222: 25
- EXP225: 32
- total: 129

Historical source runs EXP71B and EXP222 did contain their original controlled TX; EXP245 only re-analyses those old logs and does not repeat the actions.

**Observed facts**

1. `129/129` exact target payloads match the EXP226 RTC/service encoder. `0/129` violate it. `0/129` are exact payload retries.
2. First target after explicit bus recovery:
   - EXP221: ~1.219 s after `Bus Healthy -> ON`;
   - EXP222: ~1.179 s;
   - EXP225: ~1.095 s.
3. Median target delay after the immediately preceding 0x06 poll:
   - EXP71: ~0.284 s;
   - EXP71B: ~0.242 s;
   - EXP221: ~0.247 s;
   - EXP222: ~0.247 s.
4. Across 97 frames with explicit preceding 0x06 payloads, the target remains RTC-exact with `AFDC=0x0000`, `0x0010`, and `0x0020`.
5. EXP71B reached `TRUE_BOOTSTATE_CONFIRMED` with `A80E=0x28`, `AFDC=0x10`, five post-boot polls and five transmitted zero responses. One target precedes the marker and 18 follow it; all 19 remain RTC-exact.
6. EXP222 sent six allow-listed `0x0F FC16` ACKs. All 25 target payloads remain RTC-exact. Final counters remained `FC03=0`, `0708=0`.
7. EXP224 later observed zero exact target FC17 transactions in ordinary steady runtime, supporting boot/recovery gating.

**Strong conclusions**

- No existing local XTR evidence contains an RTC -> high-entropy challenge transition.
- `A80E=0x28`, `AFDC=0x10`, `AFDC=0x20`, syntactic 0x06 responder participation, served/accelerated 0x06 scheduling and partial `0x0F FC16` ACKs are **not sufficient** to select the Eco-5-like challenge regime.
- The FC17 target is an early post-boot scheduler slot following 0x06 by roughly a quarter-second.
- EXP244's cross-model two-regime description stands, but the simple local state-transition explanation is weakened.
- Stronger remaining explanations are model/firmware/profile-specific payload generation or an unobserved XTR-specific multi-stage approval prerequisite.

**Hypotheses**

1. Model/firmware/profile-specific encoder on common `071C/0730` role banks.
2. XTR-specific first-stage RTC/service approval, where a correct but unknown `0730` reply may be required before any later state.
3. Hidden persistent integration/binding selector not represented by the already-tested A80E/AFDC/0x06/FC16 states.

**Unknowns**

- Genuine XTR `0730..0737` response in the RTC regime.- Whether XTR ever emits a second challenge-like regime.
- Exact selector/profile difference versus Eco 5.
- Full independent verification of Piotrek's external capture pending raw log.

**Negative results recorded**

- 0/129 local challenge-like frames.
- 0/129 exact retries.
- No transition caused by A80E/AFDC promotion.
- No transition caused by active 0x06 zero responder.
- No transition caused by partial FC16 ACK coverage.
- No active `0730` response justified.

**Next**

Highest value: finish EXP239 from Piotrek's raw Eco 5 capture or obtain an external genuine XTR/iTec Online `0730` response. Otherwise prepare EXP246 as offline XTR RTC/service encoder reconstruction.

---
## EXP246 — XTR RTC/service encoder reconstruction — COMPLETE / OFFLINE POSITIVE

**Hypothesis**

The local XTR `071C..0723` image is a self-contained, redundantly encoded calendar/clock service record rather than merely an RTC-correlated or random challenge block.

**Method**

Offline analysis of the 129 exact local target frames from EXP71, EXP71B, EXP221, EXP222 and EXP225. No new RS485 activity or configuration change.

**Observed facts**

- All 129 frames reduce to the same calendar/time generator.
- Proven:
  - byte0 = year-2000
  - byte1 = hour
  - byte3 = 2*second
  - byte6 = byte3>>2
  - byte9 = day
  - byte11 = 4*minute
  - byte15 = 2*byte3
- Seconds therefore appear as deterministic redundant encodings, not independent values.
- Bytes4/5 are `F9/06` in all 129 and satisfy `F9 XOR 06 = FF`.
- September month 9 matches the low nibble of `F9`; `06` is its nibble complement. Candidate: `byte4=0xF0|month`, `byte5=~byte4`.
- Byte13 is `0x1E=30`, matching September month length.
- The candidate month + month-length generator reproduces 129/129 frames.
- Remaining fixed bytes: `45, AC, DC, C5, 00, 8F`.
- No unexplained dynamic byte remains.
- Controller clock lead changes from about +201 s on Sep22 to +206.35 s on Sep26, consistent with ~1.24 s/day (~14.3 ppm) relative drift if the logger clock is stable.
- The two reported Eco 5 challenge values pass only 1/13 and 0/13 local structural checks.

**Strong conclusions**

1. Local XTR `071C..0723` is best described as a redundantly encoded calendar/clock service record.
2. No hidden per-frame nonce/session entropy is visible in the local 16-byte controller image.
3. The record is structurally self-checking (redundant second encodings; complemented `F9/06` pair), though the exact purpose is unknown.
4. The local image itself does not expose a changing MAC/checksum-like field.
5. Any approval/authentication may therefore be in `0730..0737` or a later stage.
6. Eco 5's reported challenge-like payload is structurally a different regime.

**Hypotheses**

- `F9/06` encodes month 9 plus complement.
- `001E` encodes days in month.
- `45/AC/DC/C5/00/8F` are format/version/signature constants.
- The XTR first approval stage may validate controller calendar/clock state.

**Unknowns**

- Cross-month proof of month/month-length encoding.
- Whether marker bytes depend on year/profile/firmware/DST/timezone.
- Genuine XTR `0730..0737` semantics.
- Whether XTR has a later challenge-like stage.

**Negative results**

- No unexplained dynamic field.
- No local challenge entropy.
- No response synthesis justified.

**Next**

EXP247 — offline reconstruction of the natural unanswered `071C/0730` retry window and timeout/state transition from full raw cold-boot logs.

---
## EXP247 — Boot approval retry-window / timeout reconstruction — COMPLETE / OFFLINE WITH BOUNDED RESULT

**Hypothesis**

Existing full cold-boot logs may reveal the natural unanswered retry duration of the XTR `0x0F FC17 read 0730/count8 + write 071C/count8` service/approval transaction.

**Method / safety**

Offline only. No restart, TX, ACK, FC17 response, setting change, HA/YAML change or room-sensor emulation.

**Observed facts**

- EXP221: 47 exact targets; first 1.219 s after Bus Healthy, last 197.999 s after Bus Healthy, median cadence 4.276 s. Experiment ends only 0.600 s after the last target.
- EXP222: 25 exact targets; last 103.231 s after Bus Healthy; experiment ends 0.930 s later.
- EXP225: 32 exact targets; last 132.649 s after Bus Healthy; experiment ends 1.890 s later.
- All three are right-censored before one expected next target interval.
- EXP71 target traffic continues 15.382 s after its experiment-expired marker.
- EXP71B target traffic continues 2.883 s after its timeout summary.
- EXP221's Thermia power cycle remains continuous until EXP222 is armed ~1599.592 s after the same Bus Healthy transition.
- During the next 419.325 s pre-power-cycle EXP222 observation:
  - 0F FC10 04A6: 237
  - 0F FC10 085F: 119
  - 06 FC17 AFC8: 59
  - 0F FC17 0730: 0
- Thus the target naturally disappears sometime after ~197.999 s but before ~1599.592 s on that passive boot.
- Later steady runtime shows no FC03/0708 activation.

**Strong conclusions**

1. Exact natural timeout is not present in current data.
2. 200 s is not a controller timeout; it is an EXP221 capture boundary.
3. Natural target disappearance is real and occurs before ~26 min 40 s on the continuously observed passive boot.
4. The disappearance is followed by ordinary XTR operation, not Online mailbox activation.
5. Partial FC16 ACKs do not provide evidence for an earlier termination because EXP222 itself is censored.

**Hypotheses**

- Fixed startup retry timer between ~3.3 and ~26.7 min.
- Internal service-state transition rather than fixed timer.
- Model/profile-specific timeout.

**Unknowns**

- Exact final retry time/count.
- Immediate state edge at final retry.
- Determinism across boots.
- Successful genuine XTR `0730` behavior.

**Negative result**

Existing logs cannot recover the exact stop because target-aware logging is absent during the critical interval. Record this as an instrumentation/censoring limitation.
---
## EXP248 — Passive 071C/0730 natural-stop trace — PREPARED / NOT RUN

**Hypothesis**

After one controlled XTR controller cold boot with no genuine Online/DCM endpoint, the exact `0x0F FC17 read 0730/count8 + write 071C/count8` service/approval transaction retries for a finite startup window and then stops naturally. The exact final retry plus contemporaneous `A80E/A80F/AFDC` state may constrain the controller-side stop condition.

**Only experimental variable**

One controlled Thermia/controller cold boot while the ESP/Waveshare stays powered. No heat-pump setting changes.

**Design / controls**

- Fully passive RX-only. No TX-capable UART pin configured; DE held LOW.
- Configuration controls: `EXP248 Arm RX-only Timeout Trace` and `EXP248 Abort`.
- ARM requires fresh ordinary bus traffic and ESP uptime >=15 s.
- Within 60 s of ARM, require a >=6 s bus-silent controller-off gap.
- First CRC-valid frame after the gap marks bus return.
- Log every exact 071C/0730 target in brown with target number, time since bus return, inter-target delta, A80E/A80F/AFDC snapshot, and full 16-byte write image.
- Log A80E/A80F/AFDC changes in brown. Major state markers are red.
- A natural-stop candidate requires >=3 targets, >=20 s target silence, and continued healthy bus traffic.
- Confirm only after another 60 s without a target. A reappearing target records `FALSE_STOP` and resumes observation.
- Hard limit 35 min after bus return.

**Expected outcomes**

- Success: `SUMMARY CONFIRMED_STOP` identifies exact last target and post-stop state.
- Inconclusive: `CENSORED_35MIN`, no qualifying boot gap, <3 target frames, or parser integrity loss.

**Safety**

No ACK, FC17 response, probe, scan, semantic write, room-sensor emulation or automated heat-pump restart. Production functionality is otherwise preserved.

**Status**

Prepared only; no result assumed until the user returns the full ESPHome log.
---
## EXP248 — Passive natural-stop trace — VALID RUN / STOP CANDIDATE OBSERVED / FINAL CONFIRMATION TAIL MISSING

**Hypothesis**

After a controlled XTR controller cold boot with no genuine Online/DCM endpoint, the exact `071C/0730` service/approval transaction retries for a finite window and then stops naturally.

**Observed facts**

- Initial setup attempt correctly auto-aborted because no power cycle occurred; no protocol result.
- Valid run: bus gap detected 14:57:53.961; BUS_RETURN 14:58:01.042.
- First target at 1.283 s after return.
- Early states progress through `A80E 0000->0008->0028`, `AFDC 0000->0010`, and `A80F 0005->000A`; retry stream continues unchanged.
- 63 exact targets are observed.
- Final target `n=63`: 267.123 s after return, `A80E=0028 A80F=000A AFDC=0010`.
- Cadence remains ~4.29 s until the final target; no backoff or slowdown is visible.
- STOP_CANDIDATE occurs after 20.793 s target silence while the rest of the bus remains live.
- No target reappears in the supplied tail; target age reaches at least 53.5 s.
- Parser remains clean with zero resyncs and zero RX drops.

**Strong provisional conclusion**

A natural abrupt target stop is very strongly supported at ~267.1 s after BUS_RETURN and is not associated with bus loss or a visible A80E/A80F/AFDC transition.

**Hypotheses**

- fixed startup timer near 270 s; or
- fixed retry/slot budget yielding 63 observed requests; or
- hidden internal service-state deadline not exposed in A80E/A80F/AFDC.

**Unknown / completion status**

The supplied log does not include the configured 60 s confirmation after STOP_CANDIDATE and contains no `SUMMARY CONFIRMED_STOP`. EXP248 therefore remains IN PROGRESS rather than COMPLETE. About 26 s of confirmation tail is missing from the supplied excerpt.

**Safety**

RX-only; no ACK, no FC17 response, no semantic write, no room-sensor emulation.

---
## EXP248 — Passive 071C/0730 natural-stop trace — COMPLETE / VALID PASSIVE POSITIVE

**Hypothesis:** the XTR retries the unanswered `071C/0730` startup/service transaction for a finite
window and then stops naturally.

**Attempt 1 — aborted setup/control**
- ARM: 14:55:38.670
- no controller power-cycle / no >=6 s bus gap
- AUTO_ABORT: 14:56:38.968
- no protocol result; guard correctly failed closed.

**Attempt 2 — valid complete run**
- ARM: 14:57:25.491
- BUS_GAP: 14:57:53.961
- BUS_RETURN: 14:58:01.042
- first target: +1.283 s
- targets: 63
- last target: +267.123 s
- median cadence: 4298.0 ms
- last state: `A80E=0028 A80F=000A AFDC=0010`
- STOP_CANDIDATE: 20.793 s after final target
- `SUMMARY CONFIRMED_STOP`: final silence 80.793 s
- false stops: 0
- resync delta: 0
- drop delta: 0
- 0x06 polls: 86

**Observed facts**
- early state progression completes within ~11.3 s but target retries continue;
- no A80E/A80F/AFDC change coincides with the final request;
- ordinary bus traffic continues after target disappearance;
- cadence remains ~4.29 s with no backoff through the final request.

**Strong conclusions**
1. Natural disappearance of the local XTR target stream is directly confirmed.
2. Last request occurs at +267.123 s after BUS_RETURN.
3. The stop is not a bus-loss artifact.
4. EXP247's broad timing bound is superseded for this boot.
5. No response value or Online-mailbox activation was learned.

**Hypotheses**
- ~270 s controller startup deadline is the leading timing hypothesis;
- fixed retry budget remains possible;
- stop condition may live in an unobserved internal state.

**Unknowns**
- repeatability across boots;
- exact internal deadline versus retry count;
- genuine XTR `0730` semantics.

**Next:** EXP249 passive repeatability run, same instrumentation, no TX.

---
## EXP249 — Passive 071C/0730 stop repeatability trace — PREPARED / NOT RUN

**Hypothesis**

EXP248's natural target stop is primarily a repeatable ~270 s startup/service deadline rather than an incidental hidden-state transition.

**Controlled change**

Only one variable changes: a second controlled Thermia/controller cold boot. The ESP remains powered and the EXP248 RX-only instrumentation, stop-candidate threshold, confirmation window and hard ceiling are unchanged.

**EXP248 baseline**

- first target: +1.283 s after BUS_RETURN
- target count: 63
- median cadence: 4.298 s
- last target: +267.123 s
- final monitored state: `A80E=0028 A80F=000A AFDC=0010`
- confirmed target-free silence: 80.793 s

**Success / discrimination**

- Strong timer support: EXP249 last target falls within one normal retry interval (~4.3 s) of +267.123 s, with bus alive and no monitored state edge explaining the stop.
- Same target count and similar first-target timing strengthen the fixed-window model further.
- Similar count but materially different absolute stop time favors retry-budget/scheduler-phase behavior.
- Materially different count and time favors a hidden/state-dependent stop condition.

**Safety**

RX-only. GPIO17 TX absent; GPIO21 DE LOW. No ACK, `0730` response, scan, setting change, room-sensor emulation or production-function change.

**Status**

PREPARED / NOT RUN.

---
## EXP249 — Passive 071C/0730 stop repeatability trace — COMPLETE / VALID PASSIVE POSITIVE

**Hypothesis**

EXP248's natural target stop is governed by a repeatable startup/service mechanism.

**Observed facts**

- first target: +1.283 s;
- targets: 63;
- median cadence: 4293 ms;
- last target: +266.821 s;
- final state: `A80E=0028 A80F=000A AFDC=0010`;
- confirmed final silence: 80.974 s;
- 0x06 polls: 87;
- false stops: 0;
- parser resync delta: 0;
- RX drop delta: 0.

**Comparison with EXP248**

- first-target timing: identical (+1.283 s);
- target count: identical (63);
- last-target timing: 302 ms earlier in EXP249;
- median cadence: EXP248 4298 ms, EXP249 4293 ms;
- monitored final state: identical;
- meaningful early monitored state transitions reproduce within 11 ms.

**Strong conclusions**

1. The local unanswered `071C/0730` lifecycle is highly deterministic across cold boots.
2. The natural stop is reproducible in both time and request count.
3. A80E/A80F/AFDC do not expose the stop trigger.
4. There is no retry backoff.

**Hypotheses**

- ~270 s deadline remains the leading timing model.
- fixed 63-request budget remains equally compatible with current evidence.
- hidden deterministic service state remains possible.

**Unknowns**

- timer versus counter;
- hidden cutoff state;
- genuine XTR `0730` semantics.

**Negative result**

Repeatability alone does not distinguish timer from fixed retry budget.

**Next**

EXP250 — RX-only raw-frame differential around the deterministic ~267 s cutoff.

---
## EXP250 — Offline 0730..0737 response-structure classification — COMPLETE / NO TX

**Hypothesis**

The two genuine Eco 5 `0730..0737` blocks are better modeled as one opaque 128-bit response than as
eight independent status/control words.

**Observed facts**

- R1 = `1691 A5F3 F8E8 D587 3892 4416 E8E6 A3D5`
- R2 = `FD63 6CCD 0F92 1D83 FF23 2A1A 2413 B372`
- 8/8 response word positions differ.
- No response word position is fixed.
- No common small Thermia status/control constants occur in the 16 observed words.
- C1->R1 Hamming distance = 65/128.
- C2->R2 Hamming distance = 62/128.
- R1->R2 Hamming distance = 68/128.

**Strong conclusion**

Treat `0730..0737` as an opaque 16-byte approval/response blob for emulator design. There is no
evidence-backed per-word semantic interpretation.

**Hypotheses**

A keyed/nonlinear authenticator remains compatible with the data; packed/obfuscated structure is not
excluded.

**Unknowns**

Exact algorithm/key/state, installation specificity, determinism for repeated challenge, and whether
XTR M shares the Eco 5 response function.

**Negative result**

No safe word-level `0730` field can be extracted from the two pairs.

**Safety**

Offline only; no TX.

**Next**

EXP251 shadow DCM emulator/oracle harness with TX disabled by default.

---
## EXP251 — Shadow DCM / approval harness — PREPARED / NOT RUN

**Hypothesis**

The known iTec Online/DCM lifecycle can be represented locally with one opaque unresolved
`071C -> 0730` response hook while the rest of the controller/gateway traffic is classified in a
shadow state machine.

**Controlled change**

Only experiment instrumentation changes from EXP249. The Thermia connection remains RX-only and
known-good production parsing/entities are preserved.

**Classifier scope**

- exact local approval request;
- 071C RTC/service decode;
- Hamming distance to the two reported Eco 5 source challenges;
- peer FC17 16-byte candidate response;
- 0x0F FC16 request / peer ACK;
- 0x0F FC03 0708 mailbox;
- other 0x0F FC03 page reads;
- A80E/A80F/AFDC and 0x06 context.

**Safety**

No TX pin, DE forced LOW, no ACK/response/scan/write. The genuine Eco 5 response values are not
stored in this YAML.

**Status**

PREPARED / NOT RUN.

---
## EXP251 — Shadow DCM / approval harness — VALID STOP CANDIDATE / FINAL CONFIRMATION PENDING

**Hypothesis**

The Online/DCM lifecycle can be classified in a receive-only shadow state machine around one opaque
unresolved `071C -> 0730` response boundary.

**Observed facts**

- first approval +1.287 s;
- 63 approval requests;
- median cadence 4178 ms;
- last approval +261.347 s;
- final state `A80E=0028 A80F=000A AFDC=0010`;
- peer FC17 16-byte responses: 0;
- peer FC16 ACKs: 0;
- 0708 mailbox requests: 0;
- STOP_CANDIDATE after 20.044 s silence with bus alive;
- one parser resync at the boot-return edge;
- RX drops 0.

**Comparison**

EXP248/249 both had 63 requests with ~4.29 s cadence and final target near +267 s. EXP251 again has
63 requests but cadence is ~4.178 s and the final request is +261.347 s.

**Strong conclusion**

A fixed 63-request retry budget is now a better model than a simple +270 s deadline. At EXP251's
cadence, requests 64 and 65 would nominally occur before +270 s, but neither appears.

**Negative results**

No approval response, no FC16 peer ACK and no 0708 mailbox transition.

**Status**

Not formally complete: `SUMMARY SHADOW_COMPLETE` is missing from the uploaded tail.

---
## EXP251 — Shadow DCM / approval harness — COMPLETE / VALID RX-ONLY POSITIVE

**Hypothesis**

The Online/DCM lifecycle can be classified passively around an unresolved opaque `071C -> 0730`
approval boundary.

**Final summary**

`SUMMARY SHADOW_COMPLETE approval=63 first=1287ms last=261347ms final_silence=80044ms
peer17=0 fc16req=424 fc16ack=0 mailbox0708=0 fc03other=0 s06=87
A80E=0028 A80F=000A AFDC=0010 changes[A80E=3 A80F=3 AFDC=2]
false_stops=0 resync_delta=1 drop_delta=0 TX=DISABLED`

**Observed facts**
- full 60 s stop confirmation completed;
- exactly 63 approval attempts;
- faster median cadence than EXP248/249;
- no peer FC17 response, peer FC16 ACK, 0708 mailbox, or other FC03 page read;
- normal bus remains alive;
- one parser resync occurred at the boot-return edge only.

**Strong conclusions**
1. The fixed 63-attempt retry-budget model now leads over a simple fixed ~270 s timer.
2. Controller-originated FC16 traffic is not evidence of approval/session success.
3. No downstream Online/DCM state appears without an approval response.
4. A80E/A80F/AFDC do not expose the retry cutoff.

**Negative results**
- no approval response;
- no peer FC16 ACK;
- no 0708 mailbox;
- no monitored stop edge;
- one startup-edge parser resync.

**Status**

COMPLETE.

---
## EXP252 — One-shot 0730 approval oracle (Eco 5 R1) — PREPARED / NOT RUN

**Hypothesis**

A single known genuine Eco 5 16-byte return value may discriminate whether the XTR `0730` gate
performs strict challenge-dependent validation or reacts to a broader cross-profile service token.

**Only active variable**

Exactly one FC17 response to the first qualifying local `071C/0730` request:

`1691 A5F3 F8E8 D587 3892 4416 E8E6 A3D5`

No second response is possible in the experiment.

**Known provenance**

The value belongs to external Eco 5 challenge
`63CE FB32 C6F4 1382 0879 9237 0CAC EEBA`, not to the local XTR RTC/service request.

**Safety**

Explicit arm, cold-boot qualification, exact-request guard, RTC-schema guard, controller-state guard,
peer-response inhibit, post-return parser/drop guard, pre-TX latch, one physical TX frame only, then
observation only.

**Status**

PREPARED / NOT RUN.

**Provisional UI observation**

Immediately after the one-shot R1 response, the front-panel UI shows a literal `0` adjacent to the
DHW tank icon. No alarm text is visible; the screen shows `GEEN WARMTEVRAAG` and `BEDRIJF AUTO`.

Interpretation remains unknown. Do not infer `0 °C` or a changed DHW setting from this display alone.

---
## EXP252 — One-shot 0730 approval oracle — COMPLETE / ACTIVE POSITIVE / ALARM SIDE EFFECT

**Observed facts**
- exactly one R1 response transmitted;
- approvals=1, after_tx=0 through full observation;
- no peer FC17 response, no peer FC16 ACK, no 0708 mailbox and no other FC03 page request;
- clean parser/RX after BUS_RETURN;
- new `0` appeared beside the front-panel DHW/tank icon;
- after summary, A80E fell `0x28 -> 0x20 -> 0x00` and AFDC fell `0x10 -> 0x00`;
- front-panel alarm message: **`COMM. ERR ONLINE/LINK`**.

**Strong conclusions**
1. R1 is not ignored; it suppresses/terminates the local approval retry sequence.
2. Full Online/DCM authentication remains unproven.
3. The active response has a nontrivial controller-visible side effect: the controller raises
   `COMM. ERR ONLINE/LINK`, strongly tying the side effect to the Online/Link integration path.
4. This is not, by itself, evidence of a direct heating/DHW process fault.

**Safety decision**
HOLD all further active `0730` tests. Capture alarm code, then restore known-good passive operation and
verify recovery.

---
## EXP253 — Offline post-approval session reconstruction — COMPLETE / NO TX

**Hypothesis**

Reference Online/DCM captures can reveal the first downstream endpoint obligations missing after
EXP252 R1.

**Observed facts**
- capture 090550 contains 31 unanswered `0870/count17` controller FC16 writes before the endpoint
  begins ACKing;
- the same pre-transition period contains 16 unanswered `0708/count6` polls;
- first `0870` ACK is followed by a `0708` response `0000 0000 7FFF FFFF 0080 0007`;
- a broad FC16 sync burst starts immediately afterwards and is ACKed;
- established captures repeatedly serve `0708` with `...0006` idle/service images.

**Strong conclusion**

A real endpoint does substantially more after becoming present than EXP252 did. The later
`COMM. ERR ONLINE/LINK` is compatible with an incomplete endpoint/session.

**Unknown**

Local XTR post-approval sequence may differ from the reference topology.

**Next**

EXP254 passive recovery + local 0870/0708 baseline census.

---
## EXP254 — Passive recovery + 0870 baseline census — PREPARED / NOT RUN

**Hypothesis**

A clean no-responder reboot restores normal local behavior, and passive observation can determine
whether `0870/count17` and/or `0708/count6` belong to the XTR baseline.

**Safety**

RX-only; no TX path.

---
## EXP254 — Passive recovery + 0870 baseline census — PROVISIONAL / RUNNING

**Observed so far**
- clean bus gap and return;
- first approval +1.283 s;
- 23 approval requests through +94.787 s;
- recent cadence ~4.240 s;
- familiar A80E/A80F/AFDC startup progression restored;
- no `0870/count17`;
- no `0708/count6`;
- no peer FC16 ACK.

**Provisional conclusion**

The controller has returned to the normal local unanswered approval baseline. The reference
`0870/0708` cycle is not present in the first ~95 s of this passive XTR boot.

**Status**

RUNNING — wait for final summary.

---
## EXP254 — Passive recovery + 0870 baseline census — COMPLETE / VALID PASSIVE POSITIVE

**Hypothesis**

A clean no-responder boot restores local XTR baseline behavior and reveals whether reference
`0870/count17` / `0708/count6` traffic is ordinary XTR baseline activity.

**Observed facts**
- 63 approval requests;
- first +1.283 s;
- median 4.241 s;
- last +265.086 s;
- `fc16_0870=0`;- `fc16ack=0`;
- `polls0708=0`;
- final `A80E=0028 A80F=000A AFDC=0010`;
- `resync_delta=0`, `drop_delta=0`, TX disabled.

**Strong conclusions**
1. passive reboot restores the known local XTR approval baseline;
2. the 63-attempt model is further strengthened;
3. `0870/count17` and `0708/count6` are absent throughout the passive XTR trace;
4. the late A80E/AFDC fall-back is normal baseline lifecycle, not an EXP252 R1-specific effect.

**Negative result**
No reference-topology `0870/0708` traffic was observed locally.

**Next**
Candidate EXP255: same one-shot R1 as EXP252, but log every post-R1 FC16/FC03 address/count and send
no downstream ACK/response. Require visual recovery from EXP252 first.

**Recovery-procedure clarification**

The heat pump/controller was manually restarted after the EXP252 `COMM. ERR ONLINE/LINK` alarm.
Accordingly, EXP254 proves recovery **after reboot** to the normal passive XTR protocol baseline; it
does not prove that the alarm/session state self-clears without a reboot.

---
## EXP255 — Passive full 0x0F FC16/FC03 baseline census — PREPARED / NOT RUN

**Hypothesis**

A complete passive census is required before attributing any post-R1 FC16/FC03 address to the active
approval state.

**Reason**

EXP254 proved `0870/count17=0` and `0708/count6=0`, but did not log all other FC16/FC03 pairs.

**Variables changed**

Instrumentation only:
- log every `0x0F FC16` request start/count;
- log every `0x0F FC03` request start/count.

**Safety**

RX-only; no TX path.

**Recovery note**

The user confirms that after the manual post-EXP252 controller restart, both
`COMM. ERR ONLINE/LINK` and the DHW-side `0` disappeared.

**EXP255 provisional live result**

At ~+66 s after BUS_RETURN:
- approvals=16;
- FC16 requests=84;
- FC03 requests=0;
- FC16 baseline families observed:
  - `04BA/count22` x4 (startup only so far);
  - `04A6/count13` x51;
  - `085F/count5` x29.

No TX, parser resyncs or RX drops. Run remains in progress.

---
## EXP255 — Passive full 0x0F FC16/FC03 baseline census — COMPLETE / VALID

**Hypothesis**

Map the complete passive local XTR FC16/FC03 baseline before another R1 test.

**Observed facts**
- approvals=63; first=1284 ms; last=265513 ms; median cadence=4241 ms;
- FC16 total=582; FC16 ACK=0; FC03 request=0; FC03 response=0;
- only three FC16 families:
  - `04BA/count22` x4;
  - `04A6/count13` x383;
  - `085F/count5` x195;
- no parser resync or RX drop; TX disabled;
- FC16 continues after approval retry exhaustion.

**Strong conclusions**
1. These three families are the complete seven-minute passive XTR FC16 baseline.
2. No passive local FC03 phase occurs.
3. FC16 runtime traffic is independent of the 63-attempt approval retry loop.

**New hypothesis from EXP252 comparison**
EXP252 R1 total FC16=386 versus EXP255 passive=582; delta=196. Since passive `085F/count5` alone is
195, R1 may selectively suppress `085F/count5`. This is not yet proven because EXP252 did not log
FC16 addresses.

---
## EXP256 — One-shot R1 + FC16/FC03 differential census — PREPARED / NOT RUN

**Hypothesis**

The same one-shot R1 used in EXP252 selectively changes the local FC16 distribution, with
`085F/count5` disappearance as the leading discriminator.

**Only active variable**

Same already-tested single R1 response; no new target/value.

**Instrumentation change**

Log every FC16 and FC03 start/count.

**No downstream emulation**

No FC16 ACK, FC03 response, second FC17 response, mailbox response or desired-state response.

**Recovery plan**

After the 7-minute summary, perform one normal controller reboot to clear the known recoverable
Online/Link side effect; do not wait for the alarm.



---
## EXP256 — One-shot R1 + FC16/FC03 differential census — COMPLETE / ACTIVE STRONG POSITIVE

**Hypothesis**

The same one-shot R1 used in EXP252 changes the local post-approval FC16/FC03 distribution; the leading pre-test hypothesis was selective suppression of `085F/count5`.

**Observed facts**
- one exact R1 response sent at approval request #1, +1245 ms after BUS_RETURN;
- approval requests=1, retries after TX=0;
- FC16 total=390, FC16 ACK=0, FC03 `0708/count6`=0, other FC03=0;
- complete FC16 census: `04BA/count22` x1 before R1, then `03E8/count14` x389; `04A6/count13` x0; `085F/count5` x0;
- first `03E8/count14` arrived +124 ms after R1 and the same block was retransmitted until the 7-minute summary because no ACK was supplied;
- final summary: `A80E=0028 A80F=000A AFDC=0010`, `resync_postreturn=0`, `drop_postreturn=0`, `DE=LOW`;
- UI: DHW/tank-side literal `0` reappeared; VERSION screen unchanged; after summary the front panel again raised **`COMM. ERR ONLINE/LINK`**, exactly matching EXP252.

**Strong conclusions**
1. The pre-test “only `085F` is suppressed” hypothesis is rejected.
2. R1 advances the XTR out of the 071C/0730 approval retry state into the native `03E8/count14` controller->endpoint synchronization stage.
3. With no endpoint FC16 ACK, the controller stalls on and retransmits the first `03E8` sync block.
4. Full Online/Link session establishment is not proven because no downstream FC03/mailbox phase occurred.
5. The `0` + alarm side effect is reproducible across the R1 runs and remains recoverable by the planned normal controller reboot unless new evidence shows otherwise.

**Unknowns**
- exact semantic meaning of the DHW-side `0`;
- the exact first post-`03E8` block in this approval context once the expected FC16 ACK is supplied.

**Safety / next step**
Perform one normal controller reboot now. Do not run another active approval/sync experiment until the UI has returned to normal. Candidate EXP257: one-shot R1, ACK only exact `03E8/count14`, observe the first next block, and do not ACK any newly appearing block.


---
## EXP257 — One-shot R1 + single `03E8/count14` ACK + next-stage capture — PREPARED / NOT RUN

**Hypothesis**

EXP256 proved that one exact R1 response ends the local approval retry loop and enters repeated `0x0F FC16 03E8/count14`. EXP257 tests the smallest next active discriminator: ACK exactly the first post-R1 `03E8/count14` once and observe the first different FC16 or FC03 stage.

**Only new active variable**

One standard FC16 ACK for request `0x0F FC16 start=03E8 count=14`, and only when that request is the first post-R1 FC16. Exact ACK frame: `0F1003E8000EC093`. No register-value payload is introduced.

**Known target / prior evidence**

- EXP256: first `03E8/count14` arrived 124 ms after R1 and repeated for the full run without an ACK.
- EXP137: ACK of exact `03E8/count14` locally advanced the controller to `0410/count22`.
- Therefore `0410/count22` is a candidate next stage, not an assumed result.

**Fail-closed guards**

- same guarded one-shot R1 as EXP252/EXP256;
- no approval retry after R1;
- first post-R1 FC16 must be exact `03E8/count14`, bytecount 28, length 37;
- request must arrive within 5 s of R1;
- parser/RX-drop counters unchanged since BUS_RETURN;
- no unexpected peer FC17 or FC16 ACK;
- ACK latch closes before DE.

**No downstream emulation**

No second `03E8` ACK, no ACK of any newly appearing FC16 block, no FC03 response, no second R1, no mailbox response and no desired-state response.

**Observation / stop**

Capture the first different post-ACK FC16 or any FC03 and stop immediately without answering it. If only `03E8` retries continue, stop after 15 s and record the negative result.

**Recovery**

Run only after EXP256 alarm/UI recovery is complete. Reboot the Thermia controller once immediately after the EXP257 capture/summary.

**Build validation**

YAML parse passed; substitutions and `id(...)` references are complete; bus-health refresh remains unchanged. ESPHome compile was not run because the ESPHome CLI is unavailable in the execution environment.


## External iTec Eco 5 full gateway capture — analysed before EXP257

Source is a complete 1482.480 s raw gateway capture, not a local XTR experiment. It materially refines the expected downstream Online/DCM sequence.

Observed:
- 99 approval FC17 requests in three retry windows: 29 + 41 + 29.
- retry medians approximately 4.24 s, 4.26 s and 4.21 s.
- 98/99 challenge payloads unique; one duplicate.
- successful pair 1: `63CEFB32C6F41382087992370CACEEBA -> 1691A5F3F8E8D58738924416E8E6A3D5`.
- successful pair 2: `31FB59FC8FB1175CD89F904D06D92EA4 -> FD636CCD0F921D83FF232A1A2413B372`.
- both success cycles reproduce the same prefix: `R -> 03E8/14 -> ACK -> 03FC/11 -> ACK -> 0410/22 -> ACK`.
- in both cycles `03E8/14` begins 92 ms after the FC17 response.
- first-cycle timing: `03FC` +510 ms, `0410` +1.950 s.
- second-cycle timing: `03FC` +536 ms, `0410` +2.189 s.
- the first cycle continues through a long ordered FC16 export chain ending at `06F4/19`, after which `07D0/19` and `0708/count6` mailbox/runtime traffic appear.
- the capture begins in an already-established state where `0708/count6` polls receive responses and runtime FC16 pages such as `0820`, `0834`, `0848`, `0864` and `0870` are acknowledged.

Decision for EXP257:
- keep the same one-shot R1 + one exact `03E8/14` ACK boundary;
- change only the diagnostic expectation: first different post-ACK block is now expected to be `03FC/count11` by genuine Eco 5 reference;
- do not ACK `03FC` in EXP257.