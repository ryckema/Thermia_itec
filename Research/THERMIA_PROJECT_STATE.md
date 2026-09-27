# THERMIA PROJECT STATE

## Authoritative current state — 2026-09-27 — EXP256 COMPLETE / ACTIVE STRONG POSITIVE

- Last completed experiment: **EXP256 — COMPLETE / ACTIVE STRONG POSITIVE**.
- Hypothesis tested: repeat the already-tested one-shot Eco 5 R1 response and enumerate the complete local post-R1 `0x0F FC16/FC03` distribution.
- One exact R1 response was transmitted at the first local approval request, **+1245 ms after BUS_RETURN**.
- Approval requests: **1 total; 0 retries after TX**.
- User-reported front-panel effect: the DHW/tank-side literal **`0` reappeared**; the VERSION screen showed **no change**.
- After `SUMMARY COMPLETE`, the front panel again raised the exact same alarm as EXP252: **`COMM. ERR ONLINE/LINK`**. This makes the incomplete Online/Link-session side effect reproducible across both R1 runs.
- No downstream emulation was provided: **0 FC16 ACKs, 0 FC03 responses, 0 second FC17 response**.

### EXP256 definitive post-R1 census

- `FC16 requests = 390`
- `FC16 ACKs = 0`
- `FC03 0708/count6 = 0`
- other `FC03 = 0`
- `peer17 = 0`
- `self_echo = 0`
- `s06 = 102`
- final state: `A80E=0028 A80F=000A AFDC=0010`
- post-BUS_RETURN parser resync delta: **0**
- post-BUS_RETURN RX drop delta: **0**
- DE returned LOW.

Complete FC16 family census in the EXP256 run:
- `04BA/count22`: **1** request, boot-only, before R1;
- `03E8/count14`: **389** requests, first **+1369 ms after BUS_RETURN / +124 ms after R1**, last **+419896 ms**, median inter-request interval about **1308 ms**;
- `04A6/count13`: **0**;
- `085F/count5`: **0**;
- no other FC16 family observed.

### Material protocol conclusion from EXP256

The EXP255-derived numerical hypothesis that R1 might merely suppress `085F/count5` while leaving `04A6/count13` intact is **rejected**. The earlier 582-vs-386 count coincidence was misleading.

R1 instead causes a much stronger state transition: immediately after the one-shot response, the controller enters the native `03E8/count14` FC16 synchronization stage and retransmits that first settings block continuously because EXP256 deliberately supplies no FC16 ACK. This reproduces the beginning of the acknowledged `0x0F` transfer state machine previously mapped in EXP137+, but now specifically **after the approval response**.

Therefore the strongest current interpretation is:
1. the R1 response is accepted far enough to terminate the `071C/0730` approval retry loop;
2. it advances the local XTR into a controller->Online/Link synchronization phase beginning at `03E8/count14`;
3. without the expected endpoint FC16 ACK, the controller stalls on that first synchronization block;
4. full Online/Link session establishment is still not proven; no FC03/mailbox phase was reached in EXP256.

The lack of VERSION-screen change is expected and not a negative discriminator: VERSION `EXP` metadata is the separate `0x06/AFD1` expansion-board path, while EXP256 acts only on the `0x0F` approval path.

### Safety / recovery after EXP256

The known R1 side effect is reproducible at least at the UI level (`0` at the DHW/tank icon). As planned, perform **one normal Thermia controller reboot after the EXP256 summary**. Do not run another active approval/sync experiment until the UI has returned to its normal state.

**EXP239 remains OPEN.**  
**EXP238 remains PARKED / NOT RUN.**

Next active candidate is not yet prepared. The highest-value controlled discriminator is likely a bounded post-R1 ACK of the already-proven exact `03E8/count14` FC16 request, with no ACK of any newly appearing block, to determine the first post-approval progression. This must be prepared as a separate experiment with explicit fail-closed guards.

## Authoritative current state — 2026-09-27 — EXP255 COMPLETE / EXP256 PREPARED

- Last completed experiment: **EXP255 — COMPLETE / VALID PASSIVE BASELINE**.
- Current prepared experiment: **EXP256 — ONE-SHOT R1 + FULL POST-R1 FC16/FC03 DIFFERENTIAL CENSUS — PREPARED / NOT RUN**.

### EXP255 definitive passive baseline

- approval requests: **63**
- first approval: **+1284 ms**
- last approval: **+265513 ms**
- median approval cadence: **4241 ms**
- FC16 requests: **582**
- FC16 ACKs: **0**
- FC03 requests: **0**
- FC03 responses: **0**
- parser resync delta: **0**
- RX drop delta: **0**
- TX disabled

Complete local passive FC16 families:
- `04BA/count22`: **4**, boot-only (+316..+3641 ms)
- `04A6/count13`: **383**, persistent (+4337..+419417 ms)
- `085F/count5`: **195**, persistent (+2265..+419542 ms)

No other 0x0F FC16 family and no FC03 request appears in the full seven-minute run.

The FC16 streams continue after the 63rd/final approval request: 219 FC16 requests occur after
+265513 ms, proving that normal FC16 runtime traffic is separate from the approval retry budget.

### New EXP252 / EXP255 differential hypothesis

EXP252 one-shot R1 had `fc16req=386` over the same seven-minute observation window.
EXP255 passive baseline has 582, a difference of **196**.

EXP255's `085F/count5` family alone contributes **195** requests. The remaining passive families
contribute **387**, almost exactly EXP252's 386 total.

This supports, but does not yet prove, the hypothesis that R1 selectively suppresses the normal
`085F/count5` family while leaving `04A6/count13` largely intact.

### EXP256 hypothesis

Repeat the already-tested EXP252 one-shot R1 response with the same fail-closed guards while logging
every FC16 and FC03 address/count. No downstream ACK or response is added.

Primary discriminator:
- disappearance/reduction of `085F/count5`;
- persistence of `04A6/count13`;
- or appearance of any new FC16/FC03 family.

Known recoverable side effect:
- previous R1 produced DHW-side `0` and `COMM. ERR ONLINE/LINK`;
- one normal controller reboot cleared both.
- EXP256 should be followed by one controller reboot immediately after its summary; do not wait for
  the communication alarm.

**EXP239 remains OPEN.**
**EXP238 remains PARKED / NOT RUN.**



## Authoritative current state — 2026-09-27 — EXP255 PREPARED / NOT RUN

- Last completed experiment: **EXP254 — COMPLETE / VALID PASSIVE POSITIVE**.
- Recovery confirmation from the user:
  - after the manual controller restart following EXP252,
  - `COMM. ERR ONLINE/LINK` cleared,
  - the DHW/tank-side `0` also cleared.
- Therefore EXP252 side effects were **recoverable by one normal controller reboot with no active
  responder**. Spontaneous self-clear without reboot remains untested.
- Current prepared experiment: **EXP255 — PASSIVE FULL 0x0F FC16/FC03 BASELINE CENSUS**.
- Reason for inserting EXP255 before another active R1 test:
  - EXP254 counted only exact `0870/count17` and `0708/count6`;
  - it did not map all local `0x0F FC16` and `FC03` start/count pairs;
  - without this baseline, an active post-R1 address census would be ambiguous.
- EXP255 is fully RX-only and records every `0x0F FC16` request and every `0x0F FC03` request after
  BUS_RETURN.
- Candidate after EXP255, if baseline is clean:
  **EXP256 — one-shot R1 + identical post-R1 FC16/FC03 census, no downstream ACKs/responses.**
- **EXP239 remains OPEN.**
- **EXP238 remains PARKED / NOT RUN.**


## EXP252/254 recovery clarification — 2026-09-27

The heat pump/controller was manually restarted after the `COMM. ERR ONLINE/LINK` alarm from EXP252.

Therefore EXP254 demonstrates **post-reboot recovery to the normal local XTR protocol baseline**.
It does **not** demonstrate that the alarm/session state would have cleared spontaneously without a
controller restart.

The following remain valid:
- EXP252 R1 suppressed all later approval retries in that boot;
- a DHW-side `0` appeared;
- `COMM. ERR ONLINE/LINK` appeared;
- after a subsequent controller restart with no active responder, EXP254 returned to the familiar
  63-request passive approval lifecycle with no `0870/count17` and no `0708/count6`.

UI recovery of the alarm and DHW-side `0` still requires explicit visual confirmation if it was not
recorded at the time.


## Authoritative current state — 2026-09-27 — EXP254 COMPLETE / VALID PASSIVE POSITIVE

- Last completed experiment: **EXP254 — COMPLETE / VALID PASSIVE POSITIVE**.
- EXP254 clean passive recovery summary:
  - approval requests: **63**
  - first request: **+1.283 s**
  - median cadence: **4.241 s**
  - last request: **+265.086 s**
  - exact `FC16 0870/count17`: **0**
  - peer FC16 ACK: **0**
  - exact `FC03 0708/count6`: **0**
  - `s06=107`
  - final state `A80E=0028 A80F=000A AFDC=0010`
  - `resync_delta=0`
  - `drop_delta=0`
  - TX disabled
- All complete passive retry runs (EXP248, 249, 251, 254) stop at exactly **63 requests**, despite
  differing cadence and elapsed duration. The fixed 63-attempt budget remains the leading model.
- With EXP254 median cadence, a nominal 64th request would fall around +269.327 s, before +270 s,
  but does not appear.
- **Material refinement of EXP252 interpretation:** the late A80E/AFDC fall-back is not R1-specific.
  EXP254 reproduces it passively at almost the same boot age:
  - A80E `0x28 -> 0x20` at ~+642.650 s in EXP254 vs ~+647.433 s in EXP252
  - AFDC `0x10 -> 0x00` at ~+646.459 s in EXP254 vs ~+651.106 s in EXP252
- Therefore the R1-specific evidence from EXP252 is now narrowed to:
  1. immediate suppression of all later approval retries;
  2. front-panel DHW-side `0`;
  3. `COMM. ERR ONLINE/LINK`.
- Exact `0870/count17` and `0708/count6` do not occur in the 7-minute local passive XTR baseline.
  Do not copy the reference ATEC/DHP-AQ `0870 -> 0708 -> sync` sequence onto XTR without direct
  local evidence.
- Next candidate: **EXP255 — one-shot R1 + post-R1 FC16/FC03 address census, no downstream ACKs**.
- Safety prerequisite before EXP255: user confirms that `COMM. ERR ONLINE/LINK` and the DHW-side `0`
  cleared after the EXP254 passive recovery reboot.
- **EXP239 remains OPEN.**
- **EXP238 remains PARKED / NOT RUN.**


## EXP254 provisional live result — 2026-09-27 — RUNNING

- EXP254 is behaving as intended: fully passive / RX-only.
- A genuine controller-off bus gap and BUS_RETURN were observed.
- After BUS_RETURN the local XTR returned to the known unanswered approval lifecycle:
  - first `071C/0730` request at +1.283 s;
  - 23 requests observed so far through +94.787 s;
  - recent cadence ~4.240 s.
- Controller state progression returned to the familiar pattern:
  - A80E `0x28 -> 0x00 -> 0x08 -> 0x28`;
  - A80F `0x0A -> 0x05 -> 0x0A`;
  - AFDC `0x10 -> 0x00 -> 0x10`.
- So far:
  - exact `0x0F FC16 0870/count17` requests: **0**;
  - exact `0x0F FC03 0708/count6` polls: **0**;
  - peer FC16 ACKs: **0**.
- This already supports clean recovery toward the local XTR baseline and shows that the reference
  ATEC/DHP-AQ `0870/0708` service cycle is not ordinary early local XTR baseline traffic.
- EXP254 remains **RUNNING** until `SUMMARY PASSIVE_RECOVERY_COMPLETE`.


## Authoritative current state — 2026-09-27 — EXP253 COMPLETE / EXP254 PREPARED

- Last completed experiment: **EXP253 — COMPLETE / OFFLINE POST-APPROVAL SESSION RECONSTRUCTION**.
- Last completed live-bus experiment: **EXP252 — COMPLETE / ACTIVE POSITIVE / COMM. ERR ONLINE/LINK SIDE EFFECT**.
- Current prepared experiment: **EXP254 — PASSIVE RECOVERY + 0870 BASELINE CENSUS — PREPARED / NOT RUN**.

### EXP253 material finding

Reference established Online/DCM captures show a concrete endpoint-coming-online transition:

1. controller repeatedly sends `0x0F FC16 0870/count17` with no reply;
2. controller repeatedly polls `0x0F FC03 0708/count6` with no reply;
3. endpoint first ACKs `0870/count17`;
4. endpoint then answers `0708` with `0000 0000 7FFF FFFF 0080 0007`;
5. controller immediately begins a broad FC16 synchronization burst (`03E8`, `03FC`, `0884`, ...),
   with each block ACKed by the endpoint.

In capture 090550 there are 31 unanswered `0870/count17` requests and 16 unanswered `0708` polls
before this transition.

Established idle/service captures show recurring `0708` responses ending in `...0006`, including
`0000 0000 0000 0000 077F 0006` and all-zero-like variants.

### EXP252 interpretation refined

EXP252's R1 is not simply ignored: it suppresses the local approval retries. However the ESP supplied
none of the downstream endpoint duties seen in the reference topology: no FC16 ACKs and no read-side
service/mailbox responses. The later `COMM. ERR ONLINE/LINK` is therefore consistent with an
**incomplete Online/Link endpoint/session**.

This does not prove that local XTR uses the same post-approval sequence as the reference ATEC/DHP-AQ
topology.

### Safety / next step

No further active response is approved until clean passive recovery is documented.

EXP254 is fully RX-only and will establish:
- whether the alarm and DHW-side `0` clear on a normal no-responder boot;
- whether local `0870/count17` is baseline traffic;
- whether any local `0708/count6` poll occurs without active endpoint behavior;
- whether the normal 63-attempt approval lifecycle returns.

**EXP239 remains OPEN.**
**EXP238 remains PARKED / NOT RUN.**


## Authoritative current state — 2026-09-27 — EXP252 COMPLETE / ACTIVE POSITIVE / ALARM SIDE EFFECT

- Last completed experiment: **EXP252 — COMPLETE / ACTIVE POSITIVE / SAFETY SIDE EFFECT OBSERVED**.
- One mismatched externally reported Eco 5 R1 response was transmitted exactly once at the first
  local XTR `071C/0730` approval request.
- Result:
  - approval requests: **1**;
  - retries after TX: **0**;
  - no second approval request for the complete 7-minute observation;
  - `peer17=0`;
  - controller FC16 requests: **386**;
  - peer FC16 ACKs: **0**;
  - `mailbox0708=0`;
  - other FC03 page reads: **0**;
  - parser resync after BUS_RETURN: **0**;
  - RX drops after BUS_RETURN: **0**;
  - DE returned LOW.
- **Strong conclusion:** R1 is not simply ignored. It terminates/suppresses the local approval retry
  state, but full DCM/Online approval is **not proven** because no downstream peer ACK/mailbox phase
  appears.
- New controller-visible side effects:
  - front-panel displayed a new literal `0` beside the DHW/tank icon;
  - after the experiment summary, A80E fell `0x28 -> 0x20 -> 0x00` and AFDC fell `0x10 -> 0x00`;
  - the user subsequently reported a front-panel alarm.
- Alarm text is now known: **`COMM. ERR ONLINE/LINK`**.
- **Safety hold:** no further active `0730` response experiments until a normal passive/no-responder
  boot is shown to restore normal operation. The alarm is specifically an Online/Link communication
  error, not currently evidence of a direct heating/DHW process fault.
- Next evidence required: verify that `COMM. ERR ONLINE/LINK` and the DHW-icon `0` clear after return
  to passive/no-responder operation.
- **EXP239 remains OPEN.**
- **EXP238 remains PARKED / NOT RUN.**


## EXP252 provisional UI observation — 2026-09-27

After the single R1 `0730` oracle response, the local Thermia front-panel display visibly shows a
literal `0` immediately beside/above the domestic-hot-water tank icon. The display otherwise reads
`KAMER`, `GEEN WARMTEVRAAG`, and `BEDRIJF AUTO`; no alarm/fault text is visible in the supplied photo.

This UI change is temporally associated with the one-shot R1 response and the immediate suppression
of further `071C/0730` approval retries, but its semantic meaning is **unknown**. It must not yet be
interpreted as `0 °C`, a changed DHW setpoint, or proof of successful DCM approval.

The visual formatting does not clearly show a temperature unit next to the `0`, so a status/index/
service indicator remains plausible.

Do not perform another active response test before the EXP252 run is complete and the display state
has been correlated with the final bus trace.


## Authoritative current state — 2026-09-27 — EXP252 PREPARED / NOT RUN

- Last completed experiment: **EXP251 — COMPLETE / VALID RX-ONLY POSITIVE**.
- Current prepared experiment: **EXP252 — ONE-SHOT 0730 APPROVAL ORACLE (Eco 5 R1) — PREPARED / NOT RUN**.
- EXP252 hypothesis: one externally reported genuine Eco 5 response, returned exactly once to the
  first local XTR approval request, will either be rejected with retries continuing or measurably
  alter the controller approval/session state.
- New active response target:
  - controller FC17 reads `0x0730..0x0737`;
  - test payload `R1 = 1691 A5F3 F8E8 D587 3892 4416 E8E6 A3D5`;
  - R1 belongs externally to `C1 = 63CE FB32 C6F4 1382 0879 9237 0CAC EEBA`;
  - local XTR input is an RTC/service image and does not match C1, so this is deliberately a
    mismatched cross-profile oracle test.
- Possible effects before test:
  - likely rejection / retries continue;
  - possible retry suppression or approval/session state change;
  - possible partial DCM sync;
  - persistent service/binding side effects unknown.
- Fail-closed guards require:
  - explicit HA arm;
  - real cold-boot bus gap and return;
  - first exact approval request only;
  - proven local RTC/service serializer;
  - input must not equal C1;
  - `A80E=0000`, `A80F=0005`;
  - no peer FC17 response;
  - no post-BUS_RETURN parser resync or RX drop before TX.
- TX latch closes before driver enable. There is exactly one `write_array()` path in the YAML.
- After R1, no further Thermia response is emitted: no retry, FC16 ACK, mailbox response or
  desired-state page response.
- GPIO17 TX is enabled only for EXP252. GPIO21 DE defaults LOW and is returned LOW after the frame,
  abort and final summary.
- **EXP239 remains OPEN.**
- **EXP238 remains PARKED / NOT RUN.**
- Do not run a second active response value in the same boot.


## Authoritative current state — 2026-09-27 — EXP251 COMPLETE / VALID RX-ONLY POSITIVE

- Last completed experiment: **EXP251 — COMPLETE / VALID RX-ONLY POSITIVE**.
- EXP251 final summary:
  - approval requests: **63**;
  - first request: **+1.287 s** after BUS_RETURN;
  - median cadence: **4.178 s**;
  - last request: **+261.347 s**;
  - final target-free silence: **80.044 s**;
  - peer FC17 16-byte responses: **0**;
  - controller FC16 requests: **424**;
  - peer FC16 ACKs: **0**;
  - `0x0F FC03 0708/count6` mailbox requests: **0**;
  - other FC03 page requests: **0**;
  - 0x06 polls: **87**;
  - final state: `A80E=0028 A80F=000A AFDC=0010`;
  - false stops: **0**;
  - parser resync delta: **1** at the boot-return edge;
  - RX drop delta: **0**;
  - TX: **DISABLED**.
- Comparison across complete cold boots:
  - EXP248: 63 requests, median 4.298 s, last +267.123 s;
  - EXP249: 63 requests, median 4.293 s, last +266.821 s;
  - EXP251: 63 requests, median 4.178 s, last +261.347 s.
- **Material protocol conclusion:** a simple fixed ~270 s deadline is now weakened. The **fixed
  63-attempt retry-budget model is the leading explanation** because the count remains invariant
  while cadence and total elapsed window change.
- At EXP251 cadence, nominal attempts 64 and 65 would fall at approximately +265.525 s and +269.703 s,
  both before +270 s, yet neither occurs.
- Ordinary controller FC16 requests are present without any approval response, peer FC16 ACK, or
  0708 mailbox. Therefore controller-originated FC16 traffic alone is not evidence of Online/DCM approval.
- No active `0730` response was sent, derived or approved.
- **EXP239 remains OPEN.**
- **EXP238 remains PARKED / NOT RUN.**
- Do not spend another live experiment on retry timing unless new evidence requires it.
- Candidate next step: one-shot active approval-oracle test using a single known external Eco 5
  response, but only after explicit approval because `0730..0737` remains semantically opaque.


## Authoritative current state — 2026-09-27 — EXP251 VALID STOP CANDIDATE / FINAL CONFIRMATION PENDING

- Last completed experiment: **EXP250 — COMPLETE / OFFLINE / NO TX**.
- Last completed live-bus experiment: **EXP249 — COMPLETE / VALID PASSIVE POSITIVE**.
- Current experiment: **EXP251 — VALID RX-ONLY RUN / STOP CANDIDATE OBSERVED / NOT YET FORMALLY COMPLETE**.
- EXP251 observed:
  - first approval request **+1.287 s** after BUS_RETURN;
  - **63 approval requests**;
  - median cadence **4178 ms**;
  - last request **+261.347 s**;
  - final monitored state `A80E=0028 A80F=000A AFDC=0010`;
  - no peer FC17 16-byte response;
  - no peer FC16 ACK;
  - no `0x0F FC03 0708/count6` mailbox request;
  - STOP_CANDIDATE after **20.044 s** approval silence while ordinary bus traffic remained alive;
  - one parser resync exactly at bus return; RX drops remained zero.
- **Material model change:** EXP248/249 had ~4.29 s median cadence and final requests at ~267 s,
  while EXP251 has a ~4.178 s median cadence and final request at **261.347 s**, yet all three runs
  still stop after exactly **63 requests**.
- A simple fixed ~270 s deadline from BUS_RETURN is therefore materially weakened.
- **Leading hypothesis is now a fixed 63-attempt retry budget**, with total retry-window duration
  determined by actual scheduler/bus cadence.
- At EXP251 cadence, nominal request 64 would be due around **+265.525 s** and request 65
  around **+269.703 s**, both before +270 s.
- No active `0730` response was sent, derived or approved.
- Formal EXP251 completion still requires the missing 60 s post-STOP_CANDIDATE tail /
  `SUMMARY SHADOW_COMPLETE`.
- **EXP239 remains OPEN.**
- **EXP238 remains PARKED / NOT RUN.**


## Authoritative current state — 2026-09-27 — EXP251 PREPARED / NOT RUN

- Last completed experiment: **EXP250 — COMPLETE / OFFLINE / NO TX**.
- Last completed live-bus experiment: **EXP249 — COMPLETE / VALID PASSIVE POSITIVE**.
- Current prepared experiment: **EXP251 — SHADOW DCM / APPROVAL HARNESS — PREPARED / NOT RUN**.
- EXP251 hypothesis: the iTec Online/DCM lifecycle can be implemented as a shadow state-machine with
  one deliberately unresolved opaque 16-byte `071C -> 0730` response boundary.
- Only experimental change: EXP249 retry-window instrumentation is replaced by lifecycle/classifier
  instrumentation. Known-good production functionality is preserved.
- EXP251 recognizes:
  - exact `0x0F FC17 read0730/count8 + write071C/count8` approval requests;
  - local XTR RTC/service consistency and reference-challenge Hamming distance;
  - unexpected peer 16-byte FC17 responses;
  - controller 0x0F FC16 requests and peer FC16 ACKs;
  - exact `0x0F FC03 0708/count6` mailbox polls;
  - other 0x0F FC03 page reads;
  - A80E/A80F/AFDC and 0x06 context.
- **No Thermia TX path exists in the EXP251 build:** GPIO17 TX is absent and GPIO21 DE is forced LOW.
- No Eco 5 response bytes are stored in the YAML; only the two source challenge values are used for
  Hamming-distance comparison.
- Experimental controls remain under Home Assistant Configuration and logs retain the red/brown
  convention.
- **EXP239 remains OPEN.**
- **EXP238 remains PARKED / NOT RUN.**
- No active `0730` response is approved.
- Do not move to an active one-shot oracle test until EXP251 has completed cleanly and been analysed.


## Authoritative current state — 2026-09-27 — EXP250 COMPLETE / OFFLINE

- Last completed experiment: **EXP250 — COMPLETE / OFFLINE 0730 RESPONSE-STRUCTURE CLASSIFICATION**.
- Hypothesis tested: the two externally reported genuine Eco 5 `0730..0737` responses behave more
  like one opaque 128-bit approval/authenticator value than eight independent status/control words.
- Across the two available genuine response blocks:
  - all 8/8 16-bit word positions change;
  - no response word position is fixed;
  - no common small Thermia status/control constants appear;
  - C->R Hamming distances are 65/128 and 62/128;
  - R1->R2 Hamming distance is 68/128.
- **Strong conclusion:** for emulator design, `0730..0737` should currently be treated as one opaque
  16-byte response blob. There is no evidence-backed per-word semantic map.
- This does not prove a specific cryptographic primitive and does not prove XTR M uses the same
  response function as the reported Eco 5.
- Safety consequence: the result weakens the 'eight independent flags' interpretation but does not
  make arbitrary replay safe. Persistent session/binding side effects remain unknown.
- No Thermia TX occurred in EXP250. Production functionality is unchanged.
- **EXP249 remains the last completed live-bus experiment.**
- **EXP239 remains OPEN.**
- **EXP238 remains PARKED / NOT RUN.**
- Preferred next step: build **EXP251 shadow DCM emulator/oracle harness** with TX disabled by default.
  Any later active one-shot `0730` replay requires explicit approval and must use only one response in
  one boot with immediate TX hard-disable afterward.


## Authoritative current state — 2026-09-27 — EXP249 COMPLETE / VALID PASSIVE POSITIVE

- Last completed experiment: **EXP249 — COMPLETE / VALID PASSIVE POSITIVE**.
- EXP249 repeated EXP248's RX-only cold-boot natural-stop trace with only one changed variable: a second controller cold boot.
- EXP249 result:
  - first target **+1.283 s** after BUS_RETURN;
  - **63 targets**;
  - median cadence **4293 ms**;
  - last target **+266.821 s**;
  - final monitored state `A80E=0028 A80F=000A AFDC=0010`;
  - `SUMMARY CONFIRMED_STOP` after **80.974 s** final target silence;
  - 87 observed 0x06 polls;
  - `false_stops=0`, `resync_delta=0`, `drop_delta=0`.
- EXP248 comparison:
  - first target was also +1.283 s;
  - target count was also 63;
  - last target was +267.123 s;
  - last-target difference is only **302 ms**;
  - final monitored state is identical;
  - meaningful early A80E/A80F/AFDC state transitions reproduce within **11 ms**.
- **Strong conclusion:** the unanswered local XTR `071C/0730` startup/service lifecycle is highly deterministic across repeated cold boots.
- A ~270 s fixed deadline remains the leading practical model, but a fixed 63-request budget is still equally compatible because cadence and phase are also nearly identical.
- Do **not** claim that 270.000 s is proven or that the mechanism is definitively time-based.
- No active `0730` response was sent, derived or approved.
- **EXP239 remains OPEN.**
- **EXP238 remains PARKED / NOT RUN.**
- Preferred next experiment: **EXP250 — passive cutoff-neighborhood raw-frame differential**, using the deterministic ~267 s stop to capture every CRC-valid bus frame around ~245–285 s and search for an externally visible event that suppresses the next target slot.


## Authoritative current state — 2026-09-27 — EXP249 PREPARED / NOT RUN

- Last completed experiment: **EXP248 — COMPLETE / VALID PASSIVE POSITIVE**.
- Current prepared experiment: **EXP249 — PASSIVE 071C/0730 STOP REPEATABILITY TRACE — PREPARED / NOT RUN**.
- EXP249 hypothesis: the EXP248 natural stop is governed primarily by a repeatable approximately 270 s startup/service window. A second otherwise-identical RX-only cold boot should reproduce the final target within one normal retry interval (~4.3 s) of EXP248's +267.123 s result.
- EXP248 comparison baseline:
  - first target +1.283 s after BUS_RETURN;
  - 63 targets;
  - median cadence 4.298 s;
  - last target +267.123 s;
  - monitored stop state `A80E=0028 A80F=000A AFDC=0010`;
  - confirmed target-free silence 80.793 s.
- **Only experimental variable:** one additional controlled Thermia/controller cold boot. All EXP248 observation thresholds and RX-only behavior are retained.
- EXP249 contains no Thermia TX path: GPIO17 TX remains unconfigured and GPIO21 DE is forced LOW.
- No ACK, `0730` response, scan, semantic write, setting change, room-sensor emulation or production-function change is introduced.
- Experimental controls remain under Home Assistant Configuration; experiment logs retain the red/brown convention.
- **EXP239 remains OPEN.**
- **EXP238 remains PARKED / NOT RUN.**
- No active `0730` response is approved.
- Do not mark EXP249 complete until the automatic `SUMMARY CONFIRMED_STOP` (or a clearly recorded censor/abort) is present in the returned log.


## Authoritative current state — 2026-09-27 — EXP248 COMPLETE / VALID PASSIVE POSITIVE

- Last completed experiment: **EXP248 — COMPLETE / VALID PASSIVE POSITIVE**.
- Hypothesis tested: the local XTR `0x0F FC17 read 0730/count8 + write 071C/count8`
  startup/service transaction retries for a finite unanswered window and then stops naturally.
- Attempt 1 was an intentional/accidental setup negative: armed at 14:55:38.670 but no controller
  power-cycle occurred; the >=6 s boot-gap guard correctly auto-aborted after 60 s. No protocol
  conclusion is drawn from that attempt.
- Attempt 2 is valid and complete:
  - ARM 14:57:25.491;
  - boot gap detected 14:57:53.961;
  - BUS_RETURN 14:58:01.042;
  - first target +1.283 s;
  - **63 targets total**;
  - last target **+267.123 s** with `A80E=0028 A80F=000A AFDC=0010`;
  - stable target cadence, median **4298.0 ms**;
  - STOP_CANDIDATE after 20.793 s target silence;
  - `SUMMARY CONFIRMED_STOP` with **80.793 s final silence**, **0 false stops**,
    **0 resync delta**, **0 RX-drop delta**, and **86 observed 0x06 polls**.
- Ordinary bus traffic remains alive after the final `071C/0730`; therefore the target stream
  stops naturally rather than disappearing because of bus loss.
- No A80E/A80F/AFDC transition coincides with the final target; monitored state stays
  `0028 / 000A / 0010`.
- No cadence slowdown/backoff is visible before the stop.
- Strong timing hypothesis: an approximately **270 s startup retry deadline**. The next target would
  normally be due around **271.421 s**, so a ~270 s deadline lies naturally
  between target 63 and the suppressed target 64. This is not yet proven from one run.
- No active `0730` response was sent, derived or approved. Production functionality is unchanged.
- **EXP239 remains OPEN** pending the external genuine iTec Eco 5 raw capture.
- **EXP238 remains PARKED / NOT RUN.**
- Preferred next experiment: **EXP249 — passive repeatability test of the ~270 s natural-stop
  deadline**, using the same RX-only instrumentation and one additional cold boot.



## Authoritative current state — 2026-09-27 — EXP248 VALID STOP CANDIDATE / CONFIRMATION TAIL MISSING

- Current experiment: **EXP248 — IN PROGRESS / VALID RX-ONLY RUN; natural-stop candidate observed, but the configured 60 s confirmation window is not fully present in the supplied log tail**.
- Hypothesis remains: after one XTR controller cold boot with no genuine Online/DCM endpoint, exact `0x0F FC17 read 0730/count8 + write 071C/count8` retries for a finite startup/service window and then stops naturally.
- First arm attempt at 14:55:38 auto-aborted correctly because no controller power-cycle / >=6 s bus gap occurred; it carries no protocol result.
- Valid second attempt: bus gap detected at 14:57:53.961; `BUS_RETURN` at 14:58:01.042.
- First target: `n=1`, `since_return=1283 ms`, state `A80E=0000 A80F=0005 AFDC=0000`.
- Early state progression: `A80E 0000->0008` at 1761 ms, `A80E 0008->0028` at 2858 ms, `AFDC 0000->0010` at 5583 ms, `A80F 0005->000A` at 11278 ms. None stops the retry stream.
- Target stream reaches **63 requests**. Last observed exact target is `n=63` at **267123 ms after BUS_RETURN** with `A80E=0028 A80F=000A AFDC=0010`; preceding cadence remains ~4.29 s with no slowdown/backoff.
- The next expected target does not appear. EXP248 raises `STOP_CANDIDATE` after **20793 ms silence** while the ordinary bus remains active, with the same monitored state `A80E=0028 A80F=000A AFDC=0010`.
- Supplied tail contains no `FALSE_STOP` and no further target; `EXP248 Last Target Age` reaches at least **53.5 s** while controller/0x06/outdoor traffic remains live. Parser remains clean (`resync=0`, `drops=0`).
- **Important:** the experiment success criterion requires another 60 s after `STOP_CANDIDATE`. The supplied file ends about 33.7 s after that marker, therefore `SUMMARY CONFIRMED_STOP` is not present and EXP248 must not yet be marked COMPLETE.
- Provisional strong interpretation: the local XTR retry stream appears to terminate abruptly at ~267.1 s (~4 min 27.1 s) after bus return, without a bus outage or visible A80E/A80F/AFDC transition. A fixed ~270 s timer or fixed retry budget is now a plausible hypothesis, not yet proven.
- No active `0730` response was sent or approved. Production functionality is unchanged.
- Minimal missing evidence: if available, provide only the log tail from about **15:03:22 through 15:03:50+**. A rerun is not needed if that tail still exists.


## Authoritative current state — 2026-09-27 — EXP248 PREPARED / NOT RUN

- Current experiment: **EXP248 — PREPARED / PASSIVE 071C/0730 NATURAL-STOP TRACE; not yet run**.
- Hypothesis: after one XTR controller cold boot with no genuine Online/DCM endpoint, the exact `0x0F FC17 read 0730/count8 + write 071C/count8` service/approval slot retries for a finite window and then stops naturally; the immediate `A80E/A80F/AFDC` state around the final retry may identify the stop condition.
- EXP247 established only a bound on one historical passive boot: target still active at ~198 s after Bus Healthy and already absent by ~1600 s. The exact stop lies inside a logging gap.
- **Only experimental variable:** one controlled Thermia/controller cold boot. No heat-pump setting is changed.
- EXP248 is fully RX-only: GPIO17 TX is not configured; GPIO21 DE remains LOW; no ACK, FC17 response, probe, scan, semantic write, room-sensor emulation or automated controller restart exists.
- Home Assistant experimental controls are under Configuration: `EXP248 Arm RX-only Timeout Trace` and `EXP248 Abort`.
- Guarding/measurement:
  - ARM requires fresh bus traffic and >=15 s ESP uptime;
  - after ARM, a genuine >=6 s bus gap must be observed within 60 s;
  - first CRC-valid frame after that gap defines bus return;
  - every exact 071C/0730 target is logged with 16-byte `W071C` image and current A80E/A80F/AFDC snapshot;
  - >=20 s target silence is accepted as a stop candidate only while the rest of the bus remains live;
  - EXP248 then requires another 60 s without a target before confirming the stop; any target reappearance cancels the candidate and is recorded as `FALSE_STOP`;
  - hard observation ceiling is 35 min after bus return.
- Success criterion: `SUMMARY CONFIRMED_STOP` with >=3 target frames, clean parser counters, a final target time and a 60 s target-free confirmation window while ordinary bus traffic remains alive.
- Stop/inconclusive criteria: no >=6 s boot gap within 60 s of ARM, fewer than 3 target frames, parser/buffer corruption, or `SUMMARY CENSORED_35MIN`.
- **EXP239 remains OPEN** pending the external genuine iTec Eco 5 raw capture.
- **EXP238 remains PARKED / NOT RUN.**
- No active `0730` response is approved.


## Authoritative current state — 2026-09-27 after EXP247

- Last completed experiment: **EXP247 — COMPLETE / OFFLINE: natural XTR `071C/0730` disappearance is proven, but exact timeout is not recoverable from the current right-censored captures**.
- Current experiment: **none running**.
- **EXP239 remains OPEN** pending the external genuine iTec Eco 5 Online raw capture.
- **EXP238 remains PARKED / NOT RUN.**
- EXP247 made no bus interaction and changed no production functionality.
- EXP221 proves the target is still active at ~197.999 s after Bus Healthy (47th exact target), with normal ~4.276 s cadence; the experiment ends only 0.600 s later.
- The same Thermia power cycle remains continuous until EXP222 is armed at 22:39:28.826, ~1599.592 s after that Bus Healthy transition. During the next ~419.3 s before the next deliberate Thermia power-off, the EXP222 logger sees 237 native `04A6` FC16 frames, 119 `085F` FC16 frames and 59 `0x06` polls, but **zero** `071C/0730` targets.
- Therefore, on that passive boot, the target natural stop occurred somewhere between ~198 s and ~1600 s after Bus Healthy. The exact point is hidden by a target-logging gap.
- EXP71 and EXP71B independently show that experiment software timeouts do not stop the controller target stream; targets continue after those software timeout markers.
- EXP222 and EXP225 are also right-censored: their last target occurs less than one normal retry interval before each experiment ends.
- After target disappearance the XTR continues ordinary native traffic; no FC03/0708 Online mailbox state appears.
- Do **not** describe 200 s as the controller timeout. It is only EXP221's observation-window boundary.
- No active `0730` response is approved.
- If exact timeout becomes important, the next appropriate live experiment is a single **RX-only >=30 min cold-boot target logger** that records until >=3 missed expected target intervals prove the natural stop.


## Authoritative current state — 2026-09-27 after EXP246

- Last completed experiment: **EXP246 — COMPLETE / OFFLINE POSITIVE: local XTR `071C..0723` is a redundantly encoded calendar/clock service record with no unexplained per-frame entropy**.
- Current experiment: **none running**.
- **EXP239 remains OPEN** pending the external genuine iTec Eco 5 raw capture.
- **EXP238 remains PARKED / NOT RUN.**
- EXP246 made no bus interaction and changed no production functionality.
- Input corpus remained the 129 exact local XTR requests recovered by EXP245.
- Proven dynamic fields:
  - byte0 = year-2000;
  - byte1 = hour;
  - byte3 = 2*second;
  - byte6 = byte3>>2 = floor(second/2);
  - byte9 = day-of-month;
  - byte11 = 4*minute;
  - byte15 = 2*byte3 = 4*second.
- Therefore all apparent second-bearing fields are deterministic redundancy, not independent session material.
- New strong structural observation: bytes4/5 are always `F9 06` and are exact bitwise complements. In September, the low nibble of `F9` equals month 9 and `06 = 0x0F-9`. Candidate encoding: `byte4=0xF0|month`, `byte5=~byte4`.
- Byte13 is always `0x1E=30`, matching September's 30 days. This is a strong days-in-month hypothesis, not yet cross-month proven.
- A candidate complete calendar generator using those two hypotheses reproduces 129/129 frames exactly.
- Remaining invariant bytes `45, AC, DC, C5, 00, 8F` are currently best treated as format/signature markers; exact semantics unknown.
- No local payload byte remains with independent random/session/checksum/MAC-like variation.
- Controller-vs-logger lead rises from ~201 s on Sep22 to ~206.35 s on Sep26, consistent with ~1.24 s/day (~14.3 ppm) relative RTC drift if the logger timebase is stable.
- Externally reported Eco 5 values fail the local RTC signature (1/13 and 0/13 structural checks), reinforcing a genuinely different payload regime.
- No active `0730` reply is approved.
- Next preferred offline experiment: **EXP247 — boot approval retry-window / timeout reconstruction from full raw logs**.


## Authoritative current state — 2026-09-27 after EXP245

- Last completed experiment: **EXP245 — COMPLETE / OFFLINE STRONG NEGATIVE FOR A LOCAL RTC->CHALLENGE MODE TRANSITION IN THE EXISTING CORPUS**.
- Current experiment: **none running**.
- **EXP239 remains OPEN** pending Piotrek's full genuine iTec Eco 5 Online raw capture.
- **EXP238 remains PARKED / NOT RUN.**
- EXP245 made **no new bus interaction**: no restart, no RS485 TX, no ACK, no FC17 response, no setting change and no YAML/Home Assistant change.
- EXP245 directly re-parsed all 129 exact local XTR `0x0F FC17 read 0730/count8 + write 071C/count8` frames previously identified across EXP71, EXP71B, EXP221, EXP222 and EXP225.
- **129/129** local payloads exactly match the XTR RTC/service encoder established by EXP226; **0/129** show an Eco-5-like high-entropy challenge regime and **0/129** are exact retries.
- The exact target is an early boot/recovery scheduler slot:
  - EXP221: first target ~1.219 s after `Bus Healthy -> ON`;
  - EXP222: ~1.179 s;
  - EXP225: ~1.095 s.
- Where both slots are explicitly logged, the target follows the immediately preceding `0x06 FC17 AFC8/12 -> AFDC/5` poll by ~0.24–0.28 s median.
- RTC-mode targets are observed with preceding `AFDC` values `0x0000`, `0x0010` and `0x0020`.
- Historical EXP71B already tested an active 0x06 zero responder and reached `TRUE_BOOTSTATE_CONFIRMED` (`A80E=0x28`, `AFDC=0x10`, fast/served 0x06 participation); 18 target frames after that state still use the RTC encoder.
- Historical EXP222 ACKed six allow-listed `0x0F FC16` state-export pages; the target remained RTC encoded and the controller still produced no FC03/0708 mailbox.
- Therefore **A80E/AFDC promotion, 0x06 responder presence/served cadence, and partial FC16 acknowledgement are not sufficient selectors for an RTC -> challenge transition**.
- EXP224 remains the steady-runtime contrast: zero exact target transactions while ordinary native `03E8` traffic was present. The family is boot/recovery gated, but the exact natural disappearance time is not established.
- Cross-model interpretation:
  - local XTR M / no Online endpoint: deterministic RTC/service payload regime;
  - externally reported genuine Eco 5 + Online: high-entropy, retryable challenge-like regime.
- The simple state-dependent-mode hypothesis is now weaker. Stronger current alternatives are **model/firmware/profile-specific encoding** or an **XTR-specific multi-stage approval prerequisite** absent from current captures.
- No active `0730` response is approved. Do not replay the published Eco 5 responses against the XTR RTC payload.
- Preferred next evidence: Piotrek raw Eco 5 capture (finish EXP239) or an externally sourced genuine XTR/iTec Online `0730` response. If unavailable, next offline-only candidate is **EXP246 — XTR RTC/service encoder reconstruction**.


## Authoritative current state — 2026-09-27 after EXP244

- Last completed experiment: **EXP244 — COMPLETE / OFFLINE POSITIVE: local XTR `071C..0723` is a deterministic RTC-derived service image, not a high-entropy challenge in the observed no-Online-endpoint state.**
- Current experiment: **none running**.
- Next preferred experiment: **EXP245 — offline existing-capture `071C/0730` mode/precondition census**.
- **EXP239 remains OPEN** pending Piotrek's full genuine iTec Eco 5 Online raw capture; its externally reported challenge/response evidence must be kept distinct from the locally observed XTR RTC payload regime.
- **EXP238 remains PARKED / NOT RUN.**
- Production functionality is unchanged. EXP244 was offline only: no heat-pump restart, no RS485 TX, no FC17 response, no ACK, no scan, no Home Assistant/YAML change.

### EXP244 key result

EXP244 directly re-parsed 104 locally recorded exact XTR requests:
- EXP221: 47
- EXP222: 25
- EXP225: 32

All 104 payloads are unique; no exact retry occurred. The local FC17 cadence remains about 4.26 s. The previously identified RTC model reproduces all 104 payloads exactly:

```text
071C = (year_since_2000 << 8) | hour
071D = 0x4500 | (2 * second)
071E = 0xF906
071F = (floor(second/2) << 8) | 0xAC
0720 = 0xDC00 | day_of_month
0721 = 0xC500 | (4 * minute)
0722 = 0x001E
0723 = 0x8F00 | (4 * second)
```

On the same-day Sep-26 corpus only 5 of the 16 payload bytes vary; successive 128-bit payloads differ by a median of only 6 bits (range 2..18). This is incompatible with treating the local observed XTR payload as a fresh high-entropy 128-bit challenge.

The two externally reported Eco 5 controller values are structurally very different:
- they differ from each other by 55/128 bits;
- neither matches any of the 11 byte positions that remain constant throughout the local Sep-26 XTR corpus;
- the external report describes exact challenge retries after no answer, while no such retry occurs in the local XTR corpus.

### Strong architectural refinement

Do **not** generalize either payload interpretation across all states/models.

Safest current role naming:

```text
071C..0723 = controller-owned DCM/service approval input bank
0730..0737 = external/service-owned return bank
```

Observed payload regimes:
1. **Local XTR M, no Online endpoint:** deterministic RTC/service image.
2. **Externally reported genuine iTec Eco 5 + Online:** high-entropy, retryable challenge-like image.

Possible explanations include a state-dependent encoder, model/firmware-specific encoder, or profile-dependent serializer. EXP244 does not distinguish these.

### Safety consequence

Do not replay either published Eco 5 response against the local XTR RTC-derived payload. No active `0730` response is approved.

### Next experiment

**EXP245 — existing-capture 071C mode/precondition census**

Offline only. Re-scan all available local XTR captures to determine:
- first/last appearance of exact `0x0F FC17 read 0730/count8 + write 071C/count8`;
- controller state immediately before and after first appearance;
- relation to `0x06` polling/cadence;
- whether any historical local payload violates the RTC encoder;
- whether any exact local retry exists;
- whether any historical local capture ever transitions toward the externally reported challenge-like regime.


Last updated: 2026-09-27

## Authoritative current state — 2026-09-27 after EXP241

- **Last completed experiment:** **EXP241 — COMPLETE / OFFLINE DCM03 VERSION-PROFILE CENSUS**.
- **Hypothesis:** a reusable DCM03 approval implementation should appear with the same DCM firmware generation across materially different classic Thermia heat-pump profiles.
- **Only variable:** offline/public corpus analysis. No bus TX, response, ACK, scan, restart, YAML/HA change or room-sensor emulation.
- Public `python-thermia-online-api` fixtures show **DCM 2.0.17** on three different classic profiles: Diplomat/Diplomat Duo (profile 1001, HP 1.42), ATEC/DHP-AQ (1002, HP 3.1.1), and iTec/IQ (1005, HP 2.4.1).
- Newer Calibra/NCP profiles 1024/1028 do not expose the same classic DCM metadata and have null/empty DCM version; keep NCP/Genesis separate from the classic DCM03 model.
- **Strong conclusion:** DCM03 2.0.17 is a generic multi-profile firmware generation, not a model-specific ATEC-only build. A 2.0.17 dump from any classic supported system is therefore high-value.
- **Especially relevant:** the public iTec/IQ fixture proves 2.0.17 was used on an iTec-family DCM installation. This materially strengthens 2.0.17 as the primary firmware target for the Eco/XTR approval work.
- **Nuance:** common DCM firmware does not prove identical low-level HP wire protocol across older Gateway-card systems and direct DHP-AQ/iTec RS485 systems.
- **Negative:** targeted public corpus search recovered no alternative Thermia DCM version and no DCM03 binary/update package. This is a bounded small-corpus negative, not proof no other versions exist.
- **EXP239:** remains IN PROGRESS pending Eco 5 raw challenge/response capture or DCM03 firmware dump.
- **EXP238:** remains PREPARED / NOT RUN / parked.
- **Safety:** no active 0730 response is approved; no brute force or replay.

---

## Authoritative current state — 2026-09-27 after EXP240

- **Last completed experiment:** **EXP240 — COMPLETE / OFFLINE DCM03 IMPLEMENTATION-LOCUS AND FIRMWARE-LINEAGE ARCHAEOLOGY**.
- **EXP239:** remains **IN PROGRESS**; its completion still requires the genuine Eco 5 raw capture/timeline or a DCM03 firmware dump.
- **EXP238:** remains **PREPARED / NOT RUN** and parked.
- **EXP240 hypothesis:** the `071C -> 0730` approval function resides in the DCM03 / HP-facing gateway layer, and product topology can identify the correct firmware target.
- **Only variable:** offline/public-source analysis. No Thermia TX, ACK, response, write, scan, restart, YAML change or room-sensor emulation.
- **Key topology result:** DHP-AQ kit `086L2382` has no separate GateWay card; DCM03 connects directly from its `RS 485` port to the heat-pump relay-board RJ45. By contrast, DHP-H/L/A uses a separate internal GateWay card plus DCM03.
- **Strong architectural consequence:** for DHP-AQ/iTec-like topology, the HP-facing approval implementation is in DCM03 itself or the directly connected controller-side firmware, not in the Link CC host. This materially strengthens the EXP234B boundary result.
- **Product identifiers:** DCM03 module `086L1602`; Link DCM kit `086L2381`; Link DCM AQ kit `086L2382`.
- **Mode result:** official instructions show the same DCM03 family can operate in Danfoss Link integration or Danfoss Online mode. Therefore Link-mode DCM03 firmware/hardware remains a valid target for recovering the HP-facing approval function.
- **Firmware-lineage clue:** public Thermia API debug reports expose `dcmVersion = 2.0.17` separately from heat-pump `programVersion`/`firmwareVersion`. Treat `2.0.17` as the highest-value concrete DCM firmware search token.
- **Historical corroboration:** field reports describe DCM02 -> DCM03 replacement for newer Link compatibility and visually identical DCM03 units with different firmware. This is supportive, not authoritative.
- **Negative:** targeted public search still recovered no DCM03 firmware image/update package/service loader and no trustworthy MCU/debug-pad identification.
- **Safety:** no active `0730` response is approved. Brute force, cross-challenge replay and invented responses remain prohibited.
- **Next offline targets:** DCM03 `2.0.17` binary/service package, PCB/MCU/debug photos, or the full Eco 5 challenge-response capture.

---

## Authoritative current state — 2026-09-27 after EXP239 Phase B

- **Current experiment:** **EXP239 — IN PROGRESS / OFFLINE 071C→0730 CHALLENGE-RESPONSE ANALYSIS**.
- **Hypothesis:** controller `071C..0723` is a 16-byte DCM-HP approval challenge/session token and `0730..0737` is the corresponding reproducible non-trivial DCM response. Successful approval gates state synchronisation and the `0708` mailbox.
- **EXP238:** remains **PREPARED / NOT RUN** and parked.
- **Experimental variable:** offline analysis/documentation only. No Thermia TX, ACK, response, scan, restart, YAML production change or room-sensor emulation.
- **Phase A retained:** the two published pairs rule out fixed XOR, fixed add/subtract, per-byte addition, rotate+XOR and byte-permutation+XOR. Two pairs remain insufficient to identify a named primitive.
- **New Phase B evidence:** official Danfoss Link HP-kit documentation explicitly names a firmware state `DCM-HP approval`, a separate `approval failed` state, then `sending settings to DCM`, followed by `all OK`.
- **Architectural alignment:** this vendor state order strongly matches the externally reported genuine Eco 5 sequence `repeated 071C/0730 -> first valid response -> FC16/full-state synchronisation -> 0708 mailbox`. Treat this as strong cross-platform corroboration; the manual is an older HP-kit platform, not direct XTR firmware documentation.
- **Refined strong conclusion:** `071C/0730` is now best treated as the **DCM-HP approval handshake**, not an RTC/calendar block or generic keepalive. The subsequent bulk FC16 transfer is a strong candidate for the documented `sending settings to DCM` phase.
- **Crypto triage:** Link CC 2.7.42 contains AES/RSA/SHA code in `OMService.dll` / encrypted-file-system infrastructure, but no obvious AES/Rijndael/CMAC/HMAC strings in the audited DHP/regulation/HE modules. AES presence in the ROM is therefore not evidence that 071C/0730 itself uses AES.
- **Narrow AES negative:** AES-128 ECB encrypt/decrypt and AES-CMAC with only zero, FF, and obvious padded ASCII keys (`Danfoss`, `Thermia`, `DanfossLink`, `LinkCC`, `DCM03`) do not reproduce either published response. This does **not** rule out AES with unknown/derived key or a different construction.
- **Exhaustive direct-key negative:** every contiguous 16-byte and 32-byte window in the available Link CC 2.7.42 and 4.2.1724 `ccimage.bin` files was tested as a literal AES-128/AES-256 key for direct ECB encrypt/decrypt and one-block CMAC of the known challenge. Zero windows produced the known response. This rules out a verbatim embedded raw key under those direct constructions, not derived/obfuscated/DCM-local keys or other algorithms.
- **Mode clue:** official HP-kit instructions show the DCM03 hardware family can operate in Danfoss Link integration or Danfoss Online mode. Therefore a Link-mode DCM03 firmware dump remains a high-value target for the HP-facing approval implementation; Online-specific firmware is not the only useful artifact.
- **Firmware-search negative:** targeted public search still found no DCM03/Connect firmware image or source containing the missing approval implementation.
- **Pairing-secret inference:** vendor replacement/install instructions expose no manual HP↔DCM secret-provisioning step. This weakens only the hypothesis of a manually provisioned pump-specific secret; factory, fixed, derived, identity-bound or automatic keying remain open.
- **Safety consequence:** still no evidence-backed arbitrary XTR response; no active `0730` response is approved and brute force remains prohibited.
- **EXP239 blocker:** obtain the genuine Eco 5 raw capture/timeline or a DCM03/Connect firmware dump, then test response determinism, retries, cross-boot behavior and exact approval→sync timing.

---

## Authoritative current state — 2026-09-27 after EXP239 Phase A

- **Current experiment:** **EXP239 — IN PROGRESS / OFFLINE 071C→0730 CHALLENGE-RESPONSE ANALYSIS**.
- **EXP239 hypothesis:** controller words `071C..0723` form a 16-byte challenge/session token and gateway words `0730..0737` are a reproducible non-trivial response that gates entry into the iTec Online state machine.
- **EXP238 status:** remains **PREPARED / NOT RUN** and is parked while EXP239 has priority.
- **Experimental variable:** offline analysis only. No ESP YAML, Home Assistant control, Thermia-bus TX, ACK, response, setting mutation, restart, scan or room-sensor emulation was introduced.
- **Available Phase-A corpus:** two published challenge/response pairs from the new genuine iTec Eco 5 Online capture. The full 10,719-frame raw log and contributor timeline script are not yet available locally.
- **Observed Phase-A facts:**
  - pair 1 challenge→response Hamming distance = `65/128` bits;
  - pair 2 challenge→response Hamming distance = `62/128` bits;
  - the two challenges differ in `55/128` bits and their responses differ in `68/128` bits;
  - fixed XOR masks differ (`755f5ec13e1cc60530ebd621e44a4d6f` vs `cc98353180230adf27bcba5722ca9dd6`);
  - fixed 128-bit add/subtract, fixed per-byte additive mask, fixed bit-rotation+XOR, and even fixed byte-permutation+XOR models are inconsistent with the two pairs;
  - common unkeyed 128-bit digest/truncation checks do not reproduce the responses.
- **Strong conclusion:** the two available pairs already rule out the simplest static transforms. The response relation is compatible with a non-linear keyed transform/MAC-style construction, but two pairs are insufficient to identify a named primitive.
- **Protocol correction retained:** the former EXP226 RTC/calendar interpretation must not be used as a semantic constraint for `071C..0723`.
- **Safety consequence:** there is still no evidence-backed response for an arbitrary new XTR challenge. No active `0730` response is approved and brute-force is prohibited.
- **EXP239 completion blocker:** ingest the genuine Eco 5 raw capture, extract every attempt/retry/response across both gateway-connected boot cycles, then test determinism, retry behavior, boot-cycle dependence and post-handshake transition timing.
- **Tooling prepared:** `exp239_extract_071c_0730.py` performs read-only CRC validation, exact FC17 handshake extraction, duplicate/retry classification, response timing, 0708 mailbox extraction and first post-handshake FC16/mailbox timing.

---

## Authoritative current state — 2026-09-27 after EXP237 / DCM RE-AUDIT / EXP238 PREPARED

- Last completed experiment: **EXP237 — COMPLETE / VALID PASSIVE NEGATIVE FOR VISIBLE HEAT-CURVE UI INGRESS ON THIS RS485 SEGMENT**.
- Current experiment: **EXP238 — PREPARED / PASSIVE OPERATION-MODE UI INGRESS TRACE**.
- **EXP237 hypothesis tested:** if the physical Heat Curve mutation traverses the observed RS485 segment before controller-owned `0x0F FC16 03E8/count14` serialization, a reversible frame/event should appear before the changed `03E8` export in both directions.
- **Only EXP237 variable:** physical Heat Curve `36 -> 37 -> 36`; ESP remained RX-only throughout.
- **Observed +1 transition:** after the marker, the first `03E8` frame carrying the new value appeared at +2418 ms with `03E8=37`. The 17 preceding raw frames were ordinary already-known `0x02`, `0x1E`, `0x14`, `0x0A`, and `0x0F:085F` traffic; no new slave/function/event appeared within EXP237's recognised parser set.
- **Observed restore transition:** the first `03E8` after the restore marker was a stale cyclic `03E8=37` frame at +114 ms. The first export carrying the restored value `03E8=36` appeared at +4821 ms. The intervening traffic again consisted only of routine known frames; no reversible pre-export candidate appeared.
- **Trace integrity:** final EXP237 summary: `total=420 baseline=86 plus=166 restore=168 S01=0 unusualFC=0 03E8=42 resync=0 drops=0`.
- **Important logger refinement:** EXP237's `FIRST_03E8` marker is not a sufficient transition delimiter because a stale cyclic page can arrive immediately after a physical-change marker. Future UI-ingress traces must key on the first page carrying the **target value**, not merely the first page after the marker.
- **Strong conclusion:** for Heat Curve, the semantic physical-UI ingress was **not visible as a distinct reversible Modbus frame/event within EXP237's recognised parser coverage before the controller-owned `03E8` state export**.
- **Hypothesis:** the physical panel may mutate controller state internally or over a different/internal link, with this RS485 segment exposing only the resulting controller-owned serialization. This is not yet generalized to all UI settings from a single setting family, and EXP237's explicit slave-address filter leaves a residual unknown-address blind spot.
- **EXP238 hypothesis:** repeat the same passive full-bus method with the independently proven Operation Mode path `AUTO -> COMPRESSOR -> AUTO`. If a common physical-panel ingress exists on this segment, a reversible pre-export event should precede the first `0546/count20` page carrying `0553=2` and then `0553=1`.
- **EXP238 safety:** RX-only; GPIO17 TX absent; GPIO21 DE LOW; Configuration-category marker controls only; no ACK, response, probe, scan, write, restart or room-sensor emulation.
- **EXP238 logger improvements:** target-value-aware detection ignores stale `0546` frames and records the true number of frames before the first `0553=2` / `0553=1` target export; standard Modbus unit IDs `0x00..0xF7` are accepted passively so an unexpected panel/service address is not discarded.


---
## 2026-09-27 — EXP234B COMPLETE / offline raw-binary completion of service-page archaeology

- **Status:** offline/read-only historical completion of EXP234; current bus experiment remains **EXP238 PREPARED / NOT RUN**. No Thermia TX, restart or setting change.
- **Hypothesis:** the raw Danfoss Link CC 2.7.42 firmware might expose the missing low-level `0708/071C/0730` service-page serializer or a genuine `0730..0737` response builder.
- Successfully materialized and parsed the original 2.7.42 Windows CE `ccimage.bin`; carved the managed DHP/regulation assemblies and reconstructed native `HECTArch.dll`.
- `ParameterCache.dll` positively contains the real abstract DHP layer (`DHPParameterCache`, `SyncParameters`, `OnHEServiceSetGet`, `OnHEServiceBind`, `HESetGetReqRsp`) and real parameter-ID constants including `0x030A`, `0x4402`, `0x4414`. This validates the raw extraction target.
- **Negative:** no managed `ldc.i4 0x071C` or `ldc.i4 0x0730` exists in the audited heat-pump/regulation assemblies; `ParameterCache.dll` contains no `0708/071C/0730` page constant.
- Three `0x0708` immediates in `RegulationEngine.dll` map by CLR metadata to ordinary node constructors (`BatteryPoweredNodeBase`, `SCMNode`, `HCNode`) and occur with other timing/configuration integers; they are not DHP service-page references.
- Full-ROM ownership mapping places every exact 32-bit `0x071C`/`0x0730` hit in unrelated Windows/UI/framework/application files, not in the DHP/HE stack.
- Native `HECTArch.dll` is explicitly the HE/Z-Wave layer (`HESetGetReqRsp`, `ServiceBind`, `ServiceSetGet`, `ZW*` functions) and contains no exact 32-bit `0708/071C/0730` constants.
- **Strong conclusion:** the audited Link CC host firmware stops at abstract HE/DHP Set/Get. The missing DCM03/Connect -> Thermia local serializer is in another device/layer and cannot supply an evidence-backed XTR `0730..0737` response from this firmware.
- Official Danfoss HP-kit documentation independently describes a distinct `DCM-HP approval` phase and `sending settings to DCM`, consistent with a separate application/session layer beyond syntactic bus presence.
- The raw `THERMIA_PART9_BUNDLE.zip` remains non-materializable, but the original 2.7.42 firmware that underpinned that line of investigation was directly materialized and audited.
- **Safety:** no active `0730` response is approved. Do not use zero-bank, echo or positional guesses.
- **Next direction:** search specifically for Thermia Connect/DCM03 firmware/update images or heat-pump Gateway/controller firmware; use XTR as an active protocol oracle only after a concrete response candidate is evidence-backed.


---
## 2026-09-27 — Offline genuine DCM log re-audit before EXP238

No bus experiment was run. EXP238 remains PREPARED and has not been executed. The four genuine external Online/DCM captures were re-analysed specifically for command-dispatch and endpoint-rejoin state.

### Observed facts
- Across the genuine captures, the reference controller periodically issues `0x0F FC03 0708/count6` even while the slave-0x0F endpoint is absent. In `090550`, 16 such polls are unanswered before the first valid reply at 68.235 s. This strengthens that the reference scheduler is controller-side and does not appear merely because the DCM endpoint responds.
- The already-proven runtime command discriminator remains exact: `0709=0001` occurs twice and only twice, and both occurrences are immediately followed by `0x0F FC03 03E8/count13`; the next `0708` response clears `0709` back to zero.
- A second, distinct `0708` role is visible during endpoint rejoin. The first valid `090550` reply is `0708..070D = [0000,0000,7FFF,FFFF,0080,0007]`. 69 ms later the controller starts a large controller->0x0F FC16 snapshot at `03E8/count13`, then walks the configuration/state pages through `06F1/count3`. The next `0708` poll does not occur until 101.901 s, when the reply has become the normal idle image `[0000,0000,0000,0000,077F,0006]`.
- In `090209`, `070C` is `0080` in one valid reply and becomes `0000` on later replies while the high-page FC16 snapshot (`07D0`, `07E4`, `07F8`, ...) is still continuing. Therefore `070C=0080` is not simply an on/off bit meaning “full snapshot currently active”.
- Across all available valid `0708` replies, `070D=0007` is observed only in the first successful `090550` rejoin reply; normal/command/runtime replies use `070D=0006`.
- The 13-word desired image returned after the second known Heat Curve command in `210001` (`03E8=0016` plus 12 unchanged words) is byte-for-byte identical to the `03E8/count13` state image exported at the start of the successful `090550` rejoin snapshot.

### Strong conclusions
1. Reference `0708/count6` is a multi-purpose control/mailbox page, not just a command-pending boolean. `0709` carries the proven one-shot command-pending discriminator, while `070A..070D` participate in endpoint lifecycle/synchronization state.
2. The genuine reference write path is a **controller-initiated pull model**: the external endpoint advertises pending/lifecycle state in the mailbox, and the controller then fetches a full desired-state image (`03E8/count13`) rather than accepting an arbitrary master write to a settings register.
3. The local XTR `0730/count8` return bank should therefore not be searched primarily for a literal Heat Curve value. Architecturally, an XTR-native mailbox may instead contain status/dirty/session selectors that cause a second controller-initiated settings transaction. This is an architectural hypothesis only; EXP233's warning against direct field-position homology remains in force.
4. No new active write/response target is justified. There is still no genuine XTR `0730/count8` response image.

### Hypotheses / unknowns
- `070C` is plausibly a bitmask/group/capability field: observed values `077F` and `0080` are complementary within `07FF`, but this is not proven and `070C=0000` also occurs during synchronization.
- `070D=7 -> 6` may encode a rejoin/init phase, protocol state, or generation indicator; exact semantics are unknown.
- The local XTR `071C/0730` FC17 exchange may be a newer combined bidirectional service/session primitive analogous at an architectural level to the reference `0708` mailbox, but wire-level equivalence is not established.

### Direction before EXP238
Perform no active `0730` response. Before running EXP238, finish the offline mailbox state-machine table over all genuine DCM captures: correlate every `0708` response image with the adjacent FC16 page cursor and startup/runtime phase. Use the result to define what behavioral signature an XTR-native mailbox should produce. EXP238 remains the next prepared physical-bus experiment if the offline audit does not yield a stronger XTR-specific target.

## Authoritative current state — 2026-09-27 EXP237 PREPARED

- Current experiment: **EXP237 — PREPARED / PASSIVE LOCAL-UI INGRESS TRACE**.
- **Hypothesis:** the physical Thermia Heat Curve mutation is accepted upstream of the proven controller -> `0x0F FC16 03E8/count14` export; if the physical-panel ingress crosses the observed RS485 segment, a reversible frame/event should appear before the first `03E8` export in both `A -> B` and `B -> A`.
- **Only experimental variable:** physical Heat Curve `baseline -> baseline+1 -> baseline`; no other heat-pump setting is changed.
- Source YAML is the exact RX-only EXP225 build. Obsolete EXP225 cold-boot/FC17 experiment code was removed. Known-good production entities/parsing remain intact.
- EXP237 remains **RX-only**: GPIO17 TX is not configured, GPIO21 DE remains LOW, and all Home Assistant controls are Configuration-category trace markers only. No restart, ACK, response, probe, scan, semantic write or room-sensor emulation is performed.
- The experiment adds bounded raw trace windows and extends the passive parser only to recognise plausible local panel/service traffic (`0x01`, `0x03`, `0x05`, `0xC8` and common Modbus FC01/02/05/06/08/0F/16) so such frames are not discarded before offline analysis.
- Procedure: 10 s untouched baseline; marker **before** physical Heat Curve +1 then 20 s trace; marker **before** exact restore then 20 s trace; end experiment and analyse full log.
- Success criterion: a CRC-valid frame/field that (a) appears before the first `03E8` export, (b) changes reproducibly on `+1`, and (c) reverses on restore.
- Important negative criterion: if both transitions show no reversible pre-`03E8` frame on this RS485 segment, panel->controller semantic ingress is likely internal or outside this observed bus, and write research should pivot accordingly.
- YAML syntax was parsed successfully offline. Full ESPHome C++ compilation was not available in this runtime.

---

## Authoritative current state — 2026-09-27 after EXP236A/EXP236B

- Last completed experiment: **EXP236B — COMPLETE / OFFLINE CROSS-SETTING WRITE-PATH REFINEMENT**.
- Current experiment: **none running**. No ESP TX, heat-pump restart, setting mutation, YAML change or room-sensor emulation was performed in EXP236A/EXP236B.
- **EXP236A — cross-setting outbound-sync generality:** compared three locally proven physical-UI settings paths:
  - Heat Curve: physical UI change reactivates controller-originated `0x0F FC16 03E8/count14`; `03E8` follows the curve value.
  - Activate Cooling: physical UI toggle changes the native `0x0F` cooling page at `0442`; `0442` is proven `0=OFF / 1=ON`.
  - Operation Mode: physical `AUTO -> COMPRESSOR -> AUTO` changes only `0553: 1 -> 2 -> 1` within the local `0546/count20` system page.
- **Strong conclusion from EXP236A:** controller-originated `0x0F FC16` is a **general controller-owned configuration/state export layer across multiple unrelated settings families**, not a Heat-Curve-specific special case. This materially strengthens EXP236's conclusion that seeing the changed value in a `0x0F FC16` page does not identify the semantic ingress.
- **EXP236B — page-family / causality refinement:** the three physical-UI settings land in distinct page families (`03E8`, `0442`, `0546`), while EXP135/136 showed that DHW START and COMFORT/ECO do not modify the recurrent `03E8..03F5` page. This supports page-specific serialization after an upstream mutation rather than one universal writable settings block.
- **Strong conclusion from EXP236B:** tomorrow's trace should key on the **first bus event before the page-specific FC16 export**, not on the export page itself. If the same preceding slave/function pattern appears for both Heat Curve and Operation Mode, that would be strong evidence for a common panel-to-controller ingress path.
- **Important unknown:** the current archive does not prove that the physical control panel's semantic input is visible on this exact RS485 segment. If no reversible pre-export frame exists in a high-resolution trace, the panel may mutate controller state internally and only the resulting `0x0F FC16` serialization may be exposed on this bus.
- **Tomorrow's reserved experiment remains EXP237 — passive local-UI ingress trace.** Start with Heat Curve `A -> B -> A`; if timing/logging quality is good, repeat the same passive method with Operation Mode as a second discriminator. No ESP TX.
- **Safety:** no new active write target is approved. `0x0F FC16` remains outbound/state-export for control purposes; `0730` remains secondary/unknown; no AFCA or direct-setting write experiments resume without new evidence.

---

## Authoritative current state — 2026-09-27 after EXP236

- Last completed experiment: **EXP236 — COMPLETE / OFFLINE CAUSALITY AUDIT; LOCAL UI CHANGE IS THE BEST NEXT WRITE-INGRESS TRACE**.
- Current experiment: **none running**. No ESP TX, heat-pump restart, setting mutation, YAML change or room-sensor emulation was performed in EXP234–236.
- **EXP234 — offline decimal/service-page archaeology:** searched the accessible indexed Project/Library corpus and the relevant public Thermia repositories for decimal pages `1800`, `1820`, `1840`, hex `0708`, `071C`, `0730`, and the XTR FC17 shape. No named service-page schema, field labels or genuine `0730/count8` response was recovered. The archived `THERMIA_PART9_BUNDLE.zip` could not be raw-materialized in the current runtime, so this is a **negative for the accessible indexed corpus, not an exhaustive binary negative**.
- **EXP235 — offline topology-transferability audit:** the genuine DCM/reference platform and the local XTR are now treated as architecturally related but **not wire-identical write targets**. Reference traffic continuously uses `0x04`, A5 and `0x0F FC03`; local XTR runtime uses `0x1E` and lacks that scheduler family. Reference `0x02` uses `A7F8/count13` with `A811/A812=000C/0500`; local XTR uses `A7F8/count15` with `A811/A812=FFFF/0000`. Therefore the proven reference `0708 -> 03E8` command path remains valuable protocol evidence, but is **downgraded from primary local implementation target to reference architecture**.
- **EXP236 — offline local-UI causality audit:** EXP143 proved that a physical Heat Curve change on the XTR UI causes controller-originated `0x0F FC16 03E8/count14` synchronization, with word0 tracking the changed curve value. EXP177 proved that replaying the same native-looking `03E8/count14` image toward slave `0x0F` does not cause the semantic Heat Curve change. The strongest causal model is therefore: **the semantic mutation occurs upstream of the outbound `03E8` sync**; `03E8` is a consequence/state-export path, not the local command ingress itself.
- **Main research direction changed:** stop treating `0730`/old DCM emulation as the primary write-access route. Keep it as a secondary architectural line. The highest-value next active/passive experiment is a full-bus local UI A/B/A trace that captures all slaves and function codes around the exact user input, looking for the event that precedes the first `03E8` sync.
- **Tomorrow's preferred experiment: EXP237 — passive local-UI ingress trace.** Hypothesis: a Heat Curve `A -> B -> A` change on the physical panel produces a reversible bus event before the known outbound `03E8` mirror. Use a narrow pre/post window around exact UI marks, log all valid frames, make no ESP transmissions, and compare both transitions.
- **Safety:** no new active write target is approved by EXP234–236. Do not synthesize `0730` responses, do not repeat direct `0x0F FC16 03E8` writes, and do not resume AFCA payload guessing without new evidence.

---



## Authoritative current state — 2026-09-27 after EXP233

- Last completed experiment: **EXP233 — COMPLETE / OFFLINE STRUCTURAL REFINEMENT + NEGATIVE FOR FIELD-POSITION HOMOLOGY**.
- Current experiment: **none running**. Heat-pump restarts remain paused. EXP233 used only existing captures/project evidence and offline parsing; no ESP TX, setting change, YAML change or controller restart was performed.
- **Hypothesis tested:** the repeated Thermia FC17 `+0x14` read/write-bank convention might extend beyond address spacing to field-position or request/feedback semantics, allowing one or more XTR `0730..0737` words to be constrained from known roles.
- **New general FC17 bank result:** the `+0x14` hex spacing is exactly **+20 decimal registers** and is a generic Thermia FC17 page/bank stride, not an Online-specific signature. In the four genuine reference captures the recurring request schemas are:
  - slave `0x02`: read `A7F8=43000/count13`, write `A80C=43020/count7` — 274 requests;
  - slave `0x04`: read `ABE0=44000/count12`, write `ABF4=44020/count4` — 275 requests;
  - slave `0x05`: read `AC12=44050/count12`, write `AC26=44070/count4` — 2 requests;
  - slave `0x06`: read `AFC8=45000/count12`, write `AFDC=45020/count5` — 69 requests;
  - slave `0x0A`: read `B3B0=46000/count3`, write `B3C4=46020/count3` — 31 requests.
- The local XTR adds two important variants:
  - slave `0x02` uses the same `43000 -> 43020` bank pair but a different read span (`count15` locally versus `count13` reference), proving the 20-register bank stride is independent of active payload length;
  - slave `0x0F` cold-boot FC17 uses **write `071C=1820/count8`, read `0730=1840/count8`**, i.e. the same +20 page stride but with direction reversed relative to the other recurrent FC17 roles.
- The nearby XTR/reference service bases normalize cleanly to **1800 / 1820 / 1840 decimal**:
  - `0708 = 1800`;
  - `071C = 1820`;
  - `0730 = 1840`.
  This strongly suggests three consecutive reserved 20-register service pages. It materially weakens any claim that the exact `0708 -> 071C -> 0730` spacing itself proves common command semantics.
- **Field-position homology is not supported.** Known semantic ingress/control-like fields occupy different relative positions and use different feedback mechanisms:
  - room sensor `0x0A`: read-bank word1 `B3B1` is a semantic setpoint request; accepted value is later reflected at paired write-bank word1 `B3C5`;
  - accessory `0x06`: read-bank word2 `AFCA` is a transport REQ/data-valid strobe; its ACK appears outside the paired FC17 write bank at native `0x0F:0861`; read-bank word9 `AFD1` is version metadata.
  - `0x02` and reference `0x04` read banks are dominated by state/telemetry-style values and provide no proven request-field position.
  Therefore no relative index (word0/1/2/etc.) can be transferred safely to `0730..0737`.
- **All-zero is not a universal neutral image.** On `0x0A`, a zero command field means “no request” but zeroing the whole bank would also report a false 0 °C room temperature. On `0x06`, a syntactically valid zero response changes presence/cadence and exposes `EXP 0.0`. Thus a response can be command-neutral yet still semantically active at role level.
- **Lifecycle discriminator:** unlike the steady-runtime `0x02`, `0x04`, `0x06` and `0x0A` FC17 families, the local XTR `071C/0730` family is strongly boot/recovery gated. EXP224 observed zero exact frames during ordinary runtime, while EXP221/225 reproduced it after controller power-on. This makes `0730..0737` at least as plausible as startup/service/RTC-session return data as a general runtime command mailbox.
- **Strong conclusion:** EXP233 does **not** narrow any individual `0730..0737` field enough for a safe active response. The strongest new interpretation is that `0730` belongs to a generic 20-register Thermia FC17 page framework, while its role-specific semantics remain unknown.
- **Safety conclusion:** no active `0730` responder is justified. Do not infer `0731` from room-sensor word1, `0732` from accessory word2, or use eight zero words.
- Preferred next experiment: **EXP234 — offline decimal-page / service-page archaeology**, searching all available firmware/maps/source material specifically for decimal register pages `1800`, `1820`, `1840` and neighboring 20-register page structures. The goal is to find role names, field labels, or a genuine XTR service response before any TX is reconsidered.

## Authoritative current state — 2026-09-27 after EXP232

- Last completed experiment: **EXP232 — COMPLETE / OFFLINE STRUCTURAL POSITIVE WITH IMPORTANT NEGATIVE: `0730..0737` is confirmed as an XTR external/service return bank, but no genuine response image is recoverable from the current corpus**.
- Current experiment: **none running**. Heat-pump restarts remain paused. EXP232 used only existing project/library artifacts plus read-only source searches; no ESP TX, setting change, YAML change or controller restart was performed.
- **Hypothesis tested:** the XTR-native `0x0F FC17 read 0730/count8 + write 071C/count8` return bank may be reconstructible or constrained from existing captures, archived code/artifacts, related FC17 interfaces and external project sources sufficiently to define a safe no-op response.
- Exhaustive project/library search found **no genuine `0x0F FC17` count-8 response** for `0730..0737`. A normal FC17 count-8 response would be 21 bytes and begin `0F 17 10`; no such frame was found in the relevant EXP221/222/225 logs or the older EXP71/71B evidence. All locally observed `0730` requests remain unanswered because no external slave-0x0F service endpoint is present.
- Read-only searches of the available external/reference artifacts also produced no `0730` payload: fclauson's `0F_register_value_map.xlsx`, `modbus_slave.py`, Discussion #143, and repository searches for `0730`, `071C`, decimal `1840`, and FC17 did not expose this XTR bank. This is a recorded negative result, not evidence that the bank is unused on genuine XTR accessories.
- **New structural finding:** Thermia FC17 role interfaces repeatedly separate the slave-owned read bank from the controller-written bank by exactly `0x14` registers:
  - room sensor `0x0A`: read `B3B0..B3B2`, write `B3C4..B3C6` (`+0x14`);
  - accessory `0x06`: read `AFC8..AFD3`, write `AFDC..AFE0` (`+0x14`);
  - genuine/reference `0x04`: read `ABE0/count12`, write `ABF4/count4` (`+0x14`);
  - genuine/reference `0x05`: read `AC12/count12`, write `AC26/count4` (`+0x14`);
  - local XTR `0x0F`: controller writes `071C..0723` and reads `0730..0737` (`+0x14`).
- A second exact relation is now explicit: `0708 -> 071C -> 0730` are successive `+0x14` register-bank bases. The older ATEC/DCM command-header read happens at `0708`, while the XTR FC17 writes its RTC image at `071C` and reads the external bank at `0730`. This is strong architectural structure but **not proof that the three banks share field semantics or command encoding**.
- EXP226 remains decisive for the XTR write half: most changing content in `071C..0723` is transformed RTC/calendar data. This materially downgrades EXP231's tentative idea that the whole `071C/0730` exchange might be a direct wire-equivalent of ATEC `0708`. The better model is an XTR service/role transaction with controller-owned service/RTC data written to one bank and external-device-owned data read back from the adjacent bank.
- The return bank is nevertheless a **proven controller-ingress surface by transaction direction**: the controller explicitly requests `0730..0737` from slave `0x0F`. Cross-role evidence from the room-sensor FC17 path proves that Thermia FC17 read-bank words can carry semantic requests into the controller, but that does not identify any `0730` field.
- **Safety conclusion:** no safe neutral/idle `0730..0737` response can be reconstructed. Zeros, an echo of `071C..0723`, an inverse RTC transform, or copied values from another FC17 role would all be guesses and are therefore not approved for an active responder test.
- Write-access implication: `0730..0737` remains a high-value XTR-native controller-ingress candidate, but it is now classified as **external/service return bank with unknown semantics**, not as a proven command mailbox. The fully decoded ATEC `0708 -> 03E8` mailbox remains the strongest proven command architecture; XTR may use a different service serializer.
- Preferred next experiment: **EXP233 — offline cross-role FC17 bank-schema analysis**, cataloguing the known `+0x14` bank pairs and semantic ingress/feedback conventions to test whether field-position homology can constrain `0730..0737` without guessing. If no stronger mapping emerges, further active work should wait for genuine XTR/Connect/Online response evidence rather than transmit an invented payload.

## Authoritative current state — 2026-09-27 after EXP231

- Last completed experiment: **EXP231 — COMPLETE / OFFLINE POSITIVE SCHEDULER-TOPOLOGY RECONSTRUCTION**.
- Current experiment: **none running**. Heat-pump restarts remain paused; EXP231 used only existing captures and performed no bus TX or setting change.
- Hypothesis tested: the genuine ATEC/DCM `0708/count6` command poll is part of a pre-existing controller-side service scheduler, and comparison with the local XTR may reveal a homologous XTR-native service slot that is more relevant to write access than forcing the ATEC scheduler.
- Across the four genuine Online/DCM captures there are **54 exact `0x0F FC03 0708/count6` requests**. Every one occurs immediately after the same service-cycle context: a completed A5 `002E/count10` response precedes it by **0.262..0.394 s**, and the recurrent `0x06 FC17 AFC8/12 -> AFDC/5` poll precedes it by **0.110..0.236 s**. The normal inter-`0708` cadence is ~**4.2 s**.
- In genuine DCM rejoin capture `090550`, the first `0708` request occurs at **0.987 s**, while the first successful `0x0F FC16` ACK does not occur until **66.860 s**. Sixteen `0708` polls are unanswered before the first `0708` response at **68.235 s**. Therefore `0x0F` endpoint readiness / FC16 ACK completion does **not** activate the scheduler; the scheduler is already running controller-side while the DCM endpoint is absent.
- The visible trace does not contain the original scheduler-enable transition. Existing EXP172/173 evidence remains the best passive fingerprint: scheduler-enabled reference state uses controller `0x02 FC17 A7F8/count13` with `A811/A812=000C/0500`; local XTR uses count15 with `A811/A812=FFFF/0000`. These are correlates, not approved write targets.
- New cross-platform structural finding: local XTR cold-boot service traffic has **72 exact `0x0F FC17 read 0730/count8 + write 071C/count8` requests** across EXP221+EXP222, with median cadence ~**4.25 s**. Every local FC17 request follows the local `0x06` poll; median delay is ~**0.247 s**. This occupies the same recurring post-`0x06` scheduler position that the ATEC/DCM topology uses for its `0708` mailbox poll, although the wire transaction is different.
- EXP226 already proves the XTR FC17 write half `071C..0723` is predominantly controller RTC/date-time data. The **read half `0730..0737` remains unknown**. EXP231 therefore upgrades `0730..0737` to the highest-value **XTR-native command/service-mailbox candidate**, but does not assign field semantics or justify guessed responses.
- Important refinement to EXP227: XTR `071C/0730 FC17` and ATEC `0708 FC03` remain **not wire-equivalent** and must not be treated as the same register protocol. The new evidence is scheduler-position/cadence homology only.
- Write-access priority after EXP231: stop trying to make ordinary `0x0F` ACK completion create the ATEC `0708` scheduler. First reconstruct `0730..0737` response semantics from existing artifacts/captures; only after a safe neutral response image is evidence-backed should an active XTR FC17 responder be considered. No restart-based active test is proposed while the no-restart constraint remains.

## Authoritative experiment state
