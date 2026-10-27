> **Current-status refinement — ATEC-COLDSTART-01 (2026-10-03).** PROTO-OFFLINE-23 remains correct for its six-capture regression corpus: none of those six references had non-zero W0. A later genuine ATEC + DCM03 cold-start capture adds `W0 bit0 -> 0546/count20`. Do not generalize the six-capture W0-negative result to all genuine DCM profiles.

# PROTO-OFFLINE-23 — Current reference-model capture regression

**Date:** 2026-10-03  
**Status:** **COMPLETE / POSITIVE**  
**Hypothesis:** the current fail-closed reference model introduced after PROTO-OFFLINE-19 is consistent with all available genuine Online/DCM capture invariants and does not require unsupported W0/selector behavior.  
**Controlled change:** offline regression only; no device TX, YAML change, reboot or setting write.

## Corpus

Six genuine reference captures:
- four older Online/DCM captures from 2026-09-24/25;
- two genuine Eco5 + Thermia Online captures from 2026-09-26/28.

All parsed capture frames used by the regression had valid Modbus CRC.

## Results

- **6/6** successful genuine Eco5 bootstraps detected.
- Each contains the exact same **32-page** configuration spine in exact order from `03E8/count14` through `06F4/count19`.
- First `0708` poll occurs only after terminal `06F4` ACK in all six; observed post-terminal gaps are 1.361..4.213 s.
- **7** `FFFF/867F` refresh windows were detected; all seven contain exactly the expected **26-page** set in exact ascending page-index order.
- **4** fully bracketed Eco5 desired transactions were detected; each changes exactly one word and the following controller FC16 page is exactly equal to the desired page image.
- Across all six genuine reference captures, answered `0708` responses contain **zero non-zero W0 observations**.
- Recurrent overlays remain context-sensitive rather than generically ACKable: `04A6` ACK ratios are 6/357 and 10/226; `085F` ratios are 4/197 and 4/122 in the two Eco5 captures.

## Strong conclusion

The current model's fail-closed choices are supported:
- autonomous 32-page bootstrap before mailbox runtime;
- separate 26-page refresh;
- only genuinely observed desired selectors should be enabled by default;
- no generic W0 behavior;
- recurrent overlays must not be ACKed merely because their page shape is known.

No mismatch requiring a protocol-model change was found.

## Tooling

Added `Research/temp/tools/proto23_capture_regression.py` and retained the exact regression output alongside this report.

## Live status

No change:
- EXP387 COMPLETE / POSITIVE
- EXP388 RUNNING / PARTIAL
