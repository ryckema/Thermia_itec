# V5DCM3 — offline CM930 session/config/mailbox audit — 2026-10-17

**Status:** COMPLETE / POSITIVE for five isolated synthetic C++ host fixtures; COMPLETE / INCONCLUSIVE for historical raw-capture coverage, local XTR CM930 acceptance, icon and Online. No ESPHome YAML flashed or changed.

**Hypothesis:** Configuration pages, mailbox observations, runtime pages and native approval events can be tracked separately without treating a single 03E8 page as DCM acceptance.

**Baseline:** User-tested V5DCM2 FIX1, working RX-only/NO-TX, [V5DCM2] diagnostics visible. Its 2026-10-17 live log has FC23=0, 0708=0, page 03E8/count14 and 085F/count5 recurring, software TX zero, 0 RX resync/drops.

**Exactly controlled change:** A standalone C++17 **offline-only** model with passive Event/Observer and a separate test driver. Does not include or change ESPHome, UART, DE, physical TX, confidential cryptographic algorithms, response bytes or private mailbox commands. The 32 reference page start addresses are a historical reference sequence, not a universal XTR mandate.

**Firmware sources inspected:** recovered original Thermia Connect device_client/cm/modbus_server15.py, especially FC16/FC23 handler split, application handshake-state events, conditional device/operation request dispatch, and data-package readiness; device_client/cm/client.py for distinct configuration/operations parameter parser and cloud-reporting responsibilities. Firmware application ACCEPTED != XTR display icon or cloud connectivity.

**Observed offline tests:** C++17 -Wall -Wextra -Werror host compiler PASS and five synthetic fixtures PASS: (1) unrelated slave ignored, (2) repeated native FC16 03E8/14 + 085F/5 do NOT prove complete 32-page bootstrap/epoch, (3) mailbox request/reply and ACK-shaped records tracked separately, (4) a *synthetic* ordered 32-reference-page sequence counted as complete only for that sequence, and (5) isolated challenge/response-shaped and runtime event observations do not assert actual acceptance or display state.

**Positive:** pass host fixtures, do not conflate application/transport milestones, kCanTransmit=false. **Negative:** count mismatch or inferred acceptance from repeat traffic. **Abort:** physical TX attempt, publication of private recovered handshake/material, unexpected production config change. **Recovery:** no physical recovery needed (offline); live baseline remains V5DCM2 FIX1.

**Facts/unknowns:** Real native FC23, owner, epoch, response slot, semantic ACK, runtime/mailbox XTR behavior, DCM icon and Online remain unknown. Recurrent STAGE_D_LEDGER_FAULT remains separate from clean physical RX counters. Synthetic host tests are NOT genuine capture replay or firmware execution proof.

**Next:** V5DCM4 should independently replay existing genuine bus records with their provenance and timing into this offline model; first fix any mismatched geometry/ownership assumptions, without active TX. Full offline bundle provided in conversation; public GitHub docs only to respect confidential native emulation separation.
