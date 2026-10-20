# 2026-10-20 — ATEC/DHP-AQ third-party gateway V3, sanitized external source review

## 2026-10-20 source-framer comparison addendum (OFFLINE generic frames)

**A concrete V5 advantage was reproduced at SOURCE/HOST scope, NOT proven as an actual ATEC field failure.** The third-party V3 `Framer::poll` checks whether its entire buffered byte span has a valid CRC, otherwise accepts a valid suffix, emits once and clears the complete buffer. In `ThermiaSniffer::loop`, `now=micros()` is sampled once before draining all available UART bytes; consequently multiple already-buffered RTU ADUs can be pushed with the same timestamp without their original inter-frame gap. An offline standalone C++17 `Framer` test using two synthetic, independently CRC-valid 8-byte FC03 requests for generic slave addresses 0x02 and 0x04, both buffered before the poll, deterministically returned **one** emitted frame for **slave 0x04**, `ok=1`, `bad=1`, then **zero** frames on a later poll. The valid first frame was not delivered.

This is a **source-confirmed backlog/coalescing loss mode** in V3; there is no evidence it occurred on the original ATEC hardware or with any specific frequency. It contrasts with our original V49 generic StreamParser SOURCE/HOST replay in V5DCM80, where all **2687/2687** archived XTR ADUs were emitted for individual, fragmented and synthetic six-frame-coalesced delivery. The V5DCM80 *new* per-ADU router was host-only and V49 V43/V44B original TX actors still had a single-frame callback gate: do **not** present that host-only router as deployed live TX improvement. V83-FAS1 later provided **1028** byte/count-aligned B11D comparisons on the real XTR RX-only firmware, separately, not as this same two-frame coalescing test.

**Action:** preserve V5's multi-ADU parser semantics in any future native response architecture; continue comparing safety and real on-device reliability separately. No bus TX, XTR change, ATEC hardware, ESPHome compile, or private backend was used in this synthetic host check.


**Classification:** EXTERNAL / CROSS-MODEL SOURCE EVIDENCE ONLY; not a local XTR experiment, flash, TX or confirmation. Input: user-provided `V3.thermia-gateway-2026-10-20.tar`, SHA256 `e1dc7f316cd887e96e481e7e509570e9c1836b68ed271f47630b0d754f985abc`. The private original archive contains protected authentication/gateway material and MUST NOT be copied to GitHub. This note omits credentials, challenge response algorithms, private replies and command-mailbox implementation.

## Source-observed (not independently field-verified)

- Archive has an ESPHome ESP32-S3 C++ component, YAML, register-definition CSV, handoff and mailbox/field notes, and two host tests. The documents **claim** independent ATEC/DHP-AQ operation after replacing the former native Thermia Online gateway, plus repeatable display-visible setting changes. They also describe authentic original-gateway capture comparisons, but the supplied tar **does not include the raw original gateway capture logs or the seven historical replay tests** listed in the handoff.
- The implementation models a native gateway at **slave 0x0F** with a startup exchange, settings-block FC16 request/ACK servicing, FC03 reads, and a six-register data-package/control mailbox. This is a structural corroboration of our already independently verified vendor Connect2.1.105 CM930 source: settings base 0x03E8, data-package base 0x0708, operation base 0x07D0, alarm/status base 0x085F.
- External author reports two-stage repeated read-request signaling for a settings change, a field-observed bulk settings refresh without controller reboot, and a 20-Oct mailbox-bit-to-settings-group sweep for all 16 lower settings groups. These are **external reported observations only**; do not interpret as XTR-proven semantic acceptance, current version, command protocol or safe physical reply slot.
- Their firmware/profile note uses an external reported raw version field 2151=22 but resolves the external model/profile by other evidence. This does not fix the open XTR V86 mismatch: the genuine vendor source decoding of historical XTR raw22 as 0.2.2 does not match bundled profiles.
- Actual ATEC DHP-AQ devices differ from XTR topology (external material shows another outdoor-unit slave). Never port that mapping wholesale.

## Offline source checks performed for this review

- Reviewed the main C++ component, gateway responder, framing, configuration, register CSV and explanatory notes.
- Compiled and ran the **two tests present in this tar** (`test_signed.cpp`, `test_upper_write.cpp`) under C++17: both ended `ALL PASS (0 failures)`. This tests those host units only; ESPHome compile was NOT performed and XTR live validation was NOT performed.
- Source concern: the display/readback confirmation callback runs **on receipt of a requested settings-block read before checking successful reply transmission**. A read request alone is not definitive proof of delivery or of changed controller state.
- Source concern: its delivered YAML enables automatic takeover after a short listen window and generates active replies. Its RS485 gap/framer and physical-owner arbitration are not validated for the XTR. **Do not deploy or merge its YAML, automatic arming, native responder, authentication or write code.**
- Source/code inventory discrepancy: handoff lists seven historical host test suites not present in this supplied V3 tar (which includes only two tests). Claims of live success remain attributed to the external author pending actual raw evidence.

## Relevance and safe next action

**Strongest external clue:** the native 0x0F gateway path and mailbox-driven settings lifecycle match our V84–V86 source-derived architectural direction much better than the old speculative 0x06 DCM application model. This does not change current local proof.

**Local authoritative state unchanged:** FAS1 user-verified RX_ONLY/HARD_DENY; earlier V83 initial B11D failure mechanism open; EXP388 RUNNING / PARTIAL; V49 rollback source available. V86 COMPLETE / POSITIVE remains vendor-source and historical-capture **offline**; next V87 remains offline version/profile discrepancy research. No new user experiment should be considered completed, and no new TX is authorized by this cross-model example itself.

**NEXT (offline):** compare the external author's named block/read-refresh observations against exact original CM930 source and local October 3 passive 0x0F chronological evidence, preserving role/ACK/electrical-ownership uncertainty. Ask for narrowly scoped anonymized raw ATEC evidence only if needed; original gateway is not available to this XTR project.
