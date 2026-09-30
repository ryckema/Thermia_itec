# EXP345 — COMPLETE / POSITIVE — persistent DCM runtime with 0708 W5=0006

**Date:** 2026-09-30

**Hypothesis:** W5 in the FC03 0708/count6 mailbox response participates in the controller's DCM-connected/liveness decision.

**Baseline:** EXP344 used an all-zero idle 0708 response and stayed transport-clean >15 minutes, but the DCM icon was absent after the soak.

**Controlled change:** only W5 changed:

    EXP344 W0..W5 = 0000 0000 0000 0000 0000 0000
    EXP345 W0..W5 = 0000 0000 0000 0000 0000 0006
    EXP345 frame    = 0F030C0000000000000000000000069D76

All bootstrap, initial-sync, runtime FC16 whitelist/ACK and soak behavior was preserved. No semantic desired-page write was enabled.

## RESULT

**Status:** **COMPLETE / POSITIVE**

Fresh bootstrap completed and stage 40 persistent runtime was entered. At runtime age 900.5 s the firmware emitted SOAK_15M_PASS with runtimeFC16ACK=379, idle0708=210, rt085F=1, rt04A6=0, unknown16=0, unknown03=0, peer17=0, peer16ack=0, resync=0, drops=0, CONTINUE_RUNNING=1, DE=LOW. The service continued after the milestone. User observation: **DCM icon remained present** and **no COMM. ERR ONLINE/LINK**.

**Conclusion:** compared with EXP344's otherwise-equivalent negative control, W5=0006 retained the DCM-connected UI indication while preserving the clean persistent runtime. This proves sufficiency in the tested local session; it does not decode W5's semantic meaning.

---

# EXP344 — COMPLETE / NEGATIVE for persistent DCM-connected indication; POSITIVE transport sub-result

**Date:** 2026-09-30

Persistent stage-40 runtime with all-zero idle 0708 response remained clean for >15 minutes and produced no Online/Link error, but the user observed that the DCM icon was no longer present after the soak. This is the controlled baseline for EXP345.

---

# EXP343 — COMPLETE / POSITIVE — semantic 03F4 desired-page write

**Date:** 2026-09-30

**Controlled change from EXP342:** EXP342 returned a no-op clone of the current 03E8/14 page. EXP343 changed exactly one word, 03F4 0016 -> 0015, preserving all other words from the same-session cache.

## RESULT

**Status:** **COMPLETE / POSITIVE**

Authentic PULL selector 0F030C0000000100000001000000002D24 was sent. The controller pulled 03E8/14. The emulator returned 0F031C0024001400280000000000000014001400020028001E000100150002C29F. About 690 ms later the controller republished FC16 03E8/14 with observed 03F4=0015, desiredMatch=1 and extraDeltaBytes=0. The experiment stopped as COMPLETE / POSITIVE. Room Setpoint Mirror and Room Setpoint reported 21 °C. No confirmation ACK was sent and no peer/resync/drop anomaly was observed.

**Conclusion:** semantic desired-page application through the native 0708/PULL/FC03 page-response path is **PROVEN / locally confirmed** for the tested 03F4 22 -> 21 °C transition.

---
# EXP340 — COMPLETE / INCONCLUSIVE

**Date:** 2026-09-30

**Hypothesis:** in retained runtime, exact 07F8/count17 ACK -> exact 0708/count6 -> one genuine Eco5 all-zero six-word mailbox response should advance to the next non-background FC16 page.

**Controlled change from EXP339:** retain the one exact 07F8 ACK and add exactly one all-zero response to the locally observed post-07F8 0708 poll; then capture-only.

**Observed:** about 0.49 s after ARM, before 07F8 or 0708 and before any EXP340 TX, exact FC16 080C/count18 appeared. The experiment stopped fail-closed. peer17=0, peer16ack=0, resync=0, drops=0, DE LOW.

**Result:** **COMPLETE / INCONCLUSIVE**. The intended hypothesis was not tested. The retained controller runtime had already advanced beyond the planned starting page during/after the ESP OTA reboot.

---

# EXP339 — COMPLETE / INCONCLUSIVE

**Date:** 2026-09-30

**Hypothesis:** ACKing exact retained 07F8/count17 once will advance to the next runtime FC16 page.

**Controlled change from EXP338:** wait exact 07F8, ACK it once with 0F1007F8001181AE, then capture the next non-background FC16; no mailbox response.

**Observed:** exact 07F8/count17 arrived, was ACKed once, and about 1.57 s later exact FC03 0708/count6 appeared before another FC16. No 0708 response was sent; run stopped cleanly.

**Result:** **COMPLETE / INCONCLUSIVE**. The post-07F8 transition is locally confirmed to admit/interleave a 0708 mailbox poll.

---

# EXP338 — COMPLETE / INCONCLUSIVE

**Date:** 2026-09-30

**Hypothesis:** a retained 0708/count6 poll answered once with the genuine Eco5 all-zero six-word response will advance to the next runtime FC16.

**Controlled change from EXP337:** no 07D0/07E4 ACKs; wait retained 0708 and respond once; capture next FC16.

**Observed:** about 0.82 s after ARM, before any retained 0708 and with zero experiment TX, exact FC16 07F8/count17 appeared. The run stopped fail-closed.

**Result:** **COMPLETE / INCONCLUSIVE**. The intended 0708-response hypothesis was not tested. Retained runtime progress continued across ESP OTA.

---

# EXP337 — COMPLETE / POSITIVE

**Date:** 2026-09-30

**Hypothesis:** in retained runtime, exact 07D0/count19 ACK -> exact 07E4/count17 ACK -> exact FC03 0708/count6, without a fresh Thermia boot or startup replay.

**Controlled change from EXP336:** remove the retained 0708 response test; instead ACK retained 07D0 once, ACK retained 07E4 once, then capture 0708 without responding.

**Observed:** exact retained 07D0/19 was ACKed once; exact 07E4/17 followed about 2.205 s later and was ACKed once; exact FC03 0708/6 followed about 1.453 s after the 07E4 ACK. No R1, fresh sync, 085F ACK or mailbox response occurred in the run. Parser/RX counters remained clean and DE LOW.

**Result:** **COMPLETE / POSITIVE**.

---

# EXP336 — COMPLETE / INCONCLUSIVE

**Date:** 2026-09-30

**Hypothesis:** in retained runtime, exact 0708/count6 -> one historical phase-matched 0080/0006 mailbox response -> 07D0/count19.

**Controlled change from EXP335:** ESP OTA only, no Thermia reboot, no R1/cold ACK/new 085F ACK; wait retained 0708 and respond once.

**Observed:** about 0.53 s after ARM and before any 0708 or experiment TX, exact 07D0/count19 appeared. challenges=0, postR1=0, rspUsed=0, resync=0, drops=0, DE LOW.

**Result:** **COMPLETE / INCONCLUSIVE** for the planned hypothesis. **Positive retained-session evidence:** controller-side Online/runtime state survived ESP OTA and emitted 07D0 without a new startup exchange or an immediately preceding experimental mailbox response.

---

# EXP335 — COMPLETE / INCONCLUSIVE

**Date:** 2026-09-30

**Hypothesis:** after the fresh proven chain through 06F4, one exact all-zero 085F/count5 ACK might be sufficient to produce 07D0 without a mailbox response.

**Controlled change:** ACK exact post-tail all-zero 085F once; do not answer 0708.

**Observed:** after 06F4 ACK, all-zero 085F/5 appeared and was ACKed once. Exact FC03 0708/count6 appeared about 1.48 s later before 07D0. No mailbox response was sent.

**Result:** **COMPLETE / INCONCLUSIVE**. This is a local counterexample to the simplified rule '085F ACK alone immediately yields 07D0'.

---

# EXP334 — COMPLETE / INCONCLUSIVE

**Date:** 2026-09-30

**Hypothesis:** after the full fresh prefix through 06F4, bounded service of 0708 with the historical all-zero-like response 0000 0000 0000 0000 0001 0000 while leaving 085F un-ACKed may advance to runtime.

**Controlled change:** ignore post-tail 085F; send at most three matching 0708 responses.

**Observed:** full chain through 06F4 completed; first 085F was ignored; three 0708 replies were sent; no fourth 0708 and no 07D0 appeared in the bounded window; recurring 085F continued. Bus integrity stayed clean.

**Result:** **COMPLETE / INCONCLUSIVE**. Three mailbox replies without the post-tail 085F ACK were insufficient to establish 07D0 in this run.

---

# EXP333 — COMPLETE / POSITIVE

**Date:** 2026-09-30

**Hypothesis:** after the EXP332-proven prefix through 06C5, ACK 06EA/7, 06F1/3 and 06F4/19 and passively observe the post-sync transition.

**Observed:** fresh fixed-R1 session reproduced the entire prior chain; exact 06EA/7, 06F1/3 and 06F4/19 were each ACKed. About 82 ms after 06F4 ACK, 085F/5 appeared; about 1.56 s after 06F4 ACK, exact FC03 0708/count6 appeared. No response was sent to either.

**Result:** **COMPLETE / POSITIVE**. Fresh-session initial sync is locally proven through 06F4 and reaches the 085F/0708 post-tail region.

---

# EXP332 — COMPLETE / POSITIVE

**Date:** 2026-09-30

**Hypothesis:** after the proven prefix through 0546, a bounded run of the twelve 33-word blocks 055A..06C5 will advance to 06EA/7.

**Controlled change from EXP331:** ACK exactly 055A, 057B, 059C, 05BD, 05DE, 05FF, 0620, 0641, 0662, 0683, 06A4 and 06C5, each count33; capture 06EA without ACK.

**Observed:** the twelve-block sequence completed in order and exact 06EA/count7 appeared as the next stage.

**Result:** **COMPLETE / POSITIVE**.

---

# EXP331 — COMPLETE / POSITIVE

**Date:** 2026-09-30

**Hypothesis:** extend the locally proven fresh prefix from 04A6/13 through 0546/20 and capture 055A/33.

**Controlled change from EXP330:** add the bounded exact ACK sequence 04A6/13, 04BA/22, 04D8/27, 04F6/14, 050A/19, 051E/10, 0532/18, 0546/20; then capture-only.

**Observed:** the ordered continuation completed and exact 055A/count33 appeared.

**Result:** **COMPLETE / POSITIVE**.

---
# EXP331 — PREPARED / NOT RUN

**Date:** 2026-09-30

**Hypothesis:** after the locally proven EXP330 prefix through `0492/11 ACK -> 04A6/13`, a bounded eight-page ACK batch matching genuine Eco 5 / earlier research will advance through:

`04A6/13 -> 04BA/22 -> 04D8/27 -> 04F6/14 -> 050A/19 -> 051E/10 -> 0532/18 -> 0546/20 -> 055A/33`.

**Controlled change from EXP330:** ACK the eight exact pages above once each. The proven prefix is otherwise unchanged. After `0546/20` ACK, capture-only.

**New ACKs prepared:**
- `04A6/13` -> `0F1004A6000DE1F1`
- `04BA/22` -> `0F1004BA0016603C`
- `04D8/27` -> `0F1004D8001B0027`
- `04F6/14` -> `0F1004F6000EA1E1`
- `050A/19` -> `0F10050A0013A024`
- `051E/10` -> `0F10051E000A21EA`
- `0532/18` -> `0F1005320012E029`
- `0546/20` -> `0F10054600142031`

**Success:** exact `055A/count33` is first different FC16 after the `0546` ACK.

**Abort / fail-close:** wrong page shape/order/timing, previous-page retry, early FC03, parser/RX integrity delta, peer FC17 response or unexpected peer FC16 ACK.

**Safety:** address/count ACKs only; no register-value injection; no 055A ACK; no mailbox response; DE LOW on stop. ESPHome compile was not independently run when prepared.

---

# EXP330 — COMPLETE / POSITIVE

**Date:** 2026-09-30

**Hypothesis:** after the proven prefix to `046A/18`, exact one-shot ACKs for `046A/18`, `047E/19` and `0492/11` advance the same fresh initial-sync chain to `04A6/13`.

**Controlled change from EXP329:** add exactly those three standard FC16 address/count ACKs; leave the first post-`0492` stage capture-only.

**Observed result:** exact `046A/18 -> ACK -> 047E/19 -> ACK -> 0492/11 -> ACK -> 04A6/13`. `04A6/13` arrived approximately 571 ms after the `0492` ACK and was not ACKed. No approval retry, external responder, parser resync or RX drop; DE LOW.

**Result:** **COMPLETE / POSITIVE**.

---

# EXP329 — COMPLETE / POSITIVE

**Date:** 2026-09-30

**Hypothesis:** a bounded three-block continuation after the proven prefix advances `042E/15 -> 0442/13 -> 0456/12 -> 046A/18`.

**Controlled change from EXP328:** add one standard ACK each for exact `042E/15`, `0442/13`, `0456/12`; capture the next stage without ACK.

**Observed result:** exact ordered chain `042E/15 ACK -> 0442/13 ACK -> 0456/12 ACK -> 046A/18`. `046A/18` appeared approximately 1428 ms after the `0456` ACK. No post-R1 challenge retry, external responder, parser resync or RX drop; DE LOW.

**Result:** **COMPLETE / POSITIVE**.

---

# EXP328 — COMPLETE / POSITIVE

**Date:** 2026-09-30

**Hypothesis:** one standard ACK to exact `0410/count22` advances the local XTR initial sync to `042E/count15`.

**Controlled change from EXP327:** add exactly one `0410/22` address/count ACK; capture next stage only.

**Observed result:** the proven prefix reproduced; exact `0410/22` was ACKed once and exact `042E/15` appeared about 709 ms later. No further ACK. Clean parser and DE LOW.

**Result:** **COMPLETE / POSITIVE**.

---

# EXP327 — COMPLETE / POSITIVE

**Date:** 2026-09-30

**Hypothesis:** one standard ACK to exact `03FC/count11` advances the local initial sync to `0410/count22`.

**Controlled change from EXP326:** add exactly one `03FC/11` address/count ACK; capture next stage only.

**Observed result:** fresh approval and `03E8 ACK -> 03FC` reproduced; `03FC/11` was ACKed once and exact `0410/22` appeared about 1500 ms later. No further TX. Clean run.

**Result:** **COMPLETE / POSITIVE**.

---

# EXP326 — COMPLETE / POSITIVE

**Date:** 2026-09-30

**Hypothesis:** after fresh approval R1, one standard ACK for the first exact `03E8/count14` advances the controller to the next native sync stage.

**Controlled change from EXP325:** add only one `03E8/14` standard FC16 ACK `0F1003E8000EC093`.

**Observed result:** after fresh reboot and guard `A80E=0000 / A80F=0005`, a different live `071C/0730` challenge received fixed R1. Exact `03E8/14` appeared about 124 ms later. One ACK was sent, then exact `03FC/11` appeared about 697 ms after that ACK. No further TX. Parser resync 0, drops 0, DE LOW.

**Result:** **COMPLETE / POSITIVE**.

---

# EXP325 — COMPLETE / POSITIVE

**Date:** 2026-09-30

**Hypothesis:** after a true controller reboot, one previously accepted fixed R1 response to the first exact fresh `071C/0730` challenge is sufficient to open native initial sync.

**Controlled change from EXP322:** no 0x06 responder; only the first exact fresh challenge may receive one fixed R1. No FC16 ACK, no mailbox response.

**Observed result:** fresh guard `A80E=0000 / A80F=0005`; first exact `071C/0730` challenge received fixed R1. Exact `03E8/count14` appeared about 120 ms later. No prior 04A6 ACK, 085F ACK, FC16 ACK or mailbox response was required.

**Result:** **COMPLETE / POSITIVE**.

**Superseded historical note:** the earlier EXP325 concept for a cold-boot single `04A6` ACK was never run and is **SUPERSEDED / NOT RUN**. The experiment number was reused for the fresh-reboot R1 re-approval test above.

---

# EXP324 — COMPLETE / INCONCLUSIVE

**Date:** 2026-09-30

**Hypothesis:** after the EXP323 all-zero `085F` ACK, a longer post-ACK observation following ESP reboot would reveal delayed continuation.

**Controlled change:** longer intended observation, but the Thermia controller itself was not rebooted.

**Observed result:** the intended all-zero `085F` qualification state never reappeared. During the bounded window only `04A6/13` was seen; TX=0. Therefore the post-`085F` hypothesis was not actually exercised.

**Result:** **COMPLETE / INCONCLUSIVE**.

---

# EXP323 — COMPLETE / INCONCLUSIVE

**Date:** 2026-09-30

**Hypothesis:** in the clean post-controller-reboot sparse state, one standard ACK to a conservatively qualified all-zero `085F/5` can advance the scheduler.

**Controlled change from EXP322:** first exact all-zero `085F` is qualification/no-TX; second receives exactly one standard ACK `0F10085F00053356`; all later traffic capture-only.

**Observed result:** one ACK was sent. For roughly 42 s afterward, only `04A6/13` appeared; no further `085F` or known runtime/configuration stage was observed. Parser remained clean and DE LOW.

**Result:** **COMPLETE / INCONCLUSIVE**. One all-zero `085F` ACK alone was not shown to establish fresh Online progression.

---

# EXP322 — COMPLETE / POSITIVE — clean post-controller-reboot passive baseline

**Date:** 2026-09-30

**Hypothesis:** after the user rebooted the Thermia controller to clear the visible errors, the clean state may expose a different passive slave-`0x0F` sequence from the pre-reboot EXP321 state.

**Controlled change:** strict passive 90 s census after the controller reboot. Experiment TX was structurally disabled.

**Observed:**
- `total0F=125`, `FC16=125`, `FC03=0`;
- `04A6/13=83`, payload changes=0;
- `085F/5=42`, all 42 exact all-zero, `085F(0800)=0`;
- `0708=0`;
- every tracked normal-runtime page `07D0..0884=0`;
- `other=0`;
- `resync=0`, `drops=0`, `TX=0`, `DE=LOW`.

The first `04A6` was followed about 0.69 s later by all-zero `085F`. The same two frame classes dominated the complete run at approximately 2:1 cadence.

**Result:** **COMPLETE / POSITIVE** as a passive baseline.

**Strong conclusion:** repeated `04A6` alone is not specific to the prior visible alarm state. After a controller reboot, all-zero `085F/5` reappears persistently and is the clearer state discriminator versus EXP321.

---

# EXP321 — COMPLETE / INCONCLUSIVE — planned recovery entry absent

**Date:** 2026-09-30

**Hypothesis:** reconstruct the proven retained chain and hand off from qualified `07D0/19` to the existing steady-runtime responder for a short integration run.

**Observed:**
- 120 s qualification window completed;
- no exact `085F(0800)` entry frame appeared;
- approximately 111 x `04A6/13`;
- no all-zero `085F`;
- `TX=0`, `handoff=0`, `loops=0`;
- `unexpected=0`, `resync=0`, `drops=0`, DE LOW.

**Result:** **COMPLETE / INCONCLUSIVE.** The intended recovery chain was never exercised.

The user then rebooted the Thermia controller to clear visible errors before EXP322.

---

# EXP320 — COMPLETE / POSITIVE — qualified 0884 ACK reaches direct 07D0

**Date:** 2026-09-30

**Hypothesis:** from the locally reconfirmed retained chain `085F(0800) -> zero 085F -> 0884`, one qualified standard `0884/60` ACK reveals the next retained-session state.

**Observed:**
- two exact `085F(0800)` requests; ACK second once;
- two exact all-zero `085F`; ACK second once;
- two valid `0884/60`; ACK second once;
- 4.328 s after the `0884` ACK, first non-`04A6` frame was direct `07D0/19`;
- post-target `07D0` intentionally NO_TX;
- `TX=3`, `0800ACK=1`, `zeroACK=1`, `0884ACK=1`;
- `unexpected=0`, `resync=0`, `drops=0`, DE LOW.

**Result:** **COMPLETE / POSITIVE.**

**Strong conclusion:** in this retained context, `0884 ACK -> 07D0` is valid without mandatory immediate `0708`.

---

# EXP319 — COMPLETE / POSITIVE — all-zero 085F ACK exposes direct 0884

**Date:** 2026-09-30

**Hypothesis:** after normalizing `085F(0800)`, ACK a qualified exact all-zero `085F/5` and capture the first subsequent non-`04A6` frame.

**Observed:**
- two exact `085F(0800)`; ACK second once;
- two exact all-zero `085F`; ACK second once;
- 2.381 s after the all-zero ACK, first non-`04A6` frame was exact FC16 `0884/60`;
- `TX=2`, `0800ACK=1`, `zeroACK=1`, `0884ACK=0`;
- no runtime response after target; clean fail-close.

**Result:** **COMPLETE / POSITIVE.**

---

# EXP318 — COMPLETE / POSITIVE — 085F(0800) ACK reconfirms all-zero transition

**Date:** 2026-09-30

**Hypothesis:** after two exact `085F(0800)` requests, ACK the second once and capture the first subsequent non-`04A6` frame.

**Observed:**
- first target NO_TX;
- second target received one standard `085F/5` ACK;
- 2.196 s later first non-`04A6` frame was exact all-zero `085F/5`;
- `TX=1`, `0800ACK=1`, `zeroACK=0`;
- clean fail-close with no parser/RX integrity error.

**Result:** **COMPLETE / POSITIVE.**

---

# EXP317 — COMPLETE / INCONCLUSIVE — progress-anchored timeout, but no post-085F transition

**Date:** 2026-09-30

**Controlled change from EXP316-Q:** stage-1 timeout was anchored to last supported progress rather than absolute test start.

**Observed:**
- one known `085F(0800)` ACK was sent early;
- then no supported recovery/handoff progress for about 90 s;
- 86 x `04A6/13` capture-only;
- `TX=1`, `handoff=0`, `cycles=0`, `loops=0`, `unexpected=0`, `resync=0`, `drops=0`, DE LOW.

**Result:** **COMPLETE / INCONCLUSIVE.**

---

# EXP316-Q — COMPLETE / INCONCLUSIVE — quiet long-run harness timeout flaw

**Date:** 2026-09-30

**Purpose:** quiet logging variant of the EXP316 integration/endurance harness.

**Observed:**
- `085F(0800)` appeared at about 84.8 s and received one known ACK;
- roughly 5 s later the harness fired its absolute 90 s-from-start timeout;
- `TX=1`, `handoff=0`, `cycles=0`, `loops=0`, `events=0`, `r0708=0`;
- `04A6=78`, `resync=0`, `drops=0`, DE LOW.

**Result:** **COMPLETE / INCONCLUSIVE.** This was a harness-timeout defect, not a protocol-negative result.

---

# EXP316 — RUNNING / PARTIAL, then superseded by quiet variant

**Date:** 2026-09-30

Initial full-logging integration showed a healthy exact `07D0` handoff into the known runtime graph, but logging volume was about 0.5 MB per four minutes. It was replaced by EXP316-Q to test the same concept with quiet diagnostics.

**Status:** **RUNNING / PARTIAL**, then operationally superseded by EXP316-Q; do not treat it as a completed endurance result.

---

# EXP315 — COMPLETE / POSITIVE — direct retained 07E4 handoff sustains steady runtime

**Date:** 2026-09-30

**Hypothesis:** a controller retained at the already proven normal-runtime node `07E4/count17` can be safely taken over by qualifying repeated live `07E4` requests, sending one already-proven standard ACK, and then handing directly to the established EXP296/297 steady-runtime responder.

**Baseline:** EXP314 COMPLETE / INCONCLUSIVE.

**Exact controlled change from EXP314:**
- authorize exact `07E4/count17` as a retained-runtime handoff node;
- require >=2 live exact `07E4/17` requests before any EXP315 TX;
- ACK only the second qualified `07E4` with `0F 10 07 E4 00 11 40 68`;
- enter the existing post-`07E4` runtime state, allowing evidence-backed `0708` or direct `07F8`;
- no new register/page, payload value or semantic write.

**Observed:**
- one initial `0708/6` was capture-only;
- exact `07E4/17` then appeared twice;
- the second `07E4` received one standard ACK and the emulator entered stage 2 steady runtime;
- the established runtime scheduler was serviced continuously;
- 6 full returned runtime loops completed;
- steady runtime reached 126.401 s;
- 30 runtime `0708` responses were sent in evidence-backed contexts;
- the success boundary was the next returned `07D0/19`, intentionally left NO_TX;
- final summary: `TX=84`, `events=84`, `r0708=30`, `unexpected=0`, `resync=0`, `drops=0`, `DE=LOW`;
- final firmware status: `POSITIVE / retained recovery sustained proven steady runtime`.

**Result:** **COMPLETE / POSITIVE.**

**Strong conclusion:** on this XTR M, an already-active Online/DCM runtime can be rejoined directly at a qualified retained `07E4/17` node after ESP restart/OTA, and the existing runtime responder can then sustain at least 126.401 s / 6 complete loops without a controller reboot.

---

# EXP314 — COMPLETE / INCONCLUSIVE — controller retained progress to 07E4 while ESP was offline

**Date:** 2026-09-30

**Hypothesis:** the post-`07D0` `0708/6` observed in EXP313 is a valid handoff-boundary mailbox/scheduler event; servicing it with the existing proven runtime response should allow entry to steady runtime.

**Baseline:** EXP313 COMPLETE / INCONCLUSIVE.

**Exact controlled change from EXP313:**
- allow one exact post-handoff `0708/6` at the retained `07D0` boundary;
- respond with the already-proven runtime `0708` response only in that newly authorized context;
- retain the same adaptive recovery and steady-runtime graph otherwise.

**Observed:**
- after ESP restart, the controller no longer presented the expected `07D0`/boundary-`0708` state;
- on each arm, the first relevant `0x0F` frame was exact `07E4/17`;
- EXP314 therefore failed closed because direct `07E4` entry was not yet authorized;
- no protocol TX occurred in these attempts;
- parser/resync/drop counters stayed clean and DE remained LOW;
- one later manual "Error gone" button press was accidental and is INVALID for alarm analysis.

**Result:** **COMPLETE / INCONCLUSIVE.**

**Strong passive finding:** controller Online/DCM scheduler state can continue to be retained/progress across ESP restart/OTA such that the ESP reconnects while the controller is already waiting at a later known runtime node (`07E4/17`).

---

# EXP313 — COMPLETE / INCONCLUSIVE — 07D0 handoff works, post-handoff branch exposes 0708

**Date:** 2026-09-30

**Hypothesis:** after adaptive retained-session recovery reaches known runtime `07D0/19`, handing off to the already proven EXP296/297 runtime responder should sustain multiple complete runtime cycles.

**Baseline:** EXP312 COMPLETE / POSITIVE.

**Exact controlled change from EXP312:**
- promote the already-proven retained recovery path into an automatic integrator;
- once exact `07D0/19` is reached, send its already-proven ACK and switch to the full steady-runtime responder;
- no new register target or semantic write.

**Observed:**
- the controller was already at exact `07D0/19`; no recovery prerequisite ACKs were needed;
- one known `07D0` ACK was sent and the handoff flag became active;
- approximately 1.39 s later exact `0708/6` appeared before `07E4/17`;
- EXP313 had allowed only `07E4` at that post-handoff point, so it stopped fail-closed;
- no response was sent to that `0708`;
- transport integrity remained clean and DE returned LOW.

**Result:** **COMPLETE / INCONCLUSIVE.**

**Strong conclusion:** direct retained handoff at `07D0/19` is technically possible, but the immediate next scheduler event is not guaranteed to be `07E4`; an intervening `0708` can occur.

---

# EXP312 — COMPLETE / POSITIVE — 0884 ACK advances retained session to 07D0

**Date:** 2026-09-29

**Hypothesis:** one standard FC16 address/count ACK to a qualified live `0884/60` retry stage advances the retained controller session to the next known runtime stage.

**Baseline:** EXP311 COMPLETE / INCONCLUSIVE.

**Exact controlled change from EXP311:** accept direct `0884/60` as a valid target branch even when neither `0864/4` nor `0870/17` has appeared. Keep all already proven prerequisite ACKs exact-shape gated. The only new active action is one human-gated ACK to `0884/60`: `0F 10 08 84 00 3C 83 7F`.

**Observed:**
- `085F(0800)` repeated twice and received one already-proven standard ACK.
- The controller moved to all-zero `085F/5`; after qualification, one already-proven ACK was sent.
- The runtime then went through `0708` and directly to repeated `0884/60`; `0864` and `0870` were absent.
- `0884` qualified after repeated frames plus fresh `0708`.
- After human arm, exactly one `0884/60` ACK was sent at ~01:36:30.415.
- ~1.325 s later `0708/6` appeared and was intentionally left NO_TX.
- ~1.947 s after the target ACK, known runtime `07D0/19` appeared.
- No `0884` retry occurred before `07D0`.
- Final result counters included `postRetry=0`, `post0708=1`, `postKnown=1`, resync=0, drops=0 and DE LOW.

**Result:** **COMPLETE / POSITIVE.**

**Strong conclusion:** on this XTR M, a single standard ACK to a qualified live `0884/60` stage is sufficient under the tested retained-session conditions to advance through an unanswered `0708` to known runtime `07D0/19`.

---

# EXP311 — COMPLETE / INCONCLUSIVE — direct 0884 branch appears before 0870 prerequisite

**Date:** 2026-09-29

**Hypothesis:** after automatic service of already proven prerequisites through `0870`, a human-gated ACK to repeated `0884/60` should advance to the next runtime stage.

**Baseline:** EXP310 COMPLETE / POSITIVE.

**Controlled change:** `0870/17` became an automatic proven prerequisite; `0884/60` was the new human-gated target.

**Observed:**
- On one valid run, `085F(0800)` and all-zero `085F` prerequisites were ACKed as intended.
- The controller then produced `0884/60` directly, with `0864 Seen=0` and `0870 Seen=0`.
- The experiment failed closed because the state machine still required `0870` before accepting `0884`.
- A later run reproduced the same direct `all-zero 085F ACK -> 0884/60` branch.
- No experimental `0884` ACK was sent.

**Result:** **COMPLETE / INCONCLUSIVE** for the target `0884` ACK hypothesis.

**Strong passive finding:** `0884/60` can occur directly after the all-zero-`085F` stage without `0864` or `0870`. The runtime graph is more branch-like than the EXP311 state machine allowed.

---

# EXP310 — COMPLETE / POSITIVE — 0870 ACK advances to 0884

**Date:** 2026-09-29

**Hypothesis:** one standard FC16 address/count ACK to a qualified live `0870/17` stage advances the controller to another known runtime stage.

**Baseline:** EXP309 COMPLETE / INCONCLUSIVE.

**Controlled change:** accept both the `0864 -> 0870` path and a direct `0870` path; keep `0870` human-gated as the only new target.

**Observed:**
- Proven `085F(0800)` and all-zero `085F` prerequisites were serviced.
- `0870/17` appeared directly; `0864 Seen=0`.
- After human arm, exactly one ACK `0F 10 08 70 00 11 02 90` was sent.
- ~1.47 s later `0708/6` appeared and was left NO_TX.
- ~2.18 s after the ACK, known runtime `0884/60` appeared.
- No `0870` retry preceded `0884`; parser/resync/drop counters remained clean.

**Result:** **COMPLETE / POSITIVE.**

---

# EXP309 — COMPLETE / INCONCLUSIVE — direct 0870 branch disproves mandatory 0864 prerequisite

**Date:** 2026-09-29

**Hypothesis:** automate locally proven retained-session prerequisites through `0864`, then human-gate one `0870/17` ACK.

**Baseline:** EXP308 COMPLETE / POSITIVE.

**Controlled change:** deterministic automation of already proven prerequisite ACKs; no new protocol target except the still-human-gated `0870`.

**Observed:**
- The automatic `085F(0800)` and all-zero `085F` prerequisites worked.
- After the all-zero `085F` ACK, the controller sent direct `0870/17` before any `0864/4`.
- EXP309 correctly failed closed because its state machine still required `0864`.
- No `0870` ACK was sent.

**Result:** **COMPLETE / INCONCLUSIVE** for the target ACK hypothesis.

**Strong passive finding:** `0870/17` does not require a preceding `0864/4` in every retained-runtime branch.

---

# EXP308 — COMPLETE / POSITIVE — 0864 ACK advances to 0870

**Date:** 2026-09-29

**Hypothesis:** after the locally proven EXP307 retained-session chain reaches repeated `0864/4`, one standard ACK to a qualified `0864/4` frame advances the controller to another known runtime stage.

**Baseline:** EXP307 COMPLETE / POSITIVE.

**Controlled change:** keep the EXP307 prerequisites unchanged; human-gate exactly one `0864/4` ACK.

**Observed:**
- EXP307 prerequisites reproduced successfully.
- `0864/4` repeated while waiting for human arm.
- One ACK `0F 10 08 64 00 04 83 5B` was sent.
- ~1.47 s later `0708/6` appeared.
- ~2.09 s after the ACK, known runtime `0870/17` appeared.
- No `0864` retry occurred before `0870`; no parser resync/drop issue; DE LOW at fail-close.

**Result:** **COMPLETE / POSITIVE.**

---

# EXP307 — COMPLETE / POSITIVE — qualified all-zero 085F ACK advances to 0864

**Date:** 2026-09-29

**Hypothesis:** after normalizing the known `085F(0800)` retained retry state, one standard ACK to a freshly qualified all-zero `085F/5` stage advances the controller into the known runtime branch.

**Baseline:** EXP306 COMPLETE / INCONCLUSIVE.

**Controlled change:** keep the already-proven `085F(0800)` normalization as a prerequisite, then separately human-gate exactly one ACK to qualified all-zero `085F/5`.

**Observed:**
- One normalization ACK moved `085F(0800)` to all-zero `085F`.
- After a fresh `0708` and repeated all-zero `085F`, the target qualified.
- One target ACK was sent.
- ~1.48 s later `0708` appeared; ~2.05 s after target ACK, known runtime `0864/4` appeared.
- No post-target `085F` retry preceded `0864`; transport counters remained clean.

**Result:** **COMPLETE / POSITIVE.**

---

# EXP306 — COMPLETE / INCONCLUSIVE — persistent 0708 / 085F(0800) loop with NO_TX

**Date:** 2026-09-29

**Hypothesis:** after optional normalization, repeated all-zero `085F` could be qualified as a target for one bounded ACK.

**Baseline:** EXP305 COMPLETE / POSITIVE.

**Observed:** for ~30 s the retained state remained a persistent `0708 <-> 085F(0800)` loop: 14 nonzero `085F(0800)`, 7 `0708`, zero all-zero `085F`, zero `0662`, TX=0.

**Result:** **COMPLETE / INCONCLUSIVE.** The all-zero target condition never occurred, so the target hypothesis was not tested.

---

# EXP305 — COMPLETE / POSITIVE — 0662/33 ACK-gated transfer re-confirmed

**Date:** 2026-09-29

**Hypothesis:** the resurfaced repeated `0662/33` stage is the same ACK-gated XTR transfer stage already observed in EXP141.

**Baseline:** EXP304 COMPLETE / INCONCLUSIVE.

**Controlled change:** observe at least two exact `0662/33` frames, then ACK exactly the second one with standard address/count ACK `0F 10 06 62 00 21 A0 69`; all later traffic NO_TX.

**Observed:**
- exact `0662/33` repeated twice;
- one ACK was sent;
- no further `0662` retry occurred in the observation window;
- ~71 ms later `085F(0800)` appeared, then `0708`, then all-zero `085F`;
- no parser resync/drop issue; DE LOW;
- the Online/Link alarm cleared temporarily after the ACK but later returned; that alarm timing is correlation only.

**Result:** **COMPLETE / POSITIVE.**

**Strong conclusion:** `0662/33` is locally re-confirmed as an ACK-gated controller-to-DCM transfer stage. The downstream appearance of both nonzero and all-zero `085F` also shows that `0861=0x0800` is a transient session-state discriminator rather than proof that every such frame must receive a direct ACK.

---

# EXP304 — COMPLETE / INCONCLUSIVE — 0662 resurfaced before intended all-zero-085F target

**Date:** 2026-09-29

**Hypothesis:** a repeated all-zero `085F/5` stage may be ACK-gated.

**Baseline:** EXP303 COMPLETE / INCONCLUSIVE.

**Observed:** both arms encountered exact `0662/33` as the first relevant transfer. Because the classifier did not authorize that stage, EXP304 stopped fail-closed with TX=0.

**Result:** **COMPLETE / INCONCLUSIVE.** The all-zero-`085F` hypothesis was not tested. The important finding was the return of the historically known `0662/33` transfer stage.

---

# EXP303 — COMPLETE / INCONCLUSIVE — retained state did not return to 085F(0800)

**Date:** 2026-09-29

**Hypothesis:** reproduce `085F(0800)`, ACK it once, then ACK the first resulting all-zero `085F` once.

**Baseline:** EXP302 COMPLETE / POSITIVE.

**Observed:** the controller remained in the post-EXP302 all-zero state. ESP reboot/OTA did not restore the former `085F(0800)` state. The intended first-stage target therefore never occurred and no ACK was sent.

**Result:** **COMPLETE / INCONCLUSIVE.**

**Strong finding:** controller retained state can persist across ESP restart/OTA; ESP reboot is not a valid rollback assumption.

---

# EXP302 — COMPLETE / POSITIVE — ACK of 085F(0800) changes retained controller state

**Date:** 2026-09-29

**Hypothesis:** one standard FC16 ACK to exact repeated `085F/5` carrying words `0000 0000 0800 0000 0000` changes the stalled retained-session state while `0708` remains NO_TX.

**Baseline:** EXP301 COMPLETE / NEGATIVE.

**Controlled change:** exactly one standard ACK to start `0x085F`, count 5: `0F 10 08 5F 00 05 33 56`. No semantic values injected; `0708` remained NO_TX.

**Observed:**
- exactly one target ACK was sent;
- ~2.44 s later the controller emitted all-zero `085F/5`;
- post-target observations showed repeated all-zero `085F` and `0708`, with no further `085F(0800)` in the observed window;
- parser resync/drop counters remained clean;
- user-marked alarm clear occurred later, but only correlation is claimed.

**Result:** **COMPLETE / POSITIVE.**

**Strong conclusion:** `0861=0x0800` is an ACK-sensitive controller/session state marker under the tested local condition. Its semantic meaning remains unknown.

---

# EXP301 — COMPLETE / NEGATIVE — passive wait for 0848 does not recover retained session

**Date:** 2026-09-29

**Hypothesis:** the retained controller would eventually return to `0848/23`, allowing the earlier normal runtime anchor to be reused.

**Baseline:** EXP300 COMPLETE / INCONCLUSIVE.

**Observed:** repeated `0708` and repeated exact `085F(0800)` occurred, with no `0848` and TX=0.

**Result:** **COMPLETE / NEGATIVE.** Passive wait-for-`0848` is not a viable universal retained-session recovery strategy.

---

# EXP300 — COMPLETE / INCONCLUSIVE — 0848 is not a universal retained re-entry anchor

**Date:** 2026-09-29

**Hypothesis:** after ESP-side session loss, wait passively for `0848/23` and resume the known scheduler from there.

**Baseline:** EXP299 COMPLETE / INCONCLUSIVE.

**Observed:** the first relevant `0x0F` events were instead nonzero `085F(0800)` and/or `0708`; `0848` did not appear in the target window. No TX occurred.

**Result:** **COMPLETE / INCONCLUSIVE.**

---

# EXP299 — COMPLETE / INCONCLUSIVE — bounded retained-session resync reveals temporary liveness recovery

**Date:** 2026-09-29

**Hypothesis:** a bounded retained-session resync using one known runtime anchor can re-establish useful session progress without waiting for a fresh approval.

**Baseline:** EXP298 COMPLETE / INCONCLUSIVE.

**Observed:**
- one `0848/23` ACK was sent;
- a following `0708/6` received the known fixed runtime response;
- the next exact all-zero `085F/5` appeared ~467 ms later;
- TX then stopped fail-closed;
- user-marked Online/Link alarm clearing occurred ~4.5 s after arm, but the alarm was visible again about 135.6 s later.

**Result:** **COMPLETE / INCONCLUSIVE.**

**Strong conclusion:** bounded known-stage service can move a retained session and may temporarily affect visible health, but one/few responses are insufficient evidence of durable recovery.

---

# EXP298 — COMPLETE / INCONCLUSIVE — fresh-approval-only ESP reboot recovery insufficient

**Date:** 2026-09-29

## PREPARED scope retained from the original experiment

**Hypothesis:** after the ESP/DCM emulator restarts while the Thermia controller remains powered, the controller eventually presents a fresh exact `071C/0730` approval request that allows the emulator to rebuild the same proven session without requiring a Thermia-controller reboot.

**Baseline:** EXP297 COMPLETE / POSITIVE.

**Exact controlled change from EXP297:**
- the Thermia controller was deliberately **not** rebooted;
- after ESP return, EXP298 waited passively for a fresh exact `071C/0730`;
- no TX was authorized before such an approval request;
- the intended approval wait was bounded to 240 s;
- if approval arrived, the existing fixed R1, ordered 32-page config sync, startup `085F/5`, startup `0708/6` and proven runtime graph were to be reused unchanged;
- runtime `04A6/13` remained capture-only / NO_TX;
- no semantic write.

## RESULT

**Observed:**
- after ESP restart, retained `0708` and `0848` traffic was present;
- no fresh `071C/0730` approval request appeared in the supplied observation window of approximately 235.7 s;
- no protocol TX occurred;
- COMM. ERR ONLINE/LINK was visible.

The original strict 240 s negative threshold was not fully reached, so the result cannot be labeled a strict negative.

**Result:** **COMPLETE / INCONCLUSIVE.**

**Strong conclusion:** fresh-approval-only recovery is insufficient as the sole ESP-restart strategy under the tested retained-session condition. The controller can remain in an existing/recovery scheduler state rather than immediately reopen approval.

---


# EXP297 — COMPLETE / POSITIVE — active controller reboot recovered without ESP reboot/re-arm

**Date:** 2026-09-29

**Hypothesis:** after normal runtime has been established, reboot only the Thermia controller while leaving the ESP/DCM emulator active. The emulator should detect the bus interruption, reset only session-local state, accept a fresh approval exchange, rerun startup synchronization and return to runtime without manual re-arm.

**Baseline:** EXP296 COMPLETE / POSITIVE.

**Controlled change from EXP296:**
- no new Modbus payload or register;
- no new FC16 ACK target;
- no semantic write;
- runtime `04A6/13` remains capture-only / NO_TX;
- add only controller-reboot recovery state handling after a >=5 s bus gap during active runtime.

**Observed:**
- normal startup/runtime completed before the target reboot, reaching runtime cycle 5;
- target controller reboot produced a ~14.796 s bus gap;
- EXP297 emitted `CONTROLLER_REBOOT_RECOVERY_START` and cleared the current runtime/config/cache state;
- bus returned while the ESP remained online;
- a fresh exact `071C/0730` challenge arrived;
- the same fixed historical R1 replay was transmitted;
- all 32 configuration pages were again received and ACKed in order;
- startup all-zero `085F/5` was ACKed;
- startup `0708/6` was answered;
- runtime re-entered at `07D0/19`;
- the capture then completed cycles 6, 7 and 8;
- no `ABORT_FAIL_CLOSED`;
- parser resyncs remained 0;
- RX buffer drops remained 0.

**Result:** **COMPLETE / POSITIVE.**

**Strong conclusion:** on this XTR M, the current DCM emulator can recover from a Thermia-controller reboot and establish a fresh native session without rebooting or manually re-arming the ESP. The fixed historical R1 replay also remained accepted for the fresh post-reboot challenge.

---

# EXP296 — COMPLETE / POSITIVE — direct post-080C 0820 branch survives real operation-state changes

**Date:** 2026-09-29

**Hypothesis:** after EXP295 locally observed `080C/18 -> direct 0820/18`, allow exactly that additional branch while preserving all prior proven runtime handling. Runtime `04A6/13` remains capture-only / NO_TX.

**Baseline:** EXP295 COMPLETE / INCONCLUSIVE overall, with positive target result for `07E4 -> direct 07F8`.

**Controlled change from EXP295:** after valid `080C/18` ACK, allow either:
- `FC03 0708/6 -> existing runtime 0708 response -> 0820/18`, or
- direct `FC16 0820/18` using the existing proven address/count ACK.

No other protocol response was changed. No semantic write. Runtime `04A6/13` remained NO_TX.

**Observed:**
- normal startup/approval/config sync completed and steady-state began;
- first `DIRECT_POST_080C_0820_ACCEPTED` occurred at steady-state age ~94 s;
- the direct branch was accepted repeatedly, reaching count **11** in the supplied capture;
- `DIRECT_POST_07E4_07F8_ACCEPTED` also repeated, reaching count **12** near the end;
- `DIRECT_POST_0884_07D0_ACCEPTED` reached count **11**;
- runtime reached at least **16 cycles** and **159 serviced runtime events**;
- steady-state service age reached ~**329.8 s**;
- no `ABORT_FAIL_CLOSED` occurred in the supplied capture;
- RX buffer drops remained 0;
- parser resync count remained at the single controller-BUS_RETURN resync established before steady-state.

Operational transitions survived during the active session:
- user reported **Blocked -> Normal -> Enhanced -> Normal** SG progression;
- the log explicitly records Normal -> Enhanced -> Normal;
- controller context changed to `A80C=0041` and the current local decoder reported **DHW / high temperature**;
- `DHW Active` became ON and the compressor started;
- runtime continued afterwards without fail-closed termination.

Runtime `04A6/13` remained unanswered throughout:
- capture count reached **225**;
- payload-change count reached **2**;
- one change coincided with entry into the DHW/high-temperature context and a later change with return from that context;
- normal runtime progression continued while these frames were ignored.

**Supplementary later EXP296 capture (same experiment, later evidence):**
- steady-state service exceeded ~32 minutes;
- a near-complete SWW cycle was observed through DHW active, temperature rise, DHW end and compressor stop;
- a later `SG Mode = Blocked (1-0)` transition was survived;
- runtime `04A6/13` remained NO_TX and reached at least 1696 captures;
- its payload-change counter reached 3;
- shortly after the Blocked transition, `04A6` changed to a form beginning `0042 0001 ...`;
- runtime continued through the proven graph without fail-close, parser-resync growth or RX drops.

This supplementary evidence strengthens the state-dependent `04A6` hypothesis but does not prove that `0042` uniquely means SG Blocked.

**Run-criterion note:** the original plan requested five minutes after the first direct post-080C marker. The supplied capture contains about 235 s after the first marker, not a literal five minutes. The user explicitly confirmed EXP296 as **COMPLETE / POSITIVE** after reviewing that the target branch repeated many times and multiple operation-state changes were survived.

**Result:** **COMPLETE / POSITIVE.**

**Strong conclusion:** `080C -> [optional 0708] -> 0820` is locally confirmed. Together with EXP294/295, the runtime is demonstrably state/branch driven rather than one fixed sequence.

---

# EXP295 — COMPLETE / INCONCLUSIVE — direct post-07E4 07F8 accepted; next missing branch is direct post-080C 0820

**Date:** 2026-09-29

**Hypothesis:** during an operation-state transition, the `0708/6` mailbox after `07E4/17` can be omitted and `07F8/17` may follow directly.

**Baseline:** EXP294 COMPLETE / INCONCLUSIVE overall, with positive target result for direct post-`0884` `07D0`.

**Controlled change from EXP294:** after `07E4/17` ACK, allow either `0708/6` or direct `07F8/17`. Runtime `04A6/13` remained capture-only / NO_TX.

**Observed:**
- `0884 -> direct 07D0` was again accepted successfully;
- `07E4 -> direct 07F8` occurred and was accepted with `DIRECT_POST_07E4_07F8_ACCEPTED n=1`;
- `080C/18` then arrived and was ACKed normally;
- instead of the then-required `0708/6`, the controller sent direct `0820/18`;
- firmware stopped fail-closed on that newly observed branch;
- runtime `04A6/13` continued to repeat unchanged before the stop.

**Result:** **COMPLETE / INCONCLUSIVE overall**, with a **positive target result** proving `07E4 -> [optional 0708] -> 07F8` locally.

---

# EXP294 — COMPLETE / INCONCLUSIVE — direct post-0884 07D0 accepted; next missing branch is direct post-07E4 07F8

**Date:** 2026-09-29

**Hypothesis:** during an operation-state transition, the final `0708/6` after `0884/60` can be omitted and the controller may return directly to `07D0/19`.

**Baseline:** EXP293 COMPLETE / POSITIVE for stable steady-state operation.

**Controlled change from EXP293:** after `0884/60` ACK, allow either `0708/6 -> 07D0/19` or direct `07D0/19`. Runtime `04A6/13` remained capture-only / NO_TX.

**Observed:**
- transition-related runtime `04A6/13` began repeating;
- `0884 -> direct 07D0` occurred and was successfully accepted/ACKed;
- runtime advanced to `07E4/17`;
- controller then sent direct `07F8/17` without the then-required `0708/6`;
- firmware stopped fail-closed on that newly observed branch.

**Result:** **COMPLETE / INCONCLUSIVE overall**, with a **positive target result** proving `0884 -> [optional 0708] -> 07D0` locally.

---

# EXP293 — COMPLETE / POSITIVE — continuous steady-state runtime remains alarm-free for ~30 minutes

**Date:** 2026-09-29

**Hypothesis:** if the known-good startup/runtime responder continues indefinitely instead of deliberately stopping after ~4 minutes, the Online/Link communication alarm should remain absent during stable operation.

**Baseline:** EXP292 COMPLETE / POSITIVE.

**Controlled change from EXP292:** remove the automatic clean stop/RX-only phase and continue the already proven runtime graph indefinitely. No protocol payload/register change and no semantic write.

**Observed:**
- startup and runtime entered normally;
- the 15-minute marker was reached at ~900.1 s with 43 cycles, 590 runtime events, 625 TX, 0 unexpected events and clean experimental parser/drop deltas;
- the supplied log continued to roughly 30 minutes of steady-state service, reaching at least 84 cycles;
- known conditional branches, including optional post-`0870` `0708`, were serviced;
- no fail-closed termination was present in the captured steady-state run;
- user explicitly confirmed **no `COMM. ERR ONLINE/LINK` alarm** during that run.

A later operation-state-change observation showed that this result must not be generalized to all state transitions: the then-current rigid handler could still fail when the controller omitted additional `0708` mailbox positions.

**Result:** **COMPLETE / POSITIVE for stable steady-state scope.**

---

# EXP292 — COMPLETE / POSITIVE — optional post-0870 0708 branch locally supported

**Date:** 2026-09-29

**Hypothesis:** after `0870/17` ACK, accept either direct `0884/60` or an intervening `FC03 0708/6`, matching genuine XTR/DCM capture evidence.

**Baseline:** EXP291 COMPLETE / INCONCLUSIVE.

**Controlled change from EXP291:** add only the evidence-backed post-`0870` optional `0708/6` branch. No semantic writes; reverse `03E8` remained disabled/capture-only.

**Observed:**
- startup and full runtime completed normally;
- the post-`0870` `0708` branch was exercised locally and serviced;
- continuous service lasted **256.276 s**;
- final counters: **12 cycles**, **169 runtime events**, **204 TX**, **0 unexpected events**;
- experimental resync/drop deltas remained 0;
- TX then stopped deliberately at a clean loop boundary and controller traffic continued RX-only for ~180 s;
- user reported the exact Online/Link communication error appeared shortly after the deliberate stop, with exact delay not precisely timed.

**Result:** **COMPLETE / POSITIVE.**

---

# EXP291 — COMPLETE / INCONCLUSIVE — strict continuity run exposes optional post-0870 mailbox branch

**Date:** 2026-09-29

**Hypothesis:** with semantic writes disabled and only the then-known runtime paths serviced, continuous known-good runtime should remain active long enough to compare alarm behavior before and after a deliberate stop.

**Baseline:** EXP290 COMPLETE / POSITIVE for the separate reverse-page semantic write path; continuity test itself used no semantic write.

**Controlled change:** strict runtime state machine, no `0708 w1=1`, no reverse `03E8` page, no setting change. Planned ~4 minutes active service followed by clean stop and RX-only observation.

**Observed:**
- startup and first full runtime cycle succeeded;
- second cycle progressed through `0848 -> 0708 -> direct 0864 -> direct 0870`;
- after `0870`, controller emitted `FC03 0708/6`;
- handler at that point allowed only `0884`, so it intentionally failed closed after ~38 s of steady-state service;
- genuine XTR/DCM capture evidence independently contains `0870 ACK -> FC03 0708 -> runtime response -> 0884`.

**Result:** **COMPLETE / INCONCLUSIVE.** The intended alarm discriminator was not completed, but the run exposed a valid runtime branch needed by the emulator.

---

# EXP290 — COMPLETE / POSITIVE — reverse 03E8 semantic write changes controller-visible Room Setpoint

**Date:** 2026-09-29

**Hypothesis:** after EXP289 proved acceptance of an unchanged reverse `03E8/14` page, changing only locally mapped `03F4` by +1 in the same-session cached page should be semantically applied by the controller.

**Baseline:** EXP289 COMPLETE / POSITIVE.

**Controlled change:** only `03F4` changed, from current-session cached raw value `22` to `23`. All other 13 words were unchanged. Safety gate required original 15..24 and compressor stopped.

**Observed:**
- current-session `03E8/14` cache captured before the write;
- post-`07E4` `0708/6` answered with `w1=0001`;
- `FC03 03E8/14` arrived 98 ms later;
- reverse page response sent with only `03F4 22->23`;
- first next FC16 was normal runtime `07F8/17` 680 ms later;
- about two seconds later the live `Room Setpoint` sensor reported `23 °C`;
- RX buffer drops remained 0;
- one parser resync occurred at controller bus return before the active transfer.

**Result:** COMPLETE / POSITIVE for controller-visible semantic application. The experiment did not capture an authoritative `FC16 03E8/14` target echo, so that narrower confirmation remains OPEN.

**Do not rewrite this as full round-trip proof:** transport + semantic application are locally demonstrated; authoritative FC16 echo and independent room-sensor-path confirmation are still pending.

---

# EXP289 — COMPLETE / POSITIVE — unchanged reverse 03E8/14 page accepted

**Date:** 2026-09-29

**Hypothesis:** after the EXP288-proven reverse pull, return the exact current-session cached `03E8/14` page unchanged and test whether the controller accepts it.

**Controlled change from EXP288:** respond once to exact `FC03 03E8/14` with the same 28 payload bytes previously captured from the session's own `FC16 03E8/14`.

**Observed:**
- `0708 w1=0001` again caused `FC03 03E8/14` after 98 ms;
- exact unchanged current-session page was returned once;
- controller continued with `FC16 07F8/17` 680 ms later;
- no immediate retry/reject flow.

**Result:** COMPLETE / POSITIVE. Reverse-page response transport acceptance is locally proven.

---

# EXP288 — COMPLETE / POSITIVE — 0708 w1 bit0 triggers local reverse 03E8 pull

**Date:** 2026-09-29

**Hypothesis:** change only post-`07E4` 0708 `w1` from `0000` to `0001`; controller should request heating/settings page `03E8`.

**Controlled change from EXP287:** response changed from `0000 0000 0000 0000 0000 0006` to `0000 0001 0000 0000 0000 0006`.

**Observed:** 98–99 ms after the probe response, local controller sent `FC03 03E8/count14`. Firmware's original matcher expected count13 from genuine capture evidence and therefore labelled the run inconclusive, but the protocol observation itself is positive and locally specific: this XTR uses count14.

**Result:** COMPLETE / POSITIVE for the core hypothesis. `0708 w1 bit0` locally triggers reverse `03E8/14`.

---

# EXP287 — COMPLETE / INCONCLUSIVE — direct 0870 after 0864 exposes second conditional runtime branch

**Date:** 2026-09-29

**Hypothesis:** after cycle-2 `0848 -> 0708`, accept either optional `085F/5 -> ACK -> 0864/4` or direct `0864/4`, then continue the previously assumed `0864 -> 0708 -> 0870` tail.

**Observed:** direct `0864/4` was accepted and ACKed, but controller then emitted direct `0870/17` without the expected intervening `0708`. Firmware stopped fail-closed.

**Result:** COMPLETE / INCONCLUSIVE overall; positive sub-result that direct 0864 branch is valid. Strong conclusion: post-`0864` 0708 is conditional/state-dependent.

---

# THERMIA EXPERIMENT LOG

# 2026-09-29 — EXP286 COMPLETE / INCONCLUSIVE — second full runtime loop hits direct 0864 branch
## Hypothesis
Continue the entire second runtime cycle using only already locally proven actions, then capture the next returned `07D0/19`.

## Controlled change
Relative to EXP285, continue after the already proven cycle-2 `07F8` using the locally proven sequence through the rest of the runtime tail. No new register address, mailbox payload, or semantic write was introduced.

## Observed facts
- Cycle 2 progressed cleanly through `07F8 ACK -> 080C ACK -> 0708 response -> 0820 ACK -> 0848 ACK -> 0708 response`.
- The next controller-originated FC16 was `0864/count4`, not `085F/count5`.
- Firmware stopped fail-closed because EXP286 explicitly required the 085F gate.
- No ACK was sent to that direct `0864`.
- RX drops and parser resyncs remained zero around the test.

## Conclusion
**COMPLETE / INCONCLUSIVE for the exact EXP286 hypothesis.** The failure was not a bus/protocol collapse; it revealed a valid conditional branch. `085F` is not mandatory in every runtime cycle.

---

# 2026-09-29 — EXP285 COMPLETE / POSITIVE — steady-state loop restarts without new approval
## Hypothesis
After the EXP284 loop closure, ACK returned `07D0`, ACK `07E4`, answer the second-cycle `0708`, then capture the next FC03/FC16.

## Observed facts
- `0884 ACK -> 0708 response -> returned 07D0/19`.
- Returned `07D0` ACKed once.
- `07E4/17` followed and was ACKed once.
- Second-cycle `0708/6` was answered with the already proven `0000 ... 0006` response.
- `07F8/17` appeared 616 ms later and was captured.
- No second approval/R1 sequence occurred.
- RX drops and parser resyncs remained zero.

## Conclusion
**COMPLETE / POSITIVE.** The Online/DCM-style runtime sequence re-enters a new cycle without a new approval exchange.

---

# 2026-09-29 — EXP284 COMPLETE / POSITIVE — first runtime loop closes back to 07D0
## Hypothesis
After the proven `0884 ACK -> 0708/6`, answer that 0708 once with the locally proven `0000 ... 0006` response and capture the first next 0x0F FC03/FC16.

## Observed facts
- `0884/60` was valid and ACKed.
- Post-0884 `0708/6` was answered once with `0F030C0000000000000000000000069D76`.
- 571 ms later exact `07D0/count19` appeared.
- `07D0` was capture-only and not ACKed.
- Parser resync and RX-drop counters remained zero.

## Conclusion
**COMPLETE / POSITIVE.** The local runtime tail closes from `0884 -> 0708 -> 07D0`, establishing a complete loop.

---

# 2026-09-29 — EXP283 COMPLETE / POSITIVE — 0884 ACK proven locally
## Hypothesis
Instrument and repair the EXP282 0884 matcher; if exact `0884/count60` has a valid FC16 shape, ACK it once and capture the next `0708/6`.

## Observed facts
- `0884`: start 0884, count 60, bytecount 120, total frame length 129, valid/self-consistent.
- ACK `0F100884003C837F` was transmitted once.
- 1429 ms later exact `FC03 0708/count6` appeared.
- That 0708 was capture-only.

## Conclusion
**COMPLETE / POSITIVE.** `0884/60 ACK -> 0708/6` is locally confirmed.

---

# 2026-09-29 — EXP282 COMPLETE / INCONCLUSIVE — reached 0884 but handler did not ACK
## Observed facts
The local chain reached `0864 ACK -> 0708 response -> 0870/17 ACK -> 0884/60`, but the specialized EXP282 0884 ACK path did not execute. The later 0708 caused fail-closed termination.

## Conclusion
**COMPLETE / INCONCLUSIVE.** Protocol progression to 0884 was positive; the missing ACK was a firmware control-flow/instrumentation problem, not a demonstrated protocol rejection.

---

# 2026-09-29 — EXP281 COMPLETE / INCONCLUSIVE — historical direct-0870 expectation corrected later
## Observed facts
- Preserved path through post-0848 `085F ACK -> 0864/4`.
- ACKed exact `0864/4` once.
- First subsequent 0x0F FC03/FC16 was `FC03 0708/count6`, not the then-expected direct `0870`.
- No response was sent; clean fail-closed stop.

## Historical result and current interpretation
**COMPLETE / INCONCLUSIVE** remains the historical experiment status. Later genuine-capture reanalysis established that `0864 ACK -> 0708 -> 0870` is a valid native ordering, so the observed 0708 is no longer considered evidence of divergence.

---

# 2026-09-29 — EXP280 COMPLETE / POSITIVE — second 085F ACK advances to 0864
- Post-0848 `0708/6` received the proven `0000 ... 0006` response.
- Exact `085F/count5` was ACKed once.
- `0864/count4` appeared ~2.06 s later and was captured without ACK.
**Conclusion:** COMPLETE / POSITIVE.

---

# 2026-09-29 — EXP279 COMPLETE / INCONCLUSIVE — post-0848 response reveals 085F
- Post-0848 `0708/6` was answered once with the locally proven `0000 ... 0006` response.
- Next FC16 was `085F/count5`; payload ended in `0032`, so it was not the earlier all-zero 085F form.
- It was not ACKed.
**Conclusion:** COMPLETE / INCONCLUSIVE; established another 085F stage but not its required handling.

---

# 2026-09-29 — EXP278 COMPLETE / POSITIVE — 0848 ACK advances to post-0848 0708
- Preserved chain through `0820 ACK`.
- ACKed exact local `0848/count23`.
- Exact `FC03 0708/count6` appeared ~1.43 s later and was capture-only.
**Conclusion:** COMPLETE / POSITIVE.

---

# 2026-09-29 — EXP277 COMPLETE / INCONCLUSIVE — local branch is 0848, not expected 0834
- Fixed EXP276 phase-gate bug.
- `post-080C 0708 response -> 0820/18 ACK`.
- Next local FC16 was `0848/count23`, not expected `0834`.
- `0848` was capture-only.
**Conclusion:** COMPLETE / INCONCLUSIVE. The local XTR branch skips 0834 in this observed path.

---

# 2026-09-29 — EXP276 RUNNING / PARTIAL then COMPLETE / INCONCLUSIVE — phase-gate bug
- Post-080C `0708` response successfully caused `0820/18` to appear.
- Intended 0820 ACK code was unreachable because the outer phase gate omitted the new phases.
- Repeated 0820 and later 0708 were observed; parser resyncs occurred around bus return.
**Conclusion:** protocol hint positive, experiment control invalid for the intended ACK test.

---

# 2026-09-29 — EXP275 COMPLETE / POSITIVE — 080C ACK unlocks 0708
- ACKed exact `080C/count18` once.
- Exact `FC03 0708/count6` followed and was captured.
**Conclusion:** COMPLETE / POSITIVE.

---

# 2026-09-29 — EXP274 COMPLETE / POSITIVE — 07F8 ACK unlocks 080C
- ACKed exact `07F8/count17` once.
- `080C/count18` followed and was captured.
**Conclusion:** COMPLETE / POSITIVE.

---

# 2026-09-29 — EXP273 COMPLETE / POSITIVE — post-07E4 0708 response unlocks 07F8
- Answered exact post-07E4 `FC03 0708/count6` once with `0F030C0000000000000000000000069D76`.
- `07F8/count17` followed and was captured without ACK.
**Conclusion:** COMPLETE / POSITIVE.

---

# 2026-09-29 — EXP272 COMPLETE / POSITIVE — 07E4 ACK unlocks post-07E4 0708

## Hypothesis
After EXP271 locally proved `07D0/count19 -> ACK -> 07E4/count17`, a single exact standard ACK of the first `07E4/count17` should advance the XTR M to the next native mailbox request `FC03 0708/count6`.

## Controlled variable
Relative to EXP271, the entire proven path was preserved. The only new active action was one exact ACK of the first `07E4/count17` with:

`0F1007E400114068`.

The following mailbox request was capture-only. No post-`07E4` 0708 response and no later runtime-page ACK were allowed.

## Timeline / observed facts
- BUS_GAP and BUS_RETURN detected normally.
- New local approval challenge:
  `1A094566F90619ACDC1DC5A0001E8FCC`.
- Same fixed historical R1 replay sent:
  `0F17101691A5F3F8E8D58738924416E8E6A3D5E227`.
- Full known FC16 sync reproduced cleanly through `06F4/19`.
- First exact all-zero `085F/count5` was ACKed once with `0F10085F00053356`.
- First early `0708/count6` was answered once with the preserved phase-matched `0080/0006` response.
- `07D0/count19` appeared and was ACKed once with `0F1007D000138067`.
- `07E4/count17` appeared ~2.08 s later.
- EXP272 ACKed `07E4/count17` exactly once with `0F1007E400114068`.
- Exact `FC03 0708/count6` appeared 1457 ms after the 07E4 ACK.
- Firmware logged `SUCCESS_0708_AFTER_07E4_ACK`.
- The post-07E4 0708 request was deliberately not answered.
- Parser resyncs and RX buffer drops remained zero.

## Comparison with EXP271
EXP271 stopped capture-only on `07E4/17`. EXP272 preserved every preceding action and added only one exact 07E4 ACK. The controller then advanced to the next 0708 mailbox poll.

## Strong conclusion
**EXP272 is positive. `07E4/count17` is locally confirmed on the XTR M as an ordered runtime gate whose ACK advances the session to a post-07E4 `FC03 0708/count6` request.**

## Limits
- This does not prove the correct response payload for the post-07E4 0708 poll.
- This does not yet prove progression to `07F8/count17`.
- No semantic desired-state page was served or written.

## Next
EXP273 should change one variable only: answer the proven post-07E4 `0708/count6` once with the exact phase-matched genuine response `0000 0000 0000 0000 0000 0006` / raw `0F030C0000000000000000000000069D76`, then capture `07F8/count17` without ACK.

---

# 2026-09-29 — EXP271 COMPLETE / POSITIVE — 07D0 ACK unlocks 07E4

## Hypothesis
After EXP270 proved the path to first `07D0/count19`, ACKing that exact page once should advance the XTR M to `07E4/count17`.

## Controlled variable
Relative to EXP270, all earlier R1/sync/`085F`/early-`0708` behavior was retained. The only new active action was one exact standard ACK of the first `07D0/count19`:

`0F1007D000138067`.

`07E4/count17` remained capture-only.

## Timeline / observed facts
- BUS_GAP and BUS_RETURN detected normally.
- New local approval challenge:
  `1A094552F90614ACDC1DC594001E8FA4`.
- Same fixed historical R1 replay sent.
- Full known synchronization chain through `06F4/19` completed.
- exact all-zero `085F/count5` was ACKed once.
- early `0708/count6` received the same single preserved `0080/0006` response.
- first `07D0/count19` appeared and was ACKed once with `0F1007D000138067`.
- exact `07E4/count17` appeared 2159 ms after the 07D0 ACK.
- firmware logged `SUCCESS_07E4_AFTER_07D0_ACK`.
- `07E4` was deliberately not ACKed.
- parser resyncs and RX buffer drops remained zero.

## Comparison with EXP270
EXP270 stopped on first `07D0/19` without ACK. EXP271 preserved the complete EXP270 path and added only one exact 07D0 ACK; `07E4/17` then appeared.

## Strong conclusion
**EXP271 is positive. `07D0/count19` is locally confirmed as an ordered runtime gate whose ACK advances the XTR M to `07E4/count17`.**

## Limits
No conclusion is made here about the semantics or payload of 07D0/07E4. Standard FC16 ACKs contain only slave/function/start/count and do not inject the controller-originated page values.

---
# 2026-09-29 — EXP270 COMPLETE / POSITIVE — exact 085F ACK unlocks 07D0

## Hypothesis
The pending exact all-zero `FC16 085F/count5` after the initial synchronization is an ordered gate. ACKing it once should allow the XTR M to continue from the proven `06F4` tail into the first runtime page `07D0/count19`.

## Controlled variable
EXP270 intentionally preserved the EXP269 fixed replay and post-`06F4` mailbox behavior. The only material new active action was a one-shot standard ACK of the first exact all-zero `085F/5`.

## Timeline / observed facts
- BUS_GAP and BUS_RETURN detected normally.
- New local approval challenge:
  `1A004508F90602ACDC1DC5CC001E8F10`.
- The same fixed R1 replay used in prior experiments was sent:
  `0F17101691A5F3F8E8D58738924416E8E6A3D5E227`.
- The complete known FC16 prefix proceeded successfully:
  `03E8 -> 03FC -> 0410 -> 042E -> 0442 -> 0456 -> 046A -> 047E -> 0492 -> 04A6 -> 04BA -> 04D8 -> 04F6 -> 050A -> 051E -> 0532 -> 0546 -> 055A -> 057B -> 059C -> 05BD -> 05DE -> 05FF -> 0620 -> 0641 -> 0662 -> 0683 -> 06A4 -> 06C5 -> 06EA -> 06F1 -> 06F4`.
- `06F4` ACK executed at 00:48:06.727.
- exact all-zero `085F/count5` arrived immediately afterwards and was ACKed exactly once with `0F10085F00053356`.
- first `0708/count6` then arrived; EXP270 returned the same single EXP269 response:
  `0F030C0000000000000000008000069C9E`.
- first `07D0/count19` arrived 509 ms later.
- firmware logged `SUCCESS_07D0_AFTER_085F_ACK`.
- `07D0` was deliberately not ACKed.
- no broad writes/scans were performed.

## Comparison with EXP269
EXP269 used the same single `0080/0006` mailbox response but deliberately ignored the post-`06F4` `085F/5`; no `07D0` followed. EXP270 retained that mailbox response and added one exact 085F ACK; `07D0` appeared.

## Strong conclusion
**EXP270 is positive. The exact all-zero 085F/5 is locally confirmed as an ordered XTR M gate required for progression to the first runtime page.**

## Additional finding
The current 071C challenge differed from the historical challenge corresponding to the replayed R1 frame, yet the controller accepted enough of the session to complete the initial config export and reach `07D0`. Fixed 0730 replay is therefore sufficient at least through this stage; genuine challenge-response semantics remain unresolved.

## Negative/limited findings
- EXP270 does not prove that `0080/0006` is the correct genuine cold-start mailbox state; genuine Eco5 evidence also shows `0100/0000` in this phase.
- EXP270 does not prove full Online/Link session completion or steady-state operation.
- No runtime page beyond `07D0` was tested because 07D0 was intentionally left unACKed.

## Next
EXP271 should change one variable only: ACK first exact `07D0/19` once, then capture first `07E4/17` without ACK.

---

## 2026-09-28 — offline architecture analysis before EXP270

Cross-capture comparison found a likely reverse-direction settings mechanism on slave 0x0F. In the 20260924 genuine DCM capture, the only two shown `0708/count6` replies with word1=`0001` are followed ~39–41 ms later by controller `FC03 03E8/count13` reads. The DCM returns a complete settings page; between the two events only the first word changes `0017 -> 0016`. A separate genuine DCM capture shows the same 13-word page image being written controller -> DCM via `FC16 03E8/count13`.

Interpretation: FC16 likely synchronizes authoritative/current pages controller -> gateway, while FC03 can fetch desired/config pages gateway -> controller. Word1 of 0708 is a strong candidate pending-page/desired-data signal for the 03E8 family. Application semantics remain unproven locally.

## EXP270 — PREPARED / NOT RUN — exact all-zero 085F ACK gate

**Hypothesis:** first `07D0/count19` is blocked locally because exact all-zero `085F/count5` after `06F4` was wrongly ignored in EXP268/269.

Controlled change from EXP269:
- ACK the first exact all-zero `085F/count5` once using `0F10085F00053356`.
- Keep the entire proven pre-06F4 sequence unchanged.
- If 0708 occurs after that ACK before 07D0, use the same single EXP269 `0080/0006` response once only.
- Capture first `07D0/count19` without ACK and terminate.

Negative criteria are also explicit: 0708 before the 085F gate, non-zero 085F payload, 085F ACK safety refusal, repeated 085F without 07D0, timeout after 085F ACK, or 30 s RX-only after the preserved mailbox response with no 07D0.

## 2026-09-28 — deeper full-log analysis of second Eco5 capture

Four power cycles were parsed. Successful challenge replies occurred either around +10 s (request #3) or around +120 s (request #29), but first 03E8 ACK always began around +118.5..120.3 s after bus return. The fast-approval sessions contained 102 repeated unacked 03E8 frames over ~108 s before normal FC16 service began.

085F is now the strongest immediate local clue. In the two sessions where it was still pending after 06F4:
- S2: 06F4 ACK 590.919 -> 085F ACK 590.996 -> 0708 idle 592.311 -> 07D0 592.930.
- S3: 06F4 ACK 888.765 -> 085F ACK 889.309 -> 0708 idle 892.978 -> 07D0 893.603.

In sessions where 085F had already been ACKed shortly before approval, 07D0 followed 06F4 directly in ~78 ms.

Mailbox raw-word correction: the normal idle response is 0000 0000 0000 0000 **0100** 0000. After initial idle replies, the stable script proceeds through 4000/8000/010B and then FFFF/867F/03DF. The 03DF response triggers a new 03E8 within 62–94 ms in all four sessions.

Likely EXP270: reuse EXP268, change only exact 085F/5 handling from ignore to ACK once, retain normal idle 0708 behavior, capture 07D0 without ACK.

## 2026-09-28 — peer analysis of second Eco5 capture

Material new evidence:
- `085F/5` is likely ordered session traffic, not background chatter; in observed successful transitions it is ACKed before first `07D0`.
- If `085F` is already ACKed earlier, `07D0` can follow `06F4` almost immediately; if pending, controller emits `085F` after `06F4`, waits for ACK, then emits `07D0`.
- Post-first-sync mailbox script appears identical across five complete Eco5 sessions, ending in `FFFF 867F 03DF 0000`, which is followed by a second full sync.
- Challenge approval timing and first FC16 ACK timing are decoupled; first FC16 ACK appears ~118 s after bus return in all cited sessions even when challenge approval occurs much earlier.
- Six challenge/response pairs now available; no simple XOR/difference relation identified.

Next experimental focus should be the `085F` queue prerequisite before any further mailbox-payload exploration.

## 2026-09-28 — external Eco5 capture review (no new local experiment)

Major result from new genuine Eco5 gateway capture:
- successful dynamic `071C/0730` response is followed by `03E8 -> ... -> 06F4`;
- `07D0/19` follows `06F4/19` directly (~78 ms) before the next `0708/6` mailbox poll;
- therefore EXP269 tested the wrong causal hypothesis: mailbox payload `0080/0006` is not required to unlock the first `07D0` in this successful session;
- later `0708/6` idle replies (`0001/0000`) are interleaved with `07E4, 07F8, 080C, 0820, 0834, 0848, 0864, 0870, 0884`.

The capture also provides four distinct successful `071C` challenge -> 16-byte response pairs. Responses differ with the challenge, strongly supporting a dynamic challenge-response mechanism.

Project implication: next work should target the approval/session mechanism rather than additional mailbox-payload variants.

### EXP269 UI observation
Post-test display photo confirms a visible change in the lower-right status area: user reports the center of the `0`/status glyph is now filled. Alarm remains active. Treat as a UI/state side effect only; semantic meaning unknown and not evidence of successful Online session completion.

## EXP269 — COMPLETE / NEGATIVE

Hypothesis: one exact Eco5 phase-matched first post-`06F4` mailbox response `0000 0000 0000 0000 0080 0006` would cause the XTR to continue with `07D0/19`.

Observed:
- proven prefix through `06F4/19` completed cleanly;
- first `0708/6` at +1.566 s;
- one exact `0080/0006` response sent;
- no `07D0/19`;
- repeated `0708/6` began ~4.43 s later and continued;
- 30 s RX-only completed;
- summary: `responses_sent=1 mailbox_requests=8 ignored_bg=15 resync_postreturn=0 drop_postreturn=0 DE=LOW`;
- only recurrent post-`06F4` FC16 family was `085F/5`;
- A80E moved `0008 -> 0028`, AFDC to `32`;
- user reports a visible UI change (“middle of the 0 is now filled”), semantic meaning unknown.

Conclusion: valid negative. The phase-matched Eco5 `0080/0006` response is not sufficient on its own to reproduce the Eco5 `07D0` transition.

---
## EXP269 — PREPARED / NOT RUN — revised phase-matched mailbox test

Hypothesis: the first post-`06F4` XTR mailbox must receive the same phase-specific payload seen in the matching Eco5 startup trace.

Sequence: proven approval/sync prefix through `06F4/19` -> first exact `0708/6` -> send exactly once `0F030C0000000000000000008000069C9E` (words `0000 0000 0000 0000 0080 0006`) -> RX-only up to 30 s.

Primary success criterion: capture `07D0/19`, with no ACK. Repeated `0708/6` is a negative/non-progress signal and receives no second response. No other new active traffic is introduced.

The earlier EXP269 design using up to ten `0001/0000` replies remains SUPERSEDED / NOT RUN.

---
## EXP269 — PREPARED / NOT RUN

## ECO5 raw-log review after EXP268

Direct raw-log comparison changes the interpretation of the next test. In Eco5 capture `090209`, the first mailbox after `06F4/19` is answered with words `0000 0000 0000 0000 0080 0006`, after which `07D0/19` follows ~0.7 s later. Later mailbox replies with fifth word 0 and sixth word `0006` are interleaved with `07E4/17, 07F8/17, 080C/18, 0820/18, 0834/18, 0848/23, 0864/4, 0870/17, 0884/60`.

Therefore EXP269 as previously prepared (10 repetitions of `0001 0000`) is **SUPERSEDED / NOT RUN**. The next active experiment must test the exact phase-matched Eco5 first post-`06F4` response, not a larger count of the wrong payload.


Hypothesis: because EXP268 stopped answering the persistent `0708/6` mailbox after response #3, later parallel runtime traffic may have been prevented or delayed. EXP269 changes only the maximum service count from 3 to 10 exact `0708/6` idle responses using the same genuine Eco5 frame `0F030C0000000000000000010000001C88`. Proven prefix and safety gates remain unchanged. After response #10, observe RX-only for 30 s. Any different non-background FC16 or different FC03 is capture-only; no post-mailbox FC16 ACK and no eleventh mailbox response.

## EXP268 — COMPLETE / NEGATIVE

Hypothesis: after three bounded idle mailbox responses, later FC16/runtime traffic may appear during 30 s RX-only even though `0708/6` continues polling.

Observed:
- proven prefix through `06F4/19` completed again;
- one CRC resync occurred at BUS_RETURN, with post-return resync delta 0 and RX-drop delta 0 at summary;
- first `0708/6` arrived +3.621 s after `06F4` ACK;
- responses #1..#3 used the exact genuine Eco5 idle frame;
- after response #3, 30 s RX-only completed;
- mailbox requests reached 10 total, i.e. 7 more exact `0708/6` polls were observed unanswered;
- 21 recurrent `085F/5` background frames were counted after `06F4`;
- no different non-background FC16, no different FC03, and none of `07D0..0864` appeared;
- DE LOW at summary.

Conclusion: negative for the 30 s RX-only progression hypothesis. Persistent `0708/6` polling continues normally, but no later runtime family appeared while mailbox service was stopped after three replies.

---

## EXP267 — COMPLETE## EXP267 — COMPLETE## EXP267 — COMPLETE / NEGATIVE

Hypothesis: up to three consecutive exact `FC03 0708/count6` polls require the same genuine Eco5 idle response before the controller progresses.

Observed:
- proven prefix through `06F4/19` completed again;
- first `0708/6` arrived +1.561 s after `06F4` ACK;
- response #1 sent: `0F030C0000000000000000010000001C88`;
- response #2 sent after the repeated `0708/6`;
- response #3 sent after the next repeated `0708/6`;
- a fourth exact `0708/6` arrived ~4.18 s after response #3 and was deliberately not answered;
- no different meaningful FC03/FC16 appeared before the fourth poll;
- recurrent `085F/5` background traffic continued between mailbox polls;
- parser resyncs remained 0 and RX drops remained 0 in the observed run.

Conclusion: valid negative. Three identical genuine Eco5 idle mailbox responses do not cause immediate local XTR progression out of the observed `0708/6` polling phase. The repeated ~4.2 s cadence now looks more like normal ongoing mailbox service than a malformed-response retry.

---

## EXP267 — PREPARED / NOT RUN

Hypothesis: up to three consecutive exact `FC03 0708/count6` polls require the same genuine Eco5 idle response before the controller progresses. Only this repetition count changes from EXP266. Exact response: `0F030C0000000000000000010000001C88`. Max 3 TX; fourth poll is capture-only.

## EXP266 — COMPLETE / PARTIAL POSITIVE

Hypothesis: answer the first exact post-`06F4` `FC03 0708/count6` once with the genuine Eco5 idle mailbox frame `0F030C0000000000000000010000001C88`, then capture only.

Result:
- Proven prefix through `06F4/19` succeeded again.
- Background `085F/5` ignored at +95 ms.
- First `0708/6` at +1.561 s was answered exactly once with the genuine Eco5 idle response.
- Same `0708/6` repeated +4.180 s after the response; no second response sent.
- Parser resyncs 0; RX drops 0.

Conclusion: one idle mailbox response is insufficient to complete the local mailbox phase. Negative result recorded.

---

## EXP266 — PREPARED / NOT RUN

**Hypothesis:** respond once to the first exact locally proven post-`06F4/19` mailbox request `FC03 0708/count6` using the genuine Eco5 idle response `0F030C0000000000000000010000001C88`, then observe RX-only.

**Delta from EXP265:** replaces passive capture of `0708/6` with a single tightly gated response. The complete proven prefix is otherwise unchanged. No response to any other FC03, no repeated mailbox response, no post-mailbox FC16 ACK.

**Expected success signal:** after the one mailbox response, a new meaningful FC16/runtime frame or other FC03 appears without approval retry, parser/drop delta, or immediate 0708 retry.

**Negative result criteria:** repeated 0708, parser/drop delta, unexpected peer traffic, no meaningful post-mailbox frame within 10 s, or UI/controller side effect requiring recovery.

## EXP264 — 06EA/06F1/06F4 tail — COMPLETE / STRONG POSITIVE WITH CAPTURE AMBIGUITY

Hypothesis: ACK exact `06EA/7`, `06F1/3`, `06F4/19` in order after the proven prefix, then capture only.

Observed:
- `06EA/7` ACKed once.
- `06F1/3` followed and was ACKed once.
- `06F4/19` followed and was ACKed once.
- First post-`06F4` frame: `085F/5`, +107 ms, not ACKed.
- `085F/5` is a previously established recurrent passive/background family; therefore this is a capture artifact/overlay, not proof of the next ordered sync stage.
- One CRC resync occurred at bus return before the experiment chain; RX drops 0.
- No approval retry, no stage retry, no peer FC17/ACK anomaly.

Result: strong positive for the three tail ACKs; inconclusive for the next meaningful stage because the first-frame capture policy stopped on known background traffic.

## EXP264 — end-of-bulk sync tail — PREPARED / NOT RUN

Hypothesis: preserve the complete proven prefix through `06C5/33`, then ACK exact `06EA/7`, `06F1/3`, and `06F4/19` once each. After `06F4` ACK, capture the first different FC16 or FC03 and do not answer it. A `0708/6` FC03 is logged specifically but never answered in EXP264.

Negative/stop criteria: retry of the previous stage, unexpected FC16, any FC03 before tail completion, parser resync delta, RX drop delta, approval retry, peer FC17/ACK, or >5 s stage timeout.

## EXP263 — accelerated 12-block 33-word batch — COMPLETE / STRONG POSITIVE

Hypothesis: after the proven prefix through 0546/count20, ACK exact 055A, 057B, 059C, 05BD, 05DE, 05FF, 0620, 0641, 0662, 0683, 06A4 and 06C5 (all count=33), then capture only. Genuine Eco 5 predicted 06EA/count7.

Observed:
- Approval +1283 ms after controller return; R1 sent once.
- All twelve 33-word pages appeared in the expected order and were ACKed exactly once.
- First different post-06C5 frame: 06EA/count7, +475 ms after 06C5 ACK.
- Raw 06EA request: 0F1006EA00070E000A00200017001B0009001A0006F81A.
- 06EA not ACKed.
- Parser resyncs 0; RX buffer drops 0 after the run; DE LOW.
- No approval retry after R1 and no stage retry observed.

Conclusion:
Local XTR now confirms the genuine Eco 5 synchronization chain through the complete 055A..06C5 33-word run and exact 06EA/count7 next. Full Online/Link establishment remains unproven. Negative result retained: the session was intentionally stopped before 06EA ACK, so runtime/mailbox completion was not tested.

Recovery: one normal Thermia-controller reboot.

## EXP262 — accelerated 04A6..0546 ACK batch — COMPLETE / STRONG POSITIVE

Hypothesis: after the proven prefix through `0492/11`, ACK exact `04A6/13`, `04BA/22`, `04D8/27`, `04F6/14`, `050A/19`, `051E/10`, `0532/18`, and `0546/20` in order, then capture the first different FC16/FC03 without answering it.

Observed result: all eight new stages appeared in the predicted order and were ACKed exactly once. The first different frame after the `0546/20` ACK was exact `055A/count33`, +637 ms later, raw `0F10055A002142000000000000001F000C000000000000001F000C00000000000000000000001F000C000000000000001F000C00000000000000000000001F000C000000000000001FF26A`. No ACK was sent to `055A`.

Negative/clean results: no approval retry after R1; no acknowledged-stage retries observed; parser resyncs remained 0; RX buffer drops remained 0.

Conclusion: accelerated batching is confirmed workable through `0546/count20`, and the local XTR follows the genuine Eco 5 sync path through `055A/count33`. Full Online/Link remains unproven. Recovery: one normal controller reboot.


## EXP262 — accelerated 04A6..0546 batch — PREPARED / NOT RUN

Hypothesis: after the proven local Online/Link prefix through `0492/count11`, ACK a bounded batch of eight exact FC16 pages: `04A6/13`, `04BA/22`, `04D8/27`, `04F6/14`, `050A/19`, `051E/10`, `0532/18`, `0546/20`; then capture the first different FC16/FC03 without responding. Genuine Eco 5 predicts `055A/count33`.

Safety: all pages are exact known controller-originated FC16 export requests. EXP262 sends only standard address/count acknowledgements. Every stage is first-exact, time-bounded and parser-clean; unexpected traffic stops fail-closed. No FC03/mailbox response and no ACK after `0546`. Known incomplete-session recovery remains one normal controller reboot.


## EXP261 — bounded 046A/047E/0492 ACK batch — COMPLETE / STRONG POSITIVE

**Hypothesis:** after the proven local prefix, ACK exact `046A/count18`, then exact `047E/count19`, then exact `0492/count11`, and capture the first different FC16/FC03 stage without answering it.

**Observed facts:**
- first approval at +1245 ms after BUS_RETURN;
- R1 accepted with no approval retry;
- the proven prefix through `0456/count12` reproduced cleanly;
- `046A/count18` appeared and was ACKed once;
- `047E/count19` followed +722 ms later and was ACKed once;
- `0492/count11` followed +1480 ms later and was ACKed once;
- the first different block was exact `04A6/count13`, +576 ms after the 0492 ACK;
- raw `04A6` request: `0F1004A6000D1A0000000000000000000000000000000000000000402000000000CA9A`;
- `04A6` was not ACKed;
- no stage retries, no approval retry after R1, no unexpected peer frame, no post-return parser/RX-drop delta; DE LOW.

**Strong conclusion:** local XTR follows the genuine Eco 5 ordered synchronization path through `0492/count11`, with `04A6/count13` next in this run. The bounded-batch strategy remains valid.

**Unknown:** full Online/Link establishment and mailbox behavior remain unproven.

**Recovery:** one normal Thermia-controller reboot after the summary.


## EXP261 — bounded `046A -> 047E -> 0492` continuation — PREPARED / NOT RUN

**Hypothesis:** the local XTR continues to follow the genuine Eco 5 Online/Link FC16 sequence after EXP260. Preserve the complete proven prefix and ACK exactly three new expected stages: `046A/count18`, `047E/count19`, and `0492/count11`. Then capture the first different FC16/FC03 without answering it.

**New ACKs:** `046A/18 -> 0F10046A00126006`; `047E/19 -> 0F10047E0013E1C2`; `0492/11 -> 0F100492000B203D`.

**Primary prediction:** `04A6/count13` is the genuine Eco 5 next-page observation, but because `04A6/13` is also known as a recurrent passive family it is recorded as a prediction rather than a strict required success value.

**Safety:** same cold-boot approval guard and proven prefix as EXP260; first-exact-stage-only, <=5 s between ACKs, no retries, parser/drop counters unchanged, no unexpected peer frames. After `0492` ACK, capture only. No FC03 response. Controller reboot after summary.


## EXP260 — bounded `042E -> 0442 -> 0456` ACK batch — COMPLETE / STRONG POSITIVE

**Hypothesis:** after the locally proven prefix through `042E/count15`, ACK exactly `042E/15`, `0442/13`, and `0456/12` in order, then stop and capture the next different frame. Genuine Eco 5 predicts `046A/count18`.

**Observed facts:**
- first approval request at +1284 ms after BUS_RETURN; R1 sent once;
- `03E8/14` arrived +126 ms after R1 and was ACKed once;
- `03FC/11` arrived +694 ms after the `03E8` ACK and was ACKed once;
- `0410/22` arrived +1492 ms after the `03FC` ACK and was ACKed once;
- `042E/15` arrived +695 ms after the `0410` ACK and was ACKed once;
- `0442/13` arrived +1502 ms after the `042E` ACK and was ACKed once;
- `0456/12` arrived +566 ms after the `0442` ACK and was ACKed once;
- predicted `046A/count18` arrived +1473 ms after the `0456` ACK; it was captured and not ACKed.
- summary: approval retries after R1=0; all stage retry counters=0; peer17=0; unexpected peer ACK=0; post-return resync/drop deltas=0; DE LOW.

**UI side effect:** user reports the DHW-side literal `0` appeared again. No EXP260 `COMM. ERR ONLINE/LINK` confirmation yet. Recovery should be performed immediately after the summary rather than waiting for an alarm.

**Strong conclusion:** the bounded batching strategy is validated locally through `046A/count18` and preserves the same ordered sequence as the genuine Eco 5 reference.

Last updated: 2026-09-27

## EXP260 — bounded `042E -> 0442 -> 0456` ACK batch — PREPARED / NOT RUN

**Hypothesis:** continue the already-proven local Online/Link prefix in one bounded batch. After the proven EXP259 prefix, ACK exact `042E/count15`, then exact `0442/count13`, then exact `0456/count12`. The genuine Eco 5 reference predicts `046A/count18` next.

**New active variable family:** three exact standard FC16 ACKs: `0F10042E000FE01A`, `0F100442000DA1C6`, `0F100456000C2002`. Each is one-shot and only allowed after the preceding exact stage.

**Safety/stop rule:** any deviation, retry, FC03, unexpected peer response, parser/RX-drop delta, or >5 s missing expected stage stops the experiment immediately. After the `0456` ACK, capture the first different FC16/FC03 only; no `046A` ACK and no mailbox response.

**Known recovery:** deliberately incomplete Online/Link sessions have repeatedly produced DHW-side `0` and `COMM. ERR ONLINE/LINK`; reboot controller once after the summary.

## EXP259 — ACK `0410/count22`, capture next stage — COMPLETE / STRONG POSITIVE

**Hypothesis:** after the proven prefix `R1 -> 03E8/14 ACK -> 03FC/11 ACK -> 0410/22`, one exact FC16 ACK to `0410/count22` should advance the XTR to the next ordered sync block. Genuine Eco 5 predicted `042E/count15`.

**Observed:**
- approval at +1283 ms after BUS_RETURN;
- R1 once;
- `03E8/14` +138 ms after R1, ACKed once;
- `03FC/11` +682 ms after `03E8` ACK, ACKed once;
- `0410/22` +1498 ms after `03FC` ACK, ACKed once;
- `042E/15` +696 ms after `0410` ACK;
- `042E/15` not ACKed;
- `approval_after_r1=0`, `same03e8_after_ack=0`, `same03fc_after_ack=0`, `same0410_after_ack=0`;
- `peer17=0`, `unexpected_peer_ack=0`, `self_echo_r1=0`, `self_echo_ack=0`;
- `resync_postreturn=0`, `drop_postreturn=0`, `DE=LOW`.

**Result:** strong positive. Local XTR matches the genuine Eco 5 ordered sync prefix through `042E/count15`.

**Negative/safety result:** full Online/Link session is still not established; no `042E` ACK, no later FC16 ACK, and no FC03/mailbox response was emitted.

---

## EXP259 — UI side effect follow-up

After the successful protocol result, the user confirmed the same visible side effects seen in earlier incomplete Online/Link sessions: DHW-side literal `0` and exact `COMM. ERR ONLINE/LINK`. This is a repeated positive observation, not a new protocol stage.

Interpretation: the association between partial Online/Link servicing and the communication alarm is now reproducible across multiple active runs. The specific causal mechanism remains a hypothesis until a sufficiently complete session is shown to avoid the alarm. Recovery remains one normal controller reboot.


## EXP259 — exact `0410/count22` ACK then next-stage capture — PREPARED / NOT RUN

**Hypothesis:** after the locally proven prefix `R1 -> 03E8/14 ACK -> 03FC/11 ACK -> 0410/22`, one exact standard FC16 ACK to `0410/count22` should advance the XTR controller to a different block. The genuine Eco 5 reference predicts `042E/count15`.

**Only new active variable:** one ACK frame `0F1004100016401C` for exact slave `0x0F` FC16 `start=0410`, `count=22`, `bytecount=44`, request length `53`. The ACK carries no register-value payload.

**Safety:** R1, `03E8` ACK and `03FC` ACK retain the existing guards. The new `0410` ACK is one-shot, latch-before-DE, allowed only on the first exact post-`03FC`-ACK `0410/22` within 5 s with clean parser/drop counters and no approval/03E8/03FC retry or unexpected peer. After that, capture-only: no `042E` ACK, no later FC16 ACK, no FC03/mailbox response. Reboot controller after summary.

**Expected positive discriminator:** first post-`0410`-ACK block is `042E/count15`. Any other different FC16/FC03 is still recorded as a protocol result.

---

## EXP258 — exact `03FC/count11` ACK then next-stage capture — COMPLETE / STRONG POSITIVE

**Hypothesis:** after the locally proven `R1 -> 03E8/count14 ACK -> 03FC/count11`, one exact standard ACK to `03FC/count11` should advance the XTR to a different block. Genuine Eco 5 predicts `0410/count22`.

**Observed facts:** first approval +1243 ms after BUS_RETURN; R1 exactly once; `03E8/14` +138 ms after R1 and ACKed once; `03FC/11` +691 ms after the 03E8 ACK and ACKed once; `0410/22` appeared +1501 ms after the 03FC ACK and was not ACKed. No approval retry, no 03E8 retry, no 03FC retry, no unexpected peer frame, no post-return parser/drop delta; DE LOW at summary. User reports DHW-side `0` and the same `COMM. ERR ONLINE/LINK` alarm again.

**Exact result chain:** `R1 -> 03E8/14 -> ACK -> 03FC/11 -> ACK -> 0410/22 -> STOP`.

**Strong conclusion:** the first three ordered post-approval FC16 sync stages on the local XTR match the genuine Eco 5 sequence.

**Unknowns:** full session completion, later FC16 ordering on XTR, and mailbox behavior remain unproven. The repeated alarm is consistent with an incomplete approved session but is not yet proven to be caused specifically by the missing downstream ACK/mailbox service.

**Recovery:** one normal controller reboot before any further active test.

This file is the canonical experiment record. The compact table below indexes the early experiment series; EXP100+ are documented in the detailed chronological sections that follow. Detailed YAML and raw logs remain the primary evidence.

## EXP258 — exact `03FC/count11` ACK then next-stage capture — PREPARED / NOT RUN

**Hypothesis:** after the already-proven local prefix `R1 -> 03E8/count14 ACK -> 03FC/count11`, one exact standard FC16 ACK to `03FC/count11` should advance the XTR controller to a different block. The genuine Eco 5 reference predicts `0410/count22`.

**Only new active variable:** one ACK frame `0F1003FC000B4094` for exact slave `0x0F` FC16 `start=03FC`, `count=11`, `bytecount=22`, request length `31`. The ACK carries no register-value payload.

**Safety:** R1 and the `03E8` ACK retain the EXP257 guards. The new `03FC` ACK is one-shot, latch-before-DE, permitted only on the first exact post-`03E8`-ACK `03FC/11` within 5 s with clean parser/drop counters and no approval retry, `03E8` retry, or unexpected peer. After that, capture-only: no `0410` ACK, no later FC16 ACK, no FC03/mailbox response. Reboot controller after summary.

**Expected positive discriminator:** first post-`03FC`-ACK block is `0410/count22`. Any other different FC16/FC03 is still recorded as a protocol result.


## Post-EXP257 external Eco 5 follow-up — raw-log verified

No new local experiment was run. New external interpretation was checked against the complete public Eco 5 raw capture.

Observed facts:
- first cold-start approval request at +1.199/+1.202/+1.210 s after bus return in the three Eco 5 power-ups;
- successful genuine gateway responses at +120.153 s and +119.808 s after bus return, after 29 challenges each;
- middle no-gateway run ended by power-off at ~174 s and therefore cannot test a ~267 s natural cutoff;
- steady-state pre-power-off segment contains no approval exchange; Eco 8 steady-state absence must therefore remain open pending a cold-start capture;
- only two answered Eco 5 challenges exist, so repeated-challenge response determinism and cross-power-cycle response stability are unresolved;
- genuine endpoint continues ACKing the FC16 export stream after approval; `04A6/13` and `085F/5` are recurrent passive families whose ACK timing varies and is not a demonstrated precondition;
- first post-approval `0708/count6` mailbox polls occur at +158.393 s and +186.828 s after bus return, while the FC16 transfer is still active;
- in the first successful power-up the first mailbox poll is unanswered and the following poll is answered;
- the raw repeated idle response is six words `0000 0000 0000 0000 0001 0000` (not `...0100...` under standard Modbus word order);
- later fifth-word values include `03DC`=988 -> 984 -> 976 -> 908 -> 896 -> 768 -> 512 -> 0.

Interpretation/hypothesis:
- `COMM. ERR ONLINE/LINK` being a timeout of an approved-but-incompletely-serviced session is increasingly plausible but remains unproven;
- the fifth-word countdown may represent pending synchronization work, but no semantic mapping is established.

Decision:
- do not broaden directly to full-chain ACK + mailbox emulation;
- next candidate is **EXP258 (not prepared)**: add exactly one `03FC/count11` ACK after the already-proven EXP257 prefix and capture the first subsequent frame; genuine Eco 5 predicts `0410/count22`.


## EXP257 — One-shot R1 + single `03E8/count14` ACK + next-stage capture — COMPLETE / STRONG POSITIVE

**Hypothesis:** after EXP256's one-shot R1 transition into `03E8/count14`, acknowledge exactly the first `03E8/count14` once and capture the first different downstream FC16/FC03 request without answering it. Full genuine Eco 5 capture predicted `03FC/count11`.

**Observed facts:**
- controller cold-restart gap detected and clean `BUS_RETURN`;
- boot-only `04BA/count22` appeared at +316 ms after BUS_RETURN;
- first approval request at **+1285 ms**, `W071C=1A154568F9061AACDC1BC564001E8FD0`;
- exact R1 transmitted once; DE returned LOW;
- first post-R1 FC16 was exact `03E8/count14`, **+130 ms after R1**;
- exact standard ACK `0F1003E8000EC093` transmitted once; ACK latch closed before DE;
- first different post-ACK request arrived **+691 ms after ACK** and was exact `03FC/count11`, bytecount 22, length 31;
- raw `03FC` request: `0F1003FC000B160028000A0037000000000000000200120028001E003C369E`;
- payload words: `0028 000A 0037 0000 0000 0000 0002 0012 0028 001E 003C`;
- no ACK was sent to `03FC`;
- summary: `r1=1 ack03e8=1 approvals=1 approval_after_r1=0 post_r1_fc16=1 same03e8_after_ack=0 peer17=0 unexpected_peer_ack=0 self_echo_r1=0 self_echo_ack=0 resync_postreturn=0 drop_postreturn=0 DE=LOW`.

**Strong conclusions:**
- EXP257 satisfies its positive criterion.
- The XTR reproduces the genuine Eco 5 post-approval prefix `R -> 03E8/14 -> ACK -> 03FC/11`.
- The `03E8` ACK is sufficient to advance the local XTR one synchronization block.
- This substantially strengthens the interpretation that R1 enters the genuine Online/Link synchronization state machine rather than an unrelated failure state.
- Full Online/Link establishment remains unproven because `03FC` and all later stages were intentionally not acknowledged.

**Comparison with external reference:** the genuine Eco 5 capture proves twice that `03FC/count11` follows the acknowledged `03E8/count14`, and that acknowledged `03FC/count11` is followed by `0410/count22`. EXP257 reproduces the first of those transitions locally.

**Unknowns:**
- whether one exact ACK to local `03FC/count11` yields `0410/count22`;
- whether the remainder of the XTR synchronization ordering matches the Eco 5 chain;
- when `0708/count6` mailbox traffic starts locally;
- UI side effect for this run, pending user report.

**Safety/recovery:** no further ACKs were sent. One normal controller reboot is required after the incomplete session if not already performed.

## EXP256 — One-shot R1 + full post-R1 FC16/FC03 differential census — COMPLETE / ACTIVE STRONG POSITIVE

**Hypothesis:** the already-tested R1 changes the local XTR native FC16 distribution; leading pre-run hypothesis was selective suppression of `085F/count5` while `04A6/count13` persisted.

**Observed facts:**
- clean >=6 s controller bus gap and BUS_RETURN;
- first exact `071C/0730` approval request at **+1245 ms**; local `W071C=1A144532F9060CACDC1BC590001E8F64`, local schema check `RTC=OK`;
- exactly one R1 frame transmitted; DE returned LOW and one-shot latch stayed closed;
- approval requests **1**, retries after TX **0**;
- FC16 requests **390**, FC16 ACKs **0**;
- FC03 `0708/count6` **0**, other FC03 **0**;
- peer FC17 response **0**, self-echo **0**;
- complete FC16 census: `04BA/count22` = **1**, `03E8/count14` = **389**, `04A6/count13` = **0**, `085F/count5` = **0**;
- first `03E8/count14` at **+1369 ms after BUS_RETURN / +124 ms after R1**; last at **+419896 ms**; median `03E8` retry interval ~**1308 ms**;
- final state `A80E=0028 A80F=000A AFDC=0010`;
- post-return `resync_delta=0`, `drop_delta=0`;
- user reports the DHW/tank-side literal `0` reappeared; VERSION screen did not change; after summary the controller again raised **`COMM. ERR ONLINE/LINK`**, exactly matching EXP252.

**Strong conclusions:**
- R1 again suppresses all later approval retries.
- The pre-run H1 is falsified: R1 does **not** leave the passive `04A6/count13` stream intact while merely removing `085F/count5`. Both passive runtime families disappear.
- R1 instead advances the controller into the first known `0x0F` settings synchronization block, `03E8/count14`.
- Because EXP256 intentionally sent no FC16 ACK, the controller remained stalled retransmitting `03E8/count14` for the rest of the seven-minute observation.
- The prior EXP252 total `fc16req=386` is now best explained as likely the same unclassified `03E8` retransmission state, rather than the previously suspected passive-family remainder.

**Hypothesis / interpretation:** R1 is accepted at least far enough to cross the approval boundary and enter controller->Online/Link synchronization. This is not yet proof of a fully established Online/Link session because the expected endpoint transfer ACKs and any later FC03/mailbox phase were deliberately absent.

**Unknowns:**
- whether ACKing the exact first `03E8/count14` after R1 yields the same `0410/count22` next stage seen in earlier acknowledged-transfer experiments, or a different post-approval sequence;
- how far the synchronization chain proceeds before an additional service/mailbox response is required;
- exact semantics of the reproduced DHW-side `0`.

**Safety/recovery:** one normal controller reboot is required after the summary, matching the run plan and the known recoverable EXP252 side effect. No second active approval/sync test until normal UI recovery is confirmed.


### EXP141 — gated 0x0F sequence walker — PREPARED

Hypothesis:
Multiple additional controller-side 0x0F sync stages can be discovered in one run without reflashing, while retaining explicit approval for every newly observed FC16 start/count pair.

New automatic target:
- `05FF/count33` (locally proven by EXP140).

Unknown-stage gate:
1. observe exact start/count at least 3 times;
2. log full payload;
3. lock candidate;
4. operator presses `EXP141 ARM ACK Current Candidate Once`;
5. no asynchronous TX occurs;
6. next exact matching request receives one standard FC16 ACK;
7. continue to next unknown stage.

Limits/guards:
- max 8 manually approved stages;
- no FC03 response;
- no semantic value injection;
- abort on real 0x0F responder, parser resync, or RX drop.


### EXP141 — gated 0x0F sequence walker — RUNNING / PARTIAL POSITIVE

Observed:
- baseline: repeated known `05FF/count33`;
- active phase ACKed `05FF/count33`;
- new block appeared ~1.56 s later: `0662/count33`;
- exact payload repeated consistently;
- candidate locked after 3 exact start/count observations;
- no `ARM_OK` or manual-stage ACK appears in the supplied log, so the controller remained retrying `0662/count33`;
- no parser resync, RX drop, FC03, or real 0x0F responder activity in the shown run.

New proven progression:
`05FF/33 -> ACK -> 0662/33`.

Current action:
Press `EXP141 ARM ACK Current Candidate Once` while the walker remains active.


#### EXP141 continuation — 0662/33 ACKed

### EXP140 — sequential 0x0F FC16 ACK probe, stage 0x04BA — PREPARED

Hypothesis:
ACKing the locally proven next-stage request `04BA/count22` will advance the controller to a subsequent 0x0F transfer stage or to an FC03 read phase.

Only change versus EXP139:
- add `04BA/count22` to the ACK whitelist.

Safety:
No register values are injected, FC03 is never answered, unknown next-stage FC16 shapes are logged but not ACKed, and TX stops immediately on the first positive discriminator.


### EXP140 — sequential 0x0F FC16 ACK probe, stage 0x04BA — COMPLETE / POSITIVE TRANSPORT PROGRESSION

Observed:
- controller resumed/retried `04BA/count22` throughout the passive baseline after ESP reboot;
- first active `04BA/count22` was ACKed;
- ~0.65 s later new `05FF/count33` appeared;
- new block was not ACKed and test stopped;
- final summary:
  `reason=POSITIVE_NEW_FC16_STAGE_AFTER_04BA duration_ms=31011 fc16Seen=30 whitelisted=29 unknown=1 ackTx=1 txRefused=0 fc16AckSeen=0 fc03Req=0 fc03Resp=0 existingResponder=NO resyncDelta=0 dropDelta=0 DE_LOW`.

Conclusion:
Locally observed sequence now extends to:
`03E8/14 -> ACK -> 0410/22 -> ACK -> 042E/15 -> ACK -> 04A6/13 -> ACK -> 04BA/22 -> ACK -> 05FF/33`.

Next:
EXP141 adds only `05FF/count33` to the ACK whitelist.


### EXP139 — sequential 0x0F FC16 ACK probe, stage 0x042E — PREPARED

Hypothesis:
ACKing the locally proven next-stage request `042E/count15` will advance the controller to a subsequent 0x0F transfer stage or to an FC03 read phase.

Only change versus EXP138:
- add `042E/count15` to the ACK whitelist.

Safety:
No register values are injected, FC03 is never answered, unknown next-stage FC16 shapes are logged but not ACKed, and TX stops immediately on the first positive discriminator.


### EXP139 — sequential 0x0F FC16 ACK probe, stage 0x042E — COMPLETE / POSITIVE TRANSPORT PROGRESSION

Observed:
- controller resumed/retried `042E/count15` throughout the passive baseline after ESP reboot;
- first active `042E/count15` was ACKed;
- ~0.52 s later `04A6/count13` appeared and was ACKed under the unchanged prior whitelist;
- ~1.55 s after that, new `04BA/count22` appeared;
- new block was not ACKed and test stopped;
- final summary:
  `reason=POSITIVE_NEW_FC16_STAGE_AFTER_042E duration_ms=32936 fc16Seen=31 whitelisted=30 unknown=1 ackTx=2 txRefused=0 fc16AckSeen=0 fc03Req=0 fc03Resp=0 existingResponder=NO resyncDelta=0 dropDelta=0 DE_LOW`.

Conclusion:
Locally observed sequence is now:
`03E8/14 -> ACK -> 0410/22 -> ACK -> 042E/15 -> ACK -> 04A6/13 -> ACK -> 04BA/22`.

Nuance:
`04A6/13` was already known from earlier passive XTR captures and was already whitelisted, so EXP139 does not prove it is exclusively sequence-owned. It is nevertheless an observed intermediate stage in this run.

Next:
EXP140 adds only `04BA/count22` to the ACK whitelist.


### EXP138 — sequential 0x0F FC16 ACK probe — PREPARED
Hypothesis: after EXP137's proven progression `03E8/count14 ACK -> 0410/count22`, ACKing only `0410/count22` as the one new variable will reveal the next controller stage.

Only change versus EXP137:
- add `0410/count22` to the ACK whitelist.

Positive:
- first previously unseen FC16 shape after a successful 0410 ACK; or
- first 0x0F FC03 request after a successful 0410 ACK.

On either positive discriminator, TX stops immediately. New FC16 shapes are logged but not ACKed. FC03 is never answered. No semantic values are injected.


### Genuine Online capture follow-up — RAW FRAME CORRECTION
fclauson's follow-up interpretation claimed a direct `20 -> 21 -> 20` value path in `0x0848/0x07E4`. Independent raw parsing shows:
- first `0848/count23`: `0858=0`, `085A=20`;
- second `0848/count23`: `0858=21`, `085A=20`;
- therefore the actual delta is `0858: 0 -> 21`, not one field `20 -> 21`;
- the later `07E4` block does not prove the same field reverted to 20.

Record `0858=21` as a strong Heat-Curve-change/event candidate only. Do not label it as the persistent Heat Curve register yet.


### EXP138 — sequential 0x0F FC16 ACK probe — COMPLETE / POSITIVE TRANSPORT PROGRESSION

Observed:
- after reboot, controller was still stuck/retrying `0410/count22` throughout the passive baseline;
- baseline `fc16Seen=28`, all known, no FC03, no responder;
- first active `0410/count22` was ACKed;
- ~1.54 s later controller advanced to new `042E/count15`;
- new block was not ACKed and experiment stopped;
- final summary:
  `reason=POSITIVE_NEW_FC16_STAGE_AFTER_0410 duration_ms=31949 fc16Seen=30 whitelisted=29 unknown=1 ackTx=1 txRefused=0 fc16AckSeen=0 fc03Req=0 fc03Resp=0 existingResponder=NO resyncDelta=0 dropDelta=0 DE_LOW`.

Conclusion:
The acknowledged XTR 0x0F sequence is now locally proven as:
`03E8/14 -> ACK -> 0410/22 -> ACK -> 042E/15`.

Additional finding:
Controller sequence state persists across ESP reboot/responder disappearance; it resumes/retries the outstanding stage.

Next:
EXP139 adds only `042E/count15` to the ACK whitelist.


### EXP137 — PREPARED — 0x0F FC16 ACK-only presence probe
30 s passive collision-check baseline, then up to 90 s ACK-only responses to exact known XTR 0x0F FC16 shapes (`03E8/14`, `0442/13`, `04A6/13`, `085F/5`). No FC03 responses and no register values injected. Positive = controller starts an 0x0F FC03 read after ACK-only presence; first read stops TX immediately.


### EXP137 — 0x0F FC16 ACK-only presence probe — COMPLETE / POSITIVE TRANSPORT PROGRESSION

Hypothesis:
Simple slave-0x0F presence/acknowledgement may cause the controller to progress toward the genuine Online/DCM read phase.

Observed:
- 30 s baseline: `fc16Seen=42`, all `whitelisted=42`, `unknown=0`, no 0x0F FC03 and no responder activity.
- Active phase:
  - ACK `03E8/count14` once;
  - controller immediately introduced new `0410/count22`;
  - ACK `085F/count5` once;
  - `0410/count22` was never ACKed and repeated 83 times.
- Final summary:
  `duration_ms=120150 fc16Seen=127 whitelisted=44 unknown=83 ackTx=2 txRefused=0 fc16AckSeen=0 fc03Req=0 fc03Resp=0 resyncDelta=0 dropDelta=0 DE_LOW`

Conclusion:
The controller advanced from the normal unacknowledged XTR 0x0F pattern into a new `0410/count22` stage only after the first `03E8/count14` ACK. Continuous retransmission of `0410/count22` without ACK strongly indicates an acknowledged sequential transfer/synchronization state machine.

Negative:
No FC03 phase was reached because `0410/count22` remained unacknowledged.

Next:
EXP138 adds only `0410/count22` to the ACK whitelist.


### External genuine Online capture — major architecture correction
A working Thermia Online installation shows a real slave `0x0F` ACKing FC16 and serving FC03 reads. During Heat Curve 20->21->20, the two captured `03E8` read snapshots differ only at the first word, 23->22. The capture also shows recurrent controller->0x0F FC16 block families and no response to the recurring `0x06` FC17 poll. This strongly shifts the Online/DCM hypothesis from `0x06` toward a shared register interface at `0x0F`. Slave `0xA5` is also active but remains unidentified.

### EXP136 — passive DHW COMFORT/ECO mode A/B/A — COMPLETE / NEGATIVE
Confirmed physical COMFORT<->ECO change and restore. Recurrent `03E8..03F5` remained byte-for-byte unchanged; zero word changes, zero parser/drop errors. DHW mode is not represented in that recurrent block.

### EXP135 — passive DHW START A/B/A — COMPLETE / NEGATIVE FOR 03F1
Manual `SERVICE -> WARMWATER -> START` ±1 °C produced no change in recurrent `03E8..03F5`; `03F1` remained 40. `041D` was not covered by an observed block. Downgrade `03F1 = Hot Water Start` to OPEN / locally unsupported.

## 2026-09-24 — EXP129–134 current run

### EXP134 — Passive DHW START correlation — PREPARED, NOT RUN
Hypothesis: external candidate decimal 1053 / hex `0x041D` may correspond to `SERVICE → WARMWATER → START` on this XTR.

Planned controlled variable: manually change only DHW START by -1 °C and restore it while ESP passively logs 0x0F changes. `0x041D` is a candidate marker only. No ESP write.

Safety: run only after EXP133 review; use a moment when DHW production is inactive and the actual DHW temperature is sufficiently above START so the -1 °C step cannot create a new heat demand.


### EXP134 — passive DHW START correlation — PROCEDURAL / INCIDENTAL
Only `03E8 34 -> 35` changed, tracking Heating Curve. No valid DHW mapping resulted.

### EXP133 — Passive 0x0F block-structure census — RUNNING / PARTIAL
Hypothesis: the XTR uses stable native 0x0F application/settings blocks beyond the already-known 0x03E8 block, possibly sharing structural patterns with the external ATEC/DHP-AQ material.

Design: 600 s passive-only census; no RS485 TX, no 0x06 response, no direct 0x0F write. Log every unique 0x0F FC03/FC10/FC17 shape and first payload. External block starts are flagged only as hints.

Partial observed facts:
- experiment started with `PASSIVE_ONLY DE_LOW no_tx`;
- first native FC10 shape: start `0x04A6`, count 13; payload has only word `0x04B0=0x4020` nonzero in the first observed frame;
- second native FC10 shape: start `0x085F`, count 5; first payload all zero;
- `0x0861` is inside that native five-word block;
- parser resyncs and RX drops remained zero in the supplied partial log.

Status: **OPEN**. Do not infer the final 0x0F block map until the automatic EXP133 SUMMARY and full 600 s log are captured.

### EXP132 — AFC8/AFC9/AFCB validity/header matrix with AFD1=16 — COMPLETE / NEGATIVE
Hypothesis: `AFC8/AFC9/AFCB` may form a metadata validity/header pattern whose effect only appears with a nonzero valid AFD1 version.

Observed: EXP 1.6 remained unchanged when AFC8, AFC9, AFCB were zeroed individually, pairwise and all together, with AFD1 fixed at 16. Final summary: `tx=353`, `refused=0`, `marksSame=16`, `marksChanged=1`, `marksGone=0`, `resyncDelta=0`, `dropDelta=0`.

Conclusion: AFC8/AFC9/AFCB are not required for the VERSION page to display EXP 1.6.

### Architecture review after EXP132
Uploaded Discussion #143 and supporting files from another Thermia platform were compared against our own captures. They are treated as external hints, not truth for XTR. The strongest cross-check is that our XTR itself already carries `0x0F FC10` application/settings blocks starting at `0x03E8`, while the external work independently identifies similar 0x0F block traffic. This shifts the next investigation from guessed 0x06 application payloads toward passive XTR-specific 0x0F block mapping.

### EXP131 — AFD0 type with valid AFD1 version — COMPLETE / NEGATIVE
Hypothesis: `AFD0` may select accessory type/identity when `AFD1` contains a valid version.

Observed: baseline `AFD0=0, AFD1=16` displayed EXP 1.6. `AFD0=1,2,10,16` produced no visible change; restore phases were also unchanged. Summary reported `tx=208`, `refused=0`, `marksSame=10`, `marksChanged=1`, `marksGone=0`, `resyncDelta=0`, `dropDelta=0`.

Conclusion: tested AFD0 values are not a simple visible type/identity selector.

### EXP130 — AFD1 version scaling — COMPLETE / POSITIVE MAPPING
Hypothesis: `AFD1` is the visible EXP/expansion-board version field.

Observed: with a valid 0x06 responder, VERSION display tracked the tested AFD1 values as tenths: `0→0.0`, `1→0.1`, `2→0.2`, `10→1.0`, `16→1.6`.

Conclusion: `AFD1` is a proven visible EXP version field for this XTR UI path. This is metadata/UI semantics only; it does not prove Online/DCM identity or write-session readiness.

## EXP107 — PREPARED — Persistent accessory image then isolated AFCA pulse

Hypothesis:
A known 0x06 transaction may behave differently if the accessory-side image has been continuously stable for >=60 s before AFCA is asserted.

Controlled change:
Only the preload/stabilization duration changes. The historical image and AFCA 4-phase mechanism are already-tested values.

Sequence:
1. qualify clean idle baseline;
2. transmit historical REQ-low image continuously for >=60 s;
3. change only AFCA 0000->03E8;
4. wait for 0861=16;
5. change only AFCA 03E8->0000;
6. wait for 0861=0;
7. continue the identical REQ-low image for 90 s;
8. summary.

Safety:
No new semantic write target; exact 0x06 slot only; existing-responder inhibit; compressor/outdoor idle guards; parser/drop guards; hard handshake timeouts.


## EXP107 — COMPLETE — Persistent image + isolated AFCA pulse

Result: negative for semantic initialization, positive for transport reproduction.

Timeline:
- cached settings baseline accepted
- TX_PRELOAD_REQ_LOW_01 started historical envelope
- image held continuously for 61.023 s
- TX_REQ_ASSERT: only AFCA changed to 03E8
- 0861: 0 -> 16 after 328 ms
- TX_REQ_DEASSERT: only AFCA returned to 0
- 0861: 16 -> 0 after 1122 ms
- identical REQ-low image continued for 90 s

Summary:
`handshake_complete=1 total_responses=144 observe_responses=84 A80E_peak=0 A80E_changes=0 AFDC_peak=0 AFDC_changes=0 AFDC_nonzero=0 status_peak=16 settings_changed=0 resync_delta=0 drop_delta=0`

Observed negative:
No A80E/AFDC activation, no semantic settings change, no new controller-side state beyond the known 0861 ACK.

Conclusion:
Persistent presence duration is not the missing DCM semantic bootstrap. Do not spend further experiments on longer dwell times or nearby timing variants unless new external evidence justifies them.


## Firmware analysis after EXP107

No new bus experiment was run.

New binary evidence:
- 2.1.35: generic DHPParameterCache exists, but no HPNode/SystemIntegration application layer in RegulationEngine.
- 2.7.42: HPNode/SystemIntegration application layer present.
- IntegrationMode is confirmed ParameterID 0x4414.
- SystemIntegrationInitRequest and InitSyncDone are internal booleans, not wire parameters.
- IntegrationMode update triggers full three-group resynchronization.
- system integration flips selected heat-pump parameters from GET-on-sync to SET-on-sync.

Decision:
Do not design EXP108 around a guessed "init flag". First reconstruct the three sync groups and look for a local mailbox representation of grouped synchronization.


## EXP106 — Passive integration-sync window correlator — PREPARED

Hypothesis: `A80F=0x0032` may identify the broader integration/synchronisation phase that older captures associated with A80E/AFDC cycling. EXP93 never triggered, so this remains untested.

Plan: strictly passive. Arm after >=15 s uptime, observe up to 30 min, trigger on A80F=50, then capture 180 s post-trigger context across A80C..A812, A7F8..A806, AFDC..AFE0/cadence, 0861, settings, 0x1E command image and outdoor state. Hard stop 1800 s if no trigger. TX=0.


## Cross-model evidence update — Piotr Romanowski / thermia-bus-sniffer — 2026-09-23

This is not a new Marten experiment; it is independent corroborating evidence from an iTec Eco 8 / DHP-AQ unit.

Observed by Piotr:
- corrected prior claim: `0x1E 0x001E..0x0033` is not frozen; it changes rarely and out of step with the live block;
- `B3B1` works as a real room-setpoint request channel in the slave response slot, encoding x1 °C;
- the controller stores the accepted setpoint and pushes it back through `B3C5`;
- `B3B1=0` means no request, not revert/clear;
- `AFDD=AFDE=AFDF=0` throughout a long passive capture;
- `AFE0` tracks displayed outdoor temperature x1;
- `AFDC` continuously pulses `0 <-> 32` with ~64 s period (~17 s high / ~47 s low);
- `A80E` follows the same pulse timing to the second;
- passive `0861` remained constantly `0` over multiple days;
- one isolated `AFDC=16` coincided with outdoor-unit-active status rise, insufficient for a semantic interpretation;
- A80E bit 3 appeared independently for ~10 minutes.

Strong conclusion:
- the recurring A80E/AFDC `0x20` state is ordinary controller lifecycle/heartbeat behaviour, not evidence of DCM login, approval, or semantic session.
- `0861` remains the cleaner transaction-level discriminator for active `AFCA=03E8` tests.

Candidate EXP107 direction after EXP106 closes:
- maintain one already-tested, harmless 0x06 accessory baseline image continuously for a stabilization interval;
- pulse only `AFCA 0 -> 03E8 -> 0` with all other words unchanged;
- observe `0861`, settings, controller state, CMD1E and outdoor state;
- do not gate the experiment on AFDC/A80E values.


## EXP106 — CLOSED (partial but sufficient negative)

The planned final post-trigger summary was not captured, so EXP106 remains technically incomplete as a full-duration run. However, the discriminating hypothesis is sufficiently rejected:

- A80E/AFDC cycling occurred at A80F 75, 80 and 50;
- A80F=50 therefore is not required for that lifecycle;
- A80F 80->50 occurred close to ordinary outdoor-unit transition to state 16/idle;
- no passive 0861 activity or settings mutation was seen;
- cross-model Eco 8 evidence shows AFDC/A80E 0<->0x20 can be a continuous heartbeat.

Decision:
Close EXP106 and do not build further A80F/AFDC-gated semantic tests.

## EXP105 — State-gated canonical transaction — PREPARED

**Hypothesis:** a semantic/application transaction may only be accepted during the natural controller lifecycle window where `A80E=0x0020` and `AFDC=0x0020`.

**Change from EXP104:** no payload sequencing experiment. EXP105 remains passive until the natural gate and then sends one already-known historical canonical transaction. This isolates controller-state timing as the variable.

**Safety:** no known setting target, no new unknown payload values, no TX before the gate, fail-closed UART guard, 180 s hard stop.


## EXP105 — State-gated canonical transaction — COMPLETED NEGATIVE

Hypothesis: the known historical `00FF,0001,REQ,0001,0...` transaction may only gain semantic meaning during the natural `A80E=0x0020` / `AFDC=0x0020` lifecycle window.

Observed:
- gate triggered naturally at ~32.9 s after arm;
- preload and REQ-high both occurred while A80E and AFDC were still `0x0020`;
- ACK-high after 373 ms; ACK-low after 1151 ms;
- summary: `complete=1 hard_stop=0 gate_seen=1 gate_aborts=0 txn_complete=1 ack_hi=1 ack_lo=1 settings_pushes=0 settings_changes=0 cmd1e_changes=0 outdoor_changes=0 resync_delta=0 drop_delta=0`.

Result: valid negative. The natural `0x20/0x20` controller window does not make the known historical envelope semantically active.


## EXP104 — AFC8 sequence-toggle canonical transaction chain — PREPARED

Hypothesis: AFC8 may act as transaction identity/sequence metadata only when its value changes across consecutive canonical transactions.

Plan: T1 AFC8=00FF, T2 AFC8=00FE, T3 AFC8=00FF; AFC9=1, AFCB=1, tails zero, canonical AFCA handshake for each; no zero-recovery between T1/T2/T3; 10 s zero final observation; 60 s hard stop. No known setting IDs. Corrected bus-health diagnostics from fixed EXP103 retained.


## EXP104 — AFC8 sequence-toggle canonical transaction chain — COMPLETED NEGATIVE
- Hypothesis: AFC8 may act as transaction identity/sequence metadata when changed between consecutive canonical transactions.
- Sequence: T1 `00FF`, T2 `00FE`, T3 `00FF`; AFC9/AFCB fixed at `0001`; AFCA canonical REQ handshake; no recovery gap between transactions.
- Result: all 3 transactions ACKed fully (`ack_hi=3`, `ack_lo=3`, `t1=t2=t3=1`). ACK-high: 447/441/447 ms after REQ assert. ACK-low: 1076 ms after REQ deassert for all 3.
- No semantic effect: `settings_pushes=0`, `settings_changes=0`, `cmd1e_changes=0`, `outdoor_changes=0`.
- `ctrl_changes=1` and `06_changes=1` were the natural A80E/AFDC `0->32` cycle occurring after transaction completion; the cycle later reset and repeated, so not attributed to EXP104.
- Bus-health bookkeeping fix validated: frame count increases and last-valid-frame age is live.
- Conclusion: simple AFC8 sequence-toggle hypothesis negative.


## EXP103 — repeated identical canonical transaction chain — PREPARED

Hypothesis: DCM application/session state may accumulate only after multiple consecutive successfully acknowledged transactions with an unchanged historical envelope.

Plan: three identical `00FF,0001,REQ,0001,0...` canonical transactions. T2 and T3 are chained immediately after ACK-low with no 3 s zero-recovery between them. After T3, reply all zeros and observe 10 s. No new payload values or known setting IDs. Hard stop 60 s.


## EXP103 — repeated identical canonical transaction chain — COMPLETED NEGATIVE

Hypothesis: DCM application/session state may accumulate only after multiple consecutive successfully acknowledged transactions with an unchanged historical envelope.

Observed:
- T1/T2/T3 all completed with canonical `0861 0->16->0` handshakes;
- no 3 s zero-recovery was inserted between transactions;
- `ack_hi=3`, `ack_lo=3`, `t1=t2=t3=1`;
- `settings_changes=0`, `ctrl_changes=0`, `06_changes=0`;
- `cmd1e_changes=0`, `outdoor_changes=0`;
- `resync_delta=0`, `drop_delta=0`;
- final `complete=1`, `hard_stop=0`.

Result: valid negative. Three back-to-back identical historical-envelope transactions do not establish semantic DCM state.

Post-run note: after the experiment summary, a natural `A80E 0->32` followed by `AFDC 0->32` occurred, and the pattern repeated later. These transitions are not attributed to EXP103 because they occurred after the experiment ended.

Diagnostics note: this run used the pre-fix health-bookkeeping build, so `Bus Last Valid Frame Age` stayed `nan` and `Valid Frames Since Boot` stayed `0` despite continuous bus traffic. This does not invalidate the experiment result.


## Historical archive re-analysis before EXP102

Reviewed 98 archived Thermia logs. Recovered earlier coverage showed that EXP16/18 had already varied AFC9/AFC8 broadly, EXP14/15 had varied AFCB, EXP24/25 had probed words 4..11 with 0001 during the ACK window, and EXP26/28 had tested structured word4/word5 payloads. All were negative for a semantic setting change despite valid transport behavior.

This makes further isolated-word tests redundant. A new structural hypothesis is therefore promoted: one of the historical `0001` words may be a payload length/count, so previous extra tail data may have been outside the declared message length.

## EXP102 — count / structure interaction matrix — PREPARED

Hypothesis: AFC9 and/or AFCB acts as a declared payload length/count.

Plan: six canonical transactions: historical count-1 control, AFC9 lengths 2 and 3 with matching tail words, AFCB lengths 2 and 3 with matching tail words, and a both-length2 case. Small values only; no known setting IDs; 3 s zero recovery; hard stop 80 s.

## EXP102 — count / structure interaction matrix — COMPLETED NEGATIVE

Hypothesis: AFC9 and/or AFCB may be a declared payload length/count.

Observed:
- six of six transactions completed;
- `ack_hi=6`, `ack_lo=6`, `0861_changes=12`;
- T1..T6 each completed once;
- coherent AFC9 length-2/3, AFCB length-2/3, and both-length2 structures all received normal transport ACKs;
- `ctrl_changes=0`, `rsp02_changes=0`, `06_changes=0`;
- `settings_pushes=0`, `settings_changes=0`;
- `cmd1e_changes=0`, `outdoor_changes=0`;
- `resync_delta=0`, `drop_delta=0`.

Result: valid negative. Matching larger count-like values with additional tail words does not unlock semantics. The simple AFC9/AFCB length-count hypothesis is rejected.


## Post-EXP102 archive audit — 2026-09-23

No new experiment was armed. Historical archive review covered 98 logs and recovered broader prior test coverage than the condensed state showed. At least 45 unique logged experimental 0x06 response payload forms were indexed. Earlier EXP13–18, 24–28 and later EXP52–102 collectively make further isolated-word/value probing low-value. No genuine DCM03 accessory response was identified in the archive.

Decision: **EXP103 deferred pending new evidence**. Negative results are preserved; next active test should be derived from genuine DCM traffic, firmware/PCB evidence, or another independently sourced protocol trace rather than another guessed response.


## EXP101 — AFCC..AFD3 one-word influence matrix — PREPARED

Hypothesis: one or more tail response words AFCC..AFD3 may participate in the missing DCM03 application layer.

Plan: eight transactions, one word at a time: AFCC=1, AFCD=1, AFCE=1, AFCF=1, AFD0=1, AFD1=1, AFD2=1, AFD3=1. Canonical AFCA=03E8 handshake; 3 s zero-recovery between transactions; hard stop 95 s. No known setting target.

## EXP101 — AFCC..AFD3 one-word influence matrix — COMPLETED NEGATIVE

Hypothesis: one of the still-unmapped tail words `AFCC..AFD3` may be an application-layer selector when transported with the proven canonical REQ/ACK handshake.

Observed:
- 8/8 planned transactions completed;
- `ack_hi=8`, `ack_lo=8`, `0861_changes=16`;
- T1..T8 each completed once;
- per transaction exactly one of AFCC..AFD3 was `0x0001`;
- `ctrl_changes=0`, `rsp02_changes=0`, `06_changes=0`;
- `settings_pushes=0`, `settings_changes=0`;
- `cmd1e_changes=0`, `outdoor_changes=0`;
- `resync_delta=0`, `drop_delta=0`;
- no hard stop or TX refusal.

Result: negative. No tested tail word produced a detectable application-layer effect by itself.

## EXP100 — Multi-transaction historical-field matrix

**Hypothesis:** those fields may only matter inside the proven canonical REQ/ACK transaction.

**Design:** six transactions in one run: AFC9 only; AFCB only; AFC8+AFC9; AFC8+AFCB; AFC9+AFCB; AFC8+AFC9+AFCB. Each uses preload -> `AFCA=03E8` -> wait `0861=16` -> `AFCA=0` with payload stable -> wait `0861=0` -> 3 s zero-presence observation. Hard stop 75 s. No semantic setting target.

## EXP100 — Multi-transaction historical-field matrix — result

**Hypothesis:** historically observed `AFC8/AFC9/AFCB` fields may only matter inside a valid canonical `AFCA=03E8` transaction.

**Observed:** six of six transactions completed. Each followed preload -> REQ high -> `0861=16` -> REQ low with stable payload -> `0861=0` -> observation. Final summary: `duration_ms=58046`, `complete=1`, `hard_stop=0`, `06polls=51`, `tx=51`, `refused=0`, `ack_hi=6`, `ack_lo=6`, `t1=1..t6=1`, `0861_changes=12`, `settings_pushes=0`, `settings_changes=0`, `ctrl_changes=0`, `rsp02_changes=0`, `06_changes=0`, `cmd1e_changes=0`, `outdoor_changes=0`, `resync_delta=0`, `drop_delta=0`.

**Result:** valid negative. Carrying the tested historical non-REQ field combinations inside a proven transport transaction still produces no semantic effect.


## EXP100 — Multi-transaction historical-field matrix — COMPLETED

Hypothesis: AFC8/AFC9/AFCB may only have application-layer meaning inside a valid AFCA=03E8 transaction.

Result: valid negative. All six transactions completed with canonical four-phase transport (`ack_hi=6`, `ack_lo=6`, `0861_changes=12`). No controller, 0x02 response, settings, 0x1E command, outdoor-state, or 0x06 controller-write change occurred. `resync_delta=0`, `drop_delta=0`.

Conclusion: historical AFC8/AFC9/AFCB values, separately and in all tested combinations, are semantically insufficient even inside valid transport transactions.

## EXP99 — Historical-field matrix, REQ low
Prepared as a faster structured follow-up: ten 8 s phases test AFC9=0001, AFCB=0001, pairwise combinations with AFC8=00FF, and the full historical non-REQ combination. AFCA remains 0000 throughout.


## EXP99 — Historical-field matrix, REQ low — result

**Hypothesis:** `AFC8=00FF`, `AFC9=0001`, `AFCB=0001` may have standalone or combinatorial application-layer meaning without REQ.

**Observed:** 80 s complete; `06polls=75`, `tx=75`, `refused=0`; each of the ten phases received 7–8 responses. `06_min_ms=707`, `06_max_ms=1450`. `ctrl_changes=0`, `rsp02_changes=0`, `06_changes=0`, `0861_changes=0`, `settings_pushes=0`, `settings_changes=0`, `cmd1e_changes=0`, `outdoor_changes=0`, `resync_delta=0`, `drop_delta=0`.

**Conclusion:** valid negative. None of the historically observed non-REQ fields, alone or in the tested combinations, is a standalone semantic trigger with `AFCA=0000`.

## EXP98 — AFC8 single-word A/B/A influence test

**Hypothesis:** isolated `AFC8=00FF` has a measurable application-layer effect when transport presence is maintained.

**Design:** 90 s A/B/A: zero-presence 20 s; `AFC8=00FF` only for 30 s; zero-presence recovery 40 s. `AFCA=0000` throughout. No semantic write target.


### Result — EXP98
A/B/A completed cleanly. AFC8=00FF alone caused no detectable application-layer response. 81 0x06 polls and 81 TX were completed without refusals; no controller, RSP02, 0x06 write-bank, 0861, settings, CMD1E or outdoor-state changes were observed. Negative result recorded.

## EXP97 — Passive natural A80E/AFDC edge correlator

**Hypothesis:** natural A80E/AFDC transitions correlate with another controller/outdoor-unit state rather than DCM-session establishment.

**Design:** 600 s passive observation, no TX, no cold boot requirement. Every A80E or AFDC edge produces a compact multi-layer snapshot of `A80C..A812`, `A7F8..A806`, `AFDC..AFE0`, `0861`, `0x1E 0000..0008`, and outdoor-state.


## EXP97 — Passive natural A80E/AFDC edge correlator — result

**Hypothesis:** natural A80E/AFDC transitions correlate with another known controller/outdoor state rather than DCM-session establishment.

**Observed:**
- baseline `A80E=0028`, `AFDC=0010`, `0861=0000`, outdoor=`0010`;
- +71.278 s: `A80E 0028 -> 0020`;
- +72.340 s: `A80E 0020 -> 0000`;
- +74.995 s: `AFDC 0010 -> 0000`;
- all three event snapshots had identical `0861`, outdoor, `CMD1E`, and paired `RSP02`;
- experiment was passive: no 0x06 response, no REQ, no TX.

**Conclusion:** A80E/AFDC are not reliable DCM-session-success indicators. The specific monitored controller/outdoor fields did not explain the natural transition.

**Negative result recorded:** no direct edge correlation with `0861`, outdoor state, CMD1E, or paired RSP02.

## EXP96 — Cold-boot historical envelope + canonical REQ/ACK handshake

**Hypothesis:** the historical envelope gains semantic meaning only in the true cold-boot EXP95 context.

**Observed:**

- canonical transaction completed;
- `0861 0->16` after 367 ms;
- REQ deasserted with payload stable;
- `0861 16->0` after 1196 ms;
- `handshake=1`; `06polls=112`; `tx=112`; `refused=0`;
- `ctrl_changes=3`; `rsp02_changes=0`;
- `settings_pushes=0`; `settings_changes=0`;
- no higher-layer application/session transition.

**Conclusion:** valid negative. Cold-boot context does not rescue the historical envelope. The missing layer remains the DCM03 semantic/init serializer.

**Additional passive observation before ARM:** `A80E 0x28->0x20->0x00`, followed by `AFDC 0x10->0x00`, occurred naturally with no EXP96 TX. This is recorded as evidence that these fields participate in broader controller-state propagation.

## EXP95 — Cold-boot zero-presence from first 0x06 poll

**Hypothesis:** syntactic DCM presence from the first cold-boot `0x06` poll is sufficient to move the controller away from EXP94's stable waiting state.

**Observed:**

- complete `120000 ms` run;
- `frames=1133`; `06polls=112`; `tx=112`; `refused=0`;
- `06_min_ms=638`; `06_max_ms=1503`;
- boot state still followed `A80E 0->8->0x28`, `A80F/A810 5->10`, `AFDC 0->0x10`;
- `0861_final=0000`, `0861_changes=0`;
- `settings_pushes=0`, `settings_changes=0`;
- `outdoor_state_changes=0`;
- `resync_delta=1`, `drop_delta=0`.

**Strong conclusion:** zero-presence proves transport/presence and triggers fast cadence, but does not establish/advance the DCM application session. `AFDC=0x10` therefore cannot simply mean “accessory absent.”

**Negative result recorded:** syntactic presence alone does not advance the cold-boot integration state.

## EXP94 — Passive cold-boot + initial-sync timeline

**Hypothesis:** a real controller cold boot exposes a reproducible 0x06 accessory/integration startup or sync sequence that precedes semantic DCM03 operation.

**Observed facts:**

- bus silence confirmed after 5049 ms; first resumed valid frame after 11540 ms silence started capture;
- +717 ms: `A80C..A812=0040,0000,0000,0005,0005,FFFF,0000`;
- +1758 ms: `A80E 0->8`;
- +2846 ms: `A80E 8->40 (0x28)`;
- +1038 ms first 0x06 poll: `AFDC..AFE0=0000,0000,0000,0000,0019`;
- +5575 ms second 0x06 poll: `AFDC..AFE0=0010,0000,0000,0000,0014`;
- `A80F/A810` returned from 5 to 10 at about +11.3 s;
- no later DCM/integration transition occurred during the full 600 s window.

**Summary:** `frames=5185`, `06polls=140`, `06_min_ms=4086`, `06_max_ms=4537`, `ctrl_changes=3`, `rsp02_changes=1`, `0861_changes=0`, `settings_pushes=0`, `settings_changes=0`, `outdoor_state_changes=0`, `resync_delta=1`, `drop_delta=0`.

**Strong conclusion:** unanswered cold boot settles quickly into stable `A80E=0x28 / AFDC=0x10 / A80F=A810=10`; the historical A80E/AFDC 0x20 cycle is not ordinary cold-boot initialization.

**Unknowns:** exact meanings of A80E bits 0x08/0x20 and AFDC 0x10; whether a real DCM response advances this state.

## External evidence before EXP93

Commit `piotr-romanowski/thermia-bus-sniffer@b4c27157402c49624917d523e016b249cdfc4e11` independently confirmed transmit-side room-setpoint control through slave 0x0A response register B3B1/46001 on iTec Eco. This matches our passive mapping and changes the highest-value next experiment.

## EXP93 — Passive A80F=50 discriminator

**Hypothesis:** the historical A80E/AFDC 0<->0x20 cycle is gated by controller state and appears while A80F=50.

**Observed:** correctly armed in two captures, but A80F remained 10 and no EXP93 trigger/summary occurred. The 180 s observation phase never began.

**Conclusion:** untriggered/inconclusive, not negative. Superseded as immediate priority by EXP94.

## EXP92 detailed record

Hypothesis: a completed four-phase transaction initializes hidden state needed for the old A80E/AFDC cycle.

Observed:

- baseline stable
- historical envelope preloaded
- REQ asserted on SHORT
- 0861 0->16 after 401 ms
- REQ deasserted while payload held stable
- 0861 16->0 after 1031 ms
- 90 s observation completed
- 84 observation replies
- A80E changes: 0
- AFDC changes: 0
- settings changes: 0
- parser resync delta: 0
- RX drop delta: 0

Conclusion: a single completed transport transaction is not sufficient to start the historical online-state cycle.

| Experiment | Purpose | Result |
|---|---|---|
| **EXP99** | Historical-field matrix, REQ low | **COMPLETED NEGATIVE.** Ten phases completed; no controller/0861/settings/CMD1E/outdoor effect; parser/drop deltas zero |
| **EXP98** | AFC8 single-word A/B/A influence | **COMPLETED NEGATIVE.** AFC8=00FF alone had no detectable effect; 81 polls/81 TX, no controller/0861/settings/CMD1E/outdoor changes |
| **EXP97** | Passive natural A80E/AFDC edge correlator | **COMPLETED.** Natural `A80E 28→20→0`, then `AFDC 10→0`; no ESP TX; 0861/outdoor/CMD1E/RSP02 unchanged at all three edges |
| **EXP96** | Cold-boot historical envelope + canonical four-phase REQ handshake | **VALID NEGATIVE.** Handshake completed (`0861` high after 367 ms, low 1196 ms after deassert); no controller/session/settings progress |
| **EXP95** | Cold-boot zero-presence from first 0x06 poll | **VALID NEGATIVE.** 112/112 responses; cadence accelerated to 638..1503 ms, but `A80E=0x28`, `A80F/A810=10`, `AFDC=0x10`, `0861=0`; no settings changes |
| **EXP94** | Passive cold-boot + initial-sync timeline | **COMPLETED.** Boot sequence: A80F/A810 5→10, A80E 0→8→0x28, AFDC 0→0x10; then stable for 600 s; 0861 unchanged; no settings changes |
| EXP93 | Passive A80F=50 discriminator | Armed in two captures but A80F=50 never occurred; observation window never started; NOT a negative result |
| **EXP92** | Completed four-phase 03E8 handshake, then historical REQ-low envelope 90 s | **VALID NEGATIVE. ACK high after 401 ms, ACK low after 1031 ms; 84 observation responses; A80E/AFDC stayed 0; no setting/error changes** |
| EXP91 | Historical 00FF,1,REQ-low,1 envelope 90 s | Negative; 84 responses; no A80E/AFDC/settings/errors |
| EXP90 | Correct persistent 00FF 90 s | Negative; 84 responses |
| EXP89 | Intended persistent 00FF | Invalid due response-buffer bug |
| EXP88 | Fixed all-zero presence 180 s | Negative |
| EXP87 | Zero presence | Invalid/short guard stop; no semantic edge beforehand |
| EXP86 | 30-minute passive first-edge capture | No A80E/A802/AFDC edge |
| EXP85 | Passive DCM source correlator | No source edge during capture |
| EXP84 | Passive room-setpoint correlation | AFDC..AFE0 unaffected |
| EXP77-83 | HE payload/envelope/layout variants | No semantic response/write |
| EXP76B | Canonical four-phase handshake | PROVEN |
| EXP74-75 | Persistent candidate register image | No write; ACK follows REQ level |
| EXP73/73B | Passive/manual curve correlation | Curve changes do not announce through AFDC/A80E |
| EXP72 | Natural AFDC/A80E state + bare 03E8 | Transport behaviour confirmed |
| EXP71/71B | Apparent promotion / zero replies | Promotion later identified as natural controller behaviour |
| EXP70 | Repeated zero responses | Fast cadence only |
| EXP68-69B | Raw 12-word settings block variants | No setting change |
| EXP67 | Post-close 03E8 on first FAST-LONG | No second ACK |
| EXP66 | HE-like GET 440C | Handshake only; no semantic response |
| EXP63-65 | Structured register/value layouts | Transport ACK only; no setting write |
| EXP62 | Selector 03E9 after established session | No ACK |
| EXP61 | Later valid SHORT 03E8 | ACK repeats |
| EXP60 | Same 03E8 on LONG vs SHORT | SHORT phase matters |
| EXP59 | Zero stage then SHORT 03E8 | ACK; 00FF unnecessary |
| EXP58 | Bare 03E8 at wrong/normal-long phase | Fast cadence; no 0861 ACK |
| EXP57 | Bare 03E8 | ACK works |
| EXP56B/C | 03E8 with word3 variants | ACK independent of simple word3 value |
| EXP55 | word2=04A6 | No ACK |
| EXP54 | word2=03F4 | No ACK |
| EXP53 | word2=440C | No ACK |
| EXP52 | 00FF,1,03E8,1 envelope | ACK; no setting write |
| EXP51 | Single presence-like response | Cadence/state only |
| EXP50 | Passive DCM audit | Recurring structure mapped |
| EXP48-49 | Presence/multi-poll sequencing | Fast-cadence/state behaviour refined |
| EXP43+ | Active 0x02 probes | No final semantic write path |
| EXP35-42 | Passive mapping | Useful telemetry; no write path |
| EXP30-31,33 | Outdoor-related probes | No semantic write discovered |
| EXP29 | Passive correlator | Diagnostic only |
| EXP21-28 | Test trailing words/selectors/counts as setting-write encoding | Negative |
| EXP10-18 | Identify 0x06 response field responsible for controller ACK | word2/AFCA=03E8 in correct phase is decisive |