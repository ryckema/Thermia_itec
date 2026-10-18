# V5DCM21 — public lifecycle-callsite gate and passive cold-spine non-promotion
Date: 2026-10-18

## Status and scope
- **This bounded offline code/CI experiment: COMPLETE / POSITIVE.**
- **Overall native V5DCM21 integration: RUNNING / PARTIAL**; no newly authorized native TX, no local controller-native acceptance, no Connect Online, no physical test.
- Source commit: firmware `0f5b358235cca8f31db7d45bf5a313d2d4675652`.
- Mandatory test evidence: [GitHub Actions run 39119204399](https://github.com/ryckema/Thermia_Connect_Firmware/actions/runs/39119204399), conclusion **success**.

## Hypothesis, verified baseline and relevant prior evidence
Hypothesis: the public portable/embedded production RX source should contain **no direct calls** to the legacy `Core::qualify_handshake()`, `set_mailbox()` or `set_runtime_normal()` setters, and observing all 32 historical cold settings frames through the TX-disabled adapter must not advance the authoritative Core's handshake/bootstrap/write-ready state.

Locally verified previous live baseline remains **user-flashed V5DCM19 FIX1 RX-only**, with **V5DCM20 COMPLETE / POSITIVE** 18m33s passive observation and no software-reported physical TX attempts. The *exact bytes* of that flashed FIX1 YAML/ZIP are still not verified against the GitHub source. Historical V4.1 EXP386/387 native positives and EXP388 partial are independent. V5DCM18 original full seven-corpus stateful Python Core replay remains **RUNNING / PARTIAL**. Previously accepted G01–G06 remain accepted.

Previous offline results included the two Core copies made byte-identical (`fc16_decision(const Frame&) const`), original Reference-core CI repaired for pre-existing C004 validator drift, 24 readiness and 45 joined RX assertions.

## One controlled change family
This is **only a nontransmitting source regression-guard extension**, not a controller experiment:
1. Added `Thermia_Connect_Firmware/tools/audit_v5dcm21_handshake_callsites.py` at commit `39312899f08e4adb69f0841e7207b2d639718a41`. It scans existing production C++ `portable/` and `components/thermia_portable_bridge/`, excluding test fixtures, for direct lifecycle setter invocations. Its self-check injects three forbidden call shapes and confirms comments are ignored. It also requires both Core `fc16_decision` implementations to remain `const`. **The existing setter declarations/definitions are retained for legacy offline fixture compatibility.**
2. Extended `portable/test_xtr_v5dcm21_rx_join.cpp` at commit `7c970a6b57bc456f677fa5c297cad5f02bbceeaf`: after all 32 synthetic, CRC-valid native FC16 cold-reference frames pass through the existing RX-only adapter, the underlying Core still has handshake `NotAccepted`, bootstrap index 0, mailbox false, write_ready false. The separate passive observer's 32/32 *observation* counter does not constitute a physical acceptance.
3. Added the mandatory callsite audit step to `.github/workflows/v5dcm21-readiness.yml` at commit `0f5b358235cca8f31db7d45bf5a313d2d4675652`. Test failure stops this workflow.

No production ESPHome YAML, native response algorithm, protected 0x0F security code, mailbox command implementation, hardware/DE, source-to-physical-owner assignment or actual source API was modified.

## Actual reproducible result
GitHub Actions run **39119204399** at firmware commit `0f5b3582`, all mandatory steps passed on a real checkout:
- Actual-source strict C++17 Core/readiness — **24/24 assertions PASS**.
- Existing RX-only adapter + passive join — **46/46 assertions PASS**, including new 32/32 non-promotion assertion.
- Offline capture parser — **5/5 synthetic tests PASS**.
- Embedded/portable Core exact HPP/CPP parity and embedded Core strict C++17 compile — **PASS**.
- Public production lifecycle callsite audit — **33 checks across 27 source files PASS**; deliberate injected setter-call regressions were detected.
- Existing source TX hard-deny invariants — **PASS**.

## Independent source review of post-response commit
Current public `portable/xtr_adapter.cpp:BoundaryFedAdapter::feed` stages processing in `auto candidate = pipeline_`. If a dispatch creates a response record and `output_enabled=false`, the record is **not delivered and staged response-dependent Core state is not committed**. With output enabled, a response record's staged state is committed only after `port_.accept(...).delivered()`; failed delivery sets output_blocked. An event with **no response record** may still commit observational Core state as intended by the existing adapter (do not generalize the post-TX rule to all passive ingestion). This source inspection is **not proof of real physical DE line behavior**, authenticated owner/session state, or original firmware semantics. No changes to this adapter were made in this substep.

## Evidence classification
**PROVEN / public source and executed host CI:** no direct lifecycle setter call in the 27 scanned public production files at this commit; full simulated 32/32 cold observation does not promote RX-only bridge's Core handshake; guard detects three illustrative unsafe setter call patterns; no platform TX methods invoked by scoped bridge tests.

**STRONGLY SUPPORTED:** public production code keeps passive observation distinct from explicit handshake qualification, and existing adapter uses staged response-dependent commit on successful synthetic platform delivery.

**HYPOTHESIS:** a later *private*, session-proven handshake completion component can supply independently verified source/epoch/physical-slot evidence before any controlled active TX stage; not implemented here.

**OPEN / UNKNOWN:** exact deployed V5DCM19 FIX1 source and callback, real controller epoch/source ownership, exclusive physical response slot, native 0x0F firmware-derived challenge/response, application-required packages, DCM icon and Online. Existing reference-Core seven-capture full stateful replay still pending. A static source guard does not prevent indirect or dynamically linked calls and is not an electrical security proof. Test fixture setters are deliberately allowed.

## Positive, negative, inconclusive, abort/recovery and next action
- Scoped **POSITIVE:** required 24+46+5+33 checks, parity and hard-deny passed on exact commit.
- Scoped **NEGATIVE:** no unsafe direct lifecycle setter call or inadvertent activation observed.
- **INCONCLUSIVE for live XTR** native acceptance/Online; no on-device experiment executed.
- **Abort:** unexpected TX, public protected response/mailbox implementation, silent production YAML modifications, CI failures. No abort event. **Recovery:** revert isolated new source-guard and test/workflow commits if needed; flashed FIX1 unaffected.
- **NEXT:** offline source-to-interface matrix for all native handshake lifecycle transitions and firmware-derived application profile/package readiness, with the original full seven-capture Core replay remaining open. Do not publish private responder code or treat test-only qualification as physical acceptance. Obtain a byte-proven original deployed FIX1 source before wiring any changed component into the actual ESPHome callback.
