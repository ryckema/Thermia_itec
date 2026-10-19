# V5DCM49 — local post-gap RX cohort reaches terminal historical witness (2026-10-19)

> **Later provenance clarification (2026-10-19):** User explicitly confirmed causing the 10,351ms V49 interruption by manually switching the Thermia OFF and ON. The callback gap + CRC return + cold-pattern and unanswered native FC23 series are therefore **manual intervention anchored**. The precise electrical main-controller rail, hardware frame EOF, physical sender/owner and exclusive native TX slot **remain unmeasured**. Source/cross-version/03E8 offline follow-up: [V5DCM50 audit](V5DCM50_POSTGAP_PROVENANCE_PAGE_LIFECYCLE_OFFLINE_RESULT_20261019.md). Earlier “physical cycle unconfirmed” text records the state of knowledge when that paragraph was originally written and is superseded **only on the user-intervention provenance point**.

**Experiment ID:** `V5DCM49-POST-GAP-COHORT-DEVICE-01`. **RESULT: COMPLETE / POSITIVE (RX-only evidence goal ONLY).** Previous RUNNING / PARTIAL 19:21–19:24 capture is now closed by the next local XTR capture. This is **not native DCM response/Online success** and **not a test of recovering V47's orphan-17 case**.

## Provenance and controlled scope

User uploaded `Pasted text(20261019-174122).txt` and `Pasted text (2)(10).txt`; **byte-identical**, each 5000 ESPHome API lines, SHA256 **46241b6397071f66385c920a6ee155cc5d256c4f5f3390f9f0c0296737eb5971**, sample window **19:38:02.692–19:41:15.967** (approx 193 seconds). Both refer to the same deployed V49 RX-only session with 10,351ms callback gap already captured at 19:23:58 by the earlier 19:21–19:24 log (SHA256 8a2da9ce5079c5008bec527ccac2720d3cc2acc9739f31668b26a9a568812dea). Do not double-count as two independent observations or two controller restarts.

**Hypothesis:** after a >=5s callback interruption, V49's separate bounded software clean RX cohort will collect >=50 good post-anchor frames across >=30s with RAW/V5 agreement, freeze `RX_SHADOW_RECORDED` without clearing historical faults or enabling output. Known-good V49 passively deployed baseline + native software build locked (`TX=HARD_DENY`); single controlled observational change = wait for a natural interruption, no bus response. Earlier V47 observed orphan17/+17 resync, B11D sticky, native requests but TX0; V48 host replay predicted the mechanism. This V49 interval had **oldResync=0**.

## OBSERVED FACTS — local XTR

- First 19:38:05.827 periodic `[V5DCM49]` reports `phase=RX_SHADOW_RECORDED reason=NONE gapMs=10351 oldResync=0 frames=285 batches=128 ageMs=30532 B11D_history=0 P5_history=0 TX=HARD_DENY owner=UNKNOWN`. Textsensor at 19:38:07.450 independently displays the same frozen terminal state with `newFrames=285`. Seven periodic source logs through 19:41:05 and 38 text-sensor readouts through 19:41:12 retain identical terminal snapshot; freeze is intentional, not inactivity of the main receiver.
- Earlier partial 19:24:27 had `CLEAN_COHORT newFrames=270 batches=124 ageMs=29091`; the newly observed terminal snapshot has exceeded 30 seconds (`30532ms`) and 50 good frames. Terminal transition occurred after the prior capture and before the first sample of this new one; **exact transition timestamp not captured**.
- Continuous live receiver health during this 193s follow-up: V5 parser `frames=12282 -> 13898`, `resync=0 drops=0 badGeom=0 unknown=0 TX=0`; B11C portable equality and public CRC `crcMismatch=0`, ending at 13844 checked frames (periodic sampling); B11D last `rawFrames=portableFrames=comparedV5=13840`, countDiff/byteDiff/incomplete/ambiguous/overflow/fault all zero, `Bridge 11D First Fault=NONE`. FIX2 persists `QUALIFIED current=1`, first witness frames12319, last13895, reason NONE.
- Native `0x0F FC23` request counter is **63 at first and last samples of this follow-up**, `[V5DCM19] NATIVE_OBSERVE challenge=63 responseShape=0`, P74E FC23=63, R6-P30EC `REQUEST_OBSERVED_NO_LOCAL_TX req23=63 peerRspShape=0`. Prior 7 requests by 19:24:25 were part of an eventual 63 counted before 19:38. This new file supplies **no new FC23 request transition** and **no native reply**.
- `V5DCM44B` remains `step=7 deny=1 armClicks=0 replyAttempts=0 uartAttempt=0 admitted=0 build=0 DE_RX=1 conflicts=0` (same earlier build-locked Arm denial, **not a new Arm in this recording**). Final `V5 TX-02 HARD_DENY candidates=2311 denied=2311 physical_attempts=0`; all physical output counters zero. Owner/epoch/wire EOF/sender/response slot continue UNKNOWN. `R6 P24` reports `COLD_PATTERN_HISTORY_STALE / EPOCH_UNKNOWN / NO_TX`; physical power-cycle for V49 unconfirmed.
- Normal HA real-time room/outdoor/supply/DHW temperatures are present. Several heating settings such as curve/min/max are `nan`, and `HA Restore 0x0F 03E8 pages Received` stays zero in this follow-up, despite broad known `0x0F` page updates. **Separate telemetry/data-presence caveat**; causes and future recovery of these particular entities untested. No claim that all production entities are healthy.

## Interpretation / scope

**PROVEN locally:** V49 on XTR reached and retained a frozen RX-only post-gap `RX_SHADOW_RECORDED` witness after **285 new CRC-validated matched frames in 128 batches over 30.532s**, with original parser/raw CRC integrity zero faults and TX disabled. The passive 30s clean-cohort objective is COMPLETE / POSITIVE.

**STRONGLY SUPPORTED:** clean software anchor and original RAW/V5 frame parity after the observed callback gap. The terminal witness is **historical RX evidence only**, not authorization for future TX.

**OPEN/UNKNOWN:** no empirical recovery of **V47 orphan17/+17-resync + sticky B11D** in this V49 session; physical controller switch, electrical epoch, wire EOF, sender/owner, physical response slot, native FC23 acceptance, C2/Online remain unknown. 63 requests without a reply do not demonstrate a functional DCM session. No automatic relaxation/clearing of P5/B11D/FIX2 safety latches.

## Status and recovery

- `V5DCM49-PASSIVE-BASELINE-01`: COMPLETE / POSITIVE (previous result).
- `V5DCM49-POST-GAP-COHORT-OFFLINE-01`: COMPLETE / POSITIVE (host/source only, previous result).
- **`V5DCM49-POST-GAP-COHORT-DEVICE-01`: COMPLETE / POSITIVE (local RX-only terminal witness)**.
- `V5DCM47-LIVE-ONE-SHOT-01`: remains COMPLETE / INCONCLUSIVE (native physical TX=0; fault cause separate). No retrospective reclassification.
- Abort condition for any future active test: new B11D/P5 faults, RX gap/partial, owner/slot unknown unless explicitly scoped safe test, unexpected UART/DE. Current V49 hardware output is compile-locked; no new Arm, forced controller restart or transmission.
- Rollback if later observed runtime instability: return to last VERIFIED stable RX-only production variant, preserving historical diagnostic and fault observations; no automatic release.

**NEXT ACTION:** use existing captured event timing and available native firmware for **offline receiver/ownership/epoch/slot provenance analysis**, explicitly separating software callback gap from physical wire EOF and absent responses; review missing settings page `0x03E8` independently before claiming telemetry health. Do not propose another live power cycle/Arm to merely reproduce the terminal proof. New controlled TX would require a separately scoped, bounded experiment.
