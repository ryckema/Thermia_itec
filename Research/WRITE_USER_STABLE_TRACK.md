# Write User Stable — XTR M

**Status (2026-11-04):** W2R92 private standalone ESPHome YAML, **FLASHED / LIVE according to user normal-operation confirmation**. No new numerical bus-health trace or per-parameter write retest supplied; historical 51/51 + 4/4 verified user writes and accepted existing calendar tests remain closed.

- Source snapshot SHA256: `b20d145018d0ac0de36410f8738054e0841a1bd8563d3bbdf7ba39a7b37d289f`.
- Distributed privately in `Thermia_XTR_WRITE_USER_SERVICE_SPLIT_PRIVATE_20261104.zip`, member `WRITE_USER_STABLE/Thermia_WRITE_USER_STABLE_W2R92.yaml`. This snapshot is BYTE-IDENTICAL to prior private W2R92 user-live source.
- Freeze Write User control/HA entity IDs, S92 sole UART/RX/TX/DE owner, V5 RX/CRC, M6 sync, CURRENT4/4, calendar CAL32, FC03/FC16, hot rejoin, ABORT and validated user setting writes. Never port unvalidated service TX into this track.
- Future changes: fixes for proven bugs or controlled, reviewed backports only; each must preserve one owner and controller-confirmed semantics.
- This branch contains non-sensitive track metadata, **not** the private OEM/handshake/proprietary firmware. It does not yet constitute a public redistributable User 1.0.
- User-display DATE/create/delete and general service functions remain outside currently implemented scope, despite prior user acceptance of existing weekly calendar write-test campaign.
- No rewrites of project `README.md` or `Write (Beta)/iTec Eco`.

**GO:** freeze the verified User baseline; **ONE NEXT ACTION:** prepare non-sensitive public release surface and scrub proprietary source before any publication. Do not retest already accepted controller writes.
