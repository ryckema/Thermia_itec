# V5DCM12 — request-package mapping and offline capture replay (2026-10-17)

**Status:** COMPLETE / POSITIVE for bounded offline mapping and replay tests (14/14); COMPLETE / INCONCLUSIVE for native XTR packet readiness and accepted/Online session. ESPHome unchanged; no TX.

**Hypothesis:** map the original Connect 2.1.105 package request masks to documented address ranges, then join historical FC16 request-shaped starts without mistaking these for firmware confirmed receipts. **Baseline:** V5DCM11 verified application readiness states, V5DCM4–8 historical captures and live V5DCM2 FIX1 RX-only. **Controlled change:** offline source checks and 43 address-range joins over 3,063 previously decoded native event rows from seven capture files.

**Original firmware source:** 2.1.105 device_client/cm/cm_client_type.py defines request words 1802 (0x070A), 1803 (0x070B), 1804 (0x070C). cm/modbus_server15.py constructs requested pairs from the significant registers in active parser subscriptions, translates each using runtime flags JSON via _register_and_bit_for_address(request=True), and only clears request bits / advances application readiness via the register-received callback. The active parser subset and profile-selected JSON remain UNKNOWN.

**Existing repository-derived map:** Thermia_Connect_Firmware/data/cm930_modbus_flags_map.csv supplies 16 configuration-upper + 16 configuration-lower + 11 operations address-to-bit spans. Its original profile-specific flags.json contents were NOT independently re-extracted in this experiment, so this is a mapping candidate with explicit provenance, not fresh original-JSON proof.

**Observed historical matching footprints:**

| Capture | FC16-shaped requests | Distinct matching bit ranges | 070A/070B/070C |
|---|---:|---:|---|
| Sep 24 21:00 | 21 | 10 | 0 / 0 / 10 |
| Sep 25 07:15 | 40 | 11 | 0 / 1 / 10 |
| Sep 25 09:02 | 41 | 40 | 16 / 13 / 11 |
| Sep 25 09:05 | 73 | 35 | 15 / 16 / 4 |
| Oct 03 16:53 | 162 | 43 | 16 / 16 / 11 |
| iTec Eco5 Sep 26 | 1058 | 43 | 16 / 16 / 11 |
| iTec Eco5 Sep 28 | 1105 | 42 | 16 / 16 / 10 |

All 14 offline source/map/matching assertions PASS. The 3,063 records are classified *native event rows*, not the 25,031 total previously CRC-validated raw frames. Mapping request shape to a range is not proof of same-session application receipt, controller owner, epoch or display state.

**Positive criteria met:** traceable three register groups, 43 non-overlapping candidate ranges, reproducible seven-file footprints, unknown gaps fail closed. **Negative criteria not observed:** mismatching counters or ungrounded approval; genuine application readiness not tested. **Abort:** physical TX, private keys/answer/tooling disclosure, inferred Online or live write. **Recovery:** offline experiment; tested V5DCM2 FIX1 retained.

**Evidence:** PROVEN from firmware source: three request words and parser-readiness callbacks. STRONGLY SUPPORTED repository derived: 43 flags ranges. OBSERVED historically: FC16 address-shape matches. UNKNOWN: active XTR parser subset, exact flags variant, actual application receipt, FC23 accepted, DCM icon or Online.

**Next V5DCM13 — PREPARED / NOT RUN:** offline validate profile-specific original flags JSON from authentic RAUC appfs against repository-derived map and selection path. Positive: verified exact match; negative: missing/mismatch; abort secrets/TX; recovery none.

Sanitized local artifact: V5DCM12_PACKAGE_MAP_OFFLINE_20261017.zip.
