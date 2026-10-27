# V5DCM10 — RAUC-to-device_client provenance verified (2026-10-17)

**Experiment status:** COMPLETE / POSITIVE for offline content provenance (both original RAUC bundles, four embedded ext4 image checksums, 46 extracted Python module byte comparisons). COMPLETE / INCONCLUSIVE for XTR-native authentication, handshake acceptance, DCM icon, cloud Online and independent RAUC signature trust-chain verification. No YAML compiled or flashed and no physical bus action.

## Hypothesis / baseline / controlled change
- **Hypothesis:** the 21-module `device_client 0.1.45` tree and 25-module `device_client 0.2.8` tree previously compared in V5DCM9 correspond *exactly* to the appfs files inside the available Thermia Connect RAUC 2.0.18 and 2.1.105 images.
- **Baseline:** V5DCM9 static application source comparison, in which original RAUC mapping was explicitly UNVERIFIED; deployed V5DCM2 FIX1 RX-only production.
- **Controlled change:** directly parse two original RAUC SquashFS-v4/zlib files, extract embedded manifest/appfs/rootfs images, compare SHA-256 and lengths against the embedded manifest, read internal `device_client/_version.py` in appfs ext4 files and compare every Python module byte-for-byte against earlier source ZIPs. Entire test offline: no ESPHome or UART changes.

## Exact observed provenance mapping

| Original RAUC bundle | Version from own manifest | Device_client version directly read from own appfs ext4 | Matched source files |
|---|---|---|---|
| `Thermia_Connect-2.0.18-s1.raucb` | `2.0.18` | `0.1.45` | 21/21 exact byte matches with `appfs_2018.zip` |
| `Thermia_Connect-2.1.105-s1.raucb` | `2.1.105` | `0.2.8` | 25/25 exact byte matches with `device_client.zip` |

**2.0.18** RAUC SHA256 `d4c79deef2a2903e7e58af65e4f578956ad4c6be0fb7d2e9f2fa8f8152d22573`; manifest SHA256 `37e83906447f3eca84a69ffa8142dcc9a37abfa3af9e4c2423733ac99ec8361f`; appfs SHA256 `0b5d5cd2bd739957276c336f685e8c613e6996e06eee729809d840d0c677d712`; rootfs SHA256 `25f2ac6126e1d2b9da1893410b6e65d092881d23731d811ce2c4140b0f384510`; manifest build `20240429123616`.

**2.1.105** RAUC SHA256 `1da6d55dd50dee9335c03f13df35370c3ad7c1a9ebb06a0e9c2b32b92769868c`; manifest SHA256 `46aee154db02ce46783c7fd43db7b4c1730109d5adcb22e7f8d3b5883cd378b0`; appfs SHA256 `dde141340f1d48a389fb9845ff03d09526fc32c91a829a4cbc77101dd3f18cc5`; rootfs SHA256 `d79c78213fcbf860c828d1b8f31e59d857ef4909d697e11a2e48d1210ad76c9f`; manifest build `20260109001546`.

## Results and evidence classes
- **PROVEN — exact offline provenance:** two independent RAUC images, embedded version fields, four manifest-image SHA256/length matches, `/usr/lib/python3.10/site-packages/device_client/_version.py` read from each own appfs ext4, 46/46 source module byte comparisons. Thus the version-mapping limitation in V5DCM9 has been RESOLVED.
- **PROVEN — source comparison (now RAUC-version scoped):** 21 shared Python modules, 16 changed, 4 added (cm/cm_client_type.py; data/service.py; data/storage.py; smart_energy.py), zero removed.
- **FIRMWARE-DERIVED:** later application introduces separate parameter update/readiness bookkeeping and service-driven publication/request selection. This is not XTR bus proof.
- **UNKNOWN:** XTR actual native FC23 response acceptance, sender and slot, DCM/Online indicator semantics, whether challenge cryptographic transform changed. Manifest SHA checks are NOT RAUC signature-chain validation.

## Positive, negative, abort, recovery
- **Positive:** exact manifest hash and size identity; directly read appfs versions; all 46 modules identical to earlier ZIPs — MET.
- **Negative:** mismatching image hash, version or source — NOT OBSERVED.
- **Abort:** ambiguous provenance, publishing private security or mailbox command functionality, any hardware TX — no abort required.
- **Recovery:** none: offline-only. Leave tested production V5DCM2 FIX1 at TX HARD_DENY.

## Next
**V5DCM11 — PREPARED / NOT RUN:** offline version-scoped comparison of CM930 acceptance-state lifecycle, application parameter readiness and service publication witnesses. Do not infer that the DCM icon or Internet Online status is proved. No active TX without an independent authorized plan. Local repro pack: `V5DCM10_RAUC_PROVENANCE_VERIFIED_20261017.zip`; public report excludes extracted firmware/source payloads or private emulation.
