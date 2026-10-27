# V5DCM83-FAS1 — First Alignment Snapshot, source candidate

**ID:** V5DCM83-FAS1-B11D-FIRST-ALIGNMENT-SNAPSHOT-01  
**Date:** 2026-10-20  
**Status: PREPARED / NOT RUN.** The offline development checks passed. No new firmware was compiled with ESPHome, installed, or observed on the actual ESP32 for FAS1.

## Scope and existing physical baseline

User asked for the B11D First Alignment Snapshot following the previous exact-source audit. That audit showed B11D can arm after a 25ms UART *callback* gap while the original V5 parser may have a different receive-history alignment. The actual cause of the one live V83 startup count difference is still **OPEN**; the synthetic reproduction did not match the retained real first-fault pending flag.

**Last confirmed installed device:** V83 RX-only shared supervisor, status **RUNNING / PARTIAL**. User supplied 94s of successful passive telemetry, new shared owner unsafe=0, GPIO direction LOW, 0 software TX attempts, stable later parser resync but an earlier independent B11D count mismatch. The controller was **not restarted** when the ESP32 was flashed. The earlier V49 source remains the verified rollback basis and its original sticky fault history is preserved. EXP388 is also RUNNING / PARTIAL. No new native session acceptance, physical response slot or owner was proven.

## Hypothesis and one additive offline change

**Hypothesis:** A read-only first-event record can preserve the missing B11D arming and first comparison metadata until Home Assistant connects, while leaving original fault/latch, RX parser and output-denial behavior untouched.

**Controlled source change:** add one non-transmitting first-alignment C++ header to the *exact user-supplied V83 source*, insert eight anchored metadata-only observation points, and add one HA **diagnostic text sensor** named `B11D First Alignment Snapshot`. It records:
- First callback gap and byte count at B11D arming, original V5 pending/resync/drop state before its parser feed, then the same callback's after-feed state and completed-frame count.
- First RAW/V5 independent frame-count comparison: both counts, batch index and size, idle callback gap, V5 pending/resync/drops, and whether counts agree.
- If a decoder or bounded FIFO fault occurs before comparison, latch the first corresponding metadata instead.
- Only counts and states, **never captured frame bytes, peer IDs, native reply material or confidential firmware logic**. The original independent fault decision continues to act exactly as before.

This snapshot does **not** prove true electrical idle, same physical peer, controller generation, native ownership or firmware profile. It neither clears original faults nor enables output.

## Offline validation

- Exact previously delivered V83 ZIP and its full YAML compared byte-for-byte to the supplied working source. Source provenance stored privately in the delivered package.
- **37/37** Python/YAML/source integrity checks passed (unchanged other top-level blocks, all original IDs and entities retained, one diagnostic added, original frame-count decision and sticky latch unmodified).
- **200,036/200,036** C++17 host assertions passed in **each** of strict, ASan+UBSan and noexceptions/noRTTI builds.
- **2/2** forbidden native output build configurations correctly rejected.
- A complete private conversation-only 12-file deliverable was assembled: full candidate YAML, exact diff, passive header, build and validation scripts, tests, source/validation records and SHA256 manifest. ZIP SHA256 `43aaa5f1a3a43a6f353b5b2c2d9d88d08dfd249c82a13c35f9c55eaf117f9940`. Candidate YAML SHA256 `2c01c04641d62a753fd79d3445c1527e1016a922c8aa6b86632fbc3691dcbe5c`.
- **Not performed:** embedded ESPHome compile, OTA/USB flash, user-run FAS1 observation, electrical UART/DE measurement, controller restart or register write. The host assertions are NOT local-controller proof.

## Future controlled test criteria and abort/recovery

If separately flashed by the user in receive-only mode, **positive** would mean unchanged existing heating telemetry and bus-health measurements, one stored initial arming/first-compare snapshot, original B11D error latches preserved, direction LOW, software TX attempts zero and no new reception faults. A count difference is evidence for which receive windows diverged, not permission to suppress the fault.

**Negative:** lost HA entities, new output, unsafe direction, changed original fail-closed error behavior, regression in CRC/buffer handling or actual controller COMM ERR. **Inconclusive:** no B11D arming or first compare captured, incomplete logs, missing or conflicting source identity.

**Abort and recovery:** no hardware recovery required for preparation. If later compiled/flashed and device behavior regresses, cease further tests and restore the last working receive-only V83 or verified earlier V49. No controller reboot or active send is required. Before any later firmware run, validate source includes from user's private existing archive and keep the original output build locked.

**NEXT:** one user-initiated RX-only ESP compilation/observation if desired, then review the new HA sensor, original B11D first fault, parser status and output health. Do not advance to a new active experiment or claim V83 complete until first-fault provenance and the current RX behavior are evaluated. Never publish the user's private native response source in GitHub.