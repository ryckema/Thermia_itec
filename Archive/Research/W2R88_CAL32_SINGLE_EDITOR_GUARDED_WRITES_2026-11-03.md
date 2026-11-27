# W2R88 — unified calendar editor; guarded F2/F3/F4 write scope

Status: PREPARED / NOT RUN. Evidence: SOURCE / OFFLINE TESTED only.

## Baseline
XTR M 3N/controller 2.4.2 actually LIVE / LOCALLY VERIFIED MAIN04-W2R86 for Hot Water F1 Program4 and Program5 five-field writes, genuine controller-origin FC16 per field and fresh F1 final persistence. W2R87 was rejected by ESPHome switch.template update_interval and W2R87F1 was corrected, not yet shown flashed.

## One integrated implementation
One visible 32-option selector: Hot Water, EVU, Silent Mode, Temperature Reduction, eight programs each. One set of 4 time numbers and 7 day switches; shared Read, Discard, Apply, new-domain ARM and Stop controls. Legacy F1/F3 UI components kept as internal to preserve IDs and callbacks. Shared source uses owned original F1/CAL12 native reader and cached 33-word pages. Register bases F1=0x055A, F2=0x05BC, F3=0x061E, F4=0x0680; 12 words per slot, offsets startMinute1,startHour2,stopMinute6,stopHour7,days11. First record of later groups crosses an earlier 33-word page. Stale F1 auto reread retained; shared Read button added. F1 after Apply rebases only when newer authoritative F1 3/3 exactly matches staged values.

Physical setting TX for existing programmed WEEKLY (mode=1) F2/F3/F4 records is now integrated into the existing sole native S92/OEMW descriptor23 owner, with explicit user Arm New-Domain Write (45s) plus one Apply (the ARM itself NO_TX); max five separate 33-word pages and five-minute batch, no automatic retry. Same bus-idle, CRC, peer/collision, owner epoch, source age, exact record/field/page/target/full 33-word source guard and DE owner as verified F1. Every field requires genuine controller-origin exact FC16, then fresh entire owned CAL12 readback before semantic success. Empty/date slots, zero weekdays, create/delete remain NO_TX. Physical F2/F3/F4 semantic acceptance is UNKNOWN until LIVE experiment; F1 previous proven behavior retained. Stop cancels remaining fields, S92 ABORT revokes bus owner; neither reverses already-saved controller settings.

## Offline validation and deliverable
Strict duplicate-key YAML parser: PASS; 1230 unique IDs, all 1182 W2R87F1 IDs preserved; exactly one visible 32-slot calendar selector and one visible set of day/time controls; no unsupported switch.template update_interval. 38 modified/new C++ lambdas passed GCC C++17 syntax-only harness, NOT ESPHome target compile. ZIP file CRC, per-file SHA256 and exact W2R86 rollback integrity PASS. One complete private package Thermia_MAIN04_W2R88_CAL32_WRITE_PRIVATE.zip with full YAML, original W2R86 live rollback, Dutch build/test/ABORT guide, source diff and hashes. NOT TARGET COMPILED / FLASHED / LIVE.

## Next experiment — PREPARED / NOT RUN
After user flashes W2R88, require M6=5/CURRENT4/4/CRC0 and fresh selected Silent Mode Program1 (historically daily 22:00–23:59). Set only Start Minute 00 to 01, press new-domain ARM then shared Apply within 45 seconds. Expect exactly one descriptor23 S92 physical page0x05FF register0x061F, matching genuine controller FC16 and fresh CAL12 verification CAL32_BATCH_DONE exact=1 pages=1 count=1. On anomaly ABORT, do not repeat blindly, read controller state and revert deliberately via panel or independent user Apply. Successful first word enables later combined-field experiment. EVU/Temperature Reduction and true deletion remain unproven.

CURRENT MILESTONE: shared 32-slot calendar source and guarded new-domain writes.
DELIVERABLE: complete W2R88 private firmware ZIP.
REAL BLOCKER: none for bounded trial preparation; semantic controller acceptance for F2/F3/F4 remains OPEN.
ONE NEXT ACTION: user compiles/flashes W2R88 and runs one explicitly armed F3 P1 Start Minute +1 experiment.