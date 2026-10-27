# V5-NATIVE-SERVICE-12 — private offline partial service router (2026-10-20)

**Status: PREPARED / NOT RUN** (host tests only; no XTR execution).

Baseline: verified V83 FAS1 RX-only, TX=HARD_DENY; EXP388 RUNNING / PARTIAL; B11D first-start anomaly OPEN.

## Observed offline facts
- Uploaded private V5_NATIVE_TX_V41_INITIAL_HANDLER_OFFLINE_20261020(1).zip SHA-256 0428a5a31dcab66730ba3acbe13ec92cf6ccb97e377870166779c4683fef0898 matches canonical service-11 artifact.
- Inspected initial handler, native service contract and FC16/FC03 cache service.
- Existing host tests PASS: test_v41_initial_handler.cpp, test_real_fc_services.cpp, test_native_service_contract.cpp, test_v41_page_cohorts.cpp, test_guarded_port.cpp.
- New private, source-only partial router composes V41InitialHandler and existing FcServiceContext with CRC, epoch and exact-response-slot checks. It rejects unsupported Startup, SemanticWrite and RuntimeRefresh; no readiness or TX grant. New host test PASS: test_service12_partial_router.cpp.
- Standalone private seven-file offline addon generated: V5_NATIVE_SERVICE12_PARTIAL_OFFLINE_20261020.zip, SHA-256 21d5f76b03b2241aa6a7b312432ba03035de5592ceabd832a8524d5b81cfa238. This addon is **not** flashable, not production service, and must remain private.

## Conclusions and remaining blockers
This is an OFFLINE ENGINEERING STEP, not an XTR protocol result. Startup, full native session, 0x0708 application-specific mailbox, runtime refresh, semantic write, V5 UART/DE single owner and B11D integration are NOT implemented in the new partial router. Current compiled tests do not represent ESPHome compilation or hardware effects. Exact source callbacks cannot be marked completed from a partial router; NativeServiceGate still correctly requires six real services. Controller-confirmed progress/readback remains necessary. No ATEC protected authentication or challenge-response code was generated/copied.

## Next action
Implement full source-grounded startup plus V4.1 real runtime/0708/refresh/semantic callback services under single owner and verify on host with injected controller request progression. Only prepare scoped physical test after slot, peer and B11D gates are qualified. Keep HARD_DENY and known-good YAML unchanged.
