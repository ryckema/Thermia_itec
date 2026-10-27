# V5DCM68 — Version-gated read-only receipt shadow (non-deployable source feasibility)

**ID:** V5DCM68-VERSION-WAIT-RX-ONLY-SHADOW-HOST-01  
**Date:** 2026-10-20  
**Status:** **COMPLETE / POSITIVE — 17/17 final C++17 host assertions; no production code/flash/TX.**

## Question, baseline and preexisting evidence

**Hypothesis:** without changing the existing V49 UART parser or hard-DENY native output policy, a separate purely observational software *shadow* can enforce the Connect 2.1.105 initial WAIT receipt chronology: ignore page receipts until a supported exact version frame, credit the version frame in that same callback, revoke after integrity/session changes, and never promote that diagnostic to OEM accepted/Online/TX.

**Known-good user hardware baseline:** already user-flashed/running **V49 RX_ONLY/HARD_DENY, UART TX0 reported**, 285 clean frames over 30.532 s following user manual controller OFF/ON RX gap of 10.351 s; current version page `0x0864/count4`, application status `0x0708` and settings `0x03E8` **not captured in that V49 interval**. Original flashed binary checksum and physical owner/slot/epoch not established. EXP388 remains RUNNING/PARTIAL. Reuse V49 original source ZIP SHA256 `62afe39629102a3daa06f09eab3ed159f44437d702fb8d3904c61e62e2a85630`. No repeat of EXP352/355/386, V57/62 OEM tests or V67 8/8 comparison.

**Controlled variable:** use one additional host-memory observer consuming copies of the **existing CRC-complete RX callback bytes**, with **delayed source-profile selection** instead of V49's existing unconditional boot selection. Original V49 V21 ledger and V22 33-descriptor list remain unchanged. The shadow is NOT integrated into ESPHome.

## Source/provenance and constrained implementation

Offline prototype uses existing `xtr_v5dcm21_packages.hpp` class `PassivePackageLedger`, `v5dcm22_v5dcm19_rx33_witness.hpp` exact 33 source-profile descriptors, and original portable frame/CRC/core implementation extracted unchanged from supplied V49 ZIP.

Version marker: CRC-valid native `0x0F FC16 0x0864/count4` with fourth word `0867=242` **only under explicitly assumed supported XTR2.4.2 profile**. Version 232 is treated as UNSUPPORTED/UNKNOWN, not mapped into XTR2.4.2. A supported first version event initializes the local receipt ledger and then credits the **same** version frame. Distinct source evidence for OEM version/load order comes from V57 and original 2.1.105 `cm_client_type.py`, SHA256 `096a6054a68dbf249572e8390f2bc14208dcc2220065a35a5e0e1c844da34fd4`.

**Hard safety invariants:** no UART open, callback replacement, DE change, response generator, FC16 ACK, FC03 read response, mailbox or write; `kTxAllowed=false`, `kOnlineClaim=false`; `PackageSnapshot.online_or_controller_accepted=false`, `tx_authorized=false` even at 33/33. A CRC fault, native FC23, mismatched 0864/count, or unsupported version permanently REVOKES this host epoch until a separate **explicit host reset**; never silently auto-resume on seeing another 0864. No physical epoch proof is implied by `local_generation`.

**Source fixture hashes (local only, not committed as production components):**
- `v68_shadow.hpp` SHA256 `6b881298bfba6afeeef2a9650aa0a29cf750d1732f9f0e0ed884b79e3745a68a`
- `v68_check.cpp` SHA256 `c0aa2b905a13e158dbdf48f402ca1e6b80a2731670b1f91462a5e5171b276752`
- g++: `-std=c++17 -O0 -Wall -Wextra -Werror -pedantic` with V49 original portable frame/wire/core translation units. No ESPHome compile.

## Positive / negative / inconclusive / abort criteria

**POSITIVE:** bounded source-only host fixture proves correct initial UNKNOWN, supported version-gated same-frame receipt, duplicate and late-page behavior, fail-closed fault handling, zero Online/TX flags, without adding a UART reader.  
**NEGATIVE:** accepted unsupported-version frame, rearm after FC23/fault without explicit reset, false online/Tx, bad receipt geometry, missed same-frame version, or incorrect page sequence.  
**INCONCLUSIVE:** source dependencies cannot compile, version encoding/profile not supported, or synthetic frame decoder disagrees with original source.  
**Abort:** stop host harness at any failed assertion; no physical-device abort, output payload, retry, or rollback applicable. Device config stays unchanged.

## Actually executed host results

First development attempt found and fixed a *host prototype* sequencing defect: the fixture passed `validated_profile=false` into `PassivePackageLedger::configure` because its local Selected mode was assigned *after* configuration. Host assertion `version seeds and credits same event` failed, producing **no deployed device change**. The order was corrected in the disposable fixture before the final validation. Preserve this distinction; it is NOT evidence of a bug in original V49 or original Connect software.

**Final 17/17 checks passed:**
1. Default UNKNOWN has 0 required pages.
2. Pre-version page ignored.
3. Exact version seeds WAIT and credits same frame (1/33).
4. Duplicate version does not double-count.
5. Post-version 31 other pages produce 32/33 if one was seen too early.
6. Missing page retransmitted after WAIT completes 33/33.
7. No Online/TX authority at 33/33.
8. Unsupported 232 version revokes/no profile selection.
9. Subsequent valid 242 does not silently rearm after unsupported version.
10. CRC corruption revokes.
11. No rearm after CRC fault.
12. Native FC23 revokes.
13. No rearm after FC23.
14. Foreign-slave version frame ignored.
15. 31 pre-version pages then version+last results in **2/33**.
16. Explicit local reset can reinitialize in *host-only* test.
17. Static hard-DENY / no Online claim.

**PROVEN OFFLINE (source feasibility):** one read-only, version-gated chronology shadow can be modeled using the existing V49 parser/ledger classes, without a second bus parser and without TX. Nothing is integrated into running V49. The controlled synthetic 0867=242 is only a modeled input, not a current XTR observation.

**STRONG LIMITATION:** in the latest short V49 post-gap observation, there was **no actual current 0864/0867**, so such a shadow would correctly remain UNKNOWN and would not explain why native approval is not advancing. Do not misinterpret UNKNOWN as controller rejection.

**OPEN:** current controller version and physical source/epoch; genuine original Connect UI/cloud app state; how an observational shadow should be exposed in HA if/when sufficient local frames exist. 33/33 cannot certify official C2.

## Next decision

V49 remains the verified user-running RX-only baseline, no new production YAML is proposed. **Do not flash this prototype:** additional logging without present version/approval evidence would be low information. Future work should first identify a materially new **offline-supported** discriminator for the missing native fresh approval/service transition, using the historical local XTR results, not repeat already-completed 63-retry passive experiments or previously negative FC16 ACK matrices.

No firmware repo change: this is new project-local host-only fixture, not a new finding about intrinsic original Connect software beyond V57/V62/V67.
