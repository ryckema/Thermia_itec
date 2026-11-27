# XTR M heating cycle reconstruction — 2026-11-09

**Status:** COMPLETE / POSITIVE for the **offline temporal model only**. Owner-LIVE measurements in `history-34.csv`, 11:00–12:48 CET; no new physical test or RS485 TX. Original Connect 2.1.105 CM930 2.3.0–2.4.3 sensor definitions inspected locally (source not reproduced here).

## OEM semantics
- `heat_demand_pid = -{2120}` (`0x0848`); `supply_line_temp_wanted = {2121}`; measured supply `{2000}`.
- `operation_status_heat_building = {2149.0}`, `queued_demands_heating = {2150.0}`.
- XT/XTR commissioning manual service HEATING default START=-50, STOP=+50, startup circulation 5 min, heating-time maximum 30 min *for alternating demands*. Defaults are not proven active configuration on this installation.

## Repeated command → compressor sequence

| Cycle | Request 0007 ON | Run Enable 0008 ON | PID at enable | Fan ON | Compressor ON | Enable→compressor |
|---|---|---|---:|---|---|---:|
| 1 | 11:25:50 | 11:25:55 | -49 | 11:26:06 | 11:27:08 | **73 s** |
| 2 | 11:57:12 | 11:57:14 | -49 | 11:57:23 | 11:58:27 | **73 s** |
| 3 | 12:29:00 | 12:29:02 | -49 | 12:29:11 | 12:30:16 | **73 s** |

The effective start discriminator strongly supports the service default -50, allowing for cached-telemetry rounding and timing latency. Do **not** assert the entire 73 s is a single timer: it may include circulation/outdoor staging.

| Cycle | Run Enable OFF | PID at OFF | Supply/wanted | Compressor OFF | Fan OFF | Request 0007 OFF |
|---|---|---:|---|---|---|---|
| 1 | 11:21:10 | -19 | 32/33°C | 11:21:16 | 11:22:31 | 11:23:29 |
| 2 | 11:50:35 | -15 | 31/32°C | 11:50:39 | 11:51:52 | 11:52:48 |
| 3 | 12:19:58 | -10 | 32/32°C | 12:20:01 | 12:21:12 | 12:22:08 |

**STRONG CONCLUSION:** Run Enable OFF precedes compressor OFF by 3–7 s: commanded shutdown. Fan continues ~74–82 s and cycle request ~130–139 s after enable OFF: repeatable controlled run-down. The simple claim *“exported PID crosses +50, therefore stop”* is contradicted by all three observations. Actual shutdown predicate remains **OPEN** (other water/ODU control, modulation or a different internal variable possible). Do not call the pump defective.

Complete observed runs: 11:27:08→11:50:39 (23m31s), 11:58:27→12:20:01 (21m34s). Both were heating; DHW/cooling/defrost status zero. Third run ongoing at export end. Target supply 34→30°C while outdoor temperature rose 8→11°C and room 22.1→22.5°C; does not uniquely establish the heat-curve equation.

**Engineering action:** use a read-only observer (standalone analyzer delivered privately to owner) to extend this state-machine model across natural cycles. **No real blocker** to monitoring. **Real blocker to exact STOP-law claim:** missing active SERVICE/HEATING START/STOP and richer stop-reason signal. One next action: correlate natural Run Enable OFF edges against supply/wanted, compressor modulation and limits in longer existing HA history. Do not retest verified S62/S88/V4.1/S92 or generate TX.
