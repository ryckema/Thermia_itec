# V5DCM37 — independent recovered archive and continuity verification (2026-10-19)

**Status: COMPLETE / POSITIVE (NEW OFFLINE RECONSTRUCTION AND HOST REPRODUCTION ONLY).** This is not a new physical protocol experiment and does **not** supersede the existing [original V5DCM37 COMPLETE / POSITIVE historical result](V5DCM37_COMBINED_DCM_OFFLINE_RESULT_20261019.md). The user observed an apparent stall. GitHub's `EXPERIMENT_LOG.md` and `PROTOCOL_FINDINGS.md` already recorded the previous V37 positive result with **1017/1017** host checks, but `THERMIA_PROJECT_STATE.md` had incorrectly still led with V5DCM36. A separate state header correction was committed `5dc8bd306709ce21bfa1f157ea68fdafd37abb0f`.

## Provenance and controlled change

The **previously reported original V37 ZIP** `V5DCM37_COMBINED_DCM_OFFLINE_NOT_FLASHABLE.zip` (previous report SHA256 `f656c09082f6077b84db216570666a96a097ad85e676a9d693efee2e47f8974f`) was **not found** in this runtime and has not been byte-for-byte rechecked or reconstructed. No claim is made that its 1017-case executable is available here.

**One offline change:** built a *different* strictly no-TX, nonflashable V37 combined evidence coordinator, importing only the verified original V5DCM22 profile descriptor/header and existing private **V5DCM35 + V5DCM36 host tests**. It never modifies, contains, recompiles as firmware or flashes the user production YAML. User source input is unchanged `V5DCM33_FIX_B2_QUALIFIED_EVIDENCE_HOLD_OFFLINE_NOT_FLASHED.zip`, SHA256 `fdc09c5927b5a351163db95db96dc467abd43cb27e1e7fc8068782bea4a677c7`. Original B2 YAML SHA256 `32e1b7c3ea4f7411fb94d6d769370b9ae10874403961403002250b96e4365d46`, exact portable Core Git blob pins and normal output-disabled state checked.

**New artifact:** `V5DCM37_REPRODUCED_OFFLINE_NOT_FLASHABLE.zip`; **SHA256 `f94b6cccf9982df79b3eecf21693f1a4e1b82a9e6429c82effa5987dc6eafc19`**, **19 members**, **31,441 bytes**. ZIP CRC and **all 18 member SHA256** checks succeeded against own embedded manifest. The archive does **not** include B2 firmware ZIP, private 0x0F response algorithms, secrets, raw reply bytes or historic raw logs. Private bundle supplied to user as a verified file attachment, **not uploaded to public GitHub**.

## Five tested lines (independent model evidence, not native controller proof)

- **A:** canonical FC23 observation metadata → one *synthetic* delivery event → modern native `03E8/count14` FC16 yields only `InternalFreshShadow`; neither real response delivery nor accepted controller handshake is inferred.
- **B:** fresh, retained and recovery tracked separately; `085F/count5` alone yields only retained/recovery candidate and never internal fresh acceptance or real owner/slot.
- **C:** original B11D/P5 current health flags and source/boot/generation/sequence/monotonic synthetic clock, competing responder, expired scope, duplicate approval and ticket mismatches all tested as fail-closed. Test-model generation is **not** physical controller epoch.
- **D:** `v5dcm22::kProfile` directly sourced from exact FIX-B2 original: **33 selected group shapes** (15 W2, 10 W3, 8 W4), matching both address AND count; missing one of 33, duplicates, wrong lengths (including legacy XTR `03E8/count13` and `0410/count21`) are not full matching modern census. **33/33 historical shapes is not Connect C2**.
- **E:** actual pinned B2 mutable/ticketed Core remains inspected only on a copy, no ticket passed into native output provider; disabled provider always denies and new model exposes no UART, DE, response transform, CRC writer or network access.

## Executed verification and honest chronology

- Initial new source compile hit a `-Werror=misleading-indentation` formatting error; corrected before a passing binary was counted.
- One real host lifecycle mismatch surfaced: the newly coded terminal historical shadow would expire in `tick()`; repaired to preserve a frozen shadow, *without* interpreting it as current live integrity.
- The first wider combined runner exceeded a tool runtime limit while compiling the same unchanged five B2 sources repeatedly. That interrupted run was **NOT** called complete. A later runner compiled shared B2 objects only once; full run returned **exit 0**.
- **11,507 / 11,507 NEW source/host C++17 assertions PASS** from the rebuilt coordinator; **these are NOT the earlier original V37 1,017 cases and are not presented as that earlier suite**.
- Reused exact V5DCM35 **192 + 18** PASS; V5DCM36 original private B2 Core/adapter/platform **53** PASS; 3 forbidden compiler probes correctly rejected; 1 deliberately tampered original FIX-B2 archive rejected.
- Reran unchanged B2 **65**, original XTR 70/70 CRC-good frames with cohort frozen after 61, FIX-A **52**, portable stream **32**, V5DCM31 **61**, V5DCM32 original FC23 fixture **34** — all PASS.
- Rechecked four old raw logs with independent Modbus CRC metadata: XTR Oct03 **2687/2687**, XTR Sep25 **892/892**, Eco5 Sep26 **10719/10719**, Eco5 Sep28 **9174/9174** = **23472 good, zero bad**. Oct03 local XTR first `03E8/count13` is LEGACY and not modern count14; Eco5 is cross-model.
- The final new archive was extracted into **a separate fresh temporary directory**, rerun using only the archived files plus existing original B2 ZIP/log inputs, and the complete runner again returned **exit 0**. No hidden old worktree required.

## Results and remaining gaps

**COMPLETE / POSITIVE OFFLINE reconstruction only:** combined model guards and archived runner reproduce a bounded no-TX internal proof model with independent A–E checks. The original V37 report's existing 1017 count is preserved as historical project evidence but its exact ZIP remains absent from current session.

**OPEN / UNKNOWN:** electrical DE voltage, physical bus owner/slot/epoch, genuine native dynamic challenge response/actual physical delivery and controller FC16 response, retained/hot real behavior, full real Connect 33/33 application parameter C2, Online/cloud icon, original seven-fixture Python reference Core end-to-end replay and live B2 post-gap >90 second qualified-history retention. Earlier V4.1 EXP386/387 local positives, EXP388 partial and V5DCM32 negative integrity-latched restart are unchanged.

**Actual device:** still user-confirmed V5DCM33-FIX-B2 last live 204s passive **COMPLETE / POSITIVE**; original B11C/B11D stable and software physical TX attempts 0 / UART calls 0. NO new flash, ARM, controller restart, native TX or register write performed.

**Next:** design a separately scoped real native response delivery test only after exact private response payload/CRC, current unit state, response slot/owner evidence, bounded single controlled change, abort criteria and rollback are specified and user initiates live execution. Do not push confidential emulation or 0x0708 tooling to public GitHub.
