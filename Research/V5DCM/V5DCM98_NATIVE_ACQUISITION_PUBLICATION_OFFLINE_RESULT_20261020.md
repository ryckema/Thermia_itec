# V5DCM98 — Native acquisition versus application publication

**ID:** V5DCM98-CM930-ACQUISITION-PUBLICATION-01
**Status:** COMPLETE / POSITIVE (bounded offline source-path audit; not XTR acceptance)
**Date:** 2026-10-20

## Baseline / one change
Last user-verified V83-FAS1 RX_ONLY / HARD_DENY, original V49 rollback, EXP388 RUNNING / PARTIAL, earlier B11D first-start anomaly OPEN. Audit only original Connect 2.1.105 device_client source paths. No TX, flash or compile.

## OBSERVED FACTS — source level
- CM930 _on_function16 converts FC16 to RegistersReadEventPayload and emits registers_received_event.
- On transport handshake ACCEPTED, CM930 requests identification data while WAITING_FOR_DEVICE_INFO and operation data while OPERATION.
- Before external onboarding, InfoCollector feeds register events, firmware-version discovery triggers profile loading and CM930 initializes a data-package wait set.
- The generic base client feeds sensor, alarm, configuration and operation parsers in its OPERATION branch, not the pre-onboarding information branch.
- Successful onboarding sets OPERATION, activates cloud/local subscription and parameter-map publication attempt; CM930 resets outstanding requests and requests operation data.
- Parameter-map publication can be delayed until ALL_DATA_PACKAGE_RECEIVED and depends on parser timestamp tests; OPERATION alone does not prove a complete dataset or published map.

## STRONG CONCLUSIONS
Bus reception, internal events, information collection, normal runtime parser feeding and cloud publication are distinct software layers. Connect can begin collecting controller data before cloud onboarding. This does not establish native semantic write acceptance on XTR.

## HYPOTHESES / UNKNOWNS
Independent ESPHome telemetry can likely consume passive native data without cloud enrollment. Actual XTR owner/response slot, controller application-session acceptance, cancellation, version 0.2.2 mismatch and B11D initial fault remain open.

## VALIDATION / SAFETY
16/16 static source-presence assertions PASS against uploaded device_client.zip. These checks do not prove runtime reachability. No firmware compilation, flash, TX or controller experiment. Abort on source mismatch; hardware rollback N/A.

## NEXT
V5DCM99 offline: compare original acquisition/completeness gates with historical local XTR 32/32 sequences and V5 RX-only observers. Keep packet receipt, complete dataset, application OPERATION and semantically accepted write separate. No auto-TX.