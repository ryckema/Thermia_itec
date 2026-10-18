# V5DCM24-SOURCE-GATE-01 — offline Stage-D and Connect package-request audit

**Status:** COMPLETE / POSITIVE **for offline source analysis and controlled host replay only** (2026-10-18). **V5DCM23 FIX2 remains RUNNING / PARTIAL** on the user's XTR M. No ESPHome edit, device flash, active TX, or controller acknowledgement in this step.

## Hypothesis and baseline

Hypothesis: the live `[R6-P30EC] D=4 STAGE_D_LEDGER_FAULT / INTEGRITY_HOLD_NO_TX` reflects a separate, sticky 32-page transport/state gate rather than a contradiction of clean current B11C/B11D RX or the new V5DCM23 33-group portable package receipt.

Known live baseline: V5DCM23 FIX2 user-flashed RX-only first log, real portable ledger `1/33`, matching interim `03E8/count14`, B11C/B11D clean within captured interval, `DE=0`, TX HARD_DENY software counters; source/binary byte identity remains unproven. Preserve deployed configuration.

Offline input provenance:
- Private user-uploaded FIX2 ZIP SHA256 `561169c31d5a7eb341055fdb37d0302b4816d661fff9cd2df9d607a9498ea9a4`; its YAML SHA256 `04f562e2ccf5374ca890c5f107ee38e1fa108251dc80926cc3ba12c85004ed13`.
- Original `device_client.zip` SHA256 `18ebe6190bbcfff364ca27af9dbf31c8b6e66a7a828d7869b00d32f7012590ac`. Source reviewed: `device_client/cm/modbus_server15.py` and `device_client/cm/cm_client_type.py`.
- Historical reference byte capture `thermia_capture_20261003_165355.log` SHA256 `14918065297264473e2357822a8694d184e7821b8c2a3b1cb316039678a708a1`. **Not the live V5DCM23 FIX2 console log**, nor proof of current XTR geometry: historical first significant block is `03E8/13`, whereas live XTR uses `03E8/14`.

Controlled change: none to software source or hardware. Reused the exact embedded Stage-D source definition for an independent host C++17 harness, with its source-defined geometry rules, then fed CRC-validated reference frames; tested two targeted synthetic counterexamples. This is host source execution, **not** an ESPHome firmware compile.

## Observed source facts

1. R6 Stage D is a **32 ordered settings-page + matching FC16 ACK** transport ledger. It has distinct states idle/await ACK/await page/32-32 complete/**sticky hold = 4**. It checks geometry/profile consistency, ACK matching, timing and sequence. A hold is not automatically cleared by later good RX or a repeated canonical FC23. R6-P30EC mirrors Stage D's state and latches `STAGE_D_LEDGER_FAULT` on failure. Therefore `D=4` and clean B11C/B11D / V5DCM23 package receipts can coexist without inconsistency.
2. Stage-D full progress is **transport observation only**. No owner, controller epoch, response slot, native session acceptance, or TX authority is established by 32/32, much less by `1/33`.
3. Original Connect CM930 source computes significant numeric dependencies from the sensor/configuration profile into package groups. A separate update-state object tracks pending package bits and clears them when corresponding package receipts are reported; the CM client also maintains the register-request masks. Runtime/request lifecycle and accepted handshake are distinct from passive reception. **The derived 33 significant groups are readiness criteria, not 33 automatically broadcast messages**. Source logic does not prove that all will appear on an unauthenticated passive bus. No unpublished authentication/cryptographic implementation is included here.
4. HA baseline inventory: public full RX33 + statistics-fix YAML contains **187 named sensors + 60 binary sensors + 15 text sensors = 262 named HA entities** (plus a YAML `esphome.name` field, not an HA entity) and 74 `state_class: measurement` entries. Private FIX2 YAML contains **117 sensors + 13 binary sensors + 47 text sensors + 3 buttons = 180 named entities** and 31 `state_class` declarations. **This is a net 82 fewer named entities, NOT an identity-level missing-name comparison**; private FIX2 has extra diagnostics. Do not overwrite a broader known-good HA production configuration without explicit identity-level reconciliation. Do not delete HA historical statistics.

## Host test results (source-extracted Stage-D implementation)

- Host C++17 `-Wall -Wextra -Werror -pedantic` source compile: PASS.
- Full historical reference feed: 2,687 frames / 2,687 CRC-valid; Stage-D reference run reaches **32 pages / 32 ACK / state 3**, with shape selected from reference `03E8/13`. This supports reproduction of the old *transport ledger*, not local XTR acceptance.
- Synthetic local-shape baseline `03E8/14` + matching ACK + repeated same settings page instead of next: **state 4**, reason `DUPLICATE_OR_OUT_OF_ORDER_SETTINGS_PAGE`.
- Synthetic first page without ACK past its window: **state 4**, reason `ACK_TIMEOUT_1500MS`.
- No physical TX, live test, controller restart, firmware alteration, or private response implementation.

**UNKNOWN:** actual reason/timestamp of live FIX2's first Stage-D hold because this step did not have the original `[R6-P30D] HANDOFF_ABORT reason=...` line from its live console. Do not assert that repetition or timeout actually happened on the XTR. No known-good baseline is superseded.

## Conclusion and next action

**PROVEN (source/host scope):** D=4 is a separate, sticky fail-closed gate; 32 transport pairs and 33 significant semantic package groups are distinct. Historical reference replay and synthetic guards behave as described. Connect firmware uses an active package-request/readiness lifecycle, so `1/33` does not by itself indicate an RX parser fault or require a fake passive 33/33 result.

**STRONGLY SUPPORTED:** native Connect initialization/request lifecycle is a more promising next research axis than waiting for all 33 pages to arrive without a recognized session.

**OPEN:** exact current Stage-D first-fault provenance, whether original 33 masks get asserted in an accepted live XTR session, authoritative owner/epoch and true native application acceptance, source/binary authenticity, full HA entity identity parity, electrical TX measurement.

**NEXT:** source-only map of the verified, non-sensitive package-request lifecycle to observed XTR request/response direction and ordering, and reconcile lost HA names before any further device image. Existing FIX2 live test remains RUNNING / PARTIAL. If future diagnostic evidence is needed, request only the earliest `[R6-P30D] HANDOFF_ABORT` line (not another full compiler dump), while retaining current read-only setup.

**Safety/rollback:** no write target/payload; no extra bus traffic; zero retries; no rollback necessary. For any later physical test require bounded slot authorization, no output by default, preserved HA and rollback to known-good RX-only.
