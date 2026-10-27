# Thermia XTR M — native CURRENT parameterkaart v2 (2026-10-27)

**Scope:** read-only consolidation of user-supplied MAIN03-C5DK SOURCE with current GitHub semantic register map and EXP382. No firmware or physical TX changed.

## 4 CURRENT pages (62 register positions)

| Group | Native start/count | Proven fields | Candidates | Unknown |
|---|---|---|---|---|
| Heating H | `03E8/14` | `03E8..03F0`, `03F4` | — | `03F1..03F3`, `03F5` |
| Hot water D | `042E/15` | `042E`, `042F`, `0433`, `0434` | `0430` TOP_UP (strong) | `0431`, `0432`, `0435..043C` |
| Cooling C | `0442/13` | `0442`, `0443`, `0445`, `0449`, `044C..044E` | `0444`, `0446`, `0448`, `044A`, `044B` strong; `0447` hypothesis | — |
| Mode M | `0546/20` | `0553` | `0559` Link Integration (strong) | `0546..0552`, `0554..0558` |

Totals: **22 PROVEN, 7 STRONGLY SUPPORTED, 1 HYPOTHESIS and 32 OPEN**, independent of target-build/LIVE proof. C5DK currently declares **21** read-only `m6p_native_...` sensors; `03F4` appears through an existing different room-setpoint cache but lacks an M6 CURRENT-qualified sensor.

## Actionable semantic naming corrections

- `0433`: existing semantic map calls it **Startup HT**; C5DK calls it Hot water runtime limit with unit min. Exact unit needs confirmation before being asserted as authoritative.
- `0434`: **Heating Time**, rather than generic Hot water time limit.
- `044C`: **Cooling Room Sensor**, not generic Cooling service enabled.
- `0445`: **Cooling Active Above**, more precise than Cooling guard setpoint.
- A later read-only `03F4` snapshot sensor may use `m6s_heating_words[12]` with exactly the pre-existing 4/4 / native epoch / owner / 300-second freshness guard. No separate TX or new trust state.
- `03F1` as DHW START was locally **DISPROVEN**; `041D` on another native page was correlated instead.

## Validity, safety and status

C5DK SOURCE gates all native sensors on four real owner-ACKed H/D/C/M pages, same session epoch, observed CM930 profile 242, healthy RX/CRC/peer conditions and a 300s snapshot TTL; on invalidity sensors return NAN and native fresh-page count 0. This is source behavior, NOT proof of sustainable XTR LIVE refresh. Transport ACK alone is not DCM/Online semantic acceptance.

**HA parameter/setting writes remain ON HOLD.** No new physical TX or firmware change is authorized by this parameter map. Existing single UART/RX/DE owner, S92 ABORT, cold start, recovery, role guards and rollback are unchanged.

C5DK status: **PREPARED / NOT RUN** (SOURCE / OFFLINE TESTED only). C5DJ durability observation remains **RUNNING / PARTIAL** until user evidence closes it.

Sources: [register semantic map](https://github.com/ryckema/Thermia_itec/blob/main/Research/protocol%20reduction/thermia_protocol_semantic_register_map.csv) · [EXP382](https://github.com/ryckema/Thermia_itec/blob/main/Research/EXP382_OFFLINE_GAP_ANALYSIS.md) · [current project state](https://github.com/ryckema/Thermia_itec/blob/main/Research/THERMIA_PROJECT_STATE.md).

**CURRENT MILESTONE:** Durable FC03 read-only H/D/C/M freshness. **DELIVERABLE:** Parameterkaart v2, 62-position evidence inventory. **REAL BLOCKER:** C5DK recurrent 4/4 and multi-hour native owner are not XTR LIVE validated. **ONE NEXT ACTION:** Preserve C5DJ durability observation, then one bounded user-initiated C5DK target compile/OTA with second real 4/4 refresh.