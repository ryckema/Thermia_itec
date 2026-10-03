# PROTO-OFFLINE-43 — Runtime ACK-context reconstruction

**Date:** 2026-10-03  
**Status:** **COMPLETE / POSITIVE**  
**Scope:** offline evidence analysis only. No bus TX, no YAML change, no live experiment advancement.

## Hypothesis

The ACK-permission debt identified by PROTO-OFFLINE-37 can be reduced by separating page/payload recognition from protocol-state permission for `085F`, `0870`, and controller configuration-page publications.

## Controlled change

Baseline: PROTO-OFFLINE-29 runtime grammar + PROTO-OFFLINE-37 Write Beta v4.1 safety/provenance audit.

New variable: reconstruct the immediate and mailbox context of each relevant controller `0x0F FC16` publication across the seven currently available genuine Online/DCM references, including the new ATEC + classic DCM03 cold-start capture.

## Corpus

Analysed genuine references:

- `thermia_capture_20260924_210001(1).log`
- `thermia_capture_20260925_071517.log`
- `thermia_capture_20260925_090209.log`
- `thermia_capture_20260925_090550.log`
- `itec_eco5_gateway_20260926.log`
- `itec_eco5_gateway_20260928.log`
- `thermia_capture_20261003_165355.log` — ATEC + classic DCM03

## 1. `085F/count5`

Across the seven references:

- **331** controller `085F/count5` publications;
- **20 ACKed**;
- **311 unACKed**.

The payload in the relevant genuine corpus is all-zero; payload identity therefore does not explain ACK permission.

Of the 20 ACKed `085F` publications:

- **14/20** occur within 1 s of an ACKed configuration-page publication;
- **15/20** occur within 3 s of one.

Modern Eco5 evidence shows explicit service-state interaction: an ACKed `085F` while the mailbox reports `W4=0380` is followed by `W4=0300`; a subsequent ACKed `085F`, followed by `0864`, precedes `W4=0200`.

However, W4 bit `0x0080` is not sufficient by itself. The 20260928 Eco5 capture contains many unACKed `085F` repetitions while the last observed W4 still contains that bit.

### Conclusion for `085F`

**PROVEN from genuine traffic:** `085F` is a recurrent overlay whose address and payload can repeat both when ACK is withheld and when ACK is supplied.

**Strong conclusion:** current Write Beta v4.1's `known 085F payload => ACK permitted` rule is broader than genuine gateway behavior.

A future hardened XTR policy should require an explicitly qualified local service/recovery context.

## 2. `0870/count17`

Across the seven references:

- **95** `0870/count17` publications;
- **64 ACKed**;
- **31 unACKed**.

All **31 unACKed** occurrences belong to one legacy reconnect window in `thermia_capture_20260925_090550.log`. The controller repeats the same `0870` image for roughly a minute without receiving an ACK.

At **66.843 s**, one `0870` is finally ACKed. About **1.37 s later** the controller issues `FC03 0708/count6`, and the DCM replies with:

`W2=7FFF, W3=FFFF, W4=0080, W5=0007`.

This is direct evidence that ACKing `0870` can be a state-transition action in a reconnect path, not merely an unconditional page acknowledgement.

In normal modern Eco5 runtime:

- 44/44 observed `0870` publications are ACKed;
- the preceding answered `0708` is normally very recent.

ATEC steady runtime likewise ACKs all 12 observed `0870` publications.

### Conclusion for `0870`

`0870` is normally ACKed runtime traffic, but the legacy reconnect window proves that page shape alone is not universal ACK permission.

A future hardened XTR policy should distinguish qualified normal runtime from explicitly qualified retained/recovery entry.

## 3. Configuration pages during runtime / synchronization

The corpus contains many known configuration-page shapes that are deliberately not ACKed in some states.

| Page | Total publications | ACKed | UnACKed |
|---|---:|---:|---:|
| `03E8` | 220 | 18 | **202** |
| `04A6` | 586 | 19 | **567** |
| `04BA` | 44 | 17 | **27** |
| `06F4` | 27 | 26 | 1 |

Known page shape alone is therefore not permission to ACK.

## Evidence-based ACK policy model

### Configuration FC16

ACK only when one of these states explicitly owns the page:

- ordered bootstrap, exact expected page/count;
- explicit current-page refresh with the corresponding page pending;
- exact desired-state confirmation/republish;
- explicitly qualified retained export-resume sequence.

Otherwise: capture-only.

### `085F`

Recognize the page/payload separately from permission. ACK only in a locally proven service/recovery state.

### `0870`

ACK in qualified normal runtime or in an explicit locally proven recovery branch.

## Result

**COMPLETE / POSITIVE.**

PROTO43 materially sharpens the three safety-debt items from PROTO37. It does not prove one universal cross-model boolean predicate, but it does prove that the safe abstraction is **state-qualified permission**, not shape/payload-driven permission.

## Live state

Unchanged:

- EXP387 — COMPLETE / POSITIVE
- EXP388 — RUNNING / PARTIAL
- EXP383 — PREPARED / NOT RUN
