# V5DCM35-NATIVE-APPROVAL-BOUNDARY-OFFLINE-01 — experiment contract

**Status: PREPARED / NOT RUN (2026-10-19).** This document creates an offline-only research contract and **does not** prove execution, compile, a flashed image, or a native response. No device restart/ARM/TX is requested now.

## Hypothesis
A **single, output-disabled** source boundary joining (a) one already CRC/geometry-validated V5 0x0F native FC23 event, (b) a version-pinned private/published reference-Core *decision only*, (c) a stub/mock response-delivery result, and (d) subsequent controller-owned FC16 state tracking will accurately distinguish native approval *eligibility*, *attempted/successful local delivery* and *firmware-internal accepted state*, without promoting physical owner, controller epoch, ACK authority, app C2, mailbox readiness or Online. This is the smallest offline step toward faithful native DCM functionality; **no challenge response material or algorithm is published**.

## Verified known-good baseline and relevant history
- Latest user-flashed-family **V5DCM33-FIX-B2-LIVE-PASSIVE-01 COMPLETE / POSITIVE**: 204s healthy original B11C/B11D, HA values, 393/393 HARD_DENY, UART writes=0; runtime marker seen. Physical flashed hash unverified. Safe fallback **V5DCM23 FIX2 RX-only**.
- **V5DCM33-FIX-B-POST-GAP-01 COMPLETE / POSITIVE** for transient post-gap RX shadow; separate qualified-status timeout **COMPLETE / NEGATIVE**; B2 offline fix COMPLETE / POSITIVE and post-gap retention after actual new gap **NOT RUN**.
- Earlier V5DCM32 user-confirmed restart RX rejoin **COMPLETE / NEGATIVE** after B11D `RAW_INCOMPLETE_AT_IDLE` appeared before a 12.923s gap. Do not clear sticky flags or call historical B2 clean cohort ownership proof.
- Historical Write Beta **EXP386 COMPLETE / POSITIVE** cold recovery, **EXP387 COMPLETE / POSITIVE** delayed mailbox semantic rearm, **EXP388 RUNNING / PARTIAL** (two recoveries but untested extra cancellation branches). Earlier [V5DCM18 functional map](V5DCM18_FUNCTIONAL_GAP_HANDOFF_20261018.md) and [current exact-source comparison](V5DCM34_CM930_V41_FIXB2_NATIVE_GAP_AUDIT_20261019.md) are prerequisites.
- Genuine/collaborator captures and extracted original Connect 2.1.105 CM930 source already available. User has no genuine DCM for new traces.
- **Source-version caution:** actual private B2 `xtr_core.hpp/.cpp` differs from firmware-repo HEAD (different ticket/provenance and `fc16_decision` API); explicitly select/pin baseline, no unreviewed mixing. Firmware semantics do not automatically prove XTR bus authority. Previously accepted G01–G06 residual risks remain accepted, not newly authenticated.

## ONE controlled change — source/host only
Implement an **isolated nontransmitting/native decision-to-delivery-state audit seam** in an offline host harness or existing test seam. Reuse the existing V5 complete-frame callback/CRC/geometry rules as inputs. Every candidate is a *non-authoritative diagnostic intent*. The mock delivery result must remain distinct from external controller acceptance, independently proven slot, current physical sender/epoch and semantic C2.

**No production ESPHome YAML change, no new UART reader, no hardware DE/driver change, no original B11C/B11D reset, no change to existing HA entities or Configuration buttons, no live session automation, and no physical TX.** Do not expose protected FC23 transformation, raw response bytes, security keys, confidential 0x0F emulator or 0x0708 command mailbox tooling in GitHub.

## Target signals (READ-ONLY and mock-only)
- **Native observed slave 0x0F**: canonical FC23 request geometry (classification only) and subsequent FC16 controller-owned settings/runtime frame boundaries; never assume a sender from a valid CRC alone.
- **No write target**: target page/register/current setting value **NOT APPLICABLE** because there is no register write or outgoing frame.
- **Exact TX payload/CRC**: **NONE**; mocked transport result is not a physical UART send. Timing: local finite one-event-per-callback decision and bounded synthetic event windows; no autonomous polling/retries. Inactive output by default `DENY`.
- **Independent lifecycle axes:** internal CM930 NOT_ACCEPTED / RESPONSE_SENT / ACCEPTED, controller native cold 32-page reference only where the historical fresh path applies, retained/recovery state, app-profile W2/W3/W4 groups (33 derived for modern XTR), mailbox/service, owner/slot/current epoch, write transaction result, Online/cloud all separated.

## Positive / negative / inconclusive criteria
- **POSITIVE offline:** actual source revisions pinned; red negative tests for stale/replayed/wrong-geometry/CRC-damaged/foreign/gap-without-current-epoch/partial-fragment FC23, and for permission generated solely from historical B2 `RX_SHADOW_ONLY`; correctly simulated valid chronological native event **only** advances observational/model states after mock delivered result; no output/HA regression; strict host assertions under C++17/Python as applicable pass; V4.1 EXP386/387 documented positive-event ordering represented without universalizing their R1/timing.
- **NEGATIVE:** an invalid/wrong-source event promotes authorization, state acceptance is committed before qualifying mock delivery, “Accepted” or cold 32/32 silently enables TX, accepted historical RX proof masquerades as current owner, local API drift ignored, or tests fail.
- **INCONCLUSIVE:** unavailable exact source/fixtures, mock cannot distinguish delivery from controller acceptance, accepted behavior depends on unpublished/unknown data without enough source-based evidence, insufficient actual test output.
- **Abort/recovery:** on any accidental live TX path, attempt to clear B11D/P5 sticky history, production YAML regression, content confidentiality exposure or source mismatch: stop offline integration; discard only new source changes, preserve running FIX-B2. There is no equipment recovery action for a correctly isolated offline harness.

## Required evidence and next action
Before claiming any COMPLETE status, provide a source-level diff, exact file/hash provenance for B2 private Core versus current firmware HEAD, test fixture origin (historical XTR versus collaborator/genuine versus synthetic), regression results including denials, explicit `TX=HARD_DENY`, and an audit proving no new ESPHome UART/DE route and no leaked protected response/mailbox implementation.

**After reviewing the offline result**, decide whether a distinct physically scoped, user-initiated response test is warranted. That later contract must specify current heat-pump and controller operating state, target native slot/address/page or read-only reply target, exact *private* outgoing payload reference/CRC (never publish confidential content), one-step timing/attempt ceiling, positive/negative/inconclusive evidence, abort and rollback. This PREPARED contract authorizes no live frame.
