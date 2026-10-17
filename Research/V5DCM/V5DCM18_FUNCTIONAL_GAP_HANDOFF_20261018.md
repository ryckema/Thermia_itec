# V5DCM18 — functional parity / V5DCM19 handoff (2026-10-18)

**Status:** V5DCM18 COMPLETE / POSITIVE for scoped *offline functional gap identification and handoff*, not for original-reference-Core execution or full end-to-end implementation parity. The previously recorded V5DCM18 offline replay test outcomes remain distinct. There is no new flash, active TX or experimental hardware result here. **G01–G06 residual risks have already been accepted; they are not re-opened.**

## Hypothesis, baseline, controlled change

**Hypothesis:** V5DCM18's useful deliverable is a source-traceable *functional gap list* mapping locally functional Write Beta V4.1 behavior and original Connect CM930 lifecycle to existing V5 modules. Repeated standalone parser/CRC/test counts cannot replace that handoff.

**Baseline:** prior-chat Markdown historical firmware vs V4.1 direct comparison (esp. handshake, bootstrap and mailbox), source [Write (Beta) README](../../Write%20(Beta)/README.md), [v4.1 YAML](../../Write%20(Beta)/thermia_itec_xtr_m_waveshare_write_beta_v4_1.yaml), firmware repo `data/cm930_state_machine_transitions.csv`, `data/cm930_readiness_gates.csv`, `data/xtr_v41_tx_route_to_reference_core_matrix.csv`, firmware-repo original `tools/xtr_dcm_reference_core.py`, V5DCM1/2 ZIP source and previous V5DCM16–18 capture runs. Production baseline V5DCM2 FIX1 RX-only, TX HARD_DENY.

**Controlled change:** offline source reconciliation and functional mapping ONLY, no new handshake implementation or physical TX, and no extra G01–G06 criteria. This audit creates the V5DCM19 integration contract instead of another independent observer.

## Exact functional dependency map

| Native function | Original CM930 / source behavior | Local V4.1 status | Existing V5 piece | Precise implementation gap / destination |
|---|---|---|---|---|
| FC23 challenge framing, CRC/EOF | Original firmware reacts to canonical request and prepares answer | Exact recognition proven locally | V5 StreamParser + V5DCM2 observer, GAP51F–H historical | **KEEP**; don't duplicate parser; observer only records intent |
| Native challenge response | Original CM930 computes a request-dependent response | V4.1 fixed guarded R1 replay locally worked on specific cold start | Separate private approval adapter and policy-open boundary, not ordinary portable Core | **MISSING native generality:** no evidence existing RX-only V5 has a firmware-equivalent dynamic response path; implementation belongs to explicitly gated native response adapter, never copy fixed R1 as universal response |
| Handshake states | Original NOT_ACCEPTED / RESPONSE_SENT / ACCEPTED; permissive application acceptance is not physical TX owner | V4.1 requires guarded start then first expected page; stricter than firmware | V5DCM1 shadow + reference Core state | **SPLIT** semantic firmware state from external TX owner/epoch; don't treat V4.1 guard as universal CM930 requirement |
| Cold-start configuration | Controller FC16 pages, response acknowledgment; application processes register data independently | Ordered XTR 03E8/count14 to 06F4/count19, EXP386 historically positive | portable Core Bootstrap owner + profile table + V5DCM1 observer | **JOIN:** use same session context for parser→state→page/cache; 32/32 only for this fresh-path reference, not unconditional Online proof |
| Retained / hot rejoin | CM930 handles independent process, bus, handshake and app axes | V4.1 retained runtime + hot rejoin through 06F1; EXP388 partial two recoveries | reference Core `begin_retained`, `begin_recovery` & tokens; V5 snapshot observer | **JOIN/RECONCILE:** preserve legitimate no-full-bootstrap operation and cache revocation; avoid forcing 32 pages for retained/hot rejoin |
| Mailbox 0708 | Native poll/read service independent of bootstrap | V4.1 idle response and delayed re-arm EXP387 locally positive | reference Core mailbox decision and readiness gate G4 | **JOIN:** mailbox-service qualifier, data package requests and controller polling must not be conflated with handshake H2; no command-mailbox tooling to be exposed |
| Runtime publications | FC16 push + runtime selector/token context | V4.1 positive runtime after guarded path; owner-specific TX behavior | reference Core normal runtime/token/recovery and source tables | **JOIN:** keep owner/token/selector classification separate from passive observation; no unsolicited ACK |
| Profile/subscriptions | 2.1.105 parser-dependent requested package mask, distinct from 43 supported bits | V4.1 bootstrap service partial analog | firmware-profile tables & V5DCM14/15 readouts | **MISSING runtime bridge:** 43-bit map != required data completeness; use loaded device profile and actual subscriptions before claiming full CM930 app ready |
| Readback/semantic result | Desired value synchronized after return publication | V4.1 EXP387 semantic writing positive, EXP383 TEST mappings NOT RUN | reference Core transaction phase & page cache; staged host cases | **DEFER** to later HA-native semantic scope, preserve evidence and avoid treating ACK as semantic success |
| DCM icon, Online | Controller UI / cloud gates separate from CM930 local session state | Not conclusively proven by v4.1 reports | None proving icon | **UNKNOWN**: must be live observed after native test; not a criterion for V5DCM18 offline replay |

## What actual prior test evidence means

- Historical seven captures: 25,031 valid CRC text ADUs; 164 canonical FC23 challenge shapes + seven reply-shaped records; one strict complete 32-page Oct-03 sequence; Eco5 partial 28/24. Those are bounded session **correlations**, not authentication or exclusive bus response slot proof.
- Previous ZIP C++ regressions: 17/17 scoped host states passed, not proof of `Thermia_Connect_Firmware/main` Core equivalence. The ZIP Core contains ticket/provenance APIs absent in current firmware repo HEAD.
- Previous integrated observer gave seven naïve false full sessions; corrected strict session-aware replay gives one. This is an important **negative** historical observation to preserve.
- Write V4.1 EXP386 and EXP387 locally positive, EXP388 PARTIAL, EXP383 PREPARED/NOT RUN. None are to be overwritten by synthetic test scores.
- Original Python reference-Core capture/corpus suite was **not executed** in this review; no assertion of completed byte-for-byte or source-level full parity. The earlier V5DCM18 COMPLETE of *scoped functional gap inventory* must not be confused with completion of original roadmap V5DCM18 replay criteria.

## Disposition and next integration stage

**Original roadmap V5DCM18 remains RUNNING / PARTIAL** until the *existing original Python reference-Core replay* has been executed against seven fixtures and essential positive V4.1 paths verified in an offline joined model. **The functional-gap/handoff subtask itself is COMPLETE / POSITIVE.**

**V5DCM19 precise scope:** produce one cleaned RX-only ESPHome integration preserving all known-good entities, parser, bus health, `Configuration` experimental controls, and `[V5DCM]` diagnostic style. Carry over V5DCM1/2 passive observers and re-use the existing reference Core's distinctions; no second parser, no production TX policy change. Integrate independent state axes without introducing a false `native_accepted` claim. Do not implement a speculative native response during V5DCM19; target bounded active test only after later roadmap gate.

**Pass:** auditable parser→observer→native-session diagnostic path, positive cold/retained/recovery fixture states, missing-page/duplicate challenge/epoch-change error cases, no unearned owner, cache, mailbox or full-application readiness. **Fail:** generic parser duplicate, regression of live HA sensors, treating simple ACK or fixed R1 as native universal acceptance, fake 32/32 sessions. **Abort:** new TX without agreed test payload, private security material exposure, unauthorized source publication. **Recovery:** revert offline-only additions; deployed RX-only production unaffected.

**No changes to user device were made in this subtask.**
