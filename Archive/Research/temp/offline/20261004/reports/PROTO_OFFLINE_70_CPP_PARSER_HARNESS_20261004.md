# PROTO-OFFLINE-70 — Standalone C++ parser harness

**Date:** 2026-10-04  
**Status:** **COMPLETE / POSITIVE — SOURCE-FAITHFUL C++ PARSER REPRODUCES GENUINE CORPUS AND PROTO63 AMBIGUITY**  
**Hypothesis:** the current v4.1 parser behavior can be reproduced in compiled standalone C++, reducing the gap between Python shadow models and the actual C++ logic embedded in ESPHome.  
**Controlled change:** offline host compilation/execution only. No ESPHome YAML change, no firmware build, no bus TX, no flash.

## Compiler

`g++ (Debian 14.2.0-19) 14.2.0`

This is a **standalone host C++ build**, not an ESPHome compile.

## Harness provenance

The harness ports the current v4.1 stream assembler logic:

- the exact known-slave set;
- the exact known-function set;
- the same function-specific candidate-length rules;
- ascending candidate sort/unique;
- first CRC-valid candidate wins;
- byte-at-a-time resynchronization;
- pending-buffer behavior relevant to the tested streams.

Fixture input contains **25,031 CRC-valid genuine Online/DCM frames** extracted from the seven current genuine captures.

SHA-256:

- harness source: `1633f2db343a2fa2a716f5007884df5f492b437b71d754f588bf47501e63e304`
- genuine-frame fixture: `9440f0e1989b957f8e957bd954fc52f6962d6c1f6e9128620e05ed4ff1049ddf`
- compiled host binary: `2f0be85ee963ca17da82d7b9633a25d3cad40bbf62765f379c20ff81ae544add`

## Genuine replay

Each genuine frame was delivered to the compiled C++ parser with randomized internal chunk sizes across 50 complete corpus passes.

Result:

**50 / 50 complete genuine-corpus runs reconstructed all 25,031 frames exactly.**

No Python parser logic is involved in the C++ stream-processing step itself; Python was used only beforehand to export the raw CRC-valid frame fixture from the existing captures.

## PROTO63 adversarial regression

The harness also constructs the three deterministic longer CRC-valid FC03 frames whose first 8 bytes are themselves CRC-valid semantic desired-page requests:

- `042E/count15`
- `0442/count13`
- `0546/count20`

Compiled current-parser behavior:

- whole ambiguous frame supplied in one call -> short semantic prefix selected: **3/3**
- ambiguous frame split after byte 8 -> short semantic prefix selected: **3/3**

Observed examples:

- `042E`: full `0F03042E000F65D900` -> parsed first `0F03042E000F65D9`, one byte remains
- `0442`: full `0F030442000D240500` -> parsed first `0F030442000D2405`, one byte remains
- `0546`: full `0F0305460014A5F20000` -> parsed first `0F0305460014A5F2`, two bytes remain

## Observed facts

- compiled C++ reproduces the current parser's behavior over all current genuine fixtures;
- compiled C++ independently reproduces the PROTO63 shortest-valid-prefix ambiguity;
- the ambiguity is therefore not an artifact of the earlier Python parser transcription.

## Strong conclusion

PROTO63/67's parser property is now confirmed at a **compiled C++ algorithm level**.

This strengthens the implementation finding while leaving its live-risk classification unchanged:

- PROTO65: zero genuine corpus collisions;
- PROTO69: current 9600 8E1 + 5 ms idle callback timing makes split-prefix delivery physically unlikely for normal contiguous short RTU frames.

## Limitations

- this is not the generated ESPHome C++ translation unit;
- it does not include ESP-IDF UART driver or ESPHome UART-debug callback scheduling;
- it does not emulate FreeRTOS timing/concurrency;
- therefore it is not firmware-level proof of a live fault.

## Live status

Unchanged. No bus action occurred.