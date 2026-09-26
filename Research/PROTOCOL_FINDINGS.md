# THERMIA PROTOCOL FINDINGS

Last updated: 2026-09-26 after EXP182

## Bus

- Modbus RTU-like framing
- 9600 baud
- 8 data bits, even parity, 1 stop bit
- valid Modbus CRC

## Important slaves

- 0x02: controller state/sequencer data
- 0x06: DCM/accessory slot
- 0x0A: room-sensor path
- 0x0F: local controller settings/status blocks
- 0x1E: outdoor-unit path

## 0x06 FC17 accessory path

Controller reads AFC8..AFD3 (12 words) and writes AFDC..AFE0 (5 words).

Normal unserved poll cadence: ~4.3 s.
After valid accessory response: alternating fast cadence ~0.7 s / ~1.4 s.

Fast cadence proves syntactic participation only; it does not prove semantic acceptance.

## AFCA / word2 transport handshake

Canonical transaction:

1. semantic payload stable, AFCA=0000
2. assert AFCA=03E8
3. controller 0x0F:0861 rises to 16
4. deassert AFCA=0000 while payload remains stable
5. controller 0x0F:0861 falls to 0
6. payload may then change

EXP92 timing example:

- REQ assert -> ACK high: 401 ms
- REQ deassert -> ACK low: 1031 ms

This is a proven transport-level handshake.

03E8 is therefore not treated as a normal local Thermia register address.

## Historical A80E/AFDC state propagation

Older passive data repeatedly showed:

- controller A80E: 0 -> 32
- next relevant 0x06 controller write AFDC: 0 -> 32
- later A80E: 32 -> 0
- then AFDC: 32 -> 0

This is controller-originated state propagation and is distinct from the 0861 transaction ACK.

## EXP92 result

A correctly completed four-phase handshake followed by 90 s of the historical REQ-low envelope:

00FF,0001,0000,0001,0...

did not reproduce the historical online-state cycle.

Therefore:

- completed transport handshake is not sufficient;
- historical envelope is not sufficient;
- their combination is not sufficient under the tested controller state.

## New controller-state correlation

Older passive capture:

- A80F changed 80 -> 50 after outdoor-unit request turned off;
- while A80F remained 50, repeated A80E/AFDC 0<->32 cycles occurred;
- later A80F changed 50 -> 80 and the outdoor-unit cycle request became active.

EXP92 controller frame showed:

- A80C=64
- A80D=0
- A80E=0
- A80F=10
- A810=10
- A811=FFFF
- A812=0

Working hypothesis: the historical DCM state cycle may be gated by controller state, with A80F=50 currently the strongest observed discriminator. Correlation is not causation. This passive discriminator remains the next DCM fallback after the higher-value EXP93 room-sensor write-path replication.

## Room-sensor semantic path

Our XTR M passive evidence:

- genuine room-sensor setpoint event updates central controller setpoint;
- value later propagates back through B3C5;
- independent master write to B3B1 was ACKed but not adopted by the controller.

Independent transmit-side confirmation from `piotr-romanowski/thermia-bus-sniffer` commit `b4c27157402c49624917d523e016b249cdfc4e11` on iTec Eco / DHP-AQ-family hardware establishes:

- `0x0A` controller poll reads `B3B0..B3B2` and writes `B3C4..B3C6`;
- `B3B0 / 46000` = room temperature x10;
- `B3B1 / 46001` = pending room-setpoint request, x1 whole °C;
- `B3B2 / 46002` = unused/unknown in that setup;
- a non-zero B3B1 returned in the slave response makes the controller adopt that room setpoint;
- the controller then pushes the adopted value back via `B3C5 / 46021`;
- returning B3B1=0 releases the request but leaves the adopted setpoint latched;
- restoring a previous value requires explicitly requesting that value.

**Strong architectural conclusion:** the failed independent master-write test does not contradict B3B1 semantics. The write path is slot/role sensitive: the ESP must behave as slave 0x0A and answer the controller's poll.

**Local status:** transmit semantics are independently confirmed cross-model but not yet confirmed on this XTR M. EXP93 is the collision-safe local replication test.
## Control architecture decision

The intended production control architecture is **not** room-sensor emulation. The target is to emulate the Thermia/Danfoss Online/Connect/DCM03 accessory on slave `0x06`. Slave `0x0A` findings remain protocol evidence only.

## DCM03 / Danfoss Link firmware evidence

Recovered host-side HE Set/Get framing from Link CC firmware:

```text
BYTE endpoint
BYTE counts = (GET_count << 4) | SET_count
WORD SET_ID[]
WORD GET_ID[]
SET values...
```

Relevant abstract parameter IDs include `0x030A OperationMode`, `0x4400..0x4417` DHP parameters, and especially `0x4414 IntegrationMode`. `IntegrationMode` is GET-on-sync + SET-on-sync and then clears its SET-on-sync flag. Parameters are grouped into partial sync groups 0/1/2.

The Link CC image does not expose the final DCM03 -> local Thermia RS485 serializer. Raw HE packet layouts tested directly through `AFC8..AFD3` were negative, so an additional DCM-side translation/state layer remains strongly indicated.

Official Danfoss documentation states that DHP-AQ Link integration requires HP software >=2.2 and that later Link firmware may re-offer Heat Curve for 30 minutes after initial communication when the HP rejects/forgets it. This supports an initial synchronization/desired-state model. It does not prove any specific meaning for `A80E`, `A80F`, or `AFDC`.

## EXP93 status refinement

Two supplied EXP93 logs show the experiment armed correctly but no stable `A80F=50`; the 180 s capture never started. Therefore EXP93 remains inconclusive and must not be recorded as a negative result.

## EXP94 cold-boot state machine result

A true controller cold boot with slave 0x06 unanswered produced the following reproducible sequence in the completed 600 s capture:

```text
~0.7 s:  A80F/A810 = 5
~1.8 s:  A80E 0x00 -> 0x08
~2.8 s:  A80E 0x08 -> 0x28
~5.6 s:  AFDC 0x00 -> 0x10; AFE0 25 -> 20
~11.3 s: A80F/A810 5 -> 10
then stable through 600 s
```

Final stable image:

```text
A80C..A812 = 0040,0000,0028,000A,000A,FFFF,0000
AFDC..AFE0 = 0010,0000,0000,0000,0014
0861        = 0000
```

No settings changes occurred. 140 unserved 0x06 polls stayed on the normal long cadence (4086..4537 ms).

**Strong conclusions:**

- cold-boot integration state settles within about 11 s when 0x06 is unanswered;
- there is no hidden late transition up to 10 minutes;
- historical `A80E/AFDC 0x20 <-> 0` cycling is not simply ordinary cold-boot initialization;
- `0861` remains distinct from the longer-lived A80E/AFDC state machine.

**Refined after EXP95:** `AFDC=0x10` cannot simply mean “no accessory present,” because EXP95 supplies a valid 0x06 responder and still reaches the same state. It remains consistent with a higher-layer not-established/waiting/session state; exact semantics are unknown.

## EXP95 completed result

EXP95 answered every exact post-cold-boot `0x06 FC23` poll with 12 zero words (`AFCA=0`).

Observed over the complete 120 s run:

```text
frames=1133
06polls=112
tx=112
refused=0
06_min_ms=638
06_max_ms=1503
0861_changes=0
settings_pushes=0
settings_changes=0
outdoor_state_changes=0
resync_delta=1
drop_delta=0
```

The controller still converged to:

```text
A80E = 0028
A80F = 000A
A810 = 000A
AFDC = 0010
0861 = 0000
```

**Strong conclusions:**

- valid 0x06 presence from the first cold-boot poll immediately establishes the fast transport cadence;
- it does not advance the DCM application/session state;
- `AFDC=0x10` is not simply an “accessory absent” indicator;
- transport presence, transaction REQ/ACK, and higher application/session state are separate observable layers.

## EXP96 completed result

EXP96 executed the historical envelope in the true cold-boot EXP95 context. The four-phase transport transaction completed cleanly:

```text
preload:   00FF,0001,0000,0001,0...
REQ high:  00FF,0001,03E8,0001,0...
0861:      0000 -> 0010 after 367 ms
REQ low:   00FF,0001,0000,0001,0...
0861:      0010 -> 0000 after 1196 ms
```

No semantic/application progress followed: `settings_changes=0`, `rsp02_changes=0`, and the higher-layer controller state did not advance beyond the EXP95 behaviour.

**Strong conclusion:** the historical envelope is sufficient for the proven transport REQ/ACK mechanism but is not a sufficient DCM03 identity/init/application message, even in cold-boot context.

## Natural A80E/AFDC transition observed before EXP96

Before EXP96 was armed, with the ESP passive, the bus naturally showed:

```text
A80E: 0028 -> 0020 -> 0000
AFDC: 0010 -> 0000
```

This was not experiment-induced.

**Refinement:** A80E/AFDC should no longer be treated as simple dedicated DCM-session indicators. They are more likely broader controller/accessory-state propagation fields; exact semantics remain unknown.

## EXP97 test target

EXP97 is fully passive and focuses only on correlating natural A80E/AFDC edges with already-observable state:

- `A80C..A812`;
- `A7F8..A806`;
- `AFDC..AFE0`;
- `0x0F:0861`;
- outdoor-unit command block `0x1E:0000..0008`;
- outdoor operating-state reference.

No `0x06` response or other TX is generated. The goal is to determine whether the natural `0x28->0x20->0x00 / 0x10->0x00` sequence belongs to ordinary controller/outdoor operation and thereby remove A80E/AFDC as misleading DCM-session success criteria.


## EXP97 natural-state result

The natural sequence was reproduced under fully passive observation:

```text
A80E 0028 -> 0020
~1.06 s later: A80E 0020 -> 0000
~2.66 s later: AFDC 0010 -> 0000
```

At every edge, `0861=0000`, outdoor state=`0010`, and captured `CMD1E` plus paired `RSP02` were unchanged. No ESP TX occurred.

**Protocol refinement:** A80E/AFDC cannot be treated as dedicated DCM03 login/session indicators. They are broader internal controller/accessory lifecycle fields whose exact semantics remain unknown. They should no longer be the primary success criterion for DCM semantic experiments.

## EXP98 result

EXP98 returns focus to the actual accessory response bank. It isolates the first response word only:

```text
A: AFC8=0000, all others 0000, 20 s
B: AFC8=00FF, all others 0000, 30 s
A: AFC8=0000, all others 0000, 40 s
AFCA remains 0000 throughout
```

This is not a write-command test. It is an influence test for whether AFC8 alone changes controller, settings, cadence, ACK, or outdoor behaviour.


## EXP98 result
AFC8=00FF alone is not a standalone semantic trigger. In a controlled A/B/A run it produced no detectable effect on controller state, AFDC..AFE0, 0861, settings, CMD1E, outdoor state or polling cadence.

## EXP99 target
Test the remaining historically observed non-REQ fields and their combinations in a compact matrix while keeping AFCA=0000. This preserves interpretability while increasing throughput compared with one experiment per word.


## EXP99 protocol result

A controlled ten-phase matrix tested `AFC8=00FF`, `AFC9=0001`, and `AFCB=0001` individually, pairwise, and together while keeping `AFCA=0000`. All combinations were inert: no `0861`, settings, controller, AFDC..AFE0, CMD1E, or outdoor-state reaction occurred.

**Refinement:** the historical pattern `00FF,0001,REQ,0001` should not be interpreted as three independent command selectors plus REQ. Of those four fields, only `AFCA=03E8` has independently proven behaviour. The remaining fields may be structured payload/header data that is only interpreted during a valid transaction.

## EXP100 protocol target

Test that exact remaining possibility by carrying six historically grounded AFC8/AFC9/AFCB combinations through the already-proven four-phase transaction handshake. This increases throughput while preserving one-variable-family interpretability and avoids arbitrary values or setting targets.

## EXP100 protocol result

Six historically grounded AFC8/AFC9/AFCB payload combinations were each transported through the proven four-phase transaction handshake. Every transaction generated a complete `0861 0->16->0` ACK cycle, but none changed settings, AFDC..AFE0, controller state, RSP02, CMD1E or outdoor state.

**Refinement:** `AFCA=03E8` is confirmed as transport/data-valid REQ independent of application semantics. The historical `00FF,0001,REQ,0001` pattern is not sufficient to encode a recognized DCM application command. The missing DCM03 serializer/state machine must involve other AFC8..AFD3 fields and/or a higher-level multi-message/session sequence.


## EXP100 finding — first historical response words are transport-insufficient

Six canonical REQ/ACK transactions tested AFC8=00FF, AFC9=0001 and AFCB=0001 separately and in combinations. All six received normal `0861 0->16->0` acknowledgements, while controller state, settings, AFDC..AFE0, 0x1E command state and outdoor state remained unchanged.

Therefore the historical `00FF,0001,REQ,0001` prefix is not a sufficient DCM03 application command. AFCA=03E8 remains the only word in that prefix with a proven role: transport REQ/data-valid.

## EXP101 probe scope

AFCC..AFD3 remain unmapped accessory->controller response words. Their semantics are unknown. EXP101 probes only the minimal non-zero value `0x0001`, one word at a time, inside the proven transport handshake. Any observed effect must therefore be treated as positional influence first, not yet as semantic decoding.

## EXP101 finding — tail words AFCC..AFD3

Each response-bank word `AFCC`, `AFCD`, `AFCE`, `AFCF`, `AFD0`, `AFD1`, `AFD2`, and `AFD3` was individually set to `0x0001` inside a valid canonical `AFCA=03E8` transaction. All eight transactions generated the normal `0861` ACK-high/ACK-low cycle but produced no detectable changes in controller state, paired RSP02, AFDC..AFE0, settings, CMD1E, or outdoor state.

Interpretation: no tail word is a simple standalone `0x0001` selector. Combined with EXP98–100, isolated-word probing across the full `AFC8..AFD3` bank has not revealed the DCM semantic layer. Future work should focus on structured multi-word messages, payload framing/metadata, or multi-message initialization/session sequencing.

## Archive recovery finding — prior tail coverage was broader than current summary

Historical logs show that the response-bank tail had already been exercised more extensively than the current condensed state suggested. EXP24/25 tested words 4..11 with `0001` while `0861` was high, and EXP26/28 tested structured word4/word5 values. EXP16/18/14/15 also showed that AFC9/AFC8/AFCB values can vary without changing the basic AFCA=03E8 transport ACK behavior.

**Protocol implication:** isolated value probing is exhausted. A more plausible structure is that one of the historical `0001` fields is metadata such as a payload length/count. If so, earlier probes that added data beyond word3 while retaining a count of 1 could have been ignored by design.

## EXP102 protocol target — coherent declared-length interaction

Test coherent count-plus-payload structures rather than arbitrary tail values. Compare the historical count-1 control against AFC9-declared lengths 2/3, AFCB-declared lengths 2/3, and a both-length2 case. This is the smallest controlled experiment that tests whether tail words become meaningful only when a matching length/count grows with them.

## EXP102 finding — AFC9/AFCB are not simple payload length/count fields

Six coherent structures were tested using the proven transport handshake. Increasing `AFC9` to 2/3 while adding AFCC/AFCD payload words, increasing `AFCB` to 2/3 with matching tail words, and setting both fields to 2 all produced normal `0861 0->16->0` transport ACKs but no semantic effect.

**Refinement:** neither AFC9 nor AFCB behaves like a simple declared word-count whose increase makes AFCC/AFCD meaningful. The missing DCM03 application layer is therefore more structured than the tested prefix/count model and likely requires a different framing rule or a multi-message/session sequence.


## Historical archive audit — response-bank search space refinement

A full archive audit after EXP102 recovered at least 45 unique logged experimental response forms and confirmed that first-word/header, selector, tail-word, same-packet, phase, presence/session, HE-envelope and count-like hypotheses have already been exercised extensively.

No archived trace could be identified as a genuine DCM03/Thermia Online response. Logged accessory response payloads are synthetic ESP experiment traffic; raw `06 17 AFC8...` frames are controller requests and expose only controller->accessory `AFDC..AFE0` data.

**Protocol implication:** further isolated field/value guessing is not justified. The unresolved DCM layer should be treated as a structured/stateful serializer problem. The highest-value missing evidence is a genuine DCM cold-boot dialogue and one known parameter change/rollback.


## EXP103 finding — repeated identical canonical transactions are insufficient

Three consecutive transactions using the unchanged historical envelope `00FF,0001,REQ,0001,0...` were completed without the recovery gap used in earlier matrices. All three produced the normal `0861` ACK-high/ACK-low cycle, but there were no settings, controller, AFDC..AFE0, CMD1E or outdoor-unit changes during the experiment.

**Refinement:** the missing DCM03 application layer is not unlocked merely by repeating the same accepted transport transaction several times in succession. This weakens a simple cumulative/retry-count interpretation and further shifts the remaining search toward a specific ordered startup dialogue, structured metadata/sequence/checksum, or proprietary DCM-side serialization.

A natural `A80E 0->32` followed by `AFDC 0->32` occurred only after the EXP103 summary and repeated later in the same log. This is additional evidence that these fields participate in ordinary controller lifecycle/state propagation and should not be used as DCM-session success markers.


## EXP104 negative finding — AFC8 is not a simple alternating transaction sequence field
A three-transaction canonical chain using AFC8 `00FF -> 00FE -> 00FF` produced normal transport ACKs on all three transactions but no settings or command effect. This reduces support for a simple AFC8 transaction identity/sequence interpretation. Natural A80E/AFDC `0x20` cycling occurred independently during the subsequent all-zero observation and repeated later, reinforcing that it is not a reliable DCM session-success marker.


## EXP105 protocol target — controller-state gating

EXP98–104 substantially reduce support for isolated payload, count, repetition, and simple AFC8-sequence interpretations. EXP105 therefore keeps the known historical payload unchanged and tests a different dimension: whether the controller only interprets a DCM application transaction during the naturally recurring `A80E=0x0020` / `AFDC=0x0020` lifecycle window. The ESP remains passive until that state is directly observed.


## EXP105 finding — natural A80E/AFDC 0x20 window is not sufficient

A known-good canonical transport transaction was deliberately delayed until the controller naturally presented `A80E=0x0020` and the `0x06` poll carried `AFDC=0x0020`. The transaction still produced only the normal `0861 0->16->0` transport ACK and no setting or command effect.

**Protocol implication:** the missing DCM03 application layer is not explained by a simple controller-state timing gate. Combined with EXP98–104, this further reduces the value of guessed payload/timing permutations. The highest-value next evidence remains a genuine DCM/Online capture or DCM-side firmware/hardware reverse engineering.


## EXP106 target — passive A80F=50 integration-sync discriminator

Firmware/project re-search did not reveal the missing DCM03 -> Thermia serializer or any direct mapping from HE/DHP ParameterIDs into `AFC8..AFD3`. The available host-side evidence still stops at abstract HE Set/Get and sync behaviour; the proprietary/local translation remains outside the recovered host firmware.

The remaining evidence-backed passive discriminator is historical `A80F=0x0032`. Earlier EXP93 captures never reached that state, so its relationship to A80E/AFDC cycling was never actually tested. EXP106 therefore performs no bus TX and captures the broader controller/accessory context when A80F enters/leaves 50.


## Cross-model refinement — Eco 8 / DHP-AQ evidence from Piotr Romanowski

### 0x1E delayed/latched region correction

The `0x1E FC04 0x001E..0x0033` region is **not frozen** and is not proven to be an initialization snapshot. It changes, but much less often and out of step with the live `0x0000..0x0015` block. Treat any apparent pairing as delayed/latched-looking and unconfirmed.

### 0x0A positive-control semantics

`B3B1` is now independently proven as a semantic accessory request field:
- whole-degree encoding (x1);
- non-zero value requests a stored room-setpoint change;
- `0` means no request;
- accepted changes are pushed back by the controller through `B3C5`.

This is a strong architectural reference: Thermia accepts semantic commands when they arrive **inside the polled accessory response**, not as arbitrary independent writes to the same register.

### AFDC..AFE0 on Eco 8

Long passive Eco 8 capture:
- `AFDD=0`
- `AFDE=0`
- `AFDF=0`
- `AFE0` = displayed outdoor temperature x1
- `AFDC` pulses `0 <-> 0x20` continuously with ~64 s period and ~17 s high time.

`A80E` follows the AFDC pulse timing to the second.

**Protocol implication:** A80E/AFDC `0x20` is not a DCM login/approval/session-success marker. It is best treated as ordinary controller lifecycle/heartbeat state.

An isolated `AFDC=0x10` event coincided once with outdoor-unit-active status rising. This single coincidence is insufficient to assign DCM approval semantics to `0x10`.

### 0861 discriminator strengthened

On Piotr's Eco 8, `0x0F:0861` remained at `0` throughout multi-day passive observation. This independently strengthens the interpretation that `0861` movement during Marten's active tests is specifically coupled to the `AFCA=0x03E8` transaction mechanism, rather than being a common spontaneous controller state.

### Search-model refinement for 0x06

Do not use AFDC/A80E values as timing gates for the next active 0x06 experiment.

A more evidence-based architecture hypothesis is:
- the 0x06 slave presents a continuously valid accessory image;
- some fields may be persistent identity/state/capability data;
- `AFCA` is a transaction/request level;
- semantic action may require a request pulse within an already-established stable accessory image.

This remains a hypothesis; the 12-word bank may still be a framed/stateful mailbox rather than purely fixed semantic fields.


## EXP107 prepared protocol question

The next active 0x06 test no longer uses A80F/AFDC/A80E as a DCM session discriminator.

Question:
Does the controller require a continuously-present accessory image before the known AFCA request pulse is treated differently?

Test image:
`AFC8..AFD3 = 00FF,0001,0000,0001,0,0,0,0,0,0,0,0`

After >=60 s of continuous presentation:
`AFCA only: 0000 -> 03E8 -> 0000`

Interpretation rules:
- `0861 0->16->0` = transport transaction completed;
- fast 0x06 cadence = presence only;
- A80E/AFDC changes = controller lifecycle/context only;
- semantic success requires an actual settings/state effect beyond transport ACK.

If EXP107 is negative, the simple "stable accessory image before request" hypothesis is rejected.


## EXP107 finding — persistent presence is not sufficient

Confirmed sequence with a 61.023 s pre-existing stable historical accessory image:

`REQ-low image stable`
→ `AFCA 0000 -> 03E8`
→ `0861 0 -> 16` after 328 ms
→ `AFCA 03E8 -> 0000`
→ `0861 16 -> 0` after 1122 ms
→ same image held 90 s

No semantic consequence:
- settings_changed=0
- A80E remained 0
- AFDC remained 0
- no new session/integration marker emerged
- parser/drop counters remained clean

Protocol conclusion:
The canonical AFCA/0861 mechanism is a transaction-level handshake and is not itself sufficient for application-layer DCM initialization, even after prolonged accessory presence.

Research priority moves from timing/persistence toward reconstructing the application initialization state machine (identity, binding, integration mode, initial sync).


## Firmware-derived application lifecycle — 2.7.42

Recovered from .NET IL inside `RegulationEngine.dll` and `ParameterCache.dll`:

`IntegrationMode (0x4414) update`
→ internal `SystemIntegrationInitRequest = true`
→ `SystemIntegrationInit()`
→ internal `InitSyncDone = false`
→ `Sync(fullUpdate=true)`
→ partial group 0
→ partial group 1
→ partial group 2
→ commit GET values if all groups succeed
→ internal `InitSyncDone = true`

Key correction:
`SystemIntegrationInitRequest` and `InitSyncDone` are internal host booleans, not protocol ParameterIDs.

`IntegrationMode` itself is the wire ParameterID, and `IsSystemIntegration` is simply `(IntegrationMode != 0)`.

`UpdateParameterFlow()` changes ownership of RoomValue, HeatCurve, HeatCurvePlus5, HeatCurveZero, HeatCurveMinus5:
- non-system integration: GET-on-sync
- system integration: SET-on-sync

This makes grouped synchronization / ownership a higher-priority local-mailbox hypothesis than another scalar ID/value probe.

### Identity/binding
`OnHEServiceBind()` compares DivisionID + BrandID + ProductID against allowed products before endpoint allocation.
This is confirmed on the HE/Z-Wave side only; mapping to AFC8..AFD3 remains unknown.


## 2026-09-24 refinement — 0x06 VERSION semantics and 0x0F application blocks

### 0x06 no longer treated as proven DCM/Online identity
Local experiments EXP129–132 materially refine the 0x06 interpretation:
- valid 0x06 responder causes `EXP` / `UITBR.KAART` to appear on the VERSION page;
- `AFD1` is rendered directly as version/10;
- tested `AFD0` values do not change the label/type;
- AFC8/AFC9/AFCB are not required for EXP-version display.

Protocol implication: `0x06` is proven as an accessory/expansion presence + metadata path. Calling it the DCM/Online device is no longer justified without additional evidence. It may still participate in Online integration, but that is now a hypothesis rather than a naming assumption.

### 0x0F application/settings role strengthened
Our own XTR captures contain native FC10 traffic to slave `0x0F`, including the established settings block beginning `0x03E8`. `0x03F4` (decimal 1012) follows the room setpoint and independently aligns with an external ATEC/DHP-AQ observation that 1012 is room-thermostat related.

External Discussion #143 material also reports 0x0F block starts including decimal 1000/1020/1040 and higher regions. These addresses and block lengths are hypotheses for XTR until locally observed. The external files are used as candidate generators only.

### Native 0x085F block
EXP133 partial passive capture locally observed an XTR `0x0F FC10` block at `0x085F`, count 5. This covers `0x085F..0x0863`, so the known transport ACK field `0x0861` is structurally inside a native controller block.

This strengthens:
- `0861` as a real field in a controller-side 0x0F block;
- interpretation of `AFCA=03E8 -> 0861=16` as a transaction-level interaction between the 0x06 accessory response path and a native 0x0F controller block.

It does not yet identify the complete block semantics.

### New native 0x04A6 block
EXP133 also observed a local XTR `0x0F FC10` block starting `0x04A6`, count 13. First captured payload was all zero except `0x04B0=0x4020`. Semantics are unknown. This block was not one of the imported external candidates and is therefore useful XTR-specific evidence.

### Current protocol priority
1. finish EXP133 and establish the native XTR 0x0F shape census;
2. use controlled passive UI correlations to map concrete fields (EXP134 starts with DHW START);
3. only after local read/correlation evidence, infer which 0x0F direction/block is appropriate for safe semantic write testing;
4. do not return to random AFC8..AFD3 payload guessing without new evidence.


## 2026-09-24 — Genuine Online capture changes the 0x0F / 0x06 model

New external evidence from a working Thermia Online installation:
- slave `0x0F` is a real responding Modbus slave in that installation;
- it ACKs FC16 writes and serves FC03 reads;
- controller-originated FC16 traffic cycles through large state/telemetry blocks;
- controller reads `0x03E8` from `0x0F`;
- during an intentional Heat Curve 20->21->20 change, the two captured `0x03E8` read snapshots differ only at the first word (`23 -> 22`);
- recurring `0x06` FC17 polls remain unanswered in the supplied working-Online capture;
- slave `0xA5` is active but unidentified.

Protocol implications:
1. `0x06` is still proven as an expansion/accessory interface but is not required for the Online function shown in this capture.
2. `0x0F` is strongly indicated as a shared controller <-> Online/DCM register interface.
3. Controller FC16 writes to `0x0F` likely carry controller->Online state.
4. Controller FC03 reads from `0x0F` likely consume Online->controller desired/config state.
5. Register direction/ownership is therefore central; a direct second-master write is not equivalent to emulating the expected slave-side register image.
6. Exact physical implementation of slave `0x0F` and the role of `0xA5` remain open.

EXP135/136 correction:
- `03F1` is not supported as live DHW START on the tested XTR M.
- DHW COMFORT/ECO does not alter recurrent `03E8..03F5`.
- `03F1`, `03F2`, `03F3`, `03F5` remain unknown.

Next controlled discriminator — EXP137:
ACK only exact known XTR slave-0x0F FC16 writes and observe whether controller FC03 reads begin. Do not answer FC03 in EXP137.


## EXP137 — acknowledged 0x0F synchronization progression

Local XTR result:
- passive baseline contains repeated `03E8/count14` and `085F/count5` writes with no slave ACK;
- after one standard FC16 ACK to `03E8/count14`, the controller begins issuing `0410/count22`;
- without an ACK, `0410/count22` is retransmitted continuously;
- no FC03 read phase appears before `0410/count22` is acknowledged;
- bus/parser health remains clean.

Protocol implication:
`0x0F` is not behaving like a fire-and-forget telemetry mirror. At least part of the controller->0x0F traffic forms an acknowledged sequential transfer/state machine.

New locally proven XTR block:
`0x0410..0x0425` (count 22).

This block contains external candidate `0x041D` (1053), so the address exists locally in the XTR transfer family, but no semantic label is yet proven.

Next controlled discriminator:
ACK `0410/count22` in addition to the already-used exact known shapes; continue to refuse all unknown shapes and never answer FC03.


## EXP138 prepared discriminator

EXP137 established a locally observed acknowledged progression:
`03E8/count14 -> ACK -> 0410/count22`, after which the controller stalled on repeated `0410/count22` because no ACK was returned.

EXP138 changes only one variable:
acknowledge that exact `0410/count22` request.

Protocol question:
Does `0410/count22` ACK advance the XTR controller to:
- another FC16 transfer block; or
- the FC03 read-side phase seen in the genuine Thermia Online capture?

No newly appearing block will be ACKed in EXP138. FC03 will not be answered.


## Raw-frame correction: 0x0848 Heat Curve follow-up
The follow-up GitHub analysis of the genuine Online capture over-interpreted the `0x0848` block.

Exact decoded words:
- ~12.116 s, `0848/count23`: `0858=0000`, `0859=0004`, `085A=0014`, ...
- ~33.107 s, `0848/count23`: `0858=0015`, `0859=0004`, `085A=0014`, ...

Thus:
- `0858` changes `0 -> 21`;
- `085A` stays `20`;
- no same-register `20 -> 21` transition exists in those two `0848` frames.

The later `07E4` frame is a different block and cannot be used as a same-register revert without additional evidence.

Status:
- `0858` = STRONGLY INTERESTING / Heat-Curve-change correlation candidate.
- exact semantics = OPEN.
- do not encode `0858 = Heat Curve` yet.


## EXP138 — next 0x0F sequence stage proven

Local XTR sequence now proven:
`03E8/count14 -> ACK -> 0410/count22 -> ACK -> 042E/count15`.

Important persistence observation:
After EXP137 ended while the controller was waiting for an ACK to `0410/count22`, an ESP reboot and new firmware did not reset the controller-side transfer state. EXP138's passive baseline immediately contained repeated `0410/count22`. Therefore the sequence state is maintained by the Thermia/controller side, not by transient ESP state.

New local block:
`0x042E..0x043C` (count 15; decimal 1070..1084).

This aligns structurally with the external DHP/ATEC block family at decimal 1070..1084, but individual semantics are not imported as proven XTR mappings.

Next discriminator:
ACK only `042E/count15` as the one new variable; stop without answering the first new FC16 stage or FC03 read.


## EXP139 prepared discriminator — ACK 0x042E/count15

Locally proven progression before EXP139:
`03E8/14 -> ACK -> 0410/22 -> ACK -> 042E/15`.

EXP139 changes one variable only:
acknowledge `042E/count15`.

This block covers `0x042E..0x043C` (decimal 1070..1084). Structural agreement with the external DHP/ATEC 1070..1084 family is noted, but no individual semantic labels are imported.

Positive:
- first new FC16 stage after a successful 042E ACK, or
- first 0x0F FC03 request.

Neither will be answered in EXP139.


## EXP139 — 0x0F sequence extends through 0x04A6 to 0x04BA

Observed local XTR progression:
`042E/count15 -> ACK -> 04A6/count13 -> ACK -> 04BA/count22`.

Combined with prior experiments:
`03E8/14 -> ACK -> 0410/22 -> ACK -> 042E/15 -> ACK -> 04A6/13 -> ACK -> 04BA/22`.

New locally proven block:
`0x04BA..0x04CF` (count 22; decimal 1210..1231).

Persistence:
After EXP138 ended while waiting at `042E`, EXP139 rebooted and immediately saw repeated `042E/count15`, again proving controller-side persistence of the transfer state.

Nuance:
`04A6/count13` had been observed before in passive XTR traffic and was already in the whitelist. Its appearance 0.52 s after the 042E ACK and the immediate transition to 04BA after its ACK strongly place it in the current transfer path, but exclusive sequence ownership remains unproven.

Next discriminator:
ACK only `04BA/count22` as the one new variable; do not answer the next new FC16 shape or FC03 request.


## EXP140 prepared discriminator — ACK 0x04BA/count22

Locally proven progression before EXP140:
`03E8/14 -> ACK -> 0410/22 -> ACK -> 042E/15 -> ACK -> 04A6/13 -> ACK -> 04BA/22`.

EXP140 changes one variable only:
acknowledge `04BA/count22`.

This block covers `0x04BA..0x04CF` (decimal 1210..1231). Exact semantics remain OPEN.

Positive:
- first new FC16 stage after a successful 04BA ACK, or
- first 0x0F FC03 request.

Neither will be answered in EXP140.


## EXP140 — 0x0F sequence extends to 0x05FF/count33

Observed local XTR progression:
`04BA/count22 -> ACK -> 05FF/count33`.

Combined proven sequence:
`03E8/14 -> ACK -> 0410/22 -> ACK -> 042E/15 -> ACK -> 04A6/13 -> ACK -> 04BA/22 -> ACK -> 05FF/33`.

New locally proven block:
`0x05FF..0x061F` (count 33; decimal 1535..1567).

Persistence:
After EXP139 ended while waiting at `04BA`, EXP140 rebooted and immediately saw repeated `04BA/count22`, again confirming controller-side persistence of the transfer state.

Next discriminator:
ACK only `05FF/count33` as the one new variable; do not answer the next new FC16 shape or FC03 request.


## EXP141 prepared — human-gated sequence walking

Transport evidence from EXP137–EXP140 is now strong enough to replace one-reflash-per-block with a bounded interactive walker.

Static exact ACK set adds the newly proven `05FF/count33`.
All later unknown FC16 shapes require:
- >=3 exact start/count repetitions;
- explicit HA ARM action;
- ACK only on the next exact request.

No unknown block is acknowledged merely because it appears. Full payloads are logged. FC03 is detection-only and never answered.

This preserves the evidence hierarchy: a newly discovered shape becomes an acknowledged experimental target only after repeated local observation plus explicit approval.


## EXP141 partial result — 0x0662/count33 discovered and gated

New locally proven stage:
`0x0662..0x0682` (count 33; decimal 1634..1666).

Observed progression:
`05FF/count33 -> ACK -> 0662/count33`.

The 0662 payload repeated identically and the EXP141 gate locked the candidate after 3 identical start/count requests. It was not automatically ACKed.

This validates the interactive-walker method itself: unknown stages remain blocked until explicit HA approval.

Semantics of the 0662 block remain OPEN.


### 0x0662/count33 ACK behavior
A single manually gated ACK to `0662/count33` stops the controller's repeated retransmission of that block.

No next FC16 stage or FC03 request is visible in the following ~11 s of the supplied log. This makes `0662/count33` a candidate phase boundary/terminal sync stage, but that interpretation remains HYPOTHESIS until longer post-ACK observation is captured.


## EXP142 prepared — 0x0662/count33 promoted to known ACK target

`0662/count33` is promoted from a manually approved EXP141 candidate to an exact static ACK target because:
- it repeated stably;
- it was manually approved;
- its standard FC16 ACK stopped the controller retry stream.

EXP142 uses the same bounded gated walker for any later unknown stages and watches specifically for post-0662 FC16 or FC03 activity.

Semantics of the 0662 payload remain OPEN.


## EXP142 partial — post-0662 quiescent state persists across reboot

After EXP141 manually ACKed `0662/count33`, EXP142 rebooted into a state with no slave-0x0F FC16 requests during the 30 s baseline and none during the following ~61 s active window.

Implication:
The acknowledged FC16 transfer state persists on the controller side beyond ESP reboot, and `0662/count33` is a strong candidate for the terminal block or phase boundary of the controller->0x0F startup/snapshot sequence.

This does NOT yet prove that 0662 is the final protocol stage. Further 0x0F activity may be event-driven or may require an Online-side request/handshake.


## EXP143 prepared — passive event trigger after completed FC16 sync

Post-0662 state is quiescent. EXP143 does not extend the ACK chain.

Instead it tests whether a known user-level setting event (Heat Curve +1, then restore) triggers 0x0F communication after sync completion.

The ESP remains receive-only for the entire experiment.


## EXP143 — manual Heat Curve change re-triggers 0x0F FC16 synchronization

Locally proven event trigger:
A user-level Heat Curve change on the Thermia UI reactivates `0x0F FC16 @ 0x03E8 count14` after the post-0662 quiet state.

Direct value evidence in controller->0x0F FC16 block 03E8:
- Heat Curve 36 -> first word `0x0024`
- Heat Curve 35 -> first word `0x0023`

Thus, for this FC16 write-side block and this experiment, word `0x03E8` directly mirrors the Heat Curve setting as an unsigned integer.

The controller repeats this block until ACKed.

Important:
Do not conflate this FC16 write-side representation with the values observed in genuine Online FC03 read responses. The two directions may represent different state/images or ownership domains.

Implication:
The quiet post-0662 state is event-reactivated by a settings change, giving a controlled way to restart the sync sequence without power cycling or reflashing.


## EXP144 prepared — event-triggered known-sequence walk

EXP143 established a controlled re-trigger:
manual Heat Curve change -> `0x0F FC16 03E8/count14`.

EXP144 now ACKs only already locally proven FC16 shapes after this trigger and observes what appears after the known sequence.

This distinguishes startup/recovery synchronization from a user-setting-triggered synchronization cycle without introducing any new semantic write target.


## EXP144 procedural result — event-triggered 0x03E8 retry persists across reboot

After EXP143 left `03E8/count14` intentionally unacknowledged, EXP144 rebooted and immediately observed the same repeated request with first word `0x0023` (35).

Therefore the event-triggered 0x0F FC16 retry state is controller-side persistent across ESP reboot, just like the earlier startup/snapshot ACK-gated sequence.

EXP144 itself did not test progression because it aborted on its intentionally strict quiet-baseline guard.


### EXP144 repeatability
The event-triggered pending `03E8/count14` retry state was reproduced across two additional EXP144 starts, each with the same payload first word `0x0023` and the same strict-baseline abort behavior.

This makes the controller-side persistence of the outstanding 03E8 stage highly repeatable.


## EXP145 prepared — transition probe, not more blind FC16 walking

The project focus is now explicitly the transition from the proven controller->0x0F FC16 snapshot path to the desired/read-side behavior seen with genuine Online hardware.

EXP145 resumes the persistent outstanding `03E8/count14` from EXP143/144, ACKs only locally proven shapes, and then stops transmitting after `0662/count33`.

The discriminator is what follows:
- `0x0F FC03` => read-side transition;
- new FC16 => missing transport stage;
- 120 s quiet => snapshot ACK completion is insufficient by itself.

A5/A4 FC03 activity is also logged passively because those addresses were active in the genuine Online capture.


## EXP145 — event-triggered FC16 update is distinct from startup snapshot sequence

A pending runtime Heat Curve update at `0x0F FC16 03E8/count14` was ACKed once. The retry stream stopped and no `0410/count22` or later startup-chain block followed.

Therefore:
- runtime/event-triggered FC16 synchronization can consist of a single changed block;
- the long `03E8 -> 0410 -> 042E -> ... -> 0662` sequence belongs to a different initialization/snapshot context;
- FC03 read-side traffic does not automatically follow ACK of the runtime 03E8 update.

This narrows the missing write-access mechanism to an Online-side/session trigger rather than further controller-originated FC16 acknowledgement.


## EXP146 prepared — test Online-side master hypothesis directly

The genuine Online capture repeatedly contains:
`0F 03 0708 0006`
followed by a 12-byte-data FC03 response, and then a `0F 03 03E8 000D` settings read.

EXP145 showed FC03 does not emerge automatically after ACKing a controller-originated runtime FC16 update.

EXP146 therefore tests a more direct architecture:
the Online module may actively be the master issuing FC03 reads to shared slave/mailbox 0x0F.

Only the exact read-only `0708/count6` request is transmitted in EXP146.


## EXP146 invalid — timing bug prevents interpretation

The exact genuine Online FC03 request `0F 03 0708 0006` was transmitted, but EXP146's timeout logic used a stale phase elapsed-time value. The nominal 2 s response window collapsed to roughly 10 ms.

No protocol conclusion can be drawn from the absence of a captured response.

The next experiment must repeat the same request with only the timing bug corrected; changing the address or protocol target before doing so would confound the result.


## EXP147 prepared — corrected repeat of EXP146

No protocol target is changed.

EXP147 repeats the exact genuine-Online read:
`0F 03 0708 0006`

The only change is procedural: the response timer now starts from the actual TX timestamp and the same interval callback exits immediately after sending.

This experiment is the valid discriminator for whether the local 0x0F endpoint answers an Online-style master read.


## EXP147 — bare 0x0F FC03 master read does not receive a local response

Exact request:
`0F 03 0708 0006`

A genuine >2 s observation window produced no decodable 0x0F response.

This weakens the simplest Online-side-master model in which the ESP can issue the same FC03 request without any prior Online/DCM session state.

Important logging note:
EXP147's terminal summary has a printf argument-count defect, so some printed counters are shifted. The protocol result remains interpretable from the independent timestamped TX line and >2 s later summary line.

Architectural implication:
The genuine Online environment likely provides additional topology/session state before 0x0F becomes readable. A5/A4 remains a prime candidate for that missing layer, but its exact role is still unknown.


### EXP147 repeatability
A second corrected-timing run again produced no response to:
`0F 03 0708 0006`
over a genuine ~2.24 s response window.

The direct-master-read negative is therefore reproducible, strengthening the need to identify the missing Online/DCM topology or session prerequisite before further FC03 address probing.


## EXP148 prepared — topology before more protocol stimulation

After two reproducible EXP147 negatives, the project stops probing additional 0x0F FC03 addresses.

EXP148 passively profiles the logical endpoints that distinguish the genuine Online capture:
A5, A4, 0x0F, and 0x06.

The goal is to determine whether the missing prerequisite is a topology/session layer rather than another register/address detail.


## EXP148 — A5/A4 absent locally for 300 s; 0x0F FC03 absent despite active FC16

A clean 300 s passive profile produced:
- A5 FC03: 0
- A4 FC03: 0
- 0x0F FC03: 0
- 0x0F FC16 writes: 280
- 0x0F FC16 ACKs: 0
- 0x06 FC17 requests: 69
- parser/drop deltas: 0/0

This establishes a strong topology difference between the local no-Online setup and the genuine Online capture.

The repeated ~254 ms 0x06 FC17 -> 0x0F FC16 `04A6/count13` timing is highly stable and likely scheduler-related, but semantic causation remains unproven.

Next protocol work should identify the owner/presence mechanism behind A5/A4 and the genuine 0x0F FC03 responder before any new semantic write attempt.


## EXP149 prepared — direct A5 ownership discriminator

The genuine Online capture repeatedly polls A5 with:
`A5 03 0000 0012`
and receives 36 data bytes.

EXP148 showed A5/A4 are completely absent locally over 300 s.

EXP149 now asks the smallest ownership question possible:
does the local no-Online topology answer one exact genuine A5 read?

A negative result would strongly support A5 as an endpoint created/owned by genuine Online/DCM hardware rather than the heat-pump controller.


## EXP149 — exact genuine A5 FC03 read is unanswered locally

Stimulus:
`A5 03 0000 0012`

Observed:
No response during a clean 2.016 s window.

Combined evidence:
- EXP148: A5/A4 absent spontaneously for 300 s.
- EXP149: A5 also does not answer when directly queried.

Protocol implication:
A5 is strongly indicated to be an externally owned/created endpoint associated with genuine Online/DCM hardware or session state.

Do not continue arbitrary A5 register probing. The next useful discriminator is ownership/presence sequencing from the genuine Online capture.


## EXP150 prepared — efficient staged role-emulation bootstrap test

The project now tests device roles rather than additional arbitrary registers.

EXP150 uses a strict staged harness:
1. become only an ACKing slave for already-known 0x0F FC16 shapes;
2. arm byte-identical A5 responses for the three genuine discovery reads;
3. after the bootstrap window, retry the genuine 0x0F 0708/count6 read;
4. only if positive, test the genuine 03E8/count13 read.

This can determine in one run whether ACK-side presence changes the local topology, whether A5 discovery appears, and whether 0x0F read-side service becomes available.

Unknown frame shapes abort rather than being generalized.


## EXP150 — ACK-only 0x0F presence does not enable FC03 or A5/A4 discovery

Phase 2 ACKed two known pending controller writes:
`04A6/count13` then `0662/count33`.

No A5/A4 or spontaneous 0x0F FC03 appeared.

After this bootstrap, the exact genuine Online read:
`0F 03 0708 0006`
still received no response during a clean 2.015 s window.

Protocol implication:
The read-side service is not unlocked merely by acknowledging controller-to-0x0F transfers. A stronger architectural possibility is that the real Online/DCM module simultaneously occupies both the `0x06` accessory role and the `0x0F` mailbox/service role, with A5/A4 as an additional discovery endpoint.

## EXP168 key finding — combined 0x06 presence + 0x0F ACK is insufficient

EXP168 deliberately exercised the exact runtime combination that EXP167 could not reach naturally: proven `0x06` presence plus one deliberately triggered and ACKed controller-originated `0x0F FC16 0x03E8/count14` event.

Observed: 155 valid `0x06` responses; 1 exact `0x0F FC16 03E8/count14` request; 1 exact ACK; first FC16 payload word `36 / 0x0024`; no A5; no A4; no `0x05`; no `0x0F FC03`; `resyncDelta=0`, `dropDelta=0`.

### Protocol implication

The combined transport-role hypothesis is now negative: a syntactically and behaviorally valid `0x06` responder plus a working ACK-side `0x0F` role does **not** reproduce the genuine DCM/Online service state.

This materially strengthens the architectural model that the real DCM topology contains an additional discovery/binding/service-availability/ownership layer not represented by simple Modbus request/response participation.


## EXP169–182 — extended scheduler / Online-DCM architecture refinement

### Genuine `0x0F` mailbox read side

The strongest source-proven command-ingress sequence is now:

```text
controller -> 0x0F: FC03 0708/count6
DCM        -> controller: 0000 0001 0000 0000 077F 0006
~40 ms later
controller -> 0x0F: FC03 03E8/count13
DCM        -> controller: desired heating-state image
```

This exact `word1=1 -> 03E8/count13` sequence occurred twice in the genuine command-event capture.

When the `0708` response is the normal steady form:

```text
0000 0000 0000 0000 077F 0006
```

the immediate `03E8/count13` desired-state read does not occur.

### `0708/count6` is mailbox/session state, not heartbeat

Across the genuine captures, currently observed variants are:

| w0 | w1 | w2 | w3 | w4 | w5 | Observed context |
|---:|---:|---:|---:|---:|---:|---|
| 0000 | 0000 | 0000 | 0000 | 077F | 0006 | steady runtime |
| 0000 | 0001 | 0000 | 0000 | 077F | 0006 | heating desired-state pending |
| 0000 | 0000 | 0000 | 0000 | 0080 | 0006 | controller-boot transient |
| 0000 | 0000 | 0000 | 0000 | 0000 | 0006 | later controller-boot transient |
| 0000 | 0000 | 7FFF | FFFF | 0080 | 0007 | DCM rejoin / synchronization transition |

Exact semantic names for w2..w5 remain open.

### DCM rejoin is a different direction

The rejoin header:

`0000 0000 7FFF FFFF 0080 0007`

is followed by controller-originated **FC16** state/configuration resynchronisation beginning at `03E8`.

Do not conflate this with the command-pending path, where `word1=1` causes a controller-originated **FC03** desired-state read.

### Extended runtime service scheduler

The reference Online/DCM controller runs a coherent cyclic family:

- `FC03 0708/count6`;
- FC16 runtime uploads at `07D0, 07E4, 07F8, 080C, 0820, 0834, 0848, 0864, 0870, 0884`;
- A5 plus related A4/05 service/discovery traffic.

During DCM rejoin, `0708` polling and repeated pending `0870/count17` uploads are already generated while the DCM is still silent. This proves that the scheduler is owned by the controller, even though physical DCM presence may still have been involved in enabling that topology earlier.

### Local XTR discriminator

The tested XTR M has genuine native `0x0F` state/settings traffic, including `03E8`, `04A6`, `085F` and the `0861` ACK field.

The indexed local corpus does not show the reference system's full extended runtime service family:

- no spontaneous `0F 03 0708 0006`;
- no confirmed cyclic `07D0..0884` family;
- no normal A5/A4/05 service topology.

Protocol implication:

**The missing prerequisite is upstream of the mailbox payload.** It is most likely a controller topology/integration/scheduler state rather than a single register encoding.

### Controller fingerprint correlation

Reference and local controllers also differ in the `0x02 FC17 A7F8` transaction/fingerprint:

- local: readCount 15, `A811/A812 = FFFF/0000`;
- reference: readCount 13, `A811/A812 = 000C/0500`.

Active `0x06` presence and a Heat Curve A/B/A change do not alter the local fingerprint. This is a useful structural marker but not yet proven causal.

### Stop rules after EXP181/182

Do not repeat:

- AFCA response-delay/timing variants;
- direct master-originated `0x0F FC16 03E8` semantic writes;
- passive topology census already covered by EXP175;
- standalone local `0708` reads already covered by EXP147/150;
- local `0708` response spoofing when the controller did not request it.

### Highest-value next evidence

A same-controller cold-boot A/B capture:

1. genuine DCM connected;
2. DCM physically absent.

This can distinguish physical accessory recognition from fixed model/firmware/configuration differences and may expose the first event that enables the extended scheduler.


## EXP184–185 — semantic export layer and raw firmware integration model

### Exact Danfoss Link 2.7.42 HPNode sync groups

Recovered directly from `RegulationEngine.dll` constructor IL:

| PartialUpdateIndex | Semantic parameters |
|---:|---|
| 0 | HeatPumpType, OperationMode, IntegrationMode, RoomValue, ExternalControl1, ExternalControl2, ExternalControl3, DefrostDemand, AlarmField1..5, ErrorCode |
| 1 | HeatCurve, HeatCurveMin, HeatCurveMax, HeatCurvePlus5, HeatCurveZero, HeatCurveMinus5, HeatStop, RoomFactor, HotWaterStart, ControllerDemand, OperationStatus |
| 2 | OutdoorTemperature, AuxiliaryHeaterPowerStage, HotWaterTemperature, SupplyLineTemperature, ReturnLineTemperature, EVU_SW, EVU_HW |

All three groups are used by the full synchronization routine. The grouping is semantic; it does not map one-to-one onto three contiguous `0x0F` Modbus address regions.

### IntegrationMode lifecycle

`IntegrationMode` is constructed as an internal byte parameter with:
- GetOnSync = true
- SetOnSync = true
- ClearSetOnSync = true
- UseLateCommit = true
- PartialUpdateIndex = 0

A parameter update invokes `OnIntegrationModeParameterUpdated()`, which raises a system-integration init request and regulation request. The regulation path performs `SystemIntegrationInit()` and a full grouped sync.

Internal configuration of system integration is also persistent/default-driven: `HPNode::Load` reads XML attribute `SystemIntegration`, while `SetDefaultSettings` uses a factory setting loaded from `HPNodeDefault/SystemIntegration[@Value]`. No direct bind-handler-to-`set_IsSystemIntegration` call was found in the recovered RegulationEngine call graph.

### Mailbox bridge hypothesis

The genuine command path:

```text
0708 response word1 = 1
        -> FC03 03E8/count13
        -> heating desired-state image
```

now has a strong semantic parallel in firmware **partial update group 1**, which starts with HeatCurve and contains the principal heating settings. This suggests that the six-word `0708` header may include per-group dirty/command selectors.

This remains **hypothesis**, not proof:
- only selector value `word1=1` has been observed for a command event;
- firmware group 1 contains 11 semantic parameters whereas the DCM response at `03E8` carries 13 contiguous Modbus words;
- the DCM03 serializer is still missing from the Link CC firmware.

### Scheduler-gate implication

The raw firmware weakens the simple idea that `IntegrationMode` itself is the missing local scheduler gate. It is best treated as an application ownership/synchronization mode that operates after a valid integration path exists. The controller-side condition that creates/enables A5/A4/05 + `0708` + `07D0..0884` remains unresolved.



## EXP186–187 — mailbox selector scope

The genuine command pattern is:

```text
0708 response: 0000 0001 0000 0000 077F 0006
                         ^
                         w1
~40 ms later
FC03 03E8/count13
```

This occurred twice during Heat Curve changes.

The `03E8/count13` response is a contiguous native image covering `03E8..03F4`. Confirmed or strongly mapped fields in this range include the heating-curve family, Heating Stop, Room Factor and room-setpoint-related state. The public Online dump independently confirms writable native indices through the same heating range.

Danfoss Link HPNode partial group 1 overlaps semantically with this family, but it contains eleven semantic parameters and is not directly identical to the thirteen native wire words.

Protocol implication:
- `w1=1` = strongly supported heating/settings-family pending selector;
- `w1 == firmware PartialUpdateIndex 1` = plausible architectural correlation, not yet proven identity;
- `w0 -> group0` and `w2 -> group2` remain hypotheses only;
- rejoin `w2=7FFF,w3=FFFF,...` is session/resync state, not evidence for a normal group-2 command.


## EXP188 — Link-side binding is distinct from Thermia-bus scheduler activation

Raw Danfoss Link 2.7.42 IL shows the HeatPump endpoint identity and creation path:
- HEATPUMP maps to DivisionID 6, BrandID 0, ProductID 0x0203.
- OnHEServiceBind checks the incoming physical address and allowed DivisionID/BrandID/ProductID tuple before endpoint creation.
- NodeManager.CreateNode creates an HPNode for NodeType HEATPUMP.
- Link's service UI writes IHPNode.IsSystemIntegration directly from the user's System Integration selection.

Protocol implication:
Link/HE side: device identity -> bind -> HPNode -> SystemIntegration choice -> grouped sync.
Thermia RS485 side: controller/accessory topology recognition -> unresolved gate -> A5/A4/05 + 0708 + 07D0..0884.

Do not collapse these two layers. The Link firmware does not demonstrate that IntegrationMode is the local Thermia scheduler gate. It demonstrates a higher-level semantic ownership mode after a heat-pump endpoint already exists.


## EXP189 — activation versus maintenance of the extended topology

The two genuine power-event captures now separate two states:

1. **Topology active** — controller emits the reference 0x02 fingerprint, services 0x04/A5 and runs the extended 0x0F scheduler.
2. **DCM session attached** — DCM actually answers 0x0F mailbox/state traffic.

Evidence:
- During controller boot with a powered DCM, 0x04 is already operational before the first visible 0x0F FC16 ACK, and A5 follows shortly after. The first 0708 poll occurs much later.
- During DCM power-up/rejoin with the controller left running, the extended scheduler continues for about 66 s while the DCM remains silent.

Protocol implication: extended topology **activation** and DCM **session attachment** are not the same transition. The controller can maintain the topology without a currently responding DCM. This favors a very-early/latched topology-selection mechanism over a mailbox-triggered one.

The local XTR no-DCM baseline proves that C8, 0x06, AFDC/A80E lifecycle state and ordinary 0x0F FC16 traffic are not sufficient to select that topology.


## EXP190 — 0x02 A80C..A812 field classification

Current classification from local/reference boot + steady comparisons:

| Register | Current interpretation |
|---|---|
| A80C | shared controller/context field; 0040 in compared normal states |
| A80D | shared zero in compared states |
| A80E | dynamic lifecycle field; not DCM/session-specific |
| A80F | dynamic lifecycle field; boot/runtime value changes |
| A810 | dynamic lifecycle field; tracks A80F in observed boots |
| A811 | static structural discriminator: local FFFF, reference 000C |
| A812 | static structural discriminator: local 0000, reference 0500 |

Local A7F8 read-count is 15; reference is 13. In the observed local response, the two extra words at the end of the larger read span are unavailable/sentinel values, so the span difference is best treated as controller-layout/generation evidence rather than a demonstrated Online-state bit.

A811/A812 are not yet semantic controls. Their values could reflect product family, firmware layout, commissioned capability or topology state. No write is justified.


## EXP191 — model-specific outdoor nodes behind a semantic export layer

Reference topology uses slave 0x04 FC17 (ABE0/count12 + ABF4/count4) as a continuously active source. Local XTR/iTec topology instead uses slave 0x1E as the outdoor-unit/COMM-KIT source and has no normal slave-0x04 traffic.

The reference 07E4/count17 runtime export is derived from the immediately preceding 0x04 transaction rather than copied byte-for-byte. Most source response words are preserved, unavailable FC18 values are normalized to FF9C, and extra/request-derived values are inserted.

Implication:

```text
model-specific internal node
  reference: 0x04
  XTR/iTec:   0x1E
        ↓
controller semantic adapter / serializer
        ↓
DCM-facing runtime export group
```

Therefore exported runtime groups should be interpreted by semantic role, not by fixed internal slave address.

A811/A812 remain structural correlates only. In particular, A812=0500 must not be interpreted as a 0x05-node presence map from numeric coincidence alone.


## EXP192 — additional DCM runtime-export semantics

### 07F8
Strong cross-capture correlation with the controller's 0x0A write image:
- controller 0x0A B3C4..B3C6 = `[17,20,0]` -> `07F8` word15 = 17;
- `[14,21,0]` -> word15 = 14;
- `[14,20,0]` -> word15 = 14.

Therefore `07F8` is source-derived from the room-sensor/controller environment path, but is not a raw 3-word mirror.

### 0848
`0848/count23` words16..22 are proven:
`second, minute, hour, day, month, two-digit year, weekday(Monday=0)`.

### 0884
`0884/count60` decomposes into ten records of six words. The observed records are strictly reverse chronological when decoded as:
`code, minute, hour, day, month, year`.
This is strong evidence for a ten-entry event/history table. Codes 2, 41, 42 and 44 remain unmapped.

### 0870 / 0864
`0870/count17` is invariant across all checked captures, including DCM-silent operation, and is currently classified as persistent/static configuration or identity data. `0864/count4` is invariant `[0,0,0,22]`; semantics unknown.

### 080C / 0834 caution
The first words are 0x00C8 and 0x001E respectively, but this alone does not prove linkage to slave C8 or 0x1E. Treat those as unresolved until a value transition or independent source mapping exists.


## EXP193 — special runtime blocks are semantic datasets, not slave-ID mirrors

- `080C word0=00C8` does **not** identify a raw C8 mirror: steady captures contain `080C` while C8 traffic is absent.
- `0834 word0=001E` does **not** identify a raw 0x1E mirror: the reference captures contain no slave-0x1E traffic.
- `080C word14` strongly correlates with controller 0x06 write field AFDC: AFDC=0 -> word14=0; AFDC=16 -> word14=16 across the checked genuine captures. Classify `080C` as an accessory/lifecycle semantic dataset.
- `0834` is not a direct A5 copy; its word12 changes 70->0 across steady vs boot while the apparent A5 30/70 source values remain present.
- `0848` exports current RTC/date.
- `0884/count60` is strongly identified as Thermia ALARM HISTORY: exactly ten 6-word entries with alarm type/code + minute/hour/day/month/year, matching official iTec documentation that the menu stores up to ten alarms with type, time and date. Numeric alarm codes 2/41/42/44 remain unresolved.


## EXP194 — 0870 operating-time/defrost block; 0864 hidden service extension

### 0870/count17 = indices 2160..2176

The native hex start `0x0870` is decimal 2160, exactly matching Thermia Online registerIndex numbering.

Confirmed public Online labels within the block:

| Index | Online name | Genuine reference raw |
|---:|---|---:|
| 2160 | REG_OPER_TIME_COMPRESSOR | 21966 |
| 2162 | REG_OPER_TIME_HEATING | 9763 |
| 2163 | REG_OPER_TIME_COOLING | 10 |
| 2166 | REG_OPER_TIME_HOT_WATER | 12091 |
| 2167 | REG_OPER_TIME_IMM1 | 124 |
| 2168 | REG_OPER_TIME_IMM2 | 170 |
| 2169 | REG_OPER_TIME_IMM3 | 0 |
| 2171 | REG_DEFROSTS_MA_SA | 3122 |
| 2172 | REG_DEFROSTS_BETW2DEFR_MA_SA | 422 |
| 2173 | REG_DEFROST_TIME_LAST_DEFROST_MA_SA | 15462 |

Unexposed indices 2161,2164,2165,2170,2174..2176 remain unknown.

The data are self-consistent:
- compressor 21966 h versus heating+cooling+hot-water 21864 h;
- compressor-hours-to-defrost-count gives `21966*60/3122 = 422.15 min`, essentially identical to index2172=422.

Therefore 0870 is **operational lifetime / defrost statistics**, not identity or scheduler state.

### 0864/count4 = indices 2148..2151

Observed payload: `0,0,0,22`, invariant in checked genuine captures.

No public Online profile checked exposes indices 2148..2151. The range is structurally adjacent to the local/native `085F/count5` block at 2143..2147, which includes the proven 0861 transaction ACK field. This makes 0864 a plausible hidden service/capability/status continuation, but no field semantics are proven.

Do not infer the value 22 as a software version and do not write any field in 2148..2151.



### EXP194 refinement — Online registerIndex namespace pattern

Converting the cyclic FC16 block starts from hex to decimal reveals a deliberate Online-index layout:

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

This matches the stable `registerIndex` namespace exposed by public Thermia Online profiles (for example 2000 supply temperature, 2023 outdoor temperature on ATEC-family data, 2120/2121 operational status/PID or desired supply depending profile, and the now-proven 2160+ operating-time family).

**Strong architectural conclusion:** the extended controller scheduler is best understood as publishing/populating the DCM-facing Thermia Online register-index database in slave 0x0F. The FC16 blocks are contiguous database pages/semantic groups, not arbitrary private command blocks.

Consequently, 0864 is controller->DCM exported state at Online indices 2148..2151. Even if those words eventually prove to contain a capability/topology marker, they are an **output/reflection** of controller state, not a justified ingress/write target for activating the scheduler. The activation gate must sit upstream of the publisher.


## EXP195 — 085F and 0864 are adjacent but scheduler-distinct

### 085F/count5 — indices 2143..2147
Current classification: **initialization / synchronization / service-control page**.

Evidence:
- exists on the local XTR without a genuine DCM;
- contains 0861, the proven AFCA transaction ACK field;
- absent from checked steady genuine Online captures;
- appears after/between startup synchronization activity in 090209;
- repeats at ~4.2 s cadence throughout the 090550 DCM full-resync interval.

It is therefore not a DCM-topology presence bit and not the trigger for the full resync: in the rejoin capture the DCM join header at 68.235 s already causes the full FC16 resync before the first 085F at 73.235 s.

### 0864/count4 — indices 2148..2151
Current classification: **extended steady-runtime Online export page**.

Evidence:
- appears once per normal 10-slot runtime cycle in steady genuine Online captures;
- invariant observed payload `[0,0,0,22]`;
- not observed as the local no-DCM 085F service block;
- appears only after the extended runtime exporter is already active.

### Scheduler implication
Do not merge 085F+0864 into one nine-word semantic object solely because their native indices are adjacent.

Best current state machine:

```text
topology/session already selected
        ↓
full initialization/resync
        ├─ 085F service-control page (repeated)
        └─ 0708 mailbox mostly suppressed
        ↓
steady runtime
        ├─ 0708 mailbox ~4.2 s
        └─ 07D0..0884 export cycle, including 0864
```

The similar ~4.2 s cadence of resync-time 085F and steady-state 0708 is a useful hypothesis for a shared service timer/state machine, but is not yet proven.



## EXP196 — registerIndex 2060 confirms runtime database semantics

The runtime page `080C/count18` starts at decimal registerIndex 2060.

Public Thermia Online debug profiles independently expose:

```text
2060 = REG_INDOOR_TEMPERATURE
step = 0.1
```

on both ATEC/DHP-AQ and iTec IQ families.

The genuine runtime payload starts:

```text
080C/count18:
00C8 0000 0000 ...
```

`0x00C8 = 200`, which decodes naturally as **20.0 °C** at 0.1 scaling.

Therefore:
- `080C.word0` is strongly identified as indoor temperature;
- the value 00C8 is not evidence of slave C8 identity;
- the Online/DCM runtime FC16 pages share the public Thermia Online registerIndex namespace semantically, not only numerically.

The same public profiles show model-dependent differences around index 2120 (ATEC: Integral LSD; iTec: PID), so cross-model semantics must not be copied blindly.

Indices 2143..2151 remain absent from the checked public API profiles and are best treated as internal/private service-status fields until independently mapped.



## EXP197 — 0559 LIGHT is compatible with full Online/DCM topology

Genuine full synchronization includes `0x0F FC16 0546/count20`, ending exactly at 0559.

Using the ATEC/DHP-AQ Online register map:

```text
0553 = REG_OPERATIONMODE
  0 OFF
  1 AUTO
  2 COMPRESSOR
  3 AUXILIARY
  4 HOT_WATER

0559 = REG_LINK_INTEGRATION
  0 LIGHT
  1 SYSTEM
```

The two genuine power-event snapshots decode:

```text
090209: 0553=4, 0559=0
090550: 0553=4, 0559=0
```

Yet both captures have the extended A5/0x04/0x0F topology active.

Protocol implication:
**Link Integration SYSTEM is not the scheduler-enable condition.** LIGHT mode coexists with the full Online/DCM transport/export scheduler.

This aligns with the firmware-side conclusion that SystemIntegration controls semantic ownership/synchronization after a heat-pump endpoint exists, rather than creating the endpoint/topology itself.

Do not use a guessed 0559 write as a topology activation experiment.



## EXP198 — startup tail 06EA/06F1/06F4

### 06EA/count7
Proven RTC/calendar snapshot:

```text
word0 second
word1 minute
word2 hour
word3 day
word4 month
word5 year (two-digit)
word6 weekday (Monday=0)
```

090209: `22,6,8,25,9,26,4`.
A later 0848 runtime page contains the same date/time tuple with seconds advanced consistently with capture elapsed time.
090550: `14,11,8,25,9,26,4`; encoded clock delta relative to 090209 matches logger delta to within ~0.2 s.

### 06F1/count3
Observed `FFFF,FFFF,FFFF` in both genuine power-event captures. Treat as unavailable/reserved/private until independent evidence exists.

### 06F4/count19
Observed in controller cold boot only in the current genuine corpus. First five words:

`0040,0000,0028,000A,000A`

exactly match the contemporaneous 0x02 FC17 write image A80C..A810. The A811/A812 structural discriminator values 000C/0500 are not copied there.

Protocol implication: 06F4 is a controller-state/bootstrap snapshot, not demonstrated identity ingress. Because reference topology is already active before it is emitted and DCM rejoin does not require it, do not treat 06F4 as scheduler activation.



## EXP199 — DCM is not the Danfoss Link SIMPLE_COMMUNICATION_MODULE node

Recovered 2.7.42 firmware distinguishes:

```text
NodeType 16 GATEWAY                     -> Div 7 / Brand 0 / Product 0x0201
NodeType 17 HEATPUMP                    -> Div 6 / Brand 0 / Product 0x0203
NodeType 19 SIMPLE_COMMUNICATION_MODULE -> Div 5 / Brand 0 / Product 0x8100
```

`SCMNode` is built around `InputStateBinary`, `InputShifts`, `HCPowerCycleCounter` and a 30-minute check-in interval. Its state-change callback ultimately raises Link `AwayModeChanged`.

Therefore SCM is an external/simple-input communication node, not the Thermia Online/DCM transport bridge.

Architectural implication:

```text
Thermia-side topology recognition
        ↓
DCM transport/service bridge
        ↓
HE service sees heat-pump device identity
        ↓
HEATPUMP endpoint (Div6 / Product0x0203)
        ↓
HPNode / Link application
```

The recovered Link node model does not expose a separate DCM/Online node whose ProductID can simply be replayed on the Thermia RS485 bus.



## EXP200 — XTR distinguishes DCM-present from Online-connected

The exact iTec XT/XTR user guide exposes two separate UI states:

DCM ACCESSORY INSTALLED
= DCM or Thermia Connect accessory connected

ONLINE CONNECTION
= DCM or Thermia Connect connected + Internet connection

Protocol implication: do not collapse physical/local DCM recognition, DCM session attachment, and cloud connectivity into one state.

Current layered model:

physical / commissioned accessory recognition
-> extended Thermia topology + publisher
-> DCM service/session attachment
-> DCM Internet/cloud connectivity

The older DHP-AQ HP-kit installation sequence corroborates automatic bus-side discovery: DCM03 is physically connected to a spare relay-board RJ45/RS485 path, the heat pump is started, then DCM03 is paired on the Link side; no heat-pump menu switch is documented for enabling the DCM.

A811/A812 are worth retaining as passive candidates for the first layer, but their semantics are unproven.



## EXP201 — A811/A812 fit persistent topology better than live DCM session

Exact XTR documentation provides a useful semantic distinction:

- DCM accessory installed = local accessory connected/recognized;
- Online connection = accessory connected plus Internet.

Against that model, the controller 0x02 write-image pair behaves as follows:

local no DCM: A811/A812 = FFFF/0000
genuine reference: A811/A812 = 000C/0500

During the 090550 DCM power-up/rejoin capture, the reference pair stays 000C/0500 throughout the long DCM-silent interval, the first mailbox response, full resync, and return to runtime.

Therefore the pair does not represent current 0x0F session readiness. If it is DCM-related at all, it is more consistent with an installed/commissioned topology or controller capability reflection.

EXP173 independently proves that live 0x06 accessory/version presence alone does not change FFFF/0000 to the reference values.

No write to A811/A812 is justified.



## EXP202 — DCM UI state is not an obvious public Online register

Checked public Thermia Online debug profiles expose DCM information primarily as device metadata:
- dcmVersion
- deviceConnectionType = Dcm

No ordinary registerIndex matching the exact XTR UI concepts DCM accessory installed or Online connection was found.

Model-specific COMP_HAS_LINK fields exist at different high indices (Diplomat 6003, ATEC 7003, iTec IQ 10003), but the checked DCM-connected profiles report value 0. They must not be interpreted as a generic DCM-present flag.

Protocol implication:
the XTR display's local DCM-recognition state is likely private controller/display state or capability metadata rather than a normal public 0x0F Online parameter.

This increases the value of passive 0x02 write-image mapping and decreases the value of searching further public user-setting indices for the topology gate.



## REVIEW EXP183–EXP202 — corrected confidence model

The following protocol statements supersede stronger wording in earlier entries:

- "runtime-latched" is supported for the reference topology while the controller remains powered; "persistent/nonvolatile latch" is not.
- A811/A812 = FFFF/0000 vs 000C/0500 is a cross-system architecture/topology correlation, not a proven DCM-presence bitfield.
- 0x04 and 0x1E may fill analogous subsystem roles across controller families, but functional equivalence is unproven.
- 080C.word14 tracks AFDC in observed 0/16 states; direct source provenance is unproven.
- 085F is a service/status page that participates in local operation and full resync; its exact control/state-machine role remains open.
- SIMPLE_COMMUNICATION_MODULE / ProductID 0x8100 must be treated as unresolved with respect to DCM03. SCMNode behavior does not justify a categorical exclusion.
- Public Online-profile absence does not prove the XTR DCM-installed status lives outside 0x0F; it only shows that no obvious public register was found.
- EXP201 does not establish A811/A812 as the XTR DCM-installed indicator because the local/reference comparison is model/topology-confounded.

Still strong:
- 0708.w1=1 -> immediate 03E8/count13 heating/settings fetch.
- ordered ACK-gated 07D0..0884 exporter.
- Thermia Online registerIndex alignment, including 0870 operating-time/defrost block.
- 0559=SYSTEM not required for the genuine extended scheduler.
- 06EA RTC/date.
- 0884 ten-entry timestamped alarm/history structure.


## EXP203 — causal frontier of current captures

Earliest comparable cold-boot evidence:

```text
Local XTR no DCM (EXP164)
t=0 ms    first returned bus frame: 0x1E
t=317     0x0F FC16 04BA/count22
t=722     first logged 0x02 A7F8/count15, A811/A812=FFFF/0000
t=818     C8
t=1045    0x06
180 s     no A4/A5/05/0x0F-FC03

Reference with DCM present (090209)
t=31 ms   first visible frame: 0x02 A7F8/count13, A811/A812=000C/0500
t=130     C8
t=251/290 0x04 request/response
t=389     ACKed 0x0F FC16
t=1179    A5 active
```

The two branches are already different at the first available controller frame. Because they are different physical/controller systems, the differing fingerprint cannot distinguish platform identity from DCM-installed topology state.

090550 adds a different fact: an already-enabled topology survives DCM service silence and later accepts a DCM rejoin. It does not show topology creation.

**Protocol implication:** the activation gate lies upstream of all ordinary mailbox/export behavior observed so far. Current captures establish consequences and maintenance of the topology, not its creation.

The project has reached an evidence boundary for the scheduler gate with the existing logs. The decisive capture is same-controller cold boot with genuine DCM present versus absent.



## EXP204 — controller-side firmware remains the missing implementation layer

No usable heat-pump controller/relay-board firmware image was found in the checked Project, Library, public web or GitHub sources.

Official DHP-AQ Link documentation gives an important cross-model clue:
- Link integration requires DHP-AQ controller software >=2.2;
- compatibility documentation directs installers to replace the display card when the software is older than 2.2.

Therefore DCM/Link support is at least generation/software-capability dependent on DHP-AQ. This does not prove how iTec XTR selects the topology, but it makes a pre-bus controller capability/configuration gate plausible.

The recovered Danfoss Link CC firmware remains valuable for HE/HPNode semantics, but it should not be expected to contain the lower Thermia-controller RS485 topology bootstrap.


## EXP205 — no documented spare DCM-detect line on the direct path

Observed XTR RJ45 wiring accounts for all eight contacts as two duplicated conductors for one bus line, two duplicated conductors for the other bus line, two grounds and two +12 V supply conductors.

Official DHP-AQ DCM03 installation uses a separate DCM03 power supply and a communication cable from the spare relay-board RJ45 to the DCM03 port explicitly labelled RS 485. No separate detect/ID conductor, strap or jumper is documented for that direct-connection path.

Protocol implication:
- a dedicated spare-wire presence signal is currently unsupported;
- if physical recognition exists before framed traffic, it would more likely have to use the RS485 pair's electrical state/load or a controller-side persisted/capability state;
- byte-level captures cannot prove or exclude such analog detection.

Do not alter termination/bias/loading as an experimental bootstrap target without reference electrical evidence.


## EXP206 — physical DCM removal/rejoin and second mailbox selector

With DCM removed from Modbus and power-cycled while disconnected, the running controller continued its reference fingerprint, A5, 0x04, 0x06 polling, unanswered 0708 polling and ACK-gated export retries. The complete capture contains 33 controller 0x06 FC17 polls and no 0x06 response frames, yet genuine DCM service later rejoins and normal runtime resumes. Therefore DCM electrical presence is not required to maintain an already-selected topology, and the 0x06 accessory/version path is not required for genuine DCM session reattachment in this captured topology.

Observed rejoin sequence: pending 0864 request -> ACK; next 0708 -> [0,0,7FFF,FFFF,0080,6]; immediate full resync from 03E8; steady 0708 resumes; runtime exporter resumes.

Because A5 request/response traffic continues during the interval when the capture owner states that the genuine DCM is physically off the Modbus bus, the removed DCM itself cannot be the physical A5 responder on that bus. A5 should now be treated as a topology-associated native/upstream service with hardware ownership still open.

After resync, steady 0708 is repeatedly [0,0,0,0,0,6]. A later command selector [1,0,0,0,0,6] is accepted and triggers 0546/count20, so word4=077F is not a generic required ready/online marker for command dispatch.

Both [0,0,7FFF,FFFF,0080,7] from 090550 and [0,0,7FFF,FFFF,0080,6] from EXP203 trigger full resync. w5=7 is therefore not a required join marker.

Second selector: 0708 [1,0,0,0,0,6] -> FC03 0546/count20, which includes known OperationMode 0553 and Link Integration 0559. Previous mapping remains w1=1 -> FC03 03E8/count13 heating/settings. Current model: w0 selects a system/status desired-state family strongly aligned with firmware partial group 0; w1 selects the heating/settings family strongly aligned with partial group 1; normal w2 selector remains unobserved.


## EXP207 — DCM slave-0x0F responder timing model

Offline timing analysis across all five genuine DCM captures shows a consistent normal-response pattern at 9600 8E1:

- FC16 write ACKs are normally seen 13–15 ms after the request frame has completed. The 8-byte ACK itself occupies about 9.17 ms on the wire, leaving roughly 4–5 ms of silent turnaround.
- 0708/count6 FC03 responses are 17-byte frames and complete 23–26 ms after the request, implying a median pre-response silent interval of about 4.5 ms.
- 03E8/count13 responses are 31-byte frames and complete in 39–42 ms; 0546/count20 is a 45-byte response completing in 56 ms. Both imply the same approximately 4–5 ms pre-response delay.

This is consistent with ordinary Modbus-RTU inter-frame timing, not a long hidden DCM processing phase.

Protocol implication: once the controller has already enabled the Online/DCM topology, the observed DCM bus role can be implemented as a strict slave-0x0F state machine that responds only to controller-originated FC16 writes and FC03 reads after a normal RTU silent interval. The captured rejoin path does not require unsolicited 0x0F frames from the DCM.

This is an emulator-design result only. It does not reveal or bypass the controller-side scheduler/topology activation gate.

## EXP208 — next decisive external discriminator

The next highest-value evidence is a cold boot of the same genuine reference controller with the DCM physically absent before controller power-on. This directly tests whether the extended A5/A4/05 + 0708 + 07D0..0884 topology is selected from persistent/controller capability state or requires DCM presence during boot.

No local 0708 response or new semantic write is justified before that discriminator is available.


## EXP209 — physical endpoint ownership resolved for the genuine reference topology

The DCM disconnect/power-cycle/reconnect capture provides causal ownership evidence:

- A5 request/response traffic continues while the genuine DCM is physically disconnected from the Thermia Modbus bus.
- 0x06 is still polled by the controller but receives no responses anywhere in the capture.
- controller-originated slave-0x0F requests are unanswered while the DCM is absent.
- after DCM physical reconnection, the first returning DCM-side evidence is the standard slave-0x0F FC16 ACK, followed by slave-0x0F FC03 responses and full state resynchronisation.

**Protocol conclusion:** in this genuine Online installation, the DCM/Online bridge is the responding Modbus slave 0x0F. A5 is not the DCM endpoint. Slave 0x06 is a distinct accessory/version service and is not required for Online/DCM operation in this topology.

This supersedes older wording that the physical owner of slave 0x0F was unresolved.

## EXP210 — validated desired-state fields in the 0x0F registerIndex database

Independent Discussion #143 material reports registerIndex 1012 as room-thermostat related and 1053 as Hot Water Start, while a later sentence in the same source contradictorily names 1021 as the room thermostat.

Cross-check against the genuine captures resolves the room-target ambiguity:

- 090550 full sync: index 1012 = 20; repeated native room-sensor transaction write field B3C5 = 20.
- 073242 full sync: index 1012 = 21; repeated native B3C5 = 21.
- 071517: both observed 03E8/count13 state images contain index 1012 = 21; native B3C5 remains 21 throughout.
- index 1021 is 10 in both available full-resync images and does not track the 20/21 room target.

**Strong mapping:** registerIndex 1012 / 0x03F4 = room target / room-thermostat setpoint in the genuine reference Online database.

For registerIndex 1053 / 0x041D, both available full-resync images contain value 35. This is compatible with the independent Hot Water Start identification, but the project does not yet possess a same-system one-variable Hot Water Start A/B. Classification: **strong candidate, not yet project-proven**.

registerIndex 1000 / 0x03E8 remains locally proven as Heat Curve on the XTR controller->0x0F write side and is strongly supported as the matching desired-state field on the genuine DCM read side.

Control-path implication once the scheduler is available:
- heating/settings dirty selector -> 0708 word1=1;
- controller fetches 03E8/count13;
- desired-state image includes Heat Curve at 1000 and room target at 1012.

No local semantic write is justified solely by these mappings while the XTR still lacks the genuine 0708 scheduler.


## EXP211 — 03E8/count13 is the heating desired-state page

Public Thermia Online debug profiles for ATEC/DHP-AQ and iTec IQ expose the following writable registerIndex meanings directly:
- 1000 Heat Curve
- 1001 Heat Curve Min
- 1002 Heat Curve Max
- 1003 Curve +5
- 1004 Curve 0
- 1005 Curve -5
- 1006 Heat Stop
- 1008 Room Factor

These align position-for-position with the genuine DCM FC03 03E8/count13 values. Independent legacy control-register documentation aligns the otherwise hidden positions 1007 and 1009..1011 with Temperature Reduction and the Curve 2 family. EXP210 independently proves 1012 is the Room Target field by exact equality with native B3C5 across multiple genuine captures.

Current field confidence:
- 1000 Heat Curve — proven locally on XTR FC16, public-profile confirmed, strongly supported on genuine FC03 desired state
- 1001 Heat Curve Min — public-profile confirmed
- 1002 Heat Curve Max — public-profile confirmed
- 1003 Curve +5 — public-profile confirmed
- 1004 Curve 0 — public-profile confirmed
- 1005 Curve -5 — public-profile confirmed
- 1006 Heat Stop — public-profile confirmed
- 1007 Temperature Reduction — strong structural mapping
- 1008 Room Factor — public-profile confirmed
- 1009 Curve 2 — strong structural mapping
- 1010 Curve 2 Min — strong structural mapping
- 1011 Curve 2 Max — strong structural mapping
- 1012 Room Target — project-validated against B3C5

Protocol implication: 0708 word1 is now well explained as a heating/settings dirty selector. When asserted, the controller fetches a coherent heating desired-state image from the DCM at 03E8/count13.

Do not translate this into direct master-originated writes to the local XTR. The semantically correct direction remains controller FC03 -> slave-0x0F response after the genuine scheduler exists.
