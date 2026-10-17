# V5DCM18 — CM930 ↔ portable V5 Core source/API parity audit
Date: 2026-10-17

**Status:** COMPLETE / POSITIVE for bounded source-level discrepancy audit; COMPLETE / INCONCLUSIVE for live XTR hardware/session readiness. No firmware changes, no TX, no YAML/flash/compile.

## Hypothesis, baseline, controlled change
Hypothesis: the original firmware lifecycle and portable V5 API have concrete mismatch or incomplete safety contracts which are more actionable than another passive FC23 observer.
Baseline: V5DCM17, user-deployed V5DCM2 FIX1 RX-only/HARD_DENY, original CM930 firmware-derived transition/readiness tables, previously reviewed V4.1/GAP53 parity work.
Controlled change: inspect exact current public source components/thermia_portable_bridge/xtr_core.hpp, xtr_core.cpp, xtr_adapter.cpp, xtr_frame.cpp, xtr_platform.cpp, together with CM930 state transition and state-axis tables. No source modifications.

## Observed source-level facts
1. Core::fc16_decision() lines 219–222 changes handshake from ResponseSent to Accepted for a qualifying FC16 **before** owner-based FC16 authorization at lines 224 onward. Decision evaluation therefore has a state side effect, even when the same event later returns a denied Decision. The original Connect firmware also has an FC16-driven software acceptance transition, but that vendor software event is not independent XTR bus acceptance.
2. Core::qualify_handshake() (181–184) accepts an explicit call based on health only. The public API exposes no authenticated current-session evidence token in that method signature; integration policy must not call it from a shape-only observer.
3. Core::set_mailbox(enabled) (186–190) toggles a Boolean without independently checking handshake, physical reply-slot ownership, source/epoch or profile. Core::mailbox_decision() (210–214) uses only kind/start/count, mailbox and health. External orchestration remains responsible for trustworthy admission.
4. Core::recompute_write_ready() (130–132) derives write readiness from mailbox, a runtime predicate and inactive transaction. The visible State structure has no explicit version-selected semantic profile, significant-package receipt completion or independently proven exclusive physical slot. Those are separate original CM930 evidence gates, not automatically implied by core.write_ready.
5. The 32-setting kSettings geometry at xtr_core.cpp lines 8–17 fixes 03E8/count14, whereas the historical 2026-10-03 original capture candidate had 03E8/count13. Not universally interchangeable. This is a known model/capture distinction, not evidence of a regression on the local XTR.
6. Core::ingest() lines 273–277 advances generation and stores a page; commit_fc16() lines 288–295 calls ingest on any FC16 whose word count matches, although write_base is only true for recognized owning classes. Cache observation and authoritative write-base are separated, but source/physical epoch provenance still depends on external qualification.
7. BoundaryAwareRtuAssembler receives an explicit end_of_frame Boolean from the caller (adapter source). This is a software boundary interface, not a physical EOF measurement; physical exclusive response-slot evidence is still absent.
8. PlatformPort performs response-class, CRC and response-record ordering validation. These are meaningful host safeguards, not independent proof of electrical DE fail-low or physical bus arbitration.
9. Original CM930 2.1.105 significant data-package state and full application onboarding are separate gates absent as first-class State fields in xtr_core.hpp; this may be intentionally delegated, but the required adapter-level mapping has not been demonstrated in this audit.

## Evidence and conclusion
**Observed facts:** the exact source-level conditions and public API boundaries listed above; original firmware-derived independent axes and transition tables.
**Strong conclusions:** a conservative V5 implementation must not upgrade shape-only FC16/FC23 observations to acceptance or TX authorization. Public Core API depends on higher-layer evidence gates which are not represented by current method signatures. Main actionable parity gap: make acceptance, mailbox qualification, profile/data readiness and physical-output authorization explicit, immutable source-qualified inputs to a fail-closed transition layer.
**Hypotheses:** an offline witness/contract wrapper can separate observing requests from committing accepted state and refuse transitions without source/epoch proof. This has not been implemented or tested in V5DCM18.
**Unknowns:** historical V4.1 current source path may be private/out-of-tree; the audited public portable core is not proof of identical code in deployed FIX1. No direct current XTR challenge or hardware owner evidence.

## Positive / negative / abort / recovery
Positive: find exact reproducible source-level parity differences and connect them to a narrowly scoped next task — MET. Negative: no actionable code gap — NOT MET. Inconclusive: real XTR accepted native session/Online/physical ownership. Abort: revealing private authentication/mailbox implementation or proposing uncontrolled TX — not triggered. Recovery: no runtime changes; V5DCM2 FIX1 remains deployed RX-only/HARD_DENY.

## Next — V5DCM19 PREPARED / NOT RUN
Develop **offline only** a pure observation-vs-authorization test contract for the V5 Core; demonstrate that denied FC16 does not promote handshake, mailbox requires independently verified current-session provenance, and write-ready is not equated to full Connect readiness. Baseline xtr_core.cpp and V5DCM18; controlled change test-only harness or private isolated source patch; preserve production, no bus TX. Abort any private authenticated responder disclosure or host-guard bypass. Rollback discard offline patch.
