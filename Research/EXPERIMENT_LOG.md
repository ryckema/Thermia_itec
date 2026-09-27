# THERMIA EXPERIMENT LOG

Last updated: 2026-09-27

This file is the canonical experiment record. The compact table below indexes the early experiment series; EXP100+ are documented in the detailed chronological sections that follow. Detailed YAML and raw logs remain the primary evidence.

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
- FC16 map includes 1350..1369 with 1363=4 and 1369=0;
- public semantics identify those as Operation Mode and Link Integration.

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

## EXP233 — Offline FC17 page-schema analysis — COMPLETE / STRUCTURAL POSITIVE, FIELD-HOMOLOGY NEGATIVE

**Hypothesis**

The repeated Thermia FC17 +0x14 read/write-bank spacing might also imply common request/feedback field positions and thereby constrain one or more XTR 0730..0737 words.

**Observed facts**

The same 20-register page stride exists across multiple roles, including 0x02, 0x04, 0x05, 0x06, 0x0A and the XTR 0x0F 071C -> 0730 pair. Known semantic fields do not occupy one universal relative position: room-sensor command, accessory transport strobe and version metadata all use different locations/feedback paths.

**Strong conclusion**

+0x14 is a generic FC17 bank/page convention, not evidence that 0730 word positions share semantics with 0708, AFCA or B3B1. Eight zero words are not proven neutral. No active 0730 response approved.

**Negative result**

Reject field-position copying and all-zero 0730 synthesis.

---

## EXP234 — Offline service-page archaeology — COMPLETE / NEGATIVE IN ACCESSIBLE INDEXED CORPUS

**Hypothesis**

Named schemas or genuine response data for decimal pages 1800/1820/1840 (0708/071C/0730) may exist in available maps, source artifacts or repositories.

**Observed facts**

No named XTR schema, field labels or genuine 0x0F FC17 0730/count8 response were recovered from the accessible indexed corpus. The then-available Part9 raw-byte path was inaccessible.

**Strong conclusion**

The indexed corpus did not supply an evidence-backed 0730 response image.

**Negative result**

No TX justified.

---

## EXP235 — Offline topology-transferability audit — COMPLETE

**Hypothesis**

The genuine ATEC/DHP-AQ DCM scheduler may be directly reproducible on the local XTR.

**Observed facts**

Reference traffic continuously uses 0x04, A5 and 0x0F FC03. The local XTR runtime uses 0x1E and lacks that scheduler family. The 0x02 fingerprints also differ in active read span and A811/A812 values.

**Strong conclusion**

The reference DCM path remains valuable architecture evidence, but it is not a wire-identical local implementation target.

---

## EXP236 / EXP236A / EXP236B — Local UI causality and cross-setting export audit — COMPLETE

**Hypothesis**

The controller-originated 0x0F FC16 page carrying a changed setting may be the semantic ingress itself.

**Observed facts**

- Heat Curve physical UI changes are exported in 03E8.
- Activate Cooling physical UI changes are exported in 0442.
- Operation Mode AUTO -> COMPRESSOR -> AUTO changes 0553 from 1 -> 2 -> 1 inside 0546/count20.
- EXP177 had already shown that replaying a native-looking 03E8 image toward 0x0F does not create the Heat Curve semantic change.

**Strong conclusion**

0x0F FC16 is a broader controller-owned configuration/state serialization layer. The semantic mutation occurs upstream of these exports.

**Negative result**

Do not use page-specific FC16 mirror writes as the primary local write ingress.

---

## EXP237 — Passive Heat Curve UI ingress trace — COMPLETE / VALID BOUNDED NEGATIVE

**Hypothesis**

A physical Heat Curve 36 -> 37 -> 36 change produces a reversible bus event before the first target-valued 03E8 export if semantic ingress crosses the monitored RS485 segment.

**Observed facts**

- Target 03E8=37 appeared ~2.4 s after the +1 marker.
- The first target 03E8=36 restore appeared ~4.8 s after the restore marker; an earlier 03E8 frame still contained stale 37.
- The recognized pre-target frames were routine known traffic.
- Parser resync/drop counters remained zero.
- The EXP237 parser explicitly whitelisted common function codes, so proprietary/unknown-function bytes could have been dropped before frame-level logging.

**Strong conclusion**

No distinct reversible Heat Curve ingress event was found in the parser-recognized standard traffic before controller export.

**Method correction**

Target-value-aware transition detection is required; the first page after a UI marker may be stale.

**Unknown**

Raw UART activity outside the parser's function-code whitelist remains unexcluded.

---

## 2026-09-27 — Genuine DCM mailbox/rejoin re-audit — OFFLINE

Across the four genuine captures, 54 exact 0x0F FC03 0708/count6 polls were identified. Thirty-eight have valid responses and sixteen early rejoin polls are unanswered.

Observed state classes include:

- normal runtime: 070C=077F, 070D=0006;
- rejoin/transition: 070A=7FFF, 070B=FFFF, 070C=0080, 070D=0007;
- other snapshot phases with 070C=0000 or 0080 and 070D=0006.

Both and only the two observed 0709=0001 responses are followed immediately by controller FC03 03E8/count13 desired-state reads. The next 0708 poll clears 0709 again.

In the 090550 rejoin capture the first successful 0708 response is followed ~69 ms later by a large ordered 0x0F FC16 state snapshot. Regular 0708 polling pauses during that long snapshot and resumes afterward with the normal idle image.

Strong conclusions:

1. 0709 is a proven command-pending discriminator in the reference DCM architecture.
2. 0708 is a multi-purpose mailbox/lifecycle page.
3. 070C=0080 is not simply "snapshot active".
4. Desired-state and controller state export can use the same serialized page representation; direction/ownership is essential.
5. For XTR 0730, status/session/dirty-selector semantics are now a stronger architectural hypothesis than "the changed setting value lives directly in this eight-word bank". No word-level transfer is justified.

---

## EXP234B — Offline raw-binary completion of EXP234 — COMPLETE / NEGATIVE FOR XTR 0730 SERIALIZER IN LINK CC HOST

**Hypothesis**

The raw Danfoss Link CC 2.7.42 firmware may contain the missing local DCM03 -> Thermia serializer or named 0708/071C/0730 service-page constants.

**Method**

Read-only extraction of the original Windows CE ccimage.bin, including managed DHP/regulation assemblies and native HECTArch.dll. Exact constants and CLR method ownership were audited.

**Observed facts**

- ParameterCache.dll contains the real abstract DHP stack and parameter IDs including 0x030A OperationMode, 0x4402 HeatCurve and 0x4414 IntegrationMode.
- ParameterCache/Regulation code contains no service-page implementation for 071C/0730.
- The apparent 0708 constants in RegulationEngine map to ordinary decimal-1800 constructor/timing values.
- Full-ROM ownership mapping places remaining exact 071C/0730 constants in unrelated UI/framework code.
- HECTArch exposes HE/Z-Wave ServiceBind/ServiceSetGet/HESetGetReqRsp functionality and no identifiable local Thermia 0708/071C/0730 serializer.

**Strong conclusion**

The audited Link CC host stack stops at the abstract DHP -> HE/Z-Wave boundary. The missing XTR local-service translation belongs to another component, most plausibly Thermia Connect/DCM-side firmware or the heat-pump Gateway/controller.

**Negative result**

Do not spend an active experiment on guessed 0730 values derived from Link CC.

**Current continuation point**

Last completed bus experiment remains EXP237. EXP238 is PREPARED / NOT RUN and is temporarily parked while the DCM-replacement/software-artifact line is pursued.


---

## External reference evidence — genuine Thermia Online on iTec Eco 5 — MATERIAL ARCHITECTURAL UPDATE

**Source status**

Third-party capture described by piotrek_r. Raw log and timeline script are stated to be available on request but have not yet been ingested into this project. Treat the following as externally reported observations pending independent raw-log verification.

**Capture**

- 10,719 frames
- all CRC valid
- 1482 s
- A/B/A sequence: gateway attached -> gateway absent -> gateway attached

**Observed facts reported**

1. Every FC17 request to 0x06 and 0x0A is unanswered through the full capture (326 and 325 requests respectively, ~4.2 s cadence).
2. No A5, A4 or 0x05 traffic appears on this iTec.
3. Controller repeatedly issues 0x0F FC17 read 0730/count8 + write 071C/count8 from power-on.
4. With the gateway attached, the gateway eventually answers after roughly two minutes / two gateway boot cycles.
5. After the first valid 0730 response:
   - the FC17 071C/0730 exchange stops;
   - controller begins acknowledging FC16;
   - controller dumps full state over decimal 1000..1780 and 2000..2160;
   - controller begins polling mailbox decimal 1800 / hex 0708.
6. With gateway absent, the transition never occurs and ordinary 0x0F writes remain unacknowledged.
7. Roughly 90 distinct controller 16-byte values were seen across two clock hours; they do not fit the project's prior RTC/calendar transform.
8. One exact 16-byte controller value repeats about four seconds later as an unanswered retry.
9. Two complete 16-byte controller/request -> gateway/response pairs were supplied:
   - 63cefb32c6f41382087992370caceeba -> 1691a5f3f8e8d58738924416e8e6a3d5
   - 31fb59fc8fb1175cd89f904d06d92ea4 -> fd636ccd0f921d83ff232a1a2413b372
10. After successful session establishment, app-originated changes use the 0708 mailbox:
   - mailbox second word 1 triggers FC03 decimal 1000 count14;
   - mailbox second word 8 triggers FC03 decimal 1070 count15;
   - physical-display changes are exported by controller FC16 without mailbox involvement.

**Strong conclusions**

- The 071C/0730 FC17 pair is a genuine iTec Online/session gate.
- The older ATEC A5/A4/0x05 topology is not required for iTec Online operation.
- The reference 0708 mailbox architecture is transferable to iTec **after** the 071C/0730 gate succeeds.
- The prior EXP226 RTC/calendar interpretation of 071C..0723 is no longer supportable as a general semantic model and must not constrain future work.
- DCM replacement can now be decomposed into two layers: first solve the 16-byte 071C->0730 handshake, then emulate the mailbox/desired-state service.

**Hypotheses**

- 071C write data is a challenge/session nonce and 0730 is a deterministic authenticated response.
- The 16-byte block size and noise-like values are compatible with a block-cipher/MAC-style primitive, but this is not yet proven.
- The second mailbox word may be a dirty-page/command bitmask because distinct values 1 and 8 select different desired-state page families.

**Unknowns**

- Exact handshake algorithm and key/material.
- Whether identical challenges always produce identical responses.
- Whether response depends on unit pairing/subscription history, gateway identity or installation-specific secret state.
- Whether XTR M uses the identical challenge/response primitive as Eco 5.
- Exact semantics of mailbox selector bits beyond the observed examples.

**Negative/correction recorded**

Do not use the old RTC/calendar transform to construct 071C/0730 responses. Do not brute-force 128-bit response data.

**Next**

Request and ingest the raw Eco 5 capture plus timeline script for offline challenge/response analysis before any new active TX experiment.

---

## EXP239 — 071C -> 0730 challenge/response analysis — OPEN / OFFLINE

**Hypothesis:** the externally reported genuine iTec Eco 5 `071C` 16-byte controller values and `0730` gateway values form a reproducible approval/session response.

Observed genuine pairs:

```text
63cefb32c6f41382087992370caceeba -> 1691a5f3f8e8d58738924416e8e6a3d5
31fb59fc8fb1175cd89f904d06d92ea4 -> fd636ccd0f921d83ff232a1a2413b372
```

Offline analysis rules out fixed XOR, fixed 128-bit add/subtract, fixed per-byte additive masks, fixed rotation+XOR, byte-permutation+fixed-mask families, and common unkeyed digest truncations. Direct AES-ECB/AES-CMAC tests using obvious keys and exhaustive contiguous 16/32-byte windows from the inspected Link CC images produced zero matches.

**Strong conclusion:** the relation is non-trivial and compatible with a keyed/nonlinear construction, but no specific primitive is proven.

**Negative result:** no arbitrary XTR `0730` response can be calculated from current evidence. No active response is approved.

---

## EXP240 — DCM03 implementation-locus / firmware-lineage archaeology — COMPLETE / OFFLINE

**Hypothesis:** product topology can identify which device most likely implements the HP-facing approval function.

Official DHP-AQ documentation shows DCM03 connected directly by RS485 to the heat-pump relay board. Older H/L/A systems use a separate Gateway card, so those topologies must not be conflated.

**Strong conclusion:** for DHP-AQ/iTec-like direct topology, DCM03 itself is the primary firmware-recovery target for the HP-facing approval/session behavior.

Product token anchors include DCM03 module `086L1602` and AQ kit `086L2382`. Public API/debug examples expose DCM version separately from heat-pump firmware, with `2.0.17` recurring.

**Negative result:** no usable public MCU/debug-interface identification was recovered in this experiment.

---

## EXP241 — DCM03 version/profile census — COMPLETE / OFFLINE

Public classic-profile fixtures show DCM **2.0.17** across materially different systems, including Diplomat/Duo, ATEC/DHP-AQ and iTec/IQ profiles.

**Strong conclusion:** DCM03 2.0.17 is a generic multi-profile classic DCM firmware generation and is a high-value recovery target.

This does not prove identical wire protocol, keying or secrets across all installations.

---

## EXP242 — DCM03 update-path / package archaeology — COMPLETE / OFFLINE NEGATIVE

Public Danfoss Link CC packages and official update documentation were audited for a standalone DCM03 image or field-update path.

The inspected manifests contain Link CC image, EEPROM, bootloader, Z-Wave and small auxiliary firmware payloads, but no identifiable DCM03 firmware image. Direct token searches for DCM03/version/product IDs were negative.

**Strong conclusion:** no evidence-backed normal public end-user DCM03 firmware update path is known.

**Negative result:** no DCM03 2.0.17 binary, updater or service loader recovered.

---

## EXP243 — DCM03 hardware/MCU/debug archaeology — COMPLETE / OFFLINE NEGATIVE / PARKED

Public documentation confirms DCM03 identity/topology but did not yield a readable internal PCB photograph, MCU identification, schematic or credible debug/programming interface.

**Negative result:** no actionable hardware debug path recovered. This line is parked to avoid drifting away from the direct protocol blocker.

---

## EXP244 — Local XTR 071C structure/recurrence analysis — COMPLETE / OFFLINE POSITIVE

104 exact local XTR `0x0F FC17 read 0730/count8 + write 071C/count8` requests were directly re-parsed from EXP221/222/225.

Observed:
- 104/104 payloads unique;
- zero exact retries;
- ~4.26 s median cadence;
- only a small subset of bytes changes between adjacent frames;
- the prior local RTC/calendar encoder reconstructs 104/104 frames exactly.

**Strong conclusion:** in the observed local XTR no-Online-endpoint state, `071C..0723` is deterministic RTC/service data, not a fresh high-entropy 128-bit challenge.

The externally reported Eco 5 regime is structurally different. Do not generalize either interpretation across all models/states.

---

## EXP245 — Existing-capture 071C mode/precondition census — COMPLETE / OFFLINE STRONG NEGATIVE FOR LOCAL MODE TRANSITION

The historical local corpus was expanded to **129 exact target frames** across EXP71, EXP71B, EXP221, EXP222 and EXP225.

Observed:
- 129/129 match the local RTC/service encoder;
- 0/129 are challenge-like;
- 0/129 are exact retries;
- the RTC regime persists through tested A80E/AFDC promotion, an active historical 0x06 zero responder, and partial 0x0F FC16 ACK participation.

**Strong conclusion:** ordinary tested local boot/accessory state progression does not switch the XTR from RTC mode to the externally reported Eco 5 challenge-like mode.

---

## EXP246 — XTR RTC/service encoder reconstruction — COMPLETE / OFFLINE POSITIVE

The local 16-byte block is better described as a **redundantly encoded calendar/clock service record**.

Proven dynamic structure includes:
- year-2000;
- hour;
- day-of-month;
- 4x minute;
- three deterministic second encodings.

`F9 06` is an exact complemented pair and is a strong September month/complement candidate. `001E` is a strong September days-in-month candidate. Those two roles remain cross-month hypotheses.

**Strong conclusion:** there is no unexplained per-frame entropy inside the local 16-byte controller record.

---

## EXP247 — Boot approval retry-window / timeout reconstruction — COMPLETE / OFFLINE BOUNDED RESULT

Historical captures prove the unanswered target stream eventually disappears naturally, but all dedicated target captures were right-censored.

For the continuous passive EXP221 boot:
- target still active after ~198 s;
- target already absent by ~1600 s when later target-aware logging resumed on the same power cycle.

**Negative result:** exact timeout could not be reconstructed from existing historical logs.

This directly motivated a long RX-only capture.

---

## EXP248 — Passive 071C/0730 natural-stop trace — COMPLETE / VALID PASSIVE POSITIVE

**Hypothesis:** the unanswered local XTR startup/service target stream retries for a finite window and then stops naturally.

Attempt 1:
- armed at 14:55:38.670;
- no power-cycle occurred;
- boot-gap guard auto-aborted after 60 s;
- no protocol result; fail-closed control behaved correctly.

Attempt 2:
- ARM 14:57:25.491;
- BUS_GAP 14:57:53.961;
- BUS_RETURN 14:58:01.042;
- first target +1.283 s;
- **63 target requests**;
- median cadence **4298 ms**;
- last target **+267.123 s** with `A80E=0028 A80F=000A AFDC=0010`;
- STOP_CANDIDATE after 20.793 s target silence;
- SUMMARY CONFIRMED_STOP after **80.793 s** final silence;
- `false_stops=0`, `resync_delta=0`, `drop_delta=0`;
- 86 observed 0x06 polls.

**Observed fact:** ordinary bus traffic remains active after the last target.

**Strong conclusions:**
1. the local XTR `071C/0730` startup/service stream has a genuine natural stop;
2. the stop is not caused by bus loss;
3. no visible A80E/A80F/AFDC edge coincides with the final request;
4. there is no gradual retry backoff.

**Hypothesis:** an approximately 270 s startup/service deadline is the leading timing model because the next normal target slot would have been expected around +271.421 s.

**Unknown:** timer versus retry budget versus hidden internal state.

**Next:** EXP249 passive repeatability run using the same instrumentation and one additional cold boot. No TX.

