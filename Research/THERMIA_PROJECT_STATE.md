## 2026-10-25 C5 native requalification integration decision — NO-GO without controller authorization evidence

Concrete source-to-LIVE cross-check on C5T against single C5 ESP-only restart capture: post-reboot at 01:10:11 `BOOT_RX_ONLY / OWNER NOT INHERITED / TX LOCKED`, then `FC03=0 RX0708=0 physicalTXthisSession=0` through the pre-alarm window (sample at 01:11:06); user-reported Online alarm at 01:11:30-35. Passive recognized native FC16 arises around 01:11:33, after reported alarm boundary, not as prior authorized rejoin. C5T OEM_INTERNAL_ACCEPTED is a logical software state, but guarded native owner/epoch (`write_arm_ms`, `main01_native_accepted_epoch`, `s92_rejoin_approved`) remains unqualified; no controller-issued, qualified 0708 response/re-acceptance path has been verified in that window. Engineering decision: NO-GO for bridging passive FC16 to owner authorization or adding automatic physical TX; preserve last locally LIVE C1C3 and source-only C5T. Do not falsely label C5T a hot-rejoin fix. One next engineering action is isolate evidence of OEM mid-session controller-authorized response opportunity, preferably from existing original Connect traces; without that, bounded user-initiated test plan rather than automatic takeover. No flash or live retest. HA parameter writes still ON HOLD.

---

## 2026-10-25 — MAIN03-C5S OEM ACCEPTED read-demand integration — PREPARED / NOT RUN

One complete private C5S ZIP `THERMIA_MAIN03_C5S_OEM_READ_DEMAND_PRIVATE_20261025.zip` from C1C3 locally verified via C5R source-only. OEM Connect 2.1.105 `on_handshake_state_changed_event(ACCEPTED)` queues information/operation read requests; controller FC16 receipts clear their request bits. Integrated one acceptance-edge reconciliation with existing 33-group M6 request/receipt ledger, preserving already owned receipts and OEM omitted operation bit8; only when the existing S92 native owner and epoch are already qualified. No second UART/DE writer, no new physical TX, no unauthorised auto APP request button, no parameter writes. YAML parser passed offline; existing 75 native send sites unchanged; no target build/flash/live. YAML SHA256 `9a9287785e30b39b1922c36c0872ec7a063d1b19e24690403ec1b991604365ac`. Status PREPARED / NOT RUN. C5 ESP-only hot rejoin remains COMPLETE / NEGATIVE and Online alarm a real blocker; OEM internal ACCEPTED is not a physical TX permit. Do not flash during alarm/active owned session. Next action: only evidence-backed OEM TX lifecycle integration that supports rejoin; do not repeat failed restart experiment.

---

## 2026-10-25 — MAIN03-C5R OEM internal lifecycle reset — PREPARED / NOT RUN

One complete private firmware ZIP `THERMIA_MAIN03_C5R_OEM_LIFECYCLE_PRIVATE_20261025.zip` built from original user-LIVE C1C3 and source-only C5. Corrected one actual C5 state-coherence defect: internal OEM ACCEPTED/FC16 source is invalidated on native session authority revocation, manual START/ABORT and boot. Original valid FC16 OEM acceptance exceptions 085F/04BA and successful-FC23 RESPONSE_SENT unchanged. Single UART/DE owner, TX guards and 75 send occurrences preserved. YAML parsed offline with ESPHome secret-tag handling; no target compilation, flash, live testing, no HA parameter writes. SHA256 YAML `f0bad49ac29d36b8f9b0852d7ab3fb240d2b3e38d7daf9772b5749acb956f8f5`. Status PREPARED / NOT RUN. This is NOT physical hot-rejoin restoration: owner remains UNKNOWN after ESP reboot and alarm is known; no new TX permission inferred from internal acceptance. C5 remains REAL BLOCKER; do not flash merely to repeat failed restart.

---

## 2026-10-25 — MAIN03-C5 OEM internal acceptance parity — PREPARED / NOT RUN

Produced private complete ZIP `THERMIA_MAIN03_C5_OEM_INTERNAL_ACCEPTANCE_PRIVATE_20261025.zip` from locally LIVE-proven MAIN03-C1C3 (not source-only C3A). OEM Connect 2.1.105 `_on_function16` equivalent internal state: NOT_ACCEPTED at ESP boot; RESPONSE_SENT after already-guarded FC23 physical response success; ACCEPTED upon valid controller FC16 excluding 0x085F and 0x04BA. Internal state is NOT native owner/TX permission; no sender, UART/DE or safety-guard changes. One read-only diagnostic entity. YAML parsed offline, existing native send call count 75 unchanged. Full target compile, flash and XTR live verification NOT performed. This is an internal parity correction, NOT an autonomous hot-rejoin fix; online alarm/hot-rejoin remain REAL BLOCKER. No flash into current alarm/qualified session, HA writes on hold. Status PREPARED / NOT RUN.

---

## 2026-10-25 C5 post-restart timing clarification — LIVE evidence

Single ESP-only restart on MAIN03-C1C3: pre-reboot last qualified traffic approximately 01:09:38; post-reboot `BOOT_RX_ONLY / OWNER NOT INHERITED / TX LOCKED` by 01:10:11. User observed Online communication alarm approximately 01:11:30–35. Passive `NATIVE FC16 OBSERVED / SESSION OWNER UNKNOWN / TX LOCKED` first reported 01:11:33.281, after the reported alarm boundary; known FC16 shapes reached 25 by 01:12:20. No accepted new handshake is evidenced in this log. Native frame reception after alarm is NOT warm-session ownership. ~112-117 s to reported alarm supports an approximately two-minute monitoring timeout as a hypothesis, not an OEM-confirmed timing contract. C5 remains COMPLETE / NEGATIVE; do not promote FC16 observation to TX authority. OEM source initializes NOT_ACCEPTED and requires subsequent handshake acceptance evidence but does not prove warm takeover. Engineering NO-GO for unqualified physical auto-TX; retain last locally verified C1C3 and guarded cold-start. No new flash or test performed.

---

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

