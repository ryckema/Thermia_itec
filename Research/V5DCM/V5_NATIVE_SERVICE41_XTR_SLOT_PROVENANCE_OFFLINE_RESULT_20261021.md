# Service-41 — Local XTR host timestamps are not independent electrical reply-slot evidence

**Date:** 2026-10-21. **Experiment:** V5-NATIVE-SERVICE41-XTR-HOSTTIME-SLOT-PROVENANCE-01. **Status: COMPLETE / INCONCLUSIVE** for deriving a physical TX window from archived host timestamps; offline CRC/shape replay tests PASS. Physical experiment **PREPARED / NOT RUN**.

## Baseline, hypothesis, single change
Last user-confirmed ESP32: V83-family RX_ONLY/HARD_DENY; EXP388 RUNNING / PARTIAL; first B11D startup fault OPEN; prior V49 RX-only fallback. Service-40 callback witness COMPLETE/POSITIVE OFFLINE, NOT a TX-ready ESPHome binary. Previously approved installation-scoped G01–G06 experimental risk acceptance remains recognized without pretending physical evidence is present.

**Hypothesis:** earlier local XTR record timestamps around CRC-valid slave 0x0F FC16/FC03 requests and immediately following responses independently bound the physical response slot. **One offline change:** independently reparse the *five original user-supplied raw local XTR capture files* with a precise Modbus CRC16 + request/response-geometry + adjacency audit, without changing any gateway source, hardware or firmware.

## OBSERVED FACTS
| Local capture | CRC-valid ADUs | Native FC16 requests / adjacent matching ACKs | Native FC03 requests / adjacent matching replies | Equal/nonpositive FC16 host deltas |
|---|---:|---:|---:|---:|
| 2026-09-24 21:00 | 394 | 21 / 21 | 13 / 13 | 0 |
| 2026-09-25 07:15 | 674 | 40 / 40 | 18 / 18 | 0 |
| 2026-09-25 09:02 | 491 | 41 / 41 | 6 / 6 | 11 |
| 2026-09-25 09:05 | 892 | 73 / 42 | 19 / 3 | 13 |
| 2026-10-03 16:53 | 2,687 | 162 / 162 | 66 / 66 | 0 |
| **Total** | **5,138** | **337 / 306** | **122 / 106** | **24** |

5,138/5,138 parsed ADUs pass CRC; **24 FC16 request/short-ACK pairs carry the same recorded timestamp**. At 9600 8E1 an eight-byte ACK needs ~9.17 ms simply for serialization. Therefore identical record timestamps do **not** measure actual wire request EOF to reply EOF, and no physical exclusive native TX slot or sender identity follows from these host records. Missing *immediately adjacent* replies are not proof no later reply occurred. FC16 ACK ≠ semantic acceptance.

Supplied older **S36** private ZIP was verified intact: SHA256 `39f3901dc3fc33a4874721465be6c9ca61fedd842e1976b6c764b8e5e37be7bd` (209 members), S36 YAML SHA256 `55c6b1aaa8e17ea8d4ccc51d59fb7f6bc6673554cb5a2cacc841fd80574cc6ca`. Conditional boot called `set_same_owner_supervisor_wiring(true)` merely from build switches; two conditional B11D/watchdog call sites exist, but no actual on-device shared callback witness in S36. Service-40 already corrected the assumption in a **later private draft**, not supplied here; this S36 file is NOT current Service-40 source.

## Offline verification
Independent reproducible Python replay: 5,138 CRC-good source records, native requests/responses as table, 24 ambiguous equal-time pairs. **9/9 generic Modbus CRC/shape assertions PASS**. No original raw captures or firmware-derived private native responder/authentication code distributed. Reproduction scripts, nonsecret result JSON, checksums and full report in private user artifact `V5_NATIVE_SERVICE41_XTR_SLOT_PROVENANCE_OFFLINE_20261021.zip`, SHA256 `4941b12103ab54c9e1be219dd359f5fad5563ce2bae7ec737cd6e8d34af5f6e4`.

**NOT RUN:** S40 private source recompile, actual ESPHome validation, flash, physical TX, oscilloscope/logic analysis, current owner/epoch/slot or Connect C2/semantic write.

## Conclusions and next
**STRONGLY SUPPORTED:** Native 0x0F request/response adjacency is historical local XTR evidence; logger timestamps alone cannot authorize a wire-level lease. **OPEN:** actual present XTR sender/slot/epoch, B11D first fault, Service-40 embedded compile and latest source, true Connect session/setting readback. Prior G04-07 hardware-metadata work was user-deferred, not secretly run.

**NEXT (Service-42):** Review the actual latest user-private Service-40 source before preparing a separate, explicitly named TX-aware experimental ESPHome target; verify identical physical UART/DE owner and both fault supervisors, context-specific manual accepted-risk policy, bounded timing, abort and exact rollback. User's historical scoped G01–G06 risk acceptance stands; do not demand a repeat G01/G02 or impose new hardware as retroactive requirement. No auto-TX or speculative hot takeover. Actual active TX needs a separate exact user-initiated live test. Existing V83 RX_ONLY/HARD_DENY and V49 fallback unchanged.

**Abort/rollback:** Offline-only; no hardware action. Any source mismatch, CRC error, stale callback/epoch, unqualified peer/slot or output-capable regression blocks promotion; retain prior working RX-only production.