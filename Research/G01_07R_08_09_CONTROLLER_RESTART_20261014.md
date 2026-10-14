# G01-07R / G01-08 / G01-09 — XTR M restart evidence reconciliation (2026-10-14)

Status: G01-07R COMPLETE/POSITIVE historical chronology with independent electrical witness INCONCLUSIVE; G01-08 COMPLETE/POSITIVE bounded OFFLINE candidate tests, autonomous physical boot INCONCLUSIVE; **G01-09 COMPLETE/POSITIVE for VIDEO-ANCHORED / INTERVENTION_ANCHORED controller-power-cycle observation**, not a direct measurement of the main controller supply rail.

This report was assembled from user-supplied XTR ESPHome logs and the user-supplied video in this research conversation. **No new native TX, firmware flash, controller restart beyond the user-performed recorded event, write, network experiment or electrical measurement** was executed for this report. Video and raw logs are private conversation artefacts and are not committed. Native 0x0F TX remains HARD DENY.

## G01-07R historical replay
- Six local XTR candidate episodes: EXP293 (8.692 s gap, 1.302 s to FC23), EXP294 (12.105 s, 1.169 s), EXP295 (10.988 s, 1.231 s), EXP296 (13.471 s, 1.048 s, one resync), EXP297 (14.796 s, 1.283 s), EXP344 (>=5.204 s reported at detector, 1.284 s to FC23). The EXP344 gap number is a detected lower bound, NOT complete silence duration.
- CONTINUOUS ESP uptime was supported by periodic samples during the six candidate transitions. EXP296 must not be cleanly approved due to a parser-resync.
- The historical 32/32 configuration progress followed an **active** response path and must not be used as a passive controller-boot proof. Software timestamp differences are not electrical RTU EOF or response-slot measurements.
- Genuine Eco5 cross-model capture excluded from local XTR proof.

## G01-08 independent offline candidate checks
- Host-only, non-deployed, fail-closed detector: five clean historical XTR CANDIDATE and EXP296 HOLD.
- Eight fixed negative fixtures; 2,048 mutated negative streams, no false CANDIDATE in these tests; 18 historical ESP uptime-reset intervals are not automatically controller restarts.
- Long RX-only TX-16 retained comparison (97 min) had no FC23 candidate; status A80E/A80F is not unique boot evidence.
- G01-04 **original seven false-physical-epoch fixtures were not available for exact re-execution**. The old projector was DISPROVEN; new tests are not a substitute for literal regression re-run.
- Every host-only candidate leaves PHYSICAL_EPOCH=UNVERIFIED and TX_AUTHORIZED=false.

## G01-09 user-video anchored live XTR observation
**Hypothesis:** user-performed switch OFF/ON plus visible display power-off/restart and uninterrupted independent RX-only ESP capture establish an externally documented controller power intervention and a related native start sequence, without pretending to measure electrical power at the main controller.

**Baseline:** six historic XTR start episodes (G01-07R); G01-08 offline detector; existing independently powered Waveshare ESP32-S3 RX-only B6, logger and HA operational. User confirmed two accessible disconnect methods (indoor-unit breaker, internal switchable breaker), both make the Thermia display fully go dark. The exact switched controller supply rail has not been independently probed.

**Controlled intervention:** the user operated a normal Thermia power switch once and filmed the display/switch; ESPHome RX-only log continued. No experimental ESP native response was enabled.

**Source integrity:** two user-uploaded identical 4,660-line logs named `Pasted text(20261014-134304).txt` and `...(1).txt` have SHA-256 `a66541b2c8d91661863c6a315003ef26eb4ca3d8960e324479ff2a43cd8acb2e`. Original video `IMG_0079.mp4` is 23.567 s, SHA-256 `c6ca2d3e443efb367fbf8aba156b9d25769133f8717486446744120ca0b83a1f`. The user explicitly confirms video and log depict the same power-cycle event. Their clock alignment is user-associated/correlated, not an independently synchronized power-rail trace.

**Observed in the user video:** two switch-like audible clicks around 5.3 and 13.3 seconds; display visibly goes dark and resumes. These observations establish the user's documented operation, not a measured main-controller supply voltage.

**Observed in current local XTR log:**
- At 15:41:15.736 `[R6-P24] CALLBACK_GAP ms=11944 ... controllerEpoch=UNKNOWN NO_TX`.
- At 15:41:15.749 `FIRST_CRC_RETURN slave=1E callbackGap=11944 EPOCH_ID_UNKNOWN NO_TX`.
- At 15:41:16.460 `S02_AFTER_RETURN A80E=0000 A80F=0005 coldPattern=1 EVENT_ONLY EPOCH_ID_UNKNOWN NO_TX`.
- By 15:41:17.021 one FC23 request had been counted, then 24 cumulative FC23 requests by 15:42:55.315. No locally transmitted native reply and no new 32/32 bootstrap (`P=0/32`).
- ESPHome API logging, monotonic internal counts and ESP boot identity continue across the capture without observed ESP reboot/reconnection; **there are no contemporaneous separately published ESP Uptime sensor samples across the transition**, so the precise uptime proof is bounded to observed continuity and counters.
- Reported B11D raw-vs-portable RX comparison stayed matched, with no reported parser resync/drop/geometry failure in this window. Software TX calls/attempts 0 and DE software readback LOW; no independent electrical DE proof.
- TX-16 correctly entered a `HOLD` / `RETAINED_EPOCH_UNPROVEN` state at first FC23 rather than authorizing TX. Repeated FC23 is a retry series, **not** 24 physical controller restarts.

**Positive criteria:** recognizable video power operation with display off/on, corresponding sustained bus silence/return, early cold-pattern controller status, FC23 retry series, uninterrupted healthy software observer, TX=0. Achieved within documentary/video and software-log evidence.

**Negative / abort criteria:** missing/corrupt capture, misaligned unrelated video, ESP reboot/OTA during event, RX integrity degradation, unverified electrical/wiring claims or any native TX/DE assertion. If so classify INCONCLUSIVE/HOLD, retain RX-only. No new active test authorized. Recovery of any future test is the known-good RX-only firmware and normal controller startup only as required by vendor procedure.

**Verdict:** `G01-09 COMPLETE / POSITIVE — INTERVENTION_ANCHORED (VIDEO)`. G01 as **manual, event-bounded investigation** can be considered successful; this precise recorded controller protocol epoch is supported by a physically documented switch intervention. However `EXTERNAL_BOOT_WITNESSED` in the strict **direct main-controller-power / validated boot indicator** meaning has NOT been obtained. Neither video, FC23, A80F, cold-pattern, 32/32 nor software uptime is an independently measured main-controller rail. **Do not automatically promote this to proof for any later epoch, firmware boot, live TX slot, or autonomous native TX permission.**

## Gate relation / next
- G01: manual controller restart/video correlation **POSITIVE**; strict independently measured controller supply epoch **OPEN**, and future unattended epochs cannot inherit an earlier video.
- G02 exclusive actual physical responder/work owner **OPEN**; G03 physical EOF **OPEN**; G04 exclusive reply slot **OPEN**; G05 FIFO/DE electrical release **PARTIAL/HOST-ONLY**; G06 brownout/reset DE-low **OPEN**.
- **Native 0x0F FC23/FC16/0708 responses and semantic writes HARD DENY.**
- Next G02: review existing offline G02-01..07 source-specific artefacts; verify reproducible tests and reconcile status, not a new active-response experiment.

The older dated notes remain true for their original review dates; this 2026-10-14 addendum supersedes only claims that no user-video-anchored local XTR run exists.
