# V5DCM37-COMBINED-DCM-OFFLINE-01 — full combined result (2026-10-19)

**STATUS: COMPLETE / POSITIVE for scoped OFFLINE C++17 source/model/history tests only.** Original experiment contract: [PREPARED](V5DCM37_COMBINED_DCM_OFFLINE_PREPARED_20261019.md). **NO** new live XTR experiment, device boot/flashing, Configuration ARM, controller restart, native RS485 TX, actual DCM response, semantic register write, proven reply owner/slot/physical epoch, full Connect app C2/Online. The original user's ESP32 remains user-flashed **V5DCM33-FIX-B2**. Do not use this result to justify active TX without a later independently scoped user-initiated trial.

## Baseline and provenance

- Current locally proven XTR FIX-B2 passive baseline: [V5DCM33-FIX-B2-LIVE-PASSIVE-01 COMPLETE / POSITIVE](V5DCM33_FIX_B2_FIRST_LIVE_PASSIVE_RESULT_20261019.md): unarmed 204s; B11D 2342 matched, B11C 2345 matched, main parser resync/drop/fault zero, HA measurements flowing; native software executor 393 candidates all HARD_DENY, UART Write Calls=0, DE software low. Exact flashed binary hash and electrical DE remain UNVERIFIED. Last known-good rollback V5DCM23 FIX2 RX-only.
- Exact unchanged user-private source ZIP **SHA256 `fdc09c5927b5a351163db95db96dc467abd43cb27e1e7fc8068782bea4a677c7`**. Original main YAML SHA256 `32e1b7c3ea4f7411fb94d6d769370b9ae10874403961403002250b96e4365d46`. It retains the historical `V5DCM23_PREPARED_NOT_FLASHED` filename despite the later real FIX-B2 flash.
- Previous V5DCM34 exact original Connect AppFS↔historical Write Beta V4.1↔FIX-B2 functional map COMPLETE / POSITIVE offline, V5DCM35 native approval/mock-delivery model COMPLETE / POSITIVE offline (192+18 tests), V5DCM36 pinned private B2 Core/strict deny provider COMPLETE / POSITIVE offline (53/53 plus compiler guards). Historical V4.1 EXP386/387 locally positive and EXP388 partial; original V5DCM32 controller-restart rejoin COMPLETE / NEGATIVE after pre-gap B11D `RAW_INCOMPLETE_AT_IDLE`; B2 fresh post-gap >90s live retention remains **NOT RUN**.

## Exactly one controlled change

Added one **standalone, nonflashable, nontransmitting** V5DCM37 host-only evidence coordinator, combining five **separately testable** modules. The actual FIX-B2 parser, Core, YAML, UART reader, HA entities and red/brown/Configuration diagnostics were **not edited or flashed**.

| Axis | Verified research-only behavior | Boundary NOT crossed |
|---|---|---|
| A — native approval mock | Already-validated canonical native `0x0F` FC23 metadata → strictly bounded *synthetic* delivery slot → later FC16 `03E8/count14` sets **InternalFreshShadow** | No real response payload/CRC, actual delivery, controller acceptance, owner/slot, TX |
| B — path specificity | Fresh `03E8/count14` model distinct from retained/recovery. `085F/count5` after an explicit mock remains **RetainedCandidate/RecoveryCandidate** only; standalone 085F does not qualify | No false 32/32 universal fresh rule; no retained/hot controller session acceptance |
| C — integrity/continuity | Strict monotonic boot/generation/frame sequence; CRC/full boundary/from-original-parser flags; collision, synthetic slot expiry, event budget, one-scope-only and original B11D/P5 sticky revocation preserve fail-closed status | No inference that timestamp or mock token proves physical epoch/DE/current response-owner |
| D — firmware-profile shape census | Uses **EXACT unchanged private B2** `v5dcm22::kProfile` 33 source descriptors matched on **start AND count**, not on caller-supplied W2/W3/W4 bit/index; 15 W2 + 10 W3 + 8 W4 distinct receipts can be counted inside a test scope, duplicates/32-of-33/legacy wrong count denied completeness | Even complete historical 33/33 shape census is **not** authenticated Connect application C2, Online, owner, fresh 32/32 handshake |
| E — version/physical output barrier | Reuses exact pinned FIX-B2 B2 Core copy-only structural inspector and V36 deny-only output provider; replay of old compiler-negative output paths | No actual outgoing frame, 0x0F approval transform, security key, 0x0708 command mailbox, actual TX |

No active TX target slave/page/register/current write value applies, because **no frames are prepared for sending**; synthetic timeout limits are host budgets, not Thermia wire timing. Static `kLiveOutputAllowed=false`, no ESPHome/UART/DE links in new coordinator.

## Test and raw-capture results actually executed

- **NEW V5DCM37 1,017/1,017 strict C++17 host assertions PASS**, compiled with `g++ -std=c++17 -O2 -Wall -Wextra -Werror -pedantic`. Tests include successful bounded *mock-only* fresh path, retained/recovery observation-only branches, errors/late/stale/foreign/bad CRC/partial/unverified parser/out-of-order, wrong modern/legacy geometry, conflicting responder, B11D/P5 original faults, revocation, one scope, missing/duplicate/incorrect 33-group receipts, no physical authority. Arbitrary group numbers cannot be injected; source map used.
- **V5DCM37 source pin/no-output audit 34/34 PASS** on exact original B2 parent. Deliberately modified B2 ZIP rejected (expected negative).
- **V5DCM36 original private B2 Core and actual adapter/platform 53/53 PASS**, along with **three intentionally forbidden compilation attempts rejected**, and its tampered ZIP negative. Previous **V5DCM35 host model 192/192 and B2 Core differential 18/18 PASS**.
- **Unchanged B2/FIX-A/V5DCM31/V5DCM32 regressions PASS**: 65 B2 source-shadow tests; 70/70 real XTR historic CRC fixtures, frozen shadow stops at 61 frames; 52 short residual; 32 portable CRC/length; 61 V5DCM31; 34 synthetic + 34 original historical FC23 V5DCM32 checks.
- **Full physical-capture metadata replay**: four original/collaborator logs **23,472/23,472 CRC valid, zero CRC-bad**. This is **historical evidence**, not the user's currently flashed FIX-B2 wire epoch.
- **Local old XTR Oct03**: *whole recording* **31/33 exact modern shapes** (15 W2/8 W3/8 W4). Missing exactly `03E8/count14` and `0410/count22`; the recorded first page has *legacy count13*. One canonical FC23 request and one response-shaped record **do not authenticate response sender/physical delivery**.
- **Local old XTR Sep25**: **24/33 exact modern shapes** (14/8/2), no canonical FC23 request in inspected excerpt.
- **Collaborator Eco5 Sep26 and Sep28**: **33/33 modern significant page shapes in each entire capture** (15/10/8); **cross-model** and **across capture windows**, not current local XTR Connect C2 or a single owned accepted session.
- The **first** full combined runner hit its tool runtime ceiling during repeated builds; no success was claimed then. The final native XTR historical replay was separately executed PASS, the runner changed to compile common old sources once, and a **complete second combined run returned exit 0**. The assembled archive was then extracted into a **fresh temporary directory** and a **third full run from the extracted archive also exited 0**; no hidden prior work directories were used by the run scripts.

## Artifact and reproducibility

User-private, **NONFLASHABLE** archive `V5DCM37_COMBINED_DCM_OFFLINE_NOT_FLASHABLE.zip`: **21 files, 37,040 bytes**, SHA256 **`f656c09082f6077b84db216570666a96a097ad85e676a9d693efee2e47f8974f`**. Archive was reopened and `testzip()` and every member against its own SHA256 manifest verified. Contains the V37 coordinator/1,017-case host tests, original non-sensitive V36/V35 regression harness and compiler-negative probes, original private source pins, read-only historical CRC geometry scanner, sanitized historical statistics, full actual test output, runner, source-audit scripts, README and manifest. It intentionally **does not contain** the parent FIX-B2 full YAML/source ZIP or protected native output algorithms. Run extracted ZIP:

`bash run_v5dcm37_offline.sh /path/to/exact/V5DCM33_FIX_B2_QUALIFIED_EVIDENCE_HOLD_OFFLINE_NOT_FLASHED.zip /path/to/four/original/historical/logs`

Captures optional for partial retesting; missing captures explicitly marks historical cases not run. The complete *reported* run included all 4.

## Conclusions, unknowns and next decision

**PROVEN SOURCE/HOST ONLY:** FIVE evidence axes can remain independent and all physical-authority/application flags fail closed under 1,017 tested cases; real B2 source code remains unchanged, pinned private output is forced OFF. Profile matches are geometrically source-bound, not the 32 ordered bootstrap or modern C2. Actual local old geometry mismatch is independently CRC-verified. The original V5DCM36 finding about dangerous public HEAD output defaults remains valid: HEAD's default enabled `BoundaryFedAdapter` must not be copied into tested B2 without separate safety review.

**STRONGLY SUPPORTED / NEXT:** the remaining first true native-DCM functionality is a **private, version-pinned request-dependent output provider** with independently justified current owner/response-slot/epoch context, actual transport delivery accounting, later controller-owned FC16 continuation, retained/recovery requalification and separate application package/Online gates. Until a real, bounded response has been sent and independently correlated, do NOT call the model's fresh shadow a native accepted DCM session.

**OPEN:** genuine dynamic response behavior/authorization on the current XTR, physical bus owner/slot/epoch, 33/33 actual modern Connect significant packages, real C2 and Online status, electrical DE, current FIX-B2 >90s post-gap live retention, original V5DCM18 Python seven-fixture reference-Core test. Do not assume access to a genuine DCM for new logs. Previously accepted G01–G06 research residual risks remain accepted but do not become positive physical proof.

**No user action needed.** Running user FIX-B2 is preserved; do not automatically ARM/restart/flash/write/emit native traffic. A later **distinct user-initiated live** trial must first specify actual heat-pump/controller state, private exact TX frame/CRC reference, target native slot/address, response window/attempt bounds, expected effects, negative/inconclusive outcomes, abort triggers and rollback. Sensitive native approval/security and confidential command-mailbox implementation MUST NOT be pushed to public GitHub.
