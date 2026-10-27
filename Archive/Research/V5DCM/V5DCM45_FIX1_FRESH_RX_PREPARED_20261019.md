# V5DCM45-FIX1 — fresh RX qualification: source preparation

**Experiment ID V5DCM45-FIX1-FRESH-RX-SOURCE-01. PREPARED / NOT RUN before offline execution.** [Linked offline result](V5DCM45_FIX1_FRESH_RX_OFFLINE_RESULT_20261019.md).

**Hypothesis:** Distinguish historical startup RX anomalies from the present, stable RX stream without erasing earlier integrity evidence. Keep a separate, one-use manual operation guarded by a freshly qualified RX observation.

**Known-good baseline:** The user's last V45 on-device passive capture showed running HA entities, continuous incoming frames, no new faults over 195.6 seconds, seven already accumulated parser resynchronizations, historical P5 held, no actual output. Verified V44B no-output firmware remains a fallback. V45 source/host original offline 40/40, V44B 32/32.

**One controlled source intervention:** On the exact private V45 baseline, add a current-RX witness requiring 30 seconds and 100 new complete frames without subsequent anomalies; a later anomaly revokes the fresh RX privilege. Existing P5 and B11D historical records and the original parser remain unchanged. A rejected preflight Arm does not consume a successful one-use allowance. Preserve existing Configuration controls and all production entities. This is a source-only experiment, not a live action.

**Positive:** fresh historical-versus-current distinction, new-error revocation, original RX/HA entities preserved, default denial retained and bounded one-use test path unaffected. **Negative:** clearing or mutating historical fault data, stale RX treated as current, lost entities or changed hardware configuration. **Inconclusive:** user firmware compile/device validation not yet available.

**Limits, safety and recovery:** No automatic bus output, no new arbitrary register writes, no bus search, no forced device reset. User-driven physical test is separate, unexecuted and limited to a currently valid incoming request and a single bounded reply. Abort and restore V44B no-output / FIX-B2 as needed. Genuine current native request, sender identity and physical timing have not been established on the user's XTR.

**Evidence:** original user V45 capture; source diff, strict fake UART tests, YAML parser and exact component pins recorded in the [offline result](V5DCM45_FIX1_FRESH_RX_OFFLINE_RESULT_20261019.md). Confidential native implementation remains only in the user-private ZIP.
