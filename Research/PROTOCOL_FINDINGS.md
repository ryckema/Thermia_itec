# THERMIA PROTOCOL FINDINGS

Last updated: 2026-09-27 after EXP232

## Bus

- Modbus RTU-like framing
- 9600 baud
- 8 data bits, even parity, 1 stop bit
- valid Modbus CRC

## Important slaves

- 0x02: controller state/sequencer data
- 0x06: local expansion/accessory presence/version path; **not proven to be the Online/DCM endpoint**
- 0x0A: room-sensor path
- 0x0F: native controller application/settings/state serializer; genuine Online/DCM reference systems also use this role for mailbox/state exchange
- 0x1E: outdoor-unit path

## 0x06 FC17 expansion/accessory path

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

The **AFCA value** `03E8` is therefore a transport strobe/constant in this 0x06 transaction and must not be confused with native `0x0F` register address `0x03E8`, which is independently proven to belong to the Heating Curve/settings family.

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


## EXP151 prepared — simultaneous multi-endpoint presence test

EXP150 rejects 0x0F ACK-only presence as sufficient bootstrap.

EXP151 therefore combines:
- known-good 0x06 accessory transport presence;
- 0x0F FC16 ACK/mailbox presence;
- exact A5 discovery responses if requested.

This tests the architectural hypothesis that the real Online/DCM module must occupy multiple logical roles at the same time before its read-side service becomes available.

The experiment still withholds semantic settings transactions.


## EXP151 — valid 0x06 presence still does not expose 0x0F FC03 or A5/A4

The ESP maintained the known-good 0x06 REQ-low accessory image for 60 s:
`00FF,0001,0000,0001,0,0,0,0,0,0,0,0`.

Observed:
- 58 active 0x06 responses;
- fast transport cadence reproduced;
- no A5;
- no A4;
- no spontaneous 0x0F FC03;
- exact genuine `0F 03 0708 0006` read still unanswered.

No 0x0F FC16 write occurred during the combined-role phase, so the 0x0F ACK side was armed but not exercised.

Protocol implication:
The missing read-side service is not unlocked by ordinary 0x06 accessory presence. Evidence increasingly supports A5/A4 and the 0x0F FC03 responder being hosted by the genuine external Online/DCM device or another absent participant.


## EXP152 — genuine Online topology reconstructed as coordinated multi-endpoint service

Observed genuine services:
- A5 FC03: 0000/18, 0023/1, 002E/10 with valid responses.
- A4: same three reads attempted at capture end after A5 disappears, with no captured response.
- 0x0F FC16: writes followed by normal ACK.
- 0x0F FC03: 0708/6 and 03E8/13 with data responses.
- 0x06 remains an FC17 accessory poll path.

The ordering repeatedly looks scheduler-driven rather than spontaneous.

Current strongest model:
the controller is probably the common master and only schedules A5/A4 + 0x0F read-side traffic when genuine external Online/DCM hardware has been recognized.

Two-wire capture alone cannot prove transmitter identity.

Critical remaining experiment:
cold boot with simultaneous 0x06 responder and 0x0F slave presence from the first relevant frames.


## EXP153 prepared — boot-latched combined-role test

Critical untested quadrant identified by EXP152:
cold boot with both 0x06 accessory presence and 0x0F ACK-side presence available from the first relevant frames.

EXP153 is passive until a real >=3 s bus-down and first returned valid frame are observed. No active master read is generated.

This isolates boot-time topology recognition from the already-negative runtime insertion tests.


## EXP153 — cold-boot combined-role presence still does not activate Online topology

EXP153 exercised both known external roles from the first relevant traffic after a real controller restart:
- exact 0x06 accessory responder;
- strict known 0x0F FC16 ACK service.

Within ~4.5 s after bus return the controller sent and received ACKs for:
`04BA/22`, `05FF/33`, `04A6/13`, `085F/5`, `0662/33`, `04A6/13`.

The experiment then ran for 300 s with:
- 283 valid 0x06 responses,
- 6 valid 0x0F FC16 ACKs,
- zero A5,
- zero A4,
- zero spontaneous 0x0F FC03,
- zero parser/drop delta.

Protocol implication:
Transport presence, even when established during controller boot, is not sufficient for genuine Online/DCM recognition. Further work should target identity/application semantics rather than timing variants.


## EXP154 — strongest semantic bridge found: IntegrationMode ↔ Link Integration

Firmware:
`0x4414 IntegrationMode`
- 0 = LIGHT/non-system
- 1/non-zero = SYSTEM
- GET-on-sync + SET-on-sync
- update triggers SystemIntegrationInit and full grouped sync.

Public Thermia Online DCM dump:
`registerIndex 1369 = 0x0559 Link Integration`
- 0 = LIGHT
- 1 = SYSTEM.

The Online `registerIndex` namespace is independently anchored to the local XTR by proven `0x0442 Activate Cooling` and strongly aligned `0x03E8..03EE` heating mappings.

Therefore:
`HE 0x4414 IntegrationMode -> local/Online 0x0559 Link Integration`
is now the strongest available serializer mapping candidate.

Status:
STRONGLY INDICATED, not locally proven. No native 0x0559 frame has yet been seen; EXP119 found no ordinary boot broadcast at 0559.

Next:
determine ownership/direction/block shape before any semantic write.


## DCM03 manual refinement — explicit approval and integration mode

Danfoss HP-kit documentation confirms:
- DCM03 integration can be switched between Danfoss Link and Danfoss Online;
- DHP-AQ connects DCM03 by RJ45 to the relay-board bus;
- Gateway variants expose diagnostic states including DCM-HP approval, approval failed, sending settings to DCM, and all OK.

Protocol implication:
There is a documented application-level approval/configuration state above electrical/transport presence.

This strongly supports the interpretation of EXP147–153 negatives.

`0x0559 Link Integration` remains a high-value semantic candidate, but its ownership is now explicitly open: controller-local, DCM-local, or mirrored state are all possible until a genuine mode-transition capture resolves direction.

Highest-value next capture:
genuine DCM03 Online -> Link -> Online transition with exact timestamps and full RS485 bytes.


## EXP155 prepared — genuine DCM03 integration-mode differential capture

RX-only capture of Online -> Link -> Online transitions.
The key discriminator is any repeatable transition-aligned 0x0F range/value delta, especially coverage of `0x0559 Link Integration`.


## EXP155 correction — no local DCM03 hardware

A genuine DCM03 mode-toggle capture would be high-value evidence, but it cannot be generated locally.

Therefore the project should not wait on or simulate that missing hardware blindly. Continue with offline serializer/ownership reconstruction first; only use a genuine DCM transition capture if obtained externally.

## Discussion #143 re-analysis — 0x0F mailbox model strengthened, Heat Curve claim corrected

The discussion explicitly describes 0x0F as a bidirectional mailbox/gateway role with two read areas and multiple FC16 write areas. This aligns with the genuine Online capture's recurring 0x0F FC03 reads plus cyclic FC16 writes.

Important correction from direct capture parsing:
- 12.116, block 0x0848/count23: `0x0858=0`, `0x085A=20`.
- 33.107, same block: `0x0858=21`, `0x085A=20`.
- Thus `0x0858` changes 0->21; `0x085A` does not change.
- 43.705 is block 0x07E4/count17 and cannot be treated as a simple reversal of 0x0858.

Therefore the discussion's AI-generated 20->21->20 mapping is not accepted as evidence.

Priority artifact targets: `0F_register_value_map.xlsx`, `modbus_slave.py`, `config.yaml` from fclauson's work.


## EXP155 artifact analysis — 0x0F mailbox direction materially strengthened

fclauson's forensic logger explicitly targets Unit 0x0F FC03 blocks and correlates responses to absolute addresses.

Spreadsheet read blocks:
- 1000..1012 / count 13; position 12 = register 1012, labelled 20/21 field.
- 1040..1060 / count 21; position 13 = register 1053, labelled 30/31/32/33 field.

Spreadsheet FC16 map includes:
- 1350..1369 / count 20;
- 1363 = 4;
- 1369 = 0.

With public Online semantics:
- 1363 = Operation Mode;
- 1369 = Link Integration.

Protocol implication:
0x0559 is carried in controller->0x0F FC16 state/snapshot traffic in this evidence set, not established as a DCM->controller activation command.

Strong mailbox model:
- FC16 to 0x0F = controller/state/snapshot direction;
- FC03 from 0x0F = desired-state/command mailbox direction.

Cross-platform caveat:
the 1000/count13 read block matches our genuine capture exactly; fclauson's second 1040/count21 block differs from our captured 0708/count6 block, so read-block #2 is not assumed invariant.

## EXP156 — local-display vs Online-command direction split

With a genuine Thermia Online/DCM connected, a local heat-pump display Heating Curve change produced:

- FC16 `0x03E8/count13` authoritative state: `03E8 23 -> 22`;
- no FC03 `0x03E8/count13` request anywhere in the ~79 s capture;
- FC03 on 0x0F continued only at `0x0708/count6`.

This is a strong directional discriminator:

```text
local/display change
    -> controller authoritative state changes
    -> FC16 write to 0x0F (03E8 snapshot)

remote Online desired-state candidate
    -> controller FC03 read from 0x0F (03E8/count13)
    -> controller later republishes accepted/current state via FC16
```

The second path remains a hypothesis until a timestamped remote Online A/B/A capture is obtained, but EXP156 materially strengthens it because local changes do not generate the FC03 03E8 command read.

Additional correction:
A4 appeared briefly while A5 later resumed normally, so A4 should be described as alternate/discovery/fallback-like probing rather than strictly a terminal fallback after A5 failure.

## EXP157 — boot sequencing separates A5 from 0x0F readiness

Two genuine boot captures materially refine the Online topology.

### HP power-up
- A5 may already be responsive while 0x0F is still unavailable.
- Before 0x0F readiness, the controller repeatedly retries FC16 `0870/count17` and FC03 `0708/count6` without ACK/response.
- The first successful 0x0F FC16 ACK is followed by a successful 0708 FC03 response and then a broad FC16 state/configuration sync beginning at `03E8`, `03FC`, `0410`, `042E` and continuing through the large native settings families.

Protocol implication:
`A5 responsive` != `0x0F mailbox ready`.
The Online/DCM stack appears staged: discovery/status service first, settings/command mailbox later.

### DCM power-up
A broad ACKed FC16 sync sweep is visible almost immediately and includes the same `042E..06F4` sequence. The `0546/count20` block contains `0553=4` and `0559=0`, reinforcing their controller->0x0F state-sync ownership.

New open boot/discovery frames:
- repeated valid `C8 FC03 2328/count2` during early DCM startup;
- one valid `A4 FC06 0032=0046` later;
- A4 FC03 discovery-style triplet followed by 0x05 FC17 can occur before 0x0F readiness.

Do not emulate C8/A4 FC06 yet: transmitter ownership and deterministic repeatability are unresolved.

## 2026-09-25 — EXP158 structural findings

### Paired address families
Genuine boot traffic strongly indicates two paired logical accessory/service slots:

- `0xA4 <-> 0x05`
- `0xA5 <-> 0x06`

Evidence:
- A4/A5 receive the same FC03 map probes (`0000/18`, `0023/1`, `002E/10`).
- In HP boot, an A4 probe triplet is followed immediately by a 0x05 FC17 transaction; normal Online runtime uses A5 plus 0x06 FC17.
- Both high/low pairs differ by exactly `0x9F` in slave address.
- A one-off `A4 FC06 0032=0046` writes a register that exists in the shared A4/A5 FC03 map; A5's contemporaneous value at register 0032 is also 0046.

Interpretation: A4 is no longer best described as a mere fallback for A5. The safest model is two sibling logical slots/services, with exact physical ownership still OPEN.

### Deterministic initial-sync image
Across independent DCM-only and HP boot captures, 27 of 28 overlapping `0x0F FC16` blocks in `0x042E..0x06F1` are byte-identical. The only differing block is the RTC block `0x06EA/count7`.

This strongly indicates that the broad `03E8..06xx` upload is a deterministic controller configuration/state image rather than transient boot noise.

### RTC mapping PROVEN by cross-capture time progression
`0x06EA..0x06F0` contains:
- 06EA seconds
- 06EB minutes
- 06EC hour
- 06ED day
- 06EE month
- 06EF two-digit year
- 06F0 weekday (Monday=0 fits observed Friday=4)

Runtime block `0x0848/count23` mirrors the same fields at `0x0858..0x085E`.
In one DCM capture, `06EA` reports 08:06:22 at t=27.583 and `0858..085E` reports 08:06:41 at t=46.543, exactly matching the 18.96 s elapsed capture time.

### 0x085F status block
`0x085F/count5` can interleave periodically with the HP initial-sync upload at roughly the 0x06/0708 scheduler cadence. Treat it as an independent status/handshake block, not a sequential configuration fragment.

### 0x0708 command/status block
`0x0F FC03 0x0708/count6` is not constant. Distinct boot/session-phase responses have now been observed, including:
- `[0,0,32767,65535,128,7]` immediately after HP mailbox readiness;
- `[0,0,0,0,1919,6]` after HP initial sync;
- `[0,0,0,0,128,6]` early after DCM reconnect;
- `[0,0,0,0,0,6]` later in the same DCM reconnect capture.

Exact word semantics remain OPEN, but this block clearly carries synchronization/session state.

## 2026-09-25 — EXP159 no-DCM cold-boot differential

### C8 reclassified: generic native boot discovery
A clean no-DCM cold boot with wildcard passive parsing shows the exact same request seen in genuine DCM boot:

`C8 FC03 0x2328/count2`

In the no-DCM run it occurs 20 times from +0.565 s through +20.775 s with no response. Therefore C8 probing is native controller discovery and is not evidence of DCM presence.

The genuine DCM boot showed only nine early C8 probes before the Online/DCM session progressed. Working hypothesis: successful higher-layer discovery/readiness shortens or terminates the generic C8 retry phase. This causal relation is not yet proven.

### Native no-DCM 0x0F startup retries
Without a DCM, the controller still emits 0x0F FC16 requests during cold boot:
- `04BA/count22` twice at the start;
- repeated `04A6/count13` thereafter;
- recurring `085F/count5` interleaved with 04A6.

No ACKs were observed. Therefore unACKed FC16 writes to 0x0F are native controller startup/retry behaviour and do not imply an Online module is present.

### Stronger DCM-dependent discriminators
In the available no-DCM boot interval there is no A4, A5, 0x05, FC06 or 0x0F FC03 traffic. Genuine Online boots do contain A5 and, at later stages, A4/05 plus responsive 0x0F FC03/FC16 traffic.

Current working discriminator hierarchy:
1. C8 request presence — generic boot discovery; NOT DCM-specific.
2. 0x06 polling / unACKed 0x0F FC16 retries — native transport/startup; NOT sufficient.
3. A5 service responses, A4/05 sibling-slot activity and responsive 0x0F mailbox — stronger DCM/session candidates.
4. Full ACKed `03E8..06xx` initial sync — established mailbox-ready state.

## Part 9 continuation boundary

EXP159 establishes that `C8 FC03 2328/count2` is generic native cold-boot discovery and must not be used as a DCM-presence criterion.

Current discriminator hierarchy:
1. C8 request presence — generic boot discovery.
2. 0x06 polling and unACKed 0x0F FC16 retries — native startup/transport behaviour.
3. A5 service responses and A4/05 sibling activity — stronger DCM/session candidates.
4. Responsive 0x0F FC03/FC16 mailbox — established mailbox service.
5. Full ACKed `03E8..06xx` upload — established initial-sync state.

Next proposed protocol test is EXP160: exact-genuine A5 responder only, with all other candidate roles left passive.

## EXP160–EXP162 refinement: A5 activation and 0x0F ACK are separate gates

- EXP160: exact genuine A5 slave responses were armed but never invoked because the no-DCM controller emitted no A5 requests during the 180 s run.
- EXP161 cross-capture ordering: genuine DCM operation can have working 0x0F FC16 ACK service before the first visible A5 request, while C8 probing continues in parallel. Therefore C8 completion is not a necessary A5 gate. A4 is not a simple A5 precursor.
- EXP162: the local ESP successfully ACKed six whitelisted controller->0x0F FC16 writes, but this still produced no A5, A4/05 or `0x0F FC03` activity.

**Strong conclusion:** visible 0x0F FC16 mailbox acknowledgement and A5 activation are distinct parts of a broader DCM service state. Correct ACK of the known startup writes is not sufficient to make the controller schedule A5 or `0x0F FC03`.

**Current architecture hypothesis:** genuine DCM presence establishes an earlier binding/service state that enables A5 scheduling and the bidirectional 0x0F runtime mailbox. C8 discovery runs in parallel and must not be treated as the missing gate merely because it is present.

**Negative findings retained:** do not repeat A5-responder-only, 0x0F-ACK-only, or combined 0x0F-ACK + waiting-A5-responder as sufficient activation hypotheses. Do not invent a C8 response without new evidence.

**Next bounded test — EXP163:** retain the known 0x0F FC16 ACK role but remove the A5 slave responder; after the ACK phase send one exact, read-only A5 FC03 triplet (`0000/18`, `0023/1`, `002E/10`) to test the alternative direction/ownership model. No A5 writes and no broad scan.


---

## Findings added by EXP163

### A5 post-ACK active-read test
After six successful known-shape `0x0F FC16` ACKs during a valid no-DCM cold boot, the exact genuine A5 FC03 triplet (`0000/18`, `0023/1`, `002E/10`) was transmitted once. All three requests were read-only and byte-identical in shape to genuine traffic. No A5 response was observed and no autonomous A5/A4/0x05 or `0x0F FC03` traffic appeared during the complete 180 s window.

**Protocol implication:** A5 is not exposed merely by advancing the visible no-DCM `0x0F FC16` ACK state and then polling the genuine A5 registers. This strengthens, but does not prove, the model that A5 is supplied by the genuine DCM/service topology rather than being a dormant controller slave.

### 0x06 separation strengthened
`0x06 FC17` remained active throughout EXP163 despite `A5=0`, `A5rsp=0`, `A4=0`, `s05=0`, and `0F03req=0`. Therefore:
- `0x06 active` != `A5 active`;
- `0x06 active` != established Online/DCM session;
- the established no-DCM `AFDC=0x0010` state can coexist with complete absence of the higher Online/DCM service topology.

Current classification: **0x06 is a native accessory/service endpoint associated with the broader Online/DCM topology, but its transport activity is independently present without a DCM. Exact physical ownership and binding semantics remain unresolved.**

### Injection side effect
Five parser resyncs occurred around the third A5 master injection, with no RX buffer drops and no subsequent growth. Treat this as a timing/echo/collision warning for future active master injection. Prefer passive differential work until a new specific prerequisite is identified.

## EXP164 + genuine DCM runtime activation refinement

EXP164 confirms that no-DCM cold boot can reach C8 discovery, 0x06 polling, A80E=0x28, AFDC=0x0010 and sustained 0x0F FC16 attempts while A5, A4/0x05 and 0x0F FC03 remain absent. These signals are therefore insufficient DCM-presence/binding markers.

The genuine `090209` capture is a DCM power-up with the controller already running. 0x0F is ACK-capable by ~0.389 s and A5 is operational by ~1.179 s. DCM service activation is therefore demonstrably possible at runtime; a controller reboot is not intrinsically required.

UI terminology correction: `EXP 0.0` / `UITBR.KAART` is the expansion-board/version UI path already mapped in EXP129-132. A valid 0x06 responder exposes this entry and AFD1 is rendered as version/10. Appearance/change of this UI item proves 0x06 accessory metadata reception, not DCM/Online recognition.

Next discriminator: runtime hot-plug emulation should be compared with genuine 090209, while avoiding further controller reboots.

## 2026-09-25 — EXP165 runtime result and FC17 request-length correction

EXP165 adds a clean runtime-only negative for the 0x0F ACK role:
- five known 0x0F FC16 requests were successfully ACKed during a 180 s run;
- no A5, A4/0x05 or 0x0F FC03 followed;
- therefore 0x0F FC16 ACK service alone is not sufficient to activate the DCM/Online service state, including when introduced without rebooting the controller.

EXP165 does not test simultaneous 0x06 + 0x0F presence. Although 43 slave-0x06 frames were observed, `06tx=0` because the responder incorrectly required a 27-byte FC17 request. The native request shape `06 17 AFC8 000C AFDC 0005 0A + 10 data bytes + CRC` is 23 bytes total.

This is an implementation correction, not a new protocol hypothesis. EXP166 changes only this exact request-length gate from 27 to 23 so the already-proven REQ-low 0x06 response path can actually be exercised alongside the existing 0x0F ACK role.

The VERSION-page observation remains interpreted narrowly: a valid 0x06 responder can expose `EXP` / `UITBR.KAART`, with AFD1 rendered as version/10. Appearance of `EXP 0.0` therefore confirms the 0x06 accessory/metadata path is being served; it does not by itself prove DCM/Online application activation.

## 2026-09-25 — EXP166 refinement: 0x06 metadata presence is runtime-independent from DCM service activation

EXP166 corrects the EXP165 FC17-length gate and proves the known 0x06 responder works during normal controller runtime without a heat-pump reboot.

Observed:
- 169 valid 0x06 transactions in 180 s and 169 ESP responses.
- `AFD1=0` response causes the Thermia VERSION UI to expose `EXP 0.0` almost immediately.
- zero A5, A4/05, 0x0F FC03, or any 0x0F traffic during the same armed window.
- clean parser/buffer health.

Protocol conclusion:
**0x06 FC17 accessory/version service is independently activatable at runtime and directly controls the visible EXP version metadata, but it does not itself establish the DCM/Online service session.**

Refined layered model:
1. `0x06` accessory/version metadata path — can be made visible independently (`EXP 0.0`).
2. A5 discovery/status service — separate activation prerequisite remains unknown.
3. `0x0F` mailbox/settings service — separate readiness stage; genuine captures show it can be operational before/around first visible A5 depending on power-up scenario.

EXP165 + EXP166 complement each other: runtime 0x0F ACK alone and runtime 0x06 presence alone each fail to activate A5/0x0F-FC03. A single run with both roles actually exercised has not yet occurred.

Do not treat `EXP 0.0`, AFDC=0x10, A80E=0x28, or unanswered C8 discovery as sufficient DCM-presence/binding discriminators.

Next research priority: offline differential of the genuine DCM hot-plug interval immediately preceding the first 0x0F ACK and first A5 request. Do not reproduce the unresolved `A4 FC06 0032=0046` until transmitter ownership, repeatability and effect are established.


---

## EXP167 protocol update — sustained 0x06 presence does not create 0x0F/A5 service

EXP167 held the already-proven runtime `0x06` accessory/version responder active for 600.009 s. The controller accepted 559 responses, yet emitted no `0x0F` frames at all and no A5/A4/0x05 traffic. Bus health remained clean.

Observed terminal counters:

```text
s06=559
06tx=559
s0F=0
0F16req=0
0FtxACK=0
0F03req=0
0F03rsp=0
A5=0
A4=0
s05=0
resyncDelta=0
dropDelta=0
```

### Protocol implications

1. **0x06 metadata/presence and native 0x0F service activation are independent.** A correct 0x06 response can expose `EXP 0.0` and sustain fast accessory polling without causing any 0x0F traffic.
2. **0x06 presence and A5 activation are independent.** Ten minutes and 559 valid responses are insufficient to make the controller schedule A5.
3. **The exact combined `0x06 + exercised 0x0F ACK` hypothesis remains technically untested**, because no controller-originated FC16 occurred during EXP167.
4. **Waiting longer for 0x06 to trigger 0x0F is no longer a high-value path.** EXP166 and EXP167 provide increasingly strong negative evidence against that causal model.
5. Genuine DCM power-up has a qualitatively different early service state: `0x0F` is ACK-capable almost immediately and A5 follows shortly thereafter while C8 is still probing. This points to a missing discovery/binding/service-availability or physical ownership layer rather than a simple accessory-version response.

### Refined architecture

```text
0x06 accessory/version metadata path
    -> independently serviceable
    -> controls EXP / UITBR.KAART metadata
    -> NOT sufficient for DCM service state

0x0F mailbox/service
    -> generic controller FC16 attempts can exist without DCM
    -> genuine DCM topology supplies an operational ACK/read service
    -> physical owner still OPEN

A5 service
    -> observed operational only in genuine DCM topology
    -> activation/ownership still OPEN

C8 discovery
    -> generic startup probing
    -> not the missing DCM gate
```

### Research consequence
Do not spend additional experiments on longer `0x06` dwell, `EXP 0.0`, A80E/AFDC, or guessed C8 replies as DCM-recognition triggers. The next useful work is offline ownership/timing analysis of the earliest genuine DCM service transition, especially what makes `0x0F` electrically/logically available before the first A5 transaction.


## EXP168 key finding — combined 0x06 presence + 0x0F ACK is insufficient

EXP168 deliberately exercised the exact runtime combination that EXP167 could not reach naturally:

1. establish proven `0x06` accessory/version presence;
2. manually change Heat Curve +1 on the Thermia;
3. observe the exact controller-originated `0x0F FC16 0x03E8/count14`;
4. ACK that request once;
5. observe 120 s.

Observed:
- 155 valid `0x06` responses;
- 1 exact `0x0F FC16 03E8/count14` request;
- 1 exact ACK;
- first FC16 payload word = `36 / 0x0024`, matching Heat Curve 36;
- no A5;
- no A4;
- no `0x05`;
- no `0x0F FC03`;
- `resyncDelta=0`, `dropDelta=0`.

### Protocol implication

The combined transport-role hypothesis is now negative: a syntactically and behaviorally valid `0x06` responder plus a working ACK-side `0x0F` role does **not** reproduce the genuine DCM/Online service state.

This materially strengthens the architectural model that the real DCM topology contains an additional discovery/binding/service-availability/ownership layer not represented by simple Modbus request/response participation.

The next protocol question is no longer "which known transport role should be combined?" but rather "what actor or ownership property exists in the genuine DCM topology before the first successful `0x0F` transaction and first A5 service cycle?"


## EXP170 protocol refinement — native 0x0F progression is stateful

EXP170 attempted to trigger a known Heat Curve event and then advance only `03E8/14 -> 0410/22 -> 042E/15`.

Observed:
- before the Heat Curve event, the controller was already repeatedly transmitting `0x0F FC16 0x04A6/count13`;
- Heat Curve +1 still generated the expected `0x03E8/count14` with first word `37`;
- ACKing `03E8/14` did not cause `0410/22`;
- the controller kept retrying `04A6/13`;
- bus remained clean (`resyncDelta=0`, `dropDelta=0`).

Protocol implication:
The 0x0F block stream is not a stateless sequence that can always be restarted by a new `03E8` event. An already-pending block can retain scheduler ownership across unrelated parameter-change events. Therefore staged ACK experiments must account for current pending 0x0F state.

This also weakens the idea that `03E8` is a universal session-start marker. It is a valid controller-originated block/event, but not necessarily a reset/start command for the broader 0x0F synchronization state machine.


## EXP172 — controller FC17 fingerprint discriminator

A passive 180 s local capture produced a stable `0x02 FC17` controller request:

`read A7F8 / count 15`
`write A80C / count 7`
`A80C..A812 = 0040,0000,0000,000A,000A,FFFF,0000`

The scheduler-enabled, DCM-silent interval in genuine capture `090550` instead uses:

`read A7F8 / count 13`
`write A80C / count 7`
`A80C..A812 = 0040,0000,0000,000A,000A,000C,0500`

During that genuine state A5 and `0x0F FC03 0708/count6` scheduling are already active before any DCM response.

### Interpretation

`A811/A812` and the A7F8 read-span are now strong **controller-state fingerprints** associated with the scheduler-enabled versus local scheduler-disabled states.

Do **not** infer causality yet:
- `A811=000C` and `A812=0500` may be causes, consequences, model identifiers, firmware-layout markers, or accessory/configuration state;
- read count 13 versus 15 may indicate controller generation/configuration rather than scheduler state.

### Safety rule

No direct write to `A811` or `A812` until their semantics, ownership, and possible effects are established. Prefer passive correlation with natural/UI-driven state changes first.


## EXP173 finding — 0x06 presence does not change A811/A812 or scheduler state

A/B/A test result:
- local baseline: `A7F8 read-count=15`, `A811=FFFF`, `A812=0000`;
- active exact known `0x06` REQ-low responder: 56 responses, same controller values;
- passive recovery: same controller values;
- no A5, A4, `0x05`, or `0x0F FC03` scheduler traffic emerged.

Protocol conclusion:
The `FFFF/0000` vs `000C/0500` controller-state discriminator is not a simple consequence of live `0x06` accessory presence. Likewise, accessory presence alone does not enable the extended scheduler. Research priority moves to identifying persistent controller-side configuration/firmware/commissioning semantics behind A811/A812 and the A7F8 layout difference.


## EXP175 — local XTR M topology differs from scheduler-enabled reference

A 180 s passive census established:
- local slave 0x04: absent;
- local slave 0x1E: strongly active (670 frames);
- local A5/A4/0x05/C8: absent;
- local 0x0F FC03: absent;
- local 0x0F FC16: active (168 requests);
- local controller fingerprint: A7F8 read-count 15, A811=FFFF, A812=0000.

Local 0x1E repeatedly carries:
- FC16 start 0x0000/count9;
- FC16 start 0x0014/count3;
- FC04 read start 0x0000/count22;
- FC04 read start 0x001E/count6.

Scheduler-enabled reference captures instead show slave 0x04 continuously, A5 activity and 0x0F FC03 polling together with controller fingerprint `A811/A812=000C/0500` and A7F8 read-count 13.

Protocol conclusion:
The local XTR M and scheduler-enabled reference are demonstrably different observed bus topologies. The earlier A811/A812 correlation must therefore be treated as potentially platform/topology-associated metadata, not as a proven scheduler-enable control.

Safety implication:
Do not write A811/A812 based on the external reference values. First establish whether reference slave 0x04 is functionally equivalent to local slave 0x1E or belongs to a different board/firmware architecture.


## EXP176 — 0x0559 scheduler hypothesis falsified in external captures

The full-state sync block immediately before `0x055A` is `0x0546/count20`, which covers addresses `0x0546..0x0559` inclusive. The final word (`0x0559`) is `0x0000` in both scheduler-enabled reference captures.

Protocol implication:
- the documented/public semantic `0x0559 Link Integration` must not be assumed to be the scheduler-enable switch for this platform/state;
- scheduler activity (A5 and 0x0F FC03) can coexist with `0x0559=0`;
- a speculative write of `0x0559=1` is not justified by the current evidence.

## 2026-09-26 — EXP218–EXP221 local system-page and cold-boot findings

### 0x0553 Operation Mode
Local XTR controlled A/B/A validation proves:
- `0x0553 = 1` in AUTO;
- `0x0553 = 2` in COMPRESSOR;
- restoring AUTO restores `0x0553 = 1`.

### Stable 0546-page structural candidates
The local full `0546/count20` page is stable across repeated frames and across `AUTO -> COMPRESSOR -> AUTO` except for `0x0553`.
Current local values:
- `0x0546 = 1`
- `0x0547 = 1`
- `0x054A = 2`
- `0x054F = 3`
- `0x0553 = 1/2` according to Operation Mode
- `0x0559 = 0`

Compared with the genuine reference system page, `0546`, `0547`, `054A`, and `054F` remain stable cross-system discriminator candidates independent of Operation Mode. Their semantics are unknown.

### Cold-boot architecture
EXP221 shows that a local no-DCM cold boot does not spontaneously create the genuine Online/DCM scheduler:
- no A5;
- no A4;
- no slave 0x04/0x05 service burst;
- no slave `0x0F FC03`;
- no `0708/count6`.

At the same time, native local `0x0F` traffic resumes shortly after boot (`04BA`, `04A6`, `085F`, FC17 `0730`). Therefore the controller's native 0x0F serializer/runtime capability is distinct from the extended Online/DCM scheduler.

### Correction: 085F is not a scheduler marker by itself
A lone/repeated `0x0F FC16 085F/count5` occurs locally without A5 or FC03/0708. Do not classify `085F` alone as a topology/scheduler hit.
For runtime-exporter detection, prefer the genuine cyclic chain start `07D0/count19` and/or the accompanying `0x0F FC03 0708/count6` scheduler.


## 2026-09-26 — genuine DCM startup re-analysis and EXP222 rationale

In `thermia_capture_20260925_090209.log`, the genuine DCM ACKs a long controller-originated FC16 initialization/full-sync sequence. Observed initialization shapes include:
`042E/15`, `0442/13`, `0456/12`, `046A/18`, `047E/19`, `0492/9`, `04A6/13`, `04BA/22`, `04D8/27`, `04F6/14`, `050A/19`, `051E/9`, `0532/18`, `0546/20`, `055A/33`, `057B/33`, `059C/33`, `05BD/33`, `05DE/33`, `05FF/33`, `0620/33`, `0641/33`, `0662/33`, `0683/33`, `06A4/33`, `06C5/33`, `06EA/7`, `06F1/3`, `06F4/19`, and `085F/5`.

Locally proven leading ACK-gated stages `03E8/14` and `0410/22` are included in the EXP222 allow-list as well.

After the genuine initialization tail (`06F4`, then `085F`), the first observed controller request `0x0F FC03 0708/count6` occurs a few seconds later; the genuine cyclic runtime exporter then starts at `07D0/count19`.

A separate genuine capture shows `0708` already active before a temporary A4/0x05 burst. Therefore that A4/0x05 burst cannot be the primary scheduler-start trigger.

Current strongest causal hypothesis:
successful completion of the controller->DCM FC16 initialization/full-sync may set the internal synchronized/service-ready state that enables the FC03/0708 scheduler. EXP222 directly tests this with exact standard FC16 echo ACKs only and fails closed on any unrecognized shape.



---
## 2026-09-26 — EXP222 protocol finding: 0x0F ACK completion is not the Online scheduler trigger

Controlled XTR cold-boot with a minimal local slave-0x0F ACK responder produced six valid FC16 echo-ACKs (`04BA/22`, `05FF/33`, `04A6/13`, `085F/5`, `0662/33`, `04A6/13`) but never produced A5/A4/0x04/0x05 service traffic, `0x0F FC03`, `0708/count6`, or `07D0` runtime-export start.

Therefore, on the tested XTR:
- native controller->0x0F FC16 serialization exists independently of extended Online topology;
- ACKing the locally offered FC16 sequence is insufficient to create the read-side scheduler;
- `0x0F FC17 0730/count8` is native local traffic and must not be used as proof that Online topology is active;
- the genuine DCM observation that A5 can be active before the DCM's `0x0F` endpoint becomes available strongly implies that service-topology activation precedes or is independent of 0x0F full-sync completion.

Primary remaining trigger candidates: persistent service/accessory binding, commissioning/configuration state, firmware/model capability, or an earlier service-discovery/authorization event.


---
## 2026-09-26 — EXP223 protocol finding: XTR-native 0x0F FC17 071C/0730 exchange

A recurring local XTR transaction has now been promoted to a first-class protocol candidate:

`slave 0x0F, FC17: read 0x0730/count8; write 0x071C/count8; bytecount 16`.

Evidence:
- 47 exact requests in EXP221 and 25 in EXP222 (72 total analysed).
- No local response because no DCM/Online endpoint is installed.
- All 72 write images satisfy:
  - 071C=`0x1A16` constant;
  - 071E=`0xF906` constant;
  - 0720=`0xDC1A` constant;
  - 0722=`0x001E` constant;
  - 0723=`(2*071D + 0x0500) mod 65536`;
  - low byte(071F)=`0xAC`;
  - high byte(071F)=`floor(low_byte(071D)/4)`.
- 0721 changes on a much slower, roughly minute-scale cadence.
- The three available genuine ATEC/DCM captures contain no slave-0x0F FC17 frames at all; they use the separate ATEC 0x04+A5+0x0F FC03/FC16 topology.
- EXP175 already established the complementary topology difference: local XTR has active 0x1E and no 0x04/A5, while the ATEC reference captures have 0x04/A5 and no 0x1E.

Interpretation:
- Do not assume ATEC's `A5 + 0708 FC03` scheduler is the only possible Online/DCM transport on XTR-family controllers.
- `071C/0730` is a strong XTR-specific keepalive/session/mailbox candidate.
- The deterministic 16-byte write image resembles a timed/counter/challenge structure more than a set of independent scalar settings.
- This is a transport-structure conclusion only. The eight response registers `0730..0737` remain semantically unknown.

Safety consequence:
Do not answer the FC17 request with guessed zeros or echoes. First perform passive controlled correlation (EXP224), then require genuine-response evidence or a proven transformation before any responder experiment.


---
## 2026-09-26 — EXP224 protocol finding: 071C/0730 FC17 is cold-boot/recovery gated, not steady-runtime

EXP224 successfully exercised a passive Heat Curve A/B/A with native `03E8/count14` ground truth, but observed **zero** exact `0x0F FC17 read 0730/count8 + write 071C/count8` frames across the entire experiment. The parser remained clean and the Heat Curve state was clearly observed, so the target absence is real for that runtime window.

This refines EXP223: do not describe 071C/0730 as an always-on recurring XTR transaction. The exact family is proven recurring specifically in the controller cold-boot context from EXP221, where it started at ~2.9 s post-power-on and continued at roughly 4.2 s cadence through ~199.7 s post-on.

Current interpretation:
- 071C/0730 is strongly associated with controller boot/recovery/service-session state;
- its absence in ordinary runtime increases the plausibility that it is a startup/session/challenge exchange toward an external slave-0x0F service;
- no semantic meaning can yet be assigned to the eight write words;
- the eight requested return registers `0730..0737` remain unknown and must not be guessed or emulated.

EXP225 is the bounded next passive test: re-establish the cold-boot FC17 stream first, then correlate a single Heat Curve A/B/A while that stream is active.

---
## 2026-09-26 — EXP225 protocol finding: cold-boot stream reproduced; write image remains counter-like

EXP225 again reproduced the exact local XTR transaction:

`slave 0x0F FC17: read 0x0730/count8; write 0x071C/count8`

after a genuine controller power cycle. This independently confirms that the FC17 family is available in the cold-boot/recovery window and not only in EXP221.

32 exact frames were captured. Every one preserved the previously discovered deterministic relations:
- `0723 = (2 * 071D + 0x0500) mod 65536`;
- low byte of `071F = 0xAC`;
- high byte of `071F = floor(low_byte(071D) / 4)`.

Across the run:
- `071C=0x1A17` stayed constant;
- `071E=0xF906` stayed constant;
- `0720=0xDC1A` stayed constant;
- `0722=0x001E` stayed constant;
- `071D`, `071F`, `0721`, and `0723` followed a deterministic progression/wrap pattern.

Native `03E8` ground truth did show Heat Curve `36 -> 37 -> 36` while FC17 traffic was active. No obvious discrete reversible Heat-Curve signature appears in the FC17 write image; however the experiment's manual phase markers were invalidated by a late Power ON marker, so this cannot be promoted to a formal negative correlation result.

Protocol refinement:
- cold-boot/recovery gating is now reproduced in more than one experiment;
- the 071C write image is increasingly consistent with timing/session/challenge data rather than a direct copy of heating settings;
- this does **not** identify the return-side `0730..0737` semantics;
- do not answer the FC17 request with guessed zeros, echoes, or synthesized values.

Next useful test should remain passive and fix phase control automatically before repeating the single-variable Heat Curve correlation.

---
## 2026-09-27 — EXP226 protocol finding: 071C..0723 decodes as controller RTC/calendar data

Offline analysis of 129 exact local XTR requests (`0x0F FC17 read 0730/count8 + write 071C/count8`) now identifies the changing write image much more specifically than the earlier "counter/session-like" description.

### Proven/strongly validated field structure

For words `071C..0723`:

- `071C = (year_since_2000 << 8) | hour`
- `071D = 0x4500 | (2 * second)`
- `071E = 0xF906` in all 129 analysed frames; semantic meaning unknown
- `071F = (floor(second/2) << 8) | 0xAC`
- `0720 = 0xDC00 | day_of_month`
- `0721 = 0xC500 | (4 * minute)`
- `0722 = 0x001E` in all 129 analysed frames; semantic meaning unknown
- `0723 = 0x8F00 | (4 * second)`

The mapping is supported by two independent capture dates:
- 2026-09-22, hour 14: `071C=1A0E`, `0720=DC16`;
- 2026-09-26, hour 22/23: `071C=1A16/1A17`, `0720=DC1A`.

The decoded controller time leads the ESP/log clock by approximately 201 s on Sep22 and 206 s on Sep26, with sub-second-scale within-run scatter. This is strong independent validation that these are real RTC-derived fields.

### Earlier algebraic relations explained

The EXP223 relations are not arbitrary challenge math:
- `0723 = (2*071D + 0500) mod 65536` follows directly from the redundant second encodings;
- `low(071F)=AC`;
- `high(071F)=floor(low(071D)/4)` follows because `low(071D)=2*second`.

### Protocol consequence

The `071C..0723` controller-write image should no longer be described primarily as an unknown session counter. It is predominantly a transformed date/time payload. It is also not evidence of direct heating-setting content.

Do not infer the complementary read bank from this. `0730..0737` is still unknown and may contain acknowledgement, validation, command, transformed time data, or something else.

### Remaining calendar candidates

`0722=001E` equals decimal 30, matching the number of days in September, and `071E=F906` may contain other calendar metadata. These are hypotheses only: all available raw validation captures are from September, so month-dependent behaviour is not yet observable.

A future ordinary-runtime capture in another month can validate these fields without restarting the heat pump.




---
## 2026-09-27 — EXP227 protocol finding: shared 0x0F serializer, different extended service topology

EXP227 performs an offline architecture-level comparison of local XTR evidence with four genuine ATEC/DCM captures.

### Shared native `0x0F` page family

Locally proven XTR ACK-walk:
`03E8/14 -> 0410/22 -> 042E/15 -> 04A6/13 -> 04BA/22 -> 05FF/33 -> 0662/33`

Every start address appears in the genuine ATEC/DCM full-sync sequence in the same relative order:
- `03E8/13` vs XTR `03E8/14`;
- `0410/21` vs XTR `0410/22`;
- exact matches at `042E/15`, `04A6/13`, `04BA/22`, `05FF/33`, `0662/33`.

Additional exact recurrent shared pages:
- `0546/20`;
- `085F/5`.

This materially refines the earlier topology interpretation: the platforms do not use wholly separate native application protocols. They share a substantial slave-`0x0F` page/register architecture.

### Payload homology

One-frame fieldwise comparisons on exact shared shapes:
- `04BA/22`: 20/22 words equal;
- `05FF/33`: 31/33 equal;
- `0662/33`: 31/33 equal;
- `085F/5`: 5/5 equal;
- `0546/20`: 15/20 equal in the compared states.

`04A6/13` is structurally shared but the compared payloads differ strongly, so shared layout must not be confused with equal runtime/config values.

Interpretation:
shared start/count and repeated word-position agreement strongly support homologous register-page schemas with model/state-specific content.

### Sparse XTR sync versus broad ATEC/DCM sync

The genuine DCM full-sync sequence includes many intermediate pages not seen in the locally proven XTR ACK-walk. Therefore the most useful current model is:
- common serializer/register address space;
- model/firmware/capability-dependent page selection and some page-length variation;
- additional extended scheduler only on the reference topology/state.

The XTR `03E8` and `0410` pages are each one word longer than their ATEC counterparts. Exact reason is unknown.

### Extended Online/DCM runtime scheduler remains a separate subsystem

Genuine reference signature:
- A5 service traffic;
- controller `0x0F FC03 0708/count6`;
- cyclic controller `0x0F FC16` runtime family `07D0..0884`;
- special 0708 join response can trigger broad `03E8..06xx` resynchronization.

Local XTR signature:
- native lower `0x0F` sync/event pages exist;
- `085F/5` exists;
- no confirmed A5;
- no confirmed `0708/count6`;
- no confirmed cyclic `07D0..0884` family.

Thus the missing local problem is the **extended controller-side service scheduler/binding state**, not lack of the core `0x0F` register serializer.

### DCM rejoin ordering confirms scheduler-before-endpoint

In genuine rejoin capture `090550`:
- A5 active from ~0.526 s;
- `0708` polling starts ~0.987 s;
- `0x0F` FC16 ACK availability begins only at 66.860 s;
- first `0708` DCM response arrives at 68.235 s;
- 16 prior `0708` polls are unanswered.

Therefore the controller schedules the extended service subsystem while the DCM `0x0F` endpoint is still unavailable. Successful ordinary FC16 page ACK completion cannot by itself explain scheduler activation.

### `0x06` separation strengthened

Across four genuine DCM captures:
- 69 exact controller `0x06 FC17 AFC8/12 -> AFDC/5` polls;
- zero slave-0x06 responses;
- Online/DCM traffic is simultaneously functional on A5/`0x0F`.

Protocol implication:
`0x06` is a parallel expansion/accessory interface in these systems, not the observed Online/DCM data endpoint.

### 0x04 versus 0x1E

Reference 0x04:
- recurrent FC17 `ABE0/count12` with write `ABF4/count4`.

Local XTR 0x1E:
- FC16 `0000/count9`;
- FC16 `0014/count3`;
- FC04 `0000/count22`;
- FC04 `001E/count6`.

They are not wire-level renumberings. Any higher-level functional analogy remains open.

### RTC FC17 correction

EXP226 decoded local `071C..0723` as transformed controller calendar/clock data. Therefore local XTR `071C/0730 FC17` must not be treated as the direct equivalent of ATEC `0708/count6` simply because both use `0x07xx` addresses.

The `0730..0737` return semantics remain unknown.

### Research consequence

Highest-value next work is offline field-level homology:
compare persistent values and differences in shared pages to identify model/platform/service-capability discriminators.

Do not respond to `0708` locally without a controller-originated `0708` request.
Do not synthesize `0730..0737`.
Do not write A811/A812 based on the reference fingerprint.
Do not return to broad 0x06 payload guessing.


---
## 2026-09-27 — EXP228 protocol finding: persistent cross-platform discriminator set

EXP228 performs a field-level offline comparison inside the homologous `0x0F` pages established by EXP227.

### Persistent candidate differences

Best current cross-system discriminator candidates:
- `04BA`: XTR `0014`, ATEC `0013`;
- `04C0`: XTR `0028`, ATEC `001E`;
- `0546`: XTR `0001`, ATEC `0002`;
- `0547`: XTR `0001`, ATEC `0000`;
- `054A`: XTR `0002`, ATEC `0000`;
- `054F`: XTR `0003`, ATEC `0000`;
- `061C`: XTR `0003`, ATEC `0000`;
- `061E`: XTR `0001`, ATEC `0000`;
- `067E`: XTR `0003`, ATEC `0000`;
- `067F`: XTR `0001`, ATEC `0000`.

Replication is strong for the exact compared page images: local `04BA` repeats identically across EXP221/222; local `0546` is stable across many frames and prior Operation-Mode tests; EXP141 supplies 30 identical `05FF` and 267 identical `0662` images, matching the EXP222 payloads; genuine `090209` and `090550` provide identical reference images at the corresponding pages.

### Important exclusions

- `0553` is excluded as a structural/capability discriminator because local controlled testing proves it is Operation Mode.
- `04A6/count13` is excluded as a fixed fingerprint because the XTR payload varies across local runs.
- `085F/count5` is a negative discriminator: all five words are zero on both platforms in the compared corpus.

### Structural schema differences

Retain, but do not overinterpret:
- XTR `03E8/count14` versus ATEC `/13`;
- XTR `0410/count22` versus ATEC `/21`.

These indicate a model/schema difference but do not identify an Online enable bit.

### 33-word family clue

The XTR uses `05FF/33` and then `0662/33`, whereas genuine ATEC full-sync also serializes intermediate `0620/33` and `0641/33` pages. XTR-specific non-zero tail fields `061C/061E` and `067E/067F` are therefore interesting in the context of repeated-table/page-selection structure. This is only a structural correlation.

### Protocol consequence

The search for a scheduler-enable mechanism should now be constrained to:
1. stable model/config/capability candidates rather than arbitrary differing words;
2. table/page-selection structure in the `055A..06C5` family;
3. controller-side binding/commissioning state that may not be directly represented by any one shared register.

Do not copy ATEC values into the XTR. No candidate is proven causal or safe to write.

Preferred next step: EXP229 offline analysis of the `055A..06C5` 33-word family and skipped-page structure.

---
## 2026-09-27 — EXP229 protocol finding: structured 396-word descriptor family with transition-record discriminators

The genuine ATEC/DCM full-sync contains twelve consecutive `0x0F FC16 count33` pages from `055A` through `06C5`, each separated by exactly 33 words. Together they cover the contiguous register range `055A..06E5` (396 words).

The complete 396-word image is identical in reference captures `090209` and `090550`.

### Internal structure

The concatenated image has strong lag-12 periodicity:
- 315 of 384 comparable positions (82.0%) equal the value 12 words earlier/later;
- 396 = 33 * 12;
- exact 12-word template runs occur at logical records 9..15 (7 copies), 17..23 (7), 29..31 (3), and 6..7 (2).

Treat **12 words as a strong candidate logical record width**, not yet a documented schema.

### XTR differences localize to transition records

Local `05FF/count33` (31 identical observed frames) matches the ATEC page except:
- `061C`: XTR `0003`, ATEC `0000`;
- `061E`: XTR `0001`, ATEC `0000`.

These positions fall in logical record 16, immediately after the seven-record repeated run 9..15.

Local `0662/count33` (268 identical observed frames) matches the ATEC page except:
- `067E`: XTR `0003`, ATEC `0000`;
- `067F`: XTR `0001`, ATEC `0000`.

These fall in logical record 24, immediately after the seven-record repeated run 17..23.

Therefore these four cross-platform differences are **transition-record metadata candidates**, not random page-tail deltas.

### Page-selection correlation and limitation

ATEC emits:
`05FF -> 0620 -> 0641 -> 0662`.

The locally walked XTR sequence emits:
`05FF -> 0662`.

That XTR jump is exactly three 33-word page strides, and XTR `061C=3`. This is an interesting numerical correlation.

A second XTR value `067E=3` would, under a literal stride interpretation, point from `0662` to `06C5` (`+3 * 0x21`). But local XTR becomes quiescent after ACKing `0662` and does not emit `06C5`. Therefore **do not label these fields as next-page pointers**.

### Alternative descriptor interpretation

The table repeatedly contains values numerically matching common range limits (`001F=31`, `000C=12`, `003B=59`, `0017=23`). A calendar/range/constraint descriptor structure is therefore a live competing hypothesis.

### Consequence

Best current classification:
**stable structured descriptor/configuration family with model-specific transition-record fields**.

Not proven:
- Online scheduler enable bits;
- page pointers;
- safe writable capability flags;
- exact semantics of the 12-word records.

Do not write reference ATEC values into the XTR discriminator fields.

Preferred next step: EXP230 offline semantic classification of the 12-word record schema.

## EXP229 semantic refinement — `055A..06E5` strongly indicated as calendar serialization

Thermia documentation provides a new semantic anchor for the 396-word family:

- CALENDAR controls four function groups: hot-water blocking, EVU/power limitation, silent mode, and temperature reduction.
- Each function supports up to 8 calendar settings, i.e. 32 user schedule slots.
- Thermia Online documentation independently describes 8 occasions for 4 calendar categories and start/end date fields.
- EXP229 found 396 words = 33 candidate records of 12 words.
- The raw table contains multiple date/time-range signatures, including maxima `59`, `23`, `31`, `12` and time/date-like combinations consistent with calendar fields.

Current classification is therefore upgraded from generic descriptor/configuration data to **strong calendar/schedule-serialization candidate**. The exact schema is not yet proven. In particular, do not yet assign fixed meanings to every word or assume the 33rd record is the clock/header, although 32 schedule slots + 1 metadata record is an attractive model.

No write target is established. Confirmation should use a passive UI-driven calendar differential test, not a direct Modbus write.




## EXP230 — `0709` command-pending field and exact `03E8` desired-state fetch

Offline analysis of four genuine Online/DCM captures produced 54 exact controller-side `0F 03 0708 0006` polls. Thirty-eight receive valid responses and sixteen are unanswered during early rejoin before the `0x0F` endpoint is ready.

Among the 38 valid responses:
- 36 have `0709=0000`;
- 2 have `0709=0001`;
- both and only those two `0709=0001` responses are immediately followed by `0F 03 03E8 000D`.

The command-state response is:

```text
0708  0000
0709  0001   <- strongest pending-command / pending-count candidate
070A  0000
070B  0000
070C  077F
070D  0006
```

The two exact command sequences are:

```text
11.383  0F 03 0708 0006
11.406  0F 03 0C 0000 0001 0000 0000 077F 0006
11.447  0F 03 03E8 000D
11.486  0F 03 1A 0017 0014 0028 0000 0001 0001 0012 0012 0002 0028 001E 003C 0014

23.962  0F 03 0708 0006
23.986  0F 03 0C 0000 0001 0000 0000 077F 0006
24.025  0F 03 03E8 000D
24.067  0F 03 1A 0016 0014 0028 0000 0001 0001 0012 0012 0002 0028 001E 003C 0014
```

Only `03E8` differs between the two desired-state images (`23 -> 22`), while the remaining 12 words are preserved. Since `03E8` is already established as Heating Curve, this is consistent with a full-image desired-state command serializer rather than a raw single-register write.

Timing is highly deterministic in these two examples:
- `0708` request -> response: 23/24 ms;
- pending response -> `03E8` read: 41/39 ms;
- `03E8` request -> desired response: 39/42 ms;
- complete chain: 103/105 ms.

On the next `0708` poll after each command, `0709` is zero again. Treat this as one-shot consume/clear behaviour; boolean versus count semantics are still unknown.

`070C/070D` are not the command trigger because their common `077F/0006` values occur in both idle and pending responses, while startup/rejoin captures show other values. Keep them semantically unknown/session-like.

A later genuine `090550` controller->0x0F FC16 snapshot at `03E8/count13` is byte-for-byte identical to the second desired-state response (`03E8=0016`). This supports persistence/acceptance but is not a same-capture apply acknowledgement.

### Write-access consequence

The Online/DCM desired-state side can now be represented as:

```text
controller: FC03 0708/count6
DCM:        0709 = 1  (pending)
controller: FC03 03E8/count13
DCM:        return full desired image
next poll:  0709 = 0
```

The unresolved blocker is no longer the `03E8` command payload shape. It is **activation of the local controller's read-side scheduler / genuine device recognition**. Direct second-master writes remain unsupported and should not replace that missing prerequisite.


---
## 2026-09-27 — EXP231 protocol finding: service-cycle homology points to XTR `0730..0737` read mailbox

Offline cross-capture analysis materially refines the write-access direction.

### Genuine ATEC/DCM scheduler
- 54 exact `0x0F FC03 0708/count6` requests were parsed across the four reference captures.
- Every request follows the A5 `002E/count10` response by 0.262..0.394 s and follows the recurrent `0x06` FC17 poll by 0.110..0.236 s.
- The cycle repeats at ~4.2 s.
- In DCM rejoin `090550`, scheduler polling is active from 0.987 s although `0x0F` does not ACK FC16 until 66.860 s and does not answer `0708` until 68.235 s; 16 polls are unanswered first.

**Protocol consequence:** `0x0F` ACK/readiness does not create the service scheduler. The scheduler is already active on the controller side. Ordinary ACK emulation is therefore the wrong lever for enabling it.

### Local XTR comparison
Local EXP221+EXP222 provide 72 exact `0x0F FC17 read 0730/count8 + write 071C/count8` requests. Median cadence is ~4.25 s, and each follows the XTR `0x06` poll (median ~0.247 s). This is the same broad recurring scheduler position occupied by the ATEC `0708` command-header poll after its `0x06` slot.

EXP226 proves only the FC17 write half: `071C..0723` is predominantly controller calendar/RTC serialization. The eight FC17 read registers `0730..0737` remain unknown because no response was captured.

### Refined interpretation
Do not call XTR FC17 and ATEC FC03 the same protocol. Their function codes, ranges and payload structure differ. However, the cadence and scheduler-position match now make `0730..0737` the strongest XTR-native candidate for the missing external-to-controller service/desired-state channel.

This changes write-access prioritization:
1. stop attempts to create ATEC `0708` by ACKing more local FC16 blocks;
2. preserve the proven ATEC mailbox model as cross-generation reference;
3. reconstruct the XTR `0730..0737` response image offline before any active reply;
4. never use guessed zero/echo data as a response because `0730..0737` semantics are still unknown.

The existing controller-state fingerprints (`A7F8` read span and `A811/A812`) remain correlates of scheduler-enabled vs local states, not safe write targets.


---
## 2026-09-27 — EXP232 protocol finding: Thermia FC17 uses paired `+0x14` role banks; XTR `0730..0737` is a real but unmapped ingress bank

EXP232 searched the current local/reference corpus for a genuine response to the XTR request `0F 17 0730 0008 071C 0008 ...`. None was found. In particular, an eight-word FC17 response would be 21 bytes with prefix `0F 17 10`; no such response exists in the relevant EXP221/222/225 or older EXP71/71B evidence. fclauson's register spreadsheet/logger and Discussion #143 also contain no `0730` field map or response payload.

The important positive result is structural. Known Thermia FC17 roles repeatedly place the external/slave-owned read bank and controller-written bank exactly `0x14` registers apart:

```text
slave 0x0A: read B3B0...   write B3C4...   delta +0x14
slave 0x06: read AFC8...   write AFDC...   delta +0x14
slave 0x04: read ABE0...   write ABF4...   delta +0x14
slave 0x05: read AC12...   write AC26...   delta +0x14
slave 0x0F: write 071C...  read 0730...   delta +0x14
```

For the XTR service region specifically, the three bases also satisfy:

```text
0708 + 0x14 = 071C
071C + 0x14 = 0730
```

ATEC/DCM uses FC03 `0708/count6` as its command/session header. XTR uses FC17 with controller data written at `071C/count8` and external data requested from `0730/count8`. This exact spacing is architecturally suggestive but does not make the protocols semantically interchangeable.

EXP226 already proves that the changing XTR `071C..0723` content is predominantly transformed RTC/calendar data. Therefore the safest current role model is:

```text
071C..0723 = controller-owned service/RTC state bank
0730..0737 = external/service-owned return bank (semantics unknown)
```

The direction matters: `0730..0737` is genuinely read by the controller, so it is a potential ingress surface. Other Thermia FC17 paths prove the general architectural possibility that a read-bank response can carry a semantic request into the controller (e.g. the independently established room-sensor pending-setpoint mechanism), but no field/value correspondence may be copied to the XTR bank.

### Consequence for write access

- Preserve the proven ATEC `0708 -> 03E8 desired-state` sequence as the strongest known command serializer.
- Treat XTR `0730..0737` as a high-value, generation-specific **candidate ingress bank**, not yet a proven command mailbox.
- Do not synthesize an FC17 reply from zeros, an echo, RTC inversion, or another slave's layout. The corpus does not establish a safe neutral response.
- The next useful work is cross-role FC17 schema analysis or acquisition of a genuine XTR/Connect/Online response, not an invented active packet.

---

## 2026-09-27 — DCM replacement / XTR 0730 research update

### Generic FC17 page structure

EXP233 confirms that Thermia commonly separates FC17 role banks by 0x14 registers. The XTR service region 0708 -> 071C -> 0730 is therefore strongly structured as consecutive 20-register service pages. The spacing does **not** prove common field semantics. Known roles place semantic request, transport and metadata fields at different offsets.

Consequences:

- 0730..0737 is real controller-ingress data by FC17 direction.
- No specific 0730 word is yet mapped.
- Eight zero words are not an evidence-backed idle image.
- Do not copy 0708 word positions, room-sensor request positions or AFCA semantics into 0730.

### Reference DCM mailbox state machine

The genuine DCM corpus now supports a stronger state-machine model:

~~~text
controller -> FC03 0708/count6
DCM        -> mailbox/lifecycle/status image

if 0709 == 1:
    controller -> FC03 03E8/count13
    DCM        -> full desired-state image
    next 0708 poll clears 0709
~~~

Across the available command capture, both and only the observed 0709=1 replies trigger the 03E8 desired-state fetch.

0708 is broader than a command flag. During rejoin, a first successful image of:

~~~text
0000,0000,7FFF,FFFF,0080,0007
~~~

is followed about 69 ms later by the controller beginning a large ordered FC16 state snapshot. Later idle operation uses:

~~~text
0000,0000,0000,0000,077F,0006
~~~

Other captures show 070C=0080 or 0000 while snapshot traffic continues, so 070C=0080 is not a simple boolean "snapshot active" flag.

The command desired-state image at 03E8/count13 is byte-for-byte identical to a controller FC16 state image observed in a rejoin capture. The representation can therefore be shared while direction and ownership define semantics.

### Local XTR implication

The local XTR cold-boot/recovery FC17 pair remains:

~~~text
slave 0x0F
read  0730/count8
write 071C/count8
~~~

Most of 071C..0723 is decoded as transformed controller RTC/calendar data. 0730..0737 remains unknown.

The improved reference architecture changes the search heuristic: a genuine XTR 0730 response may be primarily a service/session/status/dirty-selector image that causes a subsequent controller-initiated transaction. It should not be assumed to contain the requested Heat Curve value directly.

This is an architectural analogy only. No 0708 word index or literal value is transferable to 0730 without XTR-specific evidence.

### Local UI causality

Physical UI changes on the XTR are exported by controller-originated 0x0F FC16 pages:

- Heat Curve -> 03E8 family;
- Activate Cooling -> 0442 family;
- Operation Mode -> 0553 inside 0546/count20.

Directly replaying the Heat Curve 03E8 image toward 0x0F did not create the semantic mutation. These pages are therefore treated as controller-owned state/configuration serialization, not the primary local command ingress.

EXP237 found no distinct reversible Heat Curve ingress event in the parser-recognized standard traffic before the first target-valued export. This negative is bounded by the parser whitelist; raw UART bytes were not exhaustively classified.

### Raw Link CC firmware boundary — EXP234B

Direct Windows CE binary extraction of Danfoss Link CC 2.7.42 recovered the expected application stack:

~~~text
DHP ParameterID/value
    -> ParameterCache / SyncParameters
    -> HE Set/Get / ServiceBind
    -> HECTArch / Z-Wave
    -> [missing DCM03 / Connect local Thermia translator]
~~~

Real DHP parameter constants such as 0x030A, 0x4402 and 0x4414 are present, but no identifiable XTR 071C/0730 response builder or service-page serializer exists in the audited host stack. Apparent 0708 constants in RegulationEngine are ordinary decimal-1800 timing/configuration values.

**Current protocol consequence:** the highest-value software artifacts are a Thermia Connect/DCM03 firmware/update image or the XTR Gateway/controller implementation of the opposite side of 071C/0730. No active 0730 response is approved.


---

## 2026-09-27 — Genuine iTec Eco 5 Online capture: 071C/0730 promoted to authenticated/session gate

A newly shared genuine Online capture from an iTec Eco 5 materially resolves the relationship between the XTR-style FC17 service exchange and the older 0708 mailbox architecture.

### iTec Online state-machine sequence

Externally reported sequence:

~~~text
power-on
  ↓
controller repeatedly:
0x0F FC17
  read  0730/count8
  write 071C/count8
  ↓
genuine gateway eventually returns 16-byte response
  ↓
071C/0730 polling stops
  ↓
controller starts ACKed 0x0F FC16 full-state synchronization
  ↓
controller polls 0x0F FC03 0708/count6 mailbox
  ↓
app-originated desired-state reads become available
~~~

When the gateway is physically absent, the gate never completes and the downstream Online state machine does not start.

### 0x06 / 0x0A / A5 architecture correction

On this genuine iTec Eco 5 Online installation:

- 0x06 FC17 remains unanswered;
- 0x0A FC17 remains unanswered;
- A5, A4 and 0x05 are absent.

Therefore these roles are not prerequisites for iTec Online gateway operation. A5/A4/0x05 should be treated as reference-platform-specific until independently observed on iTec.

### 071C payload semantic correction

The previous local interpretation of 071C..0723 as an encoded RTC/calendar block is contradicted by the external genuine-gateway capture and is withdrawn as a general protocol model.

Reported challenge/response examples:

~~~text
63cefb32c6f41382087992370caceeba
    -> 1691a5f3f8e8d58738924416e8e6a3d5

31fb59fc8fb1175cd89f904d06d92ea4
    -> fd636ccd0f921d83ff232a1a2413b372
~~~

Both sides are exactly 16 bytes / eight registers and appear noise-like. Roughly 90 controller values vary across the capture; one exact controller value repeats four seconds later during an unanswered exchange, consistent with retry behavior.

**Strongest current hypothesis:** 071C is a controller challenge/session token and 0730 is a gateway response/authenticator. Do not yet label the primitive AES, CMAC or any other specific cryptographic algorithm.

### iTec mailbox confirmation

After the gate succeeds, mailbox behavior matches the older genuine DCM model:

- second mailbox word value 1 triggers controller FC03 read of decimal 1000 / hex 03E8 count14;
- second mailbox word value 8 triggers FC03 read of decimal 1070 count15;
- the gateway supplies the desired-state page;
- controller applies the change;
- physical-display changes instead produce controller FC16 exports without mailbox involvement.

This resolves a major uncertainty: the older 0708 -> desired-state architecture is relevant to iTec, but only **after** successful 071C/0730 session establishment.

### Implementation consequence

A minimal ESP-based iTec Online/DCM replacement now has a much clearer architecture:

~~~text
1. observe controller 071C 16-byte challenge
2. compute valid 0730 16-byte response
3. wait for controller to enter Online state and start mailbox polling
4. answer 0708 mailbox in idle state
5. when HA requests a change, assert the correct mailbox selector
6. answer the controller's subsequent FC03 desired-state page read
7. return mailbox to idle and reconcile controller FC16 state exports
~~~

The single dominant blocker is step 2: the 16-byte challenge/response function and its key/state.

---

## 2026-09-27 — EXP239–EXP248 protocol consolidation

### 071C/0730 must be treated as a role-bank contract with at least two payload regimes

The common transaction is:

```text
slave 0x0F FC17
read  0730/count8
write 071C/count8
```

Current evidence supports at least two distinct observed encoders:

```text
local XTR M, no genuine Online endpoint
    -> deterministic redundant RTC/calendar service record

externally reported genuine iTec Eco 5 + Online
    -> high-entropy retryable challenge-like 16-byte record
```

The local XTR interpretation is now based on 129/129 exact recovered frames. The external Eco 5 challenge-like behavior must remain separate pending full independent raw-log reprocessing.

### Local XTR calendar/service record

Across the local corpus, changing bytes are fully explained by date/time plus deterministic redundancy:
- year-2000;
- hour;
- day-of-month;
- 4x minute;
- three related second encodings.

`F9/06` is an exact complemented pair and a strong September month/complement candidate. `001E` is a strong September days-in-month candidate. Fixed bytes `45 AC DC C5 00 8F` remain format/signature candidates.

There is no unexplained per-frame nonce/MAC-like entropy in the local 16-byte controller image.

### Local state-transition negative

A historical census shows 129/129 local frames remain in the RTC/service regime across tested states, including:
- A80E/AFDC promotion;
- active historical 0x06 zero-response participation;
- partial 0x0F FC16 ACK participation.

No local RTC -> Eco-5-like challenge transition is present in the known corpus.

### Natural retry stop — EXP248

A complete RX-only cold boot directly measures the unanswered target stream:

```text
first target       +1.283 s after BUS_RETURN
target count       63
median cadence     4.298 s
last target        +267.123 s
final state        A80E=0028 A80F=000A AFDC=0010
confirmed silence  80.793 s
false stops        0
parser resync Δ    0
RX drop Δ          0
```

The rest of the bus continues normally after the final target. Therefore target disappearance is a genuine service-state stop, not bus loss.

No A80E/A80F/AFDC edge coincides with the stop and cadence does not back off.

Leading hypothesis: approximately **270 s startup/service retry deadline**. With the measured cadence, the next request would normally fall near +271.421 s. Repeatability is still required before promoting this to a protocol constant.

### External Eco 5 challenge/response analysis

Two reported genuine pairs remain:

```text
63cefb32c6f41382087992370caceeba -> 1691a5f3f8e8d58738924416e8e6a3d5
31fb59fc8fb1175cd89f904d06d92ea4 -> fd636ccd0f921d83ff232a1a2413b372
```

Simple linear/static transforms, common unkeyed hashes and several direct AES/CMAC key-search constructions have been excluded. No specific primitive or key is proven.

### DCM03 firmware target

Official topology evidence places DCM03 directly on the DHP-AQ/iTec-like RS485 path. Public profile evidence repeatedly reports DCM version **2.0.17** across multiple classic Thermia families.

No public standalone DCM03 firmware/update package, service loader, readable MCU identity or debug interface has been recovered from the inspected public artifacts.

### Safety consequence

No active XTR `0730` response is approved.

In particular:
- do not replay the two Eco 5 responses against the local XTR RTC/service record;
- do not use eight zeros;
- do not echo 071C;
- do not brute-force response words.

The next safe discriminator is **EXP249**, a second identical RX-only cold boot to test repeatability of the ~267 s / 63-target stop.

