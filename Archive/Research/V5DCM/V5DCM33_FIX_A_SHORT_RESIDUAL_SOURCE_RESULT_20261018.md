# V5DCM33-FIX-A — B11D short-residual bounded deferral

**2026-10-18. Experiment status: COMPLETE / POSITIVE for OFFLINE source+host+static validation ONLY. Live-device status: PREPARED / NOT RUN.** No firmware compilation, flashing, physical bus activity or TX.

## Hypothesis and baseline

After the USER-CONFIRMED controller power cycle during V5DCM32-LIVE-OBS-01, B11D latched `RAW_INCOMPLETE_AT_IDLE` at 22:02:30, before the ~12.923s callback gap and native FC23. V5DCM32 correctly denied a fresh rejoin `BadIntegrity`, ledger revoked 0/0. Previous V5DCM33 audit identified a source inconsistency: <5 RAW residual bytes fault immediately at 25ms, while a recognized pending longer fragment could defer 250ms. Hypothesis under test **in source only**: allow a bounded 1–4-byte RAW residual wait under *fresh current V5 parser pending metadata* without accepting a bad CRC or clearing the sticky fault.

Source baseline is uploaded V5DCM32 ZIP SHA256 `346966b47cad7a184936a905e40e46fa19bb6fbe8e7140eeee505cbbc1dc9374`, itself based on user-private FIX2; live V5DCM32 status remains COMPLETE / NEGATIVE for actual rejoin. Last known-good functional fallback: V5DCM23 FIX2 RX-only. G01–G06 accepted research risks remain accepted; no need to re-open.

## One controlled change

Only one B11D 50ms interval lambda behavior changes: for a 1–4 byte residual, consult pure RX-only `v5dcm33_short_residual_guard.hpp`. Wait up to 250ms iff existing V5 parser is pending and its metadata is at most 250ms old, using existing `b11d_defer_since_ms` and `b11d_defer_count`. No V5 pending => original `RAW_INCOMPLETE_AT_IDLE`; timeout => sticky `RAW_SHORT_INCOMPLETE_TIMEOUT_250MS`. A subsequent fragment must pass the **unchanged original** candidate-length, independent CRC, original portable parse, and exact V5 parity. No sticky fault clearing or successful rejoin inferred.

Changed original ZIP files: one YAML, no others. New: one pure header, two host tests, candidate README and new SHA manifest. All pre-existing original 61 archive members retained byte-for-byte except YAML. Existing `V5DCM32_SHA256_MANIFEST.json` is BASELINE-ONLY, not candidate manifest.

## Verification

- strict C++17 `-Wall -Wextra -Werror -pedantic`: NEW short-residual decision **52/52 PASS** (1–4 bytes; fresh/absent V5 pending; 250ms timeout; wrap).
- strict original portable `candidate_lengths` / `valid_crc` stream fixture: **32/32 PASS**, with segmented complete CRC, deliberately corrupt CRC, V5 mismatch and unknown slave negative controls.
- unchanged original V5DCM32 portable ledger/bridge host harness **34/34 PASS** synthetic, **34/34 PASS** unchanged 2026-10-03 original local CRC-good FC23 capture.
- unchanged V5DCM31 accepted-risk policy **61/61 PASS**.
- YAML safe-load + semantic tree: 24 top-level keys same, all other blocks same; one added include, exactly one 50ms lambda modified; **43/43** include files; all 2 substitutions defined; unchanged 117 sensor, 13 binary_sensor, 47 text_sensor, five buttons and one switch. No new RX consumer, UART TX, GPIO DE action, or HA entity.
- New full private deliverable ZIP SHA256 `ec26b85929a760be04b03031b02d10a432fc1765c9e699428bec51aa23cf7bd0`. Candidate YAML SHA256 `e02073a54ea22963de1671fba99fa6c426282b02364a5405ef3a049dbe4797ae`. ZIP archive integrity checked.
- NO full ESPHome config/firmware build, no flash, no XTR live test, no original 22:02 incomplete residual byte-level replay, no TX or physical epoch/owner proof.

## Negative / inconclusive boundaries

Passing the host fixture **does not prove** that the original 22:02 B11D fault was a recoverable 1–4-byte V5-pending fragment. On a 13s interruption, even an appropriately deferred 1–4-byte frame will become a sticky integrity fault at 250ms. Consequently FIX-A **is not** yet a complete remedy for the observed live restart/rejoin failure and must not be advertised as such.

Explicit bad CRC, unknown/orphaned prefix, expired pending, or fault latch cannot be promoted to clean integrity, session rejoin, C2, native owner, physical controller epoch, ACK, Online or TX.

## Abort / recovery and next

No physical changes were made. If separately user-initiated live testing is prepared later, preserve fallback V5DCM23 FIX2, keep software TX HARD_DENY and DE LOW; abort on missing telemetry, CRC/parser regression, any TX/DE, power control surprises or HA regression.

NEXT **V5DCM33-FIX-B POST-GAP RX INTEGRITY QUALIFICATION — PREPARED / NOT RUN (OFFLINE FIRST)**: inspect existing original first fault metadata and design explicit clean post-gap evidence and strict bounded reset/requalification policy without silent latch clear. Do not request a repeat controller restart until source audit is done. No publication of private 0x0F/0x0708 implementations.
