## 2026-10-27 — C5DA ESP-only OTA LIVE blocked by legacy 085F response guard, alarm origin unproven

OBSERVED FACTS: User supplied C5DA XTR live log, running build MAIN03-C5DA after esphome.ota without controller restart. Automatic stage40 RETAINED_RUNTIME joined and ACKed eight genuine ordinary FC16 pages; first FC03 0708 INFO-FIRST physically replied, INFO mask reached 1F. Thereafter 085F/5 zero-payload controller FC16 repeated ~2 s, but pre-existing EXP419_085F_NO_CONTEXT intercepted each with NO_ACK. No further FC03 service, M6 remained 2, cache 0/4, session expired after 60.086s to M6=7 RX-only DE LOW, physicalTX=9 (8 FC16 ACKs + 1 FC03), CRC disagreements, parser resync, RX drops, and peer evidence all zero; HA setting writes absent. C5DA experiment COMPLETE / NEGATIVE for full retained join. C5CZ post-M6=5 upkeep remains not exercised here. Real heat pump alarm reportedly shown to user but exact local HMI alarm text/code not supplied.

SOURCE ROOT CAUSE: C5DA's passive 085F phase reclassification is not the same as physical alarm reply. The older EXP419_085F_NO_CONTEXT condition accepts only legacy write_tx_used/recovery/hot-rejoin/resume flags, not ordinary physically ACKed C5CP retained context after first FC03/INFO, so 085F is left unacknowledged. The 085F payload zero does not prove that the controller's user-interface alarm has cleared or diagnose its origin; no automatic alarm reset or fabricated owner. OEM Connect server handles FC16 transport independently from application acceptance and excludes alarm register from internal handshake acceptance. No new firmware or bus TX performed by assistant.

SAFETY DECISION: Do not flash further experimental firmware, force TX or reboot controller merely to chase session while physical device alarm type is unknown. Keep S92 STOP/RX ONLY and HA settings writes HOLD. Read actual Thermia panel alarm message/history before local user-manual alarm acknowledgement; persistent/safety alarm -> installer. Follow the iTec XTR user manual, which describes alarm display and acknowledgment through operating-mode OFF then previous mode where applicable; avoid unattended OFF in freezing conditions.

CURRENT MILESTONE: one native retained session + cache with continuous FC16/FC03 maintenance.
DELIVERABLE: user C5DA LIVE result + source-proven old EXP419 response blocker; no new firmware.
REAL BLOCKER: repeated 085F no-ACK despite valid preceding native responses, plus unknown actual controller alarm indication.
ONE NEXT ACTION: user record the exact alarm text/code shown on the Thermia controller; then distinguish alarm remediation from a single guarded native responder correction without repeated blind OTA.

---

## 2026-10-27 — C5CZ live retained 085F phase regression; C5DA SOURCE prepared

OBSERVED FACTS: User XTR ESP-only OTA ran C5CZ at 01:08:20; automatic stage40 retained native entry. Physical controller FC16 07E4/17 ACKed, then first 085F/5 ALARM ACKed. Following controller 0708/6 and 07D0/19 were denied/repeated, M6 remained2, H/D/C/M 0/4 and after 60.034s timed out to M67 RX-only DE LOW. Physical TX2, CRC_DIFF/resync/RXdrops/peer=0; no parameter writes. C5CZ COMPLETE / NEGATIVE for that join; its post-M6=5 upkeep correction was not reached and stays unverified.

SOURCE CAUSE: The passive V5 phase switch still marked 085F/5 as export/setup; it incremented c5bx_setup_fc16_seen before the 085F native ACK, diverged from same-epoch c5cl_setup_entry_baseline and therefore c5cp_retained_transport_scope rejected later 0708/07D0. Original Connect 2.1.105 modbus_server15.py explicitly excludes ALARM_START_ADDRESS from its handshake-acceptance criterion; its FC16 transport handler does not imply XTR session owner. 085F is an alarm role not a new export phase merely because it follows an ACKed retained runtime page.

C5DA complete PRIVATE YAML from C5CZ, SHA256 5bb0a467ed141de7edfc16bc2157edfa8140aee6ad8821bf77c50d63d45294f7. ONE code change: if genuine 085F/5 is observed in active same-epoch retained native session AFTER a physically ACKed ordinary FC16 first page, do not vote a new export phase. Without such physical evidence, original cold/setup classification remains; all ACK shapes, FC23, V5/CRC, peer/collision, one UART/DE owner, M6/one-shot CURRENT, HA parameter writes HOLD unchanged. Offline YAML/IDs/globals/entities/UART-TX sites/ZIP CRC PASS; not target compiled/flashed/LIVE. C5DA PREPARED / NOT RUN.

CURRENT MILESTONE: native cold/retained join, 4/4 CURRENT, continuing guarded FC16/FC03 upkeep.
DELIVERABLE: private full C5DA firmware zip SOURCE / OFFLINE TESTED; C5CZ negative live trace documented.
REAL BLOCKER: C5DA retained 085F phase transition, subsequent M6=4 and post-M6=5 uninterrupted service unverified.
ONE NEXT ACTION: user target-compile C5DA then ONE optional user-initiated bounded ESP-only OTA, existing S92 STOP/RX ONLY and C5CY/C5BN rollback available, export experimental TX false.
---

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

