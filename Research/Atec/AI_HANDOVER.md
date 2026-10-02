# AI HANDOVER — Thermia ATEC / DHP-AQ side branch

Last updated: **2026-10-02**

## 0. Mandatory source discipline

This handover is a continuation aid. Project-wide source order remains:

1. newest `Research/THERMIA_PROJECT_STATE.md`
2. newest confirmed result in `Research/EXPERIMENT_LOG.md`
3. `Research/PROTOCOL_FINDINGS.md`
4. raw capture/log
5. YAML used
6. older notes/chats

For ATEC wire behavior, raw ATEC/Eco captures outrank this handover.

Do not promote XTR-local evidence to ATEC-local proof.

---

# 1. Current ATEC state

**ATEC-EXP1 — PREPARED / NOT RUN**

Active implementation:

`Research/Atec/thermia_atec_waveshare_atec_exp1_queued_room_setpoint.yaml`

The file is now an integrated v0.2 build: full passive ATEC/DHP-AQ decoder + the bounded EXP1 `03F4` semantic write engine.

Passive-only alternative:

`Read-only/ATEC/thermia_atec_waveshare_readonly_v01.yaml`

No target ATEC EXP1 result has been supplied.

Do not mark the experiment complete.

---

# 2. Why v0.2 exists

The earlier EXP1 YAML was a small protocol harness. The user requested an ATEC file at a maturity level similar to XTR Write Beta v4.1.

v0.2 therefore adds:

- the full passive ATEC/DHP-AQ decoder;
- persisted validated `03E8` settings;
- normal Thermia telemetry and bus diagnostics;
- ATEC candidate page diagnostics;
- 120-second raw capture;
- detailed active-runtime counters;
- runtime qualification sensor;
- queue state;
- settings-snapshot progress;
- 15-minute soak marker;
- production-style Configuration control naming.

The protocol write scope itself is deliberately still narrow.

---

# 3. Controlled experimental change

Baseline:

previous ATEC-EXP1 — **PREPARED / NOT RUN**.

Hypothesis:

unchanged.

Semantic write target:

unchanged — only `03F4`.

Active selector:

unchanged:

```text
0000 0001 0000 0001 0000 0000
```

Idle response:

unchanged:

```text
0000 0000 0000 0000 0000 0000
```

FC17:

still **capture-only / NO TX**.

Material implementation correction:

the manual broad settings-refresh sequencer is now based on the exact 26 pages selected by the captured `FFFF:867F` PUSH bitmap instead of assuming all 32 page-map entries are emitted.

---

# 4. Exact 0708 snapshot bitmap

Captured response:

```text
W0 W1 W2   W3   W4   W5
0000 0000 FFFF 867F 03DF 0000
```

Raw frame:

```text
0F 03 0C 0000 0000 FFFF 867F 03DF 0000 66 AD
```

The page map is still 32 bits, but this bitmap sets only 26 PUSH bits.

## Selected low-half W3 pages

`867F` sets page bits:

`0,1,2,3,4,5,6,9,10,15`

Therefore:

```text
03E8 03FC 0410 042E 0442 0456 046A 04A6 04BA 0532
```

It does NOT select:

```text
047E 0492 04D8 04F6 050A 051E
```

## Selected high-half W2 pages

`FFFF` selects all pages 16..31:

```text
0546 055A 057B 059C 05BD 05DE 05FF 0620
0641 0662 0683 06A4 06C5 06EA 06F1 06F4
```

Total:

**26 config pages**.

This is directly supported by raw capture following the bitmap.

---

# 5. Exact ATEC-EXP1 snapshot ACK order

```text
03E8/14
03FC/11
0410/22
042E/15
0442/13
0456/12
046A/18
04A6/13
04BA/22
0532/18
0546/20
055A/33
057B/33
059C/33
05BD/33
05DE/33
05FF/33
0620/33
0641/33
0662/33
0683/33
06A4/33
06C5/33
06EA/7
06F1/3
06F4/19
```

Known runtime pages may interleave and are ACKed through the separate runtime whitelist.

Immediate retry of the previous expected snapshot page is accepted up to three times.

No other configuration page is ACKed merely because it belongs to the global 32-page map.

---

# 6. 0708 mailbox model

Current strongest model:

- W1 = low-half desired-page/PULL bitmap;
- W2:W3 = 32-bit current-page PUSH/refresh bitmap;
- W0 = possible high-half desired-page field, unproven;
- W4/W5 = lifecycle/status/session fields, unresolved.

Across the two primary gateway logs:

- 264 paired `0708/count6` replies;
- 197 are six-zero replies;
- non-zero lifecycle/status W4 states exist.

ATEC-EXP1 uses the dominant six-zero steady-state reply and does not synthesize unknown lifecycle states.

---

# 7. Strongest semantic evidence

`03F4` / decimal 1012 / `03E8` word12.

Raw gateway captures contain a desired-page round trip where the page differs only at `03F4` and the controller republishes the changed page.

ATEC-EXP1 therefore changes exactly one word.

No other ATEC setting is writable in v0.2.

Candidate fields in `0410`, `042E`, `0442`, and `0546` are passive diagnostics only.

---

# 8. FC17 evidence

Across the two primary gateway logs:

- 163 exact `071C/0730` challenges;
- six exact 16-byte responses.

A general transform is unknown.

XTR EXP386/387/388 session recovery is local XTR evidence only.

ATEC v0.2 does NOT:

- replay an R1;
- synthesize an FC17 response;
- use the XTR A80E/A80F R1 permission rule.

Any `0x0F FC17` challenge is logged/counted and left unanswered.

---

# 9. Active runtime state

```text
stage 0  passive 10 s peer qualification
stage 40 captured ATEC runtime service
stage 99 fail-closed stop
```

Full passive decoding continues during stage0.

Stage40 requires a fresh live bus and no peer responder.

Semantic dispatch additionally requires:

- >=1 known FC16 ACK;
- >=1 `0708` reply;
- unknown FC16 = 0;
- unknown FC03 = 0;
- peer = 0;
- parser resync delta = 0;
- RX drop delta = 0.

Any parser/RX delta stops active TX.

---

# 10. Active TX whitelist

Permitted TX classes:

1. exact six-zero `0708` idle response;
2. exact manually armed 26-page refresh bitmap;
3. exact `03E8` desired selector;
4. dynamic desired `03E8/count14` response made from a fresh authoritative cache with only word12 changed;
5. standard FC16 address/count ACK for:
   - exact selected snapshot pages while snapshot is active;
   - known runtime pages;
   - `03E8/count14`.

No other traffic is answered.

`04A6/count13` remains capture-only outside its exact selected position in the manual snapshot.

---

# 11. Semantic room write

Preconditions:

- stage40;
- clean runtime qualification;
- no snapshot/other write active;
- fresh `03E8` cache <=60 s;
- target integer 20..30 °C.

Flow:

```text
fresh 03E8
-> next genuine 0708
-> selector 0000,0001,0000,0001,0000,0000
-> controller FC03 03E8/count14
-> desired page with only word12 changed
-> controller FC16 03E8/count14
-> ACK
-> compare all 14 words
```

Positive:

target at word12 and all 13 other words equal cached original.

Negative:

word12 remains original and all other words equal.

Inconclusive:

anything else.

---

# 12. Queue behavior

One active transaction maximum.

One pending room target maximum.

Latest pending user intent wins.

1.5 s UI debounce.

>=2 s settle after a confirmed/no-op transaction.

No automatic semantic retry after failure.

Pending intent is dropped when the active runtime/write guard is no longer eligible.

---

# 13. Home Assistant controls

Under Configuration:

- `02 Heating | 00 Room Setpoint (ATEC EXP1)`
- `ATEC | Request Settings Snapshot`
- `ATEC | Abort Experimental TX`
- `Log 120 Seconds`

The passive ATEC/DHP-AQ monitoring entities are retained from the read-only baseline.

---

# 14. First live test

1. Boot.
2. Wait for:
   ```text
   PREFLIGHT_PASSED peer=0 busFresh=1 ENTER_STAGE40 DE=LOW
   ```
3. Confirm **ATEC Write Runtime Qualified = ON** with unknown03/unknown16/peer/resync/drop all zero.
4. Press **ATEC | Request Settings Snapshot**.
5. Require:
   ```text
   SETTINGS_SNAPSHOT_COMPLETE pages=26
   ```
6. Record current room setpoint.
7. Change by 1 °C only.
8. Wait for first terminal semantic result.
9. If positive, restore original value through the same path.

Do not queue-stress the first run.

---

# 15. Smallest useful returned log

Start at:

`PREFLIGHT_PASSED`

End after:

- `SETTINGS_SNAPSHOT_COMPLETE pages=26`; or
- first `WRITE_CONFIRMED`; or
- first negative/inconclusive marker; or
- any stop/abort marker.

Also include any:

- `UNKNOWN_0F_FC16`
- `UNKNOWN_0F_FC03`
- `0F_FC17_CAPTURE_ONLY`
- `PEER_RESPONDER_STOP`
- parser-resync/drop line.

---

# 16. Status discipline

Current:

**ATEC-EXP1 — PREPARED / NOT RUN**

Do not advance to EXP2 just because v0.2 exists.

The v0.2 upgrade is an implementation/safety consolidation plus correction of the snapshot page sequencer. It is not a positive experiment result.

---

# 17. Validation performed

Static validation before GitHub publication checks:

- every ESPHome `id(...)` reference resolves;
- no duplicate IDs;
- one critical top-level YAML section each;
- exact known mailbox frames retained;
- exact 26-page snapshot list present;
- exactly one UART write helper call;
- exactly one DE-HIGH path;
- DE restore is ALWAYS_OFF;
- no hard-coded FC17 response frame.

ESPHome compile verification is not claimed.

---

# 18. Immediate next action

Run ATEC-EXP1 v0.2.

Do not add writes for `041D`, `042E`, `0442`, `0553`, `0559` or other candidate fields before EXP1 is closed with a real target log.
