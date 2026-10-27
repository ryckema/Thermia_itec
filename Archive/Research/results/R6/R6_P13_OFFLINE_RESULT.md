# R6-P13 — Native DCM offline periodicity versus matched control
Date: 2026-10-10. Status: COMPLETE / POSITIVE for cross-model time correlations, COMPLETE / NEGATIVE for one-to-one mandatory triplet, COMPLETE / INCONCLUSIVE for handshake causality, owner, XTR behavior.

## Experimental discipline
Hypothesis: visible 085F → FC23 → 04A6 adjacency on 0x0F represents a fixed causal session handshake. Baseline: R6-P11 seven genuine Eco5/ATEC/Connect captures (25,031 previously CRC-validated ADUs); R6-P12 164 0x0F FC23 requests and 7 observed paired responses. Controlled change: timestamp/cadence comparison with within-capture FC16 085F → next 04A6 matched control; no firmware/bus action.
Positive: comparable repeated phase/period signatures. Negative: non-unique adjacency, absent/alternative sequences. Inconclusive: captured windows do not define controller boot or owner; no semantic acceptance. Abort: source integrity fault, unsafe write inference, accidental security details. Recovery: not applicable (offline only).

## Genuine cross-model capture evidence
| Measurement | Eco5 2026-09-26 | Eco5 2026-09-28 |
|---|---:|---:|
| 0x0F FC23 requests | 99 | 64 |
| 0x0F FC16 085F | 197 | 122 |
| 0x0F FC16 04A6 | 357 | 226 |
| FC23 median repeat interval | 4.2335s | 4.241s |
| 085F median repeat interval | 2.1245s | 2.131s |
| 04A6 median repeat interval | 1.383s | 1.411s |
| FC23 with 085F before, 04A6 after within 10s | 96/99 | 58/64 |
| Median preceding 085F to FC23 | 1.328s | 1.350s |
| Median FC23 to next 04A6 | 0.141s | 0.141s |
| Median joined 085F→FC23→04A6 | 1.473s | 1.4915s |
| 085F→next 04A6 matched control median (FC23 not required) | 1.451s | 1.4555s |

96/98 (98.0%) and 60/63 (95.2%) FC23 consecutive intervals fall within 3.8–4.7s. The observed 085F stream runs around twice the FC23 rate and 04A6 near three times, so these cannot be universally interpreted as one-to-one transactions. The matched control can show nearly the same 085F→04A6 phase without establishing FC23 as causal.

Exception: Oct03 records one FC23 near its start, without an earlier 085F in that capture window. Another short Sep25 capture contains 085F repeating around 4.2s without an observed FC23. The captures do not establish the actual controller power-on epoch or prove FC23 absent before recording.

## Evidence classification
Observed genuine *cross-model* ADUs: above counts and timing. Strong conclusion: distinct overlapping periodicities, correlational phase only. Hypothesis: FC23 is slower scheduled session-maintenance work, possibly handshake-related. Firmware-derived: archived Connect CM930 code provides separate handshake/settings/operation blocks, which does not validate native XTR M semantics. Unknown: causal scheduler, semantic FC23 response acceptance, 157 unpaired responses in R6-P12, local owner/epoch, any XTR FC23 write authority.

## Next
R6-P14 possible offline phase interruption/stability analysis of existing timestamps; no controller or ESPHome changes. R6-P10 FIX1 remains RUNNING / PARTIAL, first-fault HA latch untriggered in submitted logs. Native Online/DCM owner UNKNOWN; TX/ACK/write DENY.