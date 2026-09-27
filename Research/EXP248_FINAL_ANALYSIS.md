# EXP248 — Passive 071C/0730 natural-stop trace

**Status:** COMPLETE / VALID PASSIVE POSITIVE

## Hypothesis

After one controlled XTR controller cold boot with no genuine Online/DCM endpoint, the exact
`0x0F FC17 read 0730/count8 + write 071C/count8` service/approval request retries for a finite
startup window and then stops naturally.

## Safety / experimental variable

Only experimental variable: one controlled Thermia/controller cold boot.

The ESP remained powered and the experiment stayed RX-only:
- no RS485 TX;
- no ACK;
- no `0730` response;
- no probe/scan;
- no setting mutation;
- no room-sensor emulation;
- no production functionality change.

## Attempt 1 — aborted setup/control

- Armed at 14:55:38.670.
- No >=6 s bus gap occurred within 60 s.
- Auto-abort at 14:56:38.968.
- No protocol result from this attempt.

This confirms the boot-gap guard fails closed.

## Attempt 2 — valid complete run

- ARM: 14:57:25.491
- BUS_GAP >=6 s: 14:57:53.961
- BUS_RETURN: 14:58:01.042
- first target: +1.283 s
- targets: **63**
- last target: **+267.123 s**
- last state: `A80E=0028 A80F=000A AFDC=0010`
- target cadence: median **4298 ms**
- STOP_CANDIDATE: after 20.793 s target silence
- SUMMARY CONFIRMED_STOP: final silence **80.793 s**
- false stops: **0**
- parser resync delta: **0**
- RX drop delta: **0**
- observed 0x06 polls: **86**

## Observed facts

The first target appears 1.283 s after bus return. Early state progression completes within about 11.3 s, but the target stream continues. The retry cadence remains essentially constant until target 63.

Target 63 occurs at +267.123 s with `A80E=0028 A80F=000A AFDC=0010`. Ordinary controller/0x06/room/outdoor traffic remains alive afterward. No new target appears during the full configured confirmation interval.

## Strong conclusions

1. The local XTR unanswered `071C/0730` startup/service retry stream has a real natural stop.
2. The final observed request occurs at **267.123 s after BUS_RETURN**.
3. The stream does not stop because the RS485 bus stops; ordinary traffic continues.
4. No visible `A80E/A80F/AFDC` transition coincides with the stop.
5. No gradual retry backoff is present.
6. The failed first arm is a setup/control negative, not a protocol failure.

## Hypotheses

A ~270 s controller deadline is the leading timing hypothesis. With the measured cadence, the next request would normally be expected near +271.421 s, placing a 270 s cutoff naturally between target 63 and the suppressed next request.

A fixed retry budget or an unobserved internal state remains possible.

## Unknowns

- repeatability across cold boots;
- exact timer versus retry counter;
- internal state edge that suppresses the next target;
- genuine XTR `0730..0737` response semantics;
- behavior after a valid genuine Online response.

## Negative results

- no visible monitored-state edge at the stop;
- no retry backoff;
- no false stop;
- no parser corruption;
- no `0730` value learned or tested.

## Next experiment

**EXP249 — passive repeatability of the natural-stop deadline.**

Repeat the same RX-only cold boot once and compare first target, target count, last target, cadence and monitored state. No TX.
