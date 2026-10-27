# V5DCM11 — firmware-scoped CM930 handshake/readiness/publication audit (2026-10-17)

**Status:** COMPLETE / POSITIVE for offline static-source call-chain and conservative synthetic tests (10/10). COMPLETE / INCONCLUSIVE for live XTR DCM acceptance/Online and full original firmware state-machine parity. **No live experiment**, no changes to ESP32 YAML or native TX.

## Hypothesis, baseline and controlled change
**Hypothesis:** Thermia Connect RAUC 2.1.105 (embedded device_client 0.2.8) adds explicit package-readiness gates, separate from CM930 handshake state, which constrain parameter-map publication; a simple accepted/32-page flag does not model full Online integration.

**Baseline:** V5DCM10 verified RAUC 2.0.18->device_client 0.1.45 and RAUC 2.1.105->device_client 0.2.8 by direct extracted ext4 and 46/46 matching Python modules. V5DCM8 proven offline fail-closed event classifier; user live V5DCM2 FIX1 RX-only stable.

**Exactly controlled change:** offline AST symbol/call-chain assertions of original app-source files and standalone fail-closed Python witness tests. Original sources were *read*, never executed or copied into public artifacts. No ESPHome YAML change, UART, bus TX, keys, private 0x0F responder or 0708 command tooling.

## Source-confirmed differences
- **Both versions:** `cm/modbus_server15.py` separates native FC23 handshake-response handling from FC16-triggered software handshake status and `on_handshake_state_changed_event` readiness-dependent info/operation request logic. The acceptance transition is a firmware software event, not proof of controller icon or cloud Online.
- **RAUC 2.1.105 only:** `cm/cm_client_type.py` defines `CMClientParameterUpdateState` states INITIAL, WAIT_FOR_ALL_DATA_PACKAGE and ALL_DATA_PACKAGE_RECEIVED, with three package request bitmasks.
- **Data flow (new version):** `cm/modbus_server15.py` `_on_registers_read` after version configuration load invokes `wait_for_all_data_package(_get_all_data_package_to_request())` (lines approx 538–549); `reset_register_read_request` invokes `data_package_received` (approx 357–366). `cm/client.py` `on_publish_cm_params_map_event` postpones publication unless update-state is ALL_DATA_PACKAGE_RECEIVED (approx 477–488). This is a *real source-level application gate* rather than a changed class name alone.
- **Important edge case:** calling `wait_for_all_data_package` with an empty set sets WAIT and does NOT automatically set COMPLETE; completion is evaluated in `data_package_received`. Synthetic projection therefore does not automatically mark empty expected lists ready. This is source-specific application behavior, not a new XTR physical-bus finding.
- **Publication scope:** later `cm/client.py` routes service-specific subscription/publish operations and `data/parsers.py` contains service-specific parser selection.

## Validation performed
`python audit.py`: **10/10 PASS**, comprising two-version AST method checks, matching handshake event path, new publication readiness gate, data-package receipt call flow, absent old gate, empty/unknown package safety, multi-package out-of-order progress, re-arm and duplicate receipt, no Online/authentication promotion from challenge+FC16 observations and rejection of unsupported events. These tests execute **our conservative model**, not the vendor's runtime, and do not replay bus files in V5DCM11. `source_ast_inventory.json` records extracted-file SHA256 and source AST call names.

**Relevant observed bus reference (not tested live here):** slave 0x0F FC23 read 0730/8 write 071C/8; known local FC16 03E8/14 and 085F/5; the observed availability of these frames does not prove a fulfilled package mask.

## Experiment criteria and result
- **Positive:** version-scoped code evidence, reproducible call-chain tests and no false declaration of DCM acceptance: MET.
- **Negative:** unsupported state assertion or failed source test: not observed.
- **Abort:** native physical TX, implementation leak of protected responder/security algorithms or unintended change to production configuration: none.
- **Recovery:** offline only. V5DCM2 FIX1 RX-only/HARD_DENY remains deployed.

## Classification
**PROVEN / offline original-source:** package mask and publication gate exist in verified 2.1.105 code, not in examined 2.0.18 code.
**STRONGLY SUPPORTED / firmware-derived:** handshake, runtime state, package readiness and service publication require separate representation.
**HYPOTHESIS:** model these gates to approach native DCM behavior on XTR M; no proof of local Controller ACCEPTED/display.
**OPEN:** exact per-profile package bitmap and source-to-wire package identity, native sender/owner/epoch and response slot, DCM icon, Internet Online.
**DISPROVEN/SUPERSEDED:** claiming a 32-page observational cursor or raw FC23 pair alone is sufficient to declare Online.

**Next V5DCM12 — PREPARED / NOT RUN:** offline mapping and replay of actual historical config-package observations against source-verified request-mask tables with provenance and fail-closed UNKNOWN handling; do not invent absent register-bit assignments or transmit anything. No hardware rollback required.

**Artifact:** V5DCM11_CM930_READINESS_OFFLINE_20261017.zip (sanitized audit.py + JSON inventory + tests + report).
