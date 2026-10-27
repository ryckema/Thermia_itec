# S11F / 0884 runtime-transition analysis — 2026-10-07

## Scope

Offline correlation of:
- local XTR S11F result;
- genuine iTec Eco gateway captures;
- genuine ATEC/DCM03 capture;
- current native 0x0F runtime model.

No secret approval material is included.

## Local XTR S11F

Fresh-session progression reached:

```text
FC23 approval
-> 32/32 settings bootstrap
-> bounded 0708/6 mailbox service
-> runtime
-> 0864/4
-> 0870/17
-> qualified ACK0870
-> one 0708/6 response
-> 0884/60
```

First 0884 appeared about 2.04 s after ACK0870. All ESP TX stopped at first 0884. Repeated 0884 publications continued afterwards.

The run therefore proves the combined qualified-session path to 0884. It does not isolate ACK0870 from the one intervening mailbox response.

## Genuine 0884 request/ACK corpus

Current raw files with explicit controller 0884/count60 requests and matching gateway ACKs:

| capture | explicit 0884 requests | ACKed | normal ACK0884->0708->07D0 chains |
|---|---:|---:|---:|
| thermia_capture_20260925_090550.log | 1 | 1 | 0 |
| thermia_capture_20260925_071517.log | 4 | 4 | 4 |
| itec_eco5_gateway_20260926.log | 1 | 1 | 1 |
| thermia_capture_20260925_090209.log | 1 | 1 | 0 |
| thermia_capture_20260924_210001(1).log | 2 | 2 | 2 |
| thermia_capture_20261003_165355.log | 12 | 12 | 12 |
| **total** | **21** | **21** | **19** |

Two non-normal comparators:
- one 0884 ACK is followed by settings/bootstrap traffic;
- one capture ends before useful follow-on traffic.

For the 19 normal cycles:

```text
0884 -> 0708:
  min     1.253 s
  median  1.277 s
  max     3.534 s

0884 -> 07D0:
  min     1.979 s
  median  2.010 s
  max     4.578 s
```

## Interpretation

**Observed / genuine:** normal gateway traffic commonly ACKs 0884 and then resumes at 0708 followed by the runtime ring beginning at 07D0.

**Observed / local XTR:** after S11F stops at 0884, the local controller repeatedly republishes 0884 and continues 0708 polling.

**Strong conclusion:** 0884 behaves like a history/runtime overlay completion point whose acknowledgement is normally followed by another runtime cycle.

**Open:** whether one retained ACK0884 alone, after an ESP restart and without answering 0708, is sufficient to release the local XTR into 07D0.

## S11G discriminator

S11G is prepared as a no-controller-reboot retained probe:
- ESP-only OTA/restart;
- observe >=3 exact 0884/60 and >=2 exact 0708/6 with clean parser and zero TX;
- one standard FC16 ACK to the next 0884/60;
- no mailbox response and no other ACK;
- positive if 07D0/19 appears within 10 s;
- negative only for the isolated ACK-only hypothesis if live 0884/0708 continues for >=10 s without 07D0;
- unexpected/new traffic or integrity failure -> inconclusive/abort.

Hard active-TX maximum: 1.
