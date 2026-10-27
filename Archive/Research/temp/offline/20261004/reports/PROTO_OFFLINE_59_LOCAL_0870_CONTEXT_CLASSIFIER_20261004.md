# PROTO-OFFLINE-59 — Exact local-XTR `0870` context classifier

**Date:** 2026-10-04  
**Status:** **COMPLETE / POSITIVE — NORMAL-RUNTIME OWNERSHIP TOKEN CANDIDATE DERIVED; RECOVERY-REJOIN QUALIFIER REMAINS OPEN**  
**Hypothesis:** the smallest locally supported `0870` ACK qualifier can be reconstructed from XTR-only experiment history without importing Eco5/ATEC/legacy semantics.  
**Controlled change:** local evidence reduction only. No TX, no YAML change.

## Local baseline

The relevant XTR sequence is now well constrained.

### `0864`-owned path

EXP308 locally proved:

`qualified runtime -> 0864 ACK -> [optional 0708] -> 0870 appears`

with:

- `0864` ACK;
- ~1.47 s later `0708`;
- ~2.09 s after the ACK, `0870/17`.

Later experiments corrected the earlier assumption that `0708` between `0864` and `0870` was anomalous. It is a valid branch.

### all-zero-`085F`-owned direct path

EXP309 proved passively:

`qualified zero-085F ACK -> direct 0870`

with no `0864`.

EXP310 then repeated that branch and actively confirmed one `0870` ACK:

`qualified zero-085F branch -> direct 0870 -> ACK -> ~1.47 s 0708 -> ~2.18 s 0884`

No `0870` retry preceded `0884`.

### sustained runtime

EXP292 retained the `0870` branch in continuous service for 256.276 s / 12 cycles with zero unexpected events.

## Candidate rules rejected

### Mandatory `0864`

**DISPROVEN locally.**

EXP309/310 directly show a legitimate XTR `0870` branch with `0864 Seen=0`.

### `085F` only

Too narrow.

The ordinary `0864 -> 0870` path is also locally established.

### Pure time-since-0708 threshold

Not sufficiently supported as the primary local rule.

PROTO55 showed that recent `0708` is an excellent cross-profile discriminator, but the local experiments do not establish one universal maximum interval for every valid XTR `0870`.

A hard-coded three-second threshold would therefore be an implementation convenience, not a locally proven protocol rule.

## Best-supported local normal-runtime classifier

The smallest evidence-backed abstraction is an **`0870 ownership token`**.

### Token creation

Create one session-scoped, one-shot `0870` token only after a locally proven transition that can own the next `0870`:

1. ACK of a **qualified all-zero `085F/count5`** stage; or
2. ACK of a **qualified `0864/count4`** stage.

### Token preservation

The token may survive the already-proven optional `0708/count6` service exchange between its anchor and `0870`.

It must not be created by:

- page shape alone;
- an unqualified `0870`;
- `0834`;
- unknown FC16/FC03 traffic;
- old-session state.

### ACK condition

Candidate normal-runtime policy:

```text
ACK 0870/count17 only if:
  native session/runtime is qualified
  AND parser/drop/peer-responder integrity is clean
  AND one unconsumed local 0870 ownership token exists
```

### Consumption

Consume the token on the first `0870` ACK.

A repeated `0870` without a new proven owner is then capture-only/fail-closed in the proposed hardening experiment.

Reset the token on:

- controller bus loss/recovery boundary;
- session restart;
- unknown FC16/FC03;
- peer responder detection;
- parser/drop integrity fault;
- explicit writer stop.

## Why this is better than “recent 0708”

It encodes **causal local protocol progress**, not just timing.

It preserves:

- direct zero-085F -> 0870;
- 0864 -> direct 0870;
- 0864 -> 0708 -> 0870.

It also naturally refuses a reconnect-like stream of repeated standalone `0870` frames unless a separate recovery/rejoin state explicitly grants ownership.

## What this does not solve

The token above is the **normal-runtime qualifier**.

PROTO58 still requires a second architectural branch:

`explicit recovery/rejoin -> one 0870 ACK`

The exact local XTR evidence for granting that recovery token does not yet exist as an isolated live branch.

Therefore a future first hardening experiment should test the normal-runtime ownership token only and leave a conservative, explicitly instrumented recovery exception rather than guessing it.

## Safety assessment for future implementation

**Address/page:** `0870/count17`  
**Known effect of the action:** only standard FC16 address/count ACK; no values are injected.  
**Mapping source:** local EXP308/309/310/292.  
**Expected effect:** preserve known native runtime progress while preventing shape-only ACK outside an owned branch.  
**Plausible unintended effect:** a legitimate but previously unseen local `0870` branch could be withheld, causing retry/stall/Online communication error.  
**Rollback:** current Write Beta v4.1 shape-permissive `0870` ACK policy.  
**Semantic setting risk:** none directly; this ACK contains no register values.

## Evidence classification

**PROVEN / locally confirmed**
- `0864` is not mandatory before every XTR `0870`;
- qualified all-zero-085F branch can lead directly to `0870`;
- one qualified direct `0870` ACK progresses to `0708/0884`;
- `0864 -> [0708] -> 0870` is a valid local branch;
- sustained runtime can repeatedly service `0870`.

**STRONGLY SUPPORTED**
- session-scoped one-shot ownership token from zero-085F ACK or 0864 ACK is the smallest current local normal-runtime qualifier.

**OPEN**
- local recovery/rejoin rule that may authorize an `0870` without either normal-runtime anchor;
- whether a genuine lost ACK requires retry handling rather than strict one-shot consumption.

## Live status

Unchanged: EXP387 COMPLETE / POSITIVE; EXP388 RUNNING / PARTIAL; EXP383 PREPARED / NOT RUN.