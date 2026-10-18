# v31 cooling coverage and HA Unknown audit — 2026-10-18

**Status: PREPARED / NOT RUN** — offline review of user-uploaded `Devices – Home Assistant.pdf` (7 pages, printed 18 October 2026 at 12:43 local), present `Read-only/Thermia itec XTR/thermia_itec_xtr_m_read_only.yaml` at blob `9b3c7427db82c23753076d7787d49b8acc03884c`, commissioning manual, canonical experiment/findings and firmware profile tables. **No source/YAML changed, no ESPHome compile or new device test, no bus TX**.

## User-supplied actual HA snapshot — observed, but truncated names

- Device `Thermia itec XTR M`, `esp32-s3`, ESPHome `2026.9.0`, firmware build timestamp 2026-10-18 12:29:28 +0200, PDF printing 12:43. This alone **does not prove** which GitHub YAML blob was flashed or the ESP boot/controller epoch.
- Useful signals are populated on pages 1–4: compressor current ~0.8 A, frequency ~20 Hz, compressor state Running, hot-side and condenser temperatures (various 27.5, 29.4, 33.2°C), outdoor mode Heating, fan ~380 rpm, heating settings and current values.
- Several rows show `Unknown` while the compressor is operating and outdoor state = Heating; many names are physically truncated to `C…`, `D…`, etc. This PDF **cannot unambiguously identify every Unknown entity ID**, nor prove that each missing value is a decoder error.
- Page 6 displays `Thermia ESP Uptime` 121s, but this value may come from one update instant. The 12:29 firmware build time is **not a device boot timestamp**; no assertion is made about actual elapsed time since OTA versus controller restart.
- Diagnostic portion reports `+147 disabled entities` and sensor portion `+1 disabled entity` in the printed HA registry. This is an actual snapshot registry default/current-state observation, not a live YAML entity count; HA prior registry choices persist and can differ from 164 YAML `disabled_by_default` entries.

## Cooling native settings page inventory: 0x0F FC16 0442/count13

Original source defines `if (slave == 0x0F && start == 0x0442 && count >= 13)`. The firmware's `2.3.0–2.4.3` semantic profile plus manual and historical XTR experiment ledger support:

| Word address | Proposed manual meaning | Current v31 named entity / state | Confidence |
|---|---|---|---|
| 0442 | Cooling Enabled | `Cooling Enabled` | **PROVEN / local XTR** setting in historical experiments |
| 0443 | Desired Cooling Temperature | `Cooling Desired Temperature` | Firmware-supported 2.4.x profile; scaling/range as in v31 |
| 0444 | INFO Cooling Hysteresis | **MISSING** | **STRONGLY SUPPORTED**, EXP382 offline, not locally proven |
| 0445 | Cooling Active Above | `Cooling Active Above` | Firmware profile, manual |
| 0446 | SERVICE Cooling Configuration/Type | **MISSING** | **STRONGLY SUPPORTED** from manual/EXP382, not locally proven |
| 0447 | SERVICE Cooling START threshold | **MISSING** | **HYPOTHESIS only**, encoding/sign ambiguity retained |
| 0448 | SERVICE Cooling STOP threshold | **MISSING** | **STRONGLY SUPPORTED**, EXP382 |
| 0449 | Cooling Time | `Cooling Time` | Firmware/manual; manual indicates service range 5..40min versus YAML `0..180` permissive guard |
| 044A | Cooling MAX STARTTEMP | **MISSING** | **STRONGLY SUPPORTED**, EXP382 |
| 044B | Cooling MIN STOPTEMP | **MISSING** | **STRONGLY SUPPORTED**, EXP382 |
| 044C | Cooling Room Sensor Enabled | `Cooling Room Sensor` | Local historic mapping and firmware/manual |
| 044D | Cooling Room Hysteresis Low | `Cooling Room Hysteresis Low` | **PROVEN / local XTR**, EXP379 correlated 1.0→1.8→1.0 °C with reversible change |
| 044E | Cooling Room Hysteresis High | `Cooling Room Hysteresis High` | Firmware/manual; XTR origin and scaling to be checked against current epoch |

**Result:** v31 currently interprets 7/13 page words. Six other native page positions (0444, 0446, 0447, 0448, 044A, 044B) have no dedicated HA entity. The six missing fields are NOT all proven semantic; 0447 must stay raw/unknown until extra evidence. Reading a word from a correctly seen 0442 page is possible without transmitting; acquiring an absent page is a separate transport/session problem.

## Three independent cooling information sources

1. **User cooling configuration**, from controller-originated native `0x0F:0442/count13` settings page. Values such as cooling enabled and setpoint remain `Unknown` unless an appropriate complete page was actually received in the current ESP lifetime (or separately valid persistent cache; this v31 uses `update_interval: never` and no documented safe persisted page cache). A regular ESP reset alone does not prove a fresh controller-settings republish.
2. **Currently selected/run mode**, from live outdoor-unit direct `0x1E:0014/0015` and FC10 `0004/0007/0008`. The existing v29-derived `Cooling Context` and `Cooling Active` can be **OFF** during Heating while cooling *configuration* could still be enabled. Do **not** infer `Cooling Enabled=false` from `Cooling Active=false`.
3. **Native runtime activity/demand**, from passive `0x0F:0864/count4` status `0865/0866` and `0x0F:0820` operation bits. These pages may be absent or temporally different from `0442`. The `Cooling Temperature Raw 080E` value is profile-derived and remains RAW due unproven local scale.

## Diagnosis / status

- **OBSERVED**: Many Unknown entries occur in HA while core ESP/outdoor measurements work; six known register positions in the documented cooling page are not currently published by v31.
- **STRONGLY SUPPORTED**: Cooling settings Unknown are consistent with native `0442` page not having been received **since latest ESP start**, especially when no genuine Online/DCM device initiates settings sync; but **not proven** from the PDF (no frame/page-seen counter). Other possibilities include a parser/geometry gate, invalid value filters, stale HA state, the actual deployed YAML differing from GitHub or missing receipt during ESP capture window.
- **OPEN**: precise complete list of unknown HA `entity_id` values, actual flashed YAML identity, observed RX count/timestamps for 0442 after boot, correct XTR scaling/conditions for 0444/0446/0448/044A/044B, current cooling context/capability, independent verified 0447 semantic mapping.
- **NOT SUPPORTED**: claiming all 524 firmware profile words must be visible on a purely passive bus at any instant; inventing default values, treating Unknown as disabled cooling, or assuming a controlled TX/query is needed before reviewing passive evidence.

## Next controlled step — READ-V31-COOL-01 (PREPARED / NOT RUN)

**Hypothesis:** Page-arrival and page-age diagnostics, plus exact stale/source guards, will distinguish missing native 0442 receipt from bad semantic decoder values without any TX.

**Baseline:** GitHub v31 FIX2 250 entities, uncompiled/unflashed candidate; known on-device RX V5DCM19 FIX1/V5DCM20 result must not be overwritten without independent controlled passivity test. **One controlled code change at a time**: prepare a small RX-only source-observability modification that records `0442/count13` *CRC-valid full frame count and last seen time* (plus source gate for 042E and 0546 if needed). No need to flash merely to observe source counts if an existing live log of a complete frame is available.

**Positive:** log demonstrates complete valid 0442, expected 13 words and cooling source entities update; or log clearly demonstrates no 0442, justifying Unknown rather than false values. **Negative:** 0442 present and valid but current decoder doesn't publish under otherwise valid scaling/range; parser fix then justified. **Inconclusive:** capture doesn't cover boot/refresh or no 0442 in narrow window. **Abort/recovery:** stop if physical TX/DE activates unexpectedly, CRC health degrades, or production signals disappear; return to locally verified RX baseline. **Evidence:** minimal timestamped full 0442/count13 RX frame (if any), boot/OTA boundary and cooling HA entity states with full names; don't ask for compiler output as routine.

Only after source receipt explained, add the five STRONGLY SUPPORTED but unproven cooling fields as correctly marked read-only diagnostic/candidates, plus `0447` as RAW only, without introducing fictitious values when no page is present. Keep the user-requested XTR folder **one YAML + one README**, place additional audit documentation in Research. No calendar/alarm or native TX change.
