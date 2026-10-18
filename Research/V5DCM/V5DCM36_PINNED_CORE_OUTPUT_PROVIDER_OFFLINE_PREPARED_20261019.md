# V5DCM36-PINNED-CORE-OUTPUT-PROVIDER-OFFLINE-01 — PREPARED / NOT RUN

Date: 2026-10-19. **No user device action, no new firmware, no native TX.** This contract is created before implementing host-side tests.

## Hypothesis / purpose
After V5DCM35 proved a *model-only* native FC23 → mock delivery → first FC16 observation seam, the narrowest next change is **explicitly version-pinned input-Core decision inspection and a physically impossible output-provider default**. The actual privately shipped B2 ticketed Core and the current firmware repo HEAD have different APIs and materially different output-policy defaults; an unreviewed swap could change real UART behavior.

## Proven baseline and previous outcomes
- User-flashed V5DCM33-FIX-B2-LIVE-PASSIVE-01 **COMPLETE / POSITIVE** (204s, B11D/B11C parity, HA alive, 393/393 executor HARD_DENY, 0 UART writes, software DE=0), actual binary hash unknown; production and known-good rollback unchanged.
- V5DCM34 offline original Connect/V4.1/B2 functional mapping **COMPLETE / POSITIVE**; V5DCM35 offline isolated model 192/192 and B2 Core 18/18 **COMPLETE / POSITIVE**, nonflashable.
- Historical V4.1 EXP386/387 **COMPLETE / POSITIVE**; EXP388 **RUNNING / PARTIAL**; V5DCM32 real restart rejoin **COMPLETE / NEGATIVE** (B11D fault before gap); B2 qualified-age physical trial **NOT RUN**.
- Exact private FIX-B2 source ZIP SHA256 `fdc09c5927b5a351163db95db96dc467abd43cb27e1e7fc8068782bea4a677c7`; private Core Git blobs `xtr_core.hpp=63874043da0845d603b7da1ef81db403011bd063`, `.cpp=1ddb6cced68ef4571e650852913cad392e35e734`.
- Upstream `Thermia_Connect_Firmware/main` inspected 2026-10-19: `xtr_core.hpp=3d172fe134f127e9d19c5ad48d863da9a87741bc`, `.cpp=5c345d76f967103ffb58109b1e1742370e09658a`, adapter hpp `d3f1a75d551accef2576cb86c77fb2c3080c3c50`, platform hpp `95014011a004d8c3165a4619ed61cdf75aac55d3`. **Critical source-version safety difference:** current upstream `BoundaryFedAdapter` defaults `output_enabled_=true`, platform `accept` public; user-private B2 compile normally forces `output_enabled_=false`, hides bare `PlatformPort::accept` unless the host-only GAP15 macro. Source facts, not new bus measurements.

## ONE controlled change
Implement a **standalone nonflashable research-only adapter** that *pins exactly the B2 ticketed mutable Core API*, derives structural classification only from a copied (not the live) B2 Core, discards ticket/transaction payload and cannot commit the result. Provide an explicit `DENY_NO_PHYSICAL_PROVIDER` sink, with **no actual bytes, TX CRC, UART/GPIO/DE, native approval transform or 0x0708 mailbox**. Reuse V5DCM35 host mock model separately. Do not change the private source files, original on-device YAML, HA entities, live native output settings, or physical firmware repository.

## Targets / conditions / risk
Only metadata for already-validated native 0x0F events and modern XTR `03E8/count14` is observed; no target register/value/page write and **no TX payload**, transmission schedule, slot occupation or retries. Risk is a future code version silently reverting the physical output default or coupling structural `Decision.authorized` to a real send. Therefore the source pin, negative compile guard and zero-I/O invariant are mandatory. Previously accepted residual risks G01–G06 remain accepted without false claims of proof.

## Positive / negative / inconclusive criteria
- **POSITIVE OFFLINE:** strict C++17 compile and actual host assertions against extracted exact B2 Core+adapter+platform; copied-Core structural decision does not modify original Core or provide physical authority; both adapter construction forms (including `true`) remain output-disabled without host capability macro; no platform I/O events; a deliberately public bare PlatformPort accept attempt fails compilation; HEAD-like const-vs-ticket signature rejected; preserved mock state from V35 remains no-TX; source manifest/hash integrity and unchanged original ZIP verified. Report exact counts and negative controls.
- **NEGATIVE:** copying/structural decision affects original live Core, new path can commit or send, `output_enabled` accepts caller true in normal production compilation, raw PlatformPort accept is public, or source pins stale.
- **INCONCLUSIVE:** exact required B2 source not available or host toolchain/source-diff provenance inconclusive. No live device negative conclusions.

**Abort/recovery:** fail immediately if unexpected physical output symbol/path or protected code enters new artifact; discard only V5DCM36 offline changes and retain running FIX-B2. No hardware restart, sensor disconnect, ARM, flash, native approval transmission or semantic register write. No compiler output request to user.

## Required evidence and handoff
Pin byte hashes and Git blobs for all compared sources, preserve original compiler/test output and negative-compile evidence, explicitly distinguish HEAD drift from currently installed FIX-B2. If the offline criteria pass, only *then* document a future user-initiated narrowly bounded native response trial; no automatic live implementation.
