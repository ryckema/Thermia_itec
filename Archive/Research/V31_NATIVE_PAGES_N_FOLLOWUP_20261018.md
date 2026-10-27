# v31 FIX4 native page N follow-up — 2026-10-18

**Experiment IDs:** READ-V31-UNKNOWN-01 and READ-V31-COOL-01. **Status: RUNNING / PARTIAL**; user followed up after an advised 15–30 minute wait with “nog steeds op N” (still N). They did not supply a new absolute uptime or exact full page-mask string, so the absence of ESP resets and the precise extra elapsed time are **not independently verified**. Do not mark COMPLETE for the full experiment.

## Current locally observed evidence
- FIX4 flashed/confirmed by the user in the previous turn; at ESP uptime **151 s**, only `03E8:Y` of the 13 specifically tracked complete 0x0F native FC16 page shapes, and twelve `N`, including all ten page families underlying 34 exact named HA Unknowns.
- `Cooling Settings Page Source = 0442 NOT received since ESP boot`; main 03E8 heating settings populated; direct 0x1E outdoor unit and 0x02/room bus telemetry continue normally.
- User now reports that the absent-page status persists after the planned wait, but the precise second mask/uptime is **not supplied**, so interpret as a qualitative follow-up, not a precisely timed capture or controller non-transmission proof.

## Additional OFFLINE inspection of historical *local* XTR captures
Files available as private project source artifacts in the conversation container:
- `thermia_capture_20261003_165355.log`: native full-page FC16 sequence observed `0x0F:03E8/count13` at **29.262s**, `03FC/count11` at **30.016s**, `0410/count21` at **31.451s**, `042E/count15` at **32.119s**, `0442/count13` at **33.408s**, `0532/count18` at **44.763s**, and `0546/count20` at **45.941s**, followed by the other configuration pages through `06F4/count19` at **61.461s** (32 distinct configuration page starts in this prefix). An exact-format short FC16 address/count ACK appears **about 14ms after each** of the listed full page frames. From **65.664s** onward `07D0/count19` runtime pages and successive runtime pages appear repeatedly during the capture.
- `thermia_capture_20260925_090550.log`: comparable historical XTR configuration sequence `03E8/count13` first at 68.304s; `03FC` 68.9s, `0410/count21` 70.3s, `0442/count13` 72.496s, `0532` 83.688s, 0546 about 85.3s. These are *historical protocol observations with a responder context*, not proof that current FIX4 RX-only sees the same sequence.
- These *user-local historic* captures are **not** genuine manufacturer Online/DCM modules and must not be labelled as such. Time adjacency is evidence of handshake-compatible sequence, not standalone causal proof of every ACK.

## Stronger LOCAL CAUSAL results already present in canonical EXPERIMENT_LOG
- **EXP325 COMPLETE / POSITIVE**: scoped fresh-session response (with qualified controller reboot/context) resulted in first 03E8 controller page; this is already a native-response-assisted session context, not a generic always-on RX-only condition.
- **EXP326 COMPLETE / POSITIVE**: a single correctly owned `03E8/count14` ACK yielded the next `03FC/count11` page about **697ms** later.
- **EXP327 COMPLETE / POSITIVE**: a one-shot `03FC/count11` ACK yielded `0410/count22` about **1500ms** later.
- **EXP328 COMPLETE / POSITIVE**: a `0410/count22` ACK yielded `042E/count15` about **709ms** later.
- **EXP329 COMPLETE / POSITIVE**: bounded ACKs from `042E` through `0442` and `0456` advanced the chain through `046A/count18`.
- **FIX8H COMPLETE / POSITIVE** (separate prior session): a five-minute *passive* observation recorded **130** native `07D0/count19` full pages with **TX=0** after prior service-chain establishment. This demonstrates that ongoing native runtime traffic can remain observable with no current ACK, but it does **not** show a new cold/idle Online session can be established entirely via RX-only.
- Native profile nuance: the older historical local captures above use **03E8/count13 and 0410/count21**, while modern local XTR EXP326–328 used **03E8/count14 and 0410/count22**. Do not copy the old geometry or a fixed ACK into a new test without confirming controller profile, actual received page, owner and epoch.

## Conclusions / hypotheses / open questions

**OBSERVED FACT:** FIX4 reports only 03E8 source recognized for the original 151s boot window, and user subsequently reports still N for missing pages. The full named HA 34 Unknowns are currently explained as **no recognized complete native source page** in the tracked receive branches, not evidence of 34 broken semantic fields.

**STRONG CONCLUSION (evidence-bounded):** Local XTR data acquisition of complete configuration pages is **native session/ACK-dependent in previously tested initial-sync contexts**. More passive waiting alone is not expected to produce those settings in the currently unqualified session; it does not alter protocol state. A strictly physical RX-only reader cannot promise all 524 CM930 firmware-profile words in live HA.

**HYPOTHESIS:** Current FIX4 bus context lacks qualified native initial-sync session/ACK chain. `03E8:Y` may be a standalone available heating-setting broadcast; it is not evidence of complete native DCM ownership or all downstream pages.

**OPEN:** Precise current uptime after follow-up, whether bus carries other unmatched 0x0F frames, actual controller current page geometry (13/14 etc.), physical sender/owner/response slot, fresh native session consent/gates, 0x0708 token, comprehensive post-ACK application readiness, full 524 entry read feasibility. A `N` means the FIX4 exact decoder page **not recognized**, not raw non-transmission.

## Next action and delivery separation

1. **Do not modify/flash FIX4** or keep extending idle wait merely to populate missing Settings. Preserve one YAML+README and passive safety.
2. Continue **offline** verification of the known session bootstrap/ACK provenance in user-local captures + canonical V5 experiment history and firmware. Keep protected private 0x0F responder algorithms and 0708 mailbox tooling out of public docs.
3. Implement any **native TX-assisted, read-only-*semantics*** profile as a **separate, explicit experimental track** (not silently injecting TX in `Read-only/Thermia itec XTR`). That profile would *transmit native control-protocol responses* without changing heating/DHW/cooling setpoints, so it must NOT be described as physically RX-only.
4. Before a **new user-initiated active live test**, use the latest locally supported controller context/geometry/owner proof; one controlled state transition or response type, exact authorized target, payload provenance, known response slot, TX ceiling/retries, abort on ownership/peer ambiguity and rollback to current user-reported working FIX4 or independently verified V5 passive baseline. Do not invent bytes or infer session from the `03E8:Y` flag. No live active test or TX performed during this analysis.
5. Keep the scope of “all parameters” evidence-bound: map firmware rows exhaustively, publish only genuinely observed pages with correct scales; existing direct 0x1E telemetry remains available independently.

**Classification:** Source/capture review is historical/offline evidence and a user-reported partial live follow-up; no new locally emitted frame, ACK, controller write, firmware compilation, or semantic parameter acceptance established. Overall **RUNNING / PARTIAL** for FIX4 receive availability; next active experiment **PREPARED / NOT RUN** only when separately scoped.
