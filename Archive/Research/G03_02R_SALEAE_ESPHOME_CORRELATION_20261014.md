# G03-02R — Historical Saleae vs ESPHome timestamp correlation (2026-10-14)

**COMPLETE / INCONCLUSIVE for physical last-stopbit → current B6 callback latency; COMPLETE / POSITIVE for source-origin audit and demonstration of ambiguous recurring-frame matching.** G03 physical current B6 EOF OPEN; G04 reply slot OPEN; native 0x0F TX HARD DENY. This experiment was OFFLINE only, no new Saleae recording, live test, OTA, controller restart, GitHub production YAML or hardware change.

**Hypothesis:** three original local XTR Saleae D2 recordings and available ESPHome logs share same-session frame bytes and a common clock marker sufficient to estimate electrical EOF-to-callback latency. **Baseline:** G03-03/05 edge reconstructions; G03-01R current B6 9600 8E1 UART-debug 5ms batching; G04-05 callback-to-decision measurements. **Controlled change:** read Saleae original `meta.json` and CRC-good reconstructed frames, compare exact byte strings against locally available historical `.log` RAW/HEX/FRAME/DATA records; no new bytes transmitted.

**Verified original Saleae source sessions:**

| File | Acquisition UTC from embedded metadata | Complete CRC-good frames | Unique frame bytes | Maximum repeat of one frame |
|---|---|---:|---:|---:|
| `Session 3.sal` | 2026-09-04 11:22:16.306041 | 55 | 16 | 6 |
| `Session 3--1degree.sal` | 2026-09-04 11:22:46.732742 | 156 | 18 | 18 |
| `Session 5.sal` | 2026-09-04 11:31:55.810217 | 1,047 | 50 | 115 |

**Comparison:** 22 available local ESPHome `.log` files inspected; none identified as simultaneous with 2026-09-04 Saleae acquisition. Later Sept 29/30 logs share identical `0x0F` and other frame values with Saleae captures, but those payloads recur often; exact byte match from different dates is **not** a common capture or synchronized clock. Current B6/G01-09 logs are Oct 2026, not Sept 4. Saleae acquisition host timestamp is not ESP microsecond clock calibration. Thus no defensible absolute or worst-case EOF→B6 callback latency is derivable. Do not fabricate a 99.9% percentile or substitute 5ms debug threshold.

**Positive criterion:** truly simultaneous D2/ESPHome observations with multiple ordered unique frames and an independently verifiable shared timing marker, yielding an explicit uncertainty budget. **NOT MET**. **Negative/inconclusive:** no same-epoch pairing and highly repetitive bytes — MET. **Abort:** guessing clock offset/time zone, treating host timestamp as wire EOF, treating 3.5T or callback as physical evidence, or authorizing native TX. **Recovery:** none; analysis read-only. **Next:** check whether user already has a September 4 same-session ESPHome raw log; otherwise, if later separately approved, ONE passive concurrent D2 plus current B6 RX-only capture with a common observable sync event, no extra UART consumer, no native response. Historical September log would not itself validate current B6 timing.

**Evidence classification:** OBSERVED historical 1,258 CRC-good Saleae D2 frames and non-unique cross-date byte matches; STRONG CONCLUSION current callback correlation unsupported; HYPOTHESIS future synchronized passive capture can bound latency; UNKNOWN current physical EOF, clock skew, G04 slot and G05/G06 electrical controls.
