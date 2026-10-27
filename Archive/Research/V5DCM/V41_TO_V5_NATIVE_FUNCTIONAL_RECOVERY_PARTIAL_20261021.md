# V4.1 → V5 native functional recovery integration — 2026-10-21

**ID:** V41-V5-FUNCTIONAL-RECOVERY-01. **Status:** RUNNING / PARTIAL integration; selected source/host checks COMPLETE / POSITIVE (five GCC C++17 executables). Full ESPHome build, live XTR TX and semantic session NOT RUN.

## Baseline / independently known
Verified GitHub Write (Beta) v4.1 README/source: EXP386 COMPLETE/POSITIVE cold-start controller recovery including 32/32 native initial pages; EXP387 COMPLETE/POSITIVE delayed 0708 semantic re-arm; EXP388 RUNNING/PARTIAL repeated restarts and untested cancellation branches. Current private S65–S70 V5 source inspected: `UnifiedNative23` already has native cold10/long32 initial chain, semantic page model, 0708 mailbox, source-bound startup provider. Installed V83 RX_ONLY/HARD_DENY and V49 rollback unchanged. S62 G01/G02/G04 accepted-risk closure unchanged; B11D first fault and G05/G06 real physical recovery remain open.

## ONE integration intervention
Patch existing private `v5_native_service23_threeway.hpp` to implement `UnifiedNative23::recover_controller_loss(old_epoch,next_epoch,bootstrap)`, and matching older `v5_native_service17_engine.hpp` contract for consistency. Accept only advancing nonzero epoch, same previously bound epoch, no pending reply and no fault. Deny and latch fault if semantic state is AwaitCurrentRead or AwaitRepublish, or if a physical reply is outstanding. Otherwise discard unconfirmed semantic intents and cached controller pages via fresh cold reset; no UART, DE or TX calls. This directly models the V4.1 recoverable pre-semantic versus in-flight boundary. It does NOT implement complete EXP387 delayed 0708 runtime re-arm or attach the live ESPHome controller-loss callback; those remain next source integration work.

## Verification
Five selected GCC C++17 host executables PASS: two newly added recovery tests and existing service23 full merged, service23 negative paths, service16 semantic. Four changed/new private files vs S65–70 baseline, no production YAML modification. Full regression, ESPHome/IDF target compile, flash, XTR TX and semantic response verification NOT RUN. Private ZIP SHA256 c322d5b62461781e3e14134840ddb1b011711db4439e65f222e792673db6e696, 345 members; private protected code NOT published.

## Unknowns and next
Need wire this API only to a genuine existing XTR controller-loss callback after verified physical owner reset; do not fake evidence flags or reset in-flight TX. Then integrate EXP387 delayed 0708 semantic re-arm and full native runtime, compile with actual ESPHome/IDF and prepare individually scoped user-initiated TX. Rollback current S65–70 candidate / installed V83 untouched.