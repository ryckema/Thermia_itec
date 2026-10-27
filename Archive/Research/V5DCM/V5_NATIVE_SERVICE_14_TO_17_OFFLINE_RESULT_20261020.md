# V5 NATIVE SERVICE 14–17 — Offline integration report (2026-10-20)

**All four stages: PREPARED / NOT RUN.** This is source development and host validation only, not a verified XTR live experiment.

## Baseline
User-verified V83 FAS1 RX-only, TX=HARD_DENY, no change to installed YAML. Its reference SHA-256 remains `b4aaedf27f8dd3d58fcc7c09316cfe03d9c8f41d40fcd827a31bf1f104d389fa`. EXP388 remains RUNNING / PARTIAL; B11D first-start anomaly remains OPEN.

## Offline results
- S14: guarded startup-state observation and initial ten-page FC16 chain with separate transport completion / independent runtime-transition gates. Original response provider not ported; tests use explicit mock attestation.
- S15: constrained source-derived runtime service classifier with private response handling, source-only and unconnected to ESPHome.
- S16: private one-word change model with scoped bounds, fresh controller page, exact full-page controller republish, positive and negative host scenarios.
- S17: single source-only router, B11D/watchdog guard contract, hard-denied physical coordinator; known historical XTR frames checked for CRC/shape without transmission.
- **17/17 C++17 host tests PASS.** Includes complete synthetic ten-page progression, mailbox recognition, positive/negative simulated readback and hard-deny under forged permissions.
- No ESPHome compile, no flash, no physical TX, and no newly verified XTR controller acceptance.

## Outstanding blockers
An actual source-verified startup response provider; peer/slot timing and ownership; real V5 UART/DE and B11D wiring; complete validated runtime-page coverage; full-session historical replay; and independent XTR semantic acceptance. The legacy 22-page resume branch remains unproven and disabled. Source-only readiness explicitly returns false; TX remains HARD_DENY.

## Confidentiality
The private source package, native response construction, and restricted bus implementation were NOT uploaded to GitHub. Keep derived private code and response details out of public repository. ATEC V3 remains EXTERNAL SOURCE/CLAIM and is not XTR proof.

## Next action
Use source-backed V4.1 and XTR history to prove the startup provider and integration boundary, resolve the existing B11D startup fault and electrical ownership, then create an offline-tested fail-closed ESPHome candidate. Prepare an exact user-initiated single-response live test only after those conditions are satisfied. Rollback to the verified V83 FAS1 RX-only image.
