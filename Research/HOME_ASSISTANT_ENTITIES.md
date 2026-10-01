# Home Assistant entity catalogue — Thermia iTec XTR M

**Purpose:** canonical dashboard-building reference for this project.

**Source:** generated from `thermia_itec_xtr_m_waveshare_exp381b_production_cleanup.yaml`, prepared from the EXP380 COMPLETE / POSITIVE baseline on 2026-10-01.

**EXP381B status:** PREPARED / NOT RUN. This file describes the entities exposed by the prepared YAML; it does **not** promote EXP381B itself to a completed experiment.

## How to use this file

- Treat **ESPHome name** and **ESPHome `id`** as source-derived identifiers from the current prepared YAML.
- **Expected HA entity ID** is the default entity-id form inferred from the ESPHome name. Home Assistant may use a different entity ID if the entity was renamed, migrated, or collided with an existing ID. Verify uncertain IDs against the live HA entity registry.
- `text_sensor` entries are exposed in Home Assistant under the `sensor` domain.
- `entity_category: diagnostic` entities are primarily for troubleshooting/research dashboards.
- `entity_category: config` entities are controls shown under Configuration.
- Entities marked `disabled_by_default` may not exist in the live HA state machine until enabled.
- Do not infer protocol semantics from an entity name alone. For evidence/confidence, use `PROTOCOL_FINDINGS.md`.
- EXP381B intentionally keeps historical internal IDs such as `exp378_*`, `exp379_*` and `exp380_*` where changing them would add unnecessary regression risk. The user-facing Configuration names are production-oriented.
- Configuration display names are prefixed to follow the Thermia manual's functional order: **Operation → Heating → Hot Water → Cooling**.
- `Startup HT` and `Heating Time` are grouped under **Heating / Service**, matching the commissioning manual rather than their earlier experimental grouping.
- Cooling Room Hysteresis Low/High are exposed at **0.5..5.0 °C**, step **0.1 °C**.
- The useful read-only entities `Expansion Valve Steps`, `Refrigerant Temperature 1`, `Discharge Gas Temperature`, `Refrigerant Temperature 2`, `Compressor Temperature`, and `Room Setpoint Mirror` are enabled by default in EXP381B.

## Counts

- Core/primary entities: **36**
- Configuration entities: **22**
- Diagnostic entities: **133**
- Total named HA-exposed entities: **191**

## Core / primary entities

| Expected HA entity ID | ESPHome name | ESPHome id | Metadata |
|---|---|---|---|
| `sensor.room_temperature` | Room Temperature | `thermia_room_temperature` | °C; device_class=temperature |
| `sensor.room_setpoint` | Room Setpoint | `thermia_room_setpoint` | °C; device_class=temperature |
| `sensor.outdoor_temperature` | Outdoor Temperature | `thermia_outdoor_temperature` | °C; device_class=temperature |
| `sensor.supply_temperature` | Supply Temperature | `thermia_supply_temperature` | °C; device_class=temperature |
| `sensor.dhw_temperature` | DHW Temperature | `thermia_dhw_temperature` | °C; device_class=temperature |
| `sensor.dhw_upper_temperature` | DHW Upper Temperature | `thermia_dhw_upper_temperature` | °C; device_class=temperature |
| `sensor.dhw_delta_t` | DHW Delta T | `thermia_dhw_delta_t` | °C |
| `sensor.target_temperature` | Target Temperature | `thermia_target_temperature` | °C; device_class=temperature |
| `sensor.compressor_frequency` | Compressor Frequency | `thermia_compressor_frequency` | Hz; device_class=frequency |
| `sensor.compressor_current` | Compressor Current | `thermia_compressor_current` | A; device_class=current |
| `sensor.high_pressure` | High Pressure | `thermia_high_pressure` | bar; device_class=pressure |
| `sensor.outdoor_fan_speed` | Outdoor Fan Speed | `thermia_fan_speed` | rpm |
| `sensor.condenser_inlet` | Condenser Inlet | `thermia_condenser_in` | °C; device_class=temperature |
| `sensor.condenser_outlet` | Condenser Outlet | `thermia_condenser_out` | °C; device_class=temperature |
| `sensor.condenser_delta_t` | Condenser Delta T | `thermia_condenser_delta_t` | °C |
| `sensor.heating_curve` | Heating Curve | `thermia_heating_curve` | primary |
| `sensor.heating_minimum` | Heating Minimum | `thermia_heating_min` | °C; device_class=temperature |
| `sensor.heating_maximum` | Heating Maximum | `thermia_heating_max` | °C; device_class=temperature |
| `sensor.heating_stop` | Heating Stop | `thermia_heating_stop` | °C; device_class=temperature |
| `sensor.reduced_temperature` | Reduced Temperature | `thermia_reduced_temperature` | °C; device_class=temperature |
| `sensor.room_factor` | Room Factor | `thermia_room_factor` | primary |
| `sensor.heating_curve_correction_5` | Heating Curve Correction +5 | `thermia_curve_plus5` | °C |
| `sensor.heating_curve_correction_0` | Heating Curve Correction 0 | `thermia_curve_zero` | °C |
| `sensor.heating_curve_correction_5` | Heating Curve Correction -5 | `thermia_curve_minus5` | °C |
| `binary_sensor.compressor_running` | Compressor Running | `thermia_compressor_running` | device_class=running |
| `binary_sensor.outdoor_fan_running` | Outdoor Fan Running | `thermia_outdoor_fan_running` | device_class=running |
| `binary_sensor.outdoor_unit_run_enable_acknowledged` | Outdoor Unit Run Enable Acknowledged | `thermia_outdoor_unit_enabled` | device_class=running |
| `binary_sensor.heating_context` | Heating Context | `thermia_heating_context` | primary |
| `binary_sensor.dhw_context` | DHW Context | `thermia_dhw_context` | primary |
| `binary_sensor.cooling_context` | Cooling Context | `thermia_cooling_context` | primary |
| `binary_sensor.heating_active` | Heating Active | `thermia_heating_active` | device_class=running |
| `binary_sensor.dhw_active` | DHW Active | `thermia_dhw_active` | device_class=running |
| `binary_sensor.cooling_active` | Cooling Active | `thermia_cooling_active` | device_class=running |
| `sensor.sg_mode` | SG Mode | `thermia_sg_mode` | primary |
| `sensor.outdoor_unit_state` | Outdoor Unit State | `thermia_outdoor_unit_state` | primary |
| `sensor.operating_mode` | Operating Mode | `thermia_operating_mode` | primary |

## Configuration entities

These are ordered by their prepared production-facing display names.

| Expected HA entity ID | ESPHome name | ESPHome id | Metadata |
|---|---|---|---|
| `select.01_operation_01_mode` | 01 Operation | 01 Mode | `exp380_operation_mode_control` | config; options=Uit/Auto/Compressor/Bijverwarmer/Warmwater |
| `number.02_heating_00_room_setpoint` | 02 Heating | 00 Room Setpoint | `thermia_write_room_setpoint_target_control` | config; 10..30; step=1 |
| `number.02_heating_01_heating_curve` | 02 Heating | 01 Heating Curve | `thermia_write_heating_curve_target_control` | config; 22..56; step=1 |
| `number.02_heating_02_minimum` | 02 Heating | 02 Minimum | `thermia_write_heating_min_target_control` | config; 20..40; step=1 |
| `number.02_heating_03_maximum` | 02 Heating | 03 Maximum | `thermia_write_heating_max_target_control` | config; 40..85; step=1 |
| `number.02_heating_04_curve_correction_5` | 02 Heating | 04 Curve Correction +5 | `thermia_write_curve_plus5_target_control` | config; -5..5; step=1 |
| `number.02_heating_05_curve_correction_0` | 02 Heating | 05 Curve Correction 0 | `thermia_write_curve_zero_target_control` | config; -5..5; step=1 |
| `number.02_heating_06_curve_correction_5` | 02 Heating | 06 Curve Correction -5 | `thermia_write_curve_minus5_target_control` | config; -5..5; step=1 |
| `number.02_heating_07_heating_stop` | 02 Heating | 07 Heating Stop | `thermia_write_heating_stop_target_control` | config; 0..22; step=1 |
| `number.02_heating_08_reduced_temperature` | 02 Heating | 08 Reduced Temperature | `thermia_write_reduced_temperature_target_control` | config; 10..30; step=1 |
| `number.02_heating_09_room_factor` | 02 Heating | 09 Room Factor | `thermia_write_room_factor_target_control` | config; 0..4; step=1 |
| `number.02_heating_20_startup_ht` | 02 Heating | 20 Startup HT | `exp378_opstart_ht_control` | config; min; 1..30; step=1 |
| `number.02_heating_21_heating_time` | 02 Heating | 21 Heating Time | `exp378_verwarmingstijd_control` | config; min; 5..40; step=1 |
| `switch.03_hot_water_01_enabled` | 03 Hot Water | 01 Enabled | `exp378_sww_enabled_control` | config |
| `select.03_hot_water_02_mode` | 03 Hot Water | 02 Mode | `exp378_sww_mode_control` | config; options=Comfort/Eco/Vakantie Eco |
| `switch.04_cooling_01_enabled` | 04 Cooling | 01 Enabled | `exp379_cooling_enabled_control` | config |
| `number.04_cooling_02_desired_temperature` | 04 Cooling | 02 Desired Temperature | `exp379_cooling_temp_control` | config; °C; 7..40; step=1 |
| `number.04_cooling_03_active_above` | 04 Cooling | 03 Active Above | `exp379_cooling_active_control` | config; °C; 10..50; step=1 |
| `number.04_cooling_04_cooling_time` | 04 Cooling | 04 Cooling Time | `exp379_cooling_time_control` | config; min; 5..40; step=1 |
| `switch.04_cooling_05_room_sensor` | 04 Cooling | 05 Room Sensor | `exp379_room_sensor_control` | config |
| `number.04_cooling_06_room_hysteresis_low` | 04 Cooling | 06 Room Hysteresis Low | `exp379_hyst_low_control` | config; °C; 0.5..5.0; step=0.1 |
| `number.04_cooling_07_room_hysteresis_high` | 04 Cooling | 07 Room Hysteresis High | `exp379_hyst_high_control` | config; °C; 0.5..5.0; step=0.1 |

## Core diagnostics / non-write entities

| Expected HA entity ID | ESPHome name | ESPHome id | Metadata |
|---|---|---|---|
| `sensor.thermia_esp_uptime` | Thermia ESP Uptime | `—` | diagnostic |
| `sensor.thermia_wifi_signal` | Thermia WiFi Signal | `—` | diagnostic |
| `sensor.bus_last_valid_frame_age` | Bus Last Valid Frame Age | `—` | diagnostic; s |
| `sensor.valid_frames_since_boot` | Valid Frames Since Boot | `—` | diagnostic; disabled_by_default |
| `sensor.parser_resyncs_since_boot` | Parser Resyncs Since Boot | `—` | diagnostic; disabled_by_default |
| `sensor.rx_buffer_drops_since_boot` | RX Buffer Drops Since Boot | `—` | diagnostic; disabled_by_default |
| `sensor.compressor_starts_since_boot` | Compressor Starts Since Boot | `—` | diagnostic; disabled_by_default |
| `sensor.observed_compressor_run_duration` | Observed Compressor Run Duration | `—` | diagnostic; s; disabled_by_default |
| `sensor.controller_0x02_frame_age` | Controller 0x02 Frame Age | `—` | diagnostic; s; disabled_by_default |
| `sensor.online_slot_0x06_poll_age` | Online Slot 0x06 Poll Age | `—` | diagnostic; s; disabled_by_default |
| `sensor.room_sensor_0x0a_frame_age` | Room Sensor 0x0A Frame Age | `—` | diagnostic; s; disabled_by_default |
| `sensor.outdoor_unit_0x1e_frame_age` | Outdoor Unit 0x1E Frame Age | `—` | diagnostic; s; disabled_by_default |
| `sensor.thermia_esp_heap_free` | Thermia ESP Heap Free | `—` | diagnostic; disabled_by_default |
| `sensor.thermia_esp_heap_min_free` | Thermia ESP Heap Min Free | `—` | diagnostic; disabled_by_default |
| `sensor.thermia_esp_heap_fragmentation` | Thermia ESP Heap Fragmentation | `—` | diagnostic; disabled_by_default |
| `sensor.thermia_esp_loop_time` | Thermia ESP Loop Time | `—` | diagnostic; disabled_by_default |
| `sensor.controller_sequence_value_raw` | Controller Sequence Value Raw | `thermia_demand_raw` | diagnostic; disabled_by_default |
| `sensor.controller_context_raw_a80c` | Controller Context Raw A80C | `thermia_controller_state_a80c` | diagnostic; disabled_by_default |
| `sensor.controller_accessory_status_raw_a80e` | Controller Accessory Status Raw A80E | `thermia_controller_state_a80e` | diagnostic; disabled_by_default |
| `sensor.outdoor_unit_operating_state_raw` | Outdoor Unit Operating State Raw | `thermia_outdoor_unit_operating_state_raw` | diagnostic; disabled_by_default |
| `sensor.outdoor_unit_status_flags` | Outdoor Unit Status Flags | `thermia_outdoor_unit_status_flags` | diagnostic; disabled_by_default |
| `sensor.mode_request_raw` | Mode Request Raw | `thermia_mode_request_raw` | diagnostic; disabled_by_default |
| `sensor.commanded_target_temperature` | Commanded Target Temperature | `thermia_commanded_target_temperature` | diagnostic; °C; device_class=temperature |
| `sensor.room_bus_propagated_outdoor_temperature` | Room Bus Propagated Outdoor Temperature | `thermia_room_bus_outdoor_temperature` | diagnostic; °C; device_class=temperature |
| `sensor.dcm_propagated_outdoor_temperature` | DCM Propagated Outdoor Temperature | `thermia_dcm_outdoor_temperature` | diagnostic; °C; device_class=temperature |
| `sensor.onlinedcm_context_raw_afdc` | Online⁄DCM Context Raw AFDC | `thermia_dcm_status_afdc` | diagnostic; disabled_by_default |
| `sensor.expansion_valve_steps` | Expansion Valve Steps | `thermia_expansion_valve_steps` | diagnostic; steps |
| `sensor.refrigerant_temperature_1` | Refrigerant Temperature 1 | `thermia_refrigerant_temperature_1` | diagnostic; °C; device_class=temperature |
| `sensor.discharge_gas_temperature` | Discharge Gas Temperature | `thermia_discharge_gas_temperature` | diagnostic; °C; device_class=temperature |
| `sensor.refrigerant_temperature_2` | Refrigerant Temperature 2 | `thermia_refrigerant_temperature_2` | diagnostic; °C; device_class=temperature |
| `sensor.average_outdoor_temperature` | Average Outdoor Temperature | `thermia_average_outdoor_temperature` | diagnostic; °C; device_class=temperature |
| `sensor.compressor_temperature` | Compressor Temperature | `thermia_compressor_temperature` | diagnostic; °C; device_class=temperature |
| `sensor.room_setpoint_mirror` | Room Setpoint Mirror | `thermia_room_setpoint_mirror` | diagnostic; °C; device_class=temperature |
| `binary_sensor.bus_healthy` | Bus Healthy | `thermia_bus_healthy` | diagnostic; device_class=connectivity |
| `binary_sensor.compressor_starting` | Compressor Starting | `thermia_compressor_starting` | diagnostic; device_class=running |
| `binary_sensor.room_sensor_control_flag_b3c6` | Room Sensor Control Flag B3C6 | `thermia_room_boost_request` | diagnostic |
| `binary_sensor.outdoor_unit_cycle_request_0007` | Outdoor Unit Cycle Request 0007 | `thermia_outdoor_unit_command_0007` | diagnostic; disabled_by_default |
| `binary_sensor.outdoor_unit_run_enable_0008` | Outdoor Unit Run Enable 0008 | `thermia_outdoor_unit_command_0008` | diagnostic; disabled_by_default |
| `binary_sensor.controller_a80c_flag_0x10` | Controller A80C Flag 0x10 | `thermia_a80c_flag_0x10` | diagnostic; disabled_by_default |
| `binary_sensor.controller_a80c_flag_0x20` | Controller A80C Flag 0x20 | `thermia_a80c_flag_0x20` | diagnostic; disabled_by_default |
| `binary_sensor.controller_a80e_flag_0x08` | Controller A80E Flag 0x08 | `thermia_a80e_flag_0x08` | diagnostic; disabled_by_default |
| `binary_sensor.controller_a80e_periodic_flag_0x20` | Controller A80E Periodic Flag 0x20 | `thermia_a80e_flag_0x20` | diagnostic; disabled_by_default |
| `sensor.thermia_esp_reset_reason` | Thermia ESP Reset Reason | `—` | diagnostic |
| `sensor.thermia_esp_device_info` | Thermia ESP Device Info | `—` | diagnostic; disabled_by_default |
| `sensor.thermia_ip_address` | Thermia IP Address | `—` | diagnostic |
| `sensor.thermia_wifi_bssid` | Thermia WiFi BSSID | `—` | diagnostic |
| `sensor.thermia_wifi_power_save_mode` | Thermia WiFi Power Save Mode | `—` | diagnostic; disabled_by_default |
| `sensor.thermia_firmware_build` | Thermia Firmware Build | `—` | diagnostic |
| `sensor.heating_settings_source` | Heating Settings Source | `—` | diagnostic |
| `sensor.controller_context` | Controller Context | `thermia_controller_context` | diagnostic |
| `sensor.mode_request` | Mode Request | `thermia_mode_request` | diagnostic |

## Write / experiment diagnostics

These remain diagnostic entities. Historical internal experiment labels are retained where changing them would create unnecessary code-path risk.

| Expected HA entity ID | ESPHome name | ESPHome id | Metadata |
|---|---|---|---|
| `sensor.thermia_write_dirty_queue_mask` | Thermia Write Dirty Queue Mask | `thermia_write_dirty_mask_sensor` | diagnostic |
| `sensor.thermia_write_pending_write_count` | Thermia Write Pending Write Count | `thermia_write_pending_write_count_sensor` | diagnostic |
| `sensor.thermia_write_071c_0730_challenge_count` | Thermia Write 071C-0730 Challenge Count | `thermia_write_challenges` | diagnostic |
| `sensor.thermia_write_post_r1_challenge_count` | Thermia Write Post-R1 Challenge Count | `thermia_write_post_tx_challenges` | diagnostic |
| `sensor.thermia_write_fc16_pages_seen` | Thermia Write FC16 Pages Seen | `thermia_write_fc16_seen_sensor` | diagnostic |
| `sensor.thermia_write_03e8_count14_seen` | Thermia Write 03E8 Count14 Seen | `thermia_write_03e8_seen_sensor` | diagnostic |
| `sensor.thermia_write_03fc_count11_seen` | Thermia Write 03FC Count11 Seen | `thermia_write_03fc_seen_sensor` | diagnostic |
| `sensor.thermia_write_0410_count22_seen` | Thermia Write 0410 Count22 Seen | `thermia_write_0410_seen_sensor` | diagnostic |
| `sensor.thermia_write_042e_count15_seen` | Thermia Write 042E Count15 Seen | `thermia_write_042e_seen_sensor` | diagnostic |
| `sensor.thermia_write_runtime_085f_acks` | Thermia Write Runtime 085F ACKs | `thermia_write_runtime_085f_acked_sensor` | diagnostic |
| `sensor.thermia_write_runtime_04a6_acks` | Thermia Write Runtime 04A6 ACKs | `thermia_write_runtime_04a6_acked_sensor` | diagnostic |
| `sensor.thermia_write_runtime_fc16_acks` | Thermia Write Runtime FC16 ACKs | `thermia_write_runtime_fc16_ack_sensor` | diagnostic |
| `sensor.thermia_write_runtime_0708_idle_replies` | Thermia Write Runtime 0708 Idle Replies | `thermia_write_runtime_0708_reply_sensor` | diagnostic |
| `sensor.thermia_write_runtime_unknown_fc16` | Thermia Write Runtime Unknown FC16 | `thermia_write_runtime_unknown_fc16_sensor` | diagnostic |
| `sensor.thermia_write_runtime_unknown_fc03` | Thermia Write Runtime Unknown FC03 | `thermia_write_runtime_unknown_fc03_sensor` | diagnostic |
| `sensor.thermia_write_runtime_ack_self_echoes` | Thermia Write Runtime ACK Self Echoes | `thermia_write_runtime_self_echo_sensor` | diagnostic |
| `sensor.thermia_write_runtime_age` | Thermia Write Runtime Age | `—` | diagnostic; s |
| `sensor.thermia_write_same_0410_after_ack` | Thermia Write Same 0410 After ACK | `thermia_write_same_0410_after_ack_sensor` | diagnostic |
| `sensor.thermia_write_same_03fc_after_ack` | Thermia Write Same 03FC After ACK | `thermia_write_same_03fc_after_ack_sensor` | diagnostic |
| `sensor.thermia_write_same_03e8_after_ack` | Thermia Write Same 03E8 After ACK | `thermia_write_same_03e8_after_ack_sensor` | diagnostic |
| `sensor.thermia_write_external_fc17_responses` | Thermia Write External FC17 Responses | `thermia_write_peer_fc17` | diagnostic |
| `sensor.thermia_write_external_fc16_acks` | Thermia Write External FC16 ACKs | `thermia_write_peer_fc16_ack` | diagnostic |
| `sensor.thermia_write_elapsed_age` | Thermia Write Elapsed Age | `—` | diagnostic; s |
| `sensor.thermia_write_boot_age` | Thermia Write Boot Age | `—` | diagnostic; s |
| `sensor.thermia_write_post_r1_age` | Thermia Write Post-R1 Age | `—` | diagnostic; s |
| `sensor.thermia_write_semantic_page_responses` | Thermia Write Semantic Page Responses | `thermia_write_semantic_response_count_sensor` | diagnostic |
| `sensor.thermia_write_confirmed_selected_writes` | Thermia Write Confirmed Selected Writes | `thermia_write_confirmed_write_count_sensor` | diagnostic |
| `sensor.thermia_write_03e8_refresh_requests` | Thermia Write 03E8 Refresh Requests | `thermia_write_refresh_request_count_sensor` | diagnostic |
| `sensor.thermia_write_03e8_refresh_confirmed` | Thermia Write 03E8 Refresh Confirmed | `thermia_write_refresh_confirmed_count_sensor` | diagnostic |
| `sensor.thermia_write_cached_heating_curve` | Thermia Write Cached Heating Curve | `—` | diagnostic |
| `sensor.thermia_write_original_selected_value` | Thermia Write Original Selected Value | `—` | diagnostic |
| `sensor.thermia_write_target_selected_value` | Thermia Write Target Selected Value | `—` | diagnostic |
| `sensor.thermia_write_queue_pending` | Thermia Write Queue Pending | `—` | diagnostic |
| `sensor.thermia_write_queued_register` | Thermia Write Queued Register | `—` | diagnostic |
| `sensor.thermia_write_queued_word` | Thermia Write Queued Word | `—` | diagnostic |
| `sensor.thermia_write_queued_raw_value` | Thermia Write Queued Raw Value | `—` | diagnostic |
| `binary_sensor.thermia_write_dirty_queue_pending` | Thermia Write Dirty Queue Pending | `thermia_write_dirty_pending_sensor` | diagnostic |
| `binary_sensor.thermia_write_configuration_synced` | Thermia Write Configuration Synced | `thermia_write_config_synced_sensor` | diagnostic |
| `binary_sensor.thermia_write_active` | Thermia Write Active | `thermia_write_active` | diagnostic |
| `binary_sensor.thermia_write_r1_one_shot_tx_used` | Thermia Write R1 One-Shot TX Used | `thermia_write_tx_used_sensor` | diagnostic |
| `binary_sensor.thermia_write_03e8_ack_tx_used` | Thermia Write 03E8 ACK TX Used | `thermia_write_ack_used_sensor` | diagnostic |
| `binary_sensor.thermia_write_03fc_ack_tx_used` | Thermia Write 03FC ACK TX Used | `thermia_write_03fc_ack_used_sensor` | diagnostic |
| `binary_sensor.thermia_write_0410_ack_tx_used` | Thermia Write 0410 ACK TX Used | `thermia_write_0410_ack_used_sensor` | diagnostic |
| `binary_sensor.thermia_write_042e_ack_tx_used` | Thermia Write 042E ACK TX Used | `thermia_write_042e_ack_used_sensor` | diagnostic |
| `binary_sensor.thermia_write_0442_ack_tx_used` | Thermia Write 0442 ACK TX Used | `thermia_write_0442_ack_used_sensor` | diagnostic |
| `binary_sensor.thermia_write_0456_ack_tx_used` | Thermia Write 0456 ACK TX Used | `thermia_write_0456_ack_used_sensor` | diagnostic |
| `binary_sensor.thermia_write_046a_ack_tx_used` | Thermia Write 046A ACK TX Used | `thermia_write_046a_ack_used_sensor` | diagnostic |
| `binary_sensor.thermia_write_047e_ack_tx_used` | Thermia Write 047E ACK TX Used | `thermia_write_047e_ack_used_sensor` | diagnostic |
| `binary_sensor.thermia_write_0492_ack_tx_used` | Thermia Write 0492 ACK TX Used | `thermia_write_0492_ack_used_sensor` | diagnostic |
| `binary_sensor.thermia_write_04a6_ack_tx_used` | Thermia Write 04A6 ACK TX Used | `thermia_write_04a6_ack_used_sensor` | diagnostic |
| `binary_sensor.thermia_write_04ba_ack_tx_used` | Thermia Write 04BA ACK TX Used | `thermia_write_04ba_ack_used_sensor` | diagnostic |
| `binary_sensor.thermia_write_04d8_ack_tx_used` | Thermia Write 04D8 ACK TX Used | `thermia_write_04d8_ack_used_sensor` | diagnostic |
| `binary_sensor.thermia_write_04f6_ack_tx_used` | Thermia Write 04F6 ACK TX Used | `thermia_write_04f6_ack_used_sensor` | diagnostic |
| `binary_sensor.thermia_write_050a_ack_tx_used` | Thermia Write 050A ACK TX Used | `thermia_write_050a_ack_used_sensor` | diagnostic |
| `binary_sensor.thermia_write_051e_ack_tx_used` | Thermia Write 051E ACK TX Used | `thermia_write_051e_ack_used_sensor` | diagnostic |
| `binary_sensor.thermia_write_0532_ack_tx_used` | Thermia Write 0532 ACK TX Used | `thermia_write_0532_ack_used_sensor` | diagnostic |
| `binary_sensor.thermia_write_0546_ack_tx_used` | Thermia Write 0546 ACK TX Used | `thermia_write_0546_ack_used_sensor` | diagnostic |
| `binary_sensor.thermia_write_055a_ack_tx_used` | Thermia Write 055A ACK TX Used | `thermia_write_055a_ack_used_sensor` | diagnostic |
| `binary_sensor.thermia_write_057b_ack_tx_used` | Thermia Write 057B ACK TX Used | `thermia_write_057b_ack_used_sensor` | diagnostic |
| `binary_sensor.thermia_write_059c_ack_tx_used` | Thermia Write 059C ACK TX Used | `thermia_write_059c_ack_used_sensor` | diagnostic |
| `binary_sensor.thermia_write_05bd_ack_tx_used` | Thermia Write 05BD ACK TX Used | `thermia_write_05bd_ack_used_sensor` | diagnostic |
| `binary_sensor.thermia_write_05de_ack_tx_used` | Thermia Write 05DE ACK TX Used | `thermia_write_05de_ack_used_sensor` | diagnostic |
| `binary_sensor.thermia_write_05ff_ack_tx_used` | Thermia Write 05FF ACK TX Used | `thermia_write_05ff_ack_used_sensor` | diagnostic |
| `binary_sensor.thermia_write_0620_ack_tx_used` | Thermia Write 0620 ACK TX Used | `thermia_write_0620_ack_used_sensor` | diagnostic |
| `binary_sensor.thermia_write_0641_ack_tx_used` | Thermia Write 0641 ACK TX Used | `thermia_write_0641_ack_used_sensor` | diagnostic |
| `binary_sensor.thermia_write_0662_ack_tx_used` | Thermia Write 0662 ACK TX Used | `thermia_write_0662_ack_used_sensor` | diagnostic |
| `binary_sensor.thermia_write_0683_ack_tx_used` | Thermia Write 0683 ACK TX Used | `thermia_write_0683_ack_used_sensor` | diagnostic |
| `binary_sensor.thermia_write_06a4_ack_tx_used` | Thermia Write 06A4 ACK TX Used | `thermia_write_06a4_ack_used_sensor` | diagnostic |
| `binary_sensor.thermia_write_06c5_ack_tx_used` | Thermia Write 06C5 ACK TX Used | `thermia_write_06c5_ack_used_sensor` | diagnostic |
| `binary_sensor.thermia_write_06ea_ack_tx_used` | Thermia Write 06EA ACK TX Used | `thermia_write_06ea_ack_used_sensor` | diagnostic |
| `binary_sensor.thermia_write_06f1_ack_tx_used` | Thermia Write 06F1 ACK TX Used | `thermia_write_06f1_ack_used_sensor` | diagnostic |
| `binary_sensor.thermia_write_06f4_ack_tx_used` | Thermia Write 06F4 ACK TX Used | `thermia_write_06f4_ack_used_sensor` | diagnostic |
| `binary_sensor.thermia_write_persistent_runtime_active` | Thermia Write Persistent Runtime Active | `thermia_write_runtime_active_sensor` | diagnostic |
| `binary_sensor.thermia_write_soak_15m_passed` | Thermia Write Soak 15m Passed | `thermia_write_soak_15m_passed_sensor` | diagnostic |
| `binary_sensor.thermia_write_last_selected_write_confirmed` | Thermia Write Last Selected Write Confirmed | `thermia_write_write_confirmed_sensor` | diagnostic |
| `sensor.thermia_write_status` | Thermia Write Status | `thermia_write_status` | diagnostic |
| `sensor.thermia_write_stage` | Thermia Write Stage | `thermia_write_stage_text` | diagnostic |
| `sensor.thermia_write_last_event` | Thermia Write Last Event | `thermia_write_last_event` | diagnostic |
| `sensor.exp378_status` | EXP378 Status | `exp378_status` | diagnostic |
| `sensor.exp378_current_sww_mode` | EXP378 Current SWW Mode | `exp378_current_mode` | diagnostic |
| `sensor.exp379_cooling_status` | EXP379 Cooling Status | `exp379_status` | diagnostic |
| `sensor.exp380_mode_status` | EXP380 Mode Status | `exp380_status` | diagnostic |

## Dashboard-builder guidance

For normal operational dashboards, prefer **Core / primary entities**. Add selected diagnostics only when useful.

For user controls, use the **Configuration entities** section. EXP381B groups them in the same functional order as the Thermia UI/manual:

1. Operation
2. Heating
3. Hot Water
4. Cooling

The ordinary read sensors remain controller-authoritative. Configuration controls can temporarily show queued desired intent while a native semantic write is in progress.

`Return Temperature` is still intentionally absent: this project does not yet have a sufficiently reliable locally confirmed Thermia mapping for it.

When a later experiment changes entity names, availability, or adds/removes entities, regenerate this catalogue from the latest YAML. This catalogue is an entity reference, not protocol evidence.