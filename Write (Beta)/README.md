# Thermia iTec XTR M — Write (Beta)

> [!WARNING]
> **Active control software.** This build transmits on the Thermia internal RS485 bus and can change heat-pump settings. It has been locally tested only on the documented Thermia iTec XTR configuration. Verify wiring and safeguards and do not assume cross-model compatibility.

This folder contains the active native-control build for the tested XTR M. Read-only remains the conservative choice when control is not required.

> [!WARNING]
> **Read the install instruction.** After flashing the ESP you will need to restart your Thermia heat pump, getting a stable session is still a bit tricky

## Known issues
- Some limits are still incorrect, if the value is outside of the limits the write will not be accepted.
 

## Current file

`thermia_itec_xtr_m_waveshare_write_beta_v4_1.yaml`

Write Beta v4.1 keeps the **EXP381B COMPLETE / POSITIVE** production/UI baseline and the seven **EXP383 TEST controls**, and adds the session/write-stability work from EXP386–EXP388.

Current evidence status:

- **EXP386 — COMPLETE / POSITIVE:** guarded native DCM controller-restart recovery is locally confirmed end-to-end.
- **EXP387 — COMPLETE / POSITIVE:** the delayed-`0708` semantic re-arm is locally confirmed; Room Setpoint writes recover after the mailbox wait instead of being permanently disabled.
- **EXP388 — RUNNING / PARTIAL:** two consecutive Thermia controller restarts recovered successfully without rebooting the ESP, and semantic Room Setpoint control remained functional. The additional pre-semantic/refresh-only cancellation branches are present but have not yet been independently live-exercised.
- **EXP383 — PREPARED / NOT RUN:** the seven TEST mappings are still not promoted to locally proven behavior.

Important distinction:

- the established controls listed as **PROVEN** below have local XTR M write evidence;
- entities containing **TEST** are only **STRONGLY SUPPORTED** mappings;
- publishing them in v4.1 does **not** promote them to proven protocol behavior;
- session-stability evidence does not validate EXP383 semantic mappings.

Write Beta v4.0 has been moved to [old versions](./old%20versions/) and is the direct rollback point for the v4.1 session-stability changes. The older v3.0 build remains useful as a pre-EXP383 rollback point.

## Native DCM session/recovery status

The v4.1 session path keeps the proven EXP386 cold-start sequence and adds EXP387/EXP388 recovery hardening.

The confirmed sequence is:

```text
stage40
  -> non-permitted 071C/0730 challenges: NO TX, keep listening
  -> >=5 s complete bus silence
  -> cold-start recovery
  -> BOOT_RETURN
  -> A80E=0000 / A80F=0005
  -> exact 071C/0730
  -> one proven R1
  -> ordered FC16 initial sync through 06F4
  -> fresh runtime FC16 ACK + 0708 idle reply
  -> persistent runtime qualified
  -> recovery latch re-armed only after RECOVERY_POSITIVE
```

In the EXP388 run, this full sequence completed twice in succession after two separate controller restarts while the ESP remained powered. The second recovery reached `RECOVERY_POSITIVE success=2 ... recoveryRearmed=1`, with parser resync and RX-drop counters still clean.

v4.1 also treats a genuine controller restart as an authority boundary. In recoverable pre-semantic or refresh-only states, unconfirmed queued intents are cancelled and semantic caches are invalidated before the new session is built. If a semantic selector/page transaction is already in-flight, recovery remains fail-closed. The cancellation paths beyond the idle case are still **not independently live-confirmed**.

Do not treat every `071C/0730` challenge as permission to transmit. The R1 replay remains restricted to the proven cold-start guard.

## Proven write scope

The following controls are locally confirmed writable through the native controller-owned page mechanism.

### Heating — `03E8/count14`

| Home Assistant control | Register | Range used in v4.1 | Evidence |
|---|---:|---:|---|
| 02 Heating \| 00 Room Setpoint | `0x03F4` | 10..30 °C | PROVEN |
| 02 Heating \| 01 Heating Curve | `0x03E8` | 22..56 | PROVEN |
| 02 Heating \| 02 Minimum | `0x03E9` | 20..40 °C | PROVEN |
| 02 Heating \| 03 Maximum | `0x03EA` | 40..85 °C | PROVEN |
| 02 Heating \| 04 Curve Correction +5 | `0x03EB` | -5..+5 | PROVEN |
| 02 Heating \| 05 Curve Correction 0 | `0x03EC` | -5..+5 | PROVEN |
| 02 Heating \| 06 Curve Correction -5 | `0x03ED` | -5..+5 | PROVEN |
| 02 Heating \| 07 Heating Stop | `0x03EE` | implementation bound 0..22 °C | PROVEN |
| 02 Heating \| 08 Reduced Temperature | `0x03EF` | 10..30 °C | PROVEN |
| 02 Heating \| 09 Room Factor | `0x03F0` | 0..4 | PROVEN |

### Hot water / Heating service — `042E/count15`

| Home Assistant control | Register | Evidence |
|---|---:|---|
| 03 Hot Water \| 01 Enabled | `0x042E` | PROVEN |
| 03 Hot Water \| 02 Mode | `0x042F` | write path PROVEN; not every enum individually exercised |
| 02 Heating \| 20 Startup HT | `0x0433` | PROVEN |
| 02 Heating \| 21 Heating Time | `0x0434` | PROVEN |

### Cooling — `0442/count13`

| Home Assistant control | Register | Evidence |
|---|---:|---|
| 04 Cooling \| 01 Enabled | `0x0442` | PROVEN |
| 04 Cooling \| 02 Desired Temperature | `0x0443` | PROVEN |
| 04 Cooling \| 03 Active Above | `0x0445` | PROVEN; dynamic minimum `max(10 °C, Heating Stop + 3 K)` |
| 04 Cooling \| 04 Cooling Time | `0x0449` | PROVEN |
| 04 Cooling \| 05 Room Sensor | `0x044C` | PROVEN |
| 04 Cooling \| 06 Room Hysteresis Low | `0x044D` | PROVEN; raw/10; 0.5..5.0 |
| 04 Cooling \| 07 Room Hysteresis High | `0x044E` | PROVEN; raw/10; 0.5..5.0 |

### Operation — `0546/count20`

| Home Assistant control | Register | Evidence |
|---|---:|---|
| 01 Operation \| 01 Mode | `0x0553` | PROVEN by EXP380; not every enum value individually exercised |

## EXP383 TEST controls

These seven controls are fully wired into the existing native semantic-write engines but remain **STRONGLY SUPPORTED / TEST** until local XTR M validation.

| Home Assistant control | Register | Current interpretation | Current implementation |
|---|---:|---|---|
| 03 Hot Water \| 03 **TEST** Top-up | `0x0430` | Hot Water TOP_UP | switch 0/1 |
| 04 Cooling \| 08 **TEST** Hysteresis | `0x0444` | INFORMATION Cooling Hysteresis | 0.0..12.0 K, step 0.1, tentative raw×10 |
| 04 Cooling \| 09 **TEST** Configuration | `0x0446` | SERVICE Cooling type | Uit / Actieve koeling / Geïntegreerd in WP |
| 04 Cooling \| 10 **TEST** Stop Threshold | `0x0448` | SERVICE Cooling STOP threshold | raw 0..100 |
| 04 Cooling \| 11 **TEST** Max Start Temperature | `0x044A` | MAX_STARTTEMP | 5..55 °C; guarded against current Min Stop |
| 04 Cooling \| 12 **TEST** Min Stop Temperature | `0x044B` | MIN_STOPTEMP | 5..55 °C; guarded against current Max Start |
| 01 Operation \| 02 **TEST** Link Integration | `0x0559` | Link Integration | Light / System |

### Test order

Test one new candidate at a time, use the smallest reversible change, confirm the Thermia-side semantic effect, then roll it back before moving to the next candidate.

Recommended order:

`0430 → 0444 → 0446 → 0448 → 044A → 044B → 0559`

`0559 Link Integration` is intentionally last. Changing the integration mode may plausibly affect the Online/DCM-style session itself. If the session or normal bus behavior changes unexpectedly after this test, stop and do not retry automatically.

## Native write model

The implementation does not behave like an arbitrary second Modbus master writing controller registers directly. It emulates the native page-owned Online/DCM path.

For each controlled page:

```text
fresh authoritative controller FC16 page
    ↓
current-page selector if refresh is needed
    ↓
desired-page selector
    ↓
controller FC03 reads that exact page from the emulated 0x0F side
    ↓
ESP returns the full fresh page with exactly one selected word changed
    ↓
controller FC16 republishes the page
    ↓
success only when target matches and extraDeltaWords = 0
```

The mechanism is locally proven on:
- `03E8/count14`
- `042E/count15`
- `0442/count13`
- `0546/count20`

A standard ACK or a transmitted desired page by itself is not considered semantic success.

## Home Assistant behavior

Configuration controls are grouped in the Thermia-manual order:

1. Operation
2. Heating
3. Hot Water
4. Cooling

The normal read sensors remain controller-authoritative.

During an active or queued semantic write, Configuration controls may temporarily retain the user's desired value while the controller catches up. A successful controller republish makes it authoritative. A failed transaction rolls the control back to the last confirmed value where possible.

The exact entity catalogue is maintained in:

[Research/HOME_ASSISTANT_ENTITIES.md](../Research/HOME_ASSISTANT_ENTITIES.md)

## Safety model

The v4.1 build retains the existing fail-closed guards and adds session-recovery hardening:

- authoritative current page required before semantic TX;
- one selected word changed per semantic transaction;
- exact expected page/count only;
- exact controller republish required;
- `extraDeltaWords=0` required for success;
- one active semantic transaction at a time;
- queued desired-state handling is serialized;
- parser/RX integrity changes fail closed;
- unexpected peer responder/session traffic fails closed;
- no automatic semantic retry after failure;
- driver-enable remains LOW outside guarded TX;
- controller-session recovery remains separately guarded;
- after a fully qualified recovery, the recovery latch is re-armed for a later independent controller restart;
- a recoverable controller-loss boundary cancels unconfirmed intents and invalidates semantic caches rather than replaying stale work;
- selector/page-in-flight semantic states still fail closed;
- the fixed challenge replay is only locally validated behavior, not the recovered native challenge-response algorithm.

For the EXP383 candidate controls, add this rule:

> **Do not use simultaneous candidate changes as the first validation. Test one TEST entity at a time and correlate the physical/front-panel effect.**

## EXP383 result classification

A candidate becomes locally PROVEN only when both are true:

1. the controller republishes the exact target with no unrelated page changes; and
2. the observed Thermia behavior/menu value matches the expected semantic field.

Possible classifications:

- **COMPLETE / POSITIVE** — exact republish and correct semantic effect;
- **COMPLETE / NEGATIVE** — controller keeps/rejects the original selected value without unrelated changes;
- **COMPLETE / INCONCLUSIVE** — exact transport behavior is seen but the semantic effect is ambiguous, or unexpected session/page behavior occurs.

Do not promote a candidate solely because the FC16 republish accepted the raw word.

## Tested hardware and wiring

The YAML targets the Waveshare ESP32-S3-RS485-CAN / ESP32-S3-RS485-CAN-U used during the research.

For the tested isolated setup:

| Thermia RJ45 | Waveshare |
|---|---|
| pin 1 — RS485 A | A+ |
| pin 3 — RS485 B | B- |
| pin 5 — bus reference | not connected |
| pins 7/8 — +12 V | not connected |

Power the Waveshare separately over USB-C.

Write build GPIO:
- GPIO18 = RX
- GPIO17 = TX
- GPIO21 = DE/direction

Leave the Waveshare **120 Ω termination jumper open/off** when attaching to the existing Thermia bus.

Bus parameters:

```text
Modbus RTU
9600 baud
8 data bits
Even parity
1 stop bit
```

## Installation

This section describes the setup that has actually been used for the XTR M research build. It is not a generic Thermia wiring guide.

### 1. Hardware

The tested board is a **Waveshare ESP32-S3-RS485-CAN / ESP32-S3-RS485-CAN-U**. Power the board separately over USB-C; Powering it from the Thermia RJ45 connector is untested and may not work.

Tested connection:

| Thermia RJ45 | Waveshare |
|---|---|
| pin 1 — RS485 A | A+ |
| pin 3 — RS485 B | B- |
| pin 5 — bus reference | not connected in the tested setup |
| pins 7/8 — +12 V | not connected |

In my test I leave the Waveshare **120 Ω termination jumper open/off** when joining the existing Thermia bus, 
You will need to open the Waveshare and change the position of the jumper cap just above the A/B connector.

Do not disconnect the room sensor or other normal Thermia bus participants for this installation.

### 2. Add the YAML to ESPHome

Copy:

`thermia_itec_xtr_m_waveshare_write_beta_v4_1.yaml`

into your ESPHome configuration directory.

The successful EXP386/EXP388 session-recovery runs were made in the same locally tested ESPHome 2026.9.x environment used during this research. This is observed test context, not a declared minimum-version requirement.

### 3. Configure secrets

The YAML expects these secrets:

```yaml
wifi_ssid: "..."
wifi_password: "..."
thermia_api_encryption_key: "..."
thermia_ota_password: "..."
thermia_fallback_password: "..."
```

Create/update your ESPHome `secrets.yaml` with your own values. Do not commit real credentials to this repository.

### 4. Validate and flash

Run ESPHome validation/compile in your own environment and resolve any board/framework differences before flashing.

For a new board, a first USB flash is the conservative option. Once ESPHome API/OTA access works reliably, later builds can be installed OTA.

After flashing, verify that:
- the ESP connects normally;
- read-only Thermia entities continue updating;
- DE is LOW outside guarded transmissions;
- parser resync and RX-drop counters do not start increasing unexpectedly.

Do **not** change any Home Assistant write control yet.

### 5. Establish or recover the native DCM session

If the controller already has a qualified session, the ESP can remain in persistent stage40.

For the locally validated fresh-session recovery procedure:

1. Keep the ESP powered and running.
2. Start the ESPHome log.
3. Power-cycle/restart the Thermia controller once using the same normal controller power procedure you would otherwise use.
4. Leave the ESP powered during the controller restart.
5. Watch for the recovery chain.
6. Once `RECOVERY_POSITIVE` is reached, the recovery latch is re-armed. A later independent controller restart can use the same guarded path again without rebooting the ESP.

Expected successful markers include:

```text
RECOVERY_INTENTS_CANCELLED
BUS_LOSS_TO_COLD_START
RECOVERY_ARMED
BOOT_RETURN
STATE_GUARD A80E=0000 A80F=0005
TX_INTENT ... R1
TX_EXECUTED ONE-SHOT R1
03E8_ACK_TX_EXECUTED
...
INITIAL_SYNC_COMPLETE
RUNTIME_FC16_ACK_EXECUTED
RECOVERY_POSITIVE ... recoveryRearmed=1
COMPLETE / POSITIVE / fresh controller session recovered / recovery re-armed
```

The exact intermediate FC16 pages form the existing ordered native initial-sync chain and finish at `06F4/count19`.

A challenge outside the proven guard, for example while `A80E=0008 / A80F=0032`, should be logged as guard-wait/capture-only with **NO TX**. Do not weaken that guard to make activation happen sooner.

### 6. Verify runtime before using controls

Before changing settings in Home Assistant, confirm:
- `Thermia Write Persistent Runtime Active` is ON;
- the status reaches a positive/qualified stage40 state;
- at least one fresh runtime FC16 has been ACKed;
- at least one `0708` idle reply has been observed;
- after a recovery, `RECOVERY_POSITIVE ... recoveryRearmed=1` is present;
- parser/RX integrity remains clean.

If the build reports STOP, ABORT, REFUSED, stage 99, unknown runtime traffic, peer responder activity, parser resyncs or RX drops, do not use semantic controls until the cause is understood.

### 7. Test control conservatively

First use an already **PROVEN** control and make the smallest reversible change. Wait for the exact controller republish/confirmation before issuing another change.

The seven EXP383 controls containing **TEST** are still **PREPARED / NOT RUN** as semantic validation experiments. Test them only one at a time and correlate both:
1. the exact controller republish with no unrelated delta; and
2. the actual Thermia/front-panel semantic effect.

Do not start with `0559 Link Integration`; keep that candidate last because it may affect the Online/DCM-style session itself.

### 8. Rollback

If normal bus behavior does not recover or you want a passive setup, flash one of the repository's [Read-only](../Read-only/) configurations.

For an active-write rollback, v4.0 is archived in [old versions](./old%20versions/) and is the direct pre-v4.1 baseline. The older v3.0 write build remains the pre-EXP383 rollback point. The read-only build is the conservative fallback when active control is not required.

## Recovery / stop criteria

Stop active testing if:
- normal bus updates become abnormal;
- parser resync/RX-drop counters change unexpectedly;
- another responder appears;
- the controller requests an unexpected page/count;
- exact republish does not occur;
- `extraDeltaWords` is non-zero;
- the semantic effect does not match the candidate;
- Link/Online session behavior changes unexpectedly.

For conservative rollback, install one of the [Read-only](../Read-only/) builds or the previous known-good write baseline.

Do not use controller power cycling merely to force a failed write transaction.

## Evidence trail

Canonical project state and experiment evidence:

- [THERMIA_PROJECT_STATE.md](../Research/THERMIA_PROJECT_STATE.md)
- [EXPERIMENT_LOG.md](../Research/EXPERIMENT_LOG.md)
- [PROTOCOL_FINDINGS.md](../Research/PROTOCOL_FINDINGS.md)
- [HOME_ASSISTANT_ENTITIES.md](../Research/HOME_ASSISTANT_ENTITIES.md)
- [EXP382_OFFLINE_GAP_ANALYSIS.md](../Research/EXP382_OFFLINE_GAP_ANALYSIS.md)

## Scope discipline

This folder remains **Beta**, even though the established controls are locally functional. STRONGLY SUPPORTED mappings remain explicitly named **TEST** until local validation is recorded.

The long-term goal remains a stable local integration that follows the native Thermia/Danfoss Online/DCM architecture rather than relying on speculative direct-register writes.
