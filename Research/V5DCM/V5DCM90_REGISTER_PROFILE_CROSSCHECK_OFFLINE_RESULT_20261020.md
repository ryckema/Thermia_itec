# V5DCM90 — Original CM930 vs XTR vs ATEC V3 register family audit

**ID** V5DCM90-PROFILE-FAMILY-CRC-CROSSCHECK-OFFLINE-01; **COMPLETE / POSITIVE (offline semantic alignment only)**, 2026-10-20.

Baseline user-verified V83-FAS1 RX_ONLY/HARD_DENY; original V49 rollback; EXP388 RUNNING/PARTIAL; earlier first-start B11D discrepancy OPEN. ONE CHANGE: offline CRC-validated parsing of existing XTR FC16 captures, schema comparison with original Connect2.1.105 four CM930 sensor configurations and ATEC V3 third-party documentation. No TX, flash, compile or new device run.

## OBSERVED FACTS

Five archived XTR captures contain 19 CRC-valid complete 0x0F FC16 request records covering each of registers 2080, 2081, 2095, 2151. Values: 2080=80/86/89; 2081=148/150/176/177/178/327/328; 2095=130; 2151=22. This remains historical XTR evidence, not proof of actual native gateway acceptance.

Original Thermia Connect 2.1.105 930 sensor configurations: air-to-water ranges 1.1.1–2.1.0 and 2.3.0–2.4.3 both interpret 2080 as outdoor condenser-in, 2081 as condenser-out and 2095 as outdoor operation status/bitfield. Brine ranges 2.2.0–2.2.1 and 3.0.0–3.1.1 interpret 2080 as evaporation pressure and 2081 as suction temperature, without equivalent 2095 outdoor status sensor. The ATEC V3 author externally describes the same air-to-water semantic criterion, selects 2.3.0–2.4.3 manually and acknowledges ambiguity with 1.1.1–2.1.0. Cited historical ATEC source captures are absent; label EXTERNAL CLAIM.

## CONCLUSIONS, UNKNOWN, NEXT

STRONGLY SUPPORTED: air-to-water original sensor semantics are candidate interpretation for XTR registers, but register identity and historical values alone do not distinguish the two air-to-water firmware ranges, prove full 2095 bit semantics, establish actual firmware profile selection, or resolve 2151 raw22 -> 0.2.2 original decoder mismatch. UNKNOWN native XTR electrical owner/slot/EOF, app session, accepted writes and actual current firmware version. No FC16 ACK equated with semantic acceptance. No protected gateway/authentication/mailbox code included.

**Abort** offline assertion interpretation if CRC, ADU length, offsets or original vendor schema disagree; **rollback** hardware N/A. No ESPHome compilation or flashing. NEXT V91 OFFLINE discriminatory field comparison, stop inconclusive if source/capture cannot distinguish.
