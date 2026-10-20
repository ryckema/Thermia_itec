# V5DCM97 — Original Connect local versus cloud gates

**Experiment:** V5DCM97-CM930-LOCAL-VS-CLOUD-GATES-OFFLINE-01. **Status: COMPLETE / POSITIVE (offline source-path checks, not device acceptance).** Date 2026-10-20.

**Baseline:** Last user-verified V83-FAS1 RX_ONLY/HARD_DENY, original V49 rollback, EXP388 RUNNING/PARTIAL, prior separate B11D first-start anomaly OPEN. One controlled offline change: inspect Connect 2.1.105 original cm/client.py and cm/modbus_server15.py, compare high-level architecture with ATEC V3 external source. No hardware action, TX, flash, or compilation.

**OBSERVED original source:** CM930 transport handshake ACCEPTED triggers info request in WAITING_FOR_DEVICE_INFO or operation request in OPERATION. Before onboarding, collected registers may feed InfoCollector, profile loading, and data-package requests. Publishing Info triggers WAITING_FOR_SET_DEVICE_INFO and external response subscription with follow-up check. Generic sensor/alarm/configuration/operation parsers feed under OPERATION, while normal success event sets OPERATION, subscribes remote/local control topics, publishes parameter map and requests operation data. Cloud master-settings identity is a prerequisite for remote topic subscriptions in original client; it is not shown to be a controller-level requirement for native RS485 access.

**EXTERNAL ATEC V3:** author-reported cloud-independent gateway behavior is an external claim; historical captures absent, no proof of XTR electrical ownership, session or semantic acceptance. No protected authentication/handshake/mailbox implementation published.

**OFFLINE VERIFICATION:** 16/16 source-path assertions passed against original user-uploaded device_client.zip. Assertions show branch code exists, not runtime reachability. Device TX=0, compiler NOT RUN, flash NOT RUN. Abort analysis on source-path/hash discrepancy. Hardware rollback N/A.

**STRONG CONCLUSION:** Original Connect cloud onboarding gates normal Connect application publication/subscription; transport-level acceptance and information gathering may precede it. Whether XTR native local write semantics require further controller-side session processing remains UNKNOWN. Keep original baseline unchanged.

**NEXT V98 OFFLINE:** compare native data acquisition events versus application publication paths, without implementing protected or active TX.
