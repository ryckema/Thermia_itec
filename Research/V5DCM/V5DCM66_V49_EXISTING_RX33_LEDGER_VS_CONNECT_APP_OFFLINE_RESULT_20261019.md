# V5DCM66 — Existing V49 RX33 + portable ledger versus original Connect application

**ID:** V5DCM66-V49-RECEIVE-LEDGER-TO-CONNECT-APP-SEAM-OFFLINE-01
**Date:** 2026-10-19
**Status: COMPLETE / POSITIVE — exact original-source audit and 13/13 C++17 synthetic RX-only assertions.** Original native Connect C2/OPERATION/Online, controller master owner/EOF/slot, current version and physical TX readiness remain **OPEN / UNKNOWN**. No live hardware, native TX, ESPHome build/flash, new YAML, reboot, protected FC23/0708 code, register writes or on-device experiment.

## Controlled question / baseline / previous work

**Hypothesis:** does the exact historical user-provided V49 source already link its completed CRC-valid single V5 RX callback to a real native 33-group source-selected passive ledger; if yes, precisely which firmware-equivalent version/WAIT/app gates remain absent? Do not repeat V21/22/23 implementation, V57/62 original-method tests, or V65 local W3/W1/retained proof.

**Last verified user-device baseline:** V49 RX_ONLY/HARD_DENY user-confirmed running; manual Thermia off/on correlated with 10,351ms receive callback gap, 285 clean matched post-gap frames over 30.532s, native UART TX0. Repeating 04A6/085F but no sampled strict 03E8/0864/0708; first seven unanswered FC23 challenges and later cumulative63 separated by >13 minutes of unseen console. Exact deployed binary checksum **not verified**; source ZIP still carries original PREPARED/NOT FLASHED filename, but later user log confirms V49 was installed/executed. EXP388 still RUNNING / PARTIAL.

**Relevant existing work:** V5DCM21 genuine original-source RX-only PassivePackageLedger/CI; V5DCM22 portable join and 33 XTR2.4.2 source descriptors; V5DCM23 original V5 callback integration; V5DCM37 dry-run coordinator; V54/56/57 firmware internals; V62 original code 33-group tracker 9/9 + publish gate 2/2 host tests; local XTR EXP352 W3bit0 and EXP343 W1bit0 in V65; old-display Eco5/ATEC are structural/cross-model only. Preserve original HA controls, first-fault bus-health bookkeeping and B11C/B11D/P5 red/brown diagnostics.

**One controlled OFFLINE action:** inspect exact user-uploaded V49 ZIP and original 2.1.105 AppFS Python + portable V21–23 GitHub sources, then compile unchanged extracted V49 C++ ledger/RX33 classes with original frame/CRC/core translation units, exercise 13 synthetic receive-only assertions. Do not load user-private output protocols or create any responder. Passive targets: existing strict native 0x0F FC16 33 page geometries, FC23 **revocation** shape and 0864/count4. No outgoing slave/payload/current register value/timing or plant effect. Fail/revoke test if CRC/profile shape/state/authority mismatch; no physical abort or rollback required.

## Exact input pins

- ZIP: V5DCM49_RX_ONLY_POST_GAP_COHORT_PREPARED_NOT_FLASHED(2).zip SHA256 62afe39629102a3daa06f09eab3ed159f44437d702fb8d3904c61e62e2a85630, 69 members.
- Main V49 YAML inside ZIP SHA256 fe02f0b0a503f8f896442165e57397afeacd22cf951efa46ea87885f98d71c22, 4,728 lines. Exact flashed binary not confirmed.
- Original private V49 v5dcm23_v5dcm19_real_ledger.hpp SHA256 c5ffb1af07ad0e465194c753739d1213f54d4957babf8bfe96cbb5ea2f6e6544, copied xtr_v5dcm21_packages.hpp SHA256 a31a882f906e0282e9257aa1deedeafd52feba5ba5610563aea3b3708ebdc18f.
- Original V49 v5dcm22_v5dcm19_rx33_witness.hpp SHA256 e6a6e60c77c0bd2568c17e7fd564f3882bb2013941c8a102bfb4b6a1cc134777; v5dcm32_rx_rejoin_bridge.hpp SHA256 fd158cbd28be4c3c533fb2dbbe9056486161c444e5106da41733c593ce4bcfd0.
- Original genuine 2.1.105 AppFS cm/cm_client_type.py SHA256 096a6054a68dbf249572e8390f2bc14208dcc2220065a35a5e0e1c844da34fd4; cm/client.py SHA256 b131a850cfdb7102956f04f2bac86f7528e5964911e969b3712b2b6ac53c9b9c.
- Public original portable blob references: xtr_v5dcm21_packages.hpp 5f4012fce4e549470af4a015a32982aa2f990c24, xtr_v5dcm22_package_integration.hpp 9a6fc7b5e5613cbacce9bc2f053eb335cadd9747, xtr_v5dcm22_profile_242.hpp 75b800ea239b9439ac8577aec72ad97f5615a329, xtr_v5dcm23_v5_callback_gate.hpp 79ebc8fbc22f4ad8f4165383d7cac8fe1c71d22f.

## VERIFIED source connectivity

1. V49 YAML **already has** real V5DCM21-class PassivePackageLedger via the V23 private bridge, NOT just a shape-counting placeholder: on_boot reset_for_xtr242() at approx. YAML line 137, separate V22 observer reset line138. At approx. lines1662–1685, the **existing** CRC-complete V5 callback executes c.on_frame and feeds the **same original parsed frame bytes** into V22 observer and V23 NativeRxLedger. No second UART reader, no new parser and no output path.
2. V49 exact V23 ledger selects a SOURCE-ASSUMED XTR2.4.2 33-group profile **at ESP boot**, before confirming currently connected 0867 version. It thus counts source-selected FC16 frames before the genuine vendor app would seed WAIT. This is descriptive geometry observation, NOT original semantic version/profile initialization or C2.
3. Original 2.1.105 CMClientParameterUpdateState has INITIAL, WAIT_FOR_ALL_DATA_PACKAGE, ALL_DATA_PACKAGE_RECEIVED. Before WAIT, data_package_received ignores input; version/info processing can seed WAIT and credit the 0864 group in the same outer callback (V57); on_publish_cm_params_map_event postpones map publication until ALL (V62 independently tested 9+2 original-method scenarios). These **vendor application semantics are NOT present in V49**.
4. V49 NativeRxLedger independently checks CRC, complete geometry and local provenance. Any native FC23 or CRC/integrity fault revokes its selected profile/count; later 0864 alone does NOT reselect. Its private reselect_rx_only_after_accepted_risk is exposed only to the **user-armed V5DCM32 Fresh accepted-risk RX-only observation policy** after scoped controller gap/return/cold-pattern/challenge; this is NO physical epoch, owner, native ACCEPTED or TX. No automatic passive re-selection after FC23.
5. The distinct V22 RX33 observer deliberately preserves **ever-since-boot** page shapes after FC23, but clears/revokes its **active session** mask and remains revoked until reset. Such a no-session tally cannot establish that the controller refused connection.
6. Existing V49 30-second V22 and V23 log lines explicitly say C2=UNPROVEN, Online=UNPROVEN, owner=?, epoch=?, TX=HARD_DENY, even if V23 reports 33/33 shape receipt. Source class kTxAllowed=false. Physical DE and current flashed binary not independently measured.

## ACTUALLY EXECUTED offline host checks: 13/13 PASS

Strict host compilation using unchanged V49 source: g++ C++17 -O0 -Wall -Wextra -Werror -pedantic, original extracted core/frame/wire .cpp linked, no actual ESPHome compile or UART calls. Disposable synthetic inbound-only harness SHA256 0c0a35dc158000d1ecf61038f6fc0dba37c3cd7dee3c326a0b7dcc279ee8df21, not deployed/published.

1. Boot-reset selects XTR2.4.2 profile without actual version-page input.
2. Selected profile starts at 0/33.
3. Strict synthetic FC16 04A6/13 **before 0864 version** counts as 1/33.
4. Native FC23 revokes profile/0/0 ledger.
5. Valid 0864 after FC23 does not automatically reselect.
6. Another explicit host reset reselects without version.
7. All33 unique correctly formed synthetic FC16 incoming pages satisfy **passive shape** completion.
8. At synthetic33/33 Online/accepted/TX remain false.
9. Deliberately CRC-corrupted page revokes ledger.
10. V22 ever/session both 1 after first valid 04A6/13.
11. FC23 leaves ever1 but session0.
12. Next 0864 makes ever2 but session0 (still revoked).
13. V22 C2/Online/TX authoritative flags remain false.

All passed. **This is host-only source implementation evidence**, not a valid same-epoch user XTR application C2 observation and not a new OEM method execution; V57/V62 already did that.

## Evidence classification and decision

**PROVEN SOURCE + HOST:** V49 already implements single-callback passive RX33 + real portable ledger, strict CRC/FC23 fault revocation and testable 33-geometry census. Adding another FC16 observer or re-implementing V21 would DUPLICATE previous work.

**STRONGLY SUPPORTED / GAP:** original Connect 2.1.105 version-dependent profile selection, first-version SAME-CALLBACK WAIT initialization and subsequent 33 receipt-time semantics are separate from present V49 boot-time geometry selection; original parameter-map, device-info/onboarding/OPERATION/cloud Online service is **absent** from current V49. 32 native XTR bootstrap ACK != original 33 app groups; a synthetic 33/33 receipt count also not app C2/Online.

**OPEN:** current V49 XTR value at 0867; authoritative controller master/epoch/physical owner/EOF/response slot; original native response delivery and genuine application state; exact flashed binary hash and physical electrical output.

**Next:** source-only nonflashable two-column observational fixture (existing raw_shape_seen versus source-derived vendor_after_version_WAIT_receipt), with default UNKNOWN controller version/epoch. Preserve all hard DENY, no TCP/MQTT/Cloud claiming success and no secret/command-mailbox implementation. Do not automatically re-run older cold-start, W3b0, W1b0, W5, or original method tests. No new live experiment prepared in V66.
