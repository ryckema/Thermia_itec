# Canonical update pending — PROTO-OFFLINE-69..72

## PROTO-OFFLINE-69 — COMPLETE / POSITIVE
- v4.1 UART is 9600 8E1; one character = 1.145833 ms.
- nominal 3.5-char RTU gap = 4.010417 ms.
- debug callback idle timeout = 5 ms = 4.364 character times.
- after an 8-byte prefix, a contiguous 9/10-byte frame finishes 1.146/2.292 ms later, before 5 ms idle.
- therefore PROTO63/67 split-prefix callback is physically unlikely for normal contiguous short RTU frames, though exact ESPHome/ESP-IDF callback behavior remains runtime-unproven.

## PROTO-OFFLINE-70 — COMPLETE / POSITIVE
- standalone C++17 source-faithful parser harness compiled with g++ 14.2.
- 25,031 genuine frames replayed with randomized chunks over 50 full runs: 50/50 exact.
- compiled C++ reproduces all three deliberate 042E/0442/0546 shortest-prefix ambiguities.
- confirms parser property is not a Python-model artifact; still not an ESPHome firmware compile.

## PROTO-OFFLINE-71 — COMPLETE / POSITIVE
- 19 targeted safety mutants tested against compact offline regression contract.
- 19/19 killed; mutation score 100%.
- scope is regression-specification strength, not generated-firmware source mutation.

## PROTO-OFFLINE-72 — COMPLETE / POSITIVE
- v4.1 globals audited: 342 total; 12 definite write-only/no-read globals.
- `write_pending_valid` is source-constant false; pending queue diagnostics are inert.
- `write_resume_armed` is source-constant false, making the old 04A6 resume TX branch transitively unreachable.
- `write_hot_rejoin_in_progress` and `write_hot_rejoin_sent` are source-constant false, making the historical hot-rejoin chain transitively unreachable.
- current EXP388 recovery state is separate and remains live/safety-critical.

No YAML/live/GitHub change. EXP388 remains RUNNING / PARTIAL.