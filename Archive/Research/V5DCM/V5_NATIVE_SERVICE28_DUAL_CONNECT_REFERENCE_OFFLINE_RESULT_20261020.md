# V5 Native Service-28 — Two genuine Connect reference datasets and profile admission

**2026-10-20 | COMPLETE / POSITIVE for offline source/host analysis only.** Physical XTR TX **PREPARED / NOT RUN**.

## Baseline and scope
Verified user-running V83 FAS1 RX_ONLY/HARD_DENY remains unchanged (SHA-256 b4aaedf27f8dd3d58fcc7c09316cfe03d9c8f41d40fcd827a31bf1f104d389fa). Continue ONE private V5/V4.1 native service from S27. EXP388 RUNNING / PARTIAL; B11D startup first-fault cause OPEN. No flashing, compile, controlled bus transmit, or controller restart.

## OBSERVED ORIGINAL FIRMWARE FACTS
Original user-uploaded Connect **2.0.18** and **2.1.105** extracted AppFS independently inspected. Native CM930 data-package list is built by `cm/modbus_server15.py::_get_all_data_package_to_request()` from significant registers of the **sensor and configuration** parsers. The original extractor considers formula/conditions/min/max/default token references. Those numeric references are mapped to W2/W3/W4 via original byte-identical mailbox group map (SHA256 bb0b335eaf4e3a98e5d71d1cd1551e0772fedcfcd3f7d17f3c78e04c21844b9e).

- Connect **2.0.18** profile directory `2.3.0-2.4.1`: 529 unique significant registers -> **31** request groups (**23 settings, 8 operations**).
- Connect **2.1.105** profile directory `2.3.0-2.4.3`: 541 unique significant registers -> **33** request groups (**25 settings, 8 operations**).
- Two additional groups in 2.1.105: **0x04BA** and **0x06F4**. **Zero** unmapped or ambiguous significant registers in either reference extraction.
- The shared bit map being identical does **not** make the version-specific significant-group list identical. These are Connect release-profile facts, not authenticated local XTR profile identification or XTR C2 proof.

## IMPLEMENTATION — existing private Service27 codebase
- Added source-generated, immutable dual reference sets and a strict exact-set comparison to the existing profile-admission path. Incomplete, substituted, duplicate, collaborator/unknown, or stale-epoch synthetic declarations are denied.
- Replaced the staged ESPHome runtime's boolean-only `install_cm930_verified_profile` method with `install_cm930_reviewed_profile`, requiring both a user-reviewed S27 profile declaration and a chosen genuine firmware reference set, in an already bound controller session. This is still a **caller-attested interface**, NOT independent cryptographic source verification. No automatic dataset/profile selection or actual TX ARM.
- No new UART parser, observer, HA entity, direct UART write, GPIO21 DE assertion or second physical output actor. Default installed V83 remains TX=HARD_DENY; private source package remains PRIVATE.

## ACTUALLY EXECUTED
- **31/31 C++17 host test executables PASS**, including 2 FakeIo TX build variants and new 31-vs-33 exact-set/rejection tests. No actual UART output.
- **3/3 targeted ASan/UBSan test executables PASS**.
- Original AppFS extraction/source/hash check PASS.
- YAML structural verification: **24/24 original production top-level blocks**, **197/197 existing HA id/name pairs**, no S27 UART/interval/sensor changes, no added direct UART writes or DE turn-on. Verified original V83 source hash unchanged.
- Source ZIP `V5_NATIVE_SERVICE28_CM930_DUAL_REFERENCE_PRIVATE_20261020.zip` SHA256 `0a4769327706133c034e2f8393ddb1349d725940b8745b183c2c6526e7ae69db`; ZIP CRC and 172 member SHA256 verified. Staged YAML SHA256 `3fde8c9bd933b69cdbd2afbde7c9f55660c1603374b0b124a4761274229daa6c`. Private source/third-party firmware not uploaded to public GitHub.

## STRONG CONCLUSIONS / OPEN
C2/significant-group expectations differ even between TWO genuine Connect versions. The old assumption that 33 is universal is DISPROVEN. Actual current local XTR firmware/profile, version 0867, required list and local semantic write acceptance remain unverified. Historical 0x0F collaborator ATEC captures and older unknown-model logs are NOT current local XTR proof. V4.1 historical successes preserved.

## NEXT
Continue the same gateway codebase with exact local XTR version/profile evidence when available; do not manufacture a 31/33 choice to enable TX. A later integrated full-session live test can be substantial but requires specific user initiation and reviewed physical safety/abort/rollback. Maintain V83 FAS1 RX-only fallback, EXP388 PARTIAL and B11D fault provenance.
