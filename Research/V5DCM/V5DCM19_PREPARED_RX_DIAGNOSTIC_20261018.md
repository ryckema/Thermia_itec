# V5DCM19 — RX-only integration candidate, PREPARED / NOT RUN (2026-10-18)

**Experiment hypothesis:** reuse the already present V5DCM1 CM930 shadow observer and V5DCM2 challenge statistics to expose a joined `[V5DCM19]` diagnostic view, while preserving existing production HA and bridge behavior.

**Baseline:** user-supplied archived `V5DCM2_CM930_CHALLENGE_INTEGRATION_RX_ONLY_PREPARED_20261017(2).zip` includes 4,187-line YAML and local portable bridge. The user has separately reported live installed V5DCM2 FIX1 RX-only TX HARD_DENY. **Byte equivalence of that deployed FIX1 and archived prepared YAML is NOT proven**, so this is not yet cleared for flash.

**Controlled change:** only existing 30-second logging interval text and header commentary. Replace two `[V5DCM2]` log lines with three `[V5DCM19]` logs: native shape/shadow/config, mailbox/runtime service shapes, and explicit UNKNOWN owner/epoch/slot/native acceptance/icon/profile. No new native response, second UART consumer, protocol parser, active response code, or Home Assistant entity.

**Offline validation actually run:** 8/8 source/syntax checks passed on resulting YAML/package: parsed YAML syntax with `!secret` placeholder; production configuration after `globals:` byte-identical; existing frame callback symbols present; RX-only HARD_DENY maintained; exactly three new diagnostic prefixes; old diagnostic prefixes removed; secrets kept as `!secret`; unchanged native UART write call count. **NOT an ESPHome compile**, resolved ID/substitution validation or hardware regression. Full package locally created `V5DCM19_RX_ONLY_PREPARED_20261018.zip` with all original include/component files, candidate YAML, diff, validation JSON, installation/result instructions.

**Positive criterion:** after baseline equality review, live RX-only startup/logs and HA production sensor health, no TX attempt; correct labelling of shadow versus native proof. **Negative:** existing HA sensor regression, no logging, parser faults, or false claims of native accept; **abort:** unexpected native TX, new bus-health fault or loss of required production functionality; **recovery:** restore actual known-good deployed V5DCM2 FIX1 (not automatically the archived candidate).

**Status:** PREPARED / NOT RUN. No live test/flash supplied. G01–G06 already accepted, not reopened. This preparation does not close remaining V5DCM18 original reference-Core test nor authorize proceeding automatically to V5DCM20.
