# PROTO-OFFLINE-47 — Cross-profile page ABI alignment

**Date:** 2026-10-04  
**Status:** **COMPLETE / POSITIVE**  
**Hypothesis:** aligning the same native page indices across legacy A5/Online, ATEC/DCM03, modern Eco5 and local XTR can separate stable absolute-register structure from profile ABI drift and can narrow the unresolved local-XTR fields without assigning unsupported semantics.  
**Controlled change:** offline-only page/count/value alignment. No TX, no YAML change, no live experiment advancement.

## Corpus and provenance

- genuine legacy A5/Online captures;
- genuine ATEC + classic DCM03 cold-start capture;
- genuine modern Eco5 Online captures;
- local XTR passive `03E8/count14` trace;
- local XTR page counts from current Write Beta v4.1 are used only as local geometry evidence.

## Page geometry result

Across the 32 native configuration-page indices:

- **27 pages** have the same count across legacy/ATEC/Eco5/local-XTR geometry;
- **4 pages** show a clean two-family split where legacy+ATEC agree and Eco5+local-XTR agree;
- the clean split pages are: **03E8, 0410, 0492, 051E**.

The four strongest ABI split markers are:

- `03E8`: legacy/ATEC count13 vs Eco5/XTR count14;
- `0410`: 21 vs 22;
- `0492`: 9 vs 11;
- `051E`: 9 vs 10.

This independently reinforces that the local XTR configuration ABI belongs on the **modern Eco5 side** for these page geometries, even though semantics must still be proven locally register-by-register.

## New local-XTR narrowing

### `03F3`

Observed values:

- legacy: `60`;
- ATEC: `60`;
- Eco5: `1`;
- **local XTR passive trace: `1` in 70/70 observed `03E8` pages**.

**Strong conclusion:** `03F3` is not merely a generic cross-model drift marker; the local XTR explicitly shares the modern Eco5 representation at this address. The semantic name remains **OPEN**.

### `03F5`

`03F5` is physically absent from the legacy/ATEC `03E8/count13` page.

It is present in:

- Eco5 `03E8/count14`: `2`;
- **local XTR `03E8/count14`: `2` in 70/70 observed pages**.

**PROVEN structural / local XTR:** `03F5` is a real modern-page extension on this XTR.  
**OPEN:** semantic meaning.

### `03F1` / `03F2`

Across all compared profiles including the local XTR:

- `03F1 = 40`;
- `03F2 = 30`.

That makes both unusually stable structural fields, but there is still no labelled edge. `03F1=HotWaterStart` remains disproven locally; neither field receives a semantic promotion.

### `0431`, `0432`, `0447`

ATEC reproduces the legacy values (`12`, `60`, `35`), while Eco5 uses (`20`, `-10`, `-8`). The current raw local-XTR corpus does not contain those pages, so the XTR side cannot be assigned from this experiment.

## Strong conclusions

1. ATEC/DCM03 is ABI-aligned with the older legacy family for the known count-drift pages.
2. The local XTR is ABI-aligned with modern Eco5 at least for `03E8`, `0410`, `0492`, and `051E` page geometry.
3. The local XTR **directly** shares Eco5 values for the modern-only `03F3/03F5` pattern.
4. Same numeric register remains insufficient for semantic portability; `042E` already proves that semantics can differ despite stable address/count.

## Unknowns

- semantic identities of `03F1/03F2/03F3/03F5`;
- local-XTR values for `0431/0432/0447` in the current raw corpus;
- whether every modern Eco5 semantic is portable to XTR.

## Live status

Unchanged: EXP387 COMPLETE / POSITIVE; EXP388 RUNNING / PARTIAL; EXP383 PREPARED / NOT RUN.