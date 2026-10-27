# V5DCM — firmware-derived CM930 rebuild (2026-10-17)

## Objective and lineage
Implement a native Thermia Connect / CM930 / Online DCM session on the user's iTec XTR M with ESP32/ESPHome while preserving the known-good V5 Home Assistant monitoring. Rebuild motivated by recovered original Thermia Connect firmware 2.0.18 and 2.1.105. Compare against historical V4.1, genuine captures, and local XTR evidence. Visible milestones: DCM recognition icon and online indication, each separately verified; display semantics remain unknown.

## V5DCM1 — RUNNING / PARTIAL
**Hypothesis:** existing V5 CRC-good frame callback can feed an independent passive CM930 observer without impairing production monitoring.
**Baseline:** GAP-51E V5 RX-only / HARD_DENY and historical V4.1 session spine.
**Controlled change:** add passive CM930 session model wired to the existing validated frame callback; no second UART parser, no new TX route.
**Scope:** native slave 0x0F; FC23 handshake area 071C/0730 (observations only), FC16 03E8/14 and 085F/5, historical ordered configuration pages and FC03 mailbox 0708.
**User result:** user explicitly confirmed flashing the V5DCM1 YAML on 2026-10-17. Live logs Pasted text(20261017-004017).txt, Pasted text(20261017-004733).txt and Pasted text(20261017-004803).txt show continuing production telemetry, >1000 clean frames, no parser resync/drops/geometry faults, no software UART TX or physical TX attempts per software counters. No native 0x0F FC23 challenge or 0708 mailbox poll captured. The new observer lacks dedicated visible HA/log output; its internal transitions cannot be independently certified by these logs.
**Result classification:** POSITIVE (preserved observed RX-only production and NO-TX), INCONCLUSIVE (internal model transitions, DCM session/display).
**Positive:** good frames and telemetry, TX=0. **Negative:** regressions or unexpected TX. **Abort:** parser faults, RX drops, physical TX, bus disturbance. **Rollback:** GAP-51E RX-only. No rollback required or claimed.

## V5DCM2 — PREPARED / NOT RUN
**Hypothesis:** a firmware-geometry-aware native FC23 challenge observer and explicit diagnostics can integrate into V5 without affecting RX or allowing TX.
**Baseline:** user-flashed V5DCM1.
**Controlled change:** add challenge-shape/correlation observer from CRC-good frame callback and periodic [V5DCM2] logging (~30s), plus an interface for a future private handshake transform. No cryptographic transform included; no key, response bytes, live emulator or physical TX path.
**Target:** native slave 0x0F, FC23 request with write 071C/count8 and read 0730/count8, observed only. Ordinary FC16 03E8/14 and 085F/5 remain capture-only.
**Positive:** [V5DCM2] diagnostics visible; RX-frame counts progress, integrity counters remain 0, TX=0. **Negative:** diagnostics absent or degraded production monitoring. **Inconclusive:** no native challenge observed. **Abort:** any unplanned TX, RX integrity deterioration, HA production regression. **Rollback:** V5DCM1 (user-confirmed live) or GAP-51E. Firmware compile and live run not confirmed.
**Important correction:** V5DCM2 is not a dynamic cryptographic responder. A provider interface does not establish implemented challenge/response.

## Evidence categories
- **Observed XTR locally:** passive healthy V5 telemetry; periodic 03E8/count14 and 085F/count5; no fresh native FC23 nor 0708 in these runs; software TX counters zero.
- **Firmware-derived:** CM930 slave behavior, three handshake software states NOT_ACCEPTED/RESPONSE_SENT/ACCEPTED, dynamic response transform, mailbox and data-publication processing, separately modeled application readiness. Neither firmware acceptance nor local observer state proves display state.
- **Cross-model/genuine captures:** ordered bootstrap, mailbox and native approval sequences; profile-specific page counts and timing.
- **Unknown:** fresh live controller challenge, response-slot ownership/wire EOF, local challenge-derived acceptance, physical DE state independently measured, DCM icon and online display triggers.

## Next
V5DCM2 should be flashed and only compact [V5DCM2] logs plus health and TX counters returned. Next implementation V5DCM3 must respect RX-only and the private/public separation. Any live transmit test requires a separate explicit test plan, address/payload provenance, abort and rollback. Do not infer a new experiment from repeated old logs.

## Repository publication policy
User authorized GitHub updates for every new experiment on 2026-10-17. Update newest-first canonical Research/THERMIA_PROJECT_STATE.md, EXPERIMENT_LOG.md and PROTOCOL_FINDINGS.md, retaining history. Publish only nonsecret reports and passive-only public diagnostics. Never commit working private 0x0F emulation, recovered keys/security algorithms, private response bytes or mailbox/0708 command tooling. Local complete YAML bundles are *not* automatically safe for public release.
