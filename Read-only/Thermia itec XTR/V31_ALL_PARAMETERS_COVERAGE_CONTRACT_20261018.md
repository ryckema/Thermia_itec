# V31 FULL PASSIVE PARAMETER COVERAGE CONTRACT — 2026-10-18

Status: PREPARED / NOT RUN. Offline source inventory reviewed; no YAML generation/compile/flash or new live XTR evidence.

## User requirement (supersedes menu-only scope)
Expose **every parameter that the existing XTR M passively broadcasts and can be decoded**, including parameters absent from the commissioning manual's INFO/SERVICE menus. All must be read-only in HA, except calendar and alarm entities which remain excluded. Optional 2nd/3rd heating circuit, pool, buffer should have conditional runtime availability and HA disabled-by-default registration until enabled by user.

## Authoritative inventory
`ryckema/Thermia_Connect_Firmware/parameters/ALL_PARAMETERS_ACCESS_MATRIX.csv`: 564 distinct firmware-register rows, of which 524 have `xtr_m_cm_2_4_2=YES` and 40 are other-profile-only. Among 524 XTR-profile entries, 468 are firmware write-capable settings and 56 are runtime read-only (write capability is ignored for v31). Source inspection completed 2026-10-18. These are **firmware schema entries**, NOT 524 locally proven readable values or necessarily 524 separate HA entities. Profile declaration `YES` does not establish a frame was observed in an XTR capture.

Menu tables `MENU_REVIEW_INFO.csv` (46 rows), `MENU_REVIEW_SERVICE.csv` (24), `MENU_REVIEW_UNCONFIRMED.csv` (494) are optional organizational aids, NOT allowlists and NOT additional registers. Individual calendar fields can drastically inflate apparent entity counts; count registers uniquely.

## Deliverable definition
- Start from v31-alpha01/v30-alpha12 broad passive decoder and the actual verified V5DCM19 FIX1 RX framing, taking care not to regress production readings or import TX functionality.
- Catalog **all 524 XTR-profile registers**, plus any independent locally proven XTR register missing from CM930.
- For each register record: hex/decimal address; firmware read name; category and observed native FC/page/count; exact parser source; local XTR evidence grade; scaling/signedness/unit/sentinel; runtime freshness; option capability; HA ID; manual INFO/SERVICE classification or 'Additional native telemetry'; coverage state.
- Coverage states: `DECODED_VALIDATED`, `RAW_OBSERVED_UNMAPPED`, `FIRMWARE_ONLY_UNOBSERVED`, `OTHER_PROFILE_NOT_XTR`, `EXCLUDED_CALENDAR`, `EXCLUDED_ALARM`, `OPTIONAL_NOT_INSTALLED`, `AMBIGUOUS_SEMANTIC`.
- Decoded validated fields: normal human-readable HA entity, with numeric units/state classes where appropriate. On-wire observed but unresolved fields: **read-only RAW diagnostic** disabled-by-default with stable unique IDs, never mislabel as proven semantics. Firmware-only unobserved fields: **do not report fake values or manufacture activity**; include them in coverage inventory and if valuable provide a separate HA diagnostic availability indicator only after actual source is seen. Unknown is unknown, not zero.
- All values read from received CRC-valid full pages/known native controller-origin frames, with consistent page/count/source and freshness; no synthetic reads/queries/scans.
- Reuse existing HA entity IDs, make aliases rather than duplicates where several firmware labels point to one same measured value, and preserve persisted settings cache semantics.
- Apply option detection `0533 pool`, `0534 shunt-group1/2nd circuit`, `0535 shunt-group2/3rd circuit`, `0536 buffer` after page seen and valid. A missing page isn't evidence a feature is absent. ESPHome `disabled_by_default` is registry-time, not a dynamic HA toggle; separately gate live sensor availability.
- Avoid exposing alarms or calendar, even as user-facing raw-register entities; preserve internal parser/health where needed. No service actuation/button/select controls.

## Coverage acceptance criteria
Full source-derived inventory accounted for: 524/524 XTR-profile rows have a coverage state and provenance, no silent omissions; no claims 524/524 physically readable until independently shown. Every observed and supported local XTR register has a published semantic or raw diagnostic entity unless excluded. Existing v29/v30 functional entities survive. Zero physical TX, no enabled UART TX GPIO, no unauthorized DCM responses. Strict YAML parse and substitution/ID checks, then ESPHome compile, then user-flashed passive soak before COMPLETE / POSITIVE. An offline map alone cannot satisfy hardware success.

## Next concrete work
1. Join the master access matrix, the reviewed menu files, actual v30-alpha12 parser and original V5DCM19 source to build a per-register **coverage CSV**.
2. Parse locally observed page geometries from XTR native capture and separate bus-observed versus firmware-only rows.
3. Generate an HA entity manifest and expanded YAML in batches with exact register mapping and guard; keep oversized raw groups diagnostics/disabled by default for performance.
4. Replay historical captures offline, then verify source and compilation; only afterward live flash.

Existing alpha01 is an interim candidate, **not full coverage**. This note supersedes its menu-only interpretation. No change to V5DCM21 native-write readiness track.
