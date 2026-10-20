# V5 Native Service-30 — V83 FAS1 source-provenance / dependency audit

**2026-10-20.** Experiment **V5-NATIVE-SERVICE-30-FAS1-SOURCE-DEPENDENCY-OFFLINE-01**: **COMPLETE / POSITIVE (offline audit)**. Physical XTR integration **PREPARED / NOT RUN**. Installed user-confirmed V83 FAS1 RX_ONLY/HARD_DENY remains unchanged, EXP388 RUNNING / PARTIAL, B11D first-start root cause OPEN.

## OBSERVED FACTS
- User FAS1 12-member additive ZIP SHA256 `43aaa5f1a3a43a6f353b5b2c2d9d88d08dfd249c82a13c35f9c55eaf117f9940` CRC clean. Includes `v5dcm83_first_alignment_snapshot.hpp` but NOT `v5dcm83_shared_rx_supervisor.hpp`. Its README explicitly states original V49 private includes are omitted. Original source had PREPARED/NOT RUN archive labeling at creation; not evidence it was never later installed.
- Previous Service29 private ZIP SHA `d2c26270b921f9954387aa037d55d789c6ded5efb3624eb0a248c9bd7b87a40b`, 180 CRC clean members. Source YAML lists 54 header includes; 53 are present, **one missing: `v5dcm83_shared_rx_supervisor.hpp`**.
- New FAS1 uploaded candidate YAML sha `2c01c04641d62a753fd79d3445c1527e1016a922c8aa6b86632fbc3691dcbe5c` differs from S29 `REFERENCE_V83_FAS1_RX_ONLY_UNCHANGED.yaml` sha `b4aaedf27f8dd3d58fcc7c09316cfe03d9c8f41d40fcd827a31bf1f104d389fa`. Four diff blocks include one new comment, a native TX-owner policy header include, and a **V43/V44B RX dispatch widening from only single-frame clean callback to iteration over all parsed frames** when no pending tail. Material source behavior difference; no local live acceptance evidence or verified on-device equivalence; do not silently select either.
- Original FAS1 `SOURCE_INFO.json` verified original candidate hash and records an earlier separate V83 source archive not included.

## OFFLINE TEST RESULTS
- FAS1 source `run_host_tests.sh`: 200036/200036 PASS for each of 3 configurations; 2 forbidden TX macro builds refused as intended.
- S29 `RUN_SERVICE25_HOST.sh`: 32/32 host executable tests PASS; synthetic only.
- S29 `VERIFY_SERVICE29_OFFLINE.py`: 24 unchanged production top-level, 197 unchanged HA identity tuples, defined substitutions, no new physical UART/DE write, inherited missing include explicitly reported.
- Independent metadata-only S30 source ZIP auditor confirmed hashes, member inventories, four YAML diff blocks and missing shared header. No private/protected source code published.
- **No ESPHome compilation, flash, actual RS485 TX or new live XTR controller evidence**.

## CONCLUSION / OPEN / NEXT
Complete host-level source comparison does NOT recover the missing header or establish byte-identical running firmware. Service29 staged candidate **NOT FLASH-READY**; B11D remains OPEN; actual XTR native profile/version/session and slot remain UNKNOWN. No fake header or TX arming.

Next smallest input: exact original private `v5dcm83_shared_rx_supervisor.hpp` from verified V49/V83 original bundle (or the full source ZIP, plus SHA manifest if available). Verify and restore dependency then review the multi-frame V43/V44B behavior offline, while keeping user-running V83 FAS1 and TX HARD_DENY unchanged. Standalone S30 audit-only ZIP SHA256 `46616110c67293fac0e4e3f2049318e32d77868b1321e44e373f6358b83ee0ec`.

**Safety/rollback:** unchanged verified V83 RX_ONLY; historical V49 fallback. No independent live tests approved here.
