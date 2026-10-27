# V5DCM26 — identity-level HA source-parity inventory

**Status: COMPLETE / POSITIVE (OFFLINE name/ID comparison), NOT a migration or production YAML.**

Sources: user-private `V5DCM23_FIX2_COPY_ALL_TO_ESPHOME(1).zip` SHA256 `561169c31d5a7eb341055fdb37d0302b4816d661fff9cd2df9d607a9498ea9a4` (not published) compared against public **prepared/not-flashed** `V5DCM22_RX33_STATCLASS_FIX1_PREPARED_20261018.yaml` Git blob `653e683eb79f7c2962899fc44958484aab4ca627`. No secrets or private YAML published. This is **name-level** matching with ID cross-check for shared named entities, NOT an HA registry / unique_id migration check.

| Category | Extended RX33 named | Present in FIX2 by exact name | Only in extended RX33 |
|---|---:|---:|---:|
| Sensor | 187 | 33 | 154 |
| Binary sensor | 60 | 9 | 51 |
| Text sensor | 15 | 2 | 13 |
| **Total** | **262** | **44** | **218** |

Private FIX2 contains 180 named entities (117 sensor, 13 binary sensor, 47 text sensor, 3 button), including **136 private-only diagnostics/controls**. All 44 exact-name common entities have compatible explicitly declared `id` fields across types (two built-in name-only ESPHome diagnostics have no explicit id). FIX2 has 31 sensor state-class declarations; extended RX33 STATCLASS candidate has 74 `state_class: measurement` declarations. Those 74 are **not** a target to blindly copy to unrelated diagnostics.

**Migration blockers:** No automatic append of these 218 definitions: source-dependent globals, IDs, update callbacks, sensor semantics, unit/state_class consistency and HA unique-ID stability require per-entity review. The public RX33 source is itself PREPARED/NOT RUN, and does not prove the actual deployed HA registry. Never delete historical HA statistics as a metadata workaround. Preserve all 180 currently working FIX2 nodes before reintroducing any of these candidates.

## Sensoren: 154 only in RX33 STATCLASS candidate

| Existing public name | Existing ESPHome ID | state_class |
|---|---|---|
| Thermia ESP Heap Free | `not set` | not set |
| Controller Sequence Value Raw | `thermia_demand_raw` | not set |
| Controller Context Raw A80C | `thermia_controller_state_a80c` | not set |
| Controller Accessory Status Raw A80E | `thermia_controller_state_a80e` | not set |
| Outdoor Unit Operating State Raw | `thermia_outdoor_unit_operating_state_raw` | not set |
| Outdoor Unit Status Flags | `thermia_outdoor_unit_status_flags` | not set |
| Mode Request Raw | `thermia_mode_request_raw` | not set |
| Commanded Target Temperature | `thermia_commanded_target_temperature` | measurement |
| Room Bus Propagated Outdoor Temperature | `thermia_room_bus_outdoor_temperature` | measurement |
| Accessory Slot Propagated Outdoor Temperature | `thermia_dcm_outdoor_temperature` | measurement |
| Accessory Slot Context Raw AFDC | `thermia_dcm_status_afdc` | not set |
| Native ODU 0820 Raw (Condenser In / Profile Collision) | `thermia_native_0820_raw` | not set |
| Native ODU 0821 Raw (Condenser Out / Profile Collision) | `thermia_native_0821_raw` | not set |
| Native ODU Refrigerant 1 Raw 0822 | `thermia_native_0822_raw` | not set |
| Native ODU Discharge Pipe Raw 0823 | `thermia_native_0823_raw` | not set |
| Native ODU Refrigerant 2 Raw 0824 | `thermia_native_0824_raw` | not set |
| Native ODU Ambient Raw 0825 | `thermia_native_0825_raw` | not set |
| Native ODU Compressor Top Raw 0826 | `thermia_native_0826_raw` | not set |
| Native ODU Confirmed Setpoint Raw 0827 | `thermia_native_0827_raw` | not set |
| Native ODU Compressor Frequency Raw 0828 | `thermia_native_0828_raw` | not set |
| Native ODU Max Frequency Ratio Raw 0829 | `thermia_native_0829_raw` | not set |
| Native ODU Current Raw 082A | `thermia_native_082a_raw` | not set |
| Native ODU Fan 1 Speed Raw 082B | `thermia_native_082b_raw` | not set |
| Native ODU Fan 2 Speed Raw 082C | `thermia_native_082c_raw` | not set |
| Native ODU Expansion Valve Raw 082D | `thermia_native_082d_raw` | not set |
| Native ODU Status Raw 082E | `thermia_native_odu_status_raw` | not set |
| Native ODU High Pressure Raw 0830 | `thermia_native_0830_raw` | not set |
| Native ODU Register 0831 Raw | `thermia_native_0831_raw` | not set |
| Native ODU Operation Raw | `thermia_native_odu_operation_raw` | not set |
| Native Operation Status Raw | `thermia_native_operation_status_raw` | not set |
| Native Queued Demands Raw | `thermia_native_queued_demands_raw` | not set |
| Defrost Count | `thermia_defrost_count` | not set |
| Previous Defrost Interval | `thermia_previous_defrost_interval` | measurement |
| Time Since Last Defrost | `thermia_time_since_last_defrost` | measurement |
| Distribution Circuit 1 Heating Curve | `thermia_distribution_circuit_1_curve` | not set |
| Distribution Circuit 1 Minimum Temperature | `thermia_distribution_circuit_1_min_temperature` | measurement |
| Distribution Circuit 1 Maximum Temperature | `thermia_distribution_circuit_1_max_temperature` | measurement |
| Distribution Circuit 1 Curve Correction +5 | `thermia_distribution_circuit_1_correction_plus5` | measurement |
| Distribution Circuit 1 Curve Correction 0 | `thermia_distribution_circuit_1_correction_zero` | measurement |
| Distribution Circuit 1 Curve Correction -5 | `thermia_distribution_circuit_1_correction_minus5` | measurement |
| Distribution Circuit 1 Constant Temperature | `thermia_distribution_circuit_1_constant_temperature` | measurement |
| Register 0402 Raw | `thermia_0402_raw` | not set |
| Register 0403 Raw | `thermia_0403_raw` | not set |
| Register 0405 Raw | `thermia_0405_raw` | not set |
| Register 0406 Raw | `thermia_0406_raw` | not set |
| Distribution Circuit 2 Heating Curve | `thermia_distribution_circuit_2_curve` | not set |
| Distribution Circuit 2 Minimum Temperature | `thermia_distribution_circuit_2_min_temperature` | measurement |
| Distribution Circuit 2 Maximum Temperature | `thermia_distribution_circuit_2_max_temperature` | measurement |
| Distribution Circuit 2 Curve Correction +5 | `thermia_distribution_circuit_2_correction_plus5` | measurement |
| Distribution Circuit 2 Curve Correction 0 | `thermia_distribution_circuit_2_correction_zero` | measurement |
| Distribution Circuit 2 Curve Correction -5 | `thermia_distribution_circuit_2_correction_minus5` | measurement |
| Distribution Circuit 2 Constant Temperature | `thermia_distribution_circuit_2_constant_temperature` | measurement |
| Pool Start Limit Raw 041B | `thermia_pool_start_limit_raw` | not set |
| Pool Stop Limit Raw 041C | `thermia_pool_stop_limit_raw` | not set |
| Register 0416 Raw | `thermia_0416_raw` | not set |
| Register 0417 Raw | `thermia_0417_raw` | not set |
| Register 0419 Raw | `thermia_0419_raw` | not set |
| Register 041A Raw | `thermia_041a_raw` | not set |
| DHW Start Temperature | `thermia_dhw_start_temperature_setting` | measurement |
| DHW Maximum Production Time | `thermia_dhw_max_production_time_setting` | measurement |
| Anti-legionella Interval | `thermia_antilegionella_interval_setting` | measurement |
| Anti-legionella Minimum Time | `thermia_antilegionella_min_time_setting` | measurement |
| DHW Service 0421 Raw | `thermia_dhw_service_0421_raw` | not set |
| DHW Service 0422 Raw | `thermia_dhw_service_0422_raw` | not set |
| DHW Service 0423 Raw | `thermia_dhw_service_0423_raw` | not set |
| DHW Service 0424 Raw | `thermia_dhw_service_0424_raw` | not set |
| Startup HT | `thermia_startup_ht_setting` | measurement |
| Heating Time | `thermia_heating_time_setting` | measurement |
| Cooling Desired Temperature | `thermia_cooling_desired_temperature_setting` | measurement |
| Cooling Active Above | `thermia_cooling_active_above_setting` | measurement |
| Cooling Time | `thermia_cooling_time_setting` | measurement |
| Cooling Room Hysteresis Low | `thermia_cooling_room_hyst_low_setting` | measurement |
| Cooling Room Hysteresis High | `thermia_cooling_room_hyst_high_setting` | measurement |
| Cooling Hysteresis Raw 0444 | `thermia_cooling_hysteresis_raw_0444` | not set |
| Cooling Configuration Raw 0446 | `thermia_cooling_configuration_raw_0446` | not set |
| Cooling Start Threshold Raw 0447 | `thermia_cooling_start_threshold_raw_0447` | not set |
| Cooling Stop Threshold Raw 0448 | `thermia_cooling_stop_threshold_raw_0448` | not set |
| Cooling Maximum Start Temperature Raw 044A | `thermia_cooling_max_start_temp_raw_044a` | not set |
| Cooling Minimum Stop Temperature Raw 044B | `thermia_cooling_min_stop_temp_raw_044b` | not set |
| Register 0532 Raw | `thermia_0532_raw` | not set |
| Register 0537 Raw | `thermia_0537_raw` | not set |
| Register 0538 Raw | `thermia_0538_raw` | not set |
| Register 053A Raw | `thermia_053a_raw` | not set |
| Register 053B Raw | `thermia_053b_raw` | not set |
| Register 053C Raw | `thermia_053c_raw` | not set |
| Register 053D Raw | `thermia_053d_raw` | not set |
| Register 053E Raw | `thermia_053e_raw` | not set |
| Register 053F Raw | `thermia_053f_raw` | not set |
| Register 0540 Raw | `thermia_0540_raw` | not set |
| Pool Configuration Raw 0533 | `thermia_pool_config_raw` | not set |
| Distribution Circuit 1 Configuration Raw 0534 | `thermia_distribution_circuit_1_config_raw` | not set |
| Distribution Circuit 2 Configuration Raw 0535 | `thermia_distribution_circuit_2_config_raw` | not set |
| Buffer Tank Configuration Raw 0536 | `thermia_buffer_tank_config_raw` | not set |
| Register 0539 Raw (Semantic Collision) | `thermia_configured_product_raw_0539` | not set |
| Return Temperature | `thermia_return_temperature` | measurement |
| System Supply Temperature | `thermia_system_supply_temperature` | measurement |
| Buffer Tank Temperature | `thermia_buffer_tank_temperature` | measurement |
| Distribution Circuit 1 Temperature | `thermia_distribution_circuit_1_temperature` | measurement |
| Native Supply Temperature 07D0 | `thermia_native_supply_temperature_07d0` | measurement |
| Native DHW Top Temperature 07D3 | `thermia_native_dhw_top_temperature_07d3` | measurement |
| Native DHW Temperature 07D4 | `thermia_native_dhw_temperature_07d4` | measurement |
| Tank Temperature 07D9 | `thermia_tank_temperature_07d9` | measurement |
| Native Outdoor Temperature 07DA | `thermia_native_outdoor_temperature_07da` | measurement |
| Register 07D1 Raw | `thermia_07d1_raw` | not set |
| Register 07D5 Raw | `thermia_07d5_raw` | not set |
| Register 07DB Raw | `thermia_07db_raw` | not set |
| Register 07DC Raw | `thermia_07dc_raw` | not set |
| Hub Card Port D Raw 07DF | `thermia_07df_raw` | not set |
| Register 07E0 Raw | `thermia_07e0_raw` | not set |
| Register 07E1 Raw | `thermia_07e1_raw` | not set |
| Register 07E2 Raw | `thermia_07e2_raw` | not set |
| Native Room Temperature 080C | `thermia_native_room_temperature_080c` | measurement |
| Current Consumption Raw 0814 | `thermia_current_consumption_raw_0814` | not set |
| Expansion Card Port B Raw 081A | `thermia_expansion_card_port_b_raw_081a` | not set |
| Expansion Card Port D Raw 081B | `thermia_expansion_card_port_d_raw_081b` | not set |
| Register 0810 Raw | `thermia_0810_raw` | not set |
| Register 0811 Raw | `thermia_0811_raw` | not set |
| Register 0812 Raw | `thermia_0812_raw` | not set |
| Register 0813 Raw | `thermia_0813_raw` | not set |
| Register 0815 Raw | `thermia_0815_raw` | not set |
| Register 0816 Raw | `thermia_0816_raw` | not set |
| Register 0817 Raw | `thermia_0817_raw` | not set |
| Register 0818 Raw | `thermia_0818_raw` | not set |
| Register 0819 Raw | `thermia_0819_raw` | not set |
| Register 081C Raw | `thermia_081c_raw` | not set |
| Register 081D Raw | `thermia_081d_raw` | not set |
| Pool Temperature Raw 080D | `thermia_pool_temperature_raw_080d` | not set |
| Cooling Temperature Raw 080E | `thermia_cooling_temperature_raw_080e` | not set |
| Distribution Circuit 2 Temperature Raw 080F | `thermia_distribution_circuit_2_temperature_raw_080f` | not set |
| Heat Demand Raw 0848 | `thermia_heat_demand_raw_0848` | not set |
| Weighted DHW Temperature | `thermia_weighted_dhw_temperature` | measurement |
| Lowest Wanted Tank Temperature | `thermia_lowest_wanted_tank_temperature` | measurement |
| Lowest Wanted Tank Reduction Temperature | `thermia_lowest_wanted_tank_reduction_temperature` | measurement |
| Register 084D Raw | `thermia_084d_raw` | not set |
| Register 084E Raw | `thermia_084e_raw` | not set |
| Register 084F Raw | `thermia_084f_raw` | not set |
| Register 0850 Raw | `thermia_0850_raw` | not set |
| Register 0854 Raw | `thermia_0854_raw` | not set |
| Register 0855 Raw | `thermia_0855_raw` | not set |
| Register 0856 Raw | `thermia_0856_raw` | not set |
| Register 0857 Raw | `thermia_0857_raw` | not set |
| Register 0858 Raw | `thermia_0858_raw` | not set |
| Register 0859 Raw | `thermia_0859_raw` | not set |
| Register 085A Raw | `thermia_085a_raw` | not set |
| Register 085B Raw | `thermia_085b_raw` | not set |
| Register 085C Raw | `thermia_085c_raw` | not set |
| Register 085D Raw | `thermia_085d_raw` | not set |
| Register 085E Raw | `thermia_085e_raw` | not set |
| Supply Temperature Wanted | `thermia_supply_temperature_wanted` | measurement |
| System Supply Temperature Wanted | `thermia_system_supply_temperature_wanted` | measurement |
| Distribution Circuit 1 Temperature Wanted | `thermia_distribution_circuit_1_temperature_wanted` | measurement |
| Distribution Circuit 2 Temperature Wanted | `thermia_distribution_circuit_2_temperature_wanted` | measurement |
| Auxiliary Status Raw 07DD | `thermia_aux_status_raw_07dd` | not set |
| Auxiliary Status Raw 07DE | `thermia_aux_status_raw_07de` | not set |

## Binaire sensoren: 51 only in RX33 STATCLASS candidate

| Existing public name | Existing ESPHome ID | state_class |
|---|---|---|
| Pool Installed | `thermia_pool_enabled_capability` | not set |
| Distribution Circuit 1 Installed | `thermia_distribution_circuit_1_enabled_capability` | not set |
| Distribution Circuit 2 Installed | `thermia_distribution_circuit_2_enabled_capability` | not set |
| Buffer Tank Installed | `thermia_buffer_tank_enabled_capability` | not set |
| EQ Enabled | `thermia_eq_enabled_capability` | not set |
| Zoning Enabled | `thermia_zoning_enabled_capability` | not set |
| Energy Performance Enabled | `thermia_energy_performance_enabled_capability` | not set |
| Hot Water Enabled | `thermia_dhw_enabled_setting` | not set |
| Cooling Enabled | `thermia_cooling_enabled_setting` | not set |
| Cooling Room Sensor | `thermia_cooling_room_sensor_setting` | not set |
| Native ODU Compressor Status | `thermia_native_odu_compressor_status` | not set |
| Native ODU Four-way Valve Status | `thermia_native_odu_fourway_valve_status` | not set |
| Native ODU Fan Status | `thermia_native_odu_fan_status` | not set |
| Native ODU Flow Detected | `thermia_native_odu_flow_detected` | not set |
| Native ODU Refrigerant Used Flag | `thermia_native_odu_refrigerant_used` | not set |
| Native ODU Split Flag | `thermia_native_odu_split` | not set |
| Native ODU Unit On/Off | `thermia_native_odu_unit_onoff` | not set |
| Native ODU Heating Mode | `thermia_native_odu_heating_mode` | not set |
| Native ODU Hot Water Mode | `thermia_native_odu_hot_water_mode` | not set |
| Native ODU Cooling Mode | `thermia_native_odu_cooling_mode` | not set |
| Native ODU Thermal On/Off | `thermia_native_odu_thermal_onoff` | not set |
| Native ODU Compressor Down Flag | `thermia_native_odu_comp_down` | not set |
| Defrost Active | `thermia_defrost_active` | not set |
| Native Heating Active | `thermia_native_heating_active` | not set |
| Native DHW Active | `thermia_native_dhw_active` | not set |
| Native Cooling Active | `thermia_native_cooling_active` | not set |
| DHW Top-up Active | `thermia_dhw_topup_active` | not set |
| Pool Heating Active | `thermia_pool_heating_active` | not set |
| Defrost Using Building | `thermia_defrost_using_building` | not set |
| Defrost Using Hot Water | `thermia_defrost_using_dhw` | not set |
| Outdoor Stop Active | `thermia_outdoor_stop_active` | not set |
| Concrete Drying Active | `thermia_concrete_drying_active` | not set |
| Heating Demand Queued | `thermia_heating_demand_queued` | not set |
| DHW Demand Queued | `thermia_dhw_demand_queued` | not set |
| Pool Demand Queued | `thermia_pool_demand_queued` | not set |
| Cooling Demand Queued | `thermia_cooling_demand_queued` | not set |
| Concrete Drying Demand Queued | `thermia_concrete_drying_demand_queued` | not set |
| Immersion Heater 1 Active | `thermia_immersion_heater_1_active` | not set |
| Immersion Heater 2 Active | `thermia_immersion_heater_2_active` | not set |
| Immersion Heater 3 Active | `thermia_immersion_heater_3_active` | not set |
| External Auxiliary Heater Active | `thermia_external_auxiliary_active` | not set |
| External Auxiliary Potential-free Active | `thermia_external_auxiliary_potential_free_active` | not set |
| Bus Healthy | `thermia_bus_healthy` | not set |
| Compressor Starting | `thermia_compressor_starting` | not set |
| Room Sensor Control Flag B3C6 | `thermia_room_boost_request` | not set |
| Outdoor Unit Cycle Request 0007 | `thermia_outdoor_unit_command_0007` | not set |
| Outdoor Unit Run Enable 0008 | `thermia_outdoor_unit_command_0008` | not set |
| Controller A80C Flag 0x10 | `thermia_a80c_flag_0x10` | not set |
| Controller A80C Flag 0x20 | `thermia_a80c_flag_0x20` | not set |
| Controller A80E Flag 0x08 | `thermia_a80e_flag_0x08` | not set |
| Controller A80E Flag 0x20 | `thermia_a80e_flag_0x20` | not set |

## Tekstsensoren: 13 only in RX33 STATCLASS candidate

| Existing public name | Existing ESPHome ID | state_class |
|---|---|---|
| Cooling Settings Page Source | `thermia_cooling_page_source` | not set |
| Native Settings Pages Seen | `thermia_native_pages_seen_summary` | not set |
| Native DCM W2 Pages Seen | `thermia_v5dcm22_w2_pages` | not set |
| Native DCM W3 Pages Seen | `thermia_v5dcm22_w3_pages` | not set |
| Native DCM W4 Pages Seen | `thermia_v5dcm22_w4_pages` | not set |
| Native DCM 33 Page Audit | `thermia_v5dcm22_page_summary` | not set |
| Thermia ESP Reset Reason | `not set` | not set |
| Thermia IP Address | `not set` | not set |
| Hot Water Mode | `thermia_dhw_mode_setting` | not set |
| Operation Mode | `thermia_operation_mode_setting` | not set |
| Controller Context | `thermia_controller_context` | not set |
| Outdoor Unit State | `thermia_outdoor_unit_state` | not set |
| Mode Request | `thermia_mode_request` | not set |

## Follow-up

Develop a compatibility mapping of producer/provider for missing entities, then restore read-only groups by source provenance in separate reviewable offline patches. Do not combine entity restoration with the V5DCM26 native-request observation hypothesis in a single live test. Preserve TX HARD_DENY and existing RX parser. No new YAML has been compiled, flashed or executed as a result of this inventory.
