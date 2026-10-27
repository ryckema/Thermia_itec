# PROTO-OFFLINE-31 — 0884 raw event-ID archaeology

**Date:** 2026-10-03  
**Status:** **COMPLETE / NEGATIVE** — no safe raw-ID -> displayed alarm/event mapping recovered.  
**Hypothesis:** raw identifiers in `0884/count60` may correspond directly to a public Thermia/Danfoss alarm enumeration, register address or documented error code.  
**Controlled change:** offline external/document/code archaeology only. No device TX, YAML change, reboot or setting write.

## Raw IDs searched

Legacy and modern history values include:

`0x0002, 0x0019, 0x0029, 0x002A, 0x002C, 0x0172, 0x1400`.

## Thermia Online public profile result

The public iTec Online fixture contains a `REG_ERROR_CODES` group but that group is empty in the captured profile metadata.

No raw `0884` event-ID enumeration or error-name dictionary is exposed there.

## Genesis Modbus comparison

Official Thermia Genesis Modbus documentation exposes numeric digital alarm addresses, including examples such as:
- 25 = Compressor low speed alarm;
- 44 = WCS return line sensor alarm on applicable systems.

Two raw history values numerically collide with those addresses:
- `0x0019 = 25`;
- `0x002C = 44`.

This is **not sufficient for mapping**.

Reasons:
1. the history ABI is from legacy Online/Eco5/XTR families, not a proven Genesis alarm-address ABI;
2. `0x002C` occurs repeatedly in the Eco5 history without evidence of a WCS-return-sensor alarm;
3. raw modern IDs `0x0172` and `0x1400` are far outside the ordinary Genesis alarm-address range;
4. `0x0002` would collide with a generic alarm-class status bit rather than a unique event identity.

### Strong conclusion

The direct model:

`0884 raw ID == public Genesis alarm address`

is **DISPROVEN as a universal decoder**.

Numeric collisions may still be historical/shared-enum coincidences, but they are not evidence-backed names.

## Danfoss generic alarm-code comparison

Other Danfoss product families also use low numeric alarm/status indices such as 0x29/0x2A/0x2C. Those enumerations are product-specific and do not provide Thermia heat-pump event provenance.

They are therefore rejected as semantic donors.

## Current best model

For modern XTR/Eco5:

`raw A / raw B`

should remain an opaque event identity / flags tuple until one of these becomes available:
- labelled XTR alarm transition captured at matching timestamp;
- Thermia Connect/DCM serializer table;
- firmware/app error dictionary;
- official mapping table.

## Evidence classification

### Observed
- public iTec Online profile has an empty `REG_ERROR_CODES` group;
- some raw IDs numerically overlap public Genesis alarm addresses;
- other raw IDs exceed that address domain.

### Strong conclusions
- no current public source safely decodes the observed `0884` raw IDs;
- direct Genesis-address interpretation is not portable and is rejected.

### Unknown
- whether low raw IDs share a historical internal enum with some Thermia controller family;
- modern raw-B semantics;
- relationship to displayed XTR alarm name/E-code.

## Live status

Unchanged:
- EXP387 COMPLETE / POSITIVE
- EXP388 RUNNING / PARTIAL
