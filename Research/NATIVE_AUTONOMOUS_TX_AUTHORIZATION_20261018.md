# Native Online/DCM TX — user authorization decision (2026-10-18)

## Current user decision
The user explicitly changes the project's *permission policy*:

> **"Algemene, autonome TX-bevoegdheid: nu toegestaan."**

**Interpretation for V5DCM21 and future work:** The user authorizes developing, preparing, implementing and, when a controlled user-initiated live test/deployment has been explicitly scoped and armed, allowing **autonomous native TX responses** by the ESP32 for the Thermia iTec XTR M Online/Connect/DCM integration. The assistant does **not** need to request a fresh general TX permission for every response, handshake stage, bounded retry, frame, or subsequent source modification within an already defined authorized test. This supersedes earlier blanket statements that autonomous TX is not authorized.

This is a *user authorization* decision, **not new evidence** that a native handshake has succeeded, that an exclusive hardware slot is electrically proven, or that any currently installed firmware transmits.

## Scope and boundaries
- **Allowed in principle:** autonomously timed protocol responses and qualified native DCM emulation, including controlled handshake, FC16 ACK handling and justified runtime/service processing, when their session/owner/target, response class and timing conditions are specifically documented. Native protocol state is a separate authority axis from user consent.
- **G01–G06:** the user previously accepted the residual engineering research risks. Their unresolved measurements are **not an automatic reason to reopen six research projects or disallow development**. Preserve provenance of bounded G01-09 video-positive, G02 conditional installed-topology positive, and G03/G04/G06 open plus G05 partial/host-only. Do not change these technical labels to PROVEN.
- **No blanket protocol improvisation:** do not initiate uncontrolled scans, unknown-slave traffic, ACKs for unowned/unknown frames, unrelated unsolicited TX or speculative settings/actuator writes. Retain fail-closed CRC/frame checks, bounded retries, current-session cancellation, known response-slot policies, error handling and an abort/rollback path.
- **Hardware live activation is distinct from granting permission:** first autonomous run/flash still belongs to a clearly scoped **user-initiated live test or deployment** documenting exact target, response/payload provenance privately, expected effects, plausible physical risk, bounded timing/limits, negative/positive outcomes, abort and rollback. No spontaneous actual on-device transmission or modification is performed solely by recording this authorization.
- **Production provenance:** the last confirmed on-device V5DCM19 FIX1/V5DCM20 baseline remained RX-only/TX HARD_DENY. There is no evidence of a subsequent flash, physical TX or Online status. Do not silently relax a deployed software HARD_DENY based on text alone. Autonomous TX becomes a property only of a new explicitly deployed/armed implementation.
- **Confidentiality:** no public recovered native response/security algorithms, protected private 0x0F responder code, confidential command-mailbox tool or secrets. A source change and a successful CI test are never a successful live experiment.

## Status and provenance
**Authorization decision: RECORDED / user explicit instruction, NOT a device experiment.** No PREPARED/COMPLETE experiment status is being assigned to the consent itself. Previous dated experiment reports remain correct historical snapshots for their original times; where older files say general autonomous TX was not allowed, this dated decision supersedes **the authorization statement only**, not their recorded physical test results or technical unknowns.

Next: continue V5DCM21 implementation with autonomous response design under this standing permission, preserve fail-closed output for the currently installed RX-only baseline, and prepare the first narrowly documented deployment test when source and response behavior are ready. Do not ask again merely whether native TX is permitted in principle.
