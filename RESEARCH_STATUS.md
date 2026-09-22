# Thermia iTec XTR M – Reverse Engineering Research Status

_Last updated: 2026-09-22_

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
| `B3B1` | room sensor → controller | pending/requested room setpoint | STRONGLY INDICATED |
| `B3B2` | room sensor → controller | unknown | OPEN |
| `B3C4` | controller → room sensor | unknown/controller data | OPEN |
| `B3C5` | controller → room sensor | propagated/confirmed room setpoint | PROVEN |
| `B3C6` | controller → room sensor | likely boost/request/status | STRONGLY INDICATED |

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

## Direct write attempt to `B3B1`

A separate Modbus-master request to the room sensor was ACKed by the room sensor, but the Thermia controller did **not** adopt the new setpoint.

**Conclusion:** writing the register independently is not equivalent to behaving as the room sensor in the controller's expected response slot.

## Current room-sensor avenue

A promising future test is:

- disable/unplug the physical room sensor or otherwise avoid collision;
- answer the controller's exact `0x0A` FC17 poll as the slave;
- return a controlled `B3B1` setpoint request.

This route has not yet been completed in a collision-safe final experiment.

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

# 14. Historical natural `A80E/AFDC` cycle

Older captures showed a repeating natural cycle roughly every ~65 s:

```text
A80E 0 -> 32
AFDC 0 -> 32

~17 s later:

A80E 32 -> 0
AFDC 32 -> 0
```

This occurred repeatedly in older passive captures.

This matters because newer EXP88/90/91 presence tests did **not** reproduce it.

Possible explanations still open:

1. a different controller state was active in the old captures;
2. a real/previous DCM session had already established hidden state;
3. the cycle is triggered by another accessory field not yet identified;
4. boot or controller-session history matters;
5. a completed REQ/ACK transaction is needed before the state machine begins;
6. another device or condition on the bus was different.

---

# 15. Experiment chronology

This is intentionally compact. Individual YAML/log files contain the full details.

| Experiment(s) | Main question | Result |
|---|---|---|
| EXP10–18 | Which response word triggers controller ACK? | `word2=03E8` in correct phase is decisive |
| EXP21–28 | Do trailing words/selectors/counts produce a setting write? | No |
| EXP29 | Passive correlator | diagnostic only |
| EXP30–31,33 | outdoor-related probes | no semantic write discovered |
| EXP35–42 | passive mapping | useful telemetry, no write path |
| EXP43+ | active `0x02` probes | no final semantic write path |
| EXP48–49 | presence / multi-poll sequencing | fast cadence/state behaviour refined |
| EXP50 | passive DCM audit | mapped recurring structure |
| EXP51 | single presence-like response | cadence/state only |
| EXP52 | `00FF,1,03E8,1...` | ACK works; no setting write |
| EXP53 | `word2=440C` | no ACK |
| EXP54 | `word2=03F4` | no ACK |
| EXP55 | `word2=04A6` | no ACK |
| EXP56B/C | `word2=03E8`, varying `word3` | ACK independent of simple word3 value |
| EXP57 | bare `03E8` | ACK works |
| EXP58 | bare `03E8` at wrong/normal-long phase | fast cadence, no `0861` ACK |
| EXP59 | all-zero stage then SHORT `03E8` | ACK; `00FF` unnecessary |
| EXP60 | same `03E8` on LONG vs SHORT | SHORT phase matters |
| EXP61 | later valid SHORT `03E8` | ACK repeats |
| EXP62 | selector `03E9` | no ACK |
| EXP63 | trailing `03F4,22` | ACK transport only, no setting |
| EXP64 | words4/5=`03F4,23` | no setting |
| EXP65 | words3/4 register/value variant | no setting |
| EXP66 | HE-like GET `0x440C` | handshake only, no semantic response |
| EXP67 | post-close bare `03E8` on first FAST-LONG | no second ACK |
| EXP68 | raw 12-word local settings block | no change |
| EXP69B | same on second SHORT | no change |
| EXP70 | repeated zero responses | fast cadence only |
| EXP71 | apparent online promotion | later shown to be natural boot behaviour, not EXP-caused |
| EXP71B | zero replies after boot state | maintained fast cadence |
| EXP72 | natural boot AFDC/A80E state + bare `03E8` | transport behaviour confirmed |
| EXP73/73B | passive/manual curve correlation | local curve changes do not announce through AFDC/A80E |
| EXP74 | one-shot `[03E8,1,36]` | ACK, no curve write |
| EXP75 | persistent `[03E8,1,36]` | no write; ACK remains high while REQ held |
| EXP76B | canonical four-phase handshake | PROVEN |
| EXP77 | canonical HE GET endpoint 1 | no semantic response |
| EXP78 | endpoint 0 direct | negative |
| EXP79 | byte-swapped endpoint 0 | negative |
| EXP80 | +1-byte shifted HE layout | negative |
| EXP81 | historical envelope + raw HE body | negative |
| EXP82 | envelope + length=2 + HE body | negative |
| EXP83 | historical envelope + scalar curve candidate | handshake works; no write |
| EXP84 | passive room-setpoint correlation | AFDC..AFE0 unaffected |
| EXP85 | passive DCM source correlator | no source edge during capture |
| EXP86 | 30-minute passive first-edge capture | no A80E/A802/AFDC edge |
| EXP87 | zero presence | implementation guard stopped ~35 s; no semantic edge before stop |
| EXP88 | fixed zero presence, 180 s | negative |
| EXP89 | intended persistent `00FF` | invalid due second-buffer bug |
| EXP90 | corrected persistent `00FF`, 90 s | negative |
| EXP91 | `00FF,1,REQ-low,1` envelope, 90 s | negative |

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

---

# 17. Current protocol model

The best current model is:

```text
Controller normal poll
    |
    | 0x06 FC17 ~4.3 s
    v
Accessory gives any syntactically valid response
    |
    v
Fast accessory cadence starts
    |
    +--> SHORT ~0.7 s
    |
    +--> FAST-LONG ~1.4 s
```

For a transaction:

```text
semantic data stable
REQ / AFCA = 0
        |
        v
REQ / AFCA = 03E8
        |
        v
controller sets 0x0F:0861 = 16
        |
        v
REQ / AFCA = 0
(data held stable)
        |
        v
controller sets 0861 = 0
        |
        v
transaction closed
```

What is still missing is the meaning/encoding of the remaining accessory semantic fields.

---

# 18. Most likely architecture now

Current working hypothesis:

```text
AFC8..AFD3
```

are not a generic packet buffer.

They are more likely a **fixed semantic DCM register bank**, analogous to the room-sensor registers:

```text
room sensor:
B3B0  room temperature
B3B1  requested setpoint
B3B2  status/unknown
```

The DCM may similarly expose fixed fields for:

- integration/online state;
- setting ownership;
- parameter value;
- parameter selector or category;
- request type;
- controller demand;
- mode/status.

`AFCA / word2` is already known to be the REQ/data-valid level.

The remaining fixed fields still need to be identified.

---

# 19. Next high-value experiments

## A. Completed handshake → long REQ-low observation

A strong next test is:

1. establish fast cadence;
2. present the historical envelope;
3. perform one **bare, non-semantic four-phase `03E8` handshake**;
4. close it correctly;
5. continue with the historical REQ-low envelope for ~90 s;
6. observe whether `A80E/AFDC` begins the historical cycle.

This tests whether a **completed transaction/session** is required before the controller considers the accessory fully initialized.

No setting payload is needed.

---

## B. Room-sensor slave emulation

Potentially the most direct semantic control route:

```text
controller polls 0x0A
        ↓
ESP answers in the room-sensor response slot
        ↓
B3B1 = requested room setpoint
```

Requirements:

- physical room sensor must not answer at the same time;
- collision handling must be deterministic;
- start with a harmless/no-op response;
- then one controlled setpoint change;
- verify central `03F4` and returned `B3C5`.

This route is based on observed real semantic behaviour and may be more promising than continuing to guess DCM payloads.

---

## C. Recover actual DCM03 firmware / protocol material

The highest-value external evidence would be:

- DCM03 firmware image;
- DCM03 MCU identification;
- service-tool protocol;
- factory test software;
- schematic;
- old Danfoss/Thermia integration documentation;
- another reverse engineer's real DCM bus capture.

This could reveal the missing HE → local RS485 translation directly.

---

## D. Correlate AFDD..AFDF with real controller state changes

Natural or deliberately safe state changes could help identify the remaining controller→DCM fields:

- heating start/stop;
- DHW start/stop;
- SG Ready transitions;
- heating/cooling mode changes;
- controller demand changes.

No accessory write is required for this research.

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

What we know:

```text
RS485 = Modbus RTU 9600 8E1

0x0A = room sensor
0x0F = local controller settings
0x06 = DCM/Online accessory slot

0x06:
  controller reads  AFC8..AFD3
  controller writes AFDC..AFE0

AFCA / response word2:
  0000 = REQ low
  03E8 = REQ high

0x0F:0861:
  0  = ACK low
  16 = ACK high
```

Four-phase handshake:

```text
REQ 0
REQ 03E8
ACK 16
REQ 0
ACK 0
```

But:

```text
transport ACK != semantic command success
```

The remaining challenge is identifying the **fixed semantic meaning of the other `AFC8..AFD3` fields**.

That is the current frontier of the reverse engineering.
