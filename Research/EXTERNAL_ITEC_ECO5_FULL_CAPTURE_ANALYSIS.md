# External iTec Eco 5 full gateway capture — analysis

Date analysed: 2026-09-27
Source capture duration: 1482.480 s
Source lines: 10,719

## Key result

The full capture directly proves two successful approval-to-sync transitions. Both show:

`FC17 approval response -> 03E8/14 -> ACK -> 03FC/11 -> ACK -> 0410/22 -> ACK -> ...`

This materially refines the expected EXP257 discriminator: after our one exact `03E8/14` ACK, the genuine Eco 5 reference predicts `03FC/11` as the first different block.

## Approval windows

- window 1: 29 requests, 184.661..303.554 s, median cadence ~4.2425 s; successful C1/R1 at end.
- window 2: 41 requests, 394.976..565.004 s, median cadence ~4.257 s; no response.
- window 3: 29 requests, 604.688..723.223 s, median cadence ~4.213 s; successful C2/R2 at end.
- 98/99 `071C` payloads unique; one duplicate.

## Successful pairs

```text
C1 63CE FB32 C6F4 1382 0879 9237 0CAC EEBA
R1 1691 A5F3 F8E8 D587 3892 4416 E8E6 A3D5

C2 31FB 59FC 8FB1 175C D89F 904D 06D9 2EA4
R2 FD63 6CCD 0F92 1D83 FF23 2A1A 2413 B372
```

## Initial synchronization transfer after R1

Stable proved prefix in both successful gateway sessions:

`03E8/14 -> 03FC/11 -> 0410/22 -> 042E/15 -> 0442/13 -> 0456/12 -> 046A/18 -> 047E/19 -> 0492/11 -> ...`

The transfer continues through `04BA/22`, `04D8/27`, `04F6/14`, `050A/19`, `051E/10`, `0532/18`, `0546/20`, 33-register blocks `055A..06C5`, then `06EA/7`, `06F1/3`, `06F4/19`, and later `07D0/19`, `07E4/17`, `07F8/17`, `080C/18`, `0820/18`, `0834/18`, `0848/23`, `0864/4`.

`04A6/13` and `085F/5` are recurrent passive families overlaid on this traffic. They are ACKed at different phases between power-ups and are not established as mandatory ordered sync steps or approval preconditions.

## EXP257 impact

No active widening is needed. Keep one R1 plus one exact `03E8/14` ACK, then stop on the first different FC16/FC03 request. Only the diagnostic expectation changes from `0410/22` to `03FC/11`.

## Follow-up from public discussion, verified against raw capture

Cold-start timing:
- bus returns: 183.462 s, 393.774 s, 603.478 s;
- first approvals: 184.661 s, 394.976 s, 604.688 s => +1.199/+1.202/+1.210 s;
- successful approval responses: 303.615 s and 723.286 s => +120.153/+119.808 s after bus return;
- middle no-gateway run is interrupted by power-off after ~174 s, so it cannot establish the natural stop deadline.

Before the first power-off, the unit is already in steady state with the gateway connected and no `071C/0730` exchange appears. This supports treating the approval burst as a startup/session-establishment phenomenon.

Mailbox:
- first successful power-up: first `0708/6` at 341.855 s (+158.393 s), unanswered; next at 346.097 s answered;
- second successful power-up: first `0708/6` at 790.306 s (+186.828 s), answered;
- repeated idle response raw frame is `0f030c0000000000000000010000001c88`, i.e. words `0000 0000 0000 0000 0001 0000`;
- later fifth-word sequence includes 988 (`03DC`), 984, 976, 908, 896, 768, 512, then 0.

The public comment's `0100` idle fifth word is therefore a transcription/byte-order mismatch relative to the raw Modbus frame; raw-register representation is `0001`.

Only two approval requests are answered in the whole capture. The single duplicated challenge is unanswered, so the capture cannot determine whether identical challenges yield identical responses or whether response mapping is stable across power cycles.
