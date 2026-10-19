# V5DCM57 — Original CM930 FC16 ACK, event-loop requests, first-version credit, historical archive ACK correction

**ID:** V5DCM57-CM930-FC16-ACK-STATUS-SERVICE-OFFLINE-01. **Status: COMPLETE / POSITIVE FOR OFFLINE ORIGINAL-SOURCE/HOST/CAPTURE CLASSIFICATION ONLY.** No on-device TX, firmware build/flash, controller restart, native command tooling, protected handshake implementation or HA/YAML changes. Local sender/owner/EOF/exclusive response slot and native acceptance remain OPEN.

## Hypothesis, baseline, one change and abort
Hypothesis: the original Connect 2.0.18/2.1.105 automatic Modbus FC16 ACK, internal queued handshake/info request and controller status polling are distinct operations; the earlier metadata replay failed to classify CRC-valid 8-byte FC16 ACK shapes; 2.1.105 may credit the very first version-bearing 0864 page after seeding its required-group tracker *within the same callback*.

Known-good installed baseline: V49 RX-only hard deny, controller manually OFF/ON user intervention, 10351ms callback gap and 285 matched clean frames over 30.532s; no new B11C/B11D faults, UART native TX0, native 0708 poll0 and observed FC16 ACK shape0 in each of two distinct ESP console intervals; strict 03E8/14 and 0864/4 not observed, 04A6/13 and 085F/5 present. Historic V23 RX-only page03E8/14 and V47 inconclusive native trial preserved.

ONE CONTROLLED CHANGE: offline original 2018/2021 source and bundled Modbus RTU library inspection; execute original callback bodies with inert info/tracker and event stubs; correct archived packet classification for CRC-valid 8-byte native FC16 ACKs using exact start/count pairing within analyst-selected 300ms. No serial, physical risk, TX payload or private responder published. Positive criterion: verifiable source/callback order and reproducible capture census; negative: failing hashes, CRC mismatch or test assertion; inconclusive: physical owner/master ACK policy. Abort on corrupted evidence. No recovery needed.

## Original source provenance
- Genuine Connect 2.0.18 CM930 modbus_server15.py SHA256 45495f6f8e57e6eccf0cc09ee7b6952dd157e31fc645f34bbe5890c7291d7a9b.
- Genuine Connect 2.1.105 CM930 modbus_server15.py SHA256 9afc455fb50472012ae31d0767a0c39878647643ea9c37d7155142e097621d4f.
- BOTH original AppFS archives bundle BYTE-IDENTICAL modbus_tk/modbus.py SHA256 980309891121ab39605703c918bc247e133ae907381452fede18fb6581624710, and modbus_tk/modbus_rtu.py SHA256 1b74c80a9841a7f9aad8082d746fdd8e2605355e53af0624ac0677e37fa412f2.
- Private offline original callback tester SHA256 d99585f787bdf456a3c401e322daf453b78613d91a6d053225ae22219b04a91a; ACK audit script SHA256 7b0e22d0fe2e6f1a4aacdc59ea56bcc632770ce3ad7347ba8647052ef7bdc3a1; derived metadata SHA256 fe8d57b2f19e2275305a20ff8e755d15d6e4fe29f2015c78776b175287c9fcf7. Private tests are not a full original Connect process or physical device simulation.

## PROVEN firmware source service boundary

Original CM930 starts logical Modbus RTU slave15/0x0F with holding-register image and independent application events. Original modbus_tk FC16 handler validates/stores incoming words and generates an ordinary Modbus address/count ACK. In the CM930 server the RTU after-read hook runs BEFORE generic request handling, and its FC16 callback queues separate H2/received-page events. The event queue is processed by a separate application event loop. Thus (1) received page, (2) automatic protocol ACK, (3) H2/info-request event and mailbox data, and (4) a later CONTROLLER-INITIATED status read are DISTINCT operations. A queued 0867 information request is not physical TX or proof of a present master poll. Ordinary FC16 ACK is never proof of semantic setting acceptance.

The original bundled RTU server has a branch suppressing a response when more RX bytes are already pending. This is source-proven only; do NOT infer that this branch actually caused any unmatched ACK or assert any safe physical response timings. Both versions ship the same library.

## NEW first-version callback ordering: 4/4 original-method-body host tests PASS

Executed the actual original CM930Client.on_registers_received_event, _on_registers_read and reset_register_read_request source method bodies for BOTH 2.0.18 and 2.1.105 using a stub CMClient base, independent source-page/info collector and inert group-tracker. Not full firmware/process/serial execution.

For 2.1.105 WAITING_FOR_DEVICE_INFO, when the first native FC16 page 0864 actually supplies the recognized firmware version: base receipt -> info/version feed -> load matching profile -> seed required 33-group receive tracker -> RETURN from _on_registers_read -> outer handler resets corresponding native read group AND CREDITS the very same 0864/W4bit8 receipt to the newly seeded tracker. The 0864 version-group bit is thus not erroneously left pending by that specific first receipt. Any other required group such as 03E8/W3bit0 remains pending unless independently observed later. For 2.0.18 the corresponding first-version callback loads profile without the 2.1.105 tracker. When 03E8 arrives before recognized version, neither version seeds the newer tracker on that page, and 2.1.105 cannot retroactively credit such earlier pre-WAIT receipts. Both statements are compatible: the FRAME THAT CREATES WAIT is credited, while other PRE-WAIT frames are not retroactively credited. Exact source ordering proven by 4/4 host asserts; version detection and external IO were stubbed.

## Historical archive FC16 ACK parse correction (same seven files as V55)

Earlier private V51/V55 capture parser entered FC16 shape classification only for messages >=9 bytes. It **misclassified valid 8-byte FC16 ACK frames as generic OTHER**, though all their Modbus CRCs were correctly verified. The previously reported 25,031 CRC-valid frames and paired 0708 status-poll metadata remain valid. ACK interpretation was incomplete and is now corrected. 8-byte ACK shape != proof of controller acceptance or known physical sender.

| Archived source | Native FC16 request shapes | CRC-good native FC16 8-byte ACK shapes | Strict preceding same start/count paired <=300ms (host log timestamps) |
|---|---:|---:|---:|
| XTR Sep24 | 21 | 21 | 21 |
| XTR Sep25 07:15 | 40 | 40 | 40 |
| XTR Sep25 09:02 | 41 | 41 | 41 |
| XTR Sep25 09:05 | 73 | 42 | 42 |
| ATEC Oct03 | 162 | 162 | 162 |
| Eco5 Sep26 | 1,058 | 516 | 487 |
| Eco5 Sep28 | 1,105 | 543 | 531 |
| **TOTAL, 25,031 CRC-good archived frames** | **2,500** | **1,365** | **1,324** |

41 ACK forms have no unique preceding start/count match inside the arbitrary 300ms offline pairing window; 1,176 requests have no such captured pair. No physical retransmission/deadline is inferred; 300ms is a REPLAY FILTER and never a TX-time budget. Eco5 log gaps of 0ms reflect host timestamp granularity, not simultaneous physical bytes.

Notable controls:
- LOCAL XTR Sep25 07:15: 03E8/count13 requests 2 and matching ACKs 2; 0864/count4 requests 4 and ACKs 4. 18/18 native status replies exist; W3 request bit0 observed false across these snapshots. A page's FC16 ACK and a visible DCM read request bit are independent evidence dimensions.
- LOCAL XTR Sep25 09:02: 04A6/count13 1/1 ACK and 0864/count4 1/1 ACK; first native 0708 status poll t33.180s and no FC23 in bounded recording. Earlier accepted session or different owner remains possible; ACK alone does not establish a new cold Online connection.
- ATEC historical genuine/collaborator: 162/162 native FC16 requests ACK-paired, including initial 03E8 t29.262 followed by ACK t29.276, first native 0708 poll t64.923. These are host times, not physically measured EOF.
- Eco5 Sep28 has 211 native 03E8 request shapes but only 9 captured ACK shapes (all paired), and 226 04A6 requests but 10 ACK shapes. Unanswered forms and repeats co-occur, but no causal inference to controller master state, gateway version or logging incompleteness is justified.
- CURRENT XTR V49 original ESP console explicitly reports FC16 ACK shapes0, 0708 polls0, local physical UART TX0 while 04A6/085F FC16 requests continue. Local V49 is NOT the running original CM930 responder; the software-origin info-request state demonstrated in V56 is hypothetical for a substituted original DCM.

## Evidence classifications and next

**PROVEN original software:** 2018+2021 automatic FC16 ACK on accepted requests is a separate generic Modbus response from asynchronously queued internal H2/info/required-bit events, not semantic acceptance. The first 2021 recognized version-page callback seeds then credits that same version group (4/4 host tests); early pre-WAIT pages not retroactively counted. **PROVEN archived CRC metadata:** 1,365 genuine 8-byte FC16 ACK envelopes, 1,324 time/geometry-paired, and prior V55 parser omission is SUPERSEDED only for ACK classification. **PROVEN current V49 software:** normal native FC16 requests persist, but 0708 poll0, ACK shape0 and local UART TX0. **STRONGLY SUPPORTED:** request, ACK, event-loop mailbox state, controller 0708 poll, delivered status response, version page and internal tracker credit require separate evidence. **HYPOTHESIS:** present XTR master does not progress to service because native ACK/approval or some other unobserved session condition is absent; NOT proven. **OPEN:** actual physical sender/owner/epoch/EOF/slot, master policy, current 0867, original-Connect full OPERATION and Online and missing 03E8 root cause.

**NEXT:** existing V49 logs already demonstrate both ACK and status poll0; further replay of the same logs cannot reveal a missing controller decision. If subsequently user requests a new bounded PASSIVE-ONLY natural-state observation, prepare separately with existing hard-deny TX, no forced reboot or new native interface. Keep V49 source, HA production entities and diagnostic fault latches untouched. No proposed native TX follows from this study.
