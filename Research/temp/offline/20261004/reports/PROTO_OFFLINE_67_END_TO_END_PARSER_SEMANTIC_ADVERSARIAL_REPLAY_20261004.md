# PROTO-OFFLINE-67 — Parser + semantic-state end-to-end adversarial replay

**Date:** 2026-10-04  
**Status:** **COMPLETE / POSITIVE — FRAME-GAP FINALIZATION ELIMINATES THE TESTED AMBIGUOUS-PREFIX SEMANTIC TX PATH**  
**Hypothesis:** coupling parser output to the semantic authorization state machine will show whether PROTO63's ambiguous prefix can actually cross the final setting-bearing TX boundary, and whether RTU/frame-gap-aware finalization removes that path without breaking genuine traffic.  
**Controlled change:** offline end-to-end model only. No YAML change, no bus TX, no compile/flash.

## Baseline

The current YAML uses:

- 9600 baud, 8E1;
- UART debug `after: timeout: 5ms`;
- a pending stream assembler that can process a CRC-valid candidate before a longer candidate is complete;
- semantic state guards that only answer an expected page while the matching engine is waiting.

PROTO66 showed that merely changing shortest-vs-longest ordering is not sufficient under arbitrary chunk delivery.

## Gap-aware shadow policy

For this experiment the shadow parser:

1. buffers bytes belonging to one RTU/silence-delimited frame;
2. allows arbitrary internal callback/chunk splitting;
3. finalizes only at the simulated frame-gap boundary;
4. accepts the whole frame only if its complete length is structurally valid and CRC-valid;
5. never creates a semantic request from a shorter prefix of that completed frame.

The semantic engine is still required to match the exact expected page, cache validity and one-response budget.

## Genuine corpus regression

Seven genuine Online/DCM captures were replayed with 20 randomized internal chunkings each.

Exact capture-frame reconstruction:

**140/140 PASS**

No genuine frame was rejected.

This uses the recorded capture frame boundary as the RTU-gap oracle; it does not claim the current ESPHome callback always exposes boundaries this cleanly.

## Adversarial replay

**50000** cases were generated from the three deterministic double-valid frames:

- `042E/count15`
- `0442/count13`
- `0546/count20`

Variations included:

- split immediately after the CRC-valid 8-byte semantic prefix;
- whole-frame delivery;
- noise prefix;
- duplicate frames;
- delayed final tail bytes;
- matching owner, wrong owner or no semantic owner;
- stale/invalid cache and exhausted response budget controls.

### Setting-bearing TX outcomes

Current shortest-first parser + semantic state:

**17994** setting-bearing TX decisions

Gap-aware framing + same semantic state guards:

**0** setting-bearing TX decisions

Among owner-matching, otherwise-authorized cases:

- cases: **15044**
- current parser setting TX: **17994**
- gap-aware setting TX: **0**

## Positive controls

All four legitimate exact semantic FC03 request frames remain accepted at a real frame boundary:

- 03E8/count14 — PASS
- 042E/count15 — PASS
- 0442/count13 — PASS
- 0546/count20 — PASS

So the safety improvement does not require disabling valid semantic requests.

## Observed facts

- the PROTO63 ambiguity **can** cross the semantic authorization boundary in an offline owner-matching adversarial state if the current parser receives the valid 8-byte prefix before the rest of the longer frame;
- wrong-owner/no-owner/cache/budget guards still block many adversarial cases;
- frame-gap finalization removes every tested ambiguous-prefix setting TX while preserving all positive semantic request controls;
- genuine capture replay remains exact when recorded frame boundaries are used.

## Strong conclusion

The correct hardening boundary is now clearer:

> framing must be finalized before semantic interpretation.

The semantic state machine should not be asked to decide whether an 8-byte prefix is a complete RTU frame.

For a future rewrite, the safest architecture is:

`UART bytes -> RTU gap/framing -> CRC-valid complete frame -> protocol decoder -> semantic owner/expected-page guard -> optional TX`

rather than:

`UART bytes -> first CRC-valid prefix -> semantic interpretation`.

## Safety classification

This remains **offline adversarial proof**, not evidence that the live ESP has ever misparsed genuine Thermia traffic.

PROTO65 found zero such ambiguities in the current genuine corpus.

Therefore this should be fixed during a controlled parser/refactor revision, not mixed into EXP388 recovery testing.

## Live status

Unchanged.