# V5DCM58 — Can the controller poll native 0708 when preceding FC16 is not visibly ACKed? (2026-10-19)

**ID:** V5DCM58-FC16-ACK-0708-PROGRESSION-OFFLINE-01. **Status: COMPLETE / POSITIVE (archived CRC/source-level negative-control audit ONLY)**. The universal model "every FC16 must first have a matching ACK before the controller may poll native 0708" is **DISPROVEN as a universal description of archived observable traffic**. Whether fresh native XTR session approval depends on some ACK, response, prior epoch or another master-side condition is **OPEN / UNKNOWN**. This finding does not authorize native TX. No user hardware, ESPHome YAML, firmware, HA entities, controller power state or electrical wiring changed.

## One controlled investigation; baseline, precedent and abort

**Hypothesis:** Original Connect 2.0.18/2.1.105 implements FC16 ACK separately from H2/info request and controller's native status polling (V56/V57); historical local XTR and collaborator captures may demonstrate controller status polls while no matching FC16 ACK was captured. Distinguish a UNIVERSAL FC16-ACK prerequisite from an unknown COLD-SESSION-specific gate.

**Verified live baseline:** user-flashed **V49 RX-only HARD_DENY**, clean 285-frame/30.532s post-controller-manual-OFF/ON cohort with zero new B11C/B11D errors, UART TX0; native FC16 04A6 and 085F seen, native 0708 polls0, FC16 ACK-shaped replies0, no 03E8/count14 or 0864/count4. Earlier local V23 RX-only received 03E8 under a different epoch. V47 native one-shot remains COMPLETE / INCONCLUSIVE, physical TX0. Proven historic Write Beta v4.1 experiments are supporting **local** context, not the firmware source of truth.

**Relevant already-run experiments:** V5DCM25 independently confirmed Sep25 09:05 W3bit0=1 request status → 03E8 / 31 setting groups (old geometry); V55 valid 25,031 CRC frames / 367 status-poll/reply pairs; V57 corrected prior 8-byte ACK-shape omission, 2,500 FC16 request forms and 1,365 ACK shapes. No repetition of those physical experiments.

**Single controlled change:** run offline *temporal adversarial case selection* using the corrected FC16 ACK classifier on EXACT SEVEN pre-existing archive files. For each FC16 request, detect whether its next native 0708/count6 status poll, and if present its <=500ms status reply, occur **without a same-start/count FC16 ACK** (also choose the stronger condition with NO native FC16 ACK AT ALL between request and poll); exclude intervals with an observed native FC23 reply/request. Independently split local Sep25 09:05 at the first actual status reply and count all requests, ACKs, polls and settings pages. This is host-replay metadata only; no native RTU response generator or 0708 command mailbox implementation published. **Targets:** passive slave0x0F FC16 request/ACK shapes and native FC03 0708/count6 poll/reply envelope; no TX frame/payload. **Expected effect:** none. Positive = at least one CRC-valid status poll/readback despite unmatched preceding FC16 and reproducible strict local timeline. Negative = all such sequences show mandatory matching ACK or CRC errors. Inconclusive = physical electrical delivery, controller code/owner and fresh-session semantics. Stop on source/CRC conflicts; no hardware recovery needed.

## Exact evidence and reproducibility

Original raw archives (25,031/25,031 CRC-valid, unchanged): four old XTR Sep24/Sep25, one ATEC Oct03 genuine/collaborator, two Eco5 Sep26/Sep28 collaborator. Exact local XTR Sep25 09:05 file **thermia_capture_20260925_090550.log**, SHA256 **f23cd2f18764d77220409d2cf9e0caf2fc3b7c1aa1d2a1405f13c9fdbbbc0e2d**; 892 CRC-good frames and 0 native FC23 within its 0.490–106.841 s window. Independent offline metadata scripts and JSON kept PRIVATE, SHA256:
- v58_temporal_audit.py 316fdea42c8e22399a6c53c04fc6e05f7d63a83d81db8eb24bd582b890c68e1f
- v58_temporal_audit.json a77d86ac0ee701cd5689f6f23f5663fca545101e66f67108b1fb4c4cbbf0b143
- v58_master_progression.py aacef66cefbfaf4f86a5c0d5f181dbe01ddc192576b72e5766e393c5200552c7
- v58_progression_metadata.json 8eae7040c07363788e58da26a450e04c118ec4a8162ad19301a082f34a54b2ec

Original Connect source (already VERIFIED V56/V57): 2.0.18 and 2.1.105 **shipped modbus_tk** make ordinary FC16 address/count ACK independently from async original CM930 H2/info-request events; actual 0708 polling is **controller-master initiated**. Firmware has no basis to assert a universal master-side ACK->next-poll rule because it implements the slave; software internal ACCEPTED is not Online or controller semantic approval. No protected transform/reply frame or mailbox data is disclosed.

## OBSERVED LOCAL XTR: Sep25 09:05

The independent timeline and previous V25 outcome must not be merged into one assumed cause:

| Interval / event | Archive fact |
|---|---|
| First native 0708/count6 poll | **t=0.987s** |
| Repeated status polls before first FC16 ACK | **16 polls**, zero visible ACKs in capture at that point |
| First actual FC16 ACK | **t=66.860s**, for native 0870/count17 |
| All native 0708 polls through first successful reply | **17 polls**, first t0.987, last t68.210, **median 4,202.5ms** between polls |
| FC16 before first status reply | **32 0870/count17 request forms; 1 ACK shape total** |
| First captured native six-word status reply | **t=68.235s** to poll t68.210; previously V25 documented setting-group W3.bit0=1 |
| First native FC16 03E8 settings page | **t=68.304s**, **69ms** after status reply (logged host time, not wire EOF) |
| All native FC16 AFTER first status reply | **41 request forms, 41 ACK shapes** in captured remainder |
| Controller settings export | **31 distinct page group starts** 03E8..06F1, controller-pushed old 13/21-count ABI, not necessarily 32/32 boot or full firmware profile readiness |
| Additional status polls after export | **t=101.901s and 106.095s**, both paired with captured status replies |

**Therefore (local archive fact):** the master was visibly issuing native 0708 polls repeatedly even though not every native FC16 request was ACKed, and indeed issued sixteen 0708 polls BEFORE the first visible FC16 ACK in this file. First observed SUCCESSFUL status REPLY was followed 69ms later by the first native 03E8 and 31-page export. This locally shows the distinct importance of *status response delivery* in this **historical, already experimental session**, without proving it exclusively caused the page export or that a cold, new DCM session behaves identically. This capture starts with other bus traffic and does NOT establish that the original controller lacked an earlier accepted native session or different peer/owner.

## OBSERVED cross-model negative controls: status survives a recent unmatched FC16

In genuine/collaborator Eco5 CRC captures, four nonduplicated intervals contain an FC16 request without ANY native FC16 ACK (matching or unrelated) before the next 0708/count6 poll **and** six-word status response, with **no intervening FC23 envelope**:

| Source | Unmatched native FC16 request | Next status poll | Status reply | Host gap |
|---|---|---|---|---|
| Eco5 Sep26 | 080C/count18 at22.988s | 24.380s | 24.380s | 1.392s |
| Eco5 Sep26 | 0820/count18 at27.218s | 28.645s | 28.645s | 1.427s |
| Eco5 Sep26 | 0834/count18 at1058.086s | 1059.352s | 1059.383s | 1.266s |
| Eco5 Sep28 | 080C/count18 at671.897s | 673.272s | 673.318s | 1.375s |

**Strongest warranted conclusion:** an immediately preceding ACK for EVERY FC16 is **NOT an observed necessary prerequisite** for a subsequent 0708 poll/status reply in these archived ongoing service conditions. A true physical ACK might not have appeared in archived bytes due logging/other source, and this is **not a proof that all native acknowledgments can be omitted** or that a new unapproved V49 cold session would progress.

## Evidence tiers, difference versus V49, safe next step

**PROVEN locally observed envelope chronology** in old controlled XTR: 32 0870 requests/one ACK with 17 status polls, then successful status reply and 31-page config burst, plus ongoing 0708 polls. **PROVEN genuine/collaborator metadata:** four status reply sequences occur after unmatched recent FC16, no FC23 in between. **PROVEN firmware-derived:** FC16 ACK, software H2 and internal request bit vs controller-initiated status poll are distinct. **STRONGLY SUPPORTED:** controller master can retry status service in at least some already-active situations despite missing prior ACK frames. **DISPROVEN / SUPERSEDED:** proposed *universal* FC16 ACK-before-any-0708-poll rule as explanation of all observed sessions. **HYPOTHESIS:** fresh-start native approval, peer presence, ACK policy, or another controller-side qualification governs V49's absence of 0708 polls; there is no controller-master firmware source here to choose among these.

**Current installed V49 is not comparable as an already-qualified service session:** after manual OFF/ON, native FC23 attempts were unanswered, native 0708 poll0 and local FC16 ACK0, though 04A6/085F FC16 kept arriving. No real current controller owner/epoch, 0867, electrical EOF/exclusive response slot or online acceptance is verified. The fact that an older **different** experimental session tolerated missing ACKs does NOT authorize V49 ACK/TX, unsolicited 0708 response, dangerous register writes, power-cycle or session latch bypass.

**NEXT:** All existing captures now distinguish the specific missing edge: present controller **does not visibly initiate native 0708 polling in V49**. Its internal decision why cannot be proved from a slave's Python source or a second replay of the same logs. Do not propose a repeat of historical V25 31-group response experiment. Before any future physical active experiment, separately require evidence/controlled mitigation for real bus sender/owner, response slot, original firmware-mode provenance, physical safety and bounded fail-closed TX. A purely passive natural-state capture using the existing V49 receive path is an optional FUTURE experiment only if there is a new naturally occurring state change; it is NOT currently performed, prepared for flashing, or known to solve the missing master gate. Preserve exact V49 production YAML, existing diagnostics and sticky B11D/P5.
