> **S62 FINAL DECISION — 2026-10-21 (overrides older open/prerequisite wording below for this unchanged XTR installation).** On user's explicit instruction, **G01 controller epoch, G02 conditional external native peer/owner and G04 native response-slot risk are COMPLETE / POSITIVE — USER-ACCEPTED OPERATIONAL RISK CLOSURE**. This is a documented risk acceptance, **not** false claims of independently probed controller rail, universal absent peer or measured FC23 acceptance window. New user TTL waveform recordings showed 2,280/2,280 9600-8E1 CRC-valid frames in 267.387s with 2,280 matching GPIO1-like marker edges (EOF-to-marker median 19.268ms) and 373 native 0x0F FC16 requests each followed by at least 102.311ms of observed no-next-frame time. Earlier user-performed G01-09 intervention/video, preaccepted conditional G02 installation inventory and bounded XTR V4.1 success retained. **Do not routinely reopen these THREE gates, request inaccessible GPIO18, or insist on new power/peer/slot probes in future work;** reconsider only changed hardware/wiring/profile, observed competing 0x0F output, a concrete contradicting fault or explicit user reopening. Historical uncertainty stays archived and is not converted to physical `true` booleans or auto-arm. Separate UART/DE safe drain/reset and full ESPHome embedded build remain independent safety work. Reference: `Research/V5DCM/V5_NATIVE_S62_TIMED_TTL_RISK_CLOSEOUT_20261021.md`. No new flash/TX.

---

# G02 native Online/DCM owner — scoped conditional closure (2026-10-14)

**Decision explicitly approved by the user in conversation:** `G02 COMPLETE / POSITIVE (CONDITIONAL)` **for the documented, unchanged iTec XTR M installation only**. This is an engineering/research acceptance of physical-installation evidence + bounded historical native protocol work, **not** independent electrical proof of exclusive response-slot ownership, any new deployment, or permission to transmit. **NATIVE 0x0F TX = HARD DENY.**

This additive note records G02-09, G02-10, G02-11A and G02-11B. Their previous LOCAL-only study outputs were discussed with the user. **This reconciliation reviews the recorded outcomes and supporting documentary sources; it does not assert that raw-source replay, software unit tests, electrical measurements or ESPHome builds were rerun during this GitHub update.** Keep all older experiment statuses as originally reported, including EXP425 NEGATIVE and EXP419/423 INCONCLUSIVE. Private native emulation payloads and recovered challenge algorithms intentionally omitted.

## Defined acceptance scope and invalidation

The owner is **only the configured intended external slave `0x0F` endpoint** on an unchanged installation where:
- the physical hub card has two visibly identified RJ45 connectors, functionally corresponding to ATEC `122 Display` and `123 Ext.` (cross-model ATEC diagram + user's local XTR PCB photographs; board equivalence electrically unverified);
- `122` connects to the installed display; `123` is the known external DCM/Online access point used for ESP32 sniffer/emulator access (some photographs were taken while `123` appeared physically unoccupied; do not claim that photo shows the ESP plugged in);
- user confirms **no separate Thermia Online/Connect/DCM module**, nor an identified additional external DCM port; the physical installation normally permits one directly plugged-in external accessory on the known RJ45, but this is **not a proof against splitter wiring, internal responders or every possible transceiver**;
- one user-video-anchored XTR cold-start RX-only observation G01-09 shows **24 repeated FC23 requests and zero reported matching native peer response shapes in that finite log window**, ESP software TX 0; no claim of no other responder at all future times;
- earlier real local XTR native emulation experiments (including EXP355/386/S11F, EXP420 and historical confirmed page-cache writes) already demonstrated controller-assigned work and correct controller-side progression in bounded sessions, as historically documented.

**Invalidation triggers:** change to RJ45 cabling/splitter/accessories; installation or detection of any Online/DCM/competing responder; unexplained `0x0F` response shape, concurrent transmitter or peer conflict; controller reboot/new epoch not validated in the current bounded context; UART/CRC integrity loss; profile or board replacement; loss of firmware provenance or unknown session state. Any trigger -> G02 current-context status `UNKNOWN/HOLD`; native TX stays denied. G02 approval is not inherited across independent physical epochs without fresh context validation.

**Not proven:** complete copper topology/second PCB side, absence of all hidden transceivers, independent electrical physical sender IDs, unique lease token, exact UART stop-bit EOF, exclusive reply slot, physical TX/DE drain/release, DE fail-low on reset/brownout. Those are separate open safety issues.

## G02-09 — COMPLETE / POSITIVE, bounded OFFLINE classification (physical exclusivity INCONCLUSIVE)
- **Hypothesis:** capture windows distinguish request-without-response, response-present-sender-unknown and controller-work-progress candidate without fabricating exclusive ownership.
- **Baseline:** G02-01..08, genuine Eco5/ATEC DCM captures, local XTR G01-09, firmware internal CM930 state axes.
- **Controlled change:** offline replay and finite request/response window classification only; no new heat-pump TX.
- **Reported local-only result:** 25,031 CRC-valid cross-model frames examined, eight FC23 windows: five with response shape and later matching `03E8` ACK within bounded lookahead, two with FC23 response but no matching first-page ACK within 35s, one with repeated unanswered FC23; offline report states 193/193 checks PASS. Additionally **separate local XTR** 24 unanswered FC23 (not added as a ninth genuine cross-model source file). Classifications are `ASSIGNED_WORK_CANDIDATE`, `RESPONSE_SHAPE_PRESENT_SENDER_UNKNOWN` or `REQUEST_WITHOUT_RESPONSE_OBSERVED`, never physical sender certainty.
- **Negative/abort:** response shape or later ACK interpreted as exclusive physical owner; cross-model source treated as XTR; original unavailable data fabricated. None of these claims authorized.
- **Recovery:** leave as offline-only, reclassify source-specific windows if raw replay fails. Raw verification bundle was LOCAL and is not asserted reproduced/published by this GitHub commit.

## G02-10 — COMPLETE / POSITIVE documentation/topology inventory; actual exclusivity INCONCLUSIVE
- **Hypothesis:** the available local PCB photographs, user installation details and Danfoss/ATEC documentation can identify the *known* external native connector and potential peer components.
- **Baseline:** historical XTR RS485 pinout and native bus read-only observations; provided 13-page ATEC electrical schematic `DOC088786453804_IR(1).pdf`; three user PCB close-ups.
- **Controlled change:** documentary/photo review only; no wires moved, disconnects or continuity test.
- **Observed:** ATEC schematic p7 labels `Modbus RJ-45 Display` and `Modbus RJ-45 Ext.`; user's corresponding board visibly has marking `122` next to connected display RJ45 and `123` next to external jack. Separate sensor/outdoor connections exist in ATEC wiring reference, but exact local XTR PCB nets not traced. No Online/DCM device installed per user.
- **Positive:** bounded inventory of the two known RJ45 roles; **negative:** cannot rule out board-internal electrical paths or hidden responders.
- **Abort/recovery:** never extrapolate ATEC exact PCB copper to XTR; documentary correction only, no hardware rollback needed.

## G02-11A — COMPLETE / POSITIVE bounded historical protocolmatic work ownership
- **Hypothesis:** native controller-master requests, historically observed matched ESP replies, later controller progression and echoed settings prove assigned *per-transaction protocol work* in a local XTR session.
- **Baseline:** EXP355/386/S11F, EXP420, EXP421/422 and associated historical write controls; genuine ATEC/Eco5 native session trace; reconstructed CM930 2.0.18/2.1.105 state-machine and mailbox mapping; user-supplied Home Assistant Community thread PDF pages 20, 38–40.
- **Controlled change:** offline source/documentary reconciliation plus available historical log-fragment counting only; **no new TX test**.
- **Reported result:** archived XTR EXP355 fragment yielded 240 native runtime ACK executions and 133 mailbox answers in previously performed offline evaluation, source scope explicitly a *fragment*, not independently recaptured full experiment here. Historic locally accepted controller-driven settings writes used FC03 requested page followed by controller FC16 republish; positive only for mapped session work in that tested version, not universal ACK authorization. The local offline research report reported 14/14 checks, not rerun in this GitHub update.
- **Counterevidence:** EXP423 orphan `0662/count33` repeats with no valid owner; EXP425 one correct-looking ACK stopped retry but required subsequent `0683/count33` did not follow within 60 seconds (**COMPLETE/NEGATIVE** for that prediction). EXP419 and EXP423 intended branches INCONCLUSIVE. An ACK is not general semantic acceptance.
- **Positive/negative/abort:** per-transaction bounded protocol ownership historically established; absence of current physical exclusivity and universal lease remains OPEN; abort if stale work, orphan response, incorrect epoch, mismatched profile or speculated semantics. Recovery RX-only, no output.

## G02-11B — COMPLETE / INCONCLUSIVE for universal electrical proof; CONDITIONAL POSITIVE for installed hardware inventory
- **Hypothesis:** one known external `123` DCM jack with no DCM module and no peer reply in RX-only observation is enough to accept **installation-scoped single intended external responder**, without claiming every electrical possibility impossible.
- **Baseline:** G02-10, G02-11A, user PCB close-ups plus later full front-side overview `IMG_9907.jpeg`, ATEC schematic p7 and G01-09 24 unanswered FC23.
- **Controlled change:** passive review of larger photograph and user's explicit clarification that there is one external DCM RJ45 next to display RJ45. No direct PCB net measurement or electrical TX attribution.
- **Observed:** no identifiable separate Online/DCM on visible front of installed hub card; known display `122`, external `123` roles; user confirms no physically installed DCM. A single physical RJ45 receptacle does **not** exclude upstream splitters, internal transceivers or some unknown other responding hardware.
- **Positive:** documented single known external DCM port and no installed gateway, enough for **user-approved conditional installed-topology acceptance**. **Negative/inconclusive:** complete electrical proof of physical responder exclusivity not possible from images, capture silence and schematic alone.
- **Abort/recovery:** any discovery of shared `0x0F` responder or wiring changes invalidates conditional conclusion; revert owner assessment to UNKNOWN/HOLD and keep native TX HARD DENY. No on-device configuration changed.

## Current G02 decision and separate gates

**G02 research gate = COMPLETE / POSITIVE (CONDITIONAL)** by the user's explicit acceptance on 2026-10-14, *only* as `SINGLE_KNOWN_EXTERNAL_DCM_PORT + NO_INSTALLED_DCM + HISTORIC_NATIVE_WORK_OWNER + NO_OBSERVED_PEER_IN_BOUNDED_RX_CAPTURE`.

The strict independently proven **physical/electrical exclusivity predicate remains UNVERIFIED**. This acceptance is **not** an automatic downgrade of all hardware interlocks; it is an auditable experimental scope decision.

- **G01:** G01-09 positive user-video-anchored restart, autonomous/independently measured physical controller epoch still OPEN for future TX.
- **G02:** conditional scope accepted, invalidatable, not automatically transferrable to new session.
- **G03:** physical EOF OPEN.
- **G04:** exclusive reply-slot timing OPEN; G04-07 USER DEFERRED.
- **G05:** hardware FIFO/drain/DE release PARTIAL/HOST-ONLY.
- **G06:** reset/brownout electrical fail-low OPEN.
- **NATIVE TX / semantic writes:** HARD DENY. Any new live native handshake/reply/ACK/write needs explicit separately scoped approval plus all applicable safety proof.

Next investigation G03 offline physical EOF / single-owner UART metadata using existing ESPHome code and captures, no new active response or on-device flash without approval.

**Source priority:** raw XTR bus samples > exact YAML and historical experimental result > genuine collaborative capture > Connect firmware > cross-model ATEC diagrams > community posts. The user-provided PDF/photo evidence is cross-model/documentary, not an electrical bench proof.
