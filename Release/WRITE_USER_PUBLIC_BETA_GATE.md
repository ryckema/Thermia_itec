# Thermia iTec XTR M — Write User Public Beta release gate

**Date:** 2026-11-09  
**Public firmware release status:** **NO-GO — source not cleared for redistribution.**  
**Private owner installation:** **GO — RC09FC remains untouched and locally verified.**

This file documents the release decision; it is **not installable firmware** and does **not** authorize hardware transmission. Do not attach the private RC09FC ZIP or YAML to this public branch, a public PR, or a GitHub Release.

## One concrete blocker: authenticated session ownership without protected replay

The public file `Thermia iTec XTR/thermia_itec_xtr_DCM_readonly_1.0.yaml` already includes the historical `R1` / EXP374-style **single-capture FC23 replay**. It compares one complete, CRC-bearing recorded request with the incoming request and sends a recorded response **only on an exact match**. It is not a reusable universal “R key”, an implementation of the general challenge algorithm, or evidence that new controllers allow authenticated Write User operation without a challenge/response. **Do not reproduce its embedded recorded request or reply in another public release.**

A separate C5DF native *transport* scope can answer bounded read-only requests from a qualified controller context without establishing full application-level acceptance. This is helpful for **read-only discovery** but **not proof of permission to write user settings**, and no second master/parallel session owner may be introduced to force it.

The existing publicly named **DCM_readonly** file itself requires a provenance and release audit because it contains recorded challenge/response material and TX-capable native session code. “Read Only” is not equivalent to “RX only”; unlike the separate passive build, it can transmit requests/acknowledgements. Historical published content may remain in Git history even after replacement. Do not distribute these data again under the repository's MIT license without independent source and rights review.

## Verified local feature set (private XTR M / CM930 2.4.2 only)

The private RC09FC source (SHA256 `651e056df9d52d028af75b944fe8ce030cdebadf2a377c62c53880efab7367cd`) was ESPHome-target-compiled, owner-flashed, and locally observed: M6 native session, CURRENT 4/4, calendar 12/12, real-controller FC16 alarms 085F/5 with stale-to-fresh HA handling, V5 CRC0/drops0 in captured runtime. Direct TOP-UP had a separately proven bounded physical dispatch in RC09FB and user-confirmed DHW initiation; latest native 0864 status on that dispatch was inconclusive. This is **local single-device evidence**, not permission or proof for arbitrary installations.

## Public beta constraints

1. A public **source-only, independently authored** engine must establish legitimate session ownership or operate strictly receive-only/read-only within proven scope; no recorded OEM challenge/reply, extracted cipher/algorithm, private firmware blobs, proprietary tooling or secrets.
2. One UART/RX/TX/DE owner, controller-origin CRC/FC16 semantic readback, cold/rejoin protections, ABORT/rollback and user-initiated bounded authorization must remain. No authentication or controller interlocks may be bypassed.
3. Routine HA settings writes: expose **only controller-locally verified descriptors**. The 32-slot calendar write interface and all unvalidated domains remain disabled/experimental until independently confirmed. Separate read-only calendar display is not a blanket write authorization.
4. Existing user HA entities must not be silently broken or relabeled as tested when only source-level coverage exists. Build and release candidate must pass ESPHome target compilation and distinct owner-live validation. Other XTR/XT/ATEC/Eco models not claimed compatible.
5. README.md and `Write (Beta)/iTec Eco` are owner-protected and must **not be edited** by this release preparation. Public installation documentation must eventually be reconciled by the owner.

## Release status and next engineering action

**PRIVATE RC09FC:** GO; do not change/reflash solely for release work.  
**PUBLIC Write User Beta:** NO-GO; do not publish a firmware ZIP, public flash instructions, release tag or secret.  
**REAL BLOCKER:** no independently releasable implementation currently establishes the authenticated Write User owner/session on a clean XTR startup; the exact historical R1 replay cannot be assumed portable.

**ONE NEXT ACTION:** independently implement a *non-secret, evidence-based native session acquisition strategy* in an isolated public-source candidate, with HA writes disabled until the same XTR controller authoritatively confirms owner semantics. If it requires protected response material, the public release stays NO-GO; the already validated private build is not a publication source.

## Security and validation

Run the adjacent `public_release_gate.py` against a candidate YAML **locally**, not in GitHub Actions against private files. Fail-closed matches are pointers for human review, not proof that a file is legally or electrically safe. A PASS_STATIC_ONLY result **never authorizes a public firmware release**.
