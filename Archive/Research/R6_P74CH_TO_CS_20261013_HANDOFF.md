# R6-P74CH–CS — additive live/offline handoff (2026-10-13)

**Purpose:** bridge the gap between previous canonical BW–CD overlays and the later user-confirmed CH→CO installations plus offline CI–CM / CP / CQ–CS analyses. This is a **new addendum**, never a replacement of historical experiments. All native bus TX **HARD DENY** throughout this recent track. No XTR fresh Online/DCM session, physical owner, controller epoch, sender, wire EOF or response slot was proven.

## User-live RX-only experiments

- **R6-P74CH — COMPLETE / POSITIVE (bounded RX-only soak).** User tested original CH on XTR M. The long log `thermia-exp86-20261013-104747.log` spans 10:47:49.706–11:05:41.458 (17m51.752s), 26,871 lines, CG retained events ~467→1929 and no sampled parser resync/drop, B11C/B11D delta or software TX. CH has **one** native callback and one CG/P74AT shared reducer via P74L; no physical owner inferred.
- **R6-P74CN — COMPLETE / POSITIVE for user-live RX-only duration; metadata-shape semantics PARTIAL.** The user explicitly confirmed **CN was compiled, flashed and running**. The user long log `thermia-exp86-20261013-122359.log` shows a retained RX-only >15 minute firmware uptime with native page counts progressing, no sampled resync/drop/frame-difference/TX, and four API `Buffer full, ping queued` warnings; no fresh FC23-response or 32-page bootstrap. The passive CN shape tap has no periodic HA counters; its integration alone was not proof of all shape classes.
- **R6-P74CO — COMPLETE / POSITIVE for *on-demand diagnostics only*.** User installed CO and exercised existing HA Configuration button `R6 P74L DUMP Recent Native Events (NO TX)`. User log `Pasted text(20261013-104747).txt`, 12:45:02–12:47:39, shows `[R6-P74CO] CN_SHAPES accepted=214 rejected=0 last_seq=214 FC16_REQ=214 FC16_ACK_SHAPE=0 FC23_REQ=0 FC23_RSP_SHAPE=0 source_latched=0 last_source_valid=1 last_ambiguous=0 ... TX=DENY` at ~12:47:28. This establishes on-device retained shape-counter instrumentation, not fresh response recognition. CO log also has exactly one early V5 parser resync (~first 10 seconds ESP uptime), 0 drops, 0 B11C/B11D byte/frame mismatches, zero reported software TX/UART write calls, passive observer recovered after ~30 sec and historical P5 fault latch persisted. Five B13 `ABORT_NO_TX` messages were safety handling, **not actual output**. Cause of resync unknown; cannot call this a firmware regression.

## Host-only sequence and limits

- **CI COMPLETE/POSITIVE offline:** sample-only CH retained deltas `04A6/13` 993 vs `085F/5` 497 (~2:1); logger metadata is not raw native capture.
- **CJ COMPLETE/POSITIVE offline:** seven genuine previously captured cross-model logs, 25,031 CRC-good original ADUs. Seven Eco5 windows: six record FC23-response shape and broad 32/32 page+short-ACK shapes, one has 41 FC23 requests and no recorded response (collaborator-reported gateway absent). ATEC `03E8/13` differs from Eco5 `03E8/14`; no XTR proof.
- **CK COMPLETE/POSITIVE host-only:** passive state/shape classifier, 8 capture contexts and 3,726 converted genuine metadata events; owner/epoch/sender/physical EOF/slot/TX remain false.
- **CL COMPLETE/POSITIVE offline feasibility but on-device direct CK-from-P74L NO-GO:** original P74L Event lacks independent `fc16_ack` and `fc23_response` type flags even though V5 Frame itself recognizes their shapes. No extra source reader/reducer permitted.
- **CM COMPLETE/POSITIVE host-only:** shared explicit framevorm metadata contract, 3,726 original cross-model shape events / eight contexts, 88/88 CK parity fields, 7,496 assertions and sanitizer checks. No ESPHome compile then.
- **CN OFFLINE prepared and subsequently USER-LIVE:** one extra passive tap in existing V5 frame callback, production HA and TX safety preserved; native CK state-machine still NOT installed.
- **CO OFFLINE prepared and subsequently USER-LIVE:** one additional diagnostic line on existing P74L dump button; no new entity/periodic reporting/native TX.
- **CP offline analysis:** the one CO resync precedes the user dump. 7/7 host-only comparison tests reportedly pass; CH/CN captured windows lack comparable cold-boot coverage. **Resync cause INCONCLUSIVE**, P5 historical fault latch not silently cleared. Do not claim cold-boot parity with CH/CN.
- **CQ COMPLETE/POSITIVE offline window contrast:** for Eco5 contexts 3205 and 5457, 120-second response-relative ACK-shape prefixes 10/32 and 12/32; broad context windows 32/32. Does **not** prove original P74AR used 120 seconds.
- **CR COMPLETE/NEGATIVE:** retained `04A6/13` and `085F/5` plus FC23 request shape do not suffice for a response/ownership (present in the 41-unresponded-request control).
- **CS COMPLETE/POSITIVE for chronology of CO:** CO dump occurs **after** early resync; exact cause of resync INCONCLUSIVE. Host-only 20 invariant tests of CQ–CS pass in original local report.

See `R6_P74CT_TO_CW_20261013.md` for the next four tested offline experiments. The latest user-tested XTR firmware is **CO RX-only** (the current physical runtime beyond supplied logs is not independently inspected); preserve known-good CN as fallback and do not ask for another flash without a new hypothesis.

## Long-standing historical outcomes retained

- EXP355/386/387: historical guarded V4.1 bounded successes, **not** current V5 TX authorization.
- EXP388: RUNNING / PARTIAL (untested cancellation branches).
- EXP425: COMPLETE / NEGATIVE for expected ordered `0683` tail after the single `0662` ACK; not overridden by other-model ACK observations.
- G01–G04 and G06 OPEN; G05 HOST ONLY / PARTIAL. No genuine Online/DCM module available for new capture; no room-sensor disconnection test.

## Notes on source quality and artifacts

Original source priorities remain direct XTR experiment logs and exact YAML > genuine cross-model raw captures > firmware semantics > interpretation. Host `millis()` is not RTU physical EOF. CRC-/shape-good ACK proves neither original sender nor acceptance. Large offline ZIPs generated locally are **not** GitHub-published; never publish sensitive native emulation code, private algorithms, recovered security details, keys or mailbox tooling.

**Next:** prioritize passive/host-only categorization of previously classified OTHER frames using genuine captured provenance and firmware-derived symbols, and reconcile every next experimental material change in the three canonicals. No active native response, broad scan or write until separately and explicitly authorized with safety gates.
