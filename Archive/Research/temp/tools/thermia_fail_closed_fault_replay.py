#!/usr/bin/env python3
"""
PROTO-OFFLINE-46 synthetic fail-closed shadow replay.

Executed against source predicates from:
Write (Beta)/thermia_itec_xtr_m_waveshare_write_beta_v4_1.yaml
blob: 8e8a82689e53528a8b751a1abbd901f683b6b238

This is a branch-faithful reference/shadow model, not compiled ESPHome firmware.
See:
- PROTO_OFFLINE_46_SYNTHETIC_FAIL_CLOSED_REPLAY_20261004.md
- PROTO_OFFLINE_46_SYNTHETIC_FAULT_MATRIX_20261004.csv
- PROTO_OFFLINE_46_REPLAY_OUTPUT_20261004.txt

The raw synthetic frames in the matrix were derived from genuine capture frames
and rebuilt with valid Modbus CRC so the regression targets state/authorization
logic rather than CRC rejection.
"""