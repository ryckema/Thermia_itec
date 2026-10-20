# V5DCM79 — Exclusive single-owner native full-service boundary (OFFLINE)

**ID:** V5DCM79-SINGLE-OWNER-FULL-SERVICE-BOUNDARY-HOST-01  
**Date:** 2026-10-20  
**Status:** **COMPLETE / POSITIVE — source audit + host-only simulated metadata, not XTR TX**.

## Hypothesis, known-good baseline, one change

One nondeployable, payload-free session boundary can maintain the SAME logical transport/DE/B11D/watchdog owner across an initial native response *intent*, 32 exact-ordered historical controller FC16 ACK *intents*, runtime FC16 ACK *intent*, and runtime status *intent*, while denying any unverified physical context. One change: new V79 host-only metadata gate and tests; original V49 firmware/YAML, private V42/V43 backend and actual device unchanged. This is NOT an implementation of a native 0x0F response generator, frame serializer, UART or DE switch.

**Last user-verified physical baseline:** V49 RX_ONLY/HARD_DENY, TX0; manual controller restart callback gap 10.351s, 285 CRC/byte matched post-gap frames over 30.532s, 63 cumulative unanswered native FC23 challenges. Actual hardware owner, wire EOF, electrical slot, controller 0867 version and exact flashed binary hash UNKNOWN; EXP388 remains **RUNNING / PARTIAL**.

**Relevant past:** EXP255 (unanswered), EXP256 (single historical native response then settings page, incomplete follow-on caused COMM ERR), EXP257/258 (first ordered ACK transitions), EXP355/386 (historical 32/32 native ACK+runtime in earlier sessions); V74 source dual-owner/callback blocks; V75 dry 35-intent model; V76 transport dry tickets; V77 original V45 monitor host guard; V78 actual private backend and original V42 behind nonphysical FakePort. No past live test repeated.

## Actually verified source

- Original user V49 private ZIP SHA256 `62afe39629102a3daa06f09eab3ed159f44437d702fb8d3904c61e62e2a85630`, 69 members: **15/15 source audit checks PASS**.
- Original V42 `OneShot` terminates at `Complete` and cannot be restarted as full service; original default kBuildMaySend remains false.
- Original V43 and V44B each borrow the same ESPHome UART/DE switch, while actual V49 B11D owner exception and 1s watchdog both refer ONLY to V44B. No exclusive physical driver yet.
- V49 native actors see `parsed.front()` only when callback contains exactly one finished frame. Multi-frame host batching needs proper per-event routing.
- Existing passive R6P30D 32-page ledger gives ordered starts and observed geometry variants, but **does not generate native FC16 ACKs**. The historic controller 32 page chain is NOT the genuine Thermia Connect 2.1.105 APP 33 significant-page profile.

## Tests and output boundary

- **2,729/2,729** ordinary strict C++17 host assertions PASS.
- **2,729/2,729** ASan/UBSan assertions PASS.
- **2,729/2,729** no-exceptions/no-RTTI assertions PASS.
- **4/4 compile-denial checks PASS**: ESP_PLATFORM, ARDUINO and each V42 native TX macro.
- Positive host mock: 35 independently injected *mock confirmations*, both sequential and callback-batched, one owner token throughout. Negative host scenarios: 14 missing prerequisites, 12 fault/DE/owner/watchdog cases, 32 wrong-order pages, 32 geometry mismatches, 33 premature-runtime cases, plus abort and no-output assertions. This model has NO Port, UART, GPIO or native bytes; actual hardware output is impossible.
- The original private V42/V43 backend was **not executed in V79** (it WAS genuinely executed offline in V78). Artificial all-true metadata are not current controller measurements. No new ESPHome compile, flash, reset, physical response, register change or cloud session.

**PROVEN (SOURCE/HOST):** V49 lacks a unified native session writer and currently splits UART/DE ownership; a payload-free single-owner host gate can enforce source-derived stage and safety invariants.  
**STRONGLY SUPPORTED:** future physical implementation needs one actual UART/DE actor recognized by B11D+watchdog; every CRC-complete callback ADU dispatched; current-request-dependent private first reply; a *new* complete 32 FC16 ACK plus runtime service; source-verified per-session geometry; independently verified electrical bus peer/EOF/slot.  
**OPEN:** measured physical admission, current controller acceptance, real GPIO/DE timing, UART drain, original Connect APP33/C2, Online/cloud.

## Safety, criteria and next

Positive: source audit and host tests pass, all unverified contexts veto, no confidential implementation or native TX output. Negative: a forbidden build succeeds, stage advances despite failed evidence or any real output is possible. Physical/session claims remain **UNKNOWN**, not negative. Abort: discard host-only artifact if hash/source/tests fail. Device rollback: N/A; V49 unchanged RX_ONLY/HARD_DENY. **No target payload or current register value applies to this nonphysical host test**.

**NEXT V5DCM80 (not run):** source-level migration plan for one real ESPHome UART/DE authority, callback fan-out, original B11D+1s watchdog integration, full service boundary, and independently measured physical slot/peer/EOF. Do NOT enable original TX flags or run standalone EXP256-style one-reply TX; that earlier test caused COMM ERR. Any future live test requires its own exact targets, bounded timing, abort and rollback.

**Local nonsecret reproducible package (not on public GitHub):** `V5DCM79_SINGLE_OWNER_FULL_SERVICE_BOUNDARY_HOST_ONLY.zip`, SHA256 `1c8e2e2c013f8c527c7e7a79717b8c4ef9bf5d466598fd7ad149b89ef0dfd617`. Contains source audit script, 15/15 results, original nonsecret V45 ownership decision header, host-only metadata gate, tests, README, report and manifest. No private native response code.