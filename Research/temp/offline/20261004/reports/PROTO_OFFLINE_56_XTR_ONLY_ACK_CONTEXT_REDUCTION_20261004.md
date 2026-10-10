# PROTO-OFFLINE-56 — XTR-only ACK-context reduction

**Date:** 2026-10-04  
**Status:** **COMPLETE / POSITIVE — LOCAL CONTEXT MODEL NARROWED**  
**Hypothesis:** removing all cross-model evidence and using only locally confirmed XTR experiments will show which ACK permissions are genuinely supported on this unit and which parts of the current generic allowlists remain broader than local proof.  
**Controlled change:** evidence reduction only. No bus TX, YAML change, compile/flash, controller restart or setting write.

## Evidence scope

Only local XTR evidence is admitted:

- completed local EXP-series results in the canonical experiment log;
- the current local passive `thermia-logs.txt` fixture;
- current Write Beta behavior is used only to identify which permission class is being discussed.

Genuine Eco5, legacy A5 and ATEC/DCM03 captures are deliberately excluded from the conclusions below except where explicitly mentioned as *not used*.

## 1. `085F/count5`

### Locally proven positive contexts

The all-zero payload is not merely cross-model evidence. It is locally ACK-proven multiple times:

- EXP307: after `085F(0800)` normalization + fresh `0708`, one zero-085F ACK led to `0708` and then `0864`;
- EXP319: qualified zero-085F ACK led directly to `0884`;
- EXP280: post-0848/runtime zero-085F ACK led to `0864`;
- EXP335: post-bootstrap-tail zero-085F ACK led to `0708`;
- EXP386: fresh post-recovery zero-085F ACK + fresh `0708` completed local runtime qualification.

The `0861=0x0800` payload is also locally proven ACKable:

- EXP318: ACK of the second qualified `085F(0800)` transitioned to all-zero `085F`.

### Local negative/context evidence

EXP305 shows `085F(0800)` appearing as a transient state after an ACK-gated `0662` transfer without proving that every such occurrence must be ACKed immediately.

The local passive fixture also contains:

- 35 all-zero `085F/count5`;
- 70 `03E8/count14`;
- no answered `0708`;
- no visible approval exchange;
- no ACKs because the logger is passive.

That passive trace cannot prove that ACK must be withheld, but it proves **page shape/payload can exist outside a qualified emulated session**.

### Local conclusion

**PROVEN / locally confirmed:** both currently accepted 085F payload forms are genuinely ACKable on this XTR.

**NOT PROVEN:** “every occurrence of either payload in stage40 is always safe/required to ACK regardless of session/work context.”

So PROTO43's cross-model criticism needs a local nuance: the **payload allowlist itself is locally evidence-backed**; the remaining debt is **context-free use of that allowlist**, not the choice of the two payloads.

## 2. `0870/count17`

Local evidence is stronger than the earlier cross-model-only framing suggested.

### EXP309

After the proven 085F prerequisites, the controller emitted direct `0870/17` without a preceding `0864`.

The experiment intentionally failed closed and did not ACK it.

This proves:

`0864 is not a mandatory local prerequisite for 0870`.

### EXP310

The next bounded test accepted that direct branch.

One qualified live `0870/17` received exactly one standard ACK:

`0F 10 08 70 00 11 02 90`

Observed:

- ~1.47 s later `0708/6`;
- ~2.18 s after ACK, `0884/60`;
- no 0870 retry before 0884;
- transport remained clean.

**PROVEN / locally confirmed:** an `0870` ACK is valid in a qualified retained-runtime context on this XTR.

### Sustained runtime

EXP292 subsequently supported the optional post-0870 `0708` branch in continuous local runtime for 256.276 s / 12 cycles.

### Local conclusion

What is locally proven is not `shape-only 0870 ACK`.

It is:

`qualified native runtime state -> 0870 ACK -> valid runtime continuation`.

There is **no local XTR experiment proving that an unqualified/reconnect-like 0870 should be ACKed solely because address/count match**.

Therefore `0870` remains the cleanest first context-hardening candidate.

The qualification rule cannot require `0864`, because EXP309/310 explicitly disprove that prerequisite.

## 3. Configuration-page ACKs

### Proven local owned contexts

Configuration FC16 ACK is strongly locally proven for:

1. **ordered initial synchronization** — starting with `03E8/count14` after R1 and continuing through the locally established page chain;
2. **current-page refresh** — W3-bit0 request -> controller `03E8/count14` -> fresh authoritative page;
3. **semantic confirmation** — controller exact same-page FC16 republish after a desired-page response.

These three classes are unambiguous local ACK owners.

### Autonomous runtime `03E8`

EXP352 also proves something important:

while no ESP semantic write was pending, the controller independently published a new `03E8/count14` after a native/front-panel change. The emulator promoted that page as the new authoritative cache and the next write correctly used its new value.

Therefore **standalone controller-originated `03E8` runtime publication is locally real**.

The archived result does not isolate “ACK versus no-ACK” as the controlled variable, so it does not prove a universal autonomous-03E8 ACK rule. But it is enough to reject a design assumption that every runtime config page must have been explicitly requested by W2/W3 or a desired transaction.

### `04A6`

Later hardened local production work made runtime `04A6/count13` capture-only / NO ACK. EXP358 and EXP359 completed positively without requiring permissive runtime 04A6 ACK behavior in the tested scope.

So the current special-case NO ACK remains locally supportable.

### Other config pages

Outside bootstrap, explicit current refresh, semantic confirmation, and the observed autonomous `03E8` case, this pass finds no local result proving that arbitrary known config-page shapes must always be ACKed.

### Local conclusion

The broad generic `local_config` fallback is **wider than local proof**, but a universal “must have W2/W3 owner” rule would also be too strict because autonomous runtime `03E8` publication is locally proven.

The eventual safe model likely needs a separate class:

`controller-originated autonomous current-state/config publication`

rather than reducing all config traffic to request ownership.

## 4. `0834/count18`

No local XTR positive ACK experiment is identified.

Current capture-only/fail-closed treatment remains the correct evidence level.

Cross-model ACK frequency is explicitly not used to promote it.

## Observed facts

- both accepted `085F` payload forms have local positive ACK evidence;
- zero-085F has multiple different valid next branches (`0708`, `0864`, `0884`);
- direct `0870` without `0864` is locally observed;
- one qualified direct `0870` ACK is locally proven and advances to valid runtime;
- autonomous runtime `03E8` controller publication is locally observed;
- runtime `04A6` can remain unACKed in successfully completed hardened production regressions;
- `0834` has no local ACK proof.

## Strong conclusions

1. **085F:** keep the two local payload forms as valid evidence; hardening should target *context qualification*, not remove a locally proven payload.
2. **0870:** local proof supports ACK in qualified runtime but does not support universal shape-only permission. This is the strongest first hardening target.
3. **config:** bootstrap/refresh/confirmation ownership is proven, but autonomous current-state publication also exists locally; a correct future policy needs an autonomous-push state.
4. **0834:** remain capture-only until separately locally proven.

## What remains unknown locally

- exact predicate that distinguishes an `0870` normal-runtime instance from a reconnect/rejoin instance before ACK;
- whether every qualified zero/0800 `085F` should be ACKed immediately;
- which config pages besides `03E8` can be autonomously pushed during local runtime;
- whether autonomous `03E8` requires an ACK for controller progress or is merely tolerant of one.

## Safety implication

If a live ACK-hardening experiment is prepared after EXP388:

- change **0870 only** first;
- do not require `0864` as prerequisite;
- preserve the already locally proven qualified-runtime `0870` path;
- leave `085F`, config and `0834` policy otherwise unchanged;
- rollback is current Write Beta v4.1.

## Live status

Unchanged:

- EXP387 — COMPLETE / POSITIVE
- EXP388 — RUNNING / PARTIAL
- EXP383 — PREPARED / NOT RUN