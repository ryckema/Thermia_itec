# V5DCM82 — single-owner TX-HARD-DENY driver interface + B11D/watchdog scheduling (exact V49 source + host only)

**Experiment ID:** V5DCM82-SINGLE-OWNER-HARD-DENY-SCHEDULE-HOST-01  
**Date:** 2026-10-20  
**Status: COMPLETE / POSITIVE — exact original-source review + RX-only HOST assertions; INCONCLUSIVE/UNKNOWN for physical native TX.** No actual ESPHome/ESP-IDF build, firmware flashing or bus operation.

## Hypothesis, verified baseline, relevant earlier evidence and ONE change

**Hypothesis:** a *single-owner* driver-shaped interface that has NO UART writer, GPIO setter, direction-switch writer or native payload generator can keep the original V49 V45 B11D integrity decision and separate 1s watchdog in a fail-closed RX-only state across 50ms versus 1s scheduling interleavings. It must fail on attempted TX, attempted DE-high, PreGuard, wrong owner, switch-versus-GPIO mismatch, historic output, session/generation change or clock regression. This cannot establish physical slot or actual controller acceptance.

**Last USER-verified XTR known-good baseline:** installed V49 RX_ONLY/HARD_DENY with TX attempts0, controller manual restart callback gap **10.351s**, V49 RX cohort **285 independently CRC/byte-matched frames over 30.532s**, **63 cumulative unanswered native 0x0F FC23 challenges** across noncontinuous logs. Current physical electrical peer, wire EOF, DE/owner, response slot, original XTR 0x0867 controller version and exact flashed image hash remain UNKNOWN. EXP388 remains **RUNNING / PARTIAL**, not closed.

**Earlier source/local evidence:** EXP255 received unanswered native requests; EXP256 a guarded first real response induced first settings page but incomplete follow-on caused actual COMM ERR ONLINE/LINK; EXP257/258 sequential ACK advancement; EXP355/386 historical 32 native controller page ACK + runtime sequences. V74–81 are separate source/host milestones. Original Connect 2.1.105 33 app groups/C2 are not the controller's historical 32-stage ACKs.

**ONE controlled OFFLINE change:** New deliberately **NONDEPLOYABLE** `v82_locked_port.hpp` implements one logical borrowed-UART identifier and read-only supervisor access from synthetic `PinSample` data; it calls the original verbatim `v5dcm45::observe` on clean RX; refuses all native TX/DE-high/PreGuard requests with a sticky first fault and offers NO physical Port/GPIO/UART/output interface. A deterministic host scheduler tests both orderings of B11D and watchdog calls. Original V49 source/production YAML and actual installed V49 are UNCHANGED. This is a source-migration interface design, NOT a real ESP32 physical driver.

## Exact provenance and tests actually performed

1. Original **69-member** user V49 archive verified SHA256 `62afe39629102a3daa06f09eab3ed159f44437d702fb8d3904c61e62e2a85630`; copied the **nonsecret original V45 decision header byte-identically**. Source auditor **30/30 checks passed**, including original source for all 50ms B11D, 1s watchdog, GPIO21 comparison, V43/V44B dual UART/DE borrow, V42 hard-deny compile gate, 32 long-profile shapes and alternate page geometry. No original protected V43 private algorithm was copied into public output or called in V82.
2. Host-only C++17 fixture: **38,081/38,081** assertions PASS in each of (a) strict g++, (b) ASan/UBSan, (c) noexceptions/noRTTI. Four deliberate forbidden compiler builds **DENIED 4/4** (`ESP_PLATFORM`, `ARDUINO`, `V5DCM42_PRIVATE_TX_BUILD`, `V5DCM42_HARDWARE_PORT_REVIEWED`).
3. Host scheduling: B11D every **50ms** for **30 virtual seconds per phase**, 59 synthetic 1s-watchdog phase offsets (0..986ms in 17ms increments), both tie orderings on coincident calls, 80 synthetic DE/GPIO/legacy fault injection cases and 12 further first-fault variants. All source/hardware inputs are synthetic. These assertions **do not** reproduce ESP32 task preemption, GPIO edge timing or actual UART drain.
4. Pure host code has **no Port/driver writer methods**, so physical UART/GPIO/DE writes cannot occur. Any TX, DE-high, or PreGuard request is deliberately denied and latched (not interpreted as a completed native request). Original V49 RX settings, HA entities, red/brown diagnostics, bus-health bookkeeping, B11D/P5/FIX2 historical sticky faults were not modified.
5. Original V49 source has **two** actual borrowed UART/DE actors, with both B11D and periodic watchdog recognizing **V44B only**. Original V44B's watchdog may defer while in **PreGuard**, even before DE HIGH; B11D only recognizes bounded active TX window (Fill/Drain/PostGuard). V82's locked port does **not** allow even PreGuard to defer the watchdog. This proves a stricter *RX-only* policy, not the safe transition for a true transmitting driver.

## Source geometry evidence (no current-controller assumption)

Original V49 `geometry` discriminator metadata distinguishes:

| Native page | Shape 1 count | Shape 2 count |
|---|---:|---:|
| `0x03E8` | 13 | 14 |
| `0x0410` | 21 | 22 |
| `0x0492` | 9 | 11 |
| `0x051E` | 9 | 10 |

The historically confirmed 32-page local initial-sync chain is **not** sufficient to determine the current controller shape/firmware `0x0867`. The installed V49 currently supplies no new verified firmware/profile evidence. A future response encoder must fail closed on contradictory/unknown page geometry; a 32 controller ACK chain is not proof of genuine Connect APP33/C2/Online.

## Findings and limits

**PROVEN, ORIGINAL SOURCE / HOST ONLY:** exact split UART/DE ownership and watchdog asymmetry; byte-identical original V45 decisions; source-dependent geometry split; the new single logical RX-only owner can reject unsafe synthetic state without physical output, including across both simulated 50ms and 1s read-only observers. Source migration entry points are documented separately in the host ZIP.

**STRONGLY SUPPORTED:** before any genuine native integration, *one actual physical UART/DE authority* must be shared by the original B11D+watchdog, preserve first-fault history and per-ADU callback routing, and implement complete privately held dynamic first-response + current-profile 32-page FC16 ACK/runtime FC16/FC03 service. Independently electrical wire EOF, peer/slot and actual DE-UART drain scheduling must be qualified; abstract source tests are insufficient.

**OPEN / UNKNOWN:** actual source-to-ESP32 driver patch, ESPHome compilation/on-device watchdog timing, electrical 0x0F owner/EOF/slot, current controller version/geometry, private backend acceptance, full real runtime/ACK sequence, Connect APP33/C2/cloud. The V82 prototype cannot transmit and was not installed.

**Positive criteria:** 30 source checks; 38,081 host checks each build; 4 compile denials; no hardware-output API or bypass. **Negative:** any unexpected output path, accepted preguard TX, cleared first fault, omitted frame/profile guard or incorrect owner would invalidate V82; none occurred in host scope. **Inconclusive for physical TX and current XTR native session**, which was never attempted.

## Safety, abort and follow-up

No physical target frame/register/current value/payload or sending interval in this **offline-only** experiment. Abort host work if source hash/compile/test fails, discard files. Hardware rollback N/A because V49 was not changed. Do not enable original V42/V43 flags or repeat EXP256's isolated first response; that historical incomplete service caused COMM ERR. Keep **EXP388 RUNNING / PARTIAL** until the user's real evidence closes it.

**NEXT V5DCM83 (NOT RUN/PREPARED):** source-aligned *RX-only* YAML migration candidate that consolidates the one physical UART/DE observer/seam and feeds identical ownership snapshots to B11D and watchdog, keeping native output hard-denied. First perform source validation while preserving production entities/substitutions, historic first-fault bookkeeping and V49 rollback; no immediate live flash or TX. Real TX is a separate later bounded experiment after full protected service and independently measured electrical slot/owner proof.

**Reproducible nonsecret host artifact:** `V5DCM82_SINGLE_OWNER_HARD_DENY_SCHEDULE_HOST_ONLY.zip` SHA256 `51d6056a933e1ecbf04913a63db7bf447862e180adf827aa17db5a8fb820e7e2`, ZIP CRC verified, 10 files (README, migration map, result, original V45 nonsecret predicate, new host locked interface, test, compile script, source audit, audit JSON, checksum manifest). Not a flashed firmware and contains no protected native reply/security or mailbox implementation.