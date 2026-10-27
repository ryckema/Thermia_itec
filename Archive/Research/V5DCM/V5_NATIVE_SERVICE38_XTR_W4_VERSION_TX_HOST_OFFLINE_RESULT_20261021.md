# V5 Native Service-38 — local XTR runtime version-page geometry in the private TX service

**Date:** 2026-10-21. **Experiment ID:** V5-NATIVE-SERVICE38-XTR-W4-VERSION-GEOMETRY-TX-HOST-01. **Status: COMPLETE / POSITIVE — OFFLINE SOURCE/HOST ONLY.** Physical XTR test **PREPARED / NOT RUN**.

## Baseline, provenance and controlled change
Last user-confirmed running V83-family device remains RX_ONLY/HARD_DENY; the separate FAS1 add-on has no independently confirmed later flash. EXP388 remains RUNNING / PARTIAL and the original B11D first-start fault is OPEN. Verified V49 source remains rollback. Private Service-37 input ZIP SHA256 `6c228cdc0dd462f719edcf19714a3fcc26453f6cabeaf3247c9b01e4fb49257c`; staged S36/S37 RX-only YAML SHA256 `55c6b1aaa8e17ea8d4ccc51d59fb7f6bc6673554cb5a2cacc841fd80574cc6ca`.

**Hypothesis:** The existing source-level native V5 TX service incorrectly conflated original Connect CM930 W4-bit8 selector span (12 addresses) with the locally observed XTR's physical native FC16 version-page length (4 words), causing the XTR version page to be rejected by its cache and excluded from the application receipt tracking.

**ONE narrow functional change:** in a copy of the private Service-37 tree, modify only the runtime page-store and CM930 receipt bookkeeping path in two existing C++ headers so the XTR-specific physical 0x0864/count4 page is recognized, cached only after simulated ACK completion and counted against the original W4-bit8 selector when eligible. Unexpected 0x0864/count12 physical frame is rejected for this XTR-specific target. The firmware selector map, 31/33 source-significant-group lists, profile gates, actual RX-only YAML and original V83/B11D components are all unchanged.

## OBSERVED FACTS — evidence hierarchy
1. **Earlier completed LOCAL XTR S11D** documents 0x0864/count4 with raw 0x0867=0x00F2 (242), ACKed before a subsequent 0x0870 publication. This S38 audit used the prior verified S11D research report, not the original raw S11D bus capture anew. Historical acceptance does not prove current V83 readiness.
2. **Exact original Connect 2.1.105 AppFS** `modbus-flags.json` SHA256 `bb0b335eaf4e3a98e5d71d1cd1551e0772fedcfcd3f7d17f3c78e04c21844b9e`: request selector W4/1804 bit8 owns decimal 2148–2159 (0x0864–0x086F), **12 register addresses**. A selector-owned register range is not a guaranteed physical FC16 request size on a different model or software generation.
3. **ATEC V3 external source** has analogous native slave0F gateway lifecycle and FC16/FC03 services. It is EXTERNAL SOURCE/CLAIM with a different controller/display topology and does not establish XTR frame geometry, safe slots or transferable authentication.
4. **Exact previous S37 C++ source, strict host probe:** `cm930_group_exact25(0x0864,4)` returned false, the nominal 12-register version group matched and a valid CRC native 0x0864/count4 frame was not staged. The after-ACK raw-version witness and the CM930 W4 group receipt both previously required a 12-word count. These are source-level reproduction facts, not a new physical XTR failure.

## Offline test results — actual executions
- **HOST FakeIO dual-scoped-mode rehearsal PASS:** synthetic native startup followed by **32** V4.1-derived initial settings pages, runtime transition, correct XTR 0x0864/count4 and post-ACK version242, then cached FC03 readback. This is a fake transport simulation, not an original firmware approval, real physical response or semantic setpoint confirmation.
- **Negative controls PASS:** default/no-TX-macro and either single-macro mode result in zero FakeIO writes; 12-word physical version frame denied; malformed CRC produces no FakeIO write; profile/Online is not auto-granted by version/one receipt; physical-slot-condition loss revokes subsequent fake delivery.
- **4 C++17 host configurations PASS** and **1 UBSan host run PASS** for the new synthetic test. ASan+UBSan execution was blocked by this environment's address-space ulimit; do not claim ASan PASS.
- Existing private regression `RUN_SERVICE25_HOST.sh`: **35/35 executable host tests PASS**. Prior RX-only `VERIFY_SERVICE36_OFFLINE.py`: **40/40 PASS**. New S38 immutable-parent source/provenance verifier: **14/14 PASS**.
- Exact audit of the private Service37 archive proves that among its **217** original members, only **two existing headers differ**; current V36 production YAML remains byte-identical, including 24 production top-level blocks, all 198 existing HA identities, single V5 RX parser, UART/DE configuration, B11D sticky faults and original supervisor. The S36 RX-only TX-macro compile-denial is intact.
- **NOT RUN:** ESPHome/ESP-IDF embedded compilation (toolchain inaccessible), ESP32 flash, live RS485 TX, slot measurement, peer/epoch ownership, controller restart, true native Connect APP C2/Online, application write or readback acceptance.

## Strong conclusion, hypotheses, unknowns, next
**PROVEN OFFLINE SOURCE/HOST:** a real XTR-specific four-word runtime version publication is now geometrically representable across the existing V5 native response service's page cache and CM930 receipt shadow, without altering the vendor selector map or the protected original backend. The existing TX-capable service can exercise a full 32-page mock transport progression. This is necessary engineering toward TX but not sufficient live eligibility.

**HYPOTHESIS:** once a *separately tested TX-capable ESPHome target* and actual independent physical owner/slot/session attestation exist, the corrected version path will participate in XTR native startup; this has not been tested on hardware.

**OPEN:** actual ESPHome build, shared V83/B11D/watchdog TX ownership, independent electrical EOF/peer/slot, current XTR version/epoch, native Connect application readiness, and controller semantic acceptance. Do not interpret FC16 ACK or fake FC03 readback as a real configuration change.

**NEXT Service39:** prepare a distinct privately audited, fail-closed TX-capable build target, preserving the current S36 RX-only rollback, one physical UART/DE owner, V4.1 local full-service sequence and independent abort/rollback. No auto-TX and no user-live bus TX without a separately scoped initiated test. No secret handshake, ATEC key, algorithm, protected 0x0F response logic or 0x0708 implementation published.

**User-private archive:** `V5_NATIVE_SERVICE38_XTR_W4_GEOMETRY_TX_HOST_PRIVATE_20261021.zip` SHA256 `f1f5c14c205c91ede175ea165f8fc07b18b01b510d1779556fa9c95709725cf6`, 223 CRC-clean files. This contains inherited protected firmware-derived code and is not licensed for redistribution.
