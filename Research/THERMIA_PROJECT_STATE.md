# THERMIA PROJECT STATE

Last updated: 2026-10-28. Public, non-sensitive status only; private firmware and genuine OEM-derived material are not published here.

## Current verified baseline

**W2R25F4 is now FLASHED / LIVE / LOCALLY VERIFIED on iTec XTR M 3N, controller 2.4.2, for D1, D4, D7, D8, D9, D10 and D11** in a single multiwrite session. The 2026-10-28 21:12:09–21:15:33 user XTR ESPHome log contains **19** distinct direct-HA user write intents, **19** actual single-page physical sends and **19** corresponding genuine controller-origin `0x03E8/14` FC16 semantic confirmations. All were successful with one desired-page send per user edit. Neither ESP reboot nor additional global write-enable between these edits was required.

| Descriptor | Register | Field | Live verified examples |
|---|---|---|---|
| D1 | 03E8 | Heating Curve | 35→40→35→22→35 |
| D4 | 03E9 | Heating Minimum | 21→25→10→20 |
| D7 | 03EC | Correction 0 °C (signed) | +1→−2→0 |
| D8 | 03ED | Correction −5 °C (signed) | +1→−1→0 |
| D9 | 03EE | Heating Stop | 20→15→20→18→15→17 |
| D10 | 03EF | Reduced Temperature | 20→22→20 |
| D11 | 03F0 | Room Factor | 2→1 |

Each verified descriptor: **COMPLETE / POSITIVE, LIVE / LOCALLY VERIFIED** for the observed selected-word changes. **D5** (Heating Maximum), **D6** (Correction +5 °C) and **D12** (Room Setpoint) remain **PREPARED / NOT RUN** based on this capture; a user's general statement that all controls work is not treated as a missing semantic receipt. Overall Heating group: **RUNNING / PARTIAL** until those three are confirmed.

The same captured session remained in native M6=5 with genuine CURRENT 4/4 confirmation and automatic calendar 12/12 confirmation. Logs show CRC_DIFF=0, RX drops=0, resyncs=0; a single `PREVIEW_DENIED d=10 ... idle=0 ... NO_TX` during a busy writer correctly prevented overlapping TX and a later deliberate D10 edit succeeded. This is a local user run, not an assistant-flashed firmware.

**Last historically verified fallback:** W2R24, with D1 and D4 live evidence, native M6, CURRENT 4/4 and calendar 12/12. W2R19 is the earlier historical rollback. W2R25F3 and earlier pre-F4 revisions remain superseded; earlier Sept 2026 experiment records were shared as private user snapshots and should not be silently reclassified.

## Scope and safeguards

One S92 UART/RX/DE owner; V5/CRC/integrity and collision safeguards; explicit user enablement; one in-flight setting edit and one physically delivered desired page per user edit; controller-origin FC16 semantic readback required; native CURRENT/calendar refresh and ABORT/rollback preserved. No arbitrary total/per-descriptor/session time cap. No blind automatic parameter retransmission. Non-Heating parameter writes remain ON HOLD; do not infer parameter permission from transport acknowledgements or M6 alone. Original Connect's internal automatic retry semantics are not yet implemented on the XTR.

## Current milestone / deliverable / real blocker / ONE next action

- **CURRENT MILESTONE:** Write User, Heating group.
- **DELIVERABLE:** W2R25F4 LIVE / LOCALLY VERIFIED multiwrite engine for seven Heating descriptors.
- **REAL BLOCKER:** No controller-semantic live receipts yet for D5, D6, D12 in the supplied 21:12–21:15 capture.
- **ONE NEXT ACTION:** One user-initiated consolidated D5/D6/D12 acceptance using the existing W2R25F4 firmware, collecting controller-origin per-word FC16 confirmations, then GO/FIX/NO-GO for the full Heating group. Do not add further preparatory microtests.
