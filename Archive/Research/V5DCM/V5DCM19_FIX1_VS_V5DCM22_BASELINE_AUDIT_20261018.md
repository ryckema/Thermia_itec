# V5DCM19 FIX1 ZIP versus v31 FIX4 / V5DCM22 RX33 — provenance and baseline decision

Date: 2026-10-18
Type: **offline source assessment**, not a new executable/live experiment. No device action or GitHub production YAML replacement.

## Original user-provided artifact
The user supplied `V5DCM19_RX_ONLY_FIX1_20261018(2).zip`, local SHA256 **`ca1dd27231ff12d587c8931fda81d7f61fab9da84603fe11eee78c41b5ec75b5`**.

Contained principal YAML `waveshare-thermia_V5DCM19_RX_ONLY_PREPARED_NOT_FLASHED.yaml`, SHA256 **`44a9d82154aac71d1b17adf62ed0a9901a1c1bd334cb1a943d5b8eae15ad6612`**, 265,419 bytes. Includes a complete local `components/thermia_portable_bridge/` tree and numerous R6/GAP/V5 native observation-only headers.

Strict duplicate-key PyYAML loader with local `!secret` placeholder: **PASS**, 24 top-level keys, **one** `interval:` key containing 16 entries, **117** numeric sensor, **13** binary sensor, **47** text sensor, **3** buttons, **one internal** switch: **180 named HA objects** (including buttons). **31 numeric sensors** already declare `state_class: measurement` including Heating Minimum. This explains why the earlier full-monitoring v31 metadata loss could regress long-term statistics, but does not establish what firmware was running when a past HA warning appeared.

Native RX-oriented architecture: V5DMC1/2 CM930 shadow/challenge observer, V5/R6 frame/parser-parity witnesses, native session/retained-state diagnostics, three recurring `[V5DCM19]` log lines, portable bridge, `TX=HARD_DENY`. External `thermia_rx_shadow` component is pinned to public Thermia_itec commit `f8adf5fbd5cb69cc6a72cea913c6a46a48619a25`, not necessarily firmware-repo current HEAD.

## Critical provenance and safety qualifications
- **Original ZIP YAML itself says `PREPARED / NOT RUN` and its `V5DCM19_RESULT_PREPARED.md` says the archived V5DCM2 input candidate was NOT shown byte-equal to a deployed FIX1.** Do not promote filename to deployed source proof.
- Separately, the canonical [V5DCM19 live report](V5DCM/V5DCM19_FIX1_LIVE_RESULT_20261018.md) is **COMPLETE / POSITIVE** for 189 seconds of user-confirmed RX-only local XTR logs, and [V5DCM20 continuation](V5DCM/V5DCM20_LIVE_RX_ONLY_RESULT_20261018.md) is **COMPLETE / POSITIVE** for **18 min 33 s** source-independent on-device RX/parser parity and software-reported physical attempts=0. Thus a **V5DCM19 FIX1 configuration family** is a much stronger *actual native-DCM-oriented experimental baseline* than the unexecuted V5DCM22 RX33 candidate. Those logs do not certify this uploaded ZIP's exact SHA/version.
- Unlike public v31 FIX4/YAML candidate, **ZIP configures UART `tx_pin: GPIO17`**, though transceiver DE is GPIO21 `restore_mode: ALWAYS_OFF`, production policy is `TX=HARD_DENY` and local logs reported physical_attempts=0. It is **not as structurally RX-only** as v31, where UART has no TX pin. Retain explicit fail-closed guard in future candidates. Do not assume no wire TX by source labels alone.
- `SHA256SUMS.txt` has 58 historical entries; does **NOT list the principal V5DCM19 YAML**, newer FIX1 metadata and some added materials; additionally one README entry hash differs. Compute archive/YAML hashes from actual bytes as above, do not use historical manifest as proof of this ZIP's exact contents.
- Archive includes private/research-specific headers and shadow-response tool scaffolding. **Do not publish this uploaded archive or copy native security/response logic into the public repositories.** This report records only safe metadata.
- ZIP has **no** V5DCM22 source-verified **33 significant-package** coverage/HA flags and no v31 FIX4 **13-page** HA sensor. Principal ZIP is about **180 named HA objects** compared to the current v31/RX33 FULL monitoring candidate's ~259 named HA sensor/binary/text objects; names/IDs and actual production feature parity must be reviewed before porting.
- Neither locally parsed ZIP YAML nor newer RX33 STATCLASS FIX1 is established by this comparison as compiled/flashed/current. The user's latest “in orde nu” means the HA statistics issue appears resolved; do not infer exact installed YAML/hash without explicit evidence.

## Decision
**Prefer the confirmed user-tested V5DCM19 FIX1 *native observer/portable-bridge architecture* as the functional DCM integration baseline**, provided its exact deployed source can be reconciled with the uploaded archived ZIP. Separately preserve the current v31 FIX4/RX33 production sensor configuration and already-prepared `state_class` corrections as the HA entity/semantics baseline; do NOT wholesale revert HA to the smaller V5DCM19 map. Do not merge entire YAMLs or introduce a second UART consumer.

Best next scoped **offline** change: compare ZIP exact native callback/included bridge versions to current firmware `Portable`/V5DCM22 `PassivePackageIntegration`, then graft **only** the passive validated **33 W2/W3/W4 package ledger and scoped HA diagnostic** into the proven V5 native RX callback while preserving all intended HA entities and correct measurement metadata. Explicitly test existing parser parity and DE/physical-TX hard-deny. Preserve production YAML untouched until compiled source and user-driven live test evidence.

## Evidence classification
**OBSERVED:** uploaded ZIP bytes/hash/parse/top-level/platform inventory/TX pin metadata. **LOCALLY CONFIRMED in separate earlier live results:** V5DCM19 FIX1 telemetry and V5DCM20 18m33 RX-only parity. **STRONGLY SUPPORTED:** native DCM work should branch from the V5 observer architecture, not discard it for a separate simplified UART parser. **OPEN:** byte equality to flashed source, exact current on-device build after recent HA resolution, semantic/full HA migration, real 33-group native C2, controller epoch/owner/Online state.
