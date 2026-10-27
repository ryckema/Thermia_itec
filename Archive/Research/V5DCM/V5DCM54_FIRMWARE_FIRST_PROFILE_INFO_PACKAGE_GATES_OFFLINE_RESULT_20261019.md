# V5DCM54 — Firmware-first CM930 device-info, 2.4.2 profile and 33-package publication gates (2026-10-19)

**Experiment ID:** V5DCM54-CM930-FIRMWARE-INFO-PROFILE-GATES-OFFLINE-01
**Status: COMPLETE / POSITIVE — exact original firmware methods + archived JSON verified HOST/OFFLINE ONLY.** Native XTR acceptance, physical owner, reply slot, 03E8 absence root cause, application onboarding and Online remain OPEN / UNKNOWN. No ESPHome compile, device connection, new controller cycle, flash, bus TX or settings write.

## Priority/source-of-truth contract

**User instruction:** Original genuine Thermia Connect firmware determines intended CM930 implementation semantics. Write Beta v4.1 is HISTORICAL LOCAL XTR corroboration/inspiration, not the authority for an omitted original DCM application transition. For electrical/bus claims, raw local XTR captures still outrank firmware expectations.

Hypothesis: Original 2.1.105 firmware has distinct startup-info requests, version-driven profile selection, internally tracked required package groups, and later parameter-map publication gates; the firmware versions differ even though their 930 request-bit maps agree. Exact original functions and raw profile JSON can be exercised with isolated stubs rather than inferred from v4.1 or a derived CSV.

**Known-good on-device baseline (untouched):** V49 RX-only, user manual Thermia OFF/ON associated with 10351ms callback gap; RX_SHADOW_RECORDED 285 matched CRC frames/30.532s; V5/B11C/B11D no new faults, native TX0, owner/EOF/slot unknown. Current V49 sampled W3=0600 (04A6+04BA) but 03E8 missing, native 0708 status poll0, full profile readiness absent. Earlier independent local XTR V23 RX-only *did* see 03E8/count14 under TX hard deny; historical Write Beta v4.1 EXP386/387 positive/EXP388 partial, no new execution. Prior V5DCM21 profile census source-index 33 and V5DCM50–53 results preserved, not mislabeled as newly performed live tests.

**Single controlled activity:** read-only exact-source AST execution of original 2.0.18 and 2.1.105 firmware CM930 Python methods in host process with mocked event queue, Modbus IO, profile-loader and MQTT publisher; additionally parse original 2.1.105 sensor/configuration JSON with its exact original RegisterToken + tokenization and CM930 address-to-request-bit mapping functions. No serial, no protected transform, no real 0x0708 response/mailbox code, no user secrets or native TX payload output. Targets: logical CM930 0x0F application/event sequencing, version source register 2151/0x0867, request group 1804/W4 bit8, 2.4.2 required groups, internal tracker and parameter-map publication. Current version/serial/active device page values unverified from V49.

**Positive criteria:** exact-source/mocked event behavior deterministic; 33-group counts computed from ORIGINAL 2.1.105 profile JSON, not pre-derived CSV; 2.0.18 divergence reproduced; no real communication. **Negative:** version-file hash mismatch, failed mapping/test, unexpected runtime side effect. **Inconclusive:** any controller electrical/source/slot, semantic adoption or actual current XTR cause. **Abort and rollback:** stop on source mismatch or any call path touching external IO. No hardware rollback is needed because no device interaction occurred.

## Exact original primary evidence

Original complete user-uploaded extracted AppFS archives:
- Connect **2.1.105**: SHA256 42d365c89a7a0cc76138c57c1bf50cfd95c33c3ffcf7aef26f39c01b7c81f49e. CM930 modbus_server15.py SHA256 9afc455fb50472012ae31d0767a0c39878647643ea9c37d7155142e097621d4f; cm/client.py SHA256 b131a850cfdb7102956f04f2bac86f7528e5964911e969b3712b2b6ac53c9b9c.
- Connect **2.0.18**: SHA256 ad27967bdb1f8300fc3768bf30ae5033f55c858269fdd23c1d5a622a23da4c77. CM930 modbus_server15.py SHA256 45495f6f8e57e6eccf0cc09ee7b6952dd157e31fc645f34bbe5890c7291d7a9b; cm/client.py SHA256 ae92a1dc8c9db9a620036d2c2a4c027a8369cb16319c20515e21e19219f0434e.
- 2.1.105 ORIGINAL profile source files for bundled 2.3.0–2.4.3 CM930 range: sensors.json, 23,122 bytes, SHA256 6a5941387f14cb8d5419a715b8983a1d3c044c7d1ffd6c82513103413ba78c0d; configurations.json, 158,727 bytes, SHA256 d5194627e1678a1b10239b988c6ba195e62b39dbc37f4fe927d3bae907060b2c; info-2.4.2.json, SHA256 25f24756667f575a0d7cdda0f3a766b306cb19feed30886a9cd8d02087e0e114.
- Original 930/modbus-flags.json byte-identical in both firmware archives (V52 correction), SHA256 bb0b335eaf4e3a98e5d71d1cd1551e0772fedcfcd3f7d17f3c78e04c21844b9e.
- Private, IO-free offline host harness SHA256 c1626d8029bcd4bacec68f281961b1b42e6d57024a0002b39dc4c3a05172f009; original raw profile mapping audit SHA256 fb0a5a06749a06fb1f9d444d0559aa4cf4131585e6978fe43c4f612ae9a279f1. Held locally/private and not committed; tests not a complete Connect service execution.

## OBSERVED SOURCE and DIRECT HOST FACTS

### A — Startup/version/info does NOT equal H2 or application readiness

Both genuine firmware versions start CM930 with logical slave 15/0x0F, handshake NOT_ACCEPTED, and application runtime WAITING_FOR_DEVICE_INFO, tracked separately. In both original-source event dispatchers:
- ACCEPTED while WAITING_FOR_DEVICE_INFO calls the information-register request method;
- ACCEPTED while OPERATION calls the operation-data request method;
- NOT_ACCEPTED emits neither; ACCEPTED in other intermediate runtime states does not invoke one of these two actions.
Four host scenarios per version PASS (8/8).
- The original **initial CM930 firmware-version extractor references only decimal 2151 / 0x0867**; 2.0.18 and 2.1.105 both verified from the actual original extractor method with isolated ParamExtractor, 2/2.
- Original CM930 InfoMessageCollector.ready_to_send requires known firmware version **and configured serial number**. Direct original-method host checks of absent/present serial PASS for each version, 4/4. This is an information/onboarding condition, not Modbus CRC or FC23 acceptance.
- Original request-info method on both versions publishes the current InfoCollector significant-register set through the internal event dispatcher; isolated initial version-only source test returns register 2151, not an operation request. The returned event is not a physical 0x0708 request until the CM930 server application converts it and the controller polls/receives the corresponding status service. The original FC16 handler may mark internal ACCEPTED from H0 without previous FC23; internal software accepted is still not controller-authenticated.

### B — Profile selection versus request-group receipt accounting

On ORIGINAL CM930 _on_registers_read in both versions: when a version is first available and a profile has not yet been loaded, _load_config_files is called and this callback RETURNS, before a new direct request-info event or info publication in that same method call.

**2.1.105-only additional step:** immediately after profile load, call cm_client_parameter_update_state.wait_for_all_data_package(_get_all_data_package_to_request()). This starts an INTERNAL required-receipt mask; it **does not itself assert all request bits on the physical 0708 status interface**. Real outgoing application events for information or operation groups occur on the distinct _request_info_data/_request_operation_data paths and reception/clear paths. A blanket statement "loading 2.4.2 sends 33 physical requests" is therefore UNSUPPORTED.

**2.0.18 exact source difference:** the same startup profile-load branch returns without any wait_for_all_data_package call; its original on_publish_cm_params_map_event has timing/const-stability gates but **not the same explicit 33-package ALL_DATA_PACKAGE_RECEIVED blocker**. This is meaningful application-version divergence despite identical shipped flags JSON.

The 2.1.105 original tracker has INITIAL, WAIT_FOR_ALL_DATA_PACKAGE and ALL_DATA_PACKAGE_RECEIVED states. It ignores group receipts before WAIT; after seeding, it clears only mapped required bits upon page receipt. Host execution using ORIGINAL source proves: a single 03E8/W3 bit0 clears THAT group, not all significant groups, and an early pre-initialization receipt is NOT automatically credited to later pending state. **HYPOTHESIS ONLY:** certain event sequences could keep a required group pending until republished; not proven to explain V49's missing page.

### C — Recomputed required packages from ORIGINAL profile JSON

The original 2.1.105 sensors.json contains **99** items; configurations.json **471** items; exactly **541 unique numeric referenced registers** using the ORIGINAL token parser's semantics (read formula, conditions, dynamic min/max/default; NOT write-only set formulas). No unmatched/ambiguous mapping. Executed the **actual original** _register_and_bit_for_address and _get_all_data_package_to_request bodies against the raw original JSON-derived registers (not the repo's normalized CSV) and original modbus-flags.json.

Result: **33 distinct required package groups: W2/1802=15, W3/1803=10, W4/1804=8**. The actual CM930 method output exactly matches the independent direct group set, 33/33. Register 1000/0x03E8 maps W3 bit0; room setpoint 1012 shares W3 bit0. Version register 2151/0x0867 maps W4 bit8, which is *excluded by the broad request_read_all_registers routine* but correctly included by the firmware's targeted information request or source-dependent significant group set. Do not conflate those two request routes. This is original-source validation of the previous V5DCM21 derived 33-group count.

### D — 2.1.105 parameter-map publication really waits for package completion

Exact original CMClient.on_publish_cm_params_map_event tested with mocked MQTT publisher/event queue:
- WAIT_FOR_ALL_DATA_PACKAGE with outstanding 03E8 and version-related W4 group: **no map publication**, postponed.
- Receipt of only 03E8 still leaves W4 pending: **no map publication**, postponed again.
- Once all tracked required groups cleared: **map publication proceeds** in mock with available parsers.
- This is the **parameter-map publication** condition, NOT proof the controller would refuse to poll FC16/status, nor that all app features are Online before this point. Original _on_successfull_onboarding enters OPERATION and schedules parameter-map events separately; do not collapse onboarding, H2, W2/W3/W4 readiness, and cloud Online into a single status.

## Actually executed source/host checks

- **40/40 direct original-method/host-mock assertions PASS**, including two genuine-version source branches, H2/request dispatch, first-version/profile/return ordering, event output boundaries, original CM930 tracker INITIAL→WAIT→ALL and pre-WAIT negative control, 2.1.105 map publication blocking/unblocking and original 0867/serial readiness. They isolate ORIGINAL method bodies; other dependencies are inert mocks, not a complete original Connect process/Modbus firmware run.
- **Original JSON + original token/bit method profile audit PASS**, with 570 definitions, 541 unique numeric references, 33 groups (15/10/8) and zero ambiguous mappings; source methods exercised exactly, isolated from hardware.
- Previous local V49, V23 and archived v4.1 historical experiment results were not re-run. All native output remains physically unused in this investigation.

## Conclusions, uncertainty, next action

**PROVEN original firmware source/host:** distinct logical slave handshake, info-readiness, version/profile selection, internal package-receipt tracking, and 2.1.105-only parameter-map readiness gating; identical 2.0.18/2.1.105 request-bit mapping does **NOT** imply identical application behavior. A required W3 03E8 receipt is not interchangeable with W4 0867 version receipt, and internal ALL state is not necessarily controller/Online acceptance.

**STRONGLY SUPPORTED architectural conclusion:** A faithful native DCM replacement needs separately modeled (1) controller-origin bus delivery, (2) handshake state, (3) version/info/profiles, (4) request-bit publication and receipt, (5) tracker/publishing/onboarding. Write Beta v4.1 is a useful historic locally proven transport/semantic example but MUST NOT substitute for the original 2.1.105 application stages. No speculative current V49 03E8 root cause declared.

**OPEN:** actual present-day XTR physical owner/sender/electrical EOF/reply slot; whether first missing 03E8 preceded/lagged profile discovery; exact current 0867 version and whether all significant groups could be requested on live bus; complete accepted native response, full OPERATION/application onboarding and Online. V49 W3=0600/none03E8 and no status polls is INSUFFICIENT to identify specific missing application transition; old RX-only V23 had 03E8 under different context. Prior V47 orphan17 remains independent.

**NEXT — offline only:** reconcile existing raw local XTR and genuine/collaborator chronology around *first* recognized 0864/0867 information-source page, first 03E8, first six-word status poll and subsequent group-request bitmap changes; distinguish pre-profile initial traffic from post-profile readiness and from cloud onboarding. Do not suggest another power cycle, Arm, new responder/0x0708 command tooling or active TX merely to obtain evidence already captured. A later scoped passive-only observer could be considered only if the archived captures cannot resolve the state ordering; current running V49 and its known-good HA, diagnostics and fail-closed output are untouched.


## Archived cross-model chronology corroboration (passive offline metadata, not local XTR)

As a separate provenance check within this SAME offline evidence review, re-parsed existing user-supplied genuine/collaborator ATEC/DCM03 RTU capture thermia_capture_20261003_165355.log (cross-model legacy geometry, SHA256 14918065297264473e2357822a8694d184e7821b8c2a3b1cb316039678a708a1). Relevant first **CRC-good envelope** times from the existing capture only:

| First visible event (host timestamp) | Time / captured RTU geometry |
|---|---|
| Native FC23 request-shaped interaction | t=27.400 s (request family; no protected reply content included) |
| Initial controller FC16 source settings | t=29.262 s, native 0x0F:03E8 / **13** words |
| First service-family 0x085F page | t=61.529 s, count5 |
| First status six-register poll | t=64.923 s, FC03 0x0708/count6 |
| **First 0x0864 page (includes version register 0x0867)** | t=86.672 s, FC16 0x0864/count4 |

**Observed cross-model sequence:** initial native 03E8 arrives **57.410 seconds BEFORE** first observed FC16 0864/count4 (the frame geometry carrying register 0867). Even the first 0708 status poll is later than initial 03E8. This supports the separation between **controller-driven physical bootstrap before product/version profile discovery**, and **later application-level package completeness**. It does NOT establish precisely when the original Connect 2.1.105 process decoded its version or asserted the 33-group tracker in this ATEC legacy session; the captured external module software version and its actual internal event queue were not observed. The 03E8/count13 legacy payload is NOT interchangeable with current XTR 03E8/count14. Logged host times are NOT electrically measured UART EOF/slot delays.

Two Eco5 collaborator files start with some runtime/status data before their first visible native FC23; they are not independently bounded from first physical connection and should not be assigned absolute boot-state precedence on their first events. On the present RX-only V49 extracts 03E8 and 0864 profile receipt both remain unproven in this observer, while V49 serial native owner/slot is unknown.

**Strengthened conclusion (firmware plus independently archived cross-model ordering):** Receiving a first bootstrap 03E8 does NOT require that the device-client application has already loaded the final controller-version-specific profile. A firmware implementation can later seed a separate required-package tracker; earlier receipts need not be retroactively counted. This is a staged model with different clocks/evidence, **not a demonstrated V49 protocol error or permission to transmit**.
