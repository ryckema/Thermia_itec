# PROTO-OFFLINE-48 — Edge-based unresolved-register correlation

**Date:** 2026-10-04  
**Status:** **COMPLETE / NEGATIVE FOR NEW SEMANTIC PROMOTIONS; POSITIVE RECONFIRMATION OF ABI/TIME BEHAVIOR**  
**Hypothesis:** event/edge timing may distinguish unresolved register semantics that static value-domain comparison could not resolve.  
**Controlled change:** examine only value transitions of unresolved fields and correlate runtime edges with the latest known compressor/outdoor-unit state. Offline only.

## Settings fields

Tested unresolved settings fields:

`03F1`, `03F2`, `03F3`, `03F5`, `0431`, `0432`, `0447`.

Across **1210 observed field samples** in the available raw corpus, the number of within-capture value edges is:

**0**.

So the existing captures contain no event timing capable of assigning a semantic label to any of those fields.

This is a real evidence ceiling, not a failed parser.

The no-edge result does strengthen the profile interpretation from PROTO47:

- `03F3` remains fixed at `60` in legacy/ATEC and `1` in Eco5/XTR;
- `03F5` remains fixed at `2` in modern Eco5/XTR;
- `0431/0432/0447` remain fixed but profile-dependent.

## Runtime `0874` / `0875`

Across all available genuine `0870/count17` pages:

- `0874` edges observed: **0**;
- `0875` edges observed: **0**.

`0875 == 0873` remains true in the existing reference corpus, but there is no actual `0873/0875` counter edge in the available time windows to establish whether both fields update atomically over a real cooling-hour increment.

`0874` also never changes in the current windows.

Therefore neither receives a new semantic promotion.

## Runtime `087D`

`087D` produces **5** observed +1 edges in the Eco5 long capture.

For every edge, the latest known:

- `0865 compressor-running = 1`;
- `07F4 normalized outdoor state = 6`.

**Reconfirmed strong conclusion:** `087D` is a running-time accumulator tied to active compressor operation, consistent with the defrost-runtime family. This adds no new semantic name beyond PROTO35/36.

## Result

No unresolved field gains a safe new user-facing label.

The strongest new information from this pass is negative:

- the present corpus is insufficient to decode `03F1/03F2/03F3/03F5/0431/0432/0447/0874`;
- `0875` remains a proven structural duplicate of `0873`, not a separately proven semantic register.

## Live status

Unchanged: EXP387 COMPLETE / POSITIVE; EXP388 RUNNING / PARTIAL; EXP383 PREPARED / NOT RUN.