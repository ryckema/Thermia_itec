# THERMIA PROJECT STATE

## Authoritative current state — 2026-09-27 — EXP259 COMPLETE / STRONG POSITIVE

- Last completed experiment: **EXP259 — COMPLETE / STRONG POSITIVE**.
- **EXP239 remains OPEN.**
- **EXP238 remains PARKED / NOT RUN.**
- No next experiment is prepared yet.

### EXP259 hypothesis

After the locally proven chain `R1 -> 03E8/count14 ACK -> 03FC/count11 ACK -> 0410/count22`, send exactly one standard FC16 ACK for the first exact `0410/count22` block, then capture the first different FC16/FC03 stage without answering it. The genuine Eco 5 reference predicted `042E/count15`.

### EXP259 observed result

Observed sequence:
- BUS_RETURN
- first approval at +1283 ms
- R1 sent once
- `03E8/count14` at +138 ms after R1; ACKed once
- `03FC/count11` at +682 ms after 03E8 ACK; ACKed once
- `0410/count22` at +1498 ms after 03FC ACK; ACKed once
- `042E/count15` at +696 ms after 0410 ACK
- `042E` was **not** acknowledged

Exact first different request:
`0F10042E000F1E000100010000000AFFF60005001E0000002D0000000000000000000000003A99`

Decoded header:
- slave `0x0F`
- FC16
- start `0x042E`
- count `15`
- bytecount `30`

Payload words:
`0001 0001 0000 000A FFF6 0005 001E 0000 002D 0000 0000 0000 0000 0000 0000`

Safety/integrity summary:
- R1 used: 1
- 03E8 ACK: 1
- 03FC ACK: 1
- 0410 ACK: 1
- approval retries after R1: 0
- 03E8 retries after ACK: 0
- 03FC retries after ACK: 0
- 0410 retries after ACK: 0
- unexpected peer frames: 0
- post-return parser resync delta: 0
- post-return RX-drop delta: 0
- DE LOW
- no FC03/mailbox response
- no ACK beyond `0410`

### Strong conclusion

The local XTR now reproduces the genuine Eco 5 ordered Online/Link synchronization prefix through four consecutive FC16 pages:

`approval response -> 03E8/14 -> ACK -> 03FC/11 -> ACK -> 0410/22 -> ACK -> 042E/15`

This is the third consecutive bounded positive progression after EXP256–258 and strongly supports that the replayed R1 enters the native Online/Link synchronization state machine.

Full Online/Link establishment remains unproven because `042E` and all later blocks/mailbox traffic were deliberately left unanswered.

### UI / recovery

The EXP259 log itself does not report the front-panel UI. As with EXP252/256/258, an incomplete approved session may again lead to DHW-side `0` and/or `COMM. ERR ONLINE/LINK`; exact EXP259 UI outcome awaits user confirmation. Perform one normal Thermia-controller reboot after this run.

---

## Authoritative current state — 2026-09-27 — EXP258 COMPLETE / EXP259 PREPARED / NOT RUN

- Last completed experiment: **EXP258 — COMPLETE / STRONG POSITIVE**.
- Current prepared experiment: **EXP259 — R1 + exact `03E8/count14` ACK + exact `03FC/count11` ACK + exact `0410/count22` ACK + next-stage capture — PREPARED / NOT RUN**.
- **EXP239 remains OPEN.**
- **EXP238 remains PARKED / NOT RUN.**

### EXP259 hypothesis

EXP258 locally proved the ordered prefix `R1 -> 03E8/14 ACK -> 03FC/11 ACK -> 0410/22`. EXP259 changes one active variable only: acknowledge that already-proven exact `0410/count22` request once, then capture the first different FC16/FC03 stage without answering it. The genuine Eco 5 reference predicts `042E/count15` next.

### Exact new active target

- Required request: slave `0x0F`, FC16, start `0x0410`, count `22` (`0x0016`), bytecount `44` (`0x2C`), full request length `53` bytes.
- Exact standard FC16 ACK: `0F 10 04 10 00 16 40 1C`.
- CRC16 over `0F1004100016` is `0x1C40`, transmitted little-endian `40 1C`.
- The ACK carries no register-value payload; it echoes only start/count.

### EXP259 fail-closed boundary

Maximum experimental TX is four frames: one R1, one exact `03E8/14` ACK, one exact `03FC/11` ACK and one exact `0410/22` ACK. The new `0410` ACK is allowed only after the proven prefix, only when the first post-`03FC`-ACK FC16 is exact `0410/22`, within 5 s, with unchanged parser/drop counters, no approval/03E8/03FC retry, and no unexpected peer frame. All one-shot latches close before DE is enabled.

After the one `0410` ACK:
- no second `0410` ACK;
- no ACK of `042E` or any later FC16;
- no FC03/mailbox response;
- first different FC16 or any FC03 is captured and the experiment stops;
- 15 s timeout if only `0410` retries continue.

Known reproducible side effect remains the DHW-side `0` plus `COMM. ERR ONLINE/LINK` after an incomplete approved Online/Link session. **Do not run EXP259 until one normal controller reboot has cleared both after EXP258.** After EXP259 summary, reboot the Thermia controller once again.

### Build validation

- YAML syntax parsed successfully with ESPHome custom tags tolerated.
- `${device_name}` and `${friendly_name}` are the only substitutions referenced and both are defined.
- All 138 YAML IDs are unique and all `id(...)` references resolve.
- Exactly four DE-enable / UART TX call sites exist: R1, `03E8` ACK, `03FC` ACK, `0410` ACK.
- CRC-valid-frame bus-health bookkeeping is unchanged.
- ESPHome compile was **not run** because the ESPHome CLI is not installed in the available environment.

---


## Authoritative current state — 2026-09-27 — EXP258 COMPLETE / STRONG POSITIVE

- Last completed experiment: **EXP258 — COMPLETE / STRONG POSITIVE**.
- No next experiment is yet prepared.
- **EXP239 remains OPEN.**
- **EXP238 remains PARKED / NOT RUN.**

### EXP258 hypothesis

After the already-proven local prefix `R1 -> 03E8/count14 -> ACK -> 03FC/count11`, acknowledge exactly the first `03FC/count11` FC16 request once and capture the first different FC16/FC03 stage without answering it. Genuine Eco 5 reference predicts `0410/count22`.

### EXP258 observed facts

- BUS_RETURN occurred after the controller power-cycle; two parser resync events happened exactly at the return edge, while the experiment summary recorded `resync_postreturn=0` and `drop_postreturn=0`.
- First approval request: **+1243 ms after BUS_RETURN**.
- R1 sent exactly once; no approval retry after R1.
- First post-R1 `03E8/count14`: **+138 ms after R1**.
- Exact `03E8/count14` ACK sent once: `0F 10 03 E8 00 0E C0 93`.
- First post-03E8-ACK block: exact `03FC/count11` at **+691 ms**.
- Exact `03FC/count11` ACK sent once: `0F 10 03 FC 00 0B 40 94`.
- First post-03FC-ACK different block: exact **`0410/count22` at +1501 ms**.
- `0410/count22` was captured and **not acknowledged**.
- Summary: `r1=1 ack03e8=1 ack03fc=1 approvals=1 approval_after_r1=0 post_r1_fc16=1 post_03e8_fc16=1 same03e8_after_ack=0 same03fc_after_ack=0 peer17=0 unexpected_peer_ack=0 self_echo_r1=0 self_echo_ack=0 resync_postreturn=0 drop_postreturn=0 DE=LOW`.
- User reports the DHW/tank-side literal **`0` reappeared** and the same **`COMM. ERR ONLINE/LINK`** alarm appeared again.

Exact captured `0410/count22` request:

`0F10041000162C0028000A0037000000000000000200120028001E003C00120014002F001E00070000003C000D00060037000088E3`

### Strong conclusions

- EXP258 locally reproduces the genuine Eco 5 synchronization prefix one step further: `R1 -> 03E8/14 -> ACK -> 03FC/11 -> ACK -> 0410/22`.
- The Eco 5 prediction for the third ordered sync block is therefore confirmed on the XTR.
- The replayed R1 is sufficient to move the XTR through at least the first three native Online/Link synchronization stages when the expected FC16 ACKs are supplied.
- The repeated DHW-side `0` + exact `COMM. ERR ONLINE/LINK` after EXP252/256/258 remains consistent with an approved but incompletely serviced Online/Link session timing out; this causal explanation is now stronger but still not proven.

### Unknowns / safety

- Full Online/Link establishment is still unproven.
- `0410/count22` and all later FC16 pages remain unacknowledged locally.
- No local `0708/count6` mailbox response has been provided.
- Do not broaden directly to full-chain ACK + mailbox emulation in one step.
- Recovery after EXP258 remains one normal controller reboot; confirm the `0` and alarm clear before another active test.

---

## Authoritative current state — 2026-09-27 — EXP257 COMPLETE / EXP258 PREPARED / NOT RUN

- Last completed experiment: **EXP257 — COMPLETE / STRONG POSITIVE**.
- Current prepared experiment: **EXP258 — R1 + exact `03E8/count14` ACK + exact `03FC/count11` ACK + next-stage capture — PREPARED / NOT RUN**.
- **EXP239 remains OPEN.**
- **EXP238 remains PARKED / NOT RUN.**

### EXP258 hypothesis

EXP257 locally proved `R1 -> 03E8/count14 -> ACK -> 03FC/count11`. EXP258 changes one active variable only: acknowledge that already-proven exact `03FC/count11` request once, then capture the first different FC16/FC03 stage without answering it. The genuine Eco 5 reference predicts `0410/count22` next.

### Exact new active target

- Required request: slave `0x0F`, FC16, start `0x03FC`, count `11` (`0x000B`), bytecount `22` (`0x16`), full request length `31` bytes.
- Exact standard FC16 ACK: `0F 10 03 FC 00 0B 40 94`.
- CRC16 over `0F1003FC000B` is `0x9440`, transmitted little-endian `40 94`.
- The ACK carries no register-value payload; it echoes only start/count.
- The same ACK frame is present in the genuine Eco 5 raw capture.

### EXP258 fail-closed boundary

Maximum experimental TX is three frames: one R1, one exact `03E8/count14` ACK, one exact `03FC/count11` ACK. The new `03FC` ACK is allowed only after the proven prefix, only when the first post-`03E8`-ACK FC16 is exact `03FC/11`, within 5 s, with unchanged parser/drop counters, no approval retry, no `03E8` retry, and no unexpected peer frame. All one-shot latches close before DE is enabled.

After the one `03FC` ACK:
- no second `03FC` ACK;
- no ACK of `0410` or any later FC16;
- no FC03/mailbox response;
- first different FC16 or any FC03 is captured and the experiment stops;
- 15 s timeout if only `03FC` retries continue.

Known possible side effect remains an incomplete Online/Link session with DHW-side `0` and/or `COMM. ERR ONLINE/LINK`; recovery is one normal Thermia-controller reboot after the summary.

### Build validation

- YAML syntax parsed successfully with ESPHome custom tags tolerated.
- `${device_name}` and `${friendly_name}` are the only substitutions referenced and both are defined.
- All `id(...)` references resolve to defined YAML IDs; no duplicate IDs found.
- Exactly three DE-enable / UART TX call sites exist: R1, `03E8` ACK, `03FC` ACK.
- CRC-valid-frame bus-health bookkeeping remains present and unchanged.
- ESPHome compile was **not run** because the ESPHome CLI is not installed in the available environment.

---

## External Eco 5 follow-up after EXP257 — 2026-09-27

The new public-comment analysis has been cross-checked against the full raw Eco 5 capture. It materially refines the reference behavior but does not change the EXP257 result.

Observed from the raw capture:
- three cold-start approval windows begin with the first `071C/0730` request at **+1.199 s, +1.202 s, and +1.210 s** after bus return; this matches the local XTR EXP248/249/256/257 ~+1.28 s startup phase closely;
- with the genuine gateway attached, the two successful approval responses occur at **+120.153 s** and **+119.808 s** after bus return, after 29 challenge requests each;
- the no-gateway middle run was power-cycled after only ~174 s, with 41 unanswered challenges through +171.230 s, so it cannot test the local ~267 s / 63-request natural stop;
- the already-running steady-state segment before the first power-off contains no `071C/0730` traffic, so absence in steady-state captures does not prove a model lacks the cold-start approval stream;
- only two answered challenges exist, so challenge-repeat determinism and response stability across power cycles remain **unknown**; the one duplicated challenge in the capture was unanswered.

### Gateway behavior after approval

The genuine Eco 5 endpoint ACKs the controller's FC16 transfer blocks and the stable prefix is:

`03E8/14 -> ACK -> 03FC/11 -> ACK -> 0410/22 -> ACK -> 042E/15 -> ...`

The broad controller-export sequence then continues through the known 0x03E8..0x0864 range. `04A6/13` and `085F/5` are recurrent passive families overlaid on that transfer; their ACK timing differs between power-ups and they are **not supported as approval preconditions**. Do not treat their interleaving position as a required ordered sync step.

The first `0708/count6` mailbox poll occurs while the FC16 transfer is still in progress:
- first successful power-up: **+158.393 s** after bus return; the first poll is unanswered, the next poll is answered;
- second successful power-up: **+186.828 s** after bus return and is answered immediately.

**Raw-frame correction:** the repeated post-approval idle mailbox response in the public capture is `0F 03 0C 0000 0000 0000 0000 0001 0000 ...`, i.e. six Modbus words `0000 0000 0000 0000 0001 0000`. A comment transcribed the fifth word as `0100`; the raw bytes support `0001` in standard Modbus register order.

Later in the second successful session the fifth mailbox word is observed at `03DC` (988), then 984, 976, 908, 896, 768, 512, and finally 0. This is an **observed countdown-like sequence**. Interpreting it as pending sync-item count remains a hypothesis.

### Next bounded candidate

**EXP258 — candidate / NOT PREPARED.** Hypothesis: after the already-proven `R1 -> 03E8/14 ACK -> 03FC/11`, one exact standard ACK to the first local `03FC/count11` should advance the XTR to `0410/count22`, matching both successful genuine Eco 5 sessions. Stop on the first different block and do not ACK `0410`.

Do **not** jump directly to ACKing the entire chain or answering `0708`; that would change multiple active variables at once and would lose the clean discriminator established by EXP256-257.


## Authoritative current state — 2026-09-27 — EXP257 COMPLETE / STRONG POSITIVE

- Last completed experiment: **EXP257 — COMPLETE / STRONG POSITIVE**.
- **EXP239 remains OPEN.**
- **EXP238 remains PARKED / NOT RUN.**
- No next experiment is yet authorized/prepared.

### EXP257 hypothesis

After the same guarded one-shot R1 used in EXP256, acknowledge exactly the **first** post-R1 `0x0F FC16 03E8/count14` request once. Then observe the first different `0x0F` FC16/FC03 stage without answering it.

The full genuine Eco 5 gateway capture predicted `03FC/count11` as the immediate next stage.

### EXP257 observed result

The complete experiment sequence was:

```text
BUS_RETURN
  -> +1285 ms approval request 071C/0730
  -> R1 sent once
  -> +130 ms first post-R1 FC16 03E8/count14
  -> one exact FC16 ACK 0F1003E8000EC093
  -> +691 ms first different post-ACK block FC16 03FC/count11
  -> NO ACK
  -> SUMMARY NEXT_STAGE_FC16
```

Exact first different request:

`0F1003FC000B160028000A0037000000000000000200120028001E003C369E`

Decoded FC16 header:
- slave `0x0F`
- function `0x10`
- start `0x03FC`
- count `11`
- bytecount `22`

Payload words:
`0028 000A 0037 0000 0000 0000 0002 0012 0028 001E 003C`

Safety/integrity summary:
- R1 used: `1`
- one `03E8` ACK used: `1`
- approvals: `1`
- approval retries after R1: `0`
- same-`03E8` retries after ACK: `0`
- unexpected peer FC17: `0`
- unexpected peer FC16 ACK: `0`
- self echo R1/ACK: `0/0`
- post-return parser resync delta: `0`
- post-return RX-drop delta: `0`
- DE returned LOW
- `03FC/count11` was **not acknowledged**

### Strong conclusion

EXP257 reproduces the same post-approval synchronization prefix as the genuine Eco 5 reference:

`approval response -> 03E8/count14 -> ACK -> 03FC/count11`

This is a second independent XTR-to-Eco5 architecture match after EXP256 first established `approval response -> 03E8/count14`.

The result strongly supports that the replayed R1 is sufficient to advance the local XTR through at least the first two native controller->Online/Link synchronization stages. It still does **not** prove full Online/Link session establishment, because `03FC` and all downstream stages/mailbox traffic were deliberately left unanswered.

### Comparison with genuine Eco 5

The full Eco 5 capture shows the same prefix twice, then continues:

`03E8/14 -> ACK -> 03FC/11 -> ACK -> 0410/22 -> ...`

EXP257 stopped exactly at `03FC/11`, as intended. Therefore the next protocol question is whether acknowledging this exact `03FC/count11` on the XTR yields `0410/count22`, but no such next experiment has yet been run or authorized.

### UI / recovery status

The protocol objective is complete from the supplied log. Front-panel side effects for this run have not yet been reported. Because EXP252/EXP256 showed the recoverable DHW-side `0` / `COMM. ERR ONLINE/LINK` failure mode after incomplete Online/Link participation, perform one normal controller reboot after this EXP257 capture if not already done.

## Authoritative current state — 2026-09-27 — EXP256 COMPLETE / EXP257 PREPARED / NOT RUN

- Last completed experiment: **EXP256 — COMPLETE / ACTIVE STRONG POSITIVE**.
- Current prepared experiment: **EXP257 — ONE-SHOT R1 + SINGLE `03E8/count14` ACK + NEXT-STAGE CAPTURE — PREPARED / NOT RUN**.
- **EXP239 remains OPEN.**
- **EXP238 remains PARKED / NOT RUN.**

### EXP257 hypothesis

EXP256 proved the sequence `071C/0730 approval -> one R1 -> approval retries stop -> FC16 03E8/count14 repeats`. EXP257 changes one variable only: after the same guarded one-shot R1, send **one standard FC16 ACK** to the first exact post-R1 `03E8/count14` request, then observe the first different FC16/FC03 stage without answering it.

The complete genuine Eco 5 capture now makes `03FC/count11` the external-reference prediction for the immediate next stage after the `03E8/count14` ACK. Prior local EXP137 evidence still shows `0410/count22` later in progression; EXP257 does not require or ACK either block.

### New active target and known effects

- Required request: slave `0x0F`, FC16, start `0x03E8`, count `14`, bytecount `28`, length `37`.
- Single ACK frame: `0F 10 03 E8 00 0E C0 93`.
- The ACK echoes only address/count and contains **no register-value payload**.
- CRC16 over `0F1003E8000E` is `0x93C0`, transmitted little-endian `C0 93`.
- Genuine Eco 5 full capture shows `03E8/14 ACK -> 03FC/11 -> 0410/22` in two independent successful approval cycles.
- EXP137 previously showed locally that ACKing exact `03E8/count14` reaches `0410/count22`, but did not prove there was no intervening `03FC/11`.
- Possible side effect remains an incomplete Online/Link session with DHW-side `0` and later `COMM. ERR ONLINE/LINK`; recovery is one normal controller reboot.

### EXP257 fail-closed boundary

The `03E8` ACK is permitted only when R1 has already been sent once, there was no approval retry, the **first** post-R1 FC16 is exact `03E8/14/bytecount28/len37`, it arrives within 5 s of R1, parser/drop counters remain unchanged since BUS_RETURN, and no unexpected peer FC17/FC16 ACK was observed. The ACK latch closes before DE is enabled.

After that one ACK:
- no second `03E8` ACK;
- no ACK for `03FC`, `0410`, or any other FC16;
- no FC03/mailbox/desired-state response;
- first different FC16 or any FC03 is captured and the experiment stops;
- otherwise a 15 s post-ACK timeout records a negative result.

### Run prerequisite and recovery

Do not run EXP257 until the controller has recovered from EXP256: `COMM. ERR ONLINE/LINK` absent, DHW-side `0` cleared, then healthy normal traffic for at least 15 s. After EXP257 capture/summary, perform one normal controller reboot immediately.

### Build validation

- YAML syntax parsed successfully with ESPHome custom tags tolerated.
- `${device_name}` and `${friendly_name}` are the only substitutions referenced and both are defined.
- All 124 `id(...)` references have matching YAML `id:` definitions.
- Only two DE-enable TX call sites exist: one R1 script and one exact `03E8` ACK script.
- CRC-valid-frame bus-health bookkeeping is unchanged.
- ESPHome compile was **not run** because the ESPHome CLI is not installed in the available environment.

## External Eco 5 full-capture refinement — 2026-09-27 — BEFORE EXP257

The complete genuine iTec Eco 5 gateway capture materially sharpens the expected post-approval state machine without changing the bounded EXP257 TX plan.

Observed across the 1482.480 s capture:
- 99 exact `0x0F FC17 read 0730/count8 + write 071C/count8` approval requests occurred in three retry windows: 29 requests (`184.661..303.554 s`), 41 requests (`394.976..565.004 s`), and 29 requests (`604.688..723.223 s`).
- Median retry cadence in those windows is approximately 4.24 s / 4.26 s / 4.21 s.
- 98/99 16-byte `071C` payloads are unique; one payload repeats once. Therefore the genuine Eco 5 challenge value is normally regenerated between retries rather than held constant.
- Successful pair 1 is directly present in the raw capture: `C1=63CEFB32C6F41382087992370CACEEBA` -> `R1=1691A5F3F8E8D58738924416E8E6A3D5`.
- Successful pair 2 is also directly present: `C2=31FB59FC8FB1175CD89F904D06D92EA4` -> `R2=FD636CCD0F921D83FF232A1A2413B372`.

Both successful responses are followed by the same acknowledged sync prefix:

```text
FC17 response
  -> +92 ms  FC16 03E8/count14
  -> ACK 03E8/count14
  -> FC16 03FC/count11
  -> ACK 03FC/count11
  -> FC16 0410/count22
  -> ACK 0410/count22
  -> ... broader ordered sync ...
```

Timing is highly reproducible:
- R1 cycle: `03E8` at +92 ms, ACK at +137 ms, `03FC` at +510 ms, `0410` at +1.950 s.
- R2 cycle: `03E8` at +92 ms, ACK at +122 ms, `03FC` at +536 ms, `0410` at +2.189 s.

The first successful cycle then progresses through the ordered controller-export chain:

`03E8/14 -> 03FC/11 -> 0410/22 -> 042E/15 -> 0442/13 -> 0456/12 -> 046A/18 -> 047E/19 -> 0492/11 -> 04A6/13 -> 04BA/22 -> 04D8/27 -> 04F6/14 -> 050A/19 -> 051E/10 -> 0532/18 -> 0546/20 -> 055A/33 -> 057B/33 -> 059C/33 -> 05BD/33 -> 05DE/33 -> 05FF/33 -> 0620/33 -> 0641/33 -> 0662/33 -> 0683/33 -> 06A4/33 -> 06C5/33 -> 06EA/7 -> 06F1/3 -> 06F4/19`, followed by `07D0/19` and the `0708/count6` mailbox/runtime phase.

**EXP257 consequence:** the external Eco 5 reference now predicts `03FC/count11` as the immediate next block after the single `03E8/count14` ACK. Prior local EXP137 evidence still records that `0410/count22` appears after a `03E8` ACK, but did not establish that it is the first intervening block. EXP257 remains necessary to determine the local XTR ordering. Its active behavior does not need to broaden: ACK only `03E8` once, capture the first different block, and stop.

## Authoritative current state — 2026-09-27 — EXP256 COMPLETE / ACTIVE STRONG POSITIVE

- Last completed experiment: **EXP256 — COMPLETE / ACTIVE STRONG POSITIVE**.
- Hypothesis tested: repeat the already-tested one-shot Eco 5 R1 response and enumerate the complete local post-R1 `0x0F FC16/FC03` distribution.
- One exact R1 response was transmitted at the first local approval request, **+1245 ms after BUS_RETURN**.
- Approval requests: **1 total; 0 retries after TX**.
- User-reported front-panel effect: the DHW/tank-side literal **`0` reappeared**; the VERSION screen showed **no change**.
- After `SUMMARY COMPLETE`, the front panel again raised the exact same alarm as EXP252: **`COMM. ERR ONLINE/LINK`**. This makes the incomplete Online/Link-session side effect reproducible across both R1 runs.
- No downstream emulation was provided: **0 FC16 ACKs, 0 FC03 responses, 0 second FC17 response**.

### EXP256 definitive post-R1 census

- `FC16 requests = 390`
- `FC16 ACKs = 0`
- `FC03 0708/count6 = 0`
- other `FC03 = 0`
- `peer17 = 0`
- `self_echo = 0`
- `s06 = 102`
- final state: `A80E=0028 A80F=000A AFDC=0010`
- post-BUS_RETURN parser resync delta: **0**
- post-BUS_RETURN RX drop delta: **0**
- DE returned LOW.

Complete FC16 family census in the EXP256 run:
- `04BA/count22`: **1** request, boot-only, before R1;
- `03E8/count14`: **389** requests, first **+1369 ms after BUS_RETURN / +124 ms after R1**, last **+419896 ms**, median inter-request interval about **1308 ms**;
- `04A6/count13`: **0**;
- `085F/count5`: **0**;
- no other FC16 family observed.

### Material protocol conclusion from EXP256

The EXP255-derived numerical hypothesis that R1 might merely suppress `085F/count5` while leaving `04A6/count13` intact is **rejected**. The earlier 582-vs-386 count coincidence was misleading.

R1 instead causes a much stronger state transition: immediately after the one-shot response, the controller enters the native `03E8/count14` FC16 synchronization stage and retransmits that first settings block continuously because EXP256 deliberately supplies no FC16 ACK. This reproduces the beginning of the acknowledged `0x0F` transfer state machine previously mapped in EXP137+, but now specifically **after the approval response**.

Therefore the strongest current interpretation is:
1. the R1 response is accepted far enough to terminate the `071C/0730` approval retry loop;
2. it advances the local XTR into a controller->Online/Link synchronization phase beginning at `03E8/count14`;
3. without the expected endpoint FC16 ACK, the controller stalls on that first synchronization block;
4. full Online/Link session establishment is still not proven; no FC03/mailbox phase was reached in EXP256.

The lack of VERSION-screen change is expected and not a negative discriminator: VERSION `EXP` metadata is the separate `0x06/AFD1` expansion-board path, while EXP256 acts only on the `0x0F` approval path.

### Safety / recovery after EXP256

The known R1 side effect is reproducible at least at the UI level (`0` at the DHW/tank icon). As planned, perform **one normal Thermia controller reboot after the EXP256 summary**. Do not run another active approval/sync experiment until the UI has returned to its normal state.

**EXP239 remains OPEN.**  
**EXP238 remains PARKED / NOT RUN.**

Next active candidate is not yet prepared. The highest-value controlled discriminator is likely a bounded post-R1 ACK of the already-proven exact `03E8/count14` FC16 request, with no ACK of any newly appearing block, to determine the first post-approval progression. This must be prepared as a separate experiment with explicit fail-closed guards.

## Authoritative current state — 2026-09-27 — EXP255 COMPLETE / EXP256 PREPARED

- Last completed experiment: **EXP255 — COMPLETE / VALID PASSIVE BASELINE**.
- Current prepared experiment: **EXP256 — ONE-SHOT R1 + FULL POST-R1 FC16/FC03 DIFFERENTIAL CENSUS — PREPARED / NOT RUN**.

### EXP255 definitive passive baseline

- approval requests: **63**
- first approval: **+1284 ms**
- last approval: **+265513 ms**
- median approval cadence: **4241 ms**
- FC16 requests: **582**
- FC16 ACKs: **0**
- FC03 requests: **0**
- FC03 responses: **0**
- parser resync delta: **0**
- RX drop delta: **0**
- TX disabled

Complete local passive FC16 families:
- `04BA/count22`: **4**, boot-only (+316..+3641 ms)
- `04A6/count13`: **383**, persistent (+4337..+419417 ms)
- `085F/count5`: **195**, persistent (+2265..+419542 ms)

No other 0x0F FC16 family and no FC03 request appears in the full seven-minute run.

The FC16 streams continue after the 63rd/final approval request: 219 FC16 requests occur after
+265513 ms, proving that normal FC16 runtime traffic is separate from the approval retry budget.

### New EXP252 / EXP255 differential hypothesis

EXP252 one-shot R1 had `fc16req=386` over the same seven-minute observation window.
EXP255 passive baseline has 582, a difference of **196**.

EXP255's `085F/count5` family alone contributes **195** requests. The remaining passive families
contribute **387**, almost exactly EXP252's 386 total.

This supports, but does not yet prove, the hypothesis that R1 selectively suppresses the normal
`085F/count5` family while leaving `04A6/count13` largely intact.

### EXP256 hypothesis

Repeat the already-tested EXP252 one-shot R1 response with the same fail-closed guards while logging
every FC16 and FC03 address/count. No downstream ACK or response is added.

Primary discriminator:
- disappearance/reduction of `085F/count5`;
- persistence of `04A6/count13`;
- or appearance of any new FC16/FC03 family.

Known recoverable side effect:
- previous R1 produced DHW-side `0` and `COMM. ERR ONLINE/LINK`;
- one normal controller reboot cleared both.
- EXP256 should be followed by one controller reboot immediately after its summary; do not wait for
  the communication alarm.

**EXP239 remains OPEN.**
**EXP238 remains PARKED / NOT RUN.**



## Authoritative current state — 2026-09-27 — EXP255 PREPARED / NOT RUN

- Last completed experiment: **EXP254 — COMPLETE / VALID PASSIVE POSITIVE**.
- Recovery confirmation from the user:
  - after the manual controller restart following EXP252,
  - `COMM. ERR ONLINE/LINK` cleared,
  - the DHW/tank-side `0` also cleared.
- Therefore EXP252 side effects were **recoverable by one normal controller reboot with no active
  responder**. Spontaneous self-clear without reboot remains untested.
- Current prepared experiment: **EXP255 — PASSIVE FULL 0x0F FC16/FC03 BASELINE CENSUS**.
- Reason for inserting EXP255 before another active R1 test:
  - EXP254 counted only exact `0870/count17` and `0708/count6`;
  - it did not map all local `0x0F FC16` and `FC03` start/count pairs;
  - without this baseline, an active post-R1 address census would be ambiguous.
- EXP255 is fully RX-only and records every `0x0F FC16` request and every `0x0F FC03` request after
  BUS_RETURN.
- Candidate after EXP255, if baseline is clean:
  **EXP256 — one-shot R1 + identical post-R1 FC16/FC03 census, no downstream ACKs/responses.**
- **EXP239 remains OPEN.**
- **EXP238 remains PARKED / NOT RUN.**


## EXP252/254 recovery clarification — 2026-09-27

The heat pump/controller was manually restarted after the `COMM. ERR ONLINE/LINK` alarm from EXP252.

Therefore EXP254 demonstrates **post-reboot recovery to the normal local XTR protocol baseline**.
It does **not** demonstrate that the alarm/session state would have cleared spontaneously without a
controller restart.

The following remain valid:
- EXP252 R1 suppressed all later approval retries in that boot;
- a DHW-side `0` appeared;
- `COMM. ERR ONLINE/LINK` appeared;
- after a subsequent controller restart with no active responder, EXP254 returned to the familiar
  63-request passive approval lifecycle with no `0870/count17` and no `0708/count6`.

UI recovery of the alarm and DHW-side `0` still requires explicit visual confirmation if it was not
recorded at the time.


## Authoritative current state — 2026-09-27 — EXP254 COMPLETE / VALID PASSIVE POSITIVE

- Last completed experiment: **EXP254 — COMPLETE / VALID PASSIVE POSITIVE**.
- EXP254 clean passive recovery summary:
  - approval requests: **63**
  - first request: **+1.283 s**
  - median cadence: **4.241 s**
  - last request: **+265.086 s**
  - exact `FC16 0870/count17`: **0**
  - peer FC16 ACK: **0**
  - exact `FC03 0708/count6`: **0**
  - `s06=107`
  - final state `A80E=0028 A80F=000A AFDC=0010`
  - `resync_delta=0`
  - `drop_delta=0`
  - TX disabled
- All complete passive retry runs (EXP248, 249, 251, 254) stop at exactly **63 requests**, despite
  differing cadence and elapsed duration. The fixed 63-attempt budget remains the leading model.
- With EXP254 median cadence, a nominal 64th request would fall around +269.327 s, before +270 s,
  but does not appear.
- **Material refinement of EXP252 interpretation:** the late A80E/AFDC fall-back is not R1-specific.
  EXP254 reproduces it passively at almost the same boot age:
  - A80E `0x28 -> 0x20` at ~+642.650 s in EXP254 vs ~+647.433 s in EXP252
  - AFDC `0x10 -> 0x00` at ~+646.459 s in EXP254 vs ~+651.106 s in EXP252
- Therefore the R1-specific evidence from EXP252 is now narrowed to:
  1. immediate suppression of all later approval retries;
  2. front-panel DHW-side `0`;
  3. `COMM. ERR ONLINE/LINK`.
- Exact `0870/count17` and `0708/count6` do not occur in the 7-minute local passive XTR baseline.
  Do not copy the reference ATEC/DHP-AQ `0870 -> 0708 -> sync` sequence onto XTR without direct
  local evidence.
- Next candidate: **EXP255 — one-shot R1 + post-R1 FC16/FC03 address census, no downstream ACKs**.
- Safety prerequisite before EXP255: user confirms that `COMM. ERR ONLINE/LINK` and the DHW-side `0`
  cleared after the EXP254 passive recovery reboot.
- **EXP239 remains OPEN.**
- **EXP238 remains PARKED / NOT RUN.**


## EXP254 provisional live result — 2026-09-27 — RUNNING

- EXP254 is behaving as intended: fully passive / RX-only.
- A genuine controller-off bus gap and BUS_RETURN were observed.
- After BUS_RETURN the local XTR returned to the known unanswered approval lifecycle:
  - first `071C/0730` request at +1.283 s;
  - 23 requests observed so far through +94.787 s;
  - recent cadence ~4.240 s.
- Controller state progression returned to the familiar pattern:
  - A80E `0x28 -> 0x00 -> 0x08 -> 0x28`;
  - A80F `0x0A -> 0x05 -> 0x0A`;
  - AFDC `0x10 -> 0x00 -> 0x10`.
- So far:
  - exact `0x0F FC16 0870/count17` requests: **0**;
  - exact `0x0F FC03 0708/count6` polls: **0**;
  - peer FC16 ACKs: **0**.
- This already supports clean recovery toward the local XTR baseline and shows that the reference
  ATEC/DHP-AQ `0870/0708` service cycle is not ordinary early local XTR baseline traffic.
- EXP254 remains **RUNNING** until `SUMMARY PASSIVE_RECOVERY_COMPLETE`.


## Authoritative current state — 2026-09-27 — EXP253 COMPLETE / EXP254 PREPARED

- Last completed experiment: **EXP253 — COMPLETE / OFFLINE POST-APPROVAL SESSION RECONSTRUCTION**.
- Last completed live-bus experiment: **EXP252 — COMPLETE / ACTIVE POSITIVE / COMM. ERR ONLINE/LINK SIDE EFFECT**.
- Current prepared experiment: **EXP254 — PASSIVE RECOVERY + 0870 BASELINE CENSUS — PREPARED / NOT RUN**.

### EXP253 material finding

Reference established Online/DCM captures show a concrete endpoint-coming-online transition:

1. controller repeatedly sends `0x0F FC16 0870/count17` with no reply;
2. controller repeatedly polls `0x0F FC03 0708/count6` with no reply;
3. endpoint first ACKs `0870/count17`;
4. endpoint then answers `0708` with `0000 0000 7FFF FFFF 0080 0007`;
5. controller immediately begins a broad FC16 synchronization burst (`03E8`, `03FC`, `0884`, ...),
   with each block ACKed by the endpoint.

In capture 090550 there are 31 unanswered `0870/count17` requests and 16 unanswered `0708` polls
before this transition.

Established idle/service captures show recurring `0708` responses ending in `...0006`, including
`0000 0000 0000 0000 077F 0006` and all-zero-like variants.

### EXP252 interpretation refined

EXP252's R1 is not simply ignored: it suppresses the local approval retries. However the ESP supplied
none of the downstream endpoint duties seen in the reference topology: no FC16 ACKs and no read-side
service/mailbox responses. The later `COMM. ERR ONLINE/LINK` is therefore consistent with an
**incomplete Online/Link endpoint/session**.

This does not prove that local XTR uses the same post-approval sequence as the reference ATEC/DHP-AQ
topology.

### Safety / next step

No further active response is approved until clean passive recovery is documented.

EXP254 is fully RX-only and will establish:
- whether the alarm and DHW-side `0` clear on a normal no-responder boot;
- whether local `0870/count17` is baseline traffic;
- whether any local `0708/count6` poll occurs without active endpoint behavior;
- whether the normal 63-attempt approval lifecycle returns.

**EXP239 remains OPEN.**
**EXP238 remains PARKED / NOT RUN.**


## Authoritative current state — 2026-09-27 — EXP252 COMPLETE / ACTIVE POSITIVE / ALARM SIDE EFFECT

- Last completed experiment: **EXP252 — COMPLETE / ACTIVE POSITIVE / SAFETY SIDE EFFECT OBSERVED**.
- One mismatched externally reported Eco 5 R1 response was transmitted exactly once at the first
  local XTR `071C/0730` approval request.
- Result:
  - approval requests: **1**;
  - retries after TX: **0**;
  - no second approval request for the complete 7-minute observation;
  - `peer17=0`;
  - controller FC16 requests: **386**;
  - peer FC16 ACKs: **0**;
  - `mailbox0708=0`;
  - other FC03 page reads: **0**;
  - parser resync after BUS_RETURN: **0**;
  - RX drops after BUS_RETURN: **0**;
  - DE returned LOW.
- **Strong conclusion:** R1 is not simply ignored. It terminates/suppresses the local approval retry
  state, but full DCM/Online approval is **not proven** because no downstream peer ACK/mailbox phase
  appears.
- New controller-visible side effects:
  - front-panel displayed a new literal `0` beside the DHW/tank icon;
  - after the experiment summary, A80E fell `0x28 -> 0x20 -> 0x00` and AFDC fell `0x10 -> 0x00`;
  - the user subsequently reported a front-panel alarm.
- Alarm text is now known: **`COMM. ERR ONLINE/LINK`**.
- **Safety hold:** no further active `0730` response experiments until a normal passive/no-responder
  boot is shown to restore normal operation. The alarm is specifically an Online/Link communication
  error, not currently evidence of a direct heating/DHW process fault.
- Next evidence required: verify that `COMM. ERR ONLINE/LINK` and the DHW-icon `0` clear after return
  to passive/no-responder operation.
- **EXP239 remains OPEN.**
- **EXP238 remains PARKED / NOT RUN.**


## EXP252 provisional UI observation — 2026-09-27

After the single R1 `0730` oracle response, the local Thermia front-panel display visibly shows a
literal `0` immediately beside/above the domestic-hot-water tank icon. The display otherwise reads
`KAMER`, `GEEN WARMTEVRAAG`, and `BEDRIJF AUTO`; no alarm/fault text is visible in the supplied photo.

This UI change is temporally associated with the one-shot R1 response and the immediate suppression
of further `071C/0730` approval retries, but its semantic meaning is **unknown**. It must not yet be
interpreted as `0 °C`, a changed DHW setpoint, or proof of successful DCM approval.

The visual formatting does not clearly show a temperature unit next to the `0`, so a status/index/
service indicator remains plausible.

Do not perform another active response test before the EXP252 run is complete and the display state
has been correlated with the final bus trace.


## Authoritative current state — 2026-09-27 — EXP252 PREPARED / NOT RUN

- Last completed experiment: **EXP251 — COMPLETE / VALID RX-ONLY POSITIVE**.
- Current prepared experiment: **EXP252 — ONE-SHOT 0730 APPROVAL ORACLE (Eco 5 R1) — PREPARED / NOT RUN**.
- EXP252 hypothesis: one externally reported genuine Eco 5 response, returned exactly once to the
  first local XTR approval request, will either be rejected with retries continuing or measurably
  alter the controller approval/session state.
- New active response target:
  - controller FC17 reads `0x0730..0x0737`;
  - test payload `R1 = 1691 A5F3 F8E8 D587 3892 4416 E8E6 A3D5`;
  - R1 belongs externally to `C1 = 63CE FB32 C6F4 1382 0879 9237 0CAC EEBA`;
  - local XTR input is an RTC/service image and does not match C1, so this is deliberately a
    mismatched cross-profile oracle test.
- Possible effects before test:
  - likely rejection / retries continue;
  - possible retry suppression or approval/session state change;
  - possible partial DCM sync;
  - persistent service/binding side effects unknown.
- Fail-closed guards require:
  - explicit HA arm;
  - real cold-boot bus gap and return;
  - first exact approval request only;
  - proven local RTC/service serializer;
  - input must not equal C1;
  - `A80E=0000`, `A80F=0005`;
  - no peer FC17 response;
  - no post-BUS_RETURN parser resync or RX drop before TX.
- TX latch closes before driver enable. There is exactly one `write_array()` path in the YAML.
- After R1, no further Thermia response is emitted: no retry, FC16 ACK, mailbox response or
  desired-state page response.
- GPIO17 TX is enabled only for EXP252. GPIO21 DE defaults LOW and is returned LOW after the frame,
  abort and final summary.
- **EXP239 remains OPEN.**
- **EXP238 remains PARKED / NOT RUN.**
- Do not run a second active response value in the same boot.


## Authoritative current state — 2026-09-27 — EXP251 COMPLETE / VALID RX-ONLY POSITIVE

- Last completed experiment: **EXP251 — COMPLETE / VALID RX-ONLY POSITIVE**.
- EXP251 final summary:
  - approval requests: **63**;
  - first request: **+1.287 s** after BUS_RETURN;
  - median cadence: **4.178 s**;
  - last request: **+261.347 s**;
  - final target-free silence: **80.044 s**;
  - peer FC17 16-byte responses: **0**;
  - controller FC16 requests: **424**;
  - peer FC16 ACKs: **0**;
  - `0x0F FC03 0708/count6` mailbox requests: **0**;
  - other FC03 page requests: **0**;
  - 0x06 polls: **87**;
  - final state: `A80E=0028 A80F=000A AFDC=0010`;
  - false stops: **0**;
  - parser resync delta: **1** at the boot-return edge;
  - RX drop delta: **0**;
  - TX: **DISABLED**.
- Comparison across complete cold boots:
  - EXP248: 63 requests, median 4.298 s, last +267.123 s;
  - EXP249: 63 requests, median 4.293 s, last +266.821 s;
  - EXP251: 63 requests, median 4.178 s, last +261.347 s.
- **Material protocol conclusion:** a simple fixed ~270 s deadline is now weakened. The **fixed
  63-attempt retry-budget model is the leading explanation** because the count remains invariant
  while cadence and total elapsed window change.
- At EXP251 cadence, nominal attempts 64 and 65 would fall at approximately +265.525 s and +269.703 s,
  both before +270 s, yet neither occurs.
- Ordinary controller FC16 requests are present without any approval response, peer FC16 ACK, or
  0708 mailbox. Therefore controller-originated FC16 traffic alone is not evidence of Online/DCM approval.
- No active `0730` response was sent, derived or approved.
- **EXP239 remains OPEN.**
- **EXP238 remains PARKED / NOT RUN.**
- Do not spend another live experiment on retry timing unless new evidence requires it.
- Candidate next step: one-shot active approval-oracle test using a single known external Eco 5
  response, but only after explicit approval because `0730..0737` remains semantically opaque.


## Authoritative current state — 2026-09-27 — EXP251 VALID STOP CANDIDATE / FINAL CONFIRMATION PENDING

- Last completed experiment: **EXP250 — COMPLETE / OFFLINE / NO TX**.
- Last completed live-bus experiment: **EXP249 — COMPLETE / VALID PASSIVE POSITIVE**.
- Current experiment: **EXP251 — VALID RX-ONLY RUN / STOP CANDIDATE OBSERVED / NOT YET FORMALLY COMPLETE**.
- EXP251 observed:
  - first approval request **+1.287 s** after BUS_RETURN;
  - **63 approval requests**;
  - median cadence **4178 ms**;
  - last request **+261.347 s**;
  - final monitored state `A80E=0028 A80F=000A AFDC=0010`;
  - no peer FC17 16-byte response;
  - no peer FC16 ACK;
  - no `0x0F FC03 0708/count6` mailbox request;
  - STOP_CANDIDATE after **20.044 s** approval silence while ordinary bus traffic remained alive;
  - one parser resync exactly at bus return; RX drops remained zero.
- **Material model change:** EXP248/249 had ~4.29 s median cadence and final requests at ~267 s,
  while EXP251 has a ~4.178 s median cadence and final request at **261.347 s**, yet all three runs
  still stop after exactly **63 requests**.
- A simple fixed ~270 s deadline from BUS_RETURN is therefore materially weakened.
- **Leading hypothesis is now a fixed 63-attempt retry budget**, with total retry-window duration
  determined by actual scheduler/bus cadence.
- At EXP251 cadence, nominal request 64 would be due around **+265.525 s** and request 65
  around **+269.703 s**, both before +270 s.
- No active `0730` response was sent, derived or approved.
- Formal EXP251 completion still requires the missing 60 s post-STOP_CANDIDATE tail /
  `SUMMARY SHADOW_COMPLETE`.
- **EXP239 remains OPEN.**
- **EXP238 remains PARKED / NOT RUN.**


## Authoritative current state — 2026-09-27 — EXP251 PREPARED / NOT RUN

- Last completed experiment: **EXP250 — COMPLETE / OFFLINE / NO TX**.
- Last completed live-bus experiment: **EXP249 — COMPLETE / VALID PASSIVE POSITIVE**.
- Current prepared experiment: **EXP251 — SHADOW DCM / APPROVAL HARNESS — PREPARED / NOT RUN**.
- EXP251 hypothesis: the iTec Online/DCM lifecycle can be implemented as a shadow state-machine with
  one deliberately unresolved opaque 16-byte `071C -> 0730` response boundary.
- Only experimental change: EXP249 retry-window instrumentation is replaced by lifecycle/classifier
  instrumentation. Known-good production functionality is preserved.
- EXP251 recognizes:
  - exact `0x0F FC17 read0730/count8 + write071C/count8` approval requests;
  - local XTR RTC/service consistency and reference-challenge Hamming distance;
  - unexpected peer 16-byte FC17 responses;
  - controller 0x0F FC16 requests and peer FC16 ACKs;
  - exact `0x0F FC03 0708/count6` mailbox polls;
  - other 0x0F FC03 page reads;
  - A80E/A80F/AFDC and 0x06 context.
- **No Thermia TX path exists in the EXP251 build:** GPIO17 TX is absent and GPIO21 DE is forced LOW.
- No Eco 5 response bytes are stored in the YAML; only the two source challenge values are used for
  Hamming-distance comparison.
- Experimental controls remain under Home Assistant Configuration and logs retain the red/brown
  convention.
- **EXP239 remains OPEN.**
- **EXP238 remains PARKED / NOT RUN.**
- No active `0730` response is approved.
- Do not move to an active one-shot oracle test until EXP251 has completed cleanly and been analysed.


## Authoritative current state — 2026-09-27 — EXP250 COMPLETE / OFFLINE

- Last completed experiment: **EXP250 — COMPLETE / OFFLINE 0730 RESPONSE-STRUCTURE CLASSIFICATION**.
- Hypothesis tested: the two externally reported genuine Eco 5 `0730..0737` responses behave more
  like one opaque 128-bit approval/authenticator value than eight independent status/control words.
- Across the two available genuine response blocks:
  - all 8/8 16-bit word positions change;
  - no response word position is fixed;
  - no common small Thermia status/control constants appear;
  - C->R Hamming distances are 65/128 and 62/128;
  - R1->R2 Hamming distance is 68/128.
- **Strong conclusion:** for emulator design, `0730..0737` should currently be treated as one opaque
  16-byte response blob. There is no evidence-backed per-word semantic map.
- This does not prove a specific cryptographic primitive and does not prove XTR M uses the same
  response function as the reported Eco 5.
- Safety consequence: the result weakens the 'eight independent flags' interpretation but does not
  make arbitrary replay safe. Persistent session/binding side effects remain unknown.
- No Thermia TX occurred in EXP250. Production functionality is unchanged.
- **EXP249 remains the last completed live-bus experiment.**
- **EXP239 remains OPEN.**
- **EXP238 remains PARKED / NOT RUN.**
- Preferred next step: build **EXP251 shadow DCM emulator/oracle harness** with TX disabled by default.
  Any later active one-shot `0730` replay requires explicit approval and must use only one response in
  one boot with immediate TX hard-disable afterward.


## Authoritative current state — 2026-09-27 — EXP249 COMPLETE / VALID PASSIVE POSITIVE

- Last completed experiment: **EXP249 — COMPLETE / VALID PASSIVE POSITIVE**.
- EXP249 repeated EXP248's RX-only cold-boot natural-stop trace with only one changed variable: a second controller cold boot.
- EXP249 result:
  - first target **+1.283 s** after BUS_RETURN;
  - **63 targets**;
  - median cadence **4293 ms**;
  - last target **+266.821 s**;
  - final monitored state `A80E=0028 A80F=000A AFDC=0010`;
  - `SUMMARY CONFIRMED_STOP` after **80.974 s** final target silence;
  - 87 observed 0x06 polls;
  - `false_stops=0`, `resync_delta=0`, `drop_delta=0`.
- EXP248 comparison:
  - first target was also +1.283 s;
  - target count was also 63;
  - last target was +267.123 s;
  - last-target difference is only **302 ms**;
  - final monitored state is identical;
  - meaningful early A80E/A80F/AFDC state transitions reproduce within **11 ms**.
- **Strong conclusion:** the unanswered local XTR `071C/0730` startup/service lifecycle is highly deterministic across repeated cold boots.
- A ~270 s fixed deadline remains the leading practical model, but a fixed 63-request budget is still equally compatible because cadence and phase are also nearly identical.
- Do **not** claim that 270.000 s is proven or that the mechanism is definitively time-based.
- No active `0730` response was sent, derived or approved.
- **EXP239 remains OPEN.**
- **EXP238 remains PARKED / NOT RUN.**
- Preferred next experiment: **EXP250 — passive cutoff-neighborhood raw-frame differential**, using the deterministic ~267 s stop to capture every CRC-valid bus frame around ~245–285 s and search for an externally visible event that suppresses the next target slot.


## Authoritative current state — 2026-09-27 — EXP249 PREPARED / NOT RUN

- Last completed experiment: **EXP248 — COMPLETE / VALID PASSIVE POSITIVE**.
- Current prepared experiment: **EXP249 — PASSIVE 071C/0730 STOP REPEATABILITY TRACE — PREPARED / NOT RUN**.
- EXP249 hypothesis: the EXP248 natural stop is governed primarily by a repeatable approximately 270 s startup/service window. A second otherwise-identical RX-only cold boot should reproduce the final target within one normal retry interval (~4.3 s) of EXP248's +267.123 s result.
- EXP248 comparison baseline:
  - first target +1.283 s after BUS_RETURN;
  - 63 targets;
  - median cadence 4.298 s;
  - last target +267.123 s;
  - monitored stop state `A80E=0028 A80F=000A AFDC=0010`;
  - confirmed target-free silence 80.793 s.
- **Only experimental variable:** one additional controlled Thermia/controller cold boot. All EXP248 observation thresholds and RX-only behavior are retained.
- EXP249 contains no Thermia TX path: GPIO17 TX remains unconfigured and GPIO21 DE is forced LOW.
- No ACK, `0730` response, scan, semantic write, setting change, room-sensor emulation or production-function change is introduced.
- Experimental controls remain under Home Assistant Configuration; experiment logs retain the red/brown convention.
- **EXP239 remains OPEN.**
- **EXP238 remains PARKED / NOT RUN.**
- No active `0730` response is approved.
- Do not mark EXP249 complete until the automatic `SUMMARY CONFIRMED_STOP` (or a clearly recorded censor/abort) is present in the returned log.


## Authoritative current state — 2026-09-27 — EXP248 COMPLETE / VALID PASSIVE POSITIVE

- Last completed experiment: **EXP248 — COMPLETE / VALID PASSIVE POSITIVE**.
- Hypothesis tested: the local XTR `0x0F FC17 read 0730/count8 + write 071C/count8`
  startup/service transaction retries for a finite unanswered window and then stops naturally.
- Attempt 1 was an intentional/accidental setup negative: armed at 14:55:38.670 but no controller
  power-cycle occurred; the >=6 s boot-gap guard correctly auto-aborted after 60 s. No protocol
  conclusion is drawn from that attempt.
- Attempt 2 is valid and complete:
  - ARM 14:57:25.491;
  - boot gap detected 14:57:53.961;
  - BUS_RETURN 14:58:01.042;
  - first target +1.283 s;
  - **63 targets total**;
  - last target **+267.123 s** with `A80E=0028 A80F=000A AFDC=0010`;
  - stable target cadence, median **4298.0 ms**;
  - STOP_CANDIDATE after 20.793 s target silence;
  - `SUMMARY CONFIRMED_STOP` with **80.793 s final silence**, **0 false stops**,
    **0 resync delta**, **0 RX-drop delta**, and **86 observed 0x06 polls**.
- Ordinary bus traffic remains alive after the final `071C/0730`; therefore the target stream
  stops naturally rather than disappearing because of bus loss.
- No A80E/A80F/AFDC transition coincides with the final target; monitored state stays
  `0028 / 000A / 0010`.
- No cadence slowdown/backoff is visible before the stop.
- Strong timing hypothesis: an approximately **270 s startup retry deadline**. The next target would
  normally be due around **271.421 s**, so a ~270 s deadline lies naturally
  between target 63 and the suppressed target 64. This is not yet proven from one run.
- No active `0730` response was sent, derived or approved. Production functionality is unchanged.
- **EXP239 remains OPEN** pending the external genuine iTec Eco 5 raw capture.
- **EXP238 remains PARKED / NOT RUN.**
- Preferred next experiment: **EXP249 — passive repeatability test of the ~270 s natural-stop
  deadline**, using the same RX-only instrumentation and one additional cold boot.



## Authoritative current state — 2026-09-27 — EXP248 VALID STOP CANDIDATE / CONFIRMATION TAIL MISSING

- Current experiment: **EXP248 — IN PROGRESS / VALID RX-ONLY RUN; natural-stop candidate observed, but the configured 60 s confirmation window is not fully present in the supplied log tail**.
- Hypothesis remains: after one XTR controller cold boot with no genuine Online/DCM endpoint, exact `0x0F FC17 read 0730/count8 + write 071C/count8` retries for a finite startup/service window and then stops naturally.
- First arm attempt at 14:55:38 auto-aborted correctly because no controller power-cycle / >=6 s bus gap occurred; it carries no protocol result.
- Valid second attempt: bus gap detected at 14:57:53.961; `BUS_RETURN` at 14:58:01.042.
- First target: `n=1`, `since_return=1283 ms`, state `A80E=0000 A80F=0005 AFDC=0000`.
- Early state progression: `A80E 0000->0008` at 1761 ms, `A80E 0008->0028` at 2858 ms, `AFDC 0000->0010` at 5583 ms, `A80F 0005->000A` at 11278 ms. None stops the retry stream.
- Target stream reaches **63 requests**. Last observed exact target is `n=63` at **267123 ms after BUS_RETURN** with `A80E=0028 A80F=000A AFDC=0010`; preceding cadence remains ~4.29 s with no slowdown/backoff.
- The next expected target does not appear. EXP248 raises `STOP_CANDIDATE` after **20793 ms silence** while the ordinary bus remains active, with the same monitored state `A80E=0028 A80F=000A AFDC=0010`.
- Supplied tail contains no `FALSE_STOP` and no further target; `EXP248 Last Target Age` reaches at least **53.5 s** while controller/0x06/outdoor traffic remains live. Parser remains clean (`resync=0`, `drops=0`).
- **Important:** the experiment success criterion requires another 60 s after `STOP_CANDIDATE`. The supplied file ends about 33.7 s after that marker, therefore `SUMMARY CONFIRMED_STOP` is not present and EXP248 must not yet be marked COMPLETE.
- Provisional strong interpretation: the local XTR retry stream appears to terminate abruptly at ~267.1 s (~4 min 27.1 s) after bus return, without a bus outage or visible A80E/A80F/AFDC transition. A fixed ~270 s timer or fixed retry budget is now a plausible hypothesis, not yet proven.
- No active `0730` response was sent or approved. Production functionality is unchanged.
- Minimal missing evidence: if available, provide only the log tail from about **15:03:22 through 15:03:50+**. A rerun is not needed if that tail still exists.


## Authoritative current state — 2026-09-27 — EXP248 PREPARED / NOT RUN

- Current experiment: **EXP248 — PREPARED / PASSIVE 071C/0730 NATURAL-STOP TRACE; not yet run**.
- Hypothesis: after one XTR controller cold boot with no genuine Online/DCM endpoint, the exact `0x0F FC17 read 0730/count8 + write 071C/count8` service/approval slot retries for a finite window and then stops naturally; the immediate `A80E/A80F/AFDC` state around the final retry may identify the stop condition.
- EXP247 established only a bound on one historical passive boot: target still active at ~198 s after Bus Healthy and already absent by ~1600 s. The exact stop lies inside a logging gap.
- **Only experimental variable:** one controlled Thermia/controller cold boot. No heat-pump setting is changed.
- EXP248 is fully RX-only: GPIO17 TX is not configured; GPIO21 DE remains LOW; no ACK, FC17 response, probe, scan, semantic write, room-sensor emulation or automated controller restart exists.
- Home Assistant experimental controls are under Configuration: `EXP248 Arm RX-only Timeout Trace` and `EXP248 Abort`.
- Guarding/measurement:
  - ARM requires fresh bus traffic and >=15 s ESP uptime;
  - after ARM, a genuine >=6 s bus gap must be observed within 60 s;
  - first CRC-valid frame after that gap defines bus return;
  - every exact 071C/0730 target is logged with 16-byte `W071C` image and current A80E/A80F/AFDC snapshot;
  - >=20 s target silence is accepted as a stop candidate only while the rest of the bus remains live;
  - EXP248 then requires another 60 s without a target before confirming the stop; any target reappearance cancels the candidate and is recorded as `FALSE_STOP`;
  - hard observation ceiling is 35 min after bus return.
- Success criterion: `SUMMARY CONFIRMED_STOP` with >=3 target frames, clean parser counters, a final target time and a 60 s target-free confirmation window while ordinary bus traffic remains alive.
- Stop/inconclusive criteria: no >=6 s boot gap within 60 s of ARM, fewer than 3 target frames, parser/buffer corruption, or `SUMMARY CENSORED_35MIN`.
- **EXP239 remains OPEN** pending the external genuine iTec Eco 5 raw capture.
- **EXP238 remains PARKED / NOT RUN.**
- No active `0730` response is approved.


## Authoritative current state — 2026-09-27 after EXP247

- Last completed experiment: **EXP247 — COMPLETE / OFFLINE: natural XTR `071C/0730` disappearance is proven, but exact timeout is not recoverable from the current right-censored captures**.
- Current experiment: **none running**.
- **EXP239 remains OPEN** pending the external genuine iTec Eco 5 Online raw capture.