# PROTO-OFFLINE-54 — Golden-trace regression suite

**Date:** 2026-10-04  
**Status:** **COMPLETE / POSITIVE**  
**Hypothesis:** the genuine/reference capture corpus can be converted into deterministic golden assertions so future parser/state-model changes cannot silently alter already-established protocol evidence.  
**Controlled change:** offline test harness only. No bus TX, no YAML behavior change, no compile/flash.

## Corpus

Golden fixtures:

- 4 legacy A5/Online captures;
- 2 modern Eco5 Online captures;
- 1 ATEC + DCM03 cold-start capture;
- 1 local passive XTR trace.

## Executed regression

The suite executed **72 exact assertions**.

**Result: 72/72 PASS.**

The assertions pin:

- zero 0x0F CRC failures in genuine fixtures;
- complete bootstrap counts (Eco5 2 + 4, ATEC 1);
- one known partial legacy bootstrap;
- exact approval challenge/accept counts;
- desired-pull counts and four Eco5 confirmations;
- the one legacy `0870` recovery/rejoin window;
- per-capture `085F` ACK populations;
- per-capture `0834` ACK populations;
- steady runtime-group counts;
- PROTO45's approval/config overlap cases;
- the genuine ATEC steady-runtime `085F` ACK;
- two genuine standalone legacy `03E8` pushes;
- local passive XTR fail-closed fixture: no answered 0708, 70 unACKed `03E8`, 35 unACKed `085F`.

## What this gives us

This is now a reproducible **evidence regression layer**.

If the parser or state-model tooling changes later, a deviation from one of these counts has to be explained explicitly rather than silently changing the project model.

This is especially useful before any future Write Beta refactor: the evidence model can be run first, independently from live hardware.

## What it does not prove

- It does not execute ESPHome YAML.
- It does not prove TX timing.
- It does not mean every exact count is a universal Thermia rule; the assertions are golden properties of these specific fixtures.
- A new genuine capture may legitimately add a new state and require a reviewed golden update.

## Strong conclusion

The current offline evidence corpus is now suitable as a deterministic regression fixture, not just a collection of manually interpreted logs.

## Live status

Unchanged: EXP387 COMPLETE / POSITIVE; EXP388 RUNNING / PARTIAL; EXP383 PREPARED / NOT RUN.