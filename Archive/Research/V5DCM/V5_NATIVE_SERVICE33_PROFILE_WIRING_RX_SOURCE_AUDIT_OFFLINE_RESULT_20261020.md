# V5 Native Service-33 — Staged profile integration and RX callback audit

**2026-10-20. ID V5-NATIVE-SERVICE-33-STAGED-RX-PROFILE-WIRING-OFFLINE-01. COMPLETE / POSITIVE — OFFLINE SOURCE/HOST AUDIT ONLY.** Physical XTR experiment PREPARED / NOT RUN. Existing user-confirmed V83 RX_ONLY/HARD_DENY unchanged; EXP388 RUNNING / PARTIAL; startup B11D first fault OPEN.

## OBSERVED FACTS
The existing private Service-29 staged ESPHome YAML presents canonical CRC-complete RX frames to one native service runtime, but it does **not** invoke the runtime methods for controller session binding, reviewed CM930 profile installation, verified runtime refresh or scoped arm. The active RX call's evidence is explicitly unverified: epoch=0, session false, peer absence false, physical slot false and native profile false. Runtime source refuses unbound and unarmed frames. Consequently the S29 version/profile gate, although covered by host unit tests, is **not connected to a current attested on-device CM930 profile lifecycle**. No production TX or real native Connect startup is implied by compilation or unit tests.

One original inherited V83 shared RX-supervisor header remains absent from the supplied staged archive; it is unsafe to substitute a dummy. The source has different V43/V44B RX hook callback predicates: original uploaded FAS1 requires a singleton complete frame and no trailing parser pending data, whereas the staged S29 hook forwards every completed frame only when the parser has no pending tail. The existing principal per-frame parser/ledger loop sees all CRC-valid frames. This is a verified *source difference*, not a verified on-device delivery failure. V5DCM80 previously proved the general RX callback asymmetry in original V49. V83 B11D startup misalignment was likewise already investigated offline; do not count it as a new S33 finding or assume it caused the observed earlier live fault.

## OFFLINE VALIDATION
- Exact uploaded private V83 FAS1 and S29 source inputs compared with pinned digests.
- **14/14** integration call-site and safety invariant checks PASS.
- Original unmodified V83 embedded C++ StreamParser extracted for **8/8 C++17 host assertions and 8/8 ASan+UBSan assertions PASS**, using only synthetic public/general Modbus read requests; no native response/authentication generation.
- Prior S29 host test runner rerun **32/32 executable invocations PASS**. These are host tests, including previously existing fake-I/O exercises, not physical bus delivery.
- **No ESPHome compile, user flash, active RS485 TX, controller test, electrical timing/peer identity measurement or original Connect C2/Online qualification.**

## CONCLUSION / NEXT
**STRONG CONCLUSION:** S29 cannot currently enter native session/profile readiness merely because its private version-gate header exists. Implementing the missing connection safely requires authentic original V83 RX-supervisor source plus independent local XTR same-session/epoch/profile evidence, and cannot be achieved by bypassing the existing fail-closed fields. Preserve original RX-only HA/V5 watchdog and B11D sticky diagnostics.

**OPEN:** original supervisor header, B11D early first alignment, source-to-live firmware equivalence, current original firmware/profile, owner/slot, actual semantic write and Online session. **NEXT:** obtain complete original V83 source ZIP (or precise original header with provenance), reconcile the V83/S29 RX delta, and only then plan a safely integrated receive-only observer. No automatic TX or repeat live tests. Private audit package SHA256 `7d997f63c0678a14827d76e69389f35a4ca897e895c2dce784cbe4934187e264`; non-public derived source not committed.
