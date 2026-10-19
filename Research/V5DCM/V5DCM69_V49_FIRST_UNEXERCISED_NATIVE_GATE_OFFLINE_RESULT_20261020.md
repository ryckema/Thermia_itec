# V5DCM69 — V49 first unexercised native response gate: build-locked RX versus locally observed staged progression

**ID:** V5DCM69-V49-FIRST-UNEXERCISED-NATIVE-RESPONSE-GATE-OFFLINE-01  
**Date:** 2026-10-20  
**Status: COMPLETE / POSITIVE (offline source/host and prior-local-evidence reconciliation only).** The positive verdict proves V49's intentional nonparticipation and identifies the first unexercised experimental edge; it does **not** prove controller-native acceptance, a controller-side algorithm, OEM Connect C2, or Online.

## Hypothesis, baseline, controlled distinction

**Hypothesis:** the present V49 controller-return session has not been empirically rejected by a native endpoint. Rather, native response TX is deliberately unavailable in V49, leaving the master at the already locally characterized no-responder branch. Consequently, V67/V68 page-version readiness is downstream of the actual missing first response and cannot explain the present lack of settings synchronization.

**Last VERIFIED live baseline:** V49 on local XTR M, with user-attested manual controller OFF/ON, 10,351ms RX callback gap; 285 matched CRC-valid post-return frames over 30.532s, no new B11C/B11D parser faults, UART TX0 by runtime diagnostics. The first seven FC23 requests are directly timed after return, later 63 cumulatively with a >13-minute unsampled console interval. Native FC23 response shapes=0, source `03E8/count14` and `0864/count4` sampled=0, native FC03 `0708/count6` sampled=0; unrelated recurrent 04A6/count13 and 085F/count5 still visible. V49 exact flashed binary SHA, electrical DE waveform, owner, EOF and physical response slot **not measured**. EXP388 remains RUNNING / PARTIAL. No current on-wire experiment initiated here.

**Relevant existing results already completed:** EXP254/255 (63 unanswered native requests then stop, ordinary 04A6/085F continues), EXP256 (one historical bounded native response triggers first settings page, but no ACK and communication alarm), EXP257 and EXP258 (one ACK each extends sequential page chain), EXP355/386 (formerly established/guarded XTR runtime and successful reboot/rejoin with full 32 native-page ACK chain and 0708 status), V47 negative/inconclusive one-shot integrity denial with no TX, V49 verified RX-only, V58 universal FC16-ACK-before-status rule disproven for retained historic sessions, V59–61 already reconstructed stages, V66–68 page ledger/profile diagnostics. Preserve negatives; **do not rerun EXP256 or repeat V61 as a new discovery**.

**ONE controlled change in V69:** independently re-check exactly the archived V49 ZIP / build flags / unchanged V42 OneShot source and runtime logs against the earlier stage-intervention evidence, and host-compile the unchanged V42 OneShot with a fake port for three safe macro configurations: no flags; only PRIVATE_TX_BUILD; only HARDWARE_PORT_REVIEWED. No user hardware or code modification; the other XTR historical experiment records serve as fixed counterfactual evidence, **not** new randomized live A/B outcomes.

## Source pins and independently executed host checks

- Exact user V49 ZIP SHA256 `62afe39629102a3daa06f09eab3ed159f44437d702fb8d3904c61e62e2a85630`, 69 files, YAML main SHA256 `fe02f0b0a503f8f896442165e57397afeacd22cf951efa46ea87885f98d71c22`.
- The V49 YAML deliberately omits both native-TX build flags and asserts `!v5dcm42::kBuildMaySend` at source line ~234. It retains the old operator Arm/Abort controls but the Arm state machine returns `BuildLocked` before evaluating a request or invoking an output port.
- Original V42 policy `kBuildMaySend` requires **both** compile definitions; independently enabled one flag remains disabled. V49 original runtime logs after controller manual restart show a user Arm click DENIED with no reply attempt, UART write or DE assertion; this is NOT failed controller semantic authentication.
- Disposable **host-only** fixture SHA256 `ba9656a00651e67d79b5d9a5b9eb75a18eb693b8209ed460909683a6a2af5edd` compiled three times under `g++ -std=c++17 -O0 -Wall -Wextra -Werror -pedantic`, with a fake non-hardware Port.
- **3/3 builds PASS:** `kBuildMaySend=false`, `arm()` returns false, denial `BuildLocked`, zero TX attempts and zero port calls, `physically_confirmed=false`, `real_online_confirmed=false`. No real native response, request payload or protected implementation was included in the host test. No full ESPHome compile/flash or electrical port scope measurement was conducted.
- Original Connect 2.1.105 `cm/modbus_server15.py` receives native master requests and implements separate slave handler, FC16 reception/internal handshake flag and register update callbacks. Its FC16-driven *software* ACCEPTED value (e.g. 04A6) is **NOT the same as proven XTR master approval or subsequent status polling**. No controller-master code or master decision rule was recovered. V56 already identified this distinction; not newly claimed.

## Existing LOCAL XTR intervention ladder (crosschecked; NOT rerun)

| Historical local run | What endpoint actually did | Distinct observable controller progress |
| --- | --- | --- |
| EXP254 / EXP255 | RX-only throughout; no native reply | 63 approval request retries and stop; 04A6/085F FC16 continue; no new 0708; EXP255 FC16 582 with ACK0 and FC03=0 |
| Current V49 | Compiler lock + runtime no TX, manually restarted | 63 cumulative FC23 requests, responseShape0, native 03E8/0864/0708 not observed in bounded console |
| EXP256 | Exactly one tested historical native response; no downstream ACK | First 03E8/count14 ~124 ms afterward, repeats due no ACK; **DHW-side 0 / COMM ERR ONLINE/LINK** side effects |
| EXP257 | Adds first 03E8 ACK | Next 03FC/count11 observed |
| EXP258 | Adds 03FC ACK | Next 0410/count22 observed |
| EXP355 | Previously qualified retained stage40 and a user controller reboot; known guarded response + full known sequence | 32/32 historical controller pages up to 06F4/count19, then 085F and 0708 service; replay geometry differs from 2.1.105 33 significant APP groups |

**Constraint:** these are *different previous experiment runs and states*. EXP355's retained context was previously qualified; not randomized TX-on/TX-off for today's V49 boot. Host logged 124 ms is not measured electrical EOF/slot/deadline. EXP256 alarm means **never** treat single-ACK/no-service as a benign endpoint. The result establishes the first missing experimental *input* in V49, not a universal cryptographic/scheduling rule or assurance another reply will work.

## Evidence classification

**PROVEN (V49 exact source + user logs):** native V42 one-shot path intentionally build-locked; no actual response was generated by V49 and no native peer response was seen in the relevant bounded user logs. An operator Arm was blocked locally rather than refused by the controller. Current V49 **has not exercised the approval-response edge at all**.

**PROVEN historical local XTR:** in the particular controlled EXP256 run, an actually delivered response was followed by native first-page 03E8; missing ACK stalled there. Further ACKs advanced ordered pages in EXP257/258. Separate qualified EXP355 successfully reached runtime.

**STRONGLY SUPPORTED / parsimonious explanation:** V49's deliberately unanswered challenges explain its residence in the observed no-responder retry branch and lack of a new 03E8/0864/0708 service phase; the existing passive 04A6/085F do not by themselves imply an approved session. This is **not** evidence of controller rejection of a reply that was never sent.

**NOT established:** the sufficient minimum reply prerequisites for a *new* controller epoch in *today's V49 conditions*, actual wire owner/physical slot, dynamic reply acceptance, master authentication algorithm, OEM 2.1.105 application parameter-map readiness, cloud Online state, or whether the XTR would progress after a newly restored guarded TX-capable endpoint. V56's original slave internal H2 does not establish master acceptance.

**Downstream vs upstream:** V67/V68 compare 33 app receipt timing after firmware version/WAIT. But the present V49 data has no observed current 0864 page, and existing historical first-response→first-03E8 progression was not exercised. Adding more passive page readiness observers cannot cross this earlier gate.

## Safety, criteria, abort/recovery and decision

**Offline POSITIVE criterion:** unchanged V49 host source refuses Arm for all three non-TX builds and current hardware diagnostics show no output; historical already-completed runs explicitly isolate successful first stage after a delivered reply. **NEGATIVE:** any actually delivered V49 native reply contradicting no-TX source and logs, or current V49 03E8/0708 phase confirmed despite the cited bounded observations. **INCONCLUSIVE:** inability to pin source or supplied transcript, or unsupported claim of exact controller decision. Results meet scoped POSITIVE only, master-side causality remains OPEN.

**Physical test target/payload/timing/current setting:** NONE — no active experiment proposed for execution. No outbound slave frame, register write, retry or plant effect. Abort offline if source/hash/logs conflict; no live rollback necessary. Hardware unchanged: V49 RX_ONLY/HARD_DENY, normal B11D/P5 fault latches preserved. Do **not** merely turn on the two compiler flags, disable guards, publish confidential native 0x0F response material or repeat EXP256's intentionally incomplete endpoint: that old one-shot produced a real communication error.

**Next actionable research boundary:** assess feasibility of a **complete, bounded, fail-closed native session responder** as an *offline architectural preflight*, using previously local-proven full-chain service and original Connect app model, not just one answer. Before any separate user-initiated live test, require exact current version/profile evidence, current owner/epoch/physical response-slot qualification, known current plant/UI condition, strict fixed message sequence scope, no spontaneous TX, runtime abort on CRC/B11D/P5/DE/peer mismatch and a recovery plan. Preflight may decide **NOT READY**. Controller acceptance beyond the first answer is experimentally unknowable from the RX-only session. Do not ask for another identical 63-retry passive cold boot: EXP254/255/V49 already show it.

## Public-source boundary

This document intentionally includes NO protected native-response transform, dynamic challenge data, emulator payload, 0708 command mailbox tool or credentials.
