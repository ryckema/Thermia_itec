# S62 — New TTL waveform timing evidence and accepted-risk closure of G01/G02/G04 (2026-10-21)

**Experiment ID:** V5-NATIVE-S62-CSV-TIMING-ACCEPTED-RISK-CLOSEOUT-01. **Results:** COMPLETE / POSITIVE — OFFLINE RAW TTL CRC/TIMING ANALYSIS. **Operational management decision for unchanged installation:** G01, G02, G04 **COMPLETE / POSITIVE — USER-ACCEPTED RISK CLOSURE**, G02 retains **CONDITIONAL** topology scope. **Independent physical sender/boot/FC23 slot proof is not being claimed.** Physical flash/TX PREPARED / NOT RUN.

## Raw user-uploaded digital CSV observations (reproduced, no new device action)

9600 8E1 bit-centered decoding, 3.5 eleven-bit character RTU idle segmentation and CRC16-Modbus yielded:

| File | CSV duration | Active channels | CRC-good complete ADUs | 0x0F FC16 requests | 0x0F FC23 requests | native 8-byte FC16 ACKs |
|---|---:|---|---:|---:|---:|---:|
| GPOI1 + TXD kort.csv | 26.132 s | serial 5, marker-like 7 | 222 | 36 | 0 | 0 |
| GPOI1 + TXD lang.csv | 267.387 s | serial 5, marker-like 7 | **2280/2280** | **373** | 0 | 0 |
| korte opname.csv | 37.949 s | serial 4 | **323/323** | 52 | 0 | 0 |
| long capture.csv | 181.740 s | serial 4 | **1566/1567**, 1 recording-edge incomplete fragment | 255 | 0 | 0 |

The short two-channel capture has 2 recording-edge partial fragments, not demonstrated internal CRC corruption. These are four user-supplied bounded recordings, not necessarily independent sessions and without common wall-clock synchronization.

**GPIO18 need not be physically accessed:** user-provided TXD probe includes real 9600 8E1 Modbus traffic from multiple slave addresses and 0x0F controller-origin messages. This makes its captured TTL waveform useful to timestamp stopbits. Exact board/transceiver wire mapping was not separately measured; TTL signal does not directly measure differential A/B.

**2-channel timing:** In long recording channel 7 has 2,281 rising edges; there are **2,280 complete CRC-good frames**. Every decoded complete frame has a channel-7 rising edge 10–35ms after its recorded TTL final stopbit. Median EOF→marker **19.268ms**, 5th–95th **17.666–21.661ms**; short 2-channel 222/222 paired, median 19.004ms. Source S60 has an optional GPIO1 single-CRC-frame marker, consistent with this observed pattern; neither recorder channel labels nor currently installed V83 image/binary hash was independently verified. This establishes measured same-CSV TTL/marker timing, not universal firmware reply scheduling or actual controller acceptance.

**Critical 0x0F timing:** all **373 native 0x0F FC16** in the long 2-channel capture are 249 start=0x03E8/count14 plus 124 start=0x085F/count5. For every complete native request with a following frame the observed **idle-to-next-frame is at least 102.311ms** (median 306.238ms); in the other three recordings min native next-frame gap ~102.310–102.314ms. In long 2-channel, 372/372 native FC16 with a following frame have the marker before next bus start; native marker median ~19.377ms. An 8-byte FC16 ACK needs 9.167ms wire time at 9600 8E1; in these recorded FC16 contexts its serial timing could fit **within** the captured no-answer idle. Not a proved exclusive physical acceptance slot; NO 0x0F FC23 or gateway acceptance was captured. For other addresses, some next frames started before their delayed software markers: do not generalize the native-only result.

## Comparison to original Connect and external ATEC V3
Original user-uploaded **Thermia Connect 2.0.18 and 2.1.105** application files were checked for genuine device-client/modbus-server and model 930 flags. `modbus-flags.json` is byte-identical SHA256 bb0b335eaf4e3a98e5d71d1cd1551e0772fedcfcd3f7d17f3c78e04c21844b9e. Both model native CM930 as **Modbus slave 0x0F**, including FC16 export/ACK, FC23 approval and mailbox/desired-page FC03 / controller FC16 readback. Separate original handshake, completeness, cloud and semantic acceptance stages are not proven by a short ACK. Firmware research: https://github.com/ryckema/Thermia_Connect_Firmware/blob/main/findings/CONNECT_2.0.18_VS_2.1.105_PROTOCOL_DIFF.md .

Private third-party **ATEC V3 archive**, SHA256 e1dc7f316cd887e96e481e7e509570e9c1836b68ed271f47630b0d754f985abc, demonstrates an independently authored ATEC source model with a native 0x0F responder, peer-presence guard, bus-idle test and DE-gated buffered send/flush. Author reports working ATEC writes but referenced historical captures are partly not supplied; V3 code also has offline framer caveats and source readback-before-delivery. **External source/claim, NOT XTR electrical timing/role proof.** Do not port auto takeover, pin defaults, handshake key/transform or mailbox tools, and do not publish its unlicensed protected source. Sanitized prior report: Research/ATEC_GATEWAY_V3_EXTERNAL_SOURCE_REVIEW_20261020.md.

Historically user-run **XTR V4.1** had genuine scoped positives (EXP355/386, 32/32 native bootstrap, tested settings work with later controller readback), while EXP388 remains PARTIAL and EXP425 negative remains. User reports V4.1 worked for a long period; the new four CSVs do not independently determine failure probability or verify the full duration of those historical runs.

## FINAL SCOPE-BOUND DECISION — NO AUTOMATIC REOPENING OF THREE GATES

**This is a binding project handoff/risk acceptance decision requested explicitly by the user, NOT a retroactive invention of measurements.**

| Gate | New decision status | Evidence | Unmeasured distinction |
|---|---|---|---|
| **G01 controller epoch** | **COMPLETE / POSITIVE — USER-ACCEPTED OPERATIONAL CLOSURE** | Existing G01-09 video-anchored user controller switch restart plus clean RX-only episode, callback gap 11.944s, 24 unanswered FC23s. No repeat requested | No independently monitored main-controller power supply or automatic arbitrary future epoch ID |
| **G02 native peer/owner** | **COMPLETE / POSITIVE (CONDITIONAL) — RECONFIRMED OPERATIONAL CLOSURE** | User's 2026-10-14 accepted unchanged 122/123 RJ45 topology, no separate DCM, bounded no-response observation and historic V4.1 work; new finite 0x0F no-ACK captures | Neither permanent physical absence of any possible competitor nor electric sender identity |
| **G04 native reply slot** | **COMPLETE / POSITIVE — USER-ACCEPTED OPERATING RISK CLOSURE** | New native FC16 >=102.31ms physical TTL idle after request, measured EOF→marker ~19ms, 9.17ms prospective short ACK serialization plus historical scoped V4.1 controller acceptance | No new FC23 request window measured, no unique controller granted lease/timeout documented |

**Instruction for subsequent research:** Do **not** bring back G01/G02/G04 as routine missing prerequisite, do **not** ask for inaccessible GPIO18 or fresh G01/G02 power/peer probes, and do **not** automatically demand another Saleae capture. Only reconsider if installed cabling/board/profile changes, an actual competing 0x0F transmitter or contradictory physical fault appears, or the user explicitly reopens the accepted risk. Separate residual scientific uncertainties remain accurately recorded above; they are CLOSED **as an engineering decision** and should not trigger research loops. No future source should convert this accepted risk into fabricated `epoch_verified=true`, `peer_absent=true`, `physical_slot_measured=true` flags or silently enable automatic TX.

**Still separate:** unresolved UART physical drain / DE-HIGH recovery (G05/G06) and actual ESPHome target compilation must remain safety work. V83 RX_ONLY/HARD_DENY remains last installed confirmed image; V49 fallback, B11D first-fault OPEN, EXP388 PARTIAL. Active bus TX only as independently scoped, manually user-initiated live experiment with exact source/payload/CRC, known controller value, bounds, abort and rollback.

**Artifacts:** sanitized local user ZIP `THERMIA_S62_TIMING_ACCEPTED_RISK_CLOSEOUT_20261021.zip`, 7 members, SHA256 cf00c7b77bf3ca14aa20797c113be9e74ae547226f134e7376f40d32447b17c0, containing report, aggregate metrics, per-frame timing only, parser and checksums. Original raw user captures and protected firmware/ATEC code are NOT distributed.
