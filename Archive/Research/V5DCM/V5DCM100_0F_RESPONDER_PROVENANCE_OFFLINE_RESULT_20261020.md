# V5DCM100 — Local 0x0F responder provenance reconciliation (offline)

**Experiment ID:** V5DCM100-XTR-0F-OWNER-PROVENANCE-01  
**Status:** COMPLETE / POSITIVE (historical intervention contrast only; physical ownership remains OPEN)  
**Date:** 2026-10-20

## Baseline and controlled change
Prior V5DCM99 offline count, V83-FAS1 RX_ONLY / TX=HARD_DENY as most recent reported installed basis, original V49 rollback, EXP388 RUNNING / PARTIAL, B11D first-start issue OPEN. Sole intervention was to reconcile the verified previously completed EXP254–258/355/386 intervention ladder against V5DCM99 captured FC16 ACK counts. No live TX/flash/controller action or hardware change.

## OBSERVED LOCAL EXPERIMENT EVIDENCE
- EXP254 and EXP255: after controller restart with ESP RX-only/no response, 63 native 0x0F FC23 approval attempts, no 0x0F FC16 ACK or FC03 0708 service. Other periodic native pages existed; do not mistake this as no 0x0F activity whatsoever.
- EXP256: precisely one bounded historically qualified answer, then no FC16 ACK; next 03E8/count14 followed around 124 ms later, repeated 389 times in incomplete-service mode and generated real COMM. ERR ONLINE/LINK with DHW-side zero.
- EXP257: one exact 03E8 ACK permitted next 03FC/count11 page (~691 ms).
- EXP258: one exact 03FC ACK permitted subsequent 0410/count22 (~1.501s).
- EXP355/386: different previously qualified retained session, guarded response plus complete historical native acknowledgment/status chain led to 32/32 page service and later 0708. Neither exercise proves generic first-cold acceptance or fully valid Connect cloud/application session.
- V5DCM99 local historical timestamped captures yielded 337 FC16 requests, 306 ACK and 122 FC03 requests across five logs, but the timing files alone do not label sender, running YAML, electrical DE state or wire EOF-to-SOF.
- Original Connect source and external ATEC reference independently model logical 0x0F gateway behavior. ATEC is EXTERNAL SOURCE/CLAIM only, not local XTR proof.

## STRONG CONCLUSIONS
The controller's observed native session behavior changes when the ESP supplies bounded responses; sequential FC16 ACKs progress first pages, and an ESP-serviced 32-page session was observed. Thus an external protocol responder is demonstrably FUNCTIONALLY viable in tested XTR epochs. The earlier historical 0x0F ACK counts are not independent evidence of an otherwise present internal competing responder until the old capture's firmware/TX provenance is established. This does NOT independently identify the actual electrical source of every historical ACK, prove absence of any built-in 0x0F responder in all modes, or qualify V5 current TX.

## HYPOTHESES
Many old 0x0F ACKs were produced by ESP TX-enabled historical gateway code, rather than an internally integrated permanent controller responder. Confirm only by matching original capture timestamps, flashed YAML/version, TX counters and DE signal.

## OPEN UNKNOWNS
Physical owner/DE origin, current first-cold peer absence and exact stopbit-to-startbit interval, real controller acceptance of modern response path, 33 genuine Connect application groups versus 32 historical bootstrap ACKs, profile mismatch.

## Decision / next action
NO-GO automatic takeover on XTR from the ATEC source. Avoid repeat EXP256 incomplete service (real adverse alarm). Smallest evidence needed: identify prior captures' active firmware and any per-frame TX-direction observability; if absent, prepare passive dual-channel DE/RX logic capture across a NORMAL ongoing session without restart, with no TX change. Only thereafter propose scoped user-initiated complete-service live run; preserve production HA and watchdog. No raw authentication, secrets, proprietary challenge computation or 0x0708 command code published.
