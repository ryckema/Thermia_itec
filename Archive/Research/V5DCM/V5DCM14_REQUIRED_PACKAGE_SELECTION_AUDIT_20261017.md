# V5DCM14 — CM930 source-selected package readiness — 2026-10-17

**Status:** COMPLETE / POSITIVE for verified source-level dependency chain; COMPLETE / INCONCLUSIVE for actual XTR selected mask and readiness. No live test.

**Hypothesis/baseline:** Not all 43 defined request bits are necessarily required; original Connect 2.1.105 selects bits based on active parser subscriptions. Baseline V5DCM11 readiness states, V5DCM12 43 candidates, V5DCM13 old-original mapping confirmation.

**Controlled change:** AST/string source inspection in the verified Connect 2.1.105 `device_client/cm/modbus_server15.py`, `cm/client.py`, `cm/cm_client_type.py`; no vendor execution or private handler disclosure. `_get_all_data_package_to_request` collects `significant_registers()` from available parsers; maps registers via `_register_and_bit_for_address(... request=True)`; `wait_for_all_data_package` registers pending mask and `data_package_received` advances only after a firmware receive event. The map is config-dependent, and 43-of-43 globally is NOT a proven criterion.

**Relevant fields:** 0x070A / 0x070B / 0x070C bit ranges, native FC16 configuration and operation frames, 0x0F FC23 shapes; no new bus addresses or payloads. 2.1.105 app-specific profile/subscription selection and XTR required set UNKNOWN.

**Positive:** independently grounded source call graph, achieved. **Negative/inconclusive:** cannot materialize concrete XTR selected request mask or equate historical FC16 request with application data_received. **Abort:** TX, speculative live writes or invented bit requirements. **Recovery:** none; production V5DCM2 FIX1 remains.
