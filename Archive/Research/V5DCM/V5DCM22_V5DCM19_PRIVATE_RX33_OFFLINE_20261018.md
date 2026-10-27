# V5DCM22 — V5DCM19 proven-observer lineage: private RX33 adapter

Date: 2026-10-18.

**V5DCM22-V5BASE-OFFLINE-01: COMPLETE / POSITIVE** for strict host C++17 and byte-exact local historical capture metadata replay.  
**V5DCM22-V5BASE-RX33-01: PREPARED / NOT RUN** for subsequent ESPHome candidate, not compiled/flashed/executed on actual XTR.  
**V5DCM22 full native session integration: RUNNING / PARTIAL.**

## Baseline and exact source
- User-supplied private `V5DCM19_RX_ONLY_FIX1_20261018(2).zip` SHA256 `ca1dd27231ff12d587c8931fda81d7f61fab9da84603fe11eee78c41b5ec75b5`, 66 archive entries.
- Principal ZIP YAML `waveshare-thermia_V5DCM19_RX_ONLY_PREPARED_NOT_FLASHED.yaml` SHA256 `44a9d82154aac71d1b17adf62ed0a9901a1c1bd334cb1a943d5b8eae15ad6612`, 180 named HA objects, native V5 completed-CRC frame callback and existing V5DCM19 logs.
- Local V5DCM19 FIX1 live observation (189s) **COMPLETE / POSITIVE** plus V5DCM20 passive endurance (18m33s) **COMPLETE / POSITIVE**, separate earlier user logs. **Neither proves uploaded ZIP bytes identical to user-flashed build.**
- Newer v31/RX33 STATCLASS FIX1 has wider HA sensor coverage and HA statistics metadata; it remains a *separate production/HA entity reference*, not replaced or overwritten by this smaller native observer candidate.
- Firmware-source based significant data packages: 33 start/count entries (15 W2, 10 W3, 8 W4), original 2.1.105 CM930 2.3.0–2.4.3 source plus local XTR 2.4.2 geometry. `03E8/14` and `0410/22` strict; older/local historical `03E8/13`, `0410/21` do **not** match.

## One controlled offline change
An **unpublished private ZIP** was created in this conversation's sandbox:
`V5DCM22_V5DCM19_RX33_INTEGRATION_PREPARED_NOT_FLASHED.zip`, SHA256 `ba1bfb9a922f29f3c3fa1af5bf54a66484c9d1a36a6247befac8acb07add36ab`. Do **NOT** publish this ZIP or any proprietary/shadow responder sources in GitHub.

Within exact original source archive, add only:
1. A standalone **public-metadata-only** `v5dcm22_v5dcm19_rx33_witness.hpp` (33 strict shape descriptors, no UART/TX, private 0x0F/security/response or mailbox algorithms).
2. A single `esphome.includes` reference to that header and a boot reset of its passive observer.
3. One observation call inside **the original V5 completed/CRC-valid `for(const auto &f:parsed)` callback**, immediately after `c.on_frame(f,t)`, with an independent source/bus integrity-latch gate. The gate can revoke current local observation continuity, but the CRC-good since-boot shape census remains descriptive. No new frame assembler or UART reader.
4. One 30-second `[V5DCM22] RX33` status in **the existing single top-level interval list**. Old list 16 items -> 17, no duplicate interval keys. Outputs: ever-since-boot exact distinct groups, local post-boundary witness, W2/W3/W4 masks, wrong start/count/expected count, FC23 and integrity boundary, **`controllerEpoch=? owner=? C2=UNPROVEN online=UNPROVEN TX=HARD_DENY`**.

The already committed `Thermia_Connect_Firmware/portable/xtr_v5dcm22_package_integration.hpp` and `xtr_v5dcm22_profile_242.hpp` remain the **authoritative portable ledger / CI source**. This ZIP-specific stand-alone witness is a **first integration adapter using the original V5 callback**, **not** a deployed compilation of that exact portable `PassivePackageLedger`. The future portable ledger embedding/deduplication into the real V5 callback remains explicitly **OPEN**, not silently declared complete.

### Source-preservation controls
- Removing the exact four V5DCM22 YAML insertions plus the new heading recovers **byte-identical** original principal YAML.
- Strict duplicate-key YAML loader with `!secret` placeholders: **PASS**; original 24 top-level keys, still one `interval:`, original 16 schedule tasks all present plus one passive 30s diagnostic.
- Original 117 numeric sensors, 13 binary sensors, 47 text sensors and 3 buttons retained byte-identically as YAML nodes; **180 named objects**. Existing ESPHome components, globals, serial bus/CRC/parser, hardware settings, HA entity names and function definitions unchanged.
- GPIO17 **TX pin remains configured in the original V5 ZIP** (unlike v31), GPIO21 DE remains ALWAYS_OFF and historical `HARD_DENY` preserved. No **new** UART write/flush/DE GPIO or TX entrypoints introduced. Software disable is not independent physical line measurement.
- Original ZIP is not promoted as production or the actual currently flashed source; current HA/STATCLASS corrections are **not** claimed installed in this ZIP branch.

## Executed offline validation: COMPLETE / POSITIVE
**Standalone C++17 host test** compiled with `g++ -std=c++17 -Wall -Wextra -Werror -pedantic`: PASS. Tests 33 unique address descriptors and bit positions, all 33 distinct exact shapes, duplicate handling, wrong `03E8/13` and `0410/21`, native FC23 revocation, integrity and changed-source revocation, hard false controller owner/epoch/C2/Online/TX, non-native slave exclusion.

**Actual byte-exact historical capture replay** of local private `thermia_capture_20261003_165355.log` SHA256 `14918065297264473e2357822a8694d184e7821b8c2a3b1cb316039678a708a1` through this **actual new C++ witness header**: `frames=2687 CRCgood=2687 bad=0 FC16=162 FC23=2 exactOccurrences=126 matchedDistinct=31 wrongCount=2 active=0 revoked=1 C2=0 owner=0 online=0 TX=0`. Matches previous independently verified Python/C++ metadata results. The historical capture is not new physical XTR activity and is not uploaded to GitHub.

**NOT validated/executed:** full ESPHome compilation, exact ZIP's complete embedded C++ runtime as a firmware build, on-device flash, current XTR bus, electrical driver disable or exact portable-core package-ledger instantiation inside ESPHome. No active TX, messages or write tests.

## Risks, criteria and next action
**Prepared target:** passive native slave `0x0F FC16`, exactly the 33 individually verified XTR-profile physical start/count shapes. No sent payload, register writes or request frames. Count `x/33` is shape **observation only**, never native C2 or controller sender proof.

**Positive if later deployed:** stable existing V5/B11C/B11D RX counters and all original 180 named HA sensors, periodic `[V5DCM19]` and `[V5DCM22]` logs, correct page shapes and anomaly flagging, zero software/native physical TX. **Negative:** previously working HA or bus/parity regression, false exact geometry, loss of intervals, any active TX or inferred native C2. **Inconclusive:** no matching native pages in the time window, uncertain installed firmware provenance, no independent DE observation.

**Abort/rollback:** recover exact previously confirmed user-flashed V5DCM19 FIX1 or independent V5 read-only baseline if critical bus or HA regression; preserve user’s current functioning HA configuration and historical statistics. **Do not flash this ZIP to replace current production** before reconciling the 180-vs-full-HA inventory, source version and compile.

**Next offline step:** bridge the existing *portable* `PassivePackageLedger` itself into this source-proven V5 callback without adding a second parser, deduplicate the interim witness, then validate complete source/HA/metadata equivalence, strict ESPHome build and fail-closed hard-deny before proposing any live test. Full native Online/Connect/owner/C2 remains unknown.
