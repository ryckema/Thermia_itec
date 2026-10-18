# V5DCM33-FIX-B — First live passive baseline result (2026-10-18)

**Experiment V5DCM33-FIX-B-LIVE-PASSIVE-01: COMPLETE / POSITIVE — passive reception/no-ARM only.** This does not complete any controller-restart, post-gap RX cohort, fresh rejoin or native Online/DCM emulation experiment; **V5DCM33-FIX-B-POST-GAP-01 remains PREPARED / NOT RUN**.

## Provenance and baseline

- User supplied full 4,999-line ESPHome API log `Pasted text(20261018-212405).txt`, **SHA256 0f86352fd9c6cf2c70c7b3d1ef004c3d2280ef73ca42a3b188993bd566e4a87f**, 363 KB, 23:20:28.816–23:23:50.942 (202.126s visible), ESP32 uptime 485 to 665s; log began well after ESP boot.
- Firmware source basis is earlier private FIX-B ZIP SHA256 `1753e92590237e9685f74d8c9d80ca64064cb73e5151d56dcdfc38cbc0769cde`. Actual runtime **FIX-B marker** `[V5DCM33-FIX-B]` and new HA text entity `V5DCM33-FIX-B Passive Post-Gap RX Witness` observed repeatedly, supporting deployed code family. Exact compiled/flashed YAML/firmware cryptographic hash still UNVERIFIED.
- Baseline prior user-flashed FIX-A first passive report V5DCM33-FIX-A-LIVE-PASSIVE-01 RUNNING/PARTIAL had current B11D clean but eight early parser-resync steps and 1 separate old P5 historical fault; FIX-B this time starts clean, with no parser resync and P5 history 0. Do not infer this difference was caused by FIX-B source; new ESP boot and distinct observation window.

## Target, controlled change, and success criteria

No write address, page, register or TX payload: this is a receive-only baseline following user-reported flash. Observe that FIX-B remains DORMANT without manual ARM, old B11C/B11D and HA production readers are unaffected, no parser/buffer/CRC/parity faults arise, and software TX HARD_DENY/DE=0 persist. Next post-gap trial is a different experiment and was **not executed**.

## Observed facts in full log

1. **FIX-B present and idle:** at 23:20:31.262 `[V5DCM33-FIX-B] PASSIVE phase=DORMANT reason=NONE gaps=0 frames=0 batches=0 ageMs=0 B11D_OLD_FAULT=0 R6P5_HISTORY=0 TX=HARD_DENY OWNER=UNKNOWN`; all 27 logged FIX-B marker/entity occurrences remain `DORMANT`, counters 0, no ARM or gap. At 23:23:48.386 corresponding entity still `DORMANT reason=NONE frames=0 batches=0 gap=0 OLD_B11D=0 P5_HISTORY=0 NO_TX`.
2. **Independent RAW integrity:** at 23:23:26.988 `[B11D-RX]` 16,570 UART callbacks, 120,771 bytes, 2,247 RAW batches, **5,617 rawFrames=portableFrames=comparedV5**, `countDiff=0 byteDiff=0 noise=0 incomplete=0 ambiguous=0 overflow=0 nativeFault=0/0/0 ioTx=0 hold=0 fault=0 DE=0`. At 23:23:50.941 sensor `Bridge 11D Raw Frames` continued to 5,821; independent parity console snapshot was at earlier time.
3. **Original B11C parser and CRC:** at 23:23:28.765 `[B11C-PORTABLE]` original one-callback portable/V5 **5,637/5,637**, `countDiff=0 byteDiff=0 boundaryFaults=0 resync=0 drops=0 ioTxAttempts=0 hold=0/0 fault=0 DE=0`. At 23:23:30.140 B11C public CRC 5,653 checked, `crcMismatch=0 fault=0`. Sensor `Bridge 11C Portable Frames` 5,821 by 23:23:50.365. Counts sample at different timestamps; don't demand cross-observer equality at unsynchronised instants.
4. **Main parser/HA:** `V5 Parser Status` at 23:20:30.947 frames=4,124 pages=672 known=672 `badGeom=0 unknown=0 resync=0 drops=0 TX=0`; at 23:23:50.942 frames=5,829 pages=950 known=950, same zero fault fields. `Parser Resyncs Since Boot=0`, `RX Buffer Drops Since Boot=0`, `Bridge 11D Raw Faults=0`, `Bridge 11D First Fault=NONE` throughout. HA telemetry updates supply, condenser, room, outdoor, compressor, current, DHW and FC04/FC23 restored readers; in observed segment Heating mode.
5. **TX fail closed:** executor `HARD_DENY candidates=944 denied=944 physical_attempts=0` at 23:23:47.018; independent `V5 S3 UART Write Calls=0`, `V5 S2 Physical TX Attempts=0` and software DE=0. Hardware pin voltage was not measured. `P74D UART=1 DE_LOW_SW=1 EXEC=DENY_LOCKED RX_NOW=CLEAN P5_HISTORY=0 NEW_HOLD=0 resync=0 dR=0 dD=0 OWNER=UNKNOWN SLOT=UNKNOWN TX=DENY`.
6. **Native scope not advanced:** at 23:23:31.463 `[V5DCM32] RX_ONLY step=0 scope=0 localGen=0 verdict=0 epoch=UNKNOWN owner=UNKNOWN C2=UNPROVEN TX=HARD_DENY`; V5DCM23 `profile=1 received=1/33`. `R6 P24 Controller Start Witness=NO_CALLBACK_GAP_SEEN / EPOCH_UNKNOWN / NO_TX`; native 0x0F FC23 boundaries remain 0. Existing HA 0x02 and 0x0A FC23 counters are not 0x0F native handshake. P5 `UNQUALIFIED / NO_TX` reason `ESP_BOOT_UNQUALIFIED`, rather than historical fault latch.

## Result

All **passive live** acceptance criteria satisfied: FIX-B runtime markers/diagnostic entity observed, B11C/B11D independent RX and parity clean, parser/HA ongoing, software TX/DE fail closed. **COMPLETE / POSITIVE for V5DCM33-FIX-B-LIVE-PASSIVE-01 only.** Exactly matched compiled image hash absent, physical DE pin unproven, no 1–4 byte fault exercise and no post-gap cohort tested.

## Follow-up / safety plan

Next **V5DCM33-FIX-B-POST-GAP-01 PREPARED / NOT RUN** is to validate separately the manually armed 90-second bounded shadow after a >=5s fresh callback gap and >=30s/50 CRC/parity-good independent frames. This would remain RX_SHADOW_ONLY without clearing old B11D/P5 holds or authorizing the V5DCM32 native session. **Before initiating a disruptive controller power-cycle:** inspect FIX-B first fault timing, relationship between 90s arm scope and 30s/50 new frames, and whether initial B11D short residual from physical restart will appropriately coexist with shadow proof. Only start a user-initiated live reboot within separately documented abort/rollback criteria; no implicit retry. Abort on parser/CRC/HA or TX/DE failures; rollback FIX2 known-good when required. Preserve earlier V5DCM32 manual power cycle COMPLETE / NEGATIVE and all historical negative/inconclusive evidence.

No proprietary protected 0x0F emulation or 0x0708 mailbox tooling is disclosed.
