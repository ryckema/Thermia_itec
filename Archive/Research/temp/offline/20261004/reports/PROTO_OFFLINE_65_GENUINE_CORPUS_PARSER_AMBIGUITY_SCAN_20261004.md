# PROTO-OFFLINE-65 — Genuine-corpus parser ambiguity scan

**Date:** 2026-10-04  
**Status:** **COMPLETE / NEGATIVE**  
**Hypothesis:** the double-CRC-valid prefix property proven synthetically in PROTO63 may already occur in genuine Thermia/Online/DCM traffic; if so, the parser issue is bus-relevant rather than merely defensive.  
**Controlled change:** offline scan only. No YAML change, no bus TX, no compile/flash.

## Corpus

Scanned every parsed raw frame in:

- 4 legacy A5/Online captures;
- 2 modern Eco5/Online captures;
- 1 ATEC/DCM03 capture;
- 1 local passive XTR log as a separate non-genuine control.

The scan uses the **current v4.1 parser candidate rules exactly**:

- function-specific candidate lengths;
- lengths sorted shortest-first;
- CRC validated independently for every candidate prefix.

Only capture records whose **entire recorded frame has a valid Modbus CRC** are considered for ambiguity conclusions.

## Result

Across all eight files:

- full CRC-valid recorded frames: **25664**
- frames with 2+ CRC-valid parser candidate lengths: **0**
- ambiguities where shortest valid candidate is shorter than the recorded full frame: **0**
- ambiguities whose shortest prefix is one of the current semantic FC03 desired-page requests (`03E8`, `042E`, `0442`, `0546`): **0**

Across the **seven genuine Online/DCM captures only**:

- full CRC-valid frames: **25031**
- frames with 2+ CRC-valid candidate lengths: **0**
- genuine semantic-request-prefix ambiguities: **0**

Local passive XTR control:

- ambiguous frames: **0**
- semantic-request-prefix ambiguities: **0**

## Genuine ambiguity examples

none

## Genuine semantic-prefix examples

none

## Interpretation

No genuine captured frame has more than one CRC-valid candidate length under the current v4.1 parser rules. In the current corpus, PROTO63 remains a **synthetically proven defensive parser gap**, not a demonstrated genuine-bus ambiguity.

Crucially, **no genuine captured frame in the current corpus produces a shortest double-valid prefix equal to 03E8/042E/0442/0546 desired-page FC03**. So the current evidence does not show genuine traffic accidentally entering a semantic page-request shape.

The absence of a corpus hit is not proof that the condition cannot occur. CRC collisions are payload-dependent, and the available captures cover only a finite set of runtime/config values.

## Observed facts

- the scan is exhaustive over all raw frames parsed from the eight available files;
- every ambiguity requires both candidate prefixes to satisfy Modbus CRC independently;
- the seven genuine captures are distinguished from the local passive XTR control;
- no register/selector meaning is inferred from the scan.

## Strong conclusions

1. PROTO63's ambiguity remains **defensive/synthetic** with respect to the current genuine corpus.
2. There is **no current genuine semantic-prefix collision** for the four authorized desired pages.
3. Parser hardening remains appropriate in a future refactor, but this result alone does not justify modifying Write Beta v4.1 during EXP388.
4. The next useful offline parser step is still a shadow comparison of candidate disambiguation policies against this genuine corpus plus PROTO63 adversarial cases.

## Limitations

- captures are finite and do not cover every possible register payload;
- line-oriented raw captures preserve recorded frame boundaries, while the live UART parser sees an arbitrary byte stream;
- a no-hit result cannot prove collision impossibility;
- this is not ESPHome binary execution.

## Live status

Unchanged: EXP387 COMPLETE / POSITIVE; EXP388 RUNNING / PARTIAL; EXP383 PREPARED / NOT RUN.