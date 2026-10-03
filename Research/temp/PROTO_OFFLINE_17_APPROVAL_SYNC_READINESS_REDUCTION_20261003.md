# Thermia iTec XTR M — approval vs sync-readiness reduction

**Date:** 2026-10-03  
**Track:** PROTO-OFFLINE-17  
**Status:** **COMPLETE / POSITIVE** — offline evidence analysis only  
**Baseline:** PROTO-OFFLINE-02, PROTO-OFFLINE-15, PROTO-OFFLINE-16, both genuine Eco5 + Thermia Online gateway captures  
**Controlled change:** re-align all six successful genuine Eco5 session openings by controller bus return and by the *first accepted `03E8/count14` FC16 ACK*, rather than treating the 16-byte FC17 approval response as the single session-ready transition.  
**Device TX:** none  
**YAML change:** none  
**Heat-pump reboot:** none  
**Setting write:** none  
**Live XTR experiment status:** unchanged — EXP388 remains RUNNING / PARTIAL  
**GitHub modification:** none

---

## Hypothesis

The genuine Online/DCM startup has at least two separable gates:

1. the `071C/0730` 16-byte approval/session-opening response is accepted by the controller;
2. the gateway's native `0x0F` page service becomes ready to ACK the initial `03E8/count14` configuration page and continue ordered synchronization.

If this is true, a successful approval response may occur substantially before the gateway is willing to ACK `03E8`.

---

# 1. Six successful genuine sessions re-aligned

| Capture | Boot return | Response ordinal | Approval after boot | First 03E8 ACK after boot | Approval -> ACK | UnACKed 03E8 before ACK | 03E8 ACK -> 03FC |
|---|---:|---:|---:|---:|---:|---:|---:|
| 20260926 | 183.462 s | #29 | 120.153 s | 120.290 s | 0.137 s | 0 | 0.373 s |
| 20260926 | 603.478 s | #29 | 119.808 s | 119.930 s | 0.122 s | 0 | 0.414 s |
| 20260928 | 193.555 s | #29 | 120.173 s | 120.296 s | 0.123 s | 0 | 0.402 s |
| 20260928 | 438.000 s | #3 | 9.825 s | 118.478 s | 108.653 s | 102 | 0.415 s |
| 20260928 | 734.310 s | #3 | 10.043 s | 118.550 s | 108.507 s | 102 | 0.481 s |
| 20260928 | 974.803 s | #29 | 119.914 s | 120.038 s | 0.124 s | 0 | 0.401 s |

Across all six sessions the first accepted `03E8` ACK occurs:

```text
mean   119.597 s after bus return
range  118.478 .. 120.296 s
spread 1.818 s
```

This is much tighter than the approval-response timing, which occurs either at about 10 s or about 120 s.

---

# 2. Early approval does not mean native page service is ready

The two challenge-#3 sessions are decisive.

## Boot at 438.000 s

```text
+  9.795 s  challenge #3
+  9.825 s  genuine 16-byte FC17 approval response
+ 10.307 s  controller starts FC16 03E8/count14
...
+118.416 s  same 03E8/count14 request again
+118.478 s  first 03E8/count14 ACK
+118.893 s  controller advances to 03FC/count11
```

Between approval and the first ACK:

- `102` controller `03E8/count14` request frames were sent;
- all 102 carried the same page payload;
- there were no gateway FC16 ACKs for that page before the final one;
- no `0x0F` FC03 response was observed in that waiting interval.

## Boot at 734.310 s

The same pattern repeats independently:

```text
+ 10.011 s  challenge #3
+ 10.043 s  genuine approval response
+ 10.508 s  first 03E8/count14 request
...
+118.519 s  repeated 03E8/count14 request
+118.550 s  first 03E8/count14 ACK
+119.031 s  03FC/count11 follows
```

Again there are exactly `102` unACKed `03E8` requests before the first accepted ACK.

### Observed fact

The controller accepts the early approval response immediately: challenge traffic stops and the controller moves into the `03E8` initial-sync phase.

### Strong conclusion

**Approval acceptance and native settings-sync readiness are distinct bus-visible states.**

The 16-byte FC17 response is therefore a session-opening/approval gate, but it is not itself proof that the genuine gateway is ready to service the configuration transfer.

---

# 3. Challenge #29 is the late case where the two gates coincide

In four other successful sessions the gateway responds at challenge #29, around 120 s after bus return.

In those cases:

```text
approval response
   -> 122..137 ms
03E8 ACK
   -> 373..414 ms
03FC next stage
```

There is no long `03E8` retry interval.

The simplest bus-level model is therefore:

```text
controller boot
   |
   v
071C/0730 challenge polling
   |
   +---- Gate A: approval token accepted
   |          |
   |          v
   |      controller starts/retries 03E8
   |
   +---- Gate B: genuine gateway native page service ready
              |
              v
          ACK 03E8
              |
              v
          03FC and ordered initial sync
```

When Gate A happens at ~10 s, Gate B is still closed for about 108.5 s.

When Gate A happens at ~120 s, Gate B is already available and the first `03E8` is ACKed immediately.

---

# 4. A 120 s elapsed-time condition is not sufficient by itself

The 20260926 middle boot is an important negative control.

It begins at:

```text
393.774 s
```

and produces `41` exact `071C/0730` challenges through approximately:

```text
+171.230 s
```

No approval response is sent.

During that session:

- no `03E8` initial-sync phase begins;
- there are no gateway FC16 ACKs;
- there are no gateway FC03 responses.

### Strong conclusion

Passing the ~120 s point alone is not sufficient to activate native configuration transfer.

The approval/session gate must also be crossed.

The internal implementation may use a timer, cloud/session readiness, retained gateway state or another private condition; the captures cannot distinguish those possibilities.

---

# 5. Controller-side startup state does not explain early vs late approval

The 20260928 boots have near-identical visible controller startup trajectories regardless of whether the gateway answers challenge #3 or challenge #29.

Typical sequence:

```text
A80E/A80F/A810
~+0.5..0.7 s   0 / 5  / 5
~+1.55..1.77 s 8 / 60 / 5
~+11.0..11.3 s 8 / 60 / 10
```

The #3 response happens just before the `A810 5 -> 10` transition, but the same transition occurs in the #29 sessions where no early response is sent.

### Strong conclusion

The early-vs-late response choice is not explained by the currently visible `A80E/A80F/A810/AFDC` controller trajectory.

The missing discriminator is more likely gateway-internal or external to the observed controller state.

This is consistent with, but does not prove, a retained gateway session, cloud readiness, approval cache, internal startup phase or similar state.

---

# 6. `03E8` ACK is the practical sync-start boundary

Once the first `03E8/count14` ACK occurs, the controller advances to `03FC/count11` in all six sessions within:

```text
0.373 .. 0.481 s
```

This is independent of whether approval occurred at challenge #3 or challenge #29.

### Strong conclusion

For genuine Eco5/Online traces, the first accepted `03E8` ACK is the cleanest bus-visible boundary between:

```text
session opened / controller waiting for gateway
```

and:

```text
ordered native configuration synchronization actively progressing
```

The project should therefore keep these two states separate in reference models and diagnostics.

---

# 7. Relation to the local XTR emulator

PROTO-OFFLINE-02 already established that the local XTR M accepts the same fixed genuine R1 token against multiple different local request payloads.

The local write/session work then ACKs the native sync pages without reproducing the genuine Eco5 ~120 s delay, and successful complete synchronization has been locally observed.

### Strong conclusion

The ~120 s readiness boundary is **not a mandatory controller protocol delay** for the locally tested XTR M.

It is better treated as behavior of the genuine Eco5 gateway/session implementation.

A future generic emulator should therefore model:

```text
approval/session-open state
```

and:

```text
configuration-service-ready state
```

as separate concepts, without hard-coding a 120 s wait as a universal Thermia requirement.

---

# 8. Impact on ECO-WRITE-01

The current ECO-WRITE-01 information criterion remains correct:

```text
known-good replay at challenge #3
-> if controller begins FC16 03E8/count14
   then the replay was accepted as a session-opening response
```

The genuine captures now add an important interpretation rule:

- an accepted challenge-#3 approval can legitimately be followed by a long period of repeated, unACKed `03E8`;
- therefore `03E8` appearance is the approval criterion;
- `03E8` ACK is a separate gateway/synchronization-service criterion.

ECO-WRITE-01 deliberately does not ACK `03E8`, so no experiment widening is required.

---

# 9. Firmware / Connect archaeology impact

PROTO-OFFLINE-15 identified DCM03 firmware and Thermia Connect/protocol packages as the strongest serializer targets.

PROTO-OFFLINE-17 narrows what to search for inside those artifacts.

High-value strings/state machines are now not only:

```text
challenge
approval
authentication
pairing
```

but also concepts resembling:

```text
initial sync
settings transfer
configuration ready
protocol package ready
online/cloud ready
registration
approval cache
startup delay / retry timer
```

A crypto routine alone would not explain the observed two-gate behavior.

---

# 10. Evidence classification

## Observed facts

- six successful genuine approval events are present across the two Eco5 gateway captures;
- four responses occur at challenge #29, about 120 s after bus return;
- two responses occur at challenge #3, about 10 s after bus return;
- both early responses immediately cause the controller to begin `03E8/count14`;
- in each early-response session, 102 identical `03E8` requests occur before the first ACK;
- first accepted `03E8` ACK occurs at 118.478..120.296 s after bus return in all six successful sessions;
- after that ACK, `03FC/count11` follows within 0.373..0.481 s;
- one no-response boot continues challenge polling beyond 120 s and never enters configuration sync;
- visible controller startup state trajectories are near-identical in early- and late-response boots.

## Strong conclusions

1. The 16-byte `071C/0730` response and native page-service readiness are separate bus-visible gates.
2. Early approval can be accepted roughly 108.5 s before the genuine gateway begins ACKing the initial configuration page.
3. The first accepted `03E8` ACK is the cleanest marker for actual ordered configuration-sync progression.
4. Elapsed time alone is insufficient; approval must also occur.
5. The #3-versus-#29 choice is not explained by the currently observed controller lifecycle fields.
6. The genuine Eco5 ~120 s page-service readiness behavior must not be generalized into a mandatory XTR controller delay.

## Hypotheses

- the ~120 s boundary is a gateway-internal readiness/startup timer;
- #3 responses may use retained/cached gateway approval state;
- #29 responses may represent a cold/full gateway readiness path;
- cloud/session/network readiness may influence which approval opportunity is used.

None of these internal explanations is proven by the bus captures.

## Unknowns

- exact gateway-internal condition selecting challenge #3 versus #29;
- whether gateway power state, network/cloud state or retained approval state is the discriminator;
- whether other Thermia generations use the same timing;
- actual response-generation algorithm;
- how this state machine is represented inside DCM03 or Thermia Connect firmware/protocol packages.

---

# Result

**PROTO-OFFLINE-17 — COMPLETE / POSITIVE**

The genuine Online/DCM startup is now better modeled as:

```text
approval accepted
       !=
configuration service ready
```

with a reproducible genuine Eco5 configuration-service boundary near 120 s after controller bus return in all six successful sessions.

No live Thermia experiment was advanced or closed by this offline result.