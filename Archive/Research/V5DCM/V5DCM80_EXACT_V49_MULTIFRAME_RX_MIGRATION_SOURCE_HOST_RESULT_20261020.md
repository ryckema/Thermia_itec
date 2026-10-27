# V5DCM80 — Exact original V49 parser + read-only all-frame routing migration preflight

**Experiment:** V5DCM80-EXACT-V49-STREAM-PARSER-MULTIFRAME-RX-MIGRATION-HOST-01  
**Date:** 2026-10-20  
**Status:** COMPLETE / POSITIVE — offline source/host parser and RX routing only. No real native TX/session.  

## Hypothesis, baseline and one controlled change

**Hypothesis:** V49 has an integration asymmetry: existing V5 frame observers receive every CRC-complete ADU from the original parser, while the V43/V44B native actors receive `parsed.front()` only when a UART callback yields exactly ONE finished frame and no trailing parser pending data. A new RX-only host adapter, without UART/Port/DE or native response logic, should be able to fan out all original completed frames in order and reject altered original DE/B11D/P5 provenance.

**Last user-verified known-good physical baseline:** V49 installed RX_ONLY/HARD_DENY, physical TX0; user's manual controller restart was associated with 10.351s callback gap and 285 byte/CRC matched post-gap frames in 30.532s. 63 cumulative unanswered native FC23 challenges over noncontinuous logs. Controller current version `0x0867`, physical wire EOF, electrical peer, exclusive response slot and flashed exact binary checksum UNKNOWN. EXP388 remains RUNNING / PARTIAL. No new physical results.

**Prior relevant local evidence:** EXP255 unanswered; EXP256 one historical native first response progressed to settings page 0x03E8 but incomplete follow-on caused real COMM ERR; EXP257/258 early ACK progression, EXP355/386 older full 32/32 native initial page ACK + runtime. V74–79 offline source, FakePort and host-only milestones, with V78 private backend executed offline. Nothing live repeated.

**ONE V80 offline change:** mechanically extract the unmodified generic `ThermiaV5InlineCore::StreamParser` excerpt from the exact original V49 YAML for host compilation; connect a NEW nondeployable RX-only generic `ReadOnlyFanout` to each completed frame. This changes **no original YAML, original parser body, backend, firmware, RS485/UART or DE output**. Full native TX service is a separate future engineering effort, not implemented here.

## Verified exact provenance and results

- Original uploaded 69-member V49 archive SHA256 `62afe39629102a3daa06f09eab3ed159f44437d702fb8d3904c61e62e2a85630`; **20/20 code/source assertions PASS** across V42/V43/V44B/V45/YAML. Generic extracted original V49 parser excerpt SHA256 `3c0a4a33a7bd5afe88a72651a22487887e48dd19aa920d4c27fceb7bafcf8db5`.
- Existing October 3 XTR bus capture `thermia_capture_20261003_165355.log` contains **2,687 input lines** replayed as source ADUs. Under (a) one ADU at a time, (b) two fragments per ADU and (c) synthetic coalesced six-ADU batches, the same unchanged V49 parser released **2,687/2,687 CRC-complete frames in each mode**. Counts, not any TX ability, are verified.
- Synthetic six-frame coalescing produced **448 multi-frame callback batches**. Current original V49 V43/V44B `if(parsed.size()==1u && !c.parser.has_pending())` gate would skip those batches *if* real callbacks were coalesced that way. **This does NOT establish that 448 such batches actually occurred on the ESP32.**
- New host-only RX router delivers all CRC-complete frames sequentially even if another trailing partial remains pending; trailing pending is diagnosed separately and never promoted into physical EOF/TX evidence.
- **8,696/8,696 assertions PASS in each** of three builds: g++ C++17 strict, `-fno-exceptions -fno-rtti` and ASan+UBSan. Fault/owner/DE/B11D/P5/legacy activity/new callback gap and duplicate-owner denials pass; 4/4 compile denials for ESP_PLATFORM, ARDUINO, original private TX build switches.
- **0 physical UART transmissions; 0 DE writes** because host-only code has no Port/UART/GPIO/output interface. Original protected dynamic native reply backend not invoked or included in this V80 host package. No ESPHome compilation, no flash, no controller restart, no register write or real native acceptance.

## Source migration map and evidence separation

1. V49 boot currently binds **two** native runtimes, V43 and V44B, to the SAME ESPHome UART and DE switch. New actual native design must consolidate this under one physical output authority; there must never be two concurrent DE owners.
2. In existing V49 `uart.debug`, preserve exact single raw ingress, parser, B11C/B11D/R6-P5/FIX2 sticky faults, bus health bookkeeping, HA entities, prior P1/R3 history. The per-ADU `for(const auto& f:parsed)` observer loop already exists. Source migration should leverage this, not add a second UART reader or blindly lift old legacy aborts.
3. V45 B11D supervisor currently recognizes only `v5dcm44b::runtime().b11d_tx_window_owned(...)`; the **independent 1s DE watchdog** recognizes only `v5dcm44b::runtime().defer_periodic_rx_watchdog()`. Any eventual one-owner physical driver must supply both consistent scoped decisions and preserve independent switch-state vs GPIO21 comparison.
4. V42 original `OneShot` is terminal after one response; V49 has no complete native FC16 ACK/runtime writer. Later work needs a protected, current-request-dependent initial response followed by **32 historically locally confirmed native controller FC16 ACK stages and runtime 085F FC16 / FC03 0708 service**. Do NOT equate that with Thermia Connect 2.1.105 app **33 significant group** receipt/C2/Online.
5. V44B's `one_shot_timing_risk_explicitly_accepted` and 70ms software budget, and the callback-entry timestamp, are **not independent electrical EOF/slot/peer measurements**. Do not unlock V49 TX macros or send an incomplete EXP256-style first response.
6. Prior installed V49 old sticky B11D fault, post-gap RX cohort and physical owner/slot need separate treatment. Host assertions with synthetic healthy flags do not validate the real current bus.

**PROVEN (EXACT SOURCE + HOST):** complete ADU routing asymmetry; original parser behavior consistent across replay chunking; non-transmitting observer can route every complete frame in synthetic batches without assuming physical ownership; fail-closed host safety policy.  
**STRONGLY SUPPORTED:** next private implementation must integrate one UART/DE authority shared across B11D and watchdog and full native follow-on service.  
**OPEN/UNKNOWN:** actual ESPHome callback batching frequency, on-device CPU/heap, physical electrical wire EOF/owner/slot, current XTR 0x0867, native response acceptance, vendor APP33/C2/Online/cloud. 

**Positive criteria:** 20 code checks + host parser/fan-out replay + sanitizer/no-exceptions + expected forbidden builds, zero actual output. **Negative:** source pin mismatch, lost/duplicated complete ADU, unsafe owner/DE/frame routing accepted, hidden output. **Inconclusive for live controller behavior** (not tested). Offline abort: discard candidate on test/source mismatch, hardware rollback N/A. **No target register/current value/payload applies to a no-TX host test.**

## Files and next action

**Non-secret local research package:** `V5DCM80_RX_ONLY_SOURCE_PARSER_FANOUT_HOST.zip`, SHA256 `882e125f3598ef4c2800b1b7e59afcc586b49b57d316b54c3031a89900b8366f`; 10 files: generic parser excerpt, RX-only fan-out + tests, source audit, code migration map, README, result and checksums. No private native reply or `0x0708` implementation, no captured traffic distributed.

**NEXT V81 (not prepared or run):** an offline exact-source single physical UART/DE owner/B11D/watchdog interface migration, privately covering complete native follow-on service. Independently measure the real electrical response window before any separately user-initiated bounded active test. Installed V49 and EXP388 remain unchanged.