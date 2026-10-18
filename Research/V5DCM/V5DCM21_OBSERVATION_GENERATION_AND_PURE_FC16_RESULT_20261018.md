# V5DCM21 — passive observation generation + pure FC16 classification (2026-10-18)

**Scope/result:** controlled OFFLINE source+CI substep **COMPLETE / POSITIVE**, overall V5DCM21 remains **RUNNING / PARTIAL** (installed V5DCM19 integration / native DCM acceptance / owner / app runtime still OPEN). No device experiment was run.

## Hypothesis, verified production baseline and relevant history
A native FC16 classification must be side-effect free; an *observation-only* lifecycle counter can revoke previously seen cold-reference pages across suspected bus returns, observed FC23, CRC faults and input-source changes **without claiming a real controller epoch or response owner**.

Production baseline unchanged: user-flashed V5DCM19 FIX1 RX-only and local V5DCM20 **COMPLETE / POSITIVE** 18m33s, no physical TX. Earlier V5DCM21 actual-HEAD 22 readiness + 43 C++ joined-frame + 5 Python capture regressions PASS. Original V5DCM18 original full Python Core replay still PARTIAL. Historical V4.1 EXP386/387 positive, EXP388 partial. Accepted G01–G06 risks remain accepted and are not reopened.

**Provenance blocker:** the exact actual installed V5DCM19 FIX1 YAML/ZIP and immutable flashed-source fingerprint remain unavailable in both current GitHub trees; no source-equivalence claim or live callback wiring is allowed. An earlier *historical* inspection of the prepared FIX1 ZIP reported GPIO17 configured as UART TX despite RX-only HARD_DENY; that is NOT a present-turn byte verification of deployed firmware. Software counters from V5DCM20 show no physical TX attempted within their observed interval, not electrical proof of hardware TX impossibility. Do not substitute the public small bridge YAML or v31 candidate.

## One bounded offline code change family
**In `ryckema/Thermia_Connect_Firmware` only:**
- `portable/xtr_v5dcm21_rx_join.hpp`: added `PassiveBoundary` (Startup, CallerReset, SuspectedBusReturn, IntegrityFault, NativeFc23Observed, InputSourceChanged), local monotonic `local_observation_generation` starting at 1, and `last_boundary`; explicit callbacks invalidate the 32/32 observation and increase the generation. **No relationship to authenticated Core::controller_epoch or physical owner.** Code commit `f060b95d422db333c1367b85d670c8bd4f2e4dac`.
- `portable/test_xtr_v5dcm21_rx_join.cpp`: assertions for bus-return, FC23, integrity and externally signalled source change with persistent `real_controller_epoch_proven=false` and `exclusive_owner_proven=false`; commit `cafa14070b7334a94ccaefea2287294e2908cc28`.
- `portable/xtr_core.hpp/.cpp`: made `Core::fc16_decision(const Frame&)` **const** and removed its pre-authorization mutation `Handshake::ResponseSent -> Handshake::Accepted` on a matching FC16. Classification only returns an Owner/Decision; it can no longer change the handshake or bootstrap index. Commits `de54ac10ab64aeb0cbdcd35e342a2d26e99756a3`, `33eeed2318d1f228a70a350e64cb24ec6d309173`.
- `portable/test_xtr_v5dcm21_readiness.cpp`: compile-time assertion that `Core::fc16_decision` is const, and dynamic repeated FC16 + unowned 0x085F shape tests asserting no state advancement; commit `a2042fc2cadc58ad5eff304b9df939c309d42d3d`.

**Important limitation:** `Core::qualify_handshake()` remains an independently callable explicit state mutation API for existing test/legacy callers; making classification pure does not itself qualify this setter, establish firmware acceptance, replace the fixed historical R1, or implement a native dynamic challenge adapter. Do not conflate this specific fix with a general authorized-commit implementation. The private 0x0F response and 0x0708 tooling are neither included nor published.

## Actually executed tests
Dedicated mandatory GitHub Actions run [39117672490](https://github.com/ryckema/Thermia_Connect_Firmware/actions/runs/39117672490) at firmware HEAD commit `a2042fc2cadc58ad5eff304b9df939c309d42d3d`: checkout, strict actual-source C++17 compile, tests and TX hard-deny check **PASS**, log outputs:
```
PASS V5DCM21 actual HEAD C++ readiness/observer 24 assertions; TX permanently denied
PASS V5DCM21 RX-only joined adapter 45 checks, full cold spine without owner or TX
PASS passive-capture metadata smoke: 5 synthetic cases, no session/TX promotion
PASS: source output hard-deny invariants
```
No new user XTR capture or flash. Five capture tests synthetic; previously analyzed raw Eco5 Sep26/28 max 28/32 and 24/32 remain *cross-model observations*, not native acceptance.

**Separate CI caveat:** existing `Reference core unit validation` workflow remains red at `C004_INTERFACE_NAMES` in `tools/validate_xtr_portable_contracts.py`: validator hardcodes two C004 interface names (`accept`, `reset`) but current `data/xtr_portable_platform_contract_v1.json` has a third (`callback_binding`) and seven rules. This failure is independently verified on workflow [39068978579](https://github.com/ryckema/Thermia_Connect_Firmware/actions/runs/39068978579) from **2026-10-17 before this change**, and persists on [39117645279](https://github.com/ryckema/Thermia_Connect_Firmware/actions/runs/39117645279). It is pre-existing *contract-validator drift*, not evidence that the new `const` C++ classification fails. **Do not claim complete repository CI green**. The broad offline suite was still in progress when this note was prepared and must be checked independently.

## Positive/negative/inconclusive, abort and next action
- Positive **scoped**: 24 + 45 + 5 actual HEAD CI checks PASS; RX-only source hard-deny PASS; pure FC16 classification has no side-effect; locally expired observation generation does not purport to be real controller epoch. 
- Negative: **none** observed within the scoped test fixtures.
- Inconclusive/open: complete original reference-Core/session replay, actual FIX1 callback coupling, source provenance, controller/slot ownership, DCM Online, local genuine handshake acceptance and application readiness.
- Abort if production YAML changes, actual TX occurs, an unknown-page ACK is introduced, or protected responder/mailbox implementation becomes public. None occurred.
- Recovery/rollback if needed: revert the isolated firmware repo commits above; no installed ESPHome/device rollback, because there was no device action.
- **Next:** independently reconcile C004 public contract validation as separate offline controlled change; audit the explicit `Core::qualify_handshake` call sites to prevent synthetic acceptance from leaking into an eventual active path. Continue attempting exact FIX1 source provenance rather than manufacturing a substitute. Retained/hot service must not demand a fresh 32/32 cold bootstrap.
