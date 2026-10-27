# 2026-10-12 — R6-P74AQ closure / R6-P74AR phases 1–9 handoff

**Purpose:** dated, additive handover for the next Thermia iTec XTR M native Online/Connect/DCM research chat. This file preserves evidence boundaries, not private handshake material or implementation. The canonical state/log/findings are in this directory; older recorded results remain authoritative for what was actually observed.

## Installed, live-tested baseline — R6-P74AQ

**Status: COMPLETE / POSITIVE for bounded live RX-only shadow smoke test, not for full intended duration or production-HA regression.** User supplied `Pasted text(20261012-151054).txt`: 17:04:50.497–17:08:10.758 (200.261 s), seven AQ snapshots EV 715→964 and 20 AL readings ending EV 965, AQ/AL HOLD=0; 20 sampled parser statuses with badGeom/unknown/resync/drops=0, V5 TX=0, UART-write calls=0 and no visible API buffer warnings. AQ remained `TX=DENY`, `EPOCH/OWNER/WIRE_END/SLOT/DE_ELECTRICAL=?`. The reported completion is **user-authorized functional closure** within this limited scope; the originally intended five minutes and separately confirmed normal HA production entities were not documented. The currently user-tested P74AQ must not be mistaken for the older top-of-file P74AB GitHub status; firmware deployment/compilation cannot be inferred from YAML delivery. Maintain known-good RX-only configuration and existing HA functionality.

## R6-P74AR — parent RUNNING / PARTIAL; offline phase results

All phases below were performed offline using pre-existing artifacts. **None required new XTR bus TX, controller reboot, ESPHome flash, YAML changes, or genuine DCM.** The host tests are reproducible offline checks, not electrical certification.

| Phase | Result/status | Exact demonstrated scope |
|---|---|---|
| 1 | RUNNING / PARTIAL (research initiated) | Genuine cross-model episodes, historical local XTR V4.1 results and P74AQ live record separated; candidate model only |
| 2 | COMPLETE / POSITIVE (offline source audit) | Seven original FC23-response-first-page source windows tied to raw logged frames; no electrical sender/slot attribution |
| 3 | COMPLETE / POSITIVE (offline classifier) | 7/7 source windows, 12/12 tests; inherited 32-page metadata was not yet independent raw replay |
| 4 | COMPLETE / POSITIVE (offline full-page replay) | Four of six Eco5 windows 32/32 geometrical FC16 pages with per-page short address/count ACK forms; two partial at 10/32 and 12/32; 18/18 tests |
| 5 | COMPLETE / POSITIVE (offline ACK-linked FSM) | Seven cross-model windows, 150 page stages with matching ACK shapes, four 32/32 chains, 32/32 tests; wrong order/CRC fail-closed, no TX authority |
| 6 | COMPLETE / INCONCLUSIVE (epoch and owner); POSITIVE for no-TX validation | 99+64=163 original CRC-valid Eco5 FC23 request forms, seven host-gap groups; one additional ATEC reference makes 164 in broader archival corpus; 30/30 offline tests; no unique current XTR epoch/owner |
| 7 | COMPLETE / INCONCLUSIVE (unique epoch); POSITIVE source/register audit | 2,500 CRC-valid FC16 requests across seven genuine cross-model references, 88 valid calendar word tuples, 20/20 tests; RTC is not boot identity; standalone `device_client.zip` inspected; the two RAUC images were **not** newly unpacked or binary-compared |
| 8 | COMPLETE / POSITIVE (host safety audit); ACTIVE-TX NO-GO | 26/26 C++ sanitizer host tests, 20/20 static checks. G03 wire EOF OPEN, G04 exclusive reply slot OPEN, G05 FIFO/DE hardware PARTIAL (host simulation only), G06 physical DE fail-low OPEN |
| 9 | PREPARED / NOT RUN (deprioritized) | Passive electrical RX/DE measurement plan only; not performed or required before more offline protocol work |

**Classification limits:** Eco5/ATEC observations are genuine **cross-model** Online/DCM bus evidence, never local XTR M measurements. Correct frame CRC, FC23 response shape, FC16 short ACK and 32/32 progress do not prove semantic acceptance, exclusive owner, the present controller epoch, wire EOF or permission to transmit. Local EXP355/386 V4.1 controller restart and 32/32 bootstrap were historically user-confirmed, but original timestamped raw logs were not newly available for P74AR replay. Retained/recovery/cancellation branches must not be inferred from these snapshots.

## Earlier V4.1 active evidence — retain positive AND negative tests

- **EXP355 / EXP386:** COMPLETE / POSITIVE, bounded locally exercised guarded controller-restart→native 32/32→runtime recovery; do not treat the old exact active path as safe to enable directly in current V5.
- **EXP387:** historical completed active context; retain original history.
- **EXP388:** RUNNING / PARTIAL; two positive restart subcases do not close the untested pre-semantic/refresh-only cancellation branches.
- **EXP419:** COMPLETE / INCONCLUSIVE; target `085F` owner branch did not occur.
- **EXP420:** COMPLETE / POSITIVE only for the tested explicit-owner retained-runtime context.
- **EXP423:** COMPLETE / INCONCLUSIVE; repeated `0662/count33` unowned/retry problem blocked target write and configuration synchronization.
- **EXP425:** COMPLETE / NEGATIVE for predicted ordered resume tail after one `0662` ACK; the retry stopped but expected `0683→…→06F4` did not follow.
- **EXP426:** COMPLETE / INCONCLUSIVE for isolated `0662` release hypothesis because required trigger was absent; regular retained sync worked.
- **EXP455:** user mentions the broader 355–455 series; do not invent or reclassify EXP455 without a matching original result record.

## Protocol status and safety

**Locally proven:** specific old guarded XTR V4.1 active sessions; present P74AQ bounded clean RX-only smoke. **Cross-model genuine:** FC23 repetition, partial/full ACK-shape bootstrap chains, long initial-page retry. **Firmware-derived:** native CM930 has orthogonal handshake `NOT_ACCEPTED→RESPONSE_SENT→ACCEPTED`, data completeness, application and recovery state axes; not a proven XTR epoch identity. **Hypothesis:** capture-derived session and rejoin patterns can help design a stateful V5 observer. **OPEN:** unique local controller power/session generation, current response-work owner, physical response slot and DE electrical safety, general retained `085F` and orphan `0662` ownership. `A80E` toggling and `A80F` alone are unsuitable as independent epoch proof. Calendar `06EA–06F0` and cross-model `0858–085E` are clock/freshness information, not bootcounters. No new local RTC proof in P74AQ.

**Current hard rules:** controller is the native master, 0x0F is the primary observed DCM/Connect slave route. Output stays `HARD DENY`; no automatic FC23 answer, FC16 ACK, mailbox service, semantic write, unknown register scan or unsolicited TX. Ordinary FC16 address/count ACK is not semantic acceptance. Never disconnect the room sensor; no genuine DCM is available to test.

## NEXT: V4.1 ↔ V5 evidence-based gap audit (PROPOSED / NOT RUN)

Prioritize transferring **proven behavior**, not a blanket TX permission: (1) review actual source/history of EXP355–455 and match each guarded, successful native path to current P74AQ/V5 subsystem; (2) build a per-owner/state table for fresh bootstrap, retained runtime, `085F` and repeated `0662`, with EXP423/425 negatives and EXP426 untriggered branch retained; (3) replay changes offline against original captures and XTR records, with hard-deny output; (4) only after this audit and complete safety review consider a separate qualified experiment. The P74AR phase-9 electrical-measurement plan is **PREPARED / NOT RUN**, not deleted, but lower priority than protocol-state reconciliation. Preserve current working AQ YAML/entities and known-good P74AL fallback. No GitHub edits to working TX code or active ESP required by this documentation handoff.

## Offline artifact provenance

The detailed locally prepared P74AQ closure and P74AR phase-2-to-8 reports/classifiers are held as user-conversation artifacts dated 2026-10-12. **This short public handoff does not claim those archive bytes are committed here.** In the firmware research repository see `findings/R6_P74AQ_P74AR_20261012_HANDOFF.md` for a matching sanitized cross-repository note.
