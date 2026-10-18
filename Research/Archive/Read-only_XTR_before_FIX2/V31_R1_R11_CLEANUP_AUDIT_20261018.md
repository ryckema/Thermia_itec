# v31 R1–R11 cleanup — source audit and handoff

**Date:** 2026-10-18  
**Status:** PREPARED / NOT RUN — offline source editing/structural checks only. No ESPHome compile, flash or live Thermia test.  
**Direct user authorization:** all eleven cleanup groups R1–R11 approved together.  
**YAML:** [v31-alpha01 FIX1](thermia_itec_xtr_m_waveshare_v31_full_monitoring_alpha01.yaml)  
**Pre-change YAML blob:** `d81bd7673ae33d4e51460e81e18fb0e425c86c4d`.  
**Post-change YAML blob:** `debedae0c22a6d20d29cadbbb46ef0426cf70c06`.  
**Source commits:** `1ba0a5a0314d0931e4d33e695b85f7ec3a51035f` (functional cleanup), `2f876fed0c610c565a4c9533c93fa1498e6eb120` (comments/header).  
**Inventory commit:** `1866221ba78c84a7f0f2dc5736bbf6a003916441` (full list refreshed).

## Changes as approved
| ID | Approved action | Result |
|---|---|---|
| R1 | Remove Active Mapped Faults | Text entity and alarm-specific publisher removed |
| R2 | Remove Register 0539 Interpretation | Text entity and publisher removed; original 0539 RAW retained |
| R3 | Remove Installed Capability Summary | Summary text entity and publisher removed; 0533/0534/0535/0536 installed flags and related global gates preserved |
| R4 | Remove five Native-v29 temperature-delta entities | Five entities and comparison code removed; source temperature entities and direct native mirrors untouched |
| R5 | Remove five Native-v29 status agreement flags | Five entities and comparison code removed; native and production status entity decoders untouched |
| R6 | Remove Native vs v29 Mode Comparison | Text entity and comparison publisher removed; distinct Operation Mode, Operating Mode and Mode Request retained |
| R7 | Two propagated outdoor-temperature entities disabled by default | Both remain with source-bus semantics and values unchanged |
| R8 | Room Sensor Control Flag B3C6 disabled by default | Entity remains; bus decode unchanged |
| R9 | Remove three ESP/WiFi metadata entries | Device Info, WiFi BSSID and WiFi Power Save Mode removed; IP Address and Reset Reason preserved |
| R10 | Remove three ESP technical diagnostics | Heap Min Free, Heap Fragmentation and Loop Time removed; Heap Free, Uptime, WiFi Signal and Bus Healthy retained |
| R11 | Remove 30 internal alarm/fault entities | 3 raw alarm-word entities + 27 fault binaries and alarm-specific decoder/publishers removed; generic CRC-valid native frame receive processing remains |

No calendar or alarm entities appear in the new HA inventory. The initial v31-alpha01 is **not** known-good production and remains a prepared candidate.

## Entity counts
Before: **300** named HA entities (192 numeric + 92 binary + 16 text), 92 enabled / 178 disabled by default / 30 internally hidden.  
After: **250** named HA entities (181 numeric + 60 binary + 9 text), **86 enabled / 164 disabled by default / 0 internal**.  
Difference: **50 removed** and **3 retained but newly disabled by default**. The unnamed internal RS485 driver-direction GPIO switch remains untouched.

## Executed offline checks
- Confirmed no unresolved `id(...)` references: 263 distinct referenced IDs resolve against 265 declarations; no duplicate declarations.
- Confirmed both `${device_name}` and `${friendly_name}` are defined.
- Source contains one each of the original 18 top-level blocks (no duplicate top-level mapping keys).
- 250 unique named HA entities remain. 86 default enabled and 164 default disabled.
- No configured UART `tx_pin`, no ESPHome `uart.write`, and driver-enable `restore_mode: ALWAYS_OFF` retained.
- Source still contains physical RX GPIO18 and DE GPIO21, native 0x0F/0x1E page consumers, `thermia_last_valid_frame_ms`, `thermia_valid_frame_count`, `thermia_bus_healthy`, and optional-circuit `thermia_capabilities_seen`/configuration paths.
- Key retained values checked by source ID: Heating Curve, Room Temperature, DHW Temperature, Compressor Running, Buffer Tank Temperature, 0539 raw, native 0820 outdoor page, native room 080C.
- Confirmed original 30 internal alarm/fault entity names and the other explicitly removed names are absent; R7/R8 all retain the newly added `disabled_by_default: true`.
- Post-write readback via GitHub confirmed final blob and entity counts.

**Limitations:** These are text/source checks, **not** a full strict YAML parser run, ESPHome configuration validation/compile, firmware flash, HA registry audit, on-device bus soak, or independent proof of all register semantics. No physical TX has been executed as part of this work.

## Rollback and next action
If compilation or future device tests fail, revert **only the v31 YAML file** to pre-cleanup blob `d81bd7673ae33d4e51460e81e18fb0e425c86c4d`. Existing known-good production v29/V5DCM19 FIX1 is not overwritten. Before any live v31 test, independently run ESPHome config/compile (when feasible), compare prior production HA entities, verify physical TX remains zero and driver-enable stays low, and inspect CRC/resync/drop counters. The 524-row firmware XTR inventory remains a **separate, unfinished** v31 coverage objective. R4–R6 comparison regression aids have been removed at explicit user request; retain source history for later investigation.
