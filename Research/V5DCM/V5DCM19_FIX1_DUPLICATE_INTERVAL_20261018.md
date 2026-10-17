# V5DCM19 FIX1 — duplicate interval key removed (2026-10-18)

**Status:** PREPARED / NOT RUN. The previously delivered V5DCM19 YAML had two top-level `interval:` blocks, at about lines 205 and 3764. That violates the one-key configuration requirement and can lose existing scheduled automations or fail parser validation. Previous report's 8/8 syntax assertion was insufficient; it did not detect duplicate map keys.

**Baseline:** V5DCM19 diagnostics candidate, user-supplied V5DCM2 RX-only ZIP; byte equivalence to deployed FIX1 remains unproven. **Controlled change:** move the new `[V5DCM19]` 30-second diagnostic interval item under the one existing production `interval:`. All other YAML content kept identical, archive components unchanged.

**Verified offline:** strict duplicate-key YAML loader with `!secret` placeholder PASS; exactly one top-level interval; 16 periodic entries retained in aggregate; exactly one V5DCM19 diagnostic callback. No ESPHome compile, no hardware, no bus TX. **Positive** syntactic correction done. **Negative** old candidate has duplicate key (do not flash). **Abort** if any existing scheduled task disappears, production compile fails or native TX is enabled. **Recovery:** revert to deployed known-good V5DCM2 FIX1, not unverified archived candidate. G01–G06 accepted risk decisions unchanged.

**Artifacts:** `V5DCM19_RX_ONLY_FIX1_20261018.zip` and standalone YAML. Next verify installed FIX1 baseline equivalence and optionally ESPHome compile before first live RX-only result.
