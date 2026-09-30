# 2026-09-30 — EXP349 COMPLETE / POSITIVE; reusable HA-selected room-setpoint writes proven in one retained DCM session

**Authoritative current state:** EXP349 is **COMPLETE / POSITIVE** from the supplied local XTR M log plus the user's direct confirmation that it worked perfectly. EXP348 and EXP347 are also **COMPLETE / POSITIVE**. EXP350 is **NOT YET PREPARED / NOT RUN**.

## Current experiment/result

### EXP349 — COMPLETE / POSITIVE

**Hypothesis:** the locally proven HA-selected `03F4` desired-page write can be reused repeatedly in one retained stage-40 Online/DCM session, with each new transaction built from the latest exact controller-republished `03E8/count14` page.

**Controlled change from EXP348:** remove the one-write-plus-rollback limitation and allow repeated guarded writes. After every exact controller republish, promote that page to the source cache for the next write and return to READY. The experimental budget remained bounded to eight semantic responses per ESP boot. No new page, register, selector encoding or runtime ACK shape was introduced.

### Observed facts

- EXP349 was entered from the retained EXP348 controller session after ESP OTA; no Thermia-controller reboot and no new R1/bootstrap were used.
- Retained runtime qualification was repeatedly observed from known FC16 service plus exact `0708/count6` idle service with:
  `W0..W5 = 0000 0000 0000 0000 0000 0006`.
- Before semantic writes, runtime health remained clean: no new challenge, unknown FC16/FC03, peer responder, parser resync or RX drop.
- First reusable write:
  - current `03F4=22`, requested `16`;
  - selector `0000 0001 0000 0001 0000 0006`;
  - desired page changed only `03F4: 22 -> 16`;
  - controller republished exact `03E8/count14`;
  - `WRITE_CONFIRMED writeNo=1 ... extraDeltaWords=0 ... NEXT_SOURCE=CONTROLLER_REPUBLISH ... READY_AGAIN=1`;
  - Home Assistant `Room Setpoint Mirror` and normal `Room Setpoint` reached 16 °C.
- Second reusable write:
  - current `03F4=16`, requested `24`;
  - exact same native selector/pull path;
  - controller republished exact page with `03F4=24`;
  - `WRITE_CONFIRMED writeNo=2 ... extraDeltaWords=0 ... READY_AGAIN=1`;
  - Home Assistant reflected 24 °C.
- Third reusable write:
  - current `03F4=24`, requested `22`;
  - controller republished exact page with `03F4=22`;
  - `WRITE_CONFIRMED writeNo=3 ... extraDeltaWords=0 ... READY_AGAIN=1`;
  - EXP349 status became `COMPLETE / POSITIVE / 3+ reusable writes confirmed / runtime continues`;
  - Home Assistant returned to 22 °C.
- User directly confirmed the sequence worked perfectly.
- The 10..30 °C protection is implemented both in the HA number limits and in the write lambda; out-of-range current or requested values are fail-closed. This limit is a locally observed native indoor-sensor/UI range, not a claimed universal protocol range.

## Strong conclusions

**PROVEN / locally confirmed:** on this XTR M, the native Online/DCM mailbox + desired-page path for mapped register `03F4` is reusable for multiple semantic setpoint writes inside one continuously retained stage-40 session. The exact controller republish from one successful write can be promoted to the source page for the next write.

**PROVEN / locally confirmed:** a single retained session successfully carried the tested chain `22 -> 16 -> 24 -> 22 °C`, with `extraDeltaWords=0` on all three controller confirmations and continued stage-40 runtime.

**PROVEN / locally confirmed:** changing the HA number alone does not transmit a semantic write; the explicit Apply action is required. Requested/current values outside 10..30 °C are refused by local implementation guards.

## Current protocol model

Locally proven integration chain now includes:
1. retained controller-side Online/DCM session surviving ESP OTA/reboot;
2. requalification without Thermia reboot or new R1;
3. persistent stage-40 runtime FC16 service;
4. idle `0708` mailbox with W5=0006 preserving DCM-connected presentation in the tested context;
5. W1 bit0 desired-page selector for `03E8`;
6. controller FC03 `03E8/count14` pull;
7. same-session desired page changing only mapped `03F4`;
8. exact controller FC16 republish confirming the requested setpoint;
9. promotion of that republish to the next-write source cache;
10. repeated semantic writes in the same session without rebootstrap.

W1 as low desired-page/PULL bitmap and W2:W3 as current-page/PUSH bitmap remain strongly supported. W0, W4 and the exact semantic meaning of W5 remain open. W5=0006 is proven only as sufficient for persistent DCM indication in the tested local context.

## Immediately preceding results

### EXP348 — COMPLETE / POSITIVE
HA-selected generic target was locally proven with `22 -> 24 -> 22 °C`. The controller confirmed both the write and explicit rollback with `extraDeltaWords=0`; Room Setpoint followed; retained runtime stayed clean. EXP348 remained intentionally one write plus one rollback.

### EXP347 — COMPLETE / POSITIVE
After ESP OTA/reboot, the existing controller-side stage-40 session was rejoined **without Thermia-controller reboot and without new R1/bootstrap**. Retained runtime qualification succeeded, then the guarded `03F4` write/rollback worked while the user confirmed the DCM icon stayed visible, no error appeared and the temperature changed/restored correctly.

## Next experiment

**EXP350 — NOT YET PREPARED / NOT RUN.**

Preferred controlled change: remove the manual experiment Arm button. After ESP boot/OTA, automatically enter passive retained-session qualification. Do not permit semantic writes until the same EXP349 clean-runtime requirements are satisfied. Keep only the explicit HA desired-setpoint control + Apply trigger for active semantic writes. Preserve all existing 10..30 guards, cache freshness, exact republish verification, fail-closed behavior and bounded write budget unless EXP350 explicitly tests a different one.

## Safety constraints

No broad writes, scans or unknown-value injection. Semantic control remains limited to locally mapped `03F4` inside `03E8/count14`, using the latest controller-originated/confirmed full page and changing one word only. Exact stage/function/start/count/session and runtime-health guards remain mandatory. Unexpected traffic is capture-only/fail-closed. An abnormal Online/Link state remains a stop condition; Thermia-controller reboot is recovery only if such an abnormal state actually occurs.

---

# 2026-09-30 — EXP346 COMPLETE / POSITIVE; guarded semantic write + rollback inside persistent DCM runtime

**Authoritative current state:** EXP346 is **COMPLETE / POSITIVE** from supplied local XTR M logs plus the user's direct Thermia-screen observation. EXP345 remains the proven persistent-connected baseline. EXP347 is **NOT YET PREPARED / NOT RUN**.

## Current experiment/result

### EXP346 — COMPLETE / POSITIVE

**Hypothesis:** the native desired-page write path proven in EXP343 can be executed inside the persistent EXP345 Online/DCM runtime without dropping the DCM-connected presentation.

**Controlled change from EXP345:** preserve the entire EXP345 fresh-session bootstrap, ordered initial sync, stage-40 runtime FC16 whitelist/ACK scheduler and idle 0708 W5=0006 behavior; add exactly one guarded 03E8/count14 desired-page write plus one explicit rollback using a same-session controller-originated page cache. No other settings words are intentionally changed.

### Observed facts

- Fresh session entered stage 40 normally and continued serving persistent runtime with idle mailbox:
  `W0..W5 = 0000 0000 0000 0000 0000 0006`.
- Initial same-session controller FC16 `03E8/count14` cached `03F4=22`.
- User armed one guarded write:
  `current03F4=22 -> target03F4=21`.
- On the next exact `0708/count6` request, emulator returned selector:
  `W0..W5 = 0000 0001 0000 0001 0000 0006`
  with frame `0F030C000000010000000100000006AD26`.
- Controller then issued exact `FC03 03E8/count14`.
- Emulator answered with the same-session 14-word page, changing only `03F4: 0016 -> 0015`:
  `0F031C0024001400280000000000000014001400020028001E000100150002C29F`.
- Controller republished exact `FC16 03E8/count14` with `03F4=0015`.
- EXP346 verification reported:
  `WRITE_CONFIRMED original03F4=22 target03F4=21 observed03F4=21 extraDeltaWords=0 semanticResponses=1 KEEP_W5_0006=1 CONTINUE_RUNTIME=1`.
- Home Assistant `Room Setpoint Mirror` and then normal `Room Setpoint` both reached 21 °C.
- User confirmed the DCM icon remained visible and no Online/Link error appeared.
- Explicit rollback was then armed while cached `03F4=21`.
- Emulator repeated the same native selector/pull flow and returned the same-session page with only `03F4: 0015 -> 0016`:
  `0F031C0024001400280000000000000014001400020028001E000100160002329F`.
- Controller republished exact `FC16 03E8/count14` with `03F4=0016`.
- EXP346 verification reported:
  `ROLLBACK_CONFIRMED original03F4=22 observed03F4=22 extraDeltaWords=0 semanticResponses=2 KEEP_W5_0006=1 CONTINUE_RUNTIME=1`.
- Home Assistant `Room Setpoint Mirror` and normal `Room Setpoint` returned to 22 °C.
- User again confirmed DCM icon still visible and no Online/Link error.

## Strong conclusion

**PROVEN / locally confirmed:** on this XTR M, a guarded native 03E8 desired-page semantic change can be applied and rolled back inside the long-lived stage-40 Online/DCM-emulation runtime while W5=0006 preserves the DCM-connected presentation. The controller itself republishes the changed page, and in EXP346 the only page-word delta on both write and rollback was 03F4.

This upgrades the local model from “semantic write works” (EXP343) plus “persistent connected runtime works” (EXP345) to **both functions working together in the same session**.

## Current protocol model

Locally proven integration chain now includes:
1. fresh challenge / accepted fixed-R1 entry;
2. ordered full initial FC16 sync;
3. persistent stage-40 runtime FC16 service;
4. idle 0708 mailbox with W5=0006 retaining DCM indication;
5. authentic W1 bit0 desired-page selector for 03E8;
6. controller-initiated FC03 03E8/count14 pull;
7. same-session cloned desired page with exactly one 03F4 delta;
8. controller FC16 republish confirming semantic application;
9. continued persistent runtime after the write;
10. second native transaction restoring the original 03F4 value;
11. continued DCM indication and no observed Online/Link error through write and rollback.

W1 as low desired-page/PULL bitmap and W2:W3 as current-page/PUSH bitmap remain strongly supported. W0, W4 and the exact semantic meaning of W5 remain open. W5=0006 is proven only as sufficient for DCM-indication persistence in the tested local context.

## Next experiment

**EXP347 — NOT YET PREPARED / NOT RUN.** Preferred target: test **reusability of the proven semantic path within one already-established persistent session** without a new controller reboot: one additional bounded user-requested 03F4 setpoint change, using the latest controller-originated same-session page as source, followed by exact controller republish verification and rollback. Exact target, freshness bound, write budget and abort criteria must be fixed before YAML generation.

## Safety constraints

No broad writes/scans or unknown-value injection. Semantic writes remain limited to locally mapped 03F4 using same-session controller data and one controlled word delta. Every write must be guarded by exact stage/function/start/count/CRC/session state; any unexpected traffic is capture-only/fail-closed. Preserve the persistent runtime baseline and Home Assistant production functionality. Controller reboot remains recovery for any abnormal Online/Link state.

---

# 2026-09-30 — EXP345 COMPLETE / POSITIVE; persistent DCM-connected baseline established

**Authoritative current state:** EXP345 is **COMPLETE / POSITIVE** from supplied local XTR M logs plus the user's direct Thermia-screen observation. EXP343 is also confirmed **COMPLETE / POSITIVE** from its original result log. EXP346 is **NOT YET PREPARED / NOT RUN**.

## Current proven integration chain

- **EXP343 — COMPLETE / POSITIVE:** authentic 0708 selector caused controller FC03 03E8/14; emulator returned the same-session page with only 03F4 changed 0016 -> 0015; about 690 ms later controller republished exactly that one-word change, and Room Setpoint Mirror / Room Setpoint reported 21 °C. This is local semantic application.
- **EXP344 — COMPLETE / NEGATIVE for persistent DCM-connected indication; POSITIVE transport sub-result:** persistent stage-40 runtime stayed clean >15 min with all-zero idle 0708 response, but the DCM icon was absent after the soak; no Online/Link error.
- **EXP345 — COMPLETE / POSITIVE:** same persistent runtime design, with only idle-0708 W5 changed 0000 -> 0006. At runtime age 900.5 s: runtimeFC16ACK=379, idle0708=210, unknown16=0, unknown03=0, peer17=0, peer16ack=0, resync=0, drops=0, DE=LOW. User confirmed DCM icon remained present and no COMM. ERR ONLINE/LINK.

## Controlled A/B result

    EXP344 W0..W5 = 0000 0000 0000 0000 0000 0000
    EXP345 W0..W5 = 0000 0000 0000 0000 0000 0006

All bootstrap, initial-sync, stage-40 runtime service and FC16 whitelist/ACK behavior were preserved. **Local conclusion:** W5=0006 is sufficient in this tested emulator/session context to retain the DCM-connected indication where W5=0000 did not. The semantic meaning of W5 remains **OPEN / UNKNOWN**.

## Current protocol model

Locally proven: fresh challenge/fixed-R1/full-sync path; persistent stage-40 Online runtime; interleaved 0708 mailbox service; authentic 03E8 PULL selection; semantic application of a same-session desired 03E8 page (EXP343); and >15-minute persistent DCM icon with W5=0006 (EXP345). W1 as low desired-page/PULL bitmap and W2:W3 as current-page/PUSH bitmap remain strongly supported. W0, W4 and exact W5 semantics remain open.

## Next experiment

**EXP346 — NOT YET PREPARED / NOT RUN.** Preferred target: preserve EXP345 as the persistent connected baseline and add one guarded native desired-page action using the already-proven EXP343 mechanism. Exact target/value, guard, rollback and stop criteria must be fixed before YAML generation.

## Safety constraints

No broad writes/scans or unknown-value injection. Any semantic write must use a locally mapped field, known current value, same-session page data and one controlled delta. Unexpected traffic remains capture-only/fail-closed. Preserve production/Home Assistant functionality; experimental controls remain under Configuration. Controller reboot remains recovery for an abnormal Online/Link state.

---
# 2026-09-30 — EXP340 COMPLETE / INCONCLUSIVE; 0708 offline reduction COMPLETE

**Authoritative current state:** EXP340 is **COMPLETE / INCONCLUSIVE** from the supplied local XTR M log. The intended 07F8 -> 0708-zero -> next-FC16 path was not executed because retained runtime had already advanced to 080C/18 before EXP340 could transmit. The offline reduction of the available genuine gateway/DCM captures is **COMPLETE**. EXP341 is the next target, but is **NOT YET PREPARED / NOT RUN**.

## Last completed live experiment — EXP340

**Status:** **COMPLETE / INCONCLUSIVE**.

EXP340 armed in a retained controller session after ESP OTA only. About 0.49 s after ARM the controller emitted exact slave-0x0F FC16 080C/count18:

    0F10080C00122400E40000000000000000000000160008001600E4000000DC00000000000000200000000011CE

No 07F8, no 0708 and no EXP340 TX occurred before that page. The experiment stopped fail-closed, with peer responder count 0, parser resync delta 0, RX-drop delta 0 and DE LOW.

**Interpretation:** this does not test the planned EXP340 mailbox hypothesis. It does add another local retained-session observation: controller runtime can continue across an ESP OTA reboot and can be found already at a later runtime page.

## Locally confirmed runtime evidence from EXP336–340

- EXP336: after ESP OTA only, retained 07D0/19 appeared about 0.53 s after ARM with zero experiment TX. Planned retained-0708 hypothesis was therefore not tested.
- EXP337: **COMPLETE / POSITIVE** — retained 07D0/19 ACK -> 07E4/17 ACK -> exact FC03 0708/count6, with no Thermia reboot, R1, new 085F ACK or mailbox response.
- EXP338: **COMPLETE / INCONCLUSIVE** — after ESP OTA, exact 07F8/17 appeared before the planned 0708 response; zero experiment TX.
- EXP339: **COMPLETE / INCONCLUSIVE** — exact retained 07F8/17 was ACKed once; about 1.57 s later exact FC03 0708/count6 appeared. No mailbox response was sent.
- EXP340: **COMPLETE / INCONCLUSIVE** — exact 080C/18 appeared before the expected retained 07F8; zero experiment TX.

These results support a runtime model in which FC16 runtime/export pages continue in controller-owned state while 0708 mailbox polls are interleaved. They do **not** prove that every page transition is independent of mailbox service.

## Full fresh-session chain now locally proven

EXP331–333 extended the fresh XTR chain beyond the previous EXP330 boundary. The locally observed ordered chain is now:

    fresh boot
    -> 071C/0730 challenge
    -> fixed captured R1 accepted
    -> 03E8/14 -> 03FC/11 -> 0410/22 -> 042E/15 -> 0442/13
    -> 0456/12 -> 046A/18 -> 047E/19 -> 0492/11 -> 04A6/13
    -> 04BA/22 -> 04D8/27 -> 04F6/14 -> 050A/19 -> 051E/10
    -> 0532/18 -> 0546/20
    -> 055A/33 -> 057B/33 -> 059C/33 -> 05BD/33 -> 05DE/33 -> 05FF/33
    -> 0620/33 -> 0641/33 -> 0662/33 -> 0683/33 -> 06A4/33 -> 06C5/33
    -> 06EA/7 -> 06F1/3 -> 06F4/19

EXP333 then observed post-tail 085F/5 and FC03 0708/count6. The page sequence is locally confirmed; page semantics remain separate questions.

## Offline 0708 mailbox reduction — genuine gateway/DCM evidence

An offline parser reduction over the six available genuine gateway/DCM capture files found 327 FC03 0708/count6 requests, 302 with a paired six-word response suitable for reduction.

Best current six-word model:

    W0 W1 W2 W3 W4 W5

- **W1: STRONGLY SUPPORTED** as the low 16-bit gateway->controller desired-page/PULL bitmap.
- **W2:W3: STRONGLY SUPPORTED** as a 32-bit controller->gateway current-page/PUSH or refresh bitmap.
- **W0: HYPOTHESIS** as a possible high half of the PULL bitmap; it was zero in all 302 paired responses, so this is not demonstrated.
- **W4/W5: OPEN / UNKNOWN** lifecycle, status, capability or session fields. Do not port literal values between models without evidence.

### W2:W3 page-selection map from genuine captures

    bit  0 = 03E8    bit 16 = 0546
    bit  1 = 03FC    bit 17 = 055A
    bit  2 = 0410    bit 18 = 057B
    bit  3 = 042E    bit 19 = 059C
    bit  4 = 0442    bit 20 = 05BD
    bit  5 = 0456    bit 21 = 05DE
    bit  6 = 046A    bit 22 = 05FF
    bit  7 = 047E    bit 23 = 0620
    bit  8 = 0492    bit 24 = 0641
    bit  9 = 04A6    bit 25 = 0662
    bit 10 = 04BA    bit 26 = 0683
    bit 11 = 04D8    bit 27 = 06A4
    bit 12 = 04F6    bit 28 = 06C5
    bit 13 = 050A    bit 29 = 06EA
    bit 14 = 051E    bit 30 = 06F1
    bit 15 = 0532    bit 31 = 06F4

Examples include genuine 4000:8000 selecting 06F1 and 0532, FFFF:867F selecting the corresponding 26 configuration pages, and ATEC 7FFF:FFFF selecting the first 31 pages through 06F1.

### Genuine desired-page PULL/write-path evidence

- W1 bit0 (0001) is followed by controller FC03 03E8 reads.
- W1 bit3 (0008) is followed by controller FC03 042E reads.
- In Eco5 write-roundtrips, the gateway returns a desired page to that FC03 read and the controller subsequently republishes the accepted page by FC16.
- For 03E8/14, one captured roundtrip changes only 03F4 from 0014 to 001E; a later roundtrip restores 001E to 0014. 03F4 is independently locally confirmed on the XTR as the room-setpoint mirror.
- For 042E/15, captured desired-page pulls alter 042F and later 042E one field at a time, followed by matching controller FC16 publication. Exact XTR semantics of those fields are not imported from the other model.

**Strong architectural conclusion:** genuine Online/DCM traffic behaves like a bidirectional page cache: controller current state is exported to the gateway via FC16, while pending desired pages are advertised through the 0708 mailbox and pulled by controller-initiated FC03 reads. This is cross-model genuine gateway/DCM evidence until the PULL path is locally reproduced on the XTR M.

## Next experiment target — EXP341

**Status:** **NOT YET PREPARED / NOT RUN**.

Target hypothesis: locally reproduce the genuine desired-page PULL path without changing any setting. The safest design is a bounded no-op 03E8/14 test: first cache a current controller-originated 03E8/14 page, then at an exact 0708 request advertise only the authentic PULL selector needed for 03E8, answer the resulting controller FC03 03E8/14 with an exact clone of the cached current values, and capture whether the controller accepts/republishes the page.

No EXP341 frame should be finalized until the exact 0708 envelope and stop/recovery behavior are fixed. Success must be transport proof only; no semantic value change is required.

## Safety constraints

- No broad register writes, scans or unknown-value injection.
- FC16 ACKs remain address/count acknowledgements only.
- For EXP341, any FC03 data response must be an exact current-value clone captured from the same local XTR session.
- Fail closed on wrong page, wrong count, stale cache, parser/RX integrity change, peer responder evidence or unexpected session restart.
- Preserve production/Home Assistant functionality and keep experimental controls under Configuration.

---
# 2026-09-30 — EXP330 COMPLETE / POSITIVE; EXP331 PREPARED / NOT RUN

**Authoritative current state:** EXP330 is **COMPLETE / POSITIVE** from the supplied local XTR M log. EXP331 is **PREPARED / NOT RUN**. No result for EXP331 has been supplied yet.

## Current experiment — EXP331

**Status:** **PREPARED / NOT RUN**

**Hypothesis:** after reproducing the now locally confirmed fresh-session prefix through `0492/11 ACK -> 04A6/13`, a bounded eight-block continuation matching genuine Eco 5 / earlier local research will advance:

`04A6/13 -> 04BA/22 -> 04D8/27 -> 04F6/14 -> 050A/19 -> 051E/10 -> 0532/18 -> 0546/20 -> 055A/33`

**Controlled change from EXP330:** preserve the complete proven prefix and, instead of stopping at `04A6/13`, ACK exactly the eight listed FC16 pages once each. After the `0546/20` ACK, all traffic is capture-only. No `055A` ACK, no FC03/mailbox response, no 0x06 response, and no semantic register-value write.

**Safety:** the added transmissions are standard FC16 address/count ACKs only; each stage is exact-shape, ordered, timed and fail-closed. Maximum active experiment TX is one fixed R1 plus 17 FC16 ACKs. Recovery remains: abort, verify DE LOW, reboot the Thermia controller if the deliberately incomplete Online session produces an alarm.

## Last completed experiment — EXP330

**Status:** **COMPLETE / POSITIVE**

EXP330 reproduced the complete locally proven fresh-session prefix and then tested the new bounded continuation:

`046A/18 -> ACK -> 047E/19 -> ACK -> 0492/11 -> ACK -> 04A6/13`

Observed:
- exact `046A/count18` accepted its standard ACK;
- exact `047E/count19` followed and accepted its standard ACK;
- exact `0492/count11` followed and accepted its standard ACK;
- exact `04A6/count13` then appeared as the first predicted next stage, approximately 571 ms after the `0492` ACK;
- no ACK was sent to `04A6`;
- no post-R1 challenge retry, no external FC17 responder, no external FC16 ACK, parser resync delta 0, RX-drop delta 0, DE LOW.

## Fresh-session findings added by EXP323–330

- **EXP323 — COMPLETE / INCONCLUSIVE:** one standard ACK to the second qualified all-zero `085F/5` did not establish the fresh Online path; after the ACK, only `04A6/13` remained visible during the bounded observation.
- **EXP324 — COMPLETE / INCONCLUSIVE:** ESP OTA reboot without controller reboot did not recreate the all-zero `085F` qualification state; only `04A6/13` appeared. This reinforced that controller-side state persists across ESP reboot.
- **EXP325 — COMPLETE / POSITIVE:** after a true controller reboot, one fixed previously captured R1 response to the first exact fresh `071C/0730` FC17 challenge, under the observed fresh guard `A80E=0000 / A80F=0005`, caused `03E8/count14` to appear about 120 ms later. No 0x06 emulation, 04A6/085F ACK, FC16 ACK or mailbox response was required before `03E8`.
- **EXP326 — COMPLETE / POSITIVE:** one standard ACK to exact `03E8/count14` advanced the controller to exact `03FC/count11`.
- **EXP327 — COMPLETE / POSITIVE:** one standard ACK to exact `03FC/count11` advanced the controller to exact `0410/count22`.
- **EXP328 — COMPLETE / POSITIVE:** one standard ACK to exact `0410/count22` advanced the controller to exact `042E/count15`.
- **EXP329 — COMPLETE / POSITIVE:** one bounded run locally confirmed `042E/15 ACK -> 0442/13 ACK -> 0456/12 ACK -> 046A/18`.
- **EXP330 — COMPLETE / POSITIVE:** one bounded run locally confirmed `046A/18 ACK -> 047E/19 ACK -> 0492/11 ACK -> 04A6/13`.

## Current locally proven fresh-session prefix

`fresh controller boot`
`-> exact 071C/0730 challenge`
`-> fixed previously accepted R1`
`-> 03E8/14 ACK`
`-> 03FC/11 ACK`
`-> 0410/22 ACK`
`-> 042E/15 ACK`
`-> 0442/13 ACK`
`-> 0456/12 ACK`
`-> 046A/18 ACK`
`-> 047E/19 ACK`
`-> 0492/11 ACK`
`-> 04A6/13`

This is **PROVEN / locally confirmed for the tested XTR M context**. It does not prove the semantic meaning of the exported blocks.

## Current protocol model

There are two locally demonstrated families of Online/DCM behavior:

1. **Fresh-session approval + ordered initial sync:** fresh controller state exposes `071C/0730`; one fixed captured R1 can be accepted even when the live challenge differs from the challenge that originally produced that R1. The controller then advances through an ACK-driven FC16 initial-sync chain.
2. **Retained-session/runtime recovery:** previously proven retained branches can rejoin the steady runtime scheduler without repeating fresh approval.

The fresh prefix through `04A6/13` is now independently re-confirmed by EXP325–330. Standard FC16 ACKs are causal state-machine acknowledgements in this chain; they acknowledge address/count and do not inject the controller-exported values.

## Strong conclusions

- The fresh `071C/0730` FC17 exchange is a major session-entry gate on this XTR M.
- Strict per-live-challenge uniqueness is not required for acceptance in the tested case: fixed R1 replay was accepted against a different live challenge.
- Do **not** generalize that into “arbitrary responses work” or “there is no authentication”; those remain unproven.
- The fresh initial sync is an ordered, ACK-driven FC16 state machine at least through `0492/11 -> 04A6/13`.
- `04A6/13` is context-sensitive: it occurs as the predicted post-`0492` initialization stage and also as recurrent sparse/runtime traffic in other contexts. ACK policy must therefore remain state-specific.

## Important unknowns

- Exact algorithm / security semantics / lifetime scope of the `071C/0730` response.
- Whether the fixed R1 remains acceptable across firmware changes or other XTR units.
- Semantic meaning of the individual initial-sync blocks.
- Exact boundary where initial sync hands over to mailbox/startup/runtime.
- Whether the EXP331 continuation reaches `055A/33` cleanly in this current run.
- Exact `04A6` payload semantics across initialization, sparse passive and runtime contexts.
- Multi-hour production stability and rare/fault branches remain separate validation work.

## Safety constraints

- Exact slave/function/start/count/bytecount/length/CRC and state guards remain mandatory.
- No broad ACKing of unknown FC16 traffic.
- Unexpected traffic is capture-only / fail-closed.
- No semantic write is authorized by EXP331.
- 0x06 accessory emulation remains outside this fresh-session experiment.
- ESP reboot is not controller-state rollback.
- Controller reboot remains the known way to obtain a controlled fresh-session state when required.

---

# 2026-09-30 — EXP322 COMPLETE / POSITIVE passive clean-reboot baseline; EXP323 next / NOT YET PREPARED

**Authoritative current state:** EXP322 is **COMPLETE / POSITIVE** as a passive baseline from the supplied local log. EXP321 is **COMPLETE / INCONCLUSIVE**. The Thermia controller was manually rebooted by the user between EXP321 and EXP322 to clear the visible errors. EXP323 is the next proposed experiment and is **NOT YET PREPARED / NOT RUN**.

## Current experiment

**EXP323 — NOT YET PREPARED / NOT RUN.**

Planned hypothesis: in the current clean post-controller-reboot state, one conservatively qualified standard ACK to exact all-zero `085F/5` can advance the native scheduler to its next state.

Planned controlled change from EXP322:
- wait for two exact all-zero `085F/5` requests;
- first is qualification / NO_TX;
- second receives exactly one already-proven standard ACK `0F 10 08 5F 00 05 33 56`;
- `04A6/13` remains capture-only / NO_TX;
- after the one `085F` ACK, all traffic is capture-only and the first subsequent relevant non-`04A6` slave-`0x0F` frame is recorded before fail-close;
- no semantic register values are injected.

## Last completed experiment — EXP322

**Status:** **COMPLETE / POSITIVE** as a passive clean-reboot baseline.

After EXP321, the user rebooted the Thermia controller to clear the visible Online/Link errors. EXP322 then observed the resulting state for 90 s with strict TX=0.

Final census:
- total slave-`0x0F` frames: 125;
- FC16: 125;
- FC03: 0;
- `04A6/13`: 83;
- `04A6` payload changes: 0;
- `085F/5`: 42;
- all 42 `085F` frames were exact all-zero payload;
- `085F(0800)`: 0;
- `0708`: 0;
- `07D0, 07E4, 07F8, 080C, 0820, 0834, 0848, 0864, 0870, 0884`: all 0;
- other slave-`0x0F`: 0;
- parser resync delta: 0;
- RX-drop delta: 0;
- TX=0 and DE LOW.

The clean state therefore emitted a stable approximate 2:1 pattern of sparse `04A6/13` to all-zero `085F/5`, with no normal runtime progression because the emulator intentionally sent nothing.

The EXP322 `04A6` payload remained invariant:
`0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 4020 0000 0000`.

## EXP321 — COMPLETE / INCONCLUSIVE

EXP321 was intended as a 3-minute recovery-to-runtime integration test. Before the controller reboot it never reached its intended `085F(0800)` entry condition.

Observed over the 120 s qualification window:
- TX=0;
- approximately 111 x `04A6/13`;
- no `085F(0800)`;
- no all-zero `085F`;
- no handoff or runtime loops;
- unexpected=0;
- parser resync delta=0;
- RX-drop delta=0;
- DE LOW.

This is not a negative result for the previously proven retained-recovery chain; the required entry state was not present.

## EXP318–320 retained recovery result

- **EXP318 — COMPLETE / POSITIVE:** two exact `085F(0800)` requests were qualified; one standard `085F/5` ACK was sent; 2.196 s later the first non-`04A6` frame was exact all-zero `085F/5`.
- **EXP319 — COMPLETE / POSITIVE:** after qualifying and ACKing `085F(0800)`, exact all-zero `085F/5` was qualified and ACKed; 2.381 s later the first non-`04A6` frame was `0884/60`.
- **EXP320 — COMPLETE / POSITIVE:** the same prerequisites were reconstructed; `0884/60` was qualified and ACKed; 4.328 s later the first non-`04A6` frame was direct `07D0/19`.

This locally confirms the retained-session branch, in the tested context:

`085F(0800) --ACK--> all-zero 085F --ACK--> 0884/60 --ACK--> 07D0/19`.

EXP312 had previously observed `0884 ACK -> 0708 (NO_TX) -> 07D0`; EXP320 proves that `0708` is not mandatory as the immediate post-`0884` event in every retained context.

## Current protocol model

The native Online/DCM path remains an event/state graph with both fresh-session and retained-session behavior.

Confirmed retained branch:
`085F(0800) -> ACK -> all-zero 085F -> ACK -> 0884 -> ACK -> 07D0`.

Clean post-controller-reboot passive state now adds:
`sparse 04A6/13 <-> all-zero 085F/5` repeated with no emulator TX.

The current `04A6` interpretation must remain payload/context sensitive:
- genuine XTR/DCM configuration captures show the real DCM ACKing `04A6/13` with standard ACK `0F 10 04 A6 00 0D E1 F1`;
- those genuine captures include a richer `04A6` payload such as `0000 0003 0004 0002 003F 0050 003C 0002 0000 003C 000F 001E 0000`;
- EXP322's clean local passive state repeatedly emits a different sparse payload ending in `4020 0000 0000`;
- therefore genuine ACK behavior for the rich configuration payload must not yet be generalized to the current sparse `04A6` state.

## Locally proven findings added by EXP318–322

- Exact `085F/5` with `0861=0x0800` can be advanced by its standard FC16 ACK to exact all-zero `085F/5`.
- Exact all-zero `085F/5` can be ACK-gated into a scheduler branch that may lead directly to `0884/60`.
- Qualified `0884/60` can be ACKed into direct `07D0/19` without an intervening `0708` in at least one retained context.
- After a controller reboot, with no emulator TX, this XTR M can repeatedly emit sparse `04A6/13` plus all-zero `085F/5` while no normal runtime pages appear.
- The presence of repeated `04A6/13` alone is therefore not a reliable discriminator for the visible alarm state.
- The reappearance of all-zero `085F/5` after the controller reboot is a concrete state difference from EXP321.

## Strongest current hypotheses

- In the clean post-reboot state, ACKing a conservatively qualified all-zero `085F/5` may be the lowest-risk way to reveal the next native scheduler state.
- If the next state is `0708/6` or a known configuration/runtime node, one or two additional bounded experiments may be enough to reconnect this clean-start path to the already-proven runtime responder.
- The sparse `04A6` state may be part of an initialization/configuration retry loop, but its exact semantics and whether it should be ACKed locally remain open.

## Important unknowns

- What exact event follows one qualified all-zero `085F` ACK in the current clean post-reboot state.
- Whether the sparse `04A6` payload should receive the same ACK policy as the richer genuine configuration payload.
- Exact semantics of sparse versus rich `04A6/13`.
- Exact semantics of `0861=0x0800`.
- Long-duration stability after clean-start recovery reconnects to normal runtime.
- Exact `0708` latching/scheduling semantics.
- Genuine `071C/0730` challenge-response algorithm.

## Safety constraints

- Exact slave/function/address/count/bytecount/CRC and state guards remain mandatory.
- Do not broad-ACK unknown FC16 traffic.
- `0834/18` remains unsupported/capture-only.
- EXP323 must leave `04A6/13` NO_TX.
- Any post-target traffic in EXP323 is capture-only.
- ESP reboot/OTA is not controller rollback.
- A standard FC16 ACK carries address/count only and does not inject controller-originated register values.
- Unexpected traffic or parser/RX integrity changes remain fail-closed.
- Controller reboot remains the known fresh-state recovery procedure when required.

---

# 2026-09-30 — EXP315 COMPLETE / POSITIVE — retained runtime takeover sustained for 126 s / 6 loops; EXP316 next / NOT YET PREPARED

**Authoritative current state:** EXP315 is **COMPLETE / POSITIVE** from the supplied local log. EXP313 and EXP314 were intermediate retained-runtime handoff experiments. No later experiment has been run. EXP316 is the next candidate and is **NOT YET PREPARED / NOT RUN**.

## Last completed experiment — EXP315

**Hypothesis:** if the controller is retained at the already locally proven normal-runtime node `07E4/count17`, then a qualified standard `07E4` ACK can be used as a direct handoff into the established EXP296/297 steady-runtime responder.

### Baseline and exact controlled change

Baseline was EXP314 COMPLETE / INCONCLUSIVE. EXP314 observed exact `07E4/17` as the first relevant `0x0F` frame on each arm and correctly failed closed with TX=0 because its handoff model still required `07D0` or the inherited post-`07D0` `0708` boundary.

EXP315 changed only one context authorization:
- during retained stage 1, exact `07E4/count17` became a possible handoff node;
- qualification required at least two live exact `07E4/17` requests before any EXP315 TX;
- the second qualified request received the already-proven standard ACK `0F 10 07 E4 00 11 40 68`;
- after that, the existing proven post-`07E4` runtime graph was used unchanged;
- no new register/page, payload value or semantic write was introduced.

### EXP315 observed result

- Initial traffic included one `0708/6` capture-only request.
- Exact `07E4/17` then repeated twice.
- On the second `07E4`, EXP315 sent exactly one standard ACK and entered steady runtime.
- The runtime continued through the established sequence with evidence-backed `0708` responses and FC16 ACKs.
- The controller completed **6 full returned runtime loops**.
- Steady runtime reached **126.401 s** before the success boundary.
- At the final returned `07D0/19`, EXP315 intentionally stopped before ACKing that boundary.
- Final stop summary: `TX=84`, `events=84`, `r0708=30`, `unexpected=0`, `resync=0`, `drops=0`, `DE=LOW`.
- Firmware final status: `POSITIVE / retained recovery sustained proven steady runtime`.

**Result:** **COMPLETE / POSITIVE.**

## EXP313–315 retained-runtime handoff progression

- **EXP313 — COMPLETE / INCONCLUSIVE:** controller was already at `07D0/19`; one known ACK successfully initiated handoff, but ~1.39 s later `0708/6` appeared before `07E4/17`. The state machine did not yet allow that branch and failed closed. No sustained-runtime claim.
- **EXP314 — COMPLETE / INCONCLUSIVE:** after ESP restart, the controller had retained progress further into the scheduler and repeatedly presented `07E4/17` as the first relevant frame. EXP314 correctly failed closed with TX=0 because direct `07E4` entry was not yet authorized. The user's accidental "Error gone" click is invalid for alarm analysis and is not used as protocol evidence.
- **EXP315 — COMPLETE / POSITIVE:** repeated retained `07E4/17` was qualified; one already-proven `07E4` ACK joined the established runtime. The emulator then sustained 6 complete loops for 126.401 s with no unexpected session events, parser resyncs or RX drops.

## Current protocol model

The native Online/DCM integration is now best modeled as a **state/event graph with direct retained-runtime re-entry**, not as a cold-start-only sequence.

Fresh-session path remains:

`071C/0730 -> R1 -> config sync -> startup -> normal runtime`

Retained-session path can use recovery nodes when necessary:

`0662 / 085F(0800) / all-zero 085F -> branch-aware recovery -> known runtime node`

But EXP315 additionally proves a simpler path when the controller is already retained inside the normal scheduler:

`observe current known runtime node -> qualify -> send already-proven response -> join steady runtime`

Locally proven steady-runtime nodes remain:
`07D0, 07E4, 07F8, 080C, 0820, 0848, 085F, 0864, 0870, 0884`

with `0708` appearing at evidence-backed scheduler positions and using the known fixed runtime response where already proven.

## Locally proven findings added by EXP313–315

- The controller can retain its Online/DCM scheduler position across ESP reboot/OTA.
- Direct retained takeover at `07D0/19` is technically possible, but the immediate next scheduler event can include `0708` before `07E4`.
- The controller can progress further to `07E4/17` while the ESP remains offline/restarts.
- A qualified standard ACK to retained `07E4/17` can join the existing EXP296/297 steady-state runtime.
- After that handoff, the local XTR M can sustain at least **126.401 s and 6 complete loops** under the current emulator logic.
- Sustained steady runtime did not require any retained-recovery ACK in this run; direct known-node takeover was sufficient.
- The production architecture should therefore first classify the observed current `0x0F` state and directly join at a known runtime node when safe, falling back to adaptive recovery only when needed.

## Strongest current hypotheses

- Known-node retained takeover can be generalized to additional already-proven runtime nodes, provided qualification is conservative and node-specific next-event sets are preserved.
- Durable Online/Link health likely depends on sustained service of the runtime scheduler rather than any single special recovery ACK.
- A production-quality emulator should combine fresh-session startup, controller-reboot recovery, retained-runtime known-node takeover and adaptive retained recovery in one state machine.

## Important unknowns

- Multi-hour / overnight stability across compressor, DHW, defrost, SG and fault-state transitions.
- Which normal runtime nodes are safe direct retained-entry anchors besides locally proven `07E4` and the partial `07D0` handoff.
- Exact semantics of `0861=0x0800`.
- Exact long-term role and response cadence of `0708`.
- Runtime `04A6/13` semantics and native ACK policy.
- Genuine `071C/0730` challenge-response algorithm.
- Rare scheduler branches and fault/recovery behavior.

## Next experiment candidate — EXP316

**EXP316 — NOT YET PREPARED / NOT RUN.**

Highest-value next step is no longer another single ACK target. It should be a production/recovery-hardening integration test: reboot only the ESP at controlled points while the Thermia controller remains powered, classify whichever already-known runtime/recovery node is current, and verify that one combined state machine can safely rejoin steady runtime and remain healthy for multiple loops.

No new register target or semantic write should be introduced in EXP316.

## Safety constraints

- Exact slave/function/address/count/bytecount/CRC and state guards remain mandatory.
- Do not broad-ACK unknown FC16 traffic.
- `0834/18` remains unsupported/capture-only.
- Runtime `04A6/13` remains capture-only unless separately tested.
- Unexpected `0x0F` traffic remains capture-only/fail-closed.
- ESP reboot/OTA is never assumed to roll back controller state.
- Alarm marker buttons are observational only and must not be treated as protocol evidence unless intentionally pressed while the display state is actually checked.

---

# 2026-09-29 — EXP312 COMPLETE / POSITIVE — retained-session recovery now reaches 07D0; EXP313 NEXT / NOT YET PREPARED

**Authoritative current state:** EXP312 is COMPLETE / POSITIVE from the supplied local log. No later experiment has been run. EXP313 is a candidate next experiment and is **NOT YET PREPARED / NOT RUN**.

## Last completed experiment — EXP312

**Hypothesis:** a single standard FC16 address/count ACK to a qualified live `0884/60` retry stage is sufficient to move the retained controller session to the next known runtime stage.

### Baseline and controlled change

Baseline was EXP311, which showed that the post-`085F` scheduler is branch-based: `0884/60` can appear directly without preceding `0864/4` or `0870/17`.

EXP312 changed only the qualification/state-machine logic so that a direct live `0884/60` branch was accepted. The only new protocol action was one human-gated standard ACK to `0884/60`:

- target: slave `0x0F`, FC16, start `0x0884`, count `60` (`0x0884..0x08BF`);
- ACK: `0F 10 08 84 00 3C 83 7F`;
- no register values were injected;
- post-target traffic was strict NO_TX.

The already locally proven prerequisite actions remained automatic and exact-shape gated.

### EXP312 observed result

The controller first repeated `085F/5` with words `0000 0000 0800 0000 0000`. After two observations, one standard `085F/5` ACK was sent. The controller then moved to all-zero `085F/5`; after the existing qualification rule, one standard ACK was sent there as well.

The next runtime branch was:

`all-zero 085F ACK -> 0708 (NO_TX) -> repeated 0884/60`

No `0864/4` or `0870/17` occurred in this run. `0884/60` was qualified from repeated frames plus a fresh `0708`. After human arm, exactly one `0884/60` ACK was sent.

The post-target sequence was:

`0884 ACK -> 0708 (NO_TX) -> 07D0/19`

Timing in the supplied log:
- target `0884` ACK at approximately 01:36:30.415;
- post-ACK `0708` approximately 1.325 s later;
- `07D0/19` approximately 1.947 s after the target ACK.

No `0884` retry occurred before `07D0`. Final counters included `postRetry=0`, `post0708=1`, `postKnown=1`, parser resync delta 0, RX drops 0 and DE LOW at fail-close.

**Result:** **COMPLETE / POSITIVE.**

## Recent retained-session experiment chain — EXP298–312

- **EXP298 — COMPLETE / INCONCLUSIVE:** fresh-approval-only ESP reboot recovery was insufficient; no fresh `071C/0730` was observed in the supplied ~235.7 s window. Retained-session traffic continued and COMM. ERR ONLINE/LINK was visible.
- **EXP299 — COMPLETE / INCONCLUSIVE:** one bounded retained-session resync reached `0848 ACK -> 0708 -> all-zero 085F`, but did not establish durable health. Alarm clearing was temporary/correlative only.
- **EXP300 — COMPLETE / INCONCLUSIVE:** waiting for `0848` as a universal retained re-entry anchor failed; the current state could instead present `085F(0800)` or `0708`.
- **EXP301 — COMPLETE / NEGATIVE:** passive observation showed a persistent `0708 <-> 085F(0800)` retry loop with no `0848`.
- **EXP302 — COMPLETE / POSITIVE:** one standard ACK to exact `085F(0800)` changed the controller to all-zero `085F`; this locally proves that `0861=0x0800` is ACK-sensitive session/retry state, while its semantic meaning remains unknown.
- **EXP303 — COMPLETE / INCONCLUSIVE:** the desired `0800 -> zero` reproduction could not be tested because retained controller state had already changed; ESP reboot did not restore the previous controller state.
- **EXP304 — COMPLETE / INCONCLUSIVE:** exact `0662/33` resurfaced before the intended target and the experiment correctly stopped fail-closed.
- **EXP305 — COMPLETE / POSITIVE:** standard ACK of repeated `0662/33` stopped that retry stage and was followed by `085F(0800)`, `0708` and then all-zero `085F`; this re-confirms the older EXP141 `0662/33` ACK-gated transfer finding.
- **EXP306 — COMPLETE / INCONCLUSIVE:** with NO_TX, the controller persisted in `0708 <-> 085F(0800)`; the all-zero target was never reached.
- **EXP307 — COMPLETE / POSITIVE:** after the proven `085F(0800)` normalization, one ACK to qualified all-zero `085F/5` caused `0708 -> 0864/4`.
- **EXP308 — COMPLETE / POSITIVE:** one ACK to qualified `0864/4` caused `0708 -> 0870/17`.
- **EXP309 — COMPLETE / INCONCLUSIVE:** after the proven all-zero `085F` prerequisite, `0870/17` appeared directly with no `0864`; this disproved the experiment's too-linear prerequisite model.
- **EXP310 — COMPLETE / POSITIVE:** one ACK to live repeated `0870/17` caused `0708 -> 0884/60`.
- **EXP311 — COMPLETE / INCONCLUSIVE:** `0884/60` appeared directly after the all-zero `085F` ACK, without `0864` or `0870`; no `0884` ACK was sent because the state machine failed closed on the newly observed direct branch.
- **EXP312 — COMPLETE / POSITIVE:** one ACK to qualified `0884/60` caused `0708 -> 07D0/19` while the `0708` itself remained NO_TX.

## Current protocol model

The native Online/DCM runtime must be modeled as an **event/state-driven scheduler with optional branches**, not a rigid linear sequence.

The older stable runtime graph remains valid as a set of known stages:

`07D0 -> 07E4 -> [optional 0708] -> 07F8 -> 080C -> [optional 0708] -> 0820 -> 0848 -> ... -> 0864 / 0870 / 0884 -> [optional 0708] -> 07D0`

The retained-session experiments add a locally confirmed recovery view:

`0662/33 --ACK--> retained scheduler`

`085F(0800) --ACK--> all-zero 085F`

`all-zero 085F --ACK--> scheduler branch`

From that post-`085F` branch, locally observed valid paths now include at least:
- `0708 -> 0864`;
- direct `0870`;
- `0708 -> 0870`;
- direct `0884`;
- `0708 -> 0884`.

Locally tested causal target transitions include:
- `all-zero 085F ACK -> 0708 -> 0864` (EXP307);
- `0864 ACK -> 0708 -> 0870` (EXP308);
- `0870 ACK -> 0708 -> 0884` (EXP310);
- `0884 ACK -> 0708 -> 07D0` (EXP312).

The post-target `0708` frames in EXP307/308/310/312 were deliberately left NO_TX where applicable, yet the next FC16 runtime stage still appeared. This proves that an immediate `0708` response is not required for those short scheduler transitions. It does **not** prove that `0708` can be ignored for durable session health.

## Locally proven findings added by EXP298–312

- `0662/33` is an ACK-gated controller-to-DCM transfer stage on this XTR M.
- Exact `085F/5` with register `0861=0x0800` is an ACK-sensitive retained-session/retry state; semantics remain OPEN.
- Exact all-zero `085F/5` is also an ACK-gated retained-session stage in the tested recovery path.
- `0864/4`, `0870/17` and `0884/60` each accept the standard FC16 address/count ACK and can advance the local controller to another known runtime stage.
- `0884/60` can occur directly after the all-zero `085F` stage; neither `0864` nor `0870` is mandatory before it.
- `0884` payload values are runtime data and can change between repeated frames while start/count remain the same.
- Controller retained state can survive ESP reboot/OTA; ESP restart is not a rollback mechanism.

## Strongest current hypotheses

- The controller applies a liveness/watchdog model to the DCM session: isolated ACKs can temporarily progress or clear an alarm state, but sustained service of the scheduler is needed for durable Online/Link health.
- `0708` is a synchronization/mailbox descriptor whose immediate response may be optional for short FC16 scheduler progression but may still matter to durable session liveness or reverse-page signaling.
- Retained recovery can likely be converted into full steady-state service by joining the proven recovery branch back into the already proven EXP296/297 runtime responder at `07D0` or another recognized runtime node.

## Important unknowns

- Exact semantic meaning of `0861=0x0800`.
- Exact liveness/watchdog interval and minimum set of runtime events that must be serviced.
- Whether full branch-aware retained recovery can return to and sustain the EXP296/297 steady-state runtime without a controller reboot.
- Exact `0708` latching/scheduling semantics and whether/when a response is required for long-term health.
- Exact semantics of runtime pages `0864`, `0870`, `0884` and the dynamic `0884` payload fields.
- Runtime `04A6/13` semantics and native ACK policy.
- Genuine `071C/0730` challenge-response algorithm.
- Multi-hour/overnight stability and rare/fault-state behavior.

## Next experiment candidate — EXP313

**EXP313 — NOT YET PREPARED / NOT RUN.**

Highest-value next hypothesis: after branch-aware retained-session recovery reaches a known normal runtime node such as `07D0/19`, hand over to the already locally proven EXP296/297 steady-state runtime responder and determine whether the session remains healthy for multiple complete cycles without a Thermia-controller reboot.

This should introduce no new register target or semantic write. The new variable is sustained hand-off from retained recovery into the proven full runtime service. Runtime `04A6/13` should remain capture-only unless explicitly separated into its own later experiment.

## Safety constraints

- Exact slave/function/start/count/bytecount/CRC and state guards remain mandatory.
- Do not treat ESP reboot/OTA as controller-state rollback.
- Do not broad-ACK unknown FC16 traffic.
- `0834/18` remains unsupported/capture-only.
- Runtime `04A6/13` remains capture-only unless a dedicated experiment explicitly changes that.
- No semantic settings write is part of retained-recovery testing.
- Unexpected relevant `0x0F` traffic remains capture-only/fail-closed unless it is a predeclared locally proven branch.
- Recovery after an unexpected retained-state transition is TX-off/passive observation; a normal controller reboot remains the known way to force a fresh session when required.

---

# 2026-09-29 — EXP297 COMPLETE / POSITIVE — controller-reboot recovery locally proven; EXP298 PREPARED / NOT RUN

**Authoritative current state:** EXP297 COMPLETE / POSITIVE from supplied local log. EXP298 is PREPARED / NOT RUN.

## Last completed experiment — EXP297
**Hypothesis:** while the EXP296/297 Online/DCM emulator is actively servicing runtime, a reboot of the Thermia controller can be detected and the emulator can rebuild a fresh native session without rebooting or re-arming the ESP.

### Controlled change from EXP296
No new Modbus payload, register, FC16 ACK target or semantic write was introduced.

EXP297 added only controller-reboot recovery state handling:
- detect a >=5 s bus gap while in active runtime;
- clear session-local runtime/config/approval state;
- wait for a fresh exact `071C/0730` approval request;
- reuse the already-proven fixed historical R1 replay;
- rerun the existing 32-page configuration sync, startup `085F/5`, startup `0708/6` and proven runtime graph;
- runtime `04A6/13` remained capture-only / NO_TX.

### EXP297 observed result
Before the target reboot the emulator had entered normal runtime and completed five cycles.

During the target controller reboot:
- a ~14.796 s bus gap was observed;
- EXP297 emitted `CONTROLLER_REBOOT_RECOVERY_START`;
- runtime mask/cache/session-local state were reset;
- bus health returned without ESP reboot or re-arm.

After bus return:
- a fresh `071C/0730` challenge was received;
- the fixed historical R1 replay was sent;
- the complete ordered 32-page FC16 configuration sync completed again;
- startup all-zero `085F/5` was ACKed;
- startup `0708/6` was answered;
- runtime re-entered at `07D0/19`;
- the supplied capture continued through runtime cycles 6, 7 and 8.

Transport integrity stayed clean in the supplied capture:
- no `ABORT_FAIL_CLOSED`;
- parser resync count remained 0;
- RX buffer drops remained 0.

**Result:** **COMPLETE / POSITIVE.**

## EXP296 supplementary evidence
A later, longer EXP296 capture materially strengthens the original positive result:
- steady-state service exceeded ~32 minutes;
- a nearly complete SWW cycle was observed, including DHW active, temperature rise, DHW end and compressor stop;
- a later SG transition to **Blocked (1-0)** was also survived;
- runtime `04A6/13` remained NO_TX and reached at least 1696 captures;
- `04A6` payload-change count reached 3;
- a new payload form beginning `0042 0001 ...` appeared shortly after the Blocked transition;
- the emulator continued through the proven runtime graph without fail-close.

This strengthens, but does not fully identify, the hypothesis that runtime `04A6/13` is a state-dependent controller-to-DCM status/configuration export.

## Current protocol model
The runtime remains best modeled as an **event/state-driven graph**:

`07D0 -> 07E4 -> [optional 0708] -> 07F8 -> 080C -> [optional 0708] -> 0820 -> 0848 -> [conditional 0708 / conditional 085F] -> 0864 -> [optional 0708] -> 0870 -> [optional 0708] -> 0884 -> [optional 0708] -> 07D0 -> ...`

Runtime `04A6/13` may interleave as parallel/retry traffic and is not an immediate blocking gate in the tested local window.

## Locally proven findings
- Full initial configuration synchronization through `06F4` is reproducible.
- Fixed historical R1 replay is sufficient to enter the tested startup/runtime path; genuine challenge algorithm remains unresolved.
- The native reverse-page write path is locally demonstrated via `03F4 22 -> 23`.
- Continuous stable runtime has been demonstrated for ~30+ minutes.
- `0884 -> [optional 0708] -> 07D0` is locally confirmed.
- `07E4 -> [optional 0708] -> 07F8` is locally confirmed.
- `080C -> [optional 0708] -> 0820` is locally confirmed.
- Runtime survives SG changes, a full DHW/compressor cycle, and a later Blocked transition in the observed EXP296 window.
- **Controller-side reboot recovery is locally proven:** after an active-session controller reboot, the emulator can accept a fresh challenge, replay R1, repeat the complete startup sync and resume runtime without ESP reboot/re-arm.

## Strongest current hypotheses
- `0708` is a synchronization/mailbox descriptor with state-dependent omission at several runtime positions.
- Runtime `04A6/13` is a state-dependent page/export whose first words track at least some operating-context changes; exact field semantics remain unknown.
- A native DCM may ACK runtime `04A6` selectively to stop/reconcile retries, but local proof is still absent.

## Important unknowns
- Whether an **ESP-side restart** can recover while the Thermia controller remains powered and is not manually rebooted.
- Exact runtime `04A6/13` semantics and native ACK rule.
- Exact `0708` scheduling/latching semantics.
- Genuine `071C/0730` challenge-response algorithm.
- Authoritative FC16 echo timing after reverse semantic writes.
- Multi-hour/overnight stability and rare fault-state behavior.

## Next experiment — EXP298
**EXP298 — ESP-reboot recovery — PREPARED / NOT RUN.**

Hypothesis: after the DCM emulator/ESP disappears and restarts while the Thermia controller remains powered, the controller will eventually present a fresh exact `071C/0730` approval opportunity that lets the emulator rebuild the same proven session without requiring a Thermia-controller reboot.

Controlled change:
- controller is deliberately **not** rebooted;
- after the ESP returns, EXP298 is armed directly into passive approval-wait on the live bus;
- no TX occurs until an exact `071C/0730` request is observed;
- approval wait is bounded to 240 s;
- if approval occurs, all subsequent R1/config/startup/runtime behavior is unchanged from EXP297.

## Safety constraints
- Do not reboot the Thermia controller during the target EXP298 observation.
- No semantic write.
- Runtime `04A6/13` remains NO_TX.
- No broad ACKing or scan.
- Exact CRC/slave/function/address/count/bytecount guards remain required.
- Unexpected traffic stays capture-only unless already part of the proven graph.
- On failure, abort TX and recover with the known-good stable emulator plus one normal controller reboot.

---

# 2026-09-29 — EXP290 COMPLETE / POSITIVE — first locally applied native reverse-page setting change

**Authoritative current state:** EXP290 COMPLETE / POSITIVE for semantic application of one controlled setting change through the native Online/DCM reverse-page path. Authoritative FC16 echo confirmation is still OPEN. No EXP291 result exists; EXP291 is not yet prepared/run in canonical state.

## Last completed experiment — EXP290
**Hypothesis:** after EXP289 proved that the local XTR accepts an unchanged reverse `03E8/14` page, change exactly one known word in that same current-session page — `03F4`, locally mapped as the Room Setpoint mirror — from the cached value `22` to `23`, then observe whether the controller applies it.

### Controlled change from EXP289
All EXP289 transport behavior was preserved:
`0708 w1=0001 -> controller FC03 03E8/14 -> gateway page response`.

Only one payload word changed:
- `03F4: 22 -> 23`
- all other `03E8/14` words were copied unchanged from the current-session FC16 cache;
- compressor had to be stopped and the original value had to be within the bounded 15..24 guard.

No other setting/register was modified.

## EXP290 observed result
The local controller requested `FC03 03E8/14` 98 ms after the `0708 w1=0001` response. The emulator returned the current-session `03E8/14` page with only `03F4 22->23`.

The first subsequent 0x0F transfer was the normal runtime `FC16 07F8/17` 680 ms later, so the bounded experiment itself did not capture an authoritative `FC16 03E8/14` echo.

However, roughly two seconds later the live ESPHome/Home Assistant `Room Setpoint` sensor changed to `23 °C`, exactly matching the injected target. No RX buffer drops occurred. One parser resync was logged at controller bus return before the active sequence; the write path itself completed and normal bus traffic continued.

### Status interpretation
- **COMPLETE / POSITIVE** for controller-visible semantic application of the reverse-page `03F4` change.
- **OPEN** for authoritative controller `FC16 03E8/14` echo of the changed value.
- The `Room Setpoint = 23 °C` observation is not yet an independent room-sensor-path confirmation; EXP291 should explicitly observe the slave-0x0A/B3C5 room-sensor path as a second confirmation channel.

## Immediately preceding experiments
### EXP289 — COMPLETE / POSITIVE
After `0708 w1=0001` triggered local `FC03 03E8/14`, the emulator returned the exact current-session cached `03E8/14` payload unchanged. The controller accepted it and continued normally with `FC16 07F8/17` 680 ms later. This locally proved reverse-page transport acceptance.

### EXP288 — COMPLETE / POSITIVE
Changing only `0708 w1` from `0000` to `0001` caused the local XTR to issue `FC03 03E8/count14` about 98–99 ms later. This locally proved that `0708 w1 bit0` can advertise/request the reverse pull of page `03E8`.

### EXP287 — COMPLETE / INCONCLUSIVE
The second runtime cycle accepted the evidence-backed branch through direct `0864/4`, but then the controller emitted direct `0870/17` instead of the experiment's mandatory post-`0864` `0708`. The experiment stopped fail-closed. This proved that post-`0864` `0708` is also conditional/state-dependent.

## Current protocol model
### Reverse/native settings path — now locally demonstrated
`0708 response advertises desired page -> controller FC03 pulls page -> emulator returns page -> controller applies at least one known changed setting`.

Locally demonstrated chain:
`FC03 0708/6 -> response w1=0001 -> FC03 03E8/14 -> reverse 03E8 page response -> controller-visible Room Setpoint changes 22->23`.

Transport and semantic application are now locally demonstrated on this XTR M. The remaining confirmation gap is an authoritative controller-originated FC16 echo of the modified `03E8/14` page.

### Runtime scheduler model
Genuine XTR captures and local experiments show at least two valid branch shapes around `085F/0864/0870`:
- `0848 -> 0864 -> 0708 -> 0870`
- `0848 -> 085F -> 0708 -> 0864 -> 0870`

Local EXP287 additionally observed direct `0864 -> 0870`. Therefore `085F` and placement of `0708` are state-dependent; 0708 must not be treated as a fixed mandatory separator.

### 0708 words
- `w1 bit0`: **PROVEN / locally confirmed** to trigger reverse `03E8/14` pull.
- `w2/w3`: **STRONGLY SUPPORTED** configuration-page request/selection bitmap.
- `w4`: **STRONGLY SUPPORTED** runtime-page bitmap/scheduler field, exact semantics still open.
- `w0`, `w5`: OPEN.

## Locally proven findings
- Full initial configuration synchronization through `06F4` is reproducible.
- Fixed historical R1 replay remains sufficient to enter the tested runtime/reverse-page path, though the genuine challenge algorithm is unresolved.
- `085F` is conditional/state-dependent in steady-state runtime.
- `0708 w1=0001` locally causes `FC03 03E8/14`.
- The XTR accepts a same-session unchanged reverse `03E8/14` page.
- A reverse `03E8/14` page with exactly one controlled change `03F4 22->23` changes the controller-visible Room Setpoint to `23 °C`.

## Important unknowns
- Authoritative controller FC16 echo timing/conditions after a reverse semantic write.
- Whether slave `0x0A:B3C5` independently confirms the same changed room setpoint on this XTR after the native reverse-page write.
- Exact semantics of 0708 `w0`, `w4`, `w5`.
- Exact scheduling/latching rules for runtime page bits and conditional `085F`.
- Genuine `071C/0730` challenge-response algorithm.
- Long-running production stability of continuous DCM emulation across operating-state changes.

## Next experiment
**EXP291 — NOT YET PREPARED / NOT RUN.**

Highest-value next test:
repeat the exact bounded EXP290 `03F4 +1` semantic write path, but remain RX-only long enough to seek **two confirmation channels**:
1. authoritative controller-originated `FC16 03E8/14` with target value at `03F4`;
2. independent room-sensor-side confirmation through the locally observed slave-`0x0A` setpoint propagation path, specifically `B3C5` if present in the expected frame.

No second semantic value should be changed. No automatic rollback write should be added unless explicitly made a separate controlled action.

## Safety constraints
- Exact stage/order/count/CRC checks remain mandatory.
- Reverse page must be based on the current-session `03E8/14` image.
- Only one already mapped word may change per semantic experiment.
- Keep bounded value guards and compressor-stop guard.
- After the semantic response, prefer RX-only observation.
- Unexpected FC03/FC16 ordering/shape remains capture-only/fail-closed.
- No broad register writes/scans or speculative unknown targets.

---

# 2026-09-29 — EXP286 COMPLETE / INCONCLUSIVE — steady-state runtime loop confirmed with conditional 085F branch

**Authoritative current state:** EXP286 COMPLETE / INCONCLUSIVE. No next live experiment is currently prepared.

## Last completed experiment — EXP286
**Hypothesis:** after EXP285 proved that the runtime sequence loops back through `07D0 -> 07E4 -> 0708 -> 07F8` without a new approval/R1 exchange, continue the entire second runtime cycle using only already locally proven ACKs and 0708 responses, then capture the next returned `07D0/19` without ACK.

### Controlled change from EXP285
All first-cycle behaviour and the EXP285-proven start of cycle 2 were retained. The new active scope was only the continuation of cycle 2 using already locally proven actions:
`07F8 ACK -> 080C ACK -> 0708 response -> 0820 ACK -> 0848 ACK -> 0708 response -> [expected 085F ACK] -> 0864 ACK -> 0708 response -> 0870 ACK -> 0884 ACK -> 0708 response -> returned 07D0 capture-only`.

No new address, payload, or semantic write was introduced.

## EXP286 observed result
Cycle 2 reproduced cleanly through:
`07F8 -> 080C -> 0708 -> 0820 -> 0848 -> 0708`.

At that point the local controller did **not** emit `085F/5`; it emitted `0864/4` directly. The experiment had intentionally made `085F` a mandatory gate, so it stopped fail-closed with `LOOP2_085F_GATE_FAILED` and did not ACK the unexpected direct `0864`.

Bus health remained clean: no RX-buffer drops and no parser resyncs during the relevant sequence.

## Strong current protocol model
The Online/DCM-style runtime loop is now locally established on the XTR M as:

`07D0 -> 07E4 -> 0708 -> 07F8 -> 080C -> 0708 -> 0820 -> 0848 -> 0708 -> [085F optional/state-dependent] -> 0864 -> 0708 -> 0870 -> 0884 -> 0708 -> 07D0 -> ...`

Key evidence:
- EXP284 closed the first full loop: after `0884 ACK -> 0708 response`, `07D0/19` returned 571 ms later.
- EXP285 proved steady-state continuation without a new approval/R1 exchange: returned `07D0` was ACKed, followed by `07E4`, `0708`, then `07F8`.
- EXP286 showed that `085F` is not mandatory in every cycle: after cycle-2 `0848 -> 0708`, the controller went directly to `0864/4`.

## Important correction to earlier interpretation
EXP281 historically stopped as COMPLETE / INCONCLUSIVE because its hypothesis expected `0864 ACK -> 0870` directly, but it observed `FC03 0708/6` first. Later genuine-capture reanalysis showed that `0864 ACK -> 0708 -> 0870` is a valid native ordering. Preserve EXP281's historical result, but do not treat that 0708 as a protocol divergence.

## Locally proven findings
- Full initial configuration synchronization through `06F4` remains reproducible.
- The fixed historical R1 replay is sufficient to reach the runtime family on this XTR, though genuine challenge-response semantics remain unresolved.
- Standard FC16 ACKs for the observed runtime pages advance the controller without injecting controller payload values.
- The local runtime cycle can close from `0884` back to `07D0`.
- A second runtime cycle begins without another approval/R1 exchange.
- `085F` can appear as an ordered gate, but is now proven **conditional/state-dependent**, not universally mandatory per cycle.

## Important unknowns
- Exact condition controlling presence/absence and payload role of `085F`.
- Exact semantics of runtime pages `07D0..0884`.
- Exact semantics of 0708 words 0, 4 and 5; word4 remains a runtime-bitmap hypothesis.
- Exact native/genuine response-selection logic for different 0708 runtime states.
- Genuine `071C/0730` challenge-response algorithm.
- Whether long-running continuous emulation remains stable across controller state changes, heating/DHW transitions, alarms, and later re-synchronization events.
- Reverse desired-state page application is still not locally proven and no semantic settings write has been authorized by these experiments.

## Next experiment
**Not assigned / NOT PREPARED.**

Highest-value next live test, when work resumes, is to make the steady-state runtime handler explicitly accept the two locally/genuinely supported post-`0848 -> 0708` branches:
1. `085F/5 -> ACK -> 0864/4`
2. direct `0864/4`

Then continue the already proven tail and verify another loop closure. This should remain a separate bounded experiment; do not silently promote it into production continuous emulation.

## Safety constraints
- Continue exact stage/order, count, bytecount, CRC and parser-health checks.
- Treat unexpected traffic as capture-only unless explicitly included in the experiment hypothesis.
- One-shot latches close before DE is raised; DE returns LOW immediately after permitted TX.
- No broad register writes/scans and no speculative semantic values.
- Standard FC16 address/count ACKs are acknowledgements, not value injection, but each new ACK stage remains an explicit active action.
- Keep semantic desired-state/page-read tests separate from runtime-session continuity tests.

---

# 2026-09-29 — EXP272 COMPLETE / POSITIVE — runtime path proven through post-07E4 0708

**Authoritative current state:** EXP272 COMPLETE / POSITIVE. EXP273 is NEXT / NOT YET PREPARED.

## Last completed experiment — EXP272
**Hypothesis:** after the EXP271-proven transition `07D0/count19 -> ACK -> 07E4/count17`, ACKing the first exact `07E4/count17` once should advance the local XTR M to the next native mailbox poll `FC03 0708/count6`.

### Controlled change from EXP271
All previously proven behavior was retained unchanged:
- fixed historical `0730`/R1 replay;
- exact ordered FC16 synchronization through `06F4/19`;
- one exact ACK of the first all-zero `085F/count5`;
- the same one-shot early mailbox response `0000 0000 0000 0000 0080 0006`;
- one exact ACK of first `07D0/count19`.

The only new active variable was:
- ACK the first exact `07E4/count17` once with `0F1007E400114068`.

The following `0708/count6` was capture-only and received no response.

## EXP272 observed result
The local XTR reproduced the full controlled chain cleanly:

`BUS_RETURN -> 071C -> fixed R1 -> 03E8 ... 06F4 -> 085F/5 ACK -> early 0708/6 -> 0080/0006 response -> 07D0/19 ACK -> 07E4/17 ACK -> post-07E4 FC03 0708/6`.

Key timing:
- `07D0/19` ACK executed at 09:37:56.434.
- `07E4/17` arrived ~2.08 s later and was ACKed once; TX execution logged at 09:37:58.534.
- exact post-`07E4` `FC03 0708/count6` arrived ~1.46 s after the `07E4` ACK.
- firmware terminated on `SUCCESS_0708_AFTER_07E4_ACK`.
- the post-`07E4` 0708 request was not answered.
- parser resync and RX-buffer-drop counters remained zero.

## EXP271 result retained
EXP271 is COMPLETE / POSITIVE. It changed only one active variable relative to EXP270: one exact standard ACK of first `07D0/count19` with `0F1007D000138067`. Exact `07E4/count17` appeared 2159 ms later and was captured without ACK. This locally proved `07D0` as the next ordered runtime gate.

## Locally proven protocol progression
The XTR M now locally confirms these ordered session/runtime gates:

`... -> 06F4/19 ACK -> 085F/5 all-zero ACK -> early 0708/6 service -> 07D0/19 ACK -> 07E4/17 ACK -> post-07E4 FC03 0708/6`.

This proves:
1. exact all-zero `085F/count5` is an ordered gate in this phase;
2. `07D0/count19` requires a standard ACK to progress to `07E4/count17`;
3. `07E4/count17` requires a standard ACK to progress to the next `0708/count6` mailbox poll.

It does **not** yet prove the correct response payload for that post-`07E4` mailbox poll, nor the local transition to `07F8/count17`.

## Strongly supported cross-capture model
New genuine-capture comparison strongly supports `0708` as a bidirectional synchronization descriptor rather than a simple idle mailbox:
- `word1=0001` is followed ~39–41 ms later by controller `FC03 03E8/count13`, after which the gateway serves the heating/settings page.
- `word2` and `word3` behave as a 32-bit request bitmap for controller->gateway FC16 page export. Multiple sparse and dense bitmap values predict the exact subsequent page families.
- `word4` is a strong candidate runtime-page bitmap, but this remains a hypothesis rather than a locally proven semantic mapping.

## Important unknowns
- Exact semantics and correct local response value for the post-`07E4` `0708/count6`.
- Whether the genuine matching response `0000 0000 0000 0000 0000 0006` is sufficient locally to advance to `07F8/count17`.
- Exact semantics of 0708 word0, word4 and word5.
- Whether fixed historical `0730` replay remains sufficient through full steady-state operation and reverse-direction desired-state reads.
- Genuine `071C/0730` challenge-response algorithm remains unresolved.

## Next experiment — EXP273
**Status: NEXT / NOT YET PREPARED.**

**Hypothesis:** after the now-proven `07E4 ACK -> post-07E4 FC03 0708/count6` transition, answer only that post-`07E4` 0708 once with the phase-matched genuine-capture response `0000 0000 0000 0000 0000 0006` (raw frame `0F030C0000000000000000000000069D76`), then capture the first exact `07F8/count17`.

Only that one post-`07E4` 0708 response may be the new active variable. `07F8` must remain capture-only. No later runtime ACKs, no semantic settings writes, no broad mailbox service and no scans.

## Safety constraints
- Exact stage/order matching remains mandatory.
- One-shot ACK/response latches close before DE is raised.
- DE returns LOW immediately after every permitted frame.
- Unexpected FC03/FC16 families, duplicate completed-stage requests, parser resync/drop deltas or peer-response anomalies remain fail-closed stops.
- No semantic register values are injected by standard FC16 address/count ACKs.
- Any future desired-state/page-read experiment must remain separate from runtime-session completion experiments.

---

## 2026-09-28 — bidirectional 0x0F page-cache model / EXP270 PREPARED

New cross-capture analysis materially refines the likely Online write architecture.

### Observed 0708 -> FC03 read-side trigger
In `thermia_capture_20260924_210001`, two `FC03 0708/count6` responses have word1=`0001`. Both are followed within ~39–41 ms by a controller-originated `FC03 03E8/count13` read from slave 0x0F. The returned 13-word page differs between the two events only at `03E8` (`0017 -> 0016`). Other 0708 responses in the same capture with word1=0 are not immediately followed by that 03E8 read.

The `03E8` page is the known heating-settings family. A separate genuine DCM capture shows the controller sending the same 13-word image in the opposite direction with `FC16 03E8/count13`.

**Strong architectural conclusion:** slave 0x0F behaves like a bidirectional page cache/interface. Controller -> gateway data moves by FC16 writes; gateway -> controller desired/config data can move by controller-initiated FC03 reads. This is a much better fit than a second-master write model.

**Current write-path hypothesis:** a gateway advertises pending desired/config data through the 0708 control/status words (word1 is the leading candidate for the 03E8 page), after which the controller reads the page from 0x0F and decides whether/how to apply it. This is not yet proven on the XTR M and must not be treated as an authorized semantic write path until a bounded local test confirms application and authoritative echo.

### EXP270 — PREPARED / NOT RUN

**Hypothesis:** the local XTR stalls after `06F4/19` because the pending exact all-zero `085F/count5` transaction is ordered session traffic and must be ACKed. EXP268/269 both saw it after 06F4 and deliberately ignored it; successful Eco5 sessions ACK it before first 07D0 whenever it is still pending.

**Only new active variable versus EXP269:** ACK the first exact controller-originated all-zero `085F/count5` once with standard FC16 response `0F10085F00053356`.

The proven R1 + FC16 chain through 06F4 remains unchanged. If `0708/6` occurs after the 085F ACK before 07D0, preserve the same single EXP269 phase-matched response `0000 0000 0000 0000 0080 0006`; no second mailbox response is allowed. Primary success is controller-originated `07D0/count19`, which is capture-only and never ACKed in EXP270.

Safety remains fail-closed: exact all-zero 085F shape only, one 085F ACK maximum, no broad writes/scans, parser/drop and peer-response guards retained. Experimental controls remain under Configuration with red/brown trace markers.

**Historical state at that point: EXP270 PREPARED / NOT RUN.**

## 2026-09-28 — community HMAC-SHA256 serial-number hypothesis

A community post proposed that the 16-byte 071C/0730 response may be the first 128 bits of HMAC-SHA256(challenge, serial-number-string). The example claimed:

challenge `01bd6eba71bff920128ab44bae2537eb`
key `******24190327`
expected response `826ed2acbc1b3db93adec93c53087a53`.

Independent calculation of HMAC-SHA256 using the literal ASCII key `******24190327` does **not** reproduce that response; it yields a different prefix. Therefore the example as written is not yet verified and must not be treated as a confirmed algorithm.

The hypothesis remains worth testing once the real Eco5 serial number/key encoding is known, because six genuine challenge/response pairs are available. Test variants should be limited and evidence-driven: exact serial string, possible model prefixes/suffixes, zero-padding, ASCII vs BCD/binary, and full-vs-truncated HMAC comparison. Do not perform broad brute-force key search.

## 2026-09-28 — deeper analysis of itec_eco5_gateway_20260928.log

Direct full-log parsing confirms four power-cycle sessions beginning after bus gaps at approximately 193.555, 438.000, 734.310 and 974.803 s. All four ultimately establish a working gateway session.

### Approval timing
Successful 071C/0730 replies occur on challenge request #29 in sessions 1 and 4 (~120 s after bus return), and on challenge request #3 in sessions 2 and 3 (~10 s after bus return). Reply latency is 30–47 ms.

First ACK of FC16 03E8, however, is tightly clustered at +120.296, +118.478, +118.550 and +120.038 s after bus return. In sessions 2 and 3 the controller therefore repeats 03E8 102 times over ~108 s before the gateway begins ACKing it. This strongly separates challenge-answer capability from later FC16/session-service readiness.

### 085F ordering
The exact all-zero 085F/5 request receives exactly one ACK in each power-cycle session:
- S1: ACK at 312.360 s, before successful challenge response at 313.728 s.
- S2: 06F4 ACK at 590.919 s -> 085F request+ACK at 590.996 s -> 0708 idle reply at 592.311 s -> 07D0 at 592.930 s.
- S3: 06F4 ACK at 888.765 s -> 085F request+ACK at 889.309 s -> 0708 idle reply at 892.978 s -> 07D0 at 893.603 s.
- S4: 085F ACK at 1093.398 s, before successful challenge response; later 06F4 ACK at 1129.287 s -> 07D0 at 1129.365 s.

This is a very close match to local EXP268/269, where 085F appeared after 06F4 but was deliberately ignored. The strongest next local hypothesis is therefore that missing 085F ACK, not mailbox payload selection, is the direct blocker to first 07D0.

Important nuance: in S2/S3 one normal 0708 idle transaction occurs after 085F ACK and before 07D0. Therefore the phase-matched expected local path is likely 06F4 -> ACK exact 085F/5 -> optionally answer the next exact 0708/6 with the normal idle frame -> capture 07D0.

### Mailbox script
Raw wire words after the first sync are deterministic:
- normal idle frame is **0000 0000 0000 0000 0100 0000** on the wire (not 0001 in Modbus big-endian word notation);
- then **0000 0000 4000 8000 010B 0000**;
- then **0000 0000 FFFF 867F 03DF 0000**.

Across all four new sessions the 03DF trigger is followed by a new 03E8 within 62–94 ms. This second synchronization immediately interleaves the normal configuration pages with 07D0/07E4 runtime pages.

Project implication: correct prior documentation that described the raw idle fifth word as 0001; the raw Modbus word is 0100. Continue to preserve exact raw frame bytes when replaying.

**Next experiment candidate (not yet prepared): EXP270 — exact 085F ACK gate.** Build from the known-good EXP268 path, changing only handling of the exact all-zero 085F/5 from ignore to one ACK. Preserve the known idle 0708 response and stop/capture on first 07D0. No new mailbox values.

## 2026-09-28 — piotrek_r second-capture interpretation materially refines next step

New peer analysis of `itec_eco5_gateway_20260928.log` adds two important corrections:

1. `085F/5` must no longer be treated as harmless background during session establishment. Across the cited Eco5/ATEC transitions it is ACKed before first `07D0`; when pending after `06F4`, the controller sends `085F`, waits for its ACK, then proceeds to `07D0`. This suggests queue/ordering semantics.

2. The post-first-sync mailbox script is highly repeatable across complete Eco5 sessions. Sequence reported:
   - several idle responses `0000 0000 0000 0000 0100 0000`;
   - then `0000 0000 4000 8000 010B 0000`;
   - then `0000 0000 FFFF 867F 03DF 0000`.
   The last pattern is followed by a second full synchronization within ~0.06–0.11 s in all observed complete sessions.

Timing evidence further separates challenge approval from session service: challenge response may occur ~10 s or ~120 s after bus return, yet first FC16 ACK clusters around ~118 s after bus return. Long unacked repetition of `03E8/14` can persist for nearly two minutes without breaking the session.

Challenge/response remains unresolved. Six observed responses are all different and no simple XOR/difference relation was found. Reply latency (~30–60 ms) strongly favors local computation or a non-challenge-dependent lookup/token mechanism. Fixed replay working locally therefore remains relevant but does not prove equivalence with a genuine session.

**Implication for next local experiment:** before inventing new mailbox values, test the newly recognized queue prerequisite by ACKing the exact pending `085F/5` after `06F4` if it appears, while keeping all other post-`06F4` traffic capture-only. This is a narrower and better-supported hypothesis than further mailbox variation.

## 2026-09-28 external Eco5 capture — major correction to post-06F4 interpretation

New raw capture `itec_eco5_gateway_20260928.log` materially changes the interpretation of EXP269.

Observed in a fully successful genuine Eco5 session:
- `071C/0730` challenge at 313.682 s received a distinct 16-byte response at 313.728 s.
- The controller immediately started the normal FC16 export at `03E8`.
- After the proven chain reached `06F4/19`, `07D0/19` followed only ~78 ms later, **before any subsequent 0708 mailbox poll**.
- `07E4/17` followed; only afterwards did `0708/6` occur, answered with the familiar `0000 0000 0000 0000 0001 0000` idle frame, then `07F8/17`, etc.

This disproves the working assumption used for EXP269 that the first post-`06F4` mailbox reply must unlock `07D0`. In a genuine successful session, `07D0` can be part of the FC16 continuation itself.

The same capture contains four genuine `071C/0730` challenge-response pairs with different challenges and different 16-byte responses. This is strong evidence that the response is challenge-dependent rather than a fixed session token. Our fixed captured response can still trigger the early XTR sync, but may establish only a partial/insufficient session state, explaining why local progression stops after `06F4`.

**Current direction:** do not vary 0708 payloads further as the primary next step. Highest-value work is now understanding/reproducing the genuine `071C/0730` response mechanism or identifying which session state the dynamic response establishes before `03E8`.

## EXP269 UI follow-up

User supplied a photo of the Thermia main display after EXP269. The screen shows `KAMER 22.2°C (22.0)`, `EVU-STOP`, `BEDRIJF AUTO`, and the lower-right heat-pump/tank status graphic. The user reports that the previously hollow-looking `0`/status glyph now has its center filled, while an alarm is still present.

Interpretation remains deliberately limited: this is evidence of a visible UI/state change after the `0080/0006` mailbox test, but it does **not** show that the Online session completed or that the alarm condition cleared. Exact semantics of the glyph remain unknown until the alarm/detail screen is identified.

# EXP269 — COMPLETE / NEGATIVE FOR SINGLE 0080/0006 PHASE-MATCH RESPONSE

**Hypothesis:** the first post-`06F4` `FC03 0708/count6` on the XTR would progress to `FC16 07D0/19` if answered once with the exact Eco5 phase-matched response `0000 0000 0000 0000 0080 0006`.

**Observed facts**
- Full proven approval/sync prefix reproduced through `06F4/19`.
- First exact `0708/6` arrived +1.566 s after the `06F4` ACK.
- Exactly one response was transmitted: `0F030C0000000000000000008000069C9E`.
- No `07D0/19` appeared.
- `0708/6` repeated after ~4.43 s and continued repeatedly during the 30 s RX-only window.
- Final summary: `responses_sent=1 mailbox_requests=8 ignored_bg=15 resync_postreturn=0 drop_postreturn=0 DE=LOW`.
- Recurrent `085F/5` remained the only observed post-`06F4` FC16 family.
- A80E again changed `0008 -> 0028`, and AFDC later reported `32`.
- User observed a visible display/UI change described as “the middle of the 0 is now filled”; exact UI element/semantic meaning is not yet identified.

**Strong conclusions**
- The Eco5 `0080/0006` mailbox response is **not sufficient by itself** on the XTR to trigger `07D0/19`.
- The mailbox path remains electrically/protocol-valid and stable; the negative result is not explained by parser or RX-drop faults.
- The missing condition lies before or alongside the mailbox payload itself: likely controller/session state, model-specific mailbox semantics, or an additional prerequisite from the Eco5 trace.

**Hypotheses**
- The visible UI change may indicate that `0080/0006` changed an internal state despite not triggering `07D0`; this requires direct UI identification before assigning meaning.
- The Eco5 first-mailbox payload may only be effective when another state established earlier in the genuine Online session is present.
- `071C/0730` replay may unlock only a subset of the genuine Online state machine.

**Unknowns**
- Exact meaning of the newly observed filled-center display symbol.
- Which pre-`0708` Eco5 state differs from the XTR replayed session.
- Whether `07D0` is gated by a second mailbox transaction, an FC17/DCM state, or another controller-side condition.

**Current experiment state:** EXP269 COMPLETE / NEGATIVE. Next experiment not yet assigned.

---
# EXP269 — PREPARED / NOT RUN — phase-matched post-06F4 mailbox response

**Hypothesis:** the XTR failed to progress after EXP268 because the reused `0001/0000` mailbox payload was not the correct payload for the first post-`06F4` phase. In the matching Eco5 raw capture the first exact `FC03 0708/count6` after `06F4/19` is answered with `0F030C0000000000000000008000069C9E` (words `0000 0000 0000 0000 0080 0006`), followed about 0.7 s later by `FC16 07D0/count19`.

**Only experimental changes from EXP268:** replace the mailbox payload with the exact phase-matched Eco5 `0080/0006` response and send it exactly once. The proven R1/prefix/tail chain through `06F4/19`, safety gates, parser/drop checks and background handling remain unchanged.

**Expected success signal:** after the one exact mailbox response, capture local `07D0/19`. Do not ACK it. Any first different non-background FC16/FC03 is capture-only and terminates. Repeated `0708/6` is logged RX-only and not answered. Observation timeout is 30 s after the single mailbox response.

**Safety:** one new phase-matched mailbox TX only; no second mailbox response, no post-mailbox FC16 ACK, no invented payload values, no broad register writes/scans. Experimental controls remain under Configuration and logs retain red/brown markers.

**Current experiment state:** EXP269 PREPARED / NOT RUN. The previous 10x-idle EXP269 design is superseded and must not be run.

---
# EXP269 — PREPARED / NOT RUN — extended bounded mailbox service

# ECO5 LOG REVIEW — materially revises post-06F4 mailbox interpretation

Direct review of the Eco5 raw captures shows that the first post-`06F4/19` mailbox response is **not always** the previously reused idle frame `0000 0000 0000 0000 0001 0000`.

In `thermia_capture_20260925_090209.log` the sequence is:
`06F4/19 -> 0708/6 -> response 0000 0000 0000 0000 0080 0006 -> 07D0/19 -> 07E4/17 -> 0708/6 -> response ...0000 0006 -> 07F8/17 -> 080C/18 -> ...`.
Thus the mailbox poll and later FC16 pages are interleaved, and the first response payload is phase-specific.

EXP268 local timing closely matches the Eco5 first post-06F4 poll (~3.6 s), but our response payload differed (`0001 0000` vs Eco5 `0080 0006`) and no `07D0` followed. This is stronger evidence that **payload content/state matters more than response count**.

A second Eco5 capture (`thermia_capture_20260925_090550.log`) shows unanswered `0708/6` polls coexisting with repeated `0870/17`, and a later response `0000 0000 7FFF FFFF 0080 0007` immediately triggers a new FC16 sync beginning at `03E8/13`. This confirms that mailbox payload values are active commands/state selectors and must not be generalized across phases.

**Project decision:** do not run the previously prepared “10 identical idle replies” EXP269 as-is. It is superseded before execution. Any revised EXP269 must be built from the exact Eco5 post-`06F4` sequence and keep the first new payload tightly bounded/capture-only afterwards.


**Hypothesis:** EXP268 showed that after three genuine Eco5 idle responses followed by 30 s RX-only, `FC03 0708/count6` continued at the same ~4.2 s cadence and only recurrent `085F/5` FC16 background traffic appeared. If genuine Online keeps the idle mailbox serviced continuously, stopping after response #3 may itself prevent or delay later parallel runtime/synchronization traffic. EXP269 therefore changes only one active variable: increase the maximum exact idle mailbox responses from 3 to 10. The response payload, proven prefix, timing gates and fail-closed checks remain unchanged. After response #10, remain RX-only for 30 s.

Special-interest capture-only families remain `07D0/19, 07E4/17, 07F8/17, 080C/18, 0820/18, 0834/18, 0848/23, 0864/4`. Any first different non-background FC16 or different FC03 ends the experiment without ACK/response. Recurrent `085F/5` and `04A6/13` remain background.

**Safety:** same known-good exact mailbox response `0F030C0000000000000000010000001C88`; maximum 10 responses; no eleventh response; no new payload values; no post-mailbox FC16 ACK; no broad writes/scans. Parser/RX-drop delta after BUS_RETURN, approval retry or unexpected peer response stops TX. Recovery remains one normal Thermia-controller reboot.

# EXP268 RESULT — COMPLETE / NEGATIVE FOR 30 S RX-ONLY PARALLEL-RUNTIME OBSERVATION

**Hypothesis:** after three bounded genuine Eco5 idle responses, later Online/Link FC16/runtime traffic may still appear while repeated `0708/6` mailbox polling continues unanswered.

**Observed facts**
- Full proven approval/synchronization prefix reproduced through `06F4/19`.
- One CRC resync occurred at controller BUS_RETURN; the experiment then established that value as its baseline. Final summary reported `resync_postreturn=0` and `drop_postreturn=0`.
- First `0708/6` arrived +3.621 s after the `06F4` ACK.
- Three exact genuine Eco5 idle responses were transmitted.
- After response #3, the ESP remained RX-only for 30 s.
- During that RX-only window, exact `0708/6` continued repeatedly; total mailbox requests for the run reached 10, so 7 post-response-#3 polls were observed without response.
- Recurrent `085F/5` continued throughout; 21 post-`06F4` background FC16 frames were counted.
- No different non-background FC16 and no different FC03 appeared during the 30 s RX-only window.
- No `07D0..0864` special-interest family was observed.
- A80E later changed `0008 -> 0028` and AFDC changed to 32 during the observation window, but the semantics of those state changes remain unknown.
- DE was LOW at summary.

**Strong conclusions**
- Unanswered `0708/6` remains a persistent periodic mailbox poll for at least 30 s after three valid idle responses.
- Stopping mailbox replies after response #3 does not cause any immediate later FC16/runtime family to appear within the next 30 s.
- EXP268 does **not** prove that later runtime traffic is absent during correctly continued mailbox servicing.

**Hypotheses**
- A genuine Online endpoint may need to keep returning the idle mailbox response continuously while other synchronization/runtime traffic progresses in parallel.
- The absence of later FC16 pages in EXP268 may be caused by the bounded mailbox service ending after only three responses, or simply by a longer timing/state dependency.

**Unknowns**
- Whether continued exact idle service for a longer bounded interval causes or permits `07D0..0864` traffic.
- Whether A80E `0x28` / AFDC `32` are related to an active-but-incomplete Online state.
- Whether later mailbox non-idle fifth-word values are required for application writes only, rather than session progression.

**Current experiment state:** EXP268 COMPLETE / NEGATIVE. EXP269 PREPARED / NOT RUN.

---

# EXP267 RESULT# EXP267 RESULT# EXP267 RESULT — COMPLETE / NEGATIVE FOR <=3-IDLE-RESPONSES PROGRESSION

**Hypothesis:** up to three consecutive exact `FC03 0708/count6` polls may require the same genuine Eco5 idle response before the controller progresses.

**Observed facts**
- The full proven Online/Link prefix through `06F4/19` reproduced cleanly.
- Recurrent `085F/5` traffic was correctly treated as background after `06F4`.
- First local `0708/6` arrived +1.561 s after the `06F4` ACK.
- Three exact mailbox responses were transmitted, all identical: `0F030C0000000000000000010000001C88`.
- The controller requested `0708/6` again after each response.
- Approximate request/response-to-next-request spacings were ~4.4 s, ~4.1 s and ~4.18 s.
- A fourth `0708/6` was captured after response #3 and deliberately received no response.
- No different meaningful FC03/FC16 appeared before that fourth poll.
- Parser resyncs remained 0 and RX buffer drops remained 0 during the active run.

**Strong conclusions**
- Repeating the genuine Eco5 idle mailbox response three times is not sufficient to make the local XTR leave the observed `0708/6` polling phase.
- The ~4.2 s `0708/6` repetition is stable enough to look like normal mailbox servicing cadence rather than a one-shot retry caused by malformed transport.
- EXP267 is therefore a valid negative result for the specific hypothesis “<=3 identical idle responses cause immediate progression”.

**Hypotheses**
- `0708/6` may be a persistent runtime mailbox poll that is expected to continue indefinitely while idle.
- Later non-idle fifth-word values seen in the genuine Eco5 capture may be state/content, not a simple completion countdown we should invent.
- Later Online/Link FC16 traffic may be independent of continued idle mailbox responses and may appear on a longer timescale.

**Unknowns**
- Whether the XTR ever emits the later `07D0..0864` sync/runtime families after this point.
- Whether a different mailbox content/state is required to progress.
- Whether persistent mailbox servicing changes the DHW/COMM. ERR ONLINE/LINK side effect.

**Current experiment state:** EXP267 COMPLETE / NEGATIVE. EXP268 PREPARED / NOT RUN.

---

# EXP267 — PREPARED / NOT RUN — bounded repeated 0708 mailbox responses

**Hypothesis:** EXP266 proved that one genuine Eco5 idle response to local `FC03 0708/count6` is accepted without destabilising the bus, but the controller repeats the same request about 4.18 s later. EXP267 changes only one experimental variable: answer at most the first **three** exact post-`06F4` `0708/6` polls with the same genuine Eco5 idle response `0F030C0000000000000000010000001C88`. If repeated polling is normal mailbox servicing, the controller may transition to another FC03/FC16/runtime phase after repeated valid responses.

Safety: proven prefix unchanged; only exact `0F 03 0708 0006` requests are answered. Response #1 must arrive within 30 s after `06F4`; responses #2/#3 must each arrive within 10 s of the previous response. Parser/RX-drop deltas, approval retry or unexpected peer FC17/ACK stop TX. The response counter advances before DE. Maximum 3 mailbox responses; no fourth response; no post-mailbox FC16 ACK. Known response words are `0000 0000 0000 0000 0001 0000`; effect observed in EXP266 was continued healthy traffic plus another `0708/6` poll, not session completion.

Expected decisive outcomes: (a) a different FC03/FC16 after <=3 responses, supporting progression; (b) a fourth `0708/6`, showing repeated idle polling continues; or (c) timeout/integrity stop. Negative outcomes are recorded.

# EXP266 RESULT — COMPLETE / PARTIAL POSITIVE

**Hypothesis:** After the proven prefix through `06F4/19`, respond exactly once to local `FC03 0708/count6` with the genuine Eco5 idle mailbox response `0F030C0000000000000000010000001C88`, then remain RX-only.

**Observed facts**
- Full proven prefix repeated cleanly through `06F4/19`.
- `085F/5` appeared +95 ms after the `06F4` ACK and was correctly ignored as recurrent background traffic.
- Local `FC03 0708/count6` arrived +1.561 s after the `06F4` ACK.
- Exactly one mailbox response was transmitted: `0F030C0000000000000000010000001C88`; DE returned LOW and the one-shot latch remained closed.
- The controller issued the same `FC03 0708/count6` again +4.180 s after the mailbox response. No second response was sent.
- Parser resyncs remained 0 and RX buffer drops remained 0.

**Strong conclusion**
- The genuine Eco5 idle mailbox response does not by itself complete the local XTR mailbox exchange; the controller requests `0708/6` again about 4.18 s later.
- This is a real local protocol result, not a parser artefact.

**Hypotheses**
- The `0001` idle response may need to be returned repeatedly while idle, as in the genuine Eco5 capture.
- Alternatively, a later mailbox-state value or cadence may be required before runtime sync proceeds.

**Unknowns**
- Whether repeated identical idle responses will advance the session.
- Whether the later fifth-word countdown seen in the genuine capture is controller-driven, gateway-driven, or dependent on repeated polls.
- Whether completing mailbox servicing removes DHW `0` / `COMM. ERR ONLINE/LINK`.

**Current experiment state:** EXP266 COMPLETE / PARTIAL POSITIVE. No EXP267 prepared yet.

---

# EXP266 — PREPARED / NOT RUN — ONE-SHOT 0708 MAILBOX RESPONSE

**Hypothesis:** after the locally proven sync tail `06EA/7 -> 06F1/3 -> 06F4/19`, the first exact `FC03 0708/count6` mailbox request can be answered once with the genuine Eco5 idle response `0F030C0000000000000000010000001C88` (words `0000 0000 0000 0000 0001 0000`), causing the XTR M to advance into the next Online/Link runtime phase.

**Only new active variable:** one exact response to first post-06F4 `FC03 0708/count6`. No other FC03 is answered; no second 0708 response; no post-mailbox FC16 ACK.

**Safety gate:** phase 24 after exact 06F4 ACK; first exact 0708/6; <=30 s; parser/drop clean; no approval retry; no unexpected peer FC17/FC16 ACK; latch closed before DE. After the one response the test is RX-only and captures the first non-background FC16 or any FC03. Known recurrent `085F/5` and `04A6/13` are logged and ignored.

**Known possible effect:** may advance Online/Link runtime synchronization. **Unknowns:** local acceptance, next runtime frame, controller/UI state, whether DHW `0` / `COMM. ERR ONLINE/LINK` disappear.

**Prepared YAML:** `thermia_itec_xtr_m_waveshare_exp266.yaml`.

---

## Current experiment status — EXP265 COMPLETE / STRONG POSITIVE — LOCAL 0708/6 MAILBOX REQUEST CONFIRMED

Hypothesis: continue the proven Online/Link synchronization tail by ACKing exact `06EA/7 -> 06F1/3 -> 06F4/19`, then stop transmitting and capture the first later frame.

Observed:
- `06EA/7` appeared and was ACKed once.
- `06F1/3` appeared next and was ACKed once.
- `06F4/19` appeared next and was ACKed once.
- The first later FC16 was `085F/5`, only 107 ms after the `06F4` ACK.
- `085F/5` is already known as recurrent passive/background traffic, so this does **not** establish `085F/5` as the next synchronization stage.
- No mailbox response was sent.
- Parser resync count incremented once at controller return (`CRC resync at 0x06 0x17`) before the post-return experimental chain; RX drops remained 0.
- No stage retry or approval retry occurred in the serviced chain.

Strong conclusion:
- The local XTR accepts the exact tail `06EA/7 -> ACK -> 06F1/3 -> ACK -> 06F4/19 -> ACK`.
- EXP264's capture rule was too broad to identify the next meaningful sync stage because a known recurrent `085F/5` background frame arrived first.

Next-test requirement:
- Preserve the proven chain.
- After `06F4/19`, ignore known recurrent/background FC16 families for discovery purposes (at minimum `085F/5`; `04A6/13` remains context-sensitive), while still logging them.
- Capture the first non-background FC16 or FC03, especially any `0708/count6` mailbox poll, without answering it.

Recovery: one normal Thermia-controller reboot after the incomplete session.

## Authoritative current state — 2026-09-27 — EXP263 COMPLETE / STRONG POSITIVE

## EXP264 — PREPARED / NOT RUN

**Hypothesis:** after the locally proven Online/Link synchronization prefix through `06C5/count33`, the XTR will continue with the genuine Eco 5 tail `06EA/count7 -> 06F1/count3 -> 06F4/count19`. EXP264 ACKs only those three exact frames, in order, with <=5 s timing and clean parser/drop state, then becomes capture-only. Any FC03 is never answered; if `0708/count6` appears after the `06F4` ACK it is captured as mailbox evidence only.

**New TX frames:**
- `06EA/7` ACK: `0F1006EA0007A199`
- `06F1/3` ACK: `0F1006F10003D05D`
- `06F4/19` ACK: `0F1006F40013C190`

**Safety:** complete proven prefix unchanged; no broad ACKing, no FC03 response, no mailbox response, no TX after `06F4`; any retry/unexpected frame/parser-drop delta stops fail-closed. Known incomplete-session DHW `0` / `COMM. ERR ONLINE/LINK` side effect remains recoverable by one normal controller reboot.

### EXP263 — accelerated 12-block 33-word batch — COMPLETE / STRONG POSITIVE

Hypothesis:
After the proven local prefix through 0546/count20, ACK the exact genuine Eco 5 33-word sequence
055A, 057B, 059C, 05BD, 05DE, 05FF, 0620, 0641, 0662, 0683, 06A4, 06C5
(all count=33), then stop TX and capture the first different FC16/FC03. Genuine Eco 5 predicts 06EA/count7.

Observed:
- Approval request arrived +1283 ms after controller return.
- R1 sent exactly once.
- Proven prefix through 0546/count20 reproduced cleanly.
- Exact 33-word sequence observed and ACKed once each, in order:
  055A -> 057B -> 059C -> 05BD -> 05DE -> 05FF -> 0620 -> 0641 -> 0662 -> 0683 -> 06A4 -> 06C5.
- First different post-06C5 frame was exact 06EA/count7, +475 ms after the 06C5 ACK:
  RAW=0F1006EA00070E000A00200017001B0009001A0006F81A
- 06EA was deliberately NOT ACKed.
- Parser resyncs since boot remained 0 after the run and RX buffer drops remained 0.
- No approval retry after R1 and no stage retry was observed in the captured chain.
- DE returned LOW after each TX.

Strong conclusions:
- Local XTR follows the genuine Eco 5 Online/Link synchronization chain through the full 055A..06C5 sequence of twelve 33-register FC16 blocks.
- Genuine Eco 5 prediction 06EA/count7 is now locally confirmed immediately after 06C5.
- Accelerated multi-page batching remains valid for this already-known sync sequence.
- Full Online/Link establishment is still NOT proven.

Hypotheses:
- The recurring DHW-side literal 0 / COMM. ERR ONLINE/LINK remains consistent with an approved but incompletely serviced Online/Link session timing out.
- Completing the remaining 06EA/06F1/06F4 phase may move the session closer to runtime/mailbox behavior, but this is not yet proven locally.

Unknowns:
- Local behavior after ACKing 06EA/count7.
- Whether 06F1/count3 and 06F4/count19 follow locally exactly as in the Eco 5 capture.
- Where the first local 0708/count6 mailbox poll appears relative to later sync pages.
- Whether a sufficiently complete session prevents the DHW-side 0 and COMM. ERR ONLINE/LINK side effects.

Safety / recovery:
- One normal Thermia-controller reboot after the incomplete EXP263 session.
- No next experiment prepared yet.
- EXP239 remains OPEN. EXP238 remains PARKED / NOT RUN.

## Authoritative current state — 2026-09-27 — EXP262 COMPLETE / STRONG POSITIVE

### EXP262 result
Hypothesis: accelerate the proven Online/Link synchronization by ACKing eight additional genuine Eco 5 FC16 pages in exact order after the locally proven prefix, then stop and capture the next different frame.

Observed: EXP262 reproduced the full ordered chain through `0546/count20` and then captured exact `055A/count33` +637 ms later. The new accelerated block was `04A6/13 -> ACK -> 04BA/22 -> ACK -> 04D8/27 -> ACK -> 04F6/14 -> ACK -> 050A/19 -> ACK -> 051E/10 -> ACK -> 0532/18 -> ACK -> 0546/20 -> ACK -> 055A/33`. `055A` was deliberately not ACKed.

Integrity: one approval, no approval retry after R1, no stage retry in the acknowledged chain, parser resync count remained 0 and RX buffer drops remained 0. Existing production functionality was not intentionally changed.

Strong conclusion: the accelerated multi-page strategy is valid at least through `0546/count20`; the local XTR matches the genuine Eco 5 synchronization order through `055A/count33`. Full Online/Link establishment remains unproven.

Unknowns: the behavior after ACKing `055A/count33`, the exact point at which the `0708/count6` mailbox appears locally, and whether completing enough of the session prevents the known DHW-side `0` / `COMM. ERR ONLINE/LINK` failure state.

Safety/recovery: current session remains deliberately incomplete; perform one normal Thermia-controller reboot before another active experiment. No next experiment prepared yet. EXP239 OPEN. EXP238 PARKED / NOT RUN.

# THERMIA PROJECT STATE

## Authoritative current state — 2026-09-27 — EXP261 COMPLETE / EXP262 PREPARED

### EXP262 — accelerated 8-block sync batch — PREPARED / NOT RUN

**Hypothesis**
After the locally proven prefix through `0492/count11` and the locally captured next `04A6/count13`, acknowledge a bounded batch of eight exact controller-originated FC16 pages:
`04A6/13 -> 04BA/22 -> 04D8/27 -> 04F6/14 -> 050A/19 -> 051E/10 -> 0532/18 -> 0546/20`.
Then capture the first different FC16 or FC03 without answering it. Genuine Eco 5 predicts `055A/count33`.

**New active targets and known basis**
- `04A6/13`: locally observed immediately after the `0492` ACK in EXP261; also a recurrent genuine Eco 5 family, so context matters. A genuine gateway has ACKed this family in captured sessions.
- `04BA/22`, `04D8/27`, `04F6/14`, `050A/19`, `051E/10`, `0532/18`, `0546/20`: all observed in the genuine Eco 5 successful synchronization traffic.
- These are controller-originated FC16 export pages; the experiment sends only standard FC16 acknowledgements, not new register payload values. The known protocol effect is progression of the Online/Link session; direct application-setting effects are not established.
- Known incomplete-session side effect remains DHW-side literal `0` and `COMM. ERR ONLINE/LINK`; recovery is one normal Thermia-controller reboot.

**Fail-closed**
- Existing proven prefix remains unchanged.
- Each new page must be the first exact expected page, with exact count/bytecount/full length, within 5 s of the preceding ACK.
- Any retry, unexpected FC16/FC03, peer FC17/ACK, or post-return parser/drop delta stops further TX.
- After `0546/20` ACK: capture-only; no `055A` ACK and no mailbox response.
- Maximum active TX: one R1 plus seventeen exact FC16 ACKs.


## Authoritative current state — 2026-09-27 — EXP261 COMPLETE / STRONG POSITIVE

- Last completed experiment: **EXP261 — COMPLETE / STRONG POSITIVE**.
- No next experiment is prepared yet.
- **EXP239 remains OPEN.**
- **EXP238 remains PARKED / NOT RUN.**

### EXP261 hypothesis

Continue the proven local Online/Link prefix using a bounded three-block batch:
`046A/count18 -> ACK -> 047E/count19 -> ACK -> 0492/count11 -> ACK`,
then capture the first different FC16/FC03 stage without answering it.

The genuine Eco 5 reference commonly predicts `04A6/count13` next. Because `04A6/13` is also a recurrent passive family, this was treated as a prediction rather than a strict success requirement.

### EXP261 observed result

The complete observed sequence was:

`R1 -> 03E8/14 ACK -> 03FC/11 ACK -> 0410/22 ACK -> 042E/15 ACK -> 0442/13 ACK -> 0456/12 ACK -> 046A/18 ACK -> 047E/19 ACK -> 0492/11 ACK -> 04A6/13`

Key timings:
- first approval: +1245 ms after BUS_RETURN;
- 046A/18: +1433 ms after 0456 ACK;
- 047E/19: +722 ms after 046A ACK;
- 0492/11: +1480 ms after 047E ACK;
- first post-0492 frame: `04A6/count13`, +576 ms after the 0492 ACK.

Exact captured post-0492 request:
`0F1004A6000D1A0000000000000000000000000000000000000000402000000000CA9A`

It was not acknowledged.

Integrity:
- all planned one-shot ACKs through 0492 were used exactly once;
- no stage retries;
- no approval retry after R1;
- no unexpected peer FC17 / FC16 ACK;
- no post-return parser-resync or RX-drop delta in the experiment summary;
- DE returned LOW.

### Strong conclusion

EXP261 extends the local XTR match with the genuine Eco 5 Online/Link synchronization chain through `0492/count11`, and the first next block is exactly `04A6/count13`.

The bounded-batch method remains valid and materially reduces required controller restarts while preserving a clear fail-closed boundary.

Full Online/Link establishment remains unproven because `04A6` and all downstream pages/mailbox traffic remain unanswered.

### Side effects / recovery

Front-panel side effects for this specific EXP261 run have not yet been reported. Prior incomplete sessions repeatedly produced DHW-side `0` and `COMM. ERR ONLINE/LINK`. Continue to recover with one normal Thermia-controller reboot after summary.

---


## Authoritative current state — 2026-09-27 — EXP260 COMPLETE / EXP261 PREPARED / NOT RUN

- Last completed experiment: **EXP260 — COMPLETE / STRONG POSITIVE**.
- Current prepared experiment: **EXP261 — bounded three-block continuation `046A/18 -> 047E/19 -> 0492/11`, then capture-only — PREPARED / NOT RUN**.
- **EXP239 remains OPEN.**
- **EXP238 remains PARKED / NOT RUN.**

### EXP261 hypothesis

EXP260 proved the bounded-batch method works and extended the local XTR Online/Link sequence through exact `046A/count18`. EXP261 keeps all previously proven behavior unchanged and adds only three further one-shot FC16 ACKs, in the genuine Eco 5 order:

`046A/count18 -> ACK -> 047E/count19 -> ACK -> 0492/count11 -> ACK -> capture first different FC16/FC03`

The genuine Eco 5 capture commonly has `04A6/count13` after `0492/count11`, but `04A6/13` is also a recurrent passive family. EXP261 therefore treats `04A6/13` as the primary prediction, not as a required success condition. The first different post-0492 frame is captured and never answered.

### Exact new active targets

- `046A/count18` ACK: `0F 10 04 6A 00 12 60 06`
- `047E/count19` ACK: `0F 10 04 7E 00 13 E1 C2`
- `0492/count11` ACK: `0F 10 04 92 00 0B 20 3D`

All three are standard FC16 ACKs carrying no register-value payload.

### EXP261 fail-closed boundary

Each new ACK is permitted only for the first exact expected FC16 block, within 5 s of the immediately preceding ACK, with no prior stage retry, no unexpected peer response, and unchanged post-BUS_RETURN parser/RX-drop counters. All one-shot latches close before DE is enabled.

After the single `0492` ACK:
- no `04A6` ACK;
- no later FC16 ACK;
- no FC03/mailbox response;
- first different FC16 or any FC03 is captured and the experiment stops;
- 15 s capture timeout if no different stage appears.

Known side effect remains the reproducible DHW-side literal `0`, often followed by `COMM. ERR ONLINE/LINK`, after deliberately incomplete sessions. Recovery is one normal Thermia-controller reboot after summary.

### Build validation

- YAML syntax parsed successfully with ESPHome custom tags tolerated.
- `${device_name}` and `${friendly_name}` are the only substitutions referenced and both are defined.
- All YAML IDs are unique and all `id(...)` references resolve.
- Exactly ten DE-enable/UART TX paths exist: R1 plus nine exact FC16 ACKs through `0492`.
- All nine FC16 ACK CRCs validate.
- CRC-valid-frame bus-health bookkeeping remains present.
- ESPHome compile was **not run** because the ESPHome CLI is unavailable.

---


## Authoritative current state — 2026-09-27 — EXP260 COMPLETE / STRONG POSITIVE

- Last completed experiment: **EXP260 — COMPLETE / STRONG POSITIVE**.
- Hypothesis: continue the proven local Online/Link prefix with a bounded three-block ACK batch `042E/15 -> 0442/13 -> 0456/12`, then capture only. Genuine Eco 5 predicts `046A/count18` next.
- Observed local sequence: `R1 -> 03E8/14 ACK -> 03FC/11 ACK -> 0410/22 ACK -> 042E/15 ACK -> 0442/13 ACK -> 0456/12 ACK -> 046A/18`.
- Timing after previous ACK: `042E` +695 ms after `0410` ACK; `0442` +1502 ms after `042E` ACK; `0456` +566 ms after `0442` ACK; `046A` +1473 ms after `0456` ACK.
- `046A/count18` was captured and **not acknowledged**.
- Integrity: approval retries after R1=0; all same-block retry counters=0; no unexpected peer FC17/FC16 ACK; post-return parser-resync delta=0; RX-drop delta=0; DE LOW at summary.
- User reports the DHW-side literal **`0` appeared again** during/after EXP260. `COMM. ERR ONLINE/LINK` has not yet been reported for this run. Do not wait for the alarm; recovery remains one normal controller reboot after the summary.
- Strong conclusion: the local XTR now matches the genuine Eco 5 ordered Online/Link sync through `046A/count18`. The bounded batch method worked without losing causal order.
- Full Online/Link session establishment remains unproven.
- No next experiment is prepared yet.
- **EXP239 remains OPEN. EXP238 remains PARKED / NOT RUN.**

## Authoritative current state — 2026-09-27 — EXP259 COMPLETE / EXP260 PREPARED / NOT RUN

- Last completed experiment: **EXP259 — COMPLETE / STRONG POSITIVE**.
- EXP259 reproduced the genuine Eco 5 ordered prefix through `042E/count15`; user confirmed DHW-side `0` and `COMM. ERR ONLINE/LINK` again after the deliberately incomplete session.
- Current prepared experiment: **EXP260 — bounded three-block sync batch — PREPARED / NOT RUN**.
- **Hypothesis:** after the proven local prefix `R1 -> 03E8/14 ACK -> 03FC/11 ACK -> 0410/22 ACK -> 042E/15`, acknowledging the next three exact genuine-Eco5 blocks `042E/15`, `0442/13`, and `0456/12` in order will advance the XTR to `046A/count18`.
- **Only new experimental variable family:** a bounded batch of three exact standard FC16 ACKs for those already-observed reference stages.
- Maximum experimental TX: **7 frames** total: R1 + proven ACKs `03E8`, `03FC`, `0410` + new batch ACKs `042E`, `0442`, `0456`.
- Fail-closed: every stage must be the first exact expected block, within 5 s, parser/drop clean, with no approval retry, previous-page retry, FC03, unexpected peer FC17, or unexpected peer FC16 ACK.
- After the one `0456/count12` ACK, capture only. Genuine Eco 5 predicts `046A/count18`; **do not ACK `046A`**.
- No FC03/mailbox response and no downstream full-chain emulation in EXP260.
- Known side effect remains DHW-side `0` + `COMM. ERR ONLINE/LINK`; one normal controller reboot is required after summary.
- Run only after the prior alarm and DHW-side `0` have cleared following recovery reboot.
- **EXP239 remains OPEN. EXP238 remains PARKED / NOT RUN.**

### EXP260 exact new ACK frames

- `042E/count15`: `0F 10 04 2E 00 0F E0 1A` (CRC `0x1AE0`, wire `E0 1A`)
- `0442/count13`: `0F 10 04 42 00 0D A1 C6` (CRC `0xC6A1`, wire `A1 C6`)
- `0456/count12`: `0F 10 04 56 00 0C 20 02` (CRC `0x0220`, wire `20 02`)

### Build validation

- YAML syntax parsed successfully with ESPHome custom tags tolerated.
- Only `${device_name}` and `${friendly_name}` are referenced and both are defined.
- All YAML IDs are unique and every `id(...)` reference resolves.
- Exactly seven UART TX / DE-enable paths exist.
- CRC-valid-frame bus-health bookkeeping remains present.
- ESPHome compile was **not run** because the ESPHome CLI is unavailable in this environment.

---

## EXP259 UI side-effect confirmation — 2026-09-27

- EXP259 is **COMPLETE / STRONG POSITIVE**.
- User confirmed the same front-panel side effects again after the incomplete active Online/Link session:
  - DHW-side literal `0`;
  - exact alarm `COMM. ERR ONLINE/LINK`.
- This repeats the EXP252/EXP256 failure mode while the controller is progressively serviced farther into the genuine Online/Link FC16 sync chain.
- Strong conclusion: the visible side effect is reproducibly associated with entering the Online/Link session and then leaving it incompletely serviced.
- Hypothesis, still not formally proven: the alarm is the controller timing out an approved but incompletely serviced Online/Link session.
- Recovery remains one normal Thermia-controller reboot before any further active test.
- To keep the remaining reboot count practical, future experiments may acknowledge small, pre-verified batches of the genuine Eco 5 FC16 sequence, with fail-closed stop on the first unexpected block. Do not jump directly to full-chain/mailbox emulation.

## Authoritative current state — 2026-09-27 — EXP259 COMPLETE / STRONG POSITIVE

- Last completed experiment: **EXP259 — COMPLETE / STRONG POSITIVE**.
- **EXP239 remains OPEN.**
- **EXP238 remains PARKED / NOT RUN.**
- No next experiment is prepared yet.

### EXP259 hypothesis

After the locally proven chain `R1 -> 03E8/count14 ACK -> 03FC/count11 ACK -> 0410/count22`, send exactly one standard FC16 ACK for the first exact `0410/count22` block, then capture the first different FC16/FC03 stage without answering it. The genuine Eco 5 reference predicted `042E/count15`.

### EXP259 observed result

Observed sequence:
- BUS_RETURN
- first approval at +1283 ms
- R1 sent once
- `03E8/count14` at +138 ms after R1; ACKed once
- `03FC/count11` at +682 ms after 03E8 ACK; ACKed once
- `0410/count22` at +1498 ms after 03FC ACK; ACKed once
- `042E/count15` at +696 ms after 0410 ACK
- `042E` was **not** acknowledged

Exact first different request:
`0F10042E000F1E000100010000000AFFF60005001E0000002D0000000000000000000000003A99`

Decoded header:
- slave `0x0F`
- FC16
- start `0x042E`
- count `15`
- bytecount `30`

Payload words:
`0001 0001 0000 000A FFF6 0005 001E 0000 002D 0000 0000 0000 0000 0000 0000`

Safety/integrity summary:
- R1 used: 1
- 03E8 ACK: 1
- 03FC ACK: 1
- 0410 ACK: 1
- approval retries after R1: 0
- 03E8 retries after ACK: 0
- 03FC retries after ACK: 0
- 0410 retries after ACK: 0
- unexpected peer frames: 0
- post-return parser resync delta: 0
- post-return RX-drop delta: 0
- DE LOW
- no FC03/mailbox response
- no ACK beyond `0410`

### Strong conclusion

The local XTR now reproduces the genuine Eco 5 ordered Online/Link synchronization prefix through four consecutive FC16 pages:

`approval response -> 03E8/14 -> ACK -> 03FC/11 -> ACK -> 0410/22 -> ACK -> 042E/15`

This is the third consecutive bounded positive progression after EXP256–258 and strongly supports that the replayed R1 enters the native Online/Link synchronization state machine.

Full Online/Link establishment remains unproven because `042E` and all later blocks/mailbox traffic were deliberately left unanswered.

### UI / recovery

The EXP259 log itself does not report the front-panel UI. As with EXP252/256/258, an incomplete approved session may again lead to DHW-side `0` and/or `COMM. ERR ONLINE/LINK`; exact EXP259 UI outcome awaits user confirmation. Perform one normal Thermia-controller reboot after this run.

---

## Authoritative current state — 2026-09-27 — EXP258 COMPLETE / EXP259 PREPARED / NOT RUN

- Last completed experiment: **EXP258 — COMPLETE / STRONG POSITIVE**.
- Current prepared experiment: **EXP259 — R1 + exact `03E8/count14` ACK + exact `03FC/count11` ACK + exact `0410/count22` ACK + next-stage capture — PREPARED / NOT RUN**.
- **EXP239 remains OPEN.**
- **EXP238 remains PARKED / NOT RUN.**

### EXP259 hypothesis

EXP258 locally proved the ordered prefix `R1 -> 03E8/14 ACK -> 03FC/11 ACK -> 0410/22`. EXP259 changes one active variable only: acknowledge that already-proven exact `0410/count22` request once, then capture the first different FC16/FC03 stage without answering it. The genuine Eco 5 reference predicts `042E/count15` next.

### Exact new active target

- Required request: slave `0x0F`, FC16, start `0x0410`, count `22` (`0x0016`), bytecount `44` (`0x2C`), full request length `53` bytes.
- Exact standard FC16 ACK: `0F 10 04 10 00 16 40 1C`.
- CRC16 over `0F1004100016` is `0x1C40`, transmitted little-endian `40 1C`.
- The ACK carries no register-value payload; it echoes only start/count.

### EXP259 fail-closed boundary

Maximum experimental TX is four frames: one R1, one exact `03E8/14` ACK, one exact `03FC/11` ACK and one exact `0410/22` ACK. The new `0410` ACK is allowed only after the proven prefix, only when the first post-`03FC`-ACK FC16 is exact `0410/22`, within 5 s, with unchanged parser/drop counters, no approval/03E8/03FC retry, and no unexpected peer frame. All one-shot latches close before DE is enabled.

After the one `0410` ACK:
- no second `0410` ACK;
- no ACK of `042E` or any later FC16;
- no FC03/mailbox response;
- first different FC16 or any FC03 is captured and the experiment stops;
- 15 s timeout if only `0410` retries continue.

Known reproducible side effect remains the DHW-side `0` plus `COMM. ERR ONLINE/LINK` after an incomplete approved Online/Link session. **Do not run EXP259 until one normal controller reboot has cleared both after EXP258.** After EXP259 summary, reboot the Thermia controller once again.

### Build validation

- YAML syntax parsed successfully with ESPHome custom tags tolerated.
- `${device_name}` and `${friendly_name}` are the only substitutions referenced and both are defined.
- All 138 YAML IDs are unique and all `id(...)` references resolve.
- Exactly four DE-enable / UART TX call sites exist: R1, `03E8` ACK, `03FC` ACK, `0410` ACK.
- CRC-valid-frame bus-health bookkeeping is unchanged.
- ESPHome compile was **not run** because the ESPHome CLI is not installed in the available environment.

---


## Authoritative current state — 2026-09-27 — EXP258 COMPLETE / STRONG POSITIVE

- Last completed experiment: **EXP258 — COMPLETE / STRONG POSITIVE**.
- No next experiment is yet prepared.
- **EXP239 remains OPEN.**
- **EXP238 remains PARKED / NOT RUN.**

### EXP258 hypothesis

After the already-proven local prefix `R1 -> 03E8/count14 -> ACK -> 03FC/count11`, acknowledge exactly the first `03FC/count11` FC16 request once and capture the first different FC16/FC03 stage without answering it. Genuine Eco 5 reference predicts `0410/count22`.

### EXP258 observed facts

- BUS_RETURN occurred after the controller power-cycle; two parser resync events happened exactly at the return edge, while the experiment summary recorded `resync_postreturn=0` and `drop_postreturn=0`.
- First approval request: **+1243 ms after BUS_RETURN**.
- R1 sent exactly once; no approval retry after R1.
- First post-R1 `03E8/count14`: **+138 ms after R1**.
- Exact `03E8/count14` ACK sent once: `0F 10 03 E8 00 0E C0 93`.
- First post-03E8-ACK block: exact `03FC/count11` at **+691 ms**.
- Exact `03FC/count11` ACK sent once: `0F 10 03 FC 00 0B 40 94`.
- First post-03FC-ACK different block: exact **`0410/count22` at +1501 ms**.
- `0410/count22` was captured and **not acknowledged**.
- Summary: `r1=1 ack03e8=1 ack03fc=1 approvals=1 approval_after_r1=0 post_r1_fc16=1 post_03e8_fc16=1 same03e8_after_ack=0 same03fc_after_ack=0 peer17=0 unexpected_peer_ack=0 self_echo_r1=0 self_echo_ack=0 resync_postreturn=0 drop_postreturn=0 DE=LOW`.
- User reports the DHW/tank-side literal **`0` reappeared** and the same **`COMM. ERR ONLINE/LINK`** alarm appeared again.

Exact captured `0410/count22` request:

`0F10041000162C0028000A0037000000000000000200120028001E003C00120014002F001E00070000003C000D00060037000088E3`

### Strong conclusions

- EXP258 locally reproduces the genuine Eco 5 synchronization prefix one step further: `R1 -> 03E8/14 -> ACK -> 03FC/11 -> ACK -> 0410/22`.
- The Eco 5 prediction for the third ordered sync block is therefore confirmed on the XTR.
- The replayed R1 is sufficient to move the XTR through at least the first three native Online/Link synchronization stages when the expected FC16 ACKs are supplied.
- The repeated DHW-side `0` + exact `COMM. ERR ONLINE/LINK` after EXP252/256/258 remains consistent with an approved but incompletely serviced Online/Link session timing out; this causal explanation is now stronger but still not proven.

### Unknowns / safety

- Full Online/Link establishment is still unproven.
- `0410/count22` and all later FC16 pages remain unacknowledged locally.
- No local `0708/count6` mailbox response has been provided.
- Do not broaden directly to full-chain ACK + mailbox emulation in one step.
- Recovery after EXP258 remains one normal controller reboot; confirm the `0` and alarm clear before another active test.

---

## Authoritative current state — 2026-09-27 — EXP257 COMPLETE / EXP258 PREPARED / NOT RUN

- Last completed experiment: **EXP257 — COMPLETE / STRONG POSITIVE**.
- Current prepared experiment: **EXP258 — R1 + exact `03E8/count14` ACK + exact `03FC/count11` ACK + next-stage capture — PREPARED / NOT RUN**.
- **EXP239 remains OPEN.**
- **EXP238 remains PARKED / NOT RUN.**

### EXP258 hypothesis

EXP257 locally proved `R1 -> 03E8/count14 -> ACK -> 03FC/count11`. EXP258 changes one active variable only: acknowledge that already-proven exact `03FC/count11` request once, then capture the first different FC16/FC03 stage without answering it. The genuine Eco 5 reference predicts `0410/count22` next.

### Exact new active target

- Required request: slave `0x0F`, FC16, start `0x03FC`, count `11` (`0x000B`), bytecount `22` (`0x16`), full request length `31` bytes.
- Exact standard FC16 ACK: `0F 10 03 FC 00 0B 40 94`.
- CRC16 over `0F1003FC000B` is `0x9440`, transmitted little-endian `40 94`.
- The ACK carries no register-value payload; it echoes only start/count.
- The same ACK frame is present in the genuine Eco 5 raw capture.

### EXP258 fail-closed boundary

Maximum experimental TX is three frames: one R1, one exact `03E8/count14` ACK, one exact `03FC/count11` ACK. The new `03FC` ACK is allowed only after the proven prefix, only when the first post-`03E8`-ACK FC16 is exact `03FC/11`, within 5 s, with unchanged parser/drop counters, no approval retry, no `03E8` retry, and no unexpected peer frame. All one-shot latches close before DE is enabled.

After the one `03FC` ACK:
- no second `03FC` ACK;
- no ACK of `0410` or any later FC16;
- no FC03/mailbox response;
- first different FC16 or any FC03 is captured and the experiment stops;
- 15 s timeout if only `03FC` retries continue.

Known possible side effect remains an incomplete Online/Link session with DHW-side `0` and/or `COMM. ERR ONLINE/LINK`; recovery is one normal Thermia-controller reboot after the summary.

### Build validation

- YAML syntax parsed successfully with ESPHome custom tags tolerated.
- `${device_name}` and `${friendly_name}` are the only substitutions referenced and both are defined.
- All `id(...)` references resolve to defined YAML IDs; no duplicate IDs found.
- Exactly three DE-enable / UART TX call sites exist: R1, `03E8` ACK, `03FC` ACK.
- CRC-valid-frame bus-health bookkeeping remains present and unchanged.
- ESPHome compile was **not run** because the ESPHome CLI is not installed in the available environment.

---

## External Eco 5 follow-up after EXP257 — 2026-09-27

The new public-comment analysis has been cross-checked against the full raw Eco 5 capture. It materially refines the reference behavior but does not change the EXP257 result.

Observed from the raw capture:
- three cold-start approval windows begin with the first `071C/0730` request at **+1.199 s, +1.202 s, and +1.210 s** after bus return; this matches the local XTR EXP248/249/256/257 ~+1.28 s startup phase closely;
- with the genuine gateway attached, the two successful approval responses occur at **+120.153 s** and **+119.808 s** after bus return, after 29 challenge requests each;
- the no-gateway middle run was power-cycled after only ~174 s, with 41 unanswered challenges through +171.230 s, so it cannot test the local ~267 s / 63-request natural stop;
- the already-running steady-state segment before the first power-off contains no `071C/0730` traffic, so absence in steady-state captures does not prove a model lacks the cold-start approval stream;
- only two answered challenges exist, so challenge-repeat determinism and response stability across power cycles remain **unknown**; the one duplicated challenge in the capture was unanswered.

### Gateway behavior after approval

The genuine Eco 5 endpoint ACKs the controller's FC16 transfer blocks and the stable prefix is:

`03E8/14 -> ACK -> 03FC/11 -> ACK -> 0410/22 -> ACK -> 042E/15 -> ...`

The broad controller-export sequence then continues through the known 0x03E8..0x0864 range. `04A6/13` and `085F/5` are recurrent passive families overlaid on that transfer; their ACK timing differs between power-ups and they are **not supported as approval preconditions**. Do not treat their interleaving position as a required ordered sync step.

The first `0708/count6` mailbox poll occurs while the FC16 transfer is still in progress:
- first successful power-up: **+158.393 s** after bus return; the first poll is unanswered, the next poll is answered;
- second successful power-up: **+186.828 s** after bus return and is answered immediately.

**Raw-frame correction:** the repeated post-approval idle mailbox response in the public capture is `0F 03 0C 0000 0000 0000 0000 0001 0000 ...`, i.e. six Modbus words `0000 0000 0000 0000 0001 0000`. A comment transcribed the fifth word as `0100`; the raw bytes support `0001` in standard Modbus register order.

Later in the second successful session the fifth mailbox word is observed at `03DC` (988), then 984, 976, 908, 896, 768, 512, and finally 0. This is an **observed countdown-like sequence**. Interpreting it as pending sync-item count remains a hypothesis.

### Next bounded candidate

**EXP258 — candidate / NOT PREPARED.** Hypothesis: after the already-proven `R1 -> 03E8/14 ACK -> 03FC/11`, one exact standard ACK to the first local `03FC/count11` should advance the XTR to `0410/count22`, matching both successful genuine Eco 5 sessions. Stop on the first different block and do not ACK `0410`.

Do **not** jump directly to ACKing the entire chain or answering `0708`; that would change multiple active variables at once and would lose the clean discriminator established by EXP256-257.


## Authoritative current state — 2026-09-27 — EXP257 COMPLETE / STRONG POSITIVE

- Last completed experiment: **EXP257 — COMPLETE / STRONG POSITIVE**.
- **EXP239 remains OPEN.**
- **EXP238 remains PARKED / NOT RUN.**
- No next experiment is yet authorized/prepared.

### EXP257 hypothesis

After the same guarded one-shot R1 used in EXP256, acknowledge exactly the **first** post-R1 `0x0F FC16 03E8/count14` request once. Then observe the first different `0x0F` FC16/FC03 stage without answering it.

The full genuine Eco 5 gateway capture predicted `03FC/count11` as the immediate next stage.

### EXP257 observed result

The complete experiment sequence was:

```text
BUS_RETURN
  -> +1285 ms approval request 071C/0730
  -> R1 sent once
  -> +130 ms first post-R1 FC16 03E8/count14
  -> one exact FC16 ACK 0F1003E8000EC093
  -> +691 ms first different post-ACK block FC16 03FC/count11
  -> NO ACK
  -> SUMMARY NEXT_STAGE_FC16
```

Exact first different request:

`0F1003FC000B160028000A0037000000000000000200120028001E003C369E`

Decoded FC16 header:
- slave `0x0F`
- function `0x10`
- start `0x03FC`
- count `11`
- bytecount `22`

Payload words:
`0028 000A 0037 0000 0000 0000 0002 0012 0028 001E 003C`

Safety/integrity summary:
- R1 used: `1`
- one `03E8` ACK used: `1`
- approvals: `1`
- approval retries after R1: `0`
- same-`03E8` retries after ACK: `0`
- unexpected peer FC17: `0`
- unexpected peer FC16 ACK: `0`
- self echo R1/ACK: `0/0`
- post-return parser resync delta: `0`
- post-return RX-drop delta: `0`
- DE returned LOW
- `03FC/count11` was **not acknowledged**

### Strong conclusion

EXP257 reproduces the same post-approval synchronization prefix as the genuine Eco 5 reference:

`approval response -> 03E8/count14 -> ACK -> 03FC/count11`

This is a second independent XTR-to-Eco5 architecture match after EXP256 first established `approval response -> 03E8/count14`.

The result strongly supports that the replayed R1 is sufficient to advance the local XTR through at least the first two native controller->Online/Link synchronization stages. It still does **not** prove full Online/Link session establishment, because `03FC` and all downstream stages/mailbox traffic were deliberately left unanswered.

### Comparison with genuine Eco 5

The full Eco 5 capture shows the same prefix twice, then continues:

`03E8/14 -> ACK -> 03FC/11 -> ACK -> 0410/22 -> ...`

EXP257 stopped exactly at `03FC/11`, as intended. Therefore the next protocol question is whether acknowledging this exact `03FC/count11` on the XTR yields `0410/count22`, but no such next experiment has yet been run or authorized.

### UI / recovery status

The protocol objective is complete from the supplied log. Front-panel side effects for this run have not yet been reported. Because EXP252/EXP256 showed the recoverable DHW-side `0` / `COMM. ERR ONLINE/LINK` failure mode after incomplete Online/Link participation, perform one normal controller reboot after this EXP257 capture if not already done.

## Authoritative current state — 2026-09-27 — EXP256 COMPLETE / EXP257 PREPARED / NOT RUN

- Last completed experiment: **EXP256 — COMPLETE / ACTIVE STRONG POSITIVE**.
- Current prepared experiment: **EXP257 — ONE-SHOT R1 + SINGLE `03E8/count14` ACK + NEXT-STAGE CAPTURE — PREPARED / NOT RUN**.
- **EXP239 remains OPEN.**
- **EXP238 remains PARKED / NOT RUN.**

### EXP257 hypothesis

EXP256 proved the sequence `071C/0730 approval -> one R1 -> approval retries stop -> FC16 03E8/count14 repeats`. EXP257 changes one variable only: after the same guarded one-shot R1, send **one standard FC16 ACK** to the first exact post-R1 `03E8/count14` request, then observe the first different FC16/FC03 stage without answering it.

The complete genuine Eco 5 capture now makes `03FC/count11` the external-reference prediction for the immediate next stage after the `03E8/count14` ACK. Prior local EXP137 evidence still shows `0410/count22` later in progression; EXP257 does not require or ACK either block.

### New active target and known effects

- Required request: slave `0x0F`, FC16, start `0x03E8`, count `14`, bytecount `28`, length `37`.
- Single ACK frame: `0F 10 03 E8 00 0E C0 93`.
- The ACK echoes only address/count and contains **no register-value payload**.
- CRC16 over `0F1003E8000E` is `0x93C0`, transmitted little-endian `C0 93`.
- Genuine Eco 5 full capture shows `03E8/14 ACK -> 03FC/11 -> 0410/22` in two independent successful approval cycles.
- EXP137 previously showed locally that ACKing exact `03E8/count14` reaches `0410/count22`, but did not prove there was no intervening `03FC/11`.
- Possible side effect remains an incomplete Online/Link session with DHW-side `0` and later `COMM. ERR ONLINE/LINK`; recovery is one normal controller reboot.

### EXP257 fail-closed boundary

The `03E8` ACK is permitted only when R1 has already been sent once, there was no approval retry, the **first** post-R1 FC16 is exact `03E8/14/bytecount28/len37`, it arrives within 5 s of R1, parser/drop counters remain unchanged since BUS_RETURN, and no unexpected peer FC17/FC16 ACK was observed. The ACK latch closes before DE is enabled.

After that one ACK:
- no second `03E8` ACK;
- no ACK for `03FC`, `0410`, or any other FC16;
- no FC03/mailbox/desired-state response;
- first different FC16 or any FC03 is captured and the experiment stops;
- otherwise a 15 s post-ACK timeout records a negative result.

### Run prerequisite and recovery

Do not run EXP257 until the controller has recovered from EXP256: `COMM. ERR ONLINE/LINK` absent, DHW-side `0` cleared, then healthy normal traffic for at least 15 s. After EXP257 capture/summary, perform one normal controller reboot immediately.

### Build validation

- YAML syntax parsed successfully with ESPHome custom tags tolerated.
- `${device_name}` and `${friendly_name}` are the only substitutions referenced and both are defined.
- All 124 `id(...)` references have matching YAML `id:` definitions.
- Only two DE-enable TX call sites exist: one R1 script and one exact `03E8` ACK script.
- CRC-valid-frame bus-health bookkeeping is unchanged.
- ESPHome compile was **not run** because the ESPHome CLI is not installed in the available environment.

## External Eco 5 full-capture refinement — 2026-09-27 — BEFORE EXP257

The complete genuine iTec Eco 5 gateway capture materially sharpens the expected post-approval state machine without changing the bounded EXP257 TX plan.

Observed across the 1482.480 s capture:
- 99 exact `0x0F FC17 read 0730/count8 + write 071C/count8` approval requests occurred in three retry windows: 29 requests (`184.661..303.554 s`), 41 requests (`394.976..565.004 s`), and 29 requests (`604.688..723.223 s`).
- Median retry cadence in those windows is approximately 4.24 s / 4.26 s / 4.21 s.
- 98/99 16-byte `071C` payloads are unique; one payload repeats once. Therefore the genuine Eco 5 challenge value is normally regenerated between retries rather than held constant.
- Successful pair 1 is directly present in the raw capture: `C1=63CEFB32C6F41382087992370CACEEBA` -> `R1=1691A5F3F8E8D58738924416E8E6A3D5`.
- Successful pair 2 is also directly present: `C2=31FB59FC8FB1175CD89F904D06D92EA4` -> `R2=FD636CCD0F921D83FF232A1A2413B372`.

Both successful responses are followed by the same acknowledged sync prefix:

```text
FC17 response
  -> +92 ms  FC16 03E8/count14
  -> ACK 03E8/count14
  -> FC16 03FC/count11
  -> ACK 03FC/count11
  -> FC16 0410/count22
  -> ACK 0410/count22
  -> ... broader ordered sync ...
```

Timing is highly reproducible:
- R1 cycle: `03E8` at +92 ms, ACK at +137 ms, `03FC` at +510 ms, `0410` at +1.950 s.
- R2 cycle: `03E8` at +92 ms, ACK at +122 ms, `03FC` at +536 ms, `0410` at +2.189 s.

The first successful cycle then progresses through the ordered controller-export chain:

`03E8/14 -> 03FC/11 -> 0410/22 -> 042E/15 -> 0442/13 -> 0456/12 -> 046A/18 -> 047E/19 -> 0492/11 -> 04A6/13 -> 04BA/22 -> 04D8/27 -> 04F6/14 -> 050A/19 -> 051E/10 -> 0532/18 -> 0546/20 -> 055A/33 -> 057B/33 -> 059C/33 -> 05BD/33 -> 05DE/33 -> 05FF/33 -> 0620/33 -> 0641/33 -> 0662/33 -> 0683/33 -> 06A4/33 -> 06C5/33 -> 06EA/7 -> 06F1/3 -> 06F4/19`, followed by `07D0/19` and the `0708/count6` mailbox/runtime phase.

**EXP257 consequence:** the external Eco 5 reference now predicts `03FC/count11` as the immediate next block after the single `03E8/count14` ACK. Prior local EXP137 evidence still records that `0410/count22` appears after a `03E8` ACK, but did not establish that it is the first intervening block. EXP257 remains necessary to determine the local XTR ordering. Its active behavior does not need to broaden: ACK only `03E8` once, capture the first different block, and stop.

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