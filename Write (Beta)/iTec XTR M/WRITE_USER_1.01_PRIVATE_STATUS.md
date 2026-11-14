# Write User 1.01 — release and validation status

**Public standalone firmware:** [Thermia iTec XTR / thermia_itec_xtr_write_user_1.01.yaml](../../Thermia%20iTec%20XTR/thermia_itec_xtr_write_user_1.01.yaml)

The public Write User 1.01 contains the complete existing user controls, calendar, telemetry, HA pending-state UI2 fix, V5/CRC, sole RS485/UART owner, guarded FC16/FC03, ABORT and the already-public exact-capture startup response from 1.0. It contains **no additional controller handshake secrets or variable-response key**. As with 1.0, a controller restart presenting a *different* challenge is **not guaranteed to establish DCM**. Do not mistake the new 1.01 build label for evidence of a new cryptographic method in the public firmware.

A separate **private Write User 1.01 build** uses the same local Home Assistant / user control scope and adds automatic native cold-start after a real, qualified controller restart. Its implementation and fixed-key material are not part of the public distribution.

## Evidence

- **FIX19 user-armed, owner LIVE:** variable FC23 response, controller continuation through FC16 startup, CURRENT 4/4, M6=5, and repeated FC03 0708 responses on the user's XTR M.
- **Private Write User 1.01 automatic trigger:** SOURCE / OFFLINE TESTED; `PREPARED / NOT RUN`; not target compiled or owner flashed.
- **Public Write User 1.01:** existing public Write User source with release banner revised and unchanged exact-capture handshake and UI2 fix; not newly owner-live tested as version 1.01. It is not interchangeable with the private automatic implementation.

No new parameter-write permissions have been authorized. A transport acknowledgement is not a controller-semantic setting confirmation.

**Current milestone:** native DCM after controller restart.
**Real blocker:** newly assembled automatic 1.01 still requires an owner-initiated real controller restart observation.
**One next action:** flash the private 1.01 build, restart only Thermia controller (no HA button), inspect M6=5, CURRENT 4/4 and sustained FC03 0708; ABORT and restore FIX19 if required.
