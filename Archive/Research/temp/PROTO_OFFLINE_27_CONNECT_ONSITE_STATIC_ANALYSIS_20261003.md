# PROTO-OFFLINE-27 — Thermia Connect / OnSite static-analysis attempt

**Date:** 2026-10-03  
**Status:** **COMPLETE / INCONCLUSIVE** — artifact acquisition was narrowed further, but no APK/XAPK/firmware binary could be loaded for actual static decompilation.  
**Hypothesis:** a recoverable Thermia OnSite/Online application binary will expose local Connect AP discovery, commissioning/update endpoints, protocol-package metadata or model/profile selection logic.  
**Controlled change:** external artifact research only; no heat-pump access, no ESP TX, no YAML change, no controller restart and no setting write.

## Public artifact evidence recovered

### Thermia OnSite Android

Package:

`com.thermia.onsite`

Current Google Play metadata confirms:
- Thermia AB publisher;
- installer/professional positioning;
- update date 2026-09-25;
- access to system/performance/customer-support functionality.

Historical AppBrain metadata for Android version 1.7.9 reports:
- APK size ~40.4 MB;
- 22 permissions;
- relevant network/local-link permissions including:
  - access Wi-Fi state;
  - change Wi-Fi state;
  - change network connectivity;
  - full network access;
  - fine location;
  - camera.

These permissions are consistent with the official Connect commissioning flow over a local Wi-Fi access point, but they do not expose the local protocol itself.

### Thermia OnSite iOS

The public App Store version history currently reaches **1.8.2** in late September/early October 2026.

This shows active current development but is iOS-specific evidence; it must not be silently assigned as the Android version.

### Thermia Online Android

Package:

`se.thermia.online2`

APKPure exposes a concrete downloadable XAPK surface and historical versions.

For the indexed 2.1.1 package:
- XAPK;
- 37.3 MB;
- armeabi-v7a;
- signature fingerprint `38974b726e3664e3fe401a581f6d154ef48a56d3`;
- SHA-256 `b74adf4bc9006019ddc64fb1f1503b695f806d49ace2da3497a7ada5128d6126`.

A direct XAPK retrieval was attempted from the exposed download endpoint, but the analysis environment could not retrieve the binary payload.

## Static-analysis result

Because no application binary was actually acquired:

- no JADX/apktool analysis was performed;
- no AndroidManifest.xml was extracted locally;
- no classes.dex strings were searched;
- no native `.so` libraries were inspected;
- no Connect AP IP/hostname/port/API route was recovered;
- no firmware/update manifest or protocol-package filename/URL was recovered;
- no certificate/public-key or signature-validation code was extracted.

Therefore the core static-analysis hypothesis remains **UNTESTED**, not negative.

## Strong conclusions

1. The OnSite/Online app path remains the highest-value non-invasive modern Connect target.
2. Public Android permission metadata independently fits a local Wi-Fi commissioning role.
3. Thermia Online has a concrete third-party XAPK acquisition surface, so binary acquisition is practical outside the current restricted environment.
4. No endpoint, package filename, protocol format or firmware URL should be invented from metadata alone.

## Evidence classification

### Observed
- current OnSite Play listing updated 2026-09-25;
- OnSite historical Android package requests Wi-Fi/network-control permissions;
- iOS OnSite version history reaches 1.8.2;
- Thermia Online XAPK metadata/download surface is publicly indexed;
- direct binary retrieval failed in this environment.

### Strongly supported
- the mobile apps contain local-network/commissioning functionality consistent with official Connect documentation.

### Hypotheses
- OnSite or Online contains Connect local API routes;
- one app contains firmware/protocol-package manifest identifiers;
- serial/model identity participates in profile/package selection.

### Unknown
- local AP address and transport;
- protocol-package filenames/content;
- update endpoint/manifest/signing;
- Connect serializer implementation.

## Smallest useful next artifact

A single original Android APK/XAPK for either:
1. `com.thermia.onsite` (preferred), or
2. `se.thermia.online2`

would unblock the actual static-analysis phase without requiring any heat-pump access.

## Live status

No change:
- EXP387 COMPLETE / POSITIVE
- EXP388 RUNNING / PARTIAL
