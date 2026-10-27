# V5DCM83 B11D startup alignment — exact V49/V83 source audit and offline replay

**Offline investigation ID:** V5DCM83-B11D-STARTUP-SOURCE-AUDIT-01  
**Date:** 2026-10-20  
**Status: COMPLETE / POSITIVE — OFFLINE SOURCE FINDING AND SYNTHETIC REPRODUCTION ONLY.** **Actual on-device V83 remains RUNNING / PARTIAL.** This investigation does not claim the first real B11D fault cause is proven, nor that native Online/DCM communication was accepted.

## Question, baseline and one controlled operation

User confirms **ESP32 only** flashed/restarted V83 while Thermia iTec XTR M **controller remained running**. Analyze whether B11D's first post-flash `RAW_V5_FRAME_COUNT_MISMATCH` could arise from independent UART framing alignment, without changing the live bus or speculative DCM TX.

Last verified previous production source V49 RX_ONLY/HARD_DENY; V83 now actually running RX-only under user-provided 94s ESPHome log. The V83 field result stays **RUNNING / PARTIAL** due unknown startup mismatch, earlier original 22 resync and one B11D count difference. EXP388 **RUNNING / PARTIAL** unchanged. Existing local historical controller experiments including EXP256 (incomplete one-response caused COMM ERR) are not repeated. Real owner/EOF/slot, current controller identity/profile and APP33/C2/Online unknown.

**ONE offline controlled operation:** exact V49-to-V83 audit of already-existing B11D receive path, plus host-only source parser reproduction using synthetic generic read frames. No original YAML, ESPHome entities, pin, UART, GPIO, firmware, heat-pump controller or installed V83 changed.

## Original-source facts — provenance and precise state transition

The user V49 69-file ZIP SHA256 `62afe39629102a3daa06f09eab3ed159f44437d702fb8d3904c61e62e2a85630` was rechecked. **Four relevant original YAML source spans are byte-identical from V49 to V83**:
1. RAW UART ingress start: `b11d_started` turns true after **>=25ms between callback timestamps**. This proxy is **not physical RS485/RTU wire silence** or controller epoch evidence. The raw FIFO discards bytes before this threshold; the V5 `StreamParser` processes UART bytes from the very beginning.
2. V5 original `parser.feed` call is unmodified and still accumulates incomplete ADUs from pre-start callbacks.
3. Expected V5 FIFO appends **only** `parsed` outputs while `b11d_started` is true, without explicit proof that V5 pending buffer was empty at the B11D arming boundary.
4. Independent CRC RAW splitter accepts its own valid candidates, then **latches `RAW_V5_FRAME_COUNT_MISMATCH` if `independent.size()!=expect.size()`**, before comparing frame bytes; sticky failure short-circuits future B11D raw processing.

Thus **STRONGLY SUPPORTED SOURCE FAILURE MODE:** V5 and RAW observation windows may start at different byte positions following an ESP-only flash/reboot onto an already-active controller bus. A first-batch frame-count mismatch does not by itself show a corrupt Modbus CRC, unsafe DE, device-owned reply slot, or missing native ACK. But this **does not** establish it was the exact real trigger.

## Offline controlled replay actually executed

Used the **unchanged generic V49 `ThermiaV5InlineCore::StreamParser`** extracted previously in V80. A synthetic complete batch contains **two CRC-valid, public/generic eight-byte FC03/FC04 READ requests** (not private Thermia native response bytes or genuine captures). A source-matched simplified RAW-start model processes two callbacks:
- Clean pre-start parser -> first >=25ms callback yields **2 RAW / 2 V5**, no mismatch.
- Pre-start parser holds synthetic incomplete header `02 03 F0`, RAW has not armed; after 26ms callback gap, two valid synthetic frames yield **2 RAW / 0 V5** and the original counter comparison would latch. No bad CRC in either complete new frame and no output required.
- Gap under 25ms leaves B11D dormant.

**Important NON-MATCH:** in this synthetic contaminated case V5 still `has_pending()==true`, whereas the real preserved R6-P10 first-fault snapshot says `p=0 age=35 rem=0`. Therefore the host test proves **one possible structural startup false mismatch**, NOT a faithful replay of the actual unknown B11D fault. The real B11D expected frame count at the moment of first fault is not available in the supplied delayed API log.

Validated **21/21 source/log checks**, **19/19 host assertions each** strict C++17, ASan+UBSan and noexceptions/noRTTI; **4/4 ESP32/native-TX build variants rejected**. The package provides only nonsecret original generic parser subset, audit code, synthetic source-host tests and notes. `V5DCM83_B11D_STARTUP_OFFLINE_SOURCE_AUDIT.zip` SHA256 `33abf4e074ac67cb76ed233650b316cb911b34c8a10e15132486538b16615d83`; ZIP CRC/manifests verified. No ESPHome compile, firmware flash or live TX executed for this research step.

## What the user's V83 field log actually says

Log file SHA256 `bac4ceb1385d003af5dce52653fc6e5c7b000d92eee9cfb7af66f54fac7a46f6`, 2435 lines. B11D summary **one batch, two CRC-valid independent raw frames, zero portable frames, zero compared frames, one COUNT difference, zero byte differences, one coalesced batch and fault sticky**. `comparedV5=0` is zero successful completed comparisons, **not evidence that `expect.size()==0`**. The B11D count difference happened before the first API snapshot. V5 parser had already recorded 22 resyncs, but resync remained constant and drops0 during later ~94 seconds. V83 shared observer unsafe0, DE switch and GPIO21 both LOW, hardware/software TX attempts reported 0 (no independent oscilloscope confirmation). Existing B11D first-fault variables use `restore_value: no`; previous flash fault is not inherited automatically. Actual first-fault reason may still involve a different parser/portable candidate bug, callback aggregation, or real startup receive corruption; exact early UART bytes/first-fault stderr absent.

## Classification, abort and next controlled investigation

- **PROVEN / LOCALLY CONFIRMED (SOURCE ONLY):** unchanged original B11D source across V49/V83, order of RAW arming versus V5 parser feeding and compare/latch, field B11D countDiff1 and later stable software RX.
- **STRONGLY SUPPORTED:** current code can spuriously latch a first batch due to different independent decoder alignment if it arms on a callback gap without establishing common framing and V5 pending baseline.
- **HYPOTHESIS:** this mismatch mechanism was responsible for the real first V83 batch. Synthetic pending state `p=1` conflicts with preserved field snapshot `p=0`; do not upgrade hypothesis to locally PROVEN.
- **OPEN / UNKNOWN:** exact V5 expected count at original fault, identity of first two independent frames, original V5 pending *at the B11D arming instant*, actual 25ms electrical inter-frame silence, controller/peer identity and physical response slot.

No transmission, target slave/register, current value or payload exists for this offline read-only study. Positive criteria were source identity, host demonstration of a possible mismatch with valid CRC frames, and hard fail of embedded/TX builds. Negative criteria would be source drift or host false success. Abort/recovery: discard offline model, hardware unaffected.

**NEXT (not run):** create an **additional, passive, fail-closed first-alignment evidence latch**, keeping existing `b11d_fault`, `b11d_first_fault`, P5 and FIX2 history intact. Record pre/post callback V5 pending/resync and B11D start reason, RAW count, V5 expected count, callback batch length (no bytes/payload or secret algorithms), and first mismatch metadata. The current `R6-P10` snapshot does not record `expect.size()` when no RAW residual exists. Validate a narrowly scoped RX-only source diff offline **before** any user-initiated flash; no controller reboot or new TX needed. Do not clear/mask B11D faults without separate independent qualification.

**Related:** [V83 real device partial result](V5DCM83_LIVE_RX_ONLY_FIELD_RESULT_PARTIAL_20261020.md); [V83 preparation](V5DCM83_RX_ONLY_PREPARED_20261020.md).