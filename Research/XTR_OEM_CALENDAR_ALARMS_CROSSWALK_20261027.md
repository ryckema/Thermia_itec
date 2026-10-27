# XTR 2.4.2 OEM Calendar and Alarm Read-only Crosswalk — 2026-10-27

**Nature:** consolidated OEM-source research decision; NO firmware, flash, or physical TX. Main sources: private `ryckema/Thermia_Connect_Firmware` — `findings/CM930_UNIFIED_SEMANTIC_REGISTER_DATABASE.md`, `findings/CONNECT_2.0.18_VS_2.1.105_SEMANTIC_DIFF.md`, `parameters/READ_PROD_01C_BATCH_C.md`, `findings/CM930_PRODUCT_PROFILE_DIFFERENCES.md`, `findings/XTR_OFFLINE_FIRMWARE_RESEARCH_R39_R48_20261006.md`. Profile: CM930 2.3.0–2.4.3 (local XTR 2.4.2). These are OEM-firmware derivations, NOT full local live semantic validation.

## Calendar (read-only)
- `05BA` = hot-water **programmed** 8-slot bitmap. Independently correlated locally: EXP404 bit0 controls F1 slot0 validity. This is NOT the active bitmap.
- `05BB` = hot-water **currently active** 8-slot bitmap; firmware-defined.
- `061D` = EVU/block active 8-slot bitmap; firmware-defined.
- `067F` = silent calendar active 8-slot bitmap; firmware-defined.
- `06E1` = temperature-reduction active 8-slot bitmap; firmware-defined.
- Each bit 0..7 maps calendar slots 1..8. Show raw mask AND per-slot status; do not replace with a one-boolean interpretation.
- Calendar schedule records reside in additional native calendar groups, not the four C5DM H/D/C/M pages. Local XTR source-verified slot `055B` = F1 HW start minute and `055A` calendar schedule mode/group; use calendar record evidence/profile-specific mappings to decode start/stop day/month/hour/minute with freshness. Only create true Home Assistant calendar events if whole record and time interpretation are valid; unavailable otherwise.
- OEM firmware semantic map and current local XTR verification establish some fields, not every schedule record's live completeness. No new TX or writes.

## Current alarms (read-only)
- `085F/count5` = native CURRENT alarm/service page, `085F..0863`. Decode correct bit references from recovered profile-specific `alarms.json`, guard against profile collisions; report raw 16-bit words and known active alarm names. Firmware-derived names do NOT become locally proven until compared with a naturally observed real XTR alarm/panel.
- READ-PROD-01C deliberately leaves ambiguous bits raw: `085F` bits 9,10,12,14; `0860` bits 2,4,9,11,13,14,15; `0861` bits 2,7,9. Do not assert arbitrary fault names or alarm-free status from missing/stale page.
- Local XTR 2026-10-03 passive capture has `085F..0861=0000` in checked samples. This proves only no active mapped fault **at that time**, not full alarm name translation for fault cases.
- Reading/decoding does not ACK alarms, alter 085F owner/service session or request unsafe frames.

## Alarm/history records (read-only)
- `0884/count60` **modern XTR** payload structure is **eight 7-word records plus 4-word trailer** and locally demonstrated newest-entry rolling behavior. Do NOT apply the older ATEC 10 x 6-word `[code,minute,hour,day,month,year]` structure.
- No reliable **history record code -> friendly alarm name** dictionary was recovered in extensive existing OEM searches across device-client, service API, OnSite, ET/MQTT, service manager, diagnostics, appfs/rootfs/assets (R44 and R62/R75-84). This is a genuine source-coverage blocker, not a missed direct `alarms.json` join.
- Current-alarm `085F..0863` bit indices and 0884 historical event-code numbers are **different ABIs**. Matching numerically is invalid. Show history records with raw event code/time fields if independently decoded and fresh, and `Onbekende historische code (raw N)` rather than invented user-facing name.

## Implementation decision / next one action
Integrate the sourced read-only bitmaps, current-alarm bit decoder and local modern history record structure into **single existing V5 passive RX owner** in next consolidated firmware revision, using observed controller-originated FC16 pages only, owner freshness and unavailable-on-stale; no parallel UART, no additional physical TX or HA parameter writes. Preserve original `Compressor Current` exact ESPHome/HA identity and history. The rest may use a fresh HA presentation catalog. C5DN last source-only catalog is not proof of these decoders deployed.

**CURRENT MILESTONE:** full source-grounded XTR read-only HA coverage.
**DELIVERABLE:** calendar/active alarm/history OEM source assessment.
**REAL BLOCKER:** historical event-name dictionary is not present in recovered gateway resources; naturally occurring local alarms not yet correlated for all current bits.
**ONE NEXT ACTION:** integrated read-only decoder based on this mapping in current locally live-derived YAML, with provenance flags and original Compressor Current intact; compile and user flash remain separate.
