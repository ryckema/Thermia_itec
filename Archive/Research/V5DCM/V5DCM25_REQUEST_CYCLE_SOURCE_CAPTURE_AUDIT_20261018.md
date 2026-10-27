# V5DCM25-REQUEST-CYCLE-01 — original Connect request lifecycle versus captured native 0x0F traffic

**Status: COMPLETE / POSITIVE for OFFLINE firmware/source matching and passive historical-capture correlation.** 2026-10-18. Device experiment **V5DCM23 FIX2 remains RUNNING / PARTIAL (1/33)**. This report contains no private 0x0F response/emulation, 0x0708 mailbox tooling, authentication algorithm, credentials, or outgoing payloads.

## Objective and boundaries

**Hypothesis:** Connect 2.1.105 profile-dependent package requests have observable counterparts in native slave 0x0F receive traffic, separate from the old R6 32-page Stage D and the present V5DCM23 passive 33-significant-page ledger.

**Known-good baseline:** currently user-flashed V5DCM23 FIX2, first short live snapshot: portable 1/33 (03E8/14), consistent with RX33, B11C/B11D clean, DE low, HARD_DENY software output; exact deployed binary provenance and native session/owner/epoch unresolved. No run of a new firmware image.

**One controlled change:** independent offline comparison only, unchanged original source and log bytes. Decoded existing CRC-valid frames for counts, timeline and groups without synthesizing replies or modifying equipment.

**Source provenance:**
- User-original Connect 2.1.105 extracted AppFS ZIP SHA256 `42d365c89a7a0cc76138c57c1bf50cfd95c33c3ffcf7aef26f39c01b7c81f49e`.
- User-supplied `device_client.zip` SHA256 `18ebe6190bbcfff364ca27af9dbf31c8b6e66a7a828d7869b00d32f7012590ac`. **Byte-for-byte identity verified for all three relevant Python modules** between ZIP and original AppFS: `cm/modbus_server15.py`, `cm/cm_client_type.py`, `cm/client.py`. AppFS CM930 flags configuration examined, but its complete contents are not reproduced.
- Local historic `thermia_capture_20260925_090550.log` SHA256 `f23cd2f18764d77220409d2cf9e0caf2fc3b7c1aa1d2a1405f13c9fdbbbc0e2d`. Note older source geometry (settings first block 13 words), **not** today's V5DCM23 XTR geometry (14 words).
- Comparative `itec_eco5_gateway_20260926.log` SHA256 `3836b7885dfe246398fc2a053bf1be286df4001df3ab9703952c5775db1ae91f` and `itec_eco5_gateway_20260928.log` SHA256 `55583e2ec2cd940a45f17d10b0b7a523865ccc25b3ed14c099a2eecd2a12160c`. Treat peer model as **cross-model corroboration**, not local XTR proof. These do not establish genuine Online/DCM module provenance.

## 1. Original Connect 2.1.105 source findings (firmware-derived, not automatically XTR bus proof)

1. CM930 native Modbus server is explicitly configured for **slave 15 = 0x0F** (`CM930Client.SLAVE_ADDRESS`); it has dedicated settings, handshake and operations blocks. **Physical ownership/collision on the user's bus is not resolved** by a host-side server address declaration. The earlier working simplification `0x06 = full Online application interface` remains unsupported; 0x06 version/accessory evidence is separate.
2. Source state machine starts waiting for device information. A recognized handshake-related exchange changes its internal state, **but the actual `HandshakeState.ACCEPTED` may be asserted on the first qualifying received native FC16 block**, not after 32 complete pages. This is a *software-internal* accepted flag, NOT controller-authenticated acceptance, Online registration, or TX permission. Do not substitute the 32/32 Stage-D guard for the vendor's own acceptance condition.
3. Register group request bookkeeping uses **three distinct request categories**: upper settings, lower settings and operations. The original CM930 flags map ties groups/bits to native FC16 address ranges. Separately, other group indications can signal updates; do not confuse request versus update flags.
4. Version/profile load creates the `CMClientParameterUpdateState` pending set from **sensor + configuration numeric dependencies** (`_get_all_data_package_to_request()`). Requests for information and normal operation are generated at different runtime stages. Receipt of a native block clears its corresponding request bit and pending-profile bit, while onboarding/operation state also governs what gets requested. Full parameter-map publication is deferred until all selected significant groups have been received.
5. **Three distinctions are mandatory**: (a) firmware's broad register request mechanisms, (b) 33 profile-significant group readiness (W2=15, W3=10, W4=8 for derived profile 2.4.2), and (c) old R6 Stage-D ordered 32/32 transport exercise. Neither is native session ownership, C2 authorization, or semantic settings-write proof.

## 2. Local older XTR capture — positive with negative control

The passively observed status/read response changed at approximately **t=68.23s**, marking requests for **15 upper-settings groups + 16 lower-settings groups + one operational group**. The underlying read-only mailbox bytes were inspected privately but are not published. **The source code's bit-range maps match the physical FC16 start addresses.**

| Observation window | Native settings FC16 groups | Other frames |
|---|---|---|
| t=0 to 68.23s **before** request transition | **0** upper / **0** lower, across 536 CRC-valid frames | 32 recurring operational frames; these demonstrate baseline polling |
| t=68.23 to 101.92s **after** transition | **15 distinct upper + 16 distinct lower = 31/31 requested settings groups** | 8 operational frames (two distinct operational ranges), 39 corresponding FC16 ACKs total, 315 CRC-valid frames |

First requested settings FC16 arrived ~**0.07s** after the read-back change. All 31 settings groups appeared before next observed status change ~**33.69s** later. The operational request group also appeared, but unrelated periodic operational traffic continued. Thus **requested group start/count receipts and unsolicited periodic activity MUST be counted separately**.

This is a *local observation of request/receipt timing*, **not proof the request was made by a genuine Connect module**; the user does not have one for new captures. The first block was 03E8/count13 and an additional historic geometry was 0410/count21. Modern XTR selected geometry independently requires 03E8/count14 and 0410/count22; do not silently equate these captures to today's shape.

## 3. Independent model corroboration — Eco5 gateway historical logs

Cross-model capture `20260928` contains **repeated** broadened-request → FC16 burst → decreasing request indications:
- After a brief initial request phase, an expanded status at **t=377.50s** is followed within 34.12s by **16 distinct upper + 10 distinct lower** native FC16 group ranges. Some pages repeat, and operations remain concurrent. The first lower-settings block arrived ~0.09s after transition, with 14-word first-block geometry.
- Second event at **t=617.86s** repeats the same 16 upper and 10 lower distinct groups over ~30s, while the pending indications subsequently narrow.
- Third similarly broadened event at ~922.77s corroborates recurrence. The separate 20260926 gateway capture contains an analogous expansion at ~815.49s and staged clearing thereafter.
- **Negative-control nuance:** regular FC16 data blocks can exist even when no corresponding request bit is shown (periodic telemetry). Therefore observing one significant page alone is NOT enough to infer that a Connect read request was accepted.

These are **cross-model** correlations. Neither file is a proven genuine DCM/Online capture nor a live result for FIX2.

## 4. Meaning for V5DCM23 FIX2 and R6 D=4

- **Observed live XTR:** actual portable ledger only 1/33, repeated 03E8/count14, clean parser, independent older gate D=4. No newer accepted request-vector trace is included in its short live result.
- **STRONGLY SUPPORTED:** the active firmware request lifecycle matters to full package availability. A passive 1/33 ledger could reflect a controller not being in a complete profile-request/synchronization context; it does **not** by itself diagnose a parser error or an incomplete 33-group profile map.
- **HYPOTHESIS:** missing full request/operation initialization is a material cause of the live 1/33 outcome. **Not proven** until contemporaneous *native read-only* request-transition/receipt evidence is available from the current device.
- **Important correction:** the vendor's `HandshakeState.ACCEPTED` is a software-side event and does not require the old independently designed R6 Stage D 32/32 ledger. A sticky Stage-D failure must remain safely blocked, not bypassed simply because the vendor's state machine is less strict.
- **OPEN:** actual first R6 D=4 cause, local slot owner/epoch, complete C2, genuine native Online, authorization to emit application frames, exact flashed SHA, RX-only HA identity parity (private FIX2 180 vs full-monitoring 262 named).

## 5. Safe next action

**Prepare V5DCM26-REQUEST-RECEIPT-OBS-01, PREPARED / NOT RUN** as a single passive-only extension of FIX2: timestamp *already observed* high-level transitions in the three request-category counts and the next CRC-completed native FC16 group receipts; publish only grouped counts and intervals (not confidential request/mailbox bytes), preserve existing V5 callback, parity, HA names, DX fail-closed, DE low, HARD_DENY, bounded logs. No new UART reader, no active requests, no identity claim. Source-only identity and statistics parity is required before generating a candidate production YAML.

**Positive:** clear request-count → matching FC16 timing linked without observer regression or TX. **Negative:** requested group sequences absent despite an independently observed high request-count state; **inconclusive:** no request transition occurs. **Abort:** any bus/HA regression, parser loss, TX attempt/DE high; revert to previous verified RX-only. A prepared file/compile is not a physical experiment. User must initiate flash/run and supply minimal result before marking COMPLETE.

## Safety / publication constraints

No physical TX, no device reboot, no new live run, no ESPHome compilation, no firmware patch in this step. Offline scripts/raw mailbox details retained only in private working session; NOT committed. No source of confidentiality-sensitive response handlers or protected mailbox algorithm published. No reason to request compiler output.
