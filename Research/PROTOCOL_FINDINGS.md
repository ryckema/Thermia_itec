# THERMIA PROTOCOL FINDINGS

Last updated: 2026-10-28. This public summary excludes confidential OEM firmware-derived code, algorithms, credentials, mailbox tooling and raw sensitive captures.

## Controller-semantic Heating write verification — LIVE / LOCALLY VERIFIED

On iTec XTR M 3N controller 2.4.2, W2R25F4 user-initiated direct HA changes to Heating `0x03E8` 14-word page were each followed by controller-origin FC16 readback that included the desired selected register. This is semantic confirmation, not merely a transport ACK.

- D1 03E8, word0, heating curve: live verified repeated writes.
- D4 03E9, word1, heating minimum: live verified multiple writes, including **10 °C** (within the OEM 10–50 range for the applicable controller profile).
- D7 03EC, word4, signed curve correction 0: `1→0xFFFE→0`, controller accepted and Home Assistant reflected signed -2.
- D8 03ED, word5, signed curve correction -5: `1→0xFFFF→0`, controller accepted and HA reflected signed -1.
- D9 03EE, word6, heating stop: repeated writes `20→15→20→18→15→17` accepted (OEM profile 0–30).
- D10 03EF, word7, reduced temperature: `20→22→20` accepted.
- D11 03F0, word8, room factor: `2→1` accepted.
- D5 03EA, word2, Heating Maximum: **sole remaining unverified Heating descriptor**, no physical user write or controller readback in either supplied capture.\n- D6 03EB, word3, correction +5 °C: **0→1→0→1**; all three new user edits accepted via controller-origin FC16 in the second capture.\n- D12 03F4, word12, Room Setpoint: **22→21→22**; both new user edits accepted via controller-origin FC16 in the second capture.

The Heating desired payload was one 14-word page derived from the latest suitable same-epoch controller snapshot, with only the user-selected word intentionally changed. Across two real XTR captures, all **26** user-initiated physical edits had one delivered page and matching controller acceptance (19 first capture, 7 second). Runtime CURRENT 4/4 and automatic calendar 12/12 continued to work; V5 CRC integrity sample counters remained clean. An overlapping write was denied with idle=0, NO_TX. The native owner and collision/CRC safeguards remain required.

## OEM comparison and remaining uncertainty

Original Thermia Connect's per-register pending updates and controller-value comparison are consistent with the observed successful XTR semantic readback. OEM automatic retry behavior has **not** been replicated and must not be inferred from these successes. No proof here of arbitrary untested register groups, controller online state, or general authorization for autonomous parameter transmissions. Only D5 Heating Maximum still requires its own live semantic readback. In the second log, CURRENT 4/4 was confirmed and sample CRC/RX/resync counters were zero; calendar 12/12 was merely armed for reread, not independently completed in that second excerpt.

**ONE NEXT ACTION:** One user-run D5 `03EA` Heating Maximum write and genuine controller-origin FC16 readback on unchanged W2R25F4; preserve all TX guards and rollback.
