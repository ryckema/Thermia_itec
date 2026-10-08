# S11Y-AA..AD — native service/rejoin passive protocol reconciliation (public)

**Date:** 2026-10-08 (late). **Scope:** local XTR M experiments + existing genuine different-model Online/DCM captures and firmware-derived semantics. This document is intentionally **redacted**: no private slave responder implementation, security data, command-mailbox payload/response tooling or speculative writes.

## Experiment ledger

| Experiment | Observed baseline and controlled change | Measured result | Classification |
|---|---|---|---|
| S11T | retained `0662/33 + 085F(0800)`; one qualified ACK0662 | `0708/6` after ~1.422 s | XTR locally positive for this edge |
| S11U FIX1 | retained `085F(0800)+0708`; one qualified answered mailbox poll | all-zero `085F/5` after ~566 ms | XTR locally positive only for this transition |
| S11V FIX1, S11W | same-session generated all-zero `085F`, then one ACK; S11W additionally ACKed `0884/60` | `0884/60` after ~2.35 s; then `07D0/19` after ~2.04 s | XTR locally positive; not universally linear |
| S11B | one ACK `0662` and one ACK `085F` | subsequent `0708`, then `0864/4`; two physical TX | XTR locally observed; pre-TX2 zero words strongly supported |
| S11Y-Y FIX2 | one ACK0662; obsolete TX2 guard | first `085F` zero; no TX2; `0708` continued; no `0864` observed | COMPLETE / INCONCLUSIVE for two-ACK endpoint |
| S11Y-AA | new TX2 all-zero qualification but needs `0662` | post-OTA `085F(0800)+0708` without `0662`; 23:15:21.637 ARM REFUSED `tx=0/0/0` | active PREPARED / NOT RUN; ARM attempt inconclusive |
| S11Y-AB | offline comparison with older local paths and Connect timers | retained/rejoin explains observations; no mandatory `0662` timeout established | offline positive, no live protocol test |
| S11Y-AC | offline original S11B event ordering + real Eco5/ATEC captures | 321 `085F` requests all-zero, 10 ACK; first-owner branch sometimes `0864`, sometimes `07D0` | offline positive; DCM evidence cross-model |
| S11Y-AD | conservative log context model and synthetic failure cases | 9/9 offline checks pass; no TX authority ever granted | offline positive, not compiled/live |

## Conservative passive state labels

1. `SETTINGS_PENDING_CANDIDATE`: `0662/33` and `085F(0800)` repeated, `0708` absent.
2. `RETAINED_SERVICE_085F0800_PLUS_0708`: `085F(W2=0800)` and repeated `0708`, no `0662`.
3. `ZERO_085F_AND_0708_OBSERVED`: all five `085F` words zero, with `0708` in same capture.
4. `FOLLOWON_0884_OBSERVED`, `FOLLOWON_07D0_OBSERVED`, `FOLLOWON_0864_OBSERVED`: literal received pages, **not** permission to ACK.
5. `UNKNOWN_FAIL_CLOSED`: missing or mixed geometry, contradictory chronology, RX drops, parser fault or unexpected prior TX.

The implemented offline S11Y-AD prototype recognizes a **subset** of these documentary classes from specific ESPHome log markers; it is **not** a generic raw RTU CRC parser. **Every label stays CAPTURE_ONLY.** The 9 checks consist of four original-log classifications, two different predecessor histories with the same visible RX pattern, and three injected faults.

## Corrections and evidence boundaries

- S11B RX callback logs `085F` all-zero signature after physical TX2 in the same receive-event order. This **strongly supports** that ACK2 applied to already-zero `085F`, but lacks an independent before-TX word dump. Supersede the older payload attribution only, **not** its ACKs or subsequent `0864`.
- `085F(0800)+0708` after an ESP reboot is **observation-equivalent** to previous contexts but does not prove that controller-internal work ownership, application handshake or pending jobs were reset or retained identically.
- Genuine Online/DCM `085F` events: Eco5 Sep 26 = 197 requests/4 ACK; Eco5 Sep 28 = 122/4; ATEC Oct 3 = 2/2. All-zero `085F` does not uniquely imply responder ACK; following `0864` vs `07D0` differs with context. It is not XTR-native authorization evidence.
- The firmware-derived `0861.bit11` Online/gateway communication alarm label is **not independently XTR-confirmed**; Connect application/serial timers do not establish controller `0662` restart.

## Next candidate / non-action policy

**S11Y-AE OFFLINE / NOT RUN:** correlate existing per-session predecessor ACK order, `0708` selector image, actual response availability and ESP firmware restart gaps against the observed `0884`/`07D0`/`0864` first-owner branches. Positive: reproducible discriminator with counterexamples checked; negative: rule contradicted by raw logs; inconclusive: missing predecessor or selector. Offline abort: contradictory/partial corpus; no recovery on physical equipment.

**No new live ACK, write, reset, room-sensor disconnect, DCM hardware capture or automatic owner draining.** One standard FC16 ACK is transport/scheduler acknowledgment, not confirmation of settings acceptance.
