# V5DCM60 — Fresh native admission versus retained XTR service: observability audit

**ID:** V5DCM60-XTR-FRESH-VS-RETAINED-OBSERVABILITY-OFFLINE-01  
**Date:** 2026-10-19  
**Status: COMPLETE / INCONCLUSIVE (root-cause discriminator).** CRC/source/observation-boundary checks completed and internally consistent; neither the current XTR master-side admission decision nor the cause of V49's missing progression can be resolved by this corpus. **No live experiment**, TX, Arm, restart, flash, YAML change, compiler run, firmware alteration, protected handshake/mailbox implementation or HA change.

## Scope and controlled action

**Hypothesis:** archived local native XTR service windows, V49 source/witness and original Connect software together contain a discriminating, uniquely observed prerequisite for the transition from fresh native FC23 challenge to initial FC16 03E8 sync or retained FC03 0708 service.

**Last VERIFIED operating baseline:** user-installed V49 RX-only/HARD_DENY, manual Thermia OFF/ON user-confirmed, callback gap 10,351 ms, independent 285-frame/30,532-ms clean post-gap witness; no new reported B11C/B11D faults; UART TX=0. Seven initial native FC23 requests are explicitly timestamped at 19:23:59–19:24:25 with no reply; later cumulative count 63 but a >13-minute unobserved console interval prevents exact single-epoch interpretation. Native 0662 and 0708 counters zero in 19+20 independent source-console samples; 04A6/13 and 085F/5 continue; no sampled 03E8/count14 or 0864/count4. V47 inconclusive remains unchanged. This is the user's measured installed V49 behavior; **the original ZIP is a PREPARED-source artifact, not binary-hash attestation of the flashed image**.

**Earlier research deliberately NOT repeated as new protocol discovery:** V54–57 firmware callback/ACK/version analysis; V55 25,031 frame census; V58 counterexample to universal FC16-ACK-before-0708; V59 seven Eco5 anchored epochs and negative 25-family readiness scan PROTO17/18; local S11T and S11Y retained state research.

**One controlled change:** independently re-run a strictly passive CRC/first-event coverage census on the **same seven supplied original raw archive files**; explicitly compare four *left-censored local XTR service windows* against current V49 *post-manual-interruption console windows*, seven previously analyzed genuine Eco5 return episodes and the scope of the actual Connect 2.0.18/2.1.105 slave source. Audit V49 ZIP source-level hard denial and its own declared epoch limitations. No new PHY sample, no responder or TX construction.

**Passive targets:** native slave 0x0F FC23 envelopes; FC16 03E8/count geometry, 04A6, 085F, 0662; FC03 0708/count6; known sampled V49 sensor counts. **No outbound address, register, payload or physical effect** (offline only).

**Criteria:** positive root-cause discrimination would require an independently captured *same-current-XTR-epoch* native prerequisite that cannot also explain the retained/historical counterexamples; negative would require contradictory CRC/source observation refuting the previously established chronology; **inconclusive** where the historical captures start after an unknown earlier admission and V49 has a missing continuous interval and no observed qualifying response. Abort on CRC or provenance conflict; no physical abort or rollback needed.

## Independent raw census and bounded chronology

The seven user-supplied original timestamp/RTU-hex archives contain **25,031 valid CRC frames / 25,031 parsed rows; 0 invalid CRCs**. Counts below classify **request frame shapes**, not electrical source ownership, successful semantic acceptance, or all controller epochs.

| Archive / provenance | CRC-valid frames | Native 0x0F FC23 request shapes | Native 0708/count6 poll shapes | First such poll | Native FC16 03E8 request shapes |
|---|---:|---:|---:|---:|---:|
| XTR Sep24 21:00 | 394 | 0 | 11 | +2.977s | 0 |
| XTR Sep25 07:15 | 674 | 0 | 18 | +2.571s | 2 |
| XTR Sep25 09:02 | 491 | 0 | 6 | +33.180s | 0 |
| XTR Sep25 09:05 | 892 | 0 | 19 | +0.987s | 1 |
| ATEC/DHP-AQ Oct03 collaborator | 2,687 | 2 | 65 | +64.923s | 1 |
| Eco5 Sep26 collaborator | 10,719 | 101 | 188 | +3.088s | 5 |
| Eco5 Sep28 collaborator | 9,174 | 68 | 85 | +1.711s | 211 |
| **Total** | **25,031** | | | | |

**Important control newly expressed as a set:** all **four older local XTR service excerpts** combined have **2,451 CRC-valid frames, 54 native 0708 poll shapes, 38 timestamp-paired 0708 reply envelopes (per previous V55 300-ms analytic pairing), and ZERO native FC23 request shapes**. Thus an *already ongoing observable service* can be captured without fresh approval in the **bounded excerpts**. None starts at a controller power-on/electrical epoch; the zero count **CANNOT prove that fresh native admission is unnecessary**. This is a sampling/left-censor statement, not a new native protocol capability.

A bounded local XTR Sep25 09:05 counterexample remains: native 0708 polls began +0.987s, first visible FC16 ACK +66.860s, successful status reply +68.235s, then 03E8/count13 +68.304s. As established in V58, there were 16 polls before the first recorded FC16 ACK. V60 adds **no new causal interpretation**: source ownership and unrecorded predecessor session remain unknown.

Cross-model Eco5 files start with status-service traffic **before their first FC23 inside the whole file** (Sep26 poll +3.088s vs first FC23 +184.661s; Sep28 poll +1.711s vs first FC23 +194.753s). Previous V59 aligned **individual BUS_RETURN events** rather than naively interpreting first-file frames as fresh startup: six approved/reply-shaped windows, one 41-challenge/unsuccessful window; two early ~10s approval envelopes with delayed ~118s first paired 03E8 ACK; no +120s universal local XTR timer. No further controller gate follows from V60.

## Original software and current witness provenance

Read the original supplied filesystem-source archives **again**, without executing any protected algorithm: 2.0.18 CM930 `modbus_server15.py` SHA256 `45495f6f8e57e6eccf0cc09ee7b6952dd157e31fc645f34bbe5890c7291d7a9b`; 2.1.105 SHA256 `9afc455fb50472012ae31d0767a0c39878647643ea9c37d7155142e097621d4f`. Both instantiate an **RTU slave-server** for `0x0F`; the Connect side receives native FC16 and answers native FC03 via slave holding-register state. Its application-event/handshake/version logic is **not the master controller's admission policy**. Any software-local ACCEPTED, profile bit or 33-group state remains firmware-derived, not proof of present XTR master semantic acceptance or Online cloud status. No firmware binary patch made.

V49 ZIP, SHA256 `62afe39629102a3daa06f09eab3ed159f44437d702fb8d3904c61e62e2a85630`, source review only: `v5dcm49_post_gap_rx_only.hpp` explicitly contains `kCanTransmit=false` and `kCanTX=false`, plus compile-time deny; cohort records CRC/V5 parity after **RX callback** gap, not electrical EOF, physical sender ID, bus exclusivity, owner, authenticated approval or firmware flash identity. Its own README says PREPARED / NOT FLASHED; separate **later user logs** prove an operating V49 trial, without image hash attestation. Host artifact/source checks are not a compile or full device functional test.

## Evidence-ranked result and decision

**OBSERVED FACTS / PROVEN within their provenance:**
- Four older *local XTR* excerpts have 54 status polls and no FC23 frames **within those excerpts**; 25,031 / 25,031 seven-archive rows passed CRC.
- Old local Sep25 09:05 had status polling before its first visible FC16 ACK; no universal per-FC16 ACK requirement (already V58).
- Current V49 sampled post-manual-gap windows have explicit unanswered FC23, no observed 03E8 initial sync/0662 retained service/0708, TX0; incomplete contiguous FC23 observation.
- Original Connect is a slave endpoint and cannot reveal the unprovided XTR controller-master admission source.
- V49 witness qualification explicitly does not establish current owner, electrical bus epoch or physical response slot.

**STRONGLY SUPPORTED:** Fresh approval, initial settings synchronization and retained status operation are separate observable phases (previous V59), but the available local data do **not** show a single continuous original current-XTR trace bridging fresh approval through initial 03E8 and 0708.

**NOT PROVEN / INCONCLUSIVE:** Whether V49 is blocked specifically by an unanswered FC23, an unrecognized peer, missing FC16 ACK, controller-state gating, a timing/owner problem, a different firmware generation, or an incompletely observed epoch. The present data cannot rank those as causal mechanisms. No version `0867` from V49 is currently attested. This **does not** downgrade locally proven old S11T/S11B transitions.

**FALSIFIED inference:** `old local 0708 without FC23 in a 45–106s file` implies `fresh approval is optional`. The files are left-censored; the inference is invalid. Likewise `RX_SHADOW_RECORDED` does NOT prove physical session admission.

## Smallest actual new evidence that would change the answer

**One new, contiguous, passively observed CURRENT local XTR native-bus episode with real provenance**, covering a *naturally occurring* controller bus-return until either (a) the first 03E8/0708 service transition or (b) the actual end of the retry epoch, and containing strict FC23 request/reply envelopes, FC16 first settings request/ACK, FC03 0708 poll (if any), raw serial capture continuity and GPIO/DE state where independently available. Explicitly record which clocks are software callbacks and which measurements are physical. This would constrain the missing chronological edge; **even that will not alone reveal controller-internal reasons/owner cryptographic validity without additional evidence**. It is **not currently captured or prepared**, and does not justify manual restart or any TX. Do not ask to disconnect the room sensor, borrow a non-existent DCM, or rerun previously completed PROTO17/18/S11T.

**NEXT:** no new live test from V60. Preserve known-good user V49 RX-only/HARD_DENY, HA entities, Configuration controls and red/brown logs, B11D/P5 sticky diagnostics and no native output. Await genuinely new passive raw evidence or independent controller-master firmware provenance. V60's hypothesis is closed **COMPLETE / INCONCLUSIVE**; all older experiment results and negative controls remain intact.
