# Continuity and documentation workflow

## Purpose
Make research reproducible when ChatGPT chat history is missing. **START_HERE.md is the short entry point; canonical files preserve the actual evidence.** The handoff snapshot is dated and may become stale.

## Source map
| Need | Read |
|---|---|
| Fast new-chat orientation | [START_HERE.md](START_HERE.md) |
| Authoritative experiment state | [THERMIA_PROJECT_STATE.md](THERMIA_PROJECT_STATE.md) |
| Full chronological experiments | [EXPERIMENT_LOG.md](EXPERIMENT_LOG.md) |
| Provenance/confidence of protocol claims | [PROTOCOL_FINDINGS.md](PROTOCOL_FINDINGS.md) |
| Detailed V5 native DCM work | [V5DCM/](V5DCM/) |
| Actual firmware/reference implementation | [Thermia_Connect_Firmware](https://github.com/ryckema/Thermia_Connect_Firmware) |
| Production monitor vs guarded write builds | [repository root README](../README.md) |

## Required workflow
**Before work:** inspect START_HERE, verify most recent canonical entries and GitHub commits, find related experiments and exact baseline. Do not assume this handoff outranks newer raw evidence.

**Preparing:** ID, hypothesis, controlled change, tested baseline/commit or YAML provenance, expected positive/negative/inconclusive results, abort/rollback, required log. Mark PREPARED / NOT RUN.

**Reviewing:** distinguish observed facts from conclusions, hypotheses and unknowns; label local XTR vs DCM capture vs firmware vs cross-model. Only mark COMPLETE on actual supplied result/confirmation; preserve partial and negative outcomes.

**Saving:** update the canonical project state, append linked PREPARED/RESULT history without deleting earlier evidence, reconcile findings, refresh START_HERE; verify GitHub writes/commits. When writes fail, explicitly say nothing was saved.

**Safety:** TX/emulation research is authorized in principle; actual potentially disruptive live actions must belong to a clearly scoped user-initiated test with fail-closed timing, abort and rollback. Current RX-only/TX HARD_DENY status stays until a new proven deployment says otherwise.

## Reduce growth without losing history
Current canonical markdown files exceed 500 KB individually and accumulate dated status headers. A later *separate audited migration* should:
1. Create an immutable dated archive snapshot of each original file.
2. Build an experiment ID index linking reports and archive offsets/sections.
3. Reduce the live PROJECT_STATE to a single short current snapshot; keep EXPERIMENT_LOG as searchable history or partition by stable experiment families.
4. Validate all existing links and counts against the archive before replacing files.
5. Commit reversible changes separately, with a migration manifest and checksums.

**Do not truncate, rewrite, delete or relocate historical evidence in this initial navigation-only reorganization.**
