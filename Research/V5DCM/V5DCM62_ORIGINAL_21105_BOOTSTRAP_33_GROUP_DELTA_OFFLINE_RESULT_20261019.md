# V5DCM62 — Original Connect 2.1.105 33-group readiness vs locally proven V4.1 32-page bootstrap

**Experiment ID:** V5DCM62-ORIGINAL-21105-32-VS-33-SOURCE-TRACKER-OFFLINE-01
**Date:** 2026-10-19
**Status: COMPLETE / POSITIVE — OFFLINE ORIGINAL-FIRMWARE/SOURCE-TRACKER RECONCILIATION ONLY.**
No live XTR experiment, TX, ARM, ESPHome YAML edit/compile/flash, physical controller restart, new native captures, semantic register writes, controller-master admission or cloud Online validation.

## Hypothesis, baseline, previous work and one controlled change

**Question/hypothesis:** Is the original Connect 2.1.105 source-derived 33-group application data completeness only an off-by-one version of the historically functional Write Beta v4.1 local XTR 32-page controller sync, or does it represent a different source/profile-specific completeness criterion? Does the ORIGINAL software allow 32/32 alone to release parameter-map publication?

**Last VERIFIED user-installed live baseline:** V49 RX_ONLY/HARD_DENY, manual Thermia OFF/ON user-attested with UART callback gap 10,351ms, 285 clean matched post-gap frames / 30.532s, UART TX0; native 04A6/085F still observed, strict 03E8/0864/0708/0662 absent in sampled logs, seven early unresponded FC23 and cumulative63 later with >13-minute unobserved console gap. V47 local one-shot remains COMPLETE/INCONCLUSIVE TX0. All historical EXP254/255/256/257/258/355/386 statuses retained, as is EXP388 RUNNING/PARTIAL.

**Prior completed investigations not mistaken for new results:** V5DCM21-PACKAGES-02/03 grouped 33 based on original profile; V54 recomputed original 541 dependencies and tested per-receipt/publish gates; V57 confirmed original first-version same-callback seed-then-credit; V53 and V61 proved original 32/33 stages are different concepts; original local EXP355 and EXP386 documented 32/32 live bootstrap then native 0708 runtime. This V62 independently compares the *SETS*, verifies three concrete ORIGINAL bitmasks and runs new full 33-group hold/release scenarios against real ORIGINAL class/method bodies.

**Exactly ONE controlled OFFLINE activity:** source-authenticated set intersection and stage replay using genuine user-uploaded original Connect 2.1.105 extracted AppFS Python/JSON, original 2.0.18 files as source-only negative version control, and the 32 chronological page starts documented in local EXP355. Execute an isolated AST-extracted **actual original CMClientParameterUpdateState class** plus **actual original CMClient.on_publish_cm_params_map_event** with inert log/event/parser/MQTT objects, never loading the full firmware service or IO interfaces. No response generator, physical timing, UART frames, outgoing register image or cryptographic code.

**Targets:** read-only native page start *labels* (03E8..06F4, and later 07D0..0870), original internal receipt-group sets (1802/1803/1804) and parameter-map publication branch. No outbound slave/address, payload, altered plant value, transmission timing or physical effect. Positive: 32/33 overlap + actual-original 33-group tracker blocks on 32 alone and releases only after eight additional groups; negative: wrong source hash/flags/failed checks; inconclusive: physical actual current 0867/version, native owner/master action or absent live runtime groups. Abort source/hash/fixture mismatch; no hardware rollback.

## Primary provenance: ORIGINAL bytes and historic locally observed page starts

User files inspected directly in the local runtime:
- `2.1.105 extracted_appfs.zip`: original `cm/cm_client_type.py` SHA256 `096a6054a68dbf249572e8390f2bc14208dcc2220065a35a5e0e1c844da34fd4`; original `cm/modbus_server15.py` SHA256 `9afc455fb50472012ae31d0767a0c39878647643ea9c37d7155142e097621d4f`; `cm/client.py` SHA256 `b131a850cfdb7102956f04f2bac86f7528e5964911e969b3712b2b6ac53c9b9c`; original `930/modbus-flags.json` SHA256 `bb0b335eaf4e3a98e5d71d1cd1551e0772fedcfcd3f7d17f3c78e04c21844b9e`.
- ORIGINAL `930/2.3.0-2.4.3/sensors.json` and `configurations.json` were read as source, 99 + 471 objects; 541 unique source read-side numeric register dependencies independently counted from the original formula/conditions/min/max/default token strings (NOT write-only set expressions); their original W2/W3/W4 mapping equals the 33 documented groups. This confirms V54's count from a separate direct parse and crosswalk, NOT a full running original firmware.
- Original 2.0.18 `appfs_2018.zip`: `cm/client.py` SHA256 `ae92a1dc8c9db9a620036d2c2a4c027a8369cb16319c20515e21e19219f0434e`; `cm/modbus_server15.py` SHA256 `45495f6f8e57e6eccf0cc09ee7b6952dd157e31fc645f34bbe5890c7291d7a9b`. Neither contains the 2.1.105-specific `wait_for_all_data_package` call; 2.0.18 does NOT bundle the newer 2.3.0–2.4.3 profile, so do NOT apply these masks to its separate older application.
- Locally completed EXP355 original log/report describes one **ordered 32/32 controller-native bootstrap** after a guarded response, ending at 06F4/19; source chronology is from original documented user run, not independently replayed original full EXP355 wire bytes by V62.

## PROVEN SOURCE SET-OVERLAP — not "32 plus 1"

| Source-defined family | Historically locally ACKed v4.1 initial 32-page sequence | Original 2.1.105 2.4.2 profile-significant group set | Intersection |
|---|---:|---:|---:|
| Settings lower (W3 / 1803) | 16 | 10 | 10 |
| Settings upper (W2 / 1802) | 16 | 15 | 15 |
| Operations/runtime (W4 / 1804) | 0 | 8 | 0 |
| **Total distinct groups** | **32** | **33** | **25** |

The seven native bootstrap pages **NOT selected** by this original application-completeness profile are: `047E, 0492, 04D8, 04F6, 050A, 051E, 06F1` (six W3 and one W2).

The eight original application-required group starts **NOT present in the 32-page native bootstrap** are: `07D0, 07E4, 07F8, 080C, 0820, 0848, 0864, 0870` (all W4).

Actual original `cm_client_type.py` class seeded from original 2.1.105 profile flags: W2 internal pending mask **0xBFFF** (15 bits), W3 **0x867F** (10 bits), W4 **0x035F** (8 bits). These are **INTERNAL pending-receipt tracker values**, NOT a verified current-XTR on-wire 0708 response and NOT authorization to construct/send a mailbox image. Original flags selector ranges are ownership mappings, not physical FC16 wordcounts.

## Direct original-method host checks: 9/9 tracker + 2/2 publication control PASS

Full source AST-extracted actual original `CMClientParameterUpdateState` methods (not a stand-in reimplementation), with original 2.1.105 `CMClient.on_publish_cm_params_map_event` invoked with inert parser/events/MQTT methods, passed these 11 bounded behavior scenarios:

1. Pre-WAIT group receipts ignored by INITIAL.
2. Seeding original 33 required groups gives precisely 15/10/8 pending groups and masks BFFF/867F/035F.
3. ALL 32 historically observed page starts received **AFTER tracker seed** clear **only 25**, leaving **eight W4 groups pending**.
4. The eight W4 group receipts AFTER the 32 clear the pending mask and enter `ALL_DATA_PACKAGE_RECEIVED`.
5. If all 32 arrived BEFORE seed, none are credited retroactively at `wait_for_all_data_package`: **33 still pending**.
6. One `0864` receipt after seed clears its W4 version group (32 remaining), consistent with already documented V57 same-outer-callback handling.
7. If version `0864` is credited first and all 32 historical bootstrap pages are then received, **seven other W4** groups remain.
8. Supplying the remaining W4 receipts completes the original tracker.
9. W4-only group receipts leave 25 settings groups pending.
10. Calling the **actual original** parameter-map publish method after all 32 bootstrap starts, with eight W4 pending, produces **zero map publications**, postponing publication.
11. Feeding all eight W4 receipts and calling the same original publication method produces one stubbed publication and transitions into its normal follow-up event flow.

All checks **PASS**. Private local offline-only fixture `/tmp/v62_offline_tracker_audit.py` SHA256 `89afae869444ae1053db8e77d2dd3bf58eece70c31694a21370c1d1daa2732fe`, not committed, not deployable, contains NO native responder or RTU/transmit code. The stubbed successful publication is **mock output**, not evidence of real Thermia Online onboarding or device-data validity.

## Interpretation and hard boundaries

**OBSERVED / PROVEN ORIGINAL CODE:** Under 2.1.105, a complete historical 32-page local initial sync has at MOST 25/33 groups in common with the specifically selected 2.4.2 app tracker **if receipt occurs after WAIT initialization**. Without the missing eight W4 group receipts the original app's parameter-map publication is postponed. A successful version source receipt may start the tracker *after* initial settings pages, and receipts before WAIT are not retroactively credited: the actual outstanding group count depends on receipt order, not only distinct pages ever observed.

**LOCALLY PROVEN XTR vs firmware-derived:** EXP355/386 32/32 -> qualified native FC16/0708 runtime is authentic historical XTR operation; it does NOT prove the vendor 2.1.105 software would have reached 33/33, map publication, onboarding or cloud Online on this controller. Native bootstrap page ACK counts are not application received-group counts.

**2.0.18 distinct behavior:** Original CM930 2018 source has no newer explicit 33-package wait barrier. Thus this V62 25/33 condition is specifically 2.1.105 + its bundled 2.4.2-compatible profile, **not** a universal requirement across every Connect firmware or actual currently installed XTR controller version.

**OPEN:** Present XTR version register `0867`, actual 2.1.105 chosen profile, actual first version-page timing, original software's real publish/onboarding/Online state, current native owner/slot/EOF/master acceptance and physical completeness of all 8 later W4 pages. No exact Connect application live-ready evidence emerges merely from host assertions.

**NEXT (offline only):** Use pre-existing XTR and genuine/collaborator captures to classify receipt order of the eight W4 required groups, with an explicit version-bound `0864` seed candidate, and conservatively report min/max possible progress of original 33-group tracker per *bounded* archive window. Do not turn a first-file timestamp into boot time or claim cross-model software ran 2.1.105. No redundant active approval/ACK work, no new controller reboot, no protected 0708 or native FC23 implementation, no YAML modification.
