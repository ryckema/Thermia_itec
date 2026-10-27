# V5DCM86 — CM930 profile selection, flags and historical request groups

**Experiment:** V5DCM86-CM930-PROFILE-GROUP-COMPLETENESS-OFFLINE-01  
**Date:** 2026-10-20  
**Status: COMPLETE / POSITIVE — exact original Connect firmware SOURCE and historical XTR CRC metadata ONLY, NOT physical TX/native acceptance.**

## Baseline, hypothesis, controlled change

Installed/user-verified V5DCM83-FAS1 remains RX_ONLY/HARD_DENY: first RAW2=V5 expected2, B11D comparisons1028 with zero count/byte mismatch, main V5 parser1194 frames resync0/drops0, current FIX2 RX QUALIFIED; older separate V83 startup one-count difference remains unexplained. EXP388 remains RUNNING / PARTIAL; V49 was the older verified source rollback.

Hypothesis: CM930 original **profile-specific requested-group masks** differ from the 32 native controller configuration-page sequence. Single controlled **OFFLINE** operation: inspect byte-identical nonsecret source from `device_client.zip` and genuine extracted Connect 2.1.105, parse only packaged `930/modbus-flags.json` and four sets of sensors/configuration metadata, classify original Oct03 FC16 CRC-valid **start-address shapes**. No device code change, network, Modbus output, ESPHome compile, flash or Thermia controller restart.

## Original firmware (SOURCE facts only)

Eight original Python files in provided `device_client.zip` match byte-for-byte their genuine `2.1.105 extracted_appfs.zip` equivalents, including `configuration.py`, `data/info.py`, `data/extractor.py`, `cm/client.py`, `cm/cm_client_type.py`, `cm/modbus_server15.py`. Previous V84 two original source SHA pins checked.

`AppConfiguration.find_versioned_conf_dir` picks an actual version-range directory where `min <= SemVer <= max`. Bundled CM930 profile ranges: **1.1.1–2.1.0; 2.2.0–2.2.1; 2.3.0–2.4.3; 3.0.0–3.1.1**. The DEFAULT CM930 version extractor in `data/info.py` computes `semver(({2151}//100)%10, ({2151}//10)%10, {2151}%10)`. Historical local raw value **22** at 0x0867 decodes under this exact formula to **0.2.2**, which matches **NONE** of these packaged profile ranges. Hypothetical raw **220** decodes 2.2.0 and would match one range; **220 was NOT observed**. This discrepancy is OPEN, not justification to select any profile, nor proof of current live 0x0867.

Original `modbus-flags.json`: **1803 = 16 settings groups (1000–1349); 1802 = 16 settings groups (1350–1798); 1804 = 11 operation/status groups (2000–2239)** = 43 potential group bits. `request_read_all_registers` separately sets 16+16+10 = **42** bits, explicitly omitting operation bit8. Profile-specific required groups are computed from `sensors` + `configurations` `significant_registers()` (formula, min/max/default and conditions); NOT simply all 43 available bits, NOT the operation/info parser's register set. Received FC16 start address maps to ONE group via `_register_and_bit_for_address(...,request=True)`; it is used to clear that group in `reset_register_read_request` and the separate `CMClientParameterUpdateState`, whose completion condition is *all pending required bits zero*. This source behavior is not evidence of a real Connect client executing these transitions on the XTR.

| Bundled firmware profile | Required 1802 | Required 1803 | Required 1804 | Total |
|---|---:|---:|---:|---:|
| 1.1.1–2.1.0 | 14 | 9 | 7 | **30** |
| 2.2.0–2.2.1 | 14 | 9 | 8 | **31** |
| 2.3.0–2.4.3 | 15 | 10 | 8 | **33** |
| 3.0.0–3.1.1 | 14 | 9 | 8 | **31** |

Numbers are DISTINCT **vendor application required-group bits** and are NOT local controller page ACK counts or evidence of genuine APP33/C2 acceptance.

## Local historical evidence — CRC-valid Oct03 source, NOT on-device current FAS1 test

Exactly the first **32 FC16 request-shaped settings pages** from `0x03E8` through `0x06F4` map to **all 16 + 16 group-start intervals** of `1803` and `1802`, **ZERO** `1804` operation groups. After this first batch, an abstract vendor required-set model would still need **7/8/8/8** operation groups for four bundled profiles respectively. Across the entire historical October 3 file, **162** CRC-valid FC16 request shapes include at least one start address for **every one of the 43** possible group intervals (including 11 operation groups). This is HISTORIC FRAME-SHAPE COVERAGE ONLY: neither a FC16 ACK nor archived request-start mapping proves semantic acceptance, real CM930 bit clearing, native handshake, or Online.

## Provenance and scope

**PROVEN / ORIGINAL SOURCE ONLY:** exact version formula and supported ranges, source mask logic, required-group metadata and start-address clear semantics. **PROVEN / HISTORICAL LOCAL CAPTURE:** raw22 0x0867 in Oct03 (12 occurrences of 19 across all archives), 32+11 grouped start addresses and valid CRC. **STRONGLY SUPPORTED:** controller 32/32 ACK-shapes alone cannot establish vendor app completion: operational groups are missing from the initial 32. **OPEN:** actual current controller version/profile, raw22 mismatch root cause, real vendor app handshake/version-admission/data completeness, electrical peer/owner/EOF/slot, genuine APP33/C2/Online.

Reproducible privacy-safe six-file ZIP `V5DCM86_CM930_PROFILE_GROUP_COMPLETENESS_OFFLINE.zip` **SHA256 `1c6dbf9bfb54f4af2ddd34ee6f9b0a1a7c4def6a9d2a9c05b378f7e372ecddfc`**, containing source-pin AST audit, sanitized metadata JSON, 35 deterministic positive/negative Python tests, report and SHA manifest, ZIP CRC/hash verified. Tests **35/35 PASS** (including incorrect group/profile/mask conditions). No captured payload bytes, protected native reply, mailbox logic, credentials, live output tools. Abort if source SHA/CRC or test fails; physical rollback N/A.

**NEXT V87 (NOT RUN):** offline investigate historic raw `0x0867=22` vs vendor default formula `0.2.2` and absence of a matching CM930 profile using other authentic version/config source and existing passive captures before any new device experiment. FAS1 remains RX_ONLY; historical V83 startup issue and EXP388 RUNNING / PARTIAL retained. Do not repeat historical EXP256 incomplete first response (COMM ERR).
