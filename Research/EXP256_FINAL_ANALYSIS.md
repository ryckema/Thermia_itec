# EXP256 — Final analysis

Status: **COMPLETE / ACTIVE STRONG POSITIVE**

## Hypothesis

Repeat the already-tested one-shot Eco 5 R1 response on the first exact local `0x0F FC17 read 0730/count8 + write 071C/count8` approval request, then enumerate every post-R1 FC16/FC03 family without providing downstream ACKs or responses.

The leading pre-run hypothesis was selective suppression of passive `085F/count5` while `04A6/count13` remained.

## Observed facts

- BUS_GAP >= 6 s was detected and the controller returned cleanly.
- First approval request occurred at **+1245 ms after BUS_RETURN**.
- Local `W071C`: `1A144532F9060CACDC1BC590001E8F64`.
- Exactly one R1 response was transmitted:
  `0F17101691A5F3F8E8D58738924416E8E6A3D5E227`.
- DE returned LOW and the one-shot TX latch remained closed.
- Approval requests: **1**.
- Approval retries after TX: **0**.
- FC16 requests: **390**.
- FC16 ACKs: **0**.
- FC03 `0708/count6`: **0**.
- Other FC03: **0**.
- Peer FC17 responses: **0**.
- Complete FC16 family census:
  - `04BA/count22`: **1**, boot-only, before R1.
  - `03E8/count14`: **389**.
  - `04A6/count13`: **0**.
  - `085F/count5`: **0**.
- First `03E8/count14`: **+1369 ms after BUS_RETURN / +124 ms after R1**.
- Last `03E8/count14`: **+419896 ms after BUS_RETURN**.
- Post-return parser resync delta: **0**.
- Post-return RX drop delta: **0**.
- Final controller context: `A80E=0028 A80F=000A AFDC=0010`.
- Front panel: DHW/tank-side literal **`0`** reappeared.
- VERSION screen: **no change**.
- After the run the controller raised **`COMM. ERR ONLINE/LINK`**, exactly matching EXP252.

## Strong conclusions

1. The pre-run selective-`085F` hypothesis is rejected.
2. R1 is not merely ignored and is not merely suppressing one passive FC16 family.
3. R1 advances the controller out of the `071C/0730` approval retry state into the native acknowledged `0x0F` synchronization state machine.
4. The first observed post-approval synchronization stage is `03E8/count14`.
5. Because EXP256 deliberately provides no FC16 ACK, the controller stalls and retransmits that first sync block.
6. The `0` + `COMM. ERR ONLINE/LINK` side effect is reproducible across EXP252 and EXP256.
7. No VERSION-screen change is expected from this path; VERSION `EXP` metadata belongs to the separate `0x06/AFD1` expansion path.

## Hypotheses

- The correct endpoint behavior after R1 is to ACK `03E8/count14`, allowing the controller to advance to the next synchronization block.
- EXP252 likely entered the same `03E8` retransmission state, but its instrumentation did not classify the FC16 family.

## Unknowns

- Whether the next block after a single exact `03E8` ACK matches the previously mapped native sync ordering.
- Whether a later FC03/`0708` mailbox phase occurs on this local XTR path.
- Whether the full Online/Link session can be established with the external Eco 5 R1.
- Semantic meaning of the DHW-side literal `0`.

## Safety / next discriminator

Do not broadly ACK FC16 traffic. A future EXP257 should:
- repeat the exact one-shot R1 guard sequence;
- ACK **only** the first exact `03E8/count14` controller request;
- capture the first subsequent controller block;
- do **not** ACK that new block;
- retain fail-closed guards and one-shot latches.

A normal controller reboot is the required recovery action after the incomplete session/alarm.
