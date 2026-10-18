# 2026-10-18 UPDATE — extracted original 2.1.105 appfs available and audited

**Status remains RUNNING / PARTIAL**: original source count and dependency count verified directly; object-level equivalence to derived CSV still not independently performed.

## Direct original artifact evidence
User added `/mnt/data/2.1.105 extracted_appfs.zip` (SHA256 `42d365c89a7a0cc76138c57c1bf50cfd95c33c3ffcf7aef26f39c01b7c81f49e`) and `2.1.105 extracted_rootfs.zip` (SHA256 `dc8a4ca05f3e60f61939fb9ab72e1dd6af52378b9f89bd7ea71625e9f2f25447`). ZIP inspection located exact `extracted_appfs/etc/device-client.d/930/2.3.0-2.4.3/{sensors.json,configurations.json,info-2.4.2.json}`.

Direct JSON parse:
- `sensors.json` 99 objects, 23122 bytes, SHA256 `6a5941387f14cb8d5419a715b8983a1d3c044c7d1ffd6c82513103413ba78c0d`;
- `configurations.json` 471 objects, 158727 bytes, SHA256 `d5194627e1678a1b10239b988c6ba195e62b39dbc37f4fe927d3bae907060b2c`;
- `info-2.4.2.json` exists, 2087 bytes, SHA256 `25f24756667f575a0d7cdda0f3a766b306cb19feed30886a9cd8d02087e0e114`.
- zero duplicate `name` fields within each sensor and configuration list.
- Direct application of previously documented firmware literal-brace numeric-token rule on `formula`, `conditions`, `min`, `max`, `default` (never `set_register_formulas`) yields **541 unique numeric register dependencies**. These match the prior derived-index aggregate exactly.
- 99+471=570 matching the repository normalized aggregate.

**Confidence improvement:** four aggregate results reproduced directly from the original uncompressed source JSON. **Still OPEN:** comparing each original name, description, condition, formula and min/max/default against each normalized CSV record; direct 33 selector-group output from original source in this environment (the existing 33 is derived-index analysis). Do not substitute aggregate agreement for row equality. No live test / YAML / TX modifications.

---
# V5DCM21-PACKAGES-03 — original 2.1.105 RAUC provenance gate (step B, partial)
Date: 2026-10-18

**Status: RUNNING / PARTIAL — offline provenance inspection, NOT completed source equivalence.**

## Hypothesis
The 570 normalized sensor/configuration objects in the 2.1.105 CM930 2.3.0–2.4.3 index exactly reproduce the original 2.1.105 RAUC JSON and yield the source-derived 33 W2/W3/W4 significant groups. Prior PACKAGES-02 counts and strict CI are not proof of byte-for-byte equality.

## Baseline and known results
- PACKAGES-02 offline index: 570 semantic objects; 541 dependencies; 33 groups (15 W2 / 10 W3 / 8 W4); 13/33 tracked by existing FIX4.
- Current user-flashed v31 FIX4 is passive/read-only. No YAML, native TX, live tests or production entities changed.

## Evidence actually inspected in this step
- User-supplied `Thermia_Connect-2.1.105-s1.raucb`, SHA-256 `1da6d55dd50dee9335c03f13df35370c3ad7c1a9ebb06a0e9c2b32b92769868c`; file identifies as SquashFS v4 zlib, 116643235 bytes, 5 inodes. RAUC has not yet been unpacked: local environment lacks unsquashfs and libarchive could not open SquashFS. Consequently source profile JSON inside this image has NOT been compared.
- `device_client.zip`, SHA-256 `18ebe6190bbcfff364ca27af9dbf31c8b6e66a7a828d7869b00d32f7012590ac`; Python source present but no CM930 2.3.0–2.4.3 profile JSON. Parser implementation corroborates extraction semantics only.
- `appfs_2018.zip`, SHA-256 `ad27967bdb1f8300fc3768bf30ae5033f55c858269fdd23c1d5a622a23da4c77`; contains `device_client/conf/930/2.3.0-2.4.1/{sensors.json,configurations.json,...}`, an older 2.4.1 upper-bound profile. Not suitable as exact XTR 2.4.2 proof.
- Repository audit `tools/audit_v5dcm21_significant_packages.py` consumes **normalized** `cm930_semantic_objects.csv` and independent physical geometry. It does not read original RAUC JSON.

## Controlled change and criteria
Change: provenance-only audit, no simulator or bus changes.
- POSITIVE condition: extract 2.1.105 RAUC read-only, identify selected original 930 profile and compare original sensor/config objects and token sets with normalized CSV deterministically, documenting unmatched rows.
- NEGATIVE condition: reproducible semantic mismatch in source objects/dependencies.
- INCONCLUSIVE: image inaccessible/unextractable or provenance cannot be proven.
Current outcome: **INCONCLUSIVE source equivalence; valid provenance inventory**. No active experiment executed.

## Next action
Obtain/use a local SquashFS v4 extractor in a safe offline environment, unpack RAUC to a temporary directory, locate the 2.3.0–2.4.3 sensor/config JSON and produce row-level + dependency-level machine-checkable mismatch report. Only then mark B complete. Never infer physical XTR RX or Online from source equality.

## Abort / recovery
Abort on an attempt to enable TX, modify native response/security logic, publish protected implementation or change production YAML. None occurred. No recovery action needed.
