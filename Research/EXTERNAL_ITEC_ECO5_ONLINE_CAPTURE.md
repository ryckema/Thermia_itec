# External evidence — iTec Eco 5 with genuine Thermia Online gateway

Date recorded: 2026-09-27

Source: piotrek_r / Home Assistant community contribution.

Verification status: **raw log not yet ingested into this project**. This note preserves the contributor's reported observations and the immediate protocol implications. Reclassify individual details after the raw 10,719-frame capture and timeline script are independently processed.

## Capture

- iTec Eco 5
- genuine Thermia Online gateway
- 10,719 frames
- 1482 seconds
- all frames reported CRC-valid
- A/B/A power sequence:
  - pump on with gateway
  - pump on without gateway
  - pump on with gateway again

## Reported bus behavior

### Accessory roles

Every FC17 request to 0x06 and 0x0A remains unanswered (326 and 325 requests respectively, ~4.2 s cadence). No A5, A4 or 0x05 traffic appears.

### Online/session gate

From power-on the controller repeatedly sends:

~~~text
0x0F FC17
read  0730/count8
write 071C/count8
~~~

With the genuine gateway attached, a valid response appears after roughly two minutes / about two gateway boot cycles.

After the first valid response:

- 071C/0730 exchange stops;
- controller starts acknowledging FC16;
- controller performs a full-state dump over decimal 1000..1780 and 2000..2160;
- controller starts polling decimal 1800 / hex 0708 with FC03.

In the middle no-gateway cycle this downstream state machine never starts.

### Controller and gateway 16-byte examples

~~~text
C 63cefb32c6f41382087992370caceeba
R 1691a5f3f8e8d58738924416e8e6a3d5

C 31fb59fc8fb1175cd89f904d06d92ea4
R fd636ccd0f921d83ff232a1a2413b372
~~~

The contributor reports about 90 distinct controller values across two clock hours. None fit the previously proposed RTC/calendar encoding. One exact 16-byte controller value repeats four seconds later during an unanswered exchange, resembling a retry.

### Mailbox

After Online/session establishment:

- app change -> second mailbox word set;
- value 1 -> controller reads decimal 1000 count14;
- value 8 -> controller reads decimal 1070 count15;
- gateway returns desired-state page;
- controller applies state;
- physical display changes are sent by controller as plain FC16 and do not use the mailbox.

## Project interpretation

### Strong conclusions

- 071C/0730 is a real iTec Online/session gating exchange.
- iTec Online does not require 0x06/0x0A gateway responses or A5/A4/0x05 traffic.
- The 0708 mailbox model is valid on iTec after successful session establishment.
- The prior RTC/calendar model for 071C must be withdrawn as a general interpretation.

### Strong hypothesis

The 16-byte controller write is a challenge/session token and the 16-byte gateway return is an authenticator/response.

The 128-bit block size and noise-like values are compatible with a cryptographic primitive, but no specific algorithm is yet proven.

### Immediate analysis plan when raw log arrives

1. Extract every 071C challenge and 0730 response with timestamps.
2. Classify unanswered attempts, retries and fresh challenges.
3. Determine whether repeated challenge implies repeated response.
4. Measure per-byte/bit variation and response diffusion.
5. Search for simple XOR/add/rotate/word-swap/CRC-style relations and rule them in/out.
6. Test block-cipher/MAC hypotheses only against evidence and known candidate key material.
7. Correlate exact first successful response to FC16 ACK, state dump and first 0708 poll.
8. Build the minimal ESP state machine only after the response function is constrained.

No active challenge response is approved yet.
