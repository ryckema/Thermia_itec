# EXP249 — Passive 071C/0730 natural-stop repeatability

**Status:** COMPLETE / VALID PASSIVE POSITIVE

## Hypothesis

EXP248's natural `071C/0730` stop is governed by a repeatable startup/service mechanism.

## Result

```text
first target       +1.283 s
target count       63
median cadence     4.293 s
last target        +266.821 s
final state        A80E=0028 A80F=000A AFDC=0010
confirmed silence  80.974 s
0x06 polls         87
false stops        0
parser resync Δ    0
RX drop Δ          0
```

## Comparison with EXP248

```text
                 EXP248        EXP249
first target     1.283 s       1.283 s
target count     63            63
median cadence   4.298 s       4.293 s
last target      267.123 s     266.821 s
final state      0028/000A/0010 identical
```

The final-target difference is only **302 ms**.

Meaningful early A80E/A80F/AFDC transitions reproduce within about 11 ms.

## Strong conclusions

- The unanswered local XTR approval/service lifecycle is highly deterministic across cold boots.
- The natural stop is reproducible in both time and request count.
- No monitored A80E/A80F/AFDC edge exposes the cutoff.
- No retry backoff occurs.

## Remaining ambiguity

A ~270 s deadline and a fixed 63-request budget both fit the two runs because first-target phase and cadence are themselves almost identical.

No `0730` response was sent or learned.
