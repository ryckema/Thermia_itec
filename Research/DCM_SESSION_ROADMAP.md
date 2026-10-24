# Thermia iTec XTR M — native DCM session roadmap
Updated 2026-10-24. This is the central milestone plan; maintain experiment details in EXPERIMENT_LOG.md, live status in THERMIA_PROJECT_STATE.md and protocol facts in PROTOCOL_FINDINGS.md.

## End state
One ESPHome M6 native DCM session owner that safely handles first startup, FC16 configuration, FC03 CURRENT sync/refresh, long-lived runtime, ESP reset, controller reset, hot rejoin, epoch/cache integrity and recovery. Preserve production HA entities and V5 RX/CRC/DE guards. No second UART reader/writer or parallel session architecture. No automatic bus transmission based on passive recognition. HA setting/parameter writes remain ON HOLD. DCM protocol-specific read and session replies only in bounded user-initiated experiments within proven gates; distinguish a protocol write from a user-setting write.

## Evidence baseline
- FIX42 **FLASHED / LIVE / LOCALLY VERIFIED**, manual S92 cold-return -> CONFIG_SYNCED, native runtime, initial FC03 CURRENT 4/4 and CM930 33/33 OBSERVED (not Online semantic acceptance).
- At >300 s, native CURRENT became STALE_OR_MISSING 0/4, but qualified FC16 ACK runtime continued. CRC integrity clean. FIX42 one-shot refresh button **COMPLETE / NEGATIVE**: denied because no recent controller-initiated FC03 0708. No new physical TX by denied request.
- FIX43 **SOURCE / OFFLINE TESTED, PREPARED / NOT RUN**, defers authorization for a genuine future controller 0708 up to 60s; does not create polling.
- Private original Connect 2.1.105 request mapping W2=0001, W3=0019 (W0/W1 zero) matches present native 930 response. Original server request-bit architecture does **not** prove XTR physical master TX/slot. No new bus frame may be invented.
- FIX44 **SOURCE / OFFLINE TESTED — PREPARED / NOT RUN**: exact FIX42 private YAML parent, 21 native HA read-only page predicates and existing page-count/CURRENT diagnostic tightened to same owner epoch, existing RX integrity and strict 300-second TTL. One bus-loss label no longer asserts an unproven controller reboot. All 784 IDs and original UART/TX/DE sites retained, no extra bus TX or HA writes; ZIP SHA256 `3d05c8f273ce4af14ae70cb4203545b3cdd0f313093ea97636fedb38f42f6bdc`. FIX42 remains last user-LIVE rollback. M2 controller-0708 trigger remains NO-GO; M3 source fix is not compiled/flashed/live.


- FIX46 **SOURCE / OFFLINE TESTED — PREPARED / NOT RUN**: M1/M3/M5 repair four existing TX-owner denial paths plus RX write_stop with one synchronous native owner/CM930/CURRENT epoch fence in the single RX dispatcher. Existing M6 queued STOP remains sole lifecycle state transition. Same 784 IDs, 9 buttons, 75 native-send sites, sole physical UART/DE writer, unchanged CRC/frames/HA write hold. Private ZIP SHA256 `53d2698d80bf8fccc5e92d75dbbac5b035b6c101e929c8f1ee4d49d0de84ac98`. FIX42 last LIVE; M2 unproven repeat 0708 remains NO-GO; M4 ESP-only passive recognition stays RX ONLY / OWNER UNKNOWN. Not compiled/flashed/live.

- FIX47 **SOURCE / OFFLINE TESTED — PREPARED / NOT RUN**: exact FIX46 source now integrates the documented, separately source-tested FIX43 60s deferred four-CURRENT user-arm instead of old past-0708 prerequisite. The separate FIX43 archive was unavailable for byte-level comparison; this is a source-level reimplementation into one native owner, not a claimed byte-identical merge. Button NO TX, second button press cannot extend first arm, and only a *future genuine* controller 0708 inside 60s plus all existing manual owner/epoch/profile/CRC/RX/dirty/cooldown/cycle guards can reach the unchanged original four-page current-only reply. No controller poll generation, new TX site, HA write, CRC or frame change; existing 10s read timeout and 300s freshness remain. Complete private ZIP SHA256 `92b339c5307f6031da6bab746e4ce9645e76b20fa4bde5d9dd1d2a95a9661348`, YAML SHA256 `94e94eabd3193b61f7060064657b6c04beb106f7ab81d8dfa5e67b7f31905110`; 784 IDs/9 buttons/one UART/DE preserved. Not target compiled/flashed/live. **FIX42 still last LIVE**; M2 unsolicited trigger **NO-GO** pending real later XTR 0708.

## Priority work packages
### M1 — Unified session engine (partially LIVE)
Consolidate manual cold start, guarded session state, passive recognition, recovery, ownership revocation, and controller epoch in exactly one owner. States should distinguish BOOT_RX_ONLY, STARTING, CONFIG_SYNC, RUNTIME_SYNCED, RUNTIME_DATA_STALE, SESSION_LOST, RECOVERY; naming may follow existing IDs. Preservation rule: never regress FIX42 cold-return/ACKs. Acceptance: no competing authority; abort stops pending native actions; stale data does not revoke healthy transport.

### M2 — Native FC03 continuing refresh (REAL BLOCKER; highest priority)
A. Trace original Connect request bits -> actual server request handling -> XTR 0708 provenance against verified local frames. Existing W2/W3 flags already correct; do not keep retesting flags.
B. Establish a source- and XTR-supported **legal** mechanism by which controller issues another FC03 0708 in an ongoing session, or classify controller-side limitation openly. No spontaneous FC03, guessed slot, or bypass of TX-owner.
C. Once a legal RX trigger exists, integrate explicit request pending -> same epoch owner/CRC/profile guard -> existing four-page RX response -> matching receipts -> cache validity. Bound pending, cooldown, cycle count and timeout. Initial and subsequent 4/4 must be separated in ledgers.
Acceptance: at least one subsequent genuine read returns H/D/C/M 4/4 without controller reboot; if no legal trigger known, **NO-GO** new physical TX, stop speculative testing and progress non-TX engineering.

### M3 — Cache, RX, FC16 and epoch integrity (partially LIVE)
One source of truth for per-page freshness, same-controller epoch, ACK identity, parser shape and CRC; avoid stale-era values, preserve last_valid_frame_ms/watchdog, B11C/B11D safeguards and metrics. Differentiate refresh failure from controller/session loss. Acceptance: no false FRESH or accidental session ABORT after timeout, no second reader.

### M4 — ESP-only hot-rejoin (OPEN)
Passive recognition is not permission. Make explicit safe ownership/acquisition state on ESP restart; no auto TX without previously proven bus/legal authority and defined user-initiated experiment. Acceptance: either safely rejoin in one user-bounded flow without controller restart or explicitly RX ONLY / OWNER UNKNOWN with no TX. No repeated microtests.

### M5 — Controller reset, session loss and recovery (partially LIVE)
Preserve verified manual cold-start. Fence epoch, queued actions, CM930/FC03 and prior page timestamps on genuine controller reset or bus loss. Bounded intentional recovery only within existing guards, otherwise cold-start fallback. Acceptance: no stale-epoch authority, observable separate failure reasons and clean failclose, no room sensor disconnect.

### M6 — Long-lived runtime and HA production release (OPEN)
With integrated engine, ensure repeatable safe FC16, cache/FC03 refresh, read-only native HA entities, no clutter; retain all production entities, Configuration controls and red/brown key logs. One bounded user-initiated end-to-end live session/soak that changes release decision. Acceptance: stable session over hours with clear freshness and no extra UART/DE ownership. Mark TARGET COMPILED, FLASHED and LOCALLY VERIFIED only when genuine evidence exists.

## Decision gates and safety
- At most one consolidated preparatory review per milestone. Every next iteration must deliver integrated code, one targeted fix, or explicit GO/FIX/NO-GO.
- Physical TX only as part of a defined **USER-INITIATED** experiment with preconditions, receipt expectations, hard stop, ABORT/DE LOW and rollback. No spontaneous auto-TX, controller reset, autonomous flashing or HA parameter writes.
- Session-specific protocol writes (FC16 ACK / existing FC03 replies / justified native session handshake) are in scope under existing authorization; user-visible heat curve, hot water target, mode and other HA setting writes are **ON HOLD**. If a new essential DCM protocol write is found, classify it precisely and require a defined experiment before physical TX.
- Preserve FIX42 last LIVE rollback for native use, FIX39 passive rollback; FIX43 SOURCE only. Do not discard proven pathways until dependency checks.
- Original firmware-derived secrets, challenge-response and proprietary protected internals remain PRIVATE; research documentation is non-sensitive.
- Progress end: CURRENT MILESTONE / DELIVERABLE / REAL BLOCKER / ONE NEXT ACTION.

## Immediate next action
M2: Determine whether an original, supported controller-side request/edge or native session transaction can generate a subsequent 0708 **without inventing new traffic**. If not, explicitly NO-GO physical-trigger implementation and work on M1/M3 integrity in the same single engine. No HA setting writes.
