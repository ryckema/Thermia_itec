# XTR 2.4.2 — optionele menu's × Connect-parameterdatabase × lokale captures (2026-10-27)

**Status:** SOURCE + OFFLINE CROSS-REFERENCED; existing older XTR captures contain relevant natural FC16 pages, but **no new C5DL/C5DM live validation** and **no physical TX**. Source: private `ryckema/Thermia_Connect_Firmware/parameters/READ_PROD_01B/E/F/G/J/H_BATCH_*.md` and `findings/SMART_ENERGY_SMART_PRICE_ARCHITECTURE.md`. Baseline current user-live C5DL initial 4/4; C5DM 62-slot entity package remains PREPARED / NOT RUN. Profile restriction **CM930 2.3.0–2.4.3**. Firmware source is mapping evidence, not XTR semantic proof.

| Menu/feature | Exact native addresses/page | Firmware-derived semantics | Local XTR capture evidence | Publication decision |
|---|---|---|---|---|
| Shuntgroep 1 / distribution circuit 1 | `03FC/count11`, `03FC..0401`, `0404` | heat curve2, min, max, corr +5/0/-5, constant temperature | 2026-10-03: `40,10,55,0,0,0` and `0404=40`; `0534=0` | Capability-gated read-only named diagnostic if nonzero; no evidence installed |
| Shuntgroep 2 / distribution circuit 2 | `0410/count21`, `0410..0415`, `0418` | heat curve3, min/max/corrections, constant temperature | 2026-10-03: `40,10,55,0,0,0`, `0418=40`; `0535=0` | Capability-gated diagnostic only |
| Pool limits | `041B/041C` from `0410/count21` | pool temp start/stop limits | XTR `041B=20`, `041C=2` while `0533=0` | RAW diagnostics only; no °C scaling assumption |
| Pool actual | `080D` from `080C/count18` | pool measured temp | XTR 13 natural frames `080D=0` | RAW, not assumed 0 °C |
| Circuit 1/2 actual | `07D8`, `080F` | circuit1 measured, circuit2 measured | natural `07D0/count19`, `080C/count18`; 080F zeros | first source temperature under capability gate; second RAW until scaling local |
| Buffer tank actual | `07D6` from `07D0/count19` | tank measured temperature | natural frame evidence, `0536=0` locally | Unavailable when capability OFF; never present stale/default as physical reading |
| Requested temperatures | `084B/084C` from `0848/count23` | circuits 1/2 desired temperatures | 2026-10-03: both 0; 12 natural frames | Capability gated; only publish valid fresh data |
| Capability page | `0532/count18`, `0533..0536` | pool, circuit1, circuit2, buffer configuration flags | 2026-10-03 `0533=0, 0534=0, 0535=0, 0536=0` | Source STRONGLY SUPPORTED, raw observed; not proof hardware absent forever |
| Additional capability flags | `0541/0542/0543` | EQ, zoning, energy performance | all zero in 2026-10-03 capture | Read-only diagnostics; `0544` power limit is **outside** 0532/count18 and must not be imputed |
| Smart Grid native | `04A6/04A7` from `04A6` page | SG operational state and companion; smart_price_state on 2.3–2.4 profile | LOCAL XTR state correlation Normal `0000`, Enhanced `0041`, Blocked `0042` for 04A6; 04A7 Normal `0000`, enhanced/blocked `0001` | Strong local read-only status candidate; separate from physical SG contacts |
| Smart Price application | gateway-side `smart_price_enabled`, `smart_price_heat_enabled`, etc | Connect application settings **have no native CM930 register**; app may affect room setpoint `03F4` and SG `04A6` | OEM firmware-derived only, no proof cloud/app enabled locally | Do not invent register entities; HA write hold |
| DHW adjacent page | `041D/041E/041F/0420` | start temp, max DHW time, antilegionella interval/min time | 2026-10-03 raw `35,40,0,1`; first two previously locally correlated | Read-only with evidence-qualified labels |
| Other unmapped | `0402/0403/0405/0406`, `0416/0417/0419/041A`, `0421..0424`, `0539`, `0814` | Profile collisions, unknown scaling or ambiguous meanings | Natural pages exist | RAW only / disabled by default |

## Direct conclusion
The prior C5DM 62-register CURRENT H/D/C/M map is **not** complete Thermia coverage. Existing firmware repository already has 03FC, 0410, 0532, 07D0, 080C and 0848 profile-specific decoder research; do not re-derive these as speculative unassigned blocks. The older source's status is **PREPARED / NOT RUN** (static validation only); local captures prove frame presence and raw values, not that each optional field is semantically user-correlated.

## Engineering decision
Next integrated release, once current owner/periodic evidence is satisfactory: reuse *existing passive V5 owner parser* and natural FC16 pages (no second UART listener/parallel architecture), capability-gate optional circuits and stale-invalid values, separate firmware-derived typed candidates from locally proven sensors, and preserve `Compressor Current` exact existing identity/entity history. Do not trigger new read requests or parameter writes for optional groups. Confirm natural pages on current C5DL before UI promotion; if absent, report unavailable instead of inventing a refresh path. HA parameter writes remain ON HOLD.

**CURRENT MILESTONE:** complete XTR native read-only parameter coverage beyond H/D/C/M.
**DELIVERABLE:** this firmware-to-capture crosswalk, no firmware/TX edits.
**REAL BLOCKER:** optional semantics and live availability in current session are not individually proven; hardware flags zero in older capture.
**ONE NEXT ACTION:** integrate the already-sourced passive optional-page decoders/capability gating in one C5DL-derived firmware candidate, only after dependency/owner/periodic source check, without a new native TX path.
