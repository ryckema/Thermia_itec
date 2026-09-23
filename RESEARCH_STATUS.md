# Thermia iTec XTR M – Reverse Engineering Research Status

_Last updated: 2026-09-23_

This document summarizes the reverse-engineering work performed so far on a **Thermia iTec XTR M + Total Compact** installation using an **ESP32-S3 / isolated RS485 interface** and Home Assistant.

The main goals are:

1. reliably read the local Thermia bus;
2. understand the controller ↔ accessory protocols;
3. identify a safe semantic write path for room setpoint, heating settings and possibly operating mode;
4. avoid disturbing normal heat-pump operation;
5. document failed hypotheses so other researchers do not have to repeat the same dead ends.

> This work applies to the tested older/non-Genesis iTec platform. Register meanings and protocol behaviour should not automatically be assumed to apply to other Thermia generations.

---

## Status legend

- **PROVEN** — reproduced with clear bus evidence.
- **STRONGLY INDICATED** — consistent evidence, but not fully proven.
- **NEGATIVE** — tested and did not produce the expected semantic effect.
- **OPEN** — unresolved.

---

# 1. Hardware and physical bus

Test hardware:

- Waveshare ESP32-S3-RS485-CAN
- ESP32-S3R8
- 16 MB flash
- 8 MB octal PSRAM
- RS485 TX: GPIO17
- RS485 RX: GPIO18
- RS485 DE/direction: GPIO21
- GPIO21 LOW = receive mode

Observed Thermia bus:

- Modbus RTU
- 9600 baud
- 8 data bits
- EVEN parity
- 1 stop bit
- valid Modbus CRC16

Current tested RJ45 connection:

- pin 1 → RS485 A+
- pin 3 → RS485 B-

Working connector hypothesis from the wider investigation:

- pins 1/2 = A
- pins 3/4 = B
- pins 5/6 = GND
- pins 7/8 = +12 V

The Waveshare 120 Ω termination jumper is normally left **OFF** while passively attaching to the existing bus.

---

# 2. Observed slaves

| Slave | Current interpretation | Status |
|---|---|---|
| `0x02` | main/controller-side state and command context | PROVEN |
| `0x06` | Online/DCM/accessory slot | PROVEN |
| `0x0A` | room sensor | PROVEN |
| `0x0F` | controller settings/state blocks | PROVEN |
| `0x14` | auxiliary block, semantics largely unknown | OPEN |
| `0x1E` | outdoor-unit telemetry/control context | PROVEN |

---

# 3. Passive telemetry

Read-only monitoring is stable and usable in Home Assistant.

Known/usable values include:

- outdoor temperature
- room temperature
- room setpoint
- supply temperature
- return temperature
- DHW temperature
- heating curve
- heating min/max
- heating curve corrections
- room factor
- compressor frequency
- compressor current
- condenser temperatures
- discharge temperature
- high pressure
- fan speed
- expansion-valve position
- SG mode
- controller context/state
- derived compressor status
- derived delta-T values

Long clean captures have been observed with:

- `resync_delta = 0`
- `drop_delta = 0`

---

# 4. Slave `0x0A` – room sensor path

The controller periodically sends FC17 to the room sensor:

```text
0A 17
read  B3B0 count 3
write B3C4 count 3
```

## Known registers

| Register | Direction | Meaning | Status |
|---|---|---|---|
| `B3B0` | room sensor → controller | room temperature, tenths of °C | PROVEN |
| `B3B1` | room sensor → controller | pending/requested room setpoint | PROVEN (cross-model; works when returned in the polled room-sensor response slot) |
| `B3B2` | room sensor → controller | unknown | OPEN |
| `B3C4` | controller → room sensor | unknown/controller data | OPEN |
| `B3C5` | controller → room sensor | propagated/confirmed room setpoint | PROVEN |
| `B3C6` | controller → room sensor | unknown; possible alarm/status carrier | OPEN |

Example room-sensor response:

```text
0A 17 06
00 DD   # 22.1 °C
00 00
00 00
CRC
```

## Real room-sensor setpoint behaviour

A genuine room-sensor-originated setpoint event caused:

1. a room-sensor request;
2. the central Thermia room-setpoint setting to update;
3. the value to propagate back through `B3C5`.

This proves that the room-sensor path is a real semantic write path into the controller.

## `B3B1` request semantics

A separate Modbus-master write to the physical room sensor was ACKed by the room sensor, but the Thermia controller did **not** adopt the new setpoint.

**Conclusion:** writing the register independently is not equivalent to behaving as the room sensor in the controller's expected response slot.

However, the independent iTec Eco 8 / DHP-AQ cross-check has now confirmed the actual slave-response semantics:

- `B3B0` = measured room temperature ×10;
- `B3B1` = pending room-setpoint request, whole °C;
- `B3B2` = zero when nothing else is requested/known.

Returning a non-zero `B3B1` value in the controller's own FC23 poll response causes the controller to adopt that room setpoint and propagate it back through `B3C5`. Returning `0` means “no request”; it does not clear or restore the previous setpoint.

This is therefore a real semantic write path, but it is a **room-sensor control path**, not the target Online/DCM `0x06` path.

## Current room-sensor avenue

The path is technically understood well enough to emulate, provided collision handling with a physical room sensor is deterministic. It remains useful as a reference implementation of how Thermia accessory writes are expressed through a polled slave response, but the main research target is native `0x06` Online/DCM write access.

---

# 4A. Independent iTec Eco 8 / DHP-AQ cross-check

A second researcher has independently reproduced several mappings on a 2017-era **iTec Eco 8** using the Danfoss DHP-AQ board. This helps separate platform properties from XTR-M-specific observations.

Confirmed cross-model results include:

- `0x1E FC04 0x0014` operating-state sequence `29 → 28 → 24 → 16`;
- state `20` is an autonomous sequence, **not defrost**;
- `0x1E FC04 0x0015`: `0x0200` outdoor active, `0x0040` DHW context, `0x0020` heating context;
- `0x1E FC16 0x0004`: `1` heating, `2` hot water (`3` cooling on the XTR M map, not yet observed on the Eco 8);
- `0x02:A80C`: bit `0x01` = DHW request, bit `0x40` = compressor running;
- `0x02:A80F` is **not** modulation/output/load percentage;
- `0x1E FC04 0x001E..0x0033` is not a live mirror of `0x0000..0x0015`; it behaves like a delayed/latched copy;
- `0x0A:B3B1` setpoint-request semantics are independently confirmed.

The Eco 8 address scan found only `0x02` and `0x1E` as normal readable slaves plus polled accessory slots `0x06` and `0x0A`; slave `0x14` appears installation/model-specific rather than universal.

---

# 5. Slave `0x0F` – local settings block

A recurring FC10 block at `0x03E8..0x03F5` contains controller settings.

Typical observed values:

```text
35,20,40,1,0,0,20,20,2,40,30,1,22,2
```

Current mapping:

| Register | Meaning | Status |
|---|---|---|
| `03E8` | Heating Curve | PROVEN |
| `03E9` | Heating Minimum | PROVEN |
| `03EA` | Heating Maximum | PROVEN |
| `03EB` | Curve correction +5 | PROVEN |
| `03EC` | Curve correction 0 | PROVEN |
| `03ED` | Curve correction -5 | PROVEN |
| `03EE` | Heating Stop | PROVEN |
| `03EF` | Reduced temperature / related setting | STRONGLY INDICATED |
| `03F0` | Room Factor | STRONGLY INDICATED |
| `03F1` | Hot Water Start | STRONGLY INDICATED |
| `03F2` | unknown | OPEN |
| `03F3` | unknown | OPEN |
| `03F4` | room setpoint mirror | PROVEN |
| `03F5` | unknown | OPEN |

The production parser only considers a genuine controller-originated FC10 update of this block authoritative for settings-cache updates.

---

# 6. Danfoss Link / HE firmware research

Old Danfoss Link CC firmware was unpacked and inspected.

This provided the **host-side DHP/HE parameter model**, but not the missing DCM03 → Thermia RS485 translation layer.

## Recovered HE/DHP parameters

| HE parameter | Meaning |
|---|---|
| `0x4400` | HeatPumpType |
| `0x4401` | RoomValue |
| `0x4402` | HeatCurve |
| `0x4403` | HeatCurveMin |
| `0x4404` | HeatCurveMax |
| `0x4405` | HeatCurvePlus5 |
| `0x4406` | HeatCurveZero |
| `0x4407` | HeatCurveMinus5 |
| `0x4408` | HeatStop |
| `0x4409` | RoomFactor |
| `0x440A` | HotWaterStart |
| `0x440B` | ControllerDemand |
| `0x440C` | SupplyLineTemperature |
| `0x440D` | ReturnLineTemperature |
| `0x440E` | ExternalControl1 |
| `0x440F` | ExternalControl2 |
| `0x4410` | AuxiliaryHeaterPowerStage |
| `0x4411` | HotWaterTemperature |
| `0x4412` | OperationStatus |
| `0x4413` | ExternalControl3 |
| `0x4414` | IntegrationMode |
| `0x4415` | DefrostDemand |
| `0x4416` | EVU_SW |
| `0x4417` | EVU_HW |

Additional DHP parameters:

| Parameter | Meaning |
|---|---|
| `0x030A` | OperationMode |
| `0x0334` | OutdoorTemperature |
| `0x03E0` | OperationTime |
| `0x03F0` | ErrorCode |
| `0x0400..0x0404` | Alarm fields |
| `0x7001` | RoomSensorOperationMode |
| `0x7003` | RoomSensorOperationOff |

## HE Set/Get request format

Recovered request construction:

```text
BYTE endpoint
BYTE counts
WORD SET_ID[SET_count]
WORD GET_ID[GET_count]
SET values...
```

`counts`:

- high nibble = GET count
- low nibble = SET count

Maximum:

- 15 SET parameters
- 15 GET parameters

Recovered completion codes:

```text
0 = OK
1 = endpoint not found
2 = GET unknown parameter
3 = SET unknown parameter
4 = SET out of bounds
5 = SET read-only
6 = GET max payload exceeded
7 = SET unknown format
```

## Integration mode

`0x4414 IntegrationMode`:

- `0` = light/non-system integration
- `1` = system integration

In system integration mode the Link code switches several parameters from GET to SET, including:

- RoomValue
- HeatCurve
- HeatCurve +5 correction
- HeatCurve 0 correction
- HeatCurve -5 correction

This is strong evidence that the official Link/DCM stack can write those values.

## Important architecture conclusion

The Link firmware does **not** contain the Thermia RS485 translation.

Likely architecture:

```text
Link / HPNode / DHP model
        ↓
HE parameter protocol
        ↓
DCM03
        ↓
Thermia local RS485
```

The unresolved layer is therefore:

```text
HE Parameter ID/value
        ↓
DCM03 translation/state machine
        ↓
AFC8..AFD3 semantic fields
```

Raw HE parameter IDs must **not** be assumed to be local Thermia register addresses.

---

# 7. Slave `0x06` – Online/DCM accessory slot

The controller repeatedly sends:

```text
06 17
read  AFC8 count 12
write AFDC count 5
<5 write words>
CRC
```

Therefore:

- accessory → controller: `AFC8..AFD3` (12 registers)
- controller → accessory: `AFDC..AFE0` (5 registers)

The 12 read registers increasingly look like a **fixed semantic accessory register bank**, not a generic arbitrary register/value mailbox.

---

# 8. Controller → accessory registers `AFDC..AFE0`

Current interpretation:

| Register | Current meaning | Status |
|---|---|---|
| `AFDC` | delayed/derived accessory/controller state correlated with `A80E` bit `0x20` | PROVEN correlation |
| `AFDD` | unknown | OPEN |
| `AFDE` | unknown | OPEN |
| `AFDF` | unknown | OPEN |
| `AFE0` | propagated outdoor temperature | STRONGLY INDICATED |

## `AFE0`

Observed examples:

```text
AFE0 = 0x0016 -> 22 °C
AFE0 = 0x0015 -> 21 °C
AFE0 = 0x0013 -> 19 °C
```

It tracks the controller/outdoor-temperature path.

## `A80E` ↔ `AFDC`

Historical captures repeatedly showed:

```text
A80E 0 -> 32
AFDC 0 -> 32
```

followed by:

```text
A80E 32 -> 0
AFDC 32 -> 0
```

AFDC follows A80E after the next relevant controller/accessory update.

This is a real controller-originated state propagation and **not** the transaction ACK.

---

# 9. `03E8` request level and `0861` ACK

One of the strongest findings is the level-based handshake between:

- `0x06` response word 2 / `AFCA`
- `0x0F:0861`

## Proven behaviour

With the accessory in the correct phase:

```text
AFCA = 0000
```

is REQ low.

Then:

```text
AFCA = 03E8
```

causes:

```text
0x0F:0861 = 16
```

roughly 0.3–0.4 s later.

If `03E8` is held:

```text
0861 remains 16
```

When AFCA is returned to `0000` while the remaining payload stays stable:

```text
0861 returns to 0
```

roughly 1 s later.

## Canonical four-phase transaction

```text
1. payload stable, REQ=0
2. set AFCA / REQ = 03E8
3. controller ACK 0861 rises to 16
4. set AFCA / REQ back to 0, keep payload stable
5. controller ACK 0861 falls back to 0
6. payload may then be cleared/changed
```

**PROVEN:** this is a real transport-level REQ/ACK mechanism.

**NOT PROVEN:** the semantic encoding of the other 11 accessory words.

---

# 10. `0x06` cadence behaviour

Normal unserved `0x06` polling is approximately:

```text
~4.3 s
```

After the controller receives a syntactically valid `0x06` response, it enters a fast accessory cadence that alternates approximately:

```text
SHORT     ~0.65–0.78 s
FAST-LONG ~1.35–1.46 s
```

This can be sustained with simple valid responses.

**Important:** entering fast cadence does **not** mean a semantic command has been accepted.

---

# 11. Major active hypotheses tested

## A. `03E8` as a local register pointer

Early hypothesis:

```text
word2 = 03E8
```

might mean "local register 03E8 / Heating Curve".

### Result

NEGATIVE.

Evidence showed that:

- `03E8` causes the transaction ACK;
- nearby values such as `03E9`, `03EA`, `03F4`, `04A6`, `440C` do not;
- its behaviour is phase/level dependent;
- keeping it asserted keeps ACK high.

**Conclusion:** `03E8` is a transport REQ/data-valid level, not a local register address.

---

## B. `00FF` required for ACK

Hypothesis:

```text
w0 = 00FF
```

might be required for a valid request.

### Result

NEGATIVE.

Bare `03E8` in the correct phase can trigger ACK without `00FF`.

Later EXP90 also held `w0=00FF` for 90 s without generating any `A80E/AFDC` online-state cycle.

**Conclusion:** `00FF` is not required for ACK and is not sufficient as an online-state trigger.

---

## C. Simple local register/value command

Multiple layouts were tried around the proven REQ field, for example:

```text
03E8, count, value
```

and placements involving:

```text
03F4, room setpoint
03E8, heating curve
```

### Result

NEGATIVE.

The transport handshake completed, but settings did not change.

---

## D. Raw 12-word local settings image

A full local settings block was placed directly into the 12-word `0x06` accessory response.

### Result

NEGATIVE.

No semantic write occurred.

---

## E. Raw HE parameter protocol directly inside `0x06`

Canonical HE GET/SET-like bodies were attempted with:

- endpoint `0`
- endpoint `1`
- alternative endpoints
- byte-swapped forms
- shifted/aligned variants
- GET of known parameter `0x440C`
- historical envelope around HE body

### Result

NEGATIVE.

No returned semantic data or setting write was observed.

**Conclusion:** the `0x06` registers do not expose the host HE packet directly in any simple byte/word layout tried so far.

---

## F. Historical envelope

Historical request image:

```text
w0 = 00FF
w1 = 0001
w2 = 03E8
w3 = 0001
...
```

was repeatedly able to complete the known transport handshake.

Variants were tested with:

- HE body
- scalar curve value
- length/count interpretations
- endpoint interpretations
- REQ-low persistent envelope

### Result

The envelope participates in a valid transaction context, but none of the tried semantic payload interpretations changed a setting.

EXP91 held:

```text
00FF,0001,0000,0001,0...
```

for 90 s and received 84 valid responses with:

- no `A80E` edge;
- no `AFDC` promotion;
- no `0861` ACK because REQ remained low;
- no settings mutation;
- no parser/RX errors.

**Conclusion:** `w1=1` and `w3=1` plus `w0=00FF` are not sufficient on their own to activate the historical online-state cycle.

---

# 12. Passive correlation experiments

## Room setpoint vs `AFDC..AFE0`

A manual room-setpoint round trip:

```text
22 -> 23 -> 22
```

changed:

- room sensor path (`B3C5`)
- controller room-setpoint mirror (`03F4`)

but did **not** change:

```text
AFDC..AFE0
```

**Conclusion:** the five controller→DCM words do not directly carry the normal room setpoint.

---

## Long passive DCM correlation

A 300-second passive run observed:

```text
AFDC..AFE0 = stable
A80E = stable
A802 = stable
```

No useful natural edge occurred.

A later 30-minute passive run also saw no `A80E`/`AFDC` edge.

**Conclusion:** long passive waiting is not a reliable way to reproduce the old accessory-state cycle.

---

# 13. Presence / online-state experiments

These tests were designed to understand whether a particular accessory response causes the controller to enter the historical `A80E/AFDC` cycle.

## EXP88 – all-zero presence

Response:

```text
0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000
```

Result over 180 s:

- 168 valid responses
- fast cadence sustained
- `A80E=0000`
- `AFDC=0000`
- `0861=0`
- no settings changes
- no parser/RX errors

**NEGATIVE:** valid presence alone is not enough.

---

## EXP89 – intended `00FF` presence

This experiment contained an implementation mistake:

- response 1 used `00FF`;
- later responses accidentally fell back to all-zero.

**INVALID AS A DISCRIMINATOR.**

Do not use EXP89 as evidence against `00FF`.

---

## EXP90 – persistent `00FF`

Every response:

```text
00FF,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000
```

Result:

- 84 identical responses
- 90 s
- observed response CRC `88E8`
- fast cadence stable
- `A80E=0000`
- `AFDC=0000`
- `0861=0`
- no settings changes
- no parser/RX errors

**NEGATIVE:** `w0=00FF` alone is not the missing online-state trigger.

---

## EXP91 – historical envelope with REQ low

Every response:

```text
00FF,0001,0000,0001,0000,0000,0000,0000,0000,0000,0000,0000
```

Observed response CRC:

```text
C9A9
```

Result:

- 84 identical responses
- 90 s
- fast cadence stable
- `A80E=0000`
- `AFDC=0000`
- `0861=0`
- no settings changes
- `resync_delta=0`
- `drop_delta=0`

**NEGATIVE:** the historical envelope with REQ low is not sufficient to start the online-state cycle.

---

# 14. Natural `A80E/AFDC` lifecycle

Older and newer passive captures show a repeating natural controller lifecycle:

```text
A80E 0 -> 32
AFDC 0 -> 32
...
A80E 32 -> 0
AFDC 32 -> 0
```

Later passive experiments proved that this lifecycle occurs **without any ESP transmission**. Therefore `A80E=0x20` and `AFDC=0x20` are not evidence of DCM login/session acceptance. EXP106 further showed the same cycle while `A80F` was at least `75`, `80` and `50`, so `A80F=50` is not a unique gate either.

---

# 15. Experiment chronology

This is intentionally compact. Individual YAML/log files contain the full details.

| Experiment(s) | Main question | Result |
|---|---|---|
| EXP10–18 | Which response word triggers controller ACK? | `word2=03E8` in correct phase is decisive |
| EXP21–28 | trailing words/selectors/counts | no semantic write |
| EXP29–50 | passive mapping / presence / controller-state work | transport and telemetry refined |
| EXP51–75 | presence, selector, scalar, register/value and persistence hypotheses | ACK/cadence effects only; no semantic write |
| EXP76B | canonical four-phase handshake | **PROVEN** |
| EXP77–83 | direct/raw HE layouts and historical-envelope variants | all negative semantically |
| EXP84–91 | passive correlations / presence variants | no semantic DCM state |
| EXP92 | full canonical handshake + historical envelope | transport ACK only |
| EXP93 | `A80F=50` discriminator | inconclusive then; superseded by EXP106 |
| EXP94 | passive cold boot baseline | deterministic boot sequence mapped |
| EXP95 | zero presence from cold boot | fast cadence only |
| EXP96 | historical envelope from cold boot | ACK only; no session effect |
| EXP97 | passive natural-state correlation | `A80E/AFDC` can cycle with no ESP TX |
| EXP98 | AFC8 A/B/A influence | negative |
| EXP99 | historical non-REQ field matrix | negative |
| EXP100 | AFC8/AFC9/AFCB combination matrix | negative |
| EXP101 | one-word matrix over `AFCC..AFD3` | negative |
| EXP102 | AFC9/AFCB count/structure matrix | negative |
| EXP103 | repeated identical canonical transaction chain | all ACKed; no semantic state |
| EXP104 | AFC8 sequence toggle `00FF→00FE→00FF` | all ACKed; no semantic state |
| EXP105 | canonical transaction gated on natural `A80E=AFDC=0x20` | ACKed; no semantic state |
| EXP106 | passive `A80F=50` sync discriminator | partial triggered run; 50 not unique/required for A80E/AFDC lifecycle |

---

# 16. Things that are now effectively ruled out

Do **not** repeat these without new evidence:

- treating `03E8` as a local Thermia register pointer;
- assuming `00FF` is required for ACK;
- assuming `00FF` alone activates Online/DCM state;
- simple `[register,value]` payloads;
- `03E8/count/value` layouts;
- arbitrary adjacent word placement;
- trailing `03F4,setpoint` combinations;
- full raw local-settings block in `AFC8..AFD3`;
- raw HE parameter IDs as local Thermia addresses;
- canonical HE GET endpoint 0 or 1 directly in the mailbox;
- broad endpoint enumeration without a new clue;
- byte-swapped HE layout;
- one-byte shifted HE layout;
- historical envelope + raw HE body;
- historical envelope + scalar curve;
- persistent all-zero presence as an online-state trigger;
- persistent `w0=00FF` as an online-state trigger;
- persistent `00FF,1,REQ-low,1` as an online-state trigger;
- direct independent Modbus-master write to room-sensor `B3B1` expecting the controller to adopt it.
- treating `A80E=0x20` or `AFDC=0x20` as proof of DCM login/session acceptance;
- using `A80F=50` as a unique gate for the natural A80E/AFDC lifecycle;
- simple AFC8 identity/sequence toggling (`00FF→00FE→00FF`);
- repeating identical canonical transactions as a session-establishment mechanism;
- simple AFC9/AFCB count/length interpretations;
- isolated one-word activation hypotheses across `AFCC..AFD3`;
- timing the known canonical transaction specifically inside the natural `A80E=AFDC=0x20` window.

---

# 17. Current protocol model

The best current model has **three distinct layers**:

```text
1. Transport presence
   valid 0x06 response -> fast ~0.7 / ~1.4 s cadence

2. Transaction transport
   AFCA 0 -> 03E8 -> 0
   0861 0 -> 16 -> 0

3. DCM application/session semantics
   UNKNOWN -> actual parameter read/write
```

Layers 1 and 2 are proven. Layer 3 remains unresolved. Fast cadence does not imply semantic acceptance; a complete `0861` handshake does not imply semantic acceptance; repeated transactions, AFC8 sequence toggling, and `A80E=AFDC=0x20` state gating have all been tested without semantic effect.

---

# 18. Most likely architecture now

The current working architecture is:

```text
Danfoss Link / Thermia Online host
        ↓
HE/DHP parameter model
        ↓
DCM03 internal serializer / state machine
        ↓
fixed 12-word Thermia accessory bank AFC8..AFD3
        ↓
controller
```

Proven inside the 12-word bank: `AFCA`/word2 is the REQ/data-valid level, and the controller returns the transport ACK through `0x0F:0861`. The remaining identity/integration/parameter-selector/value/session fields are still unknown. The inspected Link firmware does not expose this final serializer, so the missing translation is most likely inside DCM03 hardware/firmware.

---

# 19. Next high-value work

## A. Obtain one real DCM03 / Thermia Online bus capture

This is now the highest-value path. Capture from before power-up for 60–120 s, then make one safe official setting change (ideally `HeatCurve 36 → 37`), capture 10 s before through at least 30 s after, then restore `37 → 36`. The critical evidence is the **response from slave `0x06`**.

## B. Recover DCM03 firmware / hardware details

Useful targets: MCU identification, PCB/debug pads, firmware dump, service/factory software, Z-Wave Manufacturer Specific / Version information, or old Danfoss Link HP-kit engineering material.

## C. Cross-model validation on iTec Eco 8 / DHP-AQ

Directly test whether valid `0x06` responses cause fast cadence and whether `AFCA=03E8` produces the same `0861` ACK cycle. Reproduction would strongly support a platform-wide DHP-AQ/iTec transport layer.

## D. Passive correlation only when tied to a new clue

EXP106 shows `A80F=50` is not a unique DCM-sync discriminator. More long waits or near-identical timing variants are low value without new external evidence.

## E. Room-sensor path as reference

`0x0A:B3B1` is a proven semantic accessory-write path and a useful reference, but the project target remains native `0x06` Online/DCM access.

---

# 20. Safety approach

Active experiments are deliberately narrow.

Current rules:

- one active experiment at a time;
- exact expected `0x06` poll signature only;
- fail closed;
- compressor/outdoor-unit command guards where relevant;
- abort on parser/RX corruption;
- no direct writes to unknown controller registers;
- no broad Modbus register scanning while operating;
- keep production control on the known SG Ready interface until a semantic write path is proven.

For normal operation, the preferred configuration remains **receive-only**.

---

# 21. Current practical control fallback

The heat pump supports **Smart Grid Ready** inputs.

These are currently the safest known external control interface and can be driven using isolated relays/Shelly devices.

Until native bus writing is understood, SG Ready remains the recommended production-control path.

---

# 22. Contributions wanted

If you are researching the same Thermia/Danfoss platform, useful contributions include:

- bus captures containing a real DCM03;
- register traces during Danfoss Link setpoint/curve changes;
- DCM03 firmware dumps;
- PCB photos and MCU markings;
- official service manuals;
- protocol documentation;
- captures from another DHP-AQ/iTec generation;
- confirmed meanings for `AFC8..AFD3`;
- confirmed meanings for `AFDD..AFDF`;
- safe room-sensor emulation results.

Please include:

- heat-pump model;
- controller generation;
- DCM/Online hardware model if present;
- bus speed/parity;
- exact frame bytes;
- timing between frames;
- what was changed on the heat pump at that moment.

---

# 23. Short version

```text
RS485 = Modbus RTU 9600 8E1

0x0A = room sensor
0x0F = local controller settings/state
0x06 = DCM/Online accessory slot

0x06:
  controller reads  AFC8..AFD3 (12 words)
  controller writes AFDC..AFE0 (5 words)

valid 0x06 response -> fast ~0.7 / ~1.4 s cadence
AFCA 0000 -> 03E8 -> 0000
0861 0000 -> 0010 -> 0000
```

But:

```text
valid response != semantic session
fast cadence    != semantic session
transport ACK   != semantic command success
A80E/AFDC=0x20  != DCM login proof
A80F=50         != unique DCM sync gate
```

The remaining challenge is the **DCM03 application/session serializer** inside `AFC8..AFD3`. A real DCM03/Thermia Online cold-boot capture plus one safe official setting change is now far more valuable than further isolated-word guessing.

