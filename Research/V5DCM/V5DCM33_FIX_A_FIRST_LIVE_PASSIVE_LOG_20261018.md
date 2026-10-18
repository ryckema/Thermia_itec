# V5DCM33-FIX-A — First user-flashed passive log (2026-10-18)

**Experiment:** V5DCM33-FIX-A-LIVE-PASSIVE-01 — **RUNNING / PARTIAL** (passive observation only; no ARM or heat-pump controller restart). Original OFFLINE V5DCM33-FIX-A source/host experiment remains **COMPLETE / POSITIVE**. Live rejoin remains **PREPARED / NOT RUN**.

## Provenance
- User stated V5DCM33-FIX-A was already flashed and supplied 2,050-line ESPHome API log `Pasted text(20261018-203321).txt`. Log SHA256 `96f4f25dc5ee551f21a7d3c5173eece70ec62f85bef585f44d4d65207a9e46ed`, 151,239 bytes.
- Visible 22:31:51–22:33:14, uptime 30/60/90s at 22:32:13/43 and 22:33:13. ESPHome 2026.9.0 connects via API and shows HA readings continuing.
- CLI states **validated config cache for `waveshare-thermia_GAP51D_CLEAN_RX_ONLY_PREPARED_NOT_FLASHED.yaml`**, which is NOT proof of the actual compiled/flashed source. Runtime reports V5DCM32 observer marker but no explicit V5DCM33 build ID or firmware SHA; user-flashed FIX-A is USER-ATTESTED, exact identity **UNVERIFIED**. No ESPHome full compilation evidence, no physical DE measurement.

## Observed facts
- At 22:32:44.862 `[B11D-RX]` original RAW batching counts 1,563 callbacks/11,387 bytes/529 RAW frames and 529 portable and V5 compared, `countDiff=0 byteDiff=0 noise=0 incomplete=0 ambiguous=0 overflow=0 nativeFault=0/0/0 ioTx=0 hold=0 fault=0 DE=0`. Earlier 22:32:14.862 B11D 272/272 with zero differences. B11D First Fault `NONE` and Raw Faults 0 throughout displayed snapshots.
- At 22:32:46.598 `[B11C-PORTABLE]` 548 frames/548 V5, `countDiff=0 byteDiff=0 boundaryFaults=0 resync=0 drops=0 ioTxAttempts=0 hold=0/0 fault=0 DE=0`. Sensor values including supply/return/compressor/heating continue and RX buffer drops 0.
- V5 parser resync steps **8 from first observation onward, NOT increasing during this log**, drops 0, badGeom 0. Initial origin of these eight resyncs not in supplied excerpt. `V5 Bridge02 RX Integrity Faults=1` and `R6 P5 Session Classification=UNQUALIFIED / FAULT_LATCHED / NO_TX` continue even while current RX clean (`P74D RX_NOW=CLEAN P5_HISTORY=1 NEW_HOLD=0`). These are distinct historical/per-session health gates, NOT evidence of a contemporaneous B11D new fault.
- A `[V5 BRIDGE04-1] OBSERVER_RECOVERED only=passive historyFaults=1 recoveries=1 TX_AUTH=0` event at 22:32:12.767, with first fault metadata `resync=8(+8) drops=0(+0) ambig=0(+0) valid=1 pendingBefore=0 bytes=35 first=00:1E`. This is Bridge04-1 observer historical fault, **not** `B11D First Fault`; do not conflate.
- 22:33:13.330 V5DCM32 RX_ONLY `step=0 scope=0 localGen=0 verdict=0`; V5DCM23 portable 1/33. FC23 boundaries for **native 0x0F** 0. Controller witness `NO_CALLBACK_GAP_SEEN`; no ARM or controller power cycle performed in this pass. Normal HA 0x02 and 0x0A FC23 pair counters are not native 0x0F handshake.
- At 22:33:13.047 TX executor `HARD_DENY candidates=126 denied=126 physical_attempts=0`; `V5 S2 Physical TX Attempts=0`, `V5 S3 UART Write Calls=0`, DE=0 in software logs. Physical DE pin not measured.

## Result and interpretation
**PARTIAL POSITIVE baseline observation:** no evident production RX/telemetry regression; B11D and B11C remain current healthy and TX software blocks all native candidates. The 1–4 byte deferral **was not exercised in a demonstrably faulting 1–4-byte fragment**, hence no claim the change resolved prior V5DCM32 22:02:30 `RAW_INCOMPLETE_AT_IDLE` and 12,923ms controller gap. No local epoch, native online acceptance, ACK/owner or active rejoin proof. Earlier live V5DCM32 fresh rejoin COMPLETE / NEGATIVE remains unchanged.

## Decision / next
**No ARM, no new controller restart requested** on this result alone. Proceed with separate V5DCM33-FIX-B offline post-gap observer integrity policy, distinguish B11D new sticky fault from Bridge04-1 historical observer fault and from R6 P5 history, preserve HARD_DENY and original HA/CRC bookkeeping. To attribute FIX-A at machine-code level, need version/hash attestation; no compiler log requested routinely. Fallback verified older FIX2 kept.
