# CM930 Universal development history

## 0.1.0-beta.1 — planned, not published as firmware

### dev012 — beta cleanup
**SOURCE / OFFLINE TESTED — PREPARED / NOT RUN.**

- Build-time model-specific entity visibility and duplicate-sensor defaults.
- Existing entity IDs and names retained for dashboard compatibility.
- Reduced repeated installation-selection status messages and restricted raw diagnostic output.
- Consistent beta candidate build identification.
- No intended changes to the previously verified session engine or native control permissions.

Not target-compiled or live-tested. Existing Home Assistant entity registry settings may override presentation defaults.

### dev011 — automatic session
**TARGET COMPILED / FLASHED / LIVE / LOCALLY VERIFIED** for the XTR M 3N / CM930 2.4.2 retained-session OTA recovery scope. **COMPLETE / POSITIVE**, 27 November 2026.

- Reuses the previously saved installation choice.
- Automatically restores the native session and synchronizes current configuration.
- Restores existing user-control readiness after controller-confirmed current data.
- Automatic alarm and hot-water configuration refresh observed.
- No semantic parameter write tested in this capture; no new controller cold-start or other-model native qualification established.

### dev010 — automatic profile
**COMPLETE / POSITIVE** for XTR installation confirmation and automatic retained-session recovery after ESP reboot.

This history documents private development milestones. It does not imply a public firmware release or compatibility beyond the stated evidence.
