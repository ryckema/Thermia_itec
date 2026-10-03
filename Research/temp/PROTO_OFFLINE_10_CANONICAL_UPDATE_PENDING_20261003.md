# Pending canonical reconciliation — PROTO-OFFLINE-10

**Date:** 2026-10-03  
**GitHub:** not modified  
**Track:** PROTO-OFFLINE-10 — COMPLETE / POSITIVE  
**Scope:** offline only; no live experiment state changed.

## THERMIA_PROJECT_STATE.md — proposed additions

- Add `PROTO-OFFLINE-10 — COMPLETE / POSITIVE`.
- Desired-state command architecture is now reduced beyond the PROTO-OFFLINE-09 page-bit dispatcher:
  - DCM signals desired page via `0708 W1`;
  - controller FC03-pulls the complete desired page;
  - DCM returns a coherent full page image;
  - in every fully bracketed Eco5 command, exactly one word differs from the last controller-published image;
  - controller FC16-publishes an image exactly equal to the DCM desired image ~0.49–0.57 s later.
- `03E8` Eco5 commands:
  - `03F4 20 -> 30`, exact full-page confirmation;
  - later `03F4 30 -> 20`, exact full-page confirmation;
  - room/controller `B3C5` independently follows `20 -> 30 -> 20`.
- `042E` group Eco5 commands:
  - `042F 1 -> 0`, exact full-page confirmation;
  - later `042E 1 -> 0`, exact full-page confirmation.
- Public mapping labels `042E` as Integral A1; `042F` remains unknown.
- Older genuine DCM `03E8/count13` desired images differ only at `03E8` (`0x17 -> 0x16`), independently supporting the one-target/full-page model.
- Desired-page count is profile/topology dependent (`03E8/count13` older DCM, `count14` Eco5); future emulator must honor the controller's actual request.
- Safety model: maintain current local page cache, mutate one locally proven target only, never fabricate unchanged context, and require matching controller FC16 confirmation.

## EXPERIMENT_LOG.md — proposed entry

### PROTO-OFFLINE-10 — COMPLETE / POSITIVE — desired-state command reconstruction

**Hypothesis:** native Online commands are page-level read/modify/return transactions where the DCM returns a full desired page with one target mutation, followed by controller FC16 result publication.

**Controlled change:** offline-only analysis of all six non-zero-W1 desired-state transactions in the six genuine Online/DCM captures. No device TX, YAML change, reboot, or setting write.

**Observed:**
- 6 command-pull events total: 4×`03E8`, 2×`042E`.
- 4/4 fully bracketed Eco5 commands change exactly one word from the previous controller page.
- 4/4 subsequent controller FC16 pages exactly equal the desired FC03 response.
- `03F4` A/B/A: `20 -> 30 -> 20`, with independent `B3C5` propagation.
- `042F`: `1 -> 0`; `042E`: `1 -> 0`.
- desired-response -> controller-result latency ~491–571 ms on Eco5.
- older `03E8/count13` desired snapshots differ only in page word0.

**Result:** COMPLETE / POSITIVE.

## PROTOCOL_FINDINGS.md — proposed durable updates

### PROVEN / genuine Eco5 Online

Native desired-state page transaction:

```text
0708 W1 page bit
 -> controller FC03 desired-page read
 -> DCM full page image
 -> controller FC16 result page
```

In all four fully bracketed Eco5 examples, the DCM desired image is the last/current controller image with exactly one target word changed, and the result page exactly equals the desired page.

### PROVEN / semantic propagation

For `03E8` page:

```text
03F4: 20 -> 30 -> 20
B3C5: 20 -> 30 -> 20
```

This independently confirms controller adoption of the native desired-state command.

### PROVEN / structural

`042E` group commands:
- one desired transaction changes `042F: 1 -> 0`;
- next changes `042E: 1 -> 0`;
- both are republished exactly by controller FC16.

### STRONGLY SUPPORTED

- Safe DCM emulation requires coherent page caching and read-modify-return behavior.
- FC16 result publication functions as a strong confirmation image.
- Only the target word should be deliberately changed; unchanged page context should come from the most recent local controller image.

### OPEN

- exact meaning of `042F`;
- controller rejection/clamping semantics;
- whether unchanged context fields are validated or merely carried;
- desired bits beyond observed W1 bits0 and3;
- W0 desired-page behavior.

### Safety

Do not synthesize full desired pages from external-model defaults.
Do not use Eco5/older counts blindly on XTR.
For any future active test, answer the controller's actual FC03 request shape and mutate only one locally known target from the current local page cache.