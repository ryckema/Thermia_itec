# CURRENT HANDOFF — V5DCM28 2026-10-18

Live user-flashed **V5DCM23 FIX2: RUNNING / PARTIAL RX-only**, first short log 1/33 strict page groups and clean RX, no FC23 captured, native TX HARD_DENY. Latest **V5DCM28-EPOCH-GUARD-01 COMPLETE / POSITIVE for OFFLINE host tests only**: one inert V5DCM27 source reselect guard now refuses repeated/older controller generation *labels*, cross-tested with the real historical 20261003 FC23 and gap24a/b Fresh/Retained/Recovery metadata. No current independent actual owner/physical epoch/slot proof; proof flag in host test synthetic only; 1/33 unresolved. New ZIP is **NOT FLASHABLE**, no ESPHome/HA changes. V5DCM29 trustworthy independent-session contract PREPARED / NOT RUN; V5DCM26 15–20-minute same-FIX2 passive run also PREPARED / NOT RUN. [Source/host result](V5DCM/V5DCM28_EPOCH_GUARD_AND_LIFECYCLE_PROVENANCE_OFFLINE_20261018.md). Verify newest canonical file headings below, not older snapshots.

---



---

# CURRENT VERIFIED HANDOFF — 2026-10-18 V5DCM27

Latest user-flashed device is **V5DCM23 FIX2 RX-only, RUNNING / PARTIAL** (first ~2m25 log, actual portable ledger 1/33, clean B11C/B11D and TX HARD_DENY). Previous V5DCM20 18m33 RX-only positive is a different device build. Latest OFFLINE step **V5DCM27-SOURCE-REJOIN-01 COMPLETE / POSITIVE**: strict original-private-C++ host tests confirm native 0x0F FC23 revokes V5DCM23 package ledger and the only reselect call is on ESP boot. Further FC16 alone cannot restore the package ledger, but this has NOT happened in the current short live FIX2 log (no observed FC23). Internal CM930 handshake shadow is NOT physical owner or TX authorization. Next **V5DCM27-REJOIN-BRIDGE-01 PREPARED / NOT RUN**: source-only externally qualified profile/epoch reselect, preserve all 180 current private HA entities, TX hard deny, no extra UART, no automatic FC23 rearm. Report: [V5DCM27 source and regression](V5DCM/V5DCM27_NATIVE_REJOIN_SOURCE_AUDIT_20261018.md). Prior V5DCM26 passive 15-20min live observation also PREPARED / NOT RUN. Verify exact flashed bytes before any code change. This block supersedes older dated snapshots below only for current state.

---

# START HERE — Thermia iTec XTR M
> Compact, evidence-bound entry point for a NEW ChatGPT session. Updated 2026-10-18. This is a navigation and handoff document, NOT a replacement for the canonical evidence. Verify the latest dated canonical entries before acting.

## Standing autonomous native TX authorization (2026-10-18)
User explicitly authorizes **general, autonomous native TX** for Online/Connect/DCM development and controlled deployment: no repeated general consent per handshake or response in an already scoped and armed user-initiated experiment. This is **permission, not evidence** of protocol acceptance or electrical ownership. G01–G06 previously accepted research risks remain technically scoped; do not demand repeating them simply to continue research. The verified installed V5DCM19 FIX1/V5DCM20 device remains **RX-only/TX HARD_DENY** until a separately documented live activation; no live TX/flash occurred by changing this note. Preserve fail-closed session/CRC/owner/slot/retry and abort/rollback, confidentiality, and no uncontrolled scans/unknown ACKs/speculative writes. [Authoritative user decision](NATIVE_AUTONOMOUS_TX_AUTHORIZATION_20261018.md).

## Latest cross-project handoff — 2026-10-18
- **V5DCM21 source-derived package coverage update (2026-10-18):** 2.1.105 modern profile sensor/config 570 definitions -> 541 numeric dependencies -> **33 candidate significant groups** (W2=15, W3=10, W4=8); v31 FIX4 only tracks 13/33, so `Native Settings Pages Seen` is not C2 evidence. [Source audit, limits and CI](V5DCM/V5DCM21_PROFILE_242_SIGNIFICANT_PACKAGES_20261018.md).
- **Actual latest user-run firmware:** v31 FIX4 **read-only**, with `03E8:Y` and the other 12 native settings pages `N` at 151s; user subsequently says missing pages **still N**, without a new exact uptime or no-reboot confirmation. This is READ-V31-UNKNOWN-01 **RUNNING / PARTIAL**, NOT an active V5DCM21 trial.
- **Historical native XTR proof:** EXP325–329 owned ACKs in a qualified native session advanced `03E8→03FC→0410→042E→0442`. This supports the hypothesis that missing current-service pages can require native synchronization; it is not permission or evidence of a complete new session.
- **V5DCM21 latest:** **RUNNING / PARTIAL**; actual firmware-repo HEAD CI [39124813711](https://github.com/ryckema/Thermia_Connect_Firmware/actions/runs/39124813711) PASS, including **26 new** 2.1.105 three-mask package-readiness checks plus prior source/RX/delivery cases. W2/W3/W4 bit-to-range mapping is firmware-derived and verified; *exact significant subset* for XTR profile 2.4.2 remains unknown. [Result](V5DCM/V5DCM21_2105_PACKAGE_COMPLETENESS_OFFLINE_20261018.md).
- **Autonomous native TX** authorized by user as standing permission; accepted G01–G06 risks must not be reopened by default. No new active TX or code flash was performed by this V5DCM21 offline substep; any first autonomous deployment requires an explicitly scoped/armed test.

## First five minutes
1. Read **this file** and [CONTINUITY_WORKFLOW.md](CONTINUITY_WORKFLOW.md).
2. Read the **TOP/current sections** of [THERMIA_PROJECT_STATE.md](THERMIA_PROJECT_STATE.md), [EXPERIMENT_LOG.md](EXPERIMENT_LOG.md), and [PROTOCOL_FINDINGS.md](PROTOCOL_FINDINGS.md). These large files contain historical entries: do NOT treat every older 'LATEST' heading as current.
3. For the active experiment, read the linked experiment-specific PREPARED/RESULT report and the exact code/YAML provenance.
4. Inspect relevant [Thermia Connect firmware research](https://github.com/ryckema/Thermia_Connect_Firmware) and actual firmware files when firmware claims matter.
5. Check for newer commits/experiments than this handoff. If found, update this file; never override newer evidence with this snapshot.

## Verified handoff snapshot — 2026-10-18
- **Most recent locally confirmed live test:** **V5DCM20 COMPLETE / POSITIVE** for passive RX-only stability. User-provided log covered **18 min 33 sec**; B11C/B11D raw-vs-portable parity with zero observed count/byte differences, drops 0, **2,619 TX candidates denied and physical TX attempts 0**. Some HA values briefly NaN through natural fan/compressor transitions: semantics unresolved.
- **Deployed baseline in the latest result:** V5DCM19 FIX1, RX-only, TX HARD_DENY. Do NOT infer it has since changed without current source/log verification.
- **Next planned step:** **V5DCM21 PREPARED / NOT RUN** — *offline* TX-readiness/source/evidence audit from V4.1 plus original CM930 reference. Not approval to transmit.
- **Independent unresolved task:** V5DCM18 original Python reference-Core full fixture/stateful replay remains **RUNNING / PARTIAL**; separately bounded ZIP C++ tests/replays passed but do not close it.
- **Accepted constraints:** G01–G06 residual risks remain accepted/closed pending genuinely new evidence. Physical owner, response slot, native challenge acceptance, Online icon/cloud readiness remain unproven locally. User has **now authorized general autonomous native TX in principle** for documented/armed controller-driven integration; **authorization is not evidence of safe electrical or protocol readiness**.
- **Firmware distinction:** user ZIP portable Core and firmware-repo HEAD have differed; never transfer test validity between them without checking provenance.
- **Important evidence:** [V5DCM20 live result](V5DCM/V5DCM20_LIVE_RX_ONLY_RESULT_20261018.md), [V5DCM19 FIX1 live result](V5DCM/V5DCM19_FIX1_LIVE_RESULT_20261018.md), [V5DCM18 functional gap handoff](V5DCM/V5DCM18_FUNCTIONAL_GAP_HANDOFF_20261018.md).

## Do next
1. Check whether V5DCM21 has subsequently been prepared/performed.
2. Review V4.1, original firmware reference, current deployed code and **accepted G01–G06 research risks**; prepare qualified autonomous TX behavior without reopening these gates reflexively.
3. Keep the **currently installed** RX-only TX hard-deny unchanged until a bounded user-initiated, explicitly armed deployment/test; standing general authorization does not itself execute code.
4. After any material result, update canonical files, then refresh this handoff in the **same documentation change**. Verify commit and report SHA.

## What NOT to do
- Do not ask for a DCM module, disconnect room sensor or silently repeat rejected tests.
- Do not confuse synthetic/offline acceptance with native local confirmation.
- Do not mark PREPARED as COMPLETE; do not invent compilation, flashing or TX.
- Do not expose confidential response algorithms/private 0x0F or 0x0708 material.
