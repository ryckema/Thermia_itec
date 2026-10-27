# V5 Native Service-27 — source-pinned profile admission

Date: 2026-10-20. Offline source/host integration COMPLETE / POSITIVE; on-device test PREPARED / NOT RUN.

Existing Service-26 V5 + XTR V4.1 private gateway source retained. One new profile declaration and admission adapter requires an explicit source-reviewed XTR provenance, session epoch, version, exact significant-group list and page geometry before installing a profile. External ATEC, unknown provenance, duplicate groups, excessive group lengths, geometry collisions, wrong W4 size and stale epoch are rejected. No automatic inferred XTR profile from 0867 raw value; a caller-supplied reviewed flag is NOT independent identity authentication or a physical authorization.

30/30 C++17 host tests PASS, including two synthetic FakeIo TX test runs. No firmware compilation, physical TX, flash or new XTR semantic result. Original V83 FAS1 RX-only remains user-verified unchanged, TX HARD_DENY; B11D issue OPEN and EXP388 RUNNING/PARTIAL. The actual device-specific significant register list is still unknown, so live profile selection is not claimed complete.

Private archive SHA256 2c119251376d5b6be6240a54b6ecd52c1dd10bbbd5bb0d4bf2da52ff6e3c4074; private source not uploaded. Next: source-pin genuine local XTR version/profile required groups, then bind a reviewed declaration into the same merged engine, without inventing model identity or copying protected firmware/ATEC implementation.
