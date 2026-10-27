# V5-NATIVE-SERVICE-12 — V4.1 service integration source audit

Date: 2026-10-20
Status: PREPARED / NOT RUN — SOURCE REVIEW ONLY
Baseline: user-verified V83 FAS1 RX-only, TX=HARD_DENY; EXP388 RUNNING / PARTIAL; B11D startup anomaly OPEN.
Reference: Write (Beta)/thermia_itec_xtr_m_waveshare_write_beta_v4_1.yaml, blob SHA 8e8a82689e53528a8b751a1abbd901f683b6b238.

## Observed facts
- In the V4.1 source, a CRC-valid received ADU updates thermia_last_valid_frame_ms and thermia_valid_frame_count before dispatch (approx. lines 2100-2125).
- Source comments distinguish cold-boot R1, first exact 0x03E8/count14 FC16 and ordered initial configuration pages (approx. 2132-2140).
- A 32-page address/count family appears in the FC16 configuration-shape detector (approx. 2491-2506). This shape detector is explicitly observation-only; it does not establish an accepted 32-page session by itself.
- V4.1's runtime FC16 responder constructs an 8-byte FC16 ACK, computes CRC and increments its ACK/page counter directly after local UART write and flush (approx. 4020-4050). Local ACK construction/flush is **not** independent confirmation of controller acceptance.
- The 22-page resume branch is explicitly described as unreachable legacy source because no UI/action sets resume_started (approx. 8565-8567); it is not proven live.
- Runtime handlers distinguish accepted payloads, unknown 0x085F, unsupported 0x0834 and other fail-closed conditions (approx. 3990-4020).
- In a 0x0546 republish path, the source compares the requested word with the observed controller page and checks that all other page words remain identical (approx. 3860-3900). This is a model for independent semantic readback, not proof that V5 implements it.

## Strong conclusions
- Port the initial ten-page behavior as **source-derived** with controller-request progress gates; do not transplant source ACK counters as confirmation.
- Keep the 22-page resume path disabled until an independently evidenced trigger and transition is identified.
- Preserve one physical TX owner, full CRC/epoch/slot/peer guards and V5 B11D supervision.
- Neither an FC16 ACK nor 32/32 configuration pages proves a valid Thermia Connect/DCM application session.

## Unknowns
- Private V5_NATIVE_TX_V41_INITIAL_HANDLER_OFFLINE_20261020.zip, SHA256 0428a5a31dcab66730ba3acbe13ec92cf6ccb97e377870166779c4683fef0898, is not among files currently mounted. Its precise V5 source and integration interfaces have not been verified in this turn.
- Exact complete modern V5 handler wiring, B11D owner integration, electrical response window and native semantic acceptance remain open.

## Next action
Retrieve the exact private V5 service-11 archive or verified complete V5 source. Then implement the single V5-native actor (startup, ten initial pages, gated resume, runtime FC16, FC03/0708, refresh, semantic readback) and test offline, retaining HARD_DENY. No physical TX or flash from this source audit.

Evidence scope: original GitHub V4.1 source review only; no new test result or device runtime observation.
