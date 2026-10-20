# V5 Native Service-32 — correction to XTR version and product provenance

**ID:** V5-NATIVE-SERVICE-32-PROVENANCE-RECONCILIATION-OFFLINE-01. **2026-10-20. Status: COMPLETE / POSITIVE — OFFLINE AUDIT ONLY.** Actual XTR run PREPARED / NOT RUN. Last user-confirmed V83 FAS1 RX_ONLY/HARD_DENY remains unchanged, EXP388 RUNNING/PARTIAL, B11D first-start issue OPEN.

## OBSERVED SOURCE FACTS

The earlier S29 and V5DCM92/V5DCM93 characterization of five timestamped files as *local XTR evidence* was incorrect. V5DCM64 already identified the 2026-10-03 capture as **ATEC** and four 2026-09-24/25 files as **model unconfirmed**, with genuine Eco5 captures in separate files. The value decoding itself was correct but physical provenance was not. This correction **SUPERSEDES ONLY THE INFERRED LOCAL-XTR ATTRIBUTION**, preserving all historical raw observations.

An independent new SHA256-pinned, byte-length- and Modbus-CRC-checked offline audit of all seven supplied raw files found **2,500 valid 0x0F FC16 request ADUs, 1,365 valid FC16 ACKs, and zero malformed/CRC-bad matching candidates**. The exact **0864/count4** fourth-word distribution: **Eco5 48/48 raw232 (0x00E8), ATEC 12/12 raw22 (0x0016), Sep24/25 model-unconfirmed 7/7 raw22**. None of the 19 raw22 examples is independently proven local XTR.

Separate earlier **locally tested XTR S11D (2026-10-07, COMPLETE/POSITIVE)** reports its 0864/count4 fourth word **0x00F2 = 242**, with ACK and subsequent 0870/count17. Provenance: Thermia_Connect_Firmware/findings/XTR_S11D_POSTRUN_OFFLINE_0864_0870_20261007.md and XTR_LIVE_SOURCE_RESPONDER_S11A_S11D_20261007.md. This is a documented earlier local user experiment, **not** an original S11D raw-bus capture revalidated in this audit and **not** current V83 epoch evidence.

Genuine original Connect 2.1.105 device_client/data/info.py identifies decimal register2151/0x0867 as hp_cm_firmware_version and uses the decimal digits version decoder: 22 -> 0.2.2, 232 -> 2.3.2, **242 -> 2.4.2**. Separate original 2.1.105 info-2.4.2.json identifies product code from decimal register1337/0x0539, **not** 0x0867: product code 1 is iTec E 5kW 1N; code22 XTR M 1N; code23 XTR M 3N. In these seven files product raw1 appears Eco5 18, ATEC 1, unconfirmed 2; the three samples previously called historical 'XTR product1' in V92/V93 lack XTR provenance. **Product code22 and version raw22 are unrelated fields.**

## STRONG CONCLUSION

The claimed local-XTR *22-versus-242* conflict **is NOT evidenced by a single verified XTR corpus**; it arose from conflating ATEC/unconfirmed captures with previously documented local XTR S11D. Earlier XTR 242 is consistent with the source-supported Connect 2.1.105 profile range (2.3.0-2.4.3) and XTR product-map entries, but neither active 33/33 app readiness nor actual current native Connect/Online acceptance is proven.

S29's fail-closed policy against unsupported raw22 remains a valid negative test; its stated premise of locally captured XTR raw22 is **DISPROVEN**. Importantly S11D's *historical* 242 does not satisfy S29's explicitly required same-session/current verified XTR version and does not authorize TX or remove the inherited missing original V83 RX-supervisor dependency. The S29 staged YAML remains **NOT FLASH-READY**.

## Reproducibility / remaining gaps

Standalone, read-only Service32 verifier pins all seven original SHA256s, checks exact FC16 byte count, CRC and origin cohorts, and independently confirms the original firmware's version formula and product-code map. **6/6 host tests PASS**, including CRC negative, malformed length, ACK/request distinction, file hash tampering and current-XTR non-attestation. Original raw files and firmware source unchanged. User private Service32 audit ZIP SHA256 `4b58cd85f118d219a0e36d1282ee0876824b053bda2e311ed16c1c7978c7ce6b`; no proprietary firmware, keys or protected handshake source published.

**UNKNOWNS:** current user-running V83 device version, live info/profile selection, controller owner/slot, B11D root cause, true original Connect application C2/Online, actual semantic writes. **NEXT:** recover authentic private full V83 source bundle or `v5dcm83_shared_rx_supervisor.hpp`; maintain source-correct provenance and inspect S29/FAS1 multi-frame callback divergence before any ESPHome build. Physical TX, flash, installation, device reboot and new on-bus experiment **NOT RUN**. Rollback unchanged user-confirmed V83 FAS1 with V49 fallback.

References: Research/V5DCM/V5DCM64_LEGACY_DISPLAY_VERSION_AND_REQUEST_BITMAP_CORRELATION_OFFLINE_RESULT_20261019.md; Research/V5DCM/V5DCM65_XTR_FIRST_EVIDENCE_VS_LEGACY_DISPLAY_PROFILE_OFFLINE_RESULT_20261019.md; Thermia_Connect_Firmware/findings/XTR_S11D_POSTRUN_OFFLINE_0864_0870_20261007.md; original user-provided seven capture files and original Connect 2.1.105 source archives.
