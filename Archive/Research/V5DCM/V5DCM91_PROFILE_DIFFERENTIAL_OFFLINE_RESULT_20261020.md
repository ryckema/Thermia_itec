# V5DCM91 — Offline CM930 profile differential review

Status: COMPLETE / POSITIVE (source comparison only). Historical XTR V83-FAS1 stays RX_ONLY/HARD_DENY; EXP388 remains RUNNING / PARTIAL. No compile, flash or physical transmission.

Original Connect 2.1.105 profiles compared: 1.1.1–2.1.0 contains 90 sensors, 463 configurations and 2 operations; 2.3.0–2.4.3 contains 99, 471 and 2. Newer includes 9 additional sensors and 8 configurations. Three shared sensors and three shared configurations differ; operation definitions unchanged.

Historic CRC-validated XTR measurements include register 2090=0, 1337=1, 2151=22, 2096=30 (not necessarily concurrent). Both current formulas yield 0 with these values. Newer high-pressure schema requires version >=240; older lacks that condition. This is a conditional source finding, not verified native runtime behavior. The external ATEC V3 author's hand-selected newer profile is external evidence, not proof of automatic controller compatibility.

The data cannot uniquely identify the correct generation. Next V92: offline check new-only sensor definitions versus archived captures; avoid live TX. Separate prior B11D startup discrepancy remains open; original V49 rollback available. No protected handshake or credentials reproduced.
