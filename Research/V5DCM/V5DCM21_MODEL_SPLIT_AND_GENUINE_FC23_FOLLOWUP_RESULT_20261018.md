# V5DCM21 — firmware-model acceptance split and genuine FC23-followup geometry
Date: 2026-10-18

## Status
- **V5DCM21-MODEL-SPLIT:** RUNNING / PARTIAL; **offline source/model regression PASS** (no user-confirmed live experiment).
- **V5DCM21-FC23-FOLLOWUP:** RUNNING / PARTIAL; **bounded raw-capture chronology and synthetic-CI audit PASS** (no user-confirmed live experiment).
- **V5DCM21 native Connect/Online integration overall:** **RUNNING / PARTIAL**.
- This work does **not** establish live XTR acceptance, physical TX authorization, controller epoch, exclusive response slot, application OPERATION, profile/package readiness, cloud onboarding or an Online icon.

## Baseline, provenance and one controlled change per substep
Known-good live production: user-flashed **V5DCM19 FIX1 RX-only**, V5DCM20 local 18m33s **COMPLETE / POSITIVE**, zero reported physical native TX attempts. **Exact flashed FIX1 source YAML/ZIP is still not byte-proven** and remains untouched. Previous V5DCM21 source checks: 24 Core/readiness, 46 RX-join, 33 callsite and 5 passive-capture synthetic regressions PASS; C++ portable and embedded Core now byte-identical. V5DCM18 *original full seven-corpus stateful Python Core replay* remains RUNNING / PARTIAL, and accepted G01–G06 risks remain accepted.

### Controlled change A: preserve two reference semantics without conflating authorization
Original public `Thermia_Connect_Firmware/tools/xtr_dcm_reference_core.py` is intentionally **unchanged**. It is a historical, firmware-derived model:
- `note_approval_sent()` explicitly sets `Handshake.RESPONSE_SENT` in the reference model. This is an injected **synthetic event** unless a real, successfully transmitted native reply is independently established.
- Its `Core.fc16()` promotes `RESPONSE_SENT -> ACCEPTED` on an FC16 kind whose start is not `0x085F` or `0x04BA`, **before** the subsequent owner/geometry classification.
- Direct `Core.fc16()` does not itself validate `frame.slave`. This is an **API boundary limitation**, not proof that the full actual serial pipeline forwards a foreign-slave frame.
- A mismatched out-of-order `0x03FC/count11` can therefore produce `Owner.NO, tx=False` while the *Python reference internal handshake* becomes `ACCEPTED`.
- By contrast, current public portable+embedded C++ `Core::fc16_decision(const Frame&) const` is a **pure classifier**; it does not change handshake. This is a deliberate fail-closed implementation policy, not evidence that Thermia's original firmware has that exact behavior.
- Neither internal firmware-like acceptance nor an FC16 Owner/TX classification is evidence of delivery/physical ownership, application data-package completion, semantic setting acceptance or Online.

Firmware-derived interpretation comes from `XTR focus/CM930_NATIVE_SESSION_RECONSTRUCTION.md` (Connect 2.1.105 `modbus_server15.py`, `client.py`, `state.py`, profile sources) and `findings/CM930_NATIVE_DCM_STATE_MACHINE.md`: actual recovered firmware has separate handshake enum `NOT_ACCEPTED / RESPONSE_SENT / ACCEPTED` and application/data-package/profile/onboarding axes. **Firmware semantics are not automatically locally demonstrated XTR behavior**. A compliance-test `0x03E8` example is narrower than the production Python/reference selector.

Controlled source change: add **only** offline `tools/test_v5dcm21_handshake_model_split.py` and its CI job. No alteration to original Python semantics, native reply transformation, physical response adapter, Core state setters, mailboxes or production YAML. GitHub commits: test `4c05a0aeac181c95bde49b70cfa2c73132ccb583`, CI inclusion `9d984646db3cea32ca3765bb064cf926b08c9588`.

### Controlled change B: temporal audit of already saved genuine/collaborator captures
New generic `tools/analyze_v5dcm21_reply_followup.py` observes *only* CRC-valid RTU envelope lengths, slave `0x0F`, FC23 request/response **shape**, and first subsequent full FC16 start/count/time delta. It neither checks nor emits private response payloads, never derives a security algorithm or sends frames. Analysis horizon **30 seconds** is solely an offline bounding choice, NOT a controller acceptance criterion, retry setting or native protocol timeout. Future raw file usage is local; no raw captures published.

GitHub commits: analysis tool `a458430f07a578e3c01a1400080af355d1be4856`, fixed structural dummy test shape `8cb99a3e89da70ef580df24725f5f84f2abcb525`, CI inclusion `83b4fc789dccc1c40a9f8e787d2d6587bd586491`.

## OBSERVED FACTS — genuine/collaborator raw capture replay
Three *existing user-supplied* timestamp-plus-RTU-hex captures were read locally in a separate Python CRC/geometry audit; **all rows were CRC-validated**, with no new bus interaction:

| Capture and provenance | SHA-256 | CRC-valid frames / invalid | Native 0x0F FC23 request shapes / reply shapes | First native FC16 after each reply-shaped frame |
| --- | --- | --- | --- | --- |
| iTec Eco5 2026-09-26 — genuine/collaborator cross-model | `3836b7885dfe246398fc2a053bf1be286df4001df3ab9703952c5775db1ae91f` | 10,719 / 0 | 99 / 2 | both `03E8/count14`, each **92 ms** |
| iTec Eco5 2026-09-28 — genuine/collaborator cross-model | `55583e2ec2cd940a45f17d10b0b7a523865ccc25b3ed14c099a2eecd2a12160c` | 9,174 / 0 | 64 / 4 | all `03E8/count14`; **93, 482, 465, 124 ms** |
| ATEC 2026-10-03 fragment — genuine/collaborator legacy profile | `14918065297264473e2357822a8694d184e7821b8c2a3b1cb316039678a708a1` | 2,687 / 0 | 1 / 1 | `03E8/count13`, **1,833 ms** |

Here `response shape` means only the standard FC23 reply *envelope length* matched and CRC was valid; **the hidden response transform was not verified by this analyzer**. All seven reply-shaped events had a first later full FC16 start `03E8` in the 30s observation window. The elapsed intervals above describe archived traffic only; they must **not** become a universal response deadline or active TX timing rule.

**Profile caveat / correction of potential misreading:** the October ATEC capture has a `03E8/count13` first page and therefore correctly scores **0/32** against the *modern XTR/Eco5 03E8/count14* cold reference. That is a **profile geometry mismatch**, not absence of all initial `03E8` pages or disproof of its distinct ATEC 32-page session. These are **not seven new local XTR sessions**. Repeated `03E8` after some Eco5 events shows reply-plus-first-page is not itself proof of complete cold configuration.

## ACTUALLY EXECUTED regression evidence
Mandatory GitHub Actions `V5DCM21 fail-closed readiness (offline)`:
- [Run 39120900293](https://github.com/ryckema/Thermia_Connect_Firmware/actions/runs/39120900293) firmware commit `9d984646db3cea32ca3765bb064cf926b08c9588`: **SUCCESS** with **30 source/API model-split assertions**, original 24 Core/readiness, 46 RX adapter tests, five passive metadata smoke checks, 33 lifecycle callsite checks, embedded Core parity/compile and TX hard-deny.
- [Run 39121165286](https://github.com/ryckema/Thermia_Connect_Firmware/actions/runs/39121165286) firmware commit `83b4fc789dccc1c40a9f8e787d2d6587bd586491`: **SUCCESS** including the above and **four synthetic temporal metadata scenarios** (correct length envelope, CRC fault, non-native slave, beyond bounded analysis horizon). **The GitHub CI uses synthetic fixtures, not the three private uploaded raw captures.** The actual local raw-file analysis above was executed separately with equivalent CRC/length/time logic.

No full ESPHome compile, firmware flash, controller reset, bus TX, real delivery acknowledgement or local hardware readback was executed in either substep.

## STRONG CONCLUSIONS, HYPOTHESES and UNKNOWNS
- **STRONGLY SUPPORTED by cross-model real traffic:** response-shaped FC23 frames precede `03E8` configuration requests in these three archived sources; page count depends on controller/profile. This corroborates the existing genuine-capture/session-order documentation.
- **PROVEN source/API distinction:** permissive original Python firmware-like `ACCEPTED` differs from the fail-closed C++ classifier; the models must not be silently declared behaviorally equivalent.
- **HYPOTHESIS:** after a separately proven response delivery and controller-owned source, a genuine XTR session might exhibit the firmware's permissive internal acceptance transition; this requires a scoped new local experiment and is NOT established by these captures.
- **OPEN / UNKNOWN:** electrical source/physical owner and exclusive reply slot, provable current controller epoch, native response delivery of a private firmware-dependent transform, XTR profile selection and all required app packages, genuine semantic readback, display Online/cloud onboarding, full stateful seven-corpus original Python Core test, and exact flashed V5DCM19 FIX1 source identity.

## Positive/negative/inconclusive, abort/recovery, next action
- **Offline positive validation criteria met, but experiment status remains RUNNING / PARTIAL pending a user-confirmed live result:** original reference divergences retained and regression-pinned; accurate CRC/length/time metadata on three existing captures; CI all required stages success; no private contents published.
- **Negative:** no failure in scoped tests. **Inconclusive for XTR native acceptance:** no DCM hardware, delivery proof or active TX experiment.
- **Abort criteria:** any attempt to publish private native response transform, promote raw frame shape to owner/TX authority, issue unsolicited writes or mutate deployed YAML. None occurred; **rollback** if needed is to revert isolated tool/test/workflow commits; known-good user-flashed RX-only firmware unchanged.
- **NEXT:** separately design an **offline evidence-provenance/delivery transition contract** coupling firmware-like `RESPONSE_SENT` only to a proven successful response delivery witness, never to a passive shape. Require independent session/epoch/physical owner and separately observe profile/package readiness. Keep historical Python reference intact; no public private 0x0F responder. Do not claim V5DCM18 full seven-corpus suite COMPLETE.
