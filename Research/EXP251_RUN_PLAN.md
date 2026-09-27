# EXP251 — Shadow DCM / approval harness

**Status:** PREPARED / NOT RUN

## Hypothesis

The known iTec Online/DCM lifecycle can be represented as a state machine with one unresolved opaque 16-byte `071C -> 0730` approval-response boundary. The rest of the controller/gateway traffic can be classified without transmitting anything to the heat pump.

## Only experimental change

Replace EXP249 retry-window instrumentation with shadow DCM lifecycle classification. Production parsing/entities remain unchanged.

## Classifier

EXP251 recognizes:

- exact `0x0F FC17 read0730/count8 + write071C/count8` approval requests;
- local XTR RTC/service consistency;
- Hamming distance to the two reported Eco 5 source challenges;
- unexpected peer FC17 16-byte response candidates;
- 0x0F FC16 requests and peer FC16 ACKs;
- exact `0x0F FC03 0708/count6` mailbox polls;
- other 0x0F FC03 page reads;
- A80E/A80F/AFDC and 0x06 context.

## Procedure

1. Flash EXP251.
2. Wait at least 15 s with normal bus traffic.
3. Home Assistant → Configuration → **EXP251 Arm Shadow DCM**.
4. Within 60 s power-cycle only the Thermia controller; keep ESP/Waveshare powered.
5. Do not change any Thermia setting during the trace.
6. Wait for `SUMMARY SHADOW_COMPLETE`.
7. Save the complete log from ARM through SUMMARY.

## Expected local result

- approval requests appear;
- W071C decodes as the known local RTC/service record;
- `SHADOW_0730=UNRESOLVED TX=OFF`;
- no peer FC17 16-byte response;
- no peer FC16 ACK;
- no native 0708 mailbox transition;
- retries stop naturally around the already-proven ~267 s point;
- parser resync/drop deltas remain zero.

Any peer FC17 response, FC16 ACK or 0708 mailbox request is high-value unexpected evidence.

## Safety

Fully RX-only:
- GPIO17 TX absent;
- GPIO21 DE LOW;
- no ACK;
- no response;
- no scan;
- no register write;
- no room-sensor emulation;
- no Eco 5 response bytes stored for transmission.
