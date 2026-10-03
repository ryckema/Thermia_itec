# Thermia iTec XTR M — DCM03 / Thermia Connect firmware archaeology

**Date:** 2026-10-03  
**Track:** PROTO-OFFLINE-15  
**Status:** COMPLETE / POSITIVE — positive for target localisation and acquisition paths; no DCM03/Connect firmware image recovered  
**Baseline:** PROTO-OFFLINE-07 firmware semantic/identity mining, plus the native Online/DCM runtime/session model already recovered from genuine captures  
**Controlled change:** stop treating the Danfoss Link CC host firmware as the primary place to find the Thermia-native serializer. Trace the downstream DCM03 / Thermia Online / Thermia Connect hardware, firmware-version and update ecosystem instead.  
**Device TX:** none  
**YAML change:** none  
**Heat-pump reboot:** none  
**Setting write:** none  
**GitHub modification:** none  
**Live experiment status:** unchanged — EXP388 remains RUNNING / PARTIAL

---

## Hypothesis

The unresolved translation:

```text
HE/DHP semantic parameter
        ↓
native Thermia protocol / session / pages
```

is implemented downstream from the Danfoss Link CC host, and the best offline route to the missing serializer is therefore firmware or protocol-package archaeology around:

```text
old DCM03 / Thermia Online
and
modern Thermia Connect
```

A positive result does **not** require recovering the binary itself. It requires materially narrowing which device contains the serializer and identifying concrete firmware/update acquisition surfaces.

---

# 1. Baseline from PROTO-OFFLINE-07

The recovered Danfoss Link CC 2.7.42 firmware can be followed through:

```text
HPNode
  ↓
DHP/HE ParameterID model
  ↓
HE Set/Get request
  ↓
HESetGetReqRsp / HE transport
  ↓
physical DCM peer
```

but no meaningful native Thermia address table for pages such as:

```text
03E8
055A
06F4
07D0
0820
0864
0870
```

was found in the managed Link CC assemblies.

The host-side model therefore ends before the native Thermia serializer.

This remains the baseline for PROTO-OFFLINE-15.

---

# 2. Old Danfoss Link architecture is model-family dependent

Official Danfoss Link HP-kit documentation exposes two materially different hardware paths.

## 2.1 DHP-H/L/A path

For DHP-H/L/A, the HP kit explicitly contains:

```text
heat pump
   ↓
Gateway card inside heat pump
   ↓
DCM03 outside heat pump
   ↓ wireless
Danfoss Link CC
```

The official kit contents list both:

```text
Gateway
DCM03
```

and the DCM03 cable connects to the Gateway.

### Consequence

For this family, the final native translation could be split between:

```text
Gateway firmware
and
DCM03 firmware
```

So the older generic statement "the serializer is in DCM03" would be too strong for all Thermia/Danfoss models.

## 2.2 DHP-AQ path

For DHP-AQ — much closer to the Atec/iTec lineage — the official kit is different.

Kit `086L2382` contains:

```text
AC/DC supply
DCM03
DHP-AQ ↔ DCM03 connection cable
DIN rail / installation hardware
```

There is **no separate Gateway card** in the kit.

The manual instructs the installer to connect the DCM03 cable directly to a free RJ45 connector on the heat-pump relay board and connect the other end to the DCM03's RS485 output.

### Strong conclusion

For the DHP-AQ/Atec lineage, DCM03 itself sits directly on the heat-pump communication path.

That materially narrows the missing HE-to-native serializer boundary:

```text
Danfoss Link CC
      ↓ HE / wireless
    DCM03
      ↓ native pump-side communication
DHP-AQ / Atec controller
```

Therefore **DCM03 firmware is now the strongest old-generation firmware target for the serializer used by the AQ/iTec lineage**.

This is stronger evidence than the earlier architectural inference from Link CC firmware alone.

### Important limitation

This does not prove that every later iTec/XTR byte serializer is identical to DHP-AQ DCM03 firmware.

It identifies the correct old-generation component to reverse-engineer.

---

# 3. Old Thermia Online independently confirms the same split

A 2013 Thermia Online installation manual gives the same family distinction.

For Atec, the Online accessory contains:

```text
DCM
heat-pump ↔ DCM cable
AC/DC power supply
```

and describes the DCM as the module connected on one side to the heat pump and on the other side to the internet.

For Diplomat/Atria-family installations, the manual instead shows:

```text
heat pump
 ↓
Gateway
 ↓
DCM
 ↓
internet
```

### Strong conclusion

Two independent official documentation branches agree:

```text
Atec / DHP-AQ:
    direct DCM ↔ heat-pump connection

older Diplomat / DHP-H/L/A:
    Gateway + DCM chain
```

This makes a direct DCM-side serializer for the AQ/Atec/iTec lineage substantially more likely than a serializer hidden inside Link CC.

---

# 4. DCM03 has an explicit application/integration state above transport

The Danfoss Link HP-kit troubleshooting section is unusually useful.

The DCM03 can be switched between:

```text
Danfoss Link integration
and
Danfoss Online
```

using the DCM button/LED indication.

For the Gateway-equipped family, the Gateway LED state machine explicitly distinguishes:

```text
startup
DCM-HP approval
approval failed
sending settings to DCM
all OK
```

### Strong conclusion

The old integration contains an explicit **approval / binding / synchronization layer** above mere electrical communication.

This independently fits our local project result that:

```text
valid slave-0x06 presence
!=
semantic Online/DCM session
```

and that transport ACK behavior by itself is not semantic recognition.

### Caution

The documented `DCM-HP approval` LED sequence belongs to the Gateway-equipped installation path. It must not be claimed as a directly observed DHP-AQ or XTR `071C/0730` state.

A possible relation to our native session-opening exchange remains a hypothesis only.

Also, the manual notes that the specific DHP-AQ HP-kit article numbers `086L2381/086L2382` are exceptions to Online 2 compatibility. Therefore the Link/Online mode-switch text must not be used to claim that this exact DHP-AQ kit supported every Online generation.

---

# 5. Thermia Connect is a second, modern serializer target

Current Thermia documentation explicitly lists:

```text
iTec XTR
```

as compatible with Thermia Connect.

The 2025 Connect installation guide also says that, if a heat pump already uses an internet connection through a DCM, that DCM must be disconnected/removed before Connect is installed.

For iTec/Atec variants the guide routes Connect communication to the heat-pump I/O/expansion communication ports.

### Strong conclusion

Thermia Connect is not merely a cloud-side replacement.

It physically replaces the old DCM-side heat-pump communication accessory and is therefore a **second concrete firmware target for the native southbound protocol**.

For this project:

```text
old target:
DCM03 firmware

modern target:
Thermia Connect firmware / protocol packages
```

The fact that current Connect officially supports iTec XTR makes the modern target directly relevant to this XTR M project.

---

# 6. The phrase "pairing and protocol packages" is a major acquisition clue

The current Connect commissioning guide states that some commissioning steps take extra time due to:

```text
pairing and protocol packages
```

It also requires the heat-pump serial number during onboarding.

The same guide documents that:

- the Connect device exposes a temporary local access point;
- the Thermia Online or Thermia OnSite mobile app connects locally during commissioning;
- a yellow blinking LED means Connect is updating software;
- Connect software can be updated via Thermia Online;
- local software update is also possible with the mobile app while the Connect access point is active.

### Strongly supported interpretation

Modern Connect has an update/onboarding architecture where firmware and/or pump-specific protocol material can be delivered after manufacture.

### Hypothesis — not yet proven

The term **protocol packages** may refer to model/family-specific southbound protocol descriptions, serializers, register maps or compatibility modules.

This would explain how one Connect hardware platform supports:

```text
iTec XTR
iTec XT
Legend
older Diplomat families
...
```

without requiring every mapping to be compiled as one immutable monolithic image.

However, no package contents, manifest, URL, signing scheme or file format have yet been recovered.

---

# 7. Modern Connect has a real firmware namespace and OTA path

Thermia's Smart Price Light documentation states that the embedded Thermia Connect software must be:

```text
2.1.00 or later
```

and explicitly says the user can update the embedded Connect firmware through Thermia Online using OTA.

### Proven external facts

- Connect has independently versioned embedded firmware.
- `2.1.00` is a real released firmware threshold.
- Thermia Online distributes Connect firmware OTA.
- first activation can request a Connect firmware update.

### Important distinction

Do **not** conflate:

```text
Connect embedded firmware 2.1.00+
```

with the older classic Online API field:

```text
dcmVersion = 2.0.17
```

They are different product/version namespaces.

---

# 8. Classic DCM version fingerprint: 2.0.17

Public debug fixtures in the independent `python-thermia-online-api` project contain real-looking Thermia Online API response structures for multiple classic installations.

The examples for:

```text
ATEC / DHP-AQ
iTec
Diplomat Duo
```

all expose:

```text
dcmVersion: 2.0.17
```

in the sampled fixtures.

The ATEC example separately exposes a heat-pump/controller program/firmware version such as:

```text
3.1.1
```

which shows that the API distinguishes:

```text
DCM firmware version
from
heat-pump program/firmware version
```

### Classification

**Independent/public API evidence, not vendor firmware proof.**

`2.0.17` is a useful exact fingerprint for archive hunting, strings searches, package-name searches and firmware dumps.

It is **not** claimed to be universal across all DCM installations.

---

# 9. Firmware/package acquisition search result

Searches were performed across:

- official Thermia/Danfoss documentation;
- public indexed web sources;
- GitHub code/repositories;
- public Thermia Online API reverse-engineering/debug fixtures;
- app-store/package metadata and third-party APK indexing.

### Negative sub-result

No actual:

```text
DCM03 firmware binary
classic DCM firmware update package
Thermia Connect embedded firmware binary
Thermia Connect OTA manifest
protocol-package file
protocol-package URL
```

was recovered from the public/indexed sources searched in this pass.

This is a **valid negative acquisition result**, not evidence that those artifacts are inaccessible in principle.

---

# 10. Mobile applications are now the best next offline acquisition surface

Two application paths are directly named by the Connect installation guide:

```text
Thermia Online
Thermia OnSite
```

The Android package identifiers located during this pass include:

```text
Thermia Online:
se.thermia.online2

Thermia OnSite:
com.thermia.onsite
```

The reason these are high-value targets is not the cloud API itself.

The commissioning guide proves that the apps can communicate with the **local Connect access point**, and software can be updated locally through that connection.

Therefore a static APK/XAPK analysis can plausibly reveal:

```text
local AP hostname / IP
local HTTP/HTTPS endpoints
commissioning paths
firmware manifest names
firmware package names
protocol-package names
download hosts
checksum/signature fields
update API routes
model/profile identifiers
```

without owning a Thermia Connect unit.

No application binary was successfully recovered into this analysis environment, so no static app analysis is claimed yet.

---

# 11. Refined architecture after PROTO-OFFLINE-15

The evidence now supports this more precise historical model.

## DHP-AQ / Atec / early iTec lineage

```text
Danfoss Link CC
  semantic HE parameter layer
        │
        │ wireless / HE
        ▼
      DCM03
  approval/binding state
  HE ↔ pump translation
  strongest candidate location
  for native serializer
        │
        │ direct pump communication
        ▼
Thermia controller
  native pages / state
```

## Older Gateway-equipped Diplomat/DHP-H/L/A lineage

```text
Link CC
  ↓
DCM03
  ↓
Gateway card
  ↓
heat-pump controller
```

Here the exact serializer responsibility can be split between DCM03 and Gateway.

## Modern iTec XTR path

```text
Thermia Online / OnSite app
          │
          │ onboarding / updates
          ▼
    Thermia Connect
     embedded firmware
     "protocol packages"
          │
          │ pump communication
          ▼
       iTec XTR
```

The final box-level allocation of individual state-machine functions remains open, but the firmware targets are now concrete.

---

# 12. Relation to our native `071C/0730` session opening

The project already has a native session-opening layer around:

```text
071C / 0730
```

and demonstrated that simple syntactic transport presence is insufficient for semantic integration.

Official DCM documentation now independently shows an application lifecycle containing:

```text
approval
approval failed
sending settings
ready
```

### Hypothesis

`071C/0730` may be part of the native controller-side approval/binding/session mechanism corresponding to that higher-level lifecycle.

### Why this is not promoted

There is no official byte-level mapping from those LED states to:

```text
071C
0730
AFC8..AFD3
```

and no DCM03 firmware was recovered.

Therefore this remains a useful structural hypothesis only.

---

# 13. Highest-value next offline target

The most efficient next firmware-archaeology step is no longer another broad web search.

It is:

```text
obtain Thermia OnSite APK/XAPK
then
obtain Thermia Online APK/XAPK
```

and perform static analysis focused specifically on:

```text
Connect local AP
firmware update
protocol package
manifest
model/profile
checksum/signature
download endpoint
```

Thermia OnSite is the first choice because it is the installer/commissioning application explicitly shown configuring Thermia Connect.

If either app contains local-update strings or manifests, it may lead directly to the Connect firmware or protocol packages.

Second priority is archive hunting around:

```text
DCM03
dcmVersion 2.0.17
DHP-AQ 086L2382
Atec Online DCM
```

for historical binary/update artifacts.

---

# 14. Evidence classification

## Observed facts / official documentation

- DHP-H/L/A Link HP-kit contains both Gateway and DCM03.
- DHP-AQ Link HP-kit contains DCM03 and a direct DHP-AQ↔DCM03 cable, with no separate Gateway card in that kit.
- DHP-AQ DCM03 connects directly to a free RJ45 on the heat-pump relay board and to the DCM03 RS485 port.
- DCM03 can be switched between Danfoss Link integration and Danfoss Online mode in the documented environment.
- the Gateway-equipped path has explicit startup / DCM-HP approval / approval-failed / settings-transfer / ready states.
- old Thermia Online Atec documentation independently uses direct DCM↔heat-pump connection.
- older Diplomat/Atria Online installations use Gateway + DCM.
- current Thermia Connect replaces an existing DCM connection when installed.
- Thermia Connect commissioning uses Thermia Online or Thermia OnSite.
- Connect has a temporary local access point.
- Connect software can be updated remotely and locally through the app.
- commissioning documentation explicitly mentions "pairing and protocol packages".
- Thermia Connect embedded firmware version 2.1.00+ is a real OTA requirement for Smart Price Light.
- Thermia Connect officially supports iTec XTR.

## Independent/public API evidence

- sampled ATEC/DHP-AQ, iTec and Diplomat fixtures expose `dcmVersion=2.0.17`.
- classic Online API distinguishes `dcmVersion` from the heat-pump's own firmware/program version.

## Strong conclusions

1. Link CC is an upstream semantic client; the missing native serializer is downstream.
2. For the DHP-AQ/Atec/iTec lineage, DCM03 is the strongest old-generation target for the native serializer because it connects directly to the heat pump.
3. The serializer-location conclusion must not be generalized unchanged to Gateway-equipped older families.
4. Thermia Connect is a directly relevant modern firmware target for XTR because it replaces DCM-side pump communication and officially supports iTec XTR.
5. Connect's local/OTA update path creates a realistic non-invasive route to firmware/package recovery.
6. `dcmVersion=2.0.17` and Connect firmware `2.1.00+` are useful but separate firmware fingerprints.

## Hypotheses

- Connect "protocol packages" contain model-specific pump-side protocol/serializer definitions or modules.
- some of the native `071C/0730` lifecycle corresponds to DCM/controller approval or binding.
- a DCM03 2.0.17 binary would likely contain or lead directly to the AQ/iTec native serializer.
- app static analysis may reveal local firmware/protocol package manifests and download endpoints.

## Unknowns

- DCM03 firmware package name, binary format and update mechanism.
- Connect firmware package URL, manifest and signing scheme.
- Connect protocol-package format and content.
- local Connect AP address/API routes.
- whether protocol packages are code, data tables, compatibility metadata, or a mixture.
- exact placement of session logic between controller and DCM03/Connect.
- exact native bridge for HE ParameterIDs.
- exact responsibility split on Gateway-equipped families.

---

# 15. Sources used

## Official / vendor documentation

1. Danfoss Link HP-kit installation manual, VIIFR101 / 2014  
   https://assets.danfoss.com/documents/latest/32195/AN118686466213da-000101.pdf

2. Thermia Online installation manual, VIBQF249 / 2013  
   https://www.thermia.pl/storage/Attachment_File/1-2000/195-file-x020104-th-online-install-vibqf249-pl.pdf

3. Thermia Connect installation guide, ACCTC01IG0220 / Thermia AB ©2025  
   https://lp-varaosaksi.fi/WebRoot/vilkasfi02/Shops/2017032107/668D/EB67/C452/65FF/144E/7F00/0001/E6F8/installation_manual_doc-00119653.pdf

4. Thermia Smart Price Light guide / FAQ  
   https://classiconlinestorage.blob.core.windows.net/web-resources/SmartPrice_Info_and_FAQ_SE_Light.pdf

5. Thermia Online / Thermia Connect product page  
   https://thermia.com/products/thermia-online/thermia-online/

## Independent/public code evidence

6. `python-thermia-online-api`, ATEC/DHP-AQ debug fixture  
   https://github.com/klejejs/python-thermia-online-api/blob/bcf2092f5764de6ea8bd03b42b37a78478a40420/ThermiaOnlineAPI/tests/debug_files/ATEC_DHP_AQ.txt

The independent source is used only for public API/version evidence, not as proof of native protocol behavior.

---

# Result

**PROTO-OFFLINE-15 — COMPLETE / POSITIVE**

The firmware archaeology did **not** recover a DCM03 or Thermia Connect firmware binary.

It did, however, materially narrow the target:

```text
old AQ/Atec/iTec path:
DCM03 is the strongest missing-serializer firmware target

modern XTR path:
Thermia Connect firmware / protocol packages are the strongest target
```

and it identified a concrete next offline acquisition route through the installer/mobile applications and the Connect local-update mechanism.

No live heat-pump action or GitHub modification was performed.