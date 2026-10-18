# V5DCM21-PACKAGES-01 — Thermia Connect 2.1.105 significant-package completeness
Date: 2026-10-18

**Experiment status:** RUNNING / PARTIAL (offline exact-HEAD build and host tests PASS; no user-confirmed new local V5DCM21 run). **Native V5DCM21 overall:** RUNNING / PARTIAL. No active TX/flash/new controller test.

## Hypothesis and evidence
The genuine Connect firmware's application-layer pending significant packages (three W2/W3/W4 masks, with state INITIAL -> WAIT_FOR_ALL_DATA_PACKAGE -> ALL_DATA_PACKAGE_RECEIVED) should be tracked **independently** of: (H) native handshake response/ACCEPTED, (B) controller 32/32 fresh bootstrap, (M) mailbox, (R) runtime, and (A) full Connect onboarding/OPERATION. A generic RX frame, historical count14 page, FC16 ACK or all 32 pages alone must never declare parameter publication or Online success.

Primary source verified locally: user-provided `/mnt/data/device_client.zip` (source-derived file `device_client/cm/cm_client_type.py` SHA-256 prefix `096a6054a68dbf24`; `device_client/cm/modbus_server15.py` prefix `9afc455fb5047201`; `device_client/cm/client.py` prefix `b131a850cfdb7102`). These contain `CMClientParameterUpdateState` with **three masks**, methods `wait_for_all_data_package` and `data_package_received`, call sites `reset_register_read_request`, and `on_publish_cm_params_map_event` guarding publication until all packages received. The exact local ZIP association with RAUC 2.1.105 is supported by the prior [V5DCM11 original RAUC source audit](V5DCM11_CM930_READINESS_OFFLINE_20261017.md), not a newly repeated extraction of the entire 112MB RAUC during this step.

Direct firmware repo primary model: `data/cm930_orthogonal_state_axes.csv`, `data/cm930_readiness_gates.csv`, `data/cm930_profile_layer_model.csv`, `data/cm930_state_machine_transitions.csv`. Historical XTR version `0867=242` and modern native page geometry are separately proven as documented; neither is a validated W2/W3/W4 significant-package map by itself. **Important precision:** The general W2/W3/W4 *bit-to-register-range* association is **FIRMWARE-PROVEN** in `Thermia_Connect_Firmware/data/cm930_modbus_flags_map.csv` (`modbus-flags.json`): e.g. W3b0 -> 03E8 selector range, W3b4 -> 0442 range, W2b1 -> 055A, W4b0 -> 07D0. The *physically received FC16 word counts* are XTR/profile dependent and cannot be inferred from those selector spans. The **exact profile-dependent significant-register subset** that supplies pending masks for the XTR 2.4.2 profile remains **OPEN**; the app ledger deliberately does not label every known selector bit as significant.

## Verified deployment baseline and standing permission
- Standing user decision [autonomous native TX authorized in principle](../NATIVE_AUTONOMOUS_TX_AUTHORIZATION_20261018.md). Accepted G01–G06 residual research risks remain accepted; no automatic reopening.
- The last separately verified V5DCM19 FIX1/V5DCM20 RX-only native session observer run was 18m33s, no physical software TX attempts. Its exact original installed ZIP/YAML remains unavailable; **do not assert V5DCM19 remains the latest flashed program**.
- **Newer actual user-confirmed read-only v31 FIX4 execution exists** (see top of current `THERMIA_PROJECT_STATE.md`): after 151s `03E8:Y`, other 12 source pages `N` in one short boot window. That is not a new V5DCM21 emulator trial, nor native app-package readiness. Keep v31 work separate; no code was flashed here.
- User has no physical original Online/DCM module for new captures. Native security algorithm, private responder and confidential 0x0708 tooling remain unpublished.

## One controlled source-only change and implemented invariants
Added in `ryckema/Thermia_Connect_Firmware`:
1. `portable/xtr_v5dcm21_packages.hpp` — independent, receive-only `PassivePackageLedger` with firmware-derived three `uint16_t` package masks, separate source-supplied validated profile, current local observation generation and Core controller-epoch label. Configuration rejects invalid group/bit/count, duplicate register bit, and conflicting identical page geometry, without guessing actual W2/W3/W4 bit assignments. Completed CRC-valid native `0x0F FC16` frames from existing decode path clear **only** a matching expected bit once. Any stale source/epoch, CRC error, wrong geometry, other slave, unconfigured ledger, or duplicate receipt cannot advance. `revoke()` clears package state. No UART reader, register writes, TX/DE or responder.
2. `portable/test_xtr_v5dcm21_packages.cpp` — 26 C++17 assertions with **explicitly synthetic bit/page mappings** (not claimed as genuine XTR mapping), foreign/malformed/duplicate/revocation/epoch/out-of-order and complete-three-group checks. `enrich()` sets only `IndependentEvidence.profile_selected` and `required_packages_received` from independently supplied source-qualified state; it **does not** set physical owner, transport, native ACCEPTED, `application_data_ready` without real handshake, native OPERATION/Online, or TX permission.
3. Mandatory GitHub CI compile and run added to `.github/workflows/v5dcm21-readiness.yml`.

**Deliberate safety deviation** from permissive source edge: original 2.1.105 can set WAIT even when configured expected set empty, and evaluates all masks clear on a later `data_package_received` known-register call. This conservative public ledger refuses to claim COMPLETE for a zero-entry expected set from an unrelated receipt. This is an implementation safety policy, **not exact OEM behavioral parity**.

Commits: `e31d213a` initial ledger, `aef15e00` CRC/include and mapping ambiguity safeguards, `20b72fee` host regression, `6a96c3a8cd517f689f4d420d0b8789bbd40abb4f` CI inclusion.

## Actually executed CI result
[GitHub Actions run 39124813711](https://github.com/ryckema/Thermia_Connect_Firmware/actions/runs/39124813711) on source commit **`6a96c3a8cd517f689f4d420d0b8789bbd40abb4f`**, mandatory checkout/strict C++17 compile+execution **SUCCESS**:
- **26/26** new significant-package tests;
- existing **24/24** Core/readiness and **46/46** RX-adapter checks;
- **22/22** delivery-provenance memory fake;
- **30/30** firmware-reference model split;
- **35** public production lifecycle callsite checks across 29 source files;
- **5** passive capture and **4** temporal synthetic scenarios;
- independent embedded/portable Core byte comparison and strict C++17 build, TX hard-deny source checks PASS.

This CI runs synthetic fixtures only. It does **not** replay the user's actual v31 live evidence, establish XTR bitmaps, reproduce the vendor application runtime, compile full ESPHome YAML, flash an ESP32, or measure physical bus TX. No new native OnLine result.

## Positive/negative/inconclusive and abort/recovery
- **POSITIVE offline:** actual-source package ledger compiles, 26 assertions PASS, no false semantic/Online/TX readiness in tested adverse cases.
- **NEGATIVE synthetic** tests intentionally reject ambiguous pages, bad CRC, stale provenance, unknown group/bit, duplicate receipt, incomplete and empty groups.
- **INCONCLUSIVE live:** required request mask mapping, actual XTR package cadence/receipt, genuine accepted handshake and full app OPERATION not tested.
- **Abort:** unsolicited bus TX, unbounded response/retry, mapping guessed from page starts, private 0x0F algorithm publication or loss of HA production entities. None triggered: no hardware action.
- **Recovery:** independent firmware-repo source-only rollback; the user-flashed current read-only program is unchanged.

## NEXT ACTION
Extract the actual XTR 2.4.2 semantic profile's **significant registers** from the 2.1.105 sensor/config parser profile and join them to the **already recovered and proven** W2/W3/W4 selector ranges, retaining actual local XTR physical FC16 counts and provenance. Do not treat all 43 mapped selector groups as significant requests by default or fabricate absent profile data. Only after this can package events from the existing controller CRC-valid callback supply genuine per-profile C1->C2 completeness; app OPERATION remains a separate axis. Then continue guarded autonomous native DCM adapter design under standing permission, with one scoped user-initiated live deployment test once precise payload provenance and current deployment baseline are established.
