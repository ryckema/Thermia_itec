# v31 Full Monitoring — implementation and coverage contract

Date: 2026-10-18. Status: **PREPARED / NOT RUN**; no device flash, no live test or full ESPHome compile.

## User requirement
One passive ESPHome/HA profile, maximally complete parameter monitoring for the legacy Thermia iTec XTR M. Exclude **calendar** and **alarms** from the HA entity registry. Optional second and third heating circuits, pool, and buffer tank should not clutter HA unless installed/configured.

## Existing sources checked
- Read-only production XTR public v29 YAML and README (Thermia_itec).
- V5 passive session bridge + canonical Research/THERMIA_PROJECT_STATE.md and PROTOCOL_FINDINGS.md, 2026-10-18 current sections (Thermia_itec).
- Thermia_Connect_Firmware/parameters/thermia_itec_xtr_m_waveshare_public_v30_alpha12.yaml, parameter integration roadmap and MENU_REVIEW_README.md.
- Thermia commissioning manual AWIXT01CG0210 in project materials.

## Alpha01 delivery
`thermia_itec_xtr_m_waveshare_v31_full_monitoring_alpha01.yaml` is derived from v30-alpha12 with the parser and existing entity IDs preserved. Source transformations:
- All HA entities whose names include Alarm, Fault, or Calendar are marked `internal: true` (30 newly internal entities); frame decode and cached IDs remain intact.
- Eight previously enabled optional Circuit 1/2 settings have `disabled_by_default: true`, aligning them with optional pool/buffer metrics already disabled in alpha12.
- Installed/capability flag entities are left exposed to provide discoverability.
- RX pin GPIO18 only, GPIO21 DE OFF, no UART tx_pin or TX commands. No control, response, handshake, dynamic scanning or active polling.
- Uncertain firmware-only interpretations remain marked diagnostic/raw where preexisting; these are not local XTR protocol proof.

## Capability semantics and HA limitation
Native capability flags in v30: `0x0533` pool, `0x0534` distribution/shunt group 1 (second heating circuit), `0x0535` distribution/shunt group 2 (third heating circuit), `0x0536` buffer tank. These flags are firmware-derived interpretations and require proper observed-page freshness/validity and profile applicability. Never use zero before page capture as definite 'not installed'.

ESPHome `disabled_by_default` is only the initial HA registry registration default. HA **cannot dynamically enable/disable an existing registry entry based solely on a later capability sensor update**. Runtime availability can be conditioned on known capability flags (existing alpha12 decoder does so for a subset); optional entities remain manually enableable after installation. This is an implementation tradeoff, not a claim of automatic registration on feature activation.

## Not yet completed
1. Audit and enumerate every user-visible menu parameter in INFO and SERVICE, excluding calendar/alarms, against the reviewed firmware parameter register database and 2024 manual. Neither 564 firmware-register rows nor 494 uncertain menu matches are 564 locally proven HA entities.
2. Identify which parameters are already in alpha01, which have a locally proven native value, which are firmware-derived candidates, and which are unavailable on the passive bus. Add only justified typed/derived entities.
3. Review feature-conditional availability for **every** optional entity and both shunt circuits, pool, buffer; verify sentinel handling, freshness and retained-state behavior.
4. Verify YAML with strict duplicate mapping detection, substitution/ID check, ESPHome compile, controlled flash, then live HA readings. Only the ID/substitution and TX-pin static checks have been executed; do not claim compile or deployment success.
5. Compare stable production sensors to v29 and inspect NaNs already seen in V5DCM20 transitions; promote only after evidence.
6. Preserve proven bus-health invariants and minimal production diagnostics.

## Provenance and release
This is a **new read-only delivery track**, separate from the native Online/DCM write/emulation track. No existing production v29, firmware source, private 0x0F emulation or V5 experimental file is overwritten. Alpha01 is **not** yet evidence of full parameter coverage or live acceptance.

Positive criteria for future controlled live test: current flashed version identified, bus RX stable, all existing v29 critical readings present, zero physical TX, optional absent features unavailable and initially HA-disabled, installed options recover correctly, no alarm/calendar exposed, no regression in CRC/resync/drop counters. On unexpected TX, broken bus telemetry or HA runtime regression abort and reflash verified production v29 (or actually deployed known-good).
