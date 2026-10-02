---
document_type: "AI handover / continuation guide"
project: "Thermia legacy iTec / Danfoss DHP-AQ RS485 reverse engineering"
repository: "ryckema/Thermia_itec"
snapshot_date: "2026-10-02"
language: "English"
intended_reader: "AI system assisting a technically competent owner/researcher"
status: "living handover; canonical repository files override this snapshot"
---

# Thermia iTec Reverse-Engineering Project — AI Handover

## 0. Purpose of this file

This file is designed to be given directly to another AI system together with the relevant repository files, YAML and bus logs.

Its purpose is to let that AI continue the project for **another Thermia/Danfoss heat-pump installation** without treating findings from one model as automatically valid on another model.

The project is not a generic Modbus-register project. The strongest result so far is that native control follows the Thermia/Danfoss **Online / Connect / DCM-style page-owned protocol**, and the safest continuation strategy is to reproduce that native behavior rather than issue speculative direct register writes.

This handover is a **snapshot**. It must never override newer evidence in the repository.

---

# 1. Mandatory source-of-truth order

Before answering protocol questions, generating experimental YAML or proposing a write test, the AI must read the newest available files in this order:

1. `Research/THERMIA_PROJECT_STATE.md`
2. newest confirmed result in `Research/EXPERIMENT_LOG.md`
3. `Research/PROTOCOL_FINDINGS.md`
4. relevant raw log/capture
5. YAML used for that experiment
6. older notes, README files, discussions and chats

If sources conflict, prefer newer and more direct evidence.

Never infer the current experiment from an older README or older discussion when a newer canonical state exists.

Never mark an experiment complete because YAML was generated. Completion requires a user-supplied result/log or explicit confirmation.

Use these experiment statuses exactly:

- `PREPARED / NOT RUN`
- `RUNNING / PARTIAL`
- `COMPLETE / POSITIVE`
- `COMPLETE / NEGATIVE`
- `COMPLETE / INCONCLUSIVE`
- `SUPERSEDED / NOT RUN`

---

# 2. Important repository consistency warning at this snapshot

At the time this handover was prepared there is a documentation divergence in the XTR write track:

- `Research/THERMIA_PROJECT_STATE.md` still names **EXP386** as the latest authoritative completed XTR session result and refers to Write Beta v4.0.
- `Write (Beta)/README.md` describes a newer v4.1 build and later EXP387/EXP388 work.
- the root `README.md` also still refers mainly to v4.0 / EXP383-era status.

Per the project's own source-of-truth rules, **do not silently promote README claims over the canonical state**.

Before making further XTR write-track changes, reconcile the later EXP387/EXP388 evidence into the canonical files if the underlying result logs support it.

This warning is intentional: another AI must not choose a newer-looking README over canonical experiment evidence merely because its filename/version number is larger.

---

# 3. Project goal

Primary goal:

> Understand and, where possible, emulate the native Thermia/Danfoss Online / Connect / DCM integration path with ESP32/ESPHome and Home Assistant.

Secondary goals:

- robust read-only local monitoring;
- model-specific register and page mapping;
- safe native semantic writes;
- eventual generic DCM/Online emulator;
- understand the native challenge-response mechanism;
- cross-model compatibility only after evidence is collected per model.

Do **not** redirect the project toward room-sensor emulation. Room-sensor traffic is useful supporting protocol evidence, but it is not the main integration target.

Do not ask the owner to disconnect the room sensor.

---

# 4. Safety philosophy

Start passive.

A new model or new installation is **not write-compatible until proven**.

Before any new active TX target, state:

- slave/address/page;
- current known value, if available;
- evidence source for the mapping;
- expected effect;
- plausible unintended effects;
- abort conditions;
- rollback/recovery procedure.

Avoid:

- broad register writes;
- uncontrolled scans;
- speculative writes to unknown addresses;
- changing more than one unknown field at once;
- automatic retries after a failed semantic transaction;
- treating a normal Modbus address/count ACK as proof that a setting changed.

Unexpected traffic is capture-only unless it is explicitly part of the current hypothesis.

Keep driver enable LOW outside a guarded TX.

For active Home Assistant experiments, keep controls under `Configuration`.

Keep experiment log lines visually distinctive using the existing red/brown convention.

---

# 5. Experiment discipline for any AI continuing this work

For every experiment, explicitly record:

## Experiment ID and hypothesis

Use a model-specific experiment identifier if working outside the XTR track.

Do not silently reuse the XTR experiment number sequence for another model.

Example:

`ECO-WRITE-02 — initial FC16 ACK progression`

## Baseline

Name the exact previous result or passive file used as the baseline.

## Exact controlled change

State the one new variable.

Do not change unrelated timing, parsers, page mappings and HA UI simultaneously unless the hypothesis requires it.

## Transmitted frames / pages

List every frame class that may be transmitted.

If a hard-coded frame is used, verify its Modbus CRC before publication.

## Positive criterion

Define what observation proves the hypothesis.

## Negative criterion

Define what cleanly rejects it.

## Inconclusive criterion

Use this when the required stimulus never occurred or transport evidence is ambiguous.

## Abort criterion

Parser integrity change, peer responder, unexpected page/count, wrong sequence, unsafe device behavior, loss of DE control, or any other condition that invalidates the experiment.

## Recovery

State what the owner should do if the active session becomes stuck.

Prefer passive recovery and the normal controller restart procedure over additional speculative TX.

---

# 6. Evidence classification

Every protocol statement should be labelled where relevant as one of:

- `PROVEN / locally confirmed`
- `STRONGLY SUPPORTED`
- `HYPOTHESIS`
- `OPEN / UNKNOWN`
- `DISPROVEN / SUPERSEDED`

Also identify the evidence family:

- locally confirmed on this XTR M;
- independently observed on iTec Eco / DHP-AQ;
- genuine Thermia Online/DCM capture evidence;
- firmware-derived evidence;
- official Thermia/Danfoss documentation;
- reproducible independent measurement;
- community interpretation;
- speculation.

Do not collapse these categories.

A genuine Eco5 capture is strong evidence for Eco5 native gateway behavior, but it is not automatically local proof on Eco8 or XTR.

A locally proven XTR replay behavior is not automatically proof of Eco replay tolerance.

---

# 7. Physical bus baseline

## Bus parameters confirmed on the tested legacy iTec platform

```text
Modbus RTU-like framing
9600 baud
8 data bits
Even parity
1 stop bit
Modbus CRC16
```

## Tested XTR Waveshare wiring

The tested XTR M setup uses a Waveshare ESP32-S3-RS485-CAN / ESP32-S3-RS485-CAN-U.

```text
Thermia RJ45 pin 1 -> RS485 A+
Thermia RJ45 pin 3 -> RS485 B-
Thermia RJ45 pin 5 -> bus reference not connected in the tested isolated setup
Thermia RJ45 pins 7/8 -> +12 V not connected
```

The Waveshare is powered separately by USB-C.

Current tested GPIO assignments:

```text
GPIO18 = RX
GPIO17 = TX in active write builds
GPIO21 = RS485 driver enable / direction
```

Read-only builds intentionally omit TX and keep DE low.

The tested installation leaves the Waveshare 120-ohm termination jumper open/off.

**Do not present this wiring as universally proven for every Thermia model. Verify the target installation first.**

---

# 8. High-level protocol model

The bus behaves like Modbus RTU, but the native Online/DCM integration is more than ordinary direct register writes.

The strongest current control model is **controller-owned, full-page state exchange**.

For a proven XTR semantic write:

```text
persistent qualified Online/DCM-style runtime
        |
        v
fresh authoritative controller FC16 page
        |
        v
current-page request if refresh is required
        |
        v
desired-page selector through 0708 mailbox
        |
        v
controller FC03 pulls the selected page from emulated slave 0x0F
        |
        v
ESP returns the complete fresh page
with exactly one selected word changed
        |
        v
controller republishes the page using FC16
        |
        v
success only if target matches
AND extraDeltaWords = 0
```

This is fundamentally different from treating the ESP as a second arbitrary Modbus master that writes isolated controller registers.

---

# 9. Native 0x0F configuration page structure

Genuine Online/DCM captures support a 32-page current/PUSH map selected through the `0708/count6` mailbox.

The observed ordered pages are:

```text
03E8 03FC 0410 042E 0442 0456 046A 047E
0492 04A6 04BA 04D8 04F6 050A 051E 0532
0546 055A 057B 059C 05BD 05DE 05FF 0620
0641 0662 0683 06A4 06C5 06EA 06F1 06F4
```

The strongest current mailbox interpretation is:

```text
W0 W1 W2 W3 W4 W5
```

- `W1`: low-half desired-page / PULL bitmap
- `W2:W3`: 32-bit current-page PUSH/refresh bitmap
- `W0`: probable high-half desired-page bitmap, but evidence is more limited
- `W4/W5`: session/lifecycle/status fields not fully decoded

Do not infer unknown W4/W5 semantics merely from observed values.

---

# 10. XTR M — locally proven semantic write scope

These findings are **local to the tested Thermia iTec XTR M unless stated otherwise**.

## Page `03E8/count14` — heating

Locally proven writable:

| Register | Meaning |
|---|---|
| `03E8` | Heating Curve |
| `03E9` | Heating Minimum |
| `03EA` | Heating Maximum |
| `03EB` | Curve Correction +5 |
| `03EC` | Curve Correction 0 |
| `03ED` | Curve Correction -5 |
| `03EE` | Heating Stop |
| `03EF` | Reduced Temperature |
| `03F0` | Room Factor |
| `03F4` | Room Setpoint |

Unknown/unresolved words remain around this page. Do not assign meanings to `03F1/03F2/03F3/03F5` on XTR without evidence.

## Page `042E/count15` — hot water / service

Locally proven writable:

| Register | Meaning |
|---|---|
| `042E` | Hot Water Enabled |
| `042F` | Hot Water Mode |
| `0433` | Startup HT |
| `0434` | Heating Time |

`0430` is currently a strongly supported Top-up candidate, not yet local XTR proof in the canonical EXP383 state.

## Page `0442/count13` — cooling

Locally proven writable:

| Register | Meaning |
|---|---|
| `0442` | Cooling Enabled |
| `0443` | Desired Cooling Temperature |
| `0445` | Cooling Active Above |
| `0449` | Cooling Time |
| `044C` | Cooling Room Sensor |
| `044D` | Cooling Room Hysteresis Low |
| `044E` | Cooling Room Hysteresis High |

Locally confirmed guard for `0445`:

```text
minimum Cooling Active Above = max(10 C, Heating Stop + 3 K)
```

`044D` and `044E` use raw/10 degrees C.

## Page `0546/count20` — system

Locally proven writable:

| Register | Meaning |
|---|---|
| `0553` | Operation Mode |

Working labels used by the XTR project:

```text
0 Off
1 Auto
2 Compressor
3 Auxiliary Heater
4 Hot Water
```

Not every enum value has necessarily been individually exercised in every build.

---

# 11. XTR candidate controls that must not be called proven

The canonical EXP383 state lists these as `STRONGLY SUPPORTED / TEST`:

| Register | Candidate meaning |
|---|---|
| `0430` | Hot Water Top-up |
| `0444` | Cooling Hysteresis |
| `0446` | Cooling Configuration / Type |
| `0448` | Cooling Stop Threshold |
| `044A` | Cooling Max Start Temperature |
| `044B` | Cooling Min Stop Temperature |
| `0559` | Link Integration |

`0559` is the highest-risk candidate because changing integration mode may affect the Online/DCM-style session itself.

Do not promote any of these from implementation presence alone.

---

# 12. XTR native session recovery model

Canonical XTR evidence through EXP386 locally confirms this guarded recovery path:

```text
unqualified stage40
  -> exact 071C/0730 outside guard: NO TX
  -> >=5 s complete bus silence
  -> cold-start recovery armed
  -> first valid frame after silence = BOOT_RETURN
  -> observe A80E=0000 / A80F=0005
  -> exact 071C/0730 challenge
  -> one known R1 replay
  -> first post-R1 FC16 = 03E8/count14
  -> ordered initial FC16 ACK chain
  -> synchronization through 06F4/count19
  -> persistent runtime
  -> fresh known runtime FC16 ACK
  -> 0708 idle reply
  -> runtime qualified
```

Important:

- an exact `071C/0730` challenge alone is **not** permission to TX on XTR;
- the local XTR R1 permission is guarded by the known cold-start state;
- challenge-response derivation itself is still unsolved;
- fixed replay acceptance on XTR does not prove fixed replay acceptance on Eco.

Later README files describe EXP387/EXP388 hardening, but see the consistency warning near the top of this handover before treating those as canonical.

---

# 13. Genuine iTec Eco5 + Thermia Online evidence

Two genuine Eco5 gateway captures are available:

```text
itec_eco5_gateway_20260926.log
itec_eco5_gateway_20260928.log
```

The combined reduction is documented in:

`Research/iTec Eco/ECO5_GATEWAY_CAPTURE_EVIDENCE.md`

## Directly observed

Across the two captures there are **six successful exact `071C/0730` approval responses**.

Every successful gateway response is followed by controller:

```text
0x0F FC16 start=03E8 count=14
```

Observed successful response points:

- challenge #29: four sessions
- challenge #3: two sessions

The six challenge bodies differ.

The six gateway response bodies also differ.

Therefore the captures do **not** prove a universal constant approval response.

## Initial synchronization

Where `03E8/count14` is immediately ACKed, the controller proceeds:

```text
03E8/14
 -> ACK
03FC/11
 -> ACK
0410/22
 -> ACK
042E/15
 -> ACK
0442/13
 -> ...
```

The wider captured chain continues through many configuration pages and eventually past `06F4`.

Two challenge-#3 sessions in the second capture are especially useful:

- the gateway approval response is accepted;
- the controller starts sending `03E8/count14`;
- no immediate `03E8` ACK is sent;
- the controller retransmits `03E8/count14` repeatedly;
- it does not progress to `03FC` during the inspected 10-second window.

This is genuine Eco5 evidence that the FC16 address/count ACK participates in page progression.

---

# 14. Current iTec Eco active track

Current prepared artifact:

`Research/iTec Eco/thermia_itec_eco_waveshare_write_exp01.yaml`

Status:

`ECO-WRITE-01 — PREPARED / NOT RUN`

## Hypothesis

The target iTec Eco controller accepts a previously captured known-good Eco5 gateway response against a **different live challenge**.

## Why challenge #3

The genuine Eco5 captures show two successful native gateway responses at challenge #3.

Therefore:

```text
challenge #1 -> capture only / NO TX
challenge #2 -> capture only / NO TX
challenge #3 -> one replay
```

The replay body came from another genuine Eco5 session/challenge, making it an explicit mismatched-replay test.

## One permitted frame

```text
0F 17 10 16 91 A5 F3 F8 E8 D5 87 38 92 44 16 E8 E6 A3 D5 E2 27
```

Response body:

```text
1691A5F3F8E8D58738924416E8E6A3D5
```

Modbus CRC value:

```text
0x27E2
```

## EXP01 positive criterion

After the challenge-#3 replay:

```text
controller sends 0x0F FC16 03E8/count14
```

EXP01 deliberately does **not** ACK that page.

This is because the downstream Eco5 ACK/synchronization behavior is already known from genuine captures; EXP01 isolates only replay acceptance.

## Negative criterion

Challenge #3 occurs and R1 is transmitted, but no `03E8/count14` appears within 10 seconds.

## Inconclusive

The controller returns but challenge #3 is not reached in the bounded window, or the required power-cycle/silence stimulus never occurs.

## Abort

- another response-shaped `0x0F FC17` peer;
- another `0x0F FC16` ACK-shaped responder;
- parser CRC/resync/RX-drop integrity change;
- user cancel;
- any loss of safe DE behavior.

Do not prepare the next Eco active stage until a real EXP01 result/log is supplied.

---

# 15. Useful Eco / DHP-AQ cross-model register evidence

These findings are useful when onboarding another legacy iTec Eco / DHP-AQ device, but each target still needs local confirmation where practical.

## Room-sensor path

Observed Eco/DHP-AQ semantics include:

```text
0x0A B3B0 = room temperature x10
0x0A B3B1 = pending room-setpoint request
0x0A B3C5 = controller-propagated / confirmed room setpoint
```

## Outdoor-unit telemetry around slave `0x1E`

Independent Eco evidence supports:

```text
FC04 000B = compressor frequency
FC04 000C = max-frequency ratio
FC04 000D = current /10 A
FC04 000E = fan RPM
FC04 0010 = EEV steps
FC04 0014 = status bitfield
FC04 0015 = operating/context bits
```

For `0014`, observed Eco bit semantics include:

```text
bit 0 = compressor running
bit 2 = outdoor fan turning
bit 3 = water flow / circulation pump
bit 4 = base/always-present bit in observed states
```

Known observed combined values include 16, 20, 24, 28 and 29.

Do not call `20` defrost merely from the number. It has been observed with fan-only/autonomous behavior.

## Controller output / pump-speed evidence

Cross-model Eco evidence supports:

```text
0x02 A80F = condenser/circulation-pump speed %
```

This meaning is stronger on Eco/DHP-AQ than the older XTR interpretation.

`A80C` behaves as an output bitfield on Eco and must not be blindly interpreted using older XTR sequence/context assumptions.

## Shared settings-page evidence

Eco/DHP-AQ evidence supports the same general `03E8..03F4` settings region.

`03F3` has Eco evidence as High Power on an Eco8/DHP-AQ system.

Genuine Eco5 app traffic also uses `042E/042F` for hot-water related changes.

Do not assume identical enum meanings/ranges until correlated on the target device.

---

# 16. Recommended onboarding workflow for a new owner's device

The AI should create a **separate model/device evidence track** instead of immediately modifying XTR-proven code.

## Phase A — identify the device

Collect:

```text
Thermia model:
Approximate manufacture year:
Controller board / PCB marking:
Display firmware version:
Heat-pump controller firmware if visible:
Outdoor unit model:
Existing room sensor:
Any Thermia Online / Connect / DCM hardware present:
RJ45 / bus connector layout:
ESP / transceiver board:
Current ESPHome version:
```

Photographs of board labels and the service-information screens are useful.

Do not infer board family from the commercial product name alone.

## Phase B — establish passive bus compatibility

Start from the closest read-only profile.

Confirm:

```text
9600 8E1
stable CRC-valid traffic
known participant addresses
no RX buffer drops
no growing resync counter
no unintended DE/TX
```

Record at least:

- steady-state idle;
- heating if naturally available;
- DHW if naturally available;
- controller boot;
- one or more safe front-panel setting changes.

## Phase C — compare local observations with existing maps

Classify each candidate as:

```text
locally confirmed
cross-model match
different encoding
not observed
contradicted
```

Do not rename a local field merely because an XTR or Eco label looks plausible.

## Phase D — prove page layout before active control

For the target device, verify controller-originated `0x0F` configuration pages and counts.

Where possible, change a front-panel setting and observe which exact page/word changes.

One controlled panel change is stronger evidence than a large passive correlation table.

## Phase E — prove native session behavior

Only if active Online/DCM-style emulation is required:

- reproduce the target device's cold-start challenge behavior;
- keep challenge traffic capture-only until there is a specific hypothesis;
- prefer genuine gateway captures from the same model family;
- do not assume XTR replay tolerance.

## Phase F — prove synchronization before semantic writes

For a new model, do not jump from challenge response straight to a setting change.

First prove that:

- the session opens;
- initial FC16 page progression behaves as expected;
- page/count ACKs are accepted;
- normal runtime remains stable;
- peer-responder and parser guards are clean.

## Phase G — first semantic write

Use the safest known reversible field with:

- known current value;
- known page ownership;
- known local or strong same-family semantic mapping;
- one-word delta;
- exact controller republish requirement;
- rollback value recorded before TX.

Room Setpoint `03F4` is a good candidate **only when the target's page and meaning have been independently verified**.

Do not choose it merely because it is proven on XTR.

---

# 17. What the AI should ask the owner to return after an experiment

Request the smallest useful evidence, but enough to evaluate the whole transaction.

For active session experiments, request:

```text
the experiment ARM / START marker
through
the terminal COMPLETE / NEGATIVE / INCONCLUSIVE / ABORT marker
plus 10–20 seconds of following passive traffic
```

For semantic writes, also request:

```text
authoritative pre-write page
selector / mailbox exchange
controller FC03 pull
emulator response
controller FC16 republish
front-panel / physical effect
rollback if tested
```

Do not accept a Home Assistant UI change by itself as proof.

Do not accept a standard Modbus ACK by itself as proof.

---

# 18. Canonical files another AI should load

Minimum project context:

```text
Research/THERMIA_PROJECT_STATE.md
Research/EXPERIMENT_LOG.md
Research/PROTOCOL_FINDINGS.md
```

For XTR read-only work:

```text
Read-only/Thermia itec XTR/thermia_itec_xtr_m_waveshare_public_v29.yaml
Read-only/Thermia itec XTR/thermia_itec_xtr_m_waveshare_research_v29.yaml
```

For XTR active work:

```text
Write (Beta)/README.md
Write (Beta)/thermia_itec_xtr_m_waveshare_write_beta_v4_1.yaml
```

But remember the canonical-state/version divergence described earlier. Read the experiment evidence before treating v4.1 claims as authoritative.

For Eco passive work:

```text
Read-only/iTec Eco/thermia_itec_eco_waveshare_public_v01.yaml
```

For Eco active research:

```text
Research/iTec Eco/README.md
Research/iTec Eco/ECO5_GATEWAY_CAPTURE_EVIDENCE.md
Research/iTec Eco/thermia_itec_eco_waveshare_write_exp01.yaml
Research/EXTERNAL_ITEC_ECO5_FULL_CAPTURE_ANALYSIS.md
```

Useful project-wide material:

```text
Research/HOME_ASSISTANT_ENTITIES.md
Research/EXP382_OFFLINE_GAP_ANALYSIS.md
commissioning/service documentation in the repository
raw gateway/DCM captures
collaborator captures
```

---

# 19. Repository-editing rule for an AI agent

Do not modify GitHub merely because a better interpretation is possible.

Before changing repository files:

1. verify the current target path;
2. read the newest canonical state;
3. distinguish offline analysis from a live result;
4. preserve negative and superseded history;
5. do not rewrite old experiments as if later knowledge was known at the time;
6. update canonical state when new evidence materially changes understanding;
7. report changed files and commit IDs.

If the AI does not have repository write permission, prepare the patch/content locally and clearly state that the repository update is pending.

---

# 20. What must never be inferred

Never invent:

- register addresses;
- page meanings;
- CRCs;
- challenge-response algorithms;
- wiring;
- firmware compatibility;
- enum meanings;
- value ranges;
- room-sensor absence/presence;
- Online/DCM presence;
- whether a write "worked" without the user's result.

Never infer that:

```text
same commercial model name = same controller board
same address = same semantics on every model
FC16 ACK = semantic setting accepted
XTR behavior = Eco behavior
Eco5 behavior = Eco8 behavior
generated YAML = completed experiment
published TEST control = proven mapping
```

---

# 21. Decision logic for another AI

Use this decision order:

```text
Do I know the exact target model/board/firmware?
  NO -> identify it; passive only.
  YES
   |
Do I have stable CRC-valid passive traffic?
  NO -> solve wiring/parser/serial first.
  YES
   |
Are the relevant page/register mappings locally correlated?
  NO -> passive/front-panel correlation.
  YES
   |
Is active control actually required?
  NO -> stay read-only.
  YES
   |
Is native session behavior locally or same-model captured?
  NO -> session research only, no semantic write.
  YES
   |
Is page synchronization locally stable?
  NO -> prove session + ACK progression only.
  YES
   |
Is one reversible semantic target locally/same-family supported?
  NO -> do not write.
  YES -> one target, one word, exact republish, rollback recorded.
```

---

# 22. Recommended per-device handover block

For every new collaborator/device, append a block like this to their own working file:

```yaml
device_track:
  owner_label: ""
  model: ""
  manufacture_year: ""
  controller_board: ""
  display_firmware: ""
  controller_firmware: ""
  outdoor_unit: ""
  room_sensor_present: unknown
  online_dcm_present: unknown
  bus_connector: ""
  esp_board: ""
  transceiver: ""
  serial_settings_confirmed: false
  passive_capture_available: false
  closest_existing_profile: ""
  current_experiment: ""
  current_status: "PREPARED / NOT RUN"
  last_completed_experiment: ""
  locally_confirmed_findings: []
  cross_model_candidates: []
  contradictions: []
  important_unknowns: []
  safety_constraints: []
```

This keeps local evidence separate from inherited project knowledge.

---

# 23. Suggested AI startup prompt

The following can be pasted together with this file into another AI system:

> You are continuing an evidence-driven reverse-engineering project for a Thermia/Danfoss legacy iTec heat pump using ESP32/ESPHome and Home Assistant. Treat the attached handover and repository files as a research record, not as universally valid device documentation. First identify my exact model/board/firmware and read the newest canonical project state. Separate locally confirmed behavior on my unit from XTR-local evidence, Eco/DHP-AQ cross-model evidence, genuine Online/DCM capture evidence, firmware-derived evidence and hypotheses. Start passive/read-only unless an active experiment is explicitly intended. For every experiment state the hypothesis, baseline, exact single controlled change, TX frames/pages, positive/negative/inconclusive/abort criteria and recovery plan. Never invent registers, CRCs, mappings, wiring or successful results. Do not mark an experiment complete until I provide a log/result or explicitly confirm it. Prefer the native Online/DCM page-owned mechanism over speculative direct register writes.

---

# 24. Current high-value research questions

Project-wide:

- native challenge-response derivation;
- model-by-model replay tolerance;
- complete generic DCM/Online emulator;
- remaining settings-page meanings;
- faults and alarms;
- calendar/scheduling;
- complete operating-state / defrost model;
- compatibility matrix across XTR, Eco, ATEC and DHP-AQ families.

Eco-specific next gate:

> Does the target Eco controller accept the known-good Eco5 R1 replay against a non-matching live challenge?

XTR-specific canonical gate at this snapshot:

> Reconcile later v4.1 / EXP387–EXP388 evidence into the canonical state before treating it as the official current XTR baseline.

---

# 25. Final instruction to the receiving AI

Do not try to be fast by collapsing evidence levels.

A useful continuation is one where another researcher can later answer:

- What exactly was observed?
- On which model?
- In which log?
- What changed from the previous experiment?
- What was transmitted?
- What did the controller send back?
- What remains unknown?
- Why is the next test safe and informative?

If those questions cannot be answered, the experiment is not yet well specified.

The project should progress by reducing uncertainty one controlled variable at a time.