# PROTO-OFFLINE-66 — Parser-fix shadow tournament

**Date:** 2026-10-04  
**Status:** **COMPLETE / POSITIVE WITH REFINEMENT — SORT-ORDER-ONLY FIXES ARE INSUFFICIENT UNDER ARBITRARY CHUNKING**  
**Hypothesis:** candidate parser ambiguity policies can be compared offline against all genuine captures and the PROTO63 double-valid adversarial frames without changing v4.1.  
**Controlled change:** shadow parser policy only. No YAML change, no TX, no compile/flash.

## Policies

1. `shortest` — current v4.1 behavior.
2. `longest` — choose the longest CRC-valid complete candidate.
3. `ambiguous_failclosed` — reject/resync if more than one CRC-valid candidate is simultaneously complete.
4. `semantic_context` — preserve current shortest-first behavior **except**: if the short 8-byte candidate is one of the authorized semantic FC03 desired-page requests and a longer CRC-valid candidate is already complete, do not accept the short request; choose the longer complete frame.

## Genuine-corpus replay

Seven genuine capture files were converted to concatenated byte streams and replayed with 20 randomized chunkings each.

Exact frame reconstruction:

- current shortest: **140/140**
- prefer longest: **140/140**
- ambiguous fail-closed: **140/140**
- semantic-context guard: **140/140**

Because PROTO65 found zero genuine double-valid candidates, all four policies are behavior-equivalent on the current genuine corpus.

## Deliberate double-valid adversarial frames

Three valid longer FC03 frames were used, each with an 8-byte CRC-valid prefix equal to a current semantic desired-page request:

- `0546/count20`
- `042E/count15`
- `0442/count13`

Across 100 randomized chunkings per case:

- current shortest false semantic outputs: **300**
- prefer longest false semantic outputs: **160**
- ambiguous fail-closed false semantic outputs: **160**
- semantic-context false semantic outputs: **160**

Exact preservation of the original longer valid frames:

- shortest: **0/300**
- longest: **140/300**
- ambiguous fail-closed: **0/300**
- semantic-context: **140/300**

## 30,000 noisy adversarial wrappers

False semantic outputs:

- shortest: **28486**
- longest: **7587**
- ambiguous fail-closed: **7436**
- semantic-context: **7462**

## Decision

The first shadow tournament exposes an important refinement.

When the **entire ambiguous 9/10-byte frame is already present**, `longest` and `semantic_context` preserve the valid long frame while current `shortest` does not.

But under deliberately arbitrary byte-chunk delivery, **none of the policies that decide immediately on the first CRC-valid 8-byte prefix is sufficient**. If the first callback/chunk ends exactly after the 8-byte prefix, the longer candidate is not complete yet, so even `longest`, `ambiguous_failclosed`, and the first `semantic_context` formulation can accept the semantic request before the final response byte(s) arrive.

This explains the non-zero adversarial false-semantic counts above and supersedes the initial “semantic_context is the winner” interpretation.

## Strong conclusion

A robust parser fix needs **deferral/context**, not merely a different sort order.

The best-supported future design is:

1. treat an 8-byte semantic FC03 request as **provisional** when its first bytes also define a plausible longer FC03 response length;
2. finalize it only at an RTU/frame-gap boundary **or** when transport/session context proves no continuation belongs to the same frame;
3. if the longer CRC-valid candidate completes before that boundary, prefer the complete longer frame;
4. after framing, the semantic transaction engine must still require the exact expected page/owner.

This fits the actual YAML architecture particularly well because UART debug already uses `after: timeout: 5ms`, while the bus is 9600 8E1. For short 8–10 byte frames, frame-gap-aware finalization is a narrower safety change than globally preferring longest candidates.

## Important limitation

The randomized chunk tournament is intentionally harsher than the observed ESPHome callback behavior. It proves what can happen **if** a semantic 8-byte prefix is delivered before the remaining response bytes; it does not prove that the current 5 ms UART-debug callback actually splits 8–10 byte Thermia frames this way.

PROTO65 still found zero ambiguity in 25,031 genuine CRC-valid Online/DCM frames.

No live behavior is changed by PROTO66.