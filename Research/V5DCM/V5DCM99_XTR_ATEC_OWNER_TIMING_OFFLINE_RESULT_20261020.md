# V5DCM99 — XTR/ATEC V3 ownership and response timing (offline)

**Status:** COMPLETE / POSITIVE (offline evidence classification, not TX authorization). **Date:** 2026-10-20.

**Baseline:** user-reported V83-FAS1 RX_ONLY / TX=HARD_DENY, V49 rollback; EXP388 RUNNING / PARTIAL and B11D initial fault OPEN. Source archive supplied FAS1 README itself says PREPARED / NOT FLASHED; do not confuse source archive label with later deployment confirmation.

**OBSERVED XTR:** Strict CRC-valid extraction across 5 local historical logs: 337 FC16 requests addressed to 0x0F, 306 FC16 ACK frames and 122 FC03 requests. Sep24 21/21 adjacent FC16 ACK and 13/13 adjacent FC03 responses; Oct03 162/162 adjacent FC16 ACK and 66/66 FC03 responses. Corresponding log timestamp differences were 13–42ms (Sep24) and 12–57ms (Oct03). Sep25 09:05 has only 42 ACK of 73 requests, preventing a naive completeness claim. Timestamps indicate inter-record deltas, NOT exact RS485 EOF-to-SOF response delays or owner identity. ACK != semantic setting acceptance.

**OBSERVED external ATEC source:** 8s automatic passive listen from delivered YAML, 15s recent gateway-reply detection, takeover-capable/DE pin/other-gateway-absent gates; targeted 0x0F FC16/FC03 responses; 3000us framer gap and 1500us pre-send idle check; DE lead 50us and lag 100us; disarm on competing gateway reply. Source-confirmed coalesced-frame loss risk already documented in independent ATEC review. These heuristics are not direct electrical ownership proof. No protected authentication, response bytes or private mailbox tooling reproduced.

**STRONG CONCLUSION:** XTR has native 0x0F request-response cycles in historic captures. Their response source cannot be identified from a single tap and timestamps cannot establish safe wire-level slot timing. Consequently EXTERNAL ATEC auto-takeover cannot be transplanted or auto-enabled on XTR. Source and offline evidence are not XTR live gateway acceptance.

**UNKNOWN:** physical origin and replaceability of the existing 0x0F responder; current bus epoch and exact wire idle gap; application session authorization.

**NEXT:** passive-only ownership provenance and microsecond wire timing where available, then scoped user-initiated test only after guard review. **NO-GO automatic 0x0F takeover** currently. No flash, no bus TX, no compile. Detailed local result, reproducible CRC script and JSON: XTR_ATEC_V3_OFFLINE_COMPARISON_20261020.zip (conversation artifact).
