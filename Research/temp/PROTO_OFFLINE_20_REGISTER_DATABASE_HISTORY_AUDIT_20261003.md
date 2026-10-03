# Thermia iTec XTR M — register database + experiment-history audit

**Date:** 2026-10-03  
**Track:** PROTO-OFFLINE-20  
**Status:** **COMPLETE / POSITIVE** — canonical/database inconsistencies identified and a reconciled overlay prepared  
**Baseline:** newest `Research/THERMIA_PROJECT_STATE.md`, current `Research/EXPERIMENT_LOG.md`, current `Research/PROTOCOL_FINDINGS.md`, PROTO-OFFLINE-13/14/16, current protocol-reduction CSVs, Write Beta v4.1 header, plus PROTO-OFFLINE-17/18/19 from the current offline pass  
**Controlled change:** none on device. Audit only. No bus TX, YAML behavior change, restart or setting write.  
**Live experiment status:** unchanged — EXP387 remains last fully completed live experiment; EXP388 remains RUNNING / PARTIAL.  
**GitHub modification:** none.

---

## Hypothesis

The project has accumulated enough later local proof that some database rows and current-summary statements are stale relative to the actual evidence, even though the historical experiment records themselves should remain untouched.

A useful audit should:

1. preserve historical observations and negative results;
2. distinguish an old hypothesis from its current status;
3. merge post-PROTO-OFFLINE-16 local write proof back into the register database;
4. identify canonical inconsistencies instead of silently rewriting them;
5. explicitly mark archive gaps rather than reconstructing missing experiments from memory.

**Result: positive.** Several real stale/current inconsistencies were found.

---

# 1. Audit coverage and limitation

The current GitHub `Research/EXPERIMENT_LOG.md` contains:

```text
137 unique numbered experiment IDs
earliest header: EXP92
latest header:   EXP386
```

Within the numeric range `EXP1..EXP388`, **251 numbers have no experiment header in the current canonical log**.

This does **not** mean 251 experiments were necessarily run and lost. Some numbers may have been unused, superseded before a run, documented elsewhere, or absent from the current consolidated log.

Therefore PROTO-OFFLINE-20 does **not** invent an EXP1..91 or other missing history.

The audit is complete for:

- every numbered experiment record actually present in the current canonical experiment log;
- the current-state records for EXP387/388;
- Write Beta v4.1's explicit EXP387/388 status header;
- all current durable register/protocol databases reviewed here.

### Canonical gap discovered

`THERMIA_PROJECT_STATE.md` and Write Beta v4.1 both state:

```text
EXP387 COMPLETE / POSITIVE
EXP388 RUNNING / PARTIAL
```

but the current `EXPERIMENT_LOG.md` has no EXP387 or EXP388 experiment header.

That is a documentation gap, not evidence against the experiments.

The safest correction is to add concise canonical entries using only the already-recorded state/YAML facts, without reconstructing missing raw details.

---

# 2. Major database finding: PROTO-OFFLINE-16 is now a historical snapshot

`PROTO_OFFLINE_16_NATIVE_REGISTER_DATABASE_20261003.csv` was valuable, but several of its evidence levels are now older than the later local live results already present in the experiment log/current semantic map.

Examples:

```text
PROTO16:
03E9 Heating Minimum       STRONGLY SUPPORTED
03EA Heating Maximum       STRONGLY SUPPORTED
03EC Curve 0               STRONGLY SUPPORTED
03ED Curve -5              STRONGLY SUPPORTED
03EE Heating Stop          STRONGLY SUPPORTED
03EF Reduced Temperature   OPEN / historical candidate
03F0 Room Factor           STRONGLY SUPPORTED

later local evidence:
all above are PROVEN / locally confirmed writable
```

The later evidence comes from the EXP365–375 live write series and must outrank the older offline-only classification.

Similarly:

```text
PROTO16:
042E local semantic OPEN
042F semantic OPEN
0553 desired scheduler bit not observed
```

whereas later local evidence establishes:

```text
042E = Hot Water Enabled
042F = Hot Water Mode
0553 = Operation Mode
```

and the local desired-page machinery for those controlled pages is already proven where recorded.

### Strong conclusion

PROTO-OFFLINE-16 remains useful as a cross-profile comparison and historical evidence snapshot, but it must not be used as the current XTR write-confidence database without applying the later live-experiment upgrades.

The current `thermia_protocol_semantic_register_map.csv` already contains many of those upgrades and is the better settings baseline.

---

# 3. Current semantic-register map still contains stale rows

The current semantic CSV is newer than the PROTO16 working database for many settings, but several durable findings have not yet been folded back into it.

## 3.1 `0424`

Current CSV:

```text
0424 = Unknown dynamic field
OPEN / UNKNOWN
```

Current durable protocol finding:

```text
0424 = Returnline Temperature Max Limit
STRONGLY SUPPORTED
```

The stronger label comes from the cross-model contiguous sequence anchored locally by `041D` and `041E`.

**Audit action:** upgrade `0424` in the semantic database to STRONGLY SUPPORTED, while explicitly retaining “not one-variable locally proven”.

## 3.2 `04A6/04A7`

Current CSV still calls both unknown.

Later local XTR evidence gives:

```text
SG Normal   -> 04A6=0000 / 04A7=0000
SG Enhanced -> 04A6=0041 / 04A7=0001
SG Blocked  -> 04A6=0042 / 04A7=0001
```

This is a strong local operational/SG correlation.

It must still remain context-qualified because an older local `04A6/count13` payload regime is radically different.

**Audit action:** upgrade these two fields to STRONGLY SUPPORTED / locally correlated, not to universal fixed-schema semantics.

## 3.3 `06F4..06F8` and `0701`

The semantic CSV still has some of these as generic unknown dynamic fields or omits explicit rows.

The structural relations are directly observed:

```text
06F4 = A80C
06F5 = A80D
06F6 = A80E
06F7 = A80F
06F8 = A810
0701 = AFDC
```

**Audit action:** record the mirror relation as PROVEN while leaving the source-field human meanings at their existing evidence levels.

## 3.4 `0870`

Current semantic CSV:

```text
Runtime word0; equals (06E3<<8)|06E2
semantics OPEN
```

Current durable finding:

```text
0870 = Compressor Operating Time
STRONGLY SUPPORTED
```

**Audit action:** upgrade the semantic label; retain exact raw scaling/unit caveat where not locally reduced.

## 3.5 Operating-time / defrost rows

The current semantic map does not yet contain the complete sparse runtime group established by PROTO16:

```text
0872 Heating operating time
0873 Cooling operating time
0874 OPEN
0875 OPEN
0876 Hot-water operating time
0877 Auxiliary/immersion 1
0878 Auxiliary/immersion 2
0879 Auxiliary/immersion 3 candidate
087B Defrost count
087C Between last two defrosts
087D Since last defrost
```

**Audit action:** add them with STRONGLY SUPPORTED cross-profile status, never as local causal proof.

## 3.6 `0884`

The semantic register map lacks the now-important page-level finding:

```text
0884/count60
local XTR modern ABI = 8 × 7-word timestamped records + 4-word trailer
```

It is locally proven as rolling timestamped history and very strongly supported as Online/DCM alarm/service history.

Raw event identifiers remain unresolved.

---

# 4. Canonical contradiction: `042E/042F` are not local-XTR unknowns anymore

The current top-level `PROTOCOL_FINDINGS.md` and `THERMIA_PROJECT_STATE.md` still contain wording that lists local `042E/042F` semantic identity among remaining unknowns.

That conflicts with newer/direct local evidence already recorded elsewhere in the same project:

```text
EXP376:
042E = SWW / Hot Water Enabled
042F = SWW / Hot Water Mode

EXP377:
042F active native desired-page write 1 -> 0
exact controller republish
panel semantic effect observed
```

The current semantic map likewise labels both as PROVEN / locally confirmed writable.

### Strong conclusion

The “local XTR `042E/042F` semantic identity remains unknown” wording is stale and should be removed from the current unknowns list.

The **cross-profile conflict at numeric address 042E remains valid**:

```text
ATEC profile: Integral A1
iTec profile: Hot Water Status
local XTR: Hot Water Enabled
```

That is not a contradiction; it is evidence of profile-specific semantics.

---

# 5. Current locally proven writable core after audit

The evidence-backed local XTR writable set is:

## `03E8/count14`

```text
03E8 Heating Curve
03E9 Heating Minimum
03EA Heating Maximum
03EB Curve Correction +5
03EC Curve Correction 0
03ED Curve Correction -5
03EE Heating Stop
03EF Reduced Temperature
03F0 Room Factor
03F4 Room Setpoint
```

Open in this page:

```text
03F1
03F2
03F3
03F5
```

## `042E/count15`

Locally established/proven:

```text
042E Hot Water Enabled
042F Hot Water Mode
0433 Startup HT
0434 Heating Time
```

Candidate only:

```text
0430 Hot Water TOP_UP        STRONGLY SUPPORTED / TEST-only
0431 UNKNOWN
0432 UNKNOWN
```

## `0442/count13`

Locally proven writable:

```text
0442 Cooling Enabled
0443 Desired Cooling Temperature
0445 Cooling Active Above
0449 Cooling Time
044C Cooling Room Sensor
044D Cooling Room Hysteresis Low
044E Cooling Room Hysteresis High
```

Not yet locally promoted:

```text
0444 Cooling Hysteresis             STRONGLY SUPPORTED / TEST-only
0446 Cooling Configuration/Type     STRONGLY SUPPORTED / TEST-only
0447 Cooling START threshold        HYPOTHESIS
0448 Cooling STOP threshold         STRONGLY SUPPORTED / TEST-only
044A Cooling Max Start Temperature  STRONGLY SUPPORTED / TEST-only
044B Cooling Min Stop Temperature   STRONGLY SUPPORTED / TEST-only
```

## `0546/count20`

```text
0553 Operation Mode    PROVEN / locally confirmed writable
0559 Link Integration STRONGLY SUPPORTED / TEST-only
```

The fact that local controlled page machinery can write a page does **not** promote every unknown word on that page.

---

# 6. Historical experiment claims that are now superseded/refined

The audit found a set of recurring interpretation changes that should be treated explicitly as history, not silently erased.

Most important:

```text
0x06 as main Online/DCM application identity
    -> superseded by 0x06 accessory/EXP metadata + 0x0F native application architecture

A80E/AFDC pulse = DCM login
    -> superseded by natural lifecycle/context evidence

strict challenge-specific crypto required for XTR emulation
    -> superseded for the local XTR acceptance path by fixed-R1 replay

03F1 = DHW Start
    -> disproven

042E universally = Integral A1
    -> disproven; profile-specific

W5 6/7 universal normal/join enum
    -> disproven as universal

7FFF/FFFF opaque join signature
    -> decoded as state-upload bitmap

approval accepted = page service ready
    -> refined by PROTO17 into separate states

initial sync = 0708-driven broad refresh
    -> refined by PROTO19:
       32-page autonomous bootstrap first,
       later 26-page mailbox refresh

04A6 ACK directly causes 0708
    -> EXP363 negative

085F ACK alone immediately yields 07D0
    -> context-dependent; no universal rule

0708 mandatory before every runtime page
    -> disproven as universal immediate gate

0872..0878 = contiguous seven operating counters
    -> disproven; sparse layout

0884 raw ID = displayed E-code
    -> disproven

calendar = 99-word functions
    -> disproven; 98-word logical blocks
```

The accompanying supersession CSV records these with evidence references.

---

# 7. PROTO-OFFLINE-17/18/19 impact that is not yet canonical on GitHub

The current offline pass adds three important results which are only local/pending at the moment:

## PROTO-OFFLINE-17 — COMPLETE / POSITIVE

Genuine Eco5 approval and native configuration-service readiness are separate bus-visible gates.

Two early challenge-#3 approvals are accepted near +10 s, but page ACK service begins only near +118.5 s. Across all six successful sessions, first accepted `03E8` ACK occurs in the tight `118.478..120.296 s` window after bus return.

## PROTO-OFFLINE-18 — COMPLETE / NEGATIVE

No independent captured recurrent bus field was found that predicts that readiness transition before the first `03E8` ACK.

## PROTO-OFFLINE-19 — COMPLETE / POSITIVE

Genuine Eco5 has:

```text
32-page controller-autonomous ACK-gated bootstrap
03E8 ... 06F4
```

before the first `0708`.

Later:

```text
W2/W3 = FFFF/867F
```

is a separate 26-page mailbox refresh.

The six pages bootstrap-only in the current Eco5 corpus are:

```text
047E 0492 04D8 04F6 050A 051E
```

These results should be folded into canonical state/findings when GitHub write permission is granted.

---

# 8. Experiment-log integrity findings

The experiment history itself should not be rewritten to make later discoveries appear known earlier.

The following pattern is correct and should be preserved:

- old experiment records retain what was observed and hypothesized at the time;
- current status is added separately as `SUPERSEDED`, `DISPROVEN`, `UPGRADED`, or `REFINED`;
- negative/inconclusive results such as EXP135, EXP335, EXP360–364 remain valuable;
- prepared/not-run experiments must remain clearly distinct from completed experiments.

Specific canonical log gap:

```text
EXP387 and EXP388 are authoritative in PROJECT_STATE + Write Beta v4.1
but absent as entries from EXPERIMENT_LOG.md
```

A future reconciliation should add them without inventing more detail than those sources contain.

---

# 9. Observed facts

- the current semantic register CSV and PROTO16 register DB do not carry identical evidence levels;
- later local experiments upgrade a substantial part of the PROTO16 settings table;
- `0424`, `04A6/04A7`, `06F4` mirror fields, `0870`, sparse runtime counters and `0884` are underrepresented or stale in the current semantic CSV;
- current top-level canonical unknowns still list local `042E/042F` semantics despite direct local mapping/write evidence;
- current `EXPERIMENT_LOG.md` has no EXP387/388 entries although PROJECT_STATE and Write Beta v4.1 explicitly carry their status;
- current canonical experiment log contains 137 unique numeric experiment IDs, not a continuous 1..388 ledger;
- PROTO17/18/19 are completed locally in this pass but have not been written to GitHub.

---

# 10. Strong conclusions

1. The project now needs **database reconciliation**, not another broad register hunt.
2. PROTO16 is a valuable historical/cross-profile snapshot but is not the latest XTR write-confidence layer.
3. The current semantic map is the better settings baseline, but it still misses several durable runtime/structural upgrades.
4. Local `042E/042F` semantics should no longer be listed as open.
5. Experiment history must be preserved, with supersession metadata layered on top rather than rewriting old observations.
6. The canonical experiment log has a real coverage/documentation gap around EXP387/388 and many earlier number ranges; missing entries must not be reconstructed from guesswork.
7. PROTO17–19 materially change the session/sync architecture and should be canonicalized before further offline work is treated as the new durable baseline.

---

# 11. Hypotheses retained

- `0447` is Cooling START threshold.
- `W0` is the high-half desired-state pull bitmap.
- `W1 bit4` would structurally select `0442` if used.
- `W0 bit0` would structurally select `0546` if W0 follows the symmetric page-index model.
- `0879` is the XTR auxiliary-heater stage-3 runtime counter.
- the missing ~120 s service-readiness state is gateway-internal/sideband.

None of these is promoted by this audit.

---

# 12. Important unknowns after audit

The cleaner remaining protocol unknowns are now:

```text
03F1 / 03F2 / 03F3 / 03F5
0431 / 0432
0447 exact semantic/encoding
EXP383 TEST-only fields until individually exercised
0874 / 0875
exact runtime-counter scaling where not reduced
any genuine nonzero W0 behavior
unobserved desired-state selectors
085F per-word semantics / current-alarm bridge
0884 raw-event translation
Connect/DCM03 serializer + protocol packages
calendar active-write atomicity
gateway-internal readiness discriminator
```

These are better targets than re-investigating already settled fields.

---

# Result

**PROTO-OFFLINE-20 — COMPLETE / POSITIVE**

The main deliverable is not a new register hypothesis. It is a safer evidence model:

```text
historical observation
        +
current evidence status
        +
profile provenance
        +
local semantic proof
        +
native write-path proof
```

kept as separate dimensions.

No live experiment status changed and no GitHub files were modified.