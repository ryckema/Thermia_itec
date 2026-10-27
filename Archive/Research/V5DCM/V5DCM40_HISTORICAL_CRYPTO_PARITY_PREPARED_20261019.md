# V5DCM40-GENUINE-DCM-HISTORICAL-PARITY-01 — experiment contract
**Prepared scope: PREPARED / NOT RUN (offline only), 2026-10-19.** Executed results are separately recorded in [RESULT](V5DCM40_HISTORICAL_CRYPTO_PARITY_RESULT_20261019.md).

## Hypothesis and previous evidence
V5DCM39 left genuine native cryptographic parity OPEN despite existing evidence in the original firmware repository from 2026-10-05. A pinned existing firmware-derived reference should reproduce the **seven genuine historical DCM response pairs** from the independent Eco5 gateway and ATEC+DCM03 captures; those reference-verified records should then pass through the actual V39 request-binding seam as **host-mock-only** cases without granting controller/Online authority.

Known-good deployed baseline remains **V5DCM33-FIX-B2**, last user-confirmed 204 s RX/HA stable, software executor 393/393 HARD_DENY, UART writes=0, actual OTA binary digest unverified; rollback V5DCM23 FIX2 RX-only. V4.1 EXP386/387 historical local positive, EXP388 running/partial; V5DCM32 live fresh rejoin complete/negative for integrity. Prior V35–V39 are source/host-only, not an ESP32-native accepted session.

Relevant other results: Thermia_Connect_Firmware `findings/CM930_HANDSHAKE_CORPUS_VALIDATION.md` already reports 7/7 original genuine responses and `findings/CONNECT_2.0.18_VS_2.1.105_PROTOCOL_DIFF.md` reports source-level cross-version stability. The existing reference script `tools/validate_cm930_handshake.py`, Git blob `2aeb56f3afb60414f0527acd6960996219a0b0fb`, is an **external confidential source dependency** (not republished).

## One controlled change and target
Create a **separate, offline-only** source- and capture-pinned verification suite. The original V39 ZIP SHA256 `35195716ec530ee512776e9bd6aba3a3780bcf0635edc0554d6745f6e11ebada` and existing B2/ESPHome/YAML/HA, bus RX parser, TX driver and sticky fault history are unchanged.

- Inputs: historical genuine slave 0x0F FC23 challenge/reply records in independent Eco5 Sep26/Sep28 and ATEC+DCM03 Oct03 collaborator captures, validated CRC and request geometry.
- Output: aggregate offline proof of exact reference parity, plus a recorded-only host fixture fed through the existing V39 one-request/one-use provider.
- **NO native outgoing address/payload/CRC/live retry/physical timing/current XTR register value exists in scope.** No physical TX; no thermal effects or hardware risks. Historic 29–63 ms response delays are capture observations, NOT an authorization or prescribed future TX schedule.

## Positive, negative, inconclusive, abort
**POSITIVE** for the stated offline hypothesis: exact prior-reference blob pinned; all seven captured answers reproduced byte-for-byte; all genuine pairs CRC-valid; reference replay rejects altered CRC, altered reply with recalculated CRC, and noncanonical requests; the original exact V39 source passes recorded-pair-only mock tests with one-use and zeroization; V39/V38 regressions still fail closed; private artifact hash/ZIP membership/fresh re-extraction complete. Never promote mock or historical cipher parity to current XTR acceptance.

**NEGATIVE**: cryptographic mismatch, source-pin failure, malformed captured frame accepted, fixture replay permits altered unknown challenge, stale/error bypass or embedded live TX API reachable. **INCONCLUSIVE**: necessary original captures/reference missing or test cannot complete. The local XTR live/Online state remains OPEN even after successful offline validation.

**Abort/recovery**: immediately stop offline validation and discard new separate sources if any source pin, control or output barrier fails; running user's FIX-B2 remains untouched. A later physically active experiment is distinct and must specify exact privately reviewed frame/CRC and current XTR state/owner/epoch/slot, expected effects, maximum one scoped response, abort/rollback and evidence criteria.

**Provenance requirement:** Oct03 `thermia_capture_20261003_165355.log` is **genuine collaborator ATEC+DCM03**, NOT local XTR M. Sep25 older `thermia_capture` model identity is unresolved; do not count those as locally proven XTR. Older V35–V39 source reports containing erroneous local labels remain historical and are corrected transparently in the result. No recovered algorithm/key/private native reply implementation will be added to this public repository.
