# V5 Native Service-29 — version provenance and source-range gate (2026-10-20)

**Experiment ID:** V5-NATIVE-SERVICE-29-VERSION-PROVENANCE-OFFLINE-01. **Status:** COMPLETE / POSITIVE (offline C++/source only). Physical XTR: PREPARED / NOT RUN. Unchanged user-running V83 FAS1 RX_ONLY/HARD_DENY; EXP388 RUNNING / PARTIAL; B11D first-start OPEN.

## OBSERVED FACTS
- Exact private Service-28 input archive SHA256: `0a4769327706133c034e2f8393ddb1349d725940b8745b183c2c6526e7ae69db`.
- Five user-attached historical local XTR raw captures rechecked: 19 exact CRC-valid `0x0F FC16 0x0864/count4` frames and all report `0x0867=22` decimal (2+4+1+0+12 per capture), zero bad candidates. **Historical only, not contemporary session evidence.**
- Original Connect 2.0.18 CM930 profile directory `2.3.0-2.4.1` and 2.1.105 `2.3.0-2.4.3`. The documented original firmware version formula converts raw decimal 22 to `0.2.2`, which falls in neither directory. Decimal 242 would mean `2.4.2`, eligible for the later directory only, **if** an independently verified current XTR session observed it. An earlier cross-model roadmap reports XTR 242; this is not corroborated by the 19 attached raw frames; provenance/epoch unresolved.
- Historical XTR `0x0864/count4` and firmware nominal W4 `0x0864/count12` are different register geometries: do not infer full operational group completion from the former.
- Inherited build artifact gap: **`v5dcm83_shared_rx_supervisor.hpp`** is referenced by both verified V83 source YAML and staged S28 YAML but is absent from the uploaded private S28 ZIP. This was not introduced by S29. It blocks claims of a self-contained ESPHome compile.

## SOURCE CHANGE (private, existing merged V5 gateway)
Added a pure version/provenance policy `v5_native_service29_version_provenance.hpp` and changed the staged existing profile-install method to require contemporaneous same-epoch, reviewed XTR source, exact observed page/count, CRC, stability, exact raw-version equality and the original 2.0.18/2.1.105 firmware version range in addition to Service-28's exact 31/33 reference group list. Reject historical, stale, unsupported version 22, dataset mismatch and numeric/hex or modulo alias errors. No automatic profile selection, no new UART/DE actor, no physical TX permission; assertions supplied by caller remain non-cryptographic and cannot prove hardware ownership. Added standalone offline historical-capture CRC verifier, host regression and YAML checks; unchanged verified V83 source.

## ACTUALLY EXECUTED
- 32/32 strict C++17 host executables PASS, including two synthetic FakeIo TX builds that emit **no bus TX**.
- 3/3 targeted ASan+UBSan test executables PASS.
- 19 CRC-valid historical exact frames, all raw22.
- PyYAML/static checks PASS: 24/24 original top-level blocks, 197/197 existing HA identities, all substitutions defined, S28 UART/interval AST hashes unchanged, no new physical write/DE-enable paths. The inherited missing included header is separately identified.
- **ESPHome compilation NOT RUN; firmware flash NOT RUN; physical XTR TX NOT RUN.**

**PRIVATE ZIP SHA256:** `d2c26270b921f9954387aa037d55d789c6ded5efb3624eb0a248c9bd7b87a40b`. Keep source private, no protected handshake material in this report.

## STRONG CONCLUSIONS / HYPOTHESES / UNKNOWNS
Original Connect profile-selection is version-specific, so universal 31/33 automatic selection is disallowed. The 19 available raw22 XTR frames are not evidence of a currently valid Connect CM930 session. Whether a current locally observed XTR version can source-bind the later firmware dataset, actual physical slave/slot ownership and true controller acceptance remain UNKNOWN. No semantic write acceptance claimed.

## NEXT ACTION
Recover the exact verified baseline missing supervisor header and obtain contemporaneous local XTR version/source evidence (passive first), with B11D root cause still investigated. Do not flash the private S29 candidate as-is. Any actual TX later requires its own user-initiated scoped experiment with role/slot, CRC/abort and rollback; EXP388 remains PARTIAL.
