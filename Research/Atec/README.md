# Thermia ATEC / DHP-AQ experimental path

Last updated: **2026-10-02**

> **ATEC-EXP1 status: PREPARED / NOT RUN**
>
> This folder is a separate ATEC/DHP-AQ side branch of the Thermia reverse-engineering project. It is not the XTR canonical experiment series and it is not a production integration.

Current experimental implementation:

[`thermia_atec_waveshare_atec_exp1_queued_room_setpoint.yaml`](./thermia_atec_waveshare_atec_exp1_queued_room_setpoint.yaml)

Machine-oriented continuation notes:

[`AI_HANDOVER.md`](./AI_HANDOVER.md)

Strict passive build:

[`../../Read-only/ATEC/thermia_atec_waveshare_readonly_v01.yaml`](../../Read-only/ATEC/thermia_atec_waveshare_readonly_v01.yaml)

## Goal

The ATEC branch investigates the native Thermia/Danfoss Online/DCM path on the ATEC/DHP-AQ family.

ATEC-EXP1 tests one bounded semantic target:

`0x03F4` / decimal 1012 / page `03E8` word 12 / room thermostat-setpoint candidate.

The experiment does **not** perform arbitrary register writes. It reproduces only capture-backed page-oriented traffic.

## Source discipline

For ATEC wire behaviour, prefer:

1. raw ATEC/Eco gateway captures;
2. a new live ATEC result supplied by the user;
3. current main project canonical state/findings;
4. genuine Online/DCM-family captures;
5. Discussion #143 and other external interpretation;
6. cross-model XTR mappings;
7. speculation.

Do not promote an XTR-local result to proven ATEC behaviour without an ATEC confirmation.

## Primary captures

- `itec_eco5_gateway_20260926.log`
- `itec_eco5_gateway_20260928.log`

Additional genuine Online/DCM-family captures available in the project:

- `thermia_capture_20260924_210001(1).log`
- `thermia_capture_20260925_071517.log`
- `thermia_capture_20260925_090209.log`
- `thermia_capture_20260925_090550.log`

External supporting discussion:

- [klejejs/ha-thermia-heat-pump-integration Discussion #143](https://github.com/klejejs/ha-thermia-heat-pump-integration/discussions/143)

## 2026-10-02 raw-log recheck

The two primary gateway logs were reparsed directly.

### 0708 mailbox

Combined paired `0x0F FC03 0708/count6` replies: **264**.

Exact six-zero replies:

- 155/183 in the 2026-09-26 log;
- 42/81 in the 2026-09-28 log;
- **197/264 combined**.

Therefore:

```text
0000 0000 0000 0000 0000 0000
```

is well supported as the **dominant steady-state idle reply**, but not as a universal lifecycle state.

Transient fifth-word/W4 values also occur, including raw big-endian values `0x0100`, `0x03DC`, `0x03D8`, `0x03D0`, `0x038C`, `0x0380`, `0x0300`, `0x0200`, and `0x0000`.

The exact captured `03E8` desired-page selector is:

```text
0000 0001 0000 0001 0000 0000
```

A separate captured `042E` desired-page selector is:

```text
0000 0008 0000 0008 0000 0000
```

This reinforces the page-oriented model: W1 behaves as desired-page/PULL selection while W2:W3 carry current-page PUSH/refresh selection.

### 03E8/count14

The two gateway logs contain **216** controller FC16 `03E8/count14` pages.

There are only two unique controller payloads in that set:

- dominant `03F4=20`;
- one republished `03F4=30`.

The captured desired-page transaction changes only word 12 / `03F4`, then the controller republishes that page.

Discussion #143 independently identifies decimal 1012 / `0x03F4` as the room thermostat field.

This remains the strongest ATEC-EXP1 semantic target.

### Other directly observed page shapes

Exact controller FC16 shapes repeatedly present in the ATEC/Eco logs include:

- `0410/count22`
- `042E/count15`
- `0442/count13`
- `0546/count20`

Selected observations:

- `041D=39` in the captured `0410` page; Discussion #143 maps decimal 1053 / `0x041D` to DHW Start.
- `042E/count15` has three observed payload states; `042E` changes 1→0 and `042F` changes 0↔1.
- `0442/count13` is stable in the two primary captures and numerically matches the later XTR-proven cooling page layout.
- `0546/count20` is stable with `0553=2` and `0559=0`.

Later XTR work locally proved `0553` as Operation Mode and strongly supports `0559` as Link Integration. Public Online/DCM evidence uses the same register indexes.

On ATEC these remain cross-model/capture-backed candidates until locally correlated. The read-only ATEC YAML exposes selected candidates passively; ATEC-EXP1 does **not** add new write targets for them.

### FC17 approval/session traffic

Across the two primary gateway logs:

- exact `071C/0730` challenges: **163**
- exact 16-byte FC17 responses: **6**
  - 2 in the 2026-09-26 log
  - 4 in the 2026-09-28 log

This materially strengthens the conclusion that FC17 is part of session establishment.

It still does not reveal a general challenge-response transform.

ATEC-EXP1 therefore keeps `0x0F FC17` **capture-only / NO TX**.

The current XTR branch has since locally proven guarded native DCM session recovery through EXP386. That is useful architectural evidence, but the XTR R1 permission guard is not automatically transferable to ATEC and is deliberately not imported here.

## ATEC-EXP1 controlled experiment

### Hypothesis

With the native Online/DCM responder absent, the ATEC/DHP-AQ controller can be serviced on logical endpoint `0x0F` using only exact frame shapes observed in the supplied captures, and a fresh `03E8/count14` page can be changed at exactly `03F4` through the captured desired-page mechanism.

### Exact controlled semantic variable

Only:

`0x03F4` / page word12 / room setpoint.

No other setting is part of ATEC-EXP1.

### Desired-page flow

```text
controller -> 0x0F FC03 0708/count6
emulator   -> 0000 0001 0000 0001 0000 0000

controller -> 0x0F FC03 03E8/count14
emulator   -> complete cached 03E8 page with only 03F4 changed

controller -> 0x0F FC16 03E8/count14
emulator   -> standard address/count ACK

decision   -> compare controller republish against cached original + target
```

The ACK is transport-level only. The controller republish is the semantic acceptance signal.

## Safety

ATEC-EXP1:

- sends nothing for the first 10 seconds;
- stops if a pre-existing `0x0F` responder is seen;
- stops on later peer-response evidence;
- stops on parser resync or RX-buffer-drop delta;
- leaves unknown `0x0F` traffic capture-only;
- leaves all FC17 traffic capture-only;
- requires a fresh controller-originated `03E8/count14` cache <=60 s;
- reconstructs the desired page from that exact cache;
- allows only word12 to differ;
- disables semantic writes after a republish mismatch;
- uses one pending request maximum and latest-intent-wins;
- waits at least 2 seconds after a completed transaction before dispatching another.

## Manual settings snapshot

**ATEC Request Settings Snapshot** arms one exact captured broad refresh response:

```text
0000 0000 FFFF 867F 03DF 0000
```

This asks the controller to export the known settings page family through `06F4`.

It does not inject setting values, but it is still an active gateway-emulation action because the ESP responds and ACKs known page shapes.

## First live run

Do not begin with a room write.

1. Boot and leave controls untouched during passive preflight.
2. Require:
   ```text
   PREFLIGHT_PASSED peer=0 busFresh=1 ENTER_STAGE40 DE=LOW
   ```
3. Observe clean runtime.
4. Press **ATEC Request Settings Snapshot**.
5. Require:
   ```text
   SETTINGS_SNAPSHOT_COMPLETE
   ```
6. Record the current cached room setpoint and any unknown `0x0F` traffic.
7. Only if clean, request a **1 °C** room-setpoint change.
8. Wait for one terminal result.
9. If positive, restore the original value using the same path.

Do not stress-test the queue in the first run.

## Result criteria

**COMPLETE / POSITIVE**

Controller republishes `03E8/count14` with the requested `03F4`, every other word matches the cached original, and peer/resync/drop counters remain clean.

**COMPLETE / NEGATIVE**

Controller cleanly republishes the original `03F4` unchanged.

**COMPLETE / INCONCLUSIVE**

Timeout, stale cache, unexpected page sequence, ambiguous republish, extra changed word, peer evidence, or parser/RX integrity fault.

Until a live target log is supplied, the experiment remains **PREPARED / NOT RUN**.

## Read-only branch

For passive monitoring use:

`Read-only/ATEC/thermia_atec_waveshare_readonly_v01.yaml`

The 2026-10-02 passive refresh adds Candidate diagnostics for selected fields in `0410`, `042E`, `0442`, and `0546` while preserving strict RX-only operation.
