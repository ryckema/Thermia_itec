# V5DCM67 — V49 raw page ledger versus original Connect 2.1.105 version-gated receipt chronology

**ID:** V5DCM67-V49-RAW-VS-VENDOR-WAIT-TIMELINE-OFFLINE-01  
**Date:** 2026-10-20  
**Status:** **COMPLETE / POSITIVE** — 8/8 independently rerun, exact-source offline C++17/Python comparison. Native Connect acceptance/OPERATION/cloud **OPEN / UNKNOWN**; no hardware execution.

## Hypothesis / known-good baseline / relevant results

**Hypothesis:** with an identical chronology of 33 strictly formatted native XTR 0x0F FC16 page receipts, the V49 boot-preselected RX-only ledger and the genuine Thermia Connect 2.1.105 `CMClientParameterUpdateState` can report different completeness states because the original tracker ignores pages before initial version/profile initialization.

**Last user-verified live baseline:** V5DCM49 installed/running RX_ONLY/HARD_DENY, UART TX0, controller manual OFF/ON callback gap 10,351 ms, 285 clean matched frames/30.532 s afterward; current 0867/03E8/0708 not sampled in that segment. Exact flashed binary SHA and current physical owner/slot/session are unverified. **EXP388 remains RUNNING / PARTIAL**, unchanged.

Relevant earlier results: V5DCM21–23 original V49 passive ledger integration; V5DCM57 original method ordering; V5DCM62 publish gate; V5DCM66 exact V49 callback/13 host tests; V5DCM65 historical native XTR runtime evidence. No original method, W1/W3, W5 or physical test repeated.

## Controlled offline change and source pins

**Only one controlled change:** vary chronological ordering of the same 33 source-pinned XTR 2.4.2 page descriptors relative to the first version-page event and any later re-export, using *unchanged* source implementations.

- Input V49 ZIP: `V5DCM49_RX_ONLY_POST_GAP_COHORT_PREPARED_NOT_FLASHED(3).zip`, SHA256 `62afe39629102a3daa06f09eab3ed159f44437d702fb8d3904c61e62e2a85630`. Same bytes as prior V66 ZIP.
- Extracted original V49 `v5dcm23_v5dcm19_real_ledger.hpp`, `xtr_v5dcm21_packages.hpp`, `v5dcm22_v5dcm19_rx33_witness.hpp`, original portable `xtr_frame.cpp`, `xtr_wire.cpp`, `xtr_core.cpp`; strict synthetic full-length CRC-valid 0x0F FC16 receive frames; no use of responder/TX methods.
- Genuine extracted `Thermia_Connect-2.1.105-s1.raucb` AppFS `device_client/cm/cm_client_type.py`, SHA256 `096a6054a68dbf249572e8390f2bc14208dcc2220065a35a5e0e1c844da34fd4`: original tracker class imported verbatim from original archive, not rewritten.
- Exact 33 package descriptors from original V49 V22 array: 15 settings group 1, 10 settings group 2, 8 operations; source-pinned profile 2.4.2. The `0864/count4` version page maps to operations request group bit8.
- Synthetic C++ host harness SHA256 `db075ce6bc7e43515a0e7a43ad38323c396dd6fadf46e2f7c551c9fbcc8dca31`; Python scenario/compare harness SHA256 `482532e1aa5a9e10ef3d0e9b4862955b4910c367f97826c8008840664ac413e8`. Disposable local test fixtures only; **not firmware changes or deployed code**.
- Compiler: `g++ -std=c++17 -O0 -Wall -Wextra -Werror -pedantic` on original V49 portable source. Original class in Python 3.10-compatible form executed in host interpreter.

**Original tracker comparison rule:** before version/profile selection, keep genuine `CMClientParameterUpdateState` in INITIAL, ignoring inbound group events. At the first simulated *supported* 0867=242, initialize genuine pending-bit set from 33 descriptors, then credit the same incoming 0864 event after initialization, reflecting previously established V57 callback order. A 0867=232 event is deliberately marked **profile UNKNOWN** rather than forcing a 2.4.2 profile; it is not a test of genuine 2.3.2 config selection.

## Positive / negative / inconclusive criteria

**POSITIVE** if original V49 class and genuine Connect tracker exhibit predicted chronology-dependent divergence on CRC-valid equal page sequences, including post-version replay recovery, while V49 flags Online and TX remain false.  
**NEGATIVE** if either source implementation disagrees with the predicted counts using supported profile.  
**INCONCLUSIVE** if original class/import/source profile cannot be reproduced or firmware-profile precondition is unsupported.

## Independently reproduced result — **8/8 PASS**

| Event timeline (all strictly source-mapped page shapes) | V49 descriptive ledger | Genuine 2.1.105 tracker fixture |
|---|---:|---:|
| Version first, remaining 32 afterward | 33/33 | 33/33 |
| 31 before version; version then last group | 33/33 | 2/33 |
| 25 before version; version then seven remaining | 33/33 | 8/33 |
| One required page pre-version; version + other 31 | 33/33 | 32/33 |
| Prior row plus repeat the missing page after version | 33/33 | 33/33 |
| 32 non-version pages, version never received | 32/33 | INITIAL (not initialized) |
| Version twice, then all other pages | 33/33 | 33/33 |
| Version event encodes 232, NOT confirmed 2.4.2 | 33/33 | PROFILE UNKNOWN (fixture declines selection) |

C++ flags: `profile_selected=1` at V49 boot, `online_or_controller_accepted=0`, `tx_authorized=0` in every scenario. The original Python tracker reaches ALL only after its configured required bits were credited after WAIT. Firmware configuration/profile file loading, Connect client onboarding, parameter publication, actual hardware state and cloud status were **not executed**. The test supplies the already source-derived supported 2.4.2 required-bit list to the original tracker rather than treating the original firmware as having autodetected the current controller.

**OBSERVED SOURCE FACTS / PROVEN OFFLINE:** V49 has a valid 33-shape census but does not have the original version-triggered WAIT receipt chronology. Under controlled equal event sets, V49 33/33 can coexist with genuine tracker 2/33, 8/33 or 32/33.

**STRONG CONCLUSION:** raw-shape completion does not imply vendor application data completeness and is not native session acceptance or Online readiness. Resending a required page *after* WAIT can settle a purely temporal missing bit; **do not trigger active requests based on that inference without new local evidence**.

**HYPOTHESIS / NOT PROVEN LIVE:** this distinction could explain some observed initial or retained page-readiness mismatches, but current V49 controller firmware version, epoch, complete native session, original application state and physical receive timeline are not known. No 2.3.2 Connect app equivalent is asserted.

**OPEN:** vendor version/profile detection without false positives, revocation across native FC23 and unknown controller epoch, app publication gate, original Connect onboarding and cloud Online status.

## Safety / abort / recovery / next action

No physical slave/address/write, payload, controller timing, retries or TX. There is **no operational plant effect**. All frame input is synthetic, in host memory; no physical abort/recovery is applicable. V49 installed baseline unchanged. For any later integration, default version UNKNOWN, application NOT READY, Online UNPROVEN, TX HARD_DENY; invalidate/revoke on CRC/FC23/provenance boundary rather than retaining false readiness.

**Next:** V5DCM68 can be an **offline-only implementation feasibility check** of one explicitly version-gated observational shadow next to the existing V49 ledger (without a duplicate UART callback/parser). Do **not** add another sensor, enable TX, flash or issue speculative page requests as a consequence of this source comparison. Only prepare live tests after a genuinely novel discriminator and review of current evidence.

**Source audit note:** the previous conversation export already reported this same 8/8 comparison on 2026-10-20 but did not commit it to canonical files. The eight outcomes above were **independently reproduced in this conversation** before documentation, rather than treating the exported result as verified execution.
