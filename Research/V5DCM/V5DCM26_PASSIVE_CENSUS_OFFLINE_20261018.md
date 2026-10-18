# V5DCM26-PASSIVE-CENSUS-01 — strict RX-only capture replay + live observation preparation

**Offline task status: COMPLETE / POSITIVE.** 2026-10-18. **Follow-up V5DCM26-LIVE-OBS-01: PREPARED / NOT RUN.** This is a source/capture-only discriminator, not evidence of native C2/Online. The existing live **V5DCM23 FIX2 remains RUNNING / PARTIAL**, last evidence 1/33 from ~2m25s user console log.

## Source and hypothesis

Hypothesis: native `0x0F FC16` group-delivery bursts can be reproducibly distinguished from continuously recurring operational pages using **start+count+CRC** without publishing or decoding private command-mailbox fields. The next live discriminator is whether the already-installed FIX2 observer sees any additional group progression during sustained observation; not whether 33 groups can be fabricated.

**Known-good working context:** uploaded private FIX2 source ZIP SHA256 `561169c31d5a7eb341055fdb37d0302b4816d661fff9cd2df9d607a9498ea9a4`; YAML SHA256 `04f562e2ccf5374ca890c5f107ee38e1fa108251dc80926cc3ba12c85004ed13`. Real ESPHome users' short FIX2 live log showed B11C/B11D parity and software DE/TX HARD_DENY, profile ledger 1/33. ZIP bytes and OTA partition not proven identical to device image. Preserve all existing 180 FIX2 entities, 17 periodic intervals and all TX denial code.

**Single controlled offline change:** new standalone standard-library Python `v5dcm26_rx_only_census.py` reads existing timestamped hex captures (one time and RTU frame per line) in **read-only mode**. The code validates Modbus CRC and literal FC16 PDU byte count, matches only all 33 existing source-verified significant start/count descriptors (W2=15, W3=10, W4=8), records other geometry as mismatch, counts native `0x0F FC23` boundary occurrences, groups counts/masks into configurable time windows. **No serial access, extra UART consumer, mailbox contents, request/response synthesis, no TX, no wire/credential processing.** The script prints shape completeness as descriptive since-capture inventory, not authentication or time-qualified C2. Historic logs have different start/count shapes and are not silently normalized.

## Validation

- Standard CPython no non-stdlib runtime dependencies. Host function test PASS: descriptor length 33 and group counts 15/10/8; positive original CRC fixture and a mutated-CRC negative fixture.
- The seven provided historical capture files were processed directly, and every recognized timestamped frame in each had valid CRC (not a claim that the source recordings were electrically error-free).
- `thermia_capture_20260924_210001(1).log`: 394/394 good, 21 native FC16, 8 distinct strict shapes, 0 FC23.
- `thermia_capture_20260925_071517.log`: 674/674 good, 40 native FC16, 8 strict shapes, 0 FC23, 2 wrong geometries.
- `thermia_capture_20260925_090209.log`: 491/491 good, 41 native FC16, 30 strict shapes, 0 FC23.
- `thermia_capture_20260925_090550.log`: 892/892 good, 73 native FC16, **24/33 strict distinct**, 2 historic geometry mismatches `03E8/13` and `0410/21` (expected modern `03E8/14`, `0410/22`), 0 FC23. Window t=60–90s has 14 strict distinct, t=90–120s has another 10 strict distinct, while t=0–60s recurrent W4 operational frames were already present. This provides a **negative-control distinction between recurring operational packets and settings bursts**, not request-bit proof.
- `thermia_capture_20261003_165355.log`: 2687/2687 good, 162 native FC16, **31/33 strict distinct**, exactly 2 historical geometry mismatches as above, **2 FC23 boundaries**; existing fail-closed portable ledger legitimately refuses stale qualified C2 after boundary without reselection.
- `itec_eco5_gateway_20260926.log`: 10719/10719 good, 1058 native FC16, **33/33 strict descriptors** and 101 FC23.
- `itec_eco5_gateway_20260928.log`: 9174/9174 good, 1105 native FC16, **33/33 strict descriptors** and 68 FC23. Highest 30s descriptive window t=690–720s has 29 strict distinct and 39 matching occurrences. **Cross-model only:** this is NOT a genuine DCM capture or native acceptance of this user's XTR.

### Interpretation and limitations

**OBSERVED LOCAL:** previous XTR historical captures have clear FC16 bursts and recurring operational FC16, but not necessarily matching today's local 33/33 strict geometry. **STRONGLY SUPPORTED:** the 33 descriptors can be matched offline, and data-burst vs recurring polling is visible without sensitive mailbox decoding. **HYPOTHESIS:** the current live XTR only shows 1/33 because it lacks a recognized request/initialization cycle; this requires contemporaneous XTR evidence and remains unproven. **UNKNOWN:** genuine controller owner, physical epoch, native C2/application acceptance, Online, exact original fault behind old R6 D=4, current live request count/transition, electrical DE/TX proof.

**Important:** a raw 33/33 shape inventory (especially across 101 FC23 boundaries) is NOT a continuous session/provenance-qualified 33/33 or valid DCM synchronization. Counts from this simple offline window tool MUST NOT be used to authorize TX.

## Source migration gate — now quantified

An identity-level audit of the **public prepared/not-flashed RX33 STATCLASS candidate** vs private FIX2 identifies 262 public named HA entities (187 sensors, 60 binary, 15 text), 180 private named (117,13,47 and three buttons), only **44 common**, **218 public-only**, **136 private-only**. All shared explicit source IDs align; this does not authenticate current HA registry IDs or runtime parity. The 31 vs74 state-class metadata mismatch has separate provenance. [Full source-only inventory](V5DCM26_HA_IDENTITY_PARITY_AUDIT_20261018.md). **Do not combine an unverified 218-entity restoration with the request-cycle experiment.** Never clear existing HA long-term statistics.

## Follow-up experiment — V5DCM26-LIVE-OBS-01 (PREPARED / NOT RUN)

- **Hypothesis:** current already flashed FIX2 may reveal additional significant packet groups or informative timing/boundary evidence in a longer uninterrupted passive observation, even without a new image.
- **Known-good:** current V5DCM23 FIX2 and original 1/33 live log, B11C/B11D clean, DE low, all software TX HARD_DENY. No YAML replacement, no new UART or mailbox parsing.
- **Relevant prior:** V5DCM20 had a separate 18m33 passive parity run on different firmware; it does not test the *current* V5DCM23 real ledger. The first FIX2 observation lasts ~2m25.
- **One controlled change:** lengthen *observation only* to a naturally stable 15–20 minute ESPHome logging period on **the same device image**, without reboot, HA modification, service-menu change or extra transactions. Device itself remains completely RX-only.
- **Targets:** already existing periodic `[V5DCM22] RX33` group bitmasks, `[V5DCM23] PORTABLE_LEDGER` received/pending masks, `[V5DCM19]` passive counters, `[B11C]`, `[B11D]`, `[S8]` CRC/DE/TX status and first existing `[R6-P30D] HANDOFF_ABORT` if present. No register target or payload because **no TX**; applicable observed native groups are 0x0F FC16 with 33 fixed source-verified starts/lengths.
- **Positive:** any additional W2/W3/W4 distinct receipt and corresponding V5DCM23 parity without RX/HA regression or TX; preserve timing and relevant first boundary.
- **Negative:** no new strict shape observed over the full sustained interval **with healthy RX**. This only narrows natural-broadcast hypothesis; does NOT prove an absent Connect request or failed protocol.
- **Inconclusive:** log gap, OTA/reset, unverifiable software image, missing relevant periodic rows, or ambiguous controller activity.
- **Abort/recovery:** if DE high, real TX attempt, rising CRC/parser errors, HA telemetry interruption, unwanted actuator action, stop observing and return to last independently verified RX-only build as needed. No active bus probing. No unknown writes; retries=0.
- **Required evidence:** 15–20 min log or **minimal filtered lines** including periodic V5DCM19/22/23, B11C/B11D, S8 and first R6-P30D fault; one human confirmation of ordinary HA telemetry. The user must explicitly confirm execution / send results before changing status.

If this observation stays 1/33, next **offline** work is source-only mapping of safe request *metadata*, not constructing 0x0708 mailbox commands, private 0x0F emulation, or enabling native TX.

## Artifacts and provenance

Source script + per-window CSV and JSON result are private conversation attachments available to the user, not checked in to public GitHub as executable commands. No compiled/OTA/physical execution of V5DCM26. No original capture contents or proprietary firmware dumped publicly. Code/compiler claims concern Python host execution only.
