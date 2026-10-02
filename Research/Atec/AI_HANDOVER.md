# AI HANDOVER — Thermia ATEC / DHP-AQ side branch

Last updated: **2026-10-02**

## 0. Source-of-truth rule

This file is a continuation aid, not the overall canonical project state.

For the project use:

1. newest `Research/THERMIA_PROJECT_STATE.md`
2. newest confirmed result in `Research/EXPERIMENT_LOG.md`
3. `Research/PROTOCOL_FINDINGS.md`
4. raw capture/log
5. YAML used
6. older notes/chats

For ATEC-specific bus behaviour, raw ATEC/Eco captures outrank this handover and derived notes.

Never promote XTR-local proof to ATEC-local proof without independent confirmation.

---

# 1. Current status

## ATEC

**ATEC-EXP1 — PREPARED / NOT RUN**

Active experimental YAML:

`Research/Atec/thermia_atec_waveshare_atec_exp1_queued_room_setpoint.yaml`

Human overview:

`Research/Atec/README.md`

Passive build:

`Read-only/ATEC/thermia_atec_waveshare_readonly_v01.yaml`

No live target ATEC result has been supplied.

## Current XTR context

At this update the canonical XTR state says:

- **EXP386 — COMPLETE / POSITIVE**
- **EXP383 — PREPARED / NOT RUN**
- current published write build: `Write (Beta)/thermia_itec_xtr_m_waveshare_write_beta_v4_0.yaml`

EXP386 locally proves native DCM-style controller-restart recovery on the tested XTR M.

Do not import its R1 permission rule into ATEC.

ATEC-EXP1 keeps FC17 capture-only.

---

# 2. Goal

Understand and emulate the native Thermia/Danfoss Online/DCM integration path for ATEC/DHP-AQ-family systems.

First bounded semantic target:

`03F4` / decimal 1012 / `03E8` page word12.

Do not broaden to arbitrary direct Modbus writes.

---

# 3. Primary raw evidence

Primary gateway logs:

- `itec_eco5_gateway_20260926.log`
- `itec_eco5_gateway_20260928.log`

Additional genuine Online/DCM-family captures:

- `thermia_capture_20260924_210001(1).log`
- `thermia_capture_20260925_071517.log`
- `thermia_capture_20260925_090209.log`
- `thermia_capture_20260925_090550.log`

Supporting external discussion:

`https://github.com/klejejs/ha-thermia-heat-pump-integration/discussions/143`

Derived analysis:

`Research/EXTERNAL_ITEC_ECO5_FULL_CAPTURE_ANALYSIS.md`

Raw bytes win if a derived note conflicts with them.

---

# 4. 2026-10-02 direct raw reparse

## 4.1 0708/count6

Paired replies in the two primary gateway logs:

- 2026-09-26: 183
- 2026-09-28: 81
- total: **264**

Exact six-zero reply:

```text
0000 0000 0000 0000 0000 0000
```

Counts:

- 155/183
- 42/81
- **197/264 combined**

Interpretation:

**Observed fact:** all-zero is the dominant steady-state reply.

**Unknown:** it is not the only lifecycle/status reply.

Observed raw W4 values include:

`0100, 03DC, 03D8, 03D0, 038C, 0380, 0300, 0200, 0000`.

ATEC-EXP1 therefore continues to use six-zero idle but does not claim it represents all gateway lifecycle states.

### Important byte-order correction

The derived external capture analysis contains a statement interpreting raw frame:

`0f030c0000000000000000010000001c88`

as fifth word `0001`.

Under standard Modbus big-endian register decoding, its six data words are:

```text
0000 0000 0000 0000 0100 0000
```

For future ATEC work, trust the raw frame and standard Modbus word order.

Do not rewrite historical notes as if this correction was known earlier.

## 4.2 Desired selectors

Observed:

```text
0000 0001 0000 0001 0000 0000
-> FC03 03E8/count14
```

Also observed:

```text
0000 0008 0000 0008 0000 0000
-> FC03 042E/count15
```

Strong current model:

- W1 = low-half desired-page/PULL bitmap;
- W2:W3 = current-page PUSH/refresh bitmap;
- W0 = possible high-half PULL bitmap, unproven;
- W4/W5 = lifecycle/status/session fields, unresolved.

## 4.3 03E8/count14

Combined FC16 count: **216**.

Only 2 unique controller payloads in the two gateway logs.

Dominant `03F4=20`.

One controller republish has `03F4=30`.

Captured desired-page transaction changes only `03F4`.

Discussion #143 independently maps decimal 1012 / `03F4` to room thermostat.

Status:

**STRONGLY SUPPORTED ATEC/DHP-AQ-family semantic mapping.**

Not locally proven on the user's target ATEC yet.

## 4.4 0410/count22

14 controller FC16 pages, 2 payload variants.

`041D=39` throughout those captured pages.

Discussion #143 maps decimal 1053 / `041D` to Hot Water Start.

Status:

**STRONGLY SUPPORTED candidate.**

Read-only diagnostic only. Not an EXP1 write target.

## 4.5 042E/count15

16 controller FC16 pages, 3 payload variants.

Observed:

- `042E`: 1 and 0
- `042F`: 0 and 1
- `0433`: 5
- `0434`: 40

Later XTR-local proof maps:

- 042E Hot Water Enabled
- 042F Hot Water Mode
- 0433 Startup HT
- 0434 Heating Time

ATEC status:

**cross-model/capture-backed candidates** until target correlation.

## 4.6 0442/count13

13 controller FC16 pages, one stable payload:

```text
0442  1
0443 19
0444  0
0445 28
0446  0
0447 -8
0448  5
0449 40
044A  0
044B  0
044C  0
044D 10
044E 10
```

Later XTR-local proof maps selected fields:

- 0442 Cooling Enabled
- 0443 Desired Cooling Temperature
- 0445 Cooling Active Above
- 0449 Cooling Time
- 044C Cooling Room Sensor
- 044D/044E Room Hysteresis Low/High, raw÷10

ATEC status:

**cross-model/capture-backed candidates**, not local target proof.

## 4.7 0546/count20

14 controller FC16 pages, one stable payload.

Important words:

- `0553=2`
- `0559=0`

Public Online/DCM mapping:

- 0553 Operation Mode: 0 OFF, 1 AUTO, 2 COMPRESSOR, 3 AUX, 4 HOT_WATER
- 0559 Link Integration: 0 LIGHT, 1 SYSTEM

Current XTR:

- 0553 locally proven;
- 0559 strongly supported, not yet locally proven there.

ATEC:

- 0553 STRONGLY SUPPORTED candidate
- 0559 STRONGLY SUPPORTED candidate
- passive diagnostics only
- no write test yet

## 4.8 04A6/count13

Combined count across primary gateway logs: **583**.

Three payload variants.

Interpretation:

frequent overlay family.

Do not treat it as a proven mandatory ordered approval/sync step.

---

# 5. FC17 approval/session evidence

Across the two primary gateway logs:

- `071C/0730` challenges: **163**
- exact 16-byte FC17 responses: **6**

Breakdown:

- 2026-09-26: 99 challenges / 2 responses
- 2026-09-28: 64 challenges / 4 responses

Two verified pairs:

```text
C 63CE FB32 C6F4 1382 0879 9237 0CAC EEBA
R 1691 A5F3 F8E8 D587 3892 4416 E8E6 A3D5

C 31FB 59FC 8FB1 175C D89F 904D 06D9 2EA4
R FD63 6CCD 0F92 1D83 FF23 2A1A 2413 B372
```

Four additional exact pairs occur in the 2026-09-28 log.

Unknown:

general challenge-response transform.

Therefore:

**ATEC-EXP1 FC17 policy = capture-only / NO TX.**

Do not fixed-replay a response.

Do not import XTR EXP386 R1 gating.

---

# 6. Settings PUSH/refresh page map

```text
bit00 03E8
bit01 03FC
bit02 0410
bit03 042E
bit04 0442
bit05 0456
bit06 046A
bit07 047E
bit08 0492
bit09 04A6
bit10 04BA
bit11 04D8
bit12 04F6
bit13 050A
bit14 051E
bit15 0532
bit16 0546
bit17 055A
bit18 057B
bit19 059C
bit20 05BD
bit21 05DE
bit22 05FF
bit23 0620
bit24 0641
bit25 0662
bit26 0683
bit27 06A4
bit28 06C5
bit29 06EA
bit30 06F1
bit31 06F4
```

Exact page counts used by EXP1 snapshot:

```text
03E8/14 03FC/11 0410/22 042E/15
0442/13 0456/12 046A/18 047E/19
0492/11 04A6/13 04BA/22 04D8/27
04F6/14 050A/19 051E/10 0532/18
0546/20 055A/33 057B/33 059C/33
05BD/33 05DE/33 05FF/33 0620/33
0641/33 0662/33 0683/33 06A4/33
06C5/33 06EA/7  06F1/3  06F4/19
```

---

# 7. ATEC-EXP1 hypothesis

With the native Online/DCM responder absent, the target ATEC can be serviced on logical endpoint `0x0F` using only exact capture-backed frame shapes, and a fresh `03E8/count14` page can be semantically changed at exactly word12/`03F4`.

Only `03F4` is the experiment variable.

Do not add other semantic targets before EXP1 closes.

---

# 8. ATEC-EXP1 state/safety model

```text
stage 0  passive preflight
stage 40 active capture-backed runtime service
stage 99 stopped / fail-closed
```

Preflight:

- 10 s;
- DE LOW;
- no TX;
- bus must remain fresh;
- any existing `0x0F` responder => STOP.

Active runtime aborts on:

- peer responder;
- parser resync delta;
- RX-buffer drop delta.

Unknown `0x0F` traffic:

capture-only.

FC17:

capture-only.

---

# 9. 0708 behavior in EXP1

Normal idle:

```text
0000 0000 0000 0000 0000 0000
```

Evidence: 197/264 paired replies in the two primary logs.

Do not synthesize unresolved non-zero W4 lifecycle states.

Room desired selector:

```text
0000 0001 0000 0001 0000 0000
```

Broad manual settings refresh:

```text
0000 0000 FFFF 867F 03DF 0000
```

---

# 10. Room-setpoint semantic flow

Preconditions:

- stage40 active;
- writes enabled;
- peer=0;
- parser/RX clean;
- no snapshot/write active;
- fresh controller `03E8/count14` cache <=60 s;
- target integer 20..30 °C.

Flow:

```text
fresh controller 03E8
-> exact 0708/count6
-> desired selector
-> controller FC03 03E8/count14
-> return full cached page with ONLY word12 changed
-> controller FC16 03E8/count14
-> ACK controller FC16
-> compare all words
```

Positive:

- word12 == target
- every other word == cached original
- extraDeltaWords=0
- peer=0
- resync=0
- drops=0

Negative:

controller republishes original word12 unchanged.

Inconclusive:

timeout, stale cache, unexpected page, extra delta, integrity fault, ambiguous result.

FC16 ACK alone is not semantic success.

---

# 11. Queue

One active transaction max.

One pending target max.

Latest intent wins.

No TX merely to store/replace pending intent.

>=2 s settle after completion.

Queued request must still use a fresh valid page.

No automatic retry after semantic failure.

Queue behavior is not ATEC-proven until live results exist.

---

# 12. Passive build

`Read-only/ATEC/thermia_atec_waveshare_readonly_v01.yaml`

2026-10-02 update adds passive Candidate diagnostics for selected fields in:

- 0410/22
- 042E/15
- 0442/13
- 0546/20

Safety remains:

- no tx_pin
- no UART write
- no DE HIGH
- no polling
- no ACK
- no DCM emulation

Candidate labels are not proof.

---

# 13. First live EXP1 run

1. Boot.
2. Touch nothing during preflight.
3. Require:
   ```text
   PREFLIGHT_PASSED peer=0 busFresh=1 ENTER_STAGE40 DE=LOW
   ```
4. Observe clean runtime.
5. Press **ATEC Request Settings Snapshot**.
6. Require `SETTINGS_SNAPSHOT_COMPLETE`.
7. Record current `03F4`.
8. If clean, request a 1 °C change.
9. Wait for one terminal classification.
10. If positive, restore original value.

No queue stress in first run.

---

# 14. Smallest useful returned log

Start:

`PREFLIGHT_PASSED`

End after:

- `SETTINGS_SNAPSHOT_COMPLETE`, or
- first `WRITE_CONFIRMED`, or
- first negative/inconclusive marker, or
- any STOP/abort marker.

Ideal:

```text
PREFLIGHT_PASSED
SETTINGS_SNAPSHOT_ARMED
<snapshot pages>
SETTINGS_SNAPSHOT_COMPLETE
ROOM_WRITE_ARM
0708_SELECTOR_TX
FC03 03E8/count14
desired page
FC16 03E8/count14 republish
terminal result
```

---

# 15. Status vocabulary

Use exactly:

- PREPARED / NOT RUN
- RUNNING / PARTIAL
- COMPLETE / POSITIVE
- COMPLETE / NEGATIVE
- COMPLETE / INCONCLUSIVE
- SUPERSEDED / NOT RUN

Current:

**ATEC-EXP1 — PREPARED / NOT RUN**

---

# 16. Evidence classification

## OBSERVED FACTS

- 0x0F carries mailbox/settings traffic.
- 0708/count6 is polled.
- six-zero 0708 is dominant steady-state reply.
- non-zero lifecycle/status W4 values occur.
- W1=0001 precedes FC03 03E8.
- W1=0008 precedes FC03 042E.
- 03E8 desired-page round trip changes 03F4 20↔30.
- 0410/22, 042E/15, 0442/13, 0546/20 occur.
- 0553=2 and 0559=0 in captured 0546 pages.
- 163 FC17 challenges / 6 responses across the two gateway logs.
- 04A6/13 is a frequent overlay family.

## STRONG CONCLUSIONS

- native settings flow is page-oriented;
- 03F4 is the strongest ATEC room-setpoint candidate;
- controller FC16 republish is the semantic acceptance signal;
- W1 is a desired-page/PULL selector for observed low-half pages.

## HYPOTHESES

- target ATEC works with EXP1 without an FC17 response;
- captured selector works unchanged;
- all-zero idle is sufficient for target steady-state service;
- target adopts 03F4 through current emulator;
- XTR field semantics inside 042E/0442/0546 apply unchanged to target ATEC.

## OPEN / UNKNOWN

- FC17 transform;
- ATEC R1/session permission rule;
- W0 exact role;
- W4/W5 semantics;
- firmware portability;
- local target writeability of 041D, 042E, 0442, 0553, 0559;
- ATEC queue behavior before live testing.

---

# 17. Do not do next

Do not prepare ATEC-EXP2 yet.

Do not add writes for 041D, 042E, 0442, 0553 or 0559 because passive evidence improved.

Do not fixed-replay FC17.

Do not import XTR EXP386 session rules.

First run and close ATEC-EXP1.

---

# 18. Minimum files before changing ATEC code

```text
Research/THERMIA_PROJECT_STATE.md
Research/PROTOCOL_FINDINGS.md
Research/Atec/AI_HANDOVER.md
Research/Atec/README.md
Research/Atec/thermia_atec_waveshare_atec_exp1_queued_room_setpoint.yaml
Read-only/ATEC/thermia_atec_waveshare_readonly_v01.yaml
Research/EXTERNAL_ITEC_ECO5_FULL_CAPTURE_ANALYSIS.md
```

When exact wire behavior matters, use the raw captures.

---

# 19. Immediate next action

**Run ATEC-EXP1. Do not design EXP2 yet.**

Validate, in order:

1. passive peer preflight;
2. stage40 runtime;
3. manual settings snapshot;
4. one 1 °C `03F4` change only if clean;
5. restore original after positive result.

After a live log is supplied:

- separate Observed facts / Strong conclusions / Hypotheses / Unknowns;
- classify EXP1;
- preserve negative/inconclusive evidence;
- update ATEC docs;
- only then decide on a next experiment.
