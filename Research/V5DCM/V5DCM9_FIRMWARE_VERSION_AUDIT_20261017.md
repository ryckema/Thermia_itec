# V5DCM9 — offline CM930 application version comparison — 2026-10-17

**Status:** COMPLETE / POSITIVE for independently reproducible static source-tree audit; COMPLETE / INCONCLUSIVE for mapping individual Python sources to the precise RAUC firmware bundles and for XTR M semantics.

## Hypothesis, baseline and change
- Hypothesis: later Thermia Connect application versions add explicit packet-readiness and multi-service publishing states; therefore a single configuration cursor or native handshake-shape cannot prove the DCM is accepted, shown or Online.
- Baseline: offline fail-closed V5DCM8, and user-deployed V5DCM2 FIX1 RX-only production ESPHome.
- Controlled change: offline-only static inventory and AST comparison of already extracted original source files; **no** UART, DE, TX, ESPHome YAML or actual firmware execution.

## Source identity and limitation
- Local `appfs_2018.zip`: `device_client/_version.py` = **0.1.45**, **21** Python files.
- Local `device_client.zip`: `device_client/_version.py` = **0.2.8**, **25** Python files.
- 21 shared sources, **16** changed and 5 unchanged; **4** added, zero removed. Added modules: `cm/cm_client_type.py`, `data/service.py`, `data/storage.py`, `smart_energy.py`.
- **Critical provenance boundary:** this audit has **NOT independently matched these two source snapshots one-to-one to the RAUC archives** `Thermia_Connect-2.0.18-s1.raucb` and `Thermia_Connect-2.1.105-s1.raucb`. Their archive labels are not the internal `device_client` Python versions. Thus conclusions below are *app-source version differences*, not verified RAUC-to-RAUC source mapping.

## Firmware-source-derived differences (not XTR bus proof)
1. `cm/modbus_server15.py`: CM930 register and block constants were factored into `cm/cm_client_type.py`; `CMClientParameterUpdateState` appears and is fed data-package-arrival observations; new `_get_all_data_package_to_request()` collects subscription-driven package requirements. The read/write handler remains a separate protocol layer from readiness and publication.
2. `cm/client.py`: adds explicit local/cloud service selection and service-scoped subscription/publication, room-sensor state, gateway parameter storage, and related deferred control paths. Some previous aggregate cloud-subscription handling is replaced with service-specific paths.
3. `data/parsers.py`: previous single subscription state becomes service-keyed subscriptions with conditional parameter-map generation.
4. `smart_energy.py` and `data/service.py` are additions in the newer source snapshot. These application concerns do **not** independently establish new XTR Modbus fields or a particular display icon bit.
5. **No claim** that the native FC23 answer transform or on-wire response bytes changed: a changed source file or relocated constant does not demonstrate a changed cryptographic function.

## Results and safety
- Static Python audit asserts internal versions, 21 vs 25 modules, exactly 4 added modules, changed client and server source, and mandatory RAUC mapping = NOT_VERIFIED. PASS.
- No recovered security algorithm, key, native responder payload, private 0708 mailbox command or firmware implementation copied to public GitHub.
- **Positive:** reproducible source/version inventory and independently categorized readiness changes, achieved.
- **Negative:** identity/provenance contradiction, invalid AST or unsupported generalization; not observed in bounded checks.
- **Abort:** physical TX, security material disclosure or changes to known-good production YAML. No abort or rollback needed; production V5DCM2 FIX1 unchanged.
- **Unknown:** exact RAUC version→app-source provenance, XTR local handshake acceptance, DCM icon, online status, sender and response slot.

## Next experiment
**V5DCM10 — PREPARED / NOT RUN:** offline mapping of each RAUC image to contained app version using checked hash/provenance, then check which session-state changes are wire-observable. Baseline V5DCM9; no TX. Positive criterion unambiguous source-chain match; negative ambiguous/irreproducible extraction; abort secret disclosure or live hardware action. Recovery none.

The user-facing offline archive `V5DCM9_FIRMWARE_VERSION_AUDIT_20261017.zip` contains a sanitized reproducible `audit.py`, JSON file inventory and report.
