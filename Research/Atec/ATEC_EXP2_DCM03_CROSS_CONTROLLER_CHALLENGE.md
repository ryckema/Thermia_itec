# ATEC-EXP2 — isolated DCM03 cross-controller challenge compatibility

**Date:** 2026-10-03  
**Status:** PREPARED / NOT RUN  
**Baseline:** ATEC-COLDSTART-01 — COMPLETE / POSITIVE  
**Target device:** classic DCM03 only  
**Heat pump/controller on bus:** **NO**  
**Experiment class:** bounded active FC17 DCM-only bench test

## Hypothesis

A classic DCM03 that answers its own captured ATEC `071C/0730` challenge may also answer a challenge captured from an Eco8 controller. A positive result would show that DCM03 response capability is portable across controller generations in the tested standalone context.

A foreign-challenge negative is interpretable only if the captured ATEC challenge succeeds first as a positive control on the same isolated bench.

## Exact controlled change from ATEC-COLDSTART-01

ATEC-COLDSTART-01:
```text
ATEC controller <-> DCM03
```

ATEC-EXP2:
```text
bench master <-> DCM03 only
```

No FC16 page ACK, `0708` response, setting write, scan, or unknown register traffic is allowed.

## Active target and safety declaration

- slave: `0x0F`
- function: `0x17` Read/Write Multiple Registers
- read start: `0x0730`
- read count: `8`
- write start: `0x071C`
- write count: `8`
- bytecount: `16`
- known current value: **unknown / opaque DCM03 internal challenge-mailbox state**
- mapping source: genuine ATEC/DCM03 cold-start pair + genuine Eco8 challenge corpus
- expected effect: `0F 17 10 <16-byte body> <CRC>` within 200 ms
- plausible unintended effects: DCM03 internal session/binding state may change or DCM03 may error/reset
- HP-side effect: none, because HP/controller must be physically absent
- recovery: stop TX; power-cycle DCM03; restore isolated bench; rerun control

These FC17 probes are **not read-only Modbus traffic**: each writes eight words to `071C..0723` while reading eight from `0730..0737`.

## Phase A — positive control

DCM03 should already be powered/listening before the probe.

Exact captured ATEC request:
```text
0f1707300008071c0008102ee156572b8b84a0bc7a65c72d56185d7840
```

Native captured response:
```text
0f171020b8f28a236f28fa0339669e2c6f600d57d9
```

### Control success

Any CRC-valid exact-shape response:
```text
0f 17 10 <16 bytes> <CRC>
```
within 200 ms.

An exact body match to `20b8f28a236f28fa0339669e2c6f600d` is stronger evidence, but a different valid DCM-generated body must also be recorded.

Repeat control up to three times with ~4.3 s spacing if necessary.

### Control failure

If no valid response after three correctly transmitted control probes:

**ATEC-EXP2 = COMPLETE / INCONCLUSIVE**

Stop. Do not continue to Eco8 challenges and do not interpret foreign silence.

## Phase B — Eco8 foreign challenges

Only after Phase A success.

All frames include verified Modbus CRC:
```text
0f1707300008071c0008107e928bcfce5c05ba4e973e617004c2edf39d
0f1707300008071c000810a7d68d50ebeb55e4bc2f26ba23f0a06665f7
0f1707300008071c0008108fc003efddd746c112eb1b7228f12b958810
0f1707300008071c000810c26c4ff6085912ed7e88e52f0f247bc0280b
0f1707300008071c0008102640b87be0a5cd11ceebfb791e51ad56b621
0f1707300008071c00081046cb69b9296eb9f20a3320b88e17f1f4d4b4
```

Procedure:
1. send one challenge;
2. listen for 200 ms;
3. record exact response bytes and latency;
4. wait until ~4.3 s from previous probe;
5. continue to next challenge;
6. repeat the six once under identical conditions if DCM remains stable.

Do not send additional “readiness” traffic.

## Result classification

### COMPLETE / POSITIVE

- Phase A control succeeds; and
- at least one Eco8 challenge gets a CRC-valid `0F 17 10 <16-byte body>` within 200 ms.

Record whether repeated identical challenges produce identical or different bodies.

This would make a DCM03 hardware-oracle/bridge route a genuine candidate, but it does **not** prove the Eco8 controller accepts that generated answer until a separate bounded Eco test.

### COMPLETE / NEGATIVE

- Phase A succeeds reliably; and
- all 12 bounded Eco8 probes (six × two passes) receive no valid response.

Interpretation: standalone cross-controller response is not observed in this tested state. Do **not** promote that to “pairing-bound algorithm proven”; missing prior bus/session context remains possible.

### COMPLETE / INCONCLUSIVE

Any of:
- positive control fails;
- TX cannot be independently verified;
- DCM resets/errors;
- bus not isolated;
- framing/CRC uncertainty;
- materially different conditions between control and foreign probes.

## Abort criteria

Stop immediately if:
- any HP/controller is on the bus;
- another master/slave creates collisions;
- unexpected DCM error/reset behavior appears;
- a transmitted frame differs from listed bytes;
- CRC verification fails.

## What to return

- timestamped TX line for each request;
- every DCM03 response line;
- request->response latency;
- confirmation HP/controller absent;
- whether DCM03 was power-cycled before run;
- independent TX verification method.

Do not advance to live Eco8 injection from preparation alone. Wait for the bench result.
