# V5DCM23 offline integration verification — 2026-10-18

**V5DCM23-EMBED-OFFLINE-01: COMPLETE / POSITIVE** (source-level host test and historical replay).
**V5DCM23-EMBED-LIVE-01: PREPARED / NOT RUN** (no ESPHome build, flash or device test).
Native session acceptance and Online readiness remain **OPEN / UNKNOWN**.

Built a separate private research candidate from the prior V5DCM22-on-V5DCM19 archive. It adapts the public RX-only `PassivePackageLedger` to the existing completed-frame callback, using the original portable frame decoder and retaining the older observer as an independent diagnostic comparison. No extra UART reader, no response path, no new transmission code.

Offline g++ C++17 warnings-as-errors host tests passed. The historical 2026-10-03 byte-exact 2,687-frame capture replay passed CRC and session-boundary checks: 162 native FC16, 2 FC23, zero qualified packages after boundary revocation and no application readiness claim.

A controlled four-insertion source-diff check reconstructs the preceding private YAML byte-for-byte. Original HA inventory (117 numerical sensors, 13 binary sensors, 47 text sensors, 3 buttons), original log intervals, UART configuration and RX-only policy remain intact. Current V5DCM19 lineage is not feature-equivalent to the wider full-monitoring v31/RX33 HA configuration. The previous live RX33 test remains RUNNING / PARTIAL and its boot/OTA rollback warning is unresolved.

Private archive SHA256: `127d781089134569299f4e01faa8c380d2176dcd0794e06a7fd971240e6c179d`. The archive and internal project-specific sources are NOT published to GitHub. No physical operation was initiated. Full ESPHome compile remains unverified. Do not replace a working installation with this candidate yet.

Next offline: reconcile exact deployed image provenance and HA feature parity; validate entire ESPHome build when feasible; retain safety limits and original evidence.
