# V5DCM21 — native DCM functional integration / TX-readiness contract
Date: 2026-10-18
Status: **PREPARED / NOT RUN** (offline source and integration audit only; no hardware experiment).

## Hypothesis
A source-traceable separation of native protocol observation, firmware-like internal state, physical response ownership and application readiness can close the V4.1-to-V5 functional gaps without giving passive observations or permissive firmware transitions TX authority.

## Known-good baseline and relevant results
- Actual XTR V5DCM19 FIX1 live RX-only deployment; V5DCM20 COMPLETE / POSITIVE for 18m33s steady parser parity, zero new resync/drop, zero physical TX. Preserve HA entities, existing intervals and red/brown diagnostics.
- V4.1 EXP386 and EXP387 historical local positives (guarded controller cold restart and delayed service re-arm); EXP388 PARTIAL; EXP383 NOT RUN.
- V5DCM18 original reference-Core full replay remains RUNNING / PARTIAL; ZIP and firmware-repo portable Core API/provenance diverge. Prior 17/17 ZIP host tests are not GitHub HEAD or XTR proof.
- Previously accepted residual risks G01–G06 remain accepted and closed absent new evidence.

## Preserve exactly
1. Proven native slave 0x0F processing and exact CRC/geometry/EOF frame recognition.
2. FC16 controller-owned page processing, ordered cold-start configuration observation, epoch-sensitive cache invalidation, source and owner conflict protection.
3. RX diagnostics, production sensors, existing Configuration controls, fail-closed driver enable and explicit hard-deny of physical TX.

## Replace or augment, without publishing protected implementations
1. Separate former fixed guarded R1 replay from a **private**, firmware-derived, request-dependent native response adapter. Never treat the fixed replay as universal; never publish response algorithms or confidential 0x0F code.
2. Model independent state axes: (a) firmware-internal NOT_ACCEPTED / RESPONSE_SENT / ACCEPTED, (b) independently qualified physical bus owner and response slot, (c) controller page/config lifecycle, (d) Connect application profile/subscription/semantic readiness, and (e) mailbox/service lifetime.
3. Native cold configuration completeness must reflect valid ordered pages **for a fresh cold session**; retained and hot rejoin must use their own evidence and must not be rejected merely for lacking fresh 32/32 pages.
4. Runtime processing must honor a qualified current epoch, controller-owned FC16 publication and distinct service/mailbox and request/package gates. An FC16 ACK is never by itself semantic acceptance.

## Explicit exclusions
- Do not promote permissive firmware-internal ACCEPTED into TX authorization.
- No ACK of unknown pages, unfamiliar shapes or unowned slots; no unsolicited TX, speculative register writes or uncontrolled scans.
- Do not elevate V4.1 cold-start timing to universal rule; distinguish controller state predicates and Connect application state predicates.
- No secrets, recovered response algorithms, confidential 0x0F emulation, or 0x0708 mailbox command tooling in public repository.

## One controlled change
Offline source audit / nontransmitting contract and test design only. No YAML change, flash, device TX or firmware-runtime mutation. Target observed domains: slave 0x0F FC23 challenge classification, FC16 page/ACK ownership and bounded ordered configuration; service 0x0708 read/idle behavior; profile/subscription readiness. **No candidate TX payload is authorized by this document.** Current values for write targets: not applicable; no live writes proposed.

## Positive / negative / inconclusive
- POSITIVE: exact source-to-interface/ownership matrix; tests assert denied/stale/conflicting frames cannot grant owner, ACK or semantic readiness, and cold/retained/rejoin states remain distinct; no production or TX change.
- NEGATIVE: audit demonstrates unavoidable conflation of state with authority or any proposal ACKs unknown/unowned frames.
- INCONCLUSIVE: source/API version provenance unresolved or required state predicates cannot be linked to actual code/evidence.
- Safety abort: any new physical TX, publication of protected security logic or code changing production handling. Recovery: discard offline candidate; retain V5DCM19 FIX1 known-good live RX-only and native HARD_DENY.

## Required evidence and next step
Inspect currently committed portable Core/adapter/bridge versus original CM930 derived reference, V4.1 known-positive tests and private derived response interface; record exact file revisions and test outputs. Implement only an offline/testable state-ownership boundary first. Later active test requires its own scoped user-initiated experiment documenting target, exact private payload reference, mapping/current value, timing/retry ceilings, abort and rollback. Do not mark COMPLETE before actual evidence is reviewed.
