# V5DCM19 — fail-closed observation/authorization contract (2026-10-17)

**Status:** COMPLETE / POSITIVE — 15/15 isolated synthetic offline contract tests; COMPLETE / INCONCLUSIVE — actual portable C++ Core parity, deployment integration, physical TX and local XTR approval. No new ESPHome YAML, compile, flash or physical bus TX.

## Number, hypothesis, baseline, controlled change
**Hypothesis:** explicitly separating frame observation, session authorization and state commit blocks false native-session acceptance when an FC16 has the right shape but lacks qualified provenance.
**Baseline:** V5DCM18 source review of current public `components/thermia_portable_bridge/xtr_core.cpp` and `xtr_core.hpp` (particularly pre-authorization handshake mutation in `Core::fc16_decision`, and externally supplied `qualify_handshake`, `set_mailbox`, `write_ready`); original CM930 firmware-derived independent lifecycle gates; user-deployed V5DCM2 FIX1 RX-only/HARD_DENY.
**Exact controlled change:** build and execute an **isolated, non-transmitting Python reference contract**: `observe` is pure, `authorize_acceptance` checks CRC/0x0F FC16 shape and independently supplied source/epoch/session witnesses, `commit_acceptance` alone changes state; mailbox entry has an explicit separate gate, and full Connect readiness is separate from a bus handshake. All witnesses are synthetic test inputs, NOT verified local XTR physical observations. This experiment does NOT patch the original C++ Core, implement FC23 responder, create a write API or drive serial hardware.

## Safety / relevant protocol context
Relevant **observed-only** address/context: native slave `0x0F`, FC16, `0x03E8/count14` local baseline example, `0x085F/count5` excluded from the earlier firmware acceptance selector; FC23 approval remains unhandled. The historical 2026-10-03 cross-model `0x03E8/count13` is not silently substituted for the local count14. No write target, values, CRC construction or transmitted payload exists. A frame match never authorizes native output.

## Executed tests (local isolated Python)
15/15 `unittest` tests PASSED, exit code 0. Covered: observation without mutation; deny missing source; deny missing epoch; deny missing qualified session; deny bad CRC; deny excluded FC16 start; deny foreign slave; separately authorized acceptance in synthetic fixture; reject mailbox before acceptance; reject mailbox missing witness; explicitly enable mailbox when synthetic evidence is supplied; require semantic profile and required packages separately; block output absent physical exclusive-slot evidence; denied event never promotes native TX.

**Limitation:** a fully populated synthetic `Authority(True, True, True)` is only a test fixture. It is not an authenticated current-session witness. The reference model includes a `tx_allowed=False` default, but this is not a tested physical DE or XTR line. The test intentionally does not validate the C++ Core code paths; thus a claim that the original `Core::fc16_decision()` bug is already fixed would be false.

## Evidence classification
**OBSERVED locally in offline test:** all 15 synthetic assertions passed; no serial/USB/ESPHome interface was invoked and no production files were changed.
**STRONG CONCLUSION:** a three-phase pure-observe / explicit-authorize / commit contract *can* keep denied events from changing acceptance in this reference model; original C++ source from V5DCM18 still has the issue until patched and retested.
**HYPOTHESIS:** a similarly split C++ API can remove the same ambiguity without changing unrelated production entities, if all call sites and delivery/commit ordering are reconciled.
**UNKNOWN:** actual local XTR sender, controller epoch, physical frame EOF, exclusive response slot, acceptance, application readiness, display and Online; parity of the Python reference with compiled C++ or recovered vendor firmware.

## Positive / negative / abort / recovery
**Positive:** all 15 synthetic tests pass and fail-closed invariants hold — MET.
**Negative:** a denied event promotes acceptance or output — NOT OBSERVED in these fixtures.
**Abort:** any physical TX, fabricated provenance/ownership, inclusion of private active authentication/mailbox tool code, or promotion of test fixtures to XTR proof — NOT TRIGGERED.
**Recovery:** discard isolated Python test files; V5DCM2 FIX1 remains RX-only/HARD_DENY and the portable public C++ source was not patched.

## Artifact
`V5DCM19_OFFLINE_CONTRACT_20261017.zip` (conversation download) includes `contract.py`, `test_contract.py` and `TEST_RESULTS.txt`. Not uploaded as a working native TX implementation.

## Next — V5DCM20 PREPARED / NOT RUN
Offline C++ source patch/test in a separate branch or isolated copy: remove handshake mutation from the classification method, add explicit provenance-qualified transition commit and negative tests; analyze all existing call sites and commit/delivery order before changing code. Preserve original production configuration, make no native TX available; positive full C++ offline regression including denied FC16 and retained/recovery cases; negative incompatible API or failing fixtures; abort any TX-authority or electrical-owner inference; recovery revert isolated patch. No live experiment is authorized.
