# PROTO-OFFLINE-32 — genuine Eco5 challenge-generator deep reduction

**Date:** 2026-10-03  
**Status:** **COMPLETE / NEGATIVE** — no deterministic low-complexity generator field was recovered.  
**Hypothesis:** the 16-byte genuine Eco5 `071C/0730` request body may expose a counter, timestamp, rolling field or simple PRNG relation that can be reduced offline.  
**Controlled change:** offline analysis only; no device TX, YAML change, reboot or setting write.

## Corpus

163 genuine Eco5 challenge requests:
- 99 from 2026-09-26;
- 64 from 2026-09-28;
- seven boot/session segments: 29, 41, 29, 29, 3, 3, 29 requests.

## Distribution

Across all 2,608 challenge bytes:
- one-bit fraction = **0.4936**, close to balanced;
- per-byte-position entropy is **6.62..6.91 bits** in the 163-sample corpus;
- each byte position takes **109..129 distinct values**.

No byte position is constant or low-cardinality.

## Consecutive-request diffusion

Consecutive 16-byte request Hamming distance:
- mean **64.30 / 128 bits**;
- range **0..80**;
- the sole zero-distance event is the already identified exact duplicate at consecutive #26/#27 in the final 2026-09-26 boot.

Apart from that duplicate, successive requests look high-diffusion.

## Counter/timestamp search

Each byte position was correlated against challenge ordinal within every long boot segment.

No position behaves as a stable monotonic counter:
- apparent moderate correlations occur only in isolated segments;
- the same byte position changes sign or loses correlation in other boots;
- no byte gives a consistent ordinal/time relation across the five long segments.

No fixed BCD-like date/time field analogous to the separately observed local-XTR structured request samples is present in these genuine Eco5 request bodies.

### Important cross-model distinction

Current evidence therefore supports **different request-body behavior by system/profile**:
- local XTR samples previously showed structured/timestamp-related byte positions;
- genuine Eco5 challenge bodies in these captures are high-diffusion and do not expose that same layout.

Do not use the local-XTR timestamp interpretation as a universal Thermia challenge format.

## Simple generator models rejected

The corpus does not support:
- fixed-byte fields;
- one-byte ordinal counter;
- simple per-position linear increment with ordinal;
- guaranteed fresh unique nonce;
- direct timestamp encoding in fixed byte positions.

A cryptographic PRNG/MAC-oriented internal generator remains possible, but is not proven.

## Strong conclusion

Further algebraic work on the 163 request bodies alone has low expected value. The highest-value path to the generator/response logic remains firmware/app/protocol-package acquisition.

## Live status

Unchanged:
- EXP387 COMPLETE / POSITIVE
- EXP388 RUNNING / PARTIAL
