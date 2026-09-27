## EXP266 protocol finding — local 0708 repeat after one idle response

Locally confirmed sequence:
`... -> 06EA/7 -> 06F1/3 -> 06F4/19 -> 085F/5 background -> FC03 0708/6 -> response 0F030C0000000000000000010000001C88 -> FC03 0708/6 repeat after ~4.18 s`

This proves:
- local XTR accepts the mailbox response electrically/protocol-wise far enough to keep the bus/session alive;
- one response does not terminate the mailbox polling phase;
- repeated `0708/6` polling is now locally observed after the first response, matching the repeated mailbox behavior in the genuine Eco5 capture qualitatively.

Do not infer yet that repeated identical responses are sufficient; that remains the next hypothesis to test.

---

## EXP266 target — locally confirmed 0708 mailbox, genuine Eco5 idle response

- EXP265 locally confirmed `FC03 0708/count6` as the first meaningful post-sync mailbox request after `06F4/19`, with `085F/5` appearing first as recurrent background traffic.
- Genuine Eco5 capture contains the exact idle response `0F030C0000000000000000010000001C88`, i.e. six words `0000 0000 0000 0000 0001 0000`.
- EXP266 will test that response exactly once against the local XTR M. This remains a hypothesis until run.
- No inference is made that `0001` is a generic ready flag; its semantics remain unknown.

## EXP264 — proven sync tail and background-overlay caveat

Local XTR now proves the ordered Online/Link tail:
`06EA/7 -> ACK -> 06F1/3 -> ACK -> 06F4/19 -> ACK`.

Immediately after the `06F4` ACK, the first observed FC16 was `085F/5` (+107 ms). Because `085F/5` was already established from passive captures as recurrent background traffic, it must not be promoted to an ordered synchronization stage merely because it is first after an ACK.

Protocol implication: future post-sync discovery must distinguish ordered session traffic from recurrent background families. Known recurrent `085F/5` should be logged but ignored as a discovery terminator after `06F4`; `04A6/13` remains context-sensitive because it can be both recurrent and ordered depending on phase.

The next meaningful stage after `06F4` remains unknown locally. `0708/count6` mailbox timing is still unresolved and no local mailbox response has been sent.

## EXP263 finding — 055A..06C5 33-word sync run locally confirmed

## EXP264 target — final small FC16 tail before mailbox/runtime observation

EXP263 locally proved the ordered 12-block 33-word run `055A..06C5` and captured `06EA/count7` next. EXP264 therefore tests only the next genuine Eco 5 tail: `06EA/7 -> 06F1/3 -> 06F4/19`, using standard one-shot FC16 ACKs. After `06F4` it is capture-only; FC03, including `0708/count6`, is evidence only and receives no response.

EXP263 locally confirmed the genuine Eco 5 FC16 sequence:
055A/33 -> 057B/33 -> 059C/33 -> 05BD/33 -> 05DE/33 -> 05FF/33 ->
0620/33 -> 0641/33 -> 0662/33 -> 0683/33 -> 06A4/33 -> 06C5/33 -> 06EA/7.

All twelve 33-word blocks were ACKed exactly once and in order. 06EA/count7 arrived +475 ms after the 06C5 ACK and was not ACKed. The run remained parser/RX clean. This is strong evidence that the XTR and genuine Eco 5 share this synchronization segment.

Do not generalize this into broad FC16 ACKing: only the exact known ordered stages are proven. Full Online/Link establishment, the later 06F1/06F4 stages, and local 0708 mailbox timing remain open.

## EXP262 — accelerated chain proof through 055A/count33

EXP262 establishes the following local ordered Online/Link path after the already-proven prefix: `04A6/13 -> 04BA/22 -> 04D8/27 -> 04F6/14 -> 050A/19 -> 051E/10 -> 0532/18 -> 0546/20 -> 055A/33`. The first eight pages were ACKed exactly once; `055A/33` was captured only. This matches the genuine Eco 5 ordering and validates larger bounded ACK batches.

Important refinement: `04A6/13` is recurrent elsewhere on the bus, but in EXP262 it was ACKed only in the exact post-`0492` sync phase, after which the expected ordered chain continued. Context therefore remains essential; address alone does not identify a sync-stage occurrence.

The known incomplete-session failure (`DHW-side 0` / `COMM. ERR ONLINE/LINK`) remains a session-completion hypothesis, not a proven causal mechanism. `0708/count6` has not yet been serviced locally.

# THERMIA PROTOCOL FINDINGS

## EXP262 accelerated-batch target

EXP261 locally confirmed the ordered chain through `0492/count11`, with `04A6/count13` immediately next. EXP262 deliberately increases batch size while retaining exact sequencing and fail-closed checks. Target progression:
`04A6/13 -> 04BA/22 -> 04D8/27 -> 04F6/14 -> 050A/19 -> 051E/10 -> 0532/18 -> 0546/20`, then capture-only. Genuine Eco 5 predicts `055A/count33` after this block.

`04A6/13` remains context-sensitive because it is also recurrent passive traffic; EXP262 only ACKs it in phase 12 immediately after a successful `0492/count11` ACK. This does not establish every `04A6` occurrence as a synchronization page.


## EXP261 result — ordered sync now proven through 0492

EXP261 extended the local XTR Online/Link synchronization prefix using a bounded batch of exact standard FC16 ACKs:

`046A/18 -> ACK -> 047E/19 -> ACK -> 0492/11 -> ACK -> 04A6/13`

The post-0492 `04A6/count13` request arrived +576 ms after the 0492 ACK and was not acknowledged.

This is important because `04A6/13` is also a recurrent passive family. EXP261 shows that, in the approved synchronization state, it can also occupy the expected ordered next position after `0492/11`. The observation does not make every passive `04A6` instance part of the sync chain; context remains necessary.

The local chain is now directly demonstrated through:
`03E8/14 -> 03FC/11 -> 0410/22 -> 042E/15 -> 0442/13 -> 0456/12 -> 046A/18 -> 047E/19 -> 0492/11 -> 04A6/13`.

Full Online/Link establishment is still not proven because downstream pages and FC03/mailbox service remain unanswered.


## EXP261 target — bounded continuation after EXP260

EXP260 validates batching already-proven genuine Eco 5 FC16 synchronization pages. The next bounded continuation is `046A/18 -> 047E/19 -> 0492/11`, each with a standard one-shot FC16 ACK. The first different post-0492 frame is capture-only.

Genuine Eco 5 reference order places `04A6/count13` next, but prior capture analysis also classifies `04A6/13` as a recurrent passive family overlaid on synchronization. Therefore EXP261 does not use the presence or absence of `04A6` alone as a hard protocol success/failure criterion. No broad ACKing and no `0708` response are authorized by this experiment.


## EXP260 finding — bounded batch reproduces the next three genuine sync transitions

Local XTR evidence now proves the ordered post-approval prefix through `046A/count18`:

`03E8/14 -> ACK -> 03FC/11 -> ACK -> 0410/22 -> ACK -> 042E/15 -> ACK -> 0442/13 -> ACK -> 0456/12 -> ACK -> 046A/18`

The first three stages were proven incrementally in EXP257-259; EXP260 then safely batched the next three exact Eco 5 pages. There were no same-stage retries, unexpected peer responses, or post-return parser/drop errors. `046A/count18` was deliberately left unanswered.

The recurring DHW-side literal `0` appeared again during/after this deliberately incomplete session. This supports the incomplete-session side-effect model, but the exact semantics of the UI `0` remain unknown.

Protocol implication: small, pre-verified page batches are now evidence-backed as a practical way to progress the remaining genuine sync chain without one controller reboot per FC16 page. This does **not** authorize broad blind ACKing or FC03/mailbox emulation.

Last updated: 2026-09-27 after EXP259 / EXP260 prepared

## EXP260 bounded-batch protocol target

EXP256–259 have now locally reproduced the same genuine Eco 5 ordered Online/Link prefix through `042E/count15`. Because four consecutive reference stages have matched, EXP260 deliberately increases throughput while remaining fail-closed: it ACKs only the next three exact known reference blocks `042E/15`, `0442/13`, `0456/12`, in that order, and then captures the first different stage. The external reference predicts `046A/count18`.

This does **not** authorize broad FC16 ACKing or any `0708` mailbox response. A mailbox request at any point remains a capture-and-stop event in EXP260.

## EXP259 — local ordered Online/Link sync confirmed through `042E/count15`

EXP259 extends the bounded local XTR progression by exactly one ACK.

Observed local sequence:
`R1 -> 03E8/14 -> ACK -> 03FC/11 -> ACK -> 0410/22 -> ACK -> 042E/15`

Timing:
- approval: +1283 ms after BUS_RETURN;
- `03E8`: +138 ms after R1;
- `03FC`: +682 ms after `03E8` ACK;
- `0410`: +1498 ms after `03FC` ACK;
- `042E`: +696 ms after `0410` ACK.

Exact `042E/count15` payload words:
`0001 0001 0000 000A FFF6 0005 001E 0000 002D 0000 0000 0000 0000 0000 0000`.

**Strong conclusion:** the local XTR follows the same genuine Eco 5 initial synchronization ordering at least through the first four ordered FC16 pages:
`03E8/14 -> 03FC/11 -> 0410/22 -> 042E/15`.

**Unknown:** whether all later Eco 5 pages and the `0708/count6` mailbox phase are identical on the XTR. Full Online/Link establishment is not yet proven.

---

Last updated: 2026-09-27 after EXP258

## Reproducible incomplete-session UI failure mode — confirmed through EXP259

Across multiple active approval/sync experiments, including EXP259, entering the native Online/Link state machine and then deliberately stopping before a complete endpoint session produces the same front-panel symptoms: DHW-side literal `0` and exact `COMM. ERR ONLINE/LINK`. One normal controller reboot restores normal operation.

This strongly supports an incomplete-session timeout interpretation, but does not yet prove the exact causal point or required minimum service depth. A future sufficiently complete session that does not trigger the alarm would be the cleanest confirmation.


## EXP258 — XTR confirms third ordered Online/Link sync block

EXP258 extends the local post-approval proof by one stage. After one R1 response, one exact ACK of `03E8/count14`, and one exact ACK of `03FC/count11`, the next controller block is exact `0410/count22`. Timing: approval +1243 ms after BUS_RETURN; `03E8` +138 ms after R1; `03FC` +691 ms after the 03E8 ACK; `0410` +1501 ms after the 03FC ACK.

**Strong protocol conclusion:** the local XTR now matches the genuine Eco 5 ordered prefix through three FC16 pages:

`approval response -> 03E8/14 -> ACK -> 03FC/11 -> ACK -> 0410/22`.

`0410` was intentionally not ACKed, so no claim is made about later local ordering or mailbox entry. Full Online/Link establishment remains unproven.

The user again observed the DHW/tank-side literal `0` and the exact `COMM. ERR ONLINE/LINK` alarm. This repeat strengthens the interpretation that the alarm is associated with an approved-but-incompletely-serviced Online/Link session, but that remains a hypothesis until a sufficiently complete session avoids the alarm.

---

Last updated: 2026-09-27 after EXP257; EXP258 prepared. Detailed historical findings restored from the uploaded canonical snapshots.

## External Eco 5 endpoint behavior refined after EXP257

The complete raw capture confirms the cold-start approval stream is startup-bounded rather than a steady-state feature in the observed Eco 5 sessions: first approval requests occur about 1.2 s after bus return, while an already-running steady-state segment with the gateway connected has no `071C/0730` traffic. Therefore steady-state absence on another model is not evidence that its cold-start stream is absent.

Two genuine successful sessions provide the same transfer prefix:

`approval response -> 03E8/14 -> ACK -> 03FC/11 -> ACK -> 0410/22`

This is now locally matched by EXP257 through `03FC/11`.

`04A6/13` and `085F/5` should remain classified as recurrent/passive families that can be interleaved with the transfer. Their ACK timing is phase-dependent across the two external power-ups, so they are not established approval preconditions and should not be promoted into the invariant ordered sync chain.

The genuine endpoint begins answering `0708/count6` while FC16 synchronization is still underway. The raw repeated idle response is:

`0F 03 0C 0000 0000 0000 0000 0001 0000 <CRC>`

=> six words: `0000 0000 0000 0000 0001 0000`.

A public comment wrote the fifth word as `0100`; this is not what the raw frame contains under standard Modbus big-endian register ordering. Preserve the raw value `0001` unless later evidence establishes a deliberate byte-swapped semantic representation.

Later fifth-word values in the same session descend through `03DC` (988), 984, 976, 908, 896, 768, 512, then 0. The sequence is factual; "pending synchronization item counter" is only a hypothesis.

The known local `COMM. ERR ONLINE/LINK` after partial participation is compatible with a session-service timeout, but that causal interpretation remains a hypothesis until a sufficiently serviced local session avoids the alarm.
## EXP257 — local XTR reproduces genuine Eco 5 `03E8 -> 03FC` synchronization transition

EXP257 adds the first local XTR proof of the next acknowledged post-approval transition.

Observed sequence:

```text
0x0F FC17 approval request
  -> one replayed R1
  -> FC16 03E8/count14
  -> one standard FC16 ACK
  -> FC16 03FC/count11
  -> no further ACK
```

Timing in EXP257:
- approval request: +1285 ms after BUS_RETURN;
- `03E8/count14`: +130 ms after R1;
- `03FC/count11`: +691 ms after the one `03E8` ACK.

Exact `03FC` request:

`0F1003FC000B160028000A0037000000000000000200120028001E003C369E`

Payload words:

`0028 000A 0037 0000 0000 0000 0002 0012 0028 001E 003C`

The experiment deliberately did **not** ACK `03FC`.

**Strong protocol conclusion:** the local XTR now matches the genuine Eco 5 Online/DCM synchronization prefix through two post-approval stages:

`approval response -> 03E8/count14 -> ACK -> 03FC/count11`

The genuine Eco 5 reference proves this same transition in two independent successful approval cycles and then shows:

`03FC/count11 -> ACK -> 0410/count22`.

This materially strengthens the cross-model architectural link. It does not yet prove that the local XTR will follow the complete Eco 5 synchronization chain or reach the `0708/count6` mailbox/runtime phase.

No semantic register write was performed in EXP257: the only new active frame was a standard FC16 acknowledgement echoing address/count and carrying no register-value payload.

Last updated: 2026-09-27 after EXP256 + full external Eco 5 capture refinement
## EXP256 — R1 crosses approval boundary into native 03E8 synchronization

EXP256 materially resolves the ambiguity left by EXP252/EXP255. After one exact replay of the already-tested R1 response to the first local `071C/0730` approval request:

- the approval loop stopped after **one** request;
- no second approval request occurred;
- the controller immediately began `0x0F FC16 03E8/count14`;
- first `03E8/count14` arrived **124 ms after R1**;
- `03E8/count14` repeated **389 times** through +419.896 s;
- the only other FC16 family was one boot-only `04BA/count22` request before R1;
- passive runtime families `04A6/count13` and `085F/count5` were both absent;
- no FC03 request appeared;
- EXP256 deliberately provided no FC16 ACK or FC03 response.

**Strong protocol conclusion:** R1 is not merely suppressing one passive FC16 family. It advances the local XTR controller across the approval/retry state into the native acknowledged `0x0F` synchronization state machine, whose first observed stage is `03E8/count14`. With no endpoint ACK, the controller stalls and retransmits that block.

This links two previously separate findings:
- EXP252: R1 terminates the `071C/0730` retry loop and causes a reproducible controller-visible side effect;
- EXP137+: acknowledging native `03E8/count14` advances an ordered controller->0x0F transfer sequence.

The EXP255 numerical clue (`582 - 195 ≈ 386`) is now recorded as a misleading coincidence rather than the correct mechanism. EXP256 shows that the post-R1 traffic is a **new 03E8 synchronization family**, not persistence of the passive `04A6` family.

The user again observed the DHW/tank-side literal `0`, followed after the run by the exact same front-panel alarm as EXP252: **`COMM. ERR ONLINE/LINK`**. No VERSION-screen change was seen; this is compatible with the architecture because VERSION `EXP` display is controlled by the separate `0x06/AFD1` expansion metadata path, not by the `0x0F` approval/synchronization path tested here.

**Still unknown:** full Online/Link session establishment, the required ACK chain after `03E8`, any eventual FC03/mailbox phase, and the semantic meaning of the DHW-side `0`.
## 2026-09-27 — EXP256 approval-to-sync transition

EXP256 provides the first direct local link between the startup `071C/0730` approval exchange and the native `0x0F` synchronization chain.

Observed sequence:

```text
BUS_RETURN
  -> first exact 071C/0730 approval request
  -> one-shot R1 response
  -> approval retries stop
  -> 124 ms later: controller FC16 03E8/count14
  -> no endpoint ACK
  -> repeated 03E8/count14 for the remainder of the 7-minute run
```

Complete active census: `04BA/count22` x1 before R1, then `03E8/count14` x389; `04A6/count13` x0; `085F/count5` x0; no FC03 phase.

**Protocol consequence:** the earlier EXP255/EXP252 count coincidence did not represent simple selective `085F` suppression. R1 instead advances the controller into the first stage of the acknowledged native settings synchronization state machine previously mapped in EXP137+. The endpoint is expected to ACK the FC16 block before progression.

**Session-status refinement:** R1 is accepted far enough to suppress approval retries and start sync, but this is not proof of a complete Online/Link session. In EXP256 no FC16 ACK, FC03 mailbox response, or later sync stage was supplied.

**UI side effect:** the DHW/tank-side literal `0` reappeared and the front panel again raised **`COMM. ERR ONLINE/LINK`** after the active run, exactly reproducing EXP252; VERSION did not change. This makes the R1 incomplete-session side effect reproducible while remaining separate from the `0x06/AFD1` VERSION metadata path. Exact meaning of the `0` remains unknown.


---
## 2026-09-27 — complete genuine iTec Eco 5 gateway capture: approval -> sync -> mailbox chain

A complete 1482.480 s Eco 5 gateway capture provides the first continuous raw evidence connecting genuine approval responses to the downstream acknowledged synchronization state machine.

### Approval retry behavior

The capture contains 99 exact `0x0F FC17 read 0730/count8 + write 071C/count8` requests in three windows (29, 41 and 29 requests). Their median cadences are about 4.24 s, 4.26 s and 4.21 s. 98 of the 99 16-byte `071C` payloads are unique; one payload repeats once. Thus the genuine Eco 5 source normally regenerates the 16-byte challenge-like value across retries.

Two successful challenge/response pairs are present inline in the raw capture:

```text
C1 63CE FB32 C6F4 1382 0879 9237 0CAC EEBA
R1 1691 A5F3 F8E8 D587 3892 4416 E8E6 A3D5

C2 31FB 59FC 8FB1 175C D89F 904D 06D9 2EA4
R2 FD63 6CCD 0F92 1D83 FF23 2A1A 2413 B372
```

### Reproducible post-approval prefix

Both successful responses produce the same prefix:

```text
FC17 response
 -> 03E8/count14 request
 -> FC16 ACK 03E8/count14
 -> 03FC/count11 request
 -> FC16 ACK 03FC/count11
 -> 0410/count22 request
 -> FC16 ACK 0410/count22
```

Timing:

```text
                         R1 cycle       R2 cycle
03E8 request             +92 ms         +92 ms
03E8 ACK                 +137 ms        +122 ms
03FC request             +510 ms        +536 ms
0410 request             +1.950 s       +2.189 s
```

This is stronger than the earlier local EXP137 observation. `0410/count22` is not the demonstrated immediate successor to `03E8`; the genuine Eco 5 reference contains an intervening `03FC/count11` block.

### Ordered initial synchronization export

The first successful cycle establishes this ordered FC16 sequence (retries omitted):

`03E8/14 -> 03FC/11 -> 0410/22 -> 042E/15 -> 0442/13 -> 0456/12 -> 046A/18 -> 047E/19 -> 0492/11 -> 04A6/13 -> 04BA/22 -> 04D8/27 -> 04F6/14 -> 050A/19 -> 051E/10 -> 0532/18 -> 0546/20 -> 055A/33 -> 057B/33 -> 059C/33 -> 05BD/33 -> 05DE/33 -> 05FF/33 -> 0620/33 -> 0641/33 -> 0662/33 -> 0683/33 -> 06A4/33 -> 06C5/33 -> 06EA/7 -> 06F1/3 -> 06F4/19`.

The next observed stage is `07D0/count19`, interleaved with `FC03 0708/count6` mailbox polls. Later established traffic includes acknowledged `07E4`, `07F8`, `080C`, `0820`, `0834`, `0848`, `0864` and `0870` pages plus dynamic `0708` responses.

### Consequences for the local XTR project

- EXP256's local `R1 -> 03E8/count14` transition is now a direct prefix match to genuine Eco 5 Online/DCM behavior.
- The response replay reaches a real protocol boundary, not an arbitrary controller retry quirk.
- Full session establishment still cannot be inferred from R1 alone; the genuine endpoint acknowledges a long sequence and participates in `0708` mailbox/runtime exchange.
- EXP257 remains correctly bounded: ACK exactly the first local `03E8/count14` once, then capture the first different block without answering it.
- External-reference positive discriminator is now specifically `03FC/count11`. A local `0410/count22` first would demonstrate a platform/order difference and would also be valuable.

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