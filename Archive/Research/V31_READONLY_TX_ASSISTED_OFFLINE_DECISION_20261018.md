# V31 passive versus TX-assisted semantic readout — offline decision (2026-10-18)

**Status:** OFFLINE ANALYSIS ONLY; no new physical experiment. READ-V31-UNKNOWN-01 and READ-V31-COOL-01 remain RUNNING / PARTIAL. No changes to FIX4 or flashed code.

## Verified inputs
- Current `Read-only/Thermia itec XTR/thermia_itec_xtr_m_read_only.yaml` blob `f4b90fcd3d96cb728ba4726409bacd9d5c23b5f3` is RX-only: UART has no tx_pin, GPIO21 driver-enable stays receive. 258 named HA entities, 13 native page-presence flags. CRC-valid frames update bus-health bookkeeping.
- User-confirmed FIX4 observation: 151s ESP uptime: 03E8:Y, other twelve monitored native page families N; user subsequently reported still N, without exact new uptime. The ten native source families behind 34 named Unknown entities are absent from matched decoder branches. Direct 0x1E telemetry works. No raw current physical bus audit.
- **Local causality already proven:** EXP325 qualified fresh native session; EXP326 exact owned 03E8/count14 ACK -> 03FC/count11; EXP327 03FC ACK -> 0410/count22; EXP328 0410 ACK -> 042E/count15; EXP329 bounded next ACK progression toward 046A. Historic 2026-10-03 and 2026-09-25 local captures show older count13/count21 geometry, and ordered ACK-associated configuration-page transfer.
- **Local passive counterexample:** FIX8H observed 130 recurring 07D0 runtime pages / 5 minutes with TX=0 *in an already-established session*. A newly passive device must not assume that this initializes itself.
- Genuine Online/Connect and firmware evidence identifies native service/application package tracking and roles; package completeness, native ACK delivery, accepted session, app OPERATION and cloud Online are distinct. Exact current XTR owner/session, profile-specific significant rows, and full 524-word reachability remain OPEN.

## Source inspection of FIX4
- `uart:` begins ~line 486; no UART tx_pin.
- `thermia_last_valid_frame_ms`, frame counter and healthy publish updated in CRC-valid parser (~line 682).
- `0x0F FC16` decoder recognizes `0442/count>=13` (~1837) and `0532/count>=18` (~2098), plus other exact families.
- The presence witness recognizes *complete valid decoder shape*, not indisputable physical non-emission; historical `03E8` and `0410` length variants and source-direction interpretation must be checked.
- Legacy top-of-file comments include mixed FC10/FC16 terminology: comments alone are not proof of actual current frame origin or the correct owned response.

## Architecture decision
**Profile A — RX-only monitoring (keep published FIX4 untouched):** strict physical receive only; show directly witnessed values; absent native-page settings remain unavailable. Never synthesize configuration values or present absent optional equipment as OFF.

**Profile B — TX-assisted read-only semantics (separate confidential experimental track):** potentially satisfy native session/ACK duties to obtain controller-originated pages, while exposing only HA sensors and never initiating user setpoint/mode changes. This is **NOT physically RX-only**, even if HA entities have no write controls. Do not publish proprietary native 0x0F responder, protected 0708 mailbox tooling or credentials. Do not merge untested TX into Read-only/FIX4.

## Next offline discriminator before new experiment
1. Reconcile current FIX4 input acceptance: origin/slave/FC/count, CRC, page mask, and unknowns against existing local captures; identify false negatives caused by variant shapes vs genuinely missing dependent transfers.
2. Pin the exact already-demonstrated fresh-session ownership and frame geometry from EXP325–329 and V5 rollback state; differentiate initial qualification, page ACK and repeat-runtime phases. No direct generic Modbus write assumption.
3. Construct a *single-response-class* controlled test spec only if matching ownership/current context can be established. It must spell out target slave/role/page, exact evidence-backed response bytes and CRC privately, timing/slot, expected effect, limits, refusal, abort conditions (peer ownership ambiguity, timeouts, unexpected page count, alarm/bus regression), rollback and evidence summary. No unbounded scans or broad ACK all.
4. Update three canonical files when a new experiment is PREPARED or new material finding is confirmed. Do not mark COMPLETE before user supplies live results.

## Decision
**Do not modify FIX4 yet.** The first useful new deliverable is a **private offline native-session/ACK gate review** rather than another passive 15–30 minute wait or a speculative TX firmware release. Preserve original v31 FIX4 and V5 verified fallback.
