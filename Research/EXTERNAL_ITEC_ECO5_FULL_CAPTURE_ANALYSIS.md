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

## Initial ordered sync chain after R1

`03E8/14 -> 03FC/11 -> 0410/22 -> 042E/15 -> 0442/13 -> 0456/12 -> 046A/18 -> 047E/19 -> 0492/11 -> 04A6/13 -> 04BA/22 -> 04D8/27 -> 04F6/14 -> 050A/19 -> 051E/10 -> 0532/18 -> 0546/20 -> 055A/33 -> 057B/33 -> 059C/33 -> 05BD/33 -> 05DE/33 -> 05FF/33 -> 0620/33 -> 0641/33 -> 0662/33 -> 0683/33 -> 06A4/33 -> 06C5/33 -> 06EA/7 -> 06F1/3 -> 06F4/19 -> 07D0/19`, then `0708/count6` mailbox/runtime exchange.

## EXP257 impact

No active widening is needed. Keep one R1 plus one exact `03E8/14` ACK, then stop on the first different FC16/FC03 request. Only the diagnostic expectation changes from `0410/22` to `03FC/11`.