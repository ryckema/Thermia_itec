# Thermia iTec XTR M — Write User RC09FC-UI1 (Public Beta)

## Known issue — UI1 Home Assistant state bounce (2026-11-10)

**Owner LIVE report:** Despite stable native runtime, switching a supported user parameter (e.g. `Cooling | Enabled`) can show requested → old → requested in Home Assistant. **RC09FC-UI1 is therefore NOT verified UX-stable.** Source analysis finds a presentation race: the UI1 stale-value guard begins only in OEMW physical phases 1..3 and misses the existing bounded deferred user queue / pre-TX period, plus some older publication branches. This is **not evidence of failed semantic controller FC16 writes**. An integrated **RC09FC-UI2** fix is `PREPARED / NOT RUN`, SOURCE/OFFLINE TESTED, but **has not been target-compiled, flashed, or verified LIVE**. To avoid silently replacing a published firmware with unverified behavior, this UI1 download remains unchanged for now. **Next:** one previously validated HA edit on UI2; verify controller-origin FC16 confirmation and no visible bounce. The native session, Calendar and CRC/TX protections are unaffected by the reported display symptom.


Local ESPHome / Home Assistant integration for **Thermia iTec XTR M 3N, controller CM930 2.4.2**. This is the XTR M Write User beta, **not** the iTec Eco firmware or Write Service firmware.

## Download

- [Complete ESPHome YAML](./Thermia_iTec_XTR_M_WRITE_USER_RC09FC_UI1_PUBLIC_BETA.yaml) — standalone configuration, SHA-256 `82aa1591bf9e7a1ca33bebe194d333f22712c1b36bff10a89dee7b90f731cb2e`
- [Complete release ZIP](./Thermia_iTec_XTR_M_WRITE_USER_RC09FC_UI1_PUBLIC_BETA_20261109.zip) — YAML, rollback, manifest and detailed `START_HERE.md`; SHA-256 `598cf8f150e0c17b0a054eb14e51593eefeb8dced03a56c09db65d673c652a95`

## Scope

- Runtime temperatures, state, alarms and controller data; native DCM session, CURRENT FC16 4/4, FC03 refresh, `085F/5` alarm refresh, retained-session runtime and manual hot-rejoin
- Bounded manually initiated Home Assistant Write User controls: supported Heating, Cooling, Hot Water, Operating Mode and supported 32-slot calendar editor
- Controller-origin FC16 readback required before a setting change counts as accepted; automatic parameter writes OFF
- UI1 presentation fix: suppress old same-field Home Assistant value echo while an OEMW write is awaiting controller readback
- Preserve one native UART/RX/TX/DE owner, bus-idle/CRC checks, explicit session ABORT and rollback

## DCM start / publication scope

Startup reuses the **same exact recorded 29-byte request / 21-byte response** as the already published [XTR DCM Read Only 1.0](../../Thermia%20iTec%20XTR/thermia_itec_xtr_DCM_readonly_1.0.yaml). The source does **not** contain a XXTEA computation, extra handshake key schedule, or additional cryptographic handshake constants. It is a fixed single-capture match: unknown challenges fail closed. No claim of universal Thermia compatibility.

## Evidence and beta qualification (10 November 2026)

- Owner's XTR M RC09FC W2R92 baseline: **LIVE / LOCALLY VERIFIED** for native runtime, refresh and previously accepted supported user/calendar writes.
- A later runtime log shows **53,503 s (~14 h 52 min)** elapsed; 422,000 CRC checks with zero CRC discrepancies; 26,965 FC16 pages observed; 11,953 `0708` replies; 208 CURRENT cache generations; 168 alarm FC16 responses; stage 40/M6=5 and CURRENT 4/4 still fresh.
- The log's firmware-build entity was not included. Consequently, it does **not independently prove** the exact public UI1 source hash is the flashed build, nor does it include a new deliberate HA edit demonstrating the UI bounce fix.
- **RC09FC-UI1 public source: SOURCE / OFFLINE TESTED; not independently target-compiled or verified live by this release review.** This is a beta and has not been validated on other controller firmware.

## Installation / recovery

1. Start from the verified Waveshare ESP32-S3-RS485-CAN wiring in the project documentation. Do not attach the pump's 12 V connector supply to RS485 terminals.
2. Use the standalone YAML and configure your own local ESPHome `secrets.yaml` (Wi-Fi, API encryption, OTA and fallback AP credentials). No CSV provisioner or external challenge-response key file is needed.
3. Compile/flash using ESPHome. Verify `Diagnostic | Firmware Build` = `USER-RC09FC-UI1 PUBLIC BETA`, a qualified M6 native session, CURRENT 4/4 and fresh alarm source.
4. Keep automatic parameter writes OFF. Use only supported previously validated user controls. Wait for authoritative controller FC16 confirmation, not transport ACK alone.
5. To stop native TX use `Configuration | ABORT Native Session`; to restore the prior tested behavior flash the `ROLLBACK/` YAML in the ZIP. Controller-accepted settings persist through firmware rollback.

This project is community-developed and is not an official Thermia release. The repository root MIT license applies to the project-authored code. **Do not publish private `secrets.yaml` or diagnostic logs containing credentials.**

**Release status:** PUBLIC BETA — not a Write Service release.
