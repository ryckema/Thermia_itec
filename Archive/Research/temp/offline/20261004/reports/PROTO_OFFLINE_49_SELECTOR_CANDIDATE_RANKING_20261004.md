# PROTO-OFFLINE-49 — Desired-selector candidate ranking

**Date:** 2026-10-04  
**Status:** **COMPLETE / POSITIVE AS A PRIORITIZATION ARTIFACT; NO NEW SELECTOR PROOF**  
**Hypothesis:** existing page geometry, genuine/local selector provenance, ABI stability and safety constraints can rank unobserved selector bits for future research without promoting any inferred mapping to fact.  
**Controlled change:** offline scoring only. No selector is transmitted.

## Proven selector baseline

Current proof remains:

- `W1 bit0 -> 03E8`: genuine + local XTR;
- `W1 bit3 -> 042E`: genuine + local XTR;
- `W1 bit4 -> 0442`: local XTR only;
- `W0 bit0 -> 0546`: genuine ATEC + local XTR;
- `W0 bit1 -> 055A`: local XTR only.

All other bits remain **UNPROVEN / DENY-BY-DEFAULT**.

## Ranking result

The scoring deliberately rewards:

- low-half W1 candidates because more W1 desired behavior is genuinely observed;
- stable/local-known page geometry;

and penalizes:

- calendar transport pages;
- concrete-drying pages;
- service/SG pages;
- terminal/tail pages.

### Tier A — highest information yield if a future bounded selector experiment is ever justified

W1b1→03FC, W1b2→0410, W1b5→0456, W1b6→046A, W1b7→047E, W1b8→0492, W1b10→04BA, W1b12→04F6, W1b13→050A, W1b14→051E, W1b15→0532

### Tier B — secondary

W1b9→04A6

High-half calendar bits are intentionally pushed to the bottom because the genuine corpus still contains **no calendar FC03 desired-page pull**, and calendar logical records can cross physical native page boundaries.

## Important interpretation

This ranking is **not protocol proof**.

A high score means only “if we later choose one tightly bounded active selector-discovery test, this page gives relatively high information value for comparatively fewer unknowns.”

It does **not** authorize:

- asserting the bit;
- responding to a resulting FC03;
- modifying a page payload;
- writing any unknown register.

Any future live selector test still needs its own experiment number, exact current page, mapping source, expected effect, abort criteria and one-variable safety plan.

## Result

No previously unobserved W0/W1 bit is promoted.

The ranking mainly confirms that the remaining low-half W1 pages are scientifically preferable to calendar/high-half exploration, while `04D8` and calendar pages should remain near the bottom of the active-test queue.

## Live status

Unchanged.