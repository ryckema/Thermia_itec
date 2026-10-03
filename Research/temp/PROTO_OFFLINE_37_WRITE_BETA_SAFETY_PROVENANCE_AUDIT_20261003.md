# PROTO-OFFLINE-37 — Write Beta v4.1 safety / provenance audit

**Date:** 2026-10-03  
**Status:** **COMPLETE / POSITIVE with one hardening candidate**  
**Hypothesis:** every TX route in the current Write Beta can be tied to current evidence and fail-closed guards, and stale evidence labels can be corrected without changing production behavior.  
**Controlled change:** static offline audit. Only comments/log provenance strings are corrected; no TX logic, frame, selector, ACK policy, guard threshold or HA control behavior is changed.

## Scope

Current baseline audited:

`Write (Beta)/thermia_itec_xtr_m_waveshare_write_beta_v4_1.yaml`

The file contains 58 `write_array(...)` call sites covering:
- exact bootstrap/config ACKs;
- fixed R1 session response;
- idle/runtime `0708`;
- current-page refresh selectors;
- desired-page selectors;
- dynamically generated one-word full-page desired responses;
- guarded runtime ACKs.

PROTO28–30 and PROTO34 are used as the current provenance baseline.

## Positive findings

### Session entry
The fixed `071C/0730` R1 replay remains bounded by the established local XTR cold-start/session guards. No generic challenge answering path exists.

### Bootstrap
The exact 32-page address/count ACK family is hard-coded with known CRCs. ACKs inject no setting values.

### Desired-state paths
Current code follows the evidence-backed primitive:

`fresh controller page -> proven selector -> FC03 pull -> one-word mutation -> full-page response -> exact FC16 republish verification`.

Production `03E8` and the page-specific `042E/0442/0546` controls retain page freshness, transaction-budget and concurrency guards.

### Runtime
- `04A6` remains capture-only in ordinary runtime, with only the explicit one-shot export-resume discriminator allowed.
- `0834` remains fail-closed because local XTR ACK permission has not been independently proven.
- `085F` ACK permission is payload-scoped to the two locally proven patterns.
- unknown FC03/FC16 paths stop/capture rather than answer broadly.

### TEST controls
The seven EXP383 candidate controls remain visibly labelled TEST and are not promoted by code presence.

## Stale provenance found and corrected

No behavior change was required.

Corrected in v4.1:
- EXP379 `0442` current/desired selector logs: `HYPOTHESIS` -> `LOCAL_XTR_PROVEN_EXP379`;
- production `03E8` current refresh log: `localXTR=NOT_YET_PROVEN` -> `PROVEN_EXP352`;
- EXP380 selector comment now says local XTR W0b0/W2b0 is proven while genuine Eco5 W0 remains unobserved;
- ambiguous `[EXP383]` labels in the shared `0546` Operation Mode / TEST Link path are changed to `[EXP380/383]`.

These are logging/documentation fixes only.

## One remaining hardening candidate

The runtime handler has an exact `local_config` page-shape allowlist. Outside explicit export-resume mode, recognized config pages can still reach the ACK path by shape.

That has two competing facts:

- it preserves known-good local runtime behavior;
- PROTO29 establishes that **page recognition is not equivalent to ACK permission**, and genuine Eco5 has six bootstrap-only pages that do not participate in its later broad refresh.

Therefore:

> generic runtime config-page ACK permission is a **hardening candidate**, not a confirmed bug.

It should not be tightened offline because that would change known-good production behavior without a live regression. A future live hardening experiment should make ACK permission scheduler/state-qualified page-by-page.

## Safety conclusion

No uncontrolled scan, unknown payload write, broad semantic mutation or symmetry-only desired selector was found.

The current v4.1 behavior remains compatible with the present safety model. The only recommended functional change is deferred pending a dedicated live regression.

## Compile status

No ESPHome compile was performed. This audit does **not** claim compile verification.

## Live status

Unchanged:
- EXP387 COMPLETE / POSITIVE
- EXP388 RUNNING / PARTIAL
