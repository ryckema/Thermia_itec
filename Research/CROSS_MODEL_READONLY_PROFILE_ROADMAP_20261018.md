# Cross-model RX-only Thermia / Danfoss CM930 roadmap — 2026-10-18

**Status:** DESIGN / SOURCE AUDIT ONLY — no new experiment, generated YAML, ESPHome compilation, device flashing, bus TX or model support claim. All future new profile builds start PREPARED / NOT RUN.

## Objective
Use existing Thermia Connect firmware-derived CM930 register metadata plus actual local XTR and cross-model genuine/collaborator captures to build safe, independent ESPHome/Home Assistant **read-only** integrations for other **legacy/non-Genesis** Thermia/Danfoss controller variants, without invalidating XTR proof or silently promoting firmware schema to live bus evidence. Preserve the current XTR folder containing exactly one YAML and one README.

## Canonical sources used

1. `ryckema/Thermia_Connect_Firmware/parameters/ALL_PARAMETERS_ACCESS_MATRIX.csv` — 564 distinct register rows with per-profile membership.
2. `ryckema/Thermia_Connect_Firmware/data/cm930_profile_layer_model.csv` — L0 transport through L6 session/ACK, explicitly showing geometry/runtime/semantic/model differences.
3. `ryckema/Thermia_Connect_Firmware/data/cm930_profile_difference_matrix.csv` — 63 indexed cross-model facts and hypotheses; especially P012/P014/P020/P026/P036/P037/P038/P051/P052/P055/P061.
4. `ryckema/Thermia_Connect_Firmware/data/cm930_register_master_compact.csv` — register semantic candidates.
5. Existing public `Read-only/iTec Eco/thermia_itec_eco_waveshare_public_v01.yaml`, `Read-only/ATEC/thermia_atec_waveshare_readonly_v01.yaml`, `Read-only/Danfoss DHP-AQ/danfoss_dhp_aq_waveshare_candidate_v02.yaml`; their README files/captures; current XTR v31 FIX2 and canonical Research logs.

## Source-derived profile inventory (NOT verified HA or physically available register counts)

| CM930 semantic profile | Row membership | Relation to XTR | Caveat |
| --- | ---: | --- | --- |
| `1.1.1–2.1.0` | 516 | 516 overlap with XTR 2.4.2 | An older controller should not be mapped merely from UI name |
| `2.2.0–2.2.1` | 526 | 493 overlap with XTR 2.4.2 | Firmware formulas and packet counts can vary |
| `2.3.0–2.4.3` | 524 | Actual XTR M `0867=242` anchored to 2.4.2 | XTR semantic profile observed locally, not all 524 wire-readable |
| `3.0.0–3.1.1` | 526 | 493 overlap with XTR 2.4.2 | Firmware data available; no individually identified hardware baseline yet |

`492` rows have `YES` membership in all four; `7` additional master rows have no membership in these four flags and must not be assigned. These are **firmware schema row counts**, not separate working entity counts, not installed model lists and not proof of passive visibility.

## Existing model-specific read-only source inventory

| Family | Existing source | Named source entities | Evidence bound |
| --- | --- | ---: | --- |
| Thermia iTec XTR M | `Read-only/Thermia itec XTR/thermia_itec_xtr_m_read_only.yaml` | 250 | New v31 FIX2 not compiled/installed; live known-good V5DCM19 FIX1 separate |
| Thermia iTec Eco | `Read-only/iTec Eco/thermia_itec_eco_waveshare_public_v01.yaml` | 90 | Shared and Eco cross-model fields with unconfirmed candidates separately labelled |
| Thermia ATEC | `Read-only/ATEC/thermia_atec_waveshare_readonly_v01.yaml` | 112 | Genuine captured page shapes, candidate service mappings; read-only |
| Danfoss DHP-AQ | `Read-only/Danfoss DHP-AQ/danfoss_dhp_aq_waveshare_candidate_v02.yaml` | 96 | IDLE/DHW-capture reduction; A5 cooling/refrigerant telemetry candidate for this topology |

Counts are observed source `name:` entries within HA sensor/binary_sensor/text_sensor sections, not locally tested entity totals. The existing Eco/ATEC/DHP-AQ YAMLs have no configured UART `tx_pin` and do include DE `restore_mode: ALWAYS_OFF` (static source check, not electrical test).

## Source-backed differences that prevent blind XTR YAML cloning

- `03E8` physical full-page FC16 count: **ATEC 13**, **Eco5 14**, **XTR 14** (captures; P012).
- `0410` count: **ATEC 21**, **Eco5 22**, **XTR 22** (P014).
- `0492` count: **ATEC 9**, **Eco5 11**, **XTR 11** (P020).
- `051E` count: **ATEC 9**, **Eco5 10**, **XTR 10** (P026).
- Native 0884 history page: ATEC legacy **10 × 6** record layout versus Eco5 and XTR **8 × 7 + 4 words** (P036/P052). History-layout mapping is not included if the user excludes history/calendar; it still fingerprints native family.
- Native `0867` raw captured **ATEC 0x0016**, **Eco5 0x0000**, **XTR decimal 242**. XTR 242 safely selects semantic profile `2.3.0–2.4.3`; legacy 0/0x16 do **not** unambiguously select modern CM930 profile (P037/P038/P055).
- ATEC/DHP-AQ may expose `0xA5` refrigerant-controller runtime traffic that differs from the XTR direct `0x1E` outdoor-unit map; never transplant generic 0x1E units/scalings blindly.
- Version-specific semantic collisions and model capability gates are real. Physical page geometry by itself is insufficient to prove version or product identity.

## Proposed architecture

1. **Common RX-only transport core**: 9600 baud 8E1 only where physically documented for the target legacy topology; CRC, frame boundaries, FC16/FC23 request-response observation (no replies), bus-health, ESP uptime. Maintain zero UART TX pin/driver activity.
2. **Wire geometry fingerprint**: offline classify observed native page starts/counts and known source slave roles against genuine/collaborator captures; a missing 0x0F controller page is UNKNOWN, never automatically ATEC or XTR.
3. **CM930 profile semantics**: map register names/formulas/scale/signedness/profile collisions strictly with evidence and valid identity anchors. No heuristic mapping solely from `0867` legacy raw values, marketing model name or page-count coincidence.
4. **Model source adapter**: separate outdoor telemetry `0x1E` versus `0xA5` and any FC23 `0x04` external units, capability gates and known native operating contexts. Preserve model-specific source IDs.
5. **Uniform HA presentation**: same human categories as the manual (Info/Service + bus diagnostic), optional shunts/pool/buffer OFF/default-disabled unless source supports detection, no alarms/calendar (by current user product goal). Add declared/source availability and raw diagnostics disabled by default.
6. **Distribution**: share decoder specifications and generation fixtures under `Research/tools` or a future shared directory; publish **one self-contained YAML and one README per supported physical model** for user-friendliness. Respect existing XTR one-YAML/one-README rule.
7. **Offline regression matrix**: replay known cross-model captured frames in a non-transmitting host harness; validate expected geometry, conditional feature expiry, preserved production values, no undefined ID, no malformed substitutions; then ESPHome compilation separately. Avoid profile selection by speculation.
8. **User-initiated passive validation**: brief CRC-valid log from actual target model plus contemporaneous menu values if possible. Missing native pages without a genuine Online/DCM gateway are INCONCLUSIVE, not grounds to initiate DCM TX. Release only individually evidenced entities; use `RAW` with uncertainty for unresolved fields.

## Suggested staged releases (NOT RUN)

- `CM-RO-01` — offline shared model/provenance register-join inventory (four semantic ranges, profile collisions, native source adapter); PREPARED / NOT RUN.
- `CM-RO-02` — update existing **iTec Eco** read-only v01 against shared inventory, preserve Eco-confirmed fields and independent local captures; PREPARED / NOT RUN.
- `CM-RO-03` — update **ATEC** with its legacy page-count and source adapters; no XTR assumptions; PREPARED / NOT RUN.
- `CM-RO-04` — update **DHP-AQ** from its separate A5/direct-source captured evidence; PREPARED / NOT RUN.
- `CM-RO-05` — new 2.2.x/3.x semantic profile templates for controller-verified hardware **only after** a real version/profile anchor and passive capture; PREPARED / NOT RUN.

These are proposed source deliverables, not controller experiments. A commercial model without firmware/capture/topology support is **OPEN/UNKNOWN**, even if Thermia Connect supports a related protocol family. Do not claim applicability to Genesis/newer platforms.

## Risks and acceptance

- No product automatically gains 524 or 526 HA values merely from a firmware profile matrix.
- No incorrect temperature scaling on A5 refrigerant control, no cross-profile `07D1`/other semantic substitution, no incorrect legacy `0867` profile match.
- Preserve RX-only fail-closed behavior: no UART TX, response/ACK, scans or speculative writes.
- No disruption to live XTR/V5 installation or GitHub XTR release layout.
- For each generated YAML: distinct documented `PREPARED / NOT RUN`, source/static tests and compile status separated; only user-supplied live logs can substantiate on-device result.

**NEXT ACTION:** Generate a row-by-row cross-model evidence/mapping matrix from existing `ALL_PARAMETERS_ACCESS_MATRIX.csv`, `cm930_profile_difference_matrix.csv`, and the four YAML sources; review alias collisions and model-specific frame sources **offline**, without committing a presumed universal live configuration.
