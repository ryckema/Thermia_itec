# THERMIA PROJECT STATE

Last updated: 2026-09-26

## Authoritative experiment state

## Authoritative current state — 2026-09-26 (supersedes older current-experiment bullets below)

- Last completed experiment: **EXP182 — COMPLETE / POSITIVE OFFLINE MAILBOX-STATE MAPPING**.
- Current experiment: **none armed**.
- Production functionality remains unchanged.
- Do **not** repeat AFCA timing variants, direct `0x0F` FC16 semantic writes, passive topology censuses, or standalone `0708` probes already covered by EXP147/150 and EXP175–181.
- Do **not** attempt to answer `0708/count6` locally unless the XTR controller first emits a genuine `0F 03 0708 0006`.
- Current highest-value direction: identify the **controller-side topology / integration / scheduler enable condition** that distinguishes the genuine DCM reference system from the local XTR M.

### EXP169–182 consolidated finding

- EXP169: intended `042E/count15` ACK activation condition was not exercised; inconclusive.
- EXP170: intended `03E8 -> 0410 -> 042E` ACK-chain test was confounded by a pre-existing `04A6` retry state; inconclusive, do not repeat unchanged.
- EXP171: corrected capture-role interpretation showed that the reference controller already schedules A5/A4/05 and `0x0F FC03` while the DCM service itself can still be silent.
- EXP172: reference/local controller fingerprints differ structurally; local `A7F8` readCount=15 with `A811/A812=FFFF/0000`, reference readCount=13 with `A811/A812=000C/0500`. Correlation only, not causal proof.
- EXP173: live `0x06` presence does not change that fingerprint or activate the scheduler.
- EXP174: Heat Curve A/B/A does not change the fingerprint or scheduler.
- EXP175: passive topology comparison confirms a structural split: reference has A5/A4/05 + `0x0F FC03`; local XTR does not.
- EXP176: offline analysis does not support `0x0559 Link Integration` as the missing scheduler gate.
- EXP177: guarded direct ESP-originated `0x0F FC16 03E8/count14` Heat Curve write produced no controller semantic change; direct master-originated FC16 is not demonstrated as command ingress.
- EXP178–181: attempts to reproduce the historical AFCA/0861 path in the newer context remained negative even after correcting phase and response delay; stop timing variants.
- EXP182: complete genuine-DCM `0708/count6` census establishes mailbox/session-state variants and confirms `word1=1` as the strongest source-proven heating desired-state dispatch signal.

### Current architecture

```text
reference controller:
extended service/topology scheduler
    -> A5 + A4/05 service family
    -> periodic 0x0F FC03 0708/count6
    -> cyclic 0x0F FC16 07D0..0884 runtime uploads
    -> DCM can join/rejoin
    -> full 03E8.. state resync
    -> mailbox word1=1 can trigger FC03 03E8/count13 desired-state fetch

local XTR:
native 0x0F settings/state traffic exists
    -> 03E8 / 04A6 / 085F etc.
but:
    -> no normal A5 family
    -> no demonstrated A4/05 service
    -> no spontaneous 0708 FC03 scheduler
    -> no confirmed cyclic 07D0..0884 runtime family
```

### Key open question

The unresolved problem is now:

**What enables the extended scheduler/topology in the controller?**

Remaining plausible categories:
1. controller model / firmware capability;
2. commissioning or persistent configuration;
3. physical accessory/DCM topology recognition during boot;
4. another controller-side feature flag or binding state.

Physical DCM presence remains viable because the available captures do not include a clean same-controller A/B cold boot with and without DCM attached.

### EXP164–167 consolidated finding

- EXP164 reproduced the no-DCM cold-boot baseline: C8 discovery, `0x06` polling, A80E `0 -> 8 -> 0x28`, AFDC `0x10`, and sustained unACKed `0x0F FC16` can all occur without A5, A4/0x05 or `0x0F FC03`.
- Genuine DCM runtime power-up (`090209`) differs sharply: the `0x0F` service is already ACK-capable within ~0.4 s and A5 becomes operational roughly 0.8 s later, while C8 continues in parallel.
- EXP165 proved that runtime `0x0F FC16` ACK service alone does not activate A5 or `0x0F FC03`. Its intended simultaneous 0x06 role was invalid because of a 27-byte/23-byte FC17 matcher bug.
- EXP166 corrected that matcher and transmitted 169 valid `0x06` responses in 180 s. `EXP 0.0` appeared immediately, proving runtime `0x06 -> EXP/version metadata`, but no A5, A4/0x05 or `0x0F FC03` appeared and no `0x0F FC16` occurred in that window.
- EXP167 extended the corrected runtime `0x06` responder to 600.009 s. It transmitted **559** valid 0x06 responses while the controller emitted **zero 0x0F frames of any kind**: `s0F=0`, `0F16req=0`, `0FtxACK=0`, `0F03req=0`, `A5=0`, `A4=0`, `s05=0`. Bus integrity remained clean: `resyncDelta=0`, `dropDelta=0`.
- Therefore sustained, valid `0x06` accessory/version presence does **not** induce native `0x0F` service or A5 scheduling during runtime.
- The exact intended EXP167 condition `active 0x06 + actually exercised controller-originated 0x0F FC16 ACK` still never occurred, so that narrow combination remains technically untested. However, waiting longer on `0x06` as the trigger is now low-value.
- The missing prerequisite is increasingly likely to be an earlier/parallel discovery, binding, electrical ownership or service-availability property of the genuine DCM topology rather than a simple `0x06` metadata response.

### Current protocol model

1. **0x06 accessory/version metadata path** — independently activatable; valid responses can expose `EXP / UITBR.KAART`, and `AFD1` maps to displayed version/10. This does not establish the Online/DCM session.
2. **0x0F bidirectional mailbox/service** — controller can emit FC16 writes without a DCM, but genuine DCM topology provides an operational/ACK-capable service and later FC03 reads. Physical ownership remains unresolved.
3. **A5 service** — appears only in genuine DCM topology so far; exact physical owner and activation mechanism remain unresolved.
4. **A4 <-> 0x05 sibling path** — genuine-topology alternate/discovery-like service; not a simple mandatory A5 precursor.
5. **C8 FC03 0x2328/count2** — generic native startup discovery, not DCM-specific.

### Do not repeat without new evidence

- isolated A5 responder;
- direct A5 read triplet after known 0x0F ACKs;
- 0x0F ACK-only activation;
- `0x06` presence-only activation, including longer dwell times;
- C8 response guessing;
- A80E/AFDC or `EXP 0.0` as DCM-recognition criteria.

## Permanent YAML generation invariants

These rules apply to every future experiment YAML and are not experiment variables:

- Preserve the known-good top-level production configuration unless an experiment explicitly requires changing it.
- Always preserve the `substitutions:` block used by the production YAML, including at minimum `device_name` and `friendly_name` when the file references `${device_name}` / `${friendly_name}`.
- Before delivering a new YAML, verify that every `${...}` substitution referenced in the file is defined.
- Treat a missing top-level production block (for example `substitutions:`, `esphome:`, Wi-Fi/API/OTA, UART, or known-good production entities) as a generation error, not as an experimental change.
- Validate YAML syntax and run a substitution-reference sanity check before delivery. When possible, compile with ESPHome; if no local ESPHome compile is run, state that explicitly.
- Preserve bus-health bookkeeping: after every CRC-valid frame, refresh `thermia_last_valid_frame_ms`, increment `thermia_valid_frame_count`, and publish `thermia_bus_healthy=true`; the watchdog may only publish `false` after the configured stale timeout.


- Last completed experiment: **EXP105**
- EXP93 status: **PASSIVE A80F=50 discriminator armed in two captures but never triggered; not a negative result and now superseded as next priority**
- Current experiment: **EXP106 — passive integration-sync window correlator — PREPARED, not yet run**
- Current control architecture target: **emulate Thermia/Danfoss Online/Connect/DCM03 on slave 0x06**
- Room-sensor emulation on slave 0x0A is **not pursued as the control architecture**

## System

- Heat pump: Thermia iTec XTR M / Total Compact, older non-Genesis controller
- Integration target: ESP32 / ESPHome / Home Assistant
- Bus: Modbus RTU-like, 9600 baud, 8E1, valid Modbus CRC
- Safety policy: read-only/passive by default; active responses only in exact known response slots with fail-closed guards

## Confirmed protocol findings

### 0x06 accessory/DCM slot

- Controller polls slave 0x06 with FC17.
- Normal unserved cadence is about 4.3 s.
- A syntactically valid response starts a fast alternating cadence of roughly 0.7 s SHORT and 1.4 s FAST-LONG.
- Accessory response contains 12 words corresponding to AFC8..AFD3.
- Controller writes five words AFDC..AFE0 in the FC17 request.

### Four-phase handshake

- AFCA / accessory response word2 is the REQ/data-valid level.
- REQ low: AFCA=0000.
- REQ asserted: AFCA=03E8.
- In correct phase, 03E8 causes controller 0x0F:0861 to rise 0 -> 16.
- Keeping 03E8 asserted keeps ACK high.
- Returning AFCA to 0000 while keeping the other payload stable causes 0861 to return 16 -> 0.
- This is a proven transport-level four-phase handshake.

### Historical A80E/AFDC cycle

Older passive captures repeatedly showed:

- A80E 0 -> 32
- AFDC 0 -> 32 shortly afterwards
- about 17 s later A80E 32 -> 0 and AFDC 32 -> 0
- recurrence around ~65 s in those captures

This is distinct from the 0861 transaction ACK.

## EXP90-92 conclusions

### EXP90

Persistent response w0=00FF for 90 s. 84 responses. No A80E/AFDC cycle. Negative.

### EXP91

Persistent historical envelope with REQ low:

00FF,0001,0000,0001,0...

for 90 s. 84 responses. No A80E/AFDC cycle, no settings change, no parser/RX error. Negative.

### EXP92

Hypothesis: a completed transport handshake might initialize hidden controller/accessory state required before the historical REQ-low envelope can cause the old A80E/AFDC cycle.

Sequence executed successfully:

1. stable LONG baseline
2. historical envelope preloaded with REQ low
3. AFCA 0000 -> 03E8 on SHORT
4. 0861 0 -> 16 after 401 ms
5. AFCA returned to 0000 with payload stable
6. 0861 16 -> 0 after 1031 ms
7. same historical REQ-low envelope maintained for 90 s

Result:

- handshake_complete=1
- total responses=90
- observation responses=84
- A80E peak/current=0000, changes=0
- AFDC peak/last=0000, changes=0, nonzero=0
- status peak=16
- settings_changed=0
- resync_delta=0
- drop_delta=0

**Strong conclusion:** one correctly completed four-phase 03E8 transaction is not sufficient to initialize the historical A80E/AFDC online-state cycle.

## Current architectural direction

The project target is now explicitly to emulate the official Thermia/Danfoss Online/Connect/DCM03 accessory through slave `0x06`. Room-sensor emulation on `0x0A` remains useful protocol evidence but is not the desired control path.

Firmware analysis of Danfoss Link CC recovered the host-side HE/DHP parameter protocol:

- request format: endpoint byte, GET/SET count nibbles, 16-bit parameter IDs, then SET values;
- heat-pump parameters include `0x030A OperationMode`, `0x4402 HeatCurve`, `0x440A HotWaterStart`, `0x4414 IntegrationMode`, and others;
- `0x4414 IntegrationMode` is GET-on-sync and SET-on-sync, then its one-shot SET flag is cleared;
- parameters are assigned to partial sync groups 0/1/2.

The Link CC firmware does not contain the final DCM03 -> Thermia RS485 serializer. The unresolved layer remains:

```text
HE ParameterID/value
    -> DCM03 translation/state machine
    -> AFC8..AFD3 / AFDC..AFE0
    -> Thermia controller
```

Official Danfoss documentation adds two relevant constraints:

- DHP-AQ Link integration requires heat-pump software 2.2 or newer, indicating controller-side firmware support for the integration path;
- Link firmware 4.2.1724 can keep re-offering Heat Curve for 30 minutes after initial HP communication if the HP rejects/forgets it, indicating an initial synchronization/desired-state model rather than a one-shot raw register write.

## EXP93 status

**Hypothesis:** historical `A80E/AFDC 0x0000 <-> 0x0020` cycling is gated by controller state and appears while `A80F=50`.

Result to date:

- EXP93 was correctly armed in two supplied captures;
- `A80F` remained at 10 in the observed periods;
- no `EXP93 TRIGGER` or `EXP93 SUMMARY` occurred;
- therefore EXP93 did not execute its 180 s observation window and is **not** a negative test of the hypothesis.

EXP93 is superseded as the immediate priority because the DCM03 startup/synchronization model now offers a more direct route toward the chosen `0x06` control architecture.

## EXP94 — Passive cold-boot + initial-sync timeline — COMPLETED

**Hypothesis:** after a true Thermia controller cold boot, the controller executes a reproducible accessory/integration startup or synchronization sequence that exposes preconditions/state required before semantic DCM03 commands are accepted.

**Observed facts:**

- >=5 s bus silence was correctly detected; first resumed CRC-valid frame started the 600 s capture.
- At +717 ms: `A80C..A812 = 0040,0000,0000,0005,0005,FFFF,0000`.
- At +1758 ms: `A80E 0000 -> 0008`.
- At +2846 ms: `A80E 0008 -> 0028`.
- First 0x06 poll at +1038 ms: `AFDC..AFE0 = 0000,0000,0000,0000,0019`.
- Second 0x06 poll at +5575 ms: `AFDC..AFE0 = 0010,0000,0000,0000,0014`; therefore `AFDC 0000 -> 0010`.
- `A80F/A810` start at `0005` after cold boot and return to `000A` at about +11.3 s.
- `0861` initialized to `0000` and had zero transitions during the 600 s capture.
- No settings changes occurred.
- 140 exact 0x06 polls were observed; cadence remained unserved/long at 4086..4537 ms.
- Final controller state remained `A80C..A812 = 0040,0000,0028,000A,000A,FFFF,0000`.
- Final 0x06 controller-write image remained `AFDC..AFE0 = 0010,0000,0000,0000,0014`.
- Summary: `frames=5185`, `ctrl_changes=3`, `rsp02_changes=1`, `0861_changes=0`, `settings_changes=0`, `resync_delta=1`, `drop_delta=0`.

**Strong conclusions:**

- The cold-boot controller/accessory sequence is short: the relevant state settles within roughly 11 s and then remains stable for at least 10 minutes when slave 0x06 is unanswered.
- Historical `A80E/AFDC 0x20 <-> 0` cycling is not ordinary cold-boot initialization.
- `0861` is separate from the longer-lived `A80E/AFDC` controller/accessory state machine.
- The stable unanswered post-boot state is `A80E=0x28`, `AFDC=0x10`, `A80F/A810=10`; exact semantics remain unknown.

**Hypothesis:** `AFDC=0x10` may represent an accessory-not-established / waiting state. This is not proven.

## EXP95 — Cold-boot zero-presence from first 0x06 poll — COMPLETED

**Hypothesis:** syntactic DCM presence from the first cold-boot `0x06` poll is sufficient to move the controller away from EXP94's stable application/waiting state.

**Observed facts:**

- full capture duration `120000 ms`;
- `1133` valid frames; `112` exact 0x06 polls; `112` transmitted responses; `0` TX refusals;
- 0x06 cadence accelerated to `638..1503 ms`;
- controller boot sequence remained `A80E 0->8->0x28`, `A80F/A810 5->10`;
- `AFDC` still became `0x10`;
- final application state remained `A80E=0x28`, `A80F=A810=10`, `AFDC=0x10`, `0861=0`;
- `0861_changes=0`; `settings_pushes=0`; `settings_changes=0`; `outdoor_state_changes=0`;
- `resync_delta=1`; `drop_delta=0`.

**Strong conclusions:**

- a syntactically valid `0x06` responder from the first cold-boot poll is enough to enter the fast accessory polling cadence;
- syntactic presence alone does **not** advance the higher DCM/application session state;
- `AFDC=0x10` cannot simply mean “no 0x06 slave/accessory present”;
- transport presence and DCM application/session establishment are distinct layers.

**Negative result:** zero-presence from poll #1 does not change the EXP94 cold-boot application state.

## EXP96 — Cold-boot historical envelope + canonical REQ/ACK handshake — COMPLETED

**Hypothesis:** the historical DCM envelope may only have semantic/session effect when delivered after a true cold boot in the stable EXP95 controller context.

**Observed facts:**

- true cold boot reproduced the EXP94/95 startup state;
- zero-presence established fast `0x06` polling;
- exactly one historical-envelope transaction completed;
- `0861 0->16` occurred 367 ms after REQ assertion;
- `0861 16->0` occurred 1196 ms after REQ deassertion;
- summary: `06polls=112`, `tx=112`, `refused=0`, `handshake=1`;
- `ctrl_changes=3`, `rsp02_changes=0`, `settings_pushes=0`, `settings_changes=0`, `outdoor_state_changes=0`;
- final higher-layer state remained the same as EXP95.

**Strong conclusion:** cold-boot context does not make the historical `00FF,0001,REQ,0001` envelope semantically sufficient. It remains a valid transport envelope only; the semantic DCM03 serializer/init payload is still missing.

**Important natural observation before EXP96 ARM:** while the ESP was passive, `A80E` changed `0x28 -> 0x20 -> 0x00`, followed shortly by `AFDC 0x10 -> 0x00`. This was not caused by EXP96. It weakens any simple interpretation of A80E/AFDC as a dedicated DCM session indicator and suggests broader controller-state propagation.

## EXP97 — Passive natural A80E/AFDC edge correlator — COMPLETED

**Hypothesis:** the spontaneous `A80E 0x28->0x20->0x00` / `AFDC 0x10->0x00` sequence correlates with ordinary controller/outdoor-unit state and is not DCM03 session establishment.

**Design:**

- 100% passive/read-only for 600 s;
- no cold boot required;
- no response to slave `0x06`;
- no UART TX / DE enable;
- trigger/event log on every natural `A80E` or `AFDC` transition;
- each event logs the latest `A80C..A812`, `A7F8..A806`, `AFDC..AFE0`, `0861`, `0x1E 0000..0008`, and outdoor-state context;
- controls remain under Home Assistant Configuration.

**Observed:** during the passive run the exact natural sequence recurred:
- `A80E 0x28 -> 0x20` at +71.278 s;
- `A80E 0x20 -> 0x00` 1.062 s later;
- `AFDC 0x10 -> 0x00` 2.655 s after the second A80E edge.

At all three events, `0861=0`, outdoor state remained `0x10`, and the captured `CMD1E` and paired `RSP02` blocks were unchanged.

**Strong conclusion:** A80E/AFDC transitions can occur naturally with no ESP TX and no observed DCM transaction. They must not be used as a primary DCM-session-success criterion. The monitored outdoor/controller blocks did not explain the transition, so exact semantics remain unknown.

**Negative result:** no direct correlation was found with the monitored `0x1E`/outdoor state, `0861`, `CMD1E`, or paired `RSP02`.

## EXP98 — AFC8 single-word A/B/A influence test — COMPLETED NEGATIVE

**Hypothesis:** `AFC8` participates in the accessory application layer and the historical value `0x00FF`, isolated from all other payload fields, may produce a measurable controller effect even with `AFCA=0`.

**Design:** 90 s active but non-setting test: 0–20 s zero-presence baseline, 20–50 s `AFC8=00FF` only, 50–90 s zero-presence recovery. No `03E8`, HE/DHP payload, setting target, or 0x0A emulation. Observe full controller/settings/outdoor changes and cadence.


## EXP99 — historical-field matrix, REQ low — PREPARED

Hypothesis: the non-REQ words from the historical DCM envelope may have standalone or combinatorial application-layer meaning.

Design: 80 s, ten 8 s phases. Only AFC8/AFC9/AFCB are varied using historically observed values (AFC8=00FF, AFC9=0001, AFCB=0001). AFCA remains 0000 throughout, so no REQ/ACK transaction is intentionally started. Exact known 0x06 FC23 response slot only; no setting target and no 0x0A emulation.

EXP98 result carried forward: AFC8=00FF alone produced no detectable semantic effect; controller state, AFDC..AFE0, 0861, settings, CMD1E, outdoor state and cadence remained unchanged across A/B/A phases.


## EXP99 completed result

**Hypothesis:** historically observed non-REQ fields (`AFC8=00FF`, `AFC9=0001`, `AFCB=0001`) may have standalone or combinatorial application-layer meaning while `AFCA=0000`.

**Observed:** all ten 8 s phases completed cleanly. The run delivered 75/75 guarded responses with no refusals. All single, pairwise, and full historical non-REQ combinations produced no change in controller state, paired RSP02, AFDC..AFE0, `0861`, settings, CMD1E, or outdoor state. Poll cadence remained the normal fast-presence pattern (`707..1450 ms`). Parser resync and RX-drop deltas were zero.

**Strong conclusion:** `AFC8=00FF`, `AFC9=0001`, and `AFCB=0001` are not standalone semantic triggers, individually or in the tested combinations, when `AFCA` remains low. The only historical field with proven behavioural effect remains `AFCA=03E8` as transaction REQ.

## EXP100 — prepared

**Hypothesis:** the historical non-REQ fields may acquire meaning only when carried inside a valid four-phase `AFCA=03E8` transaction.

Six payload combinations are tested sequentially in one run. Each is preloaded with REQ low, asserted with `AFCA=03E8`, held until `0861=0010`, deasserted with payload stable, held until `0861=0000`, then followed by 3 s zero-presence observation. No HE/DHP parameter ID or setting target is used.

## EXP100 — Multi-transaction historical-field matrix — COMPLETED NEGATIVE

**Hypothesis:** the historical non-REQ fields (`AFC8=00FF`, `AFC9=0001`, `AFCB=0001`) may acquire meaning only when transported inside a valid canonical `AFCA=03E8` REQ/ACK transaction.

**Observed:** all six planned transactions completed. Each produced the canonical `0861` ACK-high and ACK-low cycle; summary: `complete=1`, `hard_stop=0`, `ack_hi=6`, `ack_lo=6`, `t1..t6=1`, `0861_changes=12`. No controller, RSP02, AFDC..AFE0, settings, CMD1E or outdoor-state changes were observed; no parser resyncs or RX drops occurred.

**Strong conclusion:** none of the tested historical non-REQ field combinations becomes semantically effective merely by being carried inside a valid REQ/ACK transaction. The four-field historical pattern is therefore insufficient as a DCM application command. `AFCA=03E8` remains a transport transaction strobe; the missing semantic layer lies elsewhere in `AFC8..AFD3` and/or requires a larger/multi-message session structure.

**Current direction:** stop iterating AFC8/AFC9/AFCB combinations. Next work should target the remaining response-bank structure / multi-message initialization rather than further permutations of the historical four-word envelope.


## EXP100 — Multi-transaction historical-field matrix with canonical REQ/ACK — COMPLETED

**Hypothesis:** AFC8/AFC9/AFCB may gain application-layer meaning only when carried inside a valid AFCA=03E8 four-phase transaction.

**Observed facts:**

- all six planned transactions completed;
- `ack_hi=6`, `ack_lo=6`, `0861_changes=12`;
- every transaction produced the normal controller ACK-high and ACK-low sequence;
- `ctrl_changes=0`, `rsp02_changes=0`, `06_changes=0`;
- `settings_pushes=0`, `settings_changes=0`;
- `cmd1e_changes=0`, `outdoor_changes=0`;
- `resync_delta=0`, `drop_delta=0`;
- no hard stop and no TX refusal.

**Strong conclusion:** the historical values in AFC8/AFC9/AFCB are not semantically sufficient even when presented inside a fully valid transport transaction. The first-four-word historical-envelope branch is exhausted as a standalone application command hypothesis.

**Negative result:** six valid transport transactions produced zero application-layer effect.

## EXP101 — AFCC..AFD3 one-word influence matrix — PREPARED

**Hypothesis:** one or more of the still-unmapped response words AFCC..AFD3 participates in the DCM03 application layer.

**Only experimental variable:** eight canonical transactions; exactly one tail word per transaction is set to `0x0001`: AFCC, AFCD, AFCE, AFCF, AFD0, AFD1, AFD2, AFD3. All other application words are zero except AFCA during the already-proven REQ phase.

**Safety:** semantics of AFCC..AFD3 are unknown. `0x0001` is therefore treated as a minimal unknown probe, not as a known-good value. No HE/DHP ParameterID or known Thermia setting target is encoded; one unknown word changes at a time; 3 s all-zero recovery follows each completed transaction; TX remains restricted to the exact known `0x06 FC23` response slot.

## EXP101 — AFCC..AFD3 one-word influence matrix — COMPLETED NEGATIVE

**Hypothesis:** one or more of the still-unmapped response words `AFCC..AFD3` participates in the DCM03 application layer and may produce a measurable controller effect when a minimal `0x0001` value is carried inside a valid canonical REQ/ACK transaction.

**Observed facts:** all eight planned transactions completed successfully. Each tail word (`AFCC` through `AFD3`) was tested alone as `0x0001` with all other application words zero except `AFCA=03E8` during the proven REQ phase. Summary: `complete=1`, `hard_stop=0`, `ack_hi=8`, `ack_lo=8`, `t1..t8=1`, `0861_changes=16`. No controller, paired RSP02, AFDC..AFE0, settings, CMD1E or outdoor-state changes were observed. No parser resyncs or RX drops occurred.

**Strong conclusion:** none of `AFCC..AFD3=0001`, when tested individually, has a detectable standalone semantic effect inside an otherwise valid transport transaction. The simple one-word-selector hypothesis is negative across the entire remaining tail of the 12-word response bank.

**Unknowns:** this does not exclude multi-word payload structure, values other than `0x0001`, checksums/lengths/sequence fields inside the payload, or a multi-message DCM initialization state machine. The application-layer format remains unresolved.

**Current direction:** stop one-word probing across `AFC8..AFD3`; the full bank has now been covered either by historical-field tests or minimal tail-word tests. The next experiment should target message structure or multi-message sequencing rather than more isolated word values.

## Archive re-analysis before EXP102 — MATERIAL FINDING

A bulk archive containing 98 historical Thermia logs was re-analysed before defining EXP102.

Important recovered coverage that was underrepresented in the condensed experiment summary:
- EXP18 varied AFC8/word0 across 0000,0001,00FE,00FF,0100,FFFF while keeping AFC9=1, AFCA=03E8, AFCB=1; transport ACK occurred but no semantic write was established.
- EXP16 varied AFC9/word1 across 0000,0001,0002,0004,0008,FFFF with AFCA=03E8 and AFCB=1; again transport ACK was largely independent of that value.
- EXP14/15 varied AFCB/word3 over small and boundary values with AFCA=03E8; ACK behavior did not establish application semantics.
- EXP24 and EXP25 already probed words 4..11 with 0001 inside the 0861-active window; no settings change occurred.
- EXP26 and EXP28 tested structured word4/word5 combinations with current/target setpoint-like values and observed no write.

**Strong conclusion:** repeating isolated-word tests is low value. The remaining useful hypothesis is interaction/structure: a field such as AFC9 or AFCB may declare payload length/count, causing tail data in earlier experiments to be ignored when the declared count remained 1.

## EXP102 — count / structure interaction matrix — PREPARED

**Hypothesis:** `AFC9` and/or `AFCB` is a payload length/count field. Earlier tail-word probes may have been structurally invalid because extra non-zero words were supplied while the historical header still declared `0001`.

**Transactions:**
- T1 control: `AFC8=00FF, AFC9=1, AFCA=REQ, AFCB=1`
- T2 AFC9-length2: `AFC9=2`, `AFCC=1`
- T3 AFC9-length3: `AFC9=3`, `AFCC=1`, `AFCD=1`
- T4 AFCB-length2: `AFCB=2`, `AFCC=1`
- T5 AFCB-length3: `AFCB=3`, `AFCC=1`, `AFCD=1`
- T6 both-length2: `AFC9=2`, `AFCB=2`, `AFCC=1`

All six use the proven canonical AFCA=03E8 REQ/ACK handshake with payload stability through ACK-high -> REQ-low -> ACK-low, followed by 3 s all-zero recovery. No known setting register or HE/DHP ParameterID is transmitted. Small values 1..3 only. Hard stop 80 s.

## EXP102 — count / structure interaction matrix — COMPLETED NEGATIVE

**Hypothesis:** `AFC9` and/or `AFCB` is a payload length/count field, so tail data may only be interpreted when the declared count grows coherently with the payload.

**Observed facts:** all six planned coherent structures completed the canonical transaction handshake. Summary: `complete=1`, `hard_stop=0`, `ack_hi=6`, `ack_lo=6`, `t1..t6=1`, `0861_changes=12`. No controller, paired RSP02, AFDC..AFE0, settings, CMD1E or outdoor-state changes occurred; no parser resyncs or RX drops occurred.

**Strong conclusion:** the simple length/count interpretation of AFC9 and AFCB is not supported. Increasing either field to 2/3 while adding matching tail words did not produce any detectable application-layer effect. T6 with both fields at 2 was likewise negative.

**Hypotheses still open:** the DCM application layer may use a different structured encoding, a checksum/sequence/type field, a multi-message initialization/session state machine, or values observed only from a real DCM03.

**Current direction:** stop simple count/length experiments. Prefer evidence-driven reconstruction from real/historical multi-frame patterns or a real DCM03 capture rather than further arbitrary field permutations.


## Historical log archive audit after EXP102

A systematic audit of 98 archived logs recovered substantially broader historical coverage than the condensed experiment history implied. The archive contains extensive first-word/header, selector, tail-word, same-packet, phase, session/presence, HE-envelope and cold-boot tests. At least 45 unique logged experimental `0x06` response payload forms were extracted; early logs sometimes record only the first four words, so this is a lower bound.

**Strong conclusion:** no archived frame was identified as a genuine DCM03/Thermia Online accessory response. Recognisable `AFC8..AFD3` TX payloads are synthetic ESP experiment responses; raw `06 17 AFC8...AFDC...` frames are controller->accessory requests. Therefore the archive is valuable primarily as a negative-test/deduplication corpus, not as a hidden source of the genuine DCM serializer.

**Experiment policy:** do not start EXP103 as another guessed payload probe. EXP103 remains intentionally undefined until new structural evidence is obtained. Preferred evidence is a real DCM03/Online/Connect cold-boot capture plus one known setting change/rollback; next-best evidence is DCM firmware/PCB/debug information or an external owner's capture.


## EXP103 — repeated identical canonical transaction chain — COMPLETED NEGATIVE

**Hypothesis:** the missing DCM03 application/session layer may require multiple consecutive successful transactions with the same application envelope before higher-layer state is established.

**Observed facts:** three identical canonical transactions using `00FF,0001,REQ,0001,0...` completed successfully with no 3 s zero-recovery gap between T1/T2/T3. Each transaction produced the normal `0861 0->16->0` ACK cycle. T1 ACK-low occurred 1077 ms after REQ deassert, T2 after 1076 ms, T3 after 1076 ms. The final summary was `complete=1`, `hard_stop=0`, `ack_hi=3`, `ack_lo=3`, `t1=t2=t3=1`, `settings_changes=0`, `ctrl_changes=0`, `06_changes=0`, `cmd1e_changes=0`, `outdoor_changes=0`, `resync_delta=0`, `drop_delta=0`.

**Strong conclusion:** repeating the exact same historical envelope across three back-to-back valid transport transactions is not sufficient to establish the DCM application/session layer or produce a semantic write. A simple cumulative/repetition requirement is therefore not supported.

**Post-experiment observation:** after EXP103 had already completed and its summary had been emitted, the controller naturally changed `A80E 0->32` and shortly afterwards `AFDC 0->32`. The same natural sequence occurred again later in the same log. Because these transitions occurred after the experiment had ended, they are not attributed to EXP103 and further reinforce that A80E/AFDC transitions are not a reliable DCM-session success criterion.

**Diagnostic note:** this run was captured with the pre-fix EXP103 health bookkeeping bug. `Bus Last Valid Frame Age` remained `nan` and `Valid Frames Since Boot` remained `0` despite continuous valid raw frames. This affects Home Assistant health diagnostics only; it does not invalidate the EXP103 0x06 transaction result. The corrected EXP103 YAML restores last-valid-frame timestamping, valid-frame counting, and Bus Healthy recovery on every CRC-valid frame.

**Next direction:** do not extend this branch to longer arbitrary repetition counts without new evidence. The highest-value next evidence remains a genuine DCM03/Online/Connect capture or hardware/firmware evidence revealing the missing serializer/session protocol.


## EXP104 — AFC8 sequence-toggle canonical transaction chain — PREPARED

**Hypothesis:** `AFC8` may participate in a transaction identity / sequence mechanism whose meaning only appears when its value changes between consecutive canonical transactions. Earlier experiments tested AFC8 values individually; EXP104 tests only the ordering interaction.

**Only experimental variable:** AFC8 alternates across three back-to-back canonical transactions: T1=`00FF`, T2=`00FE`, T3=`00FF`. AFC9 remains `0001`, AFCB remains `0001`, all tail words remain zero, and AFCA uses only the proven `0000 -> 03E8 -> 0000` transport handshake. No 3 s zero-recovery is inserted between transactions; after T3, replies return to all zeros for a 10 s observation window.

**Safety:** `00FF` and `00FE` were already exercised as AFC8 values in earlier tests without a semantic write. No known setting register or HE/DHP ParameterID is transmitted. TX remains restricted to the exact known `0x06 FC23` response slot with the 5 ms UART-empty guard and driver-enable off outside TX. Hard stop 60 s.

**Production invariants retained:** corrected bus-health bookkeeping from the fixed EXP103 is present: every CRC-valid frame refreshes `thermia_last_valid_frame_ms`, increments `thermia_valid_frame_count`, and restores `Bus Healthy=true`.


## EXP104 — AFC8 sequence-toggle canonical transaction chain — COMPLETED NEGATIVE

**Hypothesis:** `AFC8` may participate in a transaction identity / sequence mechanism whose meaning appears only when its value changes between consecutive canonical transactions.

**Observed facts:** T1=`AFC8=00FF`, T2=`AFC8=00FE`, T3=`AFC8=00FF` all completed the canonical `AFCA 0000 -> 03E8 -> 0000` transaction with `0861 0000 -> 0010 -> 0000`. ACK-high delays were 447 ms, 441 ms and 447 ms; ACK-low followed REQ deassert by 1076 ms for all three. Final summary: `complete=1`, `hard_stop=0`, `ack_hi=3`, `ack_lo=3`, `t1=t2=t3=1`, `settings_pushes=0`, `settings_changes=0`, `cmd1e_changes=0`, `outdoor_changes=0`, `resync_delta=0`, `drop_delta=0`.

**Observed controller state during final observation:** after the three experiment transactions had completed and while replies were already all-zero, natural `A80E 0->32` and then `AFDC 0->32` changes occurred. The same A80E/AFDC cycle later returned to zero and repeated multiple times in the same log, so it is not attributed to the AFC8 sequence toggle.

**Strong conclusion:** alternating AFC8 `00FF -> 00FE -> 00FF` across consecutive valid transactions does not produce a semantic setting write or establish the missing DCM application/session state. The simple transaction-sequence interpretation of AFC8 is therefore not supported by this test.

**Production diagnostic validation:** the bus-health repair carried into EXP104 worked. `Valid Frames Since Boot` increased normally and `Bus Last Valid Frame Age` remained finite/near zero during active traffic.

**Next direction:** avoid further arbitrary single-field toggles. Prefer a genuinely new structural hypothesis or new external evidence (real DCM03/Online/Connect capture, firmware/PCB/debug evidence, or cross-model reproduction of the AFCA/0861 handshake).


## EXP105 — State-gated canonical transaction — PREPARED

**Hypothesis:** the unresolved DCM03 application/session layer may only accept the already-known canonical transaction during a controller-advertised lifecycle/service window. The natural `A80E=0x0020` followed by `AFDC=0x0020` cycle is the only evidence-backed candidate window currently available.

**Only experimental variable changed:** transaction timing relative to controller state. Payload remains the previously tested historical envelope `00FF,0001,REQ,0001,0...`; no new values or setting IDs are introduced.

**Sequence:**

1. Arm and remain strictly passive.
2. Wait until current `A80E=0x0020` and an exact `0x06` FC23 poll carries `AFDC=0x0020`.
3. On that poll preload `00FF,0001,0000,0001,0...`.
4. On the next safe SHORT poll while the gate remains high, assert `AFCA=0x03E8`.
5. Complete the proven `0861 0->16->0` four-phase handshake.
6. Reply zeros for 20 s observation.
7. Hard stop at 180 s if no usable window/completed transaction occurs.

If the gate closes before REQ assertion, the attempt is abandoned and the experiment returns to passive waiting.


## EXP105 — State-gated canonical transaction — COMPLETED NEGATIVE

**Hypothesis:** a semantic/application transaction may only be accepted during the natural lifecycle window where `A80E=0x0020` and `AFDC=0x0020`.

**Observed:**
- gate occurred naturally and was detected with `A80E=0020` and `AFDC=0020`;
- one historical canonical transaction was executed inside that window;
- `0861` ACK-high occurred 373 ms after REQ assert;
- ACK-low occurred 1151 ms after REQ deassert;
- `gate_seen=1`, `gate_aborts=0`, `txn_complete=1`;
- no settings, CMD1E, outdoor, or semantic state changes;
- no parser resyncs or RX drops.

**Conclusion:** controller-state gating at the natural `0x20/0x20` window does not make the known historical envelope semantically valid. This materially weakens the hypothesis that our missing layer is merely a timing/window condition. The unresolved layer remains the DCM03 application/session serializer or startup dialogue.

**Decision:** do not continue nearby timing/state-gating variants without new evidence. Prefer genuine DCM traffic, second-unit cross-check of the handshake, or hardware/firmware evidence.


## EXP106 — Passive integration-sync window correlator — PREPARED

**Hypothesis:** historical `A80F=0x0032` (decimal 50) intervals may mark a broader controller integration/synchronisation phase. EXP93 never actually reached this state. EXP105 showed that `A80E=0x20` + `AFDC=0x20` alone is not a sufficient semantic gate, so EXP106 characterises the wider passive state around A80F=50 without transmitting.

**Experimental variable:** observation only. No Thermia-bus value is changed.

**Design:** remain fully RX-only for up to 30 minutes; trigger on the first observed `A80F=0x0032`; then continue passive observation for 180 s. Log change-only context for `A80C..A812`, paired `A7F8..A806`, exact `0x06` `AFDC..AFE0` polls/cadence, `0x0F:0861`, settings pushes, `0x1E` command image, and outdoor-unit operating state. If A80F=50 never appears, hard-stop at 1800 s and record that explicitly.

**Safety:** no RS485 TX anywhere in EXP106. Driver-enable is continuously forced off. No response to `0x06`, no `0x0A` emulation, no register write. Corrected bus-health bookkeeping remains intact.

**Success / information criterion:** a repeatable constellation of controller/accessory changes specifically associated with entering/leaving A80F=50 that narrows the candidate DCM initial-sync window. A no-trigger run is inconclusive about the hypothesis but records occurrence frequency; a triggered run with no distinctive DCM-related behaviour is evidence against A80F=50 as the missing sync discriminator.


## Cross-model update from Piotr Romanowski / thermia-bus-sniffer (2026-09-23)

Independent iTec Eco 8 / DHP-AQ observations materially refine several interpretations:

- `0x1E FC04 0x001E..0x0033` is **not frozen** and not a boot snapshot. It changes rarely and out of step with the live `0x0000..0x0015` block. Treat it only as a delayed/latched-looking region with exact semantics unknown.
- `0x0A:B3B1` is a **proven semantic request channel** when returned by the accessory in the controller's FC23 poll response. Encoding is whole °C (x1). A non-zero value requests a stored room-setpoint change; `0` means no request and does not revert the stored setpoint.
- `0x0A:B3C5` is the controller's push-back/confirmed room setpoint and independently confirms acceptance of a B3B1 request.
- On the Eco 8, `AFDD`, `AFDE`, `AFDF` remained constant `0`; `AFE0` equals displayed outdoor temperature x1.
- On the Eco 8, `AFDC` pulses `0 <-> 0x20` continuously with ~64 s period (~17 s high / ~47 s low), and `A80E` moves with it to the second. This is strong cross-model evidence that the A80E/AFDC 0x20 cycle is ordinary controller lifecycle/heartbeat behaviour, not DCM login/approval/session acceptance.
- `0x0F:0861` has remained passively at `0` on the Eco 8 over multi-day observation. Therefore any `0861` transition during an active 0x06 test is highly meaningful and continues to support its role as a transaction-level response to `AFCA=0x03E8`.
- A80E can carry additional bits independently of the 0x20 heartbeat (Piotr observed bit 3 for ~10 minutes). Exact bit semantics remain open.
- One isolated `AFDC=0x10` observation coincided with the outdoor-unit active status rising. This is one coincidence only and is not sufficient evidence for an approval window.

**Protocol correction:** do not use `AFDC=0x10`, `AFDC=0x20`, or matching `A80E` values as a DCM approval/session gate without new evidence.

**Next-experiment implication:** if/when EXP107 is prepared, prefer testing a continuously present/stable accessory image followed by one isolated known `AFCA 0 -> 03E8 -> 0` pulse, rather than gating on AFDC/A80E state. EXP107 is only a candidate until EXP106 is formally closed.


## Experiment transition — 2026-09-23

### EXP106 — CLOSED (partial capture, hypothesis sufficiently rejected)

Hypothesis:
`A80F=0x0032` might identify a special integration/synchronisation phase relevant to 0x06/DCM activity.

Observed:
- one run reached `A80F=0x0032` after `0x0050 -> 0x0032`;
- the same A80E/AFDC `0 <-> 0x20` lifecycle was already observed at A80F values 75 and 80 and continued at 50;
- A80F=50 coincided with ordinary outdoor-unit sequencing toward idle;
- a later run remained at A80F=10 for at least the captured interval without any trigger;
- no `0861` activity or settings mutation occurred passively;
- the first triggered run did not include the planned final 180 s summary, so the capture is formally incomplete.

Strong conclusion:
A80F=50 is neither required nor unique for the A80E/AFDC lifecycle and is not a justified DCM approval/session gate. Piotr's Eco 8 evidence independently shows AFDC/A80E `0<->0x20` can be a steady controller heartbeat.

Negative result recorded:
Do not use A80F=50, AFDC=0x20, AFDC=0x10, or matching A80E values as 0x06 semantic-session gates without new evidence.

### EXP107 — PREPARED

Hypothesis:
The controller may require the 0x06 accessory image to be continuously present and stable before the already-known AFCA request pulse is asserted.

Only experiment-level variable changed versus the prior short-preload handshake test:
- REQ-low historical accessory image stabilization time is increased to >=60 s.

Accessory image:
`00FF,0001,0000,0001,0000,0000,0000,0000,0000,0000,0000,0000`

Then ONLY:
`AFCA: 0000 -> 03E8 -> 0000`

All other words remain unchanged.

No new semantic register target or value is introduced.

Current experiment: **EXP107 — PREPARED, not yet run**.


## EXP107 — COMPLETED — Persistent accessory image then isolated AFCA pulse

Hypothesis:
The controller may require the 0x06 accessory image to be continuously present and stable before the already-known AFCA request pulse is asserted.

Observed:
- Baseline qualified with AFDC..AFE0 = `0000,0000,0000,0000,0016`, `0861=0`, `A80E=0`.
- Settings baseline source was the validated persisted cache.
- Historical REQ-low image `00FF,0001,0000,0001,0,0,0,0,0,0,0,0` was then answered continuously.
- Presence immediately switched the controller to the familiar fast alternating cadence (~0.71 s / ~1.43-1.46 s).
- The same REQ-low image was held for 61.023 s before AFCA was changed.
- At 61.023 s, only AFCA changed `0000 -> 03E8`.
- `0861` rose `0 -> 16` after 328 ms.
- On the next exact 0x06 poll, only AFCA changed `03E8 -> 0000`.
- `0861` fell `16 -> 0` after 1122 ms.
- The identical REQ-low image remained present for another 90 s.
- Final summary:
  - handshake_complete=1
  - total_responses=144
  - observe_responses=84
  - A80E_peak=0, A80E_changes=0
  - AFDC_peak=0, AFDC_changes=0, AFDC_nonzero=0
  - status_peak=16
  - settings_changed=0
  - resync_delta=0, drop_delta=0

Strong conclusion:
Long-lived stable accessory presence before the canonical AFCA request pulse is NOT sufficient to unlock semantic DCM/Online behaviour. It changes transport cadence/presence exactly as before and completes the normal 0861 transport handshake, but produces no settings mutation or new DCM/session state.

Negative result recorded:
Reject the simple hypothesis that a 30–60 s persistent historical accessory image, followed by the known AFCA strobe, is the missing initialization step.

Current project direction:
Stop varying dwell time / simple envelope timing. The highest-value next work is firmware-led reconstruction of identity/binding/integration/initial-sync state, especially around:
`ProductID`, `BrandID`, `DivisionID`, `ServiceBind`, `IntegrationMode`, `SystemIntegrationInitRequest`, `InitialSyncDone`.

Current experiment: **EXP107 COMPLETE**.


## Firmware reverse engineering — 2026-09-23 — 2.1.35 vs 2.7.42

Deep extraction of the Windows CE `ccimage.bin` files recovered embedded .NET assemblies.

### Historical split
- `2.1.35` already contains a generic `DHPParameterCache` / HE service infrastructure, but its `RegulationEngine.dll` contains no `HPNode`, `IntegrationMode`, `SystemIntegrationInit`, or `HeatPumpRegulation` application layer.
- `2.7.42` contains a dedicated `HPNode` in `RegulationEngine.dll` plus the full DHP parameter model and integration lifecycle.

This means the generic HE/DHP transport/cache substrate predates the later heat-pump application/regulation layer.

### Exact DHP parameter IDs recovered from `ParameterCache.dll`
The 2.7.42 `ParameterID` static constructor confirms:
- 0x4400 HeatPumpType
- 0x4401 RoomValue
- 0x4402 HeatCurve
- 0x4403 HeatCurveMin
- 0x4404 HeatCurveMax
- 0x4405 HeatCurvePlus5
- 0x4406 HeatCurveZero
- 0x4407 HeatCurveMinus5
- 0x4408 HeatStop
- 0x4409 RoomFactor
- 0x440A HotWaterStart
- 0x440B ControllerDemand
- 0x440C SupplyLineTemperature
- 0x440D ReturnLineTemperature
- 0x440E ExternalControl1
- 0x440F ExternalControl2
- 0x4410 AuxiliaryHeaterPowerStage
- 0x4411 HotWaterTemperature
- 0x4412 OperationStatus
- 0x4413 ExternalControl3
- 0x4414 IntegrationMode
- 0x4415 DefrostDemand
- 0x4416 EVU_SW
- 0x4417 EVU_HW

### Critical correction: init flags are INTERNAL, not wire ParameterIDs
`m_SystemIntegrationInitRequest` and `m_InitSyncDone` are ordinary internal boolean fields in `HPNode`; they are not HE ParameterIDs.

The wire-visible trigger is `IntegrationMode` (`0x4414`). When that parameter updates:
- `OnIntegrationModeParameterUpdated()` sets `m_SystemIntegrationInitRequest = true`;
- sets `RegulationRequired = true`;
- signals model/node changed.

During the next regulation pass:
- `SystemIntegrationInit()` runs;
- `m_InitSyncDone` is cleared;
- `Sync(fullUpdate=true)` runs;
- only after successful full sync is `m_InitSyncDone` set true.

Therefore do NOT search AFC8..AFD3 for literal "SystemIntegrationInitRequest" or "InitialSyncDone" fields unless independent local-bus evidence appears.

### IntegrationMode semantics
`get_IsSystemIntegration()` returns true whenever the IntegrationMode parameter value is non-zero.

The IntegrationMode Parameter object is configured:
- default value 0;
- GetOnSync = true;
- SetOnSync = true;
- ClearSetOnSync = true;
- UseLateCommit = true;
- PartialUpdateIndex = 0.

### System integration changes sync ownership
`UpdateParameterFlow(isSystemIntegration)` switches these parameters:
- RoomValue
- HeatCurve
- HeatCurvePlus5
- HeatCurveZero
- HeatCurveMinus5

When system integration is active, those parameters become SET-on-sync; when not active, they become GET-on-sync.

### Full initial sync is explicitly split into three partial-update groups
`Sync(fullUpdate=true)` executes partial update indices 0, 1, and 2, and only commits GET values after all groups succeed.

This strongly supports a stateful, grouped synchronization model rather than independent scalar writes.

### Binding/identity architecture
2.7.42 `DHPParameterCache::OnHEServiceBind()` explicitly accepts/rejects devices by:
- physical address;
- DivisionID;
- BrandID;
- ProductID.

Only an accepted descriptor gets an endpoint.

Important scope limitation:
This proves HE/Z-Wave-side identity and binding. It does NOT prove that the local DCM03↔heat-pump RS485 mailbox contains the same identity fields.

### Practical consequence
After EXP107's negative result, the next useful 0x06 experiment should not guess an internal init flag.
Research priority is now:
1. reconstruct exact partial sync group composition and ordering;
2. determine whether the local 12-word DCM mailbox represents a grouped sync transaction;
3. only then design EXP108 around one evidence-backed group-0 / IntegrationMode-related structure.


---

## 2026-09-24 — EXP134–136 and genuine Online/DCM capture correction

### EXP134 — passive DHW START correlation — PROCEDURAL / INCIDENTAL
- Strictly passive.
- Only observed settings-word change was `0x03E8: 34 -> 35`, matching Heating Curve.
- No valid DHW START A/B/A conclusion.
- `0x041D` was not observed.

### EXP135 — passive DHW START A/B/A — COMPLETE / NEGATIVE FOR 0x03F1
Hypothesis: manual `SERVICE -> WARMWATER -> START` ±1 °C causes a reversible native `0x0F` word change.
Observed:
- valid baseline / changed / restored markers;
- recurrent `0x03E8..0x03F5` remained unchanged;
- `0x03F1` remained `40`;
- no observed block covered `0x041D`.
Conclusion:
- previous `0x03F1 = Hot Water Start` interpretation is downgraded to OPEN / locally unsupported;
- `0x041D` remains OPEN.

### EXP136 — passive DHW COMFORT/ECO A/B/A — COMPLETE / NEGATIVE
Hypothesis: DHW mode `COMFORT <-> ECO` maps to one of `0x03F2`, `0x03F3`, `0x03F5`.
Observed:
- physical Thermia mode was genuinely changed and restored;
- `wordChanges=0`;
- no change anywhere in recurrent `0x03E8..0x03F5`;
- parser resync/drop deltas remained zero.
Conclusion:
- DHW COMFORT/ECO mode is not represented in the recurrent `0x03E8..0x03F5` block on the tested XTR M.

### Genuine Thermia Online external capture — architecture correction
External capture from a working Thermia Online installation contains:
- a real slave `0x0F` that ACKs controller-originated FC16 writes;
- controller FC03 reads from slave `0x0F`, including `0x03E8`;
- during a deliberate Heat Curve `20 -> 21 -> 20` change, two observed `0x03E8` read snapshots differ only in the first word (`23 -> 22`), independently strengthening `0x03E8` as Heat Curve-related;
- recurrent controller writes to `0x0F` across large block families (`07D0`, `07E4`, `07F8`, `080C`, `0820`, `0834`, `0848`, `0864`, `0870`, `0884`);
- `0x06` is polled but no `0x06` response is present in the supplied working-Online capture;
- an active slave `0xA5` is present; exact identity remains unknown.

Strong architectural correction:
- `0x06` remains proven as an expansion/accessory presence interface, but is no longer treated as the required Online/DCM path.
- `0x0F` is now strongly indicated as the shared controller <-> Online/DCM register interface.
- Direction/ownership matters: controller FC16 writes likely populate controller->Online state, while controller FC03 reads likely consume Online->controller desired/config values.
- Exact physical ownership of slave `0x0F` and role of `0xA5` remain unknown.

### EXP137 — PREPARED
Hypothesis:
If simple slave-`0x0F` presence is the first missing step, ACKing only already-observed XTR `0x0F` FC16 write shapes may cause the XTR controller to begin FC03 reads from slave `0x0F`.

Controlled active behavior:
- 30 s passive baseline;
- abort if a pre-existing `0x0F` responder or FC03 activity is detected;
- active phase ACKs only exact known XTR FC16 shapes:
  - `03E8 / count 14`
  - `0442 / count 13`
  - `04A6 / count 13`
  - `085F / count 5`
- standard FC16 ACK only; no register values transmitted;
- never answer FC03;
- first post-ACK `0x0F` FC03 request is the positive discriminator and immediately disables TX;
- 90 s active timeout;
- fail closed on parser/RX-buffer error.

Current experiment: **EXP137 — slave 0x0F FC16 ACK-only presence probe — PREPARED, not yet run**.


---

## 2026-09-24 — EXP138 PREPARED — sequential 0x0F FC16 ACK probe

Hypothesis:
EXP137 proved that a standard ACK to controller-originated `0x0F FC16 03E8/count14` advances the controller to a new `0410/count22` stage. EXP138 tests the smallest next discriminator: does ACKing `0410/count22` advance the controller again to a new FC16 stage or to an FC03 read phase?

Only experimental variable changed versus EXP137:
- add `0x0410/count22` to the exact FC16 ACK whitelist.

Everything else remains unchanged:
- 30 s passive baseline;
- abort on any pre-existing 0x0F responder/read activity;
- no register-value injection;
- no FC03 response;
- no slave-0x06 responder;
- no room-sensor emulation;
- exact start/count whitelist only;
- parser/RX-drop fail-closed guards;
- DE LOW outside the brief ACK transmission.

Active ACK whitelist:
- `03E8/count14`
- `0410/count22`  **NEW**
- `0442/count13`
- `04A6/count13`
- `085F/count5`

Positive criterion:
After at least one successful ACK of `0410/count22`, either:
1. a previously unseen 0x0F FC16 block appears; or
2. the controller issues an 0x0F FC03 request.

For a new FC16 shape, EXP138 logs it, does NOT ACK it, forces DE LOW, and stops. For FC03, EXP138 likewise does NOT answer and stops.

Safety rationale for new target:
`0410/count22` is not guessed. EXP137 locally observed it immediately after the successful `03E8/count14` ACK and then saw it retransmitted 83 times while unacknowledged. ACKing that exact request is therefore the smallest bounded continuation of the proven controller sequence.

Current experiment: **EXP138 PREPARED, not yet run**.


---

## 2026-09-24 — Correction after fclauson follow-up analysis of genuine Online capture

The follow-up GitHub comments contain an automated interpretation of the same capture. The raw frames were re-parsed independently before accepting those claims.

Raw-frame correction:
- `0x0F FC16 start 0x0848 count 23` occurs at ~12.116 s and ~33.107 s.
- At 12.116 s, register `0x0858` is `0x0000`.
- At 33.107 s, register `0x0858` is `0x0015` (=21).
- Register `0x085A` is `0x0014` (=20) in BOTH 0x0848 frames.
- Therefore the statement that the same 0x0848 field changed `20 -> 21` is incorrect. The actual observed delta is:
  `0x0858: 0 -> 21`, while `0x085A` remains 20.
- The `0x07E4` frame at ~43.705 s matches the earlier recurring `0x07E4` block and does not by itself prove a `21 -> 20` revert of the same field.

What remains useful:
- A value 21 appears exactly once in the second `0x0848` block, at `0x0858`, temporally during the user's Heat Curve 20->21->20 test.
- This makes `0x0858` a strong event/command/synchronization candidate related to the Heat Curve change, but NOT yet a proven persistent Heat Curve register.
- The earlier `0x03E8` FC03 responses still differ by exactly one in their first word (`23 -> 22`) and remain independently consistent with Heat Curve correlation, but exact click timestamps are still needed to assign the two snapshots unambiguously to 20/21/20 phases.

Protocol implication:
Do not adopt the follow-up comment's claim that `0x0848` directly carries a persistent 20->21->20 setpoint in one field. Keep the raw-frame facts separate from that interpretation.

EXP138 remains the next controlled local test because it only probes the locally proven ACK sequence and does not depend on the disputed semantic interpretation of `0x0858`.


---

## 2026-09-24 — EXP138 COMPLETE — sequential 0x0F FC16 ACK probe

Hypothesis:
After EXP137 proved `03E8/count14 -> ACK -> 0410/count22`, ACKing the exact locally observed `0410/count22` stage should advance the XTR controller to the next 0x0F transfer stage.

Observed:
- At EXP138 start, the controller was already repeatedly transmitting `0410/count22` during the 30 s passive baseline.
- This means the controller-side 0x0F transfer state persisted across the ESP reboot / firmware change after EXP137.
- Baseline summary before active phase:
  - `fc16Seen=28`
  - `whitelisted=28`
  - `unknown=0`
  - no pre-existing 0x0F ACK responder
  - no FC03 activity
  - parser/drop counters clean.
- Active phase:
  - first `0410/count22` request was ACKed once.
  - `ack0410=1`.
  - ~1.54 s later the controller advanced to a NEW block:
    `042E/count15` (decimal 1070..1084).
  - EXP138 correctly did NOT ACK the new block and stopped immediately.
- Final summary:
  - reason=`POSITIVE_NEW_FC16_STAGE_AFTER_0410`
  - duration_ms=31949
  - fc16Seen=30
  - whitelisted=29
  - unknown=1
  - ackTx=1
  - txRefused=0
  - fc16AckSeen=0
  - fc03Req=0
  - fc03Resp=0
  - existingResponder=NO
  - resyncDelta=0
  - dropDelta=0
  - DE_LOW.

Strong conclusions:
1. The local XTR 0x0F transfer is a controller-side persistent acknowledged sequence.
2. Sequence state survives the ESP reboot / responder disappearance: after EXP137 stopped at `0410`, EXP138 booted and the controller resumed/retried `0410`.
3. One valid ACK to `0410/count22` deterministically advances the controller to `042E/count15`.
4. The sequence established locally is now at least:
   `03E8/count14 -> ACK -> 0410/count22 -> ACK -> 042E/count15`.
5. `042E/count15` is now a locally proven XTR 0x0F transfer block, not merely an external-map candidate.

External-map alignment:
`0x042E` = decimal 1070 and count 15 covers decimal 1070..1084, exactly matching a block family seen in the external DHP/ATEC register map. Semantics of individual words remain unproven on XTR.

Negative result:
No FC03 read phase is reached before `042E/count15` is acknowledged.

Current experiment: **EXP138 COMPLETE / POSITIVE TRANSPORT PROGRESSION**.

Smallest next experiment:
EXP139 should add only `042E/count15` to the exact ACK whitelist. All other behavior remains unchanged. The first new FC16 shape or first FC03 request after that ACK is the positive discriminator and must not be answered.


---

## 2026-09-24 — EXP139 PREPARED — sequential 0x0F FC16 ACK probe, stage 0x042E

Hypothesis:
EXP138 proved the local acknowledged sequence:
`03E8/count14 -> ACK -> 0410/count22 -> ACK -> 042E/count15`.
EXP139 tests the smallest next discriminator: does ACKing the exact locally observed `042E/count15` stage advance the controller again to another FC16 transfer block or to the FC03 read phase seen in the genuine Online capture?

Only experimental variable changed versus EXP138:
- add `0x042E/count15` to the exact FC16 ACK whitelist.

Known facts about the new target before testing:
- address `0x042E` = decimal 1070;
- count 15 covers `0x042E..0x043C` / decimal 1070..1084;
- EXP138 locally observed this block only after a valid ACK to `0410/count22`;
- EXP138 stopped before acknowledging it;
- external DHP/ATEC material contains a structurally matching 1070..1084 block family, but individual semantics are NOT imported as XTR truth.

Possible effect:
ACKing this request may advance the controller's 0x0F synchronization state to the next stage. No semantic register value is generated or modified by the ESP; the ACK only confirms receipt of the controller's own write request.

Everything else remains unchanged:
- 30 s passive baseline;
- abort on pre-existing 0x0F responder/read activity;
- no value injection;
- no FC03 response;
- no slave-0x06 responder;
- no room-sensor emulation;
- exact start/count whitelist only;
- fail closed on parser/RX-drop errors;
- DE LOW outside brief ACK transmission.

Active ACK whitelist:
- `03E8/count14`
- `0410/count22`
- `042E/count15` **NEW**
- `0442/count13`
- `04A6/count13`
- `085F/count5`

Positive criterion:
After at least one successful ACK of `042E/count15`, either:
1. a previously unseen 0x0F FC16 block appears; or
2. the controller issues an 0x0F FC03 request.

For either positive discriminator, EXP139 does not answer the new stage and stops with DE LOW.

Current experiment: **EXP139 PREPARED, not yet run**.


---

## 2026-09-24 — EXP139 COMPLETE — sequential 0x0F FC16 ACK probe, stage 0x042E

Hypothesis:
After EXP138 proved `03E8/14 -> ACK -> 0410/22 -> ACK -> 042E/15`, ACKing the exact locally observed `042E/count15` stage should advance the controller to the next 0x0F transfer stage.

Observed:
- At experiment start, the controller was already repeatedly transmitting `042E/count15` during the 30 s passive baseline.
- This again confirms that the Thermia/controller-side 0x0F transfer state persists across ESP reboot / firmware replacement.
- Baseline before active phase:
  - `fc16Seen=28`
  - `whitelisted=28`
  - `unknown=0`
  - no pre-existing 0x0F responder
  - no FC03 activity
- Active phase:
  1. `042E/count15` was ACKed once (`ack042E=1`);
  2. ~0.52 s later the controller sent `04A6/count13`;
  3. `04A6/count13` was already in the unchanged whitelist and was ACKed;
  4. ~1.55 s later the controller advanced to a previously unseen block:
     `04BA/count22` (decimal 1210..1231);
  5. EXP139 did not ACK `04BA/count22` and stopped immediately.
- Final summary:
  - reason=`POSITIVE_NEW_FC16_STAGE_AFTER_042E`
  - duration_ms=32936
  - fc16Seen=31
  - whitelisted=30
  - unknown=1
  - ackTx=2
  - txRefused=0
  - fc16AckSeen=0
  - fc03Req=0
  - fc03Resp=0
  - existingResponder=NO
  - resyncDelta=0
  - dropDelta=0
  - DE_LOW.

Strong conclusions:
1. ACKing `042E/count15` advances the controller out of the 042E retry state.
2. The next observed stage is `04A6/count13`; because that exact shape was already whitelisted from earlier XTR observations, it was ACKed without changing the experiment design.
3. After the `04A6/count13` ACK, the controller advances to new block `04BA/count22`.
4. The locally proven acknowledged sequence is now at least:
   `03E8/14 -> ACK -> 0410/22 -> ACK -> 042E/15 -> ACK -> 04A6/13 -> ACK -> 04BA/22`.
5. `04BA/count22` is now a locally proven XTR 0x0F transfer block.
6. Controller-side sequence state again persists across ESP reboot / responder disappearance.

Important nuance:
EXP139 does not isolate whether `04A6/count13` is exclusively caused by the 042E ACK or is an independently recurring block; however, in this run it appears 0.52 s after the 042E ACK and its ACK is immediately followed by the new 04BA stage. Treat `04A6` as a proven observed intermediate stage in this sequence, but not yet as uniquely sequence-owned.

Negative result:
No FC03 read phase was reached before `04BA/count22` was acknowledged.

Current experiment: **EXP139 COMPLETE / POSITIVE TRANSPORT PROGRESSION**.

Smallest next experiment:
EXP140 should add only `04BA/count22` to the exact ACK whitelist. Everything else remains unchanged. The first new FC16 shape or first FC03 request after that ACK is the positive discriminator and must not be answered.


---

## 2026-09-24 — EXP140 PREPARED — sequential 0x0F FC16 ACK probe, stage 0x04BA

## 2026-09-25 — EXP168 COMPLETE / VALID NEGATIVE

**Hypothesis:** with the proven runtime `0x06` responder already active, ACKing one deliberately triggered controller-originated `0x0F FC16 0x03E8/count14` Heat Curve event may reproduce the missing DCM service transition and cause native A5 and/or `0x0F FC03` activity.

**Observed facts:**
- EXP168 armed without controller/heat-pump reboot.
- After 10 valid `0x06` replies the experiment reached READY.
- The operator changed Heat Curve by +1 on the Thermia display.
- The expected exact controller-originated `0x0F FC16 0x03E8/count14` appeared at +43.148 s.
- First payload word was `36 / 0x0024`, matching the changed Heat Curve.
- ESP ACKed that exact request once; this ACK defined T0.
- `0x06` remained continuously active throughout the post-T0 window.
- The full 120 s post-ACK observation completed.
- Final summary: `duration_ms=163187 frames=1308 s05=0 s06=155 s0F=1 A4=0 A5=0 06tx=155 0FtxACK=1 A5tx=0 0F03req=0 0F03rsp=0 0F16req=1 firstAckRelMs=43163 resyncDelta=0 dropDelta=0`.

**Strong conclusions:**
1. EXP168 is a valid negative test of the combined runtime condition left unresolved by EXP167: active proven `0x06` presence plus an actually exercised known `0x0F FC16` ACK is **not sufficient** to activate native A5, A4/0x05, or `0x0F FC03`.
2. The simple transport-role branch is now strongly exhausted: `0x0F` ACK alone (EXP165), `0x06` presence alone (EXP166/167), and their deliberate runtime combination (EXP168) all fail to reproduce the genuine DCM service topology.
3. The missing prerequisite lies outside the currently emulated transport roles, most plausibly in a discovery/binding/service-availability/ownership layer already present very early in the genuine DCM topology.
4. The runtime Heat Curve event remains a clean controller-originated trigger: `03E8/count14`, first word `36`, then one ACK.

**Unknowns:** exact owner of slave `0x0F`; exact owner of A5; whether an unseen discovery/binding exchange occurs before the first visible successful genuine `0x0F` ACK; whether the missing prerequisite is protocol-only, electrical/topological, or both.

**Current experiment state:** EXP168 COMPLETE / VALID NEGATIVE.

**Next direction:** do not iterate further combinations of known `0x06` presence and known `0x0F` ACK behaviour. Before defining EXP169, perform offline transmitter/ownership analysis of the earliest genuine DCM power-up/reconnect capture. No controller reboot is justified at this point.


## 2026-09-26 — EXP182 COMPLETE / POSITIVE OFFLINE MAILBOX-STATE MAPPING

**Hypothesis:** different six-word values returned to `0x0F FC03 0708/count6` act as mailbox/session/dirty selectors and correlate with deterministic controller follow-up behaviour.

**Observed facts:**
- all four available genuine DCM captures were censused;
- the stable runtime response is commonly `0000,0000,0000,0000,077F,0006`;
- exactly two command-event responses had `word1=0001`;
- both were followed about 40 ms later by `0x0F FC03 03E8/count13`;
- controller-boot variants include `...0080,0006` and `...0000,0006`;
- DCM-rejoin first response is `0000,0000,7FFF,FFFF,0080,0007`;
- that rejoin header is followed by controller-originated FC16 state/configuration resynchronisation rather than a desired-state FC03 read;
- in the rejoin capture, the controller schedules `0708` repeatedly before the DCM begins answering, proving scheduler ownership is controller-side.

**Strong conclusions:**
1. `0708/count6` is a mailbox/session header, not a heartbeat.
2. `word1=1` is strongly evidenced as a heating-group pending/dirty indication that gates an immediate `03E8/count13` desired-state fetch.
3. the DCM-rejoin header encodes a distinct synchronization transition.
4. the reference system's `0708` polls and `07D0..0884` FC16 runtime uploads belong to one broader extended controller service scheduler.
5. the tested local XTR lacks that complete observed runtime service family, so the problem is upstream of mailbox contents.

**Unknowns:**
- exact semantics of all six `0708` words;
- exact activation condition for the extended scheduler;
- whether physical DCM recognition, firmware/model capability or commissioning state is the decisive gate.

**Next direction:** stay passive/offline until a concrete scheduler-enable candidate is identified. A same-controller cold-boot A/B capture with versus without genuine DCM is the highest-value external discriminator.


## 2026-09-26 — EXP184 COMPLETE / OFFLINE CROSS-MODEL EXPORT-MAPPING REFINEMENT

**Hypothesis:** the reference `07D0..0884` family is a semantic export layer above model-specific internal slave layouts.

**Observed facts:**
- `07D0/19` repacks the normal `0x02 FC17 A7F8/A80C` controller transaction.
- `07E4/17` strongly tracks the reference `0x04 FC17` exchange, including `FC18 -> FF9C` unavailable-value normalization.
- `0820/18` strongly repacks A5 state.
- Piotr's iTec Eco / DHP-AQ uses `0x1E` for outdoor-unit/COMM-KIT state and does not spontaneously run the extended A5/A4/0x0F-FC03 scheduler in normal no-Online operation.

**Strong conclusion:** the Online/DCM runtime image is best modeled as a semantic serializer/export layer fed by model-specific source endpoints, rather than as a direct mirror of fixed slave addresses.


## 2026-09-26 — EXP185 COMPLETE / POSITIVE FIRMWARE CALL-CHAIN + PARTIAL-GROUP RECONSTRUCTION

**Hypothesis:** the Danfoss Link 2.7.42 firmware can reveal the system-integration lifecycle and the exact semantic grouping behind the higher-level DHP sync protocol.

The original `dlcc_2.7.42` firmware archive was recovered from the project Library. `ccimage.bin` was extracted, the embedded .NET assemblies were carved, and `RegulationEngine.dll` / `ParameterCache.dll` were inspected directly.

### Exact HPNode partial-update groups recovered from constructor IL

**Group 0**
- HeatPumpType
- OperationMode
- IntegrationMode
- RoomValue
- ExternalControl1
- ExternalControl2
- ExternalControl3
- DefrostDemand
- AlarmField1..5
- ErrorCode

**Group 1**
- HeatCurve
- HeatCurveMin
- HeatCurveMax
- HeatCurvePlus5
- HeatCurveZero
- HeatCurveMinus5
- HeatStop
- RoomFactor
- HotWaterStart
- ControllerDemand
- OperationStatus

**Group 2**
- OutdoorTemperature
- AuxiliaryHeaterPowerStage
- HotWaterTemperature
- SupplyLineTemperature
- ReturnLineTemperature
- EVU_SW
- EVU_HW

`IntegrationMode` is group 0. `HeatCurve` is group 1.

### IntegrationMode lifecycle from raw IL
- `OnIntegrationModeParameterUpdated()` sets `m_SystemIntegrationInitRequest=true`, sets `RegulationRequired=true`, signals model change and node change.
- `RegulateSelf()` consumes that request, runs `SystemIntegrationInit()`, clears `m_InitSyncDone`, then runs `Sync(fullUpdate=true)`; successful full sync sets `m_InitSyncDone=true`.
- `UpdateParameterFlow(isSystemIntegration)` flips RoomValue, HeatCurve, HeatCurvePlus5, HeatCurveZero and HeatCurveMinus5 between GET-on-sync and SET-on-sync ownership.

### Important origin finding
Direct callers of `HPNode::set_IsSystemIntegration` in `RegulationEngine.dll` are:
- `HPNode::Load` — reads persisted XML attribute `SystemIntegration`;
- `HPNode::CopySettings`;
- `HPNode::SetDefaultSettings` — uses `FactorySettings::get_HPNodeSystemIntegrationEnabled`.

The factory-settings assembly loads an `HPNodeDefault/SystemIntegration` element and parses its `Value` attribute. No direct `OnHEServiceBind() -> set_IsSystemIntegration` caller was found.

**Strong conclusion:** `IntegrationMode` is an application/synchronization ownership mode with persistent/default configuration support. It is not presently supported as the controller-side scheduler-enable gate itself.

### New mailbox correlation hypothesis
The genuine mailbox event `0708 word1=1 -> immediate FC03 03E8/count13` now lines up strikingly with firmware **partial update group 1**, whose first semantic parameter is HeatCurve. This is the strongest current bridge between the Link semantic protocol and the DCM RS485 mailbox. It remains a hypothesis because group 1 has 11 semantic parameters while the RS485 fetch contains 13 contiguous registers.

**Stop rule:** do not write guessed `IntegrationMode` values to local Modbus. Treat it as a higher-level semantic parameter until an exact serializer mapping is proven.

**Next:** await same-controller DCM-connected / DCM-absent cold-boot A/B for scheduler activation; offline work may continue on mapping `0708` selector words to semantic partial-update groups.



## 2026-09-26 — EXP186–187 offline mailbox refinement

### EXP186 — COMPLETE / PARTIAL POSITIVE
- In the genuine DCM corpus, the only normal command-state selector observed is `0708.w1=1`.
- Both occurrences are followed immediately by `0x0F FC03 03E8/count13` during deliberate Heat Curve changes.
- No independent normal command-state with `w0!=0` or `w2!=0` is present.
- The rejoin header with `w2=7FFF,w3=FFFF,w4=0080,w5=0007` is a compound session/resync state and must not be treated as a simple group-2 selector.

### EXP187 — COMPLETE / NEGATIVE FOR ONE-TO-ONE PARTIAL-GROUP MAPPING
Hypothesis: the `03E8/count13` desired-state fetch is a direct wire serialization of Danfoss Link HPNode partial-update group 1.

Observed:
- `03E8/count13` spans native addresses `03E8..03F4`.
- Proven/native mappings inside that span include Heating Curve, Heating Min/Max, curve +5/0/-5, Heating Stop, Room Factor and room-setpoint mirror.
- The public Online dump confirms writable native indices `03E8..03EE` and `03F0`.
- Danfoss Link group 1 contains HeatCurve, HeatCurveMin, HeatCurveMax, HeatCurvePlus5, HeatCurveZero, HeatCurveMinus5, HeatStop, RoomFactor, HotWaterStart, ControllerDemand and OperationStatus.
- The native contiguous `03E8..03F4` image therefore overlaps strongly with group-1 semantics but is not a one-to-one serialization of the eleven group-1 parameters.

Strong conclusion:
`0708.w1=1` should be described as a heating/settings-family pending selector. The exact claim `w1 == PartialUpdateIndex 1` is plausible but not proven, because the DCM serializer adds/reorders/omits semantic fields.

Current state:
- no active EXP188;
- no YAML change;
- no new local write justified;
- highest-value next evidence remains same-controller cold boot with DCM physically present versus absent, or a genuine Online command affecting a non-heating family.


## 2026-09-26 — EXP189 COMPLETE / POSITIVE PHYSICAL-TOPOLOGY LATCH REFINEMENT

Hypothesis: existing genuine captures can reveal whether the extended Online/DCM topology is activated before, during, or only after normal DCM mailbox/application responses.

Observed facts:
- 090209 is controller/heat-pump cold boot while the DCM is already powered/present.
- The first visible controller frame at ~0.031 s is already the reference 0x02 FC17 A7F8/A80C topology fingerprint.
- C8 appears at ~0.130 s.
- Reference slave 0x04 is already queried and answered at ~0.251/0.290 s.
- The first visible 0x0F FC16 transfer/ACK occurs at ~0.389 s.
- A5 traffic is operational from ~1.179 s.
- 0x06 appears later in the visible sequence, and the first 0708 mailbox poll is only around ~33.18 s.
- In 090550, where the controller is already running and the DCM is powered/rejoined later, the extended 0x02/0x04/A5/0x0F runtime topology and repeated 0708 polls continue while the DCM service remains silent for about 66 s.
- Local EXP164 no-DCM cold boot still shows C8, 0x06 and ordinary 0x0F FC16 traffic but no A4/A5/0x05/0x0F-FC03 topology.

Strong conclusions:
1. Extended topology selection is upstream of the 0708 mailbox contents and upstream of normal DCM desired-state exchange.
2. A reference-only source endpoint (0x04) is active before the first visible 0x0F ACK in the controller-boot capture, so a simple first-ACK trigger cannot explain topology creation.
3. Once the reference controller has the extended topology active, temporary DCM silence/power loss does not immediately tear it down; the scheduler continues. Activation and maintenance are therefore distinct states.
4. The best current model is a latched/persistent controller topology mode selected very early (boot/commissioning/physical accessory recognition), followed by a separately attachable DCM mailbox/session.

Unknowns:
- whether the latch is set only at boot, at commissioning, or by an earlier physical/electrical discovery exchange not captured in the visible first frame;
- whether the same reference controller retains the latch across a full controller power cycle when DCM is physically absent.

Next: same-controller cold-boot A/B with DCM connected versus physically absent remains the decisive discriminator. No local write experiment is justified.
