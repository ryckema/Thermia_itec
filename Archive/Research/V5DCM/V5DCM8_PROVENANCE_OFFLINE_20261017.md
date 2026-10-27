# V5DCM8 — fail-closed provenance-aware offline observer (2026-10-17)

**Status:** COMPLETE / POSITIVE for offline bounded replay; COMPLETE / INCONCLUSIVE for native accepted session, DCM icon and Online. No live test or YAML update.

**Hypothesis:** separately representing exact native FC23 request-shape, response-shape, bounded temporal pairing, configuration sequence and mailbox activity avoids accidentally promoting weak evidence into owner/epoch, authentication or TX authority.

**Baseline:** V5DCM4–7 (seven existing CRC-validated genuine/collaborator text capture files; 25,031 records); live known-good V5DCM2 FIX1 read-only.

**Exact change:** create new standalone passive Python Evidence model and replay driver; no shared ESPHome code, no TX/DE, no private challenge transform or mailbox command implementation.

**Result:** 7/7 existing capture inputs replayed successfully, 164 exact challenge-shaped 0x0F FC23 request records in total, seven reply-shaped records correlated within 200 ms, one uninterrupted reference 32-page run (Oct-03 capture), zero premature upgrades to owner, controller epoch, native acceptance, display icon, online or TX authority. Mailbox-without-same-capture-FC23 counterexamples retained. Observational status capped at time correlation; **not** a proof of transport sender or actual DCM acceptance.

**Positive criterion:** all real-record replay inputs pass counters and fail-closed gates, MET. **Negative criterion:** mismatched counts or unsourced acceptance, NOT OBSERVED. **Abort criterion:** any hardware command/write, publishing private secrets or treating text timestamp as physical wire slot. **Recovery:** discard offline work; production V5DCM2 FIX1 untouched.

**Evidence classes:** observed = supplied text frame timing/count; firmware-derived = separate CM930 acceptance and package readiness states; hypothesis = cold session identity can be recovered with independent provenance; unknown = sender, slot, hardware DE, XTR accepted, icon, cloud connectivity.

**Next:** V5DCM9 PREPARED / NOT RUN, offline only: compare recovered Connect v2.0.18/v2.1.105 software state/packet logic for version-dependent differences, excluding private response and command secrets.

**Local artifact:** `V5DCM8_PROVENANCE_OFFLINE_20261017.zip` with model and executable offline replay tests (not automatically published in public repo).
