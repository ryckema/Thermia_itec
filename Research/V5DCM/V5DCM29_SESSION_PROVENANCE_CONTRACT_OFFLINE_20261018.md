# V5DCM29-SESSION-PROVENANCE-CONTRACT-01 — separated controller epoch and V5 local rejoin generation

**Status: COMPLETE / POSITIVE for one source-only design implementation and reproducible strict host tests.** 2026-10-18. **Physical/session qualification on current XTR: OPEN / UNKNOWN; no on-device V5DCM29 test performed.**

## Hypothesis and verified baseline

**Hypothesis:** the V5DCM28 source-only rejoin seam conflates a monotonically increasing numerical *local session generation* with a *physical controller epoch*. Those are not equivalent: a retained session can require a fresh local RX-readiness generation while the same controller continues running. A strictly typed, nontransmitting provenance contract can model fresh, retained and recovery separately, refuse stale/untrusted evidence, and prevent passive shape observers from promoting themselves to response ownership.

**Baseline:** user-flashed **V5DCM23 FIX2 RX-only, RUNNING / PARTIAL**, last ~2m25 live source log, native strict package `1/33`, B11C/B11D clean, software TX HARD_DENY; exact flashed image digest, physical controller epoch and owner unverified. **Do not replace this image.** Older V4.1 EXP386/387 locally confirmed guarded recovery and delayed semantic re-arm; EXP388 two restart recoveries but some cancellation branches untested (RUNNING / PARTIAL). Existing V5DCM28 source-only ZIP SHA256 `c92ffff1aaefef81a4901e8eb0b90baa02c0fa96c2b61f59249e14239eaab687`, NOT a full flashed image. V5DCM26-LIVE-OBS-01 remains PREPARED / NOT RUN.

**Single controlled change:** create a **separate, unconnected, nontransmitting C++17 evidence-contract header** with explicit `physical_controller_epoch`, `local_session_generation`, `independent_event_sequence`, fresh/retained/recovery path and a bounded-age evidence assessment. Use existing `gap24a_session_gate.hpp` and `gap24b_evidence_adapter.hpp` from V5DCM28 unchanged. Do not modify the V5DCM28 packet ledger, existing V5 parser/callback, public Write Beta, ESPHome YAML, HA identities, DE or TX.

## Source facts versus proposed abstraction

**Source-observed:** V5DCM28 `NativeRxLedger.reselect_after_verified_session(proven_controller_epoch,proof_flag)` rejects `proven_controller_epoch <= controller_epoch_`. That safely prevents repeated labels in an offline fixture, but treats that one integer simultaneously as the *current physical controller identity* and a *strictly monotonically increasing local session label*. This is insufficient for a retained rejoin where the physical controller may legitimately stay the same. V5DCM28's method also has no real trusted physical proof provider; its `proof_flag=true` is a host-fixture assertion, not an actual owner/epoch attestation.

**Source-observed:** GAP24A/B classify `FreshCandidate`, `RetainedCandidate`, `RecoveryCandidate` from the provided source metadata, while `epoch_proven`, `owner_proven`, `ack_authorized`, `tx_authorized` and `semantic_write_authorized` stay false. The `independent_physical_witness` boolean in an input event is **not itself a verified hardware attestation**.

**New offline contract:**
- `Fresh`: requires a separately attested physical restart/new epoch, and a strictly newer LOCAL session generation.
- `Retained`: requires independently attested *physical continuity* (same physical epoch) plus newer LOCAL session generation; it must not demand a physically new epoch.
- `Recovery`: requires either evidence of physical continuity at the same epoch OR of an independently attested physical restart at a different epoch; reject missing/both contradictory evidence.
- For every path, reject historical, synthetic, cross-model or firmware-only source as current XTR authority, expired event, stale/reused local generation, missing post-boundary witness sequence, missing physical attestation, no pending boundary, candidate/path mismatch or purported owner/TX status from the passive observer. The age budget is a **test-policy input** rather than an invented real bus timeout.
- Return `RxReselectCandidateOnly` (host abstraction), with every owner, ACK, TX and Online flag **always false**. **Do not invoke the old ledger reselect with this pair of numbers.**
- `IndependentProof` has no public default constructor. The independent physical proof issuer is **not implemented**. An artificial `OfflineFixtureIssuer` is visible solely when `V5DCM29_OFFLINE_FIXTURE` is enabled for host tests. This is a source separation, **not cryptographic certification**. The positive fixture only demonstrates behavior IF such independently sourced evidence becomes available.

## Reproducible evidence and results

Host code in private user-download ZIP `V5DCM29_SESSION_PROVENANCE_OFFLINE_ONLY_NOT_FOR_FLASH.zip` SHA256 `2b044617411de452870ce70210c02fa0b3fd71e31815454248212881f23c2320`; new header SHA256 `a0df6c83c880371d7e4b72e391c8987ef95283e967f93958ef4aed09253bd6b9`. The archive contains no original private responder code, original captures, credentials, keys, payloads or mailbox tool. Not uploaded to public source tree.

Three separate strict host C++17 `-Wall -Wextra -Werror -pedantic` tests **PASS**:

1. **Lifecycle and denial matrix:** synthetic witness scenarios for fresh (new physical epoch), retained (same physical epoch with newer local generation), recovery with continuity or verified restart; negative cases missing current source, missing physical proof, historical source, expired/future event, preboundary/replayed evidence, stale local generation, missing physical epoch, wrong path, contradictory continuity/restart, reused physical epoch on a claimed restart, repeated use of evidence. No owner, ACK, TX or Online authority in any positive or negative case.
2. **Production-type fail-closed build without fixture issuer:** compilation succeeds with no independent proof factory; passive GAP24B candidate and `0x0F` frame metadata alone produce `MissingIndependentProof`, no requalification or TX.
3. **Exact original source integration:** compiled against the **unchanged V5DCM28 native RX ledger header** and original portable RTU CRC/frame C++ sources, fed the *unchanged first CRC-valid native 0x0F FC23* from historical `thermia_capture_20261003_165355.log` after a synthetically constructed, valid `03E8/count14` page. Existing ledger shows 1/33 then revoked; the V5DCM29 contract denies historical-only requalification, and the real ledger stays unselected after more valid FC16. This is NOT a run on today's XTR or controller acceptance.

**Explicit incomplete work:** no ESPHome compilation, flashing, live current-XTR rejoin, independent hardware witness, current physical epoch, physical TX/ownership measurement, native Online icon, HA parity restoration, or meaningful live received group beyond existing 1/33. A test-supplied proof is not a proved controller identity.

## Safety, conclusion, next experiment

**PROVEN (offline source/host):** local generation and physical epoch must be distinct state variables for retained rejoin; the original V5DCM28 numerical guard is not sufficient for that architecture. The read-only contract and exact-legacy-ledger integration fail closed when no independent proof is present. **STRONGLY SUPPORTED:** this separation is necessary before safe V4.1-to-V5 lifecycle joining. **OPEN / UNKNOWN:** source of current real hardware-independent physical session and response slot/owner.

**Next V5DCM30-INDEPENDENT-WITNESS-AUDIT-01 — PREPARED / NOT RUN.** Hypothesis: existing source/logs or tested hardware metadata (without new bus TX) may yield a sufficiently independent current controller transition/continuity witness; audit data provenance, live vs historical, first R6 D=4 cause, and explicit safety gates. **One controlled change:** research-only witness-source audit with no executable device change. Positive: real independently sourced present physical epoch/continuity anchor found; negative: evidence explicitly contradicts assumptions; inconclusive: no such reliable source (no grant). No active scans, unsolicited frames, setting writes, controller restart or removal of room sensor. Abort/recovery: offline only; current FIX2 stays known user-flashed RX-only. Required evidence if unavailable: smallest already-existing timestamped RX diagnostic around a proven user-initiated controller transition and source metadata, NOT a requested restart.

**Do not activate TX.** Future V5 package ledger adaptation and eventual user-initiated active test are separate experiments: native responder ownership, exact private wire slot/payload, current old/new setting and rollback must be documented before any real TX.

**Confidentiality:** no original 0x0F emulator, firmware security algorithm, 0x0708 mailbox implementation, challenge response, or private raw challenge payload is published.
