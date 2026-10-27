# PROTO-OFFLINE-21 — canonical update pending

**Date:** 2026-10-03  
**Reason pending:** GitHub write permission was not granted in the current request.

## THERMIA_PROJECT_STATE.md — proposed addition

- **PROTO-OFFLINE-21 — COMPLETE / POSITIVE** — targeted Connect/OnSite artifact hunt narrowed the practical acquisition path but did not recover a firmware/APK binary.
- Official Connect commissioning ties together local AP communication, heat-pump serial identity, and explicit "pairing and protocol packages".
- Local Connect software update is supported through the mobile app while the AP is active.
- Highest-value next artifact is Thermia OnSite Android package `com.thermia.onsite`; Thermia Online Android package remains `se.thermia.online2`.
- Exact Connect hardware identifiers recovered from official declaration: kit `206495`, gateway `355202`, PSU `357577`.
- No Connect firmware binary, OTA manifest, protocol-package file/URL, local IP/hostname/API route or DCM03 firmware was recovered.
- Do not invent Connect endpoint/address/package details.
- EXP387 remains COMPLETE / POSITIVE.
- EXP388 remains RUNNING / PARTIAL.

## EXPERIMENT_LOG.md — proposed entry

`PROTO-OFFLINE-21 | Connect/OnSite artifact acquisition hunt | COMPLETE / POSITIVE. Official Connect docs establish a supported local AP commissioning/update path using Thermia Online/OnSite, require the final 8 heat-pump serial digits during onboarding and explicitly mention pairing/protocol packages. Exact hardware IDs 206495/355202/357577 provide a new acquisition fingerprint. Targeted GitHub/web searches found no firmware/protocol package or public OnSite source; APK binaries were not recovered into the analysis environment. Next acquisition target is com.thermia.onsite APK/XAPK, followed by se.thermia.online2.`

## PROTOCOL_FINDINGS.md — proposed durable additions

**PROVEN / official documentation**
- Thermia Connect commissioning uses Thermia Online or Thermia OnSite over a supported local AP.
- local Connect software update is supported through the mobile app while the AP is active.
- onboarding requires the final eight heat-pump serial digits.
- commissioning documentation explicitly references "pairing and protocol packages".
- exact hardware IDs: Thermia Connect 206495, Gateway 355202, PSU 357577.

**STRONGLY SUPPORTED**
- mobile APK static analysis is the most concrete remaining non-invasive acquisition path to Connect update/protocol-package metadata.

**HYPOTHESIS**
- heat-pump identity participates in protocol-package/profile selection.
- protocol packages contain model-specific southbound protocol/serializer material or compatibility tables.

**OPEN**
- local AP IP/hostname/API.
- package format, URL, signing/checksum.
- Connect firmware image.
- exact serial-to-package relationship.
- DCM03 firmware internals.

## Research/temp

Recommended new files when GitHub write is authorized:
- `Research/temp/PROTO_OFFLINE_21_CONNECT_APP_ARTIFACT_HUNT_20261003.md`
- `Research/temp/PROTO_OFFLINE_21_ARTIFACT_ACQUISITION_MATRIX_20261003.csv`
- this pending reconciliation note.