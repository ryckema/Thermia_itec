# PROTO-OFFLINE-61 — Model-to-code conformance audit

**Date:** 2026-10-04  
**Status:** **COMPLETE / POSITIVE WITH THREE KNOWN ACK-POLICY DEVIATIONS**  
**Hypothesis:** every actual TX route in Write Beta v4.1 should map to a route authorized or explicitly represented by the PROTO60 formal model; any uncovered TX class would be a new safety defect.  
**Controlled change:** static source/model audit only. No device TX, no YAML modification, no compile/flash.

## Result

The current source contains **58 explicit UART TX sites**, reduced to six route classes:

- 2 FC17 approval/R1 response TX sites;
- 32 ordered bootstrap FC16 ACK TX sites;
- 1 legacy retained/export-resume 04A6 ACK;
- 1 generic runtime FC16 ACK builder;
- 18 0708 mailbox response sites;
- 4 semantic full-page FC03 response sites.

**58/58 TX sites are accounted for. No seventh/unmodeled TX class was found.**

The only full-page setting-bearing TX sites are `042E`, `0442`, `0546`, and `03E8`; all are already represented by the formal desired-transaction model and current proven selector set. No symmetry-only calendar response, unknown selector, broad register writer, or second semantic response route was found.

## Known conformance debt

The audit reproduces the already-known three runtime ACK gaps rather than finding a new one:

1. `085F` source permission is broader than the formal contextual model.
2. `0870/count17` remains generically ACKable in v4.1 while the formal model now prefers owned normal-runtime or explicit recovery/rejoin context.
3. generic known configuration pages can still be ACKed outside a specific owning refresh/confirmation state.

`0834/count18` remains separately capture-only. The special `04A6` resume ACK is behind legacy resume scaffolding that normal Thermia Write does not arm.

## State-model result

PROTO60's state7 distinction is represented in source by the separate `write_delayed_refresh_pending` flag. The sole-owner invariant is still distributed across dispatcher guards rather than enforced by one global assertion, but PROTO57 already proves mixed-owner states unreachable in the modeled current graph.

## Strong conclusions

- **0 new unmodeled TX routes.**
- **4/4 semantic value-response TX classes conform to the formal model.**
- The formal PROTO60 model is sufficiently complete to act as a source-audit contract.
- Remaining debt is concentrated in already-known ACK-context policy and cleanup/refactoring.

## Limitation

This is static source conformance, not compiler/binary control-flow proof.

## Live status

Unchanged: EXP387 COMPLETE / POSITIVE; EXP388 RUNNING / PARTIAL; EXP383 PREPARED / NOT RUN.