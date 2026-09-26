# Thermia iTec XTR M – Reverse Engineering Research Status

_Last updated: 2026-09-26_

This document summarizes the reverse-engineering work performed so far on a **Thermia iTec XTR M + Total Compact** installation using an **ESP32-S3 / isolated RS485 interface** and Home Assistant.

The main goals are:

1. reliably read the local Thermia bus;
2. understand the controller ↔ accessory protocols;
3. identify a safe semantic write path for room setpoint, heating settings and possibly operating mode;
4. avoid disturbing normal heat-pump operation;
5. document failed hypotheses so other researchers do not have to repeat the same dead ends.

> This work applies to the tested older/non-Genesis iTec platform. Register meanings and protocol behaviour should not automatically be assumed to apply to other Thermia generations.

---

## Current status after EXP182

The write-path investigation has moved beyond the earlier assumption that one missing DCM register or one additional ACK would unlock control.

The strongest current model is that the genuine Online/DCM installation runs an **extended controller-side service scheduler / topology mode** that is not currently active on the tested XTR M.

### Observed reference behaviour

Genuine Online/DCM captures show a coherent service family:

- recurring `0xA5` polling plus related `0xA4 / 0x05` discovery/service activity;
- periodic controller-originated `0x0F FC03 0x0708/count6` mailbox polls;
- cyclic controller-originated `0x0F FC16` runtime uploads through `07D0, 07E4, 07F8, 080C, 0820, 0834, 0848, 0864, 0870, 0884`;
- full `0x03E8..` state resynchronisation when the DCM service joins/rejoins;
- immediate desired-state reads when the `0708` mailbox signals pending command data.

The `0708/count6` scheduler is demonstrably controller-side: in the DCM-rejoin capture it is already running while the DCM is still silent.

### EXP182 mailbox census

Across the four genuine DCM captures currently available, five distinct six-word `0708` response patterns were found:

- steady state: `0000 0000 0000 0000 077F 0006`;
- command pending: `0000 0001 0000 0000 077F 0006`;
- controller-boot transient: `0000 0000 0000 0000 0080 0006`;
- later controller-boot transient: `0000 0000 0000 0000 0000 0006`;
- DCM rejoin transition: `0000 0000 7FFF FFFF 0080 0007`.

The command-pending form occurred twice in the deliberate Heat Curve capture. In both cases, `word1=0001` was followed about 40 ms later by controller `FC03 03E8/count13`.

The rejoin form causes the opposite direction: the controller immediately begins an FC16 state/configuration resynchronisation beginning at `03E8`.

### Local XTR discriminator

The tested XTR M does have native `0x0F` traffic and settings/state blocks, including `03E8`, `04A6`, `085F` and the proven `0861` transport-ACK field.

However, the indexed local corpus does **not** show the reference system's complete extended runtime family:

- no native `0708/count6` scheduler;
- no confirmed native cyclic `07D0..0884` runtime upload family;
- no normal A5/A4/05 service topology.

This means the missing prerequisite is now best treated as a **controller-side topology / integration / scheduler state**, not as one unknown write register.

### Physical DCM-presence remains an open activation hypothesis

The available genuine captures prove that the scheduler can continue while the DCM service itself is temporarily unavailable, but they do **not** prove that physical DCM presence was irrelevant when the controller selected that topology.

A genuine DCM also becomes visible on the Thermia display when connected, implying an explicit controller-side recognition state.

The highest-value external capture is therefore an A/B cold boot of the **same controller**:

1. cold boot with genuine DCM physically connected;
2. cold boot without the DCM.

The first bus-level difference between those two runs may expose the actual topology-enablement mechanism.

No active local `0708` response experiment should be attempted unless the local controller first emits a genuine `0F 03 0708 0006`, or a separately justified scheduler-enablement mechanism is identified.

---

## Acknowledgements

Special thanks to **Piotr Romanowski** and his [`thermia-bus-sniffer`](https://github.com/piotr-romanowski/thermia-bus-sniffer) project.

Piotr's independent work on a 2017-era **Thermia iTec Eco 8 / Danfoss DHP-AQ** installation has provided unusually valuable cross-model verification. The second unit has now independently reproduced not only several register mappings, but also the core `0x06` transport behaviour found on the XTR M.

Important cross-model contributions include:

- `0x0A:B3B1` as a genuine room-setpoint request channel when returned in the controller's own poll-response slot;
- `0x0A:B3C5` as the controller-propagated/confirmed room setpoint;
- `0x1E FC04 0x0014` as a bitfield rather than a simple enum;
- confirmation that the `0x06` Online/DCM slot is a shared DHP-AQ/iTec platform feature;
- reproduction of the slow-to-fast `0x06` polling transition after any syntactically valid accessory reply;
- reproduction of the `AFCA=0x03E8` → `0x0F:0861=16` transport ACK and its clear when AFCA returns to zero;
- observation that the fast presence cadence survives for roughly two minutes after the accessory stops answering;
- long-history evidence that the recurring `AFDC 0x20` activity is strongly related to the controller's heating-stop/heating-season condition rather than DCM login/session acceptance;
- correction of the earlier `A80C bit 0x40 = compressor` interpretation: on the Eco 8 it remains set through compressor stops and is better treated as a broader controller context bit.

This cross-model work has been especially useful for separating likely **DHP-AQ/iTec platform behaviour** from observations that may be specific to this XTR M installation.

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

- Modbus RTU-like framing
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
| `0x04` | internal Thermia component; seen in genuine Online topology | OBSERVED / OPEN |
| `0x05` | rare FC17 probe seen immediately after an A4 probe sequence in genuine Online topology | OBSERVED ONCE / OPEN |
| `0x06` | expansion/accessory FC17 interface; transport presence path | PROVEN transport, physical DCM identity OPEN |
| `0x0A` | room sensor | PROVEN |
| `0x0F` | bidirectional Online/DCM-related settings/state mailbox | STRONGLY INDICATED / direction partly PROVEN |
| `0x14` | auxiliary block, semantics largely unknown | OPEN |
| `0x1E` | outdoor-unit telemetry/control context | PROVEN |
| `0xA4` | alternate/discovery-like FC03 endpoint; briefly probed even while A5 later resumes normally | OBSERVED / OPEN |
| `0xA5` | responsive FC03 endpoint seen in genuine Online capture | OBSERVED / identity OPEN |

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

Long clean captures have been observed with no RX buffer drops and very few or zero parser resyncs.

---

# 4. Slave `0x0A` – room sensor path

The controller periodically sends FC17/FC23-style combined read/write traffic to the room sensor:

```text
0A 17
read  B3B0 count 3
write B3C4 count 3
```

## Known registers

| Register | Direction | Meaning | Status |
|---|---|---|---|
| `B3B0` | room sensor → controller | room temperature, tenths of °C | PROVEN |
| `B3B1` | room sensor → controller | pending/requested room setpoint | PROVEN cross-model |
| `B3B2` | room sensor → controller | unknown | OPEN |
| `B3C4` | controller → room sensor | unknown/controller data | OPEN |
| `B3C5` | controller → room sensor | propagated/confirmed room setpoint | PROVEN |
| `B3C6` | controller → room sensor | unknown; possible status carrier | OPEN |

A genuine room-sensor-originated setpoint event causes:

1. a non-zero `B3B1` request;
2. the central Thermia room-setpoint setting to update;
3. the accepted value to propagate back through `B3C5`.

Returning `B3B1=0` means **no request**; it does not clear or revert the previous setpoint.

A separate Modbus-master write directly to the physical room sensor can be ACKed by that slave without the Thermia controller adopting the value. The important semantic action is therefore the value returned **inside the controller's expected poll-response slot**, not an arbitrary independent register write.

This is a real semantic write path, but it is a **room-sensor path**, not the target Online/DCM `0x06` path.

---

# 4A. Independent iTec Eco 8 / DHP-AQ cross-check

The Eco 8 comparison now provides substantially more than a simple register cross-check.

## `0x1E FC04 0x0014` is a bitfield

Over roughly seven days / ~20,000 samples on the Eco 8, the following bits matched their associated signals in the supplied history:

| Bit | Meaning | Status |
|---|---|---|
| `0x01` | compressor running | strongly supported cross-model |
| `0x04` | outdoor fan turning | strongly supported cross-model |
| `0x08` | water flow / circulation pump | strongly supported cross-model |
| `0x10` | base/always-set state in observed normal operation | strongly supported cross-model |

This explains observed values such as:

- `16` = idle/base state;
- `24` = circulation/water-flow bit added;
- `28` = circulation + fan;
- `29` = circulation + fan + compressor.

A defrost value of `25` (`0x19`) is a plausible future expectation because the compressor and circulation path may remain active while the fan is stopped, but that value has **not yet been observed** and remains a hypothesis.

## `A80C`

The earlier interpretation of `A80C bit 0x40` as a compressor-running bit is withdrawn. On the Eco 8 it stayed set through multiple compressor stops, including a heating-stop event with compressor and fan both at zero. Treat `0x40` as a broader **normal/context** bit until better semantics are available.

`A80C bit 0x01` remains associated with a hot-water request/context.

## `A80E` / `AFDC` recurring activity

The long Eco 8 history materially changes the interpretation of the familiar `0x20` pulse train.

Piotr found that `AFDC 0 ↔ 32` activity correlates very strongly with the displayed outdoor temperature being below the configured heating-stop limit. The correlation persists even when space heating itself is disabled and only hot water is being produced. A controlled heating-stop A/B change caused the pulse train to start/stop with the threshold change.

This makes the best current interpretation:

- **not** DCM login/session state;
- **not** a generic always-on heartbeat;
- most likely a heating-availability / heating-season-conditioned periodic controller signal.

On the XTR M, EXP122 independently showed that `A80E 0x20` precedes the corresponding `AFDC 0x20` edge by about **3.7 s**, with ~17 s high time and roughly 64–65 s recurrence while active. That suggests the same underlying controller state is propagated through two layers with a stable scheduling delay.

The exact semantic label remains open.

## `AFDC=0x10`

Longer Eco 8 history shows `AFDC=16` is not simply “heating stop”. It appears in ~10-minute windows after several different events. It should currently be treated as a generic controller window/state, not a DCM NAK or a single heating-state code.

## Longer periodic routine

The Eco 8 history also shows a roughly **25 h 33 min** recurring routine:

- `A80C` enters a state with bits `0x30` set for about one minute;
- when that ends, `A80E` raises bit `0x08` (values such as 8/40) for roughly ten controller-minutes (~636–645 s).

A possible explanation is the daily circulation-pump exercise described in older DHP documentation, but this is currently a **hypothesis only** and awaits direct physical confirmation.

---

# 5. Slave `0x0F` – bidirectional settings/state mailbox

The older description of `0x0F` as only a local settings/state sink is no longer sufficient.

A genuine Thermia Online/DCM capture shows both:

- FC16 writes **to** `0x0F`, carrying recurring controller/state/snapshot blocks;
- FC03 reads **from** `0x0F`, with responses carrying smaller command/desired-state mailbox blocks.

Independent work by fclauson on a related DHP-AQ/ATEC system identified the same model: the controller writes state into `0x0F`, while reading back command-side blocks from it.

A particularly important anchor is:

```text
0x0F FC03 start 0x03E8 count 13
range 0x03E8..0x03F4
```

This exact 13-register read block appears in the genuine Online capture and independently in fclauson's 0x0F map.

The recurrent controller-originated FC10/FC16 block at `0x03E8..0x03F5` still contains local settings/state, but the **same numeric range can also be used in the opposite mailbox direction when the controller issues FC03 against slave 0x0F**.



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
| `03F1` | unknown; recurrent block did not follow manual DHW START | OPEN / NEGATIVE for DHW START correlation |
| `03F2` | unknown | OPEN |
| `03F3` | unknown | OPEN |
| `03F4` | room setpoint mirror | PROVEN |
| `03F5` | unknown | OPEN |

The production parser only considers a genuine controller-originated FC10 update authoritative for settings-cache updates.

## Cooling block

EXP108–109 identified another native FC10 block:

```text
start 0x0442
count 13
range 0x0442..0x044E
```

Confirmed/strongly mapped fields include:

| Register | Meaning | Status |
|---|---|---|
| `0442` | Activate Cooling (`0=OFF`, `1=ON`) | PROVEN |
| `0443` | desired cooling temperature | STRONGLY INDICATED |
| `0445` | cooling-active threshold | STRONGLY INDICATED |

This block is important because `0442` is also present in the public Thermia Online DCM dump, providing the first experimentally verified **Online registerIndex → native local register** mapping on this XTR M.

---

# 6. Public Thermia Online DCM dump

A public Thermia Online debug dump from a DHP-AQ/ATEC-family system with a DCM module has been extremely useful because it exposes both human-readable register semantics and a stable `registerIndex` value.

The dump reports, among other metadata:

- connection type: `Dcm`;
- DCM version: `2.0.17`;
- firmware/program: `3.1.1`;
- `hasLinkUnit=false`;
- `linkIntegrationStatus=false` in that captured system.

The important distinction is:

- `registerId` = cloud/profile-facing identifier;
- `registerIndex` = stable numeric register index.

For at least the confirmed XTR M cases, `registerIndex` matches the local Thermia register namespace numerically.

## Writable non-computed indices in the dump

| registerIndex | Hex | Meaning |
|---:|---:|---|
| 1000 | `03E8` | Heating Curve |
| 1001 | `03E9` | Heating Minimum |
| 1002 | `03EA` | Heating Maximum |
| 1003 | `03EB` | Heat curve +5 |
| 1004 | `03EC` | Heat curve 0 |
| 1005 | `03ED` | Heat curve -5 |
| 1006 | `03EE` | Heating Stop |
| 1008 | `03F0` | Room Factor |
| 1070 | `042E` | Integral A1 |
| 1090 | `0442` | Activate Cooling |
| 1363 | `0553` | Operation Mode |
| 1369 | `0559` | Link Integration |

Dump enums include:

```text
Operation Mode (0553):
0 OFF
1 AUTO
2 COMPRESSOR
3 AUX
4 HOT_WATER

Link Integration (0559):
0 LIGHT
1 SYSTEM

Activate Cooling (0442):
0 OFF
1 ON
```

## Why the dump matters

The `0442` mapping has been independently verified on the XTR M bus: toggling **Activate Cooling** on the Thermia UI changes the native `0x0F:0442` value exactly as the Online dump predicts.

This strongly supports the idea that at least part of the Online `registerIndex` namespace is the native controller register namespace, while the DCM still performs a separate application/session translation before those values reach the local bus.

EXP119 specifically watched for `0553` and `0559` during a complete cold boot and saw neither. Therefore they are not ordinary boot broadcasts on this XTR M.

---

# 7. Danfoss Link / HE firmware research

Old Danfoss Link CC firmware was unpacked and inspected. This recovered the **host-side DHP/HE parameter model**, but not the final DCM03 → Thermia RS485 serializer.

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

Additional DHP parameters include `0x030A OperationMode`, `0x0334 OutdoorTemperature`, operation-time/error/alarm fields and room-sensor operation parameters.

## HE Set/Get request format

Recovered request construction:

```text
BYTE endpoint
BYTE counts
WORD SET_ID[SET_count]
WORD GET_ID[GET_count]
SET values...
```

`counts` uses the high nibble for GET count and low nibble for SET count.

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

## Integration mode and initial sync

`0x4414 IntegrationMode` is especially important:

- `0` = light/non-system integration;
- non-zero = system integration.

The parameter is configured GET-on-sync and SET-on-sync. When IntegrationMode updates, the Link firmware raises an **internal** `SystemIntegrationInitRequest`; the next regulation pass performs `SystemIntegrationInit()` and a full sync before an internal `InitSyncDone` flag is set.

Important correction: `SystemIntegrationInitRequest` and `InitSyncDone` are internal booleans, **not wire ParameterIDs**.

Firmware also shows identity/binding concepts including physical address, `DivisionID`, `BrandID` and `ProductID` before a logical endpoint is allocated.

## Architecture conclusion

The Link firmware does **not** contain the final Thermia RS485 serialization.

Best current architecture:

```text
Thermia Online / Danfoss Link host
        ↓
HE/DHP parameter model
        ↓
identity / binding / IntegrationMode / grouped sync
        ↓
DCM03 / Connect serializer + state machine
        ↓
Thermia local 0x06 accessory bank
        ↓
controller
```

Raw HE parameter IDs must therefore not be assumed to be directly present in `AFC8..AFD3`.

---

# 8. Slave `0x06` – Online/DCM accessory slot

The controller repeatedly sends:

```text
06 17
read  AFC8 count 12
write AFDC count 5
<5 write words>
CRC
```

Therefore:

- accessory → controller: `AFC8..AFD3` (12 registers);
- controller → accessory: `AFDC..AFE0` (5 registers).

The 12 response registers behave like a fixed accessory interface, not a generic arbitrary Modbus register/value mailbox.

---

# 9. Controller → accessory registers `AFDC..AFE0`

Current interpretation:

| Register | Current meaning | Status |
|---|---|---|
| `AFDC` | controller/accessory lifecycle/status word; `0x20` activity is heating-condition-related, not DCM login | STRONGLY INDICATED |
| `AFDD` | unknown | OPEN |
| `AFDE` | unknown | OPEN |
| `AFDF` | unknown | OPEN |
| `AFE0` | propagated outdoor temperature | STRONGLY INDICATED |

`AFE0` tracks displayed/controller outdoor temperature in whole °C on both investigated units.

## `A80E` → `AFDC` propagation

EXP122 produced a long passive XTR M capture in which matching `0x20` edges repeatedly occurred as:

```text
A80E 0 -> 32
~3.7 s later
AFDC 0 -> 32
```

and the same ordering on the falling edge.

Across the visible paired transitions the delay clustered tightly around ~3.7 s, while the high pulse was ~17 s and active recurrence ~64–65 s.

The Eco 8 history adds the important semantic clue that this pulse train is strongly enabled/disabled by the heating-stop threshold. Therefore it should no longer be described as a generic DCM heartbeat; it is better treated as a **heating-condition-related periodic controller state propagated toward the accessory slot**.

---

# 10. `AFCA=03E8` request level and `0861` ACK

One of the strongest findings is the level-based handshake between:

- `0x06` response word 2 / `AFCA`;
- `0x0F:0861`.

## Proven behaviour

With the accessory in the correct fast-poll phase:

```text
AFCA = 0000     # REQ low
AFCA = 03E8     # REQ asserted
```

causes:

```text
0x0F:0861 = 16
```

When AFCA is returned to zero while the remaining payload is kept stable, `0861` returns to zero.

Canonical four-phase transaction:

```text
1. payload stable, REQ=0
2. AFCA 0000 -> 03E8
3. controller ACK 0861 0 -> 16
4. AFCA 03E8 -> 0000, payload otherwise stable
5. controller ACK 0861 16 -> 0
6. payload may then be cleared/changed
```

**PROVEN:** this is a real transport-level REQ/ACK mechanism.

**NOT PROVEN:** semantic encoding of the other accessory words.

## Cross-model reproduction

The Eco 8 reproduces the same behaviour:

- plain zero responses move the controller from ~4.26 s polling to alternating ~0.70 / 1.44 s;
- `AFCA=03E8` makes every observed `0861` value become 16;
- returning AFCA to zero makes every observed `0861` value return to zero;
- the effect repeated in two full A/B cycles.

This is strong evidence that the transport layer is a shared DHP-AQ/iTec platform mechanism rather than an XTR M peculiarity.

## AFCA is a constant, not register 1000

Because `03E8` also equals decimal 1000 / Heating Curve in the Online register namespace, it was important to test whether AFCA might actually be a register number.

The Eco 8 test compared `03E8` against `03E9`, `03EA`, `03E7`/999 and 1234. Only `03E8` produced the `0861` ACK; none of the alternatives changed a parameter.

This strongly confirms that AFCA's `03E8` is a **transport constant/strobe value**, not a parameter address. Its numeric equality with Heating Curve index 1000 is coincidence or deliberate protocol design, but not direct addressing.

A further cross-model observation is that any non-zero AFCA value can alter the simultaneously reported AFDC pulse value (`32` appearing as `16`), even when it does not produce `0861=16`. This shows the controller notices AFCA at more than one level, but only the exact `03E8` value completes the known ACK transaction.

---

# 11. `0x06` cadence and presence timeout

Normal unserved `0x06` polling is approximately:

```text
~4.25–4.3 s
```

After any syntactically valid `0x06` response, the controller enters a fast cadence alternating roughly:

```text
SHORT      ~0.65–0.78 s
FAST-LONG  ~1.35–1.46 s
```

This can be sustained with completely inert responses.

The Eco 8 independently shows that once established, the fast cadence persists for about **two minutes after the accessory stops answering** before the controller falls back to the ~4.25 s empty-slot cadence.

Therefore the current model includes a controller-side **presence timeout/cache** of roughly two minutes.

Entering fast cadence does **not** imply semantic/session acceptance.

---

# 12. Major active hypotheses tested

## A. `03E8` as a local register pointer

**NEGATIVE.**

Nearby values do not produce the ACK, and the behaviour is phase/level dependent. `03E8` is a transport REQ constant, not a local register address.

## B. `00FF` required for ACK or online state

**NEGATIVE.**

Bare `03E8` can complete the ACK. Persistent `w0=00FF` does not establish semantic DCM state.

## C. Simple `[register,value]` or `[03E8,count,value]` commands

**NEGATIVE.**

Many layouts completed transport but did not change settings.

## D. Raw local settings image in `AFC8..AFD3`

**NEGATIVE.**

No semantic write.

## E. Raw HE Set/Get body directly in the mailbox

**NEGATIVE.**

Endpoints, byte order, shifts and grouped GET bodies were tested. No visible application response or setting mutation resulted.

EXP118 additionally tested a complete firmware-derived group-0 GET request that exactly fit the available mailbox space. It still produced only the normal transport handshake with no semantic response.

## F. Historical `00FF,1,REQ,1` envelope

**NEGATIVE as a standalone semantic format.**

Long dwell, repeated transactions, scalar payloads and raw HE bodies all failed to create a semantic change.

## G. Direct second-master writes to native slave `0x0F`

EXP110–112 tested direct/native-looking writes using the confirmed `0442` cooling block, including phase alignment to genuine native traffic.

**NEGATIVE.**

The authoritative controller block continued to publish the original value. Direct second-master `0x0F` writing is therefore parked as a control architecture.

## H. Simple local target/value in the historical `0x06` mailbox header

EXP113, EXP115 and EXP116 used the now-proven semantic target `0x0442` / value `0` in several structurally motivated placements/count interpretations.

All completed the `0861` transport transaction but all subsequent native cooling blocks remained `0442=1`.

**NEGATIVE.**

The simple historical-header + raw local `[registerIndex,value]` family is effectively exhausted.

---

# 13. Presence, commissioning and UI-recognition experiments

## EXP117 – presence-only commissioning test

A valid REQ-low `0x06` accessory image was held for ~90 s.

Result:

- fast cadence established;
- no new controller structural signature appeared;
- no AFCA/0861 transaction was initiated by the controller;
- no settings change.

**NEGATIVE:** presence alone does not trigger a visible commissioning/identity/init exchange.

## EXP123 – display detection test

The same proven presence concept was tested specifically against the Thermia UI.

Result:

- runtime presence established fast cadence;
- no DCM/Online/accessory indication appeared on the display;
- the user then rebooted the heat pump while the responder was active;
- the controller returned through a genuine cold-boot sequence and continued accepting the responder;
- still no DCM/Online indication appeared.

**STRONG NEGATIVE:** syntactic presence / fast polling is not sufficient for UI-level DCM recognition, even when present during controller restart.

## EXP124 – current test

**Prepared, not yet completed at the time of this update.**

Hypothesis: UI-level DCM/Online recognition may require not only presence, but completion of the proven four-phase `AFCA/0861` transaction.

EXP124 changes only that one variable relative to EXP123:

```text
presence stable
AFCA 0000 -> 03E8
wait 0861 0 -> 16
AFCA 03E8 -> 0000
wait 0861 16 -> 0
continue inert presence and inspect UI
```

No HE body, parameter ID, setting value or direct controller write is introduced.

---

# 14. Cold-boot lifecycle and transient native blocks

## EXP119 – Online writable-index cold-boot census

The public Online dump gave specific passive targets including `042E`, `0442`, `0553` and `0559`.

During a complete XTR M cold boot:

- known lifecycle activity occurred;
- `0442` was present in normal traffic outside the cold-boot target window;
- no native `0553` OperationMode or `0559` LinkIntegration frame appeared.

**NEGATIVE:** these Online indices are not generic cold-boot broadcasts on this unit.

## EXP120 – high-resolution cold-boot capture

Capturing from the first returned bus frame revealed a transient native block:

```text
0x0F FC10 start 0x04BA count 22
range 0x04BA..0x04CF
```

It appears repeatedly during the first few seconds after bus return, then disappears as the normal `0x04A6..0x04B2` family takes over.

A representative boot branch showed:

```text
A80F/A810 = 5
A80E 0 -> 8 -> 40
AFDC 0 -> 16
A80F/A810 5 -> 10
```

No spontaneous `0861` transaction ACK appeared.

## EXP121 – cooling ON/OFF/ON boot comparison

To determine whether `04BA..04CF` contained ordinary configuration, the known reversible `0442 Activate Cooling` setting was used in an A/B/A cold-boot comparison.

Result:

- the first `04BA` payload was byte-identical in Cooling ON, OFF and ON runs;
- therefore direct cooling-state encoding in this transient block is strongly disfavoured;
- two different boot lifecycle branches were nevertheless observed:
  - branch X: `A80E=8`, `A80F 5->50`, `AFDC` stayed 0 in the focus window;
  - branch Y: `A80E 0->8->40`, `AFDC 0->16`, `A80F/A810 5->10`.

Cooling was not a sufficient selector for the branch.

The later EXP123 restart reproduced the `A80F 5->50` branch while a valid `0x06` presence responder was already active, which further argues against interpreting `A80F=50` as simply “no accessory present”.

---

# 15. EXP122 overnight passive lifecycle capture

EXP122 ran for approximately 7.8 hours and remained completely passive.

Final summary:

```text
stateEvents=831
blockEvents=51795
resync=1
drops=0
PASSIVE_ONLY
```

The `blockEvents` count is inflated by a logger bug that re-logged identical `0x1E` blocks as changes, but the state observations are valid.

Key result:

```text
A80E 0x20 edge
        ↓ ~3.7 s
AFDC 0x20 matching edge
```

This relation repeated many times with stable timing. `A80F` remained at 10 during normal runtime even while compressor starts occurred, so `A80F=50` is not a generic compressor-start state.

Combined with the Eco 8 heating-stop history, the best current interpretation is that the `A80E/AFDC 0x20` cycle is part of a heating-condition-related controller lifecycle, not DCM application/session approval.

---

# 16. Experiment chronology

This is intentionally compact. Individual YAML/log files contain the full details.

| Experiment(s) | Main question | Result |
|---|---|---|
| EXP10–18 | Which response word triggers controller ACK? | `AFCA/word2=03E8` in correct phase is decisive |
| EXP21–28 | trailing words/selectors/counts | no semantic write |
| EXP29–50 | passive mapping / presence / controller-state work | transport and telemetry refined |
| EXP51–75 | presence, selector, scalar, register/value and persistence hypotheses | ACK/cadence effects only; no semantic write |
| EXP76B | canonical four-phase handshake | **PROVEN** |
| EXP77–83 | direct/raw HE layouts and historical-envelope variants | all negative semantically |
| EXP84–92 | passive correlations / presence variants / completed historical-envelope handshake | no semantic DCM state |
| EXP93–106 | lifecycle/state gating (`A80F`, `A80E`, `AFDC`) | state gates rejected as session criteria |
| EXP107 | 60 s stable accessory image before AFCA pulse | ACK only; no semantic state |
| EXP108 | Online dump index validation using `0442` | **POSITIVE: Online index 1090 = local 0x0442** |
| EXP109 | cooling block mapper | `0442..044E` mapped; `0442` enable confirmed |
| EXP110–112 | direct second-master native `0x0F` writes | negative |
| EXP113 | historical mailbox + confirmed `0442,value` target | transport ACK only |
| EXP114 | fail-closed transmission gate | **PROVEN** |
| EXP115 | shifted `0442` target placement | negative |
| EXP116 | declared length=2 + `[0442,0000]` | negative |
| EXP117 | presence-only commissioning/init signature | negative; fast cadence only |
| EXP118 | firmware-derived grouped HE GET | handshake only; no app response |
| EXP119 | passive cold-boot Online writable-index census | no `0553`/`0559` |
| EXP120 | exact cold-boot lifecycle capture | transient `04BA..04CF` discovered |
| EXP121 | Cooling ON/OFF/ON vs transient `04BA` | `04BA` invariant; multiple boot branches discovered |
| EXP122 | overnight passive lifecycle correlator | repeated A80E→AFDC ~3.7 s propagation |
| EXP123 | display recognition from presence | **negative**, including reboot with responder active |
| EXP124–132 | display recognition / accessory metadata / header and tail-word tests | transport/accessory semantics refined; no DCM recognition |
| EXP133–136 | passive native block census + DHW A/B tests | native block families refined; DHW tail assumptions rejected |
| EXP137–145 | 0x0F ACK-gated init/snapshot sequence | controller has persistent ACK-gated write-state machine; not sufficient for Online topology |
| EXP146–147 | genuine-shape 0x0F read probes | no response locally |
| EXP148 | 300 s passive topology watch | no A5/A4/0F-FC03 locally |
| EXP149 | one exact genuine A5 request | no response / no topology promotion |
| EXP150 | active 0x0F ACK role | no A5/A4/0F-FC03 |
| EXP151 | valid 0x06 transport presence | no A5/A4/0F-FC03 |
| EXP152 | offline genuine scheduler reconstruction | A5/A4 + 0x0F FC03 identified as genuine Online scheduler extension |
| EXP153 | cold boot with combined known 0x06 + 0x0F roles | **NEGATIVE:** transport presence at boot still insufficient |
| EXP154 | offline IntegrationMode / Link Integration reconstruction | `0x4414 IntegrationMode` ↔ `0x0559 Link Integration` strong semantic match, ownership unresolved |
| EXP155 | offline fclauson artifact + genuine-capture analysis | **POSITIVE architecture result:** 0x0F is bidirectional mailbox; FC03 03E8/count13 confirmed command-side anchor |
| EXP156 | local display Heating Curve change with genuine Online connected | **POSITIVE directional differential:** local 03E8 change produced event-driven FC16 03E8/count13 state push, with no FC03 03E8/count13 read |

---

# 17. Things that are now effectively ruled out

Do **not** repeat these without new evidence:

- treating `03E8` in AFCA as local Heating Curve register 1000;
- assuming `00FF` is required for ACK;
- assuming fast cadence means application/session acceptance;
- assuming a complete `0861` transport ACK means semantic success;
- simple `[register,value]` payloads;
- `03E8/count/value` layouts;
- arbitrary adjacent-word placement;
- raw local-settings blocks in `AFC8..AFD3`;
- raw HE parameter IDs as local Thermia mailbox data;
- endpoint/byte-swap/one-byte-shift HE variants already tested;
- historical envelope + raw HE body;
- historical envelope + scalar curve;
- persistent all-zero or `00FF` presence as an Online-state trigger;
- repeated identical canonical transactions as session establishment;
- simple AFC8 identity/sequence toggles;
- simple AFC9/AFCB count/length interpretations;
- isolated one-word activation hypotheses across `AFCC..AFD3`;
- timing the canonical transaction specifically inside `A80E/AFDC 0x20`;
- using `A80F=50` as a unique sync/session gate;
- assuming `A80C bit 0x40` means compressor running;
- treating `AFDC 0x20` as DCM login/session success;
- direct second-master writes to native `0x0F` as an equivalent substitute for controller-native writes;
- expecting plain `0x06` presence to make the DCM/Online module appear on the display.

---

# 18. Current protocol model

The model has materially changed after EXP147–155 and the genuine Online capture.

```text
1. Expansion/accessory transport on 0x06
   valid 0x06 FC17 response
   -> fast ~0.7 / ~1.4 s cadence
   -> transport presence only

2. 0x06 transaction handshake
   AFCA 0 -> 03E8 -> 0
   0x0F:0861 0 -> 16 -> 0
   -> transport transaction only

3. Genuine Online/DCM topology extension
   controller scheduler additionally uses:
   - 0xA5 FC03 primary responsive polling
   - 0xA4 FC03 alternate/discovery-like probes
   - rare 0x05 FC17 probe(s)
   - 0x0F FC03 reads
   - normal 0x0F FC16 state/snapshot writes

4. 0x0F bidirectional mailbox
   FC16 to 0x0F = controller/state/snapshot direction
   FC03 from 0x0F = command/desired-state direction
   local display setting changes can trigger asynchronous FC16 settings pushes
   using the same numeric register range as the command-side FC03 mailbox

5. DCM identity / approval / integration / grouped sync
   still unresolved
```

EXP147–153 showed that timing, 0x06 presence, 0x0F ACK behaviour and even cold-boot presence of both known transport roles are **not sufficient** to make the XTR controller add the genuine Online A5/A4/0F-FC03 scheduler.

The missing prerequisite is therefore now believed to be semantic/application-level recognition rather than simple transport presence.

The most important new anchor is the genuine `0x0F FC03 0x03E8/count13` command-mailbox read, which matches an independently reconstructed DCM mailbox block exactly.

---

# 19. Most likely architecture now

```text
Thermia Online cloud / Danfoss Link
        ↓
DCM03 / Online application state
        ↓
identity / approval / IntegrationMode / grouped sync
        ↓
┌─────────────────────────────────────────────┐
│ 0x06 expansion/accessory transport          │
│   presence + AFCA/0861 transaction layer    │
└─────────────────────────────────────────────┘
        ↓
controller scheduler recognizes Online topology
        ↓
┌─────────────────────────────────────────────┐
│ 0x0F bidirectional mailbox                  │
│   FC16 -> state/snapshot written to 0x0F    │
│   FC03 <- command/desired-state read from   │
│            0x0F                             │
└─────────────────────────────────────────────┘
        ↓
native Thermia settings/state
```

This model fits all current evidence better than the older assumption that the full semantic serializer lived directly inside `AFC8..AFD3`.

The public Online dump proves that the DCM stack knows native-looking register indices, and `0x0442 Activate Cooling` is independently verified on the XTR M.

The genuine capture plus fclauson's mailbox map now add a second major bridge: `0x0F FC03 0x03E8/count13` is a real command-side mailbox block.

`0x0559 Link Integration` remains semantically important, but current artifact evidence places register 1369 / `0x0559` inside an FC16 block written **to** slave `0x0F`. It must therefore not be treated as a proven DCM->controller activation write.

---

# 20. Next high-value work

## A. Get a longer genuine Online/DCM capture with exact action timestamps

The previous genuine Online capture was a major breakthrough. EXP156 has now added the complementary local-display direction, so the highest-value missing comparison is a timestamped Online-originated change using the same setting.

Highest-value follow-up:

1. start with the genuine DCM connected;
2. record a stable baseline;
3. change exactly one Online setting, e.g. Heating Curve `20 -> 21`;
4. record the exact action timestamp;
5. restore `21 -> 20`;
6. record the exact restore timestamp;
7. continue capturing for at least 60–90 s after restore.

This should allow a causal diff of the `0x0F FC03 0x03E8/count13` mailbox and subsequent FC16 state propagation. If an Online change produces FC03 `03E8/count13` first and a matching FC16 `03E8/count13` state push afterwards, the desired-state -> controller-state flow will be close to causally demonstrated.

## B. Reconstruct the 13-word command mailbox before more local TX

The confirmed command-side anchor is:

```text
0x0F FC03 0x03E8 count 13
```

The next analysis should compare every response word over time and correlate it with exact Online actions.

Do not perform a 13-word local mutation matrix. First identify the genuine command field and its baseline/changed/restored values from real DCM traffic.

## C. Find the scheduler activation prerequisite

On the local XTR without a genuine DCM, EXP148–153 produced no A5/A4/0F-FC03 topology even when known 0x06 and 0x0F transport roles were present and exercised.

The key question is therefore:

**what state or transaction appears immediately before the controller starts scheduling A5/A4 and 0x0F FC03 reads in a genuine Online topology?**

That prerequisite is likely more important than another guessed register write.

## D. Continue firmware-led identity/binding reconstruction

Prioritise ProductID, BrandID, DivisionID, endpoint allocation/service bind, IntegrationMode and grouped initial-sync ordering.

Do not treat internal firmware booleans such as `SystemIntegrationInitRequest` or `InitSyncDone` as literal wire fields without independent evidence.

## E. Keep `0x0559` as an observation target, not a write target

The Online dump still makes `0x0559 Link Integration` semantically important, but the current mailbox evidence places it in an FC16 state/snapshot block written to `0x0F`.

Do not issue a blind `0559=1` write unless new direction/ownership evidence appears.

---

# 20A. Genuine Thermia Online capture — major architecture update

A ~46 s capture with a real Online/DCM installation added traffic that never appears on the local XTR without a genuine DCM.

Observed counts included:

- `0xA5 FC03` — frequent responsive polling;
- `0x0F FC03` — command/mailbox reads with valid responses;
- `0x0F FC16` — recurring state/snapshot writes with ACKs;
- `0x06 FC17` — present but with no responses in this particular genuine capture;
- `0xA4 FC03` — a few tail probes, apparently fallback/discovery-like.

The recurring A5 read shapes were:

```text
A5 03 0000 count 18
A5 03 0023 count 1
A5 03 002E count 10
```

A key 0x0F command-mailbox read was:

```text
0F 03 03E8 000D
```

with a 13-word response covering `03E8..03F4`.

Two observed response images were:

```text
23,20,40,0,1,1,18,18,2,40,30,60,20
22,20,40,0,1,1,18,18,2,40,30,60,20
```

Only the first word changed between those two samples. Because the exact UI-action timestamps were not captured, this is not yet enough to identify the command field causally.

The same capture also contained the decimal-2000 FC16 family:

```text
07D0, 07E4, 07F8, 080C, 0820, 0834, 0848, 0864, 0870, 0884
```

A later controlled local-display capture (EXP156) resolved an earlier misleading `0x0858 = 21` observation: the tail of the `0x0848` block is strongly identified as RTC/date-time data. Across four samples, `0x0858` advanced as seconds (`6 -> 27 -> 48 -> 9`), `0x0859` advanced as minutes (`19 -> 20`), and `0x085A..0x085E` matched hour/day/month/year/weekday for 2026-09-25. Therefore `0x0858` should not be treated as a Heating Curve command field.

---

# 20B. fclauson 0x0F artifact analysis

The externally supplied `0F_register_value_map.xlsx` and `modbus_slave.py` materially strengthen the mailbox model.

The Python tool is a forensic logger, not a semantic slave implementation. It explicitly tracks two Unit-15 FC03 read blocks:

- 13 registers, with target position 12;
- 21 registers, with target position 13.

The spreadsheet resolves these as:

```text
1000..1012  (0x03E8..0x03F4)
1040..1060  (0x0410..0x0424)
```

The first block matches the genuine Online `03E8/count13` capture exactly.

The same spreadsheet contains an FC16 block covering decimal `1350..1369`, including:

- 1363 / `0x0553` = Operation Mode;
- 1369 / `0x0559` = Link Integration.

This places those fields in controller/state -> `0x0F` snapshot traffic in that evidence set. It is therefore unsafe to reinterpret `0x0559` as a proven external command input.

---

# 20C. EXP156 — local display setting change with genuine Online connected

EXP156 used a genuine Thermia Online/DCM-connected installation while changing Heating Curve locally on the heat-pump display.

## Hypothesis

A local display change should update controller-owned state and be pushed toward the Online/DCM mailbox with FC16, while an Online-originated desired-state command should be retrieved by the controller through FC03.

## Observed facts

Two event-driven writes to the same 13-word settings range were captured:

```text
0x0F FC16 start 0x03E8 count 13
```

The first image contained:

```text
03E8..03F4 =
23,25,40,0,1,1,18,18,2,40,30,60,21
```

The later image contained:

```text
22,25,40,0,1,1,18,18,2,40,30,60,21
```

Only `0x03E8` changed, matching the local Heating Curve change `23 -> 22`.

During this capture there was **no** `0x0F FC03 0x03E8/count13` read. The recurring `0x0F FC03` traffic remained the separate `0x0708/count6` block.

The `03E8/count13` FC16 write is not part of the ordinary ~21 s recurring snapshot carousel. It appears asynchronously and interrupts the normal sequence without resetting it. This strongly indicates a change/synchronisation push rather than periodic telemetry.

The normal FC16 carousel observed in the same capture follows the repeating family:

```text
0834 -> 0848 -> 0864 -> 0870 -> 0884 ->
07D0 -> 07E4 -> 07F8 -> 080C -> 0820 -> repeat
```

A local settings-sync event can pre-empt a normally expected `0x0F FC03 0708/count6` read, suggesting higher scheduler priority for change propagation.

## RTC/date-time identification in 0x0848

Four `0x0848` snapshots resolve the tail fields:

```text
0x0858 = seconds
0x0859 = minutes
0x085A = hour
0x085B = day
0x085C = month
0x085D = two-digit year
0x085E = weekday (Monday=0 fits 2026-09-25 -> Friday=4)
```

The seconds sequence `6 -> 27 -> 48 -> 9` with the minute rollover `19 -> 20` matches the ~21 s snapshot cadence. This rules out the earlier interpretation of `0x0858 = 21` as Heating Curve data.

## A5/A4/0x05 observations

The three recurring A5 FC03 response families remained byte-identical across the local Heating Curve change:

```text
A5 FC03 0000/count18
A5 FC03 0023/count1
A5 FC03 002E/count10
```

A4 was briefly probed with the same three shapes, after which A5 resumed normal responses. A4 should therefore be described as alternate/discovery-like rather than a terminal fallback after A5 failure.

A single `0x05 FC17` probe appeared immediately after that A4 probe sequence. Its role is unknown, but it may belong to a wider accessory/discovery sweep.

## Strong conclusions

- A local Heating Curve change is propagated as an event-driven `0x0F FC16 0x03E8/count13` state/settings push.
- The local display change does not itself cause a `0x0F FC03 0x03E8/count13` read.
- FC16 and FC03 can use the same numeric `03E8..03F4` settings structure in opposite semantic directions.
- The `0x0848` tail is RTC/date-time data, not Heating Curve command data.
- A5 does not visibly carry the changed Heating Curve value in its recurring payloads.

## Current hypothesis

The best current command-flow model is:

```text
LOCAL DISPLAY CHANGE
controller state changes
        |
        +--> FC16 03E8/count13 --> 0x0F state image

ONLINE / DCM CHANGE
0x0F desired image
        |
controller FC03 03E8/count13
        |
controller adopts value
        |
        +--> FC16 03E8/count13 --> resulting state image
```

The lower Online-command chain is still a hypothesis until a timestamped Online-originated change shows the FC03 read followed by the resulting FC16 state push.

## Remaining unknowns

- exact event that causes the controller to issue `0x0F FC03 03E8/count13`;
- exact physical owner/role of A5 and A4;
- meaning of the rare `0x05` probe;
- application-level recognition step that activates the genuine Online scheduler;
- exact command/state arbitration if Online and local display changes occur close together.

---

# 21. Safety approach

Active experiments remain deliberately narrow.

Current rules:

- one active experiment at a time;
- exact expected `0x06` poll signature only;
- fail closed;
- compressor/outdoor-unit guards where relevant;
- abort on parser/RX corruption;
- no direct writes to unknown controller registers;
- no broad Modbus register scanning while operating;
- no uncontrolled register-write sweeps;
- keep production control on the known SG Ready interface until a semantic native write path is proven.

For normal operation, the preferred configuration remains **receive-only**.

---

# 22. Current practical control fallback

The heat pump supports **Smart Grid Ready** inputs.

These remain the safest known external production-control interface and can be driven with isolated relay/Shelly hardware while native bus control remains under investigation.

---

# 23. Contributions wanted

If you are researching the same Thermia/Danfoss platform, especially useful contributions include:

- a real Thermia Online / DCM03 / Thermia Connect bus capture;
- first boot/commissioning traffic from a genuine module;
- register traces during official Online setting changes;
- DCM03/Connect firmware dumps;
- PCB photos and MCU/debug-pad markings;
- service/factory software or protocol packages;
- official installation/service material;
- captures from another DHP-AQ/iTec generation;
- confirmed meanings for remaining `AFC8..AFD3` words;
- confirmed meanings for `AFDD..AFDF`;
- further `0x1E:0014` state-bit correlations.

Please include:

- heat-pump model;
- controller generation;
- DCM/Online/Connect hardware model if present;
- bus speed/parity;
- exact frame bytes;
- timing between frames;
- what was changed on the heat pump at that moment.

---

# 24. Short version

```text
RS485 = Modbus RTU-like 9600 8E1

0x0A = room sensor
0x0F = bidirectional Online/DCM-related settings/state mailbox
0x06 = expansion/accessory transport interface

0x06 controller poll:
  reads  AFC8..AFD3 (12 words) from accessory
  writes AFDC..AFE0 (5 words) to accessory

valid 0x06 response
  -> fast ~0.7 / ~1.4 s cadence
  -> cadence persists ~2 min after accessory disappears

AFCA 0000 -> 03E8 -> 0000
0861 0000 -> 0010 -> 0000
  = proven transport transaction
```

Cross-model Eco 8 testing reproduces both the cadence and the AFCA/0861 handshake.

The public Thermia Online DCM dump exposes writable native-looking indices including:

```text
03E8..03EE heating family
03F0        room factor
042E        Integral A1
0442        Activate Cooling
0553        Operation Mode
0559        Link Integration
```

`0442` has been independently verified on the XTR M as a genuine native local mapping.

But:

```text
valid response != semantic session
fast cadence    != semantic session
transport ACK   != semantic command success
A80E/AFDC 0x20  != DCM login proof
A80F=50         != unique DCM sync gate
plain presence  != UI-level DCM recognition
```

The remaining challenge is the **DCM/Connect discovery / binding / service-availability prerequisite that makes the genuine `0x0F` mailbox and A5 service operational**. EXP166–167 show that valid `0x06` accessory/version presence — even sustained for 600 s — is not sufficient.

The most valuable next work is **offline transmitter/ownership analysis of the existing genuine DCM power-up/reconnect captures**, especially the first second before the earliest successful `0x0F` ACK and first A5 request. Additional reboot captures should only be requested if a specific later hypothesis cannot be resolved from the existing data.

---

# 25. EXP133-136 update

## EXP133 — passive native 0x0F block census — COMPLETE

Hypothesis: the XTR uses stable native slave-`0x0F` block families beyond the already-known `03E8` settings block.

Observed on the XTR M while strictly passive / DE LOW:

- recurrent FC10 block `04A6..04B2` (13 words);
- recurrent FC10 block `085F..0863` (5 words);
- `0861` is the third word of that native five-word block;
- no parser resyncs or RX drops in the completed capture.

Strong conclusion: `0861` is a field in a native controller block, and native `0x0F` traffic consists of multiple block families rather than one flat continuously emitted register map.

## EXP134 — passive DHW START correlation — PROCEDURAL / INCIDENTAL

The run did not produce a valid DHW A/B/A correlation. The only observed word change was `03E8 34 -> 35`, tracking Heating Curve. It therefore added another local confirmation of `03E8 = Heating Curve` but did not map DHW START.

## EXP135 — passive DHW START A/B/A — COMPLETE / NEGATIVE FOR 03F1

Hypothesis: changing only `SERVICE -> WARMWATER -> START` by exactly 1 °C would produce a reversible native `0x0F` word change, with `03F1` and external candidate `041D` treated only as candidates.

Observed:

- valid baseline/change/restore procedure;
- recurrent `03E8..03F5` block remained unchanged;
- `03F1` remained `40`;
- no block covering `041D` was observed during the run.

Conclusion:

- the previous `03F1 = Hot Water Start` interpretation is **not supported on this XTR M** and is downgraded to OPEN;
- `041D` remains OPEN because the relevant native block was not observed.

## EXP136 — passive DHW COMFORT/ECO mode A/B/A — COMPLETE / NEGATIVE

Hypothesis: changing only DHW mode `COMFORT <-> ECO` would alter one of the unknown words `03F2`, `03F3`, or `03F5`.

Observed:

- the physical Thermia setting was genuinely changed and restored;
- valid CHANGED and RESTORED phases;
- 127 native `0x0F` FC10 writes observed across two shapes;
- `wordChanges=0`;
- `03F2`, `03F3`, and `03F5` did not change;
- parser resync and RX-drop deltas remained zero.

Strong conclusion: DHW COMFORT/ECO mode is **not reflected in the recurrent `03E8..03F5` block** on the tested XTR M.

Combined with EXP135, this materially weakens the old assumption that the tail of `03E8..03F5` is a DHW-settings family. The safest current interpretation is that `03F1`, `03F2`, `03F3`, and `03F5` remain unknown until independently correlated.

---

# 26. v27 shared-build policy

The shared v27 YAML files remain strictly receive-only:

- `thermia_itec_xtr_m_waveshare_public_v27.yaml` — optimized normal Home Assistant use;
- `thermia_itec_xtr_m_waveshare_research_v27.yaml` — passive register mapping and diagnostics.

v26 remains available as a historical/reference snapshot.

v27 does **not** add active write experiments. It updates the protocol model to distinguish:

1. accessory presence;
2. AFCA/0861 transaction transport;
3. unresolved identity/binding/integration/initial-sync state;
4. unresolved semantic parameter serializer.


---

# 27. EXP137–155 update

## Observed facts

- ACK-gated 0x0F FC16 state persists across ESP restarts and resumes from the expected next block.
- Genuine Online topology adds A5/A4 FC03 traffic and 0x0F FC03 reads.
- Local XTR transport presence, including cold-boot presence of known 0x06 and 0x0F roles, does not reproduce that topology.
- A genuine Online FC03 read of 0x0F:03E8/count13 matches an independently reconstructed DCM mailbox block.
- External artifact analysis places 0x0559 Link Integration inside an FC16 write block to 0x0F.

## Strong conclusions

- Transport presence is not the missing DCM-recognition criterion.
- 0x0F is bidirectional in Online topology.
- FC16-to-0x0F and FC03-from-0x0F should be treated as different semantic directions.
- Blind direct writes to 0x0559 are not justified by current evidence.

## Hypotheses

- A semantic approval/binding/integration state enables the expanded A5/A4/0x0F-FC03 scheduler.
- The 03E8/count13 FC03 response is a desired-state/command image, at least partly mirroring known controller settings.

## Unknowns

- exact physical owner of A5/A4;
- exact serializer that populates the 0x0F FC03 mailbox;
- which 03E8/count13 word carries each Online command;
- exact prerequisite that activates the scheduler;
- whether IntegrationMode is mirrored, derived, or actively controlled through another path.


---

# 28. EXP156 update

## Observed facts

- With genuine Thermia Online connected, changing Heating Curve locally on the heat-pump display produced an asynchronous `0x0F FC16 0x03E8/count13` settings push.
- Two captured images differed only at `0x03E8`: `23 -> 22`; all other 12 words remained identical.
- No `0x0F FC03 0x03E8/count13` read occurred during the local display change.
- The recurrent FC03 traffic remained `0x0708/count6`.
- The recurring `0x0848` tail resolves as RTC/date-time data: seconds, minutes, hour, day, month, two-digit year, weekday.
- A5 recurring payloads remained byte-identical through the setting change.
- A4 was briefly probed and A5 subsequently resumed, so A4 is not simply a terminal fallback.
- One `0x05 FC17` probe appeared directly after the A4 sequence.

## Strong conclusions

- Local settings changes propagate controller -> `0x0F` through FC16.
- `03E8/count13` FC16 is event-driven settings synchronisation, not part of the ordinary periodic snapshot carousel.
- The earlier `0x0858 = 21` Heating Curve interpretation is withdrawn; `0x0858` is strongly identified as seconds.
- The same `03E8..03F4` structure is now directly observed as a controller-originated FC16 state image and independently observed as a genuine Online FC03 read block.

## Hypotheses

- Online-originated commands populate the `0x0F` desired-state image and are retrieved through FC03 `03E8/count13`.
- After adoption, the controller publishes the resulting state back through FC16 `03E8/count13`.
- A4/0x05 may participate in periodic discovery/enumeration rather than failure recovery.

## Unknowns

- causal Online FC03 -> controller adoption -> FC16 state sequence still needs one timestamped Online A/B/A capture;
- DCM recognition / scheduler-activation prerequisite remains unresolved;
- exact A5/A4/0x05 ownership and semantics remain open.


---

# 29. EXP157–163 update

## EXP158 — cross-capture topology analysis

### Observed facts

- `A4` and `A5` use the same three FC03 register shapes: `0000/count18`, `0023/count1`, and `002E/count10`.
- Genuine captures structurally pair `A4 <-> 0x05` and `A5 <-> 0x06`.
- A4 can appear after A5 is already operational; it is therefore not a simple one-time precursor to A5.
- Genuine boot captures show a highly repeatable ACKed `0x0F FC16` initial-sync family, while periodic/status blocks such as `085F/count5` can interleave.

### Strong conclusions

- A5 service availability and `0x0F` mailbox readiness are related parts of the Online/DCM topology but should not be treated as the same state.
- A4 is better described as a sibling/alternate service path than as a terminal A5 fallback.

## EXP159 — no-DCM cold-boot baseline — COMPLETE

### Hypothesis

A clean no-DCM cold boot should identify which apparent discovery and `0x0F` startup behaviours are generic controller behaviour rather than DCM-specific activation.

### Observed facts

- `C8 FC03 2328/count2` occurred 20 times without any DCM attached and received no response.
- The controller emitted unACKed `0x0F FC16` startup traffic, including `04BA/count22`, repeated `04A6/count13`, and periodic `085F/count5`.
- No A4, A5, `0x05`, or `0x0F FC03` traffic appeared during the 180 s run.
- The normal controller startup transitions, including the observed `A80E` and `AFDC` changes, still occurred.

### Strong conclusions

- C8 discovery and unACKed `0x0F FC16` retries are generic no-DCM startup behaviour and are not sufficient DCM/session indicators.

## EXP160 — isolated genuine A5 responder — COMPLETE / NEGATIVE

### Hypothesis

If A5 service availability alone is the missing prerequisite, answering the three exact A5 FC03 shapes with payloads copied from a genuine capture should allow the controller to enter the Online/DCM service state.

### Observed facts

Final 180 s summary:

```text
A4=0 A5=0 A5tx=0 C8=20
0F03req=0 0F03rsp=0
0F16req=248 0F16ack=0
```

The A5 responder was never invoked because the controller never issued an A5 request.

### Strong conclusion

An available A5 responder by itself does not cause the no-DCM controller to begin A5 polling.

## EXP161 — genuine-capture chronology review — OFFLINE ANALYSIS

### Observed facts

In the genuine DCM power-up capture, a successful `0x0F FC16` transaction is already visible before the first A5 triplet. A5 becomes active while unanswered C8 probes are still continuing. The genuine topology then develops recurring A5 activity, `0x06`, and `0x0F FC03` reads.

### Strong conclusions

- C8 does not need to complete or receive a visible response before genuine A5/0x0F service becomes operational.
- A4 is not a simple prerequisite that must occur before A5.
- A working `0x0F` service exists very early in genuine DCM startup, but prior experiments show that a single ACK role alone is not sufficient to cause A5 activation.

### Unknown

The exact event that makes the controller start scheduling A5 remains unidentified.

## EXP162 — combined 0x0F FC16 ACK + A5 responder — COMPLETE / NEGATIVE

### Hypothesis

The missing state may require the combination of a responsive `0x0F` mailbox and an available A5 service. EXP162 therefore ACKed only known `0x0F FC16` start/count shapes while retaining the exact A5 responder from EXP160.

### Observed facts

Final summary:

```text
EXP162 SUMMARY reason=AUTO_STOP_180S phase=3 duration_ms=180008
frames=1388 s02=344 s05=0 s06=43 s0F=49
A4=0 A5=0 A5tx=0 0FtxACK=6 C8=20
unexpectedSlaves=0
0F03req=0 0F03rsp=0
0F16req=6 0F16ack=0
resyncDelta=1 dropDelta=0
0F_ACK_PLUS_A5_ACTIVE_DE_LOW_IDLE
```

All six observed whitelisted `0x0F FC16` requests were answered by the ESP. After the ACKs, the heavy no-DCM retry behaviour stopped, but no A5 request, A4 request, `0x05` activity, or `0x0F FC03` request appeared during the complete 180 s capture. C8 again produced its 20-request discovery burst.

### Strong conclusions

- The strict `0x0F FC16` ACK implementation is operational enough to advance/suppress the controller's individual FC16 retry state.
- `0x0F FC16` ACK plus an available A5 responder is still insufficient to activate A5 polling or the genuine `0x0F FC03` scheduler.
- The no-DCM FC16 sequence being ACKed is not equivalent to the ordered full initial-sync state seen with a genuine DCM.
- The missing prerequisite occurs earlier or elsewhere in the DCM presence/binding/service-state path.

### Negative results retained

Do not repeat A5-responder-only, simple 0x0F-ACK-only, or combined ACK+A5-responder tests as though they were untested hypotheses. Do not invent a C8 response merely to force progress: genuine DCM service is already active while C8 probes continue unanswered.

## EXP163 — 0x0F ACK then exact A5 master-side FC03 probe — PROPOSED / NOT YET RUN

### Hypothesis

The A5 direction/ownership model may still be incomplete. After the known `0x0F` ACK phase, issuing the three exact A5 FC03 reads observed in genuine traffic may reveal whether A5 is an endpoint that the DCM side actively queries rather than a slave endpoint that the replacement must emulate.

### Safety / scope

- exactly the three observed FC03 read shapes only: `0000/count18`, `0023/count1`, `002E/count10`;
- no A5 writes;
- no register scan;
- existing strict known-shape `0x0F FC16` ACK behaviour only;
- C8, `0x06`, A4 and `0x05` otherwise remain passive;
- one cold-boot run, then passive observation to the 180 s summary.

This is a direction/ownership test, not evidence that A5 is already understood.

## Current model after EXP162

```text
generic controller startup
    +-- C8 discovery (parallel; not a proven gate)
    +-- no-DCM 0x0F FC16 retry path

genuine DCM service state
    +-- responsive/ACKed 0x0F mailbox
    +-- recurring A5 service
    +-- 0x06 accessory/service traffic
    +-- controller 0x0F FC03 desired-state reads
    +-- occasional A4 <-> 0x05 sibling path
```

The unresolved step is the recognition/binding/service-state transition between these two states.


---

# 30. EXP164–167 — runtime DCM activation / service-ownership update

## EXP164 — passive no-DCM cold-boot baseline — COMPLETE

### Observed facts

A clean 180 s passive no-DCM run reproduced:

- generic `C8 FC03 0x2328/count2` discovery;
- native `0x06 FC17` polling;
- controller startup transitions including `A80E 0 -> 8 -> 0x28`;
- `AFDC=0x0010`;
- sustained unACKed controller-originated `0x0F FC16` traffic;
- no A5, A4, `0x05`, or `0x0F FC03`.

### Strong conclusion

C8, `0x06` polling, A80E/AFDC startup state and unACKed `0x0F FC16` retries are all possible without a DCM. None is a sufficient DCM-recognition discriminator.

## Genuine DCM runtime power-up comparison

The genuine capture `thermia_capture_20260925_090209.log` is a DCM power-up while the heat-pump/controller is already running.

Visible chronology:

- `0x0F` is already operational and successfully ACKed at about +0.389 s;
- first A5 transaction appears at about +1.179 s;
- C8 probing continues in parallel;
- `0x06` appears later in the visible sequence.

This proves that DCM service activation does not intrinsically require a controller reboot and that the missing transition is earlier than simple `0x06` metadata presence.

## EXP165 — runtime 0x0F ACK role — COMPLETE / NEGATIVE FOR ACK-ONLY ACTIVATION

Five known controller-originated `0x0F FC16` requests were ACKed during a 180 s runtime test.

Observed:

- no A5;
- no A4 / `0x05`;
- no `0x0F FC03`.

Strong conclusion: runtime `0x0F FC16` ACK service alone is insufficient to activate the genuine DCM/Online service state.

The intended simultaneous `0x06 + 0x0F` condition was not validly tested in EXP165 because the experimental `0x06` matcher incorrectly required a 27-byte request. The native FC17 request is 23 bytes.

## EXP166 — corrected runtime 0x06 responder — COMPLETE

The request-length gate was corrected from 27 to 23 bytes.

Observed:

- 169 valid `0x06` responses in 180 s;
- `AFD1=0` caused `EXP 0.0` to appear on the VERSION page immediately at runtime;
- no controller/heat-pump reboot was required;
- no A5, A4/`0x05`, or `0x0F FC03`;
- no `0x0F FC16` occurred during the armed window.

### Strong conclusion

The `EXP / UITBR.KAART` UI entry is directly driven by the `0x06` accessory/version metadata path. A valid `0x06` response can expose this metadata dynamically at runtime, but this does not establish a DCM/Online application session.

## EXP167 — sustained runtime 0x06 presence — COMPLETE / INCONCLUSIVE COMBINED TEST; STRONG NEGATIVE FOR 0x06-DRIVEN ACTIVATION

### Hypothesis

After proven `0x06` presence, a naturally occurring known controller-originated `0x0F FC16` request would be ACKed. The combination might trigger spontaneous A5 and/or `0x0F FC03`.

### Observed facts

Final summary:

```text
EXP167 SUMMARY reason=NO_NATIVE_0F_WITHIN_600S
duration_ms=600009
frames=4715
s05=0
s06=559
s0F=0
A4=0
A5=0
06tx=559
0FtxACK=0
A5tx=0
0F03req=0
0F03rsp=0
0F16req=0
resyncDelta=0
dropDelta=0
INCONCLUSIVE_COMBINED_ROLE_NOT_EXERCISED_DE_LOW_IDLE
```

The `0x06` responder was therefore proven active for ten minutes and transmitted 559 valid replies, but the controller emitted zero `0x0F` frames of any kind.

### Strong conclusions

- Sustained valid `0x06` accessory/version presence does **not** cause the controller to start native `0x0F` service during runtime.
- It also does not cause A5, A4 or `0x05` scheduling.
- The exact combined condition `active 0x06 + actually exercised 0x0F ACK` remains technically untested because no controller-originated `0x0F FC16` appeared.
- Repeating longer `0x06` dwell tests is now low-value.
- Together, EXP165–167 show that runtime `0x0F` ACK alone and runtime `0x06` presence alone each fail to reproduce the genuine DCM service topology.

## Refined architecture after EXP167

```text
0x06 accessory/version metadata path
    -> independently serviceable
    -> can expose EXP / UITBR.KAART
    -> not sufficient for DCM recognition

0x0F bidirectional mailbox/service
    -> controller FC16 attempts can exist without DCM
    -> genuine DCM topology provides an operational ACK/read service
    -> physical/logical owner remains OPEN

A5 service
    -> operational in genuine DCM topology
    -> exact owner and activation mechanism remain OPEN

A4 <-> 0x05
    -> sibling / alternate discovery-like path
    -> not a simple mandatory A5 precursor

C8
    -> generic native startup discovery
    -> not the missing DCM gate
```

## Current research direction

Do not continue using `EXP 0.0`, A80E/AFDC state, C8 probing, or longer `0x06` presence as DCM-recognition criteria.

The highest-value next step is offline analysis of the earliest genuine DCM power-up interval, especially transmitter ownership and the event/property that makes `0x0F` service available before the first A5 transaction. A new controller reboot should only be used if a later hypothesis uniquely requires one.


---

# 31. EXP168 — valid combined-role negative

EXP168 closed the exact gap left by EXP167.

With the proven runtime `0x06` responder already active, Heat Curve was changed by +1 on the Thermia display. The controller emitted the expected exact `0x0F FC16 0x03E8/count14` event, first word `36 / 0x0024`. The ESP ACKed that request once and then observed 120 s.

Final result:

```text
s06=155
06tx=155
s0F=1
0F16req=1
0FtxACK=1
A5=0
A4=0
s05=0
0F03req=0
0F03rsp=0
resyncDelta=0
dropDelta=0
```

**Strong conclusion:** active `0x06` accessory/version presence plus a working runtime `0x0F` ACK-side role is not sufficient to activate the genuine Online/DCM A5 or FC03 scheduler.

Together with EXP165–167, this exhausts the simple known transport-role combinations as the missing DCM-recognition mechanism.

**Current direction:** focus on offline transmitter ownership / discovery / binding / service-availability analysis of the earliest genuine DCM power-up interval before defining EXP169. No controller reboot is currently justified.


## EXP183 — offline scheduler reconstruction

EXP183 reconstructs the genuine Online/DCM runtime task without any local TX.

The runtime FC16 family is ordered and cyclic:

`07D0/19 -> 07E4/17 -> 07F8/17 -> 080C/18 -> 0820/18 -> 0834/18 -> 0848/23 -> 0864/4 -> 0870/17 -> 0884/60 -> repeat`.

Typical slot spacing is about 2.1 s. The `0708/count6` mailbox poll runs at about 4.2 s and is interleaved with this stream.

A key state-machine result comes from the DCM-rejoin capture: while the DCM is silent, the controller repeatedly retransmits the same pending `0870/count17` block instead of advancing through the cycle, while `0708` polling continues. This demonstrates ACK-gated runtime export with a partially independent mailbox cadence.

Payload reconstruction shows that the runtime family is a **state-export serializer** rather than a set of independent control registers:

- `07D0/19` repacks the normal `0x02 FC17 A7F8/A80C` controller transaction. The 13 FC17 response words are exported with unavailable `FC18` values normalized to `FF9C`, followed by the first six controller write-image words.
- `0820/18` strongly repacks A5 data: the leading fields follow `A5 0000/count18`, while its final six words match words 4..9 of `A5 002E/count10` in the checked captures.
- `07E4/17` strongly tracks the reference slave `0x04 FC17` exchange, including the same unavailable-value normalization, though some fields are transformed and remain unmapped.

This materially strengthens the current architecture: A5 is upstream data consumed by the DCM-facing export image, and the local XTR is missing activation of an entire export topology/task rather than one command register.

No active EXP184 is defined yet. The same-controller cold-boot A/B capture with and without a genuine DCM remains the highest-value next discriminator.


## EXP184–185 — current offline result

Raw Danfoss Link CC 2.7.42 firmware is now available in the project corpus and has been inspected directly rather than relying only on prior summaries.

The exact HPNode partial-update groups are now reconstructed:

- group 0: identity/mode/integration/room/external-control/alarm state;
- group 1: HeatCurve family plus HeatStop, RoomFactor, HotWaterStart, ControllerDemand and OperationStatus;
- group 2: temperatures, auxiliary-heater stage and EVU state.

The most important new correlation is that genuine DCM mailbox `0708 word1=1` triggers an immediate `03E8/count13` fetch, while firmware partial-update group **1** starts with HeatCurve. This makes a group-dirty/group-selector interpretation of the mailbox substantially more plausible, but only word1 has been observed in a command state so far.

IntegrationMode itself is no longer the leading scheduler-enable candidate. In recovered RegulationEngine code it is an application synchronization/ownership mode, persisted via the HPNode `SystemIntegration` setting and factory defaults. A change causes a full grouped resync, but no direct service-bind-to-IntegrationMode enable path was found.

**Current unresolved gate:** what makes the controller instantiate/enable the extended A5/A4/05 + `0708` + `07D0..0884` export topology.

**Highest-value next evidence remains:** same-controller cold boot with genuine DCM connected versus physically absent. No new active local write experiment is currently justified.


## Status through EXP193

Offline reconstruction now shows the DCM runtime range as a semantic export database rather than a raw mirror of internal Modbus slaves. Confirmed/strong mappings include: 07D0 from controller 0x02 state, 07E4 from reference outside-unit 0x04 state, 07F8 from the controller/room-environment path, 080C containing 0x06 accessory lifecycle state (word14 tracks AFDC), 0820 from A5 data, 0848 current RTC/date, and 0884 the ten-entry alarm-history table. 0834, 0864 and 0870 remain semantically unresolved.

The raw-slave-ID interpretation of `080C word0=00C8` and `0834 word0=001E` is rejected: those blocks exist when corresponding C8/0x1E source traffic is absent. No active local write follows from these findings. The highest-value scheduler-gate evidence remains a same-reference-controller cold-boot A/B with genuine DCM physically present versus absent.


## Status through EXP194

The runtime database mapping has improved materially. `0870/count17` is now strongly identified as Thermia Online registerIndex 2160..2176: compressor/heating/cooling/hot-water/auxiliary operating times plus defrost statistics. It is therefore removed from the scheduler-gate/identity candidate set.

`0864/count4` remains unresolved. It maps to native indices 2148..2151, is invariant as `[0,0,0,22]`, and begins immediately after the local/native `085F..0863` service block containing 0861. Public Online profiles checked do not expose 2148..2151. This makes 0864 a passive topology/capability candidate worth comparing in future same-controller DCM-present/absent data, but not a justified write target.

No YAML or production functionality changed.



## Post-EXP194 architecture and next step

The extended Online/DCM scheduler is now most consistently modeled as a controller-side publisher of the Thermia Online native `registerIndex` database into slave `0x0F`. The cyclic FC16 block starts align directly with decimal Online index families: 2000, 2020, 2040, 2060, 2080, 2100, 2120, 2143, 2148, 2160 and 2180.

This materially narrows the scheduler-gate problem:
- runtime FC16 pages such as `0864` and `0870` are **exported consequences** of the active topology;
- they should not be treated as obvious ingress controls;
- the activation mechanism must lie upstream of this publisher.

`0870/count17` is now strongly identified as operating-time + defrost statistics and is removed from the identity/gate candidate set.

`0864/count4` remains unresolved at indices 2148..2151 with invariant payload `[0,0,0,22]`. Because it directly follows local/native `085F/count5` (2143..2147, containing 0861), the next useful offline task is to analyze 2143..2151 as one service/status family.

**EXP195 is proposed, not started.** It is offline/passive only and introduces no YAML, TX, or production changes.



## Status through EXP195

EXP195 separates the adjacent 2143..2151 area into two scheduler roles.

`085F/count5` (2143..2147) is now best classified as an initialization/synchronization/service-control page. It exists locally without DCM, contains the proven 0861 AFCA transaction ACK, disappears from steady genuine Online cycles, and repeats at ~4.2 s during the genuine DCM full-resync phase.

`0864/count4` (2148..2151) is a steady extended-runtime Online export page. Its observed payload remains `[0,0,0,22]`.

This is a material negative for the scheduler-gate search: full DCM resync starts before the first 085F page after rejoin, and 0864 appears only later as runtime output. Neither range is a justified activation write target.

No active local write experiment is justified. The decisive missing evidence remains a same-controller clean cold boot with a genuine DCM physically present versus absent.

