# V5DCM19 FIX1 — actual local XTR M RX-only log result (2026-10-18)

**Experiment status: COMPLETE / POSITIVE for explicitly scoped V5DCM19 RX-only diagnostic integration.** Native DCM session acceptance remains OPEN/UNKNOWN. G01–G06 accepted residual risks not reopened.

**Hypothesis:** Existing V5DCM1/2 session/challenge observers can be joined into one 30-second diagnostic layer without interfering with known-good HA production functionality, consuming extra UART or introducing native TX.

**Baseline:** user-confirmed physically flashed V5DCM19 FIX1 after correction of duplicate `interval:` top-level key, prior deployed V5DCM2 FIX1 RX-only; historical Write V4.1 EXP386/387 native positive is an *independent historical baseline*, not reproduced by this passive run.

**Controlled change:** FIX1 integrates exactly one logging interval into existing production schedule, three `[V5DCM19]` lines; no active TX, no new parser, no extra UART consumer, `HARD_DENY` retained.

**User-supplied actual result:** file `Pasted text(20261017-232227).txt`, 4,643 lines, ESPHome logs from 01:19:09 to 01:22:18 (about 189 seconds). Six distinct `[V5DCM19] NATIVE_OBSERVE`, six `SERVICE_OBSERVE`, six `PROVENANCE` lines at 30-second spacing, all printing. The latest integrated service counter at 01:22:03: `fc16Seen=254`, `mailboxPoll=0`, `runtimePages=0`, `fc16AckShape=0`. NATIVE shadow no challenge or reply; `cfg=1/32` strict contiguous count; `outOfOrder` increments with streaming unrelated pages; not an actual 1-page delivery cap. Repeated service 085F/5 and 03E8/14 observed with no approved same-epoch native session. Epoch, owner, slot, acceptance and Online icon remain UNKNOWN/UNPROVEN. No actual DCM module is present.

**RX/parser state:** `[B11D-RX]` 1,564 raw frames = portable frames = V5 comparisons at final 01:22:04 check, countDiff=0 byteDiff=0 incomplete=0 ambiguous=0 overflow=0, nativeFault=0; `[B11C-PORTABLE]` V5=portable=1,566, countDiff=0 byteDiff=0 boundaryFaults=0; 11 previously accumulated parser resyncs remain stable, one historical RX integrity fault seen; observer recovery count=1 and later no fresh drops/resyncs in sampled health lines. Production room temperature, heating curve=36, DHW and heating values were published throughout. **Native executor** physical_attempts=0 throughout; by 01:22:12 `candidates=266 denied=266 physical_attempts=0`; `TX=HARD_DENY` seen each joined diagnostic.

**Positive criteria:** three joined logs repeat, existing HA sensors live, no new native TX, no new RX/parser regression in observed interval — MET. **Negative criteria:** any missing diagnostics, physical TX, production sensor failure, rising parser errors or false native acceptance — NOT OBSERVED within tested window. **Abort criteria:** unintended TX/new critical production fault — NOT TRIGGERED. **Recovery:** known-good deployed firmware retained; no change necessary for this experiment.

**Evidence categories:** OBSERVED local XTR: live RX-only integration and counters. STRONGLY SUPPORTED: V5 observer/parser joining did not impair existing telemetry in this ~3min window. HYPOTHESIS: native retained work classification requires active session context; not proven by repeated 085F alone. UNKNOWN: true controller acceptance, DC module icon, response ownership, runtime-ready and long-term stability.

**Next experiment:** V5DCM20 passive validation should build on this result; do not repeat V5DCM19 just because no genuine FC23 challenge occurred. Whether V5DCM20 requires distinct longer observation should be decided against roadmap, not automatically marked done. No TX nor new write targets introduced.
