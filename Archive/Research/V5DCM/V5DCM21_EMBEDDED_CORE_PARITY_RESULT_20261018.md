# V5DCM21 — embedded and portable Core FC16 classification parity (2026-10-18)

**Status:** **COMPLETE / POSITIVE** scoped offline source / CI parity substep, native DCM V5DCM21 overall **RUNNING / PARTIAL**. Neither an actual ESPHome build nor a physical local XTR run.

## Hypothesis and source baseline
The public `Thermia_Connect_Firmware` tree contains a second ESPHome-embedded Core under `components/thermia_portable_bridge/`. The prior pure FC16 correction made in `portable/xtr_core.hpp/.cpp` must also apply to the embedded copy. Otherwise the portable host tests can pass while a build referencing the embedded component retains `ResponseSent -> Accepted` side effects in `fc16_decision()`.

Known-good physical reference is unchanged: user-flashed V5DCM19 FIX1 RX-only, V5DCM20 18m33s **COMPLETE / POSITIVE**, zero software-reported physical native TX attempts. User's exact flashed YAML/ZIP is still not retrieved or byte-proven in current repos; no claim it uses GitHub's embedded files. G01–G06 accepted; V5DCM18 original full stateful 7-corpus replay PARTIAL. Previous V5DCM21 partial/offline gates: 24 core/readiness, 45 passive join and 5 capture smoke PASS at `a2042fc2`, and original reference core workflow restored at `1067f49b`.

## Controlled source-only change
Directly fetched the four actual GitHub files. Verified `portable/xtr_core.cpp` versus `components/thermia_portable_bridge/xtr_core.cpp`, and header pair, differed **only** in `Core::fc16_decision` const modifier and the previously removed pre-authorization handshake mutation. Projecting precisely that fix onto embedded CPP/HPP produced **byte-identical** current portable files.

Updated **embedded copy only** to match portable:
- `components/thermia_portable_bridge/xtr_core.hpp` commit `050d681c613d529bda0469c03006c84fce12a9da`;
- `components/thermia_portable_bridge/xtr_core.cpp` commit `3ef72522bd2c16d6dc6738a4803ef036147dae66`.

Added mandatory exact-source parity checks and separate strict embedded C++17 compile to `.github/workflows/v5dcm21-readiness.yml`; commit `a1595e693229894eba03d1b20b55afb7d9087721`. No changes to native response transformations, UART, TX, platform interface, user ESPHome YAML or configuration entities.

## Actual CI result
GitHub Actions [39118302777](https://github.com/ryckema/Thermia_Connect_Firmware/actions/runs/39118302777) for exact source commit `a1595e693229894eba03d1b20b55afb7d9087721`: **COMPLETE / SUCCESS**. Mandatory steps:
- exact HEAD portable Core and passive gate compile: PASS, 24/24 source-level readiness/FC16 tests;
- portable existing adapter + RX join compile: PASS, 45/45 joined-frame checks;
- metadata-only capture regression: PASS, 5/5 synthetic fixtures;
- `cmp portable/xtr_core.hpp components/thermia_portable_bridge/xtr_core.hpp` PASS;
- `cmp portable/xtr_core.cpp components/thermia_portable_bridge/xtr_core.cpp` PASS;
- `g++ -std=c++17 -O0 -Wall -Wextra -Werror -pedantic -Icomponents/thermia_portable_bridge -c components/thermia_portable_bridge/xtr_core.cpp` PASS;
- source TX-hard-deny assertion PASS.

Separate original [Reference core unit validation 39117997136](https://github.com/ryckema/Thermia_Connect_Firmware/actions/runs/39117997136) is SUCCESS after prior C004 public validator drift fix. Broad `Offline full suite one by one` earlier [39117672487](https://github.com/ryckema/Thermia_Connect_Firmware/actions/runs/39117672487) completed SUCCESS but several initial steps have `continue-on-error`; do not treat that workflow alone as complete strict all-tests proof.

## Limitations and next action
**Proven source-level:** two public Core variants are now identical, and independently compile under strict host C++17. The matching FC16 classification cannot directly advance internal handshake. `Core::qualify_handshake()` remains independently callable in test/reference fixtures (and is not equivalent to real controller acceptance or response-slot ownership). Firmware's dynamic private challenge responder not implemented in this public code. No native Online or physical DE test.

**Unknown:** deployed V5DCM19 FIX1 original source/callback, hardware controller epoch, ownership, real response slot, current app profile/package requirements and icon/cloud result.

**Positive** scoped CI acceptance met; no negative CI failures. **Abort:** unintended physical TX/publication of protected responder/unrelated production mutation — none occurred; **rollback:** revert the three source/CI commits above, physical known-good device unaffected.

**Next action:** audit all `qualify_handshake` calls in non-test production bridge and require independent source/session proof before any future active path; preserve RX-only modes while the original flashed FIX1 source remains unverified. No user flashing requested.
