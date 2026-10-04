# Canonical update pending — PROTO-OFFLINE-65..68

## PROTO-OFFLINE-65 — COMPLETE / NEGATIVE
- 25,031 genuine CRC-valid Online/DCM frames scanned with exact v4.1 candidate rules.
- 0 double-valid candidate frames.
- 0 genuine semantic desired-page prefix collisions.
- PROTO63 remains synthetic/defensive with respect to the current genuine corpus.

## PROTO-OFFLINE-66 — COMPLETE / POSITIVE WITH REFINEMENT
- all four candidate parser policies reconstruct the genuine corpus exactly because no genuine ambiguity exists.
- simple shortest/longest/failclosed sort-order changes are insufficient under arbitrary chunking when the 8-byte semantic prefix arrives before the longer response tail.
- robust fix requires deferral/frame-gap/context, not merely candidate ordering.

## PROTO-OFFLINE-67 — COMPLETE / POSITIVE
- 50,000 parser+semantic adversarial cases.
- current shortest-prefix parser can cross the setting-bearing TX boundary in synthetic owner-matching split-prefix cases.
- frame-gap finalization produces 0 tested ambiguous-prefix setting TX decisions while preserving 140/140 randomized genuine replay runs and 4/4 legitimate semantic request positive controls.
- no live/genuine occurrence is claimed.

## PROTO-OFFLINE-68 — COMPLETE / POSITIVE
- clean schema/table-driven host core compared against current source-transcribed v4.1 logic.
- 13358496 protocol decision comparisons, 0 differences.
- bootstrap 32/32 and CRCs valid; PROTO54 and PROTO60 gates PASS.
- parser and ACK hardening deliberately excluded from structural equivalence.

Live status unchanged. No YAML change.
