> **Reconciliation status: APPLIED / HISTORICAL (2026-10-03).** The canonical Research state was reconciled through PROTO-OFFLINE-16 in commit `b4edd42cd17354845ec75111fb0aa30e5a0bda38`. This file is retained as the historical proposal that informed that reconciliation; do not apply it again blindly.

# Pending canonical reconciliation — PROTO-OFFLINE-16

**Date:** 2026-10-03  
**Status:** COMPLETE / POSITIVE — offline register/schema consolidation  
**GitHub:** not modified  
**Live experiment:** EXP388 remains RUNNING / PARTIAL

## THERMIA_PROJECT_STATE.md — proposed additions

- Add `PROTO-OFFLINE-16 — COMPLETE / POSITIVE — native settings/register schema consolidation`.
- Architecture correction: Online `registerIndex` is profile/model scoped. Numeric address can match native `0x0F`, but semantic labels are not universal across Thermia families.
- Stable ATEC+iTec core heating semantics:
  - `03E8` Heat Curve
  - `03E9` Heating Min
  - `03EA` Heating Max
  - `03EB` Curve +5
  - `03EC` Curve 0
  - `03ED` Curve -5
  - `03EE` Heat Stop
  - `03F0` Room Factor
- Local XTR proven settings:
  - `03E8` Heat Curve
  - `03EB` Curve +5
  - `03F4` Room Setpoint
  - `0442` Activate Cooling
  - `0553` Operation Mode at least `1=AUTO`, `2=COMPRESSOR`.
- Retire `03F1 = HotWaterStart` for XTR; status DISPROVEN/SUPERSEDED.
- `042E` is profile-dependent:
  - ATEC: Integral A1
  - iTec: Hot Water Status 0/1
  - genuine modern Eco5 E4 `1->0` strongly supports iTec Hot Water Status interpretation.
  - local XTR semantic remains OPEN.
- `042F` has a proven genuine desired-state mutation but semantic remains OPEN.
- `0559` Link Integration remains strongly supported cross-profile; local XTR value 0 observed, semantic causality/write not proven.
- Service/runtime correction:
  - `0870` compressor operating time
  - `0872` heating
  - `0873` cooling
  - `0876` hot water
  - `0877` auxiliary/immersion 1
  - `0878` auxiliary/immersion 2
  - `0879` auxiliary/immersion 3 (ATEC + XTR manual aligned, local XTR not confirmed)
  - `087B` defrost count
  - `087C` interval between last two defrosts
  - `087D` time/runtime since last defrost.
- Supersede prior contiguous `0872..0878 = seven operation counters` hypothesis.
- Preserve raw bridge `0870=(06E3<<8)|06E2`; reinterpret its semantic as compressor operating time.
- Safety: semantic address proof != desired-state write-path proof. Keep these evidence layers separate.

## EXPERIMENT_LOG.md — proposed entry

### PROTO-OFFLINE-16 — COMPLETE / POSITIVE — native settings/register schema consolidation

**Hypothesis:** native/Online numeric register namespace is substantially shared but profile-specific; a profile-aware database can resolve existing contradictions and reduce unsafe cross-model assumptions.

**Controlled change:** offline-only reconciliation of local XTR causal experiments, genuine desired-state captures, public ATEC/iTec Online profile metadata, firmware and XTR manual. No device traffic or settings change.

**Key results:**
- universal register-map hypothesis rejected;
- `042E` semantic conflict resolved as profile drift; modern Eco5 values favor iTec Hot Water Status;
- stable heating family identified across ATEC+iTec;
- local XTR proven setting set consolidated;
- `0870` identified as compressor operating time;
- operation-time sparse layout established;
- `087B/C/D` defrost meanings strongly upgraded;
- old `03F1=HotWaterStart` and contiguous `0872..0878` hypotheses superseded.

**Result:** COMPLETE / POSITIVE.

## PROTOCOL_FINDINGS.md — proposed durable updates

### PROVEN / locally confirmed

- `03E8` Heat Curve.
- `03EB` Heat Curve +5.
- `03F4` Room Setpoint; local desired-state writer confirmed semantic adoption/republish.
- `0442` Activate Cooling, `0=OFF`, `1=ON`.
- `0553` Operation Mode for at least `1=AUTO`, `2=COMPRESSOR`.

### STRONGLY SUPPORTED / profile-aware

- `03E9` Heating Minimum.
- `03EA` Heating Maximum.
- `03EC` Curve 0.
- `03ED` Curve -5.
- `03EE` Heating Stop.
- `03F0` Room Factor.
- `0559` Link Integration, public enum `0=LIGHT`, `1=SYSTEM`; local XTR effect not causally confirmed.
- `0870` Compressor Operating Time.
- `0872` Heating Operating Time.
- `0873` Cooling Operating Time.
- `0876` Hot Water Operating Time.
- `0877` Auxiliary/Immersion 1 Operating Time.
- `0878` Auxiliary/Immersion 2 Operating Time.
- `0879` Auxiliary/Immersion 3 Operating Time: ATEC public profile + XTR manual alignment; local XTR confirmation pending.
- `087B` Defrost count.
- `087C` time/runtime between last two defrosts.
- `087D` time/runtime since last defrost.

### PROFILE-SPECIFIC / do not universalize

- `042E`:
  - ATEC profile: Integral A1.
  - iTec profile: Hot Water Status.
  - genuine Eco5 command `1->0` strongly favors Hot Water Status for that modern profile.
  - local XTR label OPEN.

### PROVEN STRUCTURE / SEMANTIC OPEN

- `042F` genuine desired-state mutation `1->0`.

### DISPROVEN / SUPERSEDED

- `03F1 = HotWaterStart` as an XTR mapping.
- `0872..0878 = seven consecutive XTR operation-time counters`.
- public Online registerIndex as one universal Thermia semantic map.

### Safety

Keep four evidence dimensions separate:
1. address exists;
2. semantic label confirmed;
3. profile says writable;
4. native desired-state path proven.

Do not use profile writability alone to authorize an XTR write.