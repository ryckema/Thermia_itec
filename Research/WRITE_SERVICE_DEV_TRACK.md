# Write Service Development — XTR M

**Status (2026-11-04):** **SOURCE / OFFLINE TESTED; PREPARED / NOT RUN** for Service DEV S0. Private full ESPHome YAML is derived from W2R93 (itself W2R92 + 36 change-only calendar API text filters); source delta to W2R93 is two comment lines and a distinct `Thermia Firmware Build` label only.

- Source snapshot SHA256: `765b9adb6ea0099bfaaab18e47452ebfdb9dabeee739f09d189a4d0a3394160b`.
- Private package: `Thermia_XTR_WRITE_USER_SERVICE_SPLIT_PRIVATE_20261104.zip`, member `WRITE_SERVICE_DEV/Thermia_WRITE_SERVICE_DEV_S0.yaml`.
- This S0 baseline **DOES NOT implement or enable any new SERVICE parameter writes**. It preserves all working User features and sole original S92 engine/ABORT/FC03/FC16 semantic control, with no second UART or TX owner.
- For further Service functions: define actual XTR menu parameter, OEM genuine source register/page/units/range; classify safety interlocks and configured accessories; create a source-backed descriptor inside the existing native S92 writer, disabled by default; only a user-initiated bounded physical test can permit the novel TX, with authoritative controller readback and ABORT/rollback.
- Keep user release branch `xtr-write-user-stable` pinned to W2R92; backport only tested common bugs; no automatic merge of unverified Service code into User.
- Do not publish genuine protected firmware code, proprietary handshake, `0x0708` tooling or `0x0F` emulation; research and non-sensitive metadata only.
- Service user interface and model-dependent features are not claimed to exist before implementation. User can run at most one chosen firmware variant per physical ESP32 bus.
- Do not edit `README.md` or `Write (Beta)/iTec Eco`.

**ONE NEXT ACTION:** inventory actual XTR service-menu parameter sources and implement the first meaningful read-only or safely guarded service descriptor in the existing native owner, without disturbing W2R92 User Stable.
