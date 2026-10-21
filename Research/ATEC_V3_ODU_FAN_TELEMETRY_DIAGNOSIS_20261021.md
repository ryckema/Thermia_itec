# ATEC V3 — fan/ODU live telemetry mismatch: source-derived passive diagnosis (2026-10-21)

**Classification:** OFFLINE SOURCE + ARCHIVED BUS CAPTURE ONLY; not independently observed physical ATEC fan operation, not current local XTR experiment, and not a fix deployed to ATEC. The external ATEC author reports that reported status can disagree with real-world fan activity; that complaint is context, not a synchronized observation/log.

## OBSERVED FACTS / PROVEN SOURCE

1. Original Thermia Connect 2.1.105 appfs `etc/device-client.d/930/2.3.0-2.4.3/sensors.json` maps `odu_fan_1_speed` to `{2091}` and `odu_fan_2_speed` to `{2092}`, both described as measured **RPM** (fan2 only on dual-fan units). `odu_fan_status` maps to bit `{2094.2}`; `odu_operation_status` is raw `{2095}`. This establishes vendor-source semantics conditional on the 2.3.0–2.4.3 profile, NOT guaranteed installed ATEC profile or physical correlation.
2. ATEC V3 user-supplied `thermia-sniffer.yaml` exposes 2091/2092 as `ODU Fan 1/2 Speed` and 2094.bit2 as `ODU Fan Status`. The YAML itself warns: ODU 2091–2096 values not yet checked against physical events and treats them as provisional; `HANDOFF.md` §6 explicitly lists fan/valve/defrost cross-check outstanding. YAML does not set RPM units on those fan sensor entries.
3. ATEC V3 `Decoder::handle` obtains those gateway values from the HP's native 0x0F FC16 pushes; `on_register_` updates a store and HA sensors. `RegisterStore::has` tracks *ever observed since boot*, not per-register freshness. The generic `Seconds Since HP Update` refers to *any* 0x0F FC16 write, not update age of 2091/2092/2094. The separate `Live IO Fresh` <=5s mechanism applies to the author's direct FC23 pump/flow/valve I/O, not the ODU fan sensor definitions. Therefore a registered-but-old ODU value may remain displayed as current (SOURCE-PROVEN freshness limitation).
4. Previously archived Oct03 capture `thermia_capture_20261003_165355.log`, whose 2026-10-21 source-provenance correction identifies it as **ATEC/DCM03**, not locally confirmed XTR, contains **13 CRC-valid** native 0x0F FC16 `0x0820`/18-word frames at capture-relative t=78.284..334.689s (256.405s span). For every one, raw **2091=0; 2092=70; 2094=300 (0x012C: fan bit2 SET); 2095=130**. All 13 are identical: there is no on/off transition or ground-truth physical fan event in this capture. This suggests that watching `Fan 1 Speed=0` alone would give a misleading impression when `Fan 2 Speed=70` and fan-status bit is 1. It cannot establish the unit has two physical fans, that fan2 is truly spinning at 70 rpm, or that these are the current ATEC author's live readings.
5. V3 `modbus_sniff.h` Framer has independently reproduced OFFLINE valid-first-frame loss under synthetic coalescing; that could contribute to lost updates but **is not demonstrated as the cause** of this fan symptom. Original ATEC direct 0x04 FC23 traffic is captured by a separate generic live decoder, but the `ODU Fan Speed` HA entities are fed by the 0x0F gateway-copy registers, not by an independently established direct 0x04 fan-speed source.

## STRONG CONCLUSIONS

- The **first diagnostic is provenance and freshness**, not handshake modification or forced writes. The vendor mapping exists; verify 0x0F 0x0820 update timing and physical fan event before changing decoding.
- A generic gateway health/HP-update timer is insufficient to prove that specific fan registers are fresh. Do not interpret cached `2091=0` as verified physically stopped.
- Offline coalescing parser fix remains valuable independently, but cannot be claimed as demonstrated fix for fan.

## HYPOTHESES

A. Per-register ODU group updates are missing/stale (some FC16 group never reaches decoder or is lost), while other gateway writes keep `Seconds Since HP Update` low.
B. ATEC's fan configuration/model/profile differs from the generic vendor `odu_fan_1/2_speed` semantics; raw data may not represent the visually identified fan.
C. An observer compares `ODU Fan 1 Speed` with a physical fan that is represented by the other speed/status field (archived 0/70/bit2=1 illustrate, NOT proof).
D. Coalesced-frame loss affects some updates (SOURCE-PROVEN mode only, real frequency UNKNOWN).

## SAFE PASSIVE TEST / REQUEST TO ATEC AUTHOR

Use naturally occurring, physically observed fan OFF→ON→OFF transitions (do **not** force compressor/test modes or alter gateway TX). At times before/during/after, capture: what exactly is wrong in HA; raw 2091, 2092, 2094, 2095; 2094 bit2; record time of last CRC-valid **0x0F FC16 block 0x0820** that contains these registers; `Seconds Since HP Update`, CRC/framer good/bad deltas and if possible independent direct outdoor-unit evidence. Existing YAML button `Log Changed Registers Since Last Logged` can capture deltas, but its first press only seeds a baseline; a lack of changed registers does not prove they were freshly received. Log ONLY these sanitized metadata/values; no handshake key/challenges/private mailbox contents, no full memory dump and no TX changes.

**Interpretation:** (a) no 0x0820 incoming during physical state change -> stale/missing gateway source; (b) fresh raw change but wrong HA -> decode/bit/unit interpretation; (c) fresh raw never changes despite fan transition -> upstream controller signal/profile issue, inspect direct outdoor traffic without assuming same address as XTR; (d) CRC/frame-loss spikes -> investigate framer before state mapping. Add per-register last-seen timestamps and mark ODU unknown/stale when old instead of silently showing previous values.

**STATUS:** canonical XTR 2026-10-21 S63 standalone fail-closed offline model remains latest at review; S62 G01/G02/G04 accepted operational risk closure remains valid; user V83 RX_ONLY/HARD_DENY and EXP388 RUNNING/PARTIAL unchanged. No ESPHome compile/flash/active XTR or ATEC TX. External evidence does not prove a fix or controller application acceptance.
