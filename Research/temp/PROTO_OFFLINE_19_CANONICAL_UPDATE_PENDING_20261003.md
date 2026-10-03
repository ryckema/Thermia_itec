# PROTO-OFFLINE-19 — canonical update pending

**Date:** 2026-10-03  
**Reason pending:** GitHub write permission was not granted in the current request.

## THERMIA_PROJECT_STATE.md — proposed addition

- **PROTO-OFFLINE-19 — COMPLETE / POSITIVE** — genuine Eco5 initial bootstrap and later `0708` mailbox refresh are separate mechanisms.
- All six successful Eco5 sessions perform the same controller-autonomous 32-page configuration export from `03E8` through `06F4` before the first `0708` poll.
- Bootstrap progression is ACK-gated: all 186 page-to-next-page transitions across six sessions follow matching ACK of the current page; missing ACKs cause same-page retry.
- `06F4/count19` is the terminal strict-bootstrap page in all six sessions.
- Later `W2/W3=FFFF/867F` mailbox refresh selects only 26 pages.
- `047E`, `0492`, `04D8`, `04F6`, `050A`, `051E` are bootstrap-only within the current Eco5 corpus and omitted from the later broad mailbox refresh.
- Six clean `FFFF/867F` windows service the selected 26 pages in exact ascending selector order.
- W2/W3 residual masks behave as remaining configuration work.
- `04A6` and `085F` are recurrent overlays and are mostly unACKed outside synchronization context.
- W4 remains a runtime/service page-family state/refresh bitmap; it is not an exclusive immediate next-page selector.
- Across 302 answered genuine `0708` responses, W0 is always zero; W1 non-zero values are only `0001` (03E8) and `0008` (042E).
- No genuine-capture proof exists for `0442` desired bit (`W1 bit4` only structural hypothesis) or `0546` desired bit (`W0 bit0` only structural hypothesis).
- W5 remains profile/session metadata: Eco5 always 0; older DCM uses 6/7.
- EXP388 remains RUNNING / PARTIAL.

## EXPERIMENT_LOG.md — proposed entry

`PROTO-OFFLINE-19 | Mailbox + sync-sequence completion | COMPLETE / POSITIVE. Six genuine Eco5 successful sessions show a fixed 32-page ACK-gated controller-autonomous bootstrap before the first 0708 poll. Later FFFF/867F mailbox refresh selects only 26 pages. Six pages (047E,0492,04D8,04F6,050A,051E) are bootstrap-only in the current Eco5 corpus. No genuine W0 activity or desired selectors for 0442/0546 were found.`

## PROTOCOL_FINDINGS.md — proposed durable findings

**PROVEN / genuine Eco5 capture structure:** successful session bootstrap uses a fixed 32-page configuration sequence `03E8..06F4`, with page advancement gated by matching FC16 ACK. The first `0708` poll begins only after that sequence.

**STRONGLY SUPPORTED:** later `0708 W2/W3=FFFF/867F` is a mailbox-driven broad refresh of a 26-page subset, not the initial bootstrap itself. Residual masks behave as remaining work.

**STRONGLY SUPPORTED / corpus-scoped:** `047E`, `0492`, `04D8`, `04F6`, `050A`, `051E` are bootstrap-only in the two genuine Eco5 captures.

**OPEN / UNKNOWN:** W0 desired high-half semantics, desired selector for `0546`, exact W4 edge/level semantics, and W5 meaning.

**NOT PROVEN:** `W1 bit4 -> 0442` and `W0 bit0 -> 0546` remain structural symmetry hypotheses only.