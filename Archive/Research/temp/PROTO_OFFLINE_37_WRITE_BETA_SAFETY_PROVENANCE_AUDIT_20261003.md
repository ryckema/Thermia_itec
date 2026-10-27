# PROTO-OFFLINE-37 — Write Beta v4.1 safety/provenance audit

**Date:** 2026-10-03  
**Status:** **COMPLETE / POSITIVE WITH SAFETY DEBT IDENTIFIED**  
**Hypothesis:** every transmit path in the current Write Beta v4.1 can be traced to explicit protocol evidence, and any route whose permission is broader than the current evidence model can be identified before another live revision.  
**Controlled change:** static YAML audit only. **No YAML behavior was changed**, no compile/flash, no device TX, no reboot and no setting write.

## Scope

The current v4.1 YAML contains **58 explicit `write_array(...)` transmit sites**. They reduce to a much smaller set of protocol actions:

- fixed R1 replay;
- ordered FC16 address/count ACKs;
- qualified runtime FC16 ACKs;
- `0708` idle/current/desired mailbox responses;
- full-page FC03 desired-state responses.

Each route was checked against PROTO-OFFLINE-19/28/29/30/34 and the local EXP results.

## PASS — guarded R1

The fixed R1 replay is still bounded by:
- exact `071C/0730` challenge shape;
- local `A80E=0000/A80F=0005` guard;
- one-shot latch;
- unqualified-session state;
- explicit peer-FC17 abort handling.

No request-specific-crypto claim is made. This matches the locally proven fixed-R1 behavior.

## PASS — cold-start bootstrap ACK chain

The 32-page ACK chain is exact page/count/length gated and ordered. Unexpected page/order causes ACK withholding / stop.

This remains consistent with local XTR bootstrap proof and the genuine Eco5/ATEC structural model.

## PASS — semantic writes

For the proven semantic paths:
- the page must be synchronized from controller FC16;
- cache age is bounded;
- a complete page image is cloned;
- exactly one selected word is changed;
- CRC is rebuilt;
- the following controller FC16 republish is compared against the desired page;
- mismatch/extra-delta paths disable retry.

This matches the strongest current safe-write primitive.

### Proven target families in v4.1

- `03E8/count14` — proven local settings family;
- `042E/count15` — proven local Hot Water family;
- `0442/count13` — proven local Cooling family;
- `0546/count20` — proven local Operation Mode path.

The seven EXP383 candidate controls remain visibly `TEST` and are **not** promoted by code presence.

## PASS — conservative exceptions

### 0834
Runtime `0834/count18` is explicitly capture-only / NO ACK and stops the active writer.

That is conservative and appropriate because Eco5 proves the page is part of normal runtime but its payload is generation-specific and local XTR ACK safety is not established.

### 04A6
Runtime `04A6/count13` is normally capture-only. A one-shot ACK exists only behind the explicit export-resume state inherited from the bounded local EXP363 transport result.

This is narrower than a generic ACK rule.

## Safety debt 1 — 085F ACK permission is too payload-driven

Current v4.1 defines these as locally known:

- all-zero `085F/count5`;
- `0861=0800` variant.

A known payload is then sufficient to place `085F` in `local_runtime_ack_proven`, so it can be ACKed whenever it appears in qualified runtime.

PROTO-OFFLINE-24/29 materially changed the architectural interpretation:

- genuine Eco5 `085F` is overwhelmingly **unACKed** outside service contexts;
- page/payload recognition is not the same as permission to ACK;
- W4/service context matters.

### Audit conclusion

The current rule is **not demonstrated unsafe on the tested local XTR**, but it is broader than the current protocol model.

**Future production revision should require an explicit service/refresh context in addition to the known payload before ACKing 085F.**

No live behavior is changed by this offline audit.

## Safety debt 2 — 0870 ACK is context-blind

`0870/count17` is in the generic local runtime ACK allowlist.

Genuine Eco5 normally ACKs it, but one older reconnect window contains repeated unACKed `0870` publications.

Therefore a future hardened revision should consider context/state rather than page shape alone.

Priority is lower than 085F because normal Eco5 behavior overwhelmingly supports ACK.

## Safety debt 3 — runtime config-page ACK class is broad

The runtime branch recognizes the known configuration page shapes `03E8..06F4` as `local_config` and can ACK them outside the initial staged bootstrap.

PROTO19 established that later configuration refresh is mailbox/work-context driven.

### Audit conclusion

The known page geometry is correct, but **known page shape alone is broader than the latest scheduler provenance**.

A future revision should distinguish:
- autonomous cold-start bootstrap;
- explicit W2/W3/current-page refresh work;
- desired-state confirmation;
- unexpected standalone config-page publication.

Unexpected standalone config traffic should default to capture-only unless a locally proven context permits ACK.

## EXP383 controls

Seven candidate controls remain active code under Home Assistant Configuration and remain labelled `TEST`.

Status remains:

**EXP383 — PREPARED / NOT RUN**

Code availability is not semantic proof.

No automatic promotion or removal is made here because doing so would change the prepared live experiment surface.

## Overall result

No hardcoded CRC/payload error or unproven broad register-value injection was found.

The main result is architectural:

> v4.1 is strong on semantic-page mutation safety, but its runtime ACK permission model still contains three older page/payload-driven allowances that are broader than the newer PROTO29 context-driven model.

Priority for a future Write Beta revision:

1. gate `085F` ACK by explicit service context;
2. make `0870` context-aware;
3. gate runtime configuration-page ACKs by bootstrap/refresh/desired-confirmation state rather than page shape alone.

## Important

This is **not** ESPHome compile verification and does not advance EXP388.

## Live status

- EXP387 COMPLETE / POSITIVE
- EXP388 RUNNING / PARTIAL
- EXP383 PREPARED / NOT RUN
