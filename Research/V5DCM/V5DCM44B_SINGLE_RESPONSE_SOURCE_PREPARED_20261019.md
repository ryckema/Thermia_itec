# V5DCM44-B bounded one-shot source contract

**Initial status: PREPARED / NOT RUN**, followed by [offline source RESULT](V5DCM44B_SINGLE_RESPONSE_SOURCE_RESULT_20261019.md). Actual XTR TX remains a distinct, unexecuted live experiment.

**Hypothesis:** unchanged last-known-good V43 FIX1 production RX/HA can coexist with optional one-shot reply transport using the existing UART and ESPHome-owned DE switch; output must require explicit user Arm plus a fresh CRC-valid incoming controller request. No unsolicited bus frames or register-write scans.

**Known-good:** user V43 FIX1 healthy passive RX, no actual native output, installed image digest unknown, safe FIX-B2/FIX2 RX-only recovery. Previous V40 historical cross-model 7/7, V41 dynamic host backend, V42 one-use host UART, V43 user passive pass; V44-A live button denial/abort positive but overall partial.

**One controlled change:** private differential source overlay, not a device flash. Arm valid 30 seconds, at most one exact fresh response per boot, abort on invalid RX/DE/competing peer, bounded 70ms after parser callback, original 1 second RX watchdog yield only during bounded active response. Two explicit compile switches and existing Configuration buttons; no second UART reader. The owner/epoch/slot physical evidence is UNKNOWN and described as accepted-risk assumption, not local proof.

**Positive:** SHA-pin parent, preserve sensors/entities/sticky diagnostics, compile fake UART default-denied and explicitly fake-enabled modes, one-response only, replay and failure denial, DE-low recovery. **Negative:** unarmed sends, duplicate output, RX integrity regression, broken watchdog or abandoned DE high. **Inconclusive:** actual compiler/hardware timing not available. Abort by not flashing source; later live trial requires independently reviewed current response and recovery. No private security algorithm or key published.
