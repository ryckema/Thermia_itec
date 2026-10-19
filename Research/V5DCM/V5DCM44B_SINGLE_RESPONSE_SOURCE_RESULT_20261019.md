# V5DCM44-B offline source result — 2026-10-19

**Status COMPLETE / POSITIVE — SOURCE/HOST/FAKE-IDF ONLY. First native local XTR response PREPARED / NOT RUN.**

Original V43 FIX1 ZIP SHA256 pinned to 2bda32cc2efa92678ca9f9a6f615134e430884552ecabdcec667ba57f830ba47. New source-only overlay adds V44-B Arm/Abort in HA, retained UART/GPIO21 ownership and a 30-second single-response state machine with 70ms callback-relative transfer timeout. Source candidate locally parsed; all original 117 sensors/13 binary sensors and HA production blocks retained.

**Actual offline executions:** 4 fake-IDF compile switch configurations × 8 scenarios = **32/32 pass**; prior V42 six host build variants pass; existing V43 historical genuine cross-model comparison **7/7** and synthetic comparisons **256/256**, bad-CRC negatives **32/32** rerun. These are not live controller tests.

**OPEN:** genuine current XTR request seen in logs: zero. ESPHome 2026.9.0 V44-B compile, flash, actual DE timing, controller acceptance and Online have **NOT** been run. Old V5 S3 UART writer counter is not a global signal for the new direct FIFO writer. Physical owner/slot assumptions are explicitly unproved.

**NEW SOURCE FINDING [preflight](V5DCM44B_COMPILE_PREFLIGHT_HOLD_20261019.md):** the retained 50ms B11D RX-only supervisor can flag intentional DE HIGH as a permanent fault. The older 1-second watchdog exception alone does not solve this. Do not flash the TX-enabled candidate before TX-aware supervisory accounting and review. Source-only safe compile preflight and a local Mac compiler command are prepared.

The private original response implementation/key is not part of these public docs and is not committed to GitHub.
