# V5DCM15 — conservative offline CM930 session bookkeeping — 2026-10-17

**Status:** COMPLETE / POSITIVE for isolated, synthetic fail-closed model; COMPLETE / INCONCLUSIVE for vendor runtime parity / native XTR acceptance. No live test.

**Hypothesis/baseline:** Separating FC23 shape, FC16 page observation, package required, package received, handshake authorization, display and Online prevents false-positive native acceptance. Baseline V5DCM8 offline provenance observer and V5DCM11 firmware readiness gate; user-tested V5DCM2 FIX1 unchanged RX-only.

**Exactly controlled change:** A standalone no-I/O Python observer; records observed configuration/runtime starts separately, tracks a *synthetic* selected request-bit set and explicit receipt events, rejects unknown package indices, and retains native_accepted=false, display/online/epoch/owner=UNKNOWN and tx=false. No original CM930 vendor code execution or physical TX. **18/18** combined offline assertions passed, including old-source map validation, duplicate receipts, unknown receipts, reset, multi-bit set, FC23 alone not accepted, and TX false.

**Important semantic limitation:** model's `ready` is a conservative test projection and NOT complete original vendor `CMClientParameterUpdateState` parity. Original new vendor code can remain WAIT when seeded with an empty expected package set, and an event may be required to advance; no equivalence claim. No true XTR profile, owner/epoch or successful native acceptance evidenced.

**Positive:** fail-closed synthetic behavior for tested cases, MET. **Negative:** false acceptance/online/tx in those fixtures, not observed. **Abort:** unauthorized physical TX, speculatively assigning controller acceptance, source secret publication. **Recovery:** offline discard; V5DCM2 FIX1 unchanged.

**Next:** V5DCM16 PREPARED / NOT RUN — reconstruct historical challenge/response boundaries with provenance and timing; no live TX.
