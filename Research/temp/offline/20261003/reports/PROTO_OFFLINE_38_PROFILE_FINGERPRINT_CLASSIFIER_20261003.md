# PROTO-OFFLINE-38 — ABI/profile fingerprint classifier

**Date:** 2026-10-03  
**Status:** **COMPLETE / POSITIVE**  
**Hypothesis:** a small set of independently observed ABI/topology features can classify captures into broad protocol families and prevent accidental cross-profile semantic/page-shape reuse.  
**Controlled change:** offline classifier/tooling only. No device TX, YAML change, reboot or setting write.

## Classifier features

Primary features:

- physical backend:
  - legacy `A5`;
  - modern `0x1E`;
- configuration page shapes:
  - `03E8/13` vs `03E8/14`;
  - `0410/21` vs `0410/22`;
  - `0492/9` vs `0492/11`;
  - `051E/9` vs `051E/10`;
- topology fingerprint:
  - `0867=0016` legacy;
  - `0867=00E8` modern;
- secondary mailbox hint:
  - W5 6/7 legacy-like;
  - W5 0 Eco5-like.

W5 is deliberately low-weight because PROTO34 proves it is profile/session metadata rather than a universal model discriminator.

## Result

Seven available captures were classified:

- five -> **LEGACY_A5_DCM03_FAMILY**
- two -> **MODERN_1E_FAMILY**
- zero -> ambiguous/mixed.

The 2026-10-03 capture also falls cleanly into the legacy A5/DCM03 family using:
`A5 + 03E8/13 + 0410/21 + 0492/9 + 051E/9 + 0867=0016 + W5=6`.

## Important limitation

The classifier identifies **protocol/ABI family**, not exact heat-pump model.

It must not turn:

`MODERN_1E_FAMILY`

into “therefore XTR M”, nor:

`LEGACY_A5_DCM03_FAMILY`

into “therefore ATEC”.

Exact model identity still requires independent provenance.

## Safety value

Tooling can now refuse silent cross-profile reuse:

- legacy page counts must not seed modern XTR/Eco5 page responses;
- modern `0x1E` payload semantics must not be replayed into A5-family captures;
- W5 alone cannot select a profile;
- equal page address does not imply equal schema.

## Deliverable

`Research/temp/tools/thermia_profile_fingerprint.py`

is an offline-only deterministic classifier.

## Live status

Unchanged:
- EXP387 COMPLETE / POSITIVE
- EXP388 RUNNING / PARTIAL
