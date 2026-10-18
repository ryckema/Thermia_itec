# v31 optional-capability and pool conditionality audit

Date: 2026-10-18. Status: **PREPARED / NOT RUN** for any proposed runtime corrections. This is source review only, not an experiment or on-device result.

Source examined: public `Read-only/Thermia itec XTR/thermia_itec_xtr_m_waveshare_v31_full_monitoring_alpha01.yaml` current blob `debedae0c22a6d20d29cadbbb46ef0426cf70c06`.

## OBSERVED SOURCE FACTS

- `0x0F:0532/count18` controller-originated native page decodes the firmware-derived capability flags `0533` Pool Installed, `0534` Distribution Circuit 1/second heating circuit, `0535` Distribution Circuit 2/third heating circuit, `0536` Buffer Tank. This code sets `thermia_capabilities_seen=true` and related integer configuration globals. Binary capability entities are only updated for values 0 or 1; invalid values leave the previous binary state intact.
- Pool entities `Pool Start Limit Raw 041B`, `Pool Stop Limit Raw 041C`, `Pool Temperature Raw 080D`, `Pool Heating Active`, `Pool Demand Queued` are all defined with `disabled_by_default: true`, but their publication paths are not consistently gated on `thermia_capabilities_seen && thermia_pool_config==1`. Unconditionally decoded retained/default values can therefore still be published internally even with the installed flag known OFF. Source lines ~1713–1720, 1981, 1998, 080C runtime page, and relevant entity declarations.
- `Pool Installed` remains enabled by default in HA, to reveal the reported capability status.
- Named optional shunt circuit 1/2 setting entities and some hydraulic/wanted temperature entities are conditionally published only when corresponding circuit capability exists; when capability has been seen and is OFF, several entities publish `NAN`. Buffer Tank Temperature is similarly guarded. This is partial availability-state behavior, **not** HA entity-registry automatic hiding or re-enabling.
- No explicit `set_available` or equivalent per-entity availability mechanism was found in source. No capability freshness/expiration contract observed. Boot begins with `thermia_capabilities_seen=false`, so absence of a page must not be equated with OFF.
- ESPHome `disabled_by_default` applies to initial HA entity registration; it does not automatically enable existing disabled entities if native capability later becomes ON. Values blocked by NAN/unknown are not the same as automatic HA registry visibility control.

## STRONG CONCLUSIONS

**The user's conditionally visible optional hardware requirement is not fully met by v31-alpha01 FIX1.** For pool specifically, capability detection exists and its dependent HA entities start disabled, but automatic status-controlled measurement availability is incomplete and automatic registry enablement is absent. Full correctness on hardware is not established because v31 has not been flashed or live-tested.

## NEXT ACTION (no live test scheduled)

Prepare a separate small, source-only candidate with one controlled change: consistent *fail-closed* gating of pool/circuit/buffer **named values** and status on fresh valid capability state, preserving all unique raw register decoding and HA entity IDs. Treat unknown/invalid/stale capability as unavailable, never as OFF or ON. Keep optional HA entity registration defaults; if automatic visible/hidden dashboard grouping is wanted, use HA dashboard conditional cards or other HA-level logic (the ESPHome entity registry is not dynamically enabled by `disabled_by_default`). Never claim physical validation until user executes an approved passive-only test; preserve existing deployed V5DCM19 FIX1 and pre-change v31 for rollback.
