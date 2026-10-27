# PROTO-OFFLINE-63 — Stream parser / resynchronization fuzzing

**Date:** 2026-10-04  
**Status:** **COMPLETE / POSITIVE FOR RESYNC ROBUSTNESS, WITH A REAL SHORTEST-PREFIX AMBIGUITY IDENTIFIED**  
**Hypothesis:** source-faithful fuzzing of the v4.1 Modbus RTU stream assembler should reject malformed/noisy traffic without creating an unintended semantic request shape.  
**Controlled change:** offline parser transcription and fuzzing only. No device TX, YAML change or compile/flash.

## Parser model

The fuzzer transcribes the current assembler at source lines ~6078..6171:

- known-slave and known-function filter;
- candidate lengths per Modbus function;
- candidate lengths sorted shortest-first;
- CRC validation;
- byte-at-a-time resync;
- >512 pending drop and >4096 callback-buffer clear behavior.

## General fuzz result

- exact valid-frame random chunk-split checks: **160 PASS**
- randomized mutation/fragmentation/noise cases: **60000**
- parsed frames during fuzz: **57746**
- parser resync steps: **11023**
- buffer drops: **0**
- parsed semantic-request-shaped frames from reframed/non-identical fuzz inputs: **25903**

Most malformed traffic is handled conservatively by CRC rejection/resync. No parser crash or unbounded buffer behavior was observed in the host transcription.


## Targeted non-semantic fuzz control

A second deterministic fuzz pass used **100000 cases built only from non-semantic seed frames** (FC16 publications/ACKs, FC17 challenge, normal 0708 response) and never inserted a genuine desired FC03 request as a seed.

Semantic-request-shaped parser outputs found in that control:

**0**

This separates ordinary recovery of a genuine semantic request embedded in noisy concatenation from true accidental synthesis/reframing. The large semantic-shaped count in the broad fuzz run is therefore dominated by test cases that deliberately contained a genuine semantic-request seed.

The important safety finding remains the deliberately constructed double-valid FC03 response/prefix ambiguity, which does not depend on random fuzz probability.

## Important new finding — CRC-valid shortest-prefix ambiguity

The current assembler sorts candidate lengths and accepts the **first CRC-valid candidate**.

For FC03 it always considers an 8-byte request candidate as well as a byte-count response candidate.

A fully valid longer FC03 response can therefore have a shorter 8-byte prefix that is also CRC-valid and is interpreted as a request.

### Deterministic 0546 construction

A valid 10-byte FC03 response was constructed whose first 8 bytes are simultaneously the exact semantic request:

`0F 03 05 46 00 14 <CRC>`

which the write state machine interprets as:

`FC03 0546/count20`

The assembler emits the 8-byte prefix first and leaves the two trailing bytes to resynchronization.

This does **not** mean a normal Thermia frame is known to trigger the bug. The constructed response is synthetic and requires a very specific payload/CRC coincidence.

But it proves the parser property:

**CRC validity alone does not uniquely disambiguate request-vs-response when multiple candidate lengths share a prefix.**

Ambiguity search for the constrained `042E` and `0442` bytecount-4 forms:
- `042E`: **FOUND**
- `0442`: **FOUND**

## Safety consequence

The semantic state guards substantially limit practical impact: an ambiguous parsed FC03 prefix only reaches a full-page desired response if the corresponding semantic engine is already waiting for exactly that page.

Nevertheless this is a genuine parser-level defensive gap. A future rebuild should not rely solely on “shortest CRC-valid candidate”.

Safer design options include:

1. transaction-direction/context qualification before accepting an 8-byte FC03 request for slave `0x0F`;
2. when a longer structurally plausible candidate is already complete, prefer protocol/session context rather than shortest length;
3. treat ambiguous multi-candidate CRC-valid prefixes as fail-closed during semantic states.

## Random-fuzz interpretation

Random reframings that emitted semantic-shaped requests are not automatically semantic-TX bugs; many are cases where a genuine semantic request seed was embedded in noise/concatenation and correctly recovered by the parser.

The deterministic 0546 construction is the stronger result because the **original full input is a different valid Modbus frame**, yet the parser chooses the semantic-request prefix.

## Strong conclusions

- Parser resync is robust against ordinary fragmentation/noise in this host fuzz.
- **A real structural ambiguity exists in shortest-first candidate selection.**
- This should be carried into EXP388-R2 / future parser cleanup as defensive hardening.
- Do not change the live parser solely from this offline result without regression against genuine captures.

## Unknowns

- whether any genuine Thermia frame in the available corpus has such a double-valid prefix;
- whether UART direction/physical bus topology makes the constructed response impossible in the exact semantic waiting state;
- compiler/runtime timing effects.

## Live status

Unchanged.