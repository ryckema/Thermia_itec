# Thermia iTec XTR M — sync-readiness discriminator search

**Date:** 2026-10-03  
**Track:** PROTO-OFFLINE-18  
**Status:** **COMPLETE / NEGATIVE** — no independent pre-readiness bus field was found  
**Baseline:** current canonical Research state + PROTO-OFFLINE-02/15/16 + local PROTO-OFFLINE-17 result from the current research pass  
**Controlled change:** no device change. Re-align the seven genuine Eco5 boot windows and test every recurrent data-bearing bus family around the `~120 s` service-readiness boundary for a field/state transition that predicts the first accepted `03E8/count14` ACK.  
**Device TX:** none  
**YAML change:** none  
**Heat-pump reboot:** none  
**Setting write:** none  
**Live XTR experiment status:** unchanged — EXP388 remains RUNNING / PARTIAL  
**GitHub modification:** none

---

## Hypothesis

At least one already-visible controller/device field changes before the genuine gateway begins ACKing native `0x0F` configuration pages, and that field can be used as a bus-visible predictor of configuration-service readiness.

### Result

**Negative.**

No independent field in the captured bus corpus reliably predicts the transition.

The strongest model supported by the existing captures is instead:

```text
approval/session gate crossed
        AND
gateway boot/session age reaches ~120 s
        ↓
native configuration page service becomes ready
        ↓
first 03E8/count14 ACK
```

The first `03E8` ACK remains the **first direct bus-visible marker** of service readiness, not a consequence of another observed state bit.

---

# 1. Corpus and search scope

Seven genuine Eco5 boot windows were used:

- six successful Online/DCM session openings;
- one no-response/no-sync boot as a negative control.

The analysis covered all recurrent data-bearing families observed during the first ~130 s of those boots, including:

```text
0x02 FC17 A80C..A812 request-side state
0x02 FC17 response payload
0x06 FC17 AFDC..AFE0 state
0x0A room-sensor state
0x1E FC16 request payloads
0x1E FC04 response payloads
0x0F 04A6/count13
0x0F 085F/count5
0x0F 071C/0730
0x0F initial-sync pages
0x0708 mailbox when present
0xC8 traffic
```

A generic Modbus-family scan identified **25 data-bearing frame families** in the first 130 s boot windows.

Across all six successful sessions:

> **No data-bearing family had a value transition within the final 10 s before the first `03E8` ACK in all six sessions.**

At a wider 30 s window, only the `0x1E FC04 0000/count22` process-data response changes in all six, but it also changes in the failed boot and its varying words behave as ordinary process/temperature values. It is therefore not a readiness discriminator.

---

# 2. Strongest negative control: same-day failed vs successful boot

The 2026-09-26 capture provides an unusually strong control.

## Failed boot

Bus return:

```text
393.774 s
```

At about +119.5 s, the controller is still issuing `071C/0730` challenges and no approval response or native `03E8` sync has occurred.

Visible recurrent state near that point includes:

```text
A80C..A812 = 0040 0000 0008 003C 000A FFFF 0000
0x02 FC17 response = same stable 15-word state used in the later successful boot
AFDC..AFE0 = 0000 0000 0000 0000 000F
04A6/count13 starts = 0044 0001 ...
085F/count5 = all zero
```

## Later successful boot in the same capture

Bus return:

```text
603.478 s
```

Immediately before the successful challenge-#29 approval and first `03E8` ACK, the corresponding recurrent state is byte-for-byte identical for the key state families:

```text
A80C..A812
0x02 FC17 response
AFDC..AFE0
04A6/count13
085F/count5
0x1E control requests
```

The `0x1E 0000/count22` response differs only in normally varying process words.

### Strong conclusion

The failed and successful boots can reach essentially the same visible controller/peripheral state near the ~120 s boundary.

Therefore none of these recurrent state pages explains why one session is admitted and the other is not.

---

# 3. `A80C..A812` is not the missing readiness signal

The `0x02 FC17` write-side payload shows clear boot-state transitions, but they occur much earlier.

Typical 20260926 trajectory:

```text
~+0.7 s   0040 0000 0000 0005 0005 FFFF 0000
~+1.8 s   0040 0000 0008 003C 0005 FFFF 0000
~+11.3 s  0040 0000 0008 003C 000A FFFF 0000
~+64 s    ... 0028 ...
~+81 s    ... 0008 ...
```

The failed boot shows the same sequence.

The 20260928 boots have another repeatable trajectory with changes around ~56–67 s, again shared by early-approval, late-approval and successful sessions.

### Classification

**DISPROVEN as a unique sync-readiness discriminator.**

These words remain useful controller lifecycle context, but no state transition in them consistently precedes the first `03E8` ACK.

---

# 4. `AFDC..AFE0` is not the missing readiness signal

The `0x06 FC17` state also changes during boot.

Examples:

```text
20260926:
~+1 s    0000 0000 0000 0000 003C
~+5.6 s  0000 0000 0000 0000 000F/0010
~+64 s   0020 0000 0000 0000 ...
~+81 s   0000 ...
```

```text
20260928:
~+1 s    ... 003C
~+5.6 s  ... 0015
~+60 s   0010 0000 0000 0000 0015
```

The no-response boot follows the same family of transitions as successful boots.

### Classification

**DISPROVEN as a unique sync-readiness discriminator.**

This is consistent with the existing project result that expansion/accessory/version state and Online semantic session state are not equivalent.

---

# 5. `0x1E` process traffic does not expose the gate

The recurring `0x1E FC04 0000/count22` response begins with zeros after boot, then fills with live process values and continues changing.

There is no single word transition common to all six successful sessions near configuration-service readiness.

The failed 20260926 boot also has a process-data change at approximately +119.8 s despite never receiving approval and never entering native configuration sync.

Other `0x1E` request/response families remain stable across the compared boundary.

### Classification

**No readiness discriminator found.**

The changing words should continue to be treated as process/runtime data unless separately identified.

---

# 6. `04A6` and `085F` do not discriminate readiness

`04A6/count13` cannot serve as the missing readiness flag.

Within 20260926:

```text
failed boot near ~120 s:
04A6 begins 0044 0001 ...

successful later boot near ~120 s:
04A6 begins 0044 0001 ...
```

The first successful boot instead has zeros in those words.

This agrees with the earlier finding that `04A6/04A7` correlate with operating/SG context in some regimes rather than Online approval.

`085F/count5` is all-zero in the compared successful and failed readiness windows.

### Classification

```text
04A6 readiness flag: DISPROVEN
085F readiness flag: NOT SUPPORTED
```

---

# 7. `0708` is too late to be the predictor

The first `0708/count6` mailbox polls in the successful sessions occur much later than the initial `03E8` service-ready boundary:

```text
~154 .. 187 s after bus return
```

They belong to established runtime/scheduler behavior after the ordered configuration transfer has already begun.

### Classification

**Not a pre-readiness discriminator.**

---

# 8. No `0xA5` evidence exists in this Eco5 corpus

Neither genuine Eco5 capture contains frames addressed to slave `0xA5`.

Therefore `0xA5` cannot be evaluated as a candidate readiness source from these two captures.

This is an evidence limitation, not evidence that `0xA5` is irrelevant elsewhere.

---

# 9. What *does* predict readiness in the current corpus?

No independent field does.

The best supported joint condition is:

```text
A. approval has been accepted
B. boot/session age is approximately 120 s
```

Evidence:

- two challenge-#3 approvals are accepted around +10 s;
- their controllers immediately start retrying `03E8`;
- the gateway withholds the ACK until +118.478 / +118.550 s;
- four challenge-#29 approvals occur around +120 s and receive an immediate `03E8` ACK;
- the failed boot passes +120 s without approval and never enters `03E8` sync.

So:

```text
time >= ~120 s
```

is **not sufficient**, and:

```text
approval accepted
```

is **not sufficient for immediate page service**.

Together they fit every observed boot.

### Important limit

This is a corpus-level state model, not proof of the gateway's internal implementation.

The ~120 s condition may be:

- a gateway-local startup timer;
- cloud/network registration readiness;
- retained/binding state;
- protocol-package/service initialization;
- another internal condition correlated with elapsed time.

The bus capture cannot distinguish these.

---

# 10. First bus-visible readiness marker

The first accepted:

```text
0F 10 03E8 000E ...
<->
0F 10 03E8 000E <CRC>
```

is the earliest direct proof that the gateway's native page service is active.

After this ACK, `03FC/count11` follows within about:

```text
0.373 .. 0.481 s
```

across all six successful sessions.

Therefore diagnostics/reference models should distinguish:

```text
APPROVED
WAITING_FOR_PAGE_SERVICE
SYNC_ACTIVE
```

rather than collapsing approval and synchronization into one state.

---

# 11. Exhaustive transition-search result

For each successful boot, all data-bearing Modbus families in the first 130 s were reduced to value-change events.

Intersection results:

```text
common value-changing family within  0.5 s before first ACK: none
common value-changing family within  1.0 s before first ACK: none
common value-changing family within  2.0 s before first ACK: none
common value-changing family within  5.0 s before first ACK: none
common value-changing family within 10.0 s before first ACK: none
```

At 30 s:

```text
only 0x1E FC04 0000/count22 process data changes in every success
```

but the failed boot does the same, so it is rejected.

This makes a hidden **gateway-internal or non-bus-observed readiness state** the strongest remaining explanation.

---

# Evidence classification

## Observed facts

- six successful and one failed genuine Eco5 boot windows were compared;
- 25 data-bearing frame families occur in the first 130 s windows;
- no data-bearing family has a common value transition within 10 s of first `03E8` ACK across all six successes;
- failed and successful 20260926 boots share byte-identical key recurrent state near +120 s;
- the failed boot continues `071C/0730` challenge traffic past the ~120 s boundary;
- `0708` appears only later in established runtime;
- no `0xA5` frames occur in these two Eco5 captures.

## Strong conclusions

1. No independent captured bus field predicts genuine Eco5 configuration-service readiness.
2. `A80C..A812`, `AFDC..AFE0`, `04A6`, `085F`, and the observed `0x1E` state/process traffic are not the missing universal discriminator.
3. The current corpus is fully consistent with a two-condition model: **approval accepted + ~120 s gateway/session age**.
4. The first `03E8` ACK is the first direct bus-visible readiness marker.
5. The missing readiness state is most likely internal to the gateway or otherwise not represented in the captured RS485 fields.

## Hypotheses

- gateway-local timer/state machine controls the ~120 s service activation;
- network/cloud or registration readiness may be involved;
- protocol-package/service initialization may be involved;
- retained approval state may explain why some sessions answer challenge #3 rather than #29.

These remain hypotheses.

## Unknowns

- exact internal source of the ~120 s boundary;
- whether modern Thermia Connect behaves similarly;
- whether other Thermia controller generations expose a readiness field not present here;
- whether unobserved side channels or gateway-local software state determine the transition;
- role of `0xA5` in other topologies.

---

# Result

**PROTO-OFFLINE-18 — COMPLETE / NEGATIVE**

The search did **not** find a hidden RS485 field that announces configuration-service readiness before `03E8` is ACKed.

The practical protocol model is now narrower:

```text
approval accepted
      ↓
WAITING_FOR_PAGE_SERVICE
      ↓    (genuine Eco5: around 120 s after bus return)
first 03E8 ACK
      ↓
SYNC_ACTIVE
```

No live experiment was advanced, no write target was introduced, and EXP388 remains RUNNING / PARTIAL.