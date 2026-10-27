# V5DCM83 — RX-only supervisor candidate

**Status: PREPARED / NOT RUN.** Date: 2026-10-20.

From the exact V49 source archive, a receive-only observer candidate was prepared. It consolidates direction-state observation across the B11D integrity monitor and periodic watchdog, keeping the existing serial receive path and the production Home Assistant configuration. Legacy experimental runtime hardware bindings are disabled in this candidate; all output remains build-locked.

Offline validation: 77/77 YAML/source checks; 78,313/78,313 host assertions in each of three build modes; 2/2 forbidden output-build configurations correctly rejected. Original YAML identifiers preserved; one diagnostic added. Original firmware was not recompiled with ESPHome, no device was flashed, no physical TX was executed, and no actual controller result exists for V83.

Last user-confirmed V49 baseline: receive-only, output denied, manual controller communication gap 10.351s, later 285 validated receive frames in 30.532s, 63 unanswered native requests cumulatively. Existing EXP388 remains RUNNING / PARTIAL. Current electrical peer, controller version, response slot and wire EOF remain unknown. A previously incomplete response experiment caused a communications alarm; do not repeat it without a separately validated complete service and recovery plan.

The full candidate YAML, source patch, tests and checksum manifest have been supplied as a private conversation artifact rather than published in this repository. They are not verified running firmware.

**Next:** review a strictly receive-only build, preserve original settings and telemetry, and assess the resulting user-provided logs before any further live experiment. Roll back to the original verified V49 source if the eventual device test introduces errors.
