# THERMIA PROJECT STATE

Last updated: 2026-10-28. Public, non-sensitive status only; private firmware and genuine OEM-derived material are not published here.

## Latest 2026-10-28 milestone closure

**COMPLETE / POSITIVE: 10/10 Heating descriptors LIVE / LOCALLY VERIFIED on user-flashed W2R25F4.** Third XTR user log 2026-10-28 21:21:36–21:25:35: D5 Heating Maximum reg 03EA word2 user edit 40→42 at 21:25:18; one desired 03E8/14 physical page with deltaWords=1 at 21:25:28 (S92 DE=LOW); real controller-origin FC16 semantic CONTROLLER_ACCEPTED d=5 actual=42 at 21:25:29.481. M6=5; calendar AUTO_CAL_TWELVE_OWNED_ACKED 21:22:02 and 21:25:32; CURRENT 4/4 confirmed 21:22:26.991; sampled CRC_DIFF=0, RX drops=0, parser resync=0. Other d7/d8 preview attempts while busy correctly NO_TX. Combined three capture evidence: 27/27 physical Heating writes semantically accepted across all ten descriptors. **CURRENT MILESTONE:** Heating Write User complete. **DELIVERABLE:** W2R25F4, 27/27 semantic readbacks over three logs. **REAL BLOCKER:** none for Heating; other groups unvalidated. **ONE NEXT ACTION:** integrate Hot Water Write User into the same S92 writer/ledger, with user-controlled bounded live acceptance and TX still on hold until authorized. Earlier 9/10 text below is historical.

## Current verified baseline

**Latest locally verified candidate:** Private W2R25F4, flashed by user, iTec XTR M 3N controller 2.4.2. **Nine of ten Heating descriptors LIVE / LOCALLY VERIFIED**, with **26/26** actual user-initiated physical desired-page sends followed by genuine controller-origin FC16 semantic acceptance in two consecutive 2026-10-28 captures. The first log (21:12:09–21:15:33) had 19 acceptances over seven descriptors; the second (21:16:16–21:20:05) adds seven verified sends (D6 three times, D12 twice, D8 once, D7 once). No ESP reboot or per-parameter/session count boundary was needed between deliberate HA writes.

| Descriptor | Register | Field | Live verified examples |
|---|---|---|---|
| D1 | 03E8 | Heating Curve | 35→40→35→22→35 |
| D4 | 03E9 | Heating Minimum | 21→25→10→20 |
| D5 | 03EA | Heating Maximum | **NOT RUN / NO FC16 semantic proof in supplied logs** |
| D6 | 03EB | Correction +5 °C | 0→1→0→1 (second log) |
| D7 | 03EC | Correction 0 °C (signed) | 1→−2→0→1 |
| D8 | 03ED | Correction −5 °C (signed) | 1→−1→0→1 |
| D9 | 03EE | Heating Stop | 20→15→20→18→15→17 |
| D10 | 03EF | Reduced Temperature | 20→22→20 |
| D11 | 03F0 | Room Factor | 2→1 |
| D12 | 03F4 | Room Setpoint | 22→21→22 (second log) |

**Per-descriptor statuses:** D1/D4/D6/D7/D8/D9/D10/D11/D12 **COMPLETE / POSITIVE, LIVE / LOCALLY VERIFIED** for these observed register changes; D5 **PREPARED / NOT RUN**. Heating group overall **RUNNING / PARTIAL** until D5 controller readback. Second capture had **7** `HEATING_DIRECT_USER_EDIT`, **7** `GENERIC_PAGE_TX_EXECUTED`, **7** `CONTROLLER_ACCEPTED`, exact selected-word readbacks; a single d12 `PREVIEW_DENIED idle=0 / NO_TX` protected against overlapping physical writes and the subsequent edit was accepted. Native M6 remained 5 and CURRENT 4/4 remained confirmed; V5 CRC_DIFF=0, RX buffer drops=0, parser resyncs=0 in sample counters. A calendar 12/12 read was armed in the second capture, **not proof of completion**; the first captured run and historical verified W2R24 native calendar evidence remain separate.

**Historical verified fallbacks:** W2R24, D1/D4 live proof plus M6/CURRENT/calendar; W2R19 earlier historical rollback. Earlier W2R25F2 session=0 write denials were NO_TX, not controller rejection. W2R25F3 was superseded. Previous seven-of-ten status was correct **for the first capture only**; second capture supersedes the current total.

## Scope and safeguards

One S92 UART/RX/DE owner; V5/CRC/integrity and collision safeguards; explicit user enablement; one in-flight setting edit and one physically delivered desired page per user edit; controller-origin FC16 semantic readback required; native CURRENT/calendar refresh and ABORT/rollback preserved. No arbitrary total/per-descriptor/session time cap. No blind automatic parameter retransmission. Non-Heating parameter writes remain ON HOLD; do not infer parameter permission from transport acknowledgements or M6 alone. Original Connect's internal automatic retry semantics are not yet implemented on the XTR.

## Current milestone / deliverable / real blocker / ONE next action

- **CURRENT MILESTONE:** Write User, Heating group.
- **DELIVERABLE:** W2R25F4 LIVE / LOCALLY VERIFIED multiwrite engine for nine Heating descriptors (26 confirmed edits).
- **REAL BLOCKER:** No controller-semantic live receipt for D5 in either supplied live capture.
- **ONE NEXT ACTION:** One user-initiated D5 Heating Maximum acceptance with unchanged W2R25F4 and genuine controller-origin FC16 selected-word readback; then GO/FIX/NO-GO for the ten-descriptor Heating group. No new firmware or preparatory microtests.
