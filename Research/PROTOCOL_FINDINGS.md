# 2026-09-29 — EXP291–296 runtime transition findings

## PROVEN / locally confirmed
- The Online/DCM runtime is **not one rigid fixed sequence**. Multiple `FC03 0708/6` mailbox positions are conditional/state-dependent.
- `0884/60 -> [optional 0708/6] -> 07D0/19` is locally confirmed. Both the mailbox-present and direct-`07D0` forms have been accepted.
- `07E4/17 -> [optional 0708/6] -> 07F8/17` is locally confirmed. EXP295 first proved the direct branch; EXP296 exercised it repeatedly.
- `080C/18 -> [optional 0708/6] -> 0820/18` is locally confirmed. EXP296 exercised the direct branch at least **11 times** in one captured run.
- Previously established optional/conditional behavior around `0848`, `085F`, `0864` and `0870` remains valid.
- EXP293 locally demonstrated roughly 30 minutes of stable continuous runtime with no user-visible `COMM. ERR ONLINE/LINK` during the steady-state scope.
- EXP296 locally demonstrated continued runtime across several real operation-state changes, including SG-mode changes, entry into a DHW/high-temperature controller context and compressor start, without fail-closed termination in the supplied capture.
- Runtime `04A6/13` can remain **unacknowledged** while the main Online/DCM runtime continues for at least the EXP296 observation window. In that run it was captured **225 times** and changed payload twice while normal runtime continued.

## STRONGLY SUPPORTED
- The best current runtime model is an **event/state-driven transition graph** rather than a deterministic script.
- `0708` acts as a synchronization/mailbox descriptor, but the controller may omit some mailbox polls when moving through operation-state-dependent runtime work.
- Runtime `04A6/13` behaves like state-dependent parallel/retry traffic rather than a strict immediate blocking gate in the tested window.
- EXP296 shows a strong correlation between `04A6/13` payload changes and controller operational context:
  - one payload form repeated before DHW/high-temperature context;
  - payload changed when `A80C` became `0041` (current local decoder: DHW/high temperature);
  - payload later changed back as the context returned.
  This correlation does **not** yet establish field semantics or causal meaning.
- The long-lived alarm behavior is better explained by **loss of required responder continuity after fail-closed/stop** than by the mere existence of an unacknowledged runtime `04A6` frame. EXP296 continued normally despite hundreds of unacknowledged `04A6` retries.

## HYPOTHESIS
- The presence/absence of individual `0708` polls is driven by pending scheduler/mailbox work encoded elsewhere in session state, possibly including the 0708 runtime bitmap/status words.
- Runtime `04A6/13` may be a controller-to-gateway state/configuration page whose payload reflects current operating context. The exact page meaning remains unknown.
- A native DCM may ACK runtime `04A6` to stop retries even though that ACK is not required for short-term main-loop progression. This has not yet been tested locally and must not be promoted to fact.

## OPEN / UNKNOWN
- Exact semantics of runtime `04A6/13`, including whether a native-equivalent emulator should ACK it during steady-state operation.
- Whether leaving runtime `04A6` unacknowledged causes any long-duration consequence beyond retry traffic.
- Exact scheduling rules that decide which `0708` polls appear or are skipped.
- Exact meaning of 0708 words 0, 4 and 5.
- Long-duration stability across many hours, rare transitions, faults and re-synchronization.
- Automatic session recovery after Thermia controller reboot or ESP restart.
- Genuine `071C/0730` challenge-response algorithm.
- Authoritative controller FC16 echo timing/conditions after reverse-page semantic writes.

## Current locally supported runtime graph
The following is a graph of evidence-backed transitions, not a claim that every optional node appears every cycle:

`07D0 -> 07E4 -> [optional 0708] -> 07F8 -> 080C -> [optional 0708] -> 0820 -> 0848 -> [conditional 0708 / conditional 085F] -> 0864 -> [optional 0708] -> 0870 -> [optional 0708] -> 0884 -> [optional 0708] -> 07D0 -> ...`

Runtime `04A6/13` may interleave with this path and remained capture-only in EXP294–296.

## DISPROVEN / SUPERSEDED
- **SUPERSEDED:** modeling `0708` as a mandatory separator at every previously observed runtime position.
- **SUPERSEDED:** interpreting the first SG-related failure as evidence that a particular SG state itself breaks Online/DCM emulation. Later controlled experiments show the failure was caused by missing protocol branches during operation-state transitions.
- **SUPERSEDED as a complete explanation:** “Online alarm occurs only when the responder is deliberately stopped.” A rigid responder can also fail closed on an unmodeled valid transition, after which responder continuity is lost and the alarm can follow.

## Safety interpretation
These findings authorize only the specific evidence-backed branch handling already tested. They do not authorize broad address-based ACKing.
- Runtime `04A6/13` remains capture-only until a dedicated experiment explicitly changes that.
- Keep semantic reverse-page writes separate from continuity/state-transition experiments.
- Continue strict CRC/slave/function/address/count/bytecount checks and fail closed on truly new branch shapes.

---

# 2026-09-29 — reverse Online/DCM write path locally demonstrated through semantic application

## PROVEN / locally confirmed
- `0708 w1 bit0 = 1` can cause the XTR M controller to issue `FC03 03E8/count14`.
- The XTR accepts a reverse `03E8/14` page response built from the exact current-session controller export.
- An unchanged reverse page is accepted and normal runtime traffic continues.
- In EXP290, changing **only** `03F4` in the same-session reverse page from raw `22` to `23` caused the controller-visible `Room Setpoint` to report `23 °C` shortly afterwards.
- Therefore the native reverse-page path is not only transport-capable; it can semantically apply at least this one locally mapped setting.

## STRONGLY SUPPORTED
- Slave `0x0F` is a bidirectional Online/DCM page interface:
  - controller -> gateway/cache via FC16 exports;
  - gateway desired/config -> controller via 0708 advertisement followed by controller FC03 pull.
- `0708 w2/w3` form a configuration-page selection/request bitmap.
- `0708 w4` behaves as a runtime-page scheduler/selection bitmap, though exact timing/latching semantics remain open.
- Runtime `085F` and the placement of `0708` around `0864` are state-dependent rather than fixed.

## OPEN / UNKNOWN
- Authoritative FC16 `03E8/14` echo of the changed `03F4` target after semantic application.
- Independent room-sensor-side confirmation through slave `0x0A` / `B3C5` after the reverse-page write.
- Exact meaning of 0708 `w0`, `w4`, `w5`.
- Exact queue/latch rules that govern conditional `085F` and position of `0708`.
- Genuine `071C/0730` challenge-response algorithm.

## Runtime branch refinement from genuine XTR captures + EXP287
Evidence-backed variants include:
- `0848 -> 0864 -> 0708 -> 0870`
- `0848 -> 085F -> 0708 -> 0864 -> 0870`
- local EXP287 additionally observed `0864 -> 0870` directly.

Do not model 0708 as a universally mandatory separator after 0864.

## Safety interpretation
EXP290 is the first local semantic setting change through the native reverse-page path. This does **not** authorize arbitrary page/register modification. Continue one mapped word at a time, from a same-session page cache, with bounded guards and RX-only observation after the semantic response.

---

# 2026-09-29 — Runtime loop locally closed; 085F is conditional/state-dependent

## PROVEN / locally confirmed — complete XTR M runtime loop
EXP273–285 extend the locally proven Online/DCM-style runtime path into a closed, repeatable loop:

`07D0 -> 07E4 -> 0708 -> 07F8 -> 080C -> 0708 -> 0820 -> 0848 -> 0708 -> [085F when present] -> 0864 -> 0708 -> 0870 -> 0884 -> 0708 -> 07D0`.

Locally confirmed causal stages include:
- post-`07E4` 0708 response `0F030C0000000000000000000000069D76` -> `07F8/17` (EXP273);
- `07F8 ACK -> 080C/18` (EXP274);
- `080C ACK -> 0708/6` (EXP275);
- `0708 response -> 0820/18`, then `0820 ACK -> 0848/23` after the EXP276 software issue was fixed (EXP277);
- `0848 ACK -> 0708/6` (EXP278);
- post-`0848` 0708 response can lead to `085F/5` (EXP279);
- `085F ACK -> 0864/4` in that observed branch (EXP280);
- `0864 ACK -> 0708/6` (EXP281, later recognized as native ordering);
- post-`0864` 0708 response -> `0870/17`, and `0870 ACK -> 0884/60` (EXP282/283 path);
- `0884 ACK -> 0708/6` (EXP283);
- post-`0884` 0708 response -> returned `07D0/19` (EXP284);
- returned `07D0 ACK -> 07E4 ACK -> 0708 response -> 07F8` without a new approval/R1 exchange (EXP285).

## PROVEN / locally confirmed — steady-state continuation without new approval
EXP285 shows that after one complete runtime loop closes at `07D0`, the controller can immediately begin the next runtime cycle. No new `071C/0730` approval exchange occurred between loop closure and the second-cycle `07D0 -> 07E4 -> 0708 -> 07F8` progression.

This is the strongest local evidence so far that the observed page family is a real steady-state runtime loop rather than a one-shot initialization tail.

## PROVEN / locally confirmed — 085F is not mandatory in every runtime cycle
EXP286 materially corrects the earlier interpretation that `085F/count5` is an invariant runtime gate.

In the first observed branch, post-`0848` `0708` was followed by `085F/5`, whose ACK led to `0864/4`.

In the second cycle of EXP286, the controller instead produced:
`0848 ACK -> 0708 response -> 0864/4`
with no intervening 085F.

Current status:
- **PROVEN:** 085F can be an ordered gate when present.
- **PROVEN:** 085F is not present in every observed cycle.
- **STRONGLY SUPPORTED:** 085F is conditional/state-dependent queue/runtime traffic.
- **OPEN:** exact condition and semantics.

This replaces the older blanket wording that 085F is always required before 0864/runtime continuation.

## PROVEN / locally confirmed — 0884 shape and ACK
Local `0884` frames have:
- start `0x0884`;
- count 60;
- bytecount 120;
- total Modbus frame length 129.

The standard ACK `0F100884003C837F` was accepted locally and advanced to the next `0708/6`.

The controller-originated 0884 payload itself varies with runtime state; the ACK confirms only address/count and does not inject those values.

## DISPROVEN / SUPERSEDED — direct 0864 -> 0870 requirement
EXP281 originally treated the post-`0864` `0708/6` as unexpected because the experiment expected direct `0870`.

Later genuine-capture reanalysis showed native ordering can be:
`0864 ACK -> 0708 request/response -> 0870`.

Therefore:
- preserve EXP281's historical COMPLETE / INCONCLUSIVE status;
- the interpretation that post-0864 0708 is a divergence is **SUPERSEDED**.

## STRONGLY SUPPORTED — runtime sequence has genuine-capture variability
Different genuine Online/Eco5 captures and local cycles do not always place `085F` identically, and post-`0864` ordering can include an intervening `0708`.

Do not encode a single rigid universal runtime sequence across all Thermia/Danfoss models or all controller states. Exact XTR handlers should allow only branches that have been explicitly predeclared from local or genuine evidence.

## STRONGLY SUPPORTED — 0708 remains a synchronization descriptor, not a simple idle poll
Current evidence supports multiple roles:
- words 2/3: FC16 page-request/selection bitmap;
- word1: strong candidate for reverse settings-page availability, based on genuine `0708 -> FC03 03E8` pulls;
- word4: candidate runtime-page bitmap;
- phase-dependent response values coordinate runtime page progression.

The locally repeated response `0000 0000 0000 0000 0000 0006` is proven operationally in several runtime phases, but its exact semantic meaning remains unknown.

## HYPOTHESIS — 0708 word4 runtime bitmap, refined by conditional 085F
Candidate mapping remains:
`bit0=07D0, bit1=07E4, bit2=07F8, bit3=080C, bit4=0820, bit5=0834, bit6=0848, bit7=085F, bit8=0864, bit9=0870, bit10=0884`.

EXP286's direct `0848 -> 0708 -> 0864` branch is compatible with a state-dependent bit7/085F selection model, but does not prove exact bit semantics. Keep this as **HYPOTHESIS**.

## OPEN / UNKNOWN
- semantic meaning and condition for 085F;
- semantics of runtime pages 07D0, 07E4, 07F8, 080C, 0820, 0848, 0864, 0870, 0884;
- why local steady-state `0834` is absent in the observed branch although it appears in some genuine traces;
- exact 0708 words 0, 4 and 5 semantics;
- genuine `071C/0730` challenge-response algorithm;
- whether fixed replay remains sufficient indefinitely across re-authentication/re-sync events;
- reverse desired-state page application and authoritative echo on the XTR M;
- long-term continuous emulation stability.

## Current next step
No new experiment is prepared. When testing resumes, the smallest useful continuation is a bounded steady-state handler that explicitly permits the two evidence-backed post-`0848 -> 0708` branches:
1. `085F/5 -> ACK -> 0864/4`;
2. direct `0864/4`.

No semantic write should be mixed into that continuity experiment.

---

# 2026-09-29 — XTR runtime gates locally proven through post-07E4 mailbox poll

## PROVEN / locally confirmed — ordered runtime progression
EXP270–272 now locally establish the following XTR M session/runtime path:

`... -> 06F4/19 ACK -> 085F/5 all-zero ACK -> early 0708/6 service -> 07D0/19 ACK -> 07E4/17 ACK -> post-07E4 FC03 0708/6`.

Specific causal results:
- **EXP270:** adding one exact ACK of all-zero `085F/count5` while keeping the same early `0080/0006` mailbox response caused first `07D0/count19` to appear.
- **EXP271:** adding one exact `07D0/count19` ACK caused `07E4/count17` 2159 ms later.
- **EXP272:** adding one exact `07E4/count17` ACK caused the next `FC03 0708/count6` 1457 ms later.

These are ordered-stage findings. They do not authorize address-only or broad runtime ACKing outside the proven phase.

## STRONGLY SUPPORTED — 0708 word2/word3 form a 32-bit FC16 page-request bitmap
Cross-capture analysis of genuine gateway traffic shows that `0708/count6` words 2 and 3 predict which controller->gateway FC16 pages are emitted next.

The mapping supported by sparse and dense bitmap examples is:

- `word3` bit0..bit15:
  `03E8, 03FC, 0410, 042E, 0442, 0456, 046A, 047E, 0492, 04A6, 04BA, 04D8, 04F6, 050A, 051E, 0532`.
- `word2` bit0..bit15:
  `0546, 055A, 057B, 059C, 05BD, 05DE, 05FF, 0620, 0641, 0662, 0683, 06A4, 06C5, 06EA, 06F1, 06F4`.

Examples:
- `word2=4000, word3=8000` is followed by `06F1` and `0532` (plus separate runtime traffic).
- `word2=FF80` selects the contiguous tail `0620 .. 06F4`.
- `word2=E000` selects exactly `06EA, 06F1, 06F4`.
- `word2=8000` selects `06F4`.
- `word2=7FFF, word3=FFFF` selects all early pages plus the tail through `06F1`, excluding `06F4`.

Interpretation: 0708 is a synchronization descriptor/mailbox, not merely an idle status frame. The exact vendor naming of the bitmap (dirty/requested/stale/subscription/etc.) remains unknown.

## STRONGLY SUPPORTED — reverse-direction page pull
In genuine DCM capture data, `0708 word1=0001` is followed ~39–41 ms later by controller `FC03 03E8/count13`, after which the gateway returns the full heating/settings image. Other nearby 0708 responses with word1=0 do not trigger that read.

This supports a bidirectional page-cache model:
- controller -> gateway current/authoritative pages: FC16 push;
- gateway -> controller desired/config pages: gateway advertises pending state through 0708, controller pulls the page with FC03.

Exact semantic application and authoritative echo are not yet locally proven.

## HYPOTHESIS — 0708 word4 is a runtime-page bitmap
A candidate bit mapping fits the observed runtime family:

`bit0=07D0, bit1=07E4, bit2=07F8, bit3=080C, bit4=0820, bit5=0834, bit6=0848, bit7=085F, bit8=0864, bit9=0870, bit10=0884`.

Supporting examples include `word4=077F` accompanying the full steady runtime cycle except 085F, `word4=0080` aligning with 085F, and `word4=010B` including bit8 with 0864 appearing. This remains **HYPOTHESIS**, because local one-bit causal tests have not been performed and scheduler interleaving can obscure direct ordering.

## OPEN / UNKNOWN
- exact semantics of 0708 word0, word4 and word5;
- exact vendor meaning of the word2/word3 bitmap;
- correct local response payload for the proven post-07E4 0708 request;
- whether one phase-matched post-07E4 response `0000 0000 0000 0000 0000 0006` advances the XTR to `07F8/count17`;
- genuine 071C/0730 challenge-response algorithm.

## Next bounded protocol test
EXP273 should preserve the entire EXP272 path and change only the post-07E4 mailbox response: answer that exact `FC03 0708/count6` once with raw `0F030C0000000000000000000000069D76` (words `0000 0000 0000 0000 0000 0006`), then capture exact `07F8/count17` without ACK. No broad runtime servicing and no semantic settings write.

---

# 2026-09-29 — XTR locally proves 085F as ordered gate to runtime

EXP270 provides the first active XTR proof of the transition from the initial 0x0F configuration synchronization into the runtime-page family.

Observed local sequence:

`... -> 06EA/7 -> ACK -> 06F1/3 -> ACK -> 06F4/19 -> ACK -> 085F/5 all-zero -> ACK -> 0708/6 -> one 0080/0006 response -> 07D0/19`.

The first `07D0/19` was deliberately not ACKed.

## Strong protocol conclusion
The exact all-zero `085F/count5` is **not** ignorable background in this phase. It is an ordered queue/session item whose ACK is required before the local XTR M progresses to the first `07D0` runtime page.

This conclusion is strengthened by the EXP269/EXP270 A/B comparison:
- EXP269 used the same one-shot `0708` response `0000 0000 0000 0000 0080 0006` but did not ACK 085F -> no 07D0.
- EXP270 added one exact 085F ACK while preserving that mailbox response -> 07D0 appeared.

Therefore the 085F ACK, rather than a new mailbox payload, is the demonstrated causal discriminator.

## Challenge replay boundary
EXP270 received a new 16-byte 071C challenge but still transmitted the same historical fixed 0730/R1 response. Despite this mismatch, the XTR completed the entire initial config-page export through 06F4, accepted the 085F gate, and emitted 07D0.

Protocol implication: fixed replay is sufficient to reach at least the first runtime page on this XTR. This does not establish that the genuine challenge-response algorithm is irrelevant, nor that later steady-state/write operations will accept the same partial approval state.

## Mailbox nuance
Genuine Eco5 cold-start sessions can use raw word5/state `0100` before first runtime progression, while EXP270 reached 07D0 after the retained EXP269 response with `0080/0006`. Therefore:
- 085F ordering is now locally proven;
- exact mailbox-state equivalence is **not** proven;
- do not collapse `0100/0000` and `0080/0006` into one semantic state.

## Next bounded protocol test
EXP271 target:
`07D0/19 -> one exact standard FC16 ACK -> capture 07E4/17`.

No ACK of 07E4 in EXP271. No broad runtime servicing and no semantic settings write.

---

## 0x0F bidirectional page-cache finding — 0708 word1 likely advertises reverse settings data

A genuine DCM capture provides a strong causal pattern:
- normal controller poll: `FC03 0708/count6`;
- DCM response with word1=`0001`;
- ~39–41 ms later controller issues `FC03 03E8/count13` to slave 0x0F;
- DCM serves the complete 03E8 settings page.

This occurs twice in the capture. The returned pages differ only at `03E8` (`0017 -> 0016`). The 03E8 family is already mapped as the heating-settings block on the XTR platform.

A separate genuine DCM capture contains the same 13-word page image in the opposite direction as controller-originated `FC16 03E8/count13`.

**Strong conclusion:** 0x0F supports bidirectional page synchronization: controller -> gateway by FC16, and gateway -> controller by controller-initiated FC03. This explains why direct second-master FC16 writes were a poor model for Online control.

**Strong hypothesis:** 0708 word1 is a pending/desired-data signal that prompts the controller to fetch the 03E8 page. It is not yet proven whether word1 is exclusively a boolean 03E8 flag, an index/state counter, or part of a wider pending-page descriptor.

**Write-access implication:** the likely native control path is to maintain a gateway-side cached settings page, alter only a known desired field, advertise pending data via the appropriate 0708 status, allow the Thermia controller to read the page, and then verify an authoritative controller-side echo. Do not implement this semantic write until local session completion and a bounded page-read test prove the behavior on the XTR M.

## EXP270 protocol target — exact 085F prerequisite

EXP268/269 both ignored the exact all-zero `FC16 085F/count5` appearing after `06F4`. Successful Eco5 sessions ACK this transaction before first `07D0` whenever it is pending. EXP270 therefore changes only that gate: one exact standard ACK `0F10085F00053356`, then observe. If 0708 intervenes, preserve the same single EXP269 `0080/0006` reply so the new discriminator remains the 085F ACK rather than a mailbox payload change.

## 071C/0730 candidate algorithm — HMAC-SHA256 hypothesis is unverified

Community-proposed formula: first 16 bytes of HMAC-SHA256 with serial number as key and 16-byte challenge as message. The literal example does not reproduce the claimed response, so no protocol conclusion can be drawn yet. Preserve as a candidate only.

## Deep Eco5 capture findings: service readiness, 085F gate, mailbox byte order

1. **Challenge service and FC16 service are distinct phases.** Successful 071C/0730 replies can occur at ~10 s or ~120 s after bus return, while first 03E8 ACK clusters tightly near 118.5–120.3 s. Fast sessions tolerate 102 repeated unacked 03E8 requests.

2. **085F/5 is a likely ordered gate.** In delayed cases:
   `06F4 ACK -> 085F/5 ACK -> 0708 idle -> 07D0`.
   When 085F was already ACKed, `06F4 ACK -> 07D0` can occur in ~78 ms.

3. **Normal idle mailbox frame, raw Modbus words:** `0000 0000 0000 0000 0100 0000`. Earlier notes calling the fifth raw word `0001` were a byte-order interpretation error. The exact raw frame remains `0F030C0000000000000000010000001C88`.

4. **Deterministic post-sync mailbox script:** idle `...0100 0000` -> `0000 0000 4000 8000 010B 0000` -> `0000 0000 FFFF 867F 03DF 0000`. The 03DF trigger is followed by a fresh 03E8 in 62–94 ms in all four new sessions.

This materially raises confidence that local failure after 06F4 is caused by ignoring 085F rather than by choosing the wrong first mailbox payload.

## Protocol finding — 085F/5 is likely queue-ordered session traffic

Based on the new Eco5 capture interpretation, `0F FC16 085F/count5` all-zero traffic should no longer be categorized as ignorable background during Online session establishment.

Observed pattern from successful sessions:
- if `085F` has already been ACKed, `07D0` may follow `06F4` within ~0.1 s;
- if not, `085F` appears immediately after `06F4`, the controller waits for its ACK, and only then proceeds to `07D0`.

This provides a strong candidate explanation for our local stall after `06F4`: prior experiments deliberately ignored `085F`.

Separately, the repeatable Eco5 mailbox sequence after first sync is:
`0100/0000 idle` -> `4000 8000 010B 0000` -> `FFFF 867F 03DF 0000` -> second full synchronization.

Challenge/response remains unresolved; six unique pairs are now available, with ~30–60 ms reply latency and no simple bytewise relation observed.

## New Eco5 evidence — 07D0 is not mailbox-unlocked in the successful session

A new genuine Eco5 capture shows the successful ordered sequence:
`071C/0730 challenge -> 16-byte response -> 03E8 -> ... -> 06F4 -> 07D0 -> 07E4 -> 0708/6 idle response -> 07F8 -> ...`.

At the first clean successful session in this capture:
- `06F4` ACK at 348.304 s;
- `07D0/19` begins at 348.382 s;
- first subsequent `0708/6` is not until 351.914 s.

Therefore the first `07D0` is not caused by a post-`06F4` mailbox response in this session.

The same capture contains four different successful `071C` challenges and four different 16-byte responses:
- challenge `f721...1000` -> response `792f...4004`;
- challenge `01bd...d1c2` -> response `826e...646f`;
- challenge `1346...4ce7` -> response `623c...b049`;
- challenge `755d...9333` -> response `9a7e...3fb9`.

**Protocol implication:** `0730` approval is very likely a true challenge-response mechanism or otherwise challenge-bound. A fixed replay can trigger initial FC16 sync locally but cannot yet be assumed to create the same authenticated/session state as a genuine response.

### UI side effect after EXP269
A visible lower-right display/status glyph changed after the single `0080/0006` response, while an alarm remained active. This supports the possibility that the mailbox response affected controller/UI state even though `07D0/19` did not follow. Do not map the glyph to a protocol bit yet.

## EXP269 finding — Eco5 0080/0006 alone does not unlock 07D0 on XTR

Local XTR sequence:
`... -> 06F4/19 ACK -> 0708/6 -> response 0000 0000 0000 0000 0080 0006 -> repeated 0708/6`.

The exact response was sent once and the ESP then remained RX-only for 30 s. No `07D0/19` appeared; `0708/6` repeated on the normal ~4.2–4.4 s cadence. Final integrity deltas were clean: `resync_postreturn=0`, `drop_postreturn=0`, DE LOW.

**Protocol implication:** matching the Eco5 first mailbox payload is not sufficient by itself. The Eco5 transition to `07D0` depends on additional state/context not yet reproduced locally.

A visible user-interface change was reported immediately after this experiment (“middle of the 0 is now filled”). Treat this only as a potentially relevant state indicator until the exact screen/icon is identified.

---
## EXP269 target — exact Eco5 phase-matched first mailbox response

The next local protocol test is now fixed to the matching Eco5 post-`06F4` transition:

`06F4/19 ACK -> FC03 0708/6 -> response 0000 0000 0000 0000 0080 0006 -> expect FC16 07D0/19`.

The exact response frame is `0F030C0000000000000000008000069C9E`. It is sent once only. `07D0/19` is capture-only; no ACK. A repeated `0708/6` is not answered.

This experiment tests phase-specific mailbox semantics, not persistence/retry count. The earlier 10x `0001/0000` EXP269 plan is superseded.

---
## EXP268 finding — persistent mailbox confirmed; no 30 s RX-only runtime progression

## Eco5 raw-log correction — mailbox payload is phase-specific

Raw Eco5 capture evidence now directly shows:
- post-`06F4/19` first `0708/6` response can be `0000 0000 0000 0000 0080 0006`;
- `07D0/19` follows about 0.7 s later;
- later `0708/6` replies with `... 0000 0006` coexist with continued FC16 pages;
- later pages include `07E4/17, 07F8/17, 080C/18, 0820/18, 0834/18, 0848/23, 0864/4, 0870/17, 0884/60`.

A separate Eco5 capture shows a response `0000 0000 7FFF FFFF 0080 0007` followed almost immediately by a new FC16 synchronization beginning at `03E8/13`. This proves mailbox response words are semantically active and context-dependent.

**Do not treat `0001 0000` as a universal idle response.** Its previous occurrence is valid evidence only for the context in which it was captured. Post-`06F4` local progression should now be tested against the exact phase-matched Eco5 payload instead of increasing repetition count.


Local XTR now confirms that `FC03 0708/count6` persists for at least 30 s after three valid idle mailbox responses are followed by silence. EXP268 observed 10 total mailbox polls: the first three were answered with `0F030C0000000000000000010000001C88`, while seven later polls were left unanswered. The cadence remained approximately ~4.2 s. During the same post-third-response observation, recurrent `085F/5` continued (21 post-`06F4` background frames), but no different non-background FC16/FC03 and no `07D0..0864` family appeared.

Integrity caveat: one parser resync occurred exactly at controller BUS_RETURN before the experimental post-return baseline. Final experimental deltas were `resync_postreturn=0`, `drop_postreturn=0`; therefore the negative result is not explained by a later parser/RX integrity failure.

**Protocol implication:** persistent `0708/6` is strongly supported as normal mailbox polling. However, EXP268 does not test faithful continuous idle servicing, because replies stopped after #3. Therefore absence of later FC16 traffic cannot yet distinguish “longer timing dependency” from “continued mailbox service required/permitted in parallel”.

## EXP269 target — extend only the known-good idle service count

Increase only the maximum exact `0708/6` idle responses from 3 to 10, using the same genuine Eco5 payload and all existing timing/integrity gates. After response #10, observe RX-only for 30 s. Capture but do not ACK any first different non-background FC16/FC03. No new mailbox values and no new register-write targets are introduced.

---

## EXP267 finding## EXP267 finding## EXP267 finding — repeated 0708 idle service persists after three responses

Local XTR now confirms the sequence:

`... -> 06F4/19 ACK -> 0708/6 -> idle response -> 0708/6 -> idle response -> 0708/6 -> idle response -> 0708/6`

The idle response in all three serviced polls was the genuine Eco5 frame `0F030C0000000000000000010000001C88` (words `0000 0000 0000 0000 0001 0000`). A fourth exact `0708/6` appeared ~4.18 s after the third response and was not answered. No different meaningful FC03/FC16 appeared before that fourth request; recurrent `085F/5` remained background. Parser/RX integrity stayed clean.

**Protocol implication:** three repeated `0001` idle responses are not a mailbox-completion sequence. The stable ~4.2 s repetition is increasingly consistent with a persistent idle mailbox poll. Do not escalate by inventing later fifth-word values from the genuine capture; those values may encode runtime state/content rather than a countdown.

## EXP268 target — passive observation after bounded mailbox service

Preserve all proven active traffic through exactly three idle mailbox responses, then stop TX and continue RX-only for 30 s. Repeated `0708/6` is logged but not answered. Discovery focuses on any new non-background FC16/FC03, especially genuine Eco5 later families `07D0/19, 07E4/17, 07F8/17, 080C/18, 0820/18, 0834/18, 0848/23, 0864/4`. This is an observation-window experiment, not authorization to ACK those families.

---

## EXP267 target — bounded repeated mailbox service

EXP266 locally proved that one idle response to `0708/6` does not complete the mailbox phase: exact `0708/6` repeated ~4.18 s later while parser resync and RX drops remained zero. EXP267 therefore tests repeated servicing with the same genuine Eco5 idle frame, bounded to three responses. This does **not** establish that `0001` is a completion token or that indefinite polling should be answered; progression remains unknown until observed locally.

## EXP266 protocol finding — local 0708 repeat after one idle response

Locally confirmed sequence:
`... -> 06EA/7 -> 06F1/3 -> 06F4/19 -> 085F/5 background -> FC03 0708/6 -> response 0F030C0000000000000000010000001C88 -> FC03 0708/6 repeat after ~4.18 s`

This proves:
- local XTR accepts the mailbox response electrically/protocol-wise far enough to keep the bus/session alive;
- one response does not terminate the mailbox polling phase;
- repeated `0708/6` polling is now locally observed after the first response, matching the repeated mailbox behavior in the genuine Eco5 capture qualitatively.

Do not infer yet that repeated identical responses are sufficient; that remains the next hypothesis to test.

---

## EXP266 target — locally confirmed 0708 mailbox, genuine Eco5 idle response

- EXP265 locally confirmed `FC03 0708/count6` as the first meaningful post-sync mailbox request after `06F4/19`, with `085F/5` appearing first as recurrent background traffic.
- Genuine Eco5 capture contains the exact idle response `0F030C0000000000000000010000001C88`, i.e. six words `0000 0000 0000 0000 0001 0000`.
- EXP266 will test that response exactly once against the local XTR M. This remains a hypothesis until run.
- No inference is made that `0001` is a generic ready flag; its semantics remain unknown.

## EXP264 — proven sync tail and background-overlay caveat

Local XTR now proves the ordered Online/Link tail:
`06EA/7 -> ACK -> 06F1/3 -> ACK -> 06F4/19 -> ACK`.

Immediately after the `06F4` ACK, the first observed FC16 was `085F/5` (+107 ms). Because `085F/5` was already established from passive captures as recurrent background traffic, it must not be promoted to an ordered synchronization stage merely because it is first after an ACK.

Protocol implication: future post-sync discovery must distinguish ordered session traffic from recurrent background families. Known recurrent `085F/5` should be logged but ignored as a discovery terminator after `06F4`; `04A6/13` remains context-sensitive because it can be both recurrent and ordered depending on phase.

The next meaningful stage after `06F4` remains unknown locally. `0708/count6` mailbox timing is still unresolved and no local mailbox response has been sent.

## EXP263 finding — 055A..06C5 33-word sync run locally confirmed

## EXP264 target — final small FC16 tail before mailbox/runtime observation

EXP263 locally proved the ordered 12-block 33-word run `055A..06C5` and captured `06EA/count7` next. EXP264 therefore tests only the next genuine Eco 5 tail: `06EA/7 -> 06F1/3 -> 06F4/19`, using standard one-shot FC16 ACKs. After `06F4` it is capture-only; FC03, including `0708/count6`, is evidence only and receives no response.

EXP263 locally confirmed the genuine Eco 5 FC16 sequence:
055A/33 -> 057B/33 -> 059C/33 -> 05BD/33 -> 05DE/33 -> 05FF/33 ->
0620/33 -> 0641/33 -> 0662/33 -> 0683/33 -> 06A4/33 -> 06C5/33 -> 06EA/7.

All twelve 33-word blocks were ACKed exactly once and in order. 06EA/count7 arrived +475 ms after the 06C5 ACK and was not ACKed. The run remained parser/RX clean. This is strong evidence that the XTR and genuine Eco 5 share this synchronization segment.

Do not generalize this into broad FC16 ACKing: only the exact known ordered stages are proven. Full Online/Link establishment, the later 06F1/06F4 stages, and local 0708 mailbox timing remain open.

## EXP262 — accelerated chain proof through 055A/count33

EXP262 establishes the following local ordered Online/Link path after the already-proven prefix: `04A6/13 -> 04BA/22 -> 04D8/27 -> 04F6/14 -> 050A/19 -> 051E/10 -> 0532/18 -> 0546/20 -> 055A/33`. The first eight pages were ACKed exactly once; `055A/33` was captured only. This matches the genuine Eco 5 ordering and validates larger bounded ACK batches.

Important refinement: `04A6/13` is recurrent elsewhere on the bus, but in EXP262 it was ACKed only in the exact post-`0492` sync phase, after which the expected ordered chain continued. Context therefore remains essential; address alone does not identify a sync-stage occurrence.

The known incomplete-session failure (`DHW-side 0` / `COMM. ERR ONLINE/LINK`) remains a session-completion hypothesis, not a proven causal mechanism. `0708/count6` has not yet been serviced locally.

# THERMIA PROTOCOL FINDINGS

## EXP262 accelerated-batch target

EXP261 locally confirmed the ordered chain through `0492/count11`, with `04A6/count13` immediately next. EXP262 deliberately increases batch size while retaining exact sequencing and fail-closed checks. Target progression:
`04A6/13 -> 04BA/22 -> 04D8/27 -> 04F6/14 -> 050A/19 -> 051E/10 -> 0532/18 -> 0546/20`, then capture-only. Genuine Eco 5 predicts `055A/count33` after this block.

`04A6/13` remains context-sensitive because it is also recurrent passive traffic; EXP262 only ACKs it in phase 12 immediately after a successful `0492/count11` ACK. This does not establish every `04A6` occurrence as a synchronization page.


## EXP261 result — ordered sync now proven through 0492

EXP261 extended the local XTR Online/Link synchronization prefix using a bounded batch of exact standard FC16 ACKs:

`046A/18 -> ACK -> 047E/19 -> ACK -> 0492/11 -> ACK -> 04A6/13`

The post-0492 `04A6/count13` request arrived +576 ms after the 0492 ACK and was not acknowledged.

This is important because `04A6/13` is also a recurrent passive family. EXP261 shows that, in the approved synchronization state, it can also occupy the expected ordered next position after `0492/11`. The observation does not make every passive `04A6` instance part of the sync chain; context remains necessary.

The local chain is now directly demonstrated through:
`03E8/14 -> 03FC/11 -> 0410/22 -> 042E/15 -> 0442/13 -> 0456/12 -> 046A/18 -> 047E/19 -> 0492/11 -> 04A6/13`.

Full Online/Link establishment is still not proven because downstream pages and FC03/mailbox service remain unanswered.


## EXP261 target — bounded continuation after EXP260

EXP260 validates batching already-proven genuine Eco 5 FC16 synchronization pages. The next bounded continuation is `046A/18 -> 047E/19 -> 0492/11`, each with a standard one-shot FC16 ACK. The first different post-0492 frame is capture-only.

Genuine Eco 5 reference order places `04A6/count13` next, but prior capture analysis also classifies `04A6/13` as a recurrent passive family overlaid on synchronization. Therefore EXP261 does not use the presence or absence of `04A6` alone as a hard protocol success/failure criterion. No broad ACKing and no `0708` response are authorized by this experiment.


## EXP260 finding — bounded batch reproduces the next three genuine sync transitions

Local XTR evidence now proves the ordered post-approval prefix through `046A/count18`:

`03E8/14 -> ACK -> 03FC/11 -> ACK -> 0410/22 -> ACK -> 042E/15 -> ACK -> 0442/13 -> ACK -> 0456/12 -> ACK -> 046A/18`

The first three stages were proven incrementally in EXP257-259; EXP260 then safely batched the next three exact Eco 5 pages. There were no same-stage retries, unexpected peer responses, or post-return parser/drop errors. `046A/count18` was deliberately left unanswered.

The recurring DHW-side literal `0` appeared again during/after this deliberately incomplete session. This supports the incomplete-session side-effect model, but the exact semantics of the UI `0` remain unknown.

Protocol implication: small, pre-verified page batches are now evidence-backed as a practical way to progress the remaining genuine sync chain without one controller reboot per FC16 page. This does **not** authorize broad blind ACKing or FC03/mailbox emulation.

Last updated: 2026-09-27 after EXP259 / EXP260 prepared

## EXP260 bounded-batch protocol target

EXP256–259 have now locally reproduced the same genuine Eco 5 ordered Online/Link prefix through `042E/count15`. Because four consecutive reference stages have matched, EXP260 deliberately increases throughput while remaining fail-closed: it ACKs only the next three exact known reference blocks `042E/15`, `0442/13`, `0456/12`, in that order, and then captures the first different stage. The external reference predicts `046A/count18`.

This does **not** authorize broad FC16 ACKing or any `0708` mailbox response. A mailbox request at any point remains a capture-and-stop event in EXP260.

## EXP259 — local ordered Online/Link sync confirmed through `042E/count15`

EXP259 extends the bounded local XTR progression by exactly one ACK.

Observed local sequence:
`R1 -> 03E8/14 -> ACK -> 03FC/11 -> ACK -> 0410/22 -> ACK -> 042E/15`

Timing:
- approval: +1283 ms after BUS_RETURN;
- `03E8`: +138 ms after R1;
- `03FC`: +682 ms after `03E8` ACK;
- `0410`: +1498 ms after `03FC` ACK;
- `042E`: +696 ms after `0410` ACK.

Exact `042E/count15` payload words:
`0001 0001 0000 000A FFF6 0005 001E 0000 002D 0000 0000 0000 0000 0000 0000`.

**Strong conclusion:** the local XTR follows the same genuine Eco 5 initial synchronization ordering at least through the first four ordered FC16 pages:
`03E8/14 -> 03FC/11 -> 0410/22 -> 042E/15`.

**Unknown:** whether all later Eco 5 pages and the `0708/count6` mailbox phase are identical on the XTR. Full Online/Link establishment is not yet proven.

---

Last updated: 2026-09-27 after EXP258

## Reproducible incomplete-session UI failure mode — confirmed through EXP259

Across multiple active approval/sync experiments, including EXP259, entering the native Online/Link state machine and then deliberately stopping before a complete endpoint session produces the same front-panel symptoms: DHW-side literal `0` and exact `COMM. ERR ONLINE/LINK`. One normal controller reboot restores normal operation.

This strongly supports an incomplete-session timeout interpretation, but does not yet prove the exact causal point or required minimum service depth. A future sufficiently complete session that does not trigger the alarm would be the cleanest confirmation.


## EXP258 — XTR confirms third ordered Online/Link sync block

EXP258 extends the local post-approval proof by one stage. After one R1 response, one exact ACK of `03E8/count14`, and one exact ACK of `03FC/count11`, the next controller block is exact `0410/count22`. Timing: approval +1243 ms after BUS_RETURN; `03E8` +138 ms after R1; `03FC` +691 ms after the 03E8 ACK; `0410` +1501 ms after the 03FC ACK.

**Strong protocol conclusion:** the local XTR now matches the genuine Eco 5 ordered prefix through three FC16 pages:

`approval response -> 03E8/14 -> ACK -> 03FC/11 -> ACK -> 0410/22`.

`0410` was intentionally not ACKed, so no claim is made about later local ordering or mailbox entry. Full Online/Link establishment remains unproven.

The user again observed the DHW/tank-side literal `0` and the exact `COMM. ERR ONLINE/LINK` alarm. This repeat strengthens the interpretation that the alarm is associated with an approved-but-incompletely-serviced Online/Link session, but that remains a hypothesis until a sufficiently complete session avoids the alarm.

---

Last updated: 2026-09-27 after EXP257; EXP258 prepared. Detailed historical findings restored from the uploaded canonical snapshots.

## External Eco 5 endpoint behavior refined after EXP257

The complete raw capture confirms the cold-start approval stream is startup-bounded rather than a steady-state feature in the observed Eco 5 sessions: first approval requests occur about 1.2 s after bus return, while an already-running steady-state segment with the gateway connected has no `071C/0730` traffic. Therefore steady-state absence on another model is not evidence that its cold-start stream is absent.

Two genuine successful sessions provide the same transfer prefix:

`approval response -> 03E8/14 -> ACK -> 03FC/11 -> ACK -> 0410/22`

This is now locally matched by EXP257 through `03FC/11`.

`04A6/13` and `085F/5` should remain classified as recurrent/passive families that can be interleaved with the transfer. Their ACK timing is phase-dependent across the two external power-ups, so they are not established approval preconditions and should not be promoted into the invariant ordered sync chain.

The genuine endpoint begins answering `0708/count6` while FC16 synchronization is still underway. The raw repeated idle response is:

`0F 03 0C 0000 0000 0000 0000 0001 0000 <CRC>`

=> six words: `0000 0000 0000 0000 0001 0000`.

A public comment wrote the fifth word as `0100`; this is not what the raw frame contains under standard Modbus big-endian register ordering. Preserve the raw value `0001` unless later evidence establishes a deliberate byte-swapped semantic representation.

Later fifth-word values in the same session descend through `03DC` (988), 984, 976, 908, 896, 768, 512, then 0. The sequence is factual; "pending synchronization item counter" is only a hypothesis.

The known local `COMM. ERR ONLINE/LINK` after partial participation is compatible with a session-service timeout, but that causal interpretation remains a hypothesis until a sufficiently serviced local session avoids the alarm.
## EXP257 — local XTR reproduces genuine Eco 5 `03E8 -> 03FC` synchronization transition

EXP257 adds the first local XTR proof of the next acknowledged post-approval transition.

Observed sequence:

```text
0x0F FC17 approval request
  -> one replayed R1
  -> FC16 03E8/count14
  -> one standard FC16 ACK
  -> FC16 03FC/count11
  -> no further ACK
```

Timing in EXP257:
- approval request: +1285 ms after BUS_RETURN;
- `03E8/count14`: +130 ms after R1;
- `03FC/count11`: +691 ms after the one `03E8` ACK.

Exact `03FC` request:

`0F1003FC000B160028000A0037000000000000000200120028001E003C369E`

Payload words:

`0028 000A 0037 0000 0000 0000 0002 0012 0028 001E 003C`

The experiment deliberately did **not** ACK `03FC`.

**Strong protocol conclusion:** the local XTR now matches the genuine Eco 5 Online/DCM synchronization prefix through two post-approval stages:

`approval response -> 03E8/count14 -> ACK -> 03FC/count11`

The genuine Eco 5 reference proves this same transition in two independent successful approval cycles and then shows:

`03FC/count11 -> ACK -> 0410/count22`.

This materially strengthens the cross-model architectural link. It does not yet prove that the local XTR will follow the complete Eco 5 synchronization chain or reach the `0708/count6` mailbox/runtime phase.

No semantic register write was performed in EXP257: the only new active frame was a standard FC16 acknowledgement echoing address/count and carrying no register-value payload.

Last updated: 2026-09-27 after EXP256 + full external Eco 5 capture refinement
## EXP256 — R1 crosses approval boundary into native 03E8 synchronization

EXP256 materially resolves the ambiguity left by EXP252/EXP255. After one exact replay of the already-tested R1 response to the first local `071C/0730` approval request:

- the approval loop stopped after **one** request;
- no second approval request occurred;
- the controller immediately began `0x0F FC16 03E8/count14`;
- first `03E8/count14` arrived **124 ms after R1**;
- `03E8/count14` repeated **389 times** through +419.896 s;
- the only other FC16 family was one boot-only `04BA/count22` request before R1;
- passive runtime families `04A6/count13` and `085F/count5` were both absent;
- no FC03 request appeared;
- EXP256 deliberately provided no FC16 ACK or FC03 response.

**Strong protocol conclusion:** R1 is not merely suppressing one passive FC16 family. It advances the local XTR controller across the approval/retry state into the native acknowledged `0x0F` synchronization state machine, whose first observed stage is `03E8/count14`. With no endpoint ACK, the controller stalls and retransmits that block.

This links two previously separate findings:
- EXP252: R1 terminates the `071C/0730` retry loop and causes a reproducible controller-visible side effect;
- EXP137+: acknowledging native `03E8/count14` advances an ordered controller->0x0F transfer sequence.

The EXP255 numerical clue (`582 - 195 ≈ 386`) is now recorded as a misleading coincidence rather than the correct mechanism. EXP256 shows that the post-R1 traffic is a **new 03E8 synchronization family**, not persistence of the passive `04A6` family.

The user again observed the DHW/tank-side literal `0`, followed after the run by the exact same front-panel alarm as EXP252: **`COMM. ERR ONLINE/LINK`**. No VERSION-screen change was seen; this is compatible with the architecture because VERSION `EXP` display is controlled by the separate `0x06/AFD1` expansion metadata path, not by the `0x0F` approval/synchronization path tested here.

**Still unknown:** full Online/Link session establishment, the required ACK chain after `03E8`, any eventual FC03/mailbox phase, and the semantic meaning of the DHW-side `0`.
## 2026-09-27 — EXP256 approval-to-sync transition

EXP256 provides the first direct local link between the startup `071C/0730` approval exchange and the native `0x0F` synchronization chain.

Observed sequence:

```text
BUS_RETURN
  -> first exact 071C/0730 approval request
  -> one-shot R1 response
  -> approval retries stop
  -> 124 ms later: controller FC16 03E8/count14
  -> no endpoint ACK
  -> repeated 03E8/count14 for the remainder of the 7-minute run
```

Complete active census: `04BA/count22` x1 before R1, then `03E8/count14` x389; `04A6/count13` x0; `085F/count5` x0; no FC03 phase.

**Protocol consequence:** the earlier EXP255/EXP252 count coincidence did not represent simple selective `085F` suppression. R1 instead advances the controller into the first stage of the acknowledged native settings synchronization state machine previously mapped in EXP137+. The endpoint is expected to ACK the FC16 block before progression.

**Session-status refinement:** R1 is accepted far enough to suppress approval retries and start sync, but this is not proof of a complete Online/Link session. In EXP256 no FC16 ACK, FC03 mailbox response, or later sync stage was supplied.

**UI side effect:** the DHW/tank-side literal `0` reappeared and the front panel again raised **`COMM. ERR ONLINE/LINK`** after the active run, exactly reproducing EXP252; VERSION did not change. This makes the R1 incomplete-session side effect reproducible while remaining separate from the `0x06/AFD1` VERSION metadata path. Exact meaning of the `0` remains unknown.


---
## 2026-09-27 — complete genuine iTec Eco 5 gateway capture: approval -> sync -> mailbox chain

A complete 1482.480 s Eco 5 gateway capture provides the first continuous raw evidence connecting genuine approval responses to the downstream acknowledged synchronization state machine.

### Approval retry behavior

The capture contains 99 exact `0x0F FC17 read 0730/count8 + write 071C/count8` requests in three windows (29, 41 and 29 requests). Their median cadences are about 4.24 s, 4.26 s and 4.21 s. 98 of the 99 16-byte `071C` payloads are unique; one payload repeats once. Thus the genuine Eco 5 source normally regenerates the 16-byte challenge-like value across retries.

Two successful challenge/response pairs are present inline in the raw capture:

```text
C1 63CE FB32 C6F4 1382 0879 9237 0CAC EEBA
R1 1691 A5F3 F8E8 D587 3892 4416 E8E6 A3D5

C2 31FB 59FC 8FB1 175C D89F 904D 06D9 2EA4
R2 FD63 6CCD 0F92 1D83 FF23 2A1A 2413 B372
```

### Reproducible post-approval prefix

Both successful responses produce the same prefix:

```text
FC17 response
 -> 03E8/count14 request
 -> FC16 ACK 03E8/count14
 -> 03FC/count11 request
 -> FC16 ACK 03FC/count11
 -> 0410/count22 request
 -> FC16 ACK 0410/count22
```

Timing:

```text
                         R1 cycle       R2 cycle
03E8 request             +92 ms         +92 ms
03E8 ACK                 +137 ms        +122 ms
03FC request             +510 ms        +536 ms
0410 request             +1.950 s       +2.189 s
```

This is stronger than the earlier local EXP137 observation. `0410/count22` is not the demonstrated immediate successor to `03E8`; the genuine Eco 5 reference contains an intervening `03FC/count11` block.

### Ordered initial synchronization export

The first successful cycle establishes this ordered FC16 sequence (retries omitted):

`03E8/14 -> 03FC/11 -> 0410/22 -> 042E/15 -> 0442/13 -> 0456/12 -> 046A/18 -> 047E/19 -> 0492/11 -> 04A6/13 -> 04BA/22 -> 04D8/27 -> 04F6/14 -> 050A/19 -> 051E/10 -> 0532/18 -> 0546/20 -> 055A/33 -> 057B/33 -> 059C/33 -> 05BD/33 -> 05DE/33 -> 05FF/33 -> 0620/33 -> 0641/33 -> 0662/33 -> 0683/33 -> 06A4/33 -> 06C5/33 -> 06EA/7 -> 06F1/3 -> 06F4/19`.

The next observed stage is `07D0/count19`, interleaved with `FC03 0708/count6` mailbox polls. Later established traffic includes acknowledged `07E4`, `07F8`, `080C`, `0820`, `0834`, `0848`, `0864` and `0870` pages plus dynamic `0708` responses.

### Consequences for the local XTR project

- EXP256's local `R1 -> 03E8/count14` transition is now a direct prefix match to genuine Eco 5 Online/DCM behavior.
- The response replay reaches a real protocol boundary, not an arbitrary controller retry quirk.
- Full session establishment still cannot be inferred from R1 alone; the genuine endpoint acknowledges a long sequence and participates in `0708` mailbox/runtime exchange.
- EXP257 remains correctly bounded: ACK exactly the first local `03E8/count14` once, then capture the first different block without answering it.
- External-reference positive discriminator is now specifically `03FC/count11`. A local `0410/count22` first would demonstrate a platform/order difference and would also be valuable.

## Bus

- Modbus RTU-like framing
- 9600 baud
- 8 data bits, even parity, 1 stop bit
- valid Modbus CRC

## Important slaves

- 0x02: controller state/sequencer data
- 0x06: local expansion/accessory presence/version path; **not proven to be the Online/DCM endpoint**
- 0x0A: room-sensor path
- 0x0F: native controller application/settings/state serializer; genuine Online/DCM reference systems also use this role for mailbox/state exchange
- 0x1E: outdoor-unit path

## 0x06 FC17 expansion/accessory path

Controller reads AFC8..AFD3 (12 words) and writes AFDC..AFE0 (5 words).

Normal unserved poll cadence: ~4.3 s.
After valid accessory response: alternating fast cadence ~0.7 s / ~1.4 s.

Fast cadence proves syntactic participation only; it does not prove semantic acceptance.

## AFCA / word2 transport handshake

Canonical transaction:

1. semantic payload stable, AFCA=0000
2. assert AFCA=03E8
3. controller 0x0F:0861 rises to 16
4. deassert AFCA=0000 while payload remains stable
5. controller 0x0F:0861 falls to 0
6. payload may then change

EXP92 timing example:

- REQ assert -> ACK high: 401 ms
- REQ deassert -> ACK low: 1031 ms

This is a proven transport-level handshake.

The **AFCA value** `03E8` is therefore a transport strobe/constant in this 0x06 transaction and must not be confused with native `0x0F` register address `0x03E8`, which is independently proven to belong to the Heating Curve/settings family.

## Historical A80E/AFDC state propagation

Older passive data repeatedly showed:

- controller A80E: 0 -> 32
- next relevant 0x06 controller write AFDC: 0 -> 32
- later A80E: 32 -> 0
- then AFDC: 32 -> 0

This is controller-originated state propagation and is distinct from the 0861 transaction ACK.

## EXP92 result

A correctly completed four-phase handshake followed by 90 s of the historical REQ-low envelope:

00FF,0001,0000,0001,0...

did not reproduce the historical online-state cycle.

Therefore:

- completed transport handshake is not sufficient;
- historical envelope is not sufficient;
- their combination is not sufficient under the tested controller state.

## New controller-state correlation

Older passive capture:

- A80F changed 80 -> 50 after outdoor-unit request turned off;
- while A80F remained 50, repeated A80E/AFDC 0<->32 cycles occurred;
- later A80F changed 50 -> 80 and the outdoor-unit cycle request became active.

EXP92 controller frame showed:

- A80C=64
- A80D=0
- A80E=0
- A80F=10
- A810=10
- A811=FFFF
- A812=0

Working hypothesis: the historical DCM state cycle may be gated by controller state, with A80F=50 currently the strongest observed discriminator. Correlation is not causation. This passive discriminator remains the next DCM fallback after the higher-value EXP93 room-sensor write-path replication.

## Room-sensor semantic path

Our XTR M passive evidence:

- genuine room-sensor setpoint event updates central controller setpoint;
- value later propagates back through B3C5;
- independent master write to B3B1 was ACKed but not adopted by the controller.

Independent transmit-side confirmation from `piotr-romanowski/thermia-bus-sniffer` commit `b4c27157402c49624917d523e016b249cdfc4e11` on iTec Eco / DHP-AQ-family hardware establishes:

- `0x0A` controller poll reads `B3B0..B3B2` and writes `B3C4..B3C6`;
- `B3B0 / 46000` = room temperature x10;
- `B3B1 / 46001` = pending room-setpoint request, x1 whole °C;
- `B3B2 / 46002` = unused/unknown in that setup;
- a non-zero B3B1 returned in the slave response makes the controller adopt that room setpoint;
- the controller then pushes the adopted value back via `B3C5 / 46021`;
- returning B3B1=0 releases the request but leaves the adopted setpoint latched;
- restoring a previous value requires explicitly requesting that value.

**Strong architectural conclusion:** the failed independent master-write test does not contradict B3B1 semantics. The write path is slot/role sensitive: the ESP must behave as slave 0x0A and answer the controller's poll.

**Local status:** transmit semantics are independently confirmed cross-model but not yet confirmed on this XTR M. EXP93 is the collision-safe local replication test.
## Control architecture decision

The intended production control architecture is **not** room-sensor emulation. The target is to emulate the Thermia/Danfoss Online/Connect/DCM03 accessory on slave `0x06`. Slave `0x0A` findings remain protocol evidence only.

## DCM03 / Danfoss Link firmware evidence

Recovered host-side HE Set/Get framing from Link CC firmware:

```text
BYTE endpoint
BYTE counts = (GET_count << 4) | SET_count
WORD SET_ID[]
WORD GET_ID[]
SET values...
```

Relevant abstract parameter IDs include `0x030A OperationMode`, `0x4400..0x4417` DHP parameters, and especially `0x4414 IntegrationMode`. `IntegrationMode` is GET-on-sync + SET-on-sync and then clears its SET-on-sync flag. Parameters are grouped into partial sync groups 0/1/2.

The Link CC image does not expose the final DCM03 -> local Thermia RS485 serializer. Raw HE packet layouts tested directly through `AFC8..AFD3` were negative, so an additional DCM-side translation/state layer remains strongly indicated.

Official Danfoss documentation states that DHP-AQ Link integration requires HP software >=2.2 and that later Link firmware may re-offer Heat Curve for 30 minutes after initial communication when the HP rejects/forgets it. This supports an initial synchronization/desired-state model. It does not prove any specific meaning for `A80E`, `A80F`, or `AFDC`.

## EXP93 status refinement

Two supplied EXP93 logs show the experiment armed correctly but no stable `A80F=50`; the 180 s capture never started. Therefore EXP93 remains inconclusive and must not be recorded as a negative result.

## EXP94 cold-boot state machine result

A true controller cold boot with slave 0x06 unanswered produced the following reproducible sequence in the completed 600 s capture:

```text
~0.7 s:  A80F/A810 = 5
~1.8 s:  A80E 0x00 -> 0x08
~2.8 s:  A80E 0x08 -> 0x28
~5.6 s:  AFDC 0x00 -> 0x10; AFE0 25 -> 20
~11.3 s: A80F/A810 5 -> 10
then stable through 600 s
```

Final stable image:

```text
A80C..A812 = 0040,0000,0028,000A,000A,FFFF,0000
AFDC..AFE0 = 0010,0000,0000,0000,0014
0861        = 0000
```

No settings changes occurred. 140 unserved 0x06 polls stayed on the normal long cadence (4086..4537 ms).

**Strong conclusions:**

- cold-boot integration state settles within about 11 s when 0x06 is unanswered;
- there is no hidden late transition up to 10 minutes;
- historical `A80E/AFDC 0x20 <-> 0` cycling is not simply ordinary cold-boot initialization;
- `0861` remains distinct from the longer-lived A80E/AFDC state machine.

**Refined after EXP95:** `AFDC=0x10` cannot simply mean “no accessory present,” because EXP95 supplies a valid 0x06 responder and still reaches the same state. It remains consistent with a higher-layer not-established/waiting/session state; exact semantics are unknown.

## EXP95 completed result

EXP95 answered every exact post-cold-boot `0x06 FC23` poll with 12 zero words (`AFCA=0`).

Observed over the complete 120 s run:

```text
frames=1133
06polls=112
tx=112
refused=0
06_min_ms=638
06_max_ms=1503
0861_changes=0
settings_pushes=0
settings_changes=0
outdoor_state_changes=0
resync_delta=1
drop_delta=0
```

The controller still converged to:

```text
A80E = 0028
A80F = 000A
A810 = 000A
AFDC = 0010
0861 = 0000
```

**Strong conclusions:**

- valid 0x06 presence from the first cold-boot poll immediately establishes the fast transport cadence;
- it does not advance the DCM application/session state;
- `AFDC=0x10` is not simply an “accessory absent” indicator;
- transport presence, transaction REQ/ACK, and higher application/session state are separate observable layers.

## EXP96 completed result

EXP96 executed the historical envelope in the true cold-boot EXP95 context. The four-phase transport transaction completed cleanly:

```text
preload:   00FF,0001,0000,0001,0...
REQ high:  00FF,0001,03E8,0001,0...
0861:      0000 -> 0010 after 367 ms
REQ low:   00FF,0001,0000,0001,0...
0861:      0010 -> 0000 after 1196 ms
```

No semantic/application progress followed: `settings_changes=0`, `rsp02_changes=0`, and the higher-layer controller state did not advance beyond the EXP95 behaviour.

**Strong conclusion:** the historical envelope is sufficient for the proven transport REQ/ACK mechanism but is not a sufficient DCM03 identity/init/application message, even in cold-boot context.

## Natural A80E/AFDC transition observed before EXP96

Before EXP96 was armed, with the ESP passive, the bus naturally showed:

```text
A80E: 0028 -> 0020 -> 0000
AFDC: 0010 -> 0000
```

This was not experiment-induced.

**Refinement:** A80E/AFDC should no longer be treated as simple dedicated DCM-session indicators. They are more likely broader controller/accessory-state propagation fields; exact semantics remain unknown.

## EXP97 test target

EXP97 is fully passive and focuses only on correlating natural A80E/AFDC edges with already-observable state:

- `A80C..A812`;
- `A7F8..A806`;
- `AFDC..AFE0`;
- `0x0F:0861`;
- outdoor-unit command block `0x1E:0000..0008`;
- outdoor operating-state reference.

No `0x06` response or other TX is generated. The goal is to determine whether the natural `0x28->0x20->0x00 / 0x10->0x00` sequence belongs to ordinary controller/outdoor operation and thereby remove A80E/AFDC as misleading DCM-session success criteria.


## EXP97 natural-state result

The natural sequence was reproduced under fully passive observation:

```text
A80E 0028 -> 0020
~1.06 s later: A80E 0020 -> 0000
~2.66 s later: AFDC 0010 -> 0000
```

At every edge, `0861=0000`, outdoor state=`0010`, and captured `CMD1E` plus paired `RSP02` were unchanged. No ESP TX occurred.

**Protocol refinement:** A80E/AFDC cannot be treated as dedicated DCM03 login/session indicators. They are broader internal controller/accessory lifecycle fields whose exact semantics remain unknown. They should no longer be the primary success criterion for DCM semantic experiments.

## EXP98 result

EXP98 returns focus to the actual accessory response bank. It isolates the first response word only:

```text
A: AFC8=0000, all others 0000, 20 s
B: AFC8=00FF, all others 0000, 30 s
A: AFC8=0000, all others 0000, 40 s
AFCA remains 0000 throughout
```

This is not a write-command test. It is an influence test for whether AFC8 alone changes controller, settings, cadence, ACK, or outdoor behaviour.


## EXP98 result
AFC8=00FF alone is not a standalone semantic trigger. In a controlled A/B/A run it produced no detectable effect on controller state, AFDC..AFE0, 0861, settings, CMD1E, outdoor state or polling cadence.

## EXP99 target
Test the remaining historically observed non-REQ fields and their combinations in a compact matrix while keeping AFCA=0000. This preserves interpretability while increasing throughput compared with one experiment per word.


## EXP99 protocol result

A controlled ten-phase matrix tested `AFC8=00FF`, `AFC9=0001`, and `AFCB=0001` individually, pairwise, and together while keeping `AFCA=0000`. All combinations were inert: no `0861`, settings, controller, AFDC..AFE0, CMD1E, or outdoor-state reaction occurred.

**Refinement:** the historical pattern `00FF,0001,REQ,0001` should not be interpreted as three independent command selectors plus REQ. Of those four fields, only `AFCA=03E8` has independently proven behaviour. The remaining fields may be structured payload/header data that is only interpreted during a valid transaction.

## EXP100 protocol target

Test that exact remaining possibility by carrying six historically grounded AFC8/AFC9/AFCB combinations through the already-proven four-phase transaction handshake. This increases throughput while preserving one-variable-family interpretability and avoids arbitrary values or setting targets.

## EXP100 protocol result

Six historically grounded AFC8/AFC9/AFCB payload combinations were each transported through the proven four-phase transaction handshake. Every transaction generated a complete `0861 0->16->0` ACK cycle, but none changed settings, AFDC..AFE0, controller state, RSP02, CMD1E or outdoor state.

**Refinement:** `AFCA=03E8` is confirmed as transport/data-valid REQ independent of application semantics. The historical `00FF,0001,REQ,0001` pattern is not sufficient to encode a recognized DCM application command. The missing DCM03 serializer/state machine must involve other AFC8..AFD3 fields and/or a higher-level multi-message/session sequence.


## EXP100 finding — first historical response words are transport-insufficient

Six canonical REQ/ACK transactions tested AFC8=00FF, AFC9=0001 and AFCB=0001 separately and in combinations. All six received normal `0861 0->16->0` acknowledgements, while controller state, settings, AFDC..AFE0, 0x1E command state and outdoor state remained unchanged.

Therefore the historical `00FF,0001,REQ,0001` prefix is not a sufficient DCM03 application command. AFCA=03E8 remains the only word in that prefix with a proven role: transport REQ/data-valid.

## EXP101 probe scope

AFCC..AFD3 remain unmapped accessory->controller response words. Their semantics are unknown. EXP101 probes only the minimal non-zero value `0x0001`, one word at a time, inside the proven transport handshake. Any observed effect must therefore be treated as positional influence first, not yet as semantic decoding.

## EXP101 finding — tail words AFCC..AFD3

Each response-bank word `AFCC`, `AFCD`, `AFCE`, `AFCF`, `AFD0`, `AFD1`, `AFD2`, and `AFD3` was individually set to `0x0001` inside a valid canonical `AFCA=03E8` transaction. All eight transactions generated the normal `0861` ACK-high/ACK-low cycle but produced no detectable changes in controller state, paired RSP02, AFDC..AFE0, settings, CMD1E, or outdoor state.

Interpretation: no tail word is a simple standalone `0x0001` selector. Combined with EXP98–100, isolated-word probing across the full `AFC8..AFD3` bank has not revealed the DCM semantic layer. Future work should focus on structured multi-word messages, payload framing/metadata, or multi-message initialization/session sequencing.

## Archive recovery finding — prior tail coverage was broader than current summary

Historical logs show that the response-bank tail had already been exercised more extensively than the current condensed state suggested. EXP24/25 tested words 4..11 with `0001` while `0861` was high, and EXP26/28 tested structured word4/word5 values. EXP16/18/14/15 also showed that AFC9/AFC8/AFCB values can vary without changing the basic AFCA=03E8 transport ACK behavior.

**Protocol implication:** isolated value probing is exhausted. A more plausible structure is that one of the historical `0001` fields is metadata such as a payload length/count. If so, earlier probes that added data beyond word3 while retaining a count of 1 could have been ignored by design.

## EXP102 protocol target — coherent declared-length interaction

Test coherent count-plus-payload structures rather than arbitrary tail values. Compare the historical count-1 control against AFC9-declared lengths 2/3, AFCB-declared lengths 2/3, and a both-length2 case. This is the smallest controlled experiment that tests whether tail words become meaningful only when a matching length/count grows with them.

## EXP102 finding — AFC9/AFCB are not simple payload length/count fields

Six coherent structures were tested using the proven transport handshake. Increasing `AFC9` to 2/3 while adding AFCC/AFCD payload words, increasing `AFCB` to 2/3 with matching tail words, and setting both fields to 2 all produced normal `0861 0->16->0` transport ACKs but no semantic effect.

**Refinement:** neither AFC9 nor AFCB behaves like a simple declared word-count whose increase makes AFCC/AFCD meaningful. The missing DCM03 application layer is therefore more structured than the tested prefix/count model and likely requires a different framing rule or a multi-message/session sequence.


## Historical archive audit — response-bank search space refinement

A full archive audit after EXP102 recovered at least 45 unique logged experimental response forms and confirmed that first-word/header, selector, tail-word, same-packet, phase, presence/session, HE-envelope and count-like hypotheses have already been exercised extensively.

No archived trace could be identified as a genuine DCM03/Thermia Online response. Logged accessory response payloads are synthetic ESP experiment traffic; raw `06 17 AFC8...` frames are controller requests and expose only controller->accessory `AFDC..AFE0` data.

**Protocol implication:** further isolated field/value guessing is not justified. The unresolved DCM layer should be treated as a structured/stateful serializer problem. The highest-value missing evidence is a genuine DCM cold-boot dialogue and one known parameter change/rollback.


## EXP103 finding — repeated identical canonical transactions are insufficient

Three consecutive transactions using the unchanged historical envelope `00FF,0001,REQ,0001,0...` were completed without the recovery gap used in earlier matrices. All three produced the normal `0861` ACK-high/ACK-low cycle, but there were no settings, controller, AFDC..AFE0, CMD1E or outdoor-unit changes during the experiment.

**Refinement:** the missing DCM03 application layer is not unlocked merely by repeating the same accepted transport transaction several times in succession. This weakens a simple cumulative/retry-count interpretation and further shifts the remaining search toward a specific ordered startup dialogue, structured metadata/sequence/checksum, or proprietary DCM-side serialization.

A natural `A80E 0->32` followed by `AFDC 0->32` occurred only after the EXP103 summary and repeated later in the same log. This is additional evidence that these fields participate in ordinary controller lifecycle/state propagation and should not be used as DCM-session success markers.


## EXP104 negative finding — AFC8 is not a simple alternating transaction sequence field
A three-transaction canonical chain using AFC8 `00FF -> 00FE -> 00FF` produced normal transport ACKs on all three transactions but no settings or command effect. This reduces support for a simple AFC8 transaction identity/sequence interpretation. Natural A80E/AFDC `0x20` cycling occurred independently during the subsequent all-zero observation and repeated later, reinforcing that it is not a reliable DCM session-success marker.


## EXP105 protocol target — controller-state gating

EXP98–104 substantially reduce support for isolated payload, count, repetition, and simple AFC8-sequence interpretations. EXP105 therefore keeps the known historical payload unchanged and tests a different dimension: whether the controller only interprets a DCM application transaction during the naturally recurring `A80E=0x0020` / `AFDC=0x0020` lifecycle window. The ESP remains passive until that state is directly observed.


## EXP105 finding — natural A80E/AFDC 0x20 window is not sufficient

A known-good canonical transport transaction was deliberately delayed until the controller naturally presented `A80E=0x0020` and the `0x06` poll carried `AFDC=0x0020`. The transaction still produced only the normal `0861 0->16->0` transport ACK and no setting or command effect.

**Protocol implication:** the missing DCM03 application layer is not explained by a simple controller-state timing gate. Combined with EXP98–104, this further reduces the value of guessed payload/timing permutations. The highest-value next evidence remains a genuine DCM/Online capture or DCM-side firmware/hardware reverse engineering.


## EXP106 target — passive A80F=50 integration-sync discriminator

Firmware/project re-search did not reveal the missing DCM03 -> Thermia serializer or any direct mapping from HE/DHP ParameterIDs into `AFC8..AFD3`. The available host-side evidence still stops at abstract HE Set/Get and sync behaviour; the proprietary/local translation remains outside the recovered host firmware.

The remaining evidence-backed passive discriminator is historical `A80F=0x0032`. Earlier EXP93 captures never reached that state, so its relationship to A80E/AFDC cycling was never actually tested. EXP106 therefore performs no bus TX and captures the broader controller/accessory context when A80F enters/leaves 50.


## Cross-model refinement — Eco 8 / DHP-AQ evidence from Piotr Romanowski

### 0x1E delayed/latched region correction

The `0x1E FC04 0x001E..0x0033` region is **not frozen** and is not proven to be an initialization snapshot. It changes, but much less often and out of step with the live `0x0000..0x0015` block. Treat any apparent pairing as delayed/latched-looking and unconfirmed.

### 0x0A positive-control semantics

`B3B1` is now independently proven as a semantic accessory request field:
- whole-degree encoding (x1);
- non-zero value requests a stored room-setpoint change;
- `0` means no request;
- accepted changes are pushed back by the controller through `B3C5`.

This is a strong architectural reference: Thermia accepts semantic commands when they arrive **inside the polled accessory response**, not as arbitrary independent writes to the same register.

### AFDC..AFE0 on Eco 8

Long passive Eco 8 capture:
- `AFDD=0`
- `AFDE=0`
- `AFDF=0`
- `AFE0` = displayed outdoor temperature x1
- `AFDC` pulses `0 <-> 0x20` continuously with ~64 s period and ~17 s high time.

`A80E` follows the AFDC pulse timing to the second.

**Protocol implication:** A80E/AFDC `0x20` is not a DCM login/approval/session-success marker. It is best treated as ordinary controller lifecycle/heartbeat state.

An isolated `AFDC=0x10` event coincided once with outdoor-unit-active status rising. This single coincidence is insufficient to assign DCM approval semantics to `0x10`.

### 0861 discriminator strengthened

On Piotr's Eco 8, `0x0F:0861` remained at `0` throughout multi-day passive observation. This independently strengthens the interpretation that `0861` movement during Marten's active tests is specifically coupled to the `AFCA=0x03E8` transaction mechanism, rather than being a common spontaneous controller state.

### Search-model refinement for 0x06

Do not use AFDC/A80E values as timing gates for the next active 0x06 experiment.

A more evidence-based architecture hypothesis is:
- the 0x06 slave presents a continuously valid accessory image;
- some fields may be persistent identity/state/capability data;
- `AFCA` is a transaction/request level;
- semantic action may require a request pulse within an already-established stable accessory image.

This remains a hypothesis; the 12-word bank may still be a framed/stateful mailbox rather than purely fixed semantic fields.


## EXP107 prepared protocol question

The next active 0x06 test no longer uses A80F/AFDC/A80E as a DCM session discriminator.

Question:
Does the controller require a continuously-present accessory image before the known AFCA request pulse is treated differently?

Test image:
`AFC8..AFD3 = 00FF,0001,0000,0001,0,0,0,0,0,0,0,0`

After >=60 s of continuous presentation:
`AFCA only: 0000 -> 03E8 -> 0000`

Interpretation rules:
- `0861 0->16->0` = transport transaction completed;
- fast 0x06 cadence = presence only;
- A80E/AFDC changes = controller lifecycle/context only;
- semantic success requires an actual settings/state effect beyond transport ACK.

If EXP107 is negative, the simple "stable accessory image before request" hypothesis is rejected.


## EXP107 finding — persistent presence is not sufficient

Confirmed sequence with a 61.023 s pre-existing stable historical accessory image:

`REQ-low image stable`
→ `AFCA 0000 -> 03E8`
→ `0861 0 -> 16` after 328 ms
→ `AFCA 03E8 -> 0000`
→ `0861 16 -> 0` after 1122 ms
→ same image held 90 s

No semantic consequence:
- settings_changed=0
- A80E remained 0
- AFDC remained 0
- no new session/integration marker emerged
- parser/drop counters remained clean

Protocol conclusion:
The canonical AFCA/0861 mechanism is a transaction-level handshake and is not itself sufficient for application-layer DCM initialization, even after prolonged accessory presence.

Research priority moves from timing/persistence toward reconstructing the application initialization state machine (identity, binding, integration mode, initial sync).


## Firmware-derived application lifecycle — 2.7.42

Recovered from .NET IL inside `RegulationEngine.dll` and `ParameterCache.dll`:

`IntegrationMode (0x4414) update`
→ internal `SystemIntegrationInitRequest = true`
→ `SystemIntegrationInit()`
→ internal `InitSyncDone = false`
→ `Sync(fullUpdate=true)`
→ partial group 0
→ partial group 1
→ partial group 2
→ commit GET values if all groups succeed
→ internal `InitSyncDone = true`

Key correction:
`SystemIntegrationInitRequest` and `InitSyncDone` are internal host booleans, not protocol ParameterIDs.

`IntegrationMode` itself is the wire ParameterID, and `IsSystemIntegration` is simply `(IntegrationMode != 0)`.

`UpdateParameterFlow()` changes ownership of RoomValue, HeatCurve, HeatCurvePlus5, HeatCurveZero, HeatCurveMinus5:
- non-system integration: GET-on-sync
- system integration: SET-on-sync

This makes grouped synchronization / ownership a higher-priority local-mailbox hypothesis than another scalar ID/value probe.

### Identity/binding
`OnHEServiceBind()` compares DivisionID + BrandID + ProductID against allowed products before endpoint allocation.
This is confirmed on the HE/Z-Wave side only; mapping to AFC8..AFD3 remains unknown.


## 2026-09-24 refinement — 0x06 VERSION semantics and 0x0F application blocks

### 0x06 no longer treated as proven DCM/Online identity
Local experiments EXP129–132 materially refine the 0x06 interpretation:
- valid 0x06 responder causes `EXP` / `UITBR.KAART` to appear on the VERSION page;
- `AFD1` is rendered directly as version/10;
- tested `AFD0` values do not change the label/type;
- AFC8/AFC9/AFCB are not required for EXP-version display.

Protocol implication: `0x06` is proven as an accessory/expansion presence + metadata path. Calling it the DCM/Online device is no longer justified without additional evidence. It may still participate in Online integration, but that is now a hypothesis rather than a naming assumption.

### 0x0F application/settings role strengthened
Our own XTR captures contain native FC10 traffic to slave `0x0F`, including the established settings block beginning `0x03E8`. `0x03F4` (decimal 1012) follows the room setpoint and independently aligns with an external ATEC/DHP-AQ observation that 1012 is room-thermostat related.

External Discussion #143 material also reports 0x0F block starts including decimal 1000/1020/1040 and higher regions. These addresses and block lengths are hypotheses for XTR until locally observed. The external files are used as candidate generators only.

### Native 0x085F block
EXP133 partial passive capture locally observed an XTR `0x0F FC10` block at `0x085F`, count 5. This covers `0x085F..0x0863`, so the known transport ACK field `0x0861` is structurally inside a native controller block.

This strengthens:
- `0861` as a real field in a controller-side 0x0F block;
- interpretation of `AFCA=03E8 -> 0861=16` as a transaction-level interaction between the 0x06 accessory response path and a native 0x0F controller block.

It does not yet identify the complete block semantics.

### New native 0x04A6 block
EXP133 also observed a local XTR `0x0F FC10` block starting `0x04A6`, count 13. First captured payload was all zero except `0x04B0=0x4020`. Semantics are unknown. This block was not one of the imported external candidates and is therefore useful XTR-specific evidence.

### Current protocol priority
1. finish EXP133 and establish the native XTR 0x0F shape census;
2. use controlled passive UI correlations to map concrete fields (EXP134 starts with DHW START);
3. only after local read/correlation evidence, infer which 0x0F direction/block is appropriate for safe semantic write testing;
4. do not return to random AFC8..AFD3 payload guessing without new evidence.


## 2026-09-24 — Genuine Online capture changes the 0x0F / 0x06 model

New external evidence from a working Thermia Online installation:
- slave `0x0F` is a real responding Modbus slave in that installation;
- it ACKs FC16 writes and serves FC03 reads;
- controller-originated FC16 traffic cycles through large state/telemetry blocks;
- controller reads `0x03E8` from `0x0F`;
- during an intentional Heat Curve 20->21->20 change, the two captured `0x03E8` read snapshots differ only at the first word (`23 -> 22`);
- recurring `0x06` FC17 polls remain unanswered in the supplied working-Online capture;
- slave `0xA5` is active but unidentified.

Protocol implications:
1. `0x06` is still proven as an expansion/accessory interface but is not required for the Online function shown in this capture.
2. `0x0F` is strongly indicated as a shared controller <-> Online/DCM register interface.
3. Controller FC16 writes to `0x0F` likely carry controller->Online state.
4. Controller FC03 reads from `0x0F` likely consume Online->controller desired/config state.
5. Register direction/ownership is therefore central; a direct second-master write is not equivalent to emulating the expected slave-side register image.
6. Exact physical implementation of slave `0x0F` and the role of `0xA5` remain open.

EXP135/136 correction:
- `03F1` is not supported as live DHW START on the tested XTR M.
- DHW COMFORT/ECO does not alter recurrent `03E8..03F5`.
- `03F1`, `03F2`, `03F3`, `03F5` remain unknown.

Next controlled discriminator — EXP137:
ACK only exact known XTR slave-0x0F FC16 writes and observe whether controller FC03 reads begin. Do not answer FC03 in EXP137.


## EXP137 — acknowledged 0x0F synchronization progression

Local XTR result:
- passive baseline contains repeated `03E8/count14` and `085F/count5` writes with no slave ACK;
- after one standard FC16 ACK to `03E8/count14`, the controller begins issuing `0410/count22`;
- without an ACK, `0410/count22` is retransmitted continuously;
- no FC03 read phase appears before `0410/count22` is acknowledged;
- bus/parser health remains clean.

Protocol implication:
`0x0F` is not behaving like a fire-and-forget telemetry mirror. At least part of the controller->0x0F traffic forms an acknowledged sequential transfer/state machine.

New locally proven XTR block:
`0x0410..0x0425` (count 22).

This block contains external candidate `0x041D` (1053), so the address exists locally in the XTR transfer family, but no semantic label is yet proven.

Next controlled discriminator:
ACK `0410/count22` in addition to the already-used exact known shapes; continue to refuse all unknown shapes and never answer FC03.


## EXP138 prepared discriminator

EXP137 established a locally observed acknowledged progression:
`03E8/count14 -> ACK -> 0410/count22`, after which the controller stalled on repeated `0410/count22` because no ACK was returned.

EXP138 changes only one variable:
acknowledge that exact `0410/count22` request.

Protocol question:
Does `0410/count22` ACK advance the XTR controller to:
- another FC16 transfer block; or
- the FC03 read-side phase seen in the genuine Thermia Online capture?

No newly appearing block will be ACKed in EXP138. FC03 will not be answered.


## Raw-frame correction: 0x0848 Heat Curve follow-up
The follow-up GitHub analysis of the genuine Online capture over-interpreted the `0x0848` block.

Exact decoded words:
- ~12.116 s, `0848/count23`: `0858=0000`, `0859=0004`, `085A=0014`, ...
- ~33.107 s, `0848/count23`: `0858=0015`, `0859=0004`, `085A=0014`, ...

Thus:
- `0858` changes `0 -> 21`;
- `085A` stays `20`;
- no same-register `20 -> 21` transition exists in those two `0848` frames.

The later `07E4` frame is a different block and cannot be used as a same-register revert without additional evidence.

Status:
- `0858` = STRONGLY INTERESTING / Heat-Curve-change correlation candidate.
- exact semantics = OPEN.
- do not encode `0858 = Heat Curve` yet.


## EXP138 — next 0x0F sequence stage proven

Local XTR sequence now proven:
`03E8/count14 -> ACK -> 0410/count22 -> ACK -> 042E/count15`.

Important persistence observation:
After EXP137 ended while the controller was waiting for an ACK to `0410/count22`, an ESP reboot and new firmware did not reset the controller-side transfer state. EXP138's passive baseline immediately contained repeated `0410/count22`. Therefore the sequence state is maintained by the Thermia/controller side, not by transient ESP state.

New local block:
`0x042E..0x043C` (count 15; decimal 1070..1084).

This aligns structurally with the external DHP/ATEC block family at decimal 1070..1084, but individual semantics are not imported as proven XTR mappings.

Next discriminator:
ACK only `042E/count15` as the one new variable; stop without answering the first new FC16 stage or FC03 read.


## EXP139 prepared discriminator — ACK 0x042E/count15

Locally proven progression before EXP139:
`03E8/14 -> ACK -> 0410/22 -> ACK -> 042E/15`.

EXP139 changes one variable only:
acknowledge `042E/count15`.

This block covers `0x042E..0x043C` (decimal 1070..1084). Structural agreement with the external DHP/ATEC 1070..1084 family is noted, but no individual semantic labels are imported.

Positive:
- first new FC16 stage after a successful 042E ACK, or
- first 0x0F FC03 request.

Neither will be answered in EXP139.


## EXP139 — 0x0F sequence extends through 0x04A6 to 0x04BA

Observed local XTR progression:
`042E/count15 -> ACK -> 04A6/count13 -> ACK -> 04BA/count22`.

Combined with prior experiments:
`03E8/14 -> ACK -> 0410/22 -> ACK -> 042E/15 -> ACK -> 04A6/13 -> ACK -> 04BA/22`.
