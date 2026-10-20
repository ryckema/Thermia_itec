# V5DCM89 — CM930 version provenance and independent ATEC V3 comparison

**ID** V5DCM89-CM930-VERSION-PROVENANCE-ATEC-CROSSCHECK-OFFLINE-01. **COMPLETE / POSITIVE (offline cross-source comparison ONLY)** — 2026-10-20.

**Baseline:** user-confirmed V83-FAS1 RX_ONLY/HARD_DENY; original V49 rollback; EXP388 RUNNING/PARTIAL; earlier separate V83 B11D startup discrepancy OPEN. V88 previous result. **One controlled change:** examine the user-supplied ATEC V3 archive as EXTERNAL SOURCE/CLAIM beside original vendor firmware and archived XTR findings. No compile, flash, native TX, new capture, or hardware change.

## OBSERVED FACTS
* Historic local XTR bus FC16 block start 0x0864 qty4 includes decimal register 2151/0x0867 last, value raw22 in 19 archived occurrences from V87 (2+4+1+0+12). Local old captures are not proof of current controller version.
* Original Thermia Connect2.1.105 `device_client/data/info.py`: CM930 `hp_cm_firmware_version` is described as **Firmware version of heat pump Control Module (display)**; the source expression `semver(({2151} // 100) % 10, ({2151} // 10) % 10, {2151} % 10)` yields **0.2.2** for raw22. CM920 uses a different formula. `cm/modbus_server15.py` passes extracted version to config loader in WAITING_FOR_DEVICE_INFO.
* EXTERNAL ATEC V3 `step3-profile-and-mailbox.md` section 4 explicitly says block `0x0864 x4` contains 2148..2151, with **2151=22**; section 1 says 2151 reads 22 on author's ATEC. The author's source notes use **2.3.0–2.4.3** as a manually selected air-to-water register/bit-label profile, choosing newer superset over 1.1.1–2.1.0 while acknowledging overlapping identical field names. This is EXTERNAL CLAIM, not independently confirmed: the ATEC historical cold-start capture cited in that source was absent from supplied tar.
* Shipped 2.1.105 four CM930 version directories exclude 0.2.2; V88 showed filename fallback does not select a missing profile directory. The ATEC author's manual profile use is NOT a demonstrated original Connect auto-fallback.

## STRONG CONCLUSIONS
Cross-model recurrence is more plausible because two independent projects report the same 2151 value. The firmware/display version, vendor Connect software version 2.1.105, third-party gateway version V3, and hand-selected configuration profile are distinct concepts. Original Connect default resolver remains a source-level mismatch for raw22; actual original gateway behavior and XTR acceptance are UNKNOWN.

## HYPOTHESES / UNKNOWNS
An alternate corrected version at original Connect runtime, custom/OTA configs, other controller revision or parser behavior may explain mismatch, but no direct evidence picks one. Neither ATEC working-gateway claim nor FC16 ACK shape proves current XTR native session acceptance, electrical ownership, response timing or safe TX. Protected authentication/handshake and mailbox implementations remain private.

**Checks:** locally re-read original zip + external tar; assertions confirmed formula, semantic description, 0.2.2 math, external 2151=22 and profile reference: PASS. Historical count from V87 not independently revalidated in this iteration. Abort if source/value contradiction; rollback N/A. Physical TX=0, flash=0.

**Next V90 OFFLINE:** cross-check display/control-module version and model semantics against independent historical XTR register information; investigate passive-only discriminators. Keep baseline and EXP388 unchanged.
