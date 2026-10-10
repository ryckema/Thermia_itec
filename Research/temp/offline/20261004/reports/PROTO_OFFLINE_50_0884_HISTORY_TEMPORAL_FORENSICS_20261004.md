# PROTO-OFFLINE-50 — `0884` alarm/history temporal forensics

**Date:** 2026-10-04  
**Status:** **COMPLETE / POSITIVE FOR RECORD LIFECYCLE; NEGATIVE FOR RAW-ID SEMANTICS**  
**Hypothesis:** repeated `0884/count60` publications may reveal whether the page is an event edge or a periodically re-published rolling-history snapshot, and whether record replacement/rollover is visible in the current captures.  
**Controlled change:** offline temporal comparison only.

## Observed repetition

The strongest repeated examples are:

- legacy 20260925_071517: **4 identical payloads** over **63.569 s**, median repeat interval **21.248 s**;
- ATEC/DCM03: **12 identical payloads** over **233.266 s**, median repeat interval **20.995 s**.

Every observed repeated `0884` publication is ACKed.

### Strong conclusion

`0884/count60` is not merely a one-shot “new alarm just happened” notification.

The controller can periodically republish an **unchanged history snapshot** for minutes.

This is consistent with a rolling history/status page.

## Record ordering

For both decoded layouts:

- legacy/ATEC `10 × 6 words`;
- modern Eco5 `8 × 7 words + 4-word trailer`;

the valid timestamps are ordered **newest to oldest**.

Equal timestamps occur for multiple raw IDs, so timestamp equality does not imply duplicate records; multiple events can share one minute.

## Cross-profile lifecycle

The ATEC history payload is byte-for-byte the same legacy-layout snapshot seen in the older legacy references, while the new ATEC capture republishes it repeatedly.

Modern Eco5 uses the different 8×7+4 ABI already identified in PROTO14.

No capture contains an `0884` payload transition during the captured window, so this pass cannot prove:

- insertion position when a new event occurs;
- whether records shift or ring-buffer in place;
- clear/ack behavior;
- trailer generation/count semantics.

## Relationship to `085F`

The history snapshot can be non-empty and repeatedly published while `085F` remains zero/independent in the relevant corpus.

This preserves PROTO24's conclusion: `085F` is not simply the newest `0884` record mirrored elsewhere.

## Raw IDs

No new labelled alarm edge exists.

Therefore raw IDs such as `002C`, `1400`, `0172`, etc. still cannot be safely mapped to displayed Thermia E-codes or alarm names.

## Result

**New durable lifecycle finding:** `0884` is a periodically re-published, newest-first history snapshot.

**Still OPEN:** raw event identity and record-update mechanics.

## Live status

Unchanged.