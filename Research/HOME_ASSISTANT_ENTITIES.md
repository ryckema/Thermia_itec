# Home Assistant entity catalogue — Thermia iTec XTR M

**Purpose:** canonical dashboard-building reference for this project.

**Source:** generated from `thermia_itec_xtr_m_waveshare_exp350_auto_qualified_reusable_setpoint_soak.yaml` (EXP350 PREPARED / NOT RUN), 2026-09-30.

## How to use this file

- Treat **ESPHome name** and **ESPHome `id`** as source-derived identifiers from the current YAML.
- **Expected HA entity ID** is the default entity-id form inferred from the ESPHome name. Home Assistant may use a different entity ID if the entity was renamed, migrated, or collided with an existing ID. For dashboard work, verify uncertain IDs against the live HA entity registry.
- `text_sensor` entries are exposed in Home Assistant under the `sensor` domain.
- `entity_category: diagnostic` entities are primarily for troubleshooting/experiment dashboards.
- `entity_category: config` entities are controls shown under Configuration.
- Entities marked `disabled_by_default` may not exist in the live HA state machine until enabled.
- Do not infer protocol semantics from an entity name alone. For proven mappings and confidence levels, use `PROTOCOL_FINDINGS.md`.
- Current experimental entities are prefixed `EXP350`; they are not production-stable names and may change in later experiments.
- **Important:** the two names `Heating Curve Correction +5` and `Heating Curve Correction -5` slugify to the same base string. Home Assistant will disambiguate collisions, so verify their live entity IDs before using them in a dashboard.

## Counts

- Core/primary entities: 36
- Non-EXP diagnostic/config entities: 42
- EXP350 entities: 71
- Total named HA-exposed entities in this YAML: 149

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
| `sensor.heating_curve_correction_5` | Heating Curve Correction +5 | `thermia_curve_plus5` | °C; **HA entity ID collision possible — verify live ID** |
| `sensor.heating_curve_correction_0` | Heating Curve Correction 0 | `thermia_curve_zero` | °C |
| `sensor.heating_curve_correction_5` | Heating Curve Correction -5 | `thermia_curve_minus5` | °C; **HA entity ID collision possible — verify live ID** |
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

## Core diagnostics / non-EXP entities

| Expected HA entity ID | ESPHome name | ESPHome id | Metadata |
|---|---|---|---|
| `sensor.thermia_esp_uptime` | Thermia ESP Uptime | — | diagnostic |
| `sensor.thermia_wifi_signal` | Thermia WiFi Signal | — | diagnostic |
| `sensor.bus_last_valid_frame_age` | Bus Last Valid Frame Age | — | diagnostic; s |
| `sensor.valid_frames_since_boot` | Valid Frames Since Boot | — | diagnostic; disabled_by_default |
| `sensor.parser_resyncs_since_boot` | Parser Resyncs Since Boot | — | diagnostic; disabled_by_default |
| `sensor.rx_buffer_drops_since_boot` | RX Buffer Drops Since Boot | — | diagnostic; disabled_by_default |
| `sensor.compressor_starts_since_boot` | Compressor Starts Since Boot | — | diagnostic; disabled_by_default |
| `sensor.observed_compressor_run_duration` | Observed Compressor Run Duration | — | diagnostic; s; disabled_by_default |
| `sensor.controller_0x02_frame_age` | Controller 0x02 Frame Age | — | diagnostic; s; disabled_by_default |
| `sensor.online_slot_0x06_poll_age` | Online Slot 0x06 Poll Age | — | diagnostic; s; disabled_by_default |
| `sensor.room_sensor_0x0a_frame_age` | Room Sensor 0x0A Frame Age | — | diagnostic; s; disabled_by_default |
| `sensor.outdoor_unit_0x1e_frame_age` | Outdoor Unit 0x1E Frame Age | — | diagnostic; s; disabled_by_default |
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
| `sensor.expansion_valve_steps` | Expansion Valve Steps | `thermia_expansion_valve_steps` | diagnostic; steps; disabled_by_default |
| `sensor.refrigerant_temperature_1` | Refrigerant Temperature 1 | `thermia_refrigerant_temperature_1` | diagnostic; °C; device_class=temperature; disabled_by_default |
| `sensor.discharge_gas_temperature` | Discharge Gas Temperature | `thermia_discharge_gas_temperature` | diagnostic; °C; device_class=temperature; disabled_by_default |
| `sensor.refrigerant_temperature_2` | Refrigerant Temperature 2 | `thermia_refrigerant_temperature_2` | diagnostic; °C; device_class=temperature; disabled_by_default |
| `sensor.average_outdoor_temperature` | Average Outdoor Temperature | `thermia_average_outdoor_temperature` | diagnostic; °C; device_class=temperature |
| `sensor.compressor_temperature` | Compressor Temperature | `thermia_compressor_temperature` | diagnostic; °C; device_class=temperature; disabled_by_default |
| `sensor.room_setpoint_mirror` | Room Setpoint Mirror | `thermia_room_setpoint_mirror` | diagnostic; °C; device_class=temperature; disabled_by_default |
| `binary_sensor.bus_healthy` | Bus Healthy | `thermia_bus_healthy` | diagnostic; device_class=connectivity |
| `binary_sensor.compressor_starting` | Compressor Starting | `thermia_compressor_starting` | diagnostic; device_class=running |
| `binary_sensor.room_sensor_control_flag_b3c6` | Room Sensor Control Flag B3C6 | `thermia_room_boost_request` | diagnostic |
| `binary_sensor.outdoor_unit_cycle_request_0007` | Outdoor Unit Cycle Request 0007 | `thermia_outdoor_unit_command_0007` | diagnostic; disabled_by_default |
| `binary_sensor.outdoor_unit_run_enable_0008` | Outdoor Unit Run Enable 0008 | `thermia_outdoor_unit_command_0008` | diagnostic; disabled_by_default |
| `binary_sensor.controller_a80c_flag_0x10` | Controller A80C Flag 0x10 | `thermia_a80c_flag_0x10` | diagnostic; disabled_by_default |
| `binary_sensor.controller_a80c_flag_0x20` | Controller A80C Flag 0x20 | `thermia_a80c_flag_0x20` | diagnostic; disabled_by_default |
| `binary_sensor.controller_a80e_flag_0x08` | Controller A80E Flag 0x08 | `thermia_a80e_flag_0x08` | diagnostic; disabled_by_default |
| `binary_sensor.controller_a80e_periodic_flag_0x20` | Controller A80E Periodic Flag 0x20 | `thermia_a80e_flag_0x20` | diagnostic; disabled_by_default |
| `sensor.thermia_firmware_build` | Thermia Firmware Build | — | diagnostic |
| `sensor.heating_settings_source` | Heating Settings Source | — | diagnostic |
| `sensor.controller_context` | Controller Context | `thermia_controller_context` | diagnostic |
| `sensor.mode_request` | Mode Request | `thermia_mode_request` | diagnostic |

## EXP350 controls and diagnostics

| Expected HA entity ID | ESPHome name | ESPHome id | Metadata |
|---|---|---|---|
| `sensor.exp350_071c_0730_challenge_count` | EXP350 071C-0730 Challenge Count | `thermia_exp350_challenges` | diagnostic |
| `sensor.exp350_post_r1_challenge_count` | EXP350 Post-R1 Challenge Count | `thermia_exp350_post_tx_challenges` | diagnostic |
| `sensor.exp350_fc16_pages_seen` | EXP350 FC16 Pages Seen | `thermia_exp350_fc16_seen_sensor` | diagnostic |
| `sensor.exp350_03e8_count14_seen` | EXP350 03E8 Count14 Seen | `thermia_exp350_03e8_seen_sensor` | diagnostic |
| `sensor.exp350_03fc_count11_seen` | EXP350 03FC Count11 Seen | `thermia_exp350_03fc_seen_sensor` | diagnostic |
| `sensor.exp350_0410_count22_seen` | EXP350 0410 Count22 Seen | `thermia_exp350_0410_seen_sensor` | diagnostic |
| `sensor.exp350_042e_count15_seen` | EXP350 042E Count15 Seen | `thermia_exp350_042e_seen_sensor` | diagnostic |
| `sensor.exp350_runtime_085f_acks` | EXP350 Runtime 085F ACKs | `thermia_exp350_runtime_085f_acked_sensor` | diagnostic |
| `sensor.exp350_runtime_04a6_acks` | EXP350 Runtime 04A6 ACKs | `thermia_exp350_runtime_04a6_acked_sensor` | diagnostic |
| `sensor.exp350_runtime_fc16_acks` | EXP350 Runtime FC16 ACKs | `thermia_exp350_runtime_fc16_ack_sensor` | diagnostic |
| `sensor.exp350_runtime_0708_idle_replies` | EXP350 Runtime 0708 Idle Replies | `thermia_exp350_runtime_0708_reply_sensor` | diagnostic |
| `sensor.exp350_runtime_unknown_fc16` | EXP350 Runtime Unknown FC16 | `thermia_exp350_runtime_unknown_fc16_sensor` | diagnostic |
| `sensor.exp350_runtime_unknown_fc03` | EXP350 Runtime Unknown FC03 | `thermia_exp350_runtime_unknown_fc03_sensor` | diagnostic |
| `sensor.exp350_runtime_ack_self_echoes` | EXP350 Runtime ACK Self Echoes | `thermia_exp350_runtime_self_echo_sensor` | diagnostic |
| `sensor.exp350_runtime_age` | EXP350 Runtime Age | — | diagnostic; s |
| `sensor.exp350_same_0410_after_ack` | EXP350 Same 0410 After ACK | `thermia_exp350_same_0410_after_ack_sensor` | diagnostic |
| `sensor.exp350_same_03fc_after_ack` | EXP350 Same 03FC After ACK | `thermia_exp350_same_03fc_after_ack_sensor` | diagnostic |
| `sensor.exp350_same_03e8_after_ack` | EXP350 Same 03E8 After ACK | `thermia_exp350_same_03e8_after_ack_sensor` | diagnostic |
| `sensor.exp350_external_fc17_responses` | EXP350 External FC17 Responses | `thermia_exp350_peer_fc17` | diagnostic |
| `sensor.exp350_external_fc16_acks` | EXP350 External FC16 ACKs | `thermia_exp350_peer_fc16_ack` | diagnostic |
| `sensor.exp350_elapsed_age` | EXP350 Elapsed Age | — | diagnostic; s |
| `sensor.exp350_boot_age` | EXP350 Boot Age | — | diagnostic; s |
| `sensor.exp350_post_r1_age` | EXP350 Post-R1 Age | — | diagnostic; s |
| `sensor.exp350_semantic_page_responses` | EXP350 Semantic Page Responses | `thermia_exp350_semantic_response_count_sensor` | diagnostic |
| `sensor.exp350_confirmed_setpoint_writes` | EXP350 Confirmed Setpoint Writes | `thermia_exp350_confirmed_write_count_sensor` | diagnostic |
| `sensor.exp350_cached_03f4` | EXP350 Cached 03F4 | — | diagnostic |
| `sensor.exp350_original_03f4` | EXP350 Original 03F4 | — | diagnostic |
| `sensor.exp350_target_03f4` | EXP350 Target 03F4 | — | diagnostic |
| `binary_sensor.exp350_active` | EXP350 Active | `thermia_exp350_active` | diagnostic |
| `binary_sensor.exp350_r1_one_shot_tx_used` | EXP350 R1 One-Shot TX Used | `thermia_exp350_tx_used_sensor` | diagnostic |
| `binary_sensor.exp350_03e8_ack_tx_used` | EXP350 03E8 ACK TX Used | `thermia_exp350_ack_used_sensor` | diagnostic |
| `binary_sensor.exp350_03fc_ack_tx_used` | EXP350 03FC ACK TX Used | `thermia_exp350_03fc_ack_used_sensor` | diagnostic |
| `binary_sensor.exp350_0410_ack_tx_used` | EXP350 0410 ACK TX Used | `thermia_exp350_0410_ack_used_sensor` | diagnostic |
| `binary_sensor.exp350_042e_ack_tx_used` | EXP350 042E ACK TX Used | `thermia_exp350_042e_ack_used_sensor` | diagnostic |
| `binary_sensor.exp350_0442_ack_tx_used` | EXP350 0442 ACK TX Used | `thermia_exp350_0442_ack_used_sensor` | diagnostic |
| `binary_sensor.exp350_0456_ack_tx_used` | EXP350 0456 ACK TX Used | `thermia_exp350_0456_ack_used_sensor` | diagnostic |
| `binary_sensor.exp350_046a_ack_tx_used` | EXP350 046A ACK TX Used | `thermia_exp350_046a_ack_used_sensor` | diagnostic |
| `binary_sensor.exp350_047e_ack_tx_used` | EXP350 047E ACK TX Used | `thermia_exp350_047e_ack_used_sensor` | diagnostic |
| `binary_sensor.exp350_0492_ack_tx_used` | EXP350 0492 ACK TX Used | `thermia_exp350_0492_ack_used_sensor` | diagnostic |
| `binary_sensor.exp350_04a6_ack_tx_used` | EXP350 04A6 ACK TX Used | `thermia_exp350_04a6_ack_used_sensor` | diagnostic |
| `binary_sensor.exp350_04ba_ack_tx_used` | EXP350 04BA ACK TX Used | `thermia_exp350_04ba_ack_used_sensor` | diagnostic |
| `binary_sensor.exp350_04d8_ack_tx_used` | EXP350 04D8 ACK TX Used | `thermia_exp350_04d8_ack_used_sensor` | diagnostic |
| `binary_sensor.exp350_04f6_ack_tx_used` | EXP350 04F6 ACK TX Used | `thermia_exp350_04f6_ack_used_sensor` | diagnostic |
| `binary_sensor.exp350_050a_ack_tx_used` | EXP350 050A ACK TX Used | `thermia_exp350_050a_ack_used_sensor` | diagnostic |
| `binary_sensor.exp350_051e_ack_tx_used` | EXP350 051E ACK TX Used | `thermia_exp350_051e_ack_used_sensor` | diagnostic |
| `binary_sensor.exp350_0532_ack_tx_used` | EXP350 0532 ACK TX Used | `thermia_exp350_0532_ack_used_sensor` | diagnostic |
| `binary_sensor.exp350_0546_ack_tx_used` | EXP350 0546 ACK TX Used | `thermia_exp350_0546_ack_used_sensor` | diagnostic |
| `binary_sensor.exp350_055a_ack_tx_used` | EXP350 055A ACK TX Used | `thermia_exp350_055a_ack_used_sensor` | diagnostic |
| `binary_sensor.exp350_057b_ack_tx_used` | EXP350 057B ACK TX Used | `thermia_exp350_057b_ack_used_sensor` | diagnostic |
| `binary_sensor.exp350_059c_ack_tx_used` | EXP350 059C ACK TX Used | `thermia_exp350_059c_ack_used_sensor` | diagnostic |
| `binary_sensor.exp350_05bd_ack_tx_used` | EXP350 05BD ACK TX Used | `thermia_exp350_05bd_ack_used_sensor` | diagnostic |
| `binary_sensor.exp350_05de_ack_tx_used` | EXP350 05DE ACK TX Used | `thermia_exp350_05de_ack_used_sensor` | diagnostic |
| `binary_sensor.exp350_05ff_ack_tx_used` | EXP350 05FF ACK TX Used | `thermia_exp350_05ff_ack_used_sensor` | diagnostic |
| `binary_sensor.exp350_0620_ack_tx_used` | EXP350 0620 ACK TX Used | `thermia_exp350_0620_ack_used_sensor` | diagnostic |
| `binary_sensor.exp350_0641_ack_tx_used` | EXP350 0641 ACK TX Used | `thermia_exp350_0641_ack_used_sensor` | diagnostic |
| `binary_sensor.exp350_0662_ack_tx_used` | EXP350 0662 ACK TX Used | `thermia_exp350_0662_ack_used_sensor` | diagnostic |
| `binary_sensor.exp350_0683_ack_tx_used` | EXP350 0683 ACK TX Used | `thermia_exp350_0683_ack_used_sensor` | diagnostic |
| `binary_sensor.exp350_06a4_ack_tx_used` | EXP350 06A4 ACK TX Used | `thermia_exp350_06a4_ack_used_sensor` | diagnostic |
| `binary_sensor.exp350_06c5_ack_tx_used` | EXP350 06C5 ACK TX Used | `thermia_exp350_06c5_ack_used_sensor` | diagnostic |
| `binary_sensor.exp350_06ea_ack_tx_used` | EXP350 06EA ACK TX Used | `thermia_exp350_06ea_ack_used_sensor` | diagnostic |
| `binary_sensor.exp350_06f1_ack_tx_used` | EXP350 06F1 ACK TX Used | `thermia_exp350_06f1_ack_used_sensor` | diagnostic |
| `binary_sensor.exp350_06f4_ack_tx_used` | EXP350 06F4 ACK TX Used | `thermia_exp350_06f4_ack_used_sensor` | diagnostic |
| `binary_sensor.exp350_persistent_runtime_active` | EXP350 Persistent Runtime Active | `thermia_exp350_runtime_active_sensor` | diagnostic |
| `binary_sensor.exp350_soak_15m_passed` | EXP350 Soak 15m Passed | `thermia_exp350_soak_15m_passed_sensor` | diagnostic |
| `binary_sensor.exp350_last_setpoint_write_confirmed` | EXP350 Last Setpoint Write Confirmed | `thermia_exp350_write_confirmed_sensor` | diagnostic |
| `sensor.exp350_status` | EXP350 Status | `thermia_exp350_status` | diagnostic |
| `sensor.exp350_stage` | EXP350 Stage | `thermia_exp350_stage_text` | diagnostic |
| `sensor.exp350_last_event` | EXP350 Last Event | `thermia_exp350_last_event` | diagnostic |
| `number.exp350_desired_room_setpoint` | EXP350 Desired Room Setpoint | `thermia_exp350_desired_room_setpoint` | config; °C |
| `button.exp350_apply_desired_room_setpoint` | EXP350 Apply Desired Room Setpoint | — | config |
| `button.exp350_abort_reusable_setpoint_test` | EXP350 Abort Reusable Setpoint Test | — | config |

## Dashboard-builder guidance

For normal operational dashboards, prefer the **Core / primary entities** section. Add diagnostics only when needed. For the current write experiment, the user-facing controls are `number.exp350_desired_room_setpoint` and `button.exp350_apply_desired_room_setpoint`; `button.exp350_abort_reusable_setpoint_test` is the explicit abort control. Build experimental controls in a Configuration section/card rather than mixing them with normal operating telemetry.

When a later experiment changes entity names or adds/removes entities, regenerate this catalogue from the latest YAML and preserve historical protocol conclusions in the canonical research files rather than treating this list as protocol evidence.
