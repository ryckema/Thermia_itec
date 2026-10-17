# 2026-10-17 — V5DCM4–V5DCM7 offline investigations

**Source and scope:** seven existing historical Thermia / collaborator iTec Eco5 text-format RTU captures, already made available to the project; no live XTR test, no genuine DCM device required. User's known-good V5DCM2 FIX1 ESPHome/HA build remains unchanged; no physical TX or YAML edits.

## V5DCM4 — real-record parsing and V5DCM3 normalized model replay
**Status: COMPLETE / POSITIVE** for bounded replay; **INCONCLUSIVE** for acceptance.
- **Hypothesis:** 7 real text captures can be parsed with Modbus RTU CRC and fed as typed events into an offline V5DCM3-equivalent recorder without counter mismatch.
- **Baseline:** V5DCM3 5 synthetic host fixture tests; live V5DCM2 FIX1 RX-only.
- **Controlled change:** offline parse and replay only; CRC16(Modbus), request-vs-reply geometry, separate slave and function, stable timestamps, no payload publication.
- **Result:** 25,031/25,031 frame records CRC-valid in the seven supplied files; 7/7 normalized V5DCM3 event counter consistency for FC16 requests/FC23 and ordering counts. This is text-record validation, **not** an independently verified electrical trace.
- **Positive:** records and counters consistent, achieved. **Negative:** corrupted records or classification mismatch, not found. **Abort:** uncertain source identity promoted to XTR proof, no hardware action. **Recovery:** offline discard; live remains V5DCM2 FIX1.

## V5DCM5 — historical FC23 pairing and timing
**Status: COMPLETE / POSITIVE** for bounded timing, **INCONCLUSIVE** for bus sender/slot/acceptance.
- **Hypothesis:** geometrically exact native 0x0F FC23 0730/8-read, 071C/8-write request can be associated with later response-shaped record at text-record resolution, but timestamps do not establish physical direction or acceptance.
- **Baseline:** CRC-positive V5DCM4.
- **Controlled change:** offline pair consecutive native challenge and reply-shaped records inside 200ms; do not derive private response bytes.
- **Results:** Oct-03 capture: 1 exact request at 27.400s and response-shaped record at 27.429s, delta 29ms. Eco5 Sep-26: 99 exact challenge requests, 2 response-shaped records, 2 bounded pairs (61 and 63ms). Eco5 Sep-28: 64 challenges, 4 response-shaped records, 4 pairs (first three 46, 30, 32ms). Eco5 median challenge request cadence ~4.2335s and ~4.241s respectively; long gaps also exist. In four earlier Thermia captures no exact challenge appeared.
- **Positive:** bounded pairs/counts, achieved. **Negative:** no observable pair (absence must be captured as absence). **Abort:** treating text frame timestamp as wire-end, independent sender proof or active response slot. **Recovery:** offline.

## V5DCM6 — configuration ordering and profile variability
**Status: COMPLETE / POSITIVE** for evidenced shape differences, **INCONCLUSIVE** for universal XTR bootstrap requirements.
- **Hypothesis:** historical profiles differ in FC16 address/count and strict 32-page sequences cannot be inferred from normal repeated first page.
- **Baseline:** V5DCM4 classified native request records and V5DCM3 32-start historical reference list.
- **Controlled change:** offline compare start+count and consecutive reference-start sequence length.
- **Results:** Oct-03 historic trace has 32 reference starts, from 03E8/count13 through 06F4/count19, between 29.262–61.461s (32.199s). Sep-25 09:05 capture shows 31 starts 03E8/13 through 06F1/3, with no 06F4 in that capture. Sep-25 09:02 capture starts at 042E (partial-window). Eco5 records contain 03E8/count14 and other altered per-page counts (e.g. 0410/count22), whereas older traces show 03E8/count13, 0410/count21. Recently observed live XTR count14 does not establish shared semantics across capture provenance. Permissive V5DCM3 cursor across Eco5 long streams counts completed sequences, while a stricter single uninterrupted reference-run test detects zero complete uninterrupted runs in those files. This is a model limitation / false-positive risk, NOT proof Eco5 never completed a legitimate protocol exchange.
- **Positive:** profile-dependent shapes and complete/partial subsequences, achieved. **Negative:** no proven universal mapping; do not promote sequence status to accepted state. **Abort:** treating 32 starts as unconditional controller requirement. **Recovery:** offline.

## V5DCM7 — falsify premature session acceptance
**Status: COMPLETE / POSITIVE** for specific guard/counterexamples, **INCONCLUSIVE** for true vendor state rules.
- **Hypothesis:** mailbox poll or long accumulated bootstrap cursor alone is insufficient evidence for handshake acceptance, controller DCM icon or Internet Online.
- **Baseline:** V5DCM3 model + V5DCM6 stricter sequence audit.
- **Controlled change:** compare time windows with mailbox activity and no FC23; check cursor-complete vs uninterrupted-run signals.
- **Results:** Sep-24 21:00 capture shows 11 native 0708/count6 **request-shaped** polls and zero exact FC23 requests in window. Sep-25 09:05 capture: first mailbox request at 0.987s, first configuration 03E8 at 68.304s, no exact FC23 in window. These prove that FC23 **need not be visible in the same text capture** for mailbox activity; previous out-of-window handshake cannot be ruled out. An FC03 response does not carry its register address, so reply attribution requires same-session correlation. Across Eco5 long streams an accumulated cursor can pass 32 without proving a single bounded session.
- **Positive:** counterexamples and observer overclaim exposed, achieved. **Negative:** no explanatory evidence in files, not the case. **Abort:** infer handshake absent globally or claim display state. **Recovery:** offline redesign recommended.

## Source and evidence classification
- **Observed in historical captures:** CRC-correct record shapes, timing differences and interleaving; not proof of physical sender or wire-end.
- **Firmware-derived:** separate Connect CM930 application handshake states and conditional package requests; not locally proven XTR behavior.
- **Strong conclusion:** do not derive authenticated, Online or physical TX permission from FC16 ACK, 0708 poll, long config cursor or response-shaped text frame.
- **Unknown:** local live FC23 on XTR, TX ownership/slot, acceptance response, DCM icon and Online criteria. Historical capture provenance must remain explicit.

## Test validation and safety
Five offline replay assertions groups pass covering 7 capture integrity, FC23 timing, 31/32 ordered run, cross-model count differences and normalized V5DCM3 event-state parity. No ESPHome compilation or live test occurred; no hardware rollback needed. The local study pack includes Python parser, anonymous event metadata, derived JSON, reports and test output. Private authentication code and mailbox command tooling are not published.

## Next
**V5DCM8 — PREPARED / NOT RUN:** offline provenance-aware state observer, flagging independent observation, bounded correlation, epoch qualification, genuine vendor acceptance, DCM icon and Online. Baseline V5DCM4–7 and V5DCM2 FIX1 stable production. Positive: no false-positive acceptance from repeated traffic; negative: mismatch against genuine capture event counts; abort unknown sender/slot escalation or TX; recovery offline revert observer, retain V5DCM2 FIX1.

