# Thermia iTec XTR M — Thermia Connect / OnSite artifact acquisition hunt

**Date:** 2026-10-03  
**Track:** PROTO-OFFLINE-21  
**Status:** **COMPLETE / POSITIVE** — acquisition surfaces and identity chain materially narrowed; no Connect/DCM firmware or APK binary was recovered into the analysis environment  
**Baseline:** PROTO-OFFLINE-15 DCM03/Connect firmware archaeology + PROTO-OFFLINE-17..20 current offline pass  
**Controlled change:** external/offline artifact acquisition only. No heat-pump access, no ESP TX, no YAML change, no controller restart, no setting write.  
**Live XTR experiment status:** unchanged — EXP387 remains COMPLETE / POSITIVE; EXP388 remains RUNNING / PARTIAL.  
**GitHub modification:** none.

---

## Hypothesis

The most efficient remaining offline path to Thermia's native Connect/DCM serializer is no longer broad protocol guessing.

Instead, use official Connect onboarding/update documentation and the mobile-app package identities to locate:

```text
mobile app
   ↓
local Thermia Connect AP
   ↓
onboarding / heat-pump identity
   ↓
"pairing and protocol packages"
   ↓
local or OTA update logic
   ↓
Connect embedded firmware / profile package
   ↓
southbound Thermia native serializer
```

A positive result does not require recovering the binary itself. It requires narrowing concrete acquisition artifacts, identifiers and code paths enough that a future APK/firmware acquisition can be searched surgically.

**Result: positive.**

---

# 1. Official Connect commissioning flow is now a concrete artifact map

The 2025 Thermia Connect installation guide states that commissioning can be performed with:

```text
Thermia Online app
or
Thermia OnSite app
```

The gateway:

- boots through a white-flashing phase;
- exposes a blue-flashing local access-point state for commissioning;
- can enter a yellow-flashing software-update state;
- requires the heat pump's serial number during onboarding;
- specifically tells the installer to use the last **8 digits** of that serial;
- warns that some onboarding stages take longer because of **"pairing and protocol packages"**.

The same guide says local software update is possible from the mobile app, but only while the Thermia Connect access point is active.

The access point remains available for about 60 minutes after power-up and can be reactivated by a power cycle or short reset.

### Strong conclusion

The mobile application is not merely a cloud UI.

It contains, directly or through bundled/native libraries, enough logic to participate in:

```text
local Connect discovery/join
commissioning
heat-pump identity provisioning
local software-update initiation
```

That makes OnSite/Online APK analysis a substantially better acquisition target than another generic search for "Thermia firmware".

---

# 2. Heat-pump serial number is an important onboarding input

The current guide explicitly requires the heat-pump serial number and specifically the final 8 digits.

That instruction occurs immediately in the same commissioning section that warns about:

```text
pairing and protocol packages
```

### Observed fact

The serial number is an explicit input to the Connect onboarding process.

### Strongly supported interpretation

Connect onboarding uses heat-pump identity as part of selecting, validating or registering the connected pump.

### Hypothesis only

The final 8 digits may be an input to:

- model/profile lookup;
- protocol-package selection;
- pairing/binding;
- backend registration;
- some combination of the above.

There is **no evidence** yet that the serial digits are a cryptographic secret, challenge-response key or direct native-bus payload.

Do not use them that way without app/firmware evidence.

---

# 3. Exact Android application targets

## Thermia OnSite

Official Google Play package:

```text
com.thermia.onsite
```

Publisher:

```text
Thermia AB
```

The current public Play listing describes it as a support tool for Thermia installers.

This is the highest-value app target because the official Connect guide explicitly uses OnSite for commissioning.

## Thermia Online

Package identified in the existing research:

```text
se.thermia.online2
```

Third-party APK indexing exposes historical/current package metadata and version entries, but the binary could not be downloaded into the current analysis environment.

### Acquisition result

```text
OnSite APK/XAPK:  NOT RECOVERED
Online APK/XAPK:  NOT RECOVERED
```

Therefore no Java/Kotlin/native-library decompilation is claimed by PROTO-OFFLINE-21.

---

# 4. APK static-analysis target list is now very specific

Once an APK/XAPK is available, the first pass should search resources, strings, bytecode and native `.so` libraries for:

```text
Thermia Connect
Connect
protocol package
protocolPackage
package manifest
profile
heat pump type
serial
commission
onboard
pair
pairing
firmware
software update
OTA
checksum
signature
certificate
download
manifest
access point
SSID
WiFi
gateway
local
HTTP
HTTPS
WebSocket
MQTT
port
```

Then search for:

```text
private IPv4 literals
hostnames
URL paths
JSON field names
protobuf/gRPC schemas
certificate/public-key blobs
firmware filename suffixes
ZIP/TAR/package magic handling
hash algorithms
signature validation
model/profile tables
```

Do **not** begin by searching only for the known native register addresses such as `03E8` or `071C`.

If "protocol packages" are data-driven, the app may never contain those native addresses directly.

---

# 5. Connect hardware identifiers recovered from official declaration

The official Thermia EU Declaration of Conformity gives exact identifiers:

```text
Thermia Connect kit:        art.no. 206495
Gateway:                    art.no. 355202
Internal power supply:      art.no. 357577
```

### Why this matters

These are better archive/OEM/service-search fingerprints than the generic product name "Thermia Connect".

Future artifact searches should include exact combinations such as:

```text
355202 firmware
355202 update
206495 software
206495 service
355202 bin
355202 fw
355202 image
355202 bootloader
```

No firmware hit was recovered in this pass.

---

# 6. Radio declaration gives an additional hardware fingerprint

The Connect declaration includes standards for:

```text
2.4 GHz Wi-Fi:
EN 300 328

and radio standards covering cellular families:
EN 301 908-1
EN 301 908-13
EN 301 511
```

### Observed fact

Those standards are explicitly included in the official declaration for the Connect product.

### Careful interpretation

This is a **hardware/regulatory fingerprint** that may help identify the underlying gateway/OEM platform.

It is not enough to assert that every Thermia Connect installation actively uses a built-in LTE/GSM connection. Thermia's normal product documentation emphasizes Ethernet/Wi-Fi.

The useful research action is to search regulatory/OEM records using the part number plus these radio capabilities.

---

# 7. Physical/local interface facts

Official Connect documentation identifies gateway interfaces including:

```text
USB
power
pump communication port
second connected-but-unused communication port
Ethernet
reset
```

For iTec/Atec the communication cable goes between the pump-side I/O/expansion communication connection and the Connect gateway.

The current product documentation states:

```text
Wi-Fi: IEEE 802.11 b/g/n
band: 2.4 GHz
AP security: WPA-PSK
```

### Strong conclusion

The local AP is a real supported service/commissioning interface, not an undocumented debugging mode.

That makes its API/update behavior a legitimate and likely stable application code path to recover from OnSite/Online.

---

# 8. DCM replacement remains strong architectural evidence

The Connect installation guide explicitly says that when the heat pump already has an internet connection using a DCM, the DCM is to be disconnected/removed before installing Connect.

Combined with the iTec/Atec communication wiring this reinforces PROTO-OFFLINE-15:

```text
classic:
heat pump <-> DCM / Online

modern:
heat pump <-> Thermia Connect
```

For the XTR project, the Connect gateway is therefore not just a generic network bridge; it occupies the hardware position of the native integration accessory.

The exact placement of serializer logic between:

```text
Connect firmware
protocol package
controller firmware
```

remains open.

---

# 9. Public code-search result

Targeted public GitHub searches were performed for:

```text
com.thermia.onsite
se.thermia.online2
"protocol package" Thermia
"protocol packages" Thermia
Thermia Connect firmware
Thermia Connect API
Thermia Connect + private-IP clues
```

Result:

- no public OnSite source/decompilation hit;
- no useful public Thermia Connect firmware repository;
- no protocol-package file or manifest hit;
- `se.thermia.online2` appears only incidentally in an unrelated package-name dataset;
- public Thermia Online reverse-engineering projects continue to expose cloud-side APIs, not the local Connect AP protocol.

### Negative conclusion

GitHub code search is currently a poor direct acquisition route for the missing Connect-local implementation.

The binary/app path remains higher-value.

---

# 10. APK acquisition attempt

A third-party APK index exposes Thermia Online package/version metadata and a download surface.

The environment used for this research could resolve the metadata/index page but could not retrieve the actual APK/XAPK payload for local decompilation.

This failure is recorded as:

```text
artifact acquisition failure
not
absence of the artifact
```

No APK contents, classes, strings, endpoints or certificates are claimed.

---

# 11. Refined acquisition priority

## Priority A — OnSite APK/XAPK

Reason:

- installer-focused;
- directly named by official Connect commissioning instructions;
- likely contains the most explicit local Connect workflow.

Once obtained:

```text
unpack APK/XAPK
inventory assets/resources
jadx/apktool static pass
extract native libs
strings on .so files
URL/IP/hostname extraction
certificate/public-key extraction
protocol/update vocabulary search
model/profile/serial flow tracing
```

## Priority B — Thermia Online APK/XAPK

Reason:

- also supports Connect commissioning;
- may contain both local AP and cloud/update orchestration;
- older versions may expose less-obfuscated code or legacy update paths.

Compare several versions rather than only the latest.

## Priority C — exact Connect hardware identifiers

Search using:

```text
206495
355202
357577
```

alongside firmware/update/OEM/regulatory terms.

## Priority D — classic DCM03

Continue exact fingerprint hunting around:

```text
DCM03
2.0.17
DHP-AQ
Atec
086L2381 / 086L2382
```

This remains valuable for the old-generation serializer but is less directly XTR-specific than Connect.

---

# 12. What PROTO-OFFLINE-21 did NOT find

No:

```text
Thermia Connect firmware .bin/.img
Connect OTA manifest
protocol-package archive
protocol-package filename
protocol-package URL
Connect local IPv4 address
Connect local hostname
local HTTP/HTTPS API route
local service port
OnSite APK/XAPK binary
Online APK/XAPK binary loaded into analysis
DCM03 2.0.17 firmware image
```

was recovered.

Those remain OPEN.

---

# 13. Observed facts

- official Connect commissioning uses Thermia Online or Thermia OnSite;
- official documentation explicitly mentions "pairing and protocol packages";
- the final eight heat-pump serial digits are required during onboarding;
- Thermia Connect exposes a supported local access point for app connection;
- local software update requires that AP to be active;
- the AP is available for a bounded post-power-on interval and can be reactivated;
- Connect physically uses a pump communication port and replaces a pre-existing DCM installation path;
- official hardware identifiers are 206495 / 355202 / 357577;
- official declaration includes Wi-Fi and cellular-family radio standards;
- OnSite Android package is `com.thermia.onsite`;
- no firmware/package/APK binary was recovered in this pass.

---

# 14. Strong conclusions

1. **APK static analysis is now the highest-value practical offline acquisition step.**
2. The installer-focused **Thermia OnSite** app should be acquired before spending more time on generic web searches.
3. The Connect onboarding path joins three concepts that matter to this project: local AP communication, heat-pump identity, and protocol-package handling.
4. Exact Connect hardware identifiers provide a new firmware/OEM/archive search axis.
5. The Connect local AP/update path is officially supported and therefore a stronger target than speculative hidden-service probing.
6. No evidence currently justifies inventing Connect local IPs, endpoints, package names or firmware URLs.

---

# 15. Hypotheses

- heat-pump serial/model identity is used to select or validate a protocol package;
- "protocol packages" contain model/profile-specific southbound protocol logic, register/profile data or compatibility metadata;
- package selection or initialization participates in the startup/readiness behavior seen at the native bus level;
- OnSite contains the least-obfuscated/local-most-direct implementation of commissioning and update logic;
- exact Gateway art.no. 355202 may identify an OEM hardware platform in regulatory/service records.

These remain hypotheses until binary/app/manifest evidence is recovered.

---

# 16. Unknowns

- OnSite local Connect API;
- Connect AP SSID/password derivation;
- gateway local IP/hostname;
- protocol transport used between app and gateway;
- firmware-update endpoint and manifest;
- package signing/checksum scheme;
- protocol-package format/content;
- relationship between serial number and protocol-package selection;
- exact gateway chipset/OEM;
- exact location of `071C/0730` response logic;
- whether the ~120 s Eco5 service-readiness behavior has an equivalent in Connect;
- DCM03 2.0.17 firmware internals.

---

# Result

**PROTO-OFFLINE-21 — COMPLETE / POSITIVE**

The artifact hunt did not recover the desired binaries, but it significantly narrowed the acquisition problem from:

```text
"find Thermia firmware somewhere"
```

to:

```text
1. obtain com.thermia.onsite APK/XAPK
2. trace local Connect AP commissioning/update code
3. extract protocol-package / update manifest identifiers
4. use exact hardware art.no. 355202 / kit 206495 as second acquisition axis
5. keep DCM03 2.0.17 as historical serializer target
```

No live heat-pump experiment was advanced and no GitHub file was modified.

---

# Sources / provenance

## Official/vendor
- Thermia Connect installation guide ACCTC01IG0220, Thermia AB ©2025.
- Thermia Connect EU Declaration of Conformity, product 206495 / gateway 355202.
- Thermia Connect product documentation.
- Google Play listing for Thermia OnSite, publisher Thermia AB.

## Third-party/index evidence
- APK indexing for `se.thermia.online2`; used only as an artifact-acquisition lead.
- Public GitHub code search; negative acquisition result.

## Existing project research
- PROTO-OFFLINE-15 DCM03 / Thermia Connect firmware archaeology.
- PROTO-OFFLINE-17..20 current offline reduction pass.