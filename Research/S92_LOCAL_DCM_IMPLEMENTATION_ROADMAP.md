# S92 LOCAL DCM — Implementation roadmap (cloud-free)

**Updated:** 2026-10-24. **Planning decision only — not a live experiment or TX authorization.**

## Goal, exclusions, provenance

Deliver a **locally autonomous, reliable, native Thermia iTec XTR M/ESP32/ESPHome/Home Assistant integration**, functionally equivalent to the relevant *local* Thermia Connect/DCM functions: startup, ownership, synchronization, FC16/FC03 reads, cache freshness, sustained runtime and recovery. Thermia Online/cloud, registration, cloud authentication and cloud services are **OUT OF SCOPE**. HA parameter/setting writes are **ON HOLD**, including automated test writes, until the user explicitly reauthorizes a separately defined milestone. Do not disconnect the room sensor.

**Current engineering baseline:** private full `MAIN02_M6_FIX30_CM930_REQUEST_SCOPE_PRIVATE_FIRMWARE_20261024.zip` (YAML SHA-256 `63cda14784aeb9e93e808232c49d508fa4a078ba519777ec689663e4c80ce785`), **SOURCE / OFFLINE TESTED**; no reported FIX30 target compile, flash or XTR live result. Retain the **user-observed FIX28** controller-return cold startup through `06F4`, stage40 owned runtime, continued FC16 ACK + FC03 `0708` and clean RX as a *separate verified transport baseline*, not proof of full CM930 application acceptance. FIX29 repairs an exact source mismatch in current `042E/count15` receipt; FIX30 aligns initial generic requested **and** pending sets with physically requestable mapped packages (32/33), leaving all 33 observation slots. Neither fix is live-validated. Earlier FIX21 locally demonstrated CURRENT 4/4 with 300s age expiry; that does not prove FIX30 persistent refresh.

**Evidence order:** live local XTR capture > user-flashed locally checked YAML > genuine Connect/DCM capture > original user-private Connect 2.0.18/2.1.105 code > official docs > V5/S23 source-only > external ATEC V3/other models. Original CM930 describes **42 read-all request positions** and an original mapping broader than 33 local XTR page shapes; **42 positions, 33 observed shapes and 32 generically requested local shapes are not interchangeable completeness metrics**. Keep proprietary firmware, authentication and raw private protocol contents out of public Research files.

## Engineering contract — applies to every milestone

1. **ONE** S92 lifecycle/session engine, **ONE** existing UART RX callback/parser and **ONE** physical UART/DE/TX owner. No parallel V5 native transport, no second reader, no new autonomous sender.
2. Preserve known-good cold R1/FC16 bootstrap, 06F4 provenance, stage40, native 0708, manual hot-rejoin path, existing fail-closed B11C/B11D, CRC, `thermia_last_valid_frame_ms`, stale watchdog, frame counters, HA production entities and Configuration controls.
3. **Passive automatic discovery is permitted; it never authorizes physical TX.** Existing native replies/reads remain behind original fail-closed owner, peer, session epoch, CRC and explicit user-initiated TX-experiment gates. Unattended/automatic bus TX requires a new *explicit* user authorization and a defined safety envelope; **this plan grants neither**.
4. Every accepted frame, transport ACK, fresh cached page, completed request bitmap and local application state is separate evidence. **ACK != semantic DCM/HA acceptance; status must never claim ONLINE based on observed transport**.
5. Preserve controller restart vs ESP reboot vs owner/session loss vs a single FC03 timeout as distinct causes. Session invalidation expires or marks stale affected data; never refresh timestamps without a correct CRC-valid controller response and, where specified, the existing owned ACK completion.
6. Fixed bounded retry/refresh windows, ABORT, DE LOW fail-close, rollback to user-LIVE-positive FIX28 (or earlier known safe RX-only) after regression. Don't invent register geometry, controller epochs, slot ownership, firmware-version meaning or timing constants. Reuse existing XTR-observed request/response shapes only.
7. **Anti-test-loop:** one consolidated preparatory review already performed; next iteration must produce integrated firmware or a concrete bugfix. A test is run only if it changes a GO/FIX/NO-GO decision. Existing S62/S88/V4.1/S92 evidence is not re-proved absent contradiction. User compiles/flashes; firmware release includes one complete private ZIP, manifest, expected logs, bounded experiment, ABORT/rollback. Distinguish SOURCE, OFFLINE TESTED, TARGET COMPILED, FLASHED, LIVE, LOCALLY VERIFIED.

## Release R1 — S92 unified session engine (first engineering action)

**Scope:** consolidate START/STOP, qualified cold controller return, retained/manual hot-rejoin and future recovery into the **existing** S92/M6 state engine; no new transport. Build an explicit transition table using existing source states `NOT_ACCEPTED/COLD_WAIT/RETAINED_UNPROVEN/RESPONSE_SENT/ACCEPTED_SYNC_NEEDED/OPERATION/RECOVERY/ABORTED`. The transition input is *observed* controller/source and current one-owner session provenance, not a fabricated epoch. On controller-loss revoke owner approval, partial rejoin export, previous app/refresh authority and stale pending delivery; on genuine BOOT_RETURN allow previously **manually authorized** cold continuation as FIX28 live demonstrated. ESP restart must NOT silently inherit owner approval. Retained-device rejoin may progress only with verified current authority; if unproven, fail closed to passive RX and make guarded cold-start fallback available at a new user-initiated opportunity.

**Automatic ownership target:** automatic *recognition/classification and state progression* within an explicitly armed session, not unconditional bus takeover. Keep the existing manually triggered START/ABORT and existing observed-native response ownership gates. Represent separate states `OBSERVED_OWNER_UNKNOWN`, `MANUAL_ARMED`, `QUALIFIED_OWNER`, `SESSION_LOST`, `RX_ONLY`; do not call observation qualification.

**Acceptance:** a single bounded user-initiated next integration experiment (after target compilation and RX-only verification) demonstrates one qualified stage40 transition **and** continuity without the FIX27 owner mismatch; controller restart recovery doesn't inherit an old epoch; ESP-only OTA reboot remains RX ONLY; manual ABORT terminates TX and drops DE. A retained hot-rejoin can be considered complete only on actual observed ownership and runtime traffic; otherwise mark partial/OPEN, not a reason for repeated retained START tests.

**Release status:** PREPARED / NOT RUN.

## Release R2 — complete FC03/CURRENT and native CM930 application reads

**Scope:** integrate as one application/read service under R1's sole session authority:

- CURRENT four-page H/D/C/M reception including FIX29 exact `042E/count15` fix and independent `0546/count20` path; preserve other two known XTR page shapes. Maintain per-page `epoch, source timestamp, CRC-valid receipt, qualified-owner ACK`; use the **locally confirmed 300s CURRENT expiry**, never synthetic freshness. After startup/restart, all four become fresh only from real controller frames; display partial/stale accurately.
- A session-bound, bounded FC03 refresh request and receipt workflow: `IDLE -> ELIGIBLE -> REQUESTED -> RECEIVING -> COMPLETE_4_OF_4` or `TIMEOUT/FAILED`, with explicit deadlines, cancel/rollback, per-session attempts and rate caps taken from existing firmware. A missing single page should not abort the entire qualified transport session unless a real RX/owner safety fault occurs. **No unsolicited TX**: automatic scheduling can calculate *refresh needed* and prepare request state, but must not execute physical read requests without explicitly authorized experiment/operation policy.
- Correct CM930 original request vs observed vs ACKed vs fresh vs application-qualified semantics. Preserve 33 observed XTR groups; 32 currently generically requestable groups; map any of original Connect's additional 42 request positions **only after** corresponding genuine XTR page/profile evidence. Keep separate missing, requestable, received and actually served ledgers, and aging only where source-supported.
- Profile/application synchronisation: separately track raw local version/profile evidence (do not reinterpret `0867` without firmware-source mapping), qualified XTR profile, required application groups for that profile, current/cold preliminary evidence, requested/received groups and `OPERATION` readiness. Do not infer manufacturer Online onboarding/application semantic acceptance from local 33/33 or FC16 ACK. Report local read completeness as *local observed/ACKed* only.

**Acceptance:** one qualified user-initiated **read-only** session reaches 4/4 CURRENT with real fresh timestamps and returns to stale after 300s without fabricated refresh; the separately authorized, bounded native refresh repopulates 4/4 and CM930 requested/pending counts decrease exclusively after matched owned controller responses. Identify any genuine missing XTR package as NONBLOCKING UNKNOWN unless it prevents required local data operation; do not manufacture 42/42. Native HA values derive from valid fresh cache, not NaN-with-false-success.

**Release status:** PREPARED / NOT RUN.

## Release R3 — sustained local runtime, hot-rejoin/recovery and HA production readiness

**Scope:** combine R1/R2 into one continuously operable **local** endpoint. Extend watchdog and session-freshness treatment without competing UART processing: distinguish (a) healthy controller traffic but no FC03 refresh, (b) controller restart/BOOT_RETURN, (c) ESP reboot, (d) owner/session loss, (e) parser/CRC/B11C/B11D or DE fault. On session loss fail closed immediately; invalidate outstanding app/refresh authority. When prior manual/session authorization and all owner checks remain valid, permit narrowly bounded existing native recovery; otherwise remain passive until next user-initiated opportunity. Use verified cold fallback rather than self-promoting retained ownership. Never retry parameter writes.

**Home Assistant:** keep existing production heating/cooling/DHW readings and HA Configuration control surfaces; expose only a small set of meaningful *existing* diagnostics (session state, qualified vs unqualified, current 0–4 freshness, CM930 request/pending, latest fault and current firmware build). Remove more historical experiment UI only after actual dependency checks; no replacement test-button clutter. Running with no Thermia cloud must be possible over local ESPHome/HA connection. Writes remain unavailable even if legacy test controls/code exist.

**Acceptance:** one user-initiated bounded runtime observation materially long enough to cover CURRENT 300s expiration and refresh, healthy FC16/FC03 progression and a genuine chosen recovery event; no unsolicited TX and no data freshness misrepresentation, RX/CRC parser counters clean, DE LOW except guarded physical sends, no HA regressions. The session's user-observed bounded duration is reported literally; don't claim overnight stability from a minutes-long test. If controller cannot be safely restarted, choose RX-only evidence and mark recovery OPEN rather than forcing repeated power cycling.

**Release status:** PREPARED / NOT RUN.

## R4 — future HA parameter writes (BLOCKED until explicit new user authorization)

*No engineering/flash/physical write implementation or test in R1–R3.* After user explicitly reauthorizes this milestone: pick one XTR-confirmed reversible setting, independently read its baseline, define exact desired/current mapping from original firmware and local captures, enforce a separate write credential/guard, bounded one-shot change with controller-origin semantic readback and automatic baseline rollback/manual abort. HA write entities enabled only when semantic acceptance is **LOCALLY VERIFIED**. No cloud dependency. This phase is **ON HOLD**, not a current blocker for an otherwise complete read-only local gateway.

## Handoff, decision rules and next action

- Deliver **one complete private firmware ZIP per integrated implementation milestone**, not research-only packages. Do not split R1 into a new S90/S91 test loop. R1/R2 may be bundled into ONE cohesive next FIX31 if their source changes touch the same S92 state engine, followed by at most one bounded proof that changes GO/FIX/NO-GO.
- Functional work is prioritized over exhaustive parity research. Use original Connect files only for missing source-backed requirements. If a needed vendor/profile mapping remains unknown, label it NONBLOCKING UNKNOWN and implement the verified XTR subset; promote to REAL BLOCKER only when proven necessary for the requested local function.
- Update `THERMIA_PROJECT_STATE.md`, `EXPERIMENT_LOG.md` and `PROTOCOL_FINDINGS.md` after actual experiments/material findings, preserving previous evidence and exact statuses; no claims of LIVE for source-only firmware.
- **CURRENT MILESTONE:** R1 unified S92 session/recovery engine (integrate R2 where coupling warrants).
- **DELIVERABLE:** one complete FIX31 successor to private FIX30 plus manifest, source diff, offline checks, manual flash, bounded user-initiated experiment, abort and rollback.
- **REAL BLOCKER:** no new engineering blocker currently established; remaining native owner/app runtime qualification requires user-live validation, not invented test gates. No parameter writes.
- **ONE NEXT ACTION:** implement R1 in existing FIX30 M6, and fold tightly coupled FC03/CURRENT coordination from R2 into the same source pass.
