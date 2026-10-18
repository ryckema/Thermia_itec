# V5DCM33-FIX-B — post-gap independent RAW RX shadow

**Date: 2026-10-18. Status: COMPLETE / POSITIVE (OFFLINE SOURCE/HOST/STATIC ONLY). Live-device status: PREPARED / NOT RUN.** No full ESPHome compilation, flash, user ARM, controller power cycle or physical TX occurred in FIX-B.

## Purpose and known-good baseline

Existing user-flashed **FIX-A** passive log (22:31:51–22:33:14, 2050 lines, SHA256 `96f4f25dc5ee551f21a7d3c5173eece70ec62f85bef585f44d4d65207a9e46ed`) demonstrated healthy current B11D 529/529 zero parity faults, B11C 548/548, 8 stable historical resyncs, old Bridge04-1 recovered, separate P5 history still latched, software HARD_DENY, DE=0. Exact flashed FIX-A image hash unverified. The earlier V5DCM32 manual controller restart had B11D `RAW_INCOMPLETE_AT_IDLE` **before** a 12.923s observed callback gap, then native FC23 but session denied `BadIntegrity` (LIVE COMPLETE / NEGATIVE). Baseline source is user-private FIX-A ZIP SHA256 `ec26b85929a760be04b03031b02d10a432fc1765c9e699428bec51aa23cf7bd0`; last older known-good fallback V5DCM23 FIX2 RX-only.

**Hypothesis tested in source only:** independent CRC-validated RAW receive observations after a newly observed callback gap can be accumulated in a separate bounded scope **without silently clearing B11D historical integrity faults**, allowing a future separately controlled test to distinguish new clean RX from historical contamination.

## Controlled change / precise target

One additive **passive post-gap RAW evidence cohort**, not a native protocol command or runtime rejoin change. No TX target slave/register/payload; no write initiated, no physical effect expected. Existing passive 0x02/0x1E/0x0F traffic provides RX data; no native owner/epoch inferred.

- `v5dcm33b_post_gap_raw_shadow.hpp` consumes a copy of **the same already-connected UART RX callback**, never a second UART reader. Manual Configuration arm is valid once per ESP boot, then requires an increase in the already existing R6-P24 >=5s callback-gap counter. A callback gap is NOT independent physical restart proof.
- The independently framed RAW group must pass unchanged original pinned portable candidate-length and CRC helpers and exact byte parity with the same-callback completed-V5 reference. A 25ms RX quiet interval is an observational processing boundary, not wire EOF; a recognized incomplete fragment can wait no more than 250ms with pending corroboration. Up to 4KB RAW, 128 V5 expected frames per batch.
- At least **30 seconds and 50 CRC-good exact-matched frames** after the new gap are required for `RX_SHADOW_ONLY`. Entire scope expires after 90 seconds from arm; no automatic retry or scope renewal. It is **NOT** a claim of session rejoin.
- Fail closed on expired/wrong/absent arm, unsafe DE or TX counters, parser resync/drop delta after gap, second unexpected callback gap, CRC/candidate errors, orphan, count or byte disagreement, overflow, incomplete timeout, cancellation or duration expiry.
- **Original B11D sticky first fault, original B11C/C++, R6 P5 historical latch, R6 P24 state, original V5DCM32 policy/ledger, native TX HARD_DENY and all existing HA production entities are unchanged.** FIX-B shadow does not feed V5DCM32 acceptance. It cannot clear B11D, override `BadIntegrity`, publish H021, mark C2/Online or grant ACK/owner/slot/TX.
- UI: two added `Configuration` controls to arm/cancel PASSIVE post-gap shadow, one additive diagnostic text sensor, a visible FIX-B boot marker and original red/brown 30s logging convention. Existing HA 117 sensor + 13 binary_sensor + 47 text_sensor, 5 old buttons, 1 switch preserved; resulting 48 text sensors and 7 buttons.

## Offline evidence and exact artifacts

- Strict source C++17 `-Wall -Wextra -Werror -pedantic`: new FIX-B policy **54 PASS**, including fresh gap+30s/50 frames, wrong boot, unsafe output, resync, second gap, CRC mismatch, byte mismatch, split 1–4-byte fragment completion, orphan, 250ms timeout, 90s expiry, cancellation and impossible TX authority.
- Unmodified actual 2026-10-03 **local historical XTR raw frame capture** used as **byte fixtures**: FIX-B independent RAW CRC and V5 byte parity **70/70 PASS** with synthetic time/gap; this is NOT replay of original 22:02 first fault nor live physical evidence.
- Original FIX-A short fragment 52/52 PASS, original portable CRC fixture 32/32 PASS, V5DCM31 policy 61/61 PASS, V5DCM32 actual original portable ledger 34/34 PASS synthetic and 34/34 PASS unchanged original 2026-10-03 FC23 capture.
- YAML PyYAML `!secret` compatible static audit PASS: same 24 top-level blocks, 44/44 includes, unchanged original 117/13/47 sensor entities, original 5 controls/1 switch, two new Configuration controls, one diagnostic entity. Original archived FIX-A members **66** preserved byte-for-byte except the one original YAML source; no new direct UART write/flush/DE-high calls. ZIP integrity/member-manifest verified.
- **Private full ZIP** `V5DCM33_FIX_B_POST_GAP_RAW_WITNESS_OFFLINE_NOT_FLASHED.zip` SHA256 `1753e92590237e9685f74d8c9d80ca64064cb73e5151d56dcdfc38cbc0769cde`. YAML SHA256 `8610cabc3198ccb7061e9b8e905efeb6ea31b342d6f32e63b19a283ebb817477`. Original included FIX-A/V5DCM32 SHA manifests remain historical, separate FIX-B manifest in private ZIP.

## Negative / inconclusive and abort/recovery

**Positive for the offline hypothesis only.** Not yet proven that the original 22:02 fault occurred in a recoverable short frame, that a real controller power cycle yields an accepted independent RX cohort, or that the native Online/DCM session can rejoin. Under the current implementation, an **old latched B11D fault still denies V5DCM32 rejoin by design**. FIX-B is an observational prerequisite and does **not** fix that by itself.

If a future separately user-initiated live test is prepared, first inspect fresh unarmed boot RX and verify FIX-B version marker, B11D/B11C/HA parity and software HARD_DENY/DE=0. Only a later documented scoped test may involve Configuration ARM and user physical restart. Abort on missing telemetry, CRC/parser regression, any UART TX/DE output, heat pump instability, unexpected second gap or failed raw CRC/parity; restore last known-good FIX2 as required. Never silently clear historical fault or infer epoch/owner from a callback gap.

## Next research action

**V5DCM33-FIX-B-LIVE-PASSIVE-01 PREPARED / NOT RUN** (first ordinary no-ARM software/HA RX observation after a separately user-performed flash). Only after this can a distinct **post-gap cohort user test** be proposed. Subsequent possible FIX-C can investigate if and how validated independent post-gap RX evidence may be consumed by RX-only local-generation rejoin, still without erasing original evidence; that policy is **NOT implemented** in FIX-B.

No public private `0x0F` emulator implementation, `0x0708` mailbox tooling, credentials or security algorithms were committed.
