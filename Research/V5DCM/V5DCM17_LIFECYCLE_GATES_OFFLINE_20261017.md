# V5DCM17 — firmware lifecycle gate reconciliation (2026-10-17)

**Status:** COMPLETE / POSITIVE for bounded offline source reconciliation (9/9 applicable source consistency checks); COMPLETE / INCONCLUSIVE for physical XTR session acceptance, owner, profile, icon, cloud Online and permission to transmit.
**Live baseline:** user-tested V5DCM2 FIX1 RX-only; TX HARD_DENY. No new YAML, build, flash, bus test, or new active response.

## Hypothesis, baseline, controlled change
**Hypothesis:** joining the already observed V5DCM16 historical challenge/configuration candidate with independent original CM930 firmware readiness gates and the GAP51–53 findings will discriminate which next implementation feature is genuinely missing, without producing another redundant RX observer.
**Baseline:** V5DCM16 seven-capture result; V5DCM15A original 2.0.18/2.1.105 profile/flag parity; Thermia_Connect_Firmware `data/cm930_readiness_gates.csv`, `data/cm930_orthogonal_state_axes.csv`, `data/cm930_state_machine_transitions.csv`, `findings/CM930_XTR_GAP23_24_PARITY_HANDOFF_20261016.md`; earlier GAP-53 offline 12/12 function audit (previous chat, no firmware flash). Physical production baseline unchanged.
**Controlled change:** static offline consistency and dependency audit of existing original-firmware-derived gates versus the captured chronological *shapes*. No replay of authenticated traffic, no TX implementation, no command mailbox, no hardware access.

## Source checks actually run
The CSV evidence tables were retrieved again from the firmware repository. Nine independently scoped checks passed:
1. Eleven uniquely named readiness gates G1..G11 present;
2. G2 approval is distinct from FC23 response generation;
3. G4 mailbox availability is not entailed by bootstrap tail;
4. G5 semantic profile selection required for full Connect/write semantics;
5. G6 complete data-packages is its own reception/publication gate;
6. G8 safe write requires sole semantic owner and fresh authoritative cache;
7. G11 approval-response authorization remains an analytical gate with official schedule predicate open;
8. orthogonal-state-axis matrix is populated;
9. state transition matrix is populated.
These are **static source checks**, NOT nine runtime/vendor compliance tests. An additional non-applicable string assertion on a handoff report failed because it searched for a phrase absent in that document; excluded from the nine valid checks, not silently counted as a protocol failure.

## Chronological evidence ladder (separate axes)
| Candidate witness | Current evidence | What it does NOT establish |
|---|---|---|
| Exact FC23 request shape | V5DCM16 164 historical request shapes, 7 paired reply shapes | unique sender, physical EOF, exclusive response slot |
| FC23 reply shape after 29–63 ms | historical text timestamps | authenticated native XTR approval |
| First qualifying FC16/config start | Oct-03 first reference start 1.833s after reply-shaped frame | firmware H2 state on local XTR; receipt callback |
| Ordered bootstrap | Oct-03 32 strict reference starts (29.262–61.461s) | ACK ownership, profile-universal 32 requirement |
| Service/mailbox readiness | firmware G4 and historical cross-model runtime patterns | local XTR serviceable mailbox |
| Version/profile discovered | firmware I axis; version-selected JSON | selected XTR SemVer/profile |
| Required package selection and receipt | firmware G6 and V5DCM14/15A | a received-shaped FC16 automatically equals application callback |
| Cloud publication/operation | firmware separate application axis G7 | XTR display icon/cloud Online |

## GAP51–53 non-duplication decision
Earlier GAP51F/G/H, GAP52 and GAP53 provided challenge shadow/parser, integration tests and V4.1↔V5 functional comparison. GAP53's offline observer confirmed the locally witnessed XTR `03E8/count14` versus historic Oct-03 `03E8/count13` variant, and identified incomplete native session linkage. **Do not build another generic FC23 observer**: that would test an already covered frame-shape criterion. No new live output establishes that those count variants are interchangeable.

## Strong conclusions
- The Oct-03 candidate is consistent with *some* firmware lifecycle ordering, but no independent source/epoch/direction witness permits promoting shape chronology to ACCEPTED or OPERATION on the XTR.
- The most useful unresolved work is engineering the *offline-only, provenance-aware transition contract* between existing V5 frame parser, profile selection, bootstrap, service availability and application readiness; then qualify G03/G04 physical EOF/exclusive response ownership separately if a live TX phase is later explicitly authorized.
- No safe native V5 transmit or semantic write is unlocked by this reconciliation; TX remains HARD_DENY.
- 43 flag ranges describe capabilities, not a mandatory 43-of-43 readiness criterion.

## Experiment outcome
**Positive criterion:** identify each observed/firmware-derived transition gate without overclaim, and name the first missing dependency; MET for static evidence mapping.
**Negative criterion:** concrete state contradiction or evidence that a frame-only event authorizes acceptance; none supported by consulted sources. A strict physical-session proof is **INCONCLUSIVE**, not negative.
**Abort:** any ungrounded profile/source/slot assumption, private security implementation disclosure, or physical TX; no abort.
**Recovery:** offline artifact can be discarded; user-flashed V5DCM2 FIX1 remains unchanged.
**Relevant frames:** slave `0x0F` FC23 canonical session challenge shape, FC16 configuration `03E8` family, FC03 service/pull families; observed `03E8/count13` historical vs `03E8/count14` local must stay separate. No new write target or payload.

## Next: V5DCM18 — PREPARED / NOT RUN
Implement a bounded, **offline-only source/API transition parity audit** linking original CM930 event gates to existing V5 Core and historical V4.1 implementation, with explicit unsupported/missing transition rows and synthetic source tests. This is engineering of a missing connection, not a new observer. No YAML / TX. Positive: uniquely identified ownership and data-cache gaps with verified source locations; negative: no actionable difference; abort if code relies on unsupported slot/epoch or exposes confidential emulation logic; recovery no live change.
