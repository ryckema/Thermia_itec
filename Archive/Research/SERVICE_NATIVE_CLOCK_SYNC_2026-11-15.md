# Service native clock sync — iTec XTR M (2026-11-15)

**Scope:** owner-tested Thermia iTec XTR M 3N, CM930 controller 2.4.2; private Service firmware lineage `Service-dev001` through `Service-dev007`. This is a **research/status document only**. It does not publish proprietary Connect code, handshake logic, protected runtime messages, private captures, or a deployable write implementation.

## Executive result and proof boundaries

- **PROVEN / LIVE:** The native controller clock is retrievable as one seven-word `0x06EA/7` controller page, rendered as one Home Assistant entity. Existing native S92 session and sole UART/TX ownership continue to operate.
- **PROVEN / LIVE for one explicit owner-initiated correction on this XTR:** `Service-dev006` sent a clock adjustment using its UTC-based payload, received **a genuine controller-origin FC16 `06EA/7` semantic readback**, and reached `COMPLETE / POSITIVE`. The signed HA-minus-controller difference changed from about **-3629 s** to **+30 s**. This is **not** general proof for other controller families or every timezone.
- **SOURCE / OFFLINE TESTED, PREPARED / NOT RUN:** `Service-dev007` adds opt-in automatic checking and adjustment every 24 hours. Its scheduler has not been target-compiled, flashed or owner-live validated as of this entry. It must **not** be marked LIVE/POSITIVE on the strength of the manual dev006 result.
- **No autonomous firmware flashing** and no changes to unrelated user/service parameter writes.

## Register-level identification

Controller clock page `0x06EA..0x06F0`:

| Register | Field | Expected range / representation |
| --- | --- | --- |
| `06EA` | seconds | 0–59 |
| `06EB` | minutes | 0–59 |
| `06EC` | hour | 0–23 |
| `06ED` | day | 1–31 |
| `06EE` | month | 1–12 |
| `06EF` | year | 0–99, offset from 2000 |
| `06F0` | weekday | Monday=0 … Sunday=6 |

**SOURCE:** Original Connect CM930 2.4.2 configuration describes the seven fields, including write-capable parameters. **LIVE:** locally captured XTR controller data decoded consistently, including a 2026-10-03 clock and weekday. An OEM “writable” flag was *not itself* proof of local XTR acceptance; that required the later genuine FC16 controller response.

## Service development sequence

| Build | Meaningful change | Status |
| --- | --- | --- |
| `Service-dev001` | Home Assistant time source and timezone awareness; no controller RTC write | SOURCE / OFFLINE TESTED |
| `Service-dev002` | Native clock display and difference-vs-HA diagnostic | SOURCE / OFFLINE TESTED at delivery; later native read verified LIVE |
| `Service-dev003` | Explicit, bounded HA manual clock-sync experiment through existing native engine; initial attempt stalled after read | RUNNING / PARTIAL for first attempt; read positive, write inconclusive |
| `Service-dev004` | Release *only* the completed clock-read lease on a valid clock response, keeping general FC16 receipt rules intact | SOURCE / OFFLINE TESTED; fix carried into later live runs |
| `Service-dev005` | Read-only automatic RTC page refresh about every 4 minutes; one advancing HA clock text sensor; stale-data handling | LIVE native automatic read, write-result incomplete |
| `Service-dev006` | Corrected manual RTC write data to UTC-based fields; retained same physical TX engine and controller readback | **COMPLETE / POSITIVE — LIVE** for one manual clock correction |
| `Service-dev007` | Opt-in persisted 24-hour check/correct scheduler; reuses validated dev006 one-shot path | **PREPARED / NOT RUN — OFFLINE TESTED** |

The private owner firmware packages/rollback YAMLs are **not** part of this public Research note.

## Owner-live evidence, 2026-11-15

Source: owner-provided `Pasted text(20261115-123245).txt` ESPHome Service-dev006 log, XTR M 3N / CM930 2.4.2. Retain raw/private capture off public GitHub.

1. Around **13:31:05**, automatic `06EA/7` clock read observed; signed difference HA−Thermia **-3629 s**, approximately 1 hour 00 minutes 29 seconds.
2. **13:31:36.261**, explicit HA `CLOCK_USER_ONE_SHOT_ARMED` (bounded manual intent).
3. **13:31:40.304**, one physical clock page sent by existing native S92 TX owner (`CLOCK_PAGE_TX_UTC`).
4. **13:31:40.885**, genuine controller-origin FC16 `06EA/7` reported `CLOCK_SEMANTIC_CONFIRM confirmed=1`.
5. **13:31:40.930**, sync status `COMPLETE / POSITIVE / Thermia controller FC16 clock readback matches HA within 60 s`.
6. **13:31:41.720**, HA−Thermia difference **+30 s**; subsequent sampled states continue to show +30 s.

**STRONG CONCLUSION:** On this controller, the dev006 UTC-based *manual* clock payload achieved the intended semantic correction. The earlier dev005/local-time payload left approximately one hour of offset, consistent with a UTC/local-time mismatch. Do not generalize that interpretation to other models without local evidence. Transport acknowledgments alone were not used as success criteria.

## Intended automatic behavior in dev007 (not yet LIVE)

- One Home Assistant Configuration switch, **`Automatic Heat Pump Clock Sync (24h)`**, initially **OFF**, opt-in persisted across ordinary ESP restarts; manual **`Sync Heat Pump Clock`** remains available.
- Existing read-only controller RTC refresh approximately **every 4 minutes** when the native session permits. **One** combined local controller date/time sensor is shown in HA; its displayed clock advances between authoritative snapshots and must reflect stale data rather than pretend an old page is fresh.
- Scheduled evaluation **every 86,400 seconds (24 h)**, provided HA time/timezone is ready, the native S92 session is qualified, a fresh genuine `06EA/7` snapshot is available, ESP uptime is at least 5 minutes and HA time has been stable for at least 60 seconds.
- **No write** if absolute deviation is at most **60 seconds**. Larger deviation permits **at most one automatic correction attempt per 24 hours**, using precisely the same existing bounded dev006 native one-shot and requiring controller-origin semantic readback. Last-check/last-attempt timestamps survive ordinary ESP restarts.
- If no authoritative confirmation is received, do **not** retry automatically; disable the automatic switch, report the inconclusive outcome and leave the manual/ABORT/rollback workflow available.
- DST/timezone changes are handled according to the configured HA time source and next eligible check; “within the next 24h” is a design expectation, **not yet a live-verified guarantee**.
- No separate UART owner, unscheduled setting writes, new unverified parameter-write scope, or bypass of existing CRC/DE/slot/session controls.

**Expected:** Correct clock -> `AUTO_CLOCK_CHECK_OK`, no setting write. Out-of-tolerance clock -> single `AUTO_CLOCK_SYNC_ARM` and, on verified controller readback, `AUTO_CLOCK_SYNC_FINISH confirmed=1`. **Actual dev007:** not yet run.

## Experiment bookkeeping and recovery

- `SVC-CLOCK-READ`: **COMPLETE / POSITIVE**, local native read and automatic `06EA/7` refresh observed. Read-only function.
- `SVC-CLOCK-WRITE-DEV005`: **COMPLETE / NEGATIVE** for achieving full HA alignment (residual ~1 hour), but physical controller clock changed; this is *not* a transport failure.
- `SVC-CLOCK-WRITE-DEV006`: **COMPLETE / POSITIVE**, explicit one-shot, genuine controller FC16 selected page readback, +30 s residual (within 60 s).
- `SVC-CLOCK-AUTO-DEV007`: **PREPARED / NOT RUN**, automatic scheduling/persistence/fail-stop only offline tested.

**ABORT:** Turn off automatic HA switch to prevent *new* automatic attempts; for an in-flight native transaction use existing `ABORT Native Session`. **Rollback:** private dev006 YAML included with dev007 bundle. No need to disconnect room sensor or change wiring.

## Current milestone / deliverable / blocker / one next action

- **CURRENT MILESTONE:** Private Service native RTC sync: manual correction proven; automatic 24-hour scheduler prepared.
- **DELIVERABLE:** `Service-dev007_PRIVATE.zip` distributed privately to owner; this public Research evidence and handoff.
- **REAL BLOCKER:** None for the verified **manual** clock correction; the remaining evidence gap for **automatic** mode is one owner LIVE run of dev007 on the XTR.
- **ONE NEXT ACTION:** Owner flashes dev007, explicitly enables the HA automatic switch, and verifies a scheduled `AUTO_CLOCK_CHECK_OK` (no TX when within threshold), or one controller-confirmed `AUTO_CLOCK_SYNC_FINISH` if the clock drifts beyond 60 s. Do not declare dev007 live before observing it.

## Public/private boundary

Research summaries and non-sensitive register semantics are public. All private YAML/ZIP firmware, proprietary Connect implementation details, cryptographic handshake data, sensitive logs and raw frames remain private. **Protected `README.md` and `Write (Beta)/iTec Eco` must not be modified.**
