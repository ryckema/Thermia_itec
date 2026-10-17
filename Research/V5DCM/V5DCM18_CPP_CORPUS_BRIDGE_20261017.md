# V5DCM18 — 7-capture portable C++ Core parser/decision replay (2026-10-17)

**Status:** V5DCM18 original roadmap **RUNNING / PARTIAL**. Scope: new integrated corpus traversal against the **user ZIP** portable Core (not GitHub main), offline only. **G01–G06 accepted residual-risk decisions are NOT reopened**.

## Baseline, hypothesis, change
Baseline: prior 17/17 host stateful Core tests; 25,031/25,031 CRC-valid textual captures; user V5DCM2 RX-only observer; native production V5DCM2 FIX1 TX HARD_DENY. Hypothesis: seven genuine/collaborator captures can be parsed with current user-ZIP C++ Core to expose actual gaps between independent FC23 observation, FC16 decision logic and native session state.

Controlled change: single standalone C++17 traversal executable, no Core modification, no private native approval data, no UART/ESPHome/production change. The runner calls original ZIP `decode_frame()` and `Core.fc16_decision()` in a passive traversal without `commit_fc16()` and without any wire records. Tested all seven captures.

## Actually executed result
- Compiler: `g++ -std=c++17 -Wall -Wextra -pedantic`; executable exit 0 on seven-file traversal.
- **25,031 frames traversed across seven captures.**
- **2,500** raw decoded slave-0x0F FC16 requests, **1,365** FC16 ACKs; in non-committing `fresh()` decision-probe mode, **216** would be `authorized` candidates and **2,284** denied. Those 216 are hypothetical ownership outputs **NOT bus transmission approvals**, not observed device ACKs; the runner intentionally does not track epochs/physical provenance.
- **171** slave-0x0F FC23 frame appearances by function-byte classifier (requests + responses; *not* 171 challenges). Previous independent capture-only replay counted **164 challenge request shapes and 7 paired response shapes**. No claim about authentication.
- **5,115** frames decoded as Unknown excluding FC23 by the ZIP parser; this aggregate includes other frame kinds/slaves and is **not automatically an error count**, since portable `Kind` only supports FC03 and FC16; the source lacks native FC23 classification. Separate V5DCM2 RX-only challenge observer covers that purpose.
- The runner does not commit state; therefore this is a **parser/decision coverage audit, not a full stateful end-to-end native replay**.

## Evidence classification
**Observed / executed:** counts above, 7/7 files opened, C++ compile/run. **Strongly supported:** FC23 belongs to separate existing observer; avoid adding redundant FC23 parser into Core without reason. **Hypothesis:** integrate observer evidence with owner/epoch-safe state transitions. **Open:** per-frame provenance and owner on a local XTR session; complete stateful original Python reference Core/corpus tests; comparison to current GitHub HEAD; full end-to-end negative-state replay.

## Criteria and disposition
Positive bounded parser audit MET; full original-roadmap V5DCM18 condition NOT MET. No negative regression demonstrated by broad Unknown counter. Abort no active TX or production modifications; recovery none. Next verify original Python reference tests with seven fixtures, then integrate already-existing V5DCM2 observer and ZIP Core through an offline fault replay without creating a new protocol model.

No G01–G06 revalidation requested or necessary.
