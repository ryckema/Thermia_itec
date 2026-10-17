# V5DCM16 — historical native CM930 session reconstruction (2026-10-17)

**Status:** COMPLETE / POSITIVE for bounded offline replay and 14 explicit checks; COMPLETE / INCONCLUSIVE for XTR native DCM acceptance, independent sender, controller epoch, icon and cloud Online. No live test or new ESPHome YAML, TX remains HARD_DENY.

## Hypothesis, baseline, controlled change

Hypothesis: proven identical RAUC 2.0.18 / 2.1.105 request flag ranges (V5DCM15A), combined with historical FC23 pairs and strict 32-reference-start frames, permit a bounded session-candidate reconstruction while preserving unknown source/acceptance.

Baseline: V5DCM4–8 seven CRC-validated records, V5DCM13–15 firmware-derived state distinctions, V5DCM15A original flag identity and profile-difference proof; user-flashed V5DCM2 FIX1 RX-only.

Controlled change: purely offline reread seven supplied text logs, CRC16 check ADU, classify exact 0x0F FC23 request shape and reply shape, one-to-one candidate pairing within 200 ms, reference page progression. Original frame payloads are processed locally in memory but not reproduced or published. No native responder, mailbox tooling, physical TX or altered production configuration.

## Results

- **25,031 / 25,031** original text-record Modbus CRCs valid; **164** exact native 0x0F FC23 challenge request shapes and **7** reply-shaped records time-paired within 200 ms. The other **157** requests are unpaired *in the records*; this is not negative protocol evidence.
- Oct-03 native request at **27.400 s**; reply-shaped record **27.429 s** (29 ms). First reference configuration frame at **29.262 s** (1.833 s after shaped reply), followed by **32 consecutive reference starts** through **61.461 s** (32.199 s sequence). Count profile starts at 03E8/count13, ends at 06F4/count19. This is a candidate coherent sequence, not semantic handshake acceptance.
- Collaborator Eco5 Sep-26: **99** challenges, **2** bounded pairs (61,63 ms); Eco5 Sep-28: **64** challenges, **4** bounded pairs (46,30,32,47 ms). Strict longest reference runs of 28 and 24 respectively, **zero** full strict 32-reference runs; interleaving or profile differences can explain why strict reference heuristics don't complete. Do not conflate model outcome with controller failure.
- Earlier Sep-25 09:05 capture longest strict reference run **31** starts; missing final page only in bounded capture.
- Seven per-capture replay classifications retain **profile, owner, epoch, wire-end, native-acceptance, icon and cloud Online = UNKNOWN**, and **TX-authority=false**. Exact original flags map is common to both Connect RAUC versions but profile-specific JSON is not invariant; local XTR controller firmware/profile not sourced.

## Origin and classification
- **Observed from historical bus text:** CRC-correct ADU shapes, time deltas, strict page sequence; no independently grounded physical sender or direction.
- **Firmware-derived:** version-dependent profile config and separate handshake, package receive and publication gates; not local XTR proof.
- **Strong conclusion:** bounded FC23 pair + configuration burst is a legitimate *correlation candidate*, never sufficient to claim native acceptance, DCM icon, cloud Online, owner, response slot or physical TX authority.
- **Hypothesis:** Oct-03 candidate may represent one genuine DCM bootstrap; cannot prove unique controller epoch or vendor approval from transcript alone.
- **Open:** actual XTR-selected CM firmware profile, sender, slot, wire EOF, semantic approval, display and cloud Online.

## Positive, negative, abort and recovery
**Positive** all seven captures decode, 14 direct assertions pass, exact challenge counts/pairs/strict sequence match prior research, and no false upgrade of UNKNOWN statuses — MET. **Negative** parity failure/unsupported acceptance — NOT OBSERVED in these bounded tests. **Abort:** publish confidential emulation/security material, create unsolicited TX, infer direction/slot from text timestamps, or modify production ESPHome — no abort occurred. **Recovery:** discard offline results; V5DCM2 FIX1 remains unchanged with HARD_DENY.

## Next
**V5DCM17 PREPARED / NOT RUN:** offline integrate Oct-03 and Eco5 candidate lifecycle into CM930 original firmware state-gate model and independently compare available GAP51–53 evidence before proposing new active test. Keep unsourced profile and vendor acceptance UNKNOWN. No physical TX.

**Local reproducible archive:** `V5DCM16_SESSION_REPLAY_OFFLINE_20261017.zip`, containing `replay.py`, passive decoder, 7-file JSON and pair-context CSV (without authentication bytes).
