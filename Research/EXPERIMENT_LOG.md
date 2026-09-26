# THERMIA EXPERIMENT LOG

Last updated: 2026-09-26

This file is the compact canonical experiment record. Detailed YAML and raw logs remain the primary evidence.

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
| **EXP99** | Historical-field matrix, REQ low | **PREPARED.** Ten 8 s phases testing AFC9, AFCB and historical combinations; AFCA=0000 throughout |

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

**Comparison:** EXP165 = 0x0F ACK alone negative; EXP166/167 = valid runtime 0x06 presence negative; EXP168 = valid 0x06 + exercised 0x0F 03E8/14 ACK negative.

**Negative result retained:** stop repeating simple `0x06` + `0x0F` transport-role combinations.

**Next:** offline analysis of genuine DCM transmitter ownership / service activation before EXP169. No controller reboot required.


## EXP169–182 — scheduler/topology branch

| Experiment | Purpose | Result |
|---|---|---|
| EXP169 | Exercise native `042E/count15` ACK activation candidate | **Inconclusive** — target condition not exercised |
| EXP170 | Exercise `03E8 -> 0410 -> 042E` ACK chain | **Inconclusive** — pre-existing `04A6` retry state confounded sequence |
| EXP171 | Correct genuine boot/rejoin capture roles and ordering | **Positive offline correction** — extended scheduler exists controller-side while DCM service can still be silent |
| EXP172 | Compare controller `A7F8/A80C..A812` fingerprints | **Structural difference found** — correlation only |
| EXP173 | Test whether live `0x06` presence changes fingerprint/scheduler | **Negative** |
| EXP174 | Heat Curve A/B/A fingerprint/scheduler census | **Negative** |
| EXP175 | Passive reference-vs-local topology census | **Positive structural split** — reference A5/A4/05 + FC03 scheduler absent locally |
| EXP176 | Evaluate `0x0559 Link Integration` as scheduler gate | **Offline negative** |
| EXP177 | Guarded direct `0x0F FC16 03E8/count14` semantic write | **Negative** — no controller semantic change |
| EXP178 | AFCA + FC16-ACK-context mailbox trigger reproduction | **Negative** — historical 0861 ACK not reproduced |
| EXP179 | AFCA without FC16 ACK context | **Inconclusive** |
| EXP180 | Exact LONG→zero→SHORT AFCA phase reproduction | **Valid negative** |
| EXP181 | Same phase with historical 5 ms response delay | **Valid negative** — stop timing variants |
| EXP182 | Complete genuine-DCM `0708/count6` mailbox census | **Complete / positive offline mapping** |

### EXP182 key result

Five genuine `0708/count6` response classes are currently observed:

- steady: `0000 0000 0000 0000 077F 0006`;
- command pending: `0000 0001 0000 0000 077F 0006`;
- controller-boot transient: `0000 0000 0000 0000 0080 0006`;
- later controller-boot transient: `0000 0000 0000 0000 0000 0006`;
- DCM rejoin: `0000 0000 7FFF FFFF 0080 0007`.

The two observed `word1=1` events are each followed ~40 ms later by controller `FC03 03E8/count13`.

The DCM-rejoin variant instead causes controller FC16 resynchronisation beginning at `03E8`.

**Negative result retained:** decoding or spoofing `0708` is not itself a local control solution because the local XTR does not currently emit the `0708` scheduler.

**Current stop rule:** no EXP183 active write/probe until a specific evidence-backed scheduler/topology activation candidate is identified.


## EXP183–185 — offline architecture / firmware branch

| Experiment | Purpose | Result |
|---|---|---|
| EXP183 | Reconstruct cyclic `07D0..0884` scheduler and payload sources | **Positive** — ordered ACK-gated state-export serializer reconstructed |
| EXP184 | Cross-model source/export mapping | **Positive offline refinement** — semantic export layer above model-specific source slaves |
| EXP185 | Raw 2.7.42 firmware call-chain and partial-update group reconstruction | **Positive** — exact groups 0/1/2 and IntegrationMode lifecycle recovered |

### EXP185 key result

Raw `dlcc_2.7.42` firmware was recovered and inspected directly. Exact HPNode partial-update membership:

- group 0: HeatPumpType, OperationMode, IntegrationMode, RoomValue, ExternalControl1/2/3, DefrostDemand, AlarmField1..5, ErrorCode;
- group 1: HeatCurve, HeatCurveMin, HeatCurveMax, HeatCurvePlus5, HeatCurveZero, HeatCurveMinus5, HeatStop, RoomFactor, HotWaterStart, ControllerDemand, OperationStatus;
- group 2: OutdoorTemperature, AuxiliaryHeaterPowerStage, HotWaterTemperature, SupplyLineTemperature, ReturnLineTemperature, EVU_SW, EVU_HW.

`set_IsSystemIntegration` is called from persisted/default-setting paths (`Load`, `CopySettings`, `SetDefaultSettings`), not directly from `OnHEServiceBind` in the recovered RegulationEngine call graph.

**Strong conclusion:** IntegrationMode governs higher-level synchronization ownership and full grouped resync; it is not proven to activate the controller's extended Modbus scheduler.

**New hypothesis:** `0708 word1=1` may be a partial-group-1 dirty/command selector because firmware group 1 starts with HeatCurve and the genuine controller immediately fetches `03E8/count13`. Do not promote this to proven until another selector value/group is observed.

**Stop rule:** no guessed local IntegrationMode write. Continue passive/offline until cold-boot A/B or another genuine selector event provides a scheduler/group discriminator.



## EXP186 — 0708 selector reconstruction — COMPLETE / PARTIAL POSITIVE
Hypothesis: w0/w1/w2 are direct selectors for semantic sync groups 0/1/2.

Result:
- `w1=1` occurred exactly twice in the genuine command capture;
- both were followed by `FC03 03E8/count13`;
- no independent command-state `w0!=0` or `w2!=0` was observed;
- the rejoin `w2=7FFF` state is compound and triggers full resync.

Conclusion: w1 is strongly associated with the heating/settings desired-state family; full three-way selector mapping remains unproven.

## EXP187 — 03E8/count13 versus firmware group 1 — COMPLETE / NEGATIVE FOR EXACT 1:1 MAPPING
Hypothesis: `03E8/count13` directly serializes the eleven Danfoss Link group-1 parameters.

Result:
- native block spans `03E8..03F4` = 13 contiguous wire registers;
- confirmed/native semantics overlap heavily with Link group 1, especially HeatCurve through HeatStop and RoomFactor;
- however the wire image also contains room-setpoint-related/native fields and cannot be matched one-to-one to the eleven semantic group-1 parameters.

Conclusion:
retain the broader interpretation `0708.w1 -> heating/settings family pending`; do not claim exact `w1 -> PartialUpdateIndex 1` identity without another genuine group event.


## EXP188 — Raw firmware binding/topology reconstruction — COMPLETE / POSITIVE

Hypothesis: the Link firmware can show whether SystemIntegration is a discovery/binding gate or a later application setting.

Observed:
- HEATPUMP identity maps to DivisionID 6 / BrandID 0 / ProductID 0x0203.
- DHP binding validates physical address plus allowed DivisionID/BrandID/ProductID before creating an endpoint.
- HEATPUMP endpoint creation leads to HPNode.
- The service UI directly sets HPNode.IsSystemIntegration from a user-selectable radio button.

Result: positive.

Strong conclusion: SystemIntegration is a Link-side application/ownership setting applied after endpoint binding, not the discovered scheduler-enable mechanism for the local Thermia controller.

Negative result retained: do not design a local Modbus experiment around guessed IntegrationMode activation.

Next: scheduler/topology activation remains an independent controller-side problem; await/prepare the genuine DCM-connected versus absent cold-boot discriminator.


## EXP189 — physical-topology latch analysis — COMPLETE / POSITIVE

Hypothesis: genuine boot/rejoin captures can show whether the extended scheduler is created by the first DCM mailbox/ACK exchange or exists earlier.

Observed:
- 090209 controller boot with DCM already powered: reference 0x02 topology fingerprint from the first visible frame (~0.031 s), C8 ~0.130 s, slave 0x04 request/response ~0.251/0.290 s, first 0x0F FC16 ACK ~0.389 s, A5 operational ~1.179 s, first 0708 only ~33.18 s.
- 090550 DCM rejoin: extended 0x02/0x04/A5/0x0F scheduler and unanswered 0708 polls persist while DCM service is silent for ~66 s.
- local EXP164 no-DCM boot: C8, 0x06 and ordinary 0x0F FC16 exist, but A4/A5/05 and 0x0F-FC03 remain absent.

Strong conclusion: topology creation precedes normal mailbox operation and is not explained by the first 0x0F ACK. Once active, the extended topology remains latched across temporary DCM silence.

Next: no active EXP190. Highest-value evidence is same-controller cold boot with DCM connected versus absent.


## EXP191 — cross-model outdoor-node mapping — COMPLETE / POSITIVE

Hypothesis: reference 0x04 and local 0x1E are model-specific source nodes feeding the same higher-level outdoor/COMM-KIT semantics.

Observed:
- reference genuine captures: continuous 0x04 FC17 traffic, zero 0x1E frames in the checked corpus;
- local XTR EXP175: 0x04 absent, 0x1E strongly active;
- 07E4/count17 follows and repacks the 0x04 exchange, including FC18->FF9C normalization and inserted/derived values.

Conclusion: the DCM runtime exporter is semantic, not a fixed raw-slave mirror. 0x04 and 0x1E are likely architecture-specific implementations of the same broad subsystem role, but their register maps are not interchangeable.

Negative result: no evidence supports interpreting A812=0500 as a slave/node map or direct 0x05 presence encoding. Do not write or decode it that way without independent evidence.


## EXP192 — remaining runtime-export semantic mapping — COMPLETE / POSITIVE

Hypothesis: additional `07F8..0884` blocks are semantic datasets, not raw fixed-slave mirrors.

Observed:
- `07F8` penultimate word tracks the first 0x0A B3C4..B3C6 controller-write value across independent captures: 17 on 2026-09-24 and 14 on 2026-09-25.
- `0848` words16..22 are proven `[second,minute,hour,day,month,year,weekday]` from real-time progression and date/day-of-week consistency.
- `0884/count60` = ten 6-word reverse-chronological timestamped records; best interpretation is event/history table, codes unresolved.
- `0870` is invariant across all genuine captures and DCM silence; static/persistent dataset in observed corpus.
- `0864` is invariant `[0,0,0,22]`; meaning unknown.
- `080C` and `0834` remain unresolved; first words 0x00C8 and 0x001E are not enough to claim slave-source identity.

Conclusion: the DCM runtime serializer contains live state, clock/calendar, persistent/identity and history datasets in separate blocks. It is a semantic export database rather than a simple bus mirror.


## EXP193 — semantic dataset classification — COMPLETE / MIXED POSITIVE-NEGATIVE

Hypothesis: leading values `00C8` in `080C` and `001E` in `0834` may identify direct C8/0x1E source slaves.

Observed:
- `080C` is present in steady captures with no C8 traffic, rejecting a raw-C8 interpretation.
- `0834` is present in the reference topology even though no 0x1E frames occur, rejecting a raw-0x1E interpretation.
- `080C word14` tracks controller 0x06 write field AFDC across independent captures: 0/0 in steady captures and 16/16 in 090209 boot.
- `0834 word12=70` in steady captures but 0 in controller boot even while A5 still exposes the apparent 30/70 values; direct A5 mirror rejected.
- `0848` current RTC/date mapping remains proven.
- `0884/count60` is ten 6-word reverse-chronological records and matches Thermia's documented ten-entry alarm-history model (type/time/date).

Conclusion: the runtime layer is a semantic export database; first-word numeric resemblance is not source-slave identity. `080C` includes 0x06 lifecycle/accessory state; `0834` remains unresolved; `0884` is strongly identified as alarm history.

Safety: offline only, no TX/YAML change.


## EXP194 — 0864/0870 configuration-vs-runtime analysis — COMPLETE / MIXED

**Hypothesis:** `0870` and/or `0864` may encode product/commissioning identity relevant to the Online/DCM scheduler gate.

### Observed
- `0870 = decimal 2160`, count17 = 2160..2176.
- Public Thermia Online debug profiles map 2160/2162/2163/2166..2169 to operating-time counters and 2171..2173 to defrost statistics.
- Genuine 0870 payload maps coherently: compressor 21966 h; heating 9763 h; cooling 10 h; hot water 12091 h; aux1 124 h; aux2 170 h; aux3 0 h; defrost count 3122; between-defrost value 422.
- Independent numerical validation: `9763+10+12091=21864` versus compressor `21966`; and `21966*60/3122=422.15`, matching index2172=422.
- `0864 = decimal 2148`, count4 = 2148..2151; payload always `[0,0,0,22]` in checked genuine occurrences.
- Public ATEC/iTec/NCP Online profiles expose no 2148..2151 labels.
- 0864 begins exactly after the native/local `085F/count5` range 2143..2147, which contains 0861.

### Result
- **0870: strongly identified as operational lifetime + defrost statistics. Negative as scheduler/identity candidate.**
- **0864: unresolved but structurally interesting as a hidden continuation adjacent to 085F/0861.**

### Safety
No active local write. Do not infer 22 = firmware 2.2 and do not write 2148..2151.



### EXP194 refinement — Online registerIndex database architecture

Converting the cyclic runtime FC16 starts to decimal exposes the same namespace used by Thermia Online:

```text
07D0 = 2000
07E4 = 2020
07F8 = 2040
080C = 2060
0820 = 2080
0834 = 2100
0848 = 2120
085F = 2143
0864 = 2148
0870 = 2160
0884 = 2180
```

This changes the preferred interpretation of the runtime scheduler from a collection of private export commands to a controller-side publisher that populates the DCM-facing Thermia Online `registerIndex` database in slave `0x0F`.

**Strong conclusion:** `0864` is controller->DCM exported state at indices 2148..2151. Even if one field later correlates with topology/capability, it is an output/reflection and not a justified scheduler-enable write target.

**Negative result retained:** `0870` is removed from identity/scheduler-gate hypotheses; it is operational lifetime + defrost statistics.

**Next proposed work:** EXP195, offline only, reconstruct `085F..0867` as one adjacent service/status family.



## EXP195 — 085F/0864 adjacent service-family reconstruction — COMPLETE / POSITIVE-NEGATIVE

**Hypothesis:** 085F/count5 and 0864/count4 may be one contiguous service/status family exposing scheduler activation.

**Observed:**
- steady genuine Online: 0864 appears once per runtime cycle; 085F absent;
- 090209 controller boot: 085F occurs after the large startup sync, then runtime starts; 0864 appears later in the normal runtime cycle;
- 090550 DCM rejoin: DCM join response at 68.235 s starts full resync; 085F then repeats every ~4.2 s throughout the resync; 0708 mailbox polling is mostly suppressed; runtime restarts with 07D0 at 106.828 s;
- local no-DCM XTR already emits 085F and uses 0861 inside that page as the AFCA transport ACK;
- local no-DCM does not show the genuine steady 0864 runtime page.

**Result:**
- 085F = synchronization/service-control class, not steady Online runtime data;
- 0864 = extended steady-runtime export page;
- adjacency 2143..2151 is address-space adjacency, not one scheduler role.

**Negative result:** neither page is a credible scheduler-enable write target. Full resync starts before the first rejoin 085F, and 0864 appears only later as runtime output.

**Next:** retain same-controller genuine DCM present/absent cold-boot A/B as highest-value discriminator.



## EXP196 — public Online-index cross-map — COMPLETE / POSITIVE

**Hypothesis:** public Thermia Online registerIndex metadata can directly identify fields inside unresolved runtime pages.

**Observed:**
- ATEC/DHP-AQ and iTec IQ profiles both map index 2060 to `REG_INDOOR_TEMPERATURE` with 0.1 scaling.
- Genuine `080C/count18` starts exactly at index 2060 and word0 is consistently 200.
- Therefore `080C.word0 = indoor temperature 20.0 °C` is strongly supported.
- This disproves the earlier superficial `00C8 -> slave C8` reading.
- Public 2120-region semantics differ by model/profile (ATEC 2120 Integral LSD; iTec 2120 PID), so Online-index semantics are not universally identical across all controller families.
- No checked public profile exposes 2143..2151.

**Conclusion:** the DCM runtime pages are confirmed to inhabit the same Thermia Online registerIndex database used by public Online API profiles, but mapping must remain model-aware and field-specific.

**Safety:** offline only; no writes.



## EXP197 — genuine 0559 Link Integration gate test — COMPLETE / STRONG NEGATIVE

**Hypothesis:** extended Online/DCM scheduler requires `0559 REG_LINK_INTEGRATION = 1 (SYSTEM)`.

**Observed:**
- genuine full-sync `0546/count20` spans 0546..0559;
- both 090209 controller boot and 090550 DCM rejoin export identical values;
- `0553 = 4`, consistent with the public OperationMode enum;
- `0559 = 0`;
- public ATEC/DHP-AQ Online metadata defines 0559: 0 LIGHT, 1 SYSTEM;
- extended A5/0x04/0708/runtime scheduler is definitely active in both captures.

**Result:** strong negative for 0559=SYSTEM as the scheduler/topology gate.

**Conclusion:** Link Integration mode is an application ownership/sync choice above the already-active transport topology. Do not write 0559 to try to create the scheduler.



## EXP198 — 06EA/06F1/06F4 startup-tail analysis — COMPLETE / POSITIVE-NEGATIVE

**Hypothesis:** the final startup/full-sync pages contain identity/capability state that activates the Online/DCM scheduler.

**Observed:**
- `06EA/count7` decodes exactly as RTC/date: sec,min,hour,day,month,year,weekday. Cross-capture timing and the later 0848 RTC tail independently validate it.
- `06F1/count3` is `FFFF,FFFF,FFFF` in both genuine power-event captures.
- `06F4/count19` occurs in controller cold boot (090209), but not in the indexed DCM-rejoin capture (090550).
- 06F4 first five words exactly mirror contemporaneous 0x02 write fields A80C..A810.
- Reference-only A811/A812 values 000C/0500 are not included in those first copied fields.
- extended topology is already active long before 06F4 appears.

**Result:** no scheduler-enable token found. 06EA is RTC, 06F1 unresolved/unavailable, 06F4 is a late controller-boot snapshot.

**Safety:** offline only. No write to 06EA..0706.



## EXP199 — Link firmware node-model / DCM identity check — COMPLETE / POSITIVE-NEGATIVE

**Hypothesis:** `SIMPLE_COMMUNICATION_MODULE` or another Link node type may be the DCM bridge and expose its identity/binding requirements.

**Observed:**
- HEATPUMP = NodeType17; Division6/Brand0/Product0x0203.
- SIMPLE_COMMUNICATION_MODULE = NodeType19; Division5/Brand0/Product0x8100.
- GATEWAY = NodeType16; Division7/Brand0/Product0x0201.
- SCMNode carries binary input state, input-shift count, power-cycle counter and check-in interval; its delayed callback raises AwayModeChanged.
- recovered node-type model contains no explicit DCM/Online/Connect node.

**Result:** SIMPLE_COMMUNICATION_MODULE is not the DCM bridge.

**Conclusion:** DCM is best treated as a lower transport/service bridge beneath the Link application node model. Link binds the heat pump endpoint, not a separate DCM application node.

**Safety:** offline only.



## EXP200 — exact XTR DCM presence/Online status semantics — COMPLETE / POSITIVE

**Hypothesis:** XTR documentation distinguishes the local DCM-recognition state from Internet/cloud status.

**Observed:**
- exact iTec XT/XTR user guide defines DCM ACCESSORY INSTALLED as DCM/Thermia Connect connected;
- separately defines ONLINE CONNECTION as accessory connected plus Internet connection;
- older DHP-AQ HP-kit installation connects DCM03 directly to the spare relay-board RJ45, starts the heat pump, then pairs it in Link CC, without a documented heat-pump enable toggle;
- Link-vs-Online selection is performed on DCM03 itself in that older kit.

**Result:** positive.

**Conclusion:** the scheduler-gate search should target the XTR's local accessory-recognized/topology state, not cloud connectivity or Link Integration ownership mode. A811/A812 remain a passive candidate reflection only.

**Safety:** no TX/YAML change.



## EXP201 — A811/A812 versus XTR DCM-installed state — COMPLETE / PARTIAL POSITIVE

**Hypothesis:** A811/A812 may reflect the XTR's documented DCM-accessory-installed state.

**Observed:**
- local no-DCM = FFFF/0000;
- genuine extended topology = 000C/0500;
- active local 0x06 accessory/version service does not change the local pair;
- all 102 controller 0x02 requests in 090550 retain 000C/0500 before, during and after the DCM silent->responding transition.

**Result:** partial positive as a persistent installed/topology/capability correlate; negative as a live DCM-session marker.

**Conclusion:** retain A811/A812 as the strongest passive topology reflection, not as a write target and not yet as a proven UI-icon field.



## EXP202 — public register search for DCM-installed / Online-connection state — COMPLETE / NEGATIVE-POSITIVE

**Hypothesis:** XTR DCM-installed state is an ordinary public Online register.

**Observed:**
- no DCM-installed or Online-connection registerName found in checked ATEC/iTec/Diplomat/NCP public debug profiles;
- DCM appears as device metadata (dcmVersion, deviceConnectionType);
- COMP_HAS_LINK exists only at model-specific high indices (6003/7003/10003) and is 0 in checked DCM-connected profiles.

**Result:** negative for a simple public Online register; positive for layer narrowing.

**Conclusion:** prioritize private controller/display state, especially A811/A812, rather than additional 0x0F public-register hunting.

**Safety:** offline only.



## REVIEW EXP183–EXP202 — evidence-grade audit (not a new experiment)

Authoritative corrections after rechecking the offline branch:

- EXP183–188: core findings retained. EXP186/187 already correctly downgraded the exact partial-group mapping.
- EXP189: topology is proven to be **runtime-maintained through DCM service silence/rejoin**, not proven persistent/nonvolatile across controller boots.
- EXP190: A811/A812 remain a structural discriminator; read-count 15/13 as generation/layout is hypothesis only.
- EXP191: 0x04 <-> 0x1E equivalence is hypothesis; semantic/model-aware export is the retained conclusion.
- EXP192: 0870 "static/config/identity" interpretation is superseded by EXP194 operating-time/defrost mapping.
- EXP193: 080C.word14 <-> AFDC is a correlation; direct 0x06 provenance remains unproven.
- EXP195: 085F = service/status page active locally and during resync; exact initialization/control role remains unknown.
- EXP196: 2060 indoor-temperature mapping is strong, not independently proven on the reference UI.
- EXP199: retract categorical "SCM is not DCM". Firmware shows SCM binary-input/Away semantics, but no source proves or excludes DCM03=SCM.
- EXP200: XTR DCM-installed vs Online-connected distinction retained; DHP-AQ no-toggle installation sequence is corroborating only.
- EXP201: reclassify to **INCONCLUSIVE for DCM-installed mapping / STRONG NEGATIVE for live DCM-session marker**.
- EXP202: public-register search negative retained; private controller/display location remains hypothesis.

No TX, YAML or production-functionality changes were made during this review.


## EXP203 — causal-frontier / first-divergence analysis — COMPLETE / POSITIVE

**Hypothesis:** existing cold-boot data may still contain the transition that enables the extended Online/DCM topology.

**Observed:**
- local EXP164 no-DCM: t=0 first bus return on 0x1E; 0F 04BA at 317 ms; first logged 0x02 fingerprint at 722 ms already read-count15 and A811/A812=FFFF/0000; C8 at 818 ms; 0x06 at 1045 ms; no A4/A5/05/FC03 over 180 s.
- genuine 090209: first visible frame at 31 ms is already the reference 0x02 fingerprint, read-count13 and A811/A812=000C/0500; C8 130 ms; 0x04 251/290 ms; ACKed 0x0F FC16 389 ms; A5 1179 ms.
- genuine 090550: topology remains active while DCM service is silent, then DCM rejoins at ~68.235 s.

**Result:** the present corpus contains no same-controller topology OFF->ON transition.

**Strong conclusion:** current cross-system fingerprints cannot identify a causal gate. In the reference boot, topology selection is already reflected by the first observable controller frame. Further late-frame mining cannot recover an event that is not present in the capture.

**Stop rule:** do not promote A811/A812, read-count differences, 0x0F pages or 0708 fields to activation causes without same-controller differential evidence.

**Next:** same-reference-controller DCM-present/absent cold-boot A/B, or controller-side firmware/service-software reverse engineering.



## EXP204 — controller firmware/service-software source hunt — COMPLETE / NEGATIVE-POSITIVE

**Hypothesis:** actual heat-pump controller/relay-board firmware may be publicly/project-available and reveal DCM topology selection.

**Observed:**
- no usable iTec XTR / iTec / DHP-AQ controller firmware binary or update package found in Project/Library/public web/GitHub searches;
- public XTR sources are manuals/commissioning/wiring/product documents;
- official DHP-AQ Link material requires controller software >=2.2;
- official compatibility documentation says older DHP-AQ units should have the display card changed if below 2.2.

**Result:** negative for currently available controller firmware; positive evidence that Link/DCM capability can depend on controller/display-card software generation.

**Conclusion:** stop treating Link CC firmware as a likely source of the Thermia-bus scheduler gate. Cold-boot A/B remains more valuable than further Link-side firmware mining.

**Safety:** offline only.


## EXP205 — physical-layer / dedicated-detect audit — COMPLETE / NEGATIVE-POSITIVE

**Hypothesis:** DCM presence may be detected through a dedicated non-RS485 RJ45 pin or hardware strap.

**Observed:**
- observed XTR RJ45 wiring uses all eight conductors for duplicated data, ground and +12 V;
- official DHP-AQ HP-kit wiring connects spare relay-board RJ45 directly to DCM03 RS 485, with DCM03 powered separately;
- no documented extra detect/ID wire or jumper exists on that direct DHP-AQ path;
- controller software >=2.2 is required for DHP-AQ Link support;
- active reference topology survives temporary DCM service silence.

**Result:** negative for a documented dedicated spare-wire detector; physical/electrical detection on the RS485 pair itself remains unresolved.

**Conclusion:** prioritize early protocol/persistent capability evidence over speculative wiring tricks. No physical bus-loading experiment.
