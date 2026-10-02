# Thermia iTec Eco — active write research

> [!WARNING]
> This folder contains **active RS485 experiments** for the legacy/non-Genesis Thermia iTec Eco / Danfoss DHP-AQ family. These files can transmit on the internal Thermia bus. They are not production write builds.

Passive baseline:

`Read-only/iTec Eco/thermia_itec_eco_waveshare_public_v01.yaml`

Current active experiment:

`thermia_itec_eco_waveshare_write_exp01.yaml`

Combined genuine gateway evidence:

`ECO5_GATEWAY_CAPTURE_EVIDENCE.md`

## Current status

**ECO-WRITE-01 — PREPARED / NOT RUN**

No iTec Eco active result has been supplied yet. Generating or updating the YAML does not count as experiment completion.

## What is already established from genuine Eco5 logs

Re-analysis of both genuine iTec Eco 5 + Thermia Online captures found **six successful approval responses**.

All six have the same architecture:

`071C/0730 challenge -> gateway FC17 response -> controller FC16 03E8/count14`

Observed first-`03E8` delay after the gateway response is **92–482 ms**.

The successful gateway response occurred:

- on challenge **#29** in four captured sessions;
- on challenge **#3** in two captured sessions.

The six challenge bodies and six response bodies differ. Therefore the captures directly establish the Eco5 approval/synchronization architecture, but do **not** establish a constant response or the native challenge-response derivation.

The captures also directly establish the downstream ACK behavior. When `03E8/count14` is immediately ACKed, the controller proceeds into:

`03E8/14 -> ACK -> 03FC/11 -> ACK -> 0410/22 -> ACK -> 042E/15 -> ...`

In two captured challenge-#3 sessions without an immediate `03E8` ACK, the controller retransmitted `03E8/count14` nine times within the next 10 seconds and did not progress to `03FC` during that window.

So the ACK chain is **not** the main unknown for Eco anymore.

## Remaining question

The key unresolved prerequisite is now:

> **Will an iTec Eco controller accept a known-good Eco5 gateway response replayed against a different current challenge?**

That behavior is already locally proven on the XTR M: the captured Eco5 response body `1691A5F3F8E8D58738924416E8E6A3D5` was accepted there against a non-matching live challenge.

That XTR result is important cross-model evidence, but it is **not** proof of Eco replay tolerance.

## ECO-WRITE-01 hypothesis

An iTec Eco controller accepts the known-good captured Eco5 R1 even though it does not correspond to the current live challenge.

### Why challenge #3

The earlier draft answered the first challenge. The raw Eco5 captures do not support that choice: no successful gateway response occurs on challenge #1.

Challenge #3 is now used because a genuine Eco5 gateway successfully responded at challenge #3 in **two** captured sessions. Challenges #1 and #2 are therefore capture-only.

The replay body used by ECO-WRITE-01 came from a different challenge/session — a #29 response — so the experiment explicitly tests **mismatched replay acceptance**.

## Exact controlled change

Relative to the passive Eco build, only this active behavior is added:

1. GPIO17 TX is configured.
2. A Home Assistant **Configuration** button manually arms ECO-WRITE-01.
3. The ESP requires at least **5 seconds of complete controller-bus silence** followed by controller return.
4. It recognizes the exact native `0x0F FC17` challenge shape:
   - read `0x0730`, count 8;
   - write `0x071C`, count 8;
   - byte count 16.
5. Exact challenge #1: capture only, **NO TX**.
6. Exact challenge #2: capture only, **NO TX**.
7. Exact challenge #3: transmit exactly one captured known-good Eco5 gateway response.
8. Return to observation only.

There is:

- no FC16 ACK;
- no `0708` reply;
- no desired-page selector;
- no heating/DHW/cooling/operation setting write.

## Transmitted payload

Exactly one active frame is permitted per ESP boot:

```text
0F 17 10 16 91 A5 F3 F8 E8 D5 87 38 92 44 16 E8 E6 A3 D5 E2 27
```

Body:

```text
1691A5F3F8E8D58738924416E8E6A3D5
```

CRC bytes are `E2 27`; calculated Modbus CRC value is `0x27E2`.

## Result criteria

**COMPLETE / POSITIVE**

Challenge #3 is reached, the one R1 replay is transmitted, and the controller then sends:

```text
slave 0x0F
FC16
start 0x03E8
count 14
byte_count 28
```

That is enough for EXP01. The controller page is intentionally **not ACKed**.

**COMPLETE / NEGATIVE**

Challenge #3 is reached and R1 is transmitted, but no `03E8/count14` appears within 10 seconds.

**COMPLETE / INCONCLUSIVE**

- the controller returns but challenge #3 is not reached within 30 seconds; or
- no qualified silence -> boot-return sequence occurs inside the arm window.

**ABORT**

- another response-shaped `0x0F FC17` peer appears;
- another `0x0F FC16` ACK-shaped responder appears;
- CRC/resync/RX-drop integrity changes after controller return;
- the user presses Cancel.

Unexpected traffic is capture-only.

## Safety and recovery

- manual arm required;
- real >=5 s controller-bus silence required;
- one R1 maximum per ESP boot;
- one-shot latch closes before DE rises;
- DE is LOW outside that one frame;
- no setting register is modified;
- no FC16 ACK or semantic page transaction exists in EXP01;
- peer responder or parser-integrity changes abort;
- no automatic retry.

Plausible unintended effects are a temporary partial Online/DCM session, repeated `03E8` pushes, or an Online communication alarm because EXP01 deliberately stops before ACKing the first configuration page.

Recovery is passive: the ESP sends nothing else. Cancel if still armed or flash the read-only Eco profile. If the controller does not naturally leave the partial session, use only its normal controller restart procedure.

## How to run

1. Flash `thermia_itec_eco_waveshare_write_exp01.yaml`.
2. Verify normal passive sensor updates.
3. Open the ESPHome log.
4. Press **ECO-WRITE-01 | Arm Session Bootstrap Test** under Configuration.
5. Power-cycle the Thermia controller while keeping the ESP powered.
6. Do not change any Thermia setting during the run.
7. Wait for a terminal ECO-WRITE-01 marker.
8. Return the log from `ARM ACCEPTED` through the terminal marker, plus roughly 10–20 seconds of following passive traffic if available.

The build refuses a second active replay in the same ESP boot.

## Next experiment

Do not advance before an ECO-WRITE-01 result is supplied.

If ECO-WRITE-01 is **COMPLETE / POSITIVE**, the next controlled step can reuse the **already genuine-Eco5-proven** initial FC16 address/count ACK sequence. That experiment should still add ACK stages incrementally and stop on any page/count divergence.

Only after local Eco session synchronization is confirmed should a semantic setting write be exposed. `03F4` Room Setpoint remains the preferred first semantic target because its meaning is independently established across the XTR M and iTec Eco evidence.

## Validation status

After this revision:

- all YAML `id(...)` references resolve;
- all substitutions resolve;
- exactly one `write_array()` TX call remains;
- the R1 hard-coded frame CRC validates;
- there is no FC16 ACK path;
- there is no semantic settings-write control;
- challenge #1 and #2 are capture-only;
- only exact challenge #3 can use the one-shot R1 latch.

**ESPHome compile verification has not been performed.**
