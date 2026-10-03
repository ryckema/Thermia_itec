# Pending canonical reconciliation — PROTO-OFFLINE-15

**Date:** 2026-10-03  
**Status:** PROTO-OFFLINE-15 — COMPLETE / POSITIVE  
**Meaning of positive:** firmware target localisation and acquisition path were materially improved; no actual DCM03/Connect firmware binary was recovered.  
**GitHub:** not modified  
**Live experiment:** EXP388 remains RUNNING / PARTIAL

## THERMIA_PROJECT_STATE.md — proposed additions

- Add `PROTO-OFFLINE-15 — COMPLETE / POSITIVE — DCM03 / Thermia Connect firmware archaeology`.
- PROVEN official architecture:
  - DHP-H/L/A Link path uses `heat pump -> Gateway -> DCM03 -> Link CC`.
  - DHP-AQ Link path uses a direct DHP-AQ↔DCM03 cable; no separate Gateway card in kit 086L2382.
  - DHP-AQ DCM03 connects to the heat-pump relay-board RJ45 and DCM03 RS485 port.
  - old Thermia Online Atec documentation independently confirms a direct DCM↔heat-pump path.
  - older Diplomat/Atria Online path uses Gateway + DCM.
- Strong conclusion:
  for AQ/Atec/iTec lineage, DCM03 is now the strongest old-generation target for the missing HE↔native Thermia serializer.
- DCM03 official lifecycle evidence includes an approval/synchronization layer above transport (`DCM-HP approval`, failure, send settings, ready) on the Gateway-equipped path.
- Do not claim those LED states directly map to local XTR `071C/0730`; that is a hypothesis only.
- Current Thermia Connect:
  - officially supports iTec XTR;
  - replaces/displaces an old DCM connection on installation;
  - communicates with pump I/O/expansion communication ports;
  - has a local AP for Online/OnSite commissioning;
  - supports remote and local software update;
  - commissioning guide explicitly mentions `pairing and protocol packages`.
- Thermia Connect embedded firmware `2.1.00+` is an official Smart Price Light requirement and can be OTA updated.
- Public independent classic Online API fixtures expose `dcmVersion=2.0.17` on sampled ATEC/DHP-AQ, iTec and Diplomat installations. Keep separate from heat-pump program version and from Connect `2.1.00+`.
- No DCM03/Connect firmware image, manifest, package URL or protocol package was recovered from indexed public sources.
- Highest-value next offline acquisition target: static analysis of Thermia OnSite APK (`com.thermia.onsite`), then Thermia Online APK (`se.thermia.online2`), focused on Connect local-AP and update/protocol-package paths.

## EXPERIMENT_LOG.md — proposed entry

### PROTO-OFFLINE-15 — COMPLETE / POSITIVE — DCM03 / Connect firmware archaeology

**Hypothesis:** the missing HE→native serializer can be localized by tracing DCM03/Connect hardware and firmware/update paths rather than continuing Link CC host mining.

**Controlled change:** offline external research only; no TX/YAML/reboot/write.

**Observed:**
- official DHP-AQ kit has DCM03 directly attached to heat-pump communication; no separate Gateway in this family.
- older Gateway-equipped families use a Gateway + DCM chain.
- official DCM troubleshooting exposes an application-level approval/settings-transfer lifecycle.
- current Connect replaces DCM pump communication, supports XTR, local commissioning, local/OTA software update, and documentation mentions `protocol packages`.
- Connect firmware `2.1.00+` is a real OTA firmware threshold.
- independent public API fixtures expose classic DCM version `2.0.17` across several sampled families.
- no actual DCM03/Connect firmware package recovered.

**Result:** COMPLETE / POSITIVE for target localisation; firmware acquisition itself remains OPEN.

No live experiment status changed.

## PROTOCOL_FINDINGS.md — proposed durable updates

### PROVEN / official architecture

For DHP-AQ:
```text
Link CC
  -> DCM03
  -> direct DHP-AQ heat-pump communication
```

For older DHP-H/L/A:
```text
Link CC
  -> DCM03
  -> Gateway
  -> heat pump
```

For old Thermia Online:
- Atec uses direct DCM↔heat-pump connection.
- older Diplomat/Atria-family path uses Gateway + DCM.

### STRONGLY SUPPORTED

- DCM03 is the most likely old-generation home of the missing AQ/Atec/iTec native serializer/state machine.
- Thermia Connect is a modern XTR-relevant southbound-protocol target and likely contains or loads pump-family protocol logic.

### HYPOTHESIS

- Connect `protocol packages` contain model-specific native protocol mappings/serializer modules.
- native XTR `071C/0730` participates in a controller/DCM approval/binding lifecycle analogous in role to the documented older DCM-HP approval stage.

### OPEN / UNKNOWN

- DCM03 firmware binary/package.
- Connect firmware manifest/package URL and signing.
- protocol-package contents/format.
- Connect local AP endpoint/API.
- native HE ParameterID↔0x0F serializer mapping.
- exact Gateway/DCM responsibility split on older Gateway-equipped models.

### Negative acquisition result

No public/indexed DCM03 or Connect firmware binary or protocol-package artifact was recovered during PROTO-OFFLINE-15.

### Safety

No new live write target follows from this analysis. Do not synthesize identity, approval or firmware-update payloads on the Thermia bus without an independently recovered native mapping.