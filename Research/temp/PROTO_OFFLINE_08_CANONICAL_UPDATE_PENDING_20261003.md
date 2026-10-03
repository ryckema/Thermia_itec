# Pending canonical reconciliation — PROTO-OFFLINE-08

GitHub was **not modified**. Apply these changes to the canonical project artefacts only when GitHub write permission is explicitly granted.

## THERMIA_PROJECT_STATE.md — add/refine

- Offline analysis: **PROTO-OFFLINE-08 — COMPLETE / POSITIVE**.
- Live experiment remains **EXP388 — RUNNING / PARTIAL**.
- No device TX, YAML change, restart, setting mutation, or live experiment-state change occurred.
- `0865` is reconfirmed as the modern Online/DCM compressor-running export: `0865=1 <=> 1E:000B frequency>0` (48/48 genuine Eco5 samples).
- `0866` is **STRONGLY SUPPORTED** as commanded-start/pre-run: `cmd7=cmd8=1` while compressor frequency remains zero (48/48 classification; one positive event).
- `083C` is a coded/inverse copy of the same pre-run condition: `0000` during pre-run, `0080` otherwise (43/43 usable genuine Eco5 samples).
- `083B` is **STRONGLY SUPPORTED** as a modulo-60 compressor-active controller-cycle remainder: across 14 active intervals its modulo-60 increment exactly equalled the number of `0x02 FC17` controller poll cycles.
- Refine `087D`: do not call it generic/lifetime compressor runtime. The strongest current interpretation is `INFORMATIE -> ONTDOOIEN -> LAATSTE ONTD.P.` (compressor runtime in minutes since last defrost).
- `087B..087D` is **STRONGLY SUPPORTED** as the three-value defrost statistics group, likely in manual order: `ONTD.PERIODES`, `TUSSEN. 2 ONTD.`, `LAATSTE ONTD.P.`. Direct XTR UI confirmation remains pending.
- `0872..0878` is a **HYPOTHESIS** for the seven `BEDRIJFS TIJD` counters; exact order/scaling is not established.
- `0867` remains **STRONGLY SUPPORTED** as a platform/topology-dependent static constant (`0016` older Online/DCM, `00E8` Eco5); exact identity open.
- `0834=0100` remains OPEN; possible short periodic/accounting pulse only.

## EXPERIMENT_LOG.md — add

### PROTO-OFFLINE-08 — COMPLETE / POSITIVE — unresolved runtime-field reduction

Baseline: PROTO-OFFLINE-06 / PROTO-OFFLINE-05 runtime-family model.

Controlled change: offline reduction only of unresolved `0834`, `0864`, and `0870` fields using the existing six raw genuine Online/DCM captures plus the commissioning manual as a semantic menu anchor.

Key results:
- `0865` compressor-running reconfirmed 48/48.
- `0866` pre-run predicate 48/48, one positive start event.
- `083C` pre-run coded inverse 43/43.
- `083B` modulo-60 active controller-cycle accumulator: 14/14 adjacent active intervals matched exact `0x02` poll counts.
- `087B..087D` strongly match the manual's three defrost-statistic fields; `087D` advances only during compressor-running samples and is strongest for `LAATSTE ONTD.P.`.
- `0872..0878` structurally match a seven-value operating-time group but remain unassigned.
- `0867` is topology/platform static (`0016` legacy vs `00E8` Eco5).

No bus interaction occurred. EXP388 unchanged.

## PROTOCOL_FINDINGS.md — durable additions/refinements

- **PROVEN / genuine Eco5 structural:** `0865 = (1E:000B compressor frequency > 0)`.
- **STRONGLY SUPPORTED:** `0866` = commanded-start/pre-run indicator; positive when run command pair is asserted but compressor frequency remains zero.
- **PROVEN / genuine Eco5 structural:** `083C=0000` during that pre-run condition and `0080` otherwise in the analysed corpus.
- **STRONGLY SUPPORTED:** `083B` is a modulo-60 compressor-active controller-cycle accumulator/remainder, not RTC seconds.
- **STRONGLY SUPPORTED:** `087B..087D` is the defrost-statistics group; likely `ONTD.PERIODES`, `TUSSEN. 2 ONTD.`, `LAATSTE ONTD.P.` in manual order. `087D` has strongest behavioral support for runtime-since-last-defrost.
- **HYPOTHESIS:** `0872..0878` corresponds to the seven `BEDRIJFS TIJD` counters; exact order/scaling open.
- **STRONGLY SUPPORTED:** `0867` is a platform/topology-dependent static field (`0016` old, `00E8` Eco5), semantic identity unknown.
- **OPEN:** `0834=0100` short pulse semantics.
