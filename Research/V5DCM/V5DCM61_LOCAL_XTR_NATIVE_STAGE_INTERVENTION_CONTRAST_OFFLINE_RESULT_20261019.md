# V5DCM61 — Local XTR approval, synchronization, and retained service: documentary intervention contrast

**ID:** V5DCM61-XTR-INTERVENTION-LADDER-OFFLINE-01
**Date:** 2026-10-19
**Status: COMPLETE / POSITIVE (OFFLINE HISTORICAL EVIDENCE RECONCILIATION ONLY).** The positive result concerns the controller's observable stage transitions, not original Online application acceptance or current TX readiness.

## Hypothesis and scope
A single evidence table from prior controlled local XTR experiments can isolate the observable transitions between: unanswered native approval; one bounded response without FC16 ACK; one ACK per newly observed settings page; and a fully served historical native runtime. Original Thermia Connect 2.0.18 and 2.1.105 software must be treated separately from XTR-master bus behavior. This is a source/document audit of already COMPLETE experiments, NOT new raw replay, source compilation, physical transmission, full device power verification or new firmware research.

**Last verified live baseline:** V49 RX-only/HARD_DENY, manual Thermia OFF/ON user-attested, 10.351s receive-callback gap, 285 clean post-gap frames over 30.532s; native UART TX0. Seven first FC23 challenges with no response, later cumulative 63 with >13 minutes of missing console continuity; sampled 03E8/0662/0708 absent, recurring 04A6 and 085F. V47 one-shot remains COMPLETE/INCONCLUSIVE with TX0. Preserve all production HA, Configuration, red/brown diagnostics and sticky RX guards.

**Prior work:** EXP248/249/251/254, EXP255, EXP252/256/257/258, EXP355/386/387 and EXP388; R6-P74DA and G01; V5DCM53/54/56/57/59/60. Do not repeat their tests or supersede negative/partial observations.

**One controlled offline change:** compare the canonical original EXP355/386 result sections with the original completed EXP254–258 timelines, then cross-check against previously verified original Connect software findings. Targets purely observed 0x0F FC23 request shapes, native FC16 first pages 03E8/14, 03FC/11, 0410/22, later 06F4/19, and FC03 0708/6. No outbound slave/address/payload/physical effect, no recovery action. Positive = internally consistent counterfactual stages supported by user-run original experiments; negative = contradiction; inconclusive = missing continuous original raw or controller code. Stop on source conflict or private implementation leakage.

## Direct local XTR intervention ladder

| Earlier experiment | Scoped native endpoint activity | Observed controller outcome |
|---|---|---|
| EXP254 COMPLETE/POSITIVE | Passive after user controller OFF/ON; TX disabled | 63 approval requests, first +1.283s, last +265.086s; no FC16 0870/17 ACK or FC03 0708/6; parser/drop0 |
| EXP255 COMPLETE/POSITIVE | Full 7-minute passive RX-only native 0x0F census | 63 approvals, first +1.284s, last +265.513s; FC16 582 = 04BA/22 x4 + 04A6/13 x383 + 085F/5 x195; FC16 ACK0, FC03=0; 219 FC16 requests after last approval; errors0 |
| EXP256 COMPLETE/POSITIVE | Exactly one historical approval response, NO later FC16 ACK/FC03 response | One approval/no later retries; first native 03E8/14 at +124ms after response (+1.369s post-BUS_RETURN), 389 repeated 03E8/14 requests without ACK (median ~1.308s); 04A6/085F=0, other FC16 04BA x1 pre-response; FC03=0. Reproducible DHW-side 0 / COMM. ERR ONLINE/LINK from incomplete service |
| EXP257 COMPLETE/POSITIVE | Same prior qualified response plus ONE 03E8/14 ACK | First next 03FC/11 after ~691ms, deliberately no 03FC ACK |
| EXP258 COMPLETE/POSITIVE | Same prefix plus ONE 03FC/11 ACK | First next 0410/22 after ~1.501s; deliberately no 0410 ACK; same incomplete-endpoint UI/alarm side effects |
| EXP355 COMPLETE/POSITIVE | Previously qualified retained stage40, user controller power-cycle with ESP staying on; one guarded response, full known ACK chain and status service | BUS_RETURN 00:51:29.662; one response 00:51:31.005; ordered 32/32 settings chain finishes at 06F4/19 00:52:03.257 (33.595s post-return; 32.252s post-response); 085F ACK then native 0708; RECOVERY_POSITIVE 00:52:04.887. No semantic write exercised IN EXP355 |
| EXP386 COMPLETE/POSITIVE | Guard-mismatched pre-reboot challenges NO_TX; user restart; one guarded response; complete historical ACK/runtime service | 32/32 complete, then 085F ACK and 0708 idle response; clean parser; not an independently timing-resolved clone of EXP355 |

**Arithmetic consistency:** 4+383+195=582; 1+389=390; EXP355 timed bus-return-to-last-bootstrap 33.595s and response-to-last-bootstrap 32.252s. Checks concern archived report figures, NOT independent byte-by-byte CRC replay of full original EXP355/386 logs, which were not supplied to this audit.

## Findings by provenance

**OBSERVED LOCALLY, PROVEN WITHIN EXPERIMENT SCOPE:** No-responder new-XTR-session branch exhausts 63 approvals while regular 04A6/085F FC16 traffic continues. In the controlled one-reply run, approval retries stop and the controller sends 03E8/14 ~124ms later; without FC16 ACK the page repeats. A single exact ACK of 03E8 yields 03FC, another exact ACK yields 0410. The older fully serviced sessions reached a full native initial-sync chain and runtime status service; EXP355 final 32/32 ACK occurred within 34 seconds of logged bus return, disproving a universal ~120-second first-ACK requirement on local XTR. These are stage transitions, NOT proof an arbitrary response passes original native authentication.

**CONTROLLED LIMIT:** EXP355 starts from a *previously qualified* retained runtime before user intervention, whereas EXP254/255 start in other passive sessions. Thus the entire EXP355-versus-EXP255 difference is NOT one randomized isolated-variable experiment. The *closest* isolated transitions are EXP255 -> EXP256 for one bounded response, and EXP256 -> EXP257 -> EXP258 for first-page ACKs. Historical logs are ESPHome diagnostics, not independently witnessed electrical owner/EOF/slot. The original local R1 material is confidential and is deliberately not reproduced.

**ORIGINAL CONNECT FIRMWARE-DERIVED:** 2.0.18/2.1.105 CM930 implements logical slave0F and separates FC16 ACK, internal H2, information/version collection and operation/runtime. V5DCM56 host checks found 04A6 or 03E8 CAN trigger internal H0→ACCEPTED / version info request even WITHOUT prior FC23; 04BA and 085F are excluded as initiating pages. This software predicate does not force the physical XTR master to issue 0708 polls. 2.1.105 2.4.2 source JSON needs 33 significant groups (W2=15,W3=10,W4=8) for its distinct application tracker; historical Write Beta v4.1 served 32 native bootstrap ACK stages, not proof of 33/33 genuine firmware application readiness or cloud Online. V49's RX33 bitmaps are PAGE RECEIPTS, NOT genuine CM930 outbound 0708 request masks.

**STRONGLY SUPPORTED:** Distinct fresh approval challenge → native initial-settings service → later running status. The one-reply experiment is sufficient to cause the controller's *observed* initial settings scheduling change in its particular tested conditions. Sequential FC16 ACKs govern the tested first three page progressions. Genuine Eco5 archived windows corroborate but do not supersede local XTR results.

**NOT PROVEN / STILL OPEN:** Native XTR controller-master general admission algorithm, current V49 0867/version or electrical sender/slot/EOF, full Connect application/profile/Online onboarding, or whether an original CM930-style 04A6 info request can be serviced when current V49 has no observed 0708. The incomplete one-response runs produced a reproducible communication alarm; do not repeat them by default.

## Decision and next action

There is **NO need** for another identical seven-minute passive restart, another one-response 03E8/ACK experiment, or an invented +120s timer. Continue prioritizing ORIGINAL Connect 2.0.18/2.1.105 application compatibility and verified controller-master admission evidence. The earliest locally observed post-response stage is already solved; complete original 33-group app behavior and the physical TX safety/ownership envelope remain separate. Do not alter V49, send native FC23 replies/FC16 ACKs, disclose original protected material, restart the controller or clear fault guards from this offline finding alone.
