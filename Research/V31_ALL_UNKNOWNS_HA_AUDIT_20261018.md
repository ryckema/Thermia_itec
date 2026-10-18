# v31 — All visible HA Unknowns / passive-source audit — 2026-10-18

**Status for READ-V31-UNKNOWN-01: PREPARED / NOT RUN.** The source-only corrective observability modification was committed and statically audited. It has **not** been strictly YAML-parsed, ESPHome-compiled, flashed or verified on the user's device. This document is an audit, not confirmation that missing data are fixed.

## Evidence and limits

- User-provided 7-page `Devices – Home Assistant.pdf` printout timestamped **18 October 2026 12:43**. Visual inspection plus parsing of displayed value column shows **33 visibly printed `Unknown` entries**: p1=4, p2=4, p3=5, p4=4, p5=9, p6=5, p7=2. This is a count of *rendered text*, not 33 uniquely identified HA entity IDs. Entity labels are intentionally clipped as `C…`, `D…` etc. by the exported HA layout; exact IDs cannot be reliably recovered from this PDF. The word Unknown may be a literal fallback for an enum, not necessarily an uninitialized state.
- The same printout clearly shows real live data (compressor 20 Hz, current 0.8 A, fan ~380 rpm, outdoor operating mode Heating, working condenser temperatures and several heating settings). The page showing ESP uptime at ~121 s reflects a **recently running** ESP, but a firmware-build timestamp is not its boot time. No native bus frame is embedded in the PDF.
- Canonical latest source before FIX4: `Read-only/Thermia itec XTR/thermia_itec_xtr_m_read_only.yaml` at FIX3 blob `c33eed0d4be08b012018e6bd467eb0ba120ceda4`; after source modification FIX4 GitHub commit `6c24cffffbaf091c88fd68961e1abb5d872dcaa6`. The October18 PDF predates FIX4 and cannot establish the exact flashed YAML or why that unit had Unknown values then.
- Firmware CM930 semantic register inventory and local XTR experiment histories establish *candidate meaning* but **not guarantee a native settings-page refresh will be observed** by a strictly passive controller-side ESP when no genuine Online/DCM is present.

## Unknown diagnosis by source family, not by clipped PDF label

| Data family / examples | Actual source in YAML | Expected Unknown situation | Evidence status |
|---|---|---|---|
| Heating curve, main setpoints | controller `0x0F FC16 03E8/count13+` | Missing source after ESP boot or invalid data | Locally corroborated profile; some settings available in PDF |
| Extra circuit 1 values | `03FC/count11`, **plus** capability `0532` | Not installed, capability never seen/stale, or page absent; forced NAN may be correct | Conditional; firmware + local selected geometry |
| DHW Start Temp, Max Production, Anti-legionella Interval/Minimum Time | `0410/count21+` | All related settings remain Unknown until full page; invalid input range can individually suppress publication | SOURCE OBSERVED in YAML, actual PDF page unseen |
| DHW Enabled/Mode, Startup HT, Heating Time | `042E/count15+` | Settings Unknown without complete native page. DHW mode can be literal `Unknown` for unrecognized enum even if page seen | XTR page known historically |
| Cooling Enabled, temperatures, room hysteresis, time | `0442/count13+` | Missing page, invalid range, or unresolved word semantics. Note direct Cooling Active is NOT the same source | XTR historical 044D proven, EXP382 other values partially supported |
| Pool / Circuit 1 / Circuit 2 / Buffer Installed | `0532/count18` | Unknown when page never arrived, stale after **provisional 6h timeout**, or a nonbinary flag | Firmware flag semantics; current code fail-closed, not live-tested |
| Operation Mode | `0546/count20` (`0553`) | Unknown without source page, or literal `Unknown` if value outside known enum; distinct from direct Outdoor/Operating Mode | XTR operation mode historically proven |
| Aux heater outputs, hydraulic/tank states | `07D0/count19+` | Native page missing or invalid option conditions; direct 0x1E condenser values can still work | Source-only unless exact register locally correlated |
| Native room/cooling/pool/circuit2 RAW | `080C/count18` | Native values missing; source raw and manual labels do not prove scale | Firmware-derived |
| Defrost Active and native outdoor bit states | `0820/count18` | Native 082F flag absent; direct 0x1E can independently report heating and compressor | Firmware-derived bit interpretation |
| Supply Temperature Wanted / Weighted DHW Temperature | `0848/count23` | Page absent or sentinel/range filter rejects value; unavailable is not necessarily fault | Firmware derived/partly locally correlated |
| DHW top-up, Defrost Using Building/Hot Water, Outdoor Stop Active, demand queued | `0864/count3+` | Native operation status page absent; direct outdoor Heating still valid | Historically observed geometry but not necessarily current ESP session |
| Defrost Count, Previous Defrost Interval, Time Since Last Defrost | `0870/count14+` | Missing native counter page; independent direct compressor readings do not populate native defrost history | Cross-model evidence; label/detail quality differs |
| Controller Context / Mode Request / SG Mode | controller `0x02` and slave `0x1E` additional direct FC23/FC10 paths | `Unknown` also can be **enum fallback**, not missing 0x0F page | Some code paths can publish literal `Unknown`; inspect precise source and raw value |
| Direct measured temperatures/frequency/current | slave `0x1E` | Already populated in PDF; do not replace with speculative native mirrors | DIRECT local source / user screenshot |

### Why the 33 Unknowns are not yet individually proven

The export truncates every full label so no `entity_id` mapping exists. No same-run native CRC-valid `0x0F` bus capture, actual flashed YAML hash, or HA entity registry export was attached with the PDF. Distinguish:
1. **No page seen this ESP boot** — no opportunity to publish a native setting; expected Unknown.
2. **Page seen, no value published** — bounds, sentinel, profile/geometry mismatch, invalid enum, missing conditional feature.
3. **Literal `"Unknown"` emitted by YAML** — possibly a valid published string; needs raw source code comparison.
4. **Feature not installed/unknown** — optional values should remain unavailable, not become guessed zero.
5. **Stale/HA registry state** — enabled/disabled defaults are static; old Home Assistant entity registry choices persist.

Do not attempt artificial startup polling, DCM handshake, registry writes or fake values to make Unknown disappear.

## Source-only controlled change READ-V31-UNKNOWN-01

**One controlled change:** add exactly **one** new default-enabled text sensor `Native Settings Pages Seen`, backed by a non-persisted `uint32_t` receive bitmask. Only already-CRC-validated controller `0x0F FC16` page-decoder branches set their own bit; 5s existing interval publishes `03E8:Y 03FC:N ...` for **13 complete page families**: 03E8,03FC,0410,042E,0442,0532,0546,07D0,080C,0820,0848,0864,0870. Y means observed **since current ESP boot**, N means not observed; neither represents hardware installation, decoded semantic validity nor source age. Output ~90 characters, under HA state-length limit.

- YAML commit `6c24cffffbaf091c88fd68961e1abb5d872dcaa6`, source from FIX3 to FIX4.
- Original **257/257** named YAML entities retained; now **258** (187 numeric, 60 binary, 11 text) total.
- Existing `Cooling Settings Page Source` from FIX3, six raw cooling word diagnostics and all other measurement source/IDs are untouched.
- Static checks PASS: 13 unique page bits, new text sensor updated from existing interval, 0 unresolved `id(...)` references, 0 missing `${...}` vars, no duplicate IDs/top-level blocks, UART no `tx_pin`, `restore_mode: ALWAYS_OFF` preserved, bus CRC/frame bookkeeping present.
- README updated with a source table and interpretation. Target folder still contains **one YAML + one README**.
- **Not verified:** strict YAML parse, ESPHome C++ compilation, flashing, live frame/page count accuracy, HA value availability, physical driver activity.

## Future positive/negative/inconclusive live criteria

**Positive:** with a timestamped passive native page (e.g. `042E/count15`), corresponding page summary flips to Y and actual eligible HA settings receive valid values; other direct baseline entities and bus health remain stable, no physical TX. Missing pages staying N correctly explains no fresh values, not an implementation fault.

**Negative:** a CRC-valid complete page was received but summary remained N; a Y summary appears without valid page; a previously working unique entity disappears; any unexpected physical TX/driver-enable high or RX health regression. Abort/rollback to independently verified live V5 RX baseline.

**Inconclusive:** no native controller page occurs during limited capture; source and HA states are time-misaligned; actual deployed YAML not known; a page Y but native value invalid/sentinel and no raw corroboration.

**Smallest future evidence** after the user flashes FIX4: the two exact strings `Native Settings Pages Seen` and `Cooling Settings Page Source`, plus one full-name Unknown entity and its observed state. A passive frame extract only if the mask claims a page exists yet values remain Unknown. **Do not ask for routine compiler output.** No real DCM is available or required.
