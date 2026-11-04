# Write User Stable — XTR M

## USER-CLEAN02 — all-English release candidate (2026-11-04)

Private full-source CLEAN02 SHA256 `ed6845858b5bdc5b58fb6bdda2d0c243604cba841765cb06db85300380827ba9` follows CLEAN01 and exact owner-confirmed W2R92. All 444 HA labels reviewed; 43 further display labels adapted to official English Thermia User Guide; controller Hot Water mode 2 shown as **Away** in HA select and readback (same numeric value), replaces previous Holiday Eco/Vakantie Eco. Offline YAML/IDs/UART and change whitelist PASS; one original S92 physical TX writer preserved. **PREPARED / NOT RUN**, no target compile/flash/live. Exact W2R92 rollback remains in private ZIP. Neither Service nor README nor Write (Beta)/iTec Eco changed.

## WUCLEAN01 — English-label cleanup candidate (2026-11-04)

From exact live W2R92 private source (SHA256 `b20d145018d0ac0de36410f8738054e0841a1bd8563d3bbdf7ba39a7b37d289f`), prepared separate private `Thermia_XTR_WRITE_USER_CLEAN01_EN_PRIVATE_20261104.zip` (firmware SHA256 `f01e3d21db23fe6b2ca4f6b96bb5b3cc4524889707b5209b4cd20a70b5481e78`). Translated 71 of 444 exposed HA labels to English; 2 never-referenced EXP394 globals removed, concise source header and read-only build text updated. Source YAML AST, single S92 physical UART TX owner, M6/CURRENT/CAL32, FC03/FC16, V5/CRC, ABORT and all component IDs unchanged in behavior. **PREPARED / NOT RUN**; offline tested only. W2R92 stays frozen last FLASHED/LIVE normal-operation baseline and exact rollback. Service DEV unchanged. No private firmware published. English label changes may require HA entity registry review, not automatic assumption of same entity_id.

**Status (2026-11-04):** W2R92 private standalone ESPHome YAML, **FLASHED / LIVE according to user normal-operation confirmation**. No new numerical bus-health trace or per-parameter write retest supplied; historical 51/51 + 4/4 verified user writes and accepted existing calendar tests remain closed.

- Source snapshot SHA256: `b20d145018d0ac0de36410f8738054e0841a1bd8563d3bbdf7ba39a7b37d289f`.
- Distributed privately in `Thermia_XTR_WRITE_USER_SERVICE_SPLIT_PRIVATE_20261104.zip`, member `WRITE_USER_STABLE/Thermia_WRITE_USER_STABLE_W2R92.yaml`. This snapshot is BYTE-IDENTICAL to prior private W2R92 user-live source.
- Freeze Write User control/HA entity IDs, S92 sole UART/RX/TX/DE owner, V5 RX/CRC, M6 sync, CURRENT4/4, calendar CAL32, FC03/FC16, hot rejoin, ABORT and validated user setting writes. Never port unvalidated service TX into this track.
- Future changes: fixes for proven bugs or controlled, reviewed backports only; each must preserve one owner and controller-confirmed semantics.
- This branch contains non-sensitive track metadata, **not** the private OEM/handshake/proprietary firmware. It does not yet constitute a public redistributable User 1.0.
- User-display DATE/create/delete and general service functions remain outside currently implemented scope, despite prior user acceptance of existing weekly calendar write-test campaign.
- No rewrites of project `README.md` or `Write (Beta)/iTec Eco`.

**GO:** freeze the verified User baseline; **ONE NEXT ACTION:** prepare non-sensitive public release surface and scrub proprietary source before any publication. Do not retest already accepted controller writes.

## Private Write User production packaging — 2026-11-04

- **DELIVERED (private, no code delta):** `Thermia_XTR_WRITE_USER_PROD_BASELINE_W2R92_PRIVATE_20261104.zip`, containing exactly one standalone firmware YAML, NL installation/ABORT/rollback instructions, SHA256 sums and offline audit.
- Firmware YAML bytes are **unchanged** from user-confirmed running W2R92: SHA256 `b20d145018d0ac0de36410f8738054e0841a1bd8563d3bbdf7ba39a7b37d289f`.
- **OFFLINE TESTED:** YAML parsed; all substitutions defined; 1,205 component/global/UART IDs unique; one physical `thermia_uart.write_array` sender; API/Wi-Fi/OTA, native S92 ABORT and one UART preserved; ZIP CRC and member hash verified. No ESPHome target compile or new flash/live test was executed.
- **SCOPE:** user-only private production baseline. W2R93 calendar API dedup and Service DEV remain excluded pending their own evidence. No new physical TX or setting writes activated.
- No public OEM/handshake/proprietary code published; README and `Write (Beta)/iTec Eco` unchanged.

**CURRENT MILESTONE:** private, reproducible Write User production baseline. **REAL BLOCKER:** none for running existing W2R92; public redistribution still requires a licensing/privacy scrub. **ONE NEXT ACTION:** scope and implement only a demonstrated User-release defect or verified backport, without service feature creep or redundant write tests.
