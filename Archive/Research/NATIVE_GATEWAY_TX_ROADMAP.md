> **Historical S86–S93 plan (2026-10-21).** The active cloud-free implementation roadmap is [S92_LOCAL_DCM_IMPLEMENTATION_ROADMAP.md](S92_LOCAL_DCM_IMPLEMENTATION_ROADMAP.md). This older document is retained for experiment history, not the next-action queue; its S86/S88/S90/S91 gates must not restart a redundant test loop or override the later XTR S92/FIX28 live findings. This navigation notice does not grant native bus TX or HA parameter writes.

# Thermia iTec XTR M — Native Gateway & TX roadmap
Updated 2026-10-21. **Planning only; no flash or live TX authorized.**
Goal: native Thermia Online/Connect-like gateway accepted by XTR M, then one independently verified, reversible Home Assistant semantic write. Preserve verified V5 RX, B11C/B11D, watchdog and HA. Do not substitute room sensor 0x0A or blind Modbus writes.

## Baseline
- S84 COMPLETE / POSITIVE limited to V83 RX_ONLY / HARD_DENY regression; independent physical DE not verified.
- S85 RUNNING / PARTIAL. Offline local October 3 capture: a 0x0F FC23 request/reply pair and subsequent FC16 0x03E8 block/ACK. Physical sender, ownership, epoch, slot and Connect session remain OPEN.
- Existing S23 engine/scoped transport: host tests only. S83 true ESP32-S3 ESPHome target build NOT RUN. External ATEC V3 is reference only, no proven XTR electrical identity or code reuse license.

## Sequential gates
1. **S86 Passive observer:** Integrate metadata-only FC23/FC16/FC03 sequence classifier into existing V5 RX callback. Never change TX eligibility; preserve bus-health counters, B11C/B11D and HA. Validate replay, missing frame, CRC, order, timeout, split/coalesced frames.
2. **S87 Offline engine decision:** Exercise existing S23 engine with observed inputs and negative cases, test unknown ownership, epoch/slot, restart, stale state, cache-commit rules and failed delivery. Default deny; accepted_risk82 OFF. No private keys, challenge response algorithms or mailbox implementation published.
3. **S88 Real target build:** Compile RX_ONLY/HARD_DENY with ESPHome ESP-IDF for ESP32-S3 preserving verified YAML; compile separate candidate only, no flashing. Archive build hashes; compile is not runtime proof.
4. **S89 RX-only runtime:** User-initiated RX-only flash and >10 min supervised regression versus S84. Keep DE low and TX denied. Roll back V83 on HA, RX, watchdog, supervisor or device regression.
5. **S90 Electrical ownership proof:** Independently prove who sends requests and responses, bus slot ownership, controller epoch, DE state and timing. No inference from 0x0F address, ACK or historical replay. Hard STOP if unproven.
6. **S91 First scoped physical TX:** Only after a separately reviewed, user-initiated experiment: one predefined response to a verified solicitation with exact private payload/CRC, timer, arm, abort and rollback. No scans, unsolicited frames or speculative writes; success is safe delivery, not session acceptance.
7. **S92 Native session acceptance:** Validate independently real startup, FC16/FC03 synchronized state, refresh, reconnect and controller-confirmed semantics. Distinguish transport ACK from application acceptance; abort on alarm or communication errors.
8. **S93 Semantic write:** One bounded reversible parameter with XTR-proven mapping/current value. Independently read back via controller and restore baseline, then expose guarded control under HA Configuration.

## Cross-cutting requirements
Each experiment has ID, verified baseline, hypothesis, one change, frame/register details (kept private where sensitive), success/negative/inconclusive rules, abort, rollback, redacted evidence and user-confirmed result. Use only permitted statuses. No uncontrolled or automated TX. Never repeat G01-G06 without new evidence. Do not auto-enable ATEC transmitter; no copied protected handshake code or keys.
Update THERMIA_PROJECT_STATE.md, EXPERIMENT_LOG.md and PROTOCOL_FINDINGS.md after each experiment/material finding. Next: **S86**, passive RX-only observer integration and offline negative tests. If S90 cannot be established without original hardware, TX remains blocked.