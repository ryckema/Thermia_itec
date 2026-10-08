## 2026-10-08 H012 supplementary findings (independent offline study)

**GENUINE CROSS-MODEL / OFFLINE OBSERVED:** 321 genuine all-zero `085F/5` requests, 10 ACK, 311 no matched ACK; in an analyst-chosen five-second preceding-ACK window, 9/10 positive and 0/311 negative cases matched. **COUNTEREXAMPLE:** one genuine Eco5 2026-09-28 `085F` ACK lacked a preceding captured ACK within five seconds; a fixed recency predicate is not necessary and is **not proven safe as sufficient**. Observed first later FC16 family after 10 ACKs: `07D0` (4), `03E8` (3), `0864` (2), `085F` (1); do not treat ordering as causation. H012 validated its own offline census/invariants (14/14), not a live XTR ACK rule. **STATUS:** COMPLETE / POSITIVE offline counts/falsification; INCONCLUSIVE for owner authorization. S11Y-AA remains NOT RUN, all unmatched page owners **CAPTURE_ONLY**.

# 2026-10-08 (late) — S11Y-AA..AD retained native-service evidence

## PROVEN / locally confirmed (XTR M)
- S11Y-Y FIX2: ACK `0662/33` delivered; first subsequent `085F/5` had all-zero signature, then FC03 `0708/6` appeared without ACK2; ACK2 was withheld by guard, not a valid negative `0864` test.
- S11Y-AA after ESP restart: repeated `085F/5 = 0000 0000 0800 0000 0000` plus `0708/6`, absent `0662/33`; manual ARM refused 23:15:21.637 and TX=0. AA's active two-ACK hypothesis is **NOT RUN**.
- Original S11B: two physically delivered ACKs (`0662`, `085F`) followed by `0708` and `0864`; exact pre-TX2 `085F` bytes were not separately logged.
- S11Y-AD offline classifier: 9/9 tested log/ambiguity/health fixtures passed with no transmission authority; **not** a locally verified live classifier.

## STRONGLY SUPPORTED
- S11B's second ACK probably applied to an **already all-zero** `085F`: its receive-event page report is all-zero after TX2 in callback order. Preserve historic facts; supersede prior literal `ACK085F(0800)` shorthand, not the observed ACK/next page.
- Identical visible `085F(0800)+0708` after different preceding events or ESP restarts is **not** proof of the same internal controller epoch/owner. Passive recognition and reply authorization are separate.
- A single payload signature, page shape or W4 bit is insufficient to choose `0884`, `07D0` or `0864` as universally next.

## FIRMWARE-DERIVED / GENUINE CROSS-MODEL
- Applicable Connect profiles label `0861.bit11` (`0x0800`) Online/internet-gateway communication-error; no independent local XTR UI correlation, no proven causality.
- Genuine different-model Eco5/ATEC Online/DCM: 321 all-zero `085F/5` requests, 10 ACKs, and different next-owner branches `0864` versus `07D0`. These do **not** authorize an XTR `085F` ACK.
- Observed Connect software timeouts describe serial/application supervision, not a proven heat-pump-controller `0662` reset.

## HYPOTHESIS
Outstanding selector requests, work priority and *observed* predecessor ACK/response history jointly affect subsequent FC16 page order. `0861.bit11` may signal gateway communication trouble on XTR, but profile semantics are not local confirmation.

## OPEN / UNKNOWN
True retained internal owner; a safe exact `085F` ACK predicate in present controller context; conditional `0864`/`07D0`/`0884` ordering; robust restart/rejoin; XTR display/alarm mapping; native settings write read-back.

## DISPROVEN / SUPERSEDED
“TX2 in S11B definitely ACKed W2=0800” superseded as **interpretation**; all-zero pre-TX2 is supported but not separately raw-proven. Universal “all-zero `085F` permits ACK / forces `0864`” contradicted by genuine context variation. ESP reset necessarily restarts controller at `0662` unsupported.

Default remains **CAPTURE_ONLY** with unchanged production HA, parser/health bookkeeping and strict guards. See [redacted S11Y-AA..AD dossier](protocol%20reduction/S11Y_AA_AD_PASSIVE_SESSION_RECONCILIATION_20261008.md).

---

# 2026-10-08 — Passive 07D0 content, 07DF periodicity and owner-context reconciliation

## PROVEN / locally confirmed
- FIX8H, FIX8I, FIX8J and the actually run FIX8K show repeated `0x0F FC16 07D0/count19` with `FC03 0708/count6` continuing without a response from the ESP; passive physical TX counters remain 0 and bus/parser fault counters remain 0. This proves **observable retransmission in the local capture context**, not Online-session completion.
- FIX8J directly measured repeatable `07DF` bit `0x0020` edges: approximately 64.7 s between rising edges, with ~17.2 s high and ~47.5 s low in the observed steady-state runs. FIX8K reproduced the changes. Meaning/function **not** proven.
- FIX8H/FIX8I/FIX8J observed local variation in runtime words including `07D0`, `07D1`, `07D4`, `07DF` and `07E0` across runs; FIX8K observed only `07DF` changes in its latest capture.
- Independent S11X FIX1 local evidence remains valid: a qualified ACK of retained `07D0/count19` released `07E4/count17` after 2041 ms. FIX8K showing `07D0` again on a later date is a **different observed controller epoch**, not evidence against that one-ACK edge.

## STRONGLY SUPPORTED
- Runtime owner, payload contents and periodic status bit must be kept distinct: the same FC16 geometry can recur with different word payloads, and the same apparent owner may persist across an ESP restart in some contexts. Qualification should use exact geometry plus contemporary session/bus context; a payload signature alone is not a universal identity.
- A periodic telemetry bit such as `07DF/0x0020` need not indicate heating, DHW or a completed Online session.

## HYPOTHESIS
- `07DF/0x0020` could be a timer, heartbeat or periodic state flag; no specific semantic claim is validated.
- Other changing 07D0-page words may represent operating values (possibly scaled measurements); no local heating/DHW/idle correlation yet.
- The next owner after a newly qualified retained `07E4/count17` ACK could be `07F8/count17`, but no such new experiment has been run, and the current FIX8K baseline is `07D0`, not `07E4`.

## OPEN / UNKNOWN
- Why the controller is presently at repeated `07D0` after earlier S11X FIX1 observed `07E4`; possible context/session transitions not yet captured and explained.
- Whether any runtime word maps to a specific sensor, status or writable setting.
- Whether a fully functioning native Online/DCM session can be sustained autonomously and safely; one standard FC16 ACK is not semantic write acceptance.
- FIX8K semantic test has **zero manual mode markers**, hence cannot confirm any heating/DHW/idle association.

## DISPROVEN / SUPERSEDED
- **Superseded as a universal claim:** `07DF 0x0020` is definitely a heating/DHW active flag; periodicity alone does not support that.
- **Superseded as a current-baseline assumption:** after S11X FIX1, all subsequent controller epochs must still be at `07E4`. Later passive FIX8K explicitly observes repeated `07D0`.

## Safety and next research
Continue offline genuine Online/DCM capture and Thermia Connect firmware comparison; qualify current owner in passive S11Y-A before considering any **separately authorised** manual, one-shot S11Y-B ACK. No actual Online/DCM module available locally. No new heating/DHW state should be forced solely to produce test data.

---

# 2026-10-07 — Service/runtime chain refinement through S11X FIX1

## PROVEN / locally confirmed

### 0708 response creates the transient all-zero 085F service state
S11U FIX1 locally confirmed that, from the retained `0708 + 085F(W2=0800)` boundary, one source-faithful response to `0708/count6` caused exact all-zero `085F/count5` to appear about 566 ms later.

Status: **PROVEN / locally confirmed**.

### The all-zero 085F state is transient across ESP restart
S11V started after another ESP OTA/restart and the controller had returned to stable `085F(W2=0800) + 0708`; the all-zero state was absent and no TX occurred.

Status: **PROVEN / locally confirmed** that the all-zero state must not be assumed to persist across ESP restart.

### ACK of freshly generated all-zero 085F releases 0884
S11V FIX1 generated the all-zero `085F` and ACKed it within the same uninterrupted run. `0884/count60` appeared about 2355 ms after ACK085F.

Status: **PROVEN / locally confirmed** for the exercised context.

### ACK0884 releases 07D0 in the reconstructed chain
S11W extended that exact chain. After ACK0884, `07D0/count19` appeared about 2039 ms later.

Status: **PROVEN / locally confirmed**.

### 07D0 owner persists across ESP OTA/restart
S11X original began after ESP OTA/restart with repeated `07D0/count19` plus `0708/count6`, while the earlier `085F` entry state was absent. Zero TX occurred.

Status: **PROVEN / locally confirmed** that this runtime owner state can persist on the Thermia/controller side across ESP restart.

### ACK07D0 releases 07E4
S11X FIX1 qualified the retained `07D0/count19` owner and sent exactly one standard address/count ACK. `07E4/count17` appeared 2041 ms later. Accounting was exactly 1/1/1 and remained clean.

Status: **PROVEN / locally confirmed**.

### Reconstructed local route
The following route is now locally exercised across the combined S11U FIX1 -> S11V FIX1 -> S11W -> S11X FIX1 evidence:

`0708 response -> all-zero 085F -> ACK085F -> 0884 -> ACK0884 -> 07D0 -> ACK07D0 -> 07E4`.

S11W proves the portion through `07D0` in one uninterrupted run. S11X original + FIX1 prove persistence and direct continuation from retained `07D0`.

## STRONGLY SUPPORTED

- The native service/runtime mechanism is a contextual pending-work scheduler with a mailbox/service boundary, not a globally rigid page chain.
- A retained runtime owner can be adopted directly after ESP restart when its geometry and surrounding state are strongly qualified; replaying the complete earlier chain is not always necessary.
- Geometry + state/session context should dominate owner qualification. Payload signatures are useful local diagnostics but should not be promoted to universal owner identities.
- The historical runtime ring `07D0 -> 07E4 -> 07F8 -> 080C -> 0820 -> 0848` remains consistent with current local evidence.

## HYPOTHESIS

- The now-retained `07E4/count17` owner can be ACKed directly and should release `07F8/count17` in the current controller epoch.
- Repeated runtime owners may be safely drained one at a time using exact geometry plus retained-owner qualification, but this is not yet a production-safe generic rule.

## OPEN / UNKNOWN

- Whether `07E4 -> ACK -> 07F8` is reproduced directly from the current retained state after the next ESP OTA/restart.
- Whether later runtime owners remain equally persistent across ESP restart.
- Generic authorization rules for automatically resuming arbitrary retained owners.
- Semantic meaning of runtime page words remains open unless separately mapped.
- Context-dependent branches involving `0834`, `0864`, `0870`, and alternate post-`0884` paths remain valid evidence against treating the scheduler as globally linear.

## DISPROVEN / SUPERSEDED

- **Superseded:** every new experiment must reconstruct the service chain from `0708 + 085F(W2=0800)`. S11X shows that a retained runtime owner may survive ESP restart and can be continued directly.
- **Superseded:** the transient all-zero `085F` state is a reliable cross-OTA prerequisite. S11V shows it is not.
- **Superseded as a universal model:** one fixed page order describes every native session. Earlier branch evidence plus the current retained-owner behavior supports contextual scheduling instead.

---

# 2026-10-07 — Scheduler/service refinement through S11U

## PROVEN / locally confirmed

### Retained 0662 owner releases directly to the 0708 mailbox phase
On the local iTec XTR M, a stable retained state existed with repeated `0x0F FC16 0662/count33` and stable `085F/count5 = 0000 0000 0800 0000 0000`, while no `0708` polls were present.

S11T sent exactly one standard address/count ACK to `0662/count33`. After that:
- repeated `0662` stopped;
- first `0x0F FC03 0708/count6` appeared about 1.422 s later;
- `0708` then continued periodically;
- only one ESP TX occurred.

Current status: **PROVEN / locally confirmed** as a scheduler/work-completion edge.

### Post-S11T scheduler state survives ESP restart/OTA
S11U started after ESP OTA with `0708/count6` already active, `085F(W2=0800)` still stable, and `0662/count33` absent. No ESP TX occurred in S11U.

Current status: **PROVEN / locally confirmed** that ESP restart/OTA does not necessarily reset this Thermia-controller scheduler state.

### ACK085F changes state but does not by itself release a different owner
S11R FIX3 locally delivered one standard ACK to stable retained `085F(W2=0800)`. The same `085F/count5` geometry later changed from signature `7EAE5A0A` to `9BFE9A42`, while no different FC16 family appeared within the predeclared 10 s window.

Current status:
- ACK-induced same-geometry state transition: **PROVEN / locally confirmed**.
- "ACK085F alone releases a different FC16 owner within 10 s": **DISPROVEN for the exercised retained context**.

## STRONGLY SUPPORTED

### Signature 9BFE9A42 corresponds to all-zero 085F words
For exact FC16 geometry `0F 10 08 5F 00 05 0A + five words`, the project's signature function maps the known `0000,0000,0800,0000,0000` baseline to `7EAE5A0A`, and five all-zero words to `9BFE9A42`.

S11R FIX3 observed the latter signature after ACK085F. Because that run did not directly print all five post-transition words, the all-zero payload interpretation remains **STRONGLY SUPPORTED**, not directly observed there.

### Ordered service boundary model
The strongest current combined local model is:

`0662 pending -> ACK0662 -> 0708 mailbox phase -> mailbox response -> changed 085F -> ACK085F -> next pending owner`.

Only `ACK0662 -> 0708` and the previously exercised mailbox/085F interactions are individually locally supported/proven in their respective contexts. The entire combined chain has not yet been run end-to-end from the current state.

## HYPOTHESIS

- A source-faithful response to the current retained `0708/count6` phase will cause `085F` to change or expose another controller-owned FC16 family. S11U FIX1 is prepared to test exactly this with one TX and hard capture-only afterward.
- The controller's native Online/DCM path is best modeled as a contextual pending-work scheduler plus service/mailbox boundary rather than one rigid page sequence.

## OPEN / UNKNOWN

- Whether S11U FIX1 produces the expected changed `085F` state from the current post-S11T baseline.
- Whether the exact order `0708 response -> changed 085F -> ACK085F` is mandatory in every retained service context.
- Generic rules for safely auto-draining `0662`, `085F`, `0834`, `0884`, and other owners without overgeneralizing from one epoch.
- Semantic meanings of the individual words in these scheduler/runtime blocks remain open unless separately mapped.

## SUPERSEDED / methodological corrections

- Treating recurrent `0662/count33` as harmless background in all contexts is superseded. S11T proves it can be an active pending work owner whose ACK releases `0708`.
- Requiring the post-ACK `085F` signature `9BFE9A42` to persist across ESP restart is superseded; S11S showed the controller could later be back at stable `7EAE5A0A/W2=0800`.
- Strict pre-click recency gating for `0708` was too fragile in S11R FIX2; post-ARM epoch qualification is preferred.

---

# 2026-10-07 — S11J through S11R retained scheduler refinement

## PROVEN / locally confirmed

- The six-page runtime ring is locally exercised with standard ACK progression:
  `07D0/19 -> 07E4/17 -> 07F8/17 -> 080C/18 -> 0820/18 -> 0848/23`.
- `0834/count18` is now locally ACK-proven in a retained XTR context. In S11Q FIX2, one standard ACK stopped the repeated 0834 owner and exposed different controller-owned traffic.
- The S11Q FIX2 follow-on was `0708/6` then all-zero `085F/5` about 2.02 s after ACK0834.
- A fixed `0834` payload signature is not a valid owner identity: valid `0834/18` payload signatures changed while start/count geometry remained constant.
- The later passive S11R run showed the stable retained `085F/5` state as `0000 0000 0800 0000 0000` with repeated `0708/6`, zero ESP TX, and no all-zero 085F in that supplied run.
- S11O locally confirmed that after ACK0848 the controller can expose another known work family (`0864/4`) rather than a fixed final 085F boundary.
- S11P locally confirmed that after ACK0884 the first runtime owner can be `0834/18` rather than `07D0`.

## STRONGLY SUPPORTED

- The native 0x0F runtime/service mechanism is best modeled as a **contextual pending-work scheduler**, not as one globally fixed page order.
- Ownership qualification should use exact geometry plus explicit session/context evidence. Payload signatures are useful diagnostics but are not universal ownership tokens.
- The old production engine's runtime whitelist model is directionally consistent with current evidence: already-known work families can appear in different orders and need context-aware handling rather than a rigid chain.
- The all-zero 085F seen immediately after ACK0834 is a transient or phase-local state in at least this retained epoch; it must not be assumed to remain the stable post-OTA baseline.

## DISPROVEN / SUPERSEDED

- **Superseded:** local active ACK safety for `0834/18` is OPEN. It is now locally proven for the exact S11Q FIX2 retained context.
- **Disproven as a universal qualifier:** exact 0834 payload signature must remain constant for retained ownership.
- **Disproven as a universal scheduler rule:** ACK0848 must be followed by `0708 -> all-zero 085F`.
- **Disproven as a universal scheduler rule:** ACK0884 must immediately expose `07D0`.

## OPEN / UNKNOWN

- Whether one isolated ACK to stable retained `085F/5 = 0000 0000 0800 0000 0000` is sufficient to advance the current scheduler without first responding to `0708/6`. S11R FIX2 is PREPARED / NOT RUN to test this.
- Which work family follows that isolated ACK085F in the current retained controller epoch.
- Generic authorization rules for contextual 085F and qualified 0870 outside already exercised paths.
- Semantic meaning of the 18 words in `0834/count18`; ACK acceptance proves work completion, not payload semantics.

## Current evidence boundary

Do not infer semantic acceptance from a standard FC16 ACK alone. The new 0834 result proves that, in the exercised local context, ACK0834 released the pending scheduler owner. It does not identify the payload meaning.

Do not treat S11Q/S11R YAML result codes as stronger than the raw bus sequence. S11Q FIX2's inherited harness reported an inconclusive code after the positive protocol transition; the raw sequence and one-TX accounting are the authoritative evidence.

---
# 2026-10-07 — S11H refines retained service/work-owner model

## PROVEN / locally confirmed

- Current retained `085F/5` baseline was directly decoded as `0000 0000 0800 0000 0000` with signature `7EAE5A0A`.
- One proven idle `0708/6` response (`W0..W4=0000`, `W5=0006`) again changed controller-published `085F/5` to exact all-zero.
- One standard ACK of that exact changed all-zero `085F/5` again released the retained service boundary.
- In S11H, the first released runtime family was `0884/60`, not `07D0/19`.
- After release, repeated `0884/60` and `0708/6` continued while ESP TX stayed fixed at 2 and integrity remained clean.

## STRONGLY SUPPORTED

- `085F/0708` is a service gate layered in front of controller-owned pending runtime/history work, not a fixed return-to-07D0 state.
- The controller retained work-owner/session context survives ESP process restart and determines which family appears after the service gate is released.
- The post-S11H `0884/60` is consistent with prior S11F history-overlay work remaining pending across the intervening ESP restart and `085F/0708` boundary.

## DISPROVEN / SUPERSEDED

- The locally proven S10C two-step retained release does not always return directly to `07D0/19`: it did so in S10C but exposed `0884/60` in S11H.

## OPEN / UNKNOWN

- Whether one ACK to the newly exposed S11H `0884/60`, while keeping the same uninterrupted ESP/controller epoch, releases directly to `07D0/19`. S11I is prepared to test exactly this.
- Exact generic mapping from retained work owner to the service-gate sequence remains open.

---
# 2026-10-07 — S11G FIX1 retained-state observation

## PROVEN / locally confirmed

- After the S11F endpoint and a later ESP-only OTA/restart, the observed local controller state in S11G FIX1 was a repeated `085F/count5` + `0708/count6` retained loop, not repeated `0884/count60`.
- In the supplied S11G FIX1 slice, `q0884=0` while `q0708` increased through at least 27 and `085F` publications increased through at least 54.
- S11G fail-closed qualification worked: unexpected pre-arm `085F` set `otherPre=1`, locked the test inconclusive, and no TX occurred.
- No ACK0884 was sent; therefore the S11G ACK0884 hypothesis remains untested.

## OPEN / UNKNOWN

- Whether the transition from the prior repeated-0884 state to the observed `085F/0708` boundary was caused by ESP restart, elapsed controller timeout/state evolution, or another retained-session condition.
- Whether one retained ACK0884 would release to 07D0 if the exact repeated-0884 state is captured before it disappears.
- Which minimal retained `085F/0708` service sequence is sufficient to re-enter normal runtime without a controller reboot.

---

# 2026-10-07 — S11D/S11F fresh-session and 0884 retained-overlay findings

## PROVEN / locally confirmed

- A fresh local XTR M native session can progress through canonical approval, exact 32-page settings bootstrap, bounded `0708/6` mailbox service, known runtime pages, `0864/4`, `0870/17`, and `0884/60`.
- In S11D, the XTR reached `0870/17` after qualified `0864/4` completion and all TX stopped at the capture-only endpoint.
- In S11F, one qualified standard FC16 ACK to `0870/17` was delivered in the same fresh session; first `0884/60` appeared ~2.04 s later after one additional bounded `0708/6` mailbox response.
- S11F fail-closed behavior worked: first `0884/60` disabled all further TX; repeated 0884 publications continued while TX stayed fixed at 47.
- `0834/18` was not required for the exercised fresh-session path to reach `0870` or `0884`; local active ACK safety for 0834 remains OPEN.
- Local `0864/4` again carried `0867=00F2` (decimal 242) in the exercised session.

## STRONGLY SUPPORTED

- `0864 -> 0870 -> 0884` is part of the normal native runtime/onboarding progression when the surrounding session/mailbox context is qualified.
- Genuine Online/DCM captures strongly support ACKed `0884/60` as a history/runtime-overlay completion followed by a new runtime cycle.
- In 19 qualified raw-capture cases, the observed sequence after ACK0884 is `0708 -> 07D0`; median timing from the 0884 request is ~1.277 s to 0708 and ~2.010 s to 07D0.

## OPEN / UNKNOWN

- Whether local retained post-S11F `0884/60` can be safely adopted after an ESP restart with one ACK and no mailbox response. S11G is prepared to test exactly this.
- Whether ACK0870 alone is sufficient for 0884; S11F retained one mailbox response between those events.
- Whether source-faithful mailbox service is required immediately after ACK0884 on the local XTR.
- Local active ACK behavior for `0834/18`.
- Raw user-facing meanings of modern XTR `0884` history/event record codes.

## GENUINE / CROSS-MODEL 0884 evidence

Across currently available raw captures with explicit `0884/count60` request+ACK pairs, 21/21 explicit requests were ACKed. Nineteen normal-cycle cases then reached `0708/6` followed by `07D0/19`. Two other cases are not normal-cycle comparators because one enters settings/bootstrap traffic and one capture ends before useful follow-on traffic.

This cross-model schedule supports, but does not itself prove, local retained-XTR ACK authorization.

---

# 2026-10-05 — EXP426 trigger absent; normal retained startup remains healthy

## PROVEN / locally confirmed

- In the supplied EXP426 run, no `0662/count33` frame appeared and the EXP426 release-ACK route transmitted nothing.
- Normal retained-runtime startup still synchronized `042E/count15`, `0442/count13`, `0546/count20`, then `03E8/count14` without special 0662 handling.
- Configuration reached READY and remained stable through the supplied ~147 s run.
- Final parser/session integrity remained clean: no unknown FC16/FC03, peer FC17/FC16-ACK, resync or RX drops.
- The presentation-only HA entity cleanup did not disturb the observed protocol/runtime behavior.

## OPEN / UNKNOWN

- Whether the exact repeated `0662/count33` condition recurs deterministically or only under a narrower retained-controller state.
- Whether the isolated EXP426 one-shot ACK is sufficient when that condition does recur.
- The semantic owner/role of `0662/count33` remains unknown.

## STATUS

- **EXP426 COMPLETE / INCONCLUSIVE** — trigger absent, not a negative result for the isolated-release hypothesis.

---

# 2026-10-05 — EXP425 ordered-tail hypothesis negative; EXP426 isolates the 0662 ACK effect

## PROVEN / locally confirmed

- Under the exact EXP425 condition, a one-shot ACK of repeated `0662/count33` stopped the repeated 0662 loop.
- The expected next ordered config page `0683/count33` did not appear within the 60 s observation.
- The runtime subsequently recovered without a controller restart.
- Existing startup sync paths `042E/count15`, `0442/count13`, and `0546/count20` completed after the timeout.
- `03E8/count14` Configuration autosync then completed and writes became READY.
- No parser/peer/resync/drop regression was observed in that recovery.

## DISPROVEN / SUPERSEDED

- **EXP425 ordered-tail interpretation:** in this context, ACKing `0662/count33` does not imply that the controller will continue with `0683 -> 06A4 -> 06C5 -> 06EA -> 06F1 -> 06F4`.

## STRONGLY SUPPORTED

- The exact repeated `0662/count33` condition is not safely modeled as an orphaned position in the known ordered export.
- The ACK itself may be sufficient to release the controller from a stalled retained transfer, after which ordinary runtime/autosync can recover.

## OPEN / UNKNOWN

- The semantic role / owner identity of this standalone-looking `0662/count33` transfer.
- Whether the exact strict qualifier used in EXP426 is necessary and sufficient across repeated reconnects.
- Whether another predecessor/token exists that would classify this transfer more naturally than the current startup-state discriminator.

---

# 2026-10-05 — EXP423 exposed an incomplete EXP420 config-ownership predicate

## PROVEN / locally confirmed

- In the supplied post-OTA local XTR M run, `0662/count33` was repeatedly published while the ESP was already at retained `stage=40`.
- The EXP420 rule classified the page as unowned and withheld the FC16 ACK.
- The same `0662/count33` then retried persistently for the entire ~180 s supplied slice; the no-owner counter reached 166.
- During the retry loop, production writer startup states stayed unsynchronized (`exp378_state=7`, `exp379_state=7`, `exp380_state=7`), `configSynced=0`, `idle0708=0`, and no semantic TX occurred.
- Parser and bus-integrity counters stayed clean; this was not a parser corruption or generic-page-builder failure.

## STRONGLY SUPPORTED

- The EXP420 config ACK ownership predicate is **too narrow** outside the long retained-runtime context in which EXP420 originally passed.
- At least one legitimate/relevant pre-first-0708 or unsynchronized transfer context can contain `0662/count33` and requires ownership handling beyond the four production sync pages and existing EXP410/resume owners.
- The EXP421 generic desired-page core remains unimplicated by this failure because it was never entered.

## OPEN / UNKNOWN

- The exact owner for this `0662/count33` transfer: e.g. interrupted calendar/config export, reconnect continuation, or another startup/resume context.
- Whether the narrow authorization should be keyed to a preceding page/order token, an unsynchronized-start state, or another explicit session marker.
- Whether adjacent calendar/config pages would follow after an ACKed 0662 in this exact context.

## DISPROVEN / SUPERSEDED

- **Superseded as a universal rule:** “the EXP420 explicit-owner predicate is sufficient for all stage40 config traffic.”
- The original EXP420 retained-runtime result itself is not erased: it remains positive for the context actually observed there.

---

# 2026-10-05 — EXP422 generic helper second-geometry validation

## PROVEN / locally confirmed

- The shared generic desired-page builder/TX primitive is now live-proven on `042E/count15` in addition to `03E8/count14`.
- `0433` / word5 / Startup HT was changed `5 -> 6` through the generic helper and confirmed by exact controller FC16 republish with `extraDeltaWords=0`.
- The exact rollback `6 -> 5` traversed the same generic helper and was again confirmed with `extraDeltaWords=0`.
- Final EXP421/422 diagnostics were `genericTX=2 buildFail=0 lastPage=042E`; Startup HT returned to 5.
- Explicit config ACK ownership remained intact and no parser/session integrity regression was observed.

## STRONGLY SUPPORTED

- The generic helper is not specific to the `03E8/count14` frame length; it has now been locally exercised successfully on a distinct `042E/count15` geometry.
- Centralized page serialization, one-word substitution, CRC16 and TX timing can remain the shared primitive while page-specific guards/state/confirmation stay outside it.

## OPEN / UNKNOWN

- Independent live exercise of the shared helper on `0442/count13` and `0546/count20`.
- Whether the remaining page-specific orchestration can safely be consolidated into a higher-level generic transaction state machine without weakening per-page validation or ownership.
- Fresh cold-session/recovery interaction with semantic writes remains separate from these retained-runtime results.

---

# 2026-10-05 — EXP421 generic desired-page TX core

## PROVEN / locally confirmed

- The EXP421 shared desired-page byte builder/TX primitive is live-compatible with the local XTR M `03E8/count14` semantic write flow.
- A room-setpoint write `03F4 22 -> 23` traversed the shared helper once and was confirmed by exact controller FC16 republish with `extraDeltaWords=0`.
- The exact rollback `03F4 23 -> 22` traversed the same shared helper a second time and was confirmed by exact controller FC16 republish with `extraDeltaWords=0`.
- Final EXP421 diagnostics were `genericTX=2 buildFail=0 lastPage=03E8`; the room-setpoint cache was restored to 22.
- The same run retained clean parser/session integrity and explicit config ACK ownership.

## STRONGLY SUPPORTED

- Centralizing full cached-page serialization, one selected-word substitution, CRC16 and DE/UART transmit timing does not change the observed `03E8/count14` semantic behavior when page-specific validation, selectors, state and confirmation remain outside the helper.
- The generic helper is a viable base for further consolidation of the existing production writers.

## OPEN / UNKNOWN

- Independent live exercise of the shared helper on `042E/count15`, `0442/count13`, and `0546/count20`.
- Whether a higher-level generic transaction state machine can safely replace the remaining page-specific orchestration without weakening current per-page guards.
- Fresh cold-session/recovery interaction with semantic writes remains separate from this result.

---

# 2026-10-05 — EXP420 config ACK ownership hardening

## PROVEN / locally confirmed

- The local XTR M remains stable in retained `stage=40` with broad known-config page-shape ACK authorization removed.
- During the same EXP420 boot, the explicit-owner counter reached **4 owned config ACKs** while the unowned-config counter remained **0**.
- After more than 6700 s runtime age, the final supplied heartbeat remained clean: `unknown16=0 unknown03=0 peer17=0 peer16ack=0 resync=0 drops=0`.
- EXP418 0870 ownership remained clean in the same run and reached `316/316` set/consume with no tokenless event.

## STRONGLY SUPPORTED

- For the currently exercised production config path, page geometry alone is no longer required as ACK authorization; explicit transaction ownership is a viable production baseline.
- The four owned config ACKs are consistent with the normal startup/current synchronization of `042E`, `0442`, `0546`, and `03E8`; however the supplied late-runtime slice contains the counters rather than those earlier individual owner log lines.

## OPEN / UNKNOWN

- legitimate autonomous config-family publications other than the already evidence-backed idle `03E8`;
- live behavior of `EXP420_CONFIG_NO_OWNER ... NO_ACK` if such a page occurs;
- live autonomous idle `03E8` owner branch under EXP420;
- EXP419 085F context authorization;
- cold approval / recovery / rejoin ownership interactions.

---

# 2026-10-05 — EXP418 0870 ownership hardening

## PROVEN / locally confirmed

- In the supplied EXP418 retained-runtime slice, **15/15** observed `0870/count17` publications were preceded by an actually ACKed `0864/count4` that created a one-shot ownership token.
- Each of those 15 `0870` ACKs consumed exactly one token; token counters advanced in lockstep from 96/96 to 111/111.
- No tokenless `0870` was observed and no recovery/rejoin bypass was used.
- The hardened implementation remained at `stage=40` with clean final integrity counters: `unknown16=0 unknown03=0 peer17=0 peer16ack=0 resync=0 drops=0`.

## STRONGLY SUPPORTED

- The existing one-shot normal-runtime ownership-token model is now live-compatible on this XTR M, not merely offline-modeled.
- Page shape alone is no longer required as sufficient authorization for normal-runtime `0870/count17` in the production path.
- `0864` remains only one valid token source; earlier EXP309/310 evidence still disproves a mandatory-0864 prerequisite because qualified all-zero `085F` can also lead directly to valid `0870`.

## OPEN / UNKNOWN

- whether any normal-runtime XTR context can legitimately produce `0870/count17` without either token source;
- live EXP418 behavior when the token source is all-zero `085F/count5` rather than `0864/count4`;
- exact recovery/rejoin authorization predicate outside the normal-runtime token path.

---

# 2026-10-04 — durable calendar write findings through EXP404

## PROVEN / locally confirmed — F1 current and desired selectors

- `W2 bit1 -> CURRENT FC16 055A/count33`.
- `W0 bit1 + W2 bit1 -> DESIRED FC03 055A/count33`.
- `W2 bit3 -> CURRENT FC16 059C/count33`.
- `W0 bit3 + W2 bit3 -> DESIRED FC03 059C/count33`.
- `W2=000E` requests the full F1 transport window as `055A/33 + 057B/33 + 059C/33`.

These are local XTR M results, not symmetry-only inference.

## PROVEN / locally confirmed — native calendar desired-page primitive

For both 055A and 059C, the local XTR M accepts the native sequence:

`0708 desired selector -> controller FC03 full-page pull -> ESP full-page response -> controller FC16 page publication`.

An exact no-op response is locally accepted on both pages.

For semantic deltas, exact FC16 republish of the intended change is observed and used as confirmation.

## PROVEN / locally confirmed — semantic content write

`055B` / F1 slot0 word1 is start minute.

EXP401 changed `055B 0000 -> 0001` while slot0 validity remained clear. Controller FC16 confirmed exactly one changed word, and automatic rollback restored the original page.

Therefore calendar content is locally writable through the native Online/DCM desired-page mechanism.

## PROVEN / locally confirmed — F1 slot0 validity metadata

`05BA bit0` controls validity of F1 slot0.

Evidence now includes both directions:
- prior panel-driven/local mapping correlation;
- EXP404 active write `05BA 0000 -> 0001`;
- exact controller FC16 confirmation with one changed word;
- independent passive decoder observation of bit0 set;
- automatic rollback `0001 -> 0000` with exact original page restored.

This upgrades `05BA bit0 -> F1 slot0 validity` to **PROVEN / locally confirmed**.

## PROVEN / locally confirmed — rollbackability

Both content-page and metadata-page experimental writes have been restored using a second native desired transaction carrying the original authoritative page image.

Safe experimental pattern now locally supported:
1. acquire fresh current page;
2. preserve exact original image;
3. mutate only intended word(s);
4. answer one controller FC03 pull;
5. require exact FC16 confirmation;
6. send original page through the same desired mechanism;
7. require exact restoration.

## STRONGLY SUPPORTED

- F1 is the `WW_GEBLOKKEERD` / Hot Water Blocked calendar function.
- Each calendar function is 98 logical words: 8 x 12-word records + 2 metadata words.
- slot0 word6 is stop minute.
- slot0 word11 is weekday/recurrence mask; exact weekday bit identity remains incomplete.
- a production calendar writer should stage content while validity is clear, then change validity separately after content confirmation.

## OPEN / UNKNOWN

- coherent multi-word content acceptance in one local XTR 055A desired transaction;
- exact weekday bit ordering;
- mode-field semantics;
- date-vs-recurrence precedence;
- desired selectors for other F1 pages and F2/F3/F4;
- F2/F3/F4 semantic labels locally;
- persistence/reload behavior across restart;
- atomicity expectations when content and validity live on different pages;
- whether full slot creation should be ordered content-first then metadata, as currently safest, or follows another native rule.

## DISPROVEN / SUPERSEDED

- **Calendar is read-only on this XTR M** — disproven by EXP401 and EXP404.
- **055A desired selector is only a cross-model inference** — superseded by local EXP399.
- **059C desired selector is unknown** — superseded by local EXP403.
- **05BA bit0 is only a candidate validity flag** — superseded by EXP404 local write+rollback confirmation.

---

# 2026-10-04 — Durable findings from PROTO-OFFLINE-61..64

This section is current where it conflicts with older interpretations below.

## PROVEN / locally confirmed or source-confirmed

- Write Beta v4.1 contains **58 explicit UART TX sites**, all mapped to known route classes. No additional semantic TX class was found in the source audit.
- The only full-page semantic response TX classes remain 03E8, 042E, 0442, and 0546.
- 0834 remains capture-only in current source.
- The state7 delayed-refresh distinction is represented by the separate delayed-refresh flag; numeric state7 alone is not sufficient to decide re-arm behavior.

## STRONGLY SUPPORTED

- The PROTO60 formal model is sufficiently complete to act as a source-audit contract for current TX routes.
- Source-transcribed host decision logic agrees with the current golden/fault/reachability assets across **4630/4630 checks**.
- Current source still has three known ACK-context policy debts: 085F, 0870, and generic known-config runtime ACK.
- A future production-core rewrite can safely target consolidation of bootstrap ACK blocks and semantic transaction engines, but should preserve behavior until live regressions are complete.

## NEW PARSER SAFETY FINDING

- The current stream assembler considers multiple candidate frame lengths and accepts the shortest CRC-valid candidate.
- CRC validity does **not** uniquely distinguish a short FC03 request from a longer FC03 response sharing the same prefix.
- Deterministic synthetic constructions exist where a valid longer FC03 response has an 8-byte CRC-valid prefix interpreted as an exact semantic request for:
  - 0546/count20
  - 042E/count15
  - 0442/count13
- 100,000 targeted fuzz cases built only from non-semantic seed traffic produced **0 accidental semantic-request outputs**, so no ordinary random reframing problem is demonstrated.
- No genuine Thermia frame in the present corpus is known to trigger the double-valid-prefix ambiguity.
- Classification: **STRONGLY SUPPORTED defensive parser gap; not a proven live semantic write defect.**

## DISPROVEN / NOT SUPPORTED

- There is no evidence from PROTO61 that a hidden/unmodeled semantic TX route exists in v4.1.
- The parser ambiguity does not prove that genuine controller traffic has ever triggered an incorrect semantic response.
- Broad random-fuzz semantic-shaped outputs that included genuine semantic-request seeds are not evidence of accidental semantic synthesis; the targeted non-semantic control is the relevant negative control.

## Cleanup / rebuild constraints

- Preserve delayed-refresh semantics explicitly.
- Preserve direct valid 0870 behavior without inventing a mandatory 0864 prerequisite.
- Preserve both locally proven 085F payload forms.
- Preserve autonomous current-state/config behavior such as runtime 03E8.
- Keep 0834 capture-only until local evidence changes.
- Move historical resume/test scaffolding out of production core only after static/compile/golden equivalence checks.
- Do not combine parser replacement, ACK-hardening, and EXP388 recovery restructuring in one experiment.

---

# 2026-10-04 — Durable protocol findings from PROTO-OFFLINE-45..60

This section is current where it conflicts with older interpretations below.

## PROVEN / locally confirmed

- Both currently accepted XTR `085F/count5` payload forms are ACKable in qualified local contexts. The unresolved problem is context authorization, not payload identity.
- Local XTR can present `0870/count17` directly after qualified all-zero 085F **without prior 0864**. EXP309/310 disprove a mandatory-0864 prerequisite.
- One qualified direct local 0870 ACK advances to valid runtime; sustained local runtime also services 0870.
- Local config ACK ownership is proven for ordered bootstrap, explicit current-page refresh and desired-state confirmation.
- Autonomous controller-originated runtime `03E8/count14` exists locally, so every runtime config publication cannot be modeled as W2/W3-owned.
- Local XTR `03F3=1` and `03F5=2` are structurally observed on the modern `03E8/count14` page; semantic names remain OPEN.
- `0834/count18` still has no local XTR ACK proof.

## PROVEN / genuine Online/DCM capture

- Approval and service/config work can overlap; they are not strictly exclusive sequential states.
- Genuine legacy Online can ACK standalone config publication while W2/W3 are zero.
- Genuine ATEC/DCM03 can ACK steady-state `085F/count5`.
- Current genuine 0870 corpus contains 64 ACKed and 31 unACKed publications; the 31 unACKed examples are one reconnect retry population.
- `0884/count60` can be periodically republished byte-for-byte unchanged for minutes; decoded records are newest-to-oldest.
- ATEC calendar function words 0..391 match the legacy reference; changing 06E2 further separates the 06E2..06E5 tail from F1..F4.

## STRONGLY SUPPORTED

- Session/approval qualification and current work class should be modeled as **orthogonal axes**.
- Current v4.1 transitions enforce a sole-semantic-owner invariant in the modeled reachable graph: PROTO57 reaches 115 variants with zero multi-owner states.
- A global explicit sole-owner assertion is useful defensive hardening; PROTO58 shows it blocks 604 impossible synthetic conflicts and zero modeled reachable normal paths.
- Best-supported local normal-runtime 0870 qualifier: a one-shot session-scoped ownership token created after qualified all-zero 085F ACK OR qualified 0864 ACK; optional known 0708 may intervene; first 0870 ACK consumes it.
- 0870 needs at least two conceptual authorization branches: qualified normal runtime plus explicit recovery/rejoin.
- Semantic write safety debt is concentrated mainly in ACK authorization/context, not value injection.
- Local XTR configuration ABI follows modern Eco5 geometry for the known count-drift pages 03E8, 0410, 0492 and 051E.

## OPEN / UNKNOWN

- exact local recovery/rejoin predicate for 0870 outside the normal-runtime token path;
- universal/local context rule for immediate 085F ACK permission;
- which XTR config pages besides 03E8 can be autonomously pushed and whether ACK is required;
- local 0834 ACK behavior;
- raw 0884 event-ID meanings and insertion/rollover/clear mechanics;
- calendar weekday bit ordering and native cross-page write atomicity;
- exact 071C/0730 challenge-response implementation/key/state;
- Connect/OnSite/DCM03 binaries and serializer implementation.

## DISPROVEN / SUPERSEDED

- **Mandatory 0864 before 0870** — disproven locally by EXP309/310.
- **All config FC16 must be W2/W3-owned** — disproven as a general model by local autonomous 03E8 and genuine legacy standalone config pushes.
- **085F service-only ACK as a universal Thermia rule** — disproven cross-profile by genuine steady-state ATEC 085F ACK.
- **PROTO53 Cartesian conflicts as evidence of a reachable double-semantic bug** — superseded by PROTO57 reachability.

## Regression assets

- PROTO54 golden trace suite: **72/72 PASS**.
- PROTO60 formal protocol model validator: **57/57 PASS**.
- Machine-readable model: `Research/protocol reduction/thermia_protocol_model_v1.json`.
- Decision table: `Research/protocol reduction/thermia_protocol_model_v1_decision_table.csv`.

---

# 2026-10-03 — durable findings through PROTO-OFFLINE-44

## DISPROVEN / SUPERSEDED — challenge-response simple transforms

Across seven CRC-valid approval request/response pairs, no fixed XOR mask, fixed byte-wise add/sub mask, fixed byte/word permutation+mask, simple rotation+mask, direct/reversed MD5, or truncated SHA-1/SHA-256 relation explains the response. The exact DCM03/Connect response function remains OPEN and may be keyed/stateful/proprietary.

## PROVEN / genuine Eco5 desired-state confirmation

Four fully bracketed one-word semantic desired-state deltas are each followed by an exact controller FC16 republish of the desired image after 0.491..0.571 s.

## STRONGLY SUPPORTED / cross-profile no-op behavior

A genuine ATEC/DCM03 `W0 bit0 -> FC03 0546/count20` pull returns an image exactly equal to the controller's prior page and is not followed by same-page FC16 republish over 226.677 s. Missing republish after an exact no-op must not be treated as universal write failure. This remains cross-profile evidence, not a locally proven XTR rule.

## PROVEN / genuine gateway cache reuse

In the bracketed Eco5 desired transactions, the latest bus-visible same-page controller image was 67.084, 319.512, 374.586 and 87.609 s old. Therefore immediate same-page refresh is not a universal protocol requirement. The current local XTR freshness guard remains a conservative safety policy.

## PROVEN / genuine ACK-context behavior

- `085F/count5`: 331 publications, 20 ACKed, 311 unACKed. Repeated address/payload identity does not determine permission to ACK.
- `0870/count17`: 95 publications, 64 ACKed, 31 unACKed. All 31 unACKed belong to one reconnect retry window; a later ACK participates in transition to `0708` rejoin/export.
- known configuration-page shape does not imply ACK permission: large unACKed populations exist for `03E8`, `04A6` and `04BA`.

## STRONGLY SUPPORTED — protocol state model

Current genuine evidence supports distinct states:

`APPROVAL -> optional WAIT_PAGE_SERVICE -> BOOTSTRAP -> POST_BOOT_SERVICE -> NORMAL_RUNTIME`

with separate runtime branches for `CONFIG_REFRESH`, `SERVICE_REFRESH`, `DESIRED_PULL`, and `RECOVERY_REJOIN`.

ACK permission should be associated with an owning state rather than with page shape/payload alone.

## LOCAL XTR implementation consequence — not yet changed

Write Beta v4.1 remains structurally aligned with the genuine protocol, but three ACK permissions are broader than the newest evidence model:

1. known `085F` payload as generic runtime ACK permission;
2. `0870` page shape as generic runtime ACK permission;
3. generic known configuration-page ACK outside an owning bootstrap/refresh/confirmation/resume state.

These are future hardening requirements, not completed local behavior changes.

## OPEN / UNKNOWN

- exact challenge-response algorithm/key/credential/session dependence;
- universal no-op confirmation behavior across XTR and other profiles;
- local XTR maximum safe page-cache age;
- exact local XTR service/recovery predicate for `085F`;
- local XTR qualification rule for reconnect `0870`;
- local XTR ACK safety for `0834/count18`.

---

# 2026-10-03 — ATEC/DCM03 cold-start durable findings

## PROVEN / genuine ATEC + classic DCM03

- ATEC sends native slave-`0x0F` FC17 approval with read `0730/count8` and write `071C/count8`; classic DCM03 answers with `0F 17 10 <16-byte body>` 29 ms later.
- Native ATEC configuration service begins 1.833 s after that response. The genuine Eco5 ~120 s page-service boundary is **not** universal.
- ATEC performs complete ordered **32-page ACK-gated bootstrap** `03E8..06F4` before normal mailbox/runtime service.
- Page counts are profile-specific. This ATEC uses at least `03E8/13`, `0410/21`, `0492/9`, `051E/9`.
- First ATEC mailbox state is `0000 0000 0000 0000 07FF 0006`; steady state in the supplied capture uses `W4=077F, W5=0006`.
- **Genuine high-half desired selector proof:** `W0 bit0 -> controller FC03 0546/count20`.
- In that event DCM03 returns a `0546` image exactly equal to the controller's prior image; `0553=0004` is present in both. This is a **no-op desired pull**, not proof of an Operation Mode change.
- `0867=0000` in this known ATEC/DCM03 capture. `0867=0016` from the older legacy-reference corpus is therefore a corpus/profile fingerprint, not universal legacy identity.

## STRONGLY SUPPORTED

- Classic DCM03 is a first-class target for recovering or using the native challenge-response mechanism; Thermia Connect is not the only observed device class answering the approval gate.
- A hardware-oracle/bridge route becomes a genuine candidate only if ATEC-EXP2 shows DCM03 answers a foreign Eco8 challenge in controlled standalone context.

## SELECTOR PROVENANCE UPDATE

- `03E8/W1 bit0`: genuine Online + local XTR proof retained.
- `042E/W1 bit3`: genuine Online + local XTR proof retained.
- `0442/W1 bit4`: local XTR only.
- **`0546/W0 bit0`: now local XTR + genuine ATEC/DCM03 proof.**
- `055A/W0 bit1`: local XTR only.
- All unobserved desired bits remain deny-by-default.

## DISPROVEN / SUPERSEDED

- “classic ATEC does not send the challenge” — disproven.
- “Thermia Connect is the only observed device answering the challenge” — disproven; classic DCM03 answers ATEC.
- ATEC-EXP1 v0.2 no-FC17 + Eco5-derived 26-page/count14 assumptions — superseded before live execution.
- `0867=0016` as a universal legacy/ATEC fingerprint — superseded.

## OPEN / UNKNOWN

- whether standalone DCM03 can answer Eco8/foreign challenges;
- request-only/credential response vs prior bus/session/pairing dependence;
- response algorithm/key material;
- genuine W0 bits beyond bit0;
- whether a future non-no-op ATEC `0546` pull gets controller FC16 republish.

---

# 2026-10-03 — durable findings reconciliation through PROTO-OFFLINE-39

## PROVEN / genuine Eco5 Online structural

- Approval/session-open and native page-service readiness are separate states.
- Genuine Eco5 initial configuration export is a fixed **32-page ACK-gated autonomous bootstrap** `03E8 ... 06F4` before the first `0708`.
- Later `0708 W2/W3=FFFF/867F` is a separate **26-page refresh**, not the initial bootstrap.
- `06F4/count19` is terminal in the strict bootstrap in all six successful Eco5 sessions.
- `W2/W3` residual values behave as remaining configuration work.
- `W4` has a stable runtime/service page-family mapping but is **not** an exclusive immediate next-page selector.
- Genuine desired-selector observations remain `W1 bit0 -> 03E8` and `W1 bit3 -> 042E`; no genuine non-zero W0 exists in the current capture corpus.

## STRONGLY SUPPORTED / genuine Eco5 session behavior

- Across six successful sessions, first accepted `03E8/count14` ACK occurs 118.478..120.296 s after bus return.
- Early challenge-#3 approval can be accepted ~108.5 s before genuine gateway page service becomes ready.
- No independent captured recurrent bus field among the tested families predicts that transition.
- The ~120 s boundary is gateway/session behavior in the current Eco5 corpus and is **not** a universal XTR controller requirement.

## PROVEN / locally confirmed XTR semantic corrections

- `042E = Hot Water Enabled`.
- `042F = Hot Water Mode`.
- The numeric address `042E` remains profile-specific across Thermia families; local proof does not make it universal.
- Later local write experiments upgrade the current evidence for `03E9,03EA,03EC,03ED,03EE,03EF,03F0` and the already-recorded cooling/operation-mode controls beyond the older PROTO16 snapshot.

## STRONGLY SUPPORTED / locally correlated or cross-profile

- `0424 = Returnline Temperature Max Limit`.
- `04A6/04A7` correlate with SG/operational state in the later local XTR runtime; they are not an Online approval flag.
- `0870 = Compressor Operating Time`.
- Sparse runtime map: `0872` heating, `0873` cooling, `0876` hot water, `0877` aux1, `0878` aux2, `0879` aux3 candidate; `0874/0875` remain OPEN.
- `087B/087C/087D` align with defrost count / interval / since-last-defrost.
- `0884/count60` is local modern rolling timestamped history; raw event translation remains unresolved.

## CONNECT / firmware archaeology

Official Connect evidence now anchors:
- local AP commissioning/update as a supported path;
- heat-pump serial input during onboarding;
- explicit “pairing and protocol packages” wording;
- exact identifiers: Connect kit `206495`, gateway `355202`, PSU `357577`.

No Connect firmware, protocol-package archive, local API route, OnSite APK/XAPK, Online APK/XAPK or DCM03 firmware image has been recovered.

## PROTO-OFFLINE-24 current-alarm bridge

- **PROVEN in available corpus:** 339/339 observed `085F/count5` payloads are all-zero.
- **DISPROVEN:** `085F` as a direct mirror of the newest `0884` history entry; non-empty history exists while `085F` is zero.
- **OPEN:** whether `085F` changes only during an active alarm/service condition; no labelled alarm edge exists in the current corpus.

## PROTO-OFFLINE-25 unresolved-field refinements

- **PROVEN structural:** `0875 == 0873` in 83/83 reference `0870/count17` frames across legacy and Eco5; semantic reason remains OPEN.
- **STRONGLY SUPPORTED:** `087D` is a running-time accumulator; observed +1 edges in Eco5 occur while `0865` compressor-running is active. Exact raw unit/scaling remains OPEN.
- **PROFILE/GENERATION DRIFT:** `03F3`, `0431`, `0432`, and `0447` have materially different legacy vs Eco5 value domains.
- **STRUCTURAL:** `03F5` exists in modern `03E8/count14` but not legacy `03E8/count13`.

## PROTO-OFFLINE-26 challenge/session refinements

- **PROVEN in genuine Eco5 corpus:** 163 challenge requests contain 162 unique bodies; one 16-byte body repeats on consecutive polls. Fresh nonce uniqueness per poll is therefore disproven.
- **STRONGLY SUPPORTED:** challenge #3 and #29 are timing landmarks at approximately 10 s and 120 s after bus return.
- **NEGATIVE:** simple challenge-body features and recent prior gateway bus activity do not explain #3/#29/no-response behavior.

## PROTO-OFFLINE-27 app-artifact status

- **OBSERVED:** OnSite Android public metadata includes Wi-Fi/network-control permissions consistent with the official local-AP commissioning flow.
- **OBSERVED:** Thermia Online has a public XAPK acquisition surface and verifiable package hashes/metadata.
- **INCONCLUSIVE:** no APK/XAPK/firmware bytes were recovered in the current environment, so local Connect endpoints, protocol-package manifests and serializer code remain untested.

## PROTO-OFFLINE-28 selector provenance

- **GENUINE + LOCAL desired proof:** `03E8/W1 bit0`, `042E/W1 bit3`.
- **LOCAL XTR desired proof only:** `0442/W1 bit4`, `0546/W0 bit0`, `055A/W0 bit1`.
- **GENUINE CURRENT bitmap proof:** W2/W3 page-index geometry remains valid.
- **NOT PROVEN:** all other desired bits; do not promote by symmetry.
- `W0` is therefore locally proven on XTR but remains unobserved in the genuine Eco5 Online capture corpus.

## PROTO-OFFLINE-29 runtime grammar

- **PROVEN / genuine Eco5 structural:** ordinary runtime follows a stable publication ring dominated by `07D0→07E4`, `07F8→080C`, `0820→0834`, `0848→0864`, then `0870`.
- **STRONGLY SUPPORTED:** W4 is runtime/service remaining-work/state metadata during refresh, not an exclusive next-page selector.
- **PROVEN context sensitivity:** `085F` is mostly unACKed outside explicit service work; known page shape is not sufficient ACK permission.

## PROTO-OFFLINE-30 machine-readable schema

- Current protocol geometry and selector provenance are encoded in `Research/temp/thermia_protocol_schema_current.json`.
- Desired selectors are deny-by-default unless explicitly proven by PROTO28 provenance.
- Runtime page recognition is separated from context-specific ACK permission.

## PROTO-OFFLINE-31 raw history IDs

- **DISPROVEN as universal decoder:** `0884 raw ID == Genesis Modbus alarm address`.
- Numeric collisions exist for some low values, but modern values such as `0x0172` and `0x1400` exceed that domain and the public iTec Online error-code group is empty.
- Raw event identity remains OPEN pending labelled alarm/firmware evidence.

## PROTO-OFFLINE-32 challenge generator

- Genuine Eco5 request bodies are high-diffusion; no stable counter/timestamp byte field is identified.
- The local-XTR structured/timestamp-related request layout is **profile-specific evidence**, not a universal challenge format.
- Fresh nonce uniqueness per request remains disproven by the exact duplicate identified in PROTO26.

## PROTO-OFFLINE-33 Connect hardware fingerprint

- **PROVEN / official:** Connect kit `206495`, gateway `355202`, PSU `357577`; gateway is 12 VDC and exposes USB, Ethernet, pump communication, a second documented-unused communication port, LED and reset.
- **PROVEN / official:** 2.4 GHz IEEE 802.11 b/g/n with WPA-PSK AP; Wi-Fi/Ethernet are the normal network paths.
- **OPEN:** built-in cellular capability. Cellular-family standards occur in the EU declaration, while Thermia's public Online documentation describes a separate external 3G/4G modem when broadband is unavailable.
- **NOT RECOVERED:** OEM, SoC/MCU, radio module identity, bootloader/update transport.

## PROTO-OFFLINE-34 W5 semantics

- **PROVEN / local XTR causal:** W5=0006 is sufficient for persistent DCM-connected UI indication in the EXP344→345 one-variable comparison; W5=0000 remains transport/runtime-valid but the icon was absent.
- **PROVEN / genuine profile evidence:** legacy Online/DCM uses W5=0006 normally and one W5=0007 rejoin-associated response; genuine Eco5 uses W5=0000 in 264/264 answered polls.
- **DISPROVEN as universal enum:** W5 cannot be interpreted globally as 0=disconnected / 6=connected / 7=joining.

## PROTO-OFFLINE-35 runtime scaling

- **STRONGLY SUPPORTED:** `0870/0872/0873/0876/0877/0878` use raw integer **hours** for operational time; `0879` likely shares the scaling if its Aux3 identity is correct.
- **PROVEN manual semantics + strong address mapping:** `087C/087D` represent compressor-runtime **minutes** between last two defrosts / since last defrost.
- **PROVEN count semantics:** `087B` is completed defrost count.

## PROTO-OFFLINE-36 runtime-state reductions

- **PROVEN / genuine Eco5 structural:** `07F4 = 0` outside outdoor status `0x0221`; `07F4=4` for `0x0221` with compressor frequency 0; `07F4=6` for `0x0221` with compressor frequency >0 (96/96).
- **PROVEN / genuine Eco5 structural:** `0845=0x0300` iff `1E:0015=0x0221`, otherwise 0 (43/43).
- No additional heating/cooling/DHW/defrost/SG runtime label is promoted without a labelled physical transition.

## PROTO-OFFLINE-37 Write Beta audit

- Current v4.1 contains no generic unknown semantic write path: desired responses are full-page cached mutations on proven/local-proven selectors with exact republish checks.
- Runtime `04A6`, `0834`, `085F` policies remain deliberately context/payload scoped.
- **HARDENING CANDIDATE:** known config-page shape currently contributes to runtime ACK permission outside explicit resume; future tightening must be live-regressed rather than changed from offline evidence alone.

## PROTO-OFFLINE-38 ABI classifier

- **PROVEN regression:** A5/03E8-count13/0867=0016/W5=6-7 fingerprints separate the four older genuine captures from the two modern 0x1E/03E8-count14/0867=00E8/W5=0 captures.
- The classifier identifies **ABI/topology family only**, not exact model.
- Mixed modern-topology + local-XTR W5=6 behavior must not be misclassified as proof of a legacy physical platform.

## PROTO-OFFLINE-39 evidence coverage

- Canonical experiment numbering is **not continuous**: 139 numeric EXP IDs are present and missing ranges are preserved rather than reconstructed.
- Historical PREPARED/RUNNING headers deeper in the log do not override the top canonical current-state overlay.
- EXP388 remains the current active live experiment; EXP383 remains PREPARED / NOT RUN.
- Runtime config-page ACK qualification from PROTO37 remains a future hardening candidate requiring a live regression.

## PROTO-OFFLINE-37 Write Beta safety audit

- Semantic full-page mutation paths are aligned with current evidence: fresh controller cache, one intended word, exact republish comparison.
- **SAFETY DEBT:** known `085F` payload alone is currently sufficient ACK permission in v4.1; PROTO29 supports adding explicit service/W4 context.
- **REVIEW:** `0870` and known runtime configuration pages are ACKed more broadly than the latest context-driven scheduler model would require.
- No production YAML behavior was changed by this audit.

## PROTO-OFFLINE-38 profile fingerprint

- Broad capture family can be distinguished robustly using backend (`A5` vs `0x1E`), profile page counts, `0867`, and secondary W5 metadata.
- **Legacy family:** `03E8/13`, `0410/21`, `0492/9`, `051E/9`, `0867=0016`.
- **Modern family:** `03E8/14`, `0410/22`, `0492/11`, `051E/10`, `0867=00E8`.
- This is ABI/profile-family classification only; exact model identity remains provenance-dependent.

## OPEN / UNKNOWN after reconciliation

- exact gateway-internal readiness condition;
- genuine W0/high-half desired-selector behavior and unobserved W1 bits;
- `085F/count5` semantics/current-alarm bridge;
- `03F1/03F2/03F3/03F5`, `0431/0432`, `0447`, `0874/0875`;
- exact runtime-counter scaling where not directly reduced;
- raw `0884` event -> displayed alarm mapping;
- Connect/DCM03 serializer/protocol-package contents;
- calendar active-write atomicity and remaining weekday/delete semantics.

## DISPROVEN / SUPERSEDED additions

- approval accepted == page service immediately ready;
- initial Eco5 full sync == `0708 FFFF/867F` refresh;
- W4 as an exclusive immediate next-page selector;
- `042E/042F` as locally unknown on the tested XTR M.

---

# THERMIA PROTOCOL FINDINGS

# 2026-10-03 — canonical durable findings reconciliation

## PROVEN / locally confirmed

- **Native desired-state room setpoint:** `03F4` is a real XTR room-setpoint target. Local semantic writes use the controller-pulled desired-page path and are confirmed by exact controller `03E8` FC16 republish plus matching room-setpoint mirror.
- **Operation Mode anchor:** `0553` is Operation Mode locally; at least `1=AUTO` and `2=COMPRESSOR` are locally causally confirmed.
- **Activate Cooling anchor:** `0442` is Activate Cooling locally, 0/1.
- **Heat Curve anchors:** `03E8` Heat Curve and `03EB` Curve +5 are locally confirmed semantic fields.
- **Context bridge:** `06F4..06F8 = A80C..A810` and `0701=AFDC` are exact structural mirrors.
- **Local XTR service history ABI:** `0884/count60` uses 8 × 7-word timestamped records + 4-word trailer and rolls newest entries forward.

## PROVEN / genuine Online/DCM structural

### 0708 scheduler

For `0x0F FC03 0708/count6`:

- `W2/W3` form the 32-page controller FC16 upload bitmap.
- Observed low-half desired bits:
  - `W1 bit0 -> controller FC03 03E8`
  - `W1 bit3 -> controller FC03 042E`
- `W0` has never been observed nonzero in the current genuine capture corpus and is not proven.
- `W4` has a stable bit-to-runtime/service-page ordering and is strongly supported as the runtime/service page selector/refresh bitmap.
- `W5` is not a universal 6/7 normal/join enum; exact semantics remain open.

### Native semantic write primitive

Observed genuine Online command flow:

`0708 desired-page bit -> controller FC03 desired page -> DCM returns complete coherent page image -> controller applies -> controller FC16 republishes result`.

In all four fully bracketed Eco5 examples:
- prior page vs desired page differed in exactly one word;
- desired page vs following controller FC16 result was byte-for-byte identical.

Therefore safe emulation must use a fresh complete page image and mutate only the intended target; sparse or invented page context is not evidence-backed.

### Runtime export family

The recurring `0x0F` runtime family includes:

`07D0/19, 07E4/17, 07F8/17, 080C/18, 0820/18, 0834/18, 0848/23, 0864/4, 0870/17`.

The page namespace acts as a logical serializer/normalizer across topology families.

### Cross-topology source substitution

- `07D1` preserves return-line semantics while changing physical source between legacy and modern topology.
- `07E4` preserves average-outdoor semantics while changing physical source.
- `0820` is a concrete abstraction boundary: legacy data is sourced from A5; modern data from `0x1E`.
- Equal page start/count does not imply equal byte-level payload semantics across models.

### Clock/date ABI

`0858..085E` is a stable second/minute/hour/day/month/year/weekday tuple across compared topologies. Weekday enumeration is Monday=0 through Sunday=6.

### History ABI

- legacy genuine Online/DCM `0884/count60`: 10 × 6-word timestamped records;
- genuine Eco5 + local XTR: 8 × 7-word records + 4-word trailer.

This is very strongly supported as alarm/service history, but raw event codes are not yet mapped to displayed XTR E-codes.

## STRONGLY SUPPORTED

- `0x0F` is a logical Online/DCM ABI above topology-specific source adapters.
- `0867` is topology/platform metadata/fingerprint; exact human meaning remains open.
- `0870` = compressor operating time.
- Sparse operation-time mapping:
  - `0872` heating;
  - `0873` cooling;
  - `0876` hot water;
  - `0877` auxiliary/immersion 1;
  - `0878` auxiliary/immersion 2;
  - `0879` auxiliary/immersion 3 candidate aligned with ATEC + XTR manual, local XTR confirmation pending.
- Defrost group:
  - `087B` completed defrost periods/count;
  - `087C` runtime/time between last two defrosts;
  - `087D` runtime/time since last defrost.
- Core heating semantics stable across public ATEC+iTec profiles:
  `03E9` Heating Min, `03EA` Heating Max, `03EC` Curve 0, `03ED` Curve -5, `03EE` Heating Stop, `03F0` Room Factor.
- `0559` Link Integration is a strong cross-profile semantic mapping; local XTR semantic effect/write remains separately unproven.

## PROFILE-SPECIFIC / do not universalize

- Public Online `registerIndex` values are **profile/model scoped**.
- `042E` is a concrete conflict:
  - ATEC/DHP-AQ profile: Integral A1;
  - iTec profile: Hot Water Status 0/1;
  - genuine modern Eco5 `042E:1->0` strongly supports the iTec interpretation for that profile;
  - local XTR `042E` semantic identity remains separately tracked.
- Older Diplomat/NCP profiles place common semantics at other numeric indices; do not use one public map as a universal XTR schema.

## CALENDAR — STRONGLY SUPPORTED / PARTLY LOCALLY PROVEN

Ordinary calendar logical layout:

- F1 `055A..05BB`
- F2 `05BC..061D`
- F3 `061E..067F`
- F4 `0680..06E1`
- tail `06E2..06E5`

Each function = 8 × 12-word records + 2 metadata words.

Record fields are strongly reduced to mode, start minute/hour/day/month/year, stop minute/hour/day/month/year, weekday mask. Metadata0 is strongly supported as slot-validity bitmap.

F1 = WW_GEBLOKKEERD is locally correlated. F2/F3/F4 names remain hypotheses.

No nonzero W0 and no FC03 desired read of the calendar transport pages was observed in the current genuine capture corpus. Calendar write behavior is therefore OPEN.

## FIRMWARE-DERIVED

Link CC 2.7.42 proves:
- an HE heat-pump identity/binding layer;
- DHP/HE semantic parameter model;
- grouped synchronization and integration-mode behavior.

It does **not** expose the final Thermia-native `0x0F` page serializer in the recovered managed assemblies.

Official hardware/document evidence narrows:
- old AQ/Atec/iTec serializer target -> DCM03;
- modern XTR serializer/protocol target -> Thermia Connect / protocol packages.

No DCM03/Connect binary or protocol package has yet been recovered.

## OPEN / UNKNOWN

- exact local-XTR activation/re-activation prerequisite for the full Online/DCM scheduler;
- any nonzero W0 desired-state behavior;
- unobserved W1 desired bits;
- exact semantics of W5;
- local XTR semantic identity of remaining profile-dependent fields including `042E/042F`;
- alarm-history raw-code -> user-facing alarm-name/E-code translation;
- native current-alarm bridge for firmware ErrorCode/AlarmField semantics;
- `085F/count5` semantics;
- calendar weekday bit order, delete semantics and cross-page write atomicity;
- Thermia Connect protocol-package contents and update manifests.

## DISPROVEN / SUPERSEDED

- the four Sep24/25 genuine Online/DCM captures as historical local-XTR captures;
- page-size differences in those captures as proven temporal XTR page-shape drift;
- `W2/W3=7FFF/FFFF` as opaque join magic — it is a concrete state-upload bitmap;
- universal `W5=6 normal / 7 join`;
- public Online registerIndex as one universal Thermia semantic map;
- `03F1 = HotWaterStart` as an XTR mapping;
- `0872..0878` as seven consecutive operating-time counters;
- direct conversion of raw `0884` event identifiers into displayed XTR `E###` fault numbers.

## Safety

- Do not transmit unobserved W0 bits or infer desired selectors by symmetry.
- A semantic register label does not imply its desired-state path is known.
- A public profile's writable flag does not authorize an XTR write.
- Desired-state responses must be built from fresh local authoritative page state; mutate one target only.
- Do not replay complete foreign-model payloads because their page address/count matches.
- Keep calendar and alarm/history work passive unless a separate bounded active experiment explicitly defines the transaction and rollback.
- EXP388 remains RUNNING / PARTIAL until its remaining recovery branches are actually tested.

---

# 2026-10-02 — PROTO-OFFLINE-01 unknown-page correlation

## STRONGLY SUPPORTED / locally correlated — 04A6/04A7 follow SG operating state

In the later local XTR DCM-style runtime:
```text
SG Normal   (0-0) -> 04A6=0000, 04A7=0000
SG Enhanced (0-1) -> 04A6=0041, 04A7=0001
SG Blocked  (1-0) -> 04A6=0042, 04A7=0001
```

Returning to Normal returns the pair to `0000/0000`.

This is a strong local SG/operational-state correlation. It is **not** an Online/DCM approval marker: genuine Eco5 approval/challenge activity is observed with both zero and non-zero `04A6`.

An older local XTR capture contains the radically different `04A6/count13` payload `0000,0003,0004,0002,003F,0050,003C,0002,0000,003C,000F,001E,0000`. Therefore the complete page must not be assigned one fixed SG-only schema across all historical/session contexts.

### HYPOTHESIS retained

The low two bits of a non-zero `04A6` may encode the SG input combination, suggesting `0043` as a possible `(1-1)` state. This value has not been observed.

## STRONGLY SUPPORTED — 0424 = Returnline Temperature Max Limit

The external DHP/AQ contiguous service sequence is independently anchored on this XTR by `041D` = Hot Water Start Temperature and `041E` = Hot Water Operating Time. Continuing that same sequence places `0424` at Returnline Temperature Max Limit. Observed local/genuine values are plausible, but no controlled XTR UI change has yet made this local proof.

## PROVEN / directly observed structural relation — 06F4 context mirror

Across local XTR evidence and all compared genuine Eco5 `06F4/count19` frames:
```text
06F4 = A80C
06F5 = A80D
06F6 = A80E
06F7 = A80F
06F8 = A810
0701 = AFDC
```

This proves the copy/mirror relationship only; it does not independently establish the semantic meaning of the source fields.

### Strong conclusion

`06F4/count19` is at least partly a controller/integration-context snapshot in the native `0x0F` page family, not merely a static configuration page. The remaining `06F4` words stay OPEN / UNKNOWN.

---

# 2026-10-02 — Calendar structure refinement from local XTR + genuine Eco5 evidence

## PROVEN / locally confirmed — WW_GEBLOKKEERD uses 055A desired-page path

A local XTR M calendar edit for WW_GEBLOKKEERD is directly correlated with:
`0708/count6 -> W0 bit1 + W2 bit1 -> FC03 055A/count33 -> controller FC16 republish`.

This locally anchors the Hot Water Blocked calendar function to the native `055A` page-owned desired-state mechanism.

## STRONGLY SUPPORTED — corrected 98-word ordinary-calendar blocks

The 12 native count33 pages from `055A` through `06C5` cover 396 contiguous words through `06E5`.

The best structural reduction is:

```text
F1 055A..05BB
F2 05BC..061D
F3 061E..067F
F4 0680..06E1
tail 06E2..06E5
```

Each F block is exactly 98 words:
`8 × 12-word records + 2 metadata words`.

The prior interpretation of three native pages = one 99-word calendar function is **DISPROVEN / SUPERSEDED**. Logical function and record boundaries cross native 33-word transport-page boundaries.

## STRONGLY SUPPORTED — 12-word record and occupancy metadata

Best record layout:

```text
mode,
start minute/hour/day/month/year,
stop minute/hour/day/month/year,
weekday/recurrence mask
```

Local date-mode entry:
`0,0,18,2,10,26,0,19,2,10,26,0`.

Genuine weekly-looking records use mode `1` and can end in `127`, compatible with a seven-day mask.

Candidate 8-bit slot-validity/occupancy words:
`05BA`, `061C`, `067E`, `06E0`.

Observed occupancy counts match these bitmaps in historical local XTR and genuine Eco5 snapshots. An inactive group can retain record-shaped residue while its candidate bitmap is zero, strengthening the validity-bit interpretation.

## HYPOTHESIS — function ordering

Only F1 is locally anchored:
- F1 = WW_GEBLOKKEERD — local anchor.

Manual-order candidates only:
- F2 = EVU / power limiting;
- F3 = Silent Mode;
- F4 = Temperature Reduction.

F2-F4 remain **HYPOTHESIS** until local UI correlation.

## STRONGLY SUPPORTED — concrete drying at 04D8/count27

`04D8/count27` contains a 7-word header followed by exactly ten `(day/point index, supply temperature)` pairs.

This matches the commissioning manual's maximum ten concrete-drying points, day range 1..40, temperature range 15..55 °C and hysteresis factory value 2.

Current status:
- block identity as concrete-drying configuration: **STRONGLY SUPPORTED**;
- ten point pairs: **STRONGLY SUPPORTED**;
- header word5=hysteresis and word6=point count: **STRONGLY SUPPORTED**;
- header words0..4: **OPEN / UNKNOWN**.

## STRONGLY SUPPORTED — 06EA clock/date block

`06EA/count7` fits:
`second, minute, hour, day, month, year, weekday`
across local XTR and genuine Eco5 snapshots.

It should no longer be treated as ordinary calendar or concrete-drying storage.

## STRONGLY SUPPORTED observed relation / OPEN semantics — 06E2..06E5

Across the local XTR and both genuine Eco5 datasets checked:

```text
(06E3 << 8) | 06E2 == 0870.word0
```

Examples:
- XTR: `00CE,0055 -> 55CE`;
- Eco5: `006B,0004 -> 046B`;
- Eco5: `006C,0004 -> 046C`.

The equality is repeatedly observed. Its semantic meaning remains **OPEN / UNKNOWN**; do not label it as checksum, pointer or calendar ID.

---

# 2026-10-02 — combined genuine iTec Eco5 Online approval evidence

## STRONGLY SUPPORTED / genuine Eco5 Online capture evidence — approval opens configuration synchronization

This is **not local XTR M or local Eco8 proof**. It is direct raw-capture evidence from two genuine iTec Eco 5 installations with a Thermia Online gateway.

Across `itec_eco5_gateway_20260926.log` and `itec_eco5_gateway_20260928.log`:

- six successful exact `0x0F FC17` `071C/0730` approval responses are observed;
- every successful gateway response is followed by controller `FC16 03E8/count14`;
- response -> first-`03E8` delay is 92..482 ms;
- successful responses occur at challenge ordinal #29 four times and #3 twice;
- the six response bodies are different.

### Strong conclusion

For the captured Eco5 systems, native Online session entry is directly tied to the `071C/0730` approval exchange and the configuration synchronization path starts at `03E8/count14`.

The captures do **not** support a universal static FC17 response and do not reveal the challenge-response derivation.

## STRONGLY SUPPORTED / genuine Eco5 Online capture evidence — FC16 ACK controls initial page progression

Where the first `03E8/count14` page is immediately ACKed, the controller proceeds:

`03E8/14 -> ACK -> 03FC/11 -> ACK -> 0410/22 -> ACK -> 042E/15 -> ...`

Two challenge-#3 sessions in the 20260928 capture have no immediate `03E8` ACK. In each window, the controller emits nine `03E8/count14` frames during the following 10 s and does not progress to `03FC` during that window.

This directly supports the address/count ACK as part of initial synchronization progression on genuine Eco5 Online traffic.

## OPEN / UNKNOWN — mismatched replay acceptance on iTec Eco

The exact response `1691A5F3F8E8D58738924416E8E6A3D5` is a genuine Eco5 gateway response to one specific challenge.

Local XTR M work proves that this recorded response can be accepted there against a different live challenge. The genuine Eco5 captures do **not** prove that Eco itself tolerates such a mismatch.

ECO-WRITE-01 is therefore narrowed to this single unknown. Challenge #3 is used because it is an actually successful genuine Eco5 gateway-response ordinal in two captured sessions; challenges #1 and #2 remain capture-only.

No Eco semantic write is promoted by this offline evidence.

---

## PROVEN / locally confirmed — EXP386 native DCM controller-restart recovery

The full recovery path is now locally confirmed on the tested Thermia iTec XTR M:

```text
unqualified stage40
  -> exact 071C/0730 outside guard: NO TX, remain listening
  -> >=5 s complete controller bus silence
  -> stage 1 recovery armed
  -> first valid frame after silence: BOOT_RETURN -> stage 2
  -> A80E=0000 / A80F=0005
  -> exact 071C/0730 challenge
  -> one proven R1 replay
  -> first post-R1 FC16 = 03E8/count14
  -> ordered initial FC16 sync + existing address/count ACK chain
  -> final initial page = 06F4/count19
  -> stage40 persistent runtime
  -> fresh known runtime FC16 ACK
  -> 0708 idle reply
  -> runtime qualified / recovery positive
```

Durable findings:
- exact `071C/0730` is a necessary observed session event but is not by itself permission for R1;
- R1 replay remains locally permitted only under known `A80E=0000 / A80F=0005`;
- challenges seen at `A80E=0008 / A80F=0032` are capture-only and must not trigger R1;
- >=5 s complete bus silence followed by a valid returning frame is locally confirmed as a usable controller-restart boundary for this implementation;
- completing the initial FC16 export is not sufficient to call the session recovered: fresh runtime service must subsequently qualify;
- the successful EXP386 run qualified on fresh runtime FC16 ACK + `0708` idle reply;
- parser integrity for the successful run remained clean (`resync=0`, `drops=0`);
- EXP386 changed state gating only; the known R1 and hard-coded FC16 ACK payloads were unchanged.

### STRONGLY SUPPORTED interpretation

The earlier v4.0 DCM activation failures were implementation/session-state regressions, not evidence against the underlying native DCM session model.

---

# 2026-10-01 — EXP380 through EXP383 consolidation

## PROVEN / locally confirmed — 0546/count20 semantic write path

EXP380 was explicitly confirmed successful by the user. `0553` / word13 Operation Mode is therefore **PROVEN / locally confirmed writable** on this XTR M through the native 0546/count20 desired-page mechanism.

This extends the locally proven page-owned semantic-write model to four controlled pages:
- 03E8/count14
- 042E/count15
- 0442/count13
- 0546/count20

The same safety rule remains: success requires an authoritative fresh page, exactly one intended selected-word change in the desired response, and an exact controller FC16 republish with `extraDeltaWords=0`.

## PROVEN / locally confirmed — EXP381B behavior-preserving consolidation

EXP381B was run and explicitly reported successful. Manual-aligned Configuration ordering and read-only visibility cleanup did not regress the established native write behavior. This is the current proven runtime baseline.

## STRONGLY SUPPORTED — EXP382 candidate mappings

Offline EXP382 strengthened the following mappings without transmitting anything to the heat pump:

- `0430` = Hot Water TOP_UP
- `0444` = INFORMATION Cooling Hysteresis
- `0446` = SERVICE Cooling Configuration/Type
- `0448` = SERVICE Cooling STOP threshold
- `044A` = Cooling MAX_STARTTEMP
- `044B` = Cooling MIN_STOPTEMP
- `0559` = Link Integration

These remain **STRONGLY SUPPORTED**, not PROVEN.

Evidence basis:
- 0430 follows the locally mapped 042E Hot Water Enabled and 042F Mode fields exactly where the commissioning manual places TOP_UP in the user-facing Hot Water sequence.
- 0449..044E aligns exceptionally well with the SERVICE cooling tail: Cooling Time → MAX_STARTTEMP → MIN_STOPTEMP → Room Sensor → low room hysteresis → high room hysteresis. The latter four/tail fields already have local proof where stated.
- 0444 is compatible with the INFORMATION Cooling Hysteresis position and genuine capture value/scaling evidence.
- 0446 values are compatible with the documented UIT / ACTIEVE_KOELING / GEÏNTEGR. IN WP configuration enum.
- public Online/DCM register-index evidence explicitly identifies decimal 1369 / hex 0559 as Link Integration.

## HYPOTHESIS — 0447 Cooling START threshold

The position strongly suggests the SERVICE cooling START threshold, but the encoding/value evidence is not clean enough for STRONGLY SUPPORTED status. It is intentionally omitted from EXP383.

## OPEN / UNKNOWN retained

No new labels are assigned to:
- 03F1, 03F2, 03F3, 03F5
- 0431, 0432, 0435..043C
- 0546..0552, 0554..0558
- the exact encoding/semantics of 0447

## EXP383 — TEST-only implementation, not evidence promotion

Write Beta v4.0 implements seven candidate controls using the already proven page mechanisms. Their Home Assistant display names contain `TEST`. Implementation does **not** promote protocol confidence. Each candidate must be locally correlated and, where written, rolled back individually before its status can become PROVEN.

0559 Link Integration is treated as the highest-risk candidate because changing integration mode may alter the Online/DCM-style session. It should be tested last and without automatic retry.

---

# THERMIA PROTOCOL FINDINGS

# 2026-10-01 — multi-page semantic writes through EXP379

## PROVEN / locally confirmed — native semantic writes now span three settings pages

The same controller-owned full-page desired-state mechanism is locally proven on:
- `03E8/count14` heating page
- `042E/count15` DHW/runtime-service page
- `0442/count13` cooling page

Common flow:
`fresh controller FC16 page -> desired selector on 0708 -> controller FC03 page -> emulator full page with exactly one intended word changed -> controller FC16 republish -> accept only target match + extraDeltaWords=0`.

This is stronger evidence for a generic native page-cache/control model than for independent register writes.

## PROVEN / locally confirmed — 03E8/count14 writable map

Writable on this XTR M:
- `03E8` Heating Curve
- `03E9` Heating Minimum
- `03EA` Heating Maximum
- `03EB` Curve Correction +5
- `03EC` Curve Correction 0
- `03ED` Curve Correction -5
- `03EE` Heating Stop
- `03EF` Reduced Temperature
- `03F0` Room Factor
- `03F4` Room Setpoint

Unknown: `03F1`, `03F2`, `03F3`, `03F5`. `03F1` is specifically disproven as the live DHW START mapping on this XTR M.

## PROVEN / locally confirmed — 042E/count15 map and selector

Locally established:
- `042E` SWW Enabled
- `042F` SWW Mode
- `0433` Opstart HT
- `0434` Verwarmingstijd

Semantic write proof:
- EXP377 changed `042F: 1 -> 0` with exact controller republish and `extraDeltaWords=0`.
- EXP378 confirmed `0433: 5 -> 7 -> 5`.

Current/PUSH selector for 042E is W3 bit3:
`0F030C0000000000000008000000067CB7`.

Desired selector uses W1 bit3 + W3 bit3:
`0F030C0000000800000008000000061B77`.

`0430` is **HYPOTHESIS** for Extra Hot Water / Top-up only. It is not locally proven.
`0431` and `0432` are **OPEN / UNKNOWN**; the earlier START/STOP interpretation is rejected.

## PROVEN / locally confirmed — 0442/count13 cooling map

Writable on this XTR M:
- `0442` Cooling Enabled
- `0443` Desired Cooling Temperature
- `0445` Cooling Active Above
- `0449` Cooling Time
- `044C` Cooling Room Sensor
- `044D` Cooling Room Hysteresis Low
- `044E` Cooling Room Hysteresis High

Unknown: `0444`, `0446`, `0447`, `0448`, `044A`, `044B`.

### Cooling Active Above guard

Locally confirmed guard:
`minimum Cooling Active Above = max(10 °C, Heating Stop + 3 K)`.

With Heating Stop 22 °C, a requested 24 °C was blocked before semantic TX; 25 °C and 27 °C were accepted in the tested sequence.

### Cooling room hysteresis encoding and limits

Both Low and High use raw/10 °C:
- raw 10 = 1.0 °C
- raw 17 = 1.7 °C
- raw 18 = 1.8 °C

Documented/UI limits are `0.5..5.0 °C`, step `0.1 °C`, therefore raw `5..50`.

## STRONGLY SUPPORTED — 0708 high-half page mapping and 0546 selector basis

Genuine Online/DCM/Eco5 reduction maps the 32 current/PUSH pages across W3 then W2. In particular:
- W3 bit3 -> 042E
- W3 bit4 -> 0442
- W2 bit0 -> 0546

For desired/PULL, low-half pages use W1 and the genuine high-half model mirrors the page bit into W0. Therefore EXP380 is prepared with W0 bit0 + W2 bit0 for 0546 desired selection.

This 0546 desired selector is **not yet locally write-proven**.

## STRONGLY SUPPORTED / local read-side evidence — 0553 Operation Mode

`0553` is word 13 of `0546/count20`.

Local XTR panel-driven evidence confirms:
- 1 = Auto
- 2 = Compressor
with observed `1 -> 2 -> 1`.

Accepted genuine/cross-model working enum for EXP380:
- 0 = Uit
- 1 = Auto
- 2 = Compressor
- 3 = Bijverwarmer
- 4 = Warmwater

Active semantic writeability of 0553 remains unproven until EXP380 is run.

## Current remaining high-value unknowns

- `0430` Extra Hot Water / Top-up candidate
- remaining DHW service settings
- remaining heating/cooling service settings
- calendar structure/write semantics
- auxiliary-heater settings
- shunt-group settings
- pool settings
- optional buffer-tank/accessory settings
- `03F1/03F2/03F3/03F5` and remaining unknown page words
- native challenge-response derivation

---

# 2026-10-01 — full confirmed writable core of 03E8/count14

## PROVEN / locally confirmed — writable settings

The native desired-page mechanism is now locally confirmed across the practical heating/settings core of `03E8/count14`:

- `03E8` Heating Curve
- `03E9` Heating Minimum
- `03EA` Heating Maximum
- `03EB` Curve Correction +5
- `03EC` Curve Correction 0
- `03ED` Curve Correction -5
- `03EE` Heating Stop
- `03EF` Reduced Temperature
- `03F0` Room Factor
- `03F4` Room Setpoint

`03E9` and `03F0` were explicitly user-confirmed positive in EXP375A/B. `03EB` and `03EC` were explicitly confirmed through the successful multi-setting queue test. These confirmations are sufficient for local project status, but raw final-run logs were not separately supplied for those specific confirmations.

## PROVEN / locally confirmed — serialized queue behavior

EXP374's final v4d implementation preserves multiple pending register intents without overlapping Thermia semantic transactions. Each register is dispatched separately and must acquire a fresh controller-originated `03E8/count14` page before the existing selector -> FC03 pull -> one-word desired page -> exact FC16 republish sequence.

Configuration presentation is intentionally not identical to instantaneous controller state while a queue is pending:
- ordinary read sensors = actual controller state;
- Configuration numbers = active target, else queued target, else controller state.

This is UI/state separation only; it does not broaden the protocol write mechanism.

## DISPROVEN / SUPERSEDED implementation assumptions

- A single global pending slot/debounce is sufficient for rapid changes across multiple settings — superseded by the per-register dirty-set.
- Configuration controls should always republish every intermediate authoritative controller page — superseded because it makes queued desired intent appear to disappear and reappear.
- Heating Minimum requires a locally imposed Minimum < Maximum software guard — not Thermia protocol evidence and superseded by successful `03E9` writing.

## OPEN / UNKNOWN

- `03F1`, `03F2`, `03F3` and `03F5` remain semantically unknown on this XTR M.
- Prior local work specifically rejects `03F1` as the live DHW START mapping on this XTR M.
- Writeability outside `03E8/count14` must not be inferred from this page's success.
- Native challenge-response derivation remains unknown; fixed replay is only locally proven in its guarded XTR context.

---

# 2026-10-01 — semantic write expansion through EXP373

## PROVEN / locally confirmed

### Native desired-page semantic-write mechanism is reusable across multiple settings

The XTR M semantic write path is no longer proven only for Room Setpoint. The same guarded flow has now been locally confirmed for multiple words in the `03E8/count14` page:

`fresh controller FC16 03E8/count14`
-> desired-page selector on `0708`
-> controller `FC03 03E8/count14`
-> emulator returns the full page with exactly one intended word changed
-> controller republishes `FC16 03E8/count14`
-> success only when selected word equals target and `extraDeltaWords=0`.

EXP365–370 prove that this mechanism is reusable in one healthy runtime session and is not inherently a one-shot write path.

### Confirmed writable fields

- **`03E8` Heating Curve — PROVEN writable.** Confirmed examples include `30 -> 31 -> 30`, `30 -> 35`, `35 -> 32/35` during verifier-development runs, and reusable `35 -> 40 -> 30`. Exact controller republish with one-word delta was observed.
- **`03EA` Heating Maximum — PROVEN writable.** Confirmed sequence includes `40 -> 41 -> 58 -> 40`, with exact controller republish and no extra delta words.
- **`03ED` Curve Correction -5 — PROVEN writable.** EXP373 confirmed `0 -> -5 -> 0`; `-5` is transported as signed int16 `0xFFFB`.
- **`03EE` Heating Stop — PROVEN writable.** EXP373 confirmed `20 -> 22` and `22 -> 18 -> 22`.
- **`03EF` Reduced Temperature — PROVEN writable.** EXP373 confirmed `20 -> 22 -> 20`.
- **`03F4` Room Setpoint — PROVEN writable through the native desired-page flow.** Prior proof remains valid, and reusable writes were again observed in EXP370.

For all promoted write findings above, the controller republished the full `03E8/count14` page with the intended selected word changed and `extraDeltaWords=0`.

### No-op suppression is locally confirmed

When a fresh controller page already contains the requested target, the write state machine can close READY without sending a semantic desired page. EXP373 demonstrated this for `03EF` at 20.

### Controller reboot recovery remains locally proven after production hardening

EXP358 confirmed the v2.1 hardening did not break retained runtime, fresh-page refresh or the established Room Setpoint write path. EXP359 then repeated controller cold-reboot recovery: >5 s silence gate, guarded fresh-session bootstrap, full ordered sync through `06F4/count19`, stage-40 re-entry and post-recovery runtime qualification all completed with clean parser/RX health.

## STRONGLY SUPPORTED

### Semantic control is page-owned, not arbitrary direct-register write behavior

The growing set of successful one-word changes all use the same full-page desired-state exchange and exact controller republish. This strongly supports a page ownership/synchronization model for `03E8/count14`, rather than treating each setting as an independent Modbus master write target.

### Signed 16-bit interpretation applies to curve-correction words

Local EXP373 write evidence proves signed int16 handling at least for `03ED` because `-5` is represented as `0xFFFB` and was accepted/re-published exactly. The neighboring correction fields are still not promoted as writable without their own local confirmation.

## OPEN / UNKNOWN

- **`03E9` Heating Minimum writeability:** not yet locally proven. A recent attempt was blocked by a local software guard before semantic TX. Do not treat Minimum < Maximum as a Thermia protocol rule on that basis.
- **`03EB` Curve Correction +5 writeability:** mapping is locally established on the page, but no clean local write confirmation is recorded in the current EXP373 evidence.
- **`03EC` Curve Correction 0 writeability:** same status as `03EB`.
- **`03F0` Room Factor writeability:** strongly indicated by mapping/cross-model evidence but not locally write-confirmed here.
- Native hot-rejoin behavior remains unresolved. EXP360–364 produced mixed/inconclusive transport observations and do not establish a general no-R1 rejoin algorithm.
- Queueing multiple user requests safely is not yet proven. EXP374 is prepared specifically to test scheduling safety without changing the proven wire protocol.

## DISPROVEN / SUPERSEDED implementation assumptions

- A semantic write need not be limited to +/-1 changes: larger Heating Curve and Heating Maximum deltas were accepted and exactly republished.
- A semantic write need not be one-shot per ESP/runtime session: EXP370 proved reusable serialized writes.
- The previous local Minimum < Maximum guard must not be presented as Thermia protocol behavior; it blocked an experiment before any semantic TX and is therefore only an implementation constraint.

---

# 2026-10-01 — EXP357 durable findings

## PROVEN / locally confirmed — reusable W3-bit0 stale-cache refresh

The `0708/count6` response:

`W0..W5 = 0000,0000,0000,0001,0000,0006`

can be reused later in the same ESP boot to request another fresh controller-originated `FC16 03E8/count14` page.

EXP357 directly observed:
- refresh #1 confirmed in ~120 ms;
- refresh #2 confirmed in ~119 ms later in the same ESP boot.

Therefore the earlier one-refresh-per-boot limit was experimental only and is **DISPROVEN / SUPERSEDED** as a required safety constraint for this XTR M.

## PROVEN / locally confirmed — reusable refresh can safely feed the semantic write path

After refresh #2, the fresh controller `03E8` page became the write source and a 22 -> 24 °C Room Setpoint change completed through:
`W1-bit0 selector -> controller FC03 03E8/count14 -> one-word 03F4 delta -> exact controller FC16 republish`.

The confirming republish had `extraDeltaWords=0`.

## Production consequence

Write Beta v2 may perform stale-cache refresh whenever the `03E8` cache is missing or older than 300 s, provided no other semantic transaction is active. Each refresh still requires a new controller-originated `FC16 03E8/count14` before any semantic page response is allowed.

---

# 2026-10-01 — offline re-analysis of genuine Online/DCM and Eco5 gateway captures

No new live experiment was performed. These findings come from re-analysis of existing raw captures and are kept separate from the locally active-tested XTR M results.

## STRONGLY SUPPORTED — complete 0708 W2:W3 32-page current/PUSH bitmap

A genuine DCM capture contains a `0708/count6` response with:

`W0..W5 = 0000,0000,7FFF,FFFF,0080,0007`

Immediately afterward the controller publishes the ordered configuration pages beginning at `03E8`. The observed sequence and independent Eco5 gateway single/few-bit cases fit one consistent 32-page mapping:

- `W3 bit0 -> 03E8`
- `W3 bit1 -> 03FC`
- `W3 bit2 -> 0410`
- `W3 bit3 -> 042E`
- `W3 bit4 -> 0442`
- `W3 bit5 -> 0456`
- `W3 bit6 -> 046A`
- `W3 bit7 -> 047E`
- `W3 bit8 -> 0492`
- `W3 bit9 -> 04A6`
- `W3 bit10 -> 04BA`
- `W3 bit11 -> 04D8`
- `W3 bit12 -> 04F6`
- `W3 bit13 -> 050A`
- `W3 bit14 -> 051E`
- `W3 bit15 -> 0532`
- `W2 bit0 -> 0546`
- `W2 bit1 -> 055A`
- `W2 bit2 -> 057B`
- `W2 bit3 -> 059C`
- `W2 bit4 -> 05BD`
- `W2 bit5 -> 05DE`
- `W2 bit6 -> 05FF`
- `W2 bit7 -> 0620`
- `W2 bit8 -> 0641`
- `W2 bit9 -> 0662`
- `W2 bit10 -> 0683`
- `W2 bit11 -> 06A4`
- `W2 bit12 -> 06C5`
- `W2 bit13 -> 06EA`
- `W2 bit14 -> 06F1`
- `W2 bit15 -> 06F4`

Cross-checks from genuine Eco5 gateway traffic include:
- W3 bit15 together with W2 bit14 followed by controller publications for `0532` and `06F1`;
- W2 bit15 followed by controller `FC16 06F4/count19`.

**Status:** the full W2:W3 map is **STRONGLY SUPPORTED** by genuine DCM/Eco5 capture evidence. Only W3 bit0 -> `03E8` is currently **PROVEN / locally confirmed** by active XTR M testing (EXP352). Do not promote the other bits to local proof.

## STRONGLY SUPPORTED — W1 is a desired/PULL page selector using the same page-index family

Existing genuine captures provide direct examples:
- W1 bit0 is followed by controller `FC03 03E8` and a gateway page response;
- W1 bit3 is followed by controller `FC03 042E/count15`, then the gateway page response and controller republish.

This strongly supports W1 as the desired/PULL bitmap for the same ordered page family used by W3/W2 for current/PUSH advertisement.

**Local status:** W1 bit0 -> desired `03E8` is locally proven on this XTR M. W1 bit3 -> `042E` is cross-model/genuine-gateway evidence only.

## PROVEN / genuine Eco5 gateway capture — challenge response is session/challenge dependent

The exact `071C/0730` challenge does not receive one constant 16-byte response from a genuine gateway.

One captured pair is:

- challenge payload: `63CEFB32C6F41382087992370CACEeba`
- gateway response payload: `1691A5F3F8E8D58738924416E8E6A3D5`

A later session shows a different pair:

- challenge payload: `31FB59FC8FB1175CD89F904D06D92EA4`
- gateway response payload: `FD636CCD0F921D83FF232A1A2413B372`

Therefore the official gateway behavior uses a challenge-dependent/session-dependent response. The transform or cryptographic construction remains unknown.

## PROVEN / locally confirmed — fixed response replay is accepted on this XTR M

EXP355 replayed the previously captured payload:

`1691A5F3F8E8D58738924416E8E6A3D5`

under the locally proven cold-boot guard `A80E=0000 / A80F=0005`, even though the live challenge differed from the challenge that originally produced that response in the genuine gateway capture. The XTR M accepted the replay, published `03E8/count14`, completed the full ordered initial sync, and returned to qualified stage 40.

**Durable distinction:**
- genuine gateway: response varies with challenge/session;
- this XTR M: one captured response is replayable in the tested guarded context;
- unknown: whether replay works across other Thermia models, firmware versions, or every future session.

The fixed response must therefore be documented as a **locally proven replay value**, not as “the Thermia R1 algorithm” or a universal native response.

## STRONGLY SUPPORTED — at least two native Online/DCM lifecycle paths exist

Existing capture evidence is consistent with two distinct integration lifecycles:

1. **Controller cold boot with accessory present:** cold-boot state -> exact challenge -> challenge-dependent gateway response -> ordered initial sync -> runtime.
2. **Accessory/gateway rejoin while controller is already running:** `0708` response advertises a broad current-page bitmap -> controller exports requested pages -> runtime continues.

The first path is now locally emulated/recovered on this XTR M through EXP355 using a replayed response. The second hot-rejoin/page-bitmap path is genuine-capture-supported but has not been locally emulated and should not be assumed production-proven.

## STRONGLY SUPPORTED — A80E/A80F are lifecycle/state fields, exact semantics still unknown

EXP355 locally observed:

`0000/0005 -> 0008/0005 -> 0028/0005 -> 0028/000A`

Existing genuine capture evidence shows the same `0028/0005` early-session state and later `0028/000A` operation.

This further supports:
- `A80F=0005` as associated with an early integration/bootstrap phase;
- `A80F=000A` as a later operating state in this sequence;
- A80E behaving like a progressive/status bitfield.

**OPEN / UNKNOWN:** do not assign protocol names such as “connected”, “authenticated”, or “sync complete” to A80E/A80F without stronger evidence.

---

# 2026-09-30 — EXP355 durable findings: controller cold-reboot recovery

## PROVEN / locally confirmed — controller power-cycle recovery without ESP reboot

EXP355 demonstrates on this XTR M that an already-running ESP/DCM emulator can recover after the Thermia/controller itself is power-cycled while the ESP remains powered.

The tested lifecycle was:

`qualified retained stage40 -> sustained bus silence -> fresh controller bus return -> guarded fresh-session bootstrap -> ordered initial-sync -> stage40 -> fresh runtime qualification`

The implementation detected 5166 ms of bus silence before arming recovery. This >=5 s value is a proven working local implementation threshold, not a universal protocol rule.

## PROVEN / locally confirmed — fresh-session cold-boot guard and one-R1 path during recovery

After bus return the controller presented `A80E=0000 / A80F=0005`. The first exact `071C/0730` challenge then triggered exactly one already-known R1:

`0F17101691A5F3F8E8D58738924416E8E6A3D5E227`

Recovery required no ESP reboot and introduced no new payload.

## PROVEN / locally confirmed — full ordered initial-sync chain is sufficient to return to runtime

After R1 the controller began the known config publication sequence at `03E8/count14`. EXP355 ACKed all 32 expected page/count stages in order through `06F4/count19`.

The final `06F4` ACK returned the emulator to stage 40. Fresh `085F/count5` runtime traffic and an exact `0708/count6` exchange then requalified the recovered runtime.

## PROVEN / locally confirmed — fresh-session 03E8 page restores semantic cache provenance

The first post-R1 `FC16 03E8/count14` was controller-originated in the new session and contained `03F4=22`. EXP355 promoted it to the semantic cache.

This proves that fresh-session recovery itself can re-establish a controller-originated `03E8` source page. EXP355 did not test a subsequent semantic write from that recovered cache.

## STRONGLY SUPPORTED — A80F=0005 is associated with the early fresh-session/bootstrap window

Before controller reboot, normal retained runtime repeatedly showed:

`A80E=0000 / A80F=000A`

After bus return and before R1, EXP355 observed:

`A80E=0000 / A80F=0005`

During initial synchronization the observed state progressed:

`0000/0005 -> 0008/0005 -> 0028/0005 -> 0028/000A`

This strongly supports treating `A80F=0005` as associated with the early fresh-session/bootstrap window and `000A` as a later operating state in this observed sequence. The exact abstract semantics of A80E and A80F remain **OPEN / UNKNOWN**.

## OPEN / UNKNOWN

- Repeated controller power cycles in one ESP boot have not yet been locally proven.
- Recovery from arbitrary interruption points inside the initial-sync chain has not been tested.
- The >=5 s silence threshold is not established as a universal Thermia/DCM requirement.
- A semantic `03F4` write immediately after recovered-session bootstrap was deliberately not tested.
- Other writable registers/pages remain unproven.

---

# 2026-09-30 — EXP352 durable findings: local 03E8 PUSH refresh and runtime/cache separation


## STRONGLY SUPPORTED / user-confirmed follow-up — reusable 03E8 refresh across one boot (EXP353)

- EXP352 provides raw-log **PROVEN / locally confirmed** evidence for one W3-bit0 current-page refresh of `03E8`, followed by the guarded `03F4` write and exact controller republish.
- EXP353 was subsequently explicitly confirmed successful by the user for the reusable-refresh follow-up.
- The detailed EXP353 raw log/YAML is not currently archived, so exact multi-cycle counts/timings are not promoted here as raw-capture facts.
- Operationally, the Write Beta may use reusable refresh transactions while preserving the same per-transaction safety envelope.
- This does **not** generalize the W2:W3 bitmap to other pages and does not prove arbitrary long-term/power-loss recovery.


## PROVEN / locally confirmed — 0708 W3 bit0 requests a fresh current 03E8 page on this XTR M

EXP352 began with no write-eligible `03E8/count14` cache. On a user Apply, the emulator first sent **no semantic page values**. At the next exact `FC03 0708/count6` request it returned:

    W0..W5 = 0000 0000 0000 0001 0000 0006
    frame   = 0F030C000000000000000100000006A0B6

Here W1 remained zero, so no desired-page/PULL bit was advertised. About 120 ms later the controller itself published `FC16 03E8/count14` with current `03F4=23`. The log reported:

    REFRESH_CONFIRMED ... current03F4=23 ... latency=120ms
    source=controller_FC16_03E8_14 W1=0000 W3bit0=1
    NO_DESIRED_PULL=1 CACHE_FRESH=1

No `FC03 03E8/count14` desired-page pull preceded that refresh.

**Current status:** W3 bit0 -> current-page/PUSH refresh for page `03E8` is **PROVEN / locally confirmed** in the tested retained stage-40 context.

This upgrades only **bit0/page 03E8**. The remainder of the 32-bit W2:W3 page map remains **STRONGLY SUPPORTED** by genuine DCM/Eco5/ATEC captures until individually or generically validated locally.

## PROVEN / locally confirmed — retained runtime liveness is independent of a hard-coded 03E8 page image

EXP351 failed to enter active stage 40 because implementation code required persisted mapped settings to match a hard-coded historical handover page. That prevented the intended refresh experiment and produced an abnormal Online state.

EXP352 removed that equality prerequisite and intentionally started with:

    page_cache_valid = false

while retaining the same known-good runtime service. The XTR then qualified retained stage 40 normally, without Thermia reboot and without a new R1/bootstrap.

**Conclusion:** a historical exact `03E8` page image is **not required** for retained Online/DCM runtime liveness on the tested XTR session. Semantic page freshness/provenance must be handled separately from session/runtime qualification.

## DISPROVEN / SUPERSEDED — exact historical 03E8 handover equality as a runtime-entry prerequisite

The EXP351 implementation assumption that the persisted mapped settings must exactly match one prior `03E8/count14` page before activating retained runtime is superseded.

It was a local safety implementation, not a proven protocol requirement. EXP352 demonstrates successful retained runtime with no valid semantic page cache at boot.

## PROVEN / locally confirmed — native/controller 03E8 publications refresh the semantic source cache

During EXP352 normal stage-40 runtime, with no ESP semantic write pending, the controller independently published new `FC16 03E8/count14` pages.

Observed examples:

- controller publication with `03F4=22` -> emulator logged `03E8_CACHE_REFRESH current03F4=22 source=runtime_controller_FC16`;
- later controller publication with `03F4=19` -> emulator updated the cache to 19.

The user explicitly confirmed that **19 °C had been set on the Thermia front display**. Therefore the 19 °C event is locally tied to a native front-panel change. The exact physical source of the separate 22 °C event is left unresolved because both room-sensor and Thermia controls were used during the same run.

A later HA/ESP semantic transaction used the refreshed 19 °C controller page as its source and successfully changed `19 -> 21`.

**Conclusion:** the room-setpoint page cache can coexist with native physical control. A controller-originated `03E8` publication supersedes older cached state and is a valid source for a later guarded semantic write.

## PROVEN / locally confirmed — refresh + repeated semantic writes coexist in one retained runtime

After the W3-bit0 refresh, EXP352 completed six controller-confirmed ESP semantic writes in the same retained runtime:

    23 -> 25
    25 -> 17
    17 -> 23
    23 -> 21
    22 -> 21   (after native/controller cache update)
    19 -> 21   (after native Thermia-display cache update)

Each controller confirmation reported `extraDeltaWords=0`; controller republished the complete accepted `03E8/count14` page and the latest page was promoted as next-write source.

User confirmed no alarm and DCM icon remained visible.

## SUPERSEDED — EXP352 one-refresh-per-boot limit

EXP352 itself intentionally allowed only **one** W3-bit0 refresh-only request per ESP boot, so EXP352 alone did not prove repeated stale-cache refresh cycles.

That experiment-local limitation is superseded by EXP353, which the user explicitly confirmed as successful for the reusable-refresh follow-up. Because the detailed EXP353 raw log/YAML is not archived, exact cycle counts and timings remain unavailable and are not invented.

---

# 2026-09-30 — EXP347–349 retained-session reusable semantic control

## PROVEN / locally confirmed — retained session survives ESP OTA for semantic control

EXP347 proves that, on this XTR M, the already-established stage-40 Online/DCM controller session can be rejoined after an ESP OTA/reboot without rebooting the Thermia controller and without sending a new R1/bootstrap. Clean qualification used known runtime FC16 service plus exact `0708/count6` idle service with W5=0006. The guarded `03F4` write/rollback then worked while the user observed continuous DCM icon and no error.

## PROVEN / locally confirmed — HA-selected 03F4 target

EXP348 replaced the fixed -1 °C test delta with an HA-selected whole-degree setpoint. The locally tested roundtrip was:

`22 -> 24 -> 22 °C`

Both write and explicit rollback were controller-confirmed by exact `FC16 03E8/count14` republish with `extraDeltaWords=0`. Normal Home Assistant Room Setpoint followed the semantic result.

This proves selection of at least the locally tested arbitrary target value through the same native desired-page path. It does **not** prove every value from 10..30 has been exercised.

## PROVEN / locally confirmed — repeated writes in one retained session

EXP349 proves that the same native path is reusable repeatedly within one continuously retained session when each successful controller republish is promoted to the source page for the next transaction.

Locally tested chain:

`22 -> 16 -> 24 -> 22 °C`

For all three writes:
- selector remained `W0..W5 = 0000 0001 0000 0001 0000 0006`;
- controller issued exact FC03 `03E8/count14`;
- emulator returned the full current controller-confirmed page with only `03F4` changed;
- controller republished exact FC16 `03E8/count14`;
- `extraDeltaWords=0`;
- runtime continued and the state machine returned READY for the next write.

The three confirmations were:
- writeNo=1: 22 -> 16;
- writeNo=2: 16 -> 24;
- writeNo=3: 24 -> 22.

This upgrades the implementation model from a reversible test transaction to a reusable native setpoint-control mechanism for the locally mapped `03F4` field.

## PROVEN / locally confirmed — implementation safety guards

Current experimental implementation applies both UI-level and write-lambda guards:
- requested setpoint must be integer 10..30 °C;
- current cached `03F4` must also be 10..30 before arming;
- a no-op target equal to current is refused;
- cache must be valid/fresh;
- exact page/start/count and clean retained runtime are required;
- only one semantic transaction may be outstanding;
- any additional page-word delta in controller republish is fail-closed.

The **10..30 °C range is locally observed from the native indoor-sensor/UI limit**. Treat it as a local safety constraint, not a proven universal Thermia/DCM protocol range.

## STRONGLY SUPPORTED — reusable page-cache architecture

The best current architecture is a bidirectional page cache:
1. controller-originated/current `03E8` page is cached;
2. pending desired page is advertised via `0708` W1 bit0;
3. controller pulls `03E8` with FC03;
4. emulator returns full cached page with one intended semantic delta;
5. controller republishes accepted current page with FC16;
6. exact republish becomes the authoritative source for the next write.

EXP349 directly validates step 6 for three successive local semantic transactions.

## OPEN / UNKNOWN

- Exact semantic meaning of W5=0006 remains unknown; it is only proven sufficient for connected/DCM indication persistence in the tested local context.
- Generality of the reusable write mechanism to pages/registers other than locally mapped `03F4` remains unproven.
- The 10..30 UI range is not established as a protocol-level encoded range.
- Long-duration production behavior and very high write counts have not yet been established; EXP349 was intentionally bounded to eight semantic responses per ESP boot.

---

# 2026-09-30 — EXP346 durable finding: persistent native semantic write + rollback

## PROVEN / locally confirmed — guarded 03F4 semantic control inside persistent DCM runtime

EXP346 combines the two previously separate local capabilities established by EXP343 and EXP345.

In a fresh XTR M Online/DCM-emulation session that had already reached persistent stage 40 with idle 0708 W5=0006:

- controller-originated `03E8/count14` was cached from the same session with `03F4=22`;
- a guarded 0708 desired-page selector advertised 03E8 while retaining W5=0006;
- the controller initiated `FC03 03E8/count14`;
- the emulator returned the same 14-word page with exactly one delta, `03F4 0016 -> 0015`;
- the controller republished `FC16 03E8/count14` with `03F4=0015` and no other page-word delta;
- Home Assistant room setpoint became 21 °C;
- persistent runtime continued and the user observed the DCM icon still present with no Online/Link error;
- a second guarded native transaction restored `03F4 0015 -> 0016`;
- the controller republished the restored page with zero extra deltas;
- Home Assistant room setpoint returned to 22 °C;
- persistent runtime and DCM indication again remained intact.

**Durable conclusion:** on this XTR M, the native Online/DCM mailbox + desired-page mechanism is sufficient for reversible semantic control of mapped register 03F4 **without leaving the persistent connected session**.

This is stronger than EXP343 alone (semantic application) and EXP345 alone (persistent DCM presentation): EXP346 proves the two behaviors coexist in one live session.

## PROVEN / locally confirmed — exact tested semantic roundtrip

Test:
`03F4 0016 (22 °C) -> 0015 (21 °C)`

Rollback:
`03F4 0015 (21 °C) -> 0016 (22 °C)`

Both controller republishes matched all 14 words of the expected page, with `extraDeltaWords=0`.

## PROVEN / locally confirmed — connected mailbox selector used during semantic write

The tested selector response was:

`0F030C000000010000000100000006AD26`

Decoded words:

`W0=0000 W1=0001 W2=0000 W3=0001 W4=0000 W5=0006`

In this tested context:
- W1 bit0 advertises desired page 03E8;
- W3 bit0 is simultaneously present in the connected selector used by EXP346;
- W5=0006 is retained from the proven persistent-connected baseline.

Do not over-interpret W3 bit0 as a required universal condition from this single combined test; the broader W2:W3 PUSH/current-page interpretation remains **STRONGLY SUPPORTED**, while exact selector composition rules outside the tested path remain to be generalized.

## OPEN / UNKNOWN

- exact semantic meaning of W5=0006;
- whether W3 bit0 is required for every 03E8 write while connected, versus simply reflecting current-page state;
- generality of the write path to other mapped pages/registers on XTR M;
- long-term repeated-write behavior without controller reboot;
- limits/range validation required for production-grade control.

---

# 2026-09-30 — Durable findings from EXP343–345

## PROVEN / locally confirmed — native desired-page semantic application

EXP343 proves that the native 0x0F desired-page path can apply a semantic value change on the tested iTec XTR M. After the authentic 03E8 PULL selector, the controller issued FC03 03E8/14; the emulator returned the same-session page with only 03F4 changed 0016 -> 0015; about 690 ms later the controller republished FC16 03E8/14 with exactly 03F4=0015 and no other payload delta; Room Setpoint Mirror and Room Setpoint reported 21 °C.

## PROVEN / locally confirmed — persistent Online/DCM runtime

EXP344 and EXP345 both demonstrate that the emulator can maintain the known stage-40 0x0F runtime for at least 15 minutes while ACKing only the explicit runtime whitelist and servicing exact 0708/count6 mailbox polls. EXP345 reached 379 runtime FC16 ACKs and 210 idle 0708 responses at the 15-minute milestone with zero unknown FC16, unknown FC03, peer FC17, peer FC16-ACK, resync and drop counters.

## PROVEN / locally confirmed — W5=0006 sufficient for persistent DCM indication in tested context

Controlled A/B: EXP344 used W0..W5 = 0000 0000 0000 0000 0000 0000 and lost the DCM icon after the soak while transport remained healthy. EXP345 used W0..W5 = 0000 0000 0000 0000 0000 0006; transport remained healthy >15 minutes, the DCM icon remained present, and no Online/Link error appeared. Only W5 changed.

Therefore W5=0006 is sufficient, in this tested local emulator/session context, to retain the controller's DCM-connected UI indication where W5=0000 did not.

## OPEN / UNKNOWN — semantic meaning of W5

Do not label W5 as a proven connected flag. Genuine older DCM/ATEC evidence motivated 0006, but the field could encode device type, version, capability, session state or another lifecycle property. EXP345 proves a behavioral requirement/sufficiency result, not the field's abstract meaning.

## STRONGLY SUPPORTED architecture after EXP343–345

The locally demonstrated pieces now fit the genuine Online/DCM cache model: controller exports pages to slave 0x0F via FC16; 0708 is an interleaved mailbox/control envelope; desired-page availability can be advertised there; controller pulls the desired page using FC03; the returned page can change controller semantics; and W5=0006 permits the tested persistent DCM-connected presentation while runtime continues.

The next integration question is whether the EXP343 guarded desired-page action can be performed safely inside the EXP345 long-lived connected baseline, followed by longer-duration and reconnect testing.

---
# 2026-09-30 — Runtime retention and 0708 bidirectional page-cache model

## PROVEN / locally confirmed — fresh XTR initial-sync chain now reaches 06F4

EXP331–333 extend the locally proven fresh-session chain from the previous 04A6 boundary through:

    04BA/22 -> 04D8/27 -> 04F6/14 -> 050A/19 -> 051E/10 -> 0532/18 -> 0546/20
    -> 055A/33 -> 057B/33 -> 059C/33 -> 05BD/33 -> 05DE/33 -> 05FF/33
    -> 0620/33 -> 0641/33 -> 0662/33 -> 0683/33 -> 06A4/33 -> 06C5/33
    -> 06EA/7 -> 06F1/3 -> 06F4/19

After 06F4 ACK, local XTR traffic enters the post-tail region containing 085F/5 and FC03 0708/count6.

## PROVEN / locally confirmed — retained runtime survives ESP OTA and remains actionable

- EXP336: retained 07D0/19 appeared after ESP OTA with zero experiment TX.
- EXP337: 07D0/19 ACK -> 07E4/17 ACK -> FC03 0708/count6.
- EXP338: after another ESP OTA, 07F8/17 appeared before any experiment TX.
- EXP339: 07F8/17 ACK -> FC03 0708/count6 about 1.57 s later.
- EXP340: after another ESP OTA, 080C/18 appeared before any experiment TX.

**PROVEN locally:** ESP reboot is not controller-session rollback. Controller-side runtime/export state can persist and advance while the ESP restarts.

**STRONGLY SUPPORTED:** 0708 is interleaved mailbox service inside runtime, not a universal mandatory immediate gate before every runtime FC16 page.

## STRONGLY SUPPORTED / genuine gateway evidence — 0708 W2:W3 is a 32-bit PUSH/refresh page bitmap

Across the available genuine Eco5 and ATEC/DCM captures, the third and fourth response words to FC03 0708/count6 select controller-originated FC16 page refreshes bit-for-bit:

| Bit | Page | Bit | Page |
|---:|---:|---:|---:|
| 0 | 03E8 | 16 | 0546 |
| 1 | 03FC | 17 | 055A |
| 2 | 0410 | 18 | 057B |
| 3 | 042E | 19 | 059C |
| 4 | 0442 | 20 | 05BD |
| 5 | 0456 | 21 | 05DE |
| 6 | 046A | 22 | 05FF |
| 7 | 047E | 23 | 0620 |
| 8 | 0492 | 24 | 0641 |
| 9 | 04A6 | 25 | 0662 |
| 10 | 04BA | 26 | 0683 |
| 11 | 04D8 | 27 | 06A4 |
| 12 | 04F6 | 28 | 06C5 |
| 13 | 050A | 29 | 06EA |
| 14 | 051E | 30 | 06F1 |
| 15 | 0532 | 31 | 06F4 |

Evidence includes sparse 4000:8000 selecting 06F1 and 0532, Eco5 FFFF:867F selecting its corresponding 26-page refresh set, and ATEC 7FFF:FFFF selecting the first 31 pages through 06F1.

This mapping is **genuine gateway/DCM capture evidence**. It is not, by itself, a locally proven XTR mailbox-response mapping.

## STRONGLY SUPPORTED / genuine gateway evidence — 0708 W1 is desired-page PULL selector

Two independent low-bit cases are directly observed:

- W1=0001 -> controller initiates FC03 read of page 03E8.
- W1=0008 -> controller initiates FC03 read of page 042E.

ATEC/DCM capture evidence includes W1=0001 with W3=0000 followed by FC03 03E8, proving that the pull function does not require the corresponding push bit to be set simultaneously.

In Eco5 captured write-roundtrips, the gateway answers the controller's page read with desired values and the controller subsequently republishes the accepted page through FC16.

### 03E8 desired-page roundtrip

A captured Eco5 pull changes only register 03F4 from 0014 to 001E relative to the immediately preceding/current page image; the subsequent controller FC16 03E8 page matches the gateway-supplied desired page. A later roundtrip restores 03F4 from 001E to 0014 and is again followed by the matching controller page.

03F4 is independently **PROVEN / locally confirmed** on this XTR M as the room-setpoint mirror. The Eco5 write event itself remains cross-model evidence.

### 042E desired-page roundtrips

Captured Eco5 W1=0008 pulls show one-field changes within 042E/count15: first 042F 0001->0000, later 042E 0001->0000, each followed by a controller FC16 publication matching the desired page. The public DCM material labels 042E as Integral A1, but individual semantics are not imported as proven XTR behavior.

## STRONGLY SUPPORTED — Online/DCM behaves as a bidirectional page cache

Best current architecture:

    controller -> gateway current state: FC16 page export
    gateway -> controller desired state: 0708 PULL bit -> controller FC03 page read
    mailbox W2:W3: current-page refresh request bitmap
    mailbox W1: desired-page pending bitmap (low 16 bits observed)

This explains genuine setting changes without requiring the DCM to act as a second Modbus master performing direct FC16 register writes into the controller.

## HYPOTHESIS — W0 is high half of PULL bitmap

W0 was zero in all 302 paired 0708 responses in the offline reduction. Symmetry makes a high-half PULL interpretation plausible, but there is currently no positive bit observation. Keep as **HYPOTHESIS**, not fact.

## OPEN / UNKNOWN — W4 and W5

Eco5 W4 values include 0100/010B/03DF/03DC/03D8/03D0/03CF/038C/0380/0300/0200. Older ATEC/DCM captures show different values including 077F/0080 and W5 values 0006/0007. These fields likely carry lifecycle/status/capability/session information, but exact semantics and cross-model portability are unknown.

## Next discriminator

A no-op local XTR desired-page PULL test is now preferred over further one-page runtime chasing. The target is 03E8/14 because the page is locally established and includes locally mapped 03F4. The controller must first provide a fresh current page; if a matching 0708 PULL request is induced, the ESP should answer a controller FC03 read only with an exact clone of that current page. Any semantic value modification is explicitly out of scope for the first test.

---
# 2026-09-30 — Fresh approval and ordered initial-sync chain re-confirmed through 04A6/13

## PROVEN / locally confirmed — fixed captured R1 can open a fresh XTR session

On a true fresh Thermia-controller reboot, with the observed fresh guard `A80E=0000 / A80F=0005`, the first exact slave-`0x0F` FC17 request:

- read start `0x0730`, count 8;
- write start `0x071C`, count 8;
- write bytecount 16;

accepted the previously captured fixed R1 response:

`0F17101691A5F3F8E8D58738924416E8E6A3D5E227`

even though the live challenge differed from the challenge associated with that historical R1. In EXP325, `03E8/count14` followed about 120 ms later.

This proves acceptance of that fixed replay in the tested XTR context. It does **not** prove that arbitrary responses work, that the mechanism is unauthenticated, or that the replay is universal/permanent.

## PROVEN / locally confirmed — ordered fresh-session FC16 initial-sync prefix

EXP326–330 locally confirm the following ordered ACK-driven progression:

`03E8/14 --ACK--> 03FC/11 --ACK--> 0410/22 --ACK--> 042E/15 --ACK--> 0442/13 --ACK--> 0456/12 --ACK--> 046A/18 --ACK--> 047E/19 --ACK--> 0492/11 --ACK--> 04A6/13`

Together with EXP325, the currently proven fresh prefix is:

`fresh boot -> 071C/0730 challenge -> fixed R1 -> 03E8/14 -> ... -> 04A6/13`

The ACKs in these tests are standard FC16 address/count acknowledgements only. They do not inject the controller-exported payload values.

## PROVEN / locally confirmed — individual new transitions

- EXP326: `03E8/14 ACK -> 03FC/11`.
- EXP327: `03FC/11 ACK -> 0410/22`.
- EXP328: `0410/22 ACK -> 042E/15`.
- EXP329: `042E/15 ACK -> 0442/13 ACK -> 0456/12 ACK -> 046A/18`.
- EXP330: `046A/18 ACK -> 047E/19 ACK -> 0492/11 ACK -> 04A6/13`.

All current-run transitions were observed with clean parser/RX integrity and fail-closed behavior.

## PROVEN / locally confirmed — ESP reboot is not controller-state rollback

EXP324 did not recreate the clean all-zero-`085F` fresh state after ESP OTA/reboot while the Thermia controller remained powered. This agrees with prior retained-session work: controller-side Online/DCM state can persist while the ESP is restarted.

## STRONGLY SUPPORTED — next fresh-sync continuation

Genuine Eco 5 capture evidence and the earlier EXP262 design support the next ordered continuation:

`04A6/13 -> 04BA/22 -> 04D8/27 -> 04F6/14 -> 050A/19 -> 051E/10 -> 0532/18 -> 0546/20 -> 055A/33`

EXP331 is prepared to test that bounded continuation in the current fresh-XTR run. Until its result is supplied, the current-run local proof boundary remains `04A6/13`.

## HYPOTHESIS — security/session semantics of 071C/0730

The fixed-R1 replay result strongly weakens a strict “unique cryptographic response required for every live challenge” interpretation for this tested acceptance path. The actual algorithm, scope, lifetime and security role remain unknown.

Do not promote any of the following to fact:
- arbitrary 16-byte responses are accepted;
- the challenge is meaningless;
- no cryptography/authentication exists;
- R1 is universally valid across units, firmware versions or indefinitely.

## OPEN / UNKNOWN — 04A6 semantics remain context-sensitive

`04A6/count13` now occurs in at least three distinct observed contexts:
- predicted initial-sync stage immediately after `0492/11`;
- sparse passive fresh-state traffic;
- recurrent runtime traffic with state-dependent payloads.

Therefore the address alone is not enough to determine semantics or ACK policy. State, payload, ordering and session context remain required.

---

# 2026-09-30 — EXP318–322 retained recovery, 04A6 context split, and clean-reboot baseline

## PROVEN / locally confirmed

- In the tested retained context, exact `085F/5` with words `0000 0000 0800 0000 0000` advances to exact all-zero `085F/5` after one qualified standard FC16 ACK.
- In EXP319, after the `085F(0800)` prerequisite was serviced, one qualified standard ACK to exact all-zero `085F/5` was followed 2.381 s later by direct `0884/60`.
- In EXP320, one qualified standard ACK to `0884/60` was followed 4.328 s later by direct `07D0/19`.
- Therefore the locally confirmed retained branch includes:
  `085F(0800) --ACK--> all-zero 085F --ACK--> 0884/60 --ACK--> 07D0/19`.
- EXP312 had independently shown `0884 ACK -> 0708 (NO_TX) -> 07D0`; EXP320 proves `0708` is not a mandatory immediate post-`0884` step in every retained context.
- EXP322 passively proved that, after a controller reboot and with emulator TX=0, this local XTR M repeatedly emits sparse `04A6/13` and exact all-zero `085F/5` with no normal runtime pages. Over 90 s: `04A6=83`, `085F-zero=42`, all tracked runtime pages=0, parser resync=0, RX drops=0.
- The sparse EXP322 `04A6` payload remained invariant:
  `0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 4020 0000 0000`.
- Repeated `04A6/13` alone is not a reliable indicator of the prior visible alarm state, because it persists after the controller reboot that cleared those errors.

## STRONGLY SUPPORTED

- **Genuine XTR/DCM capture evidence:** a real DCM ACKs at least one richer `04A6/13` configuration payload with standard FC16 ACK `0F 10 04 A6 00 0D E1 F1`.
- Genuine configuration captures place `04A6/13` inside a broader FC16 configuration/page-sync family rather than proving it is a standalone alarm frame.
- The apparent sequence `04A6 ACK -> 085F` in some captures should not be treated as a universal causal rule. All-zero `085F` can recur periodically among different configuration pages.
- The post-reboot reappearance of all-zero `085F/5` is a more useful discriminator between EXP321 and EXP322 than the mere presence of `04A6`.

## HYPOTHESIS

- In the clean post-reboot state, one conservatively qualified standard ACK to exact all-zero `085F/5` may advance the controller to `0708/6` or another known initialization/runtime state.
- The sparse `04A6` seen locally may represent a retryable initialization/configuration state, but its exact semantics remain unknown.
- The richer genuine `04A6` payload and the sparse local `04A6` payload may belong to different sub-states of the same configuration family.

## OPEN / UNKNOWN

- First non-`04A6` state after ACKing exact all-zero `085F/5` in the current clean post-reboot condition.
- Whether the sparse `04A6` payload should receive the same ACK policy as the richer genuine DCM configuration payload.
- Exact word semantics of both sparse and rich `04A6/13` payloads.
- Exact semantics of `0861=0x0800`.
- Exact `0708` mailbox/scheduler latching rules.
- Long-duration stability once the clean-start path is reconnected to the proven runtime responder.

## DISPROVEN / SUPERSEDED

- **Superseded:** treating every runtime/config `04A6/13` as globally capture-only in the protocol model. Capture-only remains the current local safety policy, but genuine XTR/DCM evidence proves that real DCM firmware does ACK at least some `04A6/13` configuration frames.
- **Superseded:** the hypothesis that repeated `04A6` by itself identifies the visible alarm/retry state. EXP322 shows repeated `04A6` after a controller reboot that cleared the visible errors.

---

# 2026-09-30 — EXP313–315 retained-runtime direct handoff and sustained steady-state findings

## PROVEN / locally confirmed

- The XTR M controller can preserve Online/DCM scheduler state across ESP restart/OTA and can be encountered already inside the normal runtime graph rather than at fresh approval or an early retained-recovery stage.
- Exact retained `07D0/19` can accept the already-proven standard ACK as a handoff attempt. EXP313 showed that the controller then produced `0708/6` before `07E4/17` in that retained context.
- Exact retained `07E4/17`, when observed repeatedly and qualified before any ESP TX, can be used as a direct runtime re-entry node with the already-proven ACK `0F 10 07 E4 00 11 40 68`.
- EXP315 proved that direct retained takeover at `07E4/17` can hand off into the existing EXP296/297 runtime responder and sustain at least **126.401 s and 6 complete returned runtime loops**.
- The successful EXP315 run ended intentionally at a returned `07D0/19` boundary left NO_TX, with `TX=84`, `events=84`, `r0708=30`, `unexpected=0`, `resync=0`, `drops=0`, `DE=LOW`.
- In that successful run no retained-recovery ACKs for `0662`, `085F(0800)`, all-zero `085F`, `0864`, `0870` or `0884` were needed before handoff. Direct known-node takeover was sufficient.
- The earlier hypothesis that retained recovery must first be forced back to a single universal anchor such as `0848` or `07D0` is superseded. The safer production model is current-state classification plus node-specific handoff where locally proven.

## STRONGLY SUPPORTED

- A production DCM emulator should have two complementary retained-session mechanisms:
  1. direct re-entry at a recognized, qualified normal-runtime node;
  2. adaptive retained recovery only when the controller is in a recovery/retry state.
- Sustained Online/DCM health is tied to continuing the scheduler rather than merely issuing an isolated recovery ACK.
- `0708` should remain modeled as an event that can appear between FC16 scheduler nodes. Its correct treatment is context-dependent; EXP313 showed it can appear immediately after a retained `07D0` handoff, while EXP315 showed normal evidence-backed runtime responses can sustain the session after direct `07E4` entry.
- Runtime takeover must preserve the allowed-next-event set for the node at which handoff occurs; a generic broad ACK policy is not justified.

## HYPOTHESIS

- Other already-proven normal runtime nodes may also be safe direct retained-entry anchors if they are conservatively qualified and joined with their existing next-event graph.
- A unified state machine combining fresh startup, controller-reboot recovery, direct retained-runtime node takeover and adaptive retained recovery should be sufficient for production use without requiring a Thermia-controller reboot after every ESP restart.
- Longer-term Online/Link alarm clearing should correlate with sustained scheduler service, but durable alarm behavior across hours and operating modes still needs dedicated observation.

## OPEN / UNKNOWN

- Which additional runtime nodes are safe direct retained-entry anchors beyond the locally proven `07E4/17` handoff and the partially validated `07D0` handoff.
- Multi-hour/overnight stability across compressor state changes, DHW cycles, defrost, SG transitions and faults.
- Exact long-term semantics and required cadence of `0708`.
- Exact session-liveness/watchdog interval.
- Exact semantics of `0861=0x0800`.
- Runtime `04A6/13` semantics and native ACK policy.
- Genuine `071C/0730` challenge-response algorithm.
- Rare scheduler branches and fault-state recovery behavior.

## DISPROVEN / SUPERSEDED

- **SUPERSEDED:** retained-session recovery must first return to one specific anchor before steady runtime can resume. EXP315 proved direct steady-runtime takeover at retained `07E4/17`.
- **SUPERSEDED:** ESP restart implies the controller will reopen fresh approval/config sync. EXP298–315 show persistent retained controller/session state across ESP restart/OTA.
- **SUPERSEDED:** a production emulator should enforce one rigid exact-next-frame chain across all reconnect conditions. Retained-state evidence requires a qualified branch-aware event graph.

## Safety interpretation

- Direct retained-node takeover does not authorize unknown nodes. Only exact, locally proven frame shapes with node-specific next-event rules may be serviced.
- Standard FC16 ACKs still acknowledge slave/function/start/count only and do not inject the controller-originated payload values.
- `0834/18` remains capture-only/unsupported.
- Runtime `04A6/13` remains capture-only until separately tested.
- Unexpected `0x0F` traffic remains capture-only/fail-closed.
- ESP reboot/OTA is not rollback.
- Manual alarm-observation buttons are not protocol evidence unless intentionally pressed while observing the actual front-panel state.

---

# 2026-09-29 — EXP298–312 retained-session recovery and branch-aware runtime findings

## PROVEN / locally confirmed

- The XTR M Online/DCM runtime is **not a rigid linear chain**. Retained-session recovery can re-enter known runtime at different branch points.
- Exact `0662/33` is an ACK-gated controller-to-DCM transfer stage on this XTR M. EXP305 re-confirmed the older EXP141 result.
- Exact `085F/5` carrying words `0000 0000 0800 0000 0000` is ACK-sensitive. One standard ACK can move the controller to the all-zero `085F/5` state.
- The third word of that frame is register `0861`, value `0x0800`. This makes `0861=0x0800` a locally confirmed session/retry-state discriminator, but **not** a decoded semantic flag.
- Exact all-zero `085F/5` is also ACK-gated in the tested retained-session path. A single standard ACK can advance the controller to known runtime traffic.
- `0864/4`, `0870/17` and `0884/60` each accept the standard FC16 address/count ACK and can advance the local controller to another known runtime stage.
- EXP307 locally proved: `all-zero 085F ACK -> 0708 -> 0864/4`.
- EXP308 locally proved: `0864/4 ACK -> 0708 -> 0870/17`.
- EXP310 locally proved: `0870/17 ACK -> 0708 -> 0884/60`.
- EXP312 locally proved: `0884/60 ACK -> 0708 -> 07D0/19`.
- In those bounded transition tests the intervening `0708` was deliberately left NO_TX, yet the next known FC16 stage still appeared. Therefore an **immediate** `0708` response is not required for these short scheduler transitions.
- EXP309 showed direct `0870/17` after the post-`085F` branch with no preceding `0864/4`.
- EXP311 and EXP312 showed direct `0884/60` after the post-`085F` branch with no preceding `0864/4` or `0870/17`.
- Controller retained state can survive ESP reboot/OTA. ESP restart does not reset the Thermia controller session state.
- `0884/60` payload data can change between repeated frames while the start/count remain fixed. Qualification must therefore use frame shape/state context rather than assuming a fixed payload.

## Current locally supported retained-session graph

The retained-session recovery evidence now supports at least:

`0662/33 --ACK--> retained scheduler`

`085F(0800) --ACK--> all-zero 085F`

`all-zero 085F --ACK--> branch-aware runtime`

From that branch, locally observed valid paths include:
- `0708 -> 0864`;
- direct `0870`;
- `0708 -> 0870`;
- direct `0884`;
- `0708 -> 0884`.

Locally tested ACK transitions then reconnect to the normal runtime loop:
- `0864 ACK -> [0708] -> 0870`;
- `0870 ACK -> [0708] -> 0884`;
- `0884 ACK -> [0708] -> 07D0`.

The brackets above mean that `0708` was observed in the tested causal sequence but its response was intentionally omitted; this notation does **not** claim that `0708` is globally optional for all Online/DCM purposes.

## STRONGLY SUPPORTED

- The controller appears to maintain a **session-liveness/watchdog** model rather than judging health from one isolated ACK. EXP299 and EXP305 produced temporary visible progress/clearing, while lack of sustained service later returned to recovery/retry behavior.
- The most useful emulator architecture is a state/event graph with a set of allowed next events, not a single exact next-register pointer.
- `0708` remains a synchronization/mailbox descriptor. Its immediate response can be unnecessary for short FC16-to-FC16 progression, but it may still matter to long-lived session health, reverse-page advertisement or other state synchronization.
- Fresh approval is not guaranteed after an ESP restart while the Thermia controller remains powered. The controller can remain in a retained runtime/recovery state instead.

## HYPOTHESIS

- A branch-aware retained-session recovery handler that reaches any known normal runtime node can likely hand off to the already proven EXP296/297 steady-state runtime responder and restore sustained Online/Link health without rebooting the Thermia controller.
- `0861=0x0800` likely marks a retry/recovery or pending-session condition, but the exact semantics are unknown.
- The exact liveness timer may be on the order of minutes, but current alarm timing is observational and context-dependent; no timer value is proven.

## OPEN / UNKNOWN

- Exact semantic meaning of `0861=0x0800`.
- Exact conditions that select direct `0864`, direct `0870`, direct `0884`, or an intervening `0708`.
- Exact long-term role of `0708` and minimum response cadence required for durable health.
- Exact session-liveness/watchdog interval.
- Whether branch-aware retained recovery can sustain multiple complete EXP296/297 runtime cycles without controller reboot.
- Semantics of runtime pages `0864`, `0870`, `0884` and the changing fields inside `0884`.
- Runtime `04A6/13` semantics and native ACK policy.
- Genuine `071C/0730` challenge-response algorithm.
- Multi-hour/overnight stability and rare/fault-state behavior.

## DISPROVEN / SUPERSEDED

- **SUPERSEDED:** `0848/23` is a universal retained-session re-entry anchor. EXP300/301 showed retained states centered on `085F(0800)` and `0708` without `0848`.
- **SUPERSEDED:** `0864/4` must precede `0870/17`. EXP309 observed direct `0870`.
- **SUPERSEDED:** `0870/17` must precede `0884/60`. EXP311/312 observed direct `0884`.
- **SUPERSEDED:** ESP reboot/OTA can be treated as protocol rollback. EXP303 showed the controller can retain the changed session state across ESP restart.

## Safety interpretation

- Standard FC16 ACKs acknowledge only slave/function/start/count; they do not inject the FC16 payload values.
- Even so, every new ACK target remains an explicit experimental action and must stay exact-shape/state gated.
- Do not broad-ACK unknown FC16 traffic.
- `0834/18` remains capture-only/unsupported locally.
- Runtime `04A6/13` remains capture-only until separately tested.
- Retained-session experiments should not include semantic setting writes.
- Unexpected `0x0F` traffic remains capture-only/fail-closed unless its branch is explicitly predeclared from local evidence.
- Do not assume ESP reboot restores controller state.

---

# 2026-09-29 — EXP291–297 runtime, state-transition and recovery findings

## PROVEN / locally confirmed
- The Online/DCM runtime is **event/state driven**, not one rigid fixed sequence.
- `0884/60 -> [optional 0708/6] -> 07D0/19` is locally confirmed.
- `07E4/17 -> [optional 0708/6] -> 07F8/17` is locally confirmed.
- `080C/18 -> [optional 0708/6] -> 0820/18` is locally confirmed.
- Conditional behavior around `0848`, `085F`, `0864` and `0870` remains locally confirmed.
- EXP293 demonstrated roughly 30 minutes of stable continuous runtime without user-visible `COMM. ERR ONLINE/LINK` in that steady-state scope.
- Extended EXP296 evidence demonstrated >32 minutes of runtime while surviving SG changes, a near-complete DHW/compressor cycle and a later **Blocked (1-0)** transition.
- Runtime `04A6/13` can remain unacknowledged for at least the observed ~32-minute EXP296 window while the main Online/DCM runtime continues. The later capture reached at least **1696** `04A6` frames with **3** payload changes.
- **EXP297 proves controller-reboot recovery locally:** from active runtime, the emulator detected a controller bus gap, accepted a fresh `071C/0730` challenge, replayed the existing R1, completed the full 32-page startup sync, serviced startup `085F`/ `0708`, and resumed runtime without ESP reboot or manual re-arm.
- The same fixed historical R1 replay remained accepted for a fresh challenge after a later controller reboot in the same ESP uptime.

## STRONGLY SUPPORTED
- `0708` acts as a synchronization/mailbox descriptor whose presence at several runtime positions depends on controller/session state.
- Runtime `04A6/13` is parallel/retry traffic rather than an immediate blocking gate in the tested local window.
- `04A6` payload changes correlate strongly with operational context:
  - an earlier form changed around DHW/high-temperature entry;
  - it later returned;
  - after a subsequent SG Blocked transition, a new form beginning `0042 0001 ...` appeared.
  This does **not** yet prove field semantics or that `0042` uniquely encodes Blocked.
- Loss of required responder continuity explains the observed Online/Link alarm behavior better than the mere presence of unacknowledged `04A6` traffic.
- Session startup is repeatable after controller reboot; approval/config/runtime state is therefore reconstructible rather than tied to one ESP boot.

## HYPOTHESIS
- Runtime `04A6/13` is a controller-to-DCM state/configuration export whose first words encode an operating/context state.
- A native DCM may ACK runtime `04A6` selectively to stop/reconcile retries, even though local short/medium-term runtime can proceed without such ACK.
- After an ESP-side restart with the Thermia controller left powered, the controller may eventually re-open the approval path and issue a fresh `071C/0730` challenge without requiring its own reboot. EXP298 is prepared to test this directly.

## OPEN / UNKNOWN
- ESP-restart recovery while the controller remains powered.
- Exact semantics and ACK policy for runtime `04A6/13`.
- Whether `0041`, `0042` or their neighboring words map uniquely to specific operating/SG contexts.
- Exact scheduling rules for optional `0708` polls.
- Exact meaning of `0708` words 0, 4 and 5.
- Multi-hour/overnight stability, rare states and fault recovery.
- Genuine `071C/0730` challenge-response algorithm.
- Authoritative controller FC16 echo timing/conditions after reverse-page semantic writes.

## Current locally supported runtime graph
`07D0 -> 07E4 -> [optional 0708] -> 07F8 -> 080C -> [optional 0708] -> 0820 -> 0848 -> [conditional 0708 / conditional 085F] -> 0864 -> [optional 0708] -> 0870 -> [optional 0708] -> 0884 -> [optional 0708] -> 07D0 -> ...`

Runtime `04A6/13` may interleave with this path and remains capture-only in the current emulator experiments.

## DISPROVEN / SUPERSEDED
- **SUPERSEDED:** `0708` is mandatory at every previously observed runtime position.
- **SUPERSEDED:** a particular SG state itself breaks Online/DCM emulation; later tests show the earlier failures were missing protocol branches.
- **SUPERSEDED:** controller reboot necessarily requires ESP reboot/re-arm. EXP297 locally proves automatic controller-side session recovery.

## Safety interpretation
- No broad address-based ACKing.
- Runtime `04A6/13` remains capture-only until a dedicated experiment explicitly changes it.
- Keep semantic reverse-page writes separate from continuity/recovery experiments.
- Continue strict CRC/slave/function/address/count/bytecount validation and fail closed on new branch shapes.

---

# 2026-09-29 — reverse Online/DCM write path locally demonstrated through semantic application

## PROVEN / locally confirmed
- `0708 w1 bit0 = 1` can cause the XTR M controller to issue `FC03 03E8/count14`.
- The XTR accepts a reverse `03E8/14` page response built from the exact current-session controller export.
- An unchanged reverse page is accepted and normal runtime traffic continues.
- In EXP290, changing **only** `03F4` in the same-session reverse page from raw `22` to `23` caused the controller-visible `Room Setpoint` to report `23 °C` shortly afterwards.
- Therefore the native reverse-page path is not only transport-capable; it can semantically apply at least this one locally mapped setting.

## STRONGLY SUPPORTED
- Slave `0x0F` is a bidirectional Online/DCM page interface:
  - controller -> gateway/cache via FC16 exports;
  - gateway desired/config -> controller via 0708 advertisement followed by controller FC03 pull.
- `0708 w2/w3` form a configuration-page selection/request bitmap.
- `0708 w4` behaves as a runtime-page scheduler/selection bitmap, though exact timing/latching semantics remain open.
- Runtime `085F` and the placement of `0708` around `0864` are state-dependent rather than fixed.

## OPEN / UNKNOWN
- Authoritative FC16 `03E8/14` echo of the changed `03F4` target after semantic application.
- Independent room-sensor-side confirmation through slave `0x0A` / `B3C5` after the reverse-page write.
- Exact meaning of 0708 `w0`, `w4`, `w5`.
- Exact queue/latch rules that govern conditional `085F` and position of `0708`.
- Genuine `071C/0730` challenge-response algorithm.

## Runtime branch refinement from genuine XTR captures + EXP287
Evidence-backed variants include:
- `0848 -> 0864 -> 0708 -> 0870`
- `0848 -> 085F -> 0708 -> 0864 -> 0870`
- local EXP287 additionally observed `0864 -> 0870` directly.

Do not model 0708 as a universally mandatory separator after 0864.

## Safety interpretation
EXP290 is the first local semantic setting change through the native reverse-page path. This does **not** authorize arbitrary page/register modification. Continue one mapped word at a time, from a same-session page cache, with bounded guards and RX-only observation after the semantic response.

---

# 2026-09-29 — Runtime loop locally closed; 085F is conditional/state-dependent

## PROVEN / locally confirmed — complete XTR M runtime loop
EXP273–285 extend the locally proven Online/DCM-style runtime path into a closed, repeatable loop:

`07D0 -> 07E4 -> 0708 -> 07F8 -> 080C -> 0708 -> 0820 -> 0848 -> 0708 -> [085F when present] -> 0864 -> 0708 -> 0870 -> 0884 -> 0708 -> 07D0`.

Locally confirmed causal stages include:
- post-`07E4` 0708 response `0F030C0000000000000000000000069D76` -> `07F8/17` (EXP273);
- `07F8 ACK -> 080C/18` (EXP274);
- `080C ACK -> 0708/6` (EXP275);
- `0708 response -> 0820/18`, then `0820 ACK -> 0848/23` after the EXP276 software issue was fixed (EXP277);
- `0848 ACK -> 0708/6` (EXP278);
- post-`0848` 0708 response can lead to `085F/5` (EXP279);
- `085F ACK -> 0864/4` in that observed branch (EXP280);
- `0864 ACK -> 0708/6` (EXP281, later recognized as native ordering);
- post-`0864` 0708 response -> `0870/17`, and `0870 ACK -> 0884/60` (EXP282/283 path);
- `0884 ACK -> 0708/6` (EXP283);
- post-`0884` 0708 response -> returned `07D0/19` (EXP284);
- returned `07D0 ACK -> 07E4 ACK -> 0708 response -> 07F8` without a new approval/R1 exchange (EXP285).

## PROVEN / locally confirmed — steady-state continuation without new approval
EXP285 shows that after one complete runtime loop closes at `07D0`, the controller can immediately begin the next runtime cycle. No new `071C/0730` approval exchange occurred between loop closure and the second-cycle `07D0 -> 07E4 -> 0708 -> 07F8` progression.

This is the strongest local evidence so far that the observed page family is a real steady-state runtime loop rather than a one-shot initialization tail.

## PROVEN / locally confirmed — 085F is not mandatory in every runtime cycle
EXP286 materially corrects the earlier interpretation that `085F/count5` is an invariant runtime gate.

In the first observed branch, post-`0848` `0708` was followed by `085F/5`, whose ACK led to `0864/4`.

In the second cycle of EXP286, the controller instead produced:
`0848 ACK -> 0708 response -> 0864/4`
with no intervening 085F.

Current status:
- **PROVEN:** 085F can be an ordered gate when present.
- **PROVEN:** 085F is not present in every observed cycle.
- **STRONGLY SUPPORTED:** 085F is conditional/state-dependent queue/runtime traffic.
- **OPEN:** exact condition and semantics.

This replaces the older blanket wording that 085F is always required before 0864/runtime continuation.

## PROVEN / locally confirmed — 0884 shape and ACK
Local `0884` frames have:
- start `0x0884`;
- count 60;
- bytecount 120;
- total Modbus frame length 129.

The standard ACK `0F100884003C837F` was accepted locally and advanced to the next `0708/6`.

The controller-originated 0884 payload itself varies with runtime state; the ACK confirms only address/count and does not inject those values.

## DISPROVEN / SUPERSEDED — direct 0864 -> 0870 requirement
EXP281 originally treated the post-`0864` `0708/6` as unexpected because the experiment expected direct `0870`.

Later genuine-capture reanalysis showed native ordering can be:
`0864 ACK -> 0708 request/response -> 0870`.

Therefore:
- preserve EXP281's historical COMPLETE / INCONCLUSIVE status;
- the interpretation that post-0864 0708 is a divergence is **SUPERSEDED**.

## STRONGLY SUPPORTED — runtime sequence has genuine-capture variability
Different genuine Online/Eco5 captures and local cycles do not always place `085F` identically, and post-`0864` ordering can include an intervening `0708`.

Do not encode a single rigid universal runtime sequence across all Thermia/Danfoss models or all controller states. Exact XTR handlers should allow only branches that have been explicitly predeclared from local or genuine evidence.

## STRONGLY SUPPORTED — 0708 remains a synchronization descriptor, not a simple idle poll
Current evidence supports multiple roles:
- words 2/3: FC16 page-request/selection bitmap;
- word1: strong candidate for reverse settings-page availability, based on genuine `0708 -> FC03 03E8` pulls;
- word4: candidate runtime-page bitmap;
- phase-dependent response values coordinate runtime page progression.

The locally repeated response `0000 0000 0000 0000 0000 0006` is proven operationally in several runtime phases, but its exact semantic meaning remains unknown.

## HYPOTHESIS — 0708 word4 runtime bitmap, refined by conditional 085F
Candidate mapping remains:
`bit0=07D0, bit1=07E4, bit2=07F8, bit3=080C, bit4=0820, bit5=0834, bit6=0848, bit7=085F, bit8=0864, bit9=0870, bit10=0884`.

EXP286's direct `0848 -> 0708 -> 0864` branch is compatible with a state-dependent bit7/085F selection model, but does not prove exact bit semantics. Keep this as **HYPOTHESIS**.

## OPEN / UNKNOWN
- semantic meaning and condition for 085F;
- semantics of runtime pages 07D0, 07E4, 07F8, 080C, 0820, 0848, 0864, 0870, 0884;
- why local steady-state `0834` is absent in the observed branch although it appears in some genuine traces;
- exact 0708 words 0, 4 and 5 semantics;
- genuine `071C/0730` challenge-response algorithm;
- whether fixed replay remains sufficient indefinitely across re-authentication/re-sync events;
- reverse desired-state page application and authoritative echo on the XTR M;
- long-term continuous emulation stability.

## Current next step
No new experiment is prepared. When testing resumes, the smallest useful continuation is a bounded steady-state handler that explicitly permits the two evidence-backed post-`0848 -> 0708` branches:
1. `085F/5 -> ACK -> 0864/4`;
2. direct `0864/4`.

No semantic write should be mixed into that continuity experiment.

---

# 2026-09-29 — XTR runtime gates locally proven through post-07E4 mailbox poll

## PROVEN / locally confirmed — ordered runtime progression
EXP270–272 now locally establish the following XTR M session/runtime path:

`... -> 06F4/19 ACK -> 085F/5 all-zero ACK -> early 0708/6 service -> 07D0/19 ACK -> 07E4/17 ACK -> post-07E4 FC03 0708/6`.

Specific causal results:
- **EXP270:** adding one exact ACK of all-zero `085F/count5` while keeping the same early `0080/0006` mailbox response caused first `07D0/count19` to appear.
- **EXP271:** adding one exact `07D0/count19` ACK caused `07E4/count17` 2159 ms later.
- **EXP272:** adding one exact `07E4/count17` ACK caused the next `FC03 0708/count6` 1457 ms later.

These are ordered-stage findings. They do not authorize address-only or broad runtime ACKing outside the proven phase.

## STRONGLY SUPPORTED — 0708 word2/word3 form a 32-bit FC16 page-request bitmap
Cross-capture analysis of genuine gateway traffic shows that `0708/count6` words 2 and 3 predict which controller->gateway FC16 pages are emitted next.

The mapping supported by sparse and dense bitmap examples is:

- `word3` bit0..bit15:
  `03E8, 03FC, 0410, 042E, 0442, 0456, 046A, 047E, 0492, 04A6, 04BA, 04D8, 04F6, 050A, 051E, 0532`.
- `word2` bit0..bit15:
  `0546, 055A, 057B, 059C, 05BD, 05DE, 05FF, 0620, 0641, 0662, 0683, 06A4, 06C5, 06EA, 06F1, 06F4`.

Examples:
- `word2=4000, word3=8000` is followed by `06F1` and `0532` (plus separate runtime traffic).
- `word2=FF80` selects the contiguous tail `0620 .. 06F4`.
- `word2=E000` selects exactly `06EA, 06F1, 06F4`.
- `word2=8000` selects `06F4`.
- `word2=7FFF, word3=FFFF` selects all early pages plus the tail through `06F1`, excluding `06F4`.

Interpretation: 0708 is a synchronization descriptor/mailbox, not merely an idle status frame. The exact vendor naming of the bitmap (dirty/requested/stale/subscription/etc.) remains unknown.

## STRONGLY SUPPORTED — reverse-direction page pull
In genuine DCM capture data, `0708 word1=0001` is followed ~39–41 ms later by controller `FC03 03E8/count13`, after which the gateway returns the full heating/settings image. Other nearby 0708 responses with word1=0 do not trigger that read.

This supports a bidirectional page-cache model:
- controller -> gateway current/authoritative pages: FC16 push;
- gateway -> controller desired/config pages: gateway advertises pending state through 0708, controller pulls the page with FC03.

Exact semantic application and authoritative echo are not yet locally proven.

## HYPOTHESIS — 0708 word4 is a runtime-page bitmap
A candidate bit mapping fits the observed runtime family:

`bit0=07D0, bit1=07E4, bit2=07F8, bit3=080C, bit4=0820, bit5=0834, bit6=0848, bit7=085F, bit8=0864, bit9=0870, bit10=0884`.

Supporting examples include `word4=077F` accompanying the full steady runtime cycle except 085F, `word4=0080` aligning with 085F, and `word4=010B` including bit8 with 0864 appearing. This remains **HYPOTHESIS**, because local one-bit causal tests have not been performed and scheduler interleaving can obscure direct ordering.

## OPEN / UNKNOWN
- exact semantics of 0708 word0, word4 and word5;
- exact vendor meaning of the word2/word3 bitmap;
- correct local response payload for the proven post-07E4 0708 request;
- whether one phase-matched post-07E4 response `0000 0000 0000 0000 0000 0006` advances the XTR to `07F8/count17`;
- genuine 071C/0730 challenge-response algorithm.

## Next bounded protocol test
EXP273 should preserve the entire EXP272 path and change only the post-07E4 mailbox response: answer that exact `FC03 0708/count6` once with raw `0F030C0000000000000000000000069D76` (words `0000 0000 0000 0000 0000 0006`), then capture exact `07F8/count17` without ACK. No broad runtime servicing and no semantic settings write.

---

# 2026-09-29 — XTR locally proves 085F as ordered gate to runtime

EXP270 provides the first active XTR proof of the transition from the initial 0x0F configuration synchronization into the runtime-page family.

Observed local sequence:

`... -> 06EA/7 -> ACK -> 06F1/3 -> ACK -> 06F4/19 -> ACK -> 085F/5 all-zero -> ACK -> 0708/6 -> one 0080/0006 response -> 07D0/19`.

The first `07D0/19` was deliberately not ACKed.

## Strong protocol conclusion
The exact all-zero `085F/count5` is **not** ignorable background in this phase. It is an ordered queue/session item whose ACK is required before the local XTR M progresses to the first `07D0` runtime page.

This conclusion is strengthened by the EXP269/EXP270 A/B comparison:
- EXP269 used the same one-shot `0708` response `0000 0000 0000 0000 0080 0006` but did not ACK 085F -> no 07D0.
- EXP270 added one exact 085F ACK while preserving that mailbox response -> 07D0 appeared.

Therefore the 085F ACK, rather than a new mailbox payload, is the demonstrated causal discriminator.

## Challenge replay boundary
EXP270 received a new 16-byte 071C challenge but still transmitted the same historical fixed 0730/R1 response. Despite this mismatch, the XTR completed the entire initial config-page export through 06F4, accepted the 085F gate, and emitted 07D0.

Protocol implication: fixed replay is sufficient to reach at least the first runtime page on this XTR. This does not establish that the genuine challenge-response algorithm is irrelevant, nor that later steady-state/write operations will accept the same partial approval state.

## Mailbox nuance
Genuine Eco5 cold-start sessions can use raw word5/state `0100` before first runtime progression, while EXP270 reached 07D0 after the retained EXP269 response with `0080/0006`. Therefore:
- 085F ordering is now locally proven;
- exact mailbox-state equivalence is **not** proven;
- do not collapse `0100/0000` and `0080/0006` into one semantic state.

## Next bounded protocol test
EXP271 target:
`07D0/19 -> one exact standard FC16 ACK -> capture 07E4/17`.

No ACK of 07E4 in EXP271. No broad runtime servicing and no semantic settings write.

---

## 0x0F bidirectional page-cache finding — 0708 word1 likely advertises reverse settings data

A genuine DCM capture provides a strong causal pattern:
- normal controller poll: `FC03 0708/count6`;
- DCM response with word1=`0001`;
- ~39–41 ms later controller issues `FC03 03E8/count13` to slave 0x0F;
- DCM serves the complete 03E8 settings page.

This occurs twice in the capture. The returned pages differ only at `03E8` (`0017 -> 0016`). The 03E8 family is already mapped as the heating-settings block on the XTR platform.

A separate genuine DCM capture contains the same 13-word page image in the opposite direction as controller-originated `FC16 03E8/count13`.

**Strong conclusion:** 0x0F supports bidirectional page synchronization: controller -> gateway by FC16, and gateway -> controller by controller-initiated FC03. This explains why direct second-master FC16 writes were a poor model for Online control.

**Strong hypothesis:** 0708 word1 is a pending/desired-data signal that prompts the controller to fetch the 03E8 page. It is not yet proven whether word1 is exclusively a boolean 03E8 flag, an index/state counter, or part of a wider pending-page descriptor.

**Write-access implication:** the likely native control path is to maintain a gateway-side cached settings page, alter only a known desired field, advertise pending data via the appropriate 0708 status, allow the Thermia controller to read the page, and then verify an authoritative controller-side echo. Do not implement this semantic write until local session completion and a bounded page-read test prove the behavior on the XTR M.

## EXP270 protocol target — exact 085F prerequisite

EXP268/269 both ignored the exact all-zero `FC16 085F/count5` appearing after `06F4`. Successful Eco5 sessions ACK this transaction before first `07D0` whenever it is pending. EXP270 therefore changes only that gate: one exact standard ACK `0F10085F00053356`, then observe. If 0708 intervenes, preserve the same single EXP269 `0080/0006` reply so the new discriminator remains the 085F ACK rather than a mailbox payload change.

## 071C/0730 candidate algorithm — HMAC-SHA256 hypothesis is unverified

Community-proposed formula: first 16 bytes of HMAC-SHA256 with serial number as key and 16-byte challenge as message. The literal example does not reproduce the claimed response, so no protocol conclusion can be drawn yet. Preserve as a candidate only.

## Deep Eco5 capture findings: service readiness, 085F gate, mailbox byte order

1. **Challenge service and FC16 service are distinct phases.** Successful 071C/0730 replies can occur at ~10 s or ~120 s after bus return, while first 03E8 ACK clusters tightly near 118.5–120.3 s. Fast sessions tolerate 102 repeated unacked 03E8 requests.

2. **085F/5 is a likely ordered gate.** In delayed cases:
   `06F4 ACK -> 085F/5 ACK -> 0708 idle -> 07D0`.
   When 085F was already ACKed, `06F4 ACK -> 07D0` can occur in ~78 ms.

3. **Normal idle mailbox frame, raw Modbus words:** `0000 0000 0000 0000 0100 0000`. Earlier notes calling the fifth raw word `0001` were a byte-order interpretation error. The exact raw frame remains `0F030C0000000000000000010000001C88`.

4. **Deterministic post-sync mailbox script:** idle `...0100 0000` -> `0000 0000 4000 8000 010B 0000` -> `0000 0000 FFFF 867F 03DF 0000`. The 03DF trigger is followed by a fresh 03E8 in 62–94 ms in all four new sessions.

This materially raises confidence that local failure after 06F4 is caused by ignoring 085F rather than by choosing the wrong first mailbox payload.

## Protocol finding — 085F/5 is likely queue-ordered session traffic

Based on the new Eco5 capture interpretation, `0F FC16 085F/count5` all-zero traffic should no longer be categorized as ignorable background during Online session establishment.

Observed pattern from successful sessions:
- if `085F` has already been ACKed, `07D0` may follow `06F4` within ~0.1 s;
- if not, `085F` appears immediately after `06F4`, the controller waits for its ACK, and only then proceeds to `07D0`.

This provides a strong candidate explanation for our local stall after `06F4`: prior experiments deliberately ignored `085F`.

Separately, the repeatable Eco5 mailbox sequence after first sync is:
`0100/0000 idle` -> `4000 8000 010B 0000` -> `FFFF 867F 03DF 0000` -> second full synchronization.

Challenge/response remains unresolved; six unique pairs are now available, with ~30–60 ms reply latency and no simple bytewise relation observed.

## New Eco5 evidence — 07D0 is not mailbox-unlocked in the successful session

A new genuine Eco5 capture shows the successful ordered sequence:
`071C/0730 challenge -> 16-byte response -> 03E8 -> ... -> 06F4 -> 07D0 -> 07E4 -> 0708/6 idle response -> 07F8 -> ...`.

At the first clean successful session in this capture:
- `06F4` ACK at 348.304 s;
- `07D0/19` begins at 348.382 s;
- first subsequent `0708/6` is not until 351.914 s.

Therefore the first `07D0` is not caused by a post-`06F4` mailbox response in this session.

The same capture contains four different successful `071C` challenges and four different 16-byte responses:
- challenge `f721...1000` -> response `792f...4004`;
- challenge `01bd...d1c2` -> response `826e...646f`;
- challenge `1346...4ce7` -> response `623c...b049`;
- challenge `755d...9333` -> response `9a7e...3fb9`.

**Protocol implication:** `0730` approval is very likely a true challenge-response mechanism or otherwise challenge-bound. A fixed replay can trigger initial FC16 sync locally but cannot yet be assumed to create the same authenticated/session state as a genuine response.

### UI side effect after EXP269
A visible lower-right display/status glyph changed after the single `0080/0006` response, while an alarm remained active. This supports the possibility that the mailbox response affected controller/UI state even though `07D0/19` did not follow. Do not map the glyph to a protocol bit yet.

## EXP269 finding — Eco5 0080/0006 alone does not unlock 07D0 on XTR

Local XTR sequence:
`... -> 06F4/19 ACK -> 0708/6 -> response 0000 0000 0000 0000 0080 0006 -> repeated 0708/6`.

The exact response was sent once and the ESP then remained RX-only for 30 s. No `07D0/19` appeared; `0708/6` repeated on the normal ~4.2–4.4 s cadence. Final integrity deltas were clean: `resync_postreturn=0`, `drop_postreturn=0`, DE LOW.

**Protocol implication:** matching the Eco5 first mailbox payload is not sufficient by itself. The Eco5 transition to `07D0` depends on additional state/context not yet reproduced locally.

A visible user-interface change was reported immediately after this experiment (“middle of the 0 is now filled”). Treat this only as a potentially relevant state indicator until the exact screen/icon is identified.

---
## EXP269 target — exact Eco5 phase-matched first mailbox response

The next local protocol test is now fixed to the matching Eco5 post-`06F4` transition:

`06F4/19 ACK -> FC03 0708/6 -> response 0000 0000 0000 0000 0080 0006 -> expect FC16 07D0/19`.

The exact response frame is `0F030C0000000000000000008000069C9E`. It is sent once only. `07D0/19` is capture-only; no ACK. A repeated `0708/6` is not answered.

This experiment tests phase-specific mailbox semantics, not persistence/retry count. The earlier 10x `0001/0000` EXP269 plan is superseded.

---
## EXP268 finding — persistent mailbox confirmed; no 30 s RX-only runtime progression

## Eco5 raw-log correction — mailbox payload is phase-specific

Raw Eco5 capture evidence now directly shows:
- post-`06F4/19` first `0708/6` response can be `0000 0000 0000 0000 0080 0006`;
- `07D0/19` follows about 0.7 s later;
- later `0708/6` replies with `... 0000 0006` coexist with continued FC16 pages;
- later pages include `07E4/17, 07F8/17, 080C/18, 0820/18, 0834/18, 0848/23, 0864/4, 0870/17, 0884/60`.

A separate Eco5 capture shows a response `0000 0000 7FFF FFFF 0080 0007` followed almost immediately by a new FC16 synchronization beginning at `03E8/13`. This proves mailbox response words are semantically active and context-dependent.

**Do not treat `0001 0000` as a universal idle response.** Its previous occurrence is valid evidence only for the context in which it was captured. Post-`06F4` local progression should now be tested against the exact phase-matched Eco5 payload instead of increasing repetition count.


Local XTR now confirms that `FC03 0708/count6` persists for at least 30 s after three valid idle mailbox responses are followed by silence. EXP268 observed 10 total mailbox polls: the first three were answered with `0F030C0000000000000000010000001C88`, while seven later polls were left unanswered. The cadence remained approximately ~4.2 s. During the same post-third-response observation, recurrent `085F/5` continued (21 post-`06F4` background frames), but no different non-background FC16/FC03 and no `07D0..0864` family appeared.

Integrity caveat: one parser resync occurred exactly at controller BUS_RETURN before the experimental post-return baseline. Final experimental deltas were `resync_postreturn=0`, `drop_postreturn=0`; therefore the negative result is not explained by a later parser/RX integrity failure.

**Protocol implication:** persistent `0708/6` is strongly supported as normal mailbox polling. However, EXP268 does not test faithful continuous idle servicing, because replies stopped after #3. Therefore absence of later FC16 traffic cannot yet distinguish “longer timing dependency” from “continued mailbox service required/permitted in parallel”.

## EXP269 target — extend only the known-good idle service count

Increase only the maximum exact `0708/6` idle responses from 3 to 10, using the same genuine Eco5 payload and all existing timing/integrity gates. After response #10, observe RX-only for 30 s. Capture but do not ACK any first different non-background FC16/FC03. No new mailbox values and no new register-write targets are introduced.

---

## EXP267 finding## EXP267 finding## EXP267 finding — repeated 0708 idle service persists after three responses

Local XTR now confirms the sequence:

`... -> 06F4/19 ACK -> 0708/6 -> idle response -> 0708/6 -> idle response -> 0708/6 -> idle response -> 0708/6`

The idle response in all three serviced polls was the genuine Eco5 frame `0F030C0000000000000000010000001C88` (words `0000 0000 0000 0000 0001 0000`). A fourth exact `0708/6` appeared ~4.18 s after the third response and was not answered. No different meaningful FC03/FC16 appeared before that fourth request; recurrent `085F/5` remained background. Parser/RX integrity stayed clean.

**Protocol implication:** three repeated `0001` idle responses are not a mailbox-completion sequence. The stable ~4.2 s repetition is increasingly consistent with a persistent idle mailbox poll. Do not escalate by inventing later fifth-word values from the genuine capture; those values may encode runtime state/content rather than a countdown.

## EXP268 target — passive observation after bounded mailbox service

Preserve all proven active traffic through exactly three idle mailbox responses, then stop TX and continue RX-only for 30 s. Repeated `0708/6` is logged but not answered. Discovery focuses on any new non-background FC16/FC03, especially genuine Eco5 later families `07D0/19, 07E4/17, 07F8/17, 080C/18, 0820/18, 0834/18, 0848/23, 0864/4`. This is an observation-window experiment, not authorization to ACK those families.

---

## EXP267 target — bounded repeated mailbox service

EXP266 locally proved that one idle response to `0708/6` does not complete the mailbox phase: exact `0708/6` repeated ~4.18 s later while parser resync and RX drops remained zero. EXP267 therefore tests repeated servicing with the same genuine Eco5 idle frame, bounded to three responses. This does **not** establish that `0001` is a completion token or that indefinite polling should be answered; progression remains unknown until observed locally.

## EXP266 protocol finding — local 0708 repeat after one idle response

Locally confirmed sequence:
`... -> 06EA/7 -> 06F1/3 -> 06F4/19 -> 085F/5 background -> FC03 0708/6 -> response 0F030C0000000000000000010000001C88 -> FC03 0708/6 repeat after ~4.18 s`

This proves:
- local XTR accepts the mailbox response electrically/protocol-wise far enough to keep the bus/session alive;
- one response does not terminate the mailbox polling phase;
- repeated `0708/6` polling is now locally observed after the first response, matching the repeated mailbox behavior in the genuine Eco5 capture qualitatively.

Do not infer yet that repeated identical responses are sufficient; that remains the next hypothesis to test.

---

## EXP266 target — locally confirmed 0708 mailbox, genuine Eco5 idle response

- EXP265 locally confirmed `FC03 0708/count6` as the first meaningful post-sync mailbox request after `06F4/19`, with `085F/5` appearing first as recurrent background traffic.
- Genuine Eco5 capture contains the exact idle response `0F030C0000000000000000010000001C88`, i.e. six words `0000 0000 0000 0000 0001 0000`.
- EXP266 will test that response exactly once against the local XTR M. This remains a hypothesis until run.
- No inference is made that `0001` is a generic ready flag; its semantics remain unknown.

## EXP264 — proven sync tail and background-overlay caveat

Local XTR now proves the ordered Online/Link tail:
`06EA/7 -> ACK -> 06F1/3 -> ACK -> 06F4/19 -> ACK`.

Immediately after the `06F4` ACK, the first observed FC16 was `085F/5` (+107 ms). Because `085F/5` was already established from passive captures as recurrent background traffic, it must not be promoted to an ordered synchronization stage merely because it is first after an ACK.

Protocol implication: future post-sync discovery must distinguish ordered session traffic from recurrent background families. Known recurrent `085F/5` should be logged but ignored as a discovery terminator after `06F4`; `04A6/13` remains context-sensitive because it can be both recurrent and ordered depending on phase.

The next meaningful stage after `06F4` remains unknown locally. `0708/count6` mailbox timing is still unresolved and no local mailbox response has been sent.

## EXP263 finding — 055A..06C5 33-word sync run locally confirmed

## EXP264 target — final small FC16 tail before mailbox/runtime observation

EXP263 locally proved the ordered 12-block 33-word run `055A..06C5` and captured `06EA/count7` next. EXP264 therefore tests only the next genuine Eco 5 tail: `06EA/7 -> 06F1/3 -> 06F4/19`, using standard one-shot FC16 ACKs. After `06F4` it is capture-only; FC03, including `0708/count6`, is evidence only and receives no response.

EXP263 locally confirmed the genuine Eco 5 FC16 sequence:
055A/33 -> 057B/33 -> 059C/33 -> 05BD/33 -> 05DE/33 -> 05FF/33 ->
0620/33 -> 0641/33 -> 0662/33 -> 0683/33 -> 06A4/33 -> 06C5/33 -> 06EA/7.

All twelve 33-word blocks were ACKed exactly once and in order. 06EA/count7 arrived +475 ms after the 06C5 ACK and was not ACKed. The run remained parser/RX clean. This is strong evidence that the XTR and genuine Eco 5 share this synchronization segment.

Do not generalize this into broad FC16 ACKing: only the exact known ordered stages are proven. Full Online/Link establishment, the later 06F1/06F4 stages, and local 0708 mailbox timing remain open.

## EXP262 — accelerated chain proof through 055A/count33

EXP262 establishes the following local ordered Online/Link path after the already-proven prefix: `04A6/13 -> 04BA/22 -> 04D8/27 -> 04F6/14 -> 050A/19 -> 051E/10 -> 0532/18 -> 0546/20 -> 055A/33`. The first eight pages were ACKed exactly once; `055A/33` was captured only. This matches the genuine Eco 5 ordering and validates larger bounded ACK batches.

Important refinement: `04A6/13` is recurrent elsewhere on the bus, but in EXP262 it was ACKed only in the exact post-`0492` sync phase, after which the expected ordered chain continued. Context therefore remains essential; address alone does not identify a sync-stage occurrence.

The known incomplete-session failure (`DHW-side 0` / `COMM. ERR ONLINE/LINK`) remains a session-completion hypothesis, not a proven causal mechanism. `0708/count6` has not yet been serviced locally.

# THERMIA PROTOCOL FINDINGS

## EXP262 accelerated-batch target

EXP261 locally confirmed the ordered chain through `0492/count11`, with `04A6/count13` immediately next. EXP262 deliberately increases batch size while retaining exact sequencing and fail-closed checks. Target progression:
`04A6/13 -> 04BA/22 -> 04D8/27 -> 04F6/14 -> 050A/19 -> 051E/10 -> 0532/18 -> 0546/20`, then capture-only. Genuine Eco 5 predicts `055A/count33` after this block.

`04A6/13` remains context-sensitive because it is also recurrent passive traffic; EXP262 only ACKs it in phase 12 immediately after a successful `0492/count11` ACK. This does not establish every `04A6` occurrence as a synchronization page.


## EXP261 result — ordered sync now proven through 0492

EXP261 extended the local XTR Online/Link synchronization prefix using a bounded batch of exact standard FC16 ACKs:

`046A/18 -> ACK -> 047E/19 -> ACK -> 0492/11 -> ACK -> 04A6/13`

The post-0492 `04A6/count13` request arrived +576 ms after the 0492 ACK and was not acknowledged.

This is important because `04A6/13` is also a recurrent passive family. EXP261 shows that, in the approved synchronization state, it can also occupy the expected ordered next position after `0492/11`. The observation does not make every passive `04A6` instance part of the sync chain; context remains necessary.

The local chain is now directly demonstrated through:
`03E8/14 -> 03FC/11 -> 0410/22 -> 042E/15 -> 0442/13 -> 0456/12 -> 046A/18 -> 047E/19 -> 0492/11 -> 04A6/13`.

Full Online/Link establishment is still not proven because downstream pages and FC03/mailbox service remain unanswered.


## EXP261 target — bounded continuation after EXP260

EXP260 validates batching already-proven genuine Eco 5 FC16 synchronization pages. The next bounded continuation is `046A/18 -> 047E/19 -> 0492/11`, each with a standard one-shot FC16 ACK. The first different post-0492 frame is capture-only.

Genuine Eco 5 reference order places `04A6/count13` next, but prior capture analysis also classifies `04A6/13` as a recurrent passive family overlaid on synchronization. Therefore EXP261 does not use the presence or absence of `04A6` alone as a hard protocol success/failure criterion. No broad ACKing and no `0708` response are authorized by this experiment.


## EXP260 finding — bounded batch reproduces the next three genuine sync transitions

Local XTR evidence now proves the ordered post-approval prefix through `046A/count18`:

`03E8/14 -> ACK -> 03FC/11 -> ACK -> 0410/22 -> ACK -> 042E/15 -> ACK -> 0442/13 -> ACK -> 0456/12 -> ACK -> 046A/18`

The first three stages were proven incrementally in EXP257-259; EXP260 then safely batched the next three exact Eco 5 pages. There were no same-stage retries, unexpected peer responses, or post-return parser/drop errors. `046A/count18` was deliberately left unanswered.

The recurring DHW-side literal `0` appeared again during/after this deliberately incomplete session. This supports the incomplete-session side-effect model, but the exact semantics of the UI `0` remain unknown.

Protocol implication: small, pre-verified page batches are now evidence-backed as a practical way to progress the remaining genuine sync chain without one controller reboot per FC16 page. This does **not** authorize broad blind ACKing or FC03/mailbox emulation.

Last updated: 2026-09-27 after EXP259 / EXP260 prepared

## EXP260 bounded-batch protocol target

EXP256–259 have now locally reproduced the same genuine Eco 5 ordered Online/Link prefix through `042E/count15`. Because four consecutive reference stages have matched, EXP260 deliberately increases throughput while remaining fail-closed: it ACKs only the next three exact known reference blocks `042E/15`, `0442/13`, `0456/12`, in that order, and then captures the first different stage. The external reference predicts `046A/count18`.

This does **not** authorize broad FC16 ACKing or any `0708` mailbox response. A mailbox request at any point remains a capture-and-stop event in EXP260.

## EXP259 — local ordered Online/Link sync confirmed through `042E/count15`

EXP259 extends the bounded local XTR progression by exactly one ACK.

Observed local sequence:
`R1 -> 03E8/14 -> ACK -> 03FC/11 -> ACK -> 0410/22 -> ACK -> 042E/15`

Timing:
- approval: +1283 ms after BUS_RETURN;
- `03E8`: +138 ms after R1;
- `03FC`: +682 ms after `03E8` ACK;
- `0410`: +1498 ms after `03FC` ACK;
- `042E`: +696 ms after `0410` ACK.

Exact `042E/count15` payload words:
`0001 0001 0000 000A FFF6 0005 001E 0000 002D 0000 0000 0000 0000 0000 0000`.

**Strong conclusion:** the local XTR follows the same genuine Eco 5 initial synchronization ordering at least through the first four ordered FC16 pages:
`03E8/14 -> 03FC/11 -> 0410/22 -> 042E/15`.

**Unknown:** whether all later Eco 5 pages and the `0708/count6` mailbox phase are identical on the XTR. Full Online/Link establishment is not yet proven.

---

Last updated: 2026-09-27 after EXP258

## Reproducible incomplete-session UI failure mode — confirmed through EXP259

Across multiple active approval/sync experiments, including EXP259, entering the native Online/Link state machine and then deliberately stopping before a complete endpoint session produces the same front-panel symptoms: DHW-side literal `0` and exact `COMM. ERR ONLINE/LINK`. One normal controller reboot restores normal operation.

This strongly supports an incomplete-session timeout interpretation, but does not yet prove the exact causal point or required minimum service depth. A future sufficiently complete session that does not trigger the alarm would be the cleanest confirmation.


## EXP258 — XTR confirms third ordered Online/Link sync block

EXP258 extends the local post-approval proof by one stage. After one R1 response, one exact ACK of `03E8/count14`, and one exact ACK of `03FC/count11`, the next controller block is exact `0410/count22`. Timing: approval +1243 ms after BUS_RETURN; `03E8` +138 ms after R1; `03FC` +691 ms after the 03E8 ACK; `0410` +1501 ms after the 03FC ACK.

**Strong protocol conclusion:** the local XTR now matches the genuine Eco 5 ordered prefix through three FC16 pages:

`approval response -> 03E8/14 -> ACK -> 03FC/11 -> ACK -> 0410/22`.

`0410` was intentionally not ACKed, so no claim is made about later local ordering or mailbox entry. Full Online/Link establishment remains unproven.

The user again observed the DHW/tank-side literal `0` and the exact `COMM. ERR ONLINE/LINK` alarm. This repeat strengthens the interpretation that the alarm is associated with an approved-but-incompletely-serviced Online/Link session, but that remains a hypothesis until a sufficiently complete session avoids the alarm.

---

Last updated: 2026-09-27 after EXP257; EXP258 prepared. Detailed historical findings restored from the uploaded canonical snapshots.

## External Eco 5 endpoint behavior refined after EXP257

The complete raw capture confirms the cold-start approval stream is startup-bounded rather than a steady-state feature in the observed Eco 5 sessions: first approval requests occur about 1.2 s after bus return, while an already-running steady-state segment with the gateway connected has no `071C/0730` traffic. Therefore steady-state absence on another model is not evidence that its cold-start stream is absent.

Two genuine successful sessions provide the same transfer prefix:

`approval response -> 03E8/14 -> ACK -> 03FC/11 -> ACK -> 0410/22`

This is now locally matched by EXP257 through `03FC/11`.

`04A6/13` and `085F/5` should remain classified as recurrent/passive families that can be interleaved with the transfer. Their ACK timing is phase-dependent across the two external power-ups, so they are not established approval preconditions and should not be promoted into the invariant ordered sync chain.

The genuine endpoint begins answering `0708/count6` while FC16 synchronization is still underway. The raw repeated idle response is:

`0F 03 0C 0000 0000 0000 0000 0001 0000 <CRC>`

=> six words: `0000 0000 0000 0000 0001 0000`.

A public comment wrote the fifth word as `0100`; this is not what the raw frame contains under standard Modbus big-endian register ordering. Preserve the raw value `0001` unless later evidence establishes a deliberate byte-swapped semantic representation.

Later fifth-word values in the same session descend through `03DC` (988), 984, 976, 908, 896, 768, 512, then 0. The sequence is factual; "pending synchronization item counter" is only a hypothesis.

The known local `COMM. ERR ONLINE/LINK` after partial participation is compatible with a session-service timeout, but that causal interpretation remains a hypothesis until a sufficiently serviced local session avoids the alarm.
## EXP257 — local XTR reproduces genuine Eco 5 `03E8 -> 03FC` synchronization transition

EXP257 adds the first local XTR proof of the next acknowledged post-approval transition.

Observed sequence:

```text
0x0F FC17 approval request
  -> one replayed R1
  -> FC16 03E8/count14
  -> one standard FC16 ACK
  -> FC16 03FC/count11
  -> no further ACK
```

Timing in EXP257:
- approval request: +1285 ms after BUS_RETURN;
- `03E8/count14`: +130 ms after R1;
- `03FC/count11`: +691 ms after the one `03E8` ACK.

Exact `03FC` request:

`0F1003FC000B160028000A0037000000000000000200120028001E003C369E`

Payload words:

`0028 000A 0037 0000 0000 0000 0002 0012 0028 001E 003C`

The experiment deliberately did **not** ACK `03FC`.

**Strong protocol conclusion:** the local XTR now matches the genuine Eco 5 Online/DCM synchronization prefix through two post-approval stages:

`approval response -> 03E8/count14 -> ACK -> 03FC/count11`

The genuine Eco 5 reference proves this same transition in two independent successful approval cycles and then shows:

`03FC/count11 -> ACK -> 0410/count22`.

This materially strengthens the cross-model architectural link. It does not yet prove that the local XTR will follow the complete Eco 5 synchronization chain or reach the `0708/count6` mailbox/runtime phase.

No semantic register write was performed in EXP257: the only new active frame was a standard FC16 acknowledgement echoing address/count and carrying no register-value payload.

Last updated: 2026-09-27 after EXP256 + full external Eco 5 capture refinement
## EXP256 — R1 crosses approval boundary into native 03E8 synchronization

EXP256 materially resolves the ambiguity left by EXP252/EXP255. After one exact replay of the already-tested R1 response to the first local `071C/0730` approval request:

- the approval loop stopped after **one** request;
- no second approval request occurred;
- the controller immediately began `0x0F FC16 03E8/count14`;
- first `03E8/count14` arrived **124 ms after R1**;
- `03E8/count14` repeated **389 times** through +419.896 s;
- the only other FC16 family was one boot-only `04BA/count22` request before R1;
- passive runtime families `04A6/count13` and `085F/count5` were both absent;
- no FC03 request appeared;
- EXP256 deliberately provided no FC16 ACK or FC03 response.

**Strong protocol conclusion:** R1 is not merely suppressing one passive FC16 family. It advances the local XTR controller across the approval/retry state into the native acknowledged `0x0F` synchronization state machine, whose first observed stage is `03E8/count14`. With no endpoint ACK, the controller stalls and retransmits that block.

This links two previously separate findings:
- EXP252: R1 terminates the `071C/0730` retry loop and causes a reproducible controller-visible side effect;
- EXP137+: acknowledging native `03E8/count14` advances an ordered controller->0x0F transfer sequence.

The EXP255 numerical clue (`582 - 195 ≈ 386`) is now recorded as a misleading coincidence rather than the correct mechanism. EXP256 shows that the post-R1 traffic is a **new 03E8 synchronization family**, not persistence of the passive `04A6` family.

The user again observed the DHW/tank-side literal `0`, followed after the run by the exact same front-panel alarm as EXP252: **`COMM. ERR ONLINE/LINK`**. No VERSION-screen change was seen; this is compatible with the architecture because VERSION `EXP` display is controlled by the separate `0x06/AFD1` expansion metadata path, not by the `0x0F` approval/synchronization path tested here.

**Still unknown:** full Online/Link session establishment, the required ACK chain after `03E8`, any eventual FC03/mailbox phase, and the semantic meaning of the DHW-side `0`.
## 2026-09-27 — EXP256 approval-to-sync transition

EXP256 provides the first direct local link between the startup `071C/0730` approval exchange and the native `0x0F` synchronization chain.

Observed sequence:

```text
BUS_RETURN
  -> first exact 071C/0730 approval request
  -> one-shot R1 response
  -> approval retries stop
  -> 124 ms later: controller FC16 03E8/count14
  -> no endpoint ACK
  -> repeated 03E8/count14 for the remainder of the 7-minute run
```

Complete active census: `04BA/count22` x1 before R1, then `03E8/count14` x389; `04A6/count13` x0; `085F/count5` x0; no FC03 phase.

**Protocol consequence:** the earlier EXP255/EXP252 count coincidence did not represent simple selective `085F` suppression. R1 instead advances the controller into the first stage of the acknowledged native settings synchronization state machine previously mapped in EXP137+. The endpoint is expected to ACK the FC16 block before progression.

**Session-status refinement:** R1 is accepted far enough to suppress approval retries and start sync, but this is not proof of a complete Online/Link session. In EXP256 no FC16 ACK, FC03 mailbox response, or later sync stage was supplied.

**UI side effect:** the DHW/tank-side literal `0` reappeared and the front panel again raised **`COMM. ERR ONLINE/LINK`** after the active run, exactly reproducing EXP252; VERSION did not change. This makes the R1 incomplete-session side effect reproducible while remaining separate from the `0x06/AFD1` VERSION metadata path. Exact meaning of the `0` remains unknown.


---
## 2026-09-27 — complete genuine iTec Eco 5 gateway capture: approval -> sync -> mailbox chain

A complete 1482.480 s Eco 5 gateway capture provides the first continuous raw evidence connecting genuine approval responses to the downstream acknowledged synchronization state machine.

### Approval retry behavior

The capture contains 99 exact `0x0F FC17 read 0730/count8 + write 071C/count8` requests in three windows (29, 41 and 29 requests). Their median cadences are about 4.24 s, 4.26 s and 4.21 s. 98 of the 99 16-byte `071C` payloads are unique; one payload repeats once. Thus the genuine Eco 5 source normally regenerates the 16-byte challenge-like value across retries.

Two successful challenge/response pairs are present inline in the raw capture:

```text
C1 63CE FB32 C6F4 1382 0879 9237 0CAC EEBA
R1 1691 A5F3 F8E8 D587 3892 4416 E8E6 A3D5

C2 31FB 59FC 8FB1 175C D89F 904D 06D9 2EA4
R2 FD63 6CCD 0F92 1D83 FF23 2A1A 2413 B372
```

### Reproducible post-approval prefix

Both successful responses produce the same prefix:

```text
FC17 response
 -> 03E8/count14 request
 -> FC16 ACK 03E8/count14
 -> 03FC/count11 request
 -> FC16 ACK 03FC/count11
 -> 0410/count22 request
 -> FC16 ACK 0410/count22
```

Timing:

```text
                         R1 cycle       R2 cycle
03E8 request             +92 ms         +92 ms
03E8 ACK                 +137 ms        +122 ms
03FC request             +510 ms        +536 ms
0410 request             +1.950 s       +2.189 s
```

This is stronger than the earlier local EXP137 observation. `0410/count22` is not the demonstrated immediate successor to `03E8`; the genuine Eco 5 reference contains an intervening `03FC/count11` block.

### Ordered initial synchronization export

The first successful cycle establishes this ordered FC16 sequence (retries omitted):

`03E8/14 -> 03FC/11 -> 0410/22 -> 042E/15 -> 0442/13 -> 0456/12 -> 046A/18 -> 047E/19 -> 0492/11 -> 04A6/13 -> 04BA/22 -> 04D8/27 -> 04F6/14 -> 050A/19 -> 051E/10 -> 0532/18 -> 0546/20 -> 055A/33 -> 057B/33 -> 059C/33 -> 05BD/33 -> 05DE/33 -> 05FF/33 -> 0620/33 -> 0641/33 -> 0662/33 -> 0683/33 -> 06A4/33 -> 06C5/33 -> 06EA/7 -> 06F1/3 -> 06F4/19`.

The next observed stage is `07D0/count19`, interleaved with `FC03 0708/count6` mailbox polls. Later established traffic includes acknowledged `07E4`, `07F8`, `080C`, `0820`, `0834`, `0848`, `0864` and `0870` pages plus dynamic `0708` responses.

### Consequences for the local XTR project

- EXP256's local `R1 -> 03E8/count14` transition is now a direct prefix match to genuine Eco 5 Online/DCM behavior.
- The response replay reaches a real protocol boundary, not an arbitrary controller retry quirk.
- Full session establishment still cannot be inferred from R1 alone; the genuine endpoint acknowledges a long sequence and participates in `0708` mailbox/runtime exchange.
- EXP257 remains correctly bounded: ACK exactly the first local `03E8/count14` once, then capture the first different block without answering it.
- External-reference positive discriminator is now specifically `03FC/count11`. A local `0410/count22` first would demonstrate a platform/order difference and would also be valuable.

## Bus

- Modbus RTU-like framing
- 9600 baud
- 8 data bits, even parity, 1 stop bit
- valid Modbus CRC

## Important slaves

- 0x02: controller state/sequencer data
- 0x06: local expansion/accessory presence/version path; **not proven to be the Online/DCM endpoint**
- 0x0A: room-sensor path
- 0x0F: native controller application/settings/state serializer; genuine Online/DCM reference systems also use this role for mailbox/state exchange
- 0x1E: outdoor-unit path

## 0x06 FC17 expansion/accessory path

Controller reads AFC8..AFD3 (12 words) and writes AFDC..AFE0 (5 words).

Normal unserved poll cadence: ~4.3 s.
After valid accessory response: alternating fast cadence ~0.7 s / ~1.4 s.

Fast cadence proves syntactic participation only; it does not prove semantic acceptance.

## AFCA / word2 transport handshake

Canonical transaction:

1. semantic payload stable, AFCA=0000
2. assert AFCA=03E8
3. controller 0x0F:0861 rises to 16
4. deassert AFCA=0000 while payload remains stable
5. controller 0x0F:0861 falls to 0
6. payload may then change

EXP92 timing example:

- REQ assert -> ACK high: 401 ms
- REQ deassert -> ACK low: 1031 ms

This is a proven transport-level handshake.

The **AFCA value** `03E8` is therefore a transport strobe/constant in this 0x06 transaction and must not be confused with native `0x0F` register address `0x03E8`, which is independently proven to belong to the Heating Curve/settings family.

## Historical A80E/AFDC state propagation

Older passive data repeatedly showed:

- controller A80E: 0 -> 32
- next relevant 0x06 controller write AFDC: 0 -> 32
- later A80E: 32 -> 0
- then AFDC: 32 -> 0

This is controller-originated state propagation and is distinct from the 0861 transaction ACK.

## EXP92 result

A correctly completed four-phase handshake followed by 90 s of the historical REQ-low envelope:

00FF,0001,0000,0001,0...

did not reproduce the historical online-state cycle.

Therefore:

- completed transport handshake is not sufficient;
- historical envelope is not sufficient;
- their combination is not sufficient under the tested controller state.

## New controller-state correlation

Older passive capture:

- A80F changed 80 -> 50 after outdoor-unit request turned off;
- while A80F remained 50, repeated A80E/AFDC 0<->32 cycles occurred;
- later A80F changed 50 -> 80 and the outdoor-unit cycle request became active.

EXP92 controller frame showed:

- A80C=64
- A80D=0
- A80E=0
- A80F=10
- A810=10
- A811=FFFF
- A812=0

Working hypothesis: the historical DCM state cycle may be gated by controller state, with A80F=50 currently the strongest observed discriminator. Correlation is not causation. This passive discriminator remains the next DCM fallback after the higher-value EXP93 room-sensor write-path replication.

## Room-sensor semantic path

Our XTR M passive evidence:

- genuine room-sensor setpoint event updates central controller setpoint;
- value later propagates back through B3C5;
- independent master write to B3B1 was ACKed but not adopted by the controller.

Independent transmit-side confirmation from `piotr-romanowski/thermia-bus-sniffer` commit `b4c27157402c49624917d523e016b249cdfc4e11` on iTec Eco / DHP-AQ-family hardware establishes:

- `0x0A` controller poll reads `B3B0..B3B2` and writes `B3C4..B3C6`;
- `B3B0 / 46000` = room temperature x10;
- `B3B1 / 46001` = pending room-setpoint request, x1 whole °C;
- `B3B2 / 46002` = unused/unknown in that setup;
- a non-zero B3B1 returned in the slave response makes the controller adopt that room setpoint;
- the controller then pushes the adopted value back via `B3C5 / 46021`;
- returning B3B1=0 releases the request but leaves the adopted setpoint latched;
- restoring a previous value requires explicitly requesting that value.

**Strong architectural conclusion:** the failed independent master-write test does not contradict B3B1 semantics. The write path is slot/role sensitive: the ESP must behave as slave 0x0A and answer the controller's poll.

**Local status:** transmit semantics are independently confirmed cross-model but not yet confirmed on this XTR M. EXP93 is the collision-safe local replication test.
## Control architecture decision

The intended production control architecture is **not** room-sensor emulation. The target is to emulate the Thermia/Danfoss Online/Connect/DCM03 accessory on slave `0x06`. Slave `0x0A` findings remain protocol evidence only.

## DCM03 / Danfoss Link firmware evidence

Recovered host-side HE Set/Get framing from Link CC firmware:

```text
BYTE endpoint
BYTE counts = (GET_count << 4) | SET_count
WORD SET_ID[]
WORD GET_ID[]
SET values...
```

Relevant abstract parameter IDs include `0x030A OperationMode`, `0x4400..0x4417` DHP parameters, and especially `0x4414 IntegrationMode`. `IntegrationMode` is GET-on-sync + SET-on-sync and then clears its SET-on-sync flag. Parameters are grouped into partial sync groups 0/1/2.

The Link CC image does not expose the final DCM03 -> local Thermia RS485 serializer. Raw HE packet layouts tested directly through `AFC8..AFD3` were negative, so an additional DCM-side translation/state layer remains strongly indicated.

Official Danfoss documentation states that DHP-AQ Link integration requires HP software >=2.2 and that later Link firmware may re-offer Heat Curve for 30 minutes after initial communication when the HP rejects/forgets it. This supports an initial synchronization/desired-state model. It does not prove any specific meaning for `A80E`, `A80F`, or `AFDC`.

## EXP93 status refinement

Two supplied EXP93 logs show the experiment armed correctly but no stable `A80F=50`; the 180 s capture never started. Therefore EXP93 remains inconclusive and must not be recorded as a negative result.

## EXP94 cold-boot state machine result

A true controller cold boot with slave 0x06 unanswered produced the following reproducible sequence in the completed 600 s capture:

```text
~0.7 s:  A80F/A810 = 5
~1.8 s:  A80E 0x00 -> 0x08
~2.8 s:  A80E 0x08 -> 0x28
~5.6 s:  AFDC 0x00 -> 0x10; AFE0 25 -> 20
~11.3 s: A80F/A810 5 -> 10
then stable through 600 s
```

Final stable image:

```text
A80C..A812 = 0040,0000,0028,000A,000A,FFFF,0000
AFDC..AFE0 = 0010,0000,0000,0000,0014
0861        = 0000
```

No settings changes occurred. 140 unserved 0x06 polls stayed on the normal long cadence (4086..4537 ms).

**Strong conclusions:**

- cold-boot integration state settles within about 11 s when 0x06 is unanswered;
- there is no hidden late transition up to 10 minutes;
- historical `A80E/AFDC 0x20 <-> 0` cycling is not simply ordinary cold-boot initialization;
- `0861` remains distinct from the longer-lived A80E/AFDC state machine.

**Refined after EXP95:** `AFDC=0x10` cannot simply mean “no accessory present,” because EXP95 supplies a valid 0x06 responder and still reaches the same state. It remains consistent with a higher-layer not-established/waiting/session state; exact semantics are unknown.

## EXP95 completed result

EXP95 answered every exact post-cold-boot `0x06 FC23` poll with 12 zero words (`AFCA=0`).

Observed over the complete 120 s run:

```text
frames=1133
06polls=112
tx=112
refused=0
06_min_ms=638
06_max_ms=1503
0861_changes=0
settings_pushes=0
settings_changes=0
outdoor_state_changes=0
resync_delta=1
drop_delta=0
```

The controller still converged to:

```text
A80E = 0028
A80F = 000A
A810 = 000A
AFDC = 0010
0861 = 0000
```

**Strong conclusions:**

- valid 0x06 presence from the first cold-boot poll immediately establishes the fast transport cadence;
- it does not advance the DCM application/session state;
- `AFDC=0x10` is not simply an “accessory absent” indicator;
- transport presence, transaction REQ/ACK, and higher application/session state are separate observable layers.

## EXP96 completed result

EXP96 executed the historical envelope in the true cold-boot EXP95 context. The four-phase transport transaction completed cleanly:

```text
preload:   00FF,0001,0000,0001,0...
REQ high:  00FF,0001,03E8,0001,0...
0861:      0000 -> 0010 after 367 ms
REQ low:   00FF,0001,0000,0001,0...
0861:      0010 -> 0000 after 1196 ms
```

No semantic/application progress followed: `settings_changes=0`, `rsp02_changes=0`, and the higher-layer controller state did not advance beyond the EXP95 behaviour.

**Strong conclusion:** the historical envelope is sufficient for the proven transport REQ/ACK mechanism but is not a sufficient DCM03 identity/init/application message, even in cold-boot context.

## Natural A80E/AFDC transition observed before EXP96

Before EXP96 was armed, with the ESP passive, the bus naturally showed:

```text
A80E: 0028 -> 0020 -> 0000
AFDC: 0010 -> 0000
```

This was not experiment-induced.

**Refinement:** A80E/AFDC should no longer be treated as simple dedicated DCM-session indicators. They are more likely broader controller/accessory-state propagation fields; exact semantics remain unknown.

## EXP97 test target

EXP97 is fully passive and focuses only on correlating natural A80E/AFDC edges with already-observable state:

- `A80C..A812`;
- `A7F8..A806`;
- `AFDC..AFE0`;
- `0x0F:0861`;
- outdoor-unit command block `0x1E:0000..0008`;
- outdoor operating-state reference.

No `0x06` response or other TX is generated. The goal is to determine whether the natural `0x28->0x20->0x00 / 0x10->0x00` sequence belongs to ordinary controller/outdoor operation and thereby remove A80E/AFDC as misleading DCM-session success criteria.


## EXP97 natural-state result

The natural sequence was reproduced under fully passive observation:

```text
A80E 0028 -> 0020
~1.06 s later: A80E 0020 -> 0000
~2.66 s later: AFDC 0010 -> 0000
```

At every edge, `0861=0000`, outdoor state=`0010`, and captured `CMD1E` plus paired `RSP02` were unchanged. No ESP TX occurred.

**Protocol refinement:** A80E/AFDC cannot be treated as dedicated DCM03 login/session indicators. They are broader internal controller/accessory lifecycle fields whose exact semantics remain unknown. They should no longer be the primary success criterion for DCM semantic experiments.

## EXP98 result

EXP98 returns focus to the actual accessory response bank. It isolates the first response word only:

```text
A: AFC8=0000, all others 0000, 20 s
B: AFC8=00FF, all others 0000, 30 s
A: AFC8=0000, all others 0000, 40 s
AFCA remains 0000 throughout
```

This is not a write-command test. It is an influence test for whether AFC8 alone changes controller, settings, cadence, ACK, or outdoor behaviour.


## EXP98 result
AFC8=00FF alone is not a standalone semantic trigger. In a controlled A/B/A run it produced no detectable effect on controller state, AFDC..AFE0, 0861, settings, CMD1E, outdoor state or polling cadence.

## EXP99 target
Test the remaining historically observed non-REQ fields and their combinations in a compact matrix while keeping AFCA=0000. This preserves interpretability while increasing throughput compared with one experiment per word.


## EXP99 protocol result

A controlled ten-phase matrix tested `AFC8=00FF`, `AFC9=0001`, and `AFCB=0001` individually, pairwise, and together while keeping `AFCA=0000`. All combinations were inert: no `0861`, settings, controller, AFDC..AFE0, CMD1E, or outdoor-state reaction occurred.

**Refinement:** the historical pattern `00FF,0001,REQ,0001` should not be interpreted as three independent command selectors plus REQ. Of those four fields, only `AFCA=03E8` has independently proven behaviour. The remaining fields may be structured payload/header data that is only interpreted during a valid transaction.

## EXP100 protocol target

Test that exact remaining possibility by carrying six historically grounded AFC8/AFC9/AFCB combinations through the already-proven four-phase transaction handshake. This increases throughput while preserving one-variable-family interpretability and avoids arbitrary values or setting targets.

## EXP100 protocol result

Six historically grounded AFC8/AFC9/AFCB payload combinations were each transported through the proven four-phase transaction handshake. Every transaction generated a complete `0861 0->16->0` ACK cycle, but none changed settings, AFDC..AFE0, controller state, RSP02, CMD1E or outdoor state.

**Refinement:** `AFCA=03E8` is confirmed as transport/data-valid REQ independent of application semantics. The historical `00FF,0001,REQ,0001` pattern is not sufficient to encode a recognized DCM application command. The missing DCM03 serializer/state machine must involve other AFC8..AFD3 fields and/or a higher-level multi-message/session sequence.


## EXP100 finding — first historical response words are transport-insufficient

Six canonical REQ/ACK transactions tested AFC8=00FF, AFC9=0001 and AFCB=0001 separately and in combinations. All six received normal `0861 0->16->0` acknowledgements, while controller state, settings, AFDC..AFE0, 0x1E command state and outdoor state remained unchanged.

Therefore the historical `00FF,0001,REQ,0001` prefix is not a sufficient DCM03 application command. AFCA=03E8 remains the only word in that prefix with a proven role: transport REQ/data-valid.

## EXP101 probe scope

AFCC..AFD3 remain unmapped accessory->controller response words. Their semantics are unknown. EXP101 probes only the minimal non-zero value `0x0001`, one word at a time, inside the proven transport handshake. Any observed effect must therefore be treated as positional influence first, not yet as semantic decoding.

## EXP101 finding — tail words AFCC..AFD3

Each response-bank word `AFCC`, `AFCD`, `AFCE`, `AFCF`, `AFD0`, `AFD1`, `AFD2`, and `AFD3` was individually set to `0x0001` inside a valid canonical `AFCA=03E8` transaction. All eight transactions generated the normal `0861` ACK-high/ACK-low cycle but produced no detectable changes in controller state, paired RSP02, AFDC..AFE0, settings, CMD1E, or outdoor state.

Interpretation: no tail word is a simple standalone `0x0001` selector. Combined with EXP98–100, isolated-word probing across the full `AFC8..AFD3` bank has not revealed the DCM semantic layer. Future work should focus on structured multi-word messages, payload framing/metadata, or multi-message initialization/session sequencing.

## Archive recovery finding — prior tail coverage was broader than current summary

Historical logs show that the response-bank tail had already been exercised more extensively than the current condensed state suggested. EXP24/25 tested words 4..11 with `0001` while `0861` was high, and EXP26/28 tested structured word4/word5 values. EXP16/18/14/15 also showed that AFC9/AFC8/AFCB values can vary without changing the basic AFCA=03E8 transport ACK behavior.

**Protocol implication:** isolated value probing is exhausted. A more plausible structure is that one of the historical `0001` fields is metadata such as a payload length/count. If so, earlier probes that added data beyond word3 while retaining a count of 1 could have been ignored by design.

## EXP102 protocol target — coherent declared-length interaction

Test coherent count-plus-payload structures rather than arbitrary tail values. Compare the historical count-1 control against AFC9-declared lengths 2/3, AFCB-declared lengths 2/3, and a both-length2 case. This is the smallest controlled experiment that tests whether tail words become meaningful only when a matching length/count grows with them.

## EXP102 finding — AFC9/AFCB are not simple payload length/count fields

Six coherent structures were tested using the proven transport handshake. Increasing `AFC9` to 2/3 while adding AFCC/AFCD payload words, increasing `AFCB` to 2/3 with matching tail words, and setting both fields to 2 all produced normal `0861 0->16->0` transport ACKs but no semantic effect.

**Refinement:** neither AFC9 nor AFCB behaves like a simple declared word-count whose increase makes AFCC/AFCD meaningful. The missing DCM03 application layer is therefore more structured than the tested prefix/count model and likely requires a different framing rule or a multi-message/session sequence.


## Historical archive audit — response-bank search space refinement

A full archive audit after EXP102 recovered at least 45 unique logged experimental response forms and confirmed that first-word/header, selector, tail-word, same-packet, phase, presence/session, HE-envelope and count-like hypotheses have already been exercised extensively.

No archived trace could be identified as a genuine DCM03/Thermia Online response. Logged accessory response payloads are synthetic ESP experiment traffic; raw `06 17 AFC8...` frames are controller requests and expose only controller->accessory `AFDC..AFE0` data.

**Protocol implication:** further isolated field/value guessing is not justified. The unresolved DCM layer should be treated as a structured/stateful serializer problem. The highest-value missing evidence is a genuine DCM cold-boot dialogue and one known parameter change/rollback.


## EXP103 finding — repeated identical canonical transactions are insufficient

Three consecutive transactions using the unchanged historical envelope `00FF,0001,REQ,0001,0...` were completed without the recovery gap used in earlier matrices. All three produced the normal `0861` ACK-high/ACK-low cycle, but there were no settings, controller, AFDC..AFE0, CMD1E or outdoor-unit changes during the experiment.

**Refinement:** the missing DCM03 application layer is not unlocked merely by repeating the same accepted transport transaction several times in succession. This weakens a simple cumulative/retry-count interpretation and further shifts the remaining search toward a specific ordered startup dialogue, structured metadata/sequence/checksum, or proprietary DCM-side serialization.

A natural `A80E 0->32` followed by `AFDC 0->32` occurred only after the EXP103 summary and repeated later in the same log. This is additional evidence that these fields participate in ordinary controller lifecycle/state propagation and should not be used as DCM-session success markers.


## EXP104 negative finding — AFC8 is not a simple alternating transaction sequence field
A three-transaction canonical chain using AFC8 `00FF -> 00FE -> 00FF` produced normal transport ACKs on all three transactions but no settings or command effect. This reduces support for a simple AFC8 transaction identity/sequence interpretation. Natural A80E/AFDC `0x20` cycling occurred independently during the subsequent all-zero observation and repeated later, reinforcing that it is not a reliable DCM session-success marker.


## EXP105 protocol target — controller-state gating

EXP98–104 substantially reduce support for isolated payload, count, repetition, and simple AFC8-sequence interpretations. EXP105 therefore keeps the known historical payload unchanged and tests a different dimension: whether the controller only interprets a DCM application transaction during the naturally recurring `A80E=0x0020` / `AFDC=0x0020` lifecycle window. The ESP remains passive until that state is directly observed.


## EXP105 finding — natural A80E/AFDC 0x20 window is not sufficient

A known-good canonical transport transaction was deliberately delayed until the controller naturally presented `A80E=0x0020` and the `0x06` poll carried `AFDC=0x0020`. The transaction still produced only the normal `0861 0->16->0` transport ACK and no setting or command effect.

**Protocol implication:** the missing DCM03 application layer is not explained by a simple controller-state timing gate. Combined with EXP98–104, this further reduces the value of guessed payload/timing permutations. The highest-value next evidence remains a genuine DCM/Online capture or DCM-side firmware/hardware reverse engineering.


## EXP106 target — passive A80F=50 integration-sync discriminator

Firmware/project re-search did not reveal the missing DCM03 -> Thermia serializer or any direct mapping from HE/DHP ParameterIDs into `AFC8..AFD3`. The available host-side evidence still stops at abstract HE Set/Get and sync behaviour; the proprietary/local translation remains outside the recovered host firmware.

The remaining evidence-backed passive discriminator is historical `A80F=0x0032`. Earlier EXP93 captures never reached that state, so its relationship to A80E/AFDC cycling was never actually tested. EXP106 therefore performs no bus TX and captures the broader controller/accessory context when A80F enters/leaves 50.


## Cross-model refinement — Eco 8 / DHP-AQ evidence from Piotr Romanowski

### 0x1E delayed/latched region correction

The `0x1E FC04 0x001E..0x0033` region is **not frozen** and is not proven to be an initialization snapshot. It changes, but much less often and out of step with the live `0x0000..0x0015` block. Treat any apparent pairing as delayed/latched-looking and unconfirmed.

### 0x0A positive-control semantics

`B3B1` is now independently proven as a semantic accessory request field:
- whole-degree encoding (x1);
- non-zero value requests a stored room-setpoint change;
- `0` means no request;
- accepted changes are pushed back by the controller through `B3C5`.

This is a strong architectural reference: Thermia accepts semantic commands when they arrive **inside the polled accessory response**, not as arbitrary independent writes to the same register.

### AFDC..AFE0 on Eco 8

Long passive Eco 8 capture:
- `AFDD=0`
- `AFDE=0`
- `AFDF=0`
- `AFE0` = displayed outdoor temperature x1
- `AFDC` pulses `0 <-> 0x20` continuously with ~64 s period and ~17 s high time.

`A80E` follows the AFDC pulse timing to the second.

**Protocol implication:** A80E/AFDC `0x20` is not a DCM login/approval/session-success marker. It is best treated as ordinary controller lifecycle/heartbeat state.

An isolated `AFDC=0x10` event coincided once with outdoor-unit-active status rising. This single coincidence is insufficient to assign DCM approval semantics to `0x10`.

### 0861 discriminator strengthened

On Piotr's Eco 8, `0x0F:0861` remained at `0` throughout multi-day passive observation. This independently strengthens the interpretation that `0861` movement during Marten's active tests is specifically coupled to the `AFCA=0x03E8` transaction mechanism, rather than being a common spontaneous controller state.

### Search-model refinement for 0x06

Do not use AFDC/A80E values as timing gates for the next active 0x06 experiment.

A more evidence-based architecture hypothesis is:
- the 0x06 slave presents a continuously valid accessory image;
- some fields may be persistent identity/state/capability data;
- `AFCA` is a transaction/request level;
- semantic action may require a request pulse within an already-established stable accessory image.

This remains a hypothesis; the 12-word bank may still be a framed/stateful mailbox rather than purely fixed semantic fields.


## EXP107 prepared protocol question

The next active 0x06 test no longer uses A80F/AFDC/A80E as a DCM session discriminator.

Question:
Does the controller require a continuously-present accessory image before the known AFCA request pulse is treated differently?

Test image:
`AFC8..AFD3 = 00FF,0001,0000,0001,0,0,0,0,0,0,0,0`

After >=60 s of continuous presentation:
`AFCA only: 0000 -> 03E8 -> 0000`

Interpretation rules:
- `0861 0->16->0` = transport transaction completed;
- fast 0x06 cadence = presence only;
- A80E/AFDC changes = controller lifecycle/context only;
- semantic success requires an actual settings/state effect beyond transport ACK.

If EXP107 is negative, the simple "stable accessory image before request" hypothesis is rejected.


## EXP107 finding — persistent presence is not sufficient

Confirmed sequence with a 61.023 s pre-existing stable historical accessory image:

`REQ-low image stable`
→ `AFCA 0000 -> 03E8`
→ `0861 0 -> 16` after 328 ms
→ `AFCA 03E8 -> 0000`
→ `0861 16 -> 0` after 1122 ms
→ same image held 90 s

No semantic consequence:
- settings_changed=0
- A80E remained 0
- AFDC remained 0
- no new session/integration marker emerged
- parser/drop counters remained clean

Protocol conclusion:
The canonical AFCA/0861 mechanism is a transaction-level handshake and is not itself sufficient for application-layer DCM initialization, even after prolonged accessory presence.

Research priority moves from timing/persistence toward reconstructing the application initialization state machine (identity, binding, integration mode, initial sync).


## Firmware-derived application lifecycle — 2.7.42

Recovered from .NET IL inside `RegulationEngine.dll` and `ParameterCache.dll`:

`IntegrationMode (0x4414) update`
→ internal `SystemIntegrationInitRequest = true`
→ `SystemIntegrationInit()`
→ internal `InitSyncDone = false`
→ `Sync(fullUpdate=true)`
→ partial group 0
→ partial group 1
→ partial group 2
→ commit GET values if all groups succeed
→ internal `InitSyncDone = true`

Key correction:
`SystemIntegrationInitRequest` and `InitSyncDone` are internal host booleans, not protocol ParameterIDs.

`IntegrationMode` itself is the wire ParameterID, and `IsSystemIntegration` is simply `(IntegrationMode != 0)`.

`UpdateParameterFlow()` changes ownership of RoomValue, HeatCurve, HeatCurvePlus5, HeatCurveZero, HeatCurveMinus5:
- non-system integration: GET-on-sync
- system integration: SET-on-sync

This makes grouped synchronization / ownership a higher-priority local-mailbox hypothesis than another scalar ID/value probe.

### Identity/binding
`OnHEServiceBind()` compares DivisionID + BrandID + ProductID against allowed products before endpoint allocation.
This is confirmed on the HE/Z-Wave side only; mapping to AFC8..AFD3 remains unknown.


## 2026-09-24 refinement — 0x06 VERSION semantics and 0x0F application blocks

### 0x06 no longer treated as proven DCM/Online identity
Local experiments EXP129–132 materially refine the 0x06 interpretation:
- valid 0x06 responder causes `EXP` / `UITBR.KAART` to appear on the VERSION page;
- `AFD1` is rendered directly as version/10;
- tested `AFD0` values do not change the label/type;
- AFC8/AFC9/AFCB are not required for EXP-version display.

Protocol implication: `0x06` is proven as an accessory/expansion presence + metadata path. Calling it the DCM/Online device is no longer justified without additional evidence. It may still participate in Online integration, but that is now a hypothesis rather than a naming assumption.

### 0x0F application/settings role strengthened
Our own XTR captures contain native FC10 traffic to slave `0x0F`, including the established settings block beginning `0x03E8`. `0x03F4` (decimal 1012) follows the room setpoint and independently aligns with an external ATEC/DHP-AQ observation that 1012 is room-thermostat related.

External Discussion #143 material also reports 0x0F block starts including decimal 1000/1020/1040 and higher regions. These addresses and block lengths are hypotheses for XTR until locally observed. The external files are used as candidate generators only.

### Native 0x085F block
EXP133 partial passive capture locally observed an XTR `0x0F FC10` block at `0x085F`, count 5. This covers `0x085F..0x0863`, so the known transport ACK field `0x0861` is structurally inside a native controller block.

This strengthens:
- `0861` as a real field in a controller-side 0x0F block;
- interpretation of `AFCA=03E8 -> 0861=16` as a transaction-level interaction between the 0x06 accessory response path and a native 0x0F controller block.

It does not yet identify the complete block semantics.

### New native 0x04A6 block
EXP133 also observed a local XTR `0x0F FC10` block starting `0x04A6`, count 13. First captured payload was all zero except `0x04B0=0x4020`. Semantics are unknown. This block was not one of the imported external candidates and is therefore useful XTR-specific evidence.

### Current protocol priority
1. finish EXP133 and establish the native XTR 0x0F shape census;
2. use controlled passive UI correlations to map concrete fields (EXP134 starts with DHW START);
3. only after local read/correlation evidence, infer which 0x0F direction/block is appropriate for safe semantic write testing;
4. do not return to random AFC8..AFD3 payload guessing without new evidence.


## 2026-09-24 — Genuine Online capture changes the 0x0F / 0x06 model

New external evidence from a working Thermia Online installation:
- slave `0x0F` is a real responding Modbus slave in that installation;
- it ACKs FC16 writes and serves FC03 reads;
- controller-originated FC16 traffic cycles through large state/telemetry blocks;
- controller reads `0x03E8` from `0x0F`;
- during an intentional Heat Curve 20->21->20 change, the two captured `0x03E8` read snapshots differ only at the first word (`23 -> 22`);
- recurring `0x06` FC17 polls remain unanswered in the supplied working-Online capture;
- slave `0xA5` is active but unidentified.

Protocol implications:
1. `0x06` is still proven as an expansion/accessory interface but is not required for the Online function shown in this capture.
2. `0x0F` is strongly indicated as a shared controller <-> Online/DCM register interface.
3. Controller FC16 writes to `0x0F` likely carry controller->Online state.
4. Controller FC03 reads from `0x0F` likely consume Online->controller desired/config state.
5. Register direction/ownership is therefore central; a direct second-master write is not equivalent to emulating the expected slave-side register image.
6. Exact physical implementation of slave `0x0F` and the role of `0xA5` remain open.

EXP135/136 correction:
- `03F1` is not supported as live DHW START on the tested XTR M.
- DHW COMFORT/ECO does not alter recurrent `03E8..03F5`.
- `03F1`, `03F2`, `03F3`, `03F5` remain unknown.

Next controlled discriminator — EXP137:
ACK only exact known XTR slave-0x0F FC16 writes and observe whether controller FC03 reads begin. Do not answer FC03 in EXP137.


## EXP137 — acknowledged 0x0F synchronization progression

Local XTR result:
- passive baseline contains repeated `03E8/count14` and `085F/count5` writes with no slave ACK;
- after one standard FC16 ACK to `03E8/count14`, the controller begins issuing `0410/count22`;
- without an ACK, `0410/count22` is retransmitted continuously;
- no FC03 read phase appears before `0410/count22` is acknowledged;
- bus/parser health remains clean.

Protocol implication:
`0x0F` is not behaving like a fire-and-forget telemetry mirror. At least part of the controller->0x0F traffic forms an acknowledged sequential transfer/state machine.

New locally proven XTR block:
`0x0410..0x0425` (count 22).

This block contains external candidate `0x041D` (1053), so the address exists locally in the XTR transfer family, but no semantic label is yet proven.

Next controlled discriminator:
ACK `0410/count22` in addition to the already-used exact known shapes; continue to refuse all unknown shapes and never answer FC03.


## EXP138 prepared discriminator

EXP137 established a locally observed acknowledged progression:
`03E8/count14 -> ACK -> 0410/count22`, after which the controller stalled on repeated `0410/count22` because no ACK was returned.

EXP138 changes only one variable:
acknowledge that exact `0410/count22` request.

Protocol question:
Does `0410/count22` ACK advance the XTR controller to:
- another FC16 transfer block; or
- the FC03 read-side phase seen in the genuine Thermia Online capture?

No newly appearing block will be ACKed in EXP138. FC03 will not be answered.


## Raw-frame correction: 0x0848 Heat Curve follow-up
The follow-up GitHub analysis of the genuine Online capture over-interpreted the `0x0848` block.

Exact decoded words:
- ~12.116 s, `0848/count23`: `0858=0000`, `0859=0004`, `085A=0014`, ...
- ~33.107 s, `0848/count23`: `0858=0015`, `0859=0004`, `085A=0014`, ...

Thus:
- `0858` changes `0 -> 21`;
- `085A` stays `20`;
- no same-register `20 -> 21` transition exists in those two `0848` frames.

The later `07E4` frame is a different block and cannot be used as a same-register revert without additional evidence.

Status:
- `0858` = STRONGLY INTERESTING / Heat-Curve-change correlation candidate.
- exact semantics = OPEN.
- do not encode `0858 = Heat Curve` yet.


## EXP138 — next 0x0F sequence stage proven

Local XTR sequence now proven:
`03E8/count14 -> ACK -> 0410/count22 -> ACK -> 042E/count15`.

Important persistence observation:
After EXP137 ended while the controller was waiting for an ACK to `0410/count22`, an ESP reboot and new firmware did not reset the controller-side transfer state. EXP138's passive baseline immediately contained repeated `0410/count22`. Therefore the sequence state is maintained by the Thermia/controller side, not by transient ESP state.

New local block:
`0x042E..0x043C` (count 15; decimal 1070..1084).

This aligns structurally with the external DHP/ATEC block family at decimal 1070..1084, but individual semantics are not imported as proven XTR mappings.

Next discriminator:
ACK only `042E/count15` as the one new variable; stop without answering the first new FC16 stage or FC03 read.


## EXP139 prepared discriminator — ACK 0x042E/count15

Locally proven progression before EXP139:
`03E8/14 -> ACK -> 0410/22 -> ACK -> 042E/15`.

EXP139 changes one variable only:
acknowledge `042E/count15`.

This block covers `0x042E..0x043C` (decimal 1070..1084). Structural agreement with the external DHP/ATEC 1070..1084 family is noted, but no individual semantic labels are imported.

Positive:
- first new FC16 stage after a successful 042E ACK, or
- first 0x0F FC03 request.

Neither will be answered in EXP139.


## EXP139 — 0x0F sequence extends through 0x04A6 to 0x04BA

Observed local XTR progression:
`042E/count15 -> ACK -> 04A6/count13 -> ACK -> 04BA/count22`.

Combined with prior experiments:
`03E8/14 -> ACK -> 0410/22 -> ACK -> 042E/15 -> ACK -> 04A6/13 -> ACK -> 04BA/22`.
