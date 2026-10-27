# V5DCM38-PRIVATE-RESPONSE-PROVIDER-OFFLINE-01 — Prepared contract (2026-10-19)

**PREPARED / NOT RUN** at the start; the linked [offline result](V5DCM38_PRIVATE_RESPONSE_PROVIDER_RESULT_20261019.md) records subsequent execution.

**Hypothesis:** a strictly bounded host-only private response-provider interface can distinguish existing CRC-valid native request metadata, external session/slot evidence, confidential backend output, a test mock and actual controller acceptance. It must deny all production egress.

**Verified known-good baseline:** user's FIX-B2 last 204-second passive health baseline, HA telemetry, 393/393 HARD_DENY and zero UART writes; old RX-only FIX2 fallback. Parent source ZIP SHA256 `fdc09c5927b5a351163db95db96dc467abd43cb27e1e7fc8068782bea4a677c7`. Prior V4.1 EXP386/387 local guarded positives, EXP388 partial, prior V5DCM32 rejoin integrity negative and V35–V37 offline work are preserved.

**Single controlled offline change:** implement a separate C++17 host-only provider, no modification of ESPHome YAML, controller, sensors, production bus parser, firmware build or hardware. Incoming target classification is a native local 0x0F FC23 request as verified by the existing parser. No outgoing live frame or register value is defined in this offline test. Simulated response sizes and timing are host-only limits, not vendor timing.

**Positive criteria:** compile/run host success plus adversarial tests for source integrity, stale/replayed/foreign scopes, missing independent owner/epoch/slot evidence, mismatched or invalid response, original sticky error conditions, failed mock delivery and cancellation. Verify all physical-authority and Online flags remain false, embedded guard forbids output, original B2 remains unchanged, private archive checksum/re-extraction passes.

**Negative criteria:** untrusted inputs grant output, duplicate output possible, any simulated event is treated as real accepted session, any production UART path is enabled, any source pin is violated. **Inconclusive:** reference files/tests absent or compilation not possible. Actual controller acceptance remains OPEN even after successful host tests.

**Abort/recovery:** discard failed host addition; do not reset original RX faults. No physical rollback is necessary because this preparation authorizes no live execution. A later active experiment will require independently documented current request/slot, privately reviewed exact response, bounded retries, effects, abort and known-good rollback.

**State:** PREPARED / NOT RUN for the original contract; separate RESULT is COMPLETE / POSITIVE for the finished offline-only tests.
