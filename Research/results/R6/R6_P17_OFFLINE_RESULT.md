# R6-P17 — offline FC23 response vs ACK/runtime (2026-10-10)

**Status:** COMPLETE / POSITIVE for observed cross-model phase relationships; COMPLETE / NEGATIVE fixed immediately causal/linear handshake; COMPLETE / INCONCLUSIVE semantic acceptance/owner/local XTR behavior.

**Hypothesis/baseline:** After FC23 response an immediate 03E8 settings ACK and 085F ACK unlock 07D0. Baseline R6-P16: 6 reply-bearing Eco5 restart segments and one without reply/gateway. **Controlled change:** offline reparse two genuine Sep26/28 source logs, CRC check, split >5s all-address boundary, match FC16 responses to requests by slave/start/count in 0–1s window; classify first FC23, first 03E8 settings ACK, first 085F ACK, first 06F4 and 07D0. No hardware, no TX, no proprietary response content.

**Validation:** 19,893/19,893 recorded ADUs CRC-valid, 16/16 offline checks PASS. Cross-model FC23 geometry is read 0730×8/write 071C×8 to slave 0F; observational only, not XTR write permission. Six restart phases with observed FC23 response each later have FC16 03E8 setting-page request+ACK and eventual first 07D0. All six have matching 085F FC16 ACK **before** first 07D0. But three 085F ACKs occur **before** FC23 response, and three **after**. Two first 03E8 ACKs are more than 108s after FC23 reply; other four ~0.12–0.14s.

| Phase | First 03E8 ACK relative FC23 reply | First 085F ACK relative FC23 reply | First 07D0 relative FC23 reply |
|---|---:|---:|---:|
| Sep26 restart 1 | +0.137s | -1.398s | +36.936s |
| Sep26 restart 3 | +0.122s | +63.408s | +67.636s |
| Sep28 restart 1 | +0.123s | -1.368s | +34.654s |
| Sep28 restart 2 | +108.653s | +143.171s | +145.105s |
| Sep28 restart 3 | +108.507s | +144.956s | +149.250s |
| Sep28 restart 4 | +0.124s | -1.319s | +34.648s |

**Control Sep26 gateway absent:** 41 FC23 requests, no recorded FC23 response, 82 FC16 085F requests and 157 FC16 04A6 requests, zero FC16 0F ACK and no 03E8 or 07D0. This is NOT a single-variable control: gateway itself absent, so cannot infer FC23 unique causal gate. Initial mid-session recording sections cannot be treated as startup controls either.

**Conclusions:** Sequence 085F ACK before first 07D0 is replicated in all six restart segments, but no universal order between 085F ACK and FC23 reply; a valid FC16 geometry ACK does not establish semantic acceptance. Hypothesis: separate gateway presence, FC23 exchange, settings and service/runtime stages. Unknown: power-on epoch, accepted challenge state, owner, XTR applicability. Positive: matched observations; negative: universal instant linear handshake; inconclusive causal semantics. Abort: CRC mismatch, pairing ambiguity, unsafe TX/write inference or confidential response disclosure. Recovery: none, offline. Next R6-P18 proposed OFFLINE / NOT RUN.
