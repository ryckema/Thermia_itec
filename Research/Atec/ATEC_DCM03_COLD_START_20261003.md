# ATEC + classic DCM03 complete cold-start capture — 2026-10-03

**Track:** ATEC-COLDSTART-01  
**Status:** COMPLETE / POSITIVE — genuine collaborator capture analysis  
**Capture:** `thermia_capture_20261003_165355.log` supplied in project chat  
**Topology:** Modbus-to-TCP/sniffer already running; DCM03 already powered/listening; then HP powered up  
**Device TX by this project:** none  
**Local XTR experiment state:** unchanged — EXP388 RUNNING / PARTIAL

## Hypothesis

Starting the sniffer before HP power-up while the real DCM03 is already present will expose the native ATEC approval exchange and complete first-session bootstrap that earlier late-start captures could miss.

**Result: positive.**

## Timeline

| Capture time | Event |
|---:|---|
| 26.480 s | first captured bus frame |
| 27.400 s | ATEC -> `0x0F FC17`, read `0730/8`, write `071C/8`, 16-byte challenge |
| 27.429 s | DCM03 -> `0x0F FC17` 16-byte response; latency 29 ms |
| 29.262 s | first controller `FC16 03E8/count13` configuration page |
| 61.461 s | terminal bootstrap page `FC16 06F4/count19` |
| 61.529 s | `FC16 085F/count5` all-zero overlay |
| 64.923 s | first `FC03 0708/count6` mailbox poll |
| 64.948 s | DCM03 mailbox `0000 0000 0000 0000 07FF 0006` |
| 111.327 s | non-zero mailbox `0001 0000 0000 0000 077F 0006` |
| 111.366 s | controller -> `FC03 0546/count20` |
| 111.423 s | DCM03 -> complete 20-word `0546` desired image |

## Exact approval pair

Request including CRC:
```text
0f1707300008071c0008102ee156572b8b84a0bc7a65c72d56185d7840
```

Response including CRC:
```text
0f171020b8f28a236f28fa0339669e2c6f600d57d9
```

Challenge body: `2ee156572b8b84a0bc7a65c72d56185d`  
Response body: `20b8f28a236f28fa0339669e2c6f600d`

The response begins 29 ms after request. Only one `0x0F` approval challenge occurs in the five-minute capture.

## Initial configuration bootstrap

The controller publishes all 32 indexed configuration pages and receives the ordinary FC16 address/count ACK for each:

| Index | Page | Count |
|---:|---:|---:|
| 0 | 03E8 | 13 |
| 1 | 03FC | 11 |
| 2 | 0410 | 21 |
| 3 | 042E | 15 |
| 4 | 0442 | 13 |
| 5 | 0456 | 12 |
| 6 | 046A | 18 |
| 7 | 047E | 19 |
| 8 | 0492 | 9 |
| 9 | 04A6 | 13 |
| 10 | 04BA | 22 |
| 11 | 04D8 | 27 |
| 12 | 04F6 | 14 |
| 13 | 050A | 19 |
| 14 | 051E | 9 |
| 15 | 0532 | 18 |
| 16 | 0546 | 20 |
| 17 | 055A | 33 |
| 18 | 057B | 33 |
| 19 | 059C | 33 |
| 20 | 05BD | 33 |
| 21 | 05DE | 33 |
| 22 | 05FF | 33 |
| 23 | 0620 | 33 |
| 24 | 0641 | 33 |
| 25 | 0662 | 33 |
| 26 | 0683 | 33 |
| 27 | 06A4 | 33 |
| 28 | 06C5 | 33 |
| 29 | 06EA | 7 |
| 30 | 06F1 | 3 |
| 31 | 06F4 | 19 |

The page index is shared structurally with modern captures, but counts are not identical. Concrete modern-vs-ATEC differences include `03E8 14->13`, `0410 22->21`, `0492 11->9`, and `051E 10->9`.

## Approval -> page-service timing

DCM response: 27.429 s.  
First configuration page: 29.262 s.  
Delta: **1.833 s**.

This directly disproves any universal ~120 s DCM/controller readiness delay.

## Runtime/mailbox

First mailbox response:
```text
W0 W1 W2 W3 W4   W5
0000 0000 0000 0000 07FF 0006
```

Subsequent normal responses predominantly use:
```text
0000 0000 0000 0000 077F 0006
```

Across the five-minute capture there are 65 answered `0708` polls; median request cadence is ~4.199 s.

Runtime/service page shapes observed:
`07D0/19, 07E4/17, 07F8/17, 080C/18, 0820/18, 0834/18, 0848/23, 085F/5, 0864/4, 0870/17, 0884/60`.

## Genuine W0 event

At 111.327 s:
```text
0001 0000 0000 0000 077F 0006
```

Controller immediately requests `0F 03 0546 0014`.

Returned words:
```text
0546=0002 0547=0000 0548=0002 0549=0000 054A=0000
054B=0000 054C=0000 054D=0000 054E=0000 054F=0000
0550=0000 0551=0000 0552=0000 0553=0004 0554=0000
0555=0000 0556=0000 0557=0000 0558=0000 0559=0000
```

This is byte-for-byte identical to the earlier controller `FC16 0546/count20` image.

**PROVEN / genuine ATEC + DCM03:** `W0 bit0 -> FC03 desired-page pull 0546/count20`.

**NOT proven:** Operation Mode change. `0553=0004` was already current and no later `FC16 0546` republish occurs.

## 0867 refinement

ATEC `0864/count4` is all-zero, so `0867=0000`. The `0867=0016` value in the older legacy reference corpus is not a universal ATEC/DCM03 identifier.

## Consequences for ATEC-EXP1

ATEC-EXP1 v0.2 is **SUPERSEDED / NOT RUN**.

It cannot be repaired only by changing `03E8/count14` to `count13` because:
1. ATEC is FC17 challenge-gated;
2. its prepared snapshot geometry came from a modern Eco5 refresh rather than this ATEC cold start.

Historical YAML remains for provenance. No replacement HP writer is promoted from this capture alone.

## Next action

ATEC-EXP2 is an isolated DCM03 challenge-compatibility bench experiment. It first replays the exact ATEC challenge as positive control, then—only after control success—tests foreign Eco8 challenges.


---

## 2026-10-07 — repeated 0884 runtime-cycle evidence

Full-file re-analysis of the genuine ATEC/DCM03 cold-start capture finds 12 explicit `0884/count60` controller publications, all 12 followed by the standard DCM03 address/count ACK.

For all 12 normal cycles, the next native service sequence is:

```text
ACK0884
-> 0708/6
-> 07D0/19
```

Timing from the 0884 request across these 12 cycles:

```text
to 0708: 1.253..3.366 s
to 07D0: 1.979..4.578 s
```

Most cycles cluster near ~1.28 s to 0708 and ~2.01 s to 07D0.

The ATEC 0708 response after these cycles carries W4=077F and W5=0006, which is generation/profile-specific and must not be imported as local XTR mailbox semantics.

Classification: **GENUINE ATEC/DCM03 evidence**. The scheduling pattern supports the platform-level 0884 overlay model; mailbox literal values remain generation-specific.
