# EXP257 — Final analysis

Status: **COMPLETE / STRONG POSITIVE**

## Hypothesis

After the same one-shot R1 used in EXP256, acknowledge exactly the first post-R1 `0x0F FC16 03E8/count14` request once and capture the first different FC16/FC03 stage without answering it.

The full genuine Eco 5 capture predicted `03FC/count11`.

## Observed facts

- `BUS_RETURN` was detected cleanly.
- First approval request: +1285 ms after BUS_RETURN.
- One R1 was transmitted.
- First post-R1 FC16: `03E8/count14`, +130 ms after R1.
- One standard FC16 ACK was transmitted: `0F1003E8000EC093`.
- First different request: `03FC/count11`, +691 ms after ACK.
- Exact request: `0F1003FC000B160028000A0037000000000000000200120028001E003C369E`.
- Payload words: `0028 000A 0037 0000 0000 0000 0002 0012 0028 001E 003C`.
- No `03FC` ACK was sent.
- No approval retry after R1.
- No same-`03E8` retry after ACK.
- No unexpected peer FC17 / FC16 ACK.
- Post-return parser resync delta 0; RX-drop delta 0; DE LOW.

## Strong conclusions

1. EXP257 is a positive result.
2. The local XTR exactly reproduces the genuine Eco 5 prefix `R -> 03E8/14 -> ACK -> 03FC/11`.
3. The one standard `03E8` ACK is sufficient to advance the XTR one native synchronization block.
4. Together EXP256 + EXP257 strongly support that the replayed R1 enters the real Online/Link synchronization state machine.
5. Full session establishment remains unproven.

## Hypotheses

- A future single exact ACK to `03FC/count11` may advance the XTR to `0410/count22`, matching the genuine Eco 5 reference.
- If that reproduces, subsequent blocks may follow the same ordered controller-export chain.

## Unknowns

- Whether the local XTR follows the complete Eco 5 sync chain.
- Whether/when local `0708/count6` mailbox traffic begins.
- Whether additional authentication/session semantics appear later.
- Front-panel side effect for EXP257, pending user report.

## Safety

EXP257 sent no semantic register-value write. The only new active frame was a standard FC16 ACK echoing start/count. The test stopped before acknowledging `03FC`.

Perform one normal controller reboot after the capture if not already done.