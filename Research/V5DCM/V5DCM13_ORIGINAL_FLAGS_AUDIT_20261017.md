# V5DCM13 — original CM930 flags audit — 2026-10-17

**Status:** COMPLETE / POSITIVE for directly inspected Connect 2.0.18 original JSON; RUNNING / PARTIAL / INCONCLUSIVE for Connect 2.1.105 original JSON provenance. No live experiment.

**Hypothesis and baseline:** The 43 ranges in V5DCM12 repository-derived flag mapping match the original firmware. Baseline V5DCM12 14/14 offline map tests; live V5DCM2 FIX1 RX-only.

**Controlled change:** Read original `appfs_2018/usr/lib/python3.10/site-packages/device_client/conf/930/modbus-flags.json` inside the RAUC 2.0.18-source-identical appfs_2018.zip, compare each original register span (start/end) against V5DCM12 literal ranges. No TX/YAML. **Original JSON SHA256** `bb0b335eaf4e3a98e5d71d1cd1551e0772fedcfcd3f7d17f3c78e04c21844b9e`.

**Observed:** original flags JSON contains words 1800–1804; request words 1802/070A=16 bits, 1803/070B=16 bits, 1804/070C=11 bits. All 43 range start/end pairs EXACTLY match the V5DCM12 table. Four original version-labelled controller profile folders found (1.1.1-2.1.0; 2.2.0-2.2.1; 2.3.0-2.4.1; 3.0.0-3.1.1); do not infer installed XTR profile from folder presence.

**Unknown / negative scope:** original RAUC 2.1.105 appfs `modbus-flags.json` has NOT been directly extracted or compared this run; `device_client.zip` has Python files but not full conf tree. Thus no claim of byte-level mapping identity between the two RAUCs. Positive old mapping achieved. Abort on speculating new-map equality, protected payload exposure or any hardware action; recovery none, production remains RX-only.

**Next:** direct original 2.1.105 ext4 config extraction, bounded separate subtask; no new live experiment.
