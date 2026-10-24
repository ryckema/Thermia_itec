## 2026-10-25 — MAIN03-C5 OEM internal acceptance parity — PREPARED / NOT RUN

Produced private complete ZIP `THERMIA_MAIN03_C5_OEM_INTERNAL_ACCEPTANCE_PRIVATE_20261025.zip` from locally LIVE-proven MAIN03-C1C3 (not source-only C3A). OEM Connect 2.1.105 `_on_function16` equivalent internal state: NOT_ACCEPTED at ESP boot; RESPONSE_SENT after already-guarded FC23 physical response success; ACCEPTED upon valid controller FC16 excluding 0x085F and 0x04BA. Internal state is NOT native owner/TX permission; no sender, UART/DE or safety-guard changes. One read-only diagnostic entity. YAML parsed offline, existing native send call count 75 unchanged. Full target compile, flash and XTR live verification NOT performed. This is an internal parity correction, NOT an autonomous hot-rejoin fix; online alarm/hot-rejoin remain REAL BLOCKER. No flash into current alarm/qualified session, HA writes on hold. Status PREPARED / NOT RUN.

---

## 2026-10-25 C5 post-restart timing clarification — LIVE evidence

Single ESP-only restart on MAIN03-C1C3: pre-reboot last qualified traffic approximately 01:09:38; post-reboot `BOOT_RX_ONLY / OWNER NOT INHERITED / TX LOCKED` by 01:10:11. User observed Online communication alarm approximately 01:11:30–35. Passive `NATIVE FC16 OBSERVED / SESSION OWNER UNKNOWN / TX LOCKED` first reported 01:11:33.281, after the reported alarm boundary; known FC16 shapes reached 25 by 01:12:20. No accepted new handshake is evidenced in this log. Native frame reception after alarm is NOT warm-session ownership. ~112-117 s to reported alarm supports an approximately two-minute monitoring timeout as a hypothesis, not an OEM-confirmed timing contract. C5 remains COMPLETE / NEGATIVE; do not promote FC16 observation to TX authority. OEM source initializes NOT_ACCEPTED and requires subsequent handshake acceptance evidence but does not prove warm takeover. Engineering NO-GO for unqualified physical auto-TX; retain last locally verified C1C3 and guarded cold-start. No new flash or test performed.

---

## 2026-10-25 — C5 ESP-only hot-rejoin LIVE NEGATIVE / alarm

Baseline: user-live MAIN03-C1C3, qualified stage40, alarm-free before ESP restart. One user-initiated ESP restart while controller stayed powered. Subsequent uploaded log showed M6 BOOT_RX_ONLY / OWNER NOT INHERITED / TX LOCKED; passive native FC16 candidate remained OWNER UNKNOWN. No native owner promotion or verified resumed FC03/FC16 service. User directly observed controller Online-module communication alarm around 01:11:30–01:11:35. Classification COMPLETE / NEGATIVE for unattended ESP-only hot-rejoin on this exact firmware. Distinguish direct alarm report from bus log. Prior FRESH_BOOT_RUNTIME_QUALIFIED entries were from pre-restart retained runtime, not this ESP restart. Fail-closed TX is correct but operational alarm is a REAL BLOCKER. Do not try repeated ESP/controller restarts, START, refresh, or unqualified TX; settings writes remain on hold. No new firmware flashed or experimentally validated. Next engineering decision: retain single UART/DE owner and cold-start baseline; require evidence-based, controller-approved mid-session session handover/rejoin mechanism, with hard stop, before enabling physical TX. Existing C3A is source-only and NOT a C5 repair.

---

## 2026-10-25 — MAIN03-C3S — PREPARED / NOT RUN (no live experiment) (SOURCE / OFFLINE TESTED, PREPARED / NOT RUN)

From complete original C1C3 baseline plus source-only C3 atomic staging, produced ONE private firmware ZIP `THERMIA_MAIN03_C3S_REFRESH_SCHEDULER_PRIVATE_20261025.zip` (YAML SHA256 `4f7eada4eaa8cae068553ab74fe48a4c31ae9a5c005e353b6a540fd95e773b81`). Adds a single 30s passive scheduler tick that declares the *accepted* atomic CURRENT snapshot due at 240s, only with existing qualified S92 session/2.4.2 profile/integrity/idle guards; logs once per generation. 240s is a local planning threshold, NOT OEM cadence evidence. Scheduler cannot arm the read button or TX, and creates no second UART owner or new frame. Physical autonomous TX remains NOT AUTHORIZED. Existing user-initiated C3 native refresh stays the only enabled path, previous 300s TTL unchanged; exact 9 Configuration buttons, one UART writer and 75 native send calls preserved. Offline YAML/substitutions/entity parity tests passed; no target compile, flash, new XTR LIVE observation. **Do not flash over an active qualified DCM session**: ESP-only hot-rejoin remains unproven. The next functional step is a separately authorized bounded automatic physical read experiment, not an autonomous flash or parameter writes.

---

## MAIN03-C3-ONE-SHOT-01 — COMPLETE / POSITIVE (2026-10-25)

- **Hypothesis:** One explicit native read-only four-page request during an already qualified S92 runtime will re-export and owner-ACK H/D/C/M and advance local atomic snapshot generation.
- **Baseline:** User-FLASHED/LIVE MAIN03-C1C3, manual cold-return session, stage40, ~45min runtime, `snapGen=1`, last CURRENT stale, normal FC03/0708 and runtime FC16 acknowledgements; no evidence of spontaneous second four-page cycle.
- **ONE change:** User presses `MAIN01 | Arm One-Shot Four-Page CURRENT Refresh`. Physical TX only as previously guarded response to subsequent controller poll, no independent master TX.
- **Expected:** W2/W3 read-only demand, controller H/D/C/M FC16, owner ACK, `snapGen=2` within existing 60s timeout; abort on safety alarm/session loss.
- **Actual:** 00:52:50.691 PRESS_RECEIVED count=1; 00:52:53.925 `FOUR_PAGE_CURRENT_REQUEST_TX W2=0001 W3=0019`; H/03E8 00:52:54.068, D/042E 00:52:54.592, C/0442 00:52:56.170, M/0546 00:52:56.877, all native ACK; `CURRENT_4PAGE_CONFIRMED` 00:52:56.884; 00:53:01.439 `snapGen=2`, `FRESH`, `receiptPages=4/4`, `ackMask=0F`, `confirmed=1`, `button=1`, `denied=0`. CRC_DIFF/resync/drops 0; no parameter writes or restart.
- **Conclusion:** COMPLETE / POSITIVE for user-initiated native C3 fresh four-page re-export. Autonomous scheduler remains source-design only, not authorized for physical auto-TX or claimed LIVE.
- **Abort/rollback:** Existing S92 STOP/RX ONLY and fail-closed guards; no abort triggered; preserve currently qualified firmware/session; no unsolicited OTA/controller restart.

---

