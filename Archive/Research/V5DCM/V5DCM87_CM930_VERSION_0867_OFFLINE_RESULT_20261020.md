# V5DCM87 — CM930 0x0867 version/profile provenance (2026-10-20)

**Experiment ID:** V5DCM87-CM930-VERSION-0867-PROVENANCE-OFFLINE-01. **Status: COMPLETE / POSITIVE (offline mismatch reproduced; native compatibility UNKNOWN).**

**Baseline:** Last user-confirmed V83-FAS1 RX_ONLY/HARD_DENY, original V49 rollback; EXP388 RUNNING / PARTIAL and separate V83 B11D startup anomaly OPEN. V86 offline is previous result. **One change:** static analysis only. No new XTR TX, flash, compilation or hardware action.

## Observed source facts

* Original Thermia Connect 2.1.105 `device_client/data/info.py` CM930 default firmware extractor references **decimal register 2151 = hex 0x0867**, formula `semver(({2151} // 100) % 10 , ({2151} // 10) % 10 , {2151} % 10)`. This is labelled control-module/display firmware version, not necessarily DCM/outdoor software.
* Original `device_client/cm/modbus_server15.py` passes extracted `hp_cm_firmware_version` to `_load_config_files`. Original `configuration.py` uses exact or inclusive version-range directory matching.
* Bundled 2.1.105 extracted appfs `etc/device-client.d/930` profile directories: `1.1.1-2.1.0`, `2.2.0-2.2.1`, `2.3.0-2.4.3`, `3.0.0-3.1.1`.

## Observed historical local XTR facts

The existing archives contain 19 complete FC16 requests addressed to 0x0F beginning at 0x0864 count=4 with fourth register 0x0867 consistently **decimal raw22**: September24 21:00 (2), September25 07:15 (4), 09:02 (1), 09:05 (0), October03 (12). Source and raw historical records are distinguished: capture shapes prove neither source device electrical ownership nor semantic native acceptance. The old ACK shapes are not application acceptance.

Literal CM930 formula applied to raw22 gives **0.2.2**. No bundled range includes 0.2.2. A hypothetical 220 would give 2.2.0, **but 220 was not observed**. Do not substitute it.

## Conclusions, unresolved items and next

**STRONGLY SUPPORTED / OFFLINE:** Mismatch is reproduced and is not a hex-vs-decimal conversion or incorrect offset within the historical FC16 0x0864 block. **CONDITIONAL:** If an unmodified Connect2.1.105 CM930 received exactly this as its version, none of its bundled ranges matches. **UNKNOWN:** actual current controller version, whether this is the version delivered in a genuine CM930 session, alternate settings or fallback paths, live device compatibility and accepted native TX session. Never claim incompatibility from this offline finding alone.

Local offline assertions PASS: original source formula, profile selection conditions, four directories, 5 historical file counts and all 19 extracted raw22 values. No ESPHome compile/flash; no physical TX. Abort if original source, FC16 lengths, register offsets or historical values fail their checks; rollback N/A because no hardware changed.

**Next:** V88 offline native version-field/config-source provenance and firmware profile-selection fallback audit, preserving RX_ONLY/HARD_DENY, EXP388 partial, V49 rollback and the unresolved B11D first-start issue. No confidential handshake, native protected response, command mailbox or security implementation is disclosed.
