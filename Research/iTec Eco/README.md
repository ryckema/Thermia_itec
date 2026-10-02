# Thermia iTec Eco — active write research

> [!WARNING]
> This folder contains **active RS485 experiments** for the legacy/non-Genesis Thermia iTec Eco / Danfoss DHP-AQ family. These files can transmit on the internal Thermia bus. They are not production write builds.

The passive compatibility profile remains:

`Read-only/iTec Eco/thermia_itec_eco_waveshare_public_v01.yaml`

The current active Eco experiment is:

`thermia_itec_eco_waveshare_write_exp01.yaml`

## ECO-WRITE-01 — PREPARED / NOT RUN

### Hypothesis

A single genuine iTec Eco 5 Thermia Online gateway response, replayed once against the first exact `0x0F` cold-start `071C/0730` challenge, may be sufficient for an iTec Eco controller to enter the native Online/DCM synchronization path.

This is deliberately narrower than the XTR M Write Beta. It does **not** yet attempt a setting change.

### Baseline

`Read-only/iTec Eco/thermia_itec_eco_waveshare_public_v01.yaml`

The passive decoder and normal Home Assistant monitoring remain intact.

### Exact controlled change

Only the following active behavior is added:

1. GPIO17 TX is configured.
2. A Home Assistant **Configuration** button manually arms ECO-WRITE-01.
3. The ESP waits for at least **5 seconds of complete bus silence** and then for the controller to return.
4. It waits for the exact native challenge shape:
   - slave `0x0F`
   - FC17 / `0x17`
   - read `0x0730`, count 8
   - write `0x071C`, count 8
   - byte count 16
5. On the first qualifying challenge it transmits exactly **one** captured gateway response.
6. It then returns to observation only.

The experiment does **not** ACK the following FC16 configuration page, does not answer `0708`, does not send a desired-page selector, and does not modify any heating, hot-water, cooling or operation setting.

### Transmitted payload

The single response frame is:

```text
0F 17 10 16 91 A5 F3 F8 E8 D5 87 38 92 44 16 E8 E6 A3 D5 E2 27
```

Response body:

```text
1691A5F3F8E8D58738924416E8E6A3D5
```

CRC bytes:

```text
E2 27
```

The calculated Modbus CRC value is `0x27E2`.

### Evidence source

The response body comes from a **genuine iTec Eco 5 + Thermia Online gateway capture**.

Cross-model XTR M work showed that this recorded response can be accepted against a different live challenge and can open the native synchronization path on that XTR M. That does **not** prove the same behavior on an iTec Eco 8 or another Eco controller; ECO-WRITE-01 exists specifically to test that compatibility.

Passive Eco 8 evidence already shows that an unpaired controller emits the same `071C/0730` challenge family during cold start, but the Eco 8 challenge payloads vary and its challenge window is shorter than on the tested XTR M.

## Success, negative and abort criteria

**COMPLETE / POSITIVE**

After the one R1 replay, the controller sends:

```text
slave 0x0F
FC16
start 0x03E8
count 14
byte_count 28
```

That first configuration page is enough to prove session-entry compatibility for this experiment. The ESP intentionally does **not** ACK it.

**COMPLETE / NEGATIVE**

- no `03E8/count14` FC16 appears within 10 seconds after R1; or
- only challenge retries continue.

**COMPLETE / INCONCLUSIVE**

The experiment was armed but no qualified silence → controller-return → challenge sequence occurred within 180 seconds.

**ABORT**

- another response-shaped `0x0F FC17` peer is observed;
- another `0x0F FC16` ACK-shaped peer response is observed;
- CRC, stream-resync or RX-drop integrity changes after controller return and before completion;
- the user presses Cancel.

Unexpected traffic that is not part of the explicit criterion is capture-only.

## Safety and recovery

The experiment has several hard guards:

- manual arm is required;
- a real controller-off interval of at least 5 seconds is required;
- exactly one R1 is allowed per ESP boot;
- the one-shot latch is closed **before** driver enable;
- DE is LOW outside the guarded response;
- no FC16 ACK is transmitted;
- no semantic page/write transaction exists in this build;
- another apparent `0x0F` responder aborts the experiment;
- parser CRC/resync/RX-drop changes abort the active observation window.

Plausible unintended effects are a temporary partial Online/DCM session, repeated `03E8` configuration writes from the controller, or an Online communication alarm because this experiment deliberately stops after proving entry into the sync path.

Recovery is therefore passive: the ESP sends nothing else. Use the Cancel button if still armed, or flash the read-only Eco profile. If the Thermia controller does not naturally leave the partial session, use its normal controller restart procedure. Do not add speculative ACKs or setting writes to recover it.

## How to run ECO-WRITE-01

1. Flash the experimental YAML.
2. Verify normal passive sensor updates first.
3. Open the ESPHome log.
4. In Home Assistant, press **ECO-WRITE-01 | Arm Session Bootstrap Test** under Configuration.
5. Power-cycle the Thermia controller using the normal procedure while keeping the ESP powered.
6. Do not change any Thermia setting during the run.
7. Wait for a terminal `COMPLETE`, `ABORTED`, or `INCONCLUSIVE` marker.
8. Return the complete log from:
   - `[ECO-WRITE-01] ===== ARM ACCEPTED`
   through
   - the terminal ECO-WRITE-01 marker,
   plus roughly 10–20 seconds of following passive traffic if available.

Do **not** run it a second time in the same ESP boot. The YAML refuses a second active replay until the ESP has rebooted.

## What comes next

Do not advance merely because this YAML exists.

If ECO-WRITE-01 is **COMPLETE / POSITIVE**, the next controlled experiment should add only the known initial FC16 ACK chain and test whether the Eco controller completes the genuine Online synchronization sequence.

Only after session synchronization is locally confirmed should an Eco experiment expose a semantic setting write. The preferred first semantic target is `03F4` Room Setpoint because its meaning is independently established on both the XTR M and iTec Eco family and it provides a conservative cross-check before testing settings that lack another known control path.

## Validation status

Static checks performed when the file was created:

- all `id(...)` references resolve;
- all substitutions resolve;
- GPIO17 TX exists only in the active experiment;
- the hard-coded R1 frame has a valid Modbus CRC;
- there is no FC16 ACK path in ECO-WRITE-01;
- there is no semantic settings-write control.

**ESPHome compile verification has not been performed.**
