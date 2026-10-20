> **2026-10-20 SOURCE-PROVENANCE ERRATUM (Service-32, DISPROVEN / SUPERSEDED attribution only):** This historical report's five Sep24/25+Oct03 files were described as local XTR captures without model proof. Oct03 is ATEC; Sep24/25 are model-unconfirmed per prior V64. Their 19 version0867=22 and three product1337=1 observations are REAL CRC-valid historical bytes, but do NOT establish local XTR version/identity or contradict local reported S11D version242. Preserve the original report below as historical analysis; authoritative correction: [Service-32](V5_NATIVE_SERVICE32_VERSION_IDENTITY_PROVENANCE_CORRECTION_OFFLINE_RESULT_20261020.md). Current V83 epoch remains unknown.

# V5DCM92 — XTR support in original Thermia Connect 2.1.105 firmware

**ID:** V5DCM92-XTR-NATIVE-CONNECT-PROFILE-OFFLINE-01. **COMPLETE / POSITIVE (OFFLINE original-source support verified, current XTR session/profile remains OPEN)**. 2026-10-20.

**Baseline:** user-verified V83-FAS1 RX_ONLY/HARD_DENY, original V49 rollback, EXP388 RUNNING/PARTIAL, unresolved separate historical V83 first-start B11D fault. One change: offline read of original appfs CM930 info profiles versus CRC-verified historical XTR captures and official Thermia Online compatibility. No hardware change, ESPHome compile, flash or physical TX.

## Observed facts

The international Thermia Online page explicitly lists iTec XTR with Thermia Connect; the Belgian page omits XTR in its enumerated models. Original extracted Connect2.1.105 `/etc/device-client.d/930/2.3.0-2.4.3/info-2.4.2.json` and `info-2.4.3.json` each have `info[1]` called `product_name_configured`, description `Product name of the heatpump control module`, formula `{1337}`. XTR map entries: 21 S 1N, **22 XTR M 1N**, **23 XTR M 3N**, 24/25 L 1N/3N, 26/27 XL 1N/3N. Earlier info-2.3.0/2.4.0/2.4.1 do not include XTR codes. The containing profile directory is 2.3.0–2.4.3; this does **not** prove automatic original Connect version/profile selection for local XTR.

Fresh offline reparse of five archived user XTR logs with exact 0x0F FC16 request length + Modbus CRC: `1337`/0x0539 raw1 seen in 3 old FC16 requests (Sep25 09:02, Sep25 09:05, Oct03); this stock info map would label raw1 `iTec E 5kW 1N`, conflicting with physical XTR M. `2151`/0x0867 raw22 seen 19 times (2+4+1+0+12). Original CM930 version extractor maps raw22 to 0.2.2, absent from shipped profile ranges as V87/V88 showed. Both mismatches remain open: no substitution of code23 or hypothetical raw220. Historic request values do not prove genuine Connect runtime identity or semantic acceptance.

ATEC V3 is EXTERNAL SOURCE/CLAIM, useful for abstract protocol comparisons, not XTR code/profile or safe TX proof. Its missing cited captures and authentication/IP caveats remain.

## Conclusion

**PROVEN VENDOR SOURCE** XTR support in 2.4.2/2.4.3 info maps; **PROVEN HISTORICAL XTR** old raw1337=1 and raw2151=22; **OPEN** identity acquisition lifecycle, version corrections/actual profile loading, physical wire role/slot, authenticated session and semantic acceptance. FC16 ACK is not application acceptance. No TX, compile, flash or new live test. Abort source/CRC inference on any assertion failure; hardware rollback not applicable.

**NEXT V5DCM93 OFFLINE:** audit native product identity acquisition and historic register1337 chronology; prioritize true XT/XTR source over older ATEC. Retain FAS1 HARD_DENY, EXP388 partial and V49 rollback.

Official sources: https://thermia.com/products/thermia-online/thermia-online/ and https://belgium-nl.thermia.com/producten/thermia-online/ . Original source: user-supplied Connect 2.1.105 extracted appfs, plus archived local XTR captures.
