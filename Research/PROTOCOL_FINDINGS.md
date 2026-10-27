## 2026-10-27 — C5CZ post-CURRENT native upkeep source prepared

OBSERVED FACTS: In user live C5CY ESP-only OTA, retained native transport qualified M6=4, and the existing automatic read-only CURRENT request received all four controller H/D/C/M pages, mask0F and M6=5 with no HA settings write. Immediately afterward repeated ordinary controller FC16 and FC03 went unacknowledged although CRC and RX counters stayed clean. These are separate findings: C5CY automatic initial join and 4/4 COMPLETE / POSITIVE for this one live run; continuous upkeep still incomplete.

SOURCE ROOT CAUSE: The final CURRENT mode receipt was incorrectly treated as a fresh setup/export-phase observation, invalidating the retained-response scope. Independently the reused first FC03 qualifier incorrectly required the earlier unproven session state rather than allowing the same physically qualified native epoch after M6=4/5. An in-progress read-only controller refresh state must remain distinct from any real HA pending parameter write.

C5CZ is one complete private C5CY-derived firmware package, SHA256 36ac7d1079fb05e2dcbe99d6ccefbfd2c27bae9dbe1461403421c38c8fc5e2af, SOURCE / OFFLINE TESTED, PREPARED / NOT RUN. It gates the final CURRENT page classification on the actually transmitted same-epoch 4-page read, consolidates guarded ordinary FC16/FC03 upkeep through the same native session state, and removes one provably dead legacy single-page selector plus obsolete header/comments. It does not add protocol frames, an UART owner or HA writes. Maintains verified cold FC23 path, TX CRC/peer/DE/ABORT, all 663 globals, all HA entities and 572 IDs. YAML parser/ID/entity-parity/UART-writer count/ZIP integrity PASS. Not ESPHome target compiled/flashed or XTR live tested.

CURRENT MILESTONE: sustained native runtime responses following successful automatic retained join and cache freshness.
DELIVERABLE: complete private C5CZ ZIP with patch, manifest, activation, expected logs, ABORT/rollback.
REAL BLOCKER: continuing controller-offered FC16/FC03 after M6=5 remains unverified with C5CZ on hardware.
ONE NEXT ACTION: user target-compile then deliberately initiate one bounded ESP-only OTA with export experiment disabled; inspect post-M6=5 physical ordinary ACKs and served 0708, STOP/RX ONLY and revert on anomaly. HA parameter writes ON HOLD.

---

## 2026-10-27 — C5CY focused OEM comparison of first-0884 → INFO → M6 → CURRENT (SOURCE REVIEW ONLY)

OBSERVED FACTS / OEM SOURCE: Genuine Connect 2.1.105 modbus_server15.py uses Modbus slave FC16 handling independently of application-level semantic acceptance. Genuine 2026-10-03 DCM trace has 0532/18 before first 0708 and ordinary repeated 0884/60 FC16 with FC16 ACK after runtime polling. OEM 930 modbus-flags.json W2=0x4000, W3=0x8000 and W4=0x000B select the five same INFO groups, but its 1803 bit15 nominal *register mapping span* for 0532 is **20 addresses**, while actual genuine DCM wire FC16 frame is **0532/18**; distinguish source range from physical wire geometry. C5CY intentionally matches the observed 18-register FC16; no fabricated 20-register ACK shape. First 0884 after ESP-only OTA is supported by user's C5CW XTR LIVE log, not separately by OEM cold-start capture.

C5CY SOURCE TRACE: After first physical 0884/60 ACK, current-epoch token c5cg_first_0884_ack_epoch authorizes only existing next controller-0708 first INFO request; all five INFO pages were XTR LIVE ACKed in C5CW. On later exact 0884/60, C5CY outer branch, inner c5ce_retained_0884 boolean and M6 event4 retained_transport predicate all accept that same existing physically established 0884-first token or older c5aw first token. Second 0884 credit occurs after sole guarded S92 TX, then queued M6 event4 checks active/epoch, parser/peer integrity, real FC16+0708 counters, INFO>=03 and physical followup epoch; only then M6=4 and independent accepted transport epoch. OEM application semantic owner is NOT proven by these transport events. C5CU automatic CURRENT arm still additionally requires observed version242 profile and clean qualified epoch and waits for future real 0708; fresh CURRENT requires physical H/D/C/M 4/4. New OEM review found no further demonstrable predicate mismatch within this path, but offline reachability is NOT XTR live or target compile. ZIP YAML SHA256 b61d82edc9832d1c61fba5ff6358a58f1baa7bc99efd9af5fe019933d4cb3f32 verified; ZIP CRC passed; no firmware changed or physical TX performed in this review. C5CX SUPERSEDED / NOT RUN; C5CY PREPARED / NOT RUN. HA parameter writes ON HOLD.

CURRENT MILESTONE: reliable native retained join and automatic per-session CURRENT 4/4 while preserving locally verified cold path.
DELIVERABLE: C5CY OEM/source peer-review complete; unchanged private firmware ZIP.
REAL BLOCKER: C5CY 0884-followup/M6=4/auto CURRENT 4/4 not yet compiled and LIVE validated on XTR.
ONE NEXT ACTION: if user chooses, target compile unchanged C5CY and user-initiate one bounded ESP-only OTA with experimental EXPORT TX false, S92 STOP/RX ONLY and C5BN/C5CT rollback ready.

---

