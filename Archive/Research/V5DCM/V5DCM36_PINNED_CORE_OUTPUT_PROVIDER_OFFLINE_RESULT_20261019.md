# V5DCM36-PINNED-CORE-OUTPUT-PROVIDER-OFFLINE-01 — Result 2026-10-19

**Status: COMPLETE / POSITIVE for offline source pinning, production-output denial and executable host regression only.** [PREPARED contract](V5DCM36_PINNED_CORE_OUTPUT_PROVIDER_OFFLINE_PREPARED_20261019.md). **No new native DCM handshake/acceptance, original Thermia Connect-equivalent reply, output UART transaction, controller restart, ARM, flash, source change on device, application completeness or Online state.** No native bus-response algorithm, private 0x0F code, protected challenge bytes, 0x0708 command tooling or credentials published.

## Goal, exact source baseline and one controlled change

V5DCM35 had established a private **host-only** FC23 observation → *mock delivery* → first fresh FC16 `03E8/count14` model, with no live TX or native-owner proof. V5DCM34 had observed that the currently user-flashed FIX-B2 family and current public `Thermia_Connect_Firmware/main` portable Core cannot simply be substituted. V5DCM36 hypothesized that a **one-source-version-pinned, deny-only output/provider seam** could demonstrate fail-closed behavior even where the original B2 Core produces a structural `Decision.authorized`.

Known-good tested live baseline remains V5DCM33-FIX-B2-LIVE-PASSIVE-01 **COMPLETE / POSITIVE**: 204s matched independent B11D/B11C frames (2342/2345 at final snapshots), production HA temperatures present, parser CRC/resync/drop fault zero, executor 393/393 HARD_DENY, zero UART writes/software physical TX attempts. User-confirmed source-family flash and runtime marker; exact compiled/flashed binary hash unknown. Known-good fallback V5DCM23 FIX2 RX-only. Historical V4.1 EXP386/387 COMPLETE/POSITIVE, EXP388 RUNNING/PARTIAL; previous V5DCM32 physical restart RX rejoin COMPLETE/NEGATIVE after original B11D fault before gap; current B2 post-qualified live >90s trial NOT RUN.

**Single controlled change:** create a separate **nonflashable offline-only** `PinnedCoreView`/disabled output-provider probe against the *exact extracted user-private FIX-B2 Core*. The probe runs `fc16_decision` against a **copy** of Core; it returns sanitized structural booleans, **never** the ticket, response record, physical authorizer or transport send function. The intentionally empty output-provider always returns **DENIED**, even for structurally authorized pages. User production YAML, UART, DE control, HA Configuration, original B11C/B11D/P5 sticky evidence and private full firmware ZIP are **unchanged**.

## Source-provenance pins and material safety divergence

| Item | Private user-FIX-B2 Git blob (actually compiled in host tests) | Public firmware-repo HEAD blob (source-inspected, NOT compiled here) |
|---|---|---|
| `xtr_core.hpp` | `63874043da0845d603b7da1ef81db403011bd063` | `3d172fe134f127e9d19c5ad48d863da9a87741bc` |
| `xtr_core.cpp` | `1ddb6cced68ef4571e650852913cad392e35e734` | `5c345d76f967103ffb58109b1e1742370e09658a` |
| `xtr_adapter.hpp` | `6ce8fec01e673ea0a05d72c29a72747f57018238` | `d3f1a75d551accef2576cb86c77fb2c3080c3c50` |
| `xtr_platform.hpp` | `72bdbd8fb9f7045651ef281da3b978329ce20297` | `95014011a004d8c3165a4619ed61cdf75aac55d3` |

Original B2 complete source ZIP SHA256 `fdc09c5927b5a351163db95db96dc467abd43cb27e1e7fc8068782bea4a677c7`; historical-main YAML unchanged SHA256 `32e1b7c3ea4f7411fb94d6d769370b9ae10874403961403002250b96e4365d46`. The YAML filename contains `PREPARED_NOT_FLASHED` despite the user's confirmed newer live FIX-B2 flash.

**PROVEN SOURCE, critical version boundary:** private B2 `Core::fc16_decision(const Frame&)` is a **mutable, ticketed** decision API, whereas upstream HEAD method is **const and pure-classifying**. Private B2 `BoundaryFedAdapter` normally forces `output_enabled_(false)` regardless of caller-provided `true`, protecting production builds. Current upstream HEAD adapter constructor instead defaults to `output_enabled = true` and directly uses `output_enabled_(output_enabled)`; upstream platform header exposes bare public `accept`, whereas private B2 hides it under a host-only guard. This source divergence is not a newly observed physical bus event or evidence of a fault in deployed B2. **Never copy upstream HEAD's default/output API into the user device without separate review and fail-closed safeguards.**

B2's ticketed Core can still classify `03E8/count14` as **structurally authorized** while its own handshake is NotAccepted. V5DCM36 prevents confusing that local decision with verified electrical response owner, local delivery, ControllerAccepted, full profile C2 or Online. Separate source evidence and model simulated mock are not a physical delivery guarantee.

## Executed reproducible host tests

1. **15/15 exact source/package/interface assertions PASS**: SHA/Git blob pins, unchanged original main YAML/ZIP, private B2 API and deny-default, accepted upstream mismatch is explicit; `audit_pinned_sources.py`.
2. **53/53 strict C++17 checks PASS** against **actual private B2** `xtr_core.cpp`, `xtr_adapter.cpp`, `xtr_frame.cpp`, `xtr_wire.cpp`, `xtr_platform.cpp`, with `-O2 -Wall -Wextra -Werror -pedantic`. Deliberately `output_enabled=true` still yields `false` in normal build. Inspecting a *copy* of Core leaves original ticket, revision, bootstrap index and handshake unchanged; provider denial, no platform events, no writes.
3. **Three expected-negative compiler tests PASS** (genuinely rejected with correct compiler diagnostics): direct unleased `PlatformPort::accept` fails in normal B2 compilation; a HEAD-like `const fc16_decision` signature is rejected against pinned B2; trying to enable `GAP15_HOST_ACCESS` with `ARDUINO`/device macros triggers explicit source `#error`.
4. **One adversarial source-pin check PASS:** an intentionally modified source ZIP is rejected rather than silently accepted as the user's verified baseline.
5. **V5DCM35 host 192/192 PASS** and prior exact-B2-Core 18/18 PASS using the bundle's verbatim predecessor test fixtures.
6. **Original unchanged FIX-B2 suite rerun PASS:** 65 terminal witness assertions, 70/70 historic user XTR CRC-good frame fixtures (frozen witness stops at 61), 52 FIX-A, 32 stream, 61 V5DCM31, 34 V5DCM32 synthetic and 34 against historical native FC23 fixture.
7. Nonflashable 16-file archive rebuilt and ZIP integrity + all member SHA256 verified; self-contained runner retested successfully with **only original B2 ZIP plus extracted new archive**; no dependence on another old build tree. No full ESPHome compilation, and none needed for this source-only scope.

Private artifact (not published to public GitHub): `V5DCM36_PINNED_CORE_OUTPUT_PROVIDER_OFFLINE_NOT_FLASHABLE.zip`, SHA256 **`9eefe9e7452f01267277b742d83e1a9b9b54dfb1e2b42d1bdbf93d83a48d948a`**; contains scripts, host sources/negative tests, source hashes, pass output, sanitized docs but **does NOT contain the private actual B2 source ZIP or any dynamic approval answer**. Root source bundle has 16 ZIP members. A user can rerun `bash run_v5dcm36_offline.sh /dir/with/exact/B2/zip`. This script performs no device operations.

## OBSERVED FACTS / STRONG CONCLUSIONS / HYPOTHESES / UNKNOWNS

- **PROVEN / SOURCE-HOST:** source API mismatch and upstream default-output difference; in exact private B2 default production context, externally requested adapter output=true is still false; no delivery on the new research seam. Rejection of public unleased accept and host-only capability on embedded build. Existing Core structural eligibility is not physical acceptance.
- **STRONGLY SUPPORTED:** next native DCM work should reconcile versions and implement a **separately audited, private, explicitly fail-closed physical provider contract** with independent slot/owner, real current controller epoch, bounded reply timing, delivery and later FC16 confirmation. It cannot be inferred from any of the 53 model assertions or previous mock.
- **HYPOTHESIS:** such a future, constrained provider can reproduce historical V4.1 bounded native cold-session behavior in current V5 without public exposure of protected response algorithms; **NOT TESTED** now.
- **OPEN / UNKNOWN:** actual future response delivery to the controller, genuine dynamic algorithm+eligibility, physical owner/slot/epoch, retained/hot recovery, original V5DCM18 full seven-fixture Python Core parity, B2 success retention after new >=90s live gap, 33/33 meaningful application profile pages, Connect/Online, and electrical DE level.

## NEXT ACTION and safe handoff

**V5DCM37** should first prepare a **separately version-pinned offline output-provider design** and adversarial slot-expiry/revocation tests, preserving all current hardware guards, established HA configuration and old B11D/P5 evidence. Do not independently flash, ARM, restart, transmit or write registers. A *later* deliberate live response experiment requires user-initiated physical test scope, known heat-pump mode/current configuration, exact privately reviewed outgoing frame/payload/CRC if appropriate, slot/timing/bounded retry ceiling, explicit positive/negative/inconclusive criteria, abort on anomalies, and known-good fallback. No DCM module is available for new genuine captures.

**Outcome is only COMPLETE / POSITIVE OFFLINE.** No current-session acceptance or heating-setting change was attempted or proved.
