# R6-P74W–P74AI reconciliation — 2026-10-12

**Purpose:** catch the three canonical Research files up with later user-supplied live P74W and P74AB results and the completed offline P74X–P74AI research. This is **documentation only**; source/firmware files are not changed and no ESPHome build or bus action is implied.

## Current device
User-supplied local XTR M log `Pasted text(20261012-095002).txt` verifies R6-P74AB running RX-only for 11:46:13–11:49:33: 823→1101 event progression, no FC23/32-page native session, no new parser gaps or software TX. P74AB remains the installed baseline. P74W was previously live-positive; P74X and P74Y–AA components were validated offline before P74AB integration.

## Experiment evidence matrix

| ID | Current status | Strongest applicable evidence | Boundary |
|---|---|---|---|
| P74W | COMPLETE / POSITIVE — local bounded RX only | user log event 78→342, stable RX | no native bootstrap/live TX |
| P74X | COMPLETE / POSITIVE — offline model | 127/127 post-prefix regression | no separate live flash |
| P74Y | COMPLETE / POSITIVE — offline replay | 4488 historical metadata, seven deduplicated candidate episodes | Eco5/ATEC cross-model |
| P74Z | COMPLETE / INCONCLUSIVE — controller cancellation | repeated first-page capture classification | EXP388 cancellation branches unrun |
| P74AA | COMPLETE / POSITIVE — offline | 1341/1341 sanitizer assertions | no hardware |
| P74AB | COMPLETE / POSITIVE — local bounded RX only | user log event 823→1101, 21 snapshots | dump button, live bootstrap and DE electrical not tested |
| P74AC | COMPLETE / POSITIVE — offline source audit | V4.1 known 58 TX *source sites*, six families | not 58 proven wire sends |
| P74AD | COMPLETE / POSITIVE — offline source audit | 38/38 checks on P74AB source | not ESPHome build or DE proof |
| P74AE | COMPLETE / NEGATIVE — active TX readiness | 12-gate review, only normal RX met | NO-GO; no physical negative TX test |
| P74AF | COMPLETE / POSITIVE — offline adapter | metadata → owner candidate, always deny | not ESP running |
| P74AG | COMPLETE / POSITIVE — offline ledger | sticky HOLD and deny | not device runtime |
| P74AH | COMPLETE / POSITIVE — offline regression | 956305 sanitizer assertions | not genuine native TX |
| P74AI | COMPLETE / POSITIVE — bounded offline original-module parity | original Python + C++ 4488/4488 owner agreement | default unqualified only |
| P74AJ | COMPLETE / INCONCLUSIVE — epoch search | A80E changes without independent reset marker | no unique epoch discovered |
| P74AK | COMPLETE / POSITIVE — offline deny review | 436720 sanitizer assertions, 34 static checks | active NO-GO |
| EXP388 | RUNNING / PARTIAL — historical active test | two restart-related positives in recorded historical scope | two cancellation branches not run |

### Specific P74AI correction
The genuine captured ADUs are original **Eco5/ATEC cross-model**, not a newly attached DCM on the XTR M. 4394 genuine raw ADUs were CRC-checked and decoded with the original SHA-pinned Python Core; 94 collaborator entries remain shape-only. The raw-enriched 164 canonical FC23 request shapes classify as `POLICY_OPEN`, *not* physical authority, and 334 former OTHER shapes decode as FC03 responses. The C++ projector was unchanged and sends nothing. Original public Python Git blob: `671af7b27d2fbc2df988f4f080d13c7f06e6c496`. This closes P74AI's original Python-import limitation, not the hardware/session authorization problem.

### Remaining native Online blockers
1. Independent same-controller epoch/owner across ESP OTA; P74AJ did not find one.
2. Explicit exclusive physical response-slot and frame-end proof.
3. DE fail-low on power/reset/brownout and UART FIFO/drain safety on the actual output adapter.
4. Controlled native context for FC23, 085F and retained/recovery, and EXP388 cancellation cases.

**Current rule:** RX-only, TX HARD DENY; preserve unrelated Home Assistant production configuration and the room sensor. Do not propose new genuine DCM captures; user has no DCM attached.

## Sources
- Local user log analyses: `R6_P74W_LIVE_RESULT_20261012.md`, `R6_P74AB_LIVE_RESULT_20261012.md`.
- Offline project outputs: `R6_P74X_RESULT.md`, `R6_P74Y_TO_P74AB_RESULT_20261012.md`, `R6_P74AC_TO_P74AE_RESULT.md`, `R6_P74AF_TO_P74AH_RESULT.md`, `R6_P74AI_FINAL_RESULT.md`.
- Public architecture/evidence: [Firmware reference core](https://github.com/ryckema/Thermia_Connect_Firmware/blob/main/tools/xtr_dcm_reference_core.py), [reference-core hardening backlog](https://github.com/ryckema/Thermia_Connect_Firmware/blob/main/data/xtr_reference_core_hardening_backlog.csv), [native epoch continuity audit](https://github.com/ryckema/Thermia_Connect_Firmware/blob/main/findings/NATIVE_SESSION_EPOCH_CONTINUITY_AUDIT_20261010.md).

**Publication scope:** text-only evidence and status; no complete YAML, private cryptographic transform, native responder frames, 0x0708 command tooling or raw security implementation included.
