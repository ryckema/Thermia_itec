# V5DCM31-MANUAL-SESSION-SCOPE-01 — accepted-risk session policy joined to passive GAP24 metadata

**Status: COMPLETE / POSITIVE for OFFLINE C++ source implementation and host tests only (2026-10-18).** Nothing was flashed, transmitted, installed into ESPHome, or accepted by the current XTR. Current user-flashed V5DCM23 FIX2 remains **RUNNING / PARTIAL**, RX-only, 1/33 in its original short log, software TX HARD_DENY.

## Hypothesis, baseline and controlled change

**Hypothesis:** The user has previously accepted G01–G06 engineering/research risks for the unchanged local XTR, so progressing to a bounded native DCM research session should not depend on inventing an independent physical controller epoch witness. A separate **user-accepted-risk, experiment-scoped** session-policy *candidate* can coexist with V5DCM29's stronger independently verified provenance model, without falsely promoting the former to the latter or producing any native output.

**Known-good baseline:** Real user-flashed private V5DCM23 FIX2 RX-only, last ~2m25 live log `1/33` and clean B11C/B11D, no observed native FC23, existing HA sensors, zero native physical attempts by software. Exact flashed image/OTA slot unverified; previously published RX33 candidate 262 named entities versus private FIX2 180, no safe direct replacement. Historical V4.1 EXP386 and EXP387 are COMPLETE / POSITIVE for bounded native recovery/delayed semantic re-arm, EXP388 remains RUNNING / PARTIAL for untested cancellation scenarios. G01-09 historically VIDEO/INTERVENTION_ANCHORED POSITIVE; G02 installation-scoped CONDITIONAL POSITIVE; G01–G06 *remaining technical uncertainties* are user-accepted risks but not proven measurements. V5DCM29's `IndependentProof` has no real production issuer. Preserve these distinctions.

**One controlled change:** introduce ONE new standalone, **nontransmitting** C++17 `v5dcm31_accepted_risk_session_policy.hpp` with a manually armed finite scope and a distinct `RxCandidateUnderAcceptedRisk` result. Use exact unmodified source `gap24a_session_gate.hpp` and `gap24b_evidence_adapter.hpp` as a separate type-safety regression. No changes to original V5DCM23 FIX2, V5DCM28 RX ledger, V5DCM29 independent proof contract, production YAML, HA entities, UART, DE or any TX implementation.

## Original source support / boundaries

Read the actual public Write Beta v4.1 source Git blob `8e8a82689e53528a8b751a1abbd901f683b6b238`:
- Fresh controller restart path (approx source lines 2133–2265) has controller silence/return, known `A80E=0000/A80F=0005` cold guard, an exact native FC23 challenge and one bounded fresh response, with abort on RX integrity deltas. The actual response algorithm/payload is **not** reproduced here.
- The same v4.1 source distinguishes retained runtime, in which cold response should not be replayed without a new qualified context, and recovery after loss/reset with semantic cancellation/refresh rules (EXP386/387/388 source and [Write Beta README](../../Write%20(Beta)/README.md)).
- V5DCM29 source tests prove that physical controller generation and local session generation are different; evidence `GAP24` path candidates do not confer actual owner, epoch, ACK, TX or Online permission.
- This V5DCM31 policy deliberately has **no `IndependentProof` field or factory**. User permission is an explicit **research risk decision**, not an asserted electrical fact.

### Exact policy

A deliberately started scope requires a unique increasing scope ID, existing ESP boot ID, start timestamp, externally bounded duration and observation-event budget, requested `Fresh` / `Retained` / `Recovery` path, `user_initiated=true`, accepted G01–G06 risks and unchanged physical installation.

- **Fresh**: manual controller intervention in *this bounded scope*, then a current RX bus-gap/return candidate, corresponding cold controller status and a matching canonical FC23 request shape. Those are **candidate conditions**, not a physical epoch ID.
- **Retained**: previously qualified runtime *in the same ESP boot* plus a current known native runtime service and observed continuity, without a new cold challenge.
- **Recovery**: explicitly arm either a new manual controller transition with cold-context evidence, or recovery from already qualified retained runtime; never assume both are evidence of physical authority.

All observations must originate from the **single existing completed-CRC frame callback**. The caller must filter unrelated native/other-slave traffic and must supply strictly increasing completed-frame sequence numbers. The policy refuses a frame reused with altered metadata. Historical, cross-model or firmware-only input is not current-local evidence.

Abort/revoke or deny on missing arm, duplicated/reused scope ID, change in ESP boot ID, stale/duplicate frame sequence, out-of-order time, expired scope, exceeded observation budget, CRC/parser failure, competing native responder, pending stale semantic transaction or explicit cancellation. Candidate event is one-shot and cannot automatically rearm on FC23, general bus silence or device reset.

Every result sets `physical_epoch_proven=false`, `physical_owner_proven=false`, `response_slot_proven=false`, `native_accepted=false`, `ack_authorized=false`, `tx_authorized=false`, `semantic_write_authorized=false`. The only successful output is **RX rejoin CANDIDATE under an explicitly accepted experimental risk scope**, plus a monotonic LOCAL generation. This policy **does not call** the old V5DCM28 reselect API or forge V5DCM29 `IndependentProof`.

## Reproducible offline tests and artifacts

Private conversation artifact `V5DCM31_ACCEPTED_RISK_SESSION_POLICY_OFFLINE_ONLY_NOT_FOR_FLASH.zip` SHA256 `cc576fed268426107536223f790349e0dd3d723918c913f136f64c411fde47e7`; includes new header, unchanged GAP24A/B headers, two test sources, README and SHA256 manifest. No original private native 0x0F responder, challenge algorithm, command-mailbox tooling, firmware image, credentials or wire payload is included. ZIP is **NOT FLASHABLE**.

Strict host compile: `g++ -std=c++17 -Wall -Wextra -Werror -pedantic`.

- **Test 1: 61/61 assertions PASS.** Manual fresh, retained and controller-restart recovery positive metadata candidates; denied missing user arm/acceptance/topology; no manual intervention; out-of-order or duplicated same frame sequence, missing sequence, foreign source/boot, invalid CRC, competing responder, stale semantic work, expiry, over-budget, scope reuse, explicit cancellation. All success cases explicitly assert zero TX, zero independent physical proof and zero native Online claim.
- **Test 2: PASS (existing GAP24A/B source type and policy join).** The exact passive observer remains `context_admitted=false` and all owner/epoch/TX flags false on an ordinary native FC23. A deliberately armed, future local-metadata scenario can produce an **accepted-risk RX candidate** without modifying the passive observer; historical XTR intervention remains historical-only. Neither test calls an actual ledger-reselect implementation or transmit routine.
- During test hardening an intermediate assertion failed because the **test source had reused a completed-frame sequence after adding monotonic replay checks**. Fixture corrected to have a distinct next frame; both tests recompiled and fully PASS. This is test-harness correction, **not an observed negative XTR protocol outcome**.

### Distinct validation levels

| Activity | Result |
|---|---|
| Source model review (v4.1 + GAP24/V5DCM29) | COMPLETE |
| New offline C++ compile and scoped regressions | PASS |
| Source-only unchanged older GAP24 join | PASS |
| Actual V5DCM23 portable RX ledger reselect using this policy | **NOT IMPLEMENTED / NOT RUN** |
| ESPHome config / full firmware compilation | **NOT RUN** |
| Flash or live observation of V5DCM31 | **NOT RUN** |
| Physical native TX, ACK, true Connect session, semantically accepted write | **NOT RUN / UNPROVEN** |

## Evidence classification and outcome

**OBSERVED FACTS (SOURCE/HOST):** The current protected native integration need not remain stuck solely because G01–G06 lack independently measured electrical completion; those are documented accepted research risks, separate from the actual proof quality. The new policy produces a scoped metadata candidate while retaining hard zero output. All direct host cases pass.

**STRONG CONCLUSION:** Accepted-risk *research admission* and independently verified controller epoch/owner must remain different fields. V5DCM31 supplies an explicit implementation seam for the former; it does **not yet** solve real V5 packet-ledger resetting or general native emulation.

**HYPOTHESES:** Joining the bounded accepted-risk policy to the actual V5DCM23 receive and ledger path will allow stale generation revocation and valid new RX-only requalification while preserving TX HARD_DENY. This has not been compiled in ESPHome or physically run.

**UNKNOWNS:** exact flashed private V5DCM23 source/binary partition, live native FC23 occurrence after log, current controller epoch, actual native response owner/slot, first legacy R6 Stage D D=4 cause, reliable recovered application C2/Online and full production HA coverage. None are secretly treated as proven.

## Next: V5DCM32-RX-REJOIN-INTEGRATION-01 — PREPARED / NOT RUN

- **Hypothesis:** controlled, source-only integration of an accepted-risk, local-generation RX collector reset into the **exact original FIX2** native callback can recover passive package collection after a justified new bounded session without generic FC23-auto-rearm, second parser or TX; keeping separate strict V5DCM29 verified-witness path untouched.
- **Known-good:** private actual FIX2 source ZIP, 180 named HA entities and software TX HARD_DENY, existing V5DCM22/23 passive counters and V5 frame callback, V5DCM19/20 pass.
- **One change:** add a *distinct RX-only local-generation reselect method* to current portable ledger adapter, called only after a V5DCM31 positive bounded policy result from the same existing RX callback. Do **not** change protected responder or mailbox. Preserve DE low and no UART TX path.
- **Target:** strict native `0x0F` received FC23 context, subsequent CRC-validated FC16 group receipts, original 33-group profile. No writable register, no outgoing address/payload, retries=0.
- **Positive (host):** revoke on FC23 or fault; fail stale/duplicate/bad scope; bounded manual candidate -> local RX reselection under `accepted-risk` provenance (NOT physical acceptance), then strict new source-group receipts; no stale W2/W3/W4 carryover, no owner/ACK/TX/Online promotion; source diff leaves all 180 HA entities, diagnostics and hard deny intact.
- **Negative:** reselect from a lone FC23, repeated old arm, stale/wrong ESP boot, other model, unknown physical owner promoted to proven, unsolicited TX, lost HA/callback refs.
- **Inconclusive:** no current session event, unverified exact source, missing important headers / actual flash identity; do not fabricate.
- **Abort/recovery:** offline-only first. For any separately prepared live RX-only candidate, any DE/TX, parser regression or HA sensor loss -> stop, revert to last verified RX-only build. User live run results required before changing live status. No standing authorization implies spontaneous controller restart or flash.

No new physical experiment or active native transmission in V5DCM31. No secret implementations or raw native challenge data published.
