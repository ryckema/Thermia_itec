# Thermia iTec XTR M — Native desired-state command reconstruction

**Date:** 2026-10-03  
**Track:** PROTO-OFFLINE-10  
**Status:** COMPLETE / POSITIVE — offline analysis only  
**Baseline:** PROTO-OFFLINE-09 — `0x0708/count6` scheduler/page bitmap reconstruction  
**Controlled change:** analyse only the six already-captured genuine Online/DCM desired-state transactions signalled by non-zero `0708 W1`; compare each FC03 desired image with the most recent controller FC16 image for the same page, the subsequent controller FC16 publication, and independent downstream state where available.  
**Device TX:** none  
**YAML change:** none  
**Heat-pump restart:** none  
**Setting write:** none  
**GitHub change:** none  
**Live experiment state:** unchanged

## Hypothesis

The native Online/DCM command mechanism is a page-level read/modify/return transaction:

1. DCM raises one desired-page bit in `0708 W1`;
2. controller FC03-reads the complete desired page from the DCM;
3. DCM returns a coherent full page image, normally identical to the controller's last published page except for the intended target field;
4. controller accepts/applies the desired image;
5. controller FC16-publishes the resulting page back toward the DCM.

The key safety question is whether the desired FC03 response behaves like a sparse command payload or a complete page snapshot.

**Result:** strongly supported. In all four fully bracketed Eco5 command transactions, the desired image differs from the preceding controller image in exactly one word, and the following controller FC16 page is byte-for-byte identical to the desired image.

---

# 1. Corpus and success criteria

Genuine Online/DCM captures searched:

- `thermia_capture_20260924_210001(1).log`
- `thermia_capture_20260925_071517.log`
- `thermia_capture_20260925_090209.log`
- `thermia_capture_20260925_090550.log`
- `itec_eco5_gateway_20260926.log`
- `itec_eco5_gateway_20260928.log`

The six observed desired-state transactions are:

- 4 × `W1 bit0 -> FC03 03E8`
- 2 × `W1 bit3 -> FC03 042E`

Offline success criteria:

- identify the exact desired-page mutation in at least two independent page groups;
- show a stable relationship between desired FC03 image and controller FC16 result;
- obtain at least one independent semantic/downstream confirmation that the command was actually adopted rather than merely echoed.

All criteria are met.

Negative criteria would have been:

- multiword/random deltas between current and desired images;
- controller result differing unpredictably from the DCM desired response;
- no downstream evidence of semantic adoption where a suitable independent signal exists.

No such negative pattern is present in the clean Eco5 command events.

---

# 2. Older genuine Online/DCM — two `03E8/count13` desired pulls

Two older genuine Online/DCM command events use:

```text
0708:
W1 = 0001
W3 = 0000

controller desired pull:
FC03 03E8/count13
```

## Event O1

```text
0708 response:
0000 0001 0000 0000 077F 0006

desired 03E8/count13:
0017 0014 0028 0000 0001 0001 0012
0012 0002 0028 001E 003C 0014
```

Timing:

```text
0708 response -> FC03 request: ~41 ms
FC03 request  -> desired response: ~39 ms
```

## Event O2

```text
0708 response:
0000 0001 0000 0000 077F 0006

desired 03E8/count13:
0016 0014 0028 0000 0001 0001 0012
0012 0002 0028 001E 003C 0014
```

Timing:

```text
0708 response -> FC03 request: ~39 ms
FC03 request  -> desired response: ~42 ms
```

The two desired images differ in **exactly one word**:

```text
03E8: 0017 -> 0016
```

The project already associates `03E8` with the Heat Curve family, so this is consistent with a single-setting command.

### Limitation

This older capture does not provide a clean immediately preceding and following `03E8` controller FC16 page around both commands, so it cannot independently prove the full read-modify-return loop.

It does, however, independently show the same "complete page with one changed target word" shape later demonstrated much more strongly on Eco5.

---

# 3. Eco5 command E1 — `03F4` room setpoint `20 -> 30`

The previous controller-published `03E8/count14` image is:

```text
0019 0013 0028 0000 0000 0000 0015
0013 0002 0028 001E 0001 0014 0002
```

At the command event:

```text
0708:
W1 = 0001
W3 includes bit0
```

Controller asks:

```text
FC03 03E8/count14
```

DCM returns:

```text
0019 0013 0028 0000 0000 0000 0015
0013 0002 0028 001E 0001 001E 0002
```

Comparison:

```text
all words equal except:

page offset 12
address 03F4
0014 -> 001E
20   -> 30
```

Then, 524 ms after the DCM desired response, the controller publishes:

```text
FC16 03E8/count14
0019 0013 0028 0000 0000 0000 0015
0013 0002 0028 001E 0001 001E 0002
```

This is **byte-for-byte identical** to the desired image returned by the DCM.

## Independent semantic confirmation

The room-sensor/controller path independently changes its confirmed setpoint field:

```text
before command:
B3C5 = 20

after command:
B3C5 = 30
```

Therefore this is not merely a DCM/controller page echo. The desired-state transaction propagates into another controller-visible domain.

### Classification

**PROVEN in genuine Eco5 + Online traffic:**

- `W1 bit0` requests desired page `03E8`;
- the desired response is a full coherent page image;
- only `03F4` changes for this command;
- the controller adopts and republishes that page;
- the semantic effect propagates to the room-setpoint path.

---

# 4. Eco5 command E2 — `03F4` room setpoint `30 -> 20`

The reverse transaction occurs later.

Previous controller-published image:

```text
0019 0013 0028 0000 0000 0000 0015
0013 0002 0028 001E 0001 001E 0002
```

Desired image:

```text
0019 0013 0028 0000 0000 0000 0015
0013 0002 0028 001E 0001 0014 0002
```

Again:

```text
only address 03F4 changes:

001E -> 0014
30   -> 20
```

571 ms after the desired response, the controller FC16-publishes the exact same 14-word image.

Independent room-setpoint propagation also reverses:

```text
before:
B3C5 = 30

after:
B3C5 = 20
```

### Strong result

The pair E1/E2 forms an A/B/A-style reversible semantic write demonstration:

```text
controller current 03F4 = 20
Online desired       = 30
controller result    = 30
B3C5 downstream      = 30

controller current 03F4 = 30
Online desired       = 20
controller result    = 20
B3C5 downstream      = 20
```

This is the strongest existing genuine Online/DCM evidence for a native semantic setting transaction in the project corpus.

---

# 5. Eco5 command E3 — `042E` group, address `042F: 1 -> 0`

Before the command, the most recent controller `042E/count15` image is:

```text
0001 0001 0000 0014 FFF6 0005 0028 0000
002D 0000 0000 0000 0000 0000 0000
```

Scheduler header:

```text
W1 = 0008
W3 = 0008
```

Controller asks:

```text
FC03 042E/count15
```

DCM desired image:

```text
0001 0000 0000 0014 FFF6 0005 0028 0000
002D 0000 0000 0000 0000 0000 0000
```

Only one word changes:

```text
042F:
0001 -> 0000
```

491 ms later, controller FC16-publishes the exact desired 15-word image.

### Semantic caution

`042F` does not yet have a sufficiently supported semantic name in the project corpus.

Do **not** call this word "Integral A1". The public Online mapping supports `042E` / decimal 1070 as Integral A1; this event changes the *next* word, `042F`.

### Classification

**PROVEN structurally / genuine Eco5 + Online:** full-page desired image with one target mutation, exact controller republish.

**OPEN:** semantic meaning of `042F`.

---

# 6. Eco5 command E4 — address `042E: 1 -> 0`

The following command starts from:

```text
0001 0000 0000 0014 FFF6 0005 0028 0000
002D 0000 0000 0000 0000 0000 0000
```

Again:

```text
W1 = 0008
W3 = 0008
```

Desired image:

```text
0000 0000 0000 0014 FFF6 0005 0028 0000
002D 0000 0000 0000 0000 0000 0000
```

Only one word changes:

```text
042E:
0001 -> 0000
```

491 ms later the controller publishes exactly that image.

The public Online register map identifies `042E` / decimal 1070 as **Integral A1**. That gives a semantic candidate for the address, but the captured command intent is not independently labelled in the raw capture. Therefore the safe statement is:

> a genuine Online/DCM command changed native `042E` from 1 to 0 and the controller accepted/republished it; external/public mapping labels `042E` as Integral A1.

Do not infer more specific UI intent than the evidence supports.

---

# 7. Four Eco5 command events — exact invariants

For every fully bracketed Eco5 desired-state command:

```text
N = 4
```

the following are all true:

```text
previous controller page -> desired page:
exactly ONE word changed              4/4

desired FC03 image -> following FC16:
byte-for-byte equality                4/4

W1 target page matches FC03 request   4/4

matching W3 bit causes result publish 4/4
```

Observed confirmation delays:

```text
desired response -> controller FC16 result:
03E8 event 1: 524 ms
03E8 event 2: 571 ms
042E event 1: 491 ms
042E event 2: 491 ms
```

So the semantic transaction is fast and deterministic in the genuine Eco5 corpus.

---

# 8. Full-page image, not sparse command

This analysis answers a central implementation question.

The DCM does **not** return merely:

```text
target address + new value
```

after the controller asks for the selected desired page.

Instead the DCM returns the **complete requested page image**.

In all clean cases, the image appears to be constructed as:

```text
last known/current page
        +
one intentional target-word mutation
        =
desired page returned by FC03
```

The controller then republishes the resulting complete page by FC16.

### Strong implementation implication

A future emulator should maintain a coherent **page cache**.

Conceptually:

```text
capture controller FC16 current image
        ↓
copy entire page
        ↓
change exactly one known target word
        ↓
on genuine controller FC03 desired-page request:
return complete mutated page
        ↓
wait for controller FC16 confirmation
        ↓
compare complete result
```

This is much safer and more faithful than synthesizing a page from guessed defaults.

### Important limitation

The captures prove that the whole page is transmitted. They do **not** prove that the controller independently applies every unchanged context word as a setting on each command.

Therefore the precise statement is:

- complete coherent page image is required by the observed protocol;
- stale or invented context is unsafe;
- only the deliberately changed target word should be varied in a controlled future experiment.

---

# 9. Page length is profile/topology dependent

The older genuine DCM command reads:

```text
03E8/count13
```

while the Eco5 Online command reads:

```text
03E8/count14
```

The local XTR session/sync work also has its own observed page shapes.

Therefore a future emulator must **never hard-code an external model's desired-page count as a universal constant**.

The response should be shaped from:

```text
the controller's actual FC03 request
+
the locally established page image for that controller/profile
```

This is another reason a page cache is required.

---

# 10. Native command transaction model after PROTO-OFFLINE-10

The best-supported state machine is now:

```text
DCM has desired setting change
        |
        v
next controller FC03 0708/count6 poll
        |
        v
DCM sets exactly the desired-page bit in W1
(and normally corresponding result/upload bit in W3)
        |
        v
controller FC03-reads selected desired page
        |
        v
DCM returns COMPLETE coherent page image
with only intended word changed
        |
        v
controller accepts/applies page
        |
        v
controller FC16-publishes resulting page
        |
        +--> DCM compares full page with desired image
        |
        +--> independent controller domains may update
             e.g. B3C5 room setpoint
```

This is a page-level **read-modify-return / pull-apply-confirm** protocol.

---

# 11. What is now proven versus still unknown

## Observed facts

- six genuine desired-state transactions exist in the corpus;
- four target `03E8`, two target `042E`;
- older two `03E8/count13` desired snapshots differ only at `03E8`;
- all four fully bracketed Eco5 commands differ from the previous controller page in exactly one word;
- all four Eco5 controller result pages are exactly equal to the DCM desired page;
- `03F4` changes `20 -> 30 -> 20` in the two Eco5 `03E8` commands;
- room path `B3C5` independently follows `20 -> 30 -> 20`;
- `042F` changes `1 -> 0` in one command;
- `042E` changes `1 -> 0` in the next;
- Eco5 desired-response to FC16-confirmation latency is ~0.49–0.57 s.

## Strong conclusions

1. Native Online semantic control is **controller-pulled**, not an unsolicited settings FC16 injection.
2. The DCM returns a **full desired page image**.
3. In all clean captured commands, one semantic target word is mutated while the rest of the page is preserved.
4. The controller's following FC16 publication acts as a strong result/confirmation image.
5. `03F4` is not just an exported mirror in these captures: changing it through the native desired-state path produces an independent setpoint change in the room-sensor/controller path.
6. Safe emulation should be based on current-page caching + single-word mutation + exact result comparison.

## Hypotheses

- The controller may validate unchanged context fields in the desired page; no field-level validation behavior is directly exposed.
- Matching W3 bit may function as explicit "publish result/current page" request in addition to normal dirty-state semantics.
- The same full-page read-modify-return model likely applies to other W1 page bits, but only bits0 and3 are actually observed.

## Unknowns

- meanings of unobserved W1 bits;
- any W0 desired-state bits;
- semantic identity of `042F`;
- exact application/validation rules for unchanged page words;
- rejection behavior if desired page contains stale context;
- whether controller may clamp/rewrite a requested target before FC16 confirmation;
- local XTR behavior for a live semantic desired-page request has not been tested by this offline track.

---

# 12. Safety consequence for any future live semantic experiment

PROTO-OFFLINE-10 does **not** itself authorize a write.

A future active semantic experiment should:

1. start only from an established native DCM runtime/session;
2. wait for a genuine controller `0708` poll;
3. use only a proven W1 bit;
4. use the exact controller-requested page/count;
5. build the desired response by copying the latest local controller FC16 image;
6. mutate exactly one locally proven, low-risk target word;
7. accept no unrelated/stale context changes;
8. require a matching controller FC16 confirmation image;
9. abort on any unexpected request, page/count change, missing confirmation, or other semantic traffic;
10. have a deterministic reverse command using the previously captured original value.

That experiment should be defined separately and must not be inferred as complete from this offline analysis.

---

# Result

**PROTO-OFFLINE-10 — COMPLETE / POSITIVE**

The strongest result is not merely that Online can request pages through `0708`.

The genuine captures now show the full semantic write primitive:

```text
CURRENT FULL PAGE
      ↓ copy
ONE WORD MUTATED
      ↓
DCM DESIRED FULL PAGE
      ↓ FC03 response
CONTROLLER ADOPTS
      ↓
FC16 RESULT = DESIRED PAGE
```

For `03F4`, adoption is independently confirmed outside the 0x0F page itself by the room setpoint path.

This provides the clearest evidence so far for how a future safe DCM emulator should construct a native write transaction.