# PROTO-OFFLINE-52 — Thermia Connect / DCM03 artifact hunt, second pass

**Date:** 2026-10-04  
**Status:** **COMPLETE / INCONCLUSIVE FOR BINARY RECOVERY; POSITIVE FOR TARGET REFINEMENT**  
**Scope:** external/offline artifact acquisition only. No heat-pump access, no ESP TX, no YAML change, no controller restart and no setting write.

## Hypothesis

A second artifact-acquisition pass using the current 2026 Thermia app ecosystem may recover, or materially improve the acquisition path toward, an Android application binary, Connect firmware/protocol package, or DCM03 firmware that exposes the missing native southbound serializer.

## Controlled change

Baseline:

- PROTO-OFFLINE-15 — DCM03/Connect firmware archaeology;
- PROTO-OFFLINE-21 — Connect/OnSite artifact acquisition;
- PROTO-OFFLINE-27 — static-analysis attempt, blocked because no APK/XAPK was recovered;
- PROTO-OFFLINE-33 — exact Connect hardware fingerprint.

New variable:

- re-run current app/package identity searches after the September 2026 Thermia digital-service transition;
- retry the known Android XAPK acquisition surface;
- repeat public code/firmware searches with exact package and hardware identifiers.

No local protocol behavior is changed.

## 1. Important current ecosystem change: Thermia Online -> MyThermia

Thermia's current official digital-services page states that **MyThermia launched on 18 September 2026 and replaces Thermia Online**.

The transition preserves existing accounts, access, settings and data.

Most importantly for this research, the Android application on Google Play still uses the **same package identity**:

`se.thermia.online2`

The Play listing now presents it as **MyThermia** and was updated on 23 September 2026.

### Consequence

Future app/binary searches must use **both product names**:

- MyThermia
- Thermia Online

while retaining the stable Android package key:

`se.thermia.online2`

This is a material acquisition improvement because searching only for the old product name can now miss current artifacts.

## 2. Thermia OnSite remains the installer-side target

The official Play listing for:

`com.thermia.onsite`

is still active and was updated on 25 September 2026.

It remains explicitly installer/service oriented.

That preserves the previous acquisition priority:

1. OnSite for local commissioning/service logic;
2. MyThermia / former Online for user-side Connect, remote-control and update logic.

## 3. Connect remains directly relevant to iTec XTR

Thermia's current Connect product page explicitly includes **iTec XTR** among compatible heat pumps.

This keeps the modern research chain directly relevant:

`MyThermia / OnSite -> Thermia Connect -> iTec XTR native bus`

rather than treating Connect as generic unrelated gateway hardware.

## 4. Historical XAPK acquisition surface was retried

The previously identified direct APKPure/XAPK endpoint for:

`se.thermia.online2`

was retried:

`https://d.apkpure.net/b/XAPK/se.thermia.online2?version=latest`

The binary download **failed again in the current analysis environment**.

Therefore:

- no APK/XAPK bytes were acquired;
- no `AndroidManifest.xml` extraction was performed;
- no JADX/apktool decompilation was performed;
- no assets/native `.so` libraries were inspected;
- no local Connect API endpoint, firmware manifest, protocol-package filename or signing key was recovered.

This is an **artifact acquisition failure**, not evidence that the artifact does not exist.

The historical `2.1.1` XAPK fingerprint from the earlier pass remains useful:

- package: `se.thermia.online2`
- XAPK
- ~37.3 MB
- armeabi-v7a
- SHA-256 `b74adf4bc9006019ddc64fb1f1503b695f806d49ace2da3497a7ada5128d6126`

## 5. Public source / firmware search repeated

Current public GitHub searches were repeated for:

- `com.thermia.onsite`
- `se.thermia.online2`
- `Thermia Connect firmware`
- `"protocol packages" Thermia`
- `355202 Thermia`
- `DCM03 2.0.17`

Result:

- no OnSite source/decompile hit;
- no useful MyThermia/Thermia Online source/decompile;
- no Connect firmware repository;
- no protocol-package manifest/archive;
- no useful exact `355202` firmware hit;
- no DCM03 2.0.17 binary/source hit.

The only package-name hit for `se.thermia.online2` is incidental third-party dataset material and provides no application code.

## 6. Current official service/update evidence

The current MyThermia app advertises system notifications and available updates.

Thermia's current service pages also describe access to software-update information/application on supported systems.

This continues to support an update-delivery ecosystem, but it does **not** reveal:

- whether the mobile APK contains Connect firmware;
- whether protocol packages are bundled or downloaded;
- the package URL;
- the package signing/checksum mechanism;
- the southbound serializer location.

## Observed facts

- MyThermia replaced Thermia Online in September 2026.
- The Android identity remains `se.thermia.online2`.
- Current Google Play lists MyThermia as updated 23 September 2026.
- `com.thermia.onsite` remains current and installer/service oriented, updated 25 September 2026.
- Connect remains officially compatible with iTec XTR.
- The known direct XAPK acquisition endpoint could not be downloaded in this environment.
- Repeated public GitHub searches recovered no useful app decompilation, Connect firmware, protocol package or DCM03 2.0.17 binary.

## Strong conclusions

1. **The current Android acquisition target has changed name, not package identity.**
   `se.thermia.online2` must now be searched as both Thermia Online and MyThermia.
2. OnSite remains the most likely installer/local-commissioning artifact.
3. The app-binary route remains the highest-value external offline route to Connect-local endpoints and package/update handling.
4. Generic public GitHub/OEM searching continues to have very low yield.
5. No static-code claim can be made until actual APK/XAPK bytes are obtained.

## Hypotheses retained

- OnSite contains direct Connect commissioning/local-AP calls or invokes a reusable library that does.
- MyThermia contains current update/backend orchestration and possibly Connect onboarding compatibility code.
- one of those applications references firmware/protocol-package metadata rather than embedding native bus tables directly.
- older pre-MyThermia versions may be easier to analyze or preserve older Connect code paths.

## Unknowns

- local Connect IP/hostname/port;
- local API/protocol;
- firmware manifest/download endpoint;
- protocol-package format and URL;
- signing/checksum mechanism;
- model/serial-to-protocol-package selection;
- Connect SoC/OEM;
- exact DCM03 challenge-response implementation/key material.

## Best next artifact

The smallest artifact that would materially change this track remains one original Android package:

1. current `com.thermia.onsite` APK/XAPK;
2. current `se.thermia.online2` / MyThermia APK/XAPK;
3. historical `se.thermia.online2` 2.1.1 XAPK as a comparison target.

Once one is available, the next step is true static analysis rather than another broad artifact search.

## Result

**COMPLETE / INCONCLUSIVE FOR BINARY RECOVERY; POSITIVE FOR TARGET REFINEMENT.**

The binary/static-analysis hypothesis remains untested because no application or firmware bytes were recovered. The important new durable acquisition fact is that the current service is **MyThermia while retaining Android package `se.thermia.online2`**, so future archive/package searches must include both names.

## Live state

Unchanged:

- EXP387 — COMPLETE / POSITIVE
- EXP388 — RUNNING / PARTIAL
- EXP383 — PREPARED / NOT RUN