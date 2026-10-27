# V5 Native Service-35 — original V83 RX supervisor recovered

**Date:** 2026-10-20. **Experiment:** V5-NATIVE-SERVICE-35-V83-ORIGINAL-SUPERVISOR-RESTORE-OFFLINE-01. **Status: COMPLETE / POSITIVE — OFFLINE SOURCE/HOST ONLY.** Physical XTR / embedded build: PREPARED / NOT RUN.

## OBSERVED FACTS — provenance first
- Newly uploaded original V83 RX-only source ZIP SHA256 **f3b5d9945086039e8a2eb371870598171adda8b50a81b6bb68ae9af6a23a9e04** exactly matches the previous FAS1 source-metadata reference; 13 members, CRC clean, 12/12 internal manifest entries valid.
- Its authentic **v5dcm83_shared_rx_supervisor.hpp** SHA256 **26fecbe09242eb2c8dcd30d66a079f7d213136b58b6865054e0a2a0e13beea6b** was the previously missing source dependency. The original V45 helper file is byte-identical to the Service34 copy (SHA256 649c820ba45fbbbbbcdbdcdab2f849956f6c587acacf0540fb413b4e170e4922).
- Reuploaded FAS1 ZIP SHA256 **43aaa5f1a3a43a6f353b5b2c2d9d88d08dfd249c82a13c35f9c55eaf117f9940** is identical to previously audited FAS1, with matching original passive snapshot header.
- Exactly one private source modification to the Service34 archive: restore the authentic, unchanged V83 header. A separately named S35 staged YAML is **byte-identical** to original staged S34 YAML (SHA256 **4d8f85717fe53dd2e5c5b89758329602dfc92d7b76429dd6b0dcc51131f9b3bf**).
- All **64** direct C++ header names in the staged YAML now have local matching files. Separate transitive scan found only external ESPHome/ESP-IDF platform header references, not another missing project-original safety header. This is source inventory closure, **NOT an embedded compile pass**.
- The unchanged source retains **24 original YAML top-level blocks**, **197 original HA ID/name identities**, and the additional existing S34 passive version diagnostic (198 total). Physical UART configuration, parser, owner, B11D sticky fault and original RX callback behavior were not edited. No new UART or GPIO/DE write was added.
- **Safety distinction:** the original V83 header explicitly rejects older V42 native TX compile switches but **does not reject the later Service23 scoped-TX macro pair**. In the unchanged S35 source those macros are not defined and no live session bind, reviewed profile installation, runtime refresh or scoped TX arm is invoked. Before a future embedded RX-only build, a separately tested explicit fail-closed rule for newer build switches is still required.

## OFFLINE TESTS ACTUALLY RUN
- Authentic V83 host test: **3 x 78,313 assertions PASS** (normal, sanitizers, no exceptions/no RTTI), two legacy forbidden build modes rejected.
- Authentic FAS1 host test: **3 x 200,036 assertions PASS** (same three modes), two legacy forbidden build modes rejected.
- Integrated S34+restored V83 source **34/34** host executable tests PASS (including pre-existing fake-I/O tests, **no physical TX**). Targeted V83+FAS1+S34 C++ source link passed independently in strict, sanitizer and noexceptions modes; two legacy forbidden build attempts rejected.
- Standalone integrity and YAML verification **22/22 PASS**; with both original ZIPs supplied, **26/26 PASS**. Original unmodified parent Service34 audit passed *before* adding the missing header. Its historical assertion that the header was absent naturally must not be used to assess Service35.
- **NOT RUN:** ESPHome/PlatformIO compile or link, actual ESP32 flash, electrical timing, physical TX, controller reboot, current XTR version/profile, authenticated Thermia Connect/Online C2, semantic writes.

## STRONG CONCLUSION
The missing **original** V83 safety dependency is now recovered, not synthesized. This removes the previous project-include blocker for the private S34 source tree without changing its output-authority logic or claiming any native controller acceptance.

## HYPOTHESES AND UNKNOWNS
The B11D first-boot alignment fault remains unexplained. Original V83/FAS1 native callback logic differs from Service29/34 for coalesced/partial RX frames (see earlier Service30/33 and V5DCM80), unchanged in S35. The source's optional later scoped TX build flags do not have a universal compile-time denial in the restored V83 header; no evidence of safe physical owner/slot, verified controller epoch or real vendor application profile admission. A header inventory pass does not prove embedded compatibility or production safety.

## NEXT ACTION / safety / rollback
**Next offline work:** add/review an explicit compile-time hard-deny for newer Service23 TX switches in an RX-only candidate, and reconcile per-completed-ADU native callback delivery while preserving all existing V5/B11D/FAS1 safety and HA. Only after new source/embedded validation could the user separately initiate a scoped RX-only device test. No new active TX or controller restart is warranted.

**Baseline:** last user-confirmed running V83-family RX_ONLY/HARD_DENY; FAS1 overlay independently PREPARED / NOT RUN without subsequent user evidence; EXP388 RUNNING / PARTIAL; B11D startup root cause OPEN; earlier verified V49 private source remains rollback. Current service35 change is private offline only, no device rollback action required. Private user archive SHA256 **c89287f3a565a0718beb5dd2244a68791d93c62779a48683249daba3e40cb5f5**; private firmware-derived code and native protocol/authentication implementation must not be published.
