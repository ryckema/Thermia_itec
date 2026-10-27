# PROTO-OFFLINE-34 — `0708 W5` semantic audit

**Date:** 2026-10-03  
**Status:** **COMPLETE / POSITIVE** — W5 role is materially narrowed, but not assigned a universal enum.  
**Hypothesis:** W5 can be distinguished as transport state, scheduler state, liveness/UI-connected metadata, or profile-specific implementation metadata by combining genuine captures with the EXP344/345 controlled local XTR discriminator.  
**Controlled change:** offline analysis only. No bus TX, YAML change, reboot or setting write.

## Genuine-capture distribution

Across all 302 answered genuine `0708/count6` responses:

### Older genuine Online/DCM captures
- 38 answered responses total;
- `W5=0006` in **37/38**;
- `W5=0007` in **1/38**.

The single `W5=0007` response is the known legacy rejoin event:

`W2/W3 = 7FFF/FFFF`
`W4 = 0080`
`W5 = 0007`

After the refresh/rejoin progression, the same capture returns to `W5=0006`.

### Genuine Eco5 Online captures
- 264 answered responses total;
- `W5=0000` in **264/264**.

W5 remains zero through:
- ordinary idle/runtime;
- broad configuration refresh;
- staged W4 service work;
- desired-state commands.

## Local XTR controlled evidence

EXP344 and EXP345 form the strongest causal discriminator.

### EXP344
Idle mailbox:

`W0..W5 = 0000 0000 0000 0000 0000 0000`

Result:
- stage-40 transport/runtime remained clean >15 min;
- no Online/Link communication error;
- **DCM icon absent** after the soak.

### EXP345
Only controlled change:

`W5: 0000 -> 0006`

All bootstrap, FC16 service, runtime ACK policy and soak behavior otherwise preserved.

Result:
- clean >15 min runtime;
- **DCM icon remained present**;
- no Online/Link communication error.

Later retained-runtime and semantic-write experiments continued using W5=0006 successfully.

## Strong conclusions

1. **W5 is not required for basic transport/runtime service.**
   EXP344 remained transport-clean with W5=0.

2. **W5=0006 is sufficient to retain the DCM-connected UI indication on the tested local XTR M emulator path.**
   This is locally causal evidence from the EXP344 -> EXP345 one-variable comparison.

3. **W5 is not a universal “connected=true” enum.**
   Genuine Eco5 Online runs normally with W5=0 in all 264 answered responses.

4. **W5 is profile/implementation/session metadata that participates in local XTR DCM-connected presentation/liveness semantics.**
   That wording fits both local causal evidence and cross-profile genuine captures.

5. **W5=0007 cannot be independently decoded.**
   It is observed once, together with a legacy `7FFF/FFFF` rejoin/full-refresh state. It may mark a transient rejoin/session phase, but the single co-occurrence does not prove that semantic independently of the bitmap.

## Refined terminology

Recommended current terminology:

- `W5=0006` — **legacy/local-XTR DCM-connected metadata value; locally sufficient for persistent DCM icon**
- `W5=0007` — **legacy transient rejoin-associated metadata candidate**
- `W5=0000` — **normal for genuine Eco5 profile and transport-valid locally, but insufficient for persistent local-XTR DCM icon in EXP344**

Do not expose W5 as a universal boolean or enum in Home Assistant.

## Unknowns

- exact firmware field/enum name;
- whether W5=6 affects anything beyond UI/liveness presentation on XTR;
- whether W5=7 has independent meaning apart from the legacy rejoin bitmap;
- why Eco5 profile uses W5=0 for fully functional Online runtime.

## Live status

Unchanged:
- EXP387 COMPLETE / POSITIVE
- EXP388 RUNNING / PARTIAL
