# V5DCM28-EPOCH-GUARD-01 — private RX-only rejoin hardening and lifecycle-provenance check

**Status: COMPLETE / POSITIVE — offline source/static/host regression only (2026-10-18).** No ESPHome compilation, user flash, electrical TX, controller epoch/ownership proof, application acceptance or online connection. The user-flashed **V5DCM23 FIX2 remains RUNNING / PARTIAL**, last supplied live log 1/33 significant groups.

## Scope, baseline and one controlled source change

**Hypothesis:** the V5DCM27 offline prototype allowed a stale or repeated positive epoch **label** after a later FC23 revocation; this should fail closed independently of the existing separate trust question. A monotonically advancing label is only a guard, never evidence that the physical controller actually changed sessions.

- Known-good local tested device baseline: V5DCM23 FIX2 user-flashed, RX-only, B11C/B11D parity in its short log, existing HA observations and TX HARD_DENY. Exact flashed image identity remains unverified; this step does not change it.
- Offline source baseline: user-private `V5DCM27_REJOIN_SEAM_OFFLINE_ONLY_NOT_FOR_FLASH.zip` SHA256 `f7aca0e40cb15b8d306e89ee0ab414917d1e0f1d4431f069759d1b017c69197f`. The previous candidate contained the inert, unwired `reselect_after_verified_session(epoch_label, proof_flag)` API.
- **Single controlled source change:** a guard in `v5dcm23_v5dcm19_real_ledger.hpp` rejects `epoch_label <= last asserted label`, in addition to the existing no-boundary/no-proof/zero-label checks. No other implementation was changed; the 40 original dependencies, actual ESPHome YAML, entities, UART, DE, native responder and TX path were **not modified**.
- New private, **nonflashable**, source-only ZIP `V5DCM28_EPOCH_REJOIN_GUARD_OFFLINE_ONLY.zip`, SHA256 `c92ffff1aaefef81a4901e8eb0b90baa02c0fa96c2b61f59249e14239eaab687`. Only revised header, unmodified existing gap24a/b observer headers, offline regression sources and README are included. This is NOT a full production configuration or firmware image.

## Actual tests and reproducibility

**Test A — compiled actual private V5DCM23 ledger and original portable CRC/frame source** using `g++ -std=c++17 -Wall -Wextra -Werror -pedantic`, linked against unchanged original `xtr_wire.cpp`, `xtr_frame.cpp` and `xtr_core.cpp`. **PASS** for two runs: one synthetic checksum-valid FC23 and a second run using the original checksum-valid 0x0F FC23 extracted from user historical `thermia_capture_20261003_165355.log` (historical frame bytes deliberately not published). It exercised:

- after boot profile selection, real-sized strict `03E8/count14` data gives 1/33;
- observed native FC23 invalidates profile; later data never automatically reselect;
- no boundary, absent externally declared proof and zero label are rejected;
- a **synthetic host-only** externally asserted label 7 lets the inert API reinitialize once; successful group receipt resets to 1/33;
- after next FC23, reused 7 or older 6 fails, 8 with no independent proof fails; 8 with host fixture assertion reselects new 0/33;
- after a later integrity revocation, stale 8 remains rejected;
- both `tx_authorized` and `online_or_controller_accepted` remain false in every stage.

**Test B — compiled unchanged production-style `gap24a_session_gate.hpp` and `gap24b_evidence_adapter.hpp`**, same strict compiler flags: **PASS** over fresh, retained and recovery candidates. Historical-only data, out-of-epoch events or absent independent witness do not qualify a current candidate. Even when a synthetic *current local* independently-witnessed context is admitted, `epoch_proven`, `owner_proven`, `ack_authorized`, `tx_authorized` and `semantic_write_authorized` remain false. CRC failure revokes the candidate.

**Important negative boundary:** these flags are test-fixture assertions; neither the V5DCM27 prototype nor this offline test has access to a real independent session-epoch/owner witness on the current XTR. The real FIX2 log showed **no FC23 boundary**, so the prototype rejoin behavior does NOT explain the initial live 1/33.

**Artifact source hashes:** revised header SHA256 `ba04d8f383c8ba89a2fce213d3e169c24c8b6aeec94c59a0c4f69bc1553b976b`; epoch lifecycle test `61c2e63320c220969ec9641b669b49ecc179f3776bb228af83de99b6690993af`; three-path test `b2f1fb9a35ad7171be1109be5be4759504904a0835dfcaefd6d222dca66a06d2`.

## Findings, limits and immediate next action

**PROVEN / source-host:** V5DCM27 prototype's previous stale-label acceptance existed in unmodified source; this single condition now rejects it under tested transitions. Source-backed gap24A/B context classification never confers epoch/owner/physical slot or any native TX permission. The existing V5Dcm23 ledger's boundary revocation and selected profile shape accounting remain intact.

**STRONGLY SUPPORTED:** session and packet completeness are separate axes. A verified, externally sourced controller generation should eventually reinitialize only the RX package collector, while physical responder authorization requires additional independent ownership/slot validation. Reusing a V4.1 historical success log as proof of the *present* controller generation is forbidden.

**OPEN:** trusted current-session witness and native owner, exact flashed FIX2 provenance and HA registry; live response slot and physical/electrical TX; genuine native Connect readiness/C2/Online; old independent Stage-D D=4 initial trigger. Historical full package shape counts are not a completed present-time session.

**Next candidate V5DCM29-SESSION-PROVENANCE-CONTRACT-01: PREPARED / NOT RUN.** One offline controlled integration test should make the external epoch/profile provenance API typed and anchored to the *already-present* V4.1 proven fresh/retained/recovery state boundaries without asserting any proof from packet shapes, bus silence, ESP boot, ACK or fixture labels. Establish a clear trusted-evidence interface before any production YAML wiring or live native TX. Preserve all current FIX2 HA entities, diagnostics, parity, physical TX HARD_DENY and rollback. If no independent current-epoch witness can be supplied, report **INCONCLUSIVE** and stay RX-only; never silently manufacture one.

**Pending distinct live observation:** V5DCM26-LIVE-OBS-01, **PREPARED / NOT RUN**, same already flashed FIX2 for 15–20 min passive logging, no configuration change. No test requiring a genuine DCM module.

**Abort/recovery:** this run had no hardware action, so no device rollback is applicable. Later any native TX requires a separate scoped user-initiated experiment identifying address, response slot, exact private payload, present controller state, timing/retries and abort/recovery; none of those are established here.

**No protected native response implementation, private mailbox logic, security algorithm or credential is published in this report.**
