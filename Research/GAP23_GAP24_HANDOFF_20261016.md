# Thermia native Online/DCM research — GAP-23/24 handoff (2026-10-16)

**Provenance:** Local offline audit artifacts provided in project conversation, historical V4.1 source `Write (Beta)/thermia_itec_xtr_m_waveshare_write_beta_v4_1.yaml` (blob `8e8a82689e53528a8b751a1abbd901f683b6b238`), G01/G02 2026-10-14 reconciliations, portable V5 core, and Thermia Connect firmware-derived CM930 state axes. This note reports already executed user-supplied results; **no fresh compilation/replay was performed by this GitHub documentation update**.

## Experiment ledger — preserve scope

| Experiment | Accepted reported status | Observed limit |
|---|---|---|
| GAP-23E | COMPLETE/POSITIVE LIVE RX-only | `03E8/14` 69, `085F/5` 34, Heating Curve 36, TX zero in bounded sample; owner and epoch unknown |
| GAP-23F | COMPLETE/POSITIVE OFFLINE context | historical V4.1 vs V5 vs CM930 axes; source semantics not present-bus proof |
| GAP-23G | COMPLETE/POSITIVE OFFLINE cross-model fingerprints | Eco5 2026-09-28 211 `03E8/14` byte-identical; not XTR |
| GAP-23H | COMPLETE/NEGATIVE for local full-frame proof | no verified complete current XTR fingerprint pairs; does not disprove repetition |
| GAP-24A | COMPLETE/POSITIVE OFFLINE classifier | 49,631 synthetic assertions; not a production Core integration |
| GAP-24B | COMPLETE/POSITIVE OFFLINE evidence adapter | 60,253 synthetic assertions; historical/contextual evidence must not grant authority |
| GAP-24C | COMPLETE/POSITIVE OFFLINE RX adapter | 24,102 synthetic assertions; physical EOF/slot evidence unavailable from journal |
| GAP-24D | COMPLETE/POSITIVE bounded host regression; INCONCLUSIVE full replay | 28,198 assertions, 15 local sources inventoried; exact EXP355/386 raw session continuity unverified |
| GAP-24F | COMPLETE/POSITIVE bounded parity map; INCONCLUSIVE active parity | 128,259 synthetic assertions; V4.1 active bootstrap/runtime/semantic paths remain unintegrated |
| GAP-24G | COMPLETE/POSITIVE OFFLINE observational guard | const-Core host guard; no lifecycle mutation from P74L metadata |
| GAP-24H | COMPLETE/POSITIVE OFFLINE synthetic bootstrap ledger | 32/32 synthetic shapes explicitly **not** handshake/ACK/TX acceptance |
| GAP-24I | COMPLETE/POSITIVE OFFLINE gap inventory | nine typed remaining source-to-core gaps; full native parity INCONCLUSIVE |

The GAP-24G/H/I combined host regression reports **67,613/67,613 assertions**. Check counts are deterministic synthetic tests, not independent live sessions, full frame replay or firmware compile. Experimental C++ adapters remain standalone/offline candidates, **not deployed** and not incorporated into V5 here. No working private 0x0F responder, command-mailbox tools, challenge material or native TX payload published.

## Evidence classification

**PROVEN / local XTR (bounded):** GAP-23E repeated controller-originated `03E8/count14` and `085F/count5` shapes during RX-only; HA production value; zero observed software output; G01-09 video-anchored restart in its own bounded epoch; historical EXP355/386 positive native session under distinct original experimental conditions.

**STRONGLY SUPPORTED (scope-limited):** passive journal feeds safely support observational state projection. CM930 handshake, bootstrap, runtime and semantic stages must be modelled separately; 32/32 shape geometry and generic FC16 ACK do not prove semantic acceptance.

**HYPOTHESES:** source-equivalence of existing portable Core lifecycle methods and the original V4.1 guards can be tested further offline, but real native behavioral parity requires supporting continuous raw traces.

**OPEN / UNKNOWN:** current controller epoch/owner, independent physical EOF, exclusive slot, DE/FIFO physical timing and reset fail-low; exact EXP355/386 full positive replay; active V5 session qualification and semantic readback.

**DISPROVEN / SUPERSEDED interpretations:** timestamps from unsynchronized logger/Saleae sources do not give physical wire deadlines; no acceptance or TX from 32 synthetic shapes; cross-model Eco5 full-byte repetition does not imply identical current XTR payloads.

## G01–G06 dual record (accepted risk != proof != TX authorization)

| Gate | Research decision | Technical evidence |
|---|---|---|
| G01 | bounded restart risk accepted | 2026-10-14 G01-09 video/intervention-anchored positive; autonomous epoch proof open |
| G02 | COMPLETE/POSITIVE **CONDITIONAL** as user approved | unchanged single-known-external-DCM port, no installed DCM; physical exclusivity not universally proven |
| G03 | research risk accepted | wire EOF→callback latency unmeasured; GPIO18 measurement deferred |
| G04 | research risk accepted; validate later | exclusive response slot unproven |
| G05 | residual research risk accepted | software guards/host DE release tested, actual FIFO/DE electrical release PARTIAL/HOST-ONLY |
| G06 | research risk accepted | reset/brownout fail-low physically unproven |

Risk acceptance is a research scope decision, **not active write/ACK permission**. Keep physical native TX HARD_DENY without a separately scoped experiment and explicit authorization.

## Next bounded experiment

Compare real `thermia::xtr::Core` lifecycle APIs (`fresh()`, `qualify_handshake()`, `begin_retained()`, `begin_recovery()`, `admit()`, `revoke_authority()`) against historical V4.1 fresh/bootstrap/runtime/retained/recovery guards with exact source line references and one targeted host regression per mismatch. Preserve production HA entities and existing RX, never silently promote EXP388 or cross-model behavior.

## Repositories

This public report is documentation-only. Firmware-derived facts are separately maintained in the private `Thermia_Connect_Firmware` repo; no private emulation implementation should be copied here.
