# V5DCM21-C004 — restore existing reference-core CI against actual C004 contract (2026-10-18)

**Status: COMPLETE / POSITIVE for this separate offline validator-maintenance substep.** Native DCM V5DCM21 remains **RUNNING / PARTIAL**. No on-device experiment, production YAML edit, native TX, physical IO or firmware security code.

## Hypothesis, baseline and one controlled change
Hypothesis: existing `Reference core unit validation` failure is a stale **public contract validator** rather than an effect of V5DCM21's FC16 classification change.

Baseline: historical job [39068978579](https://github.com/ryckema/Thermia_Connect_Firmware/actions/runs/39068978579) on **2026-10-17** already failed in the `v4.1 route equivalence` step at `AssertionError: C004_INTERFACE_NAMES`, before V5DCM21's recent Core fix. A newer pre-fix job [39117645279](https://github.com/ryckema/Thermia_Connect_Firmware/actions/runs/39117645279) on 2026-10-18 showed the same error.

Direct source inspection:
- `data/xtr_portable_platform_contract_v1.json` has C004 interfaces `accept`, `reset`, `callback_binding` and **7** rules; existing callback adapter/release-gate source already covers the added interface.
- `tools/validate_xtr_portable_contracts.py` still expected only `accept`, `reset` and **4** rules.

**Controlled correction:** change only those two expected values in `tools/validate_xtr_portable_contracts.py`, from 2 to 3 names and 4 to 7 rules; leave JSON source, all C++, TX/CRC/RTU/port adapters, ESPHome and secrets unmodified. Firmware commit `1067f49b84bd92a8675435c1a205a66d1e747437`.

## Executed CI evidence
Actual checkout GitHub Actions [39117997136](https://github.com/ryckema/Thermia_Connect_Firmware/actions/runs/39117997136) at source commit `1067f49b84bd92a8675435c1a205a66d1e747437` **COMPLETE / SUCCESS**. All required steps passed without suppressing the previously failing validator.
- Original reference/core state tests 56/56, boundary/IO 8061/8061, pipeline 25/25.
- Contract group includes C004 expectations and prints **PASS 18/18**, plus other linked validators 24/24, 28/28 and 8/8.
- Portable C++ tests/builds and reference parity groups (50/50, 19/19, 15/15, 28/28, 37/37) passed.
- Adapter integration smoke printed `P004/P005 smoke PASS`.

The separate V5DCM21 strict C++/RX observer suite [39117672490](https://github.com/ryckema/Thermia_Connect_Firmware/actions/runs/39117672490) passed **24 readiness+classification**, **45 RX-join**, **5 synthetic capture smoke** and TX hard-deny. Reference workflow and V5DCM21 run are **different** tests / commits; do not claim native XTR integration or electrical results from either.

**Remaining check:** A longer `Offline full suite one by one` Actions run at the earlier firmware head `a2042fc2` was still `in_progress` when inspected at 10:07 UTC. Its early steps use `continue-on-error`; green full-suite completion, if later seen, does not automatically prove all early checks clean. The *separate mandatory* reference workflow above now passes.

## Decision and next action
Positive: historical C004 mismatch documented and fixed against verified JSON source; mandatory reference-core CI now passes on current HEAD, without changing behavior.

Negative: none in this scoped CI recheck. Unknowns/partial outside scope: installed V5DCM19 FIX1 source bytes, native controller/owner/response-slot, original seven-corpus complete reference replay, Online icon/Connect runtime, and active challenge response. Keep V5DCM18 full replay **PARTIAL** and accepted G01–G06 decisions unchanged.

Abort/rollback: revert this isolated two-constant validator-only diff if contract source is proven wrong; physical device untouched, no TX candidate/payload.
Next useful analysis: audit actual explicit `Core::qualify_handshake` callers for provenance and post-delivery state commit; keep existing public native challenge path inactive. Obtain exact deployed FIX1 source rather than inventing it.
