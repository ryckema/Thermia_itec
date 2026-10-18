# V5DCM21 — exact GitHub HEAD C++17 readiness/observer regression (2026-10-18)

## Status and scope
**V5DCM21 RUNNING / PARTIAL overall.** This specific compile-and-regression substep is **COMPLETE / POSITIVE**, evidenced by GitHub Actions run [39114268008](https://github.com/ryckema/Thermia_Connect_Firmware/actions/runs/39114268008) at firmware commit `1ca3cf60158ecdc8b8d83450c359673a84b7f273`. Actual checkout, compile, test execution and hard-deny invariant assertions all concluded success. This is an offline source/CI result, **not** a native XTR session, live transmission, Connect Online icon or semantic-write result.

## Baseline and one controlled change family
- Source inspected: live GitHub `portable/xtr_core.hpp/.cpp`, `portable/xtr_esphome_bridge.hpp`, existing V5DCM21 readiness/test/observer.
- User's proven on-device baseline **unchanged**: flashed V5DCM19 FIX1 RX-only, V5DCM20 18m33s successful parser parity / no physical TX. No ESPHome YAML changes.
- Controlled change family: strictly offline readiness-evidence checks and their mandatory, separate regression workflow. Updated `portable/xtr_v5dcm21_readiness.hpp` and `portable/test_xtr_v5dcm21_readiness.cpp`; added `.github/workflows/v5dcm21-readiness.yml`. Existing Core logic, bus parser, challenge handling, adapter, original RX-only bridge, semantic TX implementation and output policy are untouched.
- Prior V4.1 EXP386/387 local positives and EXP388 partial are retained; prior original V5DCM18 full Python corpus/core replay still RUNNING / PARTIAL. G01–G06 accepted risk decisions remain unchanged.

## Test and evidence
The dedicated CI step has **no continue-on-error**. Commands shown in the job logs:
```sh
g++ -std=c++17 -O0 -Wall -Wextra -Werror -pedantic \
  -Iportable portable/xtr_core.cpp \
  portable/test_xtr_v5dcm21_readiness.cpp \
  -o /tmp/v5dcm21_readiness
/tmp/v5dcm21_readiness
```
Direct GitHub job evidence: checkout PASS, compile PASS, execute PASS, TX hard-deny invariant check PASS.
Actual test output:
```text
PASS V5DCM21 actual HEAD C++ readiness/observer 22 assertions; TX permanently denied
PASS: source output hard-deny invariants
```
The 22 checks cover default denial, internal firmware acceptance without owner, path/epoch qualification, explicit external owner/slot/boundary/collision evidence, owner/session revocation, profile/packages, retained evidence, service qualification, semantic receipt, recovery-path separation, controller restart epoch invalidation, scoped 32-page cold reference, unhealthy and stale-epoch denial. Some evidence is synthetic; no independent physical ownership measurement is claimed.

## Architecture findings
- PROVEN / public Core source: `fc16_decision` may promote firmware handshake state to Accepted before separate owner qualification; this does not itself authorize TX.
- PROVEN / offline tests: explicit current path + controller epoch + external session attestation now gate *descriptive* transport/application/service readiness. Controller state health invalidates dependent readiness.
- RETAINED / RECOVERY: independent configuration evidence may qualify these modes without falsely asserting 32/32 fresh cold pages. The caller must revoke or refresh evidence across lifecycle changes; Core's retained transition does **not** guarantee a new controller epoch. This implementation does not solve that provenance problem.
- RX-only bridge and evaluator still have TX disabled. Gate `live_tx_permitted` is hardcoded false; static source invariant alone is not electrical proof.
- Native dynamic FC23 response adapter, exclusive slot/owner proof, genuine application package receipt, runtime data join, mailbox semantic service and Online icon are not implemented/proven by these tests.

## Acceptance, abort and rollback
Positive scoped acceptance met: actual-source strict compilation, 22/22 host assertions, permanent model hard-deny, no production modification.
Negative criteria (test failure, unearned readiness under tested stale/denied cases) not observed.
Overall V5DCM21 remains PARTIAL because evidence provisioning and integration with the deployed receive pipeline are not performed; the full native session remains UNKNOWN.
Abort: any physical TX, unsafe source disclosure or production behavior change; none occurred.
Rollback: new isolated files/CI may be reverted independently; no installed configuration needs rollback.

## Next action
Perform an **offline source-level observer integration audit**: determine how the existing V5DCM2 RX callback supplies genuine session/source/epoch evidence to the const observer, and identify fields that must remain UNKNOWN when absent. Do not fabricate physical ownership from frame shape or enable native TX. Test evidence reset on fresh/retained/recovery and repeated valid FC16 frames before preparing any new on-device trial.
