# V5DCM18 — original-roadmap offline replay follow-up (2026-10-17)

**Status: RUNNING / PARTIAL** for original roadmap V5DCM18. Preserve the earlier V5DCM18 source/API audit as separately scoped historical result; it is **not** proof of full end-to-end fault replay.

Baseline V5DCM16 7 captures, V5DCM17 lifecycle gates, firmware-repo reference model and tests, deployed V5DCM2 FIX1 RX-only/HARD_DENY.

Controlled change: independent passive capture-only parser replay and synthetic fault fixtures; no ESPHome update, bus transmission or original reference-core change.

**Observed:** 25,031/25,031 CRC-correct bus-text records; 164 exact 0x0F FC23 request shapes; 7 bounded time-paired response shapes; strict 32-page reference sequence once in Oct-03 log. Cross-model profile differences remain. **Structural synthetic checks:** 49/49 passed over seven captures and four modifications (remove 03FC page, duplicate request, interrupt recording, inject CRC-invalid ACK-shaped data). These are deliberately conservative no-authorization assertions, **not** original firmware/Core semantic state tests. They cannot demonstrate correct ACCEPTED transitions: the capture observer deliberately never grants acceptance or TX.

**Positive criterion** limited historical-shape replay MET; **full roadmap end-to-end stateful replay** NOT MET. **Negative** none in these structural checks. **Abort** no active payload, no private authentication distribution, no unexpected TX, no production modification. **Recovery** no changes to restore.

**Unknown:** native XTR acceptance, owner, controller epoch, electrical slot, icon/cloud and correct semantic transition behavior under faults. **Next:** run the pre-existing original firmware-repository reference-Core test suite with seven capture fixtures and extend it with stateful adverse scenarios; only then mark roadmap V5DCM18 COMPLETE. See user-delivered local V5DCM18_ROADMAP_PARTIAL_20261017.zip for reproducible limited script and JSON.
