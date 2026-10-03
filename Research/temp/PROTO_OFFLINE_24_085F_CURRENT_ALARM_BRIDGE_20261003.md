# PROTO-OFFLINE-24 — 085F / current-alarm bridge reduction

**Date:** 2026-10-03  
**Status:** **COMPLETE / NEGATIVE** — no native current-alarm bridge could be identified from the available capture corpus.  
**Hypothesis:** `085F/count5` or a tightly coupled runtime field may carry the current alarm/error state corresponding to the separate `0884/count60` timestamped history layer.  
**Controlled change:** offline correlation only; no bus TX, YAML change, reboot or setting write.

## Corpus

All six genuine Online/DCM reference captures were re-scanned for:
- `085F/count5`;
- `0884/count60`;
- nearby runtime/service pages;
- value transitions around history publication.

## Observed facts

- `085F/count5` occurs **339 times** in the four captures where it is present.
- Every one of those **339/339 payloads is exactly**:
  `0000 0000 0000 0000 0000`.
- Two older reference captures contain no `085F` frame in the captured windows.
- Non-empty `0884` history exists while `085F` remains all-zero:
  - legacy history newest raw event `0x0002`;
  - Eco5 2026-09-26 newest raw A/B `0x002C/0x0000`.
- In the legacy captures the `0884` history image is stable while `085F`, when present, stays zero.
- The Eco5 2026-09-26 history page is non-empty while all 197 `085F` publications in that capture are zero.
- No `085F` word transition was available to correlate with a history insertion, current-alarm onset or clear event edge.

## Strong conclusions

1. **`085F` is not a mirror of the newest `0884` history entry.**
2. A non-empty historical alarm/service list does **not** imply non-zero `085F`.
3. The five-word size of `085F` is not evidence that it maps directly to firmware `AlarmField1..5`.
4. The available normal/reference corpus contains no positive edge from which current-alarm semantics can be recovered.
5. The architecture should continue to keep three layers separate:
   - live operating status;
   - current alarm/error state;
   - timestamped historical events.

## What this does not disprove

The result does **not** prove that `085F` can never contain alarm/service data. The corpus lacks a locally labelled active-alarm transition. It remains possible that one or more words become non-zero only under an active alarm, service state or another condition absent here.

Therefore the correct classification remains:

- `085F/count5` page role: **PROVEN runtime/service structural**;
- all-zero normal/reference behavior: **PROVEN in available corpus**;
- current-alarm semantics: **OPEN / UNKNOWN**;
- direct current-history mirror: **DISPROVEN**.

## Smallest future evidence needed

A passive capture containing a clearly timestamped active alarm onset/clear event plus panel/UI alarm identity would be enough to test this bridge safely. No active fault injection is justified.

## Live status

Unchanged:
- EXP387 COMPLETE / POSITIVE
- EXP388 RUNNING / PARTIAL
