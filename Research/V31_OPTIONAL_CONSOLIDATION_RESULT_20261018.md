# READ-V31-OPTIONAL-FIX2 — source result and GitHub consolidation

Date: 2026-10-18.
**Overall status: PREPARED / NOT RUN.** The code/edit and offline source checks were performed and committed; **no live experiment was executed**, compiled, flashed, or proven on an XTR M. No controller TX or semantic write performed.

## Hypothesis and baseline

Hypothesis: passive native capability flags `0x0F FC16 0532/count18` can fail-close the named optional-device measurements (0533 pool; 0534 shuntgroup1 / second circuit; 0535 shuntgroup2 / third circuit; 0536 buffer) while leaving the original proven temperature/status entities, all 250 entity IDs, native raw-register evidence and RX-only bus health intact.

**Actual source baseline:** `Read-only/Thermia itec XTR/thermia_itec_xtr_m_waveshare_v31_full_monitoring_alpha01.yaml` at blob `debedae0c22a6d20d29cadbbb46ef0426cf70c06`, archived verbatim in `Research/Archive/Read-only_XTR_before_FIX2/`. v31 alpha01 FIX1 was itself PREPARED / NOT RUN. **Known deployed baseline** is separate V5DCM19 FIX1 RX-only with V5DCM20 positive live soak. Do not claim v31 inherited a physical verified baseline.

Previous: READ-V31-01, READ-V31-CLEANUP and optional capability source audit. See existing `EXPERIMENT_LOG.md`.

## One controlled code change

Implement availability handling for the four existing optional hardware flags. No new native bus commands, pages, addresses, requests, controls, or UART TX. The corresponding file was consolidated/renamed without changing entity names/IDs:

`Read-only/Thermia itec XTR/thermia_itec_xtr_m_read_only.yaml` (blob `9b3c7427db82c23753076d7787d49b8acc03884c`).

- Add a non-persisted last-seen millisecond timestamp for native `0532/count18`. A full observed controller-originated page refreshes it.
- ON is accepted *only* if flag == 1 and capability page fresh. OFF flag 0, invalid value, page not yet seen and age exceeding **21600000 ms (6h)** fail closed. Six hours is a **provisional operational timeout, not an empirically measured bus recurrence period**.
- Gate existing named second/third circuit numeric publications on fresh installed flag; on known-OFF, unknown and stale inputs clear with `NAN`, plus 5s periodic clean-up if controller runtime data stops.
- Gate `Buffer Tank Temperature`, `Tank Temperature 07D9` and two lowest-wanted tank measurements the same way; the relationship of non-buffer `Tank Temperature 07D9` to buffer hardware should be rechecked before production.
- Gate `Pool Heating Active` and `Pool Demand Queued` on pool flag. On not installed/invalid/stale, invalidate their state (not invented `false`); 5s periodic clean-up handles later expiry.
- Leave pool and circuit raw diagnostic registers intact, still disabled by default, for forensic register analysis, even when the optional equipment is absent. These are **not interpreted active feature data**.
- When a new 0532 flag is neither 0 nor 1, invalidate corresponding Installed binary capability; when the page ages out, invalidate all four Installed flags.
- Preserve all unrelated production entities, CRC frame handling, GPIO18 RX, GPIO21 always-LOW DE and no UART TX pin or active polling.

## Offline audit (performed)

- Actual **GitHub after-write readback**: `main` commit `4b83915d7899a2ee3ef4218b1a70689c4fa38fa8`.
- Source entity name inventory: **250 before / 250 after; 0 deleted / 0 added**. The latest YAML contains 181 numeric, 60 binary, 9 text entities.
- All declared ESPHome IDs unique and every `id(...)` reference resolves; direct unchanged valid-frame-counter references.
- Capability guards and 5s invalidation present for all four groups.
- Source policy truth-table reviewed: no page / flag 0 / flag -1 / stale beyond 6h => disabled, valid ON within 6h => accepted.
- TX configuration absent; `restore_mode: ALWAYS_OFF` present.
- Original complete directory tree verified archived as an identical existing tree SHA under `Research/Archive/Read-only_XTR_before_FIX2`. GitHub re-fetch verifies public XTR folder now has **exactly** `README.md` and `thermia_itec_xtr_m_read_only.yaml`.
- Root `Read-only/README.md` updated to link the new canonical location and archive.

**Not performed or claimed:** independent full YAML parser validation, ESPHome config/compilation, hardware build/flash, Home Assistant registry behavior, on-device 0532 timing or ON/OFF test, physical bus TX measurement, or complete mapping of the 524 firmware-profile registers.

## Real HA limitation and limitations of this approach

ESPHome `disabled_by_default` is a *static entity registry default*, NOT automatic HA enablement when an installed flag switches ON. Dynamic display can be achieved via conditional Lovelace cards, with actual HA assigned capability entity IDs; users must enable the desired optional entity *once* if HA initially disabled it. Example is in the sole XTR `README.md`.

Raw pool/circuit registers remain available as hidden-for-normal-use, disabled-by-default diagnostics independent of capability flag; only interpreted/feature-status entities are gated.

`6h` may be too short if native capability publications are more infrequent; if that occurs, optional data will correctly fail closed but become unavailable even when installed. Review passive native 0532 recurrence and choose an evidence-based timeout before live release.

## Test criteria / risks / recovery

**POSITIVE (future):** independently compiled, no physical TX, CRC/bus health unregressed; capabilities 0, 1 and unknown/expired show correct raw diagnostic/feature availability; no stale ON for pool statuses; capability transitions generate no invented measurements.

**NEGATIVE:** an optional absent/unknown group reports interpreted live state, an installed group cannot recover on a new 0532 page, missing unique parameter, any physical TX, bus instability or compiler failure.

**INCONCLUSIVE:** no 0532 page occurs during capture; installed option cannot be exercised naturally; incomplete log without time alignment.

**Abort:** any misdecoded native page, invalid capability interpretation, bus-health regression, unexpected module/driver activity or unverified device effect. Recovery: return to known physically deployed V5DCM19 FIX1 or archived v31 FIX1 blob `debedae0c22a6d20d29cadbbb46ef0426cf70c06` as an **offline source rollback only** (not live-proven).

**Evidence requested only if/when future live test is initiated:** brief RX capture containing 0532/count18, the option-capability HA states, and one corresponding optional sensor/active flag with timestamps, plus bus health. No DCM is required.

Other R&D documentation stays in `Research`; the user expressly requested one YAML/one README inside the XTR folder. No history rewrite or destructive deletion; original subtree is archived.
