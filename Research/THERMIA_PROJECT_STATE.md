## 2026-10-25 C5 LIVE: ESP-only rejoin NO-GO

On alarm-free user-live MAIN03-C1C3, one ESP-only restart led to `BOOT_RX_ONLY / OWNER NOT INHERITED / TX LOCKED`, while passive native traffic did not prove session authority. User observed Online communication alarm at about 01:11:30. COMPLETE / NEGATIVE for unattended hot-rejoin on this baseline. Current fail-closed gate protects the bus but lacks controller-approved session recovery. Earlier `FRESH_BOOT_RUNTIME_QUALIFIED` was old-session runtime, not post-reboot proof. Do not flash C3A as a cure; it is source-only. No more restart/TX experiments under alarm, no parameter writes. C5 repair requires a verified controller-authorized warm-session recovery path; do not invent credentials or grant ownership from traffic alone.

---

## 2026-10-25 — MAIN03-C3S bounded local CURRENT refresh planner (SOURCE / OFFLINE TESTED, PREPARED / NOT RUN)

From complete original C1C3 baseline plus source-only C3 atomic staging, produced ONE private firmware ZIP `THERMIA_MAIN03_C3S_REFRESH_SCHEDULER_PRIVATE_20261025.zip` (YAML SHA256 `4f7eada4eaa8cae068553ab74fe48a4c31ae9a5c005e353b6a540fd95e773b81`). Adds a single 30s passive scheduler tick that declares the *accepted* atomic CURRENT snapshot due at 240s, only with existing qualified S92 session/2.4.2 profile/integrity/idle guards; logs once per generation. 240s is a local planning threshold, NOT OEM cadence evidence. Scheduler cannot arm the read button or TX, and creates no second UART owner or new frame. Physical autonomous TX remains NOT AUTHORIZED. Existing user-initiated C3 native refresh stays the only enabled path, previous 300s TTL unchanged; exact 9 Configuration buttons, one UART writer and 75 native send calls preserved. Offline YAML/substitutions/entity parity tests passed; no target compile, flash, new XTR LIVE observation. **Do not flash over an active qualified DCM session**: ESP-only hot-rejoin remains unproven. The next functional step is a separately authorized bounded automatic physical read experiment, not an autonomous flash or parameter writes.

---

## 2026-10-25 MAIN03-C3 — User-initiated four-page CURRENT refresh LIVE POSITIVE

**COMPLETE / POSITIVE — locally user-LIVE on flashed MAIN03-C1C3**, not on source-only C3 candidate. In existing qualified stage40 native runtime after about 45 minutes, user pressed `MAIN01 | Arm One-Shot Four-Page CURRENT Refresh` at 00:52:50.691. Button arm recorded count=1 and did not itself transmit. On subsequent controller-owned FC03/0708, response at 00:52:53.925 carried known read-only W2=0001 W3=0019; controller returned H=03E8 (00:52:54.068), D=042E (00:52:54.592), C=0442 (00:52:56.170), M=0546 (00:52:56.877), all with native owned FC16 ACK. At 00:52:56.884: `CURRENT_4PAGE_CONFIRMED mask=0F pages=4/4 semanticTX=0`. At 00:53:01: `snapGen=2 receiptPages=4/4 page=FRESH confirmed=1 button=1 denied=0`. RX CRC_DIFF/resync/drops=0. No new controller or ESP restart; no HA parameter writes.

**Decision:** C3 *manually requested* fresh four-page refresh is proven; lack of spontaneous second cycle was missing application demand, not inability of controller to re-export these pages. Next engineering deliverable is an integrated bounded source-backed refresh scheduler reusing existing one-shot demand/ownership/FC03 responder, respecting physical-TX authorization: no autonomous physical bus TX without newly explicit user authorization for that defined experiment. ESP-only automatic hot-rejoin remains OPEN; do not equate healthy retained runtime with reboot rejoin, or fresh local snapshot with Online semantic acceptance. Existing MAIN03-C3 staged cache candidate remains PREPARED / NOT RUN and must not be flashed merely for cache staging.

---

