# W2R87F1 — ESPHome template switch config correction

**Status:** W2R87 config validation COMPLETE / NEGATIVE; W2R87F1 SOURCE / OFFLINE TESTED, PREPARED / NOT RUN.

## OBSERVED FACTS
User's ESPHome 2026.9 validator rejected W2R87: `[update_interval] is an invalid option for [switch.template]. Did you mean [internal]?`. W2R87 introduced seven weekday `switch.template` controls for F3 Silent Mode and gave each `update_interval: 5s`. These options are invalid for this platform; valid sensor/text_sensor intervals elsewhere are unaffected.

## ONE FIX
Derived from the exact prepared W2R87 complete YAML, W2R87F1 removes *only those seven invalid `update_interval: 5s` lines* and updates the build-label to `Thermia MAIN04-W2R87F1`. Existing seven weekday state lambdas and on/off `publish_state` callbacks are unchanged. W2R86-proven F1 editor/Apply and sole S92 UART/RX/TX/DE, FC03, FC16 and readback unchanged. New F3 physical parameter writes remain disabled; F3 staging/Discard/NO_TX plan and F1 stale auto-reread unchanged.

## OFFLINE VALIDATION
Whole YAML PyYAML parse with secret stub PASS, exactly 1182 unique component IDs; AST comparison vs W2R87 proves only seven switch-template options removed plus build diagnostic string; all other components unchanged. Existing 31 new F3 C++ callback GCC C++17 syntax-only harness PASS, marker count for native sender/CRC/FC16 routines unchanged, ZIP CRC and file SHA256 PASS. *Not ESPHome target compiled, flashed or live tested.* Deliverable: single private ZIP `Thermia_MAIN04_W2R87F1_F3_EDITOR_AUTO_REFRESH_PRIVATE.zip` containing complete YAML, exact W2R86 locally verified rollback, README, minimal diff, SHA manifest. W2R87 source candidate superseded, not live-verified.

**CURRENT MILESTONE:** F3 silent source editor + automatic selected F1 stale re-read.
**DELIVERABLE:** W2R87F1 corrected full firmware ZIP.
**REAL BLOCKER:** none for this config error; F3 physical semantic TX outside W2R87F1 scope.
**ONE NEXT ACTION:** user validates/compiles/flashes W2R87F1 and checks F3 source/stage/discard NO_TX plus F1 stale auto-refresh.
