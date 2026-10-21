## S90-B6-S88P5-EXACT-SOURCE-20261021 — COMPLETE / POSITIVE (source and host only)
Hypothesis: real S88 UART/lifecycle source preserves RX-only and guarded completion contract. Baseline user-flashed S88 P5 HARD_DENY. One change: read-only exact source checks, no device modification. Evidence user archive SHA256 a74d2aac11bfa965d7ac41105daca7380a2db3ab0ad46a01da75f47d4c705a0d, 10/10 static source checks and original S88 2/2 GCC C++17 strict host tests PASS. Confirmed FIFO-only admission, IDF wait_tx_done call, uncertain-inflight sticky latch, GPIO pad-level DE readback, guards and missing bind/profile/arm from RX-only YAML. G05/G06 hardware/target semantics, complete V5 session still OPEN. No ESPHome target build (toolchain unavailable), no flash/TX. Abort promotion on false hardware owner/slot or unproven DE low; rollback installed S88 P5 unchanged. User report ZIP SHA256 5276f35d532b8939d7a9d197617d4fad27445de919f4ea151909fedbb36ad137. S90 partial; S91/92/93 NOT RUN.

## S90-B5-S88-P5-SOURCE-INSPECTION — RUNNING / PARTIAL (source audit)
Baseline: user-tested S88 P5 RX_ONLY/HARD_DENY. One change: inspect uploaded exact S88 P5 ZIP offline, no source edits, flash or TX. ZIP SHA256 a74d2aac11bfa965d7ac41105daca7380a2db3ab0ad46a01da75f47d4c705a0d, 145 entries, CRC PASS. Exact S88 `v5_native_tx_esphome_io.hpp` implements uart_tx_chars FIFO admission, uart_wait_tx_done timed drain, unresolved in-flight latch and MCU GPIO21 low check; zero budget defaults deny entry. Hence earlier `write_array+flush` gap describes an earlier implementation, not this archive. Actual ESP32 compile, electrical last-stopbit/de feedback and protected newest Service43 parity NOT RUN. Success: auditable source identified; inconclusive physical safety and full V5 lifecycle. Abort promotion on absent bounded budgets, unknown real hardware state or TX gates removed. Rollback unchanged installed S88 P5/V83 RX_ONLY. Next direct target build and hardware-aware read-only review, no live TX.

## S90-B5-STRICT-PRIVATE-SOURCE-IDENTITY-20261021 — RUNNING / PARTIAL (actual code), standalone check COMPLETE / POSITIVE
Hypothesis: fail-closed source gate should reject unpinned/missing or ambiguous private V5 archive instead of confusing header keyword presence with TX readiness. Baseline user-tested S88 P5 RX_ONLY/HARD_DENY. One change: offline read-only Python source-identity utility with four synthetic unit tests, not production code. 4/4 PASS, py_compile PASS. Actual private S73/S43 archive absent, so direct V5 source test/IDF compile NOT RUN; no flash/TX. No physical drain/DE or native acceptance claim. Stop on SHA mismatch, missing/duplicate headers or invalid ZIP; rollback no installed change. ZIP SHA256 ea1e5f26ff2c9de07f7e3b02a91ad3dec6a05caf6d796efa952c2759a5920996. S90 remains RUNNING / PARTIAL; S91–S93 NOT RUN.

## S90-B4-UART-SOURCE-GATE-20261021 — COMPLETE / POSITIVE (standalone audit tool only)
Hypothesis: detect source provenance and protect against prematurely equating UART write/flush with physical DE-safe completion. User baseline S88 P5 RX_ONLY/HARD_DENY; prior Service43 source review. One change: read-only local static ZIP audit tool and four synthetic tests, no production code modifications. Result 4/4 PASS plus py_compile PASS. Private V5 exact parent unavailable, so original V5 direct-source tests NOT RUN, target IDF compilation NOT RUN, no flash/TX. Gate is fail-closed, cannot confer TX authorization; matches header SHA and keyword counts only, never exports protected source. Report ZIP SHA256 ab593b436596ec048a9764f2e90d58d6b15d8450f0fedcb77dd9717a52e39919. Failure/abort: unknown header identity, ambiguous source, missing physical drain confirmation, DE/B11D faults; rollback no installed change. Next direct private source audit and compiler check. S90 remains RUNNING / PARTIAL.

## S90-B3-XTR-CRC-FIXTURE-20261021 — COMPLETE / POSITIVE (offline parser-only)
Hypothesis: local archived XTR FC16/FC03 request/response shapes can be independently CRC-validated and paired into reproducible non-sensitive fixtures. User baseline S88 P5 RX_ONLY/HARD_DENY; one change: read-only standalone Python CRC/shape/timing parser over four local September captures. 415 0x0F parsed frames, 0 bad CRC; pairs FC16 21/21,40/40,41/41,42/73; FC03 13/13,18/18,6/6,3/19; median 13ms and 24ms; synthetic regression 5/5 PASS, py_compile PASS. Unpaired requests in fourth capture remain inconclusive. No actual V5 callback/source compilation, no hardware role/slot or session acceptance determined. Abort any promotion that substitutes matching for physical proof or enables unsolicited TX. No device change; rollback not needed. ZIP SHA256 6b643641745bad3d03ea66da0cd92e162aeba5d86269bb03f87319ad821b7cf5. Next exact private source integration/target compile; S90 partial, S91-93 not run.

## S90-B2-LIFECYCLE-CONTRACT-20261021 — COMPLETE / POSITIVE (standalone offline model only)
Hypothesis: a bounded independent host model expresses S90 lifecycle guard requirements without energizing TX. User-verified baseline S88 P5 RX_ONLY/HARD_DENY; prior S71/S73/S24/S43 evidence. One change: independent Python contract script, not production code. 12/12 tests PASS, python compilation PASS. Tested ledger not automatically authorizing, missing evidence/epoch, manual ARM/drain, staged cache, wrong epoch, DE-low/drain failure, sticky faults and readback invalidation. Positive only for conceptual contract. Actual production V5 source integration, ESP-IDF target compile, electrical G05/G06 and live XTR acceptance NOT RUN/UNKNOWN. No actual TX or flash. Abort promotion if model assumptions are substituted for evidence, or if native UART ownership/DE gate is bypassed. Rollback no physical changes; S88 P5 stays installed. ZIP SHA256 2f58c5b9f1d05e4041cc6898636bfbd46b0c68e09f296daf572ac0aed2d79079. Next source-backed equivalent tests on exact private archive. S90-B remains RUNNING / PARTIAL.

## S90-B-LIFECYCLE-ADAPTER-AUDIT-20261021 — RUNNING / PARTIAL
Hypothesis: existing S73 passive ledger, S71 session APIs, S24 transactional pages and S43 owner callback join can form one V4.1→V5 lifecycle without second RX/TX owner. Baseline: user-tested S88 P5 RX_ONLY/HARD_DENY; EXP386/387 historic scoped positive, EXP388 partial. Prior evidence reviewed: S71/S73/S74/S24/S43 and S62 GitHub Research reports. One change: offline evidence/transition-gap matrix only; no source or device change. Observed from prior reports: 32/32 passive does not bind; bind/profile/arm not invoked by RX-only YAML; host cache-commit guard exists; hardware UART last-bit/drain/DE timing unresolved; ESPHome target compile NOT RUN. This turn performed NO direct private-source host regression, flash, or TX. Positive: precise gaps recorded. Inconclusive: executable adapter and electrical gate. Abort next promotion on fabricated epoch/slot, drain/DE unknown, B11D fault, unsolicited TX. Rollback: unchanged S88 P5, V83/V49 fallback. Evidence local report S90_B_V41_V5_LIFECYCLE_REVIEW_20261021.md. Next: exact private parent archive plus source-backed mock and target build. S90 remains RUNNING / PARTIAL; S91–S93 NOT RUN.

## S90-A — 2026-10-21 — COMPLETE / INCONCLUSIVE (source-gap audit)
V4.1 historically XTR-positive EXP386/387 and partial EXP388 compared with local S88 V5 NativeEsphome23 / ScopedTransport23 / ControllerPageStore23 source. Strongest concrete gap: V5 passive 32/32 bootstrap explicitly does not bind an authorized controller session (`v5_native_service23_esphome_runtime.hpp:90-108`). V5 has fail-closed reset/recovery (34-67,112-135) and scoped output guards (`v5_native_service23_scoped_transport.hpp:27-95`), but complete compiled/flashed/live V5 native response and republish not demonstrated. S62 G01/G02/G04 user-accepted risk closure preserved for original topology; hardware drain/DE G05/G06 and target build still require review. Offline report: S90_A_V41_V5_GAP_MATRIX_20261021.md. No source modification, flash or TX. Next S90-B: callback-to-adapter offline lifecycle integration and mock regression, then target compile; S90 remains open.

## 2026-10-21 — S90–S93 execution plan created
Execution plan delivered as local user artifact THERMIA_V41_TO_V5_S90_S93_PLAN_20261021.md; GitHub roadmap creation blocked, so no repository roadmap file is claimed. S90-A next: exact offline V4.1 vs V5 source/state transition discrepancy table; no source change, flash, or TX. EXP386/387 local positive; EXP388 partial. S62 G01/G02/G04 remain operationally accepted for original topology, G05/G06 and target integration to evaluate. S91–S93 conditional/not run. Preserve S88 P5 RX_ONLY/HARD_DENY. Prior auxiliary studies do not complete milestones.

## 2026-10-21 — ROADMAP CORRECTION (authoritative)
Original milestone meaning restored: S86 native observer integration; S87 gateway engine offline; S88 ESP32-S3 build; S89 RX-only validation; S90 TX readiness gate (physical owner, slot, DE, abort); S91 first user-scoped native TX; S92 accepted session/refresh/FC03 readback; S93 HA writes. Earlier headings 'S89 offline provenance' and 'S90 offline service sequences' are RETROSPECTIVELY RELABELLED supporting analyses AUX-SESSION-PROVENANCE-20261021 and AUX-SERVICE-SEQUENCES-20261021, respectively, and NOT evidence of completion of roadmap S89/S90. Historical results retained unchanged below. Latest S88 P5 live RX-only is positive for observer classification and RX safety. S89 roadmap validation partly covered, needs formal closure review; S90 TX readiness PREPARED / NOT RUN and BLOCKED by unproven physical owner/epoch/slot, wire end and valid provider. No authorization to attempt on-bus TX. Future S91/S92/S93 not run.

## S90 — offline service pairing — COMPLETE / INCONCLUSIVE (2026-10-21)
Hypothesis: distinguish archived FC03/FC16 service request-response timing from native Online startup. Baseline working S88 P5 RX_ONLY/HARD_DENY. One change: standalone offline parser, no device intervention. 200ms shape/time matching in four September XTR files: FC16 requests/pairs 21/21,40/40,41/41,73/42; FC03 13/13,18/18,6/6,19/3; median 13-14ms/24-25ms respectively. Last file 31 and 16 unpaired requests, outcome ambiguous. No native 0F FC23 found; CRC not independently verified; no ownership or ACK semantics. Four regression tests PASS. Result file S90_OFFLINE_20261021/S90_RESULT.md. No flash/TX and no rollback needed. Next S91 design review, passive only.

## S89 — historic-vs-live native-service cohort comparison — COMPLETE / INCONCLUSIVE (2026-10-21)
Hypothesis: historical local XTR FC03 service activity explains different current S88 passive counters but may not prove Online startup. No production change; static parser counts from four local September captures: 0F10 lines 42/80/82/115; 0F03 lines 26/36/12/22; 0F17 lines 0 each. FC03 0708/6 requests 11/18/6/19. Positive: historic 0F03 request/response shapes evident. Negative: none of the sampled local files has 0F17 startup. Inconclusive: sender/epoch/owner and native Online session unknown; Oct3 is external ATEC. No flash/TX or added bus risk. Rollback none. Artifact S89_PASSIVE_NATIVE_SESSION_PROVENANCE_20261021.md. Next S90 offline sequence fixture tests.

## S88 P5 result — COMPLETE / POSITIVE (2026-10-21)
Hypothesis: broaden passive S86 FC16 recognition without RX/TX regression. User flashed P5; live log 22:09:42–22:10:36 confirms observer valid=84 fc16=84, f085f=28, f04a6=56, f03e8=0, startup req/rsp=0, tx_allowed=0. V5 health valid=294 fc16=49 (different timestamp), no RX drops/resync. B11D 276 raw=portable=V5 and countDiff=byteDiff=fault=0; executor physical_attempts=0 HARD_DENY. Positive for scoped classifier, not session handshake, ownership or gateway write. No further TX. Next S89 passive review. Evidence Pasted text(20261021-201051).txt.

## S88 P5 (2026-10-21) — PREPARED / NOT RUN
Passive diagnostic classifier updated to count FC16 more generally. Offline host tests passed. Target compilation and live test not run. Safety configuration unchanged. See S88 phase 5 package.

## S88 phase 4 — extra live-log — RUNNING / PARTIAL (2026-10-21)
Additional local log confirms V5 reception is healthy (2912 frames, zero resync and drops); S88 observer still reports FC16=0 despite V5 showing FC16 pages. Native startup not observed, owner unproven, TX remains disabled. Offline correction and regression tests required; no new flashing or physical TX in this analysis.

## S88 phase 4 live observation — RUNNING / PARTIAL (2026-10-21)
User supplied flashed ESPHome log 21:56:18–21:59:29. Hypothesis passive metadata observer recognizes native FC16 without impacting V5/HA/TX. Positive RX/safety: V5 healthy (1559 frames/255 FC16 at 21:59:09), B11D raw=portable=V5 (1568), difference/fault/resync/drop=0, TX=HARD_DENY; physical attempts=0, shared RX-only lock. Negative observer classification: 60s S88 snapshots valid=84/168/252 yet FC16=0, rejects=429/859/1290. Inconclusive native session: startup_req/rsp=0; ownership/epoch unknown. Overall RUNNING/PARTIAL, not COMPLETE; investigate shape mismatch offline, no bus TX. Abort on any later TX or RX regression; rollback known V83.

## S88 phase 4 — passive snapshot instrumentation — RUNNING / PARTIAL (2026-10-21)
Hypothesis: expose S86 classifier counts without perturbing production parsing or safety. Baseline installed S84/V83 RX_ONLY/HARD_DENY and prepared S88 P1. Single delta: throttled 60 s `ESP_LOGW` read-only snapshot in existing completed-frame callback. Offline tag-aware YAML parse, substitutions, header presence, exact reverse diff, strict C++17 S86 host and bash syntax all PASS. ZIP SHA256 08bc123d37c526340d425f8334522e7bfdd52f2f9cc035be9294ce32450bcdad, YAML SHA256 d692a4c109a1b431c641c394a45e19e2b5228271fbf3f07bddbbda1347ae6aa9. Target compile NOT RUN, flash NOT RUN, TX NONE; no on-device measurements. Abort on compilation failure, unexpected TX enabling or bus-health/HA regression. Rollback leave known-good V83 installed. Next compile-only using packaged script and sanitized result.

## S88 phase 3 — build availability and observability — RUNNING / PARTIAL (2026-10-21)
Hypothesis: S88 compiled target firmware and S86 runtime classifications are observable. Single change: NONE (source-only audit); baseline S84 positive V83 RX_ONLY/HARD_DENY. Offline `bash -n` and strict C++17 S86 test PASS; executing compile-only script exit=10 due to missing ESPHome CLI, so target compile NOT RUN, not failed. YAML SHA unchanged, one observer frame hook before c.on_frame, zero observer snapshot readers: standalone classification counters not exposed. No HA/device regression tested, no bus TX/flash. Abort if target build fails or existing safety/HA/watchdog changes. Rollback installed V83 untouched. Next target compile and separate read-only diagnostic design. Evidence local S88_PHASE3_BUILD_GATE_AND_OBSERVABILITY_20261021.md.

## S88 phase 1 — compile-only candidate — PREPARED / NOT RUN (2026-10-21)
Hypothesis: minimal passive observer is source-compatible with verified archived V83 RX_ONLY/HARD_DENY. Prior baseline S84 COMPLETE/POSITIVE live V83 RX-only, user YAML exact archive match. Single source change: observer header include + completed-CRC callback before existing c.on_frame; no HA/watches/B11D/TX changes. Offline checks PASS: archived hash match, inverse diff exact, 55/55 headers, strict g++ host test, compile script bash syntax. Actual esphome config/ESP-IDF target compile NOT RUN (tool unavailable), no flashed firmware/runtime observations, no TX. Negative/error abort: any target compile failure or changed safety. Rollback installed known-good V83 untouched. ZIP SHA256 4b90fca94740d42850f50bf64d60b702c1895d7845eabda5ec397154fc5755ab.

## S87 phase 4 — scoped deadline/token/revocation host test — scoped COMPLETE / POSITIVE; S87 RUNNING / PARTIAL (2026-10-21)
Hypothesis: scoped transport defaults locked, and an armed simulated scope is revoked on expired deadline, missing token, RX loss, slot uncertainty, unsafe reset or abort. Baseline V83 S84 complete RX_ONLY/HARD_DENY; no production change. Compiled test twice: default and both guarded test flags with -Wall -Wextra -Werror, both PASS. Fake hardware had zero writes. Safe new-epoch reset requires mock RX-low; no auto retry. Negative/inconclusive: previously successfully delivered token replay NOT exercised; no trusted startup response provider, complete session/positive refresh or physical device. Do not overstate token replay as verified. S62 risk override OFF. Rollback none; no flash/TX. ZIP SHA256 675be20fc0e67cf4c71c19de323cb790b7c85f674816be6ce45f93e26de940a1.

## S87 phase 3 — guarded port mock faults — scoped COMPLETE / POSITIVE; S87 overall RUNNING / PARTIAL (2026-10-21)
Hypothesis: original guarded-port transport fails closed under injected physical IO failures, without retries or stale active lease. Baseline installed S84 V83 RX_ONLY/HARD_DENY. One offline host C++17 test, no production code change. g++ -Wall -Wextra -Werror PASS; 11 injected cases PASS (enter, DE command/pin, short write, drain, leave, post-RX, unhealthy RX, busy lease, unsafe reset, successful mock release). Failures sticky until independent mock RX-low restoration; no real TX. Positive only for GuardedPort behavior; scoped deadline and request-token replay on live-armed scope NOT tested; no valid native provider/session. Abort if output emitted unexpectedly or reset clears while DE unsafe; neither observed. Rollback none, V83 untouched. ZIP SHA256 d28f131c05d38c8ba603c0c8bc3fff613b034908c3a2b7582cd385f2d3c04bc4.

## S87 phase 2 — denied delivery/cache/refresh host test — RUNNING / PARTIAL (2026-10-21)
Hypothesis: invalid startup, missing delivery, wrong epoch and uncommitted page cannot advance S23 or expose readback/refresh. Baseline S84 V83 RX_ONLY; S86 partial parked. One source-only host test, no production code change. Compile C++17 `-Wall -Wextra -Werror` PASS and executable PASS. Tested absent trusted provider including risk override, repeated denied FC23, delivery callback without outstanding response -> sticky fault, same-epoch recovery denied, discarded staged page invisible to FC03, wrong-epoch commit denied, epoch reset clears cache, pre-runtime refresh denied, TX compile lock. Negative delivery modeled only (not actual transport fault injection); no successful full session, UART, DE, flash or physical TX. Abort on premature publication, retry or TX; rollback unmodified V83. Package SHA256 41c398515110f2dfd750d4b1700bfbc23ee387f900f2d7ff3d203b6a2e34fc99. Next phase 3 guarded IO failure injection.

## S87 phase 1 — S23 engine admission and cache transactional negative-path host test — RUNNING / PARTIAL (2026-10-21)
Hypothesis: absent verified provider/epoch/slot prevents native startup, and staged FC16 pages cannot leak to FC03 ahead of transport ACK. Baseline installed V83 S84 RX_ONLY, S86 partial. One offline C++17 test against unmodified S82 engine. Compiler -Wall -Wextra -Werror PASS; executable assertions PASS for denied startup with no output/state, unknown provider even under accepted-risk, clean/reset recovery conditions, uncommitted page denial, wrong-epoch denial, committed current-epoch read and reset invalidation. No actual provider, no runtime promotion, no bus TX/flash/target build. Abort future tests on implicit output or early cache commit; rollback no deployed changes. Artifact SHA256 ea07e7fb345ce15df216dba899d411ac032dae88787508b08b16ac28cd9fbdcb. Next S87 phase 2 transport and refresh negative cases.

## S86 source/image provenance check — 2026-10-21 — RUNNING / PARTIAL
Hypothesis user-provided ESPHome YAML matches archived V83 reference and firmware has matching V83 indicators. One offline SHA/string inspection; no source/build/flash modification. YAML exact SHA256 b4aaedf27f8dd3d58fcc7c09316cfe03d9c8f41d40fcd827a31bf1f104d389fa (matches archives); factory image 1,078,336 bytes SHA256 f9ec707e94bbfd1e368d0552519e3530747172dcb7fd6cbbfa6d7fa34ead3e51 and embedded V83 / HARD_DENY strings. Positive source provenance, supporting binary-family evidence; installed identity and deterministic source→binary proof inconclusive. No ESPHome target compilation or live test. S86 remains RUNNING/PARTIAL; rollback none required.

## S86 three-gate readiness package — 2026-10-21 — RUNNING / PARTIAL
Hypothesis: provenance, actual target build and live regression can be bounded as separate gates without risky deployment. Baseline S84 V83 RX_ONLY/HARD_DENY. Scoped change: documentation, offline source SHA comparison and guarded compile-only script; no device change. Archived YAML hash verified; script syntax PASS, deliberate unavailable-tool run correctly BLOCKED (`esphome` absent). Results: Gate 1 PARTIAL (archive identical, flashed identity unknown), Gate 2 NOT RUN (target compile), Gate 3 NOT RUN (live). Stop criteria new B11D mismatch, RX faults, watchdog/HA regression or DE/TX; rollback known-good verified V83. User confirmation required to close live test. Artifact SHA256 c785e2a162d23395c93152324761bd5c3acd751cb00d43e1acd1fcd9e51a986c. No TX/flash.

## S86 phase 4 — offline preflight — RUNNING / PARTIAL (2026-10-21)
Hypothesis: archived V83 source consistency and include/substitution completeness can be checked without build/flash. Verified S84 live V83 RX-only baseline; source↔flashed binary mapping unknown. Single action: compare two uploaded clean S83 ZIP root YAML bytes and static reference integrity, plus prepare next RX-only gate. Result identical SHA256 b4aaedf27f8dd3d58fcc7c09316cfe03d9c8f41d40fcd827a31bf1f104d389fa; 54/54 local includes, substitutions 2/2. ESPHome absent; target compile NOT RUN. Partial because installed identity and live integration open. Abort flash until known-good V83 image and independent TX/DE checks. Rollback unchanged installed V83; no TX. Package SHA256 98cf6e750a39625d4dccad5c8fc1f82075fb73dadbff03d6a6f860a892502981.

## S86 phase 3 — offline V83 source reconciliation — RUNNING / PARTIAL (2026-10-21)
Hypothesis: S86 observer can be re-applied to archived RX-only V83 root YAML as exactly two additive changes with no active TX flags or production RX/HA modification. Baseline S84 verified installed V83 RX_ONLY/HARD_DENY by user logs, exact binary/source link UNKNOWN; source THERMIA_ESPHOME_CLEAN_S83_20261021 archive active YAML is an archived reference only. One change: include + completed-frame callback for metadata-only observer; no output authority. Exact reverse-diff PASS, C++17 -Wall -Wextra -Werror host test PASS, no active candidate flags. No ESPHome target compilation or live deployment. Positive limited to offline source correspondence; inconclusive for installed byte identity and live operation. Abort later RX-only validation for B11D/watchdog/HA/rx regression or any TX, rollback known-good V83. S86 remains RUNNING/PARTIAL.

## S86 phase 2 — V5 callback seam and two-trace offline replay — RUNNING / PARTIAL (2026-10-21)
Hypothesis: a TX-incapable observer can be attached to the existing completed V5 callback without introducing independent RX consumption. Baseline S84 V83 RX_ONLY/HARD_DENY. One source change: observer include and callback in S83 NOT FLASHABLE candidate; existing S23 call, c.on_frame, B11D, watchdog and HA source retained. Synthetic host tests and replay tool compiled g++ C++17 strict and ran PASS. EXTERNAL ATEC Oct 3: 458 CRC-good 0x0F, matched FC23 and 03E8/13 FC16 ACK once. Local historical XTR Sep 24: 68 valid 0x0F, no startup match. No transmission or deployment, no ESPHome build. Positive limited to source seam and completed-frame offline replay. Abort on any HA/RX/B11D/watchdog regression or DE/TX. Rollback delete two additive source changes; installed V83 unchanged. Archive SHA256 50077bf89c9dcc20e16306c16bd0ac865964df440abf09c51b75ee83fdab24a1.

## 2026-10-21 S85 PROVENANCE CORRECTION — source classification only; S85 remains RUNNING / PARTIAL
OBSERVED: S85 phase 2 and phase 3 replayed 458 CRC-valid 0x0F ADUs, including FC23 request/reply and `03E8/count13` ACK sequence, from `thermia_capture_20261003_165355.log`. Earlier verified provenance identifies this capture as collaborator **ATEC + genuine DCM03**, not the user's local XTR M (see `Research/Atec/ATEC_DCM03_COLD_START_20261003.md` and `Research/R6_P74DI_B10_B12_PROVENANCE_RECONCILIATION_20261013.md`). Controlled action in this entry: additive documentation correction only; no replay, new experiment, flash or TX. Correct result: raw chronology and generic offline observer/fail-deny tests retain their narrow source/host validity; purported LOCAL XTR native FC23 accepted-session evidence is DISPROVEN / SUPERSEDED. S85 overall remains RUNNING / PARTIAL; S84 stays COMPLETE / POSITIVE for user's long RX-only run. OPEN: genuine current XTR session and owner/slot. Rollback N/A; preserve historical records and original byte counts.

## S86 phase 1 — standalone passive native observer — RUNNING / PARTIAL (2026-10-21)
Hypothesis: CRC-valid native 0x0F frame metadata can be recognized without touching the transmit path. Baseline S84 RX-only verified V83 HARD_DENY. Single source change: standalone C++ header plus host test, not production YAML. Host C++17 strict compilation and synthetic positive/negative tests PASS. No independent physical source proof, split/coalesced boundary replay or target build; no TX. Abort integration on unexpected RX/B11D/HA/watchdog changes; rollback remove observer and retain V83. Next production V5 RX callback seam audit and offline trace regression. Artifact SHA256 ba1d615de1b61c5caa8aea1eb22521d5ed95eb0b048be6cba5dbb05a9dec266e.

## S85 phase 3 — passive classifier — 2026-10-21: scoped COMPLETE / POSITIVE; S85 overall RUNNING / PARTIAL
Hypothesis: recorded XTR native 0x0F startup can be identified by metadata-only non-emitting replay. Verified baseline V83 S84 RX_ONLY/HARD_DENY. One offline classifier, no installed code change. Original XTR capture: 458 CRC-good 0x0F frames; FC23 request +29ms reply, +1862ms FC16 03E8/count13, +14ms matching ACK. Four Python checks PASS including missing request/reply denial. Outcomes: positive event recognition only; no physical sender/session/semantic acceptance. Abort criteria implicit output or payload disclosure, neither observed. Rollback not needed, no flash or TX. Next integrate read-only observer with B11D and watchdog intact. Report SHA256 6e32798a723f376e31957185847939deb79ed773f28751e4f16729d31a553b54.

## S85 phase 2 — archived XTR capture → S23 dry-run admission (2026-10-21), RUNNING / PARTIAL overall; scoped offline fail-closed subtest COMPLETE / POSITIVE
Hypothesis: authentic V5-delimited 0x0F frames must not produce S23 reply/cache/session advancement without epoch/slot/provider evidence. Baseline installed V83 RX_ONLY/HARD_DENY, S84 COMPLETE/POSITIVE. One offline test, no deployed source change. Raw XTR Oct 3 capture: 458 valid-CRC 0x0F frames (FC23=2 FC16=324 FC03=132). First distinct valid FC23/FC16/FC03 fed to unchanged UnifiedNative23 with accepted_risk82=false, epoch/slot unproven, provider source_verified=false. g++ compile PASS; host executable PASS: all denied, output size zero, no pending, phase AwaitChallenge, no committed page. Abort if any state advance or implicit TX; rollback unmodified V83. Negative session proof preserved. FC23 absent in recent S84 window but PRESENT in archived startup capture; do not overgeneralize absence. No secrets or raw challenge bytes published.

## S85 Phase 1 — RUNNING / PARTIAL, 2026-10-21; OFFLINE ONLY
Hypothesis: use S82 full-path S23 native engine with proven V5 multi-ADU RX and no new RX supervisors. Baseline installed V83 S84 COMPLETE/POSITIVE. One change: offline review/integration test, NO source/YAML firmware modification, flash or TX. Source-proven scope review of threeway engine, scoped transport, ESPHome runtime and S82 accepted-risk bypass predicates. Four shipped host tests built/run unchanged via g++ -std=c++17 -O0 -I. (exit 0 each): negative_paths, scoped_transport, full_merged, engine_admission. Success is limited to host tests; actual target build and live XTR gateway remain untested. Risks/gates: operational accepted-risk is not physical epoch/owner/slot proof; default HARD_DENY must remain. Abort future integration on implicit TX/changed V5 RX, HA or watchdog, missing B11D lease, premature cache semantic commit. Next: one read-only dry-run contract at V5→S23, with deny reasons from existing captures. S85 remains RUNNING / PARTIAL, not COMPLETE.

## S84 — COMPLETE / POSITIVE (2026-10-21; scoped to RX-only regression)
Third user live log 20:20:08–20:23:21, uptime >=1203 s establishes original >=600 s observation goal. No change or bus TX. V5 frames 8774->10307, known FC16 1432->1681; resync 26->26; bad geometry/drops 0. B11D 10243 compared raw/portable frames countDiff=0 byteDiff=0 fault=0, B11C 10244 matched frames; supervisor RX_ONLY HARD_DENY unsafe=0 pin=0; executor 1684/1684 denied, 0 physical attempts (software count). P5 historical fault 1 retained; current RX QUALIFIED. Six B13-SHADOW error-level messages reflect expected abort/no-TX, not new RX corruption. Normal compressor and heating telemetry updated. Result positive for RX-only bus ingestion and safety gates; not physical DE electrical proof, not native session or write acceptance. User authorized closure. Evidence: `Pasted text(20261021-182335).txt`. No flash/TX test performed.

# S84 LIVE V83 RX-only, 2026-10-21 — RUNNING / PARTIAL. Evidence user-uploaded ESPHome 2026.9.0 API log (~20:03:10–20:05:01, ~111 s); user has not supplied full planned 10-minute interval. Observable: API handshake OK; V5 frames=91→940, known native FC16=15→153, unknown=0, badGeom=0; resync=26 from start remained unchanged, drops=0. B11D raw/portable/V5 parity 796/796/796, count/byte differences zero, first fault NONE; V83 shared supervisor locked RX-only, no unsafe/DE/TX counters, software hard-deny; 0x0F FC23=0, mailbox=0 and no native Online/Connect acceptance. Historical P5 fault=1 and Bridge02 historical RX fault=1 are preserved; current RX reaches QUALIFIED after >=30s. Classification: live regression POSITIVE for covered receive/HA/no-software-TX subset; S84 overall PARTIAL pending 10-minute coverage and electrical level/semantic checks. Do not confuse startup resync=26 with clean-from-power-on. Abort future tests on new B11D divergence, growing resync/drops or nonzero TX counts. No live TX attempted.

# 2026-10-21 S83 V2 execution: RUNNING / PARTIAL, offline source preflight COMPLETE / POSITIVE, real ESPHome target compile NOT RUN. Exact S82 Full Path ZIP SHA256 6e6c8baaba70c53d0b2b39359aba37dd59d719c7bb0850ae04c316fbf01164d4. New standalone `S83_V2_SOURCE_PREFLIGHT.py` passed exact source: 79/79 includes, substitutions 2/2, ESP32-S3 ESP-IDF 16MB octal PSRAM, portable bridge present and external thermia_rx_shadow pinned to f8adf5fbd5cb69cc6a72cea913c6a46a48619a25. Symbolic `!secret` parsed without reading secret values. Three deliberate-failure cases each DENIED: nested platformio buildflags, pinned-Git-ref drift, missing local header. Existing S83 V2 shell helper bash -n PASS; execution against source exits 69 due unavailable esphome, no PlatformIO/Xtensa compiler; PyPI DNS inaccessible. No codegen, linker, binary, flash or TX; not a target compilation failure. S82 RUNNING / PARTIAL, S83 RUNNING / PARTIAL, installed V83 RX_ONLY/HARD_DENY unchanged; G01–G06 not repeated, G05/G06 physical OPEN, EXP388 PARTIAL. Artifacts: S83_V2_EXECUTION_REPORT_20261021.md SHA256 d6d785bb826782c2541a93bfa958457a5da5ed3a1441cd661fc0b25b6182c4d8; S83_V2_SOURCE_PREFLIGHT.py SHA256 059bcbdaa0ed70b2641e3f4ad210e84fe56e9980f6946c54ee886e3bb8fb8d24. Next real RX-only ESPHome config+compile on toolchain-capable environment, then candidate separate, no flash.

# 2026-10-21 S83 compile helper V2 correction — RUNNING / PARTIAL; no target build. Previous raw grep falsely rejected legitimate `#if defined` embedded in RX-only YAML. V2 checks environment build defines and unexpected platformio_options/build_flags, retains exact RX-only filename, protects local diagnostic logs, config+compile only; bash syntax PASS and source preflight reaches expected `esphome unavailable` exit 69. Actual ESPHome compile/link NOT RUN; no flash/TX. V83 RX_ONLY/HARD_DENY unchanged, G01–G06 unchanged, G05/G06 physical OPEN, EXP388 PARTIAL. SHA256 V2: f21aae64435bbdc46f2bacf7215e59d355ee1c614d7ef3a056dcd8ad6db3e224.

# 2026-10-21 S83 real ESPHome build blocked by offline environment — RUNNING / PARTIAL, target compile NOT RUN. Verified exact private S82 ZIP and build-profile guard source; `python -m esphome version` fails `No module named esphome`, pip package index DNS unavailable. This is environment/tooling blocker, NOT a target compilation failure. Prepared `S83_RUN_TARGET_COMPILE_ONLY.sh` for user ESPHome installation: RX-only YAML check then `esphome version`, `esphome config`, `esphome compile`, no run/upload/flash. Prepared `S83_NEXT_ACTION_20261021.md` with provenance and explicit candidate build separation. Physical TX, semantic acceptance and actual build remain NOT RUN/UNKNOWN; installed V83 RX_ONLY/HARD_DENY. G01–G06 not repeated; G05/G06 physical OPEN, EXP388 PARTIAL. Next have RX-only target compilation in connected ESPHome environment; no further duplicate host sweeps. Report SHA256 fdb119359c50c6271eb13547ad1c8e16884a80fed0745360233e0a92d8800943; script SHA256 d10a7ddb3fd88d721cfb714b483e66ab913d135f03616c2372e7f6a4dcafcbe5.

# 2026-10-21 S83 offline host recheck — RUNNING / PARTIAL, real target compile NOT RUN. Checked canonical state and exact private S82 full-path ZIP, reran `tests/run_host_tests.sh` on extracted source: exit 0, all host regressions including synthetic FC16/0x0708/FC03, ESP_PLATFORM RX-only stubs and TX-denial guards PASS. Inspected `v5_native_s82_build_profile.hpp`: candidate requires all three explicit defines; rejects simultaneous legacy V42 TX; macro selection does not arm/authorize bus TX. Actual ESPHome not installed (`No module named esphome`), so no target codegen/link/image, flash or TX. Installed V83 RX_ONLY/HARD_DENY; G01–G06 unchanged; physical G05/G06 OPEN, EXP388 PARTIAL. Offline report SHA256 fddff36a796fc0167969a55a8c8d06857e22646491889c7782c5f8385af20118. Next real S83 RX-only compile, then separately reviewed candidate compile (no flash).

# 2026-10-21 S83 target preflight — RUNNING / PARTIAL; offline preflight COMPLETE / POSITIVE, actual target compile NOT RUN. Exact S82 private ZIP source inspected. ESPHome-secret-aware YAML parsed (24 top blocks); 79/79 esphome includes exist, 0 undefined substitutions; `esp32s3`/16MB/ESP-IDF/octal PSRAM configuration present; local portable bridge present. Host test runner PASS (stubs only). Current YAML does not define V5_NATIVE_S82_CANDIDATE_PROFILE, and therefore is RX_ONLY candidate, not proof of scoped native-TX build. ESPHome package unavailable; no target compile, flash or TX. External pinned Git component fetch unverified. G01–G06 unchanged, G05/G06 physical OPEN, EXP388 PARTIAL. Artifact S83_TARGET_BUILD_PREFLIGHT_20261021.md sha256 812f33318fa7b0ade4b4e3b78aa7c8615e1a7538285dc7a9395aa300c099ffd5. Next S83 genuine RX-only baseline build and separately reviewed opt-in candidate build, neither flashed.

# 2026-10-21 S82 host stub regression — RUNNING / PARTIAL. Software-only test of the private native runtime exposed a missing S62 policy-to-mailbox qualification at 0x0708; corrected inside the existing runtime. Synthetic host ESP_PLATFORM test passed bind/arm/startup, ten locally established cold FC16 pages, exact 0x0708, cached FC03, CRC/DE/scope cancellation and unresolved drain-failure guards. Normal RX-only build remained denied; two opt-in negative compile guards passed. V83 untouched; no ESPHome target compile, flash, live TX or semantic setting change. G01–G06 not re-tested; G05/G06 physical OPEN; EXP388 PARTIAL. Private ZIP SHA256 6e6c8baaba70c53d0b2b39359aba37dd59d719c7bb0850ae04c316fbf01164d4. S83 PREPARED / NOT RUN.

# 2026-10-21 S82 ESPHome runtime policy propagation — RUNNING / PARTIAL native gateway; COMPLETE / POSITIVE offline host/source-guard substep. Private `v5_native_service23_esphome_runtime.hpp` updated: `bind_qualified_controller_session` optional explicit default-false S62 policy, nonzero caller-supplied local generation, real RX/B11D/DE-low required; bound risk revoked on loss/reset; `arm_scoped` requires matching epoch + matched scoped policy + supervisor, manual bounded scope remains; `on_complete_frame` accepts policy route while preserving bound epoch equality, RX/B11D/physical DE, exact downstream framing/CRC/provider. 38 PASS host test lines and Python source-guard PASS. Not a target compile or complete behavioral FakeIo chain. No flash, TX or semantic writes. V83 RX_ONLY/HARD_DENY, G01-G06 unchanged, G05/G06 physical OPEN, EXP388 PARTIAL. Private ZIP sha256 62c4c9ad970de5be97e7c1d6ecec1ed9e75012926c908b5ddb050da488c143ec. NEXT build ESP_PLATFORM stubbed runtime and positive whole-path FakeIo test, then S83 target build.

# 2026-10-21 S82 engine admission continuation — RUNNING / PARTIAL gateway; COMPLETE / POSITIVE OFFLINE engine-boundary substep. Private source `v5_native_service23_threeway.hpp` now accepts default-false `accepted_risk82` only for historical startup/initial admission gates; `v5_native_service23_scoped_transport.hpp` forwards approved bounded/manual S62 risk without fabricating measurement fields. Exact challenge, provider validation, CRC, epoch equality, B11D and physical DE/UART checks preserved. New `test_s82_engine_admission.cpp` confirms policy-off deny, scoped policy-on in-memory success, bad epoch/B11D/CRC deny. Host `tests/run_host_tests.sh` PASS. FULL TX CHAIN NOT DONE: ESPHome bind/on_complete_frame remains old proof-gated, runtime paths need audit; target build/flash/live TX NOT RUN. V83 still RX_ONLY/HARD_DENY; G01-G06 not reopened; G05/G06 physical open, EXP388 partial. Private ZIP sha256 a32ad777a5f074c0c3062c177d508a92c6ff4525789c7a16b46072705f2e1718. Next finish ESPHome runtime integration and positive fake full path, then S83 target build.

# 2026-10-21 S82 DIRECT OWNER/TRANSPORT: RUNNING / PARTIAL native gateway; COMPLETE / POSITIVE offline source-level substep. Updated exact S82 private source directly (NOT extra policy adapter): `v5_native_tx_arbitration.hpp` now has typed `AcceptedRiskGrant82` in Preconditions distinct from physical proof; `PhysicalOwner::begin` accepts either old physical evidence or explicit accepted-risk policy with same nonzero local generation and all real CRC/RX/B11D/DE/manual restrictions. `v5_native_service23_scoped_transport.hpp` adds default-false Scope23 `s62_risk_accepted`, validates bounded reviewed manual scope, passes typed risk to physical owner. 16/16 available test*.cpp host compile/run PASS incl new owner risk deny/allow tests. IMPORTANT UnifiedNative23::prepare and ESPHome NativeEsphome23::bind/frame remain strict proof gates; full active TX path NOT complete, no target ESPHome compile/flash/TX. Installed V83 RX_ONLY/HARD_DENY, G01/G02/G04 closed under S62, G05/G06 physical open, EXP388 partial. Private ZIP SHA256 9898a47df706fcfc7932e878cfb781853edbac421b5e3c35c170c259b4d6a2f0. Next finish service/runtime policy propagation and full positive simulated frame path before target build.

# 2026-10-21 S82 gateway-firmware-only continuation — RUNNING / PARTIAL: private S82 build-profile source updated directly in `v5_native_service23_esphome_runtime.hpp`; `on_complete_frame` now rejects nonmatching `e.controller_epoch != bound_epoch_` before preparing delivery (transport already cross-checks epoch). One source change. 15/15 available top-level C++17 host tests compiled/executed PASS; ESP_PLATFORM path/actual ESPHome target compile NOT RUN, no flash/TX. Accepted-risk bind/arm/deliver integration still incomplete and not represented as implemented. Installed V83 RX_ONLY/HARD_DENY unchanged; no G01–G06 repeat. Artifact private SHA256 155b3cd775b9309adb5151f22339a8bf40041a0b524c1a4e974415cc20d2797d. Next implement complete typed native engine path and target build; no semantic writes or HA write controls in present scope.

# 2026-10-21 S82 continuation: RUNNING / PARTIAL native integration; reviewed exact S82 build-profile source. `bind`, `arm`, frame handling, transport `deliver`, and `PhysicalOwner` remain independent proof-level gates. Added ONLY an unconnected typed S62 operational-policy prototype/test (NOT active engine binding); 16/16 available top-level C++17 host test executables PASS, no full 36-suite rerun. An unconnected policy header is not a usable gateway and must not be misreported as functional progress. No target ESPHome compile, flash, TX; V83 RX_ONLY/HARD_DENY unchanged; G01/G02/G04 risk closures respected, G05/G06 physical open, EXP388 partial. Private prototype ZIP SHA256 45658e6cdf68c2b1145684cbe51508a009062464ce080825160db8307654c783. NEXT substantive code change: directly integrate typed S62 policy in existing native owner/transport/runtime chain while retaining real DE/UART/CRC/manual limits; avoid more standalone admission layers.

# 2026-10-21 S82 build-profile source continuation: RUNNING / PARTIAL for active native `bind→arm→deliver` and S83 ESPHome target compile. Exact private S81/S82 source modified directly: six headers select new `v5_native_s82_build_profile.hpp`; normal profile retains Service36 RX-only barrier; separate explicitly flagged S82 candidate profile requires all 3 opt-in build macros and rejects legacy V42 TX, but does NOT arm/authorize physical TX. Latest source-only YAML includes header, 24 roots parsed. 15/15 available host test executables pass, 3 profile compile/negative tests pass. No active engine evidence-policy refactor, no genuine target build, flash or bus TX; V83 RX_ONLY/HARD_DENY unchanged, G01/G02/G04 S62 closure maintained, G05/G06 physical OPEN, EXP388 PARTIAL. Private ZIP SHA256 2e8d022e09b88e1abc6b0d50cdba6d95c4844e657c8907c2ea641a420b9d4617. Next: implement typed accepted-risk engine transport path and target build; do not claim active gateway.

# 2026-10-21 S82/S83 joint verification: RUNNING / PARTIAL for both active-engine integration and target build. Re-read exact S81/S82 private source and current canonical state; freshly compiled/ran 14/14 directly available top-level C++ host tests PASS (historical full 36/36 remains PRIOR result, not rerun). Parsed 24 YAML roots; confirmed RX-only Service36 build macro gate and physical-evidence restrictions at bind/on_complete_frame/deliver remain. ESPHome and PlatformIO are absent, so genuine ESPHome/IDF target compile NOT RUN. No S82 native active policy-to-transport patch, flash or bus TX performed. G01/G02/G04 accepted-risk closure remains, G05/G06 physical OPEN, EXP388 PARTIAL and V83 RX_ONLY/HARD_DENY unchanged. Verified S82/S83 preflight ZIP SHA256 427ab2097af0d408fefb41cb7b16db9fa3eb89d905a1ed619e4674bf52d2554e. Next requires genuine typed accepted-risk bind/arm/prepare/deliver implementation and separate target build; no fabricated physical evidence.

# 2026-10-21 S82+S83 combined: S82 RUNNING / PARTIAL native TX integration; new PRIVATE typed S62 accepted-risk operational admission gate added (separate from physical epoch/peer/slot proof), host-tested for stale generation, expiry, DE-low, UART drain, semantic in-flight, B11D/watchdog, supervised ownership and bounded user scope. Gate DOES NOT bind/arm/deliver or authorize TX on its own. S83 RUNNING / PARTIAL: 37/37 available C++17 host tests PASS; production RX-only YAML parses (24 root blocks, no missing substitutions), SERVICE36 build lock and HARD_DENY preserved. Neither ESPHome nor PlatformIO present so actual ESP32-S3/IDF compile NOT RUN; flash/live TX NOT RUN. Production V83 unchanged. G01/G02/G04 S62 risk closures unchanged (do not repeat), G05/G06 physical OPEN, EXP388 PARTIAL. Private ZIP SHA256 f2d8db1f3464a63ce5b1ef8bf1f40b1f9cb22a66f42834dc072d5bc7a51b8cce. NEXT: finish ONE actual native engine/transport typed risk binding, run host+real target compile, prepare separate manually initiated bounded live test; do not claim active gateway now.

# 2026-10-21 S82 CONTINUATION: RUNNING / PARTIAL active binding, COMPLETE / POSITIVE comprehensive AVAILABLE host regression 36/36 (strict g++ C++17 build+run, zero failures). Reviewed exact uploaded S81/S82 private source: `NativeEsphome23::bind`, `arm`, `on_complete_frame` and `ScopedTransport23::deliver` still consume separate physical-evidence fields; S62 accepted-risk S76–80 policy is currently preparation-only. NO operational native bind→arm→deliver code changed, no physical evidence fabricated, no actual ESPHome/IDF compile, flash or TX. Installed V83 RX_ONLY/HARD_DENY unchanged. G01/G02/G04 S62 closure retained, G05/G06 physical OPEN and EXP388 partial. Offline regression report ZIP SHA256 ed14e95f58e429b737b96342ee242368701acedd4a532b87a67292fec10da528. NEXT: one cohesive typed operational-policy integration across engine and transport, preserve physical DE/UART gates, test both success/denial before target compilation.

# 2026-10-21 S81/S82 combined (private S80 basis): S81 COMPLETE / POSITIVE OFFLINE — legacy GuardedPort FakeIo test fixed to implement `de_commanded_high()`; production guard unchanged, 13/13 top-level host C++ test executables compile/run PASS. S82 RUNNING / PARTIAL — reviewed native bind/arm/deliver and added passing S82 offline release-gate host test; NO ACTIVE TX binding/arming integrated. Accepted-risk policy remains separate from unverified physical evidence; original `epoch_verified`, `peer_absent`, `physical_slot_measured` safety requirements not fabricated. Default build RX-only. No ESPHome target compile, flash or bus TX. G01/G02/G04 S62 decisions remain closed; G05/G06 physical open, EXP388 partial; installed V83 RX_ONLY/HARD_DENY unchanged. Private artifact SHA256 3318c8a88a7fd1c8fb02a09df8496cdbf99e8afe6bb73782fa1fa923733b400e. Next: implement ONE complete source-backed policy/engine bind-arm-deliver route with independent physical UART/DE checks, full regressions, target build, then separate user-initiated live TX.

# 2026-10-21 S80 `V41-V5-S80-SCOPED-OPERATIONAL-ADMISSION-01`: RUNNING / PARTIAL native gateway integration, COMPLETE / POSITIVE S80 targeted offline test (5/5 S76–S80). Exact private S79 base; ScopedSessionAdmission80 stages bounded manual scope only with generation match, reviewed profile, owner idle, supervisor joined and IO safe; <=64 responses and <=180 s. No fabricated epoch/peer/slot evidence and no physical bind/arm/frame TX enabled. Runtime hooks revoke on controller/bootstrap loss; source-only YAML has 24 parsed top-level blocks, new header included, `deliberate_enable=false`, `HARD_DENY`. Generic C++ suite 12 PASS / 1 FAIL: legacy test_guarded_port.cpp assert port.send at line 18; failure preserved and requires diagnosis, not falsely reported full PASS. Target ESPHome compile, flash and bus TX NOT RUN. Installed V83 RX_ONLY unchanged, G01/G02/G04 S62 accepted-risk closure not revisited, G05/G06 physical OPEN, EXP388 PARTIAL. Private ZIP SHA256 fe04d384f53a2c51cb64f7992a69b35b64fcbfe76aa80545af3882331a881f78. Next reconcile guard regression and run full target build; actual semantic native TX remains unimplemented.

# 2026-10-21 S79 `V41-V5-S79-ENGINE-ADMISSION-ADAPTER-01`: RUNNING / PARTIAL native integration, COMPLETE / POSITIVE targeted OFFLINE tests. Exact private S78 ZIP used to add `EngineAdmission79` host-testable policy/engine seam, checks valid CRC, healthy RX/B11D, DE-low, drained UART, no pending reply/semantic operation, explicit manual scope and matching local generation; denies fabricated physical epoch/peer/slot and denies native bind/TX. Runtime includes adapter and revokes prepared eligibility on boot reset, bus return, bootstrap fault or policy ineligibility. S76–S79 standalone strict GCC C++ compile/run 4/4 PASS. Actual V5 engine bind/arm/on-frame TX unchanged, RX-only YAML/HARD_DENY and installed V83 unchanged; full regression/ESPHome target compile/flash/live TX NOT RUN. G01/G02/G04 S62 accepted closure remains; G05/G06 physical OPEN, EXP388 PARTIAL. Private S79 ZIP SHA256 2cd1732b6ea280ee3dfaca47062d4d846c011e6891764da607b009ff351f71fd. Follow-up: source-supported policy-to-engine TX design, full regressions and target build; do not mislabel as functioning active gateway.

# 2026-10-21 S78 `V41-V5-S78-SESSION-LIFECYCLE-01`: RUNNING / PARTIAL native RX-only source lifecycle integration; COMPLETE / POSITIVE targeted offline C++ host tests S76/S77/S78 3/3. Existing NativeEsphome23 runtime now uses SessionLifecycle78 wrapper and revokes staged eligibility on reset, unqualified bus return, or bad bootstrap ledger. YAML new private header include; 24 root blocks parsed with ESPHome !secret support, deliberate_enable=false and HARD_DENY remain, native bind/arm/frame TX gates unchanged. IMPORTANT: no actual ACTIVE operational binding implemented, no fabricated epoch/peer/slot; G01/G02/G04 S62 operational closure unchanged and not retested. Full ESPHome compile/full regression/flash/bus TX NOT RUN; physical G05/G06 OPEN, EXP388 PARTIAL, installed V83 RX-only unchanged. Private S78 ZIP SHA256 5b6ce9e9f32ea92e1d5912a39d27640e763b8e831673f6674eea03e989accade. Next engineering step must explicitly design/test a scoped TX policy-to-engine adapter, not claim TX working.

# 2026-10-21 S77 `V41-V5-S77-OPERATIONAL-ADMISSION-01`: RUNNING / PARTIAL native source integration; COMPLETE / POSITIVE targeted OFFLINE host C++ tests S76/S77. S76 private baseline extended with `OperationalAdmission77` separate from physical `LiveEvidence23`: S62 accepted-risk config flags true, locally scoped generation explicitly NOT a proven controller epoch, manual deliberate-enable and live healthy RX/B11D/DE-low/bootstrap/transport criteria, and revocation on gap. Native runtime evaluator and existing RX-only YAML callback connected, but YAML deliberately sets `deliberate_enable=false`, bootstrap proof and transport resolution false; NO native bind, arm, TX or profile acceptance. YAML 24 roots parsed, strict GCC tests PASS; full regressions and actual ESPHome target build/flash/live XTR test NOT RUN. Installed V83 RX_ONLY/HARD_DENY unchanged. G01/G02/G04 remain S62 operational risk-closed (do not repeat); G05/G06 physical OPEN, EXP388 PARTIAL. Private ZIP SHA256 81210313f5e831831330f12220c4e9c30666c90ceae8bbeae8b328420cace15f. Next: separate target build and source-backed, explicitly user-initiated scoped native TX integration; do not fabricate epoch or peer evidence.

# 2026-10-21 S76 `V41-V5-S76-ACCEPTED-RISK-QUARANTINE-01`: COMPLETE / POSITIVE OFFLINE SOURCE/HOST only. Private S75 source updated with accepted-risk POLICY flags G01/G02/G04 true for unchanged installation, NOT physical evidence: epoch_verified/peer_absent/physical_slot_measured remain false and TX stays HARD_DENY. Repeated R6-P24 gap still revokes old session immediately; 3 successive CRC-complete healthy callbacks with MCU DE low release RX-only passive quarantine, never bind/arm or TX. Existing S75 and S76 strict GCC tests PASS (2 targeted); 24 YAML top blocks parsed, 38 earlier suite NOT rerun, target ESPHome compile/flash/XTR TX NOT RUN. G05/G06 physical OPEN, EXP388 PARTIAL, deployed V83 RX-only unchanged. Private ZIP SHA256 ee7e153214e2f15f9141abf3a83cf85dedfe771b3a76872bc286fefb5d767531. Active V5 gateway is STILL NOT enabled; next integration must separate scoped operational policy from physical proof without fabricated attestations.

# 2026-10-21 S75 `V41-V5-S75-REPEAT-GAP-REVOCATION-01`: COMPLETE / POSITIVE offline source/host 38/38; existing R6-P24 callback gap count now revokes native binding on **every** counter change (two successive events host-tested), replacing S73 one-shot static V49 latch; original V49 witness unchanged. 24 YAML root blocks verified, private S75 ZIP SHA ad5c8831da0706989ae949520f99e6529afb0a11337ea559bbd59fb83a42a5b1. Target ESPHome compile, flash and TX NOT RUN. V83 RX_ONLY/HARD_DENY unchanged. G01/G02/G04 S62 accepted-risk closure unchanged; G05/G06 physical OPEN; EXP388 PARTIAL. Report Research/V5DCM/V41_TO_V5_S75_REPEATABLE_CALLBACK_REVOCATION_OFFLINE_RESULT_20261021.md.

# S74 (2026-10-21): exact private S73 source re-verified; bundled strict GCC C++ host runner re-executed 37/37 PASS, physical TX=0. Real ESPHome/ESP-IDF compile NOT RUN: toolchain absent. No source, YAML or deployed V83 changes. V49 passive return and R6-P30D 32/32 are not a new epoch. V41-V5-S74-TARGET-BUILD-READY-01 RUNNING / PARTIAL. Report Research/V5DCM/V41_TO_V5_S74_TARGET_BUILD_HANDOFF_20261021.md.

# S73 2026-10-21: offline source plus 36 host checks positive; passive bootstrap counters wired into private native runtime; no real embedded build, session acceptance, TX or flash. RX-only production unchanged. Research/V5DCM/V41_TO_V5_PASSIVE_BOOTSTRAP_HANDOFF_S73_20261021.md

# 2026-10-21 V41-V5-V49-CALLBACK-01 RUNNING / PARTIAL: existing V49 passive bus-return observation now revokes NativeEsphome23 session in private RX-only source. No qualified next epoch, rebind, ESPHome build, flash or TX; installed V83 unchanged. Details Research/V5DCM/V41_TO_V5_V49_CALLBACK_REVOCATION_PARTIAL_20261021.md.

# V41-V5-RUNTIME-HANDOFF-01 — RUNNING / PARTIAL source integration (2026-10-21). Baseline prior verified V4.1→V5 private recovery candidate and installed V83 RX_ONLY. One change: existing NativeEsphome23 recovery API resets owned transport before native engine recovery and never automatically arms. Six selected generic C++ host tests PASS; no genuine ESPHome compile, callback binding, flash or TX. Semantic16 existing delayed 0708 path preserved. Abort on stale epoch, DE problem or in-flight work; discard candidate and retain V83. G01/G02/G04 accepted-risk closure unaffected. Report Research/V5DCM/V41_TO_V5_NATIVE_RUNTIME_HANDOFF_PARTIAL_20261021.md.

# V41-V5-FUNCTIONAL-RECOVERY-01 — RUNNING / PARTIAL integration; selected source-only C++ tests COMPLETE / POSITIVE (2026-10-21). Hypothesis V4.1 EXP388 recoverable pending semantic intents must be canceled on controller-loss without clearing physical in-flight operations; prior V5 lacked direct native-engine recovery API. One source intervention: add recover_controller_loss to UnifiedNative23 and Engine17; old/new epoch checked, outstanding/semantic AwaitCurrentRead/AwaitRepublish fail closed, recoverable states clear cache and pending semantic via cold native reset. Two new host tests and existing full merged/negative/semantic host tests 5/5 PASS. Full regressions and embedded compile NOT RUN, YAML unchanged, no bus TX or flash; native ESPHome callback not connected, EXP387 0708 semantic re-arm remaining. Rollback S65-S70 private source/V83 RX_ONLY unchanged. S72 line stopped, S62 G01/G02/G04 not reopened. Report Research/V5DCM/V41_TO_V5_NATIVE_FUNCTIONAL_RECOVERY_PARTIAL_20261021.md.

# V5-NATIVE-S72-EVIDENCE-TO-SESSION-01 — COMPLETE / POSITIVE standalone OFFLINE C++ host (3/3 compiler+run); runtime/native YAML integration RUNNING / PARTIAL / NOT IMPLEMENTED (2026-10-21). Baseline S65–70 confirmed native bind/profile/arm APIs but unused, supervisor join false. One new private C++ header and test only; demands consistent nonzero epoch, peer, physical slot, B11D, RX, DE low, profile flags, revokes on epoch switch, defaults deny. Evidence booleans are caller-supplied and untrusted until independently backed: no fake runtime qualifications. No actual ESPHome compile/flash/TX or semantic proof; rollback discard standalone header, leave V83 RX_ONLY unchanged. G01/G02/G04 scoped accepted risk retained; G05/G06, B11D first fault and EXP388 open. Report Research/V5DCM/V5_NATIVE_S72_SESSION_EVIDENCE_CONTRACT_OFFLINE_RESULT_20261021.md.

# V5-NATIVE-S71-BINDING-BUILD-PREFLIGHT-01 — RUNNING / PARTIAL session-integration diagnosis, 10/10 offline source-check COMPLETE / POSITIVE, 2026-10-21. Last confirmed V83 RX_ONLY/HARD_DENY, S65–70 exact source. One non-transmitting checker added; initial 9/10 from obsolete V4.1 bus-health ID assumptions, corrected to V5 ids and 10/10 PASS. APIs bind_qualified_controller_session/install_cm930_reviewed_profile/arm_scoped exist but YAML invokes none and supervisor join is false. No actual ESPHome/PIO toolchain; no embedded compile or TX; no actual source implementation change. Positive: source constraint visible and reproducible. Negative/inconclusive: no live semantic result, no binding. Abort any attempt to fabricate proof booleans or auto-enable TX; rollback none. EXP388 PARTIAL, B11D first fault OPEN. Report Research/V5DCM/V5_NATIVE_S71_SESSION_BINDING_BUILD_PREFLIGHT_20261021.md.

# V5-NATIVE-S65_S70-INTEGRATION-AUDIT-01 — S65/66/69/70 COMPLETE / POSITIVE OFFLINE; S67/68 RUNNING / PARTIAL source/host only (2026-10-21). Baseline verified S64 source SHA 28588fd60919f68e86d4b6655d75fa687b7056c4af5bb42be698a4e39a947f36, installed V83 RX-only, V49 fallback. One scoped test change: original runner FAILED at test_safe_reset.cpp:63 because legacy test expected DE LOW after ambiguous FIFO admission (false for S64 fail-closed); updated test assertion and added known deferred-drain-success + unknown-admission-sticky tests. Full 28/28 audit, 8 variant tests and 34 original host test lines PASS, 42 PASS lines in combined log; 24 YAML root blocks 403 IDs, byte-identical production YAML and no non-generated V5 production-source changes from S64. Negative result preserved; full ESPHome/IDF build/flash/TX NOT RUN. Native session remains unbound with false runtime evidence, C2/live semantic acceptance unproven. G01/G02/G04 risk accepted and not reopened; G05/G06 physical recovery OPEN. Rollback V83/S64 unchanged. Private ZIP SHA 12967fa652c572ba2b0e032cf527e1cfa5321e69f5d1af62c6846d97d8278928. Report Research/V5DCM/V5_NATIVE_S65_S70_COMBINED_OFFLINE_RESULT_20261021.md.

# 2026-10-21 EXTERNAL ATEC V3 ODU-FAN SOURCE/CAPTURE CROSS-CHECK — NON-EXPERIMENT OFFLINE ANALYSIS, NOT ATEC LIVE TEST. Compared external V3 YAML, original Connect2.1.105 CM930 sensor definitions and archival Oct03 ATEC/DCM03 raw 0x0F FC16 0820/18: 13/13 CRC-valid ODU group frames at t78.284–334.689, 2091=0,2092=70,2094=300(bit2=1),2095=130, values constant. Source V3 keeps last-seen ODU values without register-specific timeout; generic last-any-HP-update is not freshness. No synchronized physical fan event; actual bug/root cause UNKNOWN. Future observational baseline: natural OFF/ON/OFF physical state plus raw values, last 0820 update timestamp and framer statistics; no bus TX, flash, forced mode changes, or XTR verification. [Sanitized detail](ATEC_V3_ODU_FAN_TELEMETRY_DIAGNOSIS_20261021.md). Preserve S63/S62/FAS1/EXP388 unchanged.

# S64 (2026-10-21): COMPLETE / POSITIVE offline private source correction only; exact S60 base verified, one UART adapter header patched, 3 generic C++ tests PASS. No full ESPHome/IDF compile, flash or bus TX; G05/G06 physical still OPEN. RX-only V83 and G01/G02/G04 S62 decision unchanged. See Research/V5DCM/V5_NATIVE_S64_KNOWN_FIFO_DRAIN_RECOVERY_SOURCE_OFFLINE_RESULT_20261021.md.

# V5-NATIVE-S63-FAIL_CLOSED-CONTRACT-01 — COMPLETE / POSITIVE **OFFLINE REFERENCE MODEL ONLY** (2026-10-21); actual S60/V5 code integration PREPARED / NOT RUN. Baseline V83 RX_ONLY/HARD_DENY, V49 fallback, EXP388 RUNNING/PARTIAL, B11D original first fault OPEN. Hypothesis conservatively model DE HIGH/unresolved in-flight UART drain, fault propagation and epoch-owner revocation. One change: standalone Python 11-test contract model (11/11 PASS), no firmware changes, no CRC/frame payloads or bus TX. Negative/failure cases denied as intended: failed DE release, pad HIGH, UART not empty, sticky fault, stale/zero epoch; positive safe model reset still revokes owner. Actual private S60 raw ZIP was unavailable via Library/container; therefore host C++ regressions, original YAML audit, ESPHome compile, flash, physical DE and XTR application acceptance NOT RUN. No user permission for actual TX requested. S62 G01/G02/G04 closure maintained. Abort/source drift: never treat standalone reference as firmware safety proof. Rollback none. Report Research/V5DCM/V5_NATIVE_S63_FAIL_CLOSED_CONTRACT_OFFLINE_RESULT_20261021.md.

# V5-NATIVE-S62-CSV-TIMING-ACCEPTED-RISK-CLOSEOUT-01 — COMPLETE / POSITIVE OFFLINE RAW CAPTURE/TIMING ANALYSIS (2026-10-21); active XTR TX/flash PREPARED / NOT RUN. User specifically accepts remaining G01/G02/G04 engineering risks for unchanged XTR installation and directs that those THREE issues be administratively COMPLETE / POSITIVE (G02 CONDITIONAL) and NOT raised repeatedly as future proof prerequisites. One offline change: CRC16/9600-8E1 decode of four NEW digital Saleae-like CSV sources (26.132s, 267.387s, 37.949s, 181.740s); exact 222 + 2280 + 323 + 1566 complete CRC-good RTU frames (3 recording-boundary fragments); 716 native 0x0F FC16 requests, zero native FC23, zero native short ACKs. 2-channel long 2280/2280 EOF-to-channel7 marker pair median19.268ms (p05 17.666/p95 21.661); all 373 native FC16 followed by at least 102.311ms observed quiet to next physical TTL frame (within 4 files all native minima around 102.31ms). At 9600 8E1 proposed native short ACK 8bytes =9.167ms wire, physically fits idle but NOT semantic approval/accepted slot proof; no new TX. G01-09 video user controller restart prior POSITIVE preserved; G02 Oct14 topology/peer CONDITIONAL POSITIVE preserved; reported historical long-working V4.1 corroborates user's risk acceptance. Original Connect firmware 2.0.18/2.1.105 direct stable CM930 0x0F ABI, ATEC V3 external source/claim only and no keys/auto-TX reused. Standalone S62 decoder metric assertions PASS, per-frame timing CSV contains no payload; 7-item sanitized ZIP SHA cf00c7b77bf3ca14aa20797c113be9e74ae547226f134e7376f40d32447b17c0, 6-entry manifest/CRC clean. Status of G01/G02/G04 **CLOSED BY USER ACCEPTED RISK**, not physical-proof labels and don't revisit unless wiring/peer/source contradiction or explicit user request. V83 RX_ONLY/HARD_DENY, V49 fallback, EXP388 PARTIAL, B11D first startup OPEN. Separate DE fail-high recovery and real ESPHome compile still NO-GO for automatic native TX; later manual active experiment needs scoped user action. Report Research/V5DCM/V5_NATIVE_S62_TIMED_TTL_RISK_CLOSEOUT_20261021.md.

# V5-NATIVE-S61-EPOCH-PEER-SLOT-RECONCILIATION-01 — COMPLETE / POSITIVE OFFLINE SOURCE/TEST (2026-10-21); S61-PA-01 PREPARED / NOT RUN physical passive measurement. Hypothesis evidence gates labeled globally UNKNOWN may already have historical conditional scoped completion but lack current physical wiring slot proof. Source reviewed S60 private source candidate and GitHub G01-09/G02-09..11B/G03/G04. Verified G01-09 video-intervention anchored local restart, not rail; G02 user-accepted conditional unchanged installation (not exclusive electrical proof). One offline scope change: new generic no-output logic analyzer CSV / edge verifier; 14/14 existing S60 YAML predicates and 4/4 analyzer host tests PASS, ZIP 6 members CRC/manifest valid SHA 546f3a2a62fcb336f9325d7eddc70609b228193253359d72b5adfa0b7ca00515. Proposed S61-PA-01 one passive probe action with GPIO18 RX/GPIO1 callback marker(if present)/GPIO21 DE same-time capture and ESPHome log, >=1MHz 9600 8E1 1-2min natural requests, no flash/powercycle/TX. Positive only physically paired EOF/callback/DE observation, negative if DE high/unexpected or observed impossible timing, inconclusive no native/ambiguous/clock misaligned. ABORT unexpected TX, RX faults, unverified safe probe ground, abnormal device; rollback remove analyzer and leave V83 RX-only untouched. NOT RUN controller physical epoch/peer/slot acceptance, semantics, ESPHome compile. G01/G02 prior recorded statuses retained; no false promoted authorizations. EXP388 RUNNING/PARTIAL, B11D first fault OPEN, V49 fallback. Full report Research/V5DCM/V5_NATIVE_S61_EPOCH_PEER_SLOT_RECONCILIATION_PASSIVE_PREPARED_20261021.md.

# V5-NATIVE-S60-FIRMWARE-AUDIT-CORRECTIONS-01 — COMPLETE / POSITIVE OFFLINE SOURCE/HOST (2026-10-21), ESPHome/physical PREPARED / NOT RUN. Baseline last user-confirmed V83-family RX_ONLY/HARD_DENY with V49 rollback; EXP388 PARTIAL and B11D first-fault OPEN. Hypothesis firmware review defects in S52-59 GPIO21 output-only read, duplicated DE evidence and ignored upper reset boolean can be corrected WITHOUT auto-TX or false controller qualifications. ONE controlled private source correction: four C++ header files, one separate complete YAML, eight legacy mock-fixture adaptations, pinned S52-58 exact parent 5e45798f... unchanged. GPIO21 input+output permits MCU-pad `gpio_get_level` per original ESPHome 2026.9.0 source (NOT transceiver probe). GuardedPort passes separate DE switch command/pad sample with conservative legacy denial. ScopedTransport23 and NativeEsphome23 propagate release failures and preserve sticky faults. Source-only ingress evidenceHeld remains false-unqualified; no bind/install/arm/current native session. Positive 28/28 ancestry/YAML/compile-negative audit including 24 blocks/403 IDs, 8/8 new guarded-host+reset tests and 34/34 corrected original host tests; clean ZIP replay exit0; 4/4 prohibited TX macros GCC refused. Negative OUTPUT_ONLY fake GPIO-high read=>0 correctly prevents FIFO/owner TX in host. No ESPHome toolchain, true compile NOT RUN. Physical DE/epoch/slot/B11D/root cause and semantic readback unresolved; do NOT flash. Private ZIP SHA e0c7fa49b58d9ef1c68cb90f7226ce42cc6bb2ce886c0c83e296f52299933561 (321), CRC and 320 manifest verified. Abort any uncertain DE or unknown epoch/slot; rollback none because no physical work. NEXT compile RX-only and independently review true physical DE. Report Research/V5DCM/V5_NATIVE_S60_FIRMWARE_AUDIT_CORRECTIVE_SOURCE_OFFLINE_RESULT_20261021.md.

# V5-NATIVE-FIRMWARE-PARITY-AUDIT-20261021 — COMPLETE / POSITIVE **OFFLINE SOURCE REVIEW** (2026-10-21), embedded/physical PREPARED / NOT RUN. Hypothesis prior S47–59 positive host tests and source completeness would reflect original Connect and GPIO/DE safety. Baseline user-confirmed V83 RX_ONLY/HARD_DENY, V49 rollback, EXP388 PARTIAL, B11D first-fault OPEN. One offline re-review: exact original supplied 2.0.18/2.1.105 firmware Python/930 flags + pinned S52-58 V5/YAML, historic ATEC/unknown model captures, public ESPHome 2026.9.0/IDF GPIO source; no code or device changed. Results 23/23 static source/firmware checks PASS; original S47-51 host GPIO fake-level fixture PASS, identical fixture using documented output-only input-read=0 compiles but fails its positive p.send assert (exit134). DEFECTS: GPIO21 gpio_get_level does not independently read output-only pin; native YAML bind/profile/arm calls ABSENT and qualifications always false; upper ScopedTransport23 reset discards lower reset bool and clears its own fault; twice io.de_is_high used as distinct switch/pin evidence; source_complete != end-to-end app-C2 readiness. Error to S41 source PROVENANCE: ATEC Oct03/unknown Sep24-25 miscalled local XTR; corrected additively, 5,138 CRC facts/24 same-timestamp pair findings kept. No ESPHome/IDF build, flash, physical slot/DE/controller acceptance; host result not live negative. Abort any TX promotion, DE HIGH/unknown or source drift. Separate sanitized offline audit ZIP SHA256 80a4cf155952b8bea56b5513f33ba50386d8e6f9735bf0fe4a127f7c9f45e0bb. NEXT corrective source contract GPIO mode, reset propagation, real session chain, real compiler, then user-scoped live test. Report Research/V5DCM/V5_NATIVE_FIRMWARE_VS_SOURCE_REVIEW_20261021.md.

# V5-NATIVE-SERVICE59-RECOVERY-GATE-PREFLIGHT-01 — COMPLETE / POSITIVE OFFLINE SOURCE/GUARD (2026-10-21), embedded/physical PREPARED / NOT RUN. Baseline user-confirmed V83-family RX_ONLY/HARD_DENY, V49 fallback, EXP388 RUNNING/PARTIAL, B11D initial fault OPEN. One offline change only: fresh audit of exact private S52-58 source (SHA 5e45798f3ea7bf7375920b1c73fdf20e926a4f0522f027d4f22c182786b01c3e) and actual GCC negative-compilation of four prohibited TX macros; no production code altered. Results 13/13 source checks and 4/4 expected TX compiler denial PASS, original ZIP CRC. First audit 12/13 false negative due missing SOURCE_CANDIDATE ZIP path, corrected auditor only and retained in report. esphome/pio absent: full embedded compiler NOT RUN. Existing source keeps UnresolvedInFlight fail-closed and reset requires leave_de_rx plus observed RX/DE LOW; actual stuck-DE recovery remains NO-GO. No XTR flash/TX, session, sender/slot/epoch or semantic test. Abort source mismatch, DE conflict, B11D fault or unknown slot; rollback none, RX-only unchanged. Private-free audit ZIP SHA 4e8bfbe4f326b4847e57900441d86846fdcf0f6568bd2a593c6384c9f62bc12b. NEXT full real ESPHome compile and separate safe recovery review, not cold restart bypass. Report Research/V5DCM/V5_NATIVE_SERVICE59_RECOVERY_GATE_PREFLIGHT_OFFLINE_RESULT_20261021.md.

# V5-NATIVE-SERVICE52-58-COMBINED-SAFE-RESET-01 — COMPLETE / POSITIVE OFFLINE SOURCE/HOST (2026-10-21), physical embedded/hardware PREPARED / NOT RUN. Baseline user-confirmed V83 RX_ONLY/HARD_DENY, EXP388 RUNNING/PARTIAL, B11D startup cause OPEN; V49 rollback. Hypothesis old GuardedPort::reset_rx_only incorrectly clears fault despite unsuccessful `PhysicalIo::leave_de_rx()`/DE HIGH after unresolved drain. One scoped source fix in separate candidate: requires successful leave + observed RX/DE LOW before clearing sticky fault. Positive new real-GuardedPort mocked-IDF 4/4 modes and 316/316 source checks; 4/4 forbidden TX flags rejected; pinned S47-51 full runner exit0 (V5 35/35 and S46 32/32). Source-only YAML byte-identical to parent (24 production blocks/403 IDs) and no new UART owner/DE driver. Negative source finding confirmed: earlier unconditional fault reset unsafe, not a live XTR result. Current physical unresolved DE HIGH cannot safely be repaired by this software-only test: NO GO. ESPHome/PIO unavailable, actual compilation NOT RUN; original C2/FC16 semantic acceptance, sender slot/epoch remain OPEN. Two early validator false positives corrected (YAML AST identity and existing #if macros mistaken for defines). Abort on unowned DE, incomplete drain, B11D fault, unknown physical slot; no physical device changed, no rollback needed. Artifact private SHA 5e45798f3ea7bf7375920b1c73fdf20e926a4f0522f027d4f22c182786b01c3e. Next actual embedded compile + hardware safety protocol. Report Research/V5DCM/V5_NATIVE_SERVICE52_58_COMBINED_SAFETY_OFFLINE_RESULT_20261021.md.

# V5-NATIVE-SERVICE47-51-COMBINED-UART-01 — COMPLETE / POSITIVE (2026-10-21, OFFLINE SOURCE/HOST ONLY). Last user-confirmed baseline V83-family RX_ONLY/HARD_DENY, V49 rollback; EXP388 RUNNING/PARTIAL, B11D first fault OPEN. Hypothesis original one-owner V5 NativeEsphome23/ScopedTransport23/GuardedPort can host a status-bearing borrowed existing UART physical IO replacing source defect write_array(void) fabricated acceptance/ignored flush, while preserving actual RX-only production. One change, five packages: S47 candidate source adapter+typed IDFUART; S48 FIFO/drain/DE fault model; S49 actual owner and B11D/watchdog same service; S50 full YAML 24 blocks/403 IDs and bus health preserved with pointer->reference source correction; S51 tests and replays. User S46 source SHA 9b4745c5f161ade47772b9c0f4c3f8ac5545deed663c3291099e904a94f6e2ba, 307/307 parent bytes unchanged. 356/356 source audit, new 4/4 C++ builds (strict,noexceptions,UBSan,Clang), 4/4 TX-denial builds, 35/35 inherited V5, S46 32/32, S45 28/28, separately pinned S44 24/24 S43 26/26 S42 25/25 PASS. Clean ZIP extraction replay exit 0. Host negative tests: missing reviewed budget/driver, wrong port, partially admitted FIFO, negative FIFO admission, drain timeout, unresolved in-flight bytes, DE switch/GPIO release failure and unqualified owner. Critical fail-state CAN LEAVE DE HIGH and thus BLOCK the bus: actual embedded/live TX NO-GO until safe recovery designed. Any source mismatch, B11D latch, DE conflict or unknown slot abort; rollback no hardware change; use verified V83 with V49 fallback if later needed. Current S47-51 candidate Service36 compile HARD_DENY and zero budgets, no user arm, no full ESPHome/IDF compiler installed, flash/TX NOT RUN. Physical sender/slot/epoch, Connect C2, semantic write UNKNOWN. 324 private ZIP entries SHA256 36a0b37dcac6210161f495f76bc007022d61b780c67b64d91688212998df3dcf; no protected source published. NEXT actual embedded compile, then separate safety/slot assessment and user-initiated live scope.

# V5-NATIVE-SERVICE46-TYPED-IDF-RECEIPT-RXONLY-OFFLINE-01 — COMPLETE / POSITIVE **OFFLINE ONLY** (2026-10-21); physical embedded test PREPARED / NOT RUN. Hypothesis: separate typed source model distinguishes FIFO admission, drain and DE-low result without mutating the original TX-flawed adapter or granting physical send. Verified baseline installed V83-family RX_ONLY/HARD_DENY, V49 fallback, EXP388 RUNNING/PARTIAL, B11D startup fault OPEN. One additive change: typed status ledger + pinned read-only IDF/ESPHome API type probe, separate NOT FLASHABLE S46 YAML include/30s log; 292/292 S45 parent bytes exact, 24 production root blocks/403 IDs/pins/HA/bus health unchanged. Positive offline S46 host-stub tests 7/7, compile-negative TX 4/4, source/YAML 32/32. Original S45 28/28 and S44 fixture PASS; original S43 26/26, S42 25/25 in their individually pinned archives, older provenance wrappers directly on later modified descendants yield S43 25/26 and S42 24/25 mismatch (preserved). Public IDF v5.3.2 header and ESPHome 2026.9.0 header APIs checked; true ESPHome/IDF target not compiled. Original write_array(void) and ignored flush remains an unresolved safety defect; no sender, slot/epoch, DE physical completion, native C2 or semantic readback proven. Abort any source mismatch, unqualified physical work, sticky B11D or output; rollback none (offline). Private ZIP SHA256 9b4745c5f161ade47772b9c0f4c3f8ac5545deed663c3291099e904a94f6e2ba (307). S47 next reviewed typed embedded adapter with actual compiler first, separate user-initiated live test later.

# V5-NATIVE-SERVICE45-ESPHOME-UART-IDENTITY-RXONLY-01 — COMPLETE / POSITIVE OFFLINE ONLY (2026-10-21); device/embedded PREPARED / NOT RUN. Hypothesis: original ESPHome UART id(thermia_uart) and original native V5 singleton saved UART object can be checked as SAME instance using a read-only driver-installed/port-index probe, without granting TX. User baseline V83 RX_ONLY/HARD_DENY; EXP388 PARTIAL; B11D first fault OPEN; V49 rollback. ONE source change family: two getter-only additions in existing V5 headers, one new S45 passive binding header, separate S45 source-only YAML brown health diagnostic; unchanged S44 private parent 275/275 members preserved, original S43 YAML unchanged. Positive: 6/6 host-stub C++ modes, 4/4 native/legacy TX flags denied, 28/28 source/YAML checks, original 24 top blocks+403 IDs, S44 24/24 and 3+5 tests, S40/S42/S43 4/4 host suites each, S25 35/35 PASS. Old complete S40 wrapper not rerun because S39 ZIP absolute dependency absent; current S40 host binaries passed. Negative controls reject wrong/missing UART binding, invalid port/driver; no real driver checked on XTR. No ESPHome embedded compile/flash, TX, abort-on-wire or semantic write. Abort source/hash mismatch, build authorization, missing driver, old B11D fault; rollback installed RX-only unchanged. Private S45 ZIP SHA256 737964f7d63a45f18e6db76296ad2e38e125d1059bf3712a2af30afa43ff8a1e, 292 files. NEXT S46 separate driver-status/typed drain embedded-source compile, no auto-TX.

# V5-NATIVE-SERVICE44-BORROWED-UART-DRAIN-SOURCE-01 — COMPLETE / POSITIVE OFFLINE SOURCE/HOST (2026-10-21); ESPHome compile/device TX PREPARED / NOT RUN. Hypothesis existing native PhysicalIo source treats void UART write + ignored flush return as successful delivery; one private separate source-only borrowed existing-UART FIFO-admission/typed-drain test can fail closed while RX-only unaffected. Baseline user-confirmed V83-family RX_ONLY/HARD_DENY, V49 fallback, EXP388 PARTIAL, B11D first fault OPEN; source S43 pinned SHA 85486e352c83... . OBSERVED SOURCE: exact ESPHome 2026.9.0 sets UART TX ring 0, write_array returns void, flush returns UARTFlushResult from uart_wait_tx_done; S43 adapter invents bytes written and ignores drain status. Controlled change new S44 abstract BorrowedDrainIo44 beside all 263/263 original S43 members unchanged, no production YAML changes; 24 blocks/403 IDs and original V5 bus-health untouched. POSITIVE 3/3 standalone C++17 host modes, 5/5 actual embedded/default source denials, 24/24 source/provenance tests, full parent S43/S42/S40 suite rerun PASS. Fault fixtures: FIFO partial/zero, scope loss, stale owner, busy/error drain, DE mismatch/failure; no real signal. NEGATIVE for prior assumption source-level drain guarantees physical completion; this is NOT a local XTR negative. UNKNOWN actual IDF executable, UART completion/slot, current semantic acceptance. No TX/flash, no device rollback. Abort source mismatch or any embedded output. Private SHA 20f8a16181c9d6f8c1504ff6ca86b2dde0655e59e0b7459cf2a47ec85724083e (275 members). Next S45 TX-disabled actual ESPHome port binding/source audit and eventual separately scoped user test.

# V5-NATIVE-SERVICE43-REAL-GUARDED-OWNER-JOIN-OFFLINE-01 — COMPLETE / POSITIVE (2026-10-21, SOURCE/HOST ONLY); embedded/physical PREPARED / NOT RUN. Hypothesis: callback safety can consult one actual existing V5 GuardedPort owner rather than synthetic owner booleans. User-confirmed V83 RX_ONLY/HARD_DENY, V49 fallback, EXP388 RUNNING/PARTIAL, B11D first fault OPEN. One offline source addition: source-only S43 read-only owner observer, two getter-only amendments and both actual existing B11D 50ms and watchdog 1s callback references, with no existing parser, TX, DE, HA or B11D fault change. 250/252 S42 members identical; S42 ZIP pinned SHA 61652c9f14d5... . New 4/4 C++ host modes PASS against original GuardedPort FakeIO, source+YAML 26/26, original 35/35 V5 host, S40 4/4, S42 4/4 and S42 25/25 independent source tests PASS. 4/4 forbidden TX builds correctly rejected. Synthetic DE-high owner classification never grants TX; negative cases rejected (unowned/mismatch, sticky, stale, DE mismatch, bad drain, latch reset). Not compiled under ESPHome, no bus traffic or semantic readback. Abort new output/ownership claim or source mismatch; rollback none, existing RX-only unchanged. Private archive SHA 85486e352c831e1f3849f9c1bd9097d8869c32956132ea63e71e483853b493bb. NEXT S44 borrowed UART physical drain/DE completion and safe single-writer source contract before any separately user-initiated live test.

# V5-NATIVE-SERVICE42-TX-SUPERVISOR-SOURCE-01 — COMPLETE / POSITIVE OFFLINE (2026-10-21); physical/XTR PREPARED / NOT RUN. Hypothesis: a metadata-only TX-aware shared callback contract can be layered over exact S40 source while preserving RX_ONLY and separating future guarded DE-high ownership from S40's unconditional high-DE fault. User-confirmed V83 RX_ONLY/HARD_DENY; EXP388 PARTIAL; B11D startup OPEN; V49 fallback. Single offline source addition: separate S42 YAML + no-output supervisor header, calls at actual B11D 50ms and watchdog 1s and brown/red existing health diagnostic. Parent S40 240/240 unchanged; 25/25 source checks, 4/4 S42 and 4/4 S40 host build modes, 35/35 inherited host, 4/4 TX-negative builds PASS. Original 24 top blocks/403 IDs, UART ownership, DE, B11D sticky, V5 parsing intact. Synthetic future owned-window classification does not authorize real TX; no ESPHome compile/flash/COM ERR check, owner/epoch/slot physical measurement, Connect application or semantic readback. Abort: source guard regression or any output; no hardware rollback, keep verified RX-only. Private SHA 61652c9f14d561c60c21471ae42b370f494f1cc90249f673f536019b7ffed739. Next S43: actual single-writer / same-lease TX-aware source gate and manual user-scoped test design, without ATEC TX defaults.

# V5-NATIVE-SERVICE41-XTR-HOSTTIME-SLOT-PROVENANCE-01 — COMPLETE / INCONCLUSIVE (2026-10-21) for hypothesis that historical logger timestamps establish independent electrical native TX slot. User-verified baseline V83 RX_ONLY/HARD_DENY, V49 rollback, EXP388 PARTIAL, B11D first-fault OPEN. One offline step: new CRC/FC16/FC03 shape and immediate response-adjacency replay of five *original XTR* captures, plus S36 source ancestry cross-check. 5,138/5,138 CRC-valid, FC16 337/306 immediately matched, FC03 122/106; 24 FC16 pairs equal host timestamps though an 8-byte 9600 8E1 ACK occupies ~9.17ms. Positive offline 9/9 generic assertions; negative to treating host equality as actual physical EOF; source identity/slot/epoch and missing non-adjacent replies remain inconclusive. No ESPHome compile, flash, user hardware action or TX. Abort: any physical-slot claim from host timestamps or incorrect S36=>S40 source equivalence; rollback: unchanged installed RX-only. Next S42 exact current private S40 source review, bounded risk-accepted experimental TX build plan only.

# V5-NATIVE-SERVICE40-ACTUAL-CALLBACK-JOIN-GATE-OFFLINE-01 — COMPLETE / POSITIVE OFFLINE (2026-10-21), physical XTR/ESPHome PREPARED / NOT RUN. Hypothesis: S39 FakeIO shared owner is proven on device by the S36 conditional dual-macro boot claim and 50ms B11D plus 1s DE watchdog references. Last verified device V83 RX_ONLY/HARD_DENY, EXP388 PARTIAL, B11D first-start fault OPEN; V49 fallback. Prior S39 ZIP 9ecae2f2... pinned, 230/230 files unmodified. ONE change in separate private draft only: add read-only callback witness to the two actual ESPHome callback sites and replace premature set_same_owner_supervisor_wiring(TRUE) boot-time assumption by explicit FALSE. Positive offline: same service pointer, same boot, both recent callbacks and DE-low possible, but unconditional zero TX authority; missing/stale callback, differing owner, boot mismatch, legacy activity, DE/pin disagreement, high DE or B11D sticky deny. New C++ strict/noexceptions/UBSan/simulated-defines 4/4 PASS; S40 21/21 source checks, old V5 35/35 host, RX-only compile refusals 40/40, S39 12/12 audit PASS. Original 24 top-level YAML blocks/403 ID fields and inherited 198 HA names/IDs preserved. No ESPHome embedded compile, flash, live owner/slot/epoch/peer qualification, actual TX, Connect acceptance or semantic write; physical result PREPARED/NOT RUN. Abort on source provenance mismatch or any active output; rollback user-running V83 unchanged, V49 retained. Private ZIP SHA 47af7ec6..., report Research/V5DCM/V5_NATIVE_SERVICE40_CALLBACK_OWNER_WITNESS_OFFLINE_RESULT_20261021.md. NEXT independent local XTR slot evidence then separately reviewed physical TX test, not a blind build-flag grant.

# V5-NATIVE-SERVICE39-ONE-OWNER-LEASE-TX-HOST-01 — COMPLETE / POSITIVE OFFLINE SOURCE/HOST (2026-10-21), XTR physical PREPARED / NOT RUN. Hypothesis: existing S38 ScopedTransport23 owner may be safely observed by BOTH original B11D and watchdog loops, with one lease, without modifying RX_ONLY ESPHome baseline. Last verified device V83-family RX_ONLY/HARD_DENY, EXP388 RUNNING/PARTIAL, real B11D startup mismatch OPEN; S38 ZIP f1f5c14c... verified. ONE controlled source addition: host-only TxOwnerLease39, same-transport pointer join, current-request CRC, epoch, token/slot receipt checks and sticky fault/revoke; no changes to 223 inherited original S38 archive members, including 24 YAML blocks/198 HA entities/V83 supervisor. Positive: 4 separate C++17 macro-mode host runs + strict noexceptions & UBSan PASS (6/6); only dual flags permit FakeIO full 36-response startup/32-page/runtime/0864/4/FC03 simulation. Negative controls wrong owner, no arm, slot absent, expired mock slot, CRC/token replay, DE switch/GPIO mismatch, legacy actor activity, drain fail, no rearm. ESP_PLATFORM and ARDUINO compiler rejection 2/2 as designed. Inherited old 35/35 host, S36 40/40, S38 14/14, S39 12/12 provenance checks PASS. No ESPHome compilation, no live TX/flash, no true hardware timing/protocol C2/app/Online or semantic acceptance. Abort on missing independently validated epoch/slot, active peer, B11D/DE faults; user V83 left unchanged, V49 fallback. Private ZIP SHA 9ecae2f2..., 230 members; report Research/V5DCM/V5_NATIVE_SERVICE39_ONE_OWNER_TX_HOST_OFFLINE_RESULT_20261021.md. NEXT S40 separate scoped embedded TX build target only after real dual-supervisor/owner/slot review, not automatic transmit.

# V5-NATIVE-SERVICE38-XTR-W4-VERSION-GEOMETRY-TX-HOST-01 — COMPLETE / POSITIVE OFFLINE (2026-10-21), physical XTR PREPARED / NOT RUN. Hypothesis: earlier completed local XTR S11D FC16 0864/count4 cannot be processed by S37 native Service23 because firmware source W4.bit8 nominal selector has 12 addresses; version/cache/app receipt mistakenly require count12. Baseline user-running V83-family RX_ONLY/HARD_DENY; EXP388 PARTIAL and original B11D startup mismatch OPEN; S37 private SHA 6c228cdc..., RX_ONLY YAML unchanged SHA 55c6b1aa.... One functional offline correction in two C++ headers only: recognize strict 0864/count4 in existing XTR controller-cache staging; after ACK completion record raw0867; CM930 W4.bit8 local receipt accepts only physical count4, keep original 75 selector ranges and 31/33 source requirements. Prior evidence local completed S11D (reported raw0867=242, original S11D raw bytes not freshly audited), original Connect2.1.105 W4 bit8 2148..2159 verified in user AppFS, ATEC V3 EXTERNAL SOURCE/CLAIM not XTR proof. Baseline strict source probe source rejected 0864/4, accepted nominal 12; new mock TX-capable dual-flag full32 initial/runtime+0864/4+FC03 cache and fail-closed slot revocation PASS. Negative: 0864/12 physical rejected, CRC bad denied, single/zero macro FakeIO writes0, no automatic profile/Online; tests 4 host variants + UBSan PASS, existing 35/35 host, RX-only 40/40 compiler/source, new 14/14 SHA/provenance checks PASS. ASan runtime blocked environment ulimit, no ASan success claim. Real ESPHome build, physical TX and device readback NOT RUN; abort/discard on geometry, CRC, owner/DE, epoch, safety or stale-source issues; rollback unchanged user V83 with V49 fallback. Confidential private ZIP SHA f1f5c14c...; public report Research/V5DCM/V5_NATIVE_SERVICE38_XTR_W4_VERSION_TX_HOST_OFFLINE_RESULT_20261021.md. Next S39 separate TX candidate owner/slot work, not uncontrolled live transmission.

# V5-NATIVE-SERVICE-37-EMBEDDED-BUILD-PREFLIGHT-01 — COMPLETE / INCONCLUSIVE (2026-10-20) for full ESPHome embedded compile; supplementary source/host checks COMPLETE / POSITIVE OFFLINE; physical XTR PREPARED / NOT RUN. Hypothesis: S36 private RX-only candidate (ZIP SHA 39f3901d..., YAML SHA 55c6b1aa...) compiles unchanged under ESPHome/ESP-IDF. User-confirmed baseline V83-family RX_ONLY/HARD_DENY, EXP388 PARTIAL, B11D actual startup source OPEN; V49 rollback, FAS1 add-on no distinct flash proof. ONE controlled offline action: toolchain availability + source/portable component build readiness audit, with isolated future compile-only script; no staged YAML or runtime/source/header modification. Toolchain absent: esphome/platformio unavailable; uv PyPI resolution failed with DNS. Driver exited3 BEFORE ESPHome config/codegen/build: full embedded compile NOT RUN, hypothesis unresolved. Positive source evidence: original S36 35/35 host test executables, 40/40 safety/negative compiler checks PASS; S37 17/17 preflight checks PASS; local portable bridge 6/6 source C++17 host compile and linked TX-disabled stub PASS; pinned external public component fetched by GitHub at exact declared commit. Negative criteria: actual ESPHome schema/compiler/linker failure with available toolchain; not observed. INCONCLUSIVE: embedded compile compatibility; no firmware produced. Abort/discard on failed TX build denials, source drift, missing external pin, or real output path; no device touched/rollback needed. Future run scripts use synthetic secrets, esphome config/compile only and delete temporary binaries; never flash. Private ZIP SHA 6c228cdc0dd462f719edcf19714a3fcc26453f6cabeaf3247c9b01e4fb49257c. Public report Research/V5DCM/V5_NATIVE_SERVICE37_ESPHOME_BUILD_PREFLIGHT_OFFLINE_RESULT_20261020.md.

# V5-NATIVE-SERVICE-36A-RX-ONLY-BUILD-GATE-OFFLINE-01 — COMPLETE / POSITIVE OFFLINE (2026-10-20); device PREPARED / NOT RUN. Baseline last user-confirmed V83-family RX_ONLY/HARD_DENY, V49 rollback, EXP388 PARTIAL, B11D OPEN; authentic S35 RX supervisor restored, S23 newer TX flags not banned by original header. Hypothesis single or paired S23 TX owner flags could bypass earlier V42-only compile refusal in staged RX target. ONE source change: fail-closed header imported at staged ESPHome includes and native S23 header, rejects any one of four known legacy or newer TX flags; preserves original TX implementation privately but all flags forbidden in this target. Positive 15/15 flag combinations compiler-rejected, zero-flags host compiler pass. Negative any flag compiles; inconclusive ESPHome toolchain NOT RUN. No device/TX/flash. Abort on guard bypass/source change; rollback discard private patch, running V83 unchanged. Report Research/V5DCM/V5_NATIVE_SERVICE36_RX_ONLY_HARD_DENY_OFFLINE_RESULT_20261020.md.

# V5-NATIVE-SERVICE-36B-COMPLETED-ADU-RX-FANOUT-OFFLINE-01 — COMPLETE / POSITIVE OFFLINE (2026-10-20); device PREPARED / NOT RUN. Baseline gated S36A RX-only source, user V83-family RX_ONLY/HARD_DENY, EXP388 PARTIAL and B11D startup fault OPEN; prior V80/S30/S33 already established V43/V44B skipped complete ADUs with trailing partial in original source. Hypothesis can feed each original V5 CRC-validated completed ADU to still-unbound V43/V44B hooks without assuming physical EOF or modifying B11D. ONE change after 36A: pure C++ per-completed ADU visitor replaces previous tail-empty-gated RX-hook wrapper, reuses original guard expressions, one existing UART callback/parser. Positive strict/noexceptions/ASan+UBSan synthetic extracted-original-V5-parser tests 3x46 assertions PASS: split, coalesced, complete+partial and CRC-bad rejection; full 35/35 C++ host and 40/40 source/compile/YAML verifier PASS; 24 top blocks/198 HA identity pairs/other RX and safety code unchanged. Negative any dropped/duplicate/unfinished frame or compiler allowing TX; on-device behavior INCONCLUSIVE/NOT RUN. No actual UART TX/flash. Abort on CRC/parser/HA/B11D regression; rollback user V83 unchanged. Private ZIP SHA 39f3901dc3fc33a4874721465be6c9ca61fedd842e1976b6c764b8e5e37be7bd; staged S36 is NOT embedded compiled/flash-ready. Report Research/V5DCM/V5_NATIVE_SERVICE36_RX_ONLY_HARD_DENY_OFFLINE_RESULT_20261020.md.

# V5-NATIVE-SERVICE-35-V83-ORIGINAL-SUPERVISOR-RESTORE-OFFLINE-01 — COMPLETE / POSITIVE OFFLINE (2026-10-20); physical XTR PREPARED / NOT RUN. Hypothesis: authentic user V83 package supplies exact original inherited missing safety header, restoring S34 source closure without YAML/control mutations. User-verified baseline running V83-family RX_ONLY/HARD_DENY, EXP388 RUNNING/PARTIAL, B11D first fault OPEN and FAS1 supplemental source not independently flashed; V49 rollback. Prior S30/31/34 found missing original supervisor, S32 corrected spurious historic raw22-XTR attribution. Exactly ONE private source change: restore byte-identical original V83 supervisor (SHA 26fecbe0...) from verified original ZIP SHA f3b5d994... into S34 copy; no YAML semantics changed, S35 alias same SHA 4d8f8571... as S34, no new UART/DE/TX. Source positive: 64/64 direct includes present and original V45/FAS1 parity, 24/24 top blocks, 197 original HA identity pairs +1 diagnostic preserved. Host positive: original V83 3x78313; original FAS1 3x200036; 34/34 S35 compiled host programs, new S35 test strict/noexceptions/sanitizers PASS; 22/22 standalone and 26/26 with original archives exact-source audit PASS. Negative controls: V83 V42 legacy TX build flags refuse compile; no profile/session/arm method call; newer S23 dual-mode flags NOT rejected by original header (host compile exploration), so do not claim universal future TX hard-DENY. INCONCLUSIVE/NOT RUN for ESPHome build, physical UART, current XTR original Connect APP33/Online, B11D fault cause, callback effects. Abort any source pin mismatch or TX attempt; hardware not touched; rollback V83 unchanged, V49 available. Report Research/V5DCM/V5_NATIVE_SERVICE35_ORIGINAL_V83_SUPERVISOR_RESTORED_OFFLINE_RESULT_20261020.md, private ZIP SHA c89287f3.... NEXT S36 explicit newer build macro block + read-only callback fix source review.

# V5-NATIVE-SERVICE-34-PASSIVE-VERSION-WITNESS-OFFLINE-01 — COMPLETE / POSITIVE SOURCE/HOST (2026-10-20), actual XTR PREPARED / NOT RUN. Hypothesis: connect receive-only 0867 version evidence to the existing V5 parser/HA without calling S29 live profile admission, binding controller session, or TX. User-verified baseline V83-family RX_ONLY/HARD_DENY, EXP388 PARTIAL, unresolved B11D boot mismatch; original S29 private source missing authentic V83 supervisor and NOT standalone compile-ready. Exactly ONE private staged passive feature: new pure observer header, one per-completed-original-V5-ADU observer call, one extra HA diagnostic text sensor. Targets received 0x0F FC16 0864/count4 register0867 and source-range candidates only; positive offline: strict frame geometry and CRC, raw242/232/22 candidate, conflict and fault visibility without claim of local XTR provenance; all session/epoch/profile/TX authority FALSE. Negative controls: wrong slave, ACK, 12-word geometry, CRC corruption, version mismatch, unsupported/no-source and synthetic repeated242 never authorize. Results existing S29+S34 33/33 C++17 host executables PASS, targeted observer 3/3 strict/noexceptions/ASan+UBSan PASS, reversible S34 YAML insertion PASS, exact original 24 blocks/197 HA tuples + 1 diagnostic preserved. No ESPHome compiler, physical TX, flash, user test or real controller observation. Abort if expected source hashes/delta or RX safety checks drift; rollback live V83 unchanged and V49 fallback. Missing original RX supervisor and V83/S29 native RX-hook differences remain OPEN; staged S34 NOT FLASH READY. Report Research/V5DCM/V5_NATIVE_SERVICE34_PASSIVE_VERSION_WITNESS_OFFLINE_RESULT_20261020.md. Private ZIP SHA 09ac0e63e2d620355d1fe572b46679cbf56ea7a837d2ea21d592ec574f8e0dd6.

# V5-NATIVE-SERVICE-33-STAGED-RX-PROFILE-WIRING-OFFLINE-01 — COMPLETE / POSITIVE OFFLINE AUDIT (2026-10-20); device PREPARED / NOT RUN. Hypothesis: S29 tested version/profile gate is actually called from staged ESPHome with independently confirmed same-epoch XTR provenance; compare to user supplied V83 FAS1 exact YAML. Baseline user-verified V83 RX_ONLY/HARD_DENY; EXP388 PARTIAL; B11D first mismatch OPEN. Exactly one source-only change: construct standalone reachability and generic original-parser callback fixture without modifying firmware. NEGATIVE to claimed integration: source methods bind/profile-install/refresh/scope-arm have no staged YAML call site; RX observer passes false epoch/peer/slot/profile; send gate stays unbound. Positive audit: 14/14 source checks, exact original StreamParser 8/8 C++17 and 8/8 ASan+UBSan PASS, existing S29 host runner 32/32 PASS. Per-ADU coalescing gap and B11D warm-join are previously V80/V83 described, reverified source-only, NOT proven real B11D cause. No ESPHome compile, flash, UART/DE TX or native controller result. Abort criteria source pin/check failure; rollback no hardware touched, user V83 remains. Next authentic V83 RX supervisor and safe passive per-ADU wiring review; no active experiment. Report Research/V5DCM/V5_NATIVE_SERVICE33_PROFILE_WIRING_RX_SOURCE_AUDIT_OFFLINE_RESULT_20261020.md.

# V5-NATIVE-SERVICE-32-PROVENANCE-RECONCILIATION-OFFLINE-01 — COMPLETE / POSITIVE OFFLINE (2026-10-20), physical XTR PREPARED / NOT RUN. Hypothesis: prior S29 and V92/V93 '19 local XTR raw22' was model-provenance error against earlier V64 and locally user-run S11D raw242. Baseline user-running V83 FAS1 RX_ONLY/HARD_DENY, EXP388 RUNNING/PARTIAL, B11D OPEN; no TX/flash. Exactly one controlled change: SHA-pinned offline classification + strict request/ACK byte count/CRC verification of seven original logs, genuine Connect info.py version decoder and 2.1.105 info product map; no production source change. Positive 2500 CRC-valid FC16 requests, 1365 ACKs, 0 invalid candidates; Eco5 raw232=48, ATEC raw22=12, older MODEL-UNCONFIRMED raw22=7; no verified local XTR raw22. Prior user local S11D COMPLETE/POSITIVE reported raw0x00F2=242 but S32 did NOT reparse its original raw capture and cannot establish current V83 epoch. Product1337 code1 in the three old Sep/Oct files also not XTR-attributable, vendor map gives XTR M code22/23. Offline verifier 6/6 PASS incl CRC/length/hash negative. Original older observations retained; incorrect LOCAL-XTR attributions DISPROVEN / SUPERSEDED. S29 still not flash-ready; no current profile or Online claim, no ESPHome compilation or physical TX. Rollback unchanged V83 RX-only and V49 backup. Next exact original V83 supervisor source, source callback reconciliation. Report Research/V5DCM/V5_NATIVE_SERVICE32_VERSION_IDENTITY_PROVENANCE_CORRECTION_OFFLINE_RESULT_20261020.md.

# V5-NATIVE-SERVICE-31-V49-V83-PROVENANCE-OFFLINE-01 — COMPLETE / POSITIVE (offline audit only), device PREPARED / NOT RUN, 2026-10-20. Hypothesis: the newly supplied V49 and V83 FAS1 ZIPs close the inherited source gap while confirming S29 source ancestry. Baseline: last user-confirmed V83 RX_ONLY/HARD_DENY, EXP388 RUNNING / PARTIAL, B11D first-alignment OPEN. One change: read-only source/manifest/callback comparison; no changes to production YAML or hardware. Result: V49 original 67/67 non-manifest, non-YAML members agree byte-for-byte with S29; FAS1 snapshot header matches S29; one original V83 RX-supervisor header is still missing; FAS1 vs S29 YAML differ in multi-frame receive callback handling. Offline regression: FAS1 original 3 x 200036 assertions PASS, two forbidden modes refused; S29 32/32 host runs PASS. Expected full build availability NOT met; application/controller behavior INCONCLUSIVE / NOT RUN. No ESPHome compile, flash or physical bus action. Rollback remains existing verified V83 RX-only. Next source evidence: original full V83 archive or authenticated original supervisor. Public report Research/V5DCM/V5_NATIVE_SERVICE31_SOURCE_AUDIT_20261020.md.

# V5-NATIVE-SERVICE-30-FAS1-SOURCE-DEPENDENCY-OFFLINE-01 — COMPLETE / POSITIVE OFFLINE, device PREPARED / NOT RUN (2026-10-20). Baseline verified user V83 FAS1 RX_ONLY/HARD_DENY, S29 PRIVATE archive SHA d2c26270..., EXP388 PARTIAL and B11D first-start OPEN. Hypothesis: newly uploaded FAS1 snapshot archive contains the missing verified shared supervisor and can source-pin S29 without mutation. One controlled source audit only (NO code/firmware change). Result: FAS1 additive archive CRC clean but includes only new snapshot header; v5dcm83_shared_rx_supervisor.hpp absent in BOTH input ZIPs. S29 has 53/54 YAML referenced includes. Uploaded candidate YAML SHA 2c01c046... != S29 reference b4aaedf2...; 4 delta groups include V43/V44B callback handling change from parsed.size()==1 to multi-frame iteration, not proven on device. Offline FAS1 host 3x200036 assertions PASS and both forbidden TX builds refused; S29 32/32 host PASS, metadata audit PASS. Positive for exact dependency/provenance diagnosis, negative for standalone build readiness; local effect of source change INCONCLUSIVE/NOT RUN. No ESPHome compiler, flash or bus TX. Rollback unchanged running V83; next obtain exact original shared header or original V49/V83 full source ZIP. Report Research/V5DCM/V5_NATIVE_SERVICE30_FAS1_SOURCE_DEPENDENCY_AUDIT_20261020.md.

# V5-NATIVE-SERVICE-29-VERSION-PROVENANCE-OFFLINE-01 — COMPLETE / POSITIVE OFFLINE (2026-10-20); physical XTR PREPARED / NOT RUN. Hypothesis: S28 reference list/profile admission needs a contemporaneous, version-band-qualified local XTR 0867 anchor; historical raw22 cannot license 31/33 CM930 profile. Baseline verified V83 FAS1 RX_ONLY/HARD_DENY and private S28 SHA 0a476932..., EXP388 PARTIAL/B11D OPEN. One private source change: bind exact 0864/count4 reviewed same-epoch stable CRC-valid raw value + original firmware 2.0.18 2.3.0–2.4.1 or 2.1.105 2.3.0–2.4.3 to S28 exact-list installation; reject stale/historical/source mismatch/22/modulo/hex confusion. Raw offline historical evidence 19/19 CRC-valid frames 0867=decimal22 in five user XTR capture logs; not current. Result 32/32 strict C++17 executable host PASS and 3/3 ASan/UBSan PASS; original 24 YAML blocks/197 HA identities preserved. Inherited missing header v5dcm83_shared_rx_supervisor.hpp in S28 ZIP uncovered; no full ESPHome compile performed, no flash, no physical TX. Negative criteria tested: no profile installed from historical/nonmatching/stale/raw22; positive synthetic eligibility only, NOT physical acceptance. Rollback verified unchanged V83. Archive private SHA d2c26270..., report Research/V5DCM/V5_NATIVE_SERVICE29_VERSION_PROVENANCE_OFFLINE_RESULT_20261020.md.

# V5-NATIVE-SERVICE-28-DUAL-CONNECT-REFERENCE-OFFLINE-01 — COMPLETE / POSITIVE OFFLINE (2026-10-20), device PREPARED / NOT RUN. Hypothesis: firmware significant-group lists vary despite identical W2-W4 mailbox map. One source-tree change in existing S27 service: derive actual sensor+configuration groups from ORIGINAL extracted Connect 2.0.18 and 2.1.105; source-bound S27 admission to explicit exact 31/33 reference set, retain manual local XTR review. Results: older 529 registers/31 groups, newer 541/33 groups, differences 0x04BA + 0x06F4. 31/31 host and 3 sanitizer tests PASS, 24/24 YAML top-level/197 HA identities preserved. No ESPHome compile, flash or TX. Negative offline: missing/wrong/external/stale profile rejected; on-device profile/XTR C2 and true TX still UNTESTED. Abort future test on CRC/B11D/DE/peer/unknown version and wrong readback; rollback unchanged user verified V83 RX_ONLY/HARD_DENY. EXP388 RUNNING/PARTIAL; Service27 prior offline result retained. Report V5DCM/V5_NATIVE_SERVICE28_DUAL_CONNECT_REFERENCE_OFFLINE_RESULT_20261020.md.

# V5-NATIVE-SERVICE27-PROFILE-ADMISSION-OFFLINE-01 — COMPLETE / POSITIVE OFFLINE; device PREPARED / NOT RUN. Baseline S26 private merged source + verified V83 RX_ONLY. Hypothesis: untrusted code must not turn `verified=true` into automatic profile selection/C2. One change new reviewed provenance/epoch/version/geometry adapter and negative tests (ATEC/collaborator, unknown, group overlap, W4 wrong size, stale epoch). 30/30 strict C++17 host executions PASS, no ESPHome compile, flash or TX, no verified local XTR profile group manifest available. HARD_DENY and EXP388 RUNNING/PARTIAL retained. Rollback unchanged V83. Report Research/V5DCM/V5_NATIVE_SERVICE27_PROFILE_ADMISSION_OFFLINE_RESULT_20261020.md.

# V5-NATIVE-SERVICE25-CM930-GROUPS-LIFECYCLE-OFFLINE-01 — COMPLETE / POSITIVE **OFFLINE** (2026-10-20); device experiment PREPARED / NOT RUN. Baseline user-verified V83 FAS1 RX_ONLY/HARD_DENY, exact private S24 merged service; EXP388 RUNNING/PARTIAL, historical B11D OPEN. Hypothesis: genuine CM930 W0-W4 75 group table and distinct significant-package, runtime refresh, handshake vs application lifecycle can be integrated without new RX/physical output stack. One combined S24 source change: firmware-checked 75-entry map, 32 settings+11 operations including 60 words, 0867 raw version capture, externally verified profile required list, C2 and request bitmaps separate, controller FC16 only after ACK transport, guarded W2/W3/W4 mailbox and FC03 cached readback, source-correct app state transitions. 26 normal +2 FakeIo host C++17 tests PASS, 4 sanitizer suites PASS, both original firmware map rows/hash PASS, YAML 24 top-level/197 HA identities/old DE-UART preserved. No compiler/flash/on-device TX; an unverified local XTR firmware-version code or collaborator ATEC profile must NOT auto-load. Positive OFFLINE obtained, negative would be unknown group ack/automatic C2 or hardware arming; no such issues in tested fixtures, real XTR acceptance INCONCLUSIVE/NOT RUN. Abort future user-scoped live execution on CRC/DE/B11D/peer or wrong readback; rollback unchanged V83 FAS1. Report V5DCM/V5_NATIVE_SERVICE25_CM930_GROUP_LIFECYCLE_OFFLINE_RESULT_20261020.md.

# V5-NATIVE-SERVICE24-TRANSACTIONAL-NATIVE-MERGE-OFFLINE-01 — COMPLETE / POSITIVE offline (2026-10-20); live TX PREPARED / NOT RUN. Baseline verified V83 FAS1 RX_ONLY/HARD_DENY and exact S23 private three-way source. Hypothesis: cache page must not be exposed before corresponding ACK transport completion and unsafe/duplicate in-scope TX request must revoke, not be retriable without a new controller epoch and ARM. One integrated S23 source family change: stage/commit page cache, epoch/token revocation, existing V5 callback real RX health/DE evidence (physical ownership still unknown), two new host tests. 24/24 C++17 tests + 1 FakeIo scoped TX test + 5 sanitizer suites PASS; 24 top YAML blocks and 197 HA identities intact; firmware CM930 2.0.18/2.1.105 flags parity rechecked. Positive offline predicate met; no controller acceptance or local semantic write inferred. Negative live abort conditions new B11D/CRC/resync/DE mismatch/peer or readback error; inconclusive any absent controller epoch/slot; rollback unchanged V83 FAS1 RX-only. No compiler/flash/live TX. EXP388 RUNNING/PARTIAL; report V5DCM/V5_NATIVE_SERVICE24_TRANSACTIONAL_NATIVE_MERGE_OFFLINE_RESULT_20261020.md.

# V5-NATIVE-SERVICE23-THREEWAY-SOURCE-MERGE-OFFLINE-01 — COMPLETE / POSITIVE OFFLINE (2026-10-20), related XTR live TX PREPARED / NOT RUN. Hypothesis: consolidate existing V4.1 XTR native responder behavior + V5 reliable parser/HA/B11D and independent ATEC V3 architecture into one private gateway and replace fixed S17 hard-denial with a user-scoped source route. Change: actual private C++17 engine/adapter/32-group current page cache/FC16-03/0708/semantic + one guarded port and source-conditional B11D+1s watchdog shared owner; staged V83-derived YAML in same tree. Normal host 22/22 PASS; FakeIo compiled with two explicit TX macros 1/1 PASS, negative write/CRC/epoch/readback and DE disagreement tests PASS. ASan/UBSan full merged test PASS; 24 YAML blocks/HA/old UART and DE preserved; no ESPHome compiler or device test. Device baseline V83 FAS1 RX-only untouched, TX=HARD_DENY, controller scope/physical peer/slot/current epoch and app completeness OPEN; EXP388 RUNNING/PARTIAL, prior EXP256 harmful single-response COMM ERR, V47 negative and B11D fault unchanged. Abort/revert on actual source drift, bad frame, new B11D/DE fault, unexpected heater alarm or readback mismatch. Rollback verified unchanged V83 FAS1. GitHub sanitized report Research/V5DCM/V5_NATIVE_SERVICE23_THREE_SOURCE_MERGE_OFFLINE_RESULT_20261020.md; private code ZIP withheld.

# V5-NATIVE-SERVICE-23 — PREPARED / NOT RUN (2026-10-20). User clarified objective: implement ONE integrated native gateway from independent ATEC V3 source concepts + XTR V4.1 tested write chain + V5 reliable ESPHome/HA stack, firmware Connect2.0.18/2.1.105 as reference; large end-to-end tests permitted when user-initiated and scoped, not reflexively restricted to one response. Source audit confirms S14–17 Engine17 returns incomplete readiness and S19–21 are passive; real full-service private merge is NEXT and NOT YET EXECUTED. Candidate positive criteria full controlled native startup/config/runtime/one bounded semantic desired-pull + controller republish; negative controller alarm, lost HA or CRC/B11D fault, wrong readback, collision; inconclusive unknown owner/profile/epoch; stop, restore verified V83 FAS1 RX-only. No live TX, ESPHome compile or flash this stage; HARD_DENY. Details: Research/V5DCM/V5_NATIVE_SERVICE23_THREE_SOURCE_MERGE_SCOPE_20261020.md.

# V5-NATIVE-SERVICE-22-OWNER-B11D-EVIDENCE-OFFLINE-01 — PREPARED / NOT RUN (device), 2026-10-20. Hypothesis: available XTR live events and exact V83 source can isolate what still prevents safe native TX without another observer or live test. Single offline operation: reconcile user XTR V83 FAS1 good startup, separate ESP-first mismatch, V47 controller-return integrity denial, FIX-B post-gap positive/timeout bug, V77/V81 host-only owner and EXP254–258/355/386. Positive offline criteria: source SHA/pin/watchdog match, evidence provenance segregated, never promote historical ACK to physical sender, deny absent slot/health/full service; achieved 9/9 static + 6/6 host checks PASS. No hardware qualification, ESPHome compiler, TX, flash or pump restart. Result TX NO-GO due current B11D/owner/peer/EOF/full service gaps. Abort future physical evidence capture on new RX/DE/HA alarm. Rollback unchanged user-verified V83 FAS1 RX-only/HARD_DENY, exact OTA binary hash unverified; EXP388 RUNNING/PARTIAL. Report Research/V5DCM/V5_NATIVE_SERVICE22_B11D_OWNER_SLOT_OFFLINE_RESULT_20261020.md.

# V5-NATIVE-SERVICE-19..21 — PREPARED / NOT RUN (2026-10-20). Baseline user-verified V83 FAS1 RX_ONLY/HARD_DENY; EXP388 RUNNING/PARTIAL, B11D first-start unresolved. Hypothesis: firmware state axes must be observable without falsely elevating raw native traffic to actual Connect acceptance or TX entitlement. Combined offline one source-only firmware-derived lifecycle classifier, source-SHA-pinned external/UNKNOWN replay and additive existing V5 RX-only diagnostic. Host: old S14–17 17/17 PASS, S18FIX1 1/1 PASS, S19 1/1 PASS, 2 replay assertions PASS, extracted original CM930 2.0.18/2.1.105 flags parity PASS, YAML 24-block/IDs/CRC callback/UART+DE/B11D preservation PASS. No compiler, flash, local XTR bus TX or live acceptance; only external ATEC 32-group starts observed. Proposed positive criteria if later run: correct passive diagnosis without changed bus health; negative: any parser/B11D regression or sender/owner false-promotion; inconclusive: boot epoch missing; abort on peer/slot/CRC/integrity issue. Rollback unchanged V83 FAS1; TX=HARD_DENY. Report V5DCM/V5_NATIVE_SERVICE19_TO_21_FIRMWARE_PARITY_RX_ONLY_OFFLINE_20261020.md.

# V5-NATIVE-FIRMWARE-REVIEW-01 — COMPLETE / POSITIVE OFFLINE SOURCE RECONCILIATION (2026-10-20). Hypothesis: re-auditing S11-18 against original Connect AppFS will reveal gaps masked by synthetic host tests. Verified AppFS/device_client code parity 9/9; corrected S18 FC23 read/write address reversal and failed mirrored fixture. FIX1 genuine collaborator ATEC 20261003 replay 1 actual startup FC23, not 0 (request size 29 bytes); 2687 CRC-valid / 162 FC16 / 162 ACK shapes / 65 0708. Prior S18 classification as LOCAL XTR is DISPROVEN/SUPERSEDED: it is collaborator ATEC+DCM03. Sep25 exact model unknown. Corrected S18 test PASS plus original 17 host tests PASS. No ESPHome compile, flash, XTR bus TX or new local acceptance. Original S18 PREPARED/NOT RUN on device stays; S11-17 likewise partial, not native firmware parity. User-verified V83 FAS1 RX-only untouched, TX HARD_DENY, EXP388 RUNNING/PARTIAL, B11D OPEN. Report Research/V5DCM/V5_NATIVE_SERVICE_11_TO_18_FIRMWARE_REAUDIT_AND_S18_FIX1_20261020.md.

# V5-NATIVE-SERVICE-18 — PREPARED / NOT RUN (2026-10-20). Hypothesis: existing V5 single RX parser can passively classify native 0x0F startup/FC16/0708 without TX, DE changes or session permission. One additive header, one callback call, one diagnostic HA sensor. Offline verification 18/18 C++17 host tests PASS and YAML-preservation checks PASS; local historical XTR replay CRC/shape counts 2687 frames / 162 FC16 / 162 unattributed ACK forms / 65 0708 / 2 085F / no exact challenge. Historic replay is NOT a new live run. No ESPHome compile/flash/bus TX; user-verified V83 FAS1 remains installed/rollback, HARD_DENY; EXP388 RUNNING/PARTIAL and B11D OPEN. Abort any future TX on unknown peer/slot/epoch or sticky fault. Report V5DCM/V5_NATIVE_SERVICE18_RX_WITNESS_OFFLINE_RESULT_20261020.md.

# V5-NATIVE-SERVICE-14..17 — PREPARED / NOT RUN (2026-10-20). Offline integration only. Hypothesis: source-derived V4.1 startup, initial sync, runtime requests, refresh/one-word readback can be safely staged behind a single fail-closed owner. One staged integration package, no installed YAML change. 17/17 C++17 host tests PASS, including 10-page ordered sequence, CRC/epoch/slot guards, stale refresh, simulated republish positive and mismatch-negative, historical XTR request shapes, forced permission bypass denied. These are mocked controller/transport events, NOT live execution or proof of native XTR DCM write. Missing true startup response provider and UART/DE/B11D binding. Abort conditions: unknown slot/peer, CRC, epoch, parser/stale fault, readback mismatch; rollback unchanged V83 FAS1. TX HARD_DENY, EXP388 RUNNING/PARTIAL, B11D OPEN. Report V5DCM/V5_NATIVE_SERVICE_14_TO_17_OFFLINE_RESULT_20261020.md.

# V5-NATIVE-SERVICE-12 — PREPARED / NOT RUN (2026-10-20). Hypothesis: compose original V5 source-grounded initial chain and FC16/FC03 services offline without prematurely arming TX. Verified original private ZIP SHA256. Five existing C++17 tests PASS; new partial routing test PASS, including unsupported kinds, invalid CRC, wrong epoch, non-operational session, reset. No controller executed test, so remains PREPARED/NOT RUN. Missing startup, 0708, refresh, semantic, physical owner and B11D; fail closed. Known-good V83 FAS1 unchanged, TX HARD_DENY, EXP388 RUNNING/PARTIAL, abort on unknown peer/slot/context, rollback untouched YAML. See V5DCM/V5_NATIVE_SERVICE_12_PARTIAL_ROUTER_OFFLINE_RESULT_20261020.md.

# V5-NATIVE-SERVICE-12 — PREPARED / NOT RUN (2026-10-20). OFFLINE V4.1 original source review only (GitHub blob 8e8a82689e53528a8b751a1abbd901f683b6b238). Hypothesis: port genuine source-defined startup, initial and runtime handlers to V5 without premature acceptance. Facts: 32 address/count shape family; R1/cold first 03E8/14; FC16 ACK creation increments source counters before independent controller progression; 22-page resume legacy branch never armed by UI; 0546 republish checks target and unchanged other words. Source audit positive for locating behaviors but experiment NOT RUN; cannot infer V5 integrated behavior, physical TX or DCM acceptance. Stop unknown slot/peer/CRC/epoch; rollback V83 FAS1 RX-only. Missing precise V5 service-11 private ZIP blocks safe merge. See V5DCM/V5_NATIVE_SERVICE_12_V41_SOURCE_AUDIT_20261020.md.

# V5-NATIVE-SERVICE-11 — PREPARED / NOT RUN (2026-10-20). Private offline V5 source artifact V5_NATIVE_TX_V41_INITIAL_HANDLER_OFFLINE_20261020.zip (SHA-256 0428a5a31dcab66730ba3acbe13ec92cf6ccb97e377870166779c4683fef0898) adds real NativeServiceGate initial-page callback adapter for 10 V4.1-derived cold FC16 page pairs. C++17 host test PASS all ten pages plus reply CRC, suppression of duplicate, epoch guard, bad CRC, resume-page fail-close; test injects transport/runtime confirmation, not XTR wire evidence. Existing YAML sha b4aaedf27f8dd3d58fcc7c09316cfe03d9c8f41d40fcd827a31bf1f104d389fa unchanged. Other five gateway handlers still missing, no UART/B11D binding, HARD_DENY on; no ESPHome compile, flash, live TX or DCM acceptance. V4.1 22-page resume branch SOURCE PRESENT, NOT proven locally executed; EXP388 unchanged.

# V5-NATIVE-SERVICE-10 — PREPARED / NOT RUN (2026-10-20). Original V4.1 resume path is described in its source as unreachable legacy code; no assignment enabling write_resume_armed was found. The 22-page continuation is a source-defined map, not verified live resume. Private V5 candidate adds default-disabled resume gate with manual/session/peer/slot checks, 04A6/count13 transition and 22-page ordering. Isolated host C++17 tests PASS; no ESPHome coupling, no flash or live TX, HARD_DENY retained. Local transport completion is still not controller confirmation. See private V5_NATIVE_TX_V41_RESUME_GATED_OFFLINE_20261020.zip. 

# V5-NATIVE-SERVICE-09 — PREPARED / NOT RUN (2026-10-20). Baseline V5 HARD_DENY. One source change: exact V4.1 10+22 page/count cohorts added as constants, with separately gated resume; target offline FC16 ordered page sequences. C++17 host test PASS; bad transition from resumed page as initial first page rejected. No bus TX/flash, no ESPHome compilation requested. Positive live outcome would require fully integrated verified native session, not host pass; abort unknown peer/slot/state, rollback prior RX-only V83 FAS1. Next integrate actual V4.1 startup and resume trigger.

# V5-NATIVE-SERVICE-08 — PREPARED / NOT RUN (2026-10-20). Baseline native V5 HARD_DENY and incomplete 3-page test FC16 chain. Change: advance confirmed page only after local transport completion followed by next distinct expected controller request; final requires separately supplied validated runtime transition. Host C++17 test PASS on no-send, duplicate, wrong epoch, invalid CRC, missing final confirmation. No physical TX, no flash, no ESPHome compile. Fail closed on unexpected page/epoch/integrity; rollback unchanged RX-only V83 FAS1.

# V5-NATIVE-SERVICE-07 — PREPARED / NOT RUN: source-only initial FC16 page order checker, no live TX. Target offline test 03E8/14 -> 03FC/11 -> 0410/22, only a three-page subset. Host test PASS for order/CRC/epoch and duplicate rejection. Incomplete full native service; danger if a constructed ACK is mistaken for delivery. Positive live criterion not assessed. Rollback existing RX-only V83 FAS1; stop on unknown peer/slot/protocol, no physical TX attempted.

# V5-NATIVE-SERVICE-05 — PREPARED / NOT RUN (offline host tests only, 2026-10-20). Baseline V5 RX_ONLY/HARD_DENY, private V4.1 verified native service. Change: require six native service handlers and valid frame/epoch/slot for hypothetical response; no frame-generator or TX wiring. Host C++17 dummy-handler tests PASS for missing handler, invalid CRC, wrong epoch, wrong slot, no reply. No ESPHome compile, flash or bus TX; cannot mark live experiment COMPLETE. Abort/fail closed on unknown service, peer/slot or frame validation; rollback unchanged V83 FAS1. Artifact V5_NATIVE_TX_SERVICE_CONTRACT_PREPARED_20261020.zip private.

# V5DCM100-XTR-0F-OWNER-PROVENANCE-01 — COMPLETE / POSITIVE OFFLINE 2026-10-20. Historical local intervention comparison EXP254/255 no response 63 approval attempts, native ACK0/0708=0; EXP256 bounded response leads to 03E8 ~124ms later, missing ACK repeats and COMM ERR/DHW-side zero; EXP257/258 individual ACKs advance 03FC/0410; EXP355/386 qualified full service led to 32/32. Physical owner/DE timing unproven. No TX/flash; V83 FAS1 baseline, EXP388 RUNNING/PARTIAL. Report: V5DCM/V5DCM100_0F_RESPONDER_PROVENANCE_OFFLINE_RESULT_20261020.md.

# V5DCM99 — COMPLETE / POSITIVE (offline, 2026-10-20). Single change: compare 5 CRC-validated historical XTR captures against external ATEC V3 ownership and timing safeguards. Count 337 0x0F FC16 requests, 306 ACK, 122 FC03 requests. Logs do not identify physical responder or EOF-to-SOF slot; 0x0F automatic takeover NO-GO. No TX, flash or compile. Baseline RX_ONLY/HARD_DENY, EXP388 RUNNING/PARTIAL, B11D OPEN. Report: V5DCM/V5DCM99_XTR_ATEC_OWNER_TIMING_OFFLINE_RESULT_20261020.md.

# V5DCM98-CM930-ACQUISITION-PUBLICATION-01 — COMPLETE / POSITIVE (OFFLINE), 2026-10-20. One change: audit original Connect 2.1.105 register event -> info/operation state -> parameter-map publication. 16/16 source checks PASS. Original firmware gates normal parsers on OPERATION and map publication on ALL_DATA_PACKAGE_RECEIVED; information acquisition can precede cloud onboarding. No runtime/session acceptance proven, no TX/flash/compile. Baseline FAS1 RX_ONLY/HARD_DENY, EXP388 RUNNING/PARTIAL, B11D fault OPEN. NEXT V99 OFFLINE. Report: V5DCM/V5DCM98_NATIVE_ACQUISITION_PUBLICATION_OFFLINE_RESULT_20261020.md.

# V5DCM97 — COMPLETE / POSITIVE OFFLINE (2026-10-20). Connect2.1.105 CM930 source allows transport-handshake ACCEPTED to request info before external onboarding, while normal sensors/config/operation parser feed and MQTT subscriptions occur in OPERATION after external onboarding. Original cloud gate is a Connect application-state rule, not proven controller requirement for native local writes. ATEC V3 remains EXTERNAL CLAIM only. 16/16 source-presence assertions PASS; no compilation, flash, physical TX. [V97 report](V5DCM/V5DCM97_LOCAL_VS_CLOUD_GATES_OFFLINE_RESULT_20261020.md). User-verified FAS1 RX_ONLY/HARD_DENY unchanged; original V49 rollback; EXP388 RUNNING/PARTIAL and earlier B11D initial fault OPEN. NEXT V98 OFFLINE.

# V5DCM96 (2026-10-20) — COMPLETE / POSITIVE OFFLINE original-source provenance analysis. Connect CM930 receives controller serial locally, optional desired serial and onboarding completion via a separate MQTT SetDeviceInfo message, and a separate MasterSettings serial in shared state; do not conflate origins. Source confirms onboarding state separate from transport. 12/12 static assertions PASS, no native XTR acceptance proved. [V96 report](V5DCM/V5DCM96_ONBOARDING_PROVENANCE_OFFLINE_RESULT_20261020.md). Latest live user-verified FAS1 RX_ONLY/HARD_DENY, EXP388 RUNNING/PARTIAL, V49 rollback, earlier B11D anomaly OPEN. No compile, flash or TX. Next V97 OFFLINE.

# 2026-10-20 V5DCM95 COMPLETE / POSITIVE OFFLINE. Original Connect2.1.105 CM930 source implements serial-correction onboarding: device info sent while WAITING_FOR_SET_DEVICE_INFO; a desired eight-character serial may start SERIAL_NUMBER_UPDATE; a readback match republishes info, but only separate onboarding_completed advances OPERATION. Legacy fingerprint mapping is a distinct path. Firmware Transport HandshakeState.ACCEPTED, serial readback and remote onboarding completion are not interchangeable. Original vendor source checks 12/12 PASS; no XTR live acceptance or cloud feedback proven. External ATEC V3 remains EXTERNAL. [V95 report](V5DCM/V5DCM95_CM930_ONBOARDING_SERIAL_LIFECYCLE_OFFLINE_RESULT_20261020.md). FAS1 user-verified RX_ONLY/HARD_DENY unchanged, EXP388 RUNNING/PARTIAL, V49 rollback, earlier V83 B11D first-start fault OPEN; zero physical TX/flash. NEXT V96 OFFLINE trace external onboarding payload provenance.

# 2026-10-20 V5DCM94 — COMPLETE / POSITIVE OFFLINE. Strict CRC and byte-length checks of five historic XTR captures found 337 valid 0x0F FC16 request frames, 1337=1 and 1340=0 in 3, 1778=FFFF plus 1779=FFFF in 3, 2151=22 in 19; other HUB/expansion/COMM.KIT fields are separate. Original Connect2.1.105 CM930 uses 1778/1779 for serial, and source first truncates its decimal rendering to 8 digits before HPSerialNumber validation, potentially accepting a pseudo-serial from all-ones values. This is a SOURCE-PATH POSSIBILITY, not actual Connect onboarding or correct XTR identity. ATEC V3 EXTERNAL only. [V94 report](V5DCM/V5DCM94_IDENTITY_FIELDS_OFFLINE_RESULT_20261020.md). 7/7 offline assertions PASS; no physical TX, ESPHome compile or flash. FAS1 RX_ONLY/HARD_DENY user-verified, V49 rollback, EXP388 RUNNING/PARTIAL and earlier B11D startup fault OPEN. Next V95 OFFLINE identity update/provenance.

# 2026-10-20 V5DCM93 — COMPLETE / POSITIVE (OFFLINE SOURCE/CAPTURE only). Genuine Connect2.1.105 CM930 info.py decodes firmware before product name; both values latch after successful parse; product-name extractor is loaded by version-selected profile, so identity cannot itself repair missing version profile. CM930 ready_to_send requires firmware version and serial, NOT a non-null product name. Five XTR historical captures strict CRC/FC16 length checks: 337 valid 0x0F FC16 requests, register1337 three observations all raw1 and never 22/23; register2151 nineteen observations all raw22. Oct03 reg1337 first at44.763s, reg2151 first86.672s; logging timing only. No demonstrated genuine Connect profile/semantic acceptance; ATEC V3 external claim only. [V93 report](V5DCM/V5DCM93_CM930_IDENTITY_LIFECYCLE_OFFLINE_RESULT_20261020.md). FAS1 RX_ONLY/HARD_DENY unchanged, original V49 rollback, EXP388 RUNNING/PARTIAL, separate earlier B11D start anomaly OPEN; no new TX, compile or flash. NEXT V94 OFFLINE independent identity and version provenance.

# 2026-10-20 V5DCM92 — COMPLETE / POSITIVE OFFLINE original XTR-specific firmware evidence. Genuine Connect2.1.105 profile info-2.4.2.json and info-2.4.3.json list iTec XTR M 1N/3N as model codes 22/23 via register1337; earlier 2.3.0/2.4.0/2.4.1 do not. Fresh CRC-validated historical XTR FC16: register1337 raw1 in 3 prior requests; 2151 raw22 in 19 prior requests. These values conflict with direct model table and stock version profile respectively, requiring provenance investigation; do not substitute codes. Official international Thermia Online lists XTR as Connect compatible. Direct source support is PROVEN, live XTR selection/authentication/semantic acceptance UNKNOWN. ATEC V3 stays EXTERNAL. See [V92](V5DCM/V5DCM92_XTR_NATIVE_CONNECT_PROFILE_OFFLINE_RESULT_20261020.md). Baseline unchanged V83-FAS1 RX_ONLY/HARD_DENY, V49 rollback, EXP388 RUNNING/PARTIAL and old B11D startup fault OPEN. Zero TX/flash. Next V93 OFFLINE identity lifecycle.

# 2026-10-20 PRODUCT GENERATION RESEARCH (NOT EXPERIMENT): Official Thermia chronology ATEC 2011, iTec 2017, iTec Eco 2020, Athena 2021, iTec XT announced Dec 2023 / listed 2024, iTec XTR 2025. Official XT indoor / XTR outdoor shared guide indicates family continuity but not proven common protocol. International Thermia Online page expressly lists iTec XTR supported by Thermia Connect. Therefore prioritize XTR/XT source and compatibility over older external ATEC V3, which remains architectural comparison only. No native current session/2151 profile inference; V91 remains previous offline result and V92 upcoming. Live baseline V83-FAS1 RX_ONLY/HARD_DENY, EXP388 RUNNING/PARTIAL; no test/flash/TX. Details: Research/THERMIA_AIR_WATER_MODEL_GENERATIONS_OFFICIAL_20261020.md.

# V5DCM91 (2026-10-20): COMPLETE / POSITIVE OFFLINE source comparison. Older and newer CM930 air-to-water profiles differ in optional sensors, configurations and high-pressure visibility rules. Available historical XTR values do not identify a unique profile. See Research/V5DCM/V5DCM91_PROFILE_DIFFERENTIAL_OFFLINE_RESULT_20261020.md. No hardware change; FAS1 RX_ONLY/HARD_DENY, EXP388 PARTIAL, earlier B11D discrepancy OPEN. Next V92 offline.

# V5DCM90-PROFILE-FAMILY-CRC-CROSSCHECK-OFFLINE-01 COMPLETE / POSITIVE (OFFLINE only), 2026-10-20. Baseline user-confirmed V83-FAS1 RX_ONLY/HARD_DENY, EXP388 RUNNING/PARTIAL, V49 rollback, prior B11D startup anomaly OPEN. One change: read five archived XTR captures CRC-valid 0x0F FC16 and compare original Connect2.1.105 CM930 sensors.json and external ATEC V3 profile note. All 19 2080=80/86/89, 2081=148/150/176..178/327..328,2095=130,2151=22. Vendor 1.1.1–2.1.0 and 2.3.0–2.4.3 assign 2080/2081 condenser temperatures and 2095 outdoor status; brine ranges different. ATEC author independently CLAIMS same discriminator and manually picks newer range; no genuine cited ATEC capture. Offline result supports semantic family, not exact generation or application TX/session. CRC/shape source assertions pass; abort if mismatch, no rollback/hardware change, no ESPHome compile/flash/TX. [Report](V5DCM/V5DCM90_REGISTER_PROFILE_CROSSCHECK_OFFLINE_RESULT_20261020.md). NEXT V91 offline.

# V5DCM89-CM930-VERSION-PROVENANCE-ATEC-CROSSCHECK-OFFLINE-01 — COMPLETE / POSITIVE (OFFLINE source comparison, NOT device acceptance) 2026-10-20. Baseline V83-FAS1 RX_ONLY/HARD_DENY user confirmed, V49 rollback, EXP388 RUNNING/PARTIAL, earlier V83 B11D mismatch OPEN. One change: treat ATEC V3 as EXTERNAL SOURCE/CLAIM alongside genuine Connect2.1.105 and historical XTR V87 raw22. Source info.py defines register2151/0x0867 as Control Module(display) firmware version, raw22=>0.2.2. EXTERNAL ATEC author's step3 document reports 2151=22 and manually selected 2.3.0–2.4.3 air-to-water profile, not a Connect runtime auto-match; cited ATEC cold-start trace absent from tar. Static original ZIP+ATEC tar field assertions PASS. Positive is cross-source value/label corroboration only; vendor profile selection mismatch and current XTR acceptance OPEN. Abort on source disagreement; rollback N/A. Physical TX0, compile/flash NOT RUN. [Report](V5DCM/V5DCM89_CM930_VERSION_PROVENANCE_ATEC_CROSSCHECK_OFFLINE_RESULT_20261020.md); NEXT V90 OFFLINE.

# V5DCM88-CM930-VERSION-CONFIG-FALLBACK-OFFLINE-01 — **COMPLETE / POSITIVE (OFFLINE)** 2026-10-20. Baseline V83-FAS1 RX_ONLY/HARD_DENY user confirmed, V49 rollback, EXP388 RUNNING/PARTIAL; prior V87 historic raw22/0.2.2 and earlier B11D startup issue OPEN. Hypothesis native Connect custom/OTA/fallback paths could resolve unmatched 0.2.2 profile in unmodified shipped config. ONE controlled OFFLINE source check on original vendor modules/stock config; protected auth and mailbox implementation excluded. Vendor config supports default/custom/OTA paths; no evidence actual overrides installed. CM930 source default decoder uses 0x0867; only CM920 special corrections. Four shipped 930 ranges exclude 0.2.2. Profile-dir resolution fails first; version-filename fallback only chooses lower matching file within already valid directory, cannot rescue missing directory. NoConfiguration reported when required parsers missing; _version_config_loaded flag alone not proof. 15/15 static assertions PASS; old and appfs module bytes match. Positive source-model result, no live XTR semantic outcome. Abort on assertion mismatch, recovery none, TX none, flash/compile NOT RUN. [Report](V5DCM/V5DCM88_CM930_VERSION_FALLBACK_OFFLINE_RESULT_20261020.md). NEXT V89 OFFLINE source/provenance, preserve EXP388.

# 2026-10-20 ATEC V3 LEGAL/SOURCE REVIEW — NON-EXPERIMENT (NO XTR TX). Audited all 23 user-supplied ATEC tar entries: no license or SPDX; fixed vendor-firmware-derived 128-bit authentication secret included in third-party source and docs; no independent proof of authorization, EULA status or verbatim copied original firmware code; no cloud credentials shown in YAML (ESPHome connection secrets external). EU software interoperability, trade-secret and anti-circumvention laws reviewed with citations in sanitized note. This is a rights/provenance risk review, **not** a finding of unlawful conduct and not a tested protocol change. Technical experiment and running statuses remain unchanged. [Sanitized legal review](ATEC_V3_LEGAL_RISK_REVIEW_20261020.md).

# V5DCM87-CM930-VERSION-0867-PROVENANCE-OFFLINE-01 — **COMPLETE / POSITIVE (OFFLINE)** 2026-10-20. Hypothesis historical raw22/CM930 supported-profile mismatch is reproducible from genuine Connect2.1.105 source and CRC-shaped archived XTR 0x0F FC16 0x0864/count4 records. Baseline user-verified FAS1 RX_ONLY/HARD_DENY, V49 rollback, EXP388 RUNNING/PARTIAL, separate earlier V83 B11D anomaly OPEN; predecessor V86. One change static validation only: original info.py formula decimal2151/0x0867 -> raw22 produces semver0.2.2; modbus_server15.py loads configs by extracted version; configuration.py matches exact/inclusive ranges; packaged 930 ranges 1.1.1–2.1.0,2.2.0–2.2.1,2.3.0–2.4.3,3.0.0–3.1.1 exclude 0.2.2. Reparsed historical logs 2+4+1+0+12=19 raw22 entries. Positive condition source+sample agreement PASS; negative/inconclusive criterion source/count/disagreement or nonmatching current version not inferred. Abort reject static conclusion on assertion failure; recovery none, physical TX0, no flash, compile NOT RUN. Actual controller version, source provenance, native accept unknown. [Report](V5DCM/V5DCM87_CM930_VERSION_0867_OFFLINE_RESULT_20261020.md). NEXT V88 offline alternate version-data provenance/fallback audit; do not close EXP388.

# 2026-10-20 EXTERNAL ATEC V3 KEY HANDLING — NON-EXPERIMENT SOURCE AUDIT (no XTR activity). Reviewed actual third-party C++ handshake helper, passive match logger, gateway responder and ESPHome config. Observed fixed 128-bit key compiled into image, not ESPHome secret manager; challenge/response on bus, key not separately broadcast; challenge/derived-response included in diagnostics; general Wi-Fi/API/OTA secret handling separate. No source-backed secure-element/per-device key derivation. ATEC author live claims unverified without provided raw captures. Do not publish key, cryptographic implementation, protocol reply material or private emulation; no test target/payload, no compilation/flash/live TX and no change to FAS1/EXP388. [Sanitized note](ATEC_GATEWAY_V3_EXTERNAL_SOURCE_REVIEW_20261020.md).

# 2026-10-20 — EXTERNAL ATEC-V3 SOURCE/FRAMER COALESCING CHECK: COMPLETE / POSITIVE **OFFLINE FOR SOURCE FAILURE MODE ONLY**. Known baseline exact user ATEC V3 source + archived V5DCM80 V49 parser replay, recent FAS1 local RX-only; prior ATEC source review and native TX unverified. One controlled synthetic HOST input variation: concatenate two independent CRC-valid generic 8-byte FC03 slave02/slave04 ADUs in V3 Framer's input before its 3ms-gap poll. Positive criterion one emitted suffix and first dropped; negative both separately emitted; inconclusive if generic exercise did not match source. RESULT: emitted one (slave04, 8 bytes, ok1/bad1); subsequent poll yielded none. V3 source's one-timestamp UART backlog loop could produce this coalescing, but actual on-bus occurrence UNKNOWN. Cross-check V5DCM80 previous 2687/2687 three host chunking modes; FAS1 separately live 1028 comparisons. Abort/recovery: purely host no output; discard extrapolations beyond demonstrated. No target hardware/register/write payload, no TX, no user live action, no change EXP388/V86. [Review addendum](ATEC_GATEWAY_V3_EXTERNAL_SOURCE_REVIEW_20261020.md).

# 2026-10-20 EXTERNAL ATEC V3 — OFFLINE SOURCE REVIEW / NON-EXPERIMENT. User tar SHA256 e1dc7f316cd887e96e481e7e509570e9c1836b68ed271f47630b0d754f985abc contains ESPHome native 0x0F gateway replacement source and handoff claiming ATEC success (FC16 settings, FC03 re-read, mailbox-driven refresh, reported repeated setting-confirmation). Cross-model architectural corroboration ONLY: no independent ATEC raw logs in tar, no local XTR run. Two supplied host tests C++17 both ALL PASS; seven referenced historical replay suites absent. Code warning: readback published when controller FC03 request received before TX delivery confirmed; shipped YAML auto-arms TX after short listen. No XTR TX, ESPHome compile, flash or controller action. Archive includes protected authentication and gateway code; publish sanitized findings only. [Review](ATEC_GATEWAY_V3_EXTERNAL_SOURCE_REVIEW_20261020.md). Do not alter V86 or EXP388 statuses; V87 OFFLINE remains next.

# V5DCM86-CM930-PROFILE-GROUP-COMPLETENESS-OFFLINE-01 — **COMPLETE / POSITIVE (GENUINE VENDOR SOURCE + ARCHIVED CRC FRAMES ONLY)** 2026-10-20. HYPOTHESIS: source-driven requested-data completeness is different from historical controller 32/32 configuration ACK adjacency, and historic 0867 version field requires exact decoder/profile check. Verified baseline FAS1 user-run RX_ONLY/HARD_DENY with first RAW2/expected2, 1028 B11D equal,1194 V5 frames resync/drop0 and current RX QUALIFIED; prior separate V83 startup fault OPEN, EXP388 RUNNING/PARTIAL, original V49 source rollback. Relevant V84 vendor register map, V85 chronological XTR FC23→32 settings→status/poll/operations, historical EXP256 COMM ERR after incomplete responder. ONE controlled OFFLINE change: inspect byte-identical Connect2.1.105 and device_client 8 sources, vendor profile dirs+930/modbus-flags JSON and CRC-verified Oct03 XTR FC16 start intervals, abstract missing-group model. Source version formula 2151 raw22→0.2.2, bundled profiles min1.1.1, so no matching version directory (220→2.2.0 ONLY hypothetical). Source possible mask groups16+16+11=43, separate bulk request42 skipping operation bit8, profile required groups30/31/33/31. Historic 32 initial FC16 starts cover 32 distinct settings groups but none operations: profile completion would still require7/8/8/8 operation groups. Across full Oct03 FC16 starts all 43 group intervals represented; **no real vendor state/ACK acceptance proven**, native reply and current version unknown. 35/35 Python defensive checks PASS, privacy-safe ZIP SHA256 1c6dbf9bfb54f4af2ddd34ee6f9b0a1a7c4def6a9d2a9c05b378f7e372ecddfc. No hardware action, no target TX payload/register/current value required; abort/discard on source/hash/CRC/mask assertion mismatch; hardware rollback N/A. **NEXT V87 OFFLINE** investigate version field/raw22 mismatch; keep FAS1 installed RX-only and do not transmit. [V86 full result](V5DCM/V5DCM86_CM930_PROFILE_GROUP_COMPLETENESS_OFFLINE_RESULT_20261020.md).

# V5DCM85-CM930-OFFLINE-SESSION-ORDER-01 — **COMPLETE / POSITIVE (OFFLINE SOURCE/ARCHIVAL TIMELINE; NOT DEVICE SESSION COMPLETION)** (2026-10-20). Hypothesis original CM930 nonsecret app-state hierarchy is structurally consistent with order of existing local 0x0F FC23/config/status/periodic read/operation traffic. Baseline user FAS1 RX_ONLY/HARD_DENY clean 141.57s and current RX qualified, old separate V83 B11D first-fault cause unknown; EXP388 RUNNING/PARTIAL, source V49 verified earlier rollback. Relevant earlier V84 firmware register map and 873 CRC-valid archived 0x0F frames; historic EXP256 incomplete first reply COMM ERR. ONE OFFLINE controlled change: AST-inspect genuine 2.1.105 source state labels only (no private backend), CRC/shape/order audit all five existing captures and Oct03 chronology. Vendor states: handshake NOT_ACCEPTED/RESPONSE_SENT/ACCEPTED, runtime NOT_STARTED/WAITING_FOR_DEVICE_INFO/WAITING_FOR_SET_DEVICE_INFO/SERIAL_NUMBER_UPDATE/OPERATION, independent data-group INITIAL/WAIT_FOR_ALL_DATA_PACKAGE/ALL_DATA_PACKAGE_RECEIVED; no vendor APP33 completeness or cloud acceptance observed. Oct03 FC23 pair 27.400/27.429, 32 ordered config pages03E8–06F4 29.262–61.461 with 32 adjacent ACK shapes12–15ms, 085F t61.529, first0708/6 read64.923 (65 repeats ~4.071–4.332s), first07D0 operation65.664; Oct03 162/162 FC16 ACK-shape adjacency12–16ms. The logger clock is not wire EOF; capture start not controller epoch; FC16 ACK shape not semantic acceptance. Audit/negative mutation tests 19/19 PASS, file hashes/CRC verified, archive SHA256 4ab764ccc286412f743ae1262549b600c638914134d028730f970a20639a726e; no device TX or flash; abort discard offline on source/hash/CRC/ordering failure; hardware rollback N/A. NEXT V86 source-only current-profile/bitmask completion comparison, native handshake/physical owner/EOF/slot remain OPEN, no user action needed. [Full V85 report](V5DCM/V5DCM85_CM930_SESSION_CHRONOLOGY_OFFLINE_RESULT_20261020.md).

# V5DCM84-CM930-REGISTER-CONCORDANCE-OFFLINE-01 — **COMPLETE / POSITIVE (EXACT VENDOR SOURCE + EXISTING CRC-VERIFIED LOCAL XTR CAPTURES; NO LIVE TEST)** 2026-10-20. Hypothesis vendor CM930 public register layout explains local native 0x0F address families. Verified baseline user-installed V83-FAS1 RX_ONLY/HARD_DENY, 141.57s clean FAS1 device log; older V83 separate-boot B11D countDiff1 remains unresolved; EXP388 RUNNING/PARTIAL. ONE controlled offline source/CRC audit: byte-identical device_client and genuine extracted Connect2.1.105 source; 0x0F slave + 03E8 settings,0708 datapackage,07D0 operations,085F alarm/status; five historic captures contain 873 CRC-valid 0x0F ADUs, Oct03 458, 65 FC03 read 0708/6; FC16 ACK shapes explicitly NOT semantic write acceptance. Vendor sensor hp_cm_firmware_version formula {2151}; 19 prior XTR 0864/4 FC16 requests carry fourth register 0867 raw22; current controller version UNKNOWN. Reproducible nonsecret privacy-safe host audit PASS, archived as SHA256 a28cf8b106598b0ca98e9fd9b67510c651abb75105840a077adfca787b2e13df. No physical TX, payload write, new ESP flash or controller restart; hardware abort/rollback N/A. Positive exact-source/frame-family match; negative would be CRC or source disagreement; no such failure; native acceptance still INCONCLUSIVE/UNKNOWN. NEXT V85 OFFLINE source session-state/order only. [Full V84 result](V5DCM/V5DCM84_CM930_REGISTER_CONCORDANCE_OFFLINE_RESULT_20261020.md).

# V5DCM83-FAS1-B11D-FIRST-ALIGNMENT-SNAPSHOT-01 — **COMPLETE / POSITIVE (USER-RUN PASSIVE DEVICE RESULT)** 2026-10-20. RESULT after earlier PREPARED record below: user ESPHome log 3654 lines/141.57s, FAS1 stored first arm 440ms callback gap; prePending0, postPending1, first comparison RAW2/V5 expected2 COUNT_EQUAL. Last complete B11D batch compared1028 frames with countDiff0/byteDiff0 and no faults; main V5 status1194 frames resync0 drops0 TX0. V83 RX-only owner unsafe0 DE0, current FIX2 RX QUALIFIED, software write counters0. Controller protocol epoch/owner/physical slot and DCM/Online UNKNOWN. Older V83 startup count mismatch is HISTORICAL and remains unexplained, not erased; EXP388 RUNNING/PARTIAL. [User live result](V5DCM/V5DCM83_FAS1_LIVE_RESULT_20261020.md).

# V5DCM83-FAS1-B11D-FIRST-ALIGNMENT-SNAPSHOT-01 — **PREPARED / NOT RUN (OFFLINE SOURCE + HOST CHECKS PASSED)** (2026-10-20). HYPOTHESIS first metadata capture around existing B11D >=25ms callback arming and first raw-vs-V5 comparison can preserve the missing expectedCount and pre/post V5 pending/resync without changing existing sticky fault path. Last verified live V83 RUNNING/PARTIAL on ESP32 flash only/controller continuously powered; 94s software RX stable, DE LOW/TX attempts0, early first B11D countDiff1 unresolved; EXP388 RUNNING/PARTIAL. One controlled additive RX-only change against exact delivered V83 source: passive non-TX header, 8 anchored observation calls/include/entity, ONE diagnostic. 37/37 YAML/source tests PASS, 200036/200036 C++ host assertions per strict/sanitizers/noexception mode PASS; 2/2 output flag build denials. Original `independent.size()!=expect.size()` comparison, b11d_first_fault, P5/FIX2, HA entities and UART parser intact. Neither ESPHome compilation nor device flash/physical output performed. Positive after potential user run: initial snapshot + identical telemetry, no TX, unchanged B11D fault; negative missing entities, new receive errors, high DE or TX; inconclusive if never arms/comparison absent. Abort/source rollback to V83 or known-good V49. Never clear first fault or assume physical EOF from 25ms callback gap. [Detailed FAS1 preparation](V5DCM/V5DCM83_FAS1_FIRST_ALIGNMENT_SNAPSHOT_PREPARED_20261020.md).

# V5DCM83-B11D-STARTUP-SOURCE-AUDIT-01 — **COMPLETE / POSITIVE (ORIGINAL V49 SOURCE + HOST SIMULATION ONLY; FIELD V83 REMAINS RUNNING / PARTIAL)** (2026-10-20). Hypothesis: unchanged B11D raw start at >=25ms UART callback gap, while original V5 parser has already processed bytes, can latch a first-batch count discrepancy independent of bad CRC or real TX. Last confirmed live V83 RX_ONLY/HARD_DENY after ESP flash on continuously running controller; first visible API log ~94s V83 unsafe0 DEsw/pin0 TX0, original B11D countDiff1, two CRC-valid raw frames, stable parser resync22; previous verified V49 source remains rollback; EXP388 RUNNING/PARTIAL. One OFFLINE controlled operation: compare original V49 and V83 B11D start/feed/expected/splitter spans (4/4 exact), run original generic V49 StreamParser with only synthetic safe generic FC03/FC04 frames. 21/21 source/log checks, 19/19 host assertions EACH strict, sanitizers and noexceptions; 4/4 TX/embedded compile refusal. Clean raw2/V5=2, synthetic pre-start partial raw2/V5=0 illustrates possible latching; BUT synthetic parser pending=1 whereas field first-fault R6-P10 p=0, so exact real mismatch root cause OPEN and host proof MUST NOT be misrepresented as local physical evidence. No live output/flash/controller restart, no physical address/register/payload in this offline test. Positive test criteria original source identity + mismatched CRC-valid host case; abort discard host package, no hardware rollback. Next passive first-alignment expectedCount+pending snapshot design without clearing historical B11D/P5/FIX2 latches. [Full result](V5DCM/V5DCM83_B11D_STARTUP_SOURCE_AUDIT_RESULT_20261020.md).

# V5DCM83-RX-ONLY-SHARED-SUPERVISOR-YAML-01 — **RUNNING / PARTIAL (FIRST ON-DEVICE LOG; NOT FULLY QUALIFIED)** (2026-10-20). This RESULT follows the original PREPARED / NOT RUN candidate below, rather than replacing its source-validation history. Hypothesis RX-only shared supervisor should keep DE low, UART TX hard-denied, original parser/HA telemetry and first-fault history. Baseline original verified V49 RX_ONLY/HARD_DENY, original-source SHA 62afe396…, controlled change only V83 source overlay. USER log SHA256 bac4ceb1…fac7a46f6 2435 lines 93.844s via connected ESPHome API, unique V83 running diagnostic samples14→104 unsafe0 sticky0 pin/switch0, software TX attempts0, TX02 rejected128/128, parser103→868 pages16→141 resync22 unchanged drops0, independent B11C counts/bytes agree, live heating/DHW readings. However boot-time B11D first fault `RAW_V5_FRAME_COUNT_MISMATCH` countDiff1 was already latched before earliest captured rows, parser22 resync and two RX faults likewise; B11D source restore_value:NO so not automatically inherited from previous firmware. No earliest boot FIRST_FAULT records, V83 current RX qualification FIX2 REVOKED and post-gap WAIT_GAP; 0 initial native FC23, owner/EOF/slot/0x0867 unproven. Positive: 94s RX-only operation and no new observed error increments; inconclusive: root cause of startup mismatch and long-term normal operation, no independent hardware timing/TX proof. **STATUS remains RUNNING / PARTIAL.** No user-requested native output/controller reboot; stop/rollback to known V49 if new fault/telemetry regression. Minimal missing data: earliest 10–15s ESP boot log from same run, if available; avoid unplanned reboot. Do not advance active test. [V83 live RESULT](V5DCM/V5DCM83_LIVE_RX_ONLY_FIELD_RESULT_PARTIAL_20261020.md).

**V83 RESULT CLARIFICATION — 2026-10-20:** User confirms **ESP32 flash/reboot only; Thermia controller continuously powered**. Initial B11D RAW_V5_FRAME_COUNT_MISMATCH and parser resync occurred before API log on warm controller bus; possible mid-frame attachment is HYPOTHESIS, no electrical/RTU causal proof. Preserve V83 RUNNING / PARTIAL; avoid calling this a controller restart or proven new controller epoch. [Source log analysis](V5DCM/V5DCM83_LIVE_RX_ONLY_FIELD_RESULT_PARTIAL_20261020.md).

# V5DCM83 RX-ONLY SHARED SUPERVISOR — **PREPARED / NOT RUN** (2026-10-20). Hypothesis: one software RX-only direction observer, referenced by B11D and watchdog, can maintain existing fault and production monitoring while old experimental actors remain unbound from hardware. Known-good baseline: user V49 receive-only with no native output; controller callback gap 10.351s, later 285 validated frames in 30.532s and 63 unanswered native challenges cumulatively; EXP388 RUNNING / PARTIAL. Controlled change: new shared safety observer + old native hardware-binding removal, one diagnostic, no other production-configuration changes. 77 source/YAML checks PASS; 78,313 host checks in three C++ modes PASS; two forbidden output builds rejected. Device compile/flash/execution not performed, so do NOT mark COMPLETE. Positive later: normal telemetry, no TX, safe direction, preserved sticky faults. Negative: lost HA entities, output, new serial faults. Inconclusive: insufficient duration or source-only checks. Abort/recovery if later flashed: stop and restore original verified V49. [V83 source-preparation report](V5DCM/V5DCM83_RX_ONLY_PREPARED_20261020.md).

# V5DCM82-SINGLE-OWNER-HARD-DENY-SCHEDULE-HOST-01 — **COMPLETE / POSITIVE (OFFLINE ONLY: original V49 source + TX-LOCKED HOST driver interface; PHYSICAL TX NOT RUN)** (2026-10-20). HYPOTHESIS one logical borrowed UART owner can provide B11D 50ms and watchdog1s fail-closed RX-only read-only observations, with original V45 unchanged and zero TX ability, across their scheduler interleavings; not a physical bus-owner/response-slot test. BASELINE user V49 RX_ONLY/HARD_DENY TX0, 10.351s controller restart callback gap,285 matched postgap/30.532s,63 cumulative unanswered native FC23, original sticky B11D/P5/FIX2; EXP388 RUNNING/PARTIAL; current physical peer/slot/EOF/controller 0867 UNKNOWN. PAST EXP256 solitary native response then COMM ERR; EXP257–258 page progression, EXP355/386 historic native32, V74–81 source-host. ONE OFFLINE CHANGE new nondeployable `v82_locked_port.hpp` with exclusive logical UART id, V45 read-only RX interface and watchdog read-only verdict, hard-denied TX/PreGuard/DE-high with sticky first fault (NO physical Port or GPIO method). Exact original 69-file V49 zip 62afe396…a85630, source audit30/30. Host tests 38081/38081 EACH strict, ASan/UBSan, noexceptions/noRTTI; four embedded/TX compile negatives PASS; 59 phase offsets×30 virtual seconds with B11D50ms/watchdog1s, 80 fault scenarios and 12 sticky fault variants; all synthetic and NO actual RTOS/electrical timing. Source shape mismatch 03E8 13/14,0410 21/22,0492 9/11,051E 9/10 requires current controller evidence; private backend not used V82; no native ACK/status handler. Source/host POSITIVE; physical native TX viability remains UNKNOWN, no flash/compile ESPHome, no register operation. Abort discard host candidate on failing checks; physical recovery N/A. **NEXT V83** RX-only source-preserving YAML migration candidate/driver observation consolidation, no TX or flash without separate scoped review. [Full V82 result](V5DCM/V5DCM82_SINGLE_OWNER_HARD_DENY_SCHEDULER_SOURCE_HOST_RESULT_20261020.md). 

**Reconciliation after 5 offline milestones V78–V82:** V78 actual private backend executed behind host FakePort; V79 35 host mock stage intents, V80 exact parser replay, V81 original V45 shared owner mock, V82 RX-only locked-source scheduler. No physical TX, no current-controller native proof, 32 local historic controller ACK != vendor APP33 C2. [Full 5-experiment evidence audit](V5DCM/V5DCM78_82_RECONCILIATION_20261020.md). EXP388 still RUNNING / PARTIAL. 

# V5DCM81-SINGLE-SUPERVISOR-V45-SOURCE-HOST-01 — **COMPLETE / POSITIVE (EXACT SOURCE + NONDEPLOYABLE HOST LOGIC ONLY, NOT LIVE TX)** (2026-10-20). HYPOTHESIS one shared synthetic owner can drive original V45 B11D decision and 1s watchdog deferral consistently across 35 source-derived initial/32-page/runtime metadata intentions, with no output and full fault/owner veto. LAST VERIFIED USER V49 RX_ONLY/HARD_DENY TX0, manual controller gap10.351s, postgap 285 matched CRC bytes/30.532s, 63 cumulative unanswered native requests, EXP388 RUNNING/PARTIAL, physical electrical owner/EOF/slot/0867 UNKNOWN. RELEVANT EXP255–258/355/386 (EXP256 one incomplete reply caused actual COMM ERR), V74–80 source/host, V78 backend host execution, V80 parser replay. ONE NEW OFFLINE CHANGE original V45 header copied byte-identical into NEW host-only B11D/watchdog shared lease model; 24/24 exact V49 source audits, 2236/2236 strict C++17, 2236/2236 sanitizer, 2236/2236 noexceptions, 4/4 embedded/private TX macro denial. Synthetic 35 externally mocked delivery confirmations; rejects wrong owner, pin-vs-switch, legacy TX, missing peer/slot/generation/provenance, stage count/order, timeout and BOTH supervisor context changes; no UART/DE/Port API, private native backend not invoked, no native FC16/runtime generation. Source V44B original watchdog may defer PreGuard before DE HIGH; V81 *new* stricter synthetic DE-HIGH policy NOT proven on board. POSITIVE host logic only; real native session/Connect APP33/C2 still OPEN; abort discard host model, device rollback N/A. No physical target/current value/payload in this test. **NEXT V82 OFFLINE** design one real driver output hard-denied and stress scheduling/profile, then qualify independent physical owner/EOF/slot before separate bounded user-run experiment. [V81 report](V5DCM/V5DCM81_SINGLE_OWNER_B11D_WATCHDOG_SOURCE_HOST_RESULT_20261020.md).

# V5DCM80-EXACT-V49-STREAM-PARSER-MULTIFRAME-RX-MIGRATION-HOST-01 — **COMPLETE / POSITIVE (SOURCE + RX-only HOST, no live TX)** (2026-10-20). HYPOTHESIS exact original V49 completed-frame source routing can preserve all CRC-complete ADUs across split/coalesced callbacks, unlike original V43/V44B actor one-frame gate, while honoring sticky B11D/P5 and without second UART or TX. VERIFIED user baseline installed V49 RX_ONLY/HARD_DENY TX0, user manual controller 10.351s gap, 285 postgap CRC/byte matched frames over30.532s, 63 cumulative unanswered native requests; EXP388 RUNNING / PARTIAL, owner/EOF/slot/0867 UNKNOWN. Prior EXP255–258/355/386 local; V74–79 offline. ONE controlled OFFLINE change: mechanically extract unchanged original V49 StreamParser (generic RX only), new nondeployable read-only all-frame dispatcher/negative host checks. Source pin 62afe396…a85630, 20/20 exact checks. Existing Oct3 raw XTR capture 2687 frames parsed 2687 each in single/split/coalesced host modes; 448 multi-frame callback batches artificially generated, NOT observed ESP callback frequency. Original V49 V43/V44B if parsed.size()==1 branch would omit these synthetic batches; new host observer emitted all. 8696/8696 strict, ASan+UBSan and noexceptions/nortti tests each PASS; 4 forbidden ESP/TX build compile denial PASS, no physical output interface. Positive for host routing only, original private native backend not invoked here; no on-device tests, full native session, physical owner or original Connect Online proof. Abort discard offline package; V49 rollback N/A. **NEXT V81 (NOT RUN)** single B11D/watchdog physical owner offline design + complete private service preflight, independent live electrical timing before separate bounded user experiment. [V80 full report](V5DCM/V5DCM80_EXACT_V49_MULTIFRAME_RX_MIGRATION_SOURCE_HOST_RESULT_20261020.md).

# V5DCM79-SINGLE-OWNER-FULL-SERVICE-BOUNDARY-HOST-01 — **COMPLETE / POSITIVE (source/host ONLY; native TX NOT RUN)** (2026-10-20). HYPOTHESIS: one payload-free nondeployable owner boundary can enforce one consistent DE/B11D/watchdog identity and ordered first + 32-page + runtime metadata stages, including multi-frame dispatch and fail-closed context; no real service frames. LAST verified known-good V49 RX_ONLY/HARD_DENY TX0, manual controller 10.351s callback gap, post-gap 285 CRC/byte matched frames/30.532s, 63 unanswered native FC23 cumulative; live owner/EOF/slot/0867 unknown, EXP388 RUNNING / PARTIAL. Prior EXP255-258/355/386, V74-78 studied, no live replay. ONE controlled offline change new metadata-only host boundary and 15/15 exact V49 source audits (69-file zip sha256 62afe396…). Tests 2729/2729 g++ strict, ASan+UBSan, noexceptions/nortti each, 4/4 forbidden build guards. 35 mock confirmations, 32 ordering/profile checks, B11D/watchdog/DE fault veto, batch events; no native 0x0F code/CRC or actual UART/DE output. Original private backend NOT run in V79 (V78 yes). Positive is HOST model only; XTR semantic acceptance/physical owner/slot/C2 Online remain OPEN/UNKNOWN. Abort discard host candidate; device recovery N/A. **NEXT V80:** offline true UART ownership/watchdog/native service migration design, then separately authorized user-run bounded live TX only when independently qualified. [Full V79 report](Research/V5DCM/V5DCM79_SINGLE_OWNER_FULL_SERVICE_BOUNDARY_HOST_RESULT_20261020.md).

# V5DCM78 — COMPLETE / POSITIVE (offline only). Exact archived source linked and exercised with nonphysical test port. Six default-build checks passed without port output; ten isolated host-mode checks passed; 53 fault-control checks across 13 scenarios passed, including sanitizer runs. This does not establish physical transmission, controller acceptance, or a complete runtime session. Installed V49 and EXP388 remain unchanged. NEXT: V79 offline complete-service interface audit. [V78 report](V5DCM/V5DCM78_PRIVATE_BACKEND_V42_FAKEPORT_SOURCE_RESULT_20261020.md).

# V5DCM77 — COMPLETE / POSITIVE (offline host DE ownership audit, 2026-10-20). Original V45 safety rule tested unchanged with a single non-emitting FakePort owner; 3×3245 checks passed and four unsafe compilation configurations rejected. Baseline remains V49 receive-only and installed firmware unchanged. No real physical output or session admission tested. Full report: [V77](V5DCM/V5DCM77_EXCLUSIVE_UART_DE_OWNER_V45_HOST_SOURCE_RESULT_20261020.md).

# V5DCM76-EXCLUSIVE-NATIVE-TX-DRY-TRANSPORT-OFFLINE-01 — **COMPLETE / POSITIVE (HOST ONLY: 2332/2332 normal, 2332/2332 ASan/UBSan, 2332/2332 noexceptions/nortti, 4/4 prohibited builds denied; actual UART TX0)** (2026-10-20). HYPOTHESIS one exclusive owner + dry confirmed tickets can preserve V75's 32-page native controller service and fail-closed all transport context without a private response/wire TX. Last VERIFIABLE user V49 RX_ONLY/HARD_DENY user manual controller restart gap10.351s, 285 matched frames/30.532s, incoming native FC23 63 cumulative with no response, owner/EOF/slot/0867 unknown, EXP388 RUNNING/PARTIAL. Relevant prior EXP255/256/257/258 and EXP355/386 locally run historical (EXP256 incomplete responder caused COMM ERR), V47 real TX blocked, V49/V69/V74/V75 host scope. ONE OFFLINE CHANGE: nondeployable new V76 single claimant dry port `claim`→`dry_stage`→`dry_confirm`, V75 unchanged 1 initial intent+32 native page ACK intents+1 native runtime FC16 intent+1 native FC03 0708 intent, **all 35 confirmations HOST SYNTHETIC, no Modbus bytes**, no actual callback/DE writer; veto duplicate owner/physical output/no follow-on service/missing ticket/altered original fault history/operator Abort. Host 2332 checks each of 3 modes PASS, four compile negatives PASS, zero UART/DE. Original V49 ZIP source and V43 protected backend existence verified, not executed/disclosed. Positive only for dry API, native admission/controller acceptance OPEN, actual owner/EOF/slot unmeasured. No physical slave/address payload nor register changes in this experiment; offline abort discard synthetic adapter, device rollback N/A. **NEXT V77:** private true code seam audit and fake-port full-service integration, independent physical slot/owner/DE safety before any separately user-initiated TX. Report [V76](V5DCM/V5DCM76_EXCLUSIVE_NATIVE_TX_DRY_TRANSPORT_INTEGRATION_OFFLINE_RESULT_20261020.md); zip SHA256 c5f1289f8a3b8529f675e89ed1be5eda7ca557f891ab002e8863b840241d1660.

# V5DCM75-SINGLE-OWNER-FULL-SERVICE-INTENT-OFFLINE-01 — **COMPLETE / POSITIVE (HOST-ONLY state-model; NO REAL NATIVE TX)** (2026-10-20). Hypothesis: source-grounded historic full 32 native ACK and runtime 085F/0708 session may be modeled under ONE owner and fail-closed **external delivery-confirmation tickets**, without claiming controller adoption. Last verified user V49 RX_ONLY/HARD_DENY TX0, manual controller restart callback gap10.351s +285 CRC matched/30.532s post-gap, 63 cumulative native approval unanswered, physical owner/slot/EOF/0867 unknown, EXP388 RUNNING/PARTIAL. Relevant past: EXP255/256/257/258 and EXP355/386 native ACTUAL local results, V47 no TX fault-denial and V69/V74 TX-gate source proof; V70–73 separate slow RX diagnostics; no live repeat. ONE offline change: host-only abstract metadata actor with 32 directly source-extracted `write_stage=3..34` page shapes from original public v4.1, plus runtime FC16/0708 INTENT + confirmation model. Positive after mock one approval response, 32 ACK intents, runtime FC16 ACK and 0708 status intent explicitly mocked as externally delivered = 35 hypothetical confirmations; then Active model only, NOT Original Connect Online. Source 2.1.105 APP33 vs XTR native32 overlap25, native-only7, app-only8 (actual source metadata, no live app). Strict 6444/6444 assertions EACH normal+ASanUBSan+noexceptions, four prohibited ESP/Arduino/TX-flag compile tests correctly failed, all wire output0. Tests include second validated frame dispatch, unknown owner/slot no intent, no complete-service capability no Arm, missing ticket, peer, DE, firstfault history altered, wrong count for every page, CRC, epoch, stale, 60s operator scope, 5s first request/per-page and bounded model; host timestamps NOT electrically measured. No physical target bytes/current register values/physical operation, abort=discard host model; live V49 remains unmodified. Original actual EXP256 one-reply incomplete caused COMM ERR; no new responder flashed. **NEXT V76:** offline ONE real exclusive TX/DE owner fake-port integration and full-session transport with private dynamic backend (keep confidential), verify physical EOF/slot before any active test; EXP388 unchanged. [V75 report](V5DCM/V5DCM75_SINGLE_OWNER_FULL_NATIVE_SESSION_INTENT_HOST_RESULT_20261020.md). ZIP SHA256 f43c9afe747831183968c57ccf66bb0f3271d70e88626db8df78d8ee2263b61a.

# V5DCM74-NATIVE-TX-SOURCE-BLOCKERS-HOST-01 — **COMPLETE / POSITIVE (OFFLINE ONLY: 27/27 source checks, 23/23 default FakePort, 23/23 both flags FakePort, 23/23 sanitizer default, 23/23 sanitizer with both flags; bus TX0)** (2026-10-20). Hypothesis: V49 source cannot solve native TX by compile flags; controller session/full-service, timing, ownership and source routing are independently blocked. Last verified user-installed V49 RX_ONLY/HARD_DENY no TX, manual 10.351s gap, 285 matched/30.532s RX cohort, FC23 cumulative63 unanswered, physical owner/slot/current0867 unproven, EXP388 RUNNING/PARTIAL. Prior EXP255–258, EXP355/386 complete old local, V47 inconclusive NO-TX, V48/49/V69–73 retained and NOT repeated live. ONE controlled offline action: SHA-verify original 69-file V49 private ZIP and V42/V43/V44B/V45 code/YAML; source-level eight gate audit; compile unchanged V42 OneShot and V45 DE-owner with fake Port, two host-only flag modes and ASan/UBSan, without request/response bytes; simulate 2 anonymous parsed items and 10.351s/1s/30s/1.283s timing comparator. **PROVEN SOURCE:** V49 build disabled; V43 Arm gen0/timing=false/risk=false, 1s window, peer/owner/epoch/slot=false; two actors share UART DE and B11D/watchdog honor only V44B; only parsed.front forwarded to both; V49 lacks old full ACK/status engine; post-gap 30s RX witness arrives too late for +1.3s cold first request. Original V42 both flags still rejects original V43 Arm, fake port TX0 92/92 assertions total. EXP256 one-response-only previously caused COMM ERR so new full service essential. Positive scoped source evidence; NEW native acceptance and physical EOF/owner/slot INCONCLUSIVE/UNKNOWN, no live experiment. No physical target/payload/register/current value in V74 as no bus operation; abort on source pin/test mismatch and discard host tool, rollback device N/A. **NEXT V75 source-only full guarded exclusive TX-owner and complete native session state modeling** before separate bounded user-initiated live test; do not remove switches or publish protected 0x0F backend. [V74 result](V5DCM/V5DCM74_NATIVE_TX_EARLY_SESSION_BLOCKER_SOURCE_HOST_RESULT_20261020.md) reproducible host ZIP SHA256 7a9e4ff2de51e5218ff1e5a103df546dd476e4d24c282a4e4bd19f76bbf4c8f6.

# V5DCM73-FIXED-BUFFER-ROLLING-RX-WRAP-SAFE-HOST-01 — **COMPLETE / POSITIVE (OFFLINE HOST ENGINEERING ONLY: 56/56 normal, 56/56 ASan+UBSan, 56/56 noexceptions/nortti, 4/4 compile guards; prior V71 40/40)** (2026-10-20). HYPOTHESIS: V71 dynamic hot-path allocations in noexcept and normal uint32 millis wrap failure can be fixed without touching original B11D/P5/FIX2 or native TX. LAST VERIFIED baseline current live V49 RX_ONLY/HARD_DENY 10.351s manual controller callback gap, original V49 285 matched/30.532s frozen post-gap witness, native FC23 63 cumulative unanswered, all UART TX0, current 0867/owner/EOF/slot unknown; EXP388 RUNNING/PARTIAL. PRIOR relevant completed V47/48/49/69/70/71/72, EXP255/256/257/258/355/386; no physical repeat. ONE CONTROLLED OFFLINE CHANGE: build separate nondeployable fixed-array V73 rolling RAW/V5 comparator with bounded 4096 RAW,4096 expected,128 descriptors,96-byte first-fault label and unsigned modular elapsed guards. 12,288 original candidate geometry comparisons + exact unchanged inline V49 parser 5 callback tests, independent CRC, under-250ms split vs new incomplete>250ms, current invalid CRC, resync, byte mismatch, altered historical first fault, DE/TX, second software gap and 49.71-day natural wrap all tested. Total V73 member object 8896 bytes on x86-64; ZERO C++ new calls for artificial 128 short/long frame bursts in **V73 observer only**, not complete V49 callback; on-device embedded memory/CPU/PSRAM/stack NOT MEASURED. FULL C++17 56/56 normal+sanitized+noexceptions; 4 compile denials TX and embedded; V71 prior 40/40. Positive strictly HOST ONLY, physical tests/TX/flash/YAML NOT RUN. **Abort** discard host code on checksum, allocator, CRC, fault or deny failure; device recovery N/A because production V49 remains unchanged. **NEXT V74 whole-callback source/performance analysis offline before ever preparing user-run RX-only build**; no unauthorized TX unlocking, fault clearing or incomplete native responder. Package SHA256 f511c2be0a16e4af6cb84b244dd6785827ac22b77b42f9a38280b159e5ac6b50. [Report](V5DCM/V5DCM73_FIXED_BUFFER_WRAP_SAFE_ROLLING_RX_OFFLINE_RESULT_20261020.md).

# V5DCM72-V71-EMBEDDED-INTEGRATION-READINESS-OFFLINE-01 — **COMPLETE / POSITIVE (OFFLINE diagnostic audit; deployment NOT READY)** (2026-10-20). HYPOTHESIS V71 source/host can be certified for direct ESP32 integration or specific blockers found. Last user V49 RX_ONLY/HARD_DENY; 10.351s gap after manual controller OFF/ON; matched RX285/30.532s, native FC23 cumulative63 without response, EXP388 RUNNING/PARTIAL. Past V47/48/49/69/70/71 (V71 40/40) not repeated live. ONE controlled offline action: exact V49+V71 SHA pin inspection, static ESP32S3/PSRAM/UART single callback review, host g++ O2 source-linked 2k frame + 2×200 artificial 128-frame burst/heap instrumentation, near32bit clock wrap and CRC counter mismatch, V71 40/40 plus sanitizer and 4/4 compiler guards rerun. **RESULT V72 6/6 pass.** HOST mean/max 128×8 =236.61/497.24us, 301000 allocations/200 trials; 128×31=113.17/209.30us, 311000 alloc/200; tracked peak ~30693 live requested bytes (not device heap). Clock normal unsigned wrap triggers permanent ClockRollback revocation at49.71d. Dynamic STL allocations in noexcept callbacks → terminate on OOM, FAIL integration readiness (not native TX safety proof). Hardware ESP32 CPU/heap/PSRAM, exact inline production parser integration/physical owner/slot still UNKNOWN. **No physical targets/writes/outbound payload/risks/timing** in V72, fail/abort=discard host fixture; on-device rollback N/A. Old B11D errors preserved and TX permanently denied. Next V73 fixed bounded buffers and wrap-safe timers OFFLINE before any separately prepared RX-only flash. [V72 report](V5DCM/V5DCM72_V71_EMBEDDED_MEMORY_WRAP_PERFORMANCE_OFFLINE_RESULT_20261020.md).

# V5DCM71-SINGLE-CALLBACK-ROLLING-RAW-V5-RX-ONLY-HOST-01 — **COMPLETE / POSITIVE (OFFLINE HOST ONLY: 40/40 strict original-source CRC/geometry, 40/40 ASan/UBSan, 4/4 compile guards)** (2026-10-20). Hypothesis: prior controller restart can leave a truncated ADU (V47 observed 17-byte remnant, B11D 250ms, +17 resync) without proving a lasting CURRENT UART fault; maintain old sticky fault but separately diagnose NEW clean RX. Last locally verified V49 RX_ONLY/HARD_DENY/TX0, manual 10.351s gap, 285 matched/30.532s V49 frozen Recorded; native FC23 cumulative63 unanswered, owner/epoch/slot unknown, EXP388 RUNNING/PARTIAL. Prior V47/48/49/70 source reviewed, not rerun. ONE OFFLINE HOST change: nondeployable independent rolling RAW/V5 comparator, reusing unchanged original V49 callback positions and compiled original portable candidate_lengths/CRC sources; source first-fault pre-gap must be independently proven, 30s/100 NEW matched frames required, no TX. 40/40 normal and sanitized pass; split partial ADU <=250ms finishes, post-clean orphan >250ms revokes; new parser/CRC/byte mismatch/DE/clock/second gap/first-fault alteration deny. Four compile guards independently reject 2 V42 TX flags and ESP/Arduino. Original V49 real continuous callback NOT modified and original B11D/FIX2 fault never cleared; synthetic future V5 frames supplied by host fixture (not genuine user device), original production V5 parser not run in V71 host, embedded perf/owner/EOF unknown. No physical target/TX/write/timing/current setting/risk, abort only discard failed host fixture; no device recovery. Positive applies to source feasibility, NOT on-device requalification or native Online. Next potential offline ESP32 memory/counter-wrap source audit, separate future RX-only prep only after evidence review. [V71](V5DCM/V5DCM71_ROLLING_RAW_V5_SINGLE_CALLBACK_RX_ONLY_OFFLINE_RESULT_20261020.md).

# V5DCM70-RX-REQUALIFICATION-HISTORICAL-FAULT-SEPARATION-OFFLINE-01 — **COMPLETE / POSITIVE (HOST MODEL ONLY: 40/40 normal, 40/40 ASan/UBSan, 2/2 TX guard compiler denials)** (2026-10-20). Hypothesis: preserve old B11D sticky history yet distinguish independently verified NEW current CRC/RAW/V5 receive health using a new RX-only diagnostic, not changing FIX2 or TX. VERIFIED baseline local user V49 RX_ONLY/HARD_DENY, 10.351s user manual controller gap, 285 fresh historical frames/30.532s, TX0, native FC23 63 unanswered; V47 17-byte orphan B11D+17 resync and TX denied; EXP388 RUNNING/PARTIAL. Prior V45/47/48/49/69 and EXP255–258/355/386 used as immutable evidence. **ONE controlled HOST-only change:** source-pinned existing V49 Recorded plus synthetic independent live CRC-matched rolling frame counters; new read-only model needs additional >=30s/100 matched NEW frames, old first fault demonstrably pre-gap, 3s freshness, no new resync/drop/CRC/raw fault/de/output/changed epoch; stale >5s revokes. Original FIX2 remains REVOKED after old fault (host-proven), old B11D sticky never cleared; 40/40 host assertion plus sanitizer pass, both separate V42 TX build macro attempts fail under original V49 `#error`. **CRITICAL LIMIT:** V49's original diagnostic freezes after 30s and B11D stops processing after sticky fault, so independently continuously checked source is NOT on the XTR; tests use SYNTHETIC comparator evidence. V70 never permits TX/Online/owner/epoch and is NOT an ESPHome YAML. No physical payload/register/current value, controller timing, risks/abort/recovery on device; offline fail = discard host prototype. Future V71 independent RAW/V5 current comparator source review only; no active next test or flash. Package SHA256 38cefccb8dcf6f17a17ad8616c2c5403dbc228c55fe0ab123cc1ede621aa6e7a. [V70 result](V5DCM/V5DCM70_HISTORICAL_FAULT_VS_CURRENT_RX_REQUALIFICATION_OFFLINE_RESULT_20261020.md).

# V5DCM69-V49-FIRST-UNEXERCISED-NATIVE-RESPONSE-GATE-OFFLINE-01 — **COMPLETE / POSITIVE (3/3 strict original-source safe-build tests, local historical stage comparison; master cause unproven)** (2026-10-20). HYPOTHESIS current V49 native service absence is upstream nonparticipation, not demonstrated rejected native response. Baseline user V49 RX_ONLY/HARD_DENY 285 clean frames/30.532s after user manual Thermia OFF/ON gap10.351s, 63 cumulative native FC23 unanswered, no strict 03E8/0864/0708 in bounded sampled user logs; EXP388 RUNNING/PARTIAL. Prior complete EXP254/255 no-response, EXP256/257/258 one-response/FC16 ACK-ladder, EXP355/386 full historical service, V47 integrity denial, V58/61 and V66–68. ONE CONTROLLED OFFLINE CHANGE: verify exact V49 ZIP source gate (both compile flags absent, static assert kBuildMaySend=false) and compile UNCHANGED v5dcm42 OneShot with fake non-hardware Port under 0/one TX flag builds; all **3/3 PASS** BuildLocked Arm, zero tx and online. User V49 runtime Arm DENIED, no physical TX, no semantic acceptance attempted. Conclusion PROVEN build lock/nonattempt, STRONGLY SUPPORTED no-responder branch, OPEN master acceptance/owner/EOF/slot/actual 0867; prior EXP256 intentionally incomplete responder caused COMM ERR and DHW-side0. Positive=fail-closed code+prior stage reconciliation; negative=observed new V49 TX/controller progression; inconclusive=unsupported exact master cause. Abort/rollback offline N/A; no native payload, secrets, YAML, reboot, TX, flash. Next guarded full-session feasibility only offline, no changing TX flags alone. [V69 result](V5DCM/V5DCM69_V49_FIRST_UNEXERCISED_NATIVE_GATE_OFFLINE_RESULT_20261020.md).

# V5DCM68-VERSION-WAIT-RX-ONLY-SHADOW-HOST-01 — **COMPLETE / POSITIVE (17/17 final C++ source-only assertions; NOT flashed)** (2026-10-20). Hypothesis: version-WAIT chronology can be modeled in read-only shadow using same existing V49 CRC-completed frames/V21 ledger/V22 33 descriptors with default UNKNOWN, fail-closed post-FC23/CRC/unsupported-version, zero Online/TX. Baseline V49 user live RX_ONLY/HARD_DENY TX0, native 0864 absent in 30.532s sample, EXP388 RUNNING/PARTIAL. Prior V57/V62/V66/V67; no repeats. ONE OFFLINE source-only change: disposable nondeployable shadow selects source 2.4.2 profile only on modeled exact 0x0F FC16 0864/count4 with 0867=242 and credits same event; 232 unsupported. Final checks 17/17 include late/replayed pages, duplicate version, foreign slave, bad CRC, native FC23, no auto rearm, explicit host-only reset and permanent TX/Online=false. Initial host prototype sequencing assertion failed before local fixture fix; not original V49/vendor fault. No YAML/firmware modifications, TX/flash/restart, physical risk/recovery. Since real V49 short log contains no 0864, do NOT flash this shadow for no-new-information. Next novel offline discriminator of native approval/service gate. [V68 report](V5DCM/V5DCM68_RX_ONLY_VERSION_WAIT_SHADOW_HOST_FEASIBILITY_RESULT_20261020.md).

# V5DCM67-V49-RAW-VS-VENDOR-WAIT-TIMELINE-OFFLINE-01 — **COMPLETE / POSITIVE (8/8 unchanged-source offline tests)** (2026-10-20). Hypothesis: same exact 33 page receipts can make V49 source-selected raw ledger report 33/33 but original 2.1.105 version/WAIT tracker incomplete. Verified running baseline V49 RX_ONLY/HARD_DENY physical TX0 user-reported, no on-device source-version 0867 sampled; EXP388 remains RUNNING/PARTIAL. Relevant V21–23/V57/V62/V66; no prior native experiment rerun. **ONE CONTROLLED OFFLINE CHANGE:** chronology of original 33 local-XTR profile descriptors relative to 0864/version event and optional later replay, using original V49 C++ classes with CRC-valid synthetic FC16 and verbatim original Connect Python tracker class. **RESULT:** 8/8 PASS; version-first 33/33 both, 31 pre-version 33/33 vs 2/33, 25 pre-version 33/33 vs 8/33, one pre-version 33/33 vs 32/33, later replay repairs to both 33/33, no version original remains INITIAL, duplicate benign, 0867=232 unsupported profile deliberately UNKNOWN. Original firmware config loading/app/cloud not run. Proven chronology-dependent RECEIPT discrepancy only; 33/33 not OEM C2/Online. Safety target FC16 receive shapes only; no output slave/payload/current value, controller timing, TX, flash, reboot, new YAML. Abort/rollback N/A offline. Next V68 offline shadow feasibility, fail-closed version UNKNOWN and TX HARD_DENY. [V67 report](V5DCM/V5DCM67_V49_RAW_LEDGER_VS_CONNECT_VERSION_WAIT_OFFLINE_RESULT_20261020.md).

# V5DCM66-V49-RECEIVE-LEDGER-TO-CONNECT-APP-SEAM-OFFLINE-01 — **COMPLETE / POSITIVE EXACT-SOURCE + 13/13 HOST ASSERTIONS; PHYSICAL/ORIGINAL CONNECT APP OPEN** (2026-10-19). Hypothesis: verify whether V49 RX-only only reports descriptive 33-group raw shapes or ALREADY embeds real portable V21 ledger, and identify version/WAIT/online seam without another live trial. Last verified user-running V49 RX_ONLY/HARD_DENY TX0 10351ms manual controller OFF/ON RX gap, 285 clean frames/30.532s, 04A6/085F present, no sampled 0864/0708/03E8, first seven native FC23 unanswered, later63 cumulative console-discontinuous; flashed binary SHA unverified. Relevant V21–23 (implemented), V37, V54/56/57, V62, V65 historic XTR proof; Eco5/ATEC display generation older. ONE controlled change OFFLINE: extract exact user V49 ZIP SHA256 62afe39629102a3daa06f09eab3ed159f44437d702fb8d3904c61e62e2a85630; source review exact callback/onboot/bridge, compare REAL Connect 2.1.105 cm_client_type.py + client.py; compile UNCHANGED original V49 private V23 NativeRxLedger+V22 PassiveWitness with original portable CRC/frame/core C++ and synthetic received frames. **13/13 PASS:** profile selected immediately at boot without 0867; 04A6/13 pre-version credited; FC23 revokes; later 0864 does NOT auto reselect; explicit host reset does; exact 33 geometric pages complete only descriptive ledger, owner/accepted/Online/TX false; bad CRC revokes; V22 ever count retains pre/post FC23 while active session remains revoked. V49 already calls v5dcm23::ledger().on_native_crc_validated_bytes(f.bytes, v5dcm22_rx_clean) after c.on_frame in SAME parser callback, with original V22 witness and 30s status; not a missing adapter. **GAP** Connect true version-led WAIT, same-callback version receipt, parameter publication/OPERATION/Online, current controller epoch/owner/EOF/slot; no on-device C2 proof. No YAML edits, new native TX, controller restart, flash/full ESPHome compile, original Connect method replay or secrets. No physical recovery necessary. **NEXT** source-only nonflashable two-timeline comparison if it provides novelty, NO second observer, no repeat live prior tests. [V66 report](V5DCM/V5DCM66_V49_EXISTING_RX33_LEDGER_VS_CONNECT_APP_OFFLINE_RESULT_20261019.md).

# V5DCM65-XTR-LOCAL-FIRST-NATIVE-CAPABILITY-BOUNDARY-OFFLINE-01 — **COMPLETE / POSITIVE (documentary same-generation XTR capability reconciliation ONLY)** (2026-10-19). Hypothesis: previously V64 Eco5/ATEC bitmap resend/W5 patterns (OLDER DISPLAY generation per USER) may already have locally proven XTR subsets in historical EXP tests; avoid cross-model overwrite. Last VERIFIED user-live V49 RX_ONLY/HARD_DENY 10.351s post user OFF/ON UART callback gap, 285 matched clean RX /30.532s, TX0, sampled 03E8/0864/0708 missing and native FC23 unanswered; no new XTR device action. One OFFLINE controlled change: review historic source-pinned v4.1 9186-line YAML Git blob `8e8a8268`, canonical exact old EXP296/297/315/343–345/352/355/386 statements and vendor source architecture/flags. **Result PROVEN historical local:** EXP352 requested fresh controller page with `0708 W3b0=1 W1=0`, FC16 03E8/count14 followed ~120ms and 03F4=23 (not desired pull); EXP343/346 locally proved separate W1b0 desired FC03 pull → controller FC16 confirmed semantic 03F4 update/rollback; EXP296 >=16 loops/159 events 329.8s, later >32min; EXP315 6 retained cycles/126.401s/30 answered 0708; EXP355/386 full 32/32 cold rejoin; EXP344 local 0708 W5=0000 icon lost despite transport-clean >15min, EXP345 only W5→0006 kept icon at 900.5s with379 ACK+210 statuses (no Online proof). Cross-model older-display Eco5 W5=0000 264/264 vs ATEC/DCM03 W5=0006 65/65, exact original 2.0.18/2.1.105 flag W1/W3 stable, W5 no named original writer. **NOT LOCALLY PROVEN:** other31 W2/W3 request bits, official 2.1.105 33-group / map app readiness, cloud, current V49 owner/slot/version/active native acceptance. No new source build/flash/TX/controller action/semantics, no protected code, no rollback. Past statuses preserved (EXP388 RUNNING/PARTIAL). [V65](V5DCM/V5DCM65_XTR_FIRST_EVIDENCE_VS_LEGACY_DISPLAY_PROFILE_OFFLINE_RESULT_20261019.md).

# V5DCM64-LEGACY-DISPLAY-REQUEST-REEXPORT-OFFLINE-01 — **COMPLETE / POSITIVE (OFFLINE CROSS-MODEL METADATA/PROVENANCE CORRECTION ONLY)** (2026-10-19). **Hypothesis:** older-display Eco5/ATEC post-version repeated FC16 settings pages follow W2/W3 request bits from valid paired native FC03 0708 readbacks, not necessarily spontaneous native boot/sync. **Last user-installed XTR baseline:** V49 RX_ONLY/HARD_DENY, user OFF/ON 10.351s UART callback gap, clean 285 matched frames/30.532s and UART TX0; current 0867, 03E8/0708, native owner/physical slot unknown. **Past evidence:** V54/55/57/59/62/63, locally completed EXP254/255, EXP355/386, user provenance Eco5/ATEC OLDER DISPLAY FIRMWARE; byte-identical 2.0.18/2.1.105 native selector flags. **ONE CONTROLLED OFFLINE CHANGE:** strict CRC 25,031/25,031 original bytes, match prior 0708/count6 exact poll to 17B reply within <=300ms HOST analytic window, compare post-first0864 FC16 start to original flags-defined W2/W3 selector; independently decode 0867 fourth 16-bit word from FC16 0864/count4. **POSITIVE:** total post-version W2/W3 page requests 279 across seven reply-shaped segments, 278 have prior paired status, **276/278 exact bit ON**, **2 04BA OFF**, **1 04BA no prior**. Five Eco5 first positive-settings status→first FC16 intervals 79–110ms host, ATEC no post-version settings requests. **SOURCE ERRATUM:** old firmware repo mistakenly claimed Eco5 `0867=0000`; **actual raw Eco5 Sep26 32/32 and Sep28 16/16 `0867=00E8`=232**, ATEC Oct03 12/12 `0867=0016`=22. User older *display* version separate from 0867 hp_cm version; actual collaborator gateway binary unknown; old ATEC 22 must not be decoded as XTR. Three firmware-repo docs corrected with explicit V64 erratum. **UNKNOWN** causality/which endpoint set request bits, original app C2 and XTR master scheduling; no live test, HA/YAML/source emulator/CRC TX, sensor change, reboot, new flash, cryptographic/material disclosure or physical rollback. Previous V63, V62 etc not rerun live. [V64 report](V5DCM/V5DCM64_LEGACY_DISPLAY_VERSION_AND_REQUEST_BITMAP_CORRELATION_OFFLINE_RESULT_20261019.md).

# V5DCM63-W4-POST-VERSION-CHRONOLOGY-OFFLINE-01 — **COMPLETE / POSITIVE (offline archived frame chronology; original application C2 INCONCLUSIVE)** (2026-10-19). HYPOTHESIS: ATEC/Eco5 historic FC16 W4 and settings-page after first version-bearing 0864 chronology provides stricter proxy for hypothetical 2.1.105 33-group data-receipt opportunity than V62 full-file counts; test without invoking firmware source or TX. Baseline unchanged user-installed V49 RX-only HARD_DENY, TX0, 285 clean post user OFF/ON callback-gap frames/30.532s, current 03E8/0864/0708 not observed; no new safety authority. Relevant completed V54/V55/V57/V59/V62; EXP254/255/355/386 retained; provenance erratum R6-P74DI-B10/B12. ONE CONTROLLED CHANGE: strict independent 25,031 frame CRC/FC16 geometry replay of 7 archived raw files; segment at next FC23 challenge after reply shape; count distinct ORIGINAL 2.1.105 selected 33 group **request** starts at/after first 0864 by log row ordering and same start/count short ACK envelopes <=300ms host-clock filter. POSITIVE raw: 7/7 source CRC correct, all 7 reply anchored windows 31/33 (25 W2/W3 + 6 W4) **BEFORE** version page; after 0864 counts ATEC8, Eco5 Sep26 2/33 and 33/33, Eco5 Sep28 31/33,33/33,30/33,31/33; 2 full groups have 33/33 host ACK-paired shapes, first complete post-version type coverage at +79.947/+81.025 seconds. **UNKNOWN:** actual Connect client/version/profile WAIT or parameter publish, current XTR C2, physical epoch/owner/EOF/slot. **PROVENANCE CORRECTION:** Sep25 thermia_capture model unknown, Oct03 ATEC+DCM03 collaborator, Eco5 cross-model. No current XTR live action, HA, YAML, TX, compile, firmware changes, secrets or protected software. No rollback. [V63 report](V5DCM/V5DCM63_W4_POST_VERSION_CAPTURE_CHRONOLOGY_OFFLINE_RESULT_20261019.md).

# V5DCM62-ORIGINAL-21105-32-VS-33-SOURCE-TRACKER-OFFLINE-01 — **COMPLETE / POSITIVE OFFLINE SOURCE/MOCK ONLY** (2026-10-19). HYPOTHESIS: v4.1 native 32/32 bootstrap differs by more than one group from genuine Connect 2.1.105 profile2.4.2 33 app receipts; original publication gate cannot be satisfied by 32 alone. Last verified live V49 RX_ONLY/HARD_DENY unchanged: user OFF/ON 10.351s callback gap, 285 clean RX frames/30.532s, native TX0, sampled 03E8/0864/0708 absent and ongoing 04A6/085F; 13+min console gap; V47 INCONCLUSIVE. RELEVANT completed history V21/V53/V54/V57/V61 and historical EXP355/386 native 32/32 success, EXP388 PARTIAL. SINGLE controlled OFFLINE action: direct original 2.1.105 AppFS JSON+flags token parse (570 objects, 541 numeric refs), 32 EXP355 native source starts intersection, original AST-extracted CMClientParameterUpdateState and actual on_publish_cm_params_map_event host-stub executions, plus exact 2.0.18 source negative control. **RESULT 9/9 original tracker scenarios and 2/2 original publication scenarios PASS**; 32 native starts intersection 33 significant group starts **25**, 7 bootstrap-only and 8 missing W4 operation/runtime groups; W2=BFFF W3=867F W4=035F internal masks. All32 post-seed clear25, W4 8 remain, original map publish postponed; after 8 further receipt groups application tracker complete and stub publish occurs. Pre-WAIT pages not back-credited; first 0864 version-page can seed+credit same callback per previously verified V57, with seven W4 still required after subsequent full bootstrap. Original 2.0.18 has no equivalent 33 wait gate. **NOT PROVEN** physical current profile, onboard/cloud Online, actual W4 arrival/owner/slot; no source firmware runtime, live test, SHA attested flashed V49, TX, YAML, controller restart, protected material. [Full report](V5DCM/V5DCM62_ORIGINAL_21105_BOOTSTRAP_33_GROUP_DELTA_OFFLINE_RESULT_20261019.md).

# V5DCM61-XTR-INTERVENTION-LADDER-OFFLINE-01 — **COMPLETE / POSITIVE OFFLINE INTERVENTION RECONCILIATION ONLY** (2026-10-19). Hypothesis: compare local no-responder EXP254/255, bounded reply-only EXP256, next-page ACK EXP257/258, and historic complete service EXP355/386 to distinguish observable controller approval, first-settings and runtime transitions without claiming full original Thermia Online. Verified live baseline unchanged V49 RX-only, 10.351s user OFF/ON callback gap, 285 clean frames/30.532s, TX0, no sampled 03E8/0708, >13min console discontinuity. Relevant old experimental statuses unchanged; single controlled action documentary evidence cross-check in canonical state/log, G01/GAP and original Connect V54/56 source-derived reports (no original EXP355/386 full raw reparse; no new firmware-host tests). **Result:** EXP255 63 unanswered FC23, FC16 582 background 04BA4+04A6383+085F195, FC03/ACK0; EXP256 one historic native response -> 03E8/14 +124ms then 389 repeated no ACK, no FC03, communication-alarm side effect; EXP257 one first-page ACK -> 03FC/11 +691ms; EXP258 next ACK -> 0410/22 +1501ms; EXP355/386 full prior 32/32 then runtime0708, EXP355 busreturn→terminal ACK 33.595s (not general XTR 120s). Old V4.1 32 native ACK stages do NOT prove original 2.1.105 33 software profile groups; original CM930 04A6 H2 path differs from controller-master admission. Positive only for evidence discrimination; open current V49 physical slot/owner, master accept rule, complete original app/cloud Online. No TX/YAML/compile/flash/controller intervention/secret publication. [V61 result](V5DCM/V5DCM61_LOCAL_XTR_NATIVE_STAGE_INTERVENTION_CONTRAST_OFFLINE_RESULT_20261019.md).

# V5DCM60 CONTINUITY ERRATUM (2026-10-19, not a new experiment): EXP248/249/251/254 completed passive local XTR 63-request native FC23 retry-exhaustion windows. EXP254 first+1.283s last+265.086s, 0708=0, ACK0, TX disabled. EXP255 COMPLETE/POSITIVE full seven-minute passive 0x0F census: FC23=63 first+1.284s last+265.513s, FC16=582 (04BA/22 4; 04A6/13 383; 085F/5 195), FC16 ACK0, FC03 req/rsp0, RX faults0, TX disabled; 219 FC16 after final FC23. Existing old continuous diagnostic sessions are NOT verified PHY-EOF/owner captures, and current V49 has console gaps, but repeating a no-responder boot is not a new discriminator. V60 root-cause status stays COMPLETE/INCONCLUSIVE; the original NEXT recommendation was corrected. [V60](V5DCM/V5DCM60_XTR_FRESH_VS_RETAINED_OBSERVABILITY_OFFLINE_RESULT_20261019.md).

# V5DCM60-XTR-FRESH-VS-RETAINED-OBSERVABILITY-OFFLINE-01 — **COMPLETE / INCONCLUSIVE (missing current native XTR master admission cause)** (2026-10-19). Hypothesis: archived XTR service windows + installed V49 source/log + original Connect slave firmware contain unique prerequisite for fresh FC23 approval->03E8 sync/0708 service. Last user-confirmed V49 baseline RX-only/HARD_DENY, manual OFF/ON 10351ms callback gap, clean 285 frames/30.532s, UART TX0; initial seven FC23 unanswered and cumulative63 later but >13min console gap; 03E8/0662/0708 unobserved in sampled windows, 04A6/085F ongoing. Prior V54–59, PROTO17/18 and local S11T already completed, not rerun as newly discovered tests. **Single controlled change OFFLINE:** independently check CRC+first-event shape coverage of SAME seven original files, original Connect 2.0.18/2.1.105 CM930 slave/source, and V49 ZIP RX-only witness. **25,031/25,031 original RTU rows valid CRC; old FOUR local XTR bounded files 2,451 frames, 54 native 0708 polls/38 paired replies, NO native FC23 within those BOUNDED excerpts.** All four are left-censored with unknown approval history; 0708-without-visible-FC23 cannot disprove fresh approval. Cross-model Eco5 file starts also precede their later FC23 boot episodes, reinforcing V59's BUS_RETURN alignment rather than file-start timer. Original Connect only proves SLAVE logic; V49 artifact prevents output but callback gap!=electrical EOF/current owner. **COMPLETE / INCONCLUSIVE** for candidate new causal discriminator; positive archival integrity/coverage audit ONLY. No exact master reason, current firmware0867, safe slot, controller epoch, first settings service/Online proven. No device action, protected implementation, YAML change, compile/flash, active test or fault-latch clear. The smallest actually NEW evidence is ONE future continuous passive current-XTR bus-return chronology, which is not yet available or queued. [V60 full report](V5DCM/V5DCM60_XTR_FRESH_VS_RETAINED_OBSERVABILITY_OFFLINE_RESULT_20261019.md).

# V5DCM59-FRESH-APPROVAL-VS-RETAINED-SERVICE-OFFLINE-01 — **COMPLETE / POSITIVE OFFLINE ONLY** (2026-10-19). Hypothesis: archived current/new native boot approval, initial sync ACK readiness, and retained runtime status service are distinguishable by existing strict envelope evidence without inventing controller master code or repeating already-completed experiments. Last VERIFIED live baseline unchanged V49 RX_ONLY/HARD_DENY, user-manual OFF/ON callback gap10351ms clean post-gap285frames/30.532s native TX0, 03E8/0864/0708 absent, 04A6+085F present, earlier V47 INCONCLUSIVE/TX0. RELEVANT PRIOR completed PROTO17 positive six genuine Eco5 successful/one failed sessions, PROTO18 COMPLETE/NEGATIVE 25-family readiness-field scan, old local S11T ACK0662→0708 positive, V54–V58. SINGLE controlled action OFFLINE CRC-valid frame envelope replay of 7 archived bus-return Eco5 epochs plus independent count of native0662/0708 sensor observations in TWO original current V49 console excerpts, source hierarchy firmware original for app semantics. **12/12 private offline metadata assertions PASS**; six success 2 early (+9.825/+10.043s) 4 late (+119.808–120.173s) reply envelopes; first03E8 ACK +118.478–120.296s; first0708 later +154.280–186.828s. Middle Sep26 failed window 41 FC23 requests without approved reply or 03E8/status to ~+171s. Important correction to previous PROTO17 prose: 102 03E8 requests timestamped before first ACK INCLUDE FINAL ACKed request; **101 unACKed prior to acknowledged 102nd**; original history preserved with addendum. +120s is Eco5/gateway/session observation NOT local XTR mandatory delay. Historic retained S11T context 0662+085F and ACK0662→0708~1.422s, does not establish universal prerequisite. V49 log 19+20 distinct samples both 0662 counter0, native status polls0; first seven unanswered native FC23 after user cycle, cumulative63 in later log but intermediate 13+ min not captured so physical epoch/stop UNKNOWN. NO new device action, YAML/flash/compile, TX response/mailbox/security implementation, telemetry/diagnostic change. Positive strictly offline phase classification, cause/owner/slot/Online INCONCLUSIVE. [V59 full report](V5DCM/V5DCM59_FRESH_APPROVAL_VS_RETAINED_SERVICE_EPOCH_CONTRAST_OFFLINE_RESULT_20261019.md).

# V5DCM58-FC16-ACK-0708-PROGRESSION-OFFLINE-01 — **COMPLETE / POSITIVE OFFLINE CONTROLLER-STATUS TIMELINE / UNIVERSAL ACK GATE NEGATIVE** (2026-10-19). Baseline user-installed V49 RX_ONLY HARD_DENY, 04A6/085F continue, FC16 ACK0, native 0708 poll0, 03E8 source0 after user-manual OFF/ON, clean postgap. Single controlled change: offline code-only corrected 8byte FC16 ACK frame classification (V57) + time-adjacent native FC16 request→ACK→0708 status poll/reply analysis on same existing 7 CRC-good capture files, no hardware or production YAML action. Sep25 local 090550 SHA256 f23cd2f18764d77220409d2cf9e0caf2fc3b7c1aa1d2a1405f13c9fdbbbc0e2d, 892 CRC frames, FC23=0 in excerpt: **32 0870/count17 FC16 requests/1 matching ACK**, status 0708 polls **17** before first reply, first 16 polls BEFORE first FC16 ACK66.860s, median poll period4202.5ms, successful status reply68.235s followed by first FC16 03E8/count13 68.304s and 31 unique settings groups through 06F1; later two 0708 polls101.901/106.095. After initial response 41 FC16 request/41 ACK envelopes. Cross-model Eco5 CRC-negative controls: 4 status poll+reply cases after FC16 request with **no ANY FC16 ACK nor FC23 envelope in-between**, request→poll host gaps1.266–1.427s (Sep26 three, Sep28 one). Therefore hypothetical universal per-FC16-ACK prerequisite for 0708 is **DISPROVEN / SUPERSEDED** as observed rule; a separate cold-init/approval/ACK gate remains HYPOTHESIS/OPEN. Original firmware is CM930 slave, cannot prove controller-master branch. Timing not UART EOF/response deadline. **No new controller test, TX, flash, build, Arm, 0708 sender or protected algorithm**; fail-closed V49, HA and sticky diagnostics preserved. [Full V58 report](V5DCM/V5DCM58_UNACKED_FC16_VERSUS_0708_CONTROLLER_PROGRESSION_OFFLINE_RESULT_20261019.md).

# V5DCM57-CM930-FC16-ACK-STATUS-SERVICE-OFFLINE-01 — **COMPLETE / POSITIVE OFFLINE ONLY** (2026-10-19). Hypothesis: original CM930 auto FC16 ACK != app H2/0867 request, and older private V55 classifier omitted 8-byte ACK shapes. Known-good running V49 RX-only HARD_DENY TX0, 03E8 source0 and native 0708 poll0, controller manual OFF/ON already historic. One controlled read-only action: inspected ORIGINAL 2.0.18/2.1.105 modbus_server15.py + bundled identical modbus_tk/modbus.py and modbus_rtu.py, executed 4/4 exact original CM930 receipt/version callback method-body host checks, reclassified same 7 archived 25,031/25,031 CRC-good captures. **4/4 PASS:** when first 0864 provides firmware version, 2.1.105 _on_registers_read loads profile and seeds required internal 33 mask, then on_registers_received_event credits THAT same 0864 group after seed; earlier 03E8 pre-WAIT not backfilled; 2.0.18 has no comparable tracker. Source: Modbus FC16 ACK generated by Modbus RTU server separately from asynchronously queued H2/info request and later controller-owned 0708 poll. Original RTU may suppress physical reply when new input pending; NOT proven live. **V55 parser interpretation FIX:** previous private classifier ignored 8-byte ACK geometry, but correctly validated CRC; V57 shows **1,365 CRC-valid FC16 ACK shapes**, **1,324 exact start/count pairs within 300ms** of 2,500 FC16 requests, with 41 unpaired ACK and1,176 unpaired request forms, host timing only; 300ms is purely analyst pairing horizon. Historic local XTR Sep25 071517 03E8 ACK2/2 and 0864 ACK4/4, Sep25 090209 04A6 ACK1/1 and 0864 ACK1/1; Eco5 Sep28 03E8 req211 ACK9 and 04A6 req226 ACK10; no causal or owner claims. Current V49 console native FC16 ackShape0, native 0708 poll0, hard-deny physical TX0, recurrent 04A6/085F. No new device action, source/YAML/compile/flash, protected response or 0708 mailbox tooling. Positive scoped source/host/archive only; XTR master ACK policy, current 03E8 missing cause, slot/owner/Online remain inconclusive. [V57 full report](V5DCM/V5DCM57_CM930_FC16_ACK_MAILBOX_EVENT_ORDER_OFFLINE_RESULT_20261019.md).

# V5DCM56-04A6-H0-MAILBOX-OBSERVABILITY-OFFLINE-01 — **COMPLETE / POSITIVE OFFLINE ORIGINAL SOURCE + CURRENT V49 LOGS ONLY** (2026-10-19). Single controlled action: extracted ORIGINAL _on_function16 and subsequent _set_handshake_state/on_handshake_state_changed_event/_request_info_data/on_registers_request_event/set_register_read_request/_register_and_bit_for_address/_set_data_package_bit methods from BOTH archived Thermia Connect 2.0.18+2.1.105 and ran IO-free host stubs with ORIGINAL equal-bytes flags JSON; validated current V49 original RX33 source and first/postgap ESP logs. **40/40** original-handler source tests across H0/RESPONSE_SENT/ACCEPTED, four starts per version; **8/8** additional original function-body full logical event-chain fixtures from H0: FC16 **04A6 or 03E8** -> internal H2 ACCEPTED -> WAITING_FOR_DEVICE_INFO version2151/0867 request -> original software mailbox W4=0x0100 at register1804; FC16 **04BA or 085F** excluded from H0 H2 transition and no W4 request. No prior FC23 necessary IN THIS ORIGINAL SOFTWARE BRANCH; native controller semantic acceptance does not follow. CRITICAL correction to V55 shorthand: **V49 RX33 W3/W4 are seen-page bitmaps**, not original mailbox W3/W4 request words! RX33 W3=0600 = observed 04A6/13+04BA/22; RX33 W4=0000 = no observed 0864/count4; never infer genuine DCM 1804 request bit state from them. Local V49 P74L showed 04A6/13 at 19:21:25.831 pre-OFF/ON and 19:38:15.845 follow-up; 0F FC16 source counters 606→851 then1985→2237. Both current native 0708 poll counters0 (96+96 independent S8R3 sensor samples, 38+39 Bridge04), HA 03E8 source count0 (19+20), physical UART TX0. A real original CM930 would need an initialized RTU/event service plus subsequent controller 0708 read and valid reply to deliver an internally queued version request; current V49 intentionally runs neither, and master behavior remains unknown. Current installed V49 unchanged RX-only; no flash/compile/TX/power cycle or security tool. Native acceptance/owner/EOF/slot/absence-root cause OPEN. **NEXT** offline evidence-gap/firmware-state boundary only; do not repeat native live tests or interpret RX33 bitmaps as outgoing DCM register contents. [Full V56 report](V5DCM/V5DCM56_04A6_H0_INFO_REQUEST_MASK_VS_RX33_OFFLINE_RESULT_20261019.md).

# V5DCM55-0867-03E8-0708-PHASE-CORRELATION-OFFLINE-01 — **COMPLETE / POSITIVE for offline metadata/capture source audit only** (2026-10-19). Hypothesis: distinguish native initialization, version discovery and request/service phases from existing raw bus envelopes, using original CM930 2.1.105 software as intended-app semantics authority. Baseline verified V49 output-disabled RX-only after user OFF/ON, current 03E8 page0, native status poll0; older V23 03E8/count14 in another session; historical V25 explicit group-request burst already DONE; Write 4.1 secondary. **One controlled read-only analysis:** CRC replay of 7 existing local XTR/ATEC/Eco5 captures: **25,031/25,031 valid frames**, **367** status poll/reply pairs <=300ms. **7/7** CRC FC23 reply-shaped episodes: first post-reply FC16 03E8 precedes first W4.bit8=1 status then first later FC16 0864 carrying 0867; first 0864 delayed 49.437–163.761s after 03E8 (host times, not EOF). Local XTR Sep25 071517: two FC16 03E8/count13 with W3.bit0=0 in **18/18** paired status replies, four 0864/count4, zero FC23 in segment. Local Sep25 090209: 0864/4 at50.828 with previous status W4.bit8=0 at50.031. Sep25 090550 historical explicit W3bit0→03E8/13 and 31 page groups already V25 (not repeated). Original firmware 2.1.105 reset_bit/tracker/profile gates reviewed, not fresh executable tests; actual collaborator modules may not run matching binary, W4bit8 can remain set after version page in ATEC. Exact private V49 header confirms 0864/count4 maps W4.bit8; **all 13 V49 RX33 snapshots W4=0000** across two distinct logs (duplicate follow-up counted once), W3=0200→0600, 03E8/14 absent, 0708 polls0 and TX HARD_DENY. **No** new device, source, YAML, compile, flash or TX; no confidential source published. **Positive** archive sequence and local counterexamples; **inconclusive** current physical sender/epoch/EOF/slot, actual 0867 profile, native acceptance/Online and why V49 lacks 03E8. Abort on CRC/faulted provenance, no recovery needed. [Full V55 report](V5DCM/V5DCM55_EXISTING_CAPTURE_VERSION_REQUEST_PAGE_CHRONOLOGY_OFFLINE_RESULT_20261019.md).

# V5DCM54-CM930-FIRMWARE-INFO-PROFILE-GATES-OFFLINE-01 — **COMPLETE / POSITIVE ORIGINAL-FIRMWARE HOST/SOURCE/PROFILE ONLY** (2026-10-19). Single controlled offline inspection of user-uploaded ORIGINAL 2.0.18+2.1.105 AppFS and original 2.1.105 930 versioned JSON, no production YAML/device alterations or native TX. Exact original _on_registers_read / on_handshake_state_changed_event / _request_info_data / InfoMessageCollector version/serial gates / CMClientParameterUpdateState and on_publish_cm_params_map_event executed with MOCK event/IO sinks: **40/40 PASS**. 2.1.105 first profile version callback calls _load_config_files, seeds INTERNAL 33 group received tracker, RETURNS; 2.0.18 corresponding callback loads+returns but NO tracker. Both have H2 info/OPERATION dispatch and 2151/0867 version extractor. Original tracker pre-WAIT receipt not counted, receipt of 03E8 group clears only its bit; in 2.1.105 param-map emission deferred if any other required group outstanding; no such explicit gate in 2.0.18. Raw ORIGINAL 2.1.105 profile: sensors.json99, configurations.json471 -> 541 unique numeric read/formula/condition/min/max/default refs -> 33 unambiguous required packages W2=15/W3=10/W4=8 verified by actual ORIGINAL _get_all_data_package_to_request/_register_and_bit_for_address methods; 1000/03E8 W3bit0, 2151/0867 W4bit8, distinguished from general request-all excluding W4bit8. No new XTR live evidence, write/ACK, firmware compile or Online. Source logic intended semantics != electrical bus proof; Write Beta v4.1 only historical corroboration. Known-good RX-only V49 preserved, EXP388 partial and V47 inconclusive untouched. [V54 full report](V5DCM/V5DCM54_FIRMWARE_FIRST_PROFILE_INFO_PACKAGE_GATES_OFFLINE_RESULT_20261019.md).

**V54 SAME OFFLINE EXPERIMENT — CROSS-MODEL CAPTURE CHECK ADDED:** CRC-good existing ATEC/DCM03 raw (SHA256 14918065297264473e2357822a8694d184e7821b8c2a3b1cb316039678a708a1) first FC23 t27.400, first source03E8/13 t29.262, first 085F/5 t61.529, first 0708 status poll t64.923, first 0864/4 (includes version0867) t86.672. **03E8 arrives 57.410s ahead of first version-bearing page.** This historical cross-model capture supports distinct physical bootstrap-before-later-profile stages, but does not reveal ATEC internal software tracker seed or current V49 status; no new controller or UART action. V54 original-source 40/40 and raw-profile 33 groups remain intact.

# V5DCM53-WRITE41-CM930-242-CONFIG-OFFLINE-01 — **COMPLETE / POSITIVE OFFLINE, no new local TX** (2026-10-19). Controlled one-source audit comparing pinned original historical Write Beta v4.1 YAML (Git blob 8e8a82689e53528a8b751a1abbd901f683b6b238, 9186 lines) with firmware-derived Connect 2.1.105 profile2.4.2 and live V49 RX-only pages, plus existing pinned 58-route matrix (2 approval,32 bootstrap ACK,1 legacy,1 runtime,18 status responders,4 desired). **15/15 STATIC code/route invariants PASS**, no compile/flash, no byte-level private responder published. v4.1 stage40 demands fresh FC16 ACK+status service, 03E8 current-only refresh before semantic write/optional startup autosync, authoritative 03E8/14 cache, exact republish and extraDeltaWords0, restart invalidation of stale page/queued intents. Historic statuses preserved: EXP386/387 COMPLETE/POSITIVE, EXP388 RUNNING/PARTIAL, EXP383 PREPARED/NOT RUN. v4.1 **32 controller bootstrap page starts** and successful Room Setpoint write do NOT establish full original 2.1.105 chosen XTR2.4.2 **33 significant application groups W2=15 W3=10 W4=8**, firmware info/profile version loading, onboarding or Online. Current V49 W3=0600 (04A6+04BA), no 03E8 or native status polls, TX HARD_DENY; older V23 RX-only 03E8/14 means absent TX not sole proven cause. Physical owner/EOF/slot/native acceptance remain UNKNOWN. No hardware operation. [V53 report](V5DCM/V5DCM53_WRITE41_CM930_242_CONFIG_LIFECYCLE_OFFLINE_RESULT_20261019.md).

# V5DCM52-V23-V49-03E8-PROFILE-OFFLINE-01 — **COMPLETE / POSITIVE OFFLINE SOURCE, HOST & ARCHIVED XTR REPLAY ONLY** (2026-10-19). Baseline V49 healthy RX-only/no native TX; prior V23 partial local 03E8/14 and local Sep25 V25 31-group transfer already established, no new live test. Controlled read-only source/capture cross-check. Original **2.0.18 flags JSON FOUND** at old package path and byte-identical to original 2.1.105 new path (3333B, SHA256 bb0b335eaf4e3a98e5d71d1cd1551e0772fedcfcd3f7d17f3c78e04c21844b9e): **V50/V51 '2018 flags absent' SUPERSEDED**. Actual stock profile coverage old2.3.0–2.4.1 vs new2.3.0–2.4.3, 2018 lacks 2.4.2+ info files; original resolver AST/host checks 5/5 PASS for 2.4.1/2.4.2/2.4.3/2.4.4 cases, site/OTA override unverified. Exact V49 V5DCM22 header maps W3bit0 03E8/14, bit9 04A6/13, bit10 04BA/22. Current first V49 before manual OFF/ON five snapshots W3=0200 fc23=0; after restart W3=0600 fc23=2 then 63 but never 03E8 or 0708 poll, wrongGeom0 and HA source03E8 count0. Older V23 2m25s first report W3=0001/03E8 count14 without FC23 in observed excerpt, TX hard deny, so passive no-TX by itself does not predict pages. Original older local Sep25 090550 892/892 CRC-valid frames; 137 slave0F, **zero native FC23 across entire 106.35s sample**, status poll68.210s→bit1803.0 reply68.235s→03E8/13 FC16 68.304s then 31 distinct requested groups; **already V5DCM25 locally investigated**, not a fresh physical test, not proven genuine DCM. Original capture count13 geometry not present modern count14. Native device owner/physical EOF/slot/accepted/C2/Online and 2026-10-19 absent-page root cause OPEN. No YAML, OTA, user controller cycle, bus TX, physical write or secret code. [V52 full offline report](V5DCM/V5DCM52_XTR_V23_V49_03E8_SOURCE_AND_PROFILE_RECONCILIATION_OFFLINE_20261019.md).

# V5DCM51-03E8-CONFIG-REQUEST-LIFECYCLE-OFFLINE-01 — **COMPLETE / POSITIVE (offline source/host + genuine cross-model archived captures only)** (2026-10-19). Single offline hypothesis: original CM930 request-group mechanism, initial settings-export and later request-bit-driven 03E8 refresh are distinguishable without native device TX. Verified last on-device RX-only V49 and V47 unresolved TX0 baselines. Original Connect 2.1.105 930/modbus-flags.json map dec1803/0x070B bit0→dec1000–1019/0x03E8–03FB; exact original request-group function **10/10 mapping PASS**, separate original set/reset received event host **1/1 PASS**, total11/11. 2.0.18 AppFS has request category source but no packaged 930 flags.json independently available. All 4 original profile ranges map registers1000/1001/1002 to heat curve/min/max, adjustments1003–1005, room desired1012; original method clears request bit based on first start address, not proof every word arrived. CRC re-evaluated exact genuine Eco5 Sep26/28/ATEC03 archives: 5/211/1 03E8 pages respectively (counts14/14/13), 183/81/65 =329 matched 6-word status reply/poll pairs, **3+5+0=8** bit0=1; every asserted-bit observation followed by new 03E8 within **62–662ms** (host time). All 7 FC23 reply-shaped envelopes also followed by first 03E8 **without intervening matching status poll**, after92–1833ms; later refreshes 92s/~480s after prior reply disprove fresh FC23 necessarily immediately precedes every page. No secret reply validated; no physical slot/owner inferred. Current V49 two user logs native 0708 polls0 and HA 03E8 count0 **already before manually induced controller OFF/ON**; old LOCAL V5DCM23 logged 03E8/count14 in a different XTR run. NaN heating curve/min/max indicate missing current ESP cache, not verified settings reset. No live test, compiles, physical TX or GitHub production YAML edits; TX HARD_DENY preserved. [Full V51 result](V5DCM/V5DCM51_03E8_CONFIG_REQUEST_LIFECYCLE_OFFLINE_RESULT_20261019.md). Next offline compare prior local XTR V5DCM23 03E8 presence vs current V49 absence without requesting any new power cycle or active response.

**V51 result reconciliation/addendum (no second experiment):** Before proposing any physical follow-up, verified earlier V5DCM25-REQUEST-CYCLE-01 already analyzed local experimental XTR raw Sep25 090550: status poll68.210s / 1803.bit0 asserted readback68.235s / FC16 03E8 count13 at68.304s, with 31 distinct settings request groups within ~33.69s. This is pre-existing local proof, not a newly performed test or genuine DCM provenance; separate V5DCM23 local RX-only sample already showed 03E8/count14. Hence the V51 **NEW** evidence is original exact-source11/11 and two-phase collaborator corroboration, not discovering XTR request-lifecycle for the first time. Future live repeat rejected; preserve V49 TX hard deny.

# V5DCM50-POSTGAP-PROVENANCE-PAGE-AUDIT-OFFLINE-01 — **COMPLETE / POSITIVE (offline source/metadata only; native owner/response INCONCLUSIVE/UNKNOWN)**, 2026-10-19. New user confirmation: manually switched Thermia OFF/ON to cause V49 previously reported 10,351ms callback gap (no physical supply-rail/end-of-wire measurement). One scoped read-only analysis of existing local V49 19:21–19:24 and duplicate 19:38–19:41 logs, exact archived V49 private YAML (unchanged), 2.0.18+2.1.105 original AppFS, and three genuine collaborator captures. First seven local native FC23 challenge-shape times yield 6 retry gaps 4.491,4.323,4.106,4.203,4.184,4.102s (median4.1935s); 63 cumulative requests stable in later log, no local reply or new output, retry-series end not captured. Genuine Eco5 99req+2rsp and 64req+4rsp; ATEC 1req+1rsp. Seven reply geometries followed by page03E8 in 92,92,93,482,465,124,1833ms host gaps (not electrical deadline or semantic accepted). Original CM930 v2.0.18 and v2.1.105 method `_on_function16` exact-source host executions 6/6 EACH pass: H0→H2 on ordinary FC16 without prior FC23, excluded service remains H0. Both firmware versions construct internal Modbus slave 0x0F; not real XTR electrical owner evidence. V49 source: `ha_restore_03e8` only populated by CRC-good slave0F FC16 start03E8 count13/14; `03E8 received=0` in 19 samples of FIRST file (including PRE-switch) and 20 of later. Heating settings NAN are unavailable due missing source; native capture PageStore separately cleared each FC23; 13 other settings words ≠ 03E8 evidence. V49 real RX terminal stays COMPLETE/POSITIVE only as passive; V47 LIVE remains COMPLETE/INCONCLUSIVE native TX0. No new actual bus experiment or YAML; transmission HARD DENY. Full [V50 offline report](V5DCM/V5DCM50_POSTGAP_PROVENANCE_PAGE_LIFECYCLE_OFFLINE_RESULT_20261019.md).

# V5DCM49-POST-GAP-COHORT-DEVICE-01 — **COMPLETE / POSITIVE, RX-only terminal on local XTR** (2026-10-19). Follow-up user uploads `Pasted text(20261019-174122).txt` and `Pasted text (2)(10).txt` are EXACT duplicates (one observation, not two), SHA256 `46241b6397071f66385c920a6ee155cc5d256c4f5f3390f9f0c0296737eb5971`, 5000 lines/19:38:02–19:41:15. V49 froze `RX_SHADOW_RECORDED reason=NONE gapMs=10351 oldResync=0 newFrames=285 batches=128 ageMs=30532 B11D_history=0 P5_history=0 TX=HARD_DENY OWNER=UNKNOWN`; 38 periodic sensor readouts unchanged across capture. Earlier 19:24 partial ended at 270 frames/29.091s; now >=30s and >=50 CRC-good frames verified. V5 parsed 12282→13898 with resync/drop/geometry0; B11C CRC mismatch0, B11D RAW=portable=V5 13840 at last 30s sample and firstFault NONE; FIX2 QUALIFIED/current1. Native 0x0F FC23 requests=63 at start AND end (no new requests), native responses0. Physical TX0, V44B build0 step7 deny1 carried from earlier denied Arm (no new click in this file), DE RX. `0x0F:03E8` page counter0/settings curve-min-max nan is a separate data-presence limitation. No physical owner/epoch/wire EOF/timing/slot/semantic Online confirmation. Current clean cohort does not test V47 orphan17/+17 B11D sticky case; V47 remains COMPLETE / INCONCLUSIVE for native one-shot. Next offline provenance/slot and settings-page audit, no new Arm or controller cycle. [Full local report](V5DCM/V5DCM49_POST_GAP_TERMINAL_RX_SHADOW_RECORDED_RESULT_20261019.md).

# V5DCM49-POST-GAP-COHORT-DEVICE-01 — **RUNNING / PARTIAL, positive RX-only post-gap stages** (2026-10-19). User second V49 ESP log SHA256 8a2da9ce5079c5008bec527ccac2720d3cc2acc9739f31668b26a9a568812dea, 5000 lines 19:21:15–19:24:27. Same deployed V49 observer, no new firmware change. One R6P24 callback gap **10351ms** at19:23:58.308; CRC-good slave1E return plus S02 0/5 coldPattern1, physical OFF/ON not user confirmed. V49 automatic `CLEAN_COHORT reason=NONE gapMs=10351 oldResync=0` at19:24:02 frames35 age4091ms→at19:24:27 frames270 batches124 age29091ms; **recorded 30s terminal NOT YET SHOWN**, wait one short status snapshot. V5 resync/drop0, B11D FIRST_FAULT NONE/parity0, B11C CRC0, FIX2 still QUALIFIED/current1; seven CRC-good native 0x0F FC23 challenge-shaped frames via GAP46C n1..7, P74E counts six at last sampling, owner/epoch/slot UNKNOWN. Operator tried V44B Arm19:24:01, **DENIED BUILD=RX_ONLY_HARD_DENY**, V44B step7 deny1 and UARTattempt0 DE RX; no physical TX. Historical V47 orphan17/+17 B11D fault remains distinct, not reproduced by current V49 gap. Native reply remains untested. Never force restart/re-Arm merely to get terminal snapshot. [Local report](V5DCM/V5DCM49_FIRST_REAL_POST_GAP_PARTIAL_20261019.md).

# V5DCM49-PASSIVE-BASELINE-01 — **COMPLETE / POSITIVE (local passive device)**, 2026-10-19. New user ESPHome log 3358 lines/132s SHA256 985c5a77fe79b14b7c1e4b1dff9b4e52f7f5e46cf6d908aac31fc5845ba6b4e1, 19:14:10–19:16:22. V49 source-family RUNNING `WAIT_GAP` 26/26; no gap recorded. FIX2 witness QUALIFIED/current1 from elapsedMs30383 through135384; parser frames92→1118 resync/drops/geometry0, B11C CRC0, B11D raw/portable/V5 match/fault0/First Fault NONE, native TX build0 UART writes0 Arm0 DE_RX1, normal HA telemetry. **V5DCM49-POST-GAP-COHORT-DEVICE-01 RUNNING / PARTIAL:** on-device new post-gap recovery not triggered by any >=5s callback gap; no post-gap positive/negative claim. No user controller restart, Arm or physical TX evidenced. No full ESPHome compilation/machine hash attested; no source change. Wait for future natural gap, no forced restart. [Result](V5DCM/V5DCM49_FIRST_DEVICE_PASSIVE_BASELINE_20261019.md).

# V5DCM49-POST-GAP-COHORT-OFFLINE-01 — **COMPLETE / POSITIVE OFFLINE SOURCE/HOST ONLY** (2026-10-19). Baseline user-installed V45 FIX2, V47 user-confirmed controller OFF/ON with B11D incomplete17, gap8972ms, resync +17, native FC23x8 and real TX0; V48 reproduced partial mechanism. Single controlled implementation new RX-only automatic post-gap RAW/V5 witness, plus safety lock removing hardware V42 TX build flags; no original B11D/P5/FIX2 semantics changed. Offline compiled exact V5 parser and original portable CRC/geometry helpers with 8/8 synthetic replay scenarios PASS (17 old resync excluded before clean anchor, >=50 new verified frames/35030ms, terminal historical freeze, rejects second gap/new resync/new CRC fault/output/unfinished partial/expiry). YAML parsed, diagnostics ID added, no colliding IDs, 65 original FIX2 files byte-identical and package 69 files/one YAML/manifest and ZIP CRC pass. Private ZIP SHA256 62afe39629102a3daa06f09eab3ed159f44437d702fb8d3904c61e62e2a85630. No full ESPHome compile, flash, manual Arm, power cycle, active TX. **V5DCM49-POST-GAP-COHORT-DEVICE-01 PREPARED / NOT RUN**; no unnecessary controller reboot; WAIT_GAP until future natural gap. [Result](V5DCM/V5DCM49_RX_ONLY_POST_GAP_COHORT_OFFLINE_RESULT_20261019.md).

# V5DCM48-B11D-PARTIAL-GAP-SOURCE-01 — **COMPLETE / POSITIVE OFFLINE SOURCE/REPLAY ONLY** (2026-10-19). Baseline V47 user-confirmed controller OFF/ON after accepted Arm; V47 LIVE remains COMPLETE/INCONCLUSIVE native TX0. Controlled change = host-only tests and read-only exact FIX2 YAML/adapter/guard audit; no new flash, reboot, Arm or response. V47 B11D 17:55:09.662 fault after bounded 250ms defer: raw44 cursor27 expected1/len27 residual17, candidates35 and64 require more; last RX callback independently derived ~17:55:09.371/373, R6P24 callback gap8972ms at17:55:18.343. V5 parser first return resync 5→22 (+17), native 0x0F FC23 exact frames8 after restart, V44B FaultedRx/DE_LOW and UART0. Exact literal V5 inline parser compiled and replayed with *synthetic* 27+17 prefix plus clean ADUs -> exact +17 resync and CRC-good RX recovery; original candidate_lengths compiled with helper sources -> {35,64} as logged; exact FIX2 header compiled -> B11D true faults deny and even with hypothetical healthy B11D, +17 resync revokes independently. All C++17 host cases PASS; no on-wire bytes/physical EOF attributed. Strongest hypothesis controller power interruption orphaned prefix, not proof of electrical cut mid-frame. Timeout bump/clear latch **not** a safe fix; preserve B11D/P5 and no TX. [Evidence](V5DCM/V5DCM48_B11D_250MS_PARTIAL_GAP_SOURCE_REPLAY_RESULT_20261019.md).

# V5DCM47-LIVE-ONE-SHOT-01 — PROVENANCE FOLLOW-UP (2026-10-19): USER CONFIRMED manually turning the Thermia controller OFF and then ON after accepted Arm, during the already-reported V47 live scope. Previous "physical cycle not confirmed" limitation superseded, exact switch times and electrical epoch/owner still unknown. B11D FIRST_FAULT 17:55:09.662, callback gap 8972ms 17:55:18.343, eight exact native 0x0F FC23 from 17:55:19 onward, 0 native TX, V44B FaultedRx safety cutoff remain as recorded. Preserve classification **COMPLETE / INCONCLUSIVE for native reply**; no second execution, no status upgrade to native acceptance. Next offline B11D incomplete-frame source analysis, no repeat power cycling. [Amended live result](V5DCM/V5DCM47_FIRST_LIVE_ONE_SHOT_INTEGRITY_DENIAL_20261019.md).

# V5DCM47-LIVE-ONE-SHOT-01 — **COMPLETE / INCONCLUSIVE for one-shot native response** (2026-10-19), local actual Arm + returned exact-frame observations. `USER_ARM_ACCEPTED` 17:54:59.174; original B11D RAW_INCOMPLETE_TIMEOUT_250MS first fault 17:55:09.662 while Armed; 8972ms RX gap at 17:55:18.343; V5 resync 5->22 (+17), current FIX2 becomes irreversibly REVOKED. 8 CRC-complete parsed canonical 0x0F FC23 via GAP46C exact frame logs n=1..8 after return. V44B `step=7 deny=5` = Revoked/FaultedRx original private enum, replyAttempts0 uartAttempt0 admitted0 DE_RX1 and no real TX; no controller semantic answer or Online evidence. Scope was user-initiated, physical controller switch exact time not independently provided. Historical Oct18 V5DCM32 likewise failed B11D around controller restart; repeated mechanism warrants OFFLINE diagnosis before another live test, not brute-force reboots. [V47 result](V5DCM/V5DCM47_FIRST_LIVE_ONE_SHOT_INTEGRITY_DENIAL_20261019.md).

# V5DCM47-PASSIVE-PREFLIGHT-01 **COMPLETE / POSITIVE — LOCAL PASSIVE ONLY** (2026-10-19). Same startup session extended to 3257 lines 17:16:13.850–17:18:19.457: FIX2 QUALIFYING→QUALIFIED at witness elapsedMs30628, 21 following QUALIFIED samples, last frames1110 at elapsedMs130628 current1. Original parser frames96→1112 resync5 unchanged all 13 samples; B11C CRC0 B11D parity/fault0 First Fault NONE, DE RX, no Arm or native FC23/TX. Initial resync5 (+5) at valid0 caused persistent P5_HISTORY1 (not reset); exact V44B Arm source uses separate CURRENT RX witness, not legacy P5 latch. Native V47-LIVE-ONE-SHOT-01 remains PREPARED / NOT RUN, rollback output-disabled V44B. [Local result](V5DCM/V5DCM47_EXTENDED_PASSIVE_PREFLIGHT_RESULT_20261019.md).

# V5DCM47-PASSIVE-PREFLIGHT-01 — **RUNNING / PARTIAL**, 2026-10-19. New local XTR log 423 lines ~14.7s shows FIX2 QUALIFYING current0 (frames89→175, elapsed10.6→20.6s); 5 pre-existing parser resyncs unchanged between 17:16:15/25, P5_HISTORY1, Bridge02 RX Integrity Faults1, B11D first fault NONE/sticky0, DE RX, V44B step0 armClicks0/uartAttempt0, native FC23 zero; normal HA telemetry. Too brief to prove 30s QUALIFIED. One-shot TX V47-LIVE-ONE-SHOT-01 remains PREPARED / NOT RUN, no Arm or controller cycle. Requested next 60–90s passive continuation before any buttons. [Record](V5DCM/V5DCM47_FIRST_PASSIVE_STARTUP_PREFLIGHT_PARTIAL_20261019.md).

# V5DCM47-RX-GAP-HOST-01 — COMPLETE / POSITIVE offline host checks (2026-10-19): exact private FIX2 FreshRx source, 19/19 compiled strict C++17 assertions. 12s simulated no-callback controller gap: current false while phase remains QUALIFIED; new healthy frame restores current. New RX drop or B11D readiness loss still permanently revokes. Source-reviewed one-shot Arm 30s and single reply 70ms after callback; exact physical EOF/restart not tested. V5DCM47-LIVE-ONE-SHOT-01 PREPARED / NOT RUN: at most one user-initiated controlled controller return and one fresh validated native slave 0x0F FC23 response; no flash, Arm, real controller restart or TX by this V47 step. [Details](V5DCM/V5DCM47_COLD_REJOIN_ONE_SHOT_PREFLIGHT_20261019.md).

# V5DCM46-TRIGGER-H0-H2-OFFLINE-01 — **COMPLETE / POSITIVE (OFFLINE only)**, 2026-10-19. One read-only intervention: directly execute isolated original Connect 2.1.105 CM930 FC16 handler with stub state/event (7/7 PASS), source equality AppFS/device_client, recross-check latest 4580-line FIX2 local log (36 qualifier snapshots, 18 P74E snapshots all FC23=0, 36 one-shot Arm/UART=0, 18 clean parser samples) and compare documentary G01-09 local controller restart FC23 burst (24 cumulative). Original firmware H0->H2 on ordinary FC16 without FC23 is possible internally; reference Core H1->H2 restriction is deliberate fail-closed simplification, not identical vendor semantics. No live test, no XTR native response; NEXT native trigger/owner remains OPEN. [Result](V5DCM/V5DCM46_CONTROLLER_TRIGGER_AND_CM930_H0_H2_OFFLINE_RESULT_20261019.md).

# V5DCM45-FIX2-LIVE-RX-01 — **COMPLETE / POSITIVE PASSIVE LOCAL XTR** (2026-10-19). [Evidence](V5DCM/V5DCM45_FIX2_FIRST_LIVE_PASSIVE_RX_RESULT_20261019.md). FIX2 installed by user; one controlled change from FIX1: readiness-aware current RX witness instead of false REVOKED during B11D startup. Raw ESPHome API file Pasted text(20261019-142332).txt 178.8s SHA256 856d5da48c7870d54b151f022fcdc6837fb6f92ea24ef5818e2e9ad0b555a7f2. QUALIFYING->QUALIFIED at witness elapsedMs30762/262 frames, retained QUALIFIED to elapsedMs185763/1582 frames. V5 frames98->1549; resync,drops,geometry,unknown 0, B11C crcMismatch0, B11D raw=portable/first fault NONE. No Arm, no UART TX, physical output0, DE RX. P74E native FC16=251 FC23=0; owner/epoch/slot unknown. Native physical one-shot still PREPARED / NOT RUN; don't conflate RX qualification with TX/native semantic acceptance. Rollback V44B no-TX; no controller reboot, scan or write during observation.

# 2026-10-19 V5DCM45-FIX1 local first passive: RUNNING / PARTIAL; no native TX. 1912-line log ~73s shows phase=REVOKED throughout, frames94→687 resync/drops/geometry/unknown zero, B11D first fault NONE, P5_HISTORY=0, DE=0, armClicks=0, replyAttempts=0, native FC23=0. Suspected startup-order bug: guard observes before b11d_started becomes true. Separate FIX2 source candidate PREPARED / NOT RUN; retain previous FIX1 offline POSITIVE independently. [Evidence](V5DCM/V5DCM45_FIX1_FIRST_PASSIVE_STARTUP_REVOKE_20261019.md).

# V5DCM45-FIX1-RECOVERY-01 — **COMPLETE / POSITIVE OFFLINE SOURCE/HOST ONLY**, [independent result](V5DCM/V5DCM45_FIX1_INDEPENDENT_RECOVERY_RESULT_20261019.md). Reconstructed from exact uploaded V45 after last chat export ended mid-response. Separate ZIP SHA256 `fd004cf1aa0edf2adbe6569a56cf453e1401bf0010378e4e5107aa40c894f067`; not earlier FIX1. Fresh RX witness 30s/100 frames, <=3s age, permanent new-fault revoke, P5/B11D history preserved, denied preflight Arm does not consume sole accepted attempt, private backend unchanged. 57/57 C++17 guard checks plus YAML/entity/manifest tests PASS. No compiler/flash/native TX; PREPARED / NOT RUN; no new local XTR result.

---

# V5DCM45-FIX1-FRESH-RX-SOURCE-01 — **COMPLETE / POSITIVE OFFLINE ONLY**, [PREPARED](V5DCM/V5DCM45_FIX1_FRESH_RX_PREPARED_20261019.md) / [RESULT](V5DCM/V5DCM45_FIX1_FRESH_RX_OFFLINE_RESULT_20261019.md). Hypothesis: current stable RX can qualify a bounded manual reply while historical startup P5 latch is preserved. Baseline last user-running V45, source V45 original; existing history P5=1, resync7 unchanged over 195.6s, DE0, no UART/Arm, no native local challenge. **Single code change:** add separate current RX witness with 30s+100 newly validated frames, current frame age<=3s, new RX fault revokes; use in V44B Arm/tick/current-request/B11D-owned DE check, preserving original historical P5 and B11D diagnostics; preflight-denied click not counted as accepted one-shot. Offline 56/56 new FIX1 witness+click tests, 40/40 prior V45 B11D fake-IDF and 32/32 V44B fake UART; YAML original HA IDs/API/OTA/UART exact, private native backend unchanged. Full private package SHA256 `7f130635c5b8ef59f3cba9b17afd229b7afd5ee67856d1281300331ec5496791`; one YAML sha256 `37f295903aa92e2efa9b57a2a08d44acabb2572020aa81d35bcba795290df4fc`; clean ZIP extraction verified. **No real ESPHome compile, flash, Arm or native TX.** Next: user compile, separate on-device fresh qualification log before user-initiated physical one-shot. Native handshake and Online remain UNKNOWN. Historical V45 passive RUNNING/PARTIAL preserved.

---

# V5DCM45 FIRST USER LIVE LOG — **RUNNING / PARTIAL (PASSIVE), first on-wire native response PREPARED / NOT RUN**. [Evidence and source-level analysis](V5DCM/V5DCM45_FIRST_LIVE_PASSIVE_P5_ARM_GATE_20261019.md). Known-good baseline V44B user RX/HA PASS (200 s, build0), compiled/installed V45 TX-capable source by logs build1. One controlled observation: user 195.6-second device capture with no button presses or active TX (`Pasted text(20261019-123601).txt`, 5,000 lines SHA256 `768825d91e8f35b37d8fd3a6e0fdacc3b8fecac1ef344b9cb1b9afca0e288eea`). Parser 798→2416 frames, 7 preexisting resync constant, drops0, B11C and B11D no new faults, DE0, old/new TX0, HA values live. V45 `build=1` but `P5_history=1`, R6 P5 `FAULT_LATCHED`. **Source finding:** R6-P5 latches fault on any nonzero cumulative resync; V44B one-shot user-arm checks P5 clear, and first denied Arm consumes only permissible click. **DO NOT PRESS ARM YET**, no local native 0x0F FC23 request (`FC16=390 FC23=0`). This is not a negative result for physical reply because no attempt occurred. Next PREPARED offline hypothesis: preserve historical P5/B11D fault history while distinguishing current RX-clean interval, validate no new RX errors and guarantee immediate Abort; first user physical TX and semantic acceptance still NOT RUN. Rollback verified V44B compile-only (no TX) / FIX-B2/FIX2. Original V45 offline result COMPLETE / POSITIVE stays separate.

---

# V5DCM45-B11D-TX-OVERLAP-SOURCE-01 — **COMPLETE / POSITIVE OFFLINE SOURCE/HOST/FAKE-IDF ONLY** [PREPARED](V5DCM/V5DCM45_TX_AWARE_B11D_ONE_SHOT_PREPARED_20261019.md) / [RESULT](V5DCM/V5DCM45_TX_AWARE_B11D_ONE_SHOT_OFFLINE_RESULT_20261019.md). **Hypothesis:** exact B11D 50ms original sticky DE-high guard can be reconciled with one bounded actively owned native reply without clearing faults. Known-good baseline user-flashed V44B no-TX last 200.41s local positive RX/HA, native approval FC23 zero; V43/44B host 7/7 historical parity, V44-A physical denial-only partially documented, FIX-B2/FIX2 fallback. **One offline controlled change:** private V45 TX-capable source from pinned V44B complete ZIP, two V42 compile enables ON, adds pure read-only DE ownership check to existing V44B UART actor and original 50ms B11D branch, two diagnostic globals and one diagnostic text, other parser/production remains. B11D now pauses only when current actively entered TX, port GPIO21+ESPHome switch high, one attempt, same boot and fresh <70ms, no RX fault/peer conflict; otherwise original sticky B11D fault and Abort. User button Arm30s, exact CRC-valid canonical `0x0F FC23 read0730/8 write071C/8`, one reply no retry, 70ms callback-relative. Candidate one YAML SHA256 `428cb1e087d7e35d7bc806afca57ca36e8425ba6c7ed1dd2980587b5034d5941`, private single ZIP SHA256 `b77e4f20b64aa8503f2c5889f6e308678af4d4dd04e4a0e52391f1cf36363df5` (65 entries 64 verified digests), full existing 117 sensor/13 binary/11 buttons/50 text entity IDs unchanged plus new text (51 total), UART and OTA/API untouched. **Executed:** V45 strict fake-IDF 40/40 DE/Abort/expiry/stale/legacy/collision/switch-GPIO scenarios; original V44B fake-IDF 32/32; real historical DCM cross-model 7/7 matches, independently checked synthetic 256/256 and invalid CRC 32/32; fresh ZIP extract host suite pass. **No actual compiler**, no new flash, user Arm, UART wire/DE electrical, local XTR response, C2 or Online. Current frame/payload/CRC unknown until controller-origin challenge; do not claim prepared static outgoing frame. Negative case would be unowned DE accepted, retry, CRC incorrect, source/HA change, fault erased; none in offline tests. Actual physical timing/epoch/slot UNKNOWN and not assumed proven. **Next:** user compile single full candidate, then separate manually initiated first one-response physical trial with Abort and V44B/FIX-B2 recovery. V44-A RUNNING/PARTIAL historically preserved.

---

# V5DCM44-B COMPILE-ONLY POST-FLASH RX/HA — **COMPLETE / POSITIVE, PASSIVE ON DEVICE**. [Earlier user compile+flash partial](V5DCM/V5DCM44B_COMPILE_ONLY_USER_COMPILE_FLASH_PARTIAL_20261019.md) → [complete runtime RESULT](V5DCM/V5DCM44B_COMPILE_ONLY_POSTFLASH_RX_RESULT_20261019.md). Hypothesis: newly flashed output-disabled V44B preserves original V5/B11C/B11D/P5 and HA with no physical UART/DE. Known-good input original V43-FIX1 and FIX-B2; user flashed no-TX V44B, binary hash unknown. **Only intervention:** 200.41-second passive recording (user log `Pasted text(20261019-115204).txt`, 5,000 lines, SHA256 `6e0e80c33d2bdef3614a039bedb5a351a6016ea04f1a3888de911637fad63626`); no HA Arm, no power-cycle, no frame injected, no flash during capture. Parser 2130→3753, pages 348→611, bad geometry/resync/drops=0; B11C CRC checked 2306→3579 mismatch0; B11D raw=portable 3589/3589 fault0/DE0; new V44B build0/armClicks0/replyAttempts0/uartAttempt0/admitted0/DE_RX1/conflicts0 over 40 snapshots. Old UART Write Calls0 and Physical TX Attempts0, HA readings responsive. **Positive** on-device RX/HA and fail-closed software TX; no negative safety criterion observed. **Native TX/handshake NOT RUN:** current local 0x0F FC23=0, no owner/epoch/slot/wire-EOF or physical DE waveform; real native C2/Online open. **Next:** offline fix of 50ms B11D DE-high sentinel vs bounded genuine TX; stop/rollback future TX if new sticky RX fault or failed RX return; preserve original B11D/P5 history, FIX-B2/FIX2 and current user V44B no-TX. G01–G06 historical accepted risk not to be relitigated. Older V44-A button test remains RUNNING / PARTIAL as historical result.

---

# V5DCM44-B COMPILE-ONLY first user flash — **RUNNING / PARTIAL** [record](V5DCM/V5DCM44B_COMPILE_ONLY_USER_COMPILE_FLASH_PARTIAL_20261019.md); user has confirmed actual ESPHome build and flashing of single ZIP/YAML. Source archive SHA256 `c504934004331f3b3e44b1163a24a4c052d208e7a4aa0555a0158b1f9b1b1295` and YAML SHA256 `2b54ef5211bf0bbafe167803cf1401a9a7127177ae4c305263775c21aef40d9b` verified separately, binary/OTA hash unknown. This is a **passive runtime validation**; user press/Tx NOT requested. Original V42 double guard still false (both defines absent), new V44B Arm cannot send; unconditional `TX-ELIGIBLE BUILD` startup text misleading. Expected unchanged B11C/B11D, 0 DE/TX, HA working; 2–3 minute post-flash log required before COMPLETE. First report not a native success. B11D 50ms DE-high sentinel future TX conflict still OPEN; maintain last known-good FIX-B2/FIX2 and V43 rollback.

---

# V5DCM44-B — **COMPLETE / POSITIVE SOURCE/HOST ONLY**, [PREPARED](V5DCM/V5DCM44B_SINGLE_RESPONSE_SOURCE_PREPARED_20261019.md) / [RESULT](V5DCM/V5DCM44B_SINGLE_RESPONSE_SOURCE_RESULT_20261019.md); V44-B compile-only preflight **COMPLETE / POSITIVE for source validation only** [finding](V5DCM/V5DCM44B_COMPILE_PREFLIGHT_HOLD_20261019.md), actual compiler NOT RUN. One controlled change: nonsecret V44B overlay generated from exact private user V43 FIX1 (ZIP pin `2bda32cc2efa92678ca9f9a6f615134e430884552ecabdcec667ba57f830ba47`) adds manual 30-second one-response native reply scope, fake/optional UART FIFO, 70ms after-callback ceiling, existing DE switch, original 1s watchdog exemption only during an active frame; **32/32** fake-IDF four-build/eight-case scenarios pass. No local native 0x0F FC23 challenge in user logs; no physical TX. Additional single controlled source-check change now generates an otherwise-identical **compile-only** YAML with both TX build flags removed: YAML SHA256 `2b54ef5211bf0bbafe167803cf1401a9a7127177ae4c305263775c21aef40d9b`, 117/13/50/11 source entities, clean-regeneration audit, no ESPHome compiler/flash. **Blocker discovered:** original RX-only 50ms B11D DE-high check could latch a permanent fault during an intentionally high DE native response; old 1s watchdog mitigation insufficient. Do NOT flash TX-enabled source; fix with future narrowly scoped TX-aware integrity provenance, preserving sticky fault history. V44-A [RESULT](V5DCM/V5DCM44A_ARM_ABORT_RESULT_20261019.md): RUNNING / PARTIAL; actual two denied Arms, Abort and 0 TX positive, step7 latch intended, post-20s untested. Original V43 running device unchanged. NEXT Mac-side compile-only ESPhome config+compile, then B11D reconciliation and separately staged real one-response experiment with abort/recovery.

---

# V5DCM44-A — **PREPARED / NOT RUN**, [PREPARED contract](V5DCM/V5DCM44A_ARM_ABORT_DENIAL_LIVE_PREPARED_20261019.md). Hypothesis: the actual V43 FIX1 HA Configuration Arm and Abort callbacks register a one-use denial, while old B11C/B11D integrity, DE LOW and UART Write Calls=0 remain intact. Known-good last user V43 passive RX 1150 frames/0 faults, V43 TX HARD_DENY build=0 and old executor 0 real attempts, FIX-B2/FIX2 rollback; prior V40/41/42 host only. One controlled intervention: user one Arm click, 5-second wait, one Abort click, collect before/after ~20s logs, no flash/reset/forced handshake/native output. Positive criteria button event/denial evidence, 0 TX/DE/RX faults; negative any send or RX loss; inconclusive missing event proof. Await user execution/results before RESULT or COMPLETE.

---

# V5DCM43-PRIVATE-ESPHOME-INTEGRATION-OFFLINE-01 — **COMPLETE / POSITIVE SOURCE/HOST/FAKE-IDF; LIVE NOT RUN**. Linked [PREPARED](V5DCM/V5DCM43_PRIVATE_ESPHOME_INTEGRATION_PREPARED_20261019.md) / [RESULT](V5DCM/V5DCM43_PRIVATE_ESPHOME_INTEGRATION_RESULT_20261019.md). **Hypothesis:** integrate one private native ESP32 dynamic backend, bounded V42 one-shot TX actor and HA Arm/Abort using exact verified original B2 YAML, never altering UART owner, original B11C/B11D/P5, DE-switch bookkeeping, HA entities or production hard locks. Baseline user FIX-B2 last 204s on-device RX/HA stable, software 393/393 HARD_DENY/UART0, FIX2 fallback; historic V4.1 EXP386/387 positive, EXP388 partial, V5DCM32 integrity-negative, V40 7/7 cross-model crypto parity, V42 source-only positive. **One source-only controlled addition:** 3 new private headers, exact original parser callback tap, 2 Configuration HA buttons and 1 diagnostic text in generated YAML. B2 ZIP/YAML SHA pinned, new YAML SHA256 `959bc5cee094715e3475263207736146bc146ff48760619df4d8020f9939991c`; original 117 sensor/13 binary/48 text/7 buttons identities and original ESPHome single UART+GPIO21 switch, original RX code preserved. **Executed:** 7/7 genuine historical cross-model reply matches; 256 independent Python/C++ synthetic pairs; 32 invalid CRC deny; V42 six source host builds/run; four fake ESP-IDF borrowed UART/ESPHome GPIO-switch builds/run; YAML parse/full entity diff; 75-file private archive SHA256 `c74f9105d66d21b2a37b5204434953375a7036431f2997b8aeb3df8df223e745`, ZIP CRC/74 SHA entries verified and clean runner exit0. **Positive offline:** source and mock state only. **Negative guards held:** current physical owner/epoch/slot flags intentionally false, timing qualification false, absent dual hardware-build flags means Arm DENIED and no UART/DE TX. **NOT RUN:** actual ESPHome/ESP-IDF compilation, flashing, new ESP32 firmware, live user HA presses, transceiver measurements, actual current XTR response or semantic C2/Online acceptance. Risks and future effect: future canonical FC23 native private reply only if independently scoped; no arbitrary settings FC16 write, current value unknown. Abort current experiment by discarding source, running B2 untouched; future first TX max one, DE/RX fallback, sticky history, FIX-B2/FIX2 rollback. **Next:** separately source-compile and qualify physical/test-readiness before one live TX; do not promote host-only results to live.

---

# V5DCM42-BOUNDED-TX-BOUNDARY-OFFLINE-01 — **COMPLETE / POSITIVE (SOURCE/HOST/FAKE-IDF ONLY)**, linked [PREPARED](V5DCM/V5DCM42_BOUNDED_TX_BOUNDARY_OFFLINE_PREPARED_20261019.md) / [RESULT](V5DCM/V5DCM42_BOUNDED_TX_BOUNDARY_OFFLINE_RESULT_20261019.md). Hypothesis: source-only optional one-response physical TX state machine can preserve B2 production hard locks while proving a bounded, fault-aborting RX→DE-high→FIFO→drain→RX transaction in a mock port. Baseline user installed FIX-B2 last 204 s healthy RX/HA, 393/393 HARD_DENY, UART0, safe RX-only FIX2 rollback. V4.1 EXP386/387 guarded local positives, EXP388 partial; V5DCM32 rejoin negative; V41 dynamic source oracle positive host only. **One change:** separate private 15-member V42 actor/optional borrowed ESP-IDF adapter plus tests, no B2 YAML/production edit. Incoming target 0x0F FC23 canonical firmware/capture metadata, reply generic 0x0F FC23 16-byte dynamic/CRC **not generated on-device in V42**, no arbitrary register write/current value/retry, host timings artificial not qualified for bus. Actual strict results: 6 C++17 builds PASS (449×3 default/single deny and 460×3 both-switch fake enabled), 4096/4096 V39 frame-shape parity PASS, 4 fake-IDF stub builds PASS, 460 ASan/UBSan PASS, original ZIP/YAML/output lock checked. New ZIP SHA256 `a6906c78887e6a8e376fecbb7209a2bc72cf7ad2b47798e4b52dedfa67ebb53b`, 14 SHA member manifest entries, full clean-extract rerun exit0. Negative guards: no arm unless both build switches + valid boot/scope/timing, replay rejected, wrong frame/CRC, peer, owner/slot/epoch, B11D/P5, clock, FIFO faults and mid-send revocation → RX. **NOT RUN:** ESPHome compile, existing RX callback integration, native ESP32 crypto backend, GPIO/DE electrical or real UART drain, HA Configuration controls, actual XTR first response/Online. Physical live trial still PREPARED / NOT RUN and *not flash-ready*; next is reviewed source integration and private exact current response CRC/timing/abort/rollback under standing user-approved G01–G06 risks. No flash/controller restart/ARM/TX performed.

---

# V5DCM41-PRIVATE-DYNAMIC-REFERENCE-BACKEND-OFFLINE-01 — **COMPLETE / POSITIVE (executed HOST/SOURCE only)** [PREPARED](V5DCM/V5DCM41_PRIVATE_DYNAMIC_REFERENCE_BACKEND_PREPARED_20261019.md) → [RESULT](V5DCM/V5DCM41_PRIVATE_DYNAMIC_REFERENCE_BACKEND_RESULT_20261019.md). Hypothesis: exact source-pinned, externally executed genuine-reference callback can provide a per-request dynamic answer to the unmodified V39 private BoundProvider, and host-only mock stays one-use/hard-denied on production platforms. Baseline user XTR FIX-B2 last 204s passive healthy, HARD_DENY 393/393 UART0, fallback FIX2; preceding V40 seven genuine cross-model crypto pairs positive; V4.1 EXP386/387 local guarded positive, EXP388 partial, V5DCM32 rejoin negative. **One controlled change OFFLINE:** standalone 9-file nonflashable C++17/Python adapter + tests, no installed code/YAML, no real TX/target current value/physical reply timing. 7/7 real historical Eco5/ATEC+DCM03 capture responses exact; 256 novel synthetic challenges dynamic same-reference matched (NOT independent crypto oracle); **427 host negative/control assertions** including 8 deliberately wrong-crypto CRC-valid responses that V39 structurally accepts and external oracle catches (limitation), source tamper, forbidden live API compiler negative, embedded/default output deny, session faults and CRC/geometry denial. Private parent V39/B2/YAML pins checked and unchanged, existing source headers byte-identical. ZIP SHA256 `8596434e26d90172d5d4eb930b49981e86020910dfe6d21e57ac16dc385382cb`, all 8 manifest hashes + ZIP CRC pass, clean extract full runner exit 0; original source reference/key remains EXTERNAL and never published. No live user result/ARM/flash/controller restart/real response. Oct03 collaborator ATEC not local XTR; Sep25 model unknown. Physical owner/epoch/slot/controller acceptance/semantic registers/app C2/Online still UNKNOWN; no fabricated completion. Abort = discard offline addition on failed pin; original B2 untouched. **NEXT** V42 separate private controlled live-readiness preflight and actual bounded hardware trial only after fully scoped user-initiation, validated exact private frame/CRC/current controller state/limits/abort/FIX2 recovery.

---

# V5DCM40-GENUINE-DCM-HISTORICAL-PARITY-01 — **COMPLETE / POSITIVE (OFFLINE REFERENCE / GENUINE CROSS-MODEL CAPTURES ONLY)**. [PREPARED](V5DCM/V5DCM40_HISTORICAL_CRYPTO_PARITY_PREPARED_20261019.md) and [RESULT](V5DCM/V5DCM40_HISTORICAL_CRYPTO_PARITY_RESULT_20261019.md). Hypothesis: already-existing firmware-derived reference validates genuine captured native response, and V39 can consume independently documented exact historical frames under host mock fail-closed. Baseline user-installed FIX-B2 204s passive RX/HA healthy, HARD_DENY 393/393 UART=0, fallback FIX2; V4.1 EXP386/387 positive, EXP388 partial, V5DCM32 B11D rejoin negative, prior V39 host positive. One controlled change **offline**: exact pinned source+capture corpus test and recorded-pair-only private V39 host regression; no outgoing native frame/current setting value/CRC/time/retry live. Executed: original external firmware reference blob `2aeb56f3afb60414f0527acd6960996219a0b0fb`, genuine Eco5 Sept26 2/2, Sept28 4/4, Oct03 collaborator ATEC+DCM03 1/1 **7/7 byte-exact**; 21/21 negative controls; 184/184 V39 historical mock host assertions, V39 2926/2926, V38 318/318, vendor Python handler 256 stubbed, embedded/default DENY; private 8-file ZIP SHA256 `dbe134f3a11826c7beb3177d16bfa44d90f925711c78bba373845fab78a06be7`, SHA/ZIP verified, fresh runner exit 0. Source dependency/exact original captures provided privately at runtime; ZIP has no secret algorithm/key/real response fixture. **Material provenance correction:** Oct03 capture is **collaborator ATEC/DCM03**, not local XTR; Sep25 model provenance unresolved. CRC and old count geometry facts retained but local XTR promotion retracted. **OPEN:** live local XTR owner/epoch/response slot, native application handshake, dynamic on-device backend, C2/Online, B2 postgap >90sec. No physical TX/flash/ARM/restart; abort/recover = discard host addition, device unchanged; future test must privately define exact response/CRC, timing/max-one attempt/risks/abort/FIX2 rollback.

---

# V5DCM39-REQUEST-BOUND-REFERENCE-01 — **COMPLETE / POSITIVE for OFFLINE source/host input binding only** (2026-10-19). Linked [PREPARED](V5DCM/V5DCM39_REQUEST_BOUND_BACKEND_PREPARED_20261019.md) / [RESULT](V5DCM/V5DCM39_REQUEST_BOUND_BACKEND_RESULT_20261019.md). **Hypothesis:** the missing actual native FC23 request payload in V38 metadata-only `Request` can be safely bound to a one-shot out-of-tree backend while independently comparing real Connect source handler's input selection and state (with crypto stub), and embedded output remains impossible. **Known-good baseline:** user FIX-B2 last 204s positive RX/HA, TX HARD_DENY 393/393 UART=0, fallback FIX2, exact B2 ZIP+YAML hashes. Relevant prior V4.1 EXP386/387 positive, EXP388 partial, V5DCM32 B11D-gated live negative, V38 mock positive. **One change:** separate 11-file NONFLASHABLE C++17 request-bound source+host test archive; no YAML/runtime/UART change, no native outgoing frame/payload/CRC or target write/current value/real reply timing. **POSITIVE:** 2,926/2,926 new strict host tests, 318/318 original V38; 256 synthetic inputs through exact original vendor handler with fake crypto; full CRC/size/profile negative guards, original B11D/P5 and boot/scope/owner/epoch flags denied if missing; host default/ESP_PLATFORM/ARDUINO output DENY, forbidden sender compilation rejected, ZIP 10 SHA-manifest entries/CRC and fresh-extracted full runner exit 0. Package SHA256 `35195716ec530ee512776e9bd6aba3a3780bcf0635edc0554d6745f6e11ebada` private only. **Not executed:** genuine ARM xxtea/reference cipher parity, ESPHome compile/flash, physical native response, user ARM/restart/semantic write, actual owner/slot/epoch/current profile C2/Online. **No live negative claim** from stub crypto. Abort: discard source bundle on pin/test failure, running FIX-B2 unaffected. **Next:** verify confidential cryptographic response against genuine firmware/reference before separately specified one-attempt user-initiated hardware trial.

---

# V5DCM38-PRIVATE-RESPONSE-PROVIDER-OFFLINE-01 — **COMPLETE / POSITIVE (SOURCE/HOST ONLY, 2026-10-19)**. [PREPARED](V5DCM/V5DCM38_PRIVATE_RESPONSE_PROVIDER_PREPARED_20261019.md) → [RESULT](V5DCM/V5DCM38_PRIVATE_RESPONSE_PROVIDER_RESULT_20261019.md). Hypothesis: a distinct fail-closed private provider interface can gate one CRC/geometry-qualified native 0x0F FC23 request, externally provided owner/epoch/slot, abstract confidential reply and simulated delivery without promoting model output to physical DCM acceptance. Known-good user FIX-B2 204s RX health, HA preserved, 393/393 HARD_DENY, UART=0, rollback FIX2; historical V4.1 EXP386/387 positive, EXP388 partial, V5DCM32 live rejoin negative, V37 offline positive. One source-only change: new 8-file host-only private provider ZIP; no YAML/firmware changes. **318/318** strict C++17 host checks PASS; separate ESP_PLATFORM mock-delivery DENIED with zero calls, bytes wiped; unauthorized live-sender API compile negative as expected; exact source ZIP/YAML/Core/output pins and zero-IO symbol audit PASS; final archive SHA256 `9e28f3ed2ae3bf95f79b69c2b72eebf5d228bd306147285aa906a73400be6767`, manifest/ZIP verified, clean re-extracted runner exit 0. Negative fixtures include stale/foreign/gap, sticky B11D/P5, missing source/owner/epoch/slot, competing response, corrupt reply and replay; all fail closed. No output payload, outgoing CRC, register-value change, retry or actual TX in this host-only scope; actual proprietary backend NOT INCLUDED; all controller acceptance/Online/C2 unknown. Abort on failed source/test; no device rollback required. **NEXT:** privately implement independently checked vendor reply backend with reference provenance and only afterward prepare one separate user-initiated bounded hardware trial.

---

# 2026-10-19 V5DCM37-REPRODUCED-OFFLINE-01 — RESULT COMPLETE / POSITIVE (NEW OFFLINE RECONSTRUCTION, NOT NEW LIVE XTR).

Existing V5DCM37-COMBINED-DCM-OFFLINE-01 prior COMPLETE / POSITIVE and reported 1017 checks remain in the preceding original result. Its exact old ZIP was absent from this runtime. [New separate result](V5DCM/V5DCM37_REPRODUCED_ARCHIVE_VERIFICATION_20261019.md).

Hypothesis: one stand-alone no-output research source coordinator can combine already verified synthetic native FC23/mock/FC16 logic, separate retained/recovery observations, source/generation/sequence/timing and original B11D/P5 fail-closed, 33 exact profile-shape census, and pinned FIX-B2 structural Core + deny-only output. Baseline user-flashed B2 latest 204-second PASSIVE COMPLETE/POSITIVE and known-good FIX2 rollback. One controlled change OFFLINE only: rebuilt model, independent tests and reproducible ZIP. No physical address/write payload/current setting/retry or TX intended.

Actually executed: new 11507/11507 g++ C++17 host PASS; V35 192+18, V36 53, original B2 65, 70/70 historical source fixtures, FIX-A 52+32, V31 61, V32 34 PASS; original four captures 23472/23472 CRC-good; 3 forbidden-compilation negatives and 1 tampered B2 ZIP rejected. Initial compiler warning and historical-shadow expiry test failure were fixed before declaring pass. Initial repeated-build test runner timed out and was NOT classified complete; optimized full runner exited 0, fresh extracted ZIP full runner exited 0. ZIP 19 members, 18 SHA manifest entries verified, SHA256 f94b6cccf9982df79b3eecf21693f1a4e1b82a9e6429c82effa5987dc6eafc19.

Positive = bounded host/model/capture integrity and intentional 0 TX; negative checks appropriately denied. Unknown = physical native DCM reply and current bus owner/slot/epoch, real app C2/Online, device flash hash and live B2 post-gap terminal observation. Abort/recovery irrelevant to hardware because no device was touched; retain user running FIX-B2 and sticky B11D/P5. No protected algorithms or private 0x0F output committed.

---

# V5DCM37-SOURCE-CAPTURE-SPOTCHECK-20261019 — **COMPLETE / POSITIVE (offline only)**. Linked [exact report](V5DCM/V5DCM37_SOURCE_CAPTURE_SPOTCHECK_RESULT_20261019.md). Hypothesis: pinned original B2 RX33 source and four original history logs reproduce the exact modern 33 geometry and fail-closed observer without claiming authority. Baseline FIX-B2 last user live 204s PASS/HARD_DENY UART=0, fallback V5DCM23 FIX2; prior combined V37 source+host pass reports preserved. **One change:** separate host-only six-file test/archive; parent firmware/YAML untouched. **Positive:** strict actual B2 passive witness compilation/tests **113/113**, private ZIP/YAML/header SHA pins, CRC **23,472/23,472** valid, four historical shape census XTR Oct03 **31/33**, Sep25 **24/33**, collaborator Eco5 Sep26/Sep28 **33/33** entire logs each, modified legacy lengths 03E8/13 + 0410/21 excluded from modern 14/22. Archive SHA256 `050b98fe4b1dbd25d8a613ae2cf84ce74b80acb102fc68d06958aa48ecd3d55e`, re-extracted and rerun exit 0. **No native TX/CRC outgoing/port provider/current controller handshake**, no live tests, no new protocol acceptance. Negative source guards: duplicate, foreign, malformed, CRC/integrity faulty, stale continuity, FC23 boundary all denied; no Online/owner/epoch/C2. Abort on source pin/test failure and discard offline addition, original live device unaffected. **Unknown next:** independent actual physical response owner/slot/epoch and accepted dynamic vendor reply in a future separately user-initiated privately scoped test.

---

# 2026-10-19 — V5DCM37-COMBINED-DCM-OFFLINE-01 **COMPLETE / POSITIVE (original reported); independent reproducer COMPLETE / POSITIVE (new executed HOST ONLY)**. This supplements, not rewrites, the prior V37 PREPARED/RESULT entry below. New 23-file nonflashable archive SHA256 879ffcd03a7b4fe0198ef09077fbb0356f3222603a63d7c882a62e70e78d886c actually created and SHA-manifest/ZIP-verified; default runner from clean extract **exit 0**, independently **2,848/2,848 strict C++17** combined five-axis tests (A FC23→mock→first 03E8/count14 internal-only shadow; B distinct fresh/retained/recovery 085F candidates only; C boot/generation/stale/integrity/conflict/B11D/P5 revocation; D exact 33-group private B2 source start+count 15/10/8, no C2/Online promotion; E V35/V36 pins and zero output), prior source host V36 53, V35 192+18, 3 compilation negatives, 1 mutated parent rejection PASS. Four archived local/cross-model logs CRC **23,472/23,472**: XTR Oct03 31/33 modern shapes (15/8/8, legacy first count13), XTR Sep25 24/33, Eco5 Sep26 and Sep28 whole-log 33/33 (cross-model). **Original B2 full legacy regression optional follow-on timed out**; only first 65-check B2 shadow PASSED before timeout; previous V36/original V37 logs contain completed historical tests; do NOT falsely report them newly executed in this recovery. Independent recovered archive differs from the original V37 ZIP; original recorded 1,017 tests & ZIP SHA f656... not byte-reverified here. Exact parent B2 ZIP SHA fdc09c... and YAML SHA 32e1b7... VERIFIED unchanged. No outgoing slave/page/register/payload/CRC/timing, native TX, firmware flash, controller restart, ARM or original B11D/P5 reset; actual user FIX-B2 remains last proven known-good 204sec passive. **RESULT COMPLETE / POSITIVE OFFLINE for new suite; no native DCM controller acceptance or current session proven**. [Reproduction and precise provenance](V5DCM/V5DCM37_INDEPENDENT_REPRODUCTION_RESULT_20261019.md).

---

# V5DCM37-COMBINED-DCM-OFFLINE-01 — **RESULT COMPLETE / POSITIVE (SOURCE/HOST/CAPTURE ONLY)** 2026-10-19. Linked [PREPARED](V5DCM/V5DCM37_COMBINED_DCM_OFFLINE_PREPARED_20261019.md) and [FULL RESULT](V5DCM/V5DCM37_COMBINED_DCM_OFFLINE_RESULT_20261019.md). **Hypothesis** combine five separately testable native DCM evidence axes under one nonflashable, zero-output coordinator while keeping current FIX-B2, original B11C/D/P5 and all HA/TX paths unchanged: canonical native FC23→mock delivery→first modern FC16 internal shadow, path-specific fresh vs retained/recovery observation, generation/source/integrity/slot-synthetic fault denial, exact original modern 33 W2/W3/W4 significant selector geometry, pinned actual private B2 Core/no-output interface. **Known-good baseline:** user-flashed FIX-B2 204s live PASS (B11D=2342,B11C=2345 matched, HA readable, UART writes=0, executor 393/393 HARD_DENY); verified source parent SHA256 fdc09c5927b5a351163db95db96dc467abd43cb27e1e7fc8068782bea4a677c7, YAML SHA256 32e1b7c3ea4f7411fb94d6d769370b9ae10874403961403002250b96e4365d46; rollback FIX2. Earlier V5DCM35/36 host positive, V4.1 EXP386/387 historical local positive, EXP388 partial, V5DCM32 controller restart negative B11D first fault before gap. **ONE controlled change OFFLINE ONLY:** standalone coordinator/test harness and sanitized historical replay; user ESP/YAML/Core source unchanged, NO output payload or target slave/register value, outgoing CRC, response timing/retries or physical TX. **POSITIVE tested:** g++ C++17 -O2 -Wall -Wextra -Werror -pedantic **1017/1017 V37 assertions PASS**; B2 SHA/deny **34/34 PASS** and tampered source ZIP explicitly rejected; compiled V36 B2 Core 53/53+three expected-negative compiler rejects, V35 192+18, original B2 65, historical XTR 70/70, FIX-A 52, stream 32, V5DCM31 61, V5DCM32 34+34 ALL PASS. Four original raw logs 23472 CRC-good/0 bad; Oct03 local XTR whole recording **31/33** matched modern shapes, the two missing exact forms 03E8/count14 and 0410/count22, older lengths present; Sep25 old XTR 24/33; Eco5 peer 33/33 each over full recordings, NOT current XTR or single authenticated session/Online. **NEGATIVE CONTROLS:** wrong-count13/22, 32/33, duplicate, CRC fault, foreign generation/boot, responder conflict, expired synthetic slot, mocked failed delivery, legacy B11D/P5 faults, unverified parser, source tamper all denied; model structural authority never actual owner/epoch/delivery/TX/C2/Online. Initial long combined runner timed out during repeated build (NOT protocol negative); rerun optimized and completed exit=0, plus independently extracted ZIP clean run exit=0. **Archive** private/nonflashable 21 files SHA256 f656c09082f6077b84db216570666a96a097ad85e676a9d693efee2e47f8974f, each ZIP member verified. **INCONCLUSIVE/OPEN:** physical vendor reply/slot/epoch/controller acceptance, B2 >90s gap on-device, full original V5DCM18 Python reference seven-fixture replay, current modern XTR 33/33 C2, Online. **Safety:** no controller restart/ARM/flash/native TX, no live register write or HA entity change; no rollback needed. **NEXT** private output-provider design and discrete later user-initiated live test only after exact privately scoped frame/current value/risk/timing/retries/abort/rollback. 

---

# V5DCM36-PINNED-CORE-OUTPUT-PROVIDER-OFFLINE-01 — **COMPLETE / POSITIVE OFFLINE** 2026-10-19. Linked [PREPARED contract](V5DCM/V5DCM36_PINNED_CORE_OUTPUT_PROVIDER_OFFLINE_PREPARED_20261019.md), [RESULT](V5DCM/V5DCM36_PINNED_CORE_OUTPUT_PROVIDER_OFFLINE_RESULT_20261019.md). **Hypothesis** exactly source-pinned private FIX-B2 mutable ticketed Core can be inspected on a copy, with an absent/deny-only output provider and fail-closed default adapter irrespective constructor bool, rejecting version drift from latest public firmware HEAD. **Baseline** user-flashed B2 204s live RX PASS, TX HARD_DENY; original ZIP SHA256 fdc09c5927b5a351163db95db96dc467abd43cb27e1e7fc8068782bea4a677c7, old FIX2 fallback; earlier V5DCM35 mock delivery host PASS; V4.1 EXP386/387 positives, EXP388 partial, V5DCM32 restart rejoin negative remains. **ONE source-only change:** separate NONFLASHABLE offline `v5dcm36_pinned_core_output_boundary.hpp` source probe copies real Core and returns sanitized structural/no-authority evidence; provider always `DeniedNoOutputProvider`; no protected reply algorithm, outgoing bytes/CRC, UART/DE, register writes, user YAML changes or physical device actions. **Targets** passive already CRC-validated 0x0F/FC16 page metadata 03E8/count14; NO TX address, payload, CRC, timing or retries, NO current setting write. **Positive observed test:** original ZIP/YAML and private four Core/adapter/platform Git blobs exact, 15/15 guards; compiled actual private B2 Core/adapter/platform **53/53** host asserts PASS, 0 mock platform writes and output flag false despite constructor true; three negative compiler tests independently fail for intended reason; tampered baseline ZIP rejected; V35 192+18 regression PASS; unchanged original B2 suite 65+70 local historical fixtures CRC-valid+52+32+61+34+34 PASS. **Source finding** upstream HEAD adapter constructor defaults output_enabled=true/public platform accept versus user B2 production forced false/private unleased accept. Private B2 mutable classifier, HEAD pure const API incompatible; neither side proves controller acceptance. **User supplied no new live result**; status COMPLETE only for OFFLINE experiment. **Abort triggers** production source altered, unleased TX becomes possible, host macro device escape or protected publication; none met in this host audit. **Inconclusive/open physical:** current slot, electrical DE, native dynamic response, 33 significant app pages, Online, B2 post-gap >90sec. **Next:** V5DCM37 offline provider/ownership design, controlled hazards; no autonomous user device operation. Archive private 16 files SHA256 9eefe9e7452f01267277b742d83e1a9b9b54dfb1e2b42d1bdbf93d83a48d948a. 

---

# V5DCM35-NATIVE-APPROVAL-BOUNDARY-OFFLINE-01 — **RESULT COMPLETE / POSITIVE (OFFLINE ONLY)** 2026-10-19, matched existing [PREPARED contract](V5DCM/V5DCM35_NATIVE_APPROVAL_BOUNDARY_OFFLINE_PREPARED_20261019.md). **Hypothesis** isolated existing CRC/geometry-validated native 0x0F FC23 diagnostic intent→mock delivery→later matching FC16 can correctly distinguish observation, synthetic local delivery and firmware-internal ACCEPTED_SHADOW without physical owner/epoch/TX/C2/Online promotion. **Verified baseline:** user-flashed-family FIX-B2 latest live 204s COMPLETE/POSITIVE B11C/B11D stable/HARD_DENY; unchanged exact ZIP SHA fdc09c5927b5a351163db95db96dc467abd43cb27e1e7fc8068782bea4a677c7, YAML SHA 32e1b7c3ea4f7411fb94d6d769370b9ae10874403961403002250b96e4365d46; known-good rollback FIX2. Previous V5DCM34 audit POSITIVE; historical V4.1 EXP386/387 POSITIVE, EXP388 PARTIAL; V5DCM32 live rejoin NEGATIVE integrity-latched before gap. **One controlled change:** new PRIVATE standalone C++17 offline mock model only, NO production YAML, incoming UART path, GPIO/DE, native output or device action. **Exact target:** passive 0x0F canonical FC23 and first fresh FC16 03E8/count14 metadata; no outgoing slave/register/payload/CRC, no physical TX timing or current register value. **POSITIVE actual tests:** 192/192 hostile/ordering/duplicate/CRC/fragment/foreign/epoch/expiry/mock-ticket/legacy-shape C++17 tests, 18/18 source-pinned real B2 private Core differential assertions, 4/4 immutable source/output checks; earlier B2/B11D/V5DCM31/32 host suites 65 +70 capture-valid+52+32+61+34+34 PASS. 4 captures independent standard Modbus CRC: XTR Oct03 2687/2687, XTR Sep25 892/892, Eco5 Sep26 10719/10719, Eco5 Sep28 9174/9174 = **23472 CRC-valid/0 CRC-bad**, only metadata output. **KEY NEGATIVE CONTROL** old Oct03 XTR FC23→reply-shaped (29ms)→03E8/count13 (~1.862s) is NOT modern B2 03E8/count14, and Sep25 no canonical start; Eco5 count14 is cross-model, no sender/slot proof. Private B2 Core can internally classify 03E8/count14 'authorized' while handshake NotAccepted; that is not physical TX authority. **NEGATIVE live triggers/abort:** would include accidental UART/DE, fault bypass/sticky reset, protected publication — NONE because no device touched. **INCONCLUSIVE/OPEN:** actual native response, controller acceptance, full original Python 7-fixture replay, retained/recovery, physical DE, 33/33 C2 and Online. No ESPHome compile/flash. ZIP private not flashable SHA e672cbcb8fe630011982579687cbe33cd6652c732f0b9e13c14f7406b017c70b. **Next after reviewed offline result:** reconcile Core APIs and plan separately scoped private physical delivery seam before considering user-initiated active TX; do NOT auto ARM/reset/restart. [Complete report](V5DCM/V5DCM35_NATIVE_APPROVAL_BOUNDARY_OFFLINE_RESULT_20261019.md).

---

# V5DCM34-CM930-V41-FIXB2-NATIVE-GAP-AUDIT-01 — **COMPLETE / POSITIVE OFFLINE AUDIT ONLY** (2026-10-19); next V5DCM35-NATIVE-APPROVAL-BOUNDARY-OFFLINE-01 **PREPARED / NOT RUN**. Hypothesis: compare original firmware 2.1.105 AppFS CM930 and actual historically successful V4.1 EXP386/387/partial EXP388 against user-flashed-family FIX-B2 actual YAML/header and latest 204s passive logs to isolate smallest native session integration blocker, without new parser, real TX, controller restart or unknown payload. Known-good FIX-B2-LIVE-PASSIVE-01 COMPLETE/POSITIVE and fallback FIX2; earlier FIX-B post-gap shadow scoped POSITIVE, prior V5DCM32 manual fresh rejoin NEGATIVE after B11D first fault before gap. One controlled offline source-review and 21 structural/log assertions: **21/21 PASS**, original CM930 3/3 selected modules `device_client.zip` == extracted 2.1.105 AppFS byte-for-byte; original v4.1 YAML GH blob SHA 8e8a82689e53528a8b751a1abbd901f683b6b238 with bounded stage40 cold guard, recovery and delayed service paths. FIX-B2 private shadow terminal historical RX evidence has kMayQualifySession=false/kTxAllowed=false; original V5DCM32 on-frame path separately ARMed, V5DCM23 ledger boot selected or one-shot friend-only reselect; **no B2→ledger/session authority join**, current native 0x0F FC23=0 1/33 0 local generation and HARD_DENY. Firmware-original handshake internal Accepted after qualifying FC16 distinct from actual response-delivery/physical owner; 33 significant W2/W3/W4 packages distinct from cold 32/32 and semantic writes. GitHub HEAD `xtr_core.hpp` blob 3d172fe134f127e9d19c5ad48d863da9a87741bc, `.cpp` 5c345d76f967103ffb58109b1e1742370e09658a, are NOT exact private B2 Core blobs 63874043da0845d603b7da1ef81db403011bd063 / 1ddb6cced68ef4571e650852913cad392e35e734; version drift must be reconciled before code integration. Positive: concrete exact-source handoff and bounded first gap; no new live DCM proof. Negative controls: no speculative retroactive owner/epoch, 1/33 NOT C2, V4.1 fixed R1 not general. Inconclusive/unproven physical owner/slot/current epoch, genuine native acceptance, Online, original full Python reference seven-fixture corpus. Abort/recovery: source audit only; no user device change, preserve prior FIX-B2. **V5DCM35 PREPARED**: one mock-delivery source harness, no outgoing payload, strict deny/regression review before any separate active user-initiated test. [Result](V5DCM/V5DCM34_CM930_V41_FIXB2_NATIVE_GAP_AUDIT_20261019.md) [Next contract](V5DCM/V5DCM35_NATIVE_APPROVAL_BOUNDARY_OFFLINE_PREPARED_20261019.md).

---

# V5DCM33-FIX-B2-LIVE-PASSIVE-01 — **COMPLETE / POSITIVE, XTR USER-FLASHED RX-ONLY BASELINE** 2026-10-19. Hypothesis source-only B2 terminal RX witness modification leaves existing UART parser B11C/B11D, HA production telemetry and software TX blocking unchanged *while unarmed*. Known-good user-live FIX-B baseline COMPLETE/POSITIVE; FIX-B post-gap clean RX COMPLETE/POSITIVE with distinct timeout-retention COMPLETE/NEGATIVE; B2 offline qualified-evidence hold COMPLETE/POSITIVE; fallback V5DCM23 FIX2 RX-only. One controlled deployment change: user flashed B2 using historically named YAML in final ZIP; no scope ARM, no controller restart, no other HA/physical changes. **Observed** seven `[V5DCM33-FIX-B2]` runtime diagnostic rows, all `DORMANT reason=NONE gaps=0 frames=0 batches=0 TX=HARD_DENY`. Complete 5000-line user log 00:17:40–00:21:04, 371306 bytes SHA256 f00ceb663f17138b2efb57f7bc424ae3187991cc26b138e45aad6aefa136b9e7. B11D raw/portable/V5 2342/2342/2342, mismatch/boundary/overflow/incomplete/hold/fault all 0, First Fault NONE; B11C 2345/2345, countDiff=byteDiff=resync=drops=fault=0, independent public CRC 2316 checked 0 mismatch; V5 frames 800→2417, pages 129→392 zero geometry/parser resync/drops; HA room/DHW/supply values updating, some other sensors NaN not claimed resolved. TX hard deny 393/393, software physical attempts=0, UART writes=0, software DE=0; electrical DE unmeasured. Target passive existing 0x02/0x0A/0x1E/0x0F, no outgoing slave/page/register/CRC/payload. 0x0F FC16 130→393, FC23=0, V5DCM23 1/33, V5DCM32 step=0 localGen=0 epoch/owner/C2/Online unproven, no new native session. **Positive** all predefined passive safety/RX criteria; negative triggers absent; inconclusive only for separately untested qualified-hold >90s, exact flashed binary hash/physical pin levels and DCM emulation. No abort; rollback known-good FIX2 on future credible regressions. **Next** offline historical CM930/V4.1↔V5 native integration gap review, optionally separately scoped B2 post-gap test; NO ARM/restart in this passive result. [Full evidence](V5DCM/V5DCM33_FIX_B2_FIRST_LIVE_PASSIVE_RESULT_20261019.md).

---

# 2026-10-19 — V5DCM33-FIX-B2-LIVE-PASSIVE-01 **PREPARED / NOT RUN**; **FLASH USER-CONFIRMED, RUNTIME NOT YET VERIFIED**. User responded “ja” to explicitly confirming the installed file `waveshare-thermia_V5DCM23_REAL_LEDGER_PREPARED_NOT_FLASHED.yaml` was taken from final FIX-B2 ZIP, distinct from the earlier FIX-B candidate. Baseline FIX-B live passive COMPLETE / POSITIVE and post-gap COMPLETE / POSITIVE (transient independent RX), FIX-B timeout retention COMPLETE / NEGATIVE, B2 source/host remedy COMPLETE / POSITIVE; exact firmware binary hash unverified. Hypothesis candidate B2 additive terminal historical RX witness leaves ongoing HA, B11C/B11D, V5 parser, UART/DE safety unchanged when unarmed. **One controlled deployment change**: user-reported flash of B2 source; do not infer any on-device execution result until logs. Target passive traffic already present (0x02/0x0A/0x1E/0x0F), NO slave/page/register writes, NO TX frame, NO physical controller intervention. Positive: 60–90 s normal ESPHome log with FIX-B2 marker DORMANT, stable B11C/B11D equal counts no CRC/resync/drop faults, HA telemetry, HARD_DENY with zero UART writes/software TX attempts/DE=0. Negative: credible regression / unplanned TX/DE; inconclusive: missing runtime marker, too-short log or ambiguous source. Abort on new heat-pump faults, HA drop, RX corruption or unexpected output; recover to known-good RX-only FIX2 if necessary. **Await log**; no ARM, reflash or controller power cycle requested.

---

# V5DCM33-FIX-B2-QUALIFIED-HOLD-OFFLINE-01 — **COMPLETE / POSITIVE (OFFLINE ONLY)** 2026-10-19; **V5DCM33-FIX-B2-LIVE-PASSIVE-01 PREPARED / NOT RUN**. Hypothesis one bounded source-only change can freeze successful independent post-gap CRC/V5 RX_SHADOW_ONLY cohort as historical evidence, preventing subsequent ARM+90s WINDOW_EXPIRED revocation, without modifying original B11D/P5 fault holds or native TX. Verified known-good source baseline exact private FIX-B SHA256 1753e92590237e9685f74d8c9d80ca64064cb73e5151d56dcdfc38cbc0769cde, earlier FIX-B-POST-GAP-01 COMPLETE/POSITIVE live transient 348 frames and separate timeout-retention COMPLETE/NEGATIVE 23:46:38.439. ONE controlled lifecycle change: `v5dcm33b_post_gap_raw_shadow.hpp` makes qualified status terminal, no further frame processing, freezes age/batches/frames, preserves against Cancel; maintains pre-qualification 90s/CRC/fragment/buffer/unexpected-gap/output-safety hard failure. Two host tests adjusted; original YAML only 2 log marker strings changed to `[V5DCM33-FIX-B2]` and comments. Baseline **red** test `s.snapshot(91010u).phase==QualifiedReadOnly` fails on FIX-B; **green** on FIX-B2: 65 source assertions, 70/70 original local captured CRC fixtures (61 recorded before bound qualification), old FIX-A 52+32, V5DCM31 61, V5DCM32 34+34 all pass. YAML strict semantic equivalence (24 blocks/44 includes, original 117 sensors/13 binary/48 text, 7 buttons/1 switch), UART native write/DE expressions unchanged, 72 previous bundle files intact except shadow, 2 tests, YAML; new private complete 75-member ZIP SHA256 fdc09c5927b5a351163db95db96dc467abd43cb27e1e7fc8068782bea4a677c7; integrity and manifest verified. **No native target slave/page/register/write payload/CRC or TX timing**; TX HARD_DENY and original RX/HA maintained by source, not live-proven for B2. Full ESPHome compile/flash/physical test/ARM/controller restart NOT RUN. POSITIVE for host source criterion only; future live consistency UNKNOWN. Next user-initiated flash optionally then unarmed PASSIVE log 60–90s, abort new B11D/B11C faults/HA issues/TX attempts or software DE; roll back to verified RX-only FIX2. [Evidence + reproducibility](V5DCM/V5DCM33_FIX_B2_QUALIFIED_HOLD_OFFLINE_RESULT_20261019.md).

---

# V5DCM33-FIX-B-POST-GAP-01 — **COMPLETE / POSITIVE for prepared RX-only qualification** (2026-10-18). One documented ARM and new >=5s callback gap, not active TX. Original PREPARED criteria: accepted manual FIX-B ARM 23:45:04.356; R6-P24 11.888s gap at 23:45:20.888 and CRC return 0x1E; >=30s and 50 independently CRC/V5-parity-good RAW frames to RX_SHADOW_ONLY inside 90s. All MET: 23:45:58.453 RX_SHADOW_ONLY reason=NONE frames=348 batches=168 gap=1; 23:46:01.266 confirmed marker with ageMs=40376 frames=374/180 and HARD_DENY; 23:46:31.266 638/291 still qualified. No B11D sticky fault, B11D 17574 RAW=portable=V5 fault/hold/CRC diff=0, B11C 17594/17594 diff=0, parser resync/drop=0, HA reads live; TX executor HARD_DENY 2897/2897 attempts=0, UART writes=0, software DE low. Native 0x0F FC23 reaches 27 requests; V5DCM32 step=0 localGen=0, legacy profile 0/0, P5 UNQUALIFIED; no DCM owner/epoch/Online or physical voltage proof. **SEPARATE NEGATIVE SUB-RESULT FIX-B-QUALIFIED-TIMEOUT-RETENTION COMPLETE / NEGATIVE:** after prior success, at 23:46:38.439 observer changes to FAULT_NO_RELEASE/WINDOW_EXPIRED 668/303 due to original source `check()` applying arm+90000ms after qualification; it destroys qualified status *without CRC or bus fault*. Host test gap identified (no qual-then-expire regression); no live repeat. Source log 4999 lines 23:44:01–23:47:15 SHA256 8903b3707a91fdb63a56b29faa96badf8798b0fb96449670b21877a065a03753, earlier overlapping partial snapshot preserved. Next FIX-B2-POST-QUALIFIED-HOLD **PREPARED / NOT RUN OFFLINE**: one lifecycle policy correction, qualified outcome stays immutable evidence and resources bounded, original B11D/P5 and all no-TX defenses unchanged; fail-closed source and host regression before any user flash. No automatic controller restart/ARM. [Complete result](V5DCM/V5DCM33_FIX_B_POST_GAP_01_COMPLETE_RESULT_20261018.md).

---

# V5DCM33-FIX-B-POST-GAP-01 — **RUNNING / PARTIAL (LIVE EXECUTION)** 2026-10-18. Hypothesis new R6-P24 >=5s callback gap after FIX-B manual arm permits RX_SHADOW_ONLY after >=30s and 50 new CRC+V5 parity-good frames, with historical B11D/P5 holds and HARD_DENY retained. Known-good FIX-B first passive live COMPLETE/POSITIVE and earlier V5DCM32 manual rejoin COMPLETE/NEGATIVE. One controlled action actual accepted FIX-B Configuration ARM (23:45:04.356) followed by observed 11888ms callback interruption (23:45:20.888); user actual physical switch times not separately supplied. First CRC return slave 0x1E; observed coldPattern A80E=0000 A80F=0005; four native 0x0F FC23 request boundaries later, no 0x0F TX or owner. Shadow WAIT_GAP then CLEAN_WINDOW: at 23:45:28 frames=64 batches=34; 23:45:31 frames=98 batches=47 ageMs=10376, fault=NONE gap=1, no historical B11D. Primary B11D 16764 equal RAW/portable/V5, fault=0; B11C 16785 equal portable/V5, fault=0; parser resync/drop 0; HA readings continue. Original V5DCM32 remains step=0 localGen=0, portable 1/33 revoked into 0/0 after FC23 context; HARD_DENY all 2736 candidates, software physical attempts=0, DE=0, UART writes=0. Supplied 5000-line log 23:42:14–23:45:36 SHA256 5eb5bd6f1c9c82ffc9fc0d721a3defdabe1633e6d638492fbd4677b0f81862ac ends ~15s after gap return, before mandatory 30s; **NOT YET POSITIVE OR NEGATIVE**, no RX_SHADOW_ONLY/fault visible. Abort on HA/CRC/TX/alarm, no resets/re-arm; gather only 23:45:45–23:46:40 continuation or later FIX-B status and actual physical restart/alarm confirmation, then classify result. No new test or write pending. [Evidence](V5DCM/V5DCM33_FIX_B_POST_GAP_01_PARTIAL_RESULT_20261018.md).

---

# V5DCM33-FIX-B-POST-GAP-01 — **PREPARED / NOT RUN** 2026-10-18. Hypothesis one new >=5s R6-P24 callback gap after manually armed FIX-B can yield independent RAW CRC/byte-parity shadow after >=30s/50 frames without releasing B11D/P5 historical faults or native session/TX. Baseline FIX-B-LIVE-PASSIVE-01 COMPLETE/POSITIVE: B11D 5617/5617, B11C 5637/5637, parser resync/drops=0, HA live, TX HARD_DENY physical attempts=0, FIX-B dormant. Prior V5DCM32 manually restarted rejoin COMPLETE/NEGATIVE, pre-gap B11D RAW_INCOMPLETE_AT_IDLE and 12.923s callback gap, no local generation. One controlled user action: press only FIX-B passive ARM Configuration once then one safe previously used controller restart, no ESP reboot/no other YAML/HA knob changes/no TX. **Precondition compressor inactive** (latest log measured 25Hz, wait); approved restart method and normal heat-pump operation. Source <=90s from ARM; ARM log accepted, new gap>=5000ms, 30s+50 verified frames for positive `RX_SHADOW_ONLY`; negative fault reason/timeouts/mismatch/unsafe or missing proof inconclusive per source criteria; note B11D first fault separately. Abort/cancel on heat-pump alarm, unexpected TX/DE, lost HA, CRC/parser corruption; do not repeat uncontrolled restarts; restore controller approved procedure or verified FIX2 if regression. Required continuous API log from before ARM to >=90s plus exact physical timings and heat-pump state. Status PREPARED/NOT RUN until user confirms and supplies log. [Exact procedure](V5DCM/V5DCM33_FIX_B_POST_GAP_01_PREPARED_20261018.md).

---

# V5DCM33-FIX-B-LIVE-PASSIVE-01 — COMPLETE / POSITIVE (PASSIVE LIVE ONLY), 2026-10-18. User-attested flash of V5DCM33-FIX-B validated by actual runtime [V5DCM33-FIX-B] PASSIVE marker and new HA text; exact flashed hash UNKNOWN. Source log Pasted text(20261018-212405).txt SHA256 0f86352fd9c6cf2c70c7b3d1ef004c3d2280ef73ca42a3b188993bd566e4a87f, 4999 lines 23:20:28–23:23:50. Known-good source prior FIX-A, user-private FIX-B candidate; baseline local V5DCM32 manual controller-restart experiment COMPLETE/NEGATIVE. Hypothesis: additive post-gap shadow does not degrade RX/HA and cannot send TX when unarmed. ONE controlled software change from FIX-A: added RX-only dormant witness. Positive: FIX-B shown DORMANT reason=NONE gap=0/frames=0; B11D 5617 independent raw/portable/V5 equal, countDiff=byteDiff=CRC and hold/fault 0; B11C 5637/5637 correct with no resync/drops; parser grows 4124->5829 frames with resync/drops=0, HA telemetry live, P5 history=0; TX executor HARD_DENY 944 candidates denied and software physical attempts=0, DE=0, UART write calls=0. Native session V5DCM32 step=0/localGen=0 and native 0x0F FC23=0. Negative triggers absent; no actual post-gap cohort exercised and exact machine hash/physical DE pin unknown. No ARM, no controller restart, no native TX. Abort plan for subsequent distinct live experiment: stop/cancel on CRC, parser, HA, DE/TX, unexpected gap; restore FIX2 known-good RX-only. NEXT V5DCM33-FIX-B-POST-GAP-01 PREPARED / NOT RUN; only when specifically initiated, and observe source finite 90s arm; shadow proof never clears original sticky faults/authorizes session. [Live report](V5DCM/V5DCM33_FIX_B_FIRST_LIVE_PASSIVE_RESULT_20261018.md).

---

# V5DCM33-FIX-B-OFFLINE-01 — **COMPLETE / POSITIVE OFFLINE SOURCE/HOST/STATIC ONLY** (2026-10-18); **FIX-B-LIVE-PASSIVE-01 PREPARED / NOT RUN**. Hypothesis: after manually scoped >=5s R6-P24 callback gap, a separate independent CRC/byte-parity RAW witness can distinguish 30s+50 new clean RX frames from historical B11D fault without clearing any original latch. Source known baseline user-private FIX-A ZIP ec26b859..., user-attested FIX-A live passive RUNNING/PARTIAL zero B11D/B11C current errors, earlier V5DCM32 rejoin COMPLETE/NEGATIVE with user manual power cycle, 22:02:30 first fault preceding 12.923s gap, BadIntegrity and no local generation. One controlled addition: bounded one-shot 90s manually armed raw witness on EXISTING UART callback, raw candidate-length/CRC plus V5 parity (NOT session permission), 25ms idle/250ms deferral; no native target payload or TX. Positive criteria: gap after ARM; 30s/50 independent matched clean frames; negative on CRC/parity/overflow/parser delta/DE/TX/second gap/timeout. Host 54 FIX-B policy PASS and 70 original 20261003 local RAW frames PASS with synthetic timing, regressions FIX-A 52+32, V5DCM31 61, V5DCM32 34+34 PASS. Static YAML preserved all 117/13/47 existing HA entities, 5 original buttons, 1 switch, all 44 includes; added 1 diagnostics text+2 Configuration buttons, no UART write/DE changes. ZIP sha256 1753e92590237e9685f74d8c9d80ca64064cb73e5151d56dcdfc38cbc0769cde. No ESPHome build, flash, ARM, controller restart or live run. Inconclusive for original fault cause/current power-cycle rejoin; historical B11D/P5 holds never cleared, session bridge untouched. Abort future live if HA/bus CRC/TX/DE changes; rollback known-good FIX2 RX-only; no uncontrolled test. Next unarmed FIX-B boot/RX observation only after user-initiated flash, then separately scoped live cohort before considering FIX-C. [Full report](V5DCM/V5DCM33_FIX_B_POST_GAP_RAW_WITNESS_OFFLINE_20261018.md).

---

# V5DCM33-FIX-A-LIVE-PASSIVE-01 — RUNNING / PARTIAL (2026-10-18). User reports flashing offline FIX-A and supplied 2050-line API log, SHA256 96f4f25dc5ee551f21a7d3c5173eece70ec62f85bef585f44d4d65207a9e46ed. No ARM or controller restart. B11D 529 compared frames, zero CRC/byte/length differences, no new faults or hold. B11C 548 frames, zero drops, parity holds. Main V5 parser had eight resyncs already at log start, stable thereafter; Bridge04-1 recorded one historical event and recovered passively. Separate R6 P5 historical fault state remains. V5DCM32 observer stays unarmed step=0 localGen=0; portable ledger 1/33. TX HARD_DENY physical attempts 0 software DE=0. User flash attested but exact binary hash unverified. Positive passive RX health only, not proof of tested short-fragment branch or live rejoin. Existing offline FIX-A COMPLETE/POSITIVE and V5DCM32 reboot COMPLETE/NEGATIVE unchanged. NEXT offline FIX-B preparation; do not ARM or restart yet. [Live report](V5DCM/V5DCM33_FIX_A_FIRST_LIVE_PASSIVE_LOG_20261018.md).

---

# V5DCM33-FIX-A — **COMPLETE / POSITIVE (OFFLINE SOURCE/HOST/STATIC ONLY)**, 2026-10-18; LIVE PREPARED / NOT RUN. Hypothesis 1–4 RAW residuals could wait for split-frame completion without bypassing CRC iff V5 parser independently reports fresh pending. Known-good rollback V5DCM23 FIX2 RX-only; actually installed V5DCM32 fresh-rejoin live COMPLETE/NEGATIVE (confirmed manual controller cycle, 22:02:30 incomplete, 12923ms gap, 14 FC23, BadIntegrity, 0/0). ONE change: B11D short-residual decision only, <=250ms, fresh V5 pending required; no latch reset, no TX/DE/HA production changes. Offline 52+32 strict new C++ assertions PASS, regression 34+34 V5DCM32 and 61 V5DCM31 PASS; YAML one-lambda+one-include diff, 43/43 includes, 117/13/47 original sensor/binary/text and 5 buttons, 1 switch retained. Negative controls missing pending, timeout, CRC corruption, byte parity mismatch, unknown slave fail closed. No actual 22:02 raw residual replay, compile, flash, on-device run or physical epoch/owner evidence. Private ZIP SHA256 ec26b85929a760be04b03031b02d10a432fc1765c9e699428bec51aa23cf7bd0. NEXT V5DCM33-FIX-B explicit post-gap clean-integrity proof PREPARED / NOT RUN (offline); user live test not armed. Abort/recovery: software only now; future separately scoped live trial abort on RX/HA/TX regression and rollback FIX2. [Report](V5DCM/V5DCM33_FIX_A_SHORT_RESIDUAL_SOURCE_RESULT_20261018.md).

---

# V5DCM33-B11D-AUDIT-01 — COMPLETE / POSITIVE (offline source audit only), 2026-10-18. Hypothesis existing B11D incomplete-fragment guard handles all fragment lengths symmetrically; source disproves symmetry: after 25ms idle a 1–4 byte RAW residual faults immediately, whereas >=5-byte recognized pending candidates can defer up to 250ms. Baseline actually deployed RX-only V5DCM32, live rejoin denied on user-confirmed controller power cycle; controlled change NONE (analysis only). No original 22:02 raw residual reproduced, so physical event causation remains UNKNOWN. No compilation, flashing, TX, or live test. NEXT V5DCM33-FIX-A PREPARED / NOT RUN; source-only deferral prototype with strict negative CRC/orphan/timeout fixtures, preserve sticky holds and fallback FIX2. [Report](V5DCM/V5DCM33_B11D_SHORT_RESIDUAL_OFFLINE_20261018.md).

---

# 2026-10-18 V5DCM32-LIVE-OBS-01 follow-up: user explicitly answered YES to having switched the Thermia controller off and on around the observed 22:02:30–22:02:43 interval. Mark manual controller power cycle USER-CONFIRMED; clock-edge times and independent epoch still unmeasured. 22:02:30 B11D incomplete fault, 22:02:43 12923ms callback gap, 22:02:45 FC23 burst, step=2 verdict=5 BadIntegrity, local generation 0, 0/0 revoked; no rejoin. Live result COMPLETE / NEGATIVE unchanged, no TX detected in software. V5DCM33 source-only analysis next.

---

# V5DCM32-LIVE-OBS-01 COMPLETE / NEGATIVE for controlled fresh rejoin on current live XTR. Arm 22:02:23, B11D incomplete frame fault 22:02:30, R6 P24 12923ms gap 22:02:43, first FC23 22:02:45, 14 FC23 by 22:03:40. V5DCM32 Denied verdict=5 BadIntegrity at 22:02:49, localGen=0. Correct FC23-ledger invalidation 1/33 to 0/0, no reselect. Completed CRC frame parity otherwise good, but B11D fault latched. Software TX denied, DE=0. Physical controller reboot timing UNKNOWN. No automatic retest; offline B11D integrity analysis next. Full provenance: V5DCM/V5DCM32_LIVE_REJOIN_INTEGRITY_DENIAL_20261018.md.

---

# 2026-10-18 — V5DCM32-RX-REJOIN-INTEGRATION-01 COMPLETE / POSITIVE OFFLINE ONLY; V5DCM32-LIVE-OBS-01 PREPARED / NOT RUN. Hypothesis user-armed V5DCM31 accepted-risk local-generation fresh context can unblock actual FIX2 passive native 33-group ledger AFTER FC23 without fake controller epoch or TX. Known-good source user-private FIX2 ZIP SHA256 561169c3..., original deployed user V5DCM23 FIX2 RX-only 1/33 with B11C/B11D clean and HARD_DENY, exact flashed image unverified; original V4.1 EXP386/387 positive, EXP388 PARTIAL; G01–G06 accepted. One controlled source integration: add fresh-only read-only local-generation policy/bridge in existing completed-CRC callback after R6-P24 witness, require prior revoke and new post-arm return+cold+canonical FC23, forbid duplicate scope; preserve old production RX, HA and TX. Strict C++17 actual ledger/CRC test 34/34 PASS synthetic plus 34/34 same with genuine 20261003 local FC23; original V5DCM31 61/61 PASS. Negative fixtures lone FC23, no new gap, wrong ESP boot, repeated event, stale pre-arm, manual cancel DENIED. YAML static check syntax PASSED 42 original+2 new headers, 117 sensor+13 binary+47 text unchanged, original 3 buttons plus 2 Configuration; only source YAML+ledger header changed among 55 prior ZIP files; no new TX path. No full ESPHome compilation, flash, physical bus operation or live current-device result. Abort: any on-device DE/TX, CRC/parser/HA regression in later separately user-initiated run => rollback known-good FIX2. Current LIVE FIX2 RUNNING/PARTIAL; candidate is NOT FLASHED. [Report](V5DCM/V5DCM32_RX_REJOIN_SOURCE_INTEGRATION_OFFLINE_20261018.md).

---

# 2026-10-18 — V5DCM31-MANUAL-SESSION-SCOPE-01 COMPLETE / POSITIVE **OFFLINE SOURCE/HOST ONLY**, no physical experiment. Hypothesis acceptance of G01–G06 risks can become a bounded manual experimental *metadata* context without requiring counterfeit current physical-epoch proof; baseline live V5DCM23 FIX2 RX-only 1/33 software TX HARD_DENY, V5DCM29 verified-only issuer absent and V4.1 EXP386/387 positive, EXP388 partial. One controlled new header source `v5dcm31_accepted_risk_session_policy.hpp`, not wired to running YAML or old ledger, to admit limited one-shot RX candidate for fresh/retained/recovery only when user-initiated arm, current local same-boot CRC+ metadata, expected path, limited time and frame budget, accepted risk and unchanged topology; no owner/ACK/TX/Online claims. Strict g++17 61 PASS, GAP24 original header join PASS. Negative checks: absent arm/risk/topology, duplicate scoped IDs and frame sequence, stale timestamp, wrong ESP boot/model, CRC/parser fault, peer response conflict, semantic pending, timeout, budget and cancellation. Corrected one test-fixture duplicate frame sequence while adding replay guard; final rerun PASS; NOT protocol negative. No actual ESPHome compile, flash, bus TX or HA change. Private ZIP cc576fed... NOT FLASHABLE. Next V5DCM32 RX-only local-generation ledger seam PREPARED / NOT RUN. [Detailed result](V5DCM/V5DCM31_ACCEPTED_RISK_SESSION_POLICY_OFFLINE_20261018.md).

---

# 2026-10-18 — DECISION/STATUS CLARIFICATION (NOT a new experiment): user reconfirms G01–G06 residual engineering risks are accepted for this unchanged XTR research installation. Earlier accepted risks and conditional G02 must not be reopened automatically or treated as a blanket development/TX research veto. V5DCM30-INDEPENDENT-WITNESS-AUDIT-01 retains COMPLETE/INCONCLUSIVE only for obtaining an independently proven current physical epoch from existing evidence. No new on-device test occurred; no statuses or earlier negative findings retroactively promoted. Next V5DCM31 must focus on source-only bounded V4.1-derived native session/recovery experimental policy, separating verified-witness mode from user-accepted-risk test mode. Do not synthesize V5DCM29 IndependentProof or enable unsolicited output. Live activation only as documented armed user-initiated test with CRC, exact known response slot, controlled scope/timing, abort and rollback; current FIX2 remains RX-only.

---

# 2026-10-18 — V5DCM30-INDEPENDENT-WITNESS-AUDIT-01 COMPLETE / INCONCLUSIVE (current XTR independent witness). Hypothesis existing logs/video and firmware/G01–G04 sources might supply independently grounded current physical epoch/continuity to V5DCM29. Baseline user-flashed FIX2 RX-only RUNNING/PARTIAL, 1/33, 0 native FC23 in first log, TX HARD_DENY. Controlled change: offline only audit source-typed previous evidence + original historical capture hashes, no YAML/TX/controller restart. Positive historical G01-09 VIDEO_ANCHORED user intervention, not controller-rail measurement or current session; already accepted G02 conditional unchanged installation, not electric exclusive owner. Historic local raw 20261003 2687 entries/2 FC23, 20260925 892/0; G01 original video/raw referenced in report but not mounted now. EXP386/387 positive native v4.1, EXP388 partial, G04 physical EOF/slot open. No independent present session issuer and old R6 D=4 first fault unknown => current witness hypothesis INCONCLUSIVE, not protocol NEGATIVE. Abort not applicable offline; no device action, preserve all prior evidence, no TX. V5DCM31-MANUAL-SESSION-SCOPE-01 PREPARED/NOT RUN next offline. [Report](V5DCM/V5DCM30_INDEPENDENT_WITNESS_AUDIT_20261018.md).

---

# 2026-10-18 — V5DCM29-SESSION-PROVENANCE-CONTRACT-01 COMPLETE / POSITIVE (OFFLINE source design/strict host only). Hypothesis V5DCM28 conflated controller's physical epoch with increasing local session generation, preventing legitimate retained rejoin when physical epoch stays unchanged. Baseline private V5DCM28 source-only ZIP c92ffff1..., live RX-only FIX2 still partial 1/33. Single controlled change: create independent nontransmitting typed provenance contract, not wired into FIX2 or original ledger. g++17 PASS: fresh/recovery/retained synthetic evidence plus negative source, chronology, age, stale generation and continuity tests; production-style build with NO witness issuer fails closed; unchanged historical 20261003 FC23 passed into actual original V5DCM28 ledger revokes 1/33, no reselect from historical shapes. Positive only under synthetic test proof; no actual independent physical witness source/owner/slot found, all TX/ACK/Online denied. Private ZIP 2b044617411de452870ce70210c02fa0b3fd71e31815454248212881f23c2320 not flashable. No device compiles/flash/Tx/HA edits. Next V5DCM30 witness-source audit PREPARED/NOT RUN; older V5DCM26 passive live still NOT RUN. [Report](V5DCM/V5DCM29_SESSION_PROVENANCE_CONTRACT_OFFLINE_20261018.md).

---

# 2026-10-18 — V5DCM28-EPOCH-GUARD-01 COMPLETE / POSITIVE (OFFLINE ONLY). Existing unflashed V5DCM27 source allowed a repeated numeric session-generation label after a second receive-boundary reset. One controlled source change requires strictly newer labels. Original C++17 portable frame/CRC test and existing three-path evidence-adapter tests PASS, including an unchanged historical FC23 frame; synthetic test assertions are not physical controller proof. New private ZIP c92ffff1aaefef81a4901e8eb0b90baa02c0fa96c2b61f59249e14239eaab687 is NOT FLASHABLE. No ESPHome build, device run, production YAML change or bus activity. V5DCM29-SESSION-PROVENANCE-CONTRACT-01 PREPARED / NOT RUN; existing V5DCM26 passive run remains PREPARED / NOT RUN. [Report](V5DCM/V5DCM28_EPOCH_GUARD_AND_LIFECYCLE_PROVENANCE_OFFLINE_20261018.md).

---

# 2026-10-18 — V5DCM27-SOURCE-REJOIN-01 COMPLETE / POSITIVE **OFFLINE SOURCE/HOST ONLY**; follow-up V5DCM27-REJOIN-BRIDGE-01 PREPARED / NOT RUN. Hypothesis native V5DCM23 33-group ledger does not reselect itself after FC23 despite live V4.1's locally proven qualified recovery precedent. Baseline user-supplied FIX2 ZIP SHA256 561169c3..., YAML 04f562e2..., live RX-only 1/33 with no FC23 in short log. One controlled offline action: review exact private on_boot callback and run two strict C++17 test sources against unchanged v5dcm1 and v5dcm23 headers; 11 shadow invariants PASS, and ledger 1/33→0/unconfigured on CRC-valid native FC23→still unconfigured with further FC16→explicit resel→1/33 PASS, including actual original historical 20261003 CRC-valid FC23 frame. Caution: synthetic fixture has no on-wire ownership/Online implication and no current physical retransmission. Negative criterion unauthorized auto-reselect/TX/owner claim; no such in tested source. Hardware/compile/flash/run on current device NOT DONE. Next design one fail-closed external profile/epoch requalification seam, on matching RX event only after independently justified origin, preserving all 180 current HA entities and TX HARD_DENY. No native TX attempted, no recovery or rollback necessary offline; old R6 Stage D hold remains independent. [Report](Research/V5DCM/V5DCM27_NATIVE_REJOIN_SOURCE_AUDIT_20261018.md).

---

# 2026-10-18 — V5DCM26-PASSIVE-CENSUS-01 COMPLETE / POSITIVE (offline) + V5DCM26-LIVE-OBS-01 PREPARED / NOT RUN. Hypothesis: passive 0x0F FC16 strict 33-significant-group package burst census distinguishes settings delivery from periodic operational traffic. Baseline live V5DCM23 FIX2 1/33 with clean RX and HARD_DENY. One controlled offline addition: standalone standard library Python decoder for timestamped local reference frames, CRC and FC16 length check, grouped 30s start/count W2/W3/W4 masks, FC23 count; no request payload decoding / native TX. PASS script 33 distinct descriptors (15/10/8), CRC fixture + mutation negative; 7 original captures replay: local 09:05:50 892/892 valid 24/33 strict with 03E8/13 and 0410/21 wrong vs current; local 10/03 2687/2687 31/33 and 2 FC23; cross-model Eco5 09/26 10719/10719, 09/28 9174/9174, 33/33 shape inventory both, not proof of controller owner/C2/Online. Separate identity audit: 44 matching names+IDs, 218 public prepared RX33 not in private FIX2, 136 FIX2 not in public; code migration blocked pending producer/reference validation. Live observation planned: SAME FIX2 unchanged, 15–20min existing V5DCM19/22/23+B11C/B11D+S8 logs, no TX/reboot, positive new groups, negative none with healthy capture, inconclusive missing data; abort bus/HA degradation/DE high/TX, revert last verified RX-only. Never mark COMPLETE until user results. [Report](Research/V5DCM/V5DCM26_PASSIVE_CENSUS_OFFLINE_20261018.md); [Inventory](Research/V5DCM/V5DCM26_HA_IDENTITY_PARITY_AUDIT_20261018.md).

---

# 2026-10-18 — V5DCM25-REQUEST-CYCLE-01 COMPLETE / POSITIVE (offline source + passive historical log correlation only). Hypothesis original Connect active three-group request lifecycle matches native 0x0F FC16 sequence. Known-good FIX2 live RX-only 1/33 with unrelated old R6 D=4; no device changes. One controlled offline action: compare real AppFS 2.1.105 modules against device_client.zip BYTE-EQUAL (3/3), source-read 930 request/receipt/handshake phases and CRC-check existing logs. Local historic 20260925 68.23s baseline with 0 settings FC16 then single broad request edge -> 15 upper +16 lower unique FC16 in ~33.69s, 39 ACKs. Eco5 20260926/28 multiple repeat cross-model broad request and progressive clear episodes. Negative control: periodic operational FC16 without matching requests. Source shows internal accepted flag after qualifying FC16, not 32/32 vendor prerequisite; native acceptance, profile C2, owner and current FIX2 request status UNKNOWN. No writes/TX, compiler/flash/run NOT done. V5DCM26-REQUEST-RECEIPT-OBS-01 PREPARED / NOT RUN next RX-only candidate with fail-closed/rollback, but must first restore HA entity identity parity. [Evidence](Research/V5DCM/V5DCM25_REQUEST_CYCLE_SOURCE_CAPTURE_AUDIT_20261018.md).

---

# 2026-10-18 — V5DCM24-SOURCE-GATE-01 COMPLETE / POSITIVE (OFFLINE source/host test, NOT device). Hypothesis separate R6 D=4 sticky transport gate plus Connect 33-group request readiness can explain clean V5DCM23 1/33 and contemporaneous D=4 without parser contradiction. Baseline FIX2 live RX-only RUNNING/PARTIAL, user ZIP source not byte-verified flashed. Single controlled offline analysis: extract exact Stage-D ledger from ZIP and compile C++17 strict; feed historical 2687/2687 CRC-valid reference frames (32 pages/32 ACK state3), synthetic local-shape repeated page and missing ACK (both state4 with expected distinct reasons); inspect original 2.1.105 source CM930 request flags and package receipt tracker. HA inventory full RX33 FIX1 262 named /74 state classes vs private FIX2 180/31, identity diff still open. Outcome positive for source/host tests; inconclusive for actual live first D=4 reason or native C2. Abort/recovery not applicable offline; preserve current TX HARD_DENY and known-good image. No flash/physical TX. [Report](Research/V5DCM/V5DCM24_SOURCE_GATE_REQUEST_AUDIT_20261018.md).

---

# 2026-10-18 — V5DCM23-FIX2 RX-only LIVE RUNNING / PARTIAL based on user's 3536-line ESPHome log; prior FIX1 header and ESP_LOGW compiler faults resolved enough to boot and report. Actual portable ledger profile=1 received=1/33, RX33 same W3 bit0 03E8/14, 140 matching occurrences, zero geometry/FC23/integrity observer faults. B11C up to 1046 matched and B11D to 1053 matched, no CRC/diffs/resync/drop, software TX HARD_DENY 208/208 and zero physical_attempts, DE=0. HA measurements updated, uptime grows 34→124 sec. R6 P30EC reports earlier D=4 INTEGRITY_HOLD_NO_TX, distinct from current clean parser; needs offline provenance analysis. Positive partial criteria satisfied; full endurance, controller owner/epoch/C2 and electrical TX remain open. No new TX. Report Research/V5DCM/V5DCM23_FIX2_LIVE_RESULT_PARTIAL_20261018.md.

---

# 2026-10-18 — V5DCM23-FIX1 PREPARED / NOT RUN for ESPHome/device. Real user compiler failure: missing xtr_v5dcm21_packages.hpp when ESPHome generated main.cpp includes v5dcm23_v5dcm19_real_ledger.hpp. One controlled source fix: private ZIP adds xtr_v5dcm21_readiness.hpp and xtr_v5dcm21_packages.hpp to esphome.includes, ensuring generation copies both. Offline 40/40 include paths present, strict C++ ledger host test PASS, historical 2687 CRC-valid frames replay PASS; original YAML except two lines, runtime parser, HA identities, TX HARD_DENY unchanged. Positive future criterion user's actual ESP-IDF full compile and RX-only boot; negative missing further dependency or regression, abort new TX/crash, rollback previously functioning V5DCM22. Not flashed/executed. Report Research/V5DCM/V5DCM23_FIX1_ESPHome_INCLUDE_REPAIR_20261018.md.

---

# 2026-10-18 — V5DCM23-EMBED-OFFLINE-01 COMPLETE / POSITIVE; V5DCM23-EMBED-LIVE-01 PREPARED / NOT RUN. Source baseline: previous private V5DCM22-on-V5DCM19 candidate, distinct from unproven exact flashed binary. Hypothesis: actual portable RX-only 33-group ledger can consume existing CRC-completed V5 callback without parser/TX or HA regression. Controlled change: private package adapter + four YAML insertions, old RX33 witness retained for future parity check, no outgoing bytes. Validation: strict host C++17 compile/tests PASS; historical 2687/2687 CRC-good, 162 native FC16 and 2 FC23 byte replay PASS fail-closed 0 qualified post-boundary; original YAML byte-identically restored by removing additions; all 180 HA names and 17 original intervals retained. Negative criteria malformed count/CRC accepted, C2/TX promotion or HA/parser regression; abort/rollback to prior known-good if future device execution degrades. Full ESPHome build, flash, user live result NOT RUN; no current hardware change. Private ZIP SHA256 127d781089134569299f4e01faa8c380d2176dcd0794e06a7fd971240e6c179d. [Report](V5DCM/V5DCM23_OFFLINE_INTEGRATION_STATUS_20261018.md).

---

# 2026-10-18 — V5DCM22-V5BASE-RX33-01 RUNNING / PARTIAL first user live evidence: 6 RX33 rows ~3 min, 1/33 exact page (03E8/14), 28→168 strict occurrences, no wrong count/FC23/integrity, V5DCM19 heartbeat retained, B11C/B11D clean, software HARD_DENY physical_attempts=0. Earlier OTA rollback app1 warning, unresolved actual active slot/hash; do not mark experiment COMPLETE. V5DCM23 source-only controlled change replaces conceptual duplicate witness by C++ wrapper accepting existing complete-wire V5 callback and feeding actual PassivePackageIntegration, without new UART/TX; strict exact-head [CI run 39140420159](https://github.com/ryckema/Thermia_Connect_Firmware/actions/runs/39140420159) SUCCESS. **V5DCM23-OFFLINE COMPLETE / POSITIVE**, hardware/deployed private YAML **PREPARED / NOT RUN**. No new live TX or on-device change. Criteria future: exact source, unchanged HA, zero native output, qualified profile and timeout/epoch boundaries; abort bus or HA regression. [Report](V5DCM/V5DCM23_V5_CALLBACK_REAL_LEDGER_OFFLINE_20261018.md).

---

# 2026-10-18 — V5DCM22-V5BASE-OFFLINE-01 COMPLETE / POSITIVE (offline scope) and V5DCM22-V5BASE-RX33-01 PREPARED / NOT RUN (device). Hypothesis: one known V5 completed CRC-valid RX callback can witness exactly 33 source-selected W2/W3/W4 shapes without introducing a second UART reader or physical TX. Known-good actual family V5DCM19 FIX1 ~189s and V5DCM20 18m33 passively tested, but uploaded ZIP bytes not proven flashed. One controlled change in private, never GitHub-published ZIP: passive witness header, boot reset, one native frame callback, one log interval. Static restored original YAML byte-identically, strict YAML parse PASS, all 180 HA names/16 original intervals present, TX hardware settings unchanged; C++17 strict host test PASS. Real 20261003 historical capture replay: 2687 valid frames,162 0x0F FC16,2 0x0F FC23,31 strict distinct of 33 starts,126 matched frames,2 wrong-count references,FC23 continuity revoke,C2/owner/Online/TX always false. Negative criterion false Y or any new TX/HA regression; inconclusive no native traffic/source unverified; abort and revert to known good on regression. No ESPHome compilation, flash, new live XTR result or TX. Actual portable PassivePackageLedger not yet embedded; source-only adapter is interim. See Research/V5DCM/V5DCM22_V5DCM19_PRIVATE_RX33_OFFLINE_20261018.md.

---

# 2026-10-18 — **OFFLINE BASELINE AUDIT (no new live experiment)**. Compared user ZIP `V5DCM19_RX_ONLY_FIX1_20261018(2).zip` to GitHub FIX4/RX33 status. ZIP SHA256 `ca1dd272...`, internal YAML `44a9d821...`; strict YAML duplicate-key parse PASS, 180 named HA objects, 31 numeric state classes, one interval list, native V5DCM1/2 observers and RX parity guard; TX pin GPIO17 configured though DE GPIO21 ALWAYS_OFF and HARD_DENY policy. ZIP README/YAML say PREPARED, so does not establish exact bytes deployed; separate canonical V5DCM19 live and V5DCM20 18m33 results CONFIRM a V5DCM19-family RX-only live baseline. More recent RX33 full-monitoring candidate has larger HA inventory, no UART TX pin, 33 groups and 40 stat-class fixes. Decision prefer native V5 observer as DCM functional development basis, retain full HA/metadata and source-provenance gate. No new experiment status changed. [Audit](V5DCM/V5DCM19_FIX1_VS_V5DCM22_BASELINE_AUDIT_20261018.md).

---

# 2026-10-18 — **V5DCM22-RX33-01 STATCLASS FIX1 PREPARED / NOT RUN.** User warning: old Heating Minimum LTS statistics exist but current HA entity lacks `state_class`. Root cause directly verified in both known FIX4 and RX33 prepared YAML. One controlled source change: separate full YAML adds exactly 40 existing numeric physical-unit sensor `state_class: measurement` keys (21 temperature +19 other measured duration/correction/setpoint), no names/IDs or transport code changed. Offline difference audit **PASS: exactly 40 added lines, all others byte-identical** after comment header removal. Criteria: HA attributes restore `measurement`, same unique_id/entity and unit, preserve old data, continued RX health; negative: metadata/timing regressions or inadvertent TX. Abort/rollback to user-tested FIX4 on regression. No outgoing Thermia frames. No full ESPHome compile, OTA flash or HA result has occurred. **DO NOT DELETE HISTORICAL STATISTICS.** [Plan](V5DCM/V5DCM22_RX33_STATCLASS_FIX1_PREPARED_20261018.md).

---

# 2026-10-18 — **V5DCM22-RX33-01 PREPARED / NOT RUN**. Hypothesis: full strict 33-page XTR W2/W3/W4 receive-only witness can identify observed native FC16 start/count pages and separately identify variant counts, without changing existing production entities or physically TXing. Verified FIX4 starting source blob `f4b90fc...`, latest native source profile blob `75b800e...`. One controlled change: separate [full YAML candidate](V5DCM/V5DCM22_RX33_ONLY_PREPARED_20261018.yaml) with 7 globals, 4 HA diagnostics, one passive callback hook. Static reconstruction of original after removing exactly 4 inserts PASS; all IDs/checks PASS. Positive = correct match/mismatch witnesses with stable bus/no TX. Negative = false Y, bus/HA regression, TX. Inconclusive = missing live traffic / no flash / no epoch proof. No outgoing payload, native requests or active driver enable; RX observation 15–30 min once user initiates. Abort/rollback to pre-test FIX4 or independently stable V5 on any bus regression/TX. **ESPHome validation/compile NOT DONE, flashed NOT DONE, executed NOT DONE**; no new live results. [Full experiment](V5DCM/V5DCM22_RX33_01_PREPARED_20261018.md).

---

# 2026-10-18 — **V5DCM22-REPLAY-02 COMPLETE / POSITIVE** (strict standalone C++17/Python raw capture parity) **plus VERIFIED GitHub exact-HEAD source/CI SUCCESS**. [Actions 39130592175](https://github.com/ryckema/Thermia_Connect_Firmware/actions/runs/39130592175), commit `9c14bb3`, passes real portable C++ join and byte-replay build, safe synthetic two-language actual ledger fixture, original regressions and TX hard-deny. Original private capture *not* supplied to CI; locally run standalone C++ and Python against original gave exact 16 counters + 2 geometry-list parity (2687/2687 valid CRC, 162 FC16, 33 starts, 31 physical shapes, 2 FC23, 0 qualified receipts), CRC negative fixture PASS. Full v31 FIX4 production unchanged, no live physical TX, device/Online C2 not proven. V5DCM22 overall RUNNING / PARTIAL. [Report](V5DCM/V5DCM22_CPP_PYTHON_PARITY_OFFLINE_20261018.md).

---

# 2026-10-18 — **V5DCM22-REPLAY-02 COMPLETE / POSITIVE, offline host-level cross-language parity**. Hypothesis independent C++17 byte replay of historical 20261003 capture matches prior Python results for CRC/0x0F FC16 page shape/FC23 reset. Baseline original 33-package descriptor + REPLAY-01. Controlled change: local standalone C++ (not exact GitHub portable Core) compiled g++ C++17 strict, replayed unchanged original file and compared to freshly rerun Python. **16/16 fields + 2 geometry lists matched**: 2687 total+valid,162 FC16,33 selected starts,31 exact shapes,126 matching occurrences,2 wrong counts,2 FC23 resets,0 qualified receipts/physical TX. Mutation fixture single CRC byte fails both. No on-device test. Full GitHub class CI/build still NOT VERIFIED, V5DCM22 overall RUNNING / PARTIAL. Abort no TX/no production changes; none triggered. [Report](V5DCM/V5DCM22_CPP_PYTHON_PARITY_OFFLINE_20261018.md).

---

# 2026-10-18 — **V5DCM22-REPLAY-01 COMPLETE / POSITIVE (offline byte-for-byte fail-closed test)**. Hypothesis that all 33 source-selected package starts appear but local XTR 33/33 C2 is unproven because two physical count mismatches; baseline V5DCM22 source-selected 33-group ledger. Controlled change replay raw historical 20261003 log in exact timestamp order, no reconstructed payloads, verify CRC, FC16 counts, FC23 boundaries. RESULT **2687/2687 CRC valid, 162 0x0F FC16, 33/33 selected starts, 31/33 local shape matches, 126 matched occurrences, 2 wrong-count selected frames**, native 0x0F FC23 at 27.400/27.429 before FC16; existing integration revokes profile and therefore **0 qualified receipts without externally justified reselection**. Offline CRC mutation rejected. C++ actual join runner committed but build/run **unverified**; existing production unmodified, zero physical TX. Recovery not needed. [Detailed report](V5DCM/V5DCM22_RAW_CAPTURE_REPLAY_RESULT_20261018.md).

---

# 2026-10-18 — V5DCM22 offline capture provenance check RUNNING / PARTIAL: historical thermia_capture_20261003_165355.log 162 valid FC16, all 33 candidate starts, two local-geometry mismatches (03E8/13 vs14, 0410/21 vs22) therefore maximum 31/33 exact geometry in that historical source. Not a new on-device experiment; C2 not proven, no TX.

---

# 2026-10-18 — V5DCM22 RUNNING / PARTIAL extension: one source-only controlled change adds 33 profile starts/bits/counts from original 2.1.105 semantic selection + repo selector and physical XTR profile; synthetic CRC-valid full group replay test and workflow path inclusion. Criteria full replay C2 only at 33/33 and revoke on bus return; test not independently executed, no new live data. No TX or deployed YAML.

[Implementation update](V5DCM/V5DCM22_PACKAGE_INTEGRATION_PARTIAL_20261018.md)

---

# 2026-10-18 — V5DCM22 RUNNING / PARTIAL source-only: baseline v31 FIX4 RX-only and V5DCM21 package ledger. Controlled change new integration header + 13 synthetic test checks + GitHub CI compile step. Expected result: source-qualified package accounting and lifecycle revocation without TX. Actual execution of tests pending confirmation; no device test. Fail-closed and rollback via unchanged production.

[Implementation note](V5DCM/V5DCM22_PACKAGE_INTEGRATION_PARTIAL_20261018.md)

---

# 2026-10-18 — V5DCM21-PACKAGES-03 RUNNING / PARTIAL; offline original-source subcheck POSITIVE. Direct original Connect 2.1.105 CM930 sensor/config JSON parse 99+471=570 objects, token union 541; source selector ranges independently yield exact 33 group starts W2=15 W3=10 W4=8, 0 unmapped or ambiguous. No live experiment, response or TX. Full normalized CSV object-by-object parity OPEN. Report V5DCM21_PACKAGES_03_RAUC_PROVENANCE_PARTIAL_20261018.md.

---

# 2026-10-18 — V5DCM21-PACKAGES-03 RUNNING / PARTIAL original appfs update: exact 2.1.105 2.3.0–2.4.3 sensors/config JSON parsed (99+471 objects), recomputed numeric receive dependencies=541, matching derived counts. No duplicate names; source SHA hashes and provenance in report. Full row-by-row normalized CSV equality untested. No on-device experiment or TX.

[Detailed original-JSON audit](V5DCM/V5DCM21_PACKAGES_03_RAUC_PROVENANCE_PARTIAL_20261018.md)

---

# 2026-10-18 — V5DCM21-PACKAGES-03 RUNNING / PARTIAL: hypothesis source index exactly matches original 2.1.105 2.3.0–2.4.3 JSON. Inspected original RAUC/container and two source ZIPs; no suitable RAUC SquashFS extractor available. Positive: exact row/token comparison; negative: reproducible mismatch; currently INCONCLUSIVE. No physical TX, YAML or on-device execution. Abort if any unauthorized TX or protected code publication; none.

[Audit details](V5DCM/V5DCM21_PACKAGES_03_RAUC_PROVENANCE_PARTIAL_20261018.md)

---

# 2026-10-18 — V5DCM21-PACKAGES-02 **RUNNING / PARTIAL (offline source audit PASS; no on-device V5DCM21 run)**. Hypothesis: original Connect 2.1.105 significant package request subset for XTR 2.4.2 is smaller than all 32 settings+11 runtime groups and differs from current v31 FIX4 tracked sources. Source baseline original user device_client `_get_all_data_package_to_request` sensor/config-only dependencies, derived firmware `data/cm930_semantic_objects.csv`, W2/W3/W4 range data and XTR physical count profile. Controlled change ONLY `tools/audit_v5dcm21_significant_packages.py` and mandatory CI, never output response/TX frame or mailbox command. Source-derived result **570 objects, 541 numerical dependencies, 33 groups (15 W2 / 10 W3 / 8 W4)**, of which current FIX4 Y/N diagnostic follows 13 and omits 20. Data provenance: original 2.1.105 parser semantics verified from zip; normalized row-to-original JSON equality not newly checked. CI [39126103885](https://github.com/ryckema/Thermia_Connect_Firmware/actions/runs/39126103885) strict current HEAD success, 10 additional audit assertions, previous 26 package and other host suites PASS. Previous actual user FIX4 RX-only `03E8:Y` and subsequent still N report from separate READ-V31-UNKNOWN-01; **not** native Connect C2 proof. Positive scoped offline checks satisfied, negative no failed source assertions, real XTR C2/Online/readiness **INCONCLUSIVE**. Abort unauthorized physical TX/unknown ACK/private emulation publication; none, no recovery required; keep current read-only installation. Autonomous TX in principle allowed; G01–G06 accepted research risks not reopened. [Report](V5DCM/V5DCM21_PROFILE_242_SIGNIFICANT_PACKAGES_20261018.md).

---

# 2026-10-18 — READ-V31-UNKNOWN-01 / READ-V31-COOL-01 — **RUNNING / PARTIAL, further user observation**. User replies that native missing-page mask remains `N` following suggested passive observation; second exact mask/uptime/reboot counter unspecified. No software, TX or settings changes. Earlier FIX4 151s page-source result `03E8:Y`, 12 others `N`; all ten HA-Unknown dependent page branches absent. **New offline review** not a repeat of already-run experiments: historical private local XTR Oct03 native full config 03E8 at 29.262s ACK then 03FC at30.016s ACK, 0410 at31.451s ACK, 042E at32.119s ACK, cooling0442 at33.408s ACK, 0532 at44.763s, runtime07D0 after65.664s; old Sep25 09:05 comparable. Local canonical **EXP325–329 COMPLETE/POSITIVE** previously established qualified R1/FC16 ACK causal page progression in modern count14/22 geometry. **FIX8H COMPLETE/POSITIVE** independently showed 130 recurring 07D0 pages with TX=0 in a pre-established session; no proof the current RX-only firmware can establish that session. Hypothesis native qualified session/ACK unavailable in FIX4 remains STRONGLY SUPPORTED, not proof raw missing pages never transmitted. Live positive scoped receipt diagnostic but overall **RUNNING / PARTIAL** due lack of final physical source/ownership; no experiment status promoted to complete. Previous physical TX=0 cannot be inferred from missing tx_pin alone. Abort/recovery retains V5 verified passive baseline/current FIX4, no active action. NEXT offline prior experiment/provenance review; any new TX-assisted read-only-semantics controller native test must separately document one owner/response class, frame/payload source, timing, TX ceiling and rollback before user-initiated execution. [FIX4 persistent-N follow-up and historical ACK-gated XTR evidence](V31_NATIVE_PAGES_N_FOLLOWUP_20261018.md).

---

# 2026-10-18 — V5DCM21-PACKAGES-01 **RUNNING / PARTIAL** (offline exact-HEAD host execution PASS, no live execution). Hypothesis: Connect 2.1.105 three-mask application-data completeness is independent of native handshake, 32-page cold controller bootstrap, mailbox, Online and TX consent. Known-good native V5 fallback V5DCM19 FIX1 RX-only / V5DCM20 18m33s POSITIVE; **current user-confirmed separate v31 FIX4 read-only live 151s**, not a V5DCM21 flash. Controlled change only firmware repository new `portable/xtr_v5dcm21_packages.hpp`, tests and mandatory CI; no physical target/payload/register write, no new native responder, no production ESPHome YAML. Source input: device_client 2.1.105 original `CMClientParameterUpdateState` and `on_publish_cm_params_map_event`, W2/W3/W4 request map and XTR profile family 2.3.0–2.4.3 selected by existing `0867=242`. Offline criteria PASS GitHub Actions [39124813711](https://github.com/ryckema/Thermia_Connect_Firmware/actions/runs/39124813711), commit `6a96c3a8`: strict actual C++17 build, **26** new assertions for CRC, group/bit ambiguity, out-of-order/duplicate, epoch/source revocation, empty pending set and no handshake/Online/TX promotion; prior source suites and hard-deny PASS. **INCONCLUSIVE for real XTR package completion:** exact significant profile subset and real app runtime absent. Abort accidental TX, guessed package mask or protected responder publication; none occurred. Rollback isolated offline source changes; current read-only firmware unchanged. General autonomous TX authorization and accepted G01–G06 research risks retained. V5DCM18 original full replay PARTIAL. [Report](V5DCM/V5DCM21_2105_PACKAGE_COMPLETENESS_OFFLINE_20261018.md).

---

# 2026-10-18 — READ-V31-UNKNOWN-01 and READ-V31-COOL-01 — **RUNNING / PARTIAL**, user-confirmed FIX4 live observation (supersedes earlier source-only PREPARED entries). **Hypothesis:** Unknown controller-service fields correlate with native 0x0F full-page receipt, while direct 0x1E telemetry continues. **Baseline:** existing v31 FIX4 read-only candidate flashed by user via OTA, source blob `f4b90fcd3d96cb728ba4726409bacd9d5c23b5f3` not byte-matched to flashed build; independently verified previous V5DCM19 FIX1 long-soak RX baseline available for recovery. **One controlled source change** was previously prepared FIX4 Y/N page receipt witness; no code change or TX executed in this observation. **Observed RESULT at 151s ESP uptime:** HA reset reason ESPHome OTA, mask `03E8:Y 03FC:N 0410:N 042E:N 0442:N 0532:N 0546:N 07D0:N 080C:N 0820:N 0848:N 0864:N 0870:N`, `Cooling Settings Page Source = 0442 NOT received since ESP boot`; room/heating settings curve36/min20/max40/setpoint22 populated, direct outdoor Idle/0Hz/0A/fan0rpm, Bus Healthy Connected. All **ten** native decoder page families for exact 34 HA Unknowns remain `N` in 151s. **Scoped positive:** installed diagnostic working, 03E8 positive receipt and 0442 negative internally consistent. **Not proven:** 12 page families never broadcast, their possible different frame geometries, later cadence, actual electrical TX inactivity, raw CRC frame or full original compiler logs. **Future positive:** passive valid full page flips corresponding bit Y and eligible settings update, no bus regression. **Negative:** Y absent despite matching complete frame, Y without valid page, lost direct metrics or unexpected TX. **Inconclusive:** 151s is too short to establish long-run native page recurrence and no settings page receipt isn't decoder-semantic proof. **Abort/recovery:** protect bus-health, no speculative writes, rollback V5 user-verified RX baseline if direct signals regress. **Smallest next evidence:** after 15–30 min uninterrupted FIX4 with no ESP/controller reboot, resend mask, 0442 source and uptime only. Existing FIX4 YAML unchanged. [151s live audit](V31_ALL_UNKNOWNS_HA_AUDIT_20261018.md).

---

# 2026-10-18 — AUTHORIZATION / POLICY EVENT (NOT an experiment): User explicitly authorizes **general, autonomous native TX** for XTR Online/Connect/DCM research and controlled implementation; “Algemene, autonome TX-bevoegdheid: nu toegestaan.” Supersedes older general-consent denials; no need to request repeated broad TX permission for each frame or stage within a previously scoped and armed user-initiated live experiment. Preserve previously accepted G01–G06 engineering risk decisions, unknown technical facts and all negative/inconclusive results. Native autonomous TX still requires explicit bounded protocol state/response class/payload provenance, known slot/timeout/retry limits and abort/rollback in an actual user-initiated deployment/test; no unsolicited scans, speculative/unowned writes, confidential responder publication or spontaneous execution. **Execution evidence: none; on-device TX not enabled or flashed by this record**. Last verified installed V5DCM19 FIX1 RX-only baseline and V5DCM20 POSITIVE retained. V5DCM21 RUNNING / PARTIAL. [Decision](NATIVE_AUTONOMOUS_TX_AUTHORIZATION_20261018.md).

---

# 2026-10-18 — READ-V31-UNKNOWN-01 user observation addendum: still **PREPARED / NOT RUN** for FIX4 on-device testing; no execution confirmed. Full-name HA state list replaces PDF-only count with **34 unique Unknown entries** (15 normal, 19 diagnostic), all grouped by current YAML to 10 native 0x0F sources (0442:7 / 0410:4 / 042E:4 / 0532:4 / 07D0:4 / 0864:4 / 0870:3 / 0848:2 / 0546:1 / 0820:1). Baseline user-reported live healthy direct outdoor metrics (compressor 22 Hz, heat, fan 380 rpm) coexist with Unknown native service values. No exact YAML build fingerprint or FIX4 `Native Settings Pages Seen` in user's shared list. **Positive** future: documented fresh valid native frame yields Y and eligible values; **negative** frame present but source/values fail; **inconclusive** no source page, unknown flash, partial capture. No physical TX/payload/time or state-changing control. Before promoting results get only the Y/N witness from user-confirmed FIX4 with one exact Unknown, then narrow CRC frame if contradiction. Abort on lost direct baseline or DE/TX activation, restore previous verified V5 read-only firmware. [Exact 34-name Unknown source matrix](V31_ALL_UNKNOWNS_HA_AUDIT_20261018.md). No new YAML commits.

---

# 2026-10-18 — READ-V31-UNKNOWN-01 — **PREPARED / NOT RUN** (source changes and offline tests only; no live execution). Hypothesis: most presently Unknown optional/service settings can be classified by whether each complete native controller 0x0F FC16 page appeared since ESP boot, without a DCM or any TX. Known-good deployed RX-only V5DCM19 FIX1; source baseline v31 FIX3 at `c33eed0d4be08b012018e6bd467eb0ba120ceda4` (unflashed). Relevant historical sources READ-V31-COOL-01 (0442 witness) and EXP379/382 cooling mappings, true XTR and cross-model raw capture. One controlled RX-only observability addition to v31 FIX4: 13-bit unpersisted Y/N receipt mask for **03E8(13+)/03FC(11+)/0410(21+)/042E(15+)/0442(13+)/0532(18+)/0546(20+)/07D0(19+)/080C(18+)/0820(18+)/0848(23+)/0864(3+)/0870(14+)** controller FC16; single `Native Settings Pages Seen` text entity. Zero TX payload/slot/timing because no output enabled. Source-only success: all prior 257 HA entity names still present, now 258; no unresolved/duplicate IDs, vars, no uart.tx_pin and DE ALWAYS_OFF; PASS. Live POSITIVE (future): Y for CRC-good observed full native page, N otherwise, matching actual settings updates, zero physical TX; NEGATIVE: Y without frame, missing Y despite frame, baseline regression, unintended TX; INCONCLUSIVE: narrow window/unknown flashed build/no native page even though everything is healthy. Abort on bus-health or observed physical TX regression, restore verified V5 RX baseline. Required minimal evidence after flash: two text sensors (`Native Settings Pages Seen` and `Cooling Settings Page Source`), one actual Unknown full entity name and state, optional short CRC-valid page log if contradiction. Document [Full 33 Unknown HA audit and FIX4 source mapping](V31_ALL_UNKNOWNS_HA_AUDIT_20261018.md); user HA PDF shows 33 truncated Unknown **values**, not 33 proven broken register mappings. GitHub FIX4 commit `6c24cfff`. **No compilation, flashing or hardware test performed.**

---

# 2026-10-18 — V5DCM21-DELIVERY-PROVENANCE **RUNNING / PARTIAL overall; offline validation PASS, device experiment NOT RUN**. Hypothesis: platform callback `Delivered` should not become native response-sent, controller accepted, app ready or TX authorized without independent owner, current epoch, slot and physical witness. Known-good actual flashed V5DCM19 FIX1 RX-only and V5DCM20 18m33s positive; previous model split and native FC23 shape analysis CI success. **One controlled source change family** only: add nonauthorizing `portable/xtr_v5dcm21_delivery_audit.hpp` with source/session/sequence/epoch/electrical evidence axes, `test_xtr_v5dcm21_delivery_audit.cpp` fake generic FC16 adapter-memory delivery and Flush failure, and strict CI; original Core, CRC, hardware adapter, current production YAML unchanged. No active TX frame, payload, target register, timing/retries, response-slot permissions or private security implementation. GitHub firmware `105735f5`, dedicated [CI 39122071866](https://github.com/ryckema/Thermia_Connect_Firmware/actions/runs/39122071866) **22/22 new audit** plus **24 Core / 46 RX / 5 capture / 4 timing / 30 model split / 34 callsite / parity / hard deny PASS**. Scoped offline positives MET; negative synthetic rejected/faulted/replayed/stale delivery denied; physical session acceptance, native private response, exact installed YAML and Online remain **INCONCLUSIVE/UNKNOWN** (no device run). Abort any actual TX/private publication/production change; none. Rollback isolated source additions if needed; no ESP change. V5DCM18 original seven-corpus replay still PARTIAL; G01–G06 accepted. [Full result](V5DCM/V5DCM21_DELIVERY_PROVENANCE_AUDIT_RESULT_20261018.md).

---

# 2026-10-18 — V5DCM21-MODEL-SPLIT and V5DCM21-FC23-FOLLOWUP: overall **RUNNING / PARTIAL** (offline checks PASS; no user-confirmed live execution). Hypothesis A: original Python firmware-like internal ACCEPTED is *not* equivalent to C++ ownership/physical TX/application readiness; preserve and test divergence rather than deleting original historical assumptions. Controlled offline change A: `tools/test_v5dcm21_handshake_model_split.py` + CI, original Python untouched; 30/30 GitHub source/API assertions PASS (Actions 39120900293). Hypothesis B: existing genuine 0x0F FC23 reply shapes should be followed by native FC16 03E8 with profile-dependent counts, without making their CRC a security/acceptance proof. Controlled offline change B: bounded metadata-only analyzer + CI; synthetic temporal cases 4 PASS (Actions 39121165286), local independent CRC analysis on Eco5 2026-09-26 10719 good 0 bad, 99 requests/2 replies; Eco5 2026-09-28 9174 good 0 bad, 64/4; ATEC 2026-10-03 2687 good 0 bad, 1/1. First FC16 after each of 7 reply shapes: modern 03E8/14 (6) or ATEC 03E8/13 (1), delays 92,92,93,482,465,124,1833 ms. **No physical TX, no change to installed FIX1 YAML, no challenge body published; status not COMPLETE without user-confirmed experiment result.** Negative/unproved: no native accept, owner, epoch, slot, semantic success or Online; abort if provenance conflated or private source published; none. Recovery keep known-good user-flashed RX-only. V5DCM18 original seven-corpus Core replay PARTIAL; G01–G06 accepted. [Report](V5DCM/V5DCM21_MODEL_SPLIT_AND_GENUINE_FC23_FOLLOWUP_RESULT_20261018.md).

---

# 2026-10-18 — READ-V31-COOL-01 — **PREPARED / NOT RUN**; bounded offline source addition after PDF/source audit, NOT a completed device test. Hypothesis: RX-only `0x0F FC16 0442/count13` page-arrival diagnostics will separate a missing native settings page from a faulty cooling decoder while retaining all known entities. Baseline prepared v31 FIX2 (250 YAML HA names), independently physically verified V5DCM19 FIX1/V5DCM20 passive positive not overwritten. Controlled change: one receive-page scope — add `Cooling Settings Page Source` (NOT received/received since boot) and 0444/0446/0447/0448/044A/044B raw words, default-disabled, no scales or forged values. `0447` HYPOTHESIS, other five EXP382 STRONGLY SUPPORTED only; `044D` EXP379 locally PROVEN previously. Source FIX3 commit `a3be92f`; 250/250 original names preserved, seven new => 257; all declared ESPHome IDs/refs and substitutions resolve, no TX configuration; README updated. **Future positive:** valid 0442 page makes witness received and publishes raw 13-word word positions correctly, previously valid named settings remain; no bus regression. **Negative:** page CRC-valid but witness false, wrong raw offsets, HA state regression or TX; **inconclusive:** no page seen and narrow capture not covering native refresh. Abort on bus-health/DE/TX regression, recover independently verified V5 passive baseline or archived v31 FIX2; require one timestamped native 0442 full frame, exact cooling entity IDs and source status, ESP boot boundary. No actual controller live result, compile or flash. [FIX3 cooling gap and Unknown audit](V31_COOLING_UNKNOWN_AUDIT_20261018.md).

---

# 2026-10-18 — READ-V31-COOL-01 — **PREPARED / NOT RUN** (offline PDF + source gap audit complete, **no live test and no source YAML modified**). Hypothesis: many cooling settings Unknown are caused by missing fresh 0x0F 0442/count13 controller-originated page, rather than invalid v31 field mapping. Baseline current GitHub v31 FIX2 (250 entities, uncompiled/unflashed as verified project state); independently known-good user-installed V5DCM19 FIX1 and V5DCM20 passive soak preserved. Historical XTR anchors EXP379 044D hysteresis, EXP382 offline strongly supported 0444,0446,0448,044A,044B and hypothesized 0447. Source-controlled intended change: only add bounded read-only 0442 valid-page count and last-seen age diagnostics (and no semantic sensor changes in same test) after checking if current logs already contain complete 0442. Target frame 0x0F FC16 0442/count13; no address write, TX payload, response slot or transmission authorization. POSITIVE: full CRC-valid page seen then corresponding HA cooling values correlate, or absent page positively explains missing source; NEGATIVE: page present yet decoder rejects legitimate fields; INCONCLUSIVE: short window/no full-page evidence, unknown flashed build. Abort if RX health or physical TX/DE regress; rollback to last verified V5 passive baseline; required minimal timestamped 0442 capture + full cooling HA entity names and bushealth, not routine compiler output. PDF shows working compressor/ODU values and many Unknown but truncates names; cannot prove exactly which settings or currently flashed source. [v31 cooling/Unknown source audit](V31_COOLING_UNKNOWN_AUDIT_20261018.md). No external DCM required or proposed.

---

# 2026-10-18 — CM-RO cross-model passive profile planning: **PREPARED / NOT RUN** for future CM-RO-01…05, no experiment executed. Offline source review identified four CM930 semantic profile ranges and four existing model YAML variants, with platform-stable transport families but model-dependent FC16 word counts, native source adapters, history format and semantic profile selection. Controlled next change: offline register/decoder/capture join only, no physical target slave, frame payload or TX; preserve XTR production and profile-specific read-only safety. Positive future source audit: each marketed-model candidate grounded in actual frame geometry and version anchor, all existing shared sensor IDs retained and zero UART TX; negative: profile collisions falsely labelled as proven; inconclusive: absent model capture/identity. Abort on false profile inference or source integrity mismatch; rollback source-only to current profiles, no hardware recovery needed. Evidence: firmware `ALL_PARAMETERS_ACCESS_MATRIX.csv`, `cm930_profile_layer_model.csv`, `cm930_profile_difference_matrix.csv` and existing ATEC/Eco/DHP-AQ README; detailed [Cross-model RX-only profile roadmap](CROSS_MODEL_READONLY_PROFILE_ROADMAP_20261018.md). Do not assign COMPLETE without user-supplied results for actual live tests.

---

# 2026-10-18 — V5DCM21-CALLSITE-GUARD **COMPLETE / POSITIVE (offline substep)**; overall V5DCM21 **RUNNING / PARTIAL**. Hypothesis: public portable/embedded production RX bridge must not call unqualified handshake/mailbox/runtime setters, and cold 32/32 observed RX must not advance authoritative Core if no response was delivered. Known-good local user-flashed V5DCM19 FIX1 RX-only + V5DCM20 18m33s positive. Controlled change solely firmware test/CI source: `tools/audit_v5dcm21_handshake_callsites.py`, additional `test_xtr_v5dcm21_rx_join.cpp` negative assertion, and required CI step, firmware `0f5b3582`. Target observed native `0x0F FC16` 32-page synthetic cold geometry; no live write/command/CRC/payload or physical TX. GitHub Actions [39119204399](https://github.com/ryckema/Thermia_Connect_Firmware/actions/runs/39119204399) strict actual HEAD compile and tests: 24+46+5+33 PASS, embedded source parity PASS, TX hard-deny PASS. Positive scoped source criterion MET; negative no unqualified direct setter detected; XTR native runtime/Online and exact deployed FIX1 source INCONCLUSIVE/UNKNOWN. Abort unsafe TX/public confidential responder or production mutation, none; rollback revert isolated offline guard/test/CI. Keep V5DCM18 full reference replay PARTIAL, G01–G06 accepted. [Result](V5DCM/V5DCM21_CALLSITE_GUARD_AND_RX_NONPROMOTION_RESULT_20261018.md).

---

# 2026-10-18 — READ-V31-OPTIONAL-FIX2 — **PREPARED / NOT RUN** (GitHub source change + offline checks done, live not run). **Hypothesis:** existing XTR optional pool/shunt1/shunt2/buffer values can fail-close if not actually present/valid without losing one of 250 named HA entities, unique native raw registers or RX-only bus-health bookkeeping. **Known-good live baseline:** user-deployed V5DCM19 FIX1 with V5DCM20 positive; **source baseline** v31-alpha01 FIX1 blob `debedae0c22a6d20d29cadbbb46ef0426cf70c06` was itself not live validated. **Relevant earlier:** READ-V31-01, R1–R11 CLEANUP, READ-V31-OPTIONAL-AUDIT; no experiment rerun. **One controlled code change:** gate optional interpreted values and binary pool activity through fresh `0x0F FC16 0x0532/count18` controller page, specifically `0533 pool`, `0534 extra circuit 1`, `0535 extra circuit 2`, `0536 buffer`; flag exactly 1 and age <= 21600000 ms. OFF, invalid, absent or stale => NAN/invalid binary; five-second expiry guard. TTL 6h PROVISIONAL and NOT locally established. Preserve raw option words as default-disabled diagnostics. **TX target/payload/timing:** none (strict RX-only GPIO18, GPIO21 DE LOW; zero response/writes). **Offline source criteria:** 250/250 identical entity names, all unique IDs/references valid, native raw/CRC parser preserved, no UART TX => PASS by GitHub source diff; source status still PREPARED / NOT RUN. **Future POSITIVE live criterion:** captures native 0532, optional states transition ON/OFF/UNKNOWN without stale active readings, CRC health maintained and zero TX. **NEGATIVE:** stale feature ON, false readings, compiler issue or bus-health regression. **INCONCLUSIVE:** no 0532 during observation or can't naturally test installed option. **Abort/recovery:** stop trial at compilation warning, unexpected TX, bus disruption or misdecoded option; restore independently verified V5DCM19 FIX1 or previous source blob from `Research/Archive/Read-only_XTR_before_FIX2`. **Required evidence:** brief 0532 capture+capability and optional HA states with timestamps, RX/TX/CRC diagnostics. **Separate doc-only folder organization:** one YAML `thermia_itec_xtr_m_read_only.yaml` plus one README in `Read-only/Thermia itec XTR`; full previous tree moved intact to Research/Archive, no history rewrite. GitHub commit `4b83915d7899a2ee3ef4218b1a70689c4fa38fa8`; [source audit and full criteria](V31_OPTIONAL_CONSOLIDATION_RESULT_20261018.md). **Not compiled, flashed or tested on device**; HA disabled_by_default is not dynamic enabling; optional dashboard cards documented in README. 524 profile coverage still unfinished.

---

# 2026-10-18 — V5DCM21 embedded Core parity offline substep **COMPLETE / POSITIVE**, V5DCM21 native Online integration **RUNNING / PARTIAL**. Hypothesis: previously fixed pure FC16 classifier remained mutable in separately duplicated ESPHome embedded source, risking unearned handshake state if embedded variant used. Baseline user flashed V5DCM19 FIX1 RX-only/V5DCM20 live 18m33s positive; previous 24+45+5 host tests. Controlled change: mirror exact portable `const` FC16 classifier and no mutation into only embedded `xtr_core.cpp/.hpp`, plus mandatory CI source comparison and independent C++17 object compile; no native command/payload/response, production YAML, ESP physical TX. Actual GitHub CI [39118302777](https://github.com/ryckema/Thermia_Connect_Firmware/actions/runs/39118302777) firmware `a1595e69`: embedded HPP/CPP byte-parity PASS, embedded compile PASS, 24+45+5 source tests and TX hard-deny PASS. Positive bounded criteria met; no new XTR device result, real source provenance/owner/Online remains INCONCLUSIVE. Abort/recovery not triggered. Previous V5DCM18 full original Core corpus remains PARTIAL; G01–G06 accepted. [Report](V5DCM/V5DCM21_EMBEDDED_CORE_PARITY_RESULT_20261018.md).

---

# 2026-10-18 — V5DCM21-C004 validator drift separate offline substep **COMPLETE / POSITIVE** (overall V5DCM21 native integration still RUNNING / PARTIAL). Hypothesis: Reference Core workflow red status pre-dates recent Core changes and reflects public contract expectation mismatch. Pre-change evidence Actions 39068978579 on Oct17 failed `C004_INTERFACE_NAMES`; actual data contract interfaces accept/reset/callback_binding (3), 7 rules; old validator expected 2,4. **One controlled change:** `tools/validate_xtr_portable_contracts.py` expected counts/names only; no response code, Core, parser, firmware/production YAML or TX. Commit `1067f49b`; mandatory original reference workflow Actions **39117997136 SUCCESS**, contract **18/18** with all following C++/Python validation stages PASS. Positive scoped maintenance criteria met; no semantic local XTR acceptance asserted, no physical TX, abort/recovery not triggered. Keep prior V5DCM21 FC16/ref tests, V5DCM18 full Python 7-corpus replay PARTIAL and G01–G06 accepted. [Report](V5DCM/V5DCM21_C004_REFERENCE_WORKFLOW_RECONCILIATION_20261018.md).

---

# 2026-10-18 — V5DCM21-GENERATION-FC16: offline controlled source correction **COMPLETE / POSITIVE**, overall native DCM integration **RUNNING / PARTIAL**. Hypothesis: a CRC-valid native FC16 classification must not promote handshake and local RX continuity generation must reset on source/CRC/FC23/bus-return without pretending physical authority. Baseline V5DCM19 FIX1 user-flashed RX-only + V5DCM20 18m33s positive, previous V5DCM21 22+43+5 CI, accepted G01–G06. Change only portable Core `fc16_decision` to `const` (remove pre-commit handshake promotion), RX join local generation and corresponding tests; no public security responder, YAML, production flash or TX payload. Source at firmware HEAD `a2042fc2`; mandatory CI [39117672490](https://github.com/ryckema/Thermia_Connect_Firmware/actions/runs/39117672490) actual C++17 PASS 24 readiness/classification, 45 RX join, Python 5 and TX hard-deny PASS. Negative conditions (inadvertent Core acceptance/owner promotion or transmission) not observed in fixture suite; exact deployed FIX1 callback, real epoch/owner/slot/runtime and native Online remain INCONCLUSIVE. Abort if hard-deny drops, private code appears, or unwanted TX; none. Full V5DCM18 original replay PARTIAL. Separate pre-existing Reference-core C004 contract-validator failure Oct17 persists, not caused/fixed by this change. [Report](V5DCM/V5DCM21_OBSERVATION_GENERATION_AND_PURE_FC16_RESULT_20261018.md).

---

# 2026-10-18 — READ-V31-OPTIONAL-AUDIT — PREPARED / NOT RUN for correction. Offline review only (no actual experiment execution): v31-alpha01 FIX1 code and native capability flags checked against requested conditional optional hardware behavior. Baseline unchanged v31 cleaned candidate; latest physically verified V5DCM19 FIX1. Hypothesis for next controlled source change: strict per-feature gating with fresh `0533` pool, `0534` shunt1, `0535` shunt2, `0536` buffer can suppress absent/unknown optional values without deleting native raw-register evidence. Current source check NEGATIVE for full feature requirement, not a negative on-device test: pool run/demand and raw values still publish independently of cap; HA disabled_by_default cannot enable itself dynamically. Positive future: correct absent/unknown/ON behavior, all unique register decodes and RX health retained; negative: fake present values, lost raw evidence or TX; abort if stale/invalid flag, YAML/compiler failures or bus health loss; revert v31 YAML to current FIX1. No live execution, no YAML commit. [Source audit](../Read-only/Thermia%20itec%20XTR/V31_OPTIONAL_CAPABILITY_AUDIT_20261018.md).

---

# 2026-10-18 — V5DCM21 capture replay/provenance substep COMPLETE / POSITIVE offline, overall RUNNING / PARTIAL. Hypothesis one CRC-validated geometric observer can reproduce known collaborator partial cold sequences without session or TX promotion. Baseline flashed V5DCM19 FIX1 RX-only (V5DCM20 positive 18m33s) and previously committed 22+43 offline tests; G01–G06 accepted. One controlled change new read-only capture replay Python + five synthetic cases in firmware, CI run 39116725303 at `e39b8110`, PASS with existing 22 and 43. Actual supplied `itec_eco5_gateway_20260926.log` 10719 CRC valid max28/32, Sep28 9174 valid max24/32; Oct03 2687 valid incomplete excerpt max0/32 (no 03E8/count14, not the full historic 32/32 archive). Positive parity with prior Eco5 cross-model results, no physical actions. **Inconclusive:** exact deployed FIX1 YAML not found in recursive current GitHub tree, byte identity unknown, native XTR controller acceptance/owner/slot/Online unproven. Negative/abort no new physical action; recovery keep FIX1. Next source provenance gate before production wiring. [Report](V5DCM/V5DCM21_CAPTURE_PROVENANCE_AND_RX_REPLAY_20261018.md).

---

# 2026-10-18 — READ-V31-CLEANUP — PREPARED / NOT RUN (no live test). Hypothesis: the user-approved R1–R11 redundant HA entity removals can be implemented without losing unique native XTR parameters or compromising bus receive health. Verified prior source baseline: public v31-alpha01 derived from v30-alpha12; actual deployed known-good V5DCM19 FIX1 not modified; R1/R11 alarm-only, R2 0539 ambiguous interpretation, R3 duplicate capability summary, R4–R6 comparison-only, R7/R8 hide-only, R9/R10 ESP metadata. One scoped offline change set: user-approved R1–R11. Target native observation paths retained: 0x0F FC16 pages 0532 (0533–0536 option gates, 0539 RAW), 0820, 080C, 07D0 and v29 direct status/temperature streams; no target writes or payload/TX. Offline positive: exactly 50 named entities removed, 3 default-disabled, all C++ id() refs/substitutions resolve, DE OFF, no configured TX pin, CRC/frame health bookkeeping remains. Offline negative: duplicate ID, dangling ref, removed unique value or added UART write; pending live outcome **INCONCLUSIVE / NOT RUN**, not promoted to complete. Abort if strict YAML parse/compile fails or future live TX/bus-health regression; recovery pre-change v31 blob `d81bd7673ae33d4e51460e81e18fb0e425c86c4d` or independently verified deployed production. Evidence: [source audit](../Read-only/Thermia%20itec%20XTR/V31_R1_R11_CLEANUP_AUDIT_20261018.md), [full 250-entity list](../Read-only/Thermia%20itec%20XTR/V31_ENTITY_INVENTORY_20261018.md), source commits `1ba0a5a0`, `2f876fed`. YAML and docs committed; no flash, bus TX or semantic setting writes.

---

# 2026-10-18 V5DCM21 RX-path integration CI substep — COMPLETE / POSITIVE; overall V5DCM21 RUNNING / PARTIAL. Hypothesis single existing CRC/boundary-validated RX frame stream can feed native session diagnostics without second parser, unearned session claim or TX. Baseline verified flashed V5DCM19 FIX1 RX-only and V5DCM20 18m33s stable; previous 22/22 readiness gate. Single controlled change family source-only `xtr_v5dcm21_rx_join.hpp`+test+mandatory workflow; no production YAML or device change. Targets passive slave 0x0F FC16 page geometry/ordered 32-page cold reference, generic FC23 presence, bus-return/integrity invalidation; **no TX payload**. Actual GitHub Actions 39115058751 commit `1c045872`: actual C++17 compile PASS, 22 readiness checks PASS, 43 RX-join checks PASS, static hard-deny PASS. Real physical provenance/session/UI/runtime and wired FIX1 callback remain INCONCLUSIVE. No abort trigger, no rollback needed. V5DCM18 original replay and G01–G06 unchanged. [Full evidence](V5DCM/V5DCM21_PASSIVE_RX_JOIN_CI_RESULT_20261018.md).

---

# 2026-10-18 — READ-V31-ENTITY-AUDIT — SOURCE INVENTORY ONLY; v31 live build remains PREPARED / NOT RUN. Exact v31 YAML entity enumeration: 300 named, 92 enabled, 178 disabled by default, 30 internal; exposed text sensor `Active Mapped Faults` conflicts with exclusion requirement and is documented but not yet changed. No compile/flash, no TX, no new native-register proof. [Inventory](../Read-only/Thermia%20itec%20XTR/V31_ENTITY_INVENTORY_20261018.md).

---

# 2026-10-18 — V5DCM21 source-backed CI regression substep **COMPLETE / POSITIVE**, V5DCM21 integration overall **RUNNING / PARTIAL**. Hypothesis: explicit source/session epoch/path provenance prevents offline gate from promoting denied/stale Core states. Baseline V5DCM19 FIX1 RX-only / V5DCM20 18m33s positive. Controlled change only V5DCM21 readiness evaluator, host test, required CI workflow on actual firmware HEAD `1ca3cf60`, not ESPHome production. Evidence GitHub run 39114268008: g++ -std=c++17 -O0 -Wall -Wextra -Werror -pedantic compile PASS, program outputs 22 assertions PASS, source TX hard-deny PASS. Positive verified for host source; controller epoch revocation and cold/retained/recovery checks pass as synthetic/offline fixtures; physical native DCM acceptance, evidence source and real runtime join INCONCLUSIVE. No physical TX or live action, no abort/recovery. Keep V5DCM18 original replay partial and G01–G06 accepted. [Report](V5DCM/V5DCM21_HEAD_REGRESSION_RESULT_20261018.md).

---

# 2026-10-18 — READ-V31 full coverage source inventory audit, PREPARED / NOT RUN. Direct review of `Thermia_Connect_Firmware/parameters/ALL_PARAMETERS_ACCESS_MATRIX.csv` shows 564 firmware register rows, 524 with XTR 2.4.2 profile=YES (468 firmware write-capable, 56 runtime read-only) and 40 other-profile-only; these are schema entries, NOT 524 local XTR bus-proven readings. v31 is to inventory ALL 524, not only 46 INFO / 24 SERVICE name matches; the 494 UNCONFIRMED entries need classification, not exclusion. Every observed XTR register should be decoded or exposed RAW as read-only diagnostic unless calendar/alarm excluded, with option guards, freshness and no fabricated semantic values. No new YAML/flash/TX. [Coverage contract](../Read-only/Thermia%20itec%20XTR/V31_ALL_PARAMETERS_COVERAGE_CONTRACT_20261018.md).

---

# 2026-10-18 — READ-V31-MENU: PREPARED / NOT RUN, **documentation-only**, not a physical experiment. Inputs: commissioning manual AWIXT01CG0210 user photos and normalized manual index; compare to v31-alpha01 and firmware reviewed menu tables. Controlled change: new source hierarchy [Manual hierarchy](../Read-only/Thermia%20itec%20XTR/V31_MANUAL_MENU_STRUCTURE_20261018.md); no YAML/TX and no register proof. Positive future criterion: exhaustive INFO/SERVICE inventory mapped to qualified HA entities or transparently unknown; negative: unsupported/menu-only parameter incorrectly presented as proven; inconclusive: missing native correlation. Rollback: retain v31-alpha01 and verified production unchanged. No new on-device result.

---

# 2026-10-18 V5DCM21 RUNNING / PARTIAL follow-up. Hypothesis: pure passive Core snapshot does not confer ownership or alter session. Baseline known-good flashed V5DCM19 FIX1, V5DCM20 positive, V5DCM21 readiness gate initial files. Controlled change firmware header only: read-only observer seam `portable/xtr_v5dcm21_observer.hpp` (`94720084`). Locally compiled/executed reconstructed Core-header/evaluator/test fixture g++ C++17 -Wall -Wextra -Werror -pedantic PASS (exit 0); GitHub clone unavailable so exact checkout and observer compilation NOT VERIFIED. Positive limited fixture syntax/assertions; full actual-HEAD integration INCONCLUSIVE, status PARTIAL. No physical TX, flash, YAML, sensitive responder or rollback needed; abort conditions unchanged. Next test actual HEAD including observer and current state/epoch revocation. [Report](V5DCM/V5DCM21_OFFLINE_COMPILE_AND_OBSERVER_PARTIAL_20261018.md).

---

# 2026-10-18 — READ-V31-01 — PREPARED / NOT RUN (source candidate, no live experiment). Baseline public v29 and firmware-repo public v30-alpha12, separate from verified live V5DCM19 FIX1. Hypothesis: passive alpha12 decoder can be packaged as full-monitoring alpha without TX and with HA alarm/calendar exclusion plus opt-in optional hardware entities. Controlled source change: alarm/fault/calendar entities set internal, eight optional circuit entities set disabled_by_default, no decoder change. Target reads: existing native pages including 0532 capabilities (0533 pool, 0534 shunt group1, 0535 group2, 0536 buffer). Positive future validation: HA no alarm/calendar entries, conditional availability, normal v29 core readings, no physical TX, CRC/parser health stable. Negative: core entity regression or unexpected TX; inconclusive: optional feature not active/no native page. Abort: no flash if static/compile fails; for live issue revert to verified production image. Evidence so far: static duplicate ID/substitution/TX pin review only; NOT compiled/flashed or executed. [Scope](../Read-only/Thermia%20itec%20XTR/V31_FULL_MONITORING_SCOPE.md).

---

# 2026-10-18 V5DCM21 RUNNING / PARTIAL — offline source addition, not live experiment. Baseline V5DCM19 FIX1 RX-only, V5DCM20 18m33s positive. Controlled change two separate portable firmware files containing pure independent readiness evaluator and regression assertions, commit `8dc5918d63967dc53f500fb637f92d7cda1902b2`. Test scenario names: default denial; internal accepted without ownership; 5 physical ownership prerequisites; profile+required packages; 32-page cold reference; retained cold false; service qualified; semantic receipt; unhealthy denial. **Tests authored but compile/run not verified**; no Core, YAML, ESP change; physical TX zero by design. Positive criteria test execution, source provenance and safe observer integration pending; negative/inconclusive until then. Abort on real TX or unintended mutation, recovery discard new isolated files. G01-G06 stay accepted.

---

# 2026-10-18 V5DCM21 PREPARED / NOT RUN — offline native DCM functional/TX-readiness contract. Hypothesis: independent handshake, physical ownership, cold/retained config and application readiness prevent accidental authority promotion. Known-good live V5DCM19 FIX1, V5DCM20 positive; V4.1 EXP386/387 positive, EXP388 partial, V5DCM18 full reference replay partial. Single change documentation/next audit only; target 0x0F FC23 classification, FC16 page ownership, service lifecycle without TX payload. Positive: traceable source/owner matrix and denied-event tests; negative: unowned/unknown frame may grant ACK; inconclusive: unresolved provenance. Abort any TX/private publication, recovery unchanged RX-only. No result yet. [Contract](V5DCM/V5DCM21_TX_READINESS_CONTRACT_PREPARED_20261018.md).

---

# 2026-10-18 V5DCM20 RESULT COMPLETE / POSITIVE for original roadmap live passive duration, NOT original host-only 24/24 partial. Hypothesis stable parser/HA RX with no TX across 10+min. Baseline flashed V5DCM19 FIX1, prior 189-second positive and 11/1 initial resync/fault. Only controlled variable longer observation, no controller restart/write/YAML. User provided thermia-exp86-20261018-013151.log 01:31:52-01:50:25 (18m33s). 37 triplet diagnostic cycles, B11C 6677->15885 parity countDiff=byteDiff=0, B11D 6670->15880 parity zero faults, V5 frames 6590->16050, resync 11->11, RX integrity 1->1, drops 0, 2619/2619 TX candidates denied physical_attempts=0. Fan OFF->ON, compressor ON mid-run, selected NaNs observed; semantic cause unknown. Positive criteria met; negative/abort physical TX, parser divergence, production telemetry stop absent; no recovery. No new genuine DCM session acceptance claimed. G01-G06 not reopened.

[Full result](V5DCM/V5DCM20_LIVE_RX_ONLY_RESULT_20261018.md).

---

# V5DCM20 PREPARED / NOT RUN (2026-10-18), roadmap experiment distinct from earlier isolated host C++ 24/24. Hypothesis: current FIX1 stable under 10-minute passive observation, no parser regression or TX. Baseline V5DCM19 live 1566/1566 B11C, 1564/1564 B11D, zero differences, 11 stable earlier resync and 1 historical integrity fault, physical TX zero. Controlled change observation duration ONLY. Positive zero new differences/drops/TX and HA telemetry stays live. Negative integrity growth or production regression. Abort unexpected TX or critical regression. Recovery retain known-good existing FIX1. Result NOT YET RECEIVED. Report: V5DCM/V5DCM20_LIVE_RX_ONLY_PREPARED_20261018.md

---

# 2026-10-18 V5DCM19 FIX1 RESULT COMPLETE / POSITIVE scoped RX-only. Hypothesis: integrate V5DCM1/2 joined passive diagnostics with no production regression. Baseline RX-only deployed; controlled change FIX1 merges new 30s interval into existing interval key, no TX. User confirmed flashed, 01:19:09–01:22:18 live log. Six NATIVE_OBSERVE/SERVICE_OBSERVE/PROVENANCE groups printed. B11C parity 1566/1566, B11D 1564/1564 and zero delta, HA values healthy, 266 denied candidates and zero physical attempts; historical resync 11 and integrity 1 no observed increment. Positive criteria met; native acceptance not tested. Abort for unauthorized TX or production fault not triggered; recovery none. G01–G06 accepted risks preserved.

[Result](V5DCM/V5DCM19_FIX1_LIVE_RESULT_20261018.md).

---

# 2026-10-18 — V5DCM19 FIX1 duplicate interval repair

PREPARED / NOT RUN. User detected YAML issue. Actual original V5DCM19 contained two top-level `interval:` keys. Controlled correction: merge new diagnostics into existing interval list, no other source changes. Strict duplicate-map YAML parse PASS, 16 scheduled entries and one V5DCM19 diagnostic; no ESPHome compile or live installation. Previous claimed 8/8 checks insufficient. Abort unexpected missing intervals/TX; rollback deployed V5DCM2 FIX1. [Report](V5DCM/V5DCM19_FIX1_DUPLICATE_INTERVAL_20261018.md).

---

# 2026-10-18 — V5DCM19 RX-only integration candidate

PREPARED / NOT RUN. Hypothesis: join existing V5DCM1/2 observer diagnostics without rebuilding parser. Baseline archived prepared ZIP; production FIX1 byte-parity unknown. Controlled change header and logging interval only. 8/8 limited offline syntax/source checks PASS, no ESPHome compile/live test. Positive live criteria unchanged HA production entities, [V5DCM19] logs and no TX. Abort unexpected TX or sensor regression; rollback true deployed FIX1. G01–G06 not reopened. [Report](V5DCM/V5DCM19_PREPARED_RX_DIAGNOSTIC_20261018.md).

---

# 2026-10-18 — V5DCM18 function-first correction and V4.1 handoff

**RUNNING / PARTIAL overall; COMPLETE / POSITIVE scoped gap-inventory step.** Hypothesis: original CM930 firmware semantics plus locally validated Write V4.1 outcomes and existing V5 modules yield a concrete V5DCM19 implementation contract, avoiding redundant tests. Baseline V5DCM16–18 offline capture work, historical Write V4.1 EXP386/387 positive EXP388 partial, V5DCM1/2 and Python portable Core; G01–G06 accepted. Controlled change **source-only** direct matrix of challenge/parser, R1 response, handshake statuses, cold/retained bootstrap, 0708 service, runtime, profile completeness and icon/Online evidence. Positive: explicit KEEP/JOIN/MISSING/DEFER worklist created. **Unknown:** original Python seven-fixture suite NOT EXECUTED; full end-to-end V5DCM18 replay still open. No new bus activity, flash or experimental YAML. [Full mapping](V5DCM/V5DCM18_FUNCTIONAL_GAP_HANDOFF_20261018.md).

---
# 2026-10-18 — V5DCM18 direct rerun of strict capture replay and user-ZIP C++ Core

**RUNNING / PARTIAL overall.** Hypothesis: bounded replay is stable on previous authentic capture corpus and positive user ZIP Core; baseline prior GAP51/V5DCM16-18, genuine Write V4.1 EXP386/387 positive, EXP388 partial. Controlled change: g++ host test recompilation + strictly bounded replay of 7 logs only. **17/17 C++ original ZIP stateful checks PASS**; Oct-03 one 32/32 strict run, Eco5 max 28 and 24; drop 03FC, interrupt 45–65 s and CRC modification correctly eliminate false complete. Previously naive count of 7 full runs rejected. Positive for bounded checks; full reference Python corpus and V4.1 state parity NOT EXECUTED and remain OPEN; no physical TX/ESPHome change, rollback N/A. G01–G06 accepted risks unchanged. [Report](V5DCM/V5DCM18_VERIFIED_OFFLINE_RESULT_20261018.md).

---
# 2026-10-18 — V5DCM18 integrated offline observer/corpus replay

**RUNNING / PARTIAL.** Baseline GAP51 + V5DCM4–8, previous 17/17 ZIP-Core C++ stateful checks. Controlled change: host-only integrated C++ V5DCM1/V5DCM2 + portable decoding and bounded offline source-capture replay, no native TX or original code modifications. 25,031 CRC-valid frames; 164 exact FC23 request shapes, 7 reply shapes. Initial naïve counter mistakenly returned 7 full bootstrap sequences; discarded. Corrected replay exactly 1 full 32-page Oct-03 session, Eco5 longest 28/24. Injected absent 03FC -> 0 full; remove midbootstrap frames -> 16/32; CRC corruption rejected; duplicated challenge did not add full session. Full Python original Core end-to-end tests still NOT executed; not COMPLETE. Positive for bounded observer replay, negative for initial naïve counter (fixed in analysis), abort no bus TX, recovery none. G01–G06 accepted decisions preserved. [Report](V5DCM/V5DCM18_INTEGRATED_OBSERVER_REPLAY_20261018.md).

---
# 2026-10-17 — V5DCM18 offline C++ 7-capture coverage continuation

**RUNNING / PARTIAL.** Hypothesis: ZIP-Core direct C++ decoder/decision traversal can identify missing pipeline coverage without revalidating G01–G06. Baseline 17/17 ZIP-Core stateful host tests and historical passive 25,031-frame replay. Controlled change only standalone noncommitting C++17 traversal over 7 original text logs. Actual compile and execution exit 0: 25,031 frames, FC16 requests 2,500, ACKs 1,365, FC23 raw 171 (independently 164 req/7 response), uncommitted FC16 decision candidates 216 yes/2,284 no. ZIP-Core Kind intentionally lacks FC23; existing V5DCM2 observer covers. Positive for bounded audit; full stateful end-to-end still open; no production changes/TX; recovery N/A. [Report](V5DCM/V5DCM18_CPP_CORPUS_BRIDGE_20261017.md).

---
# 2026-10-17 — V5DCM18 continued: six additional ZIP portable C++ regression checks

**RUNNING / PARTIAL** original V5DCM18. Baseline previous 11/11 C++ regression on user ZIP Core; controlled change only six more standalone host assertions (epoch-stale, cross-Core ticket, frame mutation, qualified runtime, authority revoke, recovery). Actual g++ -std=c++17 compile and local run: **17/17 PASS**, 0 fail; no bus, no original Core changes. ZIP differs from Github HEAD; full original-Python-Core genuine-corpus replay still OPEN. Abort TX/prod mutation; rollback N/A. [Report](V5DCM/V5DCM18_EXTENDED_CPP_17_PASS_20261017.md).

---
# 2026-10-17 — V5DCM18 ZIP portable C++ regression and source divergence

**RUNNING / PARTIAL.** Baseline original-roadmap 25,031 historical passive frames and 49/49 structural checks, V5DCM2 FIX1 RX-only. Controlled offline variable: compile and execute 11 negative/positive native C++ Core assertions using user-supplied V5DCM2 ZIP source. **RESULT 11/11 PASS**. Tests cover denied/out-of-order FC16, first owned page, repeated commit, revoked ticket, 32-page ordered bootstrap and reset. **Blocking discrepancy:** ZIP Core has provenance/ticket APIs absent in current firmware repo HEAD; tests do NOT validate repo HEAD or full corpus integrated reference replay. No ESPHome compile, flash, bus TX. Recovery no changes. [Report](V5DCM/V5DCM18_CPP_ZIP_SOURCE_DIVERGENCE_20261017.md).

---

# 2026-10-17 — V5DCM18 test expectation correction

**RUNNING / PARTIAL**: Corrected original-Core adverse-test assertion to distinguish original CM930 internal FC16 acceptance from emulator TX owner. Added failure exit code for genuine failed assertions in the existing GitHub CI workflow. This is a test-only change, not a model fix or replay result. Baseline earlier V5DCM18 limited capture replay and pending original-Core CI verification. Positive only when original Core/corpus tests actually run and results reviewed. No new physical TX or production modification; rollback revert test code. [Details](V5DCM/V5DCM18_ROADMAP_CI_ASSERTION_FIX_20261017.md).

---

# 2026-10-17 — V5DCM18 original reference Core adverse replay instrumentation

**RUNNING / PARTIAL**: Based on V5DCM16/17 and limited 49/49 structural V5DCM18 observation checks, added offline [test_v5dcm18_roadmap_faults.py](https://github.com/ryckema/Thermia_Connect_Firmware/blob/main/tools/test_v5dcm18_roadmap_faults.py) to reference firmware repository and wired it into existing GitHub workflow. Only controlled variable new test source and CI call, no original Core logic or HA production changed. Scenarios denied first page, expected bootstrap vs missing page, repeated acknowledgement state, fresh reset, and full 32-page run. Original source unambiguously allows internal Accepted from a subsequently denied FC16; whether this violates external owner/TX invariant must be separately tested. **Outcome:** CI execution/result not retrieved; success/negative not yet certified. Abort no bus TX/private credentials; recovery remove CI test. [Report](V5DCM/V5DCM18_STATEFUL_CORE_CI_PREPARED_20261017.md).

---

# 2026-10-17 — V5DCM18 original roadmap replay follow-up

**RUNNING / PARTIAL**; earlier same-number source/API audit preserved, does not fulfil original V5DCM18 criteria. Hypothesis: bounded historical replay with missing page, duplicate challenge, truncated session and unexpected invalid ACK detects illegitimate inferred acceptance. Baseline V5DCM16/17, original reference Core tests (inspected but NOT executed), deployed V5DCM2 FIX1 RX-only. Controlled modification passive analysis only. 25,031/25,031 CRC good, 164 challenge shapes, 7 bounded pairs, 1 full strict 32-page Oct-03; 49/49 conservative structural checks PASS. These checks deliberately deny native acceptance, do NOT test stateful original Core. Full positive condition NOT MET. No TX, abort not triggered, rollback N/A. [Details](V5DCM/V5DCM18_ROADMAP_REPLAY_PARTIAL_20261017.md).

---

# 2026-10-17 — V5DCM20 isolated C++ contract, partial

**V5DCM20 — RUNNING / PARTIAL.** Hypothesis: observation and authorization must be separate from handshake commit. Baseline V5DCM18 source/API audit and V5DCM19 15/15 Python tests; live V5DCM2 FIX1 RX-only. Controlled change standalone non-transmitting C++17 test only. Result 24/24 assertions PASS under g++ strict warnings: denied source/epoch/session and invalid shape do not promote isolated handshake; positive is synthetic injected authorization only. Actual portable Core change BLOCKED / NOT APPLIED; no integrated tests or physical session proof. Positive standalone criterion met, integrated criterion unmet, negative none; abort on restricted source write triggered; recovery no modification to original Core or live system. [Details](V5DCM/V5DCM20_ISOLATED_CPP_PARTIAL_20261017.md).

---

# 2026-10-17 — V5DCM19 offline contract tests

**V5DCM19 COMPLETE / POSITIVE (15/15 synthetic offline Python tests), INCONCLUSIVE for actual C++/XTR parity.** Baseline V5DCM18 and RX-only FIX1. One controlled change: isolated test-only observe/authorize/commit Python contract; no native TX or ESPHome changes. Denied frames do not promote acceptance in this model, with separately guarded mailbox and readiness. Positive tests passed; negative promotion not observed; abort on any physical TX or unsafe claim; recovery discard offline fixtures. V5DCM20 PREPARED / NOT RUN: offline C++ source-level refactor/tests. [Report](V5DCM/V5DCM19_OBSERVE_AUTHORIZE_COMMIT_OFFLINE_20261017.md).

---

# 2026-10-17 — V5DCM18 firmware/Core API parity

**V5DCM18 — COMPLETE / POSITIVE for offline source discrepancies, INCONCLUSIVE local session.** Hypothesis: original CM930 source-derived lifecycle vs public portable V5 Core has actionable API/transition mismatch. Baseline V5DCM17, user-flashed V5DCM2 FIX1 RX-only, CM930 axes/transition tables and GAP53. Controlled source audit only: xtr_core.hpp/.cpp, xtr_adapter.cpp, xtr_frame.cpp, xtr_platform.cpp; NO YAML/TX/flash/compile. Observed: fc16_decision changes handshake to Accepted before authorization; qualify_handshake has no evidence token; set_mailbox and mailbox_decision rely on externally-qualified context; write_ready combines mailbox+runtime+no pending txn, not full profile/package/source/physical-slot proof; fixed local 03E8/count14 differs historical 03E8/count13; cache ingest separates observed data from write_base but depends on externally sourced epoch; adapter end_of_frame is supplied externally; platform validates CRC/response class, not DE-level bus authority. No real runtime parity test performed. **Conclusion:** implement fail-closed observation-versus-authorized-commit contract before new TX experiments. Positive exact source discrepancies MET, negative none, abort private disclosure/unsafe TX not triggered, recovery production unchanged. V5DCM19 PREPARED/NOT RUN offline contract tests. [Report](V5DCM/V5DCM18_SOURCE_API_PARITY_20261017.md).

---

# 2026-10-17 — V5DCM17 CM930 lifecycle-gate reconciliation

**V5DCM17 — COMPLETE / POSITIVE (9/9 bounded static source consistency checks), COMPLETE / INCONCLUSIVE for real XTR native acceptance.** Hypothesis: reconcile V5DCM16 historical FC23/FC16 chronology against original Connect firmware readiness gates and existing GAP51–53 findings to identify new engineering work rather than repeating passive observers. Baseline V5DCM16, 15A, CM930 orthogonal axes/gates, existing GAP53. Controlled change offline source/static assertions only, no bus/YAML/TX. **Observed:** firmware gates G1..G11 distinguish FC23 response, later qualified approval, bootstrap, mailbox, version-selected profile, subscribed package receipt, full operation, safety/ownership; historical Oct-03 request/reply-shape + 32 starts supplies chronology only. Nine applicable source checks pass; one unrelated literal-phrase assertion failed and was excluded from the applicable checks (not a protocol contradiction). Locally captured `03E8/count14` and historical `03E8/count13` remain distinct. **Conclusion:** first missing component is provenance-aware transition contract and implementation parity across CM930/V4.1/V5; owner/epoch/EOF/profile/app acceptance remain UNKNOWN, TX false. Positive static gate map met; negative genuine session acceptance not asserted; abort TX/unsupported promotion/private leakage; recovery discard offline report, FIX1 unchanged. V5DCM18 PREPARED/NOT RUN: offline source/API parity audit. [Full report](V5DCM/V5DCM17_LIFECYCLE_GATES_OFFLINE_20261017.md).

---

# 2026-10-17 — V5DCM16 genuine/collaborator historical session replay

**V5DCM16 — COMPLETE / POSITIVE for bounded offline replay (14/14 assertions); COMPLETE / INCONCLUSIVE for real XTR native DCM acceptance.** Hypothesis: original verified RAUC 2.0.18 and 2.1.105 flags-map parity (V5DCM15A) and historical FC23/config frames allow a cautious chronological session candidate reconstruction. Baseline V5DCM4–8, V5DCM13–15A; live V5DCM2 FIX1 RX-only. Controlled change: offline CRC+FC23 shape and time correlation, 200ms pairing and strict reference start ordering in seven historical/cooperator text logs, NO UART/TX/YAML. **Observed:** 25,031 good CRC records; 164 exact native 0x0F FC23 challenge-shaped requests; 7 bounded response-shaped pairs, 157 unpaired in-window (not proof failed protocol). Oct-03 27.400→27.429s (29ms), first 03E8 reference page at 29.262s (1.833s after reply), 32-reference-start sequence until 61.461s (32.199s). Eco5 Sep26 99 requests/2 pairs 61,63ms; Sep28 64/4 pairs 46,30,32,47ms; no strict full 32-reference runs (model criterion only). Sep25 09:05 longest 31 starts. Independently proven profile, sender, epoch, EOF, owner, acceptance, Online remain UNKNOWN; TX false. Positive all replay/guards pass; negative mismatches none; abort physical TX, secret leakage or acceptance/slot overclaim; recovery offline discard, live FIX1 unchanged. V5DCM17 PREPARED / NOT RUN: offline app state lifecycle, consult existing GAP51–53. [Report](V5DCM/V5DCM16_HISTORICAL_SESSION_REPLAY_20261017.md).

---

# 2026-10-17 — V5DCM15A original 2.1.105 CM930 profile extraction

**V5DCM15A — COMPLETE / POSITIVE (16/16 offline extraction/source checks); COMPLETE / INCONCLUSIVE (local selected XTR profile/native DCM).** Hypothesis: direct original 2.1.105 RAUC config resolves old-vs-new flag-map identity left open by V5DCM13. Baseline 13–15, V5DCM10 RAUC provenance and deployed V5DCM2 FIX1 RX-only. Controlled change: offline SquashFS→ext4 and read JSON from new appfs `/etc/device-client.d/930`; compare old original JSON and inspect 2.1.105 `configuration.py` and CM930 version-selection code. Results: new/old `modbus-flags.json` byte identical, 3333 bytes SHA256 bb0b335eaf4e3a98e5d71d1cd1551e0772fedcfcd3f7d17f3c78e04c21844b9e; original request flag 16+16+11; CM930 profile JSON count 33 old/35 new, 25 shared paths, 8 unchanged, 17 changed; 2.3.0–2.4.1 profile range extended to 2.3.0–2.4.3. Source confirms profile selector takes observed CM firmware SemVer, whose local XTR value remains UNKNOWN. Positive original JSON and source equality check achieved; negative no mismatch; abort private code exposure or TX, none; recovery none (offline). No ESPHome build/flash. Next V5DCM16 PREPARED/NOT RUN historical provenance/profile-aware FC23 replay. [Full report](V5DCM/V5DCM15A_RAUC_21105_CONFIG_AUDIT_20261017.md).

---

# 2026-10-17 — V5DCM13–15 consecutive offline results (newest first)

**V5DCM15 — COMPLETE/POSITIVE synthetic offline; INCONCLUSIVE vendor parity.** Hypothesis: separated challenge, observed page, selected required packet, package-received, native acceptance and cloud/display prevent false positives. Baseline V5DCM8/11 and V5DCM2 FIX1. Controlled new standalone no-I/O Python observer; 18/18 combined source and synthetic fixtures PASS; no replay of physical XTR acceptance. Positive no premature TX/acceptance; negative no failure observed in tests; abort any physical TX/semantic promotion; recovery offline discard. [Details](V5DCM/V5DCM15_FAIL_CLOSED_SESSION_MODEL_20261017.md).

**V5DCM14 — COMPLETE/POSITIVE source dependency; INCONCLUSIVE XTR required mask.** Hypothesis: 2.1.105 application derives requested packages from parser significant_registers, not every 43 defined bit. Baseline V5DCM11-13. Controlled AST source inspection; `_get_all_data_package_to_request`, request=True mapping and data_package_received paths present. Positive grounded software selection path; negative chosen XTR parser and actual data set cannot be derived; abort spurious requirement or any TX; recovery none. [Details](V5DCM/V5DCM14_REQUIRED_PACKAGE_SELECTION_AUDIT_20261017.md).

**V5DCM13 — COMPLETE/POSITIVE original Connect 2.0.18 map; RUNNING/PARTIAL for 2.1.105 original JSON check.** Hypothesis: earlier derived 43-bit map equals original firmware JSON. Baseline V5DCM12. Controlled read of appfs_2018.zip verified by V5DCM10: direct `conf/930/modbus-flags.json` SHA256 bb0b335eaf4e3a98e5d71d1cd1551e0772fedcfcd3f7d17f3c78e04c21844b9e; 43/43 exact range matches request words 1802=16/1803=16/1804=11. New 2.1.105 ext4 config not independently extracted; do not promote to matching new image. Positive old identity, negative none old, abort assuming cross-version identity; recovery none. [Details](V5DCM/V5DCM13_ORIGINAL_FLAGS_AUDIT_20261017.md).

**V5DCM16 — PREPARED / NOT RUN:** offline historical native session reconstruction; no TX. Production V5DCM2 FIX1 unchanged. User artifact V5DCM13_15_OFFLINE_20261017.zip includes audit.py, README.md, RESULTS.json.

---

# 2026-10-17 — V5DCM12 offline request-bit mapping

**V5DCM12 — COMPLETE / POSITIVE (14/14 offline mapping tests); COMPLETE / INCONCLUSIVE (actual XTR DCM readiness).** Hypothesis: join genuine firmware CM930 package request-words and existing derived flag ranges with historical FC16 frame starts without falsely inferring received packages. Baseline V5DCM11 source readiness, V5DCM4–8 captures, user-installed V5DCM2 FIX1 RX-only. Controlled change standalone offline Python map and replay, no YAML/TX. Original RAUC 2.1.105 source contains 1802/070A, 1803/070B, 1804/070C request words, flags-JSON-dependent mapping, and received-event-dependent completion. Existing firmware repo derived cm930_modbus_flags_map.csv provides 16+16+11 candidate ranges; original selected profile flags JSON not reverified in this experiment. Of 3,063 prior normalized native rows, historical Oct-03 and Eco5 Sep-26 touch 43 distinct candidate range bits, Eco5 Sep-28 touches 42, others 10–40. A request-shaped FC16 does NOT prove application reception. Positive source constants and 14 safe checks pass; negative mismatches or unsupported readiness not observed; abort TX/security leak/owner overclaim; recovery none, production FIX1 untouched. V5DCM13 direct appfs flags JSON provenance PREPARED / NOT RUN. [Report](V5DCM/V5DCM12_REQUEST_PACKAGE_MAP_OFFLINE_20261017.md).

---

# 2026-10-17 — V5DCM11 firmware readiness gate (offline)

**V5DCM11 — COMPLETE / POSITIVE for version-scoped AST and ten isolated synthetic tests; COMPLETE / INCONCLUSIVE for genuine XTR DCM acceptance.** Hypothesis: original Connect RAUC 2.1.105 (device_client 0.2.8) contains an application packet-readiness/publication gate absent from examined 2.0.18 (device_client 0.1.45), distinct from CM930 handshake state. Baseline V5DCM10 exact RAUC provenance, V5DCM8 offline fail-closed observer, and deployed V5DCM2 FIX1 RX-only. Controlled change static AST source references and separate conservative no-I/O Python witness; no ESPHome YAML, no RX/TX changes. Evidence: new `CMClientParameterUpdateState` WAIT/RECEIVED; `_on_registers_read` after version config load seeds `_get_all_data_package_to_request`; `reset_register_read_request` reports received package; `on_publish_cm_params_map_event` postpones publication until all. Empty wait set remains WAIT unless a receipt event occurs; do not interpret empty request as completed. Both versions retain FC23 reply handling and separate FC16-induced software handshake acceptance branches (firmware-derived only). Ten AST and synthetic tests PASS; no genuine capture replay or vendor code execution this experiment. Positive source-backed links and negative guards achieved; negative mismatches/false Online promotion not observed; abort any native TX or security leak; recovery none (offline). V5DCM12 source-bit-table and historical replay PREPARED / NOT RUN. [Details](V5DCM/V5DCM11_CM930_READINESS_OFFLINE_20261017.md).

---

# 2026-10-17 — V5DCM10 offline RAUC provenance and embedded source parity

**V5DCM10 — COMPLETE / POSITIVE (RAUC manifest/image/source provenance); COMPLETE / INCONCLUSIVE (XTR native handshake/display/cloud).** Hypothesis: V5DCM9 original 0.1.45 vs 0.2.8 source trees correspond exactly to actual 2.0.18 vs 2.1.105 RAUC firmware. Baseline V5DCM9 source comparison and user-tested V5DCM2 FIX1 RX-only. Controlled change: parse RAUC SquashFS v4, extract manifest and ext4 images, validate embedded SHA256/length, read appfs device_client/_version.py, compare extracted .py byte-for-byte to earlier ZIPs. **Result:** Thermia Connect 2.0.18 → appfs device_client 0.1.45 (21/21 matching modules); 2.1.105 → appfs device_client 0.2.8 (25/25); 4/4 embedded image SHA256 matches RAUC manifest; source comparison 21 shared / 16 changed / 4 added verified. Relevant 0x0F FC23 handshake and FC16 configuration are *not bus-tested here*. Positive direct chain of custody all verified; negative mismatches NONE; abort private algorithm leakage, unexpected TX, or unverified source identity; recovery none (offline only). Distinguish checksummed archive contents from unvalidated RAUC signature chain. Supersedes V5DCM9 provenance UNKNOWN, preserves V5DCM9 historical status. Next V5DCM11 offline state/readiness diff PREPARED / NOT RUN. [Details](V5DCM/V5DCM10_RAUC_PROVENANCE_VERIFIED_20261017.md).

---

# 2026-10-17 — V5DCM9 offline Connect version comparison

**V5DCM9 — COMPLETE / POSITIVE (statically verified differences); COMPLETE / INCONCLUSIVE (direct RAUC mapping / XTR native acceptance).** Hypothesis: later device_client adds package and subscription readiness handling independent of native FC23 acceptance. Baseline V5DCM8 offline fail-closed model; live V5DCM2 FIX1 RX-only. Controlled change: compare two original recovered local source snapshots only, no ESPHome or TX. Sources appfs_2018.zip internal device_client=0.1.45 (21 .py), device_client.zip internal=0.2.8 (25 .py); among 21 shared modules 16 changed; 4 added, 0 removed. New code has CMClientParameterUpdateState and _get_all_data_package_to_request; per-service subscriptions and conditional parameter mapping. No independent proof which application version is embedded in each of RAUC 2.0.18 and 2.1.105, and no claim handshake function changed. Positive static file inventory+AST/sha regression assertions PASS. Negative false version mapping or invalid diff, not observed. Abort secret publication or live TX; recovery none, deployed V5DCM2 FIX1 untouched. V5DCM10 provenance extraction PREPARED/NOT RUN. [Report](V5DCM/V5DCM9_FIRMWARE_VERSION_AUDIT_20261017.md).

---

# 2026-10-17 — V5DCM8 offline provenance observer

**V5DCM8 — COMPLETE / POSITIVE (offline replay gates); COMPLETE / INCONCLUSIVE (real XTR Online/acceptance).** Baseline V5DCM4–7 real-record audit and live V5DCM2 FIX1 RX-only. Hypothesis: separate observed challenge, response shape, 200ms time correlation, config page ordering and mailbox from independently proven epoch, owner, native acceptance, display and Online; avoid session false positives. Controlled change standalone no-I/O Python observer + replay script (no ESPHome YAML changes). 7/7 historical/collaborator files PASS: 164 exact native challenge request shapes, 7 time-correlated reply shapes, one strict 32-page configuration run; zero upgraded owner/epoch/acceptance/icon/cloud/TX flags. Positive all counter and fail-closed tests passed; negative false escalation/mismatch not observed; abort any live TX or private secret disclosure; recovery retain production FIX1 untouched. No ESPHome compilation or live test performed. Next V5DCM9 firmware version audit PREPARED/NOT RUN. [Details](V5DCM/V5DCM8_PROVENANCE_OFFLINE_20261017.md).

---

# 2026-10-17 — V5DCM4–V5DCM7 offline completed (newest first)

**V5DCM7 — COMPLETE / POSITIVE (offline falsification); INCONCLUSIVE (true session rules).** Hypothesis: mailbox 0708 and cumulative config cursor can create false positives for accepted session. Baseline V5DCM3 and stricter V5DCM6. Change offline counterexamples only. Sep-24 capture has 11 mailbox request shapes / 0 in-window exact FC23; Sep-25 09:05 mailbox first at 0.987s vs 03E8 at 68.304s / 0 in-window exact FC23. Earlier/out-of-window handshake cannot be excluded. Eco5 cumulative 32-page cursor can span non-contiguous bursts. Positive examples found; negative none within test; abort any unsupported owner/accepted inference; recovery none, live RX-only unchanged.

**V5DCM6 — COMPLETE / POSITIVE (historical ordering/count comparison); INCONCLUSIVE (required XTR sequence).** Hypothesis: historical page profiles differ and truncated records are not failed controller bootstrap. Baseline CRC-valid V5DCM4. Offline strict reference ordering only. Oct-03 32 successive reference starts 29.262–61.461s from 03E8/count13 to 06F4/count19. Sep-25 09:05 31 starts, ending 06F1/count3. Eco5 has count14 at 03E8 and count22 at 0410, unlike count13/count21 in historical profile. Positive profile differences; abort universal semantics claim; rollback none.

**V5DCM5 — COMPLETE / POSITIVE (text-record timing); INCONCLUSIVE (slot/owner/acceptance).** Hypothesis: time adjacent exact native 0x0F FC23 and reply-shaped records can be associated without proving sender. Baseline V5DCM4. Controlled offline <=200ms matching. Oct-03 27.400->27.429s 29ms. Eco5 Sep-26 99 exact challenges, 2 shaped replies/matches 61/63ms; Sep-28 64 challenges, 4 replies/matches, first 46/30/32ms; medians of request cadence ~4.2335/4.241s. Negative: unpaired challenges are recorded not protocol rejects; abort unauthorized slot claim. No live TX.

**V5DCM4 — COMPLETE / POSITIVE (real-record CRC/event replay); INCONCLUSIVE (native acceptance).** Hypothesis: seven historical/collaborator captures can be normalized into V5DCM3 events without counter mismatch. Baseline V5DCM3 synthetic 5/5. Offline only, CRC16(Modbus) decode. 25,031/25,031 captured text-record CRC valid, 7/7 frame-event counter parity, with variable capture provenance. Positive achieved; abort if CRC record evidence used to claim physical direction. Live V5DCM2 FIX1 retained.

**V5DCM8 — PREPARED / NOT RUN** offline session evidence gates and capture replay, no physical TX. Full results and explicit test criteria: [V5DCM4–7 evidence](V5DCM/V5DCM4_TO_7_OFFLINE_REPLAY_20261017.md).

---

# 2026-10-17 — V5DCM3 offline state-model result

**V5DCM3 — COMPLETE / POSITIVE for synthetic offline host test; COMPLETE / INCONCLUSIVE for genuine capture and local acceptance.** Baseline user-tested V5DCM2 FIX1. Hypothesis: configuration reference pages, mailbox directions, runtime candidates and handshake events can be tracked independently without asserting DCM acceptance. Controlled change: standalone C++17 offline observer, NO new ESPHome YAML or TX. Referenced original recovered Connect firmware in cm/modbus_server15.py and cm/client.py. Host fixtures: five scenarios PASS, g++ -std=c++17 -Wall -Wextra -Werror. Relevant slave 0x0F; known FC16 03E8/14 and 085F/5, FC23 handshake shape (not present live), FC03 0708 (not present live), runtime reference pages (not live validated). No real-capture replay. Positive = deterministic fixture counts, accepted/icon/online flags remain false. Negative = count mismatch or conflated milestones. Abort any physical TX or private security disclosure; recovery no live change, retain V5DCM2 FIX1. Next V5DCM4 offline real-capture replay. [Details](V5DCM/V5DCM3_OFFLINE_SESSION_AUDIT_20261017.md).

---

# 2026-10-17 — V5DCM2 FIX1 live log and duplicate-interval correction

**V5DCM2 FIX1 — COMPLETE / POSITIVE (diagnostic integration + RX-only monitoring); COMPLETE / INCONCLUSIVE (native FC23 handshake).** Hypothesis: passive CM930 observer output can be integrated into the user's V5 ESPHome build while retaining CRC-good RX, all production HA readings and TX=HARD_DENY. Baseline V5DCM1 installed; first V5DCM2 YAML failed YAML parsing due to duplicate top-level `interval:` key, so that version was not valid for testing. Controlled FIX1 change: merge V5DCM2 30s log under the existing `interval:` list; no new bus parser or TX code. Relevant 0x0F FC23 071C/0730 (none observed), FC16 03E8/count14 and 085F/count5 (observed), mailbox 0708 (none).

**Live evidence:** user log `Pasted text(20261017-010702).txt` shows [V5DCM2] diagnostics at 03:05:44, 03:06:14 and 03:06:44, consistent H=0, challenge=0, responseShape=0, acceptedShadow=0, cfg=1/32 complete=0 mailbox=0 runtime=0, provider=ABSENT, TX=HARD_DENY. At 03:06:45 [S8] HEALTH valid=781, fc16=127, cfg words=14, operation words=5, 085F=42, FC23=0, deltaResync=0, deltaDrops=0, DE=0. B11D raw=portable=V5 779 with 0 byte/count differences or RX faults. Live compressor 23 Hz, fan 390–400 rpm; HA data functional. UART-write and physical-TX *software counters* 0. Separate retained R6-P30EC D=4 first=STAGE_D_LEDGER_FAULT still appears without matching physical RX error; keep it unresolved, not cleared.

**Positive criteria achieved:** recognition of [V5DCM2] log, intact production data, clean RX, zero software TX. **Inconclusive criteria:** zero qualifying native FC23 so genuine request/response correlation and handshake transitions unexercised; display/cloud still unproven. **Abort:** any unplanned TX/DE, parser failures, sensor regression; none observed in this sample. **Recovery:** tested V5DCM1 or V5DCM2 FIX1; no rollback reported. Do not promote to active native DCM success. First original YAML duplicate-key error is a negative *build artifact defect*, corrected in FIX1 and not evidence about protocol.

**Next: V5DCM3 — PREPARED / NOT RUN** (offline-only firmware state-model work; no private working responder or physical TX).

---

# 2026-10-17 — V5DCM series (newest first)

**V5DCM2 — PREPARED / NOT RUN.** Hypothesis: an FC23 geometry-aware observer and explicit session diagnostics can run on the V5 validated frame stream without changing RX/TX behavior. Baseline V5DCM1 installed; controlled change challenge shape/correlation and 30-second [V5DCM2] logging, private response-provider interface without actual transform. Target slave 0x0F FC23 write 071C/8, read 0730/8; ongoing 03E8/14 and 085F/5 are capture-only. Positive: diagnostic visible, progressive good frames, zero RX faults and TX. Negative: missing diagnostic or production regression. Inconclusive: no spontaneous challenge. Abort: unexpected TX, bus or HA degradation. Recovery: V5DCM1 or GAP-51E. No live result supplied for V5DCM2. No ESPHome compile claimed.

**V5DCM1 — RUNNING / PARTIAL; POSITIVE (bounded RX preservation); INCONCLUSIVE (new observer state/live native session).** Hypothesis: passive firmware-derived CM930 session observer can attach to existing CRC-good V5 callback. Baseline GAP-51E RX-only. Controlled change observer/state tracking only; no additional UART consumer or physical TX. User confirmed V5DCM1 flashed. Logs: Pasted text(20261017-004017).txt, (20261017-004733).txt, (20261017-004803).txt. Observed HA monitoring working, parser/resync/drop/geometry counters 0, software TX 0, repeated native FC16 03E8/14 and 085F/5, native FC23=0, mailbox=0. Observer internal transitions not separately logged. Positive no regression shown; negative would be parser faults or TX; abort/rollback GAP-51E if degraded. No rollback observed.

**Next:** review V5DCM2 actual logs, not older repeats. Full evidence: [V5DCM handover](V5DCM/V5DCM1_V5DCM2_HANDOVER_20261017.md).

---

# 2026-10-16 — GAP-45B–46C live evidence reconciliation (newest first)

**GAP-46C — COMPLETE / POSITIVE (RX-only baseline); COMPLETE / INCONCLUSIVE (qualified event/active native response).** Hypothesis: frame-bound exact-challenge shadow diagnostic and its snapshot can run without production regression or native TX. Baseline GAP-46B live arm/revoke NO-TX positive. Controlled change: exact-frame candidate shadow/snapshot; V4.1 native responder deliberately NOT connected. Relevant `0x0F FC23 071C/0730` candidate; ordinary `03E8/14` and `085F/5` excluded. Live user log `Pasted text(20261016-184950).txt`: manual arm 20:49:07.926, automatic expiry 20:49:24.887, snapshot 20:49:37.733 `exact=0 eligible=0 refused=0 reservedState=0 TX=HARD_DENY`; native FC23 absent; production telemetry maintained; resync/drops and software TX zero. Positive criterion arm, expiry, snapshot, zero TX met. Qualified event/slot criterion NOT OBSERVED, not passed. Abort criteria physical TX/DE, CRC/parser regressions, product telemetry loss; none evidenced by provided logs. Recovery if needed GAP-36 RX-only; no rollback used/confirmed.

**GAP-46B — COMPLETE / POSITIVE (tested RX-only transaction boundary); COMPLETE / INCONCLUSIVE (revocation of pending transaction).** Hypothesis: arm expires without event; manual revoke locks the test, without TX. Baseline GAP-45C. Controlled change: one-second pending reservation model/stop control, no native TX implementation. User log `Pasted text(20261016-181858).txt`: arm 20:17:07.614, expiry 20:17:24.248 `EXPIRED_NO_EVENT_NO_TX`, manual revoke 20:18:44.093 `MANUALLY_REVOKED_NO_TX`. Native FC23 zero; zero UART writes, resync/drops; active reserved transaction absent, so its cancellation not tested. Abort criteria unexpected TX, DE, RX errors or production sensor loss; none evidenced. Recovery GAP-36 RX-only if abnormality occurs.

**GAP-46 — RUNNING / PARTIAL (offline-only staged model); active V4.1→V5 executor NOT RUN.** Hypothesis: reusable single-use transaction logic; six offline unit tests previously reported passing. Controlled change only offline state-machine model. Baseline GAP-45C. Positive offline decision/revocation coverage; no ESPHome native TX or local handshake evidence. Active executor remains NOT RUN. Recovery none (offline).

**GAP-45C — COMPLETE / POSITIVE (manual arm → automatic expiry under ordinary traffic); COMPLETE / INCONCLUSIVE (qualified event route).** Baseline GAP-45B. Controlled change: parser-event candidate hook and explicit autonomous 15s expiry; HARD_DENY retained. Live expiry `EXPIRED_NO_EVENT_NO_TX`, software TX zero; no qualified FC23 event observed. Abort unexpected TX or RX regression; recovery GAP-36.

**GAP-45B — RUNNING / PARTIAL (live arm/HOLD observed; independent expiry criterion not recorded in first live log).** Baseline GAP-36; shadow arming without TX. User log `Pasted text(20261016-144245).txt`: `ARMED_SHADOW_15S_NO_TX` 16:42:18.180; `HOLD_UNQUALIFIED_NO_TX armed=1 return=0 cold=0 challenge=0 integrity=1 outputsOff=1 HARD_DENY=1` 16:42:30.937. No challenge or physical TX attempt per software; first log did not contain explicit expiry. Superseded in practice by tested GAP-45C/46B expiry path, without retroactively changing first run's scope.

**Next planned GAP-46D — PREPARED / NOT RUN.** Baseline GAP-46C; offline exact challenge/response-timing assessment from genuine pre-existing captures + historical V4.1 implementation. Positive: unique frame-bound response slot supported by raw timing/direction; negative: ambiguity/no event; abort on missing provenance or unintended live TX. Offline only, no recovery necessary.

---

# 2026-10-16 — GAP-25E/F and GAP-26–32 result reconciliation (newest first)

**GAP-32 — COMPLETE / POSITIVE (offline observability); INCONCLUSIVE (XTR handshake trigger).** Hypothesis: versioned Connect firmware yields passively recognizable session/publication witnesses. Baseline GAP-31 + user-tested GAP-25E. Change: firmware source AST/log observability audit only. Evidence: internal handshake accepted/onboarding/runtime messages and runtime-conditioned package-request logic; these application logs are absent from raw XTR bus captures. Positive: sourced classification of observability; negative: no new independent bus-visible ACCEPTED witness; abort: active TX/secret disclosure/unproven inference. No recovery required (offline). No YAML flashed.

**GAP-31 — COMPLETE / POSITIVE (bounded provenance inventory); INCONCLUSIVE (direction, start, owner, acceptance).** Baseline GAP-30 seven CRC-validated raw captures. Change: headers/timestamps/earliest extended frames audited only. Key observation: Sep-25 09:05 capture shows `0870/count17` at 1.702s before `03E8/count13` at 68.304s, no FC23 within the recorded window. Positive: provenance limit established; negative: no directional/boot evidence; abort: unsupported attribution or active TX. No recovery required.

**GAP-30 — COMPLETE / POSITIVE (offline frame census/order); INCONCLUSIVE (causality).** Baseline GAP-29 firmware handshake-state model. Change: parse seven historical capture logs, validate recognized native frames CRC and order. 4,809/4,809 recognized native `0x0F` records passed CRC; Sep-26 Eco5 captures have extended pages before any in-window FC23; Oct-03 pair of FC23-shaped records precedes historical `03E8/count13` and several extended FC16 pages. Positive: reproducible chronology; negative: disproves only claim that every in-window extension has earlier in-window FC23; abort: conflating captures/roles. No recovery.

**GAP-29 — COMPLETE / POSITIVE (offline versioned state-source model); INCONCLUSIVE (live XTR acceptance).** Baseline GAP-28 extracted genuine 2.0.18/2.1.105 device_client sources. Change: compare relevant methods/branches. Firmware-defined NOT_ACCEPTED, RESPONSE_SENT and ACCEPTED plus conditional package requests; both versions support separate handshake acceptance, newer version adds package tracking. Positive source-specific model; negative live witness absent; abort unsolicited TX/security disclosure. No recovery.

**GAP-28 — COMPLETE / POSITIVE (firmware extraction/source comparison); INCONCLUSIVE (trigger).** Baseline GAP-27 RAUC outer images. Change: offline extract SquashFS and embedded EXT4 `appfs` and compare real `device_client` source; no firmware flashed. 21 Python sources 2.0.18 vs 25 in 2.1.105; 16 common changed, five common identical, four added. Oct-03 458/458 recognized native CRCs valid; FC23-shaped pair at 27.400/27.429s precedes extended pages starting 29.262s. Positive extraction and bounded ordering; abort active TX. No recovery.

**GAP-27 — COMPLETE / POSITIVE (RAUC outer inventory and chronology); INCONCLUSIVE (full source diff at this stage, since resolved by GAP-28).** Baseline GAP-26. Change: offline SquashFS top-level directory/read of seven historical captures. Observed firmware bundle structure and first extended page chronology. GAP-28 supersedes prior inability to inspect embedded sources, **not** the GAP-27 observation. Abort ungrounded roles/TX; no recovery.

**GAP-26 — COMPLETE / POSITIVE (bounded source/capture differential); INCONCLUSIVE (missing session prerequisite).** Baseline locally user-observed GAP-25E/F restricted native pages. Change: offline 2018 client, original RAUC inventory and collaborator/historical capture comparison. Extra parameter page families present in historical traces, absent from recent XTR; no demonstrated cause or native authentication. Abort active changes; no recovery.

**GAP-25F — COMPLETE / NEGATIVE (new page-type appearance in captured Eco→Comfort interval); INCONCLUSIVE (same-page payload change).** Baseline GAP-25E RX-only. Single controlled change: user set Water Mode Eco→Comfort on control panel. Result: native page types unchanged (`03E8/count14`, `085F/count5`), GAP25D candidates Unknown, parser error/drop counters and software native TX zero. No timestamped before/after payload fingerprint; may not infer semantic page identity, session failure or permanent inability. Restore Eco if originally intended; restoration not confirmed.

**GAP-25E — COMPLETE / POSITIVE (bounded live RX/production/TX telemetry); INCONCLUSIVE (HA registry cleanup and missing candidate pages).** YAML `disabled_by_default` set for 76 GAP25D raw sensors while maintaining decoder and production; user live log showed parser/parity clean, TX software counters zero and production sensors valid. 30 previously visible GAP25D Unknown and 19 other disabled HA entities reported; their identities not reconciled. Software counters are not oscilloscope proof of electrical DE inactivity.

**Shared criteria:** All GAP-26–32 are source-only, no YAML/plant/wiring changes. Compare raw > exact YAML > genuine firmware > cross-model. None authorizes sending FC23/ACK or other active native payload, and none proves firmware-derived semantics on XTR M. Original experiment history follows unchanged.

---

# 2026-10-16 — GAP-23E through GAP-24I offline/live handoff

**Scope:** additive summary; earlier experiment records remain historical. Full account: [GAP23_GAP24_HANDOFF_20261016.md](GAP23_GAP24_HANDOFF_20261016.md).

- **Current user-confirmed device:** GAP-23E RX-only, HA production preserved, native `0x0F` TX HARD_DENY. Live observed `03E8/count14` = 69 and `085F/count5` = 34 in sample; HA Heating Curve=36; no software UART writes/TX, but no authenticated native session/owner/epoch.
- **GAP-23F/G/H:** offline contextual/fingerprint/source audits. Eco5 byte-identical page repetition is **cross-model only**; locally observed XTR repeats have no full byte-fingerprint trace. GAP-23H **COMPLETE/NEGATIVE for obtaining verifiable local frame pairs**, not negative protocol evidence.
- **GAP-24A/B/C:** COMPLETE/POSITIVE in bounded offline fail-closed candidate classification, evidence adapter and RX projection; live V4.1 session parity remains INCONCLUSIVE.
- **GAP-24D:** COMPLETE/POSITIVE limited negative host regression; **INCONCLUSIVE** for exact EXP355/386 positive raw frame replay (source completeness/provenance not established).
- **GAP-24F:** COMPLETE/POSITIVE ten-stage offline parity map and passive projection; full active native parity INCONCLUSIVE.
- **GAP-24G/H/I:** COMPLETE/POSITIVE offline lifecycle observational guard, synthetic 32-page shape ledger and nine-source-gap inventory. `67,613/67,613` synthetic C++ assertions pass; shapes never imply semantic acceptance or TX permit. The fixture pages are artificial, not bus evidence.
- **G01–G06 research-risk decisions:** G01 accepted bounded intervention-anchored restart risk; G02 **COMPLETE/POSITIVE CONDITIONAL** only on unchanged installed topology; G03 EOF unknown/accepted research risk; G04 exclusive slot unknown/accepted research risk; G05 hardware DE/FIFO PARTIAL/HOST-ONLY, residual research risk accepted; G06 reset/brownout DE-low unproved/accepted research risk. Acceptance is distinct from technical proof and from permission to send.
- **Unchanged history:** EXP388 RUNNING/PARTIAL; EXP425 NEGATIVE; GAP-18 DEFERRED/NOT RUN; GAP-19 STOPPED/PARTIAL. Do not merge their epochs.
- **Next:** bounded actual portable Core lifecycle-method source equivalence versus V4.1 branch decisions (not another generic observer); offline only, no live TX, no new DCM hardware assumption. No ESPHome compile or deployed GAP-24 firmware claimed.

---

## Individual experiment details

Refer to the dated handoff table for statuses and scope; original experiment result reports remain offline evidence and are not presented as newly rerun tests.

---

# 2026-10-15 — GAP-11..19 latest status reconciliation (additive)

> Detailed hypotheses, baselines, changes, results, abort and recovery: [V41V5 GAP-11–19](V41V5_GAP11_TO_19_STATUS_RECONCILIATION_20261015.md). Original history below untouched.

## GAP-19 — STOPPED BY USER / PARTIAL; no completed result
Offline firmware/native state-source inquiry was initiated after GAP-18 deferral, then user requested STOP. No fresh live protocol test, accepted result, completed audit or firmware effect. Do not promote partial draft observations into PROVEN. Abort executed as requested. No next experiment is automatically running.

## GAP-18 — DEFERRED / NOT RUN
Passively synchronized Saleae and ESPHome measurement prepared as concept only. User reported GPIO18 physically unreachable and explicitly deferred measurement. No waveform/callback pair acquired, GPIO modified, OTA, native TX, or device wiring change. G03/G04 remain OPEN. Resume only upon new feasible, separately authorized design.

## GAP-17 — COMPLETE / POSITIVE provenance, NEGATIVE naive frame-match sync, INCONCLUSIVE physical EOF
Three original Saleae Sep04 acquisitions and 33 text/log sources screened (24 ESPHome-like); zero independently synchronized Saleae/ESPHome pairs. Historical 1,258 Saleae CRC-good frames are from G03-02R, **not re-decoded during GAP-17**. Digital D2-only CSV has no independent absolute clock anchor. 47/47 controls PASS. No hardware action. Do not infer physical EOF→callback latency or G04 slot.

## GAP-16 — COMPLETE / POSITIVE bounded source audit, NEGATIVE timestamp-as-wire-slot, INCONCLUSIVE native readiness
Existing seven captures 25,031/25,031 CRC-good, including four older local XTR files (2,451 frames) and three genuine cross-model captures; 35/35 offline tests. Apparent 13–14 ms FC16 request/ACK-shape logger gaps are **not electrical response deadlines**; 24 equal-millisecond structural pairs negate that extrapolation. Firmware confirms controller-polled Connect slave role but not current XTR epoch/physical sender. No bus action.

## GAP-15 — COMPLETE / POSITIVE host single-event-loop lease and API guard
Reproduced GAP-14 source API direct mock-delivery bypass in offline model; isolated four-file patch restricts production API and guards one deferred mock response lease. 188/188 focused, 175/175 GAP-14, 361/361 GAP-13, 79/79 GAP-12, 326/326 GAP-11, 541/541 historic tests. Does not prove true concurrency or physical native TX.

## GAP-14 — COMPLETE / POSITIVE synchronous staged adoption
Old staged-copy overwrite after revoke reproduced in host model; isolated five-file patch blocks stale adoption and rechecks response lifetime at mock callbacks. 175/175 focused plus earlier suites. Bytes already emitted in real hardware could not be recalled; physical TX untested.

## GAP-13 — COMPLETE / POSITIVE same-core stale Decision provenance
Old `Decision` reused after synthetic epoch previously 1, patched 0; isolated core/header correction. 361/361 focused plus prior suites. Copied stage/async scope remained open and was studied in GAP-14/15.

## GAP-12 — COMPLETE / POSITIVE adapter-fault revocation; COMPLETE / NEGATIVE full chain at the time
Old adapter did not revoke page authority on simulated transport fault; isolated adapter patch 79/79. GAP-11 326/326; historical 541/541 (obsolete expected behavior explicitly changed). Cross-epoch stale Decision remained a NEGATIVE finding, followed by GAP-13.

## GAP-11 — COMPLETE / POSITIVE offline core revocation correction
Against GAP-10 negative retoggle behavior, local core/header patch revokes `write_base` across authority-loss events while preserving diagnostic bytes, aborts in-flight transactions, verifies contradictory decisions. Targeted 326/326 and historical six suites 537/537 in this experiment (530/530 unmodified baseline). Offline only.

**Safety / rollback for all GAP-11–19:** no new native TX, no production firmware flash, leave user-installed GAP-08 RX-only `HARD_DENY`; no new software deployment needed. Every result is scoped to its original source/test.

---

# 2026-10-15 — V41V5 GAP-08B, GAP-09, GAP-10 (newest first)

> Full scoped detail: [GAP-08B–10 audit](V41V5_GAP08B_TO_10_AUDIT_20261015.md). Prior experiment records remain below unedited.

## GAP-10 — COMPLETE / NEGATIVE — offline authority revocation
**Hypothesis:** temporary mailbox/runtime disable followed by re-enable cannot restore previously cached write-authoritative pages without new provenance. **Baseline:** GAP-07 explicit fresh/retained/recovery invalidation, GAP-09 RX-only. **Controlled change:** none to deployed firmware; 23 offline host checks against GAP-08 portable C++. **Result:** toggling either flag false then true can reuse retained `write_base`; `write_ready` is blocked only while disabled. Additional synthetic `commit_fc16` contradictory-decision trust-boundary case; no real path or live exploit established. **Positive criterion:** stale authority persistently revoked and fresh qualified page needed — **NOT MET**. **Negative:** retoggle resurrects old authority — **MET**. **Abort:** any inadvertent native TX/widened policy; none performed. **Recovery:** keep GAP-08 RX-only live unchanged. **Next:** GAP-11 prepared offline defensive fix only; test fresh-qualified recovery and no bypass.

## GAP-09 — COMPLETE / POSITIVE bounded live RX-only; lifecycle case COMPLETE / INCONCLUSIVE
**Hypothesis:** user-flashed GAP-08 portable bridge equals legacy V5 RX on observed bus and stays TX disabled. **Baseline:** 15 Oct earlier V5 RX-only logs. **Controlled change:** user-installed GAP-08 image (OTA); no bus TX. **Result:** >15k compared frames, 0 byte/count/boundary differences and parser/resync/drop faults, 0 physical TX / UART writes, DE=0 and `HARD_DENY`. **Traffic:** 085F/5 all-zero and 04A6/13 repeated; no FC23/0708; owner/epoch unknown. **Positive:** parser equality/passive safety within sampled normal RX — MET. **Inconclusive:** no genuine controller lifecycle boundary; GAP-07 fix not exercised live. Full HA entity availability not independently verified. **Abort:** parser divergence, TX, DE high, missing HA functionality; rollback previous known-good RX-only. **Offline comparative finding:** fresh/retained/recovery cache revocation verified; historical S11 episodes and report-derived fixtures not one complete raw session.

## GAP-08B — COMPLETE / POSITIVE user-confirmed ESPHome compile
**Hypothesis:** GAP-08 packaged RX-only candidate integrates in ESPHome. **Baseline:** GAP-08 YAML + local GAP-07 C++ component. **Controlled change:** real ESPHome build (user-run), no active bus action. **Result:** user reported `GAP-08B compile OK`; no compiler transcript / exact image SHA reviewed. Subsequently user confirmed GAP-08 OTA installed. **Positive:** compile reported successful. **Negative:** no compiler error reported. **Abort/recovery:** preserve baseline UART owner, entities and hard TX DENY; revert previous RX-only if mismatch.

---

# 2026-10-15 — V41V5-GAP-06..08 offline results (additive; latest)

> Full scoped report: [V41V5-GAP-06..08 offline](V41V5_GAP06_TO_08_OFFLINE_20261015.md). Previous GAP-06 proposal and prior experiment descriptions below remain historical snapshots, preserved verbatim. No new live XTR result, controller change, flash or physical TX.

## GAP-08 — COMPLETE/POSITIVE offline RX-only ESPHome source packaging; full ESPHome build PREPARED/NOT RUN

**Hypothesis:** corrected GAP-07 portable core can be included from an existing single-UART V5 RX-only observer with HA sensors preserved. **Baseline:** packaged V5-TX-04B FIX1 YAML (installed build hash unverified), existing passive bridge, GAP-07 core. **Controlled change:** localize portable bridge component source to bundled `components/` with GAP-07 corrected core; separately pinned RX observer and otherwise original YAML retained. **Relevant paths:** same original UART debug producer; passive adapter never enables native transmission; no changed native register/write target. **Executed result:** YAML parsed with custom-tag tolerant PyYAML, source delta check passed; 111 sensor and 71 text_sensor entries preserved, 23 passive headers present; portable host C++ compiled; exact bundled core passed six host suites **530/530**. **Positive:** source packaging and host regression MET. **Negative:** no host regression failures or intentional output expansion observed. **Inconclusive:** ESPHome `config`/`compile` NOT RUN, installed SHA unknown, on-device native shadow behavior NOT RUN. **Abort:** any active output, UART split owner, config/entity loss, compiler mismatch or unverified installed baseline. **Recovery:** leave currently deployed RX-only V5 unchanged. Next GAP-08B PREPARED/NOT RUN.

## GAP-07 — COMPLETE/POSITIVE offline lifecycle invalidation, no live application

**Hypothesis:** stale `Page.write_base` must be invalidated on retained rejoin AND recovery while diagnostic cache remains. **Baseline:** GAP-06 stale-retained core bug; GAP-03/04 and portable semantic/revocation suites. **Controlled change:** two invalidate-writebase loops/guards in isolated portable host copy, inside `Core::begin_retained()` and `Core::begin_recovery()`, with no changed page content/CRC/bus logic. **Result:** compiled C++17 host suites PASS: lifecycle 57/57, GAP-06 108/108, semantic 69/69, revocation 46/46, GAP-03 114/114, GAP-04 136/136 (**530/530 total**). **Positive:** cached pages retain diagnostic readability but stale write admission denied in tested fixtures; newly refreshed qualified page can be admitted. **Negative:** no targeted regression failure. **Inconclusive:** complete original-XTR raw replay and on-device ESPHome compile NOT RUN. **Abort/recovery:** cancel candidate on widened TX or stale admission, retain deployed RX-only baseline. **Unknown:** toggles `set_runtime_normal(false)` and `set_mailbox(false)` do not independently revoke cache writebase; separate policy question.

## GAP-06 — COMPLETE/POSITIVE scoped event-fixture work; COMPLETE/NEGATIVE original retained cache; COMPLETE/INCONCLUSIVE positive original raw replay

**Hypothesis:** local S11 report events can test bounded owner/epoch classification, and retained rejoin must revoke stale write-authoritative pages. **Baseline:** GAP-01..05, original portable C++ reference core, local S11F/H/W/X/Y experiment reports. **Controlled change:** 12 provenance-labelled report-derived XTR event-fixtures, C++ harness, and a candidate patch to an offline core copy only. **Relevant events:** original local XTR S11 FC23/bootstrap, `0708` mailbox, `085F/5`, `0884/60`, `07D0/19` and successors; different manual episodes never merged as one controller epoch. **Result:** 12/12 fixture provenance records, 108/108 host source-characterization tests; **original core NEGATIVE:** `begin_retained()` retained `write_base` so a synthetically requalified transaction could use old authoritative cache. One-line candidate copy invalidated writebase and passed 108/108 patched assertions, plus 69/69 semantic, 46/46 revocation and 114/114 GAP-03. Original 108/108 characterizes the **bug**, it does not show safety. **Positive:** candidate patch behavior bounded host only. **Inconclusive:** original S11 raw text unavailable, full byte-accurate positive local-XTR differential replay and W0–W5 parity NOT RUN. **Abort:** no speculative universal `085F`/`0884` ACK, no private response output or live TX. **Recovery:** existing RX-only V5 untouched.

**Next experiment:** GAP-08B PREPARED/NOT RUN; obtain ESPHome config/compile logs, not just YAML parse or host g++ results.

---

# 2026-10-15 — V41V5-GAP-01..05 offline implementation/replay experiments (additive)

> Full contemporaneous report with baseline, controlled change, frames, success/negative/abort/recovery criteria and evidence classes: [V41V5-GAP-01..05](V41V5_GAP01_TO_05_OFFLINE_20261015.md). All experiments below are **offline only**. Existing historical V4.1 and all negative/inconclusive tests preserved unchanged beneath this section.

## V41V5-GAP-05 — COMPLETE/POSITIVE bounded metadata dispatch; PARTIAL/INCONCLUSIVE exact behavior
**Hypothesis:** 18 V4.1 `0x0F FC03 0708/6` response sites can be selected by one fail-closed dispatcher. **Baseline:** GAP-04's 18 classified mailbox routes; V4.1 branch ordering EXP378 → EXP379 → EXP380 → 03E8 state. **Only change:** standalone Python metadata dispatcher and test cases, no live YAML or frames. **Result:** 31/31 tested source-informed context cases PASS, 18/18 named sites reached, 12 cases choose no site; GAP-04 C++ 136/136 and GAP-03 C++ 114/114 rechecked per local test record. Simultaneous active work families deliberately DENY, not V4.1 first-match. **Positive:** bounded classification MET. **Negative:** unexpected permissive route not observed. **Inconclusive:** W0–W5 serialization, exact state side effects and local positive raw-XTR differential replay NOT RUN. **Abort:** any context conflict, unauthorized positive owner or new TX; **recovery:** keep RX-only V5. No live experiment.

## V41V5-GAP-04 — COMPLETE/POSITIVE bounded C++ mailbox shadow-policy; full parity INCONCLUSIVE
**Hypothesis:** 18 physical mailbox routes map to one `0708/6` input with distinct intent/context. **Baseline:** GAP-03 portable C++ ownership and 58-route classification, V4.1 source. **Only change:** metadata plus stand-alone C++ classification/negative policy, original core unchanged. **Result:** 136/136 assertions PASS; 8 idle/guard, 6 current refresh, 4 desired selector. `085F/5`/`0884/60` without sufficient owner context DENY; historical manually qualified cases review-only, never auto-TX. **Positive:** policy classification MET. **Negative:** unqualified approval not observed. **Inconclusive:** true branchguard priority, output bytes and full positive source event equivalence NOT RUN. **Abort/recovery:** stop on broader ACK or TX; unchanged RX-only.

## V41V5-GAP-03 — COMPLETE/POSITIVE synthetic/documentary C++ tests; positive raw equivalence INCONCLUSIVE
**Hypothesis:** the GAP-02 core can reproduce source-qualified XTR bootstrap, token, and desired-page semantics without false runtime ownership. **Baseline:** GAP-02 portable adapter; historical S9/S10/S11 local XTR logs and negative EXP425 context. **Only change:** C++ shadow policy and synthetic source-faithful geometry fixtures; no physical frame producer. **Result:** 114/114 assertions PASS; 32/32 ordered bootstrap, single-use runtime token, exact semantic controller FC16 read-back fixture. **New discrepancy:** upstream portable runtime can classify `0884/60` positively without specific owner proof; S11F ended capture-only. Supplemental policy denies unqualified `0884`. **Positive:** bounded offline state tests MET. **Negative:** general 0884 owner authority NOT proven and not granted. **Inconclusive:** original complete raw local XTR byte-by-byte replay NOT RUN. **Abort/recovery:** any unproven ACK => DENY; retain RX-only.

## V41V5-GAP-02 — COMPLETE/POSITIVE scoped host C++ integration/negative replay; positive equivalence INCONCLUSIVE
**Hypothesis:** 58 route classes can be bound to actual portable C++ owner states with no UART permission. **Baseline:** GAP-01 ledger; public V4.1 source and portable C++ reference core. **Only change:** offline C++ adapter plus host replay, copied reference core unchanged. **Result:** C++17 `-Wall -Wextra -Werror` compile; 32/32 synthetic bootstrap; 69/69 semantic tests; 46/46 revocation tests; three *cross-model* captures with 4,394 CRC-good slave-`0x0F` frames, 2,839 relevant requests and 18,507/18,507 route checks correctly DENY due to missing current session authority. **Positive:** fail-closed negative replay MET. **Negative:** unauthorized TX not observed. **Inconclusive:** no complete positive original-XTR byte+owner equivalence. **Abort/recovery:** if mismatch/bus output, stop; no device changed.

## V41V5-GAP-01 — COMPLETE/POSITIVE 58-site structural route audit
**Hypothesis:** every committed V4.1 `write_array()` site can map to one distinct logical owner or explicit reject. **Baseline:** V4.1 blob `8e8a82689e53528a8b751a1abbd901f683b6b238`, existing reference-core route matrix. **Only change:** offline ledger/Python intent-policy and tests. **Result:** all 58 sites accounted for: 2 approval, 32 bootstrap, 1 generic runtime, 18 mailbox, 4 desired, 1 denied legacy 04A6. **Positive:** 58/58 inventory MET. **Negative:** no unknown route. **Inconclusive:** no live compiled V5 TX emulator. **Abort/recovery:** no physical TX or private algorithm publication; production unaffected.

**Next:** V41V5-GAP-06 **PROPOSED / NOT RUN**, local-XTR original event-fixture differential replay. No automatic experiment advancement.

---

# 2026-10-14 — G03-01R and G03-02R offline results (additive)

> Source reports: [G03-01R](G03_01R_OFFLINE_REVALIDATION_20261014.md) and [G03-02R](G03_02R_SALEAE_ESPHOME_CORRELATION_20261014.md). Both completed OFFLINE; original G03-01 and G03-03..05 prior results preserved; no new RX capture, ESP flash, controller restart, TX, or G04-07 execution.

**G03-02R COMPLETE/INCONCLUSIVE physical EOF-to-B6 callback timing, COMPLETE/POSITIVE source audit.** Hypothesis: historical Saleae edge captures can be time-aligned to same-session ESPHome raw logs. Baseline G03-03/05 D2, G03-01R B6 and G04-05. Controlled change only original Saleae acquisition metadata read and full CRC frame byte matching across 22 locally available ESPHome logs. Frames include `0x0F` FC16 `03E8/14` and `085F/5`, plus `0x02/0x1E` as candidate markers. Result 55+156+1047 CRC-good D2 ADUs, but no verifiably simultaneous Sep 4 ESPHome log; repeated frame values across different days cannot establish shared clock. Positive criterion unique same-session multi-frame marker + calibrated time offset NOT MET. Inconclusive criterion missing common epoch MET. Abort any invented time offset, host timestamp as EOF, native TX. Recovery none, offline only. Next check pre-existing Sep 4 logs or plan separately approved passive synchronized capture.

**G03-01R COMPLETE/POSITIVE source-baseline revalidation; current physical EOF OPEN.** Hypothesis: stock ESPHome UART debug callback time is not physical last stopbit. Baseline original G03-01, Saleae G03-03..05, G04-06/07 source and user-confirmed B6. Controlled change only offline YAML/source recheck, no device changes. Relevant 9600 8E1, RX GPIO18, TX GPIO17, DE GPIO21, debug 5ms, software `micros()` callback. Result one consumer; ESPHome driver no UART event queue in inspected source; hardware RX timeout metadata possible only via version-matched instrumentation, not direct YAML; 3.5T=4.010417ms theoretical, not physical timestamp. Positive source distinction MET, negative strict electrical EOF unresolved. Abort double-reader, TX/DE, loss of parser integrity; recovery keep B6 RX-only. G04-07 deferred.

**All gates:** G02 conditional installation-scoped; G03/G04/G06 OPEN, G05 hardware partial. Native TX HARD DENY.

---

# 2026-10-14 — G02-09..11B reconciled; G02 conditional acceptance (no TX)

> Additive record of earlier locally reported offline work, photos and explicit user approval of **scoped G02 closeout**. Source classifications, baselines, controlled changes, frames, criteria, abort and recovery: [G02-09..11B full report](G02_09_TO_11B_CONDITIONAL_CLOSURE_20261014.md). This GitHub documentation update itself did NOT rerun offline scripts, ESPHome compilation, a live heat pump restart or active TX. All older experiments/negative results below kept verbatim.

## G02-11B — COMPLETE / INCONCLUSIVE independent electrical exclusivity; CONDITIONAL POSITIVE installation scope
**Hypothesis:** the documented single known external DCM port and no attached DCM allow a scoped installed-topology owner assumption. **Baseline:** G02-10, G02-11A, ATEC p7 hub pin/function diagram, local XTR PCB photos including full-front overview, G01-09 RX-only video 24 FC23/0 peer responses. **Controlled change:** photograph/diagram/user installation clarification assessment only, no wiring change. **Relevant interface:** hub RJ45 `122 Display`, `123 Ext.`, native slave `0x0F` FC23. **Positive:** one known external DCM jack and no installed module, user-approved `G02 CONDITIONAL PASS` for unchanged setup. **Negative/inconclusive:** unseen internal responders/splitters or electrical copper routes cannot be excluded without further independent observation. **Abort:** peer response, changed wiring/profile, ambiguous session, unexpected TX; revert G02 context UNKNOWN/HOLD. **Recovery:** RX-only, no physical changes. User explicitly approved conditional G02 closure; NOT a universal electrical proof.

## G02-11A — COMPLETE / POSITIVE bounded local historical protocol work ownership (offline audit)
**Hypothesis:** historic native `0x0F` transactions show controller-assigned work inside valid sessions. **Baseline:** historical EXP355/386/S11F, EXP420–425 and genuine Online/DCM references; Connect CM930 state/flags; community thread documentary recap. **Controlled change:** offline historical document/excerpt comparison, no new active response. **Relevant:** FC23 `071C/0730`, FC16 settings/runtime pages including `03E8`, FC03 `0708/6` and controller FC16 republish; `0662/33` orphan. **Reported positive:** EXP355 fragment 240 runtime ACKs and 133 mailbox responses, historical locally controller-accepted page-cache work, offline source checks 14/14 as previously reported, NOT newly re-run here. **Negative:** EXP425 ACK without expected `0683` tail, EXP423 orphan, EXP419/423 INCONCLUSIVE. **Abort:** ACK promoted to semantic success or any inferred universal responder right; recovery historical classification only. Scope: work ownership conditional, not electrical exclusive sender.

## G02-10 — COMPLETE / POSITIVE offline topology inventory; independent electrical exclusivity INCONCLUSIVE
**Hypothesis:** local PCB photo and ATEC documentation identify known external path. **Baseline:** XTR RS485 wiring evidence and ATEC 13p schematic. **Controlled change:** passive visual inspection only. **Relevant:** local `122` display and `123` Ext. RJ45; cross-model ATEC schematic p7. **Positive:** matching port labels/functions, no separately installed DCM per user. **Negative:** same precise copper/backside/unseen transceivers unknown. **Abort:** interpretation of cross-model as local netlist. **Recovery:** document correction; no device changes.

## G02-09 — COMPLETE / POSITIVE OFFLINE source-typed classification; exclusive physical responder INCONCLUSIVE
**Hypothesis:** cross-model FC23 windows separate request/no-response, response present sender unknown and controller work candidate. **Baseline:** G02-01..08 and genuine ATEC/Eco5 captured sessions; local G01-09 separate. **Controlled change:** reported host-only replay window classification, no on-wire action. **Relevant:** `0x0F` FC23 `071C/0730`, next FC16 `03E8` and ACK shapes; XTR 24 unanswered requests separate. **Reported:** 25,031 CRC-valid genuine cross-model frames; 8 FC23 windows: 5 work candidates, 2 response-present/no `03E8` ACK within 35s, 1 no-response; host-only 193/193 checks as previously reported (not rerun for this GitHub commit). **Negative:** response/ACK not a sender identity or collision-free TX lease. **Abort:** cross-model counted as XTR or offline results treated as electrical proof; recovery offline reclassification.

**G02 decision (user approved):** `COMPLETE/POSITIVE (CONDITIONAL)` installed topology + previously locally confirmed native protocol role only. Strict electric-exclusive-owner claim remains unproven; FAIL-CLOSED on any install change/peer ambiguity. Separate G03/04/05/06 and physical epoch predicates unaffected. **NATIVE TX HARD DENY.**

---

# 2026-10-14 — G02-01..08 offline research reconciled, G02-09 PREPARED / NOT RUN

> Detailed experiment hypotheses, baselines, exact controlled changes, frame families, success/abort/recovery and sources: [G02 evidence report](G02_01_TO_08_OWNER_EVIDENCE_RECONCILIATION_20261014.md). Original dated histories preserved below. No new physical TX, ESP flash, controller restart or writable YAML generated.

**G02-08 COMPLETE / POSITIVE OFFLINE, G02 physical owner INCONCLUSIVE.** Hypothesis: video-anchored G01-09 RX-only cold-start log can classify response absence without inventing responder identity. Baseline G02-01..07 genuine cross-model plus local XTR G01-09. Change only offline SHA/timestamp/counter assertion; source 4,660 lines SHA `a66541b2c8d91661863c6a315003ef26eb4ca3d8960e324479ff2a43cd8acb2e`. FC23 repeated 24 times; matching peer response shapes reported 0, bootstrap 0/32, observed native/software TX 0; RX parity/resync/drop counters remain clear in reported window. Positive bounded absence result met; negative/no-go physical owner identity remains UNKNOWN. Abort if peer absence promoted to permanent no peer or an ACK is authorized. Recovery offline-only reclassify, existing RX-only untouched.

**G02-07 COMPLETE / POSITIVE OFFLINE FORMAL NO-GO; physical owner OPEN.** Hypothesis already-collected evidence can make strict decision without live action. Baseline G02-01..06 plus G01 and G03–G06 current gates. Controlled change offline decision test only; 26/26 PASS re-run 2026-10-14. Positive `G02_OPEN_NO_GO`, no TX. Abort synthetic metadata treated as electrical proof, recovery reclassify offline. No test on warmtepomp.

**G02-06 COMPLETE / POSITIVE OFFLINE preflight; optional live SUPERSEDED/NOT RUN.** Baseline CO/CN/P74L/DI-B6 software counts, G02-05; no exact compiled as-built proof. Change host-only validation 16/16 PASS re-run. Positive enough existing diagnostics to avoid new flash. Negative external sender still unproven, abort TX promotion, recovery leave RX-only image intact.

**G02-05 COMPLETE / POSITIVE HOST-ONLY; physical owner OPEN.** Baseline genuine cross-model capture and CM930 audited work families, historical local XTR contexts. Change standalone reducer/fuzz only; re-run 38/38 units, 25,031 cross-model CRC-good frames, 4,096 synthetic streams / 131,072 events / 655,360 fail-closed checks, always `tx_authorized=false`. Positive source-typed DENY, negative actual sender/lease unproven. Abort any non-deny decision; recovery offline only, no deployed ESP reducer.

**G02-04 COMPLETE / POSITIVE DOCUMENTARY_ONLY; original local raw replay INCONCLUSIVE.** Baseline EXP419/420/423/425/426 outcomes; change status-preserving local historic context classification only. Positives context segregation and preservation of EXP420 scoped positive/EXP425 NEGATIVE; negatives orphan ACK is not semantic acceptance or ordered 0683 successor. Abort reinterpret past negatives; recovery documentary correction.

**G02-03 COMPLETE / POSITIVE OFFLINE bounded genuine cross-model capture replay; electrical owner INCONCLUSIVE.** Baseline seven source-typed ATEC/Eco5 or unknown-model originals. Change CRC-verified presence/absence matrix; 25,031 frames, 164 FC23 requests, seven response shapes, 41 unanswered Eco5 FC23 in one bounded window. Positive shape windows identified, negative identity unknown; abort assigning Eco5 result to local XTR or host times as wire EOF; recovery offline reclassification.

**G02-02 COMPLETE / POSITIVE inspected 2.1.105 CM930 paths; direct cross-version independent recheck PARTIAL.** Baseline real firmware and 2.0.18/2.1.105 comparison report. Change handler review only. No explicit owner-lease identified in inspected FC23/FC16/FC03/mailbox paths, not globally disproved; abort publishable secret transform/claim permanent bus lock; recovery documentary source check.

**G02-01 RUNNING / PARTIAL full source ledger; typed matrix POSITIVE.** Baseline historic XTR EXP355/386/S11F and EXP419–426, genuine ATEC/Eco5 and firmware. Change offline provenance ledger only; source/owner/slot separated. Full original XTR raw review missing, so not COMPLETE for that scope. Abort ACK geometry to owner inference; recovery correct classification.

**G02-09 PREPARED / NOT RUN.** Hypothesis: cross-source windows can be partitioned into REQUEST_WITHOUT_RESPONSE_OBSERVED, RESPONSE_SHAPE_PRESENT_SENDER_UNKNOWN, ASSIGNED_WORK_CANDIDATE or HOLD without granting exclusivity. Baseline G02-01..08; change planned offline-only comparator; positive proper provenance+TX DENY; negative false ownership; abort any new native transmission/secret leakage; recovery host-only correction. **No execution result yet.**

---

# 2026-10-14 — G01-07R / G01-08 / G01-09 source-linked results (additive)

> Detailed observations and limitations: [G01-07R/08/09 evidence](G01_07R_08_09_CONTROLLER_RESTART_20261014.md). Historical original experiments (including negatives and inconclusive results) preserved below. No code was flashed and no native reply was transmitted for the G01-09 observation.

## G01-09 — COMPLETE / POSITIVE, bounded VIDEO / INTERVENTION_ANCHORED; strict electrical boot witness OPEN
**Hypothesis:** filmed normal power intervention/display restart correlates with fresh native protocol start while independently powered ESP logs continuously. **Baseline:** G01-07R six historical restart candidates, G01-08 offline classifier and current user-confirmed B6 RX-only. **Exact controlled change:** user performs one normal Thermia power-cycle while filming switch/display and leaving current ESPHome capture RX-only; no experimental response, write, flash or HA configuration change. **Relevant fields:** controller `A80E=0000/A80F=0005`; 0x0F FC23; first valid `0x1E` return; 0x0F `03E8` page 0/32, 11D parser consistency and TX software counters. **Observed:** 15:41:15.736 callback gap 11,944 ms; first CRC return 15:41:15.749; status 15:41:16.460; FC23 counted by 15:41:17.021; 24 repeated by 15:42:55.315, TX=0, 32/32 absent and fail-closed HOLD. Video two clicks/display off/on, user confirms same event. ESP counters/boot identity continuous, no ESP reboot observed; no separate exact uptime samples. **Positive:** intervention correlated with protocol restart; achieved. **Negative/abort:** video/log ambiguity, ESP reset, RX corruption, unexpected TX/DE or main-rail electrical proof being assumed; not observed for software integrity, but rail measurement absent. **Recovery:** RX-only baseline, normal controller restart procedure; no further recovery required. **Verdict:** COMPLETE/POSITIVE `INTERVENTION_ANCHORED`; strict physically measured controller epoch INCONCLUSIVE/OPEN. Native TX HARD DENY.

## G01-08 — COMPLETE / POSITIVE OFFLINE candidate validation; INCONCLUSIVE for autonomous physical epoch
**Hypothesis:** passively identify protocol-start candidates without promoting to physical boot/TX. **Baseline:** EXP293–297, EXP344, G01-04 false-physical-epoch caution; TX16 retained negative; ESP-only OTA. **Change:** standalone offline replay/fail-closed fixture runner only. **Result:** 5 clean historical CANDIDATE, EXP296 HOLD (resync=1), 8 new fixed negative controls and 2,048 adversarial streams with no false candidate within tested fixture space; original seven G01-04 false-positive vectors not literally available for rerun. **Abort:** physical epoch or TX=true from software sequence; none promoted. **Recovery:** offline detector only, no on-device change.

## G01-07R — COMPLETE / POSITIVE historical source review; physical rail INCONCLUSIVE
**Hypothesis:** older local XTR logs include independent ESP-powered controller-start sequences. **Baseline:** older EXP293–297/344 raw logs. **Change:** source-typed offline event extraction with CRC/continuity metadata; exclude cross-model Eco5. **Result:** six start candidates after >=5s recorded/detected silence and FC23 in 1.05–1.30s; EXP296 parser resync HOLD; historical 32/32 followed active responses and not eligible as passive prerequisite. **Abort:** software timing or cross-model shape promoted to physical electrical proof. **Recovery:** offline-only reclassification.

**Next experiment:** G02 offline provenance/work-owner audit, not a new power-cycle or live 0x0F response. 

---

# 2026-10-14 — G04-01..07 evidence and experiment status update

> See [full source-linked G04 record](G04_RESPONSE_SLOT_G04_01_TO_G04_07_20261014.md). This is a documentation reconciliation of already completed offline work and user-provided B6 live log; no new active experiment, OTA flash, controller restart or native TX.

## G04-07 — PREPARED / NOT RUN; USER DEFERRED
Hypothesis: ESPHome 2026.9.0 same-owner ESP-IDF UART timeout metadata could separate driver event processing from 5ms debug callback. Baseline: confirmed running R6-P74DI-B6 RX-only, complete YAML/21 includes. Controlled change (not applied): bounded event queue/metadata in existing UART driver only; preserve one uart_read_bytes owner, parser, entity IDs, production HA and TX HARD DENY. Positive: full ESPHome compilation and separately approved future live RX-only test show consistent events, clean parser/HA, software TX=0. Negative: build error, missing discrimination or unpaired event. Abort: TX/DE HIGH, resync/drop, HA regression, reboot/queue overflow. Recovery exact installed B6, no controller restart. **Prototype is not compiled, integrated or flashed.** User explicitly postpones.

## G04-06 — COMPLETE / POSITIVE OFFLINE conditional feasibility
Baseline B6 UART.debug timeout 5ms and ESPHome ESP-IDF UART sources. Controlled change: offline source investigation. Found uart_driver_install event depth=0 and queue=null; hardware RXFIFO_TOUT and debugger callback distinct. Positive code path explained; negative claim of direct physical EOF measurement rejected. Abort promoting software event time to slot. Recovery no changes.

## G04-05 — COMPLETE / PARTIAL bounded USER-LIVE B6 software timing
Hypothesis B6 early RX-only decision timing is measurable without new firmware. Baseline user-confirmed running B6, 9600 8E1 and 5ms debugger grouping; user log 5000 lines 00:34:21–00:37:31. Change: offline statistics of already collected live diagnostics. 88 B4 and 88 B3 measurements; B4 entry-to-decision min/median/max 1474/1545/3124us, eval 5/6/11us, B3 entry-to-diagnostic 3370/4169/5056us. Zero reported parser resync/drops/geometry mismatch, software TX 0; one API buffer full warning. **Partial:** original one-shot B5/B6 transition not in log; repeated state=2 match_transition=0. Positive software latency and bounded RX-integrity confirmed; negative electrical EOF/slot timing not measured. Abort unintended TX/DE, framing faults, HA outage. Recovery unchanged B6; no flash.

## G04-04 — COMPLETE / POSITIVE OFFLINE feasibility
Baseline B6 debugger callback. Controlled change code examination; confirmed 5ms software grouping not physical last stopbit. No live TX or new physical measurement. Abort treating callback time as response deadline. Recovery none.

## G04-03 — COMPLETE / POSITIVE OFFLINE context matrix
Baseline historic V4.1 EXP355/386/S11F/387, EXP388 PARTIAL, EXP419/420/423/425; cross-model G04-01/02. Controlled change nine-category context decision matrix: fresh, retained, recovery, service, orphan, cancel, other responder, malformed, genuine DCM. Positive context separation; no exclusive owner. Negative previous EXP425 remains; abort granting TX. Recovery documentation only.

## G04-02 — COMPLETE / POSITIVE OFFLINE V4.1 guard comparison
Baseline V4.1 working local XTR reference versus seven genuine cross-model DCM response-shaped pairs. Controlled change source guard audit. Positive exact shape plus session/one-shot/peer integrity/cancellation guards identified. Unknown internal seven-pair owner/electrical state. Abort inferred current authority. Recovery none.

## G04-01 — COMPLETE / POSITIVE OFFLINE cross-model FC23 adjacency
Baseline seven historical genuine/collaborator logs. Controlled change CRC verification and immediately adjacent FC23 response audit. 25,031 CRC-valid recognized log records, 164 native FC23 request shapes, seven immediately adjacent response shapes with 29–63ms HOST log timestamps; NOT wire EOF or local XTR owner evidence. Abort host timestamp promoted to bus response-slot proof. Recovery documentary only.

**Project gate:** G04 physical exclusive reply slot OPEN. G04-07 deferred, not a new live experiment. Historical negative, partial and prepared experiment outcomes below are preserved.

---

# 2026-10-13 — G01-01..06 offline results; G02 owner plan PREPARED/NOT RUN

> Newest additive historical record; all previous logs preserved. Source and full bounded criteria: [G01](G01_CONTROLLER_EPOCH_20261013_SYNTHESIS.md), [G02](G02_EXCLUSIVE_OWNER_PLAN_20261013.md), [DI-B12 erratum](R6_P74DI_B10_B12_PROVENANCE_RECONCILIATION_20261013.md). No new native TX, flash or controller restart.

## G01-06 — COMPLETE/POSITIVE offline witness review, physical INCONCLUSIVE; external LIVE PREPARED/NOT RUN
Baseline G01-01..05, EXP355/386/S11F and R6-P24. Hypothesis independent controller start needs external verified witness. Exact change offline review and 15/15 checks. Result no independent source; user confirms no HA/Shelly indoor supply monitor. Abort synthetic/protocol proof claimed physical. Recovery RX-only, no controller restart.

## G01-05 — COMPLETE/POSITIVE offline CO/B6 preflight, new user LIVE PREPARED/NOT RUN
Baseline CO, actual DI-B6 log and P24. Hypothesis existing passive diagnostics suffice. Change source/log audit only, 11/11. B6 bounded 631 V5 frames/105 pages, no gaps/FC23/new resync/drop/software TX. Abort new TX/DE or HA/parser regression; recovery unchanged RX-only.

## G01-04 — COMPLETE/NEGATIVE original offline physical-proof projector; COMPLETE/POSITIVE new host gate 2087/2087
Baseline G01-02 38/38 regular tests. Hypothesis malicious metadata can falsely promote epoch. Change seven counterexamples and provenance/continuity guard plus 2048 streams/40993 synthetic events. Result seven false promotions in old standalone Python, all blocked by new offline-only guard. Abort TX or synthetic proof considered local. Recovery do not deploy old projector.

## G01-03 — COMPLETE/POSITIVE 48/48 offline chronology; independent physical epoch INCONCLUSIVE
Baseline EXP355/386/S11F and raw EXP318/319 excerpts. Controlled change historical source-typed replay. Fresh versus retained classified, but complete original EXP355/386 raw not rechecked. Abort documentary evidence presented as independently physical proof. Recovery source labels offline.

## G01-02 — COMPLETE/POSITIVE 38/38 initial offline projector, physical epoch INCONCLUSIVE
Baseline DE/V4.1/CO. Controlled change session candidate/physical evidence axes, no IO. Later G01-04 invalidated seven original adversarial proof paths, not normal candidate classification. Abort owner/TX grant. Recovery hardened host-only logic.

## G01-01 — COMPLETE/POSITIVE bounded source audit, PARTIAL binary provenance
Baseline EXP355/386 V4.1 and CO. Change 21/21 include SHA and guard mapping; no hardware. Positive scoped source checks; physical controller boot unknown. Abort ESP restart/callback gap as unique controller ID. Recovery no ESP change.

## R6-P74DD-DH offline scope refinement
R6-P74DD PARTIAL exact as-built binary/dependency provenance, source audit bounded positive; DE COMPLETE/POSITIVE offline session projection (27 host checks); DF COMPLETE/POSITIVE bounded historical documentary replay, full original local raw XTR replay INCONCLUSIVE; DG COMPLETE/POSITIVE offline fail-closed host checks; DH COMPLETE/POSITIVE OFFLINE PREFLIGHT, new user-live measurement PREPARED/NOT RUN. None licenses native TX.

## DI-B10-B12 — COMPLETE/POSITIVE offline parsing/profile, XTR-origin interpretation SUPERSEDED
Baseline genuine cross-model originals and separate local EXP318/319. Change CRC/context and firmware/model audit. Result twelve cross-model zero085F/ACK shapes, October ATEC, September uncertain legacy-like; unrelated to twelve local XTR. Negative universal 085F-ACK->0884 and universal 10x6 profile; sender/EOF inconclusive. Recovery preserve raw and correct provenance.

## G02-01..06 PREPARED/NOT RUN; G02-07 PROPOSED/NOT RUN
Baseline EXP355/386/S11F, EXP419/420/423/425, current RX-only and CM930; hypothesis sender, work owner, response window can be assessed separately. Controlled changes not yet executed. Criteria and recovery per G02 plan; any unearned exclusive owner/TX inference is abort. Native output DENY.

---

# 2026-10-13 — R6-P74CX–DC COMPLETE OFFLINE; R6-P74DD–DH PREPARED / NOT RUN (newest)

> Full baseline, controlled-change, criteria, evidence origin and abort/recovery for every experiment: [CX–DC result / DD–DH plan](R6_P74CX_TO_DC_20261013_RESULTS_AND_DD_DH_PLAN.md). Original source reports were written offline on 2026-10-13. **No user-live XTR test, reflash, external gateway hardware, native TX or register write in CX–DC.** Previous log history below is unchanged.

## R6-P74DC — COMPLETE / POSITIVE ten-stage offline gap audit; COMPLETE / INCONCLUSIVE current owner
**Baseline:** historical V4.1 EXP355/386/S11F/387 scoped outcomes; EXP388 PARTIAL, EXP425 NEGATIVE, CO RX-only, CM930 firmware. **Hypothesis:** distinguish old active state machine from CO passive observability. **Change:** compare ten exact native transition/electrical stages, source flags and 512 non-authoritative synthetic metadata combinations; no live code change. **Result:** contemporary CO observer cannot grant epoch/owner/EOF/slot/TX; ten gaps explicit, 512/512 synthetic checks fail-closed. **Negative/abort:** false ownership/semantic conclusion, source mismatch, TX=true -> stop. **Recovery:** original CO stays unchanged. **Unknown:** hardware safety and current authenticated work owner.

## R6-P74DB — COMPLETE / POSITIVE cross-model status reconstruction; COMPLETE / NEGATIVE status-only readiness
**Baseline:** DA, genuine Eco5 controller status histories. **Hypothesis:** status change alone releases first `03E8` ACK. **Change:** re-time status-pair transitions against logged ACK shapes. **Result:** four Sep28 Eco5 windows all pass `0000/0005 → 0008/003C → 0008/0005 → 0028/0005 → 0028/000A` around +66s versus ACK around +118–120s; Sep26 gateway-absent negative control can reach later status but lacks registered ACK. **Negative/abort:** status-only owner/readiness promotion; source CRC/timestamp disagreement. **Recovery:** rerun offline originals, no device changes.

## R6-P74DA — COMPLETE / POSITIVE documentary local-XTR contrast; COMPLETE / NEGATIVE universal 120s post-bus-return rule
**Baseline:** CZ Eco5 timing; locally historically confirmed EXP355/386/S11F. **Hypothesis:** Eco5 first ACK ~120s after gap universally holds for XTR. **Change:** source-classified documentary local timestamps versus raw Eco5 timing, **without independent XTR raw reparse**. **Result:** EXP355 bus return 00:51:29.662 → last 32/32 ACK 00:52:03.257 = 33.595s; first ACK necessarily earlier; S11F third qualified FC23 15:52:02.721 → first `03E8` ACK 15:52:03.312 = 591ms but no matched XTR bus-return anchor; EXP386 missing direct timing. **Negative/abort:** claiming universal 120s or inventing physical power-on epoch; source gaps -> INCONCLUSIVE. **Recovery:** existing untouched logs; no device procedure.

## R6-P74CZ — COMPLETE / POSITIVE genuine Eco5 capture timing; COMPLETE / INCONCLUSIVE causal timer
**Baseline:** CY two delayed first ACK events, genuine documented restart gaps. **Hypothesis:** early/late FC23 branches converge on a shared post-gap host-time boundary. **Change:** anchor six first `03E8` ACK shapes to first frame after restart-related gap instead of FC23 response. **Result:** 118.478–120.296s across six Eco5 contexts; four FC23 responses after 29 request shapes versus two after 3 request shapes; gateway-absent control 41 requests and no ACK. **Negative/abort:** do not claim electrically measured reboot, universal timer or owner; CRC/gap-provenance mismatch. **Recovery:** offline replay.

## R6-P74CY — COMPLETE / POSITIVE repeated page content; COMPLETE / NEGATIVE changed first-page-body trigger; causal INCONCLUSIVE
**Baseline:** CX, CT/CU. **Hypothesis:** late ACK caused by mutated first-page request. **Change:** bytewise compare 102 CRC-good first-page FC16 requests before first ACK in each slow context. **Result:** one unique request image, 101 exact repetitions each, first ACK 108.653/108.507s after response and 62/31ms after last retry; broad 32/32 continues in ~34–36s. CM930 firmware's internal handshake `ACCEPTED` event distinct from short ACK. **Negative/abort:** source mismatch, physical sender/semantic acceptance inferred from shape. **Recovery:** no hardware affected.

## R6-P74CX — COMPLETE / POSITIVE OTHER type audit; handshake cause INCONCLUSIVE
**Baseline:** CW/CU original Eco5 windows. **Hypothesis:** CJ `OTHER` hides a native `0x0F` response/condition. **Change:** passive frame shape subtyping only; same CRC/source windows. **Result:** 13 OTHER shapes all typed, no 0x0F therein; in two slow contexts `0x06 FC23` one-byte change +49.953s before ACK, `0x0A FC23` one-off request variation +0.279/+0.310s AFTER ACK; `0x02 FC23` response-shaped frames invariant within slow pre-ACK window. 25,031 original CRC-good frames; 256 synthetic negative controls. **Negative/abort:** source/auth mismatch, reclassifying room path as native endpoint. **Recovery:** repeat offline originals.

## R6-P74DD–DH — PREPARED / NOT RUN (explicitly not completed)
- **DD:** Hypothesis current source diff can isolate missing old active owner/restart guards. Baseline DC, V4.1 old source, CO user-installed source. Controlled change offline source-linked map only; **positive** verifiable present/removed/unknown mapping; **abort/negative** missing exact source or invented equivalence; **recovery** offline, CO unaffected.
- **DE:** Hypothesis a read-only session-candidate classifier can distinguish fresh/retained/recovery where evidence exists. Baseline DD/CM. Controlled change host no-TX candidate state projection; **positive** ambiguity remains UNKNOWN, no owner promotion; **abort** false grants; **recovery** rollback offline projector.
- **DF:** Hypothesis model separates historical local positive, negative and untested branches. Baseline DE, existing original XTR logs if found. Controlled change replays with raw/documentary provenance; **positive** correct scoped classification; **negative** source-incomplete/incorrect result -> INCONCLUSIVE; **abort** fake raw confirmation; **recovery** restore fixtures.
- **DG:** Hypothesis fail-closed under source mutation and cancellation while preserving production semantics. Baseline DF/CO. Change offline fault and schema tests; **positive** zero TX authority; **negative/abort** any owner/epoch leak or production regression; **recovery** no device change.
- **DH:** Conditional passive live RX-only integration ONLY after DD–DG evidence; **no YAML prepared, no user flash**. Baseline CO RX-only. Change minimal HA Configuration passive diagnostic, production blocks retained; **positive** stable RX/HA, zero output; **negative/abort** parser resync/drops/fault, DE/TX activity or entity regression; **recovery** revert tested CO/CN, no controller restart.

**Persistent older statuses:** EXP388 RUNNING / PARTIAL; EXP425 COMPLETE / NEGATIVE; offline findings never advance the user's actual live experiment or physical G01–G06 safety proof.

---

# 2026-10-13 — R6-P74CT–CW offline tests (newest first; details in reports)

> Full evidence and safety: [CT–CW](R6_P74CT_TO_CW_20261013.md); previous [CH–CS user-live/offline handoff](R6_P74CH_TO_CS_20261013_HANDOFF.md). All CT–CW changes **host-only**, original raw captures unchanged and SHA/CRC verified; **0 bus TX / 0 flash**. This is additive; historical negatives/inconclusives below are preserved.

## R6-P74CW — COMPLETE / POSITIVE, host-only fail-closed session-shape classification
**Hypothesis/baseline:** can CJ/CK evidence shape histories be classified without promoting authority? Baseline verified seven genuine Eco5 windows, existing CK/CM fail-closed principles. **Single change:** host-only passive classifier and eight synthetic metadata-fault types. **Fields:** 0x0F FC23 request/response *shapes*, 0x0F FC16 `03E8/count14` request/short ACK-shapes, 32-page observed cross-model profile; source line/time ordering; provenance trust. **Positive:** 7/7 contexts classify (6 broad 32/32 shape prefixes, 1 no response), 256/256 deterministic negative cases keep owner/epoch/sender/EOF/slot/semantic/TX false. **Negative/abort:** any inferred TX, mismatched SHA/CRC, mislabeled response context or positive authority flag. **Recovery:** offline input replay; installed CO unchanged. **Limit:** no XTR fresh-state execution; 256 repeated synthetic cases are not independent physical trials.

## R6-P74CV — COMPLETE / POSITIVE descriptive, COMPLETE / INCONCLUSIVE prospective predictor
**Hypothesis/baseline:** retained/FC23 or first two post-response host-seconds uniquely predict authenticated session; baseline CR negative control and CT/CU original six response-bearing contexts. **Single change:** response-relative 2-second shape summary without changing original decoder/window. **Fields:** retained `04A6/13`, `085F/5`, FC23, first `03E8/14` ACK-shape. **Positive/descriptive:** 4 fast contexts have first ACK-shape <=2 host seconds, 2 slow contexts do not, both later do; absent context has 41 request shapes without response shape. **Negative/abort:** no pre-response exclusive owner or causal predictor; do not infer semantic acceptance/TX. **Recovery:** offline replay, TX DENY. **Limit:** host-time/ACK-shape as observations only, ATEC first-page geometry different.

## R6-P74CU — COMPLETE / NEGATIVE for decoded status/FC23/FC03-shape change at first ACK
**Hypothesis/baseline:** a new status-pair or FC23/FC03 request shape directly precedes the first short FC16 ACK in the two slow Eco5 contexts; baseline CT. **Single change:** inspect event-kind/status-pair transitions before/after first ACK without assigning semantics to `OTHER`. **Observed:** each slow response→ACK window has 102 STATUS, 102 first-page requests, 0 extra FC23/FC03 requests, 611–612 OTHER; adjacent status pairs both (40,10), already repeated earlier. **Positive criterion not met:** no unique new observed status/FC23/FC03 shape. **Abort:** source integrity mismatch, speculative interpretation or TX. **Recovery:** source replay only. **Unknown:** content of OTHER frames, external gateway participation, physical owner.

## R6-P74CT — COMPLETE / POSITIVE, offline source-verified timing/retry reconstruction
**Hypothesis/baseline:** CQ two ~108.5s first-ACK delays contain first-page repeats; baseline CQ narrow 120s vs CJ broad windows. **Single change:** count retries/gaps in original decoded window. **Observed:** Eco5 Sep28 contexts 3205 and 5457 each 102 `03E8/count14` requests before ACK-shape (101 retries), first ACK at 108.653/108.507 host seconds; four other first ACK at 0.122–0.137 s. **Positive:** exact source-shape reproduction. **Negative/abort:** hash/CRC/window/prefix mismatch, false electrical-slot deduction. **Recovery:** offline replay, no physical action. **Limit:** these are genuine cross-model host timestamps, not controller timer/physical EOF.

## R6-P74CH–CS — cumulative preservation of intervening work
[Detailed additive chronology](R6_P74CH_TO_CS_20261013_HANDOFF.md). **CH user-live COMPLETE/POSITIVE RX-only soak** (17m51.752s); **CI/J/K/L/M bounded offline positive** (CL direct journal-to-CK **NO-GO** because missing distinct ACK/response metadata); **CN user-live COMPLETE/POSITIVE RX-only duration** with internal feature coverage partial; **CO user-live COMPLETE/POSITIVE on-demand diagnostic** (`accepted=214 rejected=0`, no FC23/ACK shapes); **CP offline chronology PASS but early-resync cause INCONCLUSIVE**; **CQ COMPLETE/POSITIVE bounded offline 120s-vs-broad context replay**; **CR COMPLETE/NEGATIVE** retained+FC23 as sufficient response/owner discriminator; **CS COMPLETE/POSITIVE for dump occurring after resync, cause INCONCLUSIVE**. The CO early single resync and historical P5 fault latch are retained, not erased. No new native TX authority gained.

---

# 2026-10-13 — R6-P74BW–CD sequential offline experiments (additive; newest first)

> Complete reproducible sanitized findings: [R6_P74BW_TO_CD_OFFLINE_20261013.md](R6_P74BW_TO_CD_OFFLINE_20261013.md). Every experiment below is **COMPLETE / POSITIVE for its explicitly bounded offline analysis**; all physical native actions NOT RUN, TX HARD DENY. Original seven genuine cross-model raw files source-hash checked, 25,031/25,031 pre-delimited CRC-good ADUs. No private TX code, new controller tests or ESP flash. Previous negative/inconclusive trials remain below unmodified.

## R6-P74CD — COMPLETE / POSITIVE, integrated offline host regression
**Hypothesis/baseline:** independently verified BW–CC results and unchanged staged BM C++ shadow observer can coexist fail-closed. **Only controlled change:** host-only aggregation and seven synthetic BM metadata scenarios; no ESPHome/hardware modification. **Relevant fields:** `0x0F FC23/FC16/FC03` shapes, 32-page geometry, `085F/5`, orphan `0662/33`, 7 original sources, controller epoch/owner/slot UNKNOWN. **Positive:** verified 25,031 CRC-good original frames, 210/210 deliberate CRC-corruption rejection checks, 7/7 actual BM C++ host-only scenario expectations, 7 prior stage SHA links; TX DENY. **Negative/abort:** unexpected TX, invented owner/epoch, bad CRC or rewritten EXP425/EXP388 results; stop offline analysis and preserve RX-only baseline. **Result limit:** no physical TX/recovery, no full ESPHome compile or controller semantic acceptance. **Next:** original P74AR/BX window scope reconciliation.

## R6-P74CC — COMPLETE / POSITIVE, V4.1 cancellation state contract OFFLINE ONLY
**Hypothesis/baseline:** V4.1 source lines 8590–8864 define cancel/invalidations before semantic in-flight boundary, explicit stop on unsafe or second attempt. EXP388 positive two controller restarts, other cancellation branches NOT RUN. **Only controlled change:** synthetic Cartesian test of main-state 0–7, three sub-engine states 0–7 and previous-attempt flag; no controller action. **Positive:** 8,192/8,192 host cases: 1,296 safe cancel/invalidate/wait-fresh, 2,800 stop-in-flight, 4,096 second-attempt stop; 4/4 witness-negative cases do not authorize TX. **Negative/abort:** false safe recovery in unsafe state or universal controller cancellation claims; halt local model, keep RX-only. **Result limit:** exact V4.1 source-based policy was modeled; not a direct original C++/YAML runtime execution or live EXP388 branch closure. EXP388 remains RUNNING/PARTIAL.

## R6-P74CB — COMPLETE / POSITIVE, orphan 0662 negative regression OFFLINE ONLY
**Hypothesis/baseline:** XTR EXP423 unowned 166 repeated `0662/33`; EXP425 one ACK stopped retry but expected `0683/33` tail missing (NEGATIVE); EXP426 trigger absent (INCONCLUSIVE). **Only controlled change:** genuine cross-model FC16 shape recount and 16 synthetic cases without any live ACK. **Positive:** 23 genuine `0662/33` request shapes; 28 `0683/33` request shapes; 16/16 fail-closed cases; EXP425 negative result preserved. **Negative/abort:** infer ACK causal acceptance or automatically advance to `0683`; halt replay, hardware unchanged. **Result limit:** original local XTR EXP423/425 raw traces were NOT directly reparsed; historical local observations are sourced from canonicals/previous source audit, not cross-model re-enactment.

## R6-P74CA — COMPLETE / POSITIVE, retained service 085F evidence OFFLINE ONLY
**Hypothesis/baseline:** old EXP419 inconclusive, EXP420 owner predicate contextually positive; current local XTR retained `085F/5` without independent owner. **Only controlled change:** reread exact original seven cross-model CRC-valid captures and six existing overlapping XTR ESPHome diagnostic logs. **Positive:** 331/331 genuine `0x0F FC16 085F/count5` requests contain all-zero data; 20 requests have a short ACK shape in the following host 1s; local retained observer logs stay no-owner. **Negative/abort:** promote ACK or repeated zero payload to native current-owner; stop offline, no TX. **Result limit:** counts are frames, not 331 epochs; XTR source is existing metadata only.

## R6-P74BZ — COMPLETE / POSITIVE, direct BM C++ observer host replay / V4.1 source contract
**Hypothesis/baseline:** BM source remains nontransmitting under genuine metadata and differs intentionally from older conditional active V4.1; historical EXP355/386/387 positive and EXP388 partial. **Only controlled change:** host compile of unchanged local BM `r6p74at_shared_observer.hpp`, 7 genuine pre-delimited capture streams converted to metadata, plus a seven-row documented V4.1 behavioral contract. **Positive:** g++ C++17 with UBSan, 10/10 source checks, 4,809 native metadata events successfully consumed by real BM C++ code, all authority fields false and TX DENY. **Negative/abort:** any owner/sender/epoch/slot/TX promotion, compile fault or claim to have executed V4.1 original binary; stop offline. **Result limit:** *original V4.1 was NOT directly executed*; differential behavior is source-contract comparison, not complete executable parity.

## R6-P74BY — COMPLETE / POSITIVE, host-logger perturbation sensitivity
**Hypothesis/baseline:** BV seven exceptional `0000/0005` contexts and 157 normal FC23 contexts differ in the original host timestamps but not necessarily physically. **Only controlled change:** deterministic synthetic host-time shifts (7 levels), 28 missing-record/status/gap/timing mutations, 4,608 artificially chunked/rejoined original CRC frames. **Positive:** all tests pass, model distinguishes 7 exceptional from 156 normal Eco5 in unshifted source; one normal ATEC context is counted separately; classification becomes sensitive at 0.1s adversarial perturbation. **Negative/abort:** use host classification as electrical t3.5, physical controller power-epoch or exclusive reply window; keep RX-only. **Result limit:** artificial rechunk does not model physical UART callback timing or an independent logger.

## R6-P74BX — COMPLETE / POSITIVE, 32-page ACK-shape chain, broader context windows
**Hypothesis/baseline:** P74AR P4/P5 had four complete 32/32 and two partial 10/32,12/32 in narrower episode bounds; BV/BW define seven larger context-to-context windows. **Only controlled change:** count matching original FC16 page/address/count + short ACK shapes under broad context windows, plus six deliberately removed-stage synthetic tests. **Positive:** all SIX response-bearing Eco5 *broad* windows contain 32/32 linked ACK shapes; six removed-stage tests fail safely. Two windows contain >100 first-page retries, which complicates segmentation. **Negative/abort:** overwrite prior P74AR 4-full/2-partial scoped finding or equate short ACK with semantic acceptance/owner; stop at observation-only. **Result limit:** **OPEN SCOPE DIFFERENCE** with old narrower P74AR episode bounds, not proof those previous partial exports were actually complete.

## R6-P74BW — COMPLETE / POSITIVE, gateway-absent Eco5 natural control
**Hypothesis/baseline:** BV seven Eco5 start-shaped windows, one with 41 FC23-request forms and no recorded response form. **Only controlled change:** original CRC-confirmed seven context-window replay, response-follow-on first-page comparison, and independent inspection of pre-existing collaborator condition label from the 2026-10-10 firmware-research README. **Positive:** 11/11 checks; six windows show response + subsequent first configuration page; Eco5-26 line 2512 has 41 requests without response. Existing external collaborator notes describe this segment as **gateway absent** in an A/B/A presence test with deliberate controller restarts. **Negative/abort:** invent physical controller lockup, treat host gap as measured bus silence or infer a causal effect from an unisolated gateway/restart change; stop offline, no rollback needed. **Result limit:** external reported intervention is not an independently measured local XTR powercycle or guaranteed sender attribution.

## Earlier BO–BV statuses reconciled (historical observations preserved)
- BO **COMPLETE/INCONCLUSIVE**: strong BM-source log fingerprint and observed RX parity; no independently verified exact flashed binary.
- BP **COMPLETE/POSITIVE offline**: historic parser-resync/P5 sticky fault-vs-Bridge04 recovery explained without changing safety gate.
- BQ **COMPLETE/INCONCLUSIVE**: positive bounded RX-only logs and source entity parity; full HA regression/10-min continuous recording not proven.
- BR/BS **COMPLETE/POSITIVE offline** baseline and V4.1↔V5 source audit.
- BT **COMPLETE/POSITIVE offline** cold/retained controller start-context model, no current epoch authorization.
- BU **COMPLETE/POSITIVE offline** for 7/7 status/startcontext correlation; physically verified controller power-generation still INCONCLUSIVE. Later independent README collaborator intervention labels are now linked without rewriting BU's raw-timing observations.
- BV **COMPLETE/POSITIVE offline**: seven special versus 157 normal FC23 cases, host-timing difference and one response-absent window; physical reboot/epoch remains INCONCLUSIVE.

**Historical result safety:** EXP355/386/387 bounded positive XTR, EXP388 still RUNNING/PARTIAL; EXP419 INCONCLUSIVE; EXP420 limited POSITIVE; EXP423 INCONCLUSIVE; EXP425 NEGATIVE; EXP426 INCONCLUSIVE. Cross-model Eco5/ATEC and firmware-derived semantics are NOT locally verified on current XTR V5. G01–G06 remain OPEN/HOST-ONLY PARTIAL and all native TX remains HARD DENY.

---

# 2026-10-12 — R6-P74AQ closure and R6-P74AR phase 1–9 additive results

> **Newest-first evidence update; old experiment entries remain intact below.** Source summary: [R6_P74AQ_P74AR_20261012_HANDOFF.md](R6_P74AQ_P74AR_20261012_HANDOFF.md). No code was flashed or controller experiment run as part of this documentation update.

## R6-P74AR phase 9 — PREPARED / NOT RUN (passive electrical measurement; DEPRIORITIZED)
**Hypothesis/baseline:** a separate passive RX/DE logic-level waveform could constrain physical t3.5 and DE behavior unresolved after phase 8; current P74AQ RX-only, historical V4.1 active TX. **Controlled change:** offline measurement-plan/scripts prepared only; no probe placed, no electrical reading supplied, no bus/TX effect. **Target:** UART RX GPIO18, TX GPIO17, software DE GPIO21 as ESP32 signal labels, **not verified physical test-pad wiring**. **Positive:** timed passive trace with independent voltage/ground safety and zero DE-high; **negative/abort:** unsafe probing, ground risk, unexpected DE assertion; stop acquisition, leave RX-only. **Recovery:** remove passive measurement leads; no firmware rollback required. User requested protocol gap audit first; do not mark test executed.

## R6-P74AR phase 8 — COMPLETE / POSITIVE (host safety); physical TX readiness NEGATIVE/NO-GO
**Hypothesis/baseline:** current V5/P74B distinguishes CRC frame end, FIFO admission/drain and DE release and fails closed; P74AQ live, phases 1–7. **Controlled change:** host-only C++ fault injections and static source review; no device changes. **Fields:** 9600/8E1, RX GPIO18, TX GPIO17, DE GPIO21 software default LOW, callback batching 5ms and 25ms observational quiet-time, G03–G06. **Positive:** 26/26 ASan/UBSan C++ host tests and 20/20 source checks; simulated latch/error recovery never grants native TX. **Negative:** G03 wire end and G04 exclusive slot OPEN, G05 FIFO/DE release PARTIAL HOST ONLY, G06 electrical reset/brownout fail-low OPEN; simulated release failure cannot physically force DE low. **Abort/recovery:** any active-output path or electrical proof claim from simulation rejects deployment; leave AQ unchanged.

## R6-P74AR phase 7 — COMPLETE / POSITIVE (offline audit); COMPLETE / INCONCLUSIVE (epoch/owner)
**Hypothesis/baseline:** original Connect device_client and native register catalog reveal a controller-specific uptime/bootcounter; phase6 epoch UNKNOWN. **Controlled change:** inspect supplied `device_client.zip`, exact firmware-derived 564-register catalog and reparse seven genuine cross-model archives; no ESP or controller action. **Fields:** `06EA–06F0` RTC, `0858–085E` RTC mirror, `0867` firmware version, `087B–087D` defrost, related other-profile `0871`. **Positive:** 2500 CRC-valid complete FC16 requests, 88 valid clock tuples, 20/20 offline checks; confirms previous RTC mirror interpretation. **Negative:** calendar/defrost/gateway uptime not unique power-epoch markers; unique local XTR epoch not found. Original RAUC bundles not newly unpacked or binary-diffed in this phase. **Abort/recovery:** CRC/provenance mismatch excludes candidate, remain UNKNOWN/DENY; offline only.

## R6-P74AR phase 6 — COMPLETE / INCONCLUSIVE (epoch/owner); POSITIVE (fail-closed classifier)
**Hypothesis/baseline:** grouped genuine FC23 and local V4.1 controlled power-cycle identify unique controller epoch and response owner; phase5 ACK-shape model. **Controlled change:** offline cross-model FC23 CRC recount + current P74AQ status audit, 30/30 negative/host tests. **Frames:** 163 CRC-valid canonical Eco5 `0x0F FC23` requests (99+64) in seven >12s-host-gap groups; one ATEC reference in broader count of 164. Local AQ software `EPOCH/OWNER/SLOT=UNKNOWN`. **Positive:** 30/30 tests; no false privilege even synthetic all-true. **Negative/inconclusive:** FC23, `A80E/A80F`, ESP reboot, page signature or ACK-shape cannot certify a present unique epoch/owner; EXP355 power-cycle proves only specific historical event. **Abort/recovery:** absent independent witness -> HARD DENY; no live action.

## R6-P74AR phase 5 — COMPLETE / POSITIVE (offline state classifier)
**Hypothesis/baseline:** independently re-decoded page requests and address/count ACK-shapes can form a strict linked 32-page state machine, without transmitting; phase4 original ADU replay. **Controlled change:** offline FSM with request/retry/ACK/next-page states; seven cross-model windows. **Frames:** `0x0F FC23`, FC16 `03E8/14` through 32 page geometries; ATEC `03E8/13` separately. **Positive:** four complete 32/32 ACK-shape chains, two partial 10/32 and 12/32; 150 paired page stages, 32/32 mutation tests, all TX=DENY. **Negative/abort:** missing required ACK with next page, wrong CRC/order => HOLD_INVALID; capture truncated => PARTIAL_OBSERVED, not fabricated controller cancellation. **Recovery:** offline fixture reset only; current AQ unchanged.

## R6-P74AR phase 4 — COMPLETE / POSITIVE (offline full-raw page/ACK shape replay)
**Hypothesis/baseline:** phase3 prior 32 metadata can be recreated independently from original raw frames; phase2 windows. **Change:** parse full original CRC-valid FC16 page and short FC16 ACK shapes; count retries and source-line timestamps. **Positive:** four of six Eco5 sequences 32/32, two 10/32 and 12/32; initial `03E8/14` retried ~102 times with first linked short ACK ~108s later in the two partial examples; 18/18 tests. **Negative/abort:** ACK-form correlation != physical source/semantic acceptance; original XTR EXP355/386 timestamped logs not available for fresh replay; no TX. **Recovery:** offline only.

## R6-P74AR phase 3 — COMPLETE / POSITIVE (offline initial classifier)
**Hypothesis/baseline:** source windows can be recognized with CRC and shape/sequence tests; phase2. **Change:** host Python replay without output path. **Positive:** seven windows, 12/12 tests, TX denied. **Limitation:** 32-page counts still derived from prior episode metadata, not original per-page independent replay; this was remedied in phases 4/5. **Abort/recovery:** fail closed on bad frame or temporal order, no device action.

## R6-P74AR phase 2 — COMPLETE / POSITIVE (offline original window audit)
**Hypothesis/baseline:** phase1 seven cross-model FC23→first-page candidates can be source-anchored. **Change:** original bus log line, timestamp, adjacent/intervening frames checked. **Positive:** seven FC23 response-shape anchors, six Eco5 first `03E8/14`, ATEC `03E8/13`; four immediate Eco5 first pages and two interleaved; no local owner attribution. **Negative/abort/recovery:** logged response shape does not prove physical sender/slot; preserve UNKNOWN, no bus action.

## R6-P74AR phase 1 / parent — RUNNING / PARTIAL (offline research)
**Hypothesis/baseline:** genuine Online/DCM captures, Thermia Connect firmware and historical XTR V4.1 can constrain native 0x0F session transitions; P74AQ smoke and historical EXP355/386. **Controlled change:** evidence ledger and preliminary passive-only model; no new YAML, TX or controller reset. **Positive:** established evidence/provenance separation and reproducible next questions; **negative/abort:** no contemporary owner/epoch/slot, no live V5 approval claim; recovery RX-only.

## R6-P74AQ — COMPLETE / POSITIVE (BOUNDED LIVE RX-ONLY SMOKE, user-requested functional closure)
**Hypothesis/baseline:** P74AQ shadow safety gate integrates into P74AL observer without loss, hold or unintended TX; P74AM RX-only endurance and prior P74AL. **Change:** user ran prepared P74AQ firmware; no TX path enabled. **Observed:** supplied 2026-10-12 17:04:50–17:08:10 log (200.261s), 7 AQ EV 715→964 SEQ aligned HOLD=0, 20 AL snapshots ending EV 965, parser anomalies=0, UART writes/software TX=0, no API-buffer warnings. **Positive:** bounded RX-only gate verified. **Limitations/negative:** initial planned 5 min not met; HA full production regression not independently checked; electrical DE and current session epoch/owner/slot UNKNOWN; no observed fresh FC23/32/32. **Abort/recovery:** any new TX/HOLD/parse regression -> stop later testing and recover last known-good RX-only P74AL; no abort triggered in observed sample.

**Next proposed work, NOT PREPARED / NOT RUN:** source-based V4.1↔V5 gap audit of EXP355–455 and ownership/rejoin/cancellation rules, especially 085F and 0662 after EXP423/425. Preserve successes *and* negative/inconclusive historical outcomes. P74AR overall remains RUNNING/PARTIAL; do not initiate active bus tests by publishing this entry.

---

# 2026-10-12 — R6-P74W–P74AI newest-first experiment reconciliation

> Dated additive entries; older experiment narratives remain intact below. **Offline successes never imply ESPHome compilation or physical bus execution.** Restore last user-proven P74AB for any later passive deployment regression; no live TX is authorized.

## R6-P74AI — COMPLETE / POSITIVE (DIRECT ORIGINAL PYTHON CORE, OFFLINE)
**Hypothesis/baseline:** unchanged P74AF C++ metadata owner projector agrees with original public Python `Core` for unqualified recorded states; previous P74AI was RUNNING/PARTIAL because full original module had not actually run. Baseline P74AB live RX-only, AF–AH offline, original module blob `671af7b27d2fbc2df988f4f080d13c7f06e6c496`. **Controlled change:** import and run SHA-pinned original `xtr_dcm_reference_core.py`, directly re-decode archived raw ADUs and enrich *offline-only* metadata; no projector/YAML change. **Frames:** slave 0x0F FC16/FC03/FC23; canonical 0730/8 read and 071C/8 write FC23 shape; exact start/count and owner class. **Positive observed:** 4488/4488 Python↔C++ owner parity, 4394 raw genuine Eco5/ATEC ADUs and 94 collaborator shape-only metadata, 16/16 local XTR journal metadata, 7/7 synthetic cases; 164 FC23 canonical shapes `POLICY_OPEN, tx=False`, 334 OTHER→FC03 response; zero live TX. **Negative criterion:** failed SHA/CRC, owner mismatch, guessed missing bytes or physical TX; none observed. **Abort/recovery:** stop offline run on mismatch; discard enriched fixture, P74AB unaffected. **Scope:** direct Python methods in default-unqualified state, *not* exhaustive stateful equivalence or physical ownership. This supersedes P74AI earlier PARTIAL status without deleting the original observation.

## R6-P74AK — COMPLETE / POSITIVE OFFLINE; ACTIVE NO-GO
**Hypothesis/baseline:** central response-review boundary can remain physically nontransmitting for any model intent or evidence flags; baseline AF–AH and P74AB live RX. **Change:** host-only HARD-DENY review contract, no output API. **Fields:** candidate owner/response type and eight simulated evidence booleans. **Positive:** 436720 C++ ASan/UBSan assertions; 34/34 static checks; even all-true test evidence cannot trigger TX. **Negative/abort:** any `tx_allowed=true`, UART/GPIO/DE/serializer source or missing deny => stop; no such path introduced. **Recovery:** discard host code only. No ESPHome build/flash.

## R6-P74AJ — COMPLETE / INCONCLUSIVE (CONTROLLER EPOCH)
**Hypothesis/baseline:** local full-word archives contain an independent controller-epoch indicator; baseline P74W/P74AB local logs and earlier native reconnection evidence. **Change:** read-only analysis of two local logs plus seven existing archives. **Fields:** A80E, A80F, FC23, callback gap and controller-power marker. **Positive criterion:** defined register and independently verified controller reset/uptime before/after. **Result:** not met. A80E switched 0000↔0020 eleven times over two recorded windows without established reset; inadequate as standalone epoch witness. A80F constant *within* each sampled run but unvalidated. **Negative criterion:** fluctuation without independent reset disqualifies A80E as a standalone witness; **abort/recovery:** offline-only, exclude wrongly attributed captures, no bus action.

## R6-P74AH — COMPLETE / POSITIVE OFFLINE (REPLAY)
**Hypothesis/baseline:** AF/AG no-TX classifier withstands real shape metadata and mutations; P74AB/AF/AG baseline. **Change:** host replay and fault injection only. **Frames:** native FC03/FC16/FC23, 32 XTR config geometries, service/runtime metadata. **Positive:** 956305 ASan/UBSan assertions; 4488 cross-model shape records, 16 local events, synthetic 32/32, 30000 malformed/mutated, 100000 runtime; P74X 127/127, P74W 30/30, Y–AA 1341/1341 and 48/48 source checks. **Negative/abort:** false owner promotion, unexpected TX or missing HOLD; abort host migration if seen. **Recovery:** remove offline adapter. Full original Python module was *not yet* run at AH; see subsequent AI closure.

## R6-P74AG — COMPLETE / POSITIVE OFFLINE (DENY LEDGER)
**Hypothesis/baseline:** a single central passive ledger can classify intents and sticky-HOLD integrity/sequence faults; AF and P74AB baseline. **Change:** standalone `IntentLedger`, no UART/DE. **Fields:** seq, integrity, FC/start/count, possible owner. **Positive:** sticky HOLD and never physical TX in host tests; **negative/abort:** any privilege promotion or continued hypothetical intent after eventgap. **Recovery:** remove host-only ledger; no device action.

## R6-P74AF — COMPLETE / POSITIVE OFFLINE (RESPONSE-INTENT)
**Hypothesis/baseline:** P74AB's journal metadata can be mapped to public reference owner/response-class ontology without fabricated payload or session authority. **Change:** standalone pure C++ shape mapper, original ESPHome unchanged. **Frames:** FC23, FC16, FC03, XTR config and runtime geometry. **Positive:** exact known shape/enum source alignment; owner at most `POLICY_OPEN`; `tx_allowed=false`. **Negative/abort:** incorrect geometry, invented owner, physical TX API. **Recovery:** discard offline code; continue P74AB.

## R6-P74AE — COMPLETE / NEGATIVE (ACTIVE TX READINESS; OFFLINE ASSESSMENT)
**Hypothesis/baseline:** current V5/P74AB may already meet physical/session authorization conditions; baseline P74AC/AD. **Change:** evaluate 12 readiness gates, no bus test. **Positive criterion:** independently proven epoch, owner, slot, physical DE/FIFO and safe device adapter. **Negative result:** only normal RX-only health is locally proven, other 11 gates remain unmet/partial; **NO-GO**. **Abort/recovery:** retain P74AB HARD DENY; no attempted TX or rollback of controller needed.

## R6-P74AD — COMPLETE / POSITIVE SOURCE-ONLY
**Hypothesis/baseline:** P74AB retains exactly one CRC-qualified receive fanout and no new live TX route; P74AB YAML and nine headers baseline. **Change:** static source audit only. **Frames:** 0x0F callback/journal/stream/ledger. **Positive:** 38/38 checks; **negative/abort:** duplicated reader, added TX/DE path, altered production blocks. **Recovery:** no source modification made.

## R6-P74AC — COMPLETE / POSITIVE SOURCE AUDIT
**Hypothesis/baseline:** original V4.1 active TX sites reduce to existing owner families. **Change:** offline spot-check of original v4.1 blob `8e8a82689e53528a8b751a1abbd901f683b6b238` against prior 58-site route inventory (not fresh 58-site recount). **Relevant:** 2 handshake sites, 32 ordered bootstrap, 1 legacy export recovery, 1 runtime ACK, 18 mailbox paths, 4 semantic paths. **Positive:** six-family inventory reconciled; **negative/abort:** do not equate source sites to confirmed emitted frames or reuse broad old runtime allowances. **Recovery:** no device change.

## R6-P74AB — COMPLETE / POSITIVE LIVE RX-ONLY, NORMAL RUNTIME
**Hypothesis/baseline:** P74X corrected P74W plus P74YZ provenance ledger preserves RX performance; baseline P74W live. **Change:** one additional observer and passive post-prefix classifier, existing callback, no TX. **User evidence:** `Pasted text(20261012-095002).txt` 11:46:13–11:49:33; P74AB 823→1101, stage0, prefix0/32, retry/follow/quarantine/gap0, no FC23 or paired ACK, epoch/owner/slot unknown, all displayed software TX and new parser/drop discrepancies0. **Positive:** bounded normal-runtime observer health. **Negative/abort:** new parser errors, unexpected DE/software TX or HA regression; none evidenced. **Not exercised:** manual Configuration dump, bootstrap, cancellation or independent physical DE. **Recovery:** restore known-good P74W RX-only if later regression; maintain P74AB otherwise.

## R6-P74AA — COMPLETE / POSITIVE OFFLINE
**Hypothesis/baseline:** passive provenance/cancellation ledger remains fail-closed; P74W/X baseline. **Change:** C++ ledger plus static YAML checks. **Frames:** FC23, FC16 ordered config, runtime and FC03 metadata. **Positive:** 1341/1341 ASan/UBSan, 15/15 provenance and 24/24 YAML/source checks. **Negative/abort:** any TX or owner promotion. **Recovery:** discard code; no bus operation.

## R6-P74Z — COMPLETE / INCONCLUSIVE (ACTUAL CANCELLATION)
**Hypothesis/baseline:** distinguish legitimate first-page retry from interrupted bootstrap and controller cancellation; EXP388 partial, Eco5 historical captures. **Change:** passive first-page retry classification. **Frames:** first 03E8/14, rest of 32-page sequence. **Positive software result:** in four of six Eco5 candidate windows full geometry, two windows repeated first 03E8 geometry 102 times; observer still denies TX. **Actual cancellation not proven:** EXP388 pre-semantic and refresh-only cancellation branches remain unexecuted. **Negative/abort/recovery:** on uncertain interrupted bootstrap remain capture-only/HOLD; no controller action.

## R6-P74Y — COMPLETE / POSITIVE OFFLINE (PROVENANCE)
**Hypothesis/baseline:** distinguish seven unique response-anchored handshake episodes instead of counting repeated FC23 requests separately; P74G/H/I baseline. **Change:** CRC-valid source-capture metadata extraction, request dedup and source tagging. **Frames:** FC23 shape and first FC16 03E8 (Eco5 /14, ATEC /13). **Positive:** 4488 native 0x0F records, seven candidate episodes; 15/15 checks; 21 ATEC intervening logged frames. **Negative/abort:** logger timestamp not physical wire-end, sender/owner unproven; exclude uncertain candidate, no bus changes.

## R6-P74X — COMPLETE / POSITIVE OFFLINE (POST-PREFIX GUARD)
**Hypothesis/baseline:** P74W false HELD after hypothetical synthetic 32/32 prefix can be eliminated without unsafe promotion. **Change:** passive post-prefix event classification only. **Frames:** known FC16 follow-on capture-only; unexpected FC23 or 03E8/14 new-epoch candidate sticky HELD; CRC/seq faults HOLD. **Positive:** 127/127 sanitizer tests and P74W regression 30/30. **Not live-deployed on its own**; included in later P74AB. **Abort/recovery:** revert host patch on regression.

## R6-P74W — COMPLETE / POSITIVE LIVE RX-ONLY
**Hypothesis/baseline:** persistent eventstream survives P74L 32-entry journal overwrite; baseline user-live P74L. **Change:** passive streaming observer, no production UART/TX change. **Evidence:** user log `Pasted text(20261012-083525).txt` P74W events 78→342, journal overwrite, zero observed parser drops/resync/byte diff/software TX, no FC23/32/32. **Positive:** bounded normal RX; **negative/abort:** RX regression/DE high; **recovery:** last known-good P74L RX-only.

**Historical EXP388 remains RUNNING / PARTIAL. No physical responder or new device flash is implied by the offline tests.**

---

# 2026-10-12 — R6-P74B–P74L newest-first reconciliation

> This is an additive summary of newly reviewed experiment evidence. Keep all older P1–P74A and EXP history below. For every live result below, software-reported GPIO LOW and zero counters are **not** oscilloscope proof of physical DE fail-low. Controller epoch/owner/slot remain UNKNOWN; native TX DENY.

## R6-P74L — PREPARED / NOT RUN
**Hypothesis:** an RX-only V5/P60 per-frame callback journal can provide ordered individual native events for a later P74J adapter without changing existing receive semantics. **Baseline:** user-deployed P74E RX-only, P74J/P74K offline models. **Controlled change:** prepared full YAML plus bounded last-32-event C++ journal; configuration diagnostic button dumps up to 16 events. **Frames/fields:** received slave 0x0F FC16/FC23 metadata, sequence, callback timestamp, address/count, parser integrity and provenance limitations. **Positive:** user compile/flash, stable production HA/RX, monotonic event IDs and correctly decoded metadata, no new drops/mismatch and TX=0. **Negative:** malformed metadata, missing events or new RX regression. **Abort:** unexpected software TX, DE HIGH, crash, new parser fault or production outage. **Recovery:** restore the last user-proven P74E RX-only firmware and capture logs; rolling back ESP does not prove clearing controller pending state. **Result:** prepared source/host checks only; **no user build, flash or live result received**. No native active TX allowed.

## R6-P74K — COMPLETE / POSITIVE (OFFLINE ADAPTER ONLY)
**Hypothesis:** P74E counters can be safely adapted without fabricating P74J ordered events. **Baseline:** P74E live, P74J synthetic event model. **Change:** offline cumulative-counter adapter, tests and two overlapping P74E log replays. **Fields:** 43 P74E snapshots, FC16 up to 392, FC23=0, mailbox=0, RX status; no individual ACK events. **Positive:** 10/10 host tests, no fictional bootstrap/authority. **Negative:** no complete 32/32 timeline inferable from counters. **Abort/recovery:** host DENY on counter reset/missing progression; no bus action.

## R6-P74J — COMPLETE / POSITIVE (OFFLINE MODEL ONLY)
**Hypothesis:** event-driven bounded state progression models native first-response and 32-page export without authorizing actual output. **Baseline:** historical V4.1 EXP355/386 and genuine cross-model reference episodes. **Change:** Python synthetic 33-step machine and 10 host tests, selected first-page episode replay. **Frames:** 0x0F FC23, 03E8/count14 first page, 32 XTR page geometries, runtime qualifications. **Positive:** 10/10 host tests; correct incomplete/out-of-profile DENY. **Negative:** capture replay is not new full 32/32 XTR or sender evidence. **Abort/recovery:** sticky HELD/DENY for resets, duplicate/unknown actions; offline reset only.

## R6-P74I — COMPLETE / POSITIVE (OFFLINE SOURCE PROVENANCE)
**Hypothesis:** original sniffer source and firmware research clarify logger times and ATEC capture identity. **Baseline:** P74G/H. **Change:** read-only inspection of `thermia-bus-sniffer` code and Thermia Connect research. **Fields:** original `<seconds> <hex>` format, host `time.time()` after receive chunk, 20261003 ATEC count13. **Positive:** source-level chunk timestamp semantics and documented ATEC attribution. **Negative:** logger revision used in each capture not independently proved. **Abort/recovery:** no bus action.

## R6-P74H — COMPLETE / POSITIVE (OFFLINE CAPTURE AUDIT)
**Hypothesis:** source provenance and timestamp quality can be qualified before timing conclusions. **Baseline:** P74G. **Change:** re-read three genuine capture files. **Positive:** 10719-frame Eco5 (26 Sep), 9174-frame Eco5 (28 Sep), 2687-frame (3 Oct) inventories; nondecreasing host times, distinct geometry. **Negative:** raw logs alone do not state exact model or wire-end timing; 3 Oct ATEC attribution established later in P74I, not retroactively claimed as P74H direct evidence. **Abort/recovery:** no bus action.

## R6-P74G — COMPLETE / POSITIVE (OFFLINE TEMPORAL REPLAY)
**Hypothesis:** genuine archived request/response/first-page episodes permit ordering and approximate host timestamp intervals, not exclusive TX windows. **Baseline:** P74F, existing Eco5 and 3 Oct captures. **Change:** seven offline episode extractions (six Eco5, one later attributed ATEC). **Frames:** FC23 request→response→03E8; Eco5 first page count14, ATEC count13. **Positive:** seven answer-followed-by-first-page sequences; 3 Oct has 21 intervening frames. **Negative:** 29–63 ms FC23 host intervals not electrical on-wire safe slots. **Abort/recovery:** no bus action.

## R6-P74F — COMPLETE / POSITIVE (OFFLINE HISTORICAL SOURCE RECONSTRUCTION)
**Hypothesis:** V4.1 source and canonically recorded EXP355/386 identify historical native bootstrap phases. **Baseline:** P74E live and V4.1 guarded restart work. **Change:** source-only sequence/stage comparison, no new raw EXP355/386 trace available in that analysis. **Positive:** first FC23, 32 ordered page stages, later runtime clarified. **Negative:** current P74E lacks physical epoch/owner/slot evidence. **Abort/recovery:** no bus action.

## R6-P74E — COMPLETE / POSITIVE (LIVE RX-ONLY SLOT MONITOR)
**Hypothesis:** monitor source evidence separately from approval. **Baseline:** P74D alternative live RX-only. **Change:** new source-only slot evidence monitor, no TX. **User result:** two overlapping real P74E logs, FC16 progressing, FC23=0, mailbox=0, resync=0, drops=0, B11C/D differences=0; user triggered P74E audit; owner/epoch/sender/wire-end/slot UNKNOWN and TX=DENY. **Positive:** monitor correct and no observed RX regression in window. **Negative:** no physical responder slot qualified. **Abort/recovery:** any new parser/DE/TX anomaly => restore P74D; not observed.

## R6-P74D alternative — COMPLETE / POSITIVE (LIVE DENY EXECUTOR ONLY)
**Hypothesis:** integrate Executor with read-only health axes while keeping native TX hard disabled. **Baseline:** P74B FIX1 live. **Change:** Executor ticks in DenyLocked and separate historic P5 from new RX fault. **User result:** P74D logs show UART present, DENY_LOCKED, current RX clean, P5_HISTORY=1, NEW_HOLD=0, resync stable at 9, UART writes/TX attempts=0, DE software LOW. **Positive:** monitor runs on ESP and fails closed. **Negative:** physical TX/drain/DE behavior not exercised. **Abort/recovery:** P74B RX-only rollback if new faults; none confirmed.

## R6-P74D isolated bench proposal — SUPERSEDED / NOT RUN
**Hypothesis:** externally isolated UART/DE bench would validate physical TX error paths. **Baseline:** P74C audit. **Controlled design:** optional separate board and isolated A/B, never installed. **Result:** user rejected all rewiring/additional ESP; proposal superseded by P74D alternative. **No live or active output occurred.**

## R6-P74C — COMPLETE / POSITIVE (OFFLINE SOURCE AUDIT)
**Hypothesis:** P5 sticky-historical faults are distinguishable from live RX and P74B UART probe is not physical TX proof. **Baseline:** P74B FIX1 source and two live logs. **Change:** static/source readiness checks (25/25), 14-gate matrix audit (zero physical TX permission). **Positive:** explains absolute P5 resync latch and baseline-delta healthy RX coexistence; P74B only inspects borrowed UART. **Negative:** no physical owner/epoch/slot/DE validation. **Abort/recovery:** no live change.

## R6-P74B FIX1 — COMPLETE / POSITIVE (LIVE BORROWED UART RX-ONLY)
**Hypothesis:** ESPHome borrowed UART can be identified without transmitting. **Baseline:** P74A RX-only positive. **Change:** corrected ESP-IDF/ESPHome header compatibility after initial compile failure. **User result:** compiled/flashed FIX1; repeated logs show UART 0 present, RX stable, software DE LOW, owner/slot unknown, no UART write/TX. **Positive:** compiler/device-level RX-only preflight. **Negative:** no instantiated physical executor or FIFO/drain proof. **Abort/recovery:** return to known-good passive image if RX destabilizes; no such result supplied.

---

# 2026-10-11 — Newest reconciliation R6-P50–P59 (all OFFLINE)

**Shared baseline:** user-flashed R6-P37 DENY-only RX-only; historical full-restart 32/32 native XTR EXP355/386 COMPLETE/POSITIVE, EXP388 RUNNING/PARTIAL. R6-P41–P49 results are retained below, newest-first. **Every P50–P59 step used offline source/capture/host fixtures only:** no new YAML, flash, GPIO/DE high, UART TX or controller recovery. **Shared positive criterion:** reproduce correct host-only handling without a physical-output path; **negative/abort:** wrong address/count, ambiguous prefix, bad CRC, unknown owner, peer or false evidence upgrade => sticky DENY. **Recovery:** software-only reset/drop, never claim that an ESP rollback clears controller-side pending state. The genuine seven captures were already frame-delimited and are from other models.

## R6-P59 — Combined capture-and-scope readiness audit — COMPLETE / POSITIVE OFFLINE / ACTIVE NO-GO
**Hypothesis:** Combined capture-and-scope readiness audit. **Baseline:** P44 gates, P51–P58. **Exact controlled change:** integrated host pipeline and review model on seven cross-model captures; source and compile-fence audits. **Relevant frames/fields:** 25,031 pre-framed CRC-valid records, 9,968 FC16/23 request shapes; 32 stages. **Positive/result:** 735,721 total P56–P59 sanitizer assertions, 60,000 fault cases, static 15/15, four build fences. **Negative/abort/unknown:** physical TX remains NO-GO: driver, slot, epoch/owner, incomplete bootstrap recovery UNKNOWN. **Recovery:** no bus state changed; P37 retained.

## R6-P58 — Fault containment in scoped synthetic bootstrap — COMPLETE / POSITIVE OFFLINE
**Hypothesis:** Fault containment in scoped synthetic bootstrap. **Baseline:** P57, P42/P43. **Exact controlled change:** 32 wrong-step/stall positions, replay, reset and unqualified runtime/write scenarios plus deterministic random faults. **Relevant frames/fields:** 32 FC16 page proposals, session/epoch/deadlines, 085F/0708. **Positive/result:** 60,000 seeded cases; sticky abort; no physical output, within P56–P59 combined assertions. **Negative/abort/unknown:** any post-abort advancement or implicit scope inheritance invalid. **Recovery:** no bus state changed; P37 retained.

## R6-P57 — Central transaction review/authority contract — COMPLETE / POSITIVE OFFLINE
**Hypothesis:** Central transaction review/authority contract. **Baseline:** P45, P51–P56. **Exact controlled change:** host C++ one-shot scoped reviews; page progression requires separate synthetic ACK-observation event. **Relevant frames/fields:** initial 0x0F FC23; 03E8/count14 through 06F4/count19; later 085F/0708. **Positive/result:** 32/32 fixture recognized, each separate action still TX DENY. **Negative/abort/unknown:** fixture identities/deadlines are not independently measured controller facts. **Recovery:** no bus state changed; P37 retained.

## R6-P56 — Historical distributed TX source inventory — COMPLETE / POSITIVE OFFLINE
**Hypothesis:** Historical distributed TX source inventory. **Baseline:** V4.1 historical EXP355/386, P37 and P44. **Exact controlled change:** source-only compare older working responder with new output-free P37; no code port. **Relevant frames/fields:** first FC23, bootstrap FC16, 0708/semantic classes. **Positive/result:** 58 textual write_array and 58 flush occurrences inventoried; no private code published. **Negative/abort/unknown:** text occurrences are not 58 proven on-wire packets; safe physical execution not implemented. **Recovery:** no bus state changed; P37 retained.

## R6-P55 — ESPHome source compatibility/readiness — COMPLETE / POSITIVE OFFLINE / ACTIVE NO-GO
**Hypothesis:** ESPHome source compatibility/readiness. **Baseline:** FIX4/P37 and P51–54. **Exact controlled change:** static production entity/top-level block comparison; distinguish UART RX-debug callback from hardware settings; build fences. **Relevant frames/fields:** P37 RX UART, B11C/B11D, HA entities, DE. **Positive/result:** 23/23 source checks; production preserved, additional P37 gate diagnostic. **Negative/abort/unknown:** no ESPHome compile, electrical DE or driver test; active NO-GO. **Recovery:** no bus state changed; P37 retained.

## R6-P54 — Cross-model replay and adversarial regression — COMPLETE / POSITIVE OFFLINE
**Hypothesis:** Cross-model replay and adversarial regression. **Baseline:** P48/P49/P53. **Exact controlled change:** 25,031 pre-delimited records replayed 3 ways plus 50,000 seeded faults. **Relevant frames/fields:** FC03/04/16/23, optional session fixture. **Positive/result:** 75,093 chunk replays; P51–P55 1,828,923 sanitizer assertions. **Negative/abort/unknown:** these are not genuine raw UART-callback timing or native XTR session tests. **Recovery:** no bus state changed; P37 retained.

## R6-P53 — RX→event→session integration — COMPLETE / POSITIVE OFFLINE
**Hypothesis:** RX→event→session integration. **Baseline:** P45/P47/P49 and P51–52. **Exact controlled change:** join existing host models with provenance-preserving metadata adapter. **Relevant frames/fields:** FC16/23 request shapes and synthetic 32-page sequence. **Positive/result:** combined host integration passes, observed traffic never grants TX. **Negative/abort/unknown:** real session owner and controller epoch remain unproven. **Recovery:** no bus state changed; P37 retained.

## R6-P52 — Boundary provenance type labeling — COMPLETE / POSITIVE OFFLINE
**Hypothesis:** Boundary provenance type labeling. **Baseline:** P48–51. **Exact controlled change:** distinguish CaptureRecord, BenchDeclaredPhysical, CallbackIdleAssumption and None; hard-false authority bits. **Relevant frames/fields:** frame origin, CRC/length, callback timing metadata. **Positive/result:** source labels preserved; unknown epoch/owner remains false. **Negative/abort/unknown:** label is not proof of physical wire idle or permission to reply. **Recovery:** no bus state changed; P37 retained.

## R6-P51 — Callback jitter, coalescence and ambiguity — COMPLETE / POSITIVE OFFLINE
**Hypothesis:** Callback jitter, coalescence and ambiguity. **Baseline:** P49/P50. **Exact controlled change:** simulate chunk timing, concatenation, CRC prefix and incomplete batches; explicit record boundary only. **Relevant frames/fields:** FC03/04 ambiguous prefix; FC16/23 geometries; 25ms callback idle. **Positive/result:** part of 1,828,923 P51–P55 assertions; no timing-only frame commit. **Negative/abort/unknown:** physical wire-end timing remains UNKNOWN. **Recovery:** no bus state changed; P37 retained.

## R6-P50 — Boundary provenance source audit — COMPLETE / POSITIVE OFFLINE (WIRE-BOUNDARY CLAIM NEGATIVE)
**Hypothesis:** Boundary provenance source audit. **Baseline:** P37, B11C/B11D, P49. **Exact controlled change:** inspect order of raw-ingress, V5 parser and 25ms callback-idle reconstruction. **Relevant frames/fields:** UART callbacks, candidate CRC boundaries. **Positive/result:** 15/15 source checks; B11D raw ingress independent of V5 parser. **Negative/abort/unknown:** NEGATIVE for claim that 25ms callback idle or B11C/B11D parity proves electrical wire end; ambiguity capture-only. **Recovery:** no bus state changed; P37 retained.

---
# 2026-10-11 — R6-P41–P49 offline experiment reconciliation

**Shared baseline:** deployed R6-P37 RX-only, historical EXP355/386 full native cold-restart success, EXP388 RUNNING/PARTIAL. All entries below are COMPLETE/POSITIVE **within offline scope**; R6-P43 isolated abort causality is INCONCLUSIVE, R6-P44 active NO-GO. **Shared positive criterion:** bounded evidence extraction or host tests with no physical TX. **Shared negative/abort criterion:** ambiguous frame, unproven owner, bad CRC/geometry, unexpected peer, unauthorized TX or false controller-state promotion -> capture-only/DENY. **Recovery:** no device intervention was performed; reset of a host fixture does not prove real controller recovery, and P37 stays installed. Frame descriptions are public geometries only, no private responses or control tooling.

## R6-P49 — Host C++ raw RX chunks→event bridge — COMPLETE / POSITIVE OFFLINE
**Hypothesis:** Host C++ raw RX chunks→event bridge. **Baseline:** P47/P48. **Exact controlled change:** bounded accumulator; external frame-end input; CRC/geometry/prefix failure DENY. **Relevant frames/fields:** FC03/04 ambiguity; FC16/23 request shapes. **Positive/result:** 25,031 framed records ×3 =75,093 replays; 1,171,252 sanitizer assertions, no TX. **Negative/abort/unknown:** unbounded/ambiguous/bad frame rejected; boundary not independently proven. **Recovery:** host DENY/reset only; no bus state changed.

## R6-P48 — Source identity versus CRC frame geometry — COMPLETE / POSITIVE OFFLINE
**Hypothesis:** Source identity versus CRC frame geometry. **Baseline:** P37/P45/P47. **Exact controlled change:** seven genuine cross-model captures indexed and conservative classifier tested. **Relevant frames/fields:** FC23 requests 5096/replies 3532; FC16 requests 4872/ACK shapes 3730; FC03/04 and FC06. **Positive/result:** 25,031/25,031 CRC valid; 125,167 assertions; owner/epoch/TX promotions=0. **Negative/abort/unknown:** no physically authenticated sender or UART-boundary proof. **Recovery:** host DENY/reset only; no bus state changed.

## R6-P47 — P37-like RX-to-P45 normalized adapter — COMPLETE / POSITIVE OFFLINE
**Hypothesis:** P37-like RX-to-P45 normalized adapter. **Baseline:** P45/P46. **Exact controlled change:** host C++ event adapter and synthetic fixtures; no firmware wiring. **Relevant frames/fields:** 32 staged FC16 requests; FC23/0708 observations. **Positive/result:** 8,000,146 sanitizer assertions, 100,000 randomized sequences; all TX DENY. **Negative/abort/unknown:** wrong origin/order/peer/reset/prefix abort; synthetic session ID not real owner. **Recovery:** host DENY/reset only; no bus state changed.

## R6-P46 — Adapter interface source audit — COMPLETE / POSITIVE OFFLINE
**Hypothesis:** Adapter interface source audit. **Baseline:** P44/P45 and installed P37. **Exact controlled change:** audit 15 source boundaries; adapter not yet implemented. **Relevant frames/fields:** P37 RX FC23/FC16/0708, UART 9600 8E1, DE. **Positive/result:** 14/14 static checks; no P37 executable output. **Negative/abort/unknown:** unknown origin/slot/physical DE forbids active bridge. **Recovery:** host DENY/reset only; no bus state changed.

## R6-P45 — Host-only session model — COMPLETE / POSITIVE OFFLINE
**Hypothesis:** Host-only session model. **Baseline:** P40/P44; historical EXP355/386. **Exact controlled change:** C++17 32-stage observer, 2048 guard cases and deliberate firmware compilation fence. **Relevant frames/fields:** 03E8/count14 to 06F4/count19 and 085F/0708. **Positive/result:** 3,920,085 assertions; 100,000 random sequences, TX DENY. **Negative/abort/unknown:** misorder/timeout/peer/ESP compilation abort; no physical proof. **Recovery:** host DENY/reset only; no bus state changed.

## R6-P44 — Full-session feasibility — COMPLETE / POSITIVE OFFLINE
**Hypothesis:** Full-session feasibility. **Baseline:** EXP355/386, partial EXP388, P41–43. **Exact controlled change:** compare historical V4.1 vs P37 source, 14 safety gates. **Relevant frames/fields:** first 0x0F FC23, 32 FC16 pages, runtime 085F/0708. **Positive/result:** 7/7 source checks; historical full recovery distinguished. **Negative/abort/unknown:** physical driver/DE/owner/slot/uncompleted-bootstrap recovery not proven; active NO-GO. **Recovery:** host DENY/reset only; no bus state changed.

## R6-P43 — Can incomplete bootstrap be recovered? — COMPLETE / POSITIVE OFFLINE (CAUSAL RECOVERY INCONCLUSIVE)
**Hypothesis:** Can incomplete bootstrap be recovered?. **Baseline:** P41/P42 plus EXP355/386. **Exact controlled change:** re-read existing captured episodes and historical logs; 11 evidence checks. **Relevant frames/fields:** first FC23 reply, 03E8 first page and ACK. **Positive/result:** 11/11; full historically local restart recovery exists. **Negative/abort/unknown:** no captured intentionally ACK-less first reply: causal recovery INCONCLUSIVE. **Recovery:** host DENY/reset only; no bus state changed.

## R6-P42 — Abort/pending-state conservative model — COMPLETE / POSITIVE OFFLINE
**Hypothesis:** Abort/pending-state conservative model. **Baseline:** P40/P41, historical EXP355/386. **Exact controlled change:** host-only policy for hypothetical first response and missing ACK. **Relevant frames/fields:** 03E8 initial FC16; later FC16 ACK, mailbox/write excluded. **Positive/result:** 10/10 tests; 529 event pairs and 102 synthetic retries; all DENY. **Negative/abort/unknown:** ESP rollback not controller abort, pending state unresolved. **Recovery:** host DENY/reset only; no bus state changed.

## R6-P41 — First-response aftermath in genuine references — COMPLETE / POSITIVE OFFLINE
**Hypothesis:** First-response aftermath in genuine references. **Baseline:** P40 and seven cross-model captures. **Exact controlled change:** read-only extraction of FC23 paired episodes through first 03E8 ACK. **Relevant frames/fields:** 0x0F FC23 then 03E8/count14. **Positive/result:** 7/7 paired windows proceed to 03E8 ACK; 2 Eco5 episodes ~108s with 102 focused first-page requests. **Negative/abort/unknown:** zero intentional response-only/no-ACK windows; controller timeout UNKNOWN. **Recovery:** host DENY/reset only; no bus state changed.

---
# 2026-10-11 — Newest reconciliation R6-P37–R6-P40

## R6-P40 — COMPLETE/POSITIVE (offline contract); ACTIVE NOT RUN
**Hypothesis:** a strictly one-shot synthetic first-response review context can be represented without granting actual native TX or follow-up privilege.
**Baseline:** R6-P39 decision, on-device R6-P37 RX-only, historical EXP355/386 and partial EXP388.
**Exact controlled change:** isolated Python contract model and tests; NO YAML, UART code, TX, controller restart or semantic write.
**Relevant fields:** historically documented slave 0x0F FC23 071C/count8 and 0730/count8; subsequent 03E8/count14 initial FC16 page export and 0708 mailbox remain excluded. No private reply payload or CRC is included in this Research entry.
**Result:** 7/7 test methods, exhaustive 2048 combinations of eleven synthetic guards, 500 repeat attempts. Maximal outcome REVIEW_ONLY_NO_TX; all physical actions return DENY. No raw on-bus replay or fresh controller event in P40.
**Positive criterion:** one bounded review, no output; met. **Negative/abort:** missing guard, stale deadline, second attempt, reset, fault, page ACK, mailbox or write DENY; passed offline. **Recovery:** none for offline test; future live abort must latch DENY, return DE LOW where possible, inspect heating/DHW and roll back to RX-only. ESP rollback may not terminate controller waiting state.

## R6-P39 — COMPLETE/POSITIVE (offline decision); ACTIVE NO-GO/NOT RUN
**Hypothesis:** old locally observed V4.1 coldstart recovery supports a bounded new design review, not direct P37 response activation.
**Baseline:** EXP355 COMPLETE/POSITIVE, EXP386 COMPLETE/POSITIVE, EXP388 RUNNING/PARTIAL (two successful restart subtests; two cancellation branches remain untested), P37 RX-only.
**Exact change:** source and log history analysis only.
**Result:** GO for offline review model; NO-GO to flash active V5 because P37 has no active TX adapter, contemporary epoch/owner unknown, missing physical reset/response-slot validation. First reply, page ACK, mailbox and semantics are independent authority scopes. No new payload or on-wire experiment.

## R6-P38 — COMPLETE/INCONCLUSIVE for assistant's independent build attempt
Assistant runtime lacked ESPHome/PlatformIO dependencies so independent full build NOT VERIFIED. User resolved missing r6p37_deny_only.hpp header and independently compiled/flashed P37; user compile success is not an assistant compile.

## R6-P37 — COMPLETE/POSITIVE live bounded RX-only regression
**Baseline:** known-good RX-only FIX4. **Controlled change:** P37 central DENY-only adapter substituted for two guarded physical TX paths; user installed on existing ESP, no wiring changes.
**Local result:** latest ~20:33:15–20:36:42 log: V5 valid=3510, FC16 573/573 known, geometry mismatch/resync/drop=0, B11C/B11D difference/fault=0, UART writes/TX attempts=0, DE reported LOW. No FC23/0708, 0/32 bootstrap, H021 NaN since source pages not received.
**Positive:** RX-only bus/bridge regression over observed intervals. **Unproven:** autonomous native session, physical controller epoch/owner, indefinite stability, physical fail-low through reset. No observed need to abort/recover.

**Historical EXP388 remains RUNNING/PARTIAL.** The P-series offline reviews do not close its remaining live branches. R6-P41 proposed offline/not run.

---
# 2026-10-11 — R6-P30 Stage A/B/C experiment records (newest first)

> New actual R6-P30 Stage B live result supersedes its earlier prepared-only state. Earlier PREPARED snapshots and all historical negative/inconclusive results below are intentionally preserved. Updating GitHub is NOT running a new device experiment.

## R6-P30 Stage C — COMPLETE / POSITIVE OFFLINE host handoff; live native-to-HA INCONCLUSIVE
**Hypothesis:** a same-run 32/32 XTR settings-page+matching-ACK record can be checked and handed to an independently guarded read-only H021 consumer without inferring controller-epoch/work owner or allowing TX. **Baseline:** Stage B actual XTR RX-only 01:59:17–02:01:14 and Stage A offline source/oracle (31 tests); historical controlled S11F/S10A 32/32 from a different context. **Exact controlled change:** host-only page/generation/ACK/boot/health/TTL gate, typed H021 catalog mapping and synthetic 32/32 fixture; no YAML, UART, HA registry or bus action. **Relevant:** 0x0F FC16 32 XTR settings pages and matching ACK geometry, H021 pages 03E8/14,042E/15,0442/13,0546/20; FC23 controller-start boundary, page state, ESP process boot, V5/B11C/D error deltas. **Observed:** 42/42 new Stage C tests plus 31/31 Stage A regressions (73/73); synthetic 32/32 and 22/22 decoded offline fields with signed and fractional scaling; live log 12/12 census snapshots 1/32 settings, 1/11 runtime and H021 0/22. **Positive:** offline integration and fail-closed conditions. **Negative/safety controls:** no unknown-owner, cross-model, stale/partial, changed ESP boot, parser-fault or unmatched-ACK fixture promoted to live HA value or active response. **Inconclusive:** any actual qualified 32/32 session currently, independent controller epoch, live H021 and real HA entity registry, semantic writes. **Abort:** any unexpected native TX or real HA publication under unknown epoch, source mismatch, parser fault, missing ACK, stale or invalid generation. **Recovery:** no device change this stage; for future implementation restore verified RX-only Stage B. **Stage D proposed only, not run.** No real ESPHome compilation claimed.

## R6-P30 Stage B — LIVE COMPLETE / POSITIVE bounded passive observer; NEGATIVE H021 pages within window
**Hypothesis:** exact additive all-XTR-page census can observe local FC16 publications without modifying R6-P24 output/safety and can refuse unobserved H021 data. **Baseline:** user-flashed R6-P24 passive start witness / Bridge15C, with no new native TX. **Exact controlled change:** 125 additive YAML lines/0 prior lines changed, two diagnostic HA text sensors, three census globals, 43 known page geometries; old four Bridge15C page trackers preserved. **Source:** actual user-supplied ESPHome API log Pasted text(20261011-000121).txt, 01:59:17.735–02:01:14.407. **Observed:** 12 census snapshots; 174/174 FC16 frames matched known geometry, 1/32 distinct cfg=04A6/13, 1/11 distinct runtime=085F/5, H021=0/4 pages and 0/22 aliases; no FC23 recorded in window. Physical TX=0, UART writes=0, delivered=0, DE LOW. At first visible sample V5 resync=4, Bridge02 integrity faults=1 and later unchanged; Bridge04 recovered after clean traffic. B11C/D new byte/count differences/drops/faults=0 in-window; B13 ABORT_NO_TX is correct defensive refusal. **Positive:** actual deployed RX-only census plus HA eligibility diagnostics and protected production. **Negative:** H021 reception/values did not occur in bounded window; not evidence that all XTR settings pages can never arrive. **Inconclusive:** epoch/owner, cold-start, long-run B11D integrity and full ESPHome compile provenance (client uses config-cache). **Abort:** unexpected TX/DE, new V5 resync/drops, B11C/D mismatch, unknown geometry, regressions. **Recovery:** known-good R6-P24 or Stage B RX-only image, no controller restart.

## R6-P30 Stage B preparation — PREPARED/NOT RUN at preparation time, later LIVE above
**Baseline:** R6-P24 2,800 YAML lines sha c08b8fa6afc437b59730e457703d50bf9c2957593a80c12a9e9ace60999df8bb; **controlled change:** additive census 125 lines, 2,925-line resulting candidate sha a2b68265650b14826fff104d7d559e1d1344b001f87cd0095adad88cf937d152. **Source checks:** parse PASS, 43/43 page geometries, 36/36 C++17 host lambda checks; full ESPHome compile not performed by assistant. **Prepared positive:** candidate diagnostics construct/guards. **Negative:** no ready positive H021 live values established. **Abort/recovery:** same TX/DE fail closed, restore known-good image. **Historical status:** PREPARED/NOT FLASHED then; explicitly superseded by actual user log.

## R6-P30 Stage A — COMPLETE / POSITIVE OFFLINE passive host reference; LIVE NOT RUN in this stage
**Hypothesis:** source-faithful read-only page/param observer can be composed with existing host-only XTR DCM pipeline/H023 without routing through a response output. **Baseline:** R6-P24 original YAML/Bridge15C, private host DCM core, H021 22 target metadata and earlier genuine captures. **Controlled change:** separate non-transmitting host shadow adapter and unit/oracle test code only. **Relevant:** XTR FC16 43 geometry profiles (32 cfg +11 runtime); H021 page starts 03E8,042E,0442,0546, exact register/scale catalog. **Observed:** 31/31 host tests, 43/43 geometry check, 22/22 read-only catalog metadata, 22,580 cross-model CRC-good ADUs, 2,321 with matching XTR geometry (**cross-model only**, not local proof). **Positive:** offline source matching, basic metadata and safety. **Negative:** cross-model geometry never eligible to publish local XTR values. **Inconclusive:** any actual live ESPHome HA data, epoch, owner. **Abort:** unexpected source provenance/geometry or presence of write/TX API; **recovery:** none offline.

---

# 2026-10-11 R6-P24 LIVE STATUS and R6-P25–P29 ledger reconciliation

> The older R6-P24 PREPARED/NOT RUN entry below is a valid historical PREPARED record, not the current post-flash status. No old results, including negative/inconclusive experiments, were deleted.

## R6-P29 — step 1 COMPLETE/POSITIVE offline audit; epoch INCONCLUSIVE; step 2 PREPARED/NOT RUN
**Hypothesis:** available S11F/G and S11W/X ESP-OTA records prove persistence of an identical pending controller work-item. **Baseline:** R6-P28 and earlier direct XTR forensic/epoch studies. **Exact change:** offline reconstruct old original-file provenance, three elapsed evidence gaps, full-session IDs, native page geometry and log signatures; no new YAML or live action. **Relevant:** 0x0F FC16 085F/5, 0884/60, 07D0/19, 07E4/17; FC03 0708/6; FC23, health and TX counters. **Positive:** 32/32 offline gap/provenance checks; historically S11W→X 07D0 geometry repeats, X original→FIX1 signature persists, manually qualified ACK07D0→07E4 proven in FIX1. **Negative:** same page geometry/signature is not a unique epoch or automatic TX authority; S11F 0884 not seen in post-OTA S11G slice. **Inconclusive:** OTA gap lacked independent recording and controller power marker. Log-to-log intervals 45m05.715s, 6m02.749s, 7m29.287s are not wire-silence durations; original complete XTR logs not freshly reopened. **Abort:** absent provenance or raw gaps -> UNKNOWN/CAPTURE_ONLY. **Recovery:** none offline. **Step 2:** proposed hardware RX-only sniffer capture PREPARED/NOT RUN, 16/16 offline software validations only, no sniffer hardware proven, no OTA/controller operation. Further duplication de-prioritized.

## R6-P28 — COMPLETE/POSITIVE offline firmware selector audit; NEGATIVE unique W4 owner
**Hypothesis:** CM930 source and preceding 0708 values reveal a uniquely observable next-work-owner field. **Baseline:** R6-P27; genuine seven-file capture corpus and recovered Connect 2.0.18/2.1.105. **Exact change:** offline firmware origin tracing, independent CRC/event pairing, W4=0 successor negative controls. **Relevant:** slave 0x0F FC03 0708/count6 W0–W5; FC16 07D0/085F/0884 and runtime families. **Positive:** 25,031/25,031 CRC-good frames, 392 polls / 367 paired replies, 62/62 host checks; W2/W3/W4 request-state origins documented. **Negative:** W4=0000 or W5 value cannot exclusively predict subsequent FC16/owner. **Inconclusive:** unknown controller internal scheduler and unique controller power epoch. **Abort:** CRC/source/window mismatch -> UNKNOWN. **Recovery:** n/a offline.

## R6-P27 — COMPLETE/POSITIVE offline predecessor audit; NEGATIVE universal 07D0 release
**Hypothesis:** same mailbox plus changed-085F ACK always exposes 07D0. **Baseline:** R6-P26 plus historically *executed* XTR S10C, S11F/G/H/I/W. **Exact change:** compare documented local precursor/response/successors without new TX; 54/54 host tests, using documentary fixtures not fresh full XTR CRC replay. **Relevant:** 0x0F FC03 0708/6, FC16 085F/5, 0884/60, 07D0/19. **Observed:** S10C exposes 07D0; S11H instead 0884. Historical executed S11I/S11W then ACKed the 0884 overlay and reached 07D0 in ~2.042s/~2.039s. **Positive:** additional 0884 continuation as demonstrated locally. **Negative:** universal 085F→07D0 endpoint. **Inconclusive:** identity of retained owner across ESP OTA. **Abort:** unsupported source/epoch -> UNKNOWN/NO_TX. **Recovery:** n/a offline.

## R6-P26 — COMPLETE/POSITIVE offline rejoin admissibility comparison
**Hypothesis:** unanswered 0708, answered retained local service, and bitmap hot-rejoin can be separated with actual answer/precursor evidence. **Baseline:** R6-P25, genuine DCM plus XTR S10B/C/S11H. **Exact change:** offline three-class source-separated matrix and fault injection; no YAML. **Relevant:** 0x0F FC03 0708 W0..W5 and FC16 085F/0884/07D0/settings family. **Positive:** 55/55 host checks, separate evidence for 16 unanswered polls, local mailbox-only S10B failure, mailbox+085F ACK S10C progress and genuine 31-page selective sync. **Negative:** simple polling/one reply/W4-only auto-owner rule. **Inconclusive:** autonomous XTR hot-rejoin. **Abort:** unmatched reply, unknown epoch or parser integrity -> UNKNOWN/NO_TX. **Recovery:** n/a.

## R6-P25 — COMPLETE/POSITIVE offline genuine hot-rejoin; NEGATIVE universal W4/W5 signature
**Hypothesis:** rejoin to an already trafficked controller has selective 0708 sync instead of requiring cold 32/32 bootstrap. **Baseline:** R6-P18–P23 and existing genuine mailbox/page mapping. **Exact change:** original six-file CRC reparse and match FC03 0708 replies to bitmap-selected FC16/ACKs plus negative-control genuine traces. **Relevant:** 0x0F FC03 0708/6 W2:W3=7FFF:FFFF W4=0080 W5=0007, 31 settings FC16 pages except 06F4. **Positive:** 22,344 valid ADUs; 327 polls, 302 paired responses; 16 unanswered then first answered mailbox; 31/31 selected pages with matching ACK, followed by regular mailbox; 40/40 host tests. **Negative:** W4=0080 or W5=0007 universally means a rejoin/owner; comparator shows W4=0080 without full sync. **Inconclusive:** physical reboot boundaries and applicability to local XTR. **Abort:** CRC, pairing or capture provenance conflicts. **Recovery:** n/a offline.

## R6-P24 — LIVE RUNNING/PARTIAL; passive RX-only baseline POSITIVE; controller start NOT EXERCISED
**Hypothesis:** passive callback gap ≥5s plus controller 0x02 A80E/A80F status witnesses restart-like pattern without TX or owner claim. **Baseline:** live Bridge15C and earlier local EXP355 controller restart (historical separate experiment). **Exact change:** user flashed the already prepared two extra HA diagnostics plus passive hooks; earlier prepared entry below remains historical. **Relevant:** CRC-good frames 0x02 FC23 A80C/count7 (A80E/A80F), 0x0F FC23/04BA/03E8, Bridge11C/D/V5 health. **Positive observed:** real user logs ~00:42:52–00:43:18 and ~00:46:32–00:50:27, NO_CALLBACK_GAP_SEEN/EPOCH_UNKNOWN/NO_TX, no ≥5s gaps or cold candidates, V5 valid 1997→3870 in later slice, no further resync, 11C/D stable, TX=0 DE LOW. One earlier resync=1 noted in initial slice and then recovered; prior long-run B11D fault remains open. **Negative:** neither positive nor missed cold-start test scored since restart absent. **Inconclusive:** genuine coldstart witness, unique controller epoch and ownership. **Abort:** unexpected TX/DE, new parser fault, loss of production HA. **Recovery:** ESP-only restore known-good Bridge15C RX-only; no Thermia reboot.

---

# 2026-10-11 R6-P24 PREPARED / NOT RUN / NOT FLASHED

**Hypothesis:** existing Bridge15C RX-only V5/Bridge03 pipeline can passively report a >=5s UART-callback-gap followed by CRC-good return and exact slave-0x02 A80E/A80F cold-start-like status without claiming a unique controller epoch or work owner. **Baseline:** Bridge15C live + historical locally executed EXP355 controller restart and EXP94/95 boot signatures; R6-P23 offline audit. **Exact controlled change:** two globals, 2 HA diagnostic text sensors, one raw-gap metadata hook and one CRC-validated frame witness; no existing code lines removed, no TX or ACK paths changed. **Relevant:** controller 0x02 FC23 A80C/count7 carrying A80E/A80F; native 0x0F FC23, 04BA/22, 03E8/14. **Positive future criterion:** healthy RX-only entities and, only if naturally observed, bounded callback-gap + clean first controller/outdoor frame + exact cold-status candidate; always EPOCH_ID_UNKNOWN/NO_TX. **Negative:** valid actual frame sequence missed or unqualified sequence promoted. **Abort:** UART TX/DE, parser resync/drop, B11C/B11D fault, device or HA regressions. **Recovery if later flashed:** restore known-good Bridge15C ESP firmware, do not reboot controller. Offline YAML/static PASS, 125 additions/0 deletions, extracted C++17 actual lambdas 37/37 host checks; **full ESPHome compile NOT RUN, no flash, no user device log.** Source sha256 c08b8fa6afc437b59730e457703d50bf9c2957593a80c12a9e9ace60999df8bb. Report archived in private firmware repo. Status stays PREPARED until actual result supplied.

---

# 2026-10-11 LATEST — R6-P18–P23 (offline-only results); Bridge15C live partial

## R6-P23 — COMPLETE/POSITIVE historical controller-restart audit; NEGATIVE standalone epoch shortcut; INCONCLUSIVE owner
**Baseline:** R6-P22, XTR EXP355/EXP94/95/123, S11F/W/X, R5 FIX2, current Bridge15C. **Hypothesis:** independent controller-restart evidence exists in local XTR history. **Controlled change:** offline-only record/epoch provenance classification; no live action. **Observed:** EXP355 controller was physically restarted while ESP stayed powered, bus silence exceeded 5s, returned with A80E/A80F=0000/0005 and completed fresh 32/32 bootstrap plus runtime. Original raw EXP355 log not newly parsed. 28/28 host checks. **Positive:** documented controlled restart event. **Negative:** BUS_GAP, A80F=5, ESP boot and FC23 alone do not prove UNIQUE controller-epoch/work owner. **Inconclusive:** universal epoch-ID and arbitrary hot rejoin. **Abort:** absent physical restart/source/health; **recovery:** none offline; current RX-only.

## R6-P22 — COMPLETE/POSITIVE seven pre-first-reply starts; NEGATIVE page/FC23 owner candidates
**Baseline:** R6-P21, genuine Eco5 Sep26/Sep28. **Hypothesis:** controller-only request/payload before any gateway response uniquely distinguishes a native owner. **Controlled change:** passive CRC replay restricted to pre-first-reply events, including gateway-absent control. **Observed:** 19,893 CRC-good original ADUs, first 04BA image and 085F zeros same in seven starts, 192 first 0x0F request geometries shared in Sep26 present/absent comparison, FC23 request bytes vary within a startup. 30/30 tests. **Negative:** no unique owner found in tested patterns. **Inconclusive:** unknown controller fields elsewhere. **Abort:** bad CRC/provenance/segment; **recovery:** offline n/a.

## R6-P21 — COMPLETE/POSITIVE prefix replay; NEGATIVE zero-085F discriminator
**Baseline:** R6-P19/P20 genuine six complete starts. **Controlled change:** strictly prior-to-07D0 event prefixes. **Observed:** three early service ACK routes recognised at 06F4 ACK (~77–78ms before 07D0) and three late routes after genuinely answered 0708 (~585–625ms before 07D0). Pre-response zero-valued 085F repeats in both. 28/28 checks. Same training/evaluation set; not independently predictive. **Abort:** missing ACK or interval => UNKNOWN. **Recovery:** offline n/a. No TX.

## R6-P20 — COMPLETE/POSITIVE observer; NEGATIVE automatic reply authority
**Baseline:** R6-P19 CRC events. **Controlled change:** metadata-only ACK and mailbox event matcher, independently of P19 labels. **Observed:** nine genuine segments 3 early/3 late/3 UNKNOWN; ten documentary local cases 2 late/8 UNKNOWN; 65/65 host checks. Route only assigned after observing 07D0, so never permit earlier ACK. **Abort:** bad geometry, integrity or sample boundary. **Recovery:** offline n/a.

## R6-P19 — COMPLETE/POSITIVE distinct startup paths; NEGATIVE universal linear handshake
**Baseline:** R6-P18 + local EXP270/271, S11F/W/X/R5. **Controlled change:** original genuine frame/CRC reparse, exact ACK and FC03 0708 pairing. **Observed:** 3 early 085F ACK before FC23, fast 06F4→07D0; 3 late 085F ACK after 06F4 with answered 0708→07D0; genuine ACK07D0→07E4 ~2.130–2.256s. 28/28 host tests. **Inconclusive:** causal response rule and owner. **Abort:** incomplete/ambiguous frame; **recovery:** n/a.

## R6-P18 — COMPLETE/POSITIVE relative ordering; NEGATIVE universal immediate path
**Baseline:** R6-P16/17. **Controlled change:** CRC recomputation and time order of FC23, FC16 085F/06F4/03E8 and 07D0 in Sep26/28 genuine starts. **Observed:** all six response-bearing starts had both ACK085F and ACK06F4 before first 07D0; three 085F before FC23, three after 06F4. 19,893/19,893 CRC-good. No semantic acceptance conclusion. **Abort:** source/CRC mismatch; **recovery:** offline n/a.

## Bridge15C — RUNNING/PARTIAL live
**Baseline:** Bridge13B/13C production RX-only. **Controlled change:** four text sensors, five metadata arrays, observer after existing V5 validation, no TX. **Observed:** ~7m38s at 23:25–23:33 Oct10; four parameter pages not seen (rx=0) even during active heating; 04A6/13 and 085F/5 received; latest V5=3943, no parser/portable differences or physical TX, DE LOW. **Positive:** absent-page and no-TX path; **not run:** page-positive freshness/invalidations. **Abort:** TX/DE or production/parser regression; **recovery:** prior RX-only Bridge13B image; no controller restart.

---

# 2026-10-10 NEWEST — R6-P17 / P16 / P15 / P14 results (append-only history below)

## R6-P17 — COMPLETE / POSITIVE cross-model sequence; COMPLETE / NEGATIVE universal instant handshake; COMPLETE / INCONCLUSIVE semantic acceptance
Hypothesis: 0x0F FC23 reply immediately/uniquely unlocks settings ACK and first runtime FC16 0x07D0. Baseline R6-P16 7 documented restart boundaries, 6 reply-bearing phases and one without gateway; R6-P11–P13 cadence. Controlled change OFFLINE ONLY: CRC revalidation on two genuine Eco5 logs, split at >5s all-address gaps, match 0x0F FC16 ACK on slave/start/count within 0–1s, compare FC23/03E8/085F/06F4/07D0 chronology. Relevant 0x0F FC23 (cross-model read 0730×8, write 071C×8, NOT XTR write authorization), FC16 03E8, 085F, 06F4, 07D0. 19,893/19,893 frames CRC-valid, 16/16 offline checks. Six reply-bearing restart phases: 03E8 FC16 ACK seen later (two >108s delayed); 085F geometry ACK precedes first 07D0 in 6/6 but falls before FC23 in 3 and after in 3. One gateway-absent restart segment: 41 FC23 requests, no reply, 82 085F requests, 0 FC16 0x0F ACK, 0 03E8, 0 07D0. Positive reproducible partial ordering; negative mandatory instant/strict order; inconclusive separate effects of physical gateway presence and FC23 answer/semantic stage, actual epoch and local XTR acceptance. Abort source/CRC mismatches or confidential handshake contents, recovery n/a (offline only).

## R6-P16 — COMPLETE / POSITIVE provenance and segmentation; COMPLETE / INCONCLUSIVE byte-perfect completeness/semantics
Hypothesis: FC23 five >5.1s pauses are logger loss vs actual phase stop. Baseline R6-P14/P15. Controlled change: resegment genuine 26/28 Sep Eco5 logs at all-address gaps >5s, verify with original collaborator documentation A/B/A gateway on/off/on and four gateway-present power cycles, inspect passive sniffer CRC-only software timestamps. 3+4 restart boundaries; 5/5 exceptional FC23 intervals span restart boundary; 156/156 intra-segment gaps 3.8–4.7s. Six startup phases with recorded FC23 responses had no further requests later within that phase; one without gateway had 41 FC23 unanswered requests. First FC23 after resumed bus ~0.981–1.210s. Positive evidence that five long intervals are cross-power-cycle censored; negative as evidence of proven uninterrupted-session timeout; inconclusive physical bus byte completeness/semantic success. Recovery n/a. R6-P14/P15 observations remain, prior causal interpretation superseded.

## R6-P15 — COMPLETE / POSITIVE gap comparisons; INCONCLUSIVE underlying mechanism; interpretation SUPERSEDED by R6-P16
Hypothesis: five long FC23 windows indicate runtime phase switches. Baseline R6-P14. Controlled change: offline 12s before/after first and last FC23 in each gap, all-address logging continuity and next repeat. Found all-address gaps 15.56–36.28s, other 0x0F traffic during windows, resumed 4.57–4.60s first request spacing. Positive capture gap identification; later original capture provenance revealed deliberate controller power cycles at these holes. No TX/hardware. Recovery n/a.

## R6-P14 — COMPLETE / POSITIVE observed cross-boundary gaps; heartbeat interpretation SUPERSEDED by R6-P16
Hypothesis: FC23 mandatory uninterrupted heartbeat would not have five >5.1s pauses while other 0x0F traffic appears. Baseline R6-P13. Controlled change: offline seven historical cross-model captures, FC23 interval threshold >5.1s, compare FC16 runtime. Five gaps 91.422s, 39.684s, 125.299s, 287.714s, 231.464s; some runtime FC16 inside. Positive discovery of timing gaps; negative/inconclusive as proof of in-session stopping after R6-P16 showed each gap crossed deliberate restart. No TX/physical changes, recovery n/a.

---

# 2026-10-10 — Newest R6-P13 / R6-P12 / R6-P11 / R6-P10 FIX1 entries
## R6-P13 — COMPLETE / POSITIVE offline; COMPLETE / NEGATIVE mandatory triplet; COMPLETE / INCONCLUSIVE semantics
Hypothesis: 085F->FC23->04A6 is a fixed causally linked handshake rather than independent periodic tasks. Baseline R6-P11 seven genuine cross-model captures, R6-P12 164 FC23 requests and 7 recorded replies. Controlled change: metadata-only timestamp cadence, nearest phase and within-capture control 085F->next 04A6 without demanding FC23. No bus/YAML/firmware action. FC23 median recurrence Sep26/Sep28 4.2335/4.241s; 085F 2.1245/2.131s, 04A6 1.383/1.411s. 96/99 and 58/64 FC23 have an 085F before plus 04A6 after within 10s. Median phase 085F->FC23 1.328/1.350s, FC23->04A6 0.141/0.141s. Matched control 085F->next 04A6 median 1.451/1.4555s versus FC23-containing overall 1.473/1.4915s. Positive recurrent phase structure; negative fixed one-to-one/semantic-acceptance claim; inconclusive controller scheduler, owner/epoch or local XTR FC23. Abort invalid source/secret disclosure/semantic write inference; offline recovery n/a.
## R6-P12 — COMPLETE / POSITIVE offline; COMPLETE / NEGATIVE one-shot claim; COMPLETE / INCONCLUSIVE acceptance
Hypothesis FC23 single bootstrap before runtime. Baseline R6-P11. Controlled change only offline CRC/structural classification/FC16 adjacency. 164 0x0F FC23 requests (99/64/1) and seven recorded immediate 21-byte responses (2/4/1), gaps 29–63ms; fixed request geometry read 0x0730 count8/write 0x071C count8. 157 requests unpaired in captures, cannot infer response absence on wire or failure. Period ~4.2s in two long captures. Most immediately preceded by 085F, followed by 04A6 in ~0.141s, correlational. No live TX. Abort if source invalid or confidential material risk.
## R6-P11 — COMPLETE / POSITIVE offline order variability; COMPLETE / INCONCLUSIVE true device boot/owner
Baseline R6-P4 raw 25,031 CRC-valid cross-model frames and archived CM930 source. Controlled change relative chronology across seven files. Visible runtime and configuration order differs by capture, sometimes 07E4 precedes 07D0. No universal captured start sequence or power epoch. No hardware changes.
## R6-P10 FIX1 LIVE — RUNNING / PARTIAL
User-supplied logs 19:16–19:28: text sensor R6 P10 First Fault Snapshot present with NONE, raw B11D independent >6000 frames and fault=0, V5 and B11C healthy, one early V5 resync recovered without later delta, drops=0, TX/DE=0, UNQUALIFIED. First-fault latching not exercised. Positive entity presence, partial health; inconclusive latch. Abort new physical TX/DE, parser or production regression; restore verified RX-only firmware, no controller reboot.
---
2026-10-10 newest R6 experiments:

R6-P10 FIX1 PREPARED / NOT RUN — hypothesis: first fault diagnostic lost when logger disconnects; baseline R6-P10 live sticky failure + offline audit. Controlled change: one string global, one diagnostic HA text sensor, one assignment in existing first_fault from already computed pending/age/remainder/header byte2/candidate range/idle/batch. Positive: subsequent first B11D scheduler fault keeps HA snapshot and RX-only V5 health. Negative: scheduler first-fault without snapshot, or regression. Inconclusive: no fault. Abort any TX/DE, V5 errors or lost production entities; recover prior known-good RX-only firmware. YAML parse/unique IDs and diff passed; not compiled or flashed. Other FIFO/TX fault branches excluded.

R6-P10 OFFLINE AUDIT COMPLETE / POSITIVE for diagnosing missing persistence, inconclusive root cause. The first_fault lambda logged pending/length metadata ONCE, retained in HA only short fault reason. Post-fault sample cannot recover the event; last-callback V5.has_pending snapshot overwritten continuously; residual byte2 not necessarily a bytecount.

R6-P10 LIVE COMPLETE / POSITIVE recurrence; COMPLETE / NEGATIVE B11D continuity; COMPLETE / INCONCLUSIVE fault root cause. First log 18:25–18:26 healthy. Second 18:57–19:01 starts after fault: B11D first RAW_NO_VALID_CRC_CANDIDATE_AT_IDLE, frames=4269, batches=1746 frozen, incomplete=1; UART/V5/B11C advance; V5 >16000 valid, resync/drops zero; TX=0 DE=LOW. No onset FIRST_FAULT_DIAG in supplied logs. No native owner/epoch proof.

R6-P9 COMPLETE / POSITIVE offline 13/13 source-rule tests: 7 bytes and unique 180-byte candidate match FC23-shaped header under source candidate_lengths, not proven actual FC23. R6-P8 COMPLETE / POSITIVE offline 12/12 split-frame simulation of 25ms idle sticky framing; not local cause proof. R6-P7 COMPLETE / POSITIVE offline 12/12 first-fault metadata arithmetic 32-25=7, V5 complete 8+17=25; actual residual bytes unknown.

---

# 2026-10-10 — R6-P1 to R6-P6 FIX1 (newest first)

## R6-P6 FIX1 — PREPARED / NOT RUN
Hypothesis: after a latched safety fault FC23 must not erase original fault reason, and expired runtime candidate reason must say STALE. Baseline R6-P5 safe RX-only and P6 audit. Controlled change: only two diagnostic classifier fixes; production V5/Bridge11C/B11D, Home Assistant entities and TX lock unchanged. Offline YAML parse and 8/8 Python tests reported PASS. No compile/flash/live result supplied. Positive: safe live RX-only, diagnostics consistent if edges occur. Negative: replicated overwrite/stale mismatch. Abort: TX/DE-high, V5 errors, loss of production entities. Recovery: rollback known-good R6-P5, no controller reboot. No bus response authorized.

## R6-P6 — COMPLETE / POSITIVE offline audit; COMPLETE / INCONCLUSIVE live runtime branch
Baseline R6-P5. Controlled change: offline source examination and simulated scenario replay only, no physical action. 15/15 Python behavior tests and 25,031 genuine cross-model ADUs replayed; zero TX. Found FC23 could overwrite latched reason without unlocking, stale status and reason could conflict, V5 CRC validation is trusted rather than repeated in classifier, B11D independent health separate. No compiled-C++ replay or local live runtime 07D0/07E4 branch proven. Abort on unintended authority grant; no hardware recovery.

## R6-P5 — COMPLETE / POSITIVE bounded local RX-only integration; COMPLETE / INCONCLUSIVE runtime classification
Baseline R6-P1 known-good production V5. Controlled change: passive V5-fed runtime classifier with three HA text sensors; no TX. Local log 16:31:00–16:34:03 (~3 min, 3,758 lines): V5 valid=1626, known FC16=266, geometry/unknown/resync/drops=0; B11D raw=1621, faults=0; B11C diffs=0; UART writes/TX/DE=0/0/LOW. Class=UNQUALIFIED/NO_TX, reason ESP_BOOT_UNQUALIFIED, node NONE; 085F/5 and 04A6/13 present, no qualified runtime/FC23/0708/ACK. Positive safe production RX; inconclusive transition logic. Abort and rollback R6-P1 if V5/HA regression or TX.

## R6-P4 — COMPLETE / POSITIVE cross-model raw replay; COMPLETE / INCONCLUSIVE local XTR
Seven genuine Eco5/ATEC reference captures, 25,031 CRC-valid ADUs, 2,500 slave 0F FC16, 794 recognized runtime geometries all denied as local XTR authority. Hypothetical source-bypass test 749 first/45 repeated but no TX. Offline only.

## R6-P3 — COMPLETE / POSITIVE reconstructed offline scenarios; COMPLETE / INCONCLUSIVE actual source replay
10/10 Python classifier scenarios reconstructed from historical findings; states UNQUALIFIED, RUNTIME_NODE_SEEN, RETAINED_CANDIDATE; TX always DENY. No raw historical local S11 replay at this stage.

## R6-P2 — COMPLETE / POSITIVE historical comparisons; COMPLETE / INCONCLUSIVE owner inference
S11W→S11X, EXP313→EXP315 establish historical retained 07D0/07E4 after ESP OTA and occasional post-07D0 0708, not a mandatory universal bootstrap nor independent physical epoch proof. No action.

## R6-P1 — COMPLETE / POSITIVE first-fault metadata; COMPLETE / NEGATIVE long-run independent raw framing
Baseline R6-P0 B11D fault after ~26min without capture metadata. Controlled change RX-only FIRST_FAULT_META, no TX. Supplied local log 15:56:09–16:28:43; FIRST_FAULT at 16:26:44.824 RAW_NO_VALID_CRC_CANDIDATE_AT_IDLE, batch 6406, raw 32, cursor25, 7 remain, expected2, candidate length180, one needs-more, zero CRC-valid remainder; B11D frame count later frozen ~15688, V5/B11C advanced, TX/DE zero. Cause unknown. Abort V5 regressions or unexpected TX; leave RX-only, rollback previous firmware if needed.

---

# 2026-10-10 — LIVE-B11D-RX-VALIDATION-01 and offline observer reconciliation (newest first)

## LIVE-B11D-RX-VALIDATION-01 — RUNNING / PARTIAL (user-provided passive log)

**Baseline:** previous local Bridge11D-A FIX1 bounded 7,159/7,159 independent raw-versus-V5 matching frames with no fault in that window; legacy V5 and V5-delimited Bridge11C remained functional. **Hypothesis:** independent raw framer continues matching V5 for ~20–30 minutes with no CRC/geometry error and no TX.
**Controlled change:** NONE. User supplied only a log from existing running XTR ESPHome configuration; no new YAML, active responder, OTA, controller reset, physical UART TX, or wiring change. Source: [LIVE_B11D_RX_VALIDATION_20261010.md](LIVE_B11D_RX_VALIDATION_20261010.md), time 15:04:31.683–15:08:43.810 (~4m12s).

**RESULT / observed:** V5 valid 151,615→153,659 (+2,044), V5 drops/resync/geometry errors 0; B11C original portable with V5-delimited frames 151,818→153,604 (+1,786), zero frame differences/faults. B11D independent rawFrames=portableFrames=comparedV5 froze at 56,714. Its callbacks +5,377 and bytes +38,429 continued while batches froze at 23,178. A sticky fault=1, incomplete=1 with first-fault reason **RAW_NO_VALID_CRC_CANDIDATE_AT_IDLE** existed before the sample started. B11D countDiff=byteDiff=0 are **stale after the fault**. TX attempts / DE = 0, owner and controller power epoch UNKNOWN.

**Positive:** safe capture-only behaviour, continued V5/V5-delimited C++ RX, zero TX within supplied capture.
**Negative:** independent raw frame continuity NOT MET. **Inconclusive:** physical root cause of first CRC idle fault, controller epoch and owner. **Duration criterion NOT MET:** requested 20–30m is NOT contained in this log. Do not promote current live test to fully complete.
**Abort:** any new V5 resync/drop, unauthorized TX/DE, ESP loop regression or loss of HA production functionality; refrain from active bus responses.
**Recovery / next:** request first actual fault transition and 20–30s of preceding log; if absent, a **separately reviewed RX-only ESP-only startup capture** (PREPARED / NOT RUN), without Thermia controller power reset, and without automatically clearing sticky faults. No next live experiment executed based on this log.

## OFFLINE-BRIDGE09 — COMPLETE / POSITIVE (host synthetic UART-callback replay only)

**Hypothesis / baseline:** Bridge08 had matched all 25,031 genuine raw cross-model ADUs through unchanged original C++ and observer using known pre-delimited frames; determine whether reconstructed callbacks/coalescing also preserve frames and fail closed.
**Controlled change:** host simulated callback segmentation (1 ADU per callback; 2 ADUs split into 3-byte callbacks; 8 ADUs split into 1-byte callbacks) and synthetic 25ms idle boundary; no live ESP action.
**RESULT:** per compiler build 25,031 genuine cross-model ADUs × 3 = 75,093 original portable C++ frame-occurrences, 4,809 native events per pattern. GCC/Clang/ASan+UBSan PASS, frame differences 0, physical output attempt count 0; CRC/noise/truncated/mid-frame idle/overflow/tick rollover tests fail closed. [Private CI 38053859261](https://github.com/ryckema/Thermia_Connect_Firmware/actions/runs/38053859261).
**Positive:** host callback reassembly and C++ integration under tested artificial segmentation. **Negative/inconclusive:** does **NOT** validate real ESP32 callback latency or Modbus RTU electrical t3.5; the later live B11D sticky fault is not contradicted.
**Abort/recovery:** any frame mismatch or TX fails CI; restart offline test only. Controller epoch / owner UNKNOWN.

## OFFLINE-NATIVE-BRIDGE-08 — COMPLETE / POSITIVE (genuine original-source HOST replay only)

**Hypothesis / baseline:** Bridge07 original C++ had processed 4,809 synthetic CRC-valid ADUs projected from genuine event metadata. Can all 25,031 genuine cross-model ADUs be run through unchanged original portable C++ and observer?
**Controlled change:** replace synthetic ADUs with seven genuine source captures, no ESPHome or heat-pump change.
**RESULT:** 25,031/25,031 original raw ADUs and 4,809/4,809 native events matched; FC03 374, FC16 1,324, FC23 7 temporal/geometric correlations; all original sources unchanged; GCC, Clang and ASan/UBSan PASS; host TX=0. [Private CI 38051370371](https://github.com/ryckema/Thermia_Connect_Firmware/actions/runs/38051370371).
**Positive:** original C++ and observer exact bounded host replay. **Negative/inconclusive:** no physical native session owner, XTR-specific semantics, true bus-silence timing or live ESP32 validation.
**Abort/recovery:** CRC mismatch, event drift, unintended TX or sanitizer fault abort host run. Temporary sensitive raw fixtures removed from private branch current HEAD; private Git history may retain them.

## OFFLINE-NATIVE-BRIDGE-07 / OFFLINE-NATIVE-OBSERVER-06 — COMPLETE / POSITIVE (bounded host test)

Metadata-only observer 06 processed 4,809 native cross-model events without TX capabilities. Bridge07 linked unchanged original portable C++ for 4,809 synthetic CRC-valid frames derived from genuine event geometry/timestamps, confirmed 4,809/4,809 event parity, observer error atomicity and owner UNKNOWN, no TX; genuine raw corpus original-source link was NOT RUN until subsequent Bridge08. Earlier historical results are retained below without retroactively rewriting what was run.

---

# 2026-10-10 — Three offline-only native-session studies (NO controller experiment; newest first)

**Historical evidence reconciliation (2026-10-10):** de genuine cross-model RTC-cluster `0858–085E` was **al gedocumenteerd op 2026-10-05** in `Thermia_Connect_Firmware/findings/CM930_UNMAPPED_PATTERN_CLASSIFICATION.md`. De nieuwe bijdrage van OFFLINE-EPOCH-WITNESS-02 is de onafhankelijke woord-/tijdcontrole tegen de firmware-klok `06EA–06F0` plus de classificatie als **ongeschikt zelfstandig controller-epoch-bewijs**. De bestaande firmwarefinding blijft prioritaire eerdere ontdekking; lokaal XTR-bewijs ontbreekt.

## OFFLINE-EPOCH-WITNESS-02 — COMPLETE / POSITIVE (reference audit and RTC mirror); COMPLETE / INCONCLUSIVE (XTR controller epoch)

**Hypothesis:** existing complete controller-origin FC16 pages and Thermia Connect semantic profiles may contain an independently usable controller boot/uptime/session-generation witness. **Baseline:** earlier NATIVE-SESSION-EPOCH-CONTINUITY audit, S11F/G/H/W/X and R5 FIX2 canonically recorded evidence, genuine Online/DCM reference captures and Connect firmware profile definitions. **Controlled change:** offline parsing of complete existing slave 0x0F FC16 frames and 16-bit register time series; no YAML edit, OTA, controller reboot, UART TX/DE or live action.

**Evidence:** 2,500 complete CRC-valid FC16 requests from seven genuine **cross-model** reference files. A second calendar-clock tuple appeared at 0858–085E in reference 0848/count23; independent time correlation was found with firmware-labelled date/time at 06EA–06F0. Example reference comparisons: a 332 s displayed-clock increment over 332.199 s capture time, and a 344 s increment over 343.914 s. The new mirror address mapping is **reference-observed, not firmware-labelled for those same addresses, and not verified locally on XTR M**. The apparent monotone 0859 candidate was the minute-of-hour clock word. Other screened register words represented or plausibly followed operational temperature/status/defrost behaviour. No unique controller epoch ID was identified.

**Positive criterion:** independently controller-sourced boot/generation marker with known semantics and local XTR pre/post-controller-reset evidence — **NOT MET**. Secondary positive goal, eliminating false monotone witnesses and reproducing the reference RTC correlation — **MET**. **Negative/inconclusive:** no counter/reset marker from this available dataset; existence elsewhere NOT DISPROVEN. **Abort/safety/recovery:** missing complete CRC/geometry, ambiguous model identity, or no independent controller reset evidence prevents owner inference; remain CAPTURE_ONLY with ACK/DENY and no TX. Offline analysis requires no recovery.

**Next:** offline search existing local XTR 0848/count23 W16–W22 and 06EA/count7; any RX-only logger is a **separate future PREPARED / NOT RUN** action requiring review. R6 unchanged.

## OFFLINE-CONDITION-REJOIN-01 / NATIVE-SESSION-EPOCH-CONTINUITY — COMPLETE / POSITIVE (boundary classification); COMPLETE / INCONCLUSIVE (power epoch)

**Hypothesis:** prior fresh/rejoin experiments might share a provable controller-owned continuity token across ESP OTA. **Baseline:** NATIVE-SESSION-MVP timestamp study. **Controlled change:** offline comparison of existing restart timestamps, controller page geometries, payload signatures, FC23 occurrence, recorded physical TX counts and missing power markers. No new live experiment.

**Observed:** S11F fresh handshake/bootstrap from a controlled experiment contrasted with S11G's later 085F + service polling and no retained 0884 in its visible segment. S11H's bounded service step led to 0884 but not target 07D0 within its timeout (the historical negative outcome is preserved). S11W repeated 07D0/19 with signature 8721F668; after an ESP firmware change, S11X original repeated the **same address/count but different signature D7EC8823**. That latter signature remained stable through the next ESP change in S11X FIX1, after which one manually qualified response preceded 07E4. The intervals between runs were not continuous and no independent controller power marker was present.

**Positive criterion:** invariant payload or independent controller generation witness straddling known ESP-only reboot — partially useful repeated payload in the S11X original→FIX1 pair, **not a proven power-epoch ID**. **Negative/inconclusive:** payload match alone, lack of FC23, or no change in local logging does not prove an unchanged controller epoch. **Abort/recovery:** uncertain epoch/owner => capture-only; none needed offline.

## NATIVE-SESSION-MVP timestamp/firmware reconciliation — COMPLETE / POSITIVE (chronology); COMPLETE / INCONCLUSIVE (unattended ACK eligibility)

**Hypothesis:** chronology of existing locally controlled fresh and retained branches plus Connect firmware semantics can identify the first missing authorization requirement. **Baseline:** S11F, S11W, S11X original and FIX1 original local logs; R5 FIX2 from canonical summary where original R5 log could not be directly reopened. **Controlled change:** offline event/time alignment and firmware cross-check only.

**Observed:** S11F bootstrap 32/32 and its subsequent runtime progression included an additional service response between the bounded 0870 ACK and subsequent 0884, so ACK-alone causality is **unresolved**. S11W service-path ACK0884 preceded 07D0 by ~2.039 s; S11X FIX1's one qualified retained ACK07D0 preceded 07E4 by ~2.041 s. R5 FIX2 reached 0870 ~2.089 s after ACK085F without a fresh observed 0864; controller epoch stayed UNKNOWN and the third R5 phase was NOT RUN. These are **context-specific** sequences, not a global deterministic scheduler or a proven owner-claim policy.

**Positive criterion:** timestamp cross-check and evidence classes — MET. **Negative/inconclusive:** no same-controller-power-epoch evidence across all compared captures and no isolated ACK-alone sufficiency. **Abort/recovery:** no physical action in study; auto-TX DENY until a separately proven owner/epoch gate exists.

**Source provenance:** original supplied local ESPHome logs for S11F/W/X; canonical experiment history for R5; genuine cross-model DCM captures; firmware-derived Connect 2.0.18/2.1.105 semantics. Full private source-linked reports, ledger and register audit CSVs under `Thermia_Connect_Firmware/findings/` with the 20261010 filenames. **No existing experiment history has been superseded or deleted by this research entry.**

---

# 2026-10-09 — CM930 2.0.18/2.1.105 source and native-session gap audit (OFFLINE, no controller experiment)

**Study ID:** NATIVE-SESSION-SOURCE-AUDIT-20261009. **Status: COMPLETE / POSITIVE for offline comparison only; COMPLETE / INCONCLUSIVE for DCM03 internal selector lifecycle and XTR auto-ACK authorization.** No ESPHome run, physical TX, new YAML, semantic write or controller action took place. This is not a replacement for or progression of R5 FIX2; R6 remains CONCEPT / NOT PREPARED / NOT RUN.

**Hypothesis:** the historical ATEC W4=077F mailbox image may be explained by an older Connect 2.0.18 selector implementation that does not clear received-page request bits, or by a periodic native read-all producer.

**Baseline / provenance:** genuine ATEC DCM03 capture showed 65 answered FC03 0708/count6 mailbox snapshots: first W4=07FF, remaining 64 W4=077F; controller FC16 pages repeatedly published in the meantime. Earlier firmware audit confirmed Connect 2.1.105 reset_register_read_request and request_read_all_registers. Newly provided original Connect 2.0.18 appfs source files (client.py, modbus_server15.py, full device_client package), plus available recovered Connect 2.1.105 sources; firmware source comparisons in Thermia_Connect_Firmware repository.

**Controlled change:** offline source-only comparison of exactly five CM930 handlers (on_registers_request_event, _request_operation_data, on_handshake_state_changed_event, _on_successfull_onboarding, on_registers_received_event), selector helpers, and event producers/timers in main.py/events.py/event loop. No changes to ESP config, HA or bus.

**Relevant source and on-wire fields:** CM930 0708/6 mailbox W2=070A, W3=070B, W4=070C; FC16 runtime groups 085F/5, 0864, 0870, 0884; W4 06FF read-all default excluding bit8 and special targeted requests. Source functions request_read_all_registers, set_register_read_request, reset_register_read_request, modbus_request_registers_event, _request_info_data, _request_operation_data.

**Observed offline results:** all five compared CM930 handler bodies functionally match across 2.0.18 and 2.1.105 (four textually identical, fifth formatting-only as previously reported). Both versions clear the corresponding selector on consumed FC16. 2.1.105 additionally informs CMClientParameterUpdateState, an application-level readiness tracker absent in 2.0.18. Both device_client code trees' identified internal request producers pass targeted register sets, not a None full read-all payload; no periodic read-all producer was identified in those searched files. Runtime publication timers and hourly parameter-map checks must not be misclassified as a Modbus W4 re-arm scheduler.

**Positive criterion:** original older source confirms self-clearing logic and identifies concrete request/event mechanisms — MET. **Negative criterion for hypothesis:** 2.0.18 lacks reset-register-bit behavior — FALSIFIED by source. **Inconclusive:** genuine legacy DCM03 source unavailable; no internal DCM03 event trace proving why W4 remains 077F; this alternative remains OPEN. Absence of an identified timer in these code trees is not proof that no other service or older DCM03 periodically rearms requests.

**Abort/recovery:** offline only; conflicting source versions or incomplete provenance stop promotion to protocol fact; no bus recovery needed. **Comparison to previous:** agrees with genuine ATEC raw frames but disproves the specific older-Connect-no-bitclear explanation. An ACK remains a transport/scheduler observation, never proof of semantic write acceptance or authorization.

**Next study proposed, NOT RUN:** NATIVE-SESSION-MVP offline transition/owner matrix using existing S11F/S11W/S11X/R5 raw sources and genuine Online/DCM captures to identify first blocker to safe unattended runtime; explicit controller epoch, predecessor evidence, exact geometry, integrity/TX guards and CAPTURE-ONLY handling. Do not invent a new live experiment or change R6 status.

---
# 2026-10-09 — V5-S8-R5 FIX2 — closed local capture experiment (separate from S11Y series)

**Number:** V5-S8-R5 FIX2. **Status:** **COMPLETE / POSITIVE** for full passive 0870/17 payload logging; **COMPLETE / INCONCLUSIVE** for the original three-stage 0864 gate; P3 **NOT RUN**. User supplied `Pasted text(20261009-095219).txt`, boot `D7726116`. This branch must not be conflated with latest S11Y-AL FIX1.

**Hypothesis:** keeping the R5 manual phase behavior intact while fixing the 0870 printf argument count permits capture of all 17 received words without changing bus transmissions. **Baseline:** previous R5 reached 0870 but omitted raw words; R5 FIX1 introduced W00–W16 logger but had a compiler warning (nine format placeholders for eight W09–W16 arguments), not safe to flash unchanged. **Controlled change in FIX2:** correct the second passive logging format string only; preserve three manual phase controls and known-good production entities.

**Observed timeline:** 11:50:59.405 P1 ARM accepted, 11:50:59.628 exactly one P1 delivery; 11:51:05.420 P2 ARM accepted; 11:51:06.663 exactly one FC16 ACK 085F/5; 11:51:08.752 first 0870/17 (**2.089 s after P2**). 24 RX0870_A/B pairs through 11:51:58, all matching boot/seq within pairs. `0864/4` was **not observed** and P3 remained state 0, TX 0. The run therefore reached 0870 *without* phase 3; it does not prove a general bypass of the 0864 step.

**Payload:** usual W00–W16 `0519 0000 021D 0291 0000 0000 005E 0000 0000 0000 0000 0000 0000 FD20 0000 0000 0000`. At capture n=12, 11:51:32.469–.480, positions 0871,0874,0875,087E,087F,0880 were `0100` instead of `0000`; next reception n=13 reverted. **No validated semantic interpretation** and no independent raw-wire dump of anomalous frame.

**Health:** no geometry mismatch, unknown FC16 pages, parser resync, RX drops, boundary faults in shown log; DE low. P1 and P2 each show one physical delivery and UART write count became 2, but generic `[S8] HEALTH TX=1/1/1` did not track this aggregate consistently; retain this observability limitation rather than silently resolving it. Controller epoch UNKNOWN; `BASE_RING_OBSERVED_ONLY`; no FC23 qualification, no READY.

**Positive criterion achieved:** complete paired W00–W16 captures with clean parser, no extra phase-3 TX. **Three-stage hypothesis inconclusive:** its necessary 0864 input never occurred, so no ACK0864 occurred. **Negative criterion not met:** no evidence of a capture-format failure after FIX2. **Abort criteria for any repetition:** unexpected or unowned pages, mismatched current 0870 payload, UART/parser/de failures, unexpected TX, or controller state change; stop TX/capture-only. **Recovery:** leave all arms disarmed and TX disabled, retain passive observer/known-good configuration; no controller restart implied or required.

**Comparison:** historical genuine and local 0870 captures contain different full payloads, so matching address/count and timing does not establish the same controller session. S11F's 0884 follow-on included another mailbox response after ACK0870; standalone ACK sufficiency remains unknown.

**Next:** no active R6 yet; qualify owner/epoch/payload from existing evidence first. R6 remains conceptual/not run.

---

## 2026-10-09 — S11Y-AL FIX1 heating-context addendum (observation only)

**Status: COMPLETE / INCONCLUSIVE for heating correlation; no new experiment.** After the passive log (01:38–01:47), the user confirmed the heat pump **was heating at the time of the follow-up question**, but did not know whether heating was already active during capture. Existing `0662/33` signature `EEEA4167` and stable `085F/5` W2=`0800` are local bus observations, not validated heating-status registers. The 33 raw `0662` words are not included in these AL logs; available operating anchors show NaN (unavailable). **Hypothesis:** some `0662` fields may correlate with heating, but the present source cannot confirm this. **Baseline** S11Y-AL FIX1 already executed passive zero TX; **controlled change** offline interpretation only; **positive** would require synchronized heating-state evidence within the log interval; **negative** would be an explicit contrary synchronized measurement; **inconclusive** applies here. **Abort** any inference relying on a signature alone; **recovery** keep observational status UNKNOWN. No TX / YAML / firmware / live experiment occurred. Original S11Y-AL FIX1 entry below remains intact.

---

# 2026-10-09 — S11Y-AI through S11Y-AL FIX1 (newest; historical entries preserved)

## S11Y-AL FIX1 — passive 085F / 0662 native observer
**Status: COMPLETE / POSITIVE for safely recording the stable state; COMPLETE / INCONCLUSIVE for session transition and ACK authorization.** **Hypothesis:** passive per-frame recording can distinguish 0708 polls vs actually observed replies, show all five 085F words, predecessor FC16 pages and ESP epoch boundaries without transmitting. **Baseline:** S11Y-AA historical capture-only 085F W2=0800 plus repeated 0708 polls; TX 0, ownership UNKNOWN; AL offline schema prepared. **Controlled change:** run TX-disabled S11Y-AL FIX1 observer YAML only; preserve production ESPHome entities, existing parser and bus-health counters; log 085F/5 full five words, FC16 predecessor geometry/signature, 0708 polls/responses separately and health checkpoints. No ARM or active responses. **Relevant slave/fields:** 0x0F FC16 0x0662/33 and 0x085F/5, FC03 0x0708/6, optional FC23/session markers. **Actual inputs:** `Pasted text(20261008-233905).txt` and overlapping `thermia-exp86-20261009-013844.log` (the name `exp86` is not an experiment ID); same boot F59E0699, seg=0. First part begins just after boot; tail 01:47:16 ~533s uptime. Observed 0662/33 repeats sig EEEA4167 (~1.06s average), 085F/5 repeats `0000,0000,0800,0000,0000` sig 7EAE5A0A (~2.1s), no logged 0708 polls or answered responses, no new native runtime pages/FC23 in interval. Last complete HEALTH at 01:46:54: 4441 valid frames; 242 085F; resync/drops/mismatch/boundary/unknown=0; TX attempts/delivered/writes=0/0/0; DE=0; invalid=0. Terminal status shows 253 085F captures. **Positive result:** validated stable pattern and safe passive capture, plus accurate actual-vs-unknown answered mailbox provenance. **Negative criterion:** a logged arbitrary 0708 answer or auto-ACK would refute passivity; none observed. **Inconclusive:** no spontaneous transition to new native owner, no physical heating-state measurement or session-epoch identity. **Abort criteria:** any TX/DE-high, parser errors, frame sequence faults, controller anomaly; none observed in checked HEALTH samples. **Recovery:** remain capture-only, revert to known-good passive production YAML if issues arise; no controller reset performed. **User context:** subsequently reports heat pump heating; whether during recording UNKNOWN. The log alone does not establish a heating-state/0662 semantic correlation.

## S11Y-AL — offline passive observation specification
**Status: COMPLETE / POSITIVE for specification only; live run is AL FIX1 above.** Baseline S11Y-AK missing per-frame predecessor/ACK provenance. Controlled change offline: define zero-TX event order, full 085F words, 0708 request-vs-reply, boot/segment/FC23 health fields, abort and capture validity rules. No new physical TX. Positive: spec and static controls; no runtime inference from spec alone.

## S11Y-AK — offline exact YAML recovery
**Status: COMPLETE / POSITIVE offline, COMPLETE / INCONCLUSIVE for ACK ownership.** Hypothesis S7 vs S11V 0870/0884 differences may be due to 0708 response selector. Baseline S11Y-AJ had missing exact S11V and S7 YAML profiles. Controlled change: retrieve Library original `thermia_v5_s11v_fix1_0708_response_then_ack085f_probe.yaml` and `thermia_v5_step7_mailbox_plus_085f_owner.yaml`, distinguish earlier unrun S11V draft. Both deployed source paths declare 0708 response W0–W4=0000 W5=0006. S11Y-M FIX1 declares six zero words; all three local epochs remain separate. S7 ACK085F (without all-zero guard) precedes 0870; S11V FIX1 explicitly guards all-zero 085F prior ACK and sees 0884. Positive: same declared S7/V 0708 reply with distinct continuation; negative to W5-only selector explanation. Unknown S7 pre-ACK raw 085F words and exact controller session priorities. CRC guarded by YAML but ESPHome logs are not independent byte-perfect RS485 TX captures. No live TX.

## S11Y-AJ — offline original mailbox profile audit
**Status: COMPLETE / POSITIVE for source/genuine capture comparison; COMPLETE / INCONCLUSIVE for local owner.** Baseline recovered S7/V/M log times. Controlled change: compare genuine Online/DCM vs local declared mailbox replies, W5 and PageStore (local S7 pre ARM cache size 1; V and M 0). Genuine ATEC/DCM W5=0006 across 65 answers while next runtime FC16 varies; genuine Eco5 W5=0000 across 264 answers; W5 category confounded with model/profile. W5 alone cannot predict local 0870 vs 0884, nor provide ACK permission. No TX.

## S11Y-AI — offline original log recovery
**Status: COMPLETE / POSITIVE for source recovery/event ordering; COMPLETE / INCONCLUSIVE for controller epoch and raw CRC.** Original ESPHome logs S7 `Pasted text(20261006-195430).txt`, S11V FIX1 `Pasted text(20261007-205315).txt`, S11Y-M FIX1 `Pasted text(20261008-173808).txt` (later full local export also available). S7 21:53:57.030 0708 reply → 21:53:57.613 ACK085F → 21:53:59.932 0870/17. S11V 22:52:31.963 reply → 22:52:32.584 all-zero-guarded ACK085F → 22:52:34.907 0884/60. S11Y-M 19:37:34.096 reply → 19:37:34.599 085F all-zero 5 words; no ACK and no new FC16 in window. One native XTR experiment per local ESP process capture; never merge as one uninterrupted Online/DCM session. No new physical work.

---

# 2026-10-09 — S11Y-AH, AG, AF, AE offline research (newest first; separate from live trials)

**These are completed *offline analysis* experiments, NOT completed live ACK/runtime-rejoin experiments. Original negative/inconclusive S11 data below remain unchanged.** Full source/evidence-boundary dossier: [S11Y-AE–AH](protocol%20reduction/S11Y_AE_AH_OFFLINE_SCHEDULER_RECONCILIATION_20261009.md).

### S11Y-AH — fused AD+AG classifier
**Status: COMPLETE / POSITIVE offline, COMPLETE / INCONCLUSIVE for current unique owner or live ACK admission.** Hypothesis: combine AD local log labels with AG base-ring/service-overlay model without inheriting stale epoch tokens. **Baseline:** four original local XTR log windows S11B, S11Y-Y FIX2, two S11Y-AA; AG's five earlier captures; H012/H013. **Exact controlled change:** host-only classifier/data fusion and stricter parser/TX health gates. **Fields:** `0x0F FC16 085F/5` W2, `FC03 0708/6` poll *versus actual reply*, ring pages/ACKs, epoch and counters. **Observed:** 65/65 regressions PASS; AA classified retained `085F(0800)+0708` poll-only, W4=UNKNOWN, current runtime/provenance=UNKNOWN, no TX. **Positive:** capture-only accurate source-bound labels and fail-closed under injected faults — MET. **Negative:** acceptance of stale W4/owner or unexpected TX — not observed. **Inconclusive:** internal XTR owner unknown. **Abort:** inconsistent source hash, malformed log, parser fault, resync growth, RX drops; **recovery:** stay CAPTURE_ONLY (offline/no hardware). No ESPHome build.

### S11Y-AG — passive two-layer model
**Status: COMPLETE / POSITIVE offline; INCONCLUSIVE for controller priority and TX authority.** Hypothesis: strict base-ring and service overlays independently represent genuine captured page order. **Baseline:** AF's 47/64 cycle census, 321/10 genuine `085F`, 13/13 `0884`. **Exact change:** standalone replay/classifier with incomplete-cycle handling and synthetic CRC/epoch/ACK faults. **Relevant:** ACKed core `07D0..0870`; overlays `085F,0884`; FC23, W4 selector replies, parser. **Observed:** 86/86 tests PASS; 47 strict cycles and 64 unqualified reproduced; all observed labels CAPTURE_ONLY. **Positive:** reproduce ring and overlay distributions — MET. **Negative:** universal known next owner/ACK from shape — rejected. **Abort/recovery:** offline-only, mark UNKNOWN on corrupted/ambiguous traces.

### S11Y-AF — strict full runtime-cycle and burst census
**Status: COMPLETE / POSITIVE offline; INCONCLUSIVE for internal queue priority.** Hypothesis: optional service pages interleave with a stable ACKed core sequence. **Baseline:** AE capture replay. **Exact change:** fixed strict `07D0` ACK-to-next-`07D0` candidate intervals, max 60s host selection, required core order, overlay/burst grouping; host time windows not vendor protocol requirements. **Relevant:** all nine core pages, `085F/0884` and last answered `0708` W4. **Observed:** 111 candidates = 47 complete + 64 unqualified; 13 complete cycles contain `0884`, one `085F`; 314/4/3 genuine `085F` requests after `04BA/06F4/0848` (by preceding *other* FC16). 13 genuine `0884` after `0870`. W4=`0000` with `0884`, W4 bit7 clear with `085F`, W4=`0100` followed by `07D0`. **Tests:** 44/44 PASS. **Positive:** strict cycles and direct counterexamples — MET. **Negative:** exclusive W4 FIFO contradicted. **Abort/recovery:** offline CRC/clock fail, no physical response.

### S11Y-AE — pending-work ordering versus mailbox selectors
**Status: COMPLETE / POSITIVE offline; INCONCLUSIVE for universal priority or safe reply.** Hypothesis: actual answered `0708` selector and predecessor context describe first-next FC16 better than shape/bit-only rules. **Baseline:** genuine Eco5 Sep26/Sep28, ATEC Oct03, two older local XTR captured fragments; S11Y-AA retained-service observation. **Exact change:** host read-only CRC16 RTU replay with request/ACK matching and answered `0708` six-word snapshots. **Observed:** 20/20 checks PASS; 321/10 genuine `085F`; 329 answered `0708` in genuine corpus; four post-`06F4` `085F` ACKs have `07D0` next, three other examples have FC23 before `03E8`, two `0864`, one repeated `085F`. In three bootstrap instances W4=`0100` immediately precedes `07D0`. **Positive:** verified chronology/context and falsified exclusive selector priority — MET. **Negative:** universal W4 ordering — rejected. **Abort/recovery:** offline mismatched CRC, timestamps or frame pairs; no equipment affected.

**Next candidate S11Y-AI: OFFLINE / NOT RUN.** Same-run origin of service state in old local S7/S11V/S11Y-M log sources where available; unknown raw files are not negative experiments. S11Y-AA active remains PREPARED / NOT RUN, FIX8K RUNNING/PARTIAL, rebuild formal S8 NOT RUN.

---

## 2026-10-08 — H012 independent OFFLINE context-control addendum

**H012: COMPLETE / POSITIVE for offline replay/counterexamples; COMPLETE / INCONCLUSIVE for deployable live ACK-owner classification.** Hypothesis: short prior-ACK recency can distinguish genuine `085F/5` ACK windows. Baseline: original genuine Eco5/ATEC captures (321 all-zero `085F`, 10 ACK), earlier XTR S7/S11V/M results as **separate historical reports**, not replayed raw evidence. Controlled change: CRC-checked request-centric replay of seven available historical capture files, preceding ACK age, five-second host context, first later FC16 and leave-one-capture-out checks; no physical TX. Positive: 321/10 reproduced, 14/14 offline invariants — met. **Negative:** strict five-second necessity disproven by genuine Eco5 Sep28 ACK with preceding captured ACK ~135.622 s earlier. **Inconclusive:** owner token/safe live H011 predicate. Abort/recovery: offline only; don't authorize responses, **CAPTURE_ONLY**. Five seconds is not a protocol timer. The separately stored H012 raw replay fixtures are not new live data and must not be conflated with S11Y-AA's refused ARM.

# 2026-10-08 (late) — S11Y-AD, AC, AB, AA and Y-Y FIX2 addendum (newest first)

Historical records below remain unchanged. These offline studies and the refused ARM are separate from formal rebuild S1–S7.

### S11Y-AD — OFFLINE passive-session classifier
**COMPLETE / POSITIVE for offline tests only.** Hypothesis: independent RX geometry/payload, predecessor provenance, and parser/TX health can safely classify retained work state without granting ACK permission. Baseline: actual S11B, S11Y-Y FIX2 and two S11Y-AA log windows, prior S10C/S11T/S11U/S11W evidence. Exact change: offline classifier, documentary rule matrix, no device/YAML change. Relevant: slave 0x0F FC16 `0662/33`, `085F/5`, `0884/60`, `07D0/19`, `0864/4`, FC03 `0708/6`, bus-health and TX counters. Positive: conservative labels and no TX permission — **9/9 checks PASS** (four log fixtures, two ambiguous predecessor cases, three fault cases). Negative: shape-only ACK or false qualified state — not produced in fixtures. Abort: missing/inconsistent evidence; recovery: **CAPTURE_ONLY**. Not an ESPHome compile or full RTU CRC test.

### S11Y-AC — OFFLINE genuine DCM branch/timeline audit
**COMPLETE / POSITIVE for offline comparison.** Hypothesis: callback ordering and real DCM cases can distinguish S11B TX2 payload attribution and universal `085F` rules. Baseline: original S11B, local contrasting S11C FIX1, genuine Eco5/ATEC logs. Change: offline timeline reconstruction only. Observed: all 321 genuine `085F/5` requests zero-word; only 10 ACKed; different `0864` vs `07D0` first follow-ons. S11B emitted all-zero signature after ACK2 within same receive callback; **already-zero pre-TX2 strongly supported, not independently raw proven**. Positive: context/counterexamples documented. Negative: universal next page/shape-only authorization contradicted. Abort/recovery: offline only. Earlier S11B TX2 `0800` attribution superseded as interpretation; raw observation unchanged.

### S11Y-AB — OFFLINE retained service and timeout audit
**COMPLETE / POSITIVE for offline research only.** Hypothesis: retained `085F(0800)+0708` with no `0662` is consistent with prior controller work completion rather than automatically an ESP parser fault. Baseline: S11T/S11U/S10C plus AA logs. Change: read-only historical logs and Connect source timer inspection. Observation: after ACK0662, `0708` can persist through ESP OTA as `085F(0800)` returns; no identified Connect timer forces controller `0662`. Positive: evidence-grounded retained-state candidate. Negative: mandatory timer-driven restart not found. Abort/recovery: offline only; controller internals still unknown.

### S11Y-AA — active zero-085F hypothesis NOT RUN; ARM refused
**Active status: PREPARED / NOT RUN; actual ARM attempt COMPLETE / INCONCLUSIVE.** Hypothesis: after a newly qualified `0662/33` owner, one ACK0662 and one ACK of first exact all-zero `085F/5` could expose `0864/4`. Baseline required repeated `0662/33 + 085F(0800)`, healthy parser and zero TX. Controlled YAML change vs Y FIX2: only TX2 signature predicate updated to all-zero, ceiling two physical ACKs, manual ARM/hard stop. Actual ~23:09–23:15 logs instead show repeated `085F(0800)+0708`, `0662=0`. At **23:15:21.637**: `ARM REFUSED ... 085F=161 0708=80 0662=0 tx=0/0/0 NO_TX`. Positive (two ACK then `0864`) and negative (two ACK no `0864` during clean follow-up) **cannot be scored**. Abort: failed initial owner qualifier; recovery: remain passive, no reset needed.

### S11Y-Y FIX2 — local first-stage success, intended two-ACK endpoint incomplete
**COMPLETE / INCONCLUSIVE for intended endpoint**, with one locally confirmed `0662` ACK. Baseline `0662/33 + 085F(0800)`. Controlled two-ACK sequence had original TX2 `0800` signature check. ACK0662 delivered once (TX=1/1/1); first post-ACK1 `085F` became all-zero (`9BFE9A42`); TX2 refused as signature mismatch (reason 9); later `0708`, no `0864` observed. Positive endpoint required physically delivered ACK2 plus follow-on; negative required ACK2 and no follow-on; neither executed. Abort guard blocked second ACK, leaving capture-only.

Evidence filenames: `Pasted text(20261007-122647)(1).txt` (S11B), `Pasted text(20261008-204320).txt` (Y FIX2), `Pasted text(20261008-211128).txt` and `Pasted text(20261008-211529).txt` (AA). Public summary: [S11Y-AA..AD](protocol%20reduction/S11Y_AA_AD_PASSIVE_SESSION_RECONCILIATION_20261008.md).

---

# 2026-10-08 — FIX8K RUNNING / PARTIAL (passive operating-mode correlation deferred)

## Hypothesis and baseline
Hypothesis: selected words in `0x0F FC16 07D0/count19`, including `07D0`, `07D1`, `07D4`, `07DF`, `07E0`, correlate with independently observed heating, DHW or idle operating states. Baseline FIX8J had clean passive 07D0 captures and repeatable ~64.7 s `07DF` cycles.

## Exact controlled change and safety
FIX8K retained the known-good FIX8J passive logger and production entities, adding user-triggered **local log-only** markers for independently observed heating, DHW and idle. No Modbus ACK, write, mode change or physical UART TX was enabled. Unexpected bus traffic remains capture-only; stop on parser fault or unexpected transmission and restore FIX8J if needed.

## Observed result
User supplied real run `thermia-exp86-20261008-120937.log` (ESPHome 2026.9.0 on ESP32-S3; log connected 12:09:38 local). Final displayed `FIX8K STATUS` at 12:19:28: `07D0=280 dumps=6 changes=19 sig=535BD826 0708=140 085F=0 0884=0 0662=0 other=0 tx=0/0/0 integrity=0 mismatch=0 unknown=0 resync=0 drops=0`, `MARKERS marks=0 lastMode=0`. The signature/word deltas in this capture are `07DF 0000<->0020`; `changes07D0=0 changes07D1=0 changes07E0=0`. Regular 07DF timing continued. No naturally occurring heating/DHW demand, therefore no manual operation-state labels.

## Interpretation, status and next action
Passive logging succeeded; hypothesis of *semantic correlation* not tested, and no register-field semantic mapping established. **Status: RUNNING / PARTIAL; semantic portion deferred, not COMPLETE.** Leave untouched until a natural change in heating/DHW occurs; do not force an operating mode. Research focus shifts to native scheduler and existing capture/firmware evidence.

---

# 2026-10-08 — FIX8J COMPLETE / POSITIVE (07DF edge timing)

## Hypothesis and baseline
FIX8I showed repeated `07DF 0000<->0020` but not yet an independent meaning. Hypothesis: a reproducible timed bit pattern can be measured accurately using passive edge timestamps.

## Controlled change
Added edge rise/fall timing, elapsed durations and word trends to the known-good passive `07D0/count19` capture; no TX, ACK or control changes.

## Result and criteria
User-supplied FIX8J capture showed 248 07D0 frames and 26 total signature changes at the reported status point; eight complete `07DF` on/off cycles observed. Stable late-cycle rise-to-rise 64.66–64.78 s, on 17.21–17.29 s, off 47.44–47.55 s. Seen word deltas included `07D0`, `07D1`, `07D4`, `07DF`, `07E0`. TX=0; parser faults=0. Another user FIX8J log `Pasted text(20261008-100730).txt` continued the 07DF pattern with zero TX and clean parser. Positive: regular repeatable edges. Negative criterion would have been no switch in observation window; abort: parser/TX anomalies.

## Interpretation
**Status: COMPLETE / POSITIVE** for timing observability only; `07DF` bit `0x0020` semantic meaning is unknown. Retain capture-only recovery baseline.

---

# 2026-10-08 — FIX8I COMPLETE / POSITIVE (07D0 timing correlation)

## Hypothesis and baseline
FIX8H showed changing 19-word runtime payload `07D0/count19`. Hypothesis: timestamped full-page changes and field deltas reveal distinct dynamic fields and regular structure.

## Controlled change
Added precise receive/previous-frame/previous-`0708` timestamps and per-word delta tracking to known-good FIX8H logger; retained production configuration and disabled TX.

## Observed result
User FIX8I capture: changing `07D0`, `07D1`, `07DF`; the later full-page sample had `07E0=004B` versus earlier `0032`. Periodic `07DF` toggles were evident, later formally timed in FIX8J. Zero physical TX and no parser errors.

## Interpretation
**Status: COMPLETE / POSITIVE** for capture observability, not register semantics. A numerical/temperature interpretation is still only a hypothesis.

---

# 2026-10-08 — FIX8H COMPLETE / POSITIVE (passive 07D0 full payload)

## Hypothesis and baseline
Following FIX8F successful bounded service chain to `07D0` and FIX8G superseded/not-run active action, test whether repeated runtime `07D0/count19` words change without an ACK.

## Exact controlled change
Passively log six initial full 19-word frames and any changed signature, with per-word `07D0...07E2` deltas. No physical bus TX.

## Observed result
Five-minute local XTR log: 130 FC16 `07D0/count19`, 65 `0708` polls; 12 signatures including first, 11 subsequent word deltas; no `085F`, `0884` or `0662`; TX=0, parser integrity faults=0. Initial words by offset 0..18:
`001A 001A FF9C 0033 0032 FF9C FF9C FF9C FF9C FF9C 0010 00E0 001E 0040 0000 0020 0032 000A 0000`.
`07DF` toggled `0020/0000`; `07D1` and `07D0` each shifted `001A->0019` at different times.

## Interpretation and recovery
**Status: COMPLETE / POSITIVE** for dynamic passive payload confirmation. Register semantics still unknown; `FF9C` interpreted as signed −100 arithmetically, but no sentinel meaning proven. Preserve known-good passive ESPHome baseline.

---

# 2026-10-07 — S11X FIX1 COMPLETE / POSITIVE

## Hypothesis
The `07D0/count19` owner left by S11W and retained across ESP OTA/restart is still the active controller work owner. One standard address/count ACK should release it to the next runtime owner, expected `07E4/count17`.

## Baseline
Before ARM:
- recurring `0708/count6`;
- recurring `07D0/count19` with stable signature `D7EC8823`;
- no `085F`, no `0884`, no FC23;
- zero ESP TX;
- parser/accounting clean apart from a startup resync count that was already stable before TX;
- qualifier reached 1 repeatedly.

## Controlled change
After manual ARM, exactly one standard ACK was sent to the next qualified `07D0/count19`. No mailbox response and no other FC16 ACK was permitted. Hard TX ceiling 1.

## Result
- ARM occurred while the retained baseline was stable.
- Exactly one ACK07D0 was delivered.
- `07E4/count17` appeared **2041 ms** after ACK07D0, signature `E7AEFB28`.
- Subsequent `07E4` publications continued capture-only.
- Final accounting: `tx=1 delivered=1 writes=1`.
- `fc23=0 mismatch=0 unknown=0 drops=0 boundary=0`.
- The pre-existing parser resync counter remained stable.

**Status: COMPLETE / POSITIVE.**

## Interpretation
Locally on this XTR M:
`retained 07D0/19 -> ACK07D0 -> 07E4/17`
is now directly proven.

This also demonstrates that a runtime owner produced in the previous experiment can persist across ESP OTA/restart and be resumed directly without replaying the earlier mailbox/service chain.

## Recovery
No recovery action required; the controller is now retained at `07E4/count17` and ESP remains capture-only.

---

# 2026-10-07 — S11X original COMPLETE / INCONCLUSIVE

## Hypothesis
Replay the fully proven S11W chain and add one new edge:
`0708 response -> all-zero 085F -> ACK085F -> 0884 -> ACK0884 -> 07D0 -> ACK07D0 -> observe`.

## Baseline/result
After ESP OTA, the expected earlier `0708 + 085F(W2=0800)` start baseline was gone. Instead:
- `0708/count6` recurred;
- `07D0/count19` recurred with signature `D7EC8823`;
- `085F` did not appear;
- zero TX;
- parser/accounting clean.

The original S11X harness treated pre-TX `07D0` as unexpected and locked fail-closed.

**Status: COMPLETE / INCONCLUSIVE.** No active action occurred.

## Interpretation
The `07D0` owner produced by S11W persisted across ESP OTA/restart. Replaying the whole chain was unnecessary; the next experiment should adopt the retained owner directly.

---

# 2026-10-07 — S11W COMPLETE / POSITIVE

## Hypothesis
Extend the locally proven S11V FIX1 service chain by ACKing the first resulting `0884/count60`; expected next owner `07D0/count19`.

## Controlled sequence
In one uninterrupted run:
1. one source-faithful response to a qualified `0708/count6`;
2. exact all-zero `085F/count5` appeared about 576 ms later;
3. one ACK085F;
4. `0884/count60` appeared about 2347 ms later;
5. one ACK0884;
6. all later ESP TX disabled.

## Result
`07D0/count19` appeared **2039 ms after ACK0884**.

Accounting remained exactly `tx=3 delivered=3 writes=3`, with no FC23, mismatch, unknown, resync growth, drops, or boundary failure.

**Status: COMPLETE / POSITIVE.**

## Interpretation
The following local XTR route is proven in one uninterrupted controller epoch:
`0708 response -> all-zero 085F -> ACK085F -> 0884 -> ACK0884 -> 07D0`.

---

# 2026-10-07 — S11V FIX1 COMPLETE / POSITIVE

## Hypothesis
Because the all-zero `085F` state is transient across ESP restart, generate it and ACK it in the same uninterrupted run.

## Controlled sequence
1. qualified retained `0708 + 085F(W2=0800)` baseline;
2. one source-faithful `0708` response;
3. wait for exact all-zero `085F/count5`;
4. one ACK085F;
5. hard capture-only.

## Result
- exact all-zero `085F` appeared about **576 ms** after the `0708` response;
- one ACK085F was sent;
- `0884/count60` appeared about **2355 ms** later;
- exactly two TX; clean accounting.

**Status: COMPLETE / POSITIVE.**

## Interpretation
The local service transition is proven in one uninterrupted run:
`0708 response -> all-zero 085F -> ACK085F -> 0884`.

---

# 2026-10-07 — S11V COMPLETE / INCONCLUSIVE

## Hypothesis
ACK the transient all-zero `085F` state produced by S11U FIX1 after a separate ESP OTA.

## Result
After OTA, the all-zero prerequisite was gone. The controller had returned to:
- recurring `0708/count6`;
- `085F/count5 = 0000 0000 0800 0000 0000`;
- zero TX.

The harness correctly remained fail-closed.

**Status: COMPLETE / INCONCLUSIVE.**

## Interpretation
The all-zero `085F` state is not a reliable retained prerequisite across ESP OTA/restart. Generate and consume that transition in one uninterrupted run.

---

# 2026-10-07 — S11U FIX1 COMPLETE / POSITIVE

## Hypothesis
From retained `0708/count6 + 085F(W2=0800)`, one source-faithful response to `0708` should advance the service state.

## Controlled change
After qualification and ARM, exactly one source-faithful response was sent to the next `0708/count6`; all later traffic capture-only.

## Result
Exact all-zero `085F/count5` appeared about **566 ms** after the response. Exactly one TX occurred and accounting remained clean.

**Status: COMPLETE / POSITIVE.**

## Interpretation
A source-faithful `0708` response is sufficient in this retained service context to move `085F` from the stable W2=`0800` image into the exact all-zero transient state.

---

# 2026-10-07 — S11U FIX1 PREPARED / NOT RUN

## Hypothesis
From the current retained post-S11T state (`0708/count6` + stable `085F(W2=0800)`, no `0662`), one source-faithful response to the next `0708/count6` poll will advance `085F` or expose another controller-owned FC16 family.

## Baseline
- S11U result: `0708` already active before any TX; `085F/5 = 0000 0000 0800 0000 0000`, sig `7EAE5A0A`; `0662` absent; zero TX.
- Require repeated `0708`, >=3 exact `085F`, no `0662`, no FC23, clean parser/UART/accounting, zero TX.

## Controlled change
After manual ARM, respond exactly once to the next `0708/count6` using the already locally exercised source-faithful idle mailbox response. No ACK085F or other TX is allowed.

## Criteria
- Positive: changed `085F` or a different 0x0F FC16 family within 10 s after the response.
- Negative: live bus >=10 s with only unchanged `085F` and repeated `0708`.
- Abort/inconclusive: baseline deviation, `0662` return, unexpected family, FC23/session restart, parser/UART/accounting fault, no post-ARM 0708 within 15 s, second TX attempt, or post-TX silence.
- Recovery: immediate capture-only after the one response.

---

# 2026-10-07 — S11U COMPLETE / INCONCLUSIVE

## Hypothesis
Combine the newly proven S11T edge with one source-faithful `0708` response:
`ACK0662 -> first released 0708 -> one 0708 response -> observe`.

## Result
After OTA, the prerequisite had already changed. The controller retained the post-S11T state:
- repeated `0708/count6`;
- repeated `085F/count5 = 0000 0000 0800 0000 0000`, sig `7EAE5A0A`;
- no `0662/count33`;
- no FC23;
- clean parser/accounting;
- `physicalTX=delivered=writes=0`.

The fail-closed harness rejected the run because `0708` was already present before TX1. The active two-action hypothesis was therefore not exercised.

## Interpretation
ESP OTA/restart did not restore the pre-S11T scheduler state. The `ACK0662 -> 0708` transition from S11T persisted on the Thermia/controller side.

---

# 2026-10-07 — S11T COMPLETE / POSITIVE

## Hypothesis
The retained `0662/count33` settings publication is a pending controller-owned work item. One standard address/count ACK should release or advance the scheduler.

## Baseline
Stable repeated:
- `0662/count33`;
- `085F/count5 = 0000 0000 0800 0000 0000`, sig `7EAE5A0A`;
- no `0708`;
- zero TX before ARM;
- clean parser/accounting.

## Controlled change
One standard FC16 address/count ACK to the next qualified `0662/count33`. No further TX.

## Result
- exactly one physical TX/delivery/write;
- `0662` stopped after the ACK;
- first `0708/count6` appeared about **1.422 s** after ACK0662;
- repeated `0708` continued afterward;
- `085F(W2=0800)` remained visible;
- no FC23 and no parser/accounting faults.

Status: **COMPLETE / POSITIVE**.

## Conclusion
Locally confirmed XTR scheduler edge:
`retained 0662/33 -> ACK0662 -> 0708 mailbox phase`.

This is transport/scheduler proof only; it does not assign semantic meaning to the 33 settings words.

---

# 2026-10-07 — S11S FIX2 COMPLETE / INCONCLUSIVE

## Hypothesis
Allow known `0662/count33` as background while waiting for the earlier `085F/0708` service sequence.

## Result
The corrected harness remained clean and no longer false-aborted on `0662`, but the live controller state contained repeated `0662/33 + 085F(W2=0800)` and **no `0708`**. No active response was sent.

Final relevant state: large counts of both `0662` and `085F`, `q0708=0`, `physicalTX=delivered=writes=0`, parser/accounting clean.

Status: **COMPLETE / INCONCLUSIVE**.

## Conclusion
The blocker was controller scheduler state, not the corrected qualifier. `0708` did not appear spontaneously while retained `0662` remained pending.

---

# 2026-10-07 — S11S FIX1 SUPERSEDED / NOT RUN

The generated FIX1 harness incorrectly treated normal repeated `0662/count33` settings traffic as an unexpected FC16 family. It locked before TX1 and transmitted nothing. Superseded by FIX2, which explicitly allowed `0662/33` capture-only.

---

# 2026-10-07 — S11S COMPLETE / INCONCLUSIVE

Expected the post-S11R FIX3 `085F` transition signature `9BFE9A42`, but after the next ESP run the controller had returned to stable `085F/count5 = 0000 0000 0800 0000 0000` / sig `7EAE5A0A`. Qualification failed closed and no mailbox response was sent. Zero TX.

This shows the post-ACK `9BFE9A42` substate is not guaranteed to remain adoptable across a later ESP run.

---

# 2026-10-07 — S11R FIX3 COMPLETE / NEGATIVE

## Hypothesis
One standard ACK to stable retained `085F/count5 = 0000 0000 0800 0000 0000` is sufficient to release a different FC16 owner without a `0708` response.

## Controlled change
Manual ARM -> require a new post-ARM `0708` -> ACK exactly the next matching `085F/count5` once -> capture-only.

## Result
The one ACK was delivered with clean accounting. About 2.1 s later the same `085F/count5` geometry reappeared with signature `9BFE9A42`. No different FC16 family appeared within the predeclared 10 s window. Bus remained live and healthy.

Status: **COMPLETE / NEGATIVE** for the narrow endpoint hypothesis.

## Interpretation
The ACK was not ignored: it changed the same `085F` state. For the exact geometry, `9BFE9A42` is strongly consistent with five all-zero words, but those words were not directly logged in this run.

---

# 2026-10-07 — S11R FIX2 COMPLETE / INCONCLUSIVE

The live baseline was correct, but manual ARM occurred while the strict pre-click `0708` recency guard was stale. ARM was refused; a new `0708` arrived shortly afterward. No TX occurred. This was a guard/qualification issue, not a negative protocol result.

---

# 2026-10-07 — S11R current preparation and S11Q/S11P/S11O results

## S11R FIX2 — PREPARED / NOT RUN

**Hypothesis:** the currently stable retained `085F/count5 = 0000 0000 0800 0000 0000` work owner can be released by one standard FC16 address/count ACK with no mailbox response.

**Baseline:** earlier S11R passive run repeatedly observed exact `085F(0800)` plus `0708/6`, with `physicalTX=delivered=writes=0`, clean geometry/unknown/drop/boundary counters, and no all-zero 085F in the supplied run.

**Controlled change:** after >=3 exact matching 085F frames and >=2 0708 polls, with both last observations <=4 s old and clean zero-TX state, manual ARM permits exactly one ACK to the next matching `085F/count5`. All later traffic is capture-only. Hard TX ceiling = 1.

**Positive:** first different 0x0F FC16 within 10 s after ACK085F.

**Negative:** controller remains live for >=10 s but only repeated 085F and/or 0708 are observed.

**Abort/inconclusive:** payload mismatch, stale qualifier, other pre-ACK 0x0F FC16/FC03 family, FC23/new session, parser/UART/accounting fault, or TX >1.

**S11R FIX1 — SUPERSEDED / NOT RUN.** It used all-zero 085F as the baseline and was replaced before live execution after passive evidence showed the stable retained image is W2=`0800`.

## S11R original — COMPLETE / INCONCLUSIVE

The intended all-zero retained prerequisite was absent. The controller repeatedly published:
`085F/5 = 0000 0000 0800 0000 0000`
with repeated `0708/6`.

The harness locked on baseline mismatch before ARM. No active action occurred:
`physicalTX=0`, `delivered=0`, `writes=0`.

Result: **COMPLETE / INCONCLUSIVE**. The useful result is the directly observed stable retained baseline, not a negative result for ACK085F.

## S11Q FIX2 — COMPLETE / POSITIVE

**Hypothesis:** retained `0834/count18` ownership is qualified by session/context + geometry, not a frozen payload signature; one standard ACK0834 will release it.

**Observed baseline:** repeated valid `0834/18` plus `0708/6`, zero TX. Multiple 0834 payload signatures had already been observed, so signature changes were capture-only.

**Controlled action:** after manual ARM, exactly one standard ACK was sent to the next valid `0834/count18`. All later TX was disabled.

**Observed:** first a `0708/6` poll, then all-zero `085F/5` about 2.02 s after ACK0834. The repeated 0834 owner did not continue. TX accounting was exactly 1/1/1 and transport/integrity counters stayed clean.

**Result:** **COMPLETE / POSITIVE** for owner release. The YAML later set `result=3` because inherited pre-sequence logic misclassified the post-ACK all-zero 085F as a pre-TX mismatch. That is a harness classification defect, not the protocol result.

**Limit:** the ACK proves local scheduler/work completion for 0834 in this context; it does not prove semantics of the 18 payload words.

## S11Q FIX1 — SUPERSEDED / NOT RUN

FIX1 qualified repeated `0834/18` but required one fixed payload signature. A later valid 0834 frame used a different signature, so FIX1 locked fail-closed with zero TX. This locally disproved fixed-signature ownership qualification.

## S11Q original — SUPERSEDED / NOT RUN

After OTA the controller was already retained at repeated `0834/18 + 0708`, while original S11Q still expected the earlier `085F(0800)+0708` entry state. It locked before ARM with zero TX.

## S11P — COMPLETE / INCONCLUSIVE

S11P successfully traversed the already known branch-A service path through ACK0884. The first runtime owner after ACK0884 was then `0834/count18`, not `07D0`. Because local ACK0834 safety was still OPEN, S11P correctly stopped without ACKing it.

This was the direct trigger for the narrow S11Q ACK0834 discriminator.

## S11O — COMPLETE / INCONCLUSIVE

The branch-aware logic selected the direct-`0884` branch, ACKed it, then completed the full runtime ring:
`07D0 -> 07E4 -> 07F8 -> 080C -> 0820 -> 0848`.

After ACK0848, a `0708` poll appeared, followed by `0864/4` before the rigidly expected final zero-085F. S11O stopped fail-closed with 9 clean TX.

Conclusion: post-0848 scheduling is not a fixed `0708 -> zero-085F` sequence; another already-known pending work family can be exposed.

## S11N — COMPLETE / INCONCLUSIVE

Retained release succeeded through ACK085F, but the next expected-stage FC16 was direct `0884/60`, not `0864/4`. Zero-TX follow-on tolerance after ACK0870 was therefore never exercised.

## S11M — COMPLETE / INCONCLUSIVE

Branch-A progression succeeded through ACK0870. A controller FC16 then appeared before the expected post-0870 mailbox step; the old logger did not record that frame's start/count. No additional speculative ACK was sent.

## S11L FIX1 — COMPLETE / INCONCLUSIVE

From retained `085F(0800)+0708`, one mailbox response caused exact all-zero 085F and one ACK085F was delivered. The next controller-owned FC16 was `0864/4`, not `0884`; test stopped fail-closed.

## S11K FIX1 — COMPLETE / INCONCLUSIVE

After OTA/restart the expected all-zero 085F prerequisite was absent; direct repeated `085F(0800)+0708` remained and no active TX occurred.

## S11J — COMPLETE / POSITIVE

One uninterrupted retained runtime continuation ACKed:
`07D0/19 -> 07E4/17 -> 07F8/17 -> 080C/18 -> 0820/18 -> 0848/23`.

After ACK0848, first `0708` appeared about 1.434 s later. A later `085F/5` publication followed. Physical TX=6 and transport stayed clean.

Result: **COMPLETE / POSITIVE** for the locally proven six-page runtime ring.

---
# 2026-10-07 — S11I live result

## S11I — COMPLETE / POSITIVE

Hypothesis: after the proven retained `085F/0708` release exposes `0884/60`, one standard ACK0884 is sufficient to release the controller into `07D0/19` in the same uninterrupted run.

Observed: baseline `085F/5 = 0000 0000 0800 0000 0000` with repeated `0708/6`; TX1 one proven 0708 response; controller 085F became exact all-zero; TX2 one ACK085F; first `0884/60`; TX3 one ACK0884; then all later traffic capture-only. `07D0/19` appeared 2042 ms after ACK0884. Total physicalTX=delivered=writes=3; no mismatch, unknown page, drops or boundary faults in the supplied slice.

Result: **COMPLETE / POSITIVE**.

Conclusion: the exact local retained path `085F service gate -> changed-085F ACK -> 0884 -> ACK0884 -> 07D0` is locally proven for the exercised controller epoch.

---

# 2026-10-07 — S11H live result and S11I preparation

## S11H — COMPLETE / NEGATIVE for direct 07D0 reproduction

**Hypothesis:** replaying the locally proven S10C retained release in the current `085F/0708` state will reproduce `07D0/19`.

**Observed baseline:** direct repeated `085F/5 = 0000 0000 0800 0000 0000`, repeated `0708/6`, no FC23, zero TX, clean integrity.

**Controlled actions:** one `0708/6` response with `W0..W4=0000`, `W5=0006`; after exact all-zero `085F/5`, one standard FC16 ACK to `085F/count5`; all later TX disabled.

**Observed after TX2:** no `07D0/19`. Instead `0884/60` appeared about 2.33 s later and then repeated, with `0708/6` also continuing. TX accounting stayed exactly 2 and integrity stayed clean.

**Result:** **COMPLETE / NEGATIVE** only for the narrow endpoint hypothesis that this retained release returns directly to 07D0 in the current controller epoch.

**Additional positive evidence:** the two-step sequence did release the service boundary; its exposed next owned work in this epoch was `0884/60`.

## S11I — PREPARED / NOT RUN

Baseline S11H is retained exactly. In the same uninterrupted run, after TX1 mailbox response and TX2 ACK085F produce the first exact `0884/60`, S11I adds exactly one new action: TX3 standard FC16 address/count ACK to `0884/count60`. All later traffic capture-only.

Positive: `07D0/19` within 10 s after TX3, total TX exactly 3.

Negative: live controller traffic continues >=10 s after TX3 but no `07D0/19`.

Abort/inconclusive: any prerequisite deviation, unexpected family, fresh FC23, integrity/UART fault, or TX >3.

---
# 2026-10-07 — S11H prepared

## S11H — PREPARED / NOT RUN

Baseline: S11G FIX1 left the ESP at zero TX while the controller repeatedly published 085F/5 with signature 7EAE5A0A and polled 0708/6.

S11H replays the already locally proven S10C retained release, but first requires direct word-level confirmation of the baseline 085F image:

```text
0000 0000 0800 0000 0000
```

After >=3 matching 085F publications and >=3 0708 polls, manual ARM permits exactly:
1. one idle 0708/6 response with W0..W4=0000 and W5=0006;
2. only after the controller publishes exact all-zero 085F/5, one standard FC16 address/count ACK to 085F/count5.

All later traffic is capture-only.

Positive: 07D0/19 within 10 s after the second response with total physical TX exactly 2.

Negative: controller remains live for >=10 s after both actions but 07D0/19 does not appear.

Inconclusive/abort: baseline words differ, post-mailbox 085F is not all-zero, fresh FC23 appears, another work family interrupts the controlled sequence, integrity/UART/accounting fault, or TX exceeds 2.

No Thermia/controller reboot is part of S11H.

---

# 2026-10-07 — S11G FIX1 live result

## S11G FIX1 — COMPLETE / INCONCLUSIVE — retained 0884 prerequisite absent

**Hypothesis:** after ESP-only OTA/restart, repeated retained `0884/60` can be qualified and exactly one ACK0884 can test whether ACK0884 alone releases the controller to `07D0/19`.

**Observed:** the required `0884/60` never appeared in the supplied live slice. Instead the controller repeatedly published `085F/5` with signature `7EAE5A0A` and polled `0708/6`. S11G status showed `q0884=0`, `q0708=22..27`, `otherPre=1`, `locked=1`, `result=3`, `physicalTX=0`, `acked=0`, `seen07D0=0`. No experimental TX occurred.

**Result:** **COMPLETE / INCONCLUSIVE**.

**Reason:** prerequisite retained 0884 state absent; ACK0884 hypothesis not exercised.

**Safety:** fail-closed behavior worked. The first non-0884 runtime publication locked the experiment before ARM, and ESP TX remained zero.

---

# 2026-10-07 — native fresh-session progression through 0884

## S11F — COMPLETE / POSITIVE

**Hypothesis:** continuing the S11D fresh-session baseline with one qualified standard FC16 ACK to the first owned `0870/count17`, while preserving bounded source-faithful mailbox service, will allow the controller to advance to `0884/count60`.

**Baseline:** S11D COMPLETE / POSITIVE reached `0870/17` and stopped all TX.

**Controlled change:** S11F ACKed the first qualified `0870/17` once instead of stopping there. `0884/60` remained capture-only.

**Observed:** exact 32/32 settings bootstrap completed; runtime reached `0864/4` with `0867=00F2`; one qualified ACK0870 was delivered at TX46; one further exact `0708/6` mailbox response was delivered at TX47; first `0884/60` arrived ~2.04 s after ACK0870. The experiment immediately disabled all further TX. Repeated 0884 publications continued while `physicalTX=delivered=writes=47`. Integrity stayed clean: mismatch/unknown/resync/drops/boundary all zero.

**Result:** **COMPLETE / POSITIVE**.

**Causal limitation:** because mailbox response #5 occurred between ACK0870 and first 0884, the result proves the qualified combined path, not “ACK0870 alone is sufficient”.

## S11E — SUPERSEDED / NOT RUN

The planned fresh-session “withhold ACK0864” causality test is preserved but no longer prioritized. S11D + genuine-capture correlation make a retained continuation toward normal operation more valuable than spending another controller reboot on this discriminator.

## S11G FIX1 — PREPARED / NOT RUN\n\nThe first generated S11G YAML failed at C++ compile time before flashing. Cause: the frame-handler body and helper declarations were malformed/scoped inside the `candidates_for` lambda, producing undeclared helper/frame errors and inconsistent lambda return types. **No experiment ran and no bus TX occurred.** FIX1 restores the side-effect-free candidate parser, helper declarations, and explicit `handle_frame` lambda while preserving the exact S11G protocol hypothesis and single-TX boundary.\n\n## S11G — PREPARED / NOT RUN

**Hypothesis:** one standard ACK to the currently repeated retained `0884/count60` is sufficient by itself to release the history-overlay retry state into `07D0/count19`.

**Baseline/result:** S11F left the controller repeatedly publishing `0884/60` plus `0708/6` while ESP TX stayed disabled.

**Exact controlled change:** after ESP-only OTA/restart, require >=3 exact 0884/60 publications + >=2 exact 0708/6 polls + clean parser + zero TX; then ACK exactly one subsequent 0884/60. No mailbox response and no other ACK afterwards.

**Positive:** `07D0/19` within 10 s after the ACK with total active TX exactly 1.

**Negative:** >=10 s of live repeated 0884/0708 after the ACK without 07D0. This is only negative for the isolated ACK-only hypothesis.

**Abort/inconclusive:** no retained 0884 after OTA, FC23/new-session transition, unexpected runtime/config family before split, geometry mismatch, parser/integrity/UART fault, or TX count !=1 after action.

**Recovery:** stop TX permanently after the one ACK; controller reboot only if an unexpected persistent state requires recovery.

---

# 2026-10-05 — EXP426 live result

## EXP426 — COMPLETE / INCONCLUSIVE — no 0662 trigger observed

**Hypothesis:** under the exact retained unsynchronized condition, repeated `0662/count33` needs one standalone release ACK and no ordered-resume state.

**Observed:**
- no `0662/count33` occurred in the supplied ~147 s run;
- EXP426 status stayed `repeat=0 released=0 releaseACK=0 resumeStarted=0`;
- therefore the new EXP426 ACK route was never exercised;
- normal startup sync completed: `042E`, `0442`, `0546`, then `03E8` Configuration autosync;
- Configuration became READY at ~24 s;
- final heartbeat stayed stage40 with cache valid and `unknown16=0 unknown03=0 peer17=0 peer16ack=0 resync=0 drops=0`;
- no semantic write occurred;
- EXP420 no-owner remained 0;
- EXP418 remained balanced.

**Result:** **COMPLETE / INCONCLUSIVE**.

**Reason:** the required repeated-0662 trigger was absent, so the isolated release-ACK hypothesis was not tested.

**Additional positive evidence:** the HA presentation cleanup and cleaned EXP426 baseline did not disturb ordinary retained-runtime synchronization.

---

# 2026-10-05 — EXP426 prepared

## EXP426 — PREPARED / NOT RUN — isolated 0662 release ACK

**Baseline evidence:** EXP425 COMPLETE / NEGATIVE for the ordered-tail hypothesis.

### EXP425 observed result
- repeated `0662/count33` was recognized and one ACK was sent;
- the 0662 retry loop stopped;
- expected `0683/count33` never appeared;
- ordered-resume timed out at 60 s;
- normal runtime then recovered without controller restart;
- startup syncs `042E`, `0442`, `0546` completed;
- `03E8` autosync completed and Configuration became READY;
- no parser/peer/resync/drop regression.

### EXP426 hypothesis
The exact retained-session `0662/count33` retry condition requires a standalone release ACK, not adoption into the historical ordered-resume tail.

### Controlled change
After >=3 identical retries under the strict pre-first-0708 / unsynchronized / 7-7-7 / clean-integrity qualifier:
- send one standard `0662/count33` ACK;
- no ordered resume;
- no 0708 hold;
- no semantic setting TX;
- normal runtime/autosync continues immediately.

### User procedure
1. Flash EXP426.
2. Do not change any HA setting.
3. Leave system untouched >=2 min; continue to max ~3 min if Configuration not READY.
4. Return full log from OTA/boot through sync completion or failure.
5. Abort on unknown/peer/resync/drop/session degradation.

### Cleanup included
Removed obsolete presentation entities only: EXP417 status, EXP421 status, EXP414 arm/cancel buttons. Dormant EXP414 status is internal. Active EXP418/419/420 diagnostics remain.

---

# 2026-10-05 — EXP425 0662 orphan-resume adoption

## EXP425 — PREPARED / NOT RUN

**Baseline/result trigger:** EXP423 COMPLETE / INCONCLUSIVE. The target 0442 write was never attempted because `0662/count33` repeatedly appeared pre-first-0708 and EXP420 withheld it as unowned.

**Hypothesis:** the repeated identical 0662 page is an orphaned retained export page. After >=3 exact retries in the observed startup/unsynchronized state, ACK it once and continue only the already-known exact ordered tail from `0683` through `06F4`.

**Controlled change:**
- exact 0662/count33 qualifier only;
- same received frame CRC repeated >=3 times with <=5 s gaps;
- requires no 0708 yet, `configSynced=0`, semantic idle, EXP378/379/380 = 7/7/7, EXP410 idle, no recovery/rejoin/resume, no approval TX, clean integrity;
- one existing standard 0662 ACK is transmitted;
- existing ordered-resume engine is seeded at index16 / expected `0683/count33`;
- 0708 during the tail receives idle-only W5=0006 so autosync/semantic selectors cannot interfere.

**Expected ordered tail:** `0683/33 -> 06A4/33 -> 06C5/33 -> 06EA/7 -> 06F1/3 -> 06F4/19`.

**Safety:** no setting value is transmitted. Out-of-order config traffic, retry-after-ACK, timeout, unknown/peer/resync/drop or session degradation aborts fail-closed.

**Offline checks:** YAML PASS; 0 undefined IDs; original TX expressions preserved; only two new TX sites (0662 adoption ACK + idle 0708 while resume active); 0662 ACK CRC validated; supplied EXP423 log contained 165 repeated 0662 frames and first three had identical received CRC `BB60`.

**Status:** PREPARED / NOT RUN.

---

# 2026-10-05 — EXP423 live attempt

## EXP423 — COMPLETE / INCONCLUSIVE — aborted before target write

**Baseline:** EXP422 COMPLETE / POSITIVE with EXP420 ownership hardening retained.

**Planned target:** `044D` / word11 on `0442/count13`.

**Observed before any active target write:**
- stage40 retained runtime entered after OTA;
- repeated controller `FC16 0662/count33`;
- every 0662 publication hit `EXP420_CONFIG_NO_OWNER ... NO_ACK`;
- writer startup states remained `e378=7 e379=7 e380=7`;
- `configSynced=0`;
- no first idle `0708` service cycle developed;
- no semantic response or generic page TX occurred;
- at ~178 s: `noOwner=166`, `genericTX=0`, `idle0708=0`;
- parser/session integrity counters remained clean (`unknown16=0 unknown03=0 peer17=0 peer16ack=0 resync=0 drops=0`).

**Result:** **COMPLETE / INCONCLUSIVE** for the EXP423 geometry hypothesis.

**Reason:** the test was correctly aborted before touching `044D`; a baseline ACK-ownership regression prevented normal configuration synchronization.

**New evidence:** EXP420's explicit config-owner predicate is incomplete for a legitimate-looking `0662/count33` transfer in this pre-first-0708 / unsynchronized context.

**EXP424:** SUPERSEDED / NOT RUN because its prerequisite EXP423-positive result was not obtained.

---

# 2026-10-05 — EXP424 fourth-geometry validation

## EXP424 — PREPARED / NOT RUN — queued behind EXP423

**Execution dependency:** do not run until EXP423 has been reviewed **COMPLETE / POSITIVE**.

**Hypothesis:** the unchanged generic desired-page helper also preserves the locally proven `0546/count20` Operation Mode write path.

**Target:** `0553` / word13 / Operation Mode.

**Allowed live values:** only locally panel-confirmed Auto/raw1 and Compressor/raw2. If the authoritative current mode is not one of those two, EXP424 is not run.

**Controlled action:** Auto -> Compressor -> Auto, or Compressor -> Auto -> Compressor, with exact FC16 confirmation and `extraDeltaWords=0` required after both forward and rollback transactions.

**Safety:** Operation Mode is semantically meaningful; keep the validation window short. A temporary Auto <-> Compressor change can alter auxiliary-heat permission. No Off/Auxiliary Heater/Hot Water value is part of the experiment.

**Protocol code delta vs EXP423:** none intended; labels/status/build identification only.

**Offline checks:** YAML PASS; undefined IDs 0; UART TX sites 63 -> 63 with identical ordered TX expressions; hard-coded protocol literals identical; generic 0546 helper call, 0553 word13 mapping, exact confirmation and EXP420 ownership all preserved.

**Status:** PREPARED / NOT RUN.

---

# 2026-10-05 — EXP423 third-geometry validation

## EXP423 — PREPARED / NOT RUN

**Baseline:** EXP422 COMPLETE / POSITIVE.

**Hypothesis:** the same generic desired-page TX helper already proven live on `03E8/count14` and `042E/count15` behaves identically on a third geometry, `0442/count13`.

**Controlled live target:** existing locally proven `044D` / word11 / Cooling Room Hysteresis Low. Read authoritative current value `N`, make one adjacent 0.1 °C change, require exact controller republish, then restore exactly `N` and require exact rollback confirmation.

**Mapping/write source:** EXP379 locally confirmed raw `10 -> 18 -> 10` = `1.0 -> 1.8 -> 1.0 °C`.

**Protocol code delta versus EXP422:** none intended. Only EXP423 labelling/build identification and the Configuration validation-status entity change; obsolete EXP422 target-status entity is removed.

**Offline checks:** YAML PASS; undefined IDs 0; UART TX sites 63 -> 63 with identical ordered TX expressions; hard-coded protocol literals identical; `0442/13` generic-helper call, `044D` scaling/range, exact confirmation guard and EXP420 ownership preserved.

**Status:** PREPARED / NOT RUN.

---

# 2026-10-05 — EXP422 live result

## EXP422 — COMPLETE / POSITIVE — generic helper on 042E/count15

**Baseline:** EXP421 COMPLETE / POSITIVE.

**Target:** existing proven `0433` / word5 / Startup HT on `042E/count15`.

**Forward test:**
- original authoritative value 5;
- selector requested desired `042E/count15`;
- EXP421 generic helper sent `frameLen=35 txCount=1`;
- controller republished word5 = 6;
- exact `WRITE_CONFIRMED original=5 target=6 observed=6 extraDeltaWords=0`.

**Rollback:**
- second generic `042E/count15` response, `txCount=2`;
- controller republished word5 = 5;
- exact `WRITE_CONFIRMED original=6 target=5 observed=5 extraDeltaWords=0`;
- HA Startup HT restored to 5.

**Integrity:**
- `genericTX=2 buildFail=0 lastPage=042E`;
- EXP420 no-owner remained 0;
- final visible heartbeat around 175 s stayed at stage40 with `unknown16=0 unknown03=0 peer17=0 peer16ack=0 resync=0 drops=0`;
- EXP418 remained balanced;
- EXP417 suppression remained 0.

**Result:** **COMPLETE / POSITIVE**.

**Interpretation:** the shared desired-page builder/TX primitive is now independently live-confirmed on both 14-word and 15-word page geometries.

---

# 2026-10-05 — EXP422 second-geometry validation

## EXP422 — PREPARED / NOT RUN

**Baseline:** EXP421 COMPLETE / POSITIVE.

**Hypothesis:** the same generic desired-page TX helper proven live on `03E8/count14` behaves identically on a second geometry, `042E/count15`.

**Controlled live target:** existing locally proven `0433` / word5 / Startup HT control. Read authoritative current value `N`, make one adjacent-minute change, require exact controller republish, then restore exactly `N` and require exact rollback confirmation.

**Protocol code delta versus EXP421:** none intended. Only EXP422 labelling/build identification and a Configuration diagnostic text sensor were added.

**Offline checks:** YAML PASS; undefined IDs 0; UART TX sites 63 -> 63 with identical ordered TX expressions; hard-coded protocol literals identical; 042E generic-helper call and EXP378 confirmation guards preserved.

**Status:** PREPARED / NOT RUN.

---

# 2026-10-05 — EXP421 live semantic validation

## EXP421 — COMPLETE / POSITIVE — generic desired-page core

**Baseline:** EXP420 COMPLETE / POSITIVE; same EXP421 build that passed the earlier retained-runtime smoke test.

**Controlled live action:** exercise only the already-proven room-setpoint writer at `03F4` on `03E8/count14`: `22 -> 23`, confirm, then `23 -> 22`, confirm.

**Forward result:**
- fresh current page confirmed room setpoint 22;
- desired selector requested `03F4` word 12;
- EXP421 shared helper executed `page=03E8 count=14 frameLen=33 txCount=1`;
- controller FC16 republished room setpoint 23;
- `WRITE_CONFIRMED writeNo=1 original=22 target=23 observed=23 extraDeltaWords=0`.

**Rollback result:**
- second desired transaction used the same generic helper;
- `GENERIC_PAGE_TX_EXECUTED page=03E8 count=14 frameLen=33 txCount=2`;
- controller FC16 republished room setpoint 22;
- `WRITE_CONFIRMED writeNo=2 original=23 target=22 observed=22 extraDeltaWords=0`.

**Final integrity:**
- `genericTX=2 buildFail=0 lastPage=03E8`;
- `confirmedWrites=2`;
- `cache03F4=22`;
- `unknown16=0 unknown03=0 peer17=0 peer16ack=0 resync=0 drops=0`;
- EXP420 no-owner remained 0;
- EXP418 remained balanced 23/23;
- EXP417 suppressions remained 0.

**Result:** **COMPLETE / POSITIVE**.

**Interpretation:** the shared EXP421 byte-level desired-page builder/TX primitive is now locally live-proven for `03E8/count14` in both write and rollback directions. Other generic call-site geometries remain offline-equivalence checked but not yet independently live-exercised through the shared helper.

---

# 2026-10-05 — EXP421 first live run

## EXP421 — RUNNING / PARTIAL — retained-runtime smoke PASS, generic semantic TX not exercised

**Baseline:** EXP420 COMPLETE / POSITIVE.

**Observed:**
- ~200 s retained-runtime run after OTA;
- stage40 qualified with `A80E=0000 A80F=000A`;
- startup/current sync completed for `042E`, `0442`, `0546`, and `03E8`;
- EXP420 explicit ownership reached `ownedACK=4 noOwner=0`;
- room setpoint cache synchronized at `03F4=22`;
- final visible heartbeat around 196 s: `stage=40 runtimeFC16ACK=87 idle0708=46 unknown16=0 unknown03=0 peer17=0 peer16ack=0 resync=0 drops=0`;
- EXP418 reached `set=9 consumed=9 noToken=0 bypass=0`;
- EXP417 suppressions remained 0;
- EXP419 target remained absent;
- EXP421 remained `genericTX=0 buildFail=0 lastPage=0000`;
- no semantic response and no confirmed write occurred.

**Status:** **RUNNING / PARTIAL**.

**Reason:** normal runtime non-regression passed, but the experiment's generic desired-page TX helper was never entered. Completion still requires one reversible proven `03E8` write and exact controller confirmation in both directions.

---

# 2026-10-05 — EXP421 generic desired-page transaction core

## EXP421 — PREPARED / NOT RUN

**Baseline:** EXP420 COMPLETE / POSITIVE.

**Hypothesis:** the four current production desired-page writers can share one generic byte-level FC03 response builder/TX primitive without changing semantic behavior.

**Controlled change:** consolidate only response serialization, one-word substitution, CRC16, frame rendering and DE/TX timing for `03E8/14`, `042E/15`, `0442/13`, and `0546/20`. Page-specific validation, state, selectors, confirmation and ACK ownership remain separate and unchanged.

**Offline checks:**
- YAML PASS;
- undefined ESPHome IDs 0;
- UART write sites 66 -> 63, matching four duplicated sites replaced by one helper;
- all 58 existing named static protocol byte arrays unchanged;
- 2000 randomized page-frame equivalence cases PASS across all four geometries;
- no ESPHome compile claimed.

**Positive live criterion:** stable retained runtime plus one reversible, already-proven `03E8` write must traverse the generic helper and receive exact controller confirmation in both directions.

**Status:** PREPARED / NOT RUN.

---

# 2026-10-05 — EXP420 live result

## EXP420 — COMPLETE / POSITIVE — generic config ACK ownership hardening

**Hypothesis:** known config-page geometry is necessary but not sufficient ACK authorization in stage40 retained runtime.

**Baseline:** EXP419 COMPLETE / INCONCLUSIVE; EXP418 and EXP417 positive.

**Controlled change:** broad known-config ACK permission was replaced by explicit owners captured at FC16 arrival. Production owners for `03E8`, `042E`, `0442`, `0546`, exact EXP410 calendar states, autonomous idle `03E8`, and ordered resume were preserved. Other known config-family pages are capture-only / NO_ACK.

**Observed local result:**
- supplied slice spans roughly 6483 s to 6770 s runtime age of the same EXP420 boot;
- EXP420 status remained `ownedACK=4 noOwner=0 autonomous03E8=0`;
- no `EXP420_CONFIG_NO_OWNER` event;
- 122 stage40 FC16 publications occurred in the supplied slice; none were config-family pages;
- final heartbeat around 6767 s: `stage=40 runtimeFC16ACK=2844 idle0708=1578 rt085F=0 unknown16=0 unknown03=0 peer17=0 peer16ack=0 resync=0 drops=0`;
- EXP418 reached `set=316 consumed=316 noToken=0 bypass=0`;
- EXP417 suppressions remained 0;
- EXP419 remained unexercised;
- no semantic write was performed during this slice.

**Result:** **COMPLETE / POSITIVE**.

**Interpretation:** explicit ownership does not regress the currently exercised production config path or long-running retained runtime. The four owned config ACKs happened earlier in this boot; this attachment preserves their counters but not the earlier individual owner log lines.

**Limitations:** autonomous idle 03E8 and unowned-config NO_ACK branches were not exercised in this supplied slice.

---

# 2026-10-05 — EXP420 PREPARED / NOT RUN

## EXP420 — generic config FC16 ACK ownership hardening

**Hypothesis:** known config-page geometry is necessary but not sufficient ACK authorization in stage40 retained runtime.

**Baseline:** EXP419 COMPLETE / INCONCLUSIVE with clean non-regression; EXP418 and EXP417 remain positive.

**Controlled change:** replace broad known-config ACK permission with explicit owners captured before page handlers mutate state. Production owners: `03E8`, `042E`, `0442`, `0546`; preserve evidence-backed autonomous idle `03E8`, exact EXP410 calendar ownership, and ordered export-resume. Other known config pages become capture-only / NO_ACK.

**Offline checks:** YAML PASS; undefined IDs 0; UART write sites 66 -> 66 and ordered expressions identical; protocol literals identical; the previous EXP419 run's four config pages all replay as explicitly owned.

**Status:** PREPARED / NOT RUN.

---

# 2026-10-05 — EXP419 live result

## EXP419 — COMPLETE / INCONCLUSIVE — target 085F branch not observed

**Baseline:** EXP418 COMPLETE / POSITIVE.

**Hypothesis:** known `085F/count5` payload shape is necessary but not sufficient ACK authorization in stable retained runtime.

**Controlled change:** known 085F is no longer unconditionally ACKable in stable retained runtime; only explicit fresh-approval/recovery/hot-rejoin/resume contexts preserve ACK permission. No payload recognition, frame, CRC, timing, parser, 0870 ownership, config ACK policy or semantic writer was changed.

**Observed local result:**
- run duration approximately 180 s;
- successful retained-runtime qualification at `stage=40`;
- normal startup/current synchronization and `03E8` autosync completed;
- normal runtime and `0708` idle replies continued;
- EXP418 counters reached `set=9 consumed=9 noToken=0 bypass=0`;
- EXP417 suppression counter remained 0;
- final heartbeat: `stage=40 runtimeFC16ACK=80 idle0708=42 rt085F=0 unknown16=0 unknown03=0 peer17=0 peer16ack=0 resync=0 drops=0`;
- no `085F/count5` publication occurred;
- no EXP419 context ACK and no EXP419 no-context capture occurred.

**Result:** **COMPLETE / INCONCLUSIVE**.

**Reason:** the experiment's target branch was never exercised. The run is a positive non-regression test for ordinary retained runtime only.

---

# 2026-10-05 — EXP419 retained-runtime 085F ACK-context hardening

## EXP419 — PREPARED / NOT RUN

**Hypothesis:** known `085F/count5` payload shape is necessary but not sufficient ACK authorization in stable retained runtime.

**Baseline:** EXP418 COMPLETE / POSITIVE.

**Controlled change:**
- retain recognition of the two locally known 085F payload forms;
- remove payload-only normal-runtime ACK authorization;
- preserve existing ACK behavior only in explicit fresh-approval, recovery, hot-rejoin or ordered-resume contexts;
- stable retained known 085F becomes capture-only / NO_ACK;
- unknown 085F payload remains fail-closed STOP;
- EXP418 0870 token creation remains after actual all-zero 085F ACK only.

**Safety:** no new transmitted payload is introduced. Target controller publication is slave `0x0F`, FC16, start `0x085F`, count 5. The experiment only withholds an existing standard address/count ACK when context ownership is absent.

**Offline validation:**
- YAML parse PASS;
- undefined `id()` refs: 0;
- UART TX sites remain 66 and ordered expressions are identical;
- existing protocol literals unchanged;
- supplied EXP418 retained-runtime trace contains zero `085F/count5`, therefore predicts no behavior difference on that trace.

**Status:** **PREPARED / NOT RUN**. ESPHome compile not claimed.

---

# 2026-10-05 — EXP418 live result

## EXP418 — COMPLETE / POSITIVE — 0870 ACK ownership hardening

**Hypothesis:** normal-runtime `0870/count17` ACK permission is session-context-owned rather than page-shape-owned.

**Baseline:** EXP417 COMPLETE / POSITIVE.

**Controlled change:**
- remove unconditional `0870/count17` runtime ACK authorization;
- one-shot token is created only after an actually transmitted ACK for all-zero `085F/count5` or `0864/count4`;
- ordinary `0708` preserves the token;
- first normal-runtime `0870` ACK consumes it;
- tokenless normal-runtime `0870` is capture-only / NO_ACK;
- explicit recovery/rejoin contexts remain passthrough and were not redefined.

**Observed local result:**
- supplied log slice spans retained runtime from approximately 2069 s to 2378 s;
- `stage=40` throughout;
- EXP418 status begins at `set=96 consumed=96 noToken=0 bypass=0`;
- 15 new `0864/count4` ACKs each produce `0870_TOKEN_SET source=0864_ACK`;
- 15 new `0870/count17` ACKs each produce `0870_TOKEN_CONSUMED source=0864_ACK`;
- counters reach `set=111 consumed=111`;
- no `EXP418_0870_NO_TOKEN`;
- no `0870_RECOVERY_PASSTHROUGH`;
- no runtime 085F ACK in this slice;
- no semantic write;
- no EXP417 double-valid suppression;
- final heartbeat: `stage=40 ... runtimeFC16ACK=1003 idle0708=555 rt085F=0 unknown16=0 unknown03=0 peer17=0 peer16ack=0 resync=0 drops=0`.

**Result:** **COMPLETE / POSITIVE**.

**Strong conclusion:** replacing page-shape-only 0870 authorization with the one-shot token rule did not regress the observed retained-runtime XTR path, and all observed normal-runtime 0870 publications were owned by an unconsumed token.

**Limitation:** this run does not exercise all-zero 085F token creation or recovery/rejoin bypass, and absence of tokenless 0870 does not prove such a context can never occur.

---

# 2026-10-05 — EXP418 0870 ACK ownership hardening

## EXP418 — PREPARED / NOT RUN

**Hypothesis:** normal-runtime `0870/count17` ACK permission is session-context-owned rather than page-shape-owned.

**Baseline:** EXP417 COMPLETE / POSITIVE, including retained-runtime and bidirectional `03F4` semantic-write regression.

**Controlled change:**
- remove unconditional `0870/count17` runtime ACK authorization;
- set a one-shot token only after an ACK is actually transmitted for all-zero `085F/count5` or `0864/count4`;
- preserve the token across ordinary `0708`;
- first normal-runtime `0870` ACK consumes the token;
- tokenless normal-runtime `0870` is capture-only / NO_ACK;
- existing explicit recovery/rejoin contexts are passthrough so this experiment does not redefine recovery behavior.

**Offline validation:**
- YAML parse PASS;
- 0 undefined `id()` references;
- UART TX call sites remain 66 and in the same order;
- existing hard-coded protocol frame literals unchanged;
- replay of the supplied EXP417 long run yielded 15 `0870/count17` publications; all 15 were authorized by an unconsumed prior `0864` token and zero would have been withheld.

**Status:** **PREPARED / NOT RUN**. ESPHome compile not claimed; CLI unavailable in the preparation environment.

---

# 2026-10-05 — EXP417 additional live write regression

## EXP417 — COMPLETE / POSITIVE — strengthened

A longer retained-runtime run exercised the production `03E8` writer while EXP417 parser hardening was active.

Observed sequence 1:
- fresh current `03E8/count14` cache;
- selector transaction for `03F4`;
- desired full-page response with exactly one changed word, `22 -> 23`;
- controller FC16 `03E8/count14` republish with `03F4=23`;
- exact transaction confirmation, no extra delta words.

Observed sequence 2:
- fresh current-page refresh;
- selector transaction for `03F4`;
- desired full-page response with exactly one changed word, `23 -> 22`;
- controller FC16 `03E8/count14` republish with `03F4=22`;
- exact transaction confirmation, no extra delta words.

Final supplied heartbeat remained `stage=40` with two confirmed writes and clean integrity counters:
`unknown16=0 unknown03=0 peer17=0 peer16ack=0 resync=0 drops=0`.

The EXP417 FC03 double-valid suppression counter stayed at zero over the supplied ~10 minute observation.

**Interpretation:** the parser hardening preserves the locally proven semantic write path. No naturally occurring double-valid frame was observed.

---

# 2026-10-05 — EXP411–416 validation track

## EXP416 — COMPLETE / POSITIVE — structural cleanup pass 2

**Baseline:** EXP415 COMPLETE / POSITIVE.

**Controlled change:** removed six additional state fields proven by static audit to be write-only. No parser rule, ACK policy, selector, frame, CRC, timing, guard, recovery path, semantic transaction or production control was intentionally changed.

**Observed:** retained `stage=40`, normal production synchronization, normal runtime ACKs, clean integrity counters throughout the supplied run, and no semantic write.

**Result:** **COMPLETE / POSITIVE**.

## EXP415 — COMPLETE / POSITIVE — structural cleanup pass 1

**Baseline:** EXP414 retained-runtime build.

**Controlled change:** removed twelve state fields proven by static audit to be dead. Ordered UART write sites, hard-coded frame sequence and executable behaviour outside those removals were preserved.

**Observed:** retained `stage=40`, startup/current synchronization for `042E`, `0442`, `0546`, automatic `03E8` synchronization, normal runtime ACKs and clean integrity counters.

**Result:** **COMPLETE / POSITIVE**.

## EXP414 — RUNNING / PARTIAL — passive natural 0532 observer

Capture-only observer for natural `FC16 0532/count18`. No natural page was observed in the supplied retained-runtime logs. No selector, desired page or setting value is transmitted by EXP414 itself.

## EXP413 — COMPLETE / INCONCLUSIVE — current-only 0532 request

One bounded current-only mailbox request was transmitted during healthy retained runtime. No `0532/count18` followed inside the 15 s discrimination window; runtime integrity stayed clean.

Conclusion: that current request alone is not proven sufficient to force `0532` during retained runtime.

## EXP412 — PREPARED / NOT RUN — 043C UI correlation

Manual UI correlation remains unrun because physical access is unavailable.

## EXP411 — COMPLETE / INCONCLUSIVE — native approval implementation

A native approval implementation derived from Thermia Connect firmware was prepared and independently validated against genuine traffic evidence. The local retained-runtime session produced no fresh controller challenge, so the implementation was not exercised live.

**Confidentiality:** security-sensitive approval parameters, capture fixtures and working implementation details are intentionally omitted from this repository.

**Positive side findings:** local `0867=242 -> 2.4.2`; local `043C=0000` baseline; no observed regression in retained runtime.

---

# 2026-10-04 — LIVE CALENDAR WRITE EXPERIMENTS EXP399..405

## EXP405 — PREPARED / NOT RUN — inactive slot0 two-word time-window write

**Hypothesis:** with F1 slot0 validity clear, one coherent 055A desired-page transaction can mutate both start and stop minute while preserving the window duration.

**Baseline:** EXP404 COMPLETE / POSITIVE.

**Controlled change:** fresh F1 baseline, require `05BA bit0=0`, then change only:
- `055B` / slot0 word1 / start minute: original +1
- `0560` / slot0 word6 / stop minute: original +1

Both originals must be <=58. No wrap is allowed. All other 31 words remain unchanged. Automatic exact rollback is mandatory.

**Status:** PREPARED / NOT RUN. No result has been supplied yet.

## EXP404 — COMPLETE / POSITIVE — F1 slot0 validity metadata write + rollback

**Hypothesis:** `05BA bit0` can be written through the proven 059C desired-page path and then restored.

**Controlled change from EXP403:** EXP403 was zero-delta. EXP404 changed exactly one word in the fresh 059C page: word index30 / address `05BA`, bit0 `0 -> 1`.

**Observed:**
- fresh CURRENT `059C/count33` acquired with `W2 bit3`;
- baseline `05BA=0000`;
- target `05BA=0001`;
- proven desired selector `W0 bit3 + W2 bit3` sent;
- controller pulled `FC03 059C/count33`;
- one 33-word response sent with only 05BA changed;
- controller republished `FC16 059C/count33` with `05BA=0001`;
- confirmation reported `deltaWords=1`, `unexpectedDelta=0`;
- passive calendar decoder independently observed `CAL_F1_METADATA0_CHANGE old=0000 new=0001 setBits=0001`;
- rollback selector sent;
- original 059C image returned;
- final controller FC16 had `05BA=0000`, `finalDeltaWords=0`.

**Result:** **COMPLETE / POSITIVE**.

**Conclusion:** `05BA bit0` is locally proven writable and rollbackable as F1 slot0 validity metadata.

## EXP403 — COMPLETE / POSITIVE — accelerated 059C desired selector + no-op

**Hypothesis A:** `W0 bit3 + W2 bit3` causes `FC03 059C/count33`.

**Hypothesis B:** an exact fresh 059C no-op image is accepted as a desired response.

**Observed:**
- fresh 059C acquired first via proven W2 bit3;
- candidate selector `W0=0008,W2=0008` sent;
- controller requested `FC03 059C/count33` about 78 ms later;
- exact 33-word cached page returned once;
- exact `FC16 059C/count33` observed with `deltaWords=0`;
- no FC03 retry in the discrimination window.

**Result:** **COMPLETE / POSITIVE**.

**Conclusion:** desired selector and no-op response acceptance for 059C are locally proven.

## EXP402 — COMPLETE / POSITIVE — isolate CURRENT 059C

**Hypothesis:** `W2 bit3` alone selects current/config page `059C/count33`.

**Controlled change:** isolate W2=0008 from EXP398 combined W2=000E.

**Observed:** `W2=0008` caused controller `FC16 059C/count33` in about 176 ms.

**Result:** **COMPLETE / POSITIVE**.

**Conclusion:** `W2 bit3 -> CURRENT 059C/count33` is locally proven.

## EXP401 — COMPLETE / POSITIVE — first semantic calendar-content write

**Hypothesis:** an exact 055A page image with one intended calendar-word mutation is accepted.

**Controlled change from EXP400:** mutate only `055B` / slot0 word1 / start minute by +1 while `05BA bit0=0`.

**Observed:**
- fresh F1 baseline; slot0 invalid;
- start minute `0 -> 1`;
- full 055A desired response transmitted;
- controller republished exact one-word delta at `055B`;
- `deltaWords=1`, `unexpectedDelta=0`;
- passive decoder saw slot0 start time become 00:01;
- automatic rollback restored the exact original 055A image.

**Result:** **COMPLETE / POSITIVE**.

**Conclusion:** semantic calendar content is locally writable through the native desired-page mechanism.

## EXP400 — COMPLETE / POSITIVE — exact 055A no-op desired response

**Hypothesis:** after the proven F1 desired selector, returning a byte-for-byte clone of fresh `055A/count33` is accepted.

**Observed:**
- candidate selector already proven by EXP399;
- controller `FC03 055A/count33`;
- one exact 33-word response, `deltaWords=0`;
- controller subsequently published exact `FC16 055A/count33`;
- no FC03 retry over the discrimination quiet window.

**Result:** **COMPLETE / POSITIVE**.

**Conclusion:** the 055A desired response stage is locally accepted.

## EXP399 — COMPLETE / POSITIVE — high-half F1 desired selector

**Hypothesis:** `W0 bit1 + W2 bit1` is the desired selector pair for page 055A.

**Observed:**
- fresh F1 current baseline acquired;
- selector `W0=0002,W2=0002` sent;
- controller requested `FC03 055A/count33` about 78 ms later;
- response deliberately withheld;
- controller repeated FC03 055A;
- generic unexpected-FC03 safety stop ended runtime.

**Result:** **COMPLETE / POSITIVE** for selector identification.

**Operational note:** the experiment caused session loss/alarm behavior, but a later controller restart plus retained-runtime qualification restored normal runtime without R1 or broad bitmap. This did not solve challenge-response.

---

# 2026-10-04 — OFFLINE EXPERIMENTS PROTO-OFFLINE-61..64

These are offline analyses only. They do **not** advance EXP388 and did not transmit to the heat pump.

## PROTO-OFFLINE-64 — COMPLETE / POSITIVE — production-core reduction / cleanup map

**Hypothesis:** v4.1 can be separated into proven production core, reusable generic machinery, historical experiment scaffolding and dead state without changing behavior.

**Controlled change:** static source inventory/classification only.

**Result:** 28 components classified. Strong cleanup candidates include old stalled-export resume scaffolding, EXP383 TEST controls, boot-observation fields, legacy request/pending state and several unused hot-rejoin fields. Bootstrap ACK blocks and the four semantic engines are later table/schema-driven merge candidates. Current recovery and ACK behavior remains unchanged for EXP388 discipline.

## PROTO-OFFLINE-63 — COMPLETE / POSITIVE FOR RESYNC ROBUSTNESS WITH PARSER AMBIGUITY

**Hypothesis:** source-faithful parser fuzzing should reject malformed/noisy traffic without synthesizing an unintended semantic request.

**Controlled change:** offline stream-assembler transcription/fuzz only.

**Result:** 60,000 broad fuzz cases plus 100,000 targeted non-semantic controls. Targeted controls produced 0 accidental semantic-request outputs. Deterministic constructions prove that a valid longer FC03 response can contain an 8-byte CRC-valid prefix that the current shortest-first parser emits as an exact semantic request; examples were found for 0546/count20, 042E/count15, and 0442/count13.

**Interpretation:** real parser-level defensive gap; no genuine Thermia frame is currently known to trigger it.

## PROTO-OFFLINE-62 — COMPLETE / POSITIVE — source-transcribed host decision engine

**Hypothesis:** important v4.1 authorization/recovery logic can be executed host-side and reproduce current regression expectations.

**Controlled change:** host-side decision model only.

**Result:** **4630/4630 checks PASS**, covering golden regression, representative fault cases, semantic selector/page guards, state7 delayed re-arm, all 4,608 EXP388 recovery-state combinations, and reachability safety.

**Limitation:** source transcription is not compiled ESPHome execution.

## PROTO-OFFLINE-61 — COMPLETE / POSITIVE WITH THREE KNOWN ACK-POLICY DEVIATIONS

**Hypothesis:** every explicit Write Beta v4.1 TX route should be represented in the PROTO60 formal model.

**Controlled change:** static model-to-code conformance audit only.

**Result:** **58/58 UART TX sites accounted for**: 2 approval responses, 32 ordered bootstrap ACKs, 1 historical 04A6 resume ACK, 1 generic runtime FC16 ACK builder, 18 mailbox responses, and 4 semantic full-page FC03 responses. No unmodeled semantic TX class was found. The remaining deviations are the known broader source permissions for 085F, 0870, and generic known-config ACKs.

---

# 2026-10-04 — OFFLINE EXPERIMENTS PROTO-OFFLINE-45..60

These are offline analyses only. They do **not** advance EXP388 and did not transmit to the heat pump.

## PROTO-OFFLINE-60 — COMPLETE / POSITIVE — formal protocol/spec package
**Hypothesis:** encode accumulated protocol knowledge as one machine-readable deny-by-default contract.  
**Controlled change:** model/documentation tooling only.  
**Result:** protocol model v1 + schema + decision table + executable validator. **57/57 checks PASS**.

## PROTO-OFFLINE-59 — COMPLETE / POSITIVE — local 0870 context classifier
**Hypothesis:** XTR-only history can yield the smallest normal-runtime 0870 qualifier.  
**Result:** mandatory 0864 is locally disproven. Best-supported candidate is a one-shot session-scoped 0870 ownership token from qualified all-zero 085F ACK OR qualified 0864 ACK; optional known 0708 may intervene; first 0870 ACK consumes it. Recovery/rejoin qualifier remains OPEN.

## PROTO-OFFLINE-58 — COMPLETE / POSITIVE — shadow-patch regression
**Result:** sole-owner guard blocks **604/604** synthetic PROTO53 conflict cases and zero modeled reachable normal paths. `qualified normal runtime OR explicit recovery/rejoin` classifies the genuine 0870 corpus exactly: **TP=64, FP=0, TN=31, FN=0**. Golden regression remains PASS.

## PROTO-OFFLINE-57 — COMPLETE / POSITIVE — semantic-state reachability
**Controlled change:** forward reachability from valid normal/recovery roots with explicit EXP387 delayed-rearm substate.  
**Result:** **115 reachable variants; 0 multi-owner states; 0 reachable PROTO53 conflict projections; 0 unsafe semantic pre-events.** No demonstrated double-semantic-TX bug.

## PROTO-OFFLINE-56 — COMPLETE / POSITIVE — XTR-only ACK context
**Result:** both known 085F payload forms are locally ACK-proven in qualified contexts. Direct 0870 without prior 0864 is locally proven; qualified 0870 ACK advances valid runtime. Bootstrap/refresh/confirmation config ownership is locally proven; autonomous runtime 03E8 also exists. 0834 remains without local ACK proof.

## PROTO-OFFLINE-55 — COMPLETE / POSITIVE — differential hardening simulation
**Result:** recent answered 0708 <=3 s for 0870 gives TP=63, FP=0, TN=31, FN=1. Simple 085F/config hardening over-blocks genuine behavior. 0870 is the cleanest first local ACK-hardening target.

## PROTO-OFFLINE-54 — COMPLETE / POSITIVE — golden trace regression
**Result:** eight fixtures converted to deterministic regression; **72/72 exact assertions PASS**.

## PROTO-OFFLINE-53 — COMPLETE / POSITIVE WITH DEFENSIVE-INVARIANT DEBT IDENTIFIED
**Result:** 4,608 Cartesian state tuples / 64,512 decision rows expose impossible mixed-owner combinations. Later PROTO57 proves those conflict states unreachable under current modeled transitions.

## PROTO-OFFLINE-52 — COMPLETE / INCONCLUSIVE FOR BINARY RECOVERY; POSITIVE FOR TARGET REFINEMENT
**Result:** no binary recovered. Current user-app target is MyThermia / `se.thermia.online2`; installer/service target remains `com.thermia.onsite`.

## PROTO-OFFLINE-51 — COMPLETE / POSITIVE STRUCTURAL RECONFIRMATION
**Result:** ATEC calendar function words 0..391 equal legacy reference; only tail 06E2 differs. No new weekday subset or calendar desired pull; generalized calendar writing remains unauthorized.

## PROTO-OFFLINE-50 — COMPLETE / POSITIVE FOR HISTORY LIFECYCLE; NEGATIVE FOR RAW-ID SEMANTICS
**Result:** 0884 pages can remain byte-identical for minutes and are ordered newest-to-oldest. Raw IDs and insertion/rollover mechanics remain OPEN.

## PROTO-OFFLINE-49 — COMPLETE / POSITIVE AS PRIORITIZATION ARTIFACT; NO NEW SELECTOR PROOF
**Result:** no new selector promoted. Ranking is planning-only; unproven bits remain DENY-BY-DEFAULT.

## PROTO-OFFLINE-48 — COMPLETE / NEGATIVE FOR NEW SEMANTIC PROMOTIONS
**Result:** unresolved settings fields show no useful within-capture edges. Five 087D +1 edges reconfirm compressor-runtime accumulation; no new semantic label.

## PROTO-OFFLINE-47 — COMPLETE / POSITIVE — cross-profile ABI alignment
**Result:** XTR aligns structurally with modern Eco5 at 03E8/0410/0492/051E; local 03F3=1 and 03F5=2 follow the modern representation. Semantics remain OPEN.

## PROTO-OFFLINE-46 — COMPLETE / POSITIVE WITH THREE BROAD ACK SURFACES CONFIRMED
**Result:** 29 valid-CRC synthetic scenarios confirm semantic write machinery is strongly fail-closed. Broad ACK surfaces remain known 085F, 0870 and generic known-config allowlists. EXP388 cancellation branches remain live-unconfirmed.

## PROTO-OFFLINE-45 — COMPLETE / POSITIVE WITH MODEL REFINEMENTS
**Result:** seven genuine captures + one local passive XTR trace replay successfully. Approval/bootstrap/runtime/desired/recovery are machine-reproducible; approval and retained service/config can overlap, so session/work state is orthogonal rather than one strict enum.

---

# 2026-10-03 — PROTO-OFFLINE-40..44 reconciliation

**Live XTR state remains unchanged:** EXP387 COMPLETE / POSITIVE; EXP388 RUNNING / PARTIAL; EXP383 PREPARED / NOT RUN.  
**Controlled change for all five tracks:** offline analysis only; no bus TX, YAML behavior change, compile/flash, reboot or setting write.

## PROTO-OFFLINE-44 — full protocol state-machine regression — COMPLETE / POSITIVE WITH HARDENING REQUIREMENTS

- seven-capture state graph reduced to APPROVAL -> optional WAIT_PAGE_SERVICE -> BOOTSTRAP -> POST_BOOT_SERVICE -> NORMAL_RUNTIME;
- runtime branches separated into CONFIG_REFRESH, SERVICE_REFRESH, DESIRED_PULL and RECOVERY_REJOIN;
- Write Beta v4.1 major architecture matches the genuine model and no new uncontrolled semantic-write route was found;
- future hardening required for `085F`, `0870` and generic runtime config-page ACK permission;
- `0834/count18` remains intentionally capture-only because local XTR ACK safety is not proven despite 63/64 genuine ACKs.

## PROTO-OFFLINE-43 — runtime ACK-context reconstruction — COMPLETE / POSITIVE

- `085F/count5`: 331 publications, 20 ACKed, 311 unACKed; payload recognition is not ACK permission;
- `0870/count17`: 95 publications, 64 ACKed, 31 unACKed; all 31 unACKed occur in one legacy reconnect retry window;
- one later `0870` ACK is followed about 1.37 s later by `0708` rejoin/export state;
- known config-page shape is not generic permission: `03E8` 220/18 ACKed, `04A6` 586/19, `04BA` 44/17;
- durable conclusion: protocol state must own ACK permission.

## PROTO-OFFLINE-42 — desired-page cache freshness/lifetime — COMPLETE / POSITIVE

- fully bracketed genuine Eco5 desired pulls reused last bus-visible same-page FC16 images aged 67.084, 319.512, 374.586 and 87.609 s;
- ATEC no-op `0546` used a 65.425 s-old bus-visible image;
- current genuine lower bound for bus-visible same-page cache reuse is >=374.586 s;
- local XTR freshness guard remains intentionally conservative.

## PROTO-OFFLINE-41 — desired-page no-op vs semantic delta republish — COMPLETE / POSITIVE

- four genuine Eco5 one-word deltas all receive exact FC16 republish in 0.491..0.571 s;
- one genuine ATEC exact no-op `0546/count20` desired image receives no same-page republish over 226.677 s;
- exact republish remains the strongest confirmation for a real delta; missing republish after exact no-op is not automatic failure.

## PROTO-OFFLINE-40 — challenge/response pair reduction — COMPLETE / NEGATIVE for tested simple-transform families

- 164 challenges yielded seven CRC-valid request/response pairs: six Eco5, one ATEC/DCM03;
- fixed XOR/add/sub masks, fixed byte/word permutation+mask families, rotations and simple unkeyed MD5/SHA transforms fail;
- exact response algorithm/key/session dependence remains OPEN.

---

# 2026-10-03 — ATEC-COLDSTART-01 / ATEC-EXP1 supersession / ATEC-EXP2 preparation

**Local XTR live state remains unchanged:** EXP387 COMPLETE / POSITIVE; EXP388 RUNNING / PARTIAL.

## ATEC-COLDSTART-01 — genuine ATEC + classic DCM03 cold start

**Status:** **COMPLETE / POSITIVE** — collaborator capture analysis.  
**Hypothesis:** a capture started before HP power-up with DCM03 already powered/listening will expose the complete native ATEC approval/bootstrap/runtime transition.  
**Controlled change:** offline analysis only; no project device TX, no YAML execution, no XTR reboot/write.

### Observed facts

- first bus frame 26.480 s;
- one exact slave-`0x0F` FC17 challenge at 27.400 s, read `0730/count8`, write `071C/count8`, body `2EE156572B8B84A0BC7A65C72D56185D`;
- classic DCM03 response at 27.429 s, 29 ms later, body `20B8F28A236F28FA0339669E2C6F600D`;
- first `03E8/count13` export at 29.262 s, 1.833 s after response;
- complete 32-page bootstrap `03E8 -> ... -> 06F4`, every page ACKed;
- ATEC-specific count differences include `03E8/13`, `0410/21`, `0492/9`, `051E/9`;
- first `0708` response `0000 0000 0000 0000 07FF 0006`; steady replies use `W4=077F, W5=0006`;
- one genuine desired event: `W0=0001` -> controller `FC03 0546/count20`;
- returned `0546` desired image exactly equals the bootstrap current image and contains `0553=0004`; no later `0546` FC16 republish occurs, so this is selector proof/no-op desired state, not proof of a mode change;
- `0867=0000` here, refining the older `0867=0016` legacy-reference fingerprint.

### Strong conclusions

- classic DCM03 is directly observed answering native ATEC approval;
- ATEC page service can begin almost immediately after approval;
- 32-page bootstrap/page-index architecture is genuine across another generation while counts remain profile-specific;
- `W0 bit0 -> 0546` is now genuine cross-model selector evidence.

---

### PROTO-OFFLINE-39 — experiment evidence / coverage audit — COMPLETE / POSITIVE
- 139 unique numbered experiment IDs catalogued from the canonical log; absent numeric IDs are not treated as lost runs;
- 63 IDs contain complete-result raw/protocol detail; 10 contain explicit user-confirmation wording;
- old EXP92..107/134 status wording is preserved rather than rewritten;
- future live priority: finish EXP388 recovery branches, then runtime ACK-context evidence, then EXP383 candidates if still useful.

### PROTO-OFFLINE-37 — Write Beta v4.1 safety/provenance audit — COMPLETE / POSITIVE WITH SAFETY DEBT
- 58 explicit write_array TX sites reduced to bounded protocol action classes;
- R1/bootstrap/semantic-page write guards remain evidence-backed and fail-closed;
- 085F ACK permission is too payload-driven versus PROTO29 context evidence;
- 0870 ACK and generic runtime config-page ACK classes should become context-aware in a future production revision;
- EXP383 TEST controls remain PREPARED / NOT RUN; no YAML behavior changed and no compile verification claimed.

## ATEC-EXP1 — historical heat-pump write candidate

**Previous status:** PREPARED / NOT RUN.  
**New status:** **SUPERSEDED / NOT RUN**.

Reason:
- never executed;
- used Eco5-derived 26-page refresh geometry and modern counts such as `03E8/count14`;
- left FC17 unanswered, while the new cold start proves ATEC is challenge-gated.

Historical YAML remains for provenance with a superseded/do-not-run header.

---

## ATEC-EXP2 — isolated DCM03 cross-controller challenge compatibility

**Status:** **PREPARED / NOT RUN**.  
**Hypothesis:** a classic DCM03 that answers its captured ATEC challenge on an isolated bench may also generate a valid `0F 17 10 <16 bytes>` response to a foreign Eco8 challenge.

**Exact controlled change:** remove the HP/controller from RS485 and send only bounded known FC17 probes to DCM03. First replay the exact captured ATEC challenge as positive control. Only after control success test the six captured Eco8 challenges.

**Active target:** slave `0x0F`; FC17 read `0730/count8`; write `071C/count8`; bytecount 16.  
**Known current value:** unknown/opaque DCM03 mailbox state.  
**Expected effect:** DCM03 returns `0F 17 10 <16-byte body> <CRC>` within ~200 ms.  
**Plausible unintended effects:** DCM03 internal session/binding state may change; HP effect impossible because HP/controller must be absent.  
**Recovery:** stop TX, power-cycle DCM03, restore isolated bench, rerun control.

**Positive:** control succeeds and at least one Eco8 challenge gets valid response.  
**Negative:** control succeeds but all bounded Eco8 probes are silent/invalid; negative only for tested standalone context.  
**Inconclusive/abort:** control fails, TX unverified, bus not isolated, malformed frame/CRC, DCM reset/error.

No HP semantic write, FC16 page ACK or `0708` emulation belongs to ATEC-EXP2.

---

# 2026-10-03 — PROTO-OFFLINE-22 canonical reconciliation

**Status:** **COMPLETE / POSITIVE** — documentation/database reconciliation only.  
**Controlled change:** no bus TX, YAML change, reboot or setting write.  
**Live state:** EXP387 COMPLETE / POSITIVE; EXP388 RUNNING / PARTIAL.

### EXP387 — delayed `0708` semantic re-arm — COMPLETE / POSITIVE
- delayed semantic re-arm locally confirmed;
- Room Setpoint native semantic write succeeded;
- retained here because PROJECT_STATE and Write Beta v4.1 already carried this authoritative result.

### EXP388 — repeated controller-restart recovery hardening — RUNNING / PARTIAL
- repeated controller-restart recovery succeeded twice without ESP reboot;
- pre-semantic and refresh-only controller-loss cancellation branches remain not independently live-exercised;
- do not mark complete.

### PROTO-OFFLINE-17 — Approval vs sync readiness — COMPLETE / POSITIVE
- approval accepted and native page-service-ready are distinct;
- six first accepted Eco5 `03E8/count14` ACKs fall at 118.478..120.296 s after bus return;
- two early challenge-#3 approvals precede page readiness by ~108.5 s and accumulate 102 unACKed `03E8` requests.

### PROTO-OFFLINE-18 — Sync-readiness discriminator search — COMPLETE / NEGATIVE
- no independent captured recurrent RS485 field predicts readiness before first `03E8` ACK;
- no live experiment changed.

### PROTO-OFFLINE-19 — Mailbox + sync-sequence completion — COMPLETE / POSITIVE
- six successful Eco5 sessions share a fixed 32-page ACK-gated bootstrap through `06F4` before first `0708`;
- later `FFFF/867F` is a 26-page mailbox refresh;
- `047E,0492,04D8,04F6,050A,051E` are bootstrap-only in the current Eco5 corpus;
- no genuine desired-selector proof for `0442` or `0546` was found.

### PROTO-OFFLINE-20 — Register/database/history audit — COMPLETE / POSITIVE
- stale evidence levels and superseded interpretations were identified;
- local XTR `042E/042F` semantics are no longer open;
- historical observations are preserved and current status layered on top.

### PROTO-OFFLINE-21 — Connect/OnSite artifact hunt — COMPLETE / POSITIVE
- official Connect onboarding ties local AP, heat-pump serial input, pairing and protocol packages;
- hardware IDs `206495/355202/357577` recovered;
- no firmware/APK/protocol-package binary recovered.

### PROTO-OFFLINE-22 — Canonical reconciliation — COMPLETE / POSITIVE
- PROTO17..21 and PROTO20 evidence corrections folded into canonical state/findings/register map;
- no historical experiment result rewritten;
- no live experiment advanced.

---

### PROTO-OFFLINE-39 — experiment evidence/coverage audit — COMPLETE / POSITIVE
- 139 unique numeric EXP IDs are present in the canonical log; 249 IDs in 1..388 are absent and are not reconstructed;
- newest-record evidence basis is inventoried separately from historical PREPARED/RESULT duplicate headers;
- EXP373/376 historical partial headers do not override the current top-level live state;
- EXP388 remains the only active live experiment; EXP383 remains PREPARED / NOT RUN;
- future runtime-ACK hardening is recorded as a candidate only, not promoted to a live experiment.

### PROTO-OFFLINE-38 — ABI/profile fingerprint classifier — COMPLETE / POSITIVE
- deterministic feature classifier added using A5/1E backend presence, 03E8 page shape, 0867 fingerprint and W5 profile values;
- 4/4 older genuine references classify LEGACY_DCM_A5;
- 2/2 genuine Eco5 references classify MODERN_1E_ONLINE;
- classifier is explicitly topology/ABI-only and must not infer exact product model.

### PROTO-OFFLINE-37 — Write Beta safety/provenance audit — COMPLETE / POSITIVE
- all current TX route classes mapped to provenance and guard policy;
- no unknown/symmetry-only desired TX route found;
- stale evidence/log labels corrected only; no functional TX logic changed;
- runtime config ACK-by-known-shape remains a future hardening candidate requiring live regression before tightening.

### PROTO-OFFLINE-36 — runtime-field correlation — COMPLETE / POSITIVE
- 07F4 is exactly reduced in 96/96 Eco5 samples: 0 inactive, 4 active/pre-run with zero frequency, 6 active/running with non-zero frequency;
- 0845 is exactly 0x0300 iff 1E:0015=0x0221 in 43/43 samples;
- prior 0865/0866/083B/083C reductions remain consistent;
- no new heating/cooling/DHW/defrost/SG semantic is promoted because labelled transitions are absent.

### PROTO-OFFLINE-35 — runtime-counter scaling — COMPLETE / POSITIVE
- compressor/heating/cooling/hot-water operating counters strongly support raw integer hours;
- mode-counter sums nearly partition total compressor hours in both legacy and Eco5 genuine captures;
- 087B is defrost count; 087C/087D are compressor-runtime minutes per the XTR manual and capture dynamics;
- 0874/0875 semantics remain OPEN.

### PROTO-OFFLINE-34 — 0708 W5 semantic audit — COMPLETE / POSITIVE
- legacy genuine Online/DCM: W5=6 in 37/38 answered polls, W5=7 once during a 7FFF/FFFF rejoin state;
- genuine Eco5: W5=0 in 264/264 answered polls across idle, refresh and desired-state activity;
- EXP344→345 locally proves W5=6 sufficient for persistent DCM icon while W5=0 remains transport/runtime-valid;
- W5 is therefore profile/session metadata with local XTR liveness/UI significance, not a universal connected enum.

### PROTO-OFFLINE-33 — Connect hardware / OEM fingerprint — COMPLETE / POSITIVE
- exact official hardware IDs and interface/power fingerprint consolidated;
- RED declaration includes Wi-Fi and cellular-family standards, but current Thermia connectivity documentation describes Wi-Fi/Ethernet plus an external 3G/4G modem option, so built-in cellular remains OPEN;
- no public OEM, SoC, radio-module or independent regulatory-module identity recovered;
- generic OEM searching is now lower value than obtaining APK/firmware/protocol-package bytes or physical gateway hardware.

### PROTO-OFFLINE-32 — challenge generator deep reduction — COMPLETE / NEGATIVE
- 163 genuine Eco5 request bodies analysed; bit fraction 0.4936 and mean consecutive Hamming distance 64.30/128;
- no fixed/low-cardinality byte, stable ordinal counter or fixed timestamp field was recovered;
- local-XTR structured challenge-byte interpretation is not portable to genuine Eco5;
- further request-body-only algebra is deprioritized in favor of firmware/app acquisition.

### PROTO-OFFLINE-31 — 0884 event-ID archaeology — COMPLETE / NEGATIVE
- public iTec Online profile exposes an empty REG_ERROR_CODES group;
- some raw IDs numerically collide with Genesis alarm addresses, but the mapping fails across the full observed ID domain;
- direct raw-ID == Genesis alarm address is rejected;
- raw A/B remain opaque until labelled local alarm or serializer/firmware evidence exists.

### PROTO-OFFLINE-30 — protocol schema + linter — COMPLETE / POSITIVE
- machine-readable schema created for bootstrap, runtime roles and selector provenance;
- deny-by-default desired-selector policy encoded;
- current Write Beta v4.1 statically checked: 0 hard errors, 0 warnings;
- this is not an ESPHome compile verification.

### PROTO-OFFLINE-29 — runtime scheduler grammar — COMPLETE / POSITIVE
- normal Eco5 runtime cycles mainly through 07D0/07E4 -> 07F8/080C -> 0820/0834 -> 0848/0864 -> 0870;
- median answered-0708 cadence is ~4.24 s in the analysed normal windows;
- W4 behaves as service state/remaining-work metadata during refresh, not an exclusive next-page command;
- 085F is a recurrent overlay (18/329 ACKed overall), so page recognition and ACK permission must remain separate.

### PROTO-OFFLINE-28 — desired-selector provenance — COMPLETE / POSITIVE
- genuine desired selector proof: 03E8/W1b0 and 042E/W1b3;
- local XTR additional desired proof: 0442/W1b4, 0546/W0b0, 055A/W0b1;
- remaining desired bits are structural symmetry only and remain NO-TX by default;
- selector CSV rewritten to carry current-selector evidence and desired-selector evidence separately.

# EXPERIMENT LOG

## 2026-10-03 — canonical reconciliation of recent offline tracks

**Live experiment state is unchanged:** EXP387 remains the last fully completed live experiment; EXP388 remains **RUNNING / PARTIAL**. The entries below are offline analyses only and do not advance any live test.

### PROTO-OFFLINE-16 — Native settings/register schema consolidation — COMPLETE / POSITIVE

**Hypothesis:** Online/native numeric register addresses substantially overlap but semantic labels are profile/model scoped rather than universal.

**Controlled change:** offline reconciliation only; no bus TX, YAML change, reboot or setting write.

**Result:** COMPLETE / POSITIVE.
- public ATEC and iTec profiles disagree at some identical numeric addresses, proving profile drift;
- stable core heating family around `03E8..03F0` retained as strong XTR donor evidence;
- `042E` is profile-dependent; genuine modern Eco5 `1->0` strongly favors iTec Hot Water Status for that profile;
- `0870` strongly identified as compressor operating time;
- previous contiguous `0872..0878` seven-counter hypothesis is superseded;
- `087B/087C/087D` strongly align to the three defrost statistics in the XTR manual.

### PROTO-OFFLINE-15 — DCM03 / Thermia Connect firmware archaeology — COMPLETE / POSITIVE

**Hypothesis:** the missing HE-to-native serializer can be localized by following real DCM03/Connect hardware and update paths.

**Controlled change:** offline external/document/firmware archaeology only.

**Result:** COMPLETE / POSITIVE for target localization; no firmware image recovered.
- DHP-AQ/Atec lineage places DCM03 directly on the pump communication path, making DCM03 the strongest old-generation serializer target;
- current Thermia Connect directly replaces the old DCM-side path and officially supports iTec XTR;
- Connect commissioning/update documentation references pairing and protocol packages;
- no DCM03/Connect firmware binary, manifest or protocol package was recovered.

### PROTO-OFFLINE-14 — Alarm/status/service-data mapping — COMPLETE / POSITIVE

**Hypothesis:** timestamped history is a separate native service layer from current status/alarm state.

**Controlled change:** offline comparison of genuine legacy/Eco5 Online traffic, local XTR stage-40 traffic, manual and firmware semantics.

**Result:** COMPLETE / POSITIVE.
- legacy `0884/count60` = 10 × 6-word timestamped records;
- genuine Eco5 and local XTR use 8 × 7-word records + 4-word trailer;
- local XTR confirms rolling/newest-first timestamped history;
- raw codes remain unmapped; direct XTR E-code interpretation is not justified;
- `085F/count5` remains semantically OPEN.

### PROTO-OFFLINE-13 — Cross-topology runtime normalisation — COMPLETE / POSITIVE

**Hypothesis:** `0x0F` runtime pages are a logical ABI fed by topology-specific physical sources.

**Controlled change:** offline comparison of legacy Online/DCM and modern Eco5+Online capture families.

**Result:** COMPLETE / POSITIVE.
- stable runtime page shapes survive topology change;
- source substitution proven for fields such as `07D1` and `07E4`;
- `0820` is a concrete legacy-A5 vs modern-`0x1E` adapter boundary;
- `0858..085E` is cross-topology clock/date with Monday=0 weekday;
- page envelope portability does not imply byte-identical payload portability.

### CAL-OFFLINE-01 — Calendar final offline closure — COMPLETE / POSITIVE

**Previous status:** RUNNING / PARTIAL.

**Controlled change:** no device action; integrate all existing calendar evidence with the reconstructed `0708` scheduler and exhaustively check for calendar desired-state pulls.

**Result:** COMPLETE / POSITIVE for offline reconstruction scope.
- four 98-word logical function blocks + 4-word tail;
- each function = 8 × 12-word schedule records + two metadata words;
- metadata0 strongly supported as slot-validity bitmap;
- F1 locally maps to WW_GEBLOKKEERD;
- no nonzero W0 and no FC03 desired read of any calendar transport page in the existing genuine corpus;
- calendar write semantics remain OPEN and are not promoted.

### PROTO-OFFLINE-10 — Desired-state command reconstruction — COMPLETE / POSITIVE

**Hypothesis:** native Online commands are full-page read/modify/return transactions.

**Controlled change:** offline-only reconstruction of all six nonzero-W1 command pulls.

**Result:** COMPLETE / POSITIVE.
- 4/4 fully bracketed Eco5 commands differ from prior controller page in exactly one word;
- 4/4 controller FC16 result pages exactly equal the DCM desired page;
- `03F4` performs reversible room-setpoint changes with independent downstream mirror confirmation;
- full-page cache + one-word mutation is the evidence-backed emulator pattern.

### PROTO-OFFLINE-09 — 0708 scheduler state machine — COMPLETE / POSITIVE

**Hypothesis:** `0708/count6` is a page scheduler rather than opaque session data.

**Controlled change:** offline correlation across the six genuine Online/DCM captures.

**Result:** COMPLETE / POSITIVE.
- `W2/W3` proven as 32-page FC16 state-upload bitmap;
- `W1 bit0 -> FC03 03E8`, `W1 bit3 -> FC03 042E`;
- `W4` strongly supported as runtime/service-page bitmap;
- `W0` remains an unobserved high-half desired-state hypothesis;
- `W5` remains implementation/profile/session metadata.

### PROTO-OFFLINE-08 — Unresolved runtime-field reduction — COMPLETE / POSITIVE

Offline reduction narrowed the dynamic `0834/0864/0870` fields. Later PROTO-OFFLINE-16 supersedes the earlier contiguous operating-time-counter interpretation; historical observations remain valid.

### PROTO-OFFLINE-07 — Firmware semantic/identity mining — COMPLETE / POSITIVE

Link CC 2.7.42 contains HE heat-pump identity/binding and semantic parameter logic but not the final Thermia-native `0x0F` serializer. Firmware-derived HE identities are not native-write payloads.

### PROTO-OFFLINE-06 — Automated runtime source correlation — COMPLETE / POSITIVE

Topology-aware correlation proves source-normalized fields including `07D1` return-line temperature and `07E4` average outdoor temperature.

### PROTO-OFFLINE-05 — Runtime export family — COMPLETE / POSITIVE

Recurring native Online/DCM runtime family established from `07D0` through `0870`, with repeated full rings in genuine Eco5 traffic.

### PROTO-OFFLINE-04 — 06F4 context bridge — COMPLETE / POSITIVE

Exact structural mirrors:
`06F4..06F8 = A80C..A810`; `0701 = AFDC`.

### PROTO-OFFLINE-03 — Page-shape provenance — COMPLETE / POSITIVE

Corrects the four Sep24/25 reference captures to genuine Online/DCM provenance. Short-vs-extended page forms are cross-system/profile variation, not proven local-XTR temporal drift.

### PROTO-OFFLINE-02 — 071C/0730 gate analysis — COMPLETE / POSITIVE

Genuine Online evidence establishes the FC17 response as a strong session-opening gate. Local XTR replay evidence shows a fixed known-good response can be accepted against different request payloads; this does not imply a universal algorithm.

### Numbering note

No completed PROTO-OFFLINE-11 or PROTO-OFFLINE-12 result is recorded. Do not infer them from roadmap numbering.

---

## PROTO-OFFLINE-01 — Native unknown-page correlation — COMPLETE / POSITIVE
**Status: COMPLETE / POSITIVE**  
**Date: 2026-10-02**  
**Track:** offline evidence analysis; no device TX and no numbered live-XTR experiment advancement.

### Hypothesis

Existing local XTR logs, genuine iTec Eco5 + Thermia Online captures and the cross-model register table can materially narrow `04A6/count13`, `0424` within `0410/count22`, and `06F4/count19`.

### Controlled change

None. Existing captures/logs only.

### Observed facts

- later local XTR runtime SG transitions correlate with Normal -> `04A6=0000/04A7=0000`, Enhanced -> `0041/0001`, Blocked -> `0042/0001`, and return to Normal -> `0000/0000`;
- genuine Eco5 Online approvals occur with both zero and non-zero `04A6`, excluding it as a simple Online approval flag;
- an older local XTR capture contains a substantially different `04A6/count13` payload regime, preserved as historical/contextual evidence;
- the cross-model contiguous service sequence is locally anchored by confirmed XTR registers `041D` and `041E`, placing `0424` at Returnline Temperature Max Limit;
- across local XTR and the compared genuine Eco5 frames: `06F4=A80C`, `06F5=A80D`, `06F6=A80E`, `06F7=A80F`, `06F8=A810`, and `0701=AFDC`.

### Conclusions

**STRONGLY SUPPORTED / locally correlated:** `04A6/04A7` encode SG/operational-state information in the later local XTR runtime; `0424` = Returnline Temperature Max Limit.

**PROVEN / directly observed structural relation:** the `06F4..06F8` and `0701` mirror relationships above.

**HYPOTHESIS:** low bits of non-zero `04A6` may encode the two SG inputs; unobserved `0x0043` for `(1-1)` is not promoted.

**OPEN / UNKNOWN:** historical alternate `04A6/count13` regime, exact `04B0` semantics, genuine Eco5 `04A6=0044` meaning, and the remaining `06F4/count19` words.

### Result

**COMPLETE / POSITIVE** as an offline evidence-reduction task. No live XTR experiment status changes.

Full report: `Research/protocol reduction/PROTO_OFFLINE_01_UNKNOWN_PAGE_CORRELATION_20261002.md`.

---

## CAL-OFFLINE-01 — Calendar structure reduction — RUNNING / PARTIAL
**Status: RUNNING / PARTIAL**  
**Date: 2026-10-02**  
**Track:** offline calendar sidetrack; does not advance the numbered live XTR experiment sequence.

### Hypothesis

The ordinary Thermia calendar is a logical record layer spanning the native 33-word `0x0F` pages, with four function blocks containing up to eight records each.

### Baseline / evidence

- user-supplied local XTR capture: WW_GEBLOKKEERD 02-10-2026 18:00 -> 19:00;
- historical local XTR page snapshots;
- genuine iTec Eco5 + Thermia Online captures;
- commissioning-manual calendar limits and concrete-drying structure.

### Controlled change

None on the device. Offline reduction only; no ESP TX.

### Observed facts

- the local WW_GEBLOKKEERD edit produces selector `W0=0002/W2=0002`, FC03 `055A/count33`, then an identical controller FC16 republish;
- the first 12 words encode the entered start/stop interval;
- the twelve native pages `055A..06C5`, each count33, cover 396 contiguous registers through `06E5`;
- exact re-alignment gives four 98-word logical blocks plus a four-word tail;
- historical XTR occupancy and genuine Eco5 occupancy align with candidate bitmaps `05BA/061C/067E/06E0`;
- `04D8/count27` contains a 7-word header followed by exactly ten day/temperature pairs, matching the documented concrete-drying shape;
- `06EA/count7` fits second/minute/hour/day/month/year/weekday;
- `(06E3 << 8) | 06E2 == 0870.word0` in the local XTR and both genuine Eco5 datasets checked.

### Strong conclusions

- earlier 99-word-per-function calendar model is **SUPERSEDED**;
- ordinary calendar blocks are **STRONGLY SUPPORTED** as 98 words = 8 × 12-word records + 2 metadata words;
- native 33-word transport pages do not coincide with logical calendar-function boundaries;
- `04D8/count27` is a much stronger concrete-drying candidate than the calendar tail.

### Proven / hypotheses / unknowns

**PROVEN / local:** WW_GEBLOKKEERD edit uses the `055A/count33` desired-page path.  
**STRONGLY SUPPORTED:** 12-word record structure, 98-word logical blocks, occupancy bitmap positions, separate concrete-drying structure, clock block.  
**HYPOTHESIS:** F2=EVU, F3=Silent Mode, F4=Temperature Reduction; mode0=DATE/mode1=DAYS-WEEK; delete may clear a bitmap while leaving stale record contents.  
**OPEN:** live delete encoding, weekday bit order, second metadata words, concrete-drying header0..4, `06E2..06E5` semantics.

### Next / stop criteria

Next calendar work remains passive-only: one controlled non-zero minute in a WW_GEBLOKKEERD DATE entry, observe the slot and candidate bitmap, delete the same entry, continue capture 60–90 s. Unexpected traffic is capture-only. Do not implement an ESP calendar writer yet.

Full analysis: `Research/CALENDAR_STRUCTURE_ANALYSIS_20261002.md`.

---

## ECO-WRITE-01 — iTec Eco mismatched R1 replay acceptance — PREPARED / NOT RUN
**Status: PREPARED / NOT RUN**  
**Date: 2026-10-02**  
**Track:** cross-model iTec Eco sidetrack; does not advance the XTR M EXP-number sequence.  
**Revision:** PREPARED definition refined before first run after combined raw reduction of both genuine Eco5 gateway captures.

### Hypothesis

The target iTec Eco controller accepts a previously captured known-good Eco5 Thermia Online FC17 response even when that response does not correspond to the current live `071C/0730` challenge.

### Baseline

`Read-only/iTec Eco/thermia_itec_eco_waveshare_public_v01.yaml`

Passive Eco compatibility remains the known-safe baseline.

### Genuine Eco5 evidence already established

Across `itec_eco5_gateway_20260926.log` and `itec_eco5_gateway_20260928.log`:

- six successful exact `071C/0730` challenge -> gateway-response events are present;
- every successful response is followed by controller `FC16 03E8/count14`;
- first `03E8` follows the response after 92..482 ms;
- four successful gateway responses occur at challenge #29;
- two successful gateway responses occur at challenge #3;
- all six gateway response bodies differ;
- in two challenge-#3 windows without an immediate `03E8` ACK, the controller emits nine `03E8/count14` frames within the next 10 s and does not advance to `03FC` during that window.

Therefore the native Eco5 approval -> configuration-sync architecture and first page-ACK progression are genuine-capture evidence. The unresolved point is replay tolerance, not the downstream sync shape.

### Exact controlled change

Only one active variable is introduced:

- configure GPIO17 TX;
- require manual Home Assistant arming;
- require >=5 s complete controller-bus silence followed by controller return;
- recognize only the exact `read 0730/count8; write 071C/count8; byte_count16` challenge;
- challenge #1 and #2: capture-only / NO TX;
- challenge #3: transmit exactly one captured known-good Eco5 response;
- perform no further TX.

Hard-coded one-shot response:

`0F17101691A5F3F8E8D58738924416E8E6A3D5E227`

That response came from a different genuine Eco5 challenge/session (#29), so transmitting it on live challenge #3 is an explicit mismatched-replay test.

No FC16 ACK, no `0708` response, no desired-page selector and no settings write are included.

### Why challenge #3

Challenge #3 is not guessed: the genuine Eco5 gateway successfully answered challenge #3 in two captured sessions. The earlier "first challenge" draft was superseded before any run because the raw logs do not show successful native Eco gateway responses at challenge #1.

### Success / negative / inconclusive / abort

**Success:** challenge #3 is reached, the single R1 replay is sent, and controller `0x0F FC16 03E8/count14` follows. EXP01 deliberately does not ACK it.

**Negative:** challenge #3 is reached and R1 is transmitted, but no `03E8/count14` appears within 10 s.

**Inconclusive:** the controller returns but challenge #3 is not reached within 30 s, or no qualified silence -> boot-return sequence occurs within 180 s.

**Abort:** another response-shaped `0x0F FC17` peer or `0x0F FC16` ACK-shaped peer is seen, parser CRC/resync/RX-drop integrity changes after boot return, or the user cancels.

Unexpected traffic is capture-only.

### Safety / recovery

- one R1 maximum per ESP boot;
- DE LOW outside the single guarded response;
- no setting register is modified;
- no FC16 ACK or semantic page mechanism exists in this build;
- plausible unintended effect is a temporary partial Online/DCM session, repeated `03E8` pushes or an Online communication alarm because the expected first page is intentionally left unACKed;
- after the one response the build is passive again;
- conservative rollback is the read-only iTec Eco profile.

### Prepared artifact

`Research/iTec Eco/thermia_itec_eco_waveshare_write_exp01.yaml`

Generated YAML does **not** count as experiment completion. Await a real Eco log/result before preparing the next active stage.

---

## EXP386 — Native DCM session activation/recovery from unqualified stage40
**Status: COMPLETE / POSITIVE**  
**Date: 2026-10-02**

### Hypothesis

The v4.0 DCM activation failures were session-state-machine regressions rather than a failure of the already-proven R1 and ordered native sync. If unqualified stage40 remains passive through guard-mismatched challenges and can re-enter the cold-start path after a real controller restart, the existing guarded R1 + ordered FC16 ACK chain should recover a persistent native DCM session.

### Baseline

- EXP381B — **COMPLETE / POSITIVE** production/UI baseline.
- Existing native session mechanics and page ACK chain already locally established by the preceding write experiments.
- EXP383 semantic candidate controls remain **PREPARED / NOT RUN** and were not exercised by EXP386.

### Exact controlled changes

Only session-state transitions changed:
1. startup bus age >2 s arms the existing stage-1 cold-start wait instead of disarming the engine;
2. >=5 s bus loss in unqualified semantic-idle stage40 re-enters cold-start recovery instead of stopping;
3. exact `071C/0730` challenges outside the proven guard are NO_TX/capture-only and do not stop stage40;
4. that guard-wait behavior applies to every challenge number, not only challenge #1.

No hard-coded TX frame array was changed.

### Safety / transmit scope

- New write register/page: **none**.
- R1 allowed only under known `A80E=0000 / A80F=0005`.
- Guard mismatch: **NO TX**.
- Semantic transaction active during bus loss: fail closed.
- Existing R1 and ordered FC16 ACK frames unchanged.

### Observed facts

- Pre-reboot challenge #2 at `A80E=0008 / A80F=0032` logged `NO_TX KEEP_STAGE40=1`.
- >=5 s complete bus silence produced `BUS_LOSS_TO_COLD_START`.
- First returning valid frame produced `BOOT_RETURN`.
- State guard reached `A80E=0000 / A80F=0005`.
- First exact challenge under that guard transmitted one R1.
- First post-R1 FC16 was exact `03E8/count14` and received the existing address/count ACK.
- Ordered sync continued through `06F4/count19`.
- Persistent stage40 resumed.
- Fresh runtime `085F/count5` FC16 was ACKed.
- A `0708` idle reply was observed.
- Firmware reported `RECOVERY_POSITIVE` and `COMPLETE / POSITIVE / fresh controller session recovered`.
- Parser integrity remained clean: `resync=0`, `drops=0`.

### Strong conclusion

**PROVEN / locally confirmed on this Thermia iTec XTR M:** the current ESP implementation can recover the native DCM-style session after a real controller power-cycle by remaining passive through non-permitted challenges, detecting controller bus loss/return, replaying the already-proven R1 only under the cold-start guard, completing the ordered initial FC16 synchronization and then qualifying persistent runtime with fresh FC16 + `0708` evidence.

### Result

**COMPLETE / POSITIVE**

### New baseline

`Write (Beta)/thermia_itec_xtr_m_waveshare_write_beta_v4_0.yaml`

---

# EXP383 — STRONGLY SUPPORTED candidate controls — PREPARED / NOT RUN

**Date:** 2026-10-01  
**Status:** PREPARED / NOT RUN

## PREPARED

**Baseline:** EXP381B COMPLETE / POSITIVE; EXP382 COMPLETE / POSITIVE offline analysis.

**Hypothesis:** the seven mappings promoted by EXP382 to STRONGLY SUPPORTED can be tested through the already proven native desired-page mechanisms of 042E/count15, 0442/count13 and 0546/count20.

**Exact controlled change:** add functional Configuration controls with `TEST` in every candidate entity name:
- 0430 word2 — Hot Water TOP_UP
- 0444 word2 — Cooling Hysteresis
- 0446 word4 — Cooling Configuration/Type
- 0448 word6 — Cooling STOP threshold
- 044A word8 — MAX_STARTTEMP
- 044B word9 — MIN_STOPTEMP
- 0559 word19 — Link Integration

The existing selectors, session model, page ownership, exact-republish requirement and fail-closed integrity guards are retained.

**Positive criterion per candidate:** controller republishes the same native page with exactly the selected target word changed, `extraDeltaWords=0`, and the physical/UI effect matches the hypothesized field. A protocol-level exact republish without the expected semantic effect is not sufficient to promote the mapping.

**Negative:** controller retains the original selected value with no unrelated page changes.

**Abort/inconclusive:** parser/RX/peer/session fault, timeout, wrong page/count, extra changed words, unexpected semantic effect, or integration/session disruption. No retry.

**Safety:** one candidate at a time; smallest reversible change; 0559 Link Integration last.

**RESULT:** not run.

---

# EXP382 — offline controlled-page gap analysis — COMPLETE / POSITIVE

**Date:** 2026-10-01  
**Status:** COMPLETE / POSITIVE — OFFLINE ONLY

## PREPARED

**Baseline:** EXP381B COMPLETE / POSITIVE.

**Hypothesis:** existing project evidence can reduce unknown words inside already controlled native pages without live TX.

**Controlled change:** none on device. No YAML/protocol transmission was required.

## RESULT

The analysis produced the following evidence upgrades:
- 0430 → Hot Water TOP_UP — STRONGLY SUPPORTED
- 0444 → Cooling Hysteresis — STRONGLY SUPPORTED
- 0446 → Service Cooling Configuration/Type — STRONGLY SUPPORTED
- 0448 → Cooling STOP threshold — STRONGLY SUPPORTED
- 044A → MAX_STARTTEMP — STRONGLY SUPPORTED
- 044B → MIN_STOPTEMP — STRONGLY SUPPORTED
- 0559 → Link Integration — STRONGLY SUPPORTED
- 0447 → Cooling START threshold — HYPOTHESIS only

No candidate was promoted to local XTR proof. Full report: `Research/EXP382_OFFLINE_GAP_ANALYSIS.md`.

---

# EXP381B — production/UI consolidation — COMPLETE / POSITIVE

**Date:** 2026-10-01  
**Status:** COMPLETE / POSITIVE — explicit user confirmation

**Baseline:** EXP380 COMPLETE / POSITIVE.

**Controlled change:** behavior-preserving production cleanup and manual-aligned entity ordering only. No protocol target, selector, page, CRC, timing, ACK or recovery-state change.

**Result:** user reported: “EXP381B run & successful”.

**Conclusion:** EXP381B becomes the locally proven runtime baseline for subsequent work.

---

# EXP381A — initial UI/read-only consolidation — SUPERSEDED / NOT RUN

EXP381A was prepared but superseded by EXP381B before a distinct run. No separate experiment result is inferred.

---

# EXP380 — persistent Operation Mode on 0546/count20 — COMPLETE / POSITIVE

**Status:** COMPLETE / POSITIVE by explicit user confirmation.

The locally exercised 0546 desired-page path successfully controlled `0553` Operation Mode while retaining the same fresh-page → selector → FC03 desired-page → exact FC16 republish architecture. The durable claim is local semantic writeability of `0553`; values not individually exercised are not retroactively promoted.

---

# THERMIA EXPERIMENT LOG

## EXP380 — Operation Mode 0553 on 0546/count20 — PREPARED / NOT RUN

**Status:** PREPARED / NOT RUN.

**Baseline:** EXP379 v2 persistent cooling control architecture and the EXP378 unified desired-state queue/UI.

**Hypothesis:** the proven native full-page desired-state write mechanism can be extended to `0546/count20` and used to change only `0553` / word 13.

**Accepted enum for the planned active test:** 0=Uit, 1=Auto, 2=Compressor, 3=Bijverwarmer, 4=Warmwater. Local XTR panel evidence confirms 1 and 2; 0/3/4 are accepted genuine/cross-model working assumptions by explicit user instruction.

**Planned selector model:** current/PUSH uses W2 bit0 for page 0546; desired/PULL mirrors the high-half page bit in W0 while retaining W2 current context. This is based on the genuine 32-page bitmap reduction and is not yet a local semantic-write result.

**Controlled change:** add only one persistent Configuration `select` for Operation Mode. Preserve existing production/heating/DHW/cooling behavior and the queue/UI semantics.

**Positive criterion:** fresh 0546 source page, controller FC03 pull, one-word desired page at word 13, controller FC16 republish with target and `extraDeltaWords=0`.

**Negative/abort:** stale/wrong page, enum outside 0..4, parser/RX/peer fault, timeout, no adoption or any extra changed word. No retry.

## EXP379 — persistent cooling controls — COMPLETE / POSITIVE

**Status:** COMPLETE / POSITIVE from supplied local XTR M runtime log.

**Baseline:** EXP378 current-refresh + desired-state queue architecture.

**Hypothesis:** mapped fields in native `0442/count13` can be exposed as persistent HA controls and written with the same fresh-page -> desired selector -> controller FC03 -> one-word desired page -> exact FC16 republish flow.

**Observed / locally confirmed:**
- `0442` Cooling Enabled: `0 -> 1`, exact republish, `extraDeltaWords=0`.
- `0443` Desired Cooling Temperature: `17 -> 18`, exact republish, `extraDeltaWords=0`.
- `0445` Cooling Active Above: `25 -> 27 -> 25`, reversible, exact republish, `extraDeltaWords=0`.
- `0449` Cooling Time: `21 -> 20`, exact republish.
- `044C` Cooling Room Sensor: `0 -> 1`, exact republish.
- `044D` Cooling Room Hysteresis Low: raw `10 -> 18 -> 10` = `1.0 -> 1.8 -> 1.0 °C`.
- `044E` Cooling Room Hysteresis High: raw `10 -> 17 -> 10` = `1.0 -> 1.7 -> 1.0 °C`.

**Guard confirmation:** with Heating Stop 22 °C, `Cooling Active Above` dynamically required at least 25 °C. Requests for 24 °C were blocked locally with `NO_TX=1` and the authoritative value restored.

**UI correction:** Low/High room hysteresis limits are `0.5..5.0 °C`, step `0.1 °C`, raw `5..50`.

**Conclusion:** every cooling field exposed by EXP379 v2 is PROVEN / locally confirmed writable on this XTR M.

## EXP378 — 042E current refresh + unified desired queue/UI — COMPLETE / POSITIVE

**Status:** COMPLETE / POSITIVE.

**Hypothesis:** page `042E/count15` can be explicitly refreshed through its current/PUSH bitmap and controlled with the same persistent desired-state UI model as the 03E8 page.

**Observed:**
- W3-only bit3 current-refresh selector locally worked:
  `0F030C0000000000000008000000067CB7`.
- Desired selector with W1/W3 bit3:
  `0F030C0000000800000008000000061B77`.
- Rapid desired queue semantics retained the newest requested UI value while queued/in-flight and restored controller authority on completion/failure.
- `0433` Opstart HT was confirmed reversible `5 -> 7 -> 5`.

**Conclusion:** W3 bit3 is locally confirmed for current refresh of 042E, and the persistent desired-state queue/UI model works on this page.

## EXP377 — first semantic write on 042E/count15 — COMPLETE / POSITIVE

**Status:** COMPLETE / POSITIVE.

**Hypothesis:** the native desired-page mechanism can write a one-word change on the 042E page.

**Controlled target:** `042F` SWW Mode, locally observed original 1.

**Observed:** full native transaction changed `042F: 1 -> 0`; controller republished the exact target with `extraDeltaWords=0`. The Thermia panel reflected Comfort.

**Conclusion:** page 042E semantic writeability and the selector path are locally proven.

## EXP376 — broader native-page mapper — RUNNING / PARTIAL

**Status:** RUNNING / PARTIAL; mapper work was paused after useful mappings were recovered.

**Locally confirmed mappings/results:**
- `041D` SWW Start Temperature: controlled `48 -> 47`.
- `041E` Warm Water Time: controlled `30 -> 31`.
- `042E` SWW Enabled: controlled on/off mapping.
- `042F` SWW Mode: Auto/Eco mapping established; later EXP377 proved active write.
- `0433` Opstart HT: controlled and reversible whole-minute behavior.
- `0434` Verwarmingstijd: controlled and reversible.

**Correction retained:** do not label `0431` or `0432` as Heating START/STOP. Their values in known 042E pages do not match that interpretation. They remain UNKNOWN.

**Open candidate:** `0430` remains a hypothesis for Extra Hot Water / Top-up. No local toggle correlation has yet confirmed it.

---

## EXP375B — Room Factor 03F0 — COMPLETE / POSITIVE

**Status:** COMPLETE / POSITIVE — user-confirmed.

**Baseline:** final EXP374 v4d serialized write engine.

**Target:** `03F0` Room Factor in native `03E8/count14`.

**Result:** the user explicitly confirmed the planned write/rollback test succeeded. No separate raw log for EXP375B was supplied in this turn, so the durable claim is limited to locally confirmed writeability and observed successful rollback, not additional timing details.

**Conclusion:** `03F0` is PROVEN / locally confirmed writable on this XTR M.

## EXP375A — Heating Minimum 03E9 — COMPLETE / POSITIVE

**Status:** COMPLETE / POSITIVE — user-confirmed.

**Baseline:** final EXP374 v4d serialized write engine.

**Target:** `03E9` Heating Minimum in native `03E8/count14`.

**Result:** the user explicitly confirmed the planned write/rollback test succeeded. This supersedes the earlier untested status caused by a local Min<Max implementation guard; that guard was never Thermia protocol evidence.

**Conclusion:** `03E9` is PROVEN / locally confirmed writable on this XTR M.

## EXP374 — queued serialized multi-setting write engine — COMPLETE / POSITIVE

**Status:** COMPLETE / POSITIVE — final v4d behavior explicitly confirmed by the user.

**Hypothesis:** multiple rapid Home Assistant setting changes can be retained and executed safely as separate native semantic writes.

**Development history retained:**
- initial one-slot queue design was insufficient;
- config controls initially displayed placeholders rather than authoritative values;
- autosync required an explicit refresh trigger;
- one autosync state collided with semantic write state;
- the first dirty-set dispatcher could remove a pending item before a later guard refused it;
- v4c fixed synchronous dispatch/latching;
- v4d changed UI presentation only, preserving active/queued user intent while read sensors stay controller-authoritative.

**Final behavior:** one active transaction; one pending value per supported register; same-register latest value wins; each queued item obtains a fresh `03E8/count14` page; exact one-word republish is required; 2 s settle retained; pending intents remain visible in Configuration instead of temporarily falling back to old controller values.

**Representative user-confirmed result:** rapid Curve Correction requests across `03EB/03EC/03ED` were applied sequentially and the final v4d UI remained stable while the controller caught up. This also locally confirms `03EB` and `03EC` writeability.

**Evidence note:** final v4d result is explicit user confirmation; no standalone final raw log was supplied.

## EXP374 — queued serialized write safety layer — PREPARED / NOT RUN

**Hypothesis:** serialize rapid Home Assistant write requests without overlapping semantic transactions or reusing stale page state.

**Baseline:** EXP370 reusable serialized semantic-write engine; EXP373 partial positive expansion to additional heating settings.

**Controlled change:** scheduling only. One active transaction plus one last-intent-wins pending slot; pending storage causes no TX; queued dispatch waits for the current exact republish, a settle delay and a new fresh `03E8/count14` page. Queue is cleared on negative/inconclusive/abort/parser/RX/peer/timeout conditions. No wire frame, selector, ACK shape or writable address is changed.

**Planned first test:** use only locally confirmed registers, e.g. Heating Stop then Reduced Temperature, and verify two independently closed writes with no overlap.

**Status:** PREPARED / NOT RUN.

## EXP373 — extended heating settings sliders — RUNNING / PARTIAL

**Hypothesis:** the established fresh-page -> selector -> FC03 desired-page -> exact FC16 republish mechanism can safely address additional one-word settings in the `03E8/count14` page.

**Observed / locally confirmed sub-results:**
- `03ED` Curve Correction -5: `0 -> -5 -> 0`; wire value `0xFFFB` for -5; both directions exact republish; `extraDeltaWords=0`.
- `03EE` Heating Stop: `20 -> 22`, later `22 -> 18 -> 22`; exact republish each time; `extraDeltaWords=0`.
- `03EF` Reduced Temperature: `20 -> 22 -> 20`; exact republish both directions; `extraDeltaWords=0`.
- no-op `03EF` request with current==target correctly produced READY with no semantic TX.
- inspected run remained clean: no abort observed; resync/drop/challenge/peer17/peer16ack counters stayed zero.

**Result:** RUNNING / PARTIAL. These individual mappings/write paths are positive, but the full EXP373 target set was not systematically closed in the supplied evidence.

## EXP372 — extended heating sliders design — SUPERSEDED / NOT RUN

Prepared to add `03EB..03F0` sliders with signed int16 handling for curve corrections and reusable serialized writes. Superseded by the audited EXP373 build before a distinct run.

## EXP371 — unrestricted Min/Max follow-up — SUPERSEDED / NOT RUN

Prepared as a distinct follow-up to remove the local +/-1 restriction for Heating Minimum/Maximum. Final conversation-21 reconciliation assigns the observed Maximum write sequence to EXP370, not to a separate EXP371 run.

## EXP370 — reusable multi-setting semantic write engine — COMPLETE / POSITIVE

**Controlled change:** remove the one-shot semantic-write limit while preserving one active transaction at a time, fresh-page provenance and exact republish verification.

**Observed:**
- Heating Curve `35 -> 40 -> 30`, exact one-word controller republish, `extraDeltaWords=0`.
- Heating Maximum `40 -> 41 -> 58 -> 40`, exact controller republish, `extraDeltaWords=0`.
- Room Setpoint `20 -> 22` confirmed through the same reusable engine.
- Heating Minimum target 40 was not transmitted because the local implementation enforced Minimum < Maximum while Maximum was 40.

**Conclusion:** reusable serialized semantic writes are locally proven across multiple settings. The local Min<Max guard is implementation behavior, not Thermia protocol evidence.

## EXP369 — verifier-latch fix — COMPLETE / POSITIVE

**Purpose:** prevent a second Apply from changing the latched register/word while the first semantic transaction is still being verified.

**Observed:** Curve `32 -> 35` confirmed. A later Room Setpoint Apply was refused before changing the active selection. The one-shot experiment limit still prevented a second semantic transaction.

## EXP368 — multi-control verifier test — COMPLETE / INCONCLUSIVE

Curve `35 -> 32` itself completed positively, but a verifier-latch bug allowed a later Apply to overwrite the selected register/word before verification. The semantic result is retained as an observation; the experiment-level verifier objective is inconclusive.

## EXP367 — larger Heating Curve delta — COMPLETE / POSITIVE

Heating Curve `30 -> 35` completed by fresh page -> selector -> desired page -> exact controller republish with only word0 changed and `extraDeltaWords=0`. Existing one-shot logic blocked a second semantic write.

## EXP366 — inverse Heating Curve write — COMPLETE / POSITIVE

Heating Curve `31 -> 30`; exact one-word controller republish, `extraDeltaWords=0`.

## EXP365 — first Heating Curve semantic write — COMPLETE / POSITIVE

Heating Curve `30 -> 31`; fresh `03E8/count14`, selector, controller FC03 desired-page pull, one-word desired page and exact controller republish with `extraDeltaWords=0`.

## EXP364 — hot-rejoin discriminator — COMPLETE / INCONCLUSIVE

The expected `04A6` discriminator did not occur. A fresh-boot/hot-rejoin-style runtime without a new R1/bitmap remained stable for more than 5.5 minutes, but this does not prove the native hot-rejoin mechanism.

## EXP363 — 04A6-to-0708 hypothesis — COMPLETE / NEGATIVE

The specific hypothesis that `04A6` ACK directly yields the expected `0708` transition was not confirmed. However, ACKing exact `04A6/count13` resumed the interleaved export sequence, which is retained as transport evidence.

## EXP362 — bitmap transmission attempt — COMPLETE / INCONCLUSIVE

The intended bitmap was never transmitted, so the target hypothesis was not actually exercised.

## EXP361 — 0708 discriminator follow-up — COMPLETE / NEGATIVE

The expected `0708` event did not occur under the tested condition.

## EXP360 — broad 0708 bitmap exploration — COMPLETE / INCONCLUSIVE

Tested broad bitmap `7FFF/FFFF/0000/0006`. The intended hot-rejoin/page-export discriminator was not cleanly resolved; no protocol fact is promoted solely from this run.

## EXP359 — controller cold-reboot recovery regression — COMPLETE / POSITIVE

Observed sustained bus silence (>5 s), cache invalidation with TX disabled/DE LOW, controller traffic return, guarded fresh-session bootstrap, ordered 32-page sync through `06F4/count19`, stage-40 re-entry and fresh FC16 + `0708` runtime qualification. Recovery count reached 1; parser/RX health remained clean. Runtime `04A6` was not permissively ACKed.

## EXP358 — Write Beta v2.1 production regression — COMPLETE / POSITIVE

v2.1 retained-runtime qualification, stale `03E8` refresh and exact Room Setpoint semantic write remained functional after hardening. The confirmed write was `22 -> 21` with exact republish and `extraDeltaWords=0`; runtime remained healthy with resync/drop counters clean. Conditional fail-closed branches that did not occur in the run remain unexercised rather than assumed proven.


# EXP358 — PREPARED / NOT RUN — Write Beta v2.1 production regression

**Date:** 2026-10-01  
**Status:** PREPARED / NOT RUN

## PREPARED

**Baseline:** EXP357 COMPLETE / POSITIVE for reusable stale-cache refresh + confirmed semantic write; EXP355 COMPLETE / POSITIVE for controller cold-reboot recovery.

**Hypothesis:** the v2.1 production hardening preserves the already-proven retained runtime, reusable refresh and `03F4` write path while removing unsupported/permissive runtime ACK behavior.

**Exact controlled change from the previous production beta:**
- runtime `04A6/count13` becomes capture-only / NO ACK;
- runtime `0834/count18` is never ACKed and fails closed;
- runtime `085F/count5` is ACKed only for the two locally proven payloads: all-zero or third word/register `0861=0x0800`;
- runtime qualification uses one explicit latch, set only after clean locally proven FC16 service plus exact `0708/count6`;
- **Runtime Active** follows that latch;
- write/recovery arming requires the qualified latch;
- no new register/page/bitmap/R1/ACK payload is introduced.

**Transmitted/ACKed frames/registers:** unchanged from the already proven production paths. The semantic target remains page `03E8/count14`, register `03F4`, one controlled integer-degree delta, with W3-bit0 refresh and W1-bit0 desired selector as already proven.

**Positive criteria:**
- retained stage 40 qualifies with clean counters;
- runtime `04A6`, if observed, remains NO_TX while runtime continues;
- no TX is sent to `0834` or unknown `085F` payloads;
- one stale-cache refresh returns fresh controller `FC16 03E8/count14`;
- one `03F4` semantic write completes with exact controller republish and `extraDeltaWords=0`;
- DE returns low after every transmission; parser resync/RX drops/peer responder remain zero.

**Negative criteria:** regression of retained qualification, refresh, selector/pull or exact republish; any ACK to runtime `04A6` or `0834`; or ACKing an unknown `085F` payload.

**Abort criteria:** parser/RX integrity delta, peer FC17/FC16 responder, unexpected runtime FC03/FC16 outside explicit handlers, semantic sequence mismatch, or DE not returning low.

**Recovery procedure:** do not force additional semantic writes after fail-close. Leave the bus passive/DE low and restart or roll back to the previous known-good beta/read-only build if required.

**RESULT:** not run. Do not infer success from YAML generation or GitHub update.

---

# EXP357 — COMPLETE / POSITIVE — reusable stale-cache refresh + confirmed write

**Date:** 2026-10-01  
**Status:** COMPLETE / POSITIVE

## PREPARED

**Baseline:** EXP355 COMPLETE / POSITIVE; EXP353 user-confirmed reusable-refresh follow-up.

**Hypothesis:** a second stale-cache refresh later in the same ESP boot can safely reuse the proven W3-bit0 current-page request and then continue through the established `03F4` semantic write path.

**Controlled change:** remove only the one-refresh-per-ESP-boot experimental budget. No new page, register, selector bit, R1 payload or ACK shape.

## RESULT

- First stale/missing-cache Apply requested a fresh `03E8/count14`; controller response arrived in ~120 ms.
- That fresh page carried `03F4=22`, after which a 22 -> 20 °C write completed and the controller exactly republished the page.
- Later in the same ESP boot, `refreshNo=2` sent the same W3-bit0 refresh-only mailbox response.
- Controller again supplied `FC16 03E8/count14`, logged as `REFRESH_CONFIRMED refreshNo=2`, in ~119 ms.
- The queued 22 -> 24 °C semantic write then completed through W1 selector -> controller FC03 -> one-word-delta desired page -> exact FC16 republish.
- That write logged `WRITE_CONFIRMED writeNo=3 ... observed03F4=24 extraDeltaWords=0`.
- The supplied run later reached five confirmed writes.
- No stale-cache refresh budget refusal occurred; no unknown FC16/FC03, peer responder, parser resync or RX drop issue was observed in the inspected result.

## CONCLUSION

**COMPLETE / POSITIVE.**

Reusable W3-bit0 stale-cache refresh is now **PROVEN / locally confirmed** on this XTR M for multiple refresh cycles in one ESP boot.

---

# EXP356 — SUPERSEDED / NOT RUN — post-recovery soak

EXP356 was prepared but not run. The user chose the targeted EXP357 reusable-refresh test instead. No EXP356 result is inferred.

---

# EXP355 — COMPLETE / POSITIVE — fresh controller-session recovery from retained runtime

**Date:** 2026-09-30  
**Status:** COMPLETE / POSITIVE

## PREPARED

**Baseline:** EXP353 COMPLETE / POSITIVE; implementation based on the EXP352-derived retained/fresh-session state machine.

**Hypothesis:** after a real Thermia-controller power cycle, an ESP that remains powered can recover the Online/DCM path by returning from qualified retained stage 40 to the already known fresh-session bootstrap, without adding any new protocol payload.

**Controlled change:** allow one recovery attempt from healthy stage 40 after >=5 s of bus silence. Reuse the existing fresh-session state guard, exact challenge, one-shot R1 and ordered initial-sync ACK chain unchanged. Invalidate stale semantic cache and reset session-local state before recovery.

**Safety:** no Room Setpoint write during recovery; no new target/page/register; DE low during outage; one R1 maximum; exact A80E/A80F guard; ordered page/count chain only; fail closed on parser/RX integrity change, peer responder, wrong page/count/order or conflicting traffic.

## RESULT

### Pre-recovery retained runtime

The emulator was healthy in stage 40. Known runtime FC16 pages were ACKed and exact `0708/count6` idle service continued. Repeated qualification logs showed `READY_FOR_POWER_CYCLE=1`.

The normal pre-reboot controller-state observation was `A80E=0000 / A80F=000A`.

### Controller outage detection

At `00:51:19.590`:

`RECOVERY_ARMED silenceAge=5166ms runtimeQualified=1 writeState=0 cacheInvalidated=1 TX=0 DE=LOW`

The ESP stayed powered. Runtime counters were reset for the new session and the semantic `03E8` cache was invalidated.

### Bus return and cold-boot guard

At `00:51:29.662`, about 10.072 s after recovery arm, the first valid bus frame returned:

`BOOT_RETURN RAW=1E04001600081267`

At `00:51:30.355`:

`STATE_GUARD A80E=0000 A80F=0005 bootAge=715ms`

The exact `071C/0730` challenge then passed the guard.

### One-shot R1

At `00:51:31.005` exactly one known response was transmitted:

`0F17101691A5F3F8E8D58738924416E8E6A3D5E227`

The R1 latch was closed before transmission; no second R1 was observed.

### First controller page / cache provenance

The first post-R1 config page was exact `FC16 03E8/count14`:

`03E8_CACHE_INITIAL current03F4=22 cacheAge=0ms source=controller_FC16_same_session`

It was ACKed using the established `03E8/count14` address/count ACK.

### Ordered initial sync

All 32 expected page/count stages completed in order:

`03E8/14 -> 03FC/11 -> 0410/22 -> 042E/15 -> 0442/13 -> 0456/12 -> 046A/18 -> 047E/19 -> 0492/11 -> 04A6/13 -> 04BA/22 -> 04D8/27 -> 04F6/14 -> 050A/19 -> 051E/10 -> 0532/18 -> 0546/20 -> 055A/33 -> 057B/33 -> 059C/33 -> 05BD/33 -> 05DE/33 -> 05FF/33 -> 0620/33 -> 0641/33 -> 0662/33 -> 0683/33 -> 06A4/33 -> 06C5/33 -> 06EA/7 -> 06F1/3 -> 06F4/19`

`06F4_ACK_TX_EXECUTED ... ENTER_PERSISTENT_RUNTIME_SERVICE` occurred at `00:52:03.257`, about 32.252 s after the logged R1 execution.

### Fresh runtime qualification after recovery

Immediately after entering stage 40, `FC16 085F/count5` was observed and ACKed. A fresh exact `0708/count6` request was then serviced.

At `00:52:04.887`:

`RECOVERY_POSITIVE success=1 runtimeFC16ACK=1 idle0708=1 r1Used=1 cacheValid=1 writeState=0 DE=LOW`

Total time from recovery arm to positive post-recovery runtime qualification was about 45.297 s.

### Post-recovery observation

A later heartbeat showed:

- `runtimeFC16ACK=22`
- `idle0708=12`
- `rt085F=1`
- `unknown16=0`
- `unknown03=0`
- `peer17=0`
- `peer16ack=0`
- `resync=0`
- `drops=0`
- `DE=LOW`
- `cacheValid=1`
- `cache03F4=22`
- `semanticResponses=0`
- `confirmedWrites=0`

No STOP, ABORT or INCONCLUSIVE event was found after recovery arm.

### State-guard progression

The fresh-session log observed:

`A80E/A80F = 0000/0005 -> 0008/0005 -> 0028/0005 -> 0028/000A`

This progression is observation only; no abstract semantic labels are assigned.

## CONCLUSION

**COMPLETE / POSITIVE.**

A running ESP/DCM emulator recovered from a real Thermia-controller power cycle without ESP reboot. The locally proven recovery chain is:

`qualified retained stage40 -> >=5 s bus silence -> bus return -> A80E=0000/A80F=0005 -> exact 071C/0730 challenge -> one R1 -> full ordered initial-sync ACK chain -> 06F4/count19 -> stage40 -> fresh runtime FC16 + 0708 -> recovered runtime qualified`

No semantic Room Setpoint write was attempted after recovery; the user explicitly chose to skip that follow-up combination test.

---

# EXP356 — PREPARED / NOT RUN — post-recovery runtime soak

**Date:** 2026-09-30  
**Status:** PREPARED / NOT RUN

**Baseline:** EXP355 COMPLETE / POSITIVE.

**Hypothesis:** a session recovered through the proven EXP355 controller cold-reboot path remains stable for an extended post-recovery soak.

**Controlled change:** observation/hardening only. No new register, page, selector, R1 payload, ACK shape or semantic target. No post-recovery Room Setpoint write.

**Positive criteria:** recovered stage-40 runtime continues servicing known FC16 and idle `0708/count6` traffic without unknown FC16/FC03, peer responder, parser resync, RX drop, alarm or loss of DCM presentation.

**Negative/abort:** existing fail-closed runtime/session/parser conditions remain authoritative.

**Result:** not run yet. Await user-supplied overnight log/result.

---

# EXP353 — COMPLETE / POSITIVE — reusable stale-cache refresh follow-up

**Date:** 2026-09-30  
**Status:** COMPLETE / POSITIVE — user-confirmed; detailed raw log/YAML not archived

## PREPARED / intended controlled change

**Baseline:** EXP352 COMPLETE / POSITIVE.

**Hypothesis:** the locally proven W3-bit0 refresh for `03E8` is reusable in one long-lived retained DCM runtime and does not need to remain limited to the EXP352 one-refresh-per-ESP-boot experimental budget.

**Controlled change:** keep the complete EXP352 runtime, refresh, write and republish path unchanged; allow reusable/bounded stale-cache refresh cycles in the same ESP boot. Do not introduce a second writable register/page.

**Safety carried forward:** only `03F4`; whole-degree `10..30 °C`; fresh controller-originated/confirmed `03E8/count14` source page; one outstanding semantic transaction; exact republish with zero extra deltas; fail closed on conflicting/session/parser anomalies.

## RESULT

The user explicitly confirmed: **“EXP353 was successful uitgevoerd.”**

No detailed EXP353 raw log or exact EXP353 YAML is currently archived in the project material. Therefore this entry records the positive completion but does **not** invent the exact number of refresh cycles, timings, native-change sequence or frame-by-frame observations.

**Current use of the result:** the new `Write (Beta)/thermia_itec_xtr_m_waveshare_write_beta_v1.yaml` removes the EXP352 one-refresh-per-boot and eight-semantic-response test budgets while retaining the proven per-transaction safeguards.

---

# EXP352 — COMPLETE / POSITIVE — runtime-independent fresh-page refresh + reusable room-setpoint writes

**Date:** 2026-09-30  
**Status:** COMPLETE / POSITIVE

## PREPARED

**Baseline:** EXP351 COMPLETE / INCONCLUSIVE.

**Hypothesis:** retained stage-40 runtime does not require a hard-coded `03E8` page image. Start/qualify runtime with no write-eligible semantic cache, then obtain a fresh controller page on demand through W3 bit0 before using the proven W1-bit0 desired-page write path.

**Controlled change:** remove EXP351's hard-coded historical handover-equality gate; seed `page_cache_valid=false` at boot; preserve the known-good retained runtime and EXP351 refresh-only state machine.

**Refresh action under test:** on stale/missing cache, next exact `0708/count6` response uses
`W0..W5 = 0000 0000 0000 0001 0000 0006`
(frame `0F030C000000000000000100000006A0B6`), with W1=0 and no semantic page values sent.

**Safety:** no semantic TX before retained runtime qualification; requested/current `03F4` whole-degree 10..30 °C; maximum one refresh request for this experiment; unexpected FC03 03E8 during refresh is not answered; 10 s refresh timeout; one outstanding semantic transaction; exact republish with zero extra deltas; fail closed on session/runtime/parser anomalies.

## RESULT

### Runtime qualification
- Automatic retained stage 40 qualified after ESP OTA.
- No Thermia-controller reboot and no new R1/bootstrap.
- Known runtime FC16 ACK service and exact `0708` idle service with W5=0006 continued.
- User later confirmed no alarm and DCM icon still visible.

### Refresh-only discriminator — POSITIVE
- First Apply: target 25 °C, `cacheValid=0`; log:
  `CACHE_REFRESH_ARM ... requested03F4=25 ... NO_SEMANTIC_TX`.
- On the next exact `0708/count6`, emulator sent:
  `0F030C000000000000000100000006A0B6`
  = `0000,0000,0000,0001,0000,0006`.
- About 120 ms later the controller published:
  `FC16 03E8/count14`, current `03F4=23`.
- Log:
  `REFRESH_CONFIRMED refreshNo=1 current03F4=23 target03F4=25 latency=120ms source=controller_FC16_03E8_14 W1=0000 W3bit0=1 NO_DESIRED_PULL=1 CACHE_FRESH=1`.
- No desired-page FC03 pull preceded this controller refresh.

**Conclusion:** W3 bit0 -> current-page/PUSH refresh for `03E8` is now **PROVEN / locally confirmed** on this XTR M in the tested retained stage-40 context.

### Semantic writes
Six ESP-originated writes were controller-confirmed in the same retained runtime, each with `extraDeltaWords=0`:

1. `23 -> 25`
2. `25 -> 17`
3. `17 -> 23`
4. `23 -> 21`
5. after a native/controller update to 22: `22 -> 21`
6. after a native/controller update to 19: `19 -> 21`

Each exact controller republish became the next-write source.

### Native / physical changes during emulator runtime
- While `writeState=4` with no ESP semantic write pending, controller published a new `FC16 03E8/count14` with `03F4=22`; EXP352 logged `03E8_CACHE_REFRESH current03F4=22 source=runtime_controller_FC16` and promoted it to the live cache.
- Later controller independently published `03F4=19`; user explicitly confirmed **19 °C was set on the Thermia front display**.
- EXP352 promoted 19 to the live cache.
- The next ESP write then correctly used `current03F4=19` as its source and wrote `19 -> 21`.
- The precise physical source of the separate 22 °C native update is not assigned because both room-sensor and Thermia controls were used in this run.

### End-to-end state
- User confirmed **no alarm**.
- DCM icon remained visible.
- Runtime continued after refresh, six writes and native UI changes.

**Conclusion:** the production-relevant architecture is now locally proven for Room Setpoint: persistent retained DCM runtime can operate independently from semantic cache provenance; stale/missing `03E8` can be refreshed on demand through W3 bit0; the proven W1-bit0 desired-page flow can then write `03F4`; controller-originated native changes update the cache and become the source for subsequent HA writes.

---

# EXP351 — COMPLETE / INCONCLUSIVE — refresh hypothesis not reached because emulator activation was gated

**Date:** 2026-09-30  
**Status:** COMPLETE / INCONCLUSIVE

## PREPARED

**Baseline:** EXP350 automatic retained runtime worked, but a later semantic write was blocked by the 300 s `03E8` cache-freshness guard.

**Hypothesis:** when cache is stale, a W3-bit0-only `0708` response with W1=0 and W5=0006 can request a fresh controller-originated `03E8` page before the semantic write.

**Controlled change:** add one bounded refresh-only request and keep the EXP350 write flow otherwise unchanged.

## RESULT

The intended protocol action was never reached.

EXP351 automatic startup still contained a historical handover safety gate that required persisted mapped `03E8` settings to exactly match a hard-coded previous page, including the old 22 °C room-setpoint value. The live system had already moved away from that historical state, so startup returned before `exp351_active=true` / stage 40.

Observed consequence:
- no `RETAINED_RUNTIME_QUALIFIED`;
- EXP351 runtime/cache age sensors remained unset/NaN;
- user reported that the emulator appeared not to trigger and an alarm appeared;
- no W3 refresh-only discriminator was validly tested.

**Conclusion:** no negative conclusion about W3 refresh can be drawn from EXP351. The experiment is **INCONCLUSIVE due to implementation gating**. The historical exact-page prerequisite is superseded as a runtime-liveness requirement; EXP352 separates session/runtime liveness from semantic page provenance.

---

# EXP350 — COMPLETE / INCONCLUSIVE — automatic retained qualification positive; long-interval write blocked by stale cache

**Date:** 2026-09-30  
**Status:** COMPLETE / INCONCLUSIVE

## PREPARED

**Baseline:** EXP349 COMPLETE / POSITIVE.

**Hypothesis:** remove the manual Arm control, automatically qualify the retained stage-40 session after ESP boot/OTA, and then sustain reusable setpoint control over a longer soak.

**Controlled change:** automatic retained qualification replaces manual Arm. Existing setpoint write path, 10..30 °C guard, <=300 s cache freshness, exact republish verification and eight-response semantic budget remain unchanged.

## RESULT

Positive sub-results:
- automatic retained qualification worked;
- persistent stage-40 runtime remained healthy;
- user confirmed no error/alarm and DCM icon still visible.

The long-interval semantic write itself was not performed. On Apply:
- `cacheValid=1`;
- cached `03F4=23`;
- `cacheAge` about 715493 ms;
- implementation correctly refused the write because the page exceeded the 300 s freshness limit.

**Conclusion:** EXP350 does not falsify the write path. It exposed a real production requirement: after long idle periods the emulator must obtain a fresh controller page rather than weaken/remove the cache-freshness safeguard. This led to EXP351/352.

---

# EXP349 — COMPLETE / POSITIVE — reusable guarded room-setpoint writes in one retained session

**Date:** 2026-09-30  
**Status:** COMPLETE / POSITIVE

## PREPARED

**Baseline:** EXP348 COMPLETE / POSITIVE.

**Hypothesis:** the HA-selected `03F4` write is reusable repeatedly in one retained stage-40 Online/DCM session when every successful controller `03E8/count14` republish becomes the source page for the next write.

**Controlled change:** remove EXP348's one-write-plus-rollback terminal behavior and return to READY after each exact controller republish. Maximum semantic budget: 8 per ESP boot. No new register/page/selector/runtime ACK shape.

**Safety:** only `03F4`, range guard 10..30 °C, cache <=300 s, exact `03E8/count14`, one outstanding write, clean retained runtime, exact republish with zero extra page deltas, fail closed on session restart/unknown traffic/parser integrity failure.

## RESULT

Retained session qualified after ESP OTA with no Thermia reboot and no new R1/bootstrap.

### Write 1 — 22 -> 16 °C
- `WRITE_ARM current03F4=22 requested03F4=16 delta=-6 ... semanticBudget=0/8`
- selector:
  `0F030C000000010000000100000006AD26`
- desired page:
  `0F031C0024001400280000000000000014001400020028001E000100100002D29E`
- controller exact republish:
  `0F1003E8000E1C0024001400280000000000000014001400020028001E0001001000023878`
- confirmation:
  `WRITE_CONFIRMED writeNo=1 original03F4=22 target03F4=16 observed03F4=16 extraDeltaWords=0 semanticResponses=1 NEXT_SOURCE=CONTROLLER_REPUBLISH KEEP_W5_0006=1 CONTINUE_RUNTIME=1 READY_AGAIN=1`
- Room Setpoint Mirror and normal Room Setpoint reached 16 °C.

### Write 2 — 16 -> 24 °C
- next write used the confirmed 16 °C controller page as source;
- selector/pull path repeated;
- desired page contained only `03F4=24`;
- controller exact republish:
  `0F1003E8000E1C0024001400280000000000000014001400020028001E000100180002B9BA`
- confirmation:
  `WRITE_CONFIRMED writeNo=2 original03F4=16 target03F4=24 observed03F4=24 extraDeltaWords=0 semanticResponses=2 NEXT_SOURCE=CONTROLLER_REPUBLISH KEEP_W5_0006=1 CONTINUE_RUNTIME=1 READY_AGAIN=1`
- Room Setpoint Mirror reached 24 °C.

### Write 3 — 24 -> 22 °C
- third transaction used the confirmed 24 °C page as source;
- desired page:
  `0F031C0024001400280000000000000014001400020028001E000100160002329F`
- controller exact republish:
  `0F1003E8000E1C0024001400280000000000000014001400020028001E000100160002D879`
- confirmation:
  `WRITE_CONFIRMED writeNo=3 original03F4=24 target03F4=22 observed03F4=22 extraDeltaWords=0 semanticResponses=3 NEXT_SOURCE=CONTROLLER_REPUBLISH KEEP_W5_0006=1 CONTINUE_RUNTIME=1 READY_AGAIN=1`
- status:
  `COMPLETE / POSITIVE / 3+ reusable writes confirmed / runtime continues`
- Room Setpoint Mirror returned to 22 °C.

Throughout the observed sequence, challenge/postTX/unknown16/unknown03/peer17/peer16ack/resync/drops stayed zero in the relevant heartbeats. User confirmed: **worked perfectly**.

**Conclusion:** repeated native semantic writes are locally proven in one retained session. Latest exact controller republish is a valid next-write source for the tested `03F4` path.

---

# EXP348 — COMPLETE / POSITIVE — HA-selected generic 03F4 target

**Date:** 2026-09-30  
**Status:** COMPLETE / POSITIVE

## PREPARED

Baseline EXP347. Replace fixed `current-1` target with a Home Assistant number, while keeping the same retained-session qualification, selector, same-session `03E8/count14` clone, exact controller republish verification and explicit rollback. Local implementation guard: 10..30 °C.

## RESULT

- retained stage-40 runtime qualified with `NO_R1=1 NO_THERMIA_REBOOT=1`;
- current `03F4=22`;
- user-selected target `24`;
- desired page changed exactly one word, `03F4: 22 -> 24`;
- controller exact republish confirmed `observed03F4=24 extraDeltaWords=0`;
- Home Assistant Room Setpoint Mirror and normal Room Setpoint reached 24 °C;
- a second new write was correctly refused because EXP348 intentionally allowed only one write before rollback;
- explicit rollback `24 -> 22` used the same native path;
- controller exact republish confirmed `extraDeltaWords=0`;
- Room Setpoint returned to 22 °C;
- runtime remained clean and user reported the test worked perfectly.

**Conclusion:** arbitrary HA-selected whole-degree target values are locally proven for the tested `03F4` path, not just a hard-coded -1 °C delta. The experiment locally exercised 22 -> 24 -> 22 °C.

---

# EXP347 — COMPLETE / POSITIVE — retained session semantic write without Thermia reboot

**Date:** 2026-09-30  
**Status:** COMPLETE / POSITIVE

## PREPARED

Baseline EXP346. Controlled change: remove the mandatory Thermia-controller reboot/fresh R1 bootstrap. After ESP OTA, seed the last exact confirmed `03E8/count14` page, qualify the already-existing stage-40 runtime using known FC16 service plus one exact `0708` idle response with W5=0006, then permit one guarded write + rollback.

## RESULT

- retained stage-40 session was rejoined after ESP OTA;
- no Thermia-controller reboot and no new R1/bootstrap;
- `RETAINED_RUNTIME_QUALIFIED ... NO_R1=1 NO_THERMIA_REBOOT=1`;
- guarded `03F4` semantic write completed successfully;
- explicit rollback completed successfully;
- user confirmed no error, DCM icon remained visible throughout, and temperature changed/restored correctly.

**Conclusion:** locally proven controller-side Online/DCM session can survive ESP OTA/reboot and remain usable for the native `03F4` semantic path without re-running the Thermia-side bootstrap.

---

# EXP346 — COMPLETE / POSITIVE — guarded 03F4 write + rollback inside persistent DCM runtime

**Date:** 2026-09-30  
**Baseline:** EXP345 — COMPLETE / POSITIVE  
**Status:** **COMPLETE / POSITIVE**

## Hypothesis

The native 03E8 desired-page semantic write mechanism proven in EXP343 can be performed inside the persistent EXP345 stage-40 Online/DCM runtime without dropping the DCM-connected state.

## Controlled change from EXP345

Preserve EXP345 bootstrap, fixed-R1 entry, complete initial sync, stage-40 FC16 whitelist/ACK scheduler and idle 0708 response with W5=0006. Add only:
- same-session full 03E8/count14 cache;
- one guarded manual 03F4 test write;
- one explicit rollback to the latched original 03F4;
- exact republish comparison requiring zero extra page-word deltas.

No other semantic target was introduced.

## RESULT

### Test write

Same-session initial controller page:

`FC16 03E8/count14 ... 03F4=0016` = 22 °C.

Write arm:

`WRITE_ARM current03F4=22 target03F4=21 delta=-1 ... semanticBudget=0/2`

Selector returned on exact 0708 request:

`0F030C000000010000000100000006AD26`

Words:

`0000 0001 0000 0001 0000 0006`

Controller then pulled exact `FC03 03E8/count14`.

Desired page returned:

`0F031C0024001400280000000000000014001400020028001E000100150002C29F`

Only semantic delta: `03F4 0016 -> 0015`.

Controller republished:

`0F1003E8000E1C0024001400280000000000000014001400020028001E0001001500022879`

Verification:

`WRITE_CONFIRMED original03F4=22 target03F4=21 observed03F4=21 extraDeltaWords=0 semanticResponses=1 KEEP_W5_0006=1 CONTINUE_RUNTIME=1`

Home Assistant subsequently showed Room Setpoint Mirror = 21 °C and Room Setpoint = 21 °C. User confirmed DCM icon remained visible and no Online/Link error appeared.

### Rollback

Rollback arm:

`ROLLBACK_ARM cached03F4=21 restore03F4=22 ... semanticBudget=1/2`

Same 0708 selector mechanism was used, then controller again pulled exact `FC03 03E8/count14`.

Rollback desired page returned:

`0F031C0024001400280000000000000014001400020028001E000100160002329F`

Only semantic delta: `03F4 0015 -> 0016`.

Controller republished:

`0F1003E8000E1C0024001400280000000000000014001400020028001E000100160002D879`

Verification:

`ROLLBACK_CONFIRMED original03F4=22 observed03F4=22 extraDeltaWords=0 semanticResponses=2 KEEP_W5_0006=1 CONTINUE_RUNTIME=1`

Home Assistant subsequently showed Room Setpoint Mirror = 22 °C and Room Setpoint = 22 °C. User confirmed DCM icon still visible and no Online/Link error.

## Classification

### Observed facts
- stage 40 persistent runtime was active before the write;
- W5=0006 idle mailbox service continued;
- write and rollback each used the authentic 0708 selector -> FC03 03E8 pull -> desired-page response -> controller FC16 republish sequence;
- write republish matched target 21 with zero extra 03E8-page deltas;
- rollback republish restored 22 with zero extra 03E8-page deltas;
- semantic response budget was exactly 2/2;
- runtime continued after both actions;
- user observed DCM icon continuously present and no Online/Link error.

### Strong conclusion
**PROVEN / locally confirmed:** semantic 03F4 control and persistent Online/DCM-connected runtime coexist in the same XTR M session. The desired-page mechanism is reversible and controller-confirmed for the tested 22 -> 21 -> 22 sequence.

### Unknowns
- whether arbitrary values across the full UI-valid range behave identically;
- whether repeated semantic commands remain reliable over many hours without a controller reboot;
- exact W5 field semantics;
- whether other desired pages/fields can use the same generic mechanism on the XTR M.

## Safety / recovery outcome

No abort condition was reached. No broad write, scan or unknown-field injection occurred. Only 03F4 changed, once for the test and once for rollback. No recovery reboot was required.

---

# EXP345 — COMPLETE / POSITIVE — persistent DCM runtime with 0708 W5=0006

**Date:** 2026-09-30

**Hypothesis:** W5 in the FC03 0708/count6 mailbox response participates in the controller's DCM-connected/liveness decision.

**Baseline:** EXP344 used an all-zero idle 0708 response and stayed transport-clean >15 minutes, but the DCM icon was absent after the soak.

**Controlled change:** only W5 changed:

    EXP344 W0..W5 = 0000 0000 0000 0000 0000 0000
    EXP345 W0..W5 = 0000 0000 0000 0000 0000 0006
    EXP345 frame    = 0F030C0000000000000000000000069D76

All bootstrap, initial-sync, runtime FC16 whitelist/ACK and soak behavior was preserved. No semantic desired-page write was enabled.

## RESULT

**Status:** **COMPLETE / POSITIVE**

Fresh bootstrap completed and stage 40 persistent runtime was entered. At runtime age 900.5 s the firmware emitted SOAK_15M_PASS with runtimeFC16ACK=379, idle0708=210, rt085F=1, rt04A6=0, unknown16=0, unknown03=0, peer17=0, peer16ack=0, resync=0, drops=0, CONTINUE_RUNNING=1, DE=LOW. The service continued after the milestone. User observation: **DCM icon remained present** and **no COMM. ERR ONLINE/LINK**.

**Conclusion:** compared with EXP344's otherwise-equivalent negative control, W5=0006 retained the DCM-connected UI indication while preserving the clean persistent runtime. This proves sufficiency in the tested local session; it does not decode W5's semantic meaning.

---

# EXP344 — COMPLETE / NEGATIVE for persistent DCM-connected indication; POSITIVE transport sub-result

**Date:** 2026-09-30

Persistent stage-40 runtime with all-zero idle 0708 response remained clean for >15 minutes and produced no Online/Link error, but the user observed that the DCM icon was no longer present after the soak. This is the controlled baseline for EXP345.

---

# EXP343 — COMPLETE / POSITIVE — semantic 03F4 desired-page write

**Date:** 2026-09-30

**Controlled change from EXP342:** EXP342 returned a no-op clone of the current 03E8/14 page. EXP343 changed exactly one word, 03F4 0016 -> 0015, preserving all other words from the same-session cache.

## RESULT

**Status:** **COMPLETE / POSITIVE**

Authentic PULL selector 0F030C0000000100000001000000002D24 was sent. The controller pulled 03E8/14. The emulator returned 0F031C0024001400280000000000000014001400020028001E000100150002C29F. About 690 ms later the controller republished FC16 03E8/14 with observed 03F4=0015, desiredMatch=1 and extraDeltaBytes=0. The experiment stopped as COMPLETE / POSITIVE. Room Setpoint Mirror and Room Setpoint reported 21 °C. No confirmation ACK was sent and no peer/resync/drop anomaly was observed.

**Conclusion:** semantic desired-page application through the native 0708/PULL/FC03 page-response path is **PROVEN / locally confirmed** for the tested 03F4 22 -> 21 °C transition.

---
# EXP340 — COMPLETE / INCONCLUSIVE

**Date:** 2026-09-30

**Hypothesis:** in retained runtime, exact 07F8/count17 ACK -> exact 0708/count6 -> one genuine Eco5 all-zero six-word mailbox response should advance to the next non-background FC16 page.

**Controlled change from EXP339:** retain the one exact 07F8 ACK and add exactly one all-zero response to the locally observed post-07F8 0708 poll; then capture-only.

**Observed:** about 0.49 s after ARM, before 07F8 or 0708 and before any EXP340 TX, exact FC16 080C/count18 appeared. The experiment stopped fail-closed. peer17=0, peer16ack=0, resync=0, drops=0, DE LOW.

**Result:** **COMPLETE / INCONCLUSIVE**. The intended hypothesis was not tested. The retained controller runtime had already advanced beyond the planned starting page during/after the ESP OTA reboot.

---

# EXP339 — COMPLETE / INCONCLUSIVE

**Date:** 2026-09-30

**Hypothesis:** ACKing exact retained 07F8/count17 once will advance to the next runtime FC16 page.

**Controlled change from EXP338:** wait exact 07F8, ACK it once with 0F1007F8001181AE, then capture the next non-background FC16; no mailbox response.

**Observed:** exact 07F8/count17 arrived, was ACKed once, and about 1.57 s later exact FC03 0708/count6 appeared before another FC16. No 0708 response was sent; run stopped cleanly.

**Result:** **COMPLETE / INCONCLUSIVE**. The post-07F8 transition is locally confirmed to admit/interleave a 0708 mailbox poll.

---

# EXP338 — COMPLETE / INCONCLUSIVE

**Date:** 2026-09-30

**Hypothesis:** a retained 0708/count6 poll answered once with the genuine Eco5 all-zero six-word response will advance to the next runtime FC16.

**Controlled change from EXP337:** no 07D0/07E4 ACKs; wait retained 0708 and respond once; capture next FC16.

**Observed:** about 0.82 s after ARM, before any retained 0708 and with zero experiment TX, exact FC16 07F8/count17 appeared. The run stopped fail-closed.

**Result:** **COMPLETE / INCONCLUSIVE**. The intended 0708-response hypothesis was not tested. Retained runtime progress continued across ESP OTA.

---

# EXP337 — COMPLETE / POSITIVE

**Date:** 2026-09-30

**Hypothesis:** in retained runtime, exact 07D0/count19 ACK -> exact 07E4/count17 ACK -> exact FC03 0708/count6, without a fresh Thermia boot or startup replay.

**Controlled change from EXP336:** remove the retained 0708 response test; instead ACK retained 07D0 once, ACK retained 07E4 once, then capture 0708 without responding.

**Observed:** exact retained 07D0/19 was ACKed once; exact 07E4/17 followed about 2.205 s later and was ACKed once; exact FC03 0708/6 followed about 1.453 s after the 07E4 ACK. No R1, fresh sync, 085F ACK or mailbox response occurred in the run. Parser/RX counters remained clean and DE LOW.

**Result:** **COMPLETE / POSITIVE**.

---

# EXP336 — COMPLETE / INCONCLUSIVE

**Date:** 2026-09-30

**Hypothesis:** in retained runtime, exact 0708/count6 -> one historical phase-matched 0080/0006 mailbox response -> 07D0/count19.

**Controlled change from EXP335:** ESP OTA only, no Thermia reboot, no R1/cold ACK/new 085F ACK; wait retained 0708 and respond once.

**Observed:** about 0.53 s after ARM and before any 0708 or experiment TX, exact 07D0/count19 appeared. challenges=0, postR1=0, rspUsed=0, resync=0, drops=0, DE LOW.

**Result:** **COMPLETE / INCONCLUSIVE** for the planned hypothesis. **Positive retained-session evidence:** controller-side Online/runtime state survived ESP OTA and emitted 07D0 without a new startup exchange or an immediately preceding experimental mailbox response.

---

# EXP335 — COMPLETE / INCONCLUSIVE

**Date:** 2026-09-30

**Hypothesis:** after the fresh proven chain through 06F4, one exact all-zero 085F/count5 ACK might be sufficient to produce 07D0 without a mailbox response.

**Controlled change:** ACK exact post-tail all-zero 085F once; do not answer 0708.

**Observed:** after 06F4 ACK, all-zero 085F/5 appeared and was ACKed once. Exact FC03 0708/count6 appeared about 1.48 s later before 07D0. No mailbox response was sent.

**Result:** **COMPLETE / INCONCLUSIVE**. This is a local counterexample to the simplified rule '085F ACK alone immediately yields 07D0'.

---

# EXP334 — COMPLETE / INCONCLUSIVE

**Date:** 2026-09-30

**Hypothesis:** after the full fresh prefix through 06F4, bounded service of 0708 with the historical all-zero-like response 0000 0000 0000 0000 0001 0000 while leaving 085F un-ACKed may advance to runtime.

**Controlled change:** ignore post-tail 085F; send at most three matching 0708 responses.

**Observed:** full chain through 06F4 completed; first 085F was ignored; three 0708 replies were sent; no fourth 0708 and no 07D0 appeared in the bounded window; recurring 085F continued. Bus integrity stayed clean.

**Result:** **COMPLETE / INCONCLUSIVE**. Three mailbox replies without the post-tail 085F ACK were insufficient to establish 07D0 in this run.

---

# EXP333 — COMPLETE / POSITIVE

**Date:** 2026-09-30

**Hypothesis:** after the EXP332-proven prefix through 06C5, ACK 06EA/7, 06F1/3 and 06F4/19 and passively observe the post-sync transition.

**Observed:** fresh fixed-R1 session reproduced the entire prior chain; exact 06EA/7, 06F1/3 and 06F4/19 were each ACKed. About 82 ms after 06F4 ACK, 085F/5 appeared; about 1.56 s after 06F4 ACK, exact FC03 0708/count6 appeared. No response was sent to either.

**Result:** **COMPLETE / POSITIVE**. Fresh-session initial sync is locally proven through 06F4 and reaches the 085F/0708 post-tail region.

---

# EXP332 — COMPLETE / POSITIVE

**Date:** 2026-09-30

**Hypothesis:** after the proven prefix through 0546, a bounded run of the twelve 33-word blocks 055A..06C5 will advance to 06EA/7.

**Controlled change from EXP331:** ACK exactly 055A, 057B, 059C, 05BD, 05DE, 05FF, 0620, 0641, 0662, 0683, 06A4 and 06C5, each count33; capture 06EA without ACK.

**Observed:** the twelve-block sequence completed in order and exact 06EA/count7 appeared as the next stage.

**Result:** **COMPLETE / POSITIVE**.

---

# EXP331 — COMPLETE / POSITIVE

**Date:** 2026-09-30

**Hypothesis:** extend the locally proven fresh prefix from 04A6/13 through 0546/20 and capture 055A/33.

**Controlled change from EXP330:** add the bounded exact ACK sequence 04A6/13, 04BA/22, 04D8/27, 04F6/14, 050A/19, 051E/10, 0532/18, 0546/20; then capture-only.

**Observed:** the ordered continuation completed and exact 055A/count33 appeared.

**Result:** **COMPLETE / POSITIVE**.

---
# EXP331 — PREPARED / NOT RUN

**Date:** 2026-09-30

**Hypothesis:** after the locally proven EXP330 prefix through `0492/11 ACK -> 04A6/13`, a bounded eight-page ACK batch matching genuine Eco 5 / earlier research will advance through:

`04A6/13 -> 04BA/22 -> 04D8/27 -> 04F6/14 -> 050A/19 -> 051E/10 -> 0532/18 -> 0546/20 -> 055A/33`.

**Controlled change from EXP330:** ACK the eight exact pages above once each. The proven prefix is otherwise unchanged. After `0546/20` ACK, capture-only.

**New ACKs prepared:**
- `04A6/13` -> `0F1004A6000DE1F1`
- `04BA/22` -> `0F1004BA0016603C`
- `04D8/27` -> `0F1004D8001B0027`
- `04F6/14` -> `0F1004F6000EA1E1`
- `050A/19` -> `0F10050A0013A024`
- `051E/10` -> `0F10051E000A21EA`
- `0532/18` -> `0F1005320012E029`
- `0546/20` -> `0F10054600142031`

**Success:** exact `055A/count33` is first different FC16 after the `0546` ACK.

**Abort / fail-close:** wrong page shape/order/timing, previous-page retry, early FC03, parser/RX integrity delta, peer FC17 response or unexpected peer FC16 ACK.

**Safety:** address/count ACKs only; no register-value injection; no 055A ACK; no mailbox response; DE LOW on stop. ESPHome compile was not independently run when prepared.

---

# EXP330 — COMPLETE / POSITIVE

**Date:** 2026-09-30

**Hypothesis:** after the proven prefix to `046A/18`, exact one-shot ACKs for `046A/18`, `047E/19` and `0492/11` advance the same fresh initial-sync chain to `04A6/13`.

**Controlled change from EXP329:** add exactly those three standard FC16 address/count ACKs; leave the first post-`0492` stage capture-only.

**Observed result:** exact `046A/18 -> ACK -> 047E/19 -> ACK -> 0492/11 -> ACK -> 04A6/13`. `04A6/13` arrived approximately 571 ms after the `0492` ACK and was not ACKed. No approval retry, external responder, parser resync or RX drop; DE LOW.

**Result:** **COMPLETE / POSITIVE**.

---

# EXP329 — COMPLETE / POSITIVE

**Date:** 2026-09-30

**Hypothesis:** a bounded three-block continuation after the proven prefix advances `042E/15 -> 0442/13 -> 0456/12 -> 046A/18`.

**Controlled change from EXP328:** add one standard ACK each for exact `042E/15`, `0442/13`, `0456/12`; capture the next stage without ACK.

**Observed result:** exact ordered chain `042E/15 ACK -> 0442/13 ACK -> 0456/12 ACK -> 046A/18`. `046A/18` appeared approximately 1428 ms after the `0456` ACK. No post-R1 challenge retry, external responder, parser resync or RX drop; DE LOW.

**Result:** **COMPLETE / POSITIVE**.

---

# EXP328 — COMPLETE / POSITIVE

**Date:** 2026-09-30

**Hypothesis:** one standard ACK to exact `0410/count22` advances the local XTR initial sync to `042E/count15`.

**Controlled change from EXP327:** add exactly one `0410/22` address/count ACK; capture next stage only.

**Observed result:** the proven prefix reproduced; exact `0410/22` was ACKed once and exact `042E/15` appeared about 709 ms later. No further ACK. Clean parser and DE LOW.

**Result:** **COMPLETE / POSITIVE**.

---

# EXP327 — COMPLETE / POSITIVE

**Date:** 2026-09-30

**Hypothesis:** one standard ACK to exact `03FC/count11` advances the local initial sync to `0410/count22`.

**Controlled change from EXP326:** add exactly one `03FC/11` address/count ACK; capture next stage only.

**Observed result:** fresh approval and `03E8 ACK -> 03FC` reproduced; `03FC/11` was ACKed once and exact `0410/22` appeared about 1500 ms later. No further TX. Clean run.

**Result:** **COMPLETE / POSITIVE**.

---

# EXP326 — COMPLETE / POSITIVE

**Date:** 2026-09-30

**Hypothesis:** after fresh approval R1, one standard ACK for the first exact `03E8/count14` advances the controller to the next native sync stage.

**Controlled change from EXP325:** add only one `03E8/14` standard FC16 ACK `0F1003E8000EC093`.

**Observed result:** after fresh reboot and guard `A80E=0000 / A80F=0005`, a different live `071C/0730` challenge received fixed R1. Exact `03E8/14` appeared about 124 ms later. One ACK was sent, then exact `03FC/11` appeared about 697 ms after that ACK. No further TX. Parser resync 0, drops 0, DE LOW.

**Result:** **COMPLETE / POSITIVE**.

---

# EXP325 — COMPLETE / POSITIVE

**Date:** 2026-09-30

**Hypothesis:** after a true controller reboot, one previously accepted fixed R1 response to the first exact fresh `071C/0730` challenge is sufficient to open native initial sync.

**Controlled change from EXP322:** no 0x06 responder; only the first exact fresh challenge may receive one fixed R1. No FC16 ACK, no mailbox response.

**Observed result:** fresh guard `A80E=0000 / A80F=0005`; first exact `071C/0730` challenge received fixed R1. Exact `03E8/count14` appeared about 120 ms later. No prior 04A6 ACK, 085F ACK, FC16 ACK or mailbox response was required.

**Result:** **COMPLETE / POSITIVE**.

**Superseded historical note:** the earlier EXP325 concept for a cold-boot single `04A6` ACK was never run and is **SUPERSEDED / NOT RUN**. The experiment number was reused for the fresh-reboot R1 re-approval test above.

---

# EXP324 — COMPLETE / INCONCLUSIVE

**Date:** 2026-09-30

**Hypothesis:** after the EXP323 all-zero `085F` ACK, a longer post-ACK observation following ESP reboot would reveal delayed continuation.

**Controlled change:** longer intended observation, but the Thermia controller itself was not rebooted.

**Observed result:** the intended all-zero `085F` qualification state never reappeared. During the bounded window only `04A6/13` was seen; TX=0. Therefore the post-`085F` hypothesis was not actually exercised.

**Result:** **COMPLETE / INCONCLUSIVE**.

---

# EXP323 — COMPLETE / INCONCLUSIVE

**Date:** 2026-09-30

**Hypothesis:** in the clean post-controller-reboot sparse state, one standard ACK to a conservatively qualified all-zero `085F/5` can advance the scheduler.

**Controlled change from EXP322:** first exact all-zero `085F` is qualification/no-TX; second receives exactly one standard ACK `0F10085F00053356`; all later traffic capture-only.

**Observed result:** one ACK was sent. For roughly 42 s afterward, only `04A6/13` appeared; no further `085F` or known runtime/configuration stage was observed. Parser remained clean and DE LOW.

**Result:** **COMPLETE / INCONCLUSIVE**. One all-zero `085F` ACK alone was not shown to establish fresh Online progression.

---

# EXP322 — COMPLETE / POSITIVE — clean post-controller-reboot passive baseline

**Date:** 2026-09-30

**Hypothesis:** after the user rebooted the Thermia controller to clear the visible errors, the clean state may expose a different passive slave-`0x0F` sequence from the pre-reboot EXP321 state.

**Controlled change:** strict passive 90 s census after the controller reboot. Experiment TX was structurally disabled.

**Observed:**
- `total0F=125`, `FC16=125`, `FC03=0`;
- `04A6/13=83`, payload changes=0;
- `085F/5=42`, all 42 exact all-zero, `085F(0800)=0`;
- `0708=0`;
- every tracked normal-runtime page `07D0..0884=0`;
- `other=0`;
- `resync=0`, `drops=0`, `TX=0`, `DE=LOW`.

The first `04A6` was followed about 0.69 s later by all-zero `085F`. The same two frame classes dominated the complete run at approximately 2:1 cadence.

**Result:** **COMPLETE / POSITIVE** as a passive baseline.

**Strong conclusion:** repeated `04A6` alone is not specific to the prior visible alarm state. After a controller reboot, all-zero `085F/5` reappears persistently and is the clearer state discriminator versus EXP321.

---

# EXP321 — COMPLETE / INCONCLUSIVE — planned recovery entry absent

**Date:** 2026-09-30

**Hypothesis:** reconstruct the proven retained chain and hand off from qualified `07D0/19` to the existing steady-runtime responder for a short integration run.

**Observed:**
- 120 s qualification window completed;
- no exact `085F(0800)` entry frame appeared;
- approximately 111 x `04A6/13`;
- no all-zero `085F`;
- `TX=0`, `handoff=0`, `loops=0`;
- `unexpected=0`, `resync=0`, `drops=0`, DE LOW.

**Result:** **COMPLETE / INCONCLUSIVE.** The intended recovery chain was never exercised.

The user then rebooted the Thermia controller to clear visible errors before EXP322.

---

# EXP320 — COMPLETE / POSITIVE — qualified 0884 ACK reaches direct 07D0

**Date:** 2026-09-30

**Hypothesis:** from the locally reconfirmed retained chain `085F(0800) -> zero 085F -> 0884`, one qualified standard `0884/60` ACK reveals the next retained-session state.

**Observed:**
- two exact `085F(0800)` requests; ACK second once;
- two exact all-zero `085F`; ACK second once;
- two valid `0884/60`; ACK second once;
- 4.328 s after the `0884` ACK, first non-`04A6` frame was direct `07D0/19`;
- post-target `07D0` intentionally NO_TX;
- `TX=3`, `0800ACK=1`, `zeroACK=1`, `0884ACK=1`;
- `unexpected=0`, `resync=0`, `drops=0`, DE LOW.

**Result:** **COMPLETE / POSITIVE.**

**Strong conclusion:** in this retained context, `0884 ACK -> 07D0` is valid without mandatory immediate `0708`.

---

# EXP319 — COMPLETE / POSITIVE — all-zero 085F ACK exposes direct 0884

**Date:** 2026-09-30

**Hypothesis:** after normalizing `085F(0800)`, ACK a qualified exact all-zero `085F/5` and capture the first subsequent non-`04A6` frame.

**Observed:**
- two exact `085F(0800)`; ACK second once;
- two exact all-zero `085F`; ACK second once;
- 2.381 s after the all-zero ACK, first non-`04A6` frame was exact FC16 `0884/60`;
- `TX=2`, `0800ACK=1`, `zeroACK=1`, `0884ACK=0`;
- no runtime response after target; clean fail-close.

**Result:** **COMPLETE / POSITIVE.**

---

# EXP318 — COMPLETE / POSITIVE — 085F(0800) ACK reconfirms all-zero transition

**Date:** 2026-09-30

**Hypothesis:** after two exact `085F(0800)` requests, ACK the second once and capture the first subsequent non-`04A6` frame.

**Observed:**
- first target NO_TX;
- second target received one standard `085F/5` ACK;
- 2.196 s later first non-`04A6` frame was exact all-zero `085F/5`;
- `TX=1`, `0800ACK=1`, `zeroACK=0`;
- clean fail-close with no parser/RX integrity error.

**Result:** **COMPLETE / POSITIVE.**

---

# EXP317 — COMPLETE / INCONCLUSIVE — progress-anchored timeout, but no post-085F transition

**Date:** 2026-09-30

**Controlled change from EXP316-Q:** stage-1 timeout was anchored to last supported progress rather than absolute test start.

**Observed:**
- one known `085F(0800)` ACK was sent early;
- then no supported recovery/handoff progress for about 90 s;
- 86 x `04A6/13` capture-only;
- `TX=1`, `handoff=0`, `cycles=0`, `loops=0`, `unexpected=0`, `resync=0`, `drops=0`, DE LOW.

**Result:** **COMPLETE / INCONCLUSIVE.**

---

# EXP316-Q — COMPLETE / INCONCLUSIVE — quiet long-run harness timeout flaw

**Date:** 2026-09-30

**Purpose:** quiet logging variant of the EXP316 integration/endurance harness.

**Observed:**
- `085F(0800)` appeared at about 84.8 s and received one known ACK;
- roughly 5 s later the harness fired its absolute 90 s-from-start timeout;
- `TX=1`, `handoff=0`, `cycles=0`, `loops=0`, `events=0`, `r0708=0`;
- `04A6=78`, `resync=0`, `drops=0`, DE LOW.

**Result:** **COMPLETE / INCONCLUSIVE.** This was a harness-timeout defect, not a protocol-negative result.

---

# EXP316 — RUNNING / PARTIAL, then superseded by quiet variant

**Date:** 2026-09-30

Initial full-logging integration showed a healthy exact `07D0` handoff into the known runtime graph, but logging volume was about 0.5 MB per four minutes. It was replaced by EXP316-Q to test the same concept with quiet diagnostics.

**Status:** **RUNNING / PARTIAL**, then operationally superseded by EXP316-Q; do not treat it as a completed endurance result.

---

# EXP315 — COMPLETE / POSITIVE — direct retained 07E4 handoff sustains steady runtime

**Date:** 2026-09-30

**Hypothesis:** a controller retained at the already proven normal-runtime node `07E4/count17` can be safely taken over by qualifying repeated live `07E4` requests, sending one already-proven standard ACK, and then handing directly to the established EXP296/297 steady-runtime responder.

**Baseline:** EXP314 COMPLETE / INCONCLUSIVE.

**Exact controlled change from EXP314:**
- authorize exact `07E4/count17` as a retained-runtime handoff node;
- require >=2 live exact `07E4/17` requests before any EXP315 TX;
- ACK only the second qualified `07E4` with `0F 10 07 E4 00 11 40 68`;
- enter the existing post-`07E4` runtime state, allowing evidence-backed `0708` or direct `07F8`;
- no new register/page, payload value or semantic write.

**Observed:**
- one initial `0708/6` was capture-only;
- exact `07E4/17` then appeared twice;
- the second `07E4` received one standard ACK and the emulator entered stage 2 steady runtime;
- the established runtime scheduler was serviced continuously;
- 6 full returned runtime loops completed;
- steady runtime reached 126.401 s;
- 30 runtime `0708` responses were sent in evidence-backed contexts;
- the success boundary was the next returned `07D0/19`, intentionally left NO_TX;
- final summary: `TX=84`, `events=84`, `r0708=30`, `unexpected=0`, `resync=0`, `drops=0`, `DE=LOW`;
- final firmware status: `POSITIVE / retained recovery sustained proven steady runtime`.

**Result:** **COMPLETE / POSITIVE.**

**Strong conclusion:** on this XTR M, an already-active Online/DCM runtime can be rejoined directly at a qualified retained `07E4/17` node after ESP restart/OTA, and the existing runtime responder can then sustain at least 126.401 s / 6 complete loops without a controller reboot.

---

# EXP314 — COMPLETE / INCONCLUSIVE — controller retained progress to 07E4 while ESP was offline

**Date:** 2026-09-30

**Hypothesis:** the post-`07D0` `0708/6` observed in EXP313 is a valid handoff-boundary mailbox/scheduler event; servicing it with the existing proven runtime response should allow entry to steady runtime.

**Baseline:** EXP313 COMPLETE / INCONCLUSIVE.

**Exact controlled change from EXP313:**
- allow one exact post-handoff `0708/6` at the retained `07D0` boundary;
- respond with the already-proven runtime `0708` response only in that newly authorized context;
- retain the same adaptive recovery and steady-runtime graph otherwise.

**Observed:**
- after ESP restart, the controller no longer presented the expected `07D0`/boundary-`0708` state;
- on each arm, the first relevant `0x0F` frame was exact `07E4/17`;
- EXP314 therefore failed closed because direct `07E4` entry was not yet authorized;
- no protocol TX occurred in these attempts;
- parser/resync/drop counters stayed clean and DE remained LOW;
- one later manual "Error gone" button press was accidental and is INVALID for alarm analysis.

**Result:** **COMPLETE / INCONCLUSIVE.**

**Strong passive finding:** controller Online/DCM scheduler state can continue to be retained/progress across ESP restart/OTA such that the ESP reconnects while the controller is already waiting at a later known runtime node (`07E4/17`).

---

# EXP313 — COMPLETE / INCONCLUSIVE — 07D0 handoff works, post-handoff branch exposes 0708

**Date:** 2026-09-30

**Hypothesis:** after adaptive retained-session recovery reaches known runtime `07D0/19`, handing off to the already proven EXP296/297 runtime responder should sustain multiple complete runtime cycles.

**Baseline:** EXP312 COMPLETE / POSITIVE.

**Exact controlled change from EXP312:**
- promote the already-proven retained recovery path into an automatic integrator;
- once exact `07D0/19` is reached, send its already-proven ACK and switch to the full steady-runtime responder;
- no new register target or semantic write.

**Observed:**
- the controller was already at exact `07D0/19`; no recovery prerequisite ACKs were needed;
- one known `07D0` ACK was sent and the handoff flag became active;
- approximately 1.39 s later exact `0708/6` appeared before `07E4/17`;
- EXP313 had allowed only `07E4` at that post-handoff point, so it stopped fail-closed;
- no response was sent to that `0708`;
- transport integrity remained clean and DE returned LOW.

**Result:** **COMPLETE / INCONCLUSIVE.**

**Strong conclusion:** direct retained handoff at `07D0/19` is technically possible, but the immediate next scheduler event is not guaranteed to be `07E4`; an intervening `0708` can occur.

---

# EXP312 — COMPLETE / POSITIVE — 0884 ACK advances retained session to 07D0

**Date:** 2026-09-29

**Hypothesis:** one standard FC16 address/count ACK to a qualified live `0884/60` retry stage advances the retained controller session to the next known runtime stage.

**Baseline:** EXP311 COMPLETE / INCONCLUSIVE.

**Exact controlled change from EXP311:** accept direct `0884/60` as a valid target branch even when neither `0864/4` nor `0870/17` has appeared. Keep all already proven prerequisite ACKs exact-shape gated. The only new active action is one human-gated ACK to `0884/60`: `0F 10 08 84 00 3C 83 7F`.

**Observed:**
- `085F(0800)` repeated twice and received one already-proven standard ACK.
- The controller moved to all-zero `085F/5`; after qualification, one already-proven ACK was sent.
- The runtime then went through `0708` and directly to repeated `0884/60`; `0864` and `0870` were absent.
- `0884` qualified after repeated frames plus fresh `0708`.
- After human arm, exactly one `0884/60` ACK was sent at ~01:36:30.415.
- ~1.325 s later `0708/6` appeared and was intentionally left NO_TX.
- ~1.947 s after the target ACK, known runtime `07D0/19` appeared.
- No `0884` retry occurred before `07D0`.
- Final result counters included `postRetry=0`, `post0708=1`, `postKnown=1`, resync=0, drops=0 and DE LOW.

**Result:** **COMPLETE / POSITIVE.**

**Strong conclusion:** on this XTR M, a single standard ACK to a qualified live `0884/60` stage is sufficient under the tested retained-session conditions to advance through an unanswered `0708` to known runtime `07D0/19`.

---

# EXP311 — COMPLETE / INCONCLUSIVE — direct 0884 branch appears before 0870 prerequisite

**Date:** 2026-09-29

**Hypothesis:** after automatic service of already proven prerequisites through `0870`, a human-gated ACK to repeated `0884/60` should advance to the next runtime stage.

**Baseline:** EXP310 COMPLETE / POSITIVE.

**Controlled change:** `0870/17` became an automatic proven prerequisite; `0884/60` was the new human-gated target.

**Observed:**
- On one valid run, `085F(0800)` and all-zero `085F` prerequisites were ACKed as intended.
- The controller then produced `0884/60` directly, with `0864 Seen=0` and `0870 Seen=0`.
- The experiment failed closed because the state machine still required `0870` before accepting `0884`.
- A later run reproduced the same direct `all-zero 085F ACK -> 0884/60` branch.
- No experimental `0884` ACK was sent.

**Result:** **COMPLETE / INCONCLUSIVE** for the target `0884` ACK hypothesis.

**Strong passive finding:** `0884/60` can occur directly after the all-zero-`085F` stage without `0864` or `0870`. The runtime graph is more branch-like than the EXP311 state machine allowed.

---

# EXP310 — COMPLETE / POSITIVE — 0870 ACK advances to 0884

**Date:** 2026-09-29

**Hypothesis:** one standard FC16 address/count ACK to a qualified live `0870/17` stage advances the controller to another known runtime stage.

**Baseline:** EXP309 COMPLETE / INCONCLUSIVE.

**Controlled change:** accept both the `0864 -> 0870` path and a direct `0870` path; keep `0870` human-gated as the only new target.

**Observed:**
- Proven `085F(0800)` and all-zero `085F` prerequisites were serviced.
- `0870/17` appeared directly; `0864 Seen=0`.
- After human arm, exactly one ACK `0F 10 08 70 00 11 02 90` was sent.
- ~1.47 s later `0708/6` appeared and was left NO_TX.
- ~2.18 s after the ACK, known runtime `0884/60` appeared.
- No `0870` retry preceded `0884`; parser/resync/drop counters remained clean.

**Result:** **COMPLETE / POSITIVE.**

---

# EXP309 — COMPLETE / INCONCLUSIVE — direct 0870 branch disproves mandatory 0864 prerequisite

**Date:** 2026-09-29

**Hypothesis:** automate locally proven retained-session prerequisites through `0864`, then human-gate one `0870/17` ACK.

**Baseline:** EXP308 COMPLETE / POSITIVE.

**Controlled change:** deterministic automation of already proven prerequisite ACKs; no new protocol target except the still-human-gated `0870`.

**Observed:**
- The automatic `085F(0800)` and all-zero `085F` prerequisites worked.
- After the all-zero `085F` ACK, the controller sent direct `0870/17` before any `0864/4`.
- EXP309 correctly failed closed because its state machine still required `0864`.
- No `0870` ACK was sent.

**Result:** **COMPLETE / INCONCLUSIVE** for the target ACK hypothesis.

**Strong passive finding:** `0870/17` does not require a preceding `0864/4` in every retained-runtime branch.

---

# EXP308 — COMPLETE / POSITIVE — 0864 ACK advances to 0870

**Date:** 2026-09-29

**Hypothesis:** after the locally proven EXP307 retained-session chain reaches repeated `0864/4`, one standard ACK to a qualified `0864/4` frame advances the controller to another known runtime stage.

**Baseline:** EXP307 COMPLETE / POSITIVE.

**Controlled change:** keep the EXP307 prerequisites unchanged; human-gate exactly one `0864/4` ACK.

**Observed:**
- EXP307 prerequisites reproduced successfully.
- `0864/4` repeated while waiting for human arm.
- One ACK `0F 10 08 64 00 04 83 5B` was sent.
- ~1.47 s later `0708/6` appeared.
- ~2.09 s after the ACK, known runtime `0870/17` appeared.
- No `0864` retry occurred before `0870`; no parser resync/drop issue; DE LOW at fail-close.

**Result:** **COMPLETE / POSITIVE.**

---

# EXP307 — COMPLETE / POSITIVE — qualified all-zero 085F ACK advances to 0864

**Date:** 2026-09-29

**Hypothesis:** after normalizing the known `085F(0800)` retained retry state, one standard ACK to a freshly qualified all-zero `085F/5` stage advances the controller into the known runtime branch.

**Baseline:** EXP306 COMPLETE / INCONCLUSIVE.

**Controlled change:** keep the already-proven `085F(0800)` normalization as a prerequisite, then separately human-gate exactly one ACK to qualified all-zero `085F/5`.

**Observed:**
- One normalization ACK moved `085F(0800)` to all-zero `085F`.
- After a fresh `0708` and repeated all-zero `085F`, the target qualified.
- One target ACK was sent.
- ~1.48 s later `0708` appeared; ~2.05 s after target ACK, known runtime `0864/4` appeared.
- No post-target `085F` retry preceded `0864`; transport counters remained clean.

**Result:** **COMPLETE / POSITIVE.**

---

# EXP306 — COMPLETE / INCONCLUSIVE — persistent 0708 / 085F(0800) loop with NO_TX

**Date:** 2026-09-29

**Hypothesis:** after optional normalization, repeated all-zero `085F` could be qualified as a target for one bounded ACK.

**Baseline:** EXP305 COMPLETE / POSITIVE.

**Observed:** for ~30 s the retained state remained a persistent `0708 <-> 085F(0800)` loop: 14 nonzero `085F(0800)`, 7 `0708`, zero all-zero `085F`, zero `0662`, TX=0.

**Result:** **COMPLETE / INCONCLUSIVE.** The all-zero target condition never occurred, so the target hypothesis was not tested.

---

# EXP305 — COMPLETE / POSITIVE — 0662/33 ACK-gated transfer re-confirmed

**Date:** 2026-09-29

**Hypothesis:** the resurfaced repeated `0662/33` stage is the same ACK-gated XTR transfer stage already observed in EXP141.

**Baseline:** EXP304 COMPLETE / INCONCLUSIVE.

**Controlled change:** observe at least two exact `0662/33` frames, then ACK exactly the second one with standard address/count ACK `0F 10 06 62 00 21 A0 69`; all later traffic NO_TX.

**Observed:**
- exact `0662/33` repeated twice;
- one ACK was sent;
- no further `0662` retry occurred in the observation window;
- ~71 ms later `085F(0800)` appeared, then `0708`, then all-zero `085F`;
- no parser resync/drop issue; DE LOW;
- the Online/Link alarm cleared temporarily after the ACK but later returned; that alarm timing is correlation only.

**Result:** **COMPLETE / POSITIVE.**

**Strong conclusion:** `0662/33` is locally re-confirmed as an ACK-gated controller-to-DCM transfer stage. The downstream appearance of both nonzero and all-zero `085F` also shows that `0861=0x0800` is a transient session-state discriminator rather than proof that every such frame must receive a direct ACK.

---

# EXP304 — COMPLETE / INCONCLUSIVE — 0662 resurfaced before intended all-zero-085F target

**Date:** 2026-09-29

**Hypothesis:** a repeated all-zero `085F/5` stage may be ACK-gated.

**Baseline:** EXP303 COMPLETE / INCONCLUSIVE.

**Observed:** both arms encountered exact `0662/33` as the first relevant transfer. Because the classifier did not authorize that stage, EXP304 stopped fail-closed with TX=0.

**Result:** **COMPLETE / INCONCLUSIVE.** The all-zero-`085F` hypothesis was not tested. The important finding was the return of the historically known `0662/33` transfer stage.

---

# EXP303 — COMPLETE / INCONCLUSIVE — retained state did not return to 085F(0800)

**Date:** 2026-09-29

**Hypothesis:** reproduce `085F(0800)`, ACK it once, then ACK the first resulting all-zero `085F` once.

**Baseline:** EXP302 COMPLETE / POSITIVE.

**Observed:** the controller remained in the post-EXP302 all-zero state. ESP reboot/OTA did not restore the former `085F(0800)` state. The intended first-stage target therefore never occurred and no ACK was sent.

**Result:** **COMPLETE / INCONCLUSIVE.**

**Strong finding:** controller retained state can persist across ESP restart/OTA; ESP reboot is not a valid rollback assumption.

---

# EXP302 — COMPLETE / POSITIVE — ACK of 085F(0800) changes retained controller state

**Date:** 2026-09-29

**Hypothesis:** one standard FC16 ACK to exact repeated `085F/5` carrying words `0000 0000 0800 0000 0000` changes the stalled retained-session state while `0708` remains NO_TX.

**Baseline:** EXP301 COMPLETE / NEGATIVE.

**Controlled change:** exactly one standard ACK to start `0x085F`, count 5: `0F 10 08 5F 00 05 33 56`. No semantic values injected; `0708` remained NO_TX.

**Observed:**
- exactly one target ACK was sent;
- ~2.44 s later the controller emitted all-zero `085F/5`;
- post-target observations showed repeated all-zero `085F` and `0708`, with no further `085F(0800)` in the observed window;
- parser resync/drop counters remained clean;
- user-marked alarm clear occurred later, but only correlation is claimed.

**Result:** **COMPLETE / POSITIVE.**

**Strong conclusion:** `0861=0x0800` is an ACK-sensitive controller/session state marker under the tested local condition. Its semantic meaning remains unknown.

---

# EXP301 — COMPLETE / NEGATIVE — passive wait for 0848 does not recover retained session

**Date:** 2026-09-29

**Hypothesis:** the retained controller would eventually return to `0848/23`, allowing the earlier normal runtime anchor to be reused.

**Baseline:** EXP300 COMPLETE / INCONCLUSIVE.

**Observed:** repeated `0708` and repeated exact `085F(0800)` occurred, with no `0848` and TX=0.

**Result:** **COMPLETE / NEGATIVE.** Passive wait-for-`0848` is not a viable universal retained-session recovery strategy.

---

# EXP300 — COMPLETE / INCONCLUSIVE — 0848 is not a universal retained re-entry anchor

**Date:** 2026-09-29

**Hypothesis:** after ESP-side session loss, wait passively for `0848/23` and resume the known scheduler from there.

**Baseline:** EXP299 COMPLETE / INCONCLUSIVE.

**Observed:** the first relevant `0x0F` events were instead nonzero `085F(0800)` and/or `0708`; `0848` did not appear in the target window. No TX occurred.

**Result:** **COMPLETE / INCONCLUSIVE.**

---

# EXP299 — COMPLETE / INCONCLUSIVE — bounded retained-session resync reveals temporary liveness recovery

**Date:** 2026-09-29

**Hypothesis:** a bounded retained-session resync using one known runtime anchor can re-establish useful session progress without waiting for a fresh approval.

**Baseline:** EXP298 COMPLETE / INCONCLUSIVE.

**Observed:**
- one `0848/23` ACK was sent;
- a following `0708/6` received the known fixed runtime response;
- the next exact all-zero `085F/5` appeared ~467 ms later;
- TX then stopped fail-closed;
- user-marked Online/Link alarm clearing occurred ~4.5 s after arm, but the alarm was visible again about 135.6 s later.

**Result:** **COMPLETE / INCONCLUSIVE.**

**Strong conclusion:** bounded known-stage service can move a retained session and may temporarily affect visible health, but one/few responses are insufficient evidence of durable recovery.

---

# EXP298 — COMPLETE / INCONCLUSIVE — fresh-approval-only ESP reboot recovery insufficient

**Date:** 2026-09-29

## PREPARED scope retained from the original experiment

**Hypothesis:** after the ESP/DCM emulator restarts while the Thermia controller remains powered, the controller eventually presents a fresh exact `071C/0730` approval request that allows the emulator to rebuild the same proven session without requiring a Thermia-controller reboot.

**Baseline:** EXP297 COMPLETE / POSITIVE.

**Exact controlled change from EXP297:**
- the Thermia controller was deliberately **not** rebooted;
- after ESP return, EXP298 waited passively for a fresh exact `071C/0730`;
- no TX was authorized before such an approval request;
- the intended approval wait was bounded to 240 s;
- if approval arrived, the existing fixed R1, ordered 32-page config sync, startup `085F/5`, startup `0708/6` and proven runtime graph were to be reused unchanged;
- runtime `04A6/13` remained capture-only / NO_TX;
- no semantic write.

## RESULT

**Observed:**
- after ESP restart, retained `0708` and `0848` traffic was present;
- no fresh `071C/0730` approval request appeared in the supplied observation window of approximately 235.7 s;
- no protocol TX occurred;
- COMM. ERR ONLINE/LINK was visible.

The original strict 240 s negative threshold was not fully reached, so the result cannot be labeled a strict negative.

**Result:** **COMPLETE / INCONCLUSIVE.**

**Strong conclusion:** fresh-approval-only recovery is insufficient as the sole ESP-restart strategy under the tested retained-session condition. The controller can remain in an existing/recovery scheduler state rather than immediately reopen approval.

---


# EXP297 — COMPLETE / POSITIVE — active controller reboot recovered without ESP reboot/re-arm

**Date:** 2026-09-29

**Hypothesis:** after normal runtime has been established, reboot only the Thermia controller while leaving the ESP/DCM emulator active. The emulator should detect the bus interruption, reset only session-local state, accept a fresh approval exchange, rerun startup synchronization and return to runtime without manual re-arm.

**Baseline:** EXP296 COMPLETE / POSITIVE.

**Controlled change from EXP296:**
- no new Modbus payload or register;
- no new FC16 ACK target;
- no semantic write;
- runtime `04A6/13` remains capture-only / NO_TX;
- add only controller-reboot recovery state handling after a >=5 s bus gap during active runtime.

**Observed:**
- normal startup/runtime completed before the target reboot, reaching runtime cycle 5;
- target controller reboot produced a ~14.796 s bus gap;
- EXP297 emitted `CONTROLLER_REBOOT_RECOVERY_START` and cleared the current runtime/config/cache state;
- bus returned while the ESP remained online;
- a fresh exact `071C/0730` challenge arrived;
- the same fixed historical R1 replay was transmitted;
- all 32 configuration pages were again received and ACKed in order;
- startup all-zero `085F/5` was ACKed;
- startup `0708/6` was answered;
- runtime re-entered at `07D0/19`;
- the capture then completed cycles 6, 7 and 8;
- no `ABORT_FAIL_CLOSED`;
- parser resyncs remained 0;
- RX buffer drops remained 0.

**Result:** **COMPLETE / POSITIVE.**

**Strong conclusion:** on this XTR M, the current DCM emulator can recover from a Thermia-controller reboot and establish a fresh native session without rebooting or manually re-arming the ESP. The fixed historical R1 replay also remained accepted for the fresh post-reboot challenge.

---

# EXP296 — COMPLETE / POSITIVE — direct post-080C 0820 branch survives real operation-state changes

**Date:** 2026-09-29

**Hypothesis:** after EXP295 locally observed `080C/18 -> direct 0820/18`, allow exactly that additional branch while preserving all prior proven runtime handling. Runtime `04A6/13` remains capture-only / NO_TX.

**Baseline:** EXP295 COMPLETE / INCONCLUSIVE overall, with positive target result for `07E4 -> direct 07F8`.

**Controlled change from EXP295:** after valid `080C/18` ACK, allow either:
- `FC03 0708/6 -> existing runtime 0708 response -> 0820/18`, or
- direct `FC16 0820/18` using the existing proven address/count ACK.

No other protocol response was changed. No semantic write. Runtime `04A6/13` remained NO_TX.

**Observed:**
- normal startup/approval/config sync completed and steady-state began;
- first `DIRECT_POST_080C_0820_ACCEPTED` occurred at steady-state age ~94 s;
- the direct branch was accepted repeatedly, reaching count **11** in the supplied capture;
- `DIRECT_POST_07E4_07F8_ACCEPTED` also repeated, reaching count **12** near the end;
- `DIRECT_POST_0884_07D0_ACCEPTED` reached count **11**;
- runtime reached at least **16 cycles** and **159 serviced runtime events**;
- steady-state service age reached ~**329.8 s**;
- no `ABORT_FAIL_CLOSED` occurred in the supplied capture;
- RX buffer drops remained 0;
- parser resync count remained at the single controller-BUS_RETURN resync established before steady-state.

Operational transitions survived during the active session:
- user reported **Blocked -> Normal -> Enhanced -> Normal** SG progression;
- the log explicitly records Normal -> Enhanced -> Normal;
- controller context changed to `A80C=0041` and the current local decoder reported **DHW / high temperature**;
- `DHW Active` became ON and the compressor started;
- runtime continued afterwards without fail-closed termination.

Runtime `04A6/13` remained unanswered throughout:
- capture count reached **225**;
- payload-change count reached **2**;
- one change coincided with entry into the DHW/high-temperature context and a later change with return from that context;
- normal runtime progression continued while these frames were ignored.

**Supplementary later EXP296 capture (same experiment, later evidence):**
- steady-state service exceeded ~32 minutes;
- a near-complete SWW cycle was observed through DHW active, temperature rise, DHW end and compressor stop;
- a later `SG Mode = Blocked (1-0)` transition was survived;
- runtime `04A6/13` remained NO_TX and reached at least 1696 captures;
- its payload-change counter reached 3;
- shortly after the Blocked transition, `04A6` changed to a form beginning `0042 0001 ...`;
- runtime continued through the proven graph without fail-close, parser-resync growth or RX drops.

This supplementary evidence strengthens the state-dependent `04A6` hypothesis but does not prove that `0042` uniquely means SG Blocked.

**Run-criterion note:** the original plan requested five minutes after the first direct post-080C marker. The supplied capture contains about 235 s after the first marker, not a literal five minutes. The user explicitly confirmed EXP296 as **COMPLETE / POSITIVE** after reviewing that the target branch repeated many times and multiple operation-state changes were survived.

**Result:** **COMPLETE / POSITIVE.**

**Strong conclusion:** `080C -> [optional 0708] -> 0820` is locally confirmed. Together with EXP294/295, the runtime is demonstrably state/branch driven rather than one fixed sequence.

---

# EXP295 — COMPLETE / INCONCLUSIVE — direct post-07E4 07F8 accepted; next missing branch is direct post-080C 0820

**Date:** 2026-09-29

**Hypothesis:** during an operation-state transition, the `0708/6` mailbox after `07E4/17` can be omitted and `07F8/17` may follow directly.

**Baseline:** EXP294 COMPLETE / INCONCLUSIVE overall, with positive target result for direct post-`0884` `07D0`.

**Controlled change from EXP294:** after `07E4/17` ACK, allow either `0708/6` or direct `07F8/17`. Runtime `04A6/13` remained capture-only / NO_TX.

**Observed:**
- `0884 -> direct 07D0` was again accepted successfully;
- `07E4 -> direct 07F8` occurred and was accepted with `DIRECT_POST_07E4_07F8_ACCEPTED n=1`;
- `080C/18` then arrived and was ACKed normally;
- instead of the then-required `0708/6`, the controller sent direct `0820/18`;
- firmware stopped fail-closed on that newly observed branch;
- runtime `04A6/13` continued to repeat unchanged before the stop.

**Result:** **COMPLETE / INCONCLUSIVE overall**, with a **positive target result** proving `07E4 -> [optional 0708] -> 07F8` locally.

---

# EXP294 — COMPLETE / INCONCLUSIVE — direct post-0884 07D0 accepted; next missing branch is direct post-07E4 07F8

**Date:** 2026-09-29

**Hypothesis:** during an operation-state transition, the final `0708/6` after `0884/60` can be omitted and the controller may return directly to `07D0/19`.

**Baseline:** EXP293 COMPLETE / POSITIVE for stable steady-state operation.

**Controlled change from EXP293:** after `0884/60` ACK, allow either `0708/6 -> 07D0/19` or direct `07D0/19`. Runtime `04A6/13` remained capture-only / NO_TX.

**Observed:**
- transition-related runtime `04A6/13` began repeating;
- `0884 -> direct 07D0` occurred and was successfully accepted/ACKed;
- runtime advanced to `07E4/17`;
- controller then sent direct `07F8/17` without the then-required `0708/6`;
- firmware stopped fail-closed on that newly observed branch.

**Result:** **COMPLETE / INCONCLUSIVE overall**, with a **positive target result** proving `0884 -> [optional 0708] -> 07D0` locally.

---

# EXP293 — COMPLETE / POSITIVE — continuous steady-state runtime remains alarm-free for ~30 minutes

**Date:** 2026-09-29

**Hypothesis:** if the known-good startup/runtime responder continues indefinitely instead of deliberately stopping after ~4 minutes, the Online/Link communication alarm should remain absent during stable operation.

**Baseline:** EXP292 COMPLETE / POSITIVE.

**Controlled change from EXP292:** remove the automatic clean stop/RX-only phase and continue the already proven runtime graph indefinitely. No protocol payload/register change and no semantic write.

**Observed:**
- startup and runtime entered normally;
- the 15-minute marker was reached at ~900.1 s with 43 cycles, 590 runtime events, 625 TX, 0 unexpected events and clean experimental parser/drop deltas;
- the supplied log continued to roughly 30 minutes of steady-state service, reaching at least 84 cycles;
- known conditional branches, including optional post-`0870` `0708`, were serviced;
- no fail-closed termination was present in the captured steady-state run;
- user explicitly confirmed **no `COMM. ERR ONLINE/LINK` alarm** during that run.

A later operation-state-change observation showed that this result must not be generalized to all state transitions: the then-current rigid handler could still fail when the controller omitted additional `0708` mailbox positions.

**Result:** **COMPLETE / POSITIVE for stable steady-state scope.**

---

# EXP292 — COMPLETE / POSITIVE — optional post-0870 0708 branch locally supported

**Date:** 2026-09-29

**Hypothesis:** after `0870/17` ACK, accept either direct `0884/60` or an intervening `FC03 0708/6`, matching genuine XTR/DCM capture evidence.

**Baseline:** EXP291 COMPLETE / INCONCLUSIVE.

**Controlled change from EXP291:** add only the evidence-backed post-`0870` optional `0708/6` branch. No semantic writes; reverse `03E8` remained disabled/capture-only.

**Observed:**
- startup and full runtime completed normally;
- the post-`0870` `0708` branch was exercised locally and serviced;
- continuous service lasted **256.276 s**;
- final counters: **12 cycles**, **169 runtime events**, **204 TX**, **0 unexpected events**;
- experimental resync/drop deltas remained 0;
- TX then stopped deliberately at a clean loop boundary and controller traffic continued RX-only for ~180 s;
- user reported the exact Online/Link communication error appeared shortly after the deliberate stop, with exact delay not precisely timed.

**Result:** **COMPLETE / POSITIVE.**

---

# EXP291 — COMPLETE / INCONCLUSIVE — strict continuity run exposes optional post-0870 mailbox branch

**Date:** 2026-09-29

**Hypothesis:** with semantic writes disabled and only the then-known runtime paths serviced, continuous known-good runtime should remain active long enough to compare alarm behavior before and after a deliberate stop.

**Baseline:** EXP290 COMPLETE / POSITIVE for the separate reverse-page semantic write path; continuity test itself used no semantic write.

**Controlled change:** strict runtime state machine, no `0708 w1=1`, no reverse `03E8` page, no setting change. Planned ~4 minutes active service followed by clean stop and RX-only observation.

**Observed:**
- startup and first full runtime cycle succeeded;
- second cycle progressed through `0848 -> 0708 -> direct 0864 -> direct 0870`;
- after `0870`, controller emitted `FC03 0708/6`;
- handler at that point allowed only `0884`, so it intentionally failed closed after ~38 s of steady-state service;
- genuine XTR/DCM capture evidence independently contains `0870 ACK -> FC03 0708 -> runtime response -> 0884`.

**Result:** **COMPLETE / INCONCLUSIVE.** The intended alarm discriminator was not completed, but the run exposed a valid runtime branch needed by the emulator.

---

# EXP290 — COMPLETE / POSITIVE — reverse 03E8 semantic write changes controller-visible Room Setpoint

**Date:** 2026-09-29

**Hypothesis:** after EXP289 proved acceptance of an unchanged reverse `03E8/14` page, changing only locally mapped `03F4` by +1 in the same-session cached page should be semantically applied by the controller.

**Baseline:** EXP289 COMPLETE / POSITIVE.

**Controlled change:** only `03F4` changed, from current-session cached raw value `22` to `23`. All other 13 words were unchanged. Safety gate required original 15..24 and compressor stopped.

**Observed:**
- current-session `03E8/14` cache captured before the write;
- post-`07E4` `0708/6` answered with `w1=0001`;
- `FC03 03E8/14` arrived 98 ms later;
- reverse page response sent with only `03F4 22->23`;
- first next FC16 was normal runtime `07F8/17` 680 ms later;
- about two seconds later the live `Room Setpoint` sensor reported `23 °C`;
- RX buffer drops remained 0;
- one parser resync occurred at controller bus return before the active transfer.

**Result:** COMPLETE / POSITIVE for controller-visible semantic application. The experiment did not capture an authoritative `FC16 03E8/14` target echo, so that narrower confirmation remains OPEN.

**Do not rewrite this as full round-trip proof:** transport + semantic application are locally demonstrated; authoritative FC16 echo and independent room-sensor-path confirmation are still pending.

---

# EXP289 — COMPLETE / POSITIVE — unchanged reverse 03E8/14 page accepted

**Date:** 2026-09-29

**Hypothesis:** after the EXP288-proven reverse pull, return the exact current-session cached `03E8/14` page unchanged and test whether the controller accepts it.

**Controlled change from EXP288:** respond once to exact `FC03 03E8/14` with the same 28 payload bytes previously captured from the session's own `FC16 03E8/14`.

**Observed:**
- `0708 w1=0001` again caused `FC03 03E8/14` after 98 ms;
- exact unchanged current-session page was returned once;
- controller continued with `FC16 07F8/17` 680 ms later;
- no immediate retry/reject flow.

**Result:** COMPLETE / POSITIVE. Reverse-page response transport acceptance is locally proven.

---

# EXP288 — COMPLETE / POSITIVE — 0708 w1 bit0 triggers local reverse 03E8 pull

**Date:** 2026-09-29

**Hypothesis:** change only post-`07E4` 0708 `w1` from `0000` to `0001`; controller should request heating/settings page `03E8`.

**Controlled change from EXP287:** response changed from `0000 0000 0000 0000 0000 0006` to `0000 0001 0000 0000 0000 0006`.

**Observed:** 98–99 ms after the probe response, local controller sent `FC03 03E8/count14`. Firmware's original matcher expected count13 from genuine capture evidence and therefore labelled the run inconclusive, but the protocol observation itself is positive and locally specific: this XTR uses count14.

**Result:** COMPLETE / POSITIVE for the core hypothesis. `0708 w1 bit0` locally triggers reverse `03E8/14`.

---

# EXP287 — COMPLETE / INCONCLUSIVE — direct 0870 after 0864 exposes second conditional runtime branch

**Date:** 2026-09-29

**Hypothesis:** after cycle-2 `0848 -> 0708`, accept either optional `085F/5 -> ACK -> 0864/4` or direct `0864/4`, then continue the previously assumed `0864 -> 0708 -> 0870` tail.

**Observed:** direct `0864/4` was accepted and ACKed, but controller then emitted direct `0870/17` without the expected intervening `0708`. Firmware stopped fail-closed.

**Result:** COMPLETE / INCONCLUSIVE overall; positive sub-result that direct 0864 branch is valid. Strong conclusion: post-`0864` 0708 is conditional/state-dependent.

---

# THERMIA EXPERIMENT LOG

# 2026-09-29 — EXP286 COMPLETE / INCONCLUSIVE — second full runtime loop hits direct 0864 branch
## Hypothesis
Continue the entire second runtime cycle using only already locally proven actions, then capture the next returned `07D0/19`.

## Controlled change
Relative to EXP285, continue after the already proven cycle-2 `07F8` using the locally proven sequence through the rest of the runtime tail. No new register address, mailbox payload, or semantic write was introduced.

## Observed facts
- Cycle 2 progressed cleanly through `07F8 ACK -> 080C ACK -> 0708 response -> 0820 ACK -> 0848 ACK -> 0708 response`.
- The next controller-originated FC16 was `0864/count4`, not `085F/count5`.
- Firmware stopped fail-closed because EXP286 explicitly required the 085F gate.
- No ACK was sent to that direct `0864`.
- RX drops and parser resyncs remained zero around the test.

## Conclusion
**COMPLETE / INCONCLUSIVE for the exact EXP286 hypothesis.** The failure was not a bus/protocol collapse; it revealed a valid conditional branch. `085F` is not mandatory in every runtime cycle.

---

# 2026-09-29 — EXP285 COMPLETE / POSITIVE — steady-state loop restarts without new approval
## Hypothesis
After the EXP284 loop closure, ACK returned `07D0`, ACK `07E4`, answer the second-cycle `0708`, then capture the next FC03/FC16.

## Observed facts
- `0884 ACK -> 0708 response -> returned 07D0/19`.
- Returned `07D0` ACKed once.
- `07E4/17` followed and was ACKed once.
- Second-cycle `0708/6` was answered with the already proven `0000 ... 0006` response.
- `07F8/17` appeared 616 ms later and was captured.
- No second approval/R1 sequence occurred.
- RX drops and parser resyncs remained zero.

## Conclusion
**COMPLETE / POSITIVE.** The Online/DCM-style runtime sequence re-enters a new cycle without a new approval exchange.

---

# 2026-09-29 — EXP284 COMPLETE / POSITIVE — first runtime loop closes back to 07D0
## Hypothesis
After the proven `0884 ACK -> 0708/6`, answer that 0708 once with the locally proven `0000 ... 0006` response and capture the first next 0x0F FC03/FC16.

## Observed facts
- `0884/60` was valid and ACKed.
- Post-0884 `0708/6` was answered once with `0F030C0000000000000000000000069D76`.
- 571 ms later exact `07D0/count19` appeared.
- `07D0` was capture-only and not ACKed.
- Parser resync and RX-drop counters remained zero.

## Conclusion
**COMPLETE / POSITIVE.** The local runtime tail closes from `0884 -> 0708 -> 07D0`, establishing a complete loop.

---

# 2026-09-29 — EXP283 COMPLETE / POSITIVE — 0884 ACK proven locally
## Hypothesis
Instrument and repair the EXP282 0884 matcher; if exact `0884/count60` has a valid FC16 shape, ACK it once and capture the next `0708/6`.

## Observed facts
- `0884`: start 0884, count 60, bytecount 120, total frame length 129, valid/self-consistent.
- ACK `0F100884003C837F` was transmitted once.
- 1429 ms later exact `FC03 0708/count6` appeared.
- That 0708 was capture-only.

## Conclusion
**COMPLETE / POSITIVE.** `0884/60 ACK -> 0708/6` is locally confirmed.

---

# 2026-09-29 — EXP282 COMPLETE / INCONCLUSIVE — reached 0884 but handler did not ACK
## Observed facts
The local chain reached `0864 ACK -> 0708 response -> 0870/17 ACK -> 0884/60`, but the specialized EXP282 0884 ACK path did not execute. The later 0708 caused fail-closed termination.

## Conclusion
**COMPLETE / INCONCLUSIVE.** Protocol progression to 0884 was positive; the missing ACK was a firmware control-flow/instrumentation problem, not a demonstrated protocol rejection.

---

# 2026-09-29 — EXP281 COMPLETE / INCONCLUSIVE — historical direct-0870 expectation corrected later
## Observed facts
- Preserved path through post-0848 `085F ACK -> 0864/4`.
- ACKed exact `0864/4` once.
- First subsequent 0x0F FC03/FC16 was `FC03 0708/count6`, not the then-expected direct `0870`.
- No response was sent; clean fail-closed stop.

## Historical result and current interpretation
**COMPLETE / INCONCLUSIVE** remains the historical experiment status. Later genuine-capture reanalysis established that `0864 ACK -> 0708 -> 0870` is a valid native ordering, so the observed 0708 is no longer considered evidence of divergence.

---

# 2026-09-29 — EXP280 COMPLETE / POSITIVE — second 085F ACK advances to 0864
- Post-0848 `0708/6` received the proven `0000 ... 0006` response.
- Exact `085F/count5` was ACKed once.
- `0864/count4` appeared ~2.06 s later and was captured without ACK.
**Conclusion:** COMPLETE / POSITIVE.

---

# 2026-09-29 — EXP279 COMPLETE / INCONCLUSIVE — post-0848 response reveals 085F
- Post-0848 `0708/6` was answered once with the locally proven `0000 ... 0006` response.
- Next FC16 was `085F/count5`; payload ended in `0032`, so it was not the earlier all-zero 085F form.
- It was not ACKed.
**Conclusion:** COMPLETE / INCONCLUSIVE; established another 085F stage but not its required handling.

---

# 2026-09-29 — EXP278 COMPLETE / POSITIVE — 0848 ACK advances to post-0848 0708
- Preserved chain through `0820 ACK`.
- ACKed exact local `0848/count23`.
- Exact `FC03 0708/count6` appeared ~1.43 s later and was capture-only.
**Conclusion:** COMPLETE / POSITIVE.

---

# 2026-09-29 — EXP277 COMPLETE / INCONCLUSIVE — local branch is 0848, not expected 0834
- Fixed EXP276 phase-gate bug.
- `post-080C 0708 response -> 0820/18 ACK`.
- Next local FC16 was `0848/count23`, not expected `0834`.
- `0848` was capture-only.
**Conclusion:** COMPLETE / INCONCLUSIVE. The local XTR branch skips 0834 in this observed path.

---

# 2026-09-29 — EXP276 RUNNING / PARTIAL then COMPLETE / INCONCLUSIVE — phase-gate bug
- Post-080C `0708` response successfully caused `0820/18` to appear.
- Intended 0820 ACK code was unreachable because the outer phase gate omitted the new phases.
- Repeated 0820 and later 0708 were observed; parser resyncs occurred around bus return.
**Conclusion:** protocol hint positive, experiment control invalid for the intended ACK test.

---

# 2026-09-29 — EXP275 COMPLETE / POSITIVE — 080C ACK unlocks 0708
- ACKed exact `080C/count18` once.
- Exact `FC03 0708/count6` followed and was captured.
**Conclusion:** COMPLETE / POSITIVE.

---

# 2026-09-29 — EXP274 COMPLETE / POSITIVE — 07F8 ACK unlocks 080C
- ACKed exact `07F8/count17` once.
- `080C/count18` followed and was captured.
**Conclusion:** COMPLETE / POSITIVE.

---

# 2026-09-29 — EXP273 COMPLETE / POSITIVE — post-07E4 0708 response unlocks 07F8
- Answered exact post-07E4 `FC03 0708/count6` once with `0F030C0000000000000000000000069D76`.
- `07F8/count17` followed and was captured without ACK.
**Conclusion:** COMPLETE / POSITIVE.

---

# 2026-09-29 — EXP272 COMPLETE / POSITIVE — 07E4 ACK unlocks post-07E4 0708

## Hypothesis
After EXP271 locally proved `07D0/count19 -> ACK -> 07E4/count17`, a single exact standard ACK of the first `07E4/count17` should advance the XTR M to the next native mailbox request `FC03 0708/count6`.

## Controlled variable
Relative to EXP271, the entire proven path was preserved. The only new active action was one exact ACK of the first `07E4/count17` with:

`0F1007E400114068`.

The following mailbox request was capture-only. No post-`07E4` 0708 response and no later runtime-page ACK were allowed.

## Timeline / observed facts
- BUS_GAP and BUS_RETURN detected normally.
- New local approval challenge:
  `1A094566F90619ACDC1DC5A0001E8FCC`.
- Same fixed historical R1 replay sent:
  `0F17101691A5F3F8E8D58738924416E8E6A3D5E227`.
- Full known FC16 sync reproduced cleanly through `06F4/19`.
- First exact all-zero `085F/count5` was ACKed once with `0F10085F00053356`.
- First early `0708/count6` was answered once with the preserved phase-matched `0080/0006` response.
- `07D0/count19` appeared and was ACKed once with `0F1007D000138067`.
- `07E4/count17` appeared ~2.08 s later.
- EXP272 ACKed `07E4/count17` exactly once with `0F1007E400114068`.
- Exact `FC03 0708/count6` appeared 1457 ms after the 07E4 ACK.
- Firmware logged `SUCCESS_0708_AFTER_07E4_ACK`.
- The post-07E4 0708 request was deliberately not answered.
- Parser resyncs and RX buffer drops remained zero.

## Comparison with EXP271
EXP271 stopped capture-only on `07E4/17`. EXP272 preserved every preceding action and added only one exact 07E4 ACK. The controller then advanced to the next 0708 mailbox poll.

## Strong conclusion
**EXP272 is positive. `07E4/count17` is locally confirmed on the XTR M as an ordered runtime gate whose ACK advances the session to a post-07E4 `FC03 0708/count6` request.**

## Limits
- This does not prove the correct response payload for the post-07E4 0708 poll.
- This does not yet prove progression to `07F8/count17`.
- No semantic desired-state page was served or written.

## Next
EXP273 should change one variable only: answer the proven post-07E4 `0708/count6` once with the exact phase-matched genuine response `0000 0000 0000 0000 0000 0006` / raw `0F030C0000000000000000000000069D76`, then capture `07F8/count17` without ACK.

---

# 2026-09-29 — EXP271 COMPLETE / POSITIVE — 07D0 ACK unlocks 07E4

## Hypothesis
After EXP270 proved the path to first `07D0/count19`, ACKing that exact page once should advance the XTR M to `07E4/count17`.

## Controlled variable
Relative to EXP270, all earlier R1/sync/`085F`/early-`0708` behavior was retained. The only new active action was one exact standard ACK of the first `07D0/count19`:

`0F1007D000138067`.

`07E4/count17` remained capture-only.

## Timeline / observed facts
- BUS_GAP and BUS_RETURN detected normally.
- New local approval challenge:
  `1A094552F90614ACDC1DC594001E8FA4`.
- Same fixed historical R1 replay sent.
- Full known synchronization chain through `06F4/19` completed.
- exact all-zero `085F/count5` was ACKed once.
- early `0708/count6` received the same single preserved `0080/0006` response.
- first `07D0/count19` appeared and was ACKed once with `0F1007D000138067`.
- exact `07E4/count17` appeared 2159 ms after the 07D0 ACK.
- firmware logged `SUCCESS_07E4_AFTER_07D0_ACK`.
- `07E4` was deliberately not ACKed.
- parser resyncs and RX buffer drops remained zero.

## Comparison with EXP270
EXP270 stopped on first `07D0/19` without ACK. EXP271 preserved the complete EXP270 path and added only one exact 07D0 ACK; `07E4/17` then appeared.

## Strong conclusion
**EXP271 is positive. `07D0/count19` is locally confirmed as an ordered runtime gate whose ACK advances the XTR M to `07E4/count17`.**

## Limits
No conclusion is made here about the semantics or payload of 07D0/07E4. Standard FC16 ACKs contain only slave/function/start/count and do not inject the controller-originated page values.

---
# 2026-09-29 — EXP270 COMPLETE / POSITIVE — exact 085F ACK unlocks 07D0

## Hypothesis
The pending exact all-zero `FC16 085F/count5` after the initial synchronization is an ordered gate. ACKing it once should allow the XTR M to continue from the proven `06F4` tail into the first runtime page `07D0/count19`.

## Controlled variable
EXP270 intentionally preserved the EXP269 fixed replay and post-`06F4` mailbox behavior. The only material new active action was a one-shot standard ACK of the first exact all-zero `085F/5`.

## Timeline / observed facts
- BUS_GAP and BUS_RETURN detected normally.
- New local approval challenge:
  `1A004508F90602ACDC1DC5CC001E8F10`.
- The same fixed R1 replay used in prior experiments was sent:
  `0F17101691A5F3F8E8D58738924416E8E6A3D5E227`.
- The complete known FC16 prefix proceeded successfully:
  `03E8 -> 03FC -> 0410 -> 042E -> 0442 -> 0456 -> 046A -> 047E -> 0492 -> 04A6 -> 04BA -> 04D8 -> 04F6 -> 050A -> 051E -> 0532 -> 0546 -> 055A -> 057B -> 059C -> 05BD -> 05DE -> 05FF -> 0620 -> 0641 -> 0662 -> 0683 -> 06A4 -> 06C5 -> 06EA -> 06F1 -> 06F4`.
- `06F4` ACK executed at 00:48:06.727.
- exact all-zero `085F/count5` arrived immediately afterwards and was ACKed exactly once with `0F10085F00053356`.
- first `0708/count6` then arrived; EXP270 returned the same single EXP269 response:
  `0F030C0000000000000000008000069C9E`.
- first `07D0/count19` arrived 509 ms later.
- firmware logged `SUCCESS_07D0_AFTER_085F_ACK`.
- `07D0` was deliberately not ACKed.
- no broad writes/scans were performed.

## Comparison with EXP269
EXP269 used the same single `0080/0006` mailbox response but deliberately ignored the post-`06F4` `085F/5`; no `07D0` followed. EXP270 retained that mailbox response and added one exact 085F ACK; `07D0` appeared.

## Strong conclusion
**EXP270 is positive. The exact all-zero 085F/5 is locally confirmed as an ordered XTR M gate required for progression to the first runtime page.**

## Additional finding
The current 071C challenge differed from the historical challenge corresponding to the replayed R1 frame, yet the controller accepted enough of the session to complete the initial config export and reach `07D0`. Fixed 0730 replay is therefore sufficient at least through this stage; genuine challenge-response semantics remain unresolved.

## Negative/limited findings
- EXP270 does not prove that `0080/0006` is the correct genuine cold-start mailbox state; genuine Eco5 evidence also shows `0100/0000` in this phase.
- EXP270 does not prove full Online/Link session completion or steady-state operation.
- No runtime page beyond `07D0` was tested because 07D0 was intentionally left unACKed.

## Next
EXP271 should change one variable only: ACK first exact `07D0/19` once, then capture first `07E4/17` without ACK.

---

## 2026-09-28 — offline architecture analysis before EXP270

Cross-capture comparison found a likely reverse-direction settings mechanism on slave 0x0F. In the 20260924 genuine DCM capture, the only two shown `0708/count6` replies with word1=`0001` are followed ~39–41 ms later by controller `FC03 03E8/count13` reads. The DCM returns a complete settings page; between the two events only the first word changes `0017 -> 0016`. A separate genuine DCM capture shows the same 13-word page image being written controller -> DCM via `FC16 03E8/count13`.

Interpretation: FC16 likely synchronizes authoritative/current pages controller -> gateway, while FC03 can fetch desired/config pages gateway -> controller. Word1 of 0708 is a strong candidate pending-page/desired-data signal for the 03E8 family. Application semantics remain unproven locally.

## EXP270 — PREPARED / NOT RUN — exact all-zero 085F ACK gate

**Hypothesis:** first `07D0/count19` is blocked locally because exact all-zero `085F/count5` after `06F4` was wrongly ignored in EXP268/269.

Controlled change from EXP269:
- ACK the first exact all-zero `085F/count5` once using `0F10085F00053356`.
- Keep the entire proven pre-06F4 sequence unchanged.
- If 0708 occurs after that ACK before 07D0, use the same single EXP269 `0080/0006` response once only.
- Capture first `07D0/count19` without ACK and terminate.

Negative criteria are also explicit: 0708 before the 085F gate, non-zero 085F payload, 085F ACK safety refusal, repeated 085F without 07D0, timeout after 085F ACK, or 30 s RX-only after the preserved mailbox response with no 07D0.

## 2026-09-28 — deeper full-log analysis of second Eco5 capture

Four power cycles were parsed. Successful challenge replies occurred either around +10 s (request #3) or around +120 s (request #29), but first 03E8 ACK always began around +118.5..120.3 s after bus return. The fast-approval sessions contained 102 repeated unacked 03E8 frames over ~108 s before normal FC16 service began.

085F is now the strongest immediate local clue. In the two sessions where it was still pending after 06F4:
- S2: 06F4 ACK 590.919 -> 085F ACK 590.996 -> 0708 idle 592.311 -> 07D0 592.930.
- S3: 06F4 ACK 888.765 -> 085F ACK 889.309 -> 0708 idle 892.978 -> 07D0 893.603.

In sessions where 085F had already been ACKed shortly before approval, 07D0 followed 06F4 directly in ~78 ms.

Mailbox raw-word correction: the normal idle response is 0000 0000 0000 0000 **0100** 0000. After initial idle replies, the stable script proceeds through 4000/8000/010B and then FFFF/867F/03DF. The 03DF response triggers a new 03E8 within 62–94 ms in all four sessions.

Likely EXP270: reuse EXP268, change only exact 085F/5 handling from ignore to ACK once, retain normal idle 0708 behavior, capture 07D0 without ACK.

## 2026-09-28 — peer analysis of second Eco5 capture

Material new evidence:
- `085F/5` is likely ordered session traffic, not background chatter; in observed successful transitions it is ACKed before first `07D0`.
- If `085F` is already ACKed earlier, `07D0` can follow `06F4` almost immediately; if pending, controller emits `085F` after `06F4`, waits for ACK, then emits `07D0`.
- Post-first-sync mailbox script appears identical across five complete Eco5 sessions, ending in `FFFF 867F 03DF 0000`, which is followed by a second full sync.
- Challenge approval timing and first FC16 ACK timing are decoupled; first FC16 ACK appears ~118 s after bus return in all cited sessions even when challenge approval occurs much earlier.
- Six challenge/response pairs now available; no simple XOR/difference relation identified.

Next experimental focus should be the `085F` queue prerequisite before any further mailbox-payload exploration.

## 2026-09-28 — external Eco5 capture review (no new local experiment)

Major result from new genuine Eco5 gateway capture:
- successful dynamic `071C/0730` response is followed by `03E8 -> ... -> 06F4`;
- `07D0/19` follows `06F4/19` directly (~78 ms) before the next `0708/6` mailbox poll;
- therefore EXP269 tested the wrong causal hypothesis: mailbox payload `0080/0006` is not required to unlock the first `07D0` in this successful session;
- later `0708/6` idle replies (`0001/0000`) are interleaved with `07E4, 07F8, 080C, 0820, 0834, 0848, 0864, 0870, 0884`.

The capture also provides four distinct successful `071C` challenge -> 16-byte response pairs. Responses differ with the challenge, strongly supporting a dynamic challenge-response mechanism.

Project implication: next work should target the approval/session mechanism rather than additional mailbox-payload variants.

### EXP269 UI observation
Post-test display photo confirms a visible change in the lower-right status area: user reports the center of the `0`/status glyph is now filled. Alarm remains active. Treat as a UI/state side effect only; semantic meaning unknown and not evidence of successful Online session completion.

## EXP269 — COMPLETE / NEGATIVE

Hypothesis: one exact Eco5 phase-matched first post-`06F4` mailbox response `0000 0000 0000 0000 0080 0006` would cause the XTR to continue with `07D0/19`.

Observed:
- proven prefix through `06F4/19` completed cleanly;
- first `0708/6` at +1.566 s;
- one exact `0080/0006` response sent;
- no `07D0/19`;
- repeated `0708/6` began ~4.43 s later and continued;
- 30 s RX-only completed;
- summary: `responses_sent=1 mailbox_requests=8 ignored_bg=15 resync_postreturn=0 drop_postreturn=0 DE=LOW`;
- only recurrent post-`06F4` FC16 family was `085F/5`;
- A80E moved `0008 -> 0028`, AFDC to `32`;
- user reports a visible UI change (“middle of the 0 is now filled”), semantic meaning unknown.

Conclusion: valid negative. The phase-matched Eco5 `0080/0006` response is not sufficient on its own to reproduce the Eco5 `07D0` transition.

---
## EXP269 — PREPARED / NOT RUN — revised phase-matched mailbox test

Hypothesis: the first post-`06F4` XTR mailbox must receive the same phase-specific payload seen in the matching Eco5 startup trace.

Sequence: proven approval/sync prefix through `06F4/19` -> first exact `0708/6` -> send exactly once `0F030C0000000000000000008000069C9E` (words `0000 0000 0000 0000 0080 0006`) -> RX-only up to 30 s.

Primary success criterion: capture `07D0/19`, with no ACK. Repeated `0708/6` is a negative/non-progress signal and receives no second response. No other new active traffic is introduced.

The earlier EXP269 design using up to ten `0001/0000` replies remains SUPERSEDED / NOT RUN.

---
## EXP269 — PREPARED / NOT RUN

## ECO5 raw-log review after EXP268

Direct raw-log comparison changes the interpretation of the next test. In Eco5 capture `090209`, the first mailbox after `06F4/19` is answered with words `0000 0000 0000 0000 0080 0006`, after which `07D0/19` follows ~0.7 s later. Later mailbox replies with fifth word 0 and sixth word `0006` are interleaved with `07E4/17, 07F8/17, 080C/18, 0820/18, 0834/18, 0848/23, 0864/4, 0870/17, 0884/60`.

Therefore EXP269 as previously prepared (10 repetitions of `0001 0000`) is **SUPERSEDED / NOT RUN**. The next active experiment must test the exact phase-matched Eco5 first post-`06F4` response, not a larger count of the wrong payload.


Hypothesis: because EXP268 stopped answering the persistent `0708/6` mailbox after response #3, later parallel runtime traffic may have been prevented or delayed. EXP269 changes only the maximum service count from 3 to 10 exact `0708/6` idle responses using the same genuine Eco5 frame `0F030C0000000000000000010000001C88`. Proven prefix and safety gates remain unchanged. After response #10, observe RX-only for 30 s. Any different non-background FC16 or different FC03 is capture-only; no post-mailbox FC16 ACK and no eleventh mailbox response.

## EXP268 — COMPLETE / NEGATIVE

Hypothesis: after three bounded idle mailbox responses, later FC16/runtime traffic may appear during 30 s RX-only even though `0708/6` continues polling.

Observed:
- proven prefix through `06F4/19` completed again;
- one CRC resync occurred at BUS_RETURN, with post-return resync delta 0 and RX-drop delta 0 at summary;
- first `0708/6` arrived +3.621 s after `06F4` ACK;
- responses #1..#3 used the exact genuine Eco5 idle frame;
- after response #3, 30 s RX-only completed;
- mailbox requests reached 10 total, i.e. 7 more exact `0708/6` polls were observed unanswered;
- 21 recurrent `085F/5` background frames were counted after `06F4`;
- no different non-background FC16, no different FC03, and none of `07D0..0864` appeared;
- DE LOW at summary.

Conclusion: negative for the 30 s RX-only progression hypothesis. Persistent `0708/6` polling continues normally, but no later runtime family appeared while mailbox service was stopped after three replies.

---

## EXP267 — COMPLETE## EXP267 — COMPLETE## EXP267 — COMPLETE / NEGATIVE

Hypothesis: up to three consecutive exact `FC03 0708/count6` polls require the same genuine Eco5 idle response before the controller progresses.

Observed:
- proven prefix through `06F4/19` completed again;
- first `0708/6` arrived +1.561 s after `06F4` ACK;
- response #1 sent: `0F030C0000000000000000010000001C88`;
- response #2 sent after the repeated `0708/6`;
- response #3 sent after the next repeated `0708/6`;
- a fourth exact `0708/6` arrived ~4.18 s after response #3 and was deliberately not answered;
- no different meaningful FC03/FC16 appeared before the fourth poll;
- recurrent `085F/5` background traffic continued between mailbox polls;
- parser resyncs remained 0 and RX drops remained 0 in the observed run.

Conclusion: valid negative. Three identical genuine Eco5 idle mailbox responses do not cause immediate local XTR progression out of the observed `0708/6` polling phase. The repeated ~4.2 s cadence now looks more like normal ongoing mailbox service than a malformed-response retry.

---

## EXP267 — PREPARED / NOT RUN

Hypothesis: up to three consecutive exact `FC03 0708/count6` polls require the same genuine Eco5 idle response before the controller progresses. Only this repetition count changes from EXP266. Exact response: `0F030C0000000000000000010000001C88`. Max 3 TX; fourth poll is capture-only.

## EXP266 — COMPLETE / PARTIAL POSITIVE

Hypothesis: answer the first exact post-`06F4` `FC03 0708/count6` once with the genuine Eco5 idle mailbox frame `0F030C0000000000000000010000001C88`, then capture only.

Result:
- Proven prefix through `06F4/19` succeeded again.
- Background `085F/5` ignored at +95 ms.
- First `0708/6` at +1.561 s was answered exactly once with the genuine Eco5 idle response.
- Same `0708/6` repeated +4.180 s after the response; no second response sent.
- Parser resyncs 0; RX drops 0.

Conclusion: one idle mailbox response is insufficient to complete the local mailbox phase. Negative result recorded.

---

## EXP266 — PREPARED / NOT RUN

**Hypothesis:** respond once to the first exact locally proven post-`06F4/19` mailbox request `FC03 0708/count6` using the genuine Eco5 idle response `0F030C0000000000000000010000001C88`, then observe RX-only.

**Delta from EXP265:** replaces passive capture of `0708/6` with a single tightly gated response. The complete proven prefix is otherwise unchanged. No response to any other FC03, no repeated mailbox response, no post-mailbox FC16 ACK.

**Expected success signal:** after the one mailbox response, a new meaningful FC16/runtime frame or other FC03 appears without approval retry, parser/drop delta, or immediate 0708 retry.

**Negative result criteria:** repeated 0708, parser/drop delta, unexpected peer traffic, no meaningful post-mailbox frame within 10 s, or UI/controller side effect requiring recovery.

## EXP264 — 06EA/06F1/06F4 tail — COMPLETE / STRONG POSITIVE WITH CAPTURE AMBIGUITY

Hypothesis: ACK exact `06EA/7`, `06F1/3`, `06F4/19` in order after the proven prefix, then capture only.

Observed:
- `06EA/7` ACKed once.
- `06F1/3` followed and was ACKed once.
- `06F4/19` followed and was ACKed once.
- First post-`06F4` frame: `085F/5`, +107 ms, not ACKed.
- `085F/5` is a previously established recurrent passive/background family; therefore this is a capture artifact/overlay, not proof of the next ordered sync stage.
- One CRC resync occurred at bus return before the experiment chain; RX drops 0.
- No approval retry, no stage retry, no peer FC17/ACK anomaly.

Result: strong positive for the three tail ACKs; inconclusive for the next meaningful stage because the first-frame capture policy stopped on known background traffic.

## EXP264 — end-of-bulk sync tail — PREPARED / NOT RUN

Hypothesis: preserve the complete proven prefix through `06C5/33`, then ACK exact `06EA/7`, `06F1/3`, and `06F4/19` once each. After `06F4` ACK, capture the first different FC16 or FC03 and do not answer it. A `0708/6` FC03 is logged specifically but never answered in EXP264.

Negative/stop criteria: retry of the previous stage, unexpected FC16, any FC03 before tail completion, parser resync delta, RX drop delta, approval retry, peer FC17/ACK, or >5 s stage timeout.

## EXP263 — accelerated 12-block 33-word batch — COMPLETE / STRONG POSITIVE

Hypothesis: after the proven prefix through 0546/count20, ACK exact 055A, 057B, 059C, 05BD, 05DE, 05FF, 0620, 0641, 0662, 0683, 06A4 and 06C5 (all count=33), then capture only. Genuine Eco 5 predicted 06EA/count7.

Observed:
- Approval +1283 ms after controller return; R1 sent once.
- All twelve 33-word pages appeared in the expected order and were ACKed exactly once.
- First different post-06C5 frame: 06EA/count7, +475 ms after 06C5 ACK.
- Raw 06EA request: 0F1006EA00070E000A00200017001B0009001A0006F81A.
- 06EA not ACKed.
- Parser resyncs 0; RX buffer drops 0 after the run; DE LOW.
- No approval retry after R1 and no stage retry observed.

Conclusion:
Local XTR now confirms the genuine Eco 5 synchronization chain through the complete 055A..06C5 33-word run and exact 06EA/count7 next. Full Online/Link establishment remains unproven. Negative result retained: the session was intentionally stopped before 06EA ACK, so runtime/mailbox completion was not tested.

Recovery: one normal Thermia-controller reboot.

## EXP262 — accelerated 04A6..0546 ACK batch — COMPLETE / STRONG POSITIVE

Hypothesis: after the proven prefix through `0492/11`, ACK exact `04A6/13`, `04BA/22`, `04D8/27`, `04F6/14`, `050A/19`, `051E/10`, `0532/18`, and `0546/20` in order, then capture the first different FC16/FC03 without answering it.

Observed result: all eight new stages appeared in the predicted order and were ACKed exactly once. The first different frame after the `0546/20` ACK was exact `055A/count33`, +637 ms later, raw `0F10055A002142000000000000001F000C000000000000001F000C00000000000000000000001F000C000000000000001F000C00000000000000000000001F000C000000000000001FF26A`. No ACK was sent to `055A`.

Negative/clean results: no approval retry after R1; no acknowledged-stage retries observed; parser resyncs remained 0; RX buffer drops remained 0.

Conclusion: accelerated batching is confirmed workable through `0546/count20`, and the local XTR follows the genuine Eco 5 sync path through `055A/count33`. Full Online/Link remains unproven. Recovery: one normal controller reboot.


## EXP262 — accelerated 04A6..0546 batch — PREPARED / NOT RUN

Hypothesis: after the proven local Online/Link prefix through `0492/count11`, ACK a bounded batch of eight exact FC16 pages: `04A6/13`, `04BA/22`, `04D8/27`, `04F6/14`, `050A/19`, `051E/10`, `0532/18`, `0546/20`; then capture the first different FC16/FC03 without responding. Genuine Eco 5 predicts `055A/count33`.

Safety: all pages are exact known controller-originated FC16 export requests. EXP262 sends only standard address/count acknowledgements. Every stage is first-exact, time-bounded and parser-clean; unexpected traffic stops fail-closed. No FC03/mailbox response and no ACK after `0546`. Known incomplete-session recovery remains one normal controller reboot.


## EXP261 — bounded 046A/047E/0492 ACK batch — COMPLETE / STRONG POSITIVE

**Hypothesis:** after the proven local prefix, ACK exact `046A/count18`, then exact `047E/count19`, then exact `0492/count11`, and capture the first different FC16/FC03 stage without answering it.

**Observed facts:**
- first approval at +1245 ms after BUS_RETURN;
- R1 accepted with no approval retry;
- the proven prefix through `0456/count12` reproduced cleanly;
- `046A/count18` appeared and was ACKed once;
- `047E/count19` followed +722 ms later and was ACKed once;
- `0492/count11` followed +1480 ms later and was ACKed once;
- the first different block was exact `04A6/count13`, +576 ms after the 0492 ACK;
- raw `04A6` request: `0F1004A6000D1A0000000000000000000000000000000000000000402000000000CA9A`;
- `04A6` was not ACKed;
- no stage retries, no approval retry after R1, no unexpected peer frame, no post-return parser/RX-drop delta; DE LOW.

**Strong conclusion:** local XTR follows the genuine Eco 5 ordered synchronization path through `0492/count11`, with `04A6/count13` next in this run. The bounded-batch strategy remains valid.

**Unknown:** full Online/Link establishment and mailbox behavior remain unproven.

**Recovery:** one normal Thermia-controller reboot after the summary.


## EXP261 — bounded `046A -> 047E -> 0492` continuation — PREPARED / NOT RUN

**Hypothesis:** the local XTR continues to follow the genuine Eco 5 Online/Link FC16 sequence after EXP260. Preserve the complete proven prefix and ACK exactly three new expected stages: `046A/count18`, `047E/count19`, and `0492/count11`. Then capture the first different FC16/FC03 without answering it.

**New ACKs:** `046A/18 -> 0F10046A00126006`; `047E/19 -> 0F10047E0013E1C2`; `0492/11 -> 0F100492000B203D`.

**Primary prediction:** `04A6/count13` is the genuine Eco 5 next-page observation, but because `04A6/13` is also known as a recurrent passive family it is recorded as a prediction rather than a strict required success value.

**Safety:** same cold-boot approval guard and proven prefix as EXP260; first-exact-stage-only, <=5 s between ACKs, no retries, parser/drop counters unchanged, no unexpected peer frames. After `0492` ACK, capture only. No FC03 response. Controller reboot after summary.


## EXP260 — bounded `042E -> 0442 -> 0456` ACK batch — COMPLETE / STRONG POSITIVE

**Hypothesis:** after the locally proven prefix through `042E/count15`, ACK exactly `042E/15`, `0442/13`, and `0456/12` in order, then stop and capture the next different frame. Genuine Eco 5 predicts `046A/count18`.

**Observed facts:**
- first approval request at +1284 ms after BUS_RETURN; R1 sent once;
- `03E8/14` arrived +126 ms after R1 and was ACKed once;
- `03FC/11` arrived +694 ms after the `03E8` ACK and was ACKed once;
- `0410/22` arrived +1492 ms after the `03FC` ACK and was ACKed once;
- `042E/15` arrived +695 ms after the `0410` ACK and was ACKed once;
- `0442/13` arrived +1502 ms after the `042E` ACK and was ACKed once;
- `0456/12` arrived +566 ms after the `0442` ACK and was ACKed once;
- predicted `046A/count18` arrived +1473 ms after the `0456` ACK; it was captured and not ACKed.
- summary: approval retries after R1=0; all stage retry counters=0; peer17=0; unexpected peer ACK=0; post-return resync/drop deltas=0; DE LOW.

**UI side effect:** user reports the DHW-side literal `0` appeared again. No EXP260 `COMM. ERR ONLINE/LINK` confirmation yet. Recovery should be performed immediately after the summary rather than waiting for an alarm.

**Strong conclusion:** the bounded batching strategy is validated locally through `046A/count18` and preserves the same ordered sequence as the genuine Eco 5 reference.

Last updated: 2026-09-27

## EXP260 — bounded `042E -> 0442 -> 0456` ACK batch — PREPARED / NOT RUN

**Hypothesis:** continue the already-proven local Online/Link prefix in one bounded batch. After the proven EXP259 prefix, ACK exact `042E/count15`, then exact `0442/count13`, then exact `0456/count12`. The genuine Eco 5 reference predicts `046A/count18` next.

**New active variable family:** three exact standard FC16 ACKs: `0F10042E000FE01A`, `0F100442000DA1C6`, `0F100456000C2002`. Each is one-shot and only allowed after the preceding exact stage.

**Safety/stop rule:** any deviation, retry, FC03, unexpected peer response, parser/RX-drop delta, or >5 s missing expected stage stops the experiment immediately. After the `0456` ACK, capture the first different FC16/FC03 only; no `046A` ACK and no mailbox response.

**Known recovery:** deliberately incomplete Online/Link sessions have repeatedly produced DHW-side `0` and `COMM. ERR ONLINE/LINK`; reboot controller once after the summary.

## EXP259 — ACK `0410/count22`, capture next stage — COMPLETE / STRONG POSITIVE

**Hypothesis:** after the proven prefix `R1 -> 03E8/14 ACK -> 03FC/11 ACK -> 0410/22`, one exact FC16 ACK to `0410/count22` should advance the XTR to the next ordered sync block. Genuine Eco 5 predicted `042E/count15`.

**Observed:**
- approval at +1283 ms after BUS_RETURN;
- R1 once;
- `03E8/14` +138 ms after R1, ACKed once;
- `03FC/11` +682 ms after `03E8` ACK, ACKed once;
- `0410/22` +1498 ms after `03FC` ACK, ACKed once;
- `042E/15` +696 ms after `0410` ACK;
- `042E/15` not ACKed;
- `approval_after_r1=0`, `same03e8_after_ack=0`, `same03fc_after_ack=0`, `same0410_after_ack=0`;
- `peer17=0`, `unexpected_peer_ack=0`, `self_echo_r1=0`, `self_echo_ack=0`;
- `resync_postreturn=0`, `drop_postreturn=0`, `DE=LOW`.

**Result:** strong positive. Local XTR matches the genuine Eco 5 ordered sync prefix through `042E/count15`.

**Negative/safety result:** full Online/Link session is still not established; no `042E` ACK, no later FC16 ACK, and no FC03/mailbox response was emitted.

---

## EXP259 — UI side effect follow-up

After the successful protocol result, the user confirmed the same visible side effects seen in earlier incomplete Online/Link sessions: DHW-side literal `0` and exact `COMM. ERR ONLINE/LINK`. This is a repeated positive observation, not a new protocol stage.

Interpretation: the association between partial Online/Link servicing and the communication alarm is now reproducible across multiple active runs. The specific causal mechanism remains a hypothesis until a sufficiently complete session is shown to avoid the alarm. Recovery remains one normal controller reboot.


## EXP259 — exact `0410/count22` ACK then next-stage capture — PREPARED / NOT RUN

**Hypothesis:** after the locally proven prefix `R1 -> 03E8/14 ACK -> 03FC/11 ACK -> 0410/22`, one exact standard FC16 ACK to `0410/count22` should advance the XTR controller to a different block. The genuine Eco 5 reference predicts `042E/count15`.

**Only new active variable:** one ACK frame `0F1004100016401C` for exact slave `0x0F` FC16 `start=0410`, `count=22`, `bytecount=44`, request length `53`. The ACK carries no register-value payload.

**Safety:** R1, `03E8` ACK and `03FC` ACK retain the existing guards. The new `0410` ACK is one-shot, latch-before-DE, allowed only on the first exact post-`03FC`-ACK `0410/22` within 5 s with clean parser/drop counters and no approval/03E8/03FC retry or unexpected peer. After that, capture-only: no `042E` ACK, no later FC16 ACK, no FC03/mailbox response. Reboot controller after summary.

**Expected positive discriminator:** first post-`0410`-ACK block is `042E/count15`. Any other different FC16/FC03 is still recorded as a protocol result.

---

## EXP258 — exact `03FC/count11` ACK then next-stage capture — COMPLETE / STRONG POSITIVE

**Hypothesis:** after the locally proven `R1 -> 03E8/count14 ACK -> 03FC/count11`, one exact standard ACK to `03FC/count11` should advance the XTR to a different block. Genuine Eco 5 predicts `0410/count22`.

**Observed facts:** first approval +1243 ms after BUS_RETURN; R1 exactly once; `03E8/14` +138 ms after R1 and ACKed once; `03FC/11` +691 ms after the 03E8 ACK and ACKed once; `0410/22` appeared +1501 ms after the 03FC ACK and was not ACKed. No approval retry, no 03E8 retry, no 03FC retry, no unexpected peer frame, no post-return parser/drop delta; DE LOW at summary. User reports DHW-side `0` and the same `COMM. ERR ONLINE/LINK` alarm again.

**Exact result chain:** `R1 -> 03E8/14 -> ACK -> 03FC/11 -> ACK -> 0410/22 -> STOP`.

**Strong conclusion:** the first three ordered post-approval FC16 sync stages on the local XTR match the genuine Eco 5 sequence.

**Unknowns:** full session completion, later FC16 ordering on XTR, and mailbox behavior remain unproven. The repeated alarm is consistent with an incomplete approved session but is not yet proven to be caused specifically by the missing downstream ACK/mailbox service.

**Recovery:** one normal controller reboot before any further active test.

This file is the canonical experiment record. The compact table below indexes the early experiment series; EXP100+ are documented in the detailed chronological sections that follow. Detailed YAML and raw logs remain the primary evidence.

## EXP258 — exact `03FC/count11` ACK then next-stage capture — PREPARED / NOT RUN

**Hypothesis:** after the already-proven local prefix `R1 -> 03E8/count14 ACK -> 03FC/count11`, one exact standard FC16 ACK to `03FC/count11` should advance the XTR controller to a different block. The genuine Eco 5 reference predicts `0410/count22`.

**Only new active variable:** one ACK frame `0F1003FC000B4094` for exact slave `0x0F` FC16 `start=03FC`, `count=11`, `bytecount=22`, request length `31`. The ACK carries no register-value payload.

**Safety:** R1 and the `03E8` ACK retain the EXP257 guards. The new `03FC` ACK is one-shot, latch-before-DE, permitted only on the first exact post-`03E8`-ACK `03FC/11` within 5 s with clean parser/drop counters and no approval retry, `03E8` retry, or unexpected peer. After that, capture-only: no `0410` ACK, no later FC16 ACK, no FC03/mailbox response. Reboot controller after summary.

**Expected positive discriminator:** first post-`03FC`-ACK block is `0410/count22`. Any other different FC16/FC03 is still recorded as a protocol result.


## Post-EXP257 external Eco 5 follow-up — raw-log verified

No new local experiment was run. New external interpretation was checked against the complete public Eco 5 raw capture.

Observed facts:
- first cold-start approval request at +1.199/+1.202/+1.210 s after bus return in the three Eco 5 power-ups;
- successful genuine gateway responses at +120.153 s and +119.808 s after bus return, after 29 challenges each;
- middle no-gateway run ended by power-off at ~174 s and therefore cannot test a ~267 s natural cutoff;
- steady-state pre-power-off segment contains no approval exchange; Eco 8 steady-state absence must therefore remain open pending a cold-start capture;
- only two answered Eco 5 challenges exist, so repeated-challenge response determinism and cross-power-cycle response stability are unresolved;
- genuine endpoint continues ACKing the FC16 export stream after approval; `04A6/13` and `085F/5` are recurrent passive families whose ACK timing varies and is not a demonstrated precondition;
- first post-approval `0708/count6` mailbox polls occur at +158.393 s and +186.828 s after bus return, while the FC16 transfer is still active;
- in the first successful power-up the first mailbox poll is unanswered and the following poll is answered;
- the raw repeated idle response is six words `0000 0000 0000 0000 0001 0000` (not `...0100...` under standard Modbus word order);
- later fifth-word values include `03DC`=988 -> 984 -> 976 -> 908 -> 896 -> 768 -> 512 -> 0.

Interpretation/hypothesis:
- `COMM. ERR ONLINE/LINK` being a timeout of an approved-but-incompletely-serviced session is increasingly plausible but remains unproven;
- the fifth-word countdown may represent pending synchronization work, but no semantic mapping is established.

Decision:
- do not broaden directly to full-chain ACK + mailbox emulation;
- next candidate is **EXP258 (not prepared)**: add exactly one `03FC/count11` ACK after the already-proven EXP257 prefix and capture the first subsequent frame; genuine Eco 5 predicts `0410/count22`.


## EXP257 — One-shot R1 + single `03E8/count14` ACK + next-stage capture — COMPLETE / STRONG POSITIVE

**Hypothesis:** after EXP256's one-shot R1 transition into `03E8/count14`, acknowledge exactly the first `03E8/count14` once and capture the first different downstream FC16/FC03 request without answering it. Full genuine Eco 5 capture predicted `03FC/count11`.

**Observed facts:**
- controller cold-restart gap detected and clean `BUS_RETURN`;
- boot-only `04BA/count22` appeared at +316 ms after BUS_RETURN;
- first approval request at **+1285 ms**, `W071C=1A154568F9061AACDC1BC564001E8FD0`;
- exact R1 transmitted once; DE returned LOW;
- first post-R1 FC16 was exact `03E8/count14`, **+130 ms after R1**;
- exact standard ACK `0F1003E8000EC093` transmitted once; ACK latch closed before DE;
- first different post-ACK request arrived **+691 ms after ACK** and was exact `03FC/count11`, bytecount 22, length 31;
- raw `03FC` request: `0F1003FC000B160028000A0037000000000000000200120028001E003C369E`;
- payload words: `0028 000A 0037 0000 0000 0000 0002 0012 0028 001E 003C`;
- no ACK was sent to `03FC`;
- summary: `r1=1 ack03e8=1 approvals=1 approval_after_r1=0 post_r1_fc16=1 same03e8_after_ack=0 peer17=0 unexpected_peer_ack=0 self_echo_r1=0 self_echo_ack=0 resync_postreturn=0 drop_postreturn=0 DE=LOW`.

**Strong conclusions:**
- EXP257 satisfies its positive criterion.
- The XTR reproduces the genuine Eco 5 post-approval prefix `R -> 03E8/14 -> ACK -> 03FC/11`.
- The `03E8` ACK is sufficient to advance the local XTR one synchronization block.
- This substantially strengthens the interpretation that R1 enters the genuine Online/Link synchronization state machine rather than an unrelated failure state.
- Full Online/Link establishment remains unproven because `03FC` and all later stages were intentionally not acknowledged.

**Comparison with external reference:** the genuine Eco 5 capture proves twice that `03FC/count11` follows the acknowledged `03E8/count14`, and that acknowledged `03FC/count11` is followed by `0410/count22`. EXP257 reproduces the first of those transitions locally.

**Unknowns:**
- whether one exact ACK to local `03FC/count11` yields `0410/count22`;
- whether the remainder of the XTR synchronization ordering matches the Eco 5 chain;
- when `0708/count6` mailbox traffic starts locally;
- UI side effect for this run, pending user report.

**Safety/recovery:** no further ACKs were sent. One normal controller reboot is required after the incomplete session if not already performed.

## EXP256 — One-shot R1 + full post-R1 FC16/FC03 differential census — COMPLETE / ACTIVE STRONG POSITIVE

**Hypothesis:** the already-tested R1 changes the local XTR native FC16 distribution; leading pre-run hypothesis was selective suppression of `085F/count5` while `04A6/count13` persisted.

**Observed facts:**
- clean >=6 s controller bus gap and BUS_RETURN;
- first exact `071C/0730` approval request at **+1245 ms**; local `W071C=1A144532F9060CACDC1BC590001E8F64`, local schema check `RTC=OK`;
- exactly one R1 frame transmitted; DE returned LOW and one-shot latch stayed closed;
- approval requests **1**, retries after TX **0**;
- FC16 requests **390**, FC16 ACKs **0**;
- FC03 `0708/count6` **0**, other FC03 **0**;
- peer FC17 response **0**, self-echo **0**;
- complete FC16 census: `04BA/count22` = **1**, `03E8/count14` = **389**, `04A6/count13` = **0**, `085F/count5` = **0**;
- first `03E8/count14` at **+1369 ms after BUS_RETURN / +124 ms after R1**; last at **+419896 ms**; median `03E8` retry interval ~**1308 ms**;
- final state `A80E=0028 A80F=000A AFDC=0010`;
- post-return `resync_delta=0`, `drop_delta=0`;
- user reports the DHW/tank-side literal `0` reappeared; VERSION screen did not change; after summary the controller again raised **`COMM. ERR ONLINE/LINK`**, exactly matching EXP252.

**Strong conclusions:**
- R1 again suppresses all later approval retries.
- The pre-run H1 is falsified: R1 does **not** leave the passive `04A6/count13` stream intact while merely removing `085F/count5`. Both passive runtime families disappear.
- R1 instead advances the controller into the first known `0x0F` settings synchronization block, `03E8/count14`.
- Because EXP256 intentionally sent no FC16 ACK, the controller remained stalled retransmitting `03E8/count14` for the rest of the seven-minute observation.
- The prior EXP252 total `fc16req=386` is now best explained as likely the same unclassified `03E8` retransmission state, rather than the previously suspected passive-family remainder.

**Hypothesis / interpretation:** R1 is accepted at least far enough to cross the approval boundary and enter controller->Online/Link synchronization. This is not yet proof of a fully established Online/Link session because the expected endpoint transfer ACKs and any later FC03/mailbox phase were deliberately absent.

**Unknowns:**
- whether ACKing the exact first `03E8/count14` after R1 yields the same `0410/count22` next stage seen in earlier acknowledged-transfer experiments, or a different post-approval sequence;
- how far the synchronization chain proceeds before an additional service/mailbox response is required;
- exact semantics of the reproduced DHW-side `0`.

**Safety/recovery:** one normal controller reboot is required after the summary, matching the run plan and the known recoverable EXP252 side effect. No second active approval/sync test until normal UI recovery is confirmed.


### EXP141 — gated 0x0F sequence walker — PREPARED

Hypothesis:
Multiple additional controller-side 0x0F sync stages can be discovered in one run without reflashing, while retaining explicit approval for every newly observed FC16 start/count pair.

New automatic target:
- `05FF/count33` (locally proven by EXP140).

Unknown-stage gate:
1. observe exact start/count at least 3 times;
2. log full payload;
3. lock candidate;
4. operator presses `EXP141 ARM ACK Current Candidate Once`;
5. no asynchronous TX occurs;
6. next exact matching request receives one standard FC16 ACK;
7. continue to next unknown stage.

Limits/guards:
- max 8 manually approved stages;
- no FC03 response;
- no semantic value injection;
- abort on real 0x0F responder, parser resync, or RX drop.


### EXP141 — gated 0x0F sequence walker — RUNNING / PARTIAL POSITIVE

Observed:
- baseline: repeated known `05FF/count33`;
- active phase ACKed `05FF/count33`;
- new block appeared ~1.56 s later: `0662/count33`;
- exact payload repeated consistently;
- candidate locked after 3 exact start/count observations;
- no `ARM_OK` or manual-stage ACK appears in the supplied log, so the controller remained retrying `0662/count33`;
- no parser resync, RX drop, FC03, or real 0x0F responder activity in the shown run.

New proven progression:
`05FF/33 -> ACK -> 0662/33`.

Current action:
Press `EXP141 ARM ACK Current Candidate Once` while the walker remains active.


#### EXP141 continuation — 0662/33 ACKed

### EXP140 — sequential 0x0F FC16 ACK probe, stage 0x04BA — PREPARED

Hypothesis:
ACKing the locally proven next-stage request `04BA/count22` will advance the controller to a subsequent 0x0F transfer stage or to an FC03 read phase.

Only change versus EXP139:
- add `04BA/count22` to the ACK whitelist.

Safety:
No register values are injected, FC03 is never answered, unknown next-stage FC16 shapes are logged but not ACKed, and TX stops immediately on the first positive discriminator.


### EXP140 — sequential 0x0F FC16 ACK probe, stage 0x04BA — COMPLETE / POSITIVE TRANSPORT PROGRESSION

Observed:
- controller resumed/retried `04BA/count22` throughout the passive baseline after ESP reboot;
- first active `04BA/count22` was ACKed;
- ~0.65 s later new `05FF/count33` appeared;
- new block was not ACKed and test stopped;
- final summary:
  `reason=POSITIVE_NEW_FC16_STAGE_AFTER_04BA duration_ms=31011 fc16Seen=30 whitelisted=29 unknown=1 ackTx=1 txRefused=0 fc16AckSeen=0 fc03Req=0 fc03Resp=0 existingResponder=NO resyncDelta=0 dropDelta=0 DE_LOW`.

Conclusion:
Locally observed sequence now extends to:
`03E8/14 -> ACK -> 0410/22 -> ACK -> 042E/15 -> ACK -> 04A6/13 -> ACK -> 04BA/22 -> ACK -> 05FF/33`.

Next:
EXP141 adds only `05FF/count33` to the ACK whitelist.


### EXP139 — sequential 0x0F FC16 ACK probe, stage 0x042E — PREPARED

Hypothesis:
ACKing the locally proven next-stage request `042E/count15` will advance the controller to a subsequent 0x0F transfer stage or to an FC03 read phase.

Only change versus EXP138:
- add `042E/count15` to the ACK whitelist.

Safety:
No register values are injected, FC03 is never answered, unknown next-stage FC16 shapes are logged but not ACKed, and TX stops immediately on the first positive discriminator.


### EXP139 — sequential 0x0F FC16 ACK probe, stage 0x042E — COMPLETE / POSITIVE TRANSPORT PROGRESSION

Observed:
- controller resumed/retried `042E/count15` throughout the passive baseline after ESP reboot;
- first active `042E/count15` was ACKed;
- ~0.52 s later `04A6/count13` appeared and was ACKed under the unchanged prior whitelist;
- ~1.55 s after that, new `04BA/count22` appeared;
- new block was not ACKed and test stopped;
- final summary:
  `reason=POSITIVE_NEW_FC16_STAGE_AFTER_042E duration_ms=32936 fc16Seen=31 whitelisted=30 unknown=1 ackTx=2 txRefused=0 fc16AckSeen=0 fc03Req=0 fc03Resp=0 existingResponder=NO resyncDelta=0 dropDelta=0 DE_LOW`.

Conclusion:
Locally observed sequence is now:
`03E8/14 -> ACK -> 0410/22 -> ACK -> 042E/15 -> ACK -> 04A6/13 -> ACK -> 04BA/22`.

Nuance:
`04A6/13` was already known from earlier passive XTR captures and was already whitelisted, so EXP139 does not prove it is exclusively sequence-owned. It is nevertheless an observed intermediate stage in this run.

Next:
EXP140 adds only `04BA/count22` to the ACK whitelist.


### EXP138 — sequential 0x0F FC16 ACK probe — PREPARED
Hypothesis: after EXP137's proven progression `03E8/count14 ACK -> 0410/count22`, ACKing only `0410/count22` as the one new variable will reveal the next controller stage.

Only change versus EXP137:
- add `0410/count22` to the ACK whitelist.

Positive:
- first previously unseen FC16 shape after a successful 0410 ACK; or
- first 0x0F FC03 request after a successful 0410 ACK.

On either positive discriminator, TX stops immediately. New FC16 shapes are logged but not ACKed. FC03 is never answered. No semantic values are injected.


### Genuine Online capture follow-up — RAW FRAME CORRECTION
fclauson's follow-up interpretation claimed a direct `20 -> 21 -> 20` value path in `0x0848/0x07E4`. Independent raw parsing shows:
- first `0848/count23`: `0858=0`, `085A=20`;
- second `0848/count23`: `0858=21`, `085A=20`;
- therefore the actual delta is `0858: 0 -> 21`, not one field `20 -> 21`;
- the later `07E4` block does not prove the same field reverted to 20.

Record `0858=21` as a strong Heat-Curve-change/event candidate only. Do not label it as the persistent Heat Curve register yet.


### EXP138 — sequential 0x0F FC16 ACK probe — COMPLETE / POSITIVE TRANSPORT PROGRESSION

Observed:
- after reboot, controller was still stuck/retrying `0410/count22` throughout the passive baseline;
- baseline `fc16Seen=28`, all known, no FC03, no responder;
- first active `0410/count22` was ACKed;
- ~1.54 s later controller advanced to new `042E/count15`;
- new block was not ACKed and experiment stopped;
- final summary:
  `reason=POSITIVE_NEW_FC16_STAGE_AFTER_0410 duration_ms=31949 fc16Seen=30 whitelisted=29 unknown=1 ackTx=1 txRefused=0 fc16AckSeen=0 fc03Req=0 fc03Resp=0 existingResponder=NO resyncDelta=0 dropDelta=0 DE_LOW`.

Conclusion:
The acknowledged XTR 0x0F sequence is now locally proven as:
`03E8/14 -> ACK -> 0410/22 -> ACK -> 042E/15`.

Additional finding:
Controller sequence state persists across ESP reboot/responder disappearance; it resumes/retries the outstanding stage.

Next:
EXP139 adds only `042E/count15` to the ACK whitelist.


### EXP137 — PREPARED — 0x0F FC16 ACK-only presence probe
30 s passive collision-check baseline, then up to 90 s ACK-only responses to exact known XTR 0x0F FC16 shapes (`03E8/14`, `0442/13`, `04A6/13`, `085F/5`). No FC03 responses and no register values injected. Positive = controller starts an 0x0F FC03 read after ACK-only presence; first read stops TX immediately.


### EXP137 — 0x0F FC16 ACK-only presence probe — COMPLETE / POSITIVE TRANSPORT PROGRESSION

Hypothesis:
Simple slave-0x0F presence/acknowledgement may cause the controller to progress toward the genuine Online/DCM read phase.

Observed:
- 30 s baseline: `fc16Seen=42`, all `whitelisted=42`, `unknown=0`, no 0x0F FC03 and no responder activity.
- Active phase:
  - ACK `03E8/count14` once;
  - controller immediately introduced new `0410/count22`;
  - ACK `085F/count5` once;
  - `0410/count22` was never ACKed and repeated 83 times.
- Final summary:
  `duration_ms=120150 fc16Seen=127 whitelisted=44 unknown=83 ackTx=2 txRefused=0 fc16AckSeen=0 fc03Req=0 fc03Resp=0 resyncDelta=0 dropDelta=0 DE_LOW`

Conclusion:
The controller advanced from the normal unacknowledged XTR 0x0F pattern into a new `0410/count22` stage only after the first `03E8/count14` ACK. Continuous retransmission of `0410/count22` without ACK strongly indicates an acknowledged sequential transfer/synchronization state machine.

Negative:
No FC03 phase was reached because `0410/count22` remained unacknowledged.

Next:
EXP138 adds only `0410/count22` to the ACK whitelist.


### External genuine Online capture — major architecture correction
A working Thermia Online installation shows a real slave `0x0F` ACKing FC16 and serving FC03 reads. During Heat Curve 20->21->20, the two captured `03E8` read snapshots differ only at the first word, 23->22. The capture also shows recurrent controller->0x0F FC16 block families and no response to the recurring `0x06` FC17 poll. This strongly shifts the Online/DCM hypothesis from `0x06` toward a shared register interface at `0x0F`. Slave `0xA5` is also active but remains unidentified.

### EXP136 — passive DHW COMFORT/ECO mode A/B/A — COMPLETE / NEGATIVE
Confirmed physical COMFORT<->ECO change and restore. Recurrent `03E8..03F5` remained byte-for-byte unchanged; zero word changes, zero parser/drop errors. DHW mode is not represented in that recurrent block.

### EXP135 — passive DHW START A/B/A — COMPLETE / NEGATIVE FOR 03F1
Manual `SERVICE -> WARMWATER -> START` ±1 °C produced no change in recurrent `03E8..03F5`; `03F1` remained 40. `041D` was not covered by an observed block. Downgrade `03F1 = Hot Water Start` to OPEN / locally unsupported.

## 2026-09-24 — EXP129–134 current run

### EXP134 — Passive DHW START correlation — PREPARED, NOT RUN
Hypothesis: external candidate decimal 1053 / hex `0x041D` may correspond to `SERVICE → WARMWATER → START` on this XTR.

Planned controlled variable: manually change only DHW START by -1 °C and restore it while ESP passively logs 0x0F changes. `0x041D` is a candidate marker only. No ESP write.

Safety: run only after EXP133 review; use a moment when DHW production is inactive and the actual DHW temperature is sufficiently above START so the -1 °C step cannot create a new heat demand.


### EXP134 — passive DHW START correlation — PROCEDURAL / INCIDENTAL
Only `03E8 34 -> 35` changed, tracking Heating Curve. No valid DHW mapping resulted.

### EXP133 — Passive 0x0F block-structure census — RUNNING / PARTIAL
Hypothesis: the XTR uses stable native 0x0F application/settings blocks beyond the already-known 0x03E8 block, possibly sharing structural patterns with the external ATEC/DHP-AQ material.

Design: 600 s passive-only census; no RS485 TX, no 0x06 response, no direct 0x0F write. Log every unique 0x0F FC03/FC10/FC17 shape and first payload. External block starts are flagged only as hints.

Partial observed facts:
- experiment started with `PASSIVE_ONLY DE_LOW no_tx`;
- first native FC10 shape: start `0x04A6`, count 13; payload has only word `0x04B0=0x4020` nonzero in the first observed frame;
- second native FC10 shape: start `0x085F`, count 5; first payload all zero;
- `0x0861` is inside that native five-word block;
- parser resyncs and RX drops remained zero in the supplied partial log.

Status: **OPEN**. Do not infer the final 0x0F block map until the automatic EXP133 SUMMARY and full 600 s log are captured.

### EXP132 — AFC8/AFC9/AFCB validity/header matrix with AFD1=16 — COMPLETE / NEGATIVE
Hypothesis: `AFC8/AFC9/AFCB` may form a metadata validity/header pattern whose effect only appears with a nonzero valid AFD1 version.

Observed: EXP 1.6 remained unchanged when AFC8, AFC9, AFCB were zeroed individually, pairwise and all together, with AFD1 fixed at 16. Final summary: `tx=353`, `refused=0`, `marksSame=16`, `marksChanged=1`, `marksGone=0`, `resyncDelta=0`, `dropDelta=0`.

Conclusion: AFC8/AFC9/AFCB are not required for the VERSION page to display EXP 1.6.

### Architecture review after EXP132
Uploaded Discussion #143 and supporting files from another Thermia platform were compared against our own captures. They are treated as external hints, not truth for XTR. The strongest cross-check is that our XTR itself already carries `0x0F FC10` application/settings blocks starting at `0x03E8`, while the external work independently identifies similar 0x0F block traffic. This shifts the next investigation from guessed 0x06 application payloads toward passive XTR-specific 0x0F block mapping.

### EXP131 — AFD0 type with valid AFD1 version — COMPLETE / NEGATIVE
Hypothesis: `AFD0` may select accessory type/identity when `AFD1` contains a valid version.

Observed: baseline `AFD0=0, AFD1=16` displayed EXP 1.6. `AFD0=1,2,10,16` produced no visible change; restore phases were also unchanged. Summary reported `tx=208`, `refused=0`, `marksSame=10`, `marksChanged=1`, `marksGone=0`, `resyncDelta=0`, `dropDelta=0`.

Conclusion: tested AFD0 values are not a simple visible type/identity selector.

### EXP130 — AFD1 version scaling — COMPLETE / POSITIVE MAPPING
Hypothesis: `AFD1` is the visible EXP/expansion-board version field.

Observed: with a valid 0x06 responder, VERSION display tracked the tested AFD1 values as tenths: `0→0.0`, `1→0.1`, `2→0.2`, `10→1.0`, `16→1.6`.

Conclusion: `AFD1` is a proven visible EXP version field for this XTR UI path. This is metadata/UI semantics only; it does not prove Online/DCM identity or write-session readiness.

## EXP107 — PREPARED — Persistent accessory image then isolated AFCA pulse

Hypothesis:
A known 0x06 transaction may behave differently if the accessory-side image has been continuously stable for >=60 s before AFCA is asserted.

Controlled change:
Only the preload/stabilization duration changes. The historical image and AFCA 4-phase mechanism are already-tested values.

Sequence:
1. qualify clean idle baseline;
2. transmit historical REQ-low image continuously for >=60 s;
3. change only AFCA 0000->03E8;
4. wait for 0861=16;
5. change only AFCA 03E8->0000;
6. wait for 0861=0;
7. continue the identical REQ-low image for 90 s;
8. summary.

Safety:
No new semantic write target; exact 0x06 slot only; existing-responder inhibit; compressor/outdoor idle guards; parser/drop guards; hard handshake timeouts.


## EXP107 — COMPLETE — Persistent image + isolated AFCA pulse

Result: negative for semantic initialization, positive for transport reproduction.

Timeline:
- cached settings baseline accepted
- TX_PRELOAD_REQ_LOW_01 started historical envelope
- image held continuously for 61.023 s
- TX_REQ_ASSERT: only AFCA changed to 03E8
- 0861: 0 -> 16 after 328 ms
- TX_REQ_DEASSERT: only AFCA returned to 0
- 0861: 16 -> 0 after 1122 ms
- identical REQ-low image continued for 90 s

Summary:
`handshake_complete=1 total_responses=144 observe_responses=84 A80E_peak=0 A80E_changes=0 AFDC_peak=0 AFDC_changes=0 AFDC_nonzero=0 status_peak=16 settings_changed=0 resync_delta=0 drop_delta=0`

Observed negative:
No A80E/AFDC activation, no semantic settings change, no new controller-side state beyond the known 0861 ACK.

Conclusion:
Persistent presence duration is not the missing DCM semantic bootstrap. Do not spend further experiments on longer dwell times or nearby timing variants unless new external evidence justifies them.


## Firmware analysis after EXP107

No new bus experiment was run.

New binary evidence:
- 2.1.35: generic DHPParameterCache exists, but no HPNode/SystemIntegration application layer in RegulationEngine.
- 2.7.42: HPNode/SystemIntegration application layer present.
- IntegrationMode is confirmed ParameterID 0x4414.
- SystemIntegrationInitRequest and InitSyncDone are internal booleans, not wire parameters.
- IntegrationMode update triggers full three-group resynchronization.
- system integration flips selected heat-pump parameters from GET-on-sync to SET-on-sync.

Decision:
Do not design EXP108 around a guessed "init flag". First reconstruct the three sync groups and look for a local mailbox representation of grouped synchronization.


## EXP106 — Passive integration-sync window correlator — PREPARED

Hypothesis: `A80F=0x0032` may identify the broader integration/synchronisation phase that older captures associated with A80E/AFDC cycling. EXP93 never triggered, so this remains untested.

Plan: strictly passive. Arm after >=15 s uptime, observe up to 30 min, trigger on A80F=50, then capture 180 s post-trigger context across A80C..A812, A7F8..A806, AFDC..AFE0/cadence, 0861, settings, 0x1E command image and outdoor state. Hard stop 1800 s if no trigger. TX=0.


## Cross-model evidence update — Piotr Romanowski / thermia-bus-sniffer — 2026-09-23

This is not a new Marten experiment; it is independent corroborating evidence from an iTec Eco 8 / DHP-AQ unit.

Observed by Piotr:
- corrected prior claim: `0x1E 0x001E..0x0033` is not frozen; it changes rarely and out of step with the live block;
- `B3B1` works as a real room-setpoint request channel in the slave response slot, encoding x1 °C;
- the controller stores the accepted setpoint and pushes it back through `B3C5`;
- `B3B1=0` means no request, not revert/clear;
- `AFDD=AFDE=AFDF=0` throughout a long passive capture;
- `AFE0` tracks displayed outdoor temperature x1;
- `AFDC` continuously pulses `0 <-> 32` with ~64 s period (~17 s high / ~47 s low);
- `A80E` follows the same pulse timing to the second;
- passive `0861` remained constantly `0` over multiple days;
- one isolated `AFDC=16` coincided with outdoor-unit-active status rise, insufficient for a semantic interpretation;
- A80E bit 3 appeared independently for ~10 minutes.

Strong conclusion:
- the recurring A80E/AFDC `0x20` state is ordinary controller lifecycle/heartbeat behaviour, not evidence of DCM login, approval, or semantic session.
- `0861` remains the cleaner transaction-level discriminator for active `AFCA=03E8` tests.

Candidate EXP107 direction after EXP106 closes:
- maintain one already-tested, harmless 0x06 accessory baseline image continuously for a stabilization interval;
- pulse only `AFCA 0 -> 03E8 -> 0` with all other words unchanged;
- observe `0861`, settings, controller state, CMD1E and outdoor state;
- do not gate the experiment on AFDC/A80E values.


## EXP106 — CLOSED (partial but sufficient negative)

The planned final post-trigger summary was not captured, so EXP106 remains technically incomplete as a full-duration run. However, the discriminating hypothesis is sufficiently rejected:

- A80E/AFDC cycling occurred at A80F 75, 80 and 50;
- A80F=50 therefore is not required for that lifecycle;
- A80F 80->50 occurred close to ordinary outdoor-unit transition to state 16/idle;
- no passive 0861 activity or settings mutation was seen;
- cross-model Eco 8 evidence shows AFDC/A80E 0<->0x20 can be a continuous heartbeat.

Decision:
Close EXP106 and do not build further A80F/AFDC-gated semantic tests.

## EXP105 — State-gated canonical transaction — PREPARED

**Hypothesis:** a semantic/application transaction may only be accepted during the natural controller lifecycle window where `A80E=0x0020` and `AFDC=0x0020`.

**Change from EXP104:** no payload sequencing experiment. EXP105 remains passive until the natural gate and then sends one already-known historical canonical transaction. This isolates controller-state timing as the variable.

**Safety:** no known setting target, no new unknown payload values, no TX before the gate, fail-closed UART guard, 180 s hard stop.


## EXP105 — State-gated canonical transaction — COMPLETED NEGATIVE

Hypothesis: the known historical `00FF,0001,REQ,0001,0...` transaction may only gain semantic meaning during the natural `A80E=0x0020` / `AFDC=0x0020` lifecycle window.

Observed:
- gate triggered naturally at ~32.9 s after arm;
- preload and REQ-high both occurred while A80E and AFDC were still `0x0020`;
- ACK-high after 373 ms; ACK-low after 1151 ms;
- summary: `complete=1 hard_stop=0 gate_seen=1 gate_aborts=0 txn_complete=1 ack_hi=1 ack_lo=1 settings_pushes=0 settings_changes=0 cmd1e_changes=0 outdoor_changes=0 resync_delta=0 drop_delta=0`.

Result: valid negative. The natural `0x20/0x20` controller window does not make the known historical envelope semantically active.


## EXP104 — AFC8 sequence-toggle canonical transaction chain — PREPARED

Hypothesis: AFC8 may act as transaction identity/sequence metadata only when its value changes across consecutive canonical transactions.

Plan: T1 AFC8=00FF, T2 AFC8=00FE, T3 AFC8=00FF; AFC9=1, AFCB=1, tails zero, canonical AFCA handshake for each; no zero-recovery between T1/T2/T3; 10 s zero final observation; 60 s hard stop. No known setting IDs. Corrected bus-health diagnostics from fixed EXP103 retained.


## EXP104 — AFC8 sequence-toggle canonical transaction chain — COMPLETED NEGATIVE
- Hypothesis: AFC8 may act as transaction identity/sequence metadata when changed between consecutive canonical transactions.
- Sequence: T1 `00FF`, T2 `00FE`, T3 `00FF`; AFC9/AFCB fixed at `0001`; AFCA canonical REQ handshake; no recovery gap between transactions.
- Result: all 3 transactions ACKed fully (`ack_hi=3`, `ack_lo=3`, `t1=t2=t3=1`). ACK-high: 447/441/447 ms after REQ assert. ACK-low: 1076 ms after REQ deassert for all 3.
- No semantic effect: `settings_pushes=0`, `settings_changes=0`, `cmd1e_changes=0`, `outdoor_changes=0`.
- `ctrl_changes=1` and `06_changes=1` were the natural A80E/AFDC `0->32` cycle occurring after transaction completion; the cycle later reset and repeated, so not attributed to EXP104.
- Bus-health bookkeeping fix validated: frame count increases and last-valid-frame age is live.
- Conclusion: simple AFC8 sequence-toggle hypothesis negative.


## EXP103 — repeated identical canonical transaction chain — PREPARED

Hypothesis: DCM application/session state may accumulate only after multiple consecutive successfully acknowledged transactions with an unchanged historical envelope.

Plan: three identical `00FF,0001,REQ,0001,0...` canonical transactions. T2 and T3 are chained immediately after ACK-low with no 3 s zero-recovery between them. After T3, reply all zeros and observe 10 s. No new payload values or known setting IDs. Hard stop 60 s.


## EXP103 — repeated identical canonical transaction chain — COMPLETED NEGATIVE

Hypothesis: DCM application/session state may accumulate only after multiple consecutive successfully acknowledged transactions with an unchanged historical envelope.

Observed:
- T1/T2/T3 all completed with canonical `0861 0->16->0` handshakes;
- no 3 s zero-recovery was inserted between transactions;
- `ack_hi=3`, `ack_lo=3`, `t1=t2=t3=1`;
- `settings_changes=0`, `ctrl_changes=0`, `06_changes=0`;
- `cmd1e_changes=0`, `outdoor_changes=0`;
- `resync_delta=0`, `drop_delta=0`;
- final `complete=1`, `hard_stop=0`.

Result: valid negative. Three back-to-back identical historical-envelope transactions do not establish semantic DCM state.

Post-run note: after the experiment summary, a natural `A80E 0->32` followed by `AFDC 0->32` occurred, and the pattern repeated later. These transitions are not attributed to EXP103 because they occurred after the experiment ended.

Diagnostics note: this run used the pre-fix health-bookkeeping build, so `Bus Last Valid Frame Age` stayed `nan` and `Valid Frames Since Boot` stayed `0` despite continuous bus traffic. This does not invalidate the experiment result.


## Historical archive re-analysis before EXP102

Reviewed 98 archived Thermia logs. Recovered earlier coverage showed that EXP16/18 had already varied AFC9/AFC8 broadly, EXP14/15 had varied AFCB, EXP24/25 had probed words 4..11 with 0001 during the ACK window, and EXP26/28 had tested structured word4/word5 payloads. All were negative for a semantic setting change despite valid transport behavior.

This makes further isolated-word tests redundant. A new structural hypothesis is therefore promoted: one of the historical `0001` words may be a payload length/count, so previous extra tail data may have been outside the declared message length.

## EXP102 — count / structure interaction matrix — PREPARED

Hypothesis: AFC9 and/or AFCB acts as a declared payload length/count.

Plan: six canonical transactions: historical count-1 control, AFC9 lengths 2 and 3 with matching tail words, AFCB lengths 2 and 3 with matching tail words, and a both-length2 case. Small values only; no known setting IDs; 3 s zero recovery; hard stop 80 s.

## EXP102 — count / structure interaction matrix — COMPLETED NEGATIVE

Hypothesis: AFC9 and/or AFCB may be a declared payload length/count.

Observed:
- six of six transactions completed;
- `ack_hi=6`, `ack_lo=6`, `0861_changes=12`;
- T1..T6 each completed once;
- coherent AFC9 length-2/3, AFCB length-2/3, and both-length2 structures all received normal transport ACKs;
- `ctrl_changes=0`, `rsp02_changes=0`, `06_changes=0`;
- `settings_pushes=0`, `settings_changes=0`;
- `cmd1e_changes=0`, `outdoor_changes=0`;
- `resync_delta=0`, `drop_delta=0`.

Result: valid negative. Matching larger count-like values with additional tail words does not unlock semantics. The simple AFC9/AFCB length-count hypothesis is rejected.


## Post-EXP102 archive audit — 2026-09-23

No new experiment was armed. Historical archive review covered 98 logs and recovered broader prior test coverage than the condensed state showed. At least 45 unique logged experimental 0x06 response payload forms were indexed. Earlier EXP13–18, 24–28 and later EXP52–102 collectively make further isolated-word/value probing low-value. No genuine DCM03 accessory response was identified in the archive.

Decision: **EXP103 deferred pending new evidence**. Negative results are preserved; next active test should be derived from genuine DCM traffic, firmware/PCB evidence, or another independently sourced protocol trace rather than another guessed response.


## EXP101 — AFCC..AFD3 one-word influence matrix — PREPARED

Hypothesis: one or more tail response words AFCC..AFD3 may participate in the missing DCM03 application layer.

Plan: eight transactions, one word at a time: AFCC=1, AFCD=1, AFCE=1, AFCF=1, AFD0=1, AFD1=1, AFD2=1, AFD3=1. Canonical AFCA=03E8 handshake; 3 s zero-recovery between transactions; hard stop 95 s. No known setting target.

## EXP101 — AFCC..AFD3 one-word influence matrix — COMPLETED NEGATIVE

Hypothesis: one of the still-unmapped tail words `AFCC..AFD3` may be an application-layer selector when transported with the proven canonical REQ/ACK handshake.

Observed:
- 8/8 planned transactions completed;
- `ack_hi=8`, `ack_lo=8`, `0861_changes=16`;
- T1..T8 each completed once;
- per transaction exactly one of AFCC..AFD3 was `0x0001`;
- `ctrl_changes=0`, `rsp02_changes=0`, `06_changes=0`;
- `settings_pushes=0`, `settings_changes=0`;
- `cmd1e_changes=0`, `outdoor_changes=0`;
- `resync_delta=0`, `drop_delta=0`;
- no hard stop or TX refusal.

Result: negative. No tested tail word produced a detectable application-layer effect by itself.

## EXP100 — Multi-transaction historical-field matrix

**Hypothesis:** those fields may only matter inside the proven canonical REQ/ACK transaction.

**Design:** six transactions in one run: AFC9 only; AFCB only; AFC8+AFC9; AFC8+AFCB; AFC9+AFCB; AFC8+AFC9+AFCB. Each uses preload -> `AFCA=03E8` -> wait `0861=16` -> `AFCA=0` with payload stable -> wait `0861=0` -> 3 s zero-presence observation. Hard stop 75 s. No semantic setting target.

## EXP100 — Multi-transaction historical-field matrix — result

**Hypothesis:** historically observed `AFC8/AFC9/AFCB` fields may only matter inside a valid canonical `AFCA=03E8` transaction.

**Observed:** six of six transactions completed. Each followed preload -> REQ high -> `0861=16` -> REQ low with stable payload -> `0861=0` -> observation. Final summary: `duration_ms=58046`, `complete=1`, `hard_stop=0`, `06polls=51`, `tx=51`, `refused=0`, `ack_hi=6`, `ack_lo=6`, `t1=1..t6=1`, `0861_changes=12`, `settings_pushes=0`, `settings_changes=0`, `ctrl_changes=0`, `rsp02_changes=0`, `06_changes=0`, `cmd1e_changes=0`, `outdoor_changes=0`, `resync_delta=0`, `drop_delta=0`.

**Result:** valid negative. Carrying the tested historical non-REQ field combinations inside a proven transport transaction still produces no semantic effect.


## EXP100 — Multi-transaction historical-field matrix — COMPLETED

Hypothesis: AFC8/AFC9/AFCB may only have application-layer meaning inside a valid AFCA=03E8 transaction.

Result: valid negative. All six transactions completed with canonical four-phase transport (`ack_hi=6`, `ack_lo=6`, `0861_changes=12`). No controller, 0x02 response, settings, 0x1E command, outdoor-state, or 0x06 controller-write change occurred. `resync_delta=0`, `drop_delta=0`.

Conclusion: historical AFC8/AFC9/AFCB values, separately and in all tested combinations, are semantically insufficient even inside valid transport transactions.

## EXP99 — Historical-field matrix, REQ low
Prepared as a faster structured follow-up: ten 8 s phases test AFC9=0001, AFCB=0001, pairwise combinations with AFC8=00FF, and the full historical non-REQ combination. AFCA remains 0000 throughout.


## EXP99 — Historical-field matrix, REQ low — result

**Hypothesis:** `AFC8=00FF`, `AFC9=0001`, `AFCB=0001` may have standalone or combinatorial application-layer meaning without REQ.

**Observed:** 80 s complete; `06polls=75`, `tx=75`, `refused=0`; each of the ten phases received 7–8 responses. `06_min_ms=707`, `06_max_ms=1450`. `ctrl_changes=0`, `rsp02_changes=0`, `06_changes=0`, `0861_changes=0`, `settings_pushes=0`, `settings_changes=0`, `cmd1e_changes=0`, `outdoor_changes=0`, `resync_delta=0`, `drop_delta=0`.

**Conclusion:** valid negative. None of the historically observed non-REQ fields, alone or in the tested combinations, is a standalone semantic trigger with `AFCA=0000`.

## EXP98 — AFC8 single-word A/B/A influence test

**Hypothesis:** isolated `AFC8=00FF` has a measurable application-layer effect when transport presence is maintained.

**Design:** 90 s A/B/A: zero-presence 20 s; `AFC8=00FF` only for 30 s; zero-presence recovery 40 s. `AFCA=0000` throughout. No semantic write target.


### Result — EXP98
A/B/A completed cleanly. AFC8=00FF alone caused no detectable application-layer response. 81 0x06 polls and 81 TX were completed without refusals; no controller, RSP02, 0x06 write-bank, 0861, settings, CMD1E or outdoor-state changes were observed. Negative result recorded.

## EXP97 — Passive natural A80E/AFDC edge correlator

**Hypothesis:** natural A80E/AFDC transitions correlate with another controller/outdoor-unit state rather than DCM-session establishment.

**Design:** 600 s passive observation, no TX, no cold boot requirement. Every A80E or AFDC edge produces a compact multi-layer snapshot of `A80C..A812`, `A7F8..A806`, `AFDC..AFE0`, `0861`, `0x1E 0000..0008`, and outdoor-state.


## EXP97 — Passive natural A80E/AFDC edge correlator — result

**Hypothesis:** natural A80E/AFDC transitions correlate with another known controller/outdoor state rather than DCM-session establishment.

**Observed:**
- baseline `A80E=0028`, `AFDC=0010`, `0861=0000`, outdoor=`0010`;
- +71.278 s: `A80E 0028 -> 0020`;
- +72.340 s: `A80E 0020 -> 0000`;
- +74.995 s: `AFDC 0010 -> 0000`;
- all three event snapshots had identical `0861`, outdoor, `CMD1E`, and paired `RSP02`;
- experiment was passive: no 0x06 response, no REQ, no TX.

**Conclusion:** A80E/AFDC are not reliable DCM-session-success indicators. The specific monitored controller/outdoor fields did not explain the natural transition.

**Negative result recorded:** no direct edge correlation with `0861`, outdoor state, CMD1E, or paired RSP02.

## EXP96 — Cold-boot historical envelope + canonical REQ/ACK handshake

**Hypothesis:** the historical envelope gains semantic meaning only in the true cold-boot EXP95 context.

**Observed:**

- canonical transaction completed;
- `0861 0->16` after 367 ms;
- REQ deasserted with payload stable;
- `0861 16->0` after 1196 ms;
- `handshake=1`; `06polls=112`; `tx=112`; `refused=0`;
- `ctrl_changes=3`; `rsp02_changes=0`;
- `settings_pushes=0`; `settings_changes=0`;
- no higher-layer application/session transition.

**Conclusion:** valid negative. Cold-boot context does not rescue the historical envelope. The missing layer remains the DCM03 semantic/init serializer.

**Additional passive observation before ARM:** `A80E 0x28->0x20->0x00`, followed by `AFDC 0x10->0x00`, occurred naturally with no EXP96 TX. This is recorded as evidence that these fields participate in broader controller-state propagation.

## EXP95 — Cold-boot zero-presence from first 0x06 poll

**Hypothesis:** syntactic DCM presence from the first cold-boot `0x06` poll is sufficient to move the controller away from EXP94's stable waiting state.

**Observed:**

- complete `120000 ms` run;
- `frames=1133`; `06polls=112`; `tx=112`; `refused=0`;
- `06_min_ms=638`; `06_max_ms=1503`;
- boot state still followed `A80E 0->8->0x28`, `A80F/A810 5->10`, `AFDC 0->0x10`;
- `0861_final=0000`, `0861_changes=0`;
- `settings_pushes=0`, `settings_changes=0`;
- `outdoor_state_changes=0`;
- `resync_delta=1`, `drop_delta=0`.

**Strong conclusion:** zero-presence proves transport/presence and triggers fast cadence, but does not establish/advance the DCM application session. `AFDC=0x10` therefore cannot simply mean “accessory absent.”

**Negative result recorded:** syntactic presence alone does not advance the cold-boot integration state.

## EXP94 — Passive cold-boot + initial-sync timeline

**Hypothesis:** a real controller cold boot exposes a reproducible 0x06 accessory/integration startup or sync sequence that precedes semantic DCM03 operation.

**Observed facts:**

- bus silence confirmed after 5049 ms; first resumed valid frame after 11540 ms silence started capture;
- +717 ms: `A80C..A812=0040,0000,0000,0005,0005,FFFF,0000`;
- +1758 ms: `A80E 0->8`;
- +2846 ms: `A80E 8->40 (0x28)`;
- +1038 ms first 0x06 poll: `AFDC..AFE0=0000,0000,0000,0000,0019`;
- +5575 ms second 0x06 poll: `AFDC..AFE0=0010,0000,0000,0000,0014`;
- `A80F/A810` returned from 5 to 10 at about +11.3 s;
- no later DCM/integration transition occurred during the full 600 s window.

**Summary:** `frames=5185`, `06polls=140`, `06_min_ms=4086`, `06_max_ms=4537`, `ctrl_changes=3`, `rsp02_changes=1`, `0861_changes=0`, `settings_pushes=0`, `settings_changes=0`, `outdoor_state_changes=0`, `resync_delta=1`, `drop_delta=0`.

**Strong conclusion:** unanswered cold boot settles quickly into stable `A80E=0x28 / AFDC=0x10 / A80F=A810=10`; the historical A80E/AFDC 0x20 cycle is not ordinary cold-boot initialization.

**Unknowns:** exact meanings of A80E bits 0x08/0x20 and AFDC 0x10; whether a real DCM response advances this state.

## External evidence before EXP93

Commit `piotr-romanowski/thermia-bus-sniffer@b4c27157402c49624917d523e016b249cdfc4e11` independently confirmed transmit-side room-setpoint control through slave 0x0A response register B3B1/46001 on iTec Eco. This matches our passive mapping and changes the highest-value next experiment.

## EXP93 — Passive A80F=50 discriminator

**Hypothesis:** the historical A80E/AFDC 0<->0x20 cycle is gated by controller state and appears while A80F=50.

**Observed:** correctly armed in two captures, but A80F remained 10 and no EXP93 trigger/summary occurred. The 180 s observation phase never began.

**Conclusion:** untriggered/inconclusive, not negative. Superseded as immediate priority by EXP94.

## EXP92 detailed record

Hypothesis: a completed four-phase transaction initializes hidden state needed for the old A80E/AFDC cycle.

Observed:

- baseline stable
- historical envelope preloaded
- REQ asserted on SHORT
- 0861 0->16 after 401 ms
- REQ deasserted while payload held stable
- 0861 16->0 after 1031 ms
- 90 s observation completed
- 84 observation replies
- A80E changes: 0
- AFDC changes: 0
- settings changes: 0
- parser resync delta: 0
- RX drop delta: 0

Conclusion: a single completed transport transaction is not sufficient to start the historical online-state cycle.

| Experiment | Purpose | Result |
|---|---|---|
| **EXP99** | Historical-field matrix, REQ low | **COMPLETED NEGATIVE.** Ten phases completed; no controller/0861/settings/CMD1E/outdoor effect; parser/drop deltas zero |
| **EXP98** | AFC8 single-word A/B/A influence | **COMPLETED NEGATIVE.** AFC8=00FF alone had no detectable effect; 81 polls/81 TX, no controller/0861/settings/CMD1E/outdoor changes |
| **EXP97** | Passive natural A80E/AFDC edge correlator | **COMPLETED.** Natural `A80E 28→20→0`, then `AFDC 10→0`; no ESP TX; 0861/outdoor/CMD1E/RSP02 unchanged at all three edges |
| **EXP96** | Cold-boot historical envelope + canonical four-phase REQ handshake | **VALID NEGATIVE.** Handshake completed (`0861` high after 367 ms, low 1196 ms after deassert); no controller/session/settings progress |
| **EXP95** | Cold-boot zero-presence from first 0x06 poll | **VALID NEGATIVE.** 112/112 responses; cadence accelerated to 638..1503 ms, but `A80E=0x28`, `A80F/A810=10`, `AFDC=0x10`, `0861=0`; no settings changes |
| **EXP94** | Passive cold-boot + initial-sync timeline | **COMPLETED.** Boot sequence: A80F/A810 5→10, A80E 0→8→0x28, AFDC 0→0x10; then stable for 600 s; 0861 unchanged; no settings changes |
| EXP93 | Passive A80F=50 discriminator | Armed in two captures but A80F=50 never occurred; observation window never started; NOT a negative result |
| **EXP92** | Completed four-phase 03E8 handshake, then historical REQ-low envelope 90 s | **VALID NEGATIVE. ACK high after 401 ms, ACK low after 1031 ms; 84 observation responses; A80E/AFDC stayed 0; no setting/error changes** |
| EXP91 | Historical 00FF,1,REQ-low,1 envelope 90 s | Negative; 84 responses; no A80E/AFDC/settings/errors |
| EXP90 | Correct persistent 00FF 90 s | Negative; 84 responses |
| EXP89 | Intended persistent 00FF | Invalid due response-buffer bug |
| EXP88 | Fixed all-zero presence 180 s | Negative |
| EXP87 | Zero presence | Invalid/short guard stop; no semantic edge beforehand |
| EXP86 | 30-minute passive first-edge capture | No A80E/A802/AFDC edge |
| EXP85 | Passive DCM source correlator | No source edge during capture |
| EXP84 | Passive room-setpoint correlation | AFDC..AFE0 unaffected |
| EXP77-83 | HE payload/envelope/layout variants | No semantic response/write |
| EXP76B | Canonical four-phase handshake | PROVEN |
| EXP74-75 | Persistent candidate register image | No write; ACK follows REQ level |
| EXP73/73B | Passive/manual curve correlation | Curve changes do not announce through AFDC/A80E |
| EXP72 | Natural AFDC/A80E state + bare 03E8 | Transport behaviour confirmed |
| EXP71/71B | Apparent promotion / zero replies | Promotion later identified as natural controller behaviour |
| EXP70 | Repeated zero responses | Fast cadence only |
| EXP68-69B | Raw 12-word settings block variants | No setting change |
| EXP67 | Post-close 03E8 on first FAST-LONG | No second ACK |
| EXP66 | HE-like GET 440C | Handshake only; no semantic response |
| EXP63-65 | Structured register/value layouts | Transport ACK only; no setting write |
| EXP62 | Selector 03E9 after established session | No ACK |
| EXP61 | Later valid SHORT 03E8 | ACK repeats |
| EXP60 | Same 03E8 on LONG vs SHORT | SHORT phase matters |
| EXP59 | Zero stage then SHORT 03E8 | ACK; 00FF unnecessary |
| EXP58 | Bare 03E8 at wrong/normal-long phase | Fast cadence; no 0861 ACK |
| EXP57 | Bare 03E8 | ACK works |
| EXP56B/C | 03E8 with word3 variants | ACK independent of simple word3 value |
| EXP55 | word2=04A6 | No ACK |
| EXP54 | word2=03F4 | No ACK |
| EXP53 | word2=440C | No ACK |
| EXP52 | 00FF,1,03E8,1 envelope | ACK; no setting write |
| EXP51 | Single presence-like response | Cadence/state only |
| EXP50 | Passive DCM audit | Recurring structure mapped |
| EXP48-49 | Presence/multi-poll sequencing | Fast-cadence/state behaviour refined |
| EXP43+ | Active 0x02 probes | No final semantic write path |
| EXP35-42 | Passive mapping | Useful telemetry; no write path |
| EXP30-31,33 | Outdoor-related probes | No semantic write discovered |
| EXP29 | Passive correlator | Diagnostic only |
| EXP21-28 | Test trailing words/selectors/counts as setting-write encoding | Negative |
| EXP10-18 | Identify 0x06 response field responsible for controller ACK | word2/AFCA=03E8 in correct phase is decisive |