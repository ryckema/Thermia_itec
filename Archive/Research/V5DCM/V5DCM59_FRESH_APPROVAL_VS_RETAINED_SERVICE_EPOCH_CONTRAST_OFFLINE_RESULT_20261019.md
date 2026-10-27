# V5DCM59 — Fresh native approval, initial sync readiness and retained status service

**Experiment ID:** V5DCM59-FRESH-APPROVAL-VS-RETAINED-SERVICE-OFFLINE-01
**Status: COMPLETE / POSITIVE (OFFLINE SOURCE + ARCHIVED-RAW EPOCH RECONCILIATION ONLY).**
**Date:** 2026-10-19. No live TX/flash/compile, controller restart, HA/source change, native 0x0F security implementation or executable 0x0708 mailbox tool.

## Research scope, baseline and controlled action

**Hypothesis:** fresh native session approval, initial settings ACK readiness, and retained status-service activity are separate observable phases. Previous completed PROTO-OFFLINE-17 (positive) and PROTO-OFFLINE-18 (negative) may already resolve the new-versus-retained distinction, so reverify their evidence against direct raw Eco5 captures and current XTR V49 without repeating physical tests.

**Source of truth:** ORIGINAL Connect 2.0.18 and 2.1.105 firmware govern intended slave/software behavior (V54–V57); local raw XTR experiments prove what happened on local bus; archived genuine/collaborator Eco5 proves Eco5 behavior only. Write Beta v4.1 is historical XTR inspiration rather than the authority on the original Connect application.

**Known-good live baseline unchanged:** V49 RX-only/HARD_DENY native TX0; user-confirmed manual controller OFF/ON produced 10,351ms RX callback gap; 285 clean matched frames/30.532s post-gap; no new B11C/B11D faults, strict source 03E8/count14 or 0864/count4 not observed; native status polls0 and FC16 ACK replies0. Historical local XTR V23 RX-only 03E8 present in another epoch; V47 native one-shot COMPLETE / INCONCLUSIVE, TX0. Historical EXP388 RUNNING / PARTIAL preserved.

**Prior relevant work:** [PROTO-OFFLINE-17](../temp/PROTO_OFFLINE_17_APPROVAL_SYNC_READINESS_REDUCTION_20261003.md) already classified six successful/one failed Eco5 boot and two approval/sync gates; [PROTO-OFFLINE-18](../temp/PROTO_OFFLINE_18_SYNC_READINESS_DISCRIMINATOR_20261003.md) already searched 25 families and found NO unique readiness discriminator; [S11Y-AA..AD](../protocol%20reduction/S11Y_AA_AD_PASSIVE_SESSION_RECONCILIATION_20261008.md) reported the historical retained local S11T native 0662-ACK→0708 transition. V55–58 already verified CRC, 8-byte ACK pairing and status-vs-ACK negative controls. None are promoted to new live experiments here.

**One controlled change:** offline metadata replay of seven PRE-EXISTING, originally documented Eco5 boot windows using the previously identified controller bus-return anchors, comparing native FC23 request/reply-envelope, native FC16 03E8 request/strict paired 8-byte ACK and first native FC03 0708 poll. Then independently recheck the two distinct V49 user console excerpts for 0662 and 0708 counters, plus controller-gap / FC23 bounded provenance. Original firmware source is referenced for distinct slave H2, ACK, info request and profile gates; we do NOT guess the controller-master code. **No TX target, address, payload, register mutation or expected physical effect** (analysis only). Positive if strict envelope chronology and V49 negative controls independently match; negative if CRC/source conflict, inconsistent epochs or +120s without approval producing sync; inconclusive if master internal scheduler, electrical owner, physical EOF/slot or actual V49 rejection cannot be proven. Abort on invalid evidence; no physical recovery needed.

## Actual raw-record reconciliation

The seven Eco5 windows are partitions of the same two previously inspected CRC-valid genuine/collaborator recordings, Sep26 and Sep28. This audit does NOT create fresh first-hand XTR results. Match a 03E8 ACK to the preceding exact 03E8 start/count inside **300ms analyst-only window**; host-timestamp gaps must NOT be treated as a wire response deadline.

| Eco5 epoch | Bus return (recording s) | First FC23 reply-shape since return | First paired 03E8 ACK since return | First 0708 poll since return | Result |
|---|---:|---:|---:|---:|---|
| Sep26 #1 | 183.462 | +120.153s | +120.290s | +158.393s | approval then sync/runtime |
| Sep26 failed middle | 393.774 | NONE | NONE | NONE | 41 FC23 challenges, no transition through ~171s |
| Sep26 #2 | 603.478 | +119.808s | +119.930s | +186.828s | approval then sync/runtime |
| Sep28 #1 | 193.555 | +120.173s | +120.296s | +158.359s | approval then sync/runtime |
| Sep28 #2 | 438.000 | +9.825s | +118.478s | +154.280s | early approval, delayed service |
| Sep28 #3 | 734.310 | +10.043s | +118.550s | +158.668s | early approval, delayed service |
| Sep28 #4 | 974.803 | +119.914s | +120.038s | +158.132s | approval then sync/runtime |

**Host metadata checks: 12/12 PASS**, including 6 successful / 1 failed windows, 2 early/4 late reply envelopes, all six successful first paired 03E8 ACKs at +118–121s, all six first 0708 polls LATER than the first 03E8 ACK, failed window with no 03E8 or status polls, and V49 native0662/status count0 in both distinct sampled console intervals. Private offline-only audit script SHA256 8c7064d7d792f89907ddda447f6fa2e167be6316a93380bfdeeab233e5c863b4; metadata SHA256 0555511ba362a4bcc4ba88ea41254fe428309b7c48526601d1d6de6462986d93. CRC-good FC23 reply shape is a bus envelope; controller subsequent progression makes acceptance strongly supported in those episodes, but cryptographic content is not published or retested.

**Small correction to the old PROTO-OFFLINE-17 count:** In BOTH early Sep28 epochs there are **102** FC16 03E8 requests timestamped before the FIRST matching 03E8 ACK, INCLUDING the final *ACKED* request. Therefore **101 prior requests are unacknowledged**, then the 102nd receives the first ACK. Verified first ACK pairing: historical t556.416→556.478 (+62ms logged), and t852.829→852.860 (+31ms logged). Previous text calling 102 *prior unACKed* requests is OFF BY ONE. This corrects description, not immutable raw history nor the substantive two-gate conclusion.

**Original PROTO-OFFLINE-18 COMPLETE / NEGATIVE retained:** exhaustive prior reduction checked 25 data-bearing families; no universal value transition within 10 seconds before the first 03E8 ACK in six successful windows. A failed Sep26 boot passes +120s with essentially the same recurrent A80C/AFDC/04A6/085F/controller process signatures but never receives native approval or proceeds to 03E8. Time alone and any of those words do NOT establish a universal readiness condition. The approximately 120s Eco5 gateway/session timing must NOT be programmed as a mandatory local XTR controller delay: older locally successful XTR tests did not require it. This is not a new field search, and the earlier negative finding remains historically intact.

## Separately observable historical local retained service

Existing [S11Y-AA..AD](../protocol%20reduction/S11Y_AA_AD_PASSIVE_SESSION_RECONCILIATION_20261008.md) records historic **S11T locally COMPLETE / POSITIVE** in its scoped retained 0662/count33 +085F(0800) context: a single ACK of 0662 was followed by native 0708 poll about 1.422s later. Other S11 captures observe 085F+0708 without 0662 inside *bounded logs*. The earlier session owner and epoch remain unknown. 0662 is **not** a proven mandatory prerequisite for status polls; this is a supporting retained-session route, not an original Connect handshake replacement.

**New direct V49 source/log negative control:** in original first V49 user console 19 samples of NSH W 0662 Count and NSH S8 Mailbox Polls remain zero; in the later DIFFERENT user console 20 samples of each remain zero: **39/39 0662 seen=0; 39/39 0708 native status polls=0** (byte-identical duplicate of second log excluded). Meanwhile recurring source FC16 04A6/13 and 085F/5 continue.

After logged 10,351ms callback gap at19:23:58.308, first canonical native FC23 request appears19:23:59.657, then six more through19:24:25.066 at intervals ~4.1–4.5s. No actual native reply observed/delivered. At start of later console 19:38 native FC23 cumulative count is **63**, unchanged through19:41. **The 13+ minute log gap between segments is NOT continuous evidence** for exactly when or how the counter reached63; a single uninterrupted 63-challenge controller epoch and a particular controller timer remain UNPROVEN. Hardware/controller power OFF/ON is user-attested; serial callback gap does NOT independently establish exact electrical EOF/owner.

## Conservative three-route classification, without speculative master logic

1. **FRESH APPROVAL→SETTINGS-SYNC (Genuine Eco5 corroboration):** canonical FC23 challenge, reply-shaped successful response, first 03E8 controller request, distinct first FC16 03E8 ACK, later 03FC/bootstrap, later runtime/status polls. The original CM930 software H2 state, Connect info/version profile, package wait and real Online are DIFFERENT axes.
2. **RETAINED WORK→STATUS SERVICE (Historical local XTR):** previously established context with 0662/085F or 085F+0708 may continue status service without fresh FC23 within a bounded sample. Does not prove approval is dispensable at initial startup or identify current native owner.
3. **CURRENT V49:** correctly label **CHALLENGE_OBSERVED_NO_LOCAL_RESPONSE / NO_INITIAL_SETTINGS_OR_RETAINED_STATUS_SERVICE_IN_SAMPLED_WINDOWS / EPOCH_UNPROVEN**. Not a proven controller rejection; not enough bus evidence to select whether approval stage, slave presence, ownership, response slot or master scheduler prevents 0708 and 03E8.

**PROVEN original firmware scope:** two independent handshake/FC16 ACK and application version/group gates (V54–57), but slave software does NOT disclose controller-master admission algorithm. **PROVEN archived cross-model:** six approved then eventually 03E8 ACK and 0708 versus one 41-challenge/no-approval/no-sync negative control, with count correction. **PROVEN current local V49:** 04A6+085F continuing, no confirmed initial settings sync nor retained 0662/0708 within sampled windows, no native TX. **STRONGLY SUPPORTED:** distinct fresh approval and subsequent service-ready stages and a separate retained native service path. **DISPROVEN / SUPERSEDED:** +120s alone ensures readiness (prior PROTO17/18), every FC16 ACK is mandatory before subsequent 0708 poll (V58), historic 102 earlier *unACKed* count (now101 prior to the matched request).

**OPEN:** exact current XTR master-side gate, sender/owner/electrical EOF/exclusive response slot, real current controller firmware register0867, Online/native semantic acceptance, why present V49 lacks 03E8/0662/0708, and original Eco5 gateway-internal reason for the ~120s boundary. No protected approval/0x0708 tooling, unsolicited TX or speculative register writes.

**NEXT (evidence-led, NO DEVICE ACTION):** do not repeat PROTO17/18 or S11T. If an actual NEW naturally occurring controller episode or fresh raw XTR data is ever captured, distinguish FC23 request/reply, first 03E8 request/ACK and 0662→0708 retained path with independent timestamp/provenance axes. If no new episode, preserve OPEN rather than invent a gate. Any future active scope still requires separately established physical sender/owner/slot, exact target and payload, bounded fail-closed response, abort and recovery before user-initiated execution. V49 remains output hard-denied and all production HA, red/brown logs and sticky fault bookkeeping unchanged.
