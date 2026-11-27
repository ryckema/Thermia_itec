# iTec XTR M — Write Service SVC4 live evidence and SVC5 0410 read handoff

**Updated:** 2026-11-13. **Scope:** XTR M 3N / CM930 controller 2.4.2. This is an evidence and implementation note, **not a public firmware release**. Existing `README.md` and `Write (Beta)/iTec Eco/` remain protected and unchanged.

## OBSERVED FACTS — SVC4 owner log (2026-11-12/13)

- Exact firmware banner: `Thermia WRITE-SERVICE SVC4 (RC09FC) | 0532 scoped read opt-in + trimmed menu / 0449 trial default OFF`.
- Native session qualified (`M6=5`, stage 40), CURRENT snapshot 4/4, original Write User available; sampled V5 CRC differences = 0, RX buffer drops = 0. No new parameter write was performed.
- At 00:37:55, the bounded `0x0532` READ was manually armed; the existing native owner issued `W3=8000` at 00:37:57. Later status: `CONFIRMED / fresh controller FC16 0532/18 received / no setting write` (visible by 00:38:15). **SVC4-0532-SCOPED-READ: COMPLETE / POSITIVE** for one controller-origin `0532/18` response and source freshness, not for indefinite auto-refresh.
- `Installation | Energy Performance (OEM)` was `0`. `0x0543` is `energy_performance_enabled`, an installation enable flag, **not** measured COP or delivered/consumed energy.
- At the same time the Service page status showed `03FC=MISS 0410=MISS 04A6=MISS 0532=OK`; warm-water Service registers `0x041D`, `0x041E`, `0x041F`, `0x0420` remained `VEROUDERD`. Missing data is not proof that controller features are absent.
- Source-based SVC4 menu cleanup removed **137** read-only catalogue entities: 122 with no XTR register mapping and 15 duplicating existing Write User controls. It retained 24 mapped Service menu statuses, ordinary telemetry, Write User controls and diagnostics. Old HA registry entries may require separate entity-registry cleanup.

## STRONG CONCLUSIONS

- The `0x0532/18` parser and native request path already existed in the earlier Write User lineage; SVC4 restored targeted refresh rather than discovering a new register.
- SVC4's successful `0x0532` read does **not** prove `0x0410` is refreshed, nor validate any new service-level setting write.
- The remaining warm-water `VEROUDERD` status is consistent with a missing same-session `0410` page. No repeat of the already positive 0532 experiment is required without contradictory evidence.

## SOURCE / OFFLINE TESTED — SVC5 implementation

- **Status:** `PREPARED / NOT RUN` for `SVC5-0410-READ`. SVC5 is not ESPHome TARGET COMPILED, FLASHED, LIVE or LOCALLY VERIFIED.
- Root cause in source: SVC4's C5DN mirror copied only FC16 `0410/21`; the native 33-page request matcher expects `0410/22`. SVC5 mirrors the first 21 words for both received shapes, preserving the old 21-word mirror, and requires a genuine CRC-valid same-session `0410/22` page for **native read success**.
- One disabled-by-default Home Assistant button arms native `0x0410` request (`W3` bit 2) using the existing S92 single UART/RX/TX/DE owner and original bus/session/collision guards. No separate physical writer or parameter-write command is added.
- The optional `0410` automatic refresh is **disabled/OFF at boot**, requires explicit opt-in after a positive manual one-shot, and is bounded to 12 attempts/boot, at least 240 seconds between requests and lockout after two missed cycles. The original 300-second Service freshness TTL remains.
- The previous `0x0532` refresh, V5 parser/CRC, FC16/FC03, CURRENT 4/4, hot-rejoin, calendar, all established Write User controls and experimental but disabled `0x0449` KOELTIJD service write are preserved. The 137 removed menu catalogue items remain removed.
- **OFFLINE TESTED:** strict YAML/unique IDs, C++17 syntax fragments of new actions, sole physical UART TX owner, ZIP integrity. This is not a full ESPHome target build or a live bus test.

## EXPERIMENT — SVC5-0410-READ

- **Hypothesis:** an owner-initiated W3 bit-2 request produces a genuine `0x0F FC16 0410/22` controller page, making `0x041D..0x0420` source-fresh.
- **Baseline:** SVC4 owner-LIVE `0532/18` native read positive, 4/4 CURRENT qualified, no sampled CRC/RX errors, `0410=MISS`.
- **ONE meaningful protocol change:** accept `0410/22` in the existing C5DN service cache and request only this page through the existing native read scheduler; optional auto remains OFF.
- **Expected:** one manual `0410_READ_ARMED`, a native request for W3 bit2, genuine controller `FC16 0410/22`, `0410=OK`, then controller-origin raw values for applicable warm-water fields. Transport ACK alone does not count.
- **Actual:** SOURCE / OFFLINE TESTED only. **No SVC5 live FC16 read receipt supplied.**
- **Bounds:** user presses the one-shot once; original 60-second TX lease plus 240-second passive receipt horizon; no default automatic retries or setting writes.
- **ABORT:** existing `Configuration | ABORT Native Session`, and turn optional 0410 auto refresh OFF. **Rollback:** exact SVC4 owner-LIVE YAML in private SVC5 ZIP; no thermostat/service setting changed by this read experiment.
- **Status:** `PREPARED / NOT RUN`.

## ARTIFACT PROVENANCE / PRIVACY

- SVC4 owner-LIVE private ZIP: `Thermia_iTec_XTR_M_WRITE_SERVICE_SVC4_0532_REFRESH_CLEAN_20261112.zip` SHA256 `b3c6117d8311abab4784bd3db3acd6d6cc95b4751f74c0d75e131bcf97ca2cdf`.
- SVC5 complete private ZIP: `Thermia_iTec_XTR_M_WRITE_SERVICE_SVC5_0410_NATIVE_REFRESH_PRIVATE_20261113.zip` SHA256 `e76b3c69a8dddf5029ccf03fe2e968ad819fed980700600a9159fc0ede28e7bf`.
- SVC5 main YAML SHA256 `dc95bef87c62b01fe94d2814422700e9dabc5f5b71ed61f8394aafc30fb104ac`; byte-identical SVC4 rollback YAML SHA256 `5fa279f9060ae0f580146fd62268cc8ae837074c878cb75886440cdfef212a3d`.
- Private firmware, captured handshake material, sensitive OEM implementation details, credential data and raw logs are **not** committed here.

## CURRENT MILESTONE / DELIVERABLE / REAL BLOCKER / ONE NEXT ACTION

- **CURRENT MILESTONE:** SVC5 native warm-water Service refresh.
- **DELIVERABLE:** integrated private SVC5 full firmware ZIP plus this research handoff; SVC4 0532 read locally observed positive.
- **REAL BLOCKER:** no source blocker to compiling; one owner-initiated `0410/22` controller-origin live receipt is still required to prove the new read path.
- **ONE NEXT ACTION:** owner compiles/flashes SVC5, verifies normal M6/CURRENT/RX runtime with auto 0410 OFF, then presses `Configuration | Service | Read Hot Water 0410 (One-Shot)` once and checks `Diagnostic | Hot Water 0410 Refresh Status` plus `Service ⁄ Parameters Status`.
