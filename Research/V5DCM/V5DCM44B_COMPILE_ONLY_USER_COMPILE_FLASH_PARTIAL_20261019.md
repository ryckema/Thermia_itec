# V5DCM44-B compile-only — user compile/flash confirmation (2026-10-19)

**Status RUNNING / PARTIAL — actual user-reported compilation and flashing POSITIVE, post-flash runtime not yet evidenced. No native TX experiment.**

## Provenance
User explicitly confirmed, in conversation: **"gelukt en geflashed"** in reply to the single-ZIP/single-YAML `V5DCM44B_COMPILE_ONLY_COMPLETE.zip` compiler-only handoff. This is user-attested ESPHome build and flash, **not** an independently collected compiler result or OTA binary attestation. Exact installed binary SHA, fresh runtime uptime and RX counters still UNKNOWN.

Archive verified in assistant container: `V5DCM44B_COMPILE_ONLY_COMPLETE.zip` SHA256 `c504934004331f3b3e44b1163a24a4c052d208e7a4aa0555a0158b1f9b1b1295`; YAML inside `waveshare-thermia_V5DCM44B_COMPILE_ONLY_HARD_DENY_DO_NOT_FLASH.yaml` SHA256 `2b54ef5211bf0bbafe167803cf1401a9a7127177ae4c305263775c21aef40d9b`; ZIP CRC valid. **These are source hashes; they are not a verified digest of the user-flashed binary.**

Actual source inspection: ESPHome YAML contains neither `V5DCM42_PRIVATE_TX_BUILD` nor `V5DCM42_HARDWARE_PORT_REVIEWED` compiler define; private V42 source defines `kBuildMaySend=false` if either is absent, `OneShot::arm()` denies when false. Thus this particular compiler-only source is intentionally NO-TX even if user presses the Arm button. The V44B startup string `PRIVATE TX-ELIGIBLE BUILD` is **hardcoded/misleading** in this disabled build and must not be taken as permission or evidence of actual TX. Runtime `build=0` must be checked in new log. Original B11D 50ms DE-high sticky fault interaction remains unresolved for a future TX-enabled image but should not occur while this image remains output-disabled.

Previous live user V43 Arm/Abort evidence remains [V44-A partial](V5DCM44A_ARM_ABORT_RESULT_20261019.md), and historic V42/V43 cross-model host corpus does not prove local XTR response/online.

## New experiment boundaries
No new active action, hardware challenge, restart or native response is requested. Next smallest evidence: **2–3 minutes post-flash passive ESPHome log**, including new `V5DCM44B Native One-Shot TX Status`, parser valid/resync/drops, B11C/B11D first faults/CRC and raw-port comparisons, old S2/S3 physical attempts and UART writes, DE and a few working HA sensors. No need to press Arm. Expected `build=0`, DE=LOW, UART/FIFO output zero, healthy RX. No local session/FC23 acceptance assumptions.

**Positive on-device runtime** only if log actually confirms healthy RX/HA and fail-closed output; **negative** if new RX faults/DE/high/writes or sensor loss; **inconclusive** if log unavailable. Preserve known-good V43 FIX1/FIX-B2/FIX2 RX-only recovery. Do not upgrade this partial status to COMPLETE based on user compile/flash alone.
