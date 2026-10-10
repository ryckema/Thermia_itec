# LIVE-B11D-RX-VALIDATION-01 — XTR M passive evidence (2026-10-10)

**Status: RUNNING / PARTIAL** (planned 20–30 min duration and fault-onset evidence not met).
**Bounded observations: COMPLETE / NEGATIVE** for independent B11D raw-parser continuity; **COMPLETE / POSITIVE** for continued V5 and V5-delimited original-portable RX.
This is a review of a user-supplied live ESPHome log, not a new firmware flash, active ACK, write, or controller reset.

## Hypothesis, baseline, controlled change
- **Hypothesis:** independent raw UART framing continues producing byte-identical messages throughout long passive capture without integrity fault or TX.
- **Baseline:** earlier Bridge11D-A FIX1 local bounded test 7,159/7,159 matched raw-vs-V5 frames with zero fault; cannot extrapolate past that window.
- **Controlled change:** none; observed existing installation and preserved working production functionality. Source: user log Pasted text(20261010-130851).txt, 15:04:31.683–15:08:43.810 (~4m12s), not the planned 20–30m run.

## Observed facts, local XTR M
- V5 Valid Frame Count 151,615 → 153,659: +2,044. V5 reports bad geometry=0, unknown=0, resync=0, drops=0, TX=0; buffer drops and boundary failures remain zero.
- Independent B11D rawFrames/portableFrames/comparedV5 stay at **56,714**. B11D raw callbacks 458,145 → 463,522 (+5,377); raw received bytes 3,259,015 → 3,297,444 (+38,429); batches 23,178 → 23,178.
- B11D retains incomplete=1, fault=1, noise=0, ambiguous=0, overflow=0, nativeFault=0/0/0, maxPending=177, idleMs=25. Text fault **RAW_NO_VALID_CRC_CANDIDATE_AT_IDLE**; RX status **INDEPENDENT_RAW_FAULT / CAPTURE_ONLY / NO_TX**.
- B11D countDiff=0 and byteDiff=0 remain frozen after the fault: **not** proof of ongoing parity.
- B11C original portable using **V5 frame boundaries**: 151,818 → 153,604 (+1,786); countDiff=0, byteDiff=0, boundaryFaults=0, resync=0, drops=0, internal fault=0, ioTxAttempts=0 in observed health summaries. This is **not** independent UART framing.
- TX attempt/UART write/physical delivery counters remain zero; DE=0; owner=UNKNOWN and controller epoch UNKNOWN. No observed FC23/qualified owner progression in these bounded log excerpts.
- The first B11D fault predates the supplied interval. **Neither its trigger nor first-fault timestamp can be extracted here.**

## Conclusions and uncertainty
**Strong conclusions:** A sticky fail-closed raw-parser fault prevents B11D from committing more independently framed ADUs despite arriving callbacks and bytes; the legacy V5 path continues. Do not confuse host-simulated 25-ms callback-idle timing with measured Modbus electrical RTU t3.5.
**Hypotheses only:** software idle boundary, UART fragmentation, incomplete/noisy buffer, scheduling delay; cause NOT determined.
**Unknown:** earliest pre-fault bytes and callback timing, ESP loop/heap at that instant, physical controller power epoch, pending native owner. Automatic TX/ACK/write remains DENY.

## Test criteria, abort and recovery
- **Positive V5 criteria:** continued good frames and no V5 drops/resync or TX: MET for supplied window.
- **Independent raw continuation:** raw frame counter progresses without faults and maintains live byte parity: NOT MET.
- **Duration criterion:** 20–30 minutes: NOT MET.
- **Abort:** new V5 resync/buffer drop, physical TX or DE, heat-pump/Home Assistant degradation. Remain capture-only.
- **Next evidence:** obtain the first actual B11D fault transition with 20–30 seconds preceding log. If unavailable, a separately reviewed **ESP-only** RX-only restart capture may be prepared; no Thermia power reset or active bus response, and no automatic restart/recovery added.
- **No new YAML or physical test has been carried out by this GitHub documentation update.** Any future ESP-only restart is PREPARED / NOT RUN.

## Offline work reconciled (cross-model HOST evidence; not local session proof)
- Native metadata observer 06: 4,809 native cross-model events, host-only.
- Bridge07: original C++ with synthetic valid-frame projections; 25,031 true raw frames through host testdouble only at that stage.
- Bridge08: 25,031 genuine cross-model raw ADUs through pinned **original C++** plus metadata observer; GCC/Clang/ASan/UBSan PASS. Private CI: https://github.com/ryckema/Thermia_Connect_Firmware/actions/runs/38051370371
- Bridge09: those genuine raw frames in **three synthetic callback fragmentation/coalescing patterns**, 75,093 ADU occurrences per compiler build, original portable bridge+observer, GCC/Clang/sanitizers PASS. Private CI: https://github.com/ryckema/Thermia_Connect_Firmware/actions/runs/38053859261
- None establishes electrical ESP32 RTU timing, controller-owner status, physical epoch or write authorization. R5 FIX2 historical active status and R6 CONCEPT/NOT RUN remain unchanged.
