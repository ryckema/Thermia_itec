# AI HANDOVER — Thermia ATEC / DHP-AQ side branch

Last updated: 2026-10-01

## Purpose

This file is a machine-oriented handover for continuing the **ATEC / DHP-AQ side branch** of the Thermia reverse-engineering project.

It is intended to let another AI continue the work without reconstructing the complete conversation history.

**Important:** this file is an index and working-state summary. It does **not** supersede the main project source-of-truth rules. For the overall project, continue to prefer the newest canonical files in this order:

1. `Research/THERMIA_PROJECT_STATE.md`
2. `Research/EXPERIMENT_LOG.md`
3. `Research/PROTOCOL_FINDINGS.md`
4. raw captures/logs
5. YAML used for the experiment
6. older notes/chats

ATEC evidence must remain separated from locally proven XTR M evidence unless the same behaviour is independently confirmed on both platforms.

---

# 1. Current ATEC state

## Active ATEC experiment

**ATEC-EXP1 — PREPARED / NOT RUN**

Implementation:

`Research/Atec/thermia_atec_waveshare_atec_exp1_queued_room_setpoint.yaml`

Human-readable overview:

`Research/Atec/README.md`

ATEC-EXP1 has been generated and statically checked, but **no target ATEC run result has yet been supplied**.

Do not mark it COMPLETE until a user supplies the actual ATEC log/result or explicitly confirms the outcome.

## Main-project context

At the time this handover was written, the main XTR branch has:

- EXP374 — **PREPARED / NOT RUN**
- EXP373 — **RUNNING / PARTIAL**
- EXP370 — last fully completed numbered experiment, **COMPLETE / POSITIVE**

The ATEC branch borrows the conservative serialized/queued-write safety architecture from the XTR work, but its protocol behaviour must be justified independently by ATEC/Eco capture evidence.

---

# 2. Goal of the ATEC branch

Primary goal:

Reproduce enough of the native Thermia Online/DCM interaction on the ATEC/DHP-AQ family to safely observe and, if confirmed, emulate the native settings write path.

First bounded semantic target:

`0x03F4` / decimal 1012 / room thermostat-room setpoint field.

Do **not** broaden the ATEC branch into arbitrary Modbus writes.

Do **not** infer that an address or behaviour proven on XTR is automatically valid on ATEC, or vice versa.

---

# 3. Evidence sources

## Strongest local files for this branch

Primary raw captures supplied to the project:

- `itec_eco5_gateway_20260926.log`
- `itec_eco5_gateway_20260928.log`

Additional genuine Thermia/DCM-family captures available in the project:

- `thermia_capture_20260924_210001(1).log`
- `thermia_capture_20260925_071517.log`
- `thermia_capture_20260925_090209.log`
- `thermia_capture_20260925_090550.log`

Derived analysis:

- `Research/EXTERNAL_ITEC_ECO5_FULL_CAPTURE_ANALYSIS.md`

External discussion used as supporting evidence:

- `https://github.com/klejejs/ha-thermia-heat-pump-integration/discussions/143`

The public discussion is useful for candidate semantics, but raw captured bus traffic outranks interpretations in the discussion.

---

# 4. Current protocol model

## 4.1 Slave 0x0F is the key path

Current evidence strongly supports `0x0F` as the mailbox/settings path used between the Thermia controller and the Online/DCM side on this platform family.

Observed traffic includes:

- controller FC03 reads from `0x0F`;
- controller FC16 writes to `0x0F`;
- desired-page pulls;
- settings/configuration page exports;
- recurrent runtime pages.

Do not equate "slave 0x0F" with a fully understood physical device identity. Treat it as the observed logical protocol endpoint.

## 4.2 0708/count6 mailbox

The controller polls:

`0x0F FC03 0x0708 count 6`

The six returned words are referred to as:

`W0 W1 W2 W3 W4 W5`

Best current directional interpretation from offline reduction of genuine captures:

- **W1** — low 16-bit desired-page/PULL bitmap;
- **W2:W3** — 32-bit current-page PUSH/refresh bitmap;
- **W0** — possible high half of the PULL bitmap; unproven;
- **W4/W5** — lifecycle/status/capability/session semantics unresolved.

Observed desired-page examples:

- `W1=0001` -> controller FC03 `03E8/count14`;
- `W1=0008` -> controller FC03 `042E/count15`.

This is stronger than a direct-register-write model. The native path is page-oriented.

## 4.3 Desired-page semantic write sequence

Best current model:

```text
1. controller polls 0708/count6
2. gateway advertises desired page through mailbox/PULL bit
3. controller initiates FC03 for that page
4. gateway returns the complete desired page
5. controller later republishes the accepted/current page using FC16
6. gateway ACKs the controller FC16 write
```

For `03E8/count14`, genuine captured write round trips show a one-word change at `0x03F4`.

## 4.4 03E8/count14 page

The page spans:

`0x03E8 .. 0x03F5`

The first ATEC experiment only treats:

`0x03F4 = page word 12`

as a semantic write target.

External discussion #143 independently identifies decimal 1012 / hex `0x03F4` as the room thermostat field.

Genuine captures show `03F4` changing between 20 and 30 and the controller subsequently republishing the page.

This is **strong capture-backed ATEC/DHP-AQ-family evidence**, but the new ESPHome emulator path itself remains unproven until ATEC-EXP1 is run.

---

# 5. Configuration/settings export map

The current 32-page PUSH/refresh map is:

```text
bit 00  03E8
bit 01  03FC
bit 02  0410
bit 03  042E
bit 04  0442
bit 05  0456
bit 06  046A
bit 07  047E
bit 08  0492
bit 09  04A6
bit 10  04BA
bit 11  04D8
bit 12  04F6
bit 13  050A
bit 14  051E
bit 15  0532
bit 16  0546
bit 17  055A
bit 18  057B
bit 19  059C
bit 20  05BD
bit 21  05DE
bit 22  05FF
bit 23  0620
bit 24  0641
bit 25  0662
bit 26  0683
bit 27  06A4
bit 28  06C5
bit 29  06EA
bit 30  06F1
bit 31  06F4
```

Captured page sequence/counts used by ATEC-EXP1:

```text
03E8 / 14
03FC / 11
0410 / 22
042E / 15
0442 / 13
0456 / 12
046A / 18
047E / 19
0492 / 11
04A6 / 13
04BA / 22
04D8 / 27
04F6 / 14
050A / 19
051E / 10
0532 / 18
0546 / 20
055A / 33
057B / 33
059C / 33
05BD / 33
05DE / 33
05FF / 33
0620 / 33
0641 / 33
0662 / 33
0683 / 33
06A4 / 33
06C5 / 33
06EA / 7
06F1 / 3
06F4 / 19
```

Important nuance:

`04A6/count13` is recurrent and can appear overlaid on other transfer activity. It is **not proven to be a mandatory ordered sync step or approval precondition**. ATEC-EXP1 therefore keeps it capture-only outside the explicitly requested settings snapshot.

---

# 6. Runtime FC16 families currently recognised by ATEC-EXP1

The current YAML recognises these captured runtime shapes:

```text
07D0 / 19
07E4 / 17
07F8 / 17
080C / 18
0820 / 18
0834 / 18
0848 / 23
0864 / 4
0870 / 17
0884 / 60
085F / 5   only when all five payload words are zero
```

Unknown `0x0F` FC16 traffic must remain **capture-only**.

Do not widen this whitelist merely because another address looks structurally similar.

---

# 7. Important unresolved 0708 idle-payload issue

There is a deliberate caution here because the available evidence is not uniform enough to promote one value as universally correct.

ATEC-EXP1 currently emits this normal idle reply:

```text
0000 0000 0000 0000 0000 0000
```

This choice was based on the ATEC/Eco capture comparison used while generating the first YAML.

However, the later offline reduction in:

`Research/EXTERNAL_ITEC_ECO5_FULL_CAPTURE_ANALYSIS.md`

documents a repeatedly observed genuine Eco5 steady-state frame:

```text
0F 03 0C 0000 0000 0000 0000 0001 0000 ...
```

i.e. raw words:

```text
0000 0000 0000 0000 0001 0000
```

It also observed later W4 values such as 988, 984, 976, 908, 896, 768, 512, then 0.

Therefore:

- do **not** claim that six zero words are the universal native ATEC/Eco idle state;
- do **not** silently change ATEC-EXP1 before comparing the exact target/capture context;
- treat W4/W5 semantics as unresolved;
- if the first target ATEC run behaves unexpectedly, this is one of the first fields to investigate.

This discrepancy must remain visible in future reasoning.

---

# 8. FC17 / approval-session evidence

Genuine Eco5 capture analysis found two successful startup approval/session transitions using `0x0F FC17`.

Example challenge/response pairs:

```text
C1 63CE FB32 C6F4 1382 0879 9237 0CAC EEBA
R1 1691 A5F3 F8E8 D587 3892 4416 E8E6 A3D5

C2 31FB 59FC 8FB1 175C D89F 904D 06D9 2EA4
R2 FD63 6CCD 0F92 1D83 FF23 2A1A 2413 B372
```

Important limitations:

- only two approval requests were answered in the analysed full capture;
- the challenge-response transform is unknown;
- a duplicated challenge was not answered;
- no general mapping algorithm is known;
- startup/session behaviour must not be guessed from two samples.

**ATEC-EXP1 intentionally does not synthesize an FC17 response.**

All ATEC `0x0F FC17` traffic is capture-only in EXP1.

Do not add fixed-response replay unless a new experiment explicitly tests that hypothesis and has a safe stop/recovery plan.

---

# 9. Current ATEC-EXP1 implementation

File:

`Research/Atec/thermia_atec_waveshare_atec_exp1_queued_room_setpoint.yaml`

## Hardware assumptions encoded in YAML

```text
ESP32 variant: ESP32-S3
UART TX:       GPIO17
UART RX:       GPIO18
RS485 DE:      GPIO21
Baud:          9600
Data bits:     8
Parity:        EVEN
Stop bits:     1
```

These are implementation settings for the test hardware, not a universal Thermia pinout.

## Startup states

```text
stage 0  = passive preflight
stage 40 = active captured-runtime service
stage 99 = stopped / fail-closed
```

Boot behaviour:

- DE LOW;
- no TX for first 10 s;
- observe bus health;
- detect any existing `0x0F` responder;
- only enter stage 40 after a clean peer-free preflight.

## Peer-responder rule

Any response-shaped `0x0F` frame that is not our own immediate echo is treated as evidence of another responder.

Result:

- DE LOW;
- active experiment disabled;
- pending queue cleared;
- snapshot state cleared;
- status becomes STOPPED;
- no bus competition is permitted.

## Parser integrity rule

Any parser resync or RX-buffer-drop delta after active runtime begins is an abort condition.

Do not weaken this guard during early ATEC experiments.

---

# 10. ATEC-EXP1 Home Assistant controls

All experimental controls are under **Configuration**.

## ATEC-EXP1 Room Setpoint

Current bounds:

```text
20 .. 30 °C
step 1 °C
```

Only integer targets are accepted.

The entity is optimistic at UI level, so the authoritative success criterion is **not** the slider state. Success is controller republish on the bus.

## ATEC Request Settings Snapshot

This arms one captured broad settings-export mailbox response on the next exact `0708/count6` poll.

Current bitmap in ATEC-EXP1:

```text
0000,0000,FFFF,867F,03DF,0000
```

The snapshot mechanism:

- does not inject setting values;
- causes/requests the controller export;
- ACKs only exact known page address/count pairs;
- tracks the expected sequence;
- allows bounded retries of the immediately previous page;
- completes at `06F4/count19`;
- provides a fresh `03E8/count14` cache.

## ATEC Abort Experiment

Manual abort:

- DE LOW;
- disables experiment TX;
- disables semantic writes;
- clears pending queue and sync state;
- enters stage 99.

---

# 11. Semantic room-setpoint write flow

A write may begin only when:

- runtime is active;
- stage is 40;
- semantic writes are still enabled;
- no peer responder has been seen;
- parser/RX integrity counters are clean;
- no snapshot/write is already active;
- `03E8/count14` cache is valid and <=60 s old;
- requested value is 20..30 °C.

Target address:

```text
page start: 03E8
page count: 14
word index: 12
address:    03F4
```

Current transaction:

```text
fresh 03E8 cache
-> wait exact 0708/count6 poll
-> return captured selector
   0000,0001,0000,0001,0000,0000
-> controller FC03 03E8/count14
-> return cached 14-word page with ONLY word12 changed
-> controller FC16 03E8/count14 republish
-> ACK controller FC16
-> compare every word
```

Success requires:

- republished word12 equals target;
- every other word equals cached original;
- `extraDeltaWords=0`;
- peer=0;
- parser resync=0;
- RX drops=0.

If controller republishes the original `03F4` value unchanged and no other fault occurs, classify as **COMPLETE / NEGATIVE** for the write attempt.

Unexpected deltas or ambiguous behaviour are **COMPLETE / INCONCLUSIVE**, and semantic writes are disabled.

---

# 12. Queue behaviour

ATEC-EXP1 inherits the one-slot bounded queue design from XTR EXP374.

Policy:

- one active semantic transaction maximum;
- one pending request maximum;
- latest user intent replaces older pending intent;
- no TX merely to store/replace a pending request;
- after a confirmed/no-op transaction, wait >=2 s before dispatch;
- queued request must re-enter the normal fresh-page path;
- no stale-page chaining;
- no automatic retry after semantic failure;
- abort/fault clears pending intent.

**ATEC queue behaviour itself is not proven until live ATEC results are supplied.**

Do not describe it as confirmed.

---

# 13. Current mapped fields

## Strongly supported ATEC/DHP-AQ-family mapping

`0x03F4 / decimal 1012`

Room thermostat / room setpoint.

Evidence:

- external discussion semantic identification;
- genuine captured one-word desired-page changes;
- controller republish after those changes.

## Read-only diagnostic candidate in ATEC-EXP1

`0x041D / decimal 1053`

Mapped in the external discussion as DHW / Hot Water Start.

ATEC-EXP1 exposes it diagnostically when seen in the `0410/count22` page.

**Do not write to 0x041D yet.**

A write target requires a dedicated experiment with exact current value, one controlled variable, expected effect, abort criteria and rollback plan.

---

# 14. First-run procedure

Do not skip directly to a room write.

Recommended first live ATEC run:

1. Boot ATEC-EXP1.
2. Touch nothing during passive preflight.
3. Require:
   ```text
   PREFLIGHT_PASSED peer=0 busFresh=1 ENTER_STAGE40 DE=LOW
   ```
4. Observe runtime long enough to confirm:
   - no peer responder;
   - no parser resync;
   - no RX drops;
   - known runtime FC16 traffic is serviced;
   - 0708 polls are seen and replied to.
5. Press **ATEC Request Settings Snapshot**.
6. Require:
   ```text
   SETTINGS_SNAPSHOT_ARMED
   ...
   SETTINGS_SNAPSHOT_COMPLETE
   ```
7. Record:
   - current cached room setpoint;
   - snapshot page order;
   - any retries;
   - unknown `0x0F` frames;
   - W4/W5 behaviour around 0708.
8. Only if snapshot/runtime are clean, change room setpoint by **1 °C**.
9. Wait for one final classification.
10. If positive, restore the original setpoint using the same path.

Do not stress-test rapid queue changes during the first live run.

---

# 15. Exact log fragment to request from the user

For first ATEC validation, request the smallest useful continuous fragment starting at:

```text
PREFLIGHT_PASSED
```

and ending after:

- `SETTINGS_SNAPSHOT_COMPLETE`, if no semantic write was attempted; or
- first `WRITE_CONFIRMED`; or
- first negative/inconclusive marker; or
- any abort/STOP marker.

For write analysis, the ideal sequence is:

```text
PREFLIGHT_PASSED
SETTINGS_SNAPSHOT_ARMED
<settings page/ACK sequence>
SETTINGS_SNAPSHOT_COMPLETE
ROOM_WRITE_ARM
0708_SELECTOR_TX
<controller FC03 03E8/count14>
<desired page response>
<controller FC16 03E8/count14 republish>
WRITE_CONFIRMED / negative / inconclusive / abort
```

Do not assume progress if the user has not supplied that evidence.

---

# 16. Result classification rules

Use the project status vocabulary exactly.

## PREPARED / NOT RUN

YAML exists, but no target result supplied.

This is the current ATEC-EXP1 status.

## RUNNING / PARTIAL

A log/result has been supplied but does not close the whole experiment.

Record any confirmed sub-results without promoting the full experiment.

## COMPLETE / POSITIVE

For ATEC-EXP1 room write:

- controller republishes `03E8/count14`;
- `03F4` equals requested target;
- every other word matches cached baseline;
- `extraDeltaWords=0`;
- no peer/parser/RX fault invalidates the transaction.

## COMPLETE / NEGATIVE

Controller cleanly republishes the original `03F4` value and does not adopt the requested value.

## COMPLETE / INCONCLUSIVE

Use for:

- timeout;
- unexpected page sequence;
- stale cache;
- unknown/ambiguous controller response;
- extra word changes;
- parser/RX fault during the attempted semantic transaction;
- evidence that does not cleanly distinguish acceptance from rejection.

## SUPERSEDED / NOT RUN

Use if a replacement ATEC experiment is prepared before the old one is run.

Never rewrite PREPARED history as though a later result was known earlier.

---

# 17. Safety constraints for future ATEC work

Before any new write target or new transmitted payload, state:

- slave/address/page;
- known current value if available;
- source of mapping;
- exact controlled change from previous experiment;
- expected effect;
- plausible unintended effects;
- rollback/recovery plan;
- positive criterion;
- negative criterion;
- abort criterion.

Always prefer:

- passive capture before active emulation;
- exact captured frame shapes;
- one unknown variable at a time;
- full-page provenance;
- one-word semantic delta;
- exact controller republish verification;
- DE LOW fail-closed handling.

Do not:

- scan broad unknown register ranges;
- write arbitrary registers;
- infer writeability from read mappings;
- infer ATEC semantics from XTR alone;
- infer XTR semantics from ATEC alone;
- respond to unexpected traffic unless the experiment explicitly tests it;
- invent an FC17 transform;
- treat a standard FC16 address/count ACK as proof that a semantic setting was accepted.

---

# 18. Known uncertainty / research priorities

Priority 1 — **run ATEC-EXP1 safely**

First establish whether stage-40 runtime and manual settings snapshot work on the target ATEC.

Priority 2 — **resolve 0708 idle/lifecycle fields**

Compare actual target responses against:

- all-zero ATEC-EXP1 idle reply;
- genuine Eco5 `W4=0001` steady-state frames;
- observed W4 countdown/state values.

Do not change more than one mailbox field at a time.

Priority 3 — **confirm 03F4 write path**

One +1 or -1 °C test, then restore.

Priority 4 — **only after EXP1 is closed, consider another field**

`0x041D` DHW Start is a candidate because of external mapping, but it must not be promoted to writable before a dedicated local ATEC experiment.

Priority 5 — **FC17/session path**

Only revisit after more capture-derived evidence or a testable transform hypothesis exists. Two challenge/response examples are insufficient for general emulation.

---

# 19. Evidence classification snapshot

## OBSERVED FACTS — genuine external ATEC/Eco captures

- controller polls `0x0F:0708/count6`;
- 0708 mailbox values correlate with desired-page pulls and config refreshes;
- `W1=0001` precedes FC03 `03E8/count14`;
- `W1=0008` precedes FC03 `042E/count15`;
- `03E8/count14` desired-page round trips occur;
- `03F4` changes in those captured round trips;
- controller later republishes the page by FC16;
- broad settings/configuration page exports occur;
- recurring runtime page families occur;
- startup FC17 approval exchanges occur in at least two successful sessions.

## STRONG CONCLUSIONS

- native Online/DCM setting changes are page-oriented, not best modeled as arbitrary direct register writes;
- `03F4` is strongly supported as room thermostat/setpoint for this ATEC/DHP-AQ-family path;
- exact controller republish is the correct semantic acceptance signal to watch.

## HYPOTHESES

- ATEC-EXP1 can safely replace the absent native responder on the target system without an FC17 session response;
- the chosen ATEC selector can be reused on that target;
- six-zero 0708 idle response is sufficient for this target/context;
- the target controller will adopt the requested `03F4` change through this emulator.

## UNKNOWNS

- W0 exact meaning;
- W4/W5 semantics;
- FC17 challenge-response transform;
- general hot-rejoin/session rules;
- portability across ATEC/iTec Eco/DHP-AQ firmware revisions;
- writeability of `0x041D`;
- queue behaviour on ATEC before live testing.

---

# 20. Files to read before changing ATEC code

Minimum set:

```text
Research/THERMIA_PROJECT_STATE.md
Research/Atec/AI_HANDOVER.md
Research/Atec/README.md
Research/Atec/thermia_atec_waveshare_atec_exp1_queued_room_setpoint.yaml
Research/EXTERNAL_ITEC_ECO5_FULL_CAPTURE_ANALYSIS.md
```

When a question depends on exact bus behaviour, go back to the raw capture files instead of relying on this summary.

If any source conflicts with raw capture evidence, prefer the raw capture.

If a new user-supplied live ATEC result conflicts with this handover, preserve the old observation historically and update the current interpretation rather than rewriting history.

---

# 21. Immediate next action

**Do not prepare ATEC-EXP2 yet.**

ATEC-EXP1 is still **PREPARED / NOT RUN**.

The next action is to obtain the first live ATEC-EXP1 log and classify:

1. passive preflight;
2. stage-40 runtime;
3. settings snapshot;
4. only if those are clean, one bounded `03F4` write and restore.

After that result is supplied:

- separate Observed facts / Strong conclusions / Hypotheses / Unknowns;
- record negative or inconclusive evidence as carefully as positive evidence;
- update this handover and the ATEC README if understanding changes;
- update the main canonical research files only where the result materially affects the wider Thermia protocol model.
