# v31 Home Assistant entity hierarchy — authoritative manual taxonomy
Date 2026-10-18. Status **PREPARED / NOT RUN**; documentation-only inventory, not verification of any extra native register.
Primary evidence: user photographs of Thermia iTec XT/iTec XTR commissioning manual AWIXT01CG0210, chapters 4–11, especially INFO 7.1–7.12 and SERVICE 8.1–8.12, cross-read with `THERMIA_iTec_XT_XTR_Inbedrijfstelling_AI.md`. Manual labels are semantic anchors **not Modbus address proof**.

## Target HA representation
ESPHome device: Thermia iTec XTR M. Preserve stable entity IDs for all existing v29/v30 sensors and status. Use native `entity_category: diagnostic` for service/technical values rather than making core temperatures diagnostics; labels may be prefixed for grouped dashboard cards. An optional Lovelace dashboard should follow the same hierarchy; ESPHome itself cannot create nested HA menu sections. Do not turn read-only parameters into editable numbers/selects/switches.

## Menu INFORMATIE (manual §7)
1. **Bedrijf** — current operating mode (UIT/AUTO/COMPRESSOR/BIJVERW.WARM/ WARMWATER; HANDMATIG only when service permits). Status/read-only enum. Proven source before publishing.
2. **Verwarming** — STOOKLIJN, MIN, MAX, STOOKLIJN +5/0/-5, WARMTESTOP, BIJ KOELING, CONST.TEMP., VERLAGEN TEMP., KAMERFACTOR, VERMOGENSBEGRENZING (when available). HOOG VERMOGEN excluded for XTR per manual.
3. **Shuntgroep 1** — heating curve, min/max, corrections, cooling behavior, constant/reduced temperature, room factor where supported. **OPTIONAL**; installed bit candidate 0x0534; semantic interpretation = second physical heating circuit.
4. **Shuntgroep 2** — same applicable group options, excluding unsupported parameters. **OPTIONAL**, expansion board required; installed bit candidate 0x0535; semantic interpretation = third physical heating circuit.
5. **Warmwater** — enable, COMFORT/ECO/AFWEZIG mode, TOP-UP current status. No write button.
6. **Koeling** — enabled, desired cooling temperature, active-above temperature, hysteresis and observed status.
7. **Zwembad** — pool activity/demand and temperature if locally mapped. **OPTIONAL** installed bit candidate 0x0533.
8. **Buffertank** — TANKTEMP, OVERLADEN, DOORV.TANK, LAGERE TANKTEMP if supported; **OPTIONAL**, installed bit candidate 0x0536.
9. **Bedrijfsgegevens** — WARMTEVRAAG, KOUDEVRAAG, VRAAG ZWEMBAD, INTEGRAAL WC, outdoor/room/DHW/supply/condenser/return/system temps; shunt/pool/buffer temps conditional; refrigerant1/2, current, discharge temp, high pressure, compressor temp, outdoor ambient.
10. **Bedrijfstijd** — counters compressor, heating, cooling, DHW, auxiliary heater 1/2/3.
11. **Ontdooien** — number of cycles, minutes between last defrosts, time since last defrost.
12. **Kalender, Alarm** — **EXCLUDED** from HA per user requirement. TAAL is configuration/UI metadata, not operational monitoring and may be diagnostic if real source is established.

## Menu SERVICE (manual §8)
1. **Warmwater** — START, STOP, WARMWATERTIJD, DOORV.INTERVAL, TOPVERW.TIJD, TOPVERW.STOP, sensor influence, ECO influence, upper and ordinary DHW sensors.
2. **Verwarming** — START, STOP, OPSTART_HT, VERWARMINGSTIJD.
3. **Koeling** — configuration/mode, START/STOP, KOELTIJD, MAX STARTTEMP, MIN STOPTEMP, room sensor enabled and low/high hysteresis.
4. **Zwembad** — supply target, additional heating option. CONDITIONAL.
5. **Bijverwarming** — MAX STAP, START, MAX STROOM, STARTVERTRAGING, frost protection, external heater settings and offsets, shutoff delay, 3-way diverter, external top-up, shunt timings, system pump cooling; applicability/model gated.
6. **Handmatig** — show passively observed statuses ONLY if supported; **NO** manual-test actuators, enable controls, service overrides or output controls.
7. **Installatie** — model/system and installed feature flags, optional circuits, current limiting, sensor calibration values if passively broadcast, firmware VERSION fields (DISPLAY/HUB/COMM.KIT/HOOFD MICOM/INV.MICOM/EEPROM/EXP CARD), logging interval, power limit. No reset/factory/select/test buttons.
8. **Ontdooien** — compressor stop and WW energy priority settings, if passively available.
9. **Optimum** — START FLOW CV, STATIONAIRE FLOW, MAX/MIN FLOW WARMTE, MIN FLOW WW/KOELING/ZWEMBAD, MAX/MIN OPLADEN WW, etc. Avoid XTR-excluded `FLOWFACTOR VERWARMING`; `ZOEK MIN FLOWS` is a procedure, not an HA control.
10. **Buffertank** — CONFIGURATIE, RET.LD.SHUNT WP, SHUNTTIJD RET, INTEGR.GRENS WC, TANKOFFSET WP/BV/EXT, system circuit/pump, shunt circuits, dependent heating stop, pool circuit. CONDITIONAL.
11. **INFO BUITENGED** — outdoor-unit telemetry e.g. compressor frequency/current, fan speed, high pressure, expansion-valve position and outdoor control sensors. Existing direct 0x1E values remain preferred until native page parity validated.

## Entity eligibility / status matrix (required before future release)
For every menu item track `manual_path`, `model_applicable`, `native_address/page`, `source_evidence` (LOCAL PROVEN / STRONGLY SUPPORTED / FIRMWARE-ONLY / UNKNOWN), `scaling/unit`, `freshness/sentinel`, `HA entity id`, `default_enabled`, `availability_guard`. A menu entry is **not** counted as covered unless a live native source plus valid scaling are established.

## Optional logic
Installed candidates: native `0x0F:0533` pool, `0534` shunt-group1, `0535` shunt-group2, `0536` buffer. Treat them as firmware-derived until locally verified. If flag UNKNOWN or source stale: dependent values unavailable, not falsely absent; if OFF: unavailable and disabled-by-default initially; if ON: expose as available while preserving safe HA registry defaults. HA registry `disabled_by_default` is static; dynamic enabling needs a dedicated HA-side mechanism, not merely an ESPHome template.

## Out of scope
Calendar schedules, alarms/history/fault entities, XTR-inapplicable values, service-test/reset/actuator buttons, controller write functionality. Continue passive bus diagnostics internally as needed without exposing alarm names in HA. Preserve previous production YAML, never assume successful YAML parse equals compile/flash/run.

## Next offline deliverable
A row-by-row gap matrix comparing THIS hierarchy to source v31 alpha01 and conservative firmware `MENU_REVIEW_INFO.csv` / `MENU_REVIEW_SERVICE.csv`, annotated with local XTR evidence, then targeted YAML changes only where mappings are defensible.
