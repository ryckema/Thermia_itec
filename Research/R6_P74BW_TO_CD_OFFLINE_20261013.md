# 2026-10-13 — R6-P74BW–CD: eight sequential offline investigations

**Status:** BW, BX, BY, BZ, CA, CB, CC, CD **COMPLETE / POSITIVE for stated offline scopes**. **Active native TX: HARD DENY / NO-GO**. No ESPHome compile, flash, controller action or electrical bus test was done. This research is tied to existing XTR M RX-only work; no live DCM hardware was required.

## Provenance and classification

Original archived genuine **cross-model** Eco5 (26/28 September 2026), ATEC (3 October) and four older captures were re-read: **25,031/25,031 original pre-delimited CRC-good ADUs**. The seven captures are not newly measured local XTR M sessions, and file timestamps are host timestamps, not independently measured RS485 last-stop-bit boundaries. Local XTR evidence was limited to existing ESPHome diagnostic metadata. The actual staged BM/P74AT C++ observer was separately compiled and host-replayed; this did not build an ESPHome firmware image.

**Important provenance reconciliation:** The `Thermia_Connect_Firmware` README (2026-10-10 R6-P14–P17 correction) records **collaborator-reported deliberate Eco5 controller restarts** and a September 26 **gateway present / absent / present** comparison. The **41-request response-absent segment** belongs to the reported gateway-absent interval. That external intervention note is stronger provenance than raw host-gaps alone, but it is NOT an independent electrical power-rail measurement, a unique XTR epoch, or an isolated causal FC23 test. Do not silently replace this provenance with the previous narrower BU/BV statement that the raw capture itself has no independently verified power trace.

## Sequential experiment results

| Experiment | Status and controlled offline result | Explicit limitation |
|---|---|---|
| **BW** | COMPLETE/POSITIVE: 7 Eco5 context windows; six recorded FC23 response shapes followed by first config page; one gateway-absent annotated context, Eco5-26 line 2512, 41 FC23 requests and no recorded response; 11/11 checks | No controller-lockup proof; response shape is not sender authentication |
| **BX** | COMPLETE/POSITIVE: 6/6 response windows show all 32 matching FC16 short ACK **shapes** when counted across the **entire context-to-context window**; six synthetic removed-stage controls fail safely | **Open scope mismatch:** earlier P74AR P4/P5 reported four 32/32 + two partial 10/32 and 12/32 under narrower window/correlation boundaries. Retain both and do not promote the two historical partial sequences to complete. Neither is physical or semantic ACK proof |
| **BY** | COMPLETE/POSITIVE: seven host-timing sensitivity scenarios, 28 counterfactual status/record mutations, 4,608 re-chunk/reassembly checks; timing classification becomes sensitive around 0.1s synthetic host shift | A host-timestamp threshold is NOT a live XTR reply slot or physical RTU idle timer |
| **BZ** | COMPLETE/POSITIVE: actual unchanged BM/P74AT C++ source compiled on host with UBSan; 10/10 static checks and 4,809 CRC-derived genuine native metadata events replayed across seven sources, output always DENY | V4.1 original binary/YAML was source-audited as a behavioral contract, NOT directly executed or flashed |
| **CA** | COMPLETE/POSITIVE: 331/331 genuine FC16 `085F/count5` requests had all-zero data, with 20 host-near short ACK shapes; six overlapping existing XTR diagnostic logs reviewed | No native current-owner proof; EXP419 INCONCLUSIVE and EXP420 only contextually POSITIVE |
| **CB** | COMPLETE/POSITIVE: 23 genuine cross-model `0662/count33` requests and 28 `0683/count33` requests; 16/16 fail-closed synthetic cases | Preserve **EXP425 COMPLETE/NEGATIVE:** one ACK ended orphan `0662` retries but the expected ordered `0683` tail did not occur. EXP423/426 INCONCLUSIVE; original local raw traces were not independently replayed |
| **CC** | COMPLETE/POSITIVE: 8,192 host-only V4.1 state combinations (1,296 cancel/invalidate; 2,800 fail-closed in-flight; 4,096 stop after prior recovery attempt) and four witness-negative cases | **EXP388 RUNNING/PARTIAL** remains; cancellation branches not exercised on the controller |
| **CD** | COMPLETE/POSITIVE: all seven prior result sets combined; 25,031 original CRC-validated records rechecked, seven additional real BM C++ synthetic metadata scenarios and 210 deliberate CRC corruptions rejected | No controller-epoch/owner/wire-end/slot authorization inferred |

Every experiment changed **only** its offline analysis/replay inputs or controlled synthetic scenario. No production YAML, Home Assistant entity, transceiver, UART, native payload, ACK, `0708` command or firmware execution path was changed. Negative and inconclusive historical outcomes were preserved.

## Historical XTR context (unchanged)

- **EXP355/386:** guarded old V4.1 controlled controller restart → full 32/32 → fresh runtime, bounded locally POSITIVE.
- **EXP387:** delayed `0708` semantic re-arm locally POSITIVE in its old qualified context.
- **EXP388:** two positive controlled restart subtrials, cancellation branches **RUNNING / PARTIAL**.
- **EXP419** INCONCLUSIVE; **EXP420** POSITIVE only for tested retained owner context; **EXP423** INCONCLUSIVE orphan `0662`; **EXP425** NEGATIVE ordered tail; **EXP426** INCONCLUSIVE, trigger absent.
- Recent R6-P74BO/BQ administratively **COMPLETE/INCONCLUSIVE** for unproven exact BM binary identity / full HA regression despite positive bounded RX diagnostics. P74BP and BR/BS offline positive; BT/BU/BV offline studies completed with physical-epoch conclusions still inconclusive.

## Evidence classification and next gate

**Observed facts:** original capture frame geometry, host timestamp relationships, six versus one response-bearing/absent contexts, source-labelled gateway intervention, genuine and synthetic replay counters.

**Strong conclusions:** native V5/BM host observer remains nontransmitting; reported gateway-absent context is a useful cross-model natural-control observation; counts from different episode boundaries cannot be substituted for one another.

**Hypotheses:** recorded Eco5 phases may help explain fresh versus retained DCM synchronization; no universal reboot/owner predicate is established.

**Unknowns:** G01 independently unique controller epoch, G02 exclusive current-work owner, G03 physical wire-end, G04 exclusive response slot, G05 real FIFO/DE drain (host-only partial), G06 DE hardware fail-low; interrupted bootstrap controller recovery, exact cross-model sender, and EXP388 untested cases.

**Next:** resolve the AR-vs-BX window boundary discrepancy using the exact original source-line bounds before drawing new protocol claims. No automatic native TX, speculative `0x0F` ACK, `0708` mailbox operation or write is authorized.

Local reproducible scripts/results and SHA manifest are retained in the separately delivered R6-P74BW–CD offline artifact. This public report contains no recovered approval algorithms, private emulation payloads or command-service tooling.
