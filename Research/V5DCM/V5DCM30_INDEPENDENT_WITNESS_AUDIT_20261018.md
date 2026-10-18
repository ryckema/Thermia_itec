# V5DCM30-INDEPENDENT-WITNESS-AUDIT-01 — previous restart and ownership evidence versus CURRENT V5 rejoin

**Experiment status: COMPLETE / INCONCLUSIVE for the hypothesis that the AVAILABLE evidence provides a sufficiently independent CURRENT controller epoch/continuity witness.** The **offline documentary/source audit itself is complete**, with an important bounded historical POSITIVE. Date: 2026-10-18. This experiment does not supersede prior EXP386/387/388 or G01/G02 result statuses.

## Scope and test contract

**Hypothesis:** existing local XTR logs, dated intervention video, tested v4.1 recovery, software source or hardware inventory might furnish an independent physical controller-session/continuity witness suitable for *today's V5DCM29* read-only requalification, without bus TX or restarting the device.

**Known-good:** currently user-flashed V5DCM23 FIX2 RX-only, short ~2m25 live observation of V5DCM23 ledger `1/33` (only exact `03E8/14` shape), B11C/B11D stable and software TX HARD_DENY. The exact running image/OTA slot not authenticated; earlier R6 Stage D remains D=4, first local fault reason unknown. **Do not claim the private ZIP is byte-identically flashed**. Previous V5DCM29 typed evidence contract COMPLETE/POSITIVE **strictly offline**, and cannot issue a physical proof at runtime.

**One controlled change:** review **existing** independently sourced historical records and available original local capture files, create a source-typed evidence decision matrix. No new algorithm, parser, YAML, firmware, emulator, serial instrumentation, physical TX, ESP reboot or controller restart. Keep evidence classes distinct: physical power intervention versus physical rail verification, current versus historical, accepted installation-scoped research risk versus proven physical responder/slot.

**Primary past results, already checked for duplication:**
- [G01 controller epoch synthesis](../G01_CONTROLLER_EPOCH_20261013_SYNTHESIS.md): original host projector caused seven false-positive physical epochs (G01-04 NEGATIVE); gaps, FC23, A80E/A80F and 32/32 are not unique physical-boot evidence.
- [G01-07R/G01-08/G01-09](../G01_07R_08_09_CONTROLLER_RESTART_20261014.md): G01-09 **COMPLETE/POSITIVE** for VIDEO/INTERVENTION_ANCHORED actual user-operated switch/display restart, but direct controller rail measurement **INCONCLUSIVE**; previous synthetic/host classifications not physical boot IDs. Do NOT reclassify this as a failed experiment.
- [G02-09–11B](../G02_09_TO_11B_CONDITIONAL_CLOSURE_20261014.md): user **accepted G02 COMPLETE/POSITIVE (CONDITIONAL)** for unchanged single known external port with no separate installed DCM, historical owned work and bounded 24 unanswered FC23. This decision stands for its exact installed scope; electrically exclusive responding and new-epoch entitlement remain unproven, not grounds to revoke the original decision retrospectively.
- [G04 response-slot audit](../G04_RESPONSE_SLOT_G04_01_TO_G04_07_20261014.md): physical UART EOF, exact exclusive reply slot and DE drain/fail-low remain technically unverified. G04-07 instrumentation user-deferred; do not silently revive as already performed.
- [Write Beta v4.1](../../Write%20(Beta)/README.md): EXP386 and EXP387 local positive for bounded guarded native recovery and semantic re-arm; EXP388 partially positive for two consecutive restarts, but other branches untested. Historical functional proof, not a current V5 TX lease.
- [V5DCM29](V5DCM29_SESSION_PROVENANCE_CONTRACT_OFFLINE_20261018.md): host test permits synthetic `OfflineFixtureIssuer` only. **No independent physical issuer exists in production**, and the current `gap24A/B` candidate does not prove owner/epoch/slot.

## Observed original evidence in accessible files

1. The following source files are locally readable and checksums match the canonical historical findings:
   - `thermia_capture_20261003_165355.log`: SHA256 `14918065297264473e2357822a8694d184e7821b8c2a3b1cb316039678a708a1`, **2687 recorded hex frames**, two native `0x0F FC23` requests. This file encodes RTU byte frames and relative timestamps, **not** independent physical controller supply, responder identity, UART last stop bit, or current device operation.
   - `thermia_capture_20260925_090550.log`: SHA256 `f23cd2f18764d77220409d2cf9e0caf2fc3b7c1aa1d2a1405f13c9fdbbbc0e2d`, **892 recorded hex frames**, zero native `0x0F FC23` in that file. Contains earlier request-cycle evidence, NOT current XTR session proof.
2. G01-09 original **4,660-line** local XTR log hash `a66541b2c8d91661863c6a315003ef26eb4ca3d8960e324479ff2a43cd8acb2e` and original 23.567s video hash `c6ca2d3e443efb367fbf8aba156b9d25769133f8717486446744120ca0b83a1f` are cited in canonical GitHub reports. **Their original bytes were not available in the current mounted files**, so this V5DCM30 audit verified the *dated report*, not the raw video/log replay. No false claim of re-executing those earlier experiments.
3. G01-09 **reported observations**: one user-operated display-off/on intervention; `R6-P24 CALLBACK_GAP=11944 ms` at 15:41:15.736; first CRC-valid traffic return 15:41:15.749; cold status A80E=0000 / A80F=0005 by 15:41:16.460; 24 FC23 requests in the following bounded window; zero matching peer response shapes reported. Existing ESP parser health/software TX=0 remained stable. This is an intervention-anchored **one event**, not 24 fresh physical epochs and not a continuously valid reboot token.
4. Current V5DCM23 FIX2 short user-live result is different, ~2m25 in 2026-10-18 console; **no observed FC23** in that interval. It demonstrates one passive package and healthy source observer, **not a contemporaneous physical controller restart witness**, no physical owner, slot or epoch-proof provider.
5. The proposed V5DCM29 `IndependentProof` API explicitly lacks a runtime issuer. Its fixture-constructed proof is a **test input**. We must not reissue a `current_xtr` proof from G01-09 simply by relabeling the old timestamps.

## Evidence decision matrix

| Evidence class | Historically supported? | Currently bound to deployed FIX2? | Allowed inference | Prohibited promotion |
|---|---|---|---|---|
| G01-09 video + switch + continuous RX | **Yes, user-intervention anchored** | **No** | An externally documented restart of the *recorded* device episode | Current epoch, electrical rail proof, future autonomous owner |
| G02 installation topology + no installed DCM | **Yes, user-approved conditional scope** | Installation continuity not freshly rechecked | Conditional risk acceptance if installed topology remains identical | Physical exclusivity, protocol lease, fresh reply slot |
| EXP386/387 bounded native recovery | **Yes, locally positive in old build** | **No** | Reusable historical state/recovery design and rollback | Automatic present V5 controller acceptance or unqualified TX |
| Historical `0x0F FC23` / FC16 / `085F` / `A80E/A80F` | **Yes, source bytes/timing** | Historical or current passive only | Session-phase candidate, page shape, chronology | Physical controller power ID, local sender, exclusive slot |
| Current FIX2 parser/portable ledger and HARD_DENY | **Yes, short live snapshot** | **Yes, limited interval** | Parser consistency and RX-only stable within snapshot | Full native C2, owner, boot, electrical TX zero |
| G04 host UART debug timestamps | **Yes, software timestamps** | **No independent line edge** | Code-path timing estimate | Physical EOF or reply slot |
| V5DCM29 test-only issuer | **Yes, C++ host fixture** | **No production issuer** | Strict contract acceptance/denial under synthetic evidence | Real independent current physical witness |

This matches the **10-row locally produced `V5DCM30_WITNESS_SOURCE_MATRIX_20261018.csv`** (SHA256 `ec2e882c3e8369efb337c80c9fcee773641d94f9a6673ac06f1d0c03db146200`), provided as a conversation artifact; raw/private captures, video and 0x0F implementations were **not committed**.

## Conclusion by provenance

**OBSERVED FACTS:** G01-09 was already a positive *historical* video-anchored user intervention; G02-11B conditional owner-topology acceptance already exists. Current FIX2 short log lacks a same-window independent restart/continuity witness and has no FC23. Recorded 20261003 frames carry no separate physical power/owner channel. V5DCM29 has no production independent proof issuer.

**STRONG CONCLUSIONS:** (a) We should NOT endlessly re-run G01/G02 or demand a separate DCM module; historical user-approved installation-scoped risk decisions remain recognized. (b) A video of a previous reboot cannot be reused as an authenticated present-controller epoch. (c) Passive software counter, long RX soak, host UART callback timing or continued 1/33 cannot alone close missing current physical witness or reply-slot proof. (d) Treat epoch, bounded protocol-assigned work, electrical exclusivity, and response slot as separate gates.

**HYPOTHESIS:** an explicitly bounded, **manual intervention-anchored** future research context using previous V4.1 positive guards could be meaningful for controlled native emulation testing on the same unchanged installation, without pretending universal automatic power-epoch proof. Such a design would be **separate from a strong autonomous physical-issuer claim**, and must still have exact private response policy, permitted controller slot, timing/retries, abort and recovery before any physical TX.

**UNKNOWNS:** current physical controller generation, retained continuity on current FIX2, independent physical sender/slot, original R6-P30D first D=4 trigger, exact as-flashed source/OTA slot, actual online application acceptance. G03/G04/G05/G06 residual uncertainty remains an accepted research risk where previously authorized, not a claim of completed technical measurement.

### Experiment result

**V5DCM30-INDEPENDENT-WITNESS-AUDIT-01: COMPLETE / INCONCLUSIVE.** The audit found bounded historical external context but **no present-session independently grounded issuer/attestation** usable by current V5DCM29. Not a negative observation of protocol capability, nor a failed G01-09 or revoked G02 conditional decision. No live change, controller power cycling, bus TX, compilation, ESPHome flash or user action.

### Next controlled step: V5DCM31-MANUAL-SESSION-SCOPE-01 — PREPARED / NOT RUN

**Hypothesis:** source-only design can distinguish (1) user-initiated, bounded manual intervention context for a controlled research experiment from (2) fully autonomous verified physical epoch/slot, while respecting standing permission, G01-09/G02 conditional acceptance, and mandatory fail-closed output. This should **not require new hardware, a DCM module, room-sensor disconnection or repetition of old G01/G02 experiments.**

**Known-good** unchanged live V5DCM23 FIX2 RX-only and historical v4.1 recovery. **One controlled change:** write an offline finite evidence/expiry policy for manual context classification, with no generated response payload and no TX in the audit. Confirm when prior experiment-specific scope may be reused vs when new owner/epoch evidence is obligatory; preserve zero-output default and old R6 hold.

**Target fields:** native `0x0F` session metadata, current context quality, observer continuity, independent manual/event confirmation, owner/slot provenance, and RX ledger reset candidate (not hardware registers or writes). **Positive:** historical/manual/automatic categories never conflated, no source alone grants TX, explicit bounded future live criteria. **Negative:** stale video or RX shape promoted to autonomous current proof; old accepted G02 risk silently reopened; changed production YAML. **Inconclusive:** missing reliable same-window source context. **Abort/recovery:** offline only and preserve known-good RX-only. **Required evidence for any eventual real session operation:** present controller and installation context, exact known response slot/payload and electrical risk controls, current RX health, explicit bounded retries and rollback. Do not ask for compiler output unless diagnostics require it.

This V5DCM30 step **does not authorize a live response** or identify a new safe TX frame. No private 0x0F emulator, challenge security algorithms or 0x0708 mailbox tooling are included.
