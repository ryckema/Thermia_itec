# V5DCM15A — original Connect 2.1.105 config extract (2026-10-17)

**Status:** COMPLETE / POSITIVE for original firmware extraction, 2.0.18↔2.1.105 flag equality and static profile-selection tests (16/16); COMPLETE / INCONCLUSIVE for actual XTR M profile, local native DCM handshake acceptance, icon and Online. **No live experiment, ESPHome YAML change or TX.**

## Hypothesis / baseline / controlled change
**Hypothesis:** original Connect 2.1.105 RAUC appfs CM930 configuration can verify the V5DCM13 43-range mapping and supply profile-selection evidence needed by V5DCM16. **Baseline:** V5DCM13 old-original flags audit, V5DCM14 subscription-selected package requirements, V5DCM15 fail-closed synthetic session model and user-flashed V5DCM2 FIX1 RX-only. **Controlled change:** direct offline SquashFS→ext4 extraction of the original `Thermia_Connect-2.1.105-s1.raucb` appfs and JSON comparison to the V5DCM10-proven 2.0.18 appfs archive; inspect original 2.1.105 `configuration.py` and CM930 version configuration call site. No hardware I/O.

## Observed source facts
- Original appfs SHA256 `dde141340f1d48a389fb9845ff03d09526fc32c91a829a4cbc77101dd3f18cc5`, matching the original RAUC embedded manifest previously independently verified in V5DCM10.
- **New 2.1.105 file location:** `/etc/device-client.d/930/modbus-flags.json` within extracted ext4. Original 2.0.18 comparison file: `device_client/conf/930/modbus-flags.json` from the provenance-verified original ZIP. 2.1.105 `configuration.py` default runtime config root is `/app/etc/device-client.d`; mounted runtime path is not separately independently observed here.
- **The two original JSON flag files are byte-identical**, both 3,333 bytes and SHA256 `bb0b335eaf4e3a98e5d71d1cd1551e0772fedcfcd3f7d17f3c78e04c21844b9e`; request words 0x070A 16 ranges, 0x070B 16, 0x070C 11. This resolves the remaining V5DCM13 new-image JSON provenance gap.
- CM930 original profile config JSON count: old 33, new 35. Of 25 common relative paths, 8 identical and 17 changed. An old version-range directory `2.3.0-2.4.1` was expanded to `2.3.0-2.4.3` in 2.1.105 with newly added `info-2.4.2.json` and `info-2.4.3.json`. Other shared configurations/sensors/alarms changed. This does **not** itself prove changed on-bus XTR behavior.
- **Source-derived selection:** `configuration.py` `set_cm_fw_version` selects versioned config directory using observed CM firmware SemVer with inclusive min-max; `modbus_server15.py` triggers version config load after `hp_cm_firmware_version` becomes known; `flags_json_file_path()` resolves FlagsFile independently of profile. Actual local XTR CM version/profile not established in this experiment.
- `request_read_all_registers` excludes a particular operation request bit, further confirming 43 available map ranges ≠ 43 universally required packages.

## Interpretation and classification
**PROVEN / original recovered firmware:** static old and new mapping identical; JSON profile-tree counts/differences; version-scoped selection code. **STRONGLY SUPPORTED:** CM930 configuration varies by controller version even though range-to-bit map is unchanged. **HYPOTHESIS:** profile-aware replay can account for some historical config differences when profile provenance is available. **OPEN:** selected XTR profile, session owner/epoch/slot, native accepted, icon, cloud Online, detailed semantic impact of changed profile fields. No new local bus capture or TX.

**Positive criterion:** directly extract new RAUC JSON, hash/check old-new mapping and source-selection behavior — MET, 16/16 offline checks. **Negative:** mismatch or extraction/source error — NOT OBSERVED. **Abort:** disclosure of protected security/emulation material, any unauthorized TX or production modification — NONE. **Recovery:** offline discard; live V5DCM2 FIX1 remains RX-only/HARD_DENY.

**Next V5DCM16 — PREPARED / NOT RUN:** replay existing historic FC23 request/response-shaped pairs and config bursts with source-qualified profile=UNKNOWN unless independently proven; separate timing correlation from owner/epoch/acceptance and do not transmit. Positive bounded frame-level provenance and no false accepted status, negative mismatched replay; abort owner/slot overclaim or any TX; rollback no hardware change.

Sanitized user archive: `V5DCM15A_RAUC_2_1_105_CONFIG_AUDIT_20261017.zip`. 
