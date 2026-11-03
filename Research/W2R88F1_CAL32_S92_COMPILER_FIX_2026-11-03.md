# W2R88F1 — target C++ build fix for S92 calendar guard

**W2R88 TARGET COMPILE: COMPLETE / NEGATIVE. W2R88F1 SOURCE / OFFLINE TESTED: PREPARED / NOT RUN.**

## OBSERVED FACTS
Actual user ESPHome 2026.9.0 ESP32-S3 ESP-IDF 5.5.5 build reached C++ main.cpp.obj and failed at YAML line 14277: `expected ':' before ')' token`, `expected primary-expression before ')' token`, expression ending `cal32_page_send_guard) :`. No W2R88 successful target firmware or new F2/F3/F4 physical TX was demonstrated. Latest FLASHED / LIVE / LOCALLY VERIFIED baseline remains W2R86 on XTR M 3N controller 2.4.2 for F1 P4/P5 genuine 5-field controller FC16 and fresh F1 persistence.

## ROOT CAUSE AND ONE FIX
W2R88 appended the F2/F3/F4 new-domain `cal32_page_send_guard` to the existing F1 authorized predicate in the main S92 desired-page sender but closed the ternary branch before its OR term. Repair adds one opening parenthesis before the old F1 predicate so the exact expression is `((existing_F1_predicate) || cal32_page_send_guard)`, still under all the original common TX/CRC/session/DE guards. This is a grouping-only source fix; W2R88F1 additionally updates the build string from MAIN04-W2R88 to MAIN04-W2R88F1. No other source changes. New-domain physical TX remains explicitly user-initiated/ARM guarded and unvalidated until genuine controller FC16+fresh CAL12 after user flash.

## OFFLINE TESTS
1) G++ C++17 with -Wall -Wextra -Werror -fsyntax-only on the whole formerly faulty editor42 ternary/S92 send gate: PASS. 2) Existing 38 new/modified W2R88 callback and owner/receipt snippets C++17 syntax-only: PASS. 3) Strict duplicate-key YAML parse, all 1230 unique IDs and 32 shared calendar options: PASS. 4) No unsupported switch.template update_interval: PASS. 5) exact two-line diff W2R88→W2R88F1; private ZIP archive CRC, per-entry SHA256 and byte-exact W2R86 verified rollback: PASS. NOT actual ESPHome target compiled or flashed.

**One complete private deliverable:** `Thermia_MAIN04_W2R88F1_CAL32_COMPILE_FIX_PRIVATE.zip` with one complete ESPHome YAML, W2R86 rollback, concise Dutch build/flash/ABORT/test plan, minimal patch, SHA256 manifest. Original GitHub README.md and Write (Beta)/iTec Eco untouched.

## Bounded next step
User compiles/installs W2R88F1 and checks build label, M6=5, CURRENT4/4, CRC_DIFF=0, 32-slot HA UI and source snapshot. Then, only if user explicitly activates first new-domain experiment, select existing Silent Mode P1, fresh-controller read (historically daily 22:00–23:59), stage start-minute 00→01, press ARM45s + one Apply. Require real FC16 exact word and newly owned CAL12; ABORT if anomalous, do not blind retry. New-domain physical semantic proof remains OPEN.

**CURRENT MILESTONE:** unified 32-slot weekly editor with first F3 source-verified write pathway. **DELIVERABLE:** W2R88F1 full firmware ZIP, SOURCE / OFFLINE TESTED. **REAL BLOCKER:** none established in corrected C++ expression; true target compile and F3 controller acceptance OPEN. **ONE NEXT ACTION:** user runs ESPHome target build of W2R88F1.