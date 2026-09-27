# EXP257 — ONE-SHOT R1 + SINGLE `03E8/count14` ACK + NEXT-STAGE CAPTURE

Status: **PREPARED / NOT RUN**

## Hypothesis

EXP256 proved that one exact R1 response terminates the local `071C/0730` approval retry loop and immediately moves the XTR controller into the native `0x0F FC16 03E8/count14` synchronization stage.

EXP257 tests one new variable only: after the same one-shot R1, acknowledge exactly the **first post-R1 `03E8/count14` FC16 request once**. If that block is the first acknowledged sync stage, the controller should advance to a different FC16 or FC03 stage.

The complete genuine Eco 5 capture now predicts `03FC/count11` as the immediate next stage after the `03E8/count14` ACK in two independent successful approval cycles. Prior local EXP137 had observed `0410/count22` after a `03E8` ACK, but did not prove it was the first intervening block. EXP257 will not ACK either `03FC` or `0410`.

## Exact active frames

### R1 — already tested in EXP252 and EXP256

Payload:

`1691 A5F3 F8E8 D587 3892 4416 E8E6 A3D5`

Exact response frame:

`0F 17 10 1691A5F3F8E8D58738924416E8E6A3D5 E227`

### New EXP257 target — one FC16 ACK only

The controller request must be exactly:

- slave: `0x0F`
- function: `0x10` / FC16
- start: `0x03E8`
- count: `14` (`0x000E`)
- bytecount: `28` (`0x1C`)
- full request length: `37` bytes
- and it must be the **first FC16 request after R1**.

The single response is the standard Modbus FC16 ACK, which echoes only start/count and contains **no register-value payload**:

`0F 10 03 E8 00 0E C0 93`

CRC16 over `0F1003E8000E` = `0x93C0`, transmitted little-endian as `C0 93`.

## What is known about the target and possible effects

- `03E8/count14` is a native controller-originated settings/synchronization export block.
- EXP256 proved that it becomes the immediate post-R1 stage and is retransmitted indefinitely when not acknowledged.
- Complete genuine Eco 5 capture proves twice that `03E8/count14 ACK -> 03FC/count11`; after `03FC` is ACKed, `0410/count22` follows.
- Earlier EXP137 proved locally that ACKing `03E8/count14` reaches `0410/count22`, but did not rule out an intervening `03FC/count11`.
- The ACK itself does not carry a new register value; it is a transport acknowledgement.
- Advancing this incomplete Online/Link session can still lead to the known DHW-side `0` and later `COMM. ERR ONLINE/LINK` until a normal controller reboot.

## Fail-closed guards

The `03E8` ACK is sent only if all of these remain true:

1. R1 was sent exactly once on the first qualifying approval request.
2. There has been no approval retry after R1.
3. The first post-R1 FC16 request is exactly `03E8/count14`, bytecount 28, length 37.
4. That request arrives within 5 seconds of R1.
5. Parser-resync and RX-drop counters remain unchanged since BUS_RETURN.
6. No unexpected peer FC17 or FC16 ACK has been observed.
7. The ACK one-shot latch is still unused.

The ACK latch closes **before** DE is enabled.

## No downstream chain emulation

EXP257 does **not** send:

- a second `03E8` ACK;
- an ACK for `0410` or any later FC16 block;
- an FC03 response;
- a second R1/FC17 response;
- a mailbox response;
- a desired-state response.

## Procedure

1. Confirm recovery from EXP256 first: no `COMM. ERR ONLINE/LINK`, the DHW-side `0` is gone, and normal traffic has been healthy for at least 15 seconds.
2. Flash `thermia_itec_xtr_m_waveshare_exp257.yaml`.
3. In Home Assistant → **Configuration**, press **EXP257 Arm R1 + One 03E8 ACK**.
4. Within 60 seconds, power-cycle **only the Thermia controller**.
5. Do not change any Thermia setting during the experiment.
6. Wait for one of:
   - `NEXT_STAGE_CAPTURED ...`, or
   - `SUMMARY POST_ACK_TIMEOUT ...`.
7. The post-ACK observation window is at most 15 seconds.
8. Immediately after the EXP257 summary/capture, reboot the Thermia controller once to leave the incomplete Online/Link session cleanly.
9. Return the complete log from `ARMED ACTIVE` through the final `SUMMARY` / `NEXT_STAGE_CAPTURED` marker, plus whether the DHW-side `0` or `COMM. ERR ONLINE/LINK` appeared.

## Positive criterion

After the single exact `03E8/count14` ACK, the controller emits a **different** `0x0F` FC16 request or any `0x0F` FC03 request. The first such request is captured and never answered.

`03FC/count11` is the genuine Eco 5 prediction and the primary positive discriminator. `0410/count22` remains an informative alternative because earlier local EXP137 reached it after a `03E8` ACK, but EXP257 records any different block without ACKing it.

## Negative / stop criteria

- First post-R1 FC16 is not exact `03E8/count14` → **no ACK**, stop.
- Parser/drop guard changes → **no ACK**, stop.
- Approval retry or unexpected peer frame appears before ACK → **no ACK**, stop.
- Only `03E8` retries continue for 15 seconds after the one ACK → stop and record as a negative result.

## Expected recognizable log sequence

```text
[EXP257] ===== ARMED ACTIVE ... =====
[EXP257] ===== BUS_GAP >=6s ... =====
[EXP257] ===== BUS_RETURN ... =====
[EXP257] APPROVAL_REQ n=1 ...
[EXP257] ===== R1_TX_INTENT ... =====
[EXP257] ===== R1_TX_EXECUTED ... =====
[EXP257] FC16_REQ ... start=03E8 count=14 ...
[EXP257] ===== 03E8_ACK_TX_INTENT ... =====
[EXP257] ===== 03E8_ACK_TX_EXECUTED ... =====
```

Then either:

```text
[EXP257] ===== NEXT_STAGE_CAPTURED FC16 ...; NO ACK =====
```

or:

```text
[EXP257] ===== NEXT_STAGE_CAPTURED FC03 ...; NO RESPONSE =====
```

or after 15 seconds:

```text
[EXP257] ===== SUMMARY POST_ACK_TIMEOUT ... =====
```