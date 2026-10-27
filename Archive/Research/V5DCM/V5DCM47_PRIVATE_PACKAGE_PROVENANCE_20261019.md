# V5DCM47 — private ZIP package provenance (2026-10-19)

**Artifact status:** PREPARED / NOT RUN. This is private packaging of **unchanged local XTR V5DCM45-FIX2 source**, not a new V47 program revision, compilation, flashing or TX experiment.

- Private chat-only downloadable artifact: `V5DCM47_LIVE_ONE_SHOT_01_PRIVATE_PREPARED_NOT_RUN.zip`.
- Package SHA256: `644ab24a9e53fb236dd61832feb48402b343ac791b1285b7c7923825276c860d`, 189086 bytes, 70 entries.
- Source ZIP: `V5DCM45_FIX2_PRIVATE_B11D_STARTUP_GUARD_ONE_ZIP_ONE_YAML_NOT_FLASHED.zip`; source SHA256 `9a709b5e4a53d05ced25e59310bc0b87f6c794a685a32ed18fa9ccdc432ca3ef`.
- Exactly ONE YAML unchanged: `waveshare-thermia_V5DCM45_FIX2_B11D_STARTUP_READY_ONE_SHOT_PREPARED_NOT_FLASHED.yaml`; SHA256 `9f9b2ac86a3f407a09b387ef4638469b9831a2e5681a59cd9bdbca12ef1c7fb7`.
- All **67 original FIX2 archive entries** byte-identical; existing original SHA256_MANIFEST passes; source ZIP and output ZIP CRC testzip passes; no source edits.
- Three extra V47 packaging-only entries: `V47_README_FIRST.txt`, `V47_LIVE_TEST_PLAN_PREPARED_NOT_RUN.md`, `V47_PACKAGE_PROVENANCE.json`. This metadata includes bounds, abort/rollback and source hashes. No source algorithms, recovered keys or private responder implementation are uploaded to GitHub.
- Actual FIX2 user live proof: 178.8s RX qualified, B11D/parser healthy, physical TX zero. One-shot native reply remains PREPARED / NOT RUN; 70ms callback-relative deadline is not physically measured EOF. The private ZIP is not recoverable from the public repository alone: retain the private chat download/backup.

**This packaging work does not count as an additional experiment or protocol discovery.** No new ESPHome compilation was performed for the renamed archive. For a future first live controller-return test follow [V47 scope](V5DCM47_COLD_REJOIN_ONE_SHOT_PREFLIGHT_20261019.md), with an intentionally initiated scope, one canonical current challenge, one bounded response at most, explicit abort and V44B no-TX rollback. Do not needlessly reflash FIX2 solely because the ZIP filename is V47.
