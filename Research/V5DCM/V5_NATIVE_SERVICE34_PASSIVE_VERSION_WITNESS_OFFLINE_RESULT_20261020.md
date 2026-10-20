# V5 Native Service-34 — Passive version witness on the existing V5 RX path

**Date:** 2026-10-20. **ID:** V5-NATIVE-SERVICE-34-PASSIVE-VERSION-WITNESS-OFFLINE-01. **Status: COMPLETE / POSITIVE — OFFLINE SOURCE/HOST ONLY**; physical XTR PREPARED / NOT RUN.

## Baseline, scope, one controlled change
Canonical verified project baseline: last user-confirmed V83-family RX_ONLY/HARD_DENY installation; the separately prepared FAS1 add-on itself has no verified new flash in supplied evidence. EXP388 RUNNING / PARTIAL; B11D first startup mismatch OPEN. The S29 private staged candidate already has a reviewed-version admission policy but no session/profile-bind call sites and a missing original V83 RX-supervisor header.

**ONE private offline source feature:** copy S29 private source and add exactly three reversible staged ESPHome changes: (a) one RX-only C++17 source header, (b) one observation call for each CRC-validated completed ADU in the existing original V5 callback loop, and (c) a single diagnostic HA text sensor. No new UART parser/reader, TX worker, DE/GPIO operation, register command, mailbox frame, native session bind, profile install, refresh or TX arm. The real ESP32 configuration was not modified.

## OBSERVED FACTS (source + host only)
- Source observer accepts only native 0x0F FC16 0x0864/count4 request geometry (17 bytes), independently checks Modbus CRC and extracts native 0x0867 from the fourth word. This is not firmware W4 nominal 0x0864/count12. It rejects invalid geometry, CRC, other slaves and FC16 ACKs.
- All outputs are explicitly unattributed: raw242->2.4.2 candidate, raw232->2.3.2 candidate, raw22->legacy candidate, unknown or conflicting. Only the original V5 parser provides data; neither repeated values nor a callback gap confer actual XTR identity, controller epoch or electrical response-slot evidence.
- RX health failure is sticky **in this diagnostic only**, while version sightings remain independently visible. Later FC23 is reported as a post-version boundary hint only, not proof of a new physical session.
- A deliberately unqualified adapter for the pre-existing S29 version-observation type **always** has epoch0, reviewed local XTR provenance=false and current epoch=false. Thus S29's profile gate cannot pass because of this witness; profile installation and physical TX are compile-time-false observer properties.
- Reversal of the exact three staged changes restores the S29 parent YAML **byte-for-byte**. Same 24 production top-level YAML blocks, original 197/197 HA ID/name tuples unchanged plus one NEW diagnostic text sensor (198 total), original substitutions and all existing V5/B11D/HA safety controls retained.
- One original safety include, `v5dcm83_shared_rx_supervisor.hpp`, is still unavailable in private S29/V49/FAS1 files. **The staged S34 YAML is NOT FLASH-READY**, and full ESPHome compilation must not be claimed. Previous V83/S29 V43/V44B multi-frame hook delta is not resolved by this passive addition.

## Actual offline validation
- Existing `RUN_SERVICE25_HOST.sh`: **33/33 C++17 host executable tests PASS** (32 prior S29 invocations + one S34 observer; previous FakeIo TX unit tests remain host-only).
- New observer tests in **strict**, **-fno-exceptions/-fno-rtti**, and **ASan+UBSan** builds: **3/3 PASS**. Synthetic tests cover CRC corruption, malformed geometry, FC16 ACK vs request, wrong slave, raw 22/232/242, conflicting version, RX hold, FC23-after-version, no epoch/provenance, and absolute no-TX/no-profile assertions.
- Exact reversible source and YAML structural audit PASS: 24/24 blocks, original 197/197 HA identities, one extra diagnostic, no extra UART reader or physical output path, missing inherited supervisor explicitly flagged.
- **NOT RUN:** embedded ESPHome compiler, flash, physical RS485 TX, user XTR version measurement, controller reboot, Online/DCM session qualification or semantic writes.
- Exact PRIVATE ZIP SHA256 `09ac0e63e2d620355d1fe572b46679cbf56ea7a837d2ea21d592ec574f8e0dd6`, 191 CRC-clean entries. It includes inherited firmware-derived private source and is NOT FOR PUBLIC REDISTRIBUTION. Staged S34 YAML SHA256 `4d8f85717fe53dd2e5c5b89758329602dfc92d7b76429dd6b0dcc51131f9b3bf`.

## Conclusions, unknowns and next
**PROVEN SOURCE/HOST ONLY:** passive visibility into version page source observations can be connected to a single existing validated RX loop without automatically binding source/session and without creating TX capability. **HYPOTHESIS:** a future qualified user-observed RX session may supply new current version evidence, but this has not occurred and will not automatically license CM930. **OPEN:** original missing V83 supervisor, B11D first actual fault cause, physical owner/epoch/slot, current XTR raw 0867, actual original Connect information/33-group/C2/Online state. 

**NEXT:** recover authenticated original full V83 source ZIP or original RX-supervisor header; reconcile V83/S29 complete-plus-partial frame hook behavior offline and preserve sticky B11D fail-close before any embedded build. No need for speculative boot/reboot/TX. User-running V83-family RX_ONLY/HARD_DENY and V49 rollback remain untouched.

**Research precedence:** Service32 corrected the prior misattribution of archived ATEC/model-unconfirmed raw22 frames to local XTR. Previously reported user-local S11D raw242 is historical, not current epoch evidence. No protected native approval logic, key, authentication procedure, private 0x0F emulation source or 0x0708 tooling is published here.
